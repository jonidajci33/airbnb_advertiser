# Airbnb Business Improvement Agent

A multi-skill analysis agent that reads your 2 years of sales and rental data, runs 8 specialized analysis skills one by one, and produces a prioritized list of everything you need to improve.

---

## Quick Start

```bash
cd C:\Users\jonid\OneDrive\Documents\GIT\ai\airbnb_advertiser
python agent.py
```

That's it. The agent runs all 8 skills automatically and saves the results.

---

## Requirements

- **Python 3.12+** (installed at `C:\Users\jonid\AppData\Local\Programs\Python\Python312\`)
- **openpyxl** — `pip install openpyxl`

If Python isn't on your PATH, run:

```bash
set PATH=C:\Users\jonid\AppData\Local\Programs\Python\Python312;C:\Users\jonid\AppData\Local\Programs\Python\Python312\Scripts;%PATH%
python agent.py
```

---

## What the Agent Does

When you run `python agent.py`, it executes this pipeline:

```
  START
    |
    v
  [1] data_loader ............... Load leads.xlsx, email logs, property data
    |
    v
  [2] outreach_analyzer ........ Analyze email & WhatsApp campaign effectiveness
    |
    v
  [3] lead_quality_analyzer .... Analyze lead database quality & completeness
    |
    v
  [4] property_analyzer ........ Analyze listing performance vs benchmarks
    |
    v
  [5] pricing_analyzer ......... Analyze pricing strategy & revenue potential
    |
    v
  [6] marketing_analyzer ....... Evaluate all 12 marketing channels
    |
    v
  [7] competitor_analyzer ...... Benchmark against Tirana market & competitors
    |
    v
  [8] review_analyzer .......... Analyze reviews & guest experience quality
    |
    v
  COLLECT all issues from every skill
    |
    v
  PRIORITIZE by severity (CRITICAL > HIGH > MEDIUM > LOW)
    |
    v
  GENERATE improvement_report.md + improvement_data.json
    |
    v
  PRINT top 10 improvements to terminal
    |
    v
  DONE
```

---

## Output Files

After running, the agent creates two files in the project root:

| File | Format | Purpose |
|------|--------|---------|
| `improvement_report.md` | Markdown | Human-readable prioritized report with a 30-day action plan |
| `improvement_data.json` | JSON | Machine-readable raw analysis data from all 8 skills |

Open `improvement_report.md` in any Markdown viewer to see the full report with all findings, recommendations, and action items.

---

## The 8 Skills Explained

### Skill 1: Data Loader (`skills/data_loader.py`)

**What it does:** Loads and parses every data source in the project.

**Data sources it reads:**
- `leads.xlsx` — 608 clinic leads with name, location, phone, email, category, website, proximity score, outreach status
- `email_sender.log` — Timestamped history of every email sent (164 successful sends)
- `property_profile.md` — Property metadata (ratings, capacity, pricing, channels)
- `airbnb_info.txt` — Apartment description in Albanian
- `marketing_report.md` — Previous marketing research

**What it returns:** A summary of all data — total leads, phone/email coverage, category breakdown, email success/failure counts.

---

### Skill 2: Outreach Analyzer (`skills/outreach_analyzer.py`)

**What it does:** Measures how effective your email and WhatsApp outreach campaigns have been.

**What it analyzes:**
- Email coverage rate (what % of leads with email have been contacted)
- WhatsApp coverage rate (what % of leads with phone have been messaged)
- Send session patterns (when you sent, how many per session, velocity)
- Category distribution of outreach (DENTAL vs HAIR_TRANSPLANT)
- Missing systems (follow-ups, conversion tracking)

**Example finding:** "Only 0% of leads with phone have been messaged via WhatsApp — 466 leads are waiting."

---

### Skill 3: Lead Quality Analyzer (`skills/lead_quality_analyzer.py`)

**What it does:** Audits the health of your lead database.

**What it analyzes:**
- Field completeness — % of leads with name, phone, email, website, score
- Category balance — dental vs hair transplant vs unknown
- Proximity score distribution — how many leads are within 1-2km vs 12km+
- Growth timeline — when leads were added, whether scraping has stalled
- Fully complete leads — how many have ALL key fields filled

**Example finding:** "Only 20.9% of leads have all key fields (name + phone + email + category)."

---

### Skill 4: Property Analyzer (`skills/property_analyzer.py`)

**What it does:** Benchmarks your Airbnb/Booking.com listing against industry standards.

**What it analyzes:**
- Photo count (current vs target vs top performers)
- Guest capacity assessment
- Rating performance on both platforms
- Review volume vs Superhost thresholds
- Marketing channel readiness (active vs missing)
- Missing features (video tour, long-stay discounts, social media)

**Example finding:** "Only 8 photos (target: 25+). This is the #1 factor limiting bookings."

---

### Skill 5: Pricing Analyzer (`skills/pricing_analyzer.py`)

**What it does:** Evaluates your pricing strategy and calculates revenue you're leaving on the table.

**What it analyzes:**
- Current rate vs market average (€45 vs €50)
- Rating-adjusted fair price (your 4.88/10.0 ratings justify higher pricing)
- Revenue scenarios at different rates and occupancy levels
- Medical tourism weekly/bi-weekly package pricing
- Missing strategies: dynamic pricing, seasonal rates, direct booking incentives, clinic referral rates

**Example finding:** "Charging €45/night but your ratings justify €57/night. You're leaving €240/month on the table."

---

### Skill 6: Marketing Analyzer (`skills/marketing_analyzer.py`)

**What it does:** Evaluates all 12 possible marketing channels and identifies what's missing.

**Channels it evaluates:**

| Channel | Your Status |
|---------|-------------|
| Airbnb | Active |
| Booking.com | Active |
| Email outreach | Active |
| WhatsApp outreach | Minimal (0 sent) |
| Social media (Instagram/TikTok) | Not started |
| Google Business Profile | Not started |
| Direct booking website | Not started |
| Paid ads (Google/Facebook) | Not started |
| In-person clinic visits | Not started |
| Medical tourism directories | Not started |
| YouTube | Not started |
| Guest referral program | Not started |

**Example finding:** "Only using 3 of 12 marketing channels (29.2% utilization). This is a single point of failure."

---

### Skill 7: Competitor Analyzer (`skills/competitor_analyzer.py`)

**What it does:** Benchmarks you against the Tirana short-term rental market and identifies your competitive advantages and gaps.

**What it analyzes:**
- Market landscape (3,639 listings in Tirana, average rates, medical tourism growth)
- 7 competitive gaps where others outperform you (photos, capacity, description, platforms, social proof, Superhost, video)
- 5 unique advantages you have (soundproofing, private entrance, medical niche, perfect Booking rating, location)
- First-mover opportunity window in the medical tourism niche

**Example finding:** "Albania's medical tourism grew 400% since 2020 with 80,000 annual patients. Competitors will start targeting this niche soon."

---

### Skill 8: Review Analyzer (`skills/review_analyzer.py`)

**What it does:** Analyzes your review performance and guest experience quality.

**What it analyzes:**
- Review metrics (54 total — 33 Airbnb + 21 Booking.com)
- Review velocity (2.2/month vs target 5/month)
- Time-to-milestone projections (20 months to 100 reviews at current rate)
- Guest experience audit across 8 areas (arrival, welcome, recovery amenities, guidebook, follow-up, check-in flexibility, kitchen, soundproofing)

**Example finding:** "4 of 8 guest experience areas are missing: welcome package, recovery amenities, digital guidebook, post-checkout follow-up."

---

## Running Individual Skills

You don't have to run the full agent every time. Run any single skill for focused analysis:

```bash
# Outreach effectiveness only
python -c "from skills.outreach_analyzer import run; run()"

# Lead database health only
python -c "from skills.lead_quality_analyzer import run; run()"

# Property listing gaps only
python -c "from skills.property_analyzer import run; run()"

# Pricing optimization only
python -c "from skills.pricing_analyzer import run; run()"

# Marketing channels only
python -c "from skills.marketing_analyzer import run; run()"

# Competitor benchmarking only
python -c "from skills.competitor_analyzer import run; run()"

# Reviews & guest experience only
python -c "from skills.review_analyzer import run; run()"
```

Each skill prints its findings to the terminal and returns a Python dict you can use programmatically.

---

## Understanding the Output

### Severity Levels

Every issue the agent finds is tagged with a severity:

| Severity | Meaning | Action |
|----------|---------|--------|
| **CRITICAL** | Blocking your growth right now | Fix this week |
| **HIGH** | Major impact on revenue/bookings | Fix within 2 weeks |
| **MEDIUM** | Meaningful improvement opportunity | Fix within 1 month |
| **LOW** | Nice to have, incremental gain | Fix when you have time |

### Issue Structure

Each issue contains:

```
Area:            What aspect of the business it relates to
Source Skill:    Which analysis skill found it
Finding:         What the data shows (the problem)
Recommendation:  Specific action to take (the solution)
Estimated Impact: Expected improvement (when quantifiable)
```

---

## Project File Structure

```
airbnb_advertiser/
├── agent.py                    ← Master orchestrator (run this)
├── AGENT.md                    ← This documentation
│
├── skills/                     ← Analysis skill modules
│   ├── __init__.py
│   ├── data_loader.py          ← Skill 1: Load all data
│   ├── outreach_analyzer.py    ← Skill 2: Email & WhatsApp analysis
│   ├── lead_quality_analyzer.py ← Skill 3: Lead database audit
│   ├── property_analyzer.py    ← Skill 4: Listing benchmarks
│   ├── pricing_analyzer.py     ← Skill 5: Pricing optimization
│   ├── marketing_analyzer.py   ← Skill 6: Channel evaluation
│   ├── competitor_analyzer.py  ← Skill 7: Market benchmarking
│   └── review_analyzer.py      ← Skill 8: Reviews & experience
│
├── .claude/skills/             ← Claude Code skill definitions
│   ├── improvement_agent/SKILL.md
│   ├── outreach_analysis/SKILL.md
│   ├── lead_analysis/SKILL.md
│   ├── property_analysis/SKILL.md
│   ├── pricing_analysis/SKILL.md
│   ├── marketing_analysis/SKILL.md
│   ├── competitor_analysis/SKILL.md
│   └── review_analysis/SKILL.md
│
├── leads.xlsx                  ← Lead database (608 clinics)
├── email_sender.log            ← Email send history
├── airbnb_info.txt             ← Property details (Albanian)
├── property_profile.md         ← Property metadata
├── property_fixes.md           ← Known improvement checklist
├── marketing_report.md         ← Marketing research report
│
├── improvement_report.md       ← OUTPUT: Generated improvement report
├── improvement_data.json       ← OUTPUT: Raw analysis data (JSON)
│
├── scraper.py                  ← Clinic lead scraper (Serper API)
├── email_sender.py             ← Email outreach sender
├── email_scraper.py            ← Website email extractor
├── whatsapp_sender.py          ← WhatsApp outreach sender
└── fix_names.py                ← Lead name cleaner
```

---

## How to Use the Results

### 1. Read the Report

Open `improvement_report.md`. Start from the top — issues are sorted by impact.

### 2. Follow the 30-Day Action Plan

The report includes a week-by-week plan:
- **Week 1:** Fix the 2 CRITICAL items (photos, channel diversification)
- **Week 2:** Address the top 5 HIGH items (description, capacity, outreach gaps)
- **Week 3-4:** Work through MEDIUM items (social media, pricing, reviews)

### 3. Re-run After Making Changes

After you implement improvements, run the agent again to see updated results:

```bash
python agent.py
```

The new report will reflect your progress — fixed issues will disappear and new priorities will surface.

### 4. Use the JSON Data Programmatically

`improvement_data.json` contains the raw output from every skill. Use it to build dashboards, track progress over time, or feed into other tools:

```python
import json

with open("improvement_data.json") as f:
    data = json.load(f)

# Get all critical issues
critical = [i for i in data["prioritized_issues"] if i["severity"] == "CRITICAL"]

# Get outreach stats
outreach = data["skills_results"]["outreach_analyzer"]
print(f"Email coverage: {outreach['email_outreach']['email_coverage_pct']}%")
```

---

## Adding a New Skill

To add a new analysis skill:

1. Create `skills/your_skill.py` with a `run()` function that returns a dict with `status`, `issues`, and `issues_count`
2. Register it in `agent.py` by adding an entry to the `SKILLS` list
3. Optionally create `.claude/skills/your_skill/SKILL.md` for Claude Code integration

Skill template:

```python
from skills.data_loader import load_leads, _find_project_root

SKILL_NAME = "your_skill"

def run():
    root = _find_project_root()
    leads = load_leads(root)

    issues = []
    # Your analysis logic here
    issues.append({
        "severity": "HIGH",        # CRITICAL, HIGH, MEDIUM, or LOW
        "area": "What It's About",
        "finding": "What the data shows",
        "recommendation": "What to do about it",
    })

    return {
        "skill": SKILL_NAME,
        "status": "success",
        "issues": issues,
        "issues_count": len(issues),
    }
```

---

## Latest Results (2026-02-21)

The last run found **54 improvement areas**:

| Severity | Count |
|----------|-------|
| CRITICAL | 2 |
| HIGH | 20 |
| MEDIUM | 29 |
| LOW | 3 |

**Top 5 things to fix:**

1. Only using 3 of 12 marketing channels (29.2% utilization)
2. Only 8 photos — target is 25+ (the #1 booking limiter)
3. 2-sentence description vs competitor multi-paragraph narratives
4. Guest capacity below competitor average
5. 466 WhatsApp leads untouched (0% contacted)
