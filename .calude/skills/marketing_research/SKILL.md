# SKILL: Airbnb Marketing Research & Ideas Generator

You are my Claude Agent. Create a reusable skill named:

**`marketing_research`**

## Goal
Research current Airbnb marketing strategies, trends, and tactics online. Analyze what top-performing Airbnb hosts and property managers are doing, then generate actionable marketing ideas tailored to the user's Airbnb listing — **Lulebore Apartment 1** in central Tirana, Albania.

The agent searches the web for up-to-date marketing strategies, analyzes competitors, and produces a prioritized list of ideas the user can implement immediately.

## Context — The User's Airbnb Business

| Detail | Value |
|--------|-------|
| Property | Lulebore Apartment 1 |
| Location | Central Tirana, Albania |
| Type | 1-bedroom apartment |
| Guests | 1 |
| Amenities | Free WiFi, flat-screen TV, washing machine, fully equipped kitchen, private entrance, soundproofing |
| Rating | 4.88/5 (33 reviews) |
| Listing URL | https://www.airbnb.com/rooms/1079680851745325307 |
| Target guests | International patients visiting Tirana for dental care or hair transplants |
| Current outreach | Email & WhatsApp campaigns to dental and hair transplant clinics in Tirana |

## How It Works

```
1. Search the web for current Airbnb marketing strategies & trends
2. Search for medical tourism accommodation marketing tactics
3. Search for competitor Airbnb listings in Tirana to analyze pricing & positioning
4. Search for social media marketing strategies for short-term rentals
5. Search for partnership/referral program ideas for Airbnb hosts
6. Compile findings into categorized, actionable ideas
7. Prioritize by effort vs impact
8. Present results in a structured report
```

## Research Topics to Search

The agent MUST search for information on ALL of the following topics. Use the WebSearch tool for each.

### 1. Airbnb Listing Optimization
Search queries:
- `Airbnb listing optimization tips 2026`
- `how to rank higher on Airbnb search results`
- `Airbnb SEO best practices`
- `Airbnb photo tips increase bookings`
- `Airbnb title and description optimization`
- `Airbnb pricing strategy dynamic pricing`

### 2. Medical Tourism Accommodation Marketing
Search queries:
- `medical tourism accommodation marketing strategies`
- `dental tourism patient housing marketing`
- `how to market apartment to medical tourists`
- `clinic partnership accommodation referral program`
- `medical tourism Albania Tirana trends 2026`

### 3. Social Media Marketing for Airbnb
Search queries:
- `Instagram marketing for Airbnb hosts`
- `TikTok marketing short term rental`
- `social media content ideas Airbnb property`
- `Airbnb host personal branding`
- `how to get more Airbnb reviews`

### 4. Direct Booking & Multi-Platform Strategies
Search queries:
- `Airbnb direct booking website strategy`
- `list property on Booking.com vs Airbnb`
- `multi-platform short term rental marketing`
- `Google Business Profile vacation rental`
- `Airbnb alternative platforms for hosts`

### 5. Partnership & Referral Marketing
Search queries:
- `Airbnb partnership with local businesses`
- `referral program short term rental`
- `dental clinic partnership accommodation deal`
- `B2B marketing for Airbnb hosts`
- `corporate housing partnerships`

### 6. Content Marketing & Online Presence
Search queries:
- `content marketing for Airbnb hosts blog`
- `Airbnb guidebook marketing strategy`
- `email marketing for vacation rental owners`
- `Google Ads for Airbnb listing`
- `Facebook Ads short term rental targeting`

### 7. Guest Experience & Upselling
Search queries:
- `Airbnb guest experience improvement ideas`
- `upselling services Airbnb host`
- `Airbnb welcome package ideas`
- `airport transfer service Airbnb`
- `Airbnb experience hosting side income`

### 8. Competitor Analysis — Tirana Market
Search queries:
- `best Airbnb apartments Tirana Albania`
- `Airbnb Tirana central apartment price per night`
- `vacation rental market Tirana Albania`
- `Booking.com Tirana apartment reviews`

## Output Format

The agent MUST produce a structured report with the following sections:

### Report Structure

```markdown
# Airbnb Marketing Research Report
**Generated:** {date}
**Property:** Lulebore Apartment 1, Tirana

---

## Executive Summary
{3-5 sentence overview of the most impactful findings}

---

## 1. Quick Wins (Do This Week)
{Ideas that take < 2 hours and cost nothing}
- Idea 1: {title}
  - What: {description}
  - Why: {expected impact}
  - How: {step-by-step}

## 2. Listing Optimization
{Specific improvements to the Airbnb listing}
- ...

## 3. Medical Tourism Angle
{Strategies specific to targeting dental/hair transplant patients}
- ...

## 4. Social Media Strategy
{Platform-specific tactics}
- ...

## 5. Partnership Ideas
{B2B and referral strategies beyond current clinic outreach}
- ...

## 6. Paid Marketing Opportunities
{Ads, sponsored content, paid listings}
- ...

## 7. Guest Experience Upgrades
{In-property improvements that lead to more bookings}
- ...

## 8. Multi-Platform Expansion
{Other platforms and channels to list on}
- ...

## 9. Content & SEO
{Blog, social, video content ideas}
- ...

## 10. Competitor Insights
{What top Tirana Airbnb hosts are doing}
- ...

---

## Priority Matrix

| Idea | Effort | Impact | Priority |
|------|--------|--------|----------|
| ... | Low/Med/High | Low/Med/High | 1-10 |

---

## Sources
{List all URLs consulted}
```

## Important Rules

1. **Always search the web** — do NOT rely solely on existing knowledge. Use WebSearch for every topic.
2. **Be specific to Tirana, Albania** — generic Airbnb advice is less useful than localized insights.
3. **Be specific to medical tourism** — the user's main angle is providing accommodation for clinic patients.
4. **Prioritize actionable ideas** — each idea must have clear steps to implement.
5. **Include pricing context** — mention cost of any paid strategies.
6. **Include competitor examples** — reference real listings or businesses when possible.
7. **Save the report** to `/mnt/windows/projekte Joni/airbnb_advertiser/marketing_report.md`
8. **Include sources** — list every URL used in the research.

## Execution Checklist

- [ ] Search for Airbnb listing optimization tips (2+ searches)
- [ ] Search for medical tourism accommodation marketing (2+ searches)
- [ ] Search for social media strategies for short-term rentals (2+ searches)
- [ ] Search for direct booking and multi-platform strategies (2+ searches)
- [ ] Search for partnership and referral marketing ideas (2+ searches)
- [ ] Search for content marketing strategies (1+ search)
- [ ] Search for guest experience and upselling ideas (1+ search)
- [ ] Search for Tirana Airbnb competitor landscape (1+ search)
- [ ] Compile all findings into the report format
- [ ] Create priority matrix ranking ideas by effort vs impact
- [ ] Save report to marketing_report.md
- [ ] Present summary to user

## Constraints

- Do NOT make up statistics or data — only cite what is found in search results
- Do NOT recommend anything illegal or against Airbnb Terms of Service
- Do NOT recommend buying fake reviews
- Focus on strategies relevant to a single apartment (not a property management company)
- All monetary references should include EUR equivalent (Albania uses ALL/Lek but EUR is widely understood)
- Keep the report concise — max 5 bullet points per section
- The report should be readable in under 10 minutes
