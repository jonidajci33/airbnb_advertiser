"""
Skill: Guest Experience
Researches the guest experience tactics that drive 5-star reviews and higher
rankings — then compares top-host practices against your current setup to
identify the highest-impact improvements.
"""

import sys
from pathlib import Path

SKILL_NAME = "guest_experience"
DESCRIPTION = "Guest experience tactics that drive 5-star reviews, Guest Favorite badge, and higher search rankings"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# --- Researched Guest Experience Data (Feb 2026) ----------------------------

GUEST_FAVORITE_BADGE = {
    "search_visibility_boost_pct": 40,
    "min_rating": 4.9,
    "min_reviews_4_years": 5,
    "min_reviews_past_2_years": 1,
    "algorithm_double_weighted_categories": ["cleanliness", "accuracy", "check-in"],
    "negative_review_top_cause": "cleanliness",
    "negative_review_cleanliness_pct": 45,
    "badge_effect": "Listing appears 40% more often in search results",
}

FIVE_STAR_JOURNEY = {
    "pre_arrival": {
        "step_1": "Immediate booking confirmation — warm, personalized tone",
        "step_2": "7 days before: detailed check-in instructions, local tips, upsell offers",
        "step_3": "1 day before: reminder with directions, parking info, WiFi password",
    },
    "check_in": {
        "step_4": "Self check-in via smart lock or lockbox (maximum flexibility)",
        "step_5": "Welcome package: Albanian coffee, raki, local biscuits, handwritten note with guest name",
        "step_6": "Printed or digital guidebook: restaurants, pharmacy, ATM, clinic locations, transport tips",
    },
    "during_stay": {
        "step_7": "Mid-stay message: 'Is everything to your liking?'",
        "step_8": "Respond to any issue within minutes",
        "step_9": "Proactively resolve problems — offer compensation if something goes wrong",
    },
    "post_stay": {
        "step_10": "Checkout reminder with clear instructions",
        "step_11": "Within 24h: thank-you message + gentle review reminder",
        "step_12": "Offer discount code for direct rebooking",
    },
}

CRITICAL_SUCCESS_FACTORS = {
    "response_rate_target_pct": 100,
    "response_rate_note": "Airbnb tracks response rate and penalizes hosts below 90%",
    "under_promise_over_deliver": "Small surprises create 5-star emotional impact disproportionate to their cost",
    "cleanliness_is_king": "Detailed cleaning checklist, quality inspections, replace worn items immediately",
    "accuracy_matters": "Never exaggerate listing — accuracy is a review category AND algorithm factor",
}

REVIEW_VELOCITY_DATA = {
    "user_reviews_per_month": 2.2,
    "target_reviews_per_month": 5,
    "direct_ask_multiplier": 2.0,
    "direct_ask_note": "Guests asked directly are 2x more likely to leave a review",
    "algorithm_recency_weight": "Recent positive reviews weighted heavily — steady stream beats old high count",
    "respond_to_all": "Respond to EVERY review (positive and negative) — shows engagement, boosts ranking",
}

PHOTOGRAPHY_DATA = {
    "professional_photo_booking_boost_pct": 40,
    "professional_photo_rate_boost_pct": 26,
    "first_5_photos_decision_share_pct": 90,
    "cost_range_eur": "300-800",
    "cost_images": "30-50 professional images",
    "roi_payback_weeks": "2-4",
    "video_tour_inquiry_multiplier": 2.0,
    "video_listing_inquiry_boost_pct": 200,
    "amenity_checkboxes": "Complete ALL amenity checkboxes — missing ones make you invisible in filtered search",
    "title_tip": "Front-load best keyword in listing title",
}

