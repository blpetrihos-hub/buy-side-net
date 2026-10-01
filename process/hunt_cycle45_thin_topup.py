#!/usr/bin/env python3
"""Cycle 45 thin_topup: balsa / nickel / fission_smr (fewest post-pass).

Hit: U.S.–El Salvador 123 Agreement negotiations completed (Mar 2026).
Miss: balsa (WITS/AIMA/Plantabal dense); nickel (DFC/Centaurus/Atlantic dense).
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
        "id": "el_salvador_123_negotiations_202603",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "us",
        "counterpart": "U.S. Department of State — El Salvador 123 Agreement negotiations complete",
        "country": "El Salvador",
        "asset": "13 Mar 2026: U.S. Under Secretary of State Thomas G. DiNanno announces completion of negotiations on a U.S.–El Salvador Section 123 Agreement for peaceful nuclear cooperation, with remaining steps before signature/entry into force. Distinct from el_salvador_ncmou_20250203 (non-binding NCMOU). Framework diplomacy — no project CAPEX.",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "13.69",
        "lon": "-89.19",
        "geo_note": "San Salvador / bilateral diplomacy pin (no reactor site named).",
        "evidence": "documented",
        "source_id": "elsalvador_english_123_20260313",
        "note": "Actor: U.S. State Department with El Salvador — us. El Salvador in English 13 Mar 2026 quoting Under Secretary DiNanno. Complements NCMOU row as next legal step toward material/equipment transfer authority.",
    },
    {
        "id": "el_salvador_123_negotiations_202603",
        "retrieved": "2026-10-01",
        "source_id": "elsalvador_english_123_20260313",
        "url": "https://elsalvadorinenglish.com/2026/03/13/u-s-and-el-salvador-strengthen-energy-partnership-with-123-agreement/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The governments of United States and El Salvador have successfully concluded negotiations on a 123 Agreement … The announcement was made by Thomas G. DiNanno, U.S. Under Secretary of State … Officials from both countries expressed their commitment to advancing the remaining steps required before the agreement is formally signed and enters into force.",
        "note": "Opened El Salvador in English 13 Mar 2026.",
    },
    {
        "id": "elsalvador_english_123_20260313",
        "type": "press",
        "chicago": "El Salvador in English. “U.S. and El Salvador Strengthen Energy Partnership with 123 Agreement.” 13 March 2026.",
        "url": "https://elsalvadorinenglish.com/2026/03/13/u-s-and-el-salvador-strengthen-energy-partnership-with-123-agreement/",
        "annotation": "English-language report of completed U.S.–El Salvador 123 negotiations. Supports el_salvador_123_negotiations_202603.",
        "supports": ["el_salvador_123_negotiations_202603", "hunt_energy_fission_smr"],
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

    for hid, note in {
        "hunt_res_balsa": "Cycle 45 thin_topup: miss (WITS/AIMA/Plantabal dense).",
        "hunt_res_nickel": "Cycle 45 thin_topup: miss (DFC/Centaurus/Atlantic dense).",
        "hunt_energy_fission_smr": "Cycle 45 thin_topup: logged el_salvador_123_negotiations_202603 (U.S.).",
    }.items():
        if hid in by_id:
            rows[by_id[hid]]["note"] = (
                (rows[by_id[hid]].get("note") or "") + " " + note
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
    print("Cycle 45 thin_topup added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
