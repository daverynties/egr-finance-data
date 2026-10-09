# Content review: EGR Parking Deck Bond Guide
**Page:** https://egr-finance.vercel.app/parking-deck/ (live HTML is byte-identical to `site/parking-deck/index.html` at repo HEAD `dfdee7f`, pulled Oct 8, 2026, ~10:25 PM ET)
**Reviewer:** Grok Bot, Oct 8, 2026. Review only: nothing in the site, repo, or Drive was edited.
**Scope (per the organizer):** content only, covering accuracy against the primary sources, fairness, clarity, completeness, order, framing, overreach, redundancy, and whether the page's conclusions are supported. Rendering, fonts, accessibility, meta/SEO and link-status checks were dropped on purpose.

**Sources checked against:** [local path] (debt-schedule CSV, utilization CSV, traffic memo plus Feb 4 letter transcriptions, operating-cost emails, Aug 3 packet findings, comment-card transcriptions, research dossier plus Oct 9 update, due-diligence notes, Claude assessment) and the prior reviews in `reviews/parking-deck/`. Page text extract: [local path].

---

## Summary

The factual core is strong. Every number I recomputed checks out:
- debt service is $9,000,000 + $4,212,287 = $13,212,287
- average levy 0.4925 mills, year one 0.5922 mills
- $49 per $100K average, $59 year one, $985 over 20 years
- utilization peak 939/1,310 = 71.68%; school category 81.0% weekday and 86.8% Saturday; public lots at most 65.7%
- $63.5K–$75.5K per stall and $80K–$95K per net new space
- the $42K × 240 = $10.08M benchmark
- 3.5% escalation

Most fixes from the earlier review have been made: the comment-card tally, the 145 figure, LOS F, the East Insider attribution, the Drive link, and the "$160K" callout.

Three things hold it back:

1. **The AI-vote layer undercuts the "independent voter guide" framing.** The two-minute summary at the top shows four AI models all leaning or voting No, and the AI section is close to half the page. On a live ballot measure, this works like a No recommendation, whatever the disclaimers say. It also misstates Claude's position: Claude declined to vote. And it carries leftover chat text ("the model powering this assistant").
2. **Some important money figures are framed wrong or incompletely:**
   - The $160K operating figure is described as the City's *share*, but the record has it as the *whole deck* split 50/50.
   - The "$9M + ~$7M ≈ $16M falls within the OAK range" line hides a funding gap. $16M is below four of the six OAK estimates, including every 2028-dollar case.
   - "$15.2M–$18.1M total project" is really a deck-only estimate. The signal and other extras sit outside it.
   - The household tax is shown at flat taxable value. That understates what a typical household pays when its taxable value rises.
3. **A voter's basic questions go unanswered or are buried:**
   - What exactly is on the ballot?
   - What happens if Yes or No wins?
   - Who can park there during school hours? (The district letter says about two-thirds of the deck is school-only then.)
   - Can it open before the 2028–2030 crunch?
   - Where is parking tight *near the school* today?

   The page also leaves out evidence that cuts toward Yes, which hurts balance: near-school streets and lots ran 106%–233% full in the study.

### Overall grade: **C+**
- **Factual guide sections (Overview through Risks): B+.** Accurate, well sourced and unusually transparent about inference. Docked for the money-framing problems above, a few unsourced or overbroad lines, jargon, and Yes/No asymmetries in the fact-check notes.
- **AI analysis plus its teaser in the summary: D.** It misrepresents one model, it isn't independent (Muse built the page and then voted on it), it repeats the factual sections three times, and it tilts the page.
- If the AI votes come out of the summary and the eight Critical/High items below are fixed, the page would be a solid **B+/A−** neutral guide.

### Count by priority
| Priority | Count |
|---|---|
| Critical | 3 |
| High | 9 |
| Medium | 14 |
| Low | 10 |
| **Total** | **36** |

---

## Prior-review checklist (from `reviews/parking-deck/README.md` and the Codex fix list)

