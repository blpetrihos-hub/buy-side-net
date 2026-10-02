#!/usr/bin/env python3
"""Cycle 113 hunt: shuffle_seed=20261113; equal budget; U.S./PRC split; thin after.

Order: wind, bridges_roads, port_cranes, other_renewables, rail, engineering_epc,
balsa, fission_smr, port_ownership, water, building_materials, solar,
power_plants_grid, nickel, niobium, copper, lithium, graphite.
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


# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Caddell Mexico City NEC 2017 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "caddell_mexico_city_nec_2017",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Caddell Construction Co. (DE) LLC — State Dept Mexico City New Embassy Compound",
        "country": "Mexico",
        "asset": "29 Sep 2017: Department of State awards contract SAQMMA17C0287 to Caddell Construction Co. (DE), LLC for construction of New Embassy Compound (NEC) in Mexico City (chancery, Marine residence, support facilities); obligated USD 584,167,549.09 including VAT. Distinct from Caddell Borinquen USCG rebuild and other LatAm NEC awards.",
        "investment_type": "epc",
        "value": "584167549.09",
        "currency": "USD",
        "value_usd": "584167549.09",
        "fx_usd": "1",
        "fx_date": "2017-09-29",
        "year": "2017",
        "status": "active",
        "lat": "19.420",
        "lon": "-99.170",
        "geo_note": "New U.S. Embassy campus, Mexico City (State OBO / USASpending PoP Mexico).",
        "evidence": "documented",
        "source_id": "usaspending_caddell_mexico_nec_20170929",
        "note": "Actor: Caddell Construction (Montgomery AL HQ) under State OBO — us. Official USASpending Award API; State OBO media note 6 Oct 2017 confirms award.",
    },
    {
        "id": "caddell_mexico_city_nec_2017",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caddell_mexico_nec_20170929",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0287_1900_-NONE-_-NONE-/",
        "price_year": "2017",
        "evidence": "documented",
        "quote": "CONSTRUCTION SERVICES FOR NEW EMBASSY COMPOUND (NEC) IN MEXICO CITY, MEXICO",
        "note": "Opened USASpending Award API: Caddell; USD 584,167,549.09; date_signed 2017-09-29; PoP Mexico.",
    },
    {
        "id": "usaspending_caddell_mexico_nec_20170929",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0287_1900_-NONE-_-NONE- (Caddell Construction Co. (DE), LLC; Mexico City NEC). Signed 29 September 2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0287_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0287_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 584.2m Mexico City NEC. Supports caddell_mexico_city_nec_2017.",
        "supports": ["caddell_mexico_city_nec_2017", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Caddell Brasília NEC 2022 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "caddell_brasilia_nec_2022",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Caddell Construction Co. (DE) LLC — State Dept Brasília New Embassy Compound",
        "country": "Brazil",
        "asset": "10 May 2022: Department of State awards contract 19AQMM22C0102 to Caddell Construction Co. (DE), LLC for construction of New Embassy Compound in Brasília, Brazil; obligated USD 415,301,838.50. Distinct from Mexico City / Port of Spain / Nassau Caddell NEC awards.",
        "investment_type": "epc",
        "value": "415301838.50",
        "currency": "USD",
        "value_usd": "415301838.50",
        "fx_usd": "1",
        "fx_date": "2022-05-10",
        "year": "2022",
        "status": "active",
        "lat": "-15.800",
        "lon": "-47.870",
        "geo_note": "New U.S. Embassy Compound, Brasília, Brazil (USASpending PoP Brazil).",
        "evidence": "documented",
        "source_id": "usaspending_caddell_brasilia_nec_20220510",
        "note": "Actor: Caddell Construction (Montgomery AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "caddell_brasilia_nec_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caddell_brasilia_nec_20220510",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0102_1900_-NONE-_-NONE-/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "THE PURPOSE OF THIS AWARD IS TO PROVIDE CONSTRUCTION SERVICES FOR A NEW EMBASSY COMPOUND IN BRASILIA BRAZIL.",
        "note": "Opened USASpending Award API: Caddell; USD 415,301,838.50; date_signed 2022-05-10; PoP Brazil.",
    },
    {
        "id": "usaspending_caddell_brasilia_nec_20220510",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22C0102_1900_-NONE-_-NONE- (Caddell Construction Co. (DE), LLC; Brasília NEC). Signed 10 May 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0102_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0102_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 415.3m Brasília NEC. Supports caddell_brasilia_nec_2022.",
        "supports": ["caddell_brasilia_nec_2022", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Caddell Port of Spain NEC 2024 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "caddell_port_of_spain_nec_2024",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Caddell Construction Co. (DE) LLC — State Dept Port of Spain New Embassy Compound",
        "country": "Trinidad and Tobago",
        "asset": "27 Sep 2024: Department of State awards contract 19AQMM24C0140 to Caddell Construction Co. (DE), LLC for design/build New Embassy Compound in Port of Spain, Trinidad and Tobago; obligated USD 353,585,673.00. Distinct from Mexico City / Brasília Caddell NEC awards.",
        "investment_type": "epc",
        "value": "353585673.00",
        "currency": "USD",
        "value_usd": "353585673.00",
        "fx_usd": "1",
        "fx_date": "2024-09-27",
        "year": "2024",
        "status": "active",
        "lat": "10.655",
        "lon": "-61.512",
        "geo_note": "New U.S. Embassy Compound, Port of Spain, Trinidad and Tobago (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_caddell_pos_nec_20240927",
        "note": "Actor: Caddell Construction (Montgomery AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "caddell_port_of_spain_nec_2024",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caddell_pos_nec_20240927",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24C0140_1900_-NONE-_-NONE-/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "DESIGN/BUILD NEW EMBASSY COMPOUND IN PORT OF SPAIN, TRINIDAD AND TOBAGO",
        "note": "Opened USASpending Award API: Caddell; USD 353,585,673.00; date_signed 2024-09-27; PoP Trinidad and Tobago.",
    },
    {
        "id": "usaspending_caddell_pos_nec_20240927",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24C0140_1900_-NONE-_-NONE- (Caddell Construction Co. (DE), LLC; Port of Spain NEC). Signed 27 September 2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24C0140_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24C0140_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 353.6m Port of Spain NEC. Supports caddell_port_of_spain_nec_2024.",
        "supports": ["caddell_port_of_spain_nec_2024", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — BL Harbert Guatemala City NEC 2017 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "bl_harbert_guatemala_nec_2017",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "BL Harbert International LLC — State Dept Guatemala City New Embassy Compound",
        "country": "Guatemala",
        "asset": "30 Sep 2017: Department of State awards contract SAQMMA17C0325 to BL Harbert International LLC for design-build construction of New Embassy Compound (NEC) in Guatemala City; obligated USD 307,160,338.67. Distinct from BL Harbert Tegucigalpa / Hermosillo / Merida consulate awards.",
        "investment_type": "epc",
        "value": "307160338.67",
        "currency": "USD",
        "value_usd": "307160338.67",
        "fx_usd": "1",
        "fx_date": "2017-09-30",
        "year": "2017",
        "status": "active",
        "lat": "14.610",
        "lon": "-90.515",
        "geo_note": "New U.S. Embassy Compound, Guatemala City (USASpending PoP Guatemala).",
        "evidence": "documented",
        "source_id": "usaspending_harbert_guatemala_nec_20170930",
        "note": "Actor: BL Harbert International (Birmingham AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "bl_harbert_guatemala_nec_2017",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_harbert_guatemala_nec_20170930",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0325_1900_-NONE-_-NONE-/",
        "price_year": "2017",
        "evidence": "documented",
        "quote": "DESIGN-BUILD CONSTRUCTION SERVICES FOR NEW EMBASSY COMPOUND (NEC) IN GUATEMALA CITY, GUATEMALA",
        "note": "Opened USASpending Award API: BL Harbert; USD 307,160,338.67; date_signed 2017-09-30; PoP Guatemala.",
    },
    {
        "id": "usaspending_harbert_guatemala_nec_20170930",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0325_1900_-NONE-_-NONE- (BL Harbert International LLC; Guatemala City NEC). Signed 30 September 2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0325_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0325_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 307.2m Guatemala City NEC. Supports bl_harbert_guatemala_nec_2017.",
        "supports": ["bl_harbert_guatemala_nec_2017", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# energy/solar — Sungrow Vista Alegre 1+X inverters 2024 (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sungrow_vista_alegre_inverters_2024",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Sungrow — 1+X Modular Inverter supply for Atlas Vista Alegre 902 MWp (MG)",
        "country": "Brazil",
        "asset": "29 Oct 2024 Sungrow: supplies 1+X Modular Inverter turnkey solutions (75 × 8.8 MW + 18 × 6.6 MW units; MV containers with transformers/switchgear) for Vista Alegre 902 MWp / 778 MWac solar plant in Minas Gerais under 21-year PPA; grid-connection targeted 2025; includes commissioning and O&M training. CapEx USD not disclosed. Distinct from atlas_vista_alegre_solar_br_2025 ownership row and Helio Valgas / Futura Sungrow inverter rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-15.800",
        "lon": "-43.270",
        "geo_note": "Vista Alegre / Janaúba, Minas Gerais, Brazil (Sungrow / Atlas geography).",
        "evidence": "documented",
        "source_id": "sungrow_vista_alegre_20241029",
        "note": "Actor: Sungrow (PRC HQ) — prc; plant majority Atlas (allied) logged separately. Company English primary. CapEx blank.",
    },
    {
        "id": "sungrow_vista_alegre_inverters_2024",
        "retrieved": "2026-10-02",
        "source_id": "sungrow_vista_alegre_20241029",
        "url": "https://en.sungrowpower.com/newsDetail/5778/sungrow-supplies-one-of-the-americas-largest-pv-projects-a-902-mwp-solar-plant-located-in-brazil",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Sungrow announced that it has supplied the project Vista Alegre with its cutting-edge 1+X Modular Inverter solutions to one of the Americas’ largest PV projects -- a 902 MWp solar plant in Brazil.",
        "note": "Opened Sungrow English newsDetail/5778: Vista Alegre Minas Gerais; 902 MWp / 778 MWac; 75×8.8 MW + 18×6.6 MW; COD targeted 2025.",
    },
    {
        "id": "sungrow_vista_alegre_20241029",
        "type": "company",
        "chicago": "Sungrow Power Supply Co., Ltd. “Sungrow Supplies One of the Americas’ Largest PV Projects — A 902 MWp Solar Plant Located in Brazil.” News release, 29 October 2024. https://en.sungrowpower.com/newsDetail/5778/sungrow-supplies-one-of-the-americas-largest-pv-projects-a-902-mwp-solar-plant-located-in-brazil.",
        "url": "https://en.sungrowpower.com/newsDetail/5778/sungrow-supplies-one-of-the-americas-largest-pv-projects-a-902-mwp-solar-plant-located-in-brazil",
        "annotation": "Sungrow primary: Vista Alegre 902 MWp 1+X inverter supply. Supports sungrow_vista_alegre_inverters_2024.",
        "supports": ["sungrow_vista_alegre_inverters_2024", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# energy/power_plants_grid — Siemens GTMO LNG ESPC 2019 (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "siemens_gtmo_lng_espc_2019",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "Siemens Government Technologies Inc — NAVFAC GTMO ESPC including LNG plant",
        "country": "Cuba",
        "asset": "24 Jul 2019: Department of the Navy awards task order N3943019F9909 under DOE ESPC IDIQ to Siemens Government Technologies Inc for Energy Savings Performance Contract at Naval Base Guantanamo Bay, Cuba, including a liquefied natural gas plant; obligated USD 101,059,504.30. Distinct from RQ Construction JTF barracks award at same base.",
        "investment_type": "epc",
        "value": "101059504.30",
        "currency": "USD",
        "value_usd": "101059504.30",
        "fx_usd": "1",
        "fx_date": "2019-07-24",
        "year": "2019",
        "status": "active",
        "lat": "19.910",
        "lon": "-75.120",
        "geo_note": "Naval Station Guantanamo Bay, Cuba (USASpending PoP Cuba).",
        "evidence": "documented",
        "source_id": "usaspending_siemens_gtmo_lng_20190724",
        "note": "Actor: Siemens Government Technologies (Siemens AG Germany federal vehicle) — allied. Official USASpending Award API.",
    },
    {
        "id": "siemens_gtmo_lng_espc_2019",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_siemens_gtmo_lng_20190724",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N3943019F9909_9700_DEAM3609GO29041_8900/",
        "price_year": "2019",
        "evidence": "documented",
        "quote": "ENERGY SAVINGS PERFORMANCE CONTRACT FOR NAVAL BASE GUANTANAMO BAY, CUBA, TO INCLUDED AN LIQUIFIED NATURAL GAS PLANT",
        "note": "Opened USASpending Award API: Siemens GT; USD 101,059,504.30; date_signed 2019-07-24; PoP Cuba.",
    },
    {
        "id": "usaspending_siemens_gtmo_lng_20190724",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N3943019F9909_9700_DEAM3609GO29041_8900 (Siemens Government Technologies Inc; Guantanamo Bay ESPC/LNG). Signed 24 July 2019. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N3943019F9909_9700_DEAM3609GO29041_8900/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N3943019F9909_9700_DEAM3609GO29041_8900/",
        "annotation": "USASpending primary: USD 101.1m GTMO ESPC including LNG plant. Supports siemens_gtmo_lng_espc_2019.",
        "supports": ["siemens_gtmo_lng_espc_2019", "hunt_br_power_equip"],
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
        "hunt_energy_wind": "Cycle 113: equal budget; Goldwind/Vestas dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 113: equal budget; De Diego / CHEC dense (miss).",
        "hunt_infra_port_cranes": "Cycle 113: equal budget; ZPMC dense (miss).",
        "hunt_energy_other_renewables": "Cycle 113: equal budget; Sungrow BESS dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 113: equal budget; CRRC/CRCC dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 113: logged caddell_mexico_city_nec_2017 + caddell_brasilia_nec_2022 + caddell_port_of_spain_nec_2024 + bl_harbert_guatemala_nec_2017 (State OBO NECs).",
        "hunt_res_balsa": "Cycle 113: equal budget; Plantabal/WITS dense (miss). Thin dry — shift.",
        "hunt_energy_fission_smr": "Cycle 113: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_infra_port_ownership": "Cycle 113: equal budget; Hutchison/APM dense (miss).",
        "hunt_res_water": "Cycle 113: equal budget; Portugués/Ferrovial dense (miss).",
        "hunt_infra_building_materials": "Cycle 113: equal budget; Caribbean Lumber dense (miss).",
        "hunt_energy_solar": "Cycle 113: logged sungrow_vista_alegre_inverters_2024 (902 MWp 1+X).",
        "hunt_br_power_equip": "Cycle 113: logged siemens_gtmo_lng_espc_2019 (USD 101.1m NAVFAC ESPC).",
        "hunt_res_nickel": "Cycle 113: equal budget; BRN/MMG dense (miss). Thin dry — shift.",
        "hunt_fenb_araxa": "Cycle 113: equal budget; CBMM dense (miss).",
        "hunt_res_copper": "Cycle 113: equal budget; CMOC Cangrejos dense (miss).",
        "hunt_res_lithium": "Cycle 113: equal budget; Ganfeng dense (miss).",
        "hunt_res_graphite": "Cycle 113: equal budget; Graphcoa/South Star dense (miss). Thin dry — shift.",
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
    print("Cycle 113 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
