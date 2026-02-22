"""
Skill: Pricing Mastery
Researches advanced pricing strategies that successful Albanian Airbnb hosts use
— dynamic pricing tools, seasonal adjustments, length-of-stay discounts, rating-adjusted
pricing, clinic referral models, and direct booking savings — then compares each against
Lulebore Apartment 1's current static-pricing setup.
"""

import sys
from pathlib import Path

SKILL_NAME = "pricing_mastery"
DESCRIPTION = "Advanced pricing strategies: dynamic pricing, seasonal, discounts, clinic referrals, and direct bookings"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# --- Researched Pricing Data (Feb 2026) -----------------------------------------------

DYNAMIC_PRICING_DATA = {
    "study_listing_count": 541,
    "study_revenue_increase_pct": 36,
    "tool_revenue_increase_range_pct": "20-40",
    "tools": {
        "pricelabs": {
            "cost": "$19.99/listing/month (flat fee)",
            "strength": "Most granular control, best for individual hosts",
            "pricing_model": "flat_fee",
            "monthly_usd": 19.99,
        },
        "beyond_pricing": {
            "cost": "1% of revenue",
            "strength": "Good for larger portfolios, hands-off",
            "pricing_model": "revenue_share",
            "pct_of_revenue": 1.0,
        },
        "wheelhouse": {
            "cost": "$19.99/month OR 1% revenue OR free manual tier",
            "strength": "Flexible pricing options, free tier available",
            "pricing_model": "hybrid",
            "monthly_usd_option": 19.99,
            "pct_option": 1.0,
        },
        "airbnb_smart_pricing": {
            "cost": "Free",
            "strength": "Built-in, zero cost",
            "warning": "UNDERPRICES listings — optimizes for Airbnb booking volume, NOT host revenue",
            "pricing_model": "free",
        },
    },
    "case_study": {
        "original_static_rate_usd": 159,
        "switched_to": "dynamic pricing",
        "period_days": 90,
        "revenue_increase_pct": 31.1,
        "extra_revenue_usd": 3564,
        "tool_cost_usd": 59.97,
        "roi_multiplier": round(3564 / 59.97, 0),
    },
}

SEASONAL_STRATEGY_TIRANA = {
    "peak": {
        "months": ["June", "July", "August", "September"],
        "rate_range_eur": "55-63",
        "rate_low_eur": 55,
        "rate_high_eur": 63,
        "occupancy_pct_range": "49-52",
    },
    "shoulder": {
        "months": ["April", "May", "October"],
        "rate_range_eur": "45-50",
        "rate_low_eur": 45,
        "rate_high_eur": 50,
    },
    "off_season": {
        "months": ["November", "December", "January", "February", "March"],
        "rate_range_eur": "35-43",
        "rate_low_eur": 35,
        "rate_high_eur": 43,
        "occupancy_pct": 35,
    },
    "event_premiums": ["Christmas", "New Year", "Independence Day (Nov 28)", "Summer Day (Mar 14)"],
    "tirana_swing": "1.5-2x (mild vs coastal 5-7x)",
}

LENGTH_OF_STAY_DISCOUNTS = {
    "weekly": {
        "threshold_nights": 7,
        "discount_pct_range": "10-15",
        "discount_pct_low": 10,
        "discount_pct_high": 15,
        "target_guest": "Digital nomads, medical tourists",
        "benefit": "Reduces turnover costs, guaranteed income block",
    },
    "monthly": {
        "threshold_nights": 28,
        "discount_pct_range": "20-30",
        "discount_pct_low": 20,
        "discount_pct_high": 30,
        "target_guest": "Long-term remote workers, relocations",
        "market_fact": "28+ day stays account for 20% of all Airbnb bookings globally",
    },
    "last_minute": {
        "within_days": 7,
        "discount_pct_range": "15-27",
        "discount_pct_low": 15,
        "discount_pct_high": 27,
        "target_guest": "Spontaneous travelers, gap-fillers",
        "benefit": "Fills gaps that would otherwise earn zero",
    },
    "combined_results": {
        "occupancy_increase_pct": 11,
        "revenue_increase_pct": 9,
    },
}

