#!/usr/bin/env python3
"""Cycles 1274–1279: USASpending LatAm CapEx (ICS/Alutiiq/Futron/KVA/Human Tech/EMR + residual other).

Seeds: 20262274–20262279. Thin top-up dry. Consular expansion / forensics equipment / electrical CapEx + misc other.
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

# === Cycle 1274 ===
row_doc(
    "ics_brazil_rio_consular_expansion_8745k_2012",
    "infrastructure", "building_materials", "us",
    "International Construction Services — Rio de Janeiro consular expansion",
    "Brazil",
    "26 Apr 2012: Department of State awards contract to INTERNATIONAL CONSTRUCTION SERVICES, LLC for Rio de Janeiro consular expansion project (PoP Brazil); obligated USD 8745844. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "8745844", "2012-04-26", "2012", "", "",
    "RIO DE JANEIRO CONSULAR EXPANSION PROJECT, RIO DE JANEIRO, BRAZIL. IMPROVEMENTS TO CONSULAR AREA AND NEW WORK , Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_ics_brazil_rio_consular_expansion_8745k_2012",
    "RIO DE JANEIRO CONSULAR EXPANSION PROJECT, RIO DE JANEIRO, BRAZIL. IMPROVEMENTS TO CONSULAR AREA AND NEW WORK STATIONS TO ACCOMODATE INCREASED CONSULAR OFFICE STAFFING.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F0732_1900_SAQMMA08D0005_1900/",
    "Actor: INTERNATIONAL CONSTRUCTION SERVICES, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1274",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F0732_1900_SAQMMA08D0005_1900 (ics_brazil_rio_consular_expansion_8745k_2012). Signed 2012-04-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F0732_1900_SAQMMA08D0005_1900/.",
    "USASpending: ics_brazil_rio_consular_expansion_8745k_2012 USD 8.746m. Supports ics_brazil_rio_consular_expansion_8745k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8745844.0; date_signed 2012-04-26.",
    investment_type="epc",
)

# === Cycle 1274 ===
row_doc(
    "ics_brazil_sao_paulo_consular_expansion_6384k_2012",
    "infrastructure", "building_materials", "us",
    "International Construction Services — São Paulo consular expansion",
    "Brazil",
    "17 Apr 2012: Department of State awards contract to INTERNATIONAL CONSTRUCTION SERVICES, LLC for São Paulo consular expansion project (PoP Brazil); obligated USD 6384387. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "6384387", "2012-04-17", "2012", "", "",
    "SAO PAULO CONSULAR EXPANSION PROJECT, SAO PAULO, BRAZIL.  IMPROVEMENTS TO CONSULAR AREA AND NEW WORK STATIONS , Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_ics_brazil_sao_paulo_consular_expansion_6384k_2012",
    "SAO PAULO CONSULAR EXPANSION PROJECT, SAO PAULO, BRAZIL.  IMPROVEMENTS TO CONSULAR AREA AND NEW WORK STATIONS TO ACCOMODATE INCREASED CONSULAR OFFICE STAFFING.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F0731_1900_SAQMMA08D0005_1900/",
    "Actor: INTERNATIONAL CONSTRUCTION SERVICES, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1274",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F0731_1900_SAQMMA08D0005_1900 (ics_brazil_sao_paulo_consular_expansion_6384k_2012). Signed 2012-04-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F0731_1900_SAQMMA08D0005_1900/.",
    "USASpending: ics_brazil_sao_paulo_consular_expansion_6384k_2012 USD 6.384m. Supports ics_brazil_sao_paulo_consular_expansion_6384k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6384387.0; date_signed 2012-04-17.",
    investment_type="epc",
)

# === Cycle 1274 ===
row_doc(
    "misc_brazil_fire_alarm_project_124k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil fire alarm project",
    "Brazil",
    "22 Sep 2017: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for fire alarm project (PoP Brazil); obligated USD 124321.74. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "124321.74", "2017-09-22", "2017", "", "",
    "113 FIRE ALARM PROJECT ''IGF::OT::IGF'', Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_fire_alarm_project_124k_2017",
    "113 FIRE ALARM PROJECT ''IGF::OT::IGF''",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M1178_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1274",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25017M1178_1900_-NONE-_-NONE- (misc_brazil_fire_alarm_project_124k_2017). Signed 2017-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M1178_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_fire_alarm_project_124k_2017 USD 0.124m. Supports misc_brazil_fire_alarm_project_124k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 124321.74; date_signed 2017-09-22.",
    investment_type="epc",
)

# === Cycle 1274 ===
row_doc(
    "misc_bahamas_ship_ahoy_roof_98k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas Ship Ahoy roof replacement",
    "Bahamas",
    "20 Jun 2017: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for roof replacement at Ship Ahoy (PoP Bahamas); obligated USD 98792.50. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "98792.50", "2017-06-20", "2017", "", "",
    "IGF::OT::IGF ROOF REPLACEMENT AT SHIP AHOY, Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_bahamas_ship_ahoy_roof_98k_2017",
    "IGF::OT::IGF ROOF REPLACEMENT AT SHIP AHOY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017C0008_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1274",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50017C0008_1900_-NONE-_-NONE- (misc_bahamas_ship_ahoy_roof_98k_2017). Signed 2017-06-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017C0008_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_ship_ahoy_roof_98k_2017 USD 0.099m. Supports misc_bahamas_ship_ahoy_roof_98k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 98792.5; date_signed 2017-06-20.",
    investment_type="epc",
)

# === Cycle 1274 ===
row_doc(
    "misc_mexico_musset_elevator_replacement_91k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Musset elevator replacement",
    "Mexico",
    "11 Jul 2023: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for Musset elevator replacement FY23 (PoP Mexico); obligated USD 91850.34. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "91850.34", "2023-07-11", "2023", "", "",
    "MEX-FAC-7903RSTR-FWP605-MUS-ELEVATOR REPLACEMENT-FY23, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_musset_elevator_replacement_91k_2023",
    "MEX-FAC-7903RSTR-FWP605-MUS-ELEVATOR REPLACEMENT-FY23",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5323P1083_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1274",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5323P1083_1900_-NONE-_-NONE- (misc_mexico_musset_elevator_replacement_91k_2023). Signed 2023-07-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5323P1083_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_musset_elevator_replacement_91k_2023 USD 0.092m. Supports misc_mexico_musset_elevator_replacement_91k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 91850.34; date_signed 2023-07-11.",
    investment_type="equipment_supply",
)

# === Cycle 1275 ===
row_doc(
    "alutiiq_mexico_testing_equipment_9000k_2020",
    "infrastructure", "building_materials", "us",
    "Alutiiq — Mexico testing equipment",
    "Mexico",
    "26 May 2020: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for testing equipment (PoP Mexico); obligated USD 9000855.53. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "9000855.53", "2020-05-26", "2020", "", "",
    "TESTING EQUIPMENT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_testing_equipment_9000k_2020",
    "TESTING EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0083_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1275",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20C0083_1900_-NONE-_-NONE- (alutiiq_mexico_testing_equipment_9000k_2020). Signed 2020-05-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0083_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_testing_equipment_9000k_2020 USD 9.001m. Supports alutiiq_mexico_testing_equipment_9000k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9000855.53; date_signed 2020-05-26.",
    investment_type="equipment_supply",
)

# === Cycle 1275 ===
row_doc(
    "alutiiq_mexico_it_hardware_install_5303k_2023",
    "infrastructure", "building_materials", "us",
    "Alutiiq — Mexico IT hardware/software installation for Comisión Nacional",
    "Mexico",
    "6 Mar 2023: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for IT hardware and software installation in support of Comisión Nacional (PoP Mexico); obligated USD 5303361.94. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "5303361.94", "2023-03-06", "2023", "", "",
    "IT HARDWARE AND SOFTWARE INSTALLATION IN SUPPORT OF COMISION NACIONAL DE TRIBUNALES CONATRIB., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_it_hardware_install_5303k_2023",
    "IT HARDWARE AND SOFTWARE INSTALLATION IN SUPPORT OF COMISION NACIONAL DE TRIBUNALES CONATRIB.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5004_1900_19AQMM20D0010_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1275",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMR23F5004_1900_19AQMM20D0010_1900 (alutiiq_mexico_it_hardware_install_5303k_2023). Signed 2023-03-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5004_1900_19AQMM20D0010_1900/.",
    "USASpending: alutiiq_mexico_it_hardware_install_5303k_2023 USD 5.303m. Supports alutiiq_mexico_it_hardware_install_5303k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5303361.94; date_signed 2023-03-06.",
    investment_type="equipment_supply",
)

# === Cycle 1275 ===
row_doc(
    "misc_belize_milgroup_roof_80k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Belize U.S. Military Group roof replacement",
    "Belize",
    "23 Sep 2010: Department of Defense awards contract to MISCELLANEOUS FOREIGN AWARDEES for roof replacement at US Military Group (PoP Belize); obligated USD 80587.89. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "80587.89", "2010-09-23", "2010", "", "",
    "ROOF REPLACEMENT AT US MILITARY GROUP, Belize (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_belize_milgroup_roof_80k_2010",
    "ROOF REPLACEMENT AT US MILITARY GROUP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0030_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1275",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0030_9700_-NONE-_-NONE- (misc_belize_milgroup_roof_80k_2010). Signed 2010-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0030_9700_-NONE-_-NONE-/.",
    "USASpending: misc_belize_milgroup_roof_80k_2010 USD 0.081m. Supports misc_belize_milgroup_roof_80k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 80587.89; date_signed 2010-09-23.",
    investment_type="epc",
)

# === Cycle 1275 ===
row_doc(
    "misc_bahamas_residential_generator_install_47k_2023",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Bahamas residential generator installation",
    "Bahamas",
    "1 Mar 2023: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for residential generator installation (PoP Bahamas); obligated USD 47160.52. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "47160.52", "2023-03-01", "2023", "", "",
    "10301-8/802 RESIDENTIAL GENERATOR INSTALLATION, Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_bahamas_residential_generator_install_47k_2023",
    "10301-8/802 RESIDENTIAL GENERATOR INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5023P0261_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1275",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BF5023P0261_1900_-NONE-_-NONE- (misc_bahamas_residential_generator_install_47k_2023). Signed 2023-03-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5023P0261_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_residential_generator_install_47k_2023 USD 0.047m. Supports misc_bahamas_residential_generator_install_47k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 47160.52; date_signed 2023-03-01.",
    investment_type="equipment_supply",
)

# === Cycle 1275 ===
row_doc(
    "misc_ecuador_residence_roof_x141_44k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador residence X-141 total roof replacement",
    "Ecuador",
    "6 May 2019: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for total roof replacement at residence X-141 (PoP Ecuador); obligated USD 44477.71. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "44477.71", "2019-05-06", "2019", "", "",
    "TOTAL ROOF REPLACEMENT AT RESIDENCE X-141, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_ecuador_residence_roof_x141_44k_2019",
    "TOTAL ROOF REPLACEMENT AT RESIDENCE X-141",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3019P0243_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1275",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3019P0243_1900_-NONE-_-NONE- (misc_ecuador_residence_roof_x141_44k_2019). Signed 2019-05-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3019P0243_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_residence_roof_x141_44k_2019 USD 0.044m. Supports misc_ecuador_residence_roof_x141_44k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 44477.71; date_signed 2019-05-06.",
    investment_type="epc",
)

# === Cycle 1276 ===
row_doc(
    "continuity_mexico_biometrics_hardware_3276k_2018",
    "infrastructure", "building_materials", "us",
    "Continuity Global — Mexico DHS INL biometrics hardware/servers/equipment",
    "Mexico",
    "30 Sep 2018: Department of Defense awards contract to CONTINUITY GLOBAL SOLUTIONS LLC for DHS INL biometrics hardware, servers and equipment (PoP Mexico); obligated USD 3276710. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3276710", "2018-09-30", "2018", "", "",
    "DHS INL BIOMETRICS HARDWARE, SERVERS AND EQUIPMENT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_continuity_mexico_biometrics_hardware_3276k_2018",
    "DHS INL BIOMETRICS HARDWARE, SERVERS AND EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489018F3007_9700_FA489016D0012_9700/",
    "Actor: CONTINUITY GLOBAL SOLUTIONS LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1276",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489018F3007_9700_FA489016D0012_9700 (continuity_mexico_biometrics_hardware_3276k_2018). Signed 2018-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489018F3007_9700_FA489016D0012_9700/.",
    "USASpending: continuity_mexico_biometrics_hardware_3276k_2018 USD 3.277m. Supports continuity_mexico_biometrics_hardware_3276k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3276710.0; date_signed 2018-09-30.",
    investment_type="equipment_supply",
)

# === Cycle 1276 ===
row_doc(
    "alutiiq_mexico_fingerprint_equipment_3193k_2022",
    "infrastructure", "building_materials", "us",
    "Alutiiq — Mexico GOM forensic laboratories fingerprint equipment",
    "Mexico",
    "28 Feb 2022: Department of State awards contract to ALUTIIQ TECHNICAL SERVICES LLC for fingerprint equipment GOM forensic laboratories (PoP Mexico); obligated USD 3193107.47. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3193107.47", "2022-02-28", "2022", "", "",
    "FINGERPRINT EQUIPMENT GOM FORENSIC LABORATORIES, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_fingerprint_equipment_3193k_2022",
    "FINGERPRINT EQUIPMENT GOM FORENSIC LABORATORIES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR22F5005_1900_19AQMM21D0040_1900/",
    "Actor: ALUTIIQ TECHNICAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1276",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMR22F5005_1900_19AQMM21D0040_1900 (alutiiq_mexico_fingerprint_equipment_3193k_2022). Signed 2022-02-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR22F5005_1900_19AQMM21D0040_1900/.",
    "USASpending: alutiiq_mexico_fingerprint_equipment_3193k_2022 USD 3.193m. Supports alutiiq_mexico_fingerprint_equipment_3193k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3193107.47; date_signed 2022-02-28.",
    investment_type="equipment_supply",
)

# === Cycle 1276 ===
row_doc(
    "misc_brazil_rio_switchgear_replacement_41k_2014",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Rio switchgear replacement light work",
    "Brazil",
    "22 Oct 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for Rio switchgear replacement light work (PoP Brazil); obligated USD 41515.40. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "41515.40", "2014-10-22", "2014", "", "",
    "IGF::CT::IGF RIO SWITCHGEAR REPLACEMENT LIGHT WORK - PROJECT FUNDS, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_rio_switchgear_replacement_41k_2014",
    "IGF::CT::IGF RIO SWITCHGEAR REPLACEMENT LIGHT WORK - PROJECT FUNDS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82015M0024_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1276",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82015M0024_1900_-NONE-_-NONE- (misc_brazil_rio_switchgear_replacement_41k_2014). Signed 2014-10-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82015M0024_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_rio_switchgear_replacement_41k_2014 USD 0.042m. Supports misc_brazil_rio_switchgear_replacement_41k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 41515.4; date_signed 2014-10-22.",
    investment_type="epc",
)

# === Cycle 1276 ===
row_doc(
    "misc_ecuador_residence_roof_x141b_39k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador residence X-141 new total roof replacement",
    "Ecuador",
    "27 Sep 2019: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for new total roof replacement X-141 (PoP Ecuador); obligated USD 39718.55. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "39718.55", "2019-09-27", "2019", "", "",
    "NEW TOTAL ROOF REPLACEMENT X-141, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_ecuador_residence_roof_x141b_39k_2019",
    "NEW TOTAL ROOF REPLACEMENT X-141",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3019P0578_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1276",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3019P0578_1900_-NONE-_-NONE- (misc_ecuador_residence_roof_x141b_39k_2019). Signed 2019-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3019P0578_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_residence_roof_x141b_39k_2019 USD 0.040m. Supports misc_ecuador_residence_roof_x141b_39k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 39718.55; date_signed 2019-09-27.",
    investment_type="epc",
)

# === Cycle 1276 ===
row_doc(
    "misc_ecuador_cbp_generators_install_31k_2020",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Ecuador CBP CSI residences generators installation",
    "Ecuador",
    "16 Dec 2019: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for generators installation at CBP CSI residences (PoP Ecuador); obligated USD 31614.33. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "31614.33", "2019-12-16", "2019", "", "",
    "GENERATORS INSTALLATION AT CBP CSI RESIDENCES, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_ecuador_cbp_generators_install_31k_2020",
    "GENERATORS INSTALLATION AT CBP CSI RESIDENCES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3020P0106_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1276",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3020P0106_1900_-NONE-_-NONE- (misc_ecuador_cbp_generators_install_31k_2020). Signed 2019-12-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3020P0106_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_cbp_generators_install_31k_2020 USD 0.032m. Supports misc_ecuador_cbp_generators_install_31k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 31614.33; date_signed 2019-12-16.",
    investment_type="equipment_supply",
)

# === Cycle 1277 ===
row_doc(
    "futron_jamaica_kingston_consular_reconfig_2676k_2023",
    "infrastructure", "building_materials", "us",
    "Futron — Kingston embassy consular affairs reconfiguration",
    "Jamaica",
    "29 Sep 2023: Department of State awards contract to FUTRON, INC. for consular affairs reconfiguration U.S. Embassy Kingston (PoP Jamaica); obligated USD 2676519.26. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2676519.26", "2023-09-29", "2023", "", "",
    "CONSULAR AFFAIRS RECONFIGURATION U.S. EMBASSY IN KINGSTON JAMAICA, Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_futron_jamaica_kingston_consular_reconfig_2676k_2023",
    "CONSULAR AFFAIRS RECONFIGURATION U.S. EMBASSY IN KINGSTON JAMAICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0773_1900_19AQMM22D0075_1900/",
    "Actor: FUTRON, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1277",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F0773_1900_19AQMM22D0075_1900 (futron_jamaica_kingston_consular_reconfig_2676k_2023). Signed 2023-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0773_1900_19AQMM22D0075_1900/.",
    "USASpending: futron_jamaica_kingston_consular_reconfig_2676k_2023 USD 2.677m. Supports futron_jamaica_kingston_consular_reconfig_2676k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2676519.26; date_signed 2023-09-29.",
    investment_type="epc",
)

# === Cycle 1277 ===
row_doc(
    "human_tech_colombia_hanger_tents_rigid_boxes_1692k_2022",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Colombia hanger tents and rigid boxes",
    "Colombia",
    "12 Sep 2022: Department of State awards contract to HUMAN TECHNOLOGIES CORP for purchase of hanger tents and rigid boxes (PoP Colombia); obligated USD 1692987.44. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1692987.44", "2022-09-12", "2022", "", "",
    "PURCHASE OF HANGER TENTS AND RIGID BOXES, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_colombia_hanger_tents_rigid_boxes_1692k_2022",
    "PURCHASE OF HANGER TENTS AND RIGID BOXES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22F0025_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1277",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE22F0025_1900_19AQMM21D0007_1900 (human_tech_colombia_hanger_tents_rigid_boxes_1692k_2022). Signed 2022-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22F0025_1900_19AQMM21D0007_1900/.",
    "USASpending: human_tech_colombia_hanger_tents_rigid_boxes_1692k_2022 USD 1.693m. Supports human_tech_colombia_hanger_tents_rigid_boxes_1692k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1692987.44; date_signed 2022-09-12.",
    investment_type="equipment_supply",
)

# === Cycle 1277 ===
row_doc(
    "misc_costarica_cmr_generator_install_29k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Costa Rica CMR generator installation",
    "Costa Rica",
    "19 Sep 2024: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for CMR generator installation (PoP Costa Rica); obligated USD 29914.83. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "29914.83", "2024-09-19", "2024", "", "",
    "PR12920502: FAC/OBO XJZMOPSP/ CMR GENERATOR INSTALLATION, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_costarica_cmr_generator_install_29k_2024",
    "PR12920502: FAC/OBO XJZMOPSP/ CMR GENERATOR INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8024P1376_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1277",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8024P1376_1900_-NONE-_-NONE- (misc_costarica_cmr_generator_install_29k_2024). Signed 2024-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8024P1376_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costarica_cmr_generator_install_29k_2024 USD 0.030m. Supports misc_costarica_cmr_generator_install_29k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 29914.83; date_signed 2024-09-19.",
    investment_type="equipment_supply",
)

# === Cycle 1277 ===
row_doc(
    "misc_barbados_generator_install_29k_2019",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Barbados generator installation",
    "Barbados",
    "25 Sep 2019: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for generator installation (PoP Barbados); obligated USD 29700.15. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "29700.15", "2019-09-25", "2019", "", "",
    "GENERATOR INSTALLATION, Barbados (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_barbados_generator_install_29k_2019",
    "GENERATOR INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2119C0005_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1277",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BB2119C0005_1900_-NONE-_-NONE- (misc_barbados_generator_install_29k_2019). Signed 2019-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2119C0005_1900_-NONE-_-NONE-/.",
    "USASpending: misc_barbados_generator_install_29k_2019 USD 0.030m. Supports misc_barbados_generator_install_29k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 29700.15; date_signed 2019-09-25.",
    investment_type="equipment_supply",
)

# === Cycle 1277 ===
row_doc(
    "misc_honduras_solar_water_heaters_27k_2012",
    "energy", "solar", "other",
    "Miscellaneous foreign awardees — Honduras solar panels for water heaters",
    "Honduras",
    "24 Sep 2012: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for procure 20 solar panels for water heaters (PoP Honduras); obligated USD 27500. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "27500", "2012-09-24", "2012", "", "",
    "PROCURE 20 SOLAR PANELS FOR WATER HEATERS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_honduras_solar_water_heaters_27k_2012",
    "PROCURE 20 SOLAR PANELS FOR WATER HEATERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80012M0779_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle solar.",
    "hunt_cycle1277",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80012M0779_1900_-NONE-_-NONE- (misc_honduras_solar_water_heaters_27k_2012). Signed 2012-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80012M0779_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_solar_water_heaters_27k_2012 USD 0.028m. Supports misc_honduras_solar_water_heaters_27k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 27500.0; date_signed 2012-09-24.",
    investment_type="equipment_supply",
)

# === Cycle 1278 ===
row_doc(
    "emr_guatemala_ahu_replacement_1414k_2014",
    "energy", "power_plants_grid", "us",
    "Enviro-Management & Research — Guatemala air handling unit replacement",
    "Guatemala",
    "29 Sep 2014: Department of State awards contract to ENVIRO-MANAGEMENT & RESEARCH, INC. for air handling unit replacement (PoP Guatemala); obligated USD 1414666. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1414666", "2014-09-29", "2014", "", "",
    "AIR HANDLING UNIT REPLACEMENT.  IGF::OT::IGF, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_emr_guatemala_ahu_replacement_1414k_2014",
    "AIR HANDLING UNIT REPLACEMENT.  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F4608_1900_SAQMMA14D0061_1900/",
    "Actor: ENVIRO-MANAGEMENT & RESEARCH, INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1278",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14F4608_1900_SAQMMA14D0061_1900 (emr_guatemala_ahu_replacement_1414k_2014). Signed 2014-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F4608_1900_SAQMMA14D0061_1900/.",
    "USASpending: emr_guatemala_ahu_replacement_1414k_2014 USD 1.415m. Supports emr_guatemala_ahu_replacement_1414k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1414666.0; date_signed 2014-09-29.",
    investment_type="equipment_supply",
)

# === Cycle 1278 ===
row_doc(
    "kva_honduras_electrical_work_1367k_2015",
    "energy", "power_plants_grid", "us",
    "KVA Electric — Honduras electrical work",
    "Honduras",
    "7 Aug 2015: Department of State awards contract to KVA ELECTRIC INC for electrical work (PoP Honduras); obligated USD 1367394.42. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1367394.42", "2015-08-07", "2015", "", "",
    "ELECTRICAL WORK IGF::CT::IGF, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_kva_honduras_electrical_work_1367k_2015",
    "ELECTRICAL WORK IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F2280_1900_SAQMMA13D0022_1900/",
    "Actor: KVA ELECTRIC INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1278",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15F2280_1900_SAQMMA13D0022_1900 (kva_honduras_electrical_work_1367k_2015). Signed 2015-08-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F2280_1900_SAQMMA13D0022_1900/.",
    "USASpending: kva_honduras_electrical_work_1367k_2015 USD 1.367m. Supports kva_honduras_electrical_work_1367k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1367394.42; date_signed 2015-08-07.",
    investment_type="epc",
)

# === Cycle 1278 ===
row_doc(
    "misc_mexico_campeche_solar_panels_26k_2014",
    "energy", "solar", "other",
    "Miscellaneous foreign awardees — Mexico Campeche solar panels for highway LPR",
    "Mexico",
    "17 Oct 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for Campeche solar panels for highway LPR (PoP Mexico); obligated USD 26328.05. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "26328.05", "2014-10-17", "2014", "", "",
    "INL-MI-IN23MX88 CAMPECHE SOLAR PANELS FOR HIGHWAY LPR, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_campeche_solar_panels_26k_2014",
    "INL-MI-IN23MX88 CAMPECHE SOLAR PANELS FOR HIGHWAY LPR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX90015M0001_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle solar.",
    "hunt_cycle1278",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX90015M0001_1900_-NONE-_-NONE- (misc_mexico_campeche_solar_panels_26k_2014). Signed 2014-10-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX90015M0001_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_campeche_solar_panels_26k_2014 USD 0.026m. Supports misc_mexico_campeche_solar_panels_26k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 26328.05; date_signed 2014-10-17.",
    investment_type="equipment_supply",
)

# === Cycle 1278 ===
row_doc(
    "misc_brazil_msgr_fire_alarm_26k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil MSGR fire alarm solicitation",
    "Brazil",
    "31 Jul 2019: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for MSGR fire alarm solicitation (PoP Brazil); obligated USD 26280.12. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "26280.12", "2019-07-31", "2019", "", "",
    "BSB-FAC: MSGR FIRE ALARM SOLICITATION, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_msgr_fire_alarm_26k_2019",
    "BSB-FAC: MSGR FIRE ALARM SOLICITATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0985_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1278",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2519P0985_1900_-NONE-_-NONE- (misc_brazil_msgr_fire_alarm_26k_2019). Signed 2019-07-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0985_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_msgr_fire_alarm_26k_2019 USD 0.026m. Supports misc_brazil_msgr_fire_alarm_26k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 26280.12; date_signed 2019-07-31.",
    investment_type="equipment_supply",
)

# === Cycle 1278 ===
row_doc(
    "misc_colombia_fire_alarm_install_24k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia fire alarm system supply and installation",
    "Colombia",
    "1 Feb 2019: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for supply and installation fire alarm system (PoP Colombia); obligated USD 24682.70. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "24682.70", "2019-02-01", "2019", "", "",
    "PR7888123 SUPPLY&INSTALLATION FIRE ALARM SYSTEM ICASS OFFSITE WAREHOUS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_fire_alarm_install_24k_2019",
    "PR7888123 SUPPLY&INSTALLATION FIRE ALARM SYSTEM ICASS OFFSITE WAREHOUS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02019P0189_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1278",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02019P0189_1900_-NONE-_-NONE- (misc_colombia_fire_alarm_install_24k_2019). Signed 2019-02-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02019P0189_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_fire_alarm_install_24k_2019 USD 0.025m. Supports misc_colombia_fire_alarm_install_24k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 24682.7; date_signed 2019-02-01.",
    investment_type="equipment_supply",
)

# === Cycle 1279 ===
row_doc(
    "human_tech_colombia_quick_deploy_tents_985k_2020",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Colombia quick deploy tents, beds, and flooring",
    "Colombia",
    "28 May 2020: Department of State awards contract to HUMAN TECHNOLOGIES CORP for quick deploy tents, beds, and flooring (PoP Colombia); obligated USD 985837.30. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "985837.30", "2020-05-28", "2020", "", "",
    "QUICK DEPLOY TENTS, BEDS, AND FLOORING, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_colombia_quick_deploy_tents_985k_2020",
    "QUICK DEPLOY TENTS, BEDS, AND FLOORING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1039_1900_19AQMM18D0100_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1279",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F1039_1900_19AQMM18D0100_1900 (human_tech_colombia_quick_deploy_tents_985k_2020). Signed 2020-05-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1039_1900_19AQMM18D0100_1900/.",
    "USASpending: human_tech_colombia_quick_deploy_tents_985k_2020 USD 0.986m. Supports human_tech_colombia_quick_deploy_tents_985k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 985837.3; date_signed 2020-05-28.",
    investment_type="equipment_supply",
)

# === Cycle 1279 ===
row_doc(
    "ics_trinidad_hurricane_doors_windows_838k_2010",
    "infrastructure", "building_materials", "us",
    "International Construction Services — Trinidad hurricane-rated door and window replacement",
    "Trinidad and Tobago",
    "23 Sep 2010: Department of State awards contract to INTERNATIONAL CONSTRUCTION SERVICES, LLC for hurricane rated door and window replacement (PoP Trinidad and Tobago); obligated USD 838838.12. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "838838.12", "2010-09-23", "2010", "", "",
    "TAS::19 0535 000::TAS HURRICANE RATED DOOR & WINDOW REPLACEMENT FOR CMR/DMR, Trinidad and Tobago (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_ics_trinidad_hurricane_doors_windows_838k_2010",
    "TAS::19 0535 000::TAS HURRICANE RATED DOOR & WINDOW REPLACEMENT FOR CMR/DMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F4413_1900_SAQMMA08D0005_1900/",
    "Actor: INTERNATIONAL CONSTRUCTION SERVICES, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1279",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F4413_1900_SAQMMA08D0005_1900 (ics_trinidad_hurricane_doors_windows_838k_2010). Signed 2010-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F4413_1900_SAQMMA08D0005_1900/.",
    "USASpending: ics_trinidad_hurricane_doors_windows_838k_2010 USD 0.839m. Supports ics_trinidad_hurricane_doors_windows_838k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 838838.12; date_signed 2010-09-23.",
    investment_type="epc",
)

# === Cycle 1279 ===
row_doc(
    "misc_mexico_nogales_fire_alarm_install_22k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Nogales fire alarm system installation",
    "Mexico",
    "12 Sep 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for OBO fire alarm system installation Nogales (PoP Mexico); obligated USD 22356.36. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "22356.36", "2014-09-12", "2014", "", "",
    "OBO - FIRE ALARM SYSTEM INSTALLATION - NOGALES, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_nogales_fire_alarm_install_22k_2014",
    "OBO - FIRE ALARM SYSTEM INSTALLATION - NOGALES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX60014M0172_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1279",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX60014M0172_1900_-NONE-_-NONE- (misc_mexico_nogales_fire_alarm_install_22k_2014). Signed 2014-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX60014M0172_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_nogales_fire_alarm_install_22k_2014 USD 0.022m. Supports misc_mexico_nogales_fire_alarm_install_22k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 22356.36; date_signed 2014-09-12.",
    investment_type="equipment_supply",
)

# === Cycle 1279 ===
row_doc(
    "misc_mexico_emr_cctv_install_21k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico EMR CCTV installation",
    "Mexico",
    "25 May 2010: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for RSO CCTV installation in the EMR (PoP Mexico); obligated USD 21170.83. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "21170.83", "2010-05-25", "2010", "", "",
    "RSO- CCTV INSTALLATION IN THE EMR, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_emr_cctv_install_21k_2010",
    "RSO- CCTV INSTALLATION IN THE EMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0438_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1279",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53010M0438_1900_-NONE-_-NONE- (misc_mexico_emr_cctv_install_21k_2010). Signed 2010-05-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0438_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_emr_cctv_install_21k_2010 USD 0.021m. Supports misc_mexico_emr_cctv_install_21k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 21170.83; date_signed 2010-05-25.",
    investment_type="equipment_supply",
)

# === Cycle 1279 ===
row_doc(
    "misc_costarica_obc_elevator_upgrade_32k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Costa Rica OBC elevators replacement upgrade",
    "Costa Rica",
    "27 Aug 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for upgrade OBC elevators replacement (PoP Costa Rica); obligated USD 32986.16. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "32986.16", "2014-08-27", "2014", "", "",
    "FAC/OBO/ICASS 1901.0 UPGRADE OBC ELEVATORS REPLACEMENT PARTS, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_costarica_obc_elevator_upgrade_32k_2014",
    "FAC/OBO/ICASS 1901.0 UPGRADE OBC ELEVATORS REPLACEMENT PARTS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80014M0505_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1279",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80014M0505_1900_-NONE-_-NONE- (misc_costarica_obc_elevator_upgrade_32k_2014). Signed 2014-08-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80014M0505_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costarica_obc_elevator_upgrade_32k_2014 USD 0.033m. Supports misc_costarica_obc_elevator_upgrade_32k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 32986.16; date_signed 2014-08-27.",
    investment_type="equipment_supply",
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
