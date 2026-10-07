# Methodology — East Grand Rapids Spending Analysis (Workstream A)

Neutral, resident-friendly analysis of City of East Grand Rapids financial data.
Tone: neutral analyst. A "flag" means spending that differs from budgets, history, or normal
patterns and may deserve explanation — it never implies fraud or misconduct.

## Sources (all in `~/workspace/egr-spending/data/`)

| File | Contents | Period covered |
|---|---|---|
| Chart of Accounts.xlsx (sheet ChartofAccounts) | 1,425 GL accounts with type, description | As of 6/5/2026 |
| GL Activity by Journal Type 7.1.23-6.30.24.xlsx (sheet ActivitybyGLJournal) | ~39,235 journal transactions | FY2024 (7/1/2023–6/30/2024) |
| GL Transactions 7.1.24-6.30.25.xlsx (sheet ActivitybyGLJournal) | ~38,994 journal transactions | FY2025 (7/1/2024–6/30/2025) |
| YTD GL Detail thru 3-31-26.xlsx (sheet RevenueandExpenditureWithActivi) | 669 accounts: amended budget vs YTD actual + 11,666 transaction lines | FY2026 thru 3/31/2026 (75% of FY) |
| FY2024 Check Register.xlsx (sheet CheckRegister) | 2,371 check disbursements | **Check dates 7/1/2024–6/30/2025** (see labeling caveat) |
| FY2025 Check Regsiter.xlsx (sheet CheckRegister) | 2,309 check disbursements | **Check dates 7/1/2025–6/4/2026** (see labeling caveat) |
| Fund transfers 6.30.24.xlsx / 6-30-2025.xlsx / 6.30.26.xlsx (sheet RevenueandExpenditureReport) | Transfer accounts only (depts 930/965), not full revenue/expenditure reports | FY2024 / FY2025 / FY2026 |

City fiscal year: July 1 – June 30. All figures USD.

## Check-register labeling caveat (material)

The two check-register **file names do not match their contents**. Each file's own title row and the
actual check dates show: the file named "FY2024 Check Register.xlsx" contains checks dated
7/3/2024–6/30/2025 (i.e., FY2025), and "FY2025 Check Regsiter.xlsx" contains checks dated
7/1/2025–6/4/2026 (i.e., FY2026, partial, with 277 checks still marked "Open"). All vendor figures are
labeled by **actual check-date fiscal year**. No check data with FY2024 (7/1/2023–6/30/2024) dates was
provided, so vendor `fy2024` totals are null by necessity, not by choice. Year-over-year vendor
comparisons use like-for-like July–May windows (the FY2026 file ends 6/4/2026).

## GL account structure (from Chart of Accounts)

GL numbers are `FFF-DDD-AAAA.SS`:
- **FFF (fund)**: 101 General Fund; 202 Major Street; 203 Local Street; 204 Municipal Street;
  205 Public Safety; 265 Drug Law Enforcement; 286 ARPA; 308/309 Parks Millage Debt Service;
  372 Municipal Complex Debt Service; 408 Parks Capital Projects; 592 Water & Sewer (enterprise);
  677 Health Care (internal service); 692 Motor Equipment Revolving (internal service);
  731 Retirement System (fiduciary); 736 OPEB Trust (fiduciary); 810 Special Assessment;
  901 GASB 34 (government-wide conversion entries); 099 pooled cash; 701 tax-collection agency fund.
- **DDD (department)**: e.g., 345 Public Safety, 751 Recreation, 447 City Engineering,
  905 Debt Service, **930 Transfers In, 965 Transfers Out**.
- **AAAA.SS (account)**: object code, e.g., 7060 salaries, 8010 contractual services,
  9700 capital expenditures, 6900/9950 transfers.

## How "spending" is computed

1. Both GL activity files were parsed journal-line by journal-line into per-account debit/credit totals.
   **Sanity check:** sum of (debits − credits) over all accounts = $0.00 both years (double-entry balances).
2. **Operating expenditures** = net (debit − credit) on accounts typed `Expenditure` in the chart of accounts,
   **excluding** department 965 (interfund transfers-out) and fund 901 (GASB 34 conversion entries, which are
   negative in these extracts and represent accounting adjustments, not cash spending).
3. **Interfund transfers excluded from all spending totals** (depts 930/965) so the same dollars are not
   counted in both the sending and receiving funds. FY2025 transfers-out totaled $3,232,450; FY2024 $2,862,456.
4. **Headline "Total City Spending FY2025" = $26,702,474.22**, defined as: total FY2025 operating
   expenditures of all governmental funds plus the Water & Sewer enterprise fund plus the Motor Equipment
   Revolving Fund, excluding interfund transfers and GASB 34 entries. The Health Care internal-service fund
   (677), Retirement System fiduciary fund (731), and OPEB Trust fiduciary fund (736) are excluded from the
   headline to avoid double-counting costs already recorded as departmental expenditures (e.g., ~$1.2M of
   employer health premiums appear both as departmental fringe-benefit expenditures and as Health Care Fund
   claim expenditures). Their totals are reported separately in spending.json. An all-funds gross figure
   ($30,841,463.63) is also reported with this caveat.

