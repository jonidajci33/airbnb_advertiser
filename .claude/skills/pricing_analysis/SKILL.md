# Skill: Pricing Analysis

## Purpose
Analyze pricing strategy and identify revenue optimization opportunities.

## When to Use
- When you need to assess if pricing is optimal for the rating level
- When you want to calculate potential revenue gains
- When you need to design discount strategies for medical tourists

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
python -c "from skills.pricing_analyzer import run; run()"
```

## What It Analyzes
1. **Rate Positioning**: Current rate vs market average, adjusted for rating quality
2. **Revenue Scenarios**: Monthly revenue at different rates and occupancy levels
3. **Medical Tourism Pricing**: Weekly/bi-weekly rates for patient stays
4. **Missing Strategies**: Dynamic pricing, seasonal rates, direct booking incentives, clinic referral rates

## Data Sources
- `property_profile.md` — Pricing and rating data
- `marketing_report.md` — Market context

## Output
Returns a dict with `pricing_analysis` and `issues` (revenue optimization opportunities).
