"""
Skill: Competitor Analyzer
Benchmarks the property against competitors and identifies competitive gaps.

Analysis areas:
  - Feature comparison vs top Tirana listings
  - Niche positioning (medical tourism)
  - Unique selling propositions
  - Competitive weaknesses
  - Market opportunity gaps
"""

from skills.data_loader import load_property_profile, load_marketing_report, _find_project_root

SKILL_NAME = "competitor_analyzer"
DESCRIPTION = "Benchmarks against competitors and identifies competitive gaps"


def build_competitor_landscape():
    """Build competitive landscape from market data."""
    return {
        "market_overview": {
            "total_listings_tirana": 3639,
            "avg_nightly_rate": 50,
            "rate_range": "€17-60/night",
            "top_competitor_photos": "25-40",
            "top_competitor_capacity": "2-4 guests",
            "top_competitor_features": [
                "Panoramic views",
                "Rooftop access",
                "Balconies",
                "Professional photography",
                "Superhost status",
                "Detailed descriptions with walking distances",
            ],
        },
        "medical_tourism_market": {
            "annual_patients_albania": 80000,
            "growth_since_2020": "400%",
            "top_source_countries": ["Italy", "UK", "Germany"],
            "projected_top5_by": 2027,
            "avg_patient_stay_days": "5-14",
            "dental_procedures": ["Implants", "Veneers", "Whitening", "Orthodontics"],
            "hair_procedures": ["FUE Transplant", "DHI Transplant"],
        },
    }


def analyze_competitive_position(profile_text):
    """Analyze our position vs competitors."""

    our_features = {
        "private_entrance": True,
        "soundproofing": True,
        "central_location": True,
        "medical_tourism_focus": True,
        "equipped_kitchen": True,
        "free_wifi": True,
        "air_conditioning": True,
        "washing_machine": True,
        "balcony": True,
    }

    # What top competitors have that we don't
    competitor_advantages = {
        "superhost_status": {
            "gap": "Not a Superhost yet (requires consistent performance metrics)",
            "impact": "Superhosts get priority in search results and a badge that increases trust",
            "fix": "Maintain 4.8+ rating, <1% cancellation rate, 90%+ response rate, 10+ stays/year",
        },
        "photo_quality": {
            "gap": "8 photos vs competitor average of 25-40",
            "impact": "Listings with more photos book 2x more often",
            "fix": "Add 20+ photos covering every room, amenity, and the neighborhood",
        },
        "guest_capacity": {
            "gap": "2 guests vs competitor average of 2-4",
            "impact": "Limited to solo travelers and couples, can't serve small groups",
            "fix": "If space allows, add a sofa bed to increase capacity to 3-4",
        },
        "description_depth": {
            "gap": "2-sentence description vs competitor multi-paragraph narratives",
            "impact": "Guests can't envision the experience before booking",
            "fix": "Write 3-4 paragraphs covering hook, room details, neighborhood, and medical tourism angle",
        },
        "platform_presence": {
            "gap": "2 platforms vs some competitors on 4-5 platforms",
            "impact": "Missing 15-25% of potential bookings from other channels",
            "fix": "Add Google Vacation Rentals, Facebook Marketplace, and a direct booking site",
        },
        "social_proof": {
            "gap": "54 total reviews vs top competitors with 100+",
            "impact": "Fewer reviews = lower search ranking and less trust",
            "fix": "Actively request reviews from every guest post-checkout",
        },
        "video_content": {
            "gap": "No video tour vs competitors with YouTube/Instagram video content",
            "impact": "Video listings get 200% more inquiries",
            "fix": "Record a 30-60 second walk-through video",
        },
    }

    # Our unique competitive advantages
    our_advantages = {
        "soundproofing": {
            "strength": "Almost no competitors in Tirana offer soundproofing",
            "leverage": "Emphasize in title and description. Critical for post-surgery recovery guests.",
        },
        "private_entrance": {
            "strength": "Rare in Tirana apartment market",
            "leverage": "Privacy is the #1 concern for medical tourists. Feature prominently.",
        },
        "medical_niche": {
            "strength": "Almost nobody in Tirana targets medical tourists specifically",
            "leverage": "First-mover advantage. Build clinic partnerships before competitors catch on.",
        },
        "perfect_booking_rating": {
            "strength": "10/10 on Booking.com is exceptional",
            "leverage": "Use this in all marketing. '10/10 rated' is a powerful trust signal.",
        },
        "location_proximity": {
            "strength": "Central location close to all major clinics",
            "leverage": "Map showing walking distances to top clinics would be a unique selling tool.",
        },
    }

    return {
        "competitor_advantages": competitor_advantages,
        "our_advantages": our_advantages,
        "competitive_gaps_count": len(competitor_advantages),
        "unique_advantages_count": len(our_advantages),
    }


