# SKILL: Serper Clinic Lead Crawler (Expanding Map Search)

You are my Claude Agent. Create a reusable skill named:

**`serper_clinic_leads`**

## Goal
Crawl outward from a **user-supplied starting point** on Google Maps, discovering clinics in an expanding radius. The agent **loops continuously** — after each round of searches, it jumps to the farthest-away clinic it found and searches again from there. This repeats **until the Serper API credits are exhausted** (i.e. the API returns a 403/429 error or a credits-exhausted message).

Categories to search:
- Dental clinics / dentists
- Hair transplant clinics

## How the Crawl Loop Works

```
CURRENT_LAT, CURRENT_LNG = starting point from user

LOOP forever:
  1. Run all query templates against Serper Places API using CURRENT_LAT, CURRENT_LNG as the `ll` parameter
  2. Collect all places[] results
  3. Deduplicate against ALL previously found leads (in-memory set + leads.xlsx) — skip if Name OR Location/address already exists
  4. Append new leads to leads.xlsx
  5. Print iteration summary: "Iteration X: Found Y new leads (Z total). Jumping to: <farthest clinic name>"
  6. From ALL results in this iteration, find the clinic with the GREATEST distance from (CURRENT_LAT, CURRENT_LNG)
     - Use the Haversine formula to calculate distance:
       a = sin²(Δlat/2) + cos(lat1) * cos(lat2) * sin²(Δlng/2)
       c = 2 * atan2(√a, √(1−a))
       d = R * c   (R = 6371 km)
  7. Set CURRENT_LAT, CURRENT_LNG = that farthest clinic's latitude, longitude
  8. Go back to step 1

STOP ONLY when:
  - Serper API returns an error (403, 429, or body contains "credits" / "limit" / "exceeded")
  - OR 3 consecutive iterations produce ZERO new leads (the area is fully covered)
```

**IMPORTANT:** Do NOT stop early. Do NOT set a max iteration count. The agent must keep going until it physically cannot make more API calls or the area is saturated.

## Location Input (REQUIRED)

The user MUST provide a starting location in one of these formats:
- **Google Maps coordinates:** `@lat,lng,zoom` (e.g. `@41.3212598,19.8230679,17z`)
- **City + Country:** e.g. `Tirana, Albania`
- **Google Maps URL:** containing coordinates in the URL

### How to use the starting location
1. **Extract coordinates** (lat, lng) from whatever format the user provides.
2. **Reverse-geocode the coordinates** to determine the **city name** and **country** — use common knowledge if the location is well-known.
3. **The following variables are hardcoded for Albania** (do NOT change these):
   - `COUNTRY` = `Albania`
   - `COUNTRY_CODE` = `al`
   - `LOCAL_LANG` = `sq` (Albanian)
   - `PHONE_PREFIX` = `+355`
   - `LOCAL_DENTAL_TERM` = `klinikë dentare`
   - `LOCAL_HAIR_TERM` = `transplant flokësh`
   - `CITY` — derive from the user's starting coordinates (e.g. "Tirana")
   - `CITY_LOCAL` — Albanian spelling if different (e.g. "Tiranë")
4. Set `CURRENT_LAT` and `CURRENT_LNG` to the extracted coordinates. These will update after each iteration.

## MANDATORY: Excel Output (NEVER skip this)

**File:** `leads.xlsx` (in the project root directory)

### Excel Rules (STRICTLY ENFORCED)
1. **NEVER delete, clear, or overwrite existing data** in the file.
2. If `leads.xlsx` already exists, **read the existing data first**, then **append** new records below the last row.
3. If `leads.xlsx` does not exist, create it with the header row.
4. **Deduplicate against existing rows** — do NOT add a lead if a row with the same **Name + Location** (address) already exists. Check both columns A and B before appending. If either the Name matches an existing row OR the Location/address matches an existing row, skip that lead.
5. Use the `openpyxl` Python library to read/write the Excel file.
6. **Save the file after EVERY iteration** — not just at the end. If the agent crashes mid-run, all previously found leads must be persisted.

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
| H      | Score          | Proximity score 1-10 (10 = closest to base)  |

