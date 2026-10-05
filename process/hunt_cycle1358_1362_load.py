#!/usr/bin/env python3
"""Cycles 1358–1362: USASpending LatAm CapEx (FAAC/Virtra/Obera + Eterna/MFG/Proyectos residual EPC).

Seeds: 20262358–20262362. Thin top-up dry.
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

# === Cycle 1358 ===
row_doc(
    "faac_mexico_firearms_training_simulators_725k_2020",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico firearms training simulators",
    "Mexico",
    "02 Apr 2020: Department of State awards contract to FAAC INCORPORATED for firearms training simulators; obligated USD 724634.98. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "724634.98", "2020-04-02", "2020", "", "",
    "REQUIREMENT FOR FIREARMS TRAINING SIMULATORS., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_firearms_training_simulators_725k_2020",
    "REQUIREMENT FOR FIREARMS TRAINING SIMULATORS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1333_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle bridges_roads dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1358",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F1333_1900_SWHARC16D0002_1900 (faac_mexico_firearms_training_simulators_725k_2020). Signed 2020-04-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1333_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_firearms_training_simulators_725k_2020 USD 0.725m. Supports faac_mexico_firearms_training_simulators_725k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 724634.98; date_signed 2020-04-02.",
    investment_type="equipment_supply",
)

# === Cycle 1358 ===
row_doc(
    "virtra_mexico_firearms_training_simulators_593k_2020",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico firearms training simulators",
    "Mexico",
    "02 Apr 2020: Department of State awards contract to VIRTRA, INC. for firearms training simulators; obligated USD 593107.80. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "593107.80", "2020-04-02", "2020", "", "",
    "REQUIREMENT FOR FIREARMS TRAINING SIMULATORS., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_firearms_training_simulators_593k_2020",
    "REQUIREMENT FOR FIREARMS TRAINING SIMULATORS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1326_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle water dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1358",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F1326_1900_SWHARC16D0003_1900 (virtra_mexico_firearms_training_simulators_593k_2020). Signed 2020-04-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1326_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_firearms_training_simulators_593k_2020 USD 0.593m. Supports virtra_mexico_firearms_training_simulators_593k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 593107.80; date_signed 2020-04-02.",
    investment_type="equipment_supply",
)

# === Cycle 1358 ===
row_doc(
    "eterna_honduras_resurface_landing_zone_phase1_806k_2010",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Honduras Soto Cano landing zone resurface Phase 1 design-build",
    "Honduras",
    "27 Sep 2010: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D/B resurface landing zone Phase 1, Soto Cano AB, Honduras; obligated USD 805883.49. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "805883.49", "2010-09-27", "2010", "", "",
    "D/B RESURFACE LANDING ZONE PHASE 1, SOTO CANO AB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_resurface_landing_zone_phase1_806k_2010",
    "D/B RESURFACE LANDING ZONE PHASE 1, SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0015_9700_W9127809D0071_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads CapEx.",
    "hunt_cycle1358",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0015_9700_W9127809D0071_9700 (eterna_honduras_resurface_landing_zone_phase1_806k_2010). Signed 2010-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0015_9700_W9127809D0071_9700/.",
    "USASpending: eterna_honduras_resurface_landing_zone_phase1_806k_2010 USD 0.806m. Supports eterna_honduras_resurface_landing_zone_phase1_806k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 805883.49; date_signed 2010-09-27.",
    investment_type="epc",
)

# === Cycle 1358 ===
row_doc(
    "eterna_honduras_taxiway_charlie_shoulders_400k_2024",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Honduras Soto Cano taxiway Charlie shoulders construction",
    "Honduras",
    "15 Nov 2024: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. to construct taxiway Charlie shoulders, Soto Cano Air Base, Honduras; obligated USD 399841.73. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "399841.73", "2024-11-15", "2024", "", "",
    "CONSTRUCT TAXIWAY CHARLIE SHOULDERS, SOTO CANO AIR BASE, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_taxiway_charlie_shoulders_400k_2024",
    "CONSTRUCT TAXIWAY CHARLIE SHOULDERS, SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825F0023_9700_W9127823D0073_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads CapEx.",
    "hunt_cycle1358",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825F0023_9700_W9127823D0073_9700 (eterna_honduras_taxiway_charlie_shoulders_400k_2024). Signed 2024-11-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825F0023_9700_W9127823D0073_9700/.",
    "USASpending: eterna_honduras_taxiway_charlie_shoulders_400k_2024 USD 0.400m. Supports eterna_honduras_taxiway_charlie_shoulders_400k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 399841.73; date_signed 2024-11-15.",
    investment_type="epc",
)

# === Cycle 1358 ===
row_doc(
    "eterna_honduras_construction_project_448516_395k_2014",
    "infrastructure", "building_materials", "other",
    "Eterna — Honduras construction project 448516",
    "Honduras",
    "30 Sep 2014: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for construction project 448516; obligated USD 395334.07. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "395334.07", "2014-09-30", "2014", "", "",
    "CONSTRUCTION PROJECT: 448516, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_construction_project_448516_395k_2014",
    "IGF::OT::IGF CONSTRUCTION PROJECT: 448516",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0015_9700_W9127813D0020_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1358",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0015_9700_W9127813D0020_9700 (eterna_honduras_construction_project_448516_395k_2014). Signed 2014-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0015_9700_W9127813D0020_9700/.",
    "USASpending: eterna_honduras_construction_project_448516_395k_2014 USD 0.395m. Supports eterna_honduras_construction_project_448516_395k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 395334.07; date_signed 2014-09-30.",
    investment_type="epc",
)

# === Cycle 1359 ===
row_doc(
    "virtra_mexico_firearms_training_simulators_579k_2020",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico firearms training simulators",
    "Mexico",
    "02 Apr 2020: Department of State awards contract to VIRTRA, INC. for firearms training simulators; obligated USD 579093.12. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "579093.12", "2020-04-02", "2020", "", "",
    "REQUIREMENT FOR FIREARMS TRAINING SIMULATORS., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_firearms_training_simulators_579k_2020",
    "REQUIREMENT FOR FIREARMS TRAINING SIMULATORS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1330_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle fission_smr dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1359",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F1330_1900_SWHARC16D0003_1900 (virtra_mexico_firearms_training_simulators_579k_2020). Signed 2020-04-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1330_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_firearms_training_simulators_579k_2020 USD 0.579m. Supports virtra_mexico_firearms_training_simulators_579k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 579093.12; date_signed 2020-04-02.",
    investment_type="equipment_supply",
)

# === Cycle 1359 ===
row_doc(
    "faac_mexico_firearms_training_simulators_573k_2020",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico firearms training simulators",
    "Mexico",
    "02 Apr 2020: Department of State awards contract to FAAC INCORPORATED for firearms training simulators; obligated USD 573366.51. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "573366.51", "2020-04-02", "2020", "", "",
    "REQUIREMENT FIREARMS TRAINING SIMULATORS., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_firearms_training_simulators_573k_2020",
    "REQUIREMENT FIREARMS TRAINING SIMULATORS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1325_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle wind dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1359",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F1325_1900_SWHARC16D0002_1900 (faac_mexico_firearms_training_simulators_573k_2020). Signed 2020-04-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1325_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_firearms_training_simulators_573k_2020 USD 0.573m. Supports faac_mexico_firearms_training_simulators_573k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 573366.51; date_signed 2020-04-02.",
    investment_type="equipment_supply",
)

# === Cycle 1359 ===
row_doc(
    "eterna_honduras_taxiway_hotel_392k_2022",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Honduras Soto Cano taxiway Hotel",
    "Honduras",
    "09 Sep 2022: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for taxiway Hotel Soto Cano Air Base, HN; obligated USD 391875.75. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "391875.75", "2022-09-09", "2022", "", "",
    "TAXIWAY HOTEL SOTO CANO AIR BASE, HN, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_taxiway_hotel_392k_2022",
    "TAXIWAY HOTEL SOTO CANO AIR BASE, HN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0306_9700_W9127821D0075_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads CapEx.",
    "hunt_cycle1359",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0306_9700_W9127821D0075_9700 (eterna_honduras_taxiway_hotel_392k_2022). Signed 2022-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0306_9700_W9127821D0075_9700/.",
    "USASpending: eterna_honduras_taxiway_hotel_392k_2022 USD 0.392m. Supports eterna_honduras_taxiway_hotel_392k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 391875.75; date_signed 2022-09-09.",
    investment_type="epc",
)

# === Cycle 1359 ===
row_doc(
    "eterna_honduras_puerto_castilla_helo_pads_375k_2012",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Honduras Puerto Castilla helo landing pads and team room",
    "Honduras",
    "09 Mar 2012: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for construction of helo landing pads and team room improvements at Puerto Castilla, Honduras; obligated USD 374881.91. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "374881.91", "2012-03-09", "2012", "", "",
    "CONSTRUCTION OF HELO LANDING PADS AND TEAM ROOM IMPROVEMENTS AT PUERTO CASTILLA, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_puerto_castilla_helo_pads_375k_2012",
    "TAS::21 2020::TAS CONSTRUCTION OF HELO LANDING PADS AND TEAM ROOM IMPROVEMENTS AT PUERTO CASTILLA, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0014_9700_W9127811D0046_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads CapEx.",
    "hunt_cycle1359",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0014_9700_W9127811D0046_9700 (eterna_honduras_puerto_castilla_helo_pads_375k_2012). Signed 2012-03-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0014_9700_W9127811D0046_9700/.",
    "USASpending: eterna_honduras_puerto_castilla_helo_pads_375k_2012 USD 0.375m. Supports eterna_honduras_puerto_castilla_helo_pads_375k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 374881.91; date_signed 2012-03-09.",
    investment_type="epc",
)

# === Cycle 1359 ===
row_doc(
    "eterna_honduras_taxiway_golf_356k_2022",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Honduras Soto Cano taxiway Golf",
    "Honduras",
    "09 Sep 2022: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for taxiway Golf SCAB, HN; obligated USD 356013.20. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "356013.20", "2022-09-09", "2022", "", "",
    "TAXIWAY GOLF SCAB, HN, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_taxiway_golf_356k_2022",
    "TAXIWAY GOLF SCAB, HN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0312_9700_W9127821D0075_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads CapEx.",
    "hunt_cycle1359",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0312_9700_W9127821D0075_9700 (eterna_honduras_taxiway_golf_356k_2022). Signed 2022-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0312_9700_W9127821D0075_9700/.",
    "USASpending: eterna_honduras_taxiway_golf_356k_2022 USD 0.356m. Supports eterna_honduras_taxiway_golf_356k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 356013.20; date_signed 2022-09-09.",
    investment_type="epc",
)

# === Cycle 1360 ===
row_doc(
    "virtra_mexico_sidepol_slp_juarez_simulators_567k_2016",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico SIDEPOL/San Luis Potosi/Ciudad Juarez firearms simulators",
    "Mexico",
    "26 Sep 2016: Department of State awards contract to VIRTRA, INC. for three firearms training simulators for SIDEPOL, San Luis Potosi, and Ciudad Juarez including installation; obligated USD 566545.32. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "566545.32", "2016-09-26", "2016", "", "",
    "INL MEXICO - THREE (3) FIREARMS TRAINING SIMULATORS FOR SIDEPOL, SAN LUIS POTOSI, AND CIUD, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_sidepol_slp_juarez_simulators_567k_2016",
    "INL MEXICO - THREE (3) FIREARMS TRAINING SIMULATORS FOR SIDEPOL, SAN LUIS POTOSI, AND CIUDAD JUAREZ. INCLUDES INSTALLATION AND 3-YEAR IN-COUNTRY WARRANTY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0041_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1360",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16F0041_1900_SWHARC16D0003_1900 (virtra_mexico_sidepol_slp_juarez_simulators_567k_2016). Signed 2016-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16F0041_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_sidepol_slp_juarez_simulators_567k_2016 USD 0.567m. Supports virtra_mexico_sidepol_slp_juarez_simulators_567k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 566545.32; date_signed 2016-09-26.",
    investment_type="equipment_supply",
)

# === Cycle 1360 ===
row_doc(
    "virtra_el_salvador_virtual_shooting_simulator_521k_2024",
    "infrastructure", "engineering_epc", "us",
    "Virtra — El Salvador INL virtual shooting simulator",
    "El Salvador",
    "09 Jul 2024: Department of State awards contract to VIRTRA, INC. for procurement of a virtual shooting simulator for INL/El Salvador; obligated USD 520521.62. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "520521.62", "2024-07-09", "2024", "", "",
    "PURCHASE AWARD FOR INL/EL SALVADOR FOR THE PROCUREMENT OF A VIRTUAL SHOOTING SIMULATOR WIT, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_el_salvador_virtual_shooting_simulator_521k_2024",
    "PURCHASE AWARD FOR INL/EL SALVADOR FOR THE PROCUREMENT OF A VIRTUAL SHOOTING SIMULATOR WITH THE OPTION TO EXERCISE ADDITIONAL TRAINING YEARS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24P0066_1900_-NONE-_-NONE-/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle solar dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1360",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24P0066_1900_-NONE-_-NONE- (virtra_el_salvador_virtual_shooting_simulator_521k_2024). Signed 2024-07-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24P0066_1900_-NONE-_-NONE-/.",
    "USASpending: virtra_el_salvador_virtual_shooting_simulator_521k_2024 USD 0.521m. Supports virtra_el_salvador_virtual_shooting_simulator_521k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 520521.62; date_signed 2024-07-09.",
    investment_type="equipment_supply",
)

# === Cycle 1360 ===
row_doc(
    "eterna_guatemala_chiquimula_elementary_school_326k_2017",
    "infrastructure", "building_materials", "other",
    "Eterna — Guatemala Chiquimula elementary school",
    "Guatemala",
    "30 Sep 2017: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for Chiquimula elementary school, Guatemala; obligated USD 326162.40. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "326162.40", "2017-09-30", "2017", "", "",
    "CHIQUIMULA ELEMENTARY SCHOOL, GUATEMALA, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_guatemala_chiquimula_elementary_school_326k_2017",
    "IGF::OT::IGF CHIQUIMULA ELEMENTARY SCHOOL, GUATEMALA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0507_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1360",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0507_9700_W9127816D0102_9700 (eterna_guatemala_chiquimula_elementary_school_326k_2017). Signed 2017-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0507_9700_W9127816D0102_9700/.",
    "USASpending: eterna_guatemala_chiquimula_elementary_school_326k_2017 USD 0.326m. Supports eterna_guatemala_chiquimula_elementary_school_326k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 326162.40; date_signed 2017-09-30.",
    investment_type="epc",
)

# === Cycle 1360 ===
row_doc(
    "eterna_honduras_gca_facility_r34_278k_2017",
    "infrastructure", "building_materials", "other",
    "Eterna — Honduras Soto Cano convert building R-34 to GCA facility",
    "Honduras",
    "09 Jun 2017: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. to convert building R-34 to ground control approach facility at Soto Cano Air Base Honduras; obligated USD 278418.66. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "278418.66", "2017-06-09", "2017", "", "",
    "CONSTRUCTION OF CONVERT BUILDING R-34 TO GROUND CONTROL APPROACH FACILITY AT SOTO CANO AIR, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_gca_facility_r34_278k_2017",
    "IGF::OT::IGF  CONSTRUCTION OF CONVERT BUILDING R-34 TO GROUND CONTROL APPROACH FACILITY AT SOTO CANO AIR BASE HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0044_9700_W9127813D0020_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1360",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0044_9700_W9127813D0020_9700 (eterna_honduras_gca_facility_r34_278k_2017). Signed 2017-06-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0044_9700_W9127813D0020_9700/.",
    "USASpending: eterna_honduras_gca_facility_r34_278k_2017 USD 0.278m. Supports eterna_honduras_gca_facility_r34_278k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 278418.66; date_signed 2017-06-09.",
    investment_type="epc",
)

# === Cycle 1360 ===
row_doc(
    "eterna_honduras_perimeter_fence_269k_2014",
    "infrastructure", "building_materials", "other",
    "Eterna — Honduras perimeter fence construction",
    "Honduras",
    "27 Sep 2014: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for perimeter fence; obligated USD 269452.77. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "269452.77", "2014-09-27", "2014", "", "",
    "PERIMETER FENCE, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_perimeter_fence_269k_2014",
    "IGF::OT::IGF PERIMETER FENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127813D0020_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1360",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0008_9700_W9127813D0020_9700 (eterna_honduras_perimeter_fence_269k_2014). Signed 2014-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127813D0020_9700/.",
    "USASpending: eterna_honduras_perimeter_fence_269k_2014 USD 0.269m. Supports eterna_honduras_perimeter_fence_269k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 269452.77; date_signed 2014-09-27.",
    investment_type="epc",
)

# === Cycle 1361 ===
row_doc(
    "faac_mexico_aguascalientes_guerrero_michoacan_simulators_518k_2017",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Mexico Aguascalientes/Guerrero/Michoacan fixed and portable firearms simulators",
    "Mexico",
    "27 Sep 2017: Department of State awards contract to FAAC INCORPORATED for fixed and portable firearms training simulators for Aguascalientes, Guerrero, and Michoacan including installation; obligated USD 517904.47. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "517904.47", "2017-09-27", "2017", "", "",
    "INL MEXICO FIXED AND PORTABLE FIREARMS TRAINING SIMULATORS FOR AGUASCALIENTES, GUERRERO, A, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_mexico_aguascalientes_guerrero_michoacan_simulators_518k_2017",
    "INL MEXICO FIXED AND PORTABLE FIREARMS TRAINING SIMULATORS FOR AGUASCALIENTES, GUERRERO, AND MICHOACAN. INCLUDES INSTALLATION AND 3-YEAR IN-COUNTRY WARRANTY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0034_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle water dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1361",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC17F0034_1900_SWHARC16D0002_1900 (faac_mexico_aguascalientes_guerrero_michoacan_simulators_518k_2017). Signed 2017-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC17F0034_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_mexico_aguascalientes_guerrero_michoacan_simulators_518k_2017 USD 0.518m. Supports faac_mexico_aguascalientes_guerrero_michoacan_simulators_518k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 517904.47; date_signed 2017-09-27.",
    investment_type="equipment_supply",
)

# === Cycle 1361 ===
row_doc(
    "virtra_mexico_firearms_training_simulators_509k_2020",
    "infrastructure", "engineering_epc", "us",
    "Virtra — Mexico firearms training simulators",
    "Mexico",
    "03 Apr 2020: Department of State awards contract to VIRTRA, INC. for firearms training simulators; obligated USD 509227.84. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "509227.84", "2020-04-03", "2020", "", "",
    "REQUIREMENT FOR FIREARMS TRAINING SIMULATORS., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_virtra_mexico_firearms_training_simulators_509k_2020",
    "REQUIREMENT FOR FIREARMS TRAINING SIMULATORS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1340_1900_SWHARC16D0003_1900/",
    "Actor: VIRTRA, INC. (U.S.) — us. Official USASpending Award API. Shuffle solar dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1361",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F1340_1900_SWHARC16D0003_1900 (virtra_mexico_firearms_training_simulators_509k_2020). Signed 2020-04-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F1340_1900_SWHARC16D0003_1900/.",
    "USASpending: virtra_mexico_firearms_training_simulators_509k_2020 USD 0.509m. Supports virtra_mexico_firearms_training_simulators_509k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 509227.84; date_signed 2020-04-03.",
    investment_type="equipment_supply",
)

# === Cycle 1361 ===
row_doc(
    "eterna_costa_rica_educational_building_254k_2010",
    "infrastructure", "building_materials", "other",
    "Eterna — Costa Rica HAP 7615 renovate educational building",
    "Costa Rica",
    "30 Sep 2010: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D/B HAP 7615 renovate educational build, Costa Rica; obligated USD 253683.11. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "253683.11", "2010-09-30", "2010", "", "",
    "D/B HAP 7615 RENOVATE EDUCATIONAL BUILD, COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_costa_rica_educational_building_254k_2010",
    "D/B HAP 7615 RENOVATE EDUCATIONAL BUILD, COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0022_9700_W9127809D0071_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1361",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0022_9700_W9127809D0071_9700 (eterna_costa_rica_educational_building_254k_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0022_9700_W9127809D0071_9700/.",
    "USASpending: eterna_costa_rica_educational_building_254k_2010 USD 0.254m. Supports eterna_costa_rica_educational_building_254k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 253683.11; date_signed 2010-09-30.",
    investment_type="epc",
)

# === Cycle 1361 ===
row_doc(
    "eterna_honduras_rejection_lane_search_pit_245k_2011",
    "infrastructure", "building_materials", "other",
    "Eterna — Honduras Soto Cano rejection lane search pit",
    "Honduras",
    "24 Sep 2011: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. to construct rejection lane search pit, Soto Cano Air Base, Honduras; obligated USD 244971.11. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "244971.11", "2011-09-24", "2011", "", "",
    "CONSTRUCT REJECTION LANE SEARCH PIT, SOTO CANO AIR BASE, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_rejection_lane_search_pit_245k_2011",
    "TAS::21 2020::TAS CONSTRUCT REJECTION LANE SEARCH PIT, SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127811D0046_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1361",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0006_9700_W9127811D0046_9700 (eterna_honduras_rejection_lane_search_pit_245k_2011). Signed 2011-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127811D0046_9700/.",
    "USASpending: eterna_honduras_rejection_lane_search_pit_245k_2011 USD 0.245m. Supports eterna_honduras_rejection_lane_search_pit_245k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 244971.11; date_signed 2011-09-24.",
    investment_type="epc",
)

# === Cycle 1361 ===
row_doc(
    "mfg_colombia_antenna_tower_puerto_rico_74k_2011",
    "infrastructure", "engineering_epc", "other",
    "MFG Ingenieria — Colombia Puerto Rico antenna tower",
    "Colombia",
    "15 Sep 2011: Department of Defense awards contract to MFG INGENIERIA SAS for antenna tower Puerto Rico Colombia; obligated USD 74459.19. CapEx face = award obligation. Exact site coords not stated — lat/lon blank. Named site is Puerto Rico, Colombia (municipality), not U.S. territory.",
    "74459.19", "2011-09-15", "2011", "", "",
    "ANTENNA TOWER PUERTO RICO COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mfg_colombia_antenna_tower_puerto_rico_74k_2011",
    "ANTENNA TOWER PUERTO RICO COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0035_9700_-NONE-_-NONE-/",
    "Actor: MFG INGENIERIA SAS — other. Official USASpending Award API. Shuffle engineering_epc CapEx. Puerto Rico Colombia municipality.",
    "hunt_cycle1361",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11C0035_9700_-NONE-_-NONE- (mfg_colombia_antenna_tower_puerto_rico_74k_2011). Signed 2011-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0035_9700_-NONE-_-NONE-/.",
    "USASpending: mfg_colombia_antenna_tower_puerto_rico_74k_2011 USD 0.074m. Supports mfg_colombia_antenna_tower_puerto_rico_74k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 74459.19; date_signed 2011-09-15.",
    investment_type="epc",
)

# === Cycle 1362 ===
row_doc(
    "obera_panama_license_plate_recognition_install_480k_2017",
    "infrastructure", "engineering_epc", "us",
    "Obera — Panama license plate recognition system installment",
    "Panama",
    "18 Sep 2017: Department of Defense awards contract to OBERA LLC for license plate recognition system installment and sustainment; obligated USD 480084.31. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "480084.31", "2017-09-18", "2017", "", "",
    "LICENSE PLATE RECOGNITION SYSTEM INSTALLMENT AND SUSTAINMENT, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_obera_panama_license_plate_recognition_install_480k_2017",
    "IGF::OT::IGF LICENSE PLATE RECOGNITION SYSTEM INSTALLMENT AND SUSTAINMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489017F3056_9700_FA489016D0013_9700/",
    "Actor: OBERA LLC (U.S.) — us. Official USASpending Award API. Shuffle lithium dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1362",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489017F3056_9700_FA489016D0013_9700 (obera_panama_license_plate_recognition_install_480k_2017). Signed 2017-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489017F3056_9700_FA489016D0013_9700/.",
    "USASpending: obera_panama_license_plate_recognition_install_480k_2017 USD 0.480m. Supports obera_panama_license_plate_recognition_install_480k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 480084.31; date_signed 2017-09-18.",
    investment_type="equipment_supply",
)

# === Cycle 1362 ===
row_doc(
    "faac_honduras_training_simulators_347k_2019",
    "infrastructure", "engineering_epc", "us",
    "FAAC — Honduras training simulators",
    "Honduras",
    "21 Feb 2019: Department of State awards contract to FAAC INCORPORATED for training simulators; obligated USD 346982.34. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "346982.34", "2019-02-21", "2019", "", "",
    "REQUIREMENT FOR TRAINING SIMULATORS., Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_faac_honduras_training_simulators_347k_2019",
    "REQUIREMENT FOR TRAINING SIMULATORS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F0826_1900_SWHARC16D0002_1900/",
    "Actor: FAAC INCORPORATED (U.S.) — us. Official USASpending Award API. Shuffle rail dry→engineering_epc CapEx; ≥1/3 U.S.",
    "hunt_cycle1362",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19F0826_1900_SWHARC16D0002_1900 (faac_honduras_training_simulators_347k_2019). Signed 2019-02-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F0826_1900_SWHARC16D0002_1900/.",
    "USASpending: faac_honduras_training_simulators_347k_2019 USD 0.347m. Supports faac_honduras_training_simulators_347k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 346982.34; date_signed 2019-02-21.",
    investment_type="equipment_supply",
)

# === Cycle 1362 ===
row_doc(
    "mfg_colombia_scaffold_antenna_tower_48k_2011",
    "infrastructure", "engineering_epc", "other",
    "MFG Ingenieria — Colombia scaffold antenna tower",
    "Colombia",
    "20 Sep 2011: Department of Defense awards contract to MFG INGENIERIA SAS for scaffold antenna tower; obligated USD 47557.04. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "47557.04", "2011-09-20", "2011", "", "",
    "SCAFFOLD ANTENNA TOWER, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mfg_colombia_scaffold_antenna_tower_48k_2011",
    "SCAFFOLD ANTENNA TOWER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0037_9700_-NONE-_-NONE-/",
    "Actor: MFG INGENIERIA SAS — other. Official USASpending Award API. Shuffle engineering_epc CapEx.",
    "hunt_cycle1362",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11C0037_9700_-NONE-_-NONE- (mfg_colombia_scaffold_antenna_tower_48k_2011). Signed 2011-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0037_9700_-NONE-_-NONE-/.",
    "USASpending: mfg_colombia_scaffold_antenna_tower_48k_2011 USD 0.048m. Supports mfg_colombia_scaffold_antenna_tower_48k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 47557.04; date_signed 2011-09-20.",
    investment_type="epc",
)

# === Cycle 1362 ===
row_doc(
    "proyectos_colombia_construction_47k_2010",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia construction",
    "Colombia",
    "27 Sep 2010: Department of Defense awards contract to PROYECTOS CIVILES S Y M LIMITADA for construction; obligated USD 47151.55. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "47151.55", "2010-09-27", "2010", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_construction_47k_2010",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10P0236_9700_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1362",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT10P0236_9700_-NONE-_-NONE- (proyectos_colombia_construction_47k_2010). Signed 2010-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10P0236_9700_-NONE-_-NONE-/.",
    "USASpending: proyectos_colombia_construction_47k_2010 USD 0.047m. Supports proyectos_colombia_construction_47k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 47151.55; date_signed 2010-09-27.",
    investment_type="epc",
)

# === Cycle 1362 ===
row_doc(
    "proyectos_colombia_construction_27k_2011",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia construction",
    "Colombia",
    "06 Sep 2011: Department of Defense awards contract to PROYECTOS CIVILES S Y M LIMITADA for construction; obligated USD 27236.34. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "27236.34", "2011-09-06", "2011", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_construction_27k_2011",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0236_9700_-NONE-_-NONE-/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials CapEx.",
    "hunt_cycle1362",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11P0236_9700_-NONE-_-NONE- (proyectos_colombia_construction_27k_2011). Signed 2011-09-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0236_9700_-NONE-_-NONE-/.",
    "USASpending: proyectos_colombia_construction_27k_2011 USD 0.027m. Supports proyectos_colombia_construction_27k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 27236.34; date_signed 2011-09-06.",
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