| # | Prior finding | Status now | Note |
|---|---|---|---|
| 1 | Source [18] (Sept 30 letter) linked to private HANDOFF Drive doc | **Fixed (link removed)** | Now reads "Copy not publicly available online." But the headline "~65 spaces" and the "no fee" claim now rest on a source readers can't see. See M-1. No drive.google.com links remain on the page. |
| 2 | $9M + ~$7M vs $16.91M / $18.11M unexplained | **Still present, reworded** | Now says "~$16M, which falls within the OAK range." True of the range's endpoints, but it hides the gap. See H-2. |
| 3 | Reserves: "substantially reduce the cushion" | **Still present** | See L-3. |
| 4 | Comment cards: unsigned card counted as Bagley | **Fixed** | "three … from Bagley Avenue residents, a fourth opposed card that is unsigned and lists no address" matches the transcription. |
| 5 | "90 minutes" unattributed | **Mostly fixed** | Now attributed to East Insider, but it still says "before the August 3 *vote*" (the source says *meeting*). Source [13] also links the wrong East Insider article. See M-9. |
| 6a | LOS F rated "False" | **Fixed** | Now "Not in source," which is correct. |
| 6b | Signal "$350K–$600K True" | **Fixed differently** | The claim was relabeled "Signal cost about $500K" and rated True. That isn't WalkSafeEGR's actual claim, which was $350K–$600K. See L-5. |
| 7a | 216 − 71 = 144 | **Fixed** (145) | |
| 7b | "$160K" heading never explained | **Fixed, but the explanation is wrong** | The new text calls $160K the City's *share*. See H-1. |
| 7c | Source [22] (parking map) links the wrong PDF | **Still present** | It links the operating-cost PDF, but the 9/12/25 map is page 5 of the traffic-memo PDF ([5]). The description "reproduced in the City parking-deck operating-cost materials" is also wrong. |
| 7d | share-card.png 404, fonts, chart size | Out of scope now | Noted only: `og:image` still points to `/parking-deck/assets/share-card.png`, which returns 404. The file exists at `/assets/share-card.png`. |
| C1 | 85% benchmark attributed to Shared Parking Manual [16] | **Still present** | Source [16] still says "85% utilization benchmark," and the Need text cites [8][16] for it. Fig. 5-1 is a cost table. See M-10. |
| C2 | Walker $42K benchmark sourced to June 29 packet [17] | **Still present** | The source is Walker's 2026 Saugatuck summary. |
| C3 | Schwartz quote cites July 20 packet [4] | **Still present** | The minutes are reproduced in the Aug 3 packet, pp. 248–251. |
| C4 | Third-level math (118 vs 122 spaces) | **Still present** | See M-4. |
| C5 | "Realistic full annual cost" | **Still present** | See H-1. |
| C6 | "Key primary-source finding" callout favors Nov. memo | **Still present** | See M-6. |
| C7 | "Bottom line" editorial ranking | **Still present** | See M-7. |
| C8 | Household tax shown as a measured median bill | **Still present** | See H-4. |
| C9 | City seal beside "Independent voter guide" | **Still present** | Commit `c9b63c0` says "seal kept," so this is a deliberate choice by the organizer. Flagged Low (L-1) for the record only. |
| C10 | Alternatives table "About $0," "~118–136" | **Still present** | See M-5. |
| C11 | Overbroad "public record does not show" | **Still present** | See M-11. |

---

## CRITICAL

### C-1. AI votes in the top summary turn the guide into a de facto "No" recommendation
- **Where:** Overview / Quick Summary, "What the four AI models said" block. About block ("Four independent models … published their votes in the AI Analysis tab"). Meta/og description ("plus a clearly labeled four-model AI analysis").
- **Current text:** "What the four AI models said / Claude — Lean no… / Codex — No, 80% confidence… / Grok — Lean no, 60–65%… / Muse — No—the $9 million request comes before the governing terms…"
- **What's wrong:**
  - This is the third thing a voter sees, ahead of the factual guide. A 4-for-4 No tally inside a page titled "Independent voter guide," on a measure decided Nov 3, reads as an endorsement.
  - The disclaimer ("do not tell anyone how to vote") appears only further down, in the AI section.
  - It conflicts with the site's own ground rules in the Muse task list ("Neutral tone: facts, sources, context. No adjectives that judge"; ballot content "stays neutral and factual").
  - Agreement among the models is not independent evidence. Muse wrote the guide and then voted on it. Claude worked from Muse's guide. Codex fact-checked the guide. The page's own caveat ("Agreement among models is not evidence…") is buried at the bottom of the AI section.
- **Suggested fix:**
  - Delete the "What the four AI models said" block and the "Read the full AI analysis" button from the summary.
  - Strike "Four independent models… published their votes in the AI Analysis tab" from the About block.
  - Change the meta/og descriptions to: "A source-backed guide to the cost, need and process behind East Grand Rapids' Nov. 3, 2026 parking deck and pedestrian-safety bond."
  - Preferred: move the AI analysis to a separate page (for example /parking-deck/ai-analysis/) with the disclaimer as its first line, or drop it until after Nov 3.
  - Minimum: keep it as the last tab, and never surface vote outcomes in the summary.
- **Evidence:** pd-text.txt lines 24, 65–75. MUSE TASKS "Ground rules." Inputs described at pd-text line 360.

### C-2. Claude's position is misstated as "Lean no"
- **Where:** Summary ("Claude — Lean no—the need is real, but key terms are not binding."). Comparison table ("Claude | Leans no | Not quantified"). About block ("published their votes").
- **What's wrong:** Claude's assessment says, verbatim: "The AI doesn't vote. It also won't cast a personal yes or no on a live ballot question, especially one that may appear in a public voter guide." It then says "The record as it stands leans against this proposal as written." Calling that a vote of "Lean no" puts words in the source's mouth. `vote-comparison.md` also records "Declines to vote personally."
- **Suggested replacement:**
  - Table: "Claude | Declined to vote | — | Said the record 'as it stands leans against this proposal as written' | Signed agreement, itemized estimate, two-level price, schedule and funded upkeep."
  - Anywhere else: "Claude declined to cast a vote; it said the record leans against the proposal as written."
- **Evidence:** `parking-audit/docs/parking-deck-ai-assessment.md` lines 21–23. `reviews/parking-deck/vote-comparison.md`.

### C-3. Leftover assistant text and undisclosed conflict in Muse's entry
- **Where:** AI analysis, "Muse's assessment (Oct 8, 2026)."
- **Current text:** "Model: Muse Spark 1.3 (Meta) — the model powering this assistant · Input: assembled guide and primary-source record"
- **What's wrong:**
  - "the model powering this assistant" is chat-session text pasted onto a public page. There is no "assistant" on the page.
  - It also understates the conflict: Muse *built this page* and then rated the proposal using a guide it wrote.
  - No Muse vote existed when the earlier reviews were done tonight ("No Muse vote was found"). Its provenance isn't documented.
- **Suggested replacement:** "Model: Muse Spark 1.3 (Meta) · Input: this guide, which Muse also drafted, and the primary-source record. Because Muse built the guide, its view is not independent of the page's framing." Better still, remove Muse's vote (see C-1).
- **Evidence:** pd-text line 442. `reviews/parking-deck/README.md` line 21.

