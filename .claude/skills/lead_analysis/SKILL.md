# Skill: Lead Quality Analysis

## Purpose
Analyze the completeness and quality of the clinic lead database in leads.xlsx.

## When to Use
- When you need to assess the health of the lead database
- When you need to prioritize data enrichment efforts
- When you want to understand category balance and proximity distribution

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
python -c "from skills.lead_quality_analyzer import run; run()"
```

## What It Analyzes
1. **Data Completeness**: % of leads with name, phone, email, website, score
2. **Category Distribution**: DENTAL vs HAIR_TRANSPLANT vs UNKNOWN balance
3. **Proximity Scores**: Distance distribution from property
4. **Growth Timeline**: When leads were added, scraping velocity

## Data Sources
- `leads.xlsx` — All columns (A through J)

## Output
Returns a dict with `completeness`, `categories`, `proximity_scores`, `growth_timeline`, and `issues`.
