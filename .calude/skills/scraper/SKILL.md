# SKILL: Serper Clinic Lead Finder (Location-Based)

You are my Claude Agent. Create a reusable skill named:

**`serper_clinic_leads`**

## Goal
Query Serper (Google Search API) to find **local clinics near a user-supplied location** in these categories:
- Dental clinics / dentists
- Hair transplant clinics

Return a clean, deduplicated lead list with useful contact sources (website, phone if visible, maps link).

## Location Input (REQUIRED)

The user MUST provide a location in one of these formats:
- **Google Maps coordinates:** `@lat,lng,zoom` (e.g. `@41.3212598,19.8230679,17z`)
- **City + Country:** e.g. `Tirana, Albania`
- **Google Maps URL:** containing coordinates in the URL

### How to use the location
1. **Extract coordinates** (lat, lng) from whatever format the user provides.
2. **Reverse-geocode the coordinates** to determine the **city name** and **country** by using Serper to search: `"what city is at coordinates <lat>, <lng>"` — OR use common knowledge if the location is well-known.
3. **Derive the following variables** that will be used throughout all queries:
   - `CITY` — the city name (e.g. "Tirana")
   - `CITY_LOCAL` — the city name in local language/spelling if different (e.g. "Tiranë")
   - `COUNTRY` — the country name (e.g. "Albania")
   - `COUNTRY_CODE` — 2-letter ISO code, lowercase (e.g. "al")
   - `LOCAL_LANG` — primary local language code (e.g. "sq" for Albanian)
   - `PHONE_PREFIX` — international dialing prefix (e.g. "+355")
   - `LOCAL_DENTAL_TERM` — the word for "dental clinic" in the local language (e.g. "klinikë dentare")
   - `LOCAL_HAIR_TERM` — the word for "hair transplant" in the local language (e.g. "mbjellje floku")
   - `LOCAL_CONTACT_TERM` — the word for "contact" in the local language (e.g. "kontakt")

4. Use `CITY`, `COUNTRY`, and derived local-language terms in **all queries below** (replacing the previously hardcoded "Tirana" references).

## MANDATORY: Excel Output (NEVER skip this)

**Every single run of this skill MUST write results to the Excel file:**

**File:** `leads.xlsx` (in the project root directory)

### Excel Rules (STRICTLY ENFORCED)
1. **NEVER delete, clear, or overwrite existing data** in the file.
2. If `leads.xlsx` already exists, **read the existing data first**, then **append** new records below the last row.
3. If `leads.xlsx` does not exist, create it with the header row.
4. **Deduplicate against existing rows** — do NOT add a lead if a row with the same Name + Phone already exists in the file.
5. Use the `openpyxl` Python library to read/write the Excel file.

### Excel Columns (in this exact order)
| Column | Header         | Description                                  |
|--------|----------------|----------------------------------------------|
| A      | Name           | Business / clinic name                       |
| B      | Location       | Full address or "{CITY}, {COUNTRY}"          |
| C      | Phone          | Phone number (or empty if unknown)           |
| D      | Email          | Email address (or empty if unknown)          |
| E      | Category       | DENTAL / HAIR_TRANSPLANT / UNKNOWN           |
| F      | Website        | Website URL                                  |
| G      | Date Added     | Date the record was added (YYYY-MM-DD)       |

### Excel Write Procedure (execute every run)
```
1. pip install openpyxl (if not already installed)
2. If leads.xlsx exists → load it with openpyxl, find last row
3. If leads.xlsx does NOT exist → create workbook, write header row
4. For each new lead NOT already in the file → append a new row
5. Save the file
6. Print summary: "Added X new leads. Total leads in file: Y"
```

## Constraints
- Search ONLY for the location the user provided — do NOT search other cities.
- Use Serper only (no direct scraping of Google Maps HTML).
- Do NOT send messages, do NOT automate WhatsApp outreach.
- Keep costs low: minimize number of queries while keeping good coverage.
- Deduplicate aggressively by domain + phone + title similarity.
- Output must be JSON + a human-readable summary + **Excel file updated**.

