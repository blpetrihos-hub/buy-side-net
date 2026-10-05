#!/usr/bin/env python3
"""Cycles 1210–1215: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262210–20262215. Thin top-up dry.
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

# === Cycle 1210 ===
row_doc(
    "generac_haiti_mobile_tower_lights_hnp_north_218k_2012",
    "energy", "power_plants_grid", "us",
    "Generac Mobile Products — Haiti mobile tower lights for HNP (North)",
    "Haiti",
    "14 Jun 2012: Department of State awards contract SHA70012F0815 to GENERAC MOBILE PRODUCTS, LLC for Mobile tower lights for HNP (North) (PoP Haiti); obligated USD 218304.60. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "218304.60", "2012-06-14", "2012", "", "",
    "Mobile tower lights for HNP (North), Haiti (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_generac_haiti_mobile_tower_lights_hnp_north_218k_2012",
    "MOBILE TOWER LIGHTS FOR HNP (NORTH)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHA70012F0815_1900_GS07F0211M_4730/",
    "Actor: GENERAC MOBILE PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1210",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHA70012F0815_1900_GS07F0211M_4730 (generac_haiti_mobile_tower_lights_hnp_north_218k_2012). Signed 2012-06-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHA70012F0815_1900_GS07F0211M_4730/.",
    "USASpending: generac_haiti_mobile_tower_lights_hnp_north_218k_2012 USD 0.218m. Supports generac_haiti_mobile_tower_lights_hnp_north_218k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 218304.6; date_signed 2012-06-14.",
)

# === Cycle 1210 ===
row_doc(
    "eaton_dominican_ups_for_dncd_27k_2011",
    "energy", "power_plants_grid", "us",
    "Eaton Corporation — Dominican Republic UPS for DNCD",
    "Dominican Republic",
    "1 Sep 2011: Department of State awards contract SDR86011F0043 to EATON CORPORATION for UPS for DNCD (PoP Dominican Republic); obligated USD 26613. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "26613", "2011-09-01", "2011", "", "",
    "UPS for DNCD, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_eaton_dominican_ups_for_dncd_27k_2011",
    "NAS-MI-IN23DRMG-UPS FOR DNCD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011F0043_1900_GS07F9460G_4730/",
    "Actor: EATON CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1210",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86011F0043_1900_GS07F9460G_4730 (eaton_dominican_ups_for_dncd_27k_2011). Signed 2011-09-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011F0043_1900_GS07F9460G_4730/.",
    "USASpending: eaton_dominican_ups_for_dncd_27k_2011 USD 0.027m. Supports eaton_dominican_ups_for_dncd_27k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 26613.0; date_signed 2011-09-01.",
)

# === Cycle 1210 ===
row_doc(
    "misc_mexico_nogales_perimeter_fence_upgrade_13k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico OBO upgrade perimeter fence of post Nogales",
    "Mexico",
    "27 Sep 2013: Department of State awards contract SMX60013C0001 for Upgrade perimeter fence of post — Nogales (PoP Mexico); obligated USD 12946.42. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12946.42", "2013-09-27", "2013", "", "",
    "Upgrade perimeter fence of post — Nogales, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_nogales_perimeter_fence_upgrade_13k_2013",
    "OBO - AWARD TO UPGRADE PERIMETER FENCE OF POST - NOGALES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX60013C0001_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1210",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX60013C0001_1900_-NONE-_-NONE- (misc_mexico_nogales_perimeter_fence_upgrade_13k_2013). Signed 2013-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX60013C0001_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_nogales_perimeter_fence_upgrade_13k_2013 USD 0.013m. Supports misc_mexico_nogales_perimeter_fence_upgrade_13k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12946.42; date_signed 2013-09-27.",
)

# === Cycle 1210 ===
row_doc(
    "misc_venezuela_chancery_fan_coil_switchboard_13k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Venezuela chancery fan coil installation at switchboard area",
    "Venezuela",
    "10 Dec 2012: Department of State awards contract SVE30013M0091 for Chancery fan coil installation at switchboard area (PoP Venezuela); obligated USD 12925.92. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12925.92", "2012-12-10", "2012", "", "",
    "Chancery fan coil installation at switchboard area, Venezuela (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_venezuela_chancery_fan_coil_switchboard_13k_2013",
    "CHANCERY: FAN COIL INSTALLATION AT SWITCHBOARD AREA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30013M0091_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1210",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30013M0091_1900_-NONE-_-NONE- (misc_venezuela_chancery_fan_coil_switchboard_13k_2013). Signed 2012-12-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30013M0091_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_chancery_fan_coil_switchboard_13k_2013 USD 0.013m. Supports misc_venezuela_chancery_fan_coil_switchboard_13k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12925.92; date_signed 2012-12-10.",
)

# === Cycle 1210 ===
row_doc(
    "misc_peru_chilled_water_primary_pumps_install_13k_2018",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Peru installation of new chilled water primary pumps",
    "Peru",
    "21 Jun 2018: Department of State awards contract 19PE5018C0014 for Installation of new chilled water primary pumps (PoP Peru); obligated USD 12924.79. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12924.79", "2018-06-21", "2018", "", "",
    "Installation of new chilled water primary pumps, Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_peru_chilled_water_primary_pumps_install_13k_2018",
    "INSTALLATION OF NEW CHILLED WATER PRIMARY PUMPS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5018C0014_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1210",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5018C0014_1900_-NONE-_-NONE- (misc_peru_chilled_water_primary_pumps_install_13k_2018). Signed 2018-06-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5018C0014_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_chilled_water_primary_pumps_install_13k_2018 USD 0.013m. Supports misc_peru_chilled_water_primary_pumps_install_13k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12924.79; date_signed 2018-06-21.",
)

# === Cycle 1211 ===
row_doc(
    "generac_jamaica_light_tower_power_generators_20k_2016",
    "energy", "power_plants_grid", "us",
    "Generac Mobile Products — Jamaica RSO embassy general use light tower and power generators",
    "Jamaica",
    "25 Jul 2016: Department of State awards contract SJM37016F0051 to GENERAC MOBILE PRODUCTS, LLC for RSO embassy general use light tower, power generators — ICASS (PoP Jamaica); obligated USD 20115.27. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "20115.27", "2016-07-25", "2016", "", "",
    "RSO embassy general use light tower, power generators — ICASS, Jamaica (USASpending description; site not named — lat/lon blank).",
    "usaspending_generac_jamaica_light_tower_power_generators_20k_2016",
    "RSO - EMB. GENERAL USE LIGHT TOWER, POWER GENERATOS - ICASS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016F0051_1900_GS07F0211M_4730/",
    "Actor: GENERAC MOBILE PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1211",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37016F0051_1900_GS07F0211M_4730 (generac_jamaica_light_tower_power_generators_20k_2016). Signed 2016-07-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016F0051_1900_GS07F0211M_4730/.",
    "USASpending: generac_jamaica_light_tower_power_generators_20k_2016 USD 0.020m. Supports generac_jamaica_light_tower_power_generators_20k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 20115.27; date_signed 2016-07-25.",
)

# === Cycle 1211 ===
row_doc(
    "ross_technology_belize_window_nob_carpentry_9k_2016",
    "infrastructure", "building_materials", "us",
    "Ross Technology — Belize FM carpentry window nob",
    "Belize",
    "20 May 2016: Department of State awards contract SBH20016M0254 to ROSS TECHNOLOGY COMPANY for FM carpentry — window nob (PoP Belize); obligated USD 8796. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "8796", "2016-05-20", "2016", "", "",
    "FM carpentry — window nob, Belize (USASpending description; site not named — lat/lon blank).",
    "usaspending_ross_technology_belize_window_nob_carpentry_9k_2016",
    "IGF::OT::IGF FM - CARPENTRY - 7901 - WINDOW NOB",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20016M0254_1900_-NONE-_-NONE-/",
    "Actor: ROSS TECHNOLOGY COMPANY (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1211",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20016M0254_1900_-NONE-_-NONE- (ross_technology_belize_window_nob_carpentry_9k_2016). Signed 2016-05-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20016M0254_1900_-NONE-_-NONE-/.",
    "USASpending: ross_technology_belize_window_nob_carpentry_9k_2016 USD 0.009m. Supports ross_technology_belize_window_nob_carpentry_9k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8796.0; date_signed 2016-05-20.",
)

# === Cycle 1211 ===
row_doc(
    "misc_ecuador_replace_doors_usg_house_13k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador replace doors for USG house",
    "Ecuador",
    "20 Sep 2010: Department of State awards contract SEC30010M0997 for Replace doors for USG house (PoP Ecuador); obligated USD 12924. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12924", "2010-09-20", "2010", "", "",
    "Replace doors for USG house, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_replace_doors_usg_house_13k_2010",
    "REPLACE DOORS FOR USG HOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC30010M0997_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1211",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SEC30010M0997_1900_-NONE-_-NONE- (misc_ecuador_replace_doors_usg_house_13k_2010). Signed 2010-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC30010M0997_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_replace_doors_usg_house_13k_2010 USD 0.013m. Supports misc_ecuador_replace_doors_usg_house_13k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12924.0; date_signed 2010-09-20.",
)

# === Cycle 1211 ===
row_doc(
    "misc_dominican_make_ready_sanabacoa_4_13k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic USAID make-ready Sanabacoa 4",
    "Dominican Republic",
    "10 Jul 2024: Department of State awards contract 19DR8624C0055 for USAID make-ready works Sanabacoa 4 PID 591 (PoP Dominican Republic); obligated USD 12923.44. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12923.44", "2024-07-10", "2024", "", "",
    "USAID make-ready works Sanabacoa 4 PID 591, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_make_ready_sanabacoa_4_13k_2024",
    "USAID- MAKE READY WORKS SANABACOA 4 PID 591 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0055_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1211",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0055_1900_-NONE-_-NONE- (misc_dominican_make_ready_sanabacoa_4_13k_2024). Signed 2024-07-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0055_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_make_ready_sanabacoa_4_13k_2024 USD 0.013m. Supports misc_dominican_make_ready_sanabacoa_4_13k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12923.44; date_signed 2024-07-10.",
)

# === Cycle 1211 ===
row_doc(
    "misc_guatemala_concertina_razor_wire_replace_13k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guatemala concertina/razor wire removal and replacement",
    "Guatemala",
    "26 Sep 2019: Department of State awards contract 19GT5019P1016 for Concertina/razor wire removal and replacement (PoP Guatemala); obligated USD 12922.59. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12922.59", "2019-09-26", "2019", "", "",
    "Concertina/razor wire removal and replacement, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guatemala_concertina_razor_wire_replace_13k_2019",
    "CONCERTINA/RAZOR WIRE REMOVAL AND REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5019P1016_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1211",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GT5019P1016_1900_-NONE-_-NONE- (misc_guatemala_concertina_razor_wire_replace_13k_2019). Signed 2019-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5019P1016_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_concertina_razor_wire_replace_13k_2019 USD 0.013m. Supports misc_guatemala_concertina_razor_wire_replace_13k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12922.59; date_signed 2019-09-26.",
)

# === Cycle 1212 ===
row_doc(
    "generac_bahamas_portable_light_tower_8k_2011",
    "energy", "power_plants_grid", "us",
    "Generac Mobile Products — Bahamas portable light tower",
    "Bahamas",
    "21 Sep 2011: Department of State awards contract SBF50011M0821 to GENERAC MOBILE PRODUCTS, LLC for EOY portable light tower (PoP Bahamas); obligated USD 8245.65. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "8245.65", "2011-09-21", "2011", "", "",
    "EOY portable light tower, Bahamas (USASpending description; site not named — lat/lon blank).",
    "usaspending_generac_bahamas_portable_light_tower_8k_2011",
    "C-EOY-PORTABLE LIGHT TOWER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50011M0821_1900_-NONE-_-NONE-/",
    "Actor: GENERAC MOBILE PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1212",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50011M0821_1900_-NONE-_-NONE- (generac_bahamas_portable_light_tower_8k_2011). Signed 2011-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50011M0821_1900_-NONE-_-NONE-/.",
    "USASpending: generac_bahamas_portable_light_tower_8k_2011 USD 0.008m. Supports generac_bahamas_portable_light_tower_8k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8245.65; date_signed 2011-09-21.",
)

# === Cycle 1212 ===
row_doc(
    "fabrication_designs_guyana_metal_door_screen_6k_2020",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Guyana metal door screen",
    "Guyana",
    "28 Jan 2020: Department of State awards contract 19AQMM20P0295 to FABRICATION DESIGNS, INC. for Metal door screen etc. (PoP Guyana); obligated USD 6203.34. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "6203.34", "2020-01-28", "2020", "", "",
    "Metal door screen etc., Guyana (USASpending description; site not named — lat/lon blank).",
    "usaspending_fabrication_designs_guyana_metal_door_screen_6k_2020",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0295_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1212",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20P0295_1900_-NONE-_-NONE- (fabrication_designs_guyana_metal_door_screen_6k_2020). Signed 2020-01-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0295_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_guyana_metal_door_screen_6k_2020 USD 0.006m. Supports fabrication_designs_guyana_metal_door_screen_6k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6203.34; date_signed 2020-01-28.",
)

# === Cycle 1212 ===
row_doc(
    "misc_bahamas_cctv_dale_house_13k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas CCTV camera system at Dale House",
    "Bahamas",
    "1 Dec 2021: Department of State awards contract 19BF5022P0111 for CCTV camera system at Dale House (PoP Bahamas); obligated USD 12911.36. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12911.36", "2021-12-01", "2021", "", "",
    "CCTV camera system at Dale House, Bahamas (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_bahamas_cctv_dale_house_13k_2022",
    "CCTV CAMERA SYSTEM AT (DALE HOUSE)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5022P0111_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1212",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BF5022P0111_1900_-NONE-_-NONE- (misc_bahamas_cctv_dale_house_13k_2022). Signed 2021-12-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5022P0111_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_cctv_dale_house_13k_2022 USD 0.013m. Supports misc_bahamas_cctv_dale_house_13k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12911.36; date_signed 2021-12-01.",
)

# === Cycle 1212 ===
row_doc(
    "misc_guatemala_avn_barracks_renovation_13k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guatemala renovation of AVN barracks",
    "Guatemala",
    "18 Feb 2010: Department of Defense awards contract W912CL10C0011 for Renovation of AVN barracks (PoP Guatemala); obligated USD 12856.10. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12856.10", "2010-02-18", "2010", "", "",
    "Renovation of AVN barracks, Guatemala (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_guatemala_avn_barracks_renovation_13k_2010",
    "RENOVATION OF AVN BARRACKS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0011_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1212",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0011_9700_-NONE-_-NONE- (misc_guatemala_avn_barracks_renovation_13k_2010). Signed 2010-02-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0011_9700_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_avn_barracks_renovation_13k_2010 USD 0.013m. Supports misc_guatemala_avn_barracks_renovation_13k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12856.1; date_signed 2010-02-18.",
)

# === Cycle 1212 ===
row_doc(
    "misc_dominican_power_generator_make_ready_ananman_13k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic OBO purchase of power generator for make-ready",
    "Dominican Republic",
    "8 Aug 2011: Department of State awards contract SDR86011M1307 for OBO purchase of power generator for make-ready at Mr. Paul Anaman (PoP Dominican Republic); obligated USD 12850. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12850", "2011-08-08", "2011", "", "",
    "OBO purchase of power generator for make-ready at Mr. Paul Anaman, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_power_generator_make_ready_ananman_13k_2011",
    "OBO -PURCHASE OF POWER GENERATOR TP MAKE READY AT MR. PAUL ANAMAN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011M1307_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1212",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86011M1307_1900_-NONE-_-NONE- (misc_dominican_power_generator_make_ready_ananman_13k_2011). Signed 2011-08-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011M1307_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_power_generator_make_ready_ananman_13k_2011 USD 0.013m. Supports misc_dominican_power_generator_make_ready_ananman_13k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12850.0; date_signed 2011-08-08.",
)

# === Cycle 1213 ===
row_doc(
    "ross_technology_suriname_metal_door_screen_6k_2018",
    "infrastructure", "building_materials", "us",
    "Ross Technology — Suriname metal door screen",
    "Suriname",
    "20 Mar 2018: Department of State awards contract 19AQMM18P0550 to ROSS TECHNOLOGY COMPANY for Metal door screen etc. (PoP Suriname); obligated USD 6155. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "6155", "2018-03-20", "2018", "", "",
    "Metal door screen etc., Suriname (USASpending description; site not named — lat/lon blank).",
    "usaspending_ross_technology_suriname_metal_door_screen_6k_2018",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P0550_1900_-NONE-_-NONE-/",
    "Actor: ROSS TECHNOLOGY COMPANY (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1213",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18P0550_1900_-NONE-_-NONE- (ross_technology_suriname_metal_door_screen_6k_2018). Signed 2018-03-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P0550_1900_-NONE-_-NONE-/.",
    "USASpending: ross_technology_suriname_metal_door_screen_6k_2018 USD 0.006m. Supports ross_technology_suriname_metal_door_screen_6k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6155.0; date_signed 2018-03-20.",
)

# === Cycle 1213 ===
row_doc(
    "norshield_brazil_metal_door_screen_6k_2018",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Brazil metal door screen",
    "Brazil",
    "27 Mar 2018: Department of State awards contract 19AQMM18P0584 to NORSHIELD SECURITY PRODUCTS, LLC for Metal door screen etc. (PoP Brazil); obligated USD 5800. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "5800", "2018-03-27", "2018", "", "",
    "Metal door screen etc., Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_brazil_metal_door_screen_6k_2018",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P0584_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1213",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18P0584_1900_-NONE-_-NONE- (norshield_brazil_metal_door_screen_6k_2018). Signed 2018-03-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P0584_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_brazil_metal_door_screen_6k_2018 USD 0.006m. Supports norshield_brazil_metal_door_screen_6k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5800.0; date_signed 2018-03-27.",
)

# === Cycle 1213 ===
row_doc(
    "misc_dominican_make_ready_bambues_38_13k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic INL make-ready Bambues 38",
    "Dominican Republic",
    "28 Jun 2022: Department of State awards contract 19DR8622C0020 for INL make-ready Bambues 38 PID 853 (PoP Dominican Republic); obligated USD 12833.90. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12833.90", "2022-06-28", "2022", "", "",
    "INL make-ready Bambues 38 PID 853, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_make_ready_bambues_38_13k_2022",
    "INL- MAKE READY BAMBUES 38 PID 853 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622C0020_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1213",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8622C0020_1900_-NONE-_-NONE- (misc_dominican_make_ready_bambues_38_13k_2022). Signed 2022-06-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622C0020_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_make_ready_bambues_38_13k_2022 USD 0.013m. Supports misc_dominican_make_ready_bambues_38_13k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12833.9; date_signed 2022-06-28.",
)

# === Cycle 1213 ===
row_doc(
    "misc_chile_grills_13k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Chile grills",
    "Chile",
    "30 Dec 2024: Department of State awards contract 19C18025P0244 for Grills (PoP Chile); obligated USD 12807.33. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12807.33", "2024-12-30", "2024", "", "",
    "Grills, Chile (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_chile_grills_13k_2025",
    "GRILLS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18025P0244_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1213",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C18025P0244_1900_-NONE-_-NONE- (misc_chile_grills_13k_2025). Signed 2024-12-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18025P0244_1900_-NONE-_-NONE-/.",
    "USASpending: misc_chile_grills_13k_2025 USD 0.013m. Supports misc_chile_grills_13k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12807.33; date_signed 2024-12-30.",
)

# === Cycle 1213 ===
row_doc(
    "misc_el_salvador_cmr_water_heater_13k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — El Salvador water heater for CMR",
    "El Salvador",
    "9 Aug 2024: Department of State awards contract 19ES6024P0849 for Water heater for CMR (PoP El Salvador); obligated USD 12962.95. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12962.95", "2024-08-09", "2024", "", "",
    "Water heater for CMR, El Salvador (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_el_salvador_cmr_water_heater_13k_2024",
    "WATER HEATER FOR CMR - 19ES6024P0849",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6024P0849_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1213",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6024P0849_1900_-NONE-_-NONE- (misc_el_salvador_cmr_water_heater_13k_2024). Signed 2024-08-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6024P0849_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_cmr_water_heater_13k_2024 USD 0.013m. Supports misc_el_salvador_cmr_water_heater_13k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12962.95; date_signed 2024-08-09.",
)

# === Cycle 1214 ===
row_doc(
    "fabrication_designs_mexico_metal_door_screen_embassies_5k_2023",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Mexico metal door screen for international embassies",
    "Mexico",
    "15 Dec 2022: Department of State awards contract 19AQMM23P0103 to FABRICATION DESIGNS, INC. for Metal door screen etc. for international embassies (PoP Mexico); obligated USD 5336. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "5336", "2022-12-15", "2022", "", "",
    "Metal door screen etc. for international embassies, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_fabrication_designs_mexico_metal_door_screen_embassies_5k_2023",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0103_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1214",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23P0103_1900_-NONE-_-NONE- (fabrication_designs_mexico_metal_door_screen_embassies_5k_2023). Signed 2022-12-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0103_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_mexico_metal_door_screen_embassies_5k_2023 USD 0.005m. Supports fabrication_designs_mexico_metal_door_screen_embassies_5k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5336.0; date_signed 2022-12-15.",
)

# === Cycle 1214 ===
row_doc(
    "norshield_nicaragua_replace_2nd_broken_window_5k_2010",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Nicaragua replace 2nd broken window",
    "Nicaragua",
    "16 Sep 2010: Department of State awards contract SNU70010M0865 to NORSHIELD SECURITY PRODUCTS, LLC for Replace 2nd broken window (PoP Nicaragua); obligated USD 4941. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "4941", "2010-09-16", "2010", "", "",
    "Replace 2nd broken window, Nicaragua (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_nicaragua_replace_2nd_broken_window_5k_2010",
    "REPLACE 2ND BROKEN WINDOW - 7901",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70010M0865_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1214",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SNU70010M0865_1900_-NONE-_-NONE- (norshield_nicaragua_replace_2nd_broken_window_5k_2010). Signed 2010-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70010M0865_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_nicaragua_replace_2nd_broken_window_5k_2010 USD 0.005m. Supports norshield_nicaragua_replace_2nd_broken_window_5k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4941.0; date_signed 2010-09-16.",
)

# === Cycle 1214 ===
row_doc(
    "misc_brazil_potus_cables_electrical_install_13k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil POTUS/PTS speech cables and electrical installation",
    "Brazil",
    "19 Mar 2011: Department of State awards contract SBR82011M1494 for POTUS/PTS speech — cables and electrical installation (PoP Brazil); obligated USD 12822.05. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12822.05", "2011-03-19", "2011", "", "",
    "POTUS/PTS speech — cables and electrical installation, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_potus_cables_electrical_install_13k_2011",
    "POTUS/PTS/PTS SPEECH - CABLES AND ELECTRICAL INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82011M1494_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1214",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82011M1494_1900_-NONE-_-NONE- (misc_brazil_potus_cables_electrical_install_13k_2011). Signed 2011-03-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82011M1494_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_potus_cables_electrical_install_13k_2011 USD 0.013m. Supports misc_brazil_potus_cables_electrical_install_13k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12822.05; date_signed 2011-03-19.",
)

# === Cycle 1214 ===
row_doc(
    "misc_guyana_steel_material_msg_post1_renovation_13k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guyana FAC steel material Post 1 MSG renovation",
    "Guyana",
    "28 Jun 2016: Department of State awards contract SGY20016M0227 for FAC steel material Post 1 MSG renovation (PoP Guyana); obligated USD 12983.39. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12983.39", "2016-06-28", "2016", "", "",
    "FAC steel material Post 1 MSG renovation, Guyana (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_guyana_steel_material_msg_post1_renovation_13k_2016",
    "FAC - STEEL MATERIAL POST 1 MSG RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20016M0227_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1214",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGY20016M0227_1900_-NONE-_-NONE- (misc_guyana_steel_material_msg_post1_renovation_13k_2016). Signed 2016-06-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20016M0227_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guyana_steel_material_msg_post1_renovation_13k_2016 USD 0.013m. Supports misc_guyana_steel_material_msg_post1_renovation_13k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12983.39; date_signed 2016-06-28.",
)

# === Cycle 1214 ===
row_doc(
    "misc_guatemala_pavement_upgrade_construction_13k_2017",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Guatemala construction services pavement upgrade",
    "Guatemala",
    "27 Sep 2017: Department of State awards contract SGT50017M0955 for Construction services: pavement upgrade (PoP Guatemala); obligated USD 12891.32. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12891.32", "2017-09-27", "2017", "", "",
    "Construction services: pavement upgrade, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guatemala_pavement_upgrade_construction_13k_2017",
    "IGF::CL::IGF CONSTRUCTION SERVICES: PAVEMENT UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50017M0955_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1214",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50017M0955_1900_-NONE-_-NONE- (misc_guatemala_pavement_upgrade_construction_13k_2017). Signed 2017-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50017M0955_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_pavement_upgrade_construction_13k_2017 USD 0.013m. Supports misc_guatemala_pavement_upgrade_construction_13k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12891.32; date_signed 2017-09-27.",
)

# === Cycle 1215 ===
row_doc(
    "fabrication_designs_venezuela_metal_door_screen_5k_2016",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Venezuela metal door screen",
    "Venezuela",
    "13 Jun 2016: Department of State awards contract SAQMMA16M1153 to FABRICATION DESIGNS, INC. for Metal door screen etc. (PoP Venezuela); obligated USD 4704.65. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "4704.65", "2016-06-13", "2016", "", "",
    "Metal door screen etc., Venezuela (USASpending description; site not named — lat/lon blank).",
    "usaspending_fabrication_designs_venezuela_metal_door_screen_5k_2016",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M1153_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1215",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16M1153_1900_-NONE-_-NONE- (fabrication_designs_venezuela_metal_door_screen_5k_2016). Signed 2016-06-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M1153_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_venezuela_metal_door_screen_5k_2016 USD 0.005m. Supports fabrication_designs_venezuela_metal_door_screen_5k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4704.65; date_signed 2016-06-13.",
)

# === Cycle 1215 ===
row_doc(
    "norshield_colombia_metal_door_screen_5k_2016",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Colombia metal door screen",
    "Colombia",
    "25 Mar 2016: Department of State awards contract SAQMMA16M0553 to NORSHIELD SECURITY PRODUCTS, LLC for Metal door, screen etc. (PoP Colombia); obligated USD 4636. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "4636", "2016-03-25", "2016", "", "",
    "Metal door, screen etc., Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_colombia_metal_door_screen_5k_2016",
    "METAL DOOR, SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M0553_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1215",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16M0553_1900_-NONE-_-NONE- (norshield_colombia_metal_door_screen_5k_2016). Signed 2016-03-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M0553_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_colombia_metal_door_screen_5k_2016 USD 0.005m. Supports norshield_colombia_metal_door_screen_5k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4636.0; date_signed 2016-03-25.",
)

# === Cycle 1215 ===
row_doc(
    "misc_argentina_cmr_ahu_fan_coil_replace_13k_2018",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Argentina CMR air handling unit and fan coil unit replacement",
    "Argentina",
    "29 Sep 2018: Department of State awards contract 19AR2018P1054 for CMR air handling unit and fan coil unit replacement (PoP Argentina); obligated USD 12803.01. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12803.01", "2018-09-29", "2018", "", "",
    "CMR air handling unit and fan coil unit replacement, Argentina (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_cmr_ahu_fan_coil_replace_13k_2018",
    "FM - CMR - AIR HANDLING UNIT AND FAN COIL UNIT REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P1054_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1215",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2018P1054_1900_-NONE-_-NONE- (misc_argentina_cmr_ahu_fan_coil_replace_13k_2018). Signed 2018-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P1054_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_cmr_ahu_fan_coil_replace_13k_2018 USD 0.013m. Supports misc_argentina_cmr_ahu_fan_coil_replace_13k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12803.01; date_signed 2018-09-29.",
)

# === Cycle 1215 ===
row_doc(
    "misc_suriname_internet_satellite_dish_install_13k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Suriname new internet satellite dish installation work",
    "Suriname",
    "27 Jun 2022: Department of State awards contract 19NS5022P0363 for New internet satellite dish installation work (PoP Suriname); obligated USD 12800. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12800", "2022-06-27", "2022", "", "",
    "New internet satellite dish installation work, Suriname (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_suriname_internet_satellite_dish_install_13k_2022",
    "NEW INTERNET SATELLITE DISH INSTALLATION WORK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5022P0363_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1215",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19NS5022P0363_1900_-NONE-_-NONE- (misc_suriname_internet_satellite_dish_install_13k_2022). Signed 2022-06-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5022P0363_1900_-NONE-_-NONE-/.",
    "USASpending: misc_suriname_internet_satellite_dish_install_13k_2022 USD 0.013m. Supports misc_suriname_internet_satellite_dish_install_13k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12800.0; date_signed 2022-06-27.",
)

# === Cycle 1215 ===
row_doc(
    "misc_venezuela_piedras_arriba_apt31_make_ready_13k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Venezuela make-ready of Piedras Arriba apt 31",
    "Venezuela",
    "3 May 2016: Department of State awards contract SVE30016M0423 for Make-ready of Piedras Arriba, apt 31 (PoP Venezuela); obligated USD 12796.31. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "12796.31", "2016-05-03", "2016", "", "",
    "Make-ready of Piedras Arriba, apt 31, Venezuela (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_venezuela_piedras_arriba_apt31_make_ready_13k_2016",
    "IGF::CL::IGF MAKE READY OF PIEDRAS ARRIBA, APT  31.-7901.3 - URGENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30016M0423_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1215",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30016M0423_1900_-NONE-_-NONE- (misc_venezuela_piedras_arriba_apt31_make_ready_13k_2016). Signed 2016-05-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30016M0423_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_piedras_arriba_apt31_make_ready_13k_2016 USD 0.013m. Supports misc_venezuela_piedras_arriba_apt31_make_ready_13k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12796.31; date_signed 2016-05-03.",
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
