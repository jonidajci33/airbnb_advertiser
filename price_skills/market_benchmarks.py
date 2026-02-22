"""
Skill: Market Benchmarks
Compiles per-month benchmark pricing using REAL competitor data
(filtered for properties near Lulebore Apartment 1, max 3 guests)
instead of broad Tirana-wide averages.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from price_skills.competitor_analyzer import analyze_competitors

MONTH_NAMES = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]


def compile_benchmarks():
    """
    Compile per-month market benchmarks using real competitor data.

    Uses competitor_analyzer to get pricing from 31 nearby properties
    (max 3 guests) instead of broad Tirana market averages.

    Returns:
        dict with keys:
            - monthly_benchmarks: dict[1-12] -> benchmark data
            - rating_premium: rating-based price premium info
            - market_context: competitor market stats
            - competitor_summary: overview of competitor landscape
    """
    # Get real competitor data
    comp_data = analyze_competitors()
    comp_monthly = comp_data["monthly_benchmarks"]
    rating_tiers = comp_data.get("rating_tiers", {})

    # Rating premium calculation based on competitor data
    # Your ratings: 4.88/5 Airbnb + 10.0/10 Booking.com
    airbnb_rating = 4.88
    booking_rating = 10.0

    # Compute premium from actual competitor pricing by rating tier
    premium_tier = rating_tiers.get("premium", {})
    good_tier = rating_tiers.get("good", {})
    avg_tier = rating_tiers.get("average", {})

    # Use real data: premium-rated properties (4.8+) avg price vs overall avg
    overall_avg = comp_data["avg_price_eur"]
    premium_avg = premium_tier.get("avg_price_eur", overall_avg)

    if overall_avg > 0 and premium_avg > 0:
        # Calculate actual premium that top-rated competitors charge
        actual_premium_pct = round((premium_avg - overall_avg) / overall_avg * 100, 1)
        # Your rating is in the premium tier, so apply this premium
        # But cap it at reasonable bounds (5-25%)
        applied_premium_pct = max(5, min(25, actual_premium_pct))
    else:
        applied_premium_pct = 15.0

    rating_premium_multiplier = 1 + applied_premium_pct / 100

    rating_premium = {
        "airbnb_rating": airbnb_rating,
        "booking_rating": booking_rating,
        "percentile": "top 5% by rating",
        "premium_range_pct": "15-25",
        "applied_premium_pct": applied_premium_pct,
        "multiplier": rating_premium_multiplier,
        "data_source": "competitor_analysis",
        "premium_tier_avg_eur": premium_avg,
        "overall_avg_eur": overall_avg,
        "justification": (
            f"With {airbnb_rating}/5 Airbnb + {booking_rating}/10 Booking.com ratings "
            f"(top 5% by rating), a {applied_premium_pct}% premium over competitor average is justified. "
            f"Premium-rated competitors (4.8+) charge EUR {premium_avg} avg vs "
            f"EUR {overall_avg} overall avg among {comp_data['competitor_count']} nearby properties (max 3 guests)."
        ),
    }

    # Per-month benchmarks from competitor data
    monthly_benchmarks = {}
    for cm in range(1, 13):
        cb = comp_monthly[cm]

        monthly_benchmarks[cm] = {
            "month_number": cm,
            "month_name": MONTH_NAMES[cm],
            "season": cb["season"],
            "season_label": cb["season_label"],
            "market_rate_low_eur": cb["competitor_low_eur"],
            "market_rate_high_eur": cb["competitor_high_eur"],
            "market_avg_rate_eur": cb["competitor_avg_eur"],
            "market_median_rate_eur": cb["competitor_median_eur"],
            "market_occupancy_pct": cb["market_occupancy_pct"],
            "rating_premium_multiplier": rating_premium_multiplier,
            "data_source": "competitor_filtered",
        }

    # Competitor market context
    pos = comp_data.get("your_position", {})
    market_context = {
        "competitors_analyzed": comp_data["competitor_count"],
        "competitor_avg_price_eur": comp_data["avg_price_eur"],
        "competitor_median_price_eur": comp_data["median_price_eur"],
        "competitor_p25_price_eur": comp_data["p25_price_eur"],
        "competitor_p75_price_eur": comp_data["p75_price_eur"],
        "your_price_percentile": pos.get("price_percentile", 0),
        "your_price_vs_avg_pct": pos.get("price_vs_avg_pct", 0),
        "your_rating_rank": pos.get("rating_rank", "unknown"),
        "filter": "central Tirana, max 3 guests",
    }

    # Competitor summary for the report
    competitor_summary = {
        "total_competitors": comp_data["competitor_count"],
        "avg_price_eur": comp_data["avg_price_eur"],
        "median_price_eur": comp_data["median_price_eur"],
        "price_range": f"EUR {comp_data['p25_price_eur']}-{comp_data['p75_price_eur']}",
        "your_position": pos,
        "rating_tiers": rating_tiers,
        "top_5_cheapest": comp_data["competitors"][:5] if comp_data.get("competitors") else [],
        "top_5_expensive": comp_data["competitors"][-5:] if comp_data.get("competitors") else [],
    }

    return {
        "monthly_benchmarks": monthly_benchmarks,
        "rating_premium": rating_premium,
        "market_context": market_context,
        "competitor_summary": competitor_summary,
    }


if __name__ == "__main__":
    result = compile_benchmarks()
    rp = result["rating_premium"]
    mc = result["market_context"]
    print(f"\nMarket Benchmarks (Competitor-Based)")
    print(f"{'=' * 65}")
    print(f"  Data source:      {mc['competitors_analyzed']} nearby competitors (max 3 guests)")
    print(f"  Competitor avg:   EUR {mc['competitor_avg_price_eur']}")
    print(f"  Competitor median: EUR {mc['competitor_median_price_eur']}")
    print(f"  Your price:       EUR 45 (percentile: {mc['your_price_percentile']}%)")
    print(f"  Your rating rank: {mc['your_rating_rank']}")
    print(f"  Rating Premium:   {rp['applied_premium_pct']}% (premium tier avg EUR {rp['premium_tier_avg_eur']})")
    print(f"\n  {'Month':<12} {'Season':<12} {'Comp Avg':>9} {'Comp Med':>9} {'Low':>6} {'High':>6} {'Occ':>6}")
    print(f"  {'-'*12} {'-'*12} {'-'*9} {'-'*9} {'-'*6} {'-'*6} {'-'*6}")
    for cm in range(1, 13):
        b = result["monthly_benchmarks"][cm]
        print(f"  {b['month_name']:<12} {b['season_label']:<12} "
              f"EUR{b['market_avg_rate_eur']:>6} EUR{b['market_median_rate_eur']:>6} "
              f"EUR{b['market_rate_low_eur']:>4} EUR{b['market_rate_high_eur']:>4} "
              f"{b['market_occupancy_pct']:>4}%")
    print()
