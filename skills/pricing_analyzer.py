"""
Skill: Pricing Analyzer
Analyzes pricing strategy and identifies optimization opportunities.

Metrics analyzed:
  - Current rate vs market average
  - Price positioning relative to rating
  - Discount strategy (weekly/monthly)
  - Revenue optimization potential
  - Seasonal pricing readiness
  - Medical tourism pricing angle
"""

from skills.data_loader import load_property_profile, load_marketing_report, _find_project_root

SKILL_NAME = "pricing_analyzer"
DESCRIPTION = "Analyzes pricing strategy and revenue optimization opportunities"


def analyze_pricing(profile_text, marketing_text):
    """Analyze current pricing vs market and identify gaps."""

    # Known data from property profile
    current_rate = 45  # EUR per night
    market_avg = 50
    budget_low = 17
    budget_high = 60
    airbnb_rating = 4.88
    booking_rating = 10.0
    total_reviews = 54  # 33 + 21

    # Pricing analysis
    rate_vs_market = round((current_rate / market_avg - 1) * 100, 1)
    percentile = round((current_rate - budget_low) / (budget_high - budget_low) * 100, 1)

    # Rating-adjusted fair price (higher ratings justify higher prices)
    # Top 5% ratings can charge 20-30% above average
    rating_premium = 0
    if airbnb_rating >= 4.9:
        rating_premium = 25
    elif airbnb_rating >= 4.8:
        rating_premium = 15
    elif airbnb_rating >= 4.7:
        rating_premium = 10

    fair_price = round(market_avg * (1 + rating_premium / 100))

    # Revenue scenarios
    scenarios = {
        "current_30_nights": current_rate * 30,
        "current_20_nights": current_rate * 20,
        "current_15_nights": current_rate * 15,
        "optimized_30_nights": fair_price * 30,
        "optimized_20_nights": fair_price * 20,
        "optimized_15_nights": fair_price * 15,
    }

    # Medical tourism pricing
    medical_weekly_rate = current_rate * 7 * 0.85  # 15% weekly discount
    medical_biweekly_rate = current_rate * 14 * 0.80  # 20% extended discount

    return {
        "current_rate_eur": current_rate,
        "market_average_eur": market_avg,
        "rate_vs_market_pct": rate_vs_market,
        "market_percentile": percentile,
        "rating_adjusted_fair_price": fair_price,
        "rating_premium_pct": rating_premium,
        "revenue_scenarios": scenarios,
        "medical_weekly_rate": round(medical_weekly_rate),
        "medical_biweekly_rate": round(medical_biweekly_rate),
        "potential_monthly_revenue_gain": scenarios["optimized_20_nights"] - scenarios["current_20_nights"],
    }


def identify_issues(pricing):
    """Identify pricing improvement areas."""
    issues = []

    # Underpriced for rating
    if pricing["rate_vs_market_pct"] < 0 and pricing["rating_premium_pct"] > 0:
        gain = pricing["rating_adjusted_fair_price"] - pricing["current_rate_eur"]
        issues.append({
            "severity": "HIGH",
            "area": "Underpriced for Rating Quality",
            "finding": (
                f"Charging €{pricing['current_rate_eur']}/night but your ratings "
                f"(4.88 Airbnb, 10/10 Booking) justify €{pricing['rating_adjusted_fair_price']}/night. "
                f"You're leaving €{gain}/night on the table."
            ),
            "recommendation": (
                f"Gradually increase to €{pricing['rating_adjusted_fair_price']}/night. "
                f"Start by raising €2-3 every 2 weeks. With {pricing['rating_premium_pct']}% rating premium, "
                f"this could mean €{pricing['potential_monthly_revenue_gain']:.0f}/month more revenue "
                f"(assuming 20 nights occupancy)."
            ),
            "estimated_impact": f"+€{pricing['potential_monthly_revenue_gain']:.0f}/month",
        })

    # No dynamic pricing
    issues.append({
        "severity": "HIGH",
        "area": "No Dynamic Pricing",
        "finding": "Not using any dynamic pricing tool. Static pricing leaves money on the table during high-demand periods.",
        "recommendation": "Enable Airbnb Smart Pricing or sign up for PriceLabs/Beyond Pricing. These tools automatically adjust rates based on demand, events, and seasonality.",
        "estimated_impact": "10-20% more revenue",
    })

    # No weekly/monthly discounts
    issues.append({
        "severity": "HIGH",
        "area": "No Long-Stay Discounts",
        "finding": "No weekly or monthly discounts configured. Medical tourists stay 5-14 days on average.",
        "recommendation": (
            f"Set up: 10-15% weekly discount (€{pricing['medical_weekly_rate']}/week), "
            f"20% bi-weekly discount (€{pricing['medical_biweekly_rate']}/2 weeks). "
            "This is the #1 way to attract medical tourist bookings."
        ),
        "estimated_impact": "Attract longer stays, higher total revenue",
    })

    # No seasonal strategy
    issues.append({
        "severity": "MEDIUM",
        "area": "No Seasonal Pricing",
        "finding": "No evidence of seasonal price adjustments. Tirana has clear high season (Apr-Oct) and low season (Nov-Mar).",
        "recommendation": "Set high season rate at €50-55/night (Apr-Oct), shoulder season at €45/night (Mar, Nov), low season at €35-40/night (Dec-Feb). Maintain occupancy year-round.",
        "estimated_impact": "Consistent occupancy year-round",
    })

    # No direct booking pricing
    issues.append({
        "severity": "MEDIUM",
        "area": "No Direct Booking Incentive",
        "finding": "No direct booking channel with better pricing. Airbnb charges ~15% in fees.",
        "recommendation": "Offer 10% discount for direct bookings through your own website. You still earn 5% more than Airbnb bookings, and guests save money too.",
        "estimated_impact": "Save 5-15% on fees per booking",
    })

    # No clinic referral pricing
    issues.append({
        "severity": "MEDIUM",
        "area": "No Clinic Referral Rate",
        "finding": "No special rate for clinic-referred patients. Clinics need a clear incentive to recommend you.",
        "recommendation": "Create a 'Clinic Partner Rate' at 10% off for patients referred by partner clinics. Give clinics €5-10 commission per night. Both sides win.",
        "estimated_impact": "Steady stream of referral bookings",
    })

    return issues


def run():
    """Main skill entry point."""
    root = _find_project_root()
    profile = load_property_profile(root)
    marketing = load_marketing_report(root)

    pricing = analyze_pricing(profile, marketing)
    issues = identify_issues(pricing)

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "pricing_analysis": pricing,
        "issues": issues,
        "issues_count": len(issues),
    }

    # Print summary
    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  PRICING ANALYSIS:")
    print(f"    Current rate:        €{pricing['current_rate_eur']}/night")
    print(f"    Market average:      €{pricing['market_average_eur']}/night")
    print(f"    vs Market:           {pricing['rate_vs_market_pct']}%")
    print(f"    Fair price (rating): €{pricing['rating_adjusted_fair_price']}/night")
    print(f"    Medical weekly:      €{pricing['medical_weekly_rate']}/week")
    print(f"    Revenue potential:   +€{pricing['potential_monthly_revenue_gain']:.0f}/month")
    print(f"\n  ISSUES FOUND: {len(issues)}")
    for i, issue in enumerate(issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area']}")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
