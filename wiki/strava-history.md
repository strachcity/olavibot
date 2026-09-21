# Strava history (compiled)

**Derived. Regenerate, don't hand-edit.** Everything here is `[data]`.

- **Source:** Strava MCP, all activities Aug 2019 → 21 Sep 2026
- **Compiled:** 21 Sep 2026 · 802 runs, 188 gym sessions
- **Row data:** `raw/history/strava-runs-2019-2026.csv`, `strava-gym-2019-2026.csv`

Pace bands are **share of running time**, not run count, and exclude backyard events and
hikes so they describe training rather than racing. Interval sessions sit in the band of
their *average* pace, so a track session with jog recoveries reads slower than it felt.

---

## Volume by year

| Year | Runs | km | Hours | km/wk | Longest | Gym |
|---|---|---|---|---|---|---|
| 2021 | 51 | 343 | 31 | 6.6 | 21.2 | 0 |
| 2022 | 46 | 249 | 23 | 4.8 | 21.3 | 2 |
| 2023 | 142 | 1259 | 108 | 24.2 | 42.5 | 6 |
| 2024 | 203 | 2076 | 176 | 39.9 | 101.1 | 86 |
| 2025 | 200 | 1729 | 150 | 33.3 | 60.8 | 58 |
| 2026 (to 21 Sep) | 153 | 1278 | 117 | 33.6 | 42.9 | 36 |

2024 is the outlier year in every column. Gym went from ~nothing to 86 sessions (1.7/wk);
2025 fell to 1.1/wk and 2026 to 0.95/wk.

## Pace distribution

| Year | <4:15 | 4:15–4:45 | **4:45–5:15 (grey)** | 5:15–5:30 | 5:30–6:00 | ≥6:00 |
|---|---|---|---|---|---|---|
| 2023 | 4.2% | 20.5% | **26.0%** | 18.1% | 16.1% | 15.0% |
| 2024 | 6.8% | 27.9% | **28.4%** | 20.6% | 9.1% | 7.1% |
| 2025 | 1.8% | 9.5% | **56.1%** | 16.6% | 12.9% | 3.2% |
| 2026 | 0.0% | 9.9% | **53.9%** | 15.3% | 15.9% | 5.0% |

Collapsed to the three bands that matter:

| Year | Grey 4:45–5:15 | Easy ≥5:30 | Hard <4:45 |
|---|---|---|---|
| 2023 | 26% | 31% | 25% |
| 2024 | 28% | 16% | **35%** |
| 2025 | **56%** | 16% | 11% |
| 2026 | **54%** | 21% | 10% |

**The grey zone doubled between the PB year and now: 28% → 56%.** But it displaced *quality*,
not easy running — hard work fell 35% → 11% over the same period while easy stayed flat at
~16–21%. Easy volume has never been above a third of training time in any year, and the
model's ~80%-easy target has never once been met.

### Quarterly, around the inflection

The year table hides where it happened. It happened at Florence.

| Quarter | Hard <4:45 | Grey 4:45–5:15 | Easy ≥5:30 | km/wk |
|---|---|---|---|---|
| 2024 Q3 | 17.4% | 35.6% | 20.9% | 49.3 |
| **2024 Q4** | **42.9%** | 20.5% | 13.5% | 45.6 |
| 2025 Q1 | 17.5% | 48.2% | 22.9% | 37.0 |
| 2025 Q2 | 9.3% | 59.9% | 13.4% | 41.4 |
| 2025 Q3 | 8.2% | 68.6% | 16.9% | 19.4 |
| 2025 Q4 | 8.2% | 52.4% | 10.8% | 29.7 |
| 2026 Q1 | 11.4% | 54.4% | 17.0% | 38.5 |
| 2026 Q2 | 12.6% | 51.1% | 22.4% | 35.4 |

Florence was run 24 Nov 2024. Hard running goes 42.9% → 17.5% → 9.3% over the following two
quarters and never recovers.

