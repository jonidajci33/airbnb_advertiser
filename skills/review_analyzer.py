"""
Skill: Review Analyzer
Analyzes guest review patterns and identifies experience improvement areas.

Analysis areas:
  - Review volume and velocity
  - Rating trends
  - Review solicitation effectiveness
  - Guest experience gaps (based on known data)
  - Post-stay engagement
"""

from skills.data_loader import load_property_profile, _find_project_root

SKILL_NAME = "review_analyzer"
DESCRIPTION = "Analyzes guest reviews and identifies experience improvement areas"


def analyze_review_metrics():
    """Analyze review data from property profiles."""

    # Known data from property_profile.md
    metrics = {
        "airbnb": {
            "rating": 4.88,
            "total_reviews": 33,
            "platform": "Airbnb",
        },
        "booking_com": {
            "rating": 10.0,
            "total_reviews": 21,
            "platform": "Booking.com",
        },
    }

    total_reviews = sum(p["total_reviews"] for p in metrics.values())
    weighted_rating = (
        metrics["airbnb"]["rating"] / 5 * metrics["airbnb"]["total_reviews"] +
        metrics["booking_com"]["rating"] / 10 * metrics["booking_com"]["total_reviews"]
    ) / total_reviews

    return {
        "platforms": metrics,
        "total_reviews": total_reviews,
        "weighted_satisfaction": round(weighted_rating * 100, 1),
        "avg_reviews_per_platform": round(total_reviews / len(metrics), 1),
    }


def analyze_review_velocity(review_metrics):
    """Estimate review velocity and project future growth."""

    # Property has been active for approximately 2 years
    months_active = 24  # estimated
    total = review_metrics["total_reviews"]
    monthly_rate = total / months_active

    # Benchmarks
    target_monthly = 5  # healthy listing
    superhost_threshold = 10  # stays per year minimum

    return {
        "estimated_months_active": months_active,
        "avg_reviews_per_month": round(monthly_rate, 1),
        "target_reviews_per_month": target_monthly,
        "velocity_vs_target_pct": round(monthly_rate / target_monthly * 100, 1),
        "months_to_100_reviews": round((100 - total) / monthly_rate) if monthly_rate > 0 else None,
        "months_to_superhost": round((superhost_threshold - total / (months_active / 12)) * 12 / monthly_rate) if monthly_rate > 0 else None,
    }


def analyze_guest_experience():
    """Analyze guest experience gaps based on property data."""

    experience_areas = {
        "arrival_experience": {
            "current": "Private entrance available",
            "status": "GOOD",
            "gap": "No mention of check-in guide, key handoff process, or arrival instructions",
            "improvement": "Create a detailed arrival guide with photos of the entrance, key location, and parking info",
        },
        "welcome_package": {
            "current": "None",
            "status": "MISSING",
            "gap": "No welcome basket or personal touch at arrival",
            "improvement": "Add Albanian coffee, local biscuits, water bottle, and a handwritten welcome note (~€5/guest)",
        },
        "recovery_amenities": {
            "current": "None specifically for medical tourists",
            "status": "MISSING",
            "gap": "No ice packs, blender, extra soft towels, or recovery-specific amenities",
            "improvement": "Stock: ice packs, blender for smoothies, straws, neck pillow, extra soft towels. Total cost: <€50",
        },
        "digital_guidebook": {
            "current": "None",
            "status": "MISSING",
            "gap": "No digital guide with WiFi password, local tips, emergency numbers, clinic locations",
            "improvement": "Create a Touchstay or PDF guidebook with: WiFi, apartment guide, nearest pharmacy/grocery/ATM, restaurants, transport tips, clinic map",
        },
        "post_checkout_followup": {
            "current": "None",
            "status": "MISSING",
            "gap": "No follow-up message asking for reviews",
            "improvement": "Send a thank-you message 24 hours after checkout. Guests asked for reviews are 2x more likely to leave one.",
        },
        "flexible_checkin": {
            "current": "Standard hours assumed",
            "status": "NEEDS_WORK",
            "gap": "Medical tourists often arrive on early flights or have procedures at odd hours",
            "improvement": "Offer flexible check-in/check-out when possible. Mention it in the listing.",
        },
        "kitchen_amenities": {
            "current": "Microwave, toaster, basic equipment",
            "status": "GOOD",
            "gap": "Post-dental patients need soft food options. No blender or soft food guide provided.",
            "improvement": "Add blender and provide a list of nearby restaurants with soft food options.",
        },
        "soundproofing": {
            "current": "Soundproofing installed",
            "status": "EXCELLENT",
            "gap": "This is a unique feature but may not be emphasized enough",
            "improvement": "Make soundproofing a headline feature. Medical tourists recovering from procedures need quiet.",
        },
    }

    good = sum(1 for e in experience_areas.values() if e["status"] in ("GOOD", "EXCELLENT"))
    missing = sum(1 for e in experience_areas.values() if e["status"] == "MISSING")
    needs_work = sum(1 for e in experience_areas.values() if e["status"] == "NEEDS_WORK")

    return {
        "areas": experience_areas,
        "excellent_count": sum(1 for e in experience_areas.values() if e["status"] == "EXCELLENT"),
        "good_count": good,
        "missing_count": missing,
        "needs_work_count": needs_work,
        "experience_score_pct": round(good / len(experience_areas) * 100, 1),
    }


