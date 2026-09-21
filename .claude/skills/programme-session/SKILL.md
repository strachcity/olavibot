---
name: programme-session
description: Plan a single training session for Jack — a gym session, a run, or both — grounded in his training model, his current block and what he's actually done recently. Use this whenever Jack asks what to do today, wants a gym session or a run, says which gym he's at or how much time he has, asks for "session A" or "session B", wants a threshold or long run, or is deciding whether to train at all today. Use it even for quick asks like "45 mins at the flat gym?" or "easy run tonight?".
---

# Programme a session

One session, planned so it fits the model, the block, and the last fortnight.

## 1. Gather context (in this order)

1. `wiki/training-model.md` — §4 principles, §5 base week, §6 gym, §7 Achilles, §8 warm-up.
2. The **active block** in `wiki/blocks/` (status `active`). It decides which pool exercises
   fill each slot. If there's no active block, plan from the current phase in §9, and say
   that a block should be planned soon.
3. Recent history: `grep "^## \[" wiki/log.md | tail -14`, then read the last few gym and
   run entries in full. Check the **Tier 2 fortnightly rotation** — what was done last week.
4. Strava (MCP): the last 7–10 days of activities, for actual running load. **If Strava is
   unavailable**, plan from the log instead — say the running data is stale, give the date of
   the last entry you trusted, and be more conservative than usual with volume.

## 2. Know three things before planning

- **Which gym** (full or flat) — or that it's a run
- **Time available**
- **How the Achilles felt on first steps this morning** (0–10)

If any are missing, ask for them in one short message. If Jack wants the session now,
state your assumptions and plan anyway.

## 3. Decide

Run these checks. If one fails, change the session and say why in a line.

- **Achilles:** morning score up two days running → no reactive work, no quality run, keep
  calf work, hold volume.
- **Spacing:** heavy legs ≥6h from hard running, and reactive/heavy calf work 48–72h from
  the last hard run.
- **One variable:** if volume went up this fortnight, intensity doesn't.
- **Variation:** use the block's chosen exercises. Don't import exercises from outside the
  block mid-block, and don't repeat the exact same session twice in a row if the block
  allows alternatives.
- **Balance:** Tier 1 every week; Tier 2 on its fortnightly rotation; Tier 3 in the warm-up.

## 4. Output

Short intro line (which session, which gym, why this one today). Then a table.

**Gym:**

| Block | Exercise | Sets × reps | Load / effort | Notes |
|---|---|---|---|---|
| Warm-up | … | | | incl. foot/ankle, low pogos if cleared |
| Reactive | … | contacts | | Session B, only at the earned level |
| Anchor | Squat / Deadlift | | % or RPE | straight sets |
| Superset 1 | … + … | | | |
| … | | | | |
| Cool-down | … | | | stretching here, not before |

**Run:**

| Part | What | Distance | Pace | Ceiling |
|---|---|---|---|---|
| Warm-up | 5 min easy + drills (quality days) | | | |
| Main | … | km | pace / HR / RPE | stop at … |
| Strides | 4–6 × 20s (if planned) | | relaxed-fast | |
| Cool-down | … | | | |

Always give a distance, even a range, for the main part — never just "easy run".

Then always, in two lines:
- **Ceiling:** the point at which he stops, even if it's going well.
- **If it feels great:** the one pre-agreed extra (strides, one accessory set, 5 easy min).
  Never more pace, never more anchor load.

## Rules

- Don't write to the wiki. The session gets logged afterwards by `review-training`.
- Loads come from the log, not guesses. If there's no recent number for a lift, prescribe by
  RPE and say so.
- Reactive work is gated on `wiki/tests.md`, not on how he feels. Level 4 needs a seated calf
  raise ≥1× bodyweight on record. No result on record means not cleared.
- A new movement gets a conservative load and a one-line technique cue.
- Evidence questions → cite `wiki/references/` with the grade. Don't pad sessions with it.
