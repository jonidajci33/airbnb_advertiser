# Skill: Financial Calculator

## Purpose
Compute per-month, per-year, platform comparison, and all-time KPIs from combined reservation data.

## When to Use
- When you need monthly revenue, occupancy, ADR, RevPAR breakdowns
- When comparing year-over-year performance
- When analyzing platform split (Booking.com vs Airbnb)
- When you need all-time KPIs like total revenue, repeat guest rate, best/worst months

## How to Execute
```python
from finance_skills.booking_loader import load_reservations as load_booking
from finance_skills.airbnb_loader import load_reservations as load_airbnb
from finance_skills.financial_calculator import compute_metrics

combined = load_booking()["reservations"] + load_airbnb()["reservations"]
metrics = compute_metrics(combined)
```

## What It Computes

### Per-Month Metrics
- Gross/net revenue, commission
- Room nights, occupancy rate (nights / days_in_month)
- ADR (average daily rate), RevPAR (revenue per available room-night)
- Bookings count, cancellation rate
- Average length of stay, unique guests
- Platform split per month

### Per-Year Aggregates
- Same metrics aggregated by year
- YoY growth percentage

### Platform Comparison
- Booking.com vs Airbnb: revenue, bookings, nights, commission rate, revenue share %

### All-Time KPIs
- Total revenue (gross/net), avg monthly, overall occupancy, overall ADR
- Unique guests, repeat guests, repeat guest rate
- Best month, worst month

### Issues Detected
- Declining revenue trend (last 6 months vs first 6 months)
- Low occupancy months (<15%)
- Platform dependency (>90% from one platform)

## Output
Returns a dict with: `monthly`, `yearly`, `platform_comparison`, `all_time`, `issues`
