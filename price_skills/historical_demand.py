"""
Skill: Historical Demand Analysis
Analyzes reservation data to compute per-calendar-month demand patterns.
"""

import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from finance_skills.booking_loader import load_reservations as load_booking
from finance_skills.airbnb_loader import load_reservations as load_airbnb

# Calendar month names
MONTH_NAMES = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

# Days per calendar month (non-leap)
DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def analyze_demand():
    """
    Load all reservation data and compute per-calendar-month demand patterns.

    Returns:
        dict with keys:
            - monthly_patterns: dict[1-12] -> demand metrics
            - overall: overall averages
            - issues: list of warnings
    """
    # Load data from both platforms
    booking_data = load_booking()
    airbnb_data = load_airbnb()

    all_reservations = booking_data["reservations"] + airbnb_data["reservations"]
    ok_reservations = [r for r in all_reservations if r["status"] == "OK"]

    issues = []

    # Group by calendar month (1-12)
    month_buckets = defaultdict(lambda: {
        "room_nights": [], "revenues": [], "bookings": [],
        "stay_lengths": [], "year_months": set(),
    })

    for r in ok_reservations:
        mk = r["month_key"]
        if mk == "unknown":
            continue
        try:
            cal_month = int(mk[5:7])
        except (ValueError, IndexError):
            continue

        month_buckets[cal_month]["year_months"].add(mk)

    # We need monthly aggregates, so compute per year-month first, then average
    from finance_skills.financial_calculator import compute_metrics
    metrics = compute_metrics(booking_data["reservations"], airbnb_data["reservations"])

    # Group monthly metrics by calendar month
    cal_month_data = defaultdict(lambda: {
        "occupancies": [], "adrs": [],
        "room_nights": [], "bookings": [], "grosses": [],
        "years_seen": set(),
    })

    for mk, m in metrics["monthly"].items():
        try:
            cal_month = int(mk[5:7])
            year = int(mk[:4])
        except (ValueError, IndexError):
            continue

        cal_month_data[cal_month]["occupancies"].append(m["occupancy_pct"])
        cal_month_data[cal_month]["adrs"].append(m["adr"])
        cal_month_data[cal_month]["room_nights"].append(m["total_nights"])
        cal_month_data[cal_month]["bookings"].append(m["total_bookings"])
        cal_month_data[cal_month]["grosses"].append(m["total_gross"])
        cal_month_data[cal_month]["years_seen"].add(year)

    # Compute demand index (0-100) — normalize occupancy to 0-100 scale
    # based on max observed occupancy across all months
    all_occupancies = []
    for cm in range(1, 13):
        if cm in cal_month_data and cal_month_data[cm]["occupancies"]:
            all_occupancies.extend(cal_month_data[cm]["occupancies"])
    max_occ = max(all_occupancies) if all_occupancies else 100

    monthly_patterns = {}
    for cm in range(1, 13):
        data = cal_month_data.get(cm)
        if data is None or not data["occupancies"]:
            monthly_patterns[cm] = {
                "month_number": cm,
                "month_name": MONTH_NAMES[cm],
                "data_points": 0,
                "avg_occupancy_pct": 0,
                "avg_adr": 0,
                "avg_bookings": 0,
                "avg_room_nights": 0,
                "avg_revenue": 0,
                "avg_length_of_stay": 0,
                "demand_index": 0,
                "years_seen": [],
            }
            issues.append({
                "severity": "MEDIUM",
                "message": f"No data for {MONTH_NAMES[cm]} — demand estimate unreliable",
            })
            continue

        n = len(data["occupancies"])
        avg_occ = sum(data["occupancies"]) / n
        avg_adr = sum(data["adrs"]) / n
        avg_bookings = sum(data["bookings"]) / n
        avg_nights = sum(data["room_nights"]) / n
        avg_revenue = sum(data["grosses"]) / n
        avg_stay = round(sum(data["room_nights"]) / sum(data["bookings"]), 1) if sum(data["bookings"]) > 0 else 0

        # Demand index: weighted combination of occupancy (70%) and booking count (30%)
        max_bookings = max(
            max(cal_month_data[m]["bookings"]) for m in cal_month_data if cal_month_data[m]["bookings"]
        ) if cal_month_data else 1
        occ_score = (avg_occ / max_occ * 100) if max_occ > 0 else 0
        booking_score = (avg_bookings / max_bookings * 100) if max_bookings > 0 else 0
        demand_index = round(occ_score * 0.7 + booking_score * 0.3)
        demand_index = max(0, min(100, demand_index))

        monthly_patterns[cm] = {
            "month_number": cm,
            "month_name": MONTH_NAMES[cm],
            "data_points": n,
            "avg_occupancy_pct": round(avg_occ, 1),
            "avg_adr": round(avg_adr, 2),
            "avg_bookings": round(avg_bookings, 1),
            "avg_room_nights": round(avg_nights, 1),
            "avg_revenue": round(avg_revenue, 2),
            "avg_length_of_stay": round(avg_stay, 1),
            "demand_index": demand_index,
            "years_seen": sorted(data["years_seen"]),
        }

    # Check for demand cliffs (>50% drop between adjacent months)
    for cm in range(1, 12):
        curr = monthly_patterns.get(cm, {}).get("demand_index", 0)
        next_m = monthly_patterns.get(cm + 1, {}).get("demand_index", 0)
        if curr > 0 and next_m < curr * 0.5:
            issues.append({
                "severity": "MEDIUM",
                "message": (
                    f"Demand cliff: {MONTH_NAMES[cm]} (index {curr}) -> "
                    f"{MONTH_NAMES[cm + 1]} (index {next_m})"
                ),
            })

    # Check for insufficient data
    low_data_months = [
        MONTH_NAMES[cm] for cm in range(1, 13)
        if monthly_patterns[cm]["data_points"] < 2
        and monthly_patterns[cm]["data_points"] > 0
    ]
    if low_data_months:
        issues.append({
            "severity": "LOW",
            "message": f"Only 1 year of data for: {', '.join(low_data_months)} — patterns may not be reliable",
        })

    # Overall averages
    active_months = [p for p in monthly_patterns.values() if p["data_points"] > 0]
    overall = {
        "avg_occupancy_pct": round(
            sum(p["avg_occupancy_pct"] for p in active_months) / len(active_months), 1
        ) if active_months else 0,
        "avg_adr": round(
            sum(p["avg_adr"] for p in active_months) / len(active_months), 2
        ) if active_months else 0,
        "avg_demand_index": round(
            sum(p["demand_index"] for p in active_months) / len(active_months)
        ) if active_months else 0,
        "months_with_data": len(active_months),
        "total_data_points": sum(p["data_points"] for p in active_months),
    }

    return {
        "monthly_patterns": monthly_patterns,
        "overall": overall,
        "issues": issues,
    }


if __name__ == "__main__":
    result = analyze_demand()
    print(f"\nHistorical Demand Analysis")
    print(f"{'=' * 60}")
    print(f"  Overall avg occupancy: {result['overall']['avg_occupancy_pct']}%")
    print(f"  Overall avg ADR:       EUR {result['overall']['avg_adr']}")
    print(f"  Months with data:      {result['overall']['months_with_data']}")
    print(f"\n  {'Month':<12} {'Occ%':>6} {'ADR':>8} {'Bookings':>9} {'Demand':>7}")
    print(f"  {'-'*12} {'-'*6} {'-'*8} {'-'*9} {'-'*7}")
    for cm in range(1, 13):
        p = result["monthly_patterns"][cm]
        print(f"  {p['month_name']:<12} {p['avg_occupancy_pct']:>5.1f}% {p['avg_adr']:>7.2f} "
              f"{p['avg_bookings']:>8.1f} {p['demand_index']:>6}")
    if result["issues"]:
        print(f"\n  Issues:")
        for issue in result["issues"]:
            print(f"    [{issue['severity']}] {issue['message']}")
    print()
