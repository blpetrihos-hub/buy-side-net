#!/usr/bin/env python3
"""Cycle 118 hunt: shuffle_seed=20261118; equal budget; U.S./PRC split; thin after.

Order: building_materials, wind, balsa, fission_smr, copper, port_cranes, nickel,
power_plants_grid, lithium, engineering_epc, other_renewables, bridges_roads,
solar, water, port_ownership, rail, graphite, niobium.
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
        "id": "tec_lares_crib_dam_2008",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "TEC General Contractor Corp — USACE debris control structure (crib dam), Lares",
        "country": "Puerto Rico",
        "asset": "30 Sep 2008: USACE awards contract W912EP08C0020 to TEC General Contractor, Corp. for debris control structure (crib dam); obligated USD 16,427,270.12; place of performance Lares. Distinct from Portugués Dam / Río Puerto Nuevo flood-control awards.",
        "investment_type": "epc",
        "value": "16427270.12",
        "currency": "USD",
        "value_usd": "16427270.12",
        "fx_usd": "1",
        "fx_date": "2008-09-30",
        "year": "2008",
        "status": "active",
        "lat": "18.295",
        "lon": "-66.878",
        "geo_note": "Debris control crib dam, Lares Municipality, Puerto Rico (USASpending PoP Lares).",
        "evidence": "documented",
        "source_id": "usaspending_tec_lares_crib_20080930",
        "note": "Actor: TEC General Contractor Corp (Puerto Rico / U.S.) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "tec_lares_crib_dam_2008",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_tec_lares_crib_20080930",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP08C0020_9700_-NONE-_-NONE-/",
        "price_year": "2008",
        "evidence": "documented",
        "quote": "DEBRI CONTROL STRUCT.(CRIB DAM)",
        "note": "Opened USASpending: TEC; USD 16,427,270.12; signed 2008-09-30; PoP Lares, PR.",
    },
    {
        "id": "usaspending_tec_lares_crib_20080930",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP08C0020_9700_-NONE-_-NONE- (TEC General Contractor, Corp.; Lares crib dam). Signed 30 September 2008. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP08C0020_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP08C0020_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 16.4m Lares crib dam. Supports tec_lares_crib_dam_2008.",
        "supports": ["tec_lares_crib_dam_2008", "hunt_res_water"],
    },
)

A(
    {
        "id": "carro_ponce_cofferdam_2020",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Construcciones Jose Carro S.E. — USACE temporary sheet-piling cofferdam (Ponce)",
        "country": "Puerto Rico",
        "asset": "12 May 2020: USACE awards contract W912EP20C0005 to Construcciones Jose Carro, S.E. for temporary metal sheet piling (cofferdam) for toe key and ACBM installation; obligated USD 15,567,270.39; place of performance Ponce. Distinct from Carro De Diego Bridge and Portugués Dam awards.",
        "investment_type": "epc",
        "value": "15567270.39",
        "currency": "USD",
        "value_usd": "15567270.39",
        "fx_usd": "1",
        "fx_date": "2020-05-12",
        "year": "2020",
        "status": "active",
        "lat": "18.010",
        "lon": "-66.615",
        "geo_note": "Cofferdam / toe-key works, Ponce Municipality, Puerto Rico (USASpending PoP Ponce; Portugués Dam corridor).",
        "evidence": "documented",
        "source_id": "usaspending_carro_cofferdam_20200512",
        "note": "Actor: Construcciones Jose Carro S.E. (Puerto Rico / U.S.) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "carro_ponce_cofferdam_2020",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_carro_cofferdam_20200512",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP20C0005_9700_-NONE-_-NONE-/",
        "price_year": "2020",
        "evidence": "documented",
        "quote": "TEMPORARY METAL SHEET PILING (COFFERDAM) FOR TOE KEY AND ACBM INSTALLATION",
        "note": "Opened USASpending: Jose Carro; USD 15,567,270.39; signed 2020-05-12; PoP Ponce, PR.",
    },
    {
        "id": "usaspending_carro_cofferdam_20200512",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP20C0005_9700_-NONE-_-NONE- (Construcciones Jose Carro, S.E.; Ponce cofferdam). Signed 12 May 2020. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP20C0005_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP20C0005_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 15.6m Ponce cofferdam. Supports carro_ponce_cofferdam_2020.",
        "supports": ["carro_ponce_cofferdam_2020", "hunt_res_water"],
    },
)


def upsert_bib(bib: list, bib_by: dict, entry: dict) -> None:
    eid = entry["id"]
    if eid in bib_by:
        bib[bib_by[eid]].update(entry)
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added: list[str] = []

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

    hunt_updates = {
        "hunt_infra_building_materials": "Cycle 118: equal budget; Caribbean Lumber dense (miss).",
        "hunt_energy_wind": "Cycle 118: equal budget; Goldwind/Mingyang dense (miss).",
        "hunt_res_balsa": "Cycle 118: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_energy_fission_smr": "Cycle 118: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_res_copper": "Cycle 118: equal budget; CMOC dense (miss).",
        "hunt_infra_port_cranes": "Cycle 118: equal budget; ZPMC dense (miss).",
        "hunt_res_nickel": "Cycle 118: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_br_power_equip": "Cycle 118: equal budget; EXIM Guyana/State Grid dense (miss).",
        "hunt_res_lithium": "Cycle 118: equal budget; Ganfeng dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 118: equal budget; OBO NEC backlog exhausted (miss).",
        "hunt_energy_other_renewables": "Cycle 118: equal budget; Jinko Chile BESS unnamed-site pass dry; Trina dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 118: equal budget; De Diego dense (miss).",
        "hunt_energy_solar": "Cycle 118: equal budget; Sungrow Vista Alegre dense (miss).",
        "hunt_res_water": "Cycle 118: logged tec_lares_crib_dam_2008 + carro_ponce_cofferdam_2020 (USACE).",
        "hunt_infra_port_ownership": "Cycle 118: equal budget; COSCO Chancay dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 118: equal budget; CRRC dense (miss).",
        "hunt_res_graphite": "Cycle 118: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_fenb_araxa": "Cycle 118: equal budget; CBMM dense (miss).",
    }
    for hid, note in hunt_updates.items():
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
    print("Cycle 118 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
