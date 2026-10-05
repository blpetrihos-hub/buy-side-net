#!/usr/bin/env python3
"""Cycles 1110–1112: USASpending LatAm CapEx residual (~USD0.027–0.048m).

Seeds: 20262110–20262112. Thin top-up dry. Holdovers Gateway/Venesco/Tandus/AGI closed.
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


# === Cycle 1110 (seed 20262110) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "tidewater_nicaragua_underground_tank_replacement_30k_2015",
    "resources", "water", "us",
    "Tidewater — Nicaragua underground tank replacement",
    "Nicaragua",
    "26 Jun 2015: Department of State awards contract SAQMMA15F1813 to Tidewater, Inc. for underground tank replacement (PoP Nicaragua); obligated USD 29,989.25. CapEx face = award obligation. Exact tank site unnamed — lat/lon blank.",
    "29989.25", "2015-06-26", "2015", "", "",
    "Underground tank replacement, Nicaragua (USASpending description; site not named — lat/lon blank).",
    "usaspending_tidewater_nicaragua_underground_tank_replacement_30k_2015",
    "UNDERGROUND TANK REPLACEMENT IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1813_1900_SAQMMA12D0197_1900/",
    "Actor: Tidewater, Inc. (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1110",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15F1813_1900_SAQMMA12D0197_1900 (tidewater_nicaragua_underground_tank_replacement_30k_2015). Signed 2015-06-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1813_1900_SAQMMA12D0197_1900/.",
    "USASpending: tidewater_nicaragua_underground_tank_replacement_30k_2015 USD 0.030m. Supports tidewater_nicaragua_underground_tank_replacement_30k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 29989.25; date_signed 2015-06-26.",
)
row_doc(
    "cummins_guyana_dcmr_generator_30k_2013",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Guyana DCMR generator 35-37 UG",
    "Guyana",
    "10 Dec 2013: Department of State awards contract SGY20014M0054 to Cummins Power Generation Inc. for generator for DCMR 35-37 UG (PoP Guyana); obligated USD 29,679.85. CapEx face = award obligation. Exact DCMR unnamed — lat/lon blank.",
    "29679.85", "2013-12-10", "2013", "", "",
    "Generator for DCMR 35-37 UG, Guyana (USASpending description; DCMR named, site coords not stated — lat/lon blank).",
    "usaspending_cummins_guyana_dcmr_generator_30k_2013",
    "GENERATOR FOR DCMR 35-37 UG",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20014M0054_1900_-NONE-_-NONE-/",
    "Actor: Cummins Power Generation Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1110",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGY20014M0054_1900_-NONE-_-NONE- (cummins_guyana_dcmr_generator_30k_2013). Signed 2013-12-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20014M0054_1900_-NONE-_-NONE-/.",
    "USASpending: cummins_guyana_dcmr_generator_30k_2013 USD 0.030m. Supports cummins_guyana_dcmr_generator_30k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 29679.85; date_signed 2013-12-10.",
)
row_doc(
    "misc_guatemala_kaibil_barracks_2_renovation_47k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guatemala Kaibil barracks #2 renovation",
    "Guatemala",
    "18 Feb 2010: Department of Defense awards contract W912CL10C0008 for renovation of Kaibil barracks #2 (PoP Guatemala); obligated USD 46,908.81. CapEx face = award obligation. Exact barracks coords unnamed — lat/lon blank.",
    "46908.81", "2010-02-18", "2010", "", "",
    "Renovation of Kaibil barracks #2, Guatemala (USASpending description; Kaibil named, site coords not stated — lat/lon blank).",
    "usaspending_misc_guatemala_kaibil_barracks_2_renovation_47k_2010",
    "RENOVATION OF  KAIBIL BARRACKS #2",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0008_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1110",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0008_9700_-NONE-_-NONE- (misc_guatemala_kaibil_barracks_2_renovation_47k_2010). Signed 2010-02-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0008_9700_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_kaibil_barracks_2_renovation_47k_2010 USD 0.047m. Supports misc_guatemala_kaibil_barracks_2_renovation_47k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 46908.81; date_signed 2010-02-18.",
)
row_doc(
    "misc_brazil_substation_capacitor_bank_renovation_48k_2014",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil substation capacitor bank renovation",
    "Brazil",
    "14 Jul 2014: Department of State awards contract SBR25014M1195 for substation capacitor bank renovation (PoP Brazil); obligated USD 47,617.96. CapEx face = award obligation. Exact substation unnamed — lat/lon blank.",
    "47617.96", "2014-07-14", "2014", "", "",
    "Substation capacitor bank renovation, Brazil (USASpending description; substation not named — lat/lon blank).",
    "usaspending_misc_brazil_substation_capacitor_bank_renovation_48k_2014",
    "7901.C FUNDING - SUBSTATION CAPACITOR BANK RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25014M1195_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1110",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25014M1195_1900_-NONE-_-NONE- (misc_brazil_substation_capacitor_bank_renovation_48k_2014). Signed 2014-07-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25014M1195_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_substation_capacitor_bank_renovation_48k_2014 USD 0.048m. Supports misc_brazil_substation_capacitor_bank_renovation_48k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 47617.96; date_signed 2014-07-14.",
)
row_doc(
    "misc_peru_lima_annex_restrooms_renovation_44k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru Lima FAC annex restrooms renovation",
    "Peru",
    "28 Aug 2016: Department of State awards contract SPE50016C0035 for Lima FY2016 FAC annex restrooms renovation project (PoP Peru); obligated USD 44,451.13. CapEx face = award obligation. Exact annex unnamed — lat/lon blank.",
    "44451.13", "2016-08-28", "2016", "", "",
    "Lima FY2016 FAC annex restrooms renovation project, Peru (USASpending description; annex named, site coords not stated — lat/lon blank).",
    "usaspending_misc_peru_lima_annex_restrooms_renovation_44k_2016",
    "LIMA FY2016 FAC ANNEX RESTROOMS RENOVATION PROJECT IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0035_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1110",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50016C0035_1900_-NONE-_-NONE- (misc_peru_lima_annex_restrooms_renovation_44k_2016). Signed 2016-08-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0035_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_lima_annex_restrooms_renovation_44k_2016 USD 0.044m. Supports misc_peru_lima_annex_restrooms_renovation_44k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 44451.13; date_signed 2016-08-28.",
)

# === Cycle 1111 (seed 20262111) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "gateway_el_salvador_embassy_carpets_28k_2025",
    "infrastructure", "building_materials", "us",
    "Gateway International — El Salvador carpets",
    "El Salvador",
    "16 Jul 2025: Department of State awards contract 19ES6025P0613 to Gateway International Inc for carpets (PoP El Salvador); obligated USD 28,038. CapEx face = award obligation. Exact building unnamed — lat/lon blank.",
    "28038", "2025-07-16", "2025", "", "",
    "Carpets, El Salvador (USASpending description; building not named — lat/lon blank).",
    "usaspending_gateway_el_salvador_embassy_carpets_28k_2025",
    "CARPETS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6025P0613_1900_-NONE-_-NONE-/",
    "Actor: Gateway International Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1111",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6025P0613_1900_-NONE-_-NONE- (gateway_el_salvador_embassy_carpets_28k_2025). Signed 2025-07-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6025P0613_1900_-NONE-_-NONE-/.",
    "USASpending: gateway_el_salvador_embassy_carpets_28k_2025 USD 0.028m. Supports gateway_el_salvador_embassy_carpets_28k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 28038; date_signed 2025-07-16.",
)
row_doc(
    "venesco_panama_pol_econ_rso_carpet_28k_2022",
    "infrastructure", "building_materials", "us",
    "Venesco Construction Management — Panama POL/ECON and RSO carpet replacement",
    "Panama",
    "8 Jun 2022: Department of State awards contract 19PM0722P0615 to Venesco Construction Management LLC for POL/ECON and RSO carpet replacement (PoP Panama); obligated USD 27,584. CapEx face = award obligation. Exact offices unnamed — lat/lon blank.",
    "27584", "2022-06-08", "2022", "", "",
    "POL/ECON and RSO carpet replacement, Panama (USASpending description; offices named, site coords not stated — lat/lon blank).",
    "usaspending_venesco_panama_pol_econ_rso_carpet_28k_2022",
    "POL/ECON AND RSO CARPET REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0722P0615_1900_-NONE-_-NONE-/",
    "Actor: Venesco Construction Management LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1111",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0722P0615_1900_-NONE-_-NONE- (venesco_panama_pol_econ_rso_carpet_28k_2022). Signed 2022-06-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0722P0615_1900_-NONE-_-NONE-/.",
    "USASpending: venesco_panama_pol_econ_rso_carpet_28k_2022 USD 0.028m. Supports venesco_panama_pol_econ_rso_carpet_28k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 27584; date_signed 2022-06-08.",
)
row_doc(
    "misc_argentina_cervino_4616_3a_renovation_44k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina Cervino 4616 3A government-owned renovation",
    "Argentina",
    "28 Jun 2018: Department of State awards contract 19AR2018P0508 for renovation of government-owned Cervino 4616 3A CABA (PoP Argentina); obligated USD 43,929.05. CapEx face = award obligation. Street named; coords not stated — lat/lon blank.",
    "43929.05", "2018-06-28", "2018", "", "",
    "Renovation government-owned Cervino 4616 3A CABA, Argentina (USASpending description; street address named, site coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_cervino_4616_3a_renovation_44k_2018",
    "FM - RENOVATION GOVERMENT OWN - CERVINO 4616 3 A - CABA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P0508_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1111",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2018P0508_1900_-NONE-_-NONE- (misc_argentina_cervino_4616_3a_renovation_44k_2018). Signed 2018-06-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P0508_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_cervino_4616_3a_renovation_44k_2018 USD 0.044m. Supports misc_argentina_cervino_4616_3a_renovation_44k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 43929.05; date_signed 2018-06-28.",
)
row_doc(
    "misc_el_salvador_dcm_pool_renovation_43k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador DCM residence swimming pool renovation",
    "El Salvador",
    "9 Jun 2010: Department of State awards contract SES60010M0559 for DCM residence swimming pool renovation (PoP El Salvador); obligated USD 42,556.14. CapEx face = award obligation. Exact DCM residence unnamed — lat/lon blank.",
    "42556.14", "2010-06-09", "2010", "", "",
    "DCM residence swimming pool renovation, El Salvador (USASpending description; DCM residence named, site coords not stated — lat/lon blank).",
    "usaspending_misc_el_salvador_dcm_pool_renovation_43k_2010",
    "7901 DCM'S RES -SWIMMING POOL RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60010M0559_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1111",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60010M0559_1900_-NONE-_-NONE- (misc_el_salvador_dcm_pool_renovation_43k_2010). Signed 2010-06-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60010M0559_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_dcm_pool_renovation_43k_2010 USD 0.043m. Supports misc_el_salvador_dcm_pool_renovation_43k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 42556.14; date_signed 2010-06-09.",
)
row_doc(
    "misc_bahamas_cmr_landscape_renovation_42k_2017",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Bahamas CMR landscape renovation 2017",
    "Bahamas",
    "29 Sep 2017: Department of State awards contract SBF50017M1195 for CMR landscape renovation 2017 (PoP Bahamas); obligated USD 42,000. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.",
    "42000", "2017-09-29", "2017", "", "",
    "CMR landscape renovation 2017, Bahamas (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_bahamas_cmr_landscape_renovation_42k_2017",
    "IGF::OT::IGF CMR - LANDSCAPE RENOVATION 2017",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017M1195_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1111",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50017M1195_1900_-NONE-_-NONE- (misc_bahamas_cmr_landscape_renovation_42k_2017). Signed 2017-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017M1195_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_cmr_landscape_renovation_42k_2017 USD 0.042m. Supports misc_bahamas_cmr_landscape_renovation_42k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 42000; date_signed 2017-09-29.",
)

# === Cycle 1112 (seed 20262112) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "agi_panama_naos_seawater_pumps_29k_2023",
    "resources", "water", "us",
    "AGI Industries — Panama Naos seawater system pumps",
    "Panama",
    "26 Apr 2023: Smithsonian awards contract 33330523P00490692 to AGI Industries Inc for pumps for the sea water system at Naos (PoP Panama); obligated USD 28,554.8. CapEx face = award obligation. Naos named; site coords not stated — lat/lon blank.",
    "28554.8", "2023-04-26", "2023", "", "",
    "Pumps for the sea water system at Naos, Panama (USASpending description; Naos named, site coords not stated — lat/lon blank).",
    "usaspending_agi_panama_naos_seawater_pumps_29k_2023",
    "PUMPS FOR THE SEA WATER SYSTEM AT NAOS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330523P00490692_3300_-NONE-_-NONE-/",
    "Actor: AGI Industries Inc (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1112",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330523P00490692_3300_-NONE-_-NONE- (agi_panama_naos_seawater_pumps_29k_2023). Signed 2023-04-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330523P00490692_3300_-NONE-_-NONE-/.",
    "USASpending: agi_panama_naos_seawater_pumps_29k_2023 USD 0.029m. Supports agi_panama_naos_seawater_pumps_29k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 28554.8; date_signed 2023-04-26.",
)
row_doc(
    "tandus_guyana_floor_covering_28k_2012",
    "infrastructure", "building_materials", "us",
    "Tandus Centiva US — Guyana floor covering",
    "Guyana",
    "23 Aug 2012: Department of State awards contract SAQMMA12F3002 to Tandus Centiva US LLC for floor covering (PoP Guyana); obligated USD 27,732.05. CapEx face = award obligation. Exact building unnamed — lat/lon blank.",
    "27732.05", "2012-08-23", "2012", "", "",
    "Floor covering, Guyana (USASpending description; building not named — lat/lon blank).",
    "usaspending_tandus_guyana_floor_covering_28k_2012",
    "FLOOR COVERING.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F3002_1900_GS27F0032P_4730/",
    "Actor: Tandus Centiva US LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1112",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F3002_1900_GS27F0032P_4730 (tandus_guyana_floor_covering_28k_2012). Signed 2012-08-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F3002_1900_GS27F0032P_4730/.",
    "USASpending: tandus_guyana_floor_covering_28k_2012 USD 0.028m. Supports tandus_guyana_floor_covering_28k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 27732.05; date_signed 2012-08-23.",
)
row_doc(
    "misc_mexico_emr_reforma_2414_bathrooms_renovation_41k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico EMR Reforma #2414 bathrooms renovation",
    "Mexico",
    "29 Jul 2010: Department of State awards contract SMX53010M0618 for bathrooms renovation EMR Reforma #2414 Mexico (PoP Mexico); obligated USD 41,458.98. CapEx face = award obligation. Street address named; coords not stated — lat/lon blank.",
    "41458.98", "2010-07-29", "2010", "", "",
    "Bathrooms renovation EMR Reforma #2414, Mexico (USASpending description; street address named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_emr_reforma_2414_bathrooms_renovation_41k_2010",
    "BATHROOMS RENOVATION EMR REFORMA #2414 MEX",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0618_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1112",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53010M0618_1900_-NONE-_-NONE- (misc_mexico_emr_reforma_2414_bathrooms_renovation_41k_2010). Signed 2010-07-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0618_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_emr_reforma_2414_bathrooms_renovation_41k_2010 USD 0.041m. Supports misc_mexico_emr_reforma_2414_bathrooms_renovation_41k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 41458.98; date_signed 2010-07-29.",
)
row_doc(
    "misc_costa_rica_rso_office_renovation_39k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Costa Rica RSO renovation office project",
    "Costa Rica",
    "29 Aug 2011: Department of State awards contract SCS80011C0007 for RSO renovation office project (PoP Costa Rica); obligated USD 39,224. CapEx face = award obligation. Exact RSO office unnamed — lat/lon blank.",
    "39224", "2011-08-29", "2011", "", "",
    "RSO renovation office project, Costa Rica (USASpending description; RSO named, site coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_rso_office_renovation_39k_2011",
    "CONTRACT FOR RSO RENOVATION OFFICE PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80011C0007_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1112",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80011C0007_1900_-NONE-_-NONE- (misc_costa_rica_rso_office_renovation_39k_2011). Signed 2011-08-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80011C0007_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_rso_office_renovation_39k_2011 USD 0.039m. Supports misc_costa_rica_rso_office_renovation_39k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 39224; date_signed 2011-08-29.",
)
row_doc(
    "misc_panama_meteti_barracks_renovation_38k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Panama Meteti barracks renovation",
    "Panama",
    "25 Feb 2010: Department of Defense awards contract W912CL10C0005 for Meteti barracks renovation (PoP Panama); obligated USD 38,452.37. CapEx face = award obligation. Meteti named; site coords not stated — lat/lon blank.",
    "38452.37", "2010-02-25", "2010", "", "",
    "Meteti barracks renovation, Panama (USASpending description; Meteti named, site coords not stated — lat/lon blank).",
    "usaspending_misc_panama_meteti_barracks_renovation_38k_2010",
    "METETI BARRACKS RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0005_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1112",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0005_9700_-NONE-_-NONE- (misc_panama_meteti_barracks_renovation_38k_2010). Signed 2010-02-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0005_9700_-NONE-_-NONE-/.",
    "USASpending: misc_panama_meteti_barracks_renovation_38k_2010 USD 0.038m. Supports misc_panama_meteti_barracks_renovation_38k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 38452.37; date_signed 2010-02-25.",
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
