#!/usr/bin/env python3
"""Cycles 1059–1061: USASpending LatAm CapEx residual (~USD0.054–0.066m).

Seeds: 20262059–20262061. Thin top-up dry. Norshield Managua glazings.
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
    rid, layer, sub, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, sid, quote, url, note, hunt, chicago, annotation, evid_note,
    investment_type="epc",
):
    A(
        {
            "id": rid, "layer": layer, "subcategory": sub, "side": side,
            "counterpart": counterpart, "country": country, "asset": asset,
            "investment_type": investment_type, "value": value, "currency": "USD",
            "value_usd": value, "fx_usd": "1", "fx_date": fx_date, "year": year,
            "status": "active", "lat": lat, "lon": lon, "geo_note": geo,
            "evidence": "documented", "source_id": sid, "note": note,
            "pair_id": "", "counterpart_side": "", "counterpart_actor": "",
            "counterpart_value": "", "counterpart_currency": "",
            "counterpart_value_usd": "", "gap": "",
        },
        {
            "id": rid, "retrieved": "2026-10-05", "source_id": sid, "url": url,
            "price_year": year, "evidence": "documented", "quote": quote, "note": evid_note,
        },
        {
            "id": sid, "type": "government", "chicago": chicago, "url": url,
            "accessed": "2026-10-05", "annotation": annotation, "supports": [rid, hunt],
        },
    )


# === Cycle 1059 (seed 20262059) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "tidewater_panama_fuel_monitor_58k_2019",
    "energy", "power_plants_grid", "us",
    "Tidewater — Panama fuel monitor system repair",
    "Panama",
    "11 Jun 2019: Department of State awards contract 19PM0719P0344 to Tidewater, Inc. for fuel monitor system repair BME (PoP Panama); obligated USD 58,091.40. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "58091.40", "2019-06-11", "2019", "", "",
    "Fuel monitor system repair, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_tidewater_panama_fuel_monitor_58k_2019",
    "19PM0719P0344 FUEL MONITOR SYSTEM REPAIR BME (19PM0719Q0013) TIDEWATER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0344_1900_-NONE-_-NONE-/",
    "Actor: Tidewater, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1059",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0719P0344_1900_-NONE-_-NONE- (Tidewater Panama fuel monitor). Signed 2019-06-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0344_1900_-NONE-_-NONE-/.",
    "USASpending: Tidewater Panama fuel monitor USD 0.058m. Supports tidewater_panama_fuel_monitor_58k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 58091.40; date_signed 2019-06-11.",
)

row_doc(
    "monaco_honduras_d21_57k_2012",
    "infrastructure", "building_materials", "us",
    "Monaco Enterprises — Honduras Monaco D-21 installation",
    "Honduras",
    "14 Sep 2012: Department of Defense awards order W912QM12F0004 to Monaco Enterprises, Inc. for Monaco D-21 installation and training (PoP Honduras); obligated USD 56,945.09. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "56945.09", "2012-09-14", "2012", "", "",
    "Monaco D-21 installation, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_monaco_honduras_d21_57k_2012",
    "MONACO D-21 INSTALLATION AND TRAINING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM12F0004_9700_GS07F0422K_4730/",
    "Actor: Monaco Enterprises, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1059",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM12F0004_9700_GS07F0422K_4730 (Monaco Honduras D-21). Signed 2012-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM12F0004_9700_GS07F0422K_4730/.",
    "USASpending: Monaco Honduras D-21 USD 0.057m. Supports monaco_honduras_d21_57k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 56945.09; date_signed 2012-09-14.",
)

row_doc(
    "misc_argentina_villate_66k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina C. Villate 1395 Olivos remodel",
    "Argentina",
    "11 Dec 2018: Department of State awards contract 19AR2019P0135 for remodel C. Villate 1395, Olivos (PoP Argentina); obligated USD 66,086.75. CapEx face = award obligation.",
    "66086.75", "2018-12-11", "2018", "-34.512", "-58.488",
    "Remodel at C. Villate 1395, Olivos, Argentina (USASpending description; address named).",
    "usaspending_misc_argentina_villate_66k_2018",
    "FM - REMODEL C. VILLATE 1395, OLIVOS (INCREMENTAL FUNDING)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2019P0135_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1059",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2019P0135_1900_-NONE-_-NONE- (Argentina Villate). Signed 2018-12-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2019P0135_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina Villate USD 0.066m. Supports misc_argentina_villate_66k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 66086.75; date_signed 2018-12-11.",
)

row_doc(
    "misc_mexico_storm_drain_66k_2013",
    "resources", "water", "other",
    "Miscellaneous foreign awardees — Mexico NCC storm drain relocation",
    "Mexico",
    "17 Jul 2013: Department of State awards contract SMX50013M0077 for OBO/MV relocation of storm drain NCC (PoP Mexico); obligated USD 65,956.41. CapEx face = award obligation. Exact NCC site unnamed — lat/lon blank.",
    "65956.41", "2013-07-17", "2013", "", "",
    "Storm drain relocation at NCC, Mexico (USASpending description; NCC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_storm_drain_66k_2013",
    "OBO/MV RELOCATION OF STORM DRAIN NCC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX50013M0077_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water. Holdover closed.",
    "hunt_cycle1059",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX50013M0077_1900_-NONE-_-NONE- (Mexico storm drain). Signed 2013-07-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX50013M0077_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico storm drain USD 0.066m. Supports misc_mexico_storm_drain_66k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65956.41; date_signed 2013-07-17.",
)

row_doc(
    "dolliz_suriname_drainage_66k_2021",
    "resources", "water", "other",
    "Dolliz Contractor — Suriname drainage repair",
    "Suriname",
    "14 Sep 2021: Department of State awards contract 19NS5021C0001 to Dolliz Contractor NV for repair of drainage (PoP Suriname); obligated USD 65,624.93. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "65624.93", "2021-09-14", "2021", "", "",
    "Drainage repair, Suriname (USASpending description; site not named — lat/lon blank).",
    "usaspending_dolliz_suriname_drainage_66k_2021",
    "REPAIR OF DRAINAGE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5021C0001_1900_-NONE-_-NONE-/",
    "Actor: Dolliz Contractor NV (Suriname) — other. Official USASpending Award API. Shuffle water. Holdover closed.",
    "hunt_cycle1059",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19NS5021C0001_1900_-NONE-_-NONE- (Dolliz Suriname drainage). Signed 2021-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5021C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Dolliz Suriname drainage USD 0.066m. Supports dolliz_suriname_drainage_66k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65624.93; date_signed 2021-09-14.",
)

# === Cycle 1060 (seed 20262060) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "fluid_solutions_dr_fuel_dispensers_65k_2025",
    "energy", "power_plants_grid", "us",
    "Fluid Solutions — Dominican Republic fuel dispensers replacement",
    "Dominican Republic",
    "6 Mar 2025: Department of State awards contract 19DR8625P0658 to Fluid Solutions Inc for fuel dispensers replacement service (PoP Dominican Republic); obligated USD 64,604.31. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "64604.31", "2025-03-06", "2025", "", "",
    "Fuel dispensers replacement, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_fluid_solutions_dr_fuel_dispensers_65k_2025",
    "FUEL DISPENSERS REPLACEMENT SERVICE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8625P0658_1900_-NONE-_-NONE-/",
    "Actor: Fluid Solutions Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1060",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8625P0658_1900_-NONE-_-NONE- (Fluid Solutions DR fuel dispensers). Signed 2025-03-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8625P0658_1900_-NONE-_-NONE-/.",
    "USASpending: Fluid Solutions DR fuel dispensers USD 0.065m. Supports fluid_solutions_dr_fuel_dispensers_65k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64604.31; date_signed 2025-03-06.",
)

row_doc(
    "tidewater_jamaica_fuel_pump_55k_2022",
    "energy", "power_plants_grid", "us",
    "Tidewater — Jamaica fuel pump system replace and install",
    "Jamaica",
    "28 Apr 2022: Department of State awards contract 19JM3722P0430 to Tidewater, Inc. for replace and install fuel pump system (PoP Jamaica); obligated USD 54,677.15. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "54677.15", "2022-04-28", "2022", "", "",
    "Fuel pump system replace and install, Jamaica (USASpending description; site not named — lat/lon blank).",
    "usaspending_tidewater_jamaica_fuel_pump_55k_2022",
    "FAC - REPLACE AND INSTALL FUEL PUMP SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3722P0430_1900_-NONE-_-NONE-/",
    "Actor: Tidewater, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1060",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3722P0430_1900_-NONE-_-NONE- (Tidewater Jamaica fuel pump). Signed 2022-04-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3722P0430_1900_-NONE-_-NONE-/.",
    "USASpending: Tidewater Jamaica fuel pump USD 0.055m. Supports tidewater_jamaica_fuel_pump_55k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 54677.15; date_signed 2022-04-28.",
)

row_doc(
    "urbanus_panama_carports_64k_2015",
    "infrastructure", "building_materials", "other",
    "Urbanus Group — Panama embassy compound carports installation",
    "Panama",
    "4 Aug 2015: Department of State awards contract SPM07015M0713 to Urbanus Group Inc. for carports installation — U.S. Embassy compound (PoP Panama); obligated USD 64,400.54. CapEx face = award obligation. Exact compound unnamed — lat/lon blank.",
    "64400.54", "2015-08-04", "2015", "", "",
    "Carports installation at U.S. Embassy compound, Panama (USASpending description; compound not named — lat/lon blank).",
    "usaspending_urbanus_panama_carports_64k_2015",
    "IGF::OT::IGF CARPORTS INSTALLATION - U.S. EMBASSY COMPOUND - 2015",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07015M0713_1900_-NONE-_-NONE-/",
    "Actor: Urbanus Group Inc. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1060",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07015M0713_1900_-NONE-_-NONE- (Urbanus Panama carports). Signed 2015-08-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07015M0713_1900_-NONE-_-NONE-/.",
    "USASpending: Urbanus Panama carports USD 0.064m. Supports urbanus_panama_carports_64k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64400.54; date_signed 2015-08-04.",
)

row_doc(
    "misc_dr_35kva_generators_66k_2015",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic 35 kVA generators (3 units)",
    "Dominican Republic",
    "14 May 2015: Department of State awards contract SDR86015M1407 for 35KVAS generators (3 units) (PoP Dominican Republic); obligated USD 65,940. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.",
    "65940", "2015-05-14", "2015", "", "",
    "Three 35 kVA generators, Dominican Republic (USASpending description; sites not named — lat/lon blank).",
    "usaspending_misc_dr_35kva_generators_66k_2015",
    "STATE- 35KVAS GENERATORS (3 UNITS)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1407_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1060",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86015M1407_1900_-NONE-_-NONE- (DR 35 kVA generators). Signed 2015-05-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1407_1900_-NONE-_-NONE-/.",
    "USASpending: DR 35 kVA generators USD 0.066m. Supports misc_dr_35kva_generators_66k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65940; date_signed 2015-05-14.",
)

row_doc(
    "misc_belize_hvac_bas_66k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Belize HVAC BAS upgrade and repair",
    "Belize",
    "11 Sep 2014: Department of State awards contract SBH20014M0264 for HVAC BAS upgrade and repair (PoP Belize); obligated USD 65,707. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "65707", "2014-09-11", "2014", "", "",
    "HVAC building automation system upgrade and repair, Belize (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_belize_hvac_bas_66k_2014",
    "IGF::OT::IGFFM - HVAC - BAS UPGRADE AND REPAIR - DC AOA FUNDED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20014M0264_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1060",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20014M0264_1900_-NONE-_-NONE- (Belize HVAC BAS). Signed 2014-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20014M0264_1900_-NONE-_-NONE-/.",
    "USASpending: Belize HVAC BAS USD 0.066m. Supports misc_belize_hvac_bas_66k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65707; date_signed 2014-09-11.",
)

# === Cycle 1061 (seed 20262061) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "applied_security_suriname_tss_55k_2015",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Suriname TSS technical security services",
    "Suriname",
    "8 Dec 2015: Department of State awards order SAQMMA16F0269 to Applied Security Technologies Inc for technical security services (TSS) (PoP Suriname); obligated USD 54,702.99. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "54702.99", "2015-12-08", "2015", "", "",
    "Technical security services (TSS) installation, Suriname (USASpending description; site not named — lat/lon blank).",
    "usaspending_applied_security_suriname_tss_55k_2015",
    "TECHNICAL SECURITY SERVICES (TSS)  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F0269_1900_SAQMMA13D0054_1900/",
    "Actor: Applied Security Technologies Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1061",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F0269_1900_SAQMMA13D0054_1900 (Applied Security Suriname TSS). Signed 2015-12-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F0269_1900_SAQMMA13D0054_1900/.",
    "USASpending: Applied Security Suriname TSS USD 0.055m. Supports applied_security_suriname_tss_55k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 54702.99; date_signed 2015-12-08.",
)

row_doc(
    "norshield_nicaragua_managua_glazing_54k_2023",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Nicaragua Managua security glazings",
    "Nicaragua",
    "19 Dec 2023: Department of State awards contract 19AQMM24P0096 to Norshield Security Products, LLC for Managua NG225 security glazings (4 ea.) (PoP Nicaragua); obligated USD 53,640. CapEx face = award obligation.",
    "53640", "2023-12-19", "2023", "12.136", "-86.251",
    "Security glazings for Managua post, Nicaragua (USASpending description; Managua named).",
    "usaspending_norshield_nicaragua_managua_glazing_54k_2023",
    "MANAGUA_NS Q# 111123-02 (REVISED) _GPR'S_04EA.  NG225 SECURITY GLAZINGS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0096_1900_-NONE-_-NONE-/",
    "Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Nicaragua under-covered weight.",
    "hunt_cycle1061",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0096_1900_-NONE-_-NONE- (Norshield Managua glazings). Signed 2023-12-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0096_1900_-NONE-_-NONE-/.",
    "USASpending: Norshield Managua glazings USD 0.054m. Supports norshield_nicaragua_managua_glazing_54k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 53640; date_signed 2023-12-19.",
)

row_doc(
    "moderno_panama_tupper_windows_65k_2010",
    "infrastructure", "building_materials", "other",
    "Mantenimiento Moderno — Panama Tupper building window replacement",
    "Panama",
    "10 Jun 2010: Smithsonian awards contract F10PO7300000203100 to Mantenimiento Moderno de Obras Civiles for replace windows at levels 200 & 300 at Tupper Bldg. (PoP Panama); obligated USD 65,475.04. CapEx face = award obligation.",
    "65475.04", "2010-06-10", "2010", "8.953", "-79.540",
    "Window replacement at Tupper Building levels 200 & 300, Panama (USASpending description; Tupper Bldg named).",
    "usaspending_moderno_panama_tupper_windows_65k_2010",
    "REPLACE WINDOWS AT LEVELS 200 & 300 AT TUPPER BLDG.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F10PO7300000203100_3300_-NONE-_-NONE-/",
    "Actor: Mantenimiento Moderno de Obras Civiles (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1061",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F10PO7300000203100_3300_-NONE-_-NONE- (Moderno Tupper windows). Signed 2010-06-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F10PO7300000203100_3300_-NONE-_-NONE-/.",
    "USASpending: Moderno Tupper windows USD 0.065m. Supports moderno_panama_tupper_windows_65k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65475.04; date_signed 2010-06-10.",
)

row_doc(
    "misc_mexico_cdj_offices_65k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Ciudad Juárez consular offices construction",
    "Mexico",
    "5 Jun 2014: Department of State awards contract SMX11514C0004 for CDJ IVRENO construction of two offices consular area (PoP Mexico); obligated USD 65,228.41. CapEx face = award obligation.",
    "65228.41", "2014-06-05", "2014", "31.690", "-106.425",
    "Construction of two consular-area offices, Ciudad Juárez, Mexico (USASpending description; CDJ named).",
    "usaspending_misc_mexico_cdj_offices_65k_2014",
    "IGF::OT::IGF CDJ IVRENO CONSTRUCTION OF TWO OFFICES CONSULAR AREA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11514C0004_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1061",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11514C0004_1900_-NONE-_-NONE- (Mexico CDJ offices). Signed 2014-06-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11514C0004_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico CDJ offices USD 0.065m. Supports misc_mexico_cdj_offices_65k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65228.41; date_signed 2014-06-05.",
)

row_doc(
    "sarti_guatemala_windows_doors_66k_2012",
    "infrastructure", "building_materials", "other",
    "Luis Alberto Sarti Calvillo — Guatemala windows and doors",
    "Guatemala",
    "16 Apr 2012: Department of Defense awards contract W912CL12P0055 to Luis Alberto Sarti Calvillo for windows and doors (PoP Guatemala); obligated USD 66,259.82. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "66259.82", "2012-04-16", "2012", "", "",
    "Windows and doors, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_sarti_guatemala_windows_doors_66k_2012",
    "WINDOWS&DOORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL12P0055_9700_-NONE-_-NONE-/",
    "Actor: Luis Alberto Sarti Calvillo (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1061",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL12P0055_9700_-NONE-_-NONE- (Sarti Guatemala windows/doors). Signed 2012-04-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL12P0055_9700_-NONE-_-NONE-/.",
    "USASpending: Sarti Guatemala windows/doors USD 0.066m. Supports sarti_guatemala_windows_doors_66k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 66259.82; date_signed 2012-04-16.",
)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: r for r in rows}
    for row, _ev, _bib in ITEMS:
        rid = row["id"]
        if rid in by_id:
            raise SystemExit(f"duplicate id: {rid}")
        rows.append(row)
        by_id[rid] = row

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    EVID.mkdir(parents=True, exist_ok=True)
    for row, ev, _bib in ITEMS:
        path = EVID / f"{row['id']}.json"
        path.write_text(json.dumps(ev, indent=2) + "\n", encoding="utf-8")

    bib_docs = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by_id = {b["id"]: b for b in bib_docs}
    for _row, _ev, bib in ITEMS:
        sid = bib["id"]
        if sid in bib_by_id:
            existing = bib_by_id[sid]
            for s in bib.get("supports") or []:
                if s not in (existing.get("supports") or []):
                    existing.setdefault("supports", []).append(s)
        else:
            bib_docs.append(bib)
            bib_by_id[sid] = bib
    BIB.write_text(
        yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )
    print(f"loaded {len(ITEMS)} rows")


if __name__ == "__main__":
    main()
