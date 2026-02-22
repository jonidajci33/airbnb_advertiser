"""
Skill: Market Intelligence
Researches the Albanian Airbnb market size, trends, growth, seasonality,
and regulations — then compares your property's position against the market.
"""

import sys
from pathlib import Path

SKILL_NAME = "market_intel"
DESCRIPTION = "Albanian Airbnb market trends, statistics, and your position in the market"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# ─── Researched Market Data (Feb 2026) ──────────────────────────────────────
MARKET_DATA = {
    "albania_national": {
        "total_listings": 23000,
        "airbnb_revenue_2024_eur": 85_000_000,
        "listing_growth_2023_2025_pct": 38,
        "national_avg_occupancy_pct": 45,
        "national_avg_adr_eur": 56,
        "avg_annual_revenue_per_listing_usd": 6578,
        "gross_rental_yield_pct": "9-11%",
        "net_profit_margin_pct": "35-55%",
        "avg_expense_ratio_pct": "30-55%",
    },
    "tirana": {
        "active_listings": 3488,
        "composition_entire_home_pct": 93.7,
        "composition_1bed_pct": 67.2,
        "avg_adr_usd": 49,
        "avg_occupancy_pct": 45,
        "top_10_pct_occupancy": 62,
        "avg_annual_revenue_usd": 10866,
        "top_10_monthly_income_usd": 1400,
        "median_monthly_income_usd": 630,
        "international_guests_pct": 87.55,
        "largest_guest_nationality": "United States",
    },
    "seasonality": {
        "peak_months": ["July", "August"],
        "peak_occupancy_pct": 52,
        "peak_adr_usd": 63,
        "peak_monthly_revenue_usd": 1000,
        "low_months": ["January", "February"],
        "low_occupancy_pct": 35,
        "low_adr_usd": 55,
        "low_monthly_revenue_usd": 550,
        "seasonal_swing_tirana": "1.5-2x",
        "seasonal_swing_coastal": "5-7x",
    },
    "tourism": {
        "visitors_2024": 11_700_000,
        "visitor_growth_yoy_pct": 15.2,
        "visitors_vs_2019_pct": 80,
        "tourism_gdp_share_pct": 26.4,
        "tourism_revenue_q3_2024_eur": 2_300_000_000,
        "top_source_countries": ["Kosovo (15%)", "Italy (13%)", "Germany (9%)", "Poland (8%)", "France (8%)"],
        "medical_tourists_annual": 80000,
        "dental_tourism_growth_since_2020": "400%",
    },
    "regulations": {
        "tax_rate_pct": 15,
        "tax_platform": "DIVA digital platform",
        "tax_deadline": "March 31",
        "night_cap": "None (no limit)",
        "min_stay_requirement": "None",
        "restricted_zones": "None",
        "new_2026": "New fiscal reporting requirements from Jan 1, 2026",
        "regulatory_stance": "One of the most permissive in Europe",
    },
    "trends_2024_2026": {
        "supply_outpacing_demand": True,
        "property_prices_tirana_eur_sqm": "2000-2500",
        "local_rent_increase_pct": 30,
        "foreign_buyer_share_pct": 50,
        "growth_decelerating": "H1 2025 +5% vs H1 2024 +23%",
    },
}

# ─── Your Property Data ──────────────────────────────────────────────────────
YOUR_PROPERTY = {
    "nightly_rate_eur": 45,
    "occupancy_estimate_pct": 40,  # estimated from review velocity
    "monthly_revenue_estimate_eur": 45 * 30 * 0.40,  # ~540
    "annual_revenue_estimate_eur": 45 * 365 * 0.40,  # ~6570
    "reviews_total": 54,
    "airbnb_rating": 4.88,
    "booking_rating": 10.0,
    "photos": 8,
    "platforms": 2,
    "months_active": 24,
}


