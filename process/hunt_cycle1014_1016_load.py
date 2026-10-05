#!/usr/bin/env python3
"""Cycles 1014–1016: USASpending LatAm CapEx residual (~USD0.09–0.13m).

Seeds: 20262014–20262016. Thin top-up dry.
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

# === Cycle 1014 ===
row_doc(
    "casco_guatemala_awning_120k_2025",
    "infrastructure", "building_materials", "other",
    "Casco Manejadora — Guatemala official residence patio awning",
    "Guatemala",
    "25 Aug 2025: Department of State awards contract 19GT5025C0007 to Casco Manejadora de Imagen for patio awning construction at official residence (PoP Guatemala); obligated USD 119,914.28. CapEx face = award obligation.",
    "119914.28", "2025-08-25", "2025", "14.635", "-90.507",
    "Patio awning at official residence, Guatemala City, Guatemala (USASpending description; Guatemala City approximate).",
    "usaspending_casco_guatemala_awning_120k_2025",
    "PATIO AWNING CONSTRUCTION AT OFFICIAL RESIDENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5025C0007_1900_-NONE-_-NONE-/",
    "Actor: Casco Manejadora de Imagen S.A. (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1014",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GT5025C0007_1900_-NONE-_-NONE- (Casco Guatemala awning). Signed 2025-08-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5025C0007_1900_-NONE-_-NONE-/.",
    "USASpending: Casco Guatemala awning USD 0.120m. Supports casco_guatemala_awning_120k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 119914.28; date_signed 2025-08-25.",
)

row_doc(
    "wave_hnd_mezzanine_120k_2026",
    "infrastructure", "building_materials", "other",
    "S&A Wave Technology — Honduras INL warehouse prefabricated mezzanine",
    "Honduras",
    "21 May 2026: Department of State awards contract 19H08026P0265 to S&A Wave Technology for INL warehouse pre-fabricated mezzanine (PoP Honduras); obligated USD 119,900. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "119900", "2026-05-21", "2026", "", "",
    "Warehouse prefabricated mezzanine, Honduras (USASpending PoP Honduras; site not named — lat/lon blank).",
    "usaspending_wave_hnd_mezzanine_120k_2026",
    "INL - WAREHOUSE PRE-FABRICATED MEZZANINE - FY26",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08026P0265_1900_-NONE-_-NONE-/",
    "Actor: S&A Wave Technology S. de R.L. (Tegucigalpa) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1014",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19H08026P0265_1900_-NONE-_-NONE- (Wave Honduras mezzanine). Signed 2026-05-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08026P0265_1900_-NONE-_-NONE-/.",
    "USASpending: Wave Honduras mezzanine USD 0.120m. Supports wave_hnd_mezzanine_120k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 119900; date_signed 2026-05-21.",
)

row_doc(
    "misc_colombia_gym_bathrooms_119k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia gym and bathrooms construction",
    "Colombia",
    "5 Apr 2010: Department of State awards contract SCO20010C0004 for gym and bathrooms construction (PoP Colombia); obligated USD 119,041.08. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "119041.08", "2010-04-05", "2010", "", "",
    "Gym and bathrooms construction, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_misc_colombia_gym_bathrooms_119k_2010",
    "GYM  AND BATHROOMS CONSTRUCTION.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20010C0004_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1014",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20010C0004_1900_-NONE-_-NONE- (Colombia gym bathrooms). Signed 2010-04-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20010C0004_1900_-NONE-_-NONE-/.",
    "USASpending: Colombia gym bathrooms USD 0.119m. Supports misc_colombia_gym_bathrooms_119k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 119041.08; date_signed 2010-04-05.",
)

row_doc(
    "romaca_dr_chiller_118k_2017",
    "infrastructure", "building_materials", "other",
    "Romaca Industrial — Dominican Republic CMR chiller upgrade",
    "Dominican Republic",
    "9 Aug 2017: Department of State awards contract SDR86017M0632 to Romaca Industrial for OBO CMR chiller upgrade (PoP Dominican Republic); obligated USD 118,474.73. CapEx face = award obligation.",
    "118474.73", "2017-08-09", "2017", "18.486", "-69.931",
    "CMR chiller upgrade, Santo Domingo, Dominican Republic (USASpending / recipient locality).",
    "usaspending_romaca_dr_chiller_118k_2017",
    "IGF::CL::IGF OBO-CMR'S CHILLER UPGRADE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86017M0632_1900_-NONE-_-NONE-/",
    "Actor: Romaca Industrial, S.A. (Santo Domingo) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1014",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86017M0632_1900_-NONE-_-NONE- (Romaca DR chiller). Signed 2017-08-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86017M0632_1900_-NONE-_-NONE-/.",
    "USASpending: Romaca DR chiller USD 0.118m. Supports romaca_dr_chiller_118k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 118474.73; date_signed 2017-08-09.",
)

row_doc(
    "misc_brasilia_fence_118k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brasília SHIS backyard fence upgrade",
    "Brazil",
    "26 Aug 2025: Department of State awards contract 19BR2525P1094 for backyard fence upgrade at SHIS QL 12-06-19/20 (PoP Brazil/Brasília); obligated USD 117,990.86. CapEx face = award obligation. Recipient redacted.",
    "117990.86", "2025-08-26", "2025", "-15.830", "-47.880",
    "Backyard fence upgrade, SHIS QL 12, Brasília, Brazil (USASpending description).",
    "usaspending_misc_brasilia_fence_118k_2025",
    "BSB|RSO|BACK YARD FENCE UPGRADE AT SHIS QL 12-06-19/20",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2525P1094_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1014",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2525P1094_1900_-NONE-_-NONE- (Brasília fence). Signed 2025-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2525P1094_1900_-NONE-_-NONE-/.",
    "USASpending: Brasília fence USD 0.118m. Supports misc_brasilia_fence_118k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 117990.86; date_signed 2025-08-26.",
)


# === Cycle 1015 ===
row_doc(
    "store_q_panama_fence_117k_2017",
    "infrastructure", "building_materials", "other",
    "Store Q Panama — perimeter fence and front gate replacement",
    "Panama",
    "4 May 2017: DoD awards contract SPM07017M0407 to Store Q Panama for perimeter fence and front gate replacement (PoP Panama); obligated USD 116,999.44. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "116999.44", "2017-05-04", "2017", "", "",
    "Perimeter fence and front gate replacement, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_store_q_panama_fence_117k_2017",
    "PERIMETER FENCE&FRONT GATE REPLACEMENT (SPM07017Q0041)IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07017M0407_1900_-NONE-_-NONE-/",
    "Actor: Store Q Panama S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1015",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07017M0407_1900_-NONE-_-NONE- (Store Q Panama fence). Signed 2017-05-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07017M0407_1900_-NONE-_-NONE-/.",
    "USASpending: Store Q Panama fence USD 0.117m. Supports store_q_panama_fence_117k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 116999.44; date_signed 2017-05-04.",
)

row_doc(
    "misc_ecuador_asphalt_lot_116k_2018",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Ecuador employee parking lot asphalt repair",
    "Ecuador",
    "13 Jul 2018: Department of State awards contract 19EC3018P0435 for asphalt repair employees parking lot (PoP Ecuador); obligated USD 116,262.75. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "116262.75", "2018-07-13", "2018", "", "",
    "Employee parking lot asphalt repair, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_asphalt_lot_116k_2018",
    "IGF::OT::IGF ASPHALT REPAIR EMPLOYEES P. LOT-REPLACES PR7145534",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3018P0435_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1015",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3018P0435_1900_-NONE-_-NONE- (Ecuador asphalt lot). Signed 2018-07-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3018P0435_1900_-NONE-_-NONE-/.",
    "USASpending: Ecuador asphalt lot USD 0.116m. Supports misc_ecuador_asphalt_lot_116k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 116262.75; date_signed 2018-07-13.",
)

row_doc(
    "grupo_azul_electrical_115k_2021",
    "energy", "power_plants_grid", "other",
    "Grupo Azul — El Salvador electrical installation",
    "El Salvador",
    "24 Aug 2021: Department of State awards contract 19ES6021P0729 to Grupo Azul for electrical installation (PoP El Salvador); obligated USD 115,129.09. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "115129.09", "2021-08-24", "2021", "", "",
    "Electrical installation, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_grupo_azul_electrical_115k_2021",
    "ELECTRICAL INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0729_1900_-NONE-_-NONE-/",
    "Actor: Grupo Azul S.A. de C.V. (San Salvador) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1015",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6021P0729_1900_-NONE-_-NONE- (Grupo Azul electrical). Signed 2021-08-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0729_1900_-NONE-_-NONE-/.",
    "USASpending: Grupo Azul electrical USD 0.115m. Supports grupo_azul_electrical_115k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 115129.09; date_signed 2021-08-24.",
)

row_doc(
    "misc_cr_activity_deck_114k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Costa Rica activity deck and parking lot roof",
    "Costa Rica",
    "24 Sep 2014: Department of State awards contract SCS80014C0024 for activity deck and employee parking lot roof project (PoP Costa Rica); obligated USD 113,739.07. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "113739.07", "2014-09-24", "2014", "", "",
    "Activity deck and employee parking lot roof, Costa Rica (USASpending PoP Costa Rica; site not named — lat/lon blank).",
    "usaspending_misc_cr_activity_deck_114k_2014",
    "ACTIVITY DECK AND EMPLOYEE PARKING LOT ROOF PROJECT 2014 IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80014C0024_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1015",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80014C0024_1900_-NONE-_-NONE- (CR activity deck). Signed 2014-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80014C0024_1900_-NONE-_-NONE-/.",
    "USASpending: CR activity deck USD 0.114m. Supports misc_cr_activity_deck_114k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 113739.07; date_signed 2014-09-24.",
)

row_doc(
    "misc_ecuador_handrail_115k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador compound buildings roof handrail",
    "Ecuador",
    "25 Aug 2014: Department of State awards contract SEC75014M0554 for SHEM roof handrail compound buildings (PoP Ecuador); obligated USD 115,077.32. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "115077.32", "2014-08-25", "2014", "", "",
    "Compound buildings roof handrail, Ecuador (USASpending PoP Ecuador; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_handrail_115k_2014",
    "IGF::OT::IGF 1900.0 7901.C L 1/1 SHEM ROOF HANDRAIL COMPOUND BUILDINGS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75014M0554_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1015",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SEC75014M0554_1900_-NONE-_-NONE- (Ecuador handrail). Signed 2014-08-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75014M0554_1900_-NONE-_-NONE-/.",
    "USASpending: Ecuador handrail USD 0.115m. Supports misc_ecuador_handrail_115k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 115077.32; date_signed 2014-08-25.",
)


# === Cycle 1016 ===
row_doc(
    "misc_jamaica_powell_road_109k_2017",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Jamaica Powell Plaza road resurfacing",
    "Jamaica",
    "6 Jun 2017: Department of State awards contract SJM37017C0006 for road resurfacing for Powell Plaza (PoP Jamaica); obligated USD 108,843.75. CapEx face = award obligation. Recipient redacted.",
    "108843.75", "2017-06-06", "2017", "18.015", "-76.797",
    "Road resurfacing, Powell Plaza, Kingston, Jamaica (USASpending description; Kingston approximate).",
    "usaspending_misc_jamaica_powell_road_109k_2017",
    "IGF::OT::IGF FAC - ROAD RESURFACING FOR POWELL PLAZA [7901.3/79851]",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37017C0006_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1016",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37017C0006_1900_-NONE-_-NONE- (Jamaica Powell Plaza road). Signed 2017-06-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37017C0006_1900_-NONE-_-NONE-/.",
    "USASpending: Jamaica Powell Plaza road USD 0.109m. Supports misc_jamaica_powell_road_109k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 108843.75; date_signed 2017-06-06.",
)

row_doc(
    "misc_chile_water_well_107k_2022",
    "resources", "water", "other",
    "Miscellaneous foreign awardees — Chile water well work",
    "Chile",
    "14 Apr 2022: Department of State awards contract 19C18022P0566 for water well work (PoP Chile); obligated USD 106,893.75. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "106893.75", "2022-04-14", "2022", "", "",
    "Water well work, Chile (USASpending PoP Chile; site not named — lat/lon blank).",
    "usaspending_misc_chile_water_well_107k_2022",
    "WATER WELL WORK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18022P0566_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1016",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C18022P0566_1900_-NONE-_-NONE- (Chile water well). Signed 2022-04-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18022P0566_1900_-NONE-_-NONE-/.",
    "USASpending: Chile water well USD 0.107m. Supports misc_chile_water_well_107k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 106893.75; date_signed 2022-04-14.",
)

row_doc(
    "misc_jamaica_powell_roof_103k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Jamaica Powell Plaza lower roof replacement",
    "Jamaica",
    "30 Sep 2020: Department of State awards contract 19JM3720C0007 for P. Plaza lower roof replacement (PoP Jamaica); obligated USD 103,435. CapEx face = award obligation. Recipient redacted.",
    "103435", "2020-09-30", "2020", "18.015", "-76.797",
    "Lower roof replacement, Powell Plaza, Kingston, Jamaica (USASpending description; Kingston approximate).",
    "usaspending_misc_jamaica_powell_roof_103k_2020",
    "FAC - P. PLAZA LOWER ROOF REPLACEMENT  (7903 REST)99851",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3720C0007_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1016",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3720C0007_1900_-NONE-_-NONE- (Jamaica Powell Plaza roof). Signed 2020-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3720C0007_1900_-NONE-_-NONE-/.",
    "USASpending: Jamaica Powell Plaza roof USD 0.103m. Supports misc_jamaica_powell_roof_103k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 103435; date_signed 2020-09-30.",
)

row_doc(
    "misc_argentina_parking_road_133k_2026",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Argentina CHA parking road damages",
    "Argentina",
    "24 Feb 2026: Department of State awards contract 19AR2026C0001 for FAC CHA parking road damages (PoP Argentina); obligated USD 133,053.71. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "133053.71", "2026-02-24", "2026", "", "",
    "CHA parking road damages repair, Argentina (USASpending PoP Argentina; site not named — lat/lon blank).",
    "usaspending_misc_argentina_parking_road_133k_2026",
    "FAC - CHA-PARKING ROAD DAMAGES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2026C0001_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1016",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2026C0001_1900_-NONE-_-NONE- (Argentina parking road). Signed 2026-02-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2026C0001_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina parking road USD 0.133m. Supports misc_argentina_parking_road_133k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 133053.71; date_signed 2026-02-24.",
)

row_doc(
    "gale_paraguay_ncmr_roof_ae_94k_2018",
    "infrastructure", "engineering_epc", "us",
    "Gale Associates — Paraguay NCMR roof A&E design",
    "Paraguay",
    "8 May 2018: Department of State awards contract 19PA1018C0003 to Gale Associates for NCMR roof AE design work (PoP Paraguay); obligated USD 93,749. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "93749", "2018-05-08", "2018", "", "",
    "NCMR roof A&E design, Paraguay (USASpending PoP Paraguay; site not named — lat/lon blank).",
    "usaspending_gale_paraguay_ncmr_roof_ae_94k_2018",
    "NCMR ROOF AE DESIGN WORK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1018C0003_1900_-NONE-_-NONE-/",
    "Actor: Gale Associates, Inc. (Towson MD, U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1016",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PA1018C0003_1900_-NONE-_-NONE- (Gale Paraguay NCMR roof A&E). Signed 2018-05-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1018C0003_1900_-NONE-_-NONE-/.",
    "USASpending: Gale Paraguay NCMR roof A&E USD 0.094m. Supports gale_paraguay_ncmr_roof_ae_94k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 93749; date_signed 2018-05-08.",
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
    print(f"cycles1014-1016 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
