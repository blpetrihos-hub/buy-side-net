#!/usr/bin/env python3
"""Cycles 1005–1007: USASpending LatAm CapEx residual (~USD0.12–0.18m).

Seeds: 20262005–20262007. Thin top-up dry.
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

# === Cycle 1005 ===
row_doc(
    "beachfront_bahamas_facilities_179k_2018",
    "infrastructure", "building_materials", "other",
    "Beachfront Equities — Bahamas conference/meeting/admin facilities",
    "Bahamas",
    "31 May 2018: DoD awards contract W912CL18P0803 to Beachfront Equities for conference, meeting, and admin facilities (PoP Bahamas); obligated USD 178,610.93. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "178610.93", "2018-05-31", "2018", "", "",
    "Conference/meeting/admin facilities, Bahamas (USASpending PoP Bahamas; site not named — lat/lon blank).",
    "usaspending_beachfront_bahamas_facilities_179k_2018",
    "CONFERENCE, MEETING,&ADMIN FACILITIES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL18P0803_9700_-NONE-_-NONE-/",
    "Actor: Beachfront Equities Ltd. (Bahamas) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1005",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL18P0803_9700_-NONE-_-NONE- (Beachfront Bahamas facilities). Signed 2018-05-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL18P0803_9700_-NONE-_-NONE-/.",
    "USASpending: Beachfront Bahamas facilities USD 0.179m. Supports beachfront_bahamas_facilities_179k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 178610.93; date_signed 2018-05-31.",
)

row_doc(
    "misc_argentina_obc_domes_164k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina OBC acrylic domes and walkway roof",
    "Argentina",
    "27 Sep 2017: Department of State awards contract SAR20017M0838 for replacement of acrylic domes and walkway roof at OBC (PoP Argentina); obligated USD 163,785.66. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "163785.66", "2017-09-27", "2017", "", "",
    "OBC acrylic domes and walkway roof replacement, Argentina (USASpending PoP Argentina; site not named — lat/lon blank).",
    "usaspending_misc_argentina_obc_domes_164k_2017",
    "IGF::OT::IGF REPLACEMENT OF ACRYLIC DOMES AND WALKWAY ROOF OBC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20017M0838_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1005",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20017M0838_1900_-NONE-_-NONE- (Argentina OBC domes). Signed 2017-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20017M0838_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina OBC domes USD 0.164m. Supports misc_argentina_obc_domes_164k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 163785.66; date_signed 2017-09-27.",
)

row_doc(
    "seobra_macarena_water_162k_2013",
    "resources", "water", "other",
    "SEOBRA — La Macarena water system upgrades",
    "Colombia",
    "22 Aug 2013: USACE awards task order 0002 under W9127813D0009 to Servicios y Obras SEOBRA for water system upgrades La Macarena, Colombia; obligated USD 161,941. CapEx face = award obligation.",
    "161941", "2013-08-22", "2013", "2.180", "-73.780",
    "Water system upgrades, La Macarena, Meta, Colombia (USASpending description).",
    "usaspending_seobra_macarena_water_162k_2013",
    "IGF::OT::IGF WATER SYSTEM UPGRADES LA MACARENA, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127813D0009_9700/",
    "Actor: Servicios y Obras SEOBRA S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1005",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127813D0009_9700 (SEOBRA Macarena water). Signed 2013-08-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127813D0009_9700/.",
    "USASpending: SEOBRA Macarena water USD 0.162m. Supports seobra_macarena_water_162k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 161941; date_signed 2013-08-22.",
)

row_doc(
    "eterna_covered_storage_160k_2017",
    "infrastructure", "building_materials", "other",
    "Eterna — El Salvador covered storage facility",
    "El Salvador",
    "28 Sep 2017: USACE awards task order W9127817F0452 to Empresa de Construcción y Transporte Eterna for covered storage facility (PoP El Salvador); obligated USD 159,999.99. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "159999.99", "2017-09-28", "2017", "", "",
    "Covered storage facility, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_eterna_covered_storage_160k_2017",
    "IGF::OT::IGF COVERED STORAGE FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0452_9700_W9127816D0102_9700/",
    "Actor: Empresa de Construcción y Transporte Eterna S.A. de C.V. (San Pedro Sula) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1005",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0452_9700_W9127816D0102_9700 (Eterna covered storage). Signed 2017-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0452_9700_W9127816D0102_9700/.",
    "USASpending: Eterna covered storage USD 0.160m. Supports eterna_covered_storage_160k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 159999.99; date_signed 2017-09-28.",
)

row_doc(
    "proksol_von_humboldt_clinic_160k_2010",
    "infrastructure", "building_materials", "other",
    "Proksol — Von Humboldt clinic San Alejandro Peru",
    "Peru",
    "30 Sep 2010: USACE awards task order 0002 under W9127809D0078 to Proksol for D/B Von Humboldt clinic, San Alejandro, Peru; obligated USD 159,768.49. CapEx face = award obligation.",
    "159768.49", "2010-09-30", "2010", "-8.830", "-74.720",
    "Von Humboldt clinic, San Alejandro, Ucayali, Peru (USASpending description; approximate).",
    "usaspending_proksol_von_humboldt_clinic_160k_2010",
    "D/B  VON HUMBODLT CLINIC, SAN ALEJANDRO, PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127809D0078_9700/",
    "Actor: Proksol SAS (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1005",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0002_9700_W9127809D0078_9700 (Proksol Von Humboldt clinic). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0002_9700_W9127809D0078_9700/.",
    "USASpending: Proksol Von Humboldt clinic USD 0.160m. Supports proksol_von_humboldt_clinic_160k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 159768.49; date_signed 2010-09-30.",
)


# === Cycle 1006 ===
row_doc(
    "misc_santa_marta_rapel_159k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Santa Marta rapel tower",
    "Colombia",
    "11 Jul 2012: Department of State awards contract SCO15012CN011 for construction of a rapel tower for Santa Marta; obligated USD 158,826.12. CapEx face = award obligation. Recipient redacted.",
    "158826.12", "2012-07-11", "2012", "11.240", "-74.200",
    "Rapel tower, Santa Marta, Colombia (USASpending description).",
    "usaspending_misc_santa_marta_rapel_159k_2012",
    "CONSTRUCTION OF A RAPEL TOWER FOR SANTA MARTA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012CN011_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1006",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15012CN011_1900_-NONE-_-NONE- (Santa Marta rapel tower). Signed 2012-07-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012CN011_1900_-NONE-_-NONE-/.",
    "USASpending: Santa Marta rapel tower USD 0.159m. Supports misc_santa_marta_rapel_159k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 158826.12; date_signed 2012-07-11.",
)

row_doc(
    "dice_bci_handrail_157k_2021",
    "infrastructure", "building_materials", "other",
    "Design Installation and Consulting — STRI BCI handrail replacement",
    "Panama",
    "26 Aug 2021: Smithsonian awards contract 33330221CF0010409 to Design Installation and Consulting for replace handrail at STRI Barro Colorado Island; obligated USD 156,780.50. CapEx face = award obligation.",
    "156780.50", "2021-08-26", "2021", "9.165", "-79.838",
    "Handrail replacement, STRI Barro Colorado Island, Panama (USASpending / Smithsonian).",
    "usaspending_dice_bci_handrail_157k_2021",
    "TO FURNISH SERVICE, LABOR, TRANSPORT AND MATERIAL FOR REPLACE HANDRAIL AT STRI BARRO ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010409_3300_-NONE-_-NONE-/",
    "Actor: Design Installation and Consulting Engineers (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1006",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330221CF0010409_3300_-NONE-_-NONE- (DICE BCI handrail). Signed 2021-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010409_3300_-NONE-_-NONE-/.",
    "USASpending: DICE BCI handrail USD 0.157m. Supports dice_bci_handrail_157k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 156780.50; date_signed 2021-08-26.",
)

row_doc(
    "misc_bahamas_cmr_roof_156k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas CMR roof replacement",
    "Bahamas",
    "21 Jun 2017: Department of State awards contract SBF50017C0007 for CMR roof replacement (PoP Bahamas); obligated USD 156,358.75. CapEx face = award obligation. Recipient redacted.",
    "156358.75", "2017-06-21", "2017", "25.078", "-77.345",
    "CMR roof replacement, Bahamas (USASpending PoP Bahamas; Nassau approximate).",
    "usaspending_misc_bahamas_cmr_roof_156k_2017",
    "IGF::OT::IGF CMR ROOF REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017C0007_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1006",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50017C0007_1900_-NONE-_-NONE- (Bahamas CMR roof). Signed 2017-06-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50017C0007_1900_-NONE-_-NONE-/.",
    "USASpending: Bahamas CMR roof USD 0.156m. Supports misc_bahamas_cmr_roof_156k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 156358.75; date_signed 2017-06-21.",
)

row_doc(
    "misc_ecuador_ziba_electrical_156k_2026",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Ecuador ZIBA electrical distribution and backup upgrade",
    "Ecuador",
    "17 Sep 2026: Department of State awards contract 19EC7526C0007 for FAC-7482-ZIBA electrical distribution and backup upgrade (PoP Ecuador); obligated USD 155,709.23. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "155709.23", "2026-09-17", "2026", "", "",
    "ZIBA electrical distribution and backup upgrade, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_ziba_electrical_156k_2026",
    "FAC-7482-ZIBA-ELECTRICAL DISTRIBUTION AND BACKUP UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7526C0007_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1006",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7526C0007_1900_-NONE-_-NONE- (Ecuador ZIBA electrical). Signed 2026-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7526C0007_1900_-NONE-_-NONE-/.",
    "USASpending: Ecuador ZIBA electrical USD 0.156m. Supports misc_ecuador_ziba_electrical_156k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 155709.23; date_signed 2026-09-17.",
)

row_doc(
    "misc_guatemala_nec_fence_156k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guatemala NEC fence",
    "Guatemala",
    "26 Sep 2016: Department of State awards contract SGT50016C0011 for Guatemala ICASS NEC fence; obligated USD 155,513.66. CapEx face = award obligation. Recipient redacted.",
    "155513.66", "2016-09-26", "2016", "14.635", "-90.507",
    "NEC fence, Guatemala City, Guatemala (USASpending description; Guatemala City approximate).",
    "usaspending_misc_guatemala_nec_fence_156k_2016",
    "GUATEMALA - ICASS - NEC FENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50016C0011_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1006",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50016C0011_1900_-NONE-_-NONE- (Guatemala NEC fence). Signed 2016-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50016C0011_1900_-NONE-_-NONE-/.",
    "USASpending: Guatemala NEC fence USD 0.156m. Supports misc_guatemala_nec_fence_156k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 155513.66; date_signed 2016-09-26.",
)


# === Cycle 1007 ===
row_doc(
    "psi_cucuta_twall_155k_2017",
    "infrastructure", "building_materials", "us",
    "Project Services International — Cúcuta concrete defense T-wall",
    "Colombia",
    "15 Aug 2017: Department of State awards contract SCO15017C0012 to Project Services International for INL Bogotá concrete defense T-wall for Cúcuta; obligated USD 154,984.18. CapEx face = award obligation.",
    "154984.18", "2017-08-15", "2017", "7.890", "-72.510",
    "Concrete defense T-wall, Cúcuta, Colombia (USASpending description).",
    "usaspending_psi_cucuta_twall_155k_2017",
    "IGF::OT::IGF INL BOGOTA- CONCRETE DEFENSE T-WALL FOR CUCUTA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15017C0012_1900_-NONE-_-NONE-/",
    "Actor: Project Services International Corporation (Florida, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1007",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15017C0012_1900_-NONE-_-NONE- (PSI Cúcuta T-wall). Signed 2017-08-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15017C0012_1900_-NONE-_-NONE-/.",
    "USASpending: PSI Cúcuta T-wall USD 0.155m. Supports psi_cucuta_twall_155k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 154984.18; date_signed 2017-08-15.",
)

row_doc(
    "proksol_zurite_school_155k_2010",
    "infrastructure", "building_materials", "other",
    "Proksol — Zurite school Cusco Peru",
    "Peru",
    "30 Sep 2010: USACE awards task order 0001 under W9127809D0078 to Proksol for D/B Zurite school, Cusco, Peru; obligated USD 154,728.64. CapEx face = award obligation.",
    "154728.64", "2010-09-30", "2010", "-13.670", "-72.270",
    "Zurite school, Cusco Region, Peru (USASpending description).",
    "usaspending_proksol_zurite_school_155k_2010",
    "D/B ZURITE SCHOOL, CUSCO, PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127809D0078_9700/",
    "Actor: Proksol SAS (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1007",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127809D0078_9700 (Proksol Zurite school). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127809D0078_9700/.",
    "USASpending: Proksol Zurite school USD 0.155m. Supports proksol_zurite_school_155k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 154728.64; date_signed 2010-09-30.",
)

row_doc(
    "dictores_obstacle_154k_2025",
    "infrastructure", "building_materials", "other",
    "Constructora Dictores — El Salvador obstacle course",
    "El Salvador",
    "14 Mar 2025: DoD awards contract H9228125C0002 to Constructora Dictores for construct obstacle course (PoP El Salvador); obligated USD 154,031.96. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "154031.96", "2025-03-14", "2025", "", "",
    "Obstacle course construction, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_dictores_obstacle_154k_2025",
    "CONSTRUCT OBSTACLE COURSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125C0002_9700_-NONE-_-NONE-/",
    "Actor: Constructora Dictores, S.A. de C.V. (La Libertad Sur) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1007",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_H9228125C0002_9700_-NONE-_-NONE- (Dictores obstacle course). Signed 2025-03-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125C0002_9700_-NONE-_-NONE-/.",
    "USASpending: Dictores obstacle course USD 0.154m. Supports dictores_obstacle_154k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 154031.96; date_signed 2025-03-14.",
)

row_doc(
    "hermosa_belize_family_care_127k_2011",
    "infrastructure", "building_materials", "us",
    "Hermosa Construction — Belize family care building",
    "Belize",
    "19 Sep 2011: DoD awards contract W912CL11C0034 to Hermosa Construction Group for construct family care building (PoP Belize); obligated USD 127,267.50. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "127267.50", "2011-09-19", "2011", "", "",
    "Family care building, Belize (USASpending PoP Belize; site not named — lat/lon blank).",
    "usaspending_hermosa_belize_family_care_127k_2011",
    "CONSTRUCT FAMILY CARE BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0034_9700_-NONE-_-NONE-/",
    "Actor: Hermosa Construction Group, LLC (Atlanta GA, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1007",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL11C0034_9700_-NONE-_-NONE- (Hermosa Belize family care). Signed 2011-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL11C0034_9700_-NONE-_-NONE-/.",
    "USASpending: Hermosa Belize family care USD 0.127m. Supports hermosa_belize_family_care_127k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 127267.50; date_signed 2011-09-19.",
)

row_doc(
    "ml_engineering_kingston_hvac_117k_2011",
    "infrastructure", "building_materials", "us",
    "ML Engineering Associates — Kingston embassy HVAC installation",
    "Jamaica",
    "16 Sep 2011: Department of State awards task order SAQMMA11F3419 to ML Engineering Associates for installation of HVAC units at U.S. Embassy Kingston, Jamaica; obligated USD 117,121.90. CapEx face = award obligation.",
    "117121.90", "2011-09-16", "2011", "18.015", "-76.797",
    "HVAC unit installation, U.S. Embassy Kingston, Jamaica (USASpending description).",
    "usaspending_ml_engineering_kingston_hvac_117k_2011",
    "INSTALLATION OF HVAC UNITS AT THE U.S. EMBASSY IN KINGSTON, JAMAICA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3419_1900_SALMEC07D0001_1900/",
    "Actor: ML Engineering Associates, Inc. (Culpeper VA, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1007",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F3419_1900_SALMEC07D0001_1900 (ML Engineering Kingston HVAC). Signed 2011-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3419_1900_SALMEC07D0001_1900/.",
    "USASpending: ML Engineering Kingston HVAC USD 0.117m. Supports ml_engineering_kingston_hvac_117k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 117121.90; date_signed 2011-09-16.",
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
    print(f"cycles1005-1007 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