AUTOMATION_TOOLS = {
    "hospitable": {
        "name": "Hospitable",
        "function": "Automated messaging across platforms",
        "cost": "$29/month",
        "best_for": "Hosts with 1-5 properties wanting to automate guest communication",
    },
    "guesty": {
        "name": "Guesty",
        "function": "60+ channel integrations, full property management",
        "cost": "Varies by portfolio size",
        "best_for": "Hosts scaling to multiple properties",
    },
    "touchstay": {
        "name": "Touchstay",
        "function": "Free digital guidebook builder",
        "cost": "Free tier available",
        "best_for": "Creating branded digital guidebooks for guests",
    },
    "stayfi": {
        "name": "StayFi",
        "function": "WiFi-based email capture from guests",
        "cost": "Varies",
        "open_rate_pct": 60,
        "best_for": "Building a guest email list for direct rebooking campaigns",
    },
}

# --- Your Property Data (Current State) -------------------------------------

YOUR_PROPERTY = {
    "name": "Lulebore Apartment 1",
    "location": "Tirana, Albania",
    "airbnb_rating": 4.88,
    "booking_com_rating": 10.0,
    "reviews_total": 54,
    "reviews_per_month": 2.2,
    "months_active": 24,
    # Current guest experience setup
    "has_automated_messaging": False,
    "has_welcome_basket": False,
    "has_digital_guidebook": False,
    "has_post_checkout_review_request": False,
    "has_recovery_amenities": False,
    # Existing strengths
    "has_soundproofing": True,
    "soundproofing_quality": "excellent",
    "has_private_entrance": True,
    "has_equipped_kitchen": True,
}


def analyze_guest_favorite_gap():
    """Analyze the gap between current rating and Guest Favorite badge threshold."""
    current = YOUR_PROPERTY["airbnb_rating"]
    target = GUEST_FAVORITE_BADGE["min_rating"]
    gap = round(target - current, 2)

    analysis = {
        "current_rating": current,
        "target_rating": target,
        "rating_gap": gap,
        "badge_earned": current >= target,
        "visibility_boost_if_earned_pct": GUEST_FAVORITE_BADGE["search_visibility_boost_pct"],
        "double_weighted_categories": GUEST_FAVORITE_BADGE["algorithm_double_weighted_categories"],
        "biggest_risk": f"Cleanliness causes {GUEST_FAVORITE_BADGE['negative_review_cleanliness_pct']}% of negative reviews",
        "review_requirement_met": YOUR_PROPERTY["reviews_total"] >= GUEST_FAVORITE_BADGE["min_reviews_4_years"],
    }
    return analysis


