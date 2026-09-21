# Setup

1. Put these files in `raw/` (see `raw/README.md` for names):
   - both research reports from the claude.ai project → `raw/research/`
   - the ChatGPT coaching conversation → `raw/history/`
   - the Google Drive gym log, downloaded as Markdown or plain text → `raw/history/`
2. Open Claude Code in this folder and paste the prompt below.

---

Read CLAUDE.md and wiki/index.md first.

1. Initialise git, create a **private** GitHub repo called `fitness-brain`, and push.
2. Check whether the Strava MCP is connected here. If not, tell me how to add it and stop
   until it is.
3. Ingest the files in `raw/` one at a time, following CLAUDE.md. For each, tell me the
   takeaways and what it changes in the wiki before editing. Pay particular attention to
   the gym log: check `wiki/athlete.md` strength numbers against it, and flag any
   contradictions rather than resolving them yourself.
4. Once ingested, use `plan-training` to propose the first block (Phase A, Foundations).
   Don't write the block file until I've agreed it.