---

## HIGH

### H-1. The $160K operating figure is described as the City's share; the record has it as the whole deck
- **Where:** Cost section, "What $160K means" callout. Codex table ("$160K | City's stated figure for its share of operations"). Grok section ("The City's stated $160,000 figure is for its share of annual operations").
- **Current text:** "$160,000 is the City's stated figure for its share of annual operations. It is consistent with one routine-operations benchmark for the whole structure…"
- **What's wrong:**
  - The research dossier lists the City's Aug 3 figure as "~$160,000 … stated estimate, split 50/50 with schools … for 240 spaces." It says the open question is "where the city's ~$80K share comes from." Muse's own context file calls it "~$160,000/year in ongoing deck maintenance and operations."
  - The callout also contradicts itself: it calls $160K the City's share, then says it matches a benchmark "for the whole structure."
  - The paragraph above it says "The City's figure traces to a deputy city manager's April 23 email … $130,143." But the transcription notes say that file "is not a city breakdown of the $160K." $130,143 ≠ $160,000, so "traces to" overreaches.
  - "Realistic full annual cost is therefore about $70,000–$330,000" turns illustrative scenarios into a finding.
- **Suggested replacement:**
  - "The City has cited about $160,000 a year to operate the deck, to be split with the schools. It has not published a breakdown. For comparison, a deputy city manager's April 23 email cites Grand Rapids' $611 per space per year, 'not depreciation,' or $130,143 for the 213-space April design (about $147,000 at 240 spaces, inferred). The Shared Parking Manual the City circulated implies about $56,000 a year in 2018 dollars for basic operations plus a repair sinking fund. Adding a 1%-of-construction repair reserve to the $147,000 case gives about $300,000–$330,000 (inferred). These are benchmark scenarios, not a City budget. No dedicated funding source has been identified for either partner's share."
  - Retitle the callout "Where the $160K comes from." Fix the matching rows in the Codex and Grok sections.
  - Before publishing, confirm the Aug 3 wording, either from the meeting video or from the City.
- **Evidence:** dossier §9, line 193, line 198. `parking-deck-full-context.md` line 20. Transcription §2 ("This is not a city breakdown of the $160K").

### H-2. "$9M + ~$7M ≈ $16M falls within the OAK range" hides a funding gap
- **Where:** "What is proposed" card. Cost section (same sentence repeated). Codex table ("About $16M combined, within the OAK range"). Claude YES list ("The school pays half").
- **Current text:** "The $9M city bond plus the school's ~$7M set-aside totals ~$16M, which falls within the OAK range; the exact split of the final cost has not been published."
- **What's wrong:**
  - The OAK estimates are $15.25M / $15.78M / $16.33M (utilitarian, 2026/27/28 dollars) and $16.91M / $17.50M / $18.11M (brick).
  - $16M covers only the two cheapest cases. It falls short of every 2028-dollar case, which is when construction would happen, and every brick case.
  - The planned split is 50/50 (July 22 deck, City memo), which puts each side at $7.6M–$9.1M. The school's ~$7M is $0.6M–$2.1M short of half.
  - The $9M cap is roughly half the top estimate *with no contingency*. The City Manager said the original $10M was "Option 1 in 2028 dollars with roughly $1 million contingency."
  - The page never tells voters who covers overruns, and doesn't explain that the $9M must also fund the City's part of the signal and pedestrian work.
  - The Cost section says "City's portion would be about $8M–$9M," but $15.25M–$18.11M minus $7M is $8.25M–$11.1M.
  - "The school pays half" (Claude YES list) is unsupported.
- **Suggested replacement:** "The project is planned as a 50/50 city–school split, or about $7.6M–$9.1M each across OAK's estimates. The City's bond is capped at $9M, about half the highest estimate with no contingency. The school board has set aside about $7M, below half of any estimate. Together the two amounts (~$16M) would cover the utilitarian design in 2026 or 2027 dollars, but not the brick design or any 2028-dollar estimate. No published document says who pays if bids exceed the combined amount, or how much of the $9M goes to the signal and pedestrian work." (Mark "inferred" where it is arithmetic.)
  - In the third-level paragraph, replace "about $8M–$9M" with "about $7.6M–$9.1M under a 50/50 split (or up to the $9M cap)."
  - In Claude's YES list, change "The school pays half" to "The school would share the cost."
- **Evidence:** packet findings §1 ("Option 1 in 2028 dollars with roughly $1 million contingency"), §3 (OAK table). Dossier §15 "city–school agreement terms" ("capital split 50/50"). Arithmetic: 15.25 − 7 = 8.25 and 18.11 − 7 = 11.11.

### H-3. "$15.2M–$18.1M estimated total project range" is a deck estimate, not the total project
- **Where:** Summary "five facts" ("$15.2M–$18.1M / estimated total project range"). "What is proposed" card ("A three-level, 240-space deck, plus signals and pedestrian work" under the $15.2M–$18.1M heading).
- **What's wrong:** The OAK figures are deck construction estimates. The City Manager called $18M "the all-in cost for the construction of the deck." The page's own Risks section says signal work (~$500K placeholder), loading-dock changes and snow-melt are "not fully itemized." Calling it the total project, next to "plus signals and pedestrian work," overstates how complete the figure is.
- **Suggested replacement:** "$15.2M–$18.1M: OAK's deck estimates across façade options and 2026–2028 dollars. The traffic signal (City placeholder about $500K), loading-dock changes, snow-melt and pedestrian projects are not itemized in that figure."
- **Evidence:** dossier §6 (City Manager quote), §3 ("Other costs flagged as extra"). Page Risks "Undefined extras."

