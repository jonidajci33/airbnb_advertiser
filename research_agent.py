#!/usr/bin/env python3
"""
Airbnb Competitor Research Agent
=================================
Master orchestrator that researches what other Airbnb businesses in Albania
are doing to maximize profit, runs 7 specialized research skills,
and produces actionable advice on how to improve your business.

Skills executed (in order):
  1. market_intel            — Albanian Airbnb market stats, trends, your position
  2. top_hosts_tactics       — What top Albanian hosts do differently
  3. pricing_mastery         — Advanced pricing strategies used by top earners
  4. revenue_streams         — Upsells, direct bookings, multi-platform, ancillary revenue
  5. medical_tourism_strategy — Medical tourism accommodation best practices worldwide
  6. guest_experience        — Guest experience tactics that drive 5-star reviews
  7. digital_presence        — Digital marketing, social media, SEO, paid ads

Output: competitor_research_report.md — what others do + what you should do
"""

import sys
import json
from datetime import datetime
from pathlib import Path

# Add project root to path so skills can be imported
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from research_skills import market_intel
from research_skills import top_hosts_tactics
from research_skills import pricing_mastery
from research_skills import revenue_streams
from research_skills import medical_tourism_strategy
from research_skills import guest_experience
from research_skills import digital_presence

# ─── Skill Registry ─────────────────────────────────────────────────────────
SKILLS = [
    {
        "name": "market_intel",
        "module": market_intel,
        "description": "Albanian Airbnb market trends, statistics, and your position",
        "order": 1,
    },
    {
        "name": "top_hosts_tactics",
        "module": top_hosts_tactics,
        "description": "What top-performing Albanian Airbnb hosts do differently",
        "order": 2,
    },
    {
        "name": "pricing_mastery",
        "module": pricing_mastery,
        "description": "Advanced pricing strategies used by top earners",
        "order": 3,
    },
    {
        "name": "revenue_streams",
        "module": revenue_streams,
        "description": "Upsells, direct bookings, multi-platform, ancillary revenue",
        "order": 4,
    },
    {
        "name": "medical_tourism_strategy",
        "module": medical_tourism_strategy,
        "description": "Medical tourism accommodation best practices worldwide",
        "order": 5,
    },
    {
        "name": "guest_experience",
        "module": guest_experience,
        "description": "Guest experience tactics that drive 5-star reviews",
        "order": 6,
    },
    {
        "name": "digital_presence",
        "module": digital_presence,
        "description": "Digital marketing, social media, SEO, paid ads strategies",
        "order": 7,
    },
]


def run_all_skills():
    """Execute each skill in order and collect results."""
    results = {}
    all_issues = []

    print()
    print("=" * 70)
    print("  AIRBNB COMPETITOR RESEARCH AGENT")
    print("  Researching what top hosts in Albania are doing...")
    print("=" * 70)
    print()

    for skill in sorted(SKILLS, key=lambda s: s["order"]):
        name = skill["name"]
        print(f"  [{skill['order']}/{len(SKILLS)}] Running: {name}")
        print(f"       {skill['description']}")

        try:
            result = skill["module"].run()
            results[name] = result

            if isinstance(result, dict) and "issues" in result:
                for issue in result["issues"]:
                    issue["source_skill"] = name
                    all_issues.append(issue)

            status = result.get("status", "unknown") if isinstance(result, dict) else "success"
            issue_count = result.get("issues_count", 0) if isinstance(result, dict) else 0
            print(f"       Status: {status} | Findings: {issue_count}")

        except Exception as e:
            print(f"       ERROR: {e}")
            import traceback
            traceback.print_exc()
            results[name] = {"status": "error", "error": str(e)}

        print()

    return results, all_issues


def prioritize_issues(all_issues):
    """Sort all issues by severity."""
    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    return sorted(
        all_issues,
        key=lambda i: (severity_order.get(i.get("severity", "LOW"), 4), i.get("area", ""))
    )


