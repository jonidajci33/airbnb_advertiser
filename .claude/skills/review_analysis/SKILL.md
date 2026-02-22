# Skill: Review & Guest Experience Analysis

## Purpose
Analyze guest reviews and identify experience improvements that drive higher ratings and more bookings.

## When to Use
- When you need to assess review velocity and patterns
- When you want to identify guest experience gaps
- When you need to improve review solicitation

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
python -c "from skills.review_analyzer import run; run()"
```

## What It Analyzes
1. **Review Metrics**: 54 total reviews (33 Airbnb + 21 Booking.com), satisfaction score
2. **Review Velocity**: Monthly review rate vs targets, time to 100 reviews
3. **Guest Experience**: 8 experience areas rated (arrival, welcome, recovery amenities, guidebook, follow-up, check-in flexibility, kitchen, soundproofing)
4. **Missing Experience Elements**: Welcome basket, digital guidebook, recovery amenities, post-checkout follow-up

## Data Sources
- `property_profile.md` — Ratings and review counts

## Output
Returns a dict with `review_metrics`, `velocity`, `guest_experience`, and `issues`.
