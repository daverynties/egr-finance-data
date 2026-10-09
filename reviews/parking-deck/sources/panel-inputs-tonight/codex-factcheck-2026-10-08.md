| Audit result | Count |
|---|---:|
| Total claim and citation units checked | **207** |
| Supported | **174** |
| Contradicted | **8** |
| Unsupported-by-docs | **25** |
| Stale | **0** |

# Parking-deck ballot page fact-check

**Scope:** `page.html` and `page.txt`, supplied as the live-page capture fetched October 8, 2026. This report uses only files in this folder. No external pages were fetched. Repeated claims are consolidated; closely related comparison figures are grouped. Source-list descriptions are checked separately.

**Main findings:** The utilization figures, rounded debt total, millage figures and conditional home-tax arithmetic check out. Most HANDOFF changes appear on the page. Remaining problems include an incorrect resident-address attribution, incorrect resolution timing, mixed baselines in the third-level calculation, an unsupported 85% benchmark citation, an overstated signal-cost verdict, and a private link supporting important construction-period claims.

**Evidence limitation:** Much of the page is corroborated only by the supplied secondary/AI summaries. The local August 3 PDF contains **only packet pages 239–247**, not the complete packet. The original ballot, OAK estimate, complete MFCI analysis, commission minutes, school-board minutes, September 30 letter, ACFR, apportionment report and Census table are not local primary documents. A working external link does not verify its contents.

Status notation:

- **S — Supported:** substantiated directly by a supplied primary document, CSV, page inspection or reproducible arithmetic.
- **S† — Supported, secondary only:** corroborated by a supplied secondary/AI document; the underlying primary record is unavailable locally. These count as Supported but carry substantially less confidence.
- **C — Contradicted:** conflicts with available evidence, arithmetic or the page’s own stated basis.
- **U — Unsupported-by-docs:** evidence is insufficient for the stated claim or inference.
- **Stale:** demonstrably superseded information. No claim could conclusively receive this status from the supplied records. Several current-status assertions nevertheless lack current primary verification.

File abbreviations used below:

| Key | Local file |
|---|---|
| **P** | `docs/parking-deck-aug3-packet-findings.md` |
| **D** | `docs/parking-deck-research-dossier.md` |
| **DU** | `docs/parking-deck-research-dossier-update-oct9.md` |
| **F** | `docs/parking-deck-full-context.md` |
| **DD** | `docs/parking-deck-due-diligence.md` |
| **TR** | `docs/parking-deck-scanned-pages-transcribed.md` |
| **B** | `docs/parking-deck-bond-9M-debt-schedule.csv` |
| **V** | `docs/parking-deck-utilization-2025.csv` |
| **OP** | `docs/parking-deck-operating-cost-2026.pdf`, four pages |
| **TM** | `docs/parking-deck-traffic-memo-2025-11-10.pdf`, six pages |
| **CC** | `docs/parking-deck-aug3-p239-247.pdf`, nine pages |
| **LC** | `link-check.txt` |

PDF citations correspond to the supplied page images. For example, **TM p.3** is `docs/page-images/parking-deck-traffic-memo-2025-11-10-3.png`.

## Claims table

### Proposal, need and utilization

| ID | `page.txt` line(s) | Claim or number checked | Status | Evidence and qualification |
|---:|---|---|:---:|---|
| 001 | 17, 25 | Election: November 3, 2026 | S† | F:7; D:304. Original ballot unavailable locally. |
| 002 | 25 | Official name: “Public Parking Facility and Pedestrian Safety Bond Proposal” | S† | F:6; DD:1,10. No local ballot facsimile verifies exact wording. |
| 003 | 25, 29, 49 | Authority to issue up to $9 million in City bonds | S† | D:35,147,152; F:8,167. B supports the modeled principal, not legal authorization. |
| 004 | 31 | “20 years maximum term” | S† | D:152 and F:8 specify **20 years per series**. The page omits that qualification. |
| 005 | 33, 49 | Proposed deck: 240 spaces | S† | P:21,81; D:75. A design target, not a guaranteed final capacity; P:21 allows reductions and winter snow storage. |
| 006 | 35, 49 | Proposed deck: three levels | S† | F:14; D:89–90. D:75 also lists parking areas L0–L3; original drawings would clarify the terminology. |
| 007 | 35, 43, 49 | Site: Bagley Avenue at EGR High School | S | TM p.3 places the structure at Lot 11 north of the high school; TM p.5 identifies Lot 11. Current design corroborated by F:14. |
| 008 | 37, 49, 331 | School set-aside: about $7 million | S† | D:50–51: April 20 board motion, general and capital improvement funds, non-bond resources. |
| 009 | 117, 119 | Proposed City/school split: half each | S† | D:386–390; F:18,219. Proposed allocation; no executed agreement supplied. |
| 010 | 27, 347 | Built by an East Grand Rapids resident | U | No independent authorship/residency evidence in the supplied documents. |
| 011 | 27, 347 | Self-funded | U | No funding records supplied. |
| 012 | 21, 27, 347 | Independent; unaffiliated with City, district or campaigns | U | Publisher declaration; affiliations are not independently established by these files. |
| 013 | 45, 101–107 | Estimate range approximately $15.2M–$18.1M | S† | P:40–42: $15,246,696 through $18,109,782 across options and dollar years. |
| 014 | 45–49 | That range describes the complete deck-plus-signals-plus-pedestrian project | U | P:36–45 describes OAK deck estimates. D:80,389 identifies signal/loading/snow-melt extras with unresolved allocation. Complete combined scope is not established. |
| 015 | 67, 69 | Counts do not establish a system-wide shortage on measured dates | S | V:all-category rows; maximum 939/1,310. Does **not** establish available capacity everywhere or current October 2026 conditions. |
| 016 | 55, 69, 216 | System peak: 939 occupied spaces | S | V:25, March 12, 2025, 13:00. |
| 017 | 55, 69, 216 | Study inventory: 1,310 spaces | S | V:5,25 and other all-category rows. |
| 018 | 55, 69, 75, 217 | System peak: 71.7%, rounded to 72% in campaign table | S | 939 ÷ 1,310 × 100 = 71.6794%; V:25. |
| 019 | 51, 55, 69, 216 | 371 spaces empty at system peak | S | 1,310 − 939 = 371; V:25. |
| 020 | 55, 69, 75 | Weekday school-category peak: 81% / 81.0% | S | V:2: 294/363 = 80.9917%. May 8 weekday peak is lower. |
| 021 | 55, 69, 75, 217 | Saturday school-category peak: 86.8% | S | V:98: 315/363 = 86.7769%, May 10 at 13:00. |
| 022 | 69, 73, 77 | 85% is a “commonly used” benchmark, supported by source [16] | U | OP p.3, Fig. 5-1, contains cost assumptions, not an occupancy benchmark. Secondary files call 85% a benchmark but supply no local original establishing it. |
| 023 | 69, 217 | System-wide weekday utilization did not reach 85%; school lots exceeded it Saturday | S | V:25,98,102. Supported as numerical comparisons with an assumed threshold. |
| 024 | 73–77; HTML 399–408 | Chart starts at zero; 0%, 25%, 50%, 75%, 100% scale; three plotted values | S | `page.html`:402–406. Bar dimensions approximately represent 71.7%, 81.0%, 86.8%; zero baseline at y=205. |
| 025 | 81 | Senior lot contained 111 spaces | S | TM p.2; TM p.5 Lot 15; TR:21,38. |
| 026 | 81 | Expansion plan retains 40 senior-lot spaces | S | TM p.2; TR:21. |
| 027 | 81 | Loss is 71 spaces | S | TM p.2; 111 − 40 = 71. |
| 028 | 81 | Loss arises from the separately approved school expansion | S† | TM p.2 establishes expansion-related loss; separate approval is supported only by F:24,238. |
| 029 | 83 | Campus before construction: 216 spaces | S† | D:103; F:241; original April memo absent. |
| 030 | 85, 322 | Construction-period campus supply: approximately 65 spaces | S† | D:105; DU:18–20 concerns correspondence, while D:105 specifically attributes this count to September 30 letter. Letter absent and page’s link private. |
| 031 | 43, 65, 85, 261 | Low-supply construction phase: 2028–2030 | S† | D:105–110; original letter absent. |
| 032 | 87 | Campus afterward without deck: 144 spaces | S† | D:106; P:125; original campus plan absent. |
| 033 | 61, 89, 334 | Existing Bagley/Lot 11 surface lot: 49 spaces | S | TM p.5 legend: “School – High School – 49 Spots”; TR:37. D:309 reports a separate study count of 50. |
| 034 | 61 | Net gain over post-construction no-deck campus: 191 spaces | S | 240 − 49 = 191, conditional on the proposed design and retained campus count. |
| 035 | 57, 109–111, 218 | Approximately 190 net new spaces | S | Rounded 191; compare ID 034. |
| 036 | 89 | Campus afterward with deck: approximately 335 | S | 144 − 49 + 240 = 335. Inputs 144/240 rely on secondary sources; 49 confirmed by map. |
| 037 | 43, 65 | “The strongest need case” is the construction-period shortage | U | Editorial ranking, not a documented finding. Existing records also describe permanent replacement and shared community uses; P:64–69. |
| 038 | 93–95 | Engineer recommended building expansion without new parking | S | TM p.3 Recommendations; TR:31. Displayed callout is a paraphrase, not the memo’s exact wording. |
| 039 | 95 | Memo found on-street capacity within 1,500 feet | S | TM p.3 Recommendations; TR:31. |
| 040 | 95 | Structure should be considered after other options | S | TM p.4; TR:33. |
| 041 | 95 | Predicted structure load-out: 30–60 minutes | S | TM p.3; TR:28. Prediction concerns the design options evaluated then. |
| 042 | 95 | Exit delays could lead students/staff back to street parking | S | TM p.3; TR:28. Conditional prediction, not observed behavior. |
| 043 | 97, 197, 201 | February 4, 2026 follow-up said some recommendations may be infeasible because of campus limitations | S | TM p.1; TR:16. Quoted passage agrees with image. |
| 044 | 97, 283 | Follow-up is by the same engineer, Joseph P. Eberle, PE | S | TM pp.1,4 signatures. |
| 045 | 97 | Follow-up does not identify which options are infeasible | S | TM p.1; TR:18. It also does not explicitly endorse this deck. |

