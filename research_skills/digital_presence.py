"""
Skill: Digital Presence
Researches digital marketing and online presence strategies for Airbnb hosts —
social media, direct booking websites, Google Business Profile, paid ads,
email marketing, content marketing, and medical tourism platforms — then
compares best practices against your property's current (zero) digital footprint.
"""

import sys
from pathlib import Path

SKILL_NAME = "digital_presence"
DESCRIPTION = "Digital marketing, online presence, and direct booking strategies vs your current zero footprint"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# ─── Researched Digital Presence Data (Feb 2026) ────────────────────────────

SOCIAL_MEDIA_DATA = {
    "impact": {
        "active_social_media_booking_lift_pct": 23,
        "tiktok_travel_content_growth_since_2021_pct": 410,
        "european_tiktok_users_would_book_pct": 71,
    },
    "instagram": {
        "recommended_frequency": "2-3 posts per week",
        "content_types": ["Reels (room tours, neighborhood walks)", "Carousel photos (before/after stays)", "Stories (daily life in Tirana, guest shoutouts)"],
        "hashtags": ["#TiranaAirbnb", "#DentalTourismAlbania", "#AlbaniaTravel", "#TiranaStay", "#MedicalTourismAlbania"],
        "best_practice": "Mix property content (40%), local area (40%), and guest testimonials (20%)",
    },
    "tiktok": {
        "content_ideas": [
            "Short room tours (15-30 seconds)",
            "What €45/night gets you in Tirana",
            "Local food clips from nearby restaurants",
            "POV: recovering from dental surgery in Albania",
            "Day in the life of a Tirana Airbnb host",
        ],
        "search_ads_beta_2025": True,
        "search_ads_detail": "Bid on high-intent travel keywords; CPCs currently lower than Google Ads",
        "style_tip": "Keep videos natural and unpolished — authenticity outperforms production quality",
    },
    "youtube": {
        "recommended_title": "Lulebore Apartment 1 — Central Tirana Apartment Tour",
        "seo_benefit": "Apartment tour videos rank in Google search results, acting as free long-term advertising",
        "content_cadence": "Monthly patient story videos, quarterly updated room tours",
    },
}

DIRECT_BOOKING_DATA = {
    "platform_fee_saved_pct": 15.5,
    "fee_context": "Airbnb changed to 15.5% host-only fee structure in late 2025",
    "annual_fee_at_current_revenue": {
        "your_annual_revenue_eur": 6500,
        "annual_fees_to_airbnb_eur": 1008,
        "explanation": "At €6,500/year revenue, ~€1,008/year goes to Airbnb in host fees alone",
    },
    "tools": {
        "hospitable": {"cost_per_month_usd": 29, "features": "Channel manager, direct booking site, automated messaging"},
        "ownerrez": {"cost_per_month_usd": 40, "features": "Full PMS, direct booking engine, integrated payments"},
        "lodgify": {"cost_per_month_usd": "140-400", "features": "Website builder + PMS, best for scaling"},
        "carrd": {"cost_per_year_eur": 19, "features": "Simple single-page site with booking link — lowest cost option"},
    },
    "strategy": "Use Airbnb for guest acquisition (new guests find you), use direct booking for retention (repeat guests save on fees)",
    "industry_trend": {
        "operators_reporting_direct_growth_2025_pct": 37.5,
        "case_study": "One host went from 0% to 30% direct bookings in 1.5 years using email capture and a simple direct booking page",
    },
}

GOOGLE_BUSINESS_PROFILE_DATA = {
    "cost": "Free",
    "visibility": "Appears in Google Search and Google Maps for local queries",
    "category": "Register as 'Tourist Accommodation' or 'Vacation Apartment'",
    "optimization_steps": [
        "Claim and verify your business listing",
        "Add all high-quality photos (minimum 15-20)",
        "Write a detailed description mentioning medical tourism proximity",
        "Respond to every review within 24 hours",
        "Post weekly updates (local events, seasonal offers, property improvements)",
        "Add attributes: WiFi, kitchen, washer, elevator, etc.",
    ],
    "target_keywords": [
        "apartment near dental clinic Tirana",
        "central Tirana short stay",
        "dental tourism accommodation Tirana",
        "recovery apartment Tirana Albania",
    ],
}