### Excel Write Procedure (execute EVERY iteration)
```
1. pip install openpyxl (if not already installed — only on first iteration)
2. If leads.xlsx exists → load it with openpyxl, find last row
3. If leads.xlsx does NOT exist → create workbook, write header row
4. For each new lead NOT already in the file → append a new row
5. Save the file
6. Print summary: "Iteration X — Added Y new leads. Total leads in file: Z"
```

## Constraints
- Use Serper **Places endpoint only** (`/places`) — do NOT use `/search` or `/maps`.
- Do NOT send messages, do NOT automate WhatsApp outreach.
- Deduplicate aggressively by **name OR address** — if either matches an existing lead, skip it.
- **Do NOT stop until the API credits run out or 3 consecutive iterations find zero new leads.**
- Save to Excel after every single iteration.

## Inputs
- `serper_api_key`: `5a88736a239477affbba609346cd8a884da61248`
- `location`: **(REQUIRED)** — starting coordinates, city name, or Google Maps URL
- `category`: which clinic types to search — `DENTAL`, `HAIR_TRANSPLANT`, or `ALL` (default `ALL`)
- `max_results_per_query` (int, default 20)
- `country`: hardcoded to `al` (Albania)
- `language`: hardcoded to `sq` (Albanian)

## Serper Endpoint
Use **ONLY the Places endpoint** — do NOT use `/search` or `/maps`:
- POST `https://google.serper.dev/places`
  Headers:
- `X-API-KEY: <serper_api_key>`
- `Content-Type: application/json`

Payload fields (hardcoded for Albania/Albanian):
- `q` (query)
- `location`: `"Tirana County, Albania"` (always include this)
- `gl`: `"al"` (always Albania)
- `hl`: `"sq"` (always Albanian)
- `num` (max_results_per_query)
- `ll` **(REQUIRED every request)** — current search center, format: `"@CURRENT_LAT,CURRENT_LNG,14z"`

## Queries (run these EVERY iteration with updated `ll`)

All queries go to the **Places endpoint** (`/places`). Do NOT use `site:` operators.
The `ll` parameter changes every iteration — it always reflects the current search center.
All queries use `gl: "al"` and `hl: "sq"` (Albania / Albanian).

### Dental (run these if category is DENTAL or ALL)
1. `klinikë dentare`
2. `dentist`
3. `implant dentar`
4. `ortodontist`
5. `kirurgi orale`
6. `dental clinic`

### Hair transplant (run these if category is HAIR_TRANSPLANT or ALL)
7. `transplant flokësh`
8. `hair transplant clinic`
9. `klinikë transplant flokësh`

**Note:** Do NOT include city/country in the query text — the `ll` parameter handles geo-targeting. This ensures results are centered on the current crawl position, not biased toward city center.

## Parsing rules
The Places endpoint returns a `places[]` array. From each place object, extract:
- `title` — business name
- `address` — full address
- `phone` — phone number
- `website` — business website URL
- `rating` — Google rating
- `ratingCount` — number of reviews
- `cid` — Google Maps CID (use to build maps link: `https://www.google.com/maps?cid={cid}`)
- `latitude` / `longitude` — coordinates (**critical for the crawl loop**)
- `category` — Google's business category label

All fields may or may not be present — store if available, leave null otherwise.

## Distance Calculation (Haversine)

After each iteration, calculate the distance from `(CURRENT_LAT, CURRENT_LNG)` to every clinic found in that iteration using:

```python
import math

def haversine(lat1, lng1, lat2, lng2):
    R = 6371  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlng/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c
```

Pick the clinic with the **maximum distance** — that becomes the next search center.

## Proximity Score (1–10)

For every clinic, calculate a **proximity score** based on its distance from the **fixed base coordinates** `41.3212598, 19.8230679` (these NEVER change — they are NOT the crawl position).

Use the Haversine distance to the base point, then convert to a 1–10 score:

