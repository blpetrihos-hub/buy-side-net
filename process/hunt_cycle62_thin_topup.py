#!/usr/bin/env python3
"""Cycle 62 thin_topup: 3 thinnest after equal pass.

Post-equal thinnest still tied at 23: fission_smr, balsa, graphite, nickel, niobium.
Rotate from c61 (graphite/nickel/fission_smr) → balsa / niobium / graphite.
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
        "hunt_res_balsa": (
            " Cycle 62 thin_topup: balsa half-budget — AIMA Siemens / Plantabal Baltek / "
            "CoreLite already (miss)."
        ),
        "hunt_fenb_araxa": (
            " Cycle 62 thin_topup: niobium half-budget — St George Boston Metal / CBMM / "
            "CMOC Catalão already (miss)."
        ),
        "hunt_res_graphite": (
            " Cycle 62 thin_topup: graphite half-budget — Atlas Malacacheta / Graphcoa / "
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

    print("Cycle 62 thin_topup: 0 rows (3 documented misses: balsa/niobium/graphite)")


if __name__ == "__main__":
    main()
