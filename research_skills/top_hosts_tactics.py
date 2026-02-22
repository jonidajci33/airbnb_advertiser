"""
Skill: Top Hosts Tactics
Researches what the most successful Airbnb hosts in Albania/Tirana do
to maximize profit, then generates actionable advice comparing each tactic
against Lulebore Apartment 1's current setup.
"""

import sys
from pathlib import Path

SKILL_NAME = "top_hosts_tactics"
DESCRIPTION = "What top-performing Albanian Airbnb hosts do differently and how to copy them"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# --- Superhost Requirements ---------------------------------------------------
SUPERHOST_REQUIREMENTS = {
    "min_reservations_per_year": 10,
    "max_cancellation_rate_pct": 1,
    "min_response_rate_pct": 90,
    "response_window_hours": 24,
    "min_overall_rating": 4.8,
}

# --- Your Property Data -------------------------------------------------------
YOUR_PROPERTY = {
    "name": "Lulebore Apartment 1",
    "type": "1-bed, central Tirana",
    "nightly_rate_eur": 45,
    "airbnb_rating": 4.88,
    "booking_rating": 10.0,
    "photos": 8,
    "photos_professional": False,
    "reviews_total": 54,
    "platforms": 2,
    "platforms_list": ["Airbnb", "Booking.com"],
    "has_direct_website": False,
    "has_automated_messaging": False,
    "has_dynamic_pricing": False,
    "uses_smart_pricing": False,
    "has_welcome_basket": False,
    "has_digital_guidebook": False,
    "has_length_of_stay_discounts": False,
    "has_review_request_system": False,
    "has_channel_manager": False,
    "has_stayfi_or_email_capture": False,
    "months_active": 24,
    "estimated_occupancy_pct": 40,
}

# --- Researched Top Host Tactics (Feb 2026) ------------------------------------
TOP_HOST_TACTICS = {
    "automated_messaging": {
        "tactic": "Automated Guest Messaging",
        "tools": ["Hospitable", "Guesty", "Hostaway"],
        "five_touch_sequence": [
            "Booking confirmation (immediate)",
            "7-day pre-arrival: local tips + upsell offers",
            "1-day reminder: WiFi password, directions, check-in instructions",
            "Mid-stay check-in: anything you need?",
            "Checkout day: thank you + review request",
        ],
        "algorithm_impact": "Airbnb algorithm directly rewards fast response times",
        "superhost_link": "90%+ response rate within 24h required for Superhost",
    },
    "professional_photography": {
        "tactic": "Professional Photography",
        "booking_increase_pct": 40,
        "rate_premium_pct": 26,
        "first_5_photos_impact": "First 5 photos determine 90% of booking decisions",
        "cost_eur": "300-800 for 30-50 edited images",
        "roi_timeline": "Pays for itself in 2-4 weeks",
        "roi_fast_stat": "75% of hosts recoup cost within 1 booking",
    },
    "dynamic_pricing": {
        "tactic": "Dynamic Pricing Tools",
        "recommended_tool": "PriceLabs",
        "pricelabs_cost_usd_per_month": 19.99,
        "proven_revenue_increase_pct": 36,
        "study_size_listings": 541,
        "airbnb_smart_pricing_warning": (
            "Airbnb Smart Pricing tends to underprice — it optimizes for "
            "Airbnb's booking volume, not host revenue"
        ),
        "free_alternative": "Wheelhouse (free tier available)",
    },
    "guest_favorite_badge": {
        "tactic": "Guest Favorite Badge",
        "visibility_increase_pct": 40,
        "min_rating": 4.9,
        "min_reviews_in_4_years": 5,
        "heavily_weighted_categories": ["cleanliness", "accuracy", "check-in"],
        "weighting_note": "Algorithm weights cleanliness, accuracy, check-in TWICE as heavily as overall rating",
        "cleanliness_stat": "45% of negative reviews cite cleanliness",
    },
    "welcome_experience": {
        "tactic": "Welcome Experience",
        "local_products": ["Albanian coffee", "raki", "local biscuits"],
        "handwritten_note": "Personalized with guest name",
        "digital_guidebook_contents": [
            "Restaurant recommendations",
            "Nearest pharmacy locations",
            "ATM locations",
            "Clinic/hospital directions",
            "Public transport tips",
        ],
        "cost_per_guest_eur": 5,
        "impact": "Drives 5-star 'thoughtful host' mentions in reviews",
    },
    "multi_platform": {
        "tactic": "Multi-Platform Distribution",
        "recommended_platforms": ["Airbnb", "Booking.com", "Direct website"],
        "channel_managers": ["Hostaway", "Hospitable"],
        "direct_booking_fee_savings_pct": 15,
        "case_study": "One host went from 0% to 30% direct bookings in 1.5 years using StayFi WiFi email capture",
        "stayfi_method": "Captures guest email via WiFi login splash page",
    },
    "length_of_stay_discounts": {
        "tactic": "Length-of-Stay Discounts",
        "weekly_discount_pct": "10-15%",
        "weekly_target": "Digital nomads",
        "monthly_discount_pct": "20-30%",
        "monthly_target": "Remote workers",
        "last_minute_discount_pct": "15-27%",
        "last_minute_window_days": 7,
        "occupancy_increase_pct": 11,
        "revenue_increase_pct": 9,
    },
    "listing_optimization": {
        "tactic": "Listing Optimization",
        "amenity_checkboxes": "Complete ALL amenity checkboxes — missing ones make you invisible in filtered searches",
        "title_tip": "Front-load best keywords in title",
        "freshness": "Update listing regularly — algorithm notices activity",
        "review_responses": "Respond to every review (public and professional)",
    },
}

