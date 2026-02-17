# SKILL: WhatsApp Clinic Message Sender (Airbnb Patient Accommodation)

You are my Claude Agent. Create a reusable skill named:

**`message_sender`**

## Goal
Send personalized WhatsApp messages to clinic leads from `leads.xlsx`, advertising an Airbnb apartment as patient accommodation. The agent reads leads from Excel, loads Airbnb property details from a text file, builds personalized Albanian-language messages per clinic category, and sends them via `pywhatkit` (WhatsApp Web browser automation).

## How It Works

```
1. Load Airbnb property info from airbnb_info.txt
2. Load all leads from leads.xlsx
3. Filter to sendable leads (has phone, not yet messaged, valid Albanian mobile)
4. For each lead:
   a. Clean the clinic name
   b. Pick message template based on category (DENTAL / HAIR_TRANSPLANT / UNKNOWN)
   c. Insert clinic name + Airbnb info into template
   d. Send via pywhatkit (WhatsApp Web)
   e. Mark as messaged in Excel with timestamp
   f. Wait before next message
5. Print summary
```

## Files

| File | Purpose |
|------|---------|
| `whatsapp_sender.py` | Main script — all sending logic |
| `leads.xlsx` | Lead database (source — read from columns A-I) |
| `airbnb_info.txt` | Airbnb property details (plain text, inserted into messages) |
| `whatsapp_sender.log` | Audit log of all send attempts |

All files live in the project root: `/mnt/windows/projekte Joni/airbnb_advertiser/`

## Excel Column Layout (leads.xlsx)

| Column | Index | Header     | Description                              |
|--------|-------|------------|------------------------------------------|
| A      | 1     | Name       | Clinic / business name                   |
| B      | 2     | Location   | Full address or "Tirana, Albania"        |
| C      | 3     | Phone      | Phone number (raw, various formats)      |
| D      | 4     | Email      | Email address (often empty)              |
| E      | 5     | Category   | DENTAL / HAIR_TRANSPLANT / UNKNOWN       |
| F      | 6     | Website    | Website URL                              |
| G      | 7     | Date Added | Date record was added (YYYY-MM-DD)       |
| H      | 8     | Score      | Proximity score 1-10                     |
| I      | 9     | Messaged   | Timestamp when message was sent (or empty) |

**Rules:**
- NEVER delete or overwrite existing data in leads.xlsx
- Only write to column I (Messaged) to record send timestamps
- Use `openpyxl` for all Excel operations
- Save after EVERY individual message send (crash-safe)

## Airbnb Info File (airbnb_info.txt)

The user creates this plain text file with their property details. The entire contents are inserted verbatim into the `{airbnb_info}` placeholder in message templates.

**Expected format (example):**
```
Apartament modern ne qender te Tiranes
Vendndodhja: Blloku, Tirane (5 min nga qendra)
Mysafire: deri ne 4 persona
Cmimi: nga 40 EUR/nata
Link: https://airbnb.com/rooms/12345
```

The file can contain any text the user wants — it is inserted as-is. If the file does not exist, show a warning and use a placeholder string.

## Phone Number Formatting

Albanian phone numbers must be converted to international format for WhatsApp (`+355XXXXXXXXX`).

### Formatting Rules

| Input Format | Example | Output | Action |
|-------------|---------|--------|--------|
| Already international Albanian | `+355682032462` | `+355682032462` | Keep as-is, strip spaces |
| International non-Albanian | `+39 02 8718 7132` | `None` | Skip (Albanian-only mode) |
| Albanian mobile with leading 0 | `069 701 5050` | `+355697015050` | Strip spaces, remove leading 0, prepend +355 |
| Albanian mobile no spaces | `0699676398` | `+355699676398` | Remove leading 0, prepend +355 |
| Albanian mobile without 0 | `697015050` | `+355697015050` | Prepend +355 |
| Tirana landline | `04 223 1564` | `None` | Skip (landlines have no WhatsApp) |
| Empty / None | | `None` | Skip |

### Implementation

```python
def format_phone_number(raw_phone, albanian_only=True):
    phone = str(raw_phone).strip()
    digits_with_plus = re.sub(r'[^\d+]', '', phone)

    # Already international
    if digits_with_plus.startswith('+'):
        if albanian_only and not digits_with_plus.startswith('+355'):
            return None
        return digits_with_plus if len(digits_with_plus) >= 10 else None

    digits = re.sub(r'\D', '', phone)

    if digits.startswith('04'):        return None               # landline
    if digits.startswith('0') and len(digits) == 10:
        return '+355' + digits[1:]                                # 06X with leading 0
    if digits.startswith('6') and len(digits) == 9:
        return '+355' + digits                                    # 6X without leading 0

    return None
```