### Construction, operations and third-level calculation

| ID | `page.txt` line(s) | Claim or number checked | Status | Evidence and qualification |
|---:|---|---|:---:|---|
| 046 | 101 | Utilitarian estimate rounds to $15.25 million | S† | P:40: $15,246,696. |
| 047 | 101 | Utilitarian figure is OAK Option 5 in 2026 dollars | S† | P:36–44; F:145–147. |
| 048 | 105 | Brick estimate rounds to $16.91 million | S† | P:40: $16,905,675. |
| 049 | 105 | Brick figure is OAK Option 1 in 2026 dollars | S† | P:36–44. |
| 050 | 107 | Highest displayed 2028 estimate: $18.11 million | S† | P:42: $18,109,782. |
| 051 | 103, 113 | Packet gives totals, without a released line-item estimate | S† | P:45. Full packet not local, so cannot independently establish its contents or universal publication absence. |
| 052 | 109–111 | $80K–$95K per net new space | S | $15,246,696/191 = $79,826; $18,109,782/191 = $94,816. Estimates themselves secondary. |
| 053 | 113 | Walker benchmark: roughly $42,000 all-in per structured space | S† | D:209,395; DD:90. Original Walker report absent. |
| 054 | 113, 319 | That benchmark is “cited in the record,” specifically the June 29 packet | U | D:209,325 identifies a **Saugatuck report**. No local evidence places it in June 29 packet. |
| 055 | 113 | Benchmark baseline for 240 spaces: approximately $10.1 million | S | 240 × $42,000 = $10,080,000; conditional benchmark comparison. |
| 056 | 113 | Difference from project estimate: approximately $5M–$8M | S | $15,246,696−$10,080,000=$5,166,696; upper difference $8,029,782. Not an itemized premium. |
| 057 | 113 | Design includes architectural treatment, heated walks and an elevator | S† | F:138–141; D:77–80. P:75 describes elevator as optional in an earlier presentation. |
| 058 | 113 | These features explain the calculated benchmark premium | U | Without comparable scope and line items, the arithmetic difference cannot be causally allocated to those features. |
| 059 | 117, 286 | April 23 email by deputy city manager Doug La Fave | S | OP p.1 email and signature; TR:54–57. |
| 060 | 117 | Grand Rapids O&M benchmark: $611 per space per year | S | OP p.1. |
| 061 | 117 | Email explicitly excludes depreciation | S | OP p.1: “not depreciation.” This does not establish every component included in O&M. |
| 062 | 117, 153 | Email’s total corresponds to 213 spaces; April concept smaller than 240 | S | $130,143/$611 = 213; OP p.1. April design chronology also D:119. |
| 063 | 117 | April total: $130,143 annually | S | OP p.1. |
| 064 | 117 | Applied to 240 spaces: approximately $147,000 annually | S | $611 × 240 = $146,640. |
| 065 | 117 | Manual basic above-grade operating cost: $175/space/year | S | OP p.3, Operating costs; TR:72. |
| 066 | 117 | Manual capital-maintenance sinking fund: $60/space/year | S | OP p.3; TR:73. |
| 067 | 117, 316 | Manual figures are in 2018 dollars | S | OP p.3 note. |
| 068 | 117 | Applying manual annual figures to 240 spaces | S | ($175+$60) × 240 = $56,400/year in 2018 dollars. |
| 069 | 117 | Inflation-adjusted amount is $70K–$75K “today” | U | TR:78 assumes +25–33% CPI; no CPI series, date endpoints or calculation evidence supplied. |
| 070 | 117 | Use 1% of construction cost annually as repair reserve | S† | D:318 attributes this to Walker. OP p.3 instead supplies a $60/space sinking fund; it does not supply a 1% rule. |
| 071 | 117 | O&M plus 1% reserve produces approximately $300K–$330K | S | $146,640 + $152,466.96–$181,097.82 = $299,106.96–$327,737.82. Conditional scenario. |
| 072 | 117 | “The realistic full annual cost” is $70K–$330K | U | Combining two different benchmarks and an unverified CPI adjustment does not establish a project-specific full-cost range. Debt/capital recovery is excluded. |
| 073 | 117 | City’s half of that scenario: $35K–$165K/year | S | Half of the stated scenario bounds. Allocation and underlying bounds remain assumptions. |
| 074 | 117 | No dedicated funding source identified | S† | D:198,185; DD:107. Supports a reviewed-record gap, not proof no source exists in October. D:387–388 mentions proposed dedicated accounts/reserves. |
| 075 | 121, 123 | City stated annual estimate: $160,000 | S† | D:193; F:20. OP p.1 directly states $130,143, not $160,000. |
| 076 | 123 | $160K is broadly consistent with an O&M benchmark for the whole structure | S† | D:198; $146,640 extrapolation supports approximate comparability. No primary breakdown traces the difference. |
| 077 | 123 | Reviewed records establish a broader “full-cost range” | U | They establish different benchmark scenarios, not a complete project-specific cost range; see IDs 069–072. |
| 078 | 119 | Schwartz, July 20: school needs two levels; third is a City possibility | S† | P:103 quotes this. Original July 20 minutes are not local. P locates minutes in **August 3 packet pp.248–251**, not July 20 agenda packet. |
| 079 | 119, 204 | April two-story option meets school’s “no net loss” goal | S† | P:124–125. Approximately 213 campus spaces compared with 216 before construction. |
| 080 | 119 | Half of estimate range: approximately $7.6M–$9.1M | S | $15,246,696/2=$7,623,348; $18,109,782/2=$9,054,891. Proposed equal split. |
| 081 | 119 | Half-cost “buys roughly 118 spaces beyond” school-only option | C | Displayed inputs imply school-only deck 118 stalls, and 240−118=**122 additional stalls**. Versus pre-construction campus: 335−216=119. Page mixes baselines; P:129 uses an older approximate calculation. |
| 082 | 119 | $64K–$77K for each space beyond school-only option | C | Division by 118 reproduces the page’s approximation, but correct 122-stall comparison gives **$62,486–$74,220**. Neither establishes actual marginal construction cost. |

### Financing and household impact

| ID | `page.txt` line(s) | Claim or number checked | Status | Evidence and qualification |
|---:|---|---|:---:|---|
| 083 | 127, 227 | Principal plus interest: approximately $13.21M / $13.2M | S | B:2–21 sums to **$13,212,287**. Secondary summaries say $13,212,282: a $5 discrepancy, immaterial at page precision. |
| 084 | 129, 227 | Modeled principal: $9 million | S | B:2–21 principal sum = $9,000,000. |
| 085 | 129, 227 | Modeled interest: approximately $4.21 million | S | B interest sum = $4,212,287. D:147/F:198 give $4,212,282. |
| 086 | 129 | Modeled true interest cost: 4.13% | S† | P:51; D:147. CSV does not include a TIC field or issuance assumptions sufficient to independently verify TIC. |
| 087 | 131 | First-year millage: 0.5922 | S | B:2. |
| 088 | 133 | Average modeled millage: 0.4925 | S | Arithmetic mean of B:2–21 = 0.49247, rounding to 0.4925. |
| 089 | 135 | Model assumes 2% annual City taxable-value growth | S | Successive taxable values in B:2–21 grow approximately 2%; D:153 supplies prior base. |
| 090 | 137 | Slower aggregate taxable-value growth requires higher millage for unchanged debt service | S | Millage = debt service ÷ aggregate taxable value × 1,000. |
| 091 | 139 | Median home market value approximately $521,000 | S† | D:154,329 reports Census $521,300. Census extract absent locally. |
| 092 | 139 | Median home has taxable value approximately $200K–$260K | U | D:154 offers a rough assumption dependent on purchase year, not an observed median taxable-value distribution. Market median does not establish taxable median. |
| 093 | 139 | Average annual tax: $98–$128 at stated taxable values | S | $200,000–$260,000 × 0.4925/1,000 = $98.50–$128.05. Conditional on constant taxable value. |
| 094 | 139 | First-year tax: $118–$154 | S | $200,000–$260,000 × 0.5922/1,000 = $118.44–$153.972. |
| 095 | 139 | Twenty-year tax: $1,970–$2,560 | S | B’s millage sum 9.8494 × taxable value/1,000 = $1,969.88–$2,560.844. Conditional on constant taxable value; omitted assumption matters. |
| 096 | 141, 325 | Unassigned general-fund balance: $6,511,815 | S† | D:163, as of June 30, 2025. Local ACFR absent. |
| 097 | 141, 325 | Balance equals 44.01% | S† | D:163 specifies **expenditures and transfers**, omitted in page’s body. |
| 098 | 141 | City reserve target: 20%–25% | S† | D:163. Original policy/ACFR absent. |
| 099 | 141 | Using some reserves could reduce borrowing | S | Financial arithmetic, conditional on availability and authorization. |
| 100 | 141 | Paying full City share from that balance would reduce the cushion | C | $6.512M is less than modeled $7.623M–$9.055M share; shortfall is $1.112M–$2.543M before retaining any cushion. Full payment from that balance is impossible on stated figures. |
| 101 | 141 | A one-time reserve payment does not solve ongoing operating costs | S | One-time capital payment does not itself establish recurring revenue. |
| 102 | 145 | EGR’s 2024 City levy: 14.09 mills | S† | D:166: exact total 14.0909. Historical context, not a 2026 rate. |
| 103 | 145 | Components: operating 11.35, extra-voted 1.73, debt 1.01 | S† | D:166: 11.3508 + 1.7307 + 1.0094 = 14.0909. |
| 104 | 145 | Cedar Springs 18.77; Lowell 15.95 | S† | D:169–173. |
| 105 | 145 | EGR rate is high among listed nearby cities but below those two | S† | D:169–181 comparison supports limited claim. Page appropriately disclaims service equivalence and total tax burden. |

