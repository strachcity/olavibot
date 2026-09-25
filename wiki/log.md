# Log

Append-only. Newest at the bottom. Header format: `## [YYYY-MM-DD] type | title`

---

## [2026-09-21] model | Repo created
Migrated from claude.ai project "STRAVA x CLAUDE". Training model v1, athlete profile,
observations and three evidence references seeded from a conversation covering three years
of Strava data, the Drive gym log, the ChatGPT coaching history and two research passes.
Current state at migration [data]: ~19km/week over 3 runs, 1 gym session, restarting after
Sydney Marathon and the July Achilles flare. Phase A not yet formally started.

## [2026-09-21] model | Schema fixes before first use
Renamed fitness-brain → olavibot throughout. Eight changes to the schema, all reviewable as
one diff:

- **Log entries are now parseable.** `run`/`gym`/`rest` entries carry a fenced yaml metrics
  block. Block reviews asked for adherence %, enjoyment average and beyond-plan count, which
  free prose can't give without estimating — and an estimate tagged `[data]` is the exact
  failure this repo exists to prevent. `scripts/log-metrics.py` reads them.
- **`wiki/tests.md` added.** §12 defined ten tests with nowhere to record them. Protocols plus
  a results table. Baseline still pending.
- **`wiki/strava-history.md` added.** Five years of Strava is too expensive to re-derive per
  session, so the compiled view is filed. Derived, regenerated, never hand-edited. Structured
  to test the grey-zone hypothesis in observations.md.
- **§9 de-rotted.** "Currently ~19km/week" removed from training-model.md — current state
  belongs to the active block. Same for "Foundations (now → ~6 weeks)".
- **Append-only contradiction fixed.** review-training said to edit the next-morning Achilles
  score "in place" while the log claimed append-only. Now stated explicitly: resolving a
  `pending` field is the one permitted edit.
- **Reactive gates aligned to the evidence page.** Level 1–2 said <3/10; evidence-gym-pool.md
  says daily-life pain ≤2/10 admits him to reactive work, and ≤3/10 is the in-session hopping
  ceiling. Two different thresholds, now separated.
- **Strava fallback** added to all three skills — plan from the log and say the data is stale,
  rather than stalling.
- **Two operations added:** test day (review-training Mode 3) and "say where things stand".

Also promoted the undiagnosed Achilles to the top of §13. Mid-portion vs insertional changes
the loading prescription, and the whole calf plan assumes mid-portion on the strength of
`[stated]` symptom location.

No training decisions changed. `[data]`: none of the above is new information about Jack.

## [2026-09-21] model | Trimmed the schema back
Correction to the entry above: `scripts/log-metrics.py` has been removed. A 150-line script
to total a log with two entries in it was overbuilt — the LLM-wiki pattern is to keep only the
essentials and grow through use. Block reviews count the yaml metrics blocks directly; if that
becomes painful once there's a block's worth of entries, write the script then.

Also cut back: `wiki/tests.md` from a full protocol spec to the gates plus a results table
(protocol detail gets added as tests actually get run), and `review-training` Mode 3 from a
section to a paragraph. The yaml metrics block stays — retrofitting it across a few hundred
entries later is the expensive version.

## [2026-09-21] ingest | Gym log and seven years of Strava
Two sources landed. `raw/history/gym-log-to-2026-09.md` (from Gym_Log.docx) and the full
Strava record, compiled to `wiki/strava-history.md` with row data in `raw/history/`.

Strava covers **Aug 2019 → 21 Sep 2026**: 802 runs, 188 gym sessions. Seven years, not three.

Every race and PB in `athlete.md` reconciles exactly against Strava — Valencia 3:24:44,
Paris 3:27:04, Florence 3:13:20, Sydney 3:42:04, the three backyards, the 5k/10k/HM marks.
The Florence long-run ladder (24 → 30.6 → 26 → 34km) matches to the kilometre. An independent
check: Strava's own "bringing up 2k km for the year" note on 15 Dec 2024 against a computed
2024 total of 2076km.

Headline result — **the grey-zone hypothesis is confirmed and larger than estimated**. Share of
training time at 4:45–5:15/km: 26% (2023) → 28% (2024) → **56% (2025) → 54% (2026)**. But it
displaced quality, not easy running: hard work (<4:45) fell 35% → 10% across the same period
while easy (≥5:30) stayed flat at 16–21%. See `strava-history.md`.

