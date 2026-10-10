# Gaslight Village future plan (Oct 2026)

A pedestrian-first, car-light plan for Gaslight Village and the surrounding area in East Grand Rapids, phased from today to 2040+. Start with **FUTURE-PLAN.md**.

## Process
1. **Maps** (`maps/`): accurate maps rendered programmatically from OpenStreetMap (Overpass API, matplotlib). No AI imagery was used for maps. Orientation was checked against a Google Maps screenshot. Downloaded public City and USGS maps are in `maps/public/`, with source URLs in `maps/SOURCES.md`.
2. **Round 1, independent planners** (`round1/planner-*.md`). Each got the same compact context packet (`prompts/context-packet.md`), with no access to the others, and an ~800-word cap.
   | File | Lens | Model |
   |---|---|---|
   | planner-grok.md | generalist | Grok Bot |
   | planner-claude.md | generalist | Claude Code, claude-opus-5-5 |
   | planner-codex.md | generalist | Codex CLI, gpt-6.1-sol (high) |
   | planner-futurist.md | transit and autonomous-mobility futurist | Codex CLI, gpt-6.1-sol (high) |
   | planner-urbanist.md | Dutch/Japanese walk and bike urbanist | Claude Code, claude-opus-5-5 |
   | planner-realist.md | municipal-finance and political realist | Codex CLI, gpt-6.1-sol (high) |
3. **Collaborative build-on round** (`collab/collab-*.md`, ~400 words each). Each planner read the other five and proposed how to combine the best ideas and fill the gaps. This was not a critique round.
4. **Synthesis.** Grok Bot wrote `FUTURE-PLAN.md`.
5. **"Yes, and" pass** (`synthesis-addenda/yesand-*.md`, ~200 words each). Each external planner refined the shared plan once. Highlights were folded into FUTURE-PLAN.md.
6. **Concept overlays** (`maps/04–07-concept-*.png`). These are schematic and drawn on the real OSM base.

All prompts are in `prompts/`. Each model was called once per round, with no retries.