PAID_ADS_DATA = {
    "google_ads": {
        "target_keywords": ["dental tourism accommodation Tirana", "apartment near dental clinic Albania", "Tirana short stay apartment"],
        "recommended_daily_budget_eur": 5,
        "roi_note": "A single booking from a €5/day ad pays for 3+ months of ad spend",
    },
    "facebook_ads": {
        "avg_cpc_usd": 0.04,
        "target_demographics": "Ages 30-60, interests in dental tourism and medical travel",
        "geo_targets": ["Italy", "United Kingdom", "Germany", "United States"],
        "ad_types": ["Carousel (property photos)", "Video (room tour)", "Retargeting (website visitors who didn't book)"],
    },
    "retargeting_strategy": "User clicks Google Ad but doesn't book → retarget with Facebook ad showing reviews and a direct booking discount",
    "combined_budget_eur_per_month": 250,
    "expected_extra_bookings_per_month": "3-6",
    "critical_rule": "NEVER send paid traffic to your Airbnb listing — you pay platform fees on top of ad costs. Always send to your direct booking page.",
}

EMAIL_MARKETING_DATA = {
    "core_stat": "Past guests are 5x cheaper to convert than acquiring new ones",
    "email_capture": {
        "tool": "StayFi WiFi portal",
        "mechanism": "Every guest device must pass through a branded splash page to access WiFi — captures email automatically",
        "results": "StayFi customers have collected 50,000+ emails total, with 60%+ open rates on welcome emails",
    },
    "automated_drip_sequence": [
        {"timing": "Day after checkout", "email": "Thank-you email with review request and 10% direct booking code"},
        {"timing": "30 days post-stay", "email": "Discount offer for next visit (15% off direct booking)"},
        {"timing": "90 days post-stay", "email": "Rebooking reminder with seasonal highlights"},
        {"timing": "6 months post-stay", "email": "Win-back offer with 20% off and property updates"},
        {"timing": "Seasonal triggers", "email": "Pre-summer and pre-holiday targeted campaigns"},
    ],
    "monthly_newsletter": {
        "content": ["Local events and festivals in Tirana", "Property improvements and new amenities", "Exclusive direct-booking-only discounts", "Tirana travel tips and hidden gems"],
        "benefit": "Keeps your property top-of-mind — when a past guest's friend needs a place in Tirana, you're the recommendation",
    },
}

CONTENT_MARKETING_DATA = {
    "blog_seo_targets": [
        "best apartment for dental tourists Tirana",
        "recovery accommodation hair transplant Albania",
        "dental tourism Tirana where to stay",
        "Albania medical tourism accommodation guide",
    ],
    "top_content_types": {
        "patient_journey_stories": {"traffic": "Medium", "conversion": "Highest", "note": "Real guest stories about their dental/medical trip and recovery stay"},
        "cost_comparison_guides": {"traffic": "Highest", "conversion": "Medium", "note": "'Dental implants Albania vs UK vs Turkey — full cost breakdown including accommodation'"},
        "recovery_day_by_day_guides": {"traffic": "Medium", "conversion": "High", "note": "Builds trust by showing exactly what recovery looks like — 'Day 1-7 after dental implants in Tirana'"},
    },
    "pinterest": {
        "content": ["Recovery tips infographics", "Dental tourism packing lists", "Tirana neighborhood guides", "Before/after cost comparison graphics"],
    },
    "facebook_groups": {
        "target_communities": ["Dental Tourism Albania", "Medical Tourism Albania", "Expats in Tirana", "Albania Travel Tips"],
        "approach": "Provide genuine value and advice — never hard-sell. Mention your property only when directly relevant.",
    },
}

MEDICAL_TOURISM_PLATFORMS_DATA = {
    "platforms": {
        "placidway": {"description": "Global medical tourism marketplace", "feature": "Property page available in 12 languages", "model": "Subscription tiers"},
        "bookimed": {"description": "Medical tourism booking platform", "reach": "1,590+ partner clinics globally", "model": "Commission or subscription"},
        "whatclinic": {"description": "Clinic and provider directory", "reach": "120,000+ clinics listed, 1M+ monthly users", "model": "Listing + leads"},
        "airbnb_medical_stays": {"description": "Airbnb's dedicated Medical Stays program for patients needing accommodation near treatment", "model": "Standard Airbnb fees"},
        "furnished_finder": {"description": "Platform for medium-term furnished rentals, popular with medical travelers and traveling professionals", "model": "Annual listing fee"},
    },
    "opportunity": "List your property on medical tourism platforms to reach patients who are already searching for recovery accommodation — a channel your competitors have not tapped.",
}

