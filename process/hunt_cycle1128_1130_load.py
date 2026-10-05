#!/usr/bin/env python3
"""Cycles 1128–1130: USASpending LatAm CapEx residual (~USD0.021–0.036m).

Seeds: 20262128–20262130. Thin top-up dry. Includes Haiti transformers.
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


# === Cycle 1128 (seed 20262128) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_belize_metal_door_screen_21k_2024",
    "infrastructure", "building_materials", "us",
    'Norshield Security Products — Belize metal door screen frame for international embassies',
    "Belize",
    '3 Dec 2024: Department of State awards contract 19AQMM25P0128 to Norshield Security Products, LLC for metal door screen frame etc. for international embassies (PoP Belize); obligated USD 21,290. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.',
    "21290", "2024-12-03", "2024", "", "",
    'Metal door screen frame for international embassies, Belize (USASpending description; embassy not named — lat/lon blank).',
    "usaspending_norshield_belize_metal_door_screen_21k_2024",
    'METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0128_1900_-NONE-_-NONE-/",
    'Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1128",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0128_1900_-NONE-_-NONE- (norshield_belize_metal_door_screen_21k_2024). Signed 2024-12-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0128_1900_-NONE-_-NONE-/.',
    'USASpending: norshield_belize_metal_door_screen_21k_2024 USD 0.021m. Supports norshield_belize_metal_door_screen_21k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 21290; date_signed 2024-12-03.',
)
row_doc(
    "united_commercial_mexico_chancery_drinking_fountains_21k_2016",
    "resources", "water", "us",
    'United Commercial Supply — Mexico chancery drinking fountains replacement',
    "Mexico",
    '25 May 2016: Department of State awards contract SMX53016F0543 to United Commercial Supply LLC for replace chancery drinking fountains (PoP Mexico); obligated USD 21,150. CapEx face = award obligation. Exact chancery unnamed — lat/lon blank.',
    "21150", "2016-05-25", "2016", "", "",
    'Replace chancery drinking fountains, Mexico (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_united_commercial_mexico_chancery_drinking_fountains_21k_2016",
    'MEX/FAC/7901.C/REPLACE CHANCERY DRINKING FOUNTAINS *URGENT*  IGF::OT::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53016F0543_1900_GS21F0041U_4730/",
    'Actor: United Commercial Supply LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1128",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53016F0543_1900_GS21F0041U_4730 (united_commercial_mexico_chancery_drinking_fountains_21k_2016). Signed 2016-05-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53016F0543_1900_GS21F0041U_4730/.',
    'USASpending: united_commercial_mexico_chancery_drinking_fountains_21k_2016 USD 0.021m. Supports united_commercial_mexico_chancery_drinking_fountains_21k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 21150; date_signed 2016-05-25.',
)
row_doc(
    "misc_mexico_domestic_pump_bowl_replacement_36k_2014",
    "resources", "water", "other",
    'Miscellaneous foreign awardees — Mexico domestic pump bowl replacement prop R1003',
    "Mexico",
    '14 Aug 2014: Department of State awards contract SMX11514M0427 for replacement of domestic pump bowl prop R1003 (PoP Mexico); obligated USD 35,934.73. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "35934.73", "2014-08-14", "2014", "", "",
    'Replacement of domestic pump bowl prop R1003, Mexico (USASpending description; property code named, site coords not stated — lat/lon blank).',
    "usaspending_misc_mexico_domestic_pump_bowl_replacement_36k_2014",
    '7901-REPLACEMENT OF DOMESTIC PUMP BOWL PROP R1003 IGF::OT::IGF - FOR OTHER FUNCTIONS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11514M0427_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.',
    "hunt_cycle1128",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11514M0427_1900_-NONE-_-NONE- (misc_mexico_domestic_pump_bowl_replacement_36k_2014). Signed 2014-08-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11514M0427_1900_-NONE-_-NONE-/.',
    'USASpending: misc_mexico_domestic_pump_bowl_replacement_36k_2014 USD 0.036m. Supports misc_mexico_domestic_pump_bowl_replacement_36k_2014.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35934.73; date_signed 2014-08-14.',
)
row_doc(
    "misc_colombia_gso_bandf_cubicles_renovation_36k_2015",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Colombia cubicles for GSO/BANDF offices renovation',
    "Colombia",
    '29 Sep 2015: Department of State awards contract SCO20015M1577 for cubicles for GSO/BANDF offices renovation (PoP Colombia); obligated USD 35,921.08. CapEx face = award obligation. Exact offices unnamed — lat/lon blank.',
    "35921.08", "2015-09-29", "2015", "", "",
    'Cubicles for GSO/BANDF offices renovation, Colombia (USASpending description; offices named, site coords not stated — lat/lon blank).',
    "usaspending_misc_colombia_gso_bandf_cubicles_renovation_36k_2015",
    'EOFY2015_CUBICLES FOR GSO/BANDF OFFICES RENOVATIONIGF::CL::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20015M1577_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1128",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20015M1577_1900_-NONE-_-NONE- (misc_colombia_gso_bandf_cubicles_renovation_36k_2015). Signed 2015-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20015M1577_1900_-NONE-_-NONE-/.',
    'USASpending: misc_colombia_gso_bandf_cubicles_renovation_36k_2015 USD 0.036m. Supports misc_colombia_gso_bandf_cubicles_renovation_36k_2015.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35921.08; date_signed 2015-09-29.',
)
row_doc(
    "misc_uruguay_stgls_mylar_film_install_36k_2012",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Uruguay supply and installation of mylar film at STGLS',
    "Uruguay",
    '25 Sep 2012: Department of State awards contract SUY60012M0346 for supply and installation of mylar film at STGLS (PoP Uruguay); obligated USD 35,880. CapEx face = award obligation. Exact STGLS unnamed — lat/lon blank.',
    "35880", "2012-09-25", "2012", "", "",
    'Supply and installation of mylar film at STGLS, Uruguay (USASpending description; STGLS named, site coords not stated — lat/lon blank).',
    "usaspending_misc_uruguay_stgls_mylar_film_install_36k_2012",
    'SUPPLY AND INSTALLATION OF MYLAR FILM AT STGLS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60012M0346_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1128",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SUY60012M0346_1900_-NONE-_-NONE- (misc_uruguay_stgls_mylar_film_install_36k_2012). Signed 2012-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SUY60012M0346_1900_-NONE-_-NONE-/.',
    'USASpending: misc_uruguay_stgls_mylar_film_install_36k_2012 USD 0.036m. Supports misc_uruguay_stgls_mylar_film_install_36k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35880; date_signed 2012-09-25.',
)

# === Cycle 1129 (seed 20262129) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "ross_technology_suriname_metal_door_screen_21k_2021",
    "infrastructure", "building_materials", "us",
    'Ross Technology — Suriname metal door screen for international embassies',
    "Suriname",
    '8 Jun 2021: Department of State awards contract 19AQMM21P0796 to Ross Technology Company for metal door screen etc. (PoP Suriname); obligated USD 20,966. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.',
    "20966", "2021-06-08", "2021", "", "",
    'Metal door screen etc., Suriname (USASpending description; embassy not named — lat/lon blank).',
    "usaspending_ross_technology_suriname_metal_door_screen_21k_2021",
    'METAL DOOR SCREEN ETC.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21P0796_1900_-NONE-_-NONE-/",
    'Actor: Ross Technology Company (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1129",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21P0796_1900_-NONE-_-NONE- (ross_technology_suriname_metal_door_screen_21k_2021). Signed 2021-06-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21P0796_1900_-NONE-_-NONE-/.',
    'USASpending: ross_technology_suriname_metal_door_screen_21k_2021 USD 0.021m. Supports ross_technology_suriname_metal_door_screen_21k_2021.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 20966; date_signed 2021-06-08.',
)
row_doc(
    "elmeco_haiti_cmr_step_down_transformers_install_21k_2023",
    "energy", "power_plants_grid", "us",
    'Elmeco Engineering — Haiti CMR step down transformers installation',
    "Haiti",
    '3 Mar 2023: Department of State awards contract 19HA7023P0472 to Elmeco Engineering, Inc. for step down transformers installation at CMR (PoP Haiti); obligated USD 20,854.54. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.',
    "20854.54", "2023-03-03", "2023", "", "",
    'Step down transformers installation at CMR, Haiti (USASpending description; CMR named, site coords not stated — lat/lon blank).',
    "usaspending_elmeco_haiti_cmr_step_down_transformers_install_21k_2023",
    'FAC- STEP DOWN TRANSFORMERS INSTALLATION AT CMR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P0472_1900_-NONE-_-NONE-/",
    'Actor: Elmeco Engineering, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Weight under-covered Haiti.',
    "hunt_cycle1129",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7023P0472_1900_-NONE-_-NONE- (elmeco_haiti_cmr_step_down_transformers_install_21k_2023). Signed 2023-03-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P0472_1900_-NONE-_-NONE-/.',
    'USASpending: elmeco_haiti_cmr_step_down_transformers_install_21k_2023 USD 0.021m. Supports elmeco_haiti_cmr_step_down_transformers_install_21k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 20854.54; date_signed 2023-03-03.',
)
row_doc(
    "wkl_arquitectos_panama_cmr_sound_system_install_36k_2017",
    "infrastructure", "building_materials", "other",
    'W.K.L. Arquitectos — Panama CMR sound system installation',
    "Panama",
    '18 Sep 2017: Department of State awards contract SPM07017M0998 to W.K.L. Arquitectos S.A. for CMR sound system installation (PoP Panama); obligated USD 35,820. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.',
    "35820", "2017-09-18", "2017", "", "",
    'CMR sound system installation, Panama (USASpending description; CMR named, site coords not stated — lat/lon blank).',
    "usaspending_wkl_arquitectos_panama_cmr_sound_system_install_36k_2017",
    'CMR SOUND SYSTEM INSTALLATION (SOLICITATION SPM07017Q0088)IGF::OT::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07017M0998_1900_-NONE-_-NONE-/",
    'Actor: W.K.L. Arquitectos S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1129",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07017M0998_1900_-NONE-_-NONE- (wkl_arquitectos_panama_cmr_sound_system_install_36k_2017). Signed 2017-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07017M0998_1900_-NONE-_-NONE-/.',
    'USASpending: wkl_arquitectos_panama_cmr_sound_system_install_36k_2017 USD 0.036m. Supports wkl_arquitectos_panama_cmr_sound_system_install_36k_2017.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35820; date_signed 2017-09-18.',
)
row_doc(
    "misc_dominican_republic_chancery_pool_fence_36k_2022",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Dominican Republic chancery pool fence FWP 307',
    "Dominican Republic",
    '31 May 2022: Department of State awards contract 19DR8622P0518 for chancery pool fence FWP 307 (PoP Dominican Republic); obligated USD 35,781.86. CapEx face = award obligation. Exact chancery unnamed — lat/lon blank.',
    "35781.86", "2022-05-31", "2022", "", "",
    'Chancery pool fence FWP 307, Dominican Republic (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_misc_dominican_republic_chancery_pool_fence_36k_2022",
    'CHANCERY POOL FENCE- FWP#307',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622P0518_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1129",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8622P0518_1900_-NONE-_-NONE- (misc_dominican_republic_chancery_pool_fence_36k_2022). Signed 2022-05-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622P0518_1900_-NONE-_-NONE-/.',
    'USASpending: misc_dominican_republic_chancery_pool_fence_36k_2022 USD 0.036m. Supports misc_dominican_republic_chancery_pool_fence_36k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35781.86; date_signed 2022-05-31.',
)
row_doc(
    "misc_ecuador_reflective_roof_painting_fwp205_36k_2021",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Ecuador reflective roof painting FWP 205',
    "Ecuador",
    '21 Jul 2021: Department of State awards contract 19EC7521P0869 for reflective roof painting Bolanos FWP 205 (PoP Ecuador); obligated USD 35,771.52. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "35771.52", "2021-07-21", "2021", "", "",
    'Reflective roof painting FWP 205, Ecuador (USASpending description; FWP named, site coords not stated — lat/lon blank).',
    "usaspending_misc_ecuador_reflective_roof_painting_fwp205_36k_2021",
    'REFLECTIVE ROOF PAINTING PR9994987 BOLANOS 7901-L-FWP 205',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7521P0869_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1129",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7521P0869_1900_-NONE-_-NONE- (misc_ecuador_reflective_roof_painting_fwp205_36k_2021). Signed 2021-07-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7521P0869_1900_-NONE-_-NONE-/.',
    'USASpending: misc_ecuador_reflective_roof_painting_fwp205_36k_2021 USD 0.036m. Supports misc_ecuador_reflective_roof_painting_fwp205_36k_2021.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35771.52; date_signed 2021-07-21.',
)

# === Cycle 1130 (seed 20262130) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "american_classic_guatemala_cmr_concrete_roof_sealer_21k_2016",
    "infrastructure", "building_materials", "us",
    'American Classic Construction — Guatemala CMR concrete roof sealer',
    "Guatemala",
    '8 Aug 2016: Department of State awards contract SGT50016M0716 to American Classic Construction Inc. for CMR concrete roof sealer (PoP Guatemala); obligated USD 20,768.9. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.',
    "20768.9", "2016-08-08", "2016", "", "",
    'CMR concrete roof sealer, Guatemala (USASpending description; CMR named, site coords not stated — lat/lon blank).',
    "usaspending_american_classic_guatemala_cmr_concrete_roof_sealer_21k_2016",
    'IGF::CL::IGF FAC - CMR CONCRETE ROOF SEALER - OS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50016M0716_1900_-NONE-_-NONE-/",
    'Actor: American Classic Construction Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1130",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50016M0716_1900_-NONE-_-NONE- (american_classic_guatemala_cmr_concrete_roof_sealer_21k_2016). Signed 2016-08-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50016M0716_1900_-NONE-_-NONE-/.',
    'USASpending: american_classic_guatemala_cmr_concrete_roof_sealer_21k_2016 USD 0.021m. Supports american_classic_guatemala_cmr_concrete_roof_sealer_21k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 20768.9; date_signed 2016-08-08.',
)
row_doc(
    "cummins_guyana_ressouvenir_replacement_generator_21k_2015",
    "energy", "power_plants_grid", "us",
    'Cummins Power Generation — Guyana Ressouvenir 2A Area K replacement generator',
    "Guyana",
    '23 Jan 2015: Department of State awards contract SGY20015M0101 to Cummins Power Generation Inc. for replacement generator for 2A Area K Le Ressouvenir (PoP Guyana); obligated USD 20,698.17. CapEx face = award obligation. Le Ressouvenir named; site coords not stated — lat/lon blank.',
    "20698.17", "2015-01-23", "2015", "", "",
    'Replacement generator for 2A Area K Le Ressouvenir, Guyana (USASpending description; Le Ressouvenir named, site coords not stated — lat/lon blank).',
    "usaspending_cummins_guyana_ressouvenir_replacement_generator_21k_2015",
    'REPLACEMENT GENERATOR FOR 2A AREA K LE RESOUVENIR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20015M0101_1900_-NONE-_-NONE-/",
    'Actor: Cummins Power Generation Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1130",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGY20015M0101_1900_-NONE-_-NONE- (cummins_guyana_ressouvenir_replacement_generator_21k_2015). Signed 2015-01-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20015M0101_1900_-NONE-_-NONE-/.',
    'USASpending: cummins_guyana_ressouvenir_replacement_generator_21k_2015 USD 0.021m. Supports cummins_guyana_ressouvenir_replacement_generator_21k_2015.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 20698.17; date_signed 2015-01-23.',
)
row_doc(
    "misc_colombia_cmr_makeready_painting_civil_work_36k_2017",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Colombia CMR makeready exterior/interior painting and minor civil work',
    "Colombia",
    '28 Sep 2017: Department of State awards contract SCO20017C0006 for ext/int painting and minor civil work for CMR makeready X2002 (PoP Colombia); obligated USD 35,747.62. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.',
    "35747.62", "2017-09-28", "2017", "", "",
    'Ext/int painting and minor civil work for CMR makeready X2002, Colombia (USASpending description; CMR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_colombia_cmr_makeready_painting_civil_work_36k_2017",
    'IGF::OT::IGF PR6787854: EXT/INT PAINTING&MINOR CIVIL WORK FOR CMR MAKEREADY X2002',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20017C0006_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1130",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20017C0006_1900_-NONE-_-NONE- (misc_colombia_cmr_makeready_painting_civil_work_36k_2017). Signed 2017-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20017C0006_1900_-NONE-_-NONE-/.',
    'USASpending: misc_colombia_cmr_makeready_painting_civil_work_36k_2017 USD 0.036m. Supports misc_colombia_cmr_makeready_painting_civil_work_36k_2017.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35747.62; date_signed 2017-09-28.',
)
row_doc(
    "misc_honduras_usaid_voltage_regulators_install_36k_2014",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Honduras supply of 3 voltage regulators to be installed in USAID compound',
    "Honduras",
    '26 Aug 2014: USAID awards contract AID522O1400064 for supply of 3 voltage regulators to be installed in the USAID Honduras compound (PoP Honduras); obligated USD 35,700. CapEx face = award obligation. Exact compound unnamed — lat/lon blank.',
    "35700", "2014-08-26", "2014", "", "",
    'Supply of 3 voltage regulators to be installed in USAID Honduras compound (USASpending description; compound not named — lat/lon blank).',
    "usaspending_misc_honduras_usaid_voltage_regulators_install_36k_2014",
    'SUPPLY OF 3 VOLTAGE REGULATORS TO BE INSTALLED IN THE USAID HONDURAS COMPOUND.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1400064_7200_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1130",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID522O1400064_7200_-NONE-_-NONE- (misc_honduras_usaid_voltage_regulators_install_36k_2014). Signed 2014-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1400064_7200_-NONE-_-NONE-/.',
    'USASpending: misc_honduras_usaid_voltage_regulators_install_36k_2014 USD 0.036m. Supports misc_honduras_usaid_voltage_regulators_install_36k_2014.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35700; date_signed 2014-08-26.',
)
row_doc(
    "misc_bahamas_chancery_compound_exterior_painting_36k_2011",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Bahamas chancery compound exterior painting',
    "Bahamas",
    '30 Sep 2011: Department of State awards contract SBF50011M0513 for chancery compound exterior painting (PoP Bahamas); obligated USD 35,606.68. CapEx face = award obligation. Exact compound unnamed — lat/lon blank.',
    "35606.68", "2011-09-30", "2011", "", "",
    'Chancery compound exterior painting, Bahamas (USASpending description; compound not named — lat/lon blank).',
    "usaspending_misc_bahamas_chancery_compound_exterior_painting_36k_2011",
    'C-CHANCERY COMPOUND EXTERIOR PAINTING',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50011M0513_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1130",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50011M0513_1900_-NONE-_-NONE- (misc_bahamas_chancery_compound_exterior_painting_36k_2011). Signed 2011-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50011M0513_1900_-NONE-_-NONE-/.',
    'USASpending: misc_bahamas_chancery_compound_exterior_painting_36k_2011 USD 0.036m. Supports misc_bahamas_chancery_compound_exterior_painting_36k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35606.68; date_signed 2011-09-30.',
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
