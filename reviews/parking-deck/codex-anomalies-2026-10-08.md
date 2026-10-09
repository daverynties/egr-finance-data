# Parking Deck Page Anomaly Audit

**Snapshot:** October 8, 2026, approximately 9:24 p.m. ET  
**Page:** https://egr-finance.vercel.app/parking-deck/  
**Method:** Offline review of the supplied HTML, rendered DOM, screenshots, link-status results, and reference files. Line numbers below refer to `site/index.stripped.html`.

## Executive summary

No critical defect was established. The most consequential findings are:

- Household tax projections omit the assumption that the homeowner’s taxable value stays constant.
- The stated general-fund balance cannot cover the page’s stated full City share.
- The school allocation and City borrowing cap leave an unexplained gap at the upper project estimates.
- Several supporting sources were inaccessible in the prefetched link checks.
- Campus counts use inconsistent baselines, and two campaign verdicts exceed the evidence described in their explanations.
- The eight principal sections are absent from the heading hierarchy. Navigation state and dark-mode chart contrast also have defects.

The principal debt and utilization arithmetic checks out. The screenshots and render report show no horizontal overflow, overlapping content, broken internal anchors, duplicate IDs, or page JavaScript errors.

**Evidence limitation:** The operating-cost and traffic-memo reference text files contain only form-feed characters. They provide no readable source text. Consequently, claims requiring those documents’ contents could be assessed for internal consistency and citation quality, but not independently verified.

## Critical

**None established from the supplied evidence.**

## High

### H01 — Household lifetime tax estimate omits its constant-taxable-value assumption

**Current text**

> “For a median home—about $521,000 market value and roughly $200,000–$260,000 taxable value—the model implies about $98–$128 a year on average, $118–$154 in year one, or $1,970–$2,560 over 20 years.”

**Location:** Financing, line 457; growth assumption at line 454.

**Why it is anomalous:** The quoted lifetime totals multiply the declining millage schedule by a constant homeowner taxable value. The page simultaneously describes a model assuming 2% annual taxable-value growth, without distinguishing aggregate growth from growth of an individual home.

Using the supplied schedule:

```text
Sum of 20 annual millages = 9.8494
Average millage = 9.8494 / 20 = 0.49247

Constant $200,000 taxable value:
20-year tax = $200,000 × 9.8494 / 1,000 = $1,969.88

Constant $260,000 taxable value:
20-year tax = $260,000 × 9.8494 / 1,000 = $2,560.84
```

If an individual home’s taxable value grows 2% annually:

```text
20-year tax = Σ[starting taxable value × 1.02^year × annual mills / 1,000]

Starting at $200,000: $2,362.40 total; $118.12 annual average
Starting at $260,000: $3,071.12 total; $153.56 annual average
```

That is approximately **19.9% more** than the constant-value scenario. Individual taxable-value growth is not established by the supplied files, so the growing-value result is a conditional illustration.

**Confidence:** High on arithmetic; medium on the intended homeowner assumption.

**Suggested fix:** Explicitly label the existing figures “assuming your taxable value remains constant.” Present a separate growth scenario and explain that the model’s citywide growth assumption does not determine an individual homeowner’s taxable value.

### H02 — General-fund balance is insufficient to pay the stated full City share

**Current text**

> “Using reserves could reduce borrowing, but paying the full City share from that balance would substantially reduce the cushion and would not solve ongoing operating costs.”

**Location:** Financing, line 458. City-share range appears in Cost, line 442.

**Why it is anomalous:** The same page states a balance of **$6,511,815** and a City share of **$7.6M–$9.1M**. Paying that entire share from the identified balance is impossible:

```text
$7,600,000 − $6,511,815 = $1,088,185 shortfall
$9,100,000 − $6,511,815 = $2,588,185 shortfall
```

Even exhausting the balance leaves a funding gap. “Substantially reduce the cushion” understates the problem.

**Confidence:** High.

**Suggested fix:** State that the identified balance cannot cover the full share, and quantify how a partial reserve contribution would affect borrowing and remaining reserves.

### H03 — Funding amounts do not reconcile with the upper project estimates

**Current text**

> “Up to $9M in city bonds”

> “~$7M”

> “The City’s half—about $7.6M–$9.1M”

