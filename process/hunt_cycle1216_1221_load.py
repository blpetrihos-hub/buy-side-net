#!/usr/bin/env python3
"""Cycles 1216–1221: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262216–20262221. Thin top-up dry.
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

# === Cycle 1216 ===
row_doc(
    "norshield_nicaragua_replace_broken_window_5k_2010",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Nicaragua replace broken window",
    "Nicaragua",
    "5 Feb 2010: Department of State awards contract SNU70010M0541 to NORSHIELD SECURITY PRODUCTS, LLC for REPLACE BROKEN WINDOW (PoP Nicaragua); obligated USD 4808. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "4808", "2010-02-05", "2010", "", "",
    "REPLACE BROKEN WINDOW, Nicaragua (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_nicaragua_replace_broken_window_5k_2010",
    "REPLACE BROKEN WINDOW",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70010M0541_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1216",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SNU70010M0541_1900_-NONE-_-NONE- (norshield_nicaragua_replace_broken_window_5k_2010). Signed 2010-02-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70010M0541_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_nicaragua_replace_broken_window_5k_2010 USD 0.005m. Supports norshield_nicaragua_replace_broken_window_5k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4808.0; date_signed 2010-02-05.",
)

# === Cycle 1216 ===
row_doc(
    "fabrication_designs_mexico_metal_door_screen_5k_2022",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Mexico metal door screen",
    "Mexico",
    "15 Dec 2021: Department of State awards contract 19AQMM22P0074 to FABRICATION DESIGNS, INC. for METAL DOOR SCREEN ETC. (PoP Mexico); obligated USD 4627.12. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "4627.12", "2021-12-15", "2021", "", "",
    "METAL DOOR SCREEN ETC., Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_fabrication_designs_mexico_metal_door_screen_5k_2022",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0074_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1216",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22P0074_1900_-NONE-_-NONE- (fabrication_designs_mexico_metal_door_screen_5k_2022). Signed 2021-12-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0074_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_mexico_metal_door_screen_5k_2022 USD 0.005m. Supports fabrication_designs_mexico_metal_door_screen_5k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4627.12; date_signed 2021-12-15.",
)

# === Cycle 1216 ===
row_doc(
    "misc_honduras_dea_siu_ups_13k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras UPS for DEA SIU",
    "Honduras",
    "26 May 2011: Department of State awards contract SHO80011M0276 for INL - DESKTOP COMPUTERS AND UPS FOR DEA SIU  1930.2 (PoP Honduras); obligated USD 13388.73. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13388.73", "2011-05-26", "2011", "", "",
    "INL - DESKTOP COMPUTERS AND UPS FOR DEA SIU  1930.2, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_honduras_dea_siu_ups_13k_2011",
    "INL - DESKTOP COMPUTERS AND UPS FOR DEA SIU  1930.2",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80011M0276_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1216",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80011M0276_1900_-NONE-_-NONE- (misc_honduras_dea_siu_ups_13k_2011). Signed 2011-05-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80011M0276_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_dea_siu_ups_13k_2011 USD 0.013m. Supports misc_honduras_dea_siu_ups_13k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13388.73; date_signed 2011-05-26.",
)

# === Cycle 1216 ===
row_doc(
    "misc_nicaragua_security_upgrade_new_cmr_13k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Nicaragua Security upgrade installation at new CMR",
    "Nicaragua",
    "20 Jan 2021: Department of State awards contract 19NU7021P0135 for MISC. SECURITY UPGRADE INSTALLATION SERVICES AT NEW CMR (RSO) (PoP Nicaragua); obligated USD 13350. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13350", "2021-01-20", "2021", "", "",
    "MISC. SECURITY UPGRADE INSTALLATION SERVICES AT NEW CMR (RSO), Nicaragua (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_nicaragua_security_upgrade_new_cmr_13k_2021",
    "MISC. SECURITY UPGRADE INSTALLATION SERVICES AT NEW CMR (RSO)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NU7021P0135_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1216",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19NU7021P0135_1900_-NONE-_-NONE- (misc_nicaragua_security_upgrade_new_cmr_13k_2021). Signed 2021-01-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NU7021P0135_1900_-NONE-_-NONE-/.",
    "USASpending: misc_nicaragua_security_upgrade_new_cmr_13k_2021 USD 0.013m. Supports misc_nicaragua_security_upgrade_new_cmr_13k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13350.0; date_signed 2021-01-20.",
)

# === Cycle 1216 ===
row_doc(
    "misc_guyana_chancery_well_pump_13k_2025",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Guyana Well pump procurement chancery well",
    "Guyana",
    "17 Dec 2024: Department of State awards contract 19GY2025P0077 for WELL PUMP PROCUREMENT CHANCERY WELL (PoP Guyana); obligated USD 13255.81. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13255.81", "2024-12-17", "2024", "", "",
    "WELL PUMP PROCUREMENT CHANCERY WELL, Guyana (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_guyana_chancery_well_pump_13k_2025",
    "WELL PUMP PROCUREMENT CHANCERY WELL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2025P0077_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1216",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GY2025P0077_1900_-NONE-_-NONE- (misc_guyana_chancery_well_pump_13k_2025). Signed 2024-12-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2025P0077_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guyana_chancery_well_pump_13k_2025 USD 0.013m. Supports misc_guyana_chancery_well_pump_13k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13255.81; date_signed 2024-12-17.",
)

# === Cycle 1217 ===
row_doc(
    "norshield_costa_rica_metal_door_screen_5k_2020",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Costa Rica metal door screen",
    "Costa Rica",
    "9 Dec 2020: Department of State awards contract 19AQMM21P0092 to NORSHIELD SECURITY PRODUCTS, LLC for METAL DOOR SCREEN ETC. (PoP Costa Rica); obligated USD 4575. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "4575", "2020-12-09", "2020", "", "",
    "METAL DOOR SCREEN ETC., Costa Rica (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_costa_rica_metal_door_screen_5k_2020",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21P0092_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1217",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21P0092_1900_-NONE-_-NONE- (norshield_costa_rica_metal_door_screen_5k_2020). Signed 2020-12-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21P0092_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_costa_rica_metal_door_screen_5k_2020 USD 0.005m. Supports norshield_costa_rica_metal_door_screen_5k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4575.0; date_signed 2020-12-09.",
)

# === Cycle 1217 ===
row_doc(
    "fabrication_designs_trinidad_metal_door_screen_4k_2018",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Trinidad and Tobago metal door screen",
    "Trinidad and Tobago",
    "13 Nov 2018: Department of State awards contract 19AQMM19P0031 to FABRICATION DESIGNS, INC. for METAL DOOR, SCREEN ETC. (PoP Trinidad and Tobago); obligated USD 4016.20. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "4016.20", "2018-11-13", "2018", "", "",
    "METAL DOOR, SCREEN ETC., Trinidad and Tobago (USASpending description; site not named — lat/lon blank).",
    "usaspending_fabrication_designs_trinidad_metal_door_screen_4k_2018",
    "METAL DOOR, SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0031_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1217",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19P0031_1900_-NONE-_-NONE- (fabrication_designs_trinidad_metal_door_screen_4k_2018). Signed 2018-11-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0031_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_trinidad_metal_door_screen_4k_2018 USD 0.004m. Supports fabrication_designs_trinidad_metal_door_screen_4k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4016.2; date_signed 2018-11-13.",
)

# === Cycle 1217 ===
row_doc(
    "misc_mexico_msg_bathroom_renovation_13k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico MSG bathroom renovation FY19",
    "Mexico",
    "17 Sep 2019: Department of State awards contract 19MX5319C0026 for MX-FAC-7901-MSG BATHROOM RENOVATION-FY19 (PoP Mexico); obligated USD 13232.13. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13232.13", "2019-09-17", "2019", "", "",
    "MX-FAC-7901-MSG BATHROOM RENOVATION-FY19, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_msg_bathroom_renovation_13k_2019",
    "MX-FAC-7901-MSG BATHROOM RENOVATION-FY19",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319C0026_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1217",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5319C0026_1900_-NONE-_-NONE- (misc_mexico_msg_bathroom_renovation_13k_2019). Signed 2019-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319C0026_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_msg_bathroom_renovation_13k_2019 USD 0.013m. Supports misc_mexico_msg_bathroom_renovation_13k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13232.13; date_signed 2019-09-17.",
)

# === Cycle 1217 ===
row_doc(
    "misc_chile_rso_house_generator_13k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Chile Generator for RSO house",
    "Chile",
    "13 Aug 2010: Department of State awards contract SCI80010M0767 for FAC - GENERATOR FOR RSO HOUSE (PoP Chile); obligated USD 13209. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13209", "2010-08-13", "2010", "", "",
    "FAC - GENERATOR FOR RSO HOUSE, Chile (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_chile_rso_house_generator_13k_2010",
    "FAC - GENERATOR FOR RSO HOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80010M0767_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1217",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCI80010M0767_1900_-NONE-_-NONE- (misc_chile_rso_house_generator_13k_2010). Signed 2010-08-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80010M0767_1900_-NONE-_-NONE-/.",
    "USASpending: misc_chile_rso_house_generator_13k_2010 USD 0.013m. Supports misc_chile_rso_house_generator_13k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13209.0; date_signed 2010-08-13.",
)

# === Cycle 1217 ===
row_doc(
    "misc_dominican_make_ready_los_bambues_33_13k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic SRM & make-ready Los Bambues 33",
    "Dominican Republic",
    "2 Jul 2024: Department of State awards contract 19DR8624C0046 for DS- SRM & MAKE READY WORK LOS BAMBUES 33 PID 823 - AWARD (PoP Dominican Republic); obligated USD 13200.99. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13200.99", "2024-07-02", "2024", "", "",
    "DS- SRM & MAKE READY WORK LOS BAMBUES 33 PID 823 - AWARD, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_make_ready_los_bambues_33_13k_2024",
    "DS- SRM & MAKE READY WORK LOS BAMBUES 33 PID 823 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0046_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1217",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0046_1900_-NONE-_-NONE- (misc_dominican_make_ready_los_bambues_33_13k_2024). Signed 2024-07-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0046_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_make_ready_los_bambues_33_13k_2024 USD 0.013m. Supports misc_dominican_make_ready_los_bambues_33_13k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13200.99; date_signed 2024-07-02.",
)

# === Cycle 1218 ===
row_doc(
    "ross_technology_suriname_metal_door_screen_4k_2019",
    "infrastructure", "building_materials", "us",
    "Ross Technology — Suriname metal door screen",
    "Suriname",
    "11 Jul 2019: Department of State awards contract 19AQMM19P1103 to ROSS TECHNOLOGY COMPANY for METAL DOOR SCREEN ETC. (PoP Suriname); obligated USD 3805. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "3805", "2019-07-11", "2019", "", "",
    "METAL DOOR SCREEN ETC., Suriname (USASpending description; site not named — lat/lon blank).",
    "usaspending_ross_technology_suriname_metal_door_screen_4k_2019",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P1103_1900_-NONE-_-NONE-/",
    "Actor: ROSS TECHNOLOGY COMPANY (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1218",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19P1103_1900_-NONE-_-NONE- (ross_technology_suriname_metal_door_screen_4k_2019). Signed 2019-07-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P1103_1900_-NONE-_-NONE-/.",
    "USASpending: ross_technology_suriname_metal_door_screen_4k_2019 USD 0.004m. Supports ross_technology_suriname_metal_door_screen_4k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3805.0; date_signed 2019-07-11.",
)

# === Cycle 1218 ===
row_doc(
    "norshield_nicaragua_metal_door_screen_4k_2020",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Nicaragua metal door screen",
    "Nicaragua",
    "12 Aug 2020: Department of State awards contract 19AQMM20P1302 to NORSHIELD SECURITY PRODUCTS, LLC for METAL DOOR, SCREEN ETC. (PoP Nicaragua); obligated USD 3755. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "3755", "2020-08-12", "2020", "", "",
    "METAL DOOR, SCREEN ETC., Nicaragua (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_nicaragua_metal_door_screen_4k_2020",
    "METAL DOOR, SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P1302_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1218",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20P1302_1900_-NONE-_-NONE- (norshield_nicaragua_metal_door_screen_4k_2020). Signed 2020-08-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P1302_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_nicaragua_metal_door_screen_4k_2020 USD 0.004m. Supports norshield_nicaragua_metal_door_screen_4k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3755.0; date_signed 2020-08-12.",
)

# === Cycle 1218 ===
row_doc(
    "misc_venezuela_fac_ac_units_replace_first_floor_13k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Venezuela Replace air conditioning units at first floor",
    "Venezuela",
    "29 Sep 2016: Department of State awards contract SVE30016C0009 for IGF::CL::IGF FAC-REPLACE AIR CONDITIONING UNITS AT THE FIRST FLOOR OF CMR (PoP Venezuela); obligated USD 13197.21. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13197.21", "2016-09-29", "2016", "", "",
    "IGF::CL::IGF FAC-REPLACE AIR CONDITIONING UNITS AT THE FIRST FLOOR OF CMR, Venezuela (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_venezuela_fac_ac_units_replace_first_floor_13k_2016",
    "IGF::CL::IGF FAC-REPLACE AIR CONDITIONING UNITS AT THE FIRST FLOOR OF CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30016C0009_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1218",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30016C0009_1900_-NONE-_-NONE- (misc_venezuela_fac_ac_units_replace_first_floor_13k_2016). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30016C0009_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_fac_ac_units_replace_first_floor_13k_2016 USD 0.013m. Supports misc_venezuela_fac_ac_units_replace_first_floor_13k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13197.21; date_signed 2016-09-29.",
)

# === Cycle 1218 ===
row_doc(
    "misc_peru_install_ac_units_rso_13k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Peru Install AC units RSO",
    "Peru",
    "9 Feb 2017: Department of State awards contract SPE50017M0739 for INSTALL AC UNITS - STEVENS, ANDREW/RSO (LABOR) \"IGF::OT::IGF\" (PoP Peru); obligated USD 13180.46. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13180.46", "2017-02-09", "2017", "", "",
    "INSTALL AC UNITS - STEVENS, ANDREW/RSO (LABOR) \"IGF::OT::IGF\", Peru (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_peru_install_ac_units_rso_13k_2017",
    "INSTALL AC UNITS - STEVENS, ANDREW/RSO (LABOR) \"IGF::OT::IGF\"",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50017M0739_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1218",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50017M0739_1900_-NONE-_-NONE- (misc_peru_install_ac_units_rso_13k_2017). Signed 2017-02-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50017M0739_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_install_ac_units_rso_13k_2017 USD 0.013m. Supports misc_peru_install_ac_units_rso_13k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13180.46; date_signed 2017-02-09.",
)

# === Cycle 1218 ===
row_doc(
    "misc_brazil_install_ac_units_greenwood_13k_2022",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil Install AC units for Greenwood",
    "Brazil",
    "12 Jan 2022: Department of State awards contract 19BR9322P0112 for SP/MAKE READY/GSO/OBO624:INSTALL AC UNITS FOR GREENWOOD(AF) (PoP Brazil); obligated USD 13176.78. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13176.78", "2022-01-12", "2022", "", "",
    "SP/MAKE READY/GSO/OBO624:INSTALL AC UNITS FOR GREENWOOD(AF), Brazil (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_install_ac_units_greenwood_13k_2022",
    "SP/MAKE READY/GSO/OBO624:INSTALL AC UNITS FOR GREENWOOD(AF)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9322P0112_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1218",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9322P0112_1900_-NONE-_-NONE- (misc_brazil_install_ac_units_greenwood_13k_2022). Signed 2022-01-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9322P0112_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_install_ac_units_greenwood_13k_2022 USD 0.013m. Supports misc_brazil_install_ac_units_greenwood_13k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13176.78; date_signed 2022-01-12.",
)

# === Cycle 1219 ===
row_doc(
    "fabrication_designs_brazil_metal_window_door_4k_2014",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Brazil metal window and door construction",
    "Brazil",
    "18 Nov 2013: Department of State awards contract SAQMMA14M0058 to FABRICATION DESIGNS, INC. for CONSTRUCTION OF MISCELLANEOUS BUILDINGS. METAL WINDOW AND DOOR. IGF::CL::IGF (PoP Brazil); obligated USD 3749.57. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "3749.57", "2013-11-18", "2013", "", "",
    "CONSTRUCTION OF MISCELLANEOUS BUILDINGS. METAL WINDOW AND DOOR. IGF::CL::IGF, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_fabrication_designs_brazil_metal_window_door_4k_2014",
    "CONSTRUCTION OF MISCELLANEOUS BUILDINGS. METAL WINDOW AND DOOR. IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14M0058_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1219",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14M0058_1900_-NONE-_-NONE- (fabrication_designs_brazil_metal_window_door_4k_2014). Signed 2013-11-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14M0058_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_brazil_metal_window_door_4k_2014 USD 0.004m. Supports fabrication_designs_brazil_metal_window_door_4k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3749.57; date_signed 2013-11-18.",
)

# === Cycle 1219 ===
row_doc(
    "norshield_dominican_febr_door_glazing_replace_4k_2012",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Dominican Republic FE/BR door glazing replace Santo Domingo",
    "Dominican Republic",
    "26 Apr 2012: Department of State awards contract SAQMMA12M0949 to NORSHIELD SECURITY PRODUCTS, LLC for TO REPLACE A DAMAGED FE/BR GLAZING ON AN FE/BR DOOR IN SANTO DOMINGO. (PoP Dominican Republic); obligated USD 3726. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "3726", "2012-04-26", "2012", "", "",
    "TO REPLACE A DAMAGED FE/BR GLAZING ON AN FE/BR DOOR IN SANTO DOMINGO., Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_norshield_dominican_febr_door_glazing_replace_4k_2012",
    "TO REPLACE A DAMAGED FE/BR GLAZING ON AN FE/BR DOOR IN SANTO DOMINGO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12M0949_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1219",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12M0949_1900_-NONE-_-NONE- (norshield_dominican_febr_door_glazing_replace_4k_2012). Signed 2012-04-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12M0949_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_dominican_febr_door_glazing_replace_4k_2012 USD 0.004m. Supports norshield_dominican_febr_door_glazing_replace_4k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3726.0; date_signed 2012-04-26.",
)

# === Cycle 1219 ===
row_doc(
    "misc_ecuador_replace_r22_ac_units_cgr_13k_2018",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Ecuador Replace two R-22 A/C units at CGR",
    "Ecuador",
    "22 Aug 2018: Department of State awards contract 19EC3018P0541 for IGF::OT::IGF REPLACE TWO R-22 A/C UNITS AT CGR (PoP Ecuador); obligated USD 13176.68. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13176.68", "2018-08-22", "2018", "", "",
    "IGF::OT::IGF REPLACE TWO R-22 A/C UNITS AT CGR, Ecuador (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_ecuador_replace_r22_ac_units_cgr_13k_2018",
    "IGF::OT::IGF REPLACE TWO R-22 A/C UNITS AT CGR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3018P0541_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1219",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3018P0541_1900_-NONE-_-NONE- (misc_ecuador_replace_r22_ac_units_cgr_13k_2018). Signed 2018-08-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3018P0541_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_replace_r22_ac_units_cgr_13k_2018 USD 0.013m. Supports misc_ecuador_replace_r22_ac_units_cgr_13k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13176.68; date_signed 2018-08-22.",
)

# === Cycle 1219 ===
row_doc(
    "misc_brazil_cctv_13k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil CCTV",
    "Brazil",
    "3 May 2021: Department of State awards contract 19BR2521P0387 for CCTV (PoP Brazil); obligated USD 12744.62. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12744.62", "2021-05-03", "2021", "", "",
    "CCTV, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_cctv_13k_2021",
    "CCTV",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521P0387_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1219",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2521P0387_1900_-NONE-_-NONE- (misc_brazil_cctv_13k_2021). Signed 2021-05-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521P0387_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_cctv_13k_2021 USD 0.013m. Supports misc_brazil_cctv_13k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12744.62; date_signed 2021-05-03.",
)

# === Cycle 1219 ===
row_doc(
    "misc_paraguay_make_ready_new_dcm_13k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Paraguay FAC make-ready for new DCM",
    "Paraguay",
    "24 May 2016: Department of State awards contract SPA10016M0220 for FAC-U-MAKE READY FOR NEW DCM (RODRIGUEZ) IGF::OT::IGF (PoP Paraguay); obligated USD 12741.13. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12741.13", "2016-05-24", "2016", "", "",
    "FAC-U-MAKE READY FOR NEW DCM (RODRIGUEZ) IGF::OT::IGF, Paraguay (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_paraguay_make_ready_new_dcm_13k_2016",
    "FAC-U-MAKE READY FOR NEW DCM (RODRIGUEZ) IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPA10016M0220_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1219",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPA10016M0220_1900_-NONE-_-NONE- (misc_paraguay_make_ready_new_dcm_13k_2016). Signed 2016-05-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPA10016M0220_1900_-NONE-_-NONE-/.",
    "USASpending: misc_paraguay_make_ready_new_dcm_13k_2016 USD 0.013m. Supports misc_paraguay_make_ready_new_dcm_13k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12741.13; date_signed 2016-05-24.",
)

# === Cycle 1220 ===
row_doc(
    "norshield_costa_rica_office_security_glazing_4k_2014",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Costa Rica office building security glazing",
    "Costa Rica",
    "10 Mar 2014: Department of State awards contract SAQMMA14M0497 to NORSHIELD SECURITY PRODUCTS, LLC for CONSTRUCTION OF OFFICE BUILDING. SECURITY GLAZING.IGF::CL::IGF (PoP Costa Rica); obligated USD 3560. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "3560", "2014-03-10", "2014", "", "",
    "CONSTRUCTION OF OFFICE BUILDING. SECURITY GLAZING.IGF::CL::IGF, Costa Rica (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_costa_rica_office_security_glazing_4k_2014",
    "CONSTRUCTION OF OFFICE BUILDING. SECURITY GLAZING.IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14M0497_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1220",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14M0497_1900_-NONE-_-NONE- (norshield_costa_rica_office_security_glazing_4k_2014). Signed 2014-03-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14M0497_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_costa_rica_office_security_glazing_4k_2014 USD 0.004m. Supports norshield_costa_rica_office_security_glazing_4k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3560.0; date_signed 2014-03-10.",
)

# === Cycle 1220 ===
row_doc(
    "overly_door_panama_day_gate_replace_3k_2014",
    "infrastructure", "building_materials", "us",
    "Overly Door — Panama replacement of day gate",
    "Panama",
    "23 Jun 2014: Department of State awards contract SPM07014M0482 to OVERLY DOOR CO for REPLACEMENT  OF DAY GATE, DOS STD HT - 7901.C (PoP Panama); obligated USD 3470. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "3470", "2014-06-23", "2014", "", "",
    "REPLACEMENT  OF DAY GATE, DOS STD HT - 7901.C, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_overly_door_panama_day_gate_replace_3k_2014",
    "REPLACEMENT  OF DAY GATE, DOS STD HT - 7901.C",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014M0482_1900_-NONE-_-NONE-/",
    "Actor: OVERLY DOOR CO (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1220",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07014M0482_1900_-NONE-_-NONE- (overly_door_panama_day_gate_replace_3k_2014). Signed 2014-06-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014M0482_1900_-NONE-_-NONE-/.",
    "USASpending: overly_door_panama_day_gate_replace_3k_2014 USD 0.003m. Supports overly_door_panama_day_gate_replace_3k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3470.0; date_signed 2014-06-23.",
)

# === Cycle 1220 ===
row_doc(
    "misc_colombia_usaid_internet_access_renovation_13k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia MAIN USAID INTERNET ACCESS RENOVATION - 2000K",
    "Colombia",
    "4 Nov 2010: Department of State awards contract SCO20011M0178 for MAIN USAID INTERNET ACCESS RENOVATION - 2000K (PoP Colombia); obligated USD 12800.09. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12800.09", "2010-11-04", "2010", "", "",
    "MAIN USAID INTERNET ACCESS RENOVATION - 2000K, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_usaid_internet_access_renovation_13k_2011",
    "MAIN USAID INTERNET ACCESS RENOVATION - 2000K",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20011M0178_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1220",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20011M0178_1900_-NONE-_-NONE- (misc_colombia_usaid_internet_access_renovation_13k_2011). Signed 2010-11-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20011M0178_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_usaid_internet_access_renovation_13k_2011 USD 0.013m. Supports misc_colombia_usaid_internet_access_renovation_13k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12800.09; date_signed 2010-11-04.",
)

# === Cycle 1220 ===
row_doc(
    "misc_bolivia_renovation_project_13k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bolivia renovation project",
    "Bolivia",
    "29 Nov 2017: Department of State awards contract 19BL4018P0050 for RENOVATION PROJECT IGF::OT::IGF (PoP Bolivia); obligated USD 12732.12. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12732.12", "2017-11-29", "2017", "", "",
    "RENOVATION PROJECT IGF::OT::IGF, Bolivia (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_bolivia_renovation_project_13k_2018",
    "RENOVATION PROJECT IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BL4018P0050_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1220",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BL4018P0050_1900_-NONE-_-NONE- (misc_bolivia_renovation_project_13k_2018). Signed 2017-11-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BL4018P0050_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bolivia_renovation_project_13k_2018 USD 0.013m. Supports misc_bolivia_renovation_project_13k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12732.12; date_signed 2017-11-29.",
)

# === Cycle 1220 ===
row_doc(
    "misc_argentina_install_ducts_air_condition_13k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Argentina install ducts for air condition",
    "Argentina",
    "29 Sep 2010: Department of State awards contract SAR20010M1650 for INSTALL DUCTS FOR AIR CONDITION (PoP Argentina); obligated USD 12722. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12722", "2010-09-29", "2010", "", "",
    "INSTALL DUCTS FOR AIR CONDITION, Argentina (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_argentina_install_ducts_air_condition_13k_2010",
    "INSTALL DUCTS FOR AIR CONDITION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20010M1650_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1220",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20010M1650_1900_-NONE-_-NONE- (misc_argentina_install_ducts_air_condition_13k_2010). Signed 2010-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20010M1650_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_install_ducts_air_condition_13k_2010 USD 0.013m. Supports misc_argentina_install_ducts_air_condition_13k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12722.0; date_signed 2010-09-29.",
)

# === Cycle 1221 ===
row_doc(
    "norshield_jamaica_febr_security_window_cmr_3k_2010",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Jamaica new FEBR security window for CMR",
    "Jamaica",
    "9 Mar 2010: Department of State awards contract SJM37010M0450 to NORSHIELD SECURITY PRODUCTS, LLC for RSO - NEW FEBR (SECURITY) WINDOW FOR CMR (PoP Jamaica); obligated USD 3400. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "3400", "2010-03-09", "2010", "", "",
    "RSO - NEW FEBR (SECURITY) WINDOW FOR CMR, Jamaica (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_norshield_jamaica_febr_security_window_cmr_3k_2010",
    "RSO - NEW FEBR (SECURITY) WINDOW FOR CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37010M0450_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1221",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37010M0450_1900_-NONE-_-NONE- (norshield_jamaica_febr_security_window_cmr_3k_2010). Signed 2010-03-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37010M0450_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_jamaica_febr_security_window_cmr_3k_2010 USD 0.003m. Supports norshield_jamaica_febr_security_window_cmr_3k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3400.0; date_signed 2010-03-09.",
)

# === Cycle 1221 ===
row_doc(
    "fabrication_designs_mexico_metal_screen_fire_door_3k_2015",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Mexico metal screen fire door",
    "Mexico",
    "19 May 2015: Department of State awards contract SAQMMA15M1144 to FABRICATION DESIGNS, INC. for METAL SCREEN, FIRE DOOR ETC. (PoP Mexico); obligated USD 3348. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "3348", "2015-05-19", "2015", "", "",
    "METAL SCREEN, FIRE DOOR ETC., Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_fabrication_designs_mexico_metal_screen_fire_door_3k_2015",
    "METAL SCREEN, FIRE DOOR ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15M1144_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1221",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15M1144_1900_-NONE-_-NONE- (fabrication_designs_mexico_metal_screen_fire_door_3k_2015). Signed 2015-05-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15M1144_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_mexico_metal_screen_fire_door_3k_2015 USD 0.003m. Supports fabrication_designs_mexico_metal_screen_fire_door_3k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3348.0; date_signed 2015-05-19.",
)

# === Cycle 1221 ===
row_doc(
    "misc_dominican_ups_back_ups_13k_2020",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic UPS BACK UPS",
    "Dominican Republic",
    "8 Sep 2020: Department of State awards contract 19DR8620P1075 for UPS BACK UPS (PoP Dominican Republic); obligated USD 12750. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12750", "2020-09-08", "2020", "", "",
    "UPS BACK UPS, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_dominican_ups_back_ups_13k_2020",
    "UPS BACK UPS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8620P1075_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1221",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8620P1075_1900_-NONE-_-NONE- (misc_dominican_ups_back_ups_13k_2020). Signed 2020-09-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8620P1075_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_ups_back_ups_13k_2020 USD 0.013m. Supports misc_dominican_ups_back_ups_13k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12750.0; date_signed 2020-09-08.",
)

# === Cycle 1221 ===
row_doc(
    "misc_guatemala_usaid_electrical_distribution_upgrade_13k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Guatemala electrical distribution system upgrade in USAID building",
    "Guatemala",
    "29 Sep 2017: U.S. Agency for International Development awards contract AID520O1700091 for IGF::CL::IGF ELECTRICAL DISTRIBUTION SYSTEM UPGRADE IN THE USAID BUILDING (PoP Guatemala); obligated USD 12727.75. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12727.75", "2017-09-29", "2017", "", "",
    "IGF::CL::IGF ELECTRICAL DISTRIBUTION SYSTEM UPGRADE IN THE USAID BUILDING, Guatemala (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_guatemala_usaid_electrical_distribution_upgrade_13k_2017",
    "IGF::CL::IGF ELECTRICAL DISTRIBUTION SYSTEM UPGRADE IN THE USAID BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID520O1700091_7200_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1221",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID520O1700091_7200_-NONE-_-NONE- (misc_guatemala_usaid_electrical_distribution_upgrade_13k_2017). Signed 2017-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID520O1700091_7200_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_usaid_electrical_distribution_upgrade_13k_2017 USD 0.013m. Supports misc_guatemala_usaid_electrical_distribution_upgrade_13k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12727.75; date_signed 2017-09-29.",
)

# === Cycle 1221 ===
row_doc(
    "misc_colombia_ups_uninterruptible_power_supply_13k_2012",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Colombia uninterruptible power supply UPS",
    "Colombia",
    "21 Sep 2012: Department of Defense awards contract W913FT12P0367 for UNINTERRUPTIBLE POWER SUPPLY UPS (PoP Colombia); obligated USD 12704.72. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12704.72", "2012-09-21", "2012", "", "",
    "UNINTERRUPTIBLE POWER SUPPLY UPS, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_colombia_ups_uninterruptible_power_supply_13k_2012",
    "UNINTERRUPTIBLE POWER SUPPLY UPS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0367_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1221",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12P0367_9700_-NONE-_-NONE- (misc_colombia_ups_uninterruptible_power_supply_13k_2012). Signed 2012-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0367_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_ups_uninterruptible_power_supply_13k_2012 USD 0.013m. Supports misc_colombia_ups_uninterruptible_power_supply_13k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12704.72; date_signed 2012-09-21.",
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
        w.writeheader(); w.writerows(rows)
    EVID.mkdir(parents=True, exist_ok=True)
    for row, ev, _bib in ITEMS:
        (EVID / f"{row['id']}.json").write_text(json.dumps(ev, indent=2) + "\n", encoding="utf-8")
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
            bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")

if __name__ == "__main__":
    main()
