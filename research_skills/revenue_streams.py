"""
Skill: Revenue Streams
Researches revenue maximization tactics — upsells, add-ons, direct bookings,
multi-platform distribution, email marketing, ancillary revenue, and experience
packages — then compares against your property's current state.
"""

import sys
from pathlib import Path

SKILL_NAME = "revenue_streams"
DESCRIPTION = "Revenue maximization: upsells, direct bookings, multi-platform, ancillary income"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# --- Researched Revenue Data (Feb 2026) -------------------------------------------

UPSELL_DATA = {
    "industry_stats": {
        "travelers_who_purchase_extras_pct": 83,
        "accommodation_share_of_trip_budget_pct": 30,
        "experiences_share_of_trip_budget_pct": 70,
        "upsell_sweet_spot_days_before_arrival": "7-14",
        "revenue_uplift_range_pct": "8-30%",
        "revenue_per_booking_range_usd": "$40-285",
        "experienced_host_additional_per_booking_usd": "85-150",
    },
    "case_study": {
        "source": "SuiteOp",
        "new_revenue_30_days_usd": 11_500,
        "projected_annual_usd": 138_000,
    },
    "upsell_menu": {
        "early_checkin_late_checkout": {
            "price_per_hour_usd": "10-20",
            "notes": "Biggest revenue driver among all upsells. At least $100/month extra.",
            "inventory_cost": "Zero (flexibility-based)",
        },
        "airport_transfers": {
            "pricing_strategy": "50-60% of standard taxi fare",
            "inventory_cost": "Zero (partner with local driver)",
            "notes": "High perceived value, no upfront investment.",
        },
        "grocery_stocking": {
            "markup_on_cost_pct": "25-40%",
            "notes": "Guest sends list, you shop and deliver before arrival.",
        },
        "mid_stay_cleaning": {
            "price_usd": "30-60",
            "discount_vs_full_turnover_pct": "30-50%",
            "opt_in_rate": "1 in 3 guests",
            "notes": "Especially popular for stays 4+ nights.",
        },
        "welcome_baskets": {
            "price_rule": "5-10% of nightly rate",
            "price_range_usd": "15-30",
            "notes": "Local products (raki, Turkish delight, coffee) add authenticity.",
        },
        "luggage_storage": {
            "price_per_bag_per_24h_usd": 5.90,
            "notes": "For guests with late flights after checkout.",
        },
    },
}

DIRECT_BOOKING_DATA = {
    "platform_fees": {
        "airbnb_total_fee_pct": 15.5,
        "airbnb_fee_note": "Changed late 2025 — host-only model now 15.5% total",
        "booking_com_avg_fee_pct": 15,
    },
    "strategy": {
        "acquisition_channel": "Airbnb / Booking.com (visibility, trust, reviews)",
        "retention_channel": "Direct booking website (no commission, guest relationship)",
        "principle": "Use OTAs to ACQUIRE new guests, direct to RETAIN returning guests",
    },
    "tools": {
        "hospitable": {"price_per_month_usd": 29, "notes": "Messaging + direct booking site"},
        "ownerrez": {"price_per_month_usd": 40, "notes": "Full PMS with direct booking engine"},
        "lodgify": {"price_per_month_usd": "140-400", "notes": "Website builder + booking engine"},
    },
    "email_capture": {
        "tool": "StayFi",
        "method": "WiFi captive portal — guest enters email to access WiFi",
        "case_study_1": "One property went from 0% to 30% direct bookings in 1.5 years",
        "case_study_2": "Another drove $35K in direct bookings in 6 months",
    },
    "conversion_stats": {
        "welcome_email_open_rate_pct": 60,
        "post_booking_page_conversion_pct": "15-20%",
    },
}

MULTI_PLATFORM_DATA = {
    "platform_shares": {
        "airbnb": {"market_share_pct": 43, "fee_pct": 15.5},
        "booking_com": {"market_share_pct": 8, "fee_pct": 15},
        "vrbo": {"market_share_pct": 21, "fee_pct": 8},
    },
    "channel_manager_impact": {
        "occupancy_increase_pct": "10-35%",
        "manual_work_reduction_pct": 40,
    },
    "channel_manager_tools": [
        "Hostaway", "Hospitable", "Guesty", "Lodgify", "Smoobu",
    ],
    "pricing_strategy": "Price 5-7% higher on higher-fee platforms to offset commission",
}