**Location:** Proposal at a glance, lines 356–361; executive summary, lines 372–374; Cost, line 442.

**Why it is anomalous:** The displayed school allocation and City borrowing cap provide approximately **$16M**. The reference cost estimates exceed that amount:

```text
2026 brick estimate:
$16,905,675 − ($9,000,000 + $7,000,000) = $905,675 gap

2028 brick estimate:
$18,109,782 − ($9,000,000 + $7,000,000) = $2,109,782 gap

Half of the 2028 brick estimate:
$18,109,782 / 2 = $9,054,891
```

An exact equal split at that upper estimate exceeds the City bond cap by **$54,891**. The page identifies an unsigned agreement, but does not reconcile these funding amounts.

This establishes an unexplained funding gap under the displayed assumptions; it does not establish that no additional funding could become available.

**Confidence:** High on arithmetic; medium on final funding arrangements.

**Suggested fix:** Distinguish the school’s current allocation, proposed ultimate contribution, City borrowing authority, and any additional funding required for each design/year scenario.

### H04 — Important source links were inaccessible in the supplied checks

**Current text**

> “EGRPS superintendent’s September 30, 2026 letter”

> “Kent County 2024 Apportionment Report”

> “U.S. Census Bureau QuickFacts”

**Location:** Sources 18, 20, and 23; lines 583, 585, and 588.

**Why it is anomalous:** `link-status.txt` records:

| Source | Prefetched result | Page claims affected |
|---|---:|---|
| 18 — Google Drive letter | **401** | Approximately 65 construction-period spaces; school-event “no fee” statement |
| 20 — County report | **403**, following one redirect | Comparative city millages |
| 23 — Census QuickFacts | **403** | Median home value used in household illustration |

The 401 response prevents anonymous verification in the recorded check. The 403 responses could reflect automated-access restrictions; the files do not prove that ordinary browser visitors are also blocked.

**Confidence:** High on recorded statuses; medium on the cause of the 403 responses.

**Suggested fix:** Make the school letter publicly readable. Replace or supplement blocked references with publicly accessible official documents or permitted copies, and verify anonymous access.

## Medium

### M01 — Campus counts and the City’s incremental-space calculation use inconsistent baselines

**Current text**

> “The senior lot had 111 spaces; the expansion plan retains 40, creating a 71-space reduction.”

> “216”

> “144”

> “≈335”

> “The City’s half—about $7.6M–$9.1M—therefore buys roughly 118 spaces beyond that”

**Location:** Need, lines 413 and 416–419; Cost, line 442; Alternatives, line 498.

**Why it is anomalous:**

```text
111 − 40 = 71 spaces lost
216 − 71 = 145 remaining, rather than 144

Using the displayed 144:
144 − 49 + 240 = 335
240 − 49 = 191 added versus the no-deck condition

Two-story option:
144 − 49 + 118 = 213 campus spaces

Increment from that two-story option to the proposed deck:
335 − 213 = 122 spaces, rather than 118

Increment over the original 216-space campus:
335 − 216 = 119 spaces
```

The reference findings also describe approximately 334 spaces and an approximately 118-space increment. These appear to mix historical or rounded baselines. The page does not explain the differences.

Using 122 incremental spaces changes the displayed City cost calculation:

```text
$7.6M / 122 = approximately $62,295 per space
$9.1M / 122 = approximately $74,590 per space
```

**Confidence:** High on internal arithmetic; medium on which underlying campus count is authoritative.

**Suggested fix:** Publish a single reconciliation showing retained lots, removed lots, deck capacity, and each comparison baseline. Explain the additional one-space loss if 144 is correct.

### M02 — The $160K operating-cost callout is not reconciled with its own calculation

**Current text**

> “What $160K means”

> “At 240 spaces that is about $147,000.”

> “The City’s stated estimate is consistent with one routine-operations benchmark for the whole structure.”

**Location:** Cost, lines 441 and 444.

**Why it is anomalous:** The displayed calculation produces:

```text
$611 × 213 = $130,143
$611 × 240 = $146,640
$160,000 − $146,640 = $13,360
```

The $160K figure is **9.1% higher** than the scaled benchmark. That could reflect rounding, escalation, or additional expenses, but none is identified.

The lower annual estimate also lacks a reproducible inflation step:

