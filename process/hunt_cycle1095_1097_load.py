#!/usr/bin/env python3
"""Cycles 1095–1097: USASpending LatAm CapEx residual (~USD0.032–0.056m).

Seeds: 20262095–20262097. Thin top-up dry.
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


# === Cycle 1095 (seed 20262095) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "caprice_brazil_water_fountains_filters_56k_2018",
    "infrastructure", "building_materials", "us",
    'Caprice Electronics — Brazil Brasilia FAC water fountains and filter elements',
    "Brazil",
    '19 Sep 2018: Department of State awards contract 19BR2518P1461 to Caprice Electronics, Inc for BSB-FAC water fountains and filter elements (PoP Brazil); obligated USD 55,628.10. CapEx face = award obligation. Exact fountain sites unnamed — lat/lon blank.',
    "55628.10", "2018-09-19", "2018", "", "",
    'Water fountains and filter elements, Brasilia FAC, Brazil (USASpending description; BSB named, site coords not stated — lat/lon blank).',
    "usaspending_caprice_brazil_water_fountains_filters_56k_2018",
    'EOFY-2018/BSB-FAC - WATER FOUNTAINS AND FILTER ELEMENTS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2518P1461_1900_-NONE-_-NONE-/",
    'Actor: Caprice Electronics, Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1095",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2518P1461_1900_-NONE-_-NONE- (caprice_brazil_water_fountains_filters_56k_2018). Signed 2018-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2518P1461_1900_-NONE-_-NONE-/.',
    'USASpending: caprice_brazil_water_fountains_filters_56k_2018 USD 0.056m. Supports caprice_brazil_water_fountains_filters_56k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55628.10; date_signed 2018-09-19.',
)
row_doc(
    "dfs_colombia_night_lights_generators_40k_2015",
    "energy", "power_plants_grid", "us",
    'DFS Technical Services — Colombia night lights and generators',
    "Colombia",
    '18 Jun 2015: Department of Defense awards contract W913FT15P0134 to DFS Technical Services LLC for night lights and generators (PoP Colombia); obligated USD 39,828.17. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.',
    "39828.17", "2015-06-18", "2015", "", "",
    'Night lights and generators, Colombia (USASpending description; sites not named — lat/lon blank).',
    "usaspending_dfs_colombia_night_lights_generators_40k_2015",
    'IGF::OT::IGF NIGHT LIGHTS AND GENERATORS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT15P0134_9700_-NONE-_-NONE-/",
    'Actor: DFS Technical Services LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1095",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT15P0134_9700_-NONE-_-NONE- (dfs_colombia_night_lights_generators_40k_2015). Signed 2015-06-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT15P0134_9700_-NONE-_-NONE-/.',
    'USASpending: dfs_colombia_night_lights_generators_40k_2015 USD 0.040m. Supports dfs_colombia_night_lights_generators_40k_2015.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 39828.17; date_signed 2015-06-18.',
)
row_doc(
    "akj_mexico_musset_bathroom_finishes_55k_2021",
    "infrastructure", "building_materials", "other",
    'Servicios AKJ — Mexico Musset bathroom finishes replacement',
    "Mexico",
    '13 May 2021: Department of State awards contract 19MX5321C0007 to Servicios AKJ, S.A de C.V to replace Musset bathroom finishes (PoP Mexico); obligated USD 54,831.91. CapEx face = award obligation. Exact Musset property unnamed — lat/lon blank.',
    "54831.91", "2021-05-13", "2021", "", "",
    'Replace Musset bathroom finishes, Mexico (USASpending description; Musset named, site coords not stated — lat/lon blank).',
    "usaspending_akj_mexico_musset_bathroom_finishes_55k_2021",
    'MEX-FAC-7903-REPLACE MUSSET BATHROOM FINISHES',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5321C0007_1900_-NONE-_-NONE-/",
    'Actor: Servicios AKJ, S.A de C.V (Mexico) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1095",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5321C0007_1900_-NONE-_-NONE- (akj_mexico_musset_bathroom_finishes_55k_2021). Signed 2021-05-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5321C0007_1900_-NONE-_-NONE-/.',
    'USASpending: akj_mexico_musset_bathroom_finishes_55k_2021 USD 0.055m. Supports akj_mexico_musset_bathroom_finishes_55k_2021.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 54831.91; date_signed 2021-05-13.',
)
row_doc(
    "secon_honduras_choluteca_morgue_concrete_55k_2026",
    "infrastructure", "building_materials", "other",
    'Servicios Energia Construccion y Telecomunicaciones — Honduras Choluteca morgue concrete blocks and pavers',
    "Honduras",
    '17 Sep 2026: Department of State awards contract 19H08026P0422 to Servicios Energia Construccion y Telecomunicaciones SA de CV for INL/CARSI concrete materials (blocks and pavers) Choluteca morgue (PoP Honduras); obligated USD 54,910.63. CapEx face = award obligation. Exact morgue site unnamed — lat/lon blank.',
    "54910.63", "2026-09-17", "2026", "", "",
    'Concrete materials (blocks and pavers) Choluteca morgue, Honduras (USASpending description; Choluteca named, site coords not stated — lat/lon blank).',
    "usaspending_secon_honduras_choluteca_morgue_concrete_55k_2026",
    'INL/CARSI: CONCRETE MATERIALS (BLOCKS&PAVERS) CHOLUTECA MORGUE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08026P0422_1900_-NONE-_-NONE-/",
    'Actor: Servicios Energia Construccion y Telecomunicaciones SA de CV (Honduras) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1095",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19H08026P0422_1900_-NONE-_-NONE- (secon_honduras_choluteca_morgue_concrete_55k_2026). Signed 2026-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08026P0422_1900_-NONE-_-NONE-/.',
    'USASpending: secon_honduras_choluteca_morgue_concrete_55k_2026 USD 0.055m. Supports secon_honduras_choluteca_morgue_concrete_55k_2026.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 54910.63; date_signed 2026-09-17.',
)
row_doc(
    "perez_mexico_carpet_gov_prop_1001_54k_2018",
    "infrastructure", "building_materials", "other",
    'Jorge Eduardo Perez Romo — Mexico government property 1001 carpet replacement',
    "Mexico",
    '24 May 2018: Department of State awards contract 19MX1118P0177 to Jorge Eduardo Perez Romo for carpet replace for gov prop 1001 (PoP Mexico); obligated USD 54,140.68. CapEx face = award obligation. Exact property unnamed — lat/lon blank.',
    "54140.68", "2018-05-24", "2018", "", "",
    'Carpet replace for government property 1001, Mexico (USASpending description; property not named — lat/lon blank).',
    "usaspending_perez_mexico_carpet_gov_prop_1001_54k_2018",
    'IGT::OT::IGT CARPET REPLACE FOR GOV PROP 1001',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1118P0177_1900_-NONE-_-NONE-/",
    'Actor: Jorge Eduardo Perez Romo (Mexico) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1095",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX1118P0177_1900_-NONE-_-NONE- (perez_mexico_carpet_gov_prop_1001_54k_2018). Signed 2018-05-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1118P0177_1900_-NONE-_-NONE-/.',
    'USASpending: perez_mexico_carpet_gov_prop_1001_54k_2018 USD 0.054m. Supports perez_mexico_carpet_gov_prop_1001_54k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 54140.68; date_signed 2018-05-24.',
)

# === Cycle 1096 (seed 20262096) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "us_ply_jamaica_warehouse_roof_37k_2010",
    "infrastructure", "building_materials", "us",
    'U.S. Ply — Jamaica materials to repair warehouse roof',
    "Jamaica",
    '15 Mar 2010: Department of State awards order SJM37010F0007 under IDV GS07F0184V to U.S. Ply, Inc. for materials to repair warehouse roof (PoP Jamaica); obligated USD 37,041.54. CapEx face = award obligation. Exact warehouse unnamed — lat/lon blank.',
    "37041.54", "2010-03-15", "2010", "", "",
    'Materials to repair warehouse roof, Jamaica (USASpending description; warehouse not named — lat/lon blank).',
    "usaspending_us_ply_jamaica_warehouse_roof_37k_2010",
    'FM - MATERIALS TO REPAIR WAREHOUSE ROOF (7901)',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37010F0007_1900_GS07F0184V_4730/",
    'Actor: U.S. Ply, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1096",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37010F0007_1900_GS07F0184V_4730 (us_ply_jamaica_warehouse_roof_37k_2010). Signed 2010-03-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37010F0007_1900_GS07F0184V_4730/.',
    'USASpending: us_ply_jamaica_warehouse_roof_37k_2010 USD 0.037m. Supports us_ply_jamaica_warehouse_roof_37k_2010.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37041.54; date_signed 2010-03-15.',
)
row_doc(
    "harden_ecuador_metal_door_screen_36k_2022",
    "infrastructure", "building_materials", "us",
    'Harden Architectural Security Products — Ecuador metal door screen',
    "Ecuador",
    '24 Jun 2022: Department of State awards contract 19AQMM22P0726 to Harden Architectural Security Products, LLC for metal door screen etc. (PoP Ecuador); obligated USD 36,443. CapEx face = award obligation. Exact embassy site unnamed — lat/lon blank.',
    "36443", "2022-06-24", "2022", "", "",
    'Metal door screen etc., Ecuador (USASpending description; site not named — lat/lon blank).',
    "usaspending_harden_ecuador_metal_door_screen_36k_2022",
    'METAL DOOR SCREEN ETC.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0726_1900_-NONE-_-NONE-/",
    'Actor: Harden Architectural Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1096",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22P0726_1900_-NONE-_-NONE- (harden_ecuador_metal_door_screen_36k_2022). Signed 2022-06-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0726_1900_-NONE-_-NONE-/.',
    'USASpending: harden_ecuador_metal_door_screen_36k_2022 USD 0.036m. Supports harden_ecuador_metal_door_screen_36k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36443; date_signed 2022-06-24.',
)
row_doc(
    "misc_colombia_warehouse_mezzanine_53k_2012",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Colombia warehouse reconfiguration mezzanine install',
    "Colombia",
    '27 Sep 2012: Department of State awards contract SCO20012M3353 for warehouse reconfiguration — removal and installation mezzanine (PoP Colombia); obligated USD 52,659.76. CapEx face = award obligation. Exact warehouse unnamed — lat/lon blank.',
    "52659.76", "2012-09-27", "2012", "", "",
    'Warehouse reconfiguration — removal and installation mezzanine, Colombia (USASpending description; warehouse not named — lat/lon blank).',
    "usaspending_misc_colombia_warehouse_mezzanine_53k_2012",
    'IGF::OT::IGF WAREHOUSE RECONFIGURATION - REMOVAL AND INSTALLATION MEZZANINE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012M3353_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1096",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20012M3353_1900_-NONE-_-NONE- (misc_colombia_warehouse_mezzanine_53k_2012). Signed 2012-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012M3353_1900_-NONE-_-NONE-/.',
    'USASpending: misc_colombia_warehouse_mezzanine_53k_2012 USD 0.053m. Supports misc_colombia_warehouse_mezzanine_53k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 52659.76; date_signed 2012-09-27.',
)
row_doc(
    "isobox_panama_shoothouse_materials_54k_2020",
    "infrastructure", "building_materials", "other",
    'Isobox — Panama shoothouse construction materials',
    "Panama",
    '12 Aug 2020: Department of State awards contract 19PM0720P0621 to Isobox Inc for shoothouse construction materials (PoP Panama); obligated USD 53,564.82. CapEx face = award obligation. Exact shoothouse unnamed — lat/lon blank.',
    "53564.82", "2020-08-12", "2020", "", "",
    'Shoothouse construction materials, Panama (USASpending description; site not named — lat/lon blank).',
    "usaspending_isobox_panama_shoothouse_materials_54k_2020",
    'SHOOTHOUSE CONSTRUCTION MATERIALS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0720P0621_1900_-NONE-_-NONE-/",
    'Actor: Isobox Inc (Panama) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1096",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0720P0621_1900_-NONE-_-NONE- (isobox_panama_shoothouse_materials_54k_2020). Signed 2020-08-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0720P0621_1900_-NONE-_-NONE-/.',
    'USASpending: isobox_panama_shoothouse_materials_54k_2020 USD 0.054m. Supports isobox_panama_shoothouse_materials_54k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53564.82; date_signed 2020-08-12.',
)
row_doc(
    "bennys_belize_videolink_fence_catwalk_53k_2018",
    "infrastructure", "building_materials", "other",
    "Benny's Enterprises — Belize Videolink fence, cat walk, electrical",
    "Belize",
    "2 Aug 2018: Department of State awards contract 19BH2018P0270 to Benny's Enterprises Ltd. for Videolink fence, cat walk, electrical (PoP Belize); obligated USD 53,350.14. CapEx face = award obligation. Exact Videolink site unnamed — lat/lon blank.",
    "53350.14", "2018-08-02", "2018", "", "",
    'Videolink fence, cat walk, electrical, Belize (USASpending description; Videolink named, site coords not stated — lat/lon blank).',
    "usaspending_bennys_belize_videolink_fence_catwalk_53k_2018",
    'VIDEOLINK - FENCE, CAT WALK, ELECTRICAL',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BH2018P0270_1900_-NONE-_-NONE-/",
    "Actor: Benny's Enterprises Ltd. (Belize) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1096",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BH2018P0270_1900_-NONE-_-NONE- (bennys_belize_videolink_fence_catwalk_53k_2018). Signed 2018-08-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BH2018P0270_1900_-NONE-_-NONE-/.',
    'USASpending: bennys_belize_videolink_fence_catwalk_53k_2018 USD 0.053m. Supports bennys_belize_videolink_fence_catwalk_53k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53350.14; date_signed 2018-08-02.',
)

# === Cycle 1097 (seed 20262097) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "ace_roof_coatings_mexico_trade_center_waterproof_35k_2013",
    "infrastructure", "building_materials", "us",
    'ACE Roof Coatings — Mexico Trade Center building waterproofing materials',
    "Mexico",
    '23 Jul 2013: Department of State awards contract SMX53013M0986 to ACE Roof Coatings, Inc for materials Trade Center building waterproof (PoP Mexico); obligated USD 34,760.94. CapEx face = award obligation. Exact Trade Center unnamed — lat/lon blank.',
    "34760.94", "2013-07-23", "2013", "", "",
    'Materials Trade Center building waterproof, Mexico (USASpending description; Trade Center named, site coords not stated — lat/lon blank).',
    "usaspending_ace_roof_coatings_mexico_trade_center_waterproof_35k_2013",
    'MEX-FAC 7901.1 / MATERIALS TRADE CENTER BUILDING WATER PROOF IGF::OT::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0986_1900_-NONE-_-NONE-/",
    'Actor: ACE Roof Coatings, Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1097",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53013M0986_1900_-NONE-_-NONE- (ace_roof_coatings_mexico_trade_center_waterproof_35k_2013). Signed 2013-07-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0986_1900_-NONE-_-NONE-/.',
    'USASpending: ace_roof_coatings_mexico_trade_center_waterproof_35k_2013 USD 0.035m. Supports ace_roof_coatings_mexico_trade_center_waterproof_35k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 34760.94; date_signed 2013-07-23.',
)
row_doc(
    "waypoint_honduras_obs_course_materials_36k_2022",
    "infrastructure", "building_materials", "us",
    'Waypoint — Honduras FC2022 construction materials for obstacle course',
    "Honduras",
    '17 Feb 2022: Department of Defense awards order W912QM22F0019 under IDV W912QM18A0008 to Waypoint LLC for FC2022 construction materials — obs. course (PoP Honduras); obligated USD 35,824.89. CapEx face = award obligation. Exact course site unnamed — lat/lon blank.',
    "35824.89", "2022-02-17", "2022", "", "",
    'Construction materials for obstacle course, Honduras (USASpending description; course not named — lat/lon blank).',
    "usaspending_waypoint_honduras_obs_course_materials_36k_2022",
    'FC2022: CONSTRUCTION MATERIALS - OBS. COURSE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM22F0019_9700_W912QM18A0008_9700/",
    'Actor: Waypoint LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1097",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM22F0019_9700_W912QM18A0008_9700 (waypoint_honduras_obs_course_materials_36k_2022). Signed 2022-02-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM22F0019_9700_W912QM18A0008_9700/.',
    'USASpending: waypoint_honduras_obs_course_materials_36k_2022 USD 0.036m. Supports waypoint_honduras_obs_course_materials_36k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35824.89; date_signed 2022-02-17.',
)
row_doc(
    "sumistradora_honduras_gracias_adios_school_55k_2016",
    "infrastructure", "building_materials", "other",
    'Sumistradora de Servicios y Materiales Hernandez — Honduras Gracias a Dios school construction materials',
    "Honduras",
    '18 Jul 2016: Department of Defense awards contract M2710016P7009 to Sumistradora de Servicios y Materiales Hernandez S. de R.L. de C.V. for construction materials for school site in Gracias a Dios Honduras; obligated USD 55,222.75. CapEx face = award obligation. Exact school site unnamed — lat/lon blank.',
    "55222.75", "2016-07-18", "2016", "", "",
    'Construction materials for school site in Gracias a Dios, Honduras (USASpending description; department named, site coords not stated — lat/lon blank).',
    "usaspending_sumistradora_honduras_gracias_adios_school_55k_2016",
    'CONSTRUCTION MATERIALS FOR SCHOOL SITE IN GRACIAS A DIOS HONDURAS.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710016P7009_9700_-NONE-_-NONE-/",
    'Actor: Sumistradora de Servicios y Materiales Hernandez S. de R.L. de C.V. (Honduras) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1097",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_M2710016P7009_9700_-NONE-_-NONE- (sumistradora_honduras_gracias_adios_school_55k_2016). Signed 2016-07-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_M2710016P7009_9700_-NONE-_-NONE-/.',
    'USASpending: sumistradora_honduras_gracias_adios_school_55k_2016 USD 0.055m. Supports sumistradora_honduras_gracias_adios_school_55k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55222.75; date_signed 2016-07-18.',
)
row_doc(
    "arcadia_colombia_acs_installation_davaa_56k_2021",
    "infrastructure", "building_materials", "other",
    'Comercializadora Arcadia — Colombia INL Bogota electrical materials ACS installation DAVAA bases',
    "Colombia",
    '14 Dec 2021: Department of State awards contract 19C01522P0064 to Comercializadora Arcadia SAS for INL Bogota elect materials ACS installation DAVAA bases (PoP Colombia); obligated USD 55,584.10. CapEx face = award obligation. Exact DAVAA bases unnamed — lat/lon blank.',
    "55584.10", "2021-12-14", "2021", "", "",
    'Electrical materials ACS installation DAVAA bases, Bogota, Colombia (USASpending description; DAVAA named, site coords not stated — lat/lon blank).',
    "usaspending_arcadia_colombia_acs_installation_davaa_56k_2021",
    'INL BOGOTA ELECT MATLS ACS INSTALLATION DAVAA BASES',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01522P0064_1900_-NONE-_-NONE-/",
    'Actor: Comercializadora Arcadia SAS (Colombia) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1097",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01522P0064_1900_-NONE-_-NONE- (arcadia_colombia_acs_installation_davaa_56k_2021). Signed 2021-12-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01522P0064_1900_-NONE-_-NONE-/.',
    'USASpending: arcadia_colombia_acs_installation_davaa_56k_2021 USD 0.056m. Supports arcadia_colombia_acs_installation_davaa_56k_2021.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55584.10; date_signed 2021-12-14.',
)
row_doc(
    "misc_dr_k9_academy_ac_installation_56k_2023",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Dominican Republic K9 academy air conditioners including installation',
    "Dominican Republic",
    '11 Jan 2023: Department of State awards contract 19DR8623P0451 for air conditioners including installation at K9 academy (PoP Dominican Republic); obligated USD 56,000. CapEx face = award obligation. Exact academy site unnamed — lat/lon blank.',
    "56000", "2023-01-11", "2023", "", "",
    'Air conditioners including installation — K9 academy, Dominican Republic (USASpending description; academy named, site coords not stated — lat/lon blank).',
    "usaspending_misc_dr_k9_academy_ac_installation_56k_2023",
    'AIR CONDITIONERS INCLUDING INSTALLATION - K9 ACADEMY',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623P0451_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1097",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8623P0451_1900_-NONE-_-NONE- (misc_dr_k9_academy_ac_installation_56k_2023). Signed 2023-01-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623P0451_1900_-NONE-_-NONE-/.',
    'USASpending: misc_dr_k9_academy_ac_installation_56k_2023 USD 0.056m. Supports misc_dr_k9_academy_ac_installation_56k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 56000; date_signed 2023-01-11.',
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
