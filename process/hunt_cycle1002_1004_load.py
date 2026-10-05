#!/usr/bin/env python3
"""Cycles 1002–1004: USASpending LatAm CapEx residual (~USD0.15–0.18m).

Seeds: 20262002–20262004. Thin top-up dry.
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


# === Cycle 1002 ===
row_doc(
    "aj_estructuras_pads_184k_2023",
    "infrastructure", "building_materials", "other",
    "AJ Estructuras — El Salvador concrete pads",
    "El Salvador",
    "27 Jun 2023: Department of State awards contract 19ES6023P0810 to AJ Estructuras for concrete pads (PoP El Salvador); obligated USD 183,605.34. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "183605.34", "2023-06-27", "2023", "", "",
    "Concrete pads, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_aj_estructuras_pads_184k_2023",
    "CONCRETE PADS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6023P0810_1900_-NONE-_-NONE-/",
    "Actor: AJ Estructuras Sociedad Anónima de Capital Variable (San Salvador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1002",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6023P0810_1900_-NONE-_-NONE- (AJ Estructuras pads). Signed 2023-06-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6023P0810_1900_-NONE-_-NONE-/.",
    "USASpending: AJ Estructuras pads USD 0.184m. Supports aj_estructuras_pads_184k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 183605.34; date_signed 2023-06-27.",
)

row_doc(
    "misc_barbados_handrails_183k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Barbados chancery roof handrails",
    "Barbados",
    "10 Aug 2011: Department of State awards contract SBB21011C0003 for supply and install handrails to chancery roof (PoP Barbados); obligated USD 183,315.03. CapEx face = award obligation. Recipient redacted.",
    "183315.03", "2011-08-10", "2011", "13.097", "-59.615",
    "Chancery roof handrails, Bridgetown, Barbados (USASpending PoP Barbados).",
    "usaspending_misc_barbados_handrails_183k_2011",
    "SUPPLY AND INSTALL HANDRAILS TO CHANCERY ROOF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21011C0003_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1002",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21011C0003_1900_-NONE-_-NONE- (Barbados handrails). Signed 2011-08-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21011C0003_1900_-NONE-_-NONE-/.",
    "USASpending: Barbados handrails USD 0.183m. Supports misc_barbados_handrails_183k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 183315.03; date_signed 2011-08-10.",
)

row_doc(
    "misc_paraguay_cmr_roof_177k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Paraguay CMR roof repair",
    "Paraguay",
    "9 Sep 2020: Department of State awards contract 19PA1020C0008 for CMR roof repair (PoP Paraguay); obligated USD 176,650.15. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "176650.15", "2020-09-09", "2020", "", "",
    "CMR roof repair, Paraguay (USASpending PoP Paraguay; site not named — lat/lon blank).",
    "usaspending_misc_paraguay_cmr_roof_177k_2020",
    "CMR ROOF REPAIR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1020C0008_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1002",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PA1020C0008_1900_-NONE-_-NONE- (Paraguay CMR roof). Signed 2020-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1020C0008_1900_-NONE-_-NONE-/.",
    "USASpending: Paraguay CMR roof USD 0.177m. Supports misc_paraguay_cmr_roof_177k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 176650.15; date_signed 2020-09-09.",
)

row_doc(
    "proyectos_corozal_bldg9_171k_2013",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles — Corozal Building #9 renovation Panama City",
    "Panama",
    "26 Sep 2013: DoD awards contract W912CL13C0015 to Proyectos Civiles for renovation of U.S. military occupied Building #9 Corozal in Panama City; obligated USD 171,156.92. CapEx face = award obligation.",
    "171156.92", "2013-09-26", "2013", "8.980", "-79.575",
    "Building #9 renovation, Corozal, Panama City, Panama (USASpending description).",
    "usaspending_proyectos_corozal_bldg9_171k_2013",
    "RENOVATION OF US MILITARY OCCUPIED BUILDING #9 COROZAL IN PANAMA CITY, PANAMA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL13C0015_9700_-NONE-_-NONE-/",
    "Actor: Proyectos Civiles S y M Limitada (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1002",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL13C0015_9700_-NONE-_-NONE- (Proyectos Corozal Bldg 9). Signed 2013-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL13C0015_9700_-NONE-_-NONE-/.",
    "USASpending: Proyectos Corozal Bldg 9 USD 0.171m. Supports proyectos_corozal_bldg9_171k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 171156.92; date_signed 2013-09-26.",
)

row_doc(
    "misc_colombia_school_169k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia school construction",
    "Colombia",
    "14 Jun 2016: U.S. Army Corps of Engineers awards contract W913FT16C0001 for school construction (PoP Colombia); obligated USD 169,386.87. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "169386.87", "2016-06-14", "2016", "", "",
    "School construction, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_misc_colombia_school_169k_2016",
    "IGF::OT::IGF SCHOOL CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT16C0001_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1002",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT16C0001_9700_-NONE-_-NONE- (Colombia school). Signed 2016-06-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT16C0001_9700_-NONE-_-NONE-/.",
    "USASpending: Colombia school USD 0.169m. Supports misc_colombia_school_169k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 169386.87; date_signed 2016-06-14.",
)

# === Cycle 1003 ===
row_doc(
    "ecm_jacmel_boat_ramp_169k_2017",
    "infrastructure", "port_ownership", "other",
    "Economic Construction Maritimes — Jacmel boat ramp",
    "Haiti",
    "31 Mar 2017: Department of State awards contract SAQMMA17C0107 to Economic Construction Maritimes for construction of boat ramp in Jacmel, Haiti; obligated USD 168,550. CapEx face = award obligation.",
    "168550", "2017-03-31", "2017", "18.234", "-72.535",
    "Boat ramp, Jacmel, Haiti (USASpending description).",
    "usaspending_ecm_jacmel_boat_ramp_169k_2017",
    "CONSTRUCTION OF BOAT RAMP IN JACMEL, HAITIIGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0107_1900_-NONE-_-NONE-/",
    "Actor: Economic Construction Maritimes S.A. (Port-au-Prince) — other. Official USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle1003",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0107_1900_-NONE-_-NONE- (ECM Jacmel boat ramp). Signed 2017-03-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0107_1900_-NONE-_-NONE-/.",
    "USASpending: ECM Jacmel boat ramp USD 0.169m. Supports ecm_jacmel_boat_ramp_169k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 168550; date_signed 2017-03-31.",
)

row_doc(
    "misc_monterrey_garage_roof_168k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Monterrey parking garage roof repair coating",
    "Mexico",
    "11 Jul 2022: Department of State awards contract 19MX5622C0004 for Monterrey parking garage roof repair coating (PoP Mexico); obligated USD 167,671.02. CapEx face = award obligation. Recipient redacted.",
    "167671.02", "2022-07-11", "2022", "25.686", "-100.316",
    "Parking garage roof repair coating, Monterrey, Mexico (USASpending description MTY-FAC).",
    "usaspending_misc_monterrey_garage_roof_168k_2022",
    "MTY-FAC-7901-FWP94-PARKING GARAGE ROOF REPAIR COATING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5622C0004_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1003",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5622C0004_1900_-NONE-_-NONE- (Monterrey garage roof). Signed 2022-07-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5622C0004_1900_-NONE-_-NONE-/.",
    "USASpending: Monterrey garage roof USD 0.168m. Supports misc_monterrey_garage_roof_168k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 167671.02; date_signed 2022-07-11.",
)

row_doc(
    "misc_suriname_paving_167k_2019",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Suriname paving",
    "Suriname",
    "25 Sep 2019: Department of State awards contract 19NS5019P0587 for paving (PoP Suriname); obligated USD 166,609.81. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "166609.81", "2019-09-25", "2019", "", "",
    "Paving, Suriname (USASpending PoP Suriname; site not named — lat/lon blank).",
    "usaspending_misc_suriname_paving_167k_2019",
    "PAVING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5019P0587_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1003",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19NS5019P0587_1900_-NONE-_-NONE- (Suriname paving). Signed 2019-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5019P0587_1900_-NONE-_-NONE-/.",
    "USASpending: Suriname paving USD 0.167m. Supports misc_suriname_paving_167k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 166609.81; date_signed 2019-09-25.",
)

row_doc(
    "ace_tres_canadas_roof_166k_2014",
    "infrastructure", "building_materials", "us",
    "Ace Roof Coatings — Tres Canadas residential roof repair Mexico",
    "Mexico",
    "21 Aug 2014: Department of State awards task order SMX53014F0613 to Ace Roof Coatings for Tres Canadas roof repair (residential) (PoP Mexico); obligated USD 165,894.12. CapEx face = award obligation. Exact Tres Canadas pin unnamed — lat/lon blank.",
    "165894.12", "2014-08-21", "2014", "", "",
    "Tres Canadas residential roof repair, Mexico (USASpending description; site not geocoded — lat/lon blank).",
    "usaspending_ace_tres_canadas_roof_166k_2014",
    "MEX-FAC 7901 TRES CANADAS ROOF REPAIR (RESIDENTIAL)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53014F0613_1900_GS07F177AA_4732/",
    "Actor: Ace Roof Coatings, Inc. (Rowlett TX, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1003",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53014F0613_1900_GS07F177AA_4732 (Ace Tres Canadas roof). Signed 2014-08-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53014F0613_1900_GS07F177AA_4732/.",
    "USASpending: Ace Tres Canadas roof USD 0.166m. Supports ace_tres_canadas_roof_166k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 165894.12; date_signed 2014-08-21.",
)

row_doc(
    "castro_shootsouse_164k_2025",
    "infrastructure", "building_materials", "other",
    "Francisco Castro — El Salvador shoothouse construction",
    "El Salvador",
    "21 Apr 2025: Department of Defense awards contract H9228125C0004 to Francisco Rigoberto Castro Barrera for construction of shoothouse (PoP El Salvador); obligated USD 164,038.32. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "164038.32", "2025-04-21", "2025", "", "",
    "Shoothouse construction, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_castro_shootsouse_164k_2025",
    "CONSTRUCTION OF SHOOTHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125C0004_9700_-NONE-_-NONE-/",
    "Actor: Francisco Rigoberto Castro Barrera (Chalchuapa) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1003",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_H9228125C0004_9700_-NONE-_-NONE- (Castro shoothouse). Signed 2025-04-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125C0004_9700_-NONE-_-NONE-/.",
    "USASpending: Castro shoothouse USD 0.164m. Supports castro_shootsouse_164k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 164038.32; date_signed 2025-04-21.",
)

# === Cycle 1004 ===
row_doc(
    "ace_cdj_nob_roof_164k_2016",
    "infrastructure", "building_materials", "us",
    "Ace Roof Coatings — Ciudad Juárez NOB roof coating",
    "Mexico",
    "5 Jul 2016: Department of State awards task order SMX11516F0068 to Ace Roof Coatings for CDJ-7901 NOB roof coating for gov prop 1000 (PoP Mexico / Ciudad Juárez); obligated USD 163,906.64. CapEx face = award obligation.",
    "163906.64", "2016-07-05", "2016", "31.690", "-106.425",
    "NOB roof coating, Ciudad Juárez, Mexico (USASpending description CDJ-7901).",
    "usaspending_ace_cdj_nob_roof_164k_2016",
    "CDJ-7901 NOB ROOF COATING FOR GOV PROP 1000",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516F0068_1900_GS07F177AA_4732/",
    "Actor: Ace Roof Coatings, Inc. (Rowlett TX, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1004",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11516F0068_1900_GS07F177AA_4732 (Ace CDJ NOB roof). Signed 2016-07-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516F0068_1900_GS07F177AA_4732/.",
    "USASpending: Ace CDJ NOB roof USD 0.164m. Supports ace_cdj_nob_roof_164k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 163906.64; date_signed 2016-07-05.",
)

row_doc(
    "tw_tupper_roof_164k_2022",
    "infrastructure", "building_materials", "other",
    "Distribuidora TW — STRI Tupper library roof replace and reinforce",
    "Panama",
    "13 Dec 2021: Smithsonian awards task order 33330222FF0010048 to Distribuidora TW for replace and reinforce roof for library at Tupper; obligated USD 163,878.21. CapEx face = award obligation.",
    "163878.21", "2021-12-13", "2021", "8.960", "-79.550",
    "Library roof replace/reinforce, STRI Tupper, Panama (USASpending / Smithsonian).",
    "usaspending_tw_tupper_roof_164k_2022",
    "STRI: REPLACE AND REINFORCE ROOF FOR LIBRARY AT TUPPER.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330222FF0010048_3300_33330220DF0010213_3300/",
    "Actor: Distribuidora TW S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1004",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330222FF0010048_3300_33330220DF0010213_3300 (TW Tupper roof). Signed 2021-12-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330222FF0010048_3300_33330220DF0010213_3300/.",
    "USASpending: TW Tupper roof USD 0.164m. Supports tw_tupper_roof_164k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 163878.21; date_signed 2021-12-13.",
)

row_doc(
    "mfg_scan_eagle_macarena_163k_2011",
    "infrastructure", "building_materials", "other",
    "MFG Ingeniería — Scan Eagle building La Macarena",
    "Colombia",
    "29 Jul 2011: U.S. Army Corps of Engineers awards contract W913FT11C0016 to MFG Ingeniería for Scan Eagle building (La Macarena / CO); obligated USD 162,538.78. CapEx face = award obligation.",
    "162538.78", "2011-07-29", "2011", "2.180", "-73.780",
    "Scan Eagle building, La Macarena, Meta, Colombia (USASpending description).",
    "usaspending_mfg_scan_eagle_macarena_163k_2011",
    "SCAN EAGLE BUILDING (LA MACARENA / CO)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0016_9700_-NONE-_-NONE-/",
    "Actor: MFG Ingeniería SAS (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1004",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11C0016_9700_-NONE-_-NONE- (MFG Scan Eagle La Macarena). Signed 2011-07-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0016_9700_-NONE-_-NONE-/.",
    "USASpending: MFG Scan Eagle La Macarena USD 0.163m. Supports mfg_scan_eagle_macarena_163k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 162538.78; date_signed 2011-07-29.",
)

row_doc(
    "energy_central_haiti_pv_159k_2022",
    "energy", "solar", "other",
    "Energy Central — HNP school and academy photovoltaic system",
    "Haiti",
    "17 Mar 2022: Department of State awards contract 19HA7022C0001 to Energy Central for INL-HNP photovoltaic system for HNP school and academy; obligated USD 158,860. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "158860", "2022-03-17", "2022", "", "",
    "Photovoltaic system for HNP school and academy, Haiti (USASpending PoP Haiti; site not named — lat/lon blank).",
    "usaspending_energy_central_haiti_pv_159k_2022",
    "INL-HNP PHOTOVOLTAIC SYSTEM FOR HNP SCHOOL & ACADEMY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7022C0001_1900_-NONE-_-NONE-/",
    "Actor: Energy Central S.A. (Port-au-Prince) — other. Official USASpending Award API. Shuffle solar.",
    "hunt_cycle1004",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7022C0001_1900_-NONE-_-NONE- (Energy Central HNP PV). Signed 2022-03-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7022C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Energy Central HNP PV USD 0.159m. Supports energy_central_haiti_pv_159k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 158860; date_signed 2022-03-17.",
)

row_doc(
    "mckinney_gamboa_ae_161k_2016",
    "infrastructure", "engineering_epc", "us",
    "McKinney and Company — A&E design Gamboa facilities refurbishment",
    "Panama",
    "7 Sep 2016: Smithsonian awards task order F16CW10590 to McKinney and Company for A-E services for design of refurbishment of facilities at Gamboa project; obligated USD 161,141.77. CapEx face = award obligation.",
    "161141.77", "2016-09-07", "2016", "9.120", "-79.700",
    "A&E design for facilities refurbishment, Gamboa, Panama (USASpending / Smithsonian).",
    "usaspending_mckinney_gamboa_ae_161k_2016",
    "IGF::OT::IGF A-E SERVICES FOR DESIGN OF REFURBISHMENT OF FACILITIES AT GAMBOA PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F16CW10590_3300_F06CC10332_3300/",
    "Actor: McKinney and Company, Inc. (Virginia, U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1004",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F16CW10590_3300_F06CC10332_3300 (McKinney Gamboa A&E). Signed 2016-09-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F16CW10590_3300_F06CC10332_3300/.",
    "USASpending: McKinney Gamboa A&E USD 0.161m. Supports mckinney_gamboa_ae_161k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 161141.77; date_signed 2016-09-07.",
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
    print(f"cycles1002-1004 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