### H-4. The household tax figures assume your taxable value never rises, which understates the typical bill
- **Where:** Summary ("About $49 a year per $100,000 of taxable value—roughly $98–$128 a year for the median home."). Financing paragraph. Codex household table. Fact check ("$49/year per $100K … True").
- **What's wrong:**
  - The 0.4925 average comes from a schedule where debt service stays flat (about $660K a year) while *citywide* taxable value is assumed to grow 2% a year. A household whose taxable value grows with the city pays about **$59 per $100K of 2027 taxable value every year**, about **$1,181 over 20 years**, not $49 and $985.
  - At $200K–$260K taxable value, that is about $118–$154 a year and **$2,360–$3,070 over 20 years**, versus the page's $1,970–$2,560.
  - Also, $521K is a market-value median. The $200K–$260K taxable range is an assumption, and $260K is the 50%-of-market ceiling. Yet the summary states "for the median home" as fact, with no "inferred" tag.
  - The $49 figure is correct as a millage average. It's the dollar translation that's incomplete.
- **Suggested replacement (summary):** "What it costs you: about $59 per $100,000 of taxable value in the first year (0.59 mills), falling to about $41 by year 20 if citywide taxable value grows 2% a year as modeled. If your own taxable value grows at that pace too, your bill stays near $59 per $100,000 each year. Example: a home with $200,000–$260,000 taxable value would pay about $118–$154 a year (inferred). Check your taxable value on your assessment notice."
  - Keep the fact-check verdict on "$49/year per $100K" as True, adding: "…as the 20-year average millage; year one is about $59."
- **Evidence:** debt-schedule CSV (computed: 13,212,287 / 1,118,641,782 × 100,000 = $1,181; 662,429 / 1,118,641,782 × 100,000 = $59.22). Grok vote notes line 63. Dossier §15 "What a household actually pays."

### H-5. The ballot question itself is never quoted
- **Where:** Missing. The page names the "Public Parking Facility and Pedestrian Safety Bond Proposal" but never shows the wording voters will see.
- **What's wrong:** This is the most basic content of a voter guide. The page also never says what millage the ballot states (the Aug 6 typo fix changed 0.44925 to 0.4925) or that the bonds are *unlimited-tax* general obligation bonds, up to 20 years per series, prepayable.
- **Suggested fix:** Add a "What's on the ballot" box right under the hero with the verbatim question from the Aug 6 corrected resolution or the Kent County sample ballot. Add a one-line plain-English gloss: "Unlimited-tax means the City can levy whatever millage is needed each year to repay the bonds." Cite the resolution and sample ballot directly.
- **Evidence:** dossier §1 (2026-147 typo fix) and §7 ("Ballot wording: unlimited tax… 20 years per series… can be prepaid"). Packet findings §4 (label mismatch).

### H-6. No neutral "What a Yes vote / No vote means"
- **Where:** Missing from the factual guide. The only "what happens if No" text is inside the AI opinions ("A no is 'not yet': the city can return in May 2027").
- **What's wrong:** Voters' most common question is answered only by advocates, inside opinion text.
- **Suggested addition (all sourced):**
  - **YES:** The City may sell up to $9M in unlimited-tax bonds. The Commission still has to approve construction bids, a city–school agreement and the bond-sale terms, and may borrow less than $9M if bids come in lower.
  - **NO:** The City cannot issue these voter-approved bonds. The City Manager's memo says the next ballot opportunity would be May 2027. The superintendent's Sept 30 letter says the vote "will help inform whether the District continues or pauses" the deck. Under Michigan law the school district can build on its own campus without City zoning approval (FOX 17, July 21).
- **Evidence:** dossier §2 ("No signed agreement…Commission still has to approve bids…", "School can build alone", "District neutrality"). Packet findings §1 ("If deferred: … May 2027"). `parking-deck-full-context.md` line 18 ("may borrow less than $9M").

### H-7. Public access during school hours is missing
- **Where:** Summary and "What the deck adds." The page treats the deck as 240 spaces for school, events and Gaslight Village.
- **What's wrong:** The Sept 30 district letter says about **two-thirds of spaces are school-only during school hours**. The April concept had only L1 public. That leaves roughly 80 public spaces on school days. This is central to "what the City's half buys" and to the Yes argument about Gaslight. The page only says access "remain[s] open."
- **Suggested addition (in "What the deck adds"):** "Under the district's Sept 30 description, about two-thirds of spaces would be reserved for school use during school hours, leaving roughly 80 for the public on school days (inferred). Evenings, weekends and non-school days would be open to all, per the June 23 presentation. None of this is in a signed agreement." Cite a public copy of the letter (see M-1).
- **Evidence:** dossier §3 ("School-hours split: about two-thirds of spaces are school-only during school hours (Sept 30 letter)"). Packet findings §5.

### H-8. The Need section uses only system-wide numbers and leaves out the localized overflow near the school
- **Where:** Need section; summary "371 open"; fact check "'371 empty spaces' True."
- **What's wrong:**
  - Every utilization number on the page is an *aggregate* (system 71.7%, school category 81%/86.8%), and each favors the "no shortage" reading.
  - The same 2025 study shows specific near-school locations over capacity: San Lu Rae up to 233%, Greenwood about 150% from 9 a.m. to 3 p.m., Lake Dr behind the bleachers up to 150%, the senior lot 106%, and the Bagley HS lot 88%–98%.
  - The 371 open spaces are spread across 1,310, including Gaslight and private lots, and the page never says how many are within walking distance of the high school. The Yes side's point that students already park on side streets "from San Lu Rae to Ogden" is therefore supported by the data, and the page omits it.
  - Related asymmetry: the "Students would avoid a street crossing" True verdict gets a counterweight ("The memo also recommended proceeding without parking improvements"), but the "371 empty spaces" True verdict gets none.
