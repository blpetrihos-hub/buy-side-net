#!/usr/bin/env python3
"""Cycle 125 hunt: shuffle_seed=20261125; equal budget; U.S./PRC split; thin after.

Order: engineering_epc, balsa, power_plants_grid, water, fission_smr,
building_materials, nickel, port_cranes, lithium, rail, niobium, wind,
other_renewables, bridges_roads, copper, solar, graphite, port_ownership.
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
    "rq_gtmo_solid_waste_2019",
    "infrastructure",
    "engineering_epc",
    "us",
    "RQ Construction LLC — NAVFAC solid waste facility NS Guantanamo Bay",
    "Cuba",
    "19 Sep 2019: Department of the Navy awards contract N6945019C0501 to RQ Construction, LLC for solid waste facility at Naval Station Guantanamo Bay, Cuba; obligated USD 59,960,875.40. Distinct from RQ GTMO JTF barracks and Wharf Bravo structural repairs.",
    "59960875.40",
    "2019-09-19",
    "2019",
    "19.915",
    "-75.125",
    "Solid waste facility, Naval Station Guantanamo Bay, Cuba (USASpending PoP Cuba).",
    "usaspending_rq_gtmo_solid_waste_20190919",
    "SOLID WASTE FACILITY, NS GUANTANAMO BAY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945019C0501_9700_-NONE-_-NONE-/",
    "Actor: RQ Construction (Carlsbad CA HQ) under NAVFAC — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "rq_gtmo_wharf_bravo_2016",
    "infrastructure",
    "engineering_epc",
    "us",
    "RQ Construction LLC — NAVFAC Wharf Bravo structural repairs Phase 1 (GTMO)",
    "Cuba",
    "22 Nov 2016: Department of the Navy awards contract N6945017C1303 to RQ Construction, LLC for Wharf Bravo structural repairs Phase 1 at Naval Station Guantanamo Bay; obligated USD 38,897,745.01. Distinct from RQ GTMO solid waste facility and JTF barracks.",
    "38897745.01",
    "2016-11-22",
    "2016",
    "19.910",
    "-75.160",
    "Wharf Bravo, Naval Station Guantanamo Bay, Cuba (USASpending PoP Cuba).",
    "usaspending_rq_gtmo_wharf_bravo_20161122",
    "WHARF BRAVO STRUCTURAL REPAIRS - PHASE 1, NS GUANTANAMO BAY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945017C1303_9700_-NONE-_-NONE-/",
    "Actor: RQ Construction (Carlsbad CA HQ) under NAVFAC — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "eterna_soto_cano_hangar_2021",
    "infrastructure",
    "engineering_epc",
    "us",
    "Eterna S.A. de C.V. — USACE aircraft MX hangar Soto Cano Air Base",
    "Honduras",
    "29 Sep 2021: USACE awards contract W9127821C0039 to Empresa de Construccion y Transporte Eterna S.A. de C.V. for aircraft maintenance hangar at Soto Cano Air Base (SCAB), Honduras; obligated USD 39,227,935.67. Distinct from CCE Soto Cano barracks and Eterna aviation storage facility award.",
    "39227935.67",
    "2021-09-29",
    "2021",
    "14.382",
    "-87.621",
    "Aircraft MX hangar, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_soto_hangar_20210929",
    "AIRCRAFT MX HANGAR SCAB",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821C0039_9700_-NONE-_-NONE-/",
    "Actor: Eterna under USACE award for U.S. forces facilities — coded us (consistent with USACE Soto Cano / GTMO rows). Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "eterna_soto_cano_aviation_storage_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Eterna S.A. de C.V. — USACE aviation storage facility Soto Cano Air Base",
    "Honduras",
    "17 Jul 2025: USACE awards contract W9127825CA006 to Empresa de Construccion y Transporte Eterna S.A. de C.V. for design-bid-build construction of an aviation storage facility for use by U.S. forces at Soto Cano Air Base, Honduras; obligated USD 37,652,953.78. Distinct from Eterna aircraft MX hangar and CCE Soto Cano barracks.",
    "37652953.78",
    "2025-07-17",
    "2025",
    "14.382",
    "-87.621",
    "Aviation storage facility, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_soto_storage_20250717",
    "DESIGN-BID-BUILD (DBB) CONSTRUCTION CONTRACT USING FULL AND OPEN COMPETITION FOR THE CONSTRUCTION OF AN AVIATION STORAGE FACILITY FOR USE BY U.S. FORCES LOCATED AT SOTO CANO AIR BASE IN HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825CA006_9700_-NONE-_-NONE-/",
    "Actor: Eterna under USACE award for U.S. forces facilities — coded us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "powerchina_ecopetrol_cartagena_23mw_2024",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Ecopetrol Cartagena Refinery 23 MW solar park",
    "Colombia",
    "12 Apr 2024 completion ceremony (company 15 Apr release): POWERCHINA-built 23 MW solar park at Ecopetrol Cartagena Refinery — first of its kind within a Latin American refinery area; expected 34.29 GWh/y to the refinery; President Petro attended. CapEx USD not disclosed on opened PowerChina page. Distinct from Guayepo III / Escobares / Francisco Juana Colombia solar rows.",
    "",
    "",
    "2024",
    "10.320",
    "-75.510",
    "Cartagena Refinery solar park, Cartagena / Bolívar, Colombia (company geography; approximate pin).",
    "powerchina_ecopetrol_cartagena_20240415",
    "The completion ceremony for the 23-megawatt solar park, built by POWERCHINA in Colombia, was held on April 12. ... The solar park has a total installed capacity of 23MW and, upon completion it will supply 34.29 gigawatt-hours of clean energy annually to the Cartagena Refinery.",
    "https://en.powerchina.cn/2024-04/15/c_828692.htm",
    "Actor: POWERCHINA (PRC SOE) EPC — prc; offtaker/site Ecopetrol Cartagena Refinery. Company English primary. CapEx blank.",
    "hunt_energy_solar",
    chicago="POWERCHINA. “Colombian president witnesses completion of solar park.” 15 April 2024. https://en.powerchina.cn/2024-04/15/c_828692.htm.",
    bib_type="company",
    annotation="POWERCHINA English primary on Ecopetrol Cartagena 23 MW solar completion. CapEx not stated. Supports powerchina_ecopetrol_cartagena_23mw_2024.",
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
        "hunt_infra_engineering_epc": "Cycle 125: logged rq_gtmo_solid_waste_2019 + rq_gtmo_wharf_bravo_2016 + eterna_soto_cano_hangar_2021 + eterna_soto_cano_aviation_storage_2025.",
        "hunt_res_balsa": "Cycle 125: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_br_power_equip": "Cycle 125: equal budget; Perini Haiti / State Grid dense (miss).",
        "hunt_res_water": "Cycle 125: equal budget; Dick/Río Puerto Nuevo dense (miss).",
        "hunt_energy_fission_smr": "Cycle 125: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_infra_building_materials": "Cycle 125: equal budget; Caribbean Lumber dense (miss).",
        "hunt_res_nickel": "Cycle 125: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 125: equal budget; ZPMC dense (miss).",
        "hunt_res_lithium": "Cycle 125: equal budget; Ganfeng dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 125: equal budget; CRRC dense (miss).",
        "hunt_fenb_araxa": "Cycle 125: equal budget; CBMM dense (miss).",
        "hunt_energy_wind": "Cycle 125: equal budget; Goldwind dense (miss).",
        "hunt_energy_other_renewables": "Cycle 125: equal budget; Suriname microgrid dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 125: equal budget; FHWA/CRBC dense (miss).",
        "hunt_res_copper": "Cycle 125: equal budget; CMOC dense (miss).",
        "hunt_energy_solar": "Cycle 125: logged powerchina_ecopetrol_cartagena_23mw_2024.",
        "hunt_res_graphite": "Cycle 125: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_infra_port_ownership": "Cycle 125: equal budget; COSCO/APM dense (miss).",
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
    print("Cycle 125 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
