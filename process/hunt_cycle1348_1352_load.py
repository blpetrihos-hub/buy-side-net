#!/usr/bin/env python3
"""Cycles 1348–1352: USASpending LatAm CapEx (Muscogee/Obera/Tsymmetry/FAAC/Edge/Virtra/Human Tech/Airborne + Estudios/Proyectos/Marago/MFG EPC).

Seeds: 20262348–20262352. Thin top-up dry (nickel/balsa/fission_smr/niobium/graphite).
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

# === Cycle 1348 ===
row_doc(
    "muscogee_mexico_setec_oral_trials_courtrooms_15412k_2014",
    "infrastructure", "building_materials", "us",
    "Muscogee International — Mexico SETEC oral trials courtrooms reporting infrastructure",
    "Mexico",
    "29 Sep 2014: Department of State awards contract to MUSCOGEE INTERNATIONAL LLC for SETEC oral trials courtrooms reporting infrastructure project in Mexico City; obligated USD 15411608.01. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "15411608.01", "2014-09-29", "2014", "", "",
    "INL MEXICO CITY - SETEC ORAL TRIALS COURTROOMS REPORTING INFRASTRUCTURE PROJECT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_muscogee_mexico_setec_oral_trials_courtrooms_15412k_2014",
    "IGF::OT::IGF  INL MEXICO CITY - SETEC ORAL TRIALS COURTROOMS REPORTING INFRASTRUCTURE PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC14C0004_1900_-NONE-_-NONE-/",
    "Actor: MUSCOGEE INTERNATIONAL LLC (U.S.) — us. Official USASpending Award API. Shuffle niobium dry→building_materials CapEx; ≥1/3 U.S.",
    "hunt_cycle1348",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC14C0004_1900_-NONE-_-NONE- (muscogee_mexico_setec_oral_trials_courtrooms_15412k_2014). Signed 2014-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC14C0004_1900_-NONE-_-NONE-/.",
    "USASpending: muscogee_mexico_setec_oral_trials_courtrooms_15412k_2014 USD 15.412m. Supports muscogee_mexico_setec_oral_trials_courtrooms_15412k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15411608.01; date_signed 2014-09-29.",
    investment_type="equipment_supply",
)

# === Cycle 1348 ===
row_doc(
    "obera_jamaica_tmpi_equipment_3452k_2024",
    "infrastructure", "engineering_epc", "us",
    "Obera — Jamaica SOUTHCOM TMPI equipment procurement",
    "Jamaica",
    "11 Sep 2024: Department of Defense awards contract to OBERA LLC for FY23 Tranche 10 SOUTHCOM Jamaica Theatre Maintenance Partnership Initiative equipment procurement; obligated USD 3451652.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3451652.00", "2024-09-11", "2024", "", "",
    "FISCAL YEAR 23 TRANCHE 10 U.S. SOUTHERN COMMAND (SOUTHCOM) JAMAICA THEATRE MAINTENANCE PAR, Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_obera_jamaica_tmpi_equipment_3452k_2024",
    "FISCAL YEAR 23 TRANCHE 10 U.S. SOUTHERN COMMAND (SOUTHCOM) JAMAICA THEATRE MAINTENANCE PARTNERSHIP INITIATIVE (TMPI) EQUIPMENT PROCUREMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489024F0125_9700_FA489023D0008_9700/",
    "Actor: OBERA LLC (U.S.) — us. Official USASpending Award API. Shuffle rail dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1348",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489024F0125_9700_FA489023D0008_9700 (obera_jamaica_tmpi_equipment_3452k_2024). Signed 2024-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489024F0125_9700_FA489023D0008_9700/.",
    "USASpending: obera_jamaica_tmpi_equipment_3452k_2024 USD 3.452m. Supports obera_jamaica_tmpi_equipment_3452k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3451652.00; date_signed 2024-09-11.",
    investment_type="equipment_supply",
)

# === Cycle 1348 ===
row_doc(
    "estudios_colombia_construction_incidental_design_451k_2011",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Colombia construction with incidental design",
    "Colombia",
    "17 Jun 2011: Department of Defense awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for construction with incidental design; obligated USD 451393.99. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "451393.99", "2011-06-17", "2011", "", "",
    "CONSTRUCTION WITH INCIDENTAL DESIGN, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_construction_incidental_design_451k_2011",
    "TAS::21 2020::TAS CONSTRUCTION WITH INCIDENTAL DESIGN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127809D0077_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1348",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0004_9700_W9127809D0077_9700 (estudios_colombia_construction_incidental_design_451k_2011). Signed 2011-06-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127809D0077_9700/.",
    "USASpending: estudios_colombia_construction_incidental_design_451k_2011 USD 0.451m. Supports estudios_colombia_construction_incidental_design_451k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 451393.99; date_signed 2011-06-17.",
    investment_type="epc",
)

# === Cycle 1348 ===
row_doc(
    "estudios_colombia_sofa_parking_container_storage_426k_2016",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Colombia SOFA parking and container storage",
    "Colombia",
    "29 Sep 2016: Department of Defense awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for SOFA agreement parking and container storage; obligated USD 426499.25. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "426499.25", "2016-09-29", "2016", "", "",
    "SOFA AGREEMENT PARKING&CONTAINER STORAGE, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_sofa_parking_container_storage_426k_2016",
    "IGF::OT::IGF SOFA AGREEMENT PARKING&CONTAINER STORAGE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127813D0010_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1348",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127813D0010_9700 (estudios_colombia_sofa_parking_container_storage_426k_2016). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127813D0010_9700/.",
    "USASpending: estudios_colombia_sofa_parking_container_storage_426k_2016 USD 0.426m. Supports estudios_colombia_sofa_parking_container_storage_426k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 426499.25; date_signed 2016-09-29.",
    investment_type="epc",
)

# === Cycle 1348 ===
row_doc(
    "proyectos_panama_medical_clinic_hap_355k_2011",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Panama HAP medical clinic",
    "Panama",
    "06 Jun 2011: Department of Defense awards contract to PROYECTOS CIVILES S Y M LIMITADA to construct medical clinic in support of Humanitarian Assistance Program, SOUTHCOM; obligated USD 354545.89. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "354545.89", "2011-06-06", "2011", "", "",
    "CONSTRUCT MEDICAL CLINIC IN SUPPORT OF HUMANITARIAN ASSISTANCE PROGRAM, UNITED STATES SOUT, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_panama_medical_clinic_hap_355k_2011",
    "CONSTRUCT MEDICAL CLINIC IN SUPPORT OF HUMANITARIAN ASSISTANCE PROGRAM, UNITED STATES SOUTHERN COMMAND.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0021_9700_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1348",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL11C0021_9700_-NONE-_-NONE- (proyectos_panama_medical_clinic_hap_355k_2011). Signed 2011-06-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0021_9700_-NONE-_-NONE-/.",
    "USASpending: proyectos_panama_medical_clinic_hap_355k_2011 USD 0.355m. Supports proyectos_panama_medical_clinic_hap_355k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 354545.89; date_signed 2011-06-06.",
    investment_type="epc",
)

# === Cycle 1349 ===
row_doc(
    "tsymmetry_colombia_cop_equipment_phase_vi_2700k_2021",
    "infrastructure", "engineering_epc", "us",
    "Tsymmetry — Colombia COP equipment order Phase VI",
    "Colombia",
    "09 Mar 2021: Department of State awards contract to TSYMMETRY INC for COP equipment order Phase VI for Colombia; obligated USD 2699782.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2699782.00", "2021-03-09", "2021", "", "",
    "COP EQUIPMENT ORDER PHASE VI - FOR COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tsymmetry_colombia_cop_equipment_phase_vi_2700k_2021",
    "COP EQUIPMENT ORDER PHASE VI - FOR COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F0965_1900_SAQMMA15D0080_1900/",
    "Actor: TSYMMETRY INC (U.S.) — us. Official USASpending Award API. Shuffle balsa dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1349",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21F0965_1900_SAQMMA15D0080_1900 (tsymmetry_colombia_cop_equipment_phase_vi_2700k_2021). Signed 2021-03-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F0965_1900_SAQMMA15D0080_1900/.",
    "USASpending: tsymmetry_colombia_cop_equipment_phase_vi_2700k_2021 USD 2.700m. Supports tsymmetry_colombia_cop_equipment_phase_vi_2700k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2699782.00; date_signed 2021-03-09.",
    investment_type="equipment_supply",
)

# === Cycle 1349 ===
row_doc(
    "faac_mexico_le_training_simulators_2410k_2019",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico law enforcement training simulators",
    "Mexico",
    "13 Mar 2019: Department of State awards contract to FAAC INCORPORATED for law enforcement training simulators; obligated USD 2410314.44. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2410314.44", "2019-03-13", "2019", "", "",
    "REQUIREMENT FOR LAW ENFORCEMENT TRAINING SIMULATORS, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_le_training_simulators_2410k_2019",
    "REQUIREMENT FOR LAW ENFORCEMENT TRAINING SIMULATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1081_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle nickel dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1349",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19F1081_1900_SWHARC16D0002_1900 (faac_mexico_le_training_simulators_2410k_2019). Signed 2019-03-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1081_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_le_training_simulators_2410k_2019 USD 2.410m. Supports faac_mexico_le_training_simulators_2410k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2410314.44; date_signed 2019-03-13.",
    investment_type="equipment_supply",
)

# === Cycle 1349 ===
row_doc(
    "proyectos_colombia_containers_336k_2018",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia containers",
    "Colombia",
    "14 Aug 2018: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for containers; obligated USD 336126.80. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "336126.80", "2018-08-14", "2018", "", "",
    "CONTAINERS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_containers_336k_2018",
    "CONTAINERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01518C0004_1900_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1349",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01518C0004_1900_-NONE-_-NONE- (proyectos_colombia_containers_336k_2018). Signed 2018-08-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01518C0004_1900_-NONE-_-NONE-/.",
    "USASpending: proyectos_colombia_containers_336k_2018 USD 0.336m. Supports proyectos_colombia_containers_336k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 336126.80; date_signed 2018-08-14.",
    investment_type="epc",
)

# === Cycle 1349 ===
row_doc(
    "estudios_colombia_tulua_warehouse_304k_2020",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Colombia Tulua warehouse",
    "Colombia",
    "06 Feb 2020: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for warehouse at Tulua City, Colombia; obligated USD 304108.23. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "304108.23", "2020-02-06", "2020", "", "",
    "WAREHOUSE AT TULUA CITY, COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_tulua_warehouse_304k_2020",
    "WAREHOUSE AT TULUA CITY, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0031_1900_-NONE-_-NONE-/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1349",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20C0031_1900_-NONE-_-NONE- (estudios_colombia_tulua_warehouse_304k_2020). Signed 2020-02-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0031_1900_-NONE-_-NONE-/.",
    "USASpending: estudios_colombia_tulua_warehouse_304k_2020 USD 0.304m. Supports estudios_colombia_tulua_warehouse_304k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 304108.23; date_signed 2020-02-06.",
    investment_type="epc",
)

# === Cycle 1349 ===
row_doc(
    "marago_colombia_tower_construction_292k_2017",
    "infrastructure", "engineering_epc", "other",
    "Constructora Marago — Colombia tower construction",
    "Colombia",
    "01 Jun 2017: Department of State awards contract to CONSTRUCTORA MARAGO S A S for tower construction Colombia; obligated USD 292418.46. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "292418.46", "2017-06-01", "2017", "", "",
    "TOWER CONSTRUCTION COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_marago_colombia_tower_construction_292k_2017",
    "TOWER CONSTRUCTION COLOMBIAIGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0181_1900_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA MARAGO S A S — other. Official USASpending Award API. Shuffle engineering_epc CapEx.",
    "hunt_cycle1349",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0181_1900_-NONE-_-NONE- (marago_colombia_tower_construction_292k_2017). Signed 2017-06-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0181_1900_-NONE-_-NONE-/.",
    "USASpending: marago_colombia_tower_construction_292k_2017 USD 0.292m. Supports marago_colombia_tower_construction_292k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 292418.46; date_signed 2017-06-01.",
    investment_type="epc",
)

# === Cycle 1350 ===
row_doc(
    "faac_mexico_driving_simulators_2258k_2017",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico 12 driving simulator systems with installation",
    "Mexico",
    "26 Sep 2017: Department of State awards contract to FAAC INCORPORATED for 12 driving simulator systems including accessories, training, installation, and in-country maintenance; obligated USD 2257697.51. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2257697.51", "2017-09-26", "2017", "", "",
    "INL MEXICO -  12 DRIVING SIMULATOR SYSTEMS (INCLUDING ACCESSORIES, TRAINING, INSTALLATION,, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_driving_simulators_2258k_2017",
    "INL MEXICO -  12 DRIVING SIMULATOR SYSTEMS (INCLUDING ACCESSORIES, TRAINING, INSTALLATION, AND IN-COUNTRY MAINTENANCE AND SUPPORT).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0030_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle niobium dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1350",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC17F0030_1900_SWHARC16D0002_1900 (faac_mexico_driving_simulators_2258k_2017). Signed 2017-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0030_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_driving_simulators_2258k_2017 USD 2.258m. Supports faac_mexico_driving_simulators_2258k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2257697.51; date_signed 2017-09-26.",
    investment_type="equipment_supply",
)

# === Cycle 1350 ===
row_doc(
    "edge_colombia_motorola_radio_telecom_2170k_2024",
    "infrastructure", "engineering_epc", "us",
    "Edge Technology — Colombia Motorola radio and telecommunications equipment",
    "Colombia",
    "28 Sep 2024: Department of State awards contract to EDGE TECHNOLOGY DISTRIBUTORS, INC. for Motorola radio and telecommunications equipment; obligated USD 2169959.99. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2169959.99", "2024-09-28", "2024", "", "",
    "MOTOROLA RADIO AND TELECOMMUNICATIONS EQUIPMENT, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_edge_colombia_motorola_radio_telecom_2170k_2024",
    "MOTOROLA RADIO AND TELECOMMUNICATIONS EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24P0136_1900_-NONE-_-NONE-/",
    "Actor: EDGE TECHNOLOGY DISTRIBUTORS, INC. (U.S.) — us. Official USASpending Award API. Shuffle graphite dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1350",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24P0136_1900_-NONE-_-NONE- (edge_colombia_motorola_radio_telecom_2170k_2024). Signed 2024-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24P0136_1900_-NONE-_-NONE-/.",
    "USASpending: edge_colombia_motorola_radio_telecom_2170k_2024 USD 2.170m. Supports edge_colombia_motorola_radio_telecom_2170k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2169959.99; date_signed 2024-09-28.",
    investment_type="equipment_supply",
)

# === Cycle 1350 ===
row_doc(
    "mfg_colombia_slab_shack_271k_2012",
    "infrastructure", "building_materials", "other",
    "MFG Ingenieria — Colombia slab and shack construction",
    "Colombia",
    "14 Sep 2012: Department of Defense awards contract to MFG INGENIERIA SAS to construct a slab and shack; obligated USD 270621.32. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "270621.32", "2012-09-14", "2012", "", "",
    "CONSTRUCT A SLAB AND SHACK, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mfg_colombia_slab_shack_271k_2012",
    "CONSTRUCT A SLAB AND SHACK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0020_9700_-NONE-_-NONE-/",
    "Actor: MFG INGENIERIA SAS — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1350",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12C0020_9700_-NONE-_-NONE- (mfg_colombia_slab_shack_271k_2012). Signed 2012-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0020_9700_-NONE-_-NONE-/.",
    "USASpending: mfg_colombia_slab_shack_271k_2012 USD 0.271m. Supports mfg_colombia_slab_shack_271k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 270621.32; date_signed 2012-09-14.",
    investment_type="epc",
)

# === Cycle 1350 ===
row_doc(
    "proyectos_colombia_inl_bogota_construction_247k_2020",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia INL Bogota construction",
    "Colombia",
    "22 Jan 2020: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for INL Bogota construction; obligated USD 246871.99. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "246871.99", "2020-01-22", "2020", "", "",
    "INL BOGOTA-CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_inl_bogota_construction_247k_2020",
    "INL BOGOTA-CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520C0002_1900_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1350",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01520C0002_1900_-NONE-_-NONE- (proyectos_colombia_inl_bogota_construction_247k_2020). Signed 2020-01-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520C0002_1900_-NONE-_-NONE-/.",
    "USASpending: proyectos_colombia_inl_bogota_construction_247k_2020 USD 0.247m. Supports proyectos_colombia_inl_bogota_construction_247k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 246871.99; date_signed 2020-01-22.",
    investment_type="epc",
)

# === Cycle 1350 ===
row_doc(
    "marago_colombia_caucasia_communications_tower_243k_2023",
    "infrastructure", "engineering_epc", "other",
    "Constructora Marago — Colombia Caucasia communications tower",
    "Colombia",
    "21 Jun 2023: Department of State awards contract to CONSTRUCTORA MARAGO S A S for Caucasia communications tower; obligated USD 243123.80. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "243123.80", "2023-06-21", "2023", "", "",
    "CAUCASIA COMMUNICATIONS TOWER, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_marago_colombia_caucasia_communications_tower_243k_2023",
    "CAUCASIA COMMUNICATIONS TOWER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0936_1900_19AQMM21D0036_1900/",
    "Actor: CONSTRUCTORA MARAGO S A S — other. Official USASpending Award API. Shuffle engineering_epc CapEx.",
    "hunt_cycle1350",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F0936_1900_19AQMM21D0036_1900 (marago_colombia_caucasia_communications_tower_243k_2023). Signed 2023-06-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0936_1900_19AQMM21D0036_1900/.",
    "USASpending: marago_colombia_caucasia_communications_tower_243k_2023 USD 0.243m. Supports marago_colombia_caucasia_communications_tower_243k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 243123.80; date_signed 2023-06-21.",
    investment_type="epc",
)

# === Cycle 1351 ===
row_doc(
    "virtra_mexico_le_training_simulators_1922k_2019",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico law enforcement training simulators",
    "Mexico",
    "14 Mar 2019: Department of State awards contract to VIRTRA, INC. for law enforcement training simulators; obligated USD 1922287.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1922287.00", "2019-03-14", "2019", "", "",
    "REQUIREMENT FOR LAW ENFORCEMENT TRAINING SIMULATORS, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_le_training_simulators_1922k_2019",
    "REQUIREMENT FOR LAW ENFORCEMENT TRAINING SIMULATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1077_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle water dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1351",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19F1077_1900_SWHARC16D0003_1900 (virtra_mexico_le_training_simulators_1922k_2019). Signed 2019-03-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1077_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_le_training_simulators_1922k_2019 USD 1.922m. Supports virtra_mexico_le_training_simulators_1922k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1922287.00; date_signed 2019-03-14.",
    investment_type="equipment_supply",
)

# === Cycle 1351 ===
row_doc(
    "human_tech_haiti_rigid_shelters_1876k_2025",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Haiti INL rigid shelters",
    "Haiti",
    "12 Dec 2025: Department of State awards contract to HUMAN TECHNOLOGIES CORP for INL Haiti rigid shelters; obligated USD 1875906.16. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1875906.16", "2025-12-12", "2025", "", "",
    "INL HAITI RIGID SHELTERS, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_haiti_rigid_shelters_1876k_2025",
    "INL HAITI RIGID SHELTERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE26F0001_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle bridges_roads dry→building_materials CapEx; ≥1/3 U.S. Asset country Haiti per description.",
    "hunt_cycle1351",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE26F0001_1900_19AQMM21D0007_1900 (human_tech_haiti_rigid_shelters_1876k_2025). Signed 2025-12-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE26F0001_1900_19AQMM21D0007_1900/.",
    "USASpending: human_tech_haiti_rigid_shelters_1876k_2025 USD 1.876m. Supports human_tech_haiti_rigid_shelters_1876k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1875906.16; date_signed 2025-12-12.",
    investment_type="epc",
)

# === Cycle 1351 ===
row_doc(
    "proyectos_colombia_ammo_bunkers_224k_2012",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia ammo bunkers construction",
    "Colombia",
    "10 Aug 2012: Department of Defense awards contract to PROYECTOS CIVILES S Y M LIMITADA for construction ammo bunkers; obligated USD 224163.69. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "224163.69", "2012-08-10", "2012", "", "",
    "CONSTRUCTION AMMO BUNKERS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_ammo_bunkers_224k_2012",
    "CONSTRUCTION AMMO BUNKERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0015_9700_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1351",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12C0015_9700_-NONE-_-NONE- (proyectos_colombia_ammo_bunkers_224k_2012). Signed 2012-08-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0015_9700_-NONE-_-NONE-/.",
    "USASpending: proyectos_colombia_ammo_bunkers_224k_2012 USD 0.224m. Supports proyectos_colombia_ammo_bunkers_224k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 224163.69; date_signed 2012-08-10.",
    investment_type="epc",
)

# === Cycle 1351 ===
row_doc(
    "proyectos_colombia_construction_199k_2010",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia construction",
    "Colombia",
    "27 Sep 2010: Department of Defense awards contract to PROYECTOS CIVILES S Y M LIMITADA for construction; obligated USD 198568.22. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "198568.22", "2010-09-27", "2010", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_construction_199k_2010",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10C0040_9700_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1351",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT10C0040_9700_-NONE-_-NONE- (proyectos_colombia_construction_199k_2010). Signed 2010-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10C0040_9700_-NONE-_-NONE-/.",
    "USASpending: proyectos_colombia_construction_199k_2010 USD 0.199m. Supports proyectos_colombia_construction_199k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 198568.22; date_signed 2010-09-27.",
    investment_type="epc",
)

# === Cycle 1351 ===
row_doc(
    "mfg_colombia_construct_school_139k_2012",
    "infrastructure", "building_materials", "other",
    "MFG Ingenieria — Colombia school construction",
    "Colombia",
    "14 Sep 2012: Department of Defense awards contract to MFG INGENIERIA SAS to construct school; obligated USD 138606.36. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "138606.36", "2012-09-14", "2012", "", "",
    "CONSTRUCT SCHOOL, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mfg_colombia_construct_school_139k_2012",
    "CONSTRUCT SCHOOL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0347_9700_-NONE-_-NONE-/",
    "Actor: MFG INGENIERIA SAS — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1351",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12P0347_9700_-NONE-_-NONE- (mfg_colombia_construct_school_139k_2012). Signed 2012-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0347_9700_-NONE-_-NONE-/.",
    "USASpending: mfg_colombia_construct_school_139k_2012 USD 0.139m. Supports mfg_colombia_construct_school_139k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 138606.36; date_signed 2012-09-14.",
    investment_type="epc",
)

# === Cycle 1352 ===
row_doc(
    "airborne_colombia_system_installation_1331k_2016",
    "infrastructure", "engineering_epc", "us",
    "Airborne Data Systems — Colombia system installation and support",
    "Colombia",
    "25 Apr 2016: Department of State awards contract to AIRBORNE DATA SYSTEMS INC for system, installation and support; obligated USD 1331255.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1331255.00", "2016-04-25", "2016", "", "",
    "AWARD FOR SYSTEM, INSTALLATION AND SUPPORT., Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_airborne_colombia_system_installation_1331k_2016",
    "AWARD FOR SYSTEM, INSTALLATION AND SUPPORT. IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SINLEC16C0014_1900_-NONE-_-NONE-/",
    "Actor: AIRBORNE DATA SYSTEMS INC (U.S.) — us. Official USASpending Award API. Shuffle graphite dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1352",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SINLEC16C0014_1900_-NONE-_-NONE- (airborne_colombia_system_installation_1331k_2016). Signed 2016-04-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SINLEC16C0014_1900_-NONE-_-NONE-/.",
    "USASpending: airborne_colombia_system_installation_1331k_2016 USD 1.331m. Supports airborne_colombia_system_installation_1331k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1331255.00; date_signed 2016-04-25.",
    investment_type="equipment_supply",
)

# === Cycle 1352 ===
row_doc(
    "tsymmetry_colombia_cnp_servers_install_1278k_2017",
    "infrastructure", "engineering_epc", "us",
    "Tsymmetry — Colombia CNP servers supply installation and configuration",
    "Colombia",
    "30 Sep 2017: Department of State awards contract to TSYMMETRY INC for supply, installation, and configuration of servers and software for the Colombian National Police; obligated USD 1278302.30. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1278302.30", "2017-09-30", "2017", "", "",
    "SUPPLY, INSTALLATION, AND CONFIGURATION OF SERVERS AND SOFTWARE FOR THE COLOMBIAN NATIONAL, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tsymmetry_colombia_cnp_servers_install_1278k_2017",
    "SUPPLY, INSTALLATION, AND CONFIGURATION OF SERVERS AND SOFTWARE FOR THE COLOMBIAN NATIONAL POLICE ACCORDING TO THE DESCRIPTION AND TECHNICAL SPECIFICATIONS HEREBY DETAILED.  WARRANTY, MAINTENANCE, AND TECHNICAL SUPPORT S",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F4799_1900_SAQMMA15D0080_1900/",
    "Actor: TSYMMETRY INC (U.S.) — us. Official USASpending Award API. Shuffle nickel dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1352",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17F4799_1900_SAQMMA15D0080_1900 (tsymmetry_colombia_cnp_servers_install_1278k_2017). Signed 2017-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F4799_1900_SAQMMA15D0080_1900/.",
    "USASpending: tsymmetry_colombia_cnp_servers_install_1278k_2017 USD 1.278m. Supports tsymmetry_colombia_cnp_servers_install_1278k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1278302.30; date_signed 2017-09-30.",
    investment_type="equipment_supply",
)

# === Cycle 1352 ===
row_doc(
    "proyectos_colombia_bogota_inl_construction_131k_2018",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia Bogota INL construction",
    "Colombia",
    "29 Oct 2018: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for Bogota INL construction; obligated USD 131368.29. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "131368.29", "2018-10-29", "2018", "", "",
    "BOGOTA INL CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_bogota_inl_construction_131k_2018",
    "BOGOTA INL CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01519C0001_1900_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1352",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01519C0001_1900_-NONE-_-NONE- (proyectos_colombia_bogota_inl_construction_131k_2018). Signed 2018-10-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01519C0001_1900_-NONE-_-NONE-/.",
    "USASpending: proyectos_colombia_bogota_inl_construction_131k_2018 USD 0.131m. Supports proyectos_colombia_bogota_inl_construction_131k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 131368.29; date_signed 2018-10-29.",
    investment_type="epc",
)

# === Cycle 1352 ===
row_doc(
    "mfg_colombia_bogota_ups_equipment_97k_2020",
    "infrastructure", "engineering_epc", "other",
    "MFG Ingenieria — Colombia Bogota INL UPS equipment",
    "Colombia",
    "05 Jun 2020: Department of State awards contract to MFG INGENIERIA SAS for Bogota INL UPS equipment; obligated USD 96830.24. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "96830.24", "2020-06-05", "2020", "", "",
    "BOGOTA INL. UPS EQUIPMENT, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mfg_colombia_bogota_ups_equipment_97k_2020",
    "BOGOTA INL. UPS EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520P0222_1900_-NONE-_-NONE-/",
    "Actor: MFG INGENIERIA SAS — other. Official USASpending Award API. Shuffle engineering_epc CapEx.",
    "hunt_cycle1352",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01520P0222_1900_-NONE-_-NONE- (mfg_colombia_bogota_ups_equipment_97k_2020). Signed 2020-06-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520P0222_1900_-NONE-_-NONE-/.",
    "USASpending: mfg_colombia_bogota_ups_equipment_97k_2020 USD 0.097m. Supports mfg_colombia_bogota_ups_equipment_97k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 96830.24; date_signed 2020-06-05.",
    investment_type="equipment_supply",
)

# === Cycle 1352 ===
row_doc(
    "estudios_colombia_caucasia_utilities_control_room_40k_2018",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Colombia Caucasia CNP utilities control room",
    "Colombia",
    "04 Sep 2018: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for Caucasia CNP utilities control room construction; obligated USD 39957.22. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "39957.22", "2018-09-04", "2018", "", "",
    "CAUCASIA CNP UTILITIES CONTROL ROOM CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_caucasia_utilities_control_room_40k_2018",
    "CAUCASIA CNP UTILITIES CONTROL ROOM CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P1831_1900_-NONE-_-NONE-/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1352",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18P1831_1900_-NONE-_-NONE- (estudios_colombia_caucasia_utilities_control_room_40k_2018). Signed 2018-09-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P1831_1900_-NONE-_-NONE-/.",
    "USASpending: estudios_colombia_caucasia_utilities_control_room_40k_2018 USD 0.040m. Supports estudios_colombia_caucasia_utilities_control_room_40k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 39957.22; date_signed 2018-09-04.",
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