# ─── Your Current Digital Presence ───────────────────────────────────────────

YOUR_DIGITAL_PRESENCE = {
    "social_media": {
        "instagram": False,
        "tiktok": False,
        "youtube": False,
        "facebook_page": False,
    },
    "direct_booking_website": False,
    "google_business_profile": False,
    "paid_ads": {
        "google_ads": False,
        "facebook_ads": False,
        "tiktok_search_ads": False,
    },
    "email_marketing": {
        "email_capture_system": False,
        "automated_drip": False,
        "newsletter": False,
    },
    "content_marketing": {
        "blog": False,
        "pinterest": False,
        "facebook_group_presence": False,
    },
    "medical_tourism_platforms": {
        "placidway": False,
        "bookimed": False,
        "whatclinic": False,
        "airbnb_medical_stays": False,
        "furnished_finder": False,
    },
    "current_channels": ["Airbnb", "Booking.com"],
    "channel_dependency_pct": 100,
}


def analyze_digital_gaps():
    """Compare your digital presence against what successful hosts do."""
    you = YOUR_DIGITAL_PRESENCE

    channels_used = len(you["current_channels"])
    channels_missing = (
        sum(1 for v in you["social_media"].values() if not v)
        + (0 if you["direct_booking_website"] else 1)
        + (0 if you["google_business_profile"] else 1)
        + sum(1 for v in you["paid_ads"].values() if not v)
        + sum(1 for v in you["email_marketing"].values() if not v)
        + sum(1 for v in you["content_marketing"].values() if not v)
        + sum(1 for v in you["medical_tourism_platforms"].values() if not v)
    )

    return {
        "channels_active": channels_used,
        "channels_missing": channels_missing,
        "platform_dependency_pct": you["channel_dependency_pct"],
        "risk_level": "CRITICAL",
        "summary": (
            f"You use {channels_used} booking channels and {channels_missing} digital marketing "
            f"channels are completely unused. 100% of your revenue depends on third-party platforms "
            f"that charge 15-20% fees and could change algorithms or policies at any time."
        ),
    }


