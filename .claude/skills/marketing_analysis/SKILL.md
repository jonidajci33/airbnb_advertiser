# Skill: Marketing Channel Analysis

## Purpose
Evaluate all marketing channels and identify which ones are missing or underutilized.

## When to Use
- When you need a complete picture of marketing channel health
- When you want to identify the most impactful new channels to add
- When you need to prioritize marketing efforts

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
python -c "from skills.marketing_analyzer import run; run()"
```

## What It Analyzes
12 marketing channels:
1. Airbnb (active)
2. Booking.com (active)
3. Email outreach (active)
4. WhatsApp outreach (minimal)
5. Social media (not started)
6. Google Business (not started)
7. Direct booking website (not started)
8. Paid ads (not started)
9. In-person clinic visits (not started)
10. Medical tourism directories (not started)
11. YouTube (not started)
12. Guest referral program (not started)

## Data Sources
- `leads.xlsx` — Outreach data
- `email_sender.log` — Email campaign data
- `property_profile.md` — Channel status

## Output
Returns a dict with `channel_analysis` and `issues` (missing/underutilized channels).
