---
name: review-training
description: Log and review Jack's completed training — a single session, or a whole block (which includes a health check of the wiki). Use this whenever Jack reports a session he's done ("just finished Session A", "ran 10k", "gym done"), shares a Strava activity, tells you how something felt, reports Achilles symptoms, finishes a block, runs a test, or asks "how's it going?" or "am I improving?". Use it even when he mentions a session in passing.
---

# Review training

Two modes. Work out which one Jack wants.

---

## Mode 1 — Log and review a session

### Gather
- Strava (MCP) for the activity if it's a run or it's recorded there.
- The session plan, if one was made this conversation, and the active block.
- From Jack, only what isn't already known. Ask in **one** message:
  - RPE (1–10) and **enjoyment (1–5)**
  - Achilles: during (0–10); next-morning score can be added later
  - Anything done beyond the plan — and why

### Write the log entry
Append to `wiki/log.md`:

```
## [YYYY-MM-DD] gym | Session A — <block> wk<n> (<full|flat> gym)
- Planned: <one line>
- Done: <exercises × sets × reps @ load, or distance / time / pace / HR>
- Beyond plan: none | <what> — <why>
- RPE: x/10 · Enjoyment: x/5
- Achilles: during x/10 · next morning x/10 (or "pending")
- Capacity: <what he could do today that he couldn't recently, if anything>
- Review: <2–4 lines>
```

For a run, swap the header type to `run` and the Done line to running data.
When Jack later reports the next-morning Achilles score, edit that line in place.

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
Fill the Review section of the block file:
- Planned vs done: sessions, volume, adherence %
- Tests from `training-model.md` §12 vs last block — trend, not single numbers
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

## Always
- Ask about **capacity**, not only symptoms: "what can you comfortably do now that you
  couldn't a few weeks ago?"
- Keep it short. A session review is four lines, not a report.
