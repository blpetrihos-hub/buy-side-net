#!/usr/bin/env python3
"""Cycles 1224–1229: USASpending LatAm CapEx (US vendor stock + residual other).

Seeds: 20262224–20262229. Thin top-up dry.
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

# === Cycle 1224 ===
row_doc(
    "fortis_colombia_cctv_various_5p42m_2016",
    "infrastructure", "building_materials", "us",
    "Fortis Networks — Colombia CCTV systems at various locations",
    "Colombia",
    "17 Dec 2015: Department of State awards contract to FORTIS NETWORKS, INC. for installation of CCTV systems at various locations in Colombia (PoP Colombia); obligated USD 5419953.59. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.",
    "5419953.59", "2015-12-17", "2015", "", "",
    "INSTALLATION OF CCTV SYSTEMS AT VARIOUS LOCATIONS IN COLOMBIA, SERVICES CONSIDERED CRITICAL FUNCT..., Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_fortis_colombia_cctv_various_5p42m_2016",
    "INSTALLATION OF CCTV SYSTEMS AT VARIOUS LOCATIONS IN COLOMBIA, SERVICES CONSIDERED CRITICAL FUNCTIONS.  REFERENCE CLASSIFICATION CODE IGF::CT::IGF.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16C0002_1900_-NONE-_-NONE-/",
    "Actor: FORTIS NETWORKS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1224",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16C0002_1900_-NONE-_-NONE- (fortis_colombia_cctv_various_5p42m_2016). Signed 2015-12-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16C0002_1900_-NONE-_-NONE-/.",
    "USASpending: fortis_colombia_cctv_various_5p42m_2016 USD 5.420m. Supports fortis_colombia_cctv_various_5p42m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5419953.59; date_signed 2015-12-17.",
)

# === Cycle 1224 ===
row_doc(
    "hardline_sao_paulo_febr_1p40m_2015",
    "infrastructure", "building_materials", "us",
    "Hardline Nati Construction — São Paulo embassy FEBR R&R",
    "Brazil",
    "13 Aug 2015: Department of State awards task order to HARDLINE NATI CONSTRUCTION LLC for FEBR R&R project at U.S. Embassy São Paulo, Brazil (PoP Brazil); obligated USD 1399452. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "1399452", "2015-08-13", "2015", "", "",
    "IGF::OT::IGF NATI-HARDLINE (HNC, LLC) - SAQMMA14-D-0085- TO: SAQMMA15-F-2323- FEBR R&R PROJECT - ..., Brazil (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_hardline_sao_paulo_febr_1p40m_2015",
    "IGF::OT::IGF NATI-HARDLINE (HNC, LLC) - SAQMMA14-D-0085- TO: SAQMMA15-F-2323- FEBR R&R PROJECT - US EMBASSY SAO PAULO, BRAZIL - PERIOD OF PERFORMANCE - 18 MONTHS FROM ISSUANCE OF NTP  TO REMOVE AND REPLACE 15 FE/BR DOORS, ADD 2 PERIMETER CAC FIXED WINDOWS, REMOVE 4 NON-RATED COMPOUND CAC FIXED WINDOWS AND REPLACE THEM WITH 4 FE FIXED WINDOWS, AND TO REMOVE AND REPLACE 23 DELAMINATED/FOGGED FEBR GLAZING PANELS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F2323_1900_SAQMMA14D0085_1900/",
    "Actor: HARDLINE NATI CONSTRUCTION LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1224",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15F2323_1900_SAQMMA14D0085_1900 (hardline_sao_paulo_febr_1p40m_2015). Signed 2015-08-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F2323_1900_SAQMMA14D0085_1900/.",
    "USASpending: hardline_sao_paulo_febr_1p40m_2015 USD 1.399m. Supports hardline_sao_paulo_febr_1p40m_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1399452.0; date_signed 2015-08-13.",
)

# === Cycle 1224 ===
row_doc(
    "misc_el_salvador_grilles_doors_windows_izalco_13k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador manufacture grilles on doors and windows Izalco",
    "El Salvador",
    "7 Jun 2022: Department of State awards contract for manufacture grilles on doors and windows Izalco (PoP El Salvador); obligated USD 12998. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12998", "2022-06-07", "2022", "", "",
    "19ES6022P0502 RSO 5841  MANUFACTURE GRILLES ON DOORS AND WINDOWS IZALCO 3, El Salvador (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_el_salvador_grilles_doors_windows_izalco_13k_2022",
    "19ES6022P0502 RSO 5841  MANUFACTURE GRILLES ON DOORS AND WINDOWS IZALCO 3",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0502_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1224",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6022P0502_1900_-NONE-_-NONE- (misc_el_salvador_grilles_doors_windows_izalco_13k_2022). Signed 2022-06-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0502_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_grilles_doors_windows_izalco_13k_2022 USD 0.013m. Supports misc_el_salvador_grilles_doors_windows_izalco_13k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12998.0; date_signed 2022-06-07.",
)

# === Cycle 1224 ===
row_doc(
    "misc_colombia_concrete_slab_screening_cartagena_13k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia concrete slab and walkway screening facility Cartagena",
    "Colombia",
    "29 Sep 2017: Department of State awards contract for concrete slab and walkway screening facility Cartagena (PoP Colombia); obligated USD 12989.49. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12989.49", "2017-09-29", "2017", "", "",
    "CONCRETE SLAB AND WALKWA SCREENING FACILITY CARTAGENA, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_concrete_slab_screening_cartagena_13k_2017",
    "CONCRETE SLAB AND WALKWA SCREENING FACILITY CARTAGENA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20017C0009_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1224",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20017C0009_1900_-NONE-_-NONE- (misc_colombia_concrete_slab_screening_cartagena_13k_2017). Signed 2017-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20017C0009_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_concrete_slab_screening_cartagena_13k_2017 USD 0.013m. Supports misc_colombia_concrete_slab_screening_cartagena_13k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12989.49; date_signed 2017-09-29.",
)

# === Cycle 1224 ===
row_doc(
    "misc_honduras_security_system_doj_13k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Honduras DOJ security system",
    "Honduras",
    "21 Mar 2012: Department of State awards contract for DOJ security system (PoP Honduras); obligated USD 12983.76. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12983.76", "2012-03-21", "2012", "", "",
    "SECURITY SYSTEM - DOJ, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_honduras_security_system_doj_13k_2012",
    "SECURITY SYSTEM - DOJ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80012M0242_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1224",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80012M0242_1900_-NONE-_-NONE- (misc_honduras_security_system_doj_13k_2012). Signed 2012-03-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80012M0242_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_security_system_doj_13k_2012 USD 0.013m. Supports misc_honduras_security_system_doj_13k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12983.76; date_signed 2012-03-21.",
)

# === Cycle 1225 ===
row_doc(
    "olgoonik_belize_febr_doors_windows_1p40m_2013",
    "infrastructure", "building_materials", "us",
    "Olgoonik Specialty Contractors — Belize FE/BR doors and fixed windows replacement",
    "Belize",
    "28 Sep 2013: Department of State awards task order to OLGOONIK SPECIALTY CONTRACTORS LLC to replace (9) FE/BR doors and 30 fixed windows and two glazing panels (PoP Belize); obligated USD 1396595.35. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "1396595.35", "2013-09-28", "2013", "", "",
    "IGF::OT::IGF  REPLACE (9) FE/BR DOORS AND 30 FIXED WINDOWS AND TWO GLAZING PANELS IN THE CHANCERY..., Belize (USASpending description; site not named — lat/lon blank).",
    "usaspending_olgoonik_belize_febr_doors_windows_1p40m_2013",
    "IGF::OT::IGF  REPLACE (9) FE/BR DOORS AND 30 FIXED WINDOWS AND TWO GLAZING PANELS IN THE CHANCERY BUILDING AT BELMOPAN, BELIZE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F3952_1900_SAQMMA13D0124_1900/",
    "Actor: OLGOONIK SPECIALTY CONTRACTORS LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1225",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F3952_1900_SAQMMA13D0124_1900 (olgoonik_belize_febr_doors_windows_1p40m_2013). Signed 2013-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F3952_1900_SAQMMA13D0124_1900/.",
    "USASpending: olgoonik_belize_febr_doors_windows_1p40m_2013 USD 1.397m. Supports olgoonik_belize_febr_doors_windows_1p40m_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1396595.35; date_signed 2013-09-28.",
)

# === Cycle 1225 ===
row_doc(
    "us_pan_american_honduras_300kw_generator_465k_2022",
    "energy", "power_plants_grid", "us",
    "U.S. Pan American Solutions — Honduras 300 kW generator with ATS",
    "Honduras",
    "14 Sep 2022: Department of Defense awards contract to U.S. PAN AMERICAN SOLUTIONS LLC to provide one (1) ea 300 kW generator with ATS (PoP Honduras); obligated USD 465250. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "465250", "2022-09-14", "2022", "", "",
    "PROVIDE ONE(1) EA 300KW GENERATOR W/ATS, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_us_pan_american_honduras_300kw_generator_465k_2022",
    "PROVIDE ONE(1) EA 300KW GENERATOR W/ATS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM22P0030_9700_-NONE-_-NONE-/",
    "Actor: U.S. PAN AMERICAN SOLUTIONS LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1225",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM22P0030_9700_-NONE-_-NONE- (us_pan_american_honduras_300kw_generator_465k_2022). Signed 2022-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM22P0030_9700_-NONE-_-NONE-/.",
    "USASpending: us_pan_american_honduras_300kw_generator_465k_2022 USD 0.465m. Supports us_pan_american_honduras_300kw_generator_465k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 465250.0; date_signed 2022-09-14.",
)

# === Cycle 1225 ===
row_doc(
    "misc_chile_infrared_motion_sensors_res_13k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Chile RSO external infrared motion sensors for residential security",
    "Chile",
    "28 Sep 2012: Department of State awards contract for RSO external infrared motion sensors for residential security (PoP Chile); obligated USD 12918.99. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12918.99", "2012-09-28", "2012", "", "",
    "RSO/EXTERNAL INFRARED MOTION SENSORS FOR RES SECURITY, Chile (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_chile_infrared_motion_sensors_res_13k_2012",
    "RSO/EXTERNAL INFRARED MOTION SENSORS FOR RES SECURITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80012M1132_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1225",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCI80012M1132_1900_-NONE-_-NONE- (misc_chile_infrared_motion_sensors_res_13k_2012). Signed 2012-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80012M1132_1900_-NONE-_-NONE-/.",
    "USASpending: misc_chile_infrared_motion_sensors_res_13k_2012 USD 0.013m. Supports misc_chile_infrared_motion_sensors_res_13k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12918.99; date_signed 2012-09-28.",
)

# === Cycle 1225 ===
row_doc(
    "misc_colombia_ac_jungla_instructors_13k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Colombia air conditioning for Jungla instructors",
    "Colombia",
    "28 Mar 2016: Department of State awards contract for air conditioning for Jungla instructors (PoP Colombia); obligated USD 12897.61. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12897.61", "2016-03-28", "2016", "", "",
    "INTERD (Y-J) AIR CONDITIONING  FOR JUNGLA INSTRUCTORS, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_ac_jungla_instructors_13k_2016",
    "INTERD (Y-J) AIR CONDITIONING  FOR JUNGLA INSTRUCTORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15016M0275_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1225",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15016M0275_1900_-NONE-_-NONE- (misc_colombia_ac_jungla_instructors_13k_2016). Signed 2016-03-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15016M0275_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_ac_jungla_instructors_13k_2016 USD 0.013m. Supports misc_colombia_ac_jungla_instructors_13k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12897.61; date_signed 2016-03-28.",
)

# === Cycle 1225 ===
row_doc(
    "misc_peru_security_upgrades_rinconada_del_lago_13k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru security upgrades Rinconada del Lago 1480",
    "Peru",
    "13 Jan 2014: Department of State awards contract for security upgrades for Rinconada del Lago 1480 (PoP Peru); obligated USD 12895.71. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12895.71", "2014-01-13", "2014", "", "",
    "01/10-SECURITY UPGRADES FOR RINCONADA DEL LAGO 1480 IGF::CT::IGF, Peru (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_peru_security_upgrades_rinconada_del_lago_13k_2014",
    "01/10-SECURITY UPGRADES FOR RINCONADA DEL LAGO 1480 IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M0465_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1225",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50014M0465_1900_-NONE-_-NONE- (misc_peru_security_upgrades_rinconada_del_lago_13k_2014). Signed 2014-01-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M0465_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_security_upgrades_rinconada_del_lago_13k_2014 USD 0.013m. Supports misc_peru_security_upgrades_rinconada_del_lago_13k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12895.71; date_signed 2014-01-13.",
)

# === Cycle 1226 ===
row_doc(
    "regional_engineering_barbados_tw24_hvac_generators_298k_2024",
    "energy", "power_plants_grid", "us",
    "Regional Engineering Consultancy — Barbados Tradewinds 24 HVAC, power outlets, generators",
    "Barbados",
    "3 May 2024: Department of Defense awards contract to REGIONAL ENGINEERING CONSULTANCY INC for Tradewinds 24 HVAC, power outlets, generators (PoP Barbados); obligated USD 298222.85. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "298222.85", "2024-05-03", "2024", "", "",
    "TW 24 HVAC, POWER OUTLETS, GENERATORS, Barbados (USASpending description; site not named — lat/lon blank).",
    "usaspending_regional_engineering_barbados_tw24_hvac_generators_298k_2024",
    "TW 24 HVAC, POWER OUTLETS, GENERATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W569QE24P0024_9700_-NONE-_-NONE-/",
    "Actor: REGIONAL ENGINEERING CONSULTANCY INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1226",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W569QE24P0024_9700_-NONE-_-NONE- (regional_engineering_barbados_tw24_hvac_generators_298k_2024). Signed 2024-05-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W569QE24P0024_9700_-NONE-_-NONE-/.",
    "USASpending: regional_engineering_barbados_tw24_hvac_generators_298k_2024 USD 0.298m. Supports regional_engineering_barbados_tw24_hvac_generators_298k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 298222.85; date_signed 2024-05-03.",
)

# === Cycle 1226 ===
row_doc(
    "psi_colombia_generators_257k_2018",
    "energy", "power_plants_grid", "us",
    "Project Services International — Colombia generators",
    "Colombia",
    "4 Sep 2018: Department of Defense awards contract to PROJECT SERVICES INTERNATIONAL CORPORATION for generators (PoP Colombia); obligated USD 256791.41. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "256791.41", "2018-09-04", "2018", "", "",
    "GENERATORS, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_psi_colombia_generators_257k_2018",
    "GENERATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT18P0125_9700_-NONE-_-NONE-/",
    "Actor: PROJECT SERVICES INTERNATIONAL CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1226",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT18P0125_9700_-NONE-_-NONE- (psi_colombia_generators_257k_2018). Signed 2018-09-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT18P0125_9700_-NONE-_-NONE-/.",
    "USASpending: psi_colombia_generators_257k_2018 USD 0.257m. Supports psi_colombia_generators_257k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 256791.41; date_signed 2018-09-04.",
)

# === Cycle 1226 ===
row_doc(
    "misc_el_salvador_electrical_platform_escalon_13k_2020",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — El Salvador INL electrical platform device Escalon project",
    "El Salvador",
    "14 Dec 2020: Department of State awards contract for INL electrical platform device for Escalon project (MPP) (PoP El Salvador); obligated USD 12882. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12882", "2020-12-14", "2020", "", "",
    "INL - ELECTRICAL PLATFORM DEVICE FOR ESCALON PROJECT (MPP), El Salvador (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_el_salvador_electrical_platform_escalon_13k_2020",
    "INL - ELECTRICAL PLATFORM DEVICE FOR ESCALON PROJECT (MPP)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0125_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1226",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6021P0125_1900_-NONE-_-NONE- (misc_el_salvador_electrical_platform_escalon_13k_2020). Signed 2020-12-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0125_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_electrical_platform_escalon_13k_2020 USD 0.013m. Supports misc_el_salvador_electrical_platform_escalon_13k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12882.0; date_signed 2020-12-14.",
)

# === Cycle 1226 ===
row_doc(
    "misc_dominican_inl_security_syst_dncd_omega_13k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic INL internal security system DNCD Omega/DITD offices",
    "Dominican Republic",
    "29 Sep 2015: Department of State awards contract for INL internal security system DNCD Omega/DITD offices (PoP Dominican Republic); obligated USD 12866.52. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12866.52", "2015-09-29", "2015", "", "",
    "INL INTERNAL SECURITY SYST. DNCD OMEGA/DITD OFCES. IN23DRC IGF::CL::IGF FOR CLOSELY ASSOCIATED, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_inl_security_syst_dncd_omega_13k_2015",
    "INL INTERNAL SECURITY SYST. DNCD OMEGA/DITD OFCES. IN23DRC IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M2016_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1226",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86015M2016_1900_-NONE-_-NONE- (misc_dominican_inl_security_syst_dncd_omega_13k_2015). Signed 2015-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M2016_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_inl_security_syst_dncd_omega_13k_2015 USD 0.013m. Supports misc_dominican_inl_security_syst_dncd_omega_13k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12866.52; date_signed 2015-09-29.",
)

# === Cycle 1226 ===
row_doc(
    "misc_brazil_new_ac_equipment_obo610_13k_2020",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil new AC equipment and installation service OBO 610",
    "Brazil",
    "18 Dec 2020: Department of State awards contract for new AC equipment and installation service on OBO 610 (PoP Brazil); obligated USD 12799.57. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12799.57", "2020-12-18", "2020", "", "",
    "NEW AC EQUIPMENT AND INSTALLATION SERVICE ON OBO 610, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_new_ac_equipment_obo610_13k_2020",
    "NEW AC EQUIPMENT AND INSTALLATION SERVICE ON OBO 610",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9321P0089_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1226",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9321P0089_1900_-NONE-_-NONE- (misc_brazil_new_ac_equipment_obo610_13k_2020). Signed 2020-12-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9321P0089_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_new_ac_equipment_obo610_13k_2020 USD 0.013m. Supports misc_brazil_new_ac_equipment_obo610_13k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12799.57; date_signed 2020-12-18.",
)

# === Cycle 1227 ===
row_doc(
    "marathon_electric_mexico_generator_218k_2025",
    "energy", "power_plants_grid", "us",
    "Marathon Electric — Mexico generator",
    "Mexico",
    "18 Dec 2025: Department of Defense awards contract to MARATHON ELECTRIC LLC for generator (PoP Mexico); obligated USD 217822.92. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "217822.92", "2025-12-18", "2025", "", "",
    "GENERATOR, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_marathon_electric_mexico_generator_218k_2025",
    "GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPMYM226P5111_9700_-NONE-_-NONE-/",
    "Actor: MARATHON ELECTRIC LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1227",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPMYM226P5111_9700_-NONE-_-NONE- (marathon_electric_mexico_generator_218k_2025). Signed 2025-12-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPMYM226P5111_9700_-NONE-_-NONE-/.",
    "USASpending: marathon_electric_mexico_generator_218k_2025 USD 0.218m. Supports marathon_electric_mexico_generator_218k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 217822.92; date_signed 2025-12-18.",
)

# === Cycle 1227 ===
row_doc(
    "atelier4_guatemala_metal_door_screen_214k_2022",
    "infrastructure", "building_materials", "us",
    "Atelier 4 — Guatemala metal door screen for international embassies",
    "Guatemala",
    "23 May 2022: Department of State awards contract to ATELIER 4, LLC for metal door screen etc. for international embassies (PoP Guatemala); obligated USD 213618.72. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "213618.72", "2022-05-23", "2022", "", "",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES., Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_atelier4_guatemala_metal_door_screen_214k_2022",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0594_1900_-NONE-_-NONE-/",
    "Actor: ATELIER 4, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1227",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22P0594_1900_-NONE-_-NONE- (atelier4_guatemala_metal_door_screen_214k_2022). Signed 2022-05-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0594_1900_-NONE-_-NONE-/.",
    "USASpending: atelier4_guatemala_metal_door_screen_214k_2022 USD 0.214m. Supports atelier4_guatemala_metal_door_screen_214k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 213618.72; date_signed 2022-05-23.",
)

# === Cycle 1227 ===
row_doc(
    "misc_mexico_aphis_tij_electrical_setup_13k_2015",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico APHIS Tijuana electrical set up",
    "Mexico",
    "10 Sep 2015: Department of State awards contract for APHIS/TIJ electrical set up (PoP Mexico); obligated USD 12791.3. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12791.3", "2015-09-10", "2015", "", "",
    "APHIS/TIJ/ ELECTRICAL SET UP IGF::OT::IGF, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_aphis_tij_electrical_setup_13k_2015",
    "APHIS/TIJ/ ELECTRICAL SET UP IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX72015M0241_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1227",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX72015M0241_1900_-NONE-_-NONE- (misc_mexico_aphis_tij_electrical_setup_13k_2015). Signed 2015-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX72015M0241_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_aphis_tij_electrical_setup_13k_2015 USD 0.013m. Supports misc_mexico_aphis_tij_electrical_setup_13k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12791.3; date_signed 2015-09-10.",
)

# === Cycle 1227 ===
row_doc(
    "misc_bolivia_heat_pumps_motor_pool_13k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Bolivia heat pumps for motor pool compound",
    "Bolivia",
    "16 Sep 2013: Department of State awards contract for heat pumps for motor pool compound (PoP Bolivia); obligated USD 12781.69. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12781.69", "2013-09-16", "2013", "", "",
    "HEAT PUMPS FOR MOTOR POOL COMPOUND, Bolivia (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_bolivia_heat_pumps_motor_pool_13k_2013",
    "HEAT PUMPS FOR MOTOR POOL COMPOUND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40013M0577_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1227",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBL40013M0577_1900_-NONE-_-NONE- (misc_bolivia_heat_pumps_motor_pool_13k_2013). Signed 2013-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40013M0577_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bolivia_heat_pumps_motor_pool_13k_2013 USD 0.013m. Supports misc_bolivia_heat_pumps_motor_pool_13k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12781.69; date_signed 2013-09-16.",
)

# === Cycle 1227 ===
row_doc(
    "misc_brazil_electrical_meter_guard_shack_13k_2018",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil Rio NCC new electrical meter for guard shack",
    "Brazil",
    "9 Apr 2018: Department of State awards contract for Rio-FAC NCC new electrical meter for guard shack (PoP Brazil); obligated USD 12758.83. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12758.83", "2018-04-09", "2018", "", "",
    "RIO-FAC: NCC NEW ELECTRICAL METER FOR GUARD SHACK, Brazil (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_electrical_meter_guard_shack_13k_2018",
    "RIO-FAC: NCC NEW ELECTRICAL METER FOR GUARD SHACK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8218P0331_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1227",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR8218P0331_1900_-NONE-_-NONE- (misc_brazil_electrical_meter_guard_shack_13k_2018). Signed 2018-04-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8218P0331_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_electrical_meter_guard_shack_13k_2018 USD 0.013m. Supports misc_brazil_electrical_meter_guard_shack_13k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12758.83; date_signed 2018-04-09.",
)

# === Cycle 1228 ===
row_doc(
    "native_instinct_honduras_kohler_125kw_174k_2021",
    "energy", "power_plants_grid", "us",
    "Native Instinct — Honduras Kohler 125 kW generator",
    "Honduras",
    "27 Sep 2021: Department of Defense awards contract to NATIVE INSTINCT LLC for Kohler 125 kW generator (PoP Honduras); obligated USD 173709.72. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "173709.72", "2021-09-27", "2021", "", "",
    "KOHLER 125KW GENERATOR, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_native_instinct_honduras_kohler_125kw_174k_2021",
    "KOHLER 125KW GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM21F0072_9700_47QSWA19D00AP_4732/",
    "Actor: NATIVE INSTINCT LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1228",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM21F0072_9700_47QSWA19D00AP_4732 (native_instinct_honduras_kohler_125kw_174k_2021). Signed 2021-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM21F0072_9700_47QSWA19D00AP_4732/.",
    "USASpending: native_instinct_honduras_kohler_125kw_174k_2021 USD 0.174m. Supports native_instinct_honduras_kohler_125kw_174k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 173709.72; date_signed 2021-09-27.",
)

# === Cycle 1228 ===
row_doc(
    "millenium_jamaica_household_generator_108k_2010",
    "energy", "power_plants_grid", "us",
    "Millenium Products — Jamaica GSO household generator",
    "Jamaica",
    "30 Sep 2010: Department of State awards contract to MILLENIUM PRODUCTS, INC for GSO household generator (PoP Jamaica); obligated USD 108090. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "108090", "2010-09-30", "2010", "", "",
    "GSO - HOUSEHOLD GENERATOR (EOFY), Jamaica (USASpending description; site not named — lat/lon blank).",
    "usaspending_millenium_jamaica_household_generator_108k_2010",
    "GSO - HOUSEHOLD GENERATOR (EOFY)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37010F0017_1900_GS07F5791R_4730/",
    "Actor: MILLENIUM PRODUCTS, INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1228",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37010F0017_1900_GS07F5791R_4730 (millenium_jamaica_household_generator_108k_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37010F0017_1900_GS07F5791R_4730/.",
    "USASpending: millenium_jamaica_household_generator_108k_2010 USD 0.108m. Supports millenium_jamaica_household_generator_108k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 108090.0; date_signed 2010-09-30.",
)

# === Cycle 1228 ===
row_doc(
    "misc_brazil_renovation_project_13k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil renovation project",
    "Brazil",
    "6 Dec 2012: Department of State awards contract for renovation project (PoP Brazil); obligated USD 12607.67. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12607.67", "2012-12-06", "2012", "", "",
    "IGF::OT::IGF RENOVATION PROJECT, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_renovation_project_13k_2012",
    "IGF::OT::IGF RENOVATION PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82013F0001_1900_SBR82012D0003_1900/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1228",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82013F0001_1900_SBR82012D0003_1900 (misc_brazil_renovation_project_13k_2012). Signed 2012-12-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82013F0001_1900_SBR82012D0003_1900/.",
    "USASpending: misc_brazil_renovation_project_13k_2012 USD 0.013m. Supports misc_brazil_renovation_project_13k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12607.67; date_signed 2012-12-06.",
)

# === Cycle 1228 ===
row_doc(
    "misc_nicaragua_submersible_well_pump_13k_2023",
    "infrastructure", "water", "other",
    "Miscellaneous foreign awardees — Nicaragua submersible well pump and motor",
    "Nicaragua",
    "4 May 2023: Department of State awards contract for submersible well pump and motor (PoP Nicaragua); obligated USD 12586.82. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12586.82", "2023-05-04", "2023", "", "",
    "SUBMERGIBLE WELL PUMP AND MOTOR - FM, Nicaragua (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_nicaragua_submersible_well_pump_13k_2023",
    "SUBMERGIBLE WELL PUMP AND MOTOR - FM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NU7023P0193_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1228",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19NU7023P0193_1900_-NONE-_-NONE- (misc_nicaragua_submersible_well_pump_13k_2023). Signed 2023-05-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NU7023P0193_1900_-NONE-_-NONE-/.",
    "USASpending: misc_nicaragua_submersible_well_pump_13k_2023 USD 0.013m. Supports misc_nicaragua_submersible_well_pump_13k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12586.82; date_signed 2023-05-04.",
)

# === Cycle 1228 ===
row_doc(
    "misc_peru_dea_make_ready_gergye_11k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru DEA make-ready works Gergye",
    "Peru",
    "13 Oct 2011: Department of State awards contract for DEA make-ready works Gergye (PoP Peru); obligated USD 10989.01. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "10989.01", "2011-10-13", "2011", "", "",
    "10/11 DEA - MAKE-READY WORKS - GERGYE, Peru (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_peru_dea_make_ready_gergye_11k_2011",
    "10/11 DEA - MAKE-READY WORKS - GERGYE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50012M0015_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1228",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50012M0015_1900_-NONE-_-NONE- (misc_peru_dea_make_ready_gergye_11k_2011). Signed 2011-10-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50012M0015_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_dea_make_ready_gergye_11k_2011 USD 0.011m. Supports misc_peru_dea_make_ready_gergye_11k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10989.01; date_signed 2011-10-13.",
)

# === Cycle 1229 ===
row_doc(
    "rrds_colombia_portable_generators_104k_2020",
    "energy", "power_plants_grid", "us",
    "RRDS — Colombia INL portable generators",
    "Colombia",
    "28 Apr 2020: Department of State awards contract to RRDS INC for INL portable generators (PoP Colombia); obligated USD 104080. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "104080", "2020-04-28", "2020", "", "",
    "INL- PORTABLE GENERATORS, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_rrds_colombia_portable_generators_104k_2020",
    "INL- PORTABLE GENERATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520P0164_1900_-NONE-_-NONE-/",
    "Actor: RRDS INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1229",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01520P0164_1900_-NONE-_-NONE- (rrds_colombia_portable_generators_104k_2020). Signed 2020-04-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520P0164_1900_-NONE-_-NONE-/.",
    "USASpending: rrds_colombia_portable_generators_104k_2020 USD 0.104m. Supports rrds_colombia_portable_generators_104k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 104080.0; date_signed 2020-04-28.",
)

# === Cycle 1229 ===
row_doc(
    "bp_consort_brazil_ac_generator_102k_2020",
    "energy", "power_plants_grid", "us",
    "B & P Consort — Brazil AC generator",
    "Brazil",
    "2 Jul 2020: Department of Defense awards contract to B & P CONSORT, INC. for AC generator (PoP Brazil); obligated USD 101846.67. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "101846.67", "2020-07-02", "2020", "", "",
    "AC GENERATOR, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_bp_consort_brazil_ac_generator_102k_2020",
    "AC GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPMYM220P2209_9700_-NONE-_-NONE-/",
    "Actor: B & P CONSORT, INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1229",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPMYM220P2209_9700_-NONE-_-NONE- (bp_consort_brazil_ac_generator_102k_2020). Signed 2020-07-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPMYM220P2209_9700_-NONE-_-NONE-/.",
    "USASpending: bp_consort_brazil_ac_generator_102k_2020 USD 0.102m. Supports bp_consort_brazil_ac_generator_102k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 101846.67; date_signed 2020-07-02.",
)

# === Cycle 1229 ===
row_doc(
    "misc_brazil_motorpool_bathroom_renovation_11k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil motorpool bathroom renovation",
    "Brazil",
    "26 Jun 2017: Department of State awards contract for FAC motorpool bathroom renovation (PoP Brazil); obligated USD 10948.09. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "10948.09", "2017-06-26", "2017", "", "",
    "FAC - MOTORPOOL BATHROOM RENOVATION ''IGF::OT::IGF'', Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_motorpool_bathroom_renovation_11k_2017",
    "FAC - MOTORPOOL BATHROOM RENOVATION ''IGF::OT::IGF''",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M0825_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1229",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25017M0825_1900_-NONE-_-NONE- (misc_brazil_motorpool_bathroom_renovation_11k_2017). Signed 2017-06-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M0825_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_motorpool_bathroom_renovation_11k_2017 USD 0.011m. Supports misc_brazil_motorpool_bathroom_renovation_11k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10948.09; date_signed 2017-06-26.",
)

# === Cycle 1229 ===
row_doc(
    "misc_colombia_torre95_x50035_make_ready_13k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Torre 95 X50035 make-ready",
    "Colombia",
    "25 Apr 2023: Department of State awards contract for Torre 95 X50035 make-ready (PoP Colombia); obligated USD 13189.78. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13189.78", "2023-04-25", "2023", "", "",
    "PR11584290 - TORRE 95 X50035 - (MAINT & REP) MAKE READY, Colombia (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_torre95_x50035_make_ready_13k_2023",
    "PR11584290 - TORRE 95 X50035 - (MAINT & REP) MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02023P0855_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1229",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02023P0855_1900_-NONE-_-NONE- (misc_colombia_torre95_x50035_make_ready_13k_2023). Signed 2023-04-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02023P0855_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_torre95_x50035_make_ready_13k_2023 USD 0.013m. Supports misc_colombia_torre95_x50035_make_ready_13k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13189.78; date_signed 2023-04-25.",
)

# === Cycle 1229 ===
row_doc(
    "misc_colombia_rubber_floor_playground_14k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia rubber floor installation in playground area",
    "Colombia",
    "7 Sep 2016: Department of State awards contract for rubber floor installation in playground area (PoP Colombia); obligated USD 14148.01. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14148.01", "2016-09-07", "2016", "", "",
    "IGF::OT::IGF FAC_RUBBER FLOOR INSTALLATION IN PLAYGROUND AREA_IDX3003, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_colombia_rubber_floor_playground_14k_2016",
    "IGF::OT::IGF FAC_RUBBER FLOOR INSTALLATION IN PLAYGROUND AREA_IDX3003",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20016M0788_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1229",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20016M0788_1900_-NONE-_-NONE- (misc_colombia_rubber_floor_playground_14k_2016). Signed 2016-09-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20016M0788_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_rubber_floor_playground_14k_2016 USD 0.014m. Supports misc_colombia_rubber_floor_playground_14k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14148.01; date_signed 2016-09-07.",
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
