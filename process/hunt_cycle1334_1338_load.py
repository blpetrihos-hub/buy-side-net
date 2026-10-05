#!/usr/bin/env python3
"""Cycles 1334–1338: USASpending LatAm CapEx (CEEPCO/Alutiiq/Human Tech/IsoBOX + Eterna/Estudios/Proyectos EPC).

Seeds: 20262334–20262338. Thin top-up dry.
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

# === Cycle 1334 ===
row_doc(
    "ceepco_haiti_ucref_rehab_1426k_2014",
    "infrastructure", "building_materials", "us",
    "CEEPCO Contracting — Haiti UCREF facility rehabilitation",
    "Haiti",
    "11 Apr 2014: Department of State awards contract to CEEPCO CONTRACTING, LLC for rehabilitation of UCREF facility; obligated USD 1425848.80. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1425848.80", "2014-04-11", "2014", "", "",
    "REHABILITATION OF UCREF FACILITY, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_ceepco_haiti_ucref_rehab_1426k_2014",
    "OTHER FUNCTIONS IGF::OT::IGF REHABILITATION OF UCREF FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0093_1900_-NONE-_-NONE-/",
    "Actor: CEEPCO CONTRACTING, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1334",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14C0093_1900_-NONE-_-NONE- (ceepco_haiti_ucref_rehab_1426k_2014). Signed 2014-04-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0093_1900_-NONE-_-NONE-/.",
    "USASpending: ceepco_haiti_ucref_rehab_1426k_2014 USD 1.426m. Supports ceepco_haiti_ucref_rehab_1426k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1425848.8; date_signed 2014-04-11.",
    investment_type="epc",
)

# === Cycle 1334 ===
row_doc(
    "alutiiq_mexico_chemistry_equipment_6267k_2018",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Mexico INL chemistry equipment",
    "Mexico",
    "21 Sep 2018: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for chemistry equipment for INL/Mexico; obligated USD 6266917.66. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "6266917.66", "2018-09-21", "2018", "", "",
    "CHEMISTRY EQUIPMENT FOR INL/MEXICO, Mexico (USASpending description; award text names Mexico; coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_chemistry_equipment_6267k_2018",
    "PURCHASE ORDER FOR CHEMISTRY EQUIPMENT FOR INL/MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE18P0126_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Country from award description (INL/Mexico).",
    "hunt_cycle1334",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE18P0126_1900_-NONE-_-NONE- (alutiiq_mexico_chemistry_equipment_6267k_2018). Signed 2018-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE18P0126_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_chemistry_equipment_6267k_2018 USD 6.267m. Supports alutiiq_mexico_chemistry_equipment_6267k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6266917.66; date_signed 2018-09-21.",
    investment_type="equipment_supply",
)

# === Cycle 1334 ===
row_doc(
    "eterna_guatemala_ops_center_barracks_2006k_2016",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Guatemala operations center and barracks",
    "Guatemala",
    "28 Sep 2016: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for SOFA agreement operations center and barracks; obligated USD 2006482.66. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2006482.66", "2016-09-28", "2016", "", "",
    "SOFA AGREEMENT OPERATIONS CENTER&BARRACKS, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_guatemala_ops_center_barracks_2006k_2016",
    "IGF::OT::IGF SOFA AGREEMENT OPERATIONS CENTER&BARRACKS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127816D0101_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1334",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127816D0101_9700 (eterna_guatemala_ops_center_barracks_2006k_2016). Signed 2016-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127816D0101_9700/.",
    "USASpending: eterna_guatemala_ops_center_barracks_2006k_2016 USD 2.006m. Supports eterna_guatemala_ops_center_barracks_2006k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2006482.66; date_signed 2016-09-28.",
    investment_type="epc",
)

# === Cycle 1334 ===
row_doc(
    "eterna_panama_medical_facility_1664k_2014",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Panama medical facility construction",
    "Panama",
    "30 Sep 2014: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for medical facility construction; obligated USD 1663746.66. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1663746.66", "2014-09-30", "2014", "", "",
    "MEDICAL FACILITY CONSTRUCTION, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_panama_medical_facility_1664k_2014",
    "IGF::OT::IGF MEDICAL FACILITY CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127813D0011_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1334",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127813D0011_9700 (eterna_panama_medical_facility_1664k_2014). Signed 2014-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127813D0011_9700/.",
    "USASpending: eterna_panama_medical_facility_1664k_2014 USD 1.664m. Supports eterna_panama_medical_facility_1664k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1663746.66; date_signed 2014-09-30.",
    investment_type="epc",
)

# === Cycle 1334 ===
row_doc(
    "eterna_colombia_hap_67205_1143k_2023",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Colombia HAP 67205 and HAP 672026",
    "Colombia",
    "30 Sep 2023: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for HAP 67205 and HAP 672026; obligated USD 1143206.36. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1143206.36", "2023-09-30", "2023", "", "",
    "HAP 67205 & HAP 672026, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_colombia_hap_67205_1143k_2023",
    "HAP 67205 & HAP 672026",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0500_9700_W9127823D0059_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1334",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127823F0500_9700_W9127823D0059_9700 (eterna_colombia_hap_67205_1143k_2023). Signed 2023-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0500_9700_W9127823D0059_9700/.",
    "USASpending: eterna_colombia_hap_67205_1143k_2023 USD 1.143m. Supports eterna_colombia_hap_67205_1143k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1143206.36; date_signed 2023-09-30.",
    investment_type="epc",
)

# === Cycle 1335 ===
row_doc(
    "human_tech_colombia_computer_equipment_649k_2022",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Colombia GAPP computer equipment Bogota",
    "Colombia",
    "23 Sep 2022: Department of State awards contract to HUMAN TECHNOLOGIES CORP for 46 GAPP computer equipment Bogota Colombia; obligated USD 648541.09. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "648541.09", "2022-09-23", "2022", "", "",
    "46 GAPP COMPUTER EQUIPMENT - BOGOTA COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_colombia_computer_equipment_649k_2022",
    "46 GAPP COMPUTER EQUIPMENT - BOGOTA COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22F0051_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1335",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE22F0051_1900_19AQMM21D0007_1900 (human_tech_colombia_computer_equipment_649k_2022). Signed 2022-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22F0051_1900_19AQMM21D0007_1900/.",
    "USASpending: human_tech_colombia_computer_equipment_649k_2022 USD 0.649m. Supports human_tech_colombia_computer_equipment_649k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 648541.09; date_signed 2022-09-23.",
    investment_type="equipment_supply",
)

# === Cycle 1335 ===
row_doc(
    "alutiiq_colombia_prefab_containers_do25_627k_2020",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Colombia prefabricated containers DO 25",
    "Colombia",
    "12 May 2020: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for delivery order 25 prefabricated containers; obligated USD 626791.84. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "626791.84", "2020-05-12", "2020", "", "",
    "PRE-FABRICATED CONTAINERS DO 25, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_colombia_prefab_containers_do25_627k_2020",
    "INL BOGOTA ERADICATION SUPPORT IDIQ - ALUTIIQ ESSENTIAL SERVICES - DELIVERY ORDER 25: PRE-FABRICATED CONTAINERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1749_1900_19AQMM19D0050_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1335",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F1749_1900_19AQMM19D0050_1900 (alutiiq_colombia_prefab_containers_do25_627k_2020). Signed 2020-05-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1749_1900_19AQMM19D0050_1900/.",
    "USASpending: alutiiq_colombia_prefab_containers_do25_627k_2020 USD 0.627m. Supports alutiiq_colombia_prefab_containers_do25_627k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 626791.84; date_signed 2020-05-12.",
    investment_type="equipment_supply",
)

# === Cycle 1335 ===
row_doc(
    "estudios_costarica_cnt_checkpoint_golfito_1089k_2011",
    "infrastructure", "bridges_roads", "other",
    "Estudios Edificaciones EEII — Costa Rica CNT checkpoint 35 Golfito",
    "Costa Rica",
    "26 Sep 2011: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for construction of CNT checkpoint 35 Golfito; obligated USD 1089159.60. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1089159.60", "2011-09-26", "2011", "", "",
    "CONSTRUCTION OF CNT CHECKPOINT 35, GOLFITO, COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_costarica_cnt_checkpoint_golfito_1089k_2011",
    "TAS::21 2020::TAS CONSTRUCTION OF CNT CHECKPOINT 35, GOLFITO, COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127811D0050_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1335",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127811D0050_9700 (estudios_costarica_cnt_checkpoint_golfito_1089k_2011). Signed 2011-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127811D0050_9700/.",
    "USASpending: estudios_costarica_cnt_checkpoint_golfito_1089k_2011 USD 1.089m. Supports estudios_costarica_cnt_checkpoint_golfito_1089k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1089159.6; date_signed 2011-09-26.",
    investment_type="epc",
)

# === Cycle 1335 ===
row_doc(
    "eterna_colombia_hap_20209_1000k_2013",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Colombia construction of HAP 20209",
    "Colombia",
    "28 Sep 2013: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for construction of HAP 20209; obligated USD 1000000.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1000000.00", "2013-09-28", "2013", "", "",
    "CONSTRUCTION OF HAP 20209, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_colombia_hap_20209_1000k_2013",
    "IGF::OT::IGF CONSTRUCTION OF HAP 20209",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0011_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1335",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127813D0011_9700 (eterna_colombia_hap_20209_1000k_2013). Signed 2013-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0011_9700/.",
    "USASpending: eterna_colombia_hap_20209_1000k_2013 USD 1.000m. Supports eterna_colombia_hap_20209_1000k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1000000.0; date_signed 2013-09-28.",
    investment_type="epc",
)

# === Cycle 1335 ===
row_doc(
    "estudios_ecuador_hap_latines_pucara_937k_2010",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Ecuador HAP latrines Pucara",
    "Ecuador",
    "21 Sep 2010: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for D/B HAP latrines Pucara; obligated USD 936984.56. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "936984.56", "2010-09-21", "2010", "", "",
    "D/B HAP LATINES PUCARA, ECUADOR, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_ecuador_hap_latines_pucara_937k_2010",
    "D/B HAP LATINES PUCARA, ECUADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127809D0077_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1335",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127809D0077_9700 (estudios_ecuador_hap_latines_pucara_937k_2010). Signed 2010-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127809D0077_9700/.",
    "USASpending: estudios_ecuador_hap_latines_pucara_937k_2010 USD 0.937m. Supports estudios_ecuador_hap_latines_pucara_937k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 936984.56; date_signed 2010-09-21.",
    investment_type="epc",
)

# === Cycle 1336 ===
row_doc(
    "alutiiq_colombia_forensics_equipment_2484k_2021",
    "infrastructure", "building_materials", "us",
    "Alutiiq Technical Services — Colombia Attorney General forensics equipment",
    "Colombia",
    "30 Sep 2021: Department of State awards contract to ALUTIIQ TECHNICAL SERVICES LLC for procure, deliver, install forensic equipment in six laboratories; obligated USD 2483502.21. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2483502.21", "2021-09-30", "2021", "", "",
    "ATTORNEY'S GENERAL OFFICE FORENSICS PROJECT, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_colombia_forensics_equipment_2484k_2021",
    "INL BOGOTA ATTORNEY'S GENERAL OFFICE FORENSICS PROJECT. THE CONTRACTOR WILL PROCURE, DELIVER, INSTALL, AND PROVIDE TRAINING FOR A VARIETY (OVER 100 DIFFERENT ITEMS) OF FORENSIC EQUIPMENT IN SIX (6) LABORATORIES THROUGHOU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F4953_1900_19AQMM21D0040_1900/",
    "Actor: ALUTIIQ TECHNICAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1336",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21F4953_1900_19AQMM21D0040_1900 (alutiiq_colombia_forensics_equipment_2484k_2021). Signed 2021-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F4953_1900_19AQMM21D0040_1900/.",
    "USASpending: alutiiq_colombia_forensics_equipment_2484k_2021 USD 2.484m. Supports alutiiq_colombia_forensics_equipment_2484k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2483502.21; date_signed 2021-09-30.",
    investment_type="equipment_supply",
)

# === Cycle 1336 ===
row_doc(
    "alutiiq_colombia_emcar_field_equipment_636k_2019",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Colombia EMCAR field equipment",
    "Colombia",
    "9 May 2019: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for delivery order 8 EMCAR field equipment; obligated USD 636055.96. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "636055.96", "2019-05-09", "2019", "", "",
    "EMCAR FIELD EQUIPMENT, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_colombia_emcar_field_equipment_636k_2019",
    "INL BOGOTA ERADICATION SUPPORT IDIQ - ALUTIIQ ESSENTIAL SERVICES - DELIVERY ORDER 8: EMCAR FIELD EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1595_1900_19AQMM19D0050_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1336",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19F1595_1900_19AQMM19D0050_1900 (alutiiq_colombia_emcar_field_equipment_636k_2019). Signed 2019-05-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1595_1900_19AQMM19D0050_1900/.",
    "USASpending: alutiiq_colombia_emcar_field_equipment_636k_2019 USD 0.636m. Supports alutiiq_colombia_emcar_field_equipment_636k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 636055.96; date_signed 2019-05-09.",
    investment_type="equipment_supply",
)

# === Cycle 1336 ===
row_doc(
    "estudios_peru_hap_river_school_898k_2011",
    "infrastructure", "bridges_roads", "other",
    "Estudios Edificaciones EEII — Peru HAP river crossing and school Chumbquihiu",
    "Peru",
    "22 Sep 2011: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for design build HAP 9385 river crossing and HAP 9308 school; obligated USD 897831.87. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "897831.87", "2011-09-22", "2011", "", "",
    "DESIGN BUILD HAP 9385 RIVER CROSSING AND HAP 9308 SCHOOL AT CASERIO, CHUMBQUIHUI, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_peru_hap_river_school_898k_2011",
    "TAS::97 0819::TAS DESIGN BUILD HAP 9385 RIVER CROSSING AND HAP 9308 SCHOOL AT CASERIO, CHUMBQUIHUI,",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127809D0077_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1336",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0007_9700_W9127809D0077_9700 (estudios_peru_hap_river_school_898k_2011). Signed 2011-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127809D0077_9700/.",
    "USASpending: estudios_peru_hap_river_school_898k_2011 USD 0.898m. Supports estudios_peru_hap_river_school_898k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 897831.87; date_signed 2011-09-22.",
    investment_type="epc",
)

# === Cycle 1336 ===
row_doc(
    "eterna_honduras_lrc_facility_877k_2020",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras Soto Cano LRC facility",
    "Honduras",
    "22 Jun 2020: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for LRC facility at Soto Cano AB; obligated USD 877085.73. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "877085.73", "2020-06-22", "2020", "", "",
    "LRC FACILITY AT SOTO CANO AB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_lrc_facility_877k_2020",
    "LRC FACILITY AT SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0221_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1336",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127820F0221_9700_W9127816D0102_9700 (eterna_honduras_lrc_facility_877k_2020). Signed 2020-06-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0221_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_lrc_facility_877k_2020 USD 0.877m. Supports eterna_honduras_lrc_facility_877k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 877085.73; date_signed 2020-06-22.",
    investment_type="epc",
)

# === Cycle 1336 ===
row_doc(
    "eterna_honduras_hap_copan_844k_2015",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras HAP 23825 Copan",
    "Honduras",
    "12 Jun 2015: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D/B HAP 23825 Copan; obligated USD 844044.83. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "844044.83", "2015-06-12", "2015", "", "",
    "D/B HAP 23825 COPAN, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_hap_copan_844k_2015",
    "IGF::OT::IGF D/B HAP 23825 COPAN, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127815D0048_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1336",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127815D0048_9700 (eterna_honduras_hap_copan_844k_2015). Signed 2015-06-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127815D0048_9700/.",
    "USASpending: eterna_honduras_hap_copan_844k_2015 USD 0.844m. Supports eterna_honduras_hap_copan_844k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 844044.83; date_signed 2015-06-12.",
    investment_type="epc",
)

# === Cycle 1337 ===
row_doc(
    "isobox_panama_office_dormitory_containers_46k_2024",
    "infrastructure", "building_materials", "us",
    "IsoBOX — Panama office and dormitory containers",
    "Panama",
    "4 Sep 2024: Department of State awards contract to ISOBOX INC for office and dormitory containers; obligated USD 45540.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "45540.00", "2024-09-04", "2024", "", "",
    "OFFICE AND DORMITORY CONTAINERS, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_isobox_panama_office_dormitory_containers_46k_2024",
    "OFFICE AND DORMITORY CONTAINERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0724P0894_1900_-NONE-_-NONE-/",
    "Actor: ISOBOX INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1337",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0724P0894_1900_-NONE-_-NONE- (isobox_panama_office_dormitory_containers_46k_2024). Signed 2024-09-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0724P0894_1900_-NONE-_-NONE-/.",
    "USASpending: isobox_panama_office_dormitory_containers_46k_2024 USD 0.046m. Supports isobox_panama_office_dormitory_containers_46k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 45540.0; date_signed 2024-09-04.",
    investment_type="equipment_supply",
)

# === Cycle 1337 ===
row_doc(
    "isobox_panama_workspace_modules_43k_2017",
    "infrastructure", "building_materials", "us",
    "IsoBOX — Panama transportable temporary workspace modules",
    "Panama",
    "9 Mar 2017: Department of State awards contract to ISOBOX INC for transportable temporary workspace modules for containers; obligated USD 42930.90. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "42930.90", "2017-03-09", "2017", "", "",
    "TRANSPORTABLE TEMPORARY WORKSPACE MODULES FOR CONTAINERS, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_isobox_panama_workspace_modules_43k_2017",
    "TRANSPORTABLE TEMPORARY WORKSPACE MODULES FOR CONTAINERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07017M0247_1900_-NONE-_-NONE-/",
    "Actor: ISOBOX INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1337",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07017M0247_1900_-NONE-_-NONE- (isobox_panama_workspace_modules_43k_2017). Signed 2017-03-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07017M0247_1900_-NONE-_-NONE-/.",
    "USASpending: isobox_panama_workspace_modules_43k_2017 USD 0.043m. Supports isobox_panama_workspace_modules_43k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 42930.9; date_signed 2017-03-09.",
    investment_type="equipment_supply",
)

# === Cycle 1337 ===
row_doc(
    "eterna_honduras_construction_warehouse_838k_2024",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras Soto Cano construction installation warehouse",
    "Honduras",
    "25 Sep 2024: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for construction installation warehouse Soto Cano AB; obligated USD 837962.13. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "837962.13", "2024-09-25", "2024", "", "",
    "CONSTRUCTION INSTALLATION WAREHOUSE FOR SOTO CANO AB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_construction_warehouse_838k_2024",
    "CONSTRUCTION INSTALLATION WAREHOUSE FOR SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0338_9700_W9127823D0073_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1337",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0338_9700_W9127823D0073_9700 (eterna_honduras_construction_warehouse_838k_2024). Signed 2024-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0338_9700_W9127823D0073_9700/.",
    "USASpending: eterna_honduras_construction_warehouse_838k_2024 USD 0.838m. Supports eterna_honduras_construction_warehouse_838k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 837962.13; date_signed 2024-09-25.",
    investment_type="epc",
)

# === Cycle 1337 ===
row_doc(
    "eterna_honduras_juliet_taxiway_835k_2021",
    "infrastructure", "bridges_roads", "other",
    "Empresa Eterna — Honduras Soto Cano Juliet taxiway",
    "Honduras",
    "15 Jul 2021: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for Juliet taxiway Soto Cano; obligated USD 834694.86. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "834694.86", "2021-07-15", "2021", "", "",
    "JULIET TAXIWAY, SOTO CANO, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_juliet_taxiway_835k_2021",
    "JULIET TAXIWAY, SOTO CANO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0224_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1337",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0224_9700_W9127816D0102_9700 (eterna_honduras_juliet_taxiway_835k_2021). Signed 2021-07-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0224_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_juliet_taxiway_835k_2021 USD 0.835m. Supports eterna_honduras_juliet_taxiway_835k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 834694.86; date_signed 2021-07-15.",
    investment_type="epc",
)

# === Cycle 1337 ===
row_doc(
    "eterna_honduras_marforsouth_hq_799k_2016",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras MARFORSOUTH HQ facility",
    "Honduras",
    "19 Sep 2016: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for MARFORSOUTH HQ facility SOFA agreement; obligated USD 799363.80. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "799363.80", "2016-09-19", "2016", "", "",
    "MARFORSOUTH HQ FACILITY SOFA AGREEMENT, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_marforsouth_hq_799k_2016",
    "IGF::OT::IGF MARFORSOUTH HQ FACILITY SOFA AGREEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1337",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127816D0102_9700 (eterna_honduras_marforsouth_hq_799k_2016). Signed 2016-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_marforsouth_hq_799k_2016 USD 0.799m. Supports eterna_honduras_marforsouth_hq_799k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 799363.8; date_signed 2016-09-19.",
    investment_type="epc",
)

# === Cycle 1338 ===
row_doc(
    "isobox_panama_modular_shower_laundry_14k_2020",
    "infrastructure", "building_materials", "us",
    "IsoBOX — Panama modular shower and laundry area",
    "Panama",
    "5 Jun 2020: Department of State awards contract to ISOBOX INC for modular shower and laundry area; obligated USD 13785.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "13785.00", "2020-06-05", "2020", "", "",
    "MODULAR SHOWER AND LAUNDRY AREA, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_isobox_panama_modular_shower_laundry_14k_2020",
    "MODULAR SHOWER AND LAUNDRY AREA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0720P0407_1900_-NONE-_-NONE-/",
    "Actor: ISOBOX INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1338",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0720P0407_1900_-NONE-_-NONE- (isobox_panama_modular_shower_laundry_14k_2020). Signed 2020-06-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0720P0407_1900_-NONE-_-NONE-/.",
    "USASpending: isobox_panama_modular_shower_laundry_14k_2020 USD 0.014m. Supports isobox_panama_modular_shower_laundry_14k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13785.0; date_signed 2020-06-05.",
    investment_type="equipment_supply",
)

# === Cycle 1338 ===
row_doc(
    "isobox_panama_window_fabrication_install_30k_2023",
    "infrastructure", "building_materials", "us",
    "IsoBOX — Panama window fabrication and installation",
    "Panama",
    "27 Nov 2023: Department of State awards contract to ISOBOX INC for window fabrication and installation; obligated USD 29733.20. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "29733.20", "2023-11-27", "2023", "", "",
    "WINDOW FABRICATION AND INSTALLATION, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_isobox_panama_window_fabrication_install_30k_2023",
    "WINDOW FABRICATION AND INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0724P0080_1900_-NONE-_-NONE-/",
    "Actor: ISOBOX INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1338",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0724P0080_1900_-NONE-_-NONE- (isobox_panama_window_fabrication_install_30k_2023). Signed 2023-11-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0724P0080_1900_-NONE-_-NONE-/.",
    "USASpending: isobox_panama_window_fabrication_install_30k_2023 USD 0.030m. Supports isobox_panama_window_fabrication_install_30k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 29733.2; date_signed 2023-11-27.",
    investment_type="epc",
)

# === Cycle 1338 ===
row_doc(
    "proyectos_colombia_tumaco_buildings_772k_2022",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia Tumaco buildings structural repair and upgrades",
    "Colombia",
    "14 Apr 2022: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for Tumaco buildings structural repair and upgrades; obligated USD 772428.73. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "772428.73", "2022-04-14", "2022", "", "",
    "TUMACO BUILDINGS STRUCTURAL REPAIR AND UPGRADES, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_tumaco_buildings_772k_2022",
    "TUMACO BUILDINGS STRUCTURAL REPAIR AND UPGRADES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0680_1900_19AQMM21D0039_1900/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1338",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F0680_1900_19AQMM21D0039_1900 (proyectos_colombia_tumaco_buildings_772k_2022). Signed 2022-04-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0680_1900_19AQMM21D0039_1900/.",
    "USASpending: proyectos_colombia_tumaco_buildings_772k_2022 USD 0.772m. Supports proyectos_colombia_tumaco_buildings_772k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 772428.73; date_signed 2022-04-14.",
    investment_type="epc",
)

# === Cycle 1338 ===
row_doc(
    "estudios_colombia_jamundi_fire_protection_741k_2023",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Colombia Jamundi prison fire protection upgrades",
    "Colombia",
    "13 Jan 2023: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for Jamundi prison fire protection upgrades; obligated USD 740788.38. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "740788.38", "2023-01-13", "2023", "", "",
    "JAMUNDI PRISON FIRE PROTECTION UPGRADES, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_jamundi_fire_protection_741k_2023",
    "JAMUNDI PRISON FIRE PROTECTION UPGRADES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0031_1900_19AQMM21D0037_1900/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1338",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F0031_1900_19AQMM21D0037_1900 (estudios_colombia_jamundi_fire_protection_741k_2023). Signed 2023-01-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0031_1900_19AQMM21D0037_1900/.",
    "USASpending: estudios_colombia_jamundi_fire_protection_741k_2023 USD 0.741m. Supports estudios_colombia_jamundi_fire_protection_741k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 740788.38; date_signed 2023-01-13.",
    investment_type="epc",
)

# === Cycle 1338 ===
row_doc(
    "eterna_costarica_taxiway_apron_734k_2010",
    "infrastructure", "bridges_roads", "other",
    "Empresa Eterna — Costa Rica taxiway and parking apron",
    "Costa Rica",
    "17 Aug 2010: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for taxiway and parking apron; obligated USD 734104.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "734104.00", "2010-08-17", "2010", "", "",
    "TAXIWAY AND PARKING APRON, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_costarica_taxiway_apron_734k_2010",
    "TAXIWAY AND PARKING APRON",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127809D0071_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1338",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0009_9700_W9127809D0071_9700 (eterna_costarica_taxiway_apron_734k_2010). Signed 2010-08-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127809D0071_9700/.",
    "USASpending: eterna_costarica_taxiway_apron_734k_2010 USD 0.734m. Supports eterna_costarica_taxiway_apron_734k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 734104.0; date_signed 2010-08-17.",
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
