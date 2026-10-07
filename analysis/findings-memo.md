# Findings Memo — East Grand Rapids Spending Analysis (merged, 2026-10-07)

Merged from Workstream A (financial-file analysis) and Workstream B (official public records).
Every number below traces to a file in this directory or a URL in `sources.md`.
Neutral framing throughout: flags are "things worth understanding," not allegations.

## Cross-check (coordinator QC): computed totals reconcile to the audited financials

- Workstream A's **FY2025 headline: $26,702,474.22** = operating expenditures of all governmental funds
  + Water & Sewer enterprise fund + Motor Equipment Revolving Fund, **excluding** interfund
  transfers ($3,232,450), GASB-34 conversion entries, and the Health Care / Pension / OPEB
  trust funds (excluded to avoid double-counting costs also booked as departmental spending).
- The governmental-funds portion of that figure = **$21,943,289**, vs. the audited ACFR
  (FY ended 6/30/2025) governmental-fund expenditures of **$21,943,295** — a **$6 difference
  (rounding)**. The computed total is verified against the audit.
- Accrual-basis "primary government expenses" in the ACFR are $19,067,333 (different
  accounting basis; not directly comparable to the modified-accrual headline).
- GL files balance to $0.00 (debits − credits); check-register parsed totals match both
  report footers to the cent.

## Note on the numbers in the original site brief

The brief's example figures were spot-checked: buildings $1.17M → $1.93M (+65%) and
public safety $4.93M → $4.67M (−5%) both match the verified data (actuals: $1,173,693 →
$1,932,488; $4,941,244 → $4,690,846). **But the brief's headline "$29.2M" does not match:
verified FY2025 total city spending is $26.7M.** Do not use $29.2M or the +1.7% change
figure (verified FY24→FY25 change on the same definition: $27.57M → $26.70M, −3.1%).
The police-uniforms example ($28K budget / $46,253 spent) was not separately verified —
verify per-item before use.

## The 10 most important verified findings

1. **FY2025 total city spending was $26,702,474** (definition above; reconciles to the
   audited ACFR within $6). FY2024 comparable: $27,565,044. Source: GL files →
   `spending.json`; ACFR via Nov 25, 2025 commission packet.

2. **Only ~30% of a resident's property-tax bill goes to City Hall.** 2025 homestead levy:
   **47.4995 mills** total; the City of EGR levies just 14.2107 mills (operating 11.1419,
   roads 1.9632, complex debt 0.6129, parks debt 0.3508 + 0.1419). The rest: EGR schools
   11.7894, Kent County 5.7573, Kent ISD 5.3515, GRCC 1.6793, State Education Tax 6.0,
   The Rapid 1.3817, KDL 1.0832. School debt alone (9.95 mills) is 70% of the entire city
   levy. Non-homestead pays 65.4995 (adds the 18-mill school operating levy).
   Source: city's official millage document (6/25/2026) → `tax.json`.

3. **The parking-deck bond is on the November 3, 2026 ballot — not yet approved.** Up to
   **$9,000,000** in GO unlimited-tax bonds (max 20-year term per series) for a ~240-space
   deck on Bagley at the EGR schools lot, plus traffic signals and pedestrian/
   micromobility infrastructure. Ballot estimates: **0.5922 mills first year, 0.4925
   average** (a corrected resolution fixed 0.44925 → 0.4925; vote 4-1-2). By arithmetic
   (no official dollar figure published): ~$118/yr first year on a $200,000 taxable value
   (~$400K home), ~$98.50/yr average — about 1.2% added to the homestead rate. The same
   ballot also carries the Kent County jail millage (0.98-mill renewal+increase).
   Source: official special-meeting minutes; `tax.json`.

4. **Manhattan Park is the city's biggest active capital project: $2,377,027 in FY2025,
   up 272% from $638,849 in FY2024.** FY2024 was design (Viridis Design Group $121,080)
   and early site work (Groundhawg Excavating $489,983); FY2025 is construction by
   Katerberg-VerHage Inc ($1,939,970 booked; $1,981,311 in checks, incl. single payments
   of $708,396 and $594,567). Cumulative FY24+FY25 ≈ $3.02M, consistent with secondary
   reporting of a ~$3.18M program. Source: GL journal descriptions; check register.

5. **Parks playground capital wound down as Manhattan Park ramped up: $3,290,943
   (FY2024) → $125,806 (FY2025).** Net parks & recreation spending fell $6.67M → $5.39M —
   a completed project phase offsetting the Manhattan Park build. Source: GL files.

6. **City buildings capital spending rose 156% ($329,155 → $843,495), and it is
   itemized:** a DPW salt/aggregate storage building (~$275K + $34K steel), HVAC capital
   replacements (~$110K + ~$106K), flooring ($109K), and an EGR library study room
   ($56K). Source: FY2025 GL journal descriptions on 101-265-9700.00.

