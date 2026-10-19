# Food diary: prototype week

**Mon 19 → Sun 25 Oct 2026** (Foundations week 5). Agreed with Jack `[stated, 2026-10-19]`.

**Why:** a sense check, not a diet. Jack doesn't want to gain fat `[stated, 2026-10-19]`. The
question: does what he eats match what his training asks, especially protein, and carbs on
light days compared with heavy ones? Targets come from `references/evidence-nutrition.md`.

**How it runs:**
- Background only. Session plans and reviews don't mention it until the week is reviewed.
- Jack messages meals as he goes, roughly. He can add packet details when he has them.
- Claude estimates kcal, protein and carbs. Every estimate is `[inferred]`, probably out by
  20–30%. Packet figures become `[data]`.
- Weigh at the gym scale on gym days. Compare the weekly figures, not single days.
- Training per day comes from `log.md` and Strava.
- The end-of-week review goes at the bottom of this page, with one `review` entry in `log.md`.

**Daily block.** Each field is a number, a listed word or `pending`. Omit what's genuinely
unknown.

```yaml
training: none        # none | run | gym | run+gym | test
relative_effort: 0    # Strava, summed; omit if none
weight_kg: 78.5       # only on a day he weighed; note the scale
kcal_est: 2400        # Claude's estimate
protein_g_est: 120
carbs_g_est: 300
alcohol_units: 0
energy: 3             # 1-5, how he felt
hunger: 3             # 1-5, 5 = hungry most of the day
complete: yes         # yes | partial — partial if meals were missed or recalled loosely
```

**Baseline weight:** 78.5 kg, gym scale, 18 Oct (Session B day). Usually 77–78 kg on the gym
scale `[stated, 2026-10-19]`.

---

## Mon 19 Oct: travel, rest

```yaml
training: none
kcal_est: pending
protein_g_est: pending
carbs_g_est: pending
alcohol_units: pending
energy: pending
hunger: pending
complete: pending
```

| Time | What | kcal | P (g) | C (g) | Source |
|---|---|---|---|---|---|
