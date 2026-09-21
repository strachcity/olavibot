# Strava history (compiled)

**Derived, not raw. Regenerate this page; never hand-edit it.**

`CLAUDE.md` says don't copy Strava into the wiki, because it's re-queryable. That holds for
recent activity. It doesn't hold for the multi-year picture: re-deriving five years of pace
distribution every time a question touches it is slow and gives slightly different answers
each time. So the long view is compiled here once and refreshed deliberately.

Everything on this page is `[data]` with its range. If it disagrees with Strava, Strava wins —
regenerate.

- **Source:** Strava MCP, athlete history to the refresh date below
- **Last refreshed:** not yet compiled
- **Covers:** —

---

## Why this page exists

It isn't a numbers dump. It's built to answer the questions the wiki currently can't, and each
section names the claim it tests.

| Section | Tests |
|---|---|
| Volume by year and quarter | "~19km/wk at migration", the 30–50km/wk 2025–26 range `[data]` |
| Pace distribution by year | **The grey-zone hypothesis** — `observations.md` `[inferred]` |
| Long-run progression | Florence's 24 → 30.6 → 26 → 34km build `[data]` |
| Gaps and layoffs | Injury dates in `athlete.md`, and what preceded them |
| Single-session spikes | Runs far longer than the recent longest — the risk factor that has evidence behind it `[evidence: W]` |
| Build periods | Valencia / Florence / backyard builds, as actually run rather than as remembered |

The grey-zone line is the important one. `observations.md` carries *"Grey-zone running
(4:45–5:15/km) is what capped volume in 2025–26"* as `[inferred]`. Five years of pace
distribution either promotes it to `[data]` or refutes it. Don't promote it by hand — the
distribution has to show it, and Jack has to confirm.

---

## Volume

*Pending first compile.*

| Year | Runs | km | Hours | Longest run | Notes |
|---|---|---|---|---|---|

## Pace distribution

Share of running **time** in each band, per year. Bands chosen to match the model's
definitions (§4: easy is 5:30–6:00/km or slower; the grey zone is 4:45–5:15/km).

*Pending first compile.*

| Year | ≥6:00 | 5:30–6:00 | 5:15–5:30 | **4:45–5:15 (grey)** | 4:15–4:45 | <4:15 |
|---|---|---|---|---|---|---|

## Long runs

*Pending first compile.*

## Gaps, layoffs and spikes

*Pending first compile.*

| Period | Gap length | What preceded it | What followed |
|---|---|---|---|

## Build periods

*Pending first compile.*

---

## How to regenerate

1. Pull activities with the Strava MCP across the full range. Page through it; don't assume
   one call covers five years.
2. Compute the tables above. **Distribution is by time, not by run count** — a 90-minute easy
   run and a 20-minute tempo are not one-all.
3. Rewrite this page whole. Update *Last refreshed* and *Covers*.
4. Check every affected claim: `athlete.md` training history, the `[inferred]` lines in
   `observations.md`, the entry state of the active block. Flag contradictions, resolve none
   of them alone.
5. Append an `ingest` entry to `wiki/log.md` and commit.

Refresh at block reviews, or when a question genuinely needs the long view. Not every session.

**Caveats to carry.** GPS pace is noisy on trails and in cities. Moving time understates
stopped time on backyard laps. Gym sessions recorded as Strava activities aren't runs —
exclude them from volume. An empty week may mean injury, travel or a dead watch; don't read
intent into a gap without asking.
