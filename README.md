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

## Logging gym sessions from claude.ai

The normal workflow: run the session while talking to Claude in the claude.ai project, then
paste the drafted log entry into Claude Code here to commit. Claude Code picks up
`.claude/skills/` automatically. claude.ai doesn't — install the skills there by hand.

Skills needed:
- `programme-session` — plans the session (with the Why column)
- `review-training` — drafts the log entry in the right format

Install:
1. Zip each skill folder, keeping the folder at the top of the zip:
   `cd .claude/skills && zip -r review-training.zip review-training && zip -r programme-session.zip programme-session`
2. claude.ai → Settings → Capabilities → turn on code execution if it's off, then
   **Skills → Upload skill** and upload each zip.
3. In the claude.ai project, add `wiki/training-model.md`, `wiki/log.md` and the active block
   in `wiki/blocks/` to project knowledge — the skills read them, and claude.ai can't see this
   repo.

When a skill changes here, re-zip and re-upload it. Refresh the project knowledge files when
the block or model changes, and `log.md` every so often so recent loads are current.

Private repo. Contains health information. Not medical advice.
