# East Grand Rapids City Spending — data & site

Resident-friendly analysis of City of East Grand Rapids finances, built from FOIA financial records.

## What's here

- `raw/` — the FOIA records from the City Clerk (June 15, 2026), converted from the
  original spreadsheets to clean CSVs (report headers/footers removed, data tables only —
  no desktop software needed to open them): GL transaction detail, YTD budget-vs-actual,
  check registers, fund transfers, chart of accounts.
- `analysis/` — normalized analysis: spending by category (FY24/FY25 actuals, FY26 budget/YTD),
  vendor rankings, budget flags, capital projects, millage breakdown, methodology, sources.
- `site/` — the public-facing website (`index.html`), built from the verified analysis.

## Key verified figures

- FY2025 total city spending: **$26,702,474** (all governmental funds + Water & Sewer enterprise +
  Motor Equipment Revolving Fund, excluding interfund transfers). Governmental-funds portion
  matches the audited ACFR within $6.
- FY2024 → FY2025 change: **−3.1%**.
- Fiscal year: July 1 – June 30.

## Parking proposal

Shown separately on the site: proposed parking-facility bond/millage is **on the ballot
November 3, 2026 — not approved**. First-year rate 0.5922 mills; dollar figures are derived
arithmetically from that rate, not official city figures.

## Data notes

- Check-register files are mislabeled by one fiscal year in their filenames; figures in the
  analysis are labeled by actual check dates. No FY2024-dated check data exists.
- ~$33M/yr of register dollars are property-tax pass-throughs (schools, county, ISD, GRCC),
  excluded from vendor analysis. Payroll (ACH/wires) is not in the check registers.
- See `analysis/methodology.md` for full methodology and limitations.