def analyze_market_position():
    """Compare your property against market averages."""
    t = MARKET_DATA["tirana"]
    you = YOUR_PROPERTY

    position = {
        "rate_vs_market": {
            "your_rate_eur": you["nightly_rate_eur"],
            "market_avg_usd": t["avg_adr_usd"],
            "market_avg_eur_approx": round(t["avg_adr_usd"] * 0.92),
            "position": "BELOW" if you["nightly_rate_eur"] < t["avg_adr_usd"] * 0.92 else "ABOVE",
        },
        "revenue_vs_market": {
            "your_annual_eur": you["annual_revenue_estimate_eur"],
            "market_avg_annual_usd": t["avg_annual_revenue_usd"],
            "your_monthly_eur": you["monthly_revenue_estimate_eur"],
            "market_median_monthly_usd": t["median_monthly_income_usd"],
            "top_10_monthly_usd": t["top_10_monthly_income_usd"],
        },
        "occupancy_vs_market": {
            "your_estimate_pct": you["occupancy_estimate_pct"],
            "market_avg_pct": t["avg_occupancy_pct"],
            "top_10_pct": t["top_10_pct_occupancy"],
        },
        "listing_competition": {
            "total_tirana_listings": t["active_listings"],
            "your_composition_match": f"{t['composition_1bed_pct']}% of listings are 1-bed like yours",
            "estimated_direct_competitors": round(t["active_listings"] * t["composition_1bed_pct"] / 100),
        },
    }
    return position


def identify_opportunities():
    """Identify market opportunities based on research."""
    opportunities = []

    # Supply outpacing demand
    opportunities.append({
        "severity": "HIGH",
        "area": "Market Saturation Warning",
        "finding": (
            f"Listings grew 38% in 2 years (to {MARKET_DATA['albania_national']['total_listings']:,}) "
            f"while tourism growth slowed from 23% to 5%. Supply is outpacing demand."
        ),
        "recommendation": (
            "Differentiation is now critical. Generic apartments will struggle. "
            "Your medical tourism niche is your biggest defense against saturation. "
            "Double down on it — become THE recovery apartment in Tirana."
        ),
        "what_others_do": "Top performers differentiate through niche targeting, superior photography, and multi-platform presence.",
    })

    # International guest opportunity
    opportunities.append({
        "severity": "HIGH",
        "area": "International Guest Targeting",
        "finding": (
            f"87.55% of Tirana Airbnb guests are international, with Americans being the largest group. "
            f"Your listing and outreach are primarily in Albanian."
        ),
        "recommendation": (
            "Optimize your entire listing for English-speaking international travelers. "
            "Add listing descriptions in English, Italian, and German (top source countries). "
            "Marketing materials to clinics should include English versions for their international patients."
        ),
        "what_others_do": "Top hosts write listings in 2-3 languages and target their marketing to source countries.",
    })

    # Seasonal strategy
    s = MARKET_DATA["seasonality"]
    opportunities.append({
        "severity": "HIGH",
        "area": "No Seasonal Pricing Strategy",
        "finding": (
            f"Tirana has a 1.5-2x seasonal swing: peak months (Jul-Aug) see ${s['peak_adr_usd']}/night "
            f"and {s['peak_occupancy_pct']}% occupancy vs low months at ${s['low_adr_usd']}/night "
            f"and {s['low_occupancy_pct']}% occupancy."
        ),
        "recommendation": (
            "Implement seasonal pricing: €55-60/night in summer (Jun-Sep), €45/night shoulder (Apr-May, Oct), "
            "€35-40/night winter (Nov-Mar). Use PriceLabs ($19.99/month) for dynamic adjustments. "
            "Top hosts using dynamic pricing see 20-40% revenue increases."
        ),
        "what_others_do": "Top Albanian hosts use PriceLabs or Beyond Pricing and adjust rates daily based on demand.",
    })

    # Tax compliance
    r = MARKET_DATA["regulations"]
    opportunities.append({
        "severity": "MEDIUM",
        "area": "Tax Compliance (DIVA Platform)",
        "finding": (
            f"Albania charges {r['tax_rate_pct']}% on rental income via the {r['tax_platform']}. "
            f"Deadline: {r['tax_deadline']}. New 2026 fiscal reporting requirements now in effect."
        ),
        "recommendation": (
            "Ensure you're registered on DIVA and declaring income. "
            "Keep records of all bookings and expenses. "
            "Deductible expenses (cleaning, supplies, repairs, platform fees) reduce your taxable base."
        ),
        "what_others_do": "Professional hosts track all expenses meticulously to minimize tax burden within legal limits.",
    })

    # Medical tourism boom
    opportunities.append({
        "severity": "HIGH",
        "area": "Medical Tourism Boom — Act Now",
        "finding": (
            f"Albania sees {MARKET_DATA['tourism']['medical_tourists_annual']:,} medical tourists/year "
            f"with {MARKET_DATA['tourism']['dental_tourism_growth_since_2020']} growth since 2020. "
            f"Dental implants cost €460 in Albania vs €3,100 in the UK — 85% savings."
        ),
        "recommendation": (
            "Create a dedicated 'Medical Stay Package' with recovery amenities, clinic transport, "
            "and weekly rates. Albania is projected to enter the top 5 European dental tourism destinations by 2027. "
            "First movers who build clinic partnerships now will own this niche."
        ),
        "what_others_do": "In Turkey (the market leader), clinics bundle 3-5 night hotel stays into every surgery package. Albania has NO provider doing this yet.",
    })

    # Revenue opportunity
    you = YOUR_PROPERTY
    top_10_annual = MARKET_DATA["tirana"]["top_10_monthly_income_usd"] * 12
    your_annual = you["annual_revenue_estimate_eur"]
    gap = top_10_annual - your_annual
    opportunities.append({
        "severity": "HIGH",
        "area": "Revenue Gap vs Top Performers",
        "finding": (
            f"Your estimated annual revenue (~€{your_annual:,.0f}) is near the Tirana median. "
            f"Top 10% listings earn ~${top_10_annual:,.0f}/year — a ${gap:,.0f} gap."
        ),
        "recommendation": (
            "Close the gap through: (1) raise nightly rate to €55-57, (2) implement dynamic pricing, "
            "(3) add upsells (airport transfers, early check-in), (4) list on Booking.com + direct. "
            "Combined, these can increase revenue 40-60%."
        ),
        "what_others_do": "Top 10% hosts combine dynamic pricing, multi-platform distribution, upsells, and direct bookings.",
    })

    return opportunities