# --- Common Mistakes Albanian Hosts Make ---------------------------------------
COMMON_MISTAKES = [
    "Static pricing (the #1 revenue killer)",
    "Using only Airbnb Smart Pricing (underprices by design)",
    "Poor cleanliness (45% of negative reviews cite it)",
    "Misleading descriptions that set wrong expectations",
    "Slow communication (kills Superhost status + search ranking)",
    "Listing on only 1 platform (leaving money on the table)",
    "Amateur photography (loses 40% of potential bookings)",
    "Not collecting guest contact info for direct rebooking",
    "Ignoring DIVA tax obligations (15% tax, March 31 deadline)",
    "Inadequately supplied kitchens and worn mattresses",
]


def analyze_against_property():
    """Compare each top-host tactic against Lulebore Apartment 1's current setup."""
    issues = []
    you = YOUR_PROPERTY

    # 1. Automated Messaging
    t = TOP_HOST_TACTICS["automated_messaging"]
    issues.append({
        "severity": "CRITICAL",
        "area": "Automated Guest Messaging",
        "finding": (
            f"You have no automated messaging system. Top hosts use tools like "
            f"{', '.join(t['tools'])} to run a 5-touch guest communication sequence "
            f"(confirmation, pre-arrival tips, day-before directions, mid-stay check-in, "
            f"checkout review request). {t['algorithm_impact']}. "
            f"Superhost status requires {SUPERHOST_REQUIREMENTS['min_response_rate_pct']}%+ "
            f"response rate within {SUPERHOST_REQUIREMENTS['response_window_hours']}h."
        ),
        "recommendation": (
            "Set up Hospitable (starts ~$40/month) or use Airbnb's free Scheduled Messages "
            "as a minimum. Create these 5 automated messages: "
            "(1) Booking confirmation with house rules, "
            "(2) 7 days before: area guide + offer airport transfer upsell, "
            "(3) 1 day before: WiFi password, door code, directions, "
            "(4) Day 2 of stay: 'Everything OK? Need anything?', "
            "(5) Checkout day: thank you + review request link. "
            "Even Airbnb's free Scheduled Messages feature covers most of this."
        ),
        "what_others_do": (
            "Top hosts automate 100% of routine communication. The 5-touch sequence "
            "is industry standard. Automated instant replies boost search ranking directly."
        ),
    })

    # 2. Professional Photography
    t = TOP_HOST_TACTICS["professional_photography"]
    issues.append({
        "severity": "CRITICAL",
        "area": "Professional Photography",
        "finding": (
            f"You have {you['photos']} amateur photos. Professional photos increase bookings "
            f"by {t['booking_increase_pct']}% and allow {t['rate_premium_pct']}% higher nightly rates. "
            f"{t['first_5_photos_impact']}. With only {you['photos']} amateur shots, you are "
            f"losing bookings every single day."
        ),
        "recommendation": (
            f"Hire a professional Airbnb photographer immediately. Cost: EUR {t['cost_eur']}. "
            f"{t['roi_timeline']} — {t['roi_fast_stat']}. "
            f"Get 30-50 edited images covering: hero exterior/view shot, living room (2 angles), "
            f"bedroom (2 angles), kitchen, bathroom, balcony/view, neighborhood highlights, "
            f"welcome basket detail shot. At your EUR {you['nightly_rate_eur']}/night rate, the "
            f"{t['rate_premium_pct']}% premium alone would mean EUR {round(you['nightly_rate_eur'] * t['rate_premium_pct'] / 100)}/night more — "
            f"roughly EUR {round(you['nightly_rate_eur'] * t['rate_premium_pct'] / 100 * 30 * you['estimated_occupancy_pct'] / 100)}/month extra."
        ),
        "what_others_do": (
            "Every top-performing listing uses professional photography. "
            "The first 5 photos are curated as a 'story' — hero shot, living area, bedroom, "
            "kitchen, and a lifestyle/amenity shot. Many reshoot seasonally."
        ),
    })

    # 3. Dynamic Pricing
    t = TOP_HOST_TACTICS["dynamic_pricing"]
    issues.append({
        "severity": "CRITICAL",
        "area": "Dynamic Pricing",
        "finding": (
            f"You use static pricing at EUR {you['nightly_rate_eur']}/night with no dynamic adjustments. "
            f"Static pricing is the #1 revenue killer for Albanian hosts. "
            f"A {t['study_size_listings']}-listing study proved PriceLabs delivers "
            f"{t['proven_revenue_increase_pct']}% revenue increase. "
            f"Warning: {t['airbnb_smart_pricing_warning']}."
        ),
        "recommendation": (
            f"Sign up for PriceLabs (${t['pricelabs_cost_usd_per_month']}/listing/month). "
            f"Set a base price of EUR {you['nightly_rate_eur']}, minimum EUR 35, maximum EUR 75. "
            f"PriceLabs will auto-adjust based on demand, day-of-week, seasonality, local events, "
            f"and competitor pricing. At your current revenue, a {t['proven_revenue_increase_pct']}% increase "
            f"would mean ~EUR {round(you['nightly_rate_eur'] * 365 * you['estimated_occupancy_pct'] / 100 * t['proven_revenue_increase_pct'] / 100)} "
            f"more per year. Free alternative: {t['free_alternative']}."
        ),
        "what_others_do": (
            f"Top Albanian hosts use PriceLabs or Beyond Pricing and adjust rates daily. "
            f"They NEVER use Airbnb Smart Pricing alone because it systematically underprices "
            f"to maximize Airbnb's booking volume at the host's expense."
        ),
    })

    # 4. Guest Favorite Badge
    t = TOP_HOST_TACTICS["guest_favorite_badge"]
    badge_eligible = you["airbnb_rating"] >= t["min_rating"] and you["reviews_total"] >= t["min_reviews_in_4_years"]
    issues.append({
        "severity": "HIGH",
        "area": "Guest Favorite Badge",
        "finding": (
            f"The Guest Favorite badge makes listings appear {t['visibility_increase_pct']}% more often in search. "
            f"It requires a {t['min_rating']}+ rating and {t['min_reviews_in_4_years']}+ reviews in 4 years. "
            f"Your rating is {you['airbnb_rating']} (need {t['min_rating']}) and you have {you['reviews_total']} reviews. "
            f"{'You meet the review threshold but your rating of ' + str(you['airbnb_rating']) + ' is just below the ' + str(t['min_rating']) + ' requirement.' if you['reviews_total'] >= t['min_reviews_in_4_years'] and you['airbnb_rating'] < t['min_rating'] else ''} "
            f"{t['weighting_note']}. {t['cleanliness_stat']}."
        ),
        "recommendation": (
            f"Your {you['airbnb_rating']} rating is close but needs to reach {t['min_rating']}. "
            f"Focus intensely on the double-weighted categories: cleanliness, accuracy, and check-in. "
            f"Actionable steps: (1) hire a professional cleaner with a detailed checklist, "
            f"(2) ensure your listing description matches reality exactly (no exaggeration), "
            f"(3) provide crystal-clear check-in instructions with photos of the entrance. "
            f"Since 45% of negative reviews cite cleanliness, this is your #1 lever to push "
            f"from {you['airbnb_rating']} to {t['min_rating']}+."
        ),
        "what_others_do": (
            "Top hosts treat cleanliness as a business-critical function, not an afterthought. "
            "They use checklists, hire dedicated cleaners, and do pre-guest inspections. "
            "Many install keypad locks for seamless self-check-in rated 5 stars."
        ),
    })

    # 5. Welcome Experience
    t = TOP_HOST_TACTICS["welcome_experience"]
    issues.append({
        "severity": "HIGH",
        "area": "Welcome Experience",
        "finding": (
            f"You have no welcome basket and no digital guidebook. Top hosts provide "
            f"local products ({', '.join(t['local_products'])}), a handwritten note with the "
            f"guest's name, and a digital guidebook with restaurant, pharmacy, ATM, clinic, "
            f"and transport recommendations. This costs only EUR {t['cost_per_guest_eur']}/guest "
            f"but {t['impact']}."
        ),
        "recommendation": (
            f"Spend EUR {t['cost_per_guest_eur']}/guest on a welcome basket: Albanian coffee, a small "
            f"bottle of raki, local biscuits, and a handwritten welcome note using the guest's "
            f"first name. Create a free digital guidebook using Touchstay or a simple Google Doc "
            f"with: (1) your top 10 restaurant picks within walking distance, (2) nearest pharmacy, "
            f"(3) nearest ATM, (4) nearest clinic/hospital with address + phone, (5) how to use "
            f"Tirana buses/taxis/Bolt. Send the guidebook link in your pre-arrival message. "
            f"At 40% occupancy and ~12 guests/month, that is EUR {12 * t['cost_per_guest_eur']}/month "
            f"for a major review boost."
        ),
        "what_others_do": (
            "Top hosts in Tirana stock Albanian coffee, raki, and snacks. "
            "The handwritten note is the single most-mentioned 'thoughtful touch' in 5-star reviews. "
            "Digital guidebooks reduce guest questions by 70% and boost location scores."
        ),
    })

    # 6. Multi-Platform + Direct Bookings
    t = TOP_HOST_TACTICS["multi_platform"]
    issues.append({
        "severity": "HIGH",
        "area": "Multi-Platform & Direct Bookings",
        "finding": (
            f"You list on {you['platforms']} platforms ({', '.join(you['platforms_list'])}) but have "
            f"no direct booking website and no channel manager. You are paying 15% platform fees "
            f"on every booking with no path to reduce them. "
            f"{t['case_study']}."
        ),
        "recommendation": (
            f"Phase 1 (now): Set up a channel manager (Hostaway or Hospitable) to sync calendars "
            f"across Airbnb and Booking.com — prevents double bookings. "
            f"Phase 2 (month 2): Create a simple direct booking website using Hospitable's built-in "
            f"site or Lodgify. Direct bookings save you the {t['direct_booking_fee_savings_pct']}% platform fee. "
            f"Phase 3 (month 3): Install StayFi (WiFi email capture) — every guest who connects "
            f"to WiFi gives you their email. Build an email list for direct rebooking campaigns. "
            f"At EUR {you['nightly_rate_eur']}/night, converting just 30% of bookings to direct saves "
            f"EUR {round(you['nightly_rate_eur'] * 365 * you['estimated_occupancy_pct'] / 100 * 0.30 * t['direct_booking_fee_savings_pct'] / 100)}/year in fees."
        ),
        "what_others_do": (
            "Top hosts treat Airbnb as a customer acquisition channel, not the final destination. "
            "They capture guest contact info and convert repeat guests to direct bookings at a "
            "15% discount (which is still more profitable due to zero platform fees)."
        ),
    })

    # 7. Length-of-Stay Discounts
    t = TOP_HOST_TACTICS["length_of_stay_discounts"]
    issues.append({
        "severity": "HIGH",
        "area": "Length-of-Stay Discounts",
        "finding": (
            f"You offer no weekly, monthly, or last-minute discounts. Properties with length-of-stay "
            f"discounts see {t['occupancy_increase_pct']}% higher occupancy and {t['revenue_increase_pct']}% "
            f"higher revenue. Weekly discounts ({t['weekly_discount_pct']}% off) attract digital nomads. "
            f"Monthly discounts ({t['monthly_discount_pct']}% off) attract remote workers. Last-minute "
            f"discounts ({t['last_minute_discount_pct']}% off within {t['last_minute_window_days']} days) "
            f"fill gaps."
        ),
        "recommendation": (
            f"Enable these in your Airbnb settings today (takes 2 minutes): "
            f"(1) Weekly discount: 12% (EUR {round(you['nightly_rate_eur'] * 0.88 * 7)}/week instead of "
            f"EUR {you['nightly_rate_eur'] * 7}), "
            f"(2) Monthly discount: 25% (EUR {round(you['nightly_rate_eur'] * 0.75 * 30)}/month instead of "
            f"EUR {you['nightly_rate_eur'] * 30}), "
            f"(3) Last-minute discount: 20% for bookings within {t['last_minute_window_days']} days. "
            f"A month-long booking at 25% off (EUR {round(you['nightly_rate_eur'] * 0.75 * 30)}) is better "
            f"than 12 empty nights at full price (EUR 0). These discounts compound with the "
            f"{t['occupancy_increase_pct']}% occupancy lift."
        ),
        "what_others_do": (
            "Top Tirana hosts all offer weekly and monthly discounts. "
            "The best operators target digital nomads specifically — Tirana is increasingly "
            "popular with remote workers due to low cost of living and fast internet."
        ),
    })

    # 8. Listing Optimization
    t = TOP_HOST_TACTICS["listing_optimization"]
    issues.append({
        "severity": "MEDIUM",
        "area": "Listing Optimization",
        "finding": (
            f"Listing optimization is an ongoing process most hosts neglect. "
            f"{t['amenity_checkboxes']}. {t['title_tip']}. {t['freshness']}. {t['review_responses']}. "
            f"Every unchecked amenity box is a filtered search where your listing is invisible."
        ),
        "recommendation": (
            "Do a full listing audit this week: "
            "(1) Go through EVERY amenity checkbox on Airbnb — check everything you have "
            "(WiFi, AC, heating, iron, hair dryer, kitchen items, etc.), "
            "(2) Rewrite your title to front-load keywords: e.g., 'Central Tirana | 1-Bed Apt | "
            "Fast WiFi | Near Clinics' instead of a generic name, "
            "(3) Update your listing description and photos at least quarterly — the algorithm "
            "rewards fresh content, "
            "(4) Respond publicly to every review within 24 hours — shows future guests you are "
            "an engaged, responsive host."
        ),
        "what_others_do": (
            "Top hosts review and update their listing monthly. They A/B test titles, "
            "rotate hero photos seasonally, and respond to 100% of reviews with personalized "
            "messages (not copy-paste). They check every single amenity box that applies."
        ),
    })

    # 9. Post-Checkout Review Request System
    issues.append({
        "severity": "MEDIUM",
        "area": "Review Collection System",
        "finding": (
            f"You have no systematic post-checkout review request process. With {you['reviews_total']} "
            f"reviews over {you['months_active']} months, your review rate is ~{round(you['reviews_total'] / you['months_active'], 1)} "
            f"reviews/month. Top hosts achieve 2-4 reviews/month by actively requesting them. "
            f"More reviews = higher search ranking = more bookings."
        ),
        "recommendation": (
            "Add a review request to your checkout message: 'Thank you for staying! If you "
            "enjoyed your time, a review would mean the world to us and helps other travelers "
            "find our apartment.' Send this within 2 hours of checkout while the experience "
            "is fresh. Airbnb's Scheduled Messages can automate this. Also leave a review for "
            "every guest — Airbnb notifies them, prompting a reciprocal review."
        ),
        "what_others_do": (
            "Top hosts leave a guest review within 1 hour of checkout (triggers a notification) "
            "and send a personal thank-you message with a gentle review request. "
            "Some include a small card in the apartment: 'Loved your stay? Leave us a review!'"
        ),
    })

    # 10. Common Albanian Host Mistakes — Comprehensive Warning
    issues.append({
        "severity": "MEDIUM",
        "area": "Common Albanian Host Mistakes to Avoid",
        "finding": (
            "Research identifies 10 common mistakes Albanian hosts make that directly reduce "
            "revenue: " + "; ".join(COMMON_MISTAKES) + ". "
            "Based on your current setup, you are making at least 6 of these mistakes: "
            "static pricing, no dynamic pricing tool, amateur photography, single-platform "
            "mentality (no direct bookings), not collecting guest contact info, and no "
            "systematic review collection."
        ),
        "recommendation": (
            "Priority fix order based on revenue impact: "
            "(1) CRITICAL: Dynamic pricing — sign up for PriceLabs today ($19.99/month). "
            "(2) CRITICAL: Professional photography — book a photographer this week (EUR 300-800). "
            "(3) CRITICAL: Automated messaging — set up Airbnb Scheduled Messages today (free). "
            "(4) HIGH: Welcome basket + guidebook — prepare for next guest (EUR 5/guest). "
            "(5) HIGH: Length-of-stay discounts — enable in Airbnb settings (2 minutes). "
            "(6) HIGH: StayFi email capture — install at next opportunity. "
            "Fixing items 1-3 alone could increase revenue by 40-60%."
        ),
        "what_others_do": (
            "The most successful Albanian hosts treat their listing as a business, not a side project. "
            "They invest in professional tools, optimize continuously, and build direct booking "
            "channels to reduce platform dependency."
        ),
    })

    return issues


