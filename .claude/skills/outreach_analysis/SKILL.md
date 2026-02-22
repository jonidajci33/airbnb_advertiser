# Skill: Outreach Analysis

## Purpose
Analyze email and WhatsApp outreach campaign effectiveness for the Airbnb clinic partnership program.

## When to Use
- When you need to understand how effective the clinic outreach has been
- When you need to identify gaps in the outreach strategy
- When you want to know which clinics haven't been contacted yet

## How to Execute
Run the Python skill:
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
python -c "from skills.outreach_analyzer import run; run()"
```

## What It Analyzes
1. **Email Campaign**: Coverage rate, send sessions, category distribution
2. **WhatsApp Campaign**: Coverage rate, phone number availability
3. **Gaps**: Missing follow-ups, no conversion tracking, low send velocity

## Data Sources
- `leads.xlsx` — Column J (Emailed), Column I (Messaged)
- `email_sender.log` — Timestamped send history

## Output
Returns a dict with `email_outreach`, `whatsapp_outreach`, and `issues` (list of improvement areas with severity, finding, and recommendation).