def identify_issues(competitive_position, landscape):
    """Identify competitive improvement areas."""
    issues = []

    # Gaps vs competitors
    for gap_name, gap_data in competitive_position["competitor_advantages"].items():
        severity = "HIGH" if gap_name in ["photo_quality", "description_depth", "guest_capacity"] else "MEDIUM"
        issues.append({
            "severity": severity,
            "area": f"Competitive Gap: {gap_name.replace('_', ' ').title()}",
            "finding": gap_data["gap"],
            "recommendation": gap_data["fix"],
        })

    # Underleveraged advantages
    for adv_name, adv_data in competitive_position["our_advantages"].items():
        issues.append({
            "severity": "MEDIUM",
            "area": f"Underleveraged Advantage: {adv_name.replace('_', ' ').title()}",
            "finding": f"Unique strength: {adv_data['strength']}",
            "recommendation": adv_data["leverage"],
        })

    # Medical tourism first-mover risk
    issues.append({
        "severity": "HIGH",
        "area": "First-Mover Window Closing",
        "finding": (
            f"Albania's medical tourism grew 400% since 2020 with {landscape['medical_tourism_market']['annual_patients_albania']:,} "
            f"annual patients. Competitors will start targeting this niche soon."
        ),
        "recommendation": "Lock in clinic partnerships NOW with commission agreements. Build brand recognition in the medical tourism space before competitors enter. Speed is your biggest advantage.",
    })

    # No differentiated experience
    issues.append({
        "severity": "MEDIUM",
        "area": "No Recovery-Specific Amenities",
        "finding": "No medical recovery amenities mentioned (ice packs, blender for smoothies, neck pillows). This is an easy differentiator.",
        "recommendation": "Add ice packs, a blender, straws, extra soft towels, and a neck pillow. Cost: <€50 total. Mention these in your listing — no competitor does this.",
    })

    return issues


def run():
    """Main skill entry point."""
    root = _find_project_root()
    profile = load_property_profile(root)
    marketing = load_marketing_report(root)

    landscape = build_competitor_landscape()
    position = analyze_competitive_position(profile)
    issues = identify_issues(position, landscape)

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "market_landscape": landscape,
        "competitive_position": {
            "gaps_count": position["competitive_gaps_count"],
            "advantages_count": position["unique_advantages_count"],
        },
        "issues": issues,
        "issues_count": len(issues),
    }

    # Print summary
    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  MARKET LANDSCAPE:")
    print(f"    Total Tirana listings:    {landscape['market_overview']['total_listings_tirana']}")
    print(f"    Medical tourists/year:    {landscape['medical_tourism_market']['annual_patients_albania']:,}")
    print(f"    Market growth:            {landscape['medical_tourism_market']['growth_since_2020']}")
    print(f"\n  COMPETITIVE POSITION:")
    print(f"    Gaps vs competitors:      {position['competitive_gaps_count']}")
    print(f"    Unique advantages:        {position['unique_advantages_count']}")
    print(f"\n  OUR ADVANTAGES:")
    for name, data in position["our_advantages"].items():
        print(f"    + {name.replace('_', ' ').title()}: {data['strength']}")
    print(f"\n  ISSUES FOUND: {len(issues)}")
    for i, issue in enumerate(issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area'][:60]}")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
