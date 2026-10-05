#!/usr/bin/env python3
"""Cycles 920–922: USASpending Central America / Caribbean residual CapEx.

Seeds: 20261920–20261922. Thin top-up dry.
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


# === 920 ===
row_doc(
    "alutiiq_santiago_psap_12p1m_2016",
    "infrastructure", "building_materials", "us",
    "Alutiiq Information Management, LLC — INL Santiago Northern Region PSAP",
    "Dominican Republic",
    "7 Sep 2016: Department of State awards contract SWHARC16C0007 to Alutiiq Information "
    "Management, LLC for INL Santo Domingo Northern Region Public Safety Answering Point (PSAP) "
    "project in Santiago, Dominican Republic (includes up to 3 years on-site maintenance/tech "
    "support, CCTVs, UAVs); obligated USD 12,143,990.10. CapEx face = award obligation.",
    "12143990.10", "2016-09-07", "2016", "19.450", "-70.700",
    "PSAP facility, Santiago, Dominican Republic (award description; Santiago pin).",
    "usaspending_alutiiq_santiago_psap_20160907",
    "INL SANTO DOMINGO NORTHERN REGION PUBLIC SAFETY ANSWERING POINT (PSAP) PROJECT: THE MAIN "
    "OBJECTIVE OF THIS PROJECT IS TO PROVIDE A PSAP IN THE CITY OF SANTIAGO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16C0007_1900_-NONE-_-NONE-/",
    "Actor: Alutiiq Information Management, LLC (U.S.) under State INL — us. Official USASpending "
    "Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle920",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16C0007_1900_-NONE-_-NONE- "
    "(Alutiiq; Santiago PSAP). Signed 7 September 2016. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16C0007_1900_-NONE-_-NONE-/.",
    "USASpending: Alutiiq Santiago PSAP USD 12.144m. Supports alutiiq_santiago_psap_12p1m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12,143,990.10; date_signed 2016-09-07.",
)
row_doc(
    "jacobs_guatemala_port_ae_22p2m_2025",
    "infrastructure", "port_ownership", "us",
    "Jacobs Government Services Company — USACE Guatemala port planning/design/construction A&E",
    "Guatemala",
    "2 Dec 2025: USACE awards task order W9127826FA025 to Jacobs Government Services Company for "
    "architectural and engineering services supporting a port planning, design, and construction "
    "project in Guatemala; obligated USD 22,206,913.21. CapEx face = award obligation. "
    "USASpending PoP codes Mobile AL (USACE office) — country coded Guatemala per description.",
    "22206913.21", "2025-12-02", "2025", "", "",
    "Guatemala port planning/design/construction A&E — lat/lon blank (site unnamed on award).",
    "usaspending_jacobs_guatemala_port_ae_20251202",
    "THE USACE IS REQUESTING ARCHITECTURAL AND ENGINEERING SERVICES IN SUPPORT OF A PORT PLANNING, "
    "DESIGN, AND CONSTRUCTION PROJECT IN THE COUNTRY OF GUATEMALA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127826FA025_9700_W9127820D0031_9700/",
    "Actor: Jacobs Government Services Company (U.S.) under USACE — us. Official USASpending Award "
    "API. Shuffle port_ownership; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle920",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127826FA025_9700_W9127820D0031_9700 (Jacobs; Guatemala port A&E). Signed 2 December "
    "2025. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127826FA025_9700_W9127820D0031_9700/.",
    "USASpending: Jacobs Guatemala port A&E USD 22.207m. Supports jacobs_guatemala_port_ae_22p2m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 22,206,913.21; date_signed 2025-12-02.",
)
row_doc(
    "ds_san_salvador_design_17p9m_2024",
    "infrastructure", "engineering_epc", "us",
    "D+S International LLC — planning and design services San Salvador",
    "El Salvador",
    "26 Sep 2024: Department of State awards task order 19AQMM24F2487 to D+S International LLC for "
    "planning and design services in San Salvador, El Salvador; obligated USD 17,901,804.00. CapEx "
    "face = award obligation. Distinct from futron_san_salvador_csu_2022.",
    "17901804.00", "2024-09-26", "2024", "13.692", "-89.218",
    "U.S. facilities planning/design, San Salvador, El Salvador (award description; San Salvador pin). "
    "USASpending PoP codes New York office — country coded El Salvador per description.",
    "usaspending_ds_san_salvador_design_20240926",
    "PLANNING AND DESIGN SERVICES IN SAN SALVADOR, EL SALVADOR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2487_1900_19AQMM19D0060_1900/",
    "Actor: D+S International LLC (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle920",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM24F2487_1900_19AQMM19D0060_1900 (D+S International; San Salvador design). Signed "
    "26 September 2024. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2487_1900_19AQMM19D0060_1900/.",
    "USASpending: D+S San Salvador design USD 17.902m. Supports ds_san_salvador_design_17p9m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 17,901,804.00; date_signed 2024-09-26.",
)
row_doc(
    "chugach_belmopan_hvac_5p90m_2022",
    "infrastructure", "building_materials", "us",
    "Chugach Intelligence Solutions, LLC — Belmopan REC chillers / HVAC repairs",
    "Belize",
    "26 Sep 2022: Department of State awards contract 19AQMM22C0148 to Chugach Intelligence "
    "Solutions, LLC for REC Belmopan, Belize chillers / HVAC repairs; obligated USD 5,895,327.63. "
    "CapEx face = award obligation. Distinct from jajones_belmopan_nec_2004.",
    "5895327.63", "2022-09-26", "2022", "17.251", "-88.759",
    "REC Belmopan chillers/HVAC, Belize (USASpending PoP Belize; Belmopan pin).",
    "usaspending_chugach_belmopan_hvac_20220926",
    "REC BELMOPAN, BELIZE CHILLERS / HVAC REPAIRS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0148_1900_-NONE-_-NONE-/",
    "Actor: Chugach Intelligence Solutions, LLC (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx; Belize under-covered.",
    "hunt_cycle920",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22C0148_1900_-NONE-_-NONE- "
    "(Chugach; Belmopan HVAC). Signed 26 September 2022. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0148_1900_-NONE-_-NONE-/.",
    "USASpending: Chugach Belmopan HVAC USD 5.895m. Supports chugach_belmopan_hvac_5p90m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5,895,327.63; date_signed 2022-09-26.",
)
row_doc(
    "roofing_resources_managua_roof_3p77m_2013",
    "infrastructure", "building_materials", "us",
    "Roofing Resources Inc. — compound roof replacement Managua",
    "Nicaragua",
    "28 Aug 2013: Department of State awards task order SAQMMA13F2639 to Roofing Resources Inc. for "
    "compound roof replacement project in Managua, Nicaragua; obligated USD 3,765,658.08. CapEx "
    "face = award obligation. Distinct from zachry_managua_nec_2004.",
    "3765658.08", "2013-08-28", "2013", "12.136", "-86.251",
    "U.S. compound roof replacement, Managua, Nicaragua (USASpending PoP Nicaragua).",
    "usaspending_roofing_managua_20130828",
    "COMPOUND ROOF REPLACEMENT PROJECT IN MANAGUA, NICARAGUA,  SAQMMA13F2639 AWARDED TO ROOFING "
    "RESOURCES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F2639_1900_SALMEC07D0028_1900/",
    "Actor: Roofing Resources Inc. (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx; Nicaragua under-covered.",
    "hunt_cycle920",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA13F2639_1900_SALMEC07D0028_1900 (Roofing Resources; Managua roof). Signed 28 "
    "August 2013. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F2639_1900_SALMEC07D0028_1900/.",
    "USASpending: Roofing Resources Managua USD 3.766m. Supports roofing_resources_managua_roof_3p77m_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,765,658.08; date_signed 2013-08-28.",
)

# === 921 ===
row_doc(
    "otak_cdema_barbados_4p01m_2013",
    "infrastructure", "engineering_epc", "us",
    "Otak Group, Inc. — CDEMA facility works Bridgetown",
    "Barbados",
    "27 Sep 2013: DoD awards task order 0004 under N6945012D0038 to Otak Group, Inc. for CDEMA "
    "(Caribbean Disaster Emergency Management Agency) works in Bridgetown, Barbados; obligated "
    "USD 4,014,745.92. CapEx face = award obligation.",
    "4014745.92", "2013-09-27", "2013", "13.097", "-59.615",
    "CDEMA facility, Bridgetown, Barbados (USASpending PoP Barbados).",
    "usaspending_otak_cdema_barbados_20130927",
    "CDEMA, BRIDGETOWN, BARBADOS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_N6945012D0038_9700/",
    "Actor: Otak Group, Inc. (U.S.) under DoD — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle921",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0004_9700_N6945012D0038_9700 "
    "(Otak; CDEMA Bridgetown). Signed 27 September 2013. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_N6945012D0038_9700/.",
    "USASpending: Otak CDEMA Barbados USD 4.015m. Supports otak_cdema_barbados_4p01m_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,014,745.92; date_signed 2013-09-27.",
)
row_doc(
    "ped_concepts_antigua_trinidad_2p69m_2026",
    "infrastructure", "building_materials", "us",
    "PED Concepts Inc. — construction of 6 projects for Antigua and Trinidad",
    "Trinidad and Tobago",
    "5 Jan 2026: DoD awards task order N6945026F0008 to PED Concepts Inc. for construction of 6 "
    "individual projects for Antigua and Trinidad; obligated USD 2,692,613.12. CapEx face = award "
    "obligation. Country coded Trinidad and Tobago per USASpending PoP (multi-island package).",
    "2692613.12", "2026-01-05", "2026", "10.667", "-61.519",
    "Six-project package Antigua and Trinidad (USASpending PoP Trinidad and Tobago; Port of Spain approximate).",
    "usaspending_ped_antigua_trinidad_20260105",
    "CONSTRUCTION OF 6 INDIVIDUAL PROJECTS FOR ANTIGUA AND TRINIDAD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945026F0008_9700_N6945025D0018_9700/",
    "Actor: PED Concepts Inc. (U.S.) under DoD — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle921",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_N6945026F0008_9700_N6945025D0018_9700 (PED Concepts; Antigua/Trinidad). Signed 5 "
    "January 2026. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945026F0008_9700_N6945025D0018_9700/.",
    "USASpending: PED Antigua/Trinidad USD 2.693m. Supports ped_concepts_antigua_trinidad_2p69m_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,692,613.12; date_signed 2026-01-05.",
)
row_doc(
    "bozdemir_managua_water_1p92m_2026",
    "resources", "water", "us",
    "Bozdemir Construction LLC — Embassy Managua water infrastructure improvements",
    "Nicaragua",
    "23 Sep 2026: Department of State awards contract 19GE5026C0115 to Bozdemir Construction LLC "
    "for water infrastructure improvements at U.S. Embassy Managua, Nicaragua; obligated USD "
    "1,923,542.30. CapEx face = award obligation.",
    "1923542.30", "2026-09-23", "2026", "12.136", "-86.251",
    "U.S. Embassy Managua water infrastructure, Nicaragua (USASpending PoP Nicaragua).",
    "usaspending_bozdemir_managua_water_20260923",
    "WATER INFRASTRUCTURE IMPROVEMENTS, U.S. EMBASSY MANAGUA, NICARAGUA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0115_1900_-NONE-_-NONE-/",
    "Actor: Bozdemir Construction LLC (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle water; ≥1/3 U.S. hunt CapEx; Nicaragua under-covered.",
    "hunt_cycle921",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5026C0115_1900_-NONE-_-NONE- "
    "(Bozdemir; Managua water). Signed 23 September 2026. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0115_1900_-NONE-_-NONE-/.",
    "USASpending: Bozdemir Managua water USD 1.924m. Supports bozdemir_managua_water_1p92m_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,923,542.30; date_signed 2026-09-23.",
)
row_doc(
    "bonatti_hunting_caye_ops_1p80m_2012",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros y Arquitectos S.A. — Hunting Caye ops/barracks maintenance facility",
    "Belize",
    "10 Aug 2012: DoD awards task order 0008 under W9127811D0044 to Bonatti Ingenieros y "
    "Arquitectos S.A. (Guatemala) for construction of operations/barracks maintenance facility "
    "at Hunting Caye, Belize; obligated USD 1,800,000.00. CapEx face = award obligation.",
    "1800000.00", "2012-08-10", "2012", "16.100", "-88.260",
    "Ops/barracks maintenance facility, Hunting Caye, Belize (USASpending PoP Belize; approximate).",
    "usaspending_bonatti_hunting_caye_20120810",
    "CONSTRUCTION OF OPERATIONS/BARRACKS MAINTENACE FACILITY, HUNTING CAYE, BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127811D0044_9700/",
    "Actor: Bonatti Ingenieros y Arquitectos S.A. (Guatemala) under DoD — other. Official "
    "USASpending Award API. Shuffle building_materials; Belize under-covered.",
    "hunt_cycle921",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0008_9700_W9127811D0044_9700 "
    "(Bonatti; Hunting Caye). Signed 10 August 2012. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127811D0044_9700/.",
    "USASpending: Bonatti Hunting Caye USD 1.800m. Supports bonatti_hunting_caye_ops_1p80m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,800,000.00; recipient Guatemala.",
)
row_doc(
    "bonatti_san_pedro_ops_1p76m_2011",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros y Arquitectos S.A. — San Pedro CN ops center",
    "Belize",
    "27 Sep 2011: DoD awards task order 0001 under W9127811D0044 to Bonatti Ingenieros y "
    "Arquitectos S.A. for construction of CN ops center at San Pedro, Belize; obligated USD "
    "1,759,986.60. CapEx face = award obligation. Distinct from "
    "bonatti_hunting_caye_ops_1p80m_2012.",
    "1759986.60", "2011-09-27", "2011", "17.921", "-87.961",
    "CN ops center, San Pedro, Belize (USASpending PoP Belize; San Pedro pin).",
    "usaspending_bonatti_san_pedro_20110927",
    "CONSTRUCTION OF CN OPS CENTER, SAN PEDRO, BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127811D0044_9700/",
    "Actor: Bonatti Ingenieros y Arquitectos S.A. (Guatemala) under DoD — other. Official "
    "USASpending Award API. Shuffle building_materials.",
    "hunt_cycle921",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127811D0044_9700 "
    "(Bonatti; San Pedro ops). Signed 27 September 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127811D0044_9700/.",
    "USASpending: Bonatti San Pedro USD 1.760m. Supports bonatti_san_pedro_ops_1p76m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,759,986.60; date_signed 2011-09-27.",
)

# === 922 ===
row_doc(
    "eterna_el_bluff_ops_1p43m_2011",
    "infrastructure", "port_ownership", "other",
    "Eterna S.A. de C.V. — El Bluff CN ops center, boat ramp, and gravel drive",
    "Nicaragua",
    "20 Sep 2011: DoD awards task order 0004 under W9127811D0046 to Empresa de Construccion y "
    "Transporte Eterna S.A. de C.V. for construction of CN ops center, boat ramp, and gravel "
    "drive at El Bluff, Nicaragua; obligated USD 1,431,695.11. CapEx face = award obligation. "
    "Distinct from eterna_soto_cano_hangar_2021 / eterna_soto_cano_aviation_storage_2025.",
    "1431695.11", "2011-09-20", "2011", "11.990", "-83.690",
    "CN ops center / boat ramp, El Bluff, Nicaragua (USASpending PoP Nicaragua; El Bluff pin).",
    "usaspending_eterna_el_bluff_20110920",
    "CONSTRUCTION OF CN OPS CENTER, BOAT RAMP, AND GRAVEL DR., EL BLUFF, NICARAGUA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127811D0046_9700/",
    "Actor: Eterna S.A. de C.V. (Honduras) under DoD — other. Official USASpending Award API. "
    "Shuffle port_ownership (boat ramp/ops); Nicaragua under-covered.",
    "hunt_cycle922",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0004_9700_W9127811D0046_9700 "
    "(Eterna; El Bluff ops/boat ramp). Signed 20 September 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127811D0046_9700/.",
    "USASpending: Eterna El Bluff USD 1.432m. Supports eterna_el_bluff_ops_1p43m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,431,695.11; date_signed 2011-09-20.",
)
row_doc(
    "nika_georgetown_voltage_705k_2011",
    "energy", "power_plants_grid", "us",
    "NIKA & EMR JV — Embassy Georgetown electrical voltage upgrade Phase I D/B",
    "Guyana",
    "24 Jan 2011: Department of State awards task order SAQMMA11F0517 to NIKA & EMR Joint Venture "
    "for Phase I design/build electrical voltage upgrade at U.S. Embassy Georgetown, Guyana; "
    "obligated USD 705,179.00. CapEx face = award obligation. Distinct from "
    "spectrum_georgetown_pcc_generator_738k_2022.",
    "705179.00", "2011-01-24", "2011", "6.801", "-58.155",
    "U.S. Embassy Georgetown electrical voltage upgrade, Guyana (USASpending PoP Guyana).",
    "usaspending_nika_georgetown_voltage_20110124",
    "PHASE I SERVICES DESIGN/BUILD FOR ELECTRICAL VOLTAGE UPGRADE AT US EMBASSY GEORGETOWN,GUYANA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0517_1900_SAQMMA08D0020_1900/",
    "Actor: NIKA & EMR JV (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle922",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA11F0517_1900_SAQMMA08D0020_1900 (NIKA & EMR; Georgetown voltage). Signed 24 "
    "January 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0517_1900_SAQMMA08D0020_1900/.",
    "USASpending: NIKA Georgetown voltage USD 0.705m. Supports nika_georgetown_voltage_705k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 705,179.00; date_signed 2011-01-24.",
)
row_doc(
    "swanke_barbados_nrl_design_863k_2012",
    "infrastructure", "engineering_epc", "us",
    "Swanke Hayden Connell Ltd. — Bridgetown regional reference laboratory design documents",
    "Barbados",
    "11 Jul 2012: Department of State awards task order SAQMMA12F2295 to Swanke Hayden Connell "
    "Ltd. for development of design documents for construction of a regional reference laboratory "
    "in Bridgetown, Barbados; obligated USD 862,892.27. CapEx face = award obligation. Distinct "
    "from palgag_barbados_nrl_7p69m_2015 (construction).",
    "862892.27", "2012-07-11", "2012", "13.097", "-59.615",
    "Regional reference laboratory design, Bridgetown, Barbados (USASpending PoP Barbados).",
    "usaspending_swanke_barbados_nrl_design_20120711",
    "DEVELOPMENT OF DESIGN DOCUMENTS FOR CONSTRUCTION OF A REGIONAL REFERENCE LABORATORY IN "
    "BRIDGETOWN, BARBADOS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2295_1900_SAQMMA09D0005_1900/",
    "Actor: Swanke Hayden Connell Ltd. (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle922",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA12F2295_1900_SAQMMA09D0005_1900 (Swanke; Bridgetown NRL design). Signed 11 July "
    "2012. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2295_1900_SAQMMA09D0005_1900/.",
    "USASpending: Swanke Barbados NRL design USD 0.863m. Supports swanke_barbados_nrl_design_863k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 862,892.27; date_signed 2012-07-11.",
)
row_doc(
    "blackwell_managua_design_910k_2023",
    "infrastructure", "engineering_epc", "us",
    "Marlon Blackwell Architects, P.A. — project development and design Managua",
    "Nicaragua",
    "28 Sep 2023: Department of State awards task order 19AQMM23F2541 to Marlon Blackwell "
    "Architects, P.A. for project development and design services in Managua, Nicaragua; "
    "obligated USD 910,290.44. CapEx face = award obligation.",
    "910290.44", "2023-09-28", "2023", "12.136", "-86.251",
    "U.S. facilities design services, Managua, Nicaragua (award description; Managua pin).",
    "usaspending_blackwell_managua_design_20230928",
    "PROJECT DEVELOPMENT AND DESIGN SERVICES IN MANAGUA, NICARAGUA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2541_1900_19AQMM19D0066_1900/",
    "Actor: Marlon Blackwell Architects, P.A. (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx; Nicaragua under-covered.",
    "hunt_cycle922",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM23F2541_1900_19AQMM19D0066_1900 (Blackwell; Managua design). Signed 28 "
    "September 2023. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2541_1900_19AQMM19D0066_1900/.",
    "USASpending: Blackwell Managua design USD 0.910m. Supports blackwell_managua_design_910k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 910,290.44; date_signed 2023-09-28.",
)
row_doc(
    "palgag_us_modular_481k_2017",
    "infrastructure", "building_materials", "us",
    "Palgag US LLC — Haiti modular construction (2017 award)",
    "Haiti",
    "12 Sep 2017: Department of State awards contract SAQMMA17C0235 to Palgag US LLC for Haiti "
    "modular construction; obligated USD 481,375.78. CapEx face = award obligation. Distinct from "
    "palgag_us_modular_1p73m_2016.",
    "481375.78", "2017-09-12", "2017", "18.540", "-72.340",
    "Haiti modular construction (USASpending PoP Haiti; Port-au-Prince approximate).",
    "usaspending_palgag_us_modular_20170912",
    "HAITI MODULAR IGF::OT::IGF IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0235_1900_-NONE-_-NONE-/",
    "Actor: Palgag US LLC (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle922",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0235_1900_-NONE-_-NONE- "
    "(Palgag US; Haiti modular 2017). Signed 12 September 2017. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0235_1900_-NONE-_-NONE-/.",
    "USASpending: Palgag US modular 2017 USD 0.481m. Supports palgag_us_modular_481k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 481,375.78; date_signed 2017-09-12.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    supports = entry.get("supports") or []
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        prev = existing.get("supports") or []
        for s in supports:
            if s not in prev:
                prev.append(s)
        existing.update(entry)
        existing["supports"] = prev
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added = []
    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        upsert_bib(bib, bib_by, bib_entry)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})
    BIB.write_text(yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8")
    print(f"cycles920-922 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
