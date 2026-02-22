# Skill: Historical Demand Analysis

## Purpose
Analyze reservation data to compute per-calendar-month demand patterns, revealing seasonal demand cycles and identifying high/low demand periods.

## When to Use
- When you need to understand seasonal booking patterns
- When you want demand indices (0-100) per month to inform pricing
- Before running the price optimizer
- When analyzing which months need more marketing

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
/c/Users/jonid/AppData/Local/Programs/Python/Python312/python.exe price_skills/historical_demand.py
```

Or in Python:
```python
from price_skills.historical_demand import analyze_demand
result = analyze_demand()
```

## What It Computes
For each calendar month (January-December), averaged across all available years:
- **Average occupancy %** - how full the apartment was
- **Average ADR** - average nightly rate actually earned
- **Average bookings** - number of reservations
- **Average room nights** - total nights booked
- **Average revenue** - gross earnings
- **Average length of stay** - how long guests stayed
- **Demand index (0-100)** - weighted score combining occupancy (70%) and booking count (30%)

### Issues Detected
- Demand cliffs (>50% drop between adjacent months)
- Insufficient data months (only 1 year of data)
- Months with no data at all

## Data Sources
- Loads from `finance_skills/booking_loader` and `finance_skills/airbnb_loader` automatically
- Uses `finance_skills/financial_calculator` for monthly metric computation

## Output
Returns a dict with:
- `monthly_patterns`: dict[1-12] with demand metrics per calendar month
- `overall`: average occupancy, ADR, demand index across all months
- `issues`: list of warnings
