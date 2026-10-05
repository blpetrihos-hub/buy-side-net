#!/usr/bin/env python3
"""Cycles 939–941: USASpending page-2 residual CapEx.

Seeds: 20261939–20261941. Thin top-up dry.
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


# === 939 ===
row_doc(
    "sea_pac_san_jose_elevator_899k_2024",
    "infrastructure", "engineering_epc", "us",
    "Sea Pac Engineering Inc. — San José embassy elevator replacement design/build",
    "Costa Rica",
    "26 Sep 2024: Department of State awards contract 19GE5024C0051 to Sea Pac Engineering Inc. for "
    "U.S. Embassy San José, Costa Rica design/build elevator replacement and modernization; "
    "obligated USD 899,030. CapEx face = award obligation.",
    "899030", "2024-09-26", "2024", "9.928", "-84.091",
    "Elevator replacement/modernization, U.S. Embassy San José, Costa Rica (USASpending PoP Costa Rica).",
    "usaspending_sea_pac_san_jose_elevator_20240926",
    "U.S. EMBASSY SAN JOSE, COSTA RICA. DESIGN/BUILD ELEVATOR REPLACEMENT AND MODERNIZATION PRO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024C0051_1900_-NONE-_-NONE-/",
    "Actor: Sea Pac Engineering Inc. (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle939",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19GE5024C0051_1900_-NONE-_-NONE- (Sea Pac; San José elevator). Signed 26 September "
    "2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024C0051_1900_-NONE-_-NONE-/.",
    "USASpending: Sea Pac San José elevator USD 0.899m. Supports sea_pac_san_jose_elevator_899k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 899,030; date_signed 2024-09-26.",
)
row_doc(
    "sea_pac_san_salvador_elevators_2p82m_2022",
    "infrastructure", "engineering_epc", "us",
    "Sea Pac Engineering Inc. — San Salvador five-elevator modernization design/build",
    "El Salvador",
    "21 Sep 2022: Department of State awards contract 19GE5022C0039 to Sea Pac Engineering Inc. for "
    "San Salvador design/build elevator modernization of five elevators; obligated USD 2,818,539.88. "
    "CapEx face = award obligation. Distinct from sea_pac_san_jose_elevator_899k_2024 / "
    "nbc_san_salvador_roof_5p68m_2018.",
    "2818539.88", "2022-09-21", "2022", "13.693", "-89.219",
    "Five-elevator modernization, San Salvador, El Salvador (USASpending PoP El Salvador).",
    "usaspending_sea_pac_san_salvador_elev_20220921",
    "SAN SALVADOR, DESIGN/BUILD ELEVATOR MODERNIZATION OF FIVE ELEVATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5022C0039_1900_-NONE-_-NONE-/",
    "Actor: Sea Pac Engineering Inc. (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle939",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19GE5022C0039_1900_-NONE-_-NONE- (Sea Pac; San Salvador elevators). Signed 21 "
    "September 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5022C0039_1900_-NONE-_-NONE-/.",
    "USASpending: Sea Pac San Salvador elevators USD 2.819m. Supports sea_pac_san_salvador_elevators_2p82m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,818,539.88; date_signed 2022-09-21.",
)
row_doc(
    "serrano_namru6_admin_3p72m_2017",
    "infrastructure", "building_materials", "other",
    "Serrano Proaño — NAMRU-6 admin building renovation and addition (Lima)",
    "Peru",
    "29 Sep 2017: USACE awards task order W9127817F0487 to Serrano Proaño Diseño y Construcción S.A. "
    "for NAMRU-6 admin building renovation and addition; obligated USD 3,719,576.53. CapEx face = "
    "award obligation. Distinct from palgag_namru6_lima_25p4m_2018.",
    "3719576.53", "2017-09-29", "2017", "-12.046", "-77.043",
    "NAMRU-6 admin building renovation/addition, Lima, Peru (USASpending PoP Peru).",
    "usaspending_serrano_namru6_admin_20170929",
    "IGF::OT::IGF NAMRU-6 ADMIN BLDG RENOVATION&ADDITION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0487_9700_W9127813D0014_9700/",
    "Actor: Serrano Proaño (Ecuador/Quito) under DoD/USACE — other. Official USASpending Award API. "
    "Shuffle building_materials.",
    "hunt_cycle939",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127817F0487_9700_W9127813D0014_9700 (Serrano; NAMRU-6 admin). Signed 29 September "
    "2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0487_9700_W9127813D0014_9700/.",
    "USASpending: Serrano NAMRU-6 admin USD 3.720m. Supports serrano_namru6_admin_3p72m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,719,576.53; date_signed 2017-09-29.",
)
row_doc(
    "horizon_brasilia_fcu_1p77m_2018",
    "infrastructure", "building_materials", "us",
    "Horizon Construction Group / ICS JV — Brasília fan coil units replacement",
    "Brazil",
    "26 Sep 2018: Department of State awards task order 19AQMM18F4595 to Horizon Construction Group / "
    "ICS JV for fan coil units replacement at U.S. Embassy Brasília; obligated USD 1,772,168. CapEx "
    "face = award obligation. Distinct from horizon_brasilia_cw_elec_5p56m_2017.",
    "1772168", "2018-09-26", "2018", "-15.797", "-47.892",
    "Fan coil units replacement, U.S. Embassy Brasília, Brazil (USASpending PoP Brazil).",
    "usaspending_horizon_brasilia_fcu_20180926",
    "FAN COIL UNITS REPLACEMENT PROJECT AT THE U.S. EMBASSY IN BRASILIA, BRAZIL.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4595_1900_SAQMMA14D0056_1900/",
    "Actor: Horizon Construction Group / ICS JV (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle939",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM18F4595_1900_SAQMMA14D0056_1900 (Horizon; Brasília FCU). Signed 26 September "
    "2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4595_1900_SAQMMA14D0056_1900/.",
    "USASpending: Horizon Brasília FCU USD 1.772m. Supports horizon_brasilia_fcu_1p77m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,772,168; date_signed 2018-09-26.",
)
row_doc(
    "eterna_el_coca_boat_1p29m_2022",
    "infrastructure", "building_materials", "other",
    "Eterna — El Coca boat maintenance facility design/build",
    "Ecuador",
    "22 Sep 2022: USACE awards task order W9127822F0385 to Eterna for D/B boat maintenance facility, "
    "El Coca, Ecuador; obligated USD 1,286,730.56. CapEx face = award obligation. Distinct from "
    "ped_jamaica_boat_facility_2p53m_2023.",
    "1286730.56", "2022-09-22", "2022", "-0.462", "-76.987",
    "Boat maintenance facility, El Coca (Puerto Francisco de Orellana), Ecuador (USASpending PoP Ecuador).",
    "usaspending_eterna_el_coca_boat_20220922",
    "D/B BOAT MAINTENANCE FACILITY, EL COCA, ECUADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0385_9700_W9127817D0095_9700/",
    "Actor: Eterna (Honduras) under DoD/USACE — other. Official USASpending Award API. Shuffle "
    "building_materials.",
    "hunt_cycle939",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127822F0385_9700_W9127817D0095_9700 (Eterna; El Coca boat). Signed 22 September "
    "2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0385_9700_W9127817D0095_9700/.",
    "USASpending: Eterna El Coca boat facility USD 1.287m. Supports eterna_el_coca_boat_1p29m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,286,730.56; date_signed 2022-09-22.",
)

# === 940 ===
row_doc(
    "serrano_shushufindi_hospital_1p31m_2021",
    "infrastructure", "building_materials", "other",
    "Serrano Proaño — Shushufindi hospital repair and construction",
    "Ecuador",
    "6 Jul 2021: USACE awards task order W9127821F0218 to Serrano Proaño for repair and construction "
    "of hospital in Shushufindi, Ecuador; obligated USD 1,309,663.97. CapEx face = award obligation.",
    "1309663.97", "2021-07-06", "2021", "-0.187", "-76.645",
    "Hospital repair/construction, Shushufindi, Sucumbíos, Ecuador (USASpending PoP Ecuador).",
    "usaspending_serrano_shushufindi_20210706",
    "REPAIR AND CONSTRUCTION OF HOSPITAL IN SHUSHUFINDI, ECUADOR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0218_9700_W9127817D0098_9700/",
    "Actor: Serrano Proaño (Ecuador) under DoD/USACE — other. Official USASpending Award API. "
    "Shuffle building_materials.",
    "hunt_cycle940",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127821F0218_9700_W9127817D0098_9700 (Serrano; Shushufindi hospital). Signed 6 July "
    "2021. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0218_9700_W9127817D0098_9700/.",
    "USASpending: Serrano Shushufindi hospital USD 1.310m. Supports serrano_shushufindi_hospital_1p31m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,309,663.97; date_signed 2021-07-06.",
)
row_doc(
    "palgag_dr_peb_711k_2009",
    "infrastructure", "building_materials", "allied",
    "Palgag Building Technologies Ltd — Dominican Republic PEB / obstacle / MOUT / checkpoint",
    "Dominican Republic",
    "3 Nov 2009: DoD awards contract N6945010C0002 to Palgag Building Technologies Ltd for "
    "pre-engineered building (PEB), obstacle course, MOUT site, and checkpoint, Dominican Republic; "
    "obligated USD 710,700. CapEx face = award obligation.",
    "710700", "2009-11-03", "2009", "18.486", "-69.931",
    "PEB / obstacle / MOUT / checkpoint facilities, Dominican Republic (USASpending PoP Dominican "
    "Republic; national pin).",
    "usaspending_palgag_dr_peb_20091103",
    "PRE-ENGINEERED BUILDING (PEB); OBSTACLE COURSE; MOUT SITE; CHECK POINT; DOMINICAN REPUBLIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0002_9700_-NONE-_-NONE-/",
    "Actor: Palgag Building Technologies Ltd (Israel) under DoD — allied. Official USASpending Award "
    "API. Shuffle building_materials.",
    "hunt_cycle940",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_N6945010C0002_9700_-NONE-_-NONE- (Palgag; DR PEB). Signed 3 November 2009. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0002_9700_-NONE-_-NONE-/.",
    "USASpending: Palgag DR PEB USD 0.711m. Supports palgag_dr_peb_711k_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 710,700; date_signed 2009-11-03.",
)
row_doc(
    "fortuna_isla_saona_pier_792k_2011",
    "infrastructure", "port_ownership", "other",
    "J. Fortuna Constructora S.R.L. — Isla Saona pier construction",
    "Dominican Republic",
    "28 Sep 2011: DoD awards contract N6945011C0085 to J. Fortuna Constructora S.R.L. for "
    "construction of pier, Isla Saona, Dominican Republic; obligated USD 791,901.11. CapEx face = "
    "award obligation.",
    "791901.11", "2011-09-28", "2011", "18.152", "-68.700",
    "Pier construction, Isla Saona, Dominican Republic (USASpending PoP Dominican Republic).",
    "usaspending_fortuna_isla_saona_pier_20110928",
    "CONSTRUCTION OF PIER, ISLA SAONA, DOMINICAN REPUBLIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0085_9700_-NONE-_-NONE-/",
    "Actor: J. Fortuna Constructora S.R.L. (Dominican Republic) under DoD — other. Official "
    "USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle940",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_N6945011C0085_9700_-NONE-_-NONE- (Fortuna; Isla Saona pier). Signed 28 September "
    "2011. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0085_9700_-NONE-_-NONE-/.",
    "USASpending: Fortuna Isla Saona pier USD 0.792m. Supports fortuna_isla_saona_pier_792k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 791,901.11; date_signed 2011-09-28.",
)
row_doc(
    "marenco_dr_boat_ramp_pier_930k_2009",
    "infrastructure", "port_ownership", "other",
    "Marenco Ltd — Dominican Republic boat ramp, access and pier",
    "Dominican Republic",
    "25 Sep 2009: DoD awards contract N6945009C0096 to Marenco Ltd for boat ramp, access and pier, "
    "Dominican Republic; obligated USD 930,481. CapEx face = award obligation. Distinct from "
    "fortuna_isla_saona_pier_792k_2011.",
    "930481", "2009-09-25", "2009", "18.486", "-69.931",
    "Boat ramp, access and pier, Dominican Republic (USASpending PoP Dominican Republic; national pin).",
    "usaspending_marenco_dr_pier_20090925",
    "BOAT RAMP, ACCESS & PIER; DOMINICAN REPUBLIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945009C0096_9700_-NONE-_-NONE-/",
    "Actor: Marenco Ltd under DoD — other (PoP Dominican Republic; recipient location blank on "
    "award). Official USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle940",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_N6945009C0096_9700_-NONE-_-NONE- (Marenco; DR boat ramp/pier). Signed 25 September "
    "2009. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945009C0096_9700_-NONE-_-NONE-/.",
    "USASpending: Marenco DR boat ramp/pier USD 0.930m. Supports marenco_dr_boat_ramp_pier_930k_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 930,481; date_signed 2009-09-25.",
)
row_doc(
    "mesan_bridgetown_cmr_perimeter_619k_2009",
    "infrastructure", "building_materials", "us",
    "Mesan-Martinez JV — Bridgetown CMR perimeter security upgrade",
    "Barbados",
    "14 Sep 2009: Department of State awards task order SWHARC09F0058 to Mesan-Martinez Joint Venture "
    "LLP for perimeter security upgrade of Chief of Mission Residence in Bridgetown, Barbados; "
    "obligated USD 618,896. CapEx face = award obligation.",
    "618896", "2009-09-14", "2009", "13.097", "-59.615",
    "CMR perimeter security upgrade, Bridgetown, Barbados (USASpending PoP Barbados).",
    "usaspending_mesan_bridgetown_cmr_20090914",
    "PERIMETER SECURITY UPGRADE OF CHIEF OF MISSION RESIDENCE IN BRIDGETOWN, BARBADOS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC09F0058_1900_SAQMMA08D0015_1900/",
    "Actor: Mesan-Martinez JV (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle940",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SWHARC09F0058_1900_SAQMMA08D0015_1900 (Mesan; Bridgetown CMR). Signed 14 September "
    "2009. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC09F0058_1900_SAQMMA08D0015_1900/.",
    "USASpending: Mesan Bridgetown CMR perimeter USD 0.619m. Supports mesan_bridgetown_cmr_perimeter_619k_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 618,896; date_signed 2009-09-14.",
)

# === 941 ===
row_doc(
    "eterna_scab_grid_9p71m_2020",
    "energy", "power_plants_grid", "other",
    "Eterna — Soto Cano primary electrical grid repair",
    "Honduras",
    "28 Sep 2020: USACE awards task order W9127820F0498 to Eterna for repair primary electrical "
    "grid, SCAB (Soto Cano Air Base); obligated USD 9,705,265.43. CapEx face = award obligation. "
    "Distinct from eterna_soto_cano_pv_8p14m_2018 / eterna_soto_cano_bridge_7p64m_2021.",
    "9705265.43", "2020-09-28", "2020", "14.382", "-87.621",
    "Primary electrical grid repair, Soto Cano Air Base, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_scab_grid_20200928",
    "REPAIR PRIMARY ELECTRICAL GRID, SCAB",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0498_9700_W9127816D0102_9700/",
    "Actor: Eterna (Honduras) under DoD/USACE — other. Official USASpending Award API. Shuffle "
    "power_plants_grid.",
    "hunt_cycle941",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127820F0498_9700_W9127816D0102_9700 (Eterna; SCAB grid). Signed 28 September 2020. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0498_9700_W9127816D0102_9700/.",
    "USASpending: Eterna SCAB grid USD 9.705m. Supports eterna_scab_grid_9p71m_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9,705,265.43; date_signed 2020-09-28.",
)
row_doc(
    "eterna_honduras_fy23_db_7p00m_2023",
    "infrastructure", "building_materials", "other",
    "Eterna — Honduras FY23 two-phase design-build construction requirements",
    "Honduras",
    "29 Sep 2023: USACE awards contract W9127823C0031 to Eterna for two-phase design-build FY23 "
    "construction requirements in Honduras, Central America; obligated USD 7,003,614.61. CapEx "
    "face = award obligation.",
    "7003614.61", "2023-09-29", "2023", "14.072", "-87.192",
    "FY23 design-build construction requirements, Honduras (USASpending PoP Honduras; national pin).",
    "usaspending_eterna_honduras_fy23_20230929",
    "TWO-PHASE DESIGN-BUILD FY23 CONSTRUCTION REQUIREMENTS IN HONDURAS, CENTRAL AMERICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823C0031_9700_-NONE-_-NONE-/",
    "Actor: Eterna (Honduras) under DoD/USACE — other. Official USASpending Award API. Shuffle "
    "building_materials.",
    "hunt_cycle941",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127823C0031_9700_-NONE-_-NONE- (Eterna; Honduras FY23 DB). Signed 29 September "
    "2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823C0031_9700_-NONE-_-NONE-/.",
    "USASpending: Eterna Honduras FY23 DB USD 7.004m. Supports eterna_honduras_fy23_db_7p00m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7,003,614.61; date_signed 2023-09-29.",
)
row_doc(
    "nv5_brasilia_nec_cx_2p09m_2019",
    "infrastructure", "engineering_epc", "us",
    "NV5 Consultants, Inc. — Brasília NEC commissioning design services",
    "Brazil",
    "30 Jul 2019: Department of State awards task order 19AQMM19F2509 to NV5 Consultants, Inc. for "
    "commissioning design services for Brasília NEC D/B/B project; obligated USD 2,089,737. CapEx "
    "face = award obligation. Distinct from vistas_brasilia_db / studio_gang_brasilia_nec_design.",
    "2089737", "2019-07-30", "2019", "-15.797", "-47.892",
    "NEC commissioning design services, Brasília, Brazil (USASpending PoP Brazil).",
    "usaspending_nv5_brasilia_nec_cx_20190730",
    "COMMISSIONING DESIGN SERVICES FOR BRASILIA NEC D/B/B PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F2509_1900_19AQMM19D0019_1900/",
    "Actor: NV5 Consultants, Inc. (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle941",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM19F2509_1900_19AQMM19D0019_1900 (NV5; Brasília NEC CX). Signed 30 July 2019. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F2509_1900_19AQMM19D0019_1900/.",
    "USASpending: NV5 Brasília NEC CX USD 2.090m. Supports nv5_brasilia_nec_cx_2p09m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,089,737; date_signed 2019-07-30.",
)
row_doc(
    "sterling_royale_brasilia_db_2p64m_2010",
    "infrastructure", "building_materials", "us",
    "The Sterling Royale Group — Brasília design/construction",
    "Brazil",
    "20 Sep 2010: Department of State awards task order SAQMMA10F4384 to The Sterling Royale Group "
    "for design/construction (PoP Brazil); obligated USD 2,638,061.65. CapEx face = award "
    "obligation.",
    "2638061.65", "2010-09-20", "2010", "-15.797", "-47.892",
    "Design/construction, Brasília / Brazil diplomatic facilities (USASpending PoP Brazil).",
    "usaspending_sterling_royale_brasilia_20100920",
    "DESIGN/CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F4384_1900_SAQMMA08D0038_1900/",
    "Actor: The Sterling Royale Group (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle941",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA10F4384_1900_SAQMMA08D0038_1900 (Sterling Royale; Brasília DB). Signed 20 "
    "September 2010. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F4384_1900_SAQMMA08D0038_1900/.",
    "USASpending: Sterling Royale Brasília USD 2.638m. Supports sterling_royale_brasilia_db_2p64m_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,638,061.65; date_signed 2010-09-20.",
)
row_doc(
    "bendig_oij_incinerator_983k_2021",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig S.A. — OIJ Poder Judicial incinerator building",
    "Costa Rica",
    "27 Sep 2021: Department of State awards contract 19AQMM21C0172 to Industrias Bendig S.A. for "
    "OIJ Poder Judicial incinerator building, Costa Rica; obligated USD 983,275.80. CapEx face = "
    "award obligation. Distinct from bendig_sierpe_base_camp_1p41m_2022.",
    "983275.80", "2021-09-27", "2021", "9.928", "-84.091",
    "OIJ Poder Judicial incinerator building, Costa Rica (USASpending PoP Costa Rica; San José pin).",
    "usaspending_bendig_oij_incinerator_20210927",
    "OIJ PODER JUDICIAL - INCINERATOR BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21C0172_1900_-NONE-_-NONE-/",
    "Actor: Industrias Bendig S.A. (Costa Rica) under State — other. Official USASpending Award "
    "API. Shuffle building_materials.",
    "hunt_cycle941",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM21C0172_1900_-NONE-_-NONE- (Bendig; OIJ incinerator). Signed 27 September 2021. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21C0172_1900_-NONE-_-NONE-/.",
    "USASpending: Bendig OIJ incinerator USD 0.983m. Supports bendig_oij_incinerator_983k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 983,275.80; date_signed 2021-09-27.",
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
    print(f"cycles939-941 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