RATING_ADJUSTED_PRICING = {
    "tirana_percentiles": {
        "top_25_pct_rate_usd": 58,
        "top_10_pct_rate_usd": 81,
    },
    "your_ratings": {
        "airbnb": 4.88,
        "booking_com": 10.0,
        "percentile_estimate": "top 5% by rating",
    },
    "top_rated_premium_pct": "15-25",
    "rating_adjusted_fair_rate_eur": "55-57",
}

REVENUE_PROJECTIONS = {
    "current": {
        "label": "Current (static EUR45, ~40% occupancy)",
        "nightly_eur": 45,
        "occupancy_pct": 40,
        "monthly_eur": round(45 * 30 * 0.40),
    },
    "with_dynamic_pricing": {
        "label": "Add dynamic pricing (+30% revenue)",
        "monthly_eur": round(45 * 30 * 0.40 * 1.30),
    },
    "with_rate_increase_and_dynamic": {
        "label": "Raise to EUR55 + dynamic pricing",
        "nightly_eur": 55,
        "monthly_eur": round(55 * 30 * 0.40 * 1.30),
    },
    "with_50pct_occupancy": {
        "label": "EUR55 + 50% occupancy (multi-platform)",
        "nightly_eur": 55,
        "occupancy_pct": 50,
        "monthly_eur_low": round(55 * 30 * 0.50),
        "monthly_eur_high": round(55 * 30 * 0.50 * 1.30),
    },
    "top_10_tirana_benchmark_usd": 1400,
    "medical_stay_weekly": {
        "label": "Medical stay: 7 nights at 15% off",
        "calculation": "EUR45 x 7 x 0.85",
        "total_eur": round(45 * 7 * 0.85),
    },
    "medical_stay_2_week": {
        "label": "Medical stay: 14 nights at 20% off",
        "calculation": "EUR45 x 14 x 0.80",
        "total_eur": round(45 * 14 * 0.80),
    },
}

CLINIC_REFERRAL_PRICING = {
    "commission_model": {
        "description": "Offer clinics 10-15% commission per night for each referred patient",
        "commission_pct_range": "10-15",
    },
    "wholesale_model": {
        "description": "Offer wholesale rate (20-30% below retail) for clinic-bundled packages",
        "discount_pct_range": "20-30",
    },
    "market_context": (
        "In Turkey, clinics bundle 3-5 night hotel stays into surgery packages. "
        "Albania has nobody doing this yet — first-mover advantage is wide open."
    ),
}

DIRECT_BOOKING_SAVINGS = {
    "airbnb_commission_pct": 15.5,
    "airbnb_commission_note": "Changed late 2025 (was ~14-16% split host/guest)",
    "example_at_50k_revenue": {
        "annual_revenue_usd": 50000,
        "airbnb_fees_usd": 7750,
        "stripe_processing_usd": 1450,
        "annual_savings_usd": 6300,
    },
    "guest_incentive": "Offer 10% discount for direct booking — guest saves money, you still save ~5% vs Airbnb",
}


# --- Your Current Pricing Setup ---------------------------------------------------

YOUR_PRICING = {
    "nightly_rate_eur": 45,
    "pricing_type": "static",
    "dynamic_pricing_tool": None,
    "seasonal_adjustments": False,
    "weekly_discount": None,
    "monthly_discount": None,
    "last_minute_discount": None,
    "event_premiums": False,
    "clinic_referral_program": False,
    "direct_booking_site": False,
    "airbnb_rating": 4.88,
    "booking_com_rating": 10.0,
    "estimated_occupancy_pct": 40,
    "estimated_monthly_revenue_eur": round(45 * 30 * 0.40),
}


# --- Analysis Functions -----------------------------------------------------------

