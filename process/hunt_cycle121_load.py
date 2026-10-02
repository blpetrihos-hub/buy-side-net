#!/usr/bin/env python3
"""Cycle 121 hunt: shuffle_seed=20261121; equal budget; U.S./PRC split; thin after.

Order: building_materials, bridges_roads, wind, niobium, graphite, lithium,
fission_smr, rail, port_ownership, balsa, solar, port_cranes, nickel, water,
other_renewables, copper, engineering_epc, power_plants_grid.
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


def us_row(
    rid,
    layer,
    subcategory,
    counterpart,
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
    investment_type="epc",
):
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": "us",
            "counterpart": counterpart,
            "country": "Puerto Rico",
            "asset": asset,
            "investment_type": investment_type,
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
            "supports": [rid, f"hunt_{'infra' if layer == 'infrastructure' else 'res' if layer == 'resources' else 'energy'}_{subcategory}"],
        },
    )


us_row(
    "jose_carro_arecibo_branch2_2017",
    "infrastructure",
    "bridges_roads",
    "Construcciones Jose Carro S.E. — FHWA FEMA Branch 2 emergency repairs (Arecibo/Lares/Utuado)",
    "29 Nov 2017: FHWA awards contract 693C7318C000015 to Construcciones Jose Carro, S.E. for emergency repairs in multiple sites within FEMA Branch 2 geographical limits in the municipalities of Arecibo, Lares, and Utuado; obligated USD 5,864,133.66; place of performance Arecibo. Distinct from Design Build Ciales / Santiago Utuado Branch 2 packages.",
    "5864133.66",
    "2017-11-29",
    "2017",
    "18.472",
    "-66.716",
    "FEMA Branch 2 emergency-repair corridor, Arecibo Municipality, Puerto Rico (USASpending PoP Arecibo; work also Lares/Utuado).",
    "usaspending_jose_carro_arecibo_20171129",
    "THE WORK INVOLVES PERFORMING EMERGENCY REPAIRS IN MULTIPLE SITES WITHIN THE GEOGRAPHICAL LIMITS OF FEMA BRANCH 2 IN THE MUNICIPALITIES OF ARECIBO, LARES, AND UTUADO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7318C000015_6925_-NONE-_-NONE-/",
    "Actor: Construcciones Jose Carro, S.E. (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
)

us_row(
    "del_valle_mercedita_branch4_2017",
    "infrastructure",
    "bridges_roads",
    "Del Valle Group LLC — FHWA FEMA Branch 4 emergency repairs (Mercedita)",
    "27 Nov 2017: FHWA awards contract 693C7318C000018 to Del Valle Group LLC for emergency repairs in multiple sites within FEMA Branch 4 geographical limits; obligated USD 5,145,965.03; place of performance Mercedita. Distinct from Melendez Coamo / Desarrolladora J.A. Ciales Branch 4 packages.",
    "5145965.03",
    "2017-11-27",
    "2017",
    "18.010",
    "-66.563",
    "FEMA Branch 4 emergency-repair corridor, Mercedita / Ponce area, Puerto Rico (USASpending PoP Mercedita).",
    "usaspending_del_valle_mercedita_20171127",
    "THE WORK CONSISTS OF PERFORMING EMERGENCY REPAIRS IN MULTIPLE SITES WITHIN THE GEOGRAPHICAL LIMITS OF FEMA BRANCH 4",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7318C000018_6925_-NONE-_-NONE-/",
    "Actor: Del Valle Group LLC (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
)

us_row(
    "desarrolladora_ja_ciales_branch4_2017",
    "infrastructure",
    "bridges_roads",
    "Desarrolladora J.A. Inc — FHWA FEMA Branch 4 landslide / gabion repairs (Ciales)",
    "28 Nov 2017: FHWA awards contract 693C7318C000022 to Desarrolladora J.A. Inc for emergency repairs in multiple sites within FEMA Branch 4 geographical limits, including landslide repairs and construction of gabions; obligated USD 4,276,081.01; place of performance Ciales. Distinct from Del Valle Mercedita / Melendez Coamo Branch 4 packages.",
    "4276081.01",
    "2017-11-28",
    "2017",
    "18.336",
    "-66.469",
    "FEMA Branch 4 emergency-repair corridor, Ciales Municipality, Puerto Rico (USASpending PoP Ciales).",
    "usaspending_desarrolladora_ja_ciales_20171128",
    "THE WORK CONSISTS OF PERFORMING EMERGENCY REPAIRS IN MULTIPLE SITES WITHIN THE GEOGRAPHICAL LIMITS OF FEMA BRANCH 4, INCLUDING, BUT NOT LIMITED TO LANDSLIDE REPAIRS, CONSTRUCTION OF GABIO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_693C7318C000022_6925_-NONE-_-NONE-/",
    "Actor: Desarrolladora J.A. Inc (Puerto Rico / U.S.) under FHWA — us. Official USASpending Award API.",
)

us_row(
    "ch2m_uscg_frc_san_juan_2012",
    "infrastructure",
    "engineering_epc",
    "CH2M Hill Constructors, Inc. — USCG Sector San Juan Fast Response Cutter homeporting D/B",
    "14 Feb 2012: U.S. Coast Guard awards task order HSCG4712JA16002 to CH2M Hill Constructors, Inc. for design/build homeporting of Fast Response Cutters (FRC) at U.S. Coast Guard Sector San Juan; obligated USD 18,706,658.50; place of performance San Juan. Distinct from Tutor Perini San Juan FRC Phase II.",
    "18706658.50",
    "2012-02-14",
    "2012",
    "18.464",
    "-66.116",
    "U.S. Coast Guard Sector San Juan FRC homeport facilities, San Juan, Puerto Rico (USASpending PoP San Juan).",
    "usaspending_ch2m_uscg_frc_20120214",
    "DESIGN/BUILD FOR HOMEPORTING FAST RESPONSE CUTTERS (FRC) AT U. S. COAST GUARD SECTOR SAN JUAN, SAN JUAN, PUERTO RICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_HSCG4712JA16002_7008_HSCG4710D3EFK16_7008/",
    "Actor: CH2M Hill Constructors, Inc. (U.S.-HQ) under USCG — us. Official USASpending Award API.",
)

us_row(
    "tutor_perini_uscg_frc_p2_2013",
    "infrastructure",
    "engineering_epc",
    "Tutor Perini Corporation — USCG San Juan FRC Phase II",
    "9 Jul 2013: U.S. Coast Guard awards task order HSCG4713JA23002 to Tutor Perini Corporation for San Juan FRC Phase II homeporting works; obligated USD 7,487,441.26; place of performance San Juan. Distinct from CH2M Hill FRC homeporting design/build award.",
    "7487441.26",
    "2013-07-09",
    "2013",
    "18.464",
    "-66.116",
    "U.S. Coast Guard Sector San Juan FRC Phase II facilities, San Juan, Puerto Rico (USASpending PoP San Juan).",
    "usaspending_tutor_perini_uscg_frc_p2_20130709",
    "SAN JUAN FRC PHASE II",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_HSCG4713JA23002_7008_HSCG4709D3EFK23_7008/",
    "Actor: Tutor Perini Corporation (U.S.-HQ) under USCG — us. Official USASpending Award API.",
)

us_row(
    "contractor_jv_prarng_jtc_2022",
    "infrastructure",
    "engineering_epc",
    "4Contractor JV — USACE PRARNG Joint Training Center MILCON (Salinas)",
    "29 Aug 2022: USACE awards contract W912EP22C0008 to 4Contractor JV for design-bid-build construction in support of Puerto Rico Army National Guard (PRARNG) Joint Training Center military construction (MILCON) projects; obligated USD 294,110,596.60; place of performance Salinas. Distinct from USCG FRC homeporting and OBO NEC rows.",
    "294110596.60",
    "2022-08-29",
    "2022",
    "17.978",
    "-66.298",
    "PRARNG Joint Training Center MILCON site, Salinas Municipality, Puerto Rico (USASpending PoP Salinas).",
    "usaspending_4contractor_prarng_jtc_20220829",
    "DESIGN-BID-BUILD CONSTRUCTION CONTRACT IN SUPPORT OF PUERTO RICO ARMY NATIONAL GUARD (PRARNG) JOINT TRAINING CENTER MILITARY CONSTRUCTION (MILCON) PROJECTS, PUERTO RICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP22C0008_9700_-NONE-_-NONE-/",
    "Actor: 4Contractor JV under USACE Civil Works / MILCON award — coded us (U.S. federal award). Official USASpending Award API.",
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
        "hunt_infra_building_materials": "Cycle 121: equal budget; Caribbean Lumber dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 121: logged jose_carro_arecibo_branch2_2017 + del_valle_mercedita_branch4_2017 + desarrolladora_ja_ciales_branch4_2017.",
        "hunt_energy_wind": "Cycle 121: equal budget; Goldwind dense (miss).",
        "hunt_fenb_araxa": "Cycle 121: equal budget; CBMM dense (miss).",
        "hunt_res_graphite": "Cycle 121: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_res_lithium": "Cycle 121: equal budget; Ganfeng dense (miss).",
        "hunt_energy_fission_smr": "Cycle 121: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_latam_rail_telecom": "Cycle 121: equal budget; CRRC dense (miss).",
        "hunt_infra_port_ownership": "Cycle 121: equal budget; COSCO/APM dense (miss).",
        "hunt_res_balsa": "Cycle 121: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_energy_solar": "Cycle 121: equal budget; Sungrow dense (miss).",
        "hunt_infra_port_cranes": "Cycle 121: equal budget; ZPMC dense (miss).",
        "hunt_res_nickel": "Cycle 121: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_res_water": "Cycle 121: equal budget; Río Puerto Nuevo dense (miss).",
        "hunt_energy_other_renewables": "Cycle 121: equal budget; OEM product-only pass dry (miss).",
        "hunt_res_copper": "Cycle 121: equal budget; CMOC dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 121: logged ch2m_uscg_frc_san_juan_2012 + tutor_perini_uscg_frc_p2_2013 + contractor_jv_prarng_jtc_2022.",
        "hunt_br_power_equip": "Cycle 121: equal budget; State Grid/EXIM dense (miss).",
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
    print("Cycle 121 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
