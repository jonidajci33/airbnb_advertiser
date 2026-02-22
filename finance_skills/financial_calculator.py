"""
Skill: Financial Calculator
Computes per-month, per-year, per-platform, and all-time metrics.
All amounts in EUR.
"""

import calendar
from collections import defaultdict
from datetime import datetime


def _days_in_month(year, month):
    return calendar.monthrange(year, month)[1]


def _month_label(month_key):
    try:
        dt = datetime.strptime(month_key, "%Y-%m")
        return dt.strftime("%b %Y")
    except ValueError:
        return month_key


def compute_metrics(booking_reservations, airbnb_reservations):
    """
    Compute comprehensive financial metrics from reservation data.
    Both lists should contain normalized dicts with gross_eur, commission_eur, net_eur fields.

    Returns dict with: monthly, yearly, platform_yearly, all_time, months_processed, issues
    """
    issues = []

    # Build per-month per-platform aggregates
    # Key: (month_key, platform)
    mp = defaultdict(lambda: {
        "gross": 0.0, "fees": 0.0, "net": 0.0,
        "nights": 0, "bookings": 0, "guests": set(),
    })

    all_reservations = []

    for r in booking_reservations:
        if not r["has_revenue"]:
            continue
        mk = r["month_key"]
        p = "Booking.com"
        mp[(mk, p)]["gross"] += r["gross_eur"]
        mp[(mk, p)]["fees"] += r["commission_eur"]
        mp[(mk, p)]["net"] += r["net_eur"]
        mp[(mk, p)]["nights"] += r["room_nights"]
        mp[(mk, p)]["bookings"] += 1
        if r["guest_name"]:
            mp[(mk, p)]["guests"].add(r["guest_name"].lower())
        all_reservations.append(r)

    for r in airbnb_reservations:
        if not r.get("has_revenue", True):
            continue
        mk = r["month_key"]
        p = "Airbnb"
        mp[(mk, p)]["gross"] += r["gross_eur"]
        mp[(mk, p)]["fees"] += r["commission_eur"]
        mp[(mk, p)]["net"] += r["net_eur"]
        mp[(mk, p)]["nights"] += r["room_nights"]
        mp[(mk, p)]["bookings"] += 1
        if r["guest_name"]:
            mp[(mk, p)]["guests"].add(r["guest_name"].lower())
        all_reservations.append(r)

    # Get all months
    all_months = sorted(set(mk for mk, _ in mp.keys()) - {"unknown"})

    # Build monthly metrics
    monthly = {}
    for mk in all_months:
        try:
            year = int(mk[:4])
            month = int(mk[5:7])
            days = _days_in_month(year, month)
        except (ValueError, IndexError):
            days = 30

        booking = mp.get((mk, "Booking.com"), {"gross": 0, "fees": 0, "net": 0, "nights": 0, "bookings": 0, "guests": set()})
        airbnb = mp.get((mk, "Airbnb"), {"gross": 0, "fees": 0, "net": 0, "nights": 0, "bookings": 0, "guests": set()})

        total_gross = booking["gross"] + airbnb["gross"]
        total_fees = booking["fees"] + airbnb["fees"]
        total_net = booking["net"] + airbnb["net"]
        total_nights = booking["nights"] + airbnb["nights"]
        total_bookings = booking["bookings"] + airbnb["bookings"]

        occupancy = round(total_nights / days * 100, 1) if days > 0 else 0
        adr = round(total_gross / total_nights, 2) if total_nights > 0 else 0

        monthly[mk] = {
            "month_key": mk,
            "month_label": _month_label(mk),
            "year": mk[:4],
            "days_in_month": days,
            # Booking.com
            "booking_gross": round(booking["gross"], 2),
            "booking_fees": round(booking["fees"], 2),
            "booking_net": round(booking["net"], 2),
            "booking_nights": booking["nights"],
            "booking_bookings": booking["bookings"],
            # Airbnb
            "airbnb_gross": round(airbnb["gross"], 2),
            "airbnb_fees": round(airbnb["fees"], 2),
            "airbnb_net": round(airbnb["net"], 2),
            "airbnb_nights": airbnb["nights"],
            "airbnb_bookings": airbnb["bookings"],
            # Totals
            "total_gross": round(total_gross, 2),
            "total_fees": round(total_fees, 2),
            "total_net": round(total_net, 2),
            "total_nights": total_nights,
            "total_bookings": total_bookings,
            "occupancy_pct": occupancy,
            "adr": adr,
        }

    # Build yearly metrics
    yearly_data = defaultdict(lambda: {
        "booking_gross": 0, "booking_fees": 0, "booking_net": 0,
        "booking_nights": 0, "booking_bookings": 0,
        "airbnb_gross": 0, "airbnb_fees": 0, "airbnb_net": 0,
        "airbnb_nights": 0, "airbnb_bookings": 0,
        "total_days": 0, "months_count": 0,
    })

    for mk, m in monthly.items():
        year = m["year"]
        for key in ["booking_gross", "booking_fees", "booking_net", "booking_nights", "booking_bookings",
                     "airbnb_gross", "airbnb_fees", "airbnb_net", "airbnb_nights", "airbnb_bookings"]:
            yearly_data[year][key] += m[key]
        yearly_data[year]["total_days"] += m["days_in_month"]
        yearly_data[year]["months_count"] += 1

    yearly = {}
    sorted_years = sorted(yearly_data.keys())
    for i, year in enumerate(sorted_years):
        d = yearly_data[year]
        tg = d["booking_gross"] + d["airbnb_gross"]
        tf = d["booking_fees"] + d["airbnb_fees"]
        tn = d["booking_net"] + d["airbnb_net"]
        total_nights = d["booking_nights"] + d["airbnb_nights"]
        occ = round(total_nights / d["total_days"] * 100, 1) if d["total_days"] > 0 else 0
        adr = round(tg / total_nights, 2) if total_nights > 0 else 0

        yoy = None
        if i > 0:
            prev = sorted_years[i - 1]
            prev_tg = yearly_data[prev]["booking_gross"] + yearly_data[prev]["airbnb_gross"]
            if prev_tg > 0:
                yoy = round((tg - prev_tg) / prev_tg * 100, 1)

        yearly[year] = {
            "year": year,
            "booking_gross": round(d["booking_gross"], 2),
            "booking_fees": round(d["booking_fees"], 2),
            "booking_net": round(d["booking_net"], 2),
            "booking_nights": d["booking_nights"],
            "booking_bookings": d["booking_bookings"],
            "airbnb_gross": round(d["airbnb_gross"], 2),
            "airbnb_fees": round(d["airbnb_fees"], 2),
            "airbnb_net": round(d["airbnb_net"], 2),
            "airbnb_nights": d["airbnb_nights"],
            "airbnb_bookings": d["airbnb_bookings"],
            "total_gross": round(tg, 2),
            "total_fees": round(tf, 2),
            "total_net": round(tn, 2),
            "total_nights": total_nights,
            "total_bookings": d["booking_bookings"] + d["airbnb_bookings"],
            "occupancy_pct": occ,
            "adr": adr,
            "months_count": d["months_count"],
            "yoy_growth_pct": yoy,
        }

    # All-time totals
    tg = sum(m["total_gross"] for m in monthly.values())
    tf = sum(m["total_fees"] for m in monthly.values())
    tn = sum(m["total_net"] for m in monthly.values())
    total_nights = sum(m["total_nights"] for m in monthly.values())
    total_days = sum(m["days_in_month"] for m in monthly.values())
    num_months = len(monthly)

    all_guests = set()
    for r in all_reservations:
        if r.get("guest_name"):
            all_guests.add(r["guest_name"].lower())

    sorted_months = sorted(monthly.items(), key=lambda x: x[1]["total_gross"], reverse=True)
    best = sorted_months[0] if sorted_months else (None, {})
    nonzero = [(k, v) for k, v in sorted_months if v["total_gross"] > 0]
    worst = nonzero[-1] if nonzero else (None, {})

    all_time = {
        "total_gross": round(tg, 2),
        "total_fees": round(tf, 2),
        "total_net": round(tn, 2),
        "booking_gross": round(sum(m["booking_gross"] for m in monthly.values()), 2),
        "booking_fees": round(sum(m["booking_fees"] for m in monthly.values()), 2),
        "booking_net": round(sum(m["booking_net"] for m in monthly.values()), 2),
        "airbnb_gross": round(sum(m["airbnb_gross"] for m in monthly.values()), 2),
        "airbnb_fees": round(sum(m["airbnb_fees"] for m in monthly.values()), 2),
        "airbnb_net": round(sum(m["airbnb_net"] for m in monthly.values()), 2),
        "total_nights": total_nights,
        "total_bookings": sum(m["total_bookings"] for m in monthly.values()),
        "avg_monthly_gross": round(tg / num_months, 2) if num_months > 0 else 0,
        "avg_monthly_net": round(tn / num_months, 2) if num_months > 0 else 0,
        "occupancy_pct": round(total_nights / total_days * 100, 1) if total_days > 0 else 0,
        "adr": round(tg / total_nights, 2) if total_nights > 0 else 0,
        "unique_guests": len(all_guests),
        "best_month": {"key": best[0], "label": best[1].get("month_label", ""), "gross": best[1].get("total_gross", 0)},
        "worst_month": {"key": worst[0], "label": worst[1].get("month_label", ""), "gross": worst[1].get("total_gross", 0)},
        "months_tracked": num_months,
        "date_range": f"{min(monthly.keys())} to {max(monthly.keys())}" if monthly else "N/A",
    }

    # Low occupancy warnings
    low_occ = [(mk, m["occupancy_pct"]) for mk, m in monthly.items() if m["occupancy_pct"] < 10]
    if low_occ:
        labels = ", ".join(f"{_month_label(mk)} ({occ}%)" for mk, occ in low_occ[:5])
        issues.append({"severity": "MEDIUM", "message": f"Low occupancy months (<10%): {labels}"})

    return {
        "monthly": monthly,
        "yearly": yearly,
        "all_time": all_time,
        "months_processed": sorted(all_months),
        "issues": issues,
    }
