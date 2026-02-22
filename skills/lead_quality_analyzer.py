"""
Skill: Lead Quality Analyzer
Analyzes the quality and completeness of the lead database.

Metrics analyzed:
  - Data completeness (name, phone, email, website, score)
  - Category distribution and balance
  - Proximity score distribution
  - Date added timeline (growth rate)
  - Data quality issues (missing fields, invalid data)
  - Lead source diversity
"""

from datetime import datetime, date
from collections import Counter
from skills.data_loader import load_leads, _find_project_root

SKILL_NAME = "lead_quality_analyzer"
DESCRIPTION = "Analyzes lead database quality, completeness, and growth patterns"


def analyze_completeness(leads):
    """Analyze how complete each lead's data is."""
    total = len(leads)
    if total == 0:
        return {"error": "No leads found"}

    fields = {
        "name": sum(1 for l in leads if l["name"]),
        "location": sum(1 for l in leads if l["location"]),
        "phone": sum(1 for l in leads if l["phone"]),
        "email": sum(1 for l in leads if l["email"]),
        "website": sum(1 for l in leads if l["website"]),
        "category": sum(1 for l in leads if l["category"]),
        "score": sum(1 for l in leads if l["score"] and l["score"] != 0),
        "date_added": sum(1 for l in leads if l["date_added"]),
    }

    completeness = {}
    for field, count in fields.items():
        completeness[field] = {
            "count": count,
            "missing": total - count,
            "pct": round(count / total * 100, 1),
        }

    # Fully complete leads (have name + phone + email + category)
    fully_complete = sum(
        1 for l in leads
        if l["name"] and l["phone"] and l["email"] and l["category"]
    )

    return {
        "total_leads": total,
        "field_completeness": completeness,
        "fully_complete_leads": fully_complete,
        "fully_complete_pct": round(fully_complete / total * 100, 1),
    }


def analyze_categories(leads):
    """Analyze category distribution."""
    categories = Counter(l["category"] or "NONE" for l in leads)
    total = len(leads)

    distribution = {}
    for cat, count in categories.most_common():
        distribution[cat] = {
            "count": count,
            "pct": round(count / total * 100, 1),
        }

    return distribution


def analyze_proximity_scores(leads):
    """Analyze the distribution of proximity scores."""
    scores = [l["score"] for l in leads if l["score"] is not None]

    if not scores:
        return {"error": "No scores found"}

    score_dist = Counter(scores)
    total_scored = len(scores)

    # Group into buckets
    high_proximity = sum(1 for s in scores if s >= 8)     # 1-2km
    medium_proximity = sum(1 for s in scores if 5 <= s < 8)  # 3-12km
    low_proximity = sum(1 for s in scores if s < 5)        # 12km+

    return {
        "total_scored": total_scored,
        "unscored": len(leads) - total_scored,
        "avg_score": round(sum(scores) / len(scores), 1),
        "score_distribution": dict(sorted(score_dist.items())),
        "high_proximity_1_2km": high_proximity,
        "medium_proximity_3_12km": medium_proximity,
        "low_proximity_12km_plus": low_proximity,
    }


def analyze_growth_timeline(leads):
    """Analyze when leads were added over time."""
    dated_leads = []
    for l in leads:
        if l["date_added"]:
            try:
                d = l["date_added"][:10]
                dated_leads.append(d)
            except (ValueError, IndexError):
                continue

    if not dated_leads:
        return {"error": "No dated leads found"}

    date_counts = Counter(dated_leads)
    sorted_dates = sorted(date_counts.items())

    return {
        "total_dated": len(dated_leads),
        "first_date": sorted_dates[0][0] if sorted_dates else None,
        "last_date": sorted_dates[-1][0] if sorted_dates else None,
        "leads_by_date": dict(sorted_dates),
        "unique_add_dates": len(date_counts),
    }


