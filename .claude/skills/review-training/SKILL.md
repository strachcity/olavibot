---
name: review-training
description: Log and review Jack's completed training — a single session, or a whole block (which includes a health check of the wiki). Use this whenever Jack reports a session he's done ("just finished Session A", "ran 10k", "gym done"), shares a Strava activity, tells you how something felt, reports Achilles symptoms, finishes a block, runs a test, or asks "how's it going?" or "am I improving?". Use it even when he mentions a session in passing.
---

# Review training

Three modes. Work out which one Jack wants.

---

## Mode 1 — Log and review a session

### Gather
- Strava (MCP) for the activity if it's a run or it's recorded there. If Strava is down or the
  activity isn't there, log what Jack reports and mark the Done line `[stated]` rather than
  waiting for data.
- The session plan — made this conversation, in the pasted draft, or in the active block — and
  the active block.
- **Don't interrogate a standard run.** Jack won't answer an RPE/enjoyment/Achilles checklist
  per run, and asking anyway wastes his patience — `[stated, 2026-09-21]`. Log a run straight
  from Strava (distance, pace, duration, date). Omit `rpe`, `enjoyment`, `achilles_during` if
  he hasn't volunteered them — that's already what "omit what you don't have" below means, so
  stop short of asking. If he flags a concern (pain, missed the plan, something felt off), log
  that detail and follow up on it specifically — that's the exception, not the default.
- **Don't interrogate a gym session either** — same rule, `[stated, 2026-09-22]`. Gym still
  needs his own words (Strava doesn't capture exercises or loads), but take what he gives you
  in passing rather than running a fixed set of questions after it. Anything he doesn't
  volunteer: omit it from the yaml, write "not reported" on the prose line.
- **Sessions narrated in claude.ai are the normal workflow.** Jack runs the session while
  talking to Claude in the claude.ai project, reporting sets, reps, loads and on-the-fly swaps
  as he goes. That Claude drafts the log entry; Jack pastes it here because claude.ai has no
  write access to this repo. Treat the draft as `[stated]` and check it before appending:
  header format, metrics block holds only allowed values (numbers, listed words, `pending` —
  no prose), and the Strava activity matches. Fix format problems, flag content problems,
  then append and commit.

### Write the log entry
Append to `wiki/log.md`. Header, then the metrics block, then prose. The metrics block is what
makes block reviews arithmetic instead of impression — see `CLAUDE.md` for the field list.

**Gym:**

````
## [YYYY-MM-DD] gym | Session A — <block> wk<n> (<full|flat> gym)
```yaml
planned: yes          # yes | no | partial
rpe: 7
enjoyment: 4
achilles_during: 2
achilles_next_am: pending
beyond_plan: none     # none | short phrase, no commas
duration_min: 62
gym: full
session: A
reactive_level: 2
```
- Planned: <one line>
- Done: <exercises × sets × reps @ load>
- Beyond plan: none | <what> — <why>
- Capacity: <what he could do today that he couldn't recently, if anything>
- Review: <2–4 lines>
````

**Run:** same shape, header type `run`, and swap the last three yaml fields for `distance_km`,
`avg_pace` (m:ss) and `run_type` (easy | long | threshold | speed | strides | race). The Done
line carries distance / time / pace / HR.

- **Planned line keeps the plan's structure.** One line, but if the plan staged it (ramp-up
  then working sets, or similar), keep the stages distinct rather than collapsing them.
- **Equipment swaps** forced by the gym (flat gym, missing kit) count as planned: `planned:
  yes`, `beyond_plan: none`, the swap noted in the Done line. Beyond plan means *more*, not
  different.
- **`duration_min` is the session total** as the watch recorded it. If that includes something
  beyond the session (a walk after, watch not stopped), say so in the Review line.

`beyond_plan` appears twice on purpose: the short phrase in the block so it can be counted, the
*why* in the prose line because that's the part that's useful.

Fields you don't have, omit. Never guess a number into the block — an invented RPE becomes
`[data]` in a review three months later.

**The one permitted edit.** When Jack later reports the next-morning Achilles score, change
`achilles_next_am: pending` to the number, in place, in the existing entry. Append-only forbids
reordering, rewriting and deleting entries; resolving a field explicitly recorded as `pending`
is the exception. Anything else that turns out wrong gets a **new** entry referencing the old
one — don't quietly rewrite history.

### The review (2–4 lines)
Critical and useful, not cheerleading.
- Against the plan: did he stay under the ceiling? If not, name it plainly.
- Anything the data shows he didn't say (pace drifted into the grey zone, HR high for easy).
- One thing to carry into the next session.

### Observations
Only update `wiki/observations.md` if:
- Jack states something new and durable (`[stated]`), or
- A pattern has now appeared **three or more times** in the log (`[inferred]`, with the
  dates as evidence).
Never promote an `[inferred]` line to confirmed without Jack saying so.

Commit: `gym: …` or `run: …`.

---

## Mode 2 — Block review and lint

At the end of a block, or when Jack asks whether he's improving.

### Review the block

Count the metrics blocks in the log for the period rather than estimating from the prose —
estimating is how `[inferred]` ends up tagged `[data]`.

Fill the Review section of the block file:
- Planned vs done: sessions, volume, adherence %
- Tests: run the battery (Mode 3), then compare the new column in `wiki/tests.md` with the
  previous one — trend, not single numbers
- Enjoyment average and the lowest-scoring sessions — what made them bad?
- Beyond-plan count and what drove it
- Achilles trend across the block
- Each hypothesis the block was testing: confirmed, refuted, or still open
- What the next block should change

### Lint the wiki
Check and report, then fix what Jack agrees to:
- **Contradictions** between pages (e.g. `athlete.md` vs recent `[data]`)
- **Stale `[data]`** — numbers superseded by newer tests or the log
- **Untagged claims**
- **Old hypotheses** — `[inferred]` lines unconfirmed for more than a block: ask Jack, or
  design a test into the next block
- **Refuted claims creeping back** — check new text against the Refuted table
- **Model drift** — where what he actually does has diverged from `training-model.md`.
  Either the model is wrong or the behaviour is. Say which you think, and let Jack decide.

Changes to `training-model.md` need Jack's explicit agreement. Log them as `model` entries.

Set the block status to `reviewed`, append a `review` entry to the log, commit, then hand
over to `plan-training` for the next block.

---

---

## Mode 3 — Test day

End of a block, before planning the next. `wiki/tests.md` holds the protocols and results.
Run it the same way every time, record both sides, and note anything that would have affected
a result. Two results are gates, not information: seated calf raise ≥1× bodyweight (blocks
Reactive Level 4) and heel-raise symmetry ≥80–90%. If either fails, carry it into
`plan-training`.

Fill the new column in `wiki/tests.md`, append a `test` entry to the log, commit as `test: …`.
If baseline hasn't been done, this **is** the baseline — don't compare it to anything.

---

## Always
- Note **capacity**, not only symptoms, when he mentions it — what he can comfortably do now
  that he couldn't a few weeks ago. Don't ask; "not reported" is fine.
- Keep it short. A session review is four lines, not a report.