```text
($175 operations + $60 repair fund) × 240 = $56,400 in 2018 dollars
```

Reaching $70K–$75K requires an inflation multiplier of approximately **1.241–1.330**. No index or calculation is supplied.

The upper calculation is reproducible if it adds a 1% reserve to the $146,640 benchmark:

```text
$146,640 + 1% × $15,246,696 = $299,106.96
$146,640 + 1% × $18,109,782 = $327,737.82
```

**Confidence:** High on arithmetic. The unreadable reference extraction prevents verification of the original correspondence.

**Suggested fix:** Identify the source and scope of $160K, explain its difference from $146,640, and show the inflation basis and reserve formula.

### M03 — “False / not in source” conflates contradiction with missing evidence

**Current text**

> “LOS F at Bagley & Lake”

> “False / not in source”

> “Neither the Nov. 10, 2025 memo nor the Feb. 4, 2026 letter contains any level-of-service analysis.”

**Location:** Campaign fact check, line 520. Verdict legend at line 538.

**Why it is anomalous:** The page defines “False” as “contradicted by record.” Its explanation establishes only that the attributed documents lack the analysis. An absent analysis does not establish the intersection’s actual level of service.

The supplied traffic-memo extraction contains no readable text, so the assertion about the documents’ contents cannot be independently confirmed here.

**Confidence:** High on the verdict’s internal logic; underlying traffic claim unverified.

**Suggested fix:** Rate the intersection claim “Unverifiable” and separately identify the attribution as unsupported, unless a source directly contradicts LOS F.

### M04 — “True” signal-cost verdict does not establish the claimed range

**Current text**

> “Signal costs $350K–$600K”

> “True”

> “The City used a placeholder of about $500K; the April memo says ‘up to $500,000.’”

**Location:** Campaign fact check, line 521.

**Why it is anomalous:** A $500K placeholder lies within the campaign range, but does not establish its endpoints. The claimed $600K upper endpoint exceeds the stated source maximum by:

```text
$600,000 − $500,000 = $100,000, or 20%
```

The explanation supplies no basis for the $350K lower endpoint.

**Confidence:** High on the mismatch between claim and explanation.

**Suggested fix:** Narrow the claim to the documented placeholder or use a qualified verdict explaining that the full range is unsupported.

### M05 — Timeline citations do not identify the later meeting records they claim to support

**Current text**

> “Ballot typo corrected, 4–1–2”

> “A special meeting corrected the millage language.”

> “Commissioner Schwartz said July 20: ‘the school needs two levels and the third is a possibility for the City.’”

**Location:** Governance & process, line 472; Cost, line 442. Source descriptions at lines 566 and 569.

**Why it is anomalous:**

- The August 6 event cites **Source 1, the August 3 agenda packet**.
- The July 20 quotation cites **Source 4, the July 20 agenda packet**. The supplied reference findings locate that quotation in July 20 minutes reproduced in the **August 3 packet, pages 248–251**.
- August 3 meeting outcomes likewise cite the August 3 agenda packet.

A pre-meeting agenda packet does not, by its described identity, establish subsequent votes or spoken remarks. A later revision could contain additional records, but the page does not identify one.

**Confidence:** High on citation-date mismatch; medium on whether a linked packet was subsequently augmented.

**Suggested fix:** Cite dated minutes or meeting recordings, including page numbers or timestamps. Cite the August 3 packet’s reproduced July 20 minutes for the Schwartz quotation.

### M06 — The parking-map citation links to a differently described document

**Current text**

> “City parking map, September 12, 2025”

> “Lot 11—the Bagley surface lot—shows 49 spaces; reviewed with the Progressive materials.”

**Location:** Source 22, line 587; relied upon at lines 384 and 419.

**Current target**

```html
href="https://safestreetsegr.com/documents/progressive-traffic-memo-2025-11-10.pdf"
```

**Why it is anomalous:** The described September map links to the November traffic memo, also used for Source 5. The 49-space count controls both the **191-space net addition** and the **335-space campus total**.

The map could be an attachment, but no page reference identifies it, and the supplied extraction cannot confirm its presence.

**Confidence:** High on target reuse and description mismatch; medium on whether the map is actually absent.