def analyze_dynamic_pricing_gap():
    """Compare static pricing against dynamic pricing benchmarks."""
    d = DYNAMIC_PRICING_DATA
    you = YOUR_PRICING
    current_monthly = you["estimated_monthly_revenue_eur"]

    # Revenue with dynamic pricing (conservative 30% lift)
    projected_monthly = round(current_monthly * 1.30)
    monthly_gain = projected_monthly - current_monthly
    annual_gain = monthly_gain * 12
    tool_annual_cost = round(d["tools"]["pricelabs"]["monthly_usd"] * 12)

    return {
        "severity": "CRITICAL",
        "area": "No Dynamic Pricing Tool",
        "finding": (
            f"You use static pricing (EUR{you['nightly_rate_eur']}/night, never changes). "
            f"A {d['study_listing_count']}-listing study found dynamic pricing increases revenue by "
            f"{d['study_revenue_increase_pct']}%. Tools typically deliver {d['tool_revenue_increase_range_pct']}% "
            f"revenue gains. One host switching from static $159 to dynamic saw a "
            f"{d['case_study']['revenue_increase_pct']}% revenue increase in {d['case_study']['period_days']} days "
            f"— ${d['case_study']['extra_revenue_usd']:,} extra vs ${d['case_study']['tool_cost_usd']:.2f} tool cost "
            f"(~{int(d['case_study']['roi_multiplier'])}x ROI)."
        ),
        "your_situation": (
            f"Current: EUR{current_monthly}/month. "
            f"With dynamic pricing (+30%): ~EUR{projected_monthly}/month (+EUR{monthly_gain}/month, +EUR{annual_gain}/year). "
            f"PriceLabs costs ${tool_annual_cost}/year — paying for itself in under 1 month."
        ),
        "recommendation": (
            "Sign up for PriceLabs ($19.99/month). It has the most granular control and is "
            "best for individual hosts. AVOID Airbnb Smart Pricing — it's free but systematically "
            "underprices your listing to maximize Airbnb's booking volume, not your revenue. "
            "Beyond Pricing (1% of revenue) is better for larger portfolios. "
            "Wheelhouse offers a free manual tier if you want to test first."
        ),
        "what_top_hosts_do": (
            "Top Albanian hosts use PriceLabs or Beyond Pricing. They adjust rates daily "
            "based on local demand, competitor pricing, events, and day-of-week patterns."
        ),
    }


def analyze_seasonal_strategy_gap():
    """Compare flat pricing against seasonal adjustments."""
    s = SEASONAL_STRATEGY_TIRANA
    you = YOUR_PRICING

    peak_midpoint = (s["peak"]["rate_low_eur"] + s["peak"]["rate_high_eur"]) / 2
    off_midpoint = (s["off_season"]["rate_low_eur"] + s["off_season"]["rate_high_eur"]) / 2
    peak_monthly = round(peak_midpoint * 30 * 0.50)
    off_monthly = round(off_midpoint * 30 * 0.35)
    your_monthly_always = you["estimated_monthly_revenue_eur"]

    return {
        "severity": "HIGH",
        "area": "No Seasonal Pricing Adjustments",
        "finding": (
            f"You charge EUR{you['nightly_rate_eur']}/night year-round. Tirana has clear seasonal patterns: "
            f"Peak (Jun-Sep) supports EUR{s['peak']['rate_range_eur']}/night at "
            f"{s['peak']['occupancy_pct_range']}% occupancy. "
            f"Shoulder (Apr-May, Oct) fits EUR{s['shoulder']['rate_range_eur']}/night. "
            f"Off-season (Nov-Mar) drops to EUR{s['off_season']['rate_range_eur']}/night at "
            f"{s['off_season']['occupancy_pct']}% occupancy. "
            f"The Tirana swing is mild ({s['tirana_swing']}) but still leaves money on the table "
            f"when ignored."
        ),
        "your_situation": (
            f"At a flat EUR{you['nightly_rate_eur']}, you're underpriced in peak season by EUR10-18/night "
            f"and overpriced in off-season (hurting occupancy). "
            f"Peak months could yield ~EUR{peak_monthly}/month vs your flat EUR{your_monthly_always}. "
            f"Off-season at EUR{off_midpoint:.0f}/night with better occupancy could match or beat "
            f"your flat-rate off-season earnings."
        ),
        "recommendation": (
            f"Implement a 3-tier seasonal calendar: "
            f"(1) Peak Jun-Sep: EUR55-63/night, "
            f"(2) Shoulder Apr-May, Oct: EUR45-50/night, "
            f"(3) Off-season Nov-Mar: EUR35-43/night. "
            f"Add event premiums for {', '.join(s['event_premiums'][:3])} etc. "
            f"A dynamic pricing tool automates this entirely."
        ),
        "what_top_hosts_do": (
            "Top Tirana hosts raise rates 20-40% in peak season and drop 10-20% in winter. "
            "They also add 1.5-2x premiums around Albanian holidays and major events."
        ),
    }