Contradictions found against `athlete.md` and `observations.md` are **flagged, not resolved** —
awaiting Jack. Listed in the handover for this session; nothing in those pages edited yet.

## [2026-09-21] model | Six contradictions worked through with Jack
Resolved one at a time. Three of my six flags were wrong — my error, not the wiki's — from
comparing the wrong time windows. Recorded here so the mistakes don't get re-made.

1. **Run frequency — no contradiction.** I compared an 8-week average against a one-week
   snapshot. "~19km/wk over 3 runs" is accurate for the migration week. Added the weekly shape
   to `strava-history.md` instead: that week follows seven averaging 1.6 runs, so Phase A is
   re-establishing 3 runs, not building from them.
2. **Calf history — corrected and downgraded.** Was "never directly trained until Aug 2026
   `[data: gym log]`". The log's own Olavi notes have calf and tibialis work on 9 May 2026,
   and exercise-level records only start Jan 2026 — so earlier years are unknown, not empty.
   Jack: the Florence block included a lot of plyometric work that was never written down.
   **Also `[stated]`: the Achilles is a recent post-ultra episode, not a historical condition.**
   Data agrees — volume rose 164 → 280km/month Jan–May 2026 with no sign of management, and
   the Dec 2025 "heel > ankle pain" run was followed by 13 more runs that month. Cascaded into
   `training-model.md` §2 and §13; dropped the "9+ months recurrent" framing.
3. **Florence gym — corrected.** Was "2×/wk for ~14 weeks"; Strava says 22 sessions over
   14.9 weeks = 1.48/wk. Fixed in `athlete.md` and in the Confirmed line in `observations.md`
   that cited it. "Clustered" dropped — only three 21-day gaps in three years.
4. **Flare hypothesis — rewritten.** My earlier claim that volume fell into the flare was a
   monthly-bucketing artefact. Weekly: 1 → 3 → 4 → 6 → 7 runs/wk and 6 → 43.5km/wk in four
   weeks. But intensity fell to 0% hard in both peak weeks. Jack's framing: this was backyard
   recovery, not a training build. Points at a gap — the model has no post-ultra return
   protocol.
5. **Squat — corrected** to 100kg × 2 (8 Aug). The 12 Aug single was stopped with reps in
   reserve, so no lift has a tested max and every `%1RM` prescription is an estimate. Rest of
   the strength table verified correct against the log.
6. **Shoulder surgery, spring 2022 — added.** Was missing entirely. 48-day layoff, rehab still
   logged Oct 2023, explains 2022 being the lowest-volume year. Non-limiting now.

Still open: the grey-zone hypothesis in `observations.md` is unchanged pending Jack's call on
promoting it.

## [2026-09-21] model | Grey-zone hypothesis confirmed and rewritten
Jack confirmed it explicitly, with the mechanism: after Florence he was finishing his MPA,
running went open-ended and purely for enjoyment, quality sessions stopped entirely and
everything slipped from there `[stated]`.

Quarterly data puts the inflection exactly at Florence (24 Nov 2024). Hard running <4:45/km:
2024Q4 42.9% → 2025Q1 17.5% → 2025Q2 9.3%, and it never recovers. Grey 4:45–5:15 over the
same quarters: 20.5% → 48.2% → 59.9% `[data: Strava]`. The shape corroborates the mechanism —
before Florence the fast runs are repeated 10km+ threshold efforts; after it, nearly every run
under 4:30/km is a 5–6km one-off. Sessions became efforts.

Three lines added to Confirmed: the finding itself; that the grey zone replaced **quality, not
easy** (easy has never exceeded a third of training time in any year, so §5's ~80% target has
never once been met); and that both PBs came *after* quality stopped, so form lagged the slip
by about six months.

**Refuted:** the original wording, "grey-zone running capped volume in 2025–26". Volume fell
only 37.9 → 30.6 km/wk (19%) while hard running fell 43% → 9%. It was never a volume story.

Quarterly table added to `strava-history.md`. §2 weak-link entry updated with the numbers.

## [2026-09-21] ingest | ChatGPT coaching conversation
`raw/history/chatgpt-coaching-2025-2026.md`. An excerpt, 25 May – 30 Jul 2026; Jack says the
conversation began Oct 2025 but that part isn't included. Decisions made on the evidence rather
than referred back, at Jack's instruction.