The shape of what remains matters as much as the share. Before Florence, the fast runs are
repeated 10km+ efforts at threshold (12.0km @ 4:13, 10.6km @ 4:15, 10.5km @ 4:28). Afterwards
almost every run under 4:30/km is a **5–6km one-off**. Sessions became efforts.

## 2026 by month

| Month | km | Runs | Gym |
|---|---|---|---|
| Jan | 164 | 21 | 5 |
| Feb | 183 | 21 | 6 |
| Mar | 154 | 21 | 3 |
| Apr | 193 | 23 | 4 |
| May | 280 | 26 | 2 |
| Jun | 115 | 16 | 4 |
| Jul | 66 | 11 | 5 |
| Aug | 95 | 10 | 6 |
| Sep (to 21st) | 29 | 4 | 1 |

May includes the 127km backyard; training volume that month was ~153km. Volume then **fell**
month on month into the July flare — it did not rise.

## Entry state, September 2026

| Window | km/wk | Runs/wk | Gym/wk |
|---|---|---|---|
| Last 4 weeks | 18.8 | 1.5 | 0.2 |
| Last 8 weeks | 15.4 | 1.8 | 0.9 |
| Last 12 weeks | 15.8 | 2.1 | 1.0 |

Those averages mislead on their own, because the window contains a marathon. Week by week:

| Week of | Runs | km |
|---|---|---|
| 27 Jul | 1 | 8.3 |
| 3 Aug | 1 | 3.0 |
| 10 Aug | 3 | 19.1 |
| 17 Aug | 2 | 12.0 |
| 24 Aug | 3 | 52.1 (Sydney marathon) |
| 7 Sep | 1 | 10.0 |
| 14 Sep | 3 | 18.9 |

`log.md` records entry state as "~19km/week over 3 runs" — accurate for the migration week of
14 Sep, but that is **one** normal week after a marathon, not a base. The seven weeks before it
averaged 1.6 runs and 15km. Phase A is re-establishing 3 runs, not building from them.

## Races and bests, verified against Strava

| Event | Date | Result |
|---|---|---|
| Valencia marathon | 3 Dec 2023 | 3:24:44 |
| Paris marathon | 7 Apr 2024 | 3:27:04 |
| Florence marathon | 24 Nov 2024 | **3:13:20** (PB) |
| Sydney marathon | 30 Aug 2026 | 3:42:04 |
| Macyard backyard | 8 Jun 2024 | 101.1 km, 11h45, DNF |
| Macyard backyard | 2 Aug 2025 | 70.8 km, DNF |
| Macyard backyard | 30–31 May 2026 | **127.5 km, 19h, DNF** |
| 5k | 29 Jan 2025 | 17:55 (track) |
| 10k | 22 Apr 2024 | 39:52 |
| Half | 19 May 2024 / 18 May 2025 | 1:29:18 / 1:29:09 |

## Single-session spikes

Runs more than 1.7× the longest run of the previous 28 days — the load-management risk factor
that has evidence behind it (`references/evidence-achilles-load.md`, **W**).

| Date | Run | Recent max | Ratio |
|---|---|---|---|
| 8 Jun 2024 | 101.1 km | 21.2 km | ×4.8 |
| 13 Jul 2024 | 30.0 km trail, 1051m | 15.0 km | ×2.0 |
| 2 Aug 2025 | 60.8 km | 13.0 km | ×4.7 |
| 30 May 2026 | 38.8 km (backyard) | 14.1 km | ×2.8 |
| **30 Aug 2026** | **42.9 km (Sydney)** | **7.5 km** | **×5.7** |

Every race is a spike; the backyards and Sydney are extreme ones. Sydney is the largest in
seven years of data — a marathon run off a 28-day longest of 7.5km.

## Consistency

Gaps of 10+ days without running: frequent through 2021–23 (twenty-plus, several over a
month), then **two in the whole of 2024–2026** — 10 days in Mar 2026, and 11 days after
Sydney. Whatever changed in 2024, consistency was it.