def generate_report(results, prioritized_issues):
    """Generate the competitor research report as Markdown."""

    severity_counts = {}
    for issue in prioritized_issues:
        sev = issue.get("severity", "LOW")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    lines = [
        "# What Other Airbnb Businesses in Albania Are Doing — And How You Can Beat Them",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Property:** Lulebore Apartment 1, Central Tirana, Albania",
        f"**Research Skills Run:** {len(results)}",
        f"**Total Findings:** {len(prioritized_issues)}",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        "This report analyzes what successful Airbnb hosts in Albania and medical tourism",
        "accommodation providers worldwide are doing to maximize their profits. Each finding",
        "compares their tactics against your current setup and provides specific advice.",
        "",
        f"| Severity | Count |",
        f"|----------|-------|",
    ]
    for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
        if sev in severity_counts:
            lines.append(f"| **{sev}** | {severity_counts[sev]} |")

    lines.extend([
        "",
        "### Key Market Facts",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        "| Albania total Airbnb listings | 23,000 |",
        "| Tirana active listings | 3,488 |",
        "| Albania Airbnb revenue 2024 | EUR 85 million |",
        "| Albania visitors 2024 | 11.7 million |",
        "| Medical tourists/year | 80,000+ |",
        "| Dental tourism growth since 2020 | 400% |",
        "| Tirana avg nightly rate | $49/night |",
        "| Top 10% monthly income | $1,400+/month |",
        "| Your monthly income (est.) | ~EUR 540/month |",
        "",
        "---",
        "",
    ])

    # Group issues by skill
    skill_issues = {}
    for issue in prioritized_issues:
        source = issue.get("source_skill", "unknown")
        if source not in skill_issues:
            skill_issues[source] = []
        skill_issues[source].append(issue)

    # Write by severity
    lines.append("## All Findings (Prioritized)")
    lines.append("")

    current_severity = None
    for idx, issue in enumerate(prioritized_issues, 1):
        severity = issue.get("severity", "LOW")

        if severity != current_severity:
            current_severity = severity
            lines.extend([
                f"### {severity} Priority ({severity_counts.get(severity, 0)} items)",
                "",
            ])

        source_name = issue.get("source_skill", "unknown").replace("_", " ").title()
        lines.extend([
            f"#### {idx}. {issue.get('area', 'Unknown')}",
            f"**Source:** {source_name}",
            "",
            f"**What others do:** {issue.get('what_others_do', issue.get('what_top_hosts_do', issue.get('what_world_class_does', 'N/A')))}",
            "",
            f"**Your gap:** {issue.get('finding', '')}",
            "",
            f"**Action:** {issue.get('recommendation', '')}",
            "",
        ])
        if issue.get("estimated_impact"):
            lines.append(f"**Impact:** {issue['estimated_impact']}")
            lines.append("")
        if issue.get("your_situation"):
            lines.append(f"**Your situation:** {issue['your_situation']}")
            lines.append("")

        lines.extend(["---", ""])

    # Revenue roadmap
    lines.extend([
        "## Revenue Growth Roadmap",
        "",
        "Based on what top Albanian hosts achieve, here's your path from current to top 10%:",
        "",
        "| Stage | Monthly Revenue | What Changes |",
        "|-------|----------------|-------------|",
        "| **Current** | ~EUR 540 | EUR 45/night, ~40% occupancy, 2 platforms, no upsells |",
        "| **Month 1** | ~EUR 700 | Dynamic pricing tool (+30% revenue) |",
        "| **Month 2** | ~EUR 860 | Rate increase to EUR 55 (justified by ratings) |",
        "| **Month 3** | ~EUR 1,000 | Multi-platform + channel manager (+15% occupancy) |",
        "| **Month 4** | ~EUR 1,100 | Upsells: airport transfer, early check-in, welcome basket |",
        "| **Month 6** | ~EUR 1,200 | Direct bookings saving 15% fees + email remarketing |",
        "| **Month 12** | ~EUR 1,400+ | Full medical tourism packages, clinic partnerships, social media |",
        "",
        "**That's a 2.6x revenue increase — from EUR 540 to EUR 1,400+/month.**",
        "",
        "---",
        "",
    ])

    # 90-day action plan
    lines.extend([
        "## 90-Day Action Plan",
        "",
        "### Week 1: Quick Wins (Cost: ~EUR 20)",
        "",
    ])

    week1_actions = [
        "Sign up for PriceLabs ($19.99/month) — expected +30% revenue immediately",
        "Enable weekly discount (10-15%) and monthly discount (20-30%) on Airbnb",
        "Set up Hospitable ($29/month) for automated guest messaging",
        "Create a detailed cleaning checklist and quality protocol",
    ]
    for a in week1_actions:
        lines.append(f"- [ ] {a}")

    lines.extend([
        "",
        "### Week 2: Photography & Listing (Cost: EUR 300-500)",
        "",
    ])
    week2_actions = [
        "Hire a professional photographer (30-50 images, EUR 300-500)",
        "Record a 30-60 second video tour with your phone",
        "Rewrite listing description: 4 paragraphs (hook, rooms, neighborhood, medical tourism)",
        "Complete ALL amenity checkboxes on Airbnb",
        "Add listing in English, Italian, and German",
    ]
    for a in week2_actions:
        lines.append(f"- [ ] {a}")

    lines.extend([
        "",
        "### Week 3-4: Revenue Expansion (Cost: EUR 50)",
        "",
    ])
    week34_actions = [
        "Buy recovery amenities: ice packs, blender, neck pillow, dark towels (EUR 50)",
        "Create 'Dental Recovery Package' and 'Hair Transplant Package' descriptions",
        "Set up Google Business Profile as 'Tourist Accommodation'",
        "Create Instagram @lulebore.apartment, post first 5 apartment photos",
        "Set up early check-in (EUR 10-20/hr) and airport transfer (EUR 15-25) as upsells",
    ]
    for a in week34_actions:
        lines.append(f"- [ ] {a}")

    lines.extend([
        "",
        "### Month 2: Partnerships & Direct (Cost: EUR 19-40/month)",
        "",
    ])
    month2_actions = [
        "Build direct booking page with Carrd (EUR 19/year) or Hospitable",
        "Install StayFi for WiFi email capture (captures every guest email)",
        "Visit top 10 dental clinics in person with printed flyers + QR code",
        "Offer 10 free nights across clinics as trial partnership",
        "Register on PlacidWay medical tourism platform",
        "Start WhatsApp outreach to 466 un-contacted leads",
    ]
    for a in month2_actions:
        lines.append(f"- [ ] {a}")

    lines.extend([
        "",
        "### Month 3: Scale (Cost: EUR 250/month for ads)",
        "",
    ])
    month3_actions = [
        "Launch Google Ads targeting 'dental tourism accommodation Tirana' (EUR 5/day)",
        "Launch Facebook Ads targeting medical tourists in Italy/UK/Germany (EUR 3/day)",
        "Publish first blog post: 'Complete Guide to Your Dental Trip to Tirana'",
        "Create YouTube video: apartment tour showing recovery features",
        "Set up automated email drip: post-stay → 30-day → 90-day → seasonal",
        "Negotiate formal commission agreements with responding clinics",
    ]
    for a in month3_actions:
        lines.append(f"- [ ] {a}")

    lines.extend([
        "",
        "---",
        "",
        "## Skills Execution Summary",
        "",
        "| # | Skill | Status | Findings |",
        "|---|-------|--------|----------|",
    ])

    for skill in sorted(SKILLS, key=lambda s: s["order"]):
        name = skill["name"]
        result = results.get(name, {})
        status = result.get("status", "unknown") if isinstance(result, dict) else "error"
        issues = result.get("issues_count", 0) if isinstance(result, dict) else 0
        lines.append(f"| {skill['order']} | {name.replace('_', ' ').title()} | {status} | {issues} |")

    lines.extend([
        "",
        "---",
        "",
        "*Generated by Airbnb Competitor Research Agent*",
    ])

    return "\n".join(lines)


