"""
Skill: Outreach Analyzer
Analyzes the effectiveness of email and WhatsApp outreach campaigns.

Metrics analyzed:
  - Total emails sent vs total leads available
  - Coverage rate (% of leads contacted)
  - Send timing patterns
  - Category distribution of outreach
  - Response/follow-up gaps
  - Outreach velocity (emails per day/session)
"""

from datetime import datetime
from skills.data_loader import load_leads, load_email_log, _find_project_root

SKILL_NAME = "outreach_analyzer"
DESCRIPTION = "Analyzes email and WhatsApp outreach effectiveness"


def analyze_email_outreach(leads, email_log):
    """Analyze email campaign performance."""
    total_leads = len(leads)
    with_email = [l for l in leads if l["email"]]
    emailed = [l for l in leads if l["emailed"]]
    not_emailed = [l for l in with_email if not l["emailed"]]

    # Category breakdown of emailed leads
    emailed_by_category = {}
    for l in emailed:
        cat = l["category"] or "UNKNOWN"
        emailed_by_category[cat] = emailed_by_category.get(cat, 0) + 1

    # Category breakdown of not-yet-emailed leads with email
    pending_by_category = {}
    for l in not_emailed:
        cat = l["category"] or "UNKNOWN"
        pending_by_category[cat] = pending_by_category.get(cat, 0) + 1

    # Analyze send sessions from log
    sessions = []
    current_session = []
    last_time = None

    successes = [e for e in email_log if e.get("action") == "success"]
    for entry in successes:
        try:
            ts = datetime.strptime(entry["timestamp"][:19], "%Y-%m-%d %H:%M:%S")
            if last_time and (ts - last_time).seconds > 300:
                if current_session:
                    sessions.append(current_session)
                current_session = []
            current_session.append(entry)
            last_time = ts
        except (ValueError, KeyError):
            continue

    if current_session:
        sessions.append(current_session)

    # Calculate session stats
    session_stats = []
    for session in sessions:
        if not session:
            continue
        ts_first = datetime.strptime(session[0]["timestamp"][:19], "%Y-%m-%d %H:%M:%S")
        ts_last = datetime.strptime(session[-1]["timestamp"][:19], "%Y-%m-%d %H:%M:%S")
        duration_min = (ts_last - ts_first).seconds / 60
        session_stats.append({
            "date": ts_first.strftime("%Y-%m-%d"),
            "start_time": ts_first.strftime("%H:%M"),
            "count": len(session),
            "duration_min": round(duration_min, 1),
        })

    return {
        "total_leads": total_leads,
        "leads_with_email": len(with_email),
        "leads_emailed": len(emailed),
        "leads_pending_email": len(not_emailed),
        "email_coverage_pct": round(len(emailed) / len(with_email) * 100, 1) if with_email else 0,
        "total_coverage_pct": round(len(emailed) / total_leads * 100, 1) if total_leads else 0,
        "emailed_by_category": emailed_by_category,
        "pending_by_category": pending_by_category,
        "send_sessions": session_stats,
        "total_successful_sends": len(successes),
    }


def analyze_whatsapp_outreach(leads):
    """Analyze WhatsApp outreach status."""
    total_leads = len(leads)
    with_phone = [l for l in leads if l["phone"]]
    messaged = [l for l in leads if l["messaged"]]
    not_messaged = [l for l in with_phone if not l["messaged"]]

    messaged_by_category = {}
    for l in messaged:
        cat = l["category"] or "UNKNOWN"
        messaged_by_category[cat] = messaged_by_category.get(cat, 0) + 1

    pending_by_category = {}
    for l in not_messaged:
        cat = l["category"] or "UNKNOWN"
        pending_by_category[cat] = pending_by_category.get(cat, 0) + 1

    return {
        "total_leads": total_leads,
        "leads_with_phone": len(with_phone),
        "leads_messaged": len(messaged),
        "leads_pending_whatsapp": len(not_messaged),
        "whatsapp_coverage_pct": round(len(messaged) / len(with_phone) * 100, 1) if with_phone else 0,
        "messaged_by_category": messaged_by_category,
        "pending_by_category": pending_by_category,
    }