## Plain-English category mapping rules

Each (fund, department) pair maps to exactly one category; category totals reconcile exactly to fund totals.

- **police & public safety**: fund 101 depts 345, 346; fund 265 (drug seizure); fund 205
- **roads**: funds 202, 203, 204 (all depts); fund 101 depts 447 (city engineering), 448 (street lighting)
- **parks & recreation**: fund 408 (all); fund 101 depts 621, 751, 756, 771, 775, 777, 778, 779, 781, 783
- **city administration**: fund 101 depts 101, 172, 192, 209, 210, 260, 371, 450, 485, 875
- **water & sewer**: fund 592 (all)
- **buildings**: fund 101 dept 265 (city buildings)
- **debt service**: dept 905 in any fund (308, 372, 408)
- **vehicles & equipment**: fund 692 (motor equipment revolving)
- **other**: fund 101 depts 000, 528 (yard waste/refuse); anything unmapped (funds 286/810 have only transfers)
- Reported separately (not in headline): employee health care (677), pension trust (731), OPEB trust (736)

Judgment calls: GF engineering (101-447) is mapped to roads (engineering primarily supports streets/utilities);
GF street lighting (101-448) to roads. Vendor-to-department attribution (vendors.json) was derived by matching
vendor names against FY2025 GL journal descriptions; it reflects where the dollars were booked, not the check
register (which carries no department coding).

## Flag definitions

- **Over budget (FY2026 YTD):** expenditure account with YTD actual > full-year amended budget at 3/31/2026.
- **Ahead of pace:** YTD/budget materially above 75% without exceeding 100% (informational; not flagged individually).
- **YoY change:** department- or account-level FY2024→FY2025 change flagged when |change| > $75,000 at department level.
- **Vendor spike:** Jul–May like-for-like vendor total change > ~50% and > $25,000.
- **Duplicate-looking payments:** same normalized vendor + same amount within 31 days, amount ≥ $1,000.
- **Vendor concentration:** share of city-vendor check dollars by top 5/10/20/30 vendors.
- **Large single purchases:** largest individual check-register payments (city vendors only).
- Every flag carries `status`: "explained" (cause verified in the files) or "needs additional documentation"
  (cause not determinable from the files — never guessed).

## The budget-vs-actual timing caveat (read first)

A YTD budget comparison at 3/31/2026 is **not** an overrun finding. Reasons: (1) spending is seasonal
(winter maintenance, road salt, and paving concentrate in specific months); (2) capital purchases are lumpy
(one $567K sewer truck moves a whole account); (3) encumbrances/commitments may not appear in YTD actuals;
(4) city budgets are routinely amended before year-end. Only year-end actuals vs. final amended budgets
determine true overruns. This caveat is repeated in flags.json and a-findings.md.

## Limitations

- No FY2024-dated check data; vendor history starts with FY2025 checks.
- The check register covers only Fifth Third checking disbursements; payroll (direct deposit/ACH), wires, and
  P-card detail are not visible, so check totals ($17.5M city-vendor FY2025) do not reconcile to GL expenditures
  ($26.7M headline) — the sources are complementary, not interchangeable.
- Property-tax pass-throughs (~$33–36M/yr to schools, county, ISD, community college) and transit-millage
  pass-throughs were excluded from vendor analysis as non-city spending; the Kent District Library contract
  ($1.05M) and wholesale water purchases from the Grand Rapids City Treasurer ($2.05M) were retained as vendors.
- Small GR City Treasurer payments (fees/permits) are mixed with large monthly water-purchase payments; the
  files do not separate them.
- Three GL accounts in fund 305 exist in the FY2024 GL extract but not in the chart of accounts (net $0).
- Transfer imbalance: transfers-out exceeded transfers-in by $136,000 (FY2024) and $100,000 (FY2025) because
  677-965-9950.07 "Trans to OPEB Trust Fund" has no matching 930 receipt in these extracts.
- The 6.30.24 fund-transfer report shows $1,965,045 on GL 101-965-9950.12 "Transfer to Pension Fund," but that
  GL number has no activity in the FY2024 GL extract and is not in the chart of accounts; the 731 fund books the
  same amount as 731-560-5390.01 "Monies Received From State."

## Parse log

- GL FY2024: 837 accounts, 39,235 journal lines parsed; 9,043 non-transaction rows skipped (headers, subtotals, blanks).
- GL FY2025: 818 accounts, 38,994 journal lines parsed; 9,076 non-transaction rows skipped.
- YTD file: 669 unique accounts parsed (each account block opens with a header row and closes with a totals row;
  only totals rows were taken), 11,666 transaction lines, 1,540 rows skipped.
- Check registers: footer total rows and bank header rows excluded by requiring a parseable check date;
  zero-amount/void rows excluded. Parsed totals match both report footers to the cent
  ($50,741,611.66 and $54,257,107.08).
- Vendor names normalized (uppercase, punctuation stripped, whitespace collapsed); top vendors checked manually —
  no name variants requiring merges were found.
- Unmapped accounts: 3 (fund 305, FY2024 only, net $0). All YTD accounts mapped.
