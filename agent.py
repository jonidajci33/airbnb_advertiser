#!/usr/bin/env python3
"""
Airbnb Business Improvement Agent
===================================
Master orchestrator that runs every analysis skill one by one,
collects all findings, and produces a consolidated improvement report.

Skills executed (in order):
  1. data_loader         — Load all data sources
  2. outreach_analyzer   — Analyze email/WhatsApp campaign effectiveness
  3. lead_quality_analyzer — Analyze lead database quality
  4. property_analyzer   — Analyze property listing performance
  5. pricing_analyzer    — Analyze pricing strategy
  6. marketing_analyzer  — Analyze marketing channels
  7. competitor_analyzer — Benchmark against competitors
  8. review_analyzer     — Analyze reviews and guest experience

Output: improvement_report.md — prioritized list of things to improve
"""

import sys
import json
from datetime import datetime
from pathlib import Path

# Add project root to path so skills can be imported
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from skills import data_loader
from skills import outreach_analyzer
from skills import lead_quality_analyzer
from skills import property_analyzer
from skills import pricing_analyzer
from skills import marketing_analyzer
from skills import competitor_analyzer
from skills import review_analyzer

# ─── Skill Registry ─────────────────────────────────────────────────────────
SKILLS = [
    {
        "name": "data_loader",
        "module": data_loader,
        "description": "Loads all business data (leads, logs, property info)",
        "order": 1,
    },
    {
        "name": "outreach_analyzer",
        "module": outreach_analyzer,
        "description": "Analyzes email & WhatsApp outreach effectiveness",
        "order": 2,
    },
    {
        "name": "lead_quality_analyzer",
        "module": lead_quality_analyzer,
        "description": "Analyzes lead database quality and completeness",
        "order": 3,
    },
    {
        "name": "property_analyzer",
        "module": property_analyzer,
        "description": "Analyzes property listing performance and gaps",
        "order": 4,
    },
    {
        "name": "pricing_analyzer",
        "module": pricing_analyzer,
        "description": "Analyzes pricing strategy and revenue optimization",
        "order": 5,
    },
    {
        "name": "marketing_analyzer",
        "module": marketing_analyzer,
        "description": "Analyzes marketing channel effectiveness",
        "order": 6,
    },
    {
        "name": "competitor_analyzer",
        "module": competitor_analyzer,
        "description": "Benchmarks against competitors and market",
        "order": 7,
    },
    {
        "name": "review_analyzer",
        "module": review_analyzer,
        "description": "Analyzes guest reviews and experience quality",
        "order": 8,
    },
]


def run_all_skills():
    """Execute each skill in order and collect results."""
    results = {}
    all_issues = []

    print()
    print("=" * 70)
    print("  AIRBNB BUSINESS IMPROVEMENT AGENT")
    print("  Running all analysis skills...")
    print("=" * 70)
    print()

    for skill in sorted(SKILLS, key=lambda s: s["order"]):
        name = skill["name"]
        print(f"  [{skill['order']}/{len(SKILLS)}] Running: {name}")
        print(f"       {skill['description']}")

        try:
            result = skill["module"].run()
            results[name] = result

            # Collect issues from this skill
            if isinstance(result, dict) and "issues" in result:
                for issue in result["issues"]:
                    issue["source_skill"] = name
                    all_issues.append(issue)

            status = result.get("status", "unknown") if isinstance(result, dict) else "success"
            issue_count = result.get("issues_count", 0) if isinstance(result, dict) else 0
            print(f"       Status: {status} | Issues found: {issue_count}")

        except Exception as e:
            print(f"       ERROR: {e}")
            results[name] = {"status": "error", "error": str(e)}

        print()

    return results, all_issues


def prioritize_issues(all_issues):
    """Sort and prioritize all issues by severity and actionability."""
    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}

    sorted_issues = sorted(
        all_issues,
        key=lambda i: (severity_order.get(i.get("severity", "LOW"), 4), i.get("area", ""))
    )

    return sorted_issues


