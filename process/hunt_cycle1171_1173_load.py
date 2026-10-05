#!/usr/bin/env python3
"""Cycles 1171–1173: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262171–20262173. Thin top-up dry.
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


# === Cycle 1171 (seed 20262171) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "ross_technology_dominican_republic_parking_lot_gate_motor_drive_31k_2017",
    "infrastructure", "building_materials", "us",
    "Ross Technology — Dominican Republic motor drive for parking lot gates",
    "Dominican Republic",
    "19 May 2017: Department of State awards contract SDR86017M0521 to Ross Technology Company for motor drive for parking lot gates (PoP Dominican Republic); obligated USD 31,076.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "31076", "2017-05-19", "2017", "", "",
    "Motor drive for parking lot gates, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_ross_technology_dominican_republic_parking_lot_gate_motor_drive_31k_2017",
    "IGF::CL::IGF MOTOR DRIVE FOR PARKING LOT GATES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86017M0521_1900_-NONE-_-NONE-/",
    "Actor: ROSS TECHNOLOGY COMPANY (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1171",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86017M0521_1900_-NONE-_-NONE- (ross_technology_dominican_republic_parking_lot_gate_motor_drive_31k_2017). Signed 2017-05-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86017M0521_1900_-NONE-_-NONE-/.",
    "USASpending: ross_technology_dominican_republic_parking_lot_gate_motor_drive_31k_2017 USD 0.031m. Supports ross_technology_dominican_republic_parking_lot_gate_motor_drive_31k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 31076.0; date_signed 2017-05-19.",
)
row_doc(
    "fabrication_designs_chile_santiago_embassy_doors_27k_2024",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Chile Santiago procure and air ship doors to embassy",
    "Chile",
    "6 Jun 2024: Department of State awards contract 19AQMM24P0508 to Fabrication Designs, Inc. for procure and air ship doors to Santiago embassy (PoP Chile); obligated USD 27,161.56. CapEx face = award obligation. Santiago named; site coords not stated — lat/lon blank.",
    "27161.56", "2024-06-06", "2024", "", "",
    "Procure and air ship doors to Santiago embassy, Chile (USASpending description; Santiago named, site coords not stated — lat/lon blank).",
    "usaspending_fabrication_designs_chile_santiago_embassy_doors_27k_2024",
    "---------- COMMENTS: SANTIAGO_FDI Q:4133_GPR'S_02EA.  PROCURE   AIR SHIP WITH DOOR TO DOOR SERVICE BASED ON THE ATTACHED FDI Q:4133.  ADDRESS:  2800 AV. ANDR S BELLO  (POC) (FM) CHRIS WILGANOWSKI WILGANOWSKICA@STATE.GOV O: 56 2 2330 3360 C: 56 9 8805",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0508_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1171",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0508_1900_-NONE-_-NONE- (fabrication_designs_chile_santiago_embassy_doors_27k_2024). Signed 2024-06-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0508_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_chile_santiago_embassy_doors_27k_2024 USD 0.027m. Supports fabrication_designs_chile_santiago_embassy_doors_27k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 27161.56; date_signed 2024-06-06.",
)
row_doc(
    "misc_honduras_nine_ac_units_non_vrf_building_install_14k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras supply and installation of nine AC units for building non-VRF areas",
    "Honduras",
    "7 Apr 2016: USAID awards contract AID522O1600041 for supply and installation of nine AC units for building for non-VRF areas (PoP Honduras); obligated USD 14,488.89. CapEx face = award obligation. Exact building unnamed — lat/lon blank.",
    "14488.89", "2016-04-07", "2016", "", "",
    "Supply and installation of nine AC units for building non-VRF areas, Honduras (USASpending description; building unnamed — lat/lon blank).",
    "usaspending_misc_honduras_nine_ac_units_non_vrf_building_install_14k_2016",
    "SUPPLY AND INSTALLATION OF NINE AC UNITS FOR BUILDING FOR NON VRF AREAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1600041_7200_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1171",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID522O1600041_7200_-NONE-_-NONE- (misc_honduras_nine_ac_units_non_vrf_building_install_14k_2016). Signed 2016-04-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1600041_7200_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_nine_ac_units_non_vrf_building_install_14k_2016 USD 0.014m. Supports misc_honduras_nine_ac_units_non_vrf_building_install_14k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14488.89; date_signed 2016-04-07.",
)
row_doc(
    "misc_brazil_security_upgrades_14k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil security upgrades",
    "Brazil",
    "14 Jun 2022: Department of State awards contract 19BR2522P1071 for security upgrades (PoP Brazil); obligated USD 14,486.84. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14486.84", "2022-06-14", "2022", "", "",
    "Security upgrades, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_security_upgrades_14k_2022",
    "SECURITY UPGRADES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2522P1071_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1171",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2522P1071_1900_-NONE-_-NONE- (misc_brazil_security_upgrades_14k_2022). Signed 2022-06-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2522P1071_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_security_upgrades_14k_2022 USD 0.014m. Supports misc_brazil_security_upgrades_14k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14486.84; date_signed 2022-06-14.",
)
row_doc(
    "misc_brazil_new_cmr_shatter_resistant_window_film_14k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil shatter-resistant window film installation at new CMR",
    "Brazil",
    "26 Jun 2015: Department of State awards contract SBR25015M1019 for shatter-resistant window film installation at new CMR (PoP Brazil); obligated USD 14,484.89. CapEx face = award obligation. New CMR named; site coords not stated — lat/lon blank.",
    "14484.89", "2015-06-26", "2015", "", "",
    "Shatter-resistant window film installation at new CMR, Brazil (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_new_cmr_shatter_resistant_window_film_14k_2015",
    "SHATTER-RESISTANT WINDOW FILM INSTALLATION AT NEW CMR ''IGF::OT::IGF''",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25015M1019_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1171",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25015M1019_1900_-NONE-_-NONE- (misc_brazil_new_cmr_shatter_resistant_window_film_14k_2015). Signed 2015-06-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25015M1019_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_new_cmr_shatter_resistant_window_film_14k_2015 USD 0.014m. Supports misc_brazil_new_cmr_shatter_resistant_window_film_14k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14484.89; date_signed 2015-06-26.",
)

# === Cycle 1172 (seed 20262172) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_costa_rica_metal_door_screen_24k_2022",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Costa Rica metal door screen for international embassies",
    "Costa Rica",
    "25 Jul 2022: Department of State awards contract 19AQMM22P0872 to Norshield Security Products, LLC for metal door screen etc. for international embassies (PoP Costa Rica); obligated USD 24,395.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "24395", "2022-07-25", "2022", "", "",
    "Metal door screen etc. for international embassies, Costa Rica (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_costa_rica_metal_door_screen_24k_2022",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0872_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1172",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22P0872_1900_-NONE-_-NONE- (norshield_costa_rica_metal_door_screen_24k_2022). Signed 2022-07-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0872_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_costa_rica_metal_door_screen_24k_2022 USD 0.024m. Supports norshield_costa_rica_metal_door_screen_24k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 24395.0; date_signed 2022-07-25.",
)
row_doc(
    "fabrication_designs_el_salvador_metal_door_screen_24k_2020",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — El Salvador metal door screen",
    "El Salvador",
    "8 Jun 2020: Department of State awards contract 19AQMM20P0975 to Fabrication Designs, Inc. for metal door screen etc. (PoP El Salvador); obligated USD 24,182.1. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "24182.10", "2020-06-08", "2020", "", "",
    "Metal door screen etc., El Salvador (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_fabrication_designs_el_salvador_metal_door_screen_24k_2020",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0975_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1172",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20P0975_1900_-NONE-_-NONE- (fabrication_designs_el_salvador_metal_door_screen_24k_2020). Signed 2020-06-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0975_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_el_salvador_metal_door_screen_24k_2020 USD 0.024m. Supports fabrication_designs_el_salvador_metal_door_screen_24k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 24182.1; date_signed 2020-06-08.",
)
row_doc(
    "misc_mexico_hermosillo_street_hydrant_feeding_pipe_replace_14k_2013",
    "infrastructure", "water", "other",
    "Miscellaneous foreign awardees — Mexico Hermosillo COB street hydrant feeding pipe replacement",
    "Mexico",
    "26 Sep 2013: Department of State awards contract SMX57013M0159 for OBO/HMO COB street hydrant feeding pipe replacement (PoP Mexico); obligated USD 14,494.61. CapEx face = award obligation. Hermosillo COB named; site coords not stated — lat/lon blank.",
    "14494.61", "2013-09-26", "2013", "", "",
    "Street hydrant feeding pipe replacement, Hermosillo COB, Mexico (USASpending description; Hermosillo named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_hermosillo_street_hydrant_feeding_pipe_replace_14k_2013",
    "IGF::CL::IGF OBO/HMO 7901 COB STREET HYDRANT FEEDING PIPE REPLACEMENT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX57013M0159_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1172",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX57013M0159_1900_-NONE-_-NONE- (misc_mexico_hermosillo_street_hydrant_feeding_pipe_replace_14k_2013). Signed 2013-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX57013M0159_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_hermosillo_street_hydrant_feeding_pipe_replace_14k_2013 USD 0.014m. Supports misc_mexico_hermosillo_street_hydrant_feeding_pipe_replace_14k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14494.61; date_signed 2013-09-26.",
)
row_doc(
    "misc_mexico_ccs_frequency_driver_replace_14k_2023",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico CCS replace of frequency driver",
    "Mexico",
    "8 Aug 2023: Department of State awards contract 19MX1123P0177 for FAC CCS replace of frequency driver (PoP Mexico); obligated USD 14,476.99. CapEx face = award obligation. CCS named; site coords not stated — lat/lon blank.",
    "14476.99", "2023-08-08", "2023", "", "",
    "Replace of frequency driver, CCS, Mexico (USASpending description; CCS named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_ccs_frequency_driver_replace_14k_2023",
    "FAC 7901-S-CCS-REPLACE OF FREQUENCY DRIVER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1123P0177_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1172",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX1123P0177_1900_-NONE-_-NONE- (misc_mexico_ccs_frequency_driver_replace_14k_2023). Signed 2023-08-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1123P0177_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_ccs_frequency_driver_replace_14k_2023 USD 0.014m. Supports misc_mexico_ccs_frequency_driver_replace_14k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14476.99; date_signed 2023-08-08.",
)
row_doc(
    "misc_dominican_republic_calle_bacu_residential_security_update_14k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic DS residential security update Calle Bacu 8 Los Cacicazgo",
    "Dominican Republic",
    "12 Nov 2013: Department of State awards contract SDR86014M0243 for DS residential security update Calle Bacu 8, Los Cacicazgo (PoP Dominican Republic); obligated USD 14,427.86. CapEx face = award obligation. Calle Bacu named; site coords not stated — lat/lon blank.",
    "14427.86", "2013-11-12", "2013", "", "",
    "Residential security update Calle Bacu 8 Los Cacicazgo, Dominican Republic (USASpending description; street named, site coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_republic_calle_bacu_residential_security_update_14k_2013",
    "DS-RESIDENTIAL SECURITY UPDATE CALLE BACU  8, LOS CACICAZGO: IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M0243_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1172",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86014M0243_1900_-NONE-_-NONE- (misc_dominican_republic_calle_bacu_residential_security_update_14k_2013). Signed 2013-11-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M0243_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_republic_calle_bacu_residential_security_update_14k_2013 USD 0.014m. Supports misc_dominican_republic_calle_bacu_residential_security_update_14k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14427.86; date_signed 2013-11-12.",
)

# === Cycle 1173 (seed 20262173) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "cummins_peru_datt_residence_generator_replacement_23k_2015",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Peru generator replacement for DATT residence",
    "Peru",
    "8 Sep 2015: Department of State awards contract SPE50015M2325 to Cummins Power Generation Inc. for generator replacement for DATT residence (PoP Peru); obligated USD 22,507.53. CapEx face = award obligation. DATT residence named; site coords not stated — lat/lon blank.",
    "22507.53", "2015-09-08", "2015", "", "",
    "Generator replacement for DATT residence, Peru (USASpending description; DATT residence named, site coords not stated — lat/lon blank).",
    "usaspending_cummins_peru_datt_residence_generator_replacement_23k_2015",
    "8/28 GENERATOR REPLACEMENT FOR DATT RESIDENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M2325_1900_-NONE-_-NONE-/",
    "Actor: CUMMINS POWER GENERATION INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1173",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50015M2325_1900_-NONE-_-NONE- (cummins_peru_datt_residence_generator_replacement_23k_2015). Signed 2015-09-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M2325_1900_-NONE-_-NONE-/.",
    "USASpending: cummins_peru_datt_residence_generator_replacement_23k_2015 USD 0.023m. Supports cummins_peru_datt_residence_generator_replacement_23k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 22507.53; date_signed 2015-09-08.",
)
row_doc(
    "norshield_peru_cusco_consular_teller_windows_door_22k_2015",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Peru Cusco consular office teller windows and door",
    "Peru",
    "28 Sep 2015: Department of State awards contract SPE50015M2501 to Norshield Security Products, LLC for teller windows and door Cusco consular office (PoP Peru); obligated USD 22,075.0. CapEx face = award obligation. Cusco named; site coords not stated — lat/lon blank.",
    "22075", "2015-09-28", "2015", "", "",
    "Teller windows and door, Cusco consular office, Peru (USASpending description; Cusco named, site coords not stated — lat/lon blank).",
    "usaspending_norshield_peru_cusco_consular_teller_windows_door_22k_2015",
    "9/25 TELLER WINDOWS AND DOOR - CUSCO CONSULAR OFFICE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M2501_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1173",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50015M2501_1900_-NONE-_-NONE- (norshield_peru_cusco_consular_teller_windows_door_22k_2015). Signed 2015-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M2501_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_peru_cusco_consular_teller_windows_door_22k_2015 USD 0.022m. Supports norshield_peru_cusco_consular_teller_windows_door_22k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 22075.0; date_signed 2015-09-28.",
)
row_doc(
    "misc_bahamas_shoreline_security_grills_install_14k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas installation of security grills 4 and 6 Shoreline",
    "Bahamas",
    "17 Sep 2014: Department of State awards contract SBF50014M0881 for installation of security grills, 4 and 6 Shoreline (PoP Bahamas); obligated USD 14,405.0. CapEx face = award obligation. Shoreline addresses named; site coords not stated — lat/lon blank.",
    "14405", "2014-09-17", "2014", "", "",
    "Installation of security grills at 4 and 6 Shoreline, Bahamas (USASpending description; Shoreline named, site coords not stated — lat/lon blank).",
    "usaspending_misc_bahamas_shoreline_security_grills_install_14k_2014",
    "PC-C-INSTALLATION OF SECURITY GRILLS, 4AND6 SHORELINE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50014M0881_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1173",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50014M0881_1900_-NONE-_-NONE- (misc_bahamas_shoreline_security_grills_install_14k_2014). Signed 2014-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50014M0881_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_shoreline_security_grills_install_14k_2014 USD 0.014m. Supports misc_bahamas_shoreline_security_grills_install_14k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14405.0; date_signed 2014-09-17.",
)
row_doc(
    "misc_dominican_republic_bambues_neutral_ground_busbars_install_14k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic neutral and ground busbars installation in modules Bambues",
    "Dominican Republic",
    "25 Jul 2024: Department of State awards contract 19DR8624P1805 for neutral and ground busbars installation in modules Bambues (PoP Dominican Republic); obligated USD 14,400.0. CapEx face = award obligation. Bambues named; site coords not stated — lat/lon blank.",
    "14400", "2024-07-25", "2024", "", "",
    "Neutral and ground busbars installation in modules Bambues, Dominican Republic (USASpending description; Bambues named, site coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_republic_bambues_neutral_ground_busbars_install_14k_2024",
    "NEUTRAL AND GROUND BUSBARS INSTALLATION IN MODULES  BAMBUES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624P1805_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1173",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624P1805_1900_-NONE-_-NONE- (misc_dominican_republic_bambues_neutral_ground_busbars_install_14k_2024). Signed 2024-07-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624P1805_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_republic_bambues_neutral_ground_busbars_install_14k_2024 USD 0.014m. Supports misc_dominican_republic_bambues_neutral_ground_busbars_install_14k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14400.0; date_signed 2024-07-25.",
)
row_doc(
    "misc_brazil_new_cgr_pool_fence_side_gate_14k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil new CGR pool fence and side gate",
    "Brazil",
    "7 Dec 2011: Department of State awards contract SBR93012C0007 for new CGR pool fence and side gate (PoP Brazil); obligated USD 14,365.88. CapEx face = award obligation. New CGR named; site coords not stated — lat/lon blank.",
    "14365.88", "2011-12-07", "2011", "", "",
    "Pool fence and side gate, new CGR, Brazil (USASpending description; CGR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_new_cgr_pool_fence_side_gate_14k_2011",
    "(NEW CGR) POLL FENCE AND SIDE GATE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93012C0007_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1173",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR93012C0007_1900_-NONE-_-NONE- (misc_brazil_new_cgr_pool_fence_side_gate_14k_2011). Signed 2011-12-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93012C0007_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_new_cgr_pool_fence_side_gate_14k_2011 USD 0.014m. Supports misc_brazil_new_cgr_pool_fence_side_gate_14k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14365.88; date_signed 2011-12-07.",
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
