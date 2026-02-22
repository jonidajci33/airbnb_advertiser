"""
Price Predictor Agent - Master script for Lulebore Apartment 1 pricing optimization.

Orchestrates: historical_demand -> competitor_analyzer -> market_benchmarks -> price_optimizer
Uses real competitor data (nearby properties, max 3 guests) for accurate pricing.
Outputs: pricing_recommendations.md, pricing_data.json
"""

import json
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from price_skills.historical_demand import analyze_demand
from price_skills.competitor_analyzer import analyze_competitors
from price_skills.market_benchmarks import compile_benchmarks
from price_skills.price_optimizer import optimize_prices


def run():
    """Run the complete price prediction pipeline."""
    print(f"\n{'=' * 70}")
    print(f"  PRICE PREDICTOR AGENT - Lulebore Apartment 1")
    print(f"  Run date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'=' * 70}\n")

    all_issues = []

    # Step 1: Analyze historical demand
    print("  [1/4] Analyzing historical demand...")
    demand_data = analyze_demand()
    all_issues.extend(demand_data["issues"])
    overall = demand_data["overall"]
    print(f"         + {overall['months_with_data']} months with data")
    print(f"         + Avg occupancy: {overall['avg_occupancy_pct']}%")
    print(f"         + Avg ADR: EUR {overall['avg_adr']}")
    print(f"         + Avg demand index: {overall['avg_demand_index']}")

    # Step 2: Analyze competitors (nearby, max 3 guests)
    print("\n  [2/4] Analyzing competitors (max 3 guests, central Tirana)...")
    comp_data = analyze_competitors()
    all_issues.extend(comp_data.get("issues", []))
    pos = comp_data.get("your_position", {})
    print(f"         + {comp_data['competitor_count']} competitors analyzed")
    print(f"         + Competitor avg price: EUR {comp_data['avg_price_eur']}")
    print(f"         + Competitor median price: EUR {comp_data['median_price_eur']}")
    print(f"         + Price range (P25-P75): EUR {comp_data['p25_price_eur']}-{comp_data['p75_price_eur']}")
    if pos:
        print(f"         + Your price percentile: {pos.get('price_percentile', 'N/A')}%")
        print(f"         + Your rating rank: {pos.get('rating_rank', 'N/A')}")

    # Step 3: Compile market benchmarks (uses competitor data)
    print("\n  [3/4] Compiling market benchmarks from competitor data...")
    benchmark_data = compile_benchmarks()
    rp = benchmark_data["rating_premium"]
    mc = benchmark_data["market_context"]
    print(f"         + Rating: {rp['airbnb_rating']}/5 Airbnb + {rp['booking_rating']}/10 Booking")
    print(f"         + Rating premium: {rp['applied_premium_pct']}% (from competitor tier analysis)")
    print(f"         + Premium tier avg: EUR {rp['premium_tier_avg_eur']}")
    print(f"         + Overall competitor avg: EUR {rp['overall_avg_eur']}")

    # Step 4: Optimize prices
    print("\n  [4/4] Computing optimal prices...")
    price_data = optimize_prices(demand_data, benchmark_data)
    s = price_data["summary"]
    print(f"         + Avg recommended rate: EUR {s['avg_recommended_rate']}")
    print(f"         + Rate range: EUR {s['min_recommended_rate']} - EUR {s['max_recommended_rate']}")
    print(f"         + Months above current: {s['months_above_current']}/12")
    print(f"         + Competitors analyzed: {s['competitors_analyzed']}")

    # Generate outputs
    report_path = _generate_report(price_data, demand_data, benchmark_data, comp_data, all_issues)
    print(f"\n         + Saved: {report_path}")

    json_path = _generate_json(price_data, demand_data, benchmark_data, comp_data, all_issues)
    print(f"         + Saved: {json_path}")

    # Print summary
    _print_summary(price_data, benchmark_data, comp_data)

    return {
        "report_path": report_path,
        "json_path": json_path,
        "price_data": price_data,
        "competitor_data": comp_data,
        "issues": all_issues,
    }