def generate_report(results, prioritized_issues):
    """Generate the final improvement report as Markdown."""

    report_lines = [
        "# Airbnb Business Improvement Report",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"**Property:** Lulebore Apartment 1, Central Tirana, Albania",
        f"**Analysis Skills Run:** {len(results)}",
        f"**Total Issues Found:** {len(prioritized_issues)}",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
    ]

    # Count by severity
    severity_counts = {}
    for issue in prioritized_issues:
        sev = issue.get("severity", "LOW")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    report_lines.append(
        f"This analysis identified **{len(prioritized_issues)} improvement areas** across 7 business dimensions:"
    )
    report_lines.append("")
    report_lines.append(f"| Severity | Count |")
    report_lines.append(f"|----------|-------|")
    for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
        if sev in severity_counts:
            report_lines.append(f"| **{sev}** | {severity_counts[sev]} |")
    report_lines.append("")

    # Key data points from skills
    data_result = results.get("data_loader", {})
    if isinstance(data_result, dict) and "summary" in data_result:
        summary = data_result["summary"]
        report_lines.extend([
            "### Key Business Metrics",
            "",
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| Total leads in database | {summary.get('total_leads', 'N/A')} |",
            f"| Leads with phone | {summary.get('leads_with_phone', 'N/A')} |",
            f"| Leads with email | {summary.get('leads_with_email', 'N/A')} |",
            f"| Leads emailed | {summary.get('leads_emailed', 'N/A')} |",
            f"| Leads messaged (WhatsApp) | {summary.get('leads_messaged', 'N/A')} |",
            f"| Email success rate | {summary.get('email_successes', 0)}/{summary.get('email_successes', 0) + summary.get('email_failures', 0)} |",
            "",
        ])

    report_lines.extend([
        "---",
        "",
        "## All Improvements (Prioritized)",
        "",
    ])

    # Group by severity
    current_severity = None
    for idx, issue in enumerate(prioritized_issues, 1):
        severity = issue.get("severity", "LOW")

        if severity != current_severity:
            current_severity = severity
            emoji = {"CRITICAL": "!!!", "HIGH": "!!", "MEDIUM": "!", "LOW": "~"}
            report_lines.extend([
                f"### {severity} Priority {'(' + str(severity_counts.get(severity, 0)) + ' items)'}",
                "",
            ])

        report_lines.extend([
            f"#### {idx}. {issue.get('area', 'Unknown')}",
            f"**Source:** {issue.get('source_skill', 'unknown').replace('_', ' ').title()}",
            "",
            f"**Finding:** {issue.get('finding', '')}",
            "",
            f"**Recommendation:** {issue.get('recommendation', '')}",
            "",
            f"**Estimated Impact:** {issue.get('estimated_impact', 'Significant improvement')}" if issue.get('estimated_impact') else "",
            "",
            "---",
            "",
        ])

    # Add action plan section
    report_lines.extend([
        "## 30-Day Action Plan",
        "",
        "### Week 1 (Critical Fixes)",
        "",
    ])

    week1 = [i for i in prioritized_issues if i.get("severity") == "CRITICAL"]
    for i, issue in enumerate(week1, 1):
        report_lines.append(f"- [ ] {issue.get('area', '')}: {issue.get('recommendation', '')[:100]}")
    report_lines.append("")

    report_lines.extend([
        "### Week 2 (High Priority)",
        "",
    ])
    week2 = [i for i in prioritized_issues if i.get("severity") == "HIGH"][:5]
    for i, issue in enumerate(week2, 1):
        report_lines.append(f"- [ ] {issue.get('area', '')}: {issue.get('recommendation', '')[:100]}")
    report_lines.append("")

    report_lines.extend([
        "### Week 3-4 (Medium Priority)",
        "",
    ])
    week34 = [i for i in prioritized_issues if i.get("severity") == "MEDIUM"][:5]
    for i, issue in enumerate(week34, 1):
        report_lines.append(f"- [ ] {issue.get('area', '')}: {issue.get('recommendation', '')[:100]}")
    report_lines.append("")

    report_lines.extend([
        "---",
        "",
        "## Skills Execution Summary",
        "",
        "| # | Skill | Status | Issues |",
        "|---|-------|--------|--------|",
    ])

    for skill in sorted(SKILLS, key=lambda s: s["order"]):
        name = skill["name"]
        result = results.get(name, {})
        status = result.get("status", "unknown") if isinstance(result, dict) else "error"
        issues = result.get("issues_count", 0) if isinstance(result, dict) else 0
        report_lines.append(f"| {skill['order']} | {name.replace('_', ' ').title()} | {status} | {issues} |")

    report_lines.extend([
        "",
        "---",
        "",
        "*Generated by Airbnb Business Improvement Agent*",
    ])

    return "\n".join(report_lines)


def main():
    """Main agent entry point."""
    print()
    print("*" * 70)
    print("*" + " " * 68 + "*")
    print("*   AIRBNB BUSINESS IMPROVEMENT AGENT                              *")
    print("*   Analyzing your sales, rentals, and operations...               *")
    print("*" + " " * 68 + "*")
    print("*" * 70)
    print()

    # Step 1: Run all skills
    results, all_issues = run_all_skills()

    # Step 2: Prioritize issues
    prioritized = prioritize_issues(all_issues)

    # Step 3: Generate report
    report = generate_report(results, prioritized)

    # Step 4: Save report
    report_path = PROJECT_ROOT / "improvement_report.md"
    report_path.write_text(report, encoding="utf-8")

    # Step 5: Save raw results as JSON
    json_path = PROJECT_ROOT / "improvement_data.json"
    # Convert to serializable format
    serializable_results = {}
    for key, value in results.items():
        if isinstance(value, dict):
            serializable_results[key] = value
        else:
            serializable_results[key] = str(value)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "generated": datetime.now().isoformat(),
            "skills_results": serializable_results,
            "prioritized_issues": prioritized,
        }, f, indent=2, default=str)

    # Print final summary
    severity_counts = {}
    for issue in prioritized:
        sev = issue.get("severity", "LOW")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    print()
    print("=" * 70)
    print("  ANALYSIS COMPLETE")
    print("=" * 70)
    print()
    print(f"  Skills executed:    {len(results)}")
    print(f"  Total issues:       {len(prioritized)}")
    print(f"  Critical:           {severity_counts.get('CRITICAL', 0)}")
    print(f"  High:               {severity_counts.get('HIGH', 0)}")
    print(f"  Medium:             {severity_counts.get('MEDIUM', 0)}")
    print(f"  Low:                {severity_counts.get('LOW', 0)}")
    print()
    print(f"  Report saved to:    {report_path}")
    print(f"  Raw data saved to:  {json_path}")
    print()

    # Print top 10 improvements
    print("  TOP 10 THINGS TO IMPROVE:")
    print("  " + "-" * 60)
    for i, issue in enumerate(prioritized[:10], 1):
        print(f"  {i:2d}. [{issue['severity']:8s}] {issue['area']}")
        print(f"      {issue.get('finding', '')[:70]}")
        print()

    print("=" * 70)
    print()

    return results, prioritized


if __name__ == "__main__":
    main()