- **Suggested addition (after the system-peak paragraph):** "The study also found specific spots near the high school over capacity: San Lu Rae (15 spaces) up to 233%, Greenwood (24) about 150% through the school day, Lake Drive behind the bleachers up to 150%, and the senior lot at 106%. The 371 open spaces at the system peak were spread across Gaslight, city and private lots; the study does not say how many were within walking distance of the high school."
  - Fact-check note for "371 empty spaces": "True for the whole 1,310-space system at its busiest hour; several lots and streets near the high school were over capacity."
  - Or, for symmetry, remove the extra sentence from the street-crossing verdict.
- **Evidence:** dossier §10 table "Lots over capacity." Utilization CSV. Codex neutrality table ("Aggregate capacity framed as generally available").

### H-9. "Every figure traces to a primary source" overclaims
- **Where:** About block.
- **Current text:** "Every figure traces to a primary source; 'inferred' figures are arithmetic from cited values."
- **What's wrong:** Several figures come from secondary or advocacy-hosted sources:
  - the 90-minute account and "no minutes" (East Insider, a commissioner's commentary)
  - vote detail via Citizen Portal (an AI summary)
  - the traffic memo and operating-cost PDFs hosted by Safe Streets EGR (the Yes campaign)
  - FOX 17 for "no signed agreement"
  - the Walker benchmark (a Saugatuck study)

  Some "inferred" figures also embed *assumptions*, not just arithmetic: CPI +25–33%, a 1% reserve, the $200K–$260K taxable value, 2% growth.
- **Suggested replacement:** "Figures come from official City and school records wherever possible; where we rely on news reports or documents hosted by a campaign site, we say so. 'Inferred' marks our own calculations, and the assumptions behind them are stated next to each one."
- **Evidence:** source list [5], [6], [12], [13], [16], [17]. Codex fix "Disclose primary-evidence limits in method."

---

## MEDIUM

### M-1. A headline number rests on a source readers can't see
- **Where:** "~65 left — campus spaces during 2028–2030 construction" [18]; "no fee" to event attendees [18]; source [18] "Copy not publicly available online."
- **What's wrong:** The 2028–2030 crunch is the main Yes argument, and the page's "strongest need case." Its only source is unlinked, and the earlier link was a private Drive doc.
- **Suggested fix:** Link the copy on egrps.org if one exists (check the district's joint-parking page [21]). Otherwise add "(letter to EGRPS families; quoted figures confirmed against a copy provided to the author)," or ask the district to post it. Don't re-add a Drive link.

### M-2. Timing gap: can the deck open before the 2028–2030 crunch? It's only in the Risks section and the AI opinions
- **Current text (Risks):** "The public record does not align a committed delivery date with the projected construction crunch."
- **What's wrong:** The Yes case leans on 2028–2030, but the facts that design is "paused at 50% design development until elected officials give direction" (July 22 deck) and that construction documents were targeted for January 2027 appear only in Claude's opinion text. A voter should see this next to "~65 left."
- **Suggested addition under the ~65 figure:** "Design is paused at 50% pending the vote (July 22 presentation). No published schedule shows when the deck would open relative to the 2028–2030 low point."
- **Also missing:** today's situation, which the dossier (citing the Sept 30 letter) gives as 77 campus spaces plus a temporary lot of about 150 for fall 2026.

### M-3. The cost history is missing
- **What's wrong:** Voters judging the "3.5% escalation" risk and the size growth would want the trajectory:
  - $10.54M construction basis (OAK, Aug 2024)
  - $13.6M for ~213 spaces (Apr 2026)
  - "$14M" (July 22)
  - $15.25M–$18.11M for 240 spaces (Aug 3)
- **Suggested addition (Cost section, one line or small table):** "Estimates have risen as the design grew: about $13.6M for a 213-space concept in April 2026, to $15.25M–$18.11M for 240 spaces in August." Cite the April memo, the July 22 deck and the Aug 3 packet.
- **Evidence:** dossier §6.

### M-4. Third-level math: "roughly 118 spaces beyond the school's stated need" should be about 122, and the dollar figure needs restating
- **Current text:** "…the City's portion would be about $8M–$9M and would fund roughly 118 spaces beyond the school's stated need—about $68,000–$76,000 each." The same figures are repeated in Claude's, Muse's and Codex's sections.
- **What's wrong:** The page's own inference puts the two-story deck at about 118 stalls. The 240-stall deck therefore adds about **122** beyond it (240 − 118). "118" is the number of spaces the 240 deck adds versus *pre-construction* campus (334 − 216), which is a different comparison. Pairing it with the wrong City-share range (H-2) compounds the error.
- **Suggested replacement:** "A two-story deck would hold about 118 stalls (inferred from the April memo's 213-space 'no net loss' campus total). The 240-stall design adds about 122 beyond that. If the City's half is $7.6M–$9.1M, that works out to about $62,000–$74,000 per additional stall (inferred). This is an allocation comparison, not a priced cost for the third level; no two-story price has been released." Apply the same fix in the AI sections or cut those repeats (see M-13).

### M-5. Alternatives table: precision and unsourced statuses
- **Current rows:**
  - "Use nearby on-street supply | 89–111 | About $0"
  - "Bussing / demand-management pilot | Not stated | Unpriced | Not pursued"
  - "Middle-school lot expansion … Deferred"
  - "Shared parking … Concept only"
- **What's wrong:**
  - "About $0" ignores the memo's own drawbacks (crossing Lake Drive, longer walk) and the near-school overflow (H-8).
  - "Not pursued," "Deferred" and "Concept only" have no citation.
  - The on-street row omits that the memo found 89–111 *available* spaces and that several of those streets were already over capacity.
- **Suggested replacement:**
  - "Use nearby on-street supply | 89 minimum, 111 average available on a school day (Nov. 2025 memo) | No cost estimate; requires crossing Lake Drive | First recommendation; Feb. 2026 letter says some options may not be feasible."
  - Replace the status cells with "Status not documented" unless a source is cited.

### M-6. The "Key primary-source finding" callout gives the November memo more weight than the February follow-up
- **Current text:** "Key primary-source finding / Build the high-school expansion without new parking."
- **What's wrong:** It reads like a direct quote and gets a highlighted box, while the Feb 4 letter qualifying it gets a plain paragraph. That's still flagged from the earlier review.
- **Suggested replacement:** Title it "What the traffic consultant said," with two equal-weight dated entries:
  - "Nov. 10, 2025: recommended building the expansion 'without any parking improvements'; on-street parking first, then the middle-school lot, a structure 'only … after other options have been explored.'"
  - "Feb. 4, 2026: 'some options and recommendations may not be feasible due to certain on-campus limitations' (options not named)."

### M-7. "Bottom line" box is editorial
- **Current text:** "The strongest need case is a projected 2028–2030 construction-period shortage, not present-day system overcrowding. The strongest unresolved issues are the unsigned city–school agreement, long-term upkeep, and the lack of binding commitments…"
- **What's wrong:** Ranking the "strongest" case is a judgment. It also frames the need case negatively ("not present-day…") while listing three open issues.
- **Suggested replacement:** Rename it "Key points." Text: "The 2025 counts found room system-wide (71.7% at peak) but tight spots near the high school. The expansion permanently removes 71 campus spaces, and the district projects about 65 campus spaces during 2028–2030 construction. Not yet settled: a signed city–school agreement, upkeep funding, school-hours public access, and any street-parking changes."

### M-8. The "Process" framing implies haste and leaves out the earlier history
- **Current text (section deck):** "The proposal moved from design funding to ballot language in under four months."
- **What's wrong:**
  - The subcommittee began meeting in August 2025.
  - OAK priced a deck in August 2024.
  - The two-story concept dates to the high-school design.
  - Starting the clock at April 20 makes the process look rushed.
- **Suggested replacement:** "A joint city–school subcommittee began meeting in August 2025; the Commission funded design in April 2026 and placed the bond on the ballot in August." Keep the dated cards.
- **Also:**
  - Explain "4–1–2" on Aug 6: "Yes: Burdick, Schwartz, Skaggs, Favale; No: Wessely; abstaining: Hunter, Groff-Blaszak."
  - Say why the amount is $9M: the City Manager proposed $10M ("Option 1 in 2028 dollars with roughly $1 million contingency"), and $8M/$9M/$10M versions were prepared after commissioners asked about a lower amount. That is the late 33-page document, and it gives voters context for both the "late resolution" item and the funding gap.

### M-9. "Late resolution" item: wrong source link and "vote" vs "meeting"
- **Current text:** "East Insider reported that a revised 33-page resolution arrived about 90 minutes before the August 3 vote and was not public beforehand." [13]
- **What's wrong:**
  - Source [13] links `eastinsider.substack.com/p/city-commission-preview-september`. The account is in Commissioner Groff-Blaszak's "Cutting through the noise" post.
  - The source says before the *meeting* (emailed at 4:23 p.m.).
  - The packet shows what it was: bond counsel's $8M/$9M/$10M versions with refined ballot language, prepared on request.
- **Suggested replacement:** "Commissioner Groff-Blaszak wrote in East Insider that revised resolutions totaling 33 pages, including the $8M, $9M and $10M versions, reached commissioners about 90 minutes before the August 3 meeting and were not posted publicly beforehand." Relink [13] to https://eastinsider.substack.com/p/cutting-through-the-noise-on-the and describe it as "a commissioner's published commentary."

### M-10. 85% benchmark: source misattributed
- **Current text:** "the commonly used 85% benchmark was not reached system-wide on the weekday." [8][16]. Source [16]: "85% utilization benchmark and 2018 operating/repair-reserve figures."
- **What's wrong:** Fig. 5-1 of the Shared Parking Manual is a cost table. The transcription shows no occupancy benchmark. The 85% figure appears on the page as the Yes/No campaigns' framing.
- **Suggested replacement:** "Parking planners commonly treat about 85% occupancy as effectively full. System-wide use stayed below that on all three study days; the school category passed it only on the Saturday (86.8% at 1 p.m.)." Drop [16] from that claim and fix [16]'s description to "2018 operating-cost and repair sinking-fund figures."

### M-11. Overbroad absence claims
- **Current text:**
  - "Meetings stayed below quorum, so no minutes exist. The public record does not show how key project choices were made." (no citation)
  - "No executed intergovernmental agreement was identified." (no citation, no date)
  - "No student survey was conducted…" (no citation)
- **Suggested replacements:**
  - "The joint subcommittee met below quorum, so no minutes were kept (East Insider). City memos and presentations describe some choices, but there is no record of the subcommittee's deliberations."
  - "As of [date checked], no signed city–school agreement had been made public (FOX 17 reported none signed on Aug. 4). The July 22 presentation outlines intended terms: a 50/50 capital split, operating costs from dedicated accounts likely managed by the district, and repairs approved by both boards." (This also gives the Yes side's position a fair hearing.)
  - "Commissioner Groff-Blaszak wrote that no student survey was conducted (East Insider)."

### M-12. Grok's section contains a baseline error
- **Current text:** "145 high-school spaces after the 71-space loss; the nearby middle-school lot brings the combined cited capacity to 292."
- **What's wrong:** 292 is the study's 363-space "school" category minus 71. It is not 145 plus the middle-school lot (145 + 63 = 208). The page uses three different "school capacity" baselines (216 campus, 363 study category, 1,310 system) and never reconciles them, which will confuse readers.
- **Suggested replacement:** "The 2025 study's school category (363 spaces, including the middle-school and other school lots) would fall to about 292 after the 71-space loss, against a measured weekday school peak of 294." Add a one-line note in the Need section: "Three counts appear on this page: 216 = high-school campus lots; 363 = all school lots in the 2025 study; 1,310 = all lots in the study area."

### M-13. Length and redundancy
- **What's wrong:**
  - The page is about 790 lines of text. The AI section is about 45% of it.
  - The same figures are restated four or five times: cost per stall, $80K–$95K, the household table, the operating-cost range, 371/939/1,310, 118 spaces/$68K–$76K. They appear in the Cost section, Claude's table, Codex's three tables, Grok's section and the fact check.
  - Each repeat is another place to drift out of sync (the $160K and 118 errors are copied into three sections).
- **Suggested fix:** Keep one canonical number set in the factual sections. Cut each AI entry to a vote line, three reasons, and "what would change it," linking back to the factual sections for numbers. Target roughly half the current length.

### M-14. Missing context that voters will ask about
Add short, sourced lines for each:
- **Where exactly the deck goes:** "on the current Bagley Ave high-school lot (Lot 11, 49 spaces), north of the high school." Note that Bagley Ave is posted No Parking and the design target grew from "220 +/-" to 240 when "the top level has been extended all the way to the north wall." The City Manager says that level may be snow storage in winter and "spaces can be reduced." (Packet §1.)
- **Neighborhood effects:** the traffic memo's "Bagley Avenue will likely experience traffic backing up in the morning" and the 30–60 minute exit. The shadow study says the shadow "clears the residences" at worst case. These are on the record and currently appear only in fragments.
- **Gaslight history:** the 2004 PUD required the private structure be "retained and maintained" and made available for high-school events. It was removed in January 2025. On Aug 10, 2026 a judge voided the new development's approval, and the City says "there is currently no project in front of us." This is directly relevant to the "serve Gaslight Village" argument and to Commissioner Hunter's request that the deck "go away if the PUD goes through." (Dossier §12.)
- **Overlap with the existing street millage:** the 2024 2.0-mill street renewal already covers "traffic safety infrastructure" including bike lanes. The 2021 Mobility Plan was designed without removing on-street parking. Both are relevant to the "pedestrian safety" and "bike lanes" claims. (Dossier §7, §11.)
- **Operating cost per household:** "If the City's share is $35,000–$165,000 a year, that equals about $3–$15 per $100,000 of taxable value per year from the general fund (inferred), on top of the bond." Computed on 2027 taxable value of $1.119B.
- **Who funds the campaigns:** WalkSafeEGR is a registered committee (PO Box, Lansing). Safe Streets EGR says it is one resident with no committee. Kent County filings aren't online. (Dossier §13.)
- **Wider community input:** besides the packet's cards, 11 of 11 speakers on Aug 3 opposed (East Insider), the school board logged 15 written opposition letters on Aug 18, and Bagel Kitchen's owners spoke in support (WOOD TV). Either add these or say plainly that the section covers only the Aug 3 packet's correspondence.

---

## LOW

### L-1. City seal next to "Independent voter guide"
The seal still appears in the hero (commit `c9b63c0`: "seal kept"). It can imply official status. Recorded only, since the organizer chose to keep it. A disclaimer under it would help: "Seal shown for identification; this guide is not produced or endorsed by the City."

### L-2. "The honest case on each side"
"Honest" implies other framings are dishonest. Replace with "The strongest case on each side." Rework two NO bullets for accuracy and symmetry:
- "The City's engineer said to try cheaper options first." → "The City's traffic consultant (Progressive Companies) first recommended trying on-street parking and the middle-school lot; its February letter said some options may not be feasible, without naming them."
- "The 240-space plan is larger than the documented permanent loss." This uses the same 240-vs-71 comparison the page rates *Misleading* in "$250K per space." Change it to: "The deck adds about 191 net spaces against a 71-space permanent loss; the extra capacity is meant for public use, which isn't yet guaranteed."
- The same "City's own engineer" wording appears in the Claude, Muse and Grok sections. "Consultant" is accurate.

### L-3. Reserves paragraph
- **Current text:** "That balance could not cover a $7.6M–$9.1M City share outright. Using any of it toward the project would substantially reduce the cushion and would not solve ongoing operating costs."
- **Suggested replacement:** "That balance is less than the City's estimated $7.6M–$9.1M share. Using part of it could reduce borrowing but would lower the balance toward the City's 20%–25% target, and it would not fund annual operations." Also, "44.01%" needs its base: "of general-fund expenditures and transfers."

### L-4. "Local tax context" compares only city levies
Add one line noting that residents also pay school, county and other levies (for example, the EGRPS debt levy is 9.95 mills per the district's June 2026 budget hearing). That way the 14.09 figure isn't read as the household's total.

### L-5. Fact-check claim labels and coverage
- "Signal cost about $500K | True" isn't the campaign's claim. WalkSafeEGR said "$350K–$600K." Restore the actual claim and rate it "Partly supported — the City's placeholder is about $500K; the $350K and $600K endpoints aren't sourced."
- **Add omitted claims for balance:**
  - Safe Streets: "school lots ran 80–87% full during school hours." Rate it Misleading: the 86.8% was a Saturday, and the weekday maximum was 81%.
  - Safe Streets: "operating cost $130K–$160K." True but excludes a repair reserve.
  - Safe Streets: "2-story alternative ~136 spaces." Partly: that's the memo's 2–4 level range floor; the April memo implies about 118.
  - WalkSafeEGR: "Gaslight deck decline as precedent." Context: it was a private deck, removed in Jan 2025, and the City says it was never more than 50% used.
- The "crime statistic" verdict should cite where the claim and the 1996 NIJ paper appear (WalkSafeEGR [10]). It currently has no citation.

### L-6. "Gaslight history" closing sentence tells readers how to judge
"The current decision should be judged on the current agreements and data" is advice, not a fact. Cut it, or write: "Supporters note the old deck was private and the new one would be publicly owned."

### L-7. Jargon never defined
OAK (Owen-Ames-Kimball, the construction manager), MFCI (the City's financial advisor), TIC (true interest cost), LTGO, LOS, O&M, ACFR, PUD, sinking fund, "Option 1 / Option 5" (brick vs. exposed-concrete façades), and taxable vs. market value. Add a short glossary or define each term at first use.

### L-8. "Three levels" vs. the design's four floors
The July 22 design lists spaces on L0 51, L1 70, L2 67, L3 52, which is four parking floors. If "three-level" means three levels above a ground deck, say "ground level plus two/three decks." Otherwise verify against the presentation. Minor, but residents near Bagley will care about height.

### L-9. Dates and the Grok "Net read" quote
- Claude's assessment file is dated Oct 9, 2026, but the page says "Oct 8." Align them.
- Grok's "Net read" quote begins mid-sentence ("But the case that this deck…") and repeats the summary above it. Trim it to the flip conditions or drop it.

### L-10. Source descriptions that don't match their links
- [4]: the Schwartz quote is from the July 20 minutes reproduced in the Aug 3 packet, pp. 248–251.
- [17]: should be Walker's Saugatuck summary, not the June 29 packet.
- [21]: links the district project page, not the April 20 minutes.
- [22]: the parking map is page 5 of the traffic-memo PDF [5], not the operating-cost file.
- [12]: Citizen Portal is an AI-generated meeting summary; label it so.
- [3], [11], [12], [14], [15] are listed but never cited in the text. Cite them or drop them.

---

## What I verified (math)
| Figure on page | Recomputed | OK? |
|---|---|---|
| $13.21M = $9M + $4.21M | 9,000,000 + 4,212,287 = 13,212,287 | ✓ |
| 0.5922 yr-1 / 0.4925 avg mills | CSV yr-1 0.5922; mean of 20 = 0.49247 | ✓ |
| $49 / $59 / $985 per $100K | 49.25 / 59.22 / 984.94 | ✓ (flat-TV basis; see H-4) |
| $98–$128 avg, $118–$154 yr-1, $1,970–$2,560 | 98.49–128.04 / 118.44–153.97 / 1,969.88–2,560.84 | ✓ (assumption-labeled issue) |
| 939/1,310 = 71.7%; 371 open | 71.68%; 371 | ✓ |
| School 81.0% wkday / 86.8% Sat | 294/363 = 80.99% (Wed 8 am); 315/363 = 86.78% (Sat 1 pm) | ✓ |
| Public-city ≤ 65.70% | max 477/726 = 65.70% | ✓ |
| 216 − 71 = 145; 145 − 49 + 240 = 336; ~191 net | ✓ | ✓ |
| $63.5K–$75.5K per stall; $80K–$95K per net | 15.25/240, 18.11/240; ÷191 | ✓ |
| $42K × 240 = $10.1M; premium $5M–$8M | 10.08M; 5.2–8.0M | ✓ (source label wrong) |
| $611 × 213 = $130,143; × 240 = $146,640 | ✓ | ✓ (framing wrong, H-1) |
| ($175 + $60) × 240 = $56,400 (2018 $) → $70K–$75K | ✓ with CPI +25–33% assumption | ✓ (assumption) |
| 1% reserve upper case $300K–$330K | 146.6K + 152–181K = 299–328K | ✓ |
| City half $35K–$165K | half of 70–330K | ✓ (but see H-1) |
| 3.5% escalation; > $500K per year of delay | 16.906 → 17.497 = 3.50%; 0.035 × 15.25M = $534K | ✓ |
| City portion "$8M–$9M" | 15.25–18.11 − 7 = $8.25M–$11.1M | ✗ (H-2) |
| "118 spaces beyond school need" | 240 − 118 = 122 | ✗ (M-4) |
| Grok "combined capacity 292" via MS lot | 363 − 71 = 292 (study school category) | ✗ wording (M-12) |
| $6,511,815 < $7.6M–$9.1M | ✓ | ✓ |
| Votes 5–2, 2–4, 4–1–1, 4–1–2; school 5–1 | match dossier/minutes summaries | ✓ |

## Not checked
- Original city packets (Aug 3, Apr 20, June 29, July 20 PDFs) and the July 22 deck were not opened directly. Figures from them were checked against the local transcriptions, findings and dossier, which cite page numbers.
- The Sept 30 superintendent letter: no public copy, so it wasn't checked here.
- The exact Aug 3 wording of the City's $160K figure (H-1). Confirm it from the meeting video or the City.
- The ballot question's exact text (H-5) wasn't available locally.
- Whether any document unpublished as of Oct 8 (agreement, itemized estimate) has since been released.
- Per the organizer's scope change: rendering, screenshots, accessibility, meta/SEO and external link status.
