# raw/

Immutable sources. Add files; never edit or delete them.

## Expected on setup

| Path | What |
|---|---|
| `research/01-achilles-and-endurance-structure.md` | Research pass 1 (claude.ai, Sept 2026) |
| `research/02-gym-pool-review.md` | Research pass 2 (claude.ai, Sept 2026) |
| `history/chatgpt-coaching-2025-2026.md` | ChatGPT coaching conversation, Oct 2025 → Jul 2026 |
| `history/gym-log-to-2026-09.md` | Export of the Google Drive gym log, up to migration |
| `research/references.md` | Source-quality accounting for the two research passes — read first |
| `research/norwegian-method/` | Marius Bakken's articles + the Norwegian Singles guide, see its own README |

Strava is live via MCP and doesn't need exporting. The compiled multi-year view lives in
`wiki/strava-history.md` — derived, regenerated, never hand-edited.

## Status

**Landed:** the gym log (`history/gym-log-to-2026-09.md`), and the compiled Strava row data
(`history/strava-*.csv`, derived — regenerable from the Strava MCP, kept here so the numbers
in `wiki/strava-history.md` can be checked).

**Landed since:** the ChatGPT coaching conversation (`history/chatgpt-coaching-2025-2026.md`),
an excerpt covering 25 May – 30 Jul 2026. Jack's note says the conversation began Oct 2025;
that earlier portion is not in the excerpt.

**Landed 21 Sep 2026:** both research reports, plus `research/references.md` — the tool's own
accounting of which citations are independently checkable. **Read that file first.** Only 9
sources across both reports have a working link, and 4 of those are commercial or coaching
blogs; everything else was named (author, year, journal) without one and hasn't been
independently verified. The `[evidence: W/I/H]` grades in `wiki/references/` reflect the
research tool's own confidence, not outside appraisal — a caveat now stated on all three pages.

**Landed 21 Sep 2026:** the Norwegian Method material (Marius Bakken's four articles plus
the Norwegian Singles guide) — see `research/norwegian-method/README.md` for what's real and
what's anecdote, including a live dispute over Bakken's claimed influence on the Ingebrigtsen
system. Compiled to `wiki/references/evidence-norwegian-method.md`.

**Still pending:** nothing from the original SETUP.md list. Future sources land here the same
way.

This is a live exception to the rule in `CLAUDE.md` — *if you can't source a claim, don't write
it.* All four originally-expected files have now landed and were checked against the seeded
wiki pages; one real error was found and fixed (`training-model.md` §6's reactive-progression
gating had conflated two different pain thresholds) — see the `ingest` entry in `wiki/log.md`.

The compiled, tagged versions of the research live in `wiki/references/`. When they
disagree with the raw reports, the raw reports win.