def identify_issues(completeness, categories, scores, growth):
    """Identify data quality issues and improvement areas."""
    issues = []

    # Email coverage gap
    email_data = completeness["field_completeness"].get("email", {})
    if email_data.get("pct", 0) < 40:
        issues.append({
            "severity": "HIGH",
            "area": "Low Email Coverage",
            "finding": f"Only {email_data.get('pct', 0)}% of leads have email addresses ({email_data.get('missing', 0)} missing)",
            "recommendation": "Run email_scraper.py on leads with websites to extract more emails. Consider manual lookup for high-score leads.",
        })

    # Phone coverage
    phone_data = completeness["field_completeness"].get("phone", {})
    if phone_data.get("pct", 0) < 70:
        issues.append({
            "severity": "MEDIUM",
            "area": "Phone Coverage Gap",
            "finding": f"Only {phone_data.get('pct', 0)}% of leads have phone numbers ({phone_data.get('missing', 0)} missing)",
            "recommendation": "Re-run scraper to try to fill phone numbers, or manually look up phones for top-scoring leads.",
        })

    # Category imbalance
    dental_count = categories.get("DENTAL", {}).get("count", 0)
    hair_count = categories.get("HAIR_TRANSPLANT", {}).get("count", 0)
    unknown_count = categories.get("UNKNOWN", {}).get("count", 0) + categories.get("NONE", {}).get("count", 0)

    if hair_count < dental_count * 0.15:
        issues.append({
            "severity": "MEDIUM",
            "area": "Hair Transplant Lead Shortage",
            "finding": f"Only {hair_count} hair transplant leads vs {dental_count} dental leads",
            "recommendation": "Run more targeted hair transplant queries in the scraper. Albania's hair transplant market is growing fast.",
        })

    if unknown_count > completeness["total_leads"] * 0.1:
        issues.append({
            "severity": "LOW",
            "area": "Uncategorized Leads",
            "finding": f"{unknown_count} leads have no category (UNKNOWN/NONE)",
            "recommendation": "Review uncategorized leads and assign them to DENTAL or HAIR_TRANSPLANT based on their website/name.",
        })

    # Low completeness
    if completeness["fully_complete_pct"] < 30:
        issues.append({
            "severity": "HIGH",
            "area": "Low Data Completeness",
            "finding": f"Only {completeness['fully_complete_pct']}% of leads have all key fields (name + phone + email + category)",
            "recommendation": "Focus on enriching existing leads before scraping new ones. Quality contacts convert better than quantity.",
        })

    # Score distribution
    if isinstance(scores, dict) and "avg_score" in scores:
        if scores["low_proximity_12km_plus"] > scores["high_proximity_1_2km"]:
            issues.append({
                "severity": "LOW",
                "area": "Many Distant Leads",
                "finding": f"{scores['low_proximity_12km_plus']} leads are 12km+ away vs {scores['high_proximity_1_2km']} within 2km",
                "recommendation": "Prioritize outreach to high-proximity leads (score 8-10). Nearby clinics are more likely to partner.",
            })

    # Growth stagnation
    if isinstance(growth, dict) and "leads_by_date" in growth:
        dates = list(growth["leads_by_date"].keys())
        if len(dates) <= 2:
            issues.append({
                "severity": "MEDIUM",
                "area": "Lead Acquisition Stalled",
                "finding": f"Leads were only added on {len(dates)} different dates",
                "recommendation": "Set up regular scraping sessions (weekly) to keep discovering new clinics. The market is growing.",
            })

    # No website data
    website_data = completeness["field_completeness"].get("website", {})
    if website_data.get("pct", 0) < 50:
        issues.append({
            "severity": "LOW",
            "area": "Missing Website Data",
            "finding": f"Only {website_data.get('pct', 0)}% of leads have website URLs",
            "recommendation": "Leads with websites are more likely to be serious businesses. Website data also enables email scraping.",
        })

    return issues


def run():
    """Main skill entry point."""
    root = _find_project_root()
    leads = load_leads(root)

    if isinstance(leads, dict) and "error" in leads:
        return {"skill": SKILL_NAME, "status": "error", "error": leads["error"]}

    completeness = analyze_completeness(leads)
    categories = analyze_categories(leads)
    scores = analyze_proximity_scores(leads)
    growth = analyze_growth_timeline(leads)
    issues = identify_issues(completeness, categories, scores, growth)

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "completeness": completeness,
        "categories": categories,
        "proximity_scores": scores,
        "growth_timeline": growth,
        "issues": issues,
        "issues_count": len(issues),
    }

    # Print summary
    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  DATA COMPLETENESS:")
    print(f"    Total leads:         {completeness['total_leads']}")
    print(f"    Fully complete:      {completeness['fully_complete_leads']} ({completeness['fully_complete_pct']}%)")
    for field, data in completeness["field_completeness"].items():
        print(f"    {field:20s} {data['count']:4d} ({data['pct']}%)")
    print(f"\n  CATEGORIES:")
    for cat, data in categories.items():
        print(f"    {cat:20s} {data['count']:4d} ({data['pct']}%)")
    if isinstance(scores, dict) and "avg_score" in scores:
        print(f"\n  PROXIMITY SCORES:")
        print(f"    Average score:       {scores['avg_score']}")
        print(f"    High (1-2km):        {scores['high_proximity_1_2km']}")
        print(f"    Medium (3-12km):     {scores['medium_proximity_3_12km']}")
        print(f"    Low (12km+):         {scores['low_proximity_12km_plus']}")
    print(f"\n  ISSUES FOUND: {len(issues)}")
    for i, issue in enumerate(issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area']}: {issue['finding']}")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
