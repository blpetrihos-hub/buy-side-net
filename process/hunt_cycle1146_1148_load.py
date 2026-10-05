#!/usr/bin/env python3
"""Cycles 1146–1148: USASpending LatAm CapEx residual (~USD0.010–0.030m).

Seeds: 20262146–20262148. Thin top-up dry.
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


# === Cycle 1146 (seed 20262146) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "sanx_global_mexico_embassy_ups_25k_2024",
    "energy", "power_plants_grid", "us",
    "SANX Global — Mexico embassy UPS",
    "Mexico",
    "18 Sep 2024: Department of State awards contract 19MX5324P1492 to SANX Global, LLC for MEX/FAC/7901SRVC/PMSC106/EMB/UPS (PoP Mexico); obligated USD 24,999.96. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "24999.96", "2024-09-18", "2024", "", "",
    "Embassy UPS, Mexico (USASpending description; EMB named, site coords not stated — lat/lon blank).",
    "usaspending_sanx_global_mexico_embassy_ups_25k_2024",
    "MEX/FAC/7901SRVC/PMSC106/EMB/UPS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5324P1492_1900_-NONE-_-NONE-/",
    "Actor: SANX Global, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1146",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5324P1492_1900_-NONE-_-NONE- (sanx_global_mexico_embassy_ups_25k_2024). Signed 2024-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5324P1492_1900_-NONE-_-NONE-/.",
    "USASpending: sanx_global_mexico_embassy_ups_25k_2024 USD 0.025m. Supports sanx_global_mexico_embassy_ups_25k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 24999.96; date_signed 2024-09-18.",
)
row_doc(
    "fabrication_designs_brazil_metal_door_screen_10k_2017",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Brazil metal door screen for international embassies",
    "Brazil",
    "8 Feb 2017: Department of State awards contract SAQMMA17M0265 to Fabrication Designs, Inc. for metal door, screen etc. (PoP Brazil); obligated USD 9,981.25. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "9981.25", "2017-02-08", "2017", "", "",
    "Metal door screen etc., Brazil (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_fabrication_designs_brazil_metal_door_screen_10k_2017",
    "METAL DOOR, SCREEN ETC. IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0265_1900_-NONE-_-NONE-/",
    "Actor: Fabrication Designs, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1146",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17M0265_1900_-NONE-_-NONE- (fabrication_designs_brazil_metal_door_screen_10k_2017). Signed 2017-02-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0265_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_brazil_metal_door_screen_10k_2017 USD 0.010m. Supports fabrication_designs_brazil_metal_door_screen_10k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9981.25; date_signed 2017-02-08.",
)
row_doc(
    "misc_uruguay_cmr_solar_panel_heating_system_25k_2012",
    "energy", "other_renewables", "other",
    "Miscellaneous foreign awardees — Uruguay CMR solar panel heating system for swimming pool and hot water",
    "Uruguay",
    "18 Sep 2012: Department of State awards contract SUY60012M0321 for supply and installation of solar panel heating system for swimming pool and hot water at CMR (PoP Uruguay); obligated USD 24,994.40. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.",
    "24994.4", "2012-09-18", "2012", "", "",
    "Solar panel heating system for swimming pool and hot water at CMR, Uruguay (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_uruguay_cmr_solar_panel_heating_system_25k_2012",
    "SUPPLY AND INSTALLATION OF SOLAR PANEL HEATING SYSTEM FOR SWIMMING POOL AND HOT WATER AT CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60012M0321_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle other_renewables.",
    "hunt_cycle1146",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SUY60012M0321_1900_-NONE-_-NONE- (misc_uruguay_cmr_solar_panel_heating_system_25k_2012). Signed 2012-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60012M0321_1900_-NONE-_-NONE-/.",
    "USASpending: misc_uruguay_cmr_solar_panel_heating_system_25k_2012 USD 0.025m. Supports misc_uruguay_cmr_solar_panel_heating_system_25k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 24994.4; date_signed 2012-09-18.",
)
row_doc(
    "misc_barbados_rss_air_wing_hangar_roof_refurbish_10k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Barbados INL refurbishing of RSS Air Wing hangar roof",
    "Barbados",
    "21 Dec 2015: Department of State awards contract SBB21016M0146 for INL refurbishing of RSS Air Wing hangar roof (PoP Barbados); obligated USD 10,000. CapEx face = award obligation. RSS Air Wing hangar named; site coords not stated — lat/lon blank.",
    "10000", "2015-12-21", "2015", "", "",
    "Refurbishing of RSS Air Wing hangar roof, Barbados (USASpending description; hangar named, site coords not stated — lat/lon blank).",
    "usaspending_misc_barbados_rss_air_wing_hangar_roof_refurbish_10k_2015",
    "INL: REFURBISHING OF RSS AIR WING HANGAR ROOF IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21016M0146_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1146",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21016M0146_1900_-NONE-_-NONE- (misc_barbados_rss_air_wing_hangar_roof_refurbish_10k_2015). Signed 2015-12-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21016M0146_1900_-NONE-_-NONE-/.",
    "USASpending: misc_barbados_rss_air_wing_hangar_roof_refurbish_10k_2015 USD 0.010m. Supports misc_barbados_rss_air_wing_hangar_roof_refurbish_10k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10000; date_signed 2015-12-21.",
)
row_doc(
    "misc_haiti_reyes_ahu_condensing_air_duct_install_28k_2023",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Haiti Reyes AHU condensing and air duct installation",
    "Haiti",
    "29 Sep 2023: Department of State awards contract 19HA7023P1397 for FAC-Reyes AHU condensing and air duct installation (PoP Haiti); obligated USD 27,965.95. CapEx face = award obligation. Reyes named; site coords not stated — lat/lon blank.",
    "27965.95", "2023-09-29", "2023", "", "",
    "Reyes AHU condensing and air duct installation, Haiti (USASpending description; Reyes named, site coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_reyes_ahu_condensing_air_duct_install_28k_2023",
    "FAC-REYES AHU CONDENSING AND AIR DUCT INSTALLATION.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P1397_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1146",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7023P1397_1900_-NONE-_-NONE- (misc_haiti_reyes_ahu_condensing_air_duct_install_28k_2023). Signed 2023-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P1397_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_reyes_ahu_condensing_air_duct_install_28k_2023 USD 0.028m. Supports misc_haiti_reyes_ahu_condensing_air_duct_install_28k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 27965.95; date_signed 2023-09-29.",
)

# === Cycle 1147 (seed 20262147) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "mst_maritime_chile_15kw_power_generator_10k_2024",
    "energy", "power_plants_grid", "us",
    "MST Maritime Management — Chile 15kW power generator",
    "Chile",
    "16 Aug 2024: Department of Defense awards contract W912CL24P0028 to MST Maritime Management LLC for 15k KW power generator SF 24 (PoP Chile); obligated USD 9,994.12. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "9994.12", "2024-08-16", "2024", "", "",
    "15kW power generator, Chile (USASpending description; site not named — lat/lon blank).",
    "usaspending_mst_maritime_chile_15kw_power_generator_10k_2024",
    "15K KW POWER GENERATOR SF 24",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL24P0028_9700_-NONE-_-NONE-/",
    "Actor: MST Maritime Management LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1147",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL24P0028_9700_-NONE-_-NONE- (mst_maritime_chile_15kw_power_generator_10k_2024). Signed 2024-08-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL24P0028_9700_-NONE-_-NONE-/.",
    "USASpending: mst_maritime_chile_15kw_power_generator_10k_2024 USD 0.010m. Supports mst_maritime_chile_15kw_power_generator_10k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9994.12; date_signed 2024-08-16.",
)
row_doc(
    "daikin_paraguay_air_cooled_chillers_split_system_26k_2023",
    "energy", "power_plants_grid", "us",
    "Daikin Applied Latin America — Paraguay air cooled chillers and split system",
    "Paraguay",
    "30 May 2023: Department of State awards contract 19PA1023P0237 to Daikin Applied Latin America, L.L.C. for air cooled chillers & split system (PoP Paraguay); obligated USD 25,971. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "25971", "2023-05-30", "2023", "", "",
    "Air cooled chillers and split system, Paraguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_daikin_paraguay_air_cooled_chillers_split_system_26k_2023",
    "DAIKIN -FAC-7901-XJZMSRVC-AIR COOLED CHILLERS & SPLIT SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1023P0237_1900_-NONE-_-NONE-/",
    "Actor: Daikin Applied Latin America, L.L.C. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1147",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PA1023P0237_1900_-NONE-_-NONE- (daikin_paraguay_air_cooled_chillers_split_system_26k_2023). Signed 2023-05-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1023P0237_1900_-NONE-_-NONE-/.",
    "USASpending: daikin_paraguay_air_cooled_chillers_split_system_26k_2023 USD 0.026m. Supports daikin_paraguay_air_cooled_chillers_split_system_26k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 25971; date_signed 2023-05-30.",
)
row_doc(
    "a1_security_guyana_cctv_installation_18k_2023",
    "infrastructure", "building_materials", "other",
    "A1 Security Solutions — Guyana CCTV installation",
    "Guyana",
    "31 May 2023: Department of State awards contract 19GY2023P0214 to A1 Security Solutions for CCTV installation (PoP Guyana); obligated USD 17,982.33. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "17982.33", "2023-05-31", "2023", "", "",
    "CCTV installation, Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_a1_security_guyana_cctv_installation_18k_2023",
    "CCTV INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2023P0214_1900_-NONE-_-NONE-/",
    "Actor: A1 Security Solutions (Guyana) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1147",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GY2023P0214_1900_-NONE-_-NONE- (a1_security_guyana_cctv_installation_18k_2023). Signed 2023-05-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GY2023P0214_1900_-NONE-_-NONE-/.",
    "USASpending: a1_security_guyana_cctv_installation_18k_2023 USD 0.018m. Supports a1_security_guyana_cctv_installation_18k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 17982.33; date_signed 2023-05-31.",
)
row_doc(
    "misc_panama_panel_boards_generator_connection_29k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Panama connection of panel boards into new building electric generator",
    "Panama",
    "22 Jun 2016: Smithsonian awards contract F16CC10396 for connection of existing panel boards into the new building's electric generator and add additional panel boards (PoP Panama); obligated USD 28,902.42. CapEx face = award obligation. Exact building unnamed — lat/lon blank.",
    "28902.42", "2016-06-22", "2016", "", "",
    "Connection of panel boards into new building electric generator, Panama (USASpending description; building not named — lat/lon blank).",
    "usaspending_misc_panama_panel_boards_generator_connection_29k_2016",
    "TO PERFORM CONNECTION OF EXISTING PANEL BOARDS, INTO THE NEW BUILDING'S ELECTRIC GENERATOR AND ADD ADDITIONAL PANEL BOARDS      IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F16CC10396_3300_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1147",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F16CC10396_3300_-NONE-_-NONE- (misc_panama_panel_boards_generator_connection_29k_2016). Signed 2016-06-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F16CC10396_3300_-NONE-_-NONE-/.",
    "USASpending: misc_panama_panel_boards_generator_connection_29k_2016 USD 0.029m. Supports misc_panama_panel_boards_generator_connection_29k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 28902.42; date_signed 2016-06-22.",
)
row_doc(
    "misc_brazil_solid_security_doors_locks_11k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil solid security doors and locks",
    "Brazil",
    "16 Feb 2024: Department of State awards contract 19BR8124P0117 for PID1076 solid security doors and locks (PoP Brazil); obligated USD 10,976.99. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "10976.99", "2024-02-16", "2024", "", "",
    "Solid security doors and locks, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_solid_security_doors_locks_11k_2024",
    "PID1076 SOLID SECURITY DOORS AND LOCKS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8124P0117_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1147",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR8124P0117_1900_-NONE-_-NONE- (misc_brazil_solid_security_doors_locks_11k_2024). Signed 2024-02-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8124P0117_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_solid_security_doors_locks_11k_2024 USD 0.011m. Supports misc_brazil_solid_security_doors_locks_11k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10976.99; date_signed 2024-02-16.",
)

# === Cycle 1148 (seed 20262148) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "harden_haiti_chancery_windows_replacement_20k_2024",
    "infrastructure", "building_materials", "us",
    "Harden Architectural Security Products — Haiti chancery windows replacement",
    "Haiti",
    "9 Jul 2024: Department of State awards contract 19HA7024P0645 to Harden Architectural Security Products, LLC for windows replacement for chancery building (PoP Haiti); obligated USD 19,564. CapEx face = award obligation. Chancery named; site coords not stated — lat/lon blank.",
    "19564", "2024-07-09", "2024", "", "",
    "Windows replacement for chancery building, Haiti (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_harden_haiti_chancery_windows_replacement_20k_2024",
    "FAC- WINDOWS REPLACEMENT FOR CHANCERY BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7024P0645_1900_-NONE-_-NONE-/",
    "Actor: Harden Architectural Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1148",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7024P0645_1900_-NONE-_-NONE- (harden_haiti_chancery_windows_replacement_20k_2024). Signed 2024-07-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7024P0645_1900_-NONE-_-NONE-/.",
    "USASpending: harden_haiti_chancery_windows_replacement_20k_2024 USD 0.020m. Supports harden_haiti_chancery_windows_replacement_20k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19564; date_signed 2024-07-09.",
)
row_doc(
    "ross_technology_dominican_republic_mcac_scac_gate_motor_drive_17k_2017",
    "infrastructure", "building_materials", "us",
    "Ross Technology — Dominican Republic motor drive for MCAC and SCAC gates",
    "Dominican Republic",
    "17 Feb 2017: Department of State awards contract SDR86017M0352 to Ross Technology Company for motor drive for MCAC and SCAC gates (PoP Dominican Republic); obligated USD 16,719. CapEx face = award obligation. Exact gates unnamed — lat/lon blank.",
    "16719", "2017-02-17", "2017", "", "",
    "Motor drive for MCAC and SCAC gates, Dominican Republic (USASpending description; gates named by type, site coords not stated — lat/lon blank).",
    "usaspending_ross_technology_dominican_republic_mcac_scac_gate_motor_drive_17k_2017",
    "IGF::CL::IGF MOTOR DRIVE FOR MCAC AND SCAC GATES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86017M0352_1900_-NONE-_-NONE-/",
    "Actor: Ross Technology Company (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1148",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86017M0352_1900_-NONE-_-NONE- (ross_technology_dominican_republic_mcac_scac_gate_motor_drive_17k_2017). Signed 2017-02-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86017M0352_1900_-NONE-_-NONE-/.",
    "USASpending: ross_technology_dominican_republic_mcac_scac_gate_motor_drive_17k_2017 USD 0.017m. Supports ross_technology_dominican_republic_mcac_scac_gate_motor_drive_17k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 16719; date_signed 2017-02-17.",
)
row_doc(
    "misc_costa_rica_dcr_sidewalk_construction_30k_2010",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Costa Rica DCR sidewalk construction",
    "Costa Rica",
    "29 Jan 2010: Department of State awards contract SCS80010C0004 for DCR sidewalk construction (PoP Costa Rica); obligated USD 29,987.19. CapEx face = award obligation. DCR named; site coords not stated — lat/lon blank.",
    "29987.19", "2010-01-29", "2010", "", "",
    "DCR sidewalk construction, Costa Rica (USASpending description; DCR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_dcr_sidewalk_construction_30k_2010",
    "DCR SIDEWALK CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80010C0004_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1148",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80010C0004_1900_-NONE-_-NONE- (misc_costa_rica_dcr_sidewalk_construction_30k_2010). Signed 2010-01-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80010C0004_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_dcr_sidewalk_construction_30k_2010 USD 0.030m. Supports misc_costa_rica_dcr_sidewalk_construction_30k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 29987.19; date_signed 2010-01-29.",
)
row_doc(
    "misc_suriname_prison_surveillance_cameras_27k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Suriname small prison project surveillance cameras PID and HVB",
    "Suriname",
    "3 Mar 2016: Department of State awards contract SNS50016M0297 for small prison project: surveillance cameras PID and HVB (PoP Suriname); obligated USD 27,000. CapEx face = award obligation. Exact prison unnamed — lat/lon blank.",
    "27000", "2016-03-03", "2016", "", "",
    "Surveillance cameras for small prison project PID and HVB, Suriname (USASpending description; prison project named, site coords not stated — lat/lon blank).",
    "usaspending_misc_suriname_prison_surveillance_cameras_27k_2016",
    "IGF::OT::IGF-SMALL PRISON PROJECT: SURVEILLANCE CAMERAS PID AND HVB",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNS50016M0297_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1148",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SNS50016M0297_1900_-NONE-_-NONE- (misc_suriname_prison_surveillance_cameras_27k_2016). Signed 2016-03-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNS50016M0297_1900_-NONE-_-NONE-/.",
    "USASpending: misc_suriname_prison_surveillance_cameras_27k_2016 USD 0.027m. Supports misc_suriname_prison_surveillance_cameras_27k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 27000; date_signed 2016-03-03.",
)
row_doc(
    "soged_haiti_mission_director_onan_generator_26k_2011",
    "energy", "power_plants_grid", "other",
    "SOGED — Haiti Onan diesel generator 80 DGDA-SA for mission director residence",
    "Haiti",
    "18 Jul 2011: USAID awards contract AID521O001100221 to Societe Generale de Distribution SA for Onan diesel generator 80 DGDA-SA for mission director residence (PoP Haiti); obligated USD 26,000. CapEx face = award obligation. Mission director residence named; site coords not stated — lat/lon blank.",
    "26000", "2011-07-18", "2011", "", "",
    "Onan diesel generator 80 DGDA-SA for mission director residence, Haiti (USASpending description; residence named, site coords not stated — lat/lon blank).",
    "usaspending_soged_haiti_mission_director_onan_generator_26k_2011",
    "THIS IS A FIRM FIXED PO TO SECURE THE SERVICES OF SOGED FOR ONAN DIESEL GENERATOR 80 DGDA-SA FOR MISSION DIRECTOR RESIDENCE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521O001100221_7200_-NONE-_-NONE-/",
    "Actor: Societe Generale de Distribution SA (Haiti) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1148",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521O001100221_7200_-NONE-_-NONE- (soged_haiti_mission_director_onan_generator_26k_2011). Signed 2011-07-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521O001100221_7200_-NONE-_-NONE-/.",
    "USASpending: soged_haiti_mission_director_onan_generator_26k_2011 USD 0.026m. Supports soged_haiti_mission_director_onan_generator_26k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 26000; date_signed 2011-07-18.",
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