def analyze_length_of_stay_gap():
    """Compare no discounts against length-of-stay discount strategy."""
    d = LENGTH_OF_STAY_DISCOUNTS
    you = YOUR_PRICING
    rev = REVENUE_PROJECTIONS

    return {
        "severity": "HIGH",
        "area": "No Length-of-Stay Discounts",
        "finding": (
            f"You offer zero discounts for longer stays. "
            f"Hosts using length-of-stay discounts see an {d['combined_results']['occupancy_increase_pct']}% "
            f"occupancy rise and {d['combined_results']['revenue_increase_pct']}% revenue increase on average. "
            f"Monthly stays (28+ nights) account for 20% of all Airbnb bookings globally — "
            f"a huge segment you're invisible to because Airbnb's search filters favor listings "
            f"with weekly/monthly discounts."
        ),
        "your_situation": (
            f"Without discounts, you miss digital nomads searching for weekly deals and "
            f"medical tourists needing 1-2 week recovery stays. "
            f"A 7-night medical stay at 15% off: EUR{you['nightly_rate_eur']} x 7 x 0.85 = "
            f"EUR{rev['medical_stay_weekly']['total_eur']}/week (guaranteed block vs hoping for 7 separate bookings). "
            f"A 14-night medical stay at 20% off: EUR{you['nightly_rate_eur']} x 14 x 0.80 = "
            f"EUR{rev['medical_stay_2_week']['total_eur']}/2 weeks."
        ),
        "recommendation": (
            f"Set up 3 discount tiers immediately: "
            f"(1) Weekly (7+ nights): {d['weekly']['discount_pct_range']}% off — attracts digital nomads, "
            f"reduces turnover cleaning/laundry costs. "
            f"(2) Monthly (28+ nights): {d['monthly']['discount_pct_range']}% off — locks in reliable income. "
            f"(3) Last-minute (within {d['last_minute']['within_days']} days): "
            f"{d['last_minute']['discount_pct_range']}% off — fills gaps that would otherwise earn EUR0. "
            f"All three can be set directly in Airbnb's pricing settings in under 5 minutes."
        ),
        "what_top_hosts_do": (
            "Top Albanian hosts offer 10-15% weekly and 20-25% monthly discounts. "
            "They also use last-minute discounts (15-27% off) to fill gaps within 7 days. "
            "Medical-stay hosts specifically offer weekly packages at discounted rates."
        ),
    }