def identify_issues():
    """Generate issues comparing best practices against your zero digital presence."""
    issues = []

    # ── Issue 1: No Social Media Presence ────────────────────────────────────
    issues.append({
        "severity": "HIGH",
        "area": "Zero Social Media Presence",
        "finding": (
            f"Properties with active social media see a {SOCIAL_MEDIA_DATA['impact']['active_social_media_booking_lift_pct']}% "
            f"higher booking rate. TikTok travel content grew {SOCIAL_MEDIA_DATA['impact']['tiktok_travel_content_growth_since_2021_pct']}% "
            f"since 2021, and {SOCIAL_MEDIA_DATA['impact']['european_tiktok_users_would_book_pct']}% of European TikTok users "
            f"say they would book accommodation based on TikTok content. "
            f"You have zero social media accounts for your property."
        ),
        "recommendation": (
            "Start with Instagram and TikTok — both are free and high-impact for accommodation. "
            "Instagram: post 2-3x/week with reels, carousel photos, and stories. "
            f"Use hashtags: {', '.join(SOCIAL_MEDIA_DATA['instagram']['hashtags'][:3])}. "
            "TikTok: film short, authentic room tours and 'What €45/night gets you in Tirana' content. "
            "Keep videos natural and unpolished — authenticity outperforms production quality on both platforms."
        ),
        "what_others_do": (
            "Successful short-term rental hosts maintain active Instagram and TikTok accounts, "
            "posting 2-3x/week. They film quick room tours, neighborhood walks, and guest experience content. "
            "The most effective hosts treat social media as a free advertising channel that compounds over time."
        ),
        "action_items": [
            "Create an Instagram business account: @lulebore.tirana (or similar)",
            "Create a TikTok account with the same handle",
            "Film 5 short videos this week: room tour, balcony view, walk to nearest dental clinic, local restaurant, neighborhood overview",
            "Post 2-3x/week on Instagram (reels + carousel photos) and 3-4x/week on TikTok",
            "Use dental tourism and Tirana travel hashtags on every post",
        ],
    })

    # ── Issue 2: No YouTube Presence ─────────────────────────────────────────
    issues.append({
        "severity": "MEDIUM",
        "area": "No YouTube Apartment Tour Video",
        "finding": (
            "YouTube apartment tour videos rank directly in Google search results, providing "
            "free long-term visibility. When potential guests search 'Tirana apartment' or "
            "'dental tourism accommodation Albania', a well-optimized video can appear on page one. "
            "You have no YouTube presence."
        ),
        "recommendation": (
            f"Create a YouTube channel and upload a detailed apartment tour video titled: "
            f"'{SOCIAL_MEDIA_DATA['youtube']['recommended_title']}'. "
            f"Follow with monthly patient story videos and quarterly updated room tours. "
            f"A single well-made apartment tour video can generate bookings for years."
        ),
        "what_others_do": (
            "Top-performing hosts have YouTube apartment tour videos that rank in Google search. "
            "Some hosts report that their YouTube video is the single highest-converting piece of content they have — "
            "guests watch it, trust the property, and book with confidence."
        ),
        "action_items": [
            "Create a YouTube channel for your property",
            f"Film and upload: '{SOCIAL_MEDIA_DATA['youtube']['recommended_title']}'",
            "Optimize title, description, and tags for 'Tirana apartment', 'dental tourism Albania accommodation'",
            "Add the YouTube link to your Airbnb listing description and future direct booking page",
        ],
    })

    # ── Issue 3: No Direct Booking Website ───────────────────────────────────
    issues.append({
        "severity": "HIGH",
        "area": "No Direct Booking Website — Losing ~€1,000/Year to Platform Fees",
        "finding": (
            f"Airbnb charges {DIRECT_BOOKING_DATA['platform_fee_saved_pct']}% in host-only fees "
            f"(changed in late 2025). At your estimated annual revenue of "
            f"€{DIRECT_BOOKING_DATA['annual_fee_at_current_revenue']['your_annual_revenue_eur']:,}, "
            f"you pay approximately €{DIRECT_BOOKING_DATA['annual_fee_at_current_revenue']['annual_fees_to_airbnb_eur']:,}/year "
            f"in platform fees. {DIRECT_BOOKING_DATA['industry_trend']['operators_reporting_direct_growth_2025_pct']}% "
            f"of operators reported growth in direct reservations in 2025. "
            f"You have no direct booking channel."
        ),
        "recommendation": (
            f"Start with Carrd (€{DIRECT_BOOKING_DATA['tools']['carrd']['cost_per_year_eur']}/year) for a simple "
            f"direct booking landing page with a Stripe or PayPal payment link. "
            f"Strategy: {DIRECT_BOOKING_DATA['strategy']}. "
            f"As volume grows, upgrade to Hospitable (${DIRECT_BOOKING_DATA['tools']['hospitable']['cost_per_month_usd']}/mo) "
            f"or OwnerRez (${DIRECT_BOOKING_DATA['tools']['ownerrez']['cost_per_month_usd']}/mo) for full channel management. "
            f"Case study: {DIRECT_BOOKING_DATA['industry_trend']['case_study']}."
        ),
        "what_others_do": (
            "Successful hosts use Airbnb as a guest acquisition channel (where new guests discover them) "
            "and then convert repeat guests to direct bookings, saving 15-20% in platform fees. "
            "They offer a 5-10% 'book direct' discount that still nets them more revenue after eliminating platform fees."
        ),
        "action_items": [
            "Set up a Carrd page (€19/year) with property photos, amenities, pricing, and a booking/contact form",
            "Add a Stripe or PayPal payment link for direct bookings",
            "Offer a 10% 'book direct' discount (you still save 5.5% vs Airbnb after the discount)",
            "Include the direct booking link in your post-stay thank-you messages to past guests",
            "Upgrade to Hospitable or OwnerRez when direct bookings exceed 3-4/month",
        ],
    })

    # ── Issue 4: No Google Business Profile ──────────────────────────────────
    issues.append({
        "severity": "HIGH",
        "area": "No Google Business Profile — Missing Free Visibility",
        "finding": (
            "Google Business Profile provides free visibility in Google Search and Google Maps. "
            "When someone searches 'apartment near dental clinic Tirana' or 'central Tirana short stay', "
            "properties with claimed Google Business Profiles appear prominently with photos, reviews, "
            "and direct contact information. You have no Google Business Profile."
        ),
        "recommendation": (
            f"Create a free Google Business Profile registered as '{GOOGLE_BUSINESS_PROFILE_DATA['category']}'. "
            f"Optimization steps: {'; '.join(GOOGLE_BUSINESS_PROFILE_DATA['optimization_steps'][:4])}. "
            f"Target keywords: {', '.join(GOOGLE_BUSINESS_PROFILE_DATA['target_keywords'][:3])}. "
            f"Post weekly updates about local events and seasonal offers to boost ranking."
        ),
        "what_others_do": (
            "Professional hosts and small hotels all have claimed Google Business Profiles with "
            "15-20+ photos, detailed descriptions, and active review management. "
            "This is the single easiest free marketing action — it takes 30 minutes to set up "
            "and provides years of free visibility."
        ),
        "action_items": [
            "Go to business.google.com and create a listing for Lulebore Apartment 1",
            "Select category: 'Tourist Accommodation' or 'Vacation Apartment'",
            "Upload all high-quality property photos (minimum 15-20)",
            "Write a description mentioning: central Tirana, dental tourism proximity, medical stay friendly",
            "Add all amenities as attributes (WiFi, kitchen, washer, etc.)",
            "Respond to every review within 24 hours",
            "Post a weekly update (takes 5 minutes) about local events or property news",
        ],
    })

    # ── Issue 5: No Paid Advertising ─────────────────────────────────────────
    issues.append({
        "severity": "MEDIUM",
        "area": "No Paid Advertising — Missing High-Intent Dental Tourism Guests",
        "finding": (
            f"Google Ads targeting 'dental tourism accommodation Tirana' can be run for as little as "
            f"€{PAID_ADS_DATA['google_ads']['recommended_daily_budget_eur']}/day. A single booking from these ads "
            f"pays for 3+ months of ad spend. Facebook Ads for accommodation have CPCs as low as "
            f"${PAID_ADS_DATA['facebook_ads']['avg_cpc_usd']:.2f}. "
            f"You run zero paid ads."
        ),
        "recommendation": (
            f"Start with a €{PAID_ADS_DATA['google_ads']['recommended_daily_budget_eur']}/day Google Ads campaign "
            f"targeting: {', '.join(PAID_ADS_DATA['google_ads']['target_keywords'][:2])}. "
            f"Add Facebook Ads targeting ages 30-60 with dental tourism interests, geo-targeting "
            f"{', '.join(PAID_ADS_DATA['facebook_ads']['geo_targets'][:3])}. "
            f"Use retargeting: {PAID_ADS_DATA['retargeting_strategy']}. "
            f"Total budget: €{PAID_ADS_DATA['combined_budget_eur_per_month']}/month for "
            f"{PAID_ADS_DATA['expected_extra_bookings_per_month']} extra bookings. "
            f"CRITICAL: {PAID_ADS_DATA['critical_rule']}"
        ),
        "what_others_do": (
            "Smart hosts run small Google Ads budgets (€5-10/day) targeting high-intent niche keywords. "
            "They never send paid traffic to Airbnb (double fees). Instead, they send traffic to their "
            "direct booking page and use Facebook retargeting to recapture visitors who didn't book."
        ),
        "action_items": [
            "Set up a Google Ads account with a €5/day budget",
            "Create a search campaign targeting 'dental tourism accommodation Tirana' and related keywords",
            "Set up a Facebook Ads account targeting Italy, UK, Germany — ages 30-60, dental tourism interest",
            "Install the Facebook Pixel on your direct booking page for retargeting",
            "CRITICAL: Send all paid traffic to your direct booking page, NEVER to Airbnb",
            "Track cost-per-booking and scale what works, cut what doesn't",
        ],
    })

    # ── Issue 6: No Email Marketing to Past Guests ───────────────────────────
    issues.append({
        "severity": "HIGH",
        "area": "No Email Marketing — Losing Your Most Valuable Asset (Past Guest List)",
        "finding": (
            f"{EMAIL_MARKETING_DATA['core_stat']}. "
            f"StayFi WiFi portals have collected 50,000+ guest emails across their customers, "
            f"with 60%+ open rates on welcome emails. You capture zero guest emails "
            f"and have no way to re-engage past guests outside of Airbnb."
        ),
        "recommendation": (
            f"Install StayFi ({EMAIL_MARKETING_DATA['email_capture']['tool']}) — "
            f"{EMAIL_MARKETING_DATA['email_capture']['mechanism']}. "
            f"Set up an automated drip sequence: "
            f"(1) {EMAIL_MARKETING_DATA['automated_drip_sequence'][0]['email']}, "
            f"(2) {EMAIL_MARKETING_DATA['automated_drip_sequence'][1]['email']}, "
            f"(3) {EMAIL_MARKETING_DATA['automated_drip_sequence'][2]['email']}, "
            f"(4) {EMAIL_MARKETING_DATA['automated_drip_sequence'][3]['email']}. "
            f"Send a monthly newsletter with: {', '.join(EMAIL_MARKETING_DATA['monthly_newsletter']['content'][:3])}."
        ),
        "what_others_do": (
            "Professional hosts capture every guest's email through WiFi splash pages (StayFi is the most popular tool). "
            "They then run automated email sequences that drive repeat direct bookings. "
            "A host with 54 past reviews (like you) likely had 60-80+ unique guests — that's a ready-made email "
            "list worth hundreds of euros in direct bookings, but only if you start capturing emails now."
        ),
        "action_items": [
            "Sign up for StayFi and set up the WiFi splash page for email capture",
            "Configure your router to redirect all new devices through the StayFi portal",
            "Set up a free Mailchimp or MailerLite account for email automation",
            "Create a 4-email automated drip: thank-you → 30-day offer → 90-day reminder → 6-month win-back",
            "Send a monthly newsletter with Tirana events and exclusive direct-booking discounts",
            "Add past guests manually if you have any contact information from Airbnb messages",
        ],
    })

    # ── Issue 7: No Content Marketing / Blog ─────────────────────────────────
    issues.append({
        "severity": "MEDIUM",
        "area": "No Content Marketing — Missing Long-Tail Medical Tourism Search Traffic",
        "finding": (
            "People actively search for terms like "
            f"'{CONTENT_MARKETING_DATA['blog_seo_targets'][0]}' and "
            f"'{CONTENT_MARKETING_DATA['blog_seo_targets'][1]}'. "
            f"The highest-converting content type is patient journey stories. "
            f"The highest-traffic content type is cost comparison guides. "
            f"You produce no content and rank for zero search terms."
        ),
        "recommendation": (
            "Start a simple blog on your direct booking website (or on Medium for free). "
            "Publish 2-4 articles per month targeting medical tourism search terms. "
            "Top content to create: (1) Patient journey stories — ask past dental tourism guests to share "
            "their experience (highest conversion rate). (2) Cost comparison guides — 'Dental implants Albania "
            "vs UK vs Turkey: full cost breakdown' (drives the most traffic). (3) Recovery day-by-day guides — "
            "'What to expect days 1-7 after dental implants in Tirana' (builds trust). "
            "Also join Facebook Groups like 'Dental Tourism Albania' and provide genuine advice."
        ),
        "what_others_do": (
            "Medical tourism accommodation providers in Turkey and Thailand create extensive content libraries. "
            "They publish patient stories, cost guides, and recovery tips that rank in Google and drive "
            "organic bookings. A single well-written article can generate bookings for years. "
            "The smartest operators also maintain active presences in relevant Facebook Groups, "
            "offering genuine advice that naturally drives referrals."
        ),
        "action_items": [
            "Start a blog section on your direct booking site (or use Medium.com for free)",
            "Write your first article: 'Where to Stay During Dental Treatment in Tirana — A Complete Guide'",
            "Ask 2-3 past dental tourism guests to share their experience for a patient story post",
            "Create a cost comparison guide: 'Dental implants in Albania vs UK vs Turkey (including accommodation)'",
            "Join 'Dental Tourism Albania' and 'Medical Tourism Albania' Facebook Groups",
            "Create a Pinterest account and post infographics on dental tourism tips and packing lists",
        ],
    })

    # ── Issue 8: Not Listed on Medical Tourism Platforms ──────────────────────
    issues.append({
        "severity": "HIGH",
        "area": "Not Listed on Any Medical Tourism Platform",
        "finding": (
            f"WhatClinic has {MEDICAL_TOURISM_PLATFORMS_DATA['platforms']['whatclinic']['reach']}. "
            f"Bookimed partners with {MEDICAL_TOURISM_PLATFORMS_DATA['platforms']['bookimed']['reach']}. "
            f"PlacidWay offers listings in 12 languages. Airbnb has a dedicated Medical Stays program. "
            f"Furnished Finder targets medium-term stays popular with medical travelers. "
            f"You are listed on zero medical tourism platforms."
        ),
        "recommendation": (
            "Register on Airbnb Medical Stays (free, you're already on Airbnb — just opt into the program). "
            "List on Furnished Finder for medium-term medical stay visibility. "
            "Contact PlacidWay and Bookimed about accommodation partner listings — "
            "these platforms have patients actively searching for recovery lodging. "
            "Reach out to WhatClinic-listed dental clinics in Tirana to offer partnership referrals."
        ),
        "what_others_do": (
            "In mature medical tourism markets (Turkey, Thailand, Mexico), accommodation providers "
            "list on multiple medical tourism platforms. Clinic-accommodation bundling is standard — "
            "patients expect it. In Albania, almost nobody has done this yet, creating a first-mover advantage."
        ),
        "action_items": [
            "Opt into Airbnb's Medical Stays program (through your existing Airbnb account)",
            "Create a listing on Furnished Finder for medium-term medical stays",
            "Contact PlacidWay about their accommodation partner program",
            "Contact Bookimed about listing as a recommended recovery stay",
            "Identify WhatClinic-listed dental clinics in Tirana and reach out for referral partnerships",
        ],
    })

    # ── Issue 9: 100% Platform Dependency Risk ───────────────────────────────
    issues.append({
        "severity": "CRITICAL",
        "area": "100% Platform Dependency — Single Point of Failure",
        "finding": (
            "Your entire business depends on Airbnb and Booking.com. If either platform changes its "
            "algorithm, raises fees, suspends your listing, or changes guest-facing policies, "
            "you lose 50-100% of your revenue overnight with no fallback. You own zero guest relationships — "
            "Airbnb owns them. You have no direct booking channel, no email list, no social media following, "
            "and no organic search presence."
        ),
        "recommendation": (
            "Build a diversified acquisition strategy with 4 layers: "
            "(1) Platforms (current: Airbnb + Booking.com — keep these as your acquisition engine). "
            "(2) Organic presence (Google Business Profile + social media + YouTube — free, builds over time). "
            "(3) Direct bookings (simple website + email marketing — eliminates platform fees on repeat guests). "
            "(4) Paid acquisition (Google + Facebook Ads — scalable, sends traffic to direct booking page). "
            "Target: within 18 months, no single channel should represent more than 50% of bookings."
        ),
        "what_others_do": (
            "Resilient short-term rental businesses derive revenue from 3-5 channels. "
            "Industry best practice is: 40-50% from platforms (Airbnb/Booking.com), "
            "20-30% from direct bookings, 15-20% from organic (SEO/social), "
            "and 10-15% from paid ads and referral partnerships."
        ),
        "action_items": [
            "Week 1: Set up Google Business Profile (free, 30 minutes)",
            "Week 2: Create Instagram and TikTok accounts, post first 3 videos",
            "Week 3: Build a simple direct booking page on Carrd (€19/year)",
            "Week 4: Set up StayFi for email capture",
            "Month 2: Launch Google Ads at €5/day targeting dental tourism keywords",
            "Month 3: Start email drip sequence to captured guest emails",
            "Month 6: Evaluate channel mix — aim for 20%+ from non-platform sources",
            "Month 18: Target no single channel representing more than 50% of bookings",
        ],
    })

    # ── Issue 10: No TikTok Search Ads (2025 Beta Opportunity) ───────────────
    issues.append({
        "severity": "LOW",
        "area": "TikTok Search Ads — Early Adopter Opportunity",
        "finding": (
            "TikTok launched Search Ads in 2025 (still in beta), allowing advertisers to bid on "
            "high-intent search keywords within TikTok. CPCs are currently lower than Google Ads "
            "because few advertisers are using them yet. With 71% of European TikTok users willing "
            "to book based on TikTok content, this is an emerging channel for travel accommodation."
        ),
        "recommendation": (
            "This is a future opportunity — not a priority today. Once you have an active TikTok "
            "presence and a direct booking page, experiment with TikTok Search Ads targeting "
            "'Tirana accommodation', 'dental tourism Albania', and 'Albania travel'. "
            "Early adopters on new ad platforms typically enjoy lower CPCs before competition increases."
        ),
        "what_others_do": (
            "Early adopter travel brands are testing TikTok Search Ads and reporting CPCs 40-60% lower "
            "than Google Ads. This channel is too new for most hosts to use, but the window of low competition "
            "will close as the platform matures."
        ),
        "action_items": [
            "Bookmark TikTok Ads Manager for future use",
            "Build your organic TikTok presence first (prerequisite for effective ads)",
            "Once you have 20+ TikTok videos and a direct booking page, test a €3/day TikTok Search Ads campaign",
        ],
    })

    return issues


