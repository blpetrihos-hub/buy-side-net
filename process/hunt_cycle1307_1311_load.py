#!/usr/bin/env python3
"""Cycles 1307–1311: USASpending LatAm CapEx (Cambridge MSS/radar + Alutiiq NG911/x-ray + misc).

Seeds: 20262307–20262311. Thin top-up dry.
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

# === Cycle 1307 ===
row_doc(
    "cambridge_bahamas_mss_towers_8978k_2023",
    "infrastructure", "engineering_epc", "us",
    "Cambridge International Systems — Bahamas MSS towers",
    "Bahamas",
    "29 Sep 2023: Department of State awards contract to CAMBRIDGE INTERNATIONAL SYSTEMS, INC. for MSS towers in Bahamas (BPC effort); obligated USD 8977929.71. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "8977929.71", "2023-09-29", "2023", "", "",
    "MSS TOWERS IN BAHAMAS (BPC EFFORT), Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_cambridge_bahamas_mss_towers_8978k_2023",
    "MSS TOWERS IN BAHAMAS (BPC EFFORT)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0003923C4033_9700_-NONE-_-NONE-/",
    "Actor: CAMBRIDGE INTERNATIONAL SYSTEMS, INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1307",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N0003923C4033_9700_-NONE-_-NONE- (cambridge_bahamas_mss_towers_8978k_2023). Signed 2023-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0003923C4033_9700_-NONE-_-NONE-/.",
    "USASpending: cambridge_bahamas_mss_towers_8978k_2023 USD 8.978m. Supports cambridge_bahamas_mss_towers_8978k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8977929.71; date_signed 2023-09-29.",
    investment_type="equipment_supply",
)

# === Cycle 1307 ===
row_doc(
    "alutiiq_dr_ng911_center_6083k_2013",
    "infrastructure", "engineering_epc", "us",
    "Alutiiq Technical Services — Dominican Republic NG911 center project",
    "Dominican Republic",
    "22 Oct 2013: Department of State awards contract to ALUTIIQ TECHNICAL SERVICES LLC for NG911 center project — INL Santo Domingo; obligated USD 6082902.22. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "6082902.22", "2013-10-22", "2013", "", "",
    "IGF::OT::IGF NG911 CENTER PROJECT - INL SANTO DOMINGO, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_dr_ng911_center_6083k_2013",
    "IGF::OT::IGF NG911 CENTER PROJECT - INL SANTO DOMINGO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC14M0001_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ TECHNICAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1307",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC14M0001_1900_-NONE-_-NONE- (alutiiq_dr_ng911_center_6083k_2013). Signed 2013-10-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC14M0001_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_dr_ng911_center_6083k_2013 USD 6.083m. Supports alutiiq_dr_ng911_center_6083k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6082902.22; date_signed 2013-10-22.",
    investment_type="equipment_supply",
)

# === Cycle 1307 ===
row_doc(
    "misc_mexico_monterrey_housing_units_990k_2013",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Monterrey purchase of 15 housing units",
    "Mexico",
    "30 Sep 2013: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for OBO/MTY purchase of 15 housing units; obligated USD 989961.09. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "989961.09", "2013-09-30", "2013", "", "",
    "''IGF::OT::IGF'' OBO/MTY  PURCHASE OF 15 HOUSING UNITS, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_monterrey_housing_units_990k_2013",
    "''IGF::OT::IGF'' OBO/MTY  PURCHASE OF 15 HOUSING UNITS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX56013M0281_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1307",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX56013M0281_1900_-NONE-_-NONE- (misc_mexico_monterrey_housing_units_990k_2013). Signed 2013-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX56013M0281_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_monterrey_housing_units_990k_2013 USD 0.990m. Supports misc_mexico_monterrey_housing_units_990k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 989961.09; date_signed 2013-09-30.",
    investment_type="equipment_supply",
)

# === Cycle 1307 ===
row_doc(
    "proyectos_civiles_tumaco_steel_building_589k_2020",
    "infrastructure", "engineering_epc", "other",
    "Proyectos Civiles — Tumaco utilities and steel building upgrade",
    "Colombia",
    "2 Jun 2020: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for Tumaco utilities and steel building upgrade — BRCNA facilities in Tumaco town; obligated USD 589125.24. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "589125.24", "2020-06-02", "2020", "", "",
    "TUMACO UTILITIES&STEEL BUILDING UPGRADE- BRCNA FACILITIES IN TUMACO TOWN, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_civiles_tumaco_steel_building_589k_2020",
    "TUMACO UTILITIES&STEEL BUILDING UPGRADE- BRCNA FACILITIES IN TUMACO TOWN.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0042_1900_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1307",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20C0042_1900_-NONE-_-NONE- (proyectos_civiles_tumaco_steel_building_589k_2020). Signed 2020-06-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0042_1900_-NONE-_-NONE-/.",
    "USASpending: proyectos_civiles_tumaco_steel_building_589k_2020 USD 0.589m. Supports proyectos_civiles_tumaco_steel_building_589k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 589125.24; date_signed 2020-06-02.",
    investment_type="epc",
)

# === Cycle 1307 ===
row_doc(
    "tecnologia_honduras_north_perimeter_wall_442k_2020",
    "infrastructure", "engineering_epc", "other",
    "Tecnologia de Proyectos — Honduras Soto Cano north perimeter wall",
    "Honduras",
    "21 Sep 2020: Department of State awards contract to TECNOLOGIA DE PROYECTOS S.R.L. DE C.V. for north perimeter wall, SCAB, Honduras; obligated USD 441971.71. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "441971.71", "2020-09-21", "2020", "", "",
    "NORTH PERIMETER WALL, SCAB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tecnologia_honduras_north_perimeter_wall_442k_2020",
    "NORTH PERIMETER WALL, SCAB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0423_9700_W9127816D0103_9700/",
    "Actor: TECNOLOGIA DE PROYECTOS S.R.L. DE C.V. — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1307",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127820F0423_9700_W9127816D0103_9700 (tecnologia_honduras_north_perimeter_wall_442k_2020). Signed 2020-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0423_9700_W9127816D0103_9700/.",
    "USASpending: tecnologia_honduras_north_perimeter_wall_442k_2020 USD 0.442m. Supports tecnologia_honduras_north_perimeter_wall_442k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 441971.71; date_signed 2020-09-21.",
    investment_type="epc",
)

# === Cycle 1308 ===
row_doc(
    "cambridge_bahamas_mss_3_4_4483k_2020",
    "infrastructure", "engineering_epc", "us",
    "Cambridge International Systems — Bahamas MSS 3&4 FMS",
    "Bahamas",
    "30 Sep 2020: Department of State awards contract to CAMBRIDGE INTERNATIONAL SYSTEMS, INC. for Bahamas MSS 3&4 FMS case funded; obligated USD 4483215.03. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "4483215.03", "2020-09-30", "2020", "", "",
    "BAHAMAS MSS 3&4 FMS CASE FUNDED, Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_cambridge_bahamas_mss_3_4_4483k_2020",
    "BAHAMAS MSS 3&4 FMS CASE FUNDED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0003920F0555_9700_N0003915D0037_9700/",
    "Actor: CAMBRIDGE INTERNATIONAL SYSTEMS, INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1308",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N0003920F0555_9700_N0003915D0037_9700 (cambridge_bahamas_mss_3_4_4483k_2020). Signed 2020-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0003920F0555_9700_N0003915D0037_9700/.",
    "USASpending: cambridge_bahamas_mss_3_4_4483k_2020 USD 4.483m. Supports cambridge_bahamas_mss_3_4_4483k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4483215.03; date_signed 2020-09-30.",
    investment_type="equipment_supply",
)

# === Cycle 1308 ===
row_doc(
    "alutiiq_mexico_prison_xray_3119k_2020",
    "infrastructure", "engineering_epc", "us",
    "Alutiiq Solutions — Mexico prison x-ray machines",
    "Mexico",
    "9 Sep 2020: Department of State awards contract to ALUTIIQ SOLUTIONS, LLC for x-ray machines for Mexican prisons, INL/Mexico; obligated USD 3119004.06. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3119004.06", "2020-09-09", "2020", "", "",
    "8(A) DIRECT AWARD FOR X-RAY MACHINES FOR MEXICAN PRISONS, INL/MEXICO, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_prison_xray_3119k_2020",
    "8(A) DIRECT AWARD FOR X-RAY MACHINES FOR MEXICAN PRISONS, INL/MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE20C0013_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ SOLUTIONS, LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1308",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE20C0013_1900_-NONE-_-NONE- (alutiiq_mexico_prison_xray_3119k_2020). Signed 2020-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE20C0013_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_prison_xray_3119k_2020 USD 3.119m. Supports alutiiq_mexico_prison_xray_3119k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3119004.06; date_signed 2020-09-09.",
    investment_type="equipment_supply",
)

# === Cycle 1308 ===
row_doc(
    "misc_colombia_construction_398k_2011",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Colombia construction",
    "Colombia",
    "20 Jan 2011: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for construction (PoP Colombia); obligated USD 397522.42. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "397522.42", "2011-01-20", "2011", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_construction_398k_2011",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0004_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1308",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11C0004_9700_-NONE-_-NONE- (misc_colombia_construction_398k_2011). Signed 2011-01-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0004_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_construction_398k_2011 USD 0.398m. Supports misc_colombia_construction_398k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 397522.42; date_signed 2011-01-20.",
    investment_type="epc",
)

# === Cycle 1308 ===
row_doc(
    "misc_colombia_construction_364k_2010",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Colombia construction",
    "Colombia",
    "16 Sep 2010: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for construction (PoP Colombia); obligated USD 363528.59. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "363528.59", "2010-09-16", "2010", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_construction_364k_2010",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10C0030_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1308",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT10C0030_9700_-NONE-_-NONE- (misc_colombia_construction_364k_2010). Signed 2010-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10C0030_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_construction_364k_2010 USD 0.364m. Supports misc_colombia_construction_364k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 363528.59; date_signed 2010-09-16.",
    investment_type="epc",
)

# === Cycle 1308 ===
row_doc(
    "palgag_jamaica_launch_ramps_317k_2010",
    "infrastructure", "engineering_epc", "other",
    "Palgag Building Technologies — Jamaica Port Royal/Port Morant launch ramps",
    "Jamaica",
    "26 Jul 2010: Department of State awards contract to PALGAG BUILDING TECHNOLOGIES LTD for design build of two launch ramps; Jamaica (Port Royal and Port Morant); obligated USD 316900.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "316900.00", "2010-07-26", "2010", "", "",
    "DESIGN BUILD OF TWO LAUNCH RAMPS; JAMAICA (PORT ROYAL AND PORT MORANT), Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_palgag_jamaica_launch_ramps_317k_2010",
    "DESIGN BUILD OF TWO LAUNCH RAMPS; JAMAICA (PORT ROYAL AND PORT MORANT)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0022_9700_-NONE-_-NONE-/",
    "Actor: PALGAG BUILDING TECHNOLOGIES LTD — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1308",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945010C0022_9700_-NONE-_-NONE- (palgag_jamaica_launch_ramps_317k_2010). Signed 2010-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0022_9700_-NONE-_-NONE-/.",
    "USASpending: palgag_jamaica_launch_ramps_317k_2010 USD 0.317m. Supports palgag_jamaica_launch_ramps_317k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 316900.0; date_signed 2010-07-26.",
    investment_type="epc",
)

# === Cycle 1309 ===
row_doc(
    "cambridge_colombia_gorgona_radar_tower_1047k_2017",
    "infrastructure", "building_materials", "us",
    "Cambridge International Systems — Colombia Gorgona metallic radar tower",
    "Colombia",
    "30 Jan 2017: Department of State awards contract to CAMBRIDGE INTERNATIONAL SYSTEMS, INC. for one metallic radar tower in Gorgona, Colombia; obligated USD 1046922.90. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1046922.90", "2017-01-30", "2017", "", "",
    "ONE METALLIC RADAR TOWER IN GORGONA, COLOMBIA IGF::OT::IGF, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_cambridge_colombia_gorgona_radar_tower_1047k_2017",
    "ONE METALLIC RADAR TOWER IN GORGONA, COLOMBIA IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0077_1900_-NONE-_-NONE-/",
    "Actor: CAMBRIDGE INTERNATIONAL SYSTEMS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1309",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0077_1900_-NONE-_-NONE- (cambridge_colombia_gorgona_radar_tower_1047k_2017). Signed 2017-01-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0077_1900_-NONE-_-NONE-/.",
    "USASpending: cambridge_colombia_gorgona_radar_tower_1047k_2017 USD 1.047m. Supports cambridge_colombia_gorgona_radar_tower_1047k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1046922.9; date_signed 2017-01-30.",
    investment_type="epc",
)

# === Cycle 1309 ===
row_doc(
    "alutiiq_mexico_biometric_install_322k_2018",
    "infrastructure", "building_materials", "us",
    "Alutiiq Information Management — Mexico biometric equipment install",
    "Mexico",
    "12 Mar 2018: Department of State awards contract to ALUTIIQ INFORMATION MANAGEMENT, LLC for buy and install biometric equipment across Mexico; obligated USD 322009.17. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "322009.17", "2018-03-12", "2018", "", "",
    "THIS IS THE FIRST TASK ORDER TO BUY AND INSTALL BIO-METRIC EQUIPMENT ACROSS MEXICO, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_biometric_install_322k_2018",
    "THIS IS THE FIRST TASK ORDER TO BUY AND INSTALL BIO-METRIC EQUIPMENT ACROSS MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F0846_1900_19AQMM18D0038_1900/",
    "Actor: ALUTIIQ INFORMATION MANAGEMENT, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1309",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F0846_1900_19AQMM18D0038_1900 (alutiiq_mexico_biometric_install_322k_2018). Signed 2018-03-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F0846_1900_19AQMM18D0038_1900/.",
    "USASpending: alutiiq_mexico_biometric_install_322k_2018 USD 0.322m. Supports alutiiq_mexico_biometric_install_322k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 322009.17; date_signed 2018-03-12.",
    investment_type="equipment_supply",
)

# === Cycle 1309 ===
row_doc(
    "misc_colombia_csec_building_297k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia CSEC building construction",
    "Colombia",
    "15 Sep 2010: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for CSEC building construction; obligated USD 296730.80. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "296730.80", "2010-09-15", "2010", "", "",
    "CSEC BUILDING CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_csec_building_297k_2010",
    "CSEC BUILDING CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10C0031_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1309",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT10C0031_9700_-NONE-_-NONE- (misc_colombia_csec_building_297k_2010). Signed 2010-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10C0031_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_csec_building_297k_2010 USD 0.297m. Supports misc_colombia_csec_building_297k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 296730.8; date_signed 2010-09-15.",
    investment_type="epc",
)

# === Cycle 1309 ===
row_doc(
    "misc_colombia_school_dorm_278k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia school dorm construction",
    "Colombia",
    "11 Sep 2013: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for school dorm construction; obligated USD 277656.81. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "277656.81", "2013-09-11", "2013", "", "",
    "SCHOOL DORM CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_school_dorm_278k_2013",
    "SCHOOL DORM CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13C0019_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1309",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT13C0019_9700_-NONE-_-NONE- (misc_colombia_school_dorm_278k_2013). Signed 2013-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13C0019_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_school_dorm_278k_2013 USD 0.278m. Supports misc_colombia_school_dorm_278k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 277656.81; date_signed 2013-09-11.",
    investment_type="epc",
)

# === Cycle 1309 ===
row_doc(
    "misc_dr_site_prep_4locations_275k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic site prep (4 locations)",
    "Dominican Republic",
    "21 Dec 2016: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for site prep 4 locations in Dominican Republic; obligated USD 275470.76. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "275470.76", "2016-12-21", "2016", "", "",
    "IGF::OT::IGF SITE PREP 4 LOCATIONS IN DOMINICAN REPUBLIC, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dr_site_prep_4locations_275k_2016",
    "IGF::OT::IGF SITE PREP 4 LOCATIONS IN DOMINICAN REPUBLIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470417C1001_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1309",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA470417C1001_9700_-NONE-_-NONE- (misc_dr_site_prep_4locations_275k_2016). Signed 2016-12-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470417C1001_9700_-NONE-_-NONE-/.",
    "USASpending: misc_dr_site_prep_4locations_275k_2016 USD 0.275m. Supports misc_dr_site_prep_4locations_275k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 275470.76; date_signed 2016-12-21.",
    investment_type="epc",
)

# === Cycle 1310 ===
row_doc(
    "jeff_smith_brazil_modular_vault_205k_2011",
    "infrastructure", "building_materials", "us",
    "Jeff Smith Enterprises — Brazil Sao Paulo modular vault",
    "Brazil",
    "29 Sep 2011: Department of State awards contract to JEFF SMITH ENTERPRISES LLC for purchase a modular vault for the courier office in Sao Paulo, Brazil; obligated USD 205277.10. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "205277.10", "2011-09-29", "2011", "", "",
    "THE PURPOSE OF THIS REQUEST IS TO PURCHASE A MODULAR VAULT FOR THE COURIER OFFICE IN SAO PAULO BRASIL, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_jeff_smith_brazil_modular_vault_205k_2011",
    "THE PURPOSE OF THIS REQUEST IS TO PURCHASE A MODULAR VAULT FOR THE COURIER OFFICE IN SAO PAULO BRASIL.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11M2623_1900_-NONE-_-NONE-/",
    "Actor: JEFF SMITH ENTERPRISES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1310",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11M2623_1900_-NONE-_-NONE- (jeff_smith_brazil_modular_vault_205k_2011). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11M2623_1900_-NONE-_-NONE-/.",
    "USASpending: jeff_smith_brazil_modular_vault_205k_2011 USD 0.205m. Supports jeff_smith_brazil_modular_vault_205k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 205277.1; date_signed 2011-09-29.",
    investment_type="equipment_supply",
)

# === Cycle 1310 ===
row_doc(
    "olgoonik_mexico_sonora_prefab_kennel_184k_2023",
    "infrastructure", "building_materials", "us",
    "Olgoonik Logistics — Mexico Sonora prefabricated kennel",
    "Mexico",
    "11 Sep 2023: Department of State awards contract to OLGOONIK LOGISTICS, LLC for prefabricated kennel for Sonora State Police; obligated USD 183968.17. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "183968.17", "2023-09-11", "2023", "", "",
    "PREFABRICATED KENNEL FOR SONORA STATE POLICE, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_olgoonik_mexico_sonora_prefab_kennel_184k_2023",
    "PREFABRICATED KENNEL FOR SONORA STATE POLICE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5013_1900_19AQMM20D0098_1900/",
    "Actor: OLGOONIK LOGISTICS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1310",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMR23F5013_1900_19AQMM20D0098_1900 (olgoonik_mexico_sonora_prefab_kennel_184k_2023). Signed 2023-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5013_1900_19AQMM20D0098_1900/.",
    "USASpending: olgoonik_mexico_sonora_prefab_kennel_184k_2023 USD 0.184m. Supports olgoonik_mexico_sonora_prefab_kennel_184k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 183968.17; date_signed 2023-09-11.",
    investment_type="equipment_supply",
)

# === Cycle 1310 ===
row_doc(
    "misc_haiti_stecher_fiber_optic_250k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Haiti Stecher fiber optic cabling installation",
    "Haiti",
    "26 Sep 2023: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for PAP IM ISC fiber optic cabling installation in Stecher; obligated USD 249869.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "249869.00", "2023-09-26", "2023", "", "",
    "PAP  IM  ISC FIBER OPTIC CABLING INSTALLATION IN STECHER, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_stecher_fiber_optic_250k_2023",
    "PAP  IM  ISC FIBER OPTIC CABLING INSTALLATION IN STECHER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P1364_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1310",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7023P1364_1900_-NONE-_-NONE- (misc_haiti_stecher_fiber_optic_250k_2023). Signed 2023-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P1364_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_stecher_fiber_optic_250k_2023 USD 0.250m. Supports misc_haiti_stecher_fiber_optic_250k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 249869.0; date_signed 2023-09-26.",
    investment_type="epc",
)

# === Cycle 1310 ===
row_doc(
    "misc_paraguay_construction_services_249k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Paraguay construction services with RMT",
    "Paraguay",
    "3 May 2012: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for 1207 construction services with RMT; obligated USD 249006.03. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "249006.03", "2012-05-03", "2012", "", "",
    "1207 - CONSTRUCTION SERVICES WITH RMT, Paraguay (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_paraguay_construction_services_249k_2012",
    "1207 - CONSTRUCTION SERVICES WITH RMT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPA10012M0187_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1310",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPA10012M0187_1900_-NONE-_-NONE- (misc_paraguay_construction_services_249k_2012). Signed 2012-05-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPA10012M0187_1900_-NONE-_-NONE-/.",
    "USASpending: misc_paraguay_construction_services_249k_2012 USD 0.249m. Supports misc_paraguay_construction_services_249k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 249006.03; date_signed 2012-05-03.",
    investment_type="epc",
)

# === Cycle 1310 ===
row_doc(
    "misc_mexico_puebla_ballistic_panels_247k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Puebla ballistic panels",
    "Mexico",
    "16 Apr 2012: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for NAS-MI ballistic panels to support Puebla; obligated USD 247121.22. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "247121.22", "2012-04-16", "2012", "", "",
    "NAS-MI IN41MX72 2R32 BALLISTIC PANNELS TO SUPPORT PUEBLA, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_puebla_ballistic_panels_247k_2012",
    "NAS-MI IN41MX72 2R32 BALLISTIC PANNELS TO SUPPORT PUEBLA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M0795_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1310",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53012M0795_1900_-NONE-_-NONE- (misc_mexico_puebla_ballistic_panels_247k_2012). Signed 2012-04-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M0795_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_puebla_ballistic_panels_247k_2012 USD 0.247m. Supports misc_mexico_puebla_ballistic_panels_247k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 247121.22; date_signed 2012-04-16.",
    investment_type="equipment_supply",
)

# === Cycle 1311 ===
row_doc(
    "jet_dock_bahamas_performance_dock_136k_2012",
    "infrastructure", "engineering_epc", "us",
    "Jet Dock Systems — Bahamas universal 50 ft performance dock",
    "Bahamas",
    "22 Mar 2012: Department of State awards contract to JET DOCK SYSTEMS INC for universal 50 ft performance dock; obligated USD 136439.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "136439.00", "2012-03-22", "2012", "", "",
    "UNIVERSAL 50 FT PERFORMANCE DOCK, Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_jet_dock_bahamas_performance_dock_136k_2012",
    "UNIVERSAL 50 FT PERFORMANCE DOCK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0002412C4209_9700_-NONE-_-NONE-/",
    "Actor: JET DOCK SYSTEMS INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1311",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N0002412C4209_9700_-NONE-_-NONE- (jet_dock_bahamas_performance_dock_136k_2012). Signed 2012-03-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0002412C4209_9700_-NONE-_-NONE-/.",
    "USASpending: jet_dock_bahamas_performance_dock_136k_2012 USD 0.136m. Supports jet_dock_bahamas_performance_dock_136k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 136439.0; date_signed 2012-03-22.",
    investment_type="equipment_supply",
)

# === Cycle 1311 ===
row_doc(
    "hardline_nati_mexico_hardline_wall_80k_2017",
    "infrastructure", "engineering_epc", "us",
    "Hardline Nati Construction — Mexico hardline wall, doors and windows",
    "Mexico",
    "2 Mar 2017: Department of State awards contract to HARDLINE NATI CONSTRUCTION LLC for installation of hardline wall, doors and windows; obligated USD 79760.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "79760.00", "2017-03-02", "2017", "", "",
    "INSTALLATION OF HARDLINE WALL, DOORS AND WINDOWS, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hardline_nati_mexico_hardline_wall_80k_2017",
    "INSTALLATION OF HARDLINE WALL, DOORS AND WINDOWS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX61017M0048_1900_-NONE-_-NONE-/",
    "Actor: HARDLINE NATI CONSTRUCTION LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1311",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX61017M0048_1900_-NONE-_-NONE- (hardline_nati_mexico_hardline_wall_80k_2017). Signed 2017-03-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX61017M0048_1900_-NONE-_-NONE-/.",
    "USASpending: hardline_nati_mexico_hardline_wall_80k_2017 USD 0.080m. Supports hardline_nati_mexico_hardline_wall_80k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79760.0; date_signed 2017-03-02.",
    investment_type="epc",
)

# === Cycle 1311 ===
row_doc(
    "misc_brazil_cmr_awning_expansion_243k_2018",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Brazil CMR awning expansion",
    "Brazil",
    "26 Sep 2018: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC CMR awning expansion project; obligated USD 243328.35. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "243328.35", "2018-09-26", "2018", "", "",
    "FAC - CMR AWNING EXPANSION PROJECT, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_cmr_awning_expansion_243k_2018",
    "FAC - CMR AWNING EXPANSION PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2518P1354_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1311",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2518P1354_1900_-NONE-_-NONE- (misc_brazil_cmr_awning_expansion_243k_2018). Signed 2018-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2518P1354_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_cmr_awning_expansion_243k_2018 USD 0.243m. Supports misc_brazil_cmr_awning_expansion_243k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 243328.35; date_signed 2018-09-26.",
    investment_type="epc",
)

# === Cycle 1311 ===
row_doc(
    "misc_colombia_tumaco_security_towers_241k_2013",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Colombia Tumaco security towers",
    "Colombia",
    "19 Dec 2013: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for security towers at Tumaco; obligated USD 240545.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "240545.00", "2013-12-19", "2013", "", "",
    "SECURITY TOWERS AT TUMACO 3, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_tumaco_security_towers_241k_2013",
    "SECURITY TOWERS AT TUMACO 3.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15014CN002_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1311",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15014CN002_1900_-NONE-_-NONE- (misc_colombia_tumaco_security_towers_241k_2013). Signed 2013-12-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15014CN002_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_tumaco_security_towers_241k_2013 USD 0.241m. Supports misc_colombia_tumaco_security_towers_241k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 240545.0; date_signed 2013-12-19.",
    investment_type="epc",
)

# === Cycle 1311 ===
row_doc(
    "misc_brazil_rdj_perimeter_fence_236k_2013",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Brazil Rio de Janeiro perimeter fence",
    "Brazil",
    "25 Sep 2013: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for RDJ perimeter fence; obligated USD 236061.54. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "236061.54", "2013-09-25", "2013", "", "",
    "IGF::CT::IGF CONTRACT - RDJ PERIMETER FENCE, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_rdj_perimeter_fence_236k_2013",
    "IGF::CT::IGF CONTRACT - RDJ PERIMETER FENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82013C0002_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1311",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82013C0002_1900_-NONE-_-NONE- (misc_brazil_rdj_perimeter_fence_236k_2013). Signed 2013-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82013C0002_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_rdj_perimeter_fence_236k_2013 USD 0.236m. Supports misc_brazil_rdj_perimeter_fence_236k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 236061.54; date_signed 2013-09-25.",
    investment_type="epc",
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
                if s not in (existing.get("supports") or []):
                    existing.setdefault("supports", []).append(s)
        else:
            bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")


if __name__ == "__main__":
    main()