def identify_issues(email_stats, whatsapp_stats):
    """Identify improvement areas based on outreach analysis."""
    issues = []

    # Email coverage gaps
    if email_stats["email_coverage_pct"] < 50:
        issues.append({
            "severity": "HIGH",
            "area": "Email Coverage",
            "finding": f"Only {email_stats['email_coverage_pct']}% of leads with email have been contacted",
            "recommendation": f"You have {email_stats['leads_pending_email']} leads with email addresses that haven't been contacted yet. Run email_sender.py to reach them.",
        })

    if email_stats["total_coverage_pct"] < 30:
        issues.append({
            "severity": "HIGH",
            "area": "Email Data Gap",
            "finding": f"Only {email_stats['total_coverage_pct']}% of all leads have been emailed (many leads lack email addresses)",
            "recommendation": "Run email_scraper.py to extract more email addresses from clinic websites.",
        })

    # WhatsApp coverage
    if whatsapp_stats["whatsapp_coverage_pct"] < 10:
        issues.append({
            "severity": "HIGH",
            "area": "WhatsApp Underutilized",
            "finding": f"Only {whatsapp_stats['whatsapp_coverage_pct']}% of leads with phone have been messaged via WhatsApp",
            "recommendation": f"WhatsApp is more personal and gets higher response rates. {whatsapp_stats['leads_pending_whatsapp']} leads are waiting. Run whatsapp_sender.py.",
        })

    # Category imbalance
    for cat in ["DENTAL", "HAIR_TRANSPLANT"]:
        emailed = email_stats["emailed_by_category"].get(cat, 0)
        pending = email_stats["pending_by_category"].get(cat, 0)
        if pending > emailed * 2:
            issues.append({
                "severity": "MEDIUM",
                "area": f"{cat} Email Gap",
                "finding": f"{cat}: {emailed} emailed but {pending} still pending",
                "recommendation": f"Prioritize emailing the remaining {pending} {cat} leads.",
            })

    # Send velocity
    if email_stats["send_sessions"]:
        total_sent = sum(s["count"] for s in email_stats["send_sessions"])
        num_sessions = len(email_stats["send_sessions"])
        avg_per_session = total_sent / num_sessions
        if avg_per_session < 20:
            issues.append({
                "severity": "MEDIUM",
                "area": "Low Send Volume",
                "finding": f"Average of {avg_per_session:.0f} emails per session across {num_sessions} sessions",
                "recommendation": "Increase batch size per session. With 10s delay, you can send 60+ emails in 10 minutes.",
            })
    else:
        issues.append({
            "severity": "HIGH",
            "area": "No Email History",
            "finding": "No successful email sends found in the log",
            "recommendation": "Start your email outreach campaign immediately.",
        })

    # No follow-up system
    issues.append({
        "severity": "MEDIUM",
        "area": "No Follow-Up System",
        "finding": "There is no mechanism to track responses or send follow-up emails",
        "recommendation": "Add a 'Responded' column to track which clinics replied. Create a follow-up email template to send 7-14 days after initial contact.",
    })

    # No tracking of conversions
    issues.append({
        "severity": "HIGH",
        "area": "No Conversion Tracking",
        "finding": "There is no way to track which outreach leads to actual bookings",
        "recommendation": "Add columns for 'Partnership Agreed', 'First Referral Date', 'Total Referrals'. This is critical for measuring ROI of your outreach.",
    })

    return issues


def run():
    """Main skill entry point."""
    root = _find_project_root()
    leads = load_leads(root)
    email_log = load_email_log(root)

    if isinstance(leads, dict) and "error" in leads:
        return {"skill": SKILL_NAME, "status": "error", "error": leads["error"]}
    if isinstance(email_log, dict) and "error" in email_log:
        email_log = []

    email_stats = analyze_email_outreach(leads, email_log)
    whatsapp_stats = analyze_whatsapp_outreach(leads)
    issues = identify_issues(email_stats, whatsapp_stats)

    result = {
        "skill": SKILL_NAME,
        "status": "success",
        "email_outreach": email_stats,
        "whatsapp_outreach": whatsapp_stats,
        "issues": issues,
        "issues_count": len(issues),
    }

    # Print summary
    print(f"\n{'='*60}")
    print(f"  SKILL: {SKILL_NAME}")
    print(f"{'='*60}")
    print(f"\n  EMAIL OUTREACH:")
    print(f"    Leads with email:    {email_stats['leads_with_email']}")
    print(f"    Already emailed:     {email_stats['leads_emailed']}")
    print(f"    Pending:             {email_stats['leads_pending_email']}")
    print(f"    Coverage:            {email_stats['email_coverage_pct']}%")
    print(f"\n  WHATSAPP OUTREACH:")
    print(f"    Leads with phone:    {whatsapp_stats['leads_with_phone']}")
    print(f"    Already messaged:    {whatsapp_stats['leads_messaged']}")
    print(f"    Pending:             {whatsapp_stats['leads_pending_whatsapp']}")
    print(f"    Coverage:            {whatsapp_stats['whatsapp_coverage_pct']}%")
    print(f"\n  ISSUES FOUND: {len(issues)}")
    for i, issue in enumerate(issues, 1):
        print(f"    {i}. [{issue['severity']}] {issue['area']}: {issue['finding']}")
    print(f"{'='*60}\n")

    return result


if __name__ == "__main__":
    run()
