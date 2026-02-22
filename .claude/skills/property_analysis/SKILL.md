# Skill: Property Performance Analysis

## Purpose
Analyze the Airbnb/Booking.com listing performance and identify gaps against industry benchmarks.

## When to Use
- When you need to assess listing quality (photos, description, amenities)
- When you need to benchmark against top performers
- When you want to identify the highest-impact listing improvements

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
python -c "from skills.property_analyzer import run; run()"
```

## What It Analyzes
1. **Listing Metrics**: Photos, capacity, ratings, reviews, pricing
2. **Benchmarks**: Current vs target vs top performer for each metric
3. **Marketing Channels**: Active vs missing channels
4. **Missing Features**: Video tour, long-stay discounts, social media

## Data Sources
- `property_profile.md` — Property metadata
- `property_fixes.md` — Known improvement checklist

## Output
Returns a dict with `metrics`, `benchmarks`, and `issues` (prioritized improvements).
