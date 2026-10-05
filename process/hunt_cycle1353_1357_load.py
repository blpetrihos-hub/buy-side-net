#!/usr/bin/env python3
"""Cycles 1353–1357: USASpending LatAm CapEx (Obera/Virtra/FAAC/Leonardo/Proteus/Gemalto + Supera/Eterna EPC).

Seeds: 20262353–20262357. Thin top-up dry (nickel/balsa/fission_smr/niobium/graphite).
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

# === Cycle 1353 ===
row_doc(
    "obera_bahamas_bpc_equipment_1010k_2020",
    "infrastructure", "engineering_epc", "us",
    "Obera — Bahamas DoD BPC equipment procurement",
    "Bahamas",
    "30 Sep 2020: Department of Defense awards contract to OBERA LLC for equipment to build partner capacity (BPC) in Bahamas as part of the DoD Security Cooperation Program; obligated USD 1010174.85. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1010174.85", "2020-09-30", "2020", "", "",
    "THIS PROCUREMENT PROVIDES EQUIPMENT TO BUILD PARTNER CAPACITY (BPC) IN BAHAMAS AS PART OF , Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_obera_bahamas_bpc_equipment_1010k_2020",
    "THIS PROCUREMENT PROVIDES EQUIPMENT TO BUILD PARTNER CAPACITY (BPC) IN BAHAMAS AS PART OF THE DOD SECURITY COOPERATION PROGRAM.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489020F0119_9700_FA489016D0013_9700/",
    "Actor: OBERA LLC (U.S.) — us. Official USASpending Award API. Shuffle copper dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1353",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489020F0119_9700_FA489016D0013_9700 (obera_bahamas_bpc_equipment_1010k_2020). Signed 2020-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489020F0119_9700_FA489016D0013_9700/.",
    "USASpending: obera_bahamas_bpc_equipment_1010k_2020 USD 1.010m. Supports obera_bahamas_bpc_equipment_1010k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1010174.85; date_signed 2020-09-30.",
    investment_type="equipment_supply",
)

# === Cycle 1353 ===
row_doc(
    "virtra_costa_rica_training_simulator_955k_2024",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Costa Rica training simulator purchase",
    "Costa Rica",
    "10 Dec 2024: Department of State awards contract to VIRTRA, INC. for purchase of a training simulator supporting the U.S. Embassy in Costa Rica; obligated USD 955469.33. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "955469.33", "2024-12-10", "2024", "", "",
    "CONTRACT AWARD AWARD FOR THE PURCHASE OF A TRAINING SIMULATOR IN THE AMOUNT OF $948,615 IN, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_costa_rica_training_simulator_955k_2024",
    "CONTRACT AWARD AWARD FOR THE PURCHASE OF A TRAINING SIMULATOR IN THE AMOUNT OF $948,615 IN ADDITION TO TWO (02) OPTION YEAR RENEWALS SUPPORTING THE US EMBASSY IN COSTA RICA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE25C0019_1900_-NONE-_-NONE-/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle other_renewables dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1353",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE25C0019_1900_-NONE-_-NONE- (virtra_costa_rica_training_simulator_955k_2024). Signed 2024-12-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE25C0019_1900_-NONE-_-NONE-/.",
    "USASpending: virtra_costa_rica_training_simulator_955k_2024 USD 0.955m. Supports virtra_costa_rica_training_simulator_955k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 955469.33; date_signed 2024-12-10.",
    investment_type="equipment_supply",
)

# === Cycle 1353 ===
row_doc(
    "supera_brazil_construction_services_4586k_2023",
    "infrastructure", "building_materials", "other",
    "Supera Engenharia — Brazil construction services",
    "Brazil",
    "09 Jun 2023: Department of State awards contract to SUPERA ENGENHARIA LTDA for construction services in Brazil; obligated USD 4585525.93. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "4585525.93", "2023-06-09", "2023", "", "",
    "CONSTRUCTION SERVICES, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_supera_brazil_construction_services_4586k_2023",
    "CONSTRUCTION SERVICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0012_1900_-NONE-_-NONE-/",
    "Actor: SUPERA ENGENHARIA LTDA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1353",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5023C0012_1900_-NONE-_-NONE- (supera_brazil_construction_services_4586k_2023). Signed 2023-06-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0012_1900_-NONE-_-NONE-/.",
    "USASpending: supera_brazil_construction_services_4586k_2023 USD 4.586m. Supports supera_brazil_construction_services_4586k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4585525.93; date_signed 2023-06-09.",
    investment_type="epc",
)

# === Cycle 1353 ===
row_doc(
    "eterna_honduras_soto_cano_officers_quadruplex_675k_2010",
    "infrastructure", "building_materials", "other",
    "Eterna — Honduras Soto Cano officers quadruplex design-build",
    "Honduras",
    "FY-10: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D/B officers quadruplex at Soto Cano AB, Honduras; obligated USD 675313.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "675313.00", "2010-09-29", "2010", "", "",
    "D/B OFFICERS QUADRUPLEX FY-10DV, SOTO CANO AB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_soto_cano_officers_quadruplex_675k_2010",
    "D/B OFFICERS QUADRUPLEX FY-10DV, SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0020_9700_W9127809D0071_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1353",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0020_9700_W9127809D0071_9700 (eterna_honduras_soto_cano_officers_quadruplex_675k_2010). Signed 2010-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0020_9700_W9127809D0071_9700/.",
    "USASpending: eterna_honduras_soto_cano_officers_quadruplex_675k_2010 USD 0.675m. Supports eterna_honduras_soto_cano_officers_quadruplex_675k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 675313.00; date_signed 2010-09-29.",
    investment_type="epc",
)

# === Cycle 1353 ===
row_doc(
    "palgag_svg_canouan_coast_guard_ops_facility_2110k_2011",
    "infrastructure", "building_materials", "other",
    "Palgag Building Technologies — Canouan St. Vincent coast guard operations facility",
    "Saint Vincent and the Grenadines",
    "27 Sep 2011: Department of Defense awards contract to PALGAG BUILDING TECHNOLOGIES LTD for Coast Guard operations facility, Canouan, St. Vincent; obligated USD 2109543.52. CapEx face = award obligation. Exact site coords not stated — lat/lon blank. Place-of-performance country field lists Netherlands; named asset site is Canouan, Saint Vincent and the Grenadines.",
    "2109543.52", "2011-09-27", "2011", "", "",
    "COAST GUARD OPERATIONS FACILITY, CANOUAN, ST. VINCENT, Saint Vincent and the Grenadines (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_palgag_svg_canouan_coast_guard_ops_facility_2110k_2011",
    "COAST GUARD OPERATIONS FACILITY, CANOUAN, ST. VINCENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0074_9700_-NONE-_-NONE-/",
    "Actor: PALGAG BUILDING TECHNOLOGIES LTD — other. Official USASpending Award API. Shuffle building_materials CapEx. Named site Canouan SVG (not U.S. territory).",
    "hunt_cycle1353",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945011C0074_9700_-NONE-_-NONE- (palgag_svg_canouan_coast_guard_ops_facility_2110k_2011). Signed 2011-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0074_9700_-NONE-_-NONE-/.",
    "USASpending: palgag_svg_canouan_coast_guard_ops_facility_2110k_2011 USD 2.110m. Supports palgag_svg_canouan_coast_guard_ops_facility_2110k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2109543.52; date_signed 2011-09-27.",
    investment_type="epc",
)


# === Cycle 1354 ===
row_doc(
    "virtra_mexico_puebla_morelos_cdmx_simulators_929k_2016",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico Puebla/Morelos/CDMX/Mexico State firearm training simulators",
    "Mexico",
    "05 Jul 2016: Department of State awards contract to VIRTRA, INC. for firearm training simulators for Puebla, Morelos, Mexico City, and Mexico State police academies including installation; obligated USD 929121.01. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "929121.01", "2016-07-05", "2016", "", "",
    "INL MEXICO - FIREARM TRAINING SIMULATORS FOR THE PUEBLA, MORELOS, MEXICO CITY, AND MEXICO , Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_puebla_morelos_cdmx_simulators_929k_2016",
    "INL MEXICO - FIREARM TRAINING SIMULATORS FOR THE PUEBLA, MORELOS, MEXICO CITY, AND MEXICO STATE POLICE ACADEMIES. INCLUDES INSTALLATION AND 3-YEAR IN-COUNTRY WARRANTY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0021_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle port_ownership dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1354",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16F0021_1900_SWHARC16D0003_1900 (virtra_mexico_puebla_morelos_cdmx_simulators_929k_2016). Signed 2016-07-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0021_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_puebla_morelos_cdmx_simulators_929k_2016 USD 0.929m. Supports virtra_mexico_puebla_morelos_cdmx_simulators_929k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 929121.01; date_signed 2016-07-05.",
    investment_type="equipment_supply",
)

# === Cycle 1354 ===
row_doc(
    "faac_mexico_chiapas_colima_jalisco_simulators_919k_2017",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico Chiapas/Colima/Jalisco/Oaxaca/SLP fixed and portable firearms simulators",
    "Mexico",
    "29 Jun 2017: Department of State awards contract to FAAC INCORPORATED for fixed and portable firearms training simulators for Chiapas, Colima, Jalisco, Oaxaca, and San Luis Potosi; obligated USD 918714.96. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "918714.96", "2017-06-29", "2017", "", "",
    "INL MEXICO FIXED AND PORTABLE FIREARMS TRAINING SIMULATORS FOR THE CHIAPAS, COLIMA, JALISC, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_chiapas_colima_jalisco_simulators_919k_2017",
    "INL MEXICO FIXED AND PORTABLE FIREARMS TRAINING SIMULATORS FOR THE CHIAPAS, COLIMA, JALISCO, OAXACA, AND SAN LUIS POTOSI STATE POLICE ACADEMIES. INCLUDES INSTALLATION AND 3-YEAR IN-COUNTRY WARRANTY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0022_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle building_materials→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1354",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC17F0022_1900_SWHARC16D0002_1900 (faac_mexico_chiapas_colima_jalisco_simulators_919k_2017). Signed 2017-06-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0022_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_chiapas_colima_jalisco_simulators_919k_2017 USD 0.919m. Supports faac_mexico_chiapas_colima_jalisco_simulators_919k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 918714.96; date_signed 2017-06-29.",
    investment_type="equipment_supply",
)

# === Cycle 1354 ===
row_doc(
    "eterna_colombia_azara_nursing_home_593k_2024",
    "infrastructure", "building_materials", "other",
    "Eterna — Colombia Azara nursing home Guaviare HAP design-construction",
    "Colombia",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for design and construction of Azara nursing home in Guaviare Colombia, HAP 70353; obligated USD 593218.62. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "593218.62", "2024-05-17", "2024", "", "",
    "DESIGN AND CONSTRUCTION OF AZARA NURSING HOME IN GUAVIARE COLOMBIA, HAP 70353., Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_colombia_azara_nursing_home_593k_2024",
    "DESIGN AND CONSTRUCTION OF AZARA NURSING HOME IN GUAVIARE COLOMBIA, HAP 70353.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0097_9700_W9127823D0059_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1354",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0097_9700_W9127823D0059_9700 (eterna_colombia_azara_nursing_home_593k_2024). Signed 2024-05-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0097_9700_W9127823D0059_9700/.",
    "USASpending: eterna_colombia_azara_nursing_home_593k_2024 USD 0.593m. Supports eterna_colombia_azara_nursing_home_593k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 593218.62; date_signed 2024-05-17.",
    investment_type="epc",
)

# === Cycle 1354 ===
row_doc(
    "eterna_guatemala_uhr_training_tower_589k_2019",
    "infrastructure", "building_materials", "other",
    "Eterna — Guatemala UHR training tower design-build",
    "Guatemala",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D&B UHR training tower proj no 37584; obligated USD 588996.67. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "588996.67", "2019-09-28", "2019", "", "",
    "D&B UHR TRAINING TOWER PROJ NO: 37584, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_guatemala_uhr_training_tower_589k_2019",
    "D&B UHR TRAINING TOWER PROJ NO: 37584",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0531_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1354",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0531_9700_W9127816D0102_9700 (eterna_guatemala_uhr_training_tower_589k_2019). Signed 2019-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0531_9700_W9127816D0102_9700/.",
    "USASpending: eterna_guatemala_uhr_training_tower_589k_2019 USD 0.589m. Supports eterna_guatemala_uhr_training_tower_589k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 588996.67; date_signed 2019-09-28.",
    investment_type="epc",
)

# === Cycle 1354 ===
row_doc(
    "eterna_guatemala_coban_medical_center_585k_2018",
    "infrastructure", "building_materials", "other",
    "Eterna — Guatemala Coban medical center design-construct",
    "Guatemala",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for design/construct Coban medical center; obligated USD 585000.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "585000.00", "2018-01-12", "2018", "", "",
    "DESIGN/CONSTRUCT COBAN MEDICAL CENTER, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_guatemala_coban_medical_center_585k_2018",
    "DESIGN/CONSTRUCT COBAN MEDICAL CENTER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0168_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1354",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0168_9700_W9127816D0102_9700 (eterna_guatemala_coban_medical_center_585k_2018). Signed 2018-01-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0168_9700_W9127816D0102_9700/.",
    "USASpending: eterna_guatemala_coban_medical_center_585k_2018 USD 0.585m. Supports eterna_guatemala_coban_medical_center_585k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 585000.00; date_signed 2018-01-12.",
    investment_type="epc",
)

# === Cycle 1355 ===
row_doc(
    "leonardo_panama_license_plate_readers_install_913k_2022",
    "infrastructure", "engineering_epc", "us",
    "Leonardo US — Panama license plate readers and installation",
    "Panama",
    "21 Sep 2022: Department of State awards contract to LEONARDO US CYBER AND SECURITY SOLUTIONS, LLC for license plate readers and installation services; obligated USD 913261.81. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "913261.81", "2022-09-21", "2022", "", "",
    "LICENSE PLATE READERS AND INSTALLATION SERVICES., Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_leonardo_panama_license_plate_readers_install_913k_2022",
    "LICENSE PLATE READERS AND INSTALLATION SERVICES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22C0005_1900_-NONE-_-NONE-/",
    "Actor: LEONARDO US CYBER AND SECURITY SOLUTIONS, LLC (U.S.) — us. Official USASpending Award API. Shuffle lithium dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1355",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE22C0005_1900_-NONE-_-NONE- (leonardo_panama_license_plate_readers_install_913k_2022). Signed 2022-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE22C0005_1900_-NONE-_-NONE-/.",
    "USASpending: leonardo_panama_license_plate_readers_install_913k_2022 USD 0.913m. Supports leonardo_panama_license_plate_readers_install_913k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 913261.81; date_signed 2022-09-21.",
    investment_type="equipment_supply",
)

# === Cycle 1355 ===
row_doc(
    "proteus_haiti_semi_permanent_building_850k_2010",
    "infrastructure", "building_materials", "us",
    "Proteus On-Demand Facilities — Haiti semi-permanent building for GOH",
    "Haiti",
    "04 Mar 2010: USAID awards contract to PROTEUS ON-DEMAND FACILITIES, LLC to purchase semi-permanent building for Government of Haiti; obligated USD 850000.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "850000.00", "2010-03-04", "2010", "", "",
    "THE PURPOSE OF THIS COMMERCIAL CONTRACT IS TO PURCHASE OF SEMI-PERMANENT BUILDING FOR GOH., Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proteus_haiti_semi_permanent_building_850k_2010",
    "THE PURPOSE OF THIS COMMERCIAL CONTRACT IS TO PURCHASE OF SEMI-PERMANENT BUILDING FOR GOH.TAS::72 1037::TAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C001000009_7200_-NONE-_-NONE-/",
    "Actor: PROTEUS ON-DEMAND FACILITIES, LLC (U.S.) — us. Official USASpending Award API. Shuffle copper dry→building_materials CapEx; ≥1/3 U.S.",
    "hunt_cycle1355",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521C001000009_7200_-NONE-_-NONE- (proteus_haiti_semi_permanent_building_850k_2010). Signed 2010-03-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C001000009_7200_-NONE-_-NONE-/.",
    "USASpending: proteus_haiti_semi_permanent_building_850k_2010 USD 0.850m. Supports proteus_haiti_semi_permanent_building_850k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 850000.00; date_signed 2010-03-04.",
    investment_type="epc",
)

# === Cycle 1355 ===
row_doc(
    "eterna_costa_rica_disaster_relief_warehouse_571k_2010",
    "infrastructure", "building_materials", "other",
    "Eterna — Costa Rica HAP 7595 disaster relief warehouse design-build",
    "Costa Rica",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D/B HAP 7595 disaster relief warehouse, Costa Rica; obligated USD 571170.44. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "571170.44", "2010-09-30", "2010", "", "",
    "D/B HAP 7595 DISASTER RELIEF WAREHOUSE, COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_costa_rica_disaster_relief_warehouse_571k_2010",
    "D/B HAP 7595 DISASTER RELIEF WAREHOUSE, COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0024_9700_W9127809D0071_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1355",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0024_9700_W9127809D0071_9700 (eterna_costa_rica_disaster_relief_warehouse_571k_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0024_9700_W9127809D0071_9700/.",
    "USASpending: eterna_costa_rica_disaster_relief_warehouse_571k_2010 USD 0.571m. Supports eterna_costa_rica_disaster_relief_warehouse_571k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 571170.44; date_signed 2010-09-30.",
    investment_type="epc",
)

# === Cycle 1355 ===
row_doc(
    "eterna_el_salvador_san_vicente_eoc_559k_2010",
    "infrastructure", "building_materials", "other",
    "Eterna — El Salvador San Vicente HAP 11039 EOC construction",
    "El Salvador",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for construction with incidental design of HAP 11039 EOC San Vicente, El Salvador; obligated USD 558805.71. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "558805.71", "2011-09-29", "2011", "", "",
    "CONSTRUCTION WITH INCIDENTAL DESIGN OF HAP 11039 EOC SAN VICENTE, EL SALVADOR, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_el_salvador_san_vicente_eoc_559k_2010",
    "TAS::97 0819::TAS CONSTRUCTION WITH INCIDENTAL DESIGN OF HAP 11039 EOC SAN VICENTE, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127809D0066_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1355",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127809D0066_9700 (eterna_el_salvador_san_vicente_eoc_559k_2010). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127809D0066_9700/.",
    "USASpending: eterna_el_salvador_san_vicente_eoc_559k_2010 USD 0.559m. Supports eterna_el_salvador_san_vicente_eoc_559k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 558805.71; date_signed 2011-09-29.",
    investment_type="epc",
)

# === Cycle 1355 ===
row_doc(
    "eterna_el_salvador_san_miguel_eoc_547k_2011",
    "infrastructure", "building_materials", "other",
    "Eterna — El Salvador San Miguel HAP 11037 EOC",
    "El Salvador",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for HAP 11037 EOC, San Miguel; obligated USD 546808.45. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "546808.45", "2011-09-29", "2011", "", "",
    "HAP 11037 EOC, SAN MIGUEL, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_el_salvador_san_miguel_eoc_547k_2011",
    "TAS::21 2050::TAS HAP 11037 EOC, SAN MIGUEL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127811D0046_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1355",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0010_9700_W9127811D0046_9700 (eterna_el_salvador_san_miguel_eoc_547k_2011). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0010_9700_W9127811D0046_9700/.",
    "USASpending: eterna_el_salvador_san_miguel_eoc_547k_2011 USD 0.547m. Supports eterna_el_salvador_san_miguel_eoc_547k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 546808.45; date_signed 2011-09-29.",
    investment_type="epc",
)

# === Cycle 1356 ===
row_doc(
    "faac_mexico_firearms_simulators_install_824k_2017",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico firearms training simulator systems with installation",
    "Mexico",
    "09 Aug 2017: Department of State awards contract to FAAC INCORPORATED for firearms training simulator systems including accessories, training, installation, and in-country support; obligated USD 824327.08. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "824327.08", "2017-08-09", "2017", "", "",
    "INL MEXICO - FIREARMS TRAINING SIMULATOR SYSTEMS (INCLUDING ACCESSORIES, TRAINING, INSTALL, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_firearms_simulators_install_824k_2017",
    "INL MEXICO - FIREARMS TRAINING SIMULATOR SYSTEMS (INCLUDING ACCESSORIES, TRAINING, INSTALLATION, AND IN-COUNTRY MAINTENANCE AND SUPPORT).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0027_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle lithium dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1356",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC17F0027_1900_SWHARC16D0002_1900 (faac_mexico_firearms_simulators_install_824k_2017). Signed 2017-08-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0027_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_firearms_simulators_install_824k_2017 USD 0.824m. Supports faac_mexico_firearms_simulators_install_824k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 824327.08; date_signed 2017-08-09.",
    investment_type="equipment_supply",
)

# === Cycle 1356 ===
row_doc(
    "faac_mexico_chihuahua_sonora_veracruz_simulators_815k_2017",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico Chihuahua/Sonora/Veracruz fixed and portable firearms simulators",
    "Mexico",
    "23 Mar 2017: Department of State awards contract to FAAC INCORPORATED for fixed and portable firearms training simulators for Chihuahua, Sonora, and Veracruz state police; obligated USD 815454.83. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "815454.83", "2017-03-23", "2017", "", "",
    "INL MEXICO FIXED AND PORTABLE FIREARMS TRAINING SIMULATORS FOR THE CHIHUAHUA, SONORA, AND , Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_chihuahua_sonora_veracruz_simulators_815k_2017",
    "INL MEXICO FIXED AND PORTABLE FIREARMS TRAINING SIMULATORS FOR THE CHIHUAHUA, SONORA, AND VERACRUZ STATE POLICE ACADEMIES. INCLUDES INSTALLATION AND 3-YEAR IN-COUNTRY WARRANTY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0002_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle rail dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1356",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC17F0002_1900_SWHARC16D0002_1900 (faac_mexico_chihuahua_sonora_veracruz_simulators_815k_2017). Signed 2017-03-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0002_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_chihuahua_sonora_veracruz_simulators_815k_2017 USD 0.815m. Supports faac_mexico_chihuahua_sonora_veracruz_simulators_815k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 815454.83; date_signed 2017-03-23.",
    investment_type="equipment_supply",
)

# === Cycle 1356 ===
row_doc(
    "eterna_el_salvador_santa_ana_eoc_544k_2010",
    "infrastructure", "building_materials", "other",
    "Eterna — El Salvador Santa Ana HAP 11040 EOC construction",
    "El Salvador",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for construction with incidental design of HAP 11040 EOC, Santa Ana, El Salvador; obligated USD 543746.18. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "543746.18", "2011-09-26", "2011", "", "",
    "CONSTRUCTION WITH INCIDENTAL DESIGN OF HAP 11040 EOC, SANTA ANA, EL SALVADOR, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_el_salvador_santa_ana_eoc_544k_2010",
    "TAS::97 0819::TAS CONSTRUCTION WITH INCIDENTAL DESIGN OF HAP 11040 EOC, SANTA ANA, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127809D0066_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1356",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127809D0066_9700 (eterna_el_salvador_santa_ana_eoc_544k_2010). Signed 2011-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127809D0066_9700/.",
    "USASpending: eterna_el_salvador_santa_ana_eoc_544k_2010 USD 0.544m. Supports eterna_el_salvador_santa_ana_eoc_544k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 543746.18; date_signed 2011-09-26.",
    investment_type="epc",
)

# === Cycle 1356 ===
row_doc(
    "eterna_costa_rica_limon_school_541k_2010",
    "infrastructure", "building_materials", "other",
    "Eterna — Costa Rica Limon HAP 7618 school design-build",
    "Costa Rica",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D/B HAP 7618 construct school, Limon, Costa Rica; obligated USD 540500.70. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "540500.70", "2010-09-29", "2010", "", "",
    "D/B HAP 7618 CONSTRUCT SCHOOL, LIMON, COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_costa_rica_limon_school_541k_2010",
    "D/B HAP 7618 CONSTRUCT SCHOOL, LIMON, COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0017_9700_W9127809D0071_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1356",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0017_9700_W9127809D0071_9700 (eterna_costa_rica_limon_school_541k_2010). Signed 2010-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0017_9700_W9127809D0071_9700/.",
    "USASpending: eterna_costa_rica_limon_school_541k_2010 USD 0.541m. Supports eterna_costa_rica_limon_school_541k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 540500.70; date_signed 2010-09-29.",
    investment_type="epc",
)

# === Cycle 1356 ===
row_doc(
    "eterna_guatemala_zacapa_medical_clinic_536k_2018",
    "infrastructure", "building_materials", "other",
    "Eterna — Guatemala Zacapa medical clinic",
    "Guatemala",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for Zacapa medical clinic; obligated USD 536366.05. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "536366.05", "2018-01-12", "2018", "", "",
    "ZACAPA MEDICAL CLINIC, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_guatemala_zacapa_medical_clinic_536k_2018",
    "ZACAPA MEDICAL CLINIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0163_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1356",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0163_9700_W9127816D0102_9700 (eterna_guatemala_zacapa_medical_clinic_536k_2018). Signed 2018-01-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0163_9700_W9127816D0102_9700/.",
    "USASpending: eterna_guatemala_zacapa_medical_clinic_536k_2018 USD 0.536m. Supports eterna_guatemala_zacapa_medical_clinic_536k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 536366.05; date_signed 2018-01-12.",
    investment_type="epc",
)

# === Cycle 1357 ===
row_doc(
    "gemalto_panama_afis_expand_update_787k_2013",
    "infrastructure", "engineering_epc", "us",
    "Gemalto Cogent — Panama AFIS expand and update",
    "Panama",
    "06 May 2013: Department of State awards contract to GEMALTO COGENT, INC. to expand and update capacity of an existing automated fingerprint identification system in Panama; obligated USD 787192.80. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "787192.80", "2013-05-06", "2013", "", "",
    "THE PROJECT IS DESIGNED TO EXPAND AND UPDATE THE CAPACITY AND CAPABILITY OF AN EXISTING AU, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_gemalto_panama_afis_expand_update_787k_2013",
    "THE PROJECT IS DESIGNED TO EXPAND AND UPDATE THE CAPACITY AND CAPABILITY OF AN EXISTING AUTOMATED FINGERPRINT IDENTIFICATION SYSTEM IN PANAMA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SINLEC13M0008_1900_-NONE-_-NONE-/",
    "Actor: GEMALTO COGENT, INC. (U.S.) — us. Official USASpending Award API. Shuffle wind dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1357",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SINLEC13M0008_1900_-NONE-_-NONE- (gemalto_panama_afis_expand_update_787k_2013). Signed 2013-05-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SINLEC13M0008_1900_-NONE-_-NONE-/.",
    "USASpending: gemalto_panama_afis_expand_update_787k_2013 USD 0.787m. Supports gemalto_panama_afis_expand_update_787k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 787192.80; date_signed 2013-05-06.",
    investment_type="equipment_supply",
)

# === Cycle 1357 ===
row_doc(
    "virtra_colombia_bogota_firearms_simulators_710k_2018",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Colombia Bogota fixed and portable firearms training simulators",
    "Colombia",
    "26 Jul 2018: Department of State awards contract to VIRTRA, INC. for 2 fixed and 2 portable firearms training simulators, recoil kits, and accessories for INL Bogota including installation; obligated USD 709882.68. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "709882.68", "2018-07-26", "2018", "", "",
    "INL BOGOTA - 2 FIXED AND 2 PORTABLE FIREARMS TRAINING SIMULATORS, RECOIL KITS, AND OTHER A, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_colombia_bogota_firearms_simulators_710k_2018",
    "INL BOGOTA - 2 FIXED AND 2 PORTABLE FIREARMS TRAINING SIMULATORS, RECOIL KITS, AND OTHER ACCESSORIES. INCLUDES INSTALLATION AND 3-YEAR IN-COUNTRY WARRANTY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F2482_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle fission_smr dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1357",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F2482_1900_SWHARC16D0003_1900 (virtra_colombia_bogota_firearms_simulators_710k_2018). Signed 2018-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F2482_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_colombia_bogota_firearms_simulators_710k_2018 USD 0.710m. Supports virtra_colombia_bogota_firearms_simulators_710k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 709882.68; date_signed 2018-07-26.",
    investment_type="equipment_supply",
)

# === Cycle 1357 ===
row_doc(
    "eterna_guatemala_elementary_school_521k_2017",
    "infrastructure", "building_materials", "other",
    "Eterna — Guatemala elementary school",
    "Guatemala",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for elementary school; obligated USD 521230.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "521230.00", "2017-09-30", "2017", "", "",
    "ELEMENTARY SCHOOL, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_guatemala_elementary_school_521k_2017",
    "IGF::OT::IGF ELEMENTARY SCHOOL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0508_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1357",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0508_9700_W9127816D0102_9700 (eterna_guatemala_elementary_school_521k_2017). Signed 2017-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0508_9700_W9127816D0102_9700/.",
    "USASpending: eterna_guatemala_elementary_school_521k_2017 USD 0.521m. Supports eterna_guatemala_elementary_school_521k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 521230.00; date_signed 2017-09-30.",
    investment_type="epc",
)

# === Cycle 1357 ===
row_doc(
    "eterna_colombia_tow_way_extension_505k_2022",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Colombia tow way extension design and construction",
    "Colombia",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for design and construction of tow way extension (CADD NO:SHA21004); obligated USD 505450.65. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "505450.65", "2022-02-07", "2022", "", "",
    "DESIGN AND CONSTRUCTION OF TOW WAY EXTENSION (CADD NO:SHA21004), Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_colombia_tow_way_extension_505k_2022",
    "DESIGN AND CONSTRUCTION OF TOW WAY EXTENSION (CADD NO:SHA21004)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0047_9700_W9127817D0095_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads CapEx.",
    "hunt_cycle1357",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0047_9700_W9127817D0095_9700 (eterna_colombia_tow_way_extension_505k_2022). Signed 2022-02-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0047_9700_W9127817D0095_9700/.",
    "USASpending: eterna_colombia_tow_way_extension_505k_2022 USD 0.505m. Supports eterna_colombia_tow_way_extension_505k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 505450.65; date_signed 2022-02-07.",
    investment_type="epc",
)

# === Cycle 1357 ===
row_doc(
    "eterna_belize_sco_annex_ladyville_411k_2024",
    "infrastructure", "building_materials", "other",
    "Eterna — Belize SCO annex building Ladyville",
    "Belize",
    "Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for SCO annex building Ladyville, Belize; obligated USD 410524.06. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "410524.06", "2024-09-30", "2024", "", "",
    "SCO ANNEX BUILDING LADYVILLE, BELIZE, Belize (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_belize_sco_annex_ladyville_411k_2024",
    "SCO ANNEX BUILDING LADYVILLE, BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0397_9700_W9127823D0073_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1357",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0397_9700_W9127823D0073_9700 (eterna_belize_sco_annex_ladyville_411k_2024). Signed 2024-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0397_9700_W9127823D0073_9700/.",
    "USASpending: eterna_belize_sco_annex_ladyville_411k_2024 USD 0.411m. Supports eterna_belize_sco_annex_ladyville_411k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 410524.06; date_signed 2024-09-30.",
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
