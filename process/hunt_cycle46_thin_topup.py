#!/usr/bin/env python3
"""Cycle 46 thin_topup: post-pass thinnest balsa (16), niobium (17), fission_smr (18).

Hit: Brazil–Rosatom SMR engagement (other; WNN/Estadão).
Miss: balsa (FSC already in equal pass); niobium (Codemig/CBMM already dense).
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "codebook" / "observations.csv"
EVID = ROOT / "data" / "attribution" / "evidence"
BIB = ROOT / "sources" / "bibliography.yml"
FIELDS = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")).fieldnames)
ITEMS: list[tuple[dict, dict, dict]] = []


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


A(
    {
        "id": "brazil_rosatom_smr_engagement_2025",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "other",
        "counterpart": "Rosatom — engagement toward Brazilian SMR development (MME / Lula–Putin talks)",
        "country": "Brazil",
        "asset": "15 May 2025 World Nuclear News reporting Brazilian Mines and Energy Minister Alexandre Silveira (after Lula–Putin Moscow talks): Rosatom to begin engaging with the Brazilian government toward development of small modular reactors; prior Dec 2024 working-group path toward definitive nuclear cooperation details by end-2025 (TASS/Russian Embassy). No named site CAPEX. Distinct from brazil_microreactor_cnen_2025 (domestic program) and cnen_invap_rmb_mou_2025.",
        "investment_type": "technology_mou",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-22.98",
        "lon": "-44.47",
        "geo_note": "Angra complex / Rio de Janeiro state nuclear corridor (national program pin; no SMR site named).",
        "evidence": "documented",
        "source_id": "wnn_brazil_rosatom_smr_20250515",
        "note": "Actor: Rosatom (Russia) — other (not PRC). Framework engagement; no award value. Thin_topup fission_smr.",
    },
    {
        "id": "brazil_rosatom_smr_engagement_2025",
        "retrieved": "2026-10-01",
        "source_id": "wnn_brazil_rosatom_smr_20250515",
        "url": "https://www.world-nuclear-news.org/articles/brazil-and-russia-preparing-to-develop-smr-options",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Silveira told Brazilian newspaper Estadão that Russia's Rosatom was to \"begin engaging with the Brazilian government shortly so we can move toward the development of small nuclear reactors, which will be vital for our energy future\".",
        "note": "Opened World Nuclear News 15 May 2025.",
    },
    {
        "id": "wnn_brazil_rosatom_smr_20250515",
        "type": "press",
        "chicago": "World Nuclear News. “Brazil and Russia preparing to develop SMR options.” 15 May 2025.",
        "url": "https://www.world-nuclear-news.org/articles/brazil-and-russia-preparing-to-develop-smr-options",
        "annotation": "WNN on Brazilian MME–Rosatom SMR engagement after Moscow talks. Supports brazil_rosatom_smr_engagement_2025.",
        "supports": ["brazil_rosatom_smr_engagement_2025", "hunt_energy_fission_smr"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None:
                existing[k] = v
    else:
        bib.append(bib_entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_entry)

    if "hunt_energy_fission_smr" in by_id:
        rows[by_id["hunt_energy_fission_smr"]]["note"] = (
            (rows[by_id["hunt_energy_fission_smr"]].get("note") or "")
            + " Cycle 46 thin_topup: logged brazil_rosatom_smr_engagement_2025 (other)."
        ).strip()
    if "hunt_res_balsa" in by_id:
        rows[by_id["hunt_res_balsa"]]["note"] = (
            (rows[by_id["hunt_res_balsa"]].get("note") or "")
            + " Cycle 46 thin_topup: miss (FSC MIX already in equal pass)."
        ).strip()
    if "hunt_fenb_araxa" in by_id:
        rows[by_id["hunt_fenb_araxa"]]["note"] = (
            (rows[by_id["hunt_fenb_araxa"]].get("note") or "")
            + " Cycle 46 thin_topup: miss (Codemig/CBMM already dense)."
        ).strip()

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print("Cycle 46 thin_topup rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