### Governance and resident correspondence

| ID | `page.txt` line(s) | Claim or number checked | Status | Evidence and qualification |
|---:|---|---|:---:|---|
| 106 | 149–153 | April 20, 2026 design-funding approval: 5–2 | S† | D:31. D:40 says original minutes are in **May 4 packet**, not April 20 agenda packet. |
| 107 | 153 | April memo rejected underground parking for “safety concerns” | S† | D:93; F:214. D identifies April 14 memo included in April 20 materials. |
| 108 | 147 | Design funding to ballot language in under four months | S | April 20 to August 3 = 105 days; to August 6 = 108 days. Underlying event dates secondary. |
| 109 | 155–159 | July 20 Commission reviewed LTGO financing and chose voter-approved route | S† | F:244,252; D:157. Original minutes absent. |
| 110 | 159 | LTGO bonds “would not require a vote” without qualification | U | D:157 and F:252 describe petition rights that could force a vote. Statement needs this condition. |
| 111 | 161–165 | August 3 postponement failed 2–4 | S† | D:34,358; DD:167. D:358 explicitly corrects an East Insider “4–3” account using minutes. |
| 112 | 165 | Hunter left at 8:23 p.m. | S† | D:34,359; DD:173. |
| 113 | 165 | August 3 ballot placement passed 4–1–1 | S† | D:35; DD:168. |
| 114 | 165 | Wessely no; Groff-Blaszak abstained | S† | D:35. |
| 115 | 167–171 | August 6 special meeting corrected millage typo | S† | D:36; F:169–172. Original August 6 record absent. |
| 116 | 169–171 | Correction vote 4–1–2, separate from August 3 vote | S† | D:36–38; DD:169–171. |
| 117 | 175 | Seven unique handwritten comment cards | S | CC pp.2–6: 1 Acheson, 1 Nielsen, 3 on p.4, 2 on p.6. CC p.5 duplicates p.4; image files have identical SHA-256 hashes. |
| 118 | 175 | All seven are explicitly May 27 cards | U | Acheson, Boles, Dujovny and Dietsch display May 27 dates. Nielsen, Stevens and unsigned card have no visible date. Session attribution is plausible but not individually documented. |
| 119 | 175 | Four cards opposed or raised concerns | S | CC pp.2,3,4 bottom,6 top; inferred content classification. |
| 120 | 175 | Those four are from Bagley Avenue residents | C | Only three have Bagley addresses: Acheson, Nielsen, Dujovny. Fourth card is unsigned with blank address. TR:150,156; CC p.4 bottom. |
| 121 | 175 | One supportive card from Greenwood Avenue | S | CC p.6 bottom, Dietsch; TR:137–138. |
| 122 | 175 | Two cards offer ideas without an express position | S | CC p.4 top/middle: paid parking/access control and alternatives to driving. Inferred classification; TR:121–125. |
| 123 | 175 | Three typed emails in packet section | S | CC pp.7–9; TR:140–143. |
| 124 | 175 | One unsigned opposition form letter | S | CC p.7 ends “[Your name] [Your address]”; `docs/parking-deck-aug3-p239-247.txt`:43–51. Sender is named in header; body/signature unfilled. |
| 125 | 175 | Mayor described an “email campaign” | S | CC p.7 / packet p.245; text-layer file:17–19. Actual wording is tentative: “apparently there must be an email campaign going around.” |
| 126 | 175 | Two other emails ask for a public vote | S | CC p.8 Jacoby, July 23; p.9 Trost, July 28. They do not explicitly endorse or oppose the deck. |
| 127 | 175 | City manager summarized feedback as mostly opposition, especially nearby residents | S† | P:24; F:155. Manager memo outside local packet excerpt. |
| 128 | 175 | Resident names and street numbers omitted from page summary | S | Direct inspection of `page.txt`:175. |
| 129 | 179 | Subcommittee met below quorum; no minutes exist | S† | D:62,417; DD:177 attributes account to East Insider. No local minutes policy or comprehensive records search substantiates universal absence. |
| 130 | 179 | Public record does not show how key choices were made | U | Overbroad: P:21,102–103,124 and D:87–95 describe design evolution and reasons. Lack of subcommittee minutes does not establish absence of all decision evidence. |
| 131 | 183 | Revised resolution was 33 pages | S† | P:34; D:64,357. |
| 132 | 183 | It arrived about 90 minutes before the August 3 **vote** | C | P:34, D:64 and DD:178 say before the **meeting**. D:357 says emailed 4:23 p.m.; Hunter’s 8:23 departure followed postponement. |
| 133 | 183 | Revised document was not public beforehand | S† | D:357; DD:178. Reported secondary account, not verified distribution history. |
| 134 | 187 | Pedestrian-safety wording added in August | S† | F:30; DD:179. Local adopted resolution absent. |
| 135 | 187, 259 | No released pedestrian project list or dedicated budget/performance target | S† | D:435; DD:179,264. Supports absence in reviewed material, not an exhaustive current publication claim. |
| 136 | 191, 253 | No executed City/school agreement identified | S† | D:65,419; DD:180. Main cited news evidence dates August 4; no October executed-agreement search supplied. |
| 137 | 191 | Therefore cost share, ownership, access and third-level role all remain nonbinding | U | Absence of one agreement does not establish the legal status of every board action, resolution or commitment. No local legal analysis. |
| 138 | 195 | Prior private Gaslight structure was lost | S† | D:256–258,371; DD:191. |
| 139 | 195 | Earlier development agreements contained parking obligations | S† | D:256–257 describes retain/maintain and school-event conditions. Original PUD absent. |
| 140 | 195 | This history contributes to public skepticism | S† | D:275,279 and F:70 document its use in opposition arguments. A characterization, not a quantified sentiment finding. |

### Alternatives, campaign verdicts and risks

