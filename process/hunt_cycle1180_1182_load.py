#!/usr/bin/env python3
"""Cycles 1180–1182: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262180–20262182. Thin top-up dry.
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


# === Cycle 1180 (seed 20262180) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "boland_trane_bahamas_nassau_embassy_meternet_purchase_41k_2014",
    "energy", "power_plants_grid", "us",
    "Boland Trane Services — Bahamas Nassau embassy MeterNet purchase",
    "Bahamas",
    "22 Sep 2014: Department of State awards contract SAQMMA14F3853 to Boland Trane Services Inc for purchase MeterNet for Embassy Nassau (PoP Bahamas); obligated USD 41,005.0. CapEx face = award obligation. Nassau embassy named; site coords not stated — lat/lon blank.",
    "41005", "2014-09-22", "2014", "", "",
    "MeterNet purchase for Embassy Nassau, Bahamas (USASpending description; Nassau named, site coords not stated — lat/lon blank).",
    "usaspending_boland_trane_bahamas_nassau_embassy_meternet_purchase_41k_2014",
    "PURCHASE METERNET FOR EMBASSY NASSAU IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F3853_1900_SAQMMA13D0169_1900/",
    "Actor: BOLAND TRANE SERVICES INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1180",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14F3853_1900_SAQMMA13D0169_1900 (boland_trane_bahamas_nassau_embassy_meternet_purchase_41k_2014). Signed 2014-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F3853_1900_SAQMMA13D0169_1900/.",
    "USASpending: boland_trane_bahamas_nassau_embassy_meternet_purchase_41k_2014 USD 0.041m. Supports boland_trane_bahamas_nassau_embassy_meternet_purchase_41k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 41005.0; date_signed 2014-09-22.",
)
row_doc(
    "cummins_mexico_ciudad_juarez_msgr_electric_generator_26k_2016",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Mexico Ciudad Juarez MSGR electric generator",
    "Mexico",
    "16 Aug 2016: Department of State awards contract SMX11516F0086 to Cummins Power Generation Inc. for CDJ MSGR electric generator prop P00222 (PoP Mexico); obligated USD 25,848.0. CapEx face = award obligation. Ciudad Juarez named; site coords not stated — lat/lon blank.",
    "25848", "2016-08-16", "2016", "", "",
    "MSGR electric generator, Ciudad Juarez, Mexico (USASpending description; Ciudad Juarez named, site coords not stated — lat/lon blank).",
    "usaspending_cummins_mexico_ciudad_juarez_msgr_electric_generator_26k_2016",
    "CDJ - MSGR - ELECTRIC GENERATOR PROP P00222",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516F0086_1900_GS07F017DA_4732/",
    "Actor: CUMMINS POWER GENERATION INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1180",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11516F0086_1900_GS07F017DA_4732 (cummins_mexico_ciudad_juarez_msgr_electric_generator_26k_2016). Signed 2016-08-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516F0086_1900_GS07F017DA_4732/.",
    "USASpending: cummins_mexico_ciudad_juarez_msgr_electric_generator_26k_2016 USD 0.026m. Supports cummins_mexico_ciudad_juarez_msgr_electric_generator_26k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 25848.0; date_signed 2016-08-16.",
)
row_doc(
    "misc_mexico_guadalajara_cgr_security_grilles_upgrade_14k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Guadalajara CGR security upgrades grilles",
    "Mexico",
    "10 Aug 2018: Department of State awards contract 19MX3018P0241 for GDL DS security upgrades grilles at the CGR (PoP Mexico); obligated USD 14,278.79. CapEx face = award obligation. Guadalajara CGR named; site coords not stated — lat/lon blank.",
    "14278.79", "2018-08-10", "2018", "", "",
    "Security upgrades grilles at CGR, Guadalajara, Mexico (USASpending description; Guadalajara named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_guadalajara_cgr_security_grilles_upgrade_14k_2018",
    "GDL-DS-SECURITY UPGRADES GRILLES AT THE CGR-FY18",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX3018P0241_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1180",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX3018P0241_1900_-NONE-_-NONE- (misc_mexico_guadalajara_cgr_security_grilles_upgrade_14k_2018). Signed 2018-08-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX3018P0241_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_guadalajara_cgr_security_grilles_upgrade_14k_2018 USD 0.014m. Supports misc_mexico_guadalajara_cgr_security_grilles_upgrade_14k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14278.79; date_signed 2018-08-10.",
)
row_doc(
    "misc_colombia_diran_buenaventura_air_conditioning_system_14k_2023",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Colombia air conditioning system for DIRAN Buenaventura",
    "Colombia",
    "10 Jul 2023: Department of State awards contract 19C01523P0335 for air conditioning system for DIRAN Buenaventura (PoP Colombia); obligated USD 14,259.59. CapEx face = award obligation. Buenaventura named; site coords not stated — lat/lon blank.",
    "14259.59", "2023-07-10", "2023", "", "",
    "Air conditioning system for DIRAN Buenaventura, Colombia (USASpending description; Buenaventura named, site coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_diran_buenaventura_air_conditioning_system_14k_2023",
    "45/AIR CONDITIONING SYSTEM FOR DIRAN BUENAVENTURA/0723",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01523P0335_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1180",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01523P0335_1900_-NONE-_-NONE- (misc_colombia_diran_buenaventura_air_conditioning_system_14k_2023). Signed 2023-07-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01523P0335_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_diran_buenaventura_air_conditioning_system_14k_2023 USD 0.014m. Supports misc_colombia_diran_buenaventura_air_conditioning_system_14k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14259.59; date_signed 2023-07-10.",
)
row_doc(
    "misc_mexico_dcr_kitchen_renovation_14k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico DCR kitchen renovation",
    "Mexico",
    "16 May 2011: Department of State awards contract SMX53011M0929 for OBO MEX DCR kitchen renovation and bathroom repair (PoP Mexico); obligated USD 14,242.93. CapEx face = award obligation. DCR named; site coords not stated — lat/lon blank.",
    "14242.93", "2011-05-16", "2011", "", "",
    "DCR kitchen renovation, Mexico (USASpending description; DCR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_dcr_kitchen_renovation_14k_2011",
    "OBO MEX DCR KITCHEN RENOVATION AND BATHROOM REPAIR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M0929_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1180",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53011M0929_1900_-NONE-_-NONE- (misc_mexico_dcr_kitchen_renovation_14k_2011). Signed 2011-05-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M0929_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_dcr_kitchen_renovation_14k_2011 USD 0.014m. Supports misc_mexico_dcr_kitchen_renovation_14k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14242.93; date_signed 2011-05-16.",
)

# === Cycle 1181 (seed 20262181) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "applied_security_mexico_tss_security_systems_25k_2020",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Mexico TSS security systems",
    "Mexico",
    "19 Apr 2020: Department of State awards contract 19AQMM20F1488 to Applied Security Technologies Inc for TSS security systems (PoP Mexico); obligated USD 24,606.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "24606", "2020-04-19", "2020", "", "",
    "TSS security systems, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_applied_security_mexico_tss_security_systems_25k_2020",
    "TSS SECURITY SYSTEMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1488_1900_19AQMM19D0002_1900/",
    "Actor: APPLIED SECURITY TECHNOLOGIES INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1181",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F1488_1900_19AQMM19D0002_1900 (applied_security_mexico_tss_security_systems_25k_2020). Signed 2020-04-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1488_1900_19AQMM19D0002_1900/.",
    "USASpending: applied_security_mexico_tss_security_systems_25k_2020 USD 0.025m. Supports applied_security_mexico_tss_security_systems_25k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 24606.0; date_signed 2020-04-19.",
)
row_doc(
    "bcs_usa_el_salvador_repeater_site_gps_ups_16k_2022",
    "energy", "power_plants_grid", "us",
    "BCS USA — El Salvador IRM TAR GPS and UPS for repeater site",
    "El Salvador",
    "30 Mar 2022: Department of State awards contract 19ES6022P0320 to BCS USA Inc for IRM TAR GPS and UPS for repeater site (PoP El Salvador); obligated USD 15,566.0. CapEx face = award obligation. Repeater site unnamed — lat/lon blank.",
    "15566", "2022-03-30", "2022", "", "",
    "GPS and UPS for repeater site, El Salvador (USASpending description; repeater site unnamed — lat/lon blank).",
    "usaspending_bcs_usa_el_salvador_repeater_site_gps_ups_16k_2022",
    "IRM - TAR - GPS AND UPS FOR REPETER SITE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0320_1900_-NONE-_-NONE-/",
    "Actor: BCS USA INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1181",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6022P0320_1900_-NONE-_-NONE- (bcs_usa_el_salvador_repeater_site_gps_ups_16k_2022). Signed 2022-03-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0320_1900_-NONE-_-NONE-/.",
    "USASpending: bcs_usa_el_salvador_repeater_site_gps_ups_16k_2022 USD 0.016m. Supports bcs_usa_el_salvador_repeater_site_gps_ups_16k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15566.0; date_signed 2022-03-30.",
)
row_doc(
    "misc_chile_la_llaveria_house20_terrace_renovation_14k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Chile terrace renovation La Llaveria house #20",
    "Chile",
    "1 Jul 2010: Department of State awards contract SCI80010M0623 for FAC terrace renovation La Llaveria house #20 (PoP Chile); obligated USD 14,207.51. CapEx face = award obligation. La Llaveria house #20 named; site coords not stated — lat/lon blank.",
    "14207.51", "2010-07-01", "2010", "", "",
    "Terrace renovation, La Llaveria house #20, Chile (USASpending description; house named, site coords not stated — lat/lon blank).",
    "usaspending_misc_chile_la_llaveria_house20_terrace_renovation_14k_2010",
    "FAC - TERRACE RENOVATION / LA LLAVERIA HOUSE # 20",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80010M0623_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1181",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCI80010M0623_1900_-NONE-_-NONE- (misc_chile_la_llaveria_house20_terrace_renovation_14k_2010). Signed 2010-07-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80010M0623_1900_-NONE-_-NONE-/.",
    "USASpending: misc_chile_la_llaveria_house20_terrace_renovation_14k_2010 USD 0.014m. Supports misc_chile_la_llaveria_house20_terrace_renovation_14k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14207.51; date_signed 2010-07-01.",
)
row_doc(
    "misc_honduras_cetep_comayagua_generator_install_14k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras INL/CARSI installation of generator CETEP Comayagua",
    "Honduras",
    "23 Apr 2024: Department of State awards contract 19H08024K0474 for INL/CARSI installation of generator CETEP Comayagua (PoP Honduras); obligated USD 14,204.28. CapEx face = award obligation. CETEP Comayagua named; site coords not stated — lat/lon blank.",
    "14204.28", "2024-04-23", "2024", "", "",
    "Generator installation CETEP Comayagua, Honduras (USASpending description; Comayagua named, site coords not stated — lat/lon blank).",
    "usaspending_misc_honduras_cetep_comayagua_generator_install_14k_2024",
    "INL/CARSI INSTALLATION OF GENERATOR CETEP COMAYAGUA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08024K0474_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1181",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19H08024K0474_1900_-NONE-_-NONE- (misc_honduras_cetep_comayagua_generator_install_14k_2024). Signed 2024-04-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08024K0474_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_cetep_comayagua_generator_install_14k_2024 USD 0.014m. Supports misc_honduras_cetep_comayagua_generator_install_14k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14204.28; date_signed 2024-04-23.",
)
row_doc(
    "misc_el_salvador_cafeteria_renovation_14k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador cafeteria renovation",
    "El Salvador",
    "4 May 2010: Department of State awards contract SES60010M0416 for cafeteria renovation (PoP El Salvador); obligated USD 14,201.53. CapEx face = award obligation. Exact cafeteria unnamed — lat/lon blank.",
    "14201.53", "2010-05-04", "2010", "", "",
    "Cafeteria renovation, El Salvador (USASpending description; cafeteria unnamed — lat/lon blank).",
    "usaspending_misc_el_salvador_cafeteria_renovation_14k_2010",
    "7901 FUNDS- CAFETERIA RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60010M0416_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1181",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60010M0416_1900_-NONE-_-NONE- (misc_el_salvador_cafeteria_renovation_14k_2010). Signed 2010-05-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60010M0416_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_cafeteria_renovation_14k_2010 USD 0.014m. Supports misc_el_salvador_cafeteria_renovation_14k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14201.53; date_signed 2010-05-04.",
)

# === Cycle 1182 (seed 20262182) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "ross_technology_haiti_msg_residence_windows_replace_15k_2018",
    "infrastructure", "building_materials", "us",
    "Ross Technology — Haiti windows replacement for MSG residence at the embassy",
    "Haiti",
    "29 Sep 2018: Department of State awards contract 19HA7018P1225 to Ross Technology Company for windows replacement for MSG residence at the embassy (PoP Haiti); obligated USD 15,421.0. CapEx face = award obligation. MSG residence/embassy named; site coords not stated — lat/lon blank.",
    "15421", "2018-09-29", "2018", "", "",
    "Windows replacement for MSG residence at the embassy, Haiti (USASpending description; MSG residence named, site coords not stated — lat/lon blank).",
    "usaspending_ross_technology_haiti_msg_residence_windows_replace_15k_2018",
    "WINDOWS REPLACEMENT FOR MSG RESIDENCE AT THE EMBASSY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7018P1225_1900_-NONE-_-NONE-/",
    "Actor: ROSS TECHNOLOGY COMPANY (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1182",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7018P1225_1900_-NONE-_-NONE- (ross_technology_haiti_msg_residence_windows_replace_15k_2018). Signed 2018-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7018P1225_1900_-NONE-_-NONE-/.",
    "USASpending: ross_technology_haiti_msg_residence_windows_replace_15k_2018 USD 0.015m. Supports ross_technology_haiti_msg_residence_windows_replace_15k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15421.0; date_signed 2018-09-29.",
)
row_doc(
    "fabrication_designs_belize_metal_door_screen_frame_15k_2024",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Belize metal door screen frame for international embassies",
    "Belize",
    "5 Jun 2024: Department of State awards contract 19AQMM24P0501 to Fabrication Designs, Inc. for metal door screen frame etc. for international embassies (PoP Belize); obligated USD 15,078.33. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "15078.33", "2024-06-05", "2024", "", "",
    "Metal door screen frame etc. for international embassies, Belize (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_fabrication_designs_belize_metal_door_screen_frame_15k_2024",
    "METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0501_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1182",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0501_1900_-NONE-_-NONE- (fabrication_designs_belize_metal_door_screen_frame_15k_2024). Signed 2024-06-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0501_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_belize_metal_door_screen_frame_15k_2024 USD 0.015m. Supports fabrication_designs_belize_metal_door_screen_frame_15k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15078.33; date_signed 2024-06-05.",
)
row_doc(
    "misc_jamaica_motor_pool_car_park_shade_install_14k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Jamaica motor pool car park shade installation",
    "Jamaica",
    "13 Mar 2014: Department of State awards contract SJM37014M0399 for FAC motor pool car park shade installation (PoP Jamaica); obligated USD 14,200.94. CapEx face = award obligation. Motor pool named; site coords not stated — lat/lon blank.",
    "14200.94", "2014-03-13", "2014", "", "",
    "Motor pool car park shade installation, Jamaica (USASpending description; motor pool named, site coords not stated — lat/lon blank).",
    "usaspending_misc_jamaica_motor_pool_car_park_shade_install_14k_2014",
    "FAC: MOTOR POOL CAR PARK SHADE INSTALLATION [ICASS]",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37014M0399_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1182",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37014M0399_1900_-NONE-_-NONE- (misc_jamaica_motor_pool_car_park_shade_install_14k_2014). Signed 2014-03-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37014M0399_1900_-NONE-_-NONE-/.",
    "USASpending: misc_jamaica_motor_pool_car_park_shade_install_14k_2014 USD 0.014m. Supports misc_jamaica_motor_pool_car_park_shade_install_14k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14200.94; date_signed 2014-03-13.",
)
row_doc(
    "misc_dominican_republic_punta_cana_tciu_generator_14k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic ICE HSI generator for TCIU offsite in Punta Cana",
    "Dominican Republic",
    "18 Aug 2017: Department of State awards contract SDR86017M0977 for ICE HSI generator for TCIU offsite in Punta Cana (PoP Dominican Republic); obligated USD 14,200.0. CapEx face = award obligation. Punta Cana named; site coords not stated — lat/lon blank.",
    "14200", "2017-08-18", "2017", "", "",
    "Generator for TCIU offsite in Punta Cana, Dominican Republic (USASpending description; Punta Cana named, site coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_republic_punta_cana_tciu_generator_14k_2017",
    "ICE HSI GENERATOR FOR TCIU OFFSITE IN PUNTA CANA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86017M0977_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1182",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86017M0977_1900_-NONE-_-NONE- (misc_dominican_republic_punta_cana_tciu_generator_14k_2017). Signed 2017-08-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86017M0977_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_republic_punta_cana_tciu_generator_14k_2017 USD 0.014m. Supports misc_dominican_republic_punta_cana_tciu_generator_14k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14200.0; date_signed 2017-08-18.",
)
row_doc(
    "misc_el_salvador_pje_grilles_manufacture_install_14k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador manufacture and installation of grilles PJE 7-15",
    "El Salvador",
    "2 Mar 2023: Department of State awards contract 19ES6023P0265 for manufacture and installation grilles PJE 7-15 (PoP El Salvador); obligated USD 14,155.0. CapEx face = award obligation. PJE 7-15 named; site coords not stated — lat/lon blank.",
    "14155", "2023-03-02", "2023", "", "",
    "Manufacture and installation of grilles PJE 7-15, El Salvador (USASpending description; PJE named, site coords not stated — lat/lon blank).",
    "usaspending_misc_el_salvador_pje_grilles_manufacture_install_14k_2023",
    "19ES6023P0265 PR 5841 MANUFACTURE AND  INSTALLATION GRILLES, PJE. 7-15",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6023P0265_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1182",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6023P0265_1900_-NONE-_-NONE- (misc_el_salvador_pje_grilles_manufacture_install_14k_2023). Signed 2023-03-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6023P0265_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_pje_grilles_manufacture_install_14k_2023 USD 0.014m. Supports misc_el_salvador_pje_grilles_manufacture_install_14k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14155.0; date_signed 2023-03-02.",
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
