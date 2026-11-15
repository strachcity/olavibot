# Body map

Feeds the body diagram on the dashboard. One row per region, each pulled from a page that
already holds the claim. Nothing new is asserted here: if a row is wrong, fix the source page
and then this one.

**Format the dashboard reads.** A table, one row per callout. `key` places the marker on the
figure (`shoulder`, `hand`, `chest`, `hip`, `thigh`, `knee`, `calf`, `ankle`, `foot`). `source`
is one or more provenance tags separated by ` · `, each `tag detail`. Cells can't contain `|`.
The `ankle` row's value is replaced on the page by the live morning score from `log.md`.

**Sides.** The diagram marks regions, not sides. Only the foot is recorded as left
`[stated, 2026-10-11]`; the shoulder, hip, knee, calf and Achilles sides are not recorded.

| key | title | value | detail | source |
|---|---|---|---|---|
| shoulder | Shoulder | Surgery, spring 2022 | Non-limiting now: DB press, bench and dead hangs all progressing. Side not recorded. | data gym log 2026 · data Strava titles |
| hand | Grip | 28kg per hand, farmer's carry | Limited the conventional deadlift at 80kg × 8. | data gym log 2026 |
| chest | Bench and row | 50kg × 8 · 50kg × 10–12 | Both solo. Upper lifts are tracked but rank below the legs. | data gym log 2026 · stated 2026-11-15 |
| hip | Hip flexors | Failed first at 127km | At the May 2026 backyard he couldn't lift the leg into a running position. Hanging knee raise ≥10 is a floor, not a max: stopped for cold arms. | stated · stated 2026-10-28 |
| thigh | Squat and deadlift | Squat 100kg × 2 · deadlift 100kg × 6 | Solo squat 100kg × 2, 110kg × 3 with the trainer; deadlift 80kg × 8 solo, 100kg × 6 with the trainer. No lift has been taken to a true max, so e1RM is still blank. | data gym log 2026 |
| knee | Knee | Resolved in 2024 | Early-2024 complaints, seen by a physio. Cleared once he took strength training seriously and stretched more. | stated |
| calf | Calf | 1.14× bodyweight, seated | 90kg single at 79kg, 15 Nov. Heel raise 40 / 43 reps left / right, 93% symmetry. Both gates pass, so Reactive Level 4 is no longer blocked. | stated 2026-11-15 · stated 2026-10-28 |
| ankle | Achilles | live | Never diagnosed. Pain mainly 2–6cm above the heel. "Consistent with mid-portion" is ChatGPT's reading, not a clinician's. | stated · inferred mid-portion |
| foot | Left foot | Outside edge, 1/10 in October | Soft-tissue-type pain on landing, Aug–Oct 2026. Jack reads it as soft tissue. Not assessed by a physio. | stated 2026-10-11 |
