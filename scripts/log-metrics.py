#!/usr/bin/env python3
"""Read the metrics blocks out of wiki/log.md and total them up.

Block reviews ask for adherence %, enjoyment average, beyond-plan count and the
Achilles trend. Eyeballing a year of prose to get those is how soft numbers end
up in the wiki tagged [data]. This reads the fenced yaml blocks instead.

    scripts/log-metrics.py                      # whole log
    scripts/log-metrics.py --since 2026-10-01   # one block
    scripts/log-metrics.py --since 2026-10-01 --until 2026-11-14
    scripts/log-metrics.py --type gym --entries # list entries, don't total

Stdlib only, no PyYAML: the metrics block is deliberately flat key: value.
"""

import argparse
import pathlib
import re
import statistics
import sys

HEADER = re.compile(r"^## \[(\d{4}-\d{2}-\d{2})\]\s+(\w+)\s*\|\s*(.*)$")
FENCE = re.compile(r"^```\s*yaml\s*$")
FIELD = re.compile(r"^([a-z_]+):\s*(.*?)\s*(?:#.*)?$")


def parse(path):
    """Yield one dict per log entry. Entries without a metrics block still count."""
    entries, cur, in_block = [], None, False
    for line in path.read_text().splitlines():
        m = HEADER.match(line)
        if m:
            cur = {"date": m.group(1), "type": m.group(2), "title": m.group(3)}
            entries.append(cur)
            in_block = False
            continue
        if cur is None:
            continue
        if FENCE.match(line):
            in_block = True
            continue
        if in_block:
            if line.strip() == "```":
                in_block = False
                continue
            f = FIELD.match(line.strip())
            if f and f.group(2):
                cur[f.group(1)] = f.group(2)
    return entries


def num(entries, key):
    """Numeric values for key, skipping 'pending' and anything unparseable."""
    out = []
    for e in entries:
        v = e.get(key)
        if v is None or v == "pending":
            continue
        try:
            out.append(float(v))
        except ValueError:
            pass
    return out


def mean(vals, places=1):
    return f"{statistics.mean(vals):.{places}f}" if vals else "—"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", default="wiki/log.md")
    ap.add_argument("--since", help="inclusive YYYY-MM-DD")
    ap.add_argument("--until", help="inclusive YYYY-MM-DD")
    ap.add_argument("--type", dest="types", action="append",
                    help="filter by entry type; repeatable")
    ap.add_argument("--entries", action="store_true", help="list entries instead of totals")
    a = ap.parse_args()

    path = pathlib.Path(a.log)
    if not path.exists():
        sys.exit(f"no log at {path}")

    entries = parse(path)
    if a.since:
        entries = [e for e in entries if e["date"] >= a.since]
    if a.until:
        entries = [e for e in entries if e["date"] <= a.until]
    if a.types:
        entries = [e for e in entries if e["type"] in a.types]

    if not entries:
        sys.exit("no entries in range")

    span = f"{entries[0]['date']} → {entries[-1]['date']}"

    if a.entries:
        for e in entries:
            bits = [f"{k}={e[k]}" for k in
                    ("planned", "rpe", "enjoyment", "achilles_during", "achilles_next_am",
                     "beyond_plan", "duration_min", "distance_km", "run_type", "gym",
                     "session", "reactive_level")
                    if k in e]
            print(f"[{e['date']}] {e['type']:6} {e['title']}")
            if bits:
                print(f"           {' '.join(bits)}")
        return

    sessions = [e for e in entries if e["type"] in ("run", "gym", "rest")]
    planned = [e.get("planned") for e in sessions if e.get("planned")]
    adherence = "—"
    if planned:
        scored = sum(1.0 if p == "yes" else 0.5 if p == "partial" else 0.0 for p in planned)
        adherence = f"{100 * scored / len(planned):.0f}% (n={len(planned)})"

    beyond = [e for e in sessions if e.get("beyond_plan") not in (None, "none")]
    am = num(entries, "achilles_next_am")
    pending = sum(1 for e in entries if e.get("achilles_next_am") == "pending")
    dist = num(entries, "distance_km")

    counts = {}
    for e in entries:
        counts[e["type"]] = counts.get(e["type"], 0) + 1

    print(f"{span}   {len(entries)} entries")
    print("  " + "  ".join(f"{t}:{n}" for t, n in sorted(counts.items())))
    print()
    print(f"  adherence          {adherence}")
    print(f"  enjoyment          {mean(num(entries, 'enjoyment'))} / 5")
    print(f"  rpe                {mean(num(entries, 'rpe'))} / 10")
    print(f"  achilles during    {mean(num(entries, 'achilles_during'))} / 10")
    if am:
        first, last = am[: max(1, len(am) // 3)], am[-max(1, len(am) // 3):]
        arrow = "↑" if statistics.mean(last) > statistics.mean(first) + 0.5 else \
                "↓" if statistics.mean(last) < statistics.mean(first) - 0.5 else "→"
        print(f"  achilles next am   {mean(am)} / 10  {arrow} "
              f"({mean(first)} early → {mean(last)} late)")
    if pending:
        print(f"                     {pending} still pending")
    print(f"  beyond plan        {len(beyond)} of {len(sessions)} sessions")
    for e in beyond:
        print(f"                       [{e['date']}] {e['beyond_plan']}")
    if dist:
        print(f"  distance           {sum(dist):.1f} km over {len(dist)} runs")
    print()
    print("  Trends, not single numbers. Anything here is [data] — give the range.")


if __name__ == "__main__":
    main()