**Verified contemporaneous.** The timestamps carry days of the week, which fixes all three to
2026 (25 May, 19 Jul, 30 Jul are Mon/Sun/Thu in 2026, not 2025). Strava corroborates the 19 Jul
entry exactly: flare 13 Jul, a 5,754m run on Friday 17 Jul (ChatGPT says "5.7 km"), an 83-minute
gym session on the Saturday, and on the Sunday a 6.0km run at 5:19/km — the "20–30 minutes easy"
it prescribed.

**The significant finding: "consistent with mid-portion" was never Jack's claim.** It was tagged
`[stated]` in `athlete.md`. The source is one line of ChatGPT's on 30 Jul 2026 — *"which fits
more with the mid-portion of the tendon than the point where it inserts into the bone"*.
Re-tagged `[inferred]` with the origin quoted. This matters because §6's entire calf and
reactive prescription assumes mid-portion, and mid-portion and insertional take different
loading `[W]`. §13 rewritten to say so plainly: **the highest-stakes unverified claim in the
wiki, and it came from an AI.**

Also from the heel question, 30 Jul: ChatGPT raised **Haglund's deformity** and asked three
narrowing questions plus photos. **None were answered** — the conversation ends there. Those
three answers are most of what separates normal anatomy from Haglund's. Now recorded as
outstanding rather than lost.

**Two rules in the model turn out to be ChatGPT's, not ours**, and are now attributed: "your
biggest training risk isn't laziness, it's enthusiasm" (§3, and the Confirmed observation), and
"report capacity, not symptoms" (§3 and `review-training`). Both stand — the gym log produced
three fresh instances of the enthusiasm pattern inside one taper week — but the wiki was
presenting borrowed insight as its own.

**Corroborations.** "I'm injury free", 25 May 2026, six days before the backyard — independent
support for the Achilles being a recent episode. Height and weight sourced: 5'7", 75kg, same
date (Strava profile reads 73kg; unreconciled, and `tests.md` uses bodyweight for the calf
ratio). The over-enthusiasm examples now carry dates and Strava verification. The refuted
"never done a classic marathon block" claim traced to its exact origin, ChatGPT 19 Jul 2026.

**Not changed, deliberately.** The provenance table defines `[inferred]` as "Claude's
interpretation", and I have used it for another AI's. Widening that definition is a schema
change, and the schema says change only when Jack agrees. Flagged, not done.

## [2026-09-21] ingest | Two research reports and the references quality accounting
`raw/research/01-achilles-and-endurance-structure.md`, `02-gym-pool-review.md`,
`references.md`. The last of the four sources SETUP.md originally asked for. Jack: Norwegian
Method (Marius Bakken) material to follow separately — nothing about it added here, since none
of it has landed.

**The wiki pages were already accurately compiled from these reports** — spot-checked all
three `wiki/references/*.md` pages against the raw text; no disagreements found. So this ingest
is mostly refinement and one real correction, not reconciliation.

**Real error found and fixed** — `training-model.md` §6's reactive-progression table used
daily-life pain to gate every level (1: >2/10, 2: ≤2/10). Wrong. Per the source (Sancho 2019),
daily-life pain ≤2/10 is a single entry gate before the whole progression; movement between
Levels 1–4 is then gated by pain from *that level's own exercise*, not daily-life pain. Fixed,
with the correction noted in place rather than silently changed, since this table decides how
hard plyometric work gets introduced to a tendon that flared four months ago.

**Sourcing-quality caveat added to all three evidence pages**, from `references.md`: only 9
citations across both reports have a working link, 4 of those are commercial or coaching
blogs, and everything else was named without one and never independently checked. The
`[evidence: W]` grades reflect the research tool's own confidence, not outside appraisal. This
doesn't invalidate anything — the physiology is standard and the named studies are real — but
it changes how much weight a `[W]` tag should carry on its own.

