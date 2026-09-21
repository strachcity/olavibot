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
