#!/usr/bin/env python3
"""Cycle 50 thin_topup: post-pass thinnest niobium / fission_smr / wind (recompute).

Equal-pass hits raised water/nickel/building/balsa/port_ownership/engineering;
niobium still thinnest; fission_smr and wind tied next.
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
        "hunt_fenb_araxa": "Cycle 50 thin_topup: miss (CBMM 2025 spend / Codemig renewal / St George already).",
        "hunt_energy_fission_smr": "Cycle 50 thin_topup: miss (USTDA LAC nuclear / FIRST workshop already).",
        "hunt_energy_wind": "Cycle 50 thin_topup: miss (Vestas/Nordex/Goldwind / AES JK already).",
    }
    for hid, note in notes.items():
        if hid in by_id:
            rows[by_id[hid]]["note"] = (
                (rows[by_id[hid]].get("note") or "") + " " + note
            ).strip()
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})
    print("Cycle 50 thin_topup: 0 rows (documented misses on niobium/fission_smr/wind)")


if __name__ == "__main__":
    main()