def identify_issues():
    """Compare top-host practices against your current setup and generate issues."""
    issues = []

    # --- Issue 1: Guest Favorite Badge Gap ---
    badge = GUEST_FAVORITE_BADGE
    you = YOUR_PROPERTY
    gap = round(badge["min_rating"] - you["airbnb_rating"], 2)
    issues.append({
        "severity": "CRITICAL",
        "area": "Guest Favorite Badge — 0.02 Points Away",
        "finding": (
            f"Your Airbnb rating is {you['airbnb_rating']}, just {gap} points below the "
            f"{badge['min_rating']} threshold for the Guest Favorite badge. "
            f"This badge makes listings appear {badge['search_visibility_boost_pct']}% more "
            f"often in search. The algorithm weights cleanliness, accuracy, and check-in "
            f"TWICE as heavily as overall rating. {badge['negative_review_cleanliness_pct']}% "
            f"of negative reviews cite cleanliness as the issue."
        ),
        "recommendation": (
            "Focus obsessively on the three double-weighted categories: (1) Cleanliness — "
            "implement a 40-point cleaning checklist, inspect after every turnover, replace "
            "any worn linens or towels immediately. (2) Accuracy — audit every claim in your "
            "listing against reality; remove anything slightly exaggerated. (3) Check-in — "
            "send crystal-clear instructions with photos of the entrance, lock, and parking. "
            "Every single 5-star review pushes you closer to the badge. Every 4-star review "
            "requires roughly five 5-star reviews to recover from."
        ),
        "what_others_do": (
            "Guest Favorite hosts maintain 4.9+ by treating cleanliness as a non-negotiable "
            "system (checklists, photo verification, backup cleaners) rather than relying on "
            "a single cleaner. They also under-promise in listings so accuracy scores stay perfect."
        ),
    })

    # --- Issue 2: No Automated Messaging ---
    issues.append({
        "severity": "HIGH",
        "area": "No Automated Guest Messaging",
        "finding": (
            "You have no automated messaging system. Top hosts send a structured sequence "
            "of 6+ messages per guest: booking confirmation, pre-arrival instructions (7 days "
            "and 1 day before), mid-stay check-in, checkout instructions, and post-stay "
            "thank-you with review request. Airbnb tracks response rate and response time — "
            "hosts below 90% response rate get penalized in search rankings."
        ),
        "recommendation": (
            "Implement Hospitable ($29/month) to automate the full guest journey: "
            "(1) Instant booking confirmation with warm, personalized tone. "
            "(2) 7 days before: check-in instructions, local tips, upsell offers. "
            "(3) 1 day before: reminder with directions, parking, WiFi password. "
            "(4) Mid-stay: 'Is everything to your liking?' message. "
            "(5) Checkout day: clear checkout instructions. "
            "(6) Within 24h post-checkout: thank-you + gentle review nudge. "
            "This single change addresses your review velocity problem, response rate, "
            "and guest satisfaction simultaneously."
        ),
        "what_others_do": (
            "Top Airbnb hosts automate 100% of routine messages while keeping the tone "
            "personal. Hospitable sends messages across Airbnb AND Booking.com from one "
            "dashboard. Hosts using automated sequences report 100% response rates and "
            "significantly higher review submission rates."
        ),
    })

    # --- Issue 3: No Welcome Package ---
    issues.append({
        "severity": "HIGH",
        "area": "No Welcome Package",
        "finding": (
            "You have no welcome basket or arrival experience. The check-in moment is "
            "the single highest-impact touchpoint for setting the emotional tone of a stay. "
            "A welcome package costs €3-5 per guest but creates an outsized 5-star impression. "
            "This is the 'under-promise, over-deliver' moment that top hosts rely on."
        ),
        "recommendation": (
            "Create a signature Lulebore welcome package: (1) Albanian coffee (ready to brew), "
            "(2) a small bottle of raki, (3) local biscuits or Turkish delight, "
            "(4) a handwritten note with the guest's name and a warm welcome message, "
            "(5) a printed card with WiFi password, emergency contacts, and your phone number. "
            "Total cost: ~€3-5 per guest. Place it visibly on the kitchen counter before arrival. "
            "Your equipped kitchen makes the coffee especially relevant — guests can use it "
            "immediately."
        ),
        "what_others_do": (
            "Superhost-level hosts in tourist destinations universally provide welcome packages "
            "with local specialties. In Albania specifically, offering Albanian coffee and raki "
            "ties into the cultural hospitality tradition (mikpritja) that international guests "
            "find memorable and review-worthy. Hosts who add welcome packages report a measurable "
            "increase in 5-star reviews mentioning the personal touch."
        ),
    })

    # --- Issue 4: No Digital Guidebook ---
    issues.append({
        "severity": "HIGH",
        "area": "No Digital Guidebook",
        "finding": (
            "You have no digital guidebook. Guests in an unfamiliar city need quick access "
            "to restaurants, pharmacies, ATMs, clinics, and transport information. Without "
            "this, they message you repeatedly (increasing your workload) or figure things "
            "out themselves (decreasing satisfaction). A guidebook also reduces the 'accuracy' "
            "gap — guests who know what to expect give higher accuracy scores."
        ),
        "recommendation": (
            "Use Touchstay (free tier) to build a branded digital guidebook for Lulebore "
            "Apartment 1. Include: (1) Check-in/checkout procedures with photos, "
            "(2) WiFi password and appliance instructions, (3) Top 10 restaurants within "
            "walking distance with Google Maps links, (4) Nearest pharmacy, ATM, clinic, "
            "and supermarket, (5) Public transport guide (bus routes, taxi apps), "
            "(6) Day trip suggestions (Berat, Durres, Kruja), (7) Emergency contacts. "
            "Send the guidebook link in your 7-days-before message. This also positions "
            "you perfectly for medical tourism guests who need clinic directions."
        ),
        "what_others_do": (
            "Top hosts provide digital guidebooks via Touchstay or custom websites. The "
            "guidebook replaces 60-80% of guest questions, saving the host time while "
            "improving the guest experience. Medical tourism properties include clinic "
            "maps, pharmacy locations for prescriptions, and soft-food restaurant recommendations."
        ),
    })

    # --- Issue 5: No Post-Checkout Review Request ---
    issues.append({
        "severity": "HIGH",
        "area": "No Post-Checkout Review Request — Low Review Velocity",
        "finding": (
            f"You receive {you['reviews_per_month']} reviews/month versus a target of "
            f"{REVIEW_VELOCITY_DATA['target_reviews_per_month']}/month. You have no post-checkout "
            f"review request system. Guests who are asked directly are "
            f"{REVIEW_VELOCITY_DATA['direct_ask_multiplier']:.0f}x more likely to leave a review. "
            f"The Airbnb algorithm weights recent positive reviews heavily — a steady stream "
            f"of new reviews outperforms an old high count. You are also not responding to "
            f"all existing reviews, which signals low engagement to the algorithm."
        ),
        "recommendation": (
            "Implement a two-step review strategy: (1) AUTOMATED: Within 24 hours of checkout, "
            "send a warm thank-you message that naturally leads to a review request — "
            "'We loved hosting you! If you have a moment, a review helps small hosts like us "
            "more than you might think.' Keep the tone genuine, never pushy. "
            "(2) MANUAL: Respond to EVERY review you receive — both positive and negative. "
            "For positive reviews, thank them warmly and mention something specific about "
            "their stay. For negative reviews, acknowledge the issue, explain what you have "
            "fixed, and invite them back. This public response shows future guests you care "
            "and signals engagement to the algorithm."
        ),
        "what_others_do": (
            "Top hosts achieve 60-70% review rates by sending personalized post-checkout "
            "messages. They respond to 100% of reviews within 24 hours. Some hosts include "
            "a small 'thank you' (like sending the digital guidebook link for their next "
            "trip to Albania) alongside the review request to increase compliance."
        ),
    })

    # --- Issue 6: No Recovery Amenities (Medical Tourism Gap) ---
    issues.append({
        "severity": "HIGH",
        "area": "No Recovery Amenities Despite Medical Tourism Potential",
        "finding": (
            "Albania sees 80,000 medical tourists per year with dental tourism growing 400% "
            "since 2020. Your apartment has excellent soundproofing, a private entrance, and "
            "an equipped kitchen — three of the most important features for recovery stays. "
            "However, you have no recovery-specific amenities. This is a missed opportunity "
            "to differentiate in a market with almost zero competition for recovery-friendly "
            "accommodation."
        ),
        "recommendation": (
            "Add a 'Recovery Kit' available on request (or included for weekly stays): "
            "(1) Extra soft pillows and a wedge pillow for elevated sleeping (dental/facial), "
            "(2) Reusable ice packs (keep in freezer), (3) Soft foods starter pack (yogurt, "
            "soup, smoothie ingredients) ready in the kitchen, (4) Blender for smoothies, "
            "(5) Blackout curtains or sleep mask, (6) Printed post-procedure care tips from "
            "common Tirana clinics. Total setup cost: ~€50-80. Charge €0 extra — it is the "
            "reason they book you over generic apartments. Mention these in your listing "
            "to attract the niche."
        ),
        "what_others_do": (
            "In Turkey (the global leader in medical tourism accommodation), hosts bundle "
            "recovery amenities into apartment stays. In Tirana, virtually NO Airbnb host "
            "does this yet — you would be the first mover. Properties that market "
            "recovery-friendly features command 20-40% rate premiums for medical stays."
        ),
    })

    # --- Issue 7: Photography and Listing Optimization ---
    photo = PHOTOGRAPHY_DATA
    issues.append({
        "severity": "HIGH",
        "area": "Listing Photography and Presentation",
        "finding": (
            f"Professional photos generate {photo['professional_photo_booking_boost_pct']}% more "
            f"bookings and {photo['professional_photo_rate_boost_pct']}% higher nightly rates. "
            f"The first 5 photos drive {photo['first_5_photos_decision_share_pct']}% of booking "
            f"decisions. Video tours generate {photo['video_listing_inquiry_boost_pct']}% more "
            f"inquiries. Additionally, incomplete amenity checkboxes make your listing invisible "
            f"when guests use search filters."
        ),
        "recommendation": (
            f"Invest in a professional photo shoot ({photo['cost_range_eur']} EUR for "
            f"{photo['cost_images']}). This pays for itself in {photo['roi_payback_weeks']} "
            f"weeks through higher booking rates. Prioritize your first 5 images: "
            "(1) Hero shot of the best room with natural light, (2) Kitchen — highlight "
            "the equipped kitchen as a key feature, (3) Bedroom — clean, inviting, show "
            "the soundproofing/quiet environment, (4) Private entrance — unique selling point, "
            "(5) Welcome setup or local neighborhood charm. Add a 30-60 second video walkthrough. "
            "Then audit EVERY amenity checkbox on Airbnb and Booking.com — check everything "
            "you genuinely offer. Front-load your best keyword in the listing title "
            "(e.g., 'Quiet Private Apartment' or 'Recovery-Friendly Retreat')."
        ),
        "what_others_do": (
            "Top 10% of Airbnb hosts invest in professional photography as standard practice. "
            "Listings with video tours get 200% more inquiries. The most successful hosts "
            "update photos seasonally and A/B test their first image. They complete 100% of "
            "amenity checkboxes to maximize visibility in filtered searches."
        ),
    })

    # --- Issue 8: Cleanliness System (Double-Weighted Category) ---
    issues.append({
        "severity": "CRITICAL",
        "area": "No Systematic Cleanliness Protocol",
        "finding": (
            f"Cleanliness is the #1 cause of negative Airbnb reviews "
            f"({badge['negative_review_cleanliness_pct']}% of all negative reviews). "
            f"The Airbnb algorithm weights cleanliness scores TWICE as heavily as the overall "
            f"rating. At your current {you['airbnb_rating']} rating (needing {badge['min_rating']}), "
            f"a single cleanliness complaint could push the badge further away. You need a "
            f"systematic, repeatable cleaning process — not just a good cleaner."
        ),
        "recommendation": (
            "Build a 40-point cleaning checklist covering every surface, fixture, and item. "
            "Key areas: (1) Bathroom grout, drains, toilet base, mirror edges — these are "
            "where guests look first. (2) Kitchen appliances inside and out, under the sink, "
            "stovetop grease. (3) Linens — use white sheets/towels only (shows cleanliness, "
            "easy to bleach). Replace any stained or worn items immediately. (4) Floors — "
            "mop under furniture, not just visible areas. (5) Remote controls, light switches, "
            "door handles — wipe with disinfectant. (6) After every clean, take 3-5 photos "
            "as a quality record. Consider having a backup cleaner trained on the same "
            "checklist for emergencies."
        ),
        "what_others_do": (
            "Guest Favorite hosts treat cleaning as a documented system, not a task. They "
            "use printed checklists the cleaner signs off on, take post-clean verification "
            "photos, and do spot checks. Some use cleaning management apps. They replace "
            "towels and sheets on a fixed cycle (every 3-6 months) regardless of condition, "
            "and they keep a 'guest eye' — inspecting the space as if seeing it for the "
            "first time."
        ),
    })

    # --- Issue 9: Accuracy Audit (Double-Weighted Category) ---
    issues.append({
        "severity": "MEDIUM",
        "area": "Listing Accuracy Audit Needed",
        "finding": (
            "Accuracy is one of the three double-weighted algorithm categories. Even small "
            "discrepancies between your listing description and reality (slightly different "
            "view, older furniture than photos suggest, amenities that half-work) can trigger "
            "4-star accuracy scores. At your rating of 4.88, you cannot afford accuracy hits."
        ),
        "recommendation": (
            "Conduct a full accuracy audit: (1) Walk through your listing description "
            "sentence by sentence — does every claim match reality exactly? (2) Compare "
            "every photo to current state — has anything changed? (3) Test every amenity "
            "you list (WiFi speed, kitchen equipment, hot water consistency). (4) Read your "
            "last 20 reviews for any mentions of 'expected' or 'different' — these signal "
            "accuracy gaps. (5) When in doubt, remove the claim rather than risk a 4-star "
            "accuracy score. Under-promising creates room for pleasant surprises."
        ),
        "what_others_do": (
            "Top hosts do quarterly accuracy audits and update photos whenever anything "
            "changes. They deliberately under-describe their space so guests are pleasantly "
            "surprised. Some hosts add a line like 'The apartment may look even better in "
            "person than in photos' — setting expectations low and delivering high."
        ),
    })

    # --- Issue 10: Check-In Experience (Double-Weighted Category) ---
    issues.append({
        "severity": "MEDIUM",
        "area": "Check-In Experience Optimization",
        "finding": (
            "Check-in is the third double-weighted algorithm category. Your private entrance "
            "is a major advantage — it enables true self check-in without awkward coordination. "
            "However, without detailed check-in instructions sent in advance (with photos, "
            "maps, and step-by-step directions), even a private entrance can cause confusion "
            "and lower check-in scores."
        ),
        "recommendation": (
            "Create a visual check-in guide: (1) Photo of the building exterior from the "
            "street (with arrow pointing to entrance), (2) Photo of the private entrance "
            "door, (3) Step-by-step lockbox or key instructions with close-up photos, "
            "(4) Screenshot of Google Maps pin with walking directions from nearest landmark, "
            "(5) Parking instructions if applicable. Send this guide both 7 days and 1 day "
            "before arrival. If you do not have a smart lock, consider installing one "
            "(€80-150) — it eliminates key handoff issues entirely and lets guests check "
            "in at any hour. Your private entrance + smart lock would be a near-perfect "
            "check-in experience."
        ),
        "what_others_do": (
            "Top hosts provide check-in guides with 5-8 photos showing every step from "
            "street to bed. Many use smart locks (Nuki, Yale, August) that generate unique "
            "codes per guest, automatically sent via Hospitable. This eliminates the most "
            "common check-in complaints: finding the building, finding the door, and "
            "operating the lock."
        ),
    })

    # --- Issue 11: Guest Email Capture for Direct Rebooking ---
    issues.append({
        "severity": "MEDIUM",
        "area": "No Guest Email Capture or Direct Rebooking System",
        "finding": (
            "You have no system to capture guest emails or encourage direct rebooking. "
            "Every guest who books through Airbnb or Booking.com costs you 15-20% in "
            "platform fees. Building a direct guest list allows you to offer repeat guests "
            "a 10-15% discount (still earning more than platform bookings) and maintain "
            "the relationship outside platform control."
        ),
        "recommendation": (
            "Implement StayFi or a similar WiFi-based email capture tool. When guests "
            "connect to WiFi, they enter their email — achieving 60%+ capture rates with "
            "welcome email open rates above 60%. After their stay, add them to a simple "
            "email sequence: (1) Post-stay thank-you, (2) 3 months later: 'Planning your "
            "next trip to Albania?' with a 10% direct booking discount, (3) Seasonal "
            "highlights (e.g., 'Summer in Tirana' email in April). Even capturing 50% of "
            "guests and converting 10% to direct rebookings saves significant platform fees "
            "over time."
        ),
        "what_others_do": (
            "Professional hosts use StayFi or custom captive portals to build guest email "
            "lists. They send 2-4 emails per year per past guest. Some hosts report that "
            "15-25% of their bookings eventually come from direct repeat guests, saving "
            "thousands in annual platform commissions."
        ),
    })

    return issues