def _generate_report(price_data, demand_data, benchmark_data, comp_data, issues):
    """Generate pricing_recommendations.md."""
    recs = price_data["recommendations"]
    scenarios = price_data["revenue_scenarios"]
    rp = benchmark_data["rating_premium"]
    s = price_data["summary"]
    comp_summary = benchmark_data.get("competitor_summary", {})
    pos = comp_data.get("your_position", {})

    lines = []
    lines.append("# Pricing Recommendations - Lulebore Apartment 1\n")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append(f"**Current Rate:** EUR {s['current_flat_rate']}/night (static, no seasonal adjustment)\n")
    lines.append(f"**Based on:** {comp_data['competitor_count']} nearby competitors (max 3 guests, central Tirana)\n")

    # Competitor Analysis section
    lines.append("\n## Competitor Analysis\n")
    lines.append(f"Analyzed **{comp_data['competitor_count']} properties** near Lulebore Apartment 1 ")
    lines.append(f"that accept at most 3 guests (studios and 1-bedroom apartments in central Tirana).\n")

    lines.append("\n### Competitor Price Distribution\n")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Competitors analyzed | {comp_data['competitor_count']} |")
    lines.append(f"| Average price | EUR {comp_data['avg_price_eur']} |")
    lines.append(f"| Median price | EUR {comp_data['median_price_eur']} |")
    lines.append(f"| 25th percentile | EUR {comp_data['p25_price_eur']} |")
    lines.append(f"| 75th percentile | EUR {comp_data['p75_price_eur']} |")
    if pos:
        lines.append(f"| **Your price (EUR {pos.get('your_price_eur', 45)})** | **Percentile: {pos.get('price_percentile', 'N/A')}%** |")
        lines.append(f"| Your rating rank | {pos.get('rating_rank', 'N/A')} |")
        pct = pos.get('price_vs_avg_pct', 0)
        label = "above" if pct > 0 else "below"
        lines.append(f"| Price vs competitor avg | {abs(pct):.1f}% {label} |")

    # Rating tier pricing
    tiers = comp_data.get("rating_tiers", {})
    if tiers:
        lines.append("\n### Price by Rating Tier\n")
        lines.append("| Rating Tier | Count | Avg Price | Median | Range |")
        lines.append("|-------------|-------|-----------|--------|-------|")
        for key in ["premium", "good", "average", "below_avg"]:
            t = tiers.get(key, {})
            if t.get("count", 0) > 0:
                lines.append(f"| {t['label']} | {t['count']} | EUR {t['avg_price_eur']} | "
                             f"EUR {t['median_price_eur']} | EUR {t['min_price_eur']}-{t['max_price_eur']} |")

    # Top competitors
    competitors_list = comp_data.get("competitors", [])
    if competitors_list:
        lines.append("\n### Competitor Listings (sorted by price)\n")
        lines.append("| # | Name | Platform | Price | Rating | Guests |")
        lines.append("|---|------|----------|-------|--------|--------|")
        for i, c in enumerate(competitors_list, 1):
            rating_str = f"{c['rating']}" if c.get('rating') else "N/A"
            lines.append(f"| {i} | {c['name']} | {c['platform']} | EUR {c['price_eur']} | "
                         f"{rating_str} | {c.get('max_guests', 'N/A')} |")

    # Rating premium section
    lines.append("\n## Rating Premium Justification\n")
    lines.append(rp["justification"])
    lines.append(f"\n**Applied premium:** {rp['applied_premium_pct']}% above competitor average\n")

    # Monthly recommendations
    lines.append("\n## Monthly Price Recommendations\n")
    lines.append("| Month | Season | Recommended | Range (Min-Max) | Current | Comp. Avg | Comp. Median | Expected Occ | Expected Rev | Uplift |")
    lines.append("|-------|--------|-------------|-----------------|---------|-----------|--------------|--------------|--------------|--------|")
    for r in recs:
        lines.append(
            f"| {r['month_name']} | {r['season']} | **EUR {r['recommended_rate_eur']:.0f}** | "
            f"EUR {r['rate_range_min_eur']:.0f}-{r['rate_range_max_eur']:.0f} | "
            f"EUR {r['current_rate_eur']} | EUR {r['competitor_avg_rate_eur']:.0f} | "
            f"EUR {r['competitor_median_rate_eur']:.0f} | "
            f"{r['expected_occupancy_pct']:.0f}% | EUR {r['expected_revenue_eur']:,.0f} | "
            f"{r['revenue_uplift_pct']:+.0f}% |"
        )

    # Revenue projections
    lines.append("\n## Revenue Projections\n")
    lines.append("| Scenario | Annual Revenue | Monthly Avg |")
    lines.append("|----------|---------------|-------------|")
    for key in ["current", "recommended", "competitor_average"]:
        sc = scenarios[key]
        lines.append(f"| {sc['label']} | EUR {sc['annual_revenue_eur']:,.2f} | EUR {sc['monthly_avg_eur']:,.2f} |")

    uplift = scenarios["uplift_vs_current"]
    lines.append(f"\n**Annual uplift with recommended pricing:** EUR {uplift['annual_eur']:,.2f} "
                 f"({uplift['annual_pct']:+.1f}%)\n")

    # Seasonal strategy
    lines.append("\n## Seasonal Strategy\n")
    lines.append("### Peak Season (June-September)")
    peak_recs = [r for r in recs if r["season"] == "Peak"]
    if peak_recs:
        avg_peak = sum(r["recommended_rate_eur"] for r in peak_recs) / len(peak_recs)
        lines.append(f"- Recommended range: EUR {min(r['recommended_rate_eur'] for r in peak_recs):.0f} - "
                     f"EUR {max(r['recommended_rate_eur'] for r in peak_recs):.0f}/night")
        lines.append(f"- Average: EUR {avg_peak:.0f}/night")
        avg_comp = sum(r["competitor_avg_rate_eur"] for r in peak_recs) / len(peak_recs)
        lines.append(f"- Competitor average: EUR {avg_comp:.0f}/night")
        lines.append(f"- Maximize rate while maintaining 45-55% occupancy\n")

    lines.append("### Shoulder Season (March-May, October-December)")
    shoulder_recs = [r for r in recs if r["season"] == "Shoulder"]
    if shoulder_recs:
        avg_shoulder = sum(r["recommended_rate_eur"] for r in shoulder_recs) / len(shoulder_recs)
        lines.append(f"- Recommended range: EUR {min(r['recommended_rate_eur'] for r in shoulder_recs):.0f} - "
                     f"EUR {max(r['recommended_rate_eur'] for r in shoulder_recs):.0f}/night")
        lines.append(f"- Average: EUR {avg_shoulder:.0f}/night")
        avg_comp = sum(r["competitor_avg_rate_eur"] for r in shoulder_recs) / len(shoulder_recs)
        lines.append(f"- Competitor average: EUR {avg_comp:.0f}/night")
        lines.append(f"- Balance rate and occupancy\n")

    lines.append("### Off-Season (January-February)")
    off_recs = [r for r in recs if r["season"] == "Off Season"]
    if off_recs:
        avg_off = sum(r["recommended_rate_eur"] for r in off_recs) / len(off_recs)
        lines.append(f"- Recommended range: EUR {min(r['recommended_rate_eur'] for r in off_recs):.0f} - "
                     f"EUR {max(r['recommended_rate_eur'] for r in off_recs):.0f}/night")
        lines.append(f"- Average: EUR {avg_off:.0f}/night")
        avg_comp = sum(r["competitor_avg_rate_eur"] for r in off_recs) / len(off_recs)
        lines.append(f"- Competitor average: EUR {avg_comp:.0f}/night")
        lines.append(f"- Focus on maintaining occupancy - lower rates attract longer stays\n")

    # Demand index
    lines.append("\n## Demand Index by Month\n")
    lines.append("| Month | Demand Index (0-100) | Historical Occupancy | Historical ADR |")
    lines.append("|-------|---------------------|---------------------|----------------|")
    for cm in range(1, 13):
        p = demand_data["monthly_patterns"][cm]
        lines.append(f"| {p['month_name']} | {p['demand_index']} | {p['avg_occupancy_pct']}% | EUR {p['avg_adr']:.2f} |")

    # Action steps
    lines.append("\n## Action Steps\n")
    lines.append("1. **Immediate:** Raise base rate from EUR 45 to EUR 50 (conservative first step)")
    lines.append("2. **Week 2:** Sign up for PriceLabs ($19.99/month) - it automates dynamic pricing")
    lines.append("3. **Week 2:** Set seasonal base rates in PriceLabs using the table above")
    lines.append("4. **Week 3:** Add weekly discount (10-15%) and monthly discount (20-25%)")
    lines.append("5. **Week 4:** Review booking pace - if bookings maintained, raise to recommended rates")
    lines.append("6. **Monthly:** Run this price predictor agent to update recommendations with new data")
    lines.append("7. **Quarterly:** Update competitors.json with fresh competitor research\n")

    if issues:
        lines.append("\n## Issues & Warnings\n")
        for issue in issues:
            lines.append(f"- **[{issue['severity']}]** {issue['message']}")

    report = "\n".join(lines) + "\n"
    path = PROJECT_ROOT / "pricing_recommendations.md"
    path.write_text(report, encoding="utf-8")
    return str(path)


