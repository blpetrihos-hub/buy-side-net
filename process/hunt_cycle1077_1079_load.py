#!/usr/bin/env python3
"""Cycles 1077–1079: USASpending LatAm CapEx residual (~USD0.050–0.061m).

Seeds: 20262077–20262079. Thin top-up dry.
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


# === Cycle 1077 (seed 20262077) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "maga_mexico_warehouse_facilities_54k_2025",
    "infrastructure", "building_materials", "us",
    "Maga Forwarding — Mexico warehouse facilities",
    "Mexico",
    "8 Dec 2025: Department of State awards contract 19MX6126C0002 to Maga Forwarding LLC for warehouse facilities (PoP Mexico); obligated USD 54,400. CapEx face = award obligation. Exact warehouse unnamed — lat/lon blank.",
    "54400", "2025-12-08", "2025", "", "",
    "Warehouse facilities, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_maga_mexico_warehouse_facilities_54k_2025",
    "WAREHOUSE FACILITIES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6126C0002_1900_-NONE-_-NONE-/",
    "Actor: Maga Forwarding LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1077",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX6126C0002_1900_-NONE-_-NONE- (Maga Mexico warehouse). Signed 2025-12-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6126C0002_1900_-NONE-_-NONE-/.",
    "USASpending: Maga Mexico warehouse USD 0.054m. Supports maga_mexico_warehouse_facilities_54k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 54400; date_signed 2025-12-08.",
)

row_doc(
    "carolina_water_mexico_guadalajara_water_plant_53k_2024",
    "resources", "water", "us",
    "Carolina Water Specialties — Mexico Guadalajara domestic water plant",
    "Mexico",
    "29 Aug 2024: Department of State awards contract 19MX3024P0466 to Carolina Water Specialties LLC for NCC domestic water plant FY24 (PoP Mexico); obligated USD 53,000. CapEx face = award obligation. Exact Guadalajara site unnamed — lat/lon blank.",
    "53000", "2024-08-29", "2024", "", "",
    "Domestic water plant, Guadalajara/NCC, Mexico (USASpending description; Guadalajara named via GDL code, site coords not stated — lat/lon blank).",
    "usaspending_carolina_water_mexico_guadalajara_water_plant_53k_2024",
    "GDL-FAC-7901-PMSC13-NCC-DOMESTIC WATER PLANT-FY24",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX3024P0466_1900_-NONE-_-NONE-/",
    "Actor: Carolina Water Specialties LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1077",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX3024P0466_1900_-NONE-_-NONE- (Carolina Water Guadalajara plant). Signed 2024-08-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX3024P0466_1900_-NONE-_-NONE-/.",
    "USASpending: Carolina Water Guadalajara plant USD 0.053m. Supports carolina_water_mexico_guadalajara_water_plant_53k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 53000; date_signed 2024-08-29.",
)

row_doc(
    "misc_argentina_chiller_2_repair_61k_2022",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Argentina chiller 2 repair",
    "Argentina",
    "19 Aug 2022: Department of State awards contract 19AR2022P1015 for FAC chiller 2 repair (PoP Argentina); obligated USD 60,691.99. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "60691.99", "2022-08-19", "2022", "", "",
    "Chiller 2 repair, Argentina (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_argentina_chiller_2_repair_61k_2022",
    "FAC - CHILLER 2 REPAIR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2022P1015_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1077",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2022P1015_1900_-NONE-_-NONE- (Argentina chiller 2 repair). Signed 2022-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2022P1015_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina chiller 2 repair USD 0.061m. Supports misc_argentina_chiller_2_repair_61k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60691.99; date_signed 2022-08-19.",
)

row_doc(
    "misc_guatemala_master_bathroom_remodel_61k_2026",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guatemala master bathroom remodel",
    "Guatemala",
    "24 Sep 2026: Department of State awards contract 19GT5026C0019 for master bathroom remodel (PoP Guatemala); obligated USD 60,687. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "60687", "2026-09-24", "2026", "", "",
    "Master bathroom remodel, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guatemala_master_bathroom_remodel_61k_2026",
    "MASTER BATHROOM REMODEL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5026C0019_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1077",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GT5026C0019_1900_-NONE-_-NONE- (Guatemala master bathroom). Signed 2026-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5026C0019_1900_-NONE-_-NONE-/.",
    "USASpending: Guatemala master bathroom USD 0.061m. Supports misc_guatemala_master_bathroom_remodel_61k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60687; date_signed 2026-09-24.",
)

row_doc(
    "misc_brazil_loading_dock_roof_60k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil MANDR loading dock roof project",
    "Brazil",
    "19 Sep 2011: Department of State awards contract SBR93011C0009 for MANDR 7901 loading dock roof project (PoP Brazil); obligated USD 60,400.23. CapEx face = award obligation. Exact dock unnamed — lat/lon blank.",
    "60400.23", "2011-09-19", "2011", "", "",
    "Loading dock roof project, Brazil (USASpending description; dock not named — lat/lon blank).",
    "usaspending_misc_brazil_loading_dock_roof_60k_2011",
    "MANDR 7901 - LOADING DOCK ROOF PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93011C0009_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1077",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR93011C0009_1900_-NONE-_-NONE- (Brazil loading dock roof). Signed 2011-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93011C0009_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil loading dock roof USD 0.060m. Supports misc_brazil_loading_dock_roof_60k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60400.23; date_signed 2011-09-19.",
)

# === Cycle 1078 (seed 20262078) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "hcs_honduras_osc_renovations_53k_2016",
    "infrastructure", "building_materials", "us",
    "HCS Group — Honduras FY-16 OSC renovations projects",
    "Honduras",
    "12 May 2016: Department of Defense awards task order 0009 under IDV W9127814D0057 to HCS Group, P.C. for FY-16 OSC renovations projects in HND (PoP Honduras); obligated USD 52,727.65. CapEx face = award obligation. Exact OSC sites unnamed — lat/lon blank.",
    "52727.65", "2016-05-12", "2016", "", "",
    "FY-16 OSC renovations projects, Honduras (USASpending description; OSC named, site coords not stated — lat/lon blank).",
    "usaspending_hcs_honduras_osc_renovations_53k_2016",
    "IGF::OT::IGF FY-16 OSC RENOVATIONS PROJECTS IN HND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127814D0057_9700/",
    "Actor: HCS Group, P.C. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1078",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0009_9700_W9127814D0057_9700 (HCS Honduras OSC renovations). Signed 2016-05-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0009_9700_W9127814D0057_9700/.",
    "USASpending: HCS Honduras OSC renovations USD 0.053m. Supports hcs_honduras_osc_renovations_53k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 52727.65; date_signed 2016-05-12.",
)

row_doc(
    "seal_haiti_cas_roof_survey_52k_2021",
    "infrastructure", "engineering_epc", "us",
    "Seal Engineering — Haiti CAS housing compound roof survey and assessment",
    "Haiti",
    "26 Jul 2021: Department of State awards order 19AQMM21F2831 to Seal Engineering, Inc. for roof survey, assessment, and report services for CAS housing compound in Port au Prince (PoP Haiti); obligated USD 52,456.52. CapEx face = award obligation. Exact compound coords not stated — lat/lon blank.",
    "52456.52", "2021-07-26", "2021", "", "",
    "Roof survey, assessment, and report for CAS housing compound, Port au Prince, Haiti (USASpending description; Port au Prince named, coords not stated — lat/lon blank).",
    "usaspending_seal_haiti_cas_roof_survey_52k_2021",
    "ROOF SURVEY, ASSESSMENT, AND REPORT SERVICES FOR CAS HOUSING COMPOUND IN PORT AU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F2831_1900_19AQMM19D0048_1900/",
    "Actor: Seal Engineering, Inc. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1078",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21F2831_1900_19AQMM19D0048_1900 (Seal Haiti CAS roof survey). Signed 2021-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F2831_1900_19AQMM19D0048_1900/.",
    "USASpending: Seal Haiti CAS roof survey USD 0.052m. Supports seal_haiti_cas_roof_survey_52k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 52456.52; date_signed 2021-07-26.",
)

row_doc(
    "misc_dr_compressed_air_system_60k_2022",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic SPX shops compressed air system replacement",
    "Dominican Republic",
    "27 Sep 2022: Department of State awards contract 19DR8622P1848 for compressed air system replacement for SPX shops (PoP Dominican Republic); obligated USD 60,311.55. CapEx face = award obligation. Exact shops unnamed — lat/lon blank.",
    "60311.55", "2022-09-27", "2022", "", "",
    "Compressed air system replacement for SPX shops, Dominican Republic (USASpending description; shops not named — lat/lon blank).",
    "usaspending_misc_dr_compressed_air_system_60k_2022",
    "OBO7901 - COMPRESSED AIR SYSTEM REPLACEMENT FOR SPX SHOPS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622P1848_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1078",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8622P1848_1900_-NONE-_-NONE- (DR compressed air system). Signed 2022-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622P1848_1900_-NONE-_-NONE-/.",
    "USASpending: DR compressed air system USD 0.060m. Supports misc_dr_compressed_air_system_60k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60311.55; date_signed 2022-09-27.",
)

row_doc(
    "huracan_peru_ancon_access_roads_60k_2010",
    "infrastructure", "bridges_roads", "other",
    "Huracan Inversiones — Peru Ancon naval base access roads and sidewalks D/B",
    "Peru",
    "19 Apr 2010: Department of Defense awards contract W9127810P0215 to Huracan Inversiones E.I.R.L. for D/B access roads and sidewalks at Ancon naval base (PoP Peru); obligated USD 60,300.87. CapEx face = award obligation. Exact alignment unnamed — lat/lon blank.",
    "60300.87", "2010-04-19", "2010", "", "",
    "D/B access roads and sidewalks at Ancon naval base, Peru (USASpending description; Ancon named, alignment coords not stated — lat/lon blank).",
    "usaspending_huracan_peru_ancon_access_roads_60k_2010",
    "D/B ACCESS ROADS & SIDEWALKS AT ANCON NAVAL BASE, PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0215_9700_-NONE-_-NONE-/",
    "Actor: Huracan Inversiones E.I.R.L. (Peru) — other. Official USASpending Award API. Shuffle bridges_roads. Holdover closed.",
    "hunt_cycle1078",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127810P0215_9700_-NONE-_-NONE- (Huracan Peru Ancon roads). Signed 2010-04-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0215_9700_-NONE-_-NONE-/.",
    "USASpending: Huracan Peru Ancon roads USD 0.060m. Supports huracan_peru_ancon_access_roads_60k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60300.87; date_signed 2010-04-19.",
)

row_doc(
    "estruconsult_costa_rica_oij_incinerator_ae_61k_2020",
    "infrastructure", "engineering_epc", "other",
    "Estruconsult — Costa Rica OIJ incinerator A&E services",
    "Costa Rica",
    "21 Feb 2020: Department of State awards order 19CS8020F0171 to Estruconsult SA for OIJ incinerator A&E services (PoP Costa Rica); obligated USD 60,709.31. CapEx face = award obligation. Exact incinerator site unnamed — lat/lon blank.",
    "60709.31", "2020-02-21", "2020", "", "",
    "OIJ incinerator A&E services, Costa Rica (USASpending description; incinerator not named — lat/lon blank).",
    "usaspending_estruconsult_costa_rica_oij_incinerator_ae_61k_2020",
    "INL 1930.0 TO#4, OIJ INCINERATOR, A&E SERVICES, 19D0009",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8020F0171_1900_19CS8019D0009_1900/",
    "Actor: Estruconsult SA (Costa Rica) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1078",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8020F0171_1900_19CS8019D0009_1900 (Estruconsult OIJ incinerator A&E). Signed 2020-02-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8020F0171_1900_19CS8019D0009_1900/.",
    "USASpending: Estruconsult OIJ incinerator A&E USD 0.061m. Supports estruconsult_costa_rica_oij_incinerator_ae_61k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60709.31; date_signed 2020-02-21.",
)

# === Cycle 1079 (seed 20262079) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "mckinney_panama_gamboa_lab_permit_drawings_52k_2011",
    "infrastructure", "engineering_epc", "us",
    "McKinney and Company — Panama Gamboa laboratory facilities replacement permit drawings",
    "Panama",
    "26 Apr 2011: Smithsonian Tropical Research Institute awards work order F11CW10311 to McKinney and Company, Inc. for supplemental permit drawings for replacement of Gamboa laboratory facilities (PoP Panama); obligated USD 51,926.18. CapEx face = award obligation. Exact lab site unnamed — lat/lon blank.",
    "51926.18", "2011-04-26", "2011", "", "",
    "Supplemental permit drawings for replacement of Gamboa laboratory facilities, Panama (USASpending description; Gamboa named, site coords not stated — lat/lon blank).",
    "usaspending_mckinney_panama_gamboa_lab_permit_drawings_52k_2011",
    "WORK ORDER NO. 6 AGAINST SMITHSONIAN'S ID/IQ CONTRACT F06CC10332 FOR SUPPLEMENTAL PERMIT DRAWINGS FOR REPLACEMENT OF GAMBOA LABORATORY FACILITIES AT SMITHSONIAN TROPICAL RESEARCH INSTITUTE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F11CW10311_3300_F06CC10332_3300/",
    "Actor: McKinney and Company, Inc. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1079",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F11CW10311_3300_F06CC10332_3300 (McKinney Gamboa lab drawings). Signed 2011-04-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F11CW10311_3300_F06CC10332_3300/.",
    "USASpending: McKinney Gamboa lab drawings USD 0.052m. Supports mckinney_panama_gamboa_lab_permit_drawings_52k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 51926.18; date_signed 2011-04-26.",
)

row_doc(
    "jj_honduras_paint_apron_52k_2011",
    "infrastructure", "bridges_roads", "us",
    "J & J Maintenance — Honduras paint apron",
    "Honduras",
    "3 Aug 2011: Department of Defense awards contract W9127811P0280 to J & J Maintenance Inc for paint apron (PoP Honduras); obligated USD 51,876.94. CapEx face = award obligation. Exact apron unnamed — lat/lon blank.",
    "51876.94", "2011-08-03", "2011", "", "",
    "Paint apron, Honduras (USASpending description; apron not named — lat/lon blank).",
    "usaspending_jj_honduras_paint_apron_52k_2011",
    "PAINT APRON",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0280_9700_-NONE-_-NONE-/",
    "Actor: J & J Maintenance Inc (U.S.) — us. Official USASpending Award API. Shuffle bridges_roads; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1079",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811P0280_9700_-NONE-_-NONE- (J&J Honduras paint apron). Signed 2011-08-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0280_9700_-NONE-_-NONE-/.",
    "USASpending: J&J Honduras paint apron USD 0.052m. Supports jj_honduras_paint_apron_52k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 51876.94; date_signed 2011-08-03.",
)

row_doc(
    "misc_costa_rica_msgr_security_cameras_61k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Costa Rica MSGR security cameras",
    "Costa Rica",
    "15 Jul 2021: Department of State awards contract 19CS8021P0911 for security cameras for MSGR (PoP Costa Rica); obligated USD 60,653.06. CapEx face = award obligation. Exact MSGR site unnamed — lat/lon blank.",
    "60653.06", "2021-07-15", "2021", "", "",
    "Security cameras for MSGR, Costa Rica (USASpending description; MSGR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_msgr_security_cameras_61k_2021",
    "SECURITY CAMERAS FOR MSGR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8021P0911_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1079",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8021P0911_1900_-NONE-_-NONE- (Costa Rica MSGR cameras). Signed 2021-07-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8021P0911_1900_-NONE-_-NONE-/.",
    "USASpending: Costa Rica MSGR cameras USD 0.061m. Supports misc_costa_rica_msgr_security_cameras_61k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60653.06; date_signed 2021-07-15.",
)

row_doc(
    "misc_el_salvador_sidewalk_phase4_60k_2015",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — El Salvador sidewalk renovation project phase 4",
    "El Salvador",
    "31 Aug 2015: Department of State awards contract SES60015M0950 for sidewalk renovation project phase 4 (PoP El Salvador); obligated USD 60,060. CapEx face = award obligation. Exact sidewalks unnamed — lat/lon blank.",
    "60060", "2015-08-31", "2015", "", "",
    "Sidewalk renovation project phase 4, El Salvador (USASpending description; sidewalks not named — lat/lon blank).",
    "usaspending_misc_el_salvador_sidewalk_phase4_60k_2015",
    "IGF::OT::IGF 7901- SIDEWALK RENOVATION PROJECT PHASE 4",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60015M0950_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1079",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60015M0950_1900_-NONE-_-NONE- (El Salvador sidewalk phase 4). Signed 2015-08-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60015M0950_1900_-NONE-_-NONE-/.",
    "USASpending: El Salvador sidewalk phase 4 USD 0.060m. Supports misc_el_salvador_sidewalk_phase4_60k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60060; date_signed 2015-08-31.",
)

row_doc(
    "servin_venezuela_perimeter_fence_pathway_60k_2018",
    "infrastructure", "building_materials", "other",
    "Ingenieria Servin — Venezuela pathway for the perimeter fence",
    "Venezuela",
    "15 Aug 2018: Department of State awards contract 19VE3018C0003 to Ingenieria Servin C.A. for pathway for the perimeter fence (PoP Venezuela); obligated USD 59,923.28. CapEx face = award obligation. Exact fence path unnamed — lat/lon blank.",
    "59923.28", "2018-08-15", "2018", "", "",
    "Pathway for the perimeter fence, Venezuela (USASpending description; path not named — lat/lon blank).",
    "usaspending_servin_venezuela_perimeter_fence_pathway_60k_2018",
    "FAC: PATHWAY FOR THE PERIMETER FENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19VE3018C0003_1900_-NONE-_-NONE-/",
    "Actor: Ingenieria Servin C.A. (Venezuela) — other. Official USASpending Award API. Shuffle building_materials. Weight under-covered Venezuela.",
    "hunt_cycle1079",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19VE3018C0003_1900_-NONE-_-NONE- (Servin Venezuela perimeter fence pathway). Signed 2018-08-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19VE3018C0003_1900_-NONE-_-NONE-/.",
    "USASpending: Servin Venezuela perimeter fence pathway USD 0.060m. Supports servin_venezuela_perimeter_fence_pathway_60k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59923.28; date_signed 2018-08-15.",
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
        w.writeheader()
        w.writerows(rows)

    EVID.mkdir(parents=True, exist_ok=True)
    for row, ev, _bib in ITEMS:
        path = EVID / f"{row['id']}.json"
        path.write_text(json.dumps(ev, indent=2) + "\n", encoding="utf-8")

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
            bib_docs.append(bib)
            bib_by_id[sid] = bib
    BIB.write_text(
        yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000),
        encoding="utf-8",
    )
    print(f"loaded {len(ITEMS)} rows")


if __name__ == "__main__":
    main()