**Refinements folded in** (precise numbers replacing the vaguer versions already in the wiki):
Zanini's exact durability figures (4.7%→2.1% economy decay, not "halved") and full protocol;
Sancho's exact isometric dose (3×/day, 5×45s) and the 0.95×BW detail behind the calf-injury
marker; Deane's exact percentages (12.2%, 3.8%, 9.0%); Arellano's exact arm-swing costs
(3/9/13% by condition); Komi's ~12.5×BW figure flagged as a single-subject max, not a mean;
LT1/LT2 as distinct threshold landmarks; collagen synthesis timing (~37–78h) behind the
48–72h recovery rule; the single-session-spike evidence noted as independently corroborated by
Jack's own Strava data (backyard ×2.8, Sydney ×5.7); a caveat that marathon PBs are Strava
moving time, which flatters chip time.

**One note on scope, not changed:** the Achilles evidence page's "9+ months persistent
presentation" line is general evidence and stays as written — but a note was added that it was
originally applied to Jack's own case based on partial data, and the fuller picture (confirmed
with Jack) is a single recent episode, not a multi-year condition. The general evidence isn't
wrong; it just may not be the evidence that applies here.

## [2026-09-21] ingest | Norwegian Method / double threshold — answered, not applied
Jack asked how five sources (four Bakken articles, the Norwegian Singles PDF) supplement the
model. Saved to `raw/research/norwegian-method/`, compiled to
`wiki/references/evidence-norwegian-method.md`.

**Sourcing is weak and stated as such up front.** Almost entirely one person's first-person
account of his own training and coaching over 25 years, not a literature review. Two real
citations inside it: Kjøsen Talsnes et al. 2024 (Frontiers in Physiology, n=14, real) and
Casado & Bakken 2023 (a review Bakken co-authored, PubMed 36900796). Everything else —
including the "Golden Zone" lactate figures and the muscle-tone model — is anecdote.

**Flagged prominently: Bakken's central proof chain is disputed.** He credits himself with
shaping the Ingebrigtsen system; in 2025 he quotes Gjert Ingebrigtsen's sworn court testimony
denying this outright ("mine and only mine... no one has influenced it"). Neither side
verified here. Every "this is why the Ingebrigtsens are so good" line in the source should be
read as contested.

**What applies:** the core mechanism — controlled sub-threshold repeats with jog recoveries,
bounded by an effort ceiling — is a genuinely useful reframe of the grey-zone problem already
in `observations.md`: the fix isn't harder or slower, it's *structured* rather than continuous
at an undefined pace. The Norwegian Singles guide's progression method (change one run, hold
time flat, don't add a second workout until repeated weeks show recovery) closely matches
Phase A's approach already, with clearer checks worth borrowing.

**What doesn't apply, and the sources say so themselves:** double threshold. Every population
it's built for races 5k–10k at 150–220 km/wk. Bakken himself excludes the marathon from the
tight interval form ("you definitely need more continuous work"); the Singles guide says
directly that double threshold "is not a default solution" for ultras. Both of Jack's targets
are the two events these sources exclude.

**Not applied to `training-model.md`.** Whether to rewrite §5's threshold prescription in the
Singles style (controlled reps, effort ceiling, talk-test cross-check) is flagged as an open
question for Jack — a design change, not a factual correction, so it needs his say-so first.

## [2026-09-21] model | Norwegian Method integrated, kept small
Jack: integrate the research, don't over-engineer, delete anything not needed or repeated.

