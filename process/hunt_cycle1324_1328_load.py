#!/usr/bin/env python3
"""Cycles 1324–1328: USASpending LatAm CapEx (Alutiiq IT/NII + Eterna/Marago/Proyectos/Misc EPC).

Seeds: 20262324–20262328. Thin top-up dry.
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

# === Cycle 1324 ===
row_doc(
    "alutiiq_mexico_guanajuato_it_infra_2872k_2022",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Mexico Guanajuato IT infrastructure integration",
    "Mexico",
    "26 Aug 2022: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for FA2 Guanajuato IT infrastructure integration; obligated USD 2872371.31. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2872371.31", "2022-08-26", "2022", "", "",
    "FA2 GUANAJUATO IT INFRASTRUCTURE INTEGRATION, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_guanajuato_it_infra_2872k_2022",
    "FA2 GUANAJUATO IT INFRASTRUCTURE INTEGRATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR22F5011_1900_19AQMM20D0010_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1324",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMR22F5011_1900_19AQMM20D0010_1900 (alutiiq_mexico_guanajuato_it_infra_2872k_2022). Signed 2022-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR22F5011_1900_19AQMM20D0010_1900/.",
    "USASpending: alutiiq_mexico_guanajuato_it_infra_2872k_2022 USD 2.872m. Supports alutiiq_mexico_guanajuato_it_infra_2872k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2872371.31; date_signed 2022-08-26.",
    investment_type="equipment_supply",
)

# === Cycle 1324 ===
row_doc(
    "alutiiq_mexico_sidel_criminal_info_system_2624k_2016",
    "infrastructure", "building_materials", "us",
    "Alutiiq Technical Services — Mexico SIDEL criminal information system",
    "Mexico",
    "29 Sep 2016: Department of State awards contract to ALUTIIQ TECHNICAL SERVICES LLC for Criminal Information System SIDEL Mexico City; obligated USD 2623555.05. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2623555.05", "2016-09-29", "2016", "", "",
    "CRIMINAL INFORMATION SYSTEM- SISTEMA DE INFORMACION DELICTIVA (SIDEL) MEXICO CITY, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_sidel_criminal_info_system_2624k_2016",
    "CRIMINAL INFORMATION SYSTEM- SISTEMA DE INFORMACION DELICTIVA (SIDEL) MEXICO CITY IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16M0023_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ TECHNICAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1324",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16M0023_1900_-NONE-_-NONE- (alutiiq_mexico_sidel_criminal_info_system_2624k_2016). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16M0023_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_sidel_criminal_info_system_2624k_2016 USD 2.624m. Supports alutiiq_mexico_sidel_criminal_info_system_2624k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2623555.05; date_signed 2016-09-29.",
    investment_type="equipment_supply",
)

# === Cycle 1324 ===
row_doc(
    "eterna_colombia_tolemaida_arws_5298k_2022",
    "infrastructure", "engineering_epc", "other",
    "Empresa Eterna — Colombia Fort Tolemaida ARWS",
    "Colombia",
    "7 Dec 2022: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for ARWS FT Tolemaida base bid and options; obligated USD 5298294.20. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "5298294.20", "2022-12-07", "2022", "", "",
    "ARWS FT TOLEMAIDA BASE BID AND OPTIONS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_colombia_tolemaida_arws_5298k_2022",
    "ARWS FT TOLEMAIDA BASE BID AND OPTIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0021_9700_W9127817D0095_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1324",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127823F0021_9700_W9127817D0095_9700 (eterna_colombia_tolemaida_arws_5298k_2022). Signed 2022-12-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0021_9700_W9127817D0095_9700/.",
    "USASpending: eterna_colombia_tolemaida_arws_5298k_2022 USD 5.298m. Supports eterna_colombia_tolemaida_arws_5298k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5298294.2; date_signed 2022-12-07.",
    investment_type="epc",
)

# === Cycle 1324 ===
row_doc(
    "eterna_belize_hap_two_projects_1865k_2022",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Belize two HAP projects",
    "Belize",
    "27 Sep 2022: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for two HAP projects in Belize; obligated USD 1864557.63. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1864557.63", "2022-09-27", "2022", "", "",
    "TWO HAP PROJECTS IN BELIZE, Belize (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_belize_hap_two_projects_1865k_2022",
    "TWO HAP PROJECTS IN BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0416_9700_W9127821D0075_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1324",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0416_9700_W9127821D0075_9700 (eterna_belize_hap_two_projects_1865k_2022). Signed 2022-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0416_9700_W9127821D0075_9700/.",
    "USASpending: eterna_belize_hap_two_projects_1865k_2022 USD 1.865m. Supports eterna_belize_hap_two_projects_1865k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1864557.63; date_signed 2022-09-27.",
    investment_type="epc",
)

# === Cycle 1324 ===
row_doc(
    "marago_colombia_pijaos_utilities_1139k_2019",
    "infrastructure", "engineering_epc", "other",
    "Constructora Marago — Colombia CNP GOER utilities Pijaos",
    "Colombia",
    "30 Sep 2019: Department of State awards contract to CONSTRUCTORA MARAGO S A S for CNP GOER utilities and exterior work Pijaos; obligated USD 1139297.82. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1139297.82", "2019-09-30", "2019", "", "",
    "CNP GOER UTILITIES AND EXTERIOR WORK - PIJAOS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_marago_colombia_pijaos_utilities_1139k_2019",
    "CNP GOER UTILITIES AND EXTERIOR WORK - PIJAOS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0157_1900_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA MARAGO S A S — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1324",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0157_1900_-NONE-_-NONE- (marago_colombia_pijaos_utilities_1139k_2019). Signed 2019-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0157_1900_-NONE-_-NONE-/.",
    "USASpending: marago_colombia_pijaos_utilities_1139k_2019 USD 1.139m. Supports marago_colombia_pijaos_utilities_1139k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1139297.82; date_signed 2019-09-30.",
    investment_type="epc",
)

# === Cycle 1325 ===
row_doc(
    "alutiiq_mexico_codis_genetics_it_2093k_2023",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Mexico CODIS genetics database IT equipment",
    "Mexico",
    "12 Sep 2023: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for IT equipment for genetics database CODIS project Mexico City; obligated USD 2092711.10. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2092711.10", "2023-09-12", "2023", "", "",
    "IT EQUIPMENT FOR GENETICS DATABASE (CODIS) PROJECT - MEXICO CITY, MEXICO, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_codis_genetics_it_2093k_2023",
    "IT EQUIPMENT FOR GENETICS DATABASE (CODIS) PROJECT - MEXICO CITY, MEXICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5012_1900_19AQMM20D0010_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1325",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMR23F5012_1900_19AQMM20D0010_1900 (alutiiq_mexico_codis_genetics_it_2093k_2023). Signed 2023-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5012_1900_19AQMM20D0010_1900/.",
    "USASpending: alutiiq_mexico_codis_genetics_it_2093k_2023 USD 2.093m. Supports alutiiq_mexico_codis_genetics_it_2093k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2092711.1; date_signed 2023-09-12.",
    investment_type="equipment_supply",
)

# === Cycle 1325 ===
row_doc(
    "alutiiq_guatemala_pnc_it_equipment_1368k_2022",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Guatemala PNC IT equipment",
    "Guatemala",
    "11 Jul 2022: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for IT equipment for the PNC in Guatemala; obligated USD 1368226.25. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1368226.25", "2022-07-11", "2022", "", "",
    "REQUIREMENT FOR IT EQUIPMENT FOR THE PNC IN GUATEMALA., Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_guatemala_pnc_it_equipment_1368k_2022",
    "REQUIREMENT FOR IT EQUIPMENT FOR THE PNC IN GUATEMALA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2444_1900_19AQMM20D0010_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1325",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F2444_1900_19AQMM20D0010_1900 (alutiiq_guatemala_pnc_it_equipment_1368k_2022). Signed 2022-07-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2444_1900_19AQMM20D0010_1900/.",
    "USASpending: alutiiq_guatemala_pnc_it_equipment_1368k_2022 USD 1.368m. Supports alutiiq_guatemala_pnc_it_equipment_1368k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1368226.25; date_signed 2022-07-11.",
    investment_type="equipment_supply",
)

# === Cycle 1325 ===
row_doc(
    "marago_colombia_tumaco_fuel_system_1054k_2022",
    "infrastructure", "engineering_epc", "other",
    "Constructora Marago — Colombia Tumaco fuel system",
    "Colombia",
    "19 Aug 2022: Department of State awards contract to CONSTRUCTORA MARAGO S A S for Tumaco fuel system; obligated USD 1053682.36. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1053682.36", "2022-08-19", "2022", "", "",
    "TUMACO FUEL SYSTEM, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_marago_colombia_tumaco_fuel_system_1054k_2022",
    "TUMACO FUEL SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2255_1900_19AQMM21D0036_1900/",
    "Actor: CONSTRUCTORA MARAGO S A S — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1325",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F2255_1900_19AQMM21D0036_1900 (marago_colombia_tumaco_fuel_system_1054k_2022). Signed 2022-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2255_1900_19AQMM21D0036_1900/.",
    "USASpending: marago_colombia_tumaco_fuel_system_1054k_2022 USD 1.054m. Supports marago_colombia_tumaco_fuel_system_1054k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1053682.36; date_signed 2022-08-19.",
    investment_type="epc",
)

# === Cycle 1325 ===
row_doc(
    "eterna_honduras_sonaguera_fire_station_1031k_2024",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras Sonaguera fire station HAP 70375",
    "Honduras",
    "27 Sep 2024: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for HAP 70375 fire station in Sonaguera, Honduras; obligated USD 1031156.08. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1031156.08", "2024-09-27", "2024", "", "",
    "HAP 70375 FIRE STATION IN SONAGUERA, HONDURAS., Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_sonaguera_fire_station_1031k_2024",
    "HAP 70375 FIRE STATION IN SONAGUERA, HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0367_9700_W9127823D0073_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1325",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0367_9700_W9127823D0073_9700 (eterna_honduras_sonaguera_fire_station_1031k_2024). Signed 2024-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0367_9700_W9127823D0073_9700/.",
    "USASpending: eterna_honduras_sonaguera_fire_station_1031k_2024 USD 1.031m. Supports eterna_honduras_sonaguera_fire_station_1031k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1031156.08; date_signed 2024-09-27.",
    investment_type="epc",
)

# === Cycle 1325 ===
row_doc(
    "eterna_costarica_golfito_checkpoint_990k_2025",
    "infrastructure", "bridges_roads", "other",
    "Empresa Eterna — Costa Rica Golfito inspection checkpoint 35",
    "Costa Rica",
    "19 Aug 2025: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for inspection checkpoint 35, Gulfito, Costa Rica; obligated USD 989902.32. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "989902.32", "2025-08-19", "2025", "", "",
    "INSPECTION CHECKPOINT 35, GULFITO, COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_costarica_golfito_checkpoint_990k_2025",
    "INSPECTION CHECKPOINT 35, GULFITO, COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA115_9700_W9127823D0073_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1325",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA115_9700_W9127823D0073_9700 (eterna_costarica_golfito_checkpoint_990k_2025). Signed 2025-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA115_9700_W9127823D0073_9700/.",
    "USASpending: eterna_costarica_golfito_checkpoint_990k_2025 USD 0.990m. Supports eterna_costarica_golfito_checkpoint_990k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 989902.32; date_signed 2025-08-19.",
    investment_type="epc",
)

# === Cycle 1326 ===
row_doc(
    "alutiiq_mexico_high_impact_it_infra_938k_2022",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Mexico high-impact crimes IT infrastructure",
    "Mexico",
    "16 Nov 2022: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for IT infrastructure and integration services for high-impact crimes and anticorruption units INL Mexico City; obligated USD 938127.46. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "938127.46", "2022-11-16", "2022", "", "",
    "IT INFRASTRUCTURE AND INTEGRATION SERVICES FOR HIGH-IMPACT CRIMES AND ANTICORRUPTION UNITS FOR INL MEXICO CITY, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_high_impact_it_infra_938k_2022",
    "IT INFRASTRUCTURE AND INTEGRATION SERVICES FOR HIGH-IMPACT CRIMES AND ANTICORRUPTION UNITS FOR INL MEXICO CITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5001_1900_19AQMM20D0010_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1326",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMR23F5001_1900_19AQMM20D0010_1900 (alutiiq_mexico_high_impact_it_infra_938k_2022). Signed 2022-11-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5001_1900_19AQMM20D0010_1900/.",
    "USASpending: alutiiq_mexico_high_impact_it_infra_938k_2022 USD 0.938m. Supports alutiiq_mexico_high_impact_it_infra_938k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 938127.46; date_signed 2022-11-16.",
    investment_type="equipment_supply",
)

# === Cycle 1326 ===
row_doc(
    "alutiiq_mexico_satellite_sct_equipment_1979k_2016",
    "infrastructure", "building_materials", "us",
    "Alutiiq Technical Services — Mexico SCT satellite equipment",
    "Mexico",
    "18 May 2016: Department of State awards contract to ALUTIIQ TECHNICAL SERVICES LLC for satellite equipment to be donated to SCT Mexico; obligated USD 1979297.16. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1979297.16", "2016-05-18", "2016", "", "",
    "SATELLITE EQUIPMENT TO BE DONATED TO SCT MEXICO, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_satellite_sct_equipment_1979k_2016",
    "SATELLITE EQUIPMENT TO BE DONATED TO SCT MEXICO IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16M0014_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ TECHNICAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1326",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16M0014_1900_-NONE-_-NONE- (alutiiq_mexico_satellite_sct_equipment_1979k_2016). Signed 2016-05-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16M0014_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_satellite_sct_equipment_1979k_2016 USD 1.979m. Supports alutiiq_mexico_satellite_sct_equipment_1979k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1979297.16; date_signed 2016-05-18.",
    investment_type="equipment_supply",
)

# === Cycle 1326 ===
row_doc(
    "eterna_elsalvador_gse_storage_comalapa_948k_2019",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — El Salvador Comalapa GSE storage facility",
    "El Salvador",
    "30 Sep 2019: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for GSE storage facility and washrack oil/water separator addition CSL Comalapa; obligated USD 948386.95. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "948386.95", "2019-09-30", "2019", "", "",
    "GSE STORAGE FACILITY&WASHRACK OIL/WATER SEPARATOR ADDITION, CSL, COMALAPA, EL SALVADOR, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_elsalvador_gse_storage_comalapa_948k_2019",
    "GSE STORAGE FACILITY&WASHRACK OIL/WATER SEPARATOR ADDITION, CSL, COMALAPA, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0650_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1326",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0650_9700_W9127816D0102_9700 (eterna_elsalvador_gse_storage_comalapa_948k_2019). Signed 2019-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0650_9700_W9127816D0102_9700/.",
    "USASpending: eterna_elsalvador_gse_storage_comalapa_948k_2019 USD 0.948m. Supports eterna_elsalvador_gse_storage_comalapa_948k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 948386.95; date_signed 2019-09-30.",
    investment_type="epc",
)

# === Cycle 1326 ===
row_doc(
    "eterna_honduras_12plex_phase3_936k_2020",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras Soto Cano 12-plex housing phase III",
    "Honduras",
    "9 Sep 2020: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D/B 12 plex phase III SCAB Honduras; obligated USD 935776.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "935776.00", "2020-09-09", "2020", "", "",
    "D/B 12 PLEX PHASE III, SCAB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_12plex_phase3_936k_2020",
    "D/B 12 PLEX PHASE III, SCAB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0363_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1326",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127820F0363_9700_W9127816D0102_9700 (eterna_honduras_12plex_phase3_936k_2020). Signed 2020-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0363_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_12plex_phase3_936k_2020 USD 0.936m. Supports eterna_honduras_12plex_phase3_936k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 935776.0; date_signed 2020-09-09.",
    investment_type="epc",
)

# === Cycle 1326 ===
row_doc(
    "eterna_honduras_12plex_phase4_931k_2020",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras Soto Cano 12-plex housing phase IV",
    "Honduras",
    "14 Sep 2020: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for D/B 12 plex housing phase IV; obligated USD 930796.84. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "930796.84", "2020-09-14", "2020", "", "",
    "D/B 12 PLEX HOUSING PHASE IV, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_12plex_phase4_931k_2020",
    "D/B 12 PLEX HOUSING PHASE IV",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0377_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1326",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127820F0377_9700_W9127816D0102_9700 (eterna_honduras_12plex_phase4_931k_2020). Signed 2020-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0377_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_12plex_phase4_931k_2020 USD 0.931m. Supports eterna_honduras_12plex_phase4_931k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 930796.84; date_signed 2020-09-14.",
    investment_type="epc",
)

# === Cycle 1327 ===
row_doc(
    "alutiiq_mexico_telecom_satellite_equipment_1902k_2016",
    "infrastructure", "building_materials", "us",
    "Alutiiq Technical Services — Mexico IT telecommunication and satellite equipment",
    "Mexico",
    "29 Sep 2016: Department of State awards contract to ALUTIIQ TECHNICAL SERVICES LLC for IT telecommunication and satellite related equipment; obligated USD 1901726.22. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1901726.22", "2016-09-29", "2016", "", "",
    "IT TELECOMMUNICATION AND SATELLITE RELATED EQUIPMENT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_telecom_satellite_equipment_1902k_2016",
    "IT TELECOMMUNICATION AND SATELLITE RELATED EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0341_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ TECHNICAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1327",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16C0341_1900_-NONE-_-NONE- (alutiiq_mexico_telecom_satellite_equipment_1902k_2016). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0341_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_telecom_satellite_equipment_1902k_2016 USD 1.902m. Supports alutiiq_mexico_telecom_satellite_equipment_1902k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1901726.22; date_signed 2016-09-29.",
    investment_type="equipment_supply",
)

# === Cycle 1327 ===
row_doc(
    "alutiiq_mexico_biometric_76_workstations_562k_2018",
    "infrastructure", "building_materials", "us",
    "Alutiiq Information Management — Mexico 76 biometric workstations",
    "Mexico",
    "17 Apr 2018: Department of State awards contract to ALUTIIQ INFORMATION MANAGEMENT, LLC for purchase and install of equipment for 76 biometric workstations; obligated USD 561855.86. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "561855.86", "2018-04-17", "2018", "", "",
    "THE TASK ORDER PURCHASES AND INSTALLS ALL EQUIPMENT NECESSARY FOR 76 BIOMETRIC WORKSTATIONS., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_biometric_76_workstations_562k_2018",
    "THE TASK ORDER PURCHASES AND INSTALLS ALL EQUIPMENT NECESSARY FOR 76 BIOMETRIC WORKSTATIONS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1338_1900_19AQMM18D0038_1900/",
    "Actor: ALUTIIQ INFORMATION MANAGEMENT, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1327",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F1338_1900_19AQMM18D0038_1900 (alutiiq_mexico_biometric_76_workstations_562k_2018). Signed 2018-04-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1338_1900_19AQMM18D0038_1900/.",
    "USASpending: alutiiq_mexico_biometric_76_workstations_562k_2018 USD 0.562m. Supports alutiiq_mexico_biometric_76_workstations_562k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 561855.86; date_signed 2018-04-17.",
    investment_type="equipment_supply",
)

# === Cycle 1327 ===
row_doc(
    "eterna_panama_fiberglass_shop_907k_2022",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Panama fiberglass shop",
    "Panama",
    "28 Sep 2022: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for fiberglass shop task order; obligated USD 906510.67. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "906510.67", "2022-09-28", "2022", "", "",
    "FIBERGLASS SHOP TASK ORDER, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_panama_fiberglass_shop_907k_2022",
    "FIBERGLASS SHOP TASK ORDER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0427_9700_W9127821D0075_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1327",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0427_9700_W9127821D0075_9700 (eterna_panama_fiberglass_shop_907k_2022). Signed 2022-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0427_9700_W9127821D0075_9700/.",
    "USASpending: eterna_panama_fiberglass_shop_907k_2022 USD 0.907m. Supports eterna_panama_fiberglass_shop_907k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 906510.67; date_signed 2022-09-28.",
    investment_type="epc",
)

# === Cycle 1327 ===
row_doc(
    "eterna_colombia_guaviare_school_897k_2021",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Colombia San José del Guaviare school refurbishment HAP 39690",
    "Colombia",
    "16 Jun 2021: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for design and construction of HAP #39690 school refurbishment San Jose del Guaviare; obligated USD 896935.93. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "896935.93", "2021-06-16", "2021", "", "",
    "DESIGN AND CONSTRUCTION OF HAP #39690 SCHOOL REFURBISHMENT SAN JOSE DEL GUAVIARE, COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_colombia_guaviare_school_897k_2021",
    "DESIGN AND CONSTRUCTION OF HAP #39690 SCHOOL REFURBISHMENT SAN JOSE DEL GUAVIARE, COLOMBIA (CADD NO. SEA19015)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0206_9700_W9127817D0095_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1327",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0206_9700_W9127817D0095_9700 (eterna_colombia_guaviare_school_897k_2021). Signed 2021-06-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0206_9700_W9127817D0095_9700/.",
    "USASpending: eterna_colombia_guaviare_school_897k_2021 USD 0.897m. Supports eterna_colombia_guaviare_school_897k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 896935.93; date_signed 2021-06-16.",
    investment_type="epc",
)

# === Cycle 1327 ===
row_doc(
    "proyectos_colombia_mariquita_auditorium_866k_2022",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — Colombia Mariquita auditorium building",
    "Colombia",
    "19 Apr 2022: Department of State awards contract to PROYECTOS CIVILES S Y M LIMITADA for construction of auditorium building Mariquita; obligated USD 866048.77. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "866048.77", "2022-04-19", "2022", "", "",
    "CONSTRUCTION OF AUDITORIUM BUILDING MARIQUITA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_proyectos_colombia_mariquita_auditorium_866k_2022",
    "CONSTRUCTION OF AUDITORIUM BUILDING MARIQUITA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0627_1900_19AQMM21D0039_1900/",
    "Actor: PROYECTOS CIVILES S Y M LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1327",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F0627_1900_19AQMM21D0039_1900 (proyectos_colombia_mariquita_auditorium_866k_2022). Signed 2022-04-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0627_1900_19AQMM21D0039_1900/.",
    "USASpending: proyectos_colombia_mariquita_auditorium_866k_2022 USD 0.866m. Supports proyectos_colombia_mariquita_auditorium_866k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 866048.77; date_signed 2022-04-19.",
    investment_type="epc",
)

# === Cycle 1328 ===
row_doc(
    "alutiiq_mexico_conatrib_regional_judicial_17290k_2020",
    "infrastructure", "engineering_epc", "us",
    "Alutiiq Essential Services — Mexico CONATRIB regional judicial process build",
    "Mexico",
    "11 May 2020: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC to build CONATRIB regional judicial process; obligated USD 17290129.74. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "17290129.74", "2020-05-11", "2020", "", "",
    "REQUIREMENT TO BUILD CONATRIB REGIONAL JUDICIAL PROCESS., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_conatrib_regional_judicial_17290k_2020",
    "REQUIREMENT TO BUILD CONATRIB REGIONAL JUDICIAL PROCESS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0075_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1328",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20C0075_1900_-NONE-_-NONE- (alutiiq_mexico_conatrib_regional_judicial_17290k_2020). Signed 2020-05-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0075_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_conatrib_regional_judicial_17290k_2020 USD 17.290m. Supports alutiiq_mexico_conatrib_regional_judicial_17290k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 17290129.74; date_signed 2020-05-11.",
    investment_type="epc",
)

# === Cycle 1328 ===
row_doc(
    "alutiiq_mexico_prison_xray_machines_3119k_2020",
    "infrastructure", "engineering_epc", "us",
    "Alutiiq Solutions — Mexico prison x-ray machines",
    "Mexico",
    "9 Sep 2020: Department of State awards contract to ALUTIIQ SOLUTIONS, LLC for x-ray machines for Mexican prisons INL/Mexico; obligated USD 3119004.06. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3119004.06", "2020-09-09", "2020", "", "",
    "8(A) DIRECT AWARD FOR X-RAY MACHINES FOR MEXICAN PRISONS, INL/MEXICO., Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_prison_xray_machines_3119k_2020",
    "8(A) DIRECT AWARD FOR X-RAY MACHINES FOR MEXICAN PRISONS, INL/MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE20C0013_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ SOLUTIONS, LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1328",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE20C0013_1900_-NONE-_-NONE- (alutiiq_mexico_prison_xray_machines_3119k_2020). Signed 2020-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE20C0013_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_prison_xray_machines_3119k_2020 USD 3.119m. Supports alutiiq_mexico_prison_xray_machines_3119k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3119004.06; date_signed 2020-09-09.",
    investment_type="equipment_supply",
)

# === Cycle 1328 ===
row_doc(
    "eterna_honduras_octaplex_housing_865k_2017",
    "infrastructure", "building_materials", "other",
    "Empresa Eterna — Honduras octaplex housing",
    "Honduras",
    "20 Sep 2017: Department of State awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for octaplex housing; obligated USD 864938.07. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "864938.07", "2017-09-20", "2017", "", "",
    "IGF::OT::IGF OCTAPLEX HOUSING, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_eterna_honduras_octaplex_housing_865k_2017",
    "IGF::OT::IGF OCTAPLEX HOUSING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0278_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1328",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0278_9700_W9127816D0102_9700 (eterna_honduras_octaplex_housing_865k_2017). Signed 2017-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0278_9700_W9127816D0102_9700/.",
    "USASpending: eterna_honduras_octaplex_housing_865k_2017 USD 0.865m. Supports eterna_honduras_octaplex_housing_865k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 864938.07; date_signed 2017-09-20.",
    investment_type="epc",
)

# === Cycle 1328 ===
row_doc(
    "misc_colombia_jlsf_relocation_1079k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous Foreign Awardees — Colombia JLSF relocation",
    "Colombia",
    "24 Sep 2012: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for JLSF relocation; obligated USD 1078772.51. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1078772.51", "2012-09-24", "2012", "", "",
    "JLSF RELOCATION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_jlsf_relocation_1079k_2012",
    "JLSF RELOCATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0021_9700_-NONE-_-NONE-/",
    "Actor: MISCELLANEOUS FOREIGN AWARDEES — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1328",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12C0021_9700_-NONE-_-NONE- (misc_colombia_jlsf_relocation_1079k_2012). Signed 2012-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0021_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_jlsf_relocation_1079k_2012 USD 1.079m. Supports misc_colombia_jlsf_relocation_1079k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1078772.51; date_signed 2012-09-24.",
    investment_type="epc",
)

# === Cycle 1328 ===
row_doc(
    "misc_colombia_radar_towers_bsolano_pizarro_174k_2015",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous Foreign Awardees — Colombia Navy-Coast Guard radar towers BSolano-Pizarro",
    "Colombia",
    "22 Sep 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for Navy-Coast Guard 2nd phase radar towers BSolano-Pizarro; obligated USD 174376.18. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "174376.18", "2015-09-22", "2015", "", "",
    "NAVY-COASTGUARD-2ND PHASE RADARS TOWERS BSOLANO-PIZARRO, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_radar_towers_bsolano_pizarro_174k_2015",
    "NAVY-COASTGUARD-2ND PHASE RADARS TOWERS BSOLANO-PIZARRO 3.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15015C0006_1900_-NONE-_-NONE-/",
    "Actor: MISCELLANEOUS FOREIGN AWARDEES — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1328",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15015C0006_1900_-NONE-_-NONE- (misc_colombia_radar_towers_bsolano_pizarro_174k_2015). Signed 2015-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15015C0006_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_radar_towers_bsolano_pizarro_174k_2015 USD 0.174m. Supports misc_colombia_radar_towers_bsolano_pizarro_174k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 174376.18; date_signed 2015-09-22.",
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
