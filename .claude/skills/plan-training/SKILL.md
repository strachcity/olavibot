---
name: plan-training
description: Plan Jack's training week or a 4–6 week training block — running shape, gym sessions and exercise selection, rotations, ceilings and triggers — and write the agreed plan to the wiki. Use this whenever Jack asks to plan the week, plan the next block, start a new phase, or when something changes the plan: a marathon or backyard ultra gets booked, he's travelling, work gets heavy, he's missed a week, an injury flares, or a block has just been reviewed. Also use it when he asks "what should the next few weeks look like?".
---

# Plan training

Two sizes: a **week** (day by day) and a **block** (4–6 weeks). The block is the unit the
model is built around; weeks are drawn from it.

## 1. Gather

1. `wiki/training-model.md` — all of it for a block; §4–§7 for a week.
2. `wiki/athlete.md` and `wiki/observations.md` — especially open hypotheses.
3. The previous block file in `wiki/blocks/`, including its review.
4. `wiki/log.md` since that block started.
5. Strava (MCP): last 4–6 weeks — actual weekly volume, run count, longest run, pace spread.
   For the multi-year view use `wiki/strava-history.md` rather than re-deriving it; refresh
   that page if it's stale. **If Strava is unavailable**, plan from the log and say so.
6. `wiki/tests.md` — the latest column. It sets the Reactive level he's actually cleared for.
7. `wiki/references/` only where a decision needs evidence.

## 2. Establish the entry state

Write it down, tagged: weekly volume, runs per week, gym sessions per week, Achilles trend,
current Reactive level, latest test results. Plan from what he's **actually doing**, not from
the previous plan.

The entry state belongs in the block file — never write it back into `training-model.md`,
which holds the shape of a phase, not where he is in it.

## 3. Draft the block

Use the template in `wiki/blocks/README.md`. Decide, with a reason for each:

- **Phase** (§9) and **emphasis** — one sentence.
- **Running:** every run in the week gets its own distance and pace, not a weekly total.
  Name what differs between them (which is the long one, which carries strides, why). Use
  the pace bands in `training-model.md` §4 (easy: 5:30–6:00/km or slower). Progress one
  variable only.
- **Gym:** for Session A and B, fill every slot from the pools in §6. Pick a genuinely
  different selection from the last block for the accessories. Keep anchors. Allow one new
  lift if there's appetite. Set the Tier 2 fortnightly rotation.
- **Reactive:** the level he's cleared for **per `wiki/tests.md`**, and the condition for
  moving up. Don't clear Level 4 without a seated calf raise ≥1× bodyweight on record.
- **Ceilings** for key sessions.
- **1–2 hypotheses** from `observations.md` this block will test, and how.
- **Triggers** that change the plan.

## 4. Check it before showing it

- Does every capacity appear on its weekly or fortnightly rhythm?
- Is only one variable rising?
- Would this feel good to do? If the honest answer is "it's a grind", change it.
- Does it fit a busy work week? Name the maintenance-floor version.
- Is any current-state number in here copied from the last block rather than from the log?

## 5. Agree, then write

Show Jack the plan concisely. Accept his changes. **Only then** write
`wiki/blocks/YYYY-MM-name.md` with status `active`, set the previous block to `reviewed`,
update `wiki/index.md`, append a `block` entry to `wiki/log.md`, and commit.

## Weekly plans

Day-by-day table: day, session. Ask about the week's known constraints first (busy evenings,
travel) — they decide day placement more than anything else. Fit sessions around them; heavy
legs away from hard runs; note any back-to-back running days that fall out of a constraint
rather than being deliberate.

Write it into the active block file under `## Weekly schedule`, **below** the previous
weeks' tables — never replace or delete a past week, and don't edit one afterwards to match
what happened (that's `log.md`'s job; plan + log together show what was missed). Keep the
format the dashboard reads: a `**Week <n> (<dates>).** Constraint: …` line, then a
`| Day | Session |` table with days as `Mon 21`. Commit as a `block` entry. A run can split around a gym
session or lengthen over the block — log each leg as its own entry, same date; no format
change needed for that.

## Race mode

If a **marathon** is booked: race mode (§10) temporarily renegotiates the enjoyment
constraint. Ask Jack explicitly whether he agrees before planning it. Check the entry
condition (tolerating base volume pain-free). If not met, say so and propose running it as
a day out.

If a **backyard** date is set: count back 12 weeks to Phase C and say what has to be true
by then.
