# Skill: Excel Dashboard Generator

## Purpose
Create a formatted `financial_dashboard.xlsx` with 5 sheets containing all financial data, charts, and color-coded reservations.

## When to Use
- After running the financial calculator to produce an Excel report
- When the user wants a visual financial dashboard
- When generating monthly/quarterly financial reports

## How to Execute
```python
from finance_skills.excel_generator import generate_excel

# metrics = output from financial_calculator.compute_metrics()
# reservations = combined list of all reservations
excel_path = generate_excel(metrics, reservations)
```

Or just run the full finance agent which calls this automatically:
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
/c/Users/jonid/AppData/Local/Programs/Python/Python312/python.exe finance_agent.py
```

## What It Creates

### Sheet 1: Dashboard
- KPIs in formatted layout: total earnings, avg monthly, occupancy, ADR, etc.
- Platform comparison section
- Yearly overview section

### Sheet 2: Monthly Breakdown
- One row per month with all metrics as columns
- Line chart showing revenue trend over time

### Sheet 3: Yearly Comparison
- 2024 vs 2025 vs 2026 side by side with growth %
- Bar chart for yearly revenue comparison

### Sheet 4: Platform Comparison
- Airbnb vs Booking.com metrics (revenue, commission, bookings, ADR)
- Monthly platform split table

### Sheet 5: All Reservations
- Every booking as a row
- Color-coded: green for OK, red for CANCELLED
- Auto-filtered columns

## Dependencies
- `openpyxl` (already installed)

## Output
- `financial_dashboard.xlsx` in the project root
