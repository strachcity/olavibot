# Food diary: one-month pilot

**Mon 19 Oct → Sun 15 Nov 2026**, four weeks. Started as a one-week prototype `[stated,
2026-10-19]`; extended to a month on 24 Oct to catch patterns one week can't `[stated,
2026-10-24]`. Some weeks Jack goes out, some he doesn't; week 1 (19–25 Oct) was a quiet one
`[stated, 2026-10-24]`, so it isn't the typical week, and neither was the 12–18 Oct baseline.
A short summary at the end of each week; the full review and recommendations after 15 Nov.

**Why:** a sense check, not a diet. Jack doesn't want to gain fat `[stated, 2026-10-19]`. The
question: does what he eats match what his training asks, especially protein, and carbs on
light days compared with heavy ones? Targets come from `references/evidence-nutrition.md`.

**How it runs:**
- Background only. Session plans and training reviews don't mention it until the month is reviewed.
- Jack messages meals as he goes, roughly. He can add packet details when he has them.
- Claude estimates kcal, protein and carbs. Every estimate is `[inferred]`, probably out by
  20–30%. Packet figures become `[data]`.
- Weigh at the gym scale on gym days. Compare the weekly figures, not single days.
- Training per day comes from `log.md` and Strava.
- A short weekly summary goes under each week. The full review goes at the bottom of this page,
  with one `review` entry in `log.md`.

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

**Daily energy estimate** `[inferred]`, about ±15%. Resting rate from the Mifflin–St Jeor
equation (78kg, 170cm, age assumed early 30s, not yet confirmed): ~1,700 kcal. ×1.35 for a desk
job with ordinary walking gives ~2,300 before training. Training comes from Strava's calories:
21 Sep → 18 Oct averaged ~310 kcal/day `[data]` (8,653 kcal over 28 days). Strava's figure
includes resting burn and uses its 73kg profile weight, so the true extra is a little lower.

| Day type this week | Training | Roughly maintains weight |
|---|---|---|
| Rest or travel (Mon) | none | ~2,300 |
| Easy run 4–5km | ~300 | ~2,600 |
| Gym session | ~250–400 | ~2,600 |
| Long run 11km | ~750 | ~3,050 |
| **Week average** | | **~2,550** |

Cross-check 1, Apple Watch: active energy averaged 734 kcal/day over the last 90 days and
894 over the year `[data: Apple Watch Move, to 19 Oct 2026]`. Add ~1,700 resting gives ~2,450
a day recently and ~2,600 over the year. The watch figure is an estimate too, and depends on
the weight set in Health. It lands within ~100 kcal of the table above.

Cross-check 2: the bodyweight trend. 75kg in May → 77–78kg now on the same scale. If all of
that were fat, it would be a surplus of only ~100–150 kcal/day across ~5 months `[inferred]`.
Some may be muscle. The scale over weeks is a better calorie meter than any formula.

**Baseline weight:** 78.5 kg, gym scale, 18 Oct (Session B day). Usually 77–78 kg on the gym
scale `[stated, 2026-10-19]`.

---

## Baseline: recall of 12–18 Oct (Foundations week 4)

From Jack's rough recall `[stated, 2026-10-19]`. Every number is Claude's estimate
`[inferred]`, ±30% at best. Assumptions: 1 level scoop of Huel Black = half the recommended serving
`[stated, 2026-10-19]`, taken as ~200 kcal and 20g protein; semi-skimmed milk 300ml ≈ 140 kcal; a pint ≈ 200 kcal, ~15g carbs, ~2.5 units;
crisps a standard bag ≈ 170 kcal; sandwiches ≈ 450–550 kcal. Black coffee ×2 a day, negligible.
Chicken sandwiches always include avocado `[stated, 2026-10-19]`, taken as half an avocado per
sandwich (~120 kcal); Sun 18 corrected for it. Tuna mayo sandwiches always include onion,
chilli and lettuce, sometimes red pepper `[stated, 2026-10-19]`; negligible energy. The chicken
wrap (Mon 12) and tikka baguette (Wed 14) had no avocado `[stated]`.

| Day | Training `[data]` | Food, roughly | kcal | P (g) | C (g) | Pints |
|---|---|---|---|---|---|---|
| Mon 12 | Easy 5km | Huel + milk; fried chicken wrap; Nando's: 4 thighs, mash, garlic bread, 5 wings | 2,400 | 170 | 150 | 0 |
| Tue 13 | Easy 6km + strides | Eggs ×3, beans, toast ×2; tuna mayo baguette, crisps; Huel bar; burrito, chips, salsa, guac | 3,050 | 125 | 325 | 0 |
| Wed 14 | Session A | Huel ready-to-drink; chicken tikka baguette, crisps; ham and cheese sandwich; protein nut bar; tuna, veg and cheese sandwich | 2,300 | 140 | 200 | 0 |
| Thu 15 | Rest | Huel + milk; tuna mayo sandwich, crisps; tuna mayo sandwich | 2,100 | 80 | 175 | 3–4 |
| Fri 16 | Rest | Huel + milk; tuna mayo sandwich, crisps; oven pizza | 3,250 | 95 | 300 | 6–8 |
| Sat 17 | Long 12km | Veggie bagel; tuna sandwiches ×2; crisps | 2,250 | 65 | 210 | 4 |
| Sun 18 | Session B + 2×2.5km | Eggs ×2, avocado, seeded toast ×2; tuna mayo and cheese sandwich; chicken and avocado sandwiches ×2 | 2,350 | 125 | 150 | 0 |
| **Average** | | | **~2,550** | **~115** | **~215** | **~14.5 total** |

What it shows `[inferred]`, against `references/evidence-nutrition.md`:
- **Energy ≈ maintenance.** ~2,550 eaten against ~2,450–2,600 burned. Fits a stable 77–78kg.
- **Alcohol is the biggest single item.** ~14.5 pints ≈ 2,900 kcal, about a sixth of the
  week, all Thu–Sat. Without it the week would have run ~400 kcal/day under maintenance.
- **Protein is fine on average, low on drinking days.** ~115 g/day ≈ 1.5 g/kg, inside
  1.2–2.0. Thu–Sat ran 65–95 g, under the 94 g floor.
- **Carbs are low, fat is high.** ~215 g/day ≈ 2.8 g/kg, under even the light-day band
  (3–5 g/kg), and about a quarter of that is beer. Fat ≈ 100 g/day (~35% of energy), mostly
  mayo, cheese, crisps and fried food.
- **Veg is there, but in small amounts, and there's no fruit.** Onion, chilli and lettuce in
  every tuna mayo sandwich (at least 7), sometimes red pepper; avocado in the chicken
  sandwiches; tomato, beans, salsa and one veg topping besides. No fruit all week. *Corrected
  19 Oct: this said "almost no fruit or veg", before Jack said what goes in his sandwiches.*
- Achilles 2/10 on Sun 18 Oct followed Fri–Sat drinking, which fits the confirmed observation
  that drinking worsens next-morning symptoms.

---

## Mon 19 Oct: travel, rest

```yaml
training: none
kcal_est: 2900
protein_g_est: 200
carbs_g_est: 200
alcohol_units: 0
energy: pending
hunger: pending
complete: yes
```

| Time | What | kcal | P (g) | C (g) | Source |
|---|---|---|---|---|---|
| Breakfast | Huel Black 1 scoop, 300ml semi-skimmed milk; black coffee | 340 | 30 | 26 | `[stated]`, estimate `[inferred]` |
| Lunch | Tortilla burrito, medium: hot chicken, black beans, Mexican rice, guacamole, cheese, sour cream; black coffee | 1,050 | 50 | 110 | `[stated]`, estimate `[inferred]` |
| Dinner | 2 sandwiches, 4 slices seeded bread: 2 chicken breasts, 1 avocado, cucumber, mayo and mustard, cheese | 1,500 | 120 | 65 | `[stated]`, estimate `[inferred]` |
| Evening | Huel sparkling multivitamin energy drink, 330ml can: 3.0g sugars, 3.5g fibre, 100mg caffeine | 30 | 0 | 4 | `[data: can label]` |
| **Day** | | **~2,900** | **~200** | **~200** | |

Apple Watch active energy expected ~600 `[stated]`, so ~2,300 burned in total. ~600 over
`[inferred]`.

## Tue 20 Oct: Session A (moved from Wed; easy 5km moved to Wed)

```yaml
training: gym
relative_effort: 14
kcal_est: 1850
protein_g_est: 105
carbs_g_est: 195
alcohol_units: 0
energy: pending
hunger: pending
complete: yes
```

| Time | What | kcal | P (g) | C (g) | Source |
|---|---|---|---|---|---|
| Breakfast | None, missed by accident | 0 | 0 | 0 | `[stated]` |
| Lunch | Tuna mayo sandwich with onion, red pepper, lettuce; Walkers Baked cheese and onion, small multipack bag | 600 | 27 | 58 | `[stated]`, estimate `[inferred]` |
| Afternoon | Tesco oat and raisin cookie, 1 of a 5-pack (177 kcal `[data: label]`; macros estimated) | 177 | 2 | 25 | `[data]` + `[inferred]` |
| Dinner | Chicken, bacon and leek pasta with cherry tomatoes and garlic-and-herb Philadelphia, 1 of 2 portions (~100g dry pasta, 1 breast, ~60g Philadelphia) | 850 | 65 | 80 | `[stated]`, estimate `[inferred]` |
| Evening | Tesco chocolate milk (size not given, taken as 330ml) | 220 | 11 | 33 | `[stated]`, estimate `[inferred]` |
| **Day** | | **~1,850** | **~105** | **~195** | |

Session A: Strava 413 kcal, 81 min `[data]`. Burned ~2,600 in total `[inferred]`, so ~750
under. Taken with Monday's ~600 over, the two days roughly net out.

## Wed 21 Oct: easy 5km planned (moved from Tue)

```yaml
training: run
relative_effort: 18
kcal_est: 2170
protein_g_est: 135
carbs_g_est: 234
alcohol_units: 0
energy: pending
hunger: pending
complete: yes
```

| Time | What | kcal | P (g) | C (g) | Source |
|---|---|---|---|---|---|
| Breakfast | Huel Black 1 scoop, 300ml semi-skimmed milk (assumed the usual) | 340 | 30 | 26 | `[stated]`, estimate `[inferred]` |
| Lunch | Tuna mayo sandwich (usual fillings); Walkers Baked crisps, small bag | 600 | 27 | 58 | `[stated]`, estimate `[inferred]` |
| Day | Banana; 2 black coffees | 110 | 1 | 27 | `[stated]`, estimate `[inferred]` |
| Dinner | Leftover chicken, bacon and leek pasta, full portion | 850 | 65 | 80 | `[stated]`, estimate `[inferred]` |
| Evening | Snack a Jack, single rice cake, ~50 kcal `[stated]` | 50 | 1 | 10 | `[stated]` |
| Evening | Tesco chocolate milk (taken as 330ml, as Tue) | 220 | 11 | 33 | `[stated]`, estimate `[inferred]` |
| **Day** | | **~2,170** | **~135** | **~234** | |

Run: 6.0km, Strava 406 kcal `[data]`. Burned ~2,650 in total `[inferred]`, so ~480 under.

## Thu 22 Oct: heel-raise baseline, nothing else

```yaml
training: test
kcal_est: 2455
protein_g_est: 143
carbs_g_est: 192
alcohol_units: 0
energy: pending
hunger: pending
complete: yes
```

| Time | What | kcal | P (g) | C (g) | Source |
|---|---|---|---|---|---|
| Breakfast | Huel Black 1 scoop, 300ml semi-skimmed milk; black coffee | 340 | 30 | 26 | `[stated]`, estimate `[inferred]` |
| Lunch | Tuna mayo sandwich (usual fillings); Walkers Baked crisps, small bag | 600 | 27 | 58 | `[stated]`, estimate `[inferred]` |
| Evening | Canapés at an event: about a chicken breast's worth of chicken, 4 small spring rolls, 1 gyoza. No drinks `[stated]` | 515 | 51 | 30 | `[stated]`, estimate `[inferred]` |
| Dinner | Baked butter paneer, cooked from scratch from a cookbook recipe (serves 4: 500g paneer, 150ml double cream, 5 tbsp Greek yoghurt, 2 tbsp honey, 2 tins tomatoes, oil; no butter) `[data: recipe]`. Taken as 1 of 4 portions (~710 kcal), 75g dry rice `[stated]` (~270), pak choi instead of naan (~20) | 1,000 | 35 | 78 | `[stated]` + `[data]`, portion `[inferred]` |
| **So far** | | **~2,455** | **~143** | **~192** | |

## Fri 23 Oct: easy 6km (plan changed from 4km, 22 Oct)

```yaml
training: run
relative_effort: 31
kcal_est: 2490
protein_g_est: 162
carbs_g_est: 216
alcohol_units: 0
energy: pending
hunger: pending
complete: yes
```

| Time | What | kcal | P (g) | C (g) | Source |
|---|---|---|---|---|---|
| Breakfast | Huel Black 1 scoop, 300ml semi-skimmed milk (assumed the usual) | 340 | 30 | 26 | `[stated]`, estimate `[inferred]` |
| Lunch | Small bowl of leftover pasta; 1 ham and cheese croissant | 800 | 45 | 75 | `[stated]`, estimate `[inferred]` |
| Afternoon | Cheese and tomato croissant | 350 | 12 | 30 | `[stated]`, estimate `[inferred]` |
| Dinner | Chicken fajitas, 2 wraps, peppers, onion, fresh salsa, guac (~½ avocado). No drinks `[stated]` | 1,000 | 75 | 85 | `[stated]`, estimate `[inferred]` |
| **Day** | | **~2,490** | **~162** | **~216** | |

Run: 6.35km, Strava 425 kcal `[data]`. Burned ~2,700 `[inferred]`, so ~200 under.

## Sat 24 Oct: long run, 12.1km at 08:29

```yaml
training: run
relative_effort: 47
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
| Breakfast, after the run | Deli bagel (everything/seeded): sliced turkey or ham, bacon, lettuce, tomato, mayo `[stated: photo]` | 650 | 35 | 55 | estimate `[inferred]` |
| **So far** | | **~650** | **~35** | **~55** | |

Run: 12.1km, Strava 822 kcal `[data]`. Burn today ~3,100 `[inferred]`.