**Applied to `training-model.md` §5** — two changes, both operational, neither a rewrite:
- The threshold prescription now states the effort ceiling explicitly (talk test, finish with
  one more rep in reserve, don't chase pace/HR against what breath says) and names *structure*
  — controlled reps with jog recoveries, not continuous running — as what actually separates a
  threshold session from grey-zone running. Same rep scheme as before, same 3:24→3:11 evidence
  line kept.
- Double threshold added as a considered-and-rejected line, so it doesn't get re-proposed
  later: built for 150–220km/wk racing 5k–10k, both of Jack's targets are events its own
  source explicitly excludes.

**Cut from `wiki/references/evidence-norwegian-method.md`** — 127 lines to 43. Removed: the
NTNU split-session study (real finding, but scoped to splitting one day's volume, and Jack
doesn't run enough threshold volume to have anything to split — filed as not applicable, then
cut rather than kept as unused padding), the muscle-tone/elasticity model (H-grade speculation,
nothing built on it), and the Radcliffe corroboration paragraph (restated what
`evidence-endurance-structure.md` already says — pure repetition). Kept: the sourcing caveat,
the Ingebrigtsen dispute, the population mismatch, and the two things actually applied or
decided against.

Nothing added to `observations.md` — the grey-zone diagnosis lives there already; the fix
belongs in `training-model.md` where prescriptions live, not duplicated across both.

## [2026-09-21] block | Foundations planned
`wiki/blocks/2026-09-foundations.md`. 6 weeks, 21 Sep → 1 Nov, Phase A. Treated as already
underway since Sydney marathon — entry state drawn from Strava/gym data, not a blank start.
No threshold this block (Phase A default). Baseline testing deliberately deferred to week 6
per Jack — too soon post-marathon/post-Achilles to test to a real max now.

One variable: the squat and deadlift anchor rotates variant week to week (back/front squat,
conventional/trap-bar deadlift) to find what works empirically, rather than fixing one up
front — the reason `training-model.md` §4/§6 were amended earlier today. Winner gets fixed
at block review. Copenhagen plank is the block's one new lift.

## [2026-09-21] model | Upper body bumped to twice a week, gym sessions relisted
Jack: sessions looked thin next to his usual ~5 exercises, and upper body needs more work.
Fixed two things. Upper push and pull now run once per session (2×/week each) instead of
once a week total — `training-model.md` §6 Tier 2 **[stated, 2026-09-21]**. Session A gains
a push movement to match. Also rewrote both sessions in `blocks/2026-09-foundations.md` as
plain numbered lists instead of a superset table, so the exercise count is visible — 6 things
a session either way, not counting warm-up/cool-down.

## [2026-09-21] model | Every run gets a distance and pace, standing rule
Jack: "all easy" isn't good enough — every run needs how far, what pace, and what's different
between the runs in a week. Not a one-off fix: added it to `plan-training` and
`programme-session` skills so all future plans, block or single-session, name distance and
pace per run rather than a weekly total. Rewrote `blocks/2026-09-foundations.md`'s Running
section run-by-run against the existing easy pace band (5:30–6:00/km, `training-model.md`
§4) — no new evidence, just the existing rule applied properly.

Also widened the block's Emphasis: Jack wants Foundations read as a test of commitment,
schedule and routine too, not just the anchor/upper-body physical changes — what he actually
does or adds beyond the plan is data for block review, not noise `[stated, 2026-09-21]`.

## [2026-09-21] model | Stop asking RPE/enjoyment/Achilles per run
Jack won't answer a 3-question checklist for every standard run — flagged as never going to
happen. Fixed `review-training`: a run logs straight from Strava, subjective fields omitted
unless he volunteers them or flags a concern. That's what "omit what you don't have" already
meant; the skill was asking anyway. Gym still needs his own words (Strava has no exercise
detail) but takes what he gives rather than running the checklist after it.

## [2026-09-21] run | Easy — Foundations wk1
```yaml
planned: yes
duration_min: 40
distance_km: 6.92
avg_pace: 5:50
run_type: easy
```
- Planned: Week 1 easy run, 5–6km @ 5:30–6:00/km (`blocks/2026-09-foundations.md`)
- Done: 6.92km, 40:24 moving, avg pace 5:50/km, avg HR 140 (max 157), 75m elevation
  `[data, Strava activity 20270813370]`
- Beyond plan: none — distance and pace both land inside the plan
- Review: On target for week 1. Pace sits at the slow end of the easy band, right where it
  should for a rebuild week.

## [2026-09-21] block | Weekly schedule added, Foundations wk1
Jack wants the day-by-day table committed as the actual plan each week, not left in chat —
that's the only way to log what he does against what was intended, and he expects to shift
days around while finding a routine that works. Added `## Weekly schedule` to
`blocks/2026-09-foundations.md`: current week only, replaced week to week, past weeks read
from `log.md` instead. `plan-training` updated to match — ask the week's constraints first,
write the table into the block file, don't leave it in chat.

Week 1 constraint: busy Wed/Fri evenings, so gym moved to Tue/Thu and the long run/easy run
pushed to the weekend — leaves Sat/Sun as back-to-back running days, flagged as a side-effect
of the constraint, not deliberate.

Also noted: a run can split around a gym session (run there, lift, run back) or get longer —
no format change needed, each leg just logs as its own entry on the same date.

## [2026-09-21] model | Stop asking gym/time/Achilles before a session
Jack won't answer a pre-session checklist either — same pattern as the earlier run-logging
fix. Fixed `programme-session`: gym, time and Achilles status now default from the active
block and session shape rather than being asked, with the default stated in the intro line.
Take what he volunteers; a flagged concern after the fact is a `review-training` correction,
not a re-ask.

## [2026-09-22] gym | Session A — Foundations wk1 (flat gym)
```yaml
planned: yes
achilles_next_am: 1
beyond_plan: none
duration_min: 81
gym: flat
session: A
```
- Planned: Back squat ramp-up (bar×10 → 50×8 → 65×5 → 75×3) then working sets 3×5 @~80kg RPE7 (flex to 85kg if 80kg felt like RPE6), Bulgarian split squat + Pallof press superset, hip-flexion + pull superset, DB shoulder press 3×10 @14kg, cool-down.
- Done: Back squat bar×10 → 50×8 → 65×5 → 75×3 → working 3×5 @80kg. Bulgarian split squat 3×8/leg @14kg DB each hand. Pallof press 3×10/side @9.1kg (20lb) cable. Weighted march 3×30s/leg @16kg DB (swapped for banded march — no bands at flat gym). Single-arm DB row 3×8/side @18kg (swapped for lat pulldown — flat gym has none). DB shoulder press 3×10 @14kg standing, last set nearly failed on the left arm. `[stated]`
  Strava: 81:07 elapsed, avg HR 97 (max 148), relative effort 12, no exercise sets recorded `[data, Strava activity 20286596155]`
- Beyond plan: none — flat-gym equipment swaps only (march→weighted, pulldown→single-arm row), no added load or volume.
- Capacity: not reported.
- Review: Squat and split squat both executed exactly as planned despite pre-existing groin DOMS — tolerated throughout, no sharp or pulling pain reported. Jack's own read on the split squat: it's the hardest exercise in the session, in a way he considers productive rather than just unpleasant. Shoulder press at 14kg standing is now at or near true failure (left arm, last set) — next time either seat it or drop to 12kg for reps in reserve. `duration_min` (81) includes a post-session walk taken on the same watch activity, so it overstates actual gym time — don't read it as a clean session duration. Jack asked for session plans to include the reasoning/evidence behind exercise choices going forward, not just the prescription — noted for `programme-session` from the next session on.

## [2026-09-22] model | Gym sessions not interrogated either, session plans explain their reasoning
Jack won't answer a post-session checklist for gym any more than for runs `[stated, 2026-09-22]`.
`review-training` now says so explicitly: take what he volunteers, omit missing fields from the
yaml, "not reported" on the prose line. The "Always: ask about capacity" line became "note it
when he mentions it", since it contradicted the rule. Also written down: sessions narrated in
claude.ai are the normal workflow (Claude Code checks and commits the pasted draft); the
Planned line keeps the plan's stages; forced equipment swaps count as planned, not beyond plan
(as the 2026-09-22 gym entry already did); `duration_min` is the watch's session total, with
anything extra flagged in the Review line.

`programme-session` now gives a one-phrase Why per row — training-model section, or reference
with grade — as a table column rather than prose `[stated, 2026-09-22]`. The old "don't pad
sessions with evidence" rule narrowed to "fuller evidence only when asked".

## [2026-09-23] review | Achilles next-AM after Session A (22 Sep)
`achilles_next_am` on the 2026-09-22 gym entry resolved from `pending` to 1. Woke feeling
sensitive, 1/10, okay, not stiff `[stated, 2026-09-23]`. Inside the Achilles rules — no
first-steps stiffness, which is the signal that matters. One morning, no trend yet. Session B
on Thursday stands as planned.

## [2026-09-23] model | Weekly schedules kept, not replaced
Agreed with Jack `[stated, 2026-09-23]`: each week's schedule table now stays in the block file,
added below the previous week rather than replacing it. Without the plan, a past week can only
show what was done, never what was missed — and adherence is what Foundations is testing.
`plan-training` and the Foundations block's schedule intro updated to match. Also added the
Foundations block to `wiki/index.md`, which it was missing.

## [2026-09-23] model | Session logs committed straight to main
Jack asked for session log entries to go directly to `main` `[stated, 2026-09-23]`, so they
show up on the dashboard without a PR to merge. Scope is narrow: commits that only append
`run`/`gym`/`rest`/`test` entries or fill a `pending` field. Everything else still goes through
a branch. Written into `CLAUDE.md` → Commits.

## [2026-09-23] rest | Rest day — Foundations wk1
```yaml
planned: yes
achilles_next_am: 1
beyond_plan: none
```
- Planned: Rest (Wednesday evening busy), per week 1 schedule.
- Done: Rest. No Strava activity 23 Sep `[data, Strava]`.
- Next morning (24 Sep): woke with both ankles tender; took a few steps of walking before the
  tenderness went. Fine once moving `[stated, 2026-09-24]`. No score given yet, so the field
  stays `pending`.
- Review: That is first-steps stiffness — the signal that matters — and it's up on 23 Sep
  (1/10, sensitive, not stiff) after a rest day, not a training day. One rising morning, not
  two, so nothing triggers yet: Session B tonight stands, calf work stays in. If Friday
  morning is worse again, that's two rising mornings — hold Saturday's long run at 8km and
  drop the next quality session. Both ankles rather than one side is worth watching.

## [2026-09-24] review | Achilles next-AM after rest day (23 Sep) — correction
`achilles_next_am` on the 2026-09-23 rest entry resolved from `pending` to 1 `[stated,
2026-09-24]`. The tenderness was in the soft tissue around the Achilles, not the tendon
itself, and he'd been drinking the night before, which he says usually makes mornings worse
even after a rest day `[stated, 2026-09-24]`. That corrects the rest entry's review, which
read the morning as rising: the score is 1/10, the same as 23 Sep. Flat, not climbing, no
trigger. Session B tonight stands.

## [2026-09-24] model | Alcohol noted as a morning-symptom confounder
Added to `observations.md` → Confirmed: drinking the night before usually makes the next
morning's ankle/Achilles-area symptoms worse, even on a rest day `[stated, 2026-09-24]`. Tied
to the Achilles rule that two rising mornings trigger action, so a morning after drinking gets
noted as confounded rather than counted blind.

## [2026-09-24] block | Week 1 swap: run Thursday, gym Saturday
Jack's call `[stated, 2026-09-24]`: run tonight, move Session B to Saturday. The Week 1 table in
`blocks/2026-09-foundations.md` stays as planned; this is the change against it.

| Day | Was | Now |
|---|---|---|
| Thu 24 | Gym — Session B | Easy 5km, slow (5:45–6:15/km, RPE ≤4, no strides) |
| Fri 25 | Rest | Rest |
| Sat 26 | Long — 8km | Gym — Session B |
| Sun 27 | Easy — 5km | Long — 8km |

Running volume unchanged: the Sunday easy 5km moves to Thursday, the long run moves to Sunday.
The swap removes the Sat/Sun back-to-back running days. Cost: Session B's deadlift and heavy
calf work sit the day before the long run. At 8km easy that's acceptable. If legs are flat on
Sunday, shorten it rather than push.

## [2026-09-24] run | Easy — Foundations wk1 (swapped from Sun)
```yaml
planned: yes
achilles_next_am: 1
beyond_plan: none
duration_min: 34
distance_km: 5.01
avg_pace: 6:28
run_type: easy
```
- Planned: Easy 5km, slow (5:45–6:15/km, RPE ≤4, no strides). This is Sunday's easy run moved to
  Thursday, with Session B moving to Saturday (see the 2026-09-24 `block` entry).
- Done: 5.01km, 32:25 moving (33:54 elapsed), avg pace 6:28/km, avg HR 126 (max 144), 17m
  elevation, Victoria Park, run with Ruth `[data, Strava activity 20314126911]`
- Beyond plan: none
- Review: Easy was actually easy. Pace sat below the 5:45–6:15 band and HR averaged 126, which
  is 14 bpm under Monday's easy run (140 @ 5:50). Fastest 1k was 5:15, a brief surge and not a
  pattern. Running with someone else kept it conversational. Worth repeating. Friday morning
  is the next Achilles check.

## [2026-09-24] model | 80% easy target counted by distance, not time
Jack's call `[stated, 2026-09-24]`. §5 of `training-model.md` said "~80% easy / 20% harder, by
time", but the source for the figure (Muniz-Pumares 2024 **[W]**, via
`raw/research/01-achilles-and-endurance-structure.md`) measures share of mileage. The model now
says "by distance" and notes that by time the easy share is higher. The reference page now says
"of their mileage" too. The finding that the target has never been met still stands: the
grey-zone analysis measured time, and easy km take longer to run, so easy's share by distance
is lower still than the ≤⅓ recorded by time.