| ID | `page.txt` line(s) | Claim or number checked | Status | Evidence and qualification |
|---:|---|---|:---:|---|
| 141 | 201 | On-street availability: 89–111 spaces | S | TM p.2: **minimum 89, average 111**, not a minimum-to-maximum range. Table needs accurate labels. |
| 142 | 201 | On-street option costs “About $0” | U | TM gives no cost estimate. Existing supply might avoid construction, but administration, safety and management costs are not established as zero. |
| 143 | 202 | Engineer proposed bussing/demand-management pilot | S | TM p.3 Bussing Pilot and Recommendations; TR:29,31. |
| 144 | 202 | Pilot was not pursued | S† | DD:200. TM proposes it but does not establish subsequent implementation status. |
| 145 | 203 | Middle-school expansion could add up to 103 spaces | S | TM p.3; TR:25. |
| 146 | 203 | Engineer described middle-school expansion as less expensive | S | TM pp.3–4; TR:32. No dollar estimate. |
| 147 | 203 | Middle-school option deferred | S† | DD:201. TM gives a conditional sequence, not a formal City deferral action. |
| 148 | 204 | Two-story option approximately 118–136 spaces; 213 campus total; memo’s 2–4-level range starts at 136 | S | TM p.3 confirms 136–291 across 2–4 levels. Derived 118 = 213−(144−49), using secondary April counts. These are different concepts, not one measured design range. |
| 149 | 206 | Shared parking is undeveloped, “Concept only” | U | Cards suggest partnering with other lots, CC p.2. No implementation/status record supplied establishing this categorical claim. |
| 150 | 205 | Underground reasons varied: safety, infeasibility, limited land | S† | D:93,423; DD:205. Original April memos absent. |
| 151 | 205 | No underground analysis published | S† | D:423. Review gap; publication absence not independently verified. |
| 152 | 208, 251 | No student survey conducted | S† | D:293–295,427; DD:209 attributes this to Groff-Blaszak/East Insider. No survey inventory supplied. |
| 153 | 208, 251 | No survey tests likely deck use, queues, location or later pricing | S† | Follows from reported lack of any student survey; D:427. Specific later-pricing scenario is hypothetical. |
| 154 | 208 | Therefore behavior/demand assumptions are largely untested | U | No survey does not establish absence of traffic modeling or other behavioral evidence. Needs attribution/qualification. |
| 155 | 212, 216–221 | WalkSafeEGR is the No campaign and made these listed claims | S† | D:277–279; DD:219–225. Local campaign snapshot absent. |
| 156 | 218 | “$250K per space” uses 71–72-space loss rather than net added spaces, and is misleading | S† | D:275; DD:225. $18.11M/72≈$251.5K. Exact campaign numerator/context not locally preserved. |
| 157 | 219 | Crime statistic comes from 1996 research and a broad parking category | S† | D:279; DD:223. Original NIJ paper absent. |
| 158 | 219 | That research does not quantify expected incidents for this design | U | Plausible, but original study and its scope are unavailable locally. |
| 159 | 220 | Neither supplied traffic letter contains LOS analysis or LOS F | S | TM pp.1–4 reviewed as images; TR:34. |
| 160 | 220, 233 | “LOS F” is **False**, meaning contradicted by the record | C | The documents contain no LOS result. Absence establishes unsupported attribution, not that the intersection cannot be LOS F. The page’s own legend says False means contradicted. |
| 161 | 221 | WalkSafeEGR claims signal cost $350K–$600K | S† | D:244,279; DD:222. |
| 162 | 221 | City placeholder approximately $500K; April memo “up to $500,000” | S† | D:244. Original cost memo absent. |
| 163 | 221 | Entire $350K–$600K range is therefore “True” | U | One estimate inside a range does not validate both endpoints. No supplied $350K or $600K primary estimate. |
| 164 | 223, 227–231 | Safe Streets EGR is the Yes campaign and made listed claims | S† | D:272–275; DD:227–239. Local campaign snapshot absent. |
| 165 | 228 | $49/year per $100K taxable value matches modeled average | S | $100,000×0.4925/1,000=$49.25. First year $59.22; fixed-value qualification applies. |
| 166 | 229 | Students using structure need not cross streets | S | TM p.3; TR:27. Design-specific geometric statement, not a guarantee they use the deck. |
| 167 | 229 | Same memo warns of approximately 1,000-foot walk around school | S | TM p.3; TR:27. Quotation agrees with image. |
| 168 | 230 | Resolution intends street-parking reallocation for dedicated mobility lanes | S† | F:175–180. Original resolution absent. |
| 169 | 230, 255 | No binding street-by-street removal plan identified | S† | DD:238,247; D:435. Reviewed-record limitation. |
| 170 | 231 | June 23 presentation: “free public parking in designated spaces” during school days | S† | P:54–59. Presentation pages are not supplied locally. |
| 171 | 231 | Same presentation: “free parking for all” after school | S† | P:60–61. |
| 172 | 231 | September 30 letter’s “no fee” promise is limited to school-event attendees | S† | P:62; D:82. Original letter absent; linked copy returns 401. This limited promise does not prove other use will be charged. |
| 173 | 231, 257 | No binding general-public free-use guarantee found | S† | D:419; DD:248. Qualified finding, not proof of future charges. |
| 174 | 239 | Estimate escalation approximately 3.5% per year | S | P:40–42 totals yield approximately 3.5%; P:46 explicitly derives it. |
| 175 | 239 | One year of modeled delay adds more than $500,000 on $15M-plus project | S | $15,246,696×3.5%=$533,634.36. Estimate assumption, not certainty about bids. |
| 176 | 243 | TIC estimates rose from 3.33% to 4.13% | S† | D:144–150; P:51. Page correctly does not repeat old secondary claim that rates alone added $2M. |
| 177 | 243 | Final debt service depends on rates when issued | S† | F:203 notes estimates subject to change. Also depends on actual amount, timing and issuance structure. |
| 178 | 247 | Signal, loading dock, snow melt and façade choices lack full released itemization | S† | D:80,389,421; P:45. Full original estimates absent. |
| 179 | 261 | No committed deck-delivery date aligned with 2028–2030 phase | S† | D:110; DD:261. Absence in reviewed documents, not a verified October construction status. |
| 180 | 263 | No Lake/Bagley location-specific crash analysis identified | S† | D:250,378–381; DD:264. Does not establish absence of crashes or absence of data held elsewhere. |

### Source descriptions and method claims

These rows check what the page says each citation contains. They do not treat a 200 response as proof that its contents support the attached claim.

| ID | `page.txt` line(s) | Citation/description checked | Status | Evidence and qualification |
|---:|---|---|:---:|---|
| 181 | 270–271 | [1] August 3 packet contains staff memo, resolutions, OAK estimates, finance and correspondence | S† | P:9–15. Local CC contains correspondence only. It cannot verify same-day or August 6 vote outcomes. |
| 182 | 273–274 | [2] April 20 packet contains original recommendation, campus counts and design-funding material | S† | F:209–234; D:103. Actual April 20 vote outcome requires later minutes, D:40. |
| 183 | 276–277 | [3] June 29 packet contains utilization study/work-session material | S† | F:125–128; D:213–238. CSV available locally. |
| 184 | 279–280 | [4] July 20 agenda packet supplies July 20 meeting record/Schwartz quote | U | P:100–103 locates July 20 minutes in August 3 packet pp.248–251. No local support for same-day agenda packet containing those minutes. |
| 185 | 282–283 | [5] PDF contains November 10 memo and February 4 Eberle follow-up to La Fave | S | TM pp.1–4. Correct description. |
| 186 | 285–286 | [6] PDF contains April 23 and February 4 La Fave emails, Grand Rapids benchmark and depreciation exclusion | S | OP pp.1–2. Correct description. |
| 187 | 288–289 | [7] August 3 materials contain MFCI $9M/rate/tax-value model | S† | P:49–52; F:193–205. B independently corroborates debt and levy series. |
| 188 | 291–292 | [8] June 29 materials contain hourly school/public/private occupancy data | S† | D:6,213–238; V independently supplies counts. |
| 189 | 294–295 | [9] August 3 materials contain annual debt-service/levy schedule | S† | D:7,147,153; B is the local extracted schedule. |
| 190 | 297–298 | [10] WalkSafeEGR is source for opposition claims | S† | D:277–279. Original campaign content absent. |
| 191 | 300–301 | [11] Safe Streets EGR is source for support claims | S† | D:272–275. Original campaign content absent. |
| 192 | 303–304 | [12] Citizen Portal provides August 3 meeting summary | S† | D:354. It is an **AI summary**, not official minutes; source label should say so. |
| 193 | 306–307 | [13] East Insider supplies reporting/community context | S† | D:62–65,293–297. D identifies Commissioner Groff-Blaszak’s Substack; attribution matters. |
| 194 | 309–310 | [14] FOX 17 supplies proposal/resident-concern video coverage | S† | D:65,289–290; original video not examined locally. |
| 195 | 312–313 | [15] Group threads may require access and are not factual proof | S† | D:402; F:263–264. Page appropriately limits their evidentiary role. |
| 196 | 315–316 | [16] Fig. 5-1 contains an 85% utilization benchmark | C | OP p.3 contains **cost to own and operate parking**, not an occupancy benchmark. Operating/reserve portion of description is correct. |
| 197 | 318–319 | [17] June 29 packet is an appropriate source for Walker $42K benchmark | U | D:209,325 and DD:301 identify Walker’s Saugatuck summary. No local evidence establishes the cited packet as its source. |
| 198 | 321–322 | [18] September 30 letter supports construction supply and event-fee statements | S† | D:81–82,103–106. No local letter; LC:2 returns 401. D’s letter URL at line 67 has a different Drive file ID. |
| 199 | 324–325 | [19] FY2025 ACFR reports $6,511,815/44.01% | S† | D:163. Local ACFR absent; 200 link alone does not verify it. |
| 200 | 327–328 | [20] 2024 apportionment report supplies levy components | S† | D:166–181. Local report absent; supplied 403 is inconclusive about availability. |
| 201 | 330–331 | [21] April 20 board minutes support 5–1 and approximately $7M set-aside | S† | D:50–56. Page links a district **project page**, not the minutes themselves. |
| 202 | 333–334 | [22] September 12, 2025 map lists Lot 11 at 49 spaces | S | TM p.5, date and legend. Correct. |
| 203 | 336–337 | [23] QuickFacts supplies median owner-occupied value for 2020–2024 | S† | D:154–155 reports value and period. No local Census table. |
| 204 | 339–340 | [24] June 23 public presentation and access promises appear in August 3 packet | S† | P:54–62. Presentation not local. |
| 205 | 345 | Numbers are attributed to the closest available primary record; primary records lead | U | Several citations point to agenda packets instead of minutes, and source [16]/[17] does not support the attached claim. Local evidence cannot verify the stated methodology. |
| 206 | 345, 349 | Every “inferred” figure is arithmetic from cited figures | C | $70K–$75K requires an unstated CPI assumption; median taxable-value range is an assumption; “realistic full annual cost” is an assessment. These are more than arithmetic. |
| 207 | 349 | Last reviewed October 8, 2026 | U | Page displays that date, but no local edit/review history verifies it. October 9 dates on HANDOFF/secondary files do not justify automatically changing the captured page’s date. |

### Primary versus secondary disagreements

