"""
Skill: Competitor Analyzer
Loads and analyzes competitor data from competitors.json.
Filters for properties near Lulebore Apartment 1 accepting at most 3 guests.
Computes per-season pricing benchmarks from real competitor data.
"""

import json
import statistics
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
COMPETITORS_FILE = PROJECT_ROOT / "competitors.json"

# Your property for comparison
YOUR_PROPERTY = {
    "name": "Lulebore Apartment 1",
    "platform": "both",
    "location": "Central Tirana",
    "max_guests": 3,
    "rating_airbnb": 4.88,
    "rating_booking": 10.0,
    "base_price_eur": 45,
}

MONTH_NAMES = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

# Season assignment per calendar month
MONTH_TO_SEASON = {
    1: "low_season", 2: "low_season",
    3: "shoulder_season", 4: "shoulder_season", 5: "shoulder_season",
    6: "peak_season", 7: "peak_season", 8: "peak_season", 9: "peak_season",
    10: "shoulder_season", 11: "shoulder_season", 12: "shoulder_season",
}

SEASON_LABELS = {
    "low_season": "Off Season",
    "shoulder_season": "Shoulder",
    "peak_season": "Peak",
}


def _normalize_rating(rating, scale):
    """Normalize rating to 0-5 scale for comparison."""
    if scale == 10:
        return rating / 2
    return rating