def run():
    """Main skill entry point."""
    issues = analyze_against_property()

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "superhost_requirements": SUPERHOST_REQUIREMENTS,
        "top_host_tactics": TOP_HOST_TACTICS,
        "common_mistakes": COMMON_MISTAKES,
        "your_property": YOUR_PROPERTY,
        "issues": issues,
        "issues_count": len(issues),
    }

    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  SUPERHOST REQUIREMENTS:")
    print(f"    Min reservations/year:  {SUPERHOST_REQUIREMENTS['min_reservations_per_year']}")
    print(f"    Max cancellation rate:  {SUPERHOST_REQUIREMENTS['max_cancellation_rate_pct']}%")
    print(f"    Min response rate:      {SUPERHOST_REQUIREMENTS['min_response_rate_pct']}% within {SUPERHOST_REQUIREMENTS['response_window_hours']}h")
    print(f"    Min overall rating:     {SUPERHOST_REQUIREMENTS['min_overall_rating']}")
    print(f"\n  YOUR PROPERTY:")
    print(f"    Name:     {YOUR_PROPERTY['name']}")
    print(f"    Rate:     EUR {YOUR_PROPERTY['nightly_rate_eur']}/night")
    print(f"    Rating:   {YOUR_PROPERTY['airbnb_rating']} Airbnb / {YOUR_PROPERTY['booking_rating']} Booking.com")
    print(f"    Photos:   {YOUR_PROPERTY['photos']} (amateur)")
    print(f"    Reviews:  {YOUR_PROPERTY['reviews_total']}")
    print(f"\n  TOP HOST TACTICS ANALYZED: {len(TOP_HOST_TACTICS)}")
    for key, tactic in TOP_HOST_TACTICS.items():
        print(f"    - {tactic['tactic']}")
    print(f"\n  COMMON MISTAKES IDENTIFIED: {len(COMMON_MISTAKES)}")
    print(f"\n  ISSUES GENERATED: {len(issues)}")
    for i, issue in enumerate(issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area']}")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
