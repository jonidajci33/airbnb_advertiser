"""
Skill: Airbnb Data Loader
Parses Airbnb transaction CSV exports, pairs Payout rows with Reservation rows
to compute EUR amounts, and normalizes into the unified schema.
"""

import csv
import glob
import os
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
AIRBNB_DIR = PROJECT_ROOT / "Monthly bills" / "AirBnb"


def _parse_date(date_str):
    """Parse a date string into a date object, trying multiple formats."""
    if not date_str or not date_str.strip():
        return None
    date_str = date_str.strip()
    for fmt in ["%m/%d/%Y", "%Y-%m-%d", "%d/%m/%Y"]:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue
    return None


def _parse_float(value):
    """Safely parse a float, handling commas and currency symbols."""
    if not value:
        return 0.0
    try:
        cleaned = str(value).strip().replace(",", "").replace("$", "").replace("EUR", "").strip()
        return float(cleaned) if cleaned else 0.0
    except (ValueError, AttributeError):
        return 0.0


def load_reservations():
    """
    Load all Airbnb CSV files and return normalized data.
    Pairs Payout rows (EUR amounts) with their Reservation rows (USD amounts)
    to compute EUR gross, fees, and net for each reservation.

    Returns:
        dict with keys:
            - reservations: list of normalized reservation dicts
            - summary: dict with totals
            - issues: list of issues/warnings found
    """
    pattern = str(AIRBNB_DIR / "*.csv")
    csv_files = sorted(glob.glob(pattern))

    if not csv_files:
        return {
            "reservations": [],
            "summary": {},
            "issues": [{
                "severity": "MEDIUM",
                "message": (
                    "No Airbnb CSV files found in Monthly bills/AirBnb/. "
                    "To export: Airbnb > Professional Hosting > Earnings > "
                    "Transaction History > Export CSV. Place the file in Monthly bills/AirBnb/"
                ),
            }],
        }

    reservations = []
    issues = []

    for filepath in csv_files:
        filename = os.path.basename(filepath)
        try:
            rows = _read_csv(filepath)
            parsed = _pair_payouts_and_reservations(rows)
            reservations.extend(parsed)
        except Exception as e:
            issues.append({"severity": "HIGH", "message": f"Error reading {filename}: {str(e)}"})

    if not reservations:
        issues.append({"severity": "MEDIUM", "message": "Airbnb CSV files found but no reservation data extracted."})

    # Summary
    months_found = sorted(set(r["month_key"] for r in reservations if r["month_key"] != "unknown"))
    total_gross_eur = sum(r["gross_eur"] for r in reservations)
    total_fees_eur = sum(r["commission_eur"] for r in reservations)
    total_net_eur = sum(r["net_eur"] for r in reservations)

    summary = {
        "total_reservations": len(reservations),
        "revenue_reservations": len(reservations),
        "cancelled_reservations": 0,
        "total_room_nights": sum(r["room_nights"] for r in reservations),
        "total_gross_usd": round(sum(r["gross_usd"] for r in reservations), 2),
        "total_fees_usd": round(sum(r["fee_usd"] for r in reservations), 2),
        "total_net_usd": round(sum(r["net_usd"] for r in reservations), 2),
        "total_gross_eur": round(total_gross_eur, 2),
        "total_commission_eur": round(total_fees_eur, 2),
        "total_net_eur": round(total_net_eur, 2),
        "currency": "EUR",
        "months_covered": months_found,
        "csv_files_loaded": len(csv_files),
    }

    return {
        "reservations": reservations,
        "summary": summary,
        "issues": issues,
    }


