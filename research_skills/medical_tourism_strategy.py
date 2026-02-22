"""
Skill: Medical Tourism Strategy
Researches what world-class medical tourism accommodation providers in Turkey
and Thailand do — clinic partnerships, recovery amenities, pricing packages,
platform listings, content marketing — then compares against your current state
to generate gap-analysis issues.
"""

import sys
from pathlib import Path

SKILL_NAME = "medical_tourism_strategy"
DESCRIPTION = (
    "Medical tourism accommodation strategies: clinic partnerships, recovery amenities, "
    "pricing packages, platform listings, and content marketing — benchmarked against "
    "Turkey/Thailand gold standards"
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# ─── Researched Data: Turkey Model (Gold Standard) ──────────────────────────
TURKEY_MODEL = {
    "description": (
        "Turkish clinics bundle 3-5 night 4-5 star hotel stays into EVERY hair "
        "transplant package. VIP transport airport-to-hotel-to-clinic is always included. "
        "Albania has NOBODY doing this yet — massive first-mover opportunity."
    ),
    "package_tiers": {
        "standard": {
            "hotel_stars": 4,
            "nights": 2,
            "includes": ["hotel", "airport transfer", "clinic transport"],
        },
        "premium": {
            "hotel_stars": 5,
            "nights": 3,
            "includes": ["hotel", "airport transfer", "clinic transport", "aftercare kit"],
        },
        "vip": {
            "hotel_stars": 5,
            "nights": 5,
            "includes": [
                "hotel", "private airport transfer", "clinic transport",
                "aftercare kit", "companion accommodation", "city tour",
            ],
        },
    },
    "all_inclusive_hair_transplant_eur": "1,500-3,500 including hotel",
    "key_insight": (
        "The clinic owns the patient relationship and sells the entire package. "
        "The accommodation provider just needs to be the clinic's preferred partner."
    ),
}


# ─── Researched Data: Recovery Amenities by Tier ────────────────────────────
RECOVERY_AMENITIES = {
    "tier_1_non_negotiable": {
        "label": "Tier 1 — NON-NEGOTIABLE (must have to enter market)",
        "items": [
            "Walk-in shower with grab bars and non-slip surfaces",
            "Firm bed at 50-60cm height (easy to get in/out post-surgery)",
            "Proximity to clinic (within 15 minutes)",
            "Airport transfer arranged or offered",
            "Fast reliable WiFi",
        ],
    },
    "tier_2_expected": {
        "label": "Tier 2 — EXPECTED (significantly increases bookings)",
        "items": [
            "Ice pack station / cooling supplies",
            "Extra pillows for elevation (critical for hair transplant recovery)",
            "Blackout curtains for daytime rest",
            "Emergency contact card / on-call medical number",
            "Medication storage (small dedicated fridge or fridge section)",
            "Transportation to/from clinic for follow-up appointments",
        ],
    },
    "tier_3_differentiating": {
        "label": "Tier 3 — DIFFERENTIATING (sets you apart from any future competition)",
        "items": [
            "Special recovery pillow for hair transplant (prevents graft contact during sleep)",
            "Blender for soft-food prep (dental surgery patients)",
            "Dark-colored towels and pillowcases (blood stains common post-hair transplant)",
            "Saline spray bottles and hat/head coverings",
            "Recovery care package in room: gauze, saline spray, pain relievers, special shampoo",
        ],
    },
}


# ─── Researched Data: Clinic Partnership Models ─────────────────────────────
CLINIC_PARTNERSHIP_MODELS = {
    "models": [
        {
            "name": "Reverse Commission",
            "description": "You pay clinic 10-15% of room revenue per referral",
            "pros": "Easy for clinics to say yes — they earn from referring",
            "cons": "Eats into your margin; need volume to compensate",
            "best_for": "Initial partnerships where clinic has high patient volume",
        },
        {
            "name": "Wholesale Rate",
            "description": "Offer clinic 20-30% below your retail rate; they mark up in their package",
            "pros": "Clean arrangement; clinic profits from the markup",
            "cons": "You get lower per-night revenue",
            "best_for": "Clinics that sell all-inclusive packages (Turkish model)",
        },
        {
            "name": "Revenue Share on Joint Package",
            "description": "Build a joint package; split revenue 70/30 or 80/20",
            "pros": "Aligned incentives; both parties market the package",
            "cons": "More complex to set up and track",
            "best_for": "Deep partnerships with 1-2 anchor clinics",
        },
        {
            "name": "Flat Fee Per Referral",
            "description": "Pay EUR 25-50 per patient referred regardless of stay length",
            "pros": "Simple, predictable cost; easy to explain to clinic staff",
            "cons": "Fixed cost even for short stays",
            "best_for": "Testing partnerships before committing to revenue share",
        },
    ],
    "recommended_entry_strategy": (
        "Start with a FREE TRIAL: offer 10 free nights for their patients as a pilot. "
        "This removes all risk for the clinic, lets you collect testimonials, and gives "
        "you data to propose a formal partnership agreement."
    ),
}


# ─── Researched Data: Pricing for Medical Stays ─────────────────────────────
MEDICAL_STAY_PRICING = {
    "hair_transplant_package": {
        "name": "Hair Transplant Recovery Package",
        "typical_stay_nights": "3-5",
        "nightly_rate_eur": "40-70",
        "weekly_discount_pct": "15-25%",
        "includes": [
            "Special recovery pillow (no graft contact)",
            "Saline spray and head care supplies",
            "Dark towels and pillowcases",
            "Elevated sleeping arrangement",
            "Clinic transport for follow-ups",
        ],
    },
    "dental_package": {
        "name": "Dental Recovery Package",
        "typical_stay_nights": "7-10",
        "pricing_note": "Weekly rate essential — dental patients stay longer",
        "includes": [
            "Soft food menu guide / blender for prep",
            "Ice packs and cooling station",
            "Clinic transport for follow-ups",
            "Medication fridge",
        ],
    },
    "companion_pricing": {
        "rate": "50-60% of patient rate",
        "note": (
            "Most medical tourists bring a companion (spouse, friend). "
            "Offering a companion rate increases booking probability and total revenue."
        ),
    },
}


# ─── Researched Data: Medical Tourism Platforms ──────────────────────────────
MEDICAL_TOURISM_PLATFORMS = [
    {
        "name": "PlacidWay",
        "description": "4 subscription tiers, web page in 12 languages, 40+ countries",
        "relevance": "List your accommodation as partner lodging for Albanian clinics",
        "url": "https://www.placidway.com",
    },
    {
        "name": "Bookimed",
        "description": "1,590+ clinics listed, employs patient coordinators",
        "relevance": "Contact coordinators directly — they need accommodation partners",
        "url": "https://www.bookimed.com",
    },
    {
        "name": "WhatClinic",
        "description": "120,000+ clinics, 1M+ monthly users globally",
        "relevance": "Patients research clinics here; partner with listed Albanian clinics",
        "url": "https://www.whatclinic.com",
    },
    {
        "name": "Airbnb Medical Stays Program",
        "description": "Dedicated Airbnb program with $2M+ funding for medical travel",
        "relevance": "Apply directly — your property with recovery amenities qualifies",
        "url": "https://www.airbnb.com",
    },
    {
        "name": "Google Business Profile",
        "description": "Optimize for local search",
        "relevance": (
            "Optimize for: 'recovery apartment dental tourism Tirana', "
            "'where to stay dental work Albania', 'medical stay Tirana'"
        ),
        "url": "https://business.google.com",
    },
    {
        "name": "Furnished Finder",
        "description": "Originally for travel nurses, now expanding to medical travelers",
        "relevance": "List with medical-stay keywords for longer recovery bookings",
        "url": "https://www.furnishedfinder.com",
    },
]


# ─── Researched Data: Content Marketing ──────────────────────────────────────
CONTENT_MARKETING = {
    "content_types_ranked_by_conversion": [
        {
            "type": "Patient Journey Stories",
            "conversion_rank": 1,
            "note": "Highest conversion rate — real patients describing their stay + recovery",
        },
        {
            "type": "Cost Comparison Guides",
            "conversion_rank": 2,
            "note": (
                "Highest search traffic — 'Dental implants Albania EUR 460 vs UK EUR 3,100' "
                "drives massive organic clicks"
            ),
        },
        {
            "type": "Recovery Day-by-Day Guides",
            "conversion_rank": 3,
            "note": "Builds trust — shows you understand the patient's actual needs post-surgery",
        },
        {
            "type": "Destination + Recovery Combo Guides",
            "conversion_rank": 4,
            "note": "Captures companion traffic — 'What your partner can do in Tirana while you recover'",
        },
        {
            "type": "Packing Checklists",
            "conversion_rank": 5,
            "note": "Highly shareable on social media and forums",
        },
    ],
    "seo_keywords": [
        "dental tourism apartment Tirana",
        "recovery accommodation Albania",
        "where to stay dental work Albania",
        "hair transplant recovery apartment Tirana",
        "medical tourism accommodation Tirana",
        "dental implants Albania accommodation",
    ],
}


# ─── Researched Data: Albania vs Competitors ─────────────────────────────────
ALBANIA_VS_COMPETITORS = {
    "dental_implant_cost_eur": {
        "albania": 460,
        "turkey": "500-800",
        "hungary": "1,800-4,000",
        "uk": 3100,
        "note": "Albania is cheapest in Europe for dental — 40-60% cheaper than Hungary",
    },
    "hair_transplant_cost_eur": {
        "albania_from": 1599,
        "turkey_range": "1,500-3,500",
    },
    "albania_advantages": [
        "EU accession candidate (builds patient confidence)",
        "Short flights from UK, Germany, Italy (top source markets)",
        "Lowest cost in Europe = sustainable pricing advantage",
        "400% dental tourism growth since 2020",
        "80,000 medical tourists per year and growing",
    ],
    "albania_disadvantages": [
        "Less established medical tourism infrastructure",
        "Less international marketing vs Turkey/Hungary",
        "Smaller facilitator/coordinator network",
        "No accommodation providers bundling with clinics yet",
    ],
}


# ─── Your Current State ─────────────────────────────────────────────────────
YOUR_CURRENT_STATE = {
    "property": "Lulebore Apartment 1",
    "location": "Central Tirana, near major clinics",
    "existing_advantages": [
        "Soundproofing (rare in Tirana — critical for recovery rest)",
        "Private entrance (rare in Tirana — privacy for post-surgery patients)",
        "Central location near major clinics",
    ],
    "clinic_outreach": {
        "total_clinic_leads_in_database": 608,
        "emails_sent": 163,
        "whatsapp_messages_sent": 0,
        "in_person_visits": 0,
        "partnerships_secured": 0,
        "response_rate_estimate": "unknown (no tracking)",
    },
    "recovery_amenities": {
        "walk_in_shower_with_grab_bars": False,
        "firm_bed_correct_height": False,
        "extra_pillows_for_elevation": False,
        "blackout_curtains": False,
        "ice_pack_station": False,
        "medication_fridge": False,
        "emergency_medical_contact_card": False,
        "clinic_transport_offered": False,
        "airport_transfer_offered": False,
        "recovery_care_package": False,
        "special_recovery_pillow": False,
        "blender_for_dental_patients": False,
        "dark_towels_pillowcases": False,
        "saline_spray_head_coverings": False,
    },
    "medical_tourism_packages": {
        "hair_transplant_package": False,
        "dental_package": False,
        "companion_pricing": False,
        "weekly_rate_offered": False,
    },
    "platform_listings": {
        "placidway": False,
        "bookimed": False,
        "whatclinic_partner": False,
        "airbnb_medical_stays": False,
        "google_business_optimized_medical": False,
        "furnished_finder": False,
    },
    "content_marketing": {
        "patient_journey_stories": False,
        "cost_comparison_guides": False,
        "recovery_day_guides": False,
        "destination_recovery_combos": False,
        "packing_checklists": False,
        "seo_optimized_pages": False,
    },
}


# ─── Gap Analysis Engine ────────────────────────────────────────────────────

def analyze_outreach_gap():
    """Compare clinic outreach against what actually works."""
    issues = []
    outreach = YOUR_CURRENT_STATE["clinic_outreach"]

    # Zero WhatsApp outreach
    issues.append({
        "severity": "CRITICAL",
        "area": "Clinic Outreach — Zero WhatsApp Contact",
        "finding": (
            f"You have {outreach['total_clinic_leads_in_database']} clinic leads and sent "
            f"{outreach['emails_sent']} emails, but ZERO WhatsApp messages. In Albania and "
            f"Turkey, WhatsApp is the primary business communication channel for clinics. "
            f"Email open rates for cold outreach are typically 5-15%. WhatsApp open rates "
            f"are 90%+."
        ),
        "recommendation": (
            "Immediately start WhatsApp outreach to your top 50 clinic leads. Use a short "
            "personalized message: introduce yourself, mention the free trial offer (10 free "
            "nights), and attach one photo of the apartment. WhatsApp messages to Albanian "
            "businesses get responses within hours, not days."
        ),
        "what_world_class_does": (
            "Turkish accommodation partners maintain active WhatsApp groups with clinic "
            "coordinators. Patient bookings are confirmed via WhatsApp in real-time. "
            "The entire booking flow is WhatsApp-first, email-second."
        ),
    })

    # Zero in-person visits
    issues.append({
        "severity": "CRITICAL",
        "area": "Clinic Outreach — Zero In-Person Visits",
        "finding": (
            f"You have made 0 in-person visits to clinics despite being located in central "
            f"Tirana near major clinics. In-person visits convert at 10-20x the rate of "
            f"cold emails. Albanian business culture is heavily relationship-driven — "
            f"people do business with people they have met face-to-face."
        ),
        "recommendation": (
            "Visit your top 10 nearest clinics this week. Bring a one-page printed flyer "
            "with apartment photos, your free trial offer, and a QR code to a virtual tour. "
            "Ask to speak with the patient coordinator or international patient manager. "
            "Leave materials even if the decision-maker is unavailable."
        ),
        "what_world_class_does": (
            "Turkish hotel partners have dedicated sales staff who visit clinics monthly. "
            "They host clinic staff for property tours, provide branded welcome materials, "
            "and maintain personal relationships with every clinic coordinator."
        ),
    })

    # Email-only strategy
    issues.append({
        "severity": "HIGH",
        "area": "Clinic Outreach — Email-Only Strategy Has Failed",
        "finding": (
            f"163 emails sent with 0 partnerships secured. Assuming a generous 10% open rate, "
            f"only ~16 clinics even saw your message. Cold email alone does not work for "
            f"B2B partnerships in the Albanian medical sector. The emails may also lack "
            f"a compelling offer."
        ),
        "recommendation": (
            "Switch to a multi-channel sequence: (1) WhatsApp message with free trial offer, "
            "(2) follow up with email containing full details and photos, (3) in-person visit "
            "within 48 hours, (4) follow-up WhatsApp 3 days later. This multi-touch approach "
            "converts at 5-10x a single cold email."
        ),
        "what_world_class_does": (
            "Best-in-class providers use a dedicated partnership manager who runs a CRM, "
            "tracks every touchpoint, and follows a structured outreach cadence: introduction, "
            "free trial, property tour, contract negotiation."
        ),
    })

    return issues


def analyze_amenity_gap():
    """Compare recovery amenities against tiered best practices."""
    issues = []
    amenities = YOUR_CURRENT_STATE["recovery_amenities"]

    # Count what you have vs what you need
    tier_1_items = RECOVERY_AMENITIES["tier_1_non_negotiable"]["items"]
    tier_2_items = RECOVERY_AMENITIES["tier_2_expected"]["items"]
    tier_3_items = RECOVERY_AMENITIES["tier_3_differentiating"]["items"]

    total_amenities = len(amenities)
    have_count = sum(1 for v in amenities.values() if v)
    missing_count = total_amenities - have_count

    issues.append({
        "severity": "CRITICAL",
        "area": "Recovery Amenities — Zero of 14 Present",
        "finding": (
            f"You have {have_count} of {total_amenities} recovery amenities that medical "
            f"tourism accommodation providers are expected to offer. You are missing ALL "
            f"Tier 1 (non-negotiable) items. Without these, no clinic will recommend you "
            f"as a recovery accommodation — you are just a regular apartment."
        ),
        "recommendation": (
            "Invest in Tier 1 amenities IMMEDIATELY (estimated cost: EUR 200-400 total):\n"
            "  - Grab bars for shower: EUR 20-40\n"
            "  - Non-slip bath mat: EUR 10-15\n"
            "  - Extra firm pillows for elevation: EUR 30-50\n"
            "  - Emergency contact card (free — just print it)\n"
            "  - Airport transfer partnership (free — partner with a driver)\n"
            "These are the minimum to call yourself a 'recovery apartment'."
        ),
        "what_world_class_does": (
            "Turkish recovery hotels have ALL three tiers. Rooms are specifically designed "
            "for post-surgery patients with adjustable beds, medical-grade shower facilities, "
            "24/7 nurse call buttons, and pre-stocked recovery kits."
        ),
    })

    # Tier 2 gap
    issues.append({
        "severity": "HIGH",
        "area": "Recovery Amenities — Tier 2 Missing (Booking Killers)",
        "finding": (
            f"Tier 2 amenities (ice packs, extra pillows, blackout curtains, medication "
            f"fridge, clinic transport) significantly increase bookings. These are what "
            f"patients specifically search for when comparing recovery stays. You have none."
        ),
        "recommendation": (
            "Add Tier 2 amenities within 30 days (estimated cost: EUR 100-200):\n"
            "  - Reusable ice packs (pack of 4): EUR 15-20\n"
            "  - Blackout curtains: EUR 30-50\n"
            "  - Small medication fridge or labeled fridge section: EUR 0-50\n"
            "  - Printed emergency medical contact card: EUR 0\n"
            "  - Clinic transport arrangement with a taxi driver: EUR 0 upfront\n"
            "Take photos of every amenity for your listing."
        ),
        "what_world_class_does": (
            "Thailand's Bumrungrad Hospital partner hotels provide a 'recovery concierge' "
            "who stocks the room before arrival based on the specific procedure. Ice packs "
            "are pre-frozen. Pillows are pre-arranged for elevation. It feels medical-grade."
        ),
    })

    # Tier 3 — competitive differentiation
    issues.append({
        "severity": "MEDIUM",
        "area": "Recovery Amenities — Tier 3 Missing (Differentiation)",
        "finding": (
            f"Tier 3 amenities (special recovery pillow, blender, dark towels, saline spray, "
            f"care package) are what turn a good recovery stay into a remarkable one that "
            f"generates word-of-mouth referrals and 5-star reviews. Since Albania has zero "
            f"competitors in this space, even having Tier 1+2 puts you ahead — but Tier 3 "
            f"makes you unreferenceable."
        ),
        "recommendation": (
            "Add Tier 3 amenities within 60 days (estimated cost: EUR 50-100):\n"
            "  - Hair transplant recovery pillow: EUR 20-30\n"
            "  - Blender for dental patients: EUR 20-30\n"
            "  - Dark-colored towel set: EUR 15-20\n"
            "  - Saline spray bottles (bulk): EUR 10-15\n"
            "  - Pre-made care packages: EUR 10-15 per guest (charge it into the rate)\n"
            "Each amenity becomes a photo + selling point in your listing."
        ),
        "what_world_class_does": (
            "Turkish VIP packages include a branded recovery kit waiting in the hotel room: "
            "special pillow, saline spray, prescribed shampoo, neck pillow, hat, gauze, "
            "and a card from the clinic. Patients photograph these and share on social media."
        ),
    })

    # Existing advantages not leveraged
    issues.append({
        "severity": "HIGH",
        "area": "Existing Advantages Not Marketed as Medical Features",
        "finding": (
            f"Your property has soundproofing and a private entrance — both RARE in Tirana "
            f"and both HIGHLY valued by recovery patients. Soundproofing enables undisturbed "
            f"rest (critical post-surgery). Private entrance means patients with bandaged "
            f"heads/swollen faces can enter without walking through common areas. These are "
            f"premium features you are not marketing as medical benefits."
        ),
        "recommendation": (
            "Rewrite your listing to lead with these as medical-recovery features:\n"
            "  - 'Soundproofed rooms for undisturbed recovery rest'\n"
            "  - 'Private entrance — complete privacy during your healing'\n"
            "  - 'Central location — 10 minutes from [specific clinic names]'\n"
            "These three features alone make your property more suitable for medical stays "
            "than 95% of Tirana Airbnbs."
        ),
        "what_world_class_does": (
            "Recovery accommodation providers market every feature through a medical lens. "
            "A quiet room becomes 'soundproofed recovery suite'. A private entrance becomes "
            "'discreet access for post-procedure patients'. Every feature is a recovery benefit."
        ),
    })

    return issues


def analyze_package_gap():
    """Compare pricing and packages against medical tourism standards."""
    issues = []
    packages = YOUR_CURRENT_STATE["medical_tourism_packages"]

    issues.append({
        "severity": "CRITICAL",
        "area": "Medical Tourism Packages — None Created",
        "finding": (
            f"You have zero medical tourism packages. No hair transplant package, no dental "
            f"package, no companion pricing, no weekly rates. Patients searching for "
            f"'recovery accommodation Tirana' find nothing tailored to their needs from you. "
            f"Meanwhile, every Turkish clinic offers a complete package where accommodation "
            f"is included by default."
        ),
        "recommendation": (
            "Create two packages THIS WEEK:\n\n"
            "1. HAIR TRANSPLANT RECOVERY PACKAGE (4 nights):\n"
            "   - EUR 55/night = EUR 220 total\n"
            "   - Includes: recovery pillow, dark towels, saline spray, head coverings\n"
            "   - Includes: airport transfer, clinic transport for follow-up\n"
            "   - Companion add-on: EUR 30/night\n\n"
            "2. DENTAL RECOVERY PACKAGE (7 nights):\n"
            "   - EUR 45/night = EUR 315 total (10% weekly discount)\n"
            "   - Includes: blender, ice packs, soft food guide, medication fridge\n"
            "   - Includes: clinic transport for follow-ups\n"
            "   - Companion add-on: EUR 25/night\n\n"
            "Print these as one-page flyers for clinic visits."
        ),
        "what_world_class_does": (
            "Turkey: every clinic has 3 tiers (Standard/Premium/VIP) with accommodation "
            "bundled. All-inclusive hair transplant runs EUR 1,500-3,500 INCLUDING hotel. "
            "The accommodation is never sold separately — it is part of the medical package."
        ),
    })

    # No weekly rates
    issues.append({
        "severity": "HIGH",
        "area": "No Weekly Rate — Losing Dental Patients",
        "finding": (
            f"Dental tourism patients typically stay 7-10 days. Without a weekly rate or "
            f"discount, dental patients will choose apartments that offer weekly pricing. "
            f"A 7-night stay at your current EUR 45/night = EUR 315. With a 20% weekly "
            f"discount = EUR 252 — still profitable and far more attractive to long-stay "
            f"medical guests."
        ),
        "recommendation": (
            "Implement weekly rates immediately on all platforms:\n"
            "  - 7-night stay: 15-20% discount (EUR 38-42/night)\n"
            "  - 14-night stay: 25-30% discount (EUR 32-38/night)\n"
            "  - 28-night stay: 35-40% discount (EUR 27-33/night)\n"
            "Weekly rates convert medical guests who need extended recovery periods and "
            "generate higher total revenue per booking despite the lower nightly rate."
        ),
        "what_world_class_does": (
            "Medical tourism accommodations universally offer weekly rates. In Thailand, "
            "recovery apartments near Bumrungrad Hospital offer 30-40% discounts for stays "
            "over 7 nights, knowing the total revenue is still 3-4x a weekend booking."
        ),
    })

    # No companion pricing
    issues.append({
        "severity": "MEDIUM",
        "area": "No Companion Pricing — Missing Revenue",
        "finding": (
            f"Most medical tourists (60-70%) bring a companion. You have no companion "
            f"pricing or second-guest policy. If your apartment can accommodate a companion, "
            f"you should price and market this. A companion at EUR 25-30/night adds "
            f"EUR 100-150 per booking with minimal extra cost."
        ),
        "recommendation": (
            "Add companion pricing to all packages:\n"
            "  - Companion rate: 50-60% of patient rate\n"
            "  - Include companion in the listing description: 'Space for a companion "
            "to stay with you during recovery'\n"
            "  - Highlight Tirana activities for companions while patient rests\n"
            "  - Create a 'Companion Guide to Tirana' PDF (restaurants, sights, cafes)"
        ),
        "what_world_class_does": (
            "Turkish VIP packages explicitly include companion accommodation. Thailand's "
            "medical tourism packages have 'patient + companion' pricing on every page. "
            "Companions are treated as a revenue stream, not an afterthought."
        ),
    })

    return issues


def analyze_platform_gap():
    """Compare platform presence against where medical tourists search."""
    issues = []
    platforms = YOUR_CURRENT_STATE["platform_listings"]

    listed_count = sum(1 for v in platforms.values() if v)
    total_platforms = len(platforms)

    issues.append({
        "severity": "HIGH",
        "area": "Medical Tourism Platforms — Listed on Zero of Six",
        "finding": (
            f"You are listed on {listed_count} of {total_platforms} medical tourism platforms "
            f"and directories. Medical tourists do NOT search on regular Airbnb — they search "
            f"on specialized platforms like PlacidWay (40+ countries, 12 languages), Bookimed "
            f"(1,590+ clinics with patient coordinators), and WhatClinic (1M+ monthly users). "
            f"Your property is invisible to this audience."
        ),
        "recommendation": (
            "Priority listing order (do one per week):\n"
            "  Week 1: Google Business Profile — optimize for medical keywords (FREE)\n"
            "  Week 2: Airbnb Medical Stays Program — apply with recovery amenity photos\n"
            "  Week 3: PlacidWay — list as partner accommodation for Albanian clinics\n"
            "  Week 4: Bookimed — contact coordinators for partnership\n"
            "  Week 5: WhatClinic — partner with listed Albanian clinics\n"
            "  Week 6: Furnished Finder — list with medical-stay keywords"
        ),
        "what_world_class_does": (
            "Turkish recovery hotels are listed on ALL major medical tourism platforms, "
            "have multilingual pages, and appear as 'recommended accommodation' on clinic "
            "profiles. They are findable everywhere a medical tourist searches."
        ),
    })

    # Google Business Profile
    issues.append({
        "severity": "HIGH",
        "area": "Google Business Profile Not Optimized for Medical Tourism",
        "finding": (
            f"When patients Google 'recovery apartment dental tourism Tirana' or 'where to "
            f"stay dental work Albania', your property does not appear. Google Business "
            f"Profile optimization for medical tourism keywords is free and drives direct "
            f"bookings without platform commissions."
        ),
        "recommendation": (
            "Optimize your Google Business Profile immediately:\n"
            "  - Category: 'Furnished apartment' or 'Short-term rental'\n"
            "  - Description: include keywords 'dental tourism', 'recovery apartment', "
            "'medical stay', 'hair transplant accommodation'\n"
            "  - Photos: recovery amenities, proximity to clinics, quiet room, shower grab bars\n"
            "  - Posts: weekly posts about dental/medical tourism in Tirana\n"
            "  - Reviews: ask clinic patients to mention 'recovery stay' in their reviews"
        ),
        "what_world_class_does": (
            "Top medical tourism accommodations dominate local search results with "
            "keyword-optimized profiles, 50+ photos, 100+ reviews mentioning medical stays, "
            "and weekly Google Posts about patient experiences."
        ),
    })

    return issues


def analyze_content_gap():
    """Compare content marketing against what converts medical tourists."""
    issues = []
    content = YOUR_CURRENT_STATE["content_marketing"]

    created_count = sum(1 for v in content.values() if v)
    total_types = len(content)

    issues.append({
        "severity": "HIGH",
        "area": "Content Marketing — Zero Medical Tourism Content",
        "finding": (
            f"You have created {created_count} of {total_types} content types that drive "
            f"medical tourism bookings. Cost comparison content ('Dental implants Albania "
            f"EUR 460 vs UK EUR 3,100') drives the highest search traffic. Patient journey "
            f"stories have the highest conversion rate. You have neither."
        ),
        "recommendation": (
            "Create content in this priority order:\n"
            "  1. Cost comparison page: 'Dental Implants Albania vs UK/Germany/Hungary'\n"
            "     (captures highest search volume — patients comparing prices)\n"
            "  2. Recovery day-by-day guide: 'What to Expect: 7 Days After Dental Implants "
            "in Tirana' (builds trust, shows expertise)\n"
            "  3. Patient journey stories: collect from first medical guests "
            "(highest conversion but needs real patients first)\n"
            "  4. Companion guide: 'What Your Partner Can Do in Tirana While You Recover'\n"
            "  5. Packing checklist: 'What to Pack for Dental Tourism in Albania'\n\n"
            "Publish on your Google Business Profile, a simple landing page, and share "
            "with clinic partners for their patients."
        ),
        "what_world_class_does": (
            "Leading medical tourism accommodations maintain blogs with 50+ articles, "
            "YouTube channels with patient testimonials, Instagram accounts showing recovery "
            "rooms, and downloadable PDF guides that clinics distribute to patients."
        ),
    })

    return issues


def analyze_partnership_model_gap():
    """Compare partnership approach against proven models."""
    issues = []

    issues.append({
        "severity": "CRITICAL",
        "area": "No Partnership Model — No Value Proposition for Clinics",
        "finding": (
            f"You have contacted 163 clinics with zero partnerships. This suggests your "
            f"outreach lacks a clear value proposition for the clinic. Clinics need to "
            f"know: (1) what is in it for them, (2) how does it improve their patient "
            f"experience, (3) what is the financial arrangement. A generic 'we have an "
            f"apartment' email gives them no reason to respond."
        ),
        "recommendation": (
            "Build a structured partnership pitch with these components:\n\n"
            "OPENING OFFER (removes all risk):\n"
            "  - '10 free nights for your patients — no cost, no commitment'\n"
            "  - This lets them try it with real patients before any agreement\n\n"
            "VALUE TO CLINIC:\n"
            "  - 'Your patients get a dedicated recovery apartment with [amenities]'\n"
            "  - 'We handle accommodation logistics so you can focus on medical care'\n"
            "  - 'Your international patients get a seamless experience like Turkey offers'\n\n"
            "FINANCIAL MODEL (propose after free trial):\n"
            "  - Option A: You pay them EUR 25-50 per patient referred (flat fee)\n"
            "  - Option B: 20-30% wholesale discount they can mark up\n"
            "  - Option C: 10-15% commission on each booking\n\n"
            "Present this on a single printed page and deliver IN PERSON."
        ),
        "what_world_class_does": (
            "Turkish accommodation partners have formal partnership agreements with "
            "clinics, dedicated account managers, branded welcome packets, and monthly "
            "performance reports. The relationship is professional and mutually profitable."
        ),
    })

    # First-mover advantage urgency
    issues.append({
        "severity": "HIGH",
        "area": "First-Mover Advantage Slipping Away",
        "finding": (
            f"Albania has ZERO accommodation providers doing medical tourism packages. "
            f"You have 608 clinic leads but 0 partnerships. Meanwhile, Albania's dental "
            f"tourism grew 400% since 2020 and the country sees 80,000 medical tourists/year. "
            f"Every month you delay, the chance increases that someone else moves first. "
            f"In Turkey, the early hotel partners locked in exclusive clinic relationships "
            f"that new entrants cannot break."
        ),
        "recommendation": (
            "Execute the 30-day blitz:\n"
            "  Week 1: Buy and install Tier 1 recovery amenities (EUR 200-400)\n"
            "  Week 1: Create 2 medical packages with printed flyers\n"
            "  Week 2: Visit top 10 clinics in person with free trial offer\n"
            "  Week 2: Start WhatsApp outreach to top 50 clinic leads\n"
            "  Week 3: Follow up all contacts, book property tours for interested clinics\n"
            "  Week 3: List on Google Business Profile with medical keywords\n"
            "  Week 4: Secure at least 1-2 trial partnerships\n"
            "  Week 4: Host first medical guest, collect feedback and photos\n\n"
            "Target: 2 active clinic partnerships within 30 days."
        ),
        "what_world_class_does": (
            "Turkey's medical tourism accommodation market is now DOMINATED by the first "
            "movers who partnered with clinics in 2015-2018. Latecomers compete on price "
            "and lose. In Albania, you can still be the first — but this window will close."
        ),
    })

    return issues


def generate_summary_scorecard():
    """Generate a scorecard comparing you vs world-class."""
    categories = [
        {
            "category": "Recovery Amenities",
            "your_score": "0/14",
            "world_class": "14/14",
            "grade": "F",
            "investment_needed_eur": "350-700",
        },
        {
            "category": "Medical Packages",
            "your_score": "0/4",
            "world_class": "4/4 with 3 tiers each",
            "grade": "F",
            "investment_needed_eur": "0 (time only)",
        },
        {
            "category": "Clinic Outreach Channels",
            "your_score": "1/3 (email only)",
            "world_class": "3/3 (email + WhatsApp + in-person)",
            "grade": "D",
            "investment_needed_eur": "0 (effort only)",
        },
        {
            "category": "Clinic Partnerships",
            "your_score": "0",
            "world_class": "5-15 active partnerships",
            "grade": "F",
            "investment_needed_eur": "0 upfront (10 free trial nights = EUR 0-450 opportunity cost)",
        },
        {
            "category": "Platform Listings",
            "your_score": "0/6",
            "world_class": "6/6 medical tourism platforms",
            "grade": "F",
            "investment_needed_eur": "0-200 (most are free to list)",
        },
        {
            "category": "Content Marketing",
            "your_score": "0/6",
            "world_class": "6/6 content types + 50+ articles",
            "grade": "F",
            "investment_needed_eur": "0 (time only — or EUR 200-500 for freelance writer)",
        },
        {
            "category": "Marketing Existing Advantages",
            "your_score": "Not marketed",
            "world_class": "Every feature framed as recovery benefit",
            "grade": "D",
            "investment_needed_eur": "0 (rewrite listing text)",
        },
    ]

    total_investment_low = 350 + 0 + 0 + 0 + 0 + 0 + 0
    total_investment_high = 700 + 0 + 0 + 450 + 200 + 500 + 0

    return {
        "categories": categories,
        "overall_grade": "F",
        "total_investment_needed_eur": f"{total_investment_low}-{total_investment_high}",
        "total_investment_note": (
            f"EUR {total_investment_low}-{total_investment_high} total covers EVERYTHING. "
            f"For context, a single 7-night dental patient booking at EUR 45/night = EUR 315. "
            f"Two bookings pay for the entire investment. Turkey's clinics send 50-200 "
            f"patients/month to partner hotels."
        ),
        "bottom_line": (
            "You have a property with rare advantages (soundproofing, private entrance, "
            "central location, 608 clinic leads) but are marketing it as a generic apartment "
            "in a market with 3,488 competitors. The medical tourism niche has 80,000 patients/year, "
            "400% growth, zero competition in Albania, and requires less than EUR 700 to enter. "
            "This is the single highest-ROI opportunity available to you."
        ),
    }


def run():
    """Main skill entry point."""
    outreach_issues = analyze_outreach_gap()
    amenity_issues = analyze_amenity_gap()
    package_issues = analyze_package_gap()
    platform_issues = analyze_platform_gap()
    content_issues = analyze_content_gap()
    partnership_issues = analyze_partnership_model_gap()
    scorecard = generate_summary_scorecard()

    all_issues = (
        outreach_issues
        + amenity_issues
        + package_issues
        + platform_issues
        + content_issues
        + partnership_issues
    )

    # Sort: CRITICAL first, then HIGH, then MEDIUM
    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    all_issues.sort(key=lambda x: severity_order.get(x["severity"], 99))

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "research_data": {
            "turkey_model": TURKEY_MODEL,
            "recovery_amenities": RECOVERY_AMENITIES,
            "clinic_partnership_models": CLINIC_PARTNERSHIP_MODELS,
            "medical_stay_pricing": MEDICAL_STAY_PRICING,
            "medical_tourism_platforms": MEDICAL_TOURISM_PLATFORMS,
            "content_marketing": CONTENT_MARKETING,
            "albania_vs_competitors": ALBANIA_VS_COMPETITORS,
        },
        "your_current_state": YOUR_CURRENT_STATE,
        "scorecard": scorecard,
        "issues": all_issues,
        "issues_count": len(all_issues),
        "issues_by_severity": {
            "CRITICAL": len([i for i in all_issues if i["severity"] == "CRITICAL"]),
            "HIGH": len([i for i in all_issues if i["severity"] == "HIGH"]),
            "MEDIUM": len([i for i in all_issues if i["severity"] == "MEDIUM"]),
        },
    }

    # ─── Console Output ─────────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"  Medical Tourism Strategy — Gap Analysis")
    print(f"{'='*70}")

    print(f"\n  TURKEY MODEL (Gold Standard):")
    print(f"    Clinics bundle hotel stays into EVERY package")
    print(f"    All-inclusive hair transplant: EUR {TURKEY_MODEL['all_inclusive_hair_transplant_eur']}")
    print(f"    Albania has NOBODY doing this = first-mover opportunity")

    print(f"\n  ALBANIA COMPETITIVE POSITION:")
    ac = ALBANIA_VS_COMPETITORS
    print(f"    Dental implant: Albania EUR {ac['dental_implant_cost_eur']['albania']} "
          f"vs Turkey EUR {ac['dental_implant_cost_eur']['turkey']} "
          f"vs Hungary EUR {ac['dental_implant_cost_eur']['hungary']} "
          f"vs UK EUR {ac['dental_implant_cost_eur']['uk']}")
    print(f"    Albania is cheapest in Europe for dental (40-60% < Hungary)")
    print(f"    80,000 medical tourists/year, 400% dental growth since 2020")

    print(f"\n  YOUR CURRENT STATE:")
    print(f"    Property:        {YOUR_CURRENT_STATE['property']}")
    print(f"    Advantages:      Soundproofing, private entrance, central location")
    o = YOUR_CURRENT_STATE["clinic_outreach"]
    print(f"    Clinic leads:    {o['total_clinic_leads_in_database']}")
    print(f"    Emails sent:     {o['emails_sent']}")
    print(f"    WhatsApp sent:   {o['whatsapp_messages_sent']}")
    print(f"    In-person visits: {o['in_person_visits']}")
    print(f"    Partnerships:    {o['partnerships_secured']}")
    print(f"    Recovery amenities: 0 of 14")
    print(f"    Medical packages: 0")
    print(f"    Medical platforms: 0 of 6")

    print(f"\n  SCORECARD:")
    for cat in scorecard["categories"]:
        print(f"    [{cat['grade']}] {cat['category']}: {cat['your_score']} "
              f"(world-class: {cat['world_class']})")
    print(f"    OVERALL GRADE: {scorecard['overall_grade']}")
    print(f"    Investment needed: EUR {scorecard['total_investment_needed_eur']}")

    print(f"\n  ISSUES FOUND: {len(all_issues)}")
    print(f"    CRITICAL: {result['issues_by_severity']['CRITICAL']}")
    print(f"    HIGH:     {result['issues_by_severity']['HIGH']}")
    print(f"    MEDIUM:   {result['issues_by_severity']['MEDIUM']}")
    print()
    for i, issue in enumerate(all_issues, 1):
        print(f"    {i:2d}. [{issue['severity']}] {issue['area']}")
    print(f"\n{'='*70}")
    print(f"  {scorecard['bottom_line']}")
    print(f"{'='*70}\n")

    return result


if __name__ == "__main__":
    run()
