# Skill: Business Improvement Agent (Master Orchestrator)

## Purpose
The master agent that runs ALL analysis skills in sequence and produces a consolidated improvement report. This is the main entry point for a full business analysis.

## When to Use
- When you want a complete business analysis across all dimensions
- When you need a prioritized list of everything that needs improvement
- When you want a 30-day action plan

## How to Execute
```bash
cd /c/Users/jonid/OneDrive/Documents/GIT/ai/airbnb_advertiser
python agent.py
```

## What It Does
Runs these 8 skills **in order**:

| # | Skill | What It Does |
|---|-------|-------------|
| 1 | `data_loader` | Loads leads.xlsx, email logs, property data |
| 2 | `outreach_analyzer` | Analyzes email/WhatsApp campaign effectiveness |
| 3 | `lead_quality_analyzer` | Analyzes lead database quality and completeness |
| 4 | `property_analyzer` | Analyzes listing performance vs benchmarks |
| 5 | `pricing_analyzer` | Analyzes pricing strategy and revenue potential |
| 6 | `marketing_analyzer` | Evaluates all 12 marketing channels |
| 7 | `competitor_analyzer` | Benchmarks against competitors |
| 8 | `review_analyzer` | Analyzes reviews and guest experience |

After running all skills, the agent:
1. Collects all issues from every skill
2. Prioritizes them by severity (CRITICAL > HIGH > MEDIUM > LOW)
3. Generates a comprehensive improvement report
4. Creates a 30-day action plan
5. Saves everything to `improvement_report.md` and `improvement_data.json`

## Output Files
- `improvement_report.md` — Human-readable prioritized improvement report with action plan
- `improvement_data.json` — Machine-readable raw analysis data from all skills

## Architecture
```
agent.py (Master Orchestrator)
  ├── skills/data_loader.py
  ├── skills/outreach_analyzer.py
  ├── skills/lead_quality_analyzer.py
  ├── skills/property_analyzer.py
  ├── skills/pricing_analyzer.py
  ├── skills/marketing_analyzer.py
  ├── skills/competitor_analyzer.py
  └── skills/review_analyzer.py
```

Each skill:
- Has a `run()` function that returns a result dict
- Analyzes a specific business dimension
- Returns `issues` (list of improvement areas with severity, finding, recommendation)
- Can be run independently for focused analysis