def _generate_json(price_data, demand_data, benchmark_data, comp_data, issues):
    """Generate pricing_data.json."""
    data = {
        "generated": datetime.now().isoformat(),
        "data_source": f"{comp_data['competitor_count']} nearby competitors (max 3 guests)",
        "recommendations": price_data["recommendations"],
        "revenue_scenarios": price_data["revenue_scenarios"],
        "summary": price_data["summary"],
        "competitor_analysis": {
            "count": comp_data["competitor_count"],
            "avg_price_eur": comp_data["avg_price_eur"],
            "median_price_eur": comp_data["median_price_eur"],
            "p25_price_eur": comp_data["p25_price_eur"],
            "p75_price_eur": comp_data["p75_price_eur"],
            "your_position": comp_data.get("your_position", {}),
            "rating_tiers": comp_data.get("rating_tiers", {}),
            "competitors": comp_data.get("competitors", []),
        },
        "demand_patterns": demand_data["monthly_patterns"],
        "demand_overall": demand_data["overall"],
        "market_benchmarks": benchmark_data["monthly_benchmarks"],
        "rating_premium": benchmark_data["rating_premium"],
        "market_context": benchmark_data["market_context"],
        "issues": issues,
    }

    path = PROJECT_ROOT / "pricing_data.json"
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    return str(path)