```python
BASE_LAT = 41.3212598
BASE_LNG = 19.8230679

def proximity_score(clinic_lat, clinic_lng):
    dist_km = haversine(BASE_LAT, BASE_LNG, clinic_lat, clinic_lng)
    if dist_km <= 1:
        return 10
    elif dist_km <= 2:
        return 9
    elif dist_km <= 3:
        return 8
    elif dist_km <= 5:
        return 7
    elif dist_km <= 8:
        return 6
    elif dist_km <= 12:
        return 5
    elif dist_km <= 18:
        return 4
    elif dist_km <= 25:
        return 3
    elif dist_km <= 40:
        return 2
    else:
        return 1
```

| Score | Distance from base       |
|-------|--------------------------|
| 10    | ≤ 1 km                   |
| 9     | 1–2 km                   |
| 8     | 2–3 km                   |
| 7     | 3–5 km                   |
| 6     | 5–8 km                   |
| 5     | 8–12 km                  |
| 4     | 12–18 km                 |
| 3     | 18–25 km                 |
| 2     | 25–40 km                 |
| 1     | > 40 km                  |

Write this score to **column H** in `leads.xlsx`. If a clinic has no coordinates, set score to `0`.

## Normalization & Classification
For each result, create a `Lead` object:

```json
{
  "category": "DENTAL | HAIR_TRANSPLANT | UNKNOWN",
  "name": "...",
  "city": "{CITY}",
  "country": "{COUNTRY}",
  "address": "...",
  "website": "...",
  "maps_link": "https://www.google.com/maps?cid={cid}",
  "phone": "...",
  "email": null,
  "instagram": null,
  "facebook": null,
  "rating": null,
  "ratingCount": null,
  "latitude": 0.0,
  "longitude": 0.0,
  "confidence": 0.0,
  "found_by_query": "...",
  "found_in_iteration": 1
}
```

## Phone number extraction
- Look for Albanian phone numbers matching the `+355` prefix.
- Common formats: `+355 XX XXX XXXX`, `+355XXXXXXXXX`, `06X XXX XXXX`, etc.
- Also match local formats without the country prefix.

## Iteration Log (print after each iteration)

```
═══════════════════════════════════════════════════
  ITERATION 3
  Search center: 41.3212, 19.8230
  Queries sent: 9
  Results this round: 14
  New leads (after dedup): 8
  Total leads in file: 47
  Farthest clinic: "Dental Pro" (12.4 km away)
  Next search center: 41.4102, 19.9015
  Jumping to next point...
═══════════════════════════════════════════════════
```

## Error Handling

- **API returns 403/429/credits error** → Print final summary and STOP. This is the expected end condition.
- **API returns empty `places[]` for all queries in an iteration** → Count as a "dry iteration". After **3 consecutive dry iterations**, print final summary and STOP.
- **A single query fails but others succeed** → Continue with successful results, log the error, proceed to next iteration.
- **No latitude/longitude on any result** → Skip that result for distance calculation (but still save the lead to Excel).

## Final Summary (print when stopping)

```
═══════════════════════════════════════════════════
  CRAWL COMPLETE
  Total iterations: X
  Total leads collected: Y
  Stop reason: [API credits exhausted / Area saturated (3 dry iterations)]
  File saved: leads.xlsx
═══════════════════════════════════════════════════
```

## Execution Checklist (follow every run)
- [ ] Parse user-provided starting location → extract lat/lng
- [ ] Determine CITY, COUNTRY, and all local-language variables
- [ ] Install openpyxl if needed
- [ ] **Enter the crawl loop:**
  - [ ] Build queries with current `ll`
  - [ ] Run all Serper Places queries
  - [ ] Parse places[], extract leads with coordinates
  - [ ] Deduplicate against all previously found leads
  - [ ] Append new leads to leads.xlsx and SAVE
  - [ ] Print iteration summary
  - [ ] Find farthest clinic → update CURRENT_LAT, CURRENT_LNG
  - [ ] Check stop conditions → if not met, loop again
- [ ] Print final summary
