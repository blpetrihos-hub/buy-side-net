#!/usr/bin/env python3
"""Cycles 1343–1347: USASpending LatAm CapEx (Tseng/Muscogee/Northstar/J&J/Fortis/Afognak/Edge/Astrophysics + Estudios/Eterna/Marago/Proyectos/Misc EPC).

Seeds: 20262343–20262347. Thin top-up dry.
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

# === Cycle 1343 ===
row_doc(
    "tseng_haiti_faculty_medicine_pharmacy_21716k_2014",
    "infrastructure", "building_materials", "us",
    "Tseng Consulting Group — Haiti Faculty of Medicine and Pharmacy design-build",
    "Haiti",
    "25 Jun 2014: Department of State awards contract to TSENG CONSULTING GROUP, INC. for design and build of Faculty of Medicine and Pharmacy; obligated USD 21715874.69. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "21715874.69", "2014-06-25", "2014", "", "",
    "DESIGN AND BUILD CONTRACT TO BUILD THE FACULTY OF MEDICINE AND PHARMACY, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tseng_haiti_faculty_medicine_pharmacy_21716k_2014",
    "IGF::OT::IGF - THE PURPOSE OF THIS REQUISITION IS TO CREATE A DESIGN AND BUILD CONTRACT TO BUILD THE FACULTY OF MEDICINE AND PHARMACY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1400004_7200_-NONE-_-NONE-/",
    "Actor: TSENG CONSULTING GROUP, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1343",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521C1400004_7200_-NONE-_-NONE- (tseng_haiti_faculty_medicine_pharmacy_21716k_2014). Signed 2014-06-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1400004_7200_-NONE-_-NONE-/.",
    "USASpending: tseng_haiti_faculty_medicine_pharmacy_21716k_2014 USD 21.716m. Supports tseng_haiti_faculty_medicine_pharmacy_21716k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 21715874.69; date_signed 2014-06-25.",
    investment_type="epc",
)

# === Cycle 1343 ===
row_doc(
    "muscogee_mexico_oral_trials_courtroom_infra_21361k_2016",
    "infrastructure", "building_materials", "us",
    "Muscogee International — Mexico oral trials courtroom reporting infrastructure",
    "Mexico",
    "27 Sep 2016: Department of State awards contract to MUSCOGEE INTERNATIONAL LLC for hardware, software, and installation for oral trials courtroom reporting infrastructure project in Mexico; obligated USD 21361185.60. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "21361185.60", "2016-09-27", "2016", "", "",
    "ORAL TRIALS COURTROOM REPORTING INFRASTRUCTURE PROJECT IN MEXICO, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_muscogee_mexico_oral_trials_courtroom_infra_21361k_2016",
    "HARDWARE, SOFTWARE, AND INSTALLATION SERVICES FOR AN ORAL TRIALS COURTROOM REPORTING INFRASTRUCTURE PROJECT IN MEXICO, REQUIREMENTS CONSIDERED AS OTHER FUNCTIONS.  REFERENCE CLASSIFICATION CODE: IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16C0009_1900_-NONE-_-NONE-/",
    "Actor: MUSCOGEE INTERNATIONAL LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1343",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16C0009_1900_-NONE-_-NONE- (muscogee_mexico_oral_trials_courtroom_infra_21361k_2016). Signed 2016-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16C0009_1900_-NONE-_-NONE-/.",
    "USASpending: muscogee_mexico_oral_trials_courtroom_infra_21361k_2016 USD 21.361m. Supports muscogee_mexico_oral_trials_courtroom_infra_21361k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 21361185.6; date_signed 2016-09-27.",
    investment_type="equipment_supply",
)

# === Cycle 1343 ===
row_doc(
    "estudios_argentina_el_chaco_eoc_warehouse_1010k_2010",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Argentina El Chaco EOC and warehouse",
    "Argentina",
    "10 Sep 2010: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for D/B EOC and warehouse for El Chaco; obligated USD 1010076.79. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1010076.79", "2010-09-10", "2010", "", "",
    "D/B EOC AND WAREHOUSE FOR EL CHACO, ARGENTINA, Argentina (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_argentina_el_chaco_eoc_warehouse_1010k_2010",
    "D/B EOC AND WAWREHOUSE FOR EL CHACO, ARGENTINA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127809D0077_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1343",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127809D0077_9700 (estudios_argentina_el_chaco_eoc_warehouse_1010k_2010). Signed 2010-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127809D0077_9700/.",
    "USASpending: estudios_argentina_el_chaco_eoc_warehouse_1010k_2010 USD 1.010m. Supports estudios_argentina_el_chaco_eoc_warehouse_1010k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1010076.79; date_signed 2010-09-10.",
    investment_type="epc",
)

# === Cycle 1343 ===
row_doc(
    "estudios_guyana_eoc_977k_2012",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Guyana EOC design-build",
    "Guyana",
    "21 Sep 2012: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for D/B EOC Guyana; obligated USD 976685.55. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "976685.55", "2012-09-21", "2012", "", "",
    "D/B EOC GUYANA, Guyana (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_guyana_eoc_977k_2012",
    "D/B EOC GUYANA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127809D0077_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1343",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0011_9700_W9127809D0077_9700 (estudios_guyana_eoc_977k_2012). Signed 2012-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127809D0077_9700/.",
    "USASpending: estudios_guyana_eoc_977k_2012 USD 0.977m. Supports estudios_guyana_eoc_977k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 976685.55; date_signed 2012-09-21.",
    investment_type="epc",
)

# === Cycle 1343 ===
row_doc(
    "eterna_honduras_officers_quadruplex_10c_679k_2010",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras Soto Cano officers quadruplex FY-10C",
    "Honduras",
    "29 Sep 2010: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for design/build of officer's quadruplex housing units FY-10C Soto Cano; obligated USD 679199.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "679199.00", "2010-09-29", "2010", "", "",
    "DESIGN/BUILD OF OFFICER'S QUADRUPLEX HOUSING UNITS FY-10C SOTO CANO AIR BASE, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_officers_quadruplex_10c_679k_2010",
    "DESIGN/BUILD OF OFFICER'S QUADRUPLEX HOUSING UNITS FY-10C SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0019_9700_W9127809D0071_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1343",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0019_9700_W9127809D0071_9700 (eterna_honduras_officers_quadruplex_10c_679k_2010). Signed 2010-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0019_9700_W9127809D0071_9700/.",
    "USASpending: eterna_honduras_officers_quadruplex_10c_679k_2010 USD 0.679m. Supports eterna_honduras_officers_quadruplex_10c_679k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 679199.0; date_signed 2010-09-29.",
    investment_type="epc",
)

# === Cycle 1344 ===
row_doc(
    "northstar_argentina_radiation_portal_monitors_14400k_2011",
    "infrastructure", "engineering_epc", "us",
    "Northstar Federal Services — Argentina radiation portal monitors installation",
    "Argentina",
    "3 Jun 2011: Department of State awards contract to NORTHSTAR FEDERAL SERVICES, INC. for radiation portal monitors installation; obligated USD 14400307.11. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "14400307.11", "2011-06-03", "2011", "", "",
    "RADIATION PORTAL MONITORS INSTALLATION, Argentina (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_northstar_argentina_radiation_portal_monitors_14400k_2011",
    "SERVICES, RADIATION PORTAL MONITORS INSTALLATION FOR OFFICE OF INTERNATIONAL MATERIAL PROTECTION&COOP - NA-25.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_DEDT0002722_8900_DEAM5208NA28443_8900/",
    "Actor: NORTHSTAR FEDERAL SERVICES, INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1344",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_DEDT0002722_8900_DEAM5208NA28443_8900 (northstar_argentina_radiation_portal_monitors_14400k_2011). Signed 2011-06-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_DEDT0002722_8900_DEAM5208NA28443_8900/.",
    "USASpending: northstar_argentina_radiation_portal_monitors_14400k_2011 USD 14.400m. Supports northstar_argentina_radiation_portal_monitors_14400k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14400307.11; date_signed 2011-06-03.",
    investment_type="equipment_supply",
)

# === Cycle 1344 ===
row_doc(
    "jj_panama_punta_coco_pier_1792k_2010",
    "infrastructure", "building_materials", "us",
    "J & J Maintenance — Panama Punta Coco pier construction",
    "Panama",
    "30 Sep 2010: Department of State awards contract to J & J MAINTENANCE INC for construction of pier Punta Coco Panama; obligated USD 1791808.42. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1791808.42", "2010-09-30", "2010", "", "",
    "CONSTRUCTION OF PIER, PUNTA COCO, PANAMA, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_jj_panama_punta_coco_pier_1792k_2010",
    "CONSTRUCTION OF PIER, PUNTA COCO, PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0015_9700_W9127809D0068_9700/",
    "Actor: J & J MAINTENANCE INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1344",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0015_9700_W9127809D0068_9700 (jj_panama_punta_coco_pier_1792k_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0015_9700_W9127809D0068_9700/.",
    "USASpending: jj_panama_punta_coco_pier_1792k_2010 USD 1.792m. Supports jj_panama_punta_coco_pier_1792k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1791808.42; date_signed 2010-09-30.",
    investment_type="epc",
)

# === Cycle 1344 ===
row_doc(
    "estudios_argentina_zapala_neuquen_warehouse_eoc_528k_2011",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Argentina Zapala warehouse and Neuquen EOC",
    "Argentina",
    "19 Sep 2011: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for design build warehouse Zapala and warehouse and EOC Neuquen; obligated USD 528353.24. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "528353.24", "2011-09-19", "2011", "", "",
    "DESIGN BUILD WAREHOUSE, ZAPALA, WAREHOUSE AND EOC, NEUQUEN, ARGENTINA, Argentina (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_argentina_zapala_neuquen_warehouse_eoc_528k_2011",
    "TAS::97 0819::TAS DESIGN BUILD WARHOUSE, ZAPALA, WAREHOUSE AND EOC, NEUQUEN, ARGENTINA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127809D0077_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1344",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0005_9700_W9127809D0077_9700 (estudios_argentina_zapala_neuquen_warehouse_eoc_528k_2011). Signed 2011-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127809D0077_9700/.",
    "USASpending: estudios_argentina_zapala_neuquen_warehouse_eoc_528k_2011 USD 0.528m. Supports estudios_argentina_zapala_neuquen_warehouse_eoc_528k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 528353.24; date_signed 2011-09-19.",
    investment_type="epc",
)

# === Cycle 1344 ===
row_doc(
    "proyectos_colombia_guaymoral_warehouse_504k_2017",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia CNP warehouse Guaymoral",
    "Colombia",
    "7 Feb 2017: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for CNP warehouse Guaymoral; obligated USD 504101.29. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "504101.29", "2017-02-07", "2017", "", "",
    "CNP WAREHOUSE, GUAYMORAL, COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_guaymoral_warehouse_504k_2017",
    "CNP WAREHOUSE, GUAYMORAL, COLOMBIA IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0106_1900_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1344",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0106_1900_-NONE-_-NONE- (proyectos_colombia_guaymoral_warehouse_504k_2017). Signed 2017-02-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0106_1900_-NONE-_-NONE-/.",
    "USASpending: proyectos_colombia_guaymoral_warehouse_504k_2017 USD 0.504m. Supports proyectos_colombia_guaymoral_warehouse_504k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 504101.29; date_signed 2017-02-07.",
    investment_type="epc",
)

# === Cycle 1344 ===
row_doc(
    "estudios_peru_cusco_hap_puno_eoc_498k_2011",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Peru Cusco HAP and Puno EOC",
    "Peru",
    "29 Sep 2011: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for D/B HAP #9141 Cusco and HAP #11345 EOC Puno; obligated USD 497563.31. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "497563.31", "2011-09-29", "2011", "", "",
    "D/B HAP # 9141 CUSCO AND HAP #11345 EOC, PUNO PERU, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_peru_cusco_hap_puno_eoc_498k_2011",
    "TAS::97 0819::TAS D/B HAP # 9141 CUSCO AND HAP #11345 EOC, PUNO PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127809D0077_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1344",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0008_9700_W9127809D0077_9700 (estudios_peru_cusco_hap_puno_eoc_498k_2011). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127809D0077_9700/.",
    "USASpending: estudios_peru_cusco_hap_puno_eoc_498k_2011 USD 0.498m. Supports estudios_peru_cusco_hap_puno_eoc_498k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 497563.31; date_signed 2011-09-29.",
    investment_type="epc",
)

# === Cycle 1345 ===
row_doc(
    "jj_panama_punta_coco_ops_barracks_1772k_2010",
    "infrastructure", "building_materials", "us",
    "J & J Maintenance — Panama Punta Coco CN ops center and barracks",
    "Panama",
    "30 Sep 2010: Department of State awards contract to J & J MAINTENANCE INC for construction of CN ops center/barracks Punta Coco; obligated USD 1771872.30. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1771872.30", "2010-09-30", "2010", "", "",
    "CONSTRUCTION OF CN OPS CENTER/BARRACKS, PUNTA COCO, PANAMA, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_jj_panama_punta_coco_ops_barracks_1772k_2010",
    "CONSTRUCTION OF CN OPS CENTER/BARRACKS, PUNTA COCO, PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0016_9700_W9127809D0068_9700/",
    "Actor: J & J MAINTENANCE INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1345",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0016_9700_W9127809D0068_9700 (jj_panama_punta_coco_ops_barracks_1772k_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0016_9700_W9127809D0068_9700/.",
    "USASpending: jj_panama_punta_coco_ops_barracks_1772k_2010 USD 1.772m. Supports jj_panama_punta_coco_ops_barracks_1772k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1771872.3; date_signed 2010-09-30.",
    investment_type="epc",
)

# === Cycle 1345 ===
row_doc(
    "fortis_colombia_cctv_equipment_install_1714k_2014",
    "infrastructure", "building_materials", "us",
    "Fortis Networks — Colombia CCTV equipment design and installation",
    "Colombia",
    "29 Dec 2014: Department of State awards contract to FORTIS NETWORKS, INC. for CCTV equipment, design, and installation; obligated USD 1714071.20. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1714071.20", "2014-12-29", "2014", "", "",
    "CCTV EQUIPMENT, DESIGN, AND INSTALLATION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fortis_colombia_cctv_equipment_install_1714k_2014",
    "IGF::OT::IGF VALUE-ADDED IT RESELLER SERVICES TO PROVIDE CCTV EQUIPMENT, DESIGN, AND INSTALLATION IN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15M0005_1900_-NONE-_-NONE-/",
    "Actor: FORTIS NETWORKS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1345",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC15M0005_1900_-NONE-_-NONE- (fortis_colombia_cctv_equipment_install_1714k_2014). Signed 2014-12-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15M0005_1900_-NONE-_-NONE-/.",
    "USASpending: fortis_colombia_cctv_equipment_install_1714k_2014 USD 1.714m. Supports fortis_colombia_cctv_equipment_install_1714k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1714071.2; date_signed 2014-12-29.",
    investment_type="equipment_supply",
)

# === Cycle 1345 ===
row_doc(
    "marago_colombia_mariquita_training_hangar_616k_2021",
    "infrastructure", "building_materials", "other",
    "Constructora Marago — Colombia Mariquita training hangar",
    "Colombia",
    "24 Sep 2021: Department of State awards contract to CONSTRUCTORA MARAGO S A S for construction of training hangar Mariquita; obligated USD 615874.64. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "615874.64", "2021-09-24", "2021", "", "",
    "CONSTRUCTION OF TRAINING HANGAR MARIQUITA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_marago_colombia_mariquita_training_hangar_616k_2021",
    "CONSTRUCTION OF TRAINING HANGAR MARIQUITA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3868_1900_19AQMM21D0036_1900/",
    "Actor: CONSTRUCTORA MARAGO S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1345",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21F3868_1900_19AQMM21D0036_1900 (marago_colombia_mariquita_training_hangar_616k_2021). Signed 2021-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3868_1900_19AQMM21D0036_1900/.",
    "USASpending: marago_colombia_mariquita_training_hangar_616k_2021 USD 0.616m. Supports marago_colombia_mariquita_training_hangar_616k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 615874.64; date_signed 2021-09-24.",
    investment_type="epc",
)

# === Cycle 1345 ===
row_doc(
    "proyectos_colombia_soledad_modular_lodging_614k_2023",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia Soledad modular lodging buildings",
    "Colombia",
    "28 Jul 2023: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for modular lodging buildings Soledad; obligated USD 614272.21. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "614272.21", "2023-07-28", "2023", "", "",
    "MODULAR LODGING BUILDINGS SOLEDAD, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_soledad_modular_lodging_614k_2023",
    "MODULAR LODGING BUILDINGS SOLEDAD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1723_1900_19AQMM21D0039_1900/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1345",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F1723_1900_19AQMM21D0039_1900 (proyectos_colombia_soledad_modular_lodging_614k_2023). Signed 2023-07-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1723_1900_19AQMM21D0039_1900/.",
    "USASpending: proyectos_colombia_soledad_modular_lodging_614k_2023 USD 0.614m. Supports proyectos_colombia_soledad_modular_lodging_614k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 614272.21; date_signed 2023-07-28.",
    investment_type="epc",
)

# === Cycle 1345 ===
row_doc(
    "marago_colombia_caucasia_defense_wall_602k_2021",
    "infrastructure", "building_materials", "other",
    "Constructora Marago — Colombia CNP rural station defense wall Caucasia",
    "Colombia",
    "29 Sep 2021: Department of State awards contract to CONSTRUCTORA MARAGO S A S for CNP rural station defense wall construction; obligated USD 602452.70. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "602452.70", "2021-09-29", "2021", "", "",
    "CNP RURAL STATION DEFENSE WALL CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_marago_colombia_caucasia_defense_wall_602k_2021",
    "CNP RURAL STATION DEFENSE WALL CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21C0203_1900_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA MARAGO S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1345",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21C0203_1900_-NONE-_-NONE- (marago_colombia_caucasia_defense_wall_602k_2021). Signed 2021-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21C0203_1900_-NONE-_-NONE-/.",
    "USASpending: marago_colombia_caucasia_defense_wall_602k_2021 USD 0.602m. Supports marago_colombia_caucasia_defense_wall_602k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 602452.7; date_signed 2021-09-29.",
    investment_type="epc",
)

# === Cycle 1346 ===
row_doc(
    "afognak_mexico_cisen_biometrics_3569k_2012",
    "infrastructure", "building_materials", "us",
    "Afognak Diversified Services — Mexico CISEN biometrics project",
    "Mexico",
    "9 Nov 2012: Department of State awards contract to AFOGNAK DIVERSIFIED SERVICES, INC. for CISEN biometrics project NAS Mexico City; obligated USD 3568904.51. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3568904.51", "2012-11-09", "2012", "", "",
    "CISEN BIOMETRICS PROJECT - NAS MEXICO CITY, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_afognak_mexico_cisen_biometrics_3569k_2012",
    "IGF::OT::IGF OTHER FUNCTIONS: CISEN BIOMETRICS PROJECT - NAS MEXICO CITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC13M0001_1900_-NONE-_-NONE-/",
    "Actor: AFOGNAK DIVERSIFIED SERVICES, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1346",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC13M0001_1900_-NONE-_-NONE- (afognak_mexico_cisen_biometrics_3569k_2012). Signed 2012-11-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC13M0001_1900_-NONE-_-NONE-/.",
    "USASpending: afognak_mexico_cisen_biometrics_3569k_2012 USD 3.569m. Supports afognak_mexico_cisen_biometrics_3569k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3568904.51; date_signed 2012-11-09.",
    investment_type="equipment_supply",
)

# === Cycle 1346 ===
row_doc(
    "edge_colombia_motorola_radios_install_2456k_2020",
    "infrastructure", "building_materials", "us",
    "Edge Technology Distributors — Colombia Motorola radios equipment and install",
    "Colombia",
    "10 Sep 2020: Department of State awards contract to EDGE TECHNOLOGY DISTRIBUTORS, INC. for Motorola radios and equipment and install and training services for Colombia; obligated USD 2456449.93. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2456449.93", "2020-09-10", "2020", "", "",
    "MOTOROLA RADIOS AND EQUIPMENT AND INSTALL AND TRAINING SERVICES FOR COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_edge_colombia_motorola_radios_install_2456k_2020",
    "MOTOROLA RADIOS AND EQUIPMENT AND INSTALL AND TRAINING SERVICES FOR COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE20F0059_1900_47QTCA18D0016_4732/",
    "Actor: EDGE TECHNOLOGY DISTRIBUTORS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1346",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE20F0059_1900_47QTCA18D0016_4732 (edge_colombia_motorola_radios_install_2456k_2020). Signed 2020-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE20F0059_1900_47QTCA18D0016_4732/.",
    "USASpending: edge_colombia_motorola_radios_install_2456k_2020 USD 2.456m. Supports edge_colombia_motorola_radios_install_2456k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2456449.93; date_signed 2020-09-10.",
    investment_type="equipment_supply",
)

# === Cycle 1346 ===
row_doc(
    "estudios_colombia_mariquita_utilities_building_573k_2021",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Colombia Mariquita utilities building",
    "Colombia",
    "24 Sep 2021: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for construction of utilities building CNP Mariquita; obligated USD 572986.42. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "572986.42", "2021-09-24", "2021", "", "",
    "CONSTRUCTION OF UTILITIES BUILDING CNP MARIQUITA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_mariquita_utilities_building_573k_2021",
    "CONSTRUCTION OF UTILITIES BUILDING CNP MARIQUITA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3867_1900_19AQMM21D0039_1900/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1346",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21F3867_1900_19AQMM21D0039_1900 (estudios_colombia_mariquita_utilities_building_573k_2021). Signed 2021-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3867_1900_19AQMM21D0039_1900/.",
    "USASpending: estudios_colombia_mariquita_utilities_building_573k_2021 USD 0.573m. Supports estudios_colombia_mariquita_utilities_building_573k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 572986.42; date_signed 2021-09-24.",
    investment_type="epc",
)

# === Cycle 1346 ===
row_doc(
    "proyectos_colombia_soledad_tactical_house_538k_2023",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia Soledad tactical house",
    "Colombia",
    "28 Apr 2023: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for tactical house Soledad construction; obligated USD 538082.28. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "538082.28", "2023-04-28", "2023", "", "",
    "TACTICAL HOUSE SOLEDAD CONSTRUCTION., Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_soledad_tactical_house_538k_2023",
    "TACTICAL HOUSE SOLEDAD CONSTRUCTION.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1084_1900_19AQMM21D0039_1900/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1346",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F1084_1900_19AQMM21D0039_1900 (proyectos_colombia_soledad_tactical_house_538k_2023). Signed 2023-04-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1084_1900_19AQMM21D0039_1900/.",
    "USASpending: proyectos_colombia_soledad_tactical_house_538k_2023 USD 0.538m. Supports proyectos_colombia_soledad_tactical_house_538k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 538082.28; date_signed 2023-04-28.",
    investment_type="epc",
)

# === Cycle 1346 ===
row_doc(
    "estudios_honduras_gen_admin_hq_510k_2011",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Honduras general admin HQ facility",
    "Honduras",
    "29 Sep 2011: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for gen admin HQ facility; obligated USD 509742.12. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "509742.12", "2011-09-29", "2011", "", "",
    "GEN ADMIN HQ FACILITY, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_honduras_gen_admin_hq_510k_2011",
    "TAS::21 2020::TAS GEN ADMIN HQ FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127811D0050_9700/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1346",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0005_9700_W9127811D0050_9700 (estudios_honduras_gen_admin_hq_510k_2011). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0005_9700_W9127811D0050_9700/.",
    "USASpending: estudios_honduras_gen_admin_hq_510k_2011 USD 0.510m. Supports estudios_honduras_gen_admin_hq_510k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 509742.12; date_signed 2011-09-29.",
    investment_type="epc",
)

# === Cycle 1347 ===
row_doc(
    "jj_honduras_logistics_admin_facility_674k_2010",
    "infrastructure", "building_materials", "us",
    "J & J Maintenance — Honduras Soto Cano air force logistics admin facility",
    "Honduras",
    "29 Sep 2010: Department of State awards contract to J & J MAINTENANCE INC for D/B air force logistics admin facility Soto Cano AB; obligated USD 674044.07. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "674044.07", "2010-09-29", "2010", "", "",
    "D/B AIR FORCE LOGISTICS ADMIN FACILITY, SOTO CANO AB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_jj_honduras_logistics_admin_facility_674k_2010",
    "D/B AIR FORCE LOGISTICS ADMIN FACILITY, SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0012_9700_W9127809D0068_9700/",
    "Actor: J & J MAINTENANCE INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1347",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0012_9700_W9127809D0068_9700 (jj_honduras_logistics_admin_facility_674k_2010). Signed 2010-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0012_9700_W9127809D0068_9700/.",
    "USASpending: jj_honduras_logistics_admin_facility_674k_2010 USD 0.674m. Supports jj_honduras_logistics_admin_facility_674k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 674044.07; date_signed 2010-09-29.",
    investment_type="epc",
)

# === Cycle 1347 ===
row_doc(
    "astrophysics_mexico_cargo_xray_329k_2015",
    "infrastructure", "engineering_epc", "us",
    "Astrophysics — Mexico cargo x-ray inspection system",
    "Mexico",
    "24 Aug 2015: Department of State awards contract to ASTROPHYSICS INC for purchase of one cargo x-ray inspection system including CONUS delivery and installation; obligated USD 329000.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "329000.00", "2015-08-24", "2015", "", "",
    "PURCHASE OF ONE (1) CARGO X-RAY INSPECTION SYSTEM, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_astrophysics_mexico_cargo_xray_329k_2015",
    "PURCHASE OF ONE (1) CARGO X-RAY INSPECTION SYSTEM TO INCLUDE CONUS DELIVERY. PRICE INCLUDES INSTALLA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15M0030_1900_-NONE-_-NONE-/",
    "Actor: ASTROPHYSICS INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1347",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC15M0030_1900_-NONE-_-NONE- (astrophysics_mexico_cargo_xray_329k_2015). Signed 2015-08-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15M0030_1900_-NONE-_-NONE-/.",
    "USASpending: astrophysics_mexico_cargo_xray_329k_2015 USD 0.329m. Supports astrophysics_mexico_cargo_xray_329k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 329000.0; date_signed 2015-08-24.",
    investment_type="equipment_supply",
)

# === Cycle 1347 ===
row_doc(
    "misc_colombia_concrete_slab_building_517k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous Foreign Awardees — Colombia construct concrete slab and building",
    "Colombia",
    "17 Sep 2012: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for construct concrete slab and building; obligated USD 517321.35. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "517321.35", "2012-09-17", "2012", "", "",
    "CONSTRUCT CONCRETE SLAB AND BUILDING, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_concrete_slab_building_517k_2012",
    "CONSTRUCT CONCRETE SLAB AND BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0019_9700_-NONE-_-NONE-/",
    "Actor: MISCELLANEOUS FOREIGN AWARDEES — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1347",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12C0019_9700_-NONE-_-NONE- (misc_colombia_concrete_slab_building_517k_2012). Signed 2012-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0019_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_concrete_slab_building_517k_2012 USD 0.517m. Supports misc_colombia_concrete_slab_building_517k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 517321.35; date_signed 2012-09-17.",
    investment_type="epc",
)

# === Cycle 1347 ===
row_doc(
    "proyectos_colombia_mariquita_lodging_481k_2018",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia Mariquita lodging building",
    "Colombia",
    "16 Nov 2018: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for Mariquita lodging building construction; obligated USD 481271.67. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "481271.67", "2018-11-16", "2018", "", "",
    "MARIQUITA LODGING BUILDING CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_mariquita_lodging_481k_2018",
    "MARIQUITA LODGING BUILDING CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0009_1900_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1347",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0009_1900_-NONE-_-NONE- (proyectos_colombia_mariquita_lodging_481k_2018). Signed 2018-11-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0009_1900_-NONE-_-NONE-/.",
    "USASpending: proyectos_colombia_mariquita_lodging_481k_2018 USD 0.481m. Supports proyectos_colombia_mariquita_lodging_481k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 481271.67; date_signed 2018-11-16.",
    investment_type="epc",
)

# === Cycle 1347 ===
row_doc(
    "estudios_colombia_classroom_building_344k_2022",
    "infrastructure", "building_materials", "other",
    "Estudios Edificaciones EEII — Colombia classroom building construction",
    "Colombia",
    "19 Apr 2022: Department of State awards contract to ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S for classroom building construction; obligated USD 344427.13. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "344427.13", "2022-04-19", "2022", "", "",
    "CLASSROOM BUILDING CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_estudios_colombia_classroom_building_344k_2022",
    "CLASSROOM BUILDING CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0626_1900_19AQMM21D0039_1900/",
    "Actor: ESTUDIOS EDIFICACIONES E INTERVENTORIAS EN INGENIERIA EEII S A S — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1347",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F0626_1900_19AQMM21D0039_1900 (estudios_colombia_classroom_building_344k_2022). Signed 2022-04-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0626_1900_19AQMM21D0039_1900/.",
    "USASpending: estudios_colombia_classroom_building_344k_2022 USD 0.344m. Supports estudios_colombia_classroom_building_344k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 344427.13; date_signed 2022-04-19.",
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