## [2026-09-24] ingest | Elite vs recreational intensity distribution filed
Filed from a question Jack asked, at his request `[stated, 2026-09-24]`. Added to
`references/evidence-endurance-structure.md` → Intensity distribution: elites follow the same
pyramid as the fastest recreational marathoners **[W]**, at far higher volume; Bakken's easy
runs sit under 70% HRmax **[H]**, tighter than the 75–80% guide. Also noted on the Muniz-Pumares
line that group cut-offs aren't recorded and the paper hasn't been checked directly. No new raw
source. Everything is compiled from what `raw/research/` already held.

## [2026-09-25] block | Sessions move days freely, adherence judged per week
Jack: sessions will change days regularly and that doesn't matter. What matters is finishing a
week having missed a session, or having done something other than what was planned `[stated,
2026-09-24]`. So a day move is no longer a plan change: nothing is edited, logged or committed
for it. The dashboard now matches each logged session to a planned one anywhere in that week.
It tries the same session on the same day first, then the same session on any day, then any
session of the same kind, which it flags as not as planned. A session only counts as missed
once the week has ended without it. Mid-week, the dashboard lists what's still to do. It
flags as not as planned any session done in place of a different one, logged `planned:
partial`/`no`, beyond plan, or extra. Block adherence is now counted by session, not by day.
`plan-training` and the Foundations block's schedule intro updated to match.
The 2026-09-24 swap entry above stays as history; under this rule it didn't need logging.

