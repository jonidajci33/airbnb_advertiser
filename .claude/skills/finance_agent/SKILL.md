# Skill: Finance Agent (Master Orchestrator)

## Purpose
The master financial tracking agent that runs ALL finance skills in sequence and produces a complete financial dashboard, report, and data export. This is the main entry point for monthly financial tracking.

## When to Use
- Every month after adding new billing CSVs to `Monthly bills/`
- When you want a complete financial overview across all platforms
- When you need updated Excel dashboard, markdown report, and JSON data
- First thing to run before the price predictor agent

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
/c/Users/jonid/AppData/Local/Programs/Python/Python312/python.exe finance_agent.py
```

## What It Does
Runs these 4 skills **in order**:

| # | Skill | What It Does |
|---|-------|-------------|
| 1 | `booking_loader` | Loads all Booking.com CSVs from `Monthly bills/Booking/` |
| 2 | `airbnb_loader` | Loads all Airbnb CSVs from `Monthly bills/AirBnb/` |
| 3 | `financial_calculator` | Computes monthly/yearly/all-time KPIs from combined data |
| 4 | `excel_generator` | Creates formatted 5-sheet Excel workbook |

After running all skills, the agent:
1. Combines reservations from both platforms
2. Computes all financial metrics
3. Generates Excel dashboard with charts
4. Generates markdown report
5. Generates JSON data export
6. Prints summary to terminal

## Output Files
- `financial_dashboard.xlsx` - 6-sheet Excel workbook:
  1. **Monthly Earnings** - Main view: per-month Booking.com gross/fees/net + Airbnb gross/fees/net + totals, with yearly subtotals, grand total row, and revenue trend chart
  2. **Yearly Summary** - Year-by-year comparison with platform split and YoY growth
  3. **Dashboard** - KPIs at a glance (all-time totals, per-platform breakdown, occupancy, ADR)
  4. **Booking.com Details** - Every Booking.com reservation (color-coded by status)
  5. **Airbnb Details** - Every Airbnb reservation with USD and EUR amounts
  6. **Data Tracker** - Which months have been processed for each platform, next month to add
- `financial_report.md` - Human-readable financial report with per-platform tables
- `financial_data.json` - Machine-readable data (includes months_processed list for tracking)

## Architecture
```
finance_agent.py (Master Orchestrator)
  ├── finance_skills/booking_loader.py
  ├── finance_skills/airbnb_loader.py
  ├── finance_skills/financial_calculator.py
  └── finance_skills/excel_generator.py
```

## Monthly Workflow
1. Download new Booking.com CSV from extranet, save to `Monthly bills/Booking/`
2. Export Airbnb transaction history CSV, save to `Monthly bills/AirBnb/`
3. Run `python finance_agent.py`
4. Open `financial_dashboard.xlsx` to review
