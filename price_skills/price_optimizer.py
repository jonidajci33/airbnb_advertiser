"""
Skill: Price Optimizer
Combines historical demand + competitor-based market benchmarks to recommend
optimal nightly rates. Uses real competitor pricing (max 3 guests, central
Tirana) instead of broad market averages.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

MONTH_NAMES = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Current flat rate
CURRENT_RATE_EUR = 45


def optimize_prices(demand_data, benchmark_data):
    """
    Generate price recommendations for each of the next 12 months.

    Uses competitor-filtered benchmarks (nearby properties, max 3 guests)
    combined with your historical demand patterns and rating premium.

    Args:
        demand_data: output from historical_demand.analyze_demand()
        benchmark_data: output from market_benchmarks.compile_benchmarks()

    Returns:
        dict with keys:
            - recommendations: list of 12 monthly recommendations
            - revenue_scenarios: current vs recommended vs market
            - summary: overall summary
    """
    patterns = demand_data["monthly_patterns"]
    benchmarks = benchmark_data["monthly_benchmarks"]
    rating_premium = benchmark_data["rating_premium"]
    premium_mult = rating_premium["multiplier"]
    competitor_summary = benchmark_data.get("competitor_summary", {})

    recommendations = []

    for cm in range(1, 13):
        demand = patterns[cm]
        bench = benchmarks[cm]

        competitor_avg = bench["market_avg_rate_eur"]
        competitor_median = bench.get("market_median_rate_eur", competitor_avg)
        market_occ = bench["market_occupancy_pct"]
        season = bench["season"]

        # Use median as base (more robust to outliers than mean)
        base_rate = competitor_median

        # Historical demand adjustment
        # If our demand index is above average, price higher; below, price lower
        avg_demand = demand_data["overall"]["avg_demand_index"]
        demand_idx = demand["demand_index"]

        if avg_demand > 0 and demand_idx > 0:
            demand_ratio = demand_idx / avg_demand
            # Cap the adjustment at +/- 15%
            demand_adjustment = max(0.85, min(1.15, demand_ratio))
        else:
            demand_adjustment = 1.0

        # Historical ADR adjustment
        # If our historical ADR for this month is significantly different from
        # competitor avg, blend in our actual performance data
        hist_adr = demand["avg_adr"] if demand["data_points"] > 0 else 0
        if hist_adr > 0 and demand["data_points"] >= 2:
            # Blend: 60% competitor data + 40% historical (more weight on competitors)
            blended_base = base_rate * 0.6 + hist_adr * 0.4
        else:
            blended_base = base_rate

        # Recommended rate = blended_base * rating_premium * demand_adjustment
        recommended_rate = blended_base * premium_mult * demand_adjustment

        # Clamp to reasonable bounds based on competitor range
        rate_floor = max(25, bench["market_rate_low_eur"] * 0.9)
        rate_ceiling = min(90, bench["market_rate_high_eur"] * 1.2)
        recommended_rate = max(rate_floor, min(rate_ceiling, recommended_rate))
        recommended_rate = round(recommended_rate, 0)

        # Rate range for dynamic pricing (±10%)
        rate_min = round(max(rate_floor, recommended_rate * 0.90))
        rate_max = round(min(rate_ceiling, recommended_rate * 1.10))

        # Expected occupancy
        if demand["data_points"] > 0 and demand["avg_occupancy_pct"] > 0:
            if demand["data_points"] >= 2:
                # Strong historical data: weight it more
                expected_occ = demand["avg_occupancy_pct"] * 0.7 + market_occ * 0.3
            else:
                # Limited data: blend equally
                expected_occ = demand["avg_occupancy_pct"] * 0.5 + market_occ * 0.5
        else:
            expected_occ = market_occ

        # Price elasticity adjustment
        # If recommending higher than current, occupancy may drop slightly
        if recommended_rate > CURRENT_RATE_EUR:
            price_increase_pct = (recommended_rate - CURRENT_RATE_EUR) / CURRENT_RATE_EUR * 100
            # Every 10% price increase reduces occupancy by ~2% (conservative)
            occ_reduction = price_increase_pct / 10 * 2
            # Rating premium partially offsets this (top-rated properties retain guests)
            occ_boost = min(3, (rating_premium["applied_premium_pct"] / 10))
            expected_occ = expected_occ - occ_reduction + occ_boost
        elif recommended_rate < CURRENT_RATE_EUR:
            # Lower price should increase occupancy
            price_decrease_pct = (CURRENT_RATE_EUR - recommended_rate) / CURRENT_RATE_EUR * 100
            occ_boost = price_decrease_pct / 10 * 2
            expected_occ = expected_occ + occ_boost

        expected_occ = max(10, min(80, round(expected_occ, 1)))

        # Revenue projections
        days = DAYS_IN_MONTH[cm]
        nights_expected = round(days * expected_occ / 100)
        expected_revenue = round(recommended_rate * nights_expected, 2)

        # Current revenue (flat EUR 45)
        current_occ = demand["avg_occupancy_pct"] if demand["data_points"] > 0 else market_occ
        current_nights = round(days * current_occ / 100)
        current_revenue = round(CURRENT_RATE_EUR * current_nights, 2)

        # Competitor average revenue
        comp_nights = round(days * market_occ / 100)
        competitor_revenue = round(competitor_avg * comp_nights, 2)

        revenue_uplift = expected_revenue - current_revenue
        revenue_uplift_pct = round(revenue_uplift / current_revenue * 100, 1) if current_revenue > 0 else 0

        recommendations.append({
            "month_number": cm,
            "month_name": MONTH_NAMES[cm],
            "season": bench["season_label"],
            "recommended_rate_eur": recommended_rate,
            "rate_range_min_eur": rate_min,
            "rate_range_max_eur": rate_max,
            "current_rate_eur": CURRENT_RATE_EUR,
            "competitor_avg_rate_eur": competitor_avg,
            "competitor_median_rate_eur": competitor_median,
            "expected_occupancy_pct": expected_occ,
            "expected_revenue_eur": expected_revenue,
            "current_revenue_eur": current_revenue,
            "competitor_revenue_eur": competitor_revenue,
            "revenue_uplift_eur": round(revenue_uplift, 2),
            "revenue_uplift_pct": revenue_uplift_pct,
            "demand_index": demand["demand_index"],
            "demand_adjustment": round(demand_adjustment, 3),
            "rating_premium_applied": round(premium_mult, 3),
        })

    # Annual revenue scenarios
    annual_current = sum(r["current_revenue_eur"] for r in recommendations)
    annual_recommended = sum(r["expected_revenue_eur"] for r in recommendations)
    annual_competitor = sum(r["competitor_revenue_eur"] for r in recommendations)

    revenue_scenarios = {
        "current": {
            "label": f"Current (flat EUR {CURRENT_RATE_EUR}/night)",
            "annual_revenue_eur": round(annual_current, 2),
            "monthly_avg_eur": round(annual_current / 12, 2),
        },
        "recommended": {
            "label": "Recommended (dynamic seasonal pricing)",
            "annual_revenue_eur": round(annual_recommended, 2),
            "monthly_avg_eur": round(annual_recommended / 12, 2),
        },
        "competitor_average": {
            "label": "Competitor average pricing",
            "annual_revenue_eur": round(annual_competitor, 2),
            "monthly_avg_eur": round(annual_competitor / 12, 2),
        },
        "uplift_vs_current": {
            "annual_eur": round(annual_recommended - annual_current, 2),
            "annual_pct": round((annual_recommended - annual_current) / annual_current * 100, 1) if annual_current > 0 else 0,
        },
    }

    # Summary stats
    rates = [r["recommended_rate_eur"] for r in recommendations]
    summary = {
        "avg_recommended_rate": round(sum(rates) / len(rates), 2),
        "min_recommended_rate": min(rates),
        "max_recommended_rate": max(rates),
        "rate_spread": max(rates) - min(rates),
        "current_flat_rate": CURRENT_RATE_EUR,
        "rating_premium_pct": rating_premium["applied_premium_pct"],
        "competitors_analyzed": competitor_summary.get("total_competitors", 0),
        "competitor_avg_price": competitor_summary.get("avg_price_eur", 0),
        "months_above_current": sum(1 for r in rates if r > CURRENT_RATE_EUR),
        "months_below_current": sum(1 for r in rates if r < CURRENT_RATE_EUR),
        "months_at_current": sum(1 for r in rates if r == CURRENT_RATE_EUR),
    }

    return {
        "recommendations": recommendations,
        "revenue_scenarios": revenue_scenarios,
        "summary": summary,
    }


if __name__ == "__main__":
    print("Price Optimizer module loaded. Use optimize_prices(demand_data, benchmark_data) to get recommendations.")
