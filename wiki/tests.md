# Tests

The battery from `training-model.md` §12. "Better all-round athlete" needs to be measurable or
it becomes a feeling.

Run at the **end of each block**, before planning the next one. Same protocol every time —
a test done differently is a new test, not a trend. Record both sides where the test has sides.

**Read the trend, not the number.** Single results move on sleep, caffeine, time of day and
how much you cared. Three points make a direction.

Two results are gates, not just information:

- **Seated calf raise vs bodyweight** — below 1.0× is a flagged calf-injury risk marker and
  blocks Reactive Level 4 (`training-model.md` §6) `[evidence: I]`
- **Limb symmetry on the heel raise** — target ≥80–90%; judge on work and height, not reps
  alone, because reps recover faster than work `[evidence: W]`

---

## Protocols

| Test | How, exactly |
|---|---|
| Aerobic | Easy run, fixed HR (state which), flat known route. Record pace. Same route each time |
| Threshold | 3 × 10min off 2min. Record pace and mean HR per rep |
| Speed | Parkrun or 5k time trial. Once or twice a block |
| Strength — squat | Estimated 1RM from a working set (Epley: `load × (1 + reps/30)`). Note solo or with trainer |
| Strength — deadlift | As above. Straps on, so grip isn't the cap |
| Calf — heel raise | Single leg, straight knee, to fatigue, metronome 2s up 2s down, full height off a step. Record reps **and** whether height held. Both sides |
| Calf — seated raise | Bent knee. Heaviest clean set. Record load as a multiple of bodyweight |
| Hip flexion | Hanging knee raise, max clean reps. Or knee-drive hold, time to failure. Pick one and keep it |
| Reactive | Single-leg hop for distance, best of 3, both sides |
| Balance | Single-leg stance, eyes closed, time to failure, both sides |
| Mobility | Ankle knee-to-wall in cm, both sides. Couch stretch — pass / partial / fail |
| Behaviour | Sessions over the ceiling. `scripts/log-metrics.py --since <block start>` gives the count |

Bodyweight on test day goes in the table too — the calf ratio depends on it.

---

## Results

One column per test date. Newest to the right.

| Test | Baseline (pending) |
|---|---|
| Date | — |
| Bodyweight (kg) | — |
| Aerobic — pace @ ___ bpm | — |
| Threshold — pace / HR | — |
| 5k | — |
| Squat e1RM (kg) | — |
| Deadlift e1RM (kg) | — |
| Heel raise L (reps / height held) | — |
| Heel raise R (reps / height held) | — |
| Heel raise symmetry (%) | — |
| Seated calf raise (× bodyweight) | — |
| Hip flexion | — |
| Hop L / R (cm) | — |
| Balance L / R (s) | — |
| Knee-to-wall L / R (cm) | — |
| Couch stretch | — |
| Over-ceiling sessions | — |

**Baseline not yet done** — `training-model.md` §13 open question. Until it is, every capacity
claim in the wiki is `[stated]` or `[inferred]`, never `[data]`. Run the battery over two
sessions in the first week of the first block rather than cramming it into one.

---

## Recording a test

Append a `test` entry to `wiki/log.md` with what was run and anything that affected it
(slept badly, tested late, calf still sore). Then fill the column here. The log says what
happened; this page carries the trend.

Test results are `[data]`. Give the date.