7. **Employee pharmacy costs jumped 153% ($161,771 → $409,879, +$248,108)** in the
   Health Care Fund, spread across twice-monthly Blue Cross claim payments with no
   single anomalous payment. Medical (HRA) claims rose 27% ($661K → $842K); total
   Health Care Fund spending rose 31% to $2,026,084. **The cause (utilization, specialty
   drugs, enrollment) is not in these files.** Source: GL files.

8. **FY2026 fleet buying is over budget at the 75% mark — trucks identified.**
   Motor Equipment vehicle purchases: $1,180,000 budget vs $1,441,260 spent through
   3/31/2026 (122%; $261,260 over). Detail: $567,091 International sewer truck,
   $118,888 loader, $77,662 excavator, two dump trucks ~$114,861 each plus upfits,
   $121,166 for two replacements. **A 3/31 comparison is not an overrun finding** —
   capital budgets are routinely amended and purchases are lumpy. 51 accounts are over
   budget at the 75% mark overall (timing caveat applies to all). Source: YTD file.

9. **The check-register files are mislabeled by one fiscal year, and two-thirds of
   register dollars are tax pass-throughs, not city spending.** "FY2024 Check
   Register.xlsx" holds checks dated 7/3/2024–6/30/2025; "FY2025 Check Regsiter.xlsx"
   holds 7/1/2025–6/4/2026 (partial). **No FY2024-dated check data was provided.**
   ~$33.2M/yr of register dollars are property-tax pass-throughs to schools, county,
   ISD, and GRCC — excluded from vendor analysis. City-vendor checks: $17.5M (FY2025).
   The register also omits payroll (ACH) and wires. Source: both register files.

10. **Vendor spending is concentrated but explainable: top 10 vendors = 59.8% of
    city-vendor checks.** Top 5 (FY2025 checks): Grand Rapids City Treasurer $2,047,632
    (monthly wholesale water purchases), Katerberg-VerHage $1,981,311 (Manhattan Park),
    Michigan Paving $1,839,247 (street resurfacing), Kent District Library $1,049,240
    (library contract/millage remittance), US Bank $973,700 (bond debt service).
    Context: the city's General Fund balance ended FY2025 at $7,281,401 (~50% of
    expenditures, well above typical 25% benchmarks); adopted FY2025-26 all-funds
    budget is $37,669,310. Source: check registers; ACFR; adopted budget.

## Claims explicitly NOT verified

- The **reason** pharmacy and medical claims rose — needs benefits/claims detail.
- Whether any FY2026 over-budget account finishes the year over budget — needs final
  amended budgets and year-end actuals.
- What project the spring-2026 AJZ Concrete payments ($61,869 → $360,208, +482%)
  belong to — needs invoices or post-3/31/2026 project coding.
- The split of Grand Rapids City Treasurer payments between wholesale water and fees.
- What the $545,138 in Fifth Third Bank purchasing-card settlements bought.
- Why the DB pension contribution fell $1,380,000 → $1,100,000 — needs actuarial data.
- Why OPEB medical claims tripled ($59,967 → $187,942).
- FY2024 vendor totals — no FY2024-dated check data provided.
- Whether the $100K–$136K annual transfer imbalance (677 → OPEB trust) is a booking
  artifact — the receiving entry is not in these extracts.
- The $1,965,045 pension transfer on GL 101-965-9950.12 (a GL number with no activity
  in the FY2024 extract and no chart-of-accounts entry).
- Official dollar impact of the parking bond on a sample home (city published millage
  only); 2026 winter millage rates (not yet levied); full official text of the $9M
  bond resolution (correction verified via official minutes; complete ballot text only
  via a commissioner's secondary write-up); the city's own FY2026-27 budget book
  (figures via agenda-packet mirror only); certified canvass for the Nov 2025 school
  millages; per-project actual spending and vendor names beyond the GL (would need
  packet-by-packet review); ladder-truck (~$1.7M) and engine (~$700K) figures
  (secondary reporting only); whether the parking proposal passes (election 11/3/2026).

## Data-quality notes for the site builder

- Label all vendor figures by **actual check-date fiscal year**, not by the register
  filenames (they are off by one year).
- The check register is a **complement** to the GL, not a reconciliation of it
  ($17.5M city-vendor checks vs $26.7M GL operating expenditures).
- Budget-vs-YTD comparisons at 3/31 (75% of the fiscal year) are timing snapshots,
  not overrun findings — the methodology page must carry this caveat.
- Every category total in `spending.json` reconciles exactly to fund totals; the
  trust-fund categories (health care, pension, OPEB) are reported separately to
  avoid double-counting.
