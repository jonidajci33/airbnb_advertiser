# Skill: Price Predictor Agent (Master Orchestrator)

## Purpose
The master pricing optimization agent that runs ALL price skills in sequence and produces a comprehensive pricing recommendation report. Uses **real competitor data** (nearby properties accepting at most 3 guests) instead of broad market averages for accurate pricing.

## When to Use
- Monthly, after running the finance agent with updated billing data
- When you want optimal nightly rate recommendations for each month
- When you need revenue projections comparing current vs optimized pricing
- When you want a pricing action plan based on real competitor benchmarks
- After updating `competitors.json` with fresh competitor research

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
/c/Users/jonid/AppData/Local/Programs/Python/Python312/python.exe price_predictor_agent.py
```

## What It Does
Runs these 4 skills **in order**:

| # | Skill | What It Does |
|---|-------|-------------|
| 1 | `historical_demand` | Analyzes reservation data for per-month demand patterns (0-100 index) |
| 2 | `competitor_analyzer` | Loads 31 nearby competitors (max 3 guests), computes avg/median/percentile pricing by season and rating tier |
| 3 | `market_benchmarks` | Builds per-month benchmarks from competitor data + calculates rating premium from competitor tier analysis |
| 4 | `price_optimizer` | Generates monthly rate recommendations blending competitor benchmarks + historical demand + rating premium |

After running all skills, the agent:
1. Analyzes your historical occupancy and ADR by month
2. Loads and filters competitor data (31 nearby studios/1-bedrooms, max 3 guests)
3. Computes your position vs competitors (price percentile, rating rank)
4. Calculates rating premium from actual competitor tier pricing
5. Generates optimal rate per month using competitor median as base
6. Projects revenue under current/recommended/competitor-average scenarios
7. Generates report with competitor analysis, seasonal strategy, and action steps
8. Saves everything to markdown and JSON

## Output Files
- `pricing_recommendations.md` - Full report with:
  - Competitor analysis (price distribution, rating tiers, all 31 competitors listed)
  - 12-month price table with competitor avg/median columns
  - Revenue projections (current vs recommended vs competitor average)
  - Seasonal strategy with competitor context
  - Action steps
- `pricing_data.json` - Machine-readable data including full competitor analysis

## Data Files
- `competitors.json` - Competitor database (31 listings, manually researched). Update quarterly by searching Airbnb/Booking.com for studios and 1-bedrooms near the apartment accepting max 3 guests.

## Architecture
```
price_predictor_agent.py (Master Orchestrator)
  ├── price_skills/historical_demand.py  (loads from finance_skills loaders)
  ├── price_skills/competitor_analyzer.py (loads competitors.json)
  ├── price_skills/market_benchmarks.py   (uses competitor data)
  └── price_skills/price_optimizer.py
```

## Key Improvements over Previous Version
1. **Competitor-based**: Uses 31 real competitor listings (max 3 guests, central Tirana) instead of broad Tirana-wide averages (3,488 listings of all sizes)
2. **Rating premium from data**: Calculates premium from actual price difference between premium-rated (4.8+) and average competitors, not a hardcoded 17%
3. **Median-based pricing**: Uses competitor median (robust to outliers) as base rate instead of mean
4. **Dynamic rate bounds**: Clamps recommendations to 90%-120% of actual competitor range instead of fixed EUR 33-70
5. **Historical ADR blending**: When you have 2+ years of data for a month, blends 60% competitor + 40% your historical ADR

## Dependency
Run `finance_agent.py` first (or at least have billing CSVs in `Monthly bills/`) since the price predictor reads reservation data through the finance skills loaders.

## Monthly Workflow
1. Run `python finance_agent.py` (updates financial data)
2. Run `python price_predictor_agent.py` (updates pricing recommendations)
3. Review `pricing_recommendations.md` for updated rate suggestions
4. Adjust PriceLabs/platform rates based on recommendations

## Quarterly Workflow
1. Research competitors on Airbnb/Booking.com (search for studios/1-bed, max 3 guests, central Tirana)
2. Update `competitors.json` with new listings, prices, ratings
3. Run `python price_predictor_agent.py` to refresh recommendations
