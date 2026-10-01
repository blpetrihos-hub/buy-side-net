#!/usr/bin/env python3
"""Cycle 47 thin_topup: post-pass thinnest niobium (17), balsa (17), building_materials (20).

Misses across all three after U.S./processor angles already taken in equal pass.
Optional half-budget searches logged on hunt stubs only — no fabricated rows.
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
        "hunt_fenb_araxa": "Cycle 47 thin_topup: miss (Codemig renewal / CBMM R$13bn / CMOC 2025 production already).",
        "hunt_res_balsa": "Cycle 47 thin_topup: miss (Plantabal 2025 revenue already in equal pass; no new plantation CAPEX).",
        "hunt_infra_building_materials": "Cycle 47 thin_topup: miss (Holcim–Cemex Colombia USD 485m already).",
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
    print("Cycle 47 thin_topup: 0 rows (documented misses on niobium/balsa/building_materials)")


if __name__ == "__main__":
    main()
