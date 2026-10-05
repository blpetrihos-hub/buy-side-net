#!/usr/bin/env python3
"""Cycles 1286–1291: USASpending LatAm CapEx (NIKA/Mesan fit-outs + Bendig/Fabio + residual other).

Seeds: 20262286–20262291. Thin top-up dry.
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

# === Cycle 1286 ===
row_doc(
    "nika_jamaica_powell_plaza_doors_windows_4156k_2012",
    "infrastructure", "building_materials", "us",
    "NIKA — Jamaica Powell Plaza exterior doors and windows replacement",
    "Jamaica",
    "29 Sep 2012: Department of State awards contract to NIKA & EMR JOINT VENTURE for remove and replace all exterior doors and windows at Powell Plaza apartments (PoP Jamaica); obligated USD 4156279.97. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "4156279.97", "2012-09-29", "2012", "", "",
    "REMOVE AND REPLACE ALL EXTERIOR DOORS AND WINDOWS AT POWELL PLAZA APARTMENT COMPLEX., Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_nika_jamaica_powell_plaza_doors_windows_4156k_2012",
    "REMOVE AND REPLACE ALL EXTERIOR DOORS AND WINDOWS AT POWELL PLAZA APARTMENT COMPLEX.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F4664_1900_SAQMMA08D0020_1900/",
    "Actor: NIKA & EMR JOINT VENTURE (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1286",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F4664_1900_SAQMMA08D0020_1900 (nika_jamaica_powell_plaza_doors_windows_4156k_2012). Signed 2012-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F4664_1900_SAQMMA08D0020_1900/.",
    "USASpending: nika_jamaica_powell_plaza_doors_windows_4156k_2012 USD 4.156m. Supports nika_jamaica_powell_plaza_doors_windows_4156k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4156279.97; date_signed 2012-09-29.",
    investment_type="epc",
)

# === Cycle 1286 ===
row_doc(
    "mesan_mexico_office_buildout_2166k_2010",
    "infrastructure", "building_materials", "us",
    "Mesan-Martinez — Mexico office build-out",
    "Mexico",
    "22 Feb 2010: Department of State awards contract to MESAN-MARTINEZ JOINT VENTURE LLP for office build-out (PoP Mexico); obligated USD 2166160. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2166160", "2010-02-22", "2010", "", "",
    "OFFICE BUILD-OUT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mesan_mexico_office_buildout_2166k_2010",
    "OFFICE BUILD-OUT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F0599_1900_SAQMMA08D0015_1900/",
    "Actor: MESAN-MARTINEZ JOINT VENTURE LLP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1286",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F0599_1900_SAQMMA08D0015_1900 (mesan_mexico_office_buildout_2166k_2010). Signed 2010-02-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F0599_1900_SAQMMA08D0015_1900/.",
    "USASpending: mesan_mexico_office_buildout_2166k_2010 USD 2.166m. Supports mesan_mexico_office_buildout_2166k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2166160.0; date_signed 2010-02-22.",
    investment_type="epc",
)

# === Cycle 1286 ===
row_doc(
    "industrias_bendig_costarica_pococi_training_pool_738k_2022",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — Costa Rica Pococí training pool",
    "Costa Rica",
    "30 Sep 2022: Department of State awards contract to INDUSTRIAS BENDIG SA for training pool Pococí Limón (PoP Costa Rica); obligated USD 738144.83. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "738144.83", "2022-09-30", "2022", "", "",
    "TRAINING POOL, POCOCI, LIMON, COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_industrias_bendig_costarica_pococi_training_pool_738k_2022",
    "TRAINING POOL, POCOCI, LIMON, COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0153_1900_-NONE-_-NONE-/",
    "Actor: INDUSTRIAS BENDIG SA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1286",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22C0153_1900_-NONE-_-NONE- (industrias_bendig_costarica_pococi_training_pool_738k_2022). Signed 2022-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0153_1900_-NONE-_-NONE-/.",
    "USASpending: industrias_bendig_costarica_pococi_training_pool_738k_2022 USD 0.738m. Supports industrias_bendig_costarica_pococi_training_pool_738k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 738144.83; date_signed 2022-09-30.",
    investment_type="epc",
)

# === Cycle 1286 ===
row_doc(
    "industrias_bendig_costarica_murcielago_barracks_732k_2017",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — Costa Rica Murciélago barracks remodeling",
    "Costa Rica",
    "25 Jan 2017: Department of State awards contract to INDUSTRIAS BENDIG SA for remodeling CR barracks Murcielago (PoP Costa Rica); obligated USD 732990. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "732990", "2017-01-25", "2017", "", "",
    "REMODELING CR BARRACKS MURCILAGO, COSTA RICA IGF::OT::IGF, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_industrias_bendig_costarica_murcielago_barracks_732k_2017",
    "REMODELING CR BARRACKS MURCILAGO, COSTA RICA IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0089_1900_-NONE-_-NONE-/",
    "Actor: INDUSTRIAS BENDIG SA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1286",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0089_1900_-NONE-_-NONE- (industrias_bendig_costarica_murcielago_barracks_732k_2017). Signed 2017-01-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0089_1900_-NONE-_-NONE-/.",
    "USASpending: industrias_bendig_costarica_murcielago_barracks_732k_2017 USD 0.733m. Supports industrias_bendig_costarica_murcielago_barracks_732k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 732990.0; date_signed 2017-01-25.",
    investment_type="epc",
)

# === Cycle 1286 ===
row_doc(
    "fabio_garzon_colombia_construction_676k_2011",
    "infrastructure", "building_materials", "other",
    "Fabio Garzón Daza — Colombia construction",
    "Colombia",
    "2 Sep 2011: Department of Defense awards contract to FABIO GARZON DAZA for construction (PoP Colombia); obligated USD 676182.56. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "676182.56", "2011-09-02", "2011", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fabio_garzon_colombia_construction_676k_2011",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0023_9700_-NONE-_-NONE-/",
    "Actor: FABIO GARZON DAZA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1286",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11C0023_9700_-NONE-_-NONE- (fabio_garzon_colombia_construction_676k_2011). Signed 2011-09-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0023_9700_-NONE-_-NONE-/.",
    "USASpending: fabio_garzon_colombia_construction_676k_2011 USD 0.676m. Supports fabio_garzon_colombia_construction_676k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 676182.56; date_signed 2011-09-02.",
    investment_type="epc",
)

# === Cycle 1287 ===
row_doc(
    "mesan_mexico_city_nas_lease_fitout_2103k_2012",
    "infrastructure", "building_materials", "us",
    "Mesan-Martinez — Mexico City NAS lease fit-out",
    "Mexico",
    "8 Jun 2012: Department of State awards contract to MESAN-MARTINEZ JOINT VENTURE LLP for Mexico City NAS lease fit out (PoP Mexico); obligated USD 2103647.83. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2103647.83", "2012-06-08", "2012", "", "",
    "MEXICO CITY NAS LEASE FIT OUT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mesan_mexico_city_nas_lease_fitout_2103k_2012",
    "MEXICO CITY NAS LEASE FIT OUT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1990_1900_SAQMMA08D0015_1900/",
    "Actor: MESAN-MARTINEZ JOINT VENTURE LLP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1287",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F1990_1900_SAQMMA08D0015_1900 (mesan_mexico_city_nas_lease_fitout_2103k_2012). Signed 2012-06-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1990_1900_SAQMMA08D0015_1900/.",
    "USASpending: mesan_mexico_city_nas_lease_fitout_2103k_2012 USD 2.104m. Supports mesan_mexico_city_nas_lease_fitout_2103k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2103647.83; date_signed 2012-06-08.",
    investment_type="epc",
)

# === Cycle 1287 ===
row_doc(
    "mesan_trinidad_port_of_spain_lease_fitout_2072k_2010",
    "infrastructure", "building_materials", "us",
    "Mesan-Martinez — Port of Spain lease fit-out",
    "Trinidad and Tobago",
    "30 Sep 2010: Department of State awards contract to MESAN-MARTINEZ JOINT VENTURE LLP for Port of Spain lease fit out (PoP Trinidad and Tobago); obligated USD 2072515. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2072515", "2010-09-30", "2010", "", "",
    "PORT OF SPAIN LEASE FIT OUT, Trinidad and Tobago (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mesan_trinidad_port_of_spain_lease_fitout_2072k_2010",
    "PORT OF SPAIN LEASE FIT OUT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F5299_1900_SAQMMA08D0015_1900/",
    "Actor: MESAN-MARTINEZ JOINT VENTURE LLP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1287",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F5299_1900_SAQMMA08D0015_1900 (mesan_trinidad_port_of_spain_lease_fitout_2072k_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F5299_1900_SAQMMA08D0015_1900/.",
    "USASpending: mesan_trinidad_port_of_spain_lease_fitout_2072k_2010 USD 2.073m. Supports mesan_trinidad_port_of_spain_lease_fitout_2072k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2072515.0; date_signed 2010-09-30.",
    investment_type="epc",
)

# === Cycle 1287 ===
row_doc(
    "fabio_garzon_colombia_fence_repair_376k_2012",
    "infrastructure", "building_materials", "other",
    "Fabio Garzón Daza — Colombia phase 1 perimeter fence repair",
    "Colombia",
    "28 Aug 2012: Department of Defense awards contract to FABIO GARZON DAZA for phase 1 perimeter fence repair (PoP Colombia); obligated USD 376739.44. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "376739.44", "2012-08-28", "2012", "", "",
    "PHASE 1 PERIMETER FENCE REPAIR, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fabio_garzon_colombia_fence_repair_376k_2012",
    "PHASE 1 PERIMETER FENCE REPAIR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0013_9700_-NONE-_-NONE-/",
    "Actor: FABIO GARZON DAZA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1287",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12C0013_9700_-NONE-_-NONE- (fabio_garzon_colombia_fence_repair_376k_2012). Signed 2012-08-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0013_9700_-NONE-_-NONE-/.",
    "USASpending: fabio_garzon_colombia_fence_repair_376k_2012 USD 0.377m. Supports fabio_garzon_colombia_fence_repair_376k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 376739.44; date_signed 2012-08-28.",
    investment_type="epc",
)

# === Cycle 1287 ===
row_doc(
    "misc_uruguay_cmr_roof_replacement_244k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Uruguay CMR roof replacement",
    "Uruguay",
    "29 Sep 2011: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FM replace CMR roof (PoP Uruguay); obligated USD 244416.44. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "244416.44", "2011-09-29", "2011", "", "",
    "FM - REPLACE CMR'S ROOF., Uruguay (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_uruguay_cmr_roof_replacement_244k_2011",
    "FM - REPLACE CMR'S ROOF.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60011C0502_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1287",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SUY60011C0502_1900_-NONE-_-NONE- (misc_uruguay_cmr_roof_replacement_244k_2011). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60011C0502_1900_-NONE-_-NONE-/.",
    "USASpending: misc_uruguay_cmr_roof_replacement_244k_2011 USD 0.244m. Supports misc_uruguay_cmr_roof_replacement_244k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 244416.44; date_signed 2011-09-29.",
    investment_type="epc",
)

# === Cycle 1287 ===
row_doc(
    "fabio_garzon_colombia_apiay_vpc_239k_2013",
    "infrastructure", "building_materials", "other",
    "Fabio Garzón Daza — Colombia Apiay visitor processing center",
    "Colombia",
    "25 Jul 2013: Department of Defense awards contract to FABIO GARZON DAZA for Apiay visitor processing center (PoP Colombia); obligated USD 239558.24. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "239558.24", "2013-07-25", "2013", "", "",
    "APIAY VISITOR PROCESSING CENTER, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fabio_garzon_colombia_apiay_vpc_239k_2013",
    "APIAY VISITOR PROCESSING CENTER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13C0014_9700_-NONE-_-NONE-/",
    "Actor: FABIO GARZON DAZA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1287",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT13C0014_9700_-NONE-_-NONE- (fabio_garzon_colombia_apiay_vpc_239k_2013). Signed 2013-07-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13C0014_9700_-NONE-_-NONE-/.",
    "USASpending: fabio_garzon_colombia_apiay_vpc_239k_2013 USD 0.240m. Supports fabio_garzon_colombia_apiay_vpc_239k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 239558.24; date_signed 2013-07-25.",
    investment_type="epc",
)

# === Cycle 1288 ===
row_doc(
    "nika_brazil_rio_lighting_switchboard_1060k_2012",
    "energy", "power_plants_grid", "us",
    "NIKA — Rio de Janeiro consulate main lighting and switchboard",
    "Brazil",
    "28 Sep 2012: Department of State awards contract to NIKA & EMR JOINT VENTURE for U.S. Consulate Rio main lighting and switchboard (PoP Brazil); obligated USD 1060947. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1060947", "2012-09-28", "2012", "", "",
    "RIO DE JANEIRO, BRAZIL.  U.S. CONSULATE.  MAIN LIGHTING AND SWITCHBOARDS REPLACEMENT., Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_nika_brazil_rio_lighting_switchboard_1060k_2012",
    "RIO DE JANEIRO, BRAZIL.  U.S. CONSULATE.  MAIN LIGHTING AND SWITCHBOARDS REPLACEMENT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F3671_1900_SAQMMA08D0020_1900/",
    "Actor: NIKA & EMR JOINT VENTURE (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1288",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F3671_1900_SAQMMA08D0020_1900 (nika_brazil_rio_lighting_switchboard_1060k_2012). Signed 2012-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F3671_1900_SAQMMA08D0020_1900/.",
    "USASpending: nika_brazil_rio_lighting_switchboard_1060k_2012 USD 1.061m. Supports nika_brazil_rio_lighting_switchboard_1060k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1060947.0; date_signed 2012-09-28.",
    investment_type="epc",
)

# === Cycle 1288 ===
row_doc(
    "ics_brazil_drop_arm_barriers_666k_2017",
    "infrastructure", "building_materials", "us",
    "International Construction Services — Brazil drop arm barriers removal/replacement",
    "Brazil",
    "1 Jun 2017: Department of State awards contract to HORIZON CONSTRUCTION GROUP\INTERNATIONAL CONSTRUCTION SERVICES JV, LLC for remove two existing drop arm barriers (PoP Brazil); obligated USD 666222. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "666222", "2017-06-01", "2017", "", "",
    "THE CONTRACTOR SHALL REMOVE TWO (2) EXISTING DROP ARM BARRIERS FROM THE SERVICE ROAD IN FRONT OF THE US CONSUL, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_ics_brazil_drop_arm_barriers_666k_2017",
    "THE CONTRACTOR SHALL REMOVE TWO (2) EXISTING DROP ARM BARRIERS FROM THE SERVICE ROAD IN FRONT OF THE US CONSULATE GENERAL AND REPLACE THEM WITH TWO (2) NEW DS APPROVED DROP ARM BARRIERS THAT MEET OBO REQUIREMENTS.  IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F1795_1900_SAQMMA14D0056_1900/",
    "Actor: HORIZON CONSTRUCTION GROUP\INTERNATIONAL CONSTRUCTION SERVICES JV, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1288",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17F1795_1900_SAQMMA14D0056_1900 (ics_brazil_drop_arm_barriers_666k_2017). Signed 2017-06-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F1795_1900_SAQMMA14D0056_1900/.",
    "USASpending: ics_brazil_drop_arm_barriers_666k_2017 USD 0.666m. Supports ics_brazil_drop_arm_barriers_666k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 666222.0; date_signed 2017-06-01.",
    investment_type="epc",
)

# === Cycle 1288 ===
row_doc(
    "norma_gutierrez_mexico_residential_restoration_194k_2024",
    "infrastructure", "building_materials", "other",
    "Norma Isabel Gutiérrez López — Mexico residential restoration",
    "Mexico",
    "27 Sep 2024: Department of State awards contract to NORMA ISABEL GUTIERREZ LOPEZ for residential restoration (PoP Mexico); obligated USD 194266.51. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "194266.51", "2024-09-27", "2024", "", "",
    "RESIDENTIAL RESTORATION, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_norma_gutierrez_mexico_residential_restoration_194k_2024",
    "RESIDENTIAL RESTORATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5324C0010_1900_-NONE-_-NONE-/",
    "Actor: NORMA ISABEL GUTIERREZ LOPEZ — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1288",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5324C0010_1900_-NONE-_-NONE- (norma_gutierrez_mexico_residential_restoration_194k_2024). Signed 2024-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5324C0010_1900_-NONE-_-NONE-/.",
    "USASpending: norma_gutierrez_mexico_residential_restoration_194k_2024 USD 0.194m. Supports norma_gutierrez_mexico_residential_restoration_194k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 194266.51; date_signed 2024-09-27.",
    investment_type="epc",
)

# === Cycle 1288 ===
row_doc(
    "norma_gutierrez_mexico_kitchen_bath_restoration_190k_2024",
    "infrastructure", "building_materials", "other",
    "Norma Isabel Gutiérrez López — Mexico kitchen and bathrooms restoration",
    "Mexico",
    "6 Sep 2024: Department of State awards contract to NORMA ISABEL GUTIERREZ LOPEZ for kitchen and bathrooms restoration (PoP Mexico); obligated USD 190998.07. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "190998.07", "2024-09-06", "2024", "", "",
    "KITCHEN & BATHROOMS RESTORATION, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_norma_gutierrez_mexico_kitchen_bath_restoration_190k_2024",
    "KITCHEN & BATHROOMS RESTORATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5324C0009_1900_-NONE-_-NONE-/",
    "Actor: NORMA ISABEL GUTIERREZ LOPEZ — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1288",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5324C0009_1900_-NONE-_-NONE- (norma_gutierrez_mexico_kitchen_bath_restoration_190k_2024). Signed 2024-09-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5324C0009_1900_-NONE-_-NONE-/.",
    "USASpending: norma_gutierrez_mexico_kitchen_bath_restoration_190k_2024 USD 0.191m. Supports norma_gutierrez_mexico_kitchen_bath_restoration_190k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 190998.07; date_signed 2024-09-06.",
    investment_type="epc",
)

# === Cycle 1288 ===
row_doc(
    "misc_colombia_construct_solar_plant_185k_2013",
    "energy", "solar", "other",
    "Miscellaneous foreign awardees — Colombia construct solar plant",
    "Colombia",
    "28 Aug 2013: Department of Defense awards contract to MISCELLANEOUS FOREIGN AWARDEES for construct solar plant (PoP Colombia); obligated USD 185785.78. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "185785.78", "2013-08-28", "2013", "", "",
    "CONSTRUCT SOLAR PLANT, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_construct_solar_plant_185k_2013",
    "CONSTRUCT SOLAR PLANT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13C0016_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle solar.",
    "hunt_cycle1288",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT13C0016_9700_-NONE-_-NONE- (misc_colombia_construct_solar_plant_185k_2013). Signed 2013-08-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13C0016_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_construct_solar_plant_185k_2013 USD 0.186m. Supports misc_colombia_construct_solar_plant_185k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 185785.78; date_signed 2013-08-28.",
    investment_type="epc",
)

# === Cycle 1289 ===
row_doc(
    "nika_costa_rica_ahu_install_560k_2010",
    "energy", "power_plants_grid", "us",
    "NIKA — Costa Rica air handling unit installation phase III",
    "Costa Rica",
    "27 Aug 2010: Department of State awards contract to NIKA & EMR JOINT VENTURE for phase III construction services to install air handling unit (PoP Costa Rica); obligated USD 560907. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "560907", "2010-08-27", "2010", "", "",
    "PHASE III - CONSTRUCTION SERVICES TO INSTALL AIR HANDLING UNIT IN COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_nika_costa_rica_ahu_install_560k_2010",
    "PHASE III - CONSTRUCTION SERVICES TO INSTALL AIR HANDLING UNIT IN COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F3326_1900_SAQMMA08D0020_1900/",
    "Actor: NIKA & EMR JOINT VENTURE (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1289",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F3326_1900_SAQMMA08D0020_1900 (nika_costa_rica_ahu_install_560k_2010). Signed 2010-08-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F3326_1900_SAQMMA08D0020_1900/.",
    "USASpending: nika_costa_rica_ahu_install_560k_2010 USD 0.561m. Supports nika_costa_rica_ahu_install_560k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 560907.0; date_signed 2010-08-27.",
    investment_type="epc",
)

# === Cycle 1289 ===
row_doc(
    "nika_mexico_guadalajara_office_fitout_500k_2011",
    "infrastructure", "building_materials", "us",
    "NIKA — Guadalajara consulate office fit-out",
    "Mexico",
    "9 Jun 2011: Department of State awards contract to NIKA & EMR JOINT VENTURE for office fit-out for U.S. Consulate Guadalajara (PoP Mexico); obligated USD 500000. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "500000", "2011-06-09", "2011", "", "",
    "TASK ORDER FOR OFFICE FIT-OUT FOR U.S. CONSULATE GUADALAJARA FOR PAG, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_nika_mexico_guadalajara_office_fitout_500k_2011",
    "TASK ORDER FOR OFFICE FIT-OUT FOR U.S. CONSULATE GUADALAJARA FOR PAG",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F1795_1900_SAQMMA08D0020_1900/",
    "Actor: NIKA & EMR JOINT VENTURE (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1289",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F1795_1900_SAQMMA08D0020_1900 (nika_mexico_guadalajara_office_fitout_500k_2011). Signed 2011-06-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F1795_1900_SAQMMA08D0020_1900/.",
    "USASpending: nika_mexico_guadalajara_office_fitout_500k_2011 USD 0.500m. Supports nika_mexico_guadalajara_office_fitout_500k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 500000.0; date_signed 2011-06-09.",
    investment_type="epc",
)

# === Cycle 1289 ===
row_doc(
    "misc_belize_roof_truss_school_medical_162k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Belize roof truss system for school and medical buildings",
    "Belize",
    "22 Jan 2014: Department of Defense awards contract to MISCELLANEOUS FOREIGN AWARDEES for roof truss system for school and medical buildings (PoP Belize); obligated USD 162031.33. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "162031.33", "2014-01-22", "2014", "", "",
    "ROOF TRUSS SYSTEM FOR SCHOOL&MEDICAL BUILDINGS, Belize (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_belize_roof_truss_school_medical_162k_2014",
    "ROOF TRUSS SYSTEM FOR SCHOOL&MEDICAL BUILDINGS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470414M0002_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1289",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA470414M0002_9700_-NONE-_-NONE- (misc_belize_roof_truss_school_medical_162k_2014). Signed 2014-01-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470414M0002_9700_-NONE-_-NONE-/.",
    "USASpending: misc_belize_roof_truss_school_medical_162k_2014 USD 0.162m. Supports misc_belize_roof_truss_school_medical_162k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 162031.33; date_signed 2014-01-22.",
    investment_type="epc",
)

# === Cycle 1289 ===
row_doc(
    "misc_mexico_puebla_solar_lights_158k_2012",
    "energy", "solar", "other",
    "Miscellaneous foreign awardees — Mexico Puebla solar lights",
    "Mexico",
    "22 Mar 2012: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for solar lights to support Puebla (PoP Mexico); obligated USD 158510.39. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "158510.39", "2012-03-22", "2012", "", "",
    "IN241MX72 2R32 SOLAR LIGHTS TO SUPPORT PUEBLA, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_puebla_solar_lights_158k_2012",
    "IN241MX72 2R32 SOLAR LIGHTS TO SUPPORT PUEBLA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M0657_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle solar.",
    "hunt_cycle1289",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53012M0657_1900_-NONE-_-NONE- (misc_mexico_puebla_solar_lights_158k_2012). Signed 2012-03-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M0657_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_puebla_solar_lights_158k_2012 USD 0.159m. Supports misc_mexico_puebla_solar_lights_158k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 158510.39; date_signed 2012-03-22.",
    investment_type="equipment_supply",
)

# === Cycle 1289 ===
row_doc(
    "misc_brazil_tcmr_cctv_36k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil new TCMR CCTV",
    "Brazil",
    "18 Dec 2019: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for RSO CCTV for new TCMR Chacara 46 (PoP Brazil); obligated USD 36789.86. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "36789.86", "2019-12-18", "2019", "", "",
    "RSO - CCTV FOR NEW TCMR - QI 05 CHACARA 46, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_tcmr_cctv_36k_2020",
    "RSO - CCTV FOR NEW TCMR - QI 05 CHACARA 46",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0036_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1289",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2520P0036_1900_-NONE-_-NONE- (misc_brazil_tcmr_cctv_36k_2020). Signed 2019-12-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0036_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_tcmr_cctv_36k_2020 USD 0.037m. Supports misc_brazil_tcmr_cctv_36k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 36789.86; date_signed 2019-12-18.",
    investment_type="equipment_supply",
)

# === Cycle 1290 ===
row_doc(
    "mesan_jamaica_kingston_ice_fitout_443k_2010",
    "infrastructure", "building_materials", "us",
    "Mesan-Martinez — Kingston ICE fit-out",
    "Jamaica",
    "29 Sep 2010: Department of State awards contract to MESAN-MARTINEZ JOINT VENTURE LLP for Kingston ICE fit out (PoP Jamaica); obligated USD 443315. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "443315", "2010-09-29", "2010", "", "",
    "TAS::19 0535 000::TAS KINGSTON ICE FIT OUT, Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mesan_jamaica_kingston_ice_fitout_443k_2010",
    "TAS::19 0535 000::TAS KINGSTON ICE FIT OUT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F4926_1900_SAQMMA08D0015_1900/",
    "Actor: MESAN-MARTINEZ JOINT VENTURE LLP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1290",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F4926_1900_SAQMMA08D0015_1900 (mesan_jamaica_kingston_ice_fitout_443k_2010). Signed 2010-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F4926_1900_SAQMMA08D0015_1900/.",
    "USASpending: mesan_jamaica_kingston_ice_fitout_443k_2010 USD 0.443m. Supports mesan_jamaica_kingston_ice_fitout_443k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 443315.0; date_signed 2010-09-29.",
    investment_type="epc",
)

# === Cycle 1290 ===
row_doc(
    "human_tech_colombia_rigid_shelters_accessories_387k_2023",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Colombia rigid shelters and accessories",
    "Colombia",
    "26 Jun 2023: Department of State awards contract to HUMAN TECHNOLOGIES CORP for purchase order for rigid shelters and accessories (PoP Colombia); obligated USD 387472.60. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "387472.60", "2023-06-26", "2023", "", "",
    "PURCHASE ORDER FOR RIGID SHELTERS AND ACCESSORIES, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_colombia_rigid_shelters_accessories_387k_2023",
    "PURCHASE ORDER FOR RIGID SHELTERS AND ACCESSORIES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE23F0036_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1290",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE23F0036_1900_19AQMM21D0007_1900 (human_tech_colombia_rigid_shelters_accessories_387k_2023). Signed 2023-06-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE23F0036_1900_19AQMM21D0007_1900/.",
    "USASpending: human_tech_colombia_rigid_shelters_accessories_387k_2023 USD 0.387m. Supports human_tech_colombia_rigid_shelters_accessories_387k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 387472.6; date_signed 2023-06-26.",
    investment_type="equipment_supply",
)

# === Cycle 1290 ===
row_doc(
    "misc_colombia_ctg_ebo_fire_alarm_22k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia CTG EBO fire alarm system upgrade",
    "Colombia",
    "26 Sep 2025: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for CTG EBO existing fire alarm system upgrade (PoP Colombia); obligated USD 22061.99. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "22061.99", "2025-09-26", "2025", "", "",
    "PR15553370: CTG EBO EXISTING FIRE ALARM SYSTEM  UPGRADE-7945 X..., Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_ctg_ebo_fire_alarm_22k_2025",
    "PR15553370: CTG EBO EXISTING FIRE ALARM SYSTEM  UPGRADE-7945 X...",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02025P1777_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1290",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02025P1777_1900_-NONE-_-NONE- (misc_colombia_ctg_ebo_fire_alarm_22k_2025). Signed 2025-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02025P1777_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_ctg_ebo_fire_alarm_22k_2025 USD 0.022m. Supports misc_colombia_ctg_ebo_fire_alarm_22k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 22061.99; date_signed 2025-09-26.",
    investment_type="epc",
)

# === Cycle 1290 ===
row_doc(
    "misc_mexico_chancery_fire_alarm_panel_21k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico chancery fire alarm panel replacement",
    "Mexico",
    "14 Aug 2019: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for chancery fire alarm panel replacement (PoP Mexico); obligated USD 21519.16. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "21519.16", "2019-08-14", "2019", "", "",
    "MX-FAC-OBO-CHANCERY FIRE ALARM PANEL REPLACEMENT-FY19 URGENT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_chancery_fire_alarm_panel_21k_2019",
    "MX-FAC-OBO-CHANCERY FIRE ALARM PANEL REPLACEMENT-FY19 URGENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319P1209_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1290",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5319P1209_1900_-NONE-_-NONE- (misc_mexico_chancery_fire_alarm_panel_21k_2019). Signed 2019-08-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319P1209_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_chancery_fire_alarm_panel_21k_2019 USD 0.022m. Supports misc_mexico_chancery_fire_alarm_panel_21k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 21519.16; date_signed 2019-08-14.",
    investment_type="equipment_supply",
)

# === Cycle 1290 ===
row_doc(
    "misc_mexico_chancery_fire_alarm_final_21k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico chancery fire alarm system final payment",
    "Mexico",
    "27 Apr 2022: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for chancery fire alarm system final payment (PoP Mexico); obligated USD 21795.76. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "21795.76", "2022-04-27", "2022", "", "",
    "MEX-FAC-OBO-M&R CHANCERY FIRE ALARM SYSTEM FINAL PROGRAMMING, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_chancery_fire_alarm_final_21k_2022",
    "MEX-FAC-OBO-M&R CHANCERY FIRE ALARM SYSTEM FINAL PROGRAMMING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5322P0734_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1290",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5322P0734_1900_-NONE-_-NONE- (misc_mexico_chancery_fire_alarm_final_21k_2022). Signed 2022-04-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5322P0734_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_chancery_fire_alarm_final_21k_2022 USD 0.022m. Supports misc_mexico_chancery_fire_alarm_final_21k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 21795.76; date_signed 2022-04-27.",
    investment_type="epc",
)

# === Cycle 1291 ===
row_doc(
    "hollingsworth_haiti_terrier_rouge_design_166k_2015",
    "infrastructure", "engineering_epc", "us",
    "Hollingsworth-Pack — Haiti Terrier Rouge commissariat 100% design",
    "Haiti",
    "6 Aug 2015: Department of State awards contract to HOLLINGSWORTH-PACK CORPORATION for 100% design Terrier Rouge commissariat (PoP Haiti); obligated USD 166790. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "166790", "2015-08-06", "2015", "", "",
    "IGF::OT::IGF 100% DESIGN TERRIER ROUGE COMMISSARIAT, HAITI, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hollingsworth_haiti_terrier_rouge_design_166k_2015",
    "IGF::OT::IGF 100% DESIGN TERRIER ROUGE COMMISSARIAT, HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15C0188_1900_-NONE-_-NONE-/",
    "Actor: HOLLINGSWORTH-PACK CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1291",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15C0188_1900_-NONE-_-NONE- (hollingsworth_haiti_terrier_rouge_design_166k_2015). Signed 2015-08-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15C0188_1900_-NONE-_-NONE-/.",
    "USASpending: hollingsworth_haiti_terrier_rouge_design_166k_2015 USD 0.167m. Supports hollingsworth_haiti_terrier_rouge_design_166k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 166790.0; date_signed 2015-08-06.",
    investment_type="epc",
)

# === Cycle 1291 ===
row_doc(
    "kva_honduras_tegucigalpa_electrical_105k_2015",
    "energy", "power_plants_grid", "us",
    "KVA Electric — Tegucigalpa electrical work",
    "Honduras",
    "7 May 2015: Department of State awards contract to KVA ELECTRIC INC for electrical work Tegucigalpa (PoP Honduras); obligated USD 105457.88. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "105457.88", "2015-05-07", "2015", "", "",
    "ELECTRICAL WORK TEGUCIGALPA, HONDURAS IGF::CL::IGF, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_kva_honduras_tegucigalpa_electrical_105k_2015",
    "ELECTRICAL WORK TEGUCIGALPA, HONDURAS IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F2010_1900_SAQMMA13D0022_1900/",
    "Actor: KVA ELECTRIC INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1291",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15F2010_1900_SAQMMA13D0022_1900 (kva_honduras_tegucigalpa_electrical_105k_2015). Signed 2015-05-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F2010_1900_SAQMMA13D0022_1900/.",
    "USASpending: kva_honduras_tegucigalpa_electrical_105k_2015 USD 0.105m. Supports kva_honduras_tegucigalpa_electrical_105k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 105457.88; date_signed 2015-05-07.",
    investment_type="epc",
)

# === Cycle 1291 ===
row_doc(
    "misc_haiti_electrical_materials_299k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Haiti electrical materials purchase order",
    "Haiti",
    "4 Apr 2011: Agency for International Development awards contract to MISCELLANEOUS FOREIGN AWARDEES for firm fixed purchase order for electrical materials (PoP Haiti); obligated USD 299679.72. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "299679.72", "2011-04-04", "2011", "", "",
    "THIS IS A FIRM FIXED PURCHASE ORDER FOR ELECTRICAL MATERIALS FOR MAKE READY AT USAID RESIDENCE.TAS::72 1000::T, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_electrical_materials_299k_2011",
    "THIS IS A FIRM FIXED PURCHASE ORDER FOR ELECTRICAL MATERIALS FOR MAKE READY AT USAID RESIDENCE.TAS::72 1000::TAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521O001100120_7200_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1291",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521O001100120_7200_-NONE-_-NONE- (misc_haiti_electrical_materials_299k_2011). Signed 2011-04-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521O001100120_7200_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_electrical_materials_299k_2011 USD 0.300m. Supports misc_haiti_electrical_materials_299k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 299679.72; date_signed 2011-04-04.",
    investment_type="equipment_supply",
)

# === Cycle 1291 ===
row_doc(
    "misc_venezuela_cctv_electrical_material_39k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Venezuela electrical material for CCTV project",
    "Venezuela",
    "21 Sep 2021: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for electrical material for CCTV project (PoP Venezuela); obligated USD 39406.70. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "39406.70", "2021-09-21", "2021", "", "",
    "ELECTRICAL MATERIAL FOR CCTV PROJECT, Venezuela (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_venezuela_cctv_electrical_material_39k_2021",
    "ELECTRICAL MATERIAL FOR CCTV PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2021P0926_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1291",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2021P0926_1900_-NONE-_-NONE- (misc_venezuela_cctv_electrical_material_39k_2021). Signed 2021-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2021P0926_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_cctv_electrical_material_39k_2021 USD 0.039m. Supports misc_venezuela_cctv_electrical_material_39k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 39406.7; date_signed 2021-09-21.",
    investment_type="equipment_supply",
)

# === Cycle 1291 ===
row_doc(
    "misc_chile_cctv_supplies_38k_2026",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Chile CCTV supplies",
    "Chile",
    "10 Dec 2025: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for CCTV supplies (PoP Chile); obligated USD 38711.50. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "38711.50", "2025-12-10", "2025", "", "",
    "CCTV SUPPLIES, Chile (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_chile_cctv_supplies_38k_2026",
    "CCTV SUPPLIES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18026P0011_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1291",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C18026P0011_1900_-NONE-_-NONE- (misc_chile_cctv_supplies_38k_2026). Signed 2025-12-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18026P0011_1900_-NONE-_-NONE-/.",
    "USASpending: misc_chile_cctv_supplies_38k_2026 USD 0.039m. Supports misc_chile_cctv_supplies_38k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 38711.5; date_signed 2025-12-10.",
    investment_type="equipment_supply",
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