EMAIL_MARKETING_DATA = {
    "post_stay_sequence": [
        {"timing": "Day 1 after checkout", "content": "Thank you + review request"},
        {"timing": "30 days later", "content": "Special returning guest discount (10-15% off)"},
        {"timing": "90 days later", "content": "Plan your next trip + seasonal highlights"},
        {"timing": "6 months later", "content": "Win-back offer — exclusive rate"},
        {"timing": "Seasonal triggers", "content": "Summer/holiday promotions"},
    ],
    "open_rates": {
        "welcome_email_pct": 60,
        "regular_email_pct": "25-35%",
    },
    "newsletter_content": [
        "Local events and festivals in Tirana",
        "Property updates and improvements",
        "Exclusive returning-guest offers",
        "Guest stories and testimonials",
    ],
    "status": "Most overlooked revenue driver in short-term rentals",
}

ANCILLARY_REVENUE_DATA = {
    "partnership_types": {
        "tour_operators": {"referral_commission_pct": "10-20%"},
        "car_rental": {"model": "Affiliate referral commission"},
        "restaurants": {"model": "Dining credit partnerships — negotiate 10-15% referral fee"},
        "equipment_rentals": {"examples": "Bikes, baby gear, ski equipment", "model": "Revenue share or markup"},
    },
    "industry_stats": {
        "property_managers_with_diversified_revenue_pct": 55,
        "ancillary_projected_share_of_net_profit_by_2026_pct": 20,
    },
}

EXPERIENCE_PACKAGES = {
    "romance_honeymoon": {
        "markup_pct": "30-50%",
        "includes": ["Champagne on arrival", "Flower arrangement", "Late checkout", "Massage referral"],
        "target": "Couples, anniversaries, honeymoons",
    },
    "work_from_anywhere": {
        "markup_pct": "10-20%",
        "includes": ["Fast internet guarantee (speed test in listing)", "Ergonomic workspace", "Coffee subscription", "Quiet hours policy"],
        "target": "Remote workers, digital nomads (growing segment in Tirana)",
    },
    "medical_recovery": {
        "pricing": "Custom (weekly rates, 20-40% above base)",
        "includes": ["Ice packs and recovery supplies", "Blender for soft food", "Clinic transport coordination", "Recovery guide with local pharmacy info"],
        "target": "Dental and cosmetic surgery patients (80,000/year in Albania)",
    },
    "airbnb_experiences": {
        "price_range_per_person_usd": "10-500+",
        "airbnb_commission_pct": 20,
        "notes": "Can host or partner with local guides. Walking tours, cooking classes, wine tastings.",
    },
}

# --- Your Property's Current State -----------------------------------------------

YOUR_PROPERTY = {
    "name": "Lulebore Apartment 1",
    "location": "Central Tirana",
    "nightly_rate_eur": 45,
    "platforms": ["Airbnb", "Booking.com"],
    "platform_count": 2,
    "has_upsells": False,
    "upsell_list": [],
    "has_direct_booking_website": False,
    "has_email_capture": False,
    "has_email_marketing": False,
    "has_airport_transfer": False,
    "has_experience_packages": False,
    "has_ancillary_partnerships": False,
    "has_channel_manager": False,
    "estimated_monthly_revenue_eur": 540,
    "estimated_annual_revenue_eur": 6570,
}


# --- Analysis Functions -----------------------------------------------------------

