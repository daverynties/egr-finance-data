# EGR $9M parking deck bond: independent analysis brief (primary sources only)

Prepared Oct 8, 2026 (ET) for David. Written by Grok Bot (executor).

**Files used (primary only, copied into `codex-in/docs/`):**
- `parking-deck-bond-9M-debt-schedule.csv`
- `parking-deck-utilization-2025.csv`
- `parking-deck-traffic-memo-2025-11-10.pdf`, viewed as page images `-1.png` to `-5.png`
- `parking-deck-operating-cost-2026.pdf`, viewed as page images `-1.png` to `-4.png`
- `parking-deck-aug3-p239-247.txt` and image `-3.png`
- `parking-deck-scanned-pages-transcribed.md`. This is a transcription. I spot-checked it against the images.

**Not used:** the live page (`page.txt`) and all of the secondary AI write-ups, which are the dossier, dossier update, due-diligence, full-context, aug3-packet-findings and ai-assessment.

**Disclosure:** before David's "primary only" instruction reached me, I opened Claude's *superseded v1* assessment from Drive. I read its first ~40 lines and diffed it against the current file to check whether it was Muse's vote. It is Claude's. So I had seen Claude's bottom line before writing this brief. Every number below was recomputed from the primary files.

**Big caveat: the primary set is thin.** It does **not** contain:
- the total project cost or any engineer's estimate
- the deck design (240 spaces and 3 levels come from the task framing; the only primary hint is "three-story deck", in the Apr 23 email)
- the ballot language
- commission or board votes or minutes
- any city–school agreement
- the taxable value of a typical home
- whether parking will be free or public

All of those would need the full Aug 3 packet or other official records.

## 1. Key facts with citations

| Fact | Source |
|---|---|
| The HS expansion takes the senior lot (Lot 15, 111 spaces). The site plan keeps 40, "resulting in a net loss of 71 parking spaces." | traffic memo img -2 (Nov 10, 2025, p.1); transcription L21 |
| On-street study, Lake Dr–Argentina side streets: "average capacity of 111 parking spaces and a minimum of 89 parking spaces during a school day." This "should provide a sufficient amount of parking to accommodate the 71 lost" spaces. | memo img -2; transcription L22 |
| "There are not any known complaints about the current students using this parking." | memo img -2 |
| Middle school lot expansion: "up to 103" spaces, about 1,000 ft away, "at a less expensive price than a parking structure." | memo img -3, -4; transcription L25, L32 |
| Structure: "two (2) to four (4) level ... in the current location of Lot 11 ... 136–291 parking spaces." It would "also provide parking for Gaslight Village for after school hours." *(The transcription omits the Gaslight sentence.)* | memo img -3 |
| Load-out "anticipated to take 30 minutes to one (1) hour," which may lead students to choose on-street parking instead. Bagley "will likely experience traffic backing up in the morning." | memo img -3; transcription L28 |
| **Engineer's recommendation:** build the HS expansion "without any parking improvements." If problems occur, do the middle school lot next. A structure "should only be considered after other options have been explored." | memo img -3, -4; transcription L31–33 |
| Feb 4, 2026 follow-up: the schools' review says "some options and recommendations may not be feasible due to certain on-campus limitations." It names none and does not withdraw the recommendation. | memo img -1; transcription L14–16 |
| Lot sizes from the 9/12/25 map: Lot 11 (HS, Bagley) **49**, Lot 15 **111**, Lot 18 (MS) **63**, Lot 10 (private, paid) 183, Lot 17 (community center) 100. School lots are open after hours "But Not During School Events or Overnight." | memo img -5; transcription L37–45 |
| O&M figure: Grand Rapids (Mobile GR) uses **$611 per space per year**, "operations and maintenance (not depreciation)." For the three-story deck that "would be $130,143 per year." | op-cost img -1 (La Fave, Apr 23, 2026) |
| Shared Parking Manual Fig. 5-1 (2018 $), typical above-grade deck: construction **$12,500–$22,500 per space**. Basic O&M **$175 per space per year**. Sinking fund **$60 per space per year**. Security median $125. PARCS $375. Project cost = construction + 10% soft + 15% financing. | op-cost img -3; transcription L63–75 |
| Debt schedule: 20 levies (2027–2046). Principal **$9,000,000**, interest **$4,212,287**, total **$13,212,287**. | debt CSV L2–21 (summed) |
| 2025 counts cover 1,310 spaces: school 363, public/city 726, private-open 221. | utilization CSV |
| Public comment, May 27, 2026 session: 4 opposed or concerned (3 of them at 733–739 Bagley), 1 supportive, 2 neutral ideas. Emails: 1 unsigned form letter opposed (Jul 29); 2 asking for a public vote (Jul 23, Jul 28). | Aug 3 packet pp.239–247; .txt L7–51; transcription L92–156 |

