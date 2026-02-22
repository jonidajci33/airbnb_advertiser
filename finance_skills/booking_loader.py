"""
Skill: Booking.com Data Loader
Parses all Booking.com reservation statement CSVs and normalizes into a unified schema.
All amounts are in EUR (native currency from Booking.com).
"""

import csv
import glob
import os
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BOOKING_DIR = PROJECT_ROOT / "Monthly bills" / "Booking"


def _parse_date(date_str):
    """Parse a date string (YYYY-MM-DD) into a date object."""
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def _parse_float(value):
    """Safely parse a float from a string."""
    if not value:
        return 0.0
    try:
        return float(value.strip())
    except (ValueError, AttributeError):
        return 0.0


def _parse_int(value):
    """Safely parse an int from a string."""
    if not value:
        return 0
    try:
        return int(float(value.strip()))
    except (ValueError, AttributeError):
        return 0


def load_reservations():
    """
    Load all Booking.com reservation CSVs and return normalized data.

    Returns:
        dict with keys:
            - reservations: list of normalized reservation dicts
            - summary: dict with totals
            - issues: list of issues/warnings found
    """
    pattern = str(BOOKING_DIR / "reservation_statements_overview_*.csv")
    csv_files = sorted(glob.glob(pattern))

    if not csv_files:
        return {
            "reservations": [],
            "summary": {},
            "issues": [{"severity": "CRITICAL", "message": "No Booking.com CSV files found in Monthly bills/Booking/"}],
        }

    reservations = []
    issues = []
    months_found = set()
    cancelled_count = 0
    noshow_count = 0
    total_count = 0

    for filepath in csv_files:
        filename = os.path.basename(filepath)
        # Extract month key from filename: reservation_statements_overview_2024-01.csv -> 2024-01
        parts = filename.replace("reservation_statements_overview_", "").replace(".csv", "")
        file_month_key = parts.strip()
        months_found.add(file_month_key)

        try:
            with open(filepath, "r", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    total_count += 1
                    arrival = _parse_date(row.get("Arrival", ""))
                    departure = _parse_date(row.get("Departure", ""))
                    status = row.get("Status", "").strip().upper()
                    room_nights = _parse_int(row.get("Room nights", "0"))
                    original_amount = _parse_float(row.get("Original amount", "0"))
                    final_amount = _parse_float(row.get("Final amount", "0"))
                    commission_amount = _parse_float(row.get("Commission amount", "0"))
                    commission_pct = _parse_float(row.get("Commission %", "0"))

                    # Determine if this reservation earned revenue
                    # CANCELLED with final_amount=0 -> no revenue
                    # NO_SHOW with final_amount>0 -> chargeable, counts as revenue
                    # NO_SHOW with final_amount=0 -> no revenue
                    has_revenue = final_amount > 0

                    if status == "CANCELLED":
                        cancelled_count += 1
                    elif status == "NO_SHOW":
                        noshow_count += 1

                    # Month key based on arrival date (when the stay happened)
                    if arrival:
                        month_key = arrival.strftime("%Y-%m")
                    else:
                        month_key = file_month_key

                    net_amount = round(final_amount - commission_amount, 2) if has_revenue else 0.0

                    reservation = {
                        "platform": "Booking.com",
                        "reservation_number": row.get("Reservation number", "").strip(),
                        "arrival": arrival.isoformat() if arrival else None,
                        "departure": departure.isoformat() if departure else None,
                        "guest_name": row.get("Guest name", "").strip(),
                        "room_nights": room_nights,
                        "original_amount_eur": original_amount,
                        "gross_eur": final_amount,
                        "commission_eur": commission_amount,
                        "net_eur": net_amount,
                        "commission_pct": commission_pct,
                        "status": status if status in ("OK", "CANCELLED", "NO_SHOW") else "OK",
                        "has_revenue": has_revenue,
                        "currency": "EUR",
                        "month_key": month_key,
                        "file_month_key": file_month_key,
                        "booked_on": row.get("Booked on", "").strip(),
                        "persons": _parse_int(row.get("Persons", "0")),
                    }
                    reservations.append(reservation)

        except Exception as e:
            issues.append({"severity": "HIGH", "message": f"Error reading {filename}: {str(e)}"})

    # Check for high cancellation rate
    if total_count > 0:
        cancel_rate = (cancelled_count + noshow_count) / total_count * 100
        if cancel_rate > 20:
            issues.append({
                "severity": "HIGH",
                "message": f"High cancellation/no-show rate: {cancel_rate:.1f}% ({cancelled_count} cancelled + {noshow_count} no-show out of {total_count})",
            })

    # Check for missing months in range
    if months_found:
        first_month = min(months_found)
        last_month = max(months_found)
        all_months = set()
        start_y, start_m = int(first_month[:4]), int(first_month[5:7])
        end_y, end_m = int(last_month[:4]), int(last_month[5:7])
        y, m = start_y, start_m
        while (y, m) <= (end_y, end_m):
            all_months.add(f"{y}-{m:02d}")
            m += 1
            if m > 12:
                m = 1
                y += 1
        missing = sorted(all_months - months_found)
        if missing:
            issues.append({
                "severity": "MEDIUM",
                "message": f"Missing Booking.com CSV for: {', '.join(missing)}",
            })

    # Compute summary
    rev_reservations = [r for r in reservations if r["has_revenue"]]
    summary = {
        "total_reservations": total_count,
        "revenue_reservations": len(rev_reservations),
        "cancelled_reservations": cancelled_count,
        "noshow_reservations": noshow_count,
        "total_room_nights": sum(r["room_nights"] for r in rev_reservations),
        "total_gross_eur": round(sum(r["gross_eur"] for r in rev_reservations), 2),
        "total_commission_eur": round(sum(r["commission_eur"] for r in rev_reservations), 2),
        "total_net_eur": round(sum(r["net_eur"] for r in rev_reservations), 2),
        "currency": "EUR",
        "months_covered": sorted(months_found),
        "csv_files_loaded": len(csv_files),
    }

    return {
        "reservations": reservations,
        "summary": summary,
        "issues": issues,
    }


if __name__ == "__main__":
    result = load_reservations()
    s = result["summary"]
    print(f"\nBooking.com Data Loader")
    print(f"{'=' * 50}")
    print(f"  CSV files loaded:      {s.get('csv_files_loaded', 0)}")
    print(f"  Total reservations:    {s.get('total_reservations', 0)}")
    print(f"  Revenue reservations:  {s.get('revenue_reservations', 0)}")
    print(f"  Cancelled:             {s.get('cancelled_reservations', 0)}")
    print(f"  No-show:               {s.get('noshow_reservations', 0)}")
    print(f"  Total room nights:     {s.get('total_room_nights', 0)}")
    print(f"  Gross revenue:         EUR {s.get('total_gross_eur', 0):,.2f}")
    print(f"  Commission (expenses): EUR {s.get('total_commission_eur', 0):,.2f}")
    print(f"  Net revenue:           EUR {s.get('total_net_eur', 0):,.2f}")
    print(f"  Months covered:        {', '.join(s.get('months_covered', []))}")
    if result["issues"]:
        print(f"\n  Issues:")
        for issue in result["issues"]:
            print(f"    [{issue['severity']}] {issue['message']}")
    print()
