#!/usr/bin/env python3
"""Cycle 126 hunt: shuffle_seed=20261126; equal budget; U.S./PRC split; thin after.

Order: port_ownership, niobium, fission_smr, copper, lithium, rail,
power_plants_grid, water, balsa, bridges_roads, engineering_epc,
building_materials, other_renewables, graphite, nickel, port_cranes, solar, wind.
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
    investment_type="epc",
    evidence="documented",
    chicago=None,
    bib_type="government",
    annotation=None,
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
            "investment_type": investment_type,
            "value": value,
            "currency": "USD",
            "value_usd": value,
            "fx_usd": "1" if value else "",
            "fx_date": fx_date if value else "",
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": evidence,
            "source_id": source_id,
            "note": note,
        },
        {
            "id": rid,
            "retrieved": "2026-10-02",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": evidence,
            "quote": quote,
            "note": f"Opened primary source for {rid}.",
        },
        {
            "id": source_id,
            "type": bib_type,
            "chicago": chicago
            or f"U.S. Department of the Treasury, USAspending.gov. Award supporting {rid}. Signed {fx_date}. {url}.",
            "url": url,
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


row_doc(
    "powerchina_barbados_water_infra_2025",
    "resources",
    "water",
    "prc",
    "POWERCHINA — Barbados Water Infrastructure Project (Haymans Pump Station handover)",
    "Barbados",
    "13 Feb 2025: POWERCHINA hands over No. 5 Haymans Pump Station of the Barbados Water Infrastructure Project to the Barbados Water Authority after renovation/restoration. Project commenced 19 Feb 2024 (15-month contract): generators, turbidity control, and renovation/reconstruction of pump stations and water tanks at 11 sites including Bowmanston, Cave Hill, and Pool Gully. CapEx USD not disclosed. Distinct from Dick USACE dams PR and Río Puerto Nuevo water rows.",
    "",
    "",
    "2025",
    "13.200",
    "-59.640",
    "No. 5 Haymans Pump Station / Barbados Water Authority sites (company geography; approximate St. James / Haymans pin).",
    "powerchina_barbados_water_20250221",
    "On Feb 13, the No 5 Haymans Pump Station of the Barbados Water Infrastructure Project, undertaken by POWERCHINA, completed all renovation and restoration work and was handed over to the Barbados Water Authority.",
    "https://en.powerchina.cn/2025-02/21/c_828872.htm",
    "Actor: POWERCHINA (PRC SOE) EPC — prc; owner Barbados Water Authority. Company English primary. CapEx blank.",
    "hunt_res_water",
    chicago="POWERCHINA. “Barbados water infrastructure project handed over.” 21 February 2025. https://en.powerchina.cn/2025-02/21/c_828872.htm.",
    bib_type="company",
    annotation="POWERCHINA English primary on Barbados Water Infrastructure / Haymans handover. CapEx not stated. Supports powerchina_barbados_water_infra_2025.",
)

row_doc(
    "powerchina_tepuy_pv_108mw_2024",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Tepuy 108 MW PV plant handover (EPM Colombia)",
    "Colombia",
    "10 Oct 2024 handover (company 14 Oct): POWERCHINA-constructed 108 MW DC Tepuy Photovoltaic Plant in Colombia receives temporary acceptance from owner Empresas Públicas de Medellín (EPM); construction from 6 Mar 2023; full-capacity grid connection 22 Mar 2024; commercial operation 12 Jun 2024; ~224 GWh/y expected. CapEx USD not disclosed. Distinct from Ecopetrol Cartagena 23 MW / Guayepo / Escobares Colombia solar rows.",
    "",
    "",
    "2024",
    "5.070",
    "-75.520",
    "Tepuy PV Plant, Colombia (EPM project; approximate Antioquia / Medellín-region pin).",
    "powerchina_tepuy_20241014",
    "The 108-megawatt Tepuy Photovoltaic (PV) Plant Project in Colombia, constructed by POWERCHINA, was officially handed over on October 10th and received a temporary acceptance certificate from the owners.",
    "https://en.powerchina.cn/2024-10/14/c_828797.htm",
    "Actor: POWERCHINA (PRC SOE) EPC — prc; owner EPM. Company English primary. CapEx blank.",
    "hunt_energy_solar",
    chicago="POWERCHINA. “Colombian Tepuy PV project handed over.” 14 October 2024. https://en.powerchina.cn/2024-10/14/c_828797.htm.",
    bib_type="company",
    annotation="POWERCHINA English primary on Tepuy 108 MW handover to EPM. CapEx not stated. Supports powerchina_tepuy_pv_108mw_2024.",
)

row_doc(
    "aecom_gtmo_fuel_pier_2013",
    "infrastructure",
    "engineering_epc",
    "us",
    "AECOM Construction, Inc. — NAVFAC replace fuel pier / truckload facility (GTMO)",
    "Cuba",
    "3 Oct 2013: Department of the Navy awards task order JM01 under IDIQ to AECOM Construction, Inc. to replace fuel pier / truckload facility at Naval Station Guantanamo Bay; obligated USD 33,252,668.00. Distinct from RQ Wharf Bravo structural repairs and GTMO solid waste facility.",
    "33252668.00",
    "2013-10-03",
    "2013",
    "19.910",
    "-75.160",
    "Fuel pier / truckload facility, Naval Station Guantanamo Bay, Cuba (USASpending PoP Cuba).",
    "usaspending_aecom_gtmo_fuel_pier_20131003",
    "REPLACE FUEL PIER/TUCKLOAD FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_JM01_9700_N6274209D1174_9700/",
    "Actor: AECOM Construction, Inc. (U.S. HQ) under NAVFAC — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "v2x_gtmo_potable_water_2025",
    "resources",
    "water",
    "us",
    "V2X Systems LLC — NAVFAC potable water to leeward side NS Guantanamo Bay",
    "Cuba",
    "4 Sep 2025: Department of the Navy awards task order N6945025F1270 to V2X Systems LLC for potable water to the leeward side of Naval Station Guantanamo Bay; obligated USD 19,650,626.00. Distinct from RQ GTMO solid waste / Wharf Bravo facility construction awards.",
    "19650626.00",
    "2025-09-04",
    "2025",
    "19.900",
    "-75.150",
    "Leeward-side potable water works, Naval Station Guantanamo Bay, Cuba (USASpending PoP Cuba).",
    "usaspending_v2x_gtmo_water_20250904",
    "POTABLE WATER TO LEEWARD SIDE OF NSGB",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945025F1270_9700_N6274224D3506_9700/",
    "Actor: V2X Systems LLC (U.S.) under NAVFAC — us. Official USASpending Award API.",
    "hunt_res_water",
)

row_doc(
    "islands_mechanical_migrant_ops_2007",
    "infrastructure",
    "engineering_epc",
    "us",
    "Islands Mechanical Contractor, Inc. — NAVFAC migrant operations complex D/B (GTMO)",
    "Cuba",
    "7 May 2007: Department of the Navy awards contract N6945007C3313 to Islands Mechanical Contractor, Inc. for design-build construction of migrant operations complex at Naval Station Guantanamo Bay; obligated USD 16,577,967.00. Distinct from RQ GTMO barracks / solid waste / Wharf Bravo awards.",
    "16577967.00",
    "2007-05-07",
    "2007",
    "19.915",
    "-75.125",
    "Migrant operations complex, Naval Station Guantanamo Bay, Cuba (USASpending PoP Cuba).",
    "usaspending_islands_mech_migrant_20070507",
    "DESIGN BUILD CONSTRUCTION OF MIGRANT OPERATIONS COMPLEX",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945007C3313_9700_-NONE-_-NONE-/",
    "Actor: Islands Mechanical Contractor, Inc. (U.S.) under NAVFAC — us. Official USASpending Award API.",
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
        "hunt_infra_port_ownership": "Cycle 126: equal budget; COSCO/APM dense (miss).",
        "hunt_fenb_araxa": "Cycle 126: equal budget; CBMM dense (miss).",
        "hunt_energy_fission_smr": "Cycle 126: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_res_copper": "Cycle 126: equal budget; CMOC dense (miss).",
        "hunt_res_lithium": "Cycle 126: equal budget; Ganfeng dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 126: equal budget; CRRC dense (miss).",
        "hunt_br_power_equip": "Cycle 126: equal budget; Perini Haiti / State Grid dense (miss).",
        "hunt_res_water": "Cycle 126: logged powerchina_barbados_water_infra_2025 + v2x_gtmo_potable_water_2025.",
        "hunt_res_balsa": "Cycle 126: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_infra_bridges_roads": "Cycle 126: equal budget; FHWA/CRBC dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 126: logged aecom_gtmo_fuel_pier_2013 + islands_mechanical_migrant_ops_2007.",
        "hunt_infra_building_materials": "Cycle 126: equal budget; Caribbean Lumber dense (miss).",
        "hunt_energy_other_renewables": "Cycle 126: equal budget; Sungrow/Trina BESS dense (miss).",
        "hunt_res_graphite": "Cycle 126: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_res_nickel": "Cycle 126: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 126: equal budget; ZPMC dense (miss).",
        "hunt_energy_solar": "Cycle 126: logged powerchina_tepuy_pv_108mw_2024.",
        "hunt_energy_wind": "Cycle 126: equal budget; Goldwind dense (miss).",
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
    print("Cycle 126 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
