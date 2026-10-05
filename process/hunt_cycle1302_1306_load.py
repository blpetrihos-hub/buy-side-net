#!/usr/bin/env python3
"""Cycles 1302–1306: USASpending LatAm CapEx (Alutiiq/AIMCON/DFS/Lakeshore + LatAm EPC).

Seeds: 20262302–20262306. Thin top-up dry.
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

# === Cycle 1302 ===
row_doc(
    "alutiiq_mexico_fiu_database_infra_10466k_2016",
    "infrastructure", "building_materials", "us",
    "Alutiiq Technical Services — Mexico FIU capability infrastructure expansion",
    "Mexico",
    "7 Apr 2016: Department of State awards contract to ALUTIIQ TECHNICAL SERVICES LLC for Financial Intelligence Unit capability infrastructure expansion of databases (Government of Mexico); obligated USD 10466025.93. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "10466025.93", "2016-04-07", "2016", "", "",
    "FINANCIAL INTELLIGENCE UNIT OF THE SECRETARIAT OF FINANCE AND PUBLIC CREDIT REQUEST FOR CAPABILITY INFRASTRUCTURE EXPANS, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_fiu_database_infra_10466k_2016",
    "FINANCIAL INTELLIGENCE UNIT OF THE SECRETARIAT OF FINANCE AND PUBLIC CREDIT REQUEST FOR CAPABILITY INFRASTRUCTURE EXPANSION OF DATABASES. GOVERNMENT OF MEXICO IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16C0004_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ TECHNICAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1302",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16C0004_1900_-NONE-_-NONE- (alutiiq_mexico_fiu_database_infra_10466k_2016). Signed 2016-04-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16C0004_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_fiu_database_infra_10466k_2016 USD 10.466m. Supports alutiiq_mexico_fiu_database_infra_10466k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10466025.93; date_signed 2016-04-07.",
    investment_type="equipment_supply",
)

# === Cycle 1302 ===
row_doc(
    "alutiiq_mexico_questioned_docs_lab_2483k_2018",
    "infrastructure", "building_materials", "us",
    "Alutiiq Information Management — Mexico questioned-documents lab equipment installation",
    "Mexico",
    "3 May 2018: Department of State awards contract to ALUTIIQ INFORMATION MANAGEMENT, LLC for questioned documents equipment, installation, configuration and maintenance for state laboratories in Mexico; obligated USD 2482951.78. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2482951.78", "2018-05-03", "2018", "", "",
    "THIS PURCHASE ORDER IS FOR QUESTIONED DOCUMENTS EQUIPMENT, INSTALLATION, CONFIGURATION AND MAINTENANCE FOR STATE LABORAT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_questioned_docs_lab_2483k_2018",
    "THIS PURCHASE ORDER IS FOR QUESTIONED DOCUMENTS EQUIPMENT, INSTALLATION, CONFIGURATION AND MAINTENANCE FOR STATE LABORATORIES IN MEXICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE18P0045_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ INFORMATION MANAGEMENT, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1302",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE18P0045_1900_-NONE-_-NONE- (alutiiq_mexico_questioned_docs_lab_2483k_2018). Signed 2018-05-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE18P0045_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_questioned_docs_lab_2483k_2018 USD 2.483m. Supports alutiiq_mexico_questioned_docs_lab_2483k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2482951.78; date_signed 2018-05-03.",
    investment_type="equipment_supply",
)

# === Cycle 1302 ===
row_doc(
    "flores_serrano_ecuador_design_build_1386k_2025",
    "infrastructure", "building_materials", "other",
    "Flores Serrano — Ecuador design/build services",
    "Ecuador",
    "29 Sep 2025: Department of State awards contract to FLORES SERRANO GUILLERMO SEBASTIAN for design/build services; obligated USD 1385590.44. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1385590.44", "2025-09-29", "2025", "", "",
    "DESIGN/BUILD SERVICES, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_flores_serrano_ecuador_design_build_1386k_2025",
    "DESIGN/BUILD SERVICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025C0141_1900_-NONE-_-NONE-/",
    "Actor: FLORES SERRANO GUILLERMO SEBASTIAN — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1302",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5025C0141_1900_-NONE-_-NONE- (flores_serrano_ecuador_design_build_1386k_2025). Signed 2025-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025C0141_1900_-NONE-_-NONE-/.",
    "USASpending: flores_serrano_ecuador_design_build_1386k_2025 USD 1.386m. Supports flores_serrano_ecuador_design_build_1386k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1385590.44; date_signed 2025-09-29.",
    investment_type="epc",
)

# === Cycle 1302 ===
row_doc(
    "misc_panama_hospital_608k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Panama hospital",
    "Panama",
    "26 Sep 2010: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for hospital (PoP Panama); obligated USD 608007.70. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "608007.70", "2010-09-26", "2010", "", "",
    "HOSPITAL, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_panama_hospital_608k_2010",
    "HOSPITAL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0050_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1302",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0050_9700_-NONE-_-NONE- (misc_panama_hospital_608k_2010). Signed 2010-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0050_9700_-NONE-_-NONE-/.",
    "USASpending: misc_panama_hospital_608k_2010 USD 0.608m. Supports misc_panama_hospital_608k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 608007.7; date_signed 2010-09-26.",
    investment_type="epc",
)

# === Cycle 1302 ===
row_doc(
    "misc_colombia_fuel_storage_facility_587k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia fuel storage facility construction",
    "Colombia",
    "10 Sep 2012: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for fuel storage facility construction; obligated USD 587304.62. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "587304.62", "2012-09-10", "2012", "", "",
    "FUEL STORAGE FACILITY CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_fuel_storage_facility_587k_2012",
    "FUEL STORAGE FACILITY CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0018_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1302",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12C0018_9700_-NONE-_-NONE- (misc_colombia_fuel_storage_facility_587k_2012). Signed 2012-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0018_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_fuel_storage_facility_587k_2012 USD 0.587m. Supports misc_colombia_fuel_storage_facility_587k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 587304.62; date_signed 2012-09-10.",
    investment_type="epc",
)

# === Cycle 1303 ===
row_doc(
    "aimcon_mexico_consular_audio_1985k_2022",
    "infrastructure", "engineering_epc", "us",
    "AIMCON Design Build — Mexico consular audio system replacement",
    "Mexico",
    "29 Sep 2022: Department of State awards contract to AIMCON DESIGN BUILD, LLC for consular audio system replacement project; obligated USD 1985185.18. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1985185.18", "2022-09-29", "2022", "", "",
    "CONSULAR AUDIO SYSTEM REPLACEMENT PROJECT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_aimcon_mexico_consular_audio_1985k_2022",
    "CONSULAR AUDIO SYSTEM REPLACEMENT PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F4480_1900_19AQMM22D0051_1900/",
    "Actor: AIMCON DESIGN BUILD, LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1303",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F4480_1900_19AQMM22D0051_1900 (aimcon_mexico_consular_audio_1985k_2022). Signed 2022-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F4480_1900_19AQMM22D0051_1900/.",
    "USASpending: aimcon_mexico_consular_audio_1985k_2022 USD 1.985m. Supports aimcon_mexico_consular_audio_1985k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1985185.18; date_signed 2022-09-29.",
    investment_type="equipment_supply",
)

# === Cycle 1303 ===
row_doc(
    "alutiiq_ecuador_quito_it_install_893k_2025",
    "infrastructure", "engineering_epc", "us",
    "Alutiiq Career Ventures — Quito IT products delivery and installation",
    "Ecuador",
    "26 Sep 2025: Department of State awards contract to ALUTIIQ CAREER VENTURES LLC for delivery and installation of IT products and software in Quito, Ecuador; obligated USD 892568.86. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "892568.86", "2025-09-26", "2025", "", "",
    "DELIVERY AND INSTALLATION OF IT PRODUCTS AND SOFTWARE IN QUITO, ECUADOR, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_ecuador_quito_it_install_893k_2025",
    "DELIVERY AND INSTALLATION OF IT PRODUCTS AND SOFTWARE IN QUITO, ECUADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025P0149_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ CAREER VENTURES LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1303",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5025P0149_1900_-NONE-_-NONE- (alutiiq_ecuador_quito_it_install_893k_2025). Signed 2025-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025P0149_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_ecuador_quito_it_install_893k_2025 USD 0.893m. Supports alutiiq_ecuador_quito_it_install_893k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 892568.86; date_signed 2025-09-26.",
    investment_type="equipment_supply",
)

# === Cycle 1303 ===
row_doc(
    "tecnologia_honduras_facilities_db_993k_2019",
    "infrastructure", "engineering_epc", "other",
    "Tecnologia de Proyectos — Honduras design/build facilities repair",
    "Honduras",
    "25 Sep 2019: Department of State awards contract to TECNOLOGIA DE PROYECTOS S.R.L. DE C.V. for design, build and repair various facilities; obligated USD 992865.41. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "992865.41", "2019-09-25", "2019", "", "",
    "THE PURPOSE OF THIS TASK ORDER IS TO DESIGN, BUILD AND REPAIR VARIOUS FACILITIES FOR THE OFFICE OF SECURITY COOPERATION , Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tecnologia_honduras_facilities_db_993k_2019",
    "THE PURPOSE OF THIS TASK ORDER IS TO DESIGN, BUILD AND REPAIR VARIOUS FACILITIES FOR THE OFFICE OF SECURITY COOPERATION (OSC), U.S. EMBASSY, TEGUCIGALPA, HONDURAS, TO BE PERFORMED UNDER THE CENTRAL AMERICA MATOC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0527_9700_W9127816D0103_9700/",
    "Actor: TECNOLOGIA DE PROYECTOS S.R.L. DE C.V. — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1303",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0527_9700_W9127816D0103_9700 (tecnologia_honduras_facilities_db_993k_2019). Signed 2019-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0527_9700_W9127816D0103_9700/.",
    "USASpending: tecnologia_honduras_facilities_db_993k_2019 USD 0.993m. Supports tecnologia_honduras_facilities_db_993k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 992865.41; date_signed 2019-09-25.",
    investment_type="epc",
)

# === Cycle 1303 ===
row_doc(
    "mfg_colombia_mariquita_lodging_559k_2020",
    "infrastructure", "engineering_epc", "other",
    "MFG Ingenieria — Colombia Mariquita CNP aviation lodging building",
    "Colombia",
    "22 Jun 2020: Department of State awards contract to MFG INGENIERIA SAS for construction of lodging building at CNP aviation unit in Mariquita, Colombia; obligated USD 559003.37. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "559003.37", "2020-06-22", "2020", "", "",
    "CONSTRUCTION OF LODGING BUILDING AT CNP AVIATION UNIT IN MARIQUITA, COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mfg_colombia_mariquita_lodging_559k_2020",
    "CONSTRUCTION OF LODGING BUILDING AT CNP AVIATION UNIT IN MARIQUITA, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0102_1900_-NONE-_-NONE-/",
    "Actor: MFG INGENIERIA SAS — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1303",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20C0102_1900_-NONE-_-NONE- (mfg_colombia_mariquita_lodging_559k_2020). Signed 2020-06-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0102_1900_-NONE-_-NONE-/.",
    "USASpending: mfg_colombia_mariquita_lodging_559k_2020 USD 0.559m. Supports mfg_colombia_mariquita_lodging_559k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 559003.37; date_signed 2020-06-22.",
    investment_type="epc",
)

# === Cycle 1303 ===
row_doc(
    "misc_haiti_construction_services_483k_2010",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Haiti construction services",
    "Haiti",
    "24 Apr 2010: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for construction services; obligated USD 482954.46. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "482954.46", "2010-04-24", "2010", "", "",
    "CONSTRUCTION SERVICES, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_construction_services_483k_2010",
    "CONSTRUCTION SERVICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0015_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1303",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0015_9700_-NONE-_-NONE- (misc_haiti_construction_services_483k_2010). Signed 2010-04-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0015_9700_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_construction_services_483k_2010 USD 0.483m. Supports misc_haiti_construction_services_483k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 482954.46; date_signed 2010-04-24.",
    investment_type="epc",
)

# === Cycle 1304 ===
row_doc(
    "dfs_ecuador_floating_dock_800k_2026",
    "infrastructure", "building_materials", "us",
    "DFS Construction — Ecuador design/build floating dock",
    "Ecuador",
    "24 Jun 2026: Department of State awards contract to DFS CONSTRUCTION, LLC for design/build floating dock; obligated USD 799533.68. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "799533.68", "2026-06-24", "2026", "", "",
    "DESIGN / BUILD FLOATING DOCK, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_dfs_ecuador_floating_dock_800k_2026",
    "DESIGN / BUILD FLOATING DOCK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0051_1900_-NONE-_-NONE-/",
    "Actor: DFS CONSTRUCTION, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1304",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5026C0051_1900_-NONE-_-NONE- (dfs_ecuador_floating_dock_800k_2026). Signed 2026-06-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0051_1900_-NONE-_-NONE-/.",
    "USASpending: dfs_ecuador_floating_dock_800k_2026 USD 0.800m. Supports dfs_ecuador_floating_dock_800k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 799533.68; date_signed 2026-06-24.",
    investment_type="epc",
)

# === Cycle 1304 ===
row_doc(
    "lakeshore_haiti_housing_design_build_672k_2011",
    "infrastructure", "building_materials", "us",
    "Lakeshore Engineering — Haiti design/build housing units",
    "Haiti",
    "30 Sep 2011: Department of State awards contract to LAKESHORE ENGINEERING SERVICES, INC. for design/build of housing units; obligated USD 671794.26. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "671794.26", "2011-09-30", "2011", "", "",
    "DESIGN/BUILD OF HOUSING UNITS, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_lakeshore_haiti_housing_design_build_672k_2011",
    "DESIGN/BUILD OF HOUSING UNITS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11C0272_1900_-NONE-_-NONE-/",
    "Actor: LAKESHORE ENGINEERING SERVICES, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1304",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11C0272_1900_-NONE-_-NONE- (lakeshore_haiti_housing_design_build_672k_2011). Signed 2011-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11C0272_1900_-NONE-_-NONE-/.",
    "USASpending: lakeshore_haiti_housing_design_build_672k_2011 USD 0.672m. Supports lakeshore_haiti_housing_design_build_672k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 671794.26; date_signed 2011-09-30.",
    investment_type="epc",
)

# === Cycle 1304 ===
row_doc(
    "estudios_ecuador_floating_dock_744k_2026",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Ecuador design/build floating dock",
    "Ecuador",
    "14 Apr 2026: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for design/build floating dock; obligated USD 744325.43. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "744325.43", "2026-04-14", "2026", "", "",
    "DESIGN / BUILD FLOATING DOCK, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_ecuador_floating_dock_744k_2026",
    "DESIGN / BUILD FLOATING DOCK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0031_1900_-NONE-_-NONE-/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1304",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5026C0031_1900_-NONE-_-NONE- (estudios_ecuador_floating_dock_744k_2026). Signed 2026-04-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0031_1900_-NONE-_-NONE-/.",
    "USASpending: estudios_ecuador_floating_dock_744k_2026 USD 0.744m. Supports estudios_ecuador_floating_dock_744k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 744325.43; date_signed 2026-04-14.",
    investment_type="epc",
)

# === Cycle 1304 ===
row_doc(
    "eterna_honduras_marforsouth_ops_677k_2018",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras MarForSouth operations facility design/build",
    "Honduras",
    "19 Sep 2018: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for design/build and construct the MarForSouth operations facility; obligated USD 677472.48. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "677472.48", "2018-09-19", "2018", "", "",
    "THE PURPOSE OF THIS TASK ORDER IS TO DESIGN/BUILD AND CONSTRUCT THE MARFORSOUTH OPERATIONS FACILITY AT SOTO CANO AIR BAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_marforsouth_ops_677k_2018",
    "THE PURPOSE OF THIS TASK ORDER IS TO DESIGN/BUILD AND CONSTRUCT THE MARFORSOUTH OPERATIONS FACILITY AT SOTO CANO AIR BASE, HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0585_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1304",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0585_9700_W9127816D0102_9700 (eterna_honduras_marforsouth_ops_677k_2018). Signed 2018-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0585_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_marforsouth_ops_677k_2018 USD 0.677m. Supports eterna_honduras_marforsouth_ops_677k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 677472.48; date_signed 2018-09-19.",
    investment_type="epc",
)

# === Cycle 1304 ===
row_doc(
    "seobra_colombia_scan_eagle_db_536k_2018",
    "infrastructure", "building_materials", "other",
    "Seobra — Colombia Scan Eagle ops design/build repair",
    "Colombia",
    "26 Sep 2018: Department of State awards contract to SERVICIOS Y OBRAS SEOBRA S.A.S. for design build repair Scan Eagle operations; obligated USD 535949.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "535949.00", "2018-09-26", "2018", "", "",
    "THE PURPOSE OF THIS TASK ORDER IS FOR THE DESIGN BUILD REPAIR SCAN EAGLE OPERATIONS CENTER, LA MACARENA, COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_seobra_colombia_scan_eagle_db_536k_2018",
    "THE PURPOSE OF THIS TASK ORDER IS FOR THE DESIGN BUILD REPAIR SCAN EAGLE OPERATIONS CENTER, LA MACARENA, COLOMBIA.  THIS TASK ORDER WILL BE PERFORMED UNDER THE SOUTH AMERICA MATOC, CONTRACT W91278-17-D-0097.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0704_9700_W9127817D0097_9700/",
    "Actor: SERVICIOS Y OBRAS SEOBRA S.A.S. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1304",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0704_9700_W9127817D0097_9700 (seobra_colombia_scan_eagle_db_536k_2018). Signed 2018-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0704_9700_W9127817D0097_9700/.",
    "USASpending: seobra_colombia_scan_eagle_db_536k_2018 USD 0.536m. Supports seobra_colombia_scan_eagle_db_536k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 535949.0; date_signed 2018-09-26.",
    investment_type="epc",
)

# === Cycle 1305 ===
row_doc(
    "williams_scotsman_haiti_modular_564k_2014",
    "infrastructure", "building_materials", "us",
    "Williams Scotsman — Haiti modular buildings purchase and delivery",
    "Haiti",
    "23 Jul 2014: Department of State awards contract to WILLIAMS SCOTSMAN INC for purchase and deliver 40 Williams Scotsman modular buildings; obligated USD 563959.40. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "563959.40", "2014-07-23", "2014", "", "",
    "PURCHASE&DELIVER 40 \"WILLIAMS SCOTSMAN\" MODULAR BUILDINGS TOTAL: $501,980 + 1% SURCHAGE FUNDING SOURCE: USE 'CN' APPROPR, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_williams_scotsman_haiti_modular_564k_2014",
    "PURCHASE&DELIVER 40 \"WILLIAMS SCOTSMAN\" MODULAR BUILDINGS TOTAL: $501,980 + 1% SURCHAGE FUNDING SOURCE: USE 'CN' APPROPRIATION CONTRACTING OFFICE : AQM CONTRACT ORDER : TIM FARRELL POST CONTACT: MS SAARLAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0121_1900_-NONE-_-NONE-/",
    "Actor: WILLIAMS SCOTSMAN INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1305",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14C0121_1900_-NONE-_-NONE- (williams_scotsman_haiti_modular_564k_2014). Signed 2014-07-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0121_1900_-NONE-_-NONE-/.",
    "USASpending: williams_scotsman_haiti_modular_564k_2014 USD 0.564m. Supports williams_scotsman_haiti_modular_564k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 563959.4; date_signed 2014-07-23.",
    investment_type="equipment_supply",
)

# === Cycle 1305 ===
row_doc(
    "powerbilt_colombia_prefab_hangar_doors_376k_2017",
    "infrastructure", "building_materials", "us",
    "Powerbilt Steel Buildings — Colombia prefabricated hangar steel doors",
    "Colombia",
    "19 Jul 2017: Department of State awards contract to POWERBILT STEEL BUILDINGS, INC. for acquisition of two prefabricated ready-to-assemble steel doors for hangar; obligated USD 376178.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "376178.00", "2017-07-19", "2017", "", "",
    "IGF::OT::IGF ACQUITISION OF TWO PREFABRICATED - READY TO ENSEMBLE STEEL DOORS FOR HANGAR AND WAREHOUSE BUILDINGS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_powerbilt_colombia_prefab_hangar_doors_376k_2017",
    "IGF::OT::IGF ACQUITISION OF TWO PREFABRICATED - READY TO ENSEMBLE STEEL DOORS FOR HANGAR AND WAREHOUSE BUILDINGS.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SINLEC17M0079_1900_-NONE-_-NONE-/",
    "Actor: POWERBILT STEEL BUILDINGS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1305",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SINLEC17M0079_1900_-NONE-_-NONE- (powerbilt_colombia_prefab_hangar_doors_376k_2017). Signed 2017-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SINLEC17M0079_1900_-NONE-_-NONE-/.",
    "USASpending: powerbilt_colombia_prefab_hangar_doors_376k_2017 USD 0.376m. Supports powerbilt_colombia_prefab_hangar_doors_376k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 376178.0; date_signed 2017-07-19.",
    investment_type="equipment_supply",
)

# === Cycle 1305 ===
row_doc(
    "tecnologia_honduras_transient_db_532k_2019",
    "infrastructure", "building_materials", "other",
    "Tecnologia de Proyectos — Honduras consolidated transient design/build",
    "Honduras",
    "30 Sep 2019: Department of State awards contract to TECNOLOGIA DE PROYECTOS S.R.L. DE C.V. for design/build consolidated transient facility; obligated USD 531808.10. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "531808.10", "2019-09-30", "2019", "", "",
    "THE PURPOSE OF THIS TASK ORDER IS TO DESIGN/ BUILD CONSOLIDATED TRANSIENT AND AGE FACILITY, SOTO CANO AIR BASE, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tecnologia_honduras_transient_db_532k_2019",
    "THE PURPOSE OF THIS TASK ORDER IS TO DESIGN/ BUILD CONSOLIDATED TRANSIENT AND AGE FACILITY, SOTO CANO AIR BASE, HONDURAS, TO BE PERFORMED UNDER THE CENTRAL AMERICA MATOC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0635_9700_W9127816D0103_9700/",
    "Actor: TECNOLOGIA DE PROYECTOS S.R.L. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1305",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0635_9700_W9127816D0103_9700 (tecnologia_honduras_transient_db_532k_2019). Signed 2019-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0635_9700_W9127816D0103_9700/.",
    "USASpending: tecnologia_honduras_transient_db_532k_2019 USD 0.532m. Supports tecnologia_honduras_transient_db_532k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 531808.1; date_signed 2019-09-30.",
    investment_type="epc",
)

# === Cycle 1305 ===
row_doc(
    "mfg_colombia_jurado_radar_tower_485k_2018",
    "infrastructure", "building_materials", "other",
    "MFG Ingenieria — Colombia Jurado COLNAV metallic radar tower",
    "Colombia",
    "5 Apr 2018: Department of State awards contract to MFG INGENIERIA SAS for construct one metallic radar tower at the Colombian Navy in Jurado; obligated USD 484546.46. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "484546.46", "2018-04-05", "2018", "", "",
    "CONSTRUCT ONE (1) METALLIC RADAR TOWER AT THE COLOMBIAN NAVY (COLNAV) IN JURADO, CHOCO, COLOMBIA IGF::OT::IGF, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mfg_colombia_jurado_radar_tower_485k_2018",
    "CONSTRUCT ONE (1) METALLIC RADAR TOWER AT THE COLOMBIAN NAVY (COLNAV) IN JURADO, CHOCO, COLOMBIA IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0053_1900_-NONE-_-NONE-/",
    "Actor: MFG INGENIERIA SAS — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1305",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0053_1900_-NONE-_-NONE- (mfg_colombia_jurado_radar_tower_485k_2018). Signed 2018-04-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0053_1900_-NONE-_-NONE-/.",
    "USASpending: mfg_colombia_jurado_radar_tower_485k_2018 USD 0.485m. Supports mfg_colombia_jurado_radar_tower_485k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 484546.46; date_signed 2018-04-05.",
    investment_type="epc",
)

# === Cycle 1305 ===
row_doc(
    "misc_colombia_construction_447k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia construction",
    "Colombia",
    "2 Sep 2011: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for construction (PoP Colombia); obligated USD 447204.95. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "447204.95", "2011-09-02", "2011", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_construction_447k_2011",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0022_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1305",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11C0022_9700_-NONE-_-NONE- (misc_colombia_construction_447k_2011). Signed 2011-09-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0022_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_construction_447k_2011 USD 0.447m. Supports misc_colombia_construction_447k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 447204.95; date_signed 2011-09-02.",
    investment_type="epc",
)

# === Cycle 1306 ===
row_doc(
    "alutiiq_mexico_canine_kennels_371k_2021",
    "infrastructure", "engineering_epc", "us",
    "Alutiiq Essential Services — Mexico prefabricated canine kennels",
    "Mexico",
    "23 Aug 2021: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for acquisition and installation of prefabricated canine kennels; obligated USD 371282.30. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "371282.30", "2021-08-23", "2021", "", "",
    "THIS TASK ORDER IS FOR THE ACQUISITION AND INSTALLATION OF PREFABRICATED CANINE KENNELS FOR MEXICAN CANINE UNITS, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_canine_kennels_371k_2021",
    "THIS TASK ORDER IS FOR THE ACQUISITION AND INSTALLATION OF PREFABRICATED CANINE KENNELS FOR MEXICAN CANINE UNITS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3221_1900_19AQMM20D0072_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1306",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21F3221_1900_19AQMM20D0072_1900 (alutiiq_mexico_canine_kennels_371k_2021). Signed 2021-08-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3221_1900_19AQMM20D0072_1900/.",
    "USASpending: alutiiq_mexico_canine_kennels_371k_2021 USD 0.371m. Supports alutiiq_mexico_canine_kennels_371k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 371282.3; date_signed 2021-08-23.",
    investment_type="equipment_supply",
)

# === Cycle 1306 ===
row_doc(
    "isobox_panama_chu_298k_2025",
    "infrastructure", "engineering_epc", "us",
    "IsoBOX — Panama containerized housing unit (CHU)",
    "Panama",
    "27 Sep 2025: Department of State awards contract to ISOBOX INC for Panama CHU (containerized housing unit); obligated USD 297960.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "297960.00", "2025-09-27", "2025", "", "",
    "PANAMA CHU, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_isobox_panama_chu_298k_2025",
    "PANAMA CHU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125PE005_9700_-NONE-_-NONE-/",
    "Actor: ISOBOX INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1306",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_H9228125PE005_9700_-NONE-_-NONE- (isobox_panama_chu_298k_2025). Signed 2025-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125PE005_9700_-NONE-_-NONE-/.",
    "USASpending: isobox_panama_chu_298k_2025 USD 0.298m. Supports isobox_panama_chu_298k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 297960.0; date_signed 2025-09-27.",
    investment_type="equipment_supply",
)

# === Cycle 1306 ===
row_doc(
    "almeida_franca_brazil_cmr_storage_384k_2025",
    "infrastructure", "engineering_epc", "other",
    "Almeida Franca Engenharia — Brazil CMR storage and ACC design/build",
    "Brazil",
    "12 Sep 2025: Department of State awards contract to ALMEIDA FRANCA ENGENHARIA LTDA for BRA CMR storage and ACC (design/build); obligated USD 384104.27. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "384104.27", "2025-09-12", "2025", "", "",
    "BRA - CMR STORAGE AND ACC (DESIGN/BUILD), Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_almeida_franca_brazil_cmr_storage_384k_2025",
    "BRA - CMR STORAGE AND ACC (DESIGN/BUILD)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025C0115_1900_-NONE-_-NONE-/",
    "Actor: ALMEIDA FRANCA ENGENHARIA LTDA — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1306",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5025C0115_1900_-NONE-_-NONE- (almeida_franca_brazil_cmr_storage_384k_2025). Signed 2025-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5025C0115_1900_-NONE-_-NONE-/.",
    "USASpending: almeida_franca_brazil_cmr_storage_384k_2025 USD 0.384m. Supports almeida_franca_brazil_cmr_storage_384k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 384104.27; date_signed 2025-09-12.",
    investment_type="epc",
)

# === Cycle 1306 ===
row_doc(
    "misc_dr_foundation_site_prep_360k_2016",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Dominican Republic foundation and site prep",
    "Dominican Republic",
    "25 Jan 2016: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for foundation and site prep for vocational school and hospital clinics; obligated USD 359754.94. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "359754.94", "2016-01-25", "2016", "", "",
    "IGF::OT::IGF FOUNDATION&SITE PREP FOR VOCATIONAL SCHOOL AND HOSPITAL CLINICS, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dr_foundation_site_prep_360k_2016",
    "IGF::OT::IGF FOUNDATION&SITE PREP FOR VOCATIONAL SCHOOL AND HOSPITAL CLINICS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470416C2001_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1306",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA470416C2001_9700_-NONE-_-NONE- (misc_dr_foundation_site_prep_360k_2016). Signed 2016-01-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470416C2001_9700_-NONE-_-NONE-/.",
    "USASpending: misc_dr_foundation_site_prep_360k_2016 USD 0.360m. Supports misc_dr_foundation_site_prep_360k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 359754.94; date_signed 2016-01-25.",
    investment_type="epc",
)

# === Cycle 1306 ===
row_doc(
    "misc_colombia_vehicle_maint_building_346k_2013",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Colombia vehicle maintenance building",
    "Colombia",
    "18 Sep 2013: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for construct a vehicle maintenance building; obligated USD 346300.60. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "346300.60", "2013-09-18", "2013", "", "",
    "CONSTRUCT A VEHICLE MAINTENANCE BUILDING, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_vehicle_maint_building_346k_2013",
    "CONSTRUCT A VEHICLE MAINTENANCE BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13C0020_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1306",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT13C0020_9700_-NONE-_-NONE- (misc_colombia_vehicle_maint_building_346k_2013). Signed 2013-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13C0020_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_vehicle_maint_building_346k_2013 USD 0.346m. Supports misc_colombia_vehicle_maint_building_346k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 346300.6; date_signed 2013-09-18.",
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
