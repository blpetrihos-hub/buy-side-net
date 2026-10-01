#!/usr/bin/env python3
"""Cycle 52 thin_topup: post-pass thinnest = niobium (19), fission_smr (20), building_materials (21)."""
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


# ---------------------------------------------------------------------------
# energy/fission_smr — Jamaica–AECL/CNL nuclear S&T MoU (allied) thin_topup
# ---------------------------------------------------------------------------
A(
    {
        "id": "jamaica_aecl_cnl_nuclear_mou_2024",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "allied",
        "counterpart": "AECL / Canadian Nuclear Laboratories — Government of Jamaica nuclear S&T MoU",
        "country": "Jamaica",
        "asset": "24 Oct 2024: Atomic Energy of Canada Limited and Canadian Nuclear Laboratories sign MoU with Government of Jamaica on nuclear science and technology cooperation; focus areas explicitly include Small Modular Reactors (SMRs), hydrogen, medical isotopes, waste management and environmental monitoring; builds on Jamaica’s SLOWPOKE-2 research reactor (AECL design) at UWI Mona and CARICOM’s first independent nuclear regulator. CAPEX USD not disclosed — cooperation MoU only.",
        "investment_type": "bilateral_mou",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "18.00",
        "lon": "-76.75",
        "geo_note": "University of the West Indies Mona campus, Kingston (SLOWPOKE-2 / ICENS research reactor pin).",
        "evidence": "documented",
        "source_id": "cnl_jamaica_mou_20241024",
        "note": "Actor: AECL/CNL (Canada) with Jamaica — allied. CNL primary release; SMR listed among MoU focus areas; no reactor award USD.",
    },
    {
        "id": "jamaica_aecl_cnl_nuclear_mou_2024",
        "retrieved": "2026-10-01",
        "source_id": "cnl_jamaica_mou_20241024",
        "url": "https://www.cnl.ca/atomic-energy-of-canada-limited-canadian-nuclear-laboratories-and-government-of-jamaica-agree-to-cooperate-on-nuclear-science-technology/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Atomic Energy of Canada Limited (AECL) … and Canadian Nuclear Laboratories (CNL) … have signed a Memorandum of Understanding (MOU) with the Government of Jamaica to cooperate on nuclear science and technology. … As part of the MoU, the organizations have identified a list of focus areas that interests both parties and leverages their unique strengths, including Small Modular Reactors (SMRs), hydrogen sciences, medical isotopes, radioactive waste management, and environmental monitoring, among others.",
        "note": "Opened CNL Jamaica nuclear S&T MoU release.",
    },
    {
        "id": "cnl_jamaica_mou_20241024",
        "type": "company",
        "chicago": "Canadian Nuclear Laboratories. “Atomic Energy of Canada Limited, Canadian Nuclear Laboratories and government of Jamaica agree to cooperate on nuclear science & technology.” 24 October 2024.",
        "url": "https://www.cnl.ca/atomic-energy-of-canada-limited-canadian-nuclear-laboratories-and-government-of-jamaica-agree-to-cooperate-on-nuclear-science-technology/",
        "annotation": "CNL/AECL primary on Jamaica nuclear S&T MoU including SMRs. Supports jamaica_aecl_cnl_nuclear_mou_2024.",
        "supports": ["jamaica_aecl_cnl_nuclear_mou_2024", "hunt_energy_fission_smr"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None and k != "supports":
                existing[k] = v
        supports = list(
            dict.fromkeys((existing.get("supports") or []) + (bib_entry.get("supports") or []))
        )
        existing["supports"] = supports
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
            + " Cycle 52 thin_topup: logged jamaica_aecl_cnl_nuclear_mou_2024 (allied; SMR focus MoU)."
        ).strip()
    if "hunt_fenb_araxa" in by_id:
        rows[by_id["hunt_fenb_araxa"]]["note"] = (
            (rows[by_id["hunt_fenb_araxa"]].get("note") or "")
            + " Cycle 52 thin_topup: Boston Metal MoU already in shuffled pass (miss)."
        ).strip()
    if "hunt_infra_building_materials" in by_id:
        rows[by_id["hunt_infra_building_materials"]]["note"] = (
            (rows[by_id["hunt_infra_building_materials"]].get("note") or "")
            + " Cycle 52 thin_topup: Holcim Pacasmayo/Colombia / Sinoma Z02 Edealina already (miss)."
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
    print("Cycle 52 thin_topup rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