| Issue | Primary evidence | Secondary account | Resolution |
|---|---|---|---|
| Saturday occupancy | V:98 shows 86.78%; V:102 shows 85.40% | F:35,106,191 says no category exceeded 85% | Primary CSV controls. Live page has corrected this. |
| Resident correspondence | CC pp.7–9 contains three typed emails; pp.4–5 are duplicates | P:94,140 misidentifies pp.246–247 as handwritten and describes only one typed email | Images control. TR:90 and DU:21 correct the old summary. |
| Opposition addresses | Three addressed Bagley cards plus one unsigned card | HANDOFF:108 and TR:156 correctly distinguish three; page says four Bagley residents | Correct live-page attribution. |
| LOS F | TM pp.1–4 contains no LOS analysis | D:245,346 originally repeats campaign attribution; DD:221 calls it unverified | Primary supports “not in these documents,” not “False.” DU:13,26 corrects the attribution. |
| Operating-cost source | OP p.1 states $130,143 at $611/space, excludes depreciation; p.3 supplies $175+$60 annual figures | D:347 calls PDF a $160K breakdown; DD:105 claims exclusion of capital reserves | Those descriptions exceed primary evidence. Depreciation exclusion does not independently prove every reserve exclusion. |
| Operating-cost range | Primary offers benchmarks, not a tailored EGR full-cost estimate | D:319 says $340K–$370K; DD:102 says $300K–$330K; DU:24 says $70K–$330K | Treat as differing scenarios and assumptions, not successive verified project estimates. |
| Campus after deck | Map confirms 49 replaced spaces | Older D:16/P:129/DD:49 use approximately 334 | Using page’s inputs gives 335. Live page correctly uses 335, but third-level paragraph retains old baseline logic. |
| Debt total | B sums to $13,212,287 | D:147, F:199, DD:127 say $13,212,282 | Record $5 discrepancy; rounded live figures are correct. Original MFCI page needed to reconcile transcription. |
| Resolution timing | No local original distribution/meeting record | P:34, D:64, DD:178 say before meeting; live page says before vote | Correct “vote” to “meeting,” with attribution. |
| Underground rejection | Original April memos absent | F:25,45 says cost; F:214/D:93 later says safety/feasibility/land | Later summaries correct earlier ones, but this remains secondary-only locally. |
| Rate-cost increase | B supplies only adopted schedule | DD:135 attributes about $2M increase to rates; DU:23 says about $0.7M, balance from higher principal | Live page avoids the old erroneous $2M attribution. |

## HANDOFF checklist

The HANDOFF is treated as requested-change data, not instructions to edit, commit or contact anyone. “Applied” means present in the captured page; it does not mean independently validated.

| HANDOFF item | Result | Evidence from `page.txt` and assessment |
|---|---|---|
| **1. Add February 4 follow-up** | **Applied** | Lines 97,197,201 and source [5] at 282–283 include the letter and its limits. |
| **2. Operating-cost range and source [16]** | **Partially applied** | Line 117 reproduces proposed range and “inferred” labels. Source [16] renamed at 315, but line 316 still falsely assigns the 85% benchmark to Fig. 5-1; citation remains at 69. |
| **3. Correct footnotes and add sources** | **Partially applied** | Lines 83/87 cite [2]; 85 cites [18]; 89 cites [22]; 141 cites [19]; 145 cites [20]. $158.9M removed. New sources at 321–340. But [18] is private, originals are not local, and some source destinations remain imprecise. |
| **4. Two-story spaces ~118–136** | **Applied** | Line 204 contains range, 213-campus explanation and different memo’s 136 lower figure. Needs explicit distinction between concepts. |
| **5. “Operating levy” → “City levy”** | **Applied** | Line 145 uses “2024 city levy,” with three components. |
| **6. School-board set-aside** | **Applied** | Lines 49 and 331 give April 20, 5–1, about $7M, general/capital funds. Source links project page rather than direct minutes. |
| **7. Add LOS F and signal-cost rows** | **Applied** | Lines 220–221 contain both. Their verdicts still need correction. |
| **8. Add street-crossing walk-distance qualification** | **Applied** | Line 229 includes no-crossing quote, approximately 1,000-foot walk and original recommendation. |
| **9. Update free-parking explanation** | **Applied** | Line 231 distinguishes June presentation from September school-event promise. |
| **10. Underground reasons** | **Partially applied** | Alternative row at 205 gives all three reasons. Timeline at 153 retains only safety; acceptable historical shorthand, but requested treatment in both places is incomplete. |
| **11. Add third-level paragraph** | **Applied** | Line 119 reproduces proposal. Arithmetic/baseline attribution needs correction; HANDOFF’s own suggested wording causes the problem. |
| **12. “What residents wrote”** | **Partially applied** | Line 175 includes seven cards/three emails and anonymization. Incorrectly assigns all four opposed/concerned cards to Bagley residents; unsigned card has no address. |
| **13. Bagley lot = 49** | **Applied** | Lines 61 and 89 state 49 and use it in net/campus calculations. |
| **14. Median-home range** | **Applied** | Line 139 gives $98–$128, $118–$154, $1,970–$2,560 and assumed taxable values. Needs constant-value assumption and “example” framing. |
| **15. Link sources and both campaigns** | **Partially applied** | Source entries 270–340 have links except intentionally private group threads [15]. Both campaigns linked at 298/301. Letter [18] returns 401; [21] is not direct minutes; [17] is not locally established as correct source. |
| **16. Chart overlap** | **Applied** | Text values at 75. HTML:406 puts 81.0% inside bar in white at y=79, away from threshold y=52. |
| **17. Footnote back-links** | **Applied** | All 24 entries show ↩ in `page.txt`. HTML:566–589 provides valid section targets. Returns to sections, not exact citation occurrences. |
| **18. Update review date** | **Not applied** | Line 349 still says October 8, 2026. Actual fix date cannot be established; HANDOFF itself is dated October 9, later than capture. |
| **19. Remove official seal** | **Not applied** | Embedded image remains at line 19 next to “Independent voter guide” at 21. HTML:347 retains `<img class="hero-seal">`; supplied image is City seal. |
| **20. Add social-share tags** | **Applied** | Not visible in `page.txt`, which cannot establish head metadata. HTML:7–15 contains `og:title`, description, image and `twitter:card`. Share-image availability untested. |

HANDOFF’s “Already correct” list also needs caution:

- **Confirmed:** utilization arithmetic, 111−40, rounded debt/millage numbers and net-space calculation.
- **Secondary-only locally:** estimates, vote records, TIC, school funding and institutional-status claims.
- **Not present on live page:** $3,480 per household.
- **Not established as a project estimate:** “realistic” full annual operating-cost range.
- **HANDOFF timing conflict:** its source discussion says revised document arrived before the meeting; its reused wording elsewhere says before the vote.

## Math checks

### Millage to household dollars

Formula:

\[
\text{Annual tax}=\frac{\text{taxable value}\times\text{mills}}{1{,}000}
\]

Using page’s modeled average **0.4925 mills** and first-year **0.5922 mills**:

| Constant taxable value | First year | Average using 0.4925 mills | 20 years using CSV’s annual millages |
|---:|---:|---:|---:|
| $100,000 | $59.22 | $49.25 | $984.94 |
| $200,000 | $118.44 | $98.50 | $1,969.88 |
| $260,000 | $153.97 | $128.05 | $2,560.84 |
| $260,650 | $154.36 | $128.37 | $2,567.25 |
| $300,000 | $177.66 | $147.75 | $2,954.82 |

**Sources:** B:2–21; D:329 supplies $260,650 as half the reported $521,300 market value.

The page’s rounded $98–$128, $118–$154 and $1,970–$2,560 figures are reasonable. The limitation is **constant individual taxable value**, which the page does not disclose. The model’s 2% growth is growth in the **Citywide tax base**, not a promise about an individual parcel.

Illustrative sensitivity only: if an individual taxable value also rose 2% annually, applying the CSV’s millages gives approximately:

\[
\sum_{t=0}^{19}\frac{TV_0(1.02)^t m_t}{1{,}000}
\]

- Starting at $200,000: **$2,362.40**, not $1,969.88.
- Starting at $260,000: **$3,071.12**, not $2,560.84.

These are examples, not forecasts. The files do not establish individual assessment changes or a median taxable value.

### Debt-schedule totals

Summing all 20 rows, B:2–21:

\[
\sum P=\$9{,}000{,}000
\]

\[
\sum I=\$4{,}212{,}287
\]

\[
\sum(P+I)=\$13{,}212{,}287
\]

Every row satisfies principal + interest = total debt service.

| Measure | Local CSV result | Page / secondary comparison |
|---|---:|---|
| Principal | $9,000,000 | Page correct |
| Interest | $4,212,287 | Page’s $4.21M correct |
| Total debt service | $13,212,287 | Page’s $13.21M/$13.2M correct |
| Secondary exact total | $13,212,282 | **$5 lower** than CSV |
| Average annual debt service | $660,614.35 | Consistent with secondary “about $660K” |
| Millage sum | 9.8494 | Used for fixed-value 20-year tax |
| Simple mean millage | 0.49247 | Rounds to page’s 0.4925 |
| Levy years | 2027–2046 | 20 modeled levies |
| Fiscal years ending June 30 | 2028–2047 | Different labels from levy years |

The 4.13% TIC cannot be independently reconstructed from this CSV alone. It is not a flat interest rate that can simply be multiplied by $9M for 20 years.

**Small schedule discrepancy:** recomputing mills as `debt service / taxable value × 1,000` yields differences of 0.0001 mill from the supplied rounded millage for levy years 2029, 2031, 2034, 2044 and 2045. These are immaterial to page’s rounded examples but should be reconciled against the original MFCI table if publishing exact data.

### Utilization

\[
939/1{,}310=71.6794\%\rightarrow71.7\%
\]

\[
1{,}310-939=371
\]

\[
294/363=80.9917\%\rightarrow81.0\%
\]

