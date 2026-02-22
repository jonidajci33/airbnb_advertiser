# Skill: Competitor Analysis

## Purpose
Benchmark the property against competitors and the broader Tirana market. Identify competitive gaps and unique advantages.

## When to Use
- When you need to understand competitive positioning
- When you want to identify what competitors do better
- When you need to leverage unique selling points more effectively

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
python -c "from skills.competitor_analyzer import run; run()"
```

## What It Analyzes
1. **Market Landscape**: 3,639 Tirana listings, pricing, medical tourism growth
2. **Competitive Gaps**: 7 areas where competitors outperform us (photos, capacity, descriptions, etc.)
3. **Unique Advantages**: 5 differentiators (soundproofing, private entrance, medical niche, perfect Booking.com rating, location)
4. **First-Mover Opportunity**: Medical tourism niche timing

## Data Sources
- `property_profile.md` — Property features
- `marketing_report.md` — Market research data

## Output
Returns a dict with `market_landscape`, `competitive_position`, and `issues`.