def analyze_rating_adjusted_pricing():
    """Assess whether the listing is priced appropriately for its rating."""
    r = RATING_ADJUSTED_PRICING
    you = YOUR_PRICING

    top25_eur = round(r["tirana_percentiles"]["top_25_pct_rate_usd"] * 0.92)
    top10_eur = round(r["tirana_percentiles"]["top_10_pct_rate_usd"] * 0.92)
    fair_rate = r["rating_adjusted_fair_rate_eur"]
    underpriced_by = 55 - you["nightly_rate_eur"]  # midpoint of 55-57

    monthly_at_55 = round(55 * 30 * 0.40)
    monthly_difference = monthly_at_55 - you["estimated_monthly_revenue_eur"]
    annual_difference = monthly_difference * 12

    return {
        "severity": "HIGH",
        "area": "Underpriced for Your Rating Quality",
        "finding": (
            f"Tirana top 25% listings charge ${r['tirana_percentiles']['top_25_pct_rate_usd']}+/night "
            f"(~EUR{top25_eur}+). Top 10% charge ${r['tirana_percentiles']['top_10_pct_rate_usd']}+/night "
            f"(~EUR{top10_eur}+). "
            f"With a {you['airbnb_rating']}/5 Airbnb rating and {you['booking_com_rating']}/10 on Booking.com, "
            f"you are in the {r['your_ratings']['percentile_estimate']}. "
            f"Top-rated properties can command {r['top_rated_premium_pct']}% above market average. "
            f"Rating-adjusted fair price for your property: EUR{fair_rate}/night."
        ),
        "your_situation": (
            f"At EUR{you['nightly_rate_eur']}/night, you're EUR{underpriced_by}/night below your "
            f"rating-adjusted fair value. That's EUR{monthly_difference}/month or "
            f"~EUR{annual_difference}/year left on the table — simply because your price doesn't "
            f"reflect your quality. Guests with high ratings have earned the right to charge premium rates."
        ),
        "recommendation": (
            f"Raise your base rate from EUR{you['nightly_rate_eur']} to EUR55-57/night. "
            f"At your rating level, this will NOT hurt occupancy — guests filter and sort by rating, "
            f"and a 4.88 listing at EUR55 looks like a bargain compared to a 4.5 listing at EUR50. "
            f"If anxious, raise by EUR5 increments (EUR45 -> EUR50 -> EUR55) over 2-4 weeks and "
            f"monitor booking pace."
        ),
        "what_top_hosts_do": (
            "Top-rated hosts (4.8+) in Tirana price 15-25% above average and still maintain "
            "strong occupancy. Their reviews justify the premium and create a quality signal "
            "that attracts higher-value guests."
        ),
    }


def analyze_revenue_potential():
    """Show the revenue ladder from current to optimized."""
    rev = REVENUE_PROJECTIONS
    you = YOUR_PRICING

    current = rev["current"]["monthly_eur"]
    with_dynamic = rev["with_dynamic_pricing"]["monthly_eur"]
    with_rate_dynamic = rev["with_rate_increase_and_dynamic"]["monthly_eur"]
    multi_low = rev["with_50pct_occupancy"]["monthly_eur_low"]
    multi_high = rev["with_50pct_occupancy"]["monthly_eur_high"]
    top10 = rev["top_10_tirana_benchmark_usd"]

    return {
        "severity": "CRITICAL",
        "area": "Revenue Optimization Roadmap",
        "finding": (
            f"Your current setup generates ~EUR{current}/month. Here's the revenue ladder:\n"
            f"  Level 1 — Add dynamic pricing (+30%):         EUR{with_dynamic}/month\n"
            f"  Level 2 — Raise to EUR55 + dynamic:           EUR{with_rate_dynamic}/month\n"
            f"  Level 3 — Multi-platform + 50% occupancy:     EUR{multi_low}-{multi_high}/month\n"
            f"  Top 10% Tirana benchmark:                     ~${top10}/month\n"
            f"Each level builds on the previous. Level 3 is achievable within 3-6 months "
            f"of implementing all strategies."
        ),
        "your_situation": (
            f"You are at EUR{current}/month — Level 0. The gap to top 10% is "
            f"~EUR{round(top10 * 0.92) - current}/month. Most of this gap is recoverable through "
            f"pricing changes alone (no property improvements needed). "
            f"Dynamic pricing + rate increase (Levels 1-2) require zero investment beyond a "
            f"$19.99/month tool subscription."
        ),
        "recommendation": (
            f"Implement in order: "
            f"(1) WEEK 1: Raise base rate to EUR50 (conservative first step). "
            f"(2) WEEK 2: Sign up for PriceLabs, enable dynamic pricing. "
            f"(3) WEEK 3: Set weekly/monthly discounts on all platforms. "
            f"(4) WEEK 4: Raise base rate to EUR55 if bookings held steady. "
            f"(5) MONTH 2: Add seasonal rules and event premiums. "
            f"Expected result: EUR{with_rate_dynamic}+/month within 60 days."
        ),
        "what_top_hosts_do": (
            "Top 10% Tirana hosts (~$1,400/month) combine dynamic pricing, seasonal adjustments, "
            "multi-platform distribution, length-of-stay discounts, and direct booking channels. "
            "No single tactic gets them there — it's the stack."
        ),
    }


