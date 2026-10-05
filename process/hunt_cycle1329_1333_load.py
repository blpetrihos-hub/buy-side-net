#!/usr/bin/env python3
"""Cycles 1329–1333: USASpending LatAm CapEx (CEEPCO/Human Tech/Alutiiq/IsoBOX + Eterna/Estudios EPC).

Seeds: 20262329–20262333. Thin top-up dry.
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

# === Cycle 1329 ===
row_doc(
    "ceepco_haiti_housing_site_prep_10257k_2013",
    "infrastructure", "building_materials", "us",
    "CEEPCO Contracting — Haiti housing development site preparation construction",
    "Haiti",
    "5 Aug 2013: Department of State awards contract to CEEPCO CONTRACTING, LLC for site preparation construction works for housing development; obligated USD 10257013.21. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "10257013.21", "2013-08-05", "2013", "", "",
    "SITE PREPARATION CONSTRUCTION WORKS FOR THE HOUSING DEVELOPMENT, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_ceepco_haiti_housing_site_prep_10257k_2013",
    "IGF::OT::IGF THIS CONTRACT IS TO REQUEST FROM POTENTIAL OFFERORS PROPOSALSFOR THE SITE PREPARATION CONSTRUCTION WORKS FOR THE HOUSING DEVELOPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1300009_7200_-NONE-_-NONE-/",
    "Actor: CEEPCO CONTRACTING, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1329",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521C1300009_7200_-NONE-_-NONE- (ceepco_haiti_housing_site_prep_10257k_2013). Signed 2013-08-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1300009_7200_-NONE-_-NONE-/.",
    "USASpending: ceepco_haiti_housing_site_prep_10257k_2013 USD 10.257m. Supports ceepco_haiti_housing_site_prep_10257k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10257013.21; date_signed 2013-08-05.",
    investment_type="epc",
)

# === Cycle 1329 ===
row_doc(
    "human_tech_guatemala_data_storage_878k_2024",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Guatemala data storage expansion equipment",
    "Guatemala",
    "24 Apr 2024: Department of State awards contract to HUMAN TECHNOLOGIES CORP for data storage expansion equipment; obligated USD 877739.52. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "877739.52", "2024-04-24", "2024", "", "",
    "DATA STORAGE EXPANSION EQUIPMENT, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_guatemala_data_storage_878k_2024",
    "DATA STORAGE EXPANSION EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0021_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1329",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24F0021_1900_19AQMM21D0007_1900 (human_tech_guatemala_data_storage_878k_2024). Signed 2024-04-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0021_1900_19AQMM21D0007_1900/.",
    "USASpending: human_tech_guatemala_data_storage_878k_2024 USD 0.878m. Supports human_tech_guatemala_data_storage_878k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 877739.52; date_signed 2024-04-24.",
    investment_type="equipment_supply",
)

# === Cycle 1329 ===
row_doc(
    "eterna_honduras_tigres_facility_5226k_2016",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras El Progreso Tigres facility",
    "Honduras",
    "29 Sep 2016: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for SOFA agreement Tigres facility El Progresso; obligated USD 5226029.87. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "5226029.87", "2016-09-29", "2016", "", "",
    "SOFA AGREEMENT TIGRES FACILITY (EL PROGRESSO), Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_tigres_facility_5226k_2016",
    "IGF::OT::IGF SOFA AGREEMENT TIGRES FACILITY (EL PROGRESSO)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1329",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0005_9700_W9127816D0102_9700 (eterna_honduras_tigres_facility_5226k_2016). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_tigres_facility_5226k_2016 USD 5.226m. Supports eterna_honduras_tigres_facility_5226k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5226029.87; date_signed 2016-09-29.",
    investment_type="epc",
)

# === Cycle 1329 ===
row_doc(
    "eterna_guatemala_las_montanitas_2941k_2013",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Guatemala Las Montanitas construction",
    "Guatemala",
    "23 Sep 2013: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for Las Montanitas construction; obligated USD 2941340.74. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2941340.74", "2013-09-23", "2013", "", "",
    "LAS MONTANITAS CONSTRUCTION, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_guatemala_las_montanitas_2941k_2013",
    "IGF::OT::IGF LAS MONTANITAS CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0020_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1329",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127813D0020_9700 (eterna_guatemala_las_montanitas_2941k_2013). Signed 2013-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0020_9700/.",
    "USASpending: eterna_guatemala_las_montanitas_2941k_2013 USD 2.941m. Supports eterna_guatemala_las_montanitas_2941k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2941340.74; date_signed 2013-09-23.",
    investment_type="epc",
)

# === Cycle 1329 ===
row_doc(
    "eterna_nicaragua_barracks_ops_gravel_2470k_2012",
    "infrastructure", "bridges_roads", "other",
    "Empresa Eterna — Nicaragua barracks, ops center and gravel road",
    "Nicaragua",
    "29 Sep 2012: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for barracks, ops center and gravel road; obligated USD 2469592.93. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2469592.93", "2012-09-29", "2012", "", "",
    "BARRACKS, OPS CENTER&GRAVEL RD, Nicaragua (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_nicaragua_barracks_ops_gravel_2470k_2012",
    "BARRACKS, OPS CENTER&GRAVEL RD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0020_9700_W9127811D0046_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1329",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0020_9700_W9127811D0046_9700 (eterna_nicaragua_barracks_ops_gravel_2470k_2012). Signed 2012-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0020_9700_W9127811D0046_9700/.",
    "USASpending: eterna_nicaragua_barracks_ops_gravel_2470k_2012 USD 2.470m. Supports eterna_nicaragua_barracks_ops_gravel_2470k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2469592.93; date_signed 2012-09-29.",
    investment_type="epc",
)

# === Cycle 1330 ===
row_doc(
    "alutiiq_guatemala_rol_cgc_it_606k_2022",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Guatemala ROL/CGC IT equipment",
    "Guatemala",
    "8 Dec 2022: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for IT equipment for INL Guatemala ROL/CGC; obligated USD 605854.01. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "605854.01", "2022-12-08", "2022", "", "",
    "REQUIREMENT IT EQUIPMENT FOR INL GUATEMALA ROL/CGC., Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_guatemala_rol_cgc_it_606k_2022",
    "REQUIREMENT IT EQUIPMENT FOR INL GUATEMALA ROL/CGC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0154_1900_19AQMM20D0010_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1330",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F0154_1900_19AQMM20D0010_1900 (alutiiq_guatemala_rol_cgc_it_606k_2022). Signed 2022-12-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0154_1900_19AQMM20D0010_1900/.",
    "USASpending: alutiiq_guatemala_rol_cgc_it_606k_2022 USD 0.606m. Supports alutiiq_guatemala_rol_cgc_it_606k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 605854.01; date_signed 2022-12-08.",
    investment_type="equipment_supply",
)

# === Cycle 1330 ===
row_doc(
    "alutiiq_guatemala_it_equipment_417k_2024",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Guatemala IT equipment delivery order",
    "Guatemala",
    "20 Jun 2024: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for IT equipment; obligated USD 416603.74. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "416603.74", "2024-06-20", "2024", "", "",
    "NEW DELIVERY ORDER FOR IT EQUIPMENT, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_guatemala_it_equipment_417k_2024",
    "NEW DELIVERY ORDER IN THE AMOUNT OF $416,603.74 FOR IT EQUIPMENT WITH A DELIVERY DATE OF 08/30/2024. THIS REQUIREMENT IS IN SUPPORT OF THE INL SECTION AT THE U.S. EMBASSY GUATEMALA CITY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0037_1900_19AQMM20D0010_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1330",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24F0037_1900_19AQMM20D0010_1900 (alutiiq_guatemala_it_equipment_417k_2024). Signed 2024-06-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0037_1900_19AQMM20D0010_1900/.",
    "USASpending: alutiiq_guatemala_it_equipment_417k_2024 USD 0.417m. Supports alutiiq_guatemala_it_equipment_417k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 416603.74; date_signed 2024-06-20.",
    investment_type="equipment_supply",
)

# === Cycle 1330 ===
row_doc(
    "estudios_panama_cn_rotary_wing_hangar_2390k_2016",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Panama CN rotary wing hangar",
    "Panama",
    "28 Sep 2016: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for SOFA agreement CN rotary wing hangar; obligated USD 2390474.88. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2390474.88", "2016-09-28", "2016", "", "",
    "SOFA AGREEMENT CN ROTARY WING HANGAR, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_panama_cn_rotary_wing_hangar_2390k_2016",
    "IGF::OT::IGF SOFA AGREEMENT CN ROTARY WING HANGAR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0010_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1330",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127813D0010_9700 (estudios_panama_cn_rotary_wing_hangar_2390k_2016). Signed 2016-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0010_9700/.",
    "USASpending: estudios_panama_cn_rotary_wing_hangar_2390k_2016 USD 2.390m. Supports estudios_panama_cn_rotary_wing_hangar_2390k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2390474.88; date_signed 2016-09-28.",
    investment_type="epc",
)

# === Cycle 1330 ===
row_doc(
    "estudios_honduras_disaster_warehouses_2119k_2012",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Honduras disaster relief warehouses",
    "Honduras",
    "24 Sep 2012: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for disaster relief warehouses at Tegucigalpa, San Pedro Sula, and Puerto Lempira; obligated USD 2118613.01. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2118613.01", "2012-09-24", "2012", "", "",
    "DISASTER RELIEF WAREHOUSES AT TEGUCIGALPA, SAN PEDRO SULA, AND PUERTO LEMPIRA, HONDURAS., Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_honduras_disaster_warehouses_2119k_2012",
    "DISASTER RELIEF WAREHOUSES AT TEGUCIGALPA, SAN PEDRO SULA, AND PUERTO LEMPIRA, HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127811D0050_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1330",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0008_9700_W9127811D0050_9700 (estudios_honduras_disaster_warehouses_2119k_2012). Signed 2012-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127811D0050_9700/.",
    "USASpending: estudios_honduras_disaster_warehouses_2119k_2012 USD 2.119m. Supports estudios_honduras_disaster_warehouses_2119k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2118613.01; date_signed 2012-09-24.",
    investment_type="epc",
)

# === Cycle 1330 ===
row_doc(
    "estudios_colombia_air_force_admin_1822k_2013",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Colombia Air Force admin building",
    "Colombia",
    "25 Apr 2013: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for Air Force admin building Colombia; obligated USD 1822001.63. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1822001.63", "2013-04-25", "2013", "", "",
    "AIR FORCE ADMIN BUILDING COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_air_force_admin_1822k_2013",
    "IGF::OT::IGF AIR FORCE ADMIN BUILDING COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127811D0050_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1330",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0010_9700_W9127811D0050_9700 (estudios_colombia_air_force_admin_1822k_2013). Signed 2013-04-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127811D0050_9700/.",
    "USASpending: estudios_colombia_air_force_admin_1822k_2013 USD 1.822m. Supports estudios_colombia_air_force_admin_1822k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1822001.63; date_signed 2013-04-25.",
    investment_type="epc",
)

# === Cycle 1331 ===
row_doc(
    "alutiiq_guatemala_biometric_bdsp_311k_2024",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Guatemala biometric BDSP equipment",
    "Guatemala",
    "26 Sep 2024: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for biometric equipment BDSP system; obligated USD 310814.75. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "310814.75", "2024-09-26", "2024", "", "",
    "BIOMETRIC EQUIPMENT BDSP SYSTEM, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_guatemala_biometric_bdsp_311k_2024",
    "NEW DELIVERY ORDER IN THE AMOUNT OF $310,814.75 FOR BIOMETRIC EQUIPMENT BDSP SYSTEM WITH A DELIVERY DATE OF 11/14/2024. THIS REQUIREMENT IS IN SUPPORT OF THE INL SECTION AT THE U.S. EMBASSY GUATEMALA CITY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0065_1900_19AQMM20D0010_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1331",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24F0065_1900_19AQMM20D0010_1900 (alutiiq_guatemala_biometric_bdsp_311k_2024). Signed 2024-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0065_1900_19AQMM20D0010_1900/.",
    "USASpending: alutiiq_guatemala_biometric_bdsp_311k_2024 USD 0.311m. Supports alutiiq_guatemala_biometric_bdsp_311k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 310814.75; date_signed 2024-09-26.",
    investment_type="equipment_supply",
)

# === Cycle 1331 ===
row_doc(
    "alutiiq_guatemala_tag_it_equipment_262k_2024",
    "infrastructure", "building_materials", "us",
    "Alutiiq Career Ventures — Guatemala TAG IT equipment",
    "Guatemala",
    "25 Sep 2024: Department of State awards contract to ALUTIIQ CAREER VENTURES LLC for TAG IT equipment; obligated USD 262247.95. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "262247.95", "2024-09-25", "2024", "", "",
    "TAG IT EQUIPMENT, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_guatemala_tag_it_equipment_262k_2024",
    "NEW PURCHASE ORDER IN THE AMOUNT OF $262,247.95 FOR TAG IT EQUIPMENT WITH A PERFORMANCE PERIOD OF 09/25/24 TO 12/31/24. THIS REQUIREMENT IS IN SUPPORT OF THE INL SECTION AT THE U.S. EMBASSY IN GUATEMALA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24P0126_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ CAREER VENTURES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1331",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24P0126_1900_-NONE-_-NONE- (alutiiq_guatemala_tag_it_equipment_262k_2024). Signed 2024-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24P0126_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_guatemala_tag_it_equipment_262k_2024 USD 0.262m. Supports alutiiq_guatemala_tag_it_equipment_262k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 262247.95; date_signed 2024-09-25.",
    investment_type="equipment_supply",
)

# === Cycle 1331 ===
row_doc(
    "eterna_elsalvador_cuscatlan_barracks_1737k_2013",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — El Salvador Cuscatlan barracks Comalapa",
    "El Salvador",
    "25 Sep 2013: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for Cuscatlan barracks Comalapa; obligated USD 1736794.64. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1736794.64", "2013-09-25", "2013", "", "",
    "CUSCATLAN BARRACKS, COMALAPA, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_elsalvador_cuscatlan_barracks_1737k_2013",
    "IGF::OT::IGF CUSCATLAN BARRACKS, COMALAPA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127813D0020_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1331",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127813D0020_9700 (eterna_elsalvador_cuscatlan_barracks_1737k_2013). Signed 2013-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127813D0020_9700/.",
    "USASpending: eterna_elsalvador_cuscatlan_barracks_1737k_2013 USD 1.737m. Supports eterna_elsalvador_cuscatlan_barracks_1737k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1736794.64; date_signed 2013-09-25.",
    investment_type="epc",
)

# === Cycle 1331 ===
row_doc(
    "estudios_colombia_rotary_wing_training_1666k_2011",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Colombia rotary wing training and force protection facilities",
    "Colombia",
    "30 Sep 2011: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for construction of rotary wing training facilities and force protection facilities; obligated USD 1666121.61. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1666121.61", "2011-09-30", "2011", "", "",
    "CONSTRUCTION OF ROTARY WING TRAINING FACILITIES AND FORCE PROTECTION FACILITIES, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_rotary_wing_training_1666k_2011",
    "TAS::21 2020::TAS CONSTRUCTION OF ROTARY WING TRAINING FACILITIES AND FORCE PROTECTION FACILITIES, F",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127809D0077_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1331",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0009_9700_W9127809D0077_9700 (estudios_colombia_rotary_wing_training_1666k_2011). Signed 2011-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127809D0077_9700/.",
    "USASpending: estudios_colombia_rotary_wing_training_1666k_2011 USD 1.666m. Supports estudios_colombia_rotary_wing_training_1666k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1666121.61; date_signed 2011-09-30.",
    investment_type="epc",
)

# === Cycle 1331 ===
row_doc(
    "estudios_costarica_cn_barracks_flamingo_1531k_2012",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Costa Rica CN barracks and operations center Flamingo",
    "Costa Rica",
    "20 Sep 2012: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for CN barracks and operations center Flamingo; obligated USD 1531036.27. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1531036.27", "2012-09-20", "2012", "", "",
    "CN BARRACKS&OPERATIONS CENTER FLAMINGO, COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_costarica_cn_barracks_flamingo_1531k_2012",
    "CN BARRACKS&OPERATIONS CENTER FLAMINGO, COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127811D0050_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1331",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0007_9700_W9127811D0050_9700 (estudios_costarica_cn_barracks_flamingo_1531k_2012). Signed 2012-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127811D0050_9700/.",
    "USASpending: estudios_costarica_cn_barracks_flamingo_1531k_2012 USD 1.531m. Supports estudios_costarica_cn_barracks_flamingo_1531k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1531036.27; date_signed 2012-09-20.",
    investment_type="epc",
)

# === Cycle 1332 ===
row_doc(
    "alutiiq_colombia_prefabricated_containers_1149k_2019",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Colombia prefabricated containers",
    "Colombia",
    "26 Nov 2019: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for delivery order 18 prefabricated containers; obligated USD 1149255.02. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1149255.02", "2019-11-26", "2019", "", "",
    "PRE-FABRICATED CONTAINERS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_colombia_prefabricated_containers_1149k_2019",
    "INL BOGOTA ERADICATION SUPPORT IDIQ - ALUTIIQ ESSENTIAL SERVICES - DELIVERY ORDER 18: PRE-FABRICATED CONTAINERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F0192_1900_19AQMM19D0050_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1332",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F0192_1900_19AQMM19D0050_1900 (alutiiq_colombia_prefabricated_containers_1149k_2019). Signed 2019-11-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F0192_1900_19AQMM19D0050_1900/.",
    "USASpending: alutiiq_colombia_prefabricated_containers_1149k_2019 USD 1.149m. Supports alutiiq_colombia_prefabricated_containers_1149k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1149255.02; date_signed 2019-11-26.",
    investment_type="equipment_supply",
)

# === Cycle 1332 ===
row_doc(
    "alutiiq_mexico_inami_biometric_19061k_2010",
    "infrastructure", "building_materials", "us",
    "Alutiiq 3SG — Mexico INAMI biometric capacity building",
    "Mexico",
    "14 Dec 2010: Department of State awards contract to ALUTIIQ 3SG, LLC for INAMI biometric capacity building project; obligated USD 19060548.39. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "19060548.39", "2010-12-14", "2010", "", "",
    "INAMI BIOMETRIC CAPACITY BUILDING PROJECT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_inami_biometric_19061k_2010",
    "INAMI BIOMETRIC CAPACITY BUILDING PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11C0001_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ 3SG, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1332",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC11C0001_1900_-NONE-_-NONE- (alutiiq_mexico_inami_biometric_19061k_2010). Signed 2010-12-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11C0001_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_inami_biometric_19061k_2010 USD 19.061m. Supports alutiiq_mexico_inami_biometric_19061k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19060548.39; date_signed 2010-12-14.",
    investment_type="equipment_supply",
)

# === Cycle 1332 ===
row_doc(
    "eterna_honduras_continuing_education_1430k_2016",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras Soto Cano continuing education facility",
    "Honduras",
    "15 Sep 2016: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for SOFA agreement continuing education facility Soto Cano; obligated USD 1430367.37. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1430367.37", "2016-09-15", "2016", "", "",
    "SOFA AGREEMENT CONTINUING EDUCATION FACILITY, SOTO CANO, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_continuing_education_1430k_2016",
    "IGF::OT::IGF SOFA AGREEMENT CONTINUING EDUCATION FACILITY, SOTO CANO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0023_9700_W9127813D0020_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1332",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0023_9700_W9127813D0020_9700 (eterna_honduras_continuing_education_1430k_2016). Signed 2016-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0023_9700_W9127813D0020_9700/.",
    "USASpending: eterna_honduras_continuing_education_1430k_2016 USD 1.430m. Supports eterna_honduras_continuing_education_1430k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1430367.37; date_signed 2016-09-15.",
    investment_type="epc",
)

# === Cycle 1332 ===
row_doc(
    "eterna_honduras_hamra_landing_zone_1374k_2011",
    "infrastructure", "bridges_roads", "other",
    "Empresa Eterna — Honduras Soto Cano HAMRA landing zone phase II and taxiway",
    "Honduras",
    "30 Sep 2011: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for construction of HAMRA resurface landing zone phase II and taxiway Soto Cano; obligated USD 1374196.05. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1374196.05", "2011-09-30", "2011", "", "",
    "CONSTRUCTION OF HAMRA RESURFACE LANDING ZONE PHASE II AND TAXIWAY, SOTO CANO AIR BASE, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_hamra_landing_zone_1374k_2011",
    "TAS::57 3400::TAS  CONSTRUCTION OF HAMRA RESURFACE  LANDING ZONE PHASE II AND TAXIWAY, SOTO CANO AIR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0013_9700_W9127811D0046_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1332",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0013_9700_W9127811D0046_9700 (eterna_honduras_hamra_landing_zone_1374k_2011). Signed 2011-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0013_9700_W9127811D0046_9700/.",
    "USASpending: eterna_honduras_hamra_landing_zone_1374k_2011 USD 1.374m. Supports eterna_honduras_hamra_landing_zone_1374k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1374196.05; date_signed 2011-09-30.",
    investment_type="epc",
)

# === Cycle 1332 ===
row_doc(
    "estudios_colombia_training_flandes_1364k_2012",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Colombia Flandes training facility",
    "Colombia",
    "21 Sep 2012: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for training facility Flandes; obligated USD 1363942.93. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1363942.93", "2012-09-21", "2012", "", "",
    "TRAINING FACILITY FLANDES, COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_training_flandes_1364k_2012",
    "TRAINING FACILITY FLANDES, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0012_9700_W9127809D0077_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1332",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0012_9700_W9127809D0077_9700 (estudios_colombia_training_flandes_1364k_2012). Signed 2012-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0012_9700_W9127809D0077_9700/.",
    "USASpending: estudios_colombia_training_flandes_1364k_2012 USD 1.364m. Supports estudios_colombia_training_flandes_1364k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1363942.93; date_signed 2012-09-21.",
    investment_type="epc",
)

# === Cycle 1333 ===
row_doc(
    "isobox_panama_mobile_container_office_90k_2022",
    "infrastructure", "building_materials", "us",
    "IsoBOX — Panama mobile container office space",
    "Panama",
    "10 Mar 2022: Department of State awards contract to ISOBOX INC for mobile container office space; obligated USD 89547.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "89547.00", "2022-03-10", "2022", "", "",
    "MOBILE CONTAINER OFFICE SPACE, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_isobox_panama_mobile_container_office_90k_2022",
    "MOBILE CONTAINER OFFICE SPACE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0722P0257_1900_-NONE-_-NONE-/",
    "Actor: ISOBOX INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1333",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0722P0257_1900_-NONE-_-NONE- (isobox_panama_mobile_container_office_90k_2022). Signed 2022-03-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0722P0257_1900_-NONE-_-NONE-/.",
    "USASpending: isobox_panama_mobile_container_office_90k_2022 USD 0.090m. Supports isobox_panama_mobile_container_office_90k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 89547.0; date_signed 2022-03-10.",
    investment_type="equipment_supply",
)

# === Cycle 1333 ===
row_doc(
    "isobox_panama_container_living_units_67k_2024",
    "infrastructure", "building_materials", "us",
    "IsoBOX — Panama portable temporary container living units",
    "Panama",
    "23 Aug 2024: Department of State awards contract to ISOBOX INC for portable temporary container living units; obligated USD 67355.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "67355.00", "2024-08-23", "2024", "", "",
    "PORTABLE TEMPORARY CONTAINER LIVING UNITS, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_isobox_panama_container_living_units_67k_2024",
    "PORTABLE TEMPORARY CONTAINER LIVING UNITS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0724P0841_1900_-NONE-_-NONE-/",
    "Actor: ISOBOX INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1333",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0724P0841_1900_-NONE-_-NONE- (isobox_panama_container_living_units_67k_2024). Signed 2024-08-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0724P0841_1900_-NONE-_-NONE-/.",
    "USASpending: isobox_panama_container_living_units_67k_2024 USD 0.067m. Supports isobox_panama_container_living_units_67k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 67355.0; date_signed 2024-08-23.",
    investment_type="equipment_supply",
)

# === Cycle 1333 ===
row_doc(
    "eterna_honduras_booster_pump_1318k_2016",
    "infrastructure", "water", "other",
    "Empresa Eterna — Honduras Soto Cano booster pump",
    "Honduras",
    "23 Sep 2016: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for SOFA agreement booster pump; obligated USD 1317563.92. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1317563.92", "2016-09-23", "2016", "", "",
    "SOFA AGREEMENT BOOSTER PUMP, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_booster_pump_1318k_2016",
    "IGF::OT::IGF SOFA AGREEMENT BOOSTER PUMP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1333",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127816D0102_9700 (eterna_honduras_booster_pump_1318k_2016). Signed 2016-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_booster_pump_1318k_2016 USD 1.318m. Supports eterna_honduras_booster_pump_1318k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1317563.92; date_signed 2016-09-23.",
    investment_type="epc",
)

# === Cycle 1333 ===
row_doc(
    "eterna_honduras_guanaja_cn_facility_1253k_2010",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras Guanaja CN facility design-build",
    "Honduras",
    "9 Jun 2010: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for design build CN facility Guanaja; obligated USD 1253184.01. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1253184.01", "2010-06-09", "2010", "", "",
    "DESIGN BUILD CN FACILITY, GUANAJA, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_guanaja_cn_facility_1253k_2010",
    "DESIGN BUILD CN FACILILTY, GUANAJA, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127809D0071_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1333",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0007_9700_W9127809D0071_9700 (eterna_honduras_guanaja_cn_facility_1253k_2010). Signed 2010-06-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_W9127809D0071_9700/.",
    "USASpending: eterna_honduras_guanaja_cn_facility_1253k_2010 USD 1.253m. Supports eterna_honduras_guanaja_cn_facility_1253k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1253184.01; date_signed 2010-06-09.",
    investment_type="epc",
)

# === Cycle 1333 ===
row_doc(
    "eterna_costarica_cn_pier_boat_ramp_1214k_2012",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Costa Rica CN pier and boat ramp",
    "Costa Rica",
    "18 Sep 2012: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for CN pier and boat ramp Costa Rica; obligated USD 1213545.75. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1213545.75", "2012-09-18", "2012", "", "",
    "CN PIER&BOAT RAMP COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_costarica_cn_pier_boat_ramp_1214k_2012",
    "CN PIER&BOAT RAMP COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0015_9700_W9127811D0046_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1333",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0015_9700_W9127811D0046_9700 (eterna_costarica_cn_pier_boat_ramp_1214k_2012). Signed 2012-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0015_9700_W9127811D0046_9700/.",
    "USASpending: eterna_costarica_cn_pier_boat_ramp_1214k_2012 USD 1.214m. Supports eterna_costarica_cn_pier_boat_ramp_1214k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1213545.75; date_signed 2012-09-18.",
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