def _read_csv(filepath):
    """Read CSV and return all rows as list of dicts."""
    rows = []
    with open(filepath, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def _pair_payouts_and_reservations(rows):
    """
    Walk through rows and pair each Payout with its subsequent Reservation(s).
    The Airbnb CSV format puts a Payout row above the Reservation(s) it covers.
    """
    reservations = []
    current_payout = None
    payout_reservations = []

    for row in rows:
        row_type = row.get("Type", "").strip()

        if row_type == "Payout":
            # Flush any previous payout group
            if current_payout and payout_reservations:
                _assign_eur_amounts(current_payout, payout_reservations)
                reservations.extend(payout_reservations)

            # Start new payout group
            paid_out = _parse_float(row.get("Paid out", "0"))
            payout_currency = row.get("Currency", "").strip()
            # Some payouts are in USD (bank transfer), some in EUR (Payoneer)
            current_payout = {
                "paid_out": paid_out,
                "currency": payout_currency,
            }
            payout_reservations = []

        elif row_type == "Reservation":
            start_date = _parse_date(row.get("Start date", ""))
            end_date = _parse_date(row.get("End date", ""))
            nights = 0
            nights_str = row.get("Nights", "")
            if nights_str:
                try:
                    nights = int(nights_str)
                except ValueError:
                    nights = 0
            gross = _parse_float(row.get("Gross earnings", "0"))
            fee = _parse_float(row.get("Service fee", "0"))
            amount = _parse_float(row.get("Amount", "0"))

            if start_date:
                month_key = start_date.strftime("%Y-%m")
            else:
                month_key = "unknown"

            parsed = {
                "platform": "Airbnb",
                "reservation_number": row.get("Confirmation code", "").strip(),
                "arrival": start_date.isoformat() if start_date else None,
                "departure": end_date.isoformat() if end_date else None,
                "guest_name": row.get("Guest", "").strip(),
                "room_nights": nights,
                "gross_usd": round(gross, 2),
                "fee_usd": round(abs(fee), 2),
                "net_usd": round(amount, 2),
                # EUR amounts will be filled in by _assign_eur_amounts
                "gross_eur": 0.0,
                "commission_eur": 0.0,
                "net_eur": 0.0,
                "exchange_rate": 0.0,
                "status": "OK",
                "has_revenue": True,
                "currency": "EUR",
                "month_key": month_key,
                "file_month_key": month_key,
                "booked_on": row.get("Booking date", "").strip(),
                "persons": 0,
            }
            payout_reservations.append(parsed)

    # Flush last group
    if current_payout and payout_reservations:
        _assign_eur_amounts(current_payout, payout_reservations)
        reservations.extend(payout_reservations)

    return reservations


def _assign_eur_amounts(payout, reservation_list):
    """
    Distribute the EUR payout amount across the reservation(s) it covers,
    proportional to each reservation's USD net amount.
    """
    paid_out = payout["paid_out"]
    payout_currency = payout["currency"]

    total_net_usd = sum(r["net_usd"] for r in reservation_list)

    if total_net_usd <= 0 or paid_out <= 0:
        return

    if payout_currency == "EUR":
        # EUR payout - compute exchange rate from total USD -> EUR
        rate = total_net_usd / paid_out  # USD per EUR
        for r in reservation_list:
            proportion = r["net_usd"] / total_net_usd if total_net_usd > 0 else 0
            r["net_eur"] = round(paid_out * proportion, 2)
            r["exchange_rate"] = round(rate, 4)
            # Derive gross and fee in EUR using the same rate
            r["gross_eur"] = round(r["gross_usd"] / rate, 2) if rate > 0 else 0.0
            r["commission_eur"] = round(r["fee_usd"] / rate, 2) if rate > 0 else 0.0
    else:
        # USD payout (rare - bank transfer in USD)
        # Use a fallback EUR/USD rate of ~0.92
        fallback_rate = 1.08  # USD per EUR
        for r in reservation_list:
            r["net_eur"] = round(r["net_usd"] / fallback_rate, 2)
            r["gross_eur"] = round(r["gross_usd"] / fallback_rate, 2)
            r["commission_eur"] = round(r["fee_usd"] / fallback_rate, 2)
            r["exchange_rate"] = round(fallback_rate, 4)


if __name__ == "__main__":
    result = load_reservations()
    s = result["summary"]
    print(f"\nAirbnb Data Loader")
    print(f"{'=' * 55}")
    print(f"  CSV files loaded:      {s.get('csv_files_loaded', 0)}")
    print(f"  Total reservations:    {s.get('total_reservations', 0)}")
    print(f"  Total room nights:     {s.get('total_room_nights', 0)}")
    print(f"  Gross (USD):           ${s.get('total_gross_usd', 0):,.2f}")
    print(f"  Fees (USD):            ${s.get('total_fees_usd', 0):,.2f}")
    print(f"  Net (USD):             ${s.get('total_net_usd', 0):,.2f}")
    print(f"  Gross (EUR):           EUR {s.get('total_gross_eur', 0):,.2f}")
    print(f"  Fees (EUR):            EUR {s.get('total_commission_eur', 0):,.2f}")
    print(f"  Net (EUR):             EUR {s.get('total_net_eur', 0):,.2f}")
    print(f"  Months covered:        {', '.join(s.get('months_covered', []))}")
    if result["issues"]:
        print(f"\n  Issues:")
        for issue in result["issues"]:
            print(f"    [{issue['severity']}] {issue['message']}")
    print()
