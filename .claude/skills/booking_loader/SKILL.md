# Skill: Booking.com Data Loader

## Purpose
Parse all Booking.com reservation statement CSVs and normalize into a unified schema for financial analysis.

## When to Use
- When you need to load Booking.com reservation data
- When you want to check how many bookings came through Booking.com
- When you need raw reservation data for any financial calculation
- After adding new monthly Booking.com CSV exports

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
/c/Users/jonid/AppData/Local/Programs/Python/Python312/python.exe -c "from finance_skills.booking_loader import load_reservations; import json; r = load_reservations(); print(json.dumps(r['summary'], indent=2))"
```

Or run standalone:
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
/c/Users/jonid/AppData/Local/Programs/Python/Python312/python.exe finance_skills/booking_loader.py
```

## What It Does
1. Globs all `Monthly bills/Booking/reservation_statements_overview_*.csv` files
2. Parses each CSV with `csv.DictReader`
3. Normalizes each row into: `{platform, reservation_number, arrival, departure, guest_name, room_nights, original_amount, final_amount, commission_amount, net_amount, status, month_key, ...}`
4. Filters: cancelled rows get `final_amount=0`, `room_nights=0`
5. Flags issues: high cancellation rate (>20%), missing months in data range

## Data Source
- `Monthly bills/Booking/reservation_statements_overview_*.csv` (23 files, Jan 2024 - Dec 2025)
- Columns: Reservation number, Arrival, Departure, Guest name, Room nights, Original amount, Final amount, Commission amount, Status (OK/CANCELLED), Currency (EUR)

## Output
Returns a dict with:
- `reservations`: list of normalized reservation dicts
- `summary`: totals (ok_reservations, total_room_nights, total_gross_revenue, total_commission, total_net_revenue, months_covered)
- `issues`: list of warnings (high cancellation rate, missing months)
