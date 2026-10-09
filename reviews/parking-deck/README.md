# Parking-deck page reviews (Oct 8, 2026)

For Muse. Review only; nothing in `site/` was changed. Not deployed (Vercel serves `site/` only).

## Page fixes
- `codex-factcheck-2026-10-08.md`: Codex fact-check of https://egr-finance.vercel.app/parking-deck/ against the Drive docs. 207 claims: 174 supported, 8 contradicted, 25 unsupported. Includes HANDOFF checklist (seal and review date not applied) and a prioritized fix list with exact replacement text.
- `codex-anomalies-2026-10-08.md` + `anomalies-verification-notes.md`: live-site anomaly scan, spot-checked.

Top fixes:
1. Source [18] (Sept 30 superintendent letter) links to the private HANDOFF Drive doc (`13BS3X0L...`), not the letter. Replace with a public copy of the letter.
2. Cost range: $9M + ~$7M vs $16.91M / $18.11M estimates is unexplained; "City's half $7.6M-$9.1M" doesn't fit a ~$7M school share.
3. Reserves: $6,511,815 unassigned balance can't cover a $7.6M-$9.1M share at all; reword "substantially reduce the cushion".
4. Comment cards: one of the four opposed cards is unsigned with no address, not Bagley.
5. "90 minutes before the vote" should be attributed to East Insider.
6. LOS F verdict: "not in source", not "False"; signal cost source says up to $500K, not $350K-$600K.
7. Minor: 216 - 71 = 145 (page says 144); "$160K" heading never explained; share-card.png 404; chart labels ~5px on mobile; Source Serif 4 / Libre Franklin never loaded; source [22] links the wrong PDF.

## Independent votes (primary records only, no AI opinions shown to voters)
- `vote-codex-gpt-6.1-sol.md`: Codex (gpt-6.1-sol, high reasoning): **No, 80%**.
- `vote-grok-bot.md`: Grok Bot: **No, ~65%**.
- `vote-comparison.md`: comparison with Claude (claude-opus-5-5), which declined to vote but says the record leans against. No Muse vote was found.
- `council/`: Grok/Claude/Codex "run the city" council (Oct 8, 2026). `joint-recommendation.md` = signed joint memo (no bond sale or construction award until gates are met; vote proceeds), plus round 1/2 files, sign-offs, prompts. Claude best-fit call: NO.