def analyze_clinic_referral_pricing():
    """Evaluate the clinic referral pricing opportunity."""
    c = CLINIC_REFERRAL_PRICING
    you = YOUR_PRICING

    # Example: 4 referrals/month x 7 nights x EUR45
    example_nights_per_referral = 7
    example_referrals_per_month = 4
    gross_per_referral = you["nightly_rate_eur"] * example_nights_per_referral
    commission_15pct = round(gross_per_referral * 0.15)
    net_per_referral = gross_per_referral - commission_15pct
    monthly_from_referrals = net_per_referral * example_referrals_per_month

    wholesale_rate = round(you["nightly_rate_eur"] * 0.75)  # 25% below retail
    wholesale_weekly = wholesale_rate * example_nights_per_referral
    monthly_wholesale = wholesale_weekly * example_referrals_per_month

    return {
        "severity": "HIGH",
        "area": "No Clinic Referral Pricing Program",
        "finding": (
            f"You have no formal pricing arrangement with dental/medical clinics. "
            f"{c['market_context']} "
            f"Two models work: (1) Commission model — clinics earn {c['commission_model']['commission_pct_range']}% "
            f"per night for each referred patient. "
            f"(2) Wholesale model — offer {c['wholesale_model']['discount_pct_range']}% below retail for "
            f"clinic-bundled packages."
        ),
        "your_situation": (
            f"Without a referral program, clinics have no financial incentive to recommend you. "
            f"Example math (commission model, 15%): "
            f"EUR{you['nightly_rate_eur']} x {example_nights_per_referral} nights = EUR{gross_per_referral} gross, "
            f"clinic earns EUR{commission_15pct}, you net EUR{net_per_referral}. "
            f"At {example_referrals_per_month} referrals/month = EUR{monthly_from_referrals}/month from clinic channel alone. "
            f"Wholesale model: EUR{wholesale_rate}/night x {example_nights_per_referral} nights = "
            f"EUR{wholesale_weekly}/week, {example_referrals_per_month} referrals = EUR{monthly_wholesale}/month. "
            f"Either model creates guaranteed, recurring bookings."
        ),
        "recommendation": (
            "Create a simple 1-page referral sheet for clinics offering both models: "
            "(1) Commission: clinic earns 10-15% for every night their patient stays. "
            "(2) Wholesale: fixed weekly rate 20-25% below retail for bundled packages. "
            "Let clinics choose which model suits them. Start with 3-5 dental clinics in Tirana "
            "that serve international patients. The clinic's incentive: they can advertise "
            "'accommodation included' in their packages, which increases their conversion rate."
        ),
        "what_top_hosts_do": (
            "In Turkey (the market leader for medical tourism), clinics bundle 3-5 night hotel stays "
            "into every surgery package as standard. The accommodation provider gets guaranteed volume; "
            "the clinic gets a competitive selling point. Albania has NO host doing this yet."
        ),
    }


