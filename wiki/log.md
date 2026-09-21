# Log

Append-only. Newest at the bottom. Header format: `## [YYYY-MM-DD] type | title`

---

## [2026-09-21] model | Repo created
Migrated from claude.ai project "STRAVA x CLAUDE". Training model v1, athlete profile,
observations and three evidence references seeded from a conversation covering three years
of Strava data, the Drive gym log, the ChatGPT coaching history and two research passes.
Current state at migration [data]: ~19km/week over 3 runs, 1 gym session, restarting after
Sydney Marathon and the July Achilles flare. Phase A not yet formally started.

## [2026-09-21] model | Schema fixes before first use
Renamed fitness-brain → olavibot throughout. Eight changes to the schema, all reviewable as
one diff:

- **Log entries are now parseable.** `run`/`gym`/`rest` entries carry a fenced yaml metrics
  block. Block reviews asked for adherence %, enjoyment average and beyond-plan count, which
  free prose can't give without estimating — and an estimate tagged `[data]` is the exact
  failure this repo exists to prevent. `scripts/log-metrics.py` reads them.
- **`wiki/tests.md` added.** §12 defined ten tests with nowhere to record them. Protocols plus
  a results table. Baseline still pending.
- **`wiki/strava-history.md` added.** Five years of Strava is too expensive to re-derive per
  session, so the compiled view is filed. Derived, regenerated, never hand-edited. Structured
  to test the grey-zone hypothesis in observations.md.
- **§9 de-rotted.** "Currently ~19km/week" removed from training-model.md — current state
  belongs to the active block. Same for "Foundations (now → ~6 weeks)".
- **Append-only contradiction fixed.** review-training said to edit the next-morning Achilles
  score "in place" while the log claimed append-only. Now stated explicitly: resolving a
  `pending` field is the one permitted edit.
- **Reactive gates aligned to the evidence page.** Level 1–2 said <3/10; evidence-gym-pool.md
  says daily-life pain ≤2/10 admits him to reactive work, and ≤3/10 is the in-session hopping
  ceiling. Two different thresholds, now separated.
- **Strava fallback** added to all three skills — plan from the log and say the data is stale,
  rather than stalling.
- **Two operations added:** test day (review-training Mode 3) and "say where things stand".

Also promoted the undiagnosed Achilles to the top of §13. Mid-portion vs insertional changes
the loading prescription, and the whole calf plan assumes mid-portion on the strength of
`[stated]` symptom location.

No training decisions changed. `[data]`: none of the above is new information about Jack.

## [2026-09-21] model | Trimmed the schema back
Correction to the entry above: `scripts/log-metrics.py` has been removed. A 150-line script
to total a log with two entries in it was overbuilt — the LLM-wiki pattern is to keep only the
essentials and grow through use. Block reviews count the yaml metrics blocks directly; if that
becomes painful once there's a block's worth of entries, write the script then.

Also cut back: `wiki/tests.md` from a full protocol spec to the gates plus a results table
(protocol detail gets added as tests actually get run), and `review-training` Mode 3 from a
section to a paragraph. The yaml metrics block stays — retrofitting it across a few hundred
entries later is the expensive version.

## [2026-09-21] ingest | Gym log and seven years of Strava
Two sources landed. `raw/history/gym-log-to-2026-09.md` (from Gym_Log.docx) and the full
Strava record, compiled to `wiki/strava-history.md` with row data in `raw/history/`.

Strava covers **Aug 2019 → 21 Sep 2026**: 802 runs, 188 gym sessions. Seven years, not three.

Every race and PB in `athlete.md` reconciles exactly against Strava — Valencia 3:24:44,
Paris 3:27:04, Florence 3:13:20, Sydney 3:42:04, the three backyards, the 5k/10k/HM marks.
The Florence long-run ladder (24 → 30.6 → 26 → 34km) matches to the kilometre. An independent
check: Strava's own "bringing up 2k km for the year" note on 15 Dec 2024 against a computed
2024 total of 2076km.

Headline result — **the grey-zone hypothesis is confirmed and larger than estimated**. Share of
training time at 4:45–5:15/km: 26% (2023) → 28% (2024) → **56% (2025) → 54% (2026)**. But it
displaced quality, not easy running: hard work (<4:45) fell 35% → 10% across the same period
while easy (≥5:30) stayed flat at 16–21%. See `strava-history.md`.

Contradictions found against `athlete.md` and `observations.md` are **flagged, not resolved** —
awaiting Jack. Listed in the handover for this session; nothing in those pages edited yet.