def analyze_upsell_gap():
    """Identify missed upsell revenue opportunities."""
    issues = []
    you = YOUR_PROPERTY

    if not you["has_upsells"]:
        # Calculate potential upsell revenue at the property's price point
        # Conservative: $85/booking * estimated 12 bookings/month = $1,020/month
        monthly_bookings_est = 12  # ~2.5 night avg stay at 40% occupancy
        conservative_per_booking = 85
        aggressive_per_booking = 150
        monthly_low = monthly_bookings_est * conservative_per_booking
        monthly_high = monthly_bookings_est * aggressive_per_booking

        issues.append({
            "severity": "HIGH",
            "area": "Zero Upsell Revenue — Leaving $1,000-1,800/month on the Table",
            "finding": (
                f"You offer zero upsells. 83% of travelers purchase extras, and accommodation "
                f"accounts for only 30% of a guest's trip budget — the other 70% goes to "
                f"experiences and services. Experienced hosts earn $85-150 additional per booking "
                f"from upsells alone. At ~{monthly_bookings_est} bookings/month, you're missing "
                f"an estimated ${monthly_low:,}-${monthly_high:,}/month in upsell revenue."
            ),
            "recommendation": (
                "Implement a 6-item upsell menu immediately. Start with the three highest-ROI, "
                "zero-inventory-cost options:\n"
                "  1. Early check-in / late checkout: $10-20/hour (biggest driver, $100+/month alone)\n"
                "  2. Airport transfers: price at 50-60% of standard taxi (partner with a driver)\n"
                "  3. Mid-stay cleaning: $30-60 per clean (1 in 3 guests opts in)\n"
                "Then add grocery stocking (25-40% markup), welcome baskets ($15-30), and "
                "luggage storage ($5.90/bag/24h). Send the upsell menu 7-14 days before arrival "
                "— this is the proven sweet spot for conversion."
            ),
            "what_others_do": (
                "SuiteOp case study: one property portfolio generated $11,500 in new upsell revenue "
                "in just 30 days (projected $138K/year). Top hosts build upsells into their automated "
                "pre-arrival messaging sequence."
            ),
            "potential_monthly_revenue_usd": f"${monthly_low:,}-${monthly_high:,}",
        })

    return issues


def analyze_direct_booking_gap():
    """Identify direct booking and email capture opportunities."""
    issues = []
    you = YOUR_PROPERTY

    if not you["has_direct_booking_website"]:
        # At 15.5% Airbnb fee on €45/night, that's ~€7/night going to platform
        fee_per_night = you["nightly_rate_eur"] * 0.155
        nights_per_month_est = 12  # 40% of 30 nights
        monthly_fees_lost = fee_per_night * nights_per_month_est
        annual_fees_lost = monthly_fees_lost * 12

        issues.append({
            "severity": "HIGH",
            "area": "No Direct Booking Channel — Paying €{:,.0f}/year in Avoidable Commissions".format(annual_fees_lost),
            "finding": (
                f"Every booking through Airbnb costs you 15.5% (€{fee_per_night:.1f}/night). "
                f"With Booking.com averaging 15%, you're paying ~€{monthly_fees_lost:.0f}/month "
                f"(~€{annual_fees_lost:,.0f}/year) in platform commissions with no path to reduce them. "
                f"You have no direct booking website, meaning every single guest must come through "
                f"a commission-charging platform."
            ),
            "recommendation": (
                "Set up a direct booking website using Hospitable ($29/month) or OwnerRez ($40/month). "
                "Use Airbnb as your ACQUISITION channel (to get new guests) and your direct site as "
                "your RETENTION channel (to bring them back commission-free). Even converting 20-30% "
                "of repeat guests to direct would save €{:,.0f}-€{:,.0f}/year in fees.".format(
                    annual_fees_lost * 0.20, annual_fees_lost * 0.30
                )
            ),
            "what_others_do": (
                "Smart hosts treat OTAs like advertising: pay the commission once to acquire the guest, "
                "then redirect them to direct booking for all future stays. One StayFi user went from "
                "0% to 30% direct bookings in just 1.5 years."
            ),
            "annual_commission_savings_potential_eur": round(annual_fees_lost * 0.30),
        })

    if not you["has_email_capture"]:
        issues.append({
            "severity": "HIGH",
            "area": "No Email Capture — Losing Every Guest Relationship After Checkout",
            "finding": (
                "You have no email capture mechanism. Every guest who stays checks out and disappears "
                "into Airbnb's ecosystem — you cannot contact them directly, cannot offer returning-guest "
                "discounts, and cannot build a guest database. Without email capture, you're permanently "
                "dependent on platforms and permanently paying full commission."
            ),
            "recommendation": (
                "Install StayFi or a similar WiFi captive portal: guests enter their email to access "
                "WiFi. This captures emails passively with zero friction. Welcome emails achieve 60%+ "
                "open rates. Post-booking landing pages convert at 15-20%. A property using StayFi "
                "drove $35,000 in direct bookings within 6 months. Cost: ~$10-20/month for a single "
                "property. ROI is enormous."
            ),
            "what_others_do": (
                "Professional hosts capture 80-90% of guest emails through WiFi portals and use "
                "automated post-stay sequences to drive repeat direct bookings. The guest's email "
                "is the single most valuable asset in short-term rental — more valuable than any "
                "single booking."
            ),
        })

    return issues