## [2026-09-25] rest | Rest day — Foundations wk1
```yaml
planned: yes
achilles_next_am: pending
beyond_plan: none
```
- Planned: Rest (Friday evening busy).
- Done: Rest.
- Morning (25 Sep): both ankles sensitive, "very aware", not painful, 1/10 `[stated,
  2026-09-25]`. Added to the 24 Sep run entry as `achilles_next_am`, with Jack's agreement,
  because that entry was logged before the morning.
- Review: Third 1/10 morning in a row. Flat, inside the Achilles rules. Jack says it feels
  more sensitive this week since starting the calf work than last week without it `[stated,
  2026-09-25]`. The log has no calf work so far this week: Session A (22 Sep) had none, and
  Session B moved to Saturday. Asked what he meant. There are no morning scores for last week,
  so a week-on-week comparison isn't possible yet. Manage carefully: Saturday's calf work
  starts conservative, and neither calf load nor running goes up until the mornings stay ≤1.

## [2026-09-25] review | Correction: Session A did include calf/ankle work
Correcting the 2026-09-25 rest entry, which said the log had no calf work this week. Session A
(22 Sep) had calf/ankle work in the warm-up `[stated, 2026-09-25]`. The 22 Sep gym entry didn't
record it, because the Done line only lists the main exercises. Exact drills not yet given.
Jack's read is that this week's extra sensitivity comes from the increased load. That's
plausible: this is the first full gym week after 0.2–0.9 sessions/wk, with heavy squats, split
squats and the calf/ankle warm-up all new, while running went down (~19km, 3 runs → ~12km,
2 runs `[data, Strava, 14–25 Sep]`). But it can't be pinned on one cause yet `[inferred]`.
Scores 1, 1, 1: flat, inside the rules.

## [2026-09-25] review | Session A (22 Sep) warm-up, as planned
Warm-up content for the 22 Sep gym entry, from the session plan `[stated, 2026-09-25]`:
- Mobility, 10 min, 1 round: child's pose side-to-side, cat-cow, fire hydrants, scorpions,
  90/90s, sunrise-arc lunge.
- Foot and ankle, bodyweight: tibialis raises 1×15; short-foot holds, single-leg balance,
  heel walks and toe walks, 3×20s each. No pogos: the reactive gate isn't cleared.

This is low tendon load. No hopping, and only light calf work (toe walks). So it's an unlikely
main cause of this week's sensitivity. The heavier new load was loaded ankle dorsiflexion
under the bar and dumbbells: back squat 3×5 @80kg, Bulgarian split squat 3×8/leg, weighted
march `[inferred]`.
