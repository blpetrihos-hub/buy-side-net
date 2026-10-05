#!/usr/bin/env python3
"""Cycles 1107–1109: USASpending LatAm CapEx residual (~USD0.028–0.055m).

Seeds: 20262107–20262109. Thin top-up dry. Includes Venezuela CMR chiller.
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


# === Cycle 1107 (seed 20262107) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "interface_colombia_bogota_embassy_carpet_tiles_30k_2016",
    "infrastructure", "building_materials", "us",
    'Interface Americas — Colombia US Embassy Bogota standard carpet tiles',
    "Colombia",
    '1 Feb 2016: Department of State awards contract SCO20016M0208 to Interface Americas Inc for standard carpet tiles for US Embassy Bogota offices (PoP Colombia); obligated USD 29,535.22. CapEx face = award obligation. Exact offices unnamed — lat/lon blank.',
    "29535.22", "2016-02-01", "2016", "", "",
    'Standard carpet tiles for US Embassy Bogota offices, Colombia (USASpending description; embassy named, office coords not stated — lat/lon blank).',
    "usaspending_interface_colombia_bogota_embassy_carpet_tiles_30k_2016",
    'FAC _ STANDARD CARPET TILES FOR US EMBASSY BOGOTA OFFICESIGF::CL::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20016M0208_1900_-NONE-_-NONE-/",
    'Actor: Interface Americas Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1107",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20016M0208_1900_-NONE-_-NONE- (interface_colombia_bogota_embassy_carpet_tiles_30k_2016). Signed 2016-02-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20016M0208_1900_-NONE-_-NONE-/.',
    'USASpending: interface_colombia_bogota_embassy_carpet_tiles_30k_2016 USD 0.030m. Supports interface_colombia_bogota_embassy_carpet_tiles_30k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 29535.22; date_signed 2016-02-01.',
)
row_doc(
    "harden_belize_metal_door_screen_29k_2024",
    "infrastructure", "building_materials", "us",
    'Harden Architectural Security Products — Belize metal door screen frame for international embassies',
    "Belize",
    '5 Sep 2024: Department of State awards contract 19AQMM24P0977 to Harden Architectural Security Products, LLC for metal door screen frame etc. for international embassies (PoP Belize); obligated USD 29,461. CapEx face = award obligation. Exact embassy site unnamed — lat/lon blank.',
    "29461", "2024-09-05", "2024", "", "",
    'Metal door screen frame for international embassies, Belize (USASpending description; embassy not named — lat/lon blank).',
    "usaspending_harden_belize_metal_door_screen_29k_2024",
    'METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIE.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0977_1900_-NONE-_-NONE-/",
    'Actor: Harden Architectural Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1107",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0977_1900_-NONE-_-NONE- (harden_belize_metal_door_screen_29k_2024). Signed 2024-09-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0977_1900_-NONE-_-NONE-/.',
    'USASpending: harden_belize_metal_door_screen_29k_2024 USD 0.029m. Supports harden_belize_metal_door_screen_29k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 29461; date_signed 2024-09-05.',
)
row_doc(
    "misc_uruguay_cmr_pool_barrier_53k_2011",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Uruguay CMR pool barrier safety improvements',
    "Uruguay",
    '21 Jun 2011: Department of State awards contract SUY60011C0500 for safety improvements on CMR pool barrier (PoP Uruguay); obligated USD 53,192. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.',
    "53192", "2011-06-21", "2011", "", "",
    'Safety improvements on CMR pool barrier, Uruguay (USASpending description; CMR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_uruguay_cmr_pool_barrier_53k_2011",
    "FM SAFETY IMPROVEMENTS ON CMR'S POOL BARRIER.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60011C0500_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1107",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SUY60011C0500_1900_-NONE-_-NONE- (misc_uruguay_cmr_pool_barrier_53k_2011). Signed 2011-06-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60011C0500_1900_-NONE-_-NONE-/.',
    'USASpending: misc_uruguay_cmr_pool_barrier_53k_2011 USD 0.053m. Supports misc_uruguay_cmr_pool_barrier_53k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53192; date_signed 2011-06-21.',
)
row_doc(
    "misc_peru_chancery_elevator_door_operators_53k_2010",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Peru chancery elevator door operators upgrade',
    "Peru",
    '10 Sep 2010: Department of State awards contract SBL40010M0744 to upgrade door operators for all 3 elevators at the chancery building (PoP Peru); obligated USD 52,836. CapEx face = award obligation. Exact chancery unnamed — lat/lon blank.',
    "52836", "2010-09-10", "2010", "", "",
    'Upgrade door operators for all 3 elevators at chancery building, Peru (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_misc_peru_chancery_elevator_door_operators_53k_2010",
    'UPGRADE THE DOOR OPERATORS FOR ALL 3 ELEVATORS AT THE CHANCERY BUILDING, LABOR HAND, PARTS, DISSASSEMBLY OF OLD PARTS, A',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40010M0744_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1107",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBL40010M0744_1900_-NONE-_-NONE- (misc_peru_chancery_elevator_door_operators_53k_2010). Signed 2010-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40010M0744_1900_-NONE-_-NONE-/.',
    'USASpending: misc_peru_chancery_elevator_door_operators_53k_2010 USD 0.053m. Supports misc_peru_chancery_elevator_door_operators_53k_2010.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 52836; date_signed 2010-09-10.',
)
row_doc(
    "misc_bahamas_cmr_tile_52k_2014",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Bahamas CMR material and labour to tile CMR',
    "Bahamas",
    '31 Jan 2014: Department of State awards contract SBF50014M0250 for material and labour to tile CMR (PoP Bahamas); obligated USD 52,061. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.',
    "52061", "2014-01-31", "2014", "", "",
    'Material and labour to tile CMR, Bahamas (USASpending description; CMR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_bahamas_cmr_tile_52k_2014",
    'C-CMR - MATERIAL AND LABOUR TO TILE CMR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50014M0250_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1107",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50014M0250_1900_-NONE-_-NONE- (misc_bahamas_cmr_tile_52k_2014). Signed 2014-01-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50014M0250_1900_-NONE-_-NONE-/.',
    'USASpending: misc_bahamas_cmr_tile_52k_2014 USD 0.052m. Supports misc_bahamas_cmr_tile_52k_2014.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 52061; date_signed 2014-01-31.',
)

# === Cycle 1108 (seed 20262108) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_brazil_febr_door_cac_nurse_29k_2018",
    "infrastructure", "building_materials", "us",
    'Norshield Security Products — Brazil FE/BR door CAC and nurse (RCIP)',
    "Brazil",
    '25 Sep 2018: Department of State awards contract 19BR8118P0410 to Norshield Security Products, LLC for RCIP FE/BR door CAC + nurse XJ0H0002 and XJ0H0003 (PoP Brazil); obligated USD 29,160. CapEx face = award obligation. Exact CAC/nurse sites unnamed — lat/lon blank.',
    "29160", "2018-09-25", "2018", "", "",
    'RCIP FE/BR door CAC + nurse projects XJ0H0002 and XJ0H0003, Brazil (USASpending description; project codes named, site coords not stated — lat/lon blank).',
    "usaspending_norshield_brazil_febr_door_cac_nurse_29k_2018",
    'RCIP - FEBR DOOR CAC + NURSE XJ0H0002 AND XJ0H0003',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8118P0410_1900_-NONE-_-NONE-/",
    'Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1108",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR8118P0410_1900_-NONE-_-NONE- (norshield_brazil_febr_door_cac_nurse_29k_2018). Signed 2018-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8118P0410_1900_-NONE-_-NONE-/.',
    'USASpending: norshield_brazil_febr_door_cac_nurse_29k_2018 USD 0.029m. Supports norshield_brazil_febr_door_cac_nurse_29k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 29160; date_signed 2018-09-25.',
)
row_doc(
    "lotus_argentina_grundfos_water_pumps_29k_2024",
    "resources", "water", "us",
    'Lotus Logistics — Argentina FAC Grundfos water pumps',
    "Argentina",
    '15 Apr 2024: Department of State awards contract 19AR2024P0520 to Lotus Logistics LLC for Grundfos water pumps (PoP Argentina); obligated USD 29,076. CapEx face = award obligation. Exact pump sites unnamed — lat/lon blank.',
    "29076", "2024-04-15", "2024", "", "",
    'FAC Grundfos water pumps, Argentina (USASpending description; sites not named — lat/lon blank).',
    "usaspending_lotus_argentina_grundfos_water_pumps_29k_2024",
    'FAC - GRUNDFOS WATER PUMPS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2024P0520_1900_-NONE-_-NONE-/",
    'Actor: Lotus Logistics LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1108",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2024P0520_1900_-NONE-_-NONE- (lotus_argentina_grundfos_water_pumps_29k_2024). Signed 2024-04-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2024P0520_1900_-NONE-_-NONE-/.',
    'USASpending: lotus_argentina_grundfos_water_pumps_29k_2024 USD 0.029m. Supports lotus_argentina_grundfos_water_pumps_29k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 29076; date_signed 2024-04-15.',
)
row_doc(
    "misc_venezuela_cmr_chiller_install_52k_2010",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Venezuela CMR chiller installation',
    "Venezuela",
    '19 May 2010: Department of State awards contract SVE30010M0433 for chiller installation at CMR (PoP Venezuela); obligated USD 51,949.32. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.',
    "51949.32", "2010-05-19", "2010", "", "",
    'Chiller installation at CMR, Venezuela (USASpending description; CMR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_venezuela_cmr_chiller_install_52k_2010",
    'FM - CHILLER INSTALLATION AT CMR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30010M0433_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Weight under-covered Venezuela beyond solar.',
    "hunt_cycle1108",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30010M0433_1900_-NONE-_-NONE- (misc_venezuela_cmr_chiller_install_52k_2010). Signed 2010-05-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30010M0433_1900_-NONE-_-NONE-/.',
    'USASpending: misc_venezuela_cmr_chiller_install_52k_2010 USD 0.052m. Supports misc_venezuela_cmr_chiller_install_52k_2010.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 51949.32; date_signed 2010-05-19.',
)
row_doc(
    "misc_barbados_hurricane_shutters_install_51k_2021",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Barbados hurricane shutters installation',
    "Barbados",
    '21 Jul 2021: Department of State awards contract 19BB2121C0014 for installation of hurricane shutters (PoP Barbados); obligated USD 51,483.03. CapEx face = award obligation. Exact building unnamed — lat/lon blank.',
    "51483.03", "2021-07-21", "2021", "", "",
    'Installation of hurricane shutters, Barbados (USASpending description; building not named — lat/lon blank).',
    "usaspending_misc_barbados_hurricane_shutters_install_51k_2021",
    'INSTALLATION - HURRICANE SHUTTERS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2121C0014_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1108",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BB2121C0014_1900_-NONE-_-NONE- (misc_barbados_hurricane_shutters_install_51k_2021). Signed 2021-07-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2121C0014_1900_-NONE-_-NONE-/.',
    'USASpending: misc_barbados_hurricane_shutters_install_51k_2021 USD 0.051m. Supports misc_barbados_hurricane_shutters_install_51k_2021.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 51483.03; date_signed 2021-07-21.',
)
row_doc(
    "misc_bahamas_residential_generator_install_51k_2017",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Bahamas residential generator installation',
    "Bahamas",
    '12 Sep 2017: Department of State awards contract SBF50017C0003 for residential generator installation (PoP Bahamas); obligated USD 51,143.72. CapEx face = award obligation. Exact residence unnamed — lat/lon blank.',
    "51143.72", "2017-09-12", "2017", "", "",
    'Residential generator installation, Bahamas (USASpending description; residence not named — lat/lon blank).',
    "usaspending_misc_bahamas_residential_generator_install_51k_2017",
    'IGF::OT::IGF RESIDENTIAL GENERATOR INSTALLATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017C0003_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1108",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50017C0003_1900_-NONE-_-NONE- (misc_bahamas_residential_generator_install_51k_2017). Signed 2017-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017C0003_1900_-NONE-_-NONE-/.',
    'USASpending: misc_bahamas_residential_generator_install_51k_2017 USD 0.051m. Supports misc_bahamas_residential_generator_install_51k_2017.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 51143.72; date_signed 2017-09-12.',
)

# === Cycle 1109 (seed 20262109) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "jeff_smith_brazil_recife_febr_window_28k_2024",
    "infrastructure", "building_materials", "us",
    'Jeff Smith Enterprises — Brazil Recife consulate FE/BR window installation',
    "Brazil",
    '27 Sep 2024: Department of State awards contract 19BR8124P0372 to Jeff Smith Enterprises LLC for FE/BR window installation at U.S. Consulate Recife (PoP Brazil); obligated USD 28,311. CapEx face = award obligation. Exact consulate site unnamed — lat/lon blank.',
    "28311", "2024-09-27", "2024", "", "",
    'FE/BR window installation at U.S. Consulate Recife, Brazil (USASpending description; Recife named, site coords not stated — lat/lon blank).',
    "usaspending_jeff_smith_brazil_recife_febr_window_28k_2024",
    'FE/BR WINDOW INSTALLATION AT U.S. CONSULATE RECIFE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8124P0372_1900_-NONE-_-NONE-/",
    'Actor: Jeff Smith Enterprises LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1109",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR8124P0372_1900_-NONE-_-NONE- (jeff_smith_brazil_recife_febr_window_28k_2024). Signed 2024-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8124P0372_1900_-NONE-_-NONE-/.',
    'USASpending: jeff_smith_brazil_recife_febr_window_28k_2024 USD 0.028m. Supports jeff_smith_brazil_recife_febr_window_28k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 28311; date_signed 2024-09-27.',
)
row_doc(
    "solar_direct_jamaica_solar_pump_pool_28k_2013",
    "energy", "other_renewables", "us",
    'Solar Direct — Jamaica solar pump and pool treatment system',
    "Jamaica",
    '28 Aug 2013: Department of State awards contract SJM37013M1029 to Solar Direct, Inc. for solar pump and pool treatment system PPLZ (PoP Jamaica); obligated USD 28,000. CapEx face = award obligation. Exact pool site unnamed — lat/lon blank.',
    "28000", "2013-08-28", "2013", "", "",
    'Solar pump and pool treatment system PPLZ, Jamaica (USASpending description; site not named — lat/lon blank).',
    "usaspending_solar_direct_jamaica_solar_pump_pool_28k_2013",
    'IGF::OT::IGF FAC - SOLAR PUMP AND POOL TREATMENT SYSTEM PPLZ (7901.3)',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37013M1029_1900_-NONE-_-NONE-/",
    'Actor: Solar Direct, Inc. (U.S.) — us. Official USASpending Award API. Shuffle other_renewables; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1109",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37013M1029_1900_-NONE-_-NONE- (solar_direct_jamaica_solar_pump_pool_28k_2013). Signed 2013-08-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37013M1029_1900_-NONE-_-NONE-/.',
    'USASpending: solar_direct_jamaica_solar_pump_pool_28k_2013 USD 0.028m. Supports solar_direct_jamaica_solar_pump_pool_28k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 28000; date_signed 2013-08-28.',
)
row_doc(
    "misc_bahamas_msg_windows_install_51k_2016",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Bahamas MSG install windows at Marine residence',
    "Bahamas",
    '30 Sep 2016: Department of State awards contract SBF50016M1183 to install windows at Marine residence (PoP Bahamas); obligated USD 50,843.29. CapEx face = award obligation. Exact Marine residence unnamed — lat/lon blank.',
    "50843.29", "2016-09-30", "2016", "", "",
    'MSG install windows at Marine residence, Bahamas (USASpending description; residence not named — lat/lon blank).',
    "usaspending_misc_bahamas_msg_windows_install_51k_2016",
    'IGF::OT::IGF MSG - INSTALL WINDOWS AT MARINE RESIDENCE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50016M1183_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1109",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50016M1183_1900_-NONE-_-NONE- (misc_bahamas_msg_windows_install_51k_2016). Signed 2016-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50016M1183_1900_-NONE-_-NONE-/.',
    'USASpending: misc_bahamas_msg_windows_install_51k_2016 USD 0.051m. Supports misc_bahamas_msg_windows_install_51k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 50843.29; date_signed 2016-09-30.',
)
row_doc(
    "misc_panama_exhibit_av_install_55k_2023",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Panama supply and installation of audiovisual equipment for exhibit',
    "Panama",
    '26 Jul 2023: Smithsonian awards contract 33330523P00494468 for supply and installation of audiovisual equipment-exhibit (PoP Panama); obligated USD 54,755.31. CapEx face = award obligation. Exact exhibit site unnamed — lat/lon blank.',
    "54755.31", "2023-07-26", "2023", "", "",
    'Supply and installation of audiovisual equipment for exhibit, Panama (USASpending description; exhibit not named — lat/lon blank).',
    "usaspending_misc_panama_exhibit_av_install_55k_2023",
    'SUPPLY AND INSTALLATION OF AUDIOVISUAL EQUIPMENT-EXHIBIT',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330523P00494468_3300_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1109",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330523P00494468_3300_-NONE-_-NONE- (misc_panama_exhibit_av_install_55k_2023). Signed 2023-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330523P00494468_3300_-NONE-_-NONE-/.',
    'USASpending: misc_panama_exhibit_av_install_55k_2023 USD 0.055m. Supports misc_panama_exhibit_av_install_55k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 54755.31; date_signed 2023-07-26.',
)
row_doc(
    "misc_peru_usaid_office_renovation_28k_2024",
    "infrastructure", "building_materials", "other",
    'Foreign awardees (undisclosed) — Peru USAID office renovation',
    "Peru",
    '19 Jan 2024: USAID awards contract 72052724P00009 to foreign awardees (undisclosed) for USAID office renovation according to scope of work (PoP Peru); obligated USD 27,923.21. CapEx face = award obligation. Exact office unnamed — lat/lon blank.',
    "27923.21", "2024-01-19", "2024", "", "",
    'USAID office renovation according to scope of work, Peru (USASpending description; office not named — lat/lon blank).',
    "usaspending_misc_peru_usaid_office_renovation_28k_2024",
    'USAID OFFICE RENOVATION ACCORDING TO SCOPE OF WORK.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_72052724P00009_7200_-NONE-_-NONE-/",
    'Actor: foreign awardees (undisclosed) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1109",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_72052724P00009_7200_-NONE-_-NONE- (misc_peru_usaid_office_renovation_28k_2024). Signed 2024-01-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_72052724P00009_7200_-NONE-_-NONE-/.',
    'USASpending: misc_peru_usaid_office_renovation_28k_2024 USD 0.028m. Supports misc_peru_usaid_office_renovation_28k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27923.21; date_signed 2024-01-19.',
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