\[
315/363=86.7769\%\rightarrow86.8\%
\]

**Sources:** V:2,25,98.

The system peak is March 12 at 13:00; weekday school peak is March 12 at 08:00; Saturday school peak is May 10 at 13:00. These are **different observations**, not a single simultaneous comparison.

The study’s school category contains **363 spaces**, while the campus-before-construction claim is **216**. They describe different inventories and should not be conflated.

### Net spaces and competing baselines

Using page’s stated inputs:

\[
\text{No-deck campus}=144
\]

\[
\text{Campus with deck}=144-49+240=335
\]

\[
\text{Gain over no-deck future}=335-144=191
\]

\[
\text{Gain over pre-construction campus}=335-216=119
\]

Using April smaller option’s approximately 213 campus total:

\[
\text{Smaller deck}=213-(144-49)=118
\]

\[
\text{Larger deck's increment over smaller deck}=240-118=122
\]

Thus **118 is the inferred smaller deck’s gross capacity**, not the increment supplied by the larger deck. “Third level” also should not be equated automatically with all 122 additional stalls: designs may differ beyond one floor.

**Sources:** TM p.5; P:124–130; D:103–108.

### Cost per space

Using secondary OAK totals:

\[
\$15{,}246{,}696/191=\$79{,}825.63
\]

\[
\$18{,}109{,}782/191=\$94{,}815.61
\]

The page’s **$80K–$95K per net space** is correct.

Gross-stall comparison:

\[
\$15{,}246{,}696/240=\$63{,}527.90
\]

\[
\$18{,}109{,}782/240=\$75{,}457.43
\]

For the proposed City half divided by **122** additional stalls:

\[
\$7{,}623{,}348/122=\$62{,}486.46
\]

\[
\$9{,}054{,}891/122=\$74{,}220.42
\]

This is an **allocation comparison**, not the actual cost of constructing the additional level. No priced smaller-deck estimate is supplied.

### Benchmark comparison

\[
240\times\$42{,}000=\$10{,}080{,}000
\]

\[
\$15{,}246{,}696-\$10{,}080{,}000=\$5{,}166{,}696
\]

\[
\$18{,}109{,}782-\$10{,}080{,}000=\$8{,}029{,}782
\]

Arithmetic supports **$10.1M baseline and $5M–$8M difference**. It does not establish a directly comparable bid or quantify architectural-feature premiums. The calculation also compares a benchmark with estimates spanning 2026 and 2028 dollars.

### Operating and repair scenarios

Primary email:

\[
\$611\times213=\$130{,}143
\]

\[
\$611\times240=\$146{,}640
\]

Primary manual’s annual operating/reserve assumptions:

\[
(\$175+\$60)\times240=\$56{,}400
\]

That is in **2018 dollars**. Reaching $70K–$75K requires:

\[
\$70{,}000/\$56{,}400-1=24.11\%
\]

\[
\$75{,}000/\$56{,}400-1=32.98\%
\]

No local CPI dataset validates that adjustment.

Using the separately attributed 1% reserve assumption:

\[
\$146{,}640+0.01(\$15{,}246{,}696)=\$299{,}106.96
\]

\[
\$146{,}640+0.01(\$18{,}109{,}782)=\$327{,}737.82
\]

This supports a **conditional $299K–$328K scenario**, rounded to $300K–$330K. It does not establish “realistic full annual cost.”

**Important distinction:** OP p.3’s **$140–$240 per space per month** includes ownership/capital-financing assumptions, unlike its $175/year operating line. At 240 spaces that monthly figure equals $403,200–$691,200 annually **in the manual’s 2018-dollar model**, including capital recovery. Adding that model directly to EGR bond debt service would risk double counting.

### Reserves

\[
\$7{,}623{,}348-\$6{,}511{,}815=\$1{,}111{,}533
\]

\[
\$9{,}054{,}891-\$6{,}511{,}815=\$2{,}543{,}076
\]

The reported fund balance cannot pay the full modeled City share, even if entirely exhausted. DD:151’s older suggestion that the City could pay its full share without borrowing is likewise inconsistent with these figures.

### Escalation

\[
\$15{,}246{,}696\times3.5\%=\$533{,}634.36
\]

\[
\$16{,}905{,}675\times3.5\%=\$591{,}698.63
\]

Page’s “more than $500,000” is correct as modeled escalation.

### Per-household totals

The live page does **not** contain HANDOFF’s $3,480 per-household figure or the older $5,000 claim. They should not be reported as live-page errors.

For completeness, secondary household count 3,797 would yield:

\[
\$13{,}212{,}287/3{,}797=\$3{,}479.67
\]

This is a population-normalized debt total, **not an individual household tax bill**. It ignores business/non-homestead tax allocation and different taxable values. Household count is secondary-only, D:155.

## Links

Supplied checks cover **16 distinct external anchor destinations**: 13 return 200, one returns 401, and two return 403.

| Destination / page source | Supplied result | Assessment |
|---|---:|---|
| Citizen Portal [12] | 200, LC:1 | Reachable; AI summary, not official minutes. |
| September 30 letter [18], Drive file [Drive ID removed] | **401**, LC:2 | **Private/inaccessible public-page citation.** Key claims at page lines 85 and 231 cannot be independently inspected through this link. |
| East Insider [13] | 200, LC:3 | Reachable; identify commissioner-authored commentary where used. |
| Safe Streets EGR [11] | 200, LC:4 | Reachable campaign site; not neutral proof of its own claims. |
| Operating-cost PDF [6], [16] | 200, LC:5 | Reachable and locally supplied. Does not contain 85% benchmark. |
| Traffic PDF [5], [22] | 200, LC:6 | Reachable and locally supplied. Contains two letters and two maps. |
| WalkSafeEGR [10] | 200, LC:7 | Reachable campaign site. |
| Kent apportionment report [20] | **403**, LC:8 | Likely bot blocking as specified by input. **Do not label dead.** No local original to verify content. |
| Census QuickFacts [23] | **403**, LC:9 | Likely bot blocking. **Do not label dead.** No local original. |
| April 20 packet [2] | 200, LC:10 | Reachable; vote outcome should cite later approved minutes. |
| June 29 packet [3], [8], [17] | 200, LC:11 | Reachable; Walker benchmark placement remains unsubstantiated. |
| July 20 packet [4] | 200, LC:12 | Reachable; quote from July 20 minutes is reported in later August 3 packet. |
| August 3 packet [1], [7], [9], [24] | 200, LC:13 | Reachable; not the correct sole source for August 3/6 final vote outcomes. |
| FY2025 ACFR [19] | 200, LC:14 | Reachable; contents not locally supplied. |
| District project page [21] | 200, LC:15 | Reachable, but source label says board minutes. Use direct approved minutes or explain intermediary. |
| YouTube FOX 17 [14] | 200, LC:16 | Reachable response does not establish video title, availability or contents. |

Additional findings:

- All internal fragment destinations exist; no duplicate IDs or missing anchor targets were found.
- All 24 source entries contain working internal return targets, though returns go to sections rather than individual citations.
- D:67 uses a **different Drive file ID** for the September 30 letter. Neither file’s contents can be established locally. Do not substitute IDs without verifying the intended document.
- HTML:11,15 references `/parking-deck/assets/share-card.png`; its HTTP status is not in `link-check.txt`.
- Google Fonts CSS import at HTML:21 is also not checked. These are asset availability gaps, not proven broken links.
- There are **no confirmed 404/410 dead links** in the supplied checks.

## Neutrality and internal consistency

| Issue | Evidence | Why it matters |
|---|---|---|
| Official seal beside “Independent voter guide” | Page:19–27; HTML:347 | May imply City endorsement despite non-affiliation declaration. |
| “Strongest need case” is presented as fact | Page:43,65 | Editorially ranks reasons without a documented comparison. Shared school/community uses appear in P:64–69. |
| “Key primary-source finding” highlights only the original recommendation | Page:91–97 | Follow-up is included, which improves balance, but visual emphasis still favors the earlier recommendation. Present the dated recommendation and follow-up together. |
| Aggregate capacity framed as generally available | Page:67–69 | 371 system-wide empty spaces do not establish suitable nearby spaces for every school/event user. D:226–231 describes concentrated overcapacity. |
| Shared community benefits receive less development than risks | Page:43–65,237–263 | Pool, gym, theater, school visitors and Gaslight workforce uses are documented in secondary presentation summary P:64. Balanced coverage should include these proposed uses and their limits. |
| “Realistic full annual cost” overstates uncertain scenarios | Page:117 | Promotes selected assumptions to a project-specific finding; “full” conflicts with exclusion of debt/capital recovery. |
| City’s half “therefore buys” the third-level increment | Page:119 | Implies proven allocation and marginal value; neither a smaller-deck price nor signed allocation is supplied. |
| Unsupported “False” verdict | Page:220 vs legend:233 | Absence of LOS analysis is treated as contradictory evidence. |
| Unsupported “True” verdict | Page:221 | One $500K figure inside a campaign range is treated as validation of the full range. |
| “No minutes” becomes “no record” | Page:179 | Broader than evidence; city memos and presentations document some choices. |
| Institutional negatives sound current and exhaustive | Page:187,191,205,208,255–263 | Local files support limited review findings, not an exhaustive October publication/records search. |
| Market-value median presented as a taxable-value median | Page:139 | Assumed taxable range may be read as a measured typical household bill. |
| Full City share supposedly payable from reserves | Page:141 | Conflicts with the page’s own $7.6M–$9.1M City-share range. |
| Blank-address card counted as Bagley resident | Page:175 | Inflates geographically concentrated opposition. |
| Before-meeting timing becomes before-vote timing | Page:183 | Makes perceived deliberation time substantially shorter than reported sources establish. |
| 85% attribution conflicts with source contents | Page:69,316 | Manual figure is a cost table. |
| Claimed method understates assumptions | Page:345,349 | “Inferred” includes assumptions and judgments, not merely arithmetic. |

Positive neutrality features already present: both campaign sites are linked; the February follow-up is included; Saturday school occupancy above 85% is acknowledged; street-crossing benefit and longer walk are paired; public-vote emails are distinguished from opposition; tax comparisons include a service-equivalence caveat; and the page acknowledges that Commission chose voter approval.

## Prioritized fix list

The replacements below are exact proposed text. Secondary-supported replacements retain attribution instead of upgrading summaries to primary proof.

### Critical — Public access to the letter supporting central claims

**Location:** source [18], page lines 321–322.

**Current text:**

> Construction-period space count and school-event parking statement. Open letter

**Suggested replacement:**

> Construction-period space count and school-event parking statement. The linked Drive file is not publicly accessible. These statements are corroborated by the research summaries but require an accessible primary copy of the September 30 letter.

Remove the inaccessible “Open letter” anchor until a verified public copy is available.

**Source:** LC:2; D:81–82,103–106. This report cannot make the file public or verify an alternative copy.

### High — Correct the resident-address attribution

**Location:** page line 175.

**Current text:**

> The August 3 packet reproduces seven handwritten May 27 comment cards: four opposed or concerned from Bagley Avenue residents, one supportive from Greenwood Avenue, and two offering ideas without taking a position.

**Suggested replacement:**

> The August 3 packet reproduces seven unique handwritten comment cards associated with the May 27 session. Four oppose the deck or raise concerns: three include Bagley Avenue addresses, and one is unsigned with no address. One supportive card includes a Greenwood Avenue address, and two offer ideas without an express position. The packet prints one three-card page twice; those cards are counted once.

**Source:** CC pp.2–6; TR:90,145–156. Some cards are not individually dated.

### High — Correct resolution timing and identify the account’s source

**Location:** page line 183.

**Current text:**

> A revised 33-page resolution arrived about 90 minutes before the August 3 vote and was not public beforehand.

**Suggested replacement:**

> The supplied research summaries, citing East Insider, report that a revised 33-page resolution reached commissioners about 90 minutes before the August 3 meeting and was not public beforehand.

**Source:** P:34; D:64,357; DD:178. Original distribution evidence unavailable locally.

### High — Correct the third-level baseline and avoid marginal-cost attribution

**Location:** page line 119.

**Current text:**

> Commissioner Schwartz said July 20: “the school needs two levels and the third is a possibility for the City.” The April memo says a two-story deck meets the school’s no-net-loss goal. The City’s half—about $7.6M–$9.1M—therefore buys roughly 118 spaces beyond that, about $64,000–$77,000 each.

**Suggested replacement:**

> The packet findings quote Commissioner Schwartz on July 20: “the school needs two levels and the third is a possibility for the City.” They report that the April two-story option provided approximately 213 campus spaces. Using 144 spaces without a deck and a 49-space existing Bagley lot implies approximately 118 stalls in that smaller deck. A 240-stall deck would add approximately 122 stalls beyond that option. Dividing the proposed City half of $7.6M–$9.1M by 122 gives approximately $62,000–$74,000 per additional stall. This is an inferred allocation comparison, not a priced estimate of the additional level.

**Source:** P:103,124–132; TM p.5; calculations above. Cite original July 20 minutes when available.

### High — Replace “realistic full annual cost” with documented benchmark scenarios

**Location:** page line 117.

**Current text:**

> The City’s figure traces to a deputy city manager’s April 23 email: Grand Rapids’ $611 per space, “not depreciation,” times 213 spaces, or $130,143, for the April 213-space design. At 240 spaces that is about $147,000. The Shared Parking Manual the City circulated puts basic operations at $175 and a repair sinking fund at $60 per space per year in 2018 dollars, about $70,000–$75,000 a year today for 240 spaces. Adding 1% of construction cost as a repair reserve gives an upper case near $300,000–$330,000. The realistic full annual cost is therefore about $70,000–$330,000; the City’s half about $35,000–$165,000. No dedicated funding source is identified.

**Suggested replacement:**

> Doug La Fave’s April 23 email reports Grand Rapids operations and maintenance costs of $611 per space per year, excluding depreciation, and a $130,143 annual total. That total corresponds to 213 spaces. Applying the same rate to 240 spaces gives $146,640 annually, inferred. The circulated Shared Parking Manual lists $175 for basic operations and a $60 capital-maintenance sinking fund per space per year, totaling $56,400 for 240 spaces in 2018 dollars. No CPI dataset supplied for this review establishes a current-dollar adjustment. Separately, applying the research dossier’s 1%-of-construction-cost repair-reserve assumption to the $146,640 operating scenario produces approximately $299,000–$328,000 annually, inferred, or $150,000–$164,000 for a proposed 50% City share. These are benchmark scenarios, excluding bond debt service, rather than a project-specific operating budget. The reviewed summaries identify no finalized funding source for the City’s recurring share.

**Source:** OP pp.1–3; D:318,386–390; P:40–42.

### High — Remove unsupported 85% attribution

**Location:** source [16], page line 316.

**Current text:**

> 85% utilization benchmark and 2018 operating/repair-reserve figures, circulated with the City’s February 4 email.

**Suggested replacement:**

> 2018 operating-cost, capital-maintenance sinking-fund and ownership-cost assumptions, circulated with the City’s February 4 email. Figure 5-1 does not contain an occupancy benchmark.

**Location:** page line 69, final sentence.

**Current text:**

> The school lots reached 81% on the measured weekday and 86.8% on Saturday; the commonly used 85% benchmark was not reached system-wide on the weekday.

**Suggested replacement:**

> The school category peaked at 81.0% on a measured weekday and 86.8% on Saturday. System-wide utilization stayed below 85% on all three measured dates. The supplied primary documents do not establish the source or applicability of an 85% occupancy benchmark.

Remove [16] from the occupancy claim. Remove the unsupported threshold line from the chart, or clearly label it as an assumed reference pending an appropriate source.

**Source:** OP p.3; V:2–117.

### High — Correct LOS verdict

**Location:** page line 220.

**Current text:**

> “LOS F at Bagley & Lake” | False / not in source | WalkSafeEGR attributes this to the Progressive traffic memo. Neither the Nov. 10, 2025 memo nor the Feb. 4, 2026 letter contains any level-of-service analysis.

**Suggested replacement:**

> “LOS F at Bagley & Lake” | Unsupported by the cited documents | The supplied campaign summaries attribute this claim to Progressive. Neither the November 10, 2025 memo nor the February 4, 2026 follow-up contains a level-of-service analysis. These documents therefore do not establish a LOS grade for the intersection.

**Source:** TM pp.1–4; D:245,279. Do not imply an alternative LOS grade.

### High — Correct signal-range verdict

**Location:** page line 221.

**Current text:**

> “Signal costs $350K–$600K” | True | The City used a placeholder of about $500K; the April memo says “up to $500,000.”

**Suggested replacement:**

> “Signal costs $350K–$600K” | Partially supported | The research dossier reports a City placeholder of about $500,000 and an April memo stating “up to $500,000.” That supports a $500,000 planning figure, but the supplied documents do not verify the campaign’s $350,000 and $600,000 endpoints.

**Source:** D:244; original April memo unavailable locally.

### High — Correct reserve-funding implication

**Location:** page line 141.

**Current text:**

> The City reported $6,511,815 in unassigned general-fund balance, equal to 44.01% and above its 20%–25% target. Using reserves could reduce borrowing, but paying the full City share from that balance would substantially reduce the cushion and would not solve ongoing operating costs.

**Suggested replacement:**

> The research dossier reports $6,511,815 in unassigned general-fund balance as of June 30, 2025, equal to 44.01% of expenditures and transfers, against a 20%–25% policy target. That reported balance is less than the proposed $7.6M–$9.1M City share. Using a portion could reduce borrowing, subject to other obligations and reserve policy, but could not pay the full share and would not establish recurring operating funding.

**Source:** D:163; P:40–42; reserve arithmetic above.

### High — Disclose primary-evidence limits in method

**Location:** page line 345.

**Current text:**

> Numbers are attributed to the closest available primary record. Campaign pages and community discussion are used to frame claims, not establish facts. “Inferred” marks arithmetic calculated from cited values rather than a figure stated verbatim in a source. Unreleased agreements, surveys, estimates and datasets are treated as missing—not assumed.

**Suggested replacement:**

> This review directly checks the supplied utilization and debt CSVs, traffic correspondence, operating-cost correspondence, parking map and resident correspondence. Other claims are corroborated by research summaries and have not been independently checked against their original documents in this review. Campaign claims are identified through those summaries. “Inferred” identifies calculations or assumptions; each should state its inputs, baseline and limitations. A document absent from the reviewed files is not assumed to be nonexistent or unpublished.

**Source:** Local file inventory; citation audit above.

### High — Correct destinations for vote records and quotations

**Locations:** sources [1], [2], [4], [21] and attached vote citations.

**Current text:**

> August 3, 2026 City Commission packet

**Suggested additional source text:**

> August 3 and August 6, 2026 approved City Commission minutes, reproduced in the August 17 packet. The supplied research dossier attributes the vote counts to these minutes; the original minutes were not included in this review.

**Current text:**

> April 20, 2026 City Commission packet

**Suggested additional source text:**

> April 20, 2026 approved City Commission minutes, reproduced in the May 4 packet. Use these minutes for the design-funding vote outcome.

**Current text:**

> Bond structure, financing options and meeting record.

**Suggested replacement for source [4]:**

> Bond structure and financing options. The July 20 minutes quoted on this page are reported in the August 3 packet, pages 248–251.

**Current text:**

> EGRPS Board minutes, April 20, 2026 … Open district project page

**Suggested replacement:**

> EGRPS Board action, April 20, 2026. The research dossier reports a 5–1 vote and an approximately $7M set-aside from general and capital improvement funds. The linked district project page is an intermediary; a direct link to the approved minutes is needed.

**Source:** D:40,50–56; P:100–103. Add only verified destinations; local-only review cannot validate new URLs.

### Medium — Present household amounts as fixed-taxable-value examples

**Location:** page line 139.

**Current text:**

> For a median home—about $521,000 market value and roughly $200,000–$260,000 taxable value—the model implies about $98–$128 a year on average, $118–$154 in year one, or $1,970–$2,560 over 20 years.

**Suggested replacement:**

> At a constant taxable value of $200,000–$260,000, the modeled levy would cost approximately $99–$128 annually on average, $118–$154 in the first year, and $1,970–$2,561 over 20 years, inferred. These are examples, not a measured median household bill. The research dossier reports a Census median market value of $521,300, but market value does not establish a home’s taxable value. Use the taxable value on your assessment; future changes would change the total paid.

**Source:** B:2–21; D:154,329–333.

### Medium — Distinguish deck estimates from bundled scope

**Location:** page lines 45–49.

**Current text:**

> $15.2M–$18.1M  
> A three-level, 240-space deck, plus signals and pedestrian work.

**Suggested replacement:**

> $15.2M–$18.1M estimated deck cost across design options and dollar years  
> The proposal includes a three-level deck with a 240-space design target, plus traffic-signal and pedestrian work. The supplied summaries report OAK deck estimates of approximately $15.25M–$16.91M in 2026 dollars, with an upper 2028 estimate of $18.11M. They do not establish a complete itemized budget for all additional work.

**Source:** P:36–45; D:80,389.

### Medium — Qualify benchmark comparison and correct source [17]

**Location:** page line 113.

**Current text:**

> An industry benchmark cited in the record is roughly $42,000 all-in per structured space.

**Suggested replacement:**

> The research dossier cites a Walker Consultants Saugatuck comparison of approximately $42,000 all-in per space for a plain structured-parking facility. Its original report was not supplied for this review. Applying that figure to 240 spaces gives $10.08M, inferred; comparison with EGR’s estimates does not isolate the cost of specific design features.

**Location:** source [17], page line 319.

**Current text:**

> Structured-parking cost context cited in the reviewed record. Open June 29 packet

**Suggested replacement:**

> Structured-parking cost context attributed by the research dossier to Walker Consultants’ 2026 Saugatuck summary. The June 29 packet has not been established as the source of this benchmark; a verified direct source is needed.

**Source:** D:209,325,395–396; DD:301.

### Medium — Add LTGO petition qualification

**Location:** page line 159.

**Current text:**

> The Commission considered limited-tax general-obligation bonds, which would not require a vote, and chose to proceed with voter-approved bonds.

**Suggested replacement:**

> The research summaries report that the Commission considered limited-tax general-obligation bonds, which could proceed without an election unless a sufficient petition required one, and chose to seek voter approval instead.

**Source:** D:157; F:252. Original legal/financing materials absent.

### Medium — Correct alternatives-table precision

**Current text, page line 201:**

> Use nearby on-street supply | 89–111 | About $0

**Suggested replacement:**

> Use nearby on-street supply | Minimum 89 available; average 111 during the surveyed school day | No cost estimate supplied

**Source:** TM p.2.

**Current text, page line 204:**

> Two-story deck | ~118–136 | Not released | April memo: about 213 campus spaces, “no net loss” (≈118-space deck, inferred). Progressive’s 2–4 level range starts at 136.

**Suggested replacement:**

> Two-story deck | Approximately 118 inferred from April campus counts; separate earlier memo’s range starts at 136 | No priced smaller-deck estimate supplied | These figures describe different concepts. The April option reportedly gives approximately 213 campus spaces; the November memo discusses 136–291 spaces across two to four levels.

**Source:** P:124–125; TM p.3; campus arithmetic above.

**Current text, page line 206:**

> Shared parking | Depends on partners | Not developed | Concept only

**Suggested replacement:**

> Shared parking | Depends on partners | No cost estimate supplied | Residents suggested partnering with other lots; the supplied files do not establish subsequent implementation status.

**Source:** CC p.2; TR:108.

### Medium — Narrow categorical institutional claims

**Current text, page line 179:**

> Meetings stayed below quorum, so no minutes exist. The public record does not show how key project choices were made.

**Suggested replacement:**

> The research dossier, citing East Insider, reports that the subcommittee met below quorum and kept no minutes. City memos and presentations describe some project choices, but the supplied files do not include a complete subcommittee decision record.

**Source:** D:62,417; P:21,102–103,124.

**Current text, page line 191:**

> No executed intergovernmental agreement was identified. Cost share, ownership, access and the City’s third-level role therefore remain nonbinding.

**Suggested replacement:**

> No executed intergovernmental agreement is included in the supplied files. The research dossier cites August reporting that an agreement had not yet been signed. Its October status and the legal effect of separate board actions have not been independently verified in this review.

**Source:** D:65,419.

**Current text, page line 208:**

> No student survey was conducted to test likely deck use, willingness to wait in an exit queue, or sensitivity to location. That leaves demand-management and behavior assumptions largely untested.

**Suggested replacement:**

> The research dossier attributes the absence of a student survey to Commissioner Groff-Blaszak’s published account. No survey is supplied here. The traffic memo predicts that exit delays could discourage deck use, but the supplied files do not establish actual future usage.

**Source:** D:293–295,427; TM p.3.

For page lines 205,255,259,261 and 263, consistently replace publication-wide “no … is published” claims with **“not included in the supplied files”** or an explicitly attributed reviewed-record finding.

### Medium — Give proposed benefits and unresolved limits comparable treatment

**Location:** page line 65.

**Current text:**

> The strongest need case is a projected 2028–2030 construction-period shortage, not present-day system overcrowding. The strongest unresolved issues are the unsigned city–school agreement, long-term upkeep, and the lack of binding commitments on street-parking removal or free use.

**Suggested replacement:**

> The measured 2025 system peak was 71.7%, while the school category reached 86.8% on Saturday. The proposal would replace lost campus parking and provide shared parking for school activities and Gaslight Village users. The traffic memo describes a street-crossing benefit and possible exit delays. Research summaries also project reduced campus supply during 2028–2030. Questions remain about delivery timing, operating and repair funding, public access, fees and any street-parking changes; the supplied files do not include a finalized agreement covering those terms.

**Source:** V:25,98; TM p.3; P:64–69; D:105,419.

### Medium — Remove official seal

**Location:** embedded image, page line 19; HTML:347.

**Current element:**

> `<img class="hero-seal" … alt="" />`

**Suggested replacement:**

> Remove the image element and retain the existing “Independent voter guide” text.

**Source:** `page.html`:347 and `page.txt`:19–27; HANDOFF:149–150. A decorative plain “E” mark is also consistent with the requested change, if needed.

### Low — Label secondary commentary and AI summaries accurately

**Current source [12] text:**

> Meeting record and summary of the August 3 ballot vote.

**Suggested replacement:**

> AI-generated summary of the August 3 meeting. Use approved minutes to verify vote outcomes.

**Source:** D:354.

**Current source [13] text:**

> Local reporting and community context.

**Suggested replacement:**

> Commissioner Groff-Blaszak’s published commentary and local community context. Accounts of disputed process details should be checked against original records.

**Source:** D:293–297.

### Low — Avoid presenting a paraphrase as a verbatim callout

**Current text, page line 93:**

> Build the high-school expansion without new parking.

**Suggested replacement:**

> November 2025 recommendation, paraphrased: proceed with the high-school expansion without parking improvements.

Keep February follow-up immediately adjacent, preferably with equal visual prominence.

**Source:** TM p.3 Recommendations; TM p.1 follow-up.

### Low — Reconcile minor CSV transcription discrepancies

**Current rounded page text:**

> $13.21M principal plus projected interest

**Suggested replacement:**

> $13.21M principal plus projected interest. The supplied annual schedule sums to $13,212,287; research summaries report $13,212,282, a $5 difference requiring comparison with the original MFCI table.

This note can sit in the source entry rather than the main card.

**Source:** B:2–21; D:147; F:199. Do not silently alter the CSV or pretend the original was verified.

### Low — Clarify “inferred” and review date

**Current text, page line 349:**

> Figures marked “inferred” are arithmetic from cited sources, not stated in any source. Last reviewed October 8, 2026.

**Suggested replacement:**

> Figures marked “inferred” include calculations or assumptions; their inputs and limitations are stated alongside them. Page snapshot fetched October 8, 2026. The date of the next completed factual review should be recorded when that review is finished.

**Source:** Capture information supplied with task; IDs 069,092,206. No verified later edit date is available locally.
