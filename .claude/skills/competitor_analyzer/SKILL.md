# Skill: Competitor Analyzer

## Purpose
Loads and analyzes competitor data from `competitors.json`. Filters for properties near Lulebore Apartment 1 that accept at most 3 guests. Computes per-season pricing benchmarks, rating tiers, and your competitive position from real competitor data.

## When to Use
- Called automatically by the price predictor agent pipeline
- When you want to understand your competitive position
- After updating `competitors.json` with new competitor research
- When you need pricing benchmarks by season or rating tier

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
/c/Users/jonid/AppData/Local/Programs/Python/Python312/python.exe price_skills/competitor_analyzer.py
```

## What It Does
1. Loads competitor data from `competitors.json` (31 listings)
2. Filters for max 3 guests (studios and 1-bedrooms)
3. Computes price statistics: average, median, 25th/75th percentile
4. Groups competitors by rating tier (4.8+, 4.5-4.79, 4.0-4.49, below 4.0) and computes avg price per tier
5. Calculates your position: price percentile, rating rank, price vs avg
6. Builds per-month seasonal benchmarks using competitor seasonal data

## Output
Returns dict with:
- `competitor_count`: number of competitors analyzed
- `avg_price_eur`, `median_price_eur`, `p25_price_eur`, `p75_price_eur`: price statistics
- `your_position`: your price percentile, rating rank, price vs avg
- `monthly_benchmarks`: per-month pricing by season (off/shoulder/peak)
- `rating_tiers`: avg price per rating tier
- `competitors`: sorted list of all competitors with name, platform, price, rating

## Data File
- `competitors.json` - Update quarterly with fresh competitor research from Airbnb and Booking.com
- Filter: central Tirana, studios and 1-bedrooms, max 3 guests