**Suggested fix:** Link directly to the map or identify its exact appendix/page in the combined PDF.

### M07 — All eight principal sections are missing from heading navigation

**Current HTML**

```html
<summary><span class="section-number">01</span><span class="section-title">Need<small>Current capacity is available; construction changes the campus math.</small></span><span class="chevron" aria-hidden="true"></span></summary>
```

**Location:** Lines 394, 431, 449, 466, 489, 509, 543, and 563.

**Why it is anomalous:** Section titles 01–08 are spans. `render-report.json` confirms that the heading outline contains the H1, the executive-summary H2, and numerous H3s, but none of the eight main section titles.

Readers using heading navigation cannot jump to Need, Cost, Financing, or Sources. Subsequent H3s lack their intended H2 parents.

**Confidence:** High.

**Suggested fix:** Give each section title an H2 within the disclosure summary, preserving the disclosure control and keeping its subtitle separate.

### M08 — Navigation visibility and `aria-expanded` disagree

**Current HTML/CSS**

```html
<button class="nav-group-label" type="button" aria-expanded="false">Overview</button>
```

```css
.nav-group:hover .nav-menu,
.nav-group:focus-within .nav-menu,
.nav-group.open .nav-menu{display:grid}
```

**Location:** Lines 227, 323–331, 293, and 623–634.

**Why it is anomalous:** Hover or keyboard focus opens a desktop menu without changing `aria-expanded`. Closing its `.open` class while focus remains inside still leaves it visible through `:focus-within`.

On mobile, group links are displayed when the main menu opens, but the group buttons remain `aria-expanded="false"` and their click handlers return without acting.

**Confidence:** High from the CSS and JavaScript; interaction behavior was not independently browser-tested.

**Suggested fix:** Control desktop visibility and expanded state through one consistent mechanism. Use noninteractive group labels on mobile, or implement real group disclosures.

### M09 — Dark-mode chart label has approximately 1.72:1 contrast

**Current HTML**

```html
<text x="440" y="79" text-anchor="middle" class="value" style="fill:#fff">81.0%</text>
```

**Location:** Chart, line 406; dark teal variable at line 204.

**Why it is anomalous:** Dark mode changes the bar fill to `#6dd7c8`, while the in-bar label remains white.

```text
White (#ffffff) against dark-mode teal (#6dd7c8):
contrast ≈ 1.72:1
```

This is below the 4.5:1 threshold for normal-size text. The light-mode combination is approximately 6.12:1.

**Confidence:** High from the declared colors; dark mode is not shown in the supplied screenshots.

**Suggested fix:** Use a theme-aware label color or place all value labels outside the bars with the normal text color.

### M10 — Chart labels become approximately five pixels tall on mobile

**Current text**

> “System peak”

> “School weekday”

> “School Saturday”

**Location:** Chart, lines 401–407; mobile CSS, line 166; `screenshots/mobile-part01.png`.

**Why it is anomalous:** The SVG retains a 760-unit viewBox. At the supplied 390px viewport, its drawable width is approximately 334px. A 12-unit text size therefore renders at:

```text
12 × 334 / 760 ≈ 5.27 CSS pixels
```

The screenshot visibly shows extremely small axis and category labels. The prose and chart alternative provide the numbers, but the mobile visual is difficult to read.

**Confidence:** High.

**Suggested fix:** Create a mobile chart layout with larger labels, or show the three measurements in a compact accessible table at narrow widths.

### M11 — Social-preview image returns 404

**Current HTML**

```html
<meta property="og:image" content="https://egr-finance.vercel.app/parking-deck/assets/share-card.png" />
<meta name="twitter:image" content="https://egr-finance.vercel.app/parking-deck/assets/share-card.png" />
```

**Location:** Head, lines 11 and 15.

**Why it is anomalous:** `link-status.txt` records **404** for the shared image URL. Both social metadata systems reference the same missing asset.

**Confidence:** High.

**Suggested fix:** Deploy the image at that URL or update both tags to a working image, then verify its response and content type.

## Low

### L01 — Canonical declaration is absent and the favicon is intentionally empty

**Current HTML**

```html
<meta property="og:url" content="https://egr-finance.vercel.app/parking-deck/" />
<link rel="icon" href="data:," />
```

**Location:** Head, lines 8 and 18.

