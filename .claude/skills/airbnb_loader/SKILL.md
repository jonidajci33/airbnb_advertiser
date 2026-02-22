# Skill: Airbnb Data Loader

## Purpose
Parse Airbnb transaction/reservation CSV exports and normalize into the same unified schema as the Booking.com loader.

## When to Use
- When you need to load Airbnb reservation data
- When you want to check Airbnb earnings and booking counts
- After the user exports a new Airbnb CSV and places it in `Monthly bills/AirBnb/`
- When combining data from both platforms for financial analysis

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
/c/Users/jonid/AppData/Local/Programs/Python/Python312/python.exe -c "from finance_skills.airbnb_loader import load_reservations; import json; r = load_reservations(); print(json.dumps(r['summary'], indent=2))"
```

Or run standalone:
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
/c/Users/jonid/AppData/Local/Programs/Python/Python312/python.exe finance_skills/airbnb_loader.py
```

## What It Does
1. Globs all `Monthly bills/AirBnb/*.csv` files (skips PDFs)
2. Auto-detects Airbnb CSV format (transaction history vs reservation details)
3. Filters only "Reservation" type rows (skips payout/transfer rows)
4. Normalizes into the same schema as booking_loader: `{platform, reservation_number, arrival, departure, guest_name, room_nights, final_amount, commission_amount, net_amount, status, month_key, ...}`
5. If no CSVs found: returns empty list + MEDIUM issue with Airbnb export instructions

## Data Source
- `Monthly bills/AirBnb/*.csv`
- Current file: `airbnb_.csv` - Airbnb transaction history format
- Columns: Date, Type, Confirmation code, Start date, End date, Nights, Guest, Currency (USD), Amount, Paid out, Service fee, Gross earnings

## Output
Returns a dict with:
- `reservations`: list of normalized reservation dicts
- `summary`: totals (ok_reservations, total_room_nights, total_gross_revenue, total_commission, total_net_revenue)
- `issues`: list of warnings