def analyze_direct_booking_savings():
    """Calculate savings from direct bookings vs platform commissions."""
    d = DIRECT_BOOKING_SAVINGS
    you = YOUR_PRICING

    annual_revenue_eur = you["estimated_monthly_revenue_eur"] * 12
    current_airbnb_fees = round(annual_revenue_eur * d["airbnb_commission_pct"] / 100)
    stripe_fees_if_direct = round(annual_revenue_eur * 0.029 + 12 * 0.30)  # ~2.9% + $0.30/txn approx
    potential_savings = current_airbnb_fees - stripe_fees_if_direct

    # At scale (EUR50K revenue)
    ex = d["example_at_50k_revenue"]

    return {
        "severity": "MEDIUM",
        "area": "No Direct Booking Channel (100% Platform Dependent)",
        "finding": (
            f"Airbnb takes {d['airbnb_commission_pct']}% commission (changed late 2025). "
            f"At scale, the numbers are stark: at $50K/year revenue, you'd pay "
            f"${ex['airbnb_fees_usd']:,} to Airbnb vs ${ex['stripe_processing_usd']:,} Stripe processing "
            f"for direct bookings — a ${ex['annual_savings_usd']:,}/year difference. "
            f"You can offer guests a 10% direct-booking discount and STILL save ~5% vs Airbnb's cut."
        ),
        "your_situation": (
            f"At your current ~EUR{annual_revenue_eur:,.0f}/year revenue, you're paying "
            f"~EUR{current_airbnb_fees}/year in Airbnb fees. With a direct booking site, "
            f"fees drop to ~EUR{stripe_fees_if_direct}/year (Stripe processing). "
            f"Potential savings: ~EUR{potential_savings}/year. This is lower priority NOW because "
            f"your volume is small, but becomes significant as revenue grows toward EUR10K+/year."
        ),
        "recommendation": (
            "This is a PHASE 2 initiative (after dynamic pricing and rate increase are live). "
            "Steps: (1) Create a simple direct-booking page (Hospitable, Lodgify, or even a Carrd site). "
            "(2) Add Stripe for payments. "
            "(3) Include a card in your apartment with a QR code: 'Book direct next time and save 10%.' "
            "(4) Collect guest emails for repeat marketing. "
            "Priority: implement AFTER pricing tools and clinic partnerships are running."
        ),
        "what_top_hosts_do": (
            "Established hosts aim for 20-40% of bookings to come direct. "
            "They use business cards, email sequences, and 'book direct' discount codes. "
            "At $50K/year revenue, this saves $6,300/year in platform fees."
        ),
    }


def run():
    """Main skill entry point."""
    issues = [
        analyze_dynamic_pricing_gap(),
        analyze_seasonal_strategy_gap(),
        analyze_length_of_stay_gap(),
        analyze_rating_adjusted_pricing(),
        analyze_revenue_potential(),
        analyze_clinic_referral_pricing(),
        analyze_direct_booking_savings(),
    ]

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "issues": issues,
        "issues_count": len(issues),
    }

    # --- Print summary ---
    you = YOUR_PRICING
    rev = REVENUE_PROJECTIONS

    print(f"\n{'='*70}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*70}")

    print(f"\n  YOUR CURRENT PRICING SETUP:")
    print(f"    Nightly rate:           EUR{you['nightly_rate_eur']} (static, never changes)")
    print(f"    Dynamic pricing tool:   {'None' if you['dynamic_pricing_tool'] is None else you['dynamic_pricing_tool']}")
    print(f"    Seasonal adjustments:   {'No' if not you['seasonal_adjustments'] else 'Yes'}")
    print(f"    Weekly discount:        {'None' if you['weekly_discount'] is None else you['weekly_discount']}")
    print(f"    Monthly discount:       {'None' if you['monthly_discount'] is None else you['monthly_discount']}")
    print(f"    Last-minute discount:   {'None' if you['last_minute_discount'] is None else you['last_minute_discount']}")
    print(f"    Clinic referral program:{'No' if not you['clinic_referral_program'] else 'Yes'}")
    print(f"    Direct booking site:    {'No' if not you['direct_booking_site'] else 'Yes'}")
    print(f"    Ratings:                {you['airbnb_rating']}/5 Airbnb, {you['booking_com_rating']}/10 Booking.com")
    print(f"    Est. occupancy:         {you['estimated_occupancy_pct']}%")
    print(f"    Est. monthly revenue:   EUR{you['estimated_monthly_revenue_eur']}")

    print(f"\n  REVENUE LADDER:")
    print(f"    Current:                EUR{rev['current']['monthly_eur']}/month")
    print(f"    + Dynamic pricing:      EUR{rev['with_dynamic_pricing']['monthly_eur']}/month")
    print(f"    + Rate increase (EUR55): EUR{rev['with_rate_increase_and_dynamic']['monthly_eur']}/month")
    lo = rev['with_50pct_occupancy']['monthly_eur_low']
    hi = rev['with_50pct_occupancy']['monthly_eur_high']
    print(f"    + 50% occupancy:        EUR{lo}-{hi}/month")
    print(f"    Top 10% benchmark:      ~${rev['top_10_tirana_benchmark_usd']}/month")

    print(f"\n  ISSUES FOUND: {len(issues)}")
    for i, issue in enumerate(issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area']}")
    print(f"{'='*70}\n")

    return result


if __name__ == "__main__":
    run()
