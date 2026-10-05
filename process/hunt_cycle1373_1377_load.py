#!/usr/bin/env python3
"""Cycles 1373–1377: USASpending LatAm CapEx (Obera/Virtra/Hunter/Astrophysics/Gemalto/Carolina + Bonatti/Rogers EPC).

Seeds: 20262373–20262377. Thin top-up dry.
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

# === Cycle 1373 ===
row_doc(
    "obera_dominican_republic_safe_boat_1000k_2024",
    "infrastructure", "engineering_epc", "us",
    "Obera — Dominican Republic SOUTHCOM safe boat",
    "Dominican Republic",
    "20 Sep 2024: Department of Defense awards contract to OBERA LLC for SOUTHCOM Dominican Republic safe boat; obligated USD 1000240.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1000240.00", "2024-09-20", "2024", "", "",
    "SOUTHCOM DOMINICAN REPUBLIC SAFE BOAT, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_obera_dominican_republic_safe_boat_1000k_2024",
    "SOUTHCOM DOMINICAN REPUBLIC SAFE BOAT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489024F0162_9700_FA489023D0008_9700/",
    "Actor: OBERA LLC (U.S.) — us. Official USASpending Award API. Shuffle port_cranes dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1373",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489024F0162_9700_FA489023D0008_9700 (obera_dominican_republic_safe_boat_1000k_2024). Signed 2024-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489024F0162_9700_FA489023D0008_9700/.",
    "USASpending: obera_dominican_republic_safe_boat_1000k_2024 USD 1.000m. Supports obera_dominican_republic_safe_boat_1000k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1000240.00; date_signed 2024-09-20.",
    investment_type="equipment_supply",
)

# === Cycle 1373 ===
row_doc(
    "virtra_costa_rica_six_firearms_simulators_790k_2016",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Costa Rica six firearms training simulators",
    "Costa Rica",
    "27 Sep 2016: Department of State awards contract to VIRTRA, INC. for six firearms training simulators, simulated weapons, and related accessories for INL San Jose; obligated USD 790161.32. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "790161.32", "2016-09-27", "2016", "", "",
    "INL SAN JOSE, COSTA RICA: SIX (6) FIREARMS TRAINING SIMULATORS, SIMULATED WEAPONS, AND REL, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_costa_rica_six_firearms_simulators_790k_2016",
    "INL SAN JOSE, COSTA RICA: SIX (6) FIREARMS TRAINING SIMULATORS, SIMULATED WEAPONS, AND RELATED ACCESSORIES. INCLUDES INSTALLATION AND 3-YEAR IN-COUNTRY WARRANTY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0043_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle fission_smr dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1373",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16F0043_1900_SWHARC16D0003_1900 (virtra_costa_rica_six_firearms_simulators_790k_2016). Signed 2016-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0043_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_costa_rica_six_firearms_simulators_790k_2016 USD 0.790m. Supports virtra_costa_rica_six_firearms_simulators_790k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 790161.32; date_signed 2016-09-27.",
    investment_type="equipment_supply",
)

# === Cycle 1373 ===
row_doc(
    "bonatti_guatemala_santa_ana_berlin_cn_barracks_3244k_2012",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — Guatemala Santa Ana de Berlin CN barracks C2 dining vehicle maintenance latrines",
    "Guatemala",
    "29 Sep 2012: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for CN barracks, C2, dining, vehicle maintenance and latrines at Santa Ana de Berlin, Guatemala; obligated USD 3243641.92. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3243641.92", "2012-09-29", "2012", "", "",
    "CN BARRACKS, C2, DINING, VEHICLE MAINTENANCE AND LATRINES AT SANTA ANA DE BERLIN, GUATEMAL, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_guatemala_santa_ana_berlin_cn_barracks_3244k_2012",
    "IGF::OT::IGF CN BARRACKS, C2, DINING, VEHICLE MAINTENANCE AND LATRINES AT SANTA ANA DE BERLIN, GUATEMALA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127811D0044_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1373",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0011_9700_W9127811D0044_9700 (bonatti_guatemala_santa_ana_berlin_cn_barracks_3244k_2012). Signed 2012-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127811D0044_9700/.",
    "USASpending: bonatti_guatemala_santa_ana_berlin_cn_barracks_3244k_2012 USD 3.244m. Supports bonatti_guatemala_santa_ana_berlin_cn_barracks_3244k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3243641.92; date_signed 2012-09-29.",
    investment_type="epc",
)

# === Cycle 1373 ===
row_doc(
    "bonatti_guatemala_cn_ctoc_barracks_latrine_2907k_2014",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — Guatemala CN CTOC barracks and latrine",
    "Guatemala",
    "23 Sep 2014: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA to construct CN CTOC barracks and latrine; obligated USD 2907103.97. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2907103.97", "2014-09-23", "2014", "", "",
    "CONSTRUCT CN CTOC BARRACKS AND LATRINE, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_guatemala_cn_ctoc_barracks_latrine_2907k_2014",
    "IGF::OT::IGF CONSTRUCT CN CTOC BARRACKS AND LATRINE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127813D0017_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1373",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127813D0017_9700 (bonatti_guatemala_cn_ctoc_barracks_latrine_2907k_2014). Signed 2014-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127813D0017_9700/.",
    "USASpending: bonatti_guatemala_cn_ctoc_barracks_latrine_2907k_2014 USD 2.907m. Supports bonatti_guatemala_cn_ctoc_barracks_latrine_2907k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2907103.97; date_signed 2014-09-23.",
    investment_type="epc",
)

# === Cycle 1373 ===
row_doc(
    "rogers_panama_san_lorenzo_canopy_crane_2298k_2025",
    "infrastructure", "port_cranes", "other",
    "Constructora Rogers (CONROSA) — Panama San Lorenzo Sherman canopy crane replace",
    "Panama",
    "23 Sep 2025: Smithsonian awards contract to CONSTRUCTORA ROGERS, S.A. (CONROSA) to replace canopy crane at San Lorenzo (Sherman); obligated USD 2297820.58. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2297820.58", "2025-09-23", "2025", "", "",
    "STRI - REPLACE CANOPY CRANE AT SAN LORENZO (SHERMAN)., Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_rogers_panama_san_lorenzo_canopy_crane_2298k_2025",
    "STRI - REPLACE CANOPY CRANE AT SAN LORENZO (SHERMAN).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330225FF0010444_3300_F15CC10192_3300/",
    "Actor: CONSTRUCTORA ROGERS, S.A. (CONROSA) — other. Official USASpending Award API. Shuffle port_cranes CapEx.",
    "hunt_cycle1373",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330225FF0010444_3300_F15CC10192_3300 (rogers_panama_san_lorenzo_canopy_crane_2298k_2025). Signed 2025-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330225FF0010444_3300_F15CC10192_3300/.",
    "USASpending: rogers_panama_san_lorenzo_canopy_crane_2298k_2025 USD 2.298m. Supports rogers_panama_san_lorenzo_canopy_crane_2298k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2297820.58; date_signed 2025-09-23.",
    investment_type="equipment_supply",
)

# === Cycle 1374 ===
row_doc(
    "obera_guatemala_weapons_proficiency_equipment_467k_2024",
    "infrastructure", "engineering_epc", "us",
    "Obera — Guatemala SOUTHCOM weapons proficiency and equipment",
    "Guatemala",
    "10 Sep 2024: Department of Defense awards contract to OBERA LLC for FY23 Tranche 2 SOUTHCOM Guatemala weapons proficiency and equipment; obligated USD 467290.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "467290.00", "2024-09-10", "2024", "", "",
    "FISCAL YEAR 23 TRANCHE 2 U.S. SOUTHERN COMMAND GUATEMALA WEAPONS PROFICIENCY AND EQUIPMENT, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_obera_guatemala_weapons_proficiency_equipment_467k_2024",
    "FISCAL YEAR 23 TRANCHE 2 U.S. SOUTHERN COMMAND GUATEMALA WEAPONS PROFICIENCY AND EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489024F0123_9700_FA489023D0008_9700/",
    "Actor: OBERA LLC (U.S.) — us. Official USASpending Award API. Shuffle fission_smr dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1374",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489024F0123_9700_FA489023D0008_9700 (obera_guatemala_weapons_proficiency_equipment_467k_2024). Signed 2024-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489024F0123_9700_FA489023D0008_9700/.",
    "USASpending: obera_guatemala_weapons_proficiency_equipment_467k_2024 USD 0.467m. Supports obera_guatemala_weapons_proficiency_equipment_467k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 467290.00; date_signed 2024-09-10.",
    investment_type="equipment_supply",
)

# === Cycle 1374 ===
row_doc(
    "astrophysics_el_salvador_xray_units_205k_2011",
    "infrastructure", "engineering_epc", "us",
    "Astrophysics — El Salvador NAS seven x-ray units",
    "El Salvador",
    "29 Jul 2011: Department of State awards contract to ASTROPHYSICS INC for seven x-ray units for NAS El Salvador to be donated to the Government of El Salvador; obligated USD 205382.52. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "205382.52", "2011-07-29", "2011", "", "",
    "SEVEN X-RAY UNITS FOR NAS EL SALVADOR, ITEMS WILL BE DONATED TO THE GOVERNMENT OF EL SALVA, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_astrophysics_el_salvador_xray_units_205k_2011",
    "SEVEN X-RAY UNITS FOR NAS EL SALVADOR, ITEMS WILL BE DONATED TO THE GOVERNMENT OF EL SALVADOR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11F0076_1900_GS07F0182T_4730/",
    "Actor: ASTROPHYSICS INC (U.S.) — us. Official USASpending Award API. Shuffle lithium dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1374",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC11F0076_1900_GS07F0182T_4730 (astrophysics_el_salvador_xray_units_205k_2011). Signed 2011-07-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11F0076_1900_GS07F0182T_4730/.",
    "USASpending: astrophysics_el_salvador_xray_units_205k_2011 USD 0.205m. Supports astrophysics_el_salvador_xray_units_205k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 205382.52; date_signed 2011-07-29.",
    investment_type="equipment_supply",
)

# === Cycle 1374 ===
row_doc(
    "bonatti_honduras_soto_cano_barracks_roadway_fence_1697k_2011",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — Honduras Soto Cano barracks roadway and fence",
    "Honduras",
    "28 Sep 2011: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for construction of barracks, roadway and fence, JTFB Soto Cano, Honduras; obligated USD 1697017.66. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1697017.66", "2011-09-28", "2011", "", "",
    "CONSTRUCTION OF BARACKS, ROADWAY AND FENCE, JTFB SOTO CANO, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_honduras_soto_cano_barracks_roadway_fence_1697k_2011",
    "TAS::21 2020::TAS CONSTRUCTION OF BARACKS, ROADWAY AND FENCE, JTFB SOTO CANO, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127811D0044_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx. Asset country Honduras per description.",
    "hunt_cycle1374",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0006_9700_W9127811D0044_9700 (bonatti_honduras_soto_cano_barracks_roadway_fence_1697k_2011). Signed 2011-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127811D0044_9700/.",
    "USASpending: bonatti_honduras_soto_cano_barracks_roadway_fence_1697k_2011 USD 1.697m. Supports bonatti_honduras_soto_cano_barracks_roadway_fence_1697k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1697017.66; date_signed 2011-09-28.",
    investment_type="epc",
)

# === Cycle 1374 ===
row_doc(
    "bonatti_belize_hunting_caye_cn_pier_fueling_1501k_2011",
    "infrastructure", "port_ownership", "other",
    "Bonatti Ingenieros — Belize Hunting Caye CN pier and fueling",
    "Belize",
    "26 Sep 2011: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for construction of CN pier and fueling Hunting Caye, Belize; obligated USD 1500880.35. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1500880.35", "2011-09-26", "2011", "", "",
    "CONSTRUCTION OF CN PIER AND FUELING HUNTING CAYE, BELIZE, Belize (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_belize_hunting_caye_cn_pier_fueling_1501k_2011",
    "TAS::21 2020::TAS CONSTRUCTION OF CN PIER AND FUELING HUNTING CAYE, BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127811D0044_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle port_ownership/pier CapEx.",
    "hunt_cycle1374",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127811D0044_9700 (bonatti_belize_hunting_caye_cn_pier_fueling_1501k_2011). Signed 2011-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127811D0044_9700/.",
    "USASpending: bonatti_belize_hunting_caye_cn_pier_fueling_1501k_2011 USD 1.501m. Supports bonatti_belize_hunting_caye_cn_pier_fueling_1501k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1500880.35; date_signed 2011-09-26.",
    investment_type="epc",
)

# === Cycle 1374 ===
row_doc(
    "bonatti_belize_san_pedro_cn_pier_fueling_1334k_2011",
    "infrastructure", "port_ownership", "other",
    "Bonatti Ingenieros — Belize San Pedro CN pier and fueling",
    "Belize",
    "26 Sep 2011: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for construction of CN pier and fueling, San Pedro, Belize; obligated USD 1333582.71. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1333582.71", "2011-09-26", "2011", "", "",
    "CONSTRUCTION OF CN PIER AND FUELING, SAN PEDRO, BELIZE, Belize (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_belize_san_pedro_cn_pier_fueling_1334k_2011",
    "TAS::21 2020::TAS CONSTRUCTION OF CN PIER AND FUELING, SAN PEDRO, BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127811D0044_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle port_cranes dry→port_ownership/pier CapEx.",
    "hunt_cycle1374",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127811D0044_9700 (bonatti_belize_san_pedro_cn_pier_fueling_1334k_2011). Signed 2011-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127811D0044_9700/.",
    "USASpending: bonatti_belize_san_pedro_cn_pier_fueling_1334k_2011 USD 1.334m. Supports bonatti_belize_san_pedro_cn_pier_fueling_1334k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1333582.71; date_signed 2011-09-26.",
    investment_type="epc",
)

# === Cycle 1375 ===
row_doc(
    "hunter_haiti_usaid_warehouse_safe_haven_183k_2012",
    "infrastructure", "building_materials", "us",
    "Hunter Buildings International — Haiti USAID warehouse safe haven",
    "Haiti",
    "05 Dec 2012: USAID awards contract to HUNTER BUILDINGS INTERNATIONAL, LLC for safe heaven for USAID warehouse; obligated USD 183100.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "183100.00", "2012-12-05", "2012", "", "",
    "SAFE HEAVEN FOR USAID WAREHOUSE, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hunter_haiti_usaid_warehouse_safe_haven_183k_2012",
    "SAFE HEAVEN FOR USAID WAREHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1300002_7200_-NONE-_-NONE-/",
    "Actor: HUNTER BUILDINGS INTERNATIONAL, LLC (U.S.) — us. Official USASpending Award API. Shuffle graphite dry→building_materials CapEx; ≥1/3 U.S.",
    "hunt_cycle1375",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521C1300002_7200_-NONE-_-NONE- (hunter_haiti_usaid_warehouse_safe_haven_183k_2012). Signed 2012-12-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1300002_7200_-NONE-_-NONE-/.",
    "USASpending: hunter_haiti_usaid_warehouse_safe_haven_183k_2012 USD 0.183m. Supports hunter_haiti_usaid_warehouse_safe_haven_183k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 183100.00; date_signed 2012-12-05.",
    investment_type="epc",
)

# === Cycle 1375 ===
row_doc(
    "virtra_mexico_semar_firearms_simulator_176k_2017",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico SEMAR fixed firearms training simulator",
    "Mexico",
    "07 Jul 2017: Department of State awards contract to VIRTRA, INC. for fixed firearms training simulator system for SEMAR (Mexican Navy); obligated USD 175755.08. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "175755.08", "2017-07-07", "2017", "", "",
    "INL MEXICO - FIXED FIREARMS TRAINING SIMULATOR SYSTEM FOR SEMAR (MEXICAN NAVY). INCLUDES R, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_semar_firearms_simulator_176k_2017",
    "INL MEXICO - FIXED FIREARMS TRAINING SIMULATOR SYSTEM FOR SEMAR (MEXICAN NAVY). INCLUDES RECOIL KITS, RECHARGEABLE BATTERIES, AND INSTALLATION.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0023_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle wind dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1375",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC17F0023_1900_SWHARC16D0003_1900 (virtra_mexico_semar_firearms_simulator_176k_2017). Signed 2017-07-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0023_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_semar_firearms_simulator_176k_2017 USD 0.176m. Supports virtra_mexico_semar_firearms_simulator_176k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 175755.08; date_signed 2017-07-07.",
    investment_type="equipment_supply",
)

# === Cycle 1375 ===
row_doc(
    "bonatti_honduras_soto_cano_fire_trainer_1214k_2024",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — Honduras Soto Cano structural fire trainer design-build",
    "Honduras",
    "25 Sep 2024: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA to design and build structural fire trainer for Soto Cano Air Base; obligated USD 1214261.01. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1214261.01", "2024-09-25", "2024", "", "",
    "DESIGN AND BUILD STRUCTURAL FIRE TRAINER FOR SOTO CANO AIR BASE, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_honduras_soto_cano_fire_trainer_1214k_2024",
    "DESIGN AND BUILD STRUCTURAL FIRE TRAINER FOR SOTO CANO AIR BASE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0330_9700_W9127823D0072_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1375",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0330_9700_W9127823D0072_9700 (bonatti_honduras_soto_cano_fire_trainer_1214k_2024). Signed 2024-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0330_9700_W9127823D0072_9700/.",
    "USASpending: bonatti_honduras_soto_cano_fire_trainer_1214k_2024 USD 1.214m. Supports bonatti_honduras_soto_cano_fire_trainer_1214k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1214261.01; date_signed 2024-09-25.",
    investment_type="epc",
)

# === Cycle 1375 ===
row_doc(
    "bonatti_el_salvador_tepetitan_schools_862k_2012",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — El Salvador Tepetitan schools",
    "El Salvador",
    "30 Sep 2012: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for Tepetitan schools in El Salvador; obligated USD 861742.47. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "861742.47", "2012-09-30", "2012", "", "",
    "TEPETITAN SCHOOLS IN EL SALVADOR, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_el_salvador_tepetitan_schools_862k_2012",
    "TEPETITAN SCHOOLS IN EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127809D0064_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1375",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0011_9700_W9127809D0064_9700 (bonatti_el_salvador_tepetitan_schools_862k_2012). Signed 2012-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127809D0064_9700/.",
    "USASpending: bonatti_el_salvador_tepetitan_schools_862k_2012 USD 0.862m. Supports bonatti_el_salvador_tepetitan_schools_862k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 861742.47; date_signed 2012-09-30.",
    investment_type="epc",
)

# === Cycle 1375 ===
row_doc(
    "bonatti_guatemala_conred_hp_expansion_780k_2021",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — Guatemala HAP 37597 CONRED HP expansion",
    "Guatemala",
    "29 Sep 2021: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for HAP #37597 CONRED HP expansion; obligated USD 779732.59. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "779732.59", "2021-09-29", "2021", "", "",
    "HAP #37597 CONRED HP EXPANSION, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_guatemala_conred_hp_expansion_780k_2021",
    "HAP #37597 CONRED HP EXPANSION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0465_9700_W9127821D0076_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1375",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0465_9700_W9127821D0076_9700 (bonatti_guatemala_conred_hp_expansion_780k_2021). Signed 2021-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0465_9700_W9127821D0076_9700/.",
    "USASpending: bonatti_guatemala_conred_hp_expansion_780k_2021 USD 0.780m. Supports bonatti_guatemala_conred_hp_expansion_780k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 779732.59; date_signed 2021-09-29.",
    investment_type="epc",
)

# === Cycle 1376 ===
row_doc(
    "virtra_mexico_gendarmeria_firearms_simulators_159k_2017",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico Policia Federal Gendarmeria firearms training simulators",
    "Mexico",
    "28 Sep 2017: Department of State awards contract to VIRTRA, INC. for firearms training simulator systems for Policia Federal Gendarmeria; obligated USD 158519.11. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "158519.11", "2017-09-28", "2017", "", "",
    "INL MEXICO - FIREARMS TRAINING SIMULATOR SYSTEMS FOR POLICIA FEDERAL - GENDARMERIA. INCLUD, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_gendarmeria_firearms_simulators_159k_2017",
    "INL MEXICO - FIREARMS TRAINING SIMULATOR SYSTEMS FOR POLICIA FEDERAL - GENDARMERIA. INCLUDES RECOIL KITS, RECHARGEABLE BATTERIES, AND INSTALLATION.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0036_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle balsa dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1376",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC17F0036_1900_SWHARC16D0003_1900 (virtra_mexico_gendarmeria_firearms_simulators_159k_2017). Signed 2017-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0036_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_gendarmeria_firearms_simulators_159k_2017 USD 0.159m. Supports virtra_mexico_gendarmeria_firearms_simulators_159k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 158519.11; date_signed 2017-09-28.",
    investment_type="equipment_supply",
)

# === Cycle 1376 ===
row_doc(
    "gemalto_guatemala_fingerprint_devices_install_141k_2014",
    "infrastructure", "engineering_epc", "us",
    "Gemalto Cogent — Guatemala fingerprint devices equipment and installation",
    "Guatemala",
    "24 Sep 2014: Department of State awards contract to GEMALTO COGENT, INC. for equipment, installation and finger print devices INL Guatemala; obligated USD 140953.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "140953.00", "2014-09-24", "2014", "", "",
    "AWARD FOR EQUIPMENT, INSTALLATION AND FINGER PRINT DEVICES INL GUATEMALA., Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_gemalto_guatemala_fingerprint_devices_install_141k_2014",
    "AWARD FOR EQUIPMENT, INSTALLATION AND FINGER PRINT DEVICES INL GUATEMALA. IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SINLEC14C0019_1900_-NONE-_-NONE-/",
    "Actor: GEMALTO COGENT, INC. (U.S.) — us. Official USASpending Award API. Shuffle lithium dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1376",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SINLEC14C0019_1900_-NONE-_-NONE- (gemalto_guatemala_fingerprint_devices_install_141k_2014). Signed 2014-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SINLEC14C0019_1900_-NONE-_-NONE-/.",
    "USASpending: gemalto_guatemala_fingerprint_devices_install_141k_2014 USD 0.141m. Supports gemalto_guatemala_fingerprint_devices_install_141k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 140953.00; date_signed 2014-09-24.",
    investment_type="equipment_supply",
)

# === Cycle 1376 ===
row_doc(
    "bonatti_honduras_j6_warehouse_facility_756k_2020",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — Honduras J6 warehouse facility design-build",
    "Honduras",
    "27 Sep 2020: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for D/B J6 warehouse facility base bid; obligated USD 756015.28. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "756015.28", "2020-09-27", "2020", "", "",
    "D/B J6 WAREHOUSE FACILITY- BASE BID, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_honduras_j6_warehouse_facility_756k_2020",
    "D/B J6 WAREHOUSE FACILITY- BASE BID",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0467_9700_W9127816D0099_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1376",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127820F0467_9700_W9127816D0099_9700 (bonatti_honduras_j6_warehouse_facility_756k_2020). Signed 2020-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0467_9700_W9127816D0099_9700/.",
    "USASpending: bonatti_honduras_j6_warehouse_facility_756k_2020 USD 0.756m. Supports bonatti_honduras_j6_warehouse_facility_756k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 756015.28; date_signed 2020-09-27.",
    investment_type="epc",
)

# === Cycle 1376 ===
row_doc(
    "bonatti_el_salvador_hap_37867_zacatecoluca_699k_2021",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — El Salvador HAP 37867 Zacatecoluca design-build",
    "El Salvador",
    "24 Sep 2021: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for D/B HAP 37867, Zacatecoluca, El Salvador; obligated USD 698506.57. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "698506.57", "2021-09-24", "2021", "", "",
    "D/B HAP 37867, ZACATECOLUCA, EL SALVADOR, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_el_salvador_hap_37867_zacatecoluca_699k_2021",
    "D/B HAP 37867, ZACATECOLUCA, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0398_9700_W9127821D0076_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1376",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0398_9700_W9127821D0076_9700 (bonatti_el_salvador_hap_37867_zacatecoluca_699k_2021). Signed 2021-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0398_9700_W9127821D0076_9700/.",
    "USASpending: bonatti_el_salvador_hap_37867_zacatecoluca_699k_2021 USD 0.699m. Supports bonatti_el_salvador_hap_37867_zacatecoluca_699k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 698506.57; date_signed 2021-09-24.",
    investment_type="epc",
)

# === Cycle 1376 ===
row_doc(
    "bonatti_guatemala_sofa_maintenance_facility_684k_2016",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — Guatemala SOFA construct maintenance facility",
    "Guatemala",
    "28 Sep 2016: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for SOFA agreement construct maintenance facility; obligated USD 684482.19. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "684482.19", "2016-09-28", "2016", "", "",
    "SOFA AGREEMENT CONSTRUCT MAINTENANCE FACILILTY, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_guatemala_sofa_maintenance_facility_684k_2016",
    "IGF::OT::IGF SOFA AGREEMENT CONSTRUCT MAINTENANCE FACILILTY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127816D0099_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1376",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127816D0099_9700 (bonatti_guatemala_sofa_maintenance_facility_684k_2016). Signed 2016-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127816D0099_9700/.",
    "USASpending: bonatti_guatemala_sofa_maintenance_facility_684k_2016 USD 0.684m. Supports bonatti_guatemala_sofa_maintenance_facility_684k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 684482.19; date_signed 2016-09-28.",
    investment_type="epc",
)

# === Cycle 1377 ===
row_doc(
    "carolina_peru_firefighting_equipment_117k_2020",
    "infrastructure", "engineering_epc", "us",
    "Carolina Linkages — Peru firefighting equipment for disaster preparation",
    "Peru",
    "23 Sep 2020: Department of Defense awards contract to CAROLINA LINKAGES, INC. for firefighting equipments focused on disaster preparation; obligated USD 117108.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "117108.00", "2020-09-23", "2020", "", "",
    "FIREFIGHTING EQUIPMENTS,THIS PROJECTINCREASED FOCUS ON DISASTER PREPARATION AND BUILDING T, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_carolina_peru_firefighting_equipment_117k_2020",
    "FIREFIGHTING EQUIPMENTS,THIS PROJECTINCREASED FOCUS ON DISASTER PREPARATION AND BUILDING THE CAPACITY OF FIRE DEPARTMENTS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL20F0027_9700_W912CL17D0101_9700/",
    "Actor: CAROLINA LINKAGES, INC. (U.S.) — us. Official USASpending Award API. Shuffle balsa dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1377",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL20F0027_9700_W912CL17D0101_9700 (carolina_peru_firefighting_equipment_117k_2020). Signed 2020-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL20F0027_9700_W912CL17D0101_9700/.",
    "USASpending: carolina_peru_firefighting_equipment_117k_2020 USD 0.117m. Supports carolina_peru_firefighting_equipment_117k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 117108.00; date_signed 2020-09-23.",
    investment_type="equipment_supply",
)

# === Cycle 1377 ===
row_doc(
    "gemalto_el_salvador_pnc_biometric_scanner_57k_2016",
    "infrastructure", "engineering_epc", "us",
    "Gemalto Cogent — El Salvador PNC biometric scanner",
    "El Salvador",
    "07 Mar 2016: Department of State awards contract to GEMALTO COGENT, INC. for INL biometric scanner for PNC; obligated USD 57074.40. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "57074.40", "2016-03-07", "2016", "", "",
    "INL-BIOMETRIC SCANNER FOR PNC, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_gemalto_el_salvador_pnc_biometric_scanner_57k_2016",
    "INL-BIOMETRIC SCANNER FOR PNC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60016M0453_1900_-NONE-_-NONE-/",
    "Actor: GEMALTO COGENT, INC. (U.S.) — us. Official USASpending Award API. Shuffle bridges_roads dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1377",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60016M0453_1900_-NONE-_-NONE- (gemalto_el_salvador_pnc_biometric_scanner_57k_2016). Signed 2016-03-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60016M0453_1900_-NONE-_-NONE-/.",
    "USASpending: gemalto_el_salvador_pnc_biometric_scanner_57k_2016 USD 0.057m. Supports gemalto_el_salvador_pnc_biometric_scanner_57k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 57074.40; date_signed 2016-03-07.",
    investment_type="equipment_supply",
)

# === Cycle 1377 ===
row_doc(
    "bonatti_guatemala_tecun_uman_vehicle_judicial_683k_2011",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — Guatemala Tecun Uman vehicle maintenance and judicial buildings",
    "Guatemala",
    "28 Sep 2011: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for construction of vehicle maintenance and judicial buildings, Tecun Uman, Guatemala; obligated USD 683407.19. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "683407.19", "2011-09-28", "2011", "", "",
    "CONSTRUCTION OF VEHICLE MAINTENANCE&JUDICIAL BUILDINGS, TECUN UMAN, GUATEMALA, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_guatemala_tecun_uman_vehicle_judicial_683k_2011",
    "TAS::21 2020:TAS  CONSTRUCTION OF VEHICLE MAINTENANCE&JUDICIAL BUILDINGS, TECUN UMAN, GUATEMALA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127811D0044_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1377",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0005_9700_W9127811D0044_9700 (bonatti_guatemala_tecun_uman_vehicle_judicial_683k_2011). Signed 2011-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127811D0044_9700/.",
    "USASpending: bonatti_guatemala_tecun_uman_vehicle_judicial_683k_2011 USD 0.683m. Supports bonatti_guatemala_tecun_uman_vehicle_judicial_683k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 683407.19; date_signed 2011-09-28.",
    investment_type="epc",
)

# === Cycle 1377 ===
row_doc(
    "bonatti_guatemala_san_jose_boat_maintenance_facility_665k_2022",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — Guatemala San Jose boat maintenance facility design-build",
    "Guatemala",
    "30 Sep 2022: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for D/B boat maintenance facility San Jose, Guatemala; obligated USD 665214.72. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "665214.72", "2022-09-30", "2022", "", "",
    "D/B BOAT MAINTENANCE FACILITY SAN JOSE, GUATEMALA, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_guatemala_san_jose_boat_maintenance_facility_665k_2022",
    "D/B BOAT MAINTENANCE FACILITY SAN JOSE, GUATEMALA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0455_9700_W9127821D0076_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1377",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0455_9700_W9127821D0076_9700 (bonatti_guatemala_san_jose_boat_maintenance_facility_665k_2022). Signed 2022-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0455_9700_W9127821D0076_9700/.",
    "USASpending: bonatti_guatemala_san_jose_boat_maintenance_facility_665k_2022 USD 0.665m. Supports bonatti_guatemala_san_jose_boat_maintenance_facility_665k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 665214.72; date_signed 2022-09-30.",
    investment_type="epc",
)

# === Cycle 1377 ===
row_doc(
    "bonatti_el_salvador_nejapa_eoc_646k_2010",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — El Salvador Nejapa HAP 7708 EOC design-build",
    "El Salvador",
    "30 Sep 2010: Department of Defense awards contract to BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA for D/B HAP 7708 EOC, Nejapa, El Salvador; obligated USD 645809.93. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "645809.93", "2010-09-30", "2010", "", "",
    "D/B HAP 7708 EOC, NEJAPA, EL SALVADOR, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bonatti_el_salvador_nejapa_eoc_646k_2010",
    "D/B HAP 7708 EOC, NEJAPA, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127809D0064_9700/",
    "Actor: BONATTI INGENIEROS Y ARQUITECTOS SOCIEDAD ANONIMA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1377",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0006_9700_W9127809D0064_9700 (bonatti_el_salvador_nejapa_eoc_646k_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127809D0064_9700/.",
    "USASpending: bonatti_el_salvador_nejapa_eoc_646k_2010 USD 0.646m. Supports bonatti_el_salvador_nejapa_eoc_646k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 645809.93; date_signed 2010-09-30.",
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