def run():
    """Main skill entry point."""
    position = analyze_market_position()
    opportunities = identify_opportunities()

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "market_data": MARKET_DATA,
        "your_position": position,
        "issues": opportunities,
        "issues_count": len(opportunities),
    }

    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  ALBANIAN AIRBNB MARKET:")
    print(f"    Total listings:         {MARKET_DATA['albania_national']['total_listings']:,}")
    print(f"    Airbnb revenue 2024:    €{MARKET_DATA['albania_national']['airbnb_revenue_2024_eur']:,}")
    print(f"    Tirana listings:        {MARKET_DATA['tirana']['active_listings']:,}")
    print(f"    Tirana avg ADR:         ${MARKET_DATA['tirana']['avg_adr_usd']}/night")
    print(f"    Visitors 2024:          {MARKET_DATA['tourism']['visitors_2024']:,}")
    print(f"\n  YOUR POSITION:")
    print(f"    Rate:     €{YOUR_PROPERTY['nightly_rate_eur']}/night ({position['rate_vs_market']['position']} market)")
    print(f"    Revenue:  ~€{YOUR_PROPERTY['monthly_revenue_estimate_eur']:.0f}/month (median: ${MARKET_DATA['tirana']['median_monthly_income_usd']})")
    print(f"    Competitors: ~{position['listing_competition']['estimated_direct_competitors']} similar 1-bed listings")
    print(f"\n  OPPORTUNITIES: {len(opportunities)}")
    for i, opp in enumerate(opportunities, 1):
        print(f"    {i}. [{opp['severity']}] {opp['area']}")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
