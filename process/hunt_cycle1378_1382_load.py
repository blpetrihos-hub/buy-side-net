#!/usr/bin/env python3
"""Cycles 1378–1382: USASpending LatAm CapEx (Human Tech/Advanced C4/Edge/FAAC/Astrophysics + Bonatti/Rogers residual).

Seeds: 20262378–20262382. Thin top-up dry (NR/PRC); water CapEx logged.
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

# === Cycle 1378 ===
row_doc(
    "human_technologies_costa_rica_fronteras_riverine_boats_572k_2022",
    "infrastructure", "engineering_epc", "us",
    "Human Technologies \u2014 Costa Rica Fronteras riverine boats",
    "Costa Rica",
    "29 Sep 2022: Department of State awards contract to HUMAN TECHNOLOGIES CORP for FRONTERAS RIVERINE BOATS FOR INL/COSTA RICA; obligated USD 572412.27. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "572412.27", "2022-09-29", "2022", "", "",
    "FRONTERAS RIVERINE BOATS FOR INL/COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_human_technologies_costa_rica_fronteras_riverine_boats_572k_2022",
    "FRONTERAS RIVERINE BOATS FOR INL/COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22F0056_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) \u2014 us. Official USASpending Award API. Shuffle other_renewables dry\u2192engineering_epc CapEx; \u22651/3 U.S.",
    "hunt_cycle1378",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE22F0056_1900_19AQMM21D0007_1900 (human_technologies_costa_rica_fronteras_riverine_boats_572k_2022). Signed 2022-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22F0056_1900_19AQMM21D0007_1900/.",
    "USASpending: human_technologies_costa_rica_fronteras_riverine_boats_572k_2022 USD 0.572m. Supports human_technologies_costa_rica_fronteras_riverine_boats_572k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 572412.27; date_signed 2022-09-29.",
    investment_type="equipment_supply",
)

# === Cycle 1378 ===
row_doc(
    "advanced_c4_haiti_embassy_cabling_install_636k_2014",
    "infrastructure", "engineering_epc", "us",
    "Advanced C4 Solutions \u2014 Haiti US Embassy Port-au-Prince cabling install",
    "Haiti",
    "30 Sep 2014: Department of State awards contract to ADVANCED C4 SOLUTIONS INC for CABLING SURVEY AND INSTALLATION AND TERMINATION FOR US EMBASSY PORT AU PRINCE HAITI; obligated USD 635621.87. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "635621.87", "2014-09-30", "2014", "", "",
    "CABLING SURVEY AND INSTALLATION AND TERMINATION FOR US EMBASSY PORT AU PRINCE HAITI., Haiti (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_advanced_c4_haiti_embassy_cabling_install_636k_2014",
    "CABLING SURVEY AND INSTALLATION AND TERMINATION FOR US EMBASSY PORT AU PRINCE HAITI.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC14F0044_1900_GS06F0841Z_4732/",
    "Actor: ADVANCED C4 SOLUTIONS INC (U.S.) \u2014 us. Official USASpending Award API. Shuffle engineering_epc CapEx; \u22651/3 U.S.",
    "hunt_cycle1378",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC14F0044_1900_GS06F0841Z_4732 (advanced_c4_haiti_embassy_cabling_install_636k_2014). Signed 2014-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC14F0044_1900_GS06F0841Z_4732/.",
    "USASpending: advanced_c4_haiti_embassy_cabling_install_636k_2014 USD 0.636m. Supports advanced_c4_haiti_embassy_cabling_install_636k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 635621.87; date_signed 2014-09-30.",
    investment_type="epc",
)

# === Cycle 1378 ===
row_doc(
    "bonatti_el_salvador_la_libertad_fire_academy_854k_2025",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 El Salvador La Libertad fire academy",
    "El Salvador",
    "17 Sep 2025: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for FIRE ACADEMY IN LA LIBERTAD, EL SALVADOR; obligated USD 854484.68. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "854484.68", "2025-09-17", "2025", "", "",
    "FIRE ACADEMY IN LA LIBERTAD, EL SALVADOR. THE TASK WILL BE PERFORMED UNDER THE CENTRAL AME, El Salvador (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_el_salvador_la_libertad_fire_academy_854k_2025",
    "FIRE ACADEMY IN LA LIBERTAD, EL SALVADOR. THE TASK WILL BE PERFORMED UNDER THE CENTRAL AMERICA MATOC IN ACCORDANCE WITH THE ATTACHED SPECIFICATIONS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA209_9700_W9127823D0072_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1378",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA209_9700_W9127823D0072_9700 (bonatti_el_salvador_la_libertad_fire_academy_854k_2025). Signed 2025-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA209_9700_W9127823D0072_9700/.",
    "USASpending: bonatti_el_salvador_la_libertad_fire_academy_854k_2025 USD 0.854m. Supports bonatti_el_salvador_la_libertad_fire_academy_854k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 854484.68; date_signed 2025-09-17.",
    investment_type="epc",
)

# === Cycle 1378 ===
row_doc(
    "bonatti_honduras_soto_cano_dpw_facility_624k_2014",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 Honduras Soto Cano DPW facility",
    "Honduras",
    "29 Sep 2014: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for CONSTRUCT DPW FACILITY SOTO CAN HONDURAS; obligated USD 623820.93. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "623820.93", "2014-09-29", "2014", "", "",
    "CONSTRUCT DPW FACILITY SOTO CAN HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_honduras_soto_cano_dpw_facility_624k_2014",
    "CONSTRUCT DPW FACILITY SOTO CAN HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127813D0017_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1378",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0007_9700_W9127813D0017_9700 (bonatti_honduras_soto_cano_dpw_facility_624k_2014). Signed 2014-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127813D0017_9700/.",
    "USASpending: bonatti_honduras_soto_cano_dpw_facility_624k_2014 USD 0.624m. Supports bonatti_honduras_soto_cano_dpw_facility_624k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 623820.93; date_signed 2014-09-29.",
    investment_type="epc",
)

# === Cycle 1378 ===
row_doc(
    "bonatti_guatemala_coban_gpoi_clinic_624k_2012",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 Guatemala Coban GPOI clinic",
    "Guatemala",
    "24 Sep 2012: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for GPOI CLINIC COBAN, GUATEMALA; obligated USD 623518.73. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "623518.73", "2012-09-24", "2012", "", "",
    "GPOI CLINIC COBAN, GUATEMALA, Guatemala (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_guatemala_coban_gpoi_clinic_624k_2012",
    "GPOI CLINIC COBAN, GUATEMALA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127811D0044_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1378",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0009_9700_W9127811D0044_9700 (bonatti_guatemala_coban_gpoi_clinic_624k_2012). Signed 2012-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127811D0044_9700/.",
    "USASpending: bonatti_guatemala_coban_gpoi_clinic_624k_2012 USD 0.624m. Supports bonatti_guatemala_coban_gpoi_clinic_624k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 623518.73; date_signed 2012-09-24.",
    investment_type="epc",
)

# === Cycle 1379 ===
row_doc(
    "edge_el_salvador_handheld_radios_254k_2013",
    "infrastructure", "engineering_epc", "us",
    "Edge Technology Distributors \u2014 El Salvador handheld radios donation",
    "El Salvador",
    "8 Aug 2013: Department of State awards contract to EDGE TECHNOLOGY DISTRIBUTORS, INC. for HANDHELD RADIOS TO BE DONATED TO THE GOVERNMENT OF EL SALVADOR UNDER FOREIGN ASSISTANCE PROGRAM FOR INTERNATIONAL NARCOT; obligated USD 254352.34. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "254352.34", "2013-08-08", "2013", "", "",
    "HANDHELD RADIOS TO BE DONATED TO THE GOVERNMENT OF EL SALVADOR UNDER FOREIGN ASSISTANCE PR, El Salvador (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_edge_el_salvador_handheld_radios_254k_2013",
    "HANDHELD RADIOS TO BE DONATED TO THE GOVERNMENT OF EL SALVADOR UNDER FOREIGN ASSISTANCE PROGRAM FOR INTERNATIONAL NARCOTICS AND LAW ENFORCEMENT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC13M0009_1900_-NONE-_-NONE-/",
    "Actor: EDGE TECHNOLOGY DISTRIBUTORS, INC. (U.S.) \u2014 us. Official USASpending Award API. Shuffle bridges_roads dry\u2192engineering_epc CapEx; \u22651/3 U.S.",
    "hunt_cycle1379",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC13M0009_1900_-NONE-_-NONE- (edge_el_salvador_handheld_radios_254k_2013). Signed 2013-08-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC13M0009_1900_-NONE-_-NONE-/.",
    "USASpending: edge_el_salvador_handheld_radios_254k_2013 USD 0.254m. Supports edge_el_salvador_handheld_radios_254k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 254352.34; date_signed 2013-08-08.",
    investment_type="equipment_supply",
)

# === Cycle 1379 ===
row_doc(
    "human_technologies_guatemala_ibi_bcc_computers_244k_2025",
    "infrastructure", "engineering_epc", "us",
    "Human Technologies \u2014 Guatemala IBI BCC computer equipment",
    "Guatemala",
    "29 Sep 2025: Department of State awards contract to HUMAN TECHNOLOGIES CORP for INL GUATEMALA COMPUTER EQUIPMENT FOR IBI BCC; obligated USD 244426.88. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "244426.88", "2025-09-29", "2025", "", "",
    "INL GUATEMALA COMPUTER EQUIPMENT FOR IBI BCC, Guatemala (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_human_technologies_guatemala_ibi_bcc_computers_244k_2025",
    "INL GUATEMALA COMPUTER EQUIPMENT FOR IBI BCC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE25F0031_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) \u2014 us. Official USASpending Award API. Shuffle other_renewables dry\u2192engineering_epc CapEx; \u22651/3 U.S.",
    "hunt_cycle1379",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE25F0031_1900_19AQMM21D0007_1900 (human_technologies_guatemala_ibi_bcc_computers_244k_2025). Signed 2025-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE25F0031_1900_19AQMM21D0007_1900/.",
    "USASpending: human_technologies_guatemala_ibi_bcc_computers_244k_2025 USD 0.244m. Supports human_technologies_guatemala_ibi_bcc_computers_244k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 244426.88; date_signed 2025-09-29.",
    investment_type="equipment_supply",
)

# === Cycle 1379 ===
row_doc(
    "bonatti_el_salvador_comalapa_ops_bldg_expansion_565k_2014",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 El Salvador CSL Comalapa ops building expansion",
    "El Salvador",
    "27 Sep 2014: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for OPS BLDG EXPANSION CSL COMALAPA, EL SALV; obligated USD 565183.09. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "565183.09", "2014-09-27", "2014", "", "",
    "OPS BLDG EXPANSION CSL COMALAPA, EL SALV, El Salvador (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_el_salvador_comalapa_ops_bldg_expansion_565k_2014",
    "OPS BLDG EXPANSION CSL COMALAPA, EL SALV",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127813D0017_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1379",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0005_9700_W9127813D0017_9700 (bonatti_el_salvador_comalapa_ops_bldg_expansion_565k_2014). Signed 2014-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127813D0017_9700/.",
    "USASpending: bonatti_el_salvador_comalapa_ops_bldg_expansion_565k_2014 USD 0.565m. Supports bonatti_el_salvador_comalapa_ops_bldg_expansion_565k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 565183.09; date_signed 2014-09-27.",
    investment_type="epc",
)

# === Cycle 1379 ===
row_doc(
    "bonatti_honduras_castilla_pier_559k_2022",
    "infrastructure", "port_ownership", "other",
    "Bonatti Ingenieros \u2014 Honduras Puerto Castilla pier design-build",
    "Honduras",
    "9 Nov 2022: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for D/B CASTILLA PIER, PUERTO CASTILLA, HND; obligated USD 559465.40. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "559465.40", "2022-11-09", "2022", "", "",
    "D/B CASTILLA PIER, PUERTO CASTILLA, HND, Honduras (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_honduras_castilla_pier_559k_2022",
    "D/B CASTILLA PIER, PUERTO CASTILLA, HND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0006_9700_W9127821D0076_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle port_ownership CapEx.",
    "hunt_cycle1379",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127823F0006_9700_W9127821D0076_9700 (bonatti_honduras_castilla_pier_559k_2022). Signed 2022-11-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0006_9700_W9127821D0076_9700/.",
    "USASpending: bonatti_honduras_castilla_pier_559k_2022 USD 0.559m. Supports bonatti_honduras_castilla_pier_559k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 559465.40; date_signed 2022-11-09.",
    investment_type="epc",
)

# === Cycle 1379 ===
row_doc(
    "bonatti_honduras_soto_cano_fire_storage_547k_2020",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 Honduras Soto Cano fire department storage facility",
    "Honduras",
    "27 Sep 2020: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for FIRE DEPT STORAGE FACILITY, SOTO CANO; obligated USD 547015.99. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "547015.99", "2020-09-27", "2020", "", "",
    "FIRE DEPT STORAGE FACILITY, SOTO CANO, Honduras (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_honduras_soto_cano_fire_storage_547k_2020",
    "FIRE DEPT STORAGE FACILITY, SOTO CANO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0488_9700_W9127816D0099_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1379",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127820F0488_9700_W9127816D0099_9700 (bonatti_honduras_soto_cano_fire_storage_547k_2020). Signed 2020-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0488_9700_W9127816D0099_9700/.",
    "USASpending: bonatti_honduras_soto_cano_fire_storage_547k_2020 USD 0.547m. Supports bonatti_honduras_soto_cano_fire_storage_547k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 547015.99; date_signed 2020-09-27.",
    investment_type="epc",
)

# === Cycle 1380 ===
row_doc(
    "human_technologies_colombia_k9_equipment_286k_2022",
    "infrastructure", "engineering_epc", "us",
    "Human Technologies \u2014 Colombia DS/INL K9 equipment",
    "Colombia",
    "16 Sep 2022: Department of State awards contract to HUMAN TECHNOLOGIES CORP for AWARD OF DS/INL K9 EQUIPMENT FOR COLOMBIA; obligated USD 285501.80. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "285501.80", "2022-09-16", "2022", "", "",
    "AWARD OF DS/INL K9 EQUIPMENT FOR COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_human_technologies_colombia_k9_equipment_286k_2022",
    "AWARD OF DS/INL K9 EQUIPMENT FOR COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22F0038_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) \u2014 us. Official USASpending Award API. Shuffle fission_smr dry\u2192engineering_epc CapEx; \u22651/3 U.S.",
    "hunt_cycle1380",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE22F0038_1900_19AQMM21D0007_1900 (human_technologies_colombia_k9_equipment_286k_2022). Signed 2022-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22F0038_1900_19AQMM21D0007_1900/.",
    "USASpending: human_technologies_colombia_k9_equipment_286k_2022 USD 0.286m. Supports human_technologies_colombia_k9_equipment_286k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 285501.80; date_signed 2022-09-16.",
    investment_type="equipment_supply",
)

# === Cycle 1380 ===
row_doc(
    "faac_mexico_hidalgo_firearm_simulator_154k_2016",
    "infrastructure", "engineering_epc", "us",
    "FAAC \u2014 Mexico Hidalgo State Police Academy fixed firearm training simulator",
    "Mexico",
    "24 Jun 2016: Department of State awards contract to FAAC INCORPORATED for INL MEXICO - FIXED FIREARM TRAINING SIMULATOR FOR THE HIDALGO STATE POLICE ACADEMY. INCLUDES INSTALLATION AND 3-YEAR IN-; obligated USD 154051.90. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "154051.90", "2016-06-24", "2016", "", "",
    "INL MEXICO - FIXED FIREARM TRAINING SIMULATOR FOR THE HIDALGO STATE POLICE ACADEMY. INCLUD, Mexico (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_faac_mexico_hidalgo_firearm_simulator_154k_2016",
    "INL MEXICO - FIXED FIREARM TRAINING SIMULATOR FOR THE HIDALGO STATE POLICE ACADEMY. INCLUDES INSTALLATION AND 3-YEAR IN-COUNTRY WARRANTY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0020_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) \u2014 us. Official USASpending Award API. Shuffle solar dry\u2192engineering_epc CapEx; \u22651/3 U.S.",
    "hunt_cycle1380",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16F0020_1900_SWHARC16D0002_1900 (faac_mexico_hidalgo_firearm_simulator_154k_2016). Signed 2016-06-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0020_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_hidalgo_firearm_simulator_154k_2016 USD 0.154m. Supports faac_mexico_hidalgo_firearm_simulator_154k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 154051.90; date_signed 2016-06-24.",
    investment_type="equipment_supply",
)

# === Cycle 1380 ===
row_doc(
    "bonatti_el_salvador_santa_ana_team_house_658k_2012",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 El Salvador Santa Ana team house",
    "El Salvador",
    "25 Sep 2012: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for TEAM HOUSE SANTA ANA, EL SALVADOR; obligated USD 658414.77. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "658414.77", "2012-09-25", "2012", "", "",
    "TEAM HOUSE SANTA ANA, EL SALVADOR, El Salvador (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_el_salvador_santa_ana_team_house_658k_2012",
    "TEAM HOUSE SANTA ANA, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127811D0044_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1380",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0010_9700_W9127811D0044_9700 (bonatti_el_salvador_santa_ana_team_house_658k_2012). Signed 2012-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127811D0044_9700/.",
    "USASpending: bonatti_el_salvador_santa_ana_team_house_658k_2012 USD 0.658m. Supports bonatti_el_salvador_santa_ana_team_house_658k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 658414.77; date_signed 2012-09-25.",
    investment_type="epc",
)

# === Cycle 1380 ===
row_doc(
    "bonatti_honduras_soto_cano_guard_house_towers_berm_487k_2011",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 Honduras Soto Cano guard house, towers and berm",
    "Honduras",
    "28 Sep 2011: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for CONSTRUCTION OF GUARD HOSUE, TOWERS AND BERM, JTFB SOTO CANO, HONDURAS; obligated USD 486943.99. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "486943.99", "2011-09-28", "2011", "", "",
    "TAS::21 2020::TAS CONSTRUCTION OF GUARD HOSUE, TOWERS AND BERM, JTFB SOTO CANO, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_honduras_soto_cano_guard_house_towers_berm_487k_2011",
    "TAS::21 2020::TAS CONSTRUCTION OF GUARD HOSUE, TOWERS AND BERM, JTFB SOTO CANO, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127811D0044_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle building_materials CapEx (named Soto Cano Honduras; PoP Guatemala overridden by description).",
    "hunt_cycle1380",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0007_9700_W9127811D0044_9700 (bonatti_honduras_soto_cano_guard_house_towers_berm_487k_2011). Signed 2011-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127811D0044_9700/.",
    "USASpending: bonatti_honduras_soto_cano_guard_house_towers_berm_487k_2011 USD 0.487m. Supports bonatti_honduras_soto_cano_guard_house_towers_berm_487k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 486943.99; date_signed 2011-09-28.",
    investment_type="epc",
)

# === Cycle 1380 ===
row_doc(
    "bonatti_honduras_fence_line_reinforcement_327k_2014",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 Honduras fence line reinforcement",
    "Honduras",
    "24 Sep 2014: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for FENCE LINE REINFORCEMENT; obligated USD 326718.48. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "326718.48", "2014-09-24", "2014", "", "",
    "FENCE LINE REINFORCEMENT, Honduras (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_honduras_fence_line_reinforcement_327k_2014",
    "FENCE LINE REINFORCEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127813D0017_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1380",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0004_9700_W9127813D0017_9700 (bonatti_honduras_fence_line_reinforcement_327k_2014). Signed 2014-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127813D0017_9700/.",
    "USASpending: bonatti_honduras_fence_line_reinforcement_327k_2014 USD 0.327m. Supports bonatti_honduras_fence_line_reinforcement_327k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 326718.48; date_signed 2014-09-24.",
    investment_type="epc",
)

# === Cycle 1381 ===
row_doc(
    "astrophysics_peru_lima_mail_xray_69k_2010",
    "infrastructure", "engineering_epc", "us",
    "Astrophysics \u2014 Peru Lima NAS mail parcel x-ray machines",
    "Peru",
    "21 May 2010: Department of State awards contract to ASTROPHYSICS INC for SUPPLY, TRANSPORT AND DELIVER 2 EACH, MAIL PARCEL X-RAY MACHINES ... FOR THE NAS OFFICE IN LIMA, PERU; obligated USD 69330.78. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "69330.78", "2010-05-21", "2010", "", "",
    "CONTRACTOR IS REQURIED TO SUPPLY, TRANSPORT AND DELIVER 2 EACH, MAIL PARCEL X-RAY MACHINES, Peru (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_astrophysics_peru_lima_mail_xray_69k_2010",
    "CONTRACTOR IS REQURIED TO SUPPLY, TRANSPORT AND DELIVER 2 EACH, MAIL PARCEL X-RAY MACHINES, PLUS EXIT AND ENTRANCE ROLLER TABLES, ON-SITE OPERATOR USEAGE TRAINING AND 2-YEARS OF WARRANTY AND MAINTENANCE FOR THE NAS OFFICE IN LIMA, PERU.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC10F0060_1900_GS07F0182T_4730/",
    "Actor: ASTROPHYSICS INC (U.S.) \u2014 us. Official USASpending Award API. Shuffle niobium dry\u2192engineering_epc CapEx; \u22651/3 U.S.",
    "hunt_cycle1381",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC10F0060_1900_GS07F0182T_4730 (astrophysics_peru_lima_mail_xray_69k_2010). Signed 2010-05-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC10F0060_1900_GS07F0182T_4730/.",
    "USASpending: astrophysics_peru_lima_mail_xray_69k_2010 USD 0.069m. Supports astrophysics_peru_lima_mail_xray_69k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69330.78; date_signed 2010-05-21.",
    investment_type="equipment_supply",
)

# === Cycle 1381 ===
row_doc(
    "astrophysics_mexico_xray_baggage_inspection_1573k_2015",
    "infrastructure", "engineering_epc", "us",
    "Astrophysics \u2014 Mexico x-ray baggage inspection system donation",
    "Mexico",
    "19 Jun 2015: Department of State awards contract to ASTROPHYSICS INC for XRAY BAGGAGE INSPECTION SYSTEM TO BE DONATED TO THE GOVERNMENT OF MEXICO; obligated USD 1573039.00. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "1573039.00", "2015-06-19", "2015", "", "",
    "XRAY BAGGAGE INSPECTION SYSTEM TO BE DONATED TO THE GOVERNMENT OF MEXICO, Mexico (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_astrophysics_mexico_xray_baggage_inspection_1573k_2015",
    "XRAY BAGGAGE INSPECTION SYSTEM TO BE DONATED TO THE GOVERNMENT OF MEXICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15F0015_1900_GS07F0182T_4730/",
    "Actor: ASTROPHYSICS INC (U.S.) \u2014 us. Official USASpending Award API. Shuffle port_cranes dry\u2192engineering_epc CapEx; \u22651/3 U.S.",
    "hunt_cycle1381",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC15F0015_1900_GS07F0182T_4730 (astrophysics_mexico_xray_baggage_inspection_1573k_2015). Signed 2015-06-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15F0015_1900_GS07F0182T_4730/.",
    "USASpending: astrophysics_mexico_xray_baggage_inspection_1573k_2015 USD 1.573m. Supports astrophysics_mexico_xray_baggage_inspection_1573k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1573039.00; date_signed 2015-06-19.",
    investment_type="equipment_supply",
)

# === Cycle 1381 ===
row_doc(
    "bonatti_guatemala_champerico_cnt_ops_center_131k_2011",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 Guatemala Champerico CNT ops center design-build",
    "Guatemala",
    "27 Sep 2011: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for DESIGN AND CONSTRUCTION OF CNT OPS CENTER, CHAMPERICO, GUATEMALA; obligated USD 131116.84. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "131116.84", "2011-09-27", "2011", "", "",
    "TAS::21 2020::TAS DESIGN AND CONSTRUCTION OF CNT OPS CENTER, CHAMPERICO, GUATEMALA, Guatemala (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_guatemala_champerico_cnt_ops_center_131k_2011",
    "TAS::21 2020::TAS DESIGN AND CONSTRUCTION OF CNT OPS CENTER, CHAMPERICO, GUATEMALA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127811D0044_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1381",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0004_9700_W9127811D0044_9700 (bonatti_guatemala_champerico_cnt_ops_center_131k_2011). Signed 2011-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127811D0044_9700/.",
    "USASpending: bonatti_guatemala_champerico_cnt_ops_center_131k_2011 USD 0.131m. Supports bonatti_guatemala_champerico_cnt_ops_center_131k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 131116.84; date_signed 2011-09-27.",
    investment_type="epc",
)

# === Cycle 1381 ===
row_doc(
    "bonatti_guatemala_champerico_pier_fuel_105k_2011",
    "infrastructure", "port_ownership", "other",
    "Bonatti Ingenieros \u2014 Guatemala Champerico pier and fuel",
    "Guatemala",
    "28 Sep 2011: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for PIER&FUEL CHAMPERICO, GUATEMALA; obligated USD 105200.32. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "105200.32", "2011-09-28", "2011", "", "",
    "TAS::21 2020::TAS PIER&FUEL CHAMPERICO, GUATEMALA, Guatemala (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_guatemala_champerico_pier_fuel_105k_2011",
    "TAS::21 2020::TAS PIER&FUEL CHAMPERICO, GUATEMALA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127811D0048_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle port_ownership CapEx.",
    "hunt_cycle1381",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127811D0048_9700 (bonatti_guatemala_champerico_pier_fuel_105k_2011). Signed 2011-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127811D0048_9700/.",
    "USASpending: bonatti_guatemala_champerico_pier_fuel_105k_2011 USD 0.105m. Supports bonatti_guatemala_champerico_pier_fuel_105k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 105200.32; date_signed 2011-09-28.",
    investment_type="epc",
)

# === Cycle 1381 ===
row_doc(
    "rogers_panama_metropolitan_park_crane_civil_67k_2020",
    "infrastructure", "port_cranes", "other",
    "Constructora Rogers (CONROSA) \u2014 Panama Metropolitan Park new crane civil works",
    "Panama",
    "17 Mar 2020: Smithsonian awards contract to CONSTRUCTORA ROGERS, S.A. (CONROSA) for CIVIL WORKS FOR NEW CRANE AT METROPOLITAN PARK; obligated USD 67339.33. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "67339.33", "2020-03-17", "2020", "", "",
    "CIVIL WORKS FOR NEW CRANE AT METROPOLITAN PARK., Panama (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_rogers_panama_metropolitan_park_crane_civil_67k_2020",
    "CIVIL WORKS FOR NEW CRANE AT METROPOLITAN PARK.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330220FF0010164_3300_F15CC10192_3300/",
    "Actor: CONSTRUCTORA ROGERS, S.A. (CONROSA) \u2014 other. Official USASpending Award API. Shuffle port_cranes CapEx.",
    "hunt_cycle1381",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330220FF0010164_3300_F15CC10192_3300 (rogers_panama_metropolitan_park_crane_civil_67k_2020). Signed 2020-03-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330220FF0010164_3300_F15CC10192_3300/.",
    "USASpending: rogers_panama_metropolitan_park_crane_civil_67k_2020 USD 0.067m. Supports rogers_panama_metropolitan_park_crane_civil_67k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 67339.33; date_signed 2020-03-17.",
    investment_type="epc",
)

# === Cycle 1382 ===
row_doc(
    "astrophysics_mexico_xis_van_705k_2016",
    "infrastructure", "engineering_epc", "us",
    "Astrophysics \u2014 Mexico XIS van donation",
    "Mexico",
    "15 Apr 2016: Department of State awards contract to ASTROPHYSICS INC for XIS VAN TO BE DONATED TO THE GOVERNMENT OF MEXICO; obligated USD 704650.00. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "704650.00", "2016-04-15", "2016", "", "",
    "XIS VAN TO BE DONATED TO THE GOVERNMENT OF MEXICO, Mexico (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_astrophysics_mexico_xis_van_705k_2016",
    "XIS VAN TO BE DONATED TO THE GOVERNMENT OF MEXICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0007_1900_GS07F0182T_4730/",
    "Actor: ASTROPHYSICS INC (U.S.) \u2014 us. Official USASpending Award API. Shuffle balsa dry\u2192engineering_epc CapEx; \u22651/3 U.S.",
    "hunt_cycle1382",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16F0007_1900_GS07F0182T_4730 (astrophysics_mexico_xis_van_705k_2016). Signed 2016-04-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0007_1900_GS07F0182T_4730/.",
    "USASpending: astrophysics_mexico_xis_van_705k_2016 USD 0.705m. Supports astrophysics_mexico_xis_van_705k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 704650.00; date_signed 2016-04-15.",
    investment_type="equipment_supply",
)

# === Cycle 1382 ===
row_doc(
    "astrophysics_panama_mobile_baggage_scan_155k_2016",
    "infrastructure", "engineering_epc", "us",
    "Astrophysics \u2014 Panama airports mobile baggage scan unit",
    "Panama",
    "22 Nov 2016: Department of State awards contract to ASTROPHYSICS INC for MOBILE BAGGAGE SCAN UNIT FOR PANAMA AIRPORTS (VEHICLE) FOR INL/PANAMA; obligated USD 154551.50. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "154551.50", "2016-11-22", "2016", "", "",
    "DESCRIPTION:  CONTRACT FOR: MOBILE BAGGAGE SCAN UNIT FOR PANAMA AIRPORTS (VEHICLE) FOR INL, Panama (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_astrophysics_panama_mobile_baggage_scan_155k_2016",
    "DESCRIPTION:  CONTRACT FOR: MOBILE BAGGAGE SCAN UNIT FOR PANAMA AIRPORTS (VEHICLE) FOR INL/PANAMA AMOUNT $154,551.50",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SINLEC17M0005_1900_-NONE-_-NONE-/",
    "Actor: ASTROPHYSICS INC (U.S.) \u2014 us. Official USASpending Award API. Shuffle graphite dry\u2192engineering_epc CapEx; \u22651/3 U.S.",
    "hunt_cycle1382",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SINLEC17M0005_1900_-NONE-_-NONE- (astrophysics_panama_mobile_baggage_scan_155k_2016). Signed 2016-11-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SINLEC17M0005_1900_-NONE-_-NONE-/.",
    "USASpending: astrophysics_panama_mobile_baggage_scan_155k_2016 USD 0.155m. Supports astrophysics_panama_mobile_baggage_scan_155k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 154551.50; date_signed 2016-11-22.",
    investment_type="equipment_supply",
)

# === Cycle 1382 ===
row_doc(
    "bonatti_honduras_soto_cano_water_distribution_9002k_2019",
    "resources", "water", "other",
    "Bonatti Ingenieros \u2014 Honduras Soto Cano water distribution system replace",
    "Honduras",
    "27 Sep 2019: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for REPLACE WATER DISTRIBUTION SYSTEM (funding office USA SPT ACT SOTO CANO); obligated USD 9002099.88. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "9002099.88", "2019-09-27", "2019", "", "",
    "REPLACE WATER DISTRIBUTION SYSTEM, Honduras (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_honduras_soto_cano_water_distribution_9002k_2019",
    "REPLACE WATER DISTRIBUTION SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0503_9700_W9127816D0099_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle water CapEx thin top-up path.",
    "hunt_cycle1382",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0503_9700_W9127816D0099_9700 (bonatti_honduras_soto_cano_water_distribution_9002k_2019). Signed 2019-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0503_9700_W9127816D0099_9700/.",
    "USASpending: bonatti_honduras_soto_cano_water_distribution_9002k_2019 USD 9.002m. Supports bonatti_honduras_soto_cano_water_distribution_9002k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9002099.88; date_signed 2019-09-27.",
    investment_type="epc",
)

# === Cycle 1382 ===
row_doc(
    "bonatti_el_salvador_comalapa_post_office_579k_2012",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 El Salvador Comalapa post office",
    "El Salvador",
    "27 Sep 2012: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for POST OFFICE COMALAPA, EL SALVADOR; obligated USD 578889.07. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "578889.07", "2012-09-27", "2012", "", "",
    "POST OFFICE COMALAPA, EL SALVADOR, El Salvador (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_el_salvador_comalapa_post_office_579k_2012",
    "POST OFFICE COMALAPA, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127809D0064_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1382",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0009_9700_W9127809D0064_9700 (bonatti_el_salvador_comalapa_post_office_579k_2012). Signed 2012-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127809D0064_9700/.",
    "USASpending: bonatti_el_salvador_comalapa_post_office_579k_2012 USD 0.579m. Supports bonatti_el_salvador_comalapa_post_office_579k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 578889.07; date_signed 2012-09-27.",
    investment_type="epc",
)

# === Cycle 1382 ===
row_doc(
    "bonatti_belize_joc_water_system_upgrade_14k_2014",
    "resources", "water", "other",
    "Bonatti Ingenieros \u2014 Belize JOC facility water system upgrade",
    "Belize",
    "25 Apr 2014: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for WATER SYSTEM UPGRADE, JOC FACILITY; obligated USD 13630.48. CapEx face = award obligation. Exact site coords not stated \u2014 lat/lon blank.",
    "13630.48", "2014-04-25", "2014", "", "",
    "WATER SYSTEM UPGRADE, JOC FACILITY, Belize (USASpending description; site/city named where present, coords not stated \u2014 lat/lon blank).",
    "usaspending_bonatti_belize_joc_water_system_upgrade_14k_2014",
    "WATER SYSTEM UPGRADE, JOC FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127814P0149_9700_-NONE-_-NONE-/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA \u2014 other. Official USASpending Award API. Shuffle water CapEx.",
    "hunt_cycle1382",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127814P0149_9700_-NONE-_-NONE- (bonatti_belize_joc_water_system_upgrade_14k_2014). Signed 2014-04-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127814P0149_9700_-NONE-_-NONE-/.",
    "USASpending: bonatti_belize_joc_water_system_upgrade_14k_2014 USD 0.014m. Supports bonatti_belize_joc_water_system_upgrade_14k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13630.48; date_signed 2014-04-25.",
    investment_type="epc",
)

def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: r for r in rows}
    for row, _ev, _bib in ITEMS:
        rid = row["id"]
        if rid in by_id: raise SystemExit(f"duplicate id: {rid}")
        rows.append(row); by_id[rid] = row
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
                if s not in (existing.get("supports") or []): existing.setdefault("supports", []).append(s)
        else: bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")


if __name__ == "__main__":
    main()
