#!/usr/bin/env python3
"""Cycles 1363–1367: USASpending LatAm CapEx (FAAC/Virtra/Obera/Tsymmetry/Terrestris + SEOBRA/Vinpar/QA EPC).

Seeds: 20262363–20262367. Thin top-up dry.
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

# === Cycle 1363 ===
row_doc(
    "faac_mexico_firearms_training_simulators_497k_2020",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico firearms training simulators",
    "Mexico",
    "03 Apr 2020: Department of State awards contract to FAAC INCORPORATED for firearms training simulators; obligated USD 497298.11. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "497298.11", "2020-04-03", "2020", "", "",
    "REQUIREMENT FOR FIREARMS TRAINING SIMULATORS., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_firearms_training_simulators_497k_2020",
    "REQUIREMENT FOR FIREARMS TRAINING SIMULATORS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1343_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle fission_smr dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1363",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F1343_1900_SWHARC16D0002_1900 (faac_mexico_firearms_training_simulators_497k_2020). Signed 2020-04-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1343_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_firearms_training_simulators_497k_2020 USD 0.497m. Supports faac_mexico_firearms_training_simulators_497k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 497298.11; date_signed 2020-04-03.",
    investment_type="equipment_supply",
)

# === Cycle 1363 ===
row_doc(
    "obera_bahamas_hq_ops_center_comms_equipment_354k_2021",
    "infrastructure", "engineering_epc", "us",
    "Obera — Bahamas NORTHCOM headquarters operations center communication equipment",
    "Bahamas",
    "27 Sep 2021: Department of Defense awards contract to OBERA LLC for NORTHCOM Bahamas headquarters operations center communication equipment; obligated USD 353862.66. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "353862.66", "2021-09-27", "2021", "", "",
    "NORTHCOM BAHAMAS HEADQUARTERS OPERATIONS CENTER COMMUNICATION EQUIPMENT, Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_obera_bahamas_hq_ops_center_comms_equipment_354k_2021",
    "NORTHCOM BAHAMAS HEADQUARTERS OPERATIONS CENTER COMMUNICATION EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489021F0072_9700_FA489016D0013_9700/",
    "Actor: OBERA LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc CapEx; ≥1/3 U.S. Asset country Bahamas.",
    "hunt_cycle1363",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489021F0072_9700_FA489016D0013_9700 (obera_bahamas_hq_ops_center_comms_equipment_354k_2021). Signed 2021-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489021F0072_9700_FA489016D0013_9700/.",
    "USASpending: obera_bahamas_hq_ops_center_comms_equipment_354k_2021 USD 0.354m. Supports obera_bahamas_hq_ops_center_comms_equipment_354k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 353862.66; date_signed 2021-09-27.",
    investment_type="equipment_supply",
)

# === Cycle 1363 ===
row_doc(
    "seobra_belize_crooked_tree_school_2275k_2013",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Belize Crooked Tree school",
    "Belize",
    "11 Sep 2013: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for Crooked Tree school, Belize; obligated USD 2274512.83. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2274512.83", "2013-09-11", "2013", "", "",
    "CROOKED TREE SCHOOL, BELIZE, Belize (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_belize_crooked_tree_school_2275k_2013",
    "IGF::OT::IGF  CROOKED TREE SCHOOL, BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0023_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx. Named site Belize.",
    "hunt_cycle1363",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127813D0023_9700 (seobra_belize_crooked_tree_school_2275k_2013). Signed 2013-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127813D0023_9700/.",
    "USASpending: seobra_belize_crooked_tree_school_2275k_2013 USD 2.275m. Supports seobra_belize_crooked_tree_school_2275k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2274512.83; date_signed 2013-09-11.",
    investment_type="epc",
)

# === Cycle 1363 ===
row_doc(
    "seobra_peru_sofa_hap_construction_1747k_2016",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Peru SOFA agreement D/B construction HAP",
    "Peru",
    "28 Sep 2016: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for SOFA agreement D/B construction HAP; obligated USD 1746862.99. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1746862.99", "2016-09-28", "2016", "", "",
    "SOFA AGREEMENT D/B CONSTRUCTION HAP, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_peru_sofa_hap_construction_1747k_2016",
    "IGF::OT::IGF SOFA AGREEMENT D/B CONSTRUCTION HAP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127813D0009_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1363",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0008_9700_W9127813D0009_9700 (seobra_peru_sofa_hap_construction_1747k_2016). Signed 2016-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127813D0009_9700/.",
    "USASpending: seobra_peru_sofa_hap_construction_1747k_2016 USD 1.747m. Supports seobra_peru_sofa_hap_construction_1747k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1746862.99; date_signed 2016-09-28.",
    investment_type="epc",
)

# === Cycle 1363 ===
row_doc(
    "seobra_panama_summit_maintenance_facility_1199k_2012",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Panama Summit CN maintenance facility",
    "Panama",
    "22 Sep 2012: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for CN maintenance facility Summit, Panama; obligated USD 1199087.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1199087.00", "2012-09-22", "2012", "", "",
    "CN MAINTENANCE FACILITY SUMMIT, PANAMA, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_panama_summit_maintenance_facility_1199k_2012",
    "CN MAINTENANCE FACILITY SUMMIT, PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127809D0081_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1363",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0009_9700_W9127809D0081_9700 (seobra_panama_summit_maintenance_facility_1199k_2012). Signed 2012-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127809D0081_9700/.",
    "USASpending: seobra_panama_summit_maintenance_facility_1199k_2012 USD 1.199m. Supports seobra_panama_summit_maintenance_facility_1199k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1199087.00; date_signed 2012-09-22.",
    investment_type="epc",
)

# === Cycle 1364 ===
row_doc(
    "virtra_costa_rica_equipment_upgrade_347k_2020",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Costa Rica training equipment upgrade",
    "Costa Rica",
    "24 Jan 2020: Department of State awards contract to VIRTRA, INC. to upgrade equipment under previous order; obligated USD 346648.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "346648.00", "2020-01-24", "2020", "", "",
    "REQUIREMENT TO UPGRADE EQUIPMENT UNDER PREVIOUS ORDER., Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_costa_rica_equipment_upgrade_347k_2020",
    "REQUIREMENT TO UPGRADE EQUIPMENT UNDER PREVIOUS ORDER.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F0523_1900_GS02F0214P_4730/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle port_cranes dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1364",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F0523_1900_GS02F0214P_4730 (virtra_costa_rica_equipment_upgrade_347k_2020). Signed 2020-01-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F0523_1900_GS02F0214P_4730/.",
    "USASpending: virtra_costa_rica_equipment_upgrade_347k_2020 USD 0.347m. Supports virtra_costa_rica_equipment_upgrade_347k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 346648.00; date_signed 2020-01-24.",
    investment_type="equipment_supply",
)

# === Cycle 1364 ===
row_doc(
    "faac_mexico_pgr_firearms_simulators_334k_2016",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico PGR three firearms training simulator systems",
    "Mexico",
    "23 Sep 2016: Department of State awards contract to FAAC INCORPORATED for three firearms training simulator systems for the PGR including installation; obligated USD 334156.47. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "334156.47", "2016-09-23", "2016", "", "",
    "INL MEXICO - THREE (3) FIREARMS TRAINING SIMULATOR SYSTEMS FOR THE PGR. INCLUDES INSTALLAT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_pgr_firearms_simulators_334k_2016",
    "INL MEXICO - THREE (3) FIREARMS TRAINING SIMULATOR SYSTEMS FOR THE PGR. INCLUDES INSTALLATION AND 3-YEAR IN-COUNTRY WARRANTY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0040_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1364",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16F0040_1900_SWHARC16D0002_1900 (faac_mexico_pgr_firearms_simulators_334k_2016). Signed 2016-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0040_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_pgr_firearms_simulators_334k_2016 USD 0.334m. Supports faac_mexico_pgr_firearms_simulators_334k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 334156.47; date_signed 2016-09-23.",
    investment_type="equipment_supply",
)

# === Cycle 1364 ===
row_doc(
    "seobra_peru_tarapoto_warehouse_sar_facility_1084k_2012",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Peru Tarapoto disaster relief warehouse and SAR training facility",
    "Peru",
    "12 Sep 2012: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for disaster relief warehouse and search and rescue training facility Tarapoto, Peru; obligated USD 1083508.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1083508.00", "2012-09-12", "2012", "", "",
    "DISASTER RELIEF WAREHOUSE AND SEARCH AND RESCUE TRAINING FACILITY TARAPOTO, PERU, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_peru_tarapoto_warehouse_sar_facility_1084k_2012",
    "DISASTER RELIEF WAREHOUSE AND SEARCH AND RESCUE TRAINING FACILITY TARAPOTO, PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127809D0081_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1364",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0008_9700_W9127809D0081_9700 (seobra_peru_tarapoto_warehouse_sar_facility_1084k_2012). Signed 2012-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127809D0081_9700/.",
    "USASpending: seobra_peru_tarapoto_warehouse_sar_facility_1084k_2012 USD 1.084m. Supports seobra_peru_tarapoto_warehouse_sar_facility_1084k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1083508.00; date_signed 2012-09-12.",
    investment_type="epc",
)

# === Cycle 1364 ===
row_doc(
    "seobra_honduras_hap_21515_drw_1047k_2013",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Honduras HAP 21515 disaster relief warehouse",
    "Honduras",
    "25 Sep 2013: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for construction HAP 21515 DRW; obligated USD 1046880.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1046880.00", "2013-09-25", "2013", "", "",
    "CONSTRUCTION HAP 21515 DRW, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_honduras_hap_21515_drw_1047k_2013",
    "CONSTRUCTION HAP 21515 DRW  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127813D0023_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1364",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127813D0023_9700 (seobra_honduras_hap_21515_drw_1047k_2013). Signed 2013-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127813D0023_9700/.",
    "USASpending: seobra_honduras_hap_21515_drw_1047k_2013 USD 1.047m. Supports seobra_honduras_hap_21515_drw_1047k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1046880.00; date_signed 2013-09-25.",
    investment_type="epc",
)

# === Cycle 1364 ===
row_doc(
    "seobra_colombia_pasto_eoc_859k_2019",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Colombia Pasto HAP 37828 EOC design-build",
    "Colombia",
    "28 Sep 2019: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for D/B HAP# 37828 EOC Pasto, Colombia; obligated USD 858919.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "858919.00", "2019-09-28", "2019", "", "",
    "D/B HAP# 37828 EOC - PASTO, COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_colombia_pasto_eoc_859k_2019",
    "D/B HAP# 37828 EOC - PASTO, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0558_9700_W9127817D0097_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1364",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0558_9700_W9127817D0097_9700 (seobra_colombia_pasto_eoc_859k_2019). Signed 2019-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0558_9700_W9127817D0097_9700/.",
    "USASpending: seobra_colombia_pasto_eoc_859k_2019 USD 0.859m. Supports seobra_colombia_pasto_eoc_859k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 858919.00; date_signed 2019-09-28.",
    investment_type="epc",
)

# === Cycle 1365 ===
row_doc(
    "virtra_mexico_guanajuato_firearms_simulators_319k_2017",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico Guanajuato portable and fixed firearms training simulators",
    "Mexico",
    "23 Mar 2017: Department of State awards contract to VIRTRA, INC. for portable firearms training simulator system for Guanajuato State Police Academy and fixed firearms training; obligated USD 319492.53. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "319492.53", "2017-03-23", "2017", "", "",
    "INL MEXICO - PORTABLE FIREARMS TRAINING SIMULATOR SYSTEM FOR THE GUANAJUATO STATE POLICE A, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_guanajuato_firearms_simulators_319k_2017",
    "INL MEXICO - PORTABLE FIREARMS TRAINING SIMULATOR SYSTEM FOR THE GUANAJUATO STATE POLICE ACADEMY AND FIXED FIREARMS TRAINING SIMULATOR. INCLUDES INSTALLATION AND 3-YEAR IN-COUNTRY WARRANTY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0003_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1365",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC17F0003_1900_SWHARC16D0003_1900 (virtra_mexico_guanajuato_firearms_simulators_319k_2017). Signed 2017-03-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0003_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_guanajuato_firearms_simulators_319k_2017 USD 0.319m. Supports virtra_mexico_guanajuato_firearms_simulators_319k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 319492.53; date_signed 2017-03-23.",
    investment_type="equipment_supply",
)

# === Cycle 1365 ===
row_doc(
    "tsymmetry_colombia_gis_drug_interdiction_equipment_306k_2022",
    "infrastructure", "engineering_epc", "us",
    "Tsymmetry — Colombia GIS drug interdiction software and equipment",
    "Colombia",
    "14 Mar 2022: Department of State awards contract to TSYMMETRY INC for software and equipment purchase for drug interdiction efforts in Colombia for the GIS; obligated USD 306036.69. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "306036.69", "2022-03-14", "2022", "", "",
    "THIS TASK ORDER IS FOR SOFTWARE AND EQUIPMENT PURCHASE FOR DRUG INTERDICTION EFFORTS IN CO, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tsymmetry_colombia_gis_drug_interdiction_equipment_306k_2022",
    "THIS TASK ORDER IS FOR SOFTWARE AND EQUIPMENT PURCHASE FOR DRUG INTERDICTION EFFORTS IN COLOMBIA FOR THE GIS CONTRACT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1218_1900_SAQMMA15D0080_1900/",
    "Actor: TSYMMETRY INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1365",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F1218_1900_SAQMMA15D0080_1900 (tsymmetry_colombia_gis_drug_interdiction_equipment_306k_2022). Signed 2022-03-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1218_1900_SAQMMA15D0080_1900/.",
    "USASpending: tsymmetry_colombia_gis_drug_interdiction_equipment_306k_2022 USD 0.306m. Supports tsymmetry_colombia_gis_drug_interdiction_equipment_306k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 306036.69; date_signed 2022-03-14.",
    investment_type="equipment_supply",
)

# === Cycle 1365 ===
row_doc(
    "seobra_peru_piura_eoc_concepcion_warehouse_854k_2012",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Peru Piura EOC and Concepcion disaster relief warehouse",
    "Peru",
    "27 Jul 2012: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for emergency operations center Piura, Peru and disaster relief warehouse Concepcion, Peru; obligated USD 853500.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "853500.00", "2012-07-27", "2012", "", "",
    "EMERGENCY OPERATIONS CENTER PIURA, PERU&DISASTER RELIEF WAREHOUSE CONCEPCION, PERU., Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_peru_piura_eoc_concepcion_warehouse_854k_2012",
    "EMERGENCY OPERATIONS CENTER PIURA, PERU&DISASTER RELIEF WAREHOUSE CONCEPCION, PERU.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127809D0081_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1365",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0006_9700_W9127809D0081_9700 (seobra_peru_piura_eoc_concepcion_warehouse_854k_2012). Signed 2012-07-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127809D0081_9700/.",
    "USASpending: seobra_peru_piura_eoc_concepcion_warehouse_854k_2012 USD 0.854m. Supports seobra_peru_piura_eoc_concepcion_warehouse_854k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 853500.00; date_signed 2012-07-27.",
    investment_type="epc",
)

# === Cycle 1365 ===
row_doc(
    "seobra_colombia_hap_42210_school_843k_2022",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Colombia HAP 42210 school",
    "Colombia",
    "28 Sep 2022: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for HAP #42210 base bid school; obligated USD 842965.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "842965.00", "2022-09-28", "2022", "", "",
    "HAP #42210, BASE BID, SCHOOL, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_colombia_hap_42210_school_843k_2022",
    "HAP #42210, BASE BID, SCHOOL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0437_9700_W9127817D0097_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1365",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0437_9700_W9127817D0097_9700 (seobra_colombia_hap_42210_school_843k_2022). Signed 2022-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0437_9700_W9127817D0097_9700/.",
    "USASpending: seobra_colombia_hap_42210_school_843k_2022 USD 0.843m. Supports seobra_colombia_hap_42210_school_843k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 842965.00; date_signed 2022-09-28.",
    investment_type="epc",
)

# === Cycle 1365 ===
row_doc(
    "seobra_colombia_hangar_upgrade_737k_2010",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Colombia hangar upgrade design-build",
    "Colombia",
    "13 Jul 2010: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for D/B upgrade hangar Colombia; obligated USD 736675.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "736675.00", "2010-07-13", "2010", "", "",
    "D/B UPGRADE HANGAR COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_colombia_hangar_upgrade_737k_2010",
    "D/B UPGRADE HANGAR COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127809D0081_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1365",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127809D0081_9700 (seobra_colombia_hangar_upgrade_737k_2010). Signed 2010-07-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127809D0081_9700/.",
    "USASpending: seobra_colombia_hangar_upgrade_737k_2010 USD 0.737m. Supports seobra_colombia_hangar_upgrade_737k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 736675.00; date_signed 2010-07-13.",
    investment_type="epc",
)

# === Cycle 1366 ===
row_doc(
    "virtra_mexico_durango_tamaulipas_simulators_286k_2016",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico Durango and Tamaulipas firearms training simulators",
    "Mexico",
    "20 May 2016: Department of State awards contract to VIRTRA, INC. for firearm training simulators for Durango and Tamaulipas state academies; obligated USD 286010.04. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "286010.04", "2016-05-20", "2016", "", "",
    "FIREARM TRAINING SIMULATORS FOR DURANGO AND TAMAULIPAS STATE ACADEMIES: 1 PORTABLE AND 1 F, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_durango_tamaulipas_simulators_286k_2016",
    "FIREARM TRAINING SIMULATORS FOR DURANGO AND TAMAULIPAS STATE ACADEMIES: 1 PORTABLE AND 1 FIXED FIREARMS TRAINING SIMULATOR SYSTEMS. INCLUDES INSTALLATION AND 3-YEAR IN-COUNTRY WARRANTY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0011_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1366",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16F0011_1900_SWHARC16D0003_1900 (virtra_mexico_durango_tamaulipas_simulators_286k_2016). Signed 2016-05-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0011_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_durango_tamaulipas_simulators_286k_2016 USD 0.286m. Supports virtra_mexico_durango_tamaulipas_simulators_286k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 286010.04; date_signed 2016-05-20.",
    investment_type="equipment_supply",
)

# === Cycle 1366 ===
row_doc(
    "virtra_mexico_training_simulators_280k_2018",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico training simulators",
    "Mexico",
    "20 Mar 2018: Department of State awards contract to VIRTRA, INC. for training simulators for Mexico; obligated USD 280018.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "280018.00", "2018-03-20", "2018", "", "",
    "REQUIREMENT FOR TRAINING SIMULATORS FOR MEXICO., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_training_simulators_280k_2018",
    "REQUIREMENT FOR TRAINING SIMULATORS FOR MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1056_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1366",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F1056_1900_SWHARC16D0003_1900 (virtra_mexico_training_simulators_280k_2018). Signed 2018-03-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1056_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_training_simulators_280k_2018 USD 0.280m. Supports virtra_mexico_training_simulators_280k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 280018.00; date_signed 2018-03-20.",
    investment_type="equipment_supply",
)

# === Cycle 1366 ===
row_doc(
    "vinpar_colombia_facatativa_warehouse_731k_2019",
    "infrastructure", "building_materials", "other",
    "Construcciones Vinpar — Colombia Facatativa warehouse",
    "Colombia",
    "11 Sep 2019: Department of State awards contract to CONSTRUCCIONES VINPAR S.A.S. for Facatativa warehouse; obligated USD 731427.85. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "731427.85", "2019-09-11", "2019", "", "",
    "FACATATIVA WAREHOUSE, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_vinpar_colombia_facatativa_warehouse_731k_2019",
    "FACATATIVA WAREHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0127_1900_-NONE-_-NONE-/",
    "Actor: CONSTRUCCIONES VINPAR S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1366",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0127_1900_-NONE-_-NONE- (vinpar_colombia_facatativa_warehouse_731k_2019). Signed 2019-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0127_1900_-NONE-_-NONE-/.",
    "USASpending: vinpar_colombia_facatativa_warehouse_731k_2019 USD 0.731m. Supports vinpar_colombia_facatativa_warehouse_731k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 731427.85; date_signed 2019-09-11.",
    investment_type="epc",
)

# === Cycle 1366 ===
row_doc(
    "qa_colombia_hap_37842_base_bid_699k_2022",
    "infrastructure", "building_materials", "other",
    "QA Construction Services — Colombia HAP 37842 base bid",
    "Colombia",
    "29 Sep 2022: Department of Defense awards contract to QA CONSTRUCTION SERVICES S.A.S. for HAP 37842 base bid; obligated USD 698645.89. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "698645.89", "2022-09-29", "2022", "", "",
    "HAP 37842 - BASE BID, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_qa_colombia_hap_37842_base_bid_699k_2022",
    "HAP 37842 - BASE BID",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0471_9700_W9127821D0081_9700/",
    "Actor: QA CONSTRUCTION SERVICES S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1366",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0471_9700_W9127821D0081_9700 (qa_colombia_hap_37842_base_bid_699k_2022). Signed 2022-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0471_9700_W9127821D0081_9700/.",
    "USASpending: qa_colombia_hap_37842_base_bid_699k_2022 USD 0.699m. Supports qa_colombia_hap_37842_base_bid_699k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 698645.89; date_signed 2022-09-29.",
    investment_type="epc",
)

# === Cycle 1366 ===
row_doc(
    "seobra_colombia_tumaco_police_station_588k_2012",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Colombia Tumaco police station",
    "Colombia",
    "12 Jun 2012: Department of State awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for construction project for police station at Tumaco, Colombia; obligated USD 587645.78. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "587645.78", "2012-06-12", "2012", "", "",
    "CONSTRUCTION PROJECT FOR POLICE STATION AT TUMACO, COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_colombia_tumaco_police_station_588k_2012",
    "CONSTRUCTION PROJECT FOR POLICE STATION AT TUMACO, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC12C0003_1900_-NONE-_-NONE-/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1366",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC12C0003_1900_-NONE-_-NONE- (seobra_colombia_tumaco_police_station_588k_2012). Signed 2012-06-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC12C0003_1900_-NONE-_-NONE-/.",
    "USASpending: seobra_colombia_tumaco_police_station_588k_2012 USD 0.588m. Supports seobra_colombia_tumaco_police_station_588k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 587645.78; date_signed 2012-06-12.",
    investment_type="epc",
)

# === Cycle 1367 ===
row_doc(
    "terrestris_peru_hap_eoc_warehouse_equipment_254k_2024",
    "infrastructure", "engineering_epc", "us",
    "Terrestris — Peru HAP disaster relief EOC and warehouse equipment and supplies",
    "Peru",
    "12 Mar 2024: Department of Defense awards contract to TERRESTRIS, LLC for equipment and supplies for humanitarian assistance for a disaster relief emergency operations center and warehouse; obligated USD 254416.04. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "254416.04", "2024-03-12", "2024", "", "",
    "EQUIPMENT AND SUPPLIES FOR HUMANITARIAN ASSISTANCE FOR A DISASTER RELIEF EMERGENCY OPERATI, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_terrestris_peru_hap_eoc_warehouse_equipment_254k_2024",
    "EQUIPMENT AND SUPPLIES FOR HUMANITARIAN ASSISTANCE FOR A DISASTER RELIEF EMERGENCY OPERATIONS CENTER AND WAREHOUSE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL24F0014_9700_W912CL23D0109_9700/",
    "Actor: TERRESTRIS, LLC (U.S.) — us. Official USASpending Award API. Shuffle balsa dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1367",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL24F0014_9700_W912CL23D0109_9700 (terrestris_peru_hap_eoc_warehouse_equipment_254k_2024). Signed 2024-03-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL24F0014_9700_W912CL23D0109_9700/.",
    "USASpending: terrestris_peru_hap_eoc_warehouse_equipment_254k_2024 USD 0.254m. Supports terrestris_peru_hap_eoc_warehouse_equipment_254k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 254416.04; date_signed 2024-03-12.",
    investment_type="equipment_supply",
)

# === Cycle 1367 ===
row_doc(
    "virtra_peru_lima_virtual_range_simulator_251k_2021",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Peru Lima virtual range simulator system",
    "Peru",
    "13 Apr 2021: Department of State awards contract to VIRTRA, INC. for virtual range simulator system for Lima; obligated USD 251331.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "251331.00", "2021-04-13", "2021", "", "",
    "VIRTUAL RANGE SIMULATOR SYSTEM FOR LIMA., Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_peru_lima_virtual_range_simulator_251k_2021",
    "VIRTUAL RANGE SIMULATOR SYSTEM FOR LIMA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F1475_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle water dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1367",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21F1475_1900_SWHARC16D0003_1900 (virtra_peru_lima_virtual_range_simulator_251k_2021). Signed 2021-04-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F1475_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_peru_lima_virtual_range_simulator_251k_2021 USD 0.251m. Supports virtra_peru_lima_virtual_range_simulator_251k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 251331.00; date_signed 2021-04-13.",
    investment_type="equipment_supply",
)

# === Cycle 1367 ===
row_doc(
    "seobra_colombia_tumaco_defensive_walls_towers_559k_2018",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Colombia Tumaco defensive walls and towers",
    "Colombia",
    "24 Sep 2018: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for defensive walls and towers Tumaco Colombia; obligated USD 559381.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "559381.00", "2018-09-24", "2018", "", "",
    "DEFENSIVE WALLS&TOWERS TUMACO COLOMBIA - TASK ORDER, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_colombia_tumaco_defensive_walls_towers_559k_2018",
    "DEFENSIVE WALLS&TOWERS TUMACO COLOMBIA - TASK ORDER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0644_9700_W9127817D0097_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1367",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0644_9700_W9127817D0097_9700 (seobra_colombia_tumaco_defensive_walls_towers_559k_2018). Signed 2018-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0644_9700_W9127817D0097_9700/.",
    "USASpending: seobra_colombia_tumaco_defensive_walls_towers_559k_2018 USD 0.559m. Supports seobra_colombia_tumaco_defensive_walls_towers_559k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 559381.00; date_signed 2018-09-24.",
    investment_type="epc",
)

# === Cycle 1367 ===
row_doc(
    "seobra_uruguay_hap_community_center_555k_2010",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Uruguay HAP community center design-build",
    "Uruguay",
    "19 Jul 2010: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for design build HAP community center; obligated USD 555372.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "555372.00", "2010-07-19", "2010", "", "",
    "DESIGN BUILD HAP COMMUNITY CENTER, Uruguay (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_uruguay_hap_community_center_555k_2010",
    "DESIGN BUILD HAP COMMUNITY CENTER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127809D0081_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1367",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127809D0081_9700 (seobra_uruguay_hap_community_center_555k_2010). Signed 2010-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127809D0081_9700/.",
    "USASpending: seobra_uruguay_hap_community_center_555k_2010 USD 0.555m. Supports seobra_uruguay_hap_community_center_555k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 555372.00; date_signed 2010-07-19.",
    investment_type="epc",
)

# === Cycle 1367 ===
row_doc(
    "seobra_colombia_classrooms_1_4_549k_2017",
    "infrastructure", "building_materials", "other",
    "Servicios y Obras SEOBRA — Colombia classrooms 1-4 base bid",
    "Colombia",
    "25 Sep 2017: Department of Defense awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for base bid classrooms 1-4; obligated USD 548817.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "548817.00", "2017-09-25", "2017", "", "",
    "BASE BID, CLASSROOMS 1-4, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_colombia_classrooms_1_4_549k_2017",
    "IGF::OT::IGF BASE BID, CLASSROOMS 1-4",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0332_9700_W9127813D0009_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1367",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0332_9700_W9127813D0009_9700 (seobra_colombia_classrooms_1_4_549k_2017). Signed 2017-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0332_9700_W9127813D0009_9700/.",
    "USASpending: seobra_colombia_classrooms_1_4_549k_2017 USD 0.549m. Supports seobra_colombia_classrooms_1_4_549k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 548817.00; date_signed 2017-09-25.",
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
