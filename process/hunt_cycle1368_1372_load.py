#!/usr/bin/env python3
"""Cycles 1368–1372: USASpending LatAm CapEx (Advanced C4/Gemalto/Virtra/FAAC/Terrestris/Power Engineers + Sabillon/Andrade/Rogers/SEOBRA/QA/Vinpar/Proyectos).

Seeds: 20262368–20262372. Thin top-up dry.
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

# === Cycle 1368 ===
row_doc(
    "advanced_c4_haiti_police_emergency_call_center_965k_2015",
    "infrastructure", "engineering_epc", "us",
    "Advanced C4 Solutions — Haiti National Police emergency call center upgrade",
    "Haiti",
    "06 Apr 2015: Department of State awards contract to ADVANCED C4 SOLUTIONS INC to upgrade Haiti National Police emergency call center; obligated USD 965212.68. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "965212.68", "2015-04-06", "2015", "", "",
    "UPGRADE OF HAITI NATIONAL POLICE EMERGENCY CALL CENTER, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_advanced_c4_haiti_police_emergency_call_center_965k_2015",
    "UPGRADE OF HAITI NATIONAL POLICE EMERGENCY CALL CENTER IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15F0006_1900_GS06F0841Z_4732/",
    "Actor: ADVANCED C4 SOLUTIONS INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1368",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC15F0006_1900_GS06F0841Z_4732 (advanced_c4_haiti_police_emergency_call_center_965k_2015). Signed 2015-04-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15F0006_1900_GS06F0841Z_4732/.",
    "USASpending: advanced_c4_haiti_police_emergency_call_center_965k_2015 USD 0.965m. Supports advanced_c4_haiti_police_emergency_call_center_965k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 965212.68; date_signed 2015-04-06.",
    investment_type="equipment_supply",
)

# === Cycle 1368 ===
row_doc(
    "gemalto_haiti_afis_system_upgrade_636k_2014",
    "infrastructure", "engineering_epc", "us",
    "Gemalto Cogent — Haiti National Police AFIS system upgrade Port-au-Prince",
    "Haiti",
    "23 Sep 2014: Department of State awards contract to GEMALTO COGENT, INC. to upgrade the AFIS system for the Haitian National Police database in Port-au-Prince; obligated USD 635708.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "635708.00", "2014-09-23", "2014", "", "",
    "THIS IS TO UPRGADE THE AFIS SYSTEM FOR THE HAITIAN NATIONAL POLICE DATABASE IN PORT-AU-PRI, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_gemalto_haiti_afis_system_upgrade_636k_2014",
    "THIS IS TO UPRGADE THE AFIS SYSTEM FOR THE HAITIAN NATIONAL POLICE DATABASE IN PORT-AU-PRINCE HAITI. IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC14M0038_1900_-NONE-_-NONE-/",
    "Actor: GEMALTO COGENT, INC. (U.S.) — us. Official USASpending Award API. Shuffle rail dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1368",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC14M0038_1900_-NONE-_-NONE- (gemalto_haiti_afis_system_upgrade_636k_2014). Signed 2014-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC14M0038_1900_-NONE-_-NONE-/.",
    "USASpending: gemalto_haiti_afis_system_upgrade_636k_2014 USD 0.636m. Supports gemalto_haiti_afis_system_upgrade_636k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 635708.00; date_signed 2014-09-23.",
    investment_type="equipment_supply",
)

# === Cycle 1368 ===
row_doc(
    "sabillon_guatemala_building_materials_296k_2022",
    "infrastructure", "building_materials", "other",
    "Constructora Sabillon — Guatemala building materials",
    "Guatemala",
    "25 Mar 2022: Department of Defense awards contract to CONSTRUCTORA SABILLON for building materials; obligated USD 296342.77. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "296342.77", "2022-03-25", "2022", "", "",
    "BUILDING MATERIALS, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_sabillon_guatemala_building_materials_296k_2022",
    "BUILDING MATERIALS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL22P0007_9700_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA SABILLON — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1368",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL22P0007_9700_-NONE-_-NONE- (sabillon_guatemala_building_materials_296k_2022). Signed 2022-03-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL22P0007_9700_-NONE-_-NONE-/.",
    "USASpending: sabillon_guatemala_building_materials_296k_2022 USD 0.296m. Supports sabillon_guatemala_building_materials_296k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 296342.77; date_signed 2022-03-25.",
    investment_type="epc",
)

# === Cycle 1368 ===
row_doc(
    "andrade_ecuador_quito_ha_construction_services_295k_2024",
    "infrastructure", "building_materials", "other",
    "Constructora Andrade Asociados — Ecuador Quito HA construction services",
    "Ecuador",
    "03 Dec 2024: Department of State awards contract to CONSTRUCTORA ANDRADE ASOCIADOS S.C.C for construction services in support of humanitarian assistance, U.S. Embassy Quito; obligated USD 295252.87. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "295252.87", "2024-12-03", "2024", "", "",
    "U.S. EMBASSY QUITO, ECUADOR. CONSTRUCTION SERVICES IN SUPPORT OF  HUMANITARIAN ASSISTANCE., Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_andrade_ecuador_quito_ha_construction_services_295k_2024",
    "U.S. EMBASSY QUITO, ECUADOR. CONSTRUCTION SERVICES IN SUPPORT OF  HUMANITARIAN ASSISTANCE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025C0010_1900_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA ANDRADE ASOCIADOS S.C.C — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1368",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5025C0010_1900_-NONE-_-NONE- (andrade_ecuador_quito_ha_construction_services_295k_2024). Signed 2024-12-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025C0010_1900_-NONE-_-NONE-/.",
    "USASpending: andrade_ecuador_quito_ha_construction_services_295k_2024 USD 0.295m. Supports andrade_ecuador_quito_ha_construction_services_295k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 295252.87; date_signed 2024-12-03.",
    investment_type="epc",
)

# === Cycle 1368 ===
row_doc(
    "rogers_panama_bocas_fence_gate_security_230k_2017",
    "infrastructure", "building_materials", "other",
    "Constructora Rogers (CONROSA) — Panama Bocas STRI physical and electronic security fence and gate",
    "Panama",
    "07 Sep 2017: Smithsonian awards contract to CONSTRUCTORA ROGERS, S.A. (CONROSA) to upgrade Bocas physical and electronic security (fence and gate); obligated USD 230103.79. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "230103.79", "2017-09-07", "2017", "", "",
    "STRI: UPGRADE BOCAS PHYSICAL AND ELECTRONIC SECURITY (FENCE AND GATE); SF PROJECT NO 17801, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_rogers_panama_bocas_fence_gate_security_230k_2017",
    "STRI: UPGRADE BOCAS PHYSICAL AND ELECTRONIC SECURITY (FENCE AND GATE); SF PROJECT NO 1780101.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F17CW10550_3300_F15CC10192_3300/",
    "Actor: CONSTRUCTORA ROGERS, S.A. (CONROSA) — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1368",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F17CW10550_3300_F15CC10192_3300 (rogers_panama_bocas_fence_gate_security_230k_2017). Signed 2017-09-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F17CW10550_3300_F15CC10192_3300/.",
    "USASpending: rogers_panama_bocas_fence_gate_security_230k_2017 USD 0.230m. Supports rogers_panama_bocas_fence_gate_security_230k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 230103.79; date_signed 2017-09-07.",
    investment_type="epc",
)

# === Cycle 1369 ===
row_doc(
    "virtra_mexico_baja_nayarit_firearms_simulators_251k_2017",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico Baja California and Nayarit firearms training simulators",
    "Mexico",
    "27 Sep 2017: Department of State awards contract to VIRTRA, INC. for firearms training simulator systems for Baja California and Nayarit including recoil kits; obligated USD 250926.83. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "250926.83", "2017-09-27", "2017", "", "",
    "INL MEXICO - FIREARMS TRAINING SIMULATOR SYSTEMS FOR BAJA CALIFORNIA AND NAYARIT. INCLUDES, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_baja_nayarit_firearms_simulators_251k_2017",
    "INL MEXICO - FIREARMS TRAINING SIMULATOR SYSTEMS FOR BAJA CALIFORNIA AND NAYARIT. INCLUDES RECOIL KITS, RECHARGEABLE BATTERIES, AND INSTALLATION.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0033_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle balsa dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1369",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC17F0033_1900_SWHARC16D0003_1900 (virtra_mexico_baja_nayarit_firearms_simulators_251k_2017). Signed 2017-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0033_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_baja_nayarit_firearms_simulators_251k_2017 USD 0.251m. Supports virtra_mexico_baja_nayarit_firearms_simulators_251k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 250926.83; date_signed 2017-09-27.",
    investment_type="equipment_supply",
)

# === Cycle 1369 ===
row_doc(
    "faac_mexico_driving_simulator_install_242k_2017",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico driving simulator system with installation",
    "Mexico",
    "25 Jul 2017: Department of State awards contract to FAAC INCORPORATED for driving simulator system including accessories, training, installation, and in-country maintenance; obligated USD 241591.78. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "241591.78", "2017-07-25", "2017", "", "",
    "INL MEXICO - DRIVING SIMULATOR SYSTEM (INCLUDING ACCESSORIES, TRAINING, INSTALLATION, AND , Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_driving_simulator_install_242k_2017",
    "INL MEXICO - DRIVING SIMULATOR SYSTEM (INCLUDING ACCESSORIES, TRAINING, INSTALLATION, AND IN-COUNTRY MAINTENANCE AND SUPPORT).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0025_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle wind dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1369",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC17F0025_1900_SWHARC16D0002_1900 (faac_mexico_driving_simulator_install_242k_2017). Signed 2017-07-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0025_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_driving_simulator_install_242k_2017 USD 0.242m. Supports faac_mexico_driving_simulator_install_242k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 241591.78; date_signed 2017-07-25.",
    investment_type="equipment_supply",
)

# === Cycle 1369 ===
row_doc(
    "rogers_panama_naos_pier_ebi_cranes_replace_264k_2026",
    "infrastructure", "port_cranes", "other",
    "Constructora Rogers (CONROSA) — Panama Naos Pier EBI cranes replace",
    "Panama",
    "24 Sep 2026: Smithsonian awards contract to CONSTRUCTORA ROGERS, S.A. (CONROSA) for labor, material and transport to replace EBI cranes, Naos Pier, STRI; obligated USD 263820.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "263820.00", "2026-09-24", "2026", "", "",
    "TO SERVICE LABOR, MATERIAL AND TRANSPORT FOR REPLACE EBI CRANES, NAOS PIER, STRI., Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_rogers_panama_naos_pier_ebi_cranes_replace_264k_2026",
    "TO SERVICE LABOR, MATERIAL AND TRANSPORT FOR REPLACE EBI CRANES, NAOS PIER, STRI.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330226FF0010463_3300_33330226DF0010098_3300/",
    "Actor: CONSTRUCTORA ROGERS, S.A. (CONROSA) — other. Official USASpending Award API. Shuffle port_cranes CapEx.",
    "hunt_cycle1369",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330226FF0010463_3300_33330226DF0010098_3300 (rogers_panama_naos_pier_ebi_cranes_replace_264k_2026). Signed 2026-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330226FF0010463_3300_33330226DF0010098_3300/.",
    "USASpending: rogers_panama_naos_pier_ebi_cranes_replace_264k_2026 USD 0.264m. Supports rogers_panama_naos_pier_ebi_cranes_replace_264k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 263820.00; date_signed 2026-09-24.",
    investment_type="equipment_supply",
)

# === Cycle 1369 ===
row_doc(
    "seobra_colombia_tolemaida_concrete_magazine_136k_2011",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Colombia Tolemaida concrete magazine",
    "Colombia",
    "29 Sep 2011: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for construction with incidental design of a concrete magazine, Tolemaida, Colombia; obligated USD 135903.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "135903.00", "2011-09-29", "2011", "", "",
    "CONSTRUCTION WITH INCIDENTAL DESIGN OF A CONCRETE MAGAZINE, TOLEMAIDA, COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_colombia_tolemaida_concrete_magazine_136k_2011",
    "TAS::21 2020::TAS CONSTRUCTION WITH INCIDENTAL DESIGN OF A CONCRETE MAGAZINE, TOLEMAIDA, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127809D0081_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1369",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0005_9700_W9127809D0081_9700 (seobra_colombia_tolemaida_concrete_magazine_136k_2011). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127809D0081_9700/.",
    "USASpending: seobra_colombia_tolemaida_concrete_magazine_136k_2011 USD 0.136m. Supports seobra_colombia_tolemaida_concrete_magazine_136k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 135903.00; date_signed 2011-09-29.",
    investment_type="epc",
)

# === Cycle 1369 ===
row_doc(
    "qa_colombia_la_macarena_concrete_wall_121k_2021",
    "infrastructure", "building_materials", "other",
    "QA Construction Services — Colombia La Macarena reinforced concrete wall",
    "Colombia",
    "30 Jul 2021: Department of Defense awards contract to QA CONSTRUCTION SERVICES S.A.S. for D/B repair of defensive positions and construction of reinforced concrete wall, La Macarena Army Base; obligated USD 121219.32. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "121219.32", "2021-07-30", "2021", "", "",
    "D/B REPAIR OF DEFENSIVE POSITIONS & CONSTRUCTION OF REINFORCED CONCRETE WALL, LA MACARENA , Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_qa_colombia_la_macarena_concrete_wall_121k_2021",
    "D/B REPAIR OF DEFENSIVE POSITIONS & CONSTRUCTION OF REINFORCED CONCRETE WALL, LA MACARENA ARMY BASE, COL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0247_9700_W9127821D0081_9700/",
    "Actor: QA CONSTRUCTION SERVICES S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1369",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0247_9700_W9127821D0081_9700 (qa_colombia_la_macarena_concrete_wall_121k_2021). Signed 2021-07-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0247_9700_W9127821D0081_9700/.",
    "USASpending: qa_colombia_la_macarena_concrete_wall_121k_2021 USD 0.121m. Supports qa_colombia_la_macarena_concrete_wall_121k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 121219.32; date_signed 2021-07-30.",
    investment_type="epc",
)

# === Cycle 1370 ===
row_doc(
    "virtra_mexico_le_training_simulators_231k_2019",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico law enforcement training simulators",
    "Mexico",
    "13 Mar 2019: Department of State awards contract to VIRTRA, INC. for law enforcement training simulators; obligated USD 230965.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "230965.00", "2019-03-13", "2019", "", "",
    "REQUIREMENT FOR LAW ENFORCEMENT TRAINING SIMULATORS., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_le_training_simulators_231k_2019",
    "REQUIREMENT FOR LAW ENFORCEMENT TRAINING SIMULATORS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1082_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle other_renewables dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1370",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19F1082_1900_SWHARC16D0003_1900 (virtra_mexico_le_training_simulators_231k_2019). Signed 2019-03-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1082_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_le_training_simulators_231k_2019 USD 0.231m. Supports virtra_mexico_le_training_simulators_231k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 230965.00; date_signed 2019-03-13.",
    investment_type="equipment_supply",
)

# === Cycle 1370 ===
row_doc(
    "faac_mexico_training_simulators_226k_2018",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico training simulators",
    "Mexico",
    "20 Mar 2018: Department of State awards contract to FAAC INCORPORATED for training simulators; obligated USD 226315.23. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "226315.23", "2018-03-20", "2018", "", "",
    "REQUIREMENT FOR TRAINING SIMULATORS., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_training_simulators_226k_2018",
    "REQUIREMENT FOR TRAINING SIMULATORS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1084_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle port_cranes dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1370",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F1084_1900_SWHARC16D0002_1900 (faac_mexico_training_simulators_226k_2018). Signed 2018-03-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1084_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_training_simulators_226k_2018 USD 0.226m. Supports faac_mexico_training_simulators_226k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 226315.23; date_signed 2018-03-20.",
    investment_type="equipment_supply",
)

# === Cycle 1370 ===
row_doc(
    "vinpar_colombia_aba_lift_supply_install_84k_2026",
    "infrastructure", "engineering_epc", "other",
    "Construcciones Vinpar — Colombia CMR ABA lift supply and installation",
    "Colombia",
    "22 Sep 2026: Department of State awards contract to CONSTRUCCIONES VINPAR S.A.S. for CMR ABA lift supply and installation; obligated USD 83823.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "83823.00", "2026-09-22", "2026", "", "",
    "PR16298777: CMR ABA LIFT SUPPLY & INSTALLATION-7687 XJ1D0167, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_vinpar_colombia_aba_lift_supply_install_84k_2026",
    "PR16298777: CMR ABA LIFT SUPPLY & INSTALLATION-7687 XJ1D0167",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026C0008_1900_-NONE-_-NONE-/",
    "Actor: CONSTRUCCIONES VINPAR S.A.S. — other. Official USASpending Award API. Shuffle engineering_epc CapEx.",
    "hunt_cycle1370",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02026C0008_1900_-NONE-_-NONE- (vinpar_colombia_aba_lift_supply_install_84k_2026). Signed 2026-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026C0008_1900_-NONE-_-NONE-/.",
    "USASpending: vinpar_colombia_aba_lift_supply_install_84k_2026 USD 0.084m. Supports vinpar_colombia_aba_lift_supply_install_84k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 83823.00; date_signed 2026-09-22.",
    investment_type="equipment_supply",
)

# === Cycle 1370 ===
row_doc(
    "vinpar_colombia_picota_videoconference_rooms_63k_2022",
    "infrastructure", "building_materials", "other",
    "Construcciones Vinpar — Colombia Picota penitentiary videoconference rooms",
    "Colombia",
    "17 Nov 2022: Department of State awards contract to CONSTRUCCIONES VINPAR S.A.S. for Bogota INL videoconference rooms at Picota Penitentiary; obligated USD 62547.41. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "62547.41", "2022-11-17", "2022", "", "",
    "BOGOTA INL- VIDEOCONFERENCE ROOMS AT PICOTA PENITENTIARY, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_vinpar_colombia_picota_videoconference_rooms_63k_2022",
    "BOGOTA INL- VIDEOCONFERENCE ROOMS AT PICOTA PENITENTIARY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01523C0001_1900_-NONE-_-NONE-/",
    "Actor: CONSTRUCCIONES VINPAR S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1370",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01523C0001_1900_-NONE-_-NONE- (vinpar_colombia_picota_videoconference_rooms_63k_2022). Signed 2022-11-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01523C0001_1900_-NONE-_-NONE-/.",
    "USASpending: vinpar_colombia_picota_videoconference_rooms_63k_2022 USD 0.063m. Supports vinpar_colombia_picota_videoconference_rooms_63k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62547.41; date_signed 2022-11-17.",
    investment_type="epc",
)

# === Cycle 1370 ===
row_doc(
    "sabillon_honduras_leimus_construction_materials_63k_2016",
    "infrastructure", "building_materials", "other",
    "Constructora Sabillon — Honduras Leimus GAD construction materials",
    "Honduras",
    "08 Jun 2016: Department of Defense awards contract to CONSTRUCTORA SABILLON for construction materials for the location of Leimus GAD; obligated USD 63457.40. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "63457.40", "2016-06-08", "2016", "", "",
    "CONSTRUCTION MATERIALS FOR THE LOCATION OF LEIMUS GAD, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_sabillon_honduras_leimus_construction_materials_63k_2016",
    "CONSTRUCTION MATERIALS FOR THE LOCATION OF LEIMUS GAD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710016P7004_9700_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA SABILLON — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1370",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_M2710016P7004_9700_-NONE-_-NONE- (sabillon_honduras_leimus_construction_materials_63k_2016). Signed 2016-06-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710016P7004_9700_-NONE-_-NONE-/.",
    "USASpending: sabillon_honduras_leimus_construction_materials_63k_2016 USD 0.063m. Supports sabillon_honduras_leimus_construction_materials_63k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 63457.40; date_signed 2016-06-08.",
    investment_type="epc",
)

# === Cycle 1371 ===
row_doc(
    "terrestris_peru_ha_equipment_supplies_217k_2024",
    "infrastructure", "engineering_epc", "us",
    "Terrestris — Peru humanitarian assistance equipment supplies tools materials",
    "Peru",
    "06 Dec 2024: Department of Defense awards contract to TERRESTRIS, LLC for personnel, equipment, supplies, transportation, tools, materials, supervision for HA work in Peru; obligated USD 217417.08. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "217417.08", "2024-12-06", "2024", "", "",
    "PERSONNEL, EQUIPMENT, SUPPLIES, TRANSPORTATION, TOOLS, MATERIALS, SUPERVISION, AND OTHER I, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_terrestris_peru_ha_equipment_supplies_217k_2024",
    "PERSONNEL, EQUIPMENT, SUPPLIES, TRANSPORTATION, TOOLS, MATERIALS, SUPERVISION, AND OTHER ITEMS ALONG WITH NON-PERSONAL SERVICES NECESSARY TO PERFORM THE WORK.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL25F0003_9700_W912CL23D0109_9700/",
    "Actor: TERRESTRIS, LLC (U.S.) — us. Official USASpending Award API. Shuffle nickel dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1371",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL25F0003_9700_W912CL23D0109_9700 (terrestris_peru_ha_equipment_supplies_217k_2024). Signed 2024-12-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL25F0003_9700_W912CL23D0109_9700/.",
    "USASpending: terrestris_peru_ha_equipment_supplies_217k_2024 USD 0.217m. Supports terrestris_peru_ha_equipment_supplies_217k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 217417.08; date_signed 2024-12-06.",
    investment_type="equipment_supply",
)

# === Cycle 1371 ===
row_doc(
    "power_engineers_peru_lima_security_installation_216k_2010",
    "infrastructure", "engineering_epc", "us",
    "Power Engineers — Peru Lima power systems security installation",
    "Peru",
    "17 Mar 2010: Department of State awards contract to POWER ENGINEERS INC for power systems Lima Peru security installation; obligated USD 215507.60. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "215507.60", "2010-03-17", "2010", "", "",
    "POWER SYSTEMS- LIMA, PERU SECURITY INSTALLATION, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_power_engineers_peru_lima_security_installation_216k_2010",
    "POWER SYSTEMS- LIMA, PERU SECURITY INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F0988_1900_SALMEC05D0010_1900/",
    "Actor: POWER ENGINEERS INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1371",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F0988_1900_SALMEC05D0010_1900 (power_engineers_peru_lima_security_installation_216k_2010). Signed 2010-03-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F0988_1900_SALMEC05D0010_1900/.",
    "USASpending: power_engineers_peru_lima_security_installation_216k_2010 USD 0.216m. Supports power_engineers_peru_lima_security_installation_216k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 215507.60; date_signed 2010-03-17.",
    investment_type="equipment_supply",
)

# === Cycle 1371 ===
row_doc(
    "sabillon_honduras_self_powered_light_towers_61k_2024",
    "infrastructure", "engineering_epc", "other",
    "Constructora Sabillon — Honduras self-powered light towers",
    "Honduras",
    "07 Mar 2024: Department of Defense awards contract to CONSTRUCTORA SABILLON for self powered light towers; obligated USD 60571.25. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "60571.25", "2024-03-07", "2024", "", "",
    "SELF POWERD LIGHT TOWERS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_sabillon_honduras_self_powered_light_towers_61k_2024",
    "SELF POWERD LIGHT TOWERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM24P0018_9700_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA SABILLON — other. Official USASpending Award API. Shuffle engineering_epc CapEx.",
    "hunt_cycle1371",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM24P0018_9700_-NONE-_-NONE- (sabillon_honduras_self_powered_light_towers_61k_2024). Signed 2024-03-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM24P0018_9700_-NONE-_-NONE-/.",
    "USASpending: sabillon_honduras_self_powered_light_towers_61k_2024 USD 0.061m. Supports sabillon_honduras_self_powered_light_towers_61k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60571.25; date_signed 2024-03-07.",
    investment_type="equipment_supply",
)

# === Cycle 1371 ===
row_doc(
    "qa_colombia_material_installation_42k_2017",
    "infrastructure", "engineering_epc", "other",
    "QA Construction Services — Colombia material installation",
    "Colombia",
    "26 Sep 2017: Department of Defense awards contract to QA CONSTRUCTION SERVICES S.A.S. for material installation; obligated USD 41785.33. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "41785.33", "2017-09-26", "2017", "", "",
    "MATERIAL INSTALLATION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_qa_colombia_material_installation_42k_2017",
    "MATERIAL INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT17P0231_9700_-NONE-_-NONE-/",
    "Actor: QA CONSTRUCTION SERVICES S.A.S. — other. Official USASpending Award API. Shuffle building_materials→engineering_epc CapEx.",
    "hunt_cycle1371",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT17P0231_9700_-NONE-_-NONE- (qa_colombia_material_installation_42k_2017). Signed 2017-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT17P0231_9700_-NONE-_-NONE-/.",
    "USASpending: qa_colombia_material_installation_42k_2017 USD 0.042m. Supports qa_colombia_material_installation_42k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 41785.33; date_signed 2017-09-26.",
    investment_type="equipment_supply",
)

# === Cycle 1371 ===
row_doc(
    "sabillon_honduras_school_republica_cuba_bom_37k_2016",
    "infrastructure", "building_materials", "other",
    "Constructora Sabillon — Honduras School Republica de Cuba bill of materials",
    "Honduras",
    "19 Aug 2016: Department of Defense awards contract to CONSTRUCTORA SABILLON for School Republica de Cuba bill of materials II; obligated USD 36838.85. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "36838.85", "2016-08-19", "2016", "", "",
    "SCHOOL REPUBLICA DE CUBA BILL OF MATERIALS II, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_sabillon_honduras_school_republica_cuba_bom_37k_2016",
    "SCHOOL REPUBLICA DE CUBA BILL OF MATERIALS II",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710016P7017_9700_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA SABILLON — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1371",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_M2710016P7017_9700_-NONE-_-NONE- (sabillon_honduras_school_republica_cuba_bom_37k_2016). Signed 2016-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710016P7017_9700_-NONE-_-NONE-/.",
    "USASpending: sabillon_honduras_school_republica_cuba_bom_37k_2016 USD 0.037m. Supports sabillon_honduras_school_republica_cuba_bom_37k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 36838.85; date_signed 2016-08-19.",
    investment_type="epc",
)

# === Cycle 1372 ===
row_doc(
    "virtra_mexico_lets_idiq_211k_2018",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico law enforcement training simulators LETS",
    "Mexico",
    "18 Apr 2018: Department of State awards contract to VIRTRA, INC. for law enforcement training simulators (LETS); obligated USD 210768.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "210768.00", "2018-04-18", "2018", "", "",
    "LAW ENFORCEMENT TRAINING SIMULATORS (LETS) IDIQ FAAC INCORPORATED (SWHARC16D0002)&VIRTRA S, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_lets_idiq_211k_2018",
    "LAW ENFORCEMENT TRAINING SIMULATORS (LETS) IDIQ FAAC INCORPORATED (SWHARC16D0002)&VIRTRA SYSTEMS (SWHARC16D0003)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1382_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle niobium dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1372",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F1382_1900_SWHARC16D0003_1900 (virtra_mexico_lets_idiq_211k_2018). Signed 2018-04-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1382_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_lets_idiq_211k_2018 USD 0.211m. Supports virtra_mexico_lets_idiq_211k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 210768.00; date_signed 2018-04-18.",
    investment_type="equipment_supply",
)

# === Cycle 1372 ===
row_doc(
    "faac_mexico_training_simulators_198k_2019",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico training simulators",
    "Mexico",
    "14 Mar 2019: Department of State awards contract to FAAC INCORPORATED for training simulators; obligated USD 197625.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "197625.00", "2019-03-14", "2019", "", "",
    "REQUIREMENT FOR TRAINING SIMULATORS., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_training_simulators_198k_2019",
    "REQUIREMENT FOR TRAINING SIMULATORS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1091_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle graphite dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1372",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19F1091_1900_SWHARC16D0002_1900 (faac_mexico_training_simulators_198k_2019). Signed 2019-03-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1091_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_training_simulators_198k_2019 USD 0.198m. Supports faac_mexico_training_simulators_198k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 197625.00; date_signed 2019-03-14.",
    investment_type="equipment_supply",
)

# === Cycle 1372 ===
row_doc(
    "sabillon_honduras_building_materials_30k_2017",
    "infrastructure", "building_materials", "other",
    "Constructora Sabillon — Honduras building materials",
    "Honduras",
    "15 Jun 2017: Department of Defense awards contract to CONSTRUCTORA SABILLON for building materials in Honduras; obligated USD 30347.19. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "30347.19", "2017-06-15", "2017", "", "",
    "BUILDING MATERIALS IN HONDURAS., Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_sabillon_honduras_building_materials_30k_2017",
    "BUILDING MATERIALS IN HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710017P6004_9700_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA SABILLON — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1372",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_M2710017P6004_9700_-NONE-_-NONE- (sabillon_honduras_building_materials_30k_2017). Signed 2017-06-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710017P6004_9700_-NONE-_-NONE-/.",
    "USASpending: sabillon_honduras_building_materials_30k_2017 USD 0.030m. Supports sabillon_honduras_building_materials_30k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 30347.19; date_signed 2017-06-15.",
    investment_type="epc",
)

# === Cycle 1372 ===
row_doc(
    "proyectos_colombia_construction_19k_2011",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia construction",
    "Colombia",
    "27 Sep 2011: Department of Defense awards contract to PROYECTOS CIVILES S Y M LIMITADA for construction; obligated USD 18576.25. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "18576.25", "2011-09-27", "2011", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_construction_19k_2011",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0288_9700_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1372",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11P0288_9700_-NONE-_-NONE- (proyectos_colombia_construction_19k_2011). Signed 2011-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0288_9700_-NONE-_-NONE-/.",
    "USASpending: proyectos_colombia_construction_19k_2011 USD 0.019m. Supports proyectos_colombia_construction_19k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18576.25; date_signed 2011-09-27.",
    investment_type="epc",
)

# === Cycle 1372 ===
row_doc(
    "sabillon_honduras_scab_construction_materials_18k_2016",
    "infrastructure", "building_materials", "other",
    "Constructora Sabillon — Honduras SCAB miscellaneous construction materials",
    "Honduras",
    "08 Jun 2016: Department of Defense awards contract to CONSTRUCTORA SABILLON for miscellaneous construction materials for SCAB; obligated USD 18083.04. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "18083.04", "2016-06-08", "2016", "", "",
    "MISCELLANEOUS CONSTRUCTION MATERIALS FOR SCAB, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_sabillon_honduras_scab_construction_materials_18k_2016",
    "MISCELLANEOUS CONSTRUCTION MATERIALS FOR SCAB",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710016P7003_9700_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA SABILLON — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1372",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_M2710016P7003_9700_-NONE-_-NONE- (sabillon_honduras_scab_construction_materials_18k_2016). Signed 2016-06-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710016P7003_9700_-NONE-_-NONE-/.",
    "USASpending: sabillon_honduras_scab_construction_materials_18k_2016 USD 0.018m. Supports sabillon_honduras_scab_construction_materials_18k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18083.04; date_signed 2016-06-08.",
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