def _print_summary(price_data, benchmark_data, comp_data):
    """Print formatted summary to terminal."""
    recs = price_data["recommendations"]
    scenarios = price_data["revenue_scenarios"]
    s = price_data["summary"]
    rp = benchmark_data["rating_premium"]
    pos = comp_data.get("your_position", {})

    print(f"\n{'=' * 70}")
    print(f"  PRICING RECOMMENDATIONS")
    print(f"  Based on {comp_data['competitor_count']} nearby competitors (max 3 guests)")
    print(f"{'=' * 70}")
    print(f"  Current flat rate:   EUR {s['current_flat_rate']}/night")
    print(f"  Competitor avg:      EUR {s['competitor_avg_price']}/night")
    print(f"  Rating premium:      {rp['applied_premium_pct']}% (from competitor tier data)")
    print(f"  Avg recommended:     EUR {s['avg_recommended_rate']}/night")
    print(f"  Rate range:          EUR {s['min_recommended_rate']} - EUR {s['max_recommended_rate']}")
    if pos:
        print(f"  Your price position: {pos.get('price_percentile', 'N/A')}th percentile")
        print(f"  Your rating rank:    {pos.get('rating_rank', 'N/A')}")

    print(f"\n  {'Month':<12} {'Season':<12} {'Recommend':>10} {'Current':>8} {'Comp Avg':>9} {'Occ%':>6} {'Revenue':>10} {'Uplift':>8}")
    print(f"  {'-'*12} {'-'*12} {'-'*10} {'-'*8} {'-'*9} {'-'*6} {'-'*10} {'-'*8}")
    for r in recs:
        print(f"  {r['month_name']:<12} {r['season']:<12} "
              f"EUR{r['recommended_rate_eur']:>8.0f} EUR{r['current_rate_eur']:>6} EUR{r['competitor_avg_rate_eur']:>7.0f} "
              f"{r['expected_occupancy_pct']:>5.0f}% EUR{r['expected_revenue_eur']:>8,.0f} "
              f"{r['revenue_uplift_pct']:>+6.0f}%")

    print(f"\n  REVENUE SCENARIOS:")
    for key in ["current", "recommended", "competitor_average"]:
        sc = scenarios[key]
        print(f"    {sc['label']:<40} EUR {sc['annual_revenue_eur']:>10,.2f}/year  (EUR {sc['monthly_avg_eur']:>8,.2f}/mo)")

    uplift = scenarios["uplift_vs_current"]
    print(f"\n  ANNUAL UPLIFT: EUR {uplift['annual_eur']:,.2f} ({uplift['annual_pct']:+.1f}%)")

    print(f"\n  OUTPUT FILES:")
    print(f"    - pricing_recommendations.md  (detailed report with competitor analysis)")
    print(f"    - pricing_data.json           (machine-readable data)")
    print(f"{'=' * 70}\n")


if __name__ == "__main__":
    run()
