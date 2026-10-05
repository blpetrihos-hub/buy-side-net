#!/usr/bin/env python3
"""Cycles 999–1001: USASpending LatAm CapEx residual (~USD0.17–0.20m).

Seeds: 20261999–20262001. Thin top-up dry. Includes Luz del Sur MV substation (prc).
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


# === Cycle 999 ===
row_doc(
    "isobox_corozal_east_repairs_201k_2021",
    "infrastructure", "building_materials", "other",
    "Isobox — Corozal East facility repairs",
    "Panama",
    "26 May 2021: Department of Defense awards contract H9228121C0003 to Isobox for Corozal East facility repairs, Panama; obligated USD 201,230.86. CapEx face = award obligation. Distinct from isobox_corozal_este_237k_2025.",
    "201230.86", "2021-05-26", "2021", "8.980", "-79.575",
    "Facility repairs, Corozal East, Panama (USASpending description).",
    "usaspending_isobox_corozal_east_repairs_201k_2021",
    "COROZAL EAST FACILITY REPAIRS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228121C0003_9700_-NONE-_-NONE-/",
    "Actor: Isobox Inc. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle999",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_H9228121C0003_9700_-NONE-_-NONE- (Isobox Corozal East repairs). Signed 2021-05-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228121C0003_9700_-NONE-_-NONE-/.",
    "USASpending: Isobox Corozal East repairs USD 0.201m. Supports isobox_corozal_east_repairs_201k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 201230.86; date_signed 2021-05-26.",
)

row_doc(
    "cec_soto_cano_offices_199k_2021",
    "infrastructure", "building_materials", "other",
    "Civil Electrical Construction — Soto Cano multipurpose offices R-70/R-72",
    "Honduras",
    "23 Sep 2021: DoD awards contract W912QM21P0052 to Civil Electrical Construction Company for construction of two multipurpose offices R-70 and R-72 at Soto Cano Air Base; obligated USD 199,344.78. CapEx face = award obligation.",
    "199344.78", "2021-09-23", "2021", "14.382", "-87.621",
    "Multipurpose offices R-70 and R-72, Soto Cano Air Base, Honduras (USASpending description).",
    "usaspending_cec_soto_cano_offices_199k_2021",
    "CONSTRUCT TWO MULTIPURPOSE OFFICES, R-70 AND R72 SOTO CANO AIR BASE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM21P0052_9700_-NONE-_-NONE-/",
    "Actor: Civil Electrical Construction Company S. de R.L. (Tegucigalpa) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle999",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM21P0052_9700_-NONE-_-NONE- (CEC Soto Cano offices). Signed 2021-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM21P0052_9700_-NONE-_-NONE-/.",
    "USASpending: CEC Soto Cano offices USD 0.199m. Supports cec_soto_cano_offices_199k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 199344.78; date_signed 2021-09-23.",
)

row_doc(
    "misc_santa_marta_warehouse_197k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — CNP Santa Marta aviation warehouse enlargement",
    "Colombia",
    "23 Aug 2012: Department of State awards contract SCO15012CN014 for warehouse enlargement project at CNP aviation base Santa Marta; obligated USD 196,898.72. CapEx face = award obligation. Recipient redacted.",
    "196898.72", "2012-08-23", "2012", "11.120", "-74.230",
    "Warehouse enlargement, CNP aviation base Santa Marta, Colombia (USASpending description).",
    "usaspending_misc_santa_marta_warehouse_197k_2012",
    "WAREHOUSE ENLARGEMENT PROJECT - CNP AVIATION BASE SANTA MARTA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012CN014_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle999",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15012CN014_1900_-NONE-_-NONE- (Santa Marta warehouse). Signed 2012-08-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012CN014_1900_-NONE-_-NONE-/.",
    "USASpending: Santa Marta warehouse USD 0.197m. Supports misc_santa_marta_warehouse_197k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 196898.72; date_signed 2012-08-23.",
)

row_doc(
    "cec_soto_cano_dfac_hvac_195k_2021",
    "infrastructure", "building_materials", "other",
    "Civil Electrical Construction — Soto Cano DFAC HVAC central unit replacement",
    "Honduras",
    "22 Sep 2021: DoD awards contract W912QM21P0053 to Civil Electrical Construction Company for DFAC HVAC central unit replacement at Soto Cano Air Base; obligated USD 194,661.89. CapEx face = award obligation.",
    "194661.89", "2021-09-22", "2021", "14.382", "-87.621",
    "DFAC HVAC central unit replacement, Soto Cano Air Base, Honduras (USASpending description).",
    "usaspending_cec_soto_cano_dfac_hvac_195k_2021",
    "DFAC HVAC CENTRAL UNIT REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM21P0053_9700_-NONE-_-NONE-/",
    "Actor: Civil Electrical Construction Company S. de R.L. (Tegucigalpa) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle999",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM21P0053_9700_-NONE-_-NONE- (CEC Soto Cano DFAC HVAC). Signed 2021-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM21P0053_9700_-NONE-_-NONE-/.",
    "USASpending: CEC Soto Cano DFAC HVAC USD 0.195m. Supports cec_soto_cano_dfac_hvac_195k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 194661.89; date_signed 2021-09-22.",
)

row_doc(
    "eterna_soto_cano_barriers_191k_2011",
    "infrastructure", "building_materials", "other",
    "Eterna — Soto Cano main gate drop arm barriers",
    "Honduras",
    "15 Sep 2011: DoD awards task order 0002 under W9127811D0046 to Empresa de Construcción y Transporte Eterna for install drop arm barriers at main gate, Soto Cano Air Base, Honduras; obligated USD 190,569.21. CapEx face = award obligation.",
    "190569.21", "2011-09-15", "2011", "14.382", "-87.621",
    "Drop arm barriers at main gate, Soto Cano Air Base, Honduras (USASpending description).",
    "usaspending_eterna_soto_cano_barriers_191k_2011",
    "TAS::21 2020::TAS INSTALL DROP ARM BARRIERS AT MAIN GATE, SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127811D0046_9700/",
    "Actor: Empresa de Construcción y Transporte Eterna S.A. de C.V. (San Pedro Sula) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle999",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127811D0046_9700 (Eterna Soto Cano barriers). Signed 2011-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127811D0046_9700/.",
    "USASpending: Eterna Soto Cano barriers USD 0.191m. Supports eterna_soto_cano_barriers_191k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 190569.21; date_signed 2011-09-15.",
)

# === Cycle 1000 ===
row_doc(
    "misc_balcarce_remodel_190k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Balcarce 1776 Martinez remodel",
    "Argentina",
    "29 Sep 2018: Department of State awards contract 19AR2018C0011 for remodel at Balcarce 1776, Martinez (PoP Argentina); obligated USD 190,000. CapEx face = award obligation. Recipient redacted.",
    "190000", "2018-09-29", "2018", "-34.490", "-58.510",
    "Remodel Balcarce 1776, Martinez, Buenos Aires Province, Argentina (USASpending description).",
    "usaspending_misc_balcarce_remodel_190k_2018",
    "REMODEL BALCARCE 1776, MARTINEZ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018C0011_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1000",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2018C0011_1900_-NONE-_-NONE- (Balcarce remodel). Signed 2018-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018C0011_1900_-NONE-_-NONE-/.",
    "USASpending: Balcarce remodel USD 0.190m. Supports misc_balcarce_remodel_190k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 190000; date_signed 2018-09-29.",
)

row_doc(
    "nelson_tibu_school_190k_2018",
    "infrastructure", "building_materials", "other",
    "Nelson Rodríguez Ingeniería — Tibu school construction",
    "Colombia",
    "28 Sep 2018: U.S. Army Corps of Engineers awards contract W913FT18C0002 to Nelson Rodríguez Ingeniería for construction school Tibu; obligated USD 189,806.78. CapEx face = award obligation.",
    "189806.78", "2018-09-28", "2018", "8.640", "-72.740",
    "School construction, Tibú, Norte de Santander, Colombia (USASpending description).",
    "usaspending_nelson_tibu_school_190k_2018",
    "CONSTRUCTION SCHOOL TIBU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT18C0002_9700_-NONE-_-NONE-/",
    "Actor: Nelson Rodríguez Ingeniería S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1000",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT18C0002_9700_-NONE-_-NONE- (Nelson Tibu school). Signed 2018-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT18C0002_9700_-NONE-_-NONE-/.",
    "USASpending: Nelson Tibu school USD 0.190m. Supports nelson_tibu_school_190k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 189806.78; date_signed 2018-09-28.",
)

row_doc(
    "johnd_belize_latrines_190k_2011",
    "infrastructure", "building_materials", "other",
    "John D Engineering — Belize latrines new construction",
    "Belize",
    "21 Sep 2011: DoD awards contract W912CL11C0036 to John D Engineering for new construction, latrines (PoP Belize); obligated USD 189,730.71. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "189730.71", "2011-09-21", "2011", "", "",
    "New latrines construction, Belize (USASpending PoP Belize; site not named — lat/lon blank).",
    "usaspending_johnd_belize_latrines_190k_2011",
    "NEW CONSTRUCTION, LATRINES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0036_9700_-NONE-_-NONE-/",
    "Actor: John D Engineering Ltd. (Belize) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1000",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL11C0036_9700_-NONE-_-NONE- (John D Belize latrines). Signed 2011-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0036_9700_-NONE-_-NONE-/.",
    "USASpending: John D Belize latrines USD 0.190m. Supports johnd_belize_latrines_190k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 189730.71; date_signed 2011-09-21.",
)

row_doc(
    "bonatti_salvador_hvac_184k_2025",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros — CSL El Salvador HVAC B100 replacement",
    "El Salvador",
    "24 Sep 2025: USACE awards task order W9127825FA246 to Bonatti Ingenieros y Arquitectos for seed project replace HVAC B100 CSL El Salvador; obligated USD 183,655.31. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "183655.31", "2025-09-24", "2025", "", "",
    "HVAC B100 replacement, CSL El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_bonatti_salvador_hvac_184k_2025",
    "SEED PROJECT FOR W9127825DA035 - REPLACE HVAC B100 CSL EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA246_9700_W9127825DA035_9700/",
    "Actor: Bonatti Ingenieros y Arquitectos S.A. (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1000",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA246_9700_W9127825DA035_9700 (Bonatti CSL HVAC). Signed 2025-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA246_9700_W9127825DA035_9700/.",
    "USASpending: Bonatti CSL HVAC USD 0.184m. Supports bonatti_salvador_hvac_184k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 183655.31; date_signed 2025-09-24.",
)

row_doc(
    "luz_del_sur_lima_substation_181k_2016",
    "energy", "power_plants_grid", "prc",
    "Luz del Sur — Lima CMR MV electrical substation",
    "Peru",
    "8 Jul 2016: Department of State awards contract SPE50016C0017 to Luz del Sur S.A.A. for Lima FY2016 CMR construction of MV electrical substation; obligated USD 181,032.15. CapEx face = award obligation. Actor coded prc (Luz del Sur / China Three Gorges subsidiary, consistent with catalog LDS rows).",
    "181032.15", "2016-07-08", "2016", "-12.100", "-76.990",
    "MV electrical substation construction, CMR Lima, Peru (USASpending description; Lima approximate).",
    "usaspending_luz_del_sur_lima_substation_181k_2016",
    "LIMA FY2016 CMR CONSTRUCTION OF MV ELECTRICAL SUBSTATION IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0017_1900_-NONE-_-NONE-/",
    "Actor: Luz del Sur S.A.A. (Lima; CTG / China Three Gorges subsidiary) — prc. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1000",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50016C0017_1900_-NONE-_-NONE- (Luz del Sur Lima substation). Signed 2016-07-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0017_1900_-NONE-_-NONE-/.",
    "USASpending: Luz del Sur Lima substation USD 0.181m. Supports luz_del_sur_lima_substation_181k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 181032.15; date_signed 2016-07-08.",
)

# === Cycle 1001 ===
row_doc(
    "ramsey_antigua_erw_179k_2010",
    "infrastructure", "building_materials", "other",
    "Ramsey's Construction — Antigua emergency response warehouse",
    "Antigua and Barbuda",
    "30 Sep 2010: DoD awards contract N6945010C0044 to Ramsey's Construction & Architecture for emergency response warehouse (ERW) (PoP Antigua and Barbuda); obligated USD 179,384. CapEx face = award obligation.",
    "179384", "2010-09-30", "2010", "17.127", "-61.846",
    "Emergency response warehouse, Antigua and Barbuda (USASpending PoP Antigua; St. George's / island approximate).",
    "usaspending_ramsey_antigua_erw_179k_2010",
    "EMERGENCY RESPONSE WAREHOUSE (ERW)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0044_9700_-NONE-_-NONE-/",
    "Actor: Ramsey's Construction & Architecture (St. Georges, Antigua) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1001",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945010C0044_9700_-NONE-_-NONE- (Ramsey Antigua ERW). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0044_9700_-NONE-_-NONE-/.",
    "USASpending: Ramsey Antigua ERW USD 0.179m. Supports ramsey_antigua_erw_179k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 179384; date_signed 2010-09-30.",
)

row_doc(
    "mava_bocas_road_177k_2018",
    "infrastructure", "bridges_roads", "other",
    "MAVA Tractor — STRI Bocas del Toro station internal road repairs",
    "Panama",
    "7 Sep 2018: Smithsonian awards contract 33330218CF0010383 to MAVA Tractor for STRI Bocas del Toro station internal road repairs; obligated USD 176,680.27. CapEx face = award obligation.",
    "176680.27", "2018-09-07", "2018", "9.351", "-82.257",
    "Internal road repairs, STRI Bocas del Toro station, Panama (USASpending / Smithsonian).",
    "usaspending_mava_bocas_road_177k_2018",
    "IGF::OT::IGF STRI - BOCAS DEL TORO STATION INTERNAL ROAD REPAIRS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330218CF0010383_3300_-NONE-_-NONE-/",
    "Actor: MAVA Tractor, S.A. (Panama City) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1001",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330218CF0010383_3300_-NONE-_-NONE- (MAVA Bocas road). Signed 2018-09-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330218CF0010383_3300_-NONE-_-NONE-/.",
    "USASpending: MAVA Bocas road USD 0.177m. Supports mava_bocas_road_177k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 176680.27; date_signed 2018-09-07.",
)

row_doc(
    "tropical_ladyville_pref_173k_2014",
    "infrastructure", "building_materials", "other",
    "Tropical Holdings Ladyville — three metal prefabricated buildings",
    "Belize",
    "26 Sep 2014: DoD awards contract W912CL14C0027 to Tropical Holdings Ladyville for construction of three metal prefabricated buildings (PoP Belize); obligated USD 173,196. CapEx face = award obligation.",
    "173196", "2014-09-26", "2014", "17.455", "-88.305",
    "Three metal prefabricated buildings, Ladyville, Belize (USASpending / recipient locality).",
    "usaspending_tropical_ladyville_pref_173k_2014",
    "CONSTRUCTION THREE METAL PREF BUILDINGS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL14C0027_9700_-NONE-_-NONE-/",
    "Actor: Tropical Holdings Ladyville Ltd. (Ladyville, Belize) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1001",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL14C0027_9700_-NONE-_-NONE- (Tropical Ladyville pref). Signed 2014-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL14C0027_9700_-NONE-_-NONE-/.",
    "USASpending: Tropical Ladyville pref USD 0.173m. Supports tropical_ladyville_pref_173k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 173196; date_signed 2014-09-26.",
)

row_doc(
    "hulke_opbat_hangar_172k_2011",
    "infrastructure", "building_materials", "us",
    "Hulke Construction — OPBAT demo hangar",
    "Bahamas",
    "17 Sep 2011: DoD awards contract N6945011C0082 to Hulke Construction for OPBAT demo hangar (PoP Bahamas); obligated USD 171,850. CapEx face = award obligation. Exact OPBAT site unnamed — lat/lon blank.",
    "171850", "2011-09-17", "2011", "", "",
    "OPBAT demo hangar, Bahamas (USASpending PoP Bahamas; OPBAT site not named — lat/lon blank).",
    "usaspending_hulke_opbat_hangar_172k_2011",
    "OPBAT DEMO HANGAR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0082_9700_-NONE-_-NONE-/",
    "Actor: Hulke Construction Company, LLC (Sanford FL, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1001",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945011C0082_9700_-NONE-_-NONE- (Hulke OPBAT hangar). Signed 2011-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0082_9700_-NONE-_-NONE-/.",
    "USASpending: Hulke OPBAT hangar USD 0.172m. Supports hulke_opbat_hangar_172k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 171850; date_signed 2011-09-17.",
)

row_doc(
    "spectrum_belmopan_electrical_171k_2018",
    "energy", "power_plants_grid", "us",
    "Spectrum Electrical — Belmopan residence electrical distribution minor construction",
    "Belize",
    "26 Nov 2018: Department of State awards task order 19AQMM19F0161 to Spectrum Electrical Services for U.S. Embassy Belmopan Belize residence-only electrical distribution system minor construction; obligated USD 170,904.07. CapEx face = award obligation.",
    "170904.07", "2018-11-26", "2018", "17.251", "-88.759",
    "Residence electrical distribution minor construction, U.S. Embassy Belmopan, Belize (USASpending description).",
    "usaspending_spectrum_belmopan_electrical_171k_2018",
    "US EMBASSY BELMOPAN BELIZE -RESIDENCE ONLY- ELECTRICAL DISTRIBUTION SYSTEM MINOR CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F0161_1900_19AQMM18D0072_1900/",
    "Actor: Spectrum Electrical Services, Inc. (Fairfax VA, U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1001",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19F0161_1900_19AQMM18D0072_1900 (Spectrum Belmopan electrical). Signed 2018-11-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F0161_1900_19AQMM18D0072_1900/.",
    "USASpending: Spectrum Belmopan electrical USD 0.171m. Supports spectrum_belmopan_electrical_171k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 170904.07; date_signed 2018-11-26.",
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
    print(f"cycles999-1001 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