def calculate_revenue_impact():
    """Estimate the revenue impact of implementing digital presence strategies."""
    current_annual_eur = 6500
    platform_fees_saved = current_annual_eur * 0.155  # 15.5% of revenue shifted to direct

    projections = {
        "current_annual_revenue_eur": current_annual_eur,
        "current_annual_platform_fees_eur": round(current_annual_eur * 0.155),
        "scenario_18_months": {
            "direct_booking_share_pct": 30,
            "direct_booking_revenue_eur": round(current_annual_eur * 0.30),
            "fees_saved_on_direct_eur": round(current_annual_eur * 0.30 * 0.155),
            "additional_bookings_from_ads_eur": round(4 * 45 * 3 * 12),  # 4 extra bookings/month, 3-night avg
            "additional_bookings_from_social_eur": round(2 * 45 * 3 * 12),  # 2 extra bookings/month from social
            "total_estimated_revenue_eur": round(
                current_annual_eur
                + (current_annual_eur * 0.30 * 0.155)  # fee savings
                + (4 * 45 * 3 * 12)  # ads
                + (2 * 45 * 3 * 12)  # social
            ),
            "costs": {
                "carrd_website_eur": 19,
                "stayfi_eur": 120,
                "google_ads_eur": 1800,  # €150/month
                "facebook_ads_eur": 1200,  # €100/month
                "total_costs_eur": 3139,
            },
        },
    }

    net_gain = (
        projections["scenario_18_months"]["total_estimated_revenue_eur"]
        - current_annual_eur
        - projections["scenario_18_months"]["costs"]["total_costs_eur"]
    )
    projections["scenario_18_months"]["net_gain_eur"] = net_gain
    projections["scenario_18_months"]["roi_pct"] = round(
        (net_gain / projections["scenario_18_months"]["costs"]["total_costs_eur"]) * 100
    )

    return projections


