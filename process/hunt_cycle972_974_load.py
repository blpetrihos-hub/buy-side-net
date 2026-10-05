#!/usr/bin/env python3
"""Cycles 972–974: USASpending LatAm CapEx residual (~USD0.67–0.90m).

Seeds: 20261972–20261974. Thin top-up dry.
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


# === Cycle 972 ===
row_doc(
    "boland_trane_caracas_chiller_902k_2016",
    "infrastructure", "building_materials", "us",
    "Boland Trane Services — Caracas chiller replacement",
    "Venezuela",
    "30 Sep 2016: Department of State awards contract SAQMMA16M2941 to Boland Trane Services for Caracas, Venezuela chiller replacement; obligated USD 902,091.85. CapEx face = award obligation.",
    "902091.85", "2016-09-30", "2016", "10.480", "-66.903",
    "Caracas chiller replacement (USASpending description; Caracas pin).",
    "usaspending_boland_trane_caracas_chiller_902k_2016",
    "IGF::OT::IGF CARACAS, VENEZUELA CHILLER REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M2941_1900_-NONE-_-NONE-/",
    "Actor: Boland Trane Services Inc. (Gaithersburg MD, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx; Venezuela beyond solar.",
    "hunt_cycle972",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16M2941_1900_-NONE-_-NONE- (Boland Trane Caracas chiller). Signed 2016-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M2941_1900_-NONE-_-NONE-/.",
    "USASpending: Boland Trane Caracas chiller USD 0.902m. Supports boland_trane_caracas_chiller_902k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 902091.85; date_signed 2016-09-30.",
)

row_doc(
    "hulke_freeport_warehouse_895k_2012",
    "infrastructure", "building_materials", "us",
    "Hulke Construction — Freeport emergency relief warehouse",
    "Bahamas",
    "12 Sep 2012: Department of Defense awards contract N6945012C0048 to Hulke Construction for construction of an emergency relief warehouse in Freeport, Bahamas; obligated USD 895,488.97. CapEx face = award obligation.",
    "895488.97", "2012-09-12", "2012", "26.533", "-78.696",
    "Emergency relief warehouse, Freeport, Bahamas (USASpending description).",
    "usaspending_hulke_freeport_warehouse_895k_2012",
    "CONSTRUCT EMERGENCY RELIEF WAREHOUSE, FREEPORT, BAHAMAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945012C0048_9700_-NONE-_-NONE-/",
    "Actor: Hulke Construction Company LLC (Sanford FL, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle972",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945012C0048_9700_-NONE-_-NONE- (Hulke Freeport warehouse). Signed 2012-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945012C0048_9700_-NONE-_-NONE-/.",
    "USASpending: Hulke Freeport warehouse USD 0.895m. Supports hulke_freeport_warehouse_895k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 895488.97; date_signed 2012-09-12.",
)

row_doc(
    "misc_managua_power_feeder_892k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Managua dedicated power feeder",
    "Nicaragua",
    "28 Sep 2011: Department of State awards contract SAQMMA11M1699 for construction of a dedicated power feeder in Managua, Nicaragua; obligated USD 891,775. CapEx face = award obligation. Recipient redacted as miscellaneous foreign awardees.",
    "891775", "2011-09-28", "2011", "12.136", "-86.251",
    "Dedicated power feeder, Managua, Nicaragua (USASpending description; Managua pin).",
    "usaspending_misc_managua_power_feeder_892k_2011",
    "CONSTRUCTION OF DEDICATED POWER FEEDER IN MANAGUA, NICARAGUA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11M1699_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle972",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11M1699_1900_-NONE-_-NONE- (Managua power feeder). Signed 2011-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11M1699_1900_-NONE-_-NONE-/.",
    "USASpending: Managua dedicated power feeder USD 0.892m. Supports misc_managua_power_feeder_892k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 891775; date_signed 2011-09-28.",
)

row_doc(
    "mesan_kingston_avr_887k_2011",
    "energy", "power_plants_grid", "us",
    "Mesan-Martinez JV — Kingston automated voltage regulator replacement",
    "Jamaica",
    "15 Sep 2011: Department of State awards task order SAQMMA11F3644 to Mesan-Martinez Joint Venture for design-build automated voltage regulator replacement in Kingston, Jamaica; obligated USD 887,400. CapEx face = award obligation.",
    "887400", "2011-09-15", "2011", "18.017", "-76.810",
    "Automated voltage regulator replacement, Kingston, Jamaica (USASpending description).",
    "usaspending_mesan_kingston_avr_887k_2011",
    "DESIGN BUILD AUTOMATED VOLTAGE REGULATOR REPLACEMENT IN KINGSTON, JAMAICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3644_1900_SAQMMA11D0062_1900/",
    "Actor: Mesan-Martinez Joint Venture LLP (Parker CO, U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle972",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F3644_1900_SAQMMA11D0062_1900 (Mesan Kingston AVR). Signed 2011-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3644_1900_SAQMMA11D0062_1900/.",
    "USASpending: Mesan Kingston AVR USD 0.887m. Supports mesan_kingston_avr_887k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 887400; date_signed 2011-09-15.",
)

row_doc(
    "marago_santa_marta_lodging_847k_2020",
    "infrastructure", "building_materials", "other",
    "Constructora Marago — Santa Marta lodging facilities",
    "Colombia",
    "4 Feb 2020: Department of State awards contract 19AQMM20C0036 to Constructora Marago for construction and renovation of lodging facilities in Santa Marta, Colombia; obligated USD 846,539.29. CapEx face = award obligation.",
    "846539.29", "2020-02-04", "2020", "11.241", "-74.199",
    "Lodging facilities, Santa Marta, Colombia (USASpending description).",
    "usaspending_marago_santa_marta_lodging_847k_2020",
    "CONSTRUCTION AND RENOVATION OF LODGING FACILITIES IN SANTA MARTA, COLOMBIA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0036_1900_-NONE-_-NONE-/",
    "Actor: Constructora Marago S.A.S. (Bogotá, Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle972",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20C0036_1900_-NONE-_-NONE- (Marago Santa Marta lodging). Signed 2020-02-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0036_1900_-NONE-_-NONE-/.",
    "USASpending: Marago Santa Marta lodging USD 0.847m. Supports marago_santa_marta_lodging_847k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 846539.29; date_signed 2020-02-04.",
)

# === Cycle 973 ===
row_doc(
    "akj_mexico_seneca_reno_799k_2024",
    "infrastructure", "building_materials", "other",
    "Servicios AKJ — U.S. Embassy Mexico City Seneca building renovation",
    "Mexico",
    "19 Aug 2024: Department of State awards contract 19GE5024C0022 to Servicios AKJ for U.S. Embassy Mexico City Seneca building renovation project; obligated USD 798,653.09. CapEx face = award obligation.",
    "798653.09", "2024-08-19", "2024", "19.432", "-99.133",
    "Seneca building renovation, U.S. Embassy Mexico City (USASpending description).",
    "usaspending_akj_mexico_seneca_reno_799k_2024",
    "U.S. EMBASSY MEXICO CITY, MEXICO. SENECA BUILDING RENOVATION PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024C0022_1900_-NONE-_-NONE-/",
    "Actor: Servicios AKJ S.A. de C.V. (Ciudad de México) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle973",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5024C0022_1900_-NONE-_-NONE- (AKJ Seneca renovation). Signed 2024-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024C0022_1900_-NONE-_-NONE-/.",
    "USASpending: AKJ Seneca renovation USD 0.799m. Supports akj_mexico_seneca_reno_799k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 798653.09; date_signed 2024-08-19.",
)

row_doc(
    "proyectos_rio_sidra_clinic_759k_2011",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles — HAP medical clinic Rio Sidra (Kuna Yala)",
    "Panama",
    "12 Sep 2011: U.S. Army Corps of Engineers awards contract W912CL11C0033 to Proyectos Civiles for SOUTHCOM HAP construction of a medical clinic in Rio Sidra community, Corregimiento Nargana, Comarca de Kuna Yala, Panama; obligated USD 758,898.14. CapEx face = award obligation.",
    "758898.14", "2011-09-12", "2011", "9.440", "-78.580",
    "Medical clinic, Rio Sidra / Nargana, Comarca de Kuna Yala, Panama (USASpending description; approximate community pin).",
    "usaspending_proyectos_rio_sidra_clinic_759k_2011",
    "THIS IS A UNITED STATES SOUTHERN COMMAND HUMANITARIAN ASSISTANCE PROJECT (HAP) FOR THE CONSTRUCTION OF MEDICAL CLINIC. THIS HAP PROJECT WILL BE LOCATED IN RIO SIDRA COMMUNITY, CORREGIMIENTO NARGANA, KUNA YALA DISTRICT, COMARCA DE KUNA YALA-PANAMA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0033_9700_-NONE-_-NONE-/",
    "Actor: Proyectos Civiles S y M Limitada (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle973",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL11C0033_9700_-NONE-_-NONE- (Proyectos Rio Sidra clinic). Signed 2011-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0033_9700_-NONE-_-NONE-/.",
    "USASpending: Proyectos Rio Sidra clinic USD 0.759m. Supports proyectos_rio_sidra_clinic_759k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 758898.14; date_signed 2011-09-12.",
)

row_doc(
    "tmc_teacapan_aircraft_750k_2021",
    "infrastructure", "building_materials", "us",
    "Technology Management Company — Teacapan aircraft structure construction",
    "Mexico",
    "28 Sep 2021: Department of Defense awards task order FA489021F0076 to Technology Management Company for NORTHCOM aircraft structure construction at Teacapan, Mexico; obligated USD 749,700. CapEx face = award obligation.",
    "749700", "2021-09-28", "2021", "22.540", "-105.750",
    "Aircraft structure construction, Teacapan, Mexico (USASpending description).",
    "usaspending_tmc_teacapan_aircraft_750k_2021",
    "NORTHCOM AIRCRAFT STRUCTURE--TEACAPAN (MEXICO) CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489021F0076_9700_FA489016D0015_9700/",
    "Actor: Technology Management Company Inc. (Albuquerque NM, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle973",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489021F0076_9700_FA489016D0015_9700 (TMC Teacapan). Signed 2021-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489021F0076_9700_FA489016D0015_9700/.",
    "USASpending: TMC Teacapan aircraft structure USD 0.750m. Supports tmc_teacapan_aircraft_750k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 749700; date_signed 2021-09-28.",
)

row_doc(
    "proyectos_caucasia_cefop_lodging_750k_2017",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles — CEFOP lodging building (3), Finca Paraguay Caucasia",
    "Colombia",
    "29 Sep 2017: Department of State awards contract SAQMMA17C0202 to Proyectos Civiles for CEFOP lodging building (3) in Finca Paraguay, Caucasia at the CNP base; obligated USD 749,642.76. CapEx face = award obligation. Distinct from later Caucasia Proyectos/EEI awards.",
    "749642.76", "2017-09-29", "2017", "7.987", "-75.198",
    "CEFOP lodging building (3), Finca Paraguay / Caucasia CNP base, Colombia (USASpending description).",
    "usaspending_proyectos_caucasia_cefop_lodging_750k_2017",
    "CEFOP LODGING BUILDING (3) IN FINCA PARAGUAY, CAUCASIA AT THE CNP BASEIGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0202_1900_-NONE-_-NONE-/",
    "Actor: Proyectos Civiles S y M Limitada (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle973",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0202_1900_-NONE-_-NONE- (Proyectos Caucasia CEFOP lodging). Signed 2017-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0202_1900_-NONE-_-NONE-/.",
    "USASpending: Proyectos Caucasia CEFOP lodging USD 0.750m. Supports proyectos_caucasia_cefop_lodging_750k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 749642.76; date_signed 2017-09-29.",
)

row_doc(
    "equipos_comayagua_reno_747k_2016",
    "infrastructure", "building_materials", "other",
    "Equipos de Construcción — Comayagua renovation",
    "Honduras",
    "16 Aug 2016: Department of State awards contract SAQMMA16C0193 to Equipos de Construcción for renovation in Comayagua, Honduras; obligated USD 746,884.10. CapEx face = award obligation.",
    "746884.10", "2016-08-16", "2016", "14.460", "-87.643",
    "Renovation works, Comayagua, Honduras (USASpending description; Comayagua pin).",
    "usaspending_equipos_comayagua_reno_747k_2016",
    "RENOVATION IN COMAYAGUA,HONDURAS IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0193_1900_-NONE-_-NONE-/",
    "Actor: Equipos de Construcción S.A. de C.V. (Tegucigalpa) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle973",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16C0193_1900_-NONE-_-NONE- (Equipos Comayagua renovation). Signed 2016-08-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0193_1900_-NONE-_-NONE-/.",
    "USASpending: Equipos Comayagua renovation USD 0.747m. Supports equipos_comayagua_reno_747k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 746884.10; date_signed 2016-08-16.",
)

# === Cycle 974 ===
row_doc(
    "consolidated_mexico_scanner_747k_2017",
    "infrastructure", "building_materials", "us",
    "Consolidated Construction — Mexico border scanner site infrastructure",
    "Mexico",
    "1 Jun 2017: Department of State awards contract SAQMMA17C0136 to Consolidated Construction & Engineering for construction of scanner site infrastructure on the Mexico border; obligated USD 746,500. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "746500", "2017-06-01", "2017", "", "",
    "Scanner site infrastructure on the Mexico border (USASpending description; site not named — lat/lon blank).",
    "usaspending_consolidated_mexico_scanner_747k_2017",
    "CONSTRUCTION SCANNER SITE INFRASTRUCTURE ON THE MEXICO BORDER IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0136_1900_-NONE-_-NONE-/",
    "Actor: Consolidated Construction & Engineering Company Inc. (Germantown MD, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle974",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0136_1900_-NONE-_-NONE- (Consolidated Mexico scanner). Signed 2017-06-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0136_1900_-NONE-_-NONE-/.",
    "USASpending: Consolidated Mexico scanner site USD 0.747m. Supports consolidated_mexico_scanner_747k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 746500; date_signed 2017-06-01.",
)

row_doc(
    "cg_tto_police_academy_745k_2019",
    "infrastructure", "building_materials", "other",
    "CG Construction — Trinidad Police Academy scene house",
    "Trinidad and Tobago",
    "30 Apr 2019: Department of State awards contract 19AQMM19C0042 to CG Construction Services for renovation and construction at the Police Academy scene house in Trinidad and Tobago; obligated USD 744,664.02. CapEx face = award obligation.",
    "744664.02", "2019-04-30", "2019", "10.667", "-61.519",
    "Police Academy scene house, Trinidad and Tobago (USASpending description; Port of Spain area pin).",
    "usaspending_cg_tto_police_academy_745k_2019",
    "THIS CONTRACT IS FOR RENOVATION AND CONSTRUCTION SERVICES AT THE POLICE ACADEMY SCENE HOUSE IN TRINIDAD AND TOBAGO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0042_1900_-NONE-_-NONE-/",
    "Actor: CG Construction Services Limited (Port of Spain) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle974",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0042_1900_-NONE-_-NONE- (CG TTO Police Academy). Signed 2019-04-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0042_1900_-NONE-_-NONE-/.",
    "USASpending: CG TTO Police Academy USD 0.745m. Supports cg_tto_police_academy_745k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 744664.02; date_signed 2019-04-30.",
)

row_doc(
    "eei_cnp_utilities_740k_2017",
    "infrastructure", "building_materials", "other",
    "EEI — CNP utilities and site construction works",
    "Colombia",
    "29 Sep 2017: Department of State awards contract SAQMMA17C0210 to Estudios Edificaciones e Interventorías (EEI) for CNP utilities and site construction works, Colombia; obligated USD 739,598.52. CapEx face = award obligation. Site not named beyond CNP — lat/lon blank.",
    "739598.52", "2017-09-29", "2017", "", "",
    "CNP utilities and site construction works, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_eei_cnp_utilities_740k_2017",
    "CNP UTILITIES AND SITE CONSTRUCTION WORKS, COLOMBIAIGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0210_1900_-NONE-_-NONE-/",
    "Actor: EEI S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle974",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0210_1900_-NONE-_-NONE- (EEI CNP utilities). Signed 2017-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0210_1900_-NONE-_-NONE-/.",
    "USASpending: EEI CNP utilities USD 0.740m. Supports eei_cnp_utilities_740k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 739598.52; date_signed 2017-09-29.",
)

row_doc(
    "rogers_bocas_fire_716k_2017",
    "infrastructure", "building_materials", "other",
    "Constructora Rogers — Bocas fire protection Phase II",
    "Panama",
    "15 Aug 2017: Smithsonian awards work order F17CW10481 to Constructora Rogers for Bocas fire protection Phase II construction (SF Project No 0679802); obligated USD 716,036.09. CapEx face = award obligation.",
    "716036.09", "2017-08-15", "2017", "9.340", "-82.250",
    "Bocas fire protection Phase II, Bocas del Toro, Panama (USASpending / Smithsonian work order).",
    "usaspending_rogers_bocas_fire_716k_2017",
    "WORK ORDER FOR BOCAS FIRE PROTECTION PHASE II PROJECT - CONSTRUCTION PHASE; SF PROJECT NO 0679802.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F17CW10481_3300_F15CC10192_3300/",
    "Actor: Constructora Rogers S.A. (CONROSA, Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle974",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F17CW10481_3300_F15CC10192_3300 (Rogers Bocas fire Phase II). Signed 2017-08-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F17CW10481_3300_F15CC10192_3300/.",
    "USASpending: Rogers Bocas fire Phase II USD 0.716m. Supports rogers_bocas_fire_716k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 716036.09; date_signed 2017-08-15.",
)

row_doc(
    "mfg_turbo_lodging_702k_2018",
    "infrastructure", "building_materials", "other",
    "MFG Ingeniería — Turbo admin/lodging building",
    "Colombia",
    "23 Jan 2018: Department of State awards contract 19AQMM18C0016 to MFG Ingeniería for admin/lodging building in Turbo, Colombia; obligated USD 701,684.74. CapEx face = award obligation.",
    "701684.74", "2018-01-23", "2018", "8.095", "-76.728",
    "Admin/lodging building, Turbo, Colombia (USASpending description).",
    "usaspending_mfg_turbo_lodging_702k_2018",
    "ADMIN/LODGING BUILDING IN TURBO, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0016_1900_-NONE-_-NONE-/",
    "Actor: MFG Ingeniería SAS (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle974",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0016_1900_-NONE-_-NONE- (MFG Turbo lodging). Signed 2018-01-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0016_1900_-NONE-_-NONE-/.",
    "USASpending: MFG Turbo lodging USD 0.702m. Supports mfg_turbo_lodging_702k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 701684.74; date_signed 2018-01-23.",
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
    print(f"cycles972-974 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
