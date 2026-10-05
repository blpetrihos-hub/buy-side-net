#!/usr/bin/env python3
"""Cycles 1020–1022: USASpending LatAm CapEx residual (~USD0.08–0.11m).

Seeds: 20262020–20262022. Thin top-up dry.
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

# === Cycle 1020 ===
row_doc(
    "aa_colombia_hazmat_107k_2011",
    "infrastructure", "building_materials", "us",
    "A & A Sheet Metal — Colombia HAZMAT storage building",
    "Colombia",
    "23 May 2011: DoD awards order W913FT11F0012 to A & A Sheet Metal Products for HAZMAT storage building (PoP Colombia); obligated USD 107,451. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "107451", "2011-05-23", "2011", "", "",
    "HAZMAT storage building, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_aa_colombia_hazmat_107k_2011",
    "HAZMAT STORAGE BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11F0012_9700_GS28F0010B_4730/",
    "Actor: A & A Sheet Metal Products Inc. (La Porte TX, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1020",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11F0012_9700_GS28F0010B_4730 (A&A Colombia HAZMAT). Signed 2011-05-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11F0012_9700_GS28F0010B_4730/.",
    "USASpending: A&A Colombia HAZMAT USD 0.107m. Supports aa_colombia_hazmat_107k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 107451; date_signed 2011-05-23.",
)

row_doc(
    "serrano_peru_incinerator_109k_2018",
    "infrastructure", "building_materials", "other",
    "Serrano Proaño — Peru incinerator demolition and restoration",
    "Peru",
    "29 Sep 2018: DoD awards order W9127818F0789 to Serrano Proaño Diseño y Construcción for demolition and restoration of incinerator (PoP Peru); obligated USD 108,968.26. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "108968.26", "2018-09-29", "2018", "", "",
    "Incinerator demolition and restoration, Peru (USASpending PoP Peru; site not named — lat/lon blank).",
    "usaspending_serrano_peru_incinerator_109k_2018",
    "DEMOLITION&RESTORATION OF INCINERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0789_9700_W9127818D0034_9700/",
    "Actor: Serrano Proaño Diseño y Construcción (Ecuador firm; PoP Peru) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1020",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0789_9700_W9127818D0034_9700 (Serrano Peru incinerator). Signed 2018-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0789_9700_W9127818D0034_9700/.",
    "USASpending: Serrano Peru incinerator USD 0.109m. Supports serrano_peru_incinerator_109k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 108968.26; date_signed 2018-09-29.",
)

row_doc(
    "orellana_salvador_roof_109k_2021",
    "infrastructure", "building_materials", "other",
    "Orellana Aguirre — El Salvador ILEA residence hall roof repair",
    "El Salvador",
    "25 Feb 2021: Department of State awards contract 19ES6021P0304 to Orellana Aguirre Ingenieros Arquitectos for ILEA residence hall roof repair and waterproofing (PoP El Salvador); obligated USD 108,574.18. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "108574.18", "2021-02-25", "2021", "", "",
    "ILEA residence hall roof repair and waterproofing, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_orellana_salvador_roof_109k_2021",
    "ILEA RESIDENCE HALL ROOF REPAIR AND WATERPROOFING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0304_1900_-NONE-_-NONE-/",
    "Actor: Orellana Aguirre Ingenieros Arquitectos (El Salvador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1020",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6021P0304_1900_-NONE-_-NONE- (Orellana ILEA roof). Signed 2021-02-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0304_1900_-NONE-_-NONE-/.",
    "USASpending: Orellana ILEA roof USD 0.109m. Supports orellana_salvador_roof_109k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 108574.18; date_signed 2021-02-25.",
)

row_doc(
    "misc_tumaco_kennels_107k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Tumaco K9 kennels",
    "Colombia",
    "17 Sep 2015: Department of State awards contract SCO15015C0004 for construction of 12 individual kennels — Tumaco (PoP Colombia); obligated USD 107,125.93. CapEx face = award obligation. Recipient redacted.",
    "107125.93", "2015-09-17", "2015", "1.806", "-78.765",
    "Construction of 12 individual kennels, Tumaco, Colombia (USASpending description; Tumaco named).",
    "usaspending_misc_tumaco_kennels_107k_2015",
    "MANUAL ERAD CONSTRUCTION OF 12 INDIVIDUAL KENNELS - TUMACO 3.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15015C0004_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1020",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15015C0004_1900_-NONE-_-NONE- (Tumaco kennels). Signed 2015-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15015C0004_1900_-NONE-_-NONE-/.",
    "USASpending: Tumaco kennels USD 0.107m. Supports misc_tumaco_kennels_107k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 107125.93; date_signed 2015-09-17.",
)

row_doc(
    "misc_tumaco_fence_106k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Tumaco ARAVI DIRAN perimeter fence",
    "Colombia",
    "17 Sep 2015: Department of State awards contract SCO15015C0005 for ARAVI DIRAN area perimeter fence project Tumaco (PoP Colombia); obligated USD 106,164.31. CapEx face = award obligation. Recipient redacted.",
    "106164.31", "2015-09-17", "2015", "1.806", "-78.765",
    "ARAVI DIRAN area perimeter fence, Tumaco, Colombia (USASpending description; Tumaco named).",
    "usaspending_misc_tumaco_fence_106k_2015",
    "INTER BS- ARAVI DIRAN AREA PERIMETER FENCE PROJECT TUMACO 3.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15015C0005_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1020",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15015C0005_1900_-NONE-_-NONE- (Tumaco fence). Signed 2015-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15015C0005_1900_-NONE-_-NONE-/.",
    "USASpending: Tumaco fence USD 0.106m. Supports misc_tumaco_fence_106k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 106164.31; date_signed 2015-09-17.",
)

# === Cycle 1021 ===
row_doc(
    "inecon_helipad_105k_2011",
    "infrastructure", "building_materials", "other",
    "Inecon — Colombia helipad and tie-down construction",
    "Colombia",
    "20 Jun 2011: DoD awards contract W913FT11C0015 to Inecon for helipad and tie-down construction (PoP Colombia); obligated USD 105,000.67. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "105000.67", "2011-06-20", "2011", "", "",
    "Helipad and tie-down construction, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_inecon_helipad_105k_2011",
    "HELIPAD AND TIE DOWN CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0015_9700_-NONE-_-NONE-/",
    "Actor: Inecon S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1021",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11C0015_9700_-NONE-_-NONE- (Inecon helipad). Signed 2011-06-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0015_9700_-NONE-_-NONE-/.",
    "USASpending: Inecon helipad USD 0.105m. Supports inecon_helipad_105k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 105000.67; date_signed 2011-06-20.",
)

row_doc(
    "misc_chile_parking_expansion_105k_2023",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Chile parking lot expansion",
    "Chile",
    "24 Aug 2023: Department of State awards contract 19C18023P1449 for parking lot expansion (PoP Chile); obligated USD 104,557.75. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "104557.75", "2023-08-24", "2023", "", "",
    "Parking lot expansion, Chile (USASpending PoP Chile; site not named — lat/lon blank).",
    "usaspending_misc_chile_parking_expansion_105k_2023",
    "PARKING LOT EXPANSION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18023P1449_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1021",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C18023P1449_1900_-NONE-_-NONE- (Chile parking expansion). Signed 2023-08-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18023P1449_1900_-NONE-_-NONE-/.",
    "USASpending: Chile parking expansion USD 0.105m. Supports misc_chile_parking_expansion_105k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 104557.75; date_signed 2023-08-24.",
)

row_doc(
    "misc_nogales_fence_104k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Nogales NCC perimeter fence",
    "Mexico",
    "19 Jul 2016: Department of State awards contract SMX60016M0090 for OBO NCC perimeter fence and light — Nogales (PoP Mexico); obligated USD 104,069.40. CapEx face = award obligation. Recipient redacted.",
    "104069.4", "2016-07-19", "2016", "31.309", "-110.942",
    "NCC perimeter fence and lighting, Nogales, Mexico (USASpending description; Nogales named).",
    "usaspending_misc_nogales_fence_104k_2016",
    "OBO - NCC PERIMETER FENCE AND LIGHT - NOGALES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX60016M0090_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1021",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX60016M0090_1900_-NONE-_-NONE- (Nogales fence). Signed 2016-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX60016M0090_1900_-NONE-_-NONE-/.",
    "USASpending: Nogales fence USD 0.104m. Supports misc_nogales_fence_104k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 104069.4; date_signed 2016-07-19.",
)

row_doc(
    "misc_colombia_fuel_storage_104k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Colombia fuel storage system construction",
    "Colombia",
    "27 Sep 2010: DoD awards contract W913FT10C0039 for fuel storage system construction (PoP Colombia); obligated USD 103,773.65. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "103773.65", "2010-09-27", "2010", "", "",
    "Fuel storage system construction, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_misc_colombia_fuel_storage_104k_2010",
    "FUEL STORAGE SYSTEM CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10C0039_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1021",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT10C0039_9700_-NONE-_-NONE- (Colombia fuel storage). Signed 2010-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10C0039_9700_-NONE-_-NONE-/.",
    "USASpending: Colombia fuel storage USD 0.104m. Supports misc_colombia_fuel_storage_104k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 103773.65; date_signed 2010-09-27.",
)

row_doc(
    "red_orange_dr_generator_89k_2018",
    "energy", "power_plants_grid", "us",
    "Red Orange North America — Dominican Republic DNP DICAT backup generator",
    "Dominican Republic",
    "10 May 2018: Department of State awards contract 19DR8618P0394 to Red Orange North America for INL donation backup generator for DNP DICAT (PoP Dominican Republic); obligated USD 88,551. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "88551", "2018-05-10", "2018", "", "",
    "Backup generator donation for DNP DICAT, Dominican Republic (USASpending PoP Dominican Republic; site not named — lat/lon blank).",
    "usaspending_red_orange_dr_generator_89k_2018",
    "INL DONATION BACKUP GENERATOR FOR DNP DICAT   IN13DRC2",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8618P0394_1900_-NONE-_-NONE-/",
    "Actor: Red Orange North America Inc. (Fort Washington MD, U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1021",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8618P0394_1900_-NONE-_-NONE- (Red Orange DR generator). Signed 2018-05-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8618P0394_1900_-NONE-_-NONE-/.",
    "USASpending: Red Orange DR generator USD 0.089m. Supports red_orange_dr_generator_89k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 88551; date_signed 2018-05-10.",
)

# === Cycle 1022 ===
row_doc(
    "misc_merida_fence_103k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Mérida NCC perimeter fence and lighting",
    "Mexico",
    "2 Aug 2018: Department of State awards contract 19MX5218C0006 for Mérida OBO NCC SDMP perimeter fence and lighting (PoP Mexico); obligated USD 103,154.36. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "103154.36", "2018-08-02", "2018", "", "",
    "NCC SDMP perimeter fence and lighting, Mérida, Mexico (USASpending description; Mérida program named; site not precisely sourced — lat/lon blank).",
    "usaspending_misc_merida_fence_103k_2018",
    "MERIDA OBO - NCC SDMP, PERIMETER FENCE AND LIGHTING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5218C0006_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1022",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5218C0006_1900_-NONE-_-NONE- (Mérida fence). Signed 2018-08-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5218C0006_1900_-NONE-_-NONE-/.",
    "USASpending: Mérida fence USD 0.103m. Supports misc_merida_fence_103k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 103154.36; date_signed 2018-08-02.",
)

row_doc(
    "misc_dr_roofing_103k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic roofing framework",
    "Dominican Republic",
    "17 Feb 2017: DoD awards contract FA470417P1001 for roofing framework in Dominican Republic; obligated USD 103,068.26. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "103068.26", "2017-02-17", "2017", "", "",
    "Roofing framework, Dominican Republic (USASpending PoP Dominican Republic; site not named — lat/lon blank).",
    "usaspending_misc_dr_roofing_103k_2017",
    "IGF::OT::IGF ROOFING FRAMEWORK IN DOMINICAN REPUBLIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470417P1001_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1022",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA470417P1001_9700_-NONE-_-NONE- (DR roofing). Signed 2017-02-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA470417P1001_9700_-NONE-_-NONE-/.",
    "USASpending: DR roofing USD 0.103m. Supports misc_dr_roofing_103k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 103068.26; date_signed 2017-02-17.",
)

row_doc(
    "inecon_classrooms_102k_2013",
    "infrastructure", "building_materials", "other",
    "Inecon — Colombia classroom construction",
    "Colombia",
    "16 Aug 2013: DoD awards contract W913FT13P0161 to Inecon for construct classrooms (PoP Colombia); obligated USD 102,320.12. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "102320.12", "2013-08-16", "2013", "", "",
    "Classroom construction, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_inecon_classrooms_102k_2013",
    "CONSTRUCT CLASSROOOMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13P0161_9700_-NONE-_-NONE-/",
    "Actor: Inecon S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1022",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT13P0161_9700_-NONE-_-NONE- (Inecon classrooms). Signed 2013-08-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13P0161_9700_-NONE-_-NONE-/.",
    "USASpending: Inecon classrooms USD 0.102m. Supports inecon_classrooms_102k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 102320.12; date_signed 2013-08-16.",
)

row_doc(
    "zenith_jamaica_gate_99k_2026",
    "infrastructure", "building_materials", "us",
    "Zenith Management — Jamaica bamboo slide gate replacement",
    "Jamaica",
    "17 Sep 2026: Department of State awards contract 19JM3726C0004 to Zenith Management Consultant for engineering replace bamboo slide gate (PoP Jamaica); obligated USD 98,742.12. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "98742.12", "2026-09-17", "2026", "", "",
    "Bamboo slide gate replacement, Jamaica (USASpending PoP Jamaica; site not named — lat/lon blank).",
    "usaspending_zenith_jamaica_gate_99k_2026",
    "FAC7901RSTRENGINEERINGREPLACE BAMBOO SLIDE GATE8000",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3726C0004_1900_-NONE-_-NONE-/",
    "Actor: Zenith Management Consultant LLC (Eastchester NY, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1022",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3726C0004_1900_-NONE-_-NONE- (Zenith Jamaica gate). Signed 2026-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3726C0004_1900_-NONE-_-NONE-/.",
    "USASpending: Zenith Jamaica gate USD 0.099m. Supports zenith_jamaica_gate_99k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 98742.12; date_signed 2026-09-17.",
)

row_doc(
    "jay_henges_booth_96k_2010",
    "infrastructure", "building_materials", "us",
    "Jay Henges Enterprises — Honduras portable trailer-mounted guard booth",
    "Honduras",
    "29 Jul 2010: DoD awards contract W912QM10P0055 to Jay Henges Enterprises for portable trailer-mounted guard booth (PoP Honduras); obligated USD 95,805.20. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "95805.2", "2010-07-29", "2010", "", "",
    "Portable trailer-mounted guard booth, Honduras (USASpending PoP Honduras; site not named — lat/lon blank).",
    "usaspending_jay_henges_booth_96k_2010",
    "PORTABLE TRAILER MOUNTED GUARD BOOTH",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM10P0055_9700_-NONE-_-NONE-/",
    "Actor: Jay Henges Enterprises Inc. (Earth City MO, U.S.-incorporated) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1022",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM10P0055_9700_-NONE-_-NONE- (Jay Henges booth). Signed 2010-07-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM10P0055_9700_-NONE-_-NONE-/.",
    "USASpending: Jay Henges booth USD 0.096m. Supports jay_henges_booth_96k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 95805.2; date_signed 2010-07-29.",
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
    print(f"cycles1020-1022 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
