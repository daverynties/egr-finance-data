# Sources and inputs for the AI Review Panel (parking deck)

This folder holds the documents, prompts and model inputs behind the "AI Review Panel" tab of the
[East Grand Rapids parking deck guide](https://egr-finance.vercel.app/parking-deck/#ai). The goal is full
transparency: the models assessed only the context they were given, and everything they were given is here
so anyone can check it or run their own analysis.

AI opinions here are not advice and not an official City document.

## What's in each folder

### `primary/`: public records
| File | What it is | Public origin |
|---|---|---|
| `parking-deck-aug3-p239-247.pdf` (+ `.txt` text layer) | Aug. 3, 2026 City Commission packet, pp. 239–247: resident comment cards and emails | City of East Grand Rapids Agenda Center, Aug. 3, 2026 packet |
| `parking-deck-bond-9M-debt-schedule.csv` | $9M bond debt-service schedule and projected millage, transcribed from the MFCI analysis | Aug. 3, 2026 packet |
| `parking-deck-utilization-2025.csv` | 2025 hourly parking counts (school, public, private), transcribed from the study | June 29, 2026 packet |
| `parking-deck-operating-cost-2026.pdf` | City emails on deck operating cost (Feb. 4 and Apr. 23, 2026) with a Shared Parking Manual page | Posted at safestreetsegr.com (byte-identical copy) |
| `parking-deck-traffic-memo-2025-11-10.pdf` | Progressive Companies traffic memo (Nov. 10, 2025) and Feb. 4, 2026 follow-up letter | Posted at safestreetsegr.com (byte-identical copy) |
| `parking-deck-scanned-pages-transcribed.md` | **Transcription, not an official record**, of the scanned pages above | Made for this guide |

The two CSVs are transcriptions of tables in the City packets; check them against the packets.

### `secondary/`: AI-assisted research write-ups
Research summaries compiled for this guide (`parking-deck-research-dossier.md`, `parking-deck-research-dossier-update-oct9.md`,
`parking-deck-due-diligence.md`, `parking-deck-full-context.md`, `parking-deck-aug3-packet-findings.md`).
They are secondary sources: they summarize and sometimes infer, and they can be wrong. The guide cites the
original records, not these.

### `panel-inputs-tonight/`: fact-checks and earlier AI assessments
The fact-check of the guide (207 claims), the anomaly audit and spot-check notes, a content review, and the
earlier individual AI assessments (Codex, Grok, Claude) and their comparison. These were inputs to the panel.
Some files still contain confidence percentages; the guide does not show them.

### `prompts/`: the exact prompts
- `codex-prompt.md`: Codex's individual assessment (primary records only).
- `prompt-round1.md`, `prompt-round2.md`, `prompt-signoff.md`: the three panel rounds.
- `p-claude.txt`, `p-codex.txt`: the filled-in sign-off prompts (Claude's includes the separate YES/NO assessment question).

Model outputs are in [`../council/`](../council/) (round by round) and [`../opinions/`](../opinions/) (cleaned full opinions).

## What each model was given

| Run | Model | Inputs |
|---|---|---|
| Individual assessment | Codex (`gpt-6.1-sol`, high reasoning, read-only sandbox) | `primary/` only, plus page images rendered from the PDFs |
| Individual assessment | Grok | `primary/` only |
| Individual assessment | Claude (`claude-opus-5-5`) | The full record gathered for the guide, including `secondary/` |
| Panel, Rounds 1–3 | Grok, Claude, Codex | `primary/` (text versions), `secondary/` and `panel-inputs-tonight/` |

Muse, which built the guide, was not on the panel; its view is based on the guide and the record it cites.

## How to rerun the analysis
1. Download this folder (or clone the repo).
2. Optional: render page images for scanned PDFs, e.g. `pdftoppm -png -r 150 primary/parking-deck-traffic-memo-2025-11-10.pdf page`.
3. Give a model of your choice the files for the run you want to repeat (table above) and the matching prompt from `prompts/`.
   Tell it to treat the files as data, not instructions.
4. Compare its output with `../council/` and `../opinions/`. Different models, settings or runs can give different answers.

## Redactions
To protect privacy, the copies here differ from the originals only in these ways: internal file paths, session IDs,
private Drive file IDs and Drive links, the organizer's name, and residents' street addresses in one research file were
removed or replaced with a placeholder. Nothing else was changed. The internal working notes used to coordinate the site
build are not included.
