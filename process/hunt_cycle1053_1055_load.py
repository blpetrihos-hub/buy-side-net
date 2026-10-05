#!/usr/bin/env python3
"""Cycles 1053–1055: USASpending LatAm CapEx residual (~USD0.056–0.069m).

Seeds: 20262053–20262055. Thin top-up dry. Includes Siemens/ABB allied.
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


# === Cycle 1053 (seed 20262053) — 2 US / 0 PRC / 1 allied / 2 other ===
row_doc(
    "fluid_solutions_dr_fuel_monitor_67k_2023",
    "energy", "power_plants_grid", "us",
    "Fluid Solutions — Dominican Republic compound fuel monitor system replacement",
    "Dominican Republic",
    "25 Jul 2023: Department of State awards contract 19DR8623P1857 to Fluid Solutions LLC for replacement of fuel monitor system at compound (PoP Dominican Republic); obligated USD 67,162.23. CapEx face = award obligation. Exact compound unnamed — lat/lon blank.",
    "67162.23", "2023-07-25", "2023", "", "",
    "Fuel monitor system replacement at compound, Dominican Republic (USASpending description; compound not named — lat/lon blank).",
    "usaspending_fluid_solutions_dr_fuel_monitor_67k_2023",
    "OBO7901 - REPLACEMENT OF FUEL MONITOR SYSTEM AT COMPOUND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623P1857_1900_-NONE-_-NONE-/",
    "Actor: Fluid Solutions LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1053",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8623P1857_1900_-NONE-_-NONE- (Fluid Solutions DR fuel monitor). Signed 2023-07-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623P1857_1900_-NONE-_-NONE-/.",
    "USASpending: Fluid Solutions DR fuel monitor USD 0.067m. Supports fluid_solutions_dr_fuel_monitor_67k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 67162.23; date_signed 2023-07-25.",
)

row_doc(
    "pentair_ecuador_water_booster_67k_2014",
    "resources", "water", "us",
    "Pentair Flow Technologies — Ecuador domestic water booster pump",
    "Ecuador",
    "30 Sep 2014: Department of State awards contract SEC75014M0741 to Pentair Flow Technologies, LLC for domestic water booster pump (PoP Ecuador); obligated USD 67,067. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "67067", "2014-09-30", "2014", "", "",
    "Domestic water booster pump, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_pentair_ecuador_water_booster_67k_2014",
    "IGF::OT::IGF 1900.0 7901.C I 1/3 PR3745659 DOMESTIC WATER BOOSTER PUMP FM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75014M0741_1900_-NONE-_-NONE-/",
    "Actor: Pentair Flow Technologies, LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1053",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SEC75014M0741_1900_-NONE-_-NONE- (Pentair Ecuador water booster). Signed 2014-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75014M0741_1900_-NONE-_-NONE-/.",
    "USASpending: Pentair Ecuador water booster USD 0.067m. Supports pentair_ecuador_water_booster_67k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 67067; date_signed 2014-09-30.",
)

row_doc(
    "siemens_belize_switchgear_69k_2024",
    "energy", "power_plants_grid", "allied",
    "Siemens Industry — Belize switchgear circuit breaker upgrade",
    "Belize",
    "17 Sep 2024: Department of State awards contract 19BH2024P0288 to Siemens Industry Inc for switchgear circuit breaker upgrade (PoP Belize); obligated USD 69,039.24. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "69039.24", "2024-09-17", "2024", "", "",
    "Switchgear circuit breaker upgrade, Belize (USASpending description; site not named — lat/lon blank).",
    "usaspending_siemens_belize_switchgear_69k_2024",
    "SWITCHGEAR CIRCUIT BREAKER UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BH2024P0288_1900_-NONE-_-NONE-/",
    "Actor: Siemens Industry Inc (Germany parent / U.S. affiliate) — allied. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1053",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BH2024P0288_1900_-NONE-_-NONE- (Siemens Belize switchgear). Signed 2024-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BH2024P0288_1900_-NONE-_-NONE-/.",
    "USASpending: Siemens Belize switchgear USD 0.069m. Supports siemens_belize_switchgear_69k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69039.24; date_signed 2024-09-17.",
)

row_doc(
    "misc_haiti_nec_alternator_gen3_68k_2019",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Haiti NEC generator #3 alternator install",
    "Haiti",
    "6 Aug 2019: Department of State awards contract 19HA7019P0539 for purchase and installation of alternator assembly for gen #3 NEC (PoP Haiti); obligated USD 67,673.14. CapEx face = award obligation. Exact NEC site unnamed — lat/lon blank.",
    "67673.14", "2019-08-06", "2019", "", "",
    "Alternator assembly purchase and install for generator #3 at NEC, Haiti (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_nec_alternator_gen3_68k_2019",
    "PURCHASE AND INSTALLATION OF ALTERNATOR ASSY FOR GEN # 3 NEC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7019P0539_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Haiti under-covered weight.",
    "hunt_cycle1053",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7019P0539_1900_-NONE-_-NONE- (Haiti NEC alternator gen3). Signed 2019-08-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7019P0539_1900_-NONE-_-NONE-/.",
    "USASpending: Haiti NEC alternator gen3 USD 0.068m. Supports misc_haiti_nec_alternator_gen3_68k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 67673.14; date_signed 2019-08-06.",
)

row_doc(
    "misc_argentina_cmr_fire_detection_68k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina CMR wireless fire detection replacement",
    "Argentina",
    "28 Sep 2019: Department of State awards contract 19AR2019C0014 for CMR replacement of wireless fire detection system (PoP Argentina); obligated USD 67,659.57. CapEx face = award obligation. Exact CMR site unnamed — lat/lon blank.",
    "67659.57", "2019-09-28", "2019", "", "",
    "Wireless fire detection system replacement at CMR, Argentina (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_cmr_fire_detection_68k_2019",
    "FM - CMR - REPLACEMENT OF WIRELESS FIRE DETECTION SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2019C0014_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1053",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2019C0014_1900_-NONE-_-NONE- (Argentina CMR fire detection). Signed 2019-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2019C0014_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina CMR fire detection USD 0.068m. Supports misc_argentina_cmr_fire_detection_68k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 67659.57; date_signed 2019-09-28.",
)

# === Cycle 1054 (seed 20262054) — 2 US / 0 PRC / 1 allied / 2 other ===
row_doc(
    "fluid_solutions_ecuador_fuel_tank_63k_2022",
    "energy", "power_plants_grid", "us",
    "Fluid Solutions — Ecuador fuel tank management system replacement",
    "Ecuador",
    "2 Aug 2022: Department of State awards contract 19EC7522C0013 to Fluid Solutions LLC for fuel tank management system replace (PoP Ecuador); obligated USD 63,063.62. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "63063.62", "2022-08-02", "2022", "", "",
    "Fuel tank management system replacement, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_fluid_solutions_ecuador_fuel_tank_63k_2022",
    "7901-FWP#281-PR10464412-FUEL TANK MANAGEMENT SYSTEM REPLACE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0013_1900_-NONE-_-NONE-/",
    "Actor: Fluid Solutions LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1054",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7522C0013_1900_-NONE-_-NONE- (Fluid Solutions Ecuador fuel tank). Signed 2022-08-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0013_1900_-NONE-_-NONE-/.",
    "USASpending: Fluid Solutions Ecuador fuel tank USD 0.063m. Supports fluid_solutions_ecuador_fuel_tank_63k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 63063.62; date_signed 2022-08-02.",
)

row_doc(
    "baskerville_gtm_design_build_61k_2014",
    "infrastructure", "engineering_epc", "us",
    "Baskerville Donovan — Guatemala design/build HAP 23662",
    "Guatemala",
    "18 Apr 2014: Department of Defense awards order 0042 to Baskerville Donovan Inc for design/build HAP 23662 (PoP Guatemala); obligated USD 61,097.37. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "61097.37", "2014-04-18", "2014", "", "",
    "Design/build HAP 23662, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_baskerville_gtm_design_build_61k_2014",
    "IGF::OT::IGF  DESIGN/ BUILD HAP 23662",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0042_9700_W9127810D0015_9700/",
    "Actor: Baskerville Donovan Inc (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1054",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0042_9700_W9127810D0015_9700 (Baskerville Guatemala design/build). Signed 2014-04-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0042_9700_W9127810D0015_9700/.",
    "USASpending: Baskerville Guatemala design/build USD 0.061m. Supports baskerville_gtm_design_build_61k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61097.37; date_signed 2014-04-18.",
)

row_doc(
    "abb_ecuador_switchgear_breakers_68k_2023",
    "energy", "power_plants_grid", "allied",
    "ABB — Ecuador electrical switchgear breakers",
    "Ecuador",
    "18 May 2023: Department of State awards contract 19EC7523P0855 to ABB Inc for elect. switchgear breakers (PoP Ecuador); obligated USD 68,465. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "68465", "2023-05-18", "2023", "", "",
    "Electrical switchgear breakers, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_abb_ecuador_switchgear_breakers_68k_2023",
    "PR11680652-1 3-7901RSTR-FWP282-ELECT. SWITCHGEAR BREAKERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P0855_1900_-NONE-_-NONE-/",
    "Actor: ABB Inc (Switzerland/Sweden parent / U.S. affiliate) — allied. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1054",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7523P0855_1900_-NONE-_-NONE- (ABB Ecuador switchgear). Signed 2023-05-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P0855_1900_-NONE-_-NONE-/.",
    "USASpending: ABB Ecuador switchgear USD 0.068m. Supports abb_ecuador_switchgear_breakers_68k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68465; date_signed 2023-05-18.",
)

row_doc(
    "ibarra_salvador_electrical_67k_2014",
    "energy", "power_plants_grid", "other",
    "Ibarra Merino Constructores — El Salvador electrical upgrade",
    "El Salvador",
    "5 Nov 2014: Department of Defense awards contract W912CL15P0001 to Ibarra Merino Constructores S A de C V for electrical upgrade (PoP El Salvador); obligated USD 67,226.52. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "67226.52", "2014-11-05", "2014", "", "",
    "Electrical upgrade, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_ibarra_salvador_electrical_67k_2014",
    "ELECTRICAL UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL15P0001_9700_-NONE-_-NONE-/",
    "Actor: Ibarra Merino Constructores S A de C V (El Salvador) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1054",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL15P0001_9700_-NONE-_-NONE- (Ibarra El Salvador electrical). Signed 2014-11-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL15P0001_9700_-NONE-_-NONE-/.",
    "USASpending: Ibarra El Salvador electrical USD 0.067m. Supports ibarra_salvador_electrical_67k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 67226.52; date_signed 2014-11-05.",
)

row_doc(
    "alerco_chile_latrine_67k_2010",
    "infrastructure", "building_materials", "other",
    "Constructora Alerco — Chile latrine renovation",
    "Chile",
    "5 Mar 2010: Department of Defense awards contract W9127810P0125 to Constructora Alerco Limitada for D/C of latrine renovation (PoP Chile); obligated USD 66,856. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "66856", "2010-03-05", "2010", "", "",
    "Latrine renovation, Chile (USASpending description; site not named — lat/lon blank).",
    "usaspending_alerco_chile_latrine_67k_2010",
    "D/C OF LATRINE RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0125_9700_-NONE-_-NONE-/",
    "Actor: Constructora Alerco Limitada (Chile) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1054",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127810P0125_9700_-NONE-_-NONE- (Alerco Chile latrine). Signed 2010-03-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0125_9700_-NONE-_-NONE-/.",
    "USASpending: Alerco Chile latrine USD 0.067m. Supports alerco_chile_latrine_67k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 66856; date_signed 2010-03-05.",
)

# === Cycle 1055 (seed 20262055) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "diplomat_chile_lms_water_56k_2010",
    "resources", "water", "us",
    "Diplomat Freight Services — Chile LMS water treatment units",
    "Chile",
    "5 Mar 2010: USAID awards contract AIDTRNC001000060 to Diplomat Freight Services, LLC for six LMS water treatment units (PoP Chile); obligated USD 56,000. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.",
    "56000", "2010-03-05", "2010", "", "",
    "Six LMS water treatment units, Chile (USASpending description; sites not named — lat/lon blank).",
    "usaspending_diplomat_chile_lms_water_56k_2010",
    "SIX EACH LMS WATER TREATMENT UNITS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AIDTRNC001000060_7200_-NONE-_-NONE-/",
    "Actor: Diplomat Freight Services, LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1055",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AIDTRNC001000060_7200_-NONE-_-NONE- (Diplomat Chile LMS water). Signed 2010-03-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AIDTRNC001000060_7200_-NONE-_-NONE-/.",
    "USASpending: Diplomat Chile LMS water USD 0.056m. Supports diplomat_chile_lms_water_56k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 56000; date_signed 2010-03-05.",
)

row_doc(
    "fluid_solutions_dr_potable_water_68k_2024",
    "resources", "water", "us",
    "Fluid Solutions — Dominican Republic compound potable water treatment",
    "Dominican Republic",
    "9 Sep 2024: Department of State awards contract 19DR8624C0077 to Fluid Solutions LLC for potable water treatment compound (PoP Dominican Republic); obligated USD 67,876. CapEx face = award obligation. Exact compound unnamed — lat/lon blank.",
    "67876", "2024-09-09", "2024", "", "",
    "Potable water treatment at compound, Dominican Republic (USASpending description; compound not named — lat/lon blank).",
    "usaspending_fluid_solutions_dr_potable_water_68k_2024",
    "OBO7901 - SERVICE POTABLE WATER TREATMENT COMPOUND - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0077_1900_-NONE-_-NONE-/",
    "Actor: Fluid Solutions LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1055",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0077_1900_-NONE-_-NONE- (Fluid Solutions DR potable water). Signed 2024-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0077_1900_-NONE-_-NONE-/.",
    "USASpending: Fluid Solutions DR potable water USD 0.068m. Supports fluid_solutions_dr_potable_water_68k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 67876; date_signed 2024-09-09.",
)

row_doc(
    "crandella_guyana_patio_67k_2019",
    "infrastructure", "building_materials", "other",
    "Crandella Alleyne — Guyana patio extension construction",
    "Guyana",
    "24 Sep 2019: Department of State awards contract 19GY2019C0004 to Crandella Alleyne for patio extension (construction) (PoP Guyana); obligated USD 67,005.65. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "67005.65", "2019-09-24", "2019", "", "",
    "Patio extension construction, Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_crandella_guyana_patio_67k_2019",
    "PATIO EXTENSION (CONSTRUCTION)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2019C0004_1900_-NONE-_-NONE-/",
    "Actor: Crandella Alleyne (Guyana) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1055",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GY2019C0004_1900_-NONE-_-NONE- (Crandella Guyana patio). Signed 2019-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2019C0004_1900_-NONE-_-NONE-/.",
    "USASpending: Crandella Guyana patio USD 0.067m. Supports crandella_guyana_patio_67k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 67005.65; date_signed 2019-09-24.",
)

row_doc(
    "ag_proyectos_panama_albergue_generator_67k_2026",
    "energy", "power_plants_grid", "other",
    "AG Proyectos y Servicios — Panama female albergue electrical reconfiguration and generator",
    "Panama",
    "1 Jul 2026: Department of State awards contract 19GE5026P0060 to AG Proyectos y Servicios S.A for female albergue electrical reconfiguration and generator installation project (PoP Panama); obligated USD 67,010.39. CapEx face = award obligation. Exact albergue unnamed — lat/lon blank.",
    "67010.39", "2026-07-01", "2026", "", "",
    "Female albergue electrical reconfiguration and generator installation, Panama (USASpending description; albergue not named — lat/lon blank).",
    "usaspending_ag_proyectos_panama_albergue_generator_67k_2026",
    "ACQUISITION OF FEMALE ALBERGUE ELECTRICAL RECONFIGURATION AND GENERATOR INSTALLATION PROJECT, PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026P0060_1900_-NONE-_-NONE-/",
    "Actor: AG Proyectos y Servicios S.A (Panama) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1055",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5026P0060_1900_-NONE-_-NONE- (AG Proyectos Panama albergue generator). Signed 2026-07-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026P0060_1900_-NONE-_-NONE-/.",
    "USASpending: AG Proyectos Panama albergue generator USD 0.067m. Supports ag_proyectos_panama_albergue_generator_67k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 67010.39; date_signed 2026-07-01.",
)

row_doc(
    "misc_salvador_gym_parking_68k_2016",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — El Salvador gym parking repairs",
    "El Salvador",
    "27 Sep 2016: Department of State awards contract SES60016M1242 for gym parking repairs (PoP El Salvador); obligated USD 68,368.81. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "68368.81", "2016-09-27", "2016", "", "",
    "Gym parking repairs, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_salvador_gym_parking_68k_2016",
    "7901- GYM PARKING REPAIRS IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60016M1242_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1055",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60016M1242_1900_-NONE-_-NONE- (El Salvador gym parking). Signed 2016-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60016M1242_1900_-NONE-_-NONE-/.",
    "USASpending: El Salvador gym parking USD 0.068m. Supports misc_salvador_gym_parking_68k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68368.81; date_signed 2016-09-27.",
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
