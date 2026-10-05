#!/usr/bin/env python3
"""Cycles 1339–1342: USASpending LatAm CapEx (Hardline/Mesan/Viken/Fidelitad/Alutiiq + Eterna/Estudios/Marago/Proyectos/Palgag EPC).

Seeds: 20262339–20262342. Thin top-up dry.
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

# === Cycle 1339 ===
row_doc(
    "hardline_peru_lima_febr_install_3968k_2015",
    "infrastructure", "building_materials", "us",
    "Hardline Nati Construction — Peru Lima embassy FE/BR doors and windows",
    "Peru",
    "16 Dec 2015: Department of State awards contract to HARDLINE NATI CONSTRUCTION LLC for FE/BR R&R project US Embassy Lima Peru install 48 FE/BR doors, 86 FE/BR window units, two glazing panels; obligated USD 3968035.55. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3968035.55", "2015-12-16", "2015", "", "",
    "FEBR R&R PROJECT - US EMBASSY LIMA, PERU, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hardline_peru_lima_febr_install_3968k_2015",
    "IGF::OT::IGF HNC - SAQMMA14D0085 - TO:SAQMMA16F0335 - FEBR R&R PROJECT -  US EMBASSY LIMA, PERU.  INSTALL 48 FE/BR DOORS, 86 FE/BR WINDOW UNITS, TWO GLAZING PANELS IN THE CHANCERY, ANNEX, AND CAC BUILDINGS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F0335_1900_SAQMMA14D0085_1900/",
    "Actor: HARDLINE NATI CONSTRUCTION LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1339",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F0335_1900_SAQMMA14D0085_1900 (hardline_peru_lima_febr_install_3968k_2015). Signed 2015-12-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F0335_1900_SAQMMA14D0085_1900/.",
    "USASpending: hardline_peru_lima_febr_install_3968k_2015 USD 3.968m. Supports hardline_peru_lima_febr_install_3968k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3968035.55; date_signed 2015-12-16.",
    investment_type="epc",
)

# === Cycle 1339 ===
row_doc(
    "mesan_mexico_las_bombas_renovation_1992k_2011",
    "infrastructure", "building_materials", "us",
    "Mesan-Martinez JV — Mexico Las Bombas design and construction renovations",
    "Mexico",
    "19 May 2011: Department of State awards contract to MESAN-MARTINEZ JOINT VENTURE LLP for design and construction renovations Las Bombas Mexico; obligated USD 1991755.17. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1991755.17", "2011-05-19", "2011", "", "",
    "DESIGN AND CONSTRUCTION RENOVATIONS LAS BOMBAS, MEXICO, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mesan_mexico_las_bombas_renovation_1992k_2011",
    "THE CONTRACTOR SHALL PROVIDE ALL PLANT, LABOR, MATERIALS, ETC. NECESSARY TO DESIGN AND CONSTRUCTION RENOVATIONS TO THE PROJECT IDENTIFIED AS LAS BOMBAS, MEXICO.  ALL WORK IS BEING ACCOMPLISHED AS PART OF THE US/MEXICO INTERNATIONAL COUNTER-NARCOTIC I",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11F0055_1900_SAQMMA08D0015_1900/",
    "Actor: MESAN-MARTINEZ JOINT VENTURE LLP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1339",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC11F0055_1900_SAQMMA08D0015_1900 (mesan_mexico_las_bombas_renovation_1992k_2011). Signed 2011-05-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11F0055_1900_SAQMMA08D0015_1900/.",
    "USASpending: mesan_mexico_las_bombas_renovation_1992k_2011 USD 1.992m. Supports mesan_mexico_las_bombas_renovation_1992k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1991755.17; date_signed 2011-05-19.",
    investment_type="epc",
)

# === Cycle 1339 ===
row_doc(
    "eterna_elsalvador_gym_shelter_734k_2012",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — El Salvador gym-shelter",
    "El Salvador",
    "30 Sep 2012: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for gym-shelter El Salvador; obligated USD 734001.37. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "734001.37", "2012-09-30", "2012", "", "",
    "GYM-SHELTER EL SALVADOR, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_elsalvador_gym_shelter_734k_2012",
    "GYM-SHELTER EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127809D0066_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1339",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127809D0066_9700 (eterna_elsalvador_gym_shelter_734k_2012). Signed 2012-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127809D0066_9700/.",
    "USASpending: eterna_elsalvador_gym_shelter_734k_2012 USD 0.734m. Supports eterna_elsalvador_gym_shelter_734k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 734001.37; date_signed 2012-09-30.",
    investment_type="epc",
)

# === Cycle 1339 ===
row_doc(
    "palgag_guatemala_fen_barracks_732k_2016",
    "infrastructure", "building_materials", "other",
    "Palgag Building Technologies — Guatemala FEN barracks",
    "Guatemala",
    "28 Sep 2016: Department of State awards contract to PALGAG BUILDING TECHNOLOGIES LTD for SOFA agreement FEN barracks; obligated USD 732307.59. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "732307.59", "2016-09-28", "2016", "", "",
    "SOFA AGREEMENT FEN BARRACKS, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_palgag_guatemala_fen_barracks_732k_2016",
    "IGF::OT::IGF SOFA AGREEMENT FEN BARRACKS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127816D0101_9700/",
    "Actor: PALGAG BUILDING TECHNOLOGIES LTD — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1339",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127816D0101_9700 (palgag_guatemala_fen_barracks_732k_2016). Signed 2016-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127816D0101_9700/.",
    "USASpending: palgag_guatemala_fen_barracks_732k_2016 USD 0.732m. Supports palgag_guatemala_fen_barracks_732k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 732307.59; date_signed 2016-09-28.",
    investment_type="epc",
)

# === Cycle 1339 ===
row_doc(
    "marago_colombia_caucasia_eradication_base_715k_2018",
    "infrastructure", "building_materials", "other",
    "Constructora Marago — Colombia CNP manual eradication base Caucasia",
    "Colombia",
    "19 Sep 2018: Department of State awards contract to CONSTRUCTORA MARAGO S A S for construction of CNP manual eradication base Caucasia; obligated USD 714664.85. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "714664.85", "2018-09-19", "2018", "", "",
    "CONSTRUCTION OF THE CNP MANUAL ERADICATION BASE - CAUCASIA, COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_marago_colombia_caucasia_eradication_base_715k_2018",
    "CONSTRUCTION OF THE CNP MANUAL ERADICATION BASE - CAUCASIA, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0189_1900_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA MARAGO S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1339",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0189_1900_-NONE-_-NONE- (marago_colombia_caucasia_eradication_base_715k_2018). Signed 2018-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0189_1900_-NONE-_-NONE-/.",
    "USASpending: marago_colombia_caucasia_eradication_base_715k_2018 USD 0.715m. Supports marago_colombia_caucasia_eradication_base_715k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 714664.85; date_signed 2018-09-19.",
    investment_type="epc",
)

# === Cycle 1340 ===
row_doc(
    "viken_ecuador_handheld_xray_scanners_182k_2023",
    "infrastructure", "engineering_epc", "us",
    "Viken Detection — Ecuador handheld x-ray scanners Quito",
    "Ecuador",
    "6 Jul 2023: Department of State awards contract to VIKEN DETECTION CORPORATION for acquisition of handheld x-ray scanners U.S. Embassy Quito; obligated USD 181650.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "181650.00", "2023-07-06", "2023", "", "",
    "ACQUISITION OF HANDHELD X-RAY SCANNERS ON BEHALF OF U.S. EMBASSY QUITO, ECUADOR, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_viken_ecuador_handheld_xray_scanners_182k_2023",
    "ACQUISITION OF HANDHELD X-RAY SCANNERS ON BEHALF OF U.S. EMBASSY QUITO, ECUADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023P0097_1900_-NONE-_-NONE-/",
    "Actor: VIKEN DETECTION CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1340",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5023P0097_1900_-NONE-_-NONE- (viken_ecuador_handheld_xray_scanners_182k_2023). Signed 2023-07-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023P0097_1900_-NONE-_-NONE-/.",
    "USASpending: viken_ecuador_handheld_xray_scanners_182k_2023 USD 0.182m. Supports viken_ecuador_handheld_xray_scanners_182k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 181650.0; date_signed 2023-07-06.",
    investment_type="equipment_supply",
)

# === Cycle 1340 ===
row_doc(
    "viken_ecuador_handheld_scanners_167k_2023",
    "infrastructure", "engineering_epc", "us",
    "Viken Detection — Ecuador handheld scanners",
    "Ecuador",
    "20 Feb 2023: Department of State awards contract to VIKEN DETECTION CORPORATION for handheld scanners; obligated USD 167260.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "167260.00", "2023-02-20", "2023", "", "",
    "HANDHELD SCANNERS, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_viken_ecuador_handheld_scanners_167k_2023",
    "HANDHELD SCANNERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P0415_1900_-NONE-_-NONE-/",
    "Actor: VIKEN DETECTION CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1340",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7523P0415_1900_-NONE-_-NONE- (viken_ecuador_handheld_scanners_167k_2023). Signed 2023-02-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7523P0415_1900_-NONE-_-NONE-/.",
    "USASpending: viken_ecuador_handheld_scanners_167k_2023 USD 0.167m. Supports viken_ecuador_handheld_scanners_167k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 167260.0; date_signed 2023-02-20.",
    investment_type="equipment_supply",
)

# === Cycle 1340 ===
row_doc(
    "estudios_paraguay_eoc_warehouses_706k_2011",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Paraguay DR EOC and warehouses",
    "Paraguay",
    "22 Sep 2011: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for design build of DR EOC and warehouse San Ignacio and DR warehouse Santa Rosa; obligated USD 705891.15. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "705891.15", "2011-09-22", "2011", "", "",
    "DESIGN BUILD OF DR EOC AND WAREHOUSE, SAN IGNACIO AND DR WAREHOUSE, SANTA ROSA, Paraguay (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_paraguay_eoc_warehouses_706k_2011",
    "TAS::97 0819::TAS DESIGN BUILD OF DR EOC AND WAREHOUSE, SAN IGNACIO AND DR WAREHOUSE, SANTA ROS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127809D0077_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1340",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0006_9700_W9127809D0077_9700 (estudios_paraguay_eoc_warehouses_706k_2011). Signed 2011-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127809D0077_9700/.",
    "USASpending: estudios_paraguay_eoc_warehouses_706k_2011 USD 0.706m. Supports estudios_paraguay_eoc_warehouses_706k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 705891.15; date_signed 2011-09-22.",
    investment_type="epc",
)

# === Cycle 1340 ===
row_doc(
    "proyectos_colombia_esgac_lodging_703k_2023",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia ESGAC lodging building",
    "Colombia",
    "23 May 2023: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for ESGAC lodging building; obligated USD 702667.50. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "702667.50", "2023-05-23", "2023", "", "",
    "ESGAC LODGING BUILDING, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_esgac_lodging_703k_2023",
    "ESGAC LODGING BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1079_1900_19AQMM21D0039_1900/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1340",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F1079_1900_19AQMM21D0039_1900 (proyectos_colombia_esgac_lodging_703k_2023). Signed 2023-05-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1079_1900_19AQMM21D0039_1900/.",
    "USASpending: proyectos_colombia_esgac_lodging_703k_2023 USD 0.703m. Supports proyectos_colombia_esgac_lodging_703k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 702667.5; date_signed 2023-05-23.",
    investment_type="epc",
)

# === Cycle 1340 ===
row_doc(
    "eterna_honduras_asa_hq_facility_695k_2012",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras ASA/228th HQ facility Soto Cano",
    "Honduras",
    "26 Sep 2012: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for ASA/228th HQ facility Soto Cano; obligated USD 694822.73. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "694822.73", "2012-09-26", "2012", "", "",
    "ASA/228TH HQ FACILITY SOTO CANO, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_asa_hq_facility_695k_2012",
    "ASA/228TH HQ FACILITY SOTO CANO, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0018_9700_W9127811D0046_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1340",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0018_9700_W9127811D0046_9700 (eterna_honduras_asa_hq_facility_695k_2012). Signed 2012-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0018_9700_W9127811D0046_9700/.",
    "USASpending: eterna_honduras_asa_hq_facility_695k_2012 USD 0.695m. Supports eterna_honduras_asa_hq_facility_695k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 694822.73; date_signed 2012-09-26.",
    investment_type="epc",
)

# === Cycle 1341 ===
row_doc(
    "fidelitad_colombia_la_macarena_it_152k_2011",
    "infrastructure", "building_materials", "us",
    "Fidelitad — Colombia La Macarena IT equipment",
    "Colombia",
    "30 Aug 2011: Department of State awards contract to FIDELITAD, INC. for IT equipment for La Macarena; obligated USD 152000.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "152000.00", "2011-08-30", "2011", "", "",
    "IT EQUIPMENT FOR LA MACARENA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fidelitad_colombia_la_macarena_it_152k_2011",
    "IT EQUIPMENT FOR LA MACARENA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0219_9700_-NONE-_-NONE-/",
    "Actor: FIDELITAD, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1341",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11P0219_9700_-NONE-_-NONE- (fidelitad_colombia_la_macarena_it_152k_2011). Signed 2011-08-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0219_9700_-NONE-_-NONE-/.",
    "USASpending: fidelitad_colombia_la_macarena_it_152k_2011 USD 0.152m. Supports fidelitad_colombia_la_macarena_it_152k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 152000.0; date_signed 2011-08-30.",
    investment_type="equipment_supply",
)

# === Cycle 1341 ===
row_doc(
    "fidelitad_colombia_install_virs_vv_133k_2011",
    "infrastructure", "building_materials", "us",
    "Fidelitad — Colombia install VIRS and VV",
    "Colombia",
    "28 Sep 2011: Department of State awards contract to FIDELITAD, INC. for install VIRS&VV; obligated USD 132859.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "132859.00", "2011-09-28", "2011", "", "",
    "INSTALL VIRS&VV, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fidelitad_colombia_install_virs_vv_133k_2011",
    "INSTALL VIRS&VV",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0286_9700_-NONE-_-NONE-/",
    "Actor: FIDELITAD, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1341",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11P0286_9700_-NONE-_-NONE- (fidelitad_colombia_install_virs_vv_133k_2011). Signed 2011-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0286_9700_-NONE-_-NONE-/.",
    "USASpending: fidelitad_colombia_install_virs_vv_133k_2011 USD 0.133m. Supports fidelitad_colombia_install_virs_vv_133k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 132859.0; date_signed 2011-09-28.",
    investment_type="equipment_supply",
)

# === Cycle 1341 ===
row_doc(
    "proyectos_colombia_sibate_tactical_house_693k_2023",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia Sibate tactical house construction",
    "Colombia",
    "30 Jun 2023: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for tactical house Sibate construction; obligated USD 692523.25. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "692523.25", "2023-06-30", "2023", "", "",
    "TACTICAL HOUSE SIBATE CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_sibate_tactical_house_693k_2023",
    "TACTICAL HOUSE SIBATE CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1373_1900_19AQMM21D0039_1900/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1341",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F1373_1900_19AQMM21D0039_1900 (proyectos_colombia_sibate_tactical_house_693k_2023). Signed 2023-06-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1373_1900_19AQMM21D0039_1900/.",
    "USASpending: proyectos_colombia_sibate_tactical_house_693k_2023 USD 0.693m. Supports proyectos_colombia_sibate_tactical_house_693k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 692523.25; date_signed 2023-06-30.",
    investment_type="epc",
)

# === Cycle 1341 ===
row_doc(
    "eterna_honduras_facility_construction_689k_2014",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras facility construction",
    "Honduras",
    "28 Sep 2014: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for facility construction; obligated USD 689408.48. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "689408.48", "2014-09-28", "2014", "", "",
    "FACILITY CONSTRUCTION, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_facility_construction_689k_2014",
    "IGF::OT::IGF FACILITY CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127813D0020_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1341",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0011_9700_W9127813D0020_9700 (eterna_honduras_facility_construction_689k_2014). Signed 2014-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127813D0020_9700/.",
    "USASpending: eterna_honduras_facility_construction_689k_2014 USD 0.689m. Supports eterna_honduras_facility_construction_689k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 689408.48; date_signed 2014-09-28.",
    investment_type="epc",
)

# === Cycle 1341 ===
row_doc(
    "estudios_honduras_tecsa_building_681k_2011",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Honduras Soto Cano TECSA building",
    "Honduras",
    "29 Sep 2011: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for design build of TECSA building Soto Cano; obligated USD 681302.28. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "681302.28", "2011-09-29", "2011", "", "",
    "DESIGN BUILD OF TECSA BUILDING, SOTO CANO, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_honduras_tecsa_building_681k_2011",
    "TAS::21 2020::TAS DESIGN BUILD OF TECSA BUILDING, SOTO CANO, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127811D0050_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1341",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127811D0050_9700 (estudios_honduras_tecsa_building_681k_2011). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127811D0050_9700/.",
    "USASpending: estudios_honduras_tecsa_building_681k_2011 USD 0.681m. Supports estudios_honduras_tecsa_building_681k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 681302.28; date_signed 2011-09-29.",
    investment_type="epc",
)

# === Cycle 1342 ===
row_doc(
    "alutiiq_guatemala_high_speed_scanners_104k_2023",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Guatemala high-speed high-volume scanners",
    "Guatemala",
    "21 Dec 2023: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for INL Guatemala high speed high volume scanners for GSCJ; obligated USD 103787.59. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "103787.59", "2023-12-21", "2023", "", "",
    "INL GUATEMALA HIGH SPEED HIGH VOLUME SCANNERS FOR GSCJ, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_guatemala_high_speed_scanners_104k_2023",
    "INL GUATEMALA HIGH SPEED HIGH VOLUME SCANNERS FOR GSCJ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0090_1900_19AQMM20D0010_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1342",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24F0090_1900_19AQMM20D0010_1900 (alutiiq_guatemala_high_speed_scanners_104k_2023). Signed 2023-12-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0090_1900_19AQMM20D0010_1900/.",
    "USASpending: alutiiq_guatemala_high_speed_scanners_104k_2023 USD 0.104m. Supports alutiiq_guatemala_high_speed_scanners_104k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 103787.59; date_signed 2023-12-21.",
    investment_type="equipment_supply",
)

# === Cycle 1342 ===
row_doc(
    "mesan_mexico_dinamarca_construction_75k_2012",
    "infrastructure", "building_materials", "us",
    "Mesan-Martinez JV — Mexico Dinamarca construction project",
    "Mexico",
    "28 Sep 2012: Department of State awards contract to MESAN-MARTINEZ JOINT VENTURE LLP for Dinamarca construction project in Mexico; obligated USD 75000.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "75000.00", "2012-09-28", "2012", "", "",
    "DINAMARCA CONSTRUCTION PROJECT IN MEXICO, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mesan_mexico_dinamarca_construction_75k_2012",
    "DINAMARCA CONSTRUCTION PROJECT IN MEXICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC12F0043_1900_SAQMMA08D0015_1900/",
    "Actor: MESAN-MARTINEZ JOINT VENTURE LLP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1342",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC12F0043_1900_SAQMMA08D0015_1900 (mesan_mexico_dinamarca_construction_75k_2012). Signed 2012-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC12F0043_1900_SAQMMA08D0015_1900/.",
    "USASpending: mesan_mexico_dinamarca_construction_75k_2012 USD 0.075m. Supports mesan_mexico_dinamarca_construction_75k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 75000.0; date_signed 2012-09-28.",
    investment_type="epc",
)

# === Cycle 1342 ===
row_doc(
    "eterna_honduras_officers_quadruplex_10b_680k_2010",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras Soto Cano officers quadruplex FY-10B",
    "Honduras",
    "28 Sep 2010: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D/B officer's quadruplex FY-10B Soto Cano AB; obligated USD 680199.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "680199.00", "2010-09-28", "2010", "", "",
    "D/B OFFICER'S QUDRUPLEX FY-10B, SOTO CANO AB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_officers_quadruplex_10b_680k_2010",
    "D/B OFFICER'S QUDRUPLEX FY-10B, SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0018_9700_W9127809D0071_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1342",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0018_9700_W9127809D0071_9700 (eterna_honduras_officers_quadruplex_10b_680k_2010). Signed 2010-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0018_9700_W9127809D0071_9700/.",
    "USASpending: eterna_honduras_officers_quadruplex_10b_680k_2010 USD 0.680m. Supports eterna_honduras_officers_quadruplex_10b_680k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 680199.0; date_signed 2010-09-28.",
    investment_type="epc",
)

# === Cycle 1342 ===
row_doc(
    "eterna_honduras_officers_quadruplex_units_680k_2010",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras Soto Cano officers quadruplex housing units",
    "Honduras",
    "28 Sep 2010: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D/B officers quadruplex housing units Soto Cano AB; obligated USD 680199.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "680199.00", "2010-09-28", "2010", "", "",
    "D/B OFFICERS QUDRUPLEX HOUSING UNITS, SOTO CANO AB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_officers_quadruplex_units_680k_2010",
    "D/B OFFICERS QUDRUPLEX HOUSING UNITS, SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0016_9700_W9127809D0071_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1342",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0016_9700_W9127809D0071_9700 (eterna_honduras_officers_quadruplex_units_680k_2010). Signed 2010-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0016_9700_W9127809D0071_9700/.",
    "USASpending: eterna_honduras_officers_quadruplex_units_680k_2010 USD 0.680m. Supports eterna_honduras_officers_quadruplex_units_680k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 680199.0; date_signed 2010-09-28.",
    investment_type="epc",
)

# === Cycle 1342 ===
row_doc(
    "eterna_belize_boat_maintenance_facility_678k_2013",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Belize boat maintenance facility construction",
    "Belize",
    "25 Sep 2013: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for construction boat maintenance facility Belize; obligated USD 677500.16. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "677500.16", "2013-09-25", "2013", "", "",
    "CONSTRUCTION BOAT MAINTENANCE FACILITY BELIZE, Belize (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_belize_boat_maintenance_facility_678k_2013",
    "IGF::OT::IGF CONSTRUCTION BOAT MAINTENANCE FACILITY BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127813D0020_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1342",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0004_9700_W9127813D0020_9700 (eterna_belize_boat_maintenance_facility_678k_2013). Signed 2013-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127813D0020_9700/.",
    "USASpending: eterna_belize_boat_maintenance_facility_678k_2013 USD 0.678m. Supports eterna_belize_boat_maintenance_facility_678k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 677500.16; date_signed 2013-09-25.",
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
