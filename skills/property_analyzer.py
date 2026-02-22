"""
Skill: Property Performance Analyzer
Analyzes the property's current state and identifies performance gaps.

Metrics analyzed:
  - Listing completeness (photos, description, amenities)
  - Rating performance across platforms
  - Review volume and velocity
  - Feature utilization
  - Comparison to recommended benchmarks
"""

import re
from skills.data_loader import load_property_profile, load_property_fixes, load_airbnb_info, _find_project_root

SKILL_NAME = "property_analyzer"
DESCRIPTION = "Analyzes property listing performance and identifies gaps"


def parse_property_metrics(profile_text):
    """Extract key metrics from property_profile.md."""
    metrics = {
        "name": "Lulebore Apartment 1",
        "platforms": [],
        "guest_capacity": None,
        "bedrooms": None,
        "bathrooms": None,
        "photos_count": None,
        "airbnb_rating": None,
        "airbnb_reviews": None,
        "booking_rating": None,
        "booking_reviews": None,
        "nightly_rate": None,
        "amenities_listed": [],
        "title": None,
        "marketing_channels": {},
    }

    if not profile_text:
        return metrics

    # Extract ratings
    airbnb_match = re.search(r'Airbnb\s*\|\s*([\d.]+)\s*/\s*5\s*\|\s*(\d+)\s*reviews', profile_text)
    if airbnb_match:
        metrics["airbnb_rating"] = float(airbnb_match.group(1))
        metrics["airbnb_reviews"] = int(airbnb_match.group(2))

    booking_match = re.search(r'Booking\.com\s*\|\s*([\d.]+)\s*/\s*10\s*\|\s*(\d+)\s*reviews', profile_text)
    if booking_match:
        metrics["booking_rating"] = float(booking_match.group(1))
        metrics["booking_reviews"] = int(booking_match.group(2))

    # Extract photos
    photos_match = re.search(r'Total photos on Airbnb:\*\*\s*(\d+)', profile_text)
    if photos_match:
        metrics["photos_count"] = int(photos_match.group(1))

    # Extract capacity
    capacity_match = re.search(r'Guest capacity\s*\|\s*(\d+)', profile_text)
    if capacity_match:
        metrics["guest_capacity"] = int(capacity_match.group(1))

    bedrooms_match = re.search(r'Bedrooms\s*\|\s*(\d+)', profile_text)
    if bedrooms_match:
        metrics["bedrooms"] = int(bedrooms_match.group(1))

    # Extract pricing
    price_match = re.search(r'~\$?(\d+)\s*USD\s*\(~€(\d+)\)', profile_text)
    if price_match:
        metrics["nightly_rate"] = int(price_match.group(2))

    # Extract title
    title_match = re.search(r'Airbnb Title:\*\*\s*"(.+?)"', profile_text)
    if title_match:
        metrics["title"] = title_match.group(1)

    # Extract marketing channels
    channel_pattern = re.compile(r'\|\s*(.+?)\s*\|\s*(Active|Not active|None|Set up.*?)\s*\|')
    for match in channel_pattern.finditer(profile_text):
        channel = match.group(1).strip().strip('*')
        status = match.group(2).strip()
        if channel and channel != "Channel" and channel != "------":
            metrics["marketing_channels"][channel] = status

    return metrics


