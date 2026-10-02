#!/usr/bin/env python3
"""Cycle 119 hunt: shuffle_seed=20261119; equal budget; U.S./PRC split; thin after.

Order: bridges_roads, other_renewables, balsa, rail, port_cranes, copper,
graphite, water, solar, engineering_epc, lithium, nickel, building_materials,
port_ownership, fission_smr, niobium, power_plants_grid, wind.
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
    "desarrolladora_culebrinas_bridge_2017",
    "Desarrolladora J.A. Inc — FHWA modular bridge over Culebrinas River (Moca)",
    "17 Nov 2017: FHWA awards contract 693C7318C000014 to Desarrolladora J.A. Inc for installation of modular bridge system over Culebrinas River plus landslide and low-water crossing repairs on PR-404, Municipality of Moca; obligated USD 4,751,153.24. Distinct from Del Valle Grande de Manatí modular bridge.",
    "4751153.24",
    "2017-11-17",
    "2017",
    "18.395",
    "-67.085",
    "Culebrinas River / PR-404 corridor, Moca Municipality, Puerto Rico (USASpending PoP Moca).",
    "usaspending_desarrolladora_culebrinas_20171117",
    "INSTALLATION OF MODULAR BRIDGE SYSTEM OVER CULEBRINAS RIVER, LANDSLIDE AND LOW WATER CROSSING REPAIRS ON PR-404, MUNICIPALITY OF MOCA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7318C000014_6925_-NONE-_-NONE-/",
    "Actor: Desarrolladora J.A. Inc (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
)

fhwa(
    "del_valle_manati_bridge_2017",
    "Del Valle Group LLC — FHWA modular bridge over Grande de Manatí River (Morovis)",
    "17 Nov 2017: FHWA awards contract 693C7318C000007 to Del Valle Group LLC for installation of modular bridge system over Grande de Manatí River on PR-567 km 11.70, Municipality of Morovis; obligated USD 4,539,319.25. Distinct from Desarrolladora Culebrinas modular bridge and Del Valle Río Puerto Nuevo walls.",
    "4539319.25",
    "2017-11-17",
    "2017",
    "18.325",
    "-66.405",
    "PR-567 / Grande de Manatí River crossing, Morovis Municipality, Puerto Rico (USASpending PoP Morovis).",
    "usaspending_del_valle_manati_20171117",
    "INSTALLATION OF MODULAR BRIDGE SYSTEM OVER GRANDE DE MANATI RIVER IN PR-567 KM. 11.70, MUNICIPALITY OF MOROVIS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7318C000007_6925_-NONE-_-NONE-/",
    "Actor: Del Valle Group LLC (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
)

fhwa(
    "lpcd_el_yunque_pr930_2018",
    "LP C & D Inc — FHWA PR-930 landslide repairs (El Yunque / Río Grande)",
    "3 Apr 2018: FHWA awards contract 693C7318C000036 to LP C & D Inc for three landslide repairs along PR-930 km 0.7 in El Yunque National Forest, Río Grande; obligated USD 4,668,125.00. Distinct from LP C&D Río Puerto Nuevo Margarita and Route 9966 retaining-wall awards.",
    "4668125.00",
    "2018-04-03",
    "2018",
    "18.320",
    "-65.790",
    "PR-930 km 0.7, El Yunque National Forest, Río Grande Municipality, Puerto Rico (USASpending PoP Río Grande).",
    "usaspending_lpcd_yunque_20180403",
    "THE WORK INVOLVES THREE LANDSLIDE REPAIRS ALONG PR-930 KM. 0.7 IN EL YUNQUE NATIONAL FOREST LOCATED IN RIO GRANDE, PUERTO RICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7318C000036_6925_-NONE-_-NONE-/",
    "Actor: LP C & D Inc (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
)

fhwa(
    "aluma_vieques_camp_garcia_2008",
    "Aluma Construction Corp — FHWA Camp Garcia / Red Beach access roads (Vieques)",
    "12 Sep 2008: FHWA awards contract DTFH7108C00032 to Aluma Construction Corporation for widening and resurfacing of Camp Garcia entrance road and Red Beach access road with asphalt concrete pavement, Vieques; obligated USD 6,783,308.88. Distinct from Maria Emergency Relief packages.",
    "6783308.88",
    "2008-09-12",
    "2008",
    "18.120",
    "-65.450",
    "Camp Garcia / Red Beach road corridor, Vieques Municipality, Puerto Rico (USASpending PoP Vieques).",
    "usaspending_aluma_vieques_20080912",
    "THE PROJECT CONSISTS OF THE WIDENING AND RESURFACING OF CAMP GARCIA ENTRANCE ROAD AND RED BEACH ACCESS ROAD WITH ASPHALT CONCRETE PAVEMENT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_DTFH7108C00032_6925_-NONE-_-NONE-/",
    "Actor: Aluma Construction Corporation (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
)

fhwa(
    "lpcd_route9966_wall_2012",
    "LP C & D Inc — FHWA Route 9966 H-pile retaining wall (Palmer)",
    "27 Aug 2012: FHWA awards contract DTFH7112C00036 to LP C & D Inc for partial removal of failed H-pile retaining wall and construction of a new H-pile retaining wall on Route 9966; obligated USD 3,594,145.39; place of performance Palmer. Distinct from LP C&D El Yunque PR-930 landslides.",
    "3594145.39",
    "2012-08-27",
    "2012",
    "18.365",
    "-65.770",
    "Route 9966 retaining wall, Palmer / Río Grande area, Puerto Rico (USASpending PoP Palmer).",
    "usaspending_lpcd_9966_20120827",
    "THIS PROJECT CONSISTS OF THE PARTIAL REMOVAL OF THE FAILED H-PILE RETAINING WALL AND THE CONSTRUCTION OF A NEW H-PILE RETAINING WALL ON ROUTE 9966",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_DTFH7112C00036_6925_-NONE-_-NONE-/",
    "Actor: LP C & D Inc (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
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
        "hunt_infra_bridges_roads": "Cycle 119: logged desarrolladora_culebrinas_bridge_2017 + del_valle_manati_bridge_2017 + lpcd_el_yunque_pr930_2018 + aluma_vieques_camp_garcia_2008 + lpcd_route9966_wall_2012 (FHWA residual).",
        "hunt_energy_other_renewables": "Cycle 119: equal budget; Trina/Jinko dense (miss).",
        "hunt_res_balsa": "Cycle 119: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_latam_rail_telecom": "Cycle 119: equal budget; CRRC dense (miss).",
        "hunt_infra_port_cranes": "Cycle 119: equal budget; ZPMC dense (miss).",
        "hunt_res_copper": "Cycle 119: equal budget; CMOC dense (miss).",
        "hunt_res_graphite": "Cycle 119: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_res_water": "Cycle 119: equal budget; Lares crib / Ponce cofferdam dense (miss).",
        "hunt_energy_solar": "Cycle 119: equal budget; Sungrow dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 119: equal budget; OBO backlog exhausted (miss).",
        "hunt_res_lithium": "Cycle 119: equal budget; Ganfeng dense (miss).",
        "hunt_res_nickel": "Cycle 119: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_infra_building_materials": "Cycle 119: equal budget; Caribbean Lumber dense (miss).",
        "hunt_infra_port_ownership": "Cycle 119: equal budget; COSCO dense (miss).",
        "hunt_energy_fission_smr": "Cycle 119: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_fenb_araxa": "Cycle 119: equal budget; CBMM dense (miss).",
        "hunt_br_power_equip": "Cycle 119: equal budget; State Grid/EXIM dense (miss).",
        "hunt_energy_wind": "Cycle 119: equal budget; Goldwind dense (miss).",
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
    print("Cycle 119 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