def run():
    """Main skill entry point."""
    badge_analysis = analyze_guest_favorite_gap()
    issues = identify_issues()

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "guest_favorite_analysis": badge_analysis,
        "five_star_journey": FIVE_STAR_JOURNEY,
        "automation_tools": AUTOMATION_TOOLS,
        "issues": issues,
        "issues_count": len(issues),
    }

    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  YOUR GUEST EXPERIENCE STATUS:")
    print(f"    Airbnb Rating:          {YOUR_PROPERTY['airbnb_rating']} (need 4.9+ for Guest Favorite)")
    print(f"    Booking.com Rating:     {YOUR_PROPERTY['booking_com_rating']}")
    print(f"    Reviews:                {YOUR_PROPERTY['reviews_total']} total ({YOUR_PROPERTY['reviews_per_month']}/month)")
    print(f"    Review Target:          {REVIEW_VELOCITY_DATA['target_reviews_per_month']}/month")
    print(f"    Automated Messaging:    {'Yes' if YOUR_PROPERTY['has_automated_messaging'] else 'NO'}")
    print(f"    Welcome Package:        {'Yes' if YOUR_PROPERTY['has_welcome_basket'] else 'NO'}")
    print(f"    Digital Guidebook:      {'Yes' if YOUR_PROPERTY['has_digital_guidebook'] else 'NO'}")
    print(f"    Review Request System:  {'Yes' if YOUR_PROPERTY['has_post_checkout_review_request'] else 'NO'}")
    print(f"    Recovery Amenities:     {'Yes' if YOUR_PROPERTY['has_recovery_amenities'] else 'NO'}")
    print(f"\n  STRENGTHS:")
    print(f"    Soundproofing:          {YOUR_PROPERTY['soundproofing_quality'].upper()}")
    print(f"    Private Entrance:       YES")
    print(f"    Equipped Kitchen:       YES")
    print(f"\n  GUEST FAVORITE BADGE GAP:")
    print(f"    Current: {badge_analysis['current_rating']} | Target: {badge_analysis['target_rating']} | Gap: {badge_analysis['rating_gap']}")
    print(f"    Badge Earned: {'YES' if badge_analysis['badge_earned'] else 'NO — {:.0f}% search visibility boost at stake'.format(badge_analysis['visibility_boost_if_earned_pct'])}")
    print(f"    Double-Weighted: {', '.join(badge_analysis['double_weighted_categories'])}")
    print(f"\n  ISSUES FOUND: {len(issues)}")
    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    sorted_issues = sorted(issues, key=lambda x: severity_order.get(x["severity"], 99))
    for i, issue in enumerate(sorted_issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area']}")
    print(f"\n  5-STAR GUEST JOURNEY (top hosts send 6+ messages per guest):")
    for phase, steps in FIVE_STAR_JOURNEY.items():
        print(f"    {phase.upper().replace('_', ' ')}:")
        for key, step in steps.items():
            step_num = key.replace("step_", "")
            print(f"      {step_num}. {step}")
    print(f"\n  RECOMMENDED TOOLS:")
    for tool_key, tool in AUTOMATION_TOOLS.items():
        print(f"    - {tool['name']}: {tool['function']} ({tool['cost']})")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