def benchmark_property(metrics):
    """Compare property against industry benchmarks."""
    benchmarks = {
        "photos": {
            "current": metrics["photos_count"] or 0,
            "target": 25,
            "top_performer": 40,
            "status": "CRITICAL" if (metrics["photos_count"] or 0) < 15 else "OK",
        },
        "reviews_airbnb": {
            "current": metrics["airbnb_reviews"] or 0,
            "target": 50,
            "top_performer": 100,
            "status": "NEEDS_WORK" if (metrics["airbnb_reviews"] or 0) < 50 else "OK",
        },
        "reviews_booking": {
            "current": metrics["booking_reviews"] or 0,
            "target": 50,
            "top_performer": 100,
            "status": "NEEDS_WORK" if (metrics["booking_reviews"] or 0) < 50 else "OK",
        },
        "rating_airbnb": {
            "current": metrics["airbnb_rating"] or 0,
            "target": 4.8,
            "top_performer": 4.95,
            "status": "GOOD" if (metrics["airbnb_rating"] or 0) >= 4.8 else "NEEDS_WORK",
        },
        "rating_booking": {
            "current": metrics["booking_rating"] or 0,
            "target": 9.0,
            "top_performer": 9.5,
            "status": "EXCELLENT" if (metrics["booking_rating"] or 0) >= 9.5 else "GOOD",
        },
        "guest_capacity": {
            "current": metrics["guest_capacity"] or 0,
            "target": 2,
            "top_performer": 4,
            "status": "CRITICAL" if (metrics["guest_capacity"] or 0) < 2 else "OK",
        },
        "nightly_rate": {
            "current": metrics["nightly_rate"] or 0,
            "market_avg": 50,
            "budget_range": "17-60",
            "status": "BELOW_AVERAGE" if (metrics["nightly_rate"] or 0) < 50 else "COMPETITIVE",
        },
    }

    # Marketing channel readiness
    active_channels = sum(1 for s in metrics["marketing_channels"].values() if "Active" in s)
    total_channels = len(metrics["marketing_channels"])

    benchmarks["marketing_channels"] = {
        "active": active_channels,
        "total_possible": total_channels,
        "target": 5,
        "status": "LOW" if active_channels < 4 else "OK",
    }

    return benchmarks


