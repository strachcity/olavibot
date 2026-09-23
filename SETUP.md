# Setup

Where this repo is, and what's left to do before it's actually running.

## Done

- Repo created, scaffold committed, everything named `olavibot`
- **Strava MCP connected**, and the full seven-year record compiled to `wiki/strava-history.md`
- Gym log ingested to `raw/history/`
- Wiki seeded: training model, athlete profile, observations, three evidence references
- `wiki/tests.md` created, awaiting baseline

## Not done — in order

### 1. Land the remaining raw sources

`raw/` is empty, but the seeded wiki already cites it. Until these arrive, every `[evidence]`
and `[data: gym log]` tag in the wiki is unverifiable — see `raw/README.md`.

| Put here | What | Status |
|---|---|---|
| `raw/research/01-achilles-and-endurance-structure.md` | Research pass 1 | **landed 21 Sep** |
| `raw/research/02-gym-pool-review.md` | Research pass 2 | **landed 21 Sep** |
| `raw/research/references.md` | Source-quality accounting | **landed 21 Sep** |
| `raw/history/chatgpt-coaching-2025-2026.md` | ChatGPT coaching conversation | **landed 21 Sep** (May–Jul 2026 excerpt) |
| `raw/history/gym-log-to-2026-09.md` | Google Drive gym log export | **landed 21 Sep** |

Also worth exporting: the claude.ai conversation the wiki was actually seeded from. It's the
real source for a lot of what's in `athlete.md`, and it isn't in `raw/`.

### 2. Resolve the flagged contradictions

The Strava compile and the gym log ingest threw up contradictions with `athlete.md` and
`observations.md`. They are flagged and **not resolved** — see the `ingest` entry in
`wiki/log.md`. Jack decides each one; then those pages get updated and the grey-zone line in
`observations.md` gets promoted from `[inferred]` to `[data]` or rewritten.

### 3. Ingest the remaining `raw/` files, one at a time

Per `CLAUDE.md`: read it, give the takeaways, then edit. Not the other way round.

The ChatGPT history needs care against the Refuted table — one refuted claim ("he's never done
a classic marathon block") came from there originally.

### 4. Baseline tests

`wiki/tests.md`, over two sessions in one week. Nothing in the wiki can be tagged `[data]` for
capacity until this exists, and the Reactive gate for Level 4 needs a real seated calf raise
number.

### 5. Plan Phase A

Use `plan-training`. Foundations, 4–6 weeks. Don't write the block file until it's agreed.

---

## The open question worth handling outside this repo

The Achilles has been symptomatic 9+ months and has never been formally diagnosed. Mid-portion
and insertional take different loading, and the whole calf plan assumes mid-portion. See
`training-model.md` §13. Worth an in-person assessment; it isn't something this repo can settle.

Not medical advice. If symptoms go beyond the rules in §7, see a physio.
