#!/usr/bin/env python3
"""Cycle 49 thin_topup: post-pass thinnest balsa/niobium/building (recompute).

Balsa hit in equal pass; niobium and building_materials documented misses.
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
        "hunt_res_balsa": "Cycle 49 thin_topup: miss (Estrategia Nacional already in equal pass; no new plantation CAPEX).",
        "hunt_fenb_araxa": "Cycle 49 thin_topup: miss (CBMM 2025 spend / Codemig / St George already).",
        "hunt_infra_building_materials": "Cycle 49 thin_topup: miss (Holcim–Cemex Colombia / Holcim Geocycle already).",
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
    print("Cycle 49 thin_topup: 0 rows (documented misses on balsa/niobium/building)")


if __name__ == "__main__":
    main()