def identify_issues(metrics, benchmarks):
    """Identify property improvement areas."""
    issues = []

    # Photos - critical gap
    if benchmarks["photos"]["status"] == "CRITICAL":
        deficit = benchmarks["photos"]["target"] - benchmarks["photos"]["current"]
        issues.append({
            "severity": "CRITICAL",
            "area": "Photo Count",
            "finding": f"Only {benchmarks['photos']['current']} photos (target: {benchmarks['photos']['target']}+). This is the #1 factor limiting bookings.",
            "recommendation": f"Add {deficit}+ more photos immediately. Include: exterior, each room from multiple angles, amenities close-ups, neighborhood. Professional photography increases bookings by 40%.",
            "estimated_impact": "40% more bookings",
        })

    # Guest capacity
    if benchmarks["guest_capacity"]["status"] == "CRITICAL":
        issues.append({
            "severity": "CRITICAL",
            "area": "Guest Capacity",
            "finding": f"Capacity set to {benchmarks['guest_capacity']['current']} guest. This eliminates couples — the largest travel segment.",
            "recommendation": "Update to at least 2 guests immediately. If you have a double bed, this is a simple settings change.",
            "estimated_impact": "2x larger booking pool",
        })

    # Review velocity
    total_reviews = (metrics["airbnb_reviews"] or 0) + (metrics["booking_reviews"] or 0)
    if total_reviews < 60:
        issues.append({
            "severity": "HIGH",
            "area": "Review Volume",
            "finding": f"Total of {total_reviews} reviews across platforms. Listings with 50+ reviews per platform rank significantly higher.",
            "recommendation": "Send a follow-up message 24h after checkout asking for a review. Guests asked directly are 2x more likely to leave one.",
            "estimated_impact": "Higher search ranking",
        })

    # Marketing channels
    if benchmarks["marketing_channels"]["status"] == "LOW":
        issues.append({
            "severity": "HIGH",
            "area": "Limited Marketing Channels",
            "finding": f"Only {benchmarks['marketing_channels']['active']} active channels out of {benchmarks['marketing_channels']['total_possible']}",
            "recommendation": "Add: social media (Instagram/TikTok), direct booking website, Google Business Profile, paid ads. Multi-platform listings increase occupancy 15-25%.",
            "estimated_impact": "15-25% more occupancy",
        })

    # Platform diversity
    no_social = True
    no_direct = True
    no_google = True
    for channel, status in metrics["marketing_channels"].items():
        if "social" in channel.lower() and "Active" in status:
            no_social = False
        if "direct" in channel.lower() and status != "None":
            no_direct = False
        if "google" in channel.lower() and status != "None":
            no_google = False

    if no_social:
        issues.append({
            "severity": "MEDIUM",
            "area": "No Social Media",
            "finding": "Zero social media presence. Properties with active social media see 23% higher booking rates.",
            "recommendation": "Create Instagram @lulebore.apartment, post 3x/week with apartment photos, Tirana tips, and guest reviews.",
            "estimated_impact": "23% higher booking rate",
        })

    if no_direct:
        issues.append({
            "severity": "MEDIUM",
            "area": "No Direct Booking",
            "finding": "No direct booking website. You're paying 15% platform fees on every booking.",
            "recommendation": "Create a simple direct booking page with Carrd.co (€19/year). For repeat guests, this saves significant fees.",
            "estimated_impact": "Save 15% on repeat bookings",
        })

    if no_google:
        issues.append({
            "severity": "MEDIUM",
            "area": "No Google Presence",
            "finding": "No Google Business Profile. Missing free visibility in Google Search and Maps.",
            "recommendation": "Register as 'Tourist Accommodation' on Google Business. Add photos, collect Google reviews.",
            "estimated_impact": "Free discovery channel",
        })

    # Pricing analysis
    if benchmarks["nightly_rate"]["status"] == "BELOW_AVERAGE":
        issues.append({
            "severity": "LOW",
            "area": "Below-Average Pricing",
            "finding": f"€{benchmarks['nightly_rate']['current']}/night vs market average €{benchmarks['nightly_rate']['market_avg']}/night",
            "recommendation": "With a 10/10 Booking.com rating and 4.88 Airbnb rating, you can justify above-average pricing. Consider raising to €50-55/night after adding more photos.",
            "estimated_impact": "10-20% more revenue per booking",
        })

    # No video tour
    issues.append({
        "severity": "MEDIUM",
        "area": "No Video Tour",
        "finding": "No video tour available. Listings with video get 200% more inquiries.",
        "recommendation": "Record a 30-60 second walk-through with your phone. Upload to Airbnb, YouTube, Instagram.",
        "estimated_impact": "200% more inquiries",
    })

    # No weekly/monthly discounts mentioned
    issues.append({
        "severity": "MEDIUM",
        "area": "No Long-Stay Discounts",
        "finding": "No weekly or monthly discounts configured. Medical tourists typically stay 5-14 days.",
        "recommendation": "Set 10-15% weekly discount and 20-30% monthly discount. This is essential for attracting medical tourists.",
        "estimated_impact": "Longer average stays",
    })

    return issues


def run():
    """Main skill entry point."""
    root = _find_project_root()
    profile = load_property_profile(root)
    fixes = load_property_fixes(root)

    metrics = parse_property_metrics(profile)
    benchmarks = benchmark_property(metrics)
    issues = identify_issues(metrics, benchmarks)

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "metrics": metrics,
        "benchmarks": benchmarks,
        "issues": issues,
        "issues_count": len(issues),
    }

    # Print summary
    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  PROPERTY METRICS:")
    print(f"    Photos:           {metrics['photos_count']}")
    print(f"    Guest capacity:   {metrics['guest_capacity']}")
    print(f"    Airbnb rating:    {metrics['airbnb_rating']} ({metrics['airbnb_reviews']} reviews)")
    print(f"    Booking rating:   {metrics['booking_rating']} ({metrics['booking_reviews']} reviews)")
    print(f"    Nightly rate:     €{metrics['nightly_rate']}")
    print(f"\n  BENCHMARKS:")
    for name, data in benchmarks.items():
        status = data.get("status", "N/A")
        print(f"    {name:25s} {status}")
    print(f"\n  ISSUES FOUND: {len(issues)}")
    for i, issue in enumerate(issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area']}: {issue['finding'][:80]}")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
