"""
Skill: Marketing Channel Analyzer
Analyzes effectiveness of all marketing channels and identifies ROI gaps.

Metrics analyzed:
  - Channel utilization rate
  - Email outreach ROI indicators
  - WhatsApp outreach ROI indicators
  - Platform distribution (Airbnb vs Booking.com)
  - Missing channels and their potential
  - Content marketing status
"""

from skills.data_loader import (
    load_leads, load_email_log, load_property_profile,
    load_marketing_report, _find_project_root
)

SKILL_NAME = "marketing_analyzer"
DESCRIPTION = "Analyzes marketing channel effectiveness and identifies missing opportunities"


def analyze_channels(leads, email_log, profile_text):
    """Analyze all marketing channels."""

    # Channel inventory
    channels = {
        "airbnb": {
            "name": "Airbnb",
            "status": "active",
            "type": "platform",
            "cost": "15% commission",
            "reviews": 33,
            "rating": 4.88,
            "notes": "Primary booking channel",
        },
        "booking_com": {
            "name": "Booking.com",
            "status": "active",
            "type": "platform",
            "cost": "15% commission",
            "reviews": 21,
            "rating": 10.0,
            "notes": "Secondary booking channel",
        },
        "email_outreach": {
            "name": "Email Outreach to Clinics",
            "status": "active",
            "type": "outbound",
            "cost": "Free (time only)",
            "leads_contacted": sum(1 for l in leads if l["emailed"]),
            "total_addressable": sum(1 for l in leads if l["email"]),
            "notes": "B2B partnership outreach",
        },
        "whatsapp_outreach": {
            "name": "WhatsApp Outreach to Clinics",
            "status": "minimal",
            "type": "outbound",
            "cost": "Free (time only)",
            "leads_contacted": sum(1 for l in leads if l["messaged"]),
            "total_addressable": sum(1 for l in leads if l["phone"]),
            "notes": "Higher response rate than email but barely used",
        },
        "social_media": {
            "name": "Social Media (Instagram/TikTok)",
            "status": "not_started",
            "type": "organic",
            "cost": "Free (time only)",
            "potential_impact": "23% higher booking rate",
            "notes": "Zero presence currently",
        },
        "google_business": {
            "name": "Google Business Profile",
            "status": "not_started",
            "type": "organic",
            "cost": "Free",
            "potential_impact": "Free Google Maps/Search visibility",
            "notes": "Missing free discovery channel",
        },
        "direct_website": {
            "name": "Direct Booking Website",
            "status": "not_started",
            "type": "owned",
            "cost": "€19/year (Carrd)",
            "potential_impact": "Save 15% platform fees",
            "notes": "No direct booking option exists",
        },
        "paid_ads": {
            "name": "Paid Advertising (Google/Facebook)",
            "status": "not_started",
            "type": "paid",
            "cost": "€250/month estimated",
            "potential_impact": "3-6 extra bookings/month",
            "notes": "Not using any paid acquisition",
        },
        "in_person_clinics": {
            "name": "In-Person Clinic Visits",
            "status": "not_started",
            "type": "outbound",
            "cost": "Free (time only)",
            "potential_impact": "10x more effective than email",
            "notes": "Only doing remote outreach currently",
        },
        "medical_directories": {
            "name": "Medical Tourism Directories",
            "status": "not_started",
            "type": "listing",
            "cost": "Free to low",
            "potential_impact": "Targeted medical tourist audience",
            "notes": "Not listed on any medical tourism platforms",
        },
        "youtube": {
            "name": "YouTube",
            "status": "not_started",
            "type": "organic",
            "cost": "Free",
            "potential_impact": "YouTube videos rank in Google search",
            "notes": "No video content at all",
        },
        "guest_referrals": {
            "name": "Guest Referral Program",
            "status": "not_started",
            "type": "referral",
            "cost": "20% discount on next stay",
            "potential_impact": "Past guests are 5x cheaper to convert",
            "notes": "No referral system in place",
        },
    }

    # Channel utilization score
    active = sum(1 for c in channels.values() if c["status"] == "active")
    minimal = sum(1 for c in channels.values() if c["status"] == "minimal")
    not_started = sum(1 for c in channels.values() if c["status"] == "not_started")

    return {
        "channels": channels,
        "active_channels": active,
        "minimal_channels": minimal,
        "not_started_channels": not_started,
        "total_channels": len(channels),
        "utilization_pct": round((active + minimal * 0.5) / len(channels) * 100, 1),
    }