## Inputs
- `serper_api_key`: `5a88736a239477affbba609346cd8a884da61248`
- `location`: **(REQUIRED)** — coordinates, city name, or Google Maps URL provided by the user
- `category`: which clinic types to search — `DENTAL`, `HAIR_TRANSPLANT`, or `ALL` (default `ALL`)
- `max_results_per_query` (int, default 20)
- `max_total_leads` (int, default 30)
- `language` (string, default "en")

## Serper Endpoint
Use:
- POST `https://google.serper.dev/search`
  Headers:
- `X-API-KEY: <serper_api_key>`
- `Content-Type: application/json`

Payload fields to use:
- `q` (query)
- `gl` (country, use `COUNTRY_CODE`)
- `hl` (language, use "en" but also run local language queries using `LOCAL_LANG`)
- `num` (max_results_per_query)

## Queries (dynamically generated from location)

Replace `{CITY}`, `{COUNTRY}`, `{CITY_LOCAL}`, `{LOCAL_DENTAL_TERM}`, `{LOCAL_HAIR_TERM}`, `{LOCAL_CONTACT_TERM}` with the derived values.

### Dental (run these if category is DENTAL or ALL)
1. `dental clinic {CITY} {COUNTRY} contact`
2. `dentist {CITY} {COUNTRY} phone`
3. `best dental clinic {CITY} {COUNTRY}`
4. `{LOCAL_DENTAL_TERM} {CITY_LOCAL} {LOCAL_CONTACT_TERM}`
5. `dental implants {CITY} {COUNTRY} clinic`
6. `orthodontist {CITY} {COUNTRY}`
7. `teeth whitening {CITY} {COUNTRY} clinic`
8. `emergency dentist {CITY} {COUNTRY}`
9. `dental center {CITY} reviews`
10. `oral surgery clinic {CITY}`
11. `pediatric dentist {CITY} {COUNTRY}`
12. `site:facebook.com "{LOCAL_DENTAL_TERM}" {CITY_LOCAL}`

### Hair transplant (run these if category is HAIR_TRANSPLANT or ALL)
13. `hair transplant clinic {CITY} {COUNTRY} contact`
14. `hair transplant {CITY} phone`
15. `{LOCAL_HAIR_TERM} {CITY_LOCAL} {LOCAL_CONTACT_TERM}`
16. `best hair transplant {CITY} {COUNTRY}`
17. `site:facebook.com "{LOCAL_HAIR_TERM}" {CITY_LOCAL}`

### Maps result references (via search, not scraping)
18. `site:google.com/maps dental clinic {CITY}`
19. `site:google.com/maps hair transplant {CITY}`

You may add up to 4 more queries ONLY if lead count < `max_total_leads` after dedupe.

## Parsing rules
From Serper response, extract from `organic[]`:
- `title`
- `link`
- `snippet`

Also check if Serper returns fields like:
- `phone`
- `address`
- `rating`
- `places[]` (Google Places results — extract these too)
  (if present, store them; if not, leave null)

## Normalization & Classification
For each result, create a `Lead` object:

```json
{
  "category": "DENTAL" | "HAIR_TRANSPLANT" | "UNKNOWN",
  "name": "...",
  "city": "{CITY}",
  "country": "{COUNTRY}",
  "website": "...",
  "source_link": "...",
  "maps_link": "...",
  "phone": "...",
  "email": null,
  "instagram": null,
  "facebook": null,
  "snippet": "...",
  "confidence": 0.0,
  "found_by_query": "..."
}
```

## Phone number extraction
- Look for phone numbers matching the `{PHONE_PREFIX}` pattern in snippets.
- Common formats to match: `{PHONE_PREFIX} XX XXX XXXX`, `{PHONE_PREFIX}XXXXXXXXX`, etc.
- Also match local formats without the prefix.

## Execution Checklist (follow every run)
- [ ] Parse user-provided location → extract lat/lng or city name
- [ ] Determine CITY, COUNTRY, and all local-language variables
- [ ] Generate query list from templates above
- [ ] Run all Serper queries
- [ ] Parse and deduplicate results
- [ ] Classify each lead (DENTAL / HAIR_TRANSPLANT / UNKNOWN)
- [ ] **Load existing leads.xlsx (if it exists)**
- [ ] **Append only NEW leads (skip duplicates)**
- [ ] **Save leads.xlsx**
- [ ] **Print: "Added X new leads. Total leads in file: Y"**
- [ ] Return JSON summary to user
