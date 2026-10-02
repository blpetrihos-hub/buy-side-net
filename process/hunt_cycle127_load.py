#!/usr/bin/env python3
"""Cycle 127 hunt: shuffle_seed=20261127; equal budget; U.S./PRC split; thin after.

Order: engineering_epc, balsa, lithium, wind, solar, other_renewables,
port_ownership, graphite, bridges_roads, niobium, building_materials, water,
rail, fission_smr, power_plants_grid, nickel, copper, port_cranes.
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
    "crbc_saramacca_bridge_suriname_2025",
    "infrastructure",
    "bridges_roads",
    "prc",
    "CRBC / Kuldipsingh — Van't Hogerhuysstraat Bridge over Saramacca Canal (Paramaribo)",
    "Suriname",
    "Apr 2025 opening (CCCC 8 Apr release): Bridge of the Van't Hogerhuysstraat across the Saramacca Canal opens in Paramaribo; constructed by consortium of CRBC (CCCC subsidiary) and local Kuldipsingh Infra; 66 m span, six-lane dual carriageway, design load up to 50-tonne freight vehicles; construction began 26 Jan 2024. CapEx USD not disclosed. Distinct from CRBC Corentyne Lot 2 Guyana and CRCC Demerara bridge rows.",
    "",
    "",
    "2025",
    "5.825",
    "-55.170",
    "Van't Hogerhuysstraat / Saramacca Canal bridge, Paramaribo, Suriname (CCCC geography; approximate capital pin).",
    "cccc_crbc_saramacca_bridge_20250408",
    "Recently, the bridge of the Van't Hogerhuysstraat across the Saramacca Canal, was opened to traffic in Paramaribo, the capital of Suriname. ... The project is constructed by a consortium of CCCC's subsidiary CRBC and local company Kuldipsingh Infra. Spanning 66 meters, the bridge is a six-lane dual carriageway",
    "https://en.ccccltd.cn/xwzx/ywfb/202504/t20250411_219869.html",
    "Actor: CRBC / CCCC (PRC SOE) consortium lead — prc; local partner Kuldipsingh Infra. Company English primary. CapEx blank.",
    "hunt_infra_bridges_roads",
    chicago="China Communications Construction Company Ltd. “Surinamese President Chandrikapersad Santokhi, attends the opening ceremony of the Bridge of the Van't Hogerhuysstraat across the Saramacca Canal.” 8 April 2025. https://en.ccccltd.cn/xwzx/ywfb/202504/t20250411_219869.html.",
    bib_type="company",
    annotation="CCCC English primary on CRBC Saramacca Canal bridge opening. CapEx not stated. Supports crbc_saramacca_bridge_suriname_2025.",
)

row_doc(
    "nreca_caracol_power_2013",
    "energy",
    "power_plants_grid",
    "us",
    "NRECA International — USAID Caracol Power Plant O&M (PPSELD Haiti)",
    "Haiti",
    "30 Apr 2013: USAID awards contract AID521C1300007 to NRECA International for operation and management of the Caracol Power Plant through the Pilot Project for Sustainable Electricity Distribution (PPSELD); obligated USD 36,175,040.13. Distinct from Perini Port-au-Prince substation rehab and Fluor Haiti NEC.",
    "36175040.13",
    "2013-04-30",
    "2013",
    "19.735",
    "-72.015",
    "Caracol Power Plant / Caracol Industrial Park corridor, Nord-Est Department, Haiti (USASpending PoP Haiti; Caracol approximate).",
    "usaspending_nreca_caracol_20130430",
    "THE PURPOSE OF THIS REQUISITION IS TO REQUEST OAA TO AWARD A CONTRACT FOR THE OPERATION AND MANAGEMENT OF THE CARACOL POWER PLANT THROUGH THE PILOT PROJECT FOR SUSTAINABLE ELECTRICITY DISTRIBUTION (PPSELD).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1300007_7200_-NONE-_-NONE-/",
    "Actor: NRECA International (U.S. cooperative affiliate) under USAID — us. Official USASpending Award API.",
    "hunt_br_power_equip",
)

row_doc(
    "conti_buchanan_range_ops_2024",
    "infrastructure",
    "engineering_epc",
    "us",
    "Conti Federal Services, LLC — USACE Fort Buchanan USARC Army Range facility ops building",
    "Puerto Rico",
    "25 Sep 2024: USACE awards contract W912QR24C0031 to Conti Federal Services, LLC for USARC Fort Buchanan Army Range Facility Operations Building Base; obligated USD 32,469,608.20; place of performance Guaynabo. Distinct from R.B. Construction Fort Buchanan Readiness Center.",
    "32469608.20",
    "2024-09-25",
    "2024",
    "18.415",
    "-66.122",
    "Fort Buchanan USARC Army Range Facility Operations Building, Guaynabo, Puerto Rico (USASpending PoP Guaynabo).",
    "usaspending_conti_buchanan_range_20240925",
    "USARC FT. BUCHANAN ARMY RANGE FACILITY OPERATIONS BUILDING BASE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QR24C0031_9700_-NONE-_-NONE-/",
    "Actor: Conti Federal Services, LLC (U.S.) under USACE — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "orion_autec_pier_2021",
    "infrastructure",
    "engineering_epc",
    "us",
    "Orion Government Services LLC — NAVFAC AUTEC Facility 1902 permanent pier demo/repair (Andros)",
    "Bahamas",
    "16 Dec 2021: Department of the Navy awards contract N6945022C0006 to Orion Government Services LLC for AUTEC Facility 1902 permanent pier demolition and repair project at Andros Island, Bahamas; obligated USD 28,678,311.41. Distinct from Haskell AUTEC austere quarters and CMF Great Inagua OPBAT hangar.",
    "28678311.41",
    "2021-12-16",
    "2021",
    "24.700",
    "-77.770",
    "AUTEC Facility 1902 pier, Andros Island, Bahamas (USASpending PoP Bahamas; AUTEC approximate).",
    "usaspending_orion_autec_pier_20211216",
    "AUTEC FACILITY 1902 PERMANENT PIER DEMO AND REPAIR PROJECT AT ANDROS ISLAND BAHAMAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945022C0006_9700_-NONE-_-NONE-/",
    "Actor: Orion Government Services LLC (U.S.) under NAVFAC — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "rq_gtmo_mass_migration_2018",
    "infrastructure",
    "engineering_epc",
    "us",
    "RQ Construction LLC — NAVFAC Contingency Mass Migration Complex (GTMO)",
    "Cuba",
    "22 Feb 2018: Department of the Navy awards contract N6945018C1308 to RQ Construction, LLC for Contingency Mass Migration Complex at Naval Station Guantanamo Bay, Cuba; obligated USD 24,584,859.49. Distinct from Islands Mechanical migrant operations complex (2007) and RQ GTMO solid waste / Wharf Bravo / JTF barracks awards.",
    "24584859.49",
    "2018-02-22",
    "2018",
    "19.915",
    "-75.125",
    "Contingency Mass Migration Complex, Naval Station Guantanamo Bay, Cuba (USASpending PoP Cuba).",
    "usaspending_rq_gtmo_mass_mig_20180222",
    "CONTINGENCY MASS MIGRATION COMPLEX, NSGB, CUBA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945018C1308_9700_-NONE-_-NONE-/",
    "Actor: RQ Construction (Carlsbad CA HQ) under NAVFAC — us. Official USASpending Award API.",
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
        "hunt_infra_engineering_epc": "Cycle 127: logged conti_buchanan_range_ops_2024 + orion_autec_pier_2021 + rq_gtmo_mass_migration_2018.",
        "hunt_res_balsa": "Cycle 127: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_res_lithium": "Cycle 127: equal budget; Ganfeng dense (miss).",
        "hunt_energy_wind": "Cycle 127: equal budget; Goldwind dense (miss).",
        "hunt_energy_solar": "Cycle 127: equal budget; Sajalices/Tepuy/Cauchari dense (miss).",
        "hunt_energy_other_renewables": "Cycle 127: equal budget; Sungrow/Trina BESS dense (miss).",
        "hunt_infra_port_ownership": "Cycle 127: equal budget; COSCO/APM dense (miss).",
        "hunt_res_graphite": "Cycle 127: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_infra_bridges_roads": "Cycle 127: logged crbc_saramacca_bridge_suriname_2025.",
        "hunt_fenb_araxa": "Cycle 127: equal budget; CBMM dense (miss).",
        "hunt_infra_building_materials": "Cycle 127: equal budget; Caribbean Lumber dense (miss).",
        "hunt_res_water": "Cycle 127: equal budget; Barbados/Santo Domingo/GTMO water dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 127: equal budget; CRRC dense (miss).",
        "hunt_energy_fission_smr": "Cycle 127: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_br_power_equip": "Cycle 127: logged nreca_caracol_power_2013.",
        "hunt_res_nickel": "Cycle 127: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_res_copper": "Cycle 127: equal budget; CMOC dense (miss).",
        "hunt_infra_port_cranes": "Cycle 127: equal budget; ZPMC dense (miss).",
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
    print("Cycle 127 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