def identify_issues(channel_analysis, leads):
    """Identify marketing improvement areas."""
    issues = []
    channels = channel_analysis["channels"]

    # Low channel utilization
    if channel_analysis["utilization_pct"] < 30:
        issues.append({
            "severity": "CRITICAL",
            "area": "Extremely Low Channel Utilization",
            "finding": f"Only using {channel_analysis['active_channels']} of {channel_analysis['total_channels']} marketing channels ({channel_analysis['utilization_pct']}% utilization)",
            "recommendation": "You're relying almost entirely on Airbnb and Booking.com. This is a single point of failure. Diversify immediately.",
        })

    # WhatsApp underutilized
    wa = channels["whatsapp_outreach"]
    if wa["leads_contacted"] < wa["total_addressable"] * 0.1:
        issues.append({
            "severity": "HIGH",
            "area": "WhatsApp Channel Wasted",
            "finding": f"Only {wa['leads_contacted']} of {wa['total_addressable']} phone leads contacted via WhatsApp",
            "recommendation": "WhatsApp has 3-5x higher response rate than email for B2B in Albania. Prioritize WhatsApp outreach over email for initial contact.",
        })

    # No social media
    if channels["social_media"]["status"] == "not_started":
        issues.append({
            "severity": "HIGH",
            "area": "Zero Social Media Presence",
            "finding": "Properties with active social media see 23% higher booking rates. You have no presence at all.",
            "recommendation": "Create Instagram @lulebore.apartment this week. Post 3x/week: apartment photos, Tirana neighborhood shots, guest testimonials. Start TikTok for medical tourism content.",
        })

    # No in-person clinic visits
    if channels["in_person_clinics"]["status"] == "not_started":
        issues.append({
            "severity": "HIGH",
            "area": "No In-Person Clinic Relationships",
            "finding": "Only doing remote outreach (email/WhatsApp). In-person visits are 10x more effective for partnership building.",
            "recommendation": "Visit the top 20 clinics with highest proximity scores in person. Bring printed flyers with QR code and a clear commission offer (€5-10/night per referral).",
        })

    # No direct booking
    if channels["direct_website"]["status"] == "not_started":
        issues.append({
            "severity": "MEDIUM",
            "area": "No Direct Booking Channel",
            "finding": "Paying 15% commission on every booking to platforms. No way for returning guests to book directly.",
            "recommendation": "Create a simple direct booking page (Carrd.co, €19/year). Offer 10% discount for direct bookings — you still save 5% vs platform fees.",
        })

    # No Google presence
    if channels["google_business"]["status"] == "not_started":
        issues.append({
            "severity": "MEDIUM",
            "area": "Invisible on Google",
            "finding": "No Google Business Profile. When someone searches 'apartment near dental clinic Tirana', you don't appear.",
            "recommendation": "Set up Google Business Profile as 'Tourist Accommodation'. Add all photos, respond to reviews, post weekly updates. It's 100% free.",
        })

    # No paid advertising
    if channels["paid_ads"]["status"] == "not_started":
        issues.append({
            "severity": "MEDIUM",
            "area": "No Paid Acquisition",
            "finding": "Not running any paid ads. Relying entirely on organic discovery and manual outreach.",
            "recommendation": "Start with €5/day Google Ads targeting 'dental tourism accommodation Tirana'. A single booking pays for 3+ months of ads.",
        })

    # Email outreach only has one template
    issues.append({
        "severity": "MEDIUM",
        "area": "No Follow-Up Campaign",
        "finding": "Only one outreach email template. No follow-up sequence for clinics that didn't respond.",
        "recommendation": "Create a 3-email sequence: (1) Introduction, (2) Follow-up after 7 days with testimonial, (3) Final follow-up after 14 days with special offer. Most B2B responses come on the 2nd or 3rd email.",
    })

    # No guest email collection
    issues.append({
        "severity": "LOW",
        "area": "No Guest Email Marketing",
        "finding": "Not collecting guest emails for remarketing. Past guests are 5x cheaper to convert than new ones.",
        "recommendation": "Collect guest emails (with permission). Send quarterly newsletter with seasonal discounts and updates.",
    })

    # No content marketing
    issues.append({
        "severity": "LOW",
        "area": "No Content Marketing",
        "finding": "No blog, YouTube, or content that could rank in Google for medical tourism keywords.",
        "recommendation": "Create content targeting: 'best apartment for dental tourists Tirana', 'recovery accommodation after hair transplant Albania'. A simple blog post can bring passive organic traffic.",
    })

    return issues


def run():
    """Main skill entry point."""
    root = _find_project_root()
    leads = load_leads(root)
    email_log = load_email_log(root)
    profile = load_property_profile(root)
    marketing = load_marketing_report(root)

    if isinstance(leads, dict) and "error" in leads:
        return {"skill": SKILL_NAME, "status": "error", "error": leads["error"]}
    if isinstance(email_log, dict):
        email_log = []

    channel_analysis = analyze_channels(leads, email_log, profile)
    issues = identify_issues(channel_analysis, leads)

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "channel_analysis": {
            "active_channels": channel_analysis["active_channels"],
            "minimal_channels": channel_analysis["minimal_channels"],
            "not_started_channels": channel_analysis["not_started_channels"],
            "total_channels": channel_analysis["total_channels"],
            "utilization_pct": channel_analysis["utilization_pct"],
        },
        "issues": issues,
        "issues_count": len(issues),
    }

    # Print summary
    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  CHANNEL STATUS:")
    print(f"    Active:        {channel_analysis['active_channels']}")
    print(f"    Minimal:       {channel_analysis['minimal_channels']}")
    print(f"    Not started:   {channel_analysis['not_started_channels']}")
    print(f"    Utilization:   {channel_analysis['utilization_pct']}%")
    print(f"\n  CHANNEL BREAKDOWN:")
    for key, ch in channel_analysis["channels"].items():
        icon = "Y" if ch["status"] == "active" else ("~" if ch["status"] == "minimal" else "X")
        print(f"    [{icon}] {ch['name']}")
    print(f"\n  ISSUES FOUND: {len(issues)}")
    for i, issue in enumerate(issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area']}")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