**Why it is anomalous:** There is no canonical link in either supplied HTML version. `og:url` does not substitute for a canonical declaration. The favicon points to an empty data URL, yielding no identifiable site icon.

No duplicate-indexing problem is established by the files.

**Confidence:** High on markup; low on any actual SEO impact.

**Suggested fix:** Add a self-referencing canonical link and a valid favicon.

### L02 — Six numbered sources have no corresponding inline citation

**Current text**

> “June 29, 2026 City Commission packet”

> “Safe Streets EGR”

> “East Grand Rapids Citizen Portal”

> “East Insider”

> “FOX 17 regional reporting”

> “EGR community-group threads”

**Location:** Sources 3 and 11–15; lines 568 and 576–580.

**Why it is anomalous:** Counting `.cite` links shows no inline references to these six source numbers. Each nevertheless has a “Back to cited section” link. Source 3 overlaps cited Source 8, but the other entries’ relationship to specific claims is unclear.

**Confidence:** High.

**Suggested fix:** Cite the entries where used, or place them in a clearly labeled additional-reading list and change their return-link labels.

### L03 — Most citation links expose only a number, and return links do not identify their destination

**Current HTML**

```html
<a class="cite" href="#s21">21</a>
```

```html
<a class="source-back" href="#summary" aria-label="Back to cited section">↩</a>
```

**Location:** Example citation at line 374; source return links at lines 566–589.

**Why it is anomalous:** Only the introductory citation explicitly labels itself “Source 1.” Most others expose a bare number. Every return link uses the same accessible label, despite different destinations.

Source 1 is cited in several sections, but its return link always goes to the executive summary.

**Confidence:** High.

**Suggested fix:** Give citations accessible names such as “Source 21: EGRPS Board minutes.” Label return destinations explicitly, or return to individual citation IDs.

## Verified calculations and findings not flagged

| Check | Independent result |
|---|---|
| Principal total | **$9,000,000** |
| Interest total | **$4,212,287** |
| Total debt service | **$13,212,287**, supporting “$13.21M” |
| Debt-service rows | Principal + interest equals total in every row |
| Average scheduled millage | **0.49247**, rounding to **0.4925** |
| Year-one millage | **0.5922**, matching the CSV |
| Year-one household tax | $200K × 0.5922 / 1,000 = **$118.44**; $260K gives **$153.97** |
| Peak system occupancy | **939 / 1,310 = 71.6794%**, rounding to **71.7%** |
| Empty spaces at system peak | **1,310 − 939 = 371** |
| School weekday peak | **294 / 363 = 80.9917%**, rounding to **81%** |
| School Saturday peak | **315 / 363 = 86.7769%**, rounding to **86.8%** |
| Utilization CSV integrity | No negative occupancy, occupancy above capacity, duplicate date/hour/category rows, or component-total discrepancies found |
| SVG bar proportions | 129/180 = **71.67%**; 146/180 = **81.11%**; 156/180 = **86.67%** — consistent within pixel rounding |
| SVG benchmark | (205 − 52)/180 = **85%** |
| Net-space cost using 191 spaces | $15,246,696/191 = **$79,826**; $18,109,782/191 = **$94,816**, supporting **$80K–$95K** |
| Benchmark premium | 240 × $42K = **$10.08M**; difference from the reference cost endpoints = **$5.17M–$8.03M** |
| Local levy components | **11.35 + 1.73 + 1.01 = 14.09 mills** |
| Vote totals | 5–2 = seven; 4–1–1 = six, consistent with the stated departure; 4–1–2 = seven |
| Timeline | April 20 to August 3 is **105 days**, supporting “under four months” |
| Date freshness | “Last reviewed October 8, 2026” matches the snapshot. October 9 UTC HTTP dates correspond to October 8 ET |
| Accessibility already present | English language declaration, skip link, main/navigation landmarks, textual verdict labels, and a numerical chart alternative |
| Render checks | No reported page JS errors, overflow, duplicate IDs, broken internal anchors, or missing image `alt` attributes |

The split screenshot boundaries do not establish actual text clipping. No TODO, lorem ipsum, actionable development notes, or misleading hidden text was found. The supplied evidence does **not** include robots.txt or sitemap status checks, so no 404 finding is warranted for those endpoints.