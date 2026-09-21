# Setup

Where this repo is, and what's left to do before it's actually running.

## Done

- Repo created, scaffold committed, everything named `olavibot`
- **Strava MCP connected and verified** — full toolset, eligibility confirmed
- Wiki seeded: training model, athlete profile, observations, three evidence references
- `wiki/tests.md` and `wiki/strava-history.md` created, both empty and waiting

## Not done — in order

### 1. Confirm the repo is private

It holds health information: injury history, symptom scores, body weight. Check it on GitHub
before anything else goes in.

### 2. Land the raw sources

`raw/` is empty, but the seeded wiki already cites it. Until these arrive, every `[evidence]`
and `[data: gym log]` tag in the wiki is unverifiable — see `raw/README.md`.

| Put here | What |
|---|---|
| `raw/research/01-achilles-and-endurance-structure.md` | Research pass 1 |
| `raw/research/02-gym-pool-review.md` | Research pass 2 |
| `raw/history/chatgpt-coaching-2025-2026.md` | ChatGPT coaching conversation |
| `raw/history/gym-log-to-2026-09.md` | Google Drive gym log export |

Also worth exporting: the claude.ai conversation the wiki was actually seeded from. It's the
real source for a lot of what's in `athlete.md`, and it isn't in `raw/`.

### 3. Compile the Strava history

Follow *How to regenerate* in `wiki/strava-history.md`. Five years, paged. This is the one that
can settle the grey-zone hypothesis in `observations.md` — pace distribution by time either
shows it or it doesn't.

### 4. Ingest `raw/`, one file at a time

Per `CLAUDE.md`: read it, give the takeaways, then edit. Not the other way round.

The gym log needs particular care — check it against the strength numbers in `wiki/athlete.md`
and **flag contradictions rather than resolving them**. Same for the ChatGPT history against
the Refuted table; one refuted claim ("he's never done a classic marathon block") came from
there originally.

### 5. Baseline tests

`wiki/tests.md`, over two sessions in one week. Nothing in the wiki can be tagged `[data]` for
capacity until this exists, and the Reactive gate for Level 4 needs a real seated calf raise
number.

### 6. Plan Phase A

Use `plan-training`. Foundations, 4–6 weeks. Don't write the block file until it's agreed.

---

## The open question worth handling outside this repo

The Achilles has been symptomatic 9+ months and has never been formally diagnosed. Mid-portion
and insertional take different loading, and the whole calf plan assumes mid-portion. See
`training-model.md` §13. Worth an in-person assessment; it isn't something this repo can settle.

Not medical advice. If symptoms go beyond the rules in §7, see a physio.