## Name Cleaning

Clinic names from Google Places often contain suffixes. Clean before inserting into messages.

**Rules:**
1. Split on `|`, ` - `, ` – `, ` — `, `: ` — keep first part
2. If ends with `, Tirana` / `, Albania` / `, Tiranë` — strip that suffix
3. Truncate to 60 characters max
4. If name is empty/None, use `"klinika"` as fallback

**Examples:**
| Raw Name | Cleaned |
|----------|---------|
| `Elite Dental \| Tirana` | `Elite Dental` |
| `Dentist In Albania, Tirana` | `Dentist In Albania` |
| `HAIR TRANSPLANT -TRAPIANTO CAPELLI ALBANIA...` | `HAIR TRANSPLANT` |
| `Contact Us En` | `Contact Us En` |

## Message Templates (Albanian)

Three templates based on clinic category. All pitch the Airbnb as **patient accommodation** — a partnership where the clinic recommends the apartment to their international patients.

### DENTAL Template
```
Pershendetje {name}!

Ofrojme akomodim te pershtatshem per pacientet tuaj nderkombetare qe vijne ne Tirane per trajtim dentar.

{airbnb_info}

Pacientet tuaj mund te qendrojne ne nje apartament te rehatshem dhe te pajisur ploterisht, afer klinikes suaj. Kjo do t'u ofronte atyre nje pervojë me te mire dhe do t'ju ndihmonte te terhiqni me shume paciente nderkombetare.

A do te ishit te interesuar per nje bashkepunim? Mund t'ua rekomandoni pacienteve tuaj si akomodimin e tyre te preferuar.

Me respekt
```

### HAIR_TRANSPLANT Template
```
Pershendetje {name}!

Ofrojme akomodim te pershtatshem per klientet tuaj nderkombetare qe vijne ne Tirane per transplant flokesh.

{airbnb_info}

Klientet tuaj mund te qendrojne ne nje apartament te rehatshem dhe te pajisur ploterisht, afer klinikes suaj — ideal per periudhen e rikuperimit pas transplantit. Kjo do t'u ofronte atyre nje pervojë me te mire.

A do te ishit te interesuar per nje bashkepunim? Mund t'ua rekomandoni klienteve tuaj si akomodimin e tyre te preferuar.

Me respekt
```

### UNKNOWN Template
```
Pershendetje {name}!

Ofrojme akomodim te pershtatshem per pacientet tuaj nderkombetare qe vijne ne Tirane per trajtim mjekesor.

{airbnb_info}

Pacientet tuaj mund te qendrojne ne nje apartament te rehatshem dhe te pajisur ploterisht, afer klinikes suaj.

A do te ishit te interesuar per nje bashkepunim?

Me respekt
```

### Template Variables
| Variable | Source |
|----------|--------|
| `{name}` | Cleaned clinic name from Excel column A |
| `{airbnb_info}` | Full contents of `airbnb_info.txt` |

## Sending via pywhatkit

**Library:** `pywhatkit` (install with `pip install pywhatkit`)

**Method:** `pywhatkit.sendwhatmsg_instantly()`

```python
import pywhatkit
pywhatkit.sendwhatmsg_instantly(
    phone_no="+355697015050",
    message="...",
    wait_time=15,       # seconds to wait for WhatsApp Web to load
    tab_close=True,     # auto-close browser tab after sending
    close_time=5,       # seconds before closing tab
)
```

### Prerequisites
- WhatsApp Web must be **logged in** on the default browser
- Browser must be able to open new tabs
- Display/GUI environment required (not headless)

### pywhatkit Import Note
`pywhatkit` imports `pyautogui` at module level, which requires a display. To support `--dry-run` in headless environments, **defer the import** to inside the `send_message()` function — only import when actually sending.

## CLI Arguments

| Argument | Short | Type | Default | Description |
|----------|-------|------|---------|-------------|
| `--dry-run` | `-d` | flag | false | Simulate sending — log everything but don't call pywhatkit |
| `--limit` | `-l` | int | 0 | Max messages to send this run (0 = no limit) |
| `--delay` | | int | 60 | Seconds to wait between messages |
| `--category` | `-c` | choice | ALL | Filter: DENTAL, HAIR_TRANSPLANT, UNKNOWN, or ALL |