def analyze_email_marketing_gap():
    """Identify email marketing automation opportunities."""
    issues = []
    you = YOUR_PROPERTY

    if not you["has_email_marketing"]:
        issues.append({
            "severity": "HIGH",
            "area": "No Email Marketing — The Most Overlooked Revenue Driver",
            "finding": (
                "You have no post-stay email sequence and no newsletter. Email marketing is the "
                "most overlooked revenue driver in short-term rentals. Welcome emails achieve 60%+ "
                "open rates (vs 25-35% for regular email). You're missing the entire retention "
                "funnel: no thank-you emails, no returning-guest discounts, no seasonal promotions, "
                "no win-back campaigns."
            ),
            "recommendation": (
                "Build a 5-step automated post-stay email sequence:\n"
                "  1. Day 1 after checkout: Thank you + review request\n"
                "  2. 30 days later: 'Special returning guest discount' (10-15% off direct)\n"
                "  3. 90 days later: 'Plan your next Tirana trip' + seasonal highlights\n"
                "  4. 6 months later: Win-back offer with exclusive rate\n"
                "  5. Seasonal triggers: Summer/holiday promotions\n"
                "Also send a monthly newsletter: local Tirana events, property updates, exclusive "
                "offers, and guest stories. Free tools: Mailchimp (up to 500 contacts free), "
                "MailerLite (up to 1,000 contacts free)."
            ),
            "what_others_do": (
                "Top hosts report that their email list generates 15-25% of annual revenue through "
                "repeat direct bookings. A guest who books twice directly saves you 2x the platform "
                "commission and has a higher lifetime value."
            ),
        })

    return issues


def analyze_multi_platform_gap():
    """Identify multi-platform distribution opportunities."""
    issues = []
    you = YOUR_PROPERTY

    # Already on 2 platforms, but missing Vrbo and no channel manager
    if not you["has_channel_manager"]:
        issues.append({
            "severity": "MEDIUM",
            "area": "No Channel Manager — Manual Sync Risk and Missing Vrbo (21% Market Share)",
            "finding": (
                f"You're on {you['platform_count']} platforms (Airbnb + Booking.com) but have no channel "
                f"manager. Manual calendar sync risks double bookings and costs time. You're also "
                f"missing Vrbo, which holds 21% market share and charges only 8% commission — nearly "
                f"half of Airbnb's 15.5%. Channel managers increase occupancy by 10-35% and reduce "
                f"manual work by 40%."
            ),
            "recommendation": (
                "Add Vrbo to your distribution (8% fee vs 15.5% on Airbnb). Use a channel manager "
                "like Hospitable ($29/month — which also provides direct booking capability) or "
                "Smoobu to sync calendars automatically. Price your listing 5-7% higher on Airbnb "
                "and Booking.com to offset their higher commissions, while keeping Vrbo and direct "
                "at your base rate."
            ),
            "what_others_do": (
                "Professional hosts list on 3-5 platforms with a channel manager and use differential "
                "pricing: base rate on low-fee platforms, marked-up rate on high-fee platforms. "
                "This neutralizes commission impact while maximizing exposure."
            ),
        })

    return issues


