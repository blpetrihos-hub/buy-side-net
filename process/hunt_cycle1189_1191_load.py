#!/usr/bin/env python3
"""Cycles 1189–1191: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262189–20262191. Thin top-up dry.
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


# === Cycle 1189 (seed 20262189) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "cummins_mexico_40kw_onan_gaseous_generator_11k_2017",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Mexico 40kW Cummins Onan gaseous generator",
    "Mexico",
    "6 Jun 2017: Department of Agriculture awards contract AG3267D170071 to Cummins Power Generation Inc. for 40kW Cummins Onan gaseous generator (PoP Mexico); obligated USD 11,337.47. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "11337.47", "2017-06-06", "2017", "", "",
    "40kW Cummins Onan gaseous generator, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_cummins_mexico_40kw_onan_gaseous_generator_11k_2017",
    "40KW CUMMINS ONAN GASEOUS GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG3267D170071_12K3_GS07F017DA_4732/",
    "Actor: CUMMINS POWER GENERATION INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1189",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AG3267D170071_12K3_GS07F017DA_4732 (cummins_mexico_40kw_onan_gaseous_generator_11k_2017). Signed 2017-06-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG3267D170071_12K3_GS07F017DA_4732/.",
    "USASpending: cummins_mexico_40kw_onan_gaseous_generator_11k_2017 USD 0.011m. Supports cummins_mexico_40kw_onan_gaseous_generator_11k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11337.47; date_signed 2017-06-06.",
)
row_doc(
    "fabrication_designs_guatemala_metal_door_screen_11k_2018",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Guatemala metal door screen",
    "Guatemala",
    "8 Feb 2018: Department of State awards contract 19AQMM18P0362 to Fabrication Designs, Inc. for metal door screen etc. (PoP Guatemala); obligated USD 11,222.7. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "11222.70", "2018-02-08", "2018", "", "",
    "Metal door screen etc., Guatemala (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_fabrication_designs_guatemala_metal_door_screen_11k_2018",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P0362_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1189",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18P0362_1900_-NONE-_-NONE- (fabrication_designs_guatemala_metal_door_screen_11k_2018). Signed 2018-02-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P0362_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_guatemala_metal_door_screen_11k_2018 USD 0.011m. Supports fabrication_designs_guatemala_metal_door_screen_11k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11222.7; date_signed 2018-02-08.",
)
row_doc(
    "misc_mexico_chancery_stackable_units_replace_14k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico replacement of FAC stackable units in chancery",
    "Mexico",
    "15 Aug 2017: Department of State awards contract SMX53017M1574 for replacement of FAC stackable units in chancery (PoP Mexico); obligated USD 14,087.64. CapEx face = award obligation. Chancery named; site coords not stated — lat/lon blank.",
    "14087.64", "2017-08-15", "2017", "", "",
    "Replacement of FAC stackable units in chancery, Mexico (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_chancery_stackable_units_replace_14k_2017",
    "REPLACEMENT OF FAC STACKABLE UNITS IN CHANCERY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53017M1574_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1189",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53017M1574_1900_-NONE-_-NONE- (misc_mexico_chancery_stackable_units_replace_14k_2017). Signed 2017-08-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53017M1574_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_chancery_stackable_units_replace_14k_2017 USD 0.014m. Supports misc_mexico_chancery_stackable_units_replace_14k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14087.64; date_signed 2017-08-15.",
)
row_doc(
    "misc_mexico_variable_frequency_drivers_replace_14k_2023",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico variable frequency drivers replacement",
    "Mexico",
    "11 Sep 2023: Department of State awards contract 19MX1123P0202 for FAC variable frequency drivers replacement (PoP Mexico); obligated USD 14,040.29. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14040.29", "2023-09-11", "2023", "", "",
    "Variable frequency drivers replacement, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_variable_frequency_drivers_replace_14k_2023",
    "FAC7901-VARIABLE FREQUENCY DRIVERS REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1123P0202_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1189",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX1123P0202_1900_-NONE-_-NONE- (misc_mexico_variable_frequency_drivers_replace_14k_2023). Signed 2023-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1123P0202_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_variable_frequency_drivers_replace_14k_2023 USD 0.014m. Supports misc_mexico_variable_frequency_drivers_replace_14k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14040.29; date_signed 2023-09-11.",
)
row_doc(
    "misc_guyana_steel_louvres_install_14k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guyana FMD installation of steel louvres",
    "Guyana",
    "19 Jul 2010: Department of State awards contract SGY20010M0239 for FMD installation of steel louvres (PoP Guyana); obligated USD 14,003.51. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14003.51", "2010-07-19", "2010", "", "",
    "Installation of steel louvres, Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guyana_steel_louvres_install_14k_2010",
    "FMD-INSTALLATION OF STEEL LOURVES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20010M0239_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1189",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGY20010M0239_1900_-NONE-_-NONE- (misc_guyana_steel_louvres_install_14k_2010). Signed 2010-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20010M0239_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guyana_steel_louvres_install_14k_2010 USD 0.014m. Supports misc_guyana_steel_louvres_install_14k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14003.51; date_signed 2010-07-19.",
)

# === Cycle 1190 (seed 20262190) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "harden_mexico_metal_door_frame_11k_2024",
    "infrastructure", "building_materials", "us",
    "Harden Architectural Security Products — Mexico metal door frame for international embassies",
    "Mexico",
    "25 Sep 2024: Department of State awards contract 19AQMM24P1218 to Harden Architectural Security Products, LLC for metal door frame etc. for international embassies (PoP Mexico); obligated USD 11,077.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "11077", "2024-09-25", "2024", "", "",
    "Metal door frame etc. for international embassies, Mexico (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_harden_mexico_metal_door_frame_11k_2024",
    "METAL DOOR FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P1218_1900_-NONE-_-NONE-/",
    "Actor: HARDEN ARCHITECTURAL SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1190",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P1218_1900_-NONE-_-NONE- (harden_mexico_metal_door_frame_11k_2024). Signed 2024-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P1218_1900_-NONE-_-NONE-/.",
    "USASpending: harden_mexico_metal_door_frame_11k_2024 USD 0.011m. Supports harden_mexico_metal_door_frame_11k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11077.0; date_signed 2024-09-25.",
)
row_doc(
    "norshield_costa_rica_metal_door_screen_11k_2022",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Costa Rica metal door screen for international embassies",
    "Costa Rica",
    "22 Nov 2022: Department of State awards contract 19AQMM23P0063 to Norshield Security Products, LLC for metal door screen etc. for international embassies (PoP Costa Rica); obligated USD 10,710.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "10710", "2022-11-22", "2022", "", "",
    "Metal door screen etc. for international embassies, Costa Rica (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_costa_rica_metal_door_screen_11k_2022",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0063_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1190",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23P0063_1900_-NONE-_-NONE- (norshield_costa_rica_metal_door_screen_11k_2022). Signed 2022-11-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0063_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_costa_rica_metal_door_screen_11k_2022 USD 0.011m. Supports norshield_costa_rica_metal_door_screen_11k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10710.0; date_signed 2022-11-22.",
)
row_doc(
    "misc_panama_cmr_cctv_equipment_supply_14k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Panama RSO CCTV equipment supply for CMR",
    "Panama",
    "15 Sep 2025: Department of State awards contract 19PM0725P0718 for RSO CCTV equipment supply for CMR (PoP Panama); obligated USD 13,986.88. CapEx face = award obligation. CMR named; site coords not stated — lat/lon blank.",
    "13986.88", "2025-09-15", "2025", "", "",
    "CCTV equipment supply for CMR, Panama (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_panama_cmr_cctv_equipment_supply_14k_2025",
    "RSO - CCTV EQUIPMENT SUPPLY FOR CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0725P0718_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1190",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0725P0718_1900_-NONE-_-NONE- (misc_panama_cmr_cctv_equipment_supply_14k_2025). Signed 2025-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0725P0718_1900_-NONE-_-NONE-/.",
    "USASpending: misc_panama_cmr_cctv_equipment_supply_14k_2025 USD 0.014m. Supports misc_panama_cmr_cctv_equipment_supply_14k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13986.88; date_signed 2025-09-15.",
)
row_doc(
    "misc_trinidad_chancery_ac_condenser_coils_replace_14k_2019",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Trinidad and Tobago replace condenser coils on AC for chancery",
    "Trinidad and Tobago",
    "1 May 2019: Department of State awards contract 19TD5519P0177 for replace condenser coils on AC for chancery (PoP Trinidad and Tobago); obligated USD 13,978.82. CapEx face = award obligation. Chancery named; site coords not stated — lat/lon blank.",
    "13978.82", "2019-05-01", "2019", "", "",
    "Replace condenser coils on AC for chancery, Trinidad and Tobago (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_misc_trinidad_chancery_ac_condenser_coils_replace_14k_2019",
    "REPLACE CONDENSER COILS ON AC FOR CHANCERY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5519P0177_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1190",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19TD5519P0177_1900_-NONE-_-NONE- (misc_trinidad_chancery_ac_condenser_coils_replace_14k_2019). Signed 2019-05-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5519P0177_1900_-NONE-_-NONE-/.",
    "USASpending: misc_trinidad_chancery_ac_condenser_coils_replace_14k_2019 USD 0.014m. Supports misc_trinidad_chancery_ac_condenser_coils_replace_14k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13978.82; date_signed 2019-05-01.",
)
row_doc(
    "misc_el_salvador_soyapango_holding_cell_cctv_14k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador INL CCTV system for Soyapango holding cell",
    "El Salvador",
    "27 Mar 2019: Department of State awards contract 19ES6019P0383 for INL CCTV system for Soyapango holding cell (PoP El Salvador); obligated USD 13,964.62. CapEx face = award obligation. Soyapango named; site coords not stated — lat/lon blank.",
    "13964.62", "2019-03-27", "2019", "", "",
    "CCTV system for Soyapango holding cell, El Salvador (USASpending description; Soyapango named, site coords not stated — lat/lon blank).",
    "usaspending_misc_el_salvador_soyapango_holding_cell_cctv_14k_2019",
    "INL - CCTV SYSTEM FOR SOYAPANGO HOLDING CELL / MPP- 19ES6019P0383",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6019P0383_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1190",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6019P0383_1900_-NONE-_-NONE- (misc_el_salvador_soyapango_holding_cell_cctv_14k_2019). Signed 2019-03-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6019P0383_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_soyapango_holding_cell_cctv_14k_2019 USD 0.014m. Supports misc_el_salvador_soyapango_holding_cell_cctv_14k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13964.62; date_signed 2019-03-27.",
)

# === Cycle 1191 (seed 20262191) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_belize_metal_door_steel_11k_2019",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Belize metal door steel",
    "Belize",
    "6 Jun 2019: Department of State awards contract 19AQMM19P0946 to Norshield Security Products, LLC for metal door steel etc. (PoP Belize); obligated USD 10,620.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "10620", "2019-06-06", "2019", "", "",
    "Metal door steel etc., Belize (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_belize_metal_door_steel_11k_2019",
    "METAL DOOR STEEL ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0946_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1191",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19P0946_1900_-NONE-_-NONE- (norshield_belize_metal_door_steel_11k_2019). Signed 2019-06-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0946_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_belize_metal_door_steel_11k_2019 USD 0.011m. Supports norshield_belize_metal_door_steel_11k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10620.0; date_signed 2019-06-06.",
)
row_doc(
    "norshield_el_salvador_metal_door_screen_frame_10k_2025",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — El Salvador metal door screen frame for international embassies",
    "El Salvador",
    "25 Mar 2025: Department of State awards contract 19AQMM25P0588 to Norshield Security Products, LLC for metal door screen frame etc. for international embassies (PoP El Salvador); obligated USD 10,395.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "10395", "2025-03-25", "2025", "", "",
    "Metal door screen frame etc. for international embassies, El Salvador (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_el_salvador_metal_door_screen_frame_10k_2025",
    "METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0588_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1191",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0588_1900_-NONE-_-NONE- (norshield_el_salvador_metal_door_screen_frame_10k_2025). Signed 2025-03-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0588_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_el_salvador_metal_door_screen_frame_10k_2025 USD 0.01m. Supports norshield_el_salvador_metal_door_screen_frame_10k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10395.0; date_signed 2025-03-25.",
)
row_doc(
    "misc_guyana_steel_structure_fabricate_install_14k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guyana fabricate and install steel structure",
    "Guyana",
    "30 Jul 2021: Department of State awards contract 19GY2021P0223 for fabricate and install steel structure (PoP Guyana); obligated USD 13,953.49. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13953.49", "2021-07-30", "2021", "", "",
    "Fabricate and install steel structure, Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guyana_steel_structure_fabricate_install_14k_2021",
    "FABRICATE AND INSTALL STEEL STRUCTURE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2021P0223_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1191",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GY2021P0223_1900_-NONE-_-NONE- (misc_guyana_steel_structure_fabricate_install_14k_2021). Signed 2021-07-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2021P0223_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guyana_steel_structure_fabricate_install_14k_2021 USD 0.014m. Supports misc_guyana_steel_structure_fabricate_install_14k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13953.49; date_signed 2021-07-30.",
)
row_doc(
    "misc_uruguay_cmr_barbecue_metal_awning_replace_14k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Uruguay replace CMR barbecue metal awning",
    "Uruguay",
    "11 Sep 2024: Department of State awards contract 19UY6024P0681 for FAC replace CMR barbecue metal awning (PoP Uruguay); obligated USD 13,944.17. CapEx face = award obligation. CMR named; site coords not stated — lat/lon blank.",
    "13944.17", "2024-09-11", "2024", "", "",
    "Replace CMR barbecue metal awning, Uruguay (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_uruguay_cmr_barbecue_metal_awning_replace_14k_2024",
    "FAC - REPLACE CMR'S BARBACUE METAL AWNING - 7355RSTR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6024P0681_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1191",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19UY6024P0681_1900_-NONE-_-NONE- (misc_uruguay_cmr_barbecue_metal_awning_replace_14k_2024). Signed 2024-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6024P0681_1900_-NONE-_-NONE-/.",
    "USASpending: misc_uruguay_cmr_barbecue_metal_awning_replace_14k_2024 USD 0.014m. Supports misc_uruguay_cmr_barbecue_metal_awning_replace_14k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13944.17; date_signed 2024-09-11.",
)
row_doc(
    "misc_brazil_security_cores_14k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil security cores",
    "Brazil",
    "2 Dec 2022: Department of State awards contract 19BR2523P0161 for security cores (PoP Brazil); obligated USD 14,100.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14100", "2022-12-02", "2022", "", "",
    "Security cores, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_security_cores_14k_2022",
    "SECURITY CORES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2523P0161_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1191",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2523P0161_1900_-NONE-_-NONE- (misc_brazil_security_cores_14k_2022). Signed 2022-12-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2523P0161_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_security_cores_14k_2022 USD 0.014m. Supports misc_brazil_security_cores_14k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14100.0; date_signed 2022-12-02.",
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
