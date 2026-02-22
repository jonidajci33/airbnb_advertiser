# Skill: Market Benchmarks

## Purpose
Compile per-month market benchmark pricing for Tirana using research data, and calculate the rating-based price premium the property can command.

## When to Use
- When you need Tirana market rates by season (peak/shoulder/off-season)
- When you want to know what premium the 4.88/5 + 10.0/10 ratings justify
- Before running the price optimizer
- When comparing your pricing against the market

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
/c/Users/jonid/AppData/Local/Programs/Python/Python312/python.exe price_skills/market_benchmarks.py
```

Or in Python:
```python
from price_skills.market_benchmarks import compile_benchmarks
result = compile_benchmarks()
```

## What It Computes

### Per-Month Benchmarks (January-December)
- Season tier (peak/shoulder/off_season)
- Market rate range (low-high EUR)
- Market average rate (EUR)
- Market occupancy % for that season
- Top 25% rate from research data

### Rating Premium
- Airbnb rating: 4.88/5 (top 5% by rating)
- Booking.com rating: 10.0/10 (perfect)
- Applied premium: 17% above market average (research supports 15-25%)
- Multiplier: 1.17x

### Market Context
- Tirana active listings: 3,488
- Average ADR, occupancy, top 10% income
- Seasonal swing factors

## Data Sources
- `research_skills/pricing_mastery.py` - SEASONAL_STRATEGY_TIRANA, RATING_ADJUSTED_PRICING
- `research_skills/market_intel.py` - MARKET_DATA (Tirana benchmarks)

## Output
Returns a dict with:
- `monthly_benchmarks`: dict[1-12] with market rates, season, occupancy per month
- `rating_premium`: premium calculation details and justification
- `market_context`: general Tirana market statistics