## Lead Filtering Pipeline

When selecting which leads to message, apply these filters in order:

```
All leads from Excel (608)
  → Has phone number? (466)
    → Not already messaged? (column I empty)
      → Phone formats to valid Albanian mobile? (437)
        → Matches --category filter?
          → Apply --limit cap
            = Final sendable list
```

## Tracking & Deduplication

- After each successful send, write `YYYY-MM-DD HH:MM` to column I of that row
- On next run, any row with a value in column I is skipped
- Save the Excel file after EVERY individual send (not batched)
- This ensures crash-safety — if the script dies mid-run, all progress is saved

## Sending Loop Behavior

```
For each sendable lead:
  1. Build personalized message (template + name + airbnb_info)
  2. Print: [idx/total] clinic_name | phone | category
  3. If dry-run: log and skip
  4. If live: call pywhatkit.sendwhatmsg_instantly()
     - On success: update Excel column I, increment sent counter
     - On failure: log error, increment failed counter, continue to next
  5. Wait --delay seconds (default 60) before next message
  6. Every 10 messages: print progress summary
```

## Logging

Log to both console (INFO) and file (DEBUG):
- **File:** `whatsapp_sender.log` (append mode, UTF-8)
- **Format:** `%(asctime)s | %(levelname)s | %(message)s`
- **Log every attempt:** phone, clinic name, category, success/failure

## Console Output Format

```
═══════════════════════════════════════════════════
  WHATSAPP MESSAGE SENDER
  Mode: DRY RUN
  File: /mnt/windows/projekte Joni/airbnb_advertiser/leads.xlsx
  Limit: 5 messages
  Delay: 60s between messages
═══════════════════════════════════════════════════

  Airbnb info: loaded from airbnb_info.txt

  Total leads:        608
  With phone:         466
  Already messaged:   0
  Sendable:           437
  To send this run:   5 (limit)

  [1/5] Elite Dental | +355697015050 | DENTAL
        [DRY RUN] Would send message (648 chars)
  [2/5] Trio Dental Center | +355697474695 | DENTAL
        [DRY RUN] Would send message (653 chars)
  ...

═══════════════════════════════════════════════════
  COMPLETE
  Sent: 5 | Failed: 0
  Mode: DRY RUN (no messages were actually sent)
═══════════════════════════════════════════════════
```

## Safety & Rate Limiting

| Safeguard | Details |
|-----------|---------|
| Default delay | 60 seconds between messages |
| Daily limit recommendation | Do not exceed 50 new contacts per day |
| Dry-run mode | Always test with `--dry-run` first |
| Limit flag | Use `--limit` to cap messages per run |
| Crash-safe saves | Excel saved after every single send |
| Error continuation | Failed sends don't stop the loop |
| Duplicate prevention | Column I tracking prevents re-sending |

## Error Handling

| Error | Handling |
|-------|----------|
| `airbnb_info.txt` not found | Warning printed, placeholder text used |
| `leads.xlsx` not found | Print message and exit |
| Phone is None/empty | Skipped in filtering |
| Phone is landline (04X) | Skipped — returns None from formatter |
| Phone is non-Albanian (+39) | Skipped when albanian_only=True |
| pywhatkit fails (browser issue) | Exception caught, logged, continue to next lead |
| WhatsApp Web not logged in | pywhatkit raises exception, caught and logged |

## Execution Checklist

- [ ] Ensure `airbnb_info.txt` exists with property details
- [ ] Ensure WhatsApp Web is logged in on default browser
- [ ] Install pywhatkit: `pip install pywhatkit`
- [ ] Test with dry-run: `python3 whatsapp_sender.py --dry-run --limit 5`
- [ ] Verify message content and phone formatting look correct
- [ ] Send small batch: `python3 whatsapp_sender.py --limit 3`
- [ ] Verify messages arrived on WhatsApp
- [ ] Check `leads.xlsx` column I for timestamps
- [ ] Gradually increase: `--limit 10`, `--limit 20`, up to 50/day max
- [ ] Monitor `whatsapp_sender.log` for failures

## Constraints

- Messages are in **Albanian only**
- Only send to **Albanian mobile numbers** (+355, starting with 06X)
- Do NOT send to landlines, Italian numbers, or other international numbers
- Do NOT exceed 50 messages per day to avoid WhatsApp account flagging
- NEVER delete or overwrite lead data — only write to column I
- ALWAYS save Excel after each individual send
- ALWAYS test with `--dry-run` before live sending