def load_competitors():
    """Load competitor data from competitors.json."""
    if not COMPETITORS_FILE.exists():
        return {
            "competitors": [],
            "seasonal_benchmarks": {},
            "market_stats": {},
            "issues": [{"severity": "HIGH", "message": "competitors.json not found - run competitor research first"}],
        }

    with open(COMPETITORS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def analyze_competitors():
    """
    Analyze competitor data and compute benchmarks.

    Returns:
        dict with keys:
            - competitor_count: number of competitors analyzed
            - avg_price_eur: average base price across all competitors
            - median_price_eur: median base price
            - p25_price_eur: 25th percentile price
            - p75_price_eur: 75th percentile price
            - avg_rating: average rating (normalized to 5-point scale)
            - your_position: where you stand vs competitors
            - seasonal_benchmarks: per-month pricing based on competitor data
            - monthly_benchmarks: dict[1-12] -> competitor benchmark for that month
            - rating_tiers: pricing by rating tier
            - issues: list of warnings
    """
    data = load_competitors()
    competitors = data.get("competitors", [])
    seasonal = data.get("seasonal_benchmarks", {})
    issues = []

    if not competitors:
        issues.append({"severity": "HIGH", "message": "No competitor data found"})
        return _empty_result(issues)

    # Filter: max 3 guests only (already filtered in the data, but double-check)
    filtered = [c for c in competitors if c.get("max_guests", 99) <= 3]

    if len(filtered) < 5:
        issues.append({
            "severity": "MEDIUM",
            "message": f"Only {len(filtered)} competitors with max 3 guests - benchmarks may be unreliable",
        })

    # Compute price statistics
    prices_eur = [c["base_price_eur"] for c in filtered if c.get("base_price_eur")]
    prices_eur.sort()

    if not prices_eur:
        issues.append({"severity": "HIGH", "message": "No price data in competitor listings"})
        return _empty_result(issues)

    avg_price = round(statistics.mean(prices_eur), 2)
    median_price = round(statistics.median(prices_eur), 2)
    p25 = round(_percentile(prices_eur, 25), 2)
    p75 = round(_percentile(prices_eur, 75), 2)

    # Compute rating statistics (normalize to 5-point scale)
    ratings = []
    for c in filtered:
        if c.get("rating") and c.get("rating_scale"):
            ratings.append(_normalize_rating(c["rating"], c["rating_scale"]))
    avg_rating = round(statistics.mean(ratings), 2) if ratings else 0

    # Rating tiers: group competitors by rating and compute avg price per tier
    rating_tiers = _compute_rating_tiers(filtered)

    # Your position vs competitors
    your_rating_normalized = YOUR_PROPERTY["rating_airbnb"]  # Already on 5-point scale
    competitors_cheaper = sum(1 for p in prices_eur if p < YOUR_PROPERTY["base_price_eur"])
    competitors_same = sum(1 for p in prices_eur if p == YOUR_PROPERTY["base_price_eur"])
    competitors_more = sum(1 for p in prices_eur if p > YOUR_PROPERTY["base_price_eur"])
    your_percentile = round(competitors_cheaper / len(prices_eur) * 100)

    your_position = {
        "your_price_eur": YOUR_PROPERTY["base_price_eur"],
        "your_rating": your_rating_normalized,
        "avg_competitor_price_eur": avg_price,
        "median_competitor_price_eur": median_price,
        "price_vs_avg_pct": round((YOUR_PROPERTY["base_price_eur"] - avg_price) / avg_price * 100, 1),
        "price_percentile": your_percentile,
        "competitors_cheaper": competitors_cheaper,
        "competitors_same_price": competitors_same,
        "competitors_more_expensive": competitors_more,
        "rating_rank": _compute_rating_rank(filtered, your_rating_normalized),
    }

    # Per-month benchmarks using seasonal data and competitor spread
    monthly_benchmarks = _compute_monthly_benchmarks(seasonal, avg_price, median_price, p25, p75)

    # Check for data staleness
    last_updated = data.get("last_updated", "unknown")
    issues.append({
        "severity": "LOW",
        "message": f"Competitor data last updated: {last_updated}",
    })

    return {
        "competitor_count": len(filtered),
        "avg_price_eur": avg_price,
        "median_price_eur": median_price,
        "p25_price_eur": p25,
        "p75_price_eur": p75,
        "avg_rating": avg_rating,
        "your_position": your_position,
        "seasonal_benchmarks": seasonal,
        "monthly_benchmarks": monthly_benchmarks,
        "rating_tiers": rating_tiers,
        "competitors": [
            {
                "name": c["name"],
                "platform": c["platform"],
                "price_eur": c["base_price_eur"],
                "rating": c.get("rating"),
                "max_guests": c.get("max_guests"),
            }
            for c in sorted(filtered, key=lambda x: x["base_price_eur"])
        ],
        "issues": issues,
    }


def _percentile(sorted_list, pct):
    """Compute percentile from a sorted list."""
    if not sorted_list:
        return 0
    k = (len(sorted_list) - 1) * pct / 100
    f = int(k)
    c = f + 1
    if c >= len(sorted_list):
        return sorted_list[-1]
    return sorted_list[f] + (k - f) * (sorted_list[c] - sorted_list[f])


def _compute_rating_tiers(competitors):
    """Group competitors by rating tier and compute avg price per tier."""
    tiers = {
        "premium": {"label": "4.8+ rating", "min_rating": 4.8, "prices": []},
        "good": {"label": "4.5-4.79 rating", "min_rating": 4.5, "prices": []},
        "average": {"label": "4.0-4.49 rating", "min_rating": 4.0, "prices": []},
        "below_avg": {"label": "Below 4.0", "min_rating": 0, "prices": []},
    }

    for c in competitors:
        if not c.get("rating") or not c.get("rating_scale"):
            continue
        r = _normalize_rating(c["rating"], c["rating_scale"])
        price = c.get("base_price_eur", 0)
        if not price:
            continue

        if r >= 4.8:
            tiers["premium"]["prices"].append(price)
        elif r >= 4.5:
            tiers["good"]["prices"].append(price)
        elif r >= 4.0:
            tiers["average"]["prices"].append(price)
        else:
            tiers["below_avg"]["prices"].append(price)

    result = {}
    for key, tier in tiers.items():
        if tier["prices"]:
            result[key] = {
                "label": tier["label"],
                "count": len(tier["prices"]),
                "avg_price_eur": round(statistics.mean(tier["prices"]), 2),
                "median_price_eur": round(statistics.median(tier["prices"]), 2),
                "min_price_eur": min(tier["prices"]),
                "max_price_eur": max(tier["prices"]),
            }
        else:
            result[key] = {
                "label": tier["label"],
                "count": 0,
                "avg_price_eur": 0,
                "median_price_eur": 0,
                "min_price_eur": 0,
                "max_price_eur": 0,
            }

    return result


def _compute_rating_rank(competitors, your_rating):
    """Compute where your rating ranks among competitors."""
    ratings = []
    for c in competitors:
        if c.get("rating") and c.get("rating_scale"):
            ratings.append(_normalize_rating(c["rating"], c["rating_scale"]))
    if not ratings:
        return "unknown"
    better_count = sum(1 for r in ratings if r > your_rating)
    rank = better_count + 1
    total = len(ratings) + 1  # Including you
    return f"{rank}/{total}"


def _compute_monthly_benchmarks(seasonal, avg_price, median_price, p25, p75):
    """
    Compute per-month competitor benchmarks using seasonal data.

    Applies seasonal multipliers to the base competitor averages.
    """
    monthly = {}

    # Compute seasonal multipliers from the seasonal benchmark data
    # Base: shoulder season (most months = baseline)
    shoulder = seasonal.get("shoulder_season", {})
    peak = seasonal.get("peak_season", {})
    low = seasonal.get("low_season", {})

    shoulder_avg = shoulder.get("avg_price_eur", avg_price)
    peak_avg = peak.get("avg_price_eur", avg_price)
    low_avg = low.get("avg_price_eur", avg_price)

    if shoulder_avg > 0:
        peak_multiplier = peak_avg / shoulder_avg
        low_multiplier = low_avg / shoulder_avg
    else:
        peak_multiplier = 1.15
        low_multiplier = 0.85

    for cm in range(1, 13):
        season_key = MONTH_TO_SEASON[cm]
        season_data = seasonal.get(season_key, {})

        season_avg = season_data.get("avg_price_eur", avg_price)
        season_median = season_data.get("median_price_eur", median_price)
        season_low = season_data.get("low_end_eur", p25)
        season_high = season_data.get("high_end_eur", p75)
        season_occ = season_data.get("occupancy_pct", 42)

        monthly[cm] = {
            "month_number": cm,
            "month_name": MONTH_NAMES[cm],
            "season": season_key,
            "season_label": SEASON_LABELS[season_key],
            "competitor_avg_eur": round(season_avg, 2),
            "competitor_median_eur": round(season_median, 2),
            "competitor_low_eur": round(season_low, 2),
            "competitor_high_eur": round(season_high, 2),
            "market_occupancy_pct": season_occ,
        }

    return monthly


def _empty_result(issues):
    """Return empty result when no data available."""
    monthly = {}
    for cm in range(1, 13):
        monthly[cm] = {
            "month_number": cm,
            "month_name": MONTH_NAMES[cm],
            "season": MONTH_TO_SEASON[cm],
            "season_label": SEASON_LABELS[MONTH_TO_SEASON[cm]],
            "competitor_avg_eur": 40,
            "competitor_median_eur": 40,
            "competitor_low_eur": 25,
            "competitor_high_eur": 55,
            "market_occupancy_pct": 42,
        }
    return {
        "competitor_count": 0,
        "avg_price_eur": 40,
        "median_price_eur": 40,
        "p25_price_eur": 25,
        "p75_price_eur": 55,
        "avg_rating": 0,
        "your_position": {},
        "seasonal_benchmarks": {},
        "monthly_benchmarks": monthly,
        "rating_tiers": {},
        "competitors": [],
        "issues": issues,
    }


if __name__ == "__main__":
    result = analyze_competitors()
    print(f"\nCompetitor Analysis (max 3 guests, central Tirana)")
    print(f"{'=' * 65}")
    print(f"  Competitors analyzed: {result['competitor_count']}")
    print(f"  Avg price:    EUR {result['avg_price_eur']}")
    print(f"  Median price: EUR {result['median_price_eur']}")
    print(f"  25th pct:     EUR {result['p25_price_eur']}")
    print(f"  75th pct:     EUR {result['p75_price_eur']}")
    print(f"  Avg rating:   {result['avg_rating']}/5")

    pos = result.get("your_position", {})
    if pos:
        print(f"\n  YOUR POSITION:")
        print(f"    Price: EUR {pos['your_price_eur']} ({pos['price_vs_avg_pct']:+.1f}% vs avg)")
        print(f"    Price percentile: {pos['price_percentile']}%")
        print(f"    Rating rank: {pos['rating_rank']}")
        print(f"    Cheaper: {pos['competitors_cheaper']} | Same: {pos['competitors_same_price']} | More: {pos['competitors_more_expensive']}")

    tiers = result.get("rating_tiers", {})
    if tiers:
        print(f"\n  PRICE BY RATING TIER:")
        for key in ["premium", "good", "average", "below_avg"]:
            t = tiers.get(key, {})
            if t.get("count", 0) > 0:
                print(f"    {t['label']}: EUR {t['avg_price_eur']} avg ({t['count']} listings)")

    print(f"\n  MONTHLY BENCHMARKS:")
    print(f"  {'Month':<12} {'Season':<12} {'Avg':>8} {'Median':>8} {'Low':>8} {'High':>8} {'Occ':>6}")
    print(f"  {'-'*12} {'-'*12} {'-'*8} {'-'*8} {'-'*8} {'-'*8} {'-'*6}")
    for cm in range(1, 13):
        b = result["monthly_benchmarks"][cm]
        print(f"  {b['month_name']:<12} {b['season_label']:<12} "
              f"EUR{b['competitor_avg_eur']:>5} EUR{b['competitor_median_eur']:>5} "
              f"EUR{b['competitor_low_eur']:>5} EUR{b['competitor_high_eur']:>5} "
              f"{b['market_occupancy_pct']:>4}%")

    if result["issues"]:
        print(f"\n  Issues:")
        for issue in result["issues"]:
            print(f"    [{issue['severity']}] {issue['message']}")
    print()