def run():
    """Main skill entry point."""
    gaps = analyze_digital_gaps()
    issues = identify_issues()
    revenue_impact = calculate_revenue_impact()

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "digital_gap_analysis": gaps,
        "social_media_data": SOCIAL_MEDIA_DATA,
        "direct_booking_data": DIRECT_BOOKING_DATA,
        "google_business_profile_data": GOOGLE_BUSINESS_PROFILE_DATA,
        "paid_ads_data": PAID_ADS_DATA,
        "email_marketing_data": EMAIL_MARKETING_DATA,
        "content_marketing_data": CONTENT_MARKETING_DATA,
        "medical_tourism_platforms_data": MEDICAL_TOURISM_PLATFORMS_DATA,
        "your_digital_presence": YOUR_DIGITAL_PRESENCE,
        "revenue_impact": revenue_impact,
        "issues": issues,
        "issues_count": len(issues),
    }

    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  DIGITAL PRESENCE GAP ANALYSIS:")
    print(f"    Active channels:    {gaps['channels_active']} (Airbnb + Booking.com)")
    print(f"    Missing channels:   {gaps['channels_missing']}")
    print(f"    Platform dependency: {gaps['platform_dependency_pct']}%")
    print(f"    Risk level:         {gaps['risk_level']}")
    print(f"\n  CURRENT STATE:")
    print(f"    Social media:           NONE")
    print(f"    Direct booking website: NONE")
    print(f"    Google Business Profile: NONE")
    print(f"    Paid ads:               NONE")
    print(f"    Email marketing:        NONE")
    print(f"    Content/blog:           NONE")
    print(f"    Medical tourism sites:  NONE")
    print(f"\n  REVENUE IMPACT (18-month projection):")
    s = revenue_impact["scenario_18_months"]
    print(f"    Current annual:     €{revenue_impact['current_annual_revenue_eur']:,}")
    print(f"    Projected annual:   €{s['total_estimated_revenue_eur']:,}")
    print(f"    Implementation cost: €{s['costs']['total_costs_eur']:,}/year")
    print(f"    Net gain:           €{s['net_gain_eur']:,}/year")
    print(f"    ROI:                {s['roi_pct']}%")
    print(f"\n  ISSUES FOUND: {len(issues)}")
    for i, issue in enumerate(issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area']}")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