def analyze_ancillary_gap():
    """Identify ancillary revenue and partnership opportunities."""
    issues = []
    you = YOUR_PROPERTY

    if not you["has_ancillary_partnerships"]:
        issues.append({
            "severity": "MEDIUM",
            "area": "No Ancillary Revenue Partnerships — Missing 10-20% Referral Income",
            "finding": (
                "You have no referral partnerships with tour operators, car rentals, restaurants, "
                "or equipment rental companies. 55% of property managers already have diversified "
                "revenue streams. Ancillary revenue is projected to represent ~20% of net profit "
                "margins by 2026. You're leaving easy, passive referral income untouched."
            ),
            "recommendation": (
                "Build 4 local partnerships in Tirana:\n"
                "  1. Tour operator: walking tours, day trips to Berat/Kruja — earn 10-20% referral fee\n"
                "  2. Car rental: partner with a local agency for airport pickup + rental — affiliate commission\n"
                "  3. Restaurants: negotiate 10-15% referral fee for recommended dining (create a curated list)\n"
                "  4. Equipment: bike rentals, baby gear — revenue share model\n"
                "Add a 'Local Recommendations' digital guidebook with your affiliate links. "
                "Guest gets great tips, you earn passive income on every referral."
            ),
            "what_others_do": (
                "Top hosts create branded digital guidebooks (using Touchstay or Hostfully) with "
                "embedded referral links. Every restaurant recommendation, every tour suggestion "
                "earns them a commission — turning their local knowledge into revenue."
            ),
        })

    if not you["has_airport_transfer"]:
        issues.append({
            "severity": "MEDIUM",
            "area": "No Airport Transfer Service — High-Demand, Zero-Cost Revenue",
            "finding": (
                "You don't offer airport transfers. This is one of the most requested services "
                "by international travelers (87.55% of Tirana Airbnb guests are international). "
                "It requires zero inventory cost — you simply partner with a reliable local driver "
                "and price at 50-60% of the standard taxi fare."
            ),
            "recommendation": (
                "Partner with 1-2 reliable drivers in Tirana. Negotiate a wholesale rate and price "
                "your transfer at 50-60% of standard taxi fare (perceived value is high because guests "
                "avoid the stress of negotiating with taxi drivers at TIA). Offer it in your pre-arrival "
                "upsell message 7-14 days before check-in. Include the service in your medical recovery "
                "and romance packages."
            ),
            "what_others_do": (
                "Almost every top-rated Airbnb in tourist destinations offers airport transfers. "
                "It's the single most common upsell — high conversion, zero risk, and it creates "
                "a premium first impression."
            ),
        })

    return issues


def analyze_experience_packages_gap():
    """Identify experience package opportunities."""
    issues = []
    you = YOUR_PROPERTY

    if not you["has_experience_packages"]:
        issues.append({
            "severity": "MEDIUM",
            "area": "No Experience Packages — Missing 10-50% Premium Pricing Opportunity",
            "finding": (
                "You offer no themed experience packages. Packages allow you to charge 10-50% "
                "above your base rate by bundling your accommodation with curated extras. "
                "Three packages are especially relevant to central Tirana:\n"
                "  - Romance/Honeymoon: +30-50% markup (champagne, flowers, late checkout, massage referral)\n"
                "  - Work-From-Anywhere: +10-20% markup (fast WiFi guarantee, ergonomic workspace)\n"
                "  - Medical Recovery: custom pricing (80,000 medical tourists/year in Albania)"
            ),
            "recommendation": (
                "Create 3 bookable packages on your direct booking site:\n"
                "  1. ROMANCE PACKAGE (€65-70/night): Champagne, flowers, late checkout, massage referral. "
                "Target couples via listing keywords and Airbnb categories.\n"
                "  2. DIGITAL NOMAD PACKAGE (€50-55/night): Speed test screenshot in listing, desk photo, "
                "coffee subscription, quiet hours guarantee. Weekly rate with 15% discount.\n"
                "  3. MEDICAL RECOVERY PACKAGE (€55-65/night, weekly rates): Ice packs, blender for soft "
                "food, clinic transport, recovery guide. Market directly to dental/cosmetic clinics.\n"
                "Each package costs you €5-15 in supplies but commands €10-25+ in premium pricing."
            ),
            "what_others_do": (
                "In mature markets, themed packages are standard. Airbnb Experiences ($10-500+/person, "
                "20% Airbnb commission) are another revenue channel — you could partner with a local guide "
                "to offer walking tours of Tirana's Blloku district or Ottoman-era landmarks."
            ),
        })

    return issues


