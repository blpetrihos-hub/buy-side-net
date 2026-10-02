#!/usr/bin/env python3
"""Cycle 124 hunt: shuffle_seed=20261124; equal budget; U.S./PRC split; thin after.

Order: building_materials, copper, power_plants_grid, wind, other_renewables,
bridges_roads, niobium, fission_smr, solar, lithium, nickel, rail, balsa, water,
graphite, port_cranes, port_ownership, engineering_epc.
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
    "powerchina_sajalices_panama_530mw_2024",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Sajalices 530 MW PV EPC (Panama)",
    "Panama",
    "18 Dec 2024: POWERCHINA signs EPC contract with Sajalices Energy Co at POWERCHINA Americas regional HQ in Panama for the 530 MW Sajalices Photovoltaic Project — design, procurement, construction, installation, commissioning, trial operation, handover, performance testing, and defect rectification of the PV field, boosting station, and transmission lines. CapEx USD not disclosed on opened PowerChina page. Distinct from Conchagua El Salvador / Mauriti Brazil / Cauchari Argentina solar rows.",
    "",
    "",
    "2024",
    "8.650",
    "-79.820",
    "Sajalices Photovoltaic Project, Panama (company geography; approximate West Panama / Sajalices corridor pin).",
    "powerchina_sajalices_20241225",
    "On Dec 18, POWERCHINA met with Sajalices Energy Co at its regional headquarters in Panama to sign the EPC (engineering, procurement and construction) contract for the 530-megawatt Sajalices Photovoltaic Project.",
    "https://en.powerchina.cn/2024-12/25/c_828846.htm",
    "Actor: POWERCHINA (PRC SOE) EPC — prc; counterparty Sajalices Energy Co. Company English primary. CapEx blank.",
    "hunt_energy_solar",
    chicago="POWERCHINA. “POWERCHINA to develop solar power in Panama.” 25 December 2024. https://en.powerchina.cn/2024-12/25/c_828846.htm.",
    bib_type="company",
    annotation="POWERCHINA English primary on Sajalices 530 MW EPC signing. CapEx not stated. Supports powerchina_sajalices_panama_530mw_2024.",
)

row_doc(
    "cmf_great_inagua_opbat_2011",
    "infrastructure",
    "engineering_epc",
    "us",
    "Construction Management of Florida Inc. — USCG OPBAT hangar Great Inagua",
    "Bahamas",
    "9 Mar 2011: U.S. Coast Guard awards contract HSCG4710C3EFK08 to Construction Management of Florida Inc. to construct OPBAT hangar at Great Inagua, Bahamas; obligated USD 17,163,809.08. Distinct from USCG Borinquen hangar M&R and San Juan FRC homeporting awards.",
    "17163809.08",
    "2011-03-09",
    "2011",
    "20.975",
    "-73.670",
    "OPBAT hangar, Great Inagua, Bahamas (USASpending PoP Bahamas; Matthew Town / Inagua approximate).",
    "usaspending_cmf_inagua_20110309",
    "CONSTRUCT OPBAT HANGAR, GREAT INAGUA, BAHAMAS SFRL # 08-2648880",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_HSCG4710C3EFK08_7008_-NONE-_-NONE-/",
    "Actor: Construction Management of Florida Inc. (U.S.) under USCG — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "cce_soto_cano_barracks_2011",
    "infrastructure",
    "engineering_epc",
    "us",
    "Contracting, Consulting, Engineering LLC — USACE Soto Cano AFB barracks (Honduras)",
    "Honduras",
    "25 Aug 2011: USACE awards contract W9127811C0028 to Contracting, Consulting, Engineering LLC for FY11 barracks at Soto Cano Air Base, Honduras; obligated USD 15,608,435.27. Distinct from CCE Bogotá annex / Guayaquil NAB and Eterna Soto Cano housing award.",
    "15608435.27",
    "2011-08-25",
    "2011",
    "14.382",
    "-87.621",
    "Soto Cano Air Base barracks, Comayagua Department, Honduras (USASpending PoP Honduras).",
    "usaspending_cce_soto_cano_20110825",
    "FY11 BARRACKS AT SOTO CANO AFB HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811C0028_9700_-NONE-_-NONE-/",
    "Actor: Contracting, Consulting, Engineering LLC (U.S.) under USACE — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "perini_haiti_substations_2011",
    "energy",
    "power_plants_grid",
    "us",
    "Perini Management Services, Inc. — USAID Port-au-Prince five-substation rehab",
    "Haiti",
    "28 Jul 2011: USAID awards contract AID521C001100012 to Perini Management Services, Inc. to rehabilitate five substations in Port-au-Prince; obligated USD 14,910,475.00. Distinct from Fluor Haiti NEC and Perini Montevideo chancery renovation.",
    "14910475.00",
    "2011-07-28",
    "2011",
    "18.540",
    "-72.335",
    "Five substations, Port-au-Prince, Haiti (USASpending PoP Haiti / award description).",
    "usaspending_perini_haiti_subs_20110728",
    "THE PURPOSE OF THIS CONTRACT IS TO REHABILITATE FIVE SUBSTATIONS IN PORT AU PRINCE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C001100012_7200_-NONE-_-NONE-/",
    "Actor: Perini Management Services, Inc. (U.S.; Tutor Perini lineage) under USAID — us. Official USASpending Award API.",
    "hunt_br_power_equip",
)

row_doc(
    "cavagnero_pos_nec_bridging_2020",
    "infrastructure",
    "engineering_epc",
    "us",
    "Mark Cavagnero Associates — State Dept Port of Spain NEC bridging services",
    "Trinidad and Tobago",
    "15 Sep 2020: Department of State awards task order 19AQMM20F3492 to Mark Cavagnero Associates for bridging services for the New Embassy Campus (NEC) in Port of Spain, Trinidad & Tobago; obligated USD 14,498,552.70. Distinct from Caddell Port of Spain NEC construction award.",
    "14498552.70",
    "2020-09-15",
    "2020",
    "10.655",
    "-61.510",
    "U.S. Embassy Port of Spain NEC bridging / design services, Trinidad and Tobago (USASpending PoP).",
    "usaspending_cavagnero_pos_20200915",
    "BRIDGING SERVICES FOR THE NEW EMBASSY CAMPUS (NEC) IN PORT OF SPAIN, TRINIDAD&TOBAGO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F3492_1900_19AQMM19D0065_1900/",
    "Actor: Mark Cavagnero Associates (U.S. architecture/engineering) under State OBO — us. Official USASpending Award API.",
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
        "hunt_infra_building_materials": "Cycle 124: equal budget; Caribbean Lumber dense (miss).",
        "hunt_res_copper": "Cycle 124: equal budget; CMOC dense (miss).",
        "hunt_br_power_equip": "Cycle 124: logged perini_haiti_substations_2011.",
        "hunt_energy_wind": "Cycle 124: equal budget; Goldwind dense (miss).",
        "hunt_energy_other_renewables": "Cycle 124: equal budget; Suriname microgrid / Ormat dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 124: equal budget; FHWA/CRBC residual dense (miss).",
        "hunt_fenb_araxa": "Cycle 124: equal budget; CBMM dense (miss).",
        "hunt_energy_fission_smr": "Cycle 124: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_energy_solar": "Cycle 124: logged powerchina_sajalices_panama_530mw_2024.",
        "hunt_res_lithium": "Cycle 124: equal budget; Ganfeng dense (miss).",
        "hunt_res_nickel": "Cycle 124: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_latam_rail_telecom": "Cycle 124: equal budget; CRRC dense (miss).",
        "hunt_res_balsa": "Cycle 124: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_res_water": "Cycle 124: equal budget; Dick/Río Puerto Nuevo dense (miss).",
        "hunt_res_graphite": "Cycle 124: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 124: equal budget; ZPMC Kingston/Santos dense (miss).",
        "hunt_infra_port_ownership": "Cycle 124: equal budget; COSCO/APM dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 124: logged cmf_great_inagua_opbat_2011 + cce_soto_cano_barracks_2011 + cavagnero_pos_nec_bridging_2020.",
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
    print("Cycle 124 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
