# Skill: Price Optimizer

## Purpose
Combine historical demand patterns with market benchmarks to recommend optimal nightly rates for each month, with revenue projections comparing current vs recommended vs market pricing.

## When to Use
- When you need specific nightly rate recommendations per month
- When you want revenue projections under different pricing scenarios
- When comparing current flat EUR 45/night against optimized dynamic pricing
- After historical demand and market benchmarks have been computed

## How to Execute
```python
from price_skills.historical_demand import analyze_demand
from price_skills.market_benchmarks import compile_benchmarks
from price_skills.price_optimizer import optimize_prices

demand = analyze_demand()
benchmarks = compile_benchmarks()
result = optimize_prices(demand, benchmarks)
```

Or just run the full price predictor agent:
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
/c/Users/jonid/AppData/Local/Programs/Python/Python312/python.exe price_predictor_agent.py
```

## What It Computes

### Per-Month Recommendations (12 months)
- **Recommended nightly rate** = market_benchmark x rating_premium x demand_adjustment
- **Rate range** (min-max) for dynamic pricing (+/- 10%)
- **Expected occupancy** - blended from historical (60%) and market (40%), adjusted for price change
- **Expected revenue** - recommended rate x expected nights
- **Revenue uplift** vs current flat rate (EUR and %)

### Pricing Formula
```
recommended_rate = market_avg_rate x 1.17 (rating premium) x demand_adjustment
demand_adjustment = historical_demand_index / avg_demand_index (capped at +/- 15%)
rate clamped to EUR 33-70 range
```

### Revenue Scenarios
- **Current**: flat EUR 45/night at historical occupancy
- **Recommended**: dynamic seasonal pricing at expected occupancy
- **Market average**: market rates at market occupancy
- **Annual uplift**: EUR and % difference between current and recommended

## Output
Returns a dict with:
- `recommendations`: list of 12 monthly recommendation dicts
- `revenue_scenarios`: current vs recommended vs market annual projections
- `summary`: avg/min/max recommended rates, months above/below current