def main():
    """Main agent entry point."""
    print()
    print("*" * 70)
    print("*" + " " * 68 + "*")
    print("*   AIRBNB COMPETITOR RESEARCH AGENT                               *")
    print("*   Researching what top hosts in Albania are doing...              *")
    print("*" + " " * 68 + "*")
    print("*" * 70)
    print()

    # Step 1: Run all skills
    results, all_issues = run_all_skills()

    # Step 2: Prioritize
    prioritized = prioritize_issues(all_issues)

    # Step 3: Generate report
    report = generate_report(results, prioritized)

    # Step 4: Save report
    report_path = PROJECT_ROOT / "competitor_research_report.md"
    report_path.write_text(report, encoding="utf-8")

    # Step 5: Save raw data
    json_path = PROJECT_ROOT / "competitor_research_data.json"
    serializable = {}
    for key, value in results.items():
        if isinstance(value, dict):
            serializable[key] = value
        else:
            serializable[key] = str(value)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "generated": datetime.now().isoformat(),
            "skills_results": serializable,
            "prioritized_issues": prioritized,
        }, f, indent=2, default=str)

    # Print final summary
    severity_counts = {}
    for issue in prioritized:
        sev = issue.get("severity", "LOW")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    print()
    print("=" * 70)
    print("  RESEARCH COMPLETE")
    print("=" * 70)
    print()
    print(f"  Skills executed:    {len(results)}")
    print(f"  Total findings:     {len(prioritized)}")
    print(f"  Critical:           {severity_counts.get('CRITICAL', 0)}")
    print(f"  High:               {severity_counts.get('HIGH', 0)}")
    print(f"  Medium:             {severity_counts.get('MEDIUM', 0)}")
    print(f"  Low:                {severity_counts.get('LOW', 0)}")
    print()
    print(f"  Report saved to:    {report_path}")
    print(f"  Raw data saved to:  {json_path}")
    print()

    # Top findings
    print("  TOP 10 THINGS OTHER HOSTS DO THAT YOU DON'T:")
    print("  " + "-" * 60)
    for i, issue in enumerate(prioritized[:10], 1):
        print(f"  {i:2d}. [{issue['severity']:8s}] {issue['area']}")
        finding = issue.get('finding', '')[:70]
        print(f"      {finding}")
        print()

    # Revenue roadmap
    print("  REVENUE GROWTH PATH:")
    print("  " + "-" * 60)
    print("    Now:       ~EUR  540/month")
    print("    Month 1:   ~EUR  700/month (+dynamic pricing)")
    print("    Month 2:   ~EUR  860/month (+rate increase)")
    print("    Month 3:   ~EUR 1,000/month (+multi-platform)")
    print("    Month 6:   ~EUR 1,200/month (+upsells, direct)")
    print("    Month 12:  ~EUR 1,400/month (+medical packages)")
    print("    = 2.6x growth potential")
    print()
    print("=" * 70)
    print()

    return results, prioritized


if __name__ == "__main__":
    main()
