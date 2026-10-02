#!/usr/bin/env python3
"""Cycle 128 hunt: shuffle_seed=20261128; equal budget; U.S./PRC split; thin after.

Order: balsa, port_cranes, building_materials, lithium, nickel, rail, fission_smr,
wind, other_renewables, copper, engineering_epc, water, niobium, graphite,
port_ownership, power_plants_grid, bridges_roads, solar.
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


def row_doc(
    rid,
    layer,
    subcategory,
    side,
    counterpart,
    country,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    source_id,
    quote,
    url,
    note,
    hunt_support,
):
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": "epc",
            "value": value,
            "currency": "USD",
            "value_usd": value,
            "fx_usd": "1",
            "fx_date": fx_date,
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": "documented",
            "source_id": source_id,
            "note": note,
        },
        {
            "id": rid,
            "retrieved": "2026-10-02",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": "documented",
            "quote": quote,
            "note": f"Opened USASpending Award API; USD {value}; date_signed {fx_date}.",
        },
        {
            "id": source_id,
            "type": "government",
            "chicago": f"U.S. Department of the Treasury, USAspending.gov. Award supporting {rid}. Signed {fx_date}. {url}.",
            "url": url,
            "annotation": f"USASpending primary. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


row_doc(
    "knik_gtmo_runway_2007",
    "infrastructure",
    "engineering_epc",
    "us",
    "Knik Construction Co., Inc. — NAVFAC Runway 10-28 (NS Guantanamo Bay)",
    "Cuba",
    "1 May 2007: Department of the Navy awards contract N6945007C1257 to Knik Construction Co., Inc. for Runway 10-28 works at Naval Station Guantanamo Bay, Cuba; obligated USD 25,551,723.00. Distinct from RQ GTMO facility packages and AECOM GTMO fuel pier.",
    "25551723.00",
    "2007-05-01",
    "2007",
    "19.906",
    "-75.207",
    "Runway 10-28, Naval Station Guantanamo Bay, Cuba (USASpending PoP Cuba).",
    "usaspending_knik_gtmo_runway_20070501",
    "RUNWAY 10-28",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945007C1257_9700_-NONE-_-NONE-/",
    "Actor: Knik Construction Co., Inc. (U.S.) under NAVFAC — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "rb_degetau_hurricane_recovery_2019",
    "infrastructure",
    "engineering_epc",
    "us",
    "R.B. Construction Group, Inc. — GSA Federico Degetau Federal Building hurricane recovery",
    "Puerto Rico",
    "16 Jul 2019: GSA awards contract 47PC0319C0006 to R.B. Construction Group, Inc. for Puerto Rico hurricane recovery construction at the Federico Degetau Federal Building, Ruiz-Nazario U.S. Courthouse, Rainforest Kids Child Development Center, and federal parking garage in Hato Rey, San Juan; obligated USD 25,120,614.18. Distinct from R.B. Fort Buchanan Readiness Center and Conti Fort Buchanan range ops building.",
    "25120614.18",
    "2019-07-16",
    "2019",
    "18.430",
    "-66.070",
    "Federico Degetau Federal Building / Hato Rey federal complex, San Juan, Puerto Rico (USASpending PoP San Juan).",
    "usaspending_rb_degetau_20190716",
    "CONSTRUCTION SERVICES FOR THE PUERTO RICO HURRICANE RECOVERY PROJECT AT THE FEDERICO DEGETAU FEDERAL BUILDING, RUIZ-NAZARIO U.S. COURTHOUSE, RAINFOREST KIDS CHILD DEVELOPMENT CENTER, AND FEDERAL PARKING GARAGE IN HATO REY, SAN JUAN, P.R.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_47PC0319C0006_4740_-NONE-_-NONE-/",
    "Actor: R.B. Construction Group, Inc. (U.S.) under GSA — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "consigli_ceiba_afrc_2009",
    "infrastructure",
    "engineering_epc",
    "us",
    "Consigli Construction Co., Inc. — USACE Armed Forces Reserve Center (Ceiba)",
    "Puerto Rico",
    "4 Sep 2009: USACE awards contract W912QR09C0077 to Consigli Construction Co., Inc. for Armed Forces Reserve Center, Ceiba, Puerto Rico; obligated USD 24,110,204.40. Distinct from Conti Fort Buchanan range ops building and F&R Fort Buchanan ASTB barracks.",
    "24110204.40",
    "2009-09-04",
    "2009",
    "18.235",
    "-65.650",
    "Armed Forces Reserve Center, Ceiba Municipality, Puerto Rico (USASpending PoP Ceiba).",
    "usaspending_consigli_ceiba_20090904",
    "ARMED FORCES RESERVE CENTER, CEIBA, PR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QR09C0077_9700_-NONE-_-NONE-/",
    "Actor: Consigli Construction Co., Inc. (U.S.) under USACE — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "cscg_mayaguez_cbp_2022",
    "infrastructure",
    "engineering_epc",
    "us",
    "CSCG Inc. — CBP Mayagüez Marine Unit admin / boat maintenance hangar (Cabo Rojo)",
    "Puerto Rico",
    "30 Sep 2022: GSA awards contract 47PA0322C0015 to CSCG Inc. for CBP Mayagüez Marine Unit new construction of administrative building, boat maintenance, storage hangar and exterior vehicle parking at Boquerón, Cabo Rojo; obligated USD 23,641,673.35. Distinct from USCG San Juan FRC / Pier Echo packages.",
    "23641673.35",
    "2022-09-30",
    "2022",
    "18.015",
    "-67.170",
    "CBP Mayagüez Marine Unit / Boquerón, Cabo Rojo Municipality, Puerto Rico (USASpending PoP Cabo Rojo).",
    "usaspending_cscg_mayaguez_cbp_20220930",
    "CBP MAYAGUEZ MARINE UNIT NEW CONSTRUCTION OF ADMINISTRATIVE BUILDING, BOAT MAINTENANCE, STORAGE HANGAR AND EXTERIOR VEHICLE PARKING SPACES LOCATED AT PR KM, 18.5 BOQUERON, CABO ROJO, PR 00623",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_47PA0322C0015_4740_-NONE-_-NONE-/",
    "Actor: CSCG Inc. (U.S.) under GSA/CBP — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "fr_buchanan_astb_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "F & R Construction Group Inc — USACE Advanced Skills Training Barracks (Fort Buchanan)",
    "Puerto Rico",
    "11 Sep 2025: USACE awards contract W912QR25CA024 to F & R Construction Group Inc for construction of an Advanced Skills Training Barracks (ASTB) at Fort Buchanan, Puerto Rico; obligated USD 22,274,323.87. Distinct from Conti Fort Buchanan range ops building and R.B. Fort Buchanan Readiness Center.",
    "22274323.87",
    "2025-09-11",
    "2025",
    "18.415",
    "-66.122",
    "Advanced Skills Training Barracks, Fort Buchanan, Guaynabo / San Juan metro, Puerto Rico (USASpending PoP Fort Buchanan).",
    "usaspending_fr_buchanan_astb_20250911",
    "CONSTRUCTION OF AN ADVANCED SKILLS TRAINING BARRACKS (ASTB) AT FORT BUCHANAN, PUERTO RICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QR25CA024_9700_-NONE-_-NONE-/",
    "Actor: F & R Construction Group Inc (Puerto Rico / U.S.) under USACE — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
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
        "hunt_res_balsa": "Cycle 128: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 128: equal budget; ZPMC dense (miss).",
        "hunt_infra_building_materials": "Cycle 128: equal budget; Caribbean Lumber dense (miss).",
        "hunt_res_lithium": "Cycle 128: equal budget; Ganfeng dense (miss).",
        "hunt_res_nickel": "Cycle 128: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_latam_rail_telecom": "Cycle 128: equal budget; CRRC dense (miss).",
        "hunt_energy_fission_smr": "Cycle 128: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_energy_wind": "Cycle 128: equal budget; Goldwind dense (miss).",
        "hunt_energy_other_renewables": "Cycle 128: equal budget; Sungrow/Trina BESS dense (miss).",
        "hunt_res_copper": "Cycle 128: equal budget; CMOC dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 128: logged knik_gtmo_runway_2007 + rb_degetau_hurricane_recovery_2019 + consigli_ceiba_afrc_2009 + cscg_mayaguez_cbp_2022 + fr_buchanan_astb_2025.",
        "hunt_res_water": "Cycle 128: equal budget; Barbados/Santo Domingo/GTMO water dense (miss).",
        "hunt_fenb_araxa": "Cycle 128: equal budget; CBMM dense (miss).",
        "hunt_res_graphite": "Cycle 128: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_infra_port_ownership": "Cycle 128: equal budget; COSCO/APM dense (miss).",
        "hunt_br_power_equip": "Cycle 128: equal budget; NRECA Caracol / State Grid dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 128: equal budget; CRBC Saramacca dense (miss).",
        "hunt_energy_solar": "Cycle 128: equal budget; PowerChina solar dense (miss). PRC OEM/regulator pass dry this cycle.",
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
    print("Cycle 128 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
