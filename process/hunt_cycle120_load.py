#!/usr/bin/env python3
"""Cycle 120 hunt: shuffle_seed=20261120; equal budget; U.S./PRC split; thin after.

Order: port_ownership, other_renewables, wind, engineering_epc, graphite,
lithium, copper, nickel, port_cranes, niobium, rail, fission_smr,
bridges_roads, balsa, building_materials, water, power_plants_grid, solar.
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


def fhwa(rid, counterpart, asset, value, fx_date, year, lat, lon, geo, source_id, quote, url, note):
    A(
        {
            "id": rid,
            "layer": "infrastructure",
            "subcategory": "bridges_roads",
            "side": "us",
            "counterpart": counterpart,
            "country": "Puerto Rico",
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
            "supports": [rid, "hunt_infra_bridges_roads"],
        },
    )


fhwa(
    "design_build_ciales_branch2_2017",
    "Design Build LLC — FHWA FEMA Branch 2 emergency landslide repairs (Ciales)",
    "28 Nov 2017: FHWA awards contract 693C7318C000021 to Design Build, LLC for emergency repairs in multiple sites within FEMA Branch 2 geographical limits, including landslide repairs; obligated USD 6,817,940.00; place of performance Ciales. Distinct from Santiago Utuado Branch 2 package.",
    "6817940.00",
    "2017-11-28",
    "2017",
    "18.335",
    "-66.470",
    "FEMA Branch 2 emergency-repair corridor, Ciales Municipality, Puerto Rico (USASpending PoP Ciales).",
    "usaspending_design_build_ciales_20171128",
    "THE WORK CONSISTS OF PERFORMING EMERGENCY REPAIRS IN MULTIPLE SITES WITHIN THE GEOGRAPHICAL LIMITS OF FEMA BRANCH 2, INCLUDING, BUT NOT LIMITED TO LANDSLIDE REPAIRS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7318C000021_6925_-NONE-_-NONE-/",
    "Actor: Design Build, LLC (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
)

fhwa(
    "melendez_coamo_branch4_2017",
    "Constructora I Melendez LLC — FHWA FEMA Branch 4 emergency landslide repairs (Coamo)",
    "28 Nov 2017: FHWA awards contract 693C7318C000023 to Constructora I Melendez LLC for emergency repairs in multiple sites within FEMA Branch 4 geographical limits, including landslide repairs; obligated USD 4,528,696.96; place of performance Coamo. Distinct from Del Valle Mercedita Branch 4 package.",
    "4528696.96",
    "2017-11-28",
    "2017",
    "18.080",
    "-66.360",
    "FEMA Branch 4 emergency-repair corridor, Coamo Municipality, Puerto Rico (USASpending PoP Coamo).",
    "usaspending_melendez_coamo_20171128",
    "THE WORK CONSISTS OF PERFORMING EMERGENCY REPAIRS IN MULTIPLE SITES WITHIN THE GEOGRAPHICAL LIMITS OF FEMA BRANCH 4, INCLUDING, BUT NOT LIMITED TO LANDSLIDE REPAIRS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7318C000023_6925_-NONE-_-NONE-/",
    "Actor: Constructora I Melendez LLC (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
)

fhwa(
    "lpcd_caguas_branch3_2017",
    "LP C & D Inc — FHWA FEMA Branch 3 emergency landslide repairs (Caguas)",
    "27 Nov 2017: FHWA awards contract 693C7318C000019 to LP C & D Inc for emergency repairs in multiple sites within FEMA Branch 3 geographical limits, including landslide repairs; obligated USD 4,303,500.00; place of performance Caguas. Distinct from LP C&D El Yunque PR-930 and Route 9966 awards.",
    "4303500.00",
    "2017-11-27",
    "2017",
    "18.235",
    "-66.035",
    "FEMA Branch 3 emergency-repair corridor, Caguas Municipality, Puerto Rico (USASpending PoP Caguas).",
    "usaspending_lpcd_caguas_20171127",
    "THE WORK CONSISTS OF PERFORMING EMERGENCY REPAIRS IN MULTIPLE SITES WITHIN THE GEOGRAPHICAL LIMITS OF FEMA BRANCH 3, INCLUDING, BUT NOT LIMITED TO LANDSLIDE REPAIRS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7318C000019_6925_-NONE-_-NONE-/",
    "Actor: LP C & D Inc (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
)

fhwa(
    "santiago_utuado_branch2_2017",
    "Constructora Santiago II Corp — FHWA FEMA Branch 2 emergency landslide repairs (Utuado)",
    "27 Nov 2017: FHWA awards contract 693C7318C000016 to Constructora Santiago II Corp for emergency repairs in multiple sites within FEMA Branch 2 geographical limits, including landslide repairs; obligated USD 3,715,705.91; place of performance Utuado. Distinct from Design Build Ciales Branch 2 and Nieves Ángeles packages.",
    "3715705.91",
    "2017-11-27",
    "2017",
    "18.265",
    "-66.700",
    "FEMA Branch 2 emergency-repair corridor, Utuado Municipality, Puerto Rico (USASpending PoP Utuado).",
    "usaspending_santiago_utuado_20171127",
    "THE WORK CONSISTS OF PERFORMING EMERGENCY REPAIRS IN MULTIPLE SITES WITHIN THE GEOGRAPHICAL LIMITS OF FEMA BRANCH 2, INCLUDING, BUT NOT LIMITED TO LANDSLIDE REPAIRS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7318C000016_6925_-NONE-_-NONE-/",
    "Actor: Constructora Santiago II Corp (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
)

fhwa(
    "lagan_vieques_roads_2007",
    "Lagan Puerto Rico LLC — FHWA Vieques aggregate road and drainage repairs",
    "30 Aug 2007: FHWA awards contract DTFH7107C00032 to Lagan Puerto Rico LLC for repair of existing aggregate surfaced roads and drainage features, Vieques; obligated USD 5,683,326.70. Distinct from Aluma Camp Garcia / Red Beach asphalt resurfacing.",
    "5683326.70",
    "2007-08-30",
    "2007",
    "18.130",
    "-65.440",
    "Aggregate road / drainage repairs, Vieques Municipality, Puerto Rico (USASpending PoP Vieques).",
    "usaspending_lagan_vieques_20070830",
    "REPAIR OF EXISTING AGGREGATE SURFACED ROADS AND DRAINAGE FEATURES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_DTFH7107C00032_6925_-NONE-_-NONE-/",
    "Actor: Lagan Puerto Rico LLC under FHWA — us. Official USASpending Award API.",
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
        "hunt_infra_port_ownership": "Cycle 120: equal budget; COSCO/APM dense (miss).",
        "hunt_energy_other_renewables": "Cycle 120: equal budget; Sungrow summit/product-only pass dry (miss).",
        "hunt_energy_wind": "Cycle 120: equal budget; Goldwind dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 120: equal budget; OBO backlog exhausted (miss).",
        "hunt_res_graphite": "Cycle 120: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_res_lithium": "Cycle 120: equal budget; Ganfeng dense (miss).",
        "hunt_res_copper": "Cycle 120: equal budget; CMOC dense (miss).",
        "hunt_res_nickel": "Cycle 120: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 120: equal budget; ZPMC dense (miss).",
        "hunt_fenb_araxa": "Cycle 120: equal budget; CBMM dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 120: equal budget; CRRC dense (miss).",
        "hunt_energy_fission_smr": "Cycle 120: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_infra_bridges_roads": "Cycle 120: logged design_build_ciales_branch2_2017 + melendez_coamo_branch4_2017 + lpcd_caguas_branch3_2017 + santiago_utuado_branch2_2017 + lagan_vieques_roads_2007.",
        "hunt_res_balsa": "Cycle 120: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_infra_building_materials": "Cycle 120: equal budget; Caribbean Lumber dense (miss).",
        "hunt_res_water": "Cycle 120: equal budget; Lares/Ponce USACE dense (miss).",
        "hunt_br_power_equip": "Cycle 120: equal budget; State Grid/EXIM dense (miss).",
        "hunt_energy_solar": "Cycle 120: equal budget; Sungrow Vista Alegre dense (miss).",
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
    print("Cycle 120 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