## 2. Tax per household (recomputed from the debt schedule)

- **Millage check:** for every row, total_debt_service ÷ taxable_value × 1000 matches the CSV millage to within 0.0006 mill. No errors.
- **Underlying assumption:** citywide taxable value grows exactly **2.0%/yr**, from $1.119B to $1.630B.
- **Interest:** about 3.75–3.82% of the outstanding balance per year. The implied all-in yield is about **3.97%**.

**Dollars per year by taxable value (TV, not market value):**

| TV | Yr 1 (0.5922 mill) | 20-yr avg (0.4925) | Final yr (0.4069) | 20-yr total if TV stays flat |
|---|---|---|---|---|
| $100,000 | $59.22 | $49.25 | $40.69 | $985 |
| $150,000 | $88.83 | $73.87 | $61.03 | $1,477 |
| $200,000 | $118.44 | $98.49 | $81.38 | $1,970 |
| $250,000 | $148.05 | $123.12 | $101.72 | $2,462 |
| $300,000 | $177.66 | $147.74 | $122.07 | $2,955 |

**Why the falling millage overstates relief:** it falls only because the citywide TV is assumed to grow. If your own TV grows at the same 2%, your bill stays roughly flat at your year-1 share. That share is $662K × (your TV / $1.1186B), about **$59 per $100K of 2027 TV every year**, or about **$1,180 per $100K over 20 years**.

**What's not in the record:** the primary files don't give a typical home's TV. In Michigan, TV is at most half of market value and is usually lower. A home with a $400K market value and about $150–200K TV would pay roughly **$90–120 in year 1**.

## 3. Cost per space and per net added space

| Measure | Math | Result |
|---|---|---|
| City's $9M alone, 240 spaces | $9M ÷ 240 | **$37.5K per space** |
| City's $9M per *net added* space at the site | Deck replaces Lot 11's 49 spaces, so 240 − 49 = 191 net | **$47K** |
| City's $9M per net added campus space vs. today | Also loses 71 from Lot 15, so 191 − 71 = 120 net | **$75K** |
| *If* total cost is about 2 × $9M = $18M (half/half split assumed; not in primary files) | per space | **$75K** |
| | per 191 net | **$94K** |
| | per 120 net | **$150K** |
| Benchmark, Manual 2018 $ | $12.5–22.5K construction × 1.25 (soft and financing) = $15.6–28.1K | |
| Benchmark, CPI-adjusted to 2026 (my assumption, about +33%) | | **about $21–37K per space** |

On the assumed $18M total, the deck would cost about 2–3.5× the generic benchmark. One resident's card says "Cost is high at 100K per space" (packet img -3). Neither the actual total nor the split is in my primary set.

## 4. Utilization peaks (2025 CSV; 3 days; hourly)

- **All 1,310 spaces:** the peak is **939 occupied (71.68%) on Wed Mar 12 at 1 pm, leaving 371 empty**. Thu May 8 peaked at 917 (70.0%) and Sat May 10 at 909 (69.4%).
- **School lots (363):**
  - Weekday peak: 294 (81.0%), Wed 8 am.
  - Overall peak: **315 (86.8%), Sat May 10 at 1 pm**, then 85.4% at 2 pm. Those are the only hours above 85%.