def identify_issues(review_metrics, velocity, experience):
    """Identify review and experience improvement areas."""
    issues = []

    # Low review velocity
    if velocity["avg_reviews_per_month"] < velocity["target_reviews_per_month"]:
        issues.append({
            "severity": "HIGH",
            "area": "Low Review Velocity",
            "finding": f"Only {velocity['avg_reviews_per_month']} reviews/month vs target of {velocity['target_reviews_per_month']}/month",
            "recommendation": "Proactively ask every guest for a review 24h after checkout. Consider a small incentive (future discount coupon) for leaving a review.",
        })

    # Platform imbalance
    airbnb_reviews = review_metrics["platforms"]["airbnb"]["total_reviews"]
    booking_reviews = review_metrics["platforms"]["booking_com"]["total_reviews"]
    if abs(airbnb_reviews - booking_reviews) > 15:
        lower = "Booking.com" if booking_reviews < airbnb_reviews else "Airbnb"
        issues.append({
            "severity": "MEDIUM",
            "area": f"Review Imbalance ({lower})",
            "finding": f"Airbnb has {airbnb_reviews} reviews vs Booking.com has {booking_reviews}. Uneven platform presence.",
            "recommendation": f"Focus review requests on {lower} to balance. Both platforms rank listings higher with more reviews.",
        })

    # Missing experience areas
    for area_name, area_data in experience["areas"].items():
        if area_data["status"] == "MISSING":
            issues.append({
                "severity": "HIGH" if area_name in ["post_checkout_followup", "welcome_package"] else "MEDIUM",
                "area": f"Missing: {area_name.replace('_', ' ').title()}",
                "finding": area_data["gap"],
                "recommendation": area_data["improvement"],
            })

    # No review response strategy
    issues.append({
        "severity": "MEDIUM",
        "area": "No Review Response Strategy",
        "finding": "No evidence of systematic review responses. Responding to reviews boosts search ranking and builds trust.",
        "recommendation": "Respond to every review within 24 hours. Thank positive reviewers by name. For any constructive feedback, acknowledge and explain how you've improved.",
    })

    # Low total reviews for Superhost
    total = review_metrics["total_reviews"]
    if total < 100:
        issues.append({
            "severity": "MEDIUM",
            "area": "Below Superhost Review Threshold",
            "finding": f"54 total reviews. Superhost status requires consistent volume. Listings with 100+ reviews rank significantly higher.",
            "recommendation": f"At current rate, you'll reach 100 reviews in ~{velocity['months_to_100_reviews']} months. Increase velocity by asking every guest for a review.",
        })

    return issues


def run():
    """Main skill entry point."""
    root = _find_project_root()
    profile = load_property_profile(root)

    review_metrics = analyze_review_metrics()
    velocity = analyze_review_velocity(review_metrics)
    experience = analyze_guest_experience()
    issues = identify_issues(review_metrics, velocity, experience)

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "review_metrics": review_metrics,
        "velocity": velocity,
        "guest_experience": {
            "experience_score_pct": experience["experience_score_pct"],
            "excellent": experience["excellent_count"],
            "good": experience["good_count"],
            "missing": experience["missing_count"],
            "needs_work": experience["needs_work_count"],
        },
        "issues": issues,
        "issues_count": len(issues),
    }

    # Print summary
    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  REVIEW METRICS:")
    print(f"    Total reviews:       {review_metrics['total_reviews']}")
    print(f"    Satisfaction:        {review_metrics['weighted_satisfaction']}%")
    print(f"    Airbnb:              {review_metrics['platforms']['airbnb']['rating']}/5 ({review_metrics['platforms']['airbnb']['total_reviews']} reviews)")
    print(f"    Booking.com:         {review_metrics['platforms']['booking_com']['rating']}/10 ({review_metrics['platforms']['booking_com']['total_reviews']} reviews)")
    print(f"\n  REVIEW VELOCITY:")
    print(f"    Monthly rate:        {velocity['avg_reviews_per_month']}/month")
    print(f"    Target:              {velocity['target_reviews_per_month']}/month")
    print(f"    Months to 100:       {velocity['months_to_100_reviews']}")
    print(f"\n  GUEST EXPERIENCE:")
    print(f"    Score:               {experience['experience_score_pct']}%")
    print(f"    Excellent areas:     {experience['excellent_count']}")
    print(f"    Good areas:          {experience['good_count']}")
    print(f"    Missing areas:       {experience['missing_count']}")
    print(f"    Needs work:          {experience['needs_work_count']}")
    print(f"\n  ISSUES FOUND: {len(issues)}")
    for i, issue in enumerate(issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area']}")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
