#!/usr/bin/env python3
"""Cycle 123 hunt: shuffle_seed=20261123; equal budget; U.S./PRC split; thin after.

Order: building_materials, water, balsa, bridges_roads, nickel, lithium,
other_renewables, port_ownership, rail, graphite, niobium, solar, port_cranes,
copper, fission_smr, power_plants_grid, engineering_epc, wind.
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
            "currency": "USD" if value else "USD",
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
    "futron_san_salvador_csu_2022",
    "infrastructure",
    "engineering_epc",
    "us",
    "Futron, Inc. — State Dept San Salvador Embassy CSU design-build",
    "El Salvador",
    "16 Jun 2022: Department of State awards contract 19AQMM22C0119 to Futron, Inc. for design-build services for the U.S. Embassy in San Salvador CSU; obligated USD 28,900,833.99. Distinct from BL Harbert Tegucigalpa NEC and other Central America OBO rows.",
    "28900833.99",
    "2022-06-16",
    "2022",
    "13.701",
    "-89.227",
    "U.S. Embassy San Salvador CSU works, El Salvador (USASpending PoP El Salvador; San Salvador approximate).",
    "usaspending_futron_san_salvador_20220616",
    "DESIGN BUILD SERVICES FOR THE US EMBASSY IN SAN SALVADOR CSU.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0119_1900_-NONE-_-NONE-/",
    "Actor: Futron, Inc. (U.S.) under State OBO — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "cce_bogota_annex_2005",
    "infrastructure",
    "engineering_epc",
    "us",
    "Contracting, Consulting, Engineering LLC — State Dept Bogotá Embassy office annex",
    "Colombia",
    "26 Sep 2005: Department of State awards contract SALMEC05C0042 to Contracting, Consulting, Engineering LLC for a new office annex building on the embassy compound in Colombia; obligated USD 23,106,908.27. Distinct from CCE Guayaquil NAB and later LatAm OBO NECs.",
    "23106908.27",
    "2005-09-26",
    "2005",
    "4.638",
    "-74.095",
    "U.S. Embassy Bogotá compound office annex, Colombia (USASpending PoP Colombia; Bogotá approximate).",
    "usaspending_cce_bogota_annex_20050926",
    "NEW OFFICE ANNEX BUILDING ON THE EMBASSY COMPOUND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC05C0042_1900_-NONE-_-NONE-/",
    "Actor: Contracting, Consulting, Engineering LLC (U.S.) under State OBO — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "src_tegucigalpa_nec_pe_2019",
    "infrastructure",
    "engineering_epc",
    "us",
    "Scientific Research Corporation — State Dept Tegucigalpa NEC professional engineering",
    "Honduras",
    "6 Jun 2019: Department of State awards task order 19AQMM19F1926 to Scientific Research Corporation for professional engineering services supporting the Tegucigalpa New Embassy Compound (NEC), chancery and WSGR project (48 months; civil / project-controls engineers); obligated USD 16,909,935.50. Distinct from BL Harbert Tegucigalpa NEC construction award.",
    "16909935.50",
    "2019-06-06",
    "2019",
    "14.105",
    "-87.204",
    "U.S. Embassy Tegucigalpa NEC engineering support, Honduras (USASpending PoP Honduras; Tegucigalpa approximate).",
    "usaspending_src_tegucigalpa_pe_20190606",
    "THE CONTRACTOR SHALL PROVIDE PROFESSIONAL ENGINEERING SERVICES IN SUPPORT OF THE TEGUCIGALPA, HONDURAS NEW EMBASSY COMPOUND (NEC), CHANCERY AND WSGR PROJECT FOR A PERIOD OF 48 MONTHS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1926_1900_SAQMMA13D0078_1900/",
    "Actor: Scientific Research Corporation (U.S.) under State OBO — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "ics_borinquen_hangar_2019",
    "infrastructure",
    "engineering_epc",
    "us",
    "Integrated Construction Services, LLC — USCG Air Station Borinquen hangar D/B M&R",
    "Puerto Rico",
    "18 Sep 2019: U.S. Coast Guard awards task order 70Z08219FPACP3500 to Integrated Construction Services, LLC for design-build major M&R hangar at USCG Air Station Borinquen, Aguadilla; obligated USD 3,151,814.00. Distinct from RQ-AECOM Borinquen Phase 2 and Caddell Nova Borinquen rebuild awards.",
    "3151814.00",
    "2019-09-18",
    "2019",
    "18.495",
    "-67.129",
    "USCG Air Station Borinquen hangar, Aguadilla, Puerto Rico (USASpending PoP Aguadilla).",
    "usaspending_ics_borinquen_hangar_20190918",
    "DESIGN BUILD MAJOR M&R HANGAR AT USCG AIR STATION BORINQUEN, PR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z08219FPACP3500_7008_70Z08219DPMV23300_7008/",
    "Actor: Integrated Construction Services, LLC (U.S.) under USCG — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

row_doc(
    "powerchina_cauchari_solar_epc_2020",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Cauchari Solar Park Phase I 315 MW EPC handover (Jujuy)",
    "Argentina",
    "26 Sep 2020 commercial operations; 25 Oct 2023 final handover: POWERCHINA-built 315 MW Cauchari Solar Park Phase I in Jujuy province, Argentina, financed by China Export-Import Bank; highest-altitude / then largest-capacity PV in South America; PowerChina's largest completed PV in Argentina. CapEx USD not disclosed on opened PowerChina page. Distinct from Ganfeng Cauchari-Olaroz lithium rows and PowerChina Vicuña Batidero camp EPC.",
    "",
    "",
    "2020",
    "-23.85",
    "-66.75",
    "Cauchari Solar Park, Jujuy Province, Argentina (PowerChina geography; approximate Puna pin).",
    "powerchina_cauchari_handover_20231026",
    "On Oct 25, the 315 MW Cauchari Solar Park Phase I Project in Jujuy province, Argentina, financed by the China Export-Import Bank and built by POWERCHINA, was officially and finally signed over to the owner.",
    "https://en.powerchina.cn/2023-10/26/c_828607.htm",
    "Actor: POWERCHINA (PRC SOE) EPC — prc; CHEXIM financing named on company page. CapEx blank (company page). Distinct from lithium Cauchari-Olaroz observations.",
    "hunt_energy_solar",
    investment_type="epc",
    evidence="documented",
    chicago="POWERCHINA. “Cauchari Solar Park Phase I handed over in Argentina.” 26 October 2023. https://en.powerchina.cn/2023-10/26/c_828607.htm.",
    bib_type="company",
    annotation="POWERCHINA English primary on Cauchari 315 MW EPC/handover and CHEXIM finance. CapEx not stated. Supports powerchina_cauchari_solar_epc_2020.",
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
        "hunt_infra_building_materials": "Cycle 123: equal budget; Caribbean Lumber dense (miss).",
        "hunt_res_water": "Cycle 123: equal budget; Dick dams / Río Puerto Nuevo dense (miss).",
        "hunt_res_balsa": "Cycle 123: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_infra_bridges_roads": "Cycle 123: equal budget; FHWA residual closed (miss).",
        "hunt_res_nickel": "Cycle 123: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_res_lithium": "Cycle 123: equal budget; Ganfeng dense (miss).",
        "hunt_energy_other_renewables": "Cycle 123: equal budget; Ivirizu/Ormat dense (miss).",
        "hunt_infra_port_ownership": "Cycle 123: equal budget; COSCO/APM dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 123: equal budget; CRRC dense (miss).",
        "hunt_res_graphite": "Cycle 123: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_fenb_araxa": "Cycle 123: equal budget; CBMM dense (miss).",
        "hunt_energy_solar": "Cycle 123: logged powerchina_cauchari_solar_epc_2020.",
        "hunt_infra_port_cranes": "Cycle 123: equal budget; ZPMC dense (miss).",
        "hunt_res_copper": "Cycle 123: equal budget; CMOC dense (miss).",
        "hunt_energy_fission_smr": "Cycle 123: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_br_power_equip": "Cycle 123: equal budget; State Grid/EXIM dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 123: logged futron_san_salvador_csu_2022 + cce_bogota_annex_2005 + src_tegucigalpa_nec_pe_2019 + ics_borinquen_hangar_2019.",
        "hunt_energy_wind": "Cycle 123: equal budget; Goldwind dense (miss).",
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
    print("Cycle 123 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
