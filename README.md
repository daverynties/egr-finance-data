# East Grand Rapids City Finance Data

Public-records financial data for the City of East Grand Rapids, Michigan, plus the
public explainer site built from it.

**Live site:** https://egr-finance.vercel.app

## What's here

```
├── raw/          FOIA financial data (CSVs) — not published to the site
├── analysis/     Cleaned datasets (JSON) + methodology notes
└── site/         Public site — index.html ONLY (what Vercel deploys)
```

**Important:** Vercel builds *only* from `site/index.html`. Never put `raw/` or
`analysis/` inside `site/` — anything there may become public.

## Data sources

- **FOIA response** (June 2026) from the East Grand Rapids City Clerk: general-ledger
  extracts, check registers, budget detail, payroll journals (FY2023–FY2026 YTD).
- **City of East Grand Rapids FY2024 ACFR** (audited) — debt, pension, OPEB figures.
- **Adopted FY2025–26 city budget** — budget comparisons.
- **Michigan Dept. of Treasury F-65 data** — six-city peer comparison (FY2024 audited).
- **East Grand Rapids Public Schools** finance page — school district budget context.
- **Kent County / City of EGR ballot records** — November 3, 2026 millage/bond details.

## Key verified figures

| Item | Figure |
|---|---|
| FY2025 city spending | $26,702,474 (−3.1% vs FY2024; within $6 of audited ACFR) |
| FY2025 operating revenue | ~$30.8M |
| FY2025 payroll | $9.03M (34% of spending) |
| FY2024 governmental debt | $9,746,938 ($857/resident) |
| FY2024 net pension liability | $8,474,514 (59.2% funded) |
| FY2024 OPEB liability | $2,532,173 |
| EGRPS 2025–26 budget | ~$42.4M expenses |

See `analysis/` for methodology and per-figure verification notes.

## Deploying

The site is a single static `site/index.html`. Push to `main` → Vercel auto-deploys.

**Commit identity matters:** Vercel rejects deployments from unrecognized author emails.
All commits must use:

```
David A. Rynties <ryntiesd@mail.gvsu.edu>
```

Never commit as `muse@local` or any other identity.

## License / use

Data is from public records. The analysis and site are an independent resident project,
not affiliated with the City of East Grand Rapids, Kent County, or any campaign.
