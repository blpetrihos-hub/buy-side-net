#!/usr/bin/env python3
"""Cycle 63 thin_topup: 3 thinnest after equal pass.

Post-equal thinnest still tied at 23: fission_smr, balsa, graphite, nickel, niobium.
Rotate from c62 (balsa/niobium/graphite) → nickel / fission_smr / graphite.
No distinct new named LatAm deals opened — documented misses only.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "codebook" / "observations.csv"
FIELDS = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")).fieldnames)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}

    notes = {
        "hunt_res_nickel": (
            " Cycle 63 thin_topup: nickel half-budget — Jervois SMP / Westwin / "
            "DFC Piauí / MMG Anglo already (miss)."
        ),
        "hunt_energy_fission_smr": (
            " Cycle 63 thin_topup: fission_smr half-budget — Peru FIRST / USTDA LAC "
            "nuclear / Meitner / El Salvador 123 already (miss)."
        ),
        "hunt_res_graphite": (
            " Cycle 63 thin_topup: graphite half-budget — Atlas Malacacheta / Graphcoa / "
            "South Star already (miss)."
        ),
    }
    for hid, note in notes.items():
        if hid in by_id:
            rows[by_id[hid]]["note"] = (
                (rows[by_id[hid]].get("note") or "") + note
            ).strip()

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    print("Cycle 63 thin_topup: 0 rows (3 documented misses: nickel/fission_smr/graphite)")


if __name__ == "__main__":
    main()