def calculate_total_revenue_opportunity():
    """Estimate total additional revenue from all gaps."""
    you = YOUR_PROPERTY
    current_annual = you["estimated_annual_revenue_eur"]

    opportunities = {
        "upsells": {
            "monthly_low_usd": 1_020,
            "monthly_high_usd": 1_800,
            "description": "Upsell menu (early check-in, transfers, cleaning, baskets, storage, groceries)",
        },
        "commission_savings": {
            "monthly_low_eur": round(you["nightly_rate_eur"] * 0.155 * 12 * 0.20),  # 20% direct
            "monthly_high_eur": round(you["nightly_rate_eur"] * 0.155 * 12 * 0.30),  # 30% direct
            "description": "Commission savings from 20-30% direct booking conversion",
        },
        "experience_packages": {
            "monthly_low_eur": 50,
            "monthly_high_eur": 200,
            "description": "Premium pricing from romance, digital nomad, and medical packages",
        },
        "ancillary_referrals": {
            "monthly_low_eur": 30,
            "monthly_high_eur": 100,
            "description": "Tour, restaurant, car rental, and equipment referral commissions",
        },
        "multi_platform_occupancy": {
            "monthly_low_eur": round(current_annual / 12 * 0.10),  # 10% occupancy boost
            "monthly_high_eur": round(current_annual / 12 * 0.20),  # 20% occupancy boost
            "description": "Occupancy increase from adding Vrbo + channel manager",
        },
    }

    return opportunities


def run():
    """Main skill entry point."""
    all_issues = []
    all_issues.extend(analyze_upsell_gap())
    all_issues.extend(analyze_direct_booking_gap())
    all_issues.extend(analyze_email_marketing_gap())
    all_issues.extend(analyze_multi_platform_gap())
    all_issues.extend(analyze_ancillary_gap())
    all_issues.extend(analyze_experience_packages_gap())

    revenue_opportunity = calculate_total_revenue_opportunity()

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "upsell_data": UPSELL_DATA,
        "direct_booking_data": DIRECT_BOOKING_DATA,
        "multi_platform_data": MULTI_PLATFORM_DATA,
        "email_marketing_data": EMAIL_MARKETING_DATA,
        "ancillary_revenue_data": ANCILLARY_REVENUE_DATA,
        "experience_packages": EXPERIENCE_PACKAGES,
        "your_property": YOUR_PROPERTY,
        "revenue_opportunity": revenue_opportunity,
        "issues": all_issues,
        "issues_count": len(all_issues),
    }

    # --- Console Output ---
    high_count = sum(1 for i in all_issues if i["severity"] == "HIGH")
    medium_count = sum(1 for i in all_issues if i["severity"] == "MEDIUM")

    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  PROPERTY: {YOUR_PROPERTY['name']}")
    print(f"  Rate: EUR{YOUR_PROPERTY['nightly_rate_eur']}/night | Platforms: {YOUR_PROPERTY['platform_count']}")
    print(f"  Est. Revenue: EUR{YOUR_PROPERTY['estimated_monthly_revenue_eur']}/month | EUR{YOUR_PROPERTY['estimated_annual_revenue_eur']:,}/year")
    print(f"\n  CURRENT STATE:")
    print(f"    Upsells:              {'YES' if YOUR_PROPERTY['has_upsells'] else 'NONE'}")
    print(f"    Direct Booking Site:  {'YES' if YOUR_PROPERTY['has_direct_booking_website'] else 'NONE'}")
    print(f"    Email Capture:        {'YES' if YOUR_PROPERTY['has_email_capture'] else 'NONE'}")
    print(f"    Email Marketing:      {'YES' if YOUR_PROPERTY['has_email_marketing'] else 'NONE'}")
    print(f"    Airport Transfers:    {'YES' if YOUR_PROPERTY['has_airport_transfer'] else 'NONE'}")
    print(f"    Experience Packages:  {'YES' if YOUR_PROPERTY['has_experience_packages'] else 'NONE'}")
    print(f"    Ancillary Partners:   {'YES' if YOUR_PROPERTY['has_ancillary_partnerships'] else 'NONE'}")
    print(f"    Channel Manager:      {'YES' if YOUR_PROPERTY['has_channel_manager'] else 'NONE'}")
    print(f"\n  KEY INDUSTRY STATS:")
    print(f"    83% of travelers purchase extras")
    print(f"    Accommodation = only 30% of guest's trip budget")
    print(f"    Upsells add 8-30% to revenue ($40-285/booking)")
    print(f"    55% of property managers have diversified revenue")
    print(f"    Ancillary income projected at ~20% of net margins by 2026")
    print(f"\n  ISSUES FOUND: {len(all_issues)} ({high_count} HIGH, {medium_count} MEDIUM)")
    for i, issue in enumerate(all_issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area']}")
    print(f"\n  REVENUE OPPORTUNITY SUMMARY:")
    for key, opp in revenue_opportunity.items():
        print(f"    - {opp['description']}")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
