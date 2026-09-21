# olavibot

Jack's personal training system, maintained with Claude Code. A durable all-round endurance
athlete, a 24-hour backyard ultra as the near target, a sub-3 marathon dormant until a race
is booked.

- `CLAUDE.md` — the schema and the rules. Loads every session
- `wiki/` — the living knowledge base. **Start at `wiki/index.md`**
- `raw/` — immutable sources. Add, never edit
- `.claude/skills/` — programme a session, plan training, review training

Three layers, after Karpathy's LLM-wiki pattern: immutable sources, a wiki Claude maintains,
and a schema the two of us change together.

**Every claim carries a provenance tag** — `[stated]`, `[data]`, `[evidence]` or `[inferred]`.
`[inferred]` is a hypothesis, not a fact, until Jack says otherwise. Corrected claims move to
the Refuted table in `wiki/observations.md` rather than disappearing. That rule is the point of
the repo: without it a self-maintaining wiki turns its own guesses into permanent facts.

See `SETUP.md` for what's still outstanding.

Private repo. Contains health information. Not medical advice.