- **Public/city (726):** max 477 (65.7%).
- **Private-open (221):** max 179 (81.0%).
- **Inference: remove the 71 Lot-15 spaces** and school capacity drops to 292. The Wed 8 am weekday school demand (294) would then *exceed* school capacity, by about 2, with no slack.
  - So a **campus shortage after the expansion is plausible**.
  - Area-wide, about 300+ spaces would remain open even at peak.
  - The engineer's count of 89–111 free on-street spaces covers the 71.
- Other caveats: the counts are from 2025, before construction. There is no event-day count (Wednesdays on Wealthy, games). Only one Saturday was counted.

## 5. Operating cost

| Basis | Math | Annual |
|---|---|---|
| City/GR figure, Apr 23 | $611 × 213 = $130,143 (the email's total implies **213 spaces**) | $130K |
| GR rate at 240 spaces | $611 × 240 | **$146.6K** |
| Manual basic + sinking fund, 2018 $ | ($175 + $60) × 240 = $56.4K; × about 1.33 CPI | **about $75K** |
| Plus median security | ($175 + $60 + $125) × 240 × 1.33 | about $115K |

- **Range:** about **$56–147K a year** for the whole deck, so roughly **$28–73K** for the city's half if the costs are split equally (split not in record).
- **Scale:** about $13 a year per $100K TV if the city's general fund carries all of $147K.
- **Who pays:** no budget line, revenue source or maintenance agreement appears in the primary files.
- **What the GR figure assumes:** it is for Mobile GR decks, which are staffed and paid. An unstaffed, free deck would be closer to the Manual's basic number.

## 6. Process facts (primary only)

- Nov 10, 2025: the engineer recommends no new parking first, then the middle school lot, and a structure only as a last resort.
- Feb 4, 2026: a softening letter that cites the schools' review, with no analysis. Same day, La Fave sends the Manual cost-to-own page to Anthony Morey.
- Apr 23, 2026: O&M estimate based on a "three-story deck."
- May 27, 2026: "Potential Parking Solutions" comment session.
- Jul 23–29, 2026: emails asking for a public vote. Mayor Favale forwards a form letter, calling it unsigned and part of "an email campaign" (packet .txt L15–19).
- Not in the primary set: ballot-placement vote counts, minutes, ballot language, and any intergovernmental agreement.

## 7. Strongest YES case

- The expansion removes 71 spaces. After that, weekday school demand (294 at peak) would already exceed the remaining school capacity (292).
- A deck at Lot 11 keeps students on campus with "no streets" to cross. It would also serve Gaslight after school (memo img -3).
- The middle school lot is itself "full during school hours" and full again in the evening, which limits it as an alternative.
- Debt cost is modest: about $59 per $100K TV per year at an implied rate of about 4%.
- Voters get to decide directly, which two residents asked for.

## 8. Strongest NO case

- **The city's own engineer said not to build a structure first.** On-street spare capacity (89–111) covers the 71 lost spaces. The middle school lot (+103) is the cheaper next step. The Feb 4 retreat gives no specifics.
- **Area-wide, 2025 peak use was 72%,** with 371 spaces empty. The only hours above 85% were one Saturday in school lots.
- **The deck has known operational downsides:** 30–60 minute load-out, Bagley morning backups, and a likely student preference for the street anyway.
- **Implied cost is high:** about $75K per space on an assumed $18M total, versus a $21–37K benchmark. Per net added campus space it is about $150K.
- **Operating cost is unfunded:** $56–147K a year with no named payer.
- **Binding terms are missing from this record:** free or public access, the cost split and maintenance are not documented.
- **Neighbors oppose it:** all the substantive opposition in the record is from Bagley residents (light, noise, traffic, views).

## 9. Net read (mine)

On the primary record alone, the case for a *campus* problem after the expansion is real. The case that *this deck, at this size and cost, with this city share*, is the right fix is weak. The city's own consultant ranked it last, and the record lacks cost detail, an operating plan and a binding agreement.

If I had to lean, I'd lean **No (about 60–65%)**. That would flip toward Yes with a published, itemized cost estimate, a signed city–school agreement covering public access and O&M, and an explanation of why on-street parking and the middle school lot were ruled out.
