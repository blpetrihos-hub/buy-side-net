#!/usr/bin/env python3
"""Cycles 951–953: USASpending LatAm CapEx residual (housing, chillers, bridges, NEC power).

Seeds: 20261951–20261953. Thin top-up dry (balsa/nickel/fission_smr).
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


# === Cycle 951 ===
row_doc(
    "acc_haiti_housing_94p4m_2012",
    "infrastructure", "building_materials", "us",
    "ACC Construction-McKnight JV — Haiti design/build housing units",
    "Haiti",
    "29 Sep 2012: Department of State awards contract SAQMMA12C0265 to ACC Construction-McKnight Joint Venture for design/build of housing units (PoP Haiti); obligated USD 94,411,281. CapEx face = award obligation.",
    "94411281", "2012-09-29", "2012", "18.540", "-72.339",
    "Design/build housing units, Haiti (USASpending PoP Haiti; Port-au-Prince pin).",
    "usaspending_acc_haiti_housing_94p4m_2012",
    "DESIGN/BUILD OF HOUSING UNITS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12C0265_1900_-NONE-_-NONE-/",
    "Actor: ACC Construction-McKnight JV (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle951",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12C0265_1900_-NONE-_-NONE- (ACC Haiti housing). Signed 2012-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12C0265_1900_-NONE-_-NONE-/.",
    "USASpending: ACC Haiti housing USD 94.411m. Supports acc_haiti_housing_94p4m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 94411281; date_signed 2012-09-29.",
)

row_doc(
    "thor_haiti_750_houses_17p6m_2012",
    "infrastructure", "building_materials", "us",
    "Thor Construction — Haiti 750 house units",
    "Haiti",
    "26 Apr 2012: USAID awards contract AID521C1200004 to Thor Construction to construct 750 house units (PoP Haiti); obligated USD 17,579,482.24. CapEx face = award obligation.",
    "17579482.24", "2012-04-26", "2012", "18.540", "-72.339",
    "750 house units construction, Haiti (USASpending PoP Haiti; Port-au-Prince pin).",
    "usaspending_thor_haiti_750_houses_17p6m_2012",
    "THE PURPOSE OF THIS CONTRACT IS TO   CONSTRUCT 750 HOUSE UNITS AT THE QUALITY SPECIFIED IN THE ATTACHED CONSTRUCTION PLANS AND SPECIFICATIONS, ON TIME AND WITHIN BUDGET.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1200004_7200_-NONE-_-NONE-/",
    "Actor: Thor Construction (U.S.) under USAID — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle951",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521C1200004_7200_-NONE-_-NONE- (Thor Haiti 750 houses). Signed 2012-04-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1200004_7200_-NONE-_-NONE-/.",
    "USASpending: Thor Haiti 750 houses USD 17.579m. Supports thor_haiti_750_houses_17p6m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 17579482.24; date_signed 2012-04-26.",
)

row_doc(
    "trison_georgetown_chiller_7p80m_2024",
    "infrastructure", "building_materials", "us",
    "Trison Construction — Georgetown chiller replacement",
    "Guyana",
    "27 Sep 2024: Department of State awards task order 19AQMM24F2527 to Trison Construction for Georgetown Guyana chiller replacement; obligated USD 7,799,566. CapEx face = award obligation. Distinct from trison_georgetown_p2.",
    "7799566", "2024-09-27", "2024", "6.801", "-58.155",
    "Chiller replacement, Georgetown, Guyana (USASpending PoP Guyana).",
    "usaspending_trison_georgetown_chiller_7p80m_2024",
    "GEORGETOWN GUYANA CHILLER REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2527_1900_19AQMM22D0066_1900/",
    "Actor: Trison Construction (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle951",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24F2527_1900_19AQMM22D0066_1900 (Trison Georgetown chiller). Signed 2024-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2527_1900_19AQMM22D0066_1900/.",
    "USASpending: Trison Georgetown chiller USD 7.800m. Supports trison_georgetown_chiller_7p80m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7799566; date_signed 2024-09-27.",
)

row_doc(
    "cem_gatun_lake_piers_6p16m_2014",
    "infrastructure", "port_ownership", "other",
    "Construcciones Electromecánicas — Gatún Lake elevation piers/heliport",
    "Panama",
    "24 Dec 2014: Panama Canal / Smithsonian-linked award F15CW10093 to Construcciones Electromecánicas for Gatún Lake elevation project (sheet piles, backfill, new piers, heliport & game warden building); obligated USD 6,159,444.73. CapEx face = award obligation.",
    "6159444.73", "2014-12-24", "2014", "9.250", "-79.920",
    "Gatún Lake elevation piers/heliport, Panama (USASpending PoP Panama; Gatún Lake pin).",
    "usaspending_cem_gatun_lake_piers_6p16m_2014",
    "GATUN LAKE ELEVATION PROJECT.SHEET PILES, BACKFILL, NEW PIERS, HELIPORT&GAME WARDEN BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F15CW10093_3300_F0436CC10292_3300/",
    "Actor: Construcciones Electromecánicas (Panama) — other. Official USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle951",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F15CW10093_3300_F0436CC10292_3300 (CEM Gatún Lake piers). Signed 2014-12-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F15CW10093_3300_F0436CC10292_3300/.",
    "USASpending: CEM Gatún Lake piers USD 6.159m. Supports cem_gatun_lake_piers_6p16m_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6159444.73; date_signed 2014-12-24.",
)

row_doc(
    "cfe_nec_mexico_city_electrical_5p33m_2020",
    "infrastructure", "power_plants_grid", "other",
    "CFE Distribución — NEC Mexico City design/build electrical connection",
    "Mexico",
    "16 Dec 2020: Department of State awards contract 19GE5021C0002 to CFE Distribución for design/build electrical connection at New Embassy Compound Mexico City; obligated USD 5,326,053.88. CapEx face = award obligation.",
    "5326053.88", "2020-12-16", "2020", "19.433", "-99.133",
    "NEC electrical connection, Mexico City, Mexico (USASpending PoP Mexico).",
    "usaspending_cfe_nec_mexico_city_electrical_5p33m_2020",
    "DB ELECTRICAL CONNECTION NEC MEXICO CITY MEXICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0002_1900_-NONE-_-NONE-/",
    "Actor: CFE Distribución (Mexico) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle951",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5021C0002_1900_-NONE-_-NONE- (CFE NEC Mexico City electrical). Signed 2020-12-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0002_1900_-NONE-_-NONE-/.",
    "USASpending: CFE NEC Mexico City electrical USD 5.326m. Supports cfe_nec_mexico_city_electrical_5p33m_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5326053.88; date_signed 2020-12-16.",
)

# === Cycle 952 ===
row_doc(
    "lakeshore_ennery_bridge_5p00m_2010",
    "infrastructure", "bridges_roads", "us",
    "Lakeshore Engineering — Ennery River bridge replacement",
    "Haiti",
    "29 Jul 2010: USAID awards contract AID521C001000020 to Lakeshore Engineering to replace collapsed Ennery River bridge with new post-tensioned concrete girder bridge on existing alignment; obligated USD 5,004,467. CapEx face = award obligation.",
    "5004467", "2010-07-29", "2010", "19.483", "-72.483",
    "Ennery River bridge replacement, Ennery, Haiti (USASpending PoP Haiti; Ennery pin).",
    "usaspending_lakeshore_ennery_bridge_5p00m_2010",
    "THE PURPOSE OF THIS CONTRACT ID TO REPLACE THE COLLAPSED ENNERY RIVER BRIDGE WITH A NEW POST-TENSIONED, CONCRETE GIRDER BRIDGE ON THE EXISTING ALIGNMENT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C001000020_7200_-NONE-_-NONE-/",
    "Actor: Lakeshore Engineering (U.S.) under USAID — us. Official USASpending Award API. Shuffle bridges_roads; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle952",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521C001000020_7200_-NONE-_-NONE- (Lakeshore Ennery bridge). Signed 2010-07-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C001000020_7200_-NONE-_-NONE-/.",
    "USASpending: Lakeshore Ennery bridge USD 5.004m. Supports lakeshore_ennery_bridge_5p00m_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5004467; date_signed 2010-07-29.",
)

row_doc(
    "palgag_st_marc_commissariat_4p97m_2013",
    "infrastructure", "building_materials", "allied",
    "Palgag Building Technologies — St. Marc commissariat design/build",
    "Haiti",
    "22 Jul 2013: Department of State awards contract SAQMMA13C0182 to Palgag Building Technologies for design/build St. Marc's commissariat; obligated USD 4,972,493.77. CapEx face = award obligation. Distinct from prior Palgag Haiti commissariat rows.",
    "4972493.77", "2013-07-22", "2013", "19.108", "-72.694",
    "St. Marc commissariat design/build, St. Marc, Haiti (USASpending PoP Haiti; St. Marc pin).",
    "usaspending_palgag_st_marc_commissariat_4p97m_2013",
    "IGF::OT::IGF DESIGN BUILD ST. MARC'S COMMISSARIAT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13C0182_1900_-NONE-_-NONE-/",
    "Actor: Palgag (Israel) — allied. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle952",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13C0182_1900_-NONE-_-NONE- (Palgag St. Marc commissariat). Signed 2013-07-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13C0182_1900_-NONE-_-NONE-/.",
    "USASpending: Palgag St. Marc commissariat USD 4.972m. Supports palgag_st_marc_commissariat_4p97m_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4972493.77; date_signed 2013-07-22.",
)

row_doc(
    "emr_nogales_security_4p59m_2011",
    "infrastructure", "building_materials", "us",
    "Enviro-Management & Research — Nogales consulate physical security upgrades",
    "Mexico",
    "27 Sep 2011: Department of State awards task order SAQMMA11F4553 to EMR for design/build physical security upgrades at U.S. Consulate Nogales; obligated USD 4,594,072.25. CapEx face = award obligation.",
    "4594072.25", "2011-09-27", "2011", "31.333", "-110.942",
    "Physical security upgrades, U.S. Consulate Nogales, Mexico (USASpending PoP Mexico).",
    "usaspending_emr_nogales_security_4p59m_2011",
    "DESIGN/BUILD SERVICES FOR PHYSICAL SECURITY UPGRADES AT THE U.S CONSULATE IN NOGALES, MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4553_1900_SAQMMA08D0010_1900/",
    "Actor: EMR (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle952",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F4553_1900_SAQMMA08D0010_1900 (EMR Nogales security). Signed 2011-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4553_1900_SAQMMA08D0010_1900/.",
    "USASpending: EMR Nogales security USD 4.594m. Supports emr_nogales_security_4p59m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4594072.25; date_signed 2011-09-27.",
)

row_doc(
    "nika_emr_tijuana_warehouse_4p57m_2012",
    "infrastructure", "building_materials", "us",
    "NIKA & EMR JV — Tijuana warehouse design/construction",
    "Mexico",
    "28 Sep 2012: Department of State awards task order SAQMMA12F4409 to NIKA & EMR Joint Venture for design and construction of a warehouse in Tijuana; obligated USD 4,574,458.69. CapEx face = award obligation.",
    "4574458.69", "2012-09-28", "2012", "32.515", "-117.038",
    "Warehouse design/construction, Tijuana, Mexico (USASpending PoP Mexico).",
    "usaspending_nika_emr_tijuana_warehouse_4p57m_2012",
    "DESIGN AND CONSTRUCTION OF A WAREHOUSE IN TIJUANA, WAREHOUSE. IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F4409_1900_SAQMMA08D0020_1900/",
    "Actor: NIKA & EMR JV (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle952",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F4409_1900_SAQMMA08D0020_1900 (NIKA/EMR Tijuana warehouse). Signed 2012-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F4409_1900_SAQMMA08D0020_1900/.",
    "USASpending: NIKA/EMR Tijuana warehouse USD 4.574m. Supports nika_emr_tijuana_warehouse_4p57m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4574458.69; date_signed 2012-09-28.",
)

row_doc(
    "hsu_nassau_cmr_perimeter_4p16m_2024",
    "infrastructure", "building_materials", "us",
    "HSU Development — Nassau CMR CSU perimeter wall design/construction",
    "Bahamas",
    "22 Aug 2024: Department of State awards task order 19AQMM24F1428 to HSU Development for full design and construction of Nassau CMR CSU perimeter wall; obligated USD 4,164,115. CapEx face = award obligation. Distinct from hsu_sao_paulo_fire_alarm.",
    "4164115", "2024-08-22", "2024", "25.048", "-77.355",
    "CMR CSU perimeter wall, Nassau, Bahamas (USASpending PoP Bahamas).",
    "usaspending_hsu_nassau_cmr_perimeter_4p16m_2024",
    "TO FUND THE AWARD OF FULL DESIGN AND CONSTRUCTION SERVICES FOR THE NASSAU CMR CSU PERIMETER WALL PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F1428_1900_19AQMM22D0052_1900/",
    "Actor: HSU Development (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle952",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24F1428_1900_19AQMM22D0052_1900 (HSU Nassau CMR perimeter). Signed 2024-08-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F1428_1900_19AQMM22D0052_1900/.",
    "USASpending: HSU Nassau CMR perimeter USD 4.164m. Supports hsu_nassau_cmr_perimeter_4p16m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4164115; date_signed 2024-08-22.",
)

# === Cycle 953 ===
row_doc(
    "eterna_puerto_lempira_hospital_4p02m_2021",
    "infrastructure", "building_materials", "other",
    "Eterna — Puerto Lempira regional hospital design/construction",
    "Honduras",
    "22 Jul 2021: U.S. Army Corps of Engineers awards task order W9127821F0227 to Eterna for design and construction of regional hospital in Puerto Lempira; obligated USD 4,017,539.22. CapEx face = award obligation.",
    "4017539.22", "2021-07-22", "2021", "15.266", "-83.772",
    "Regional hospital, Puerto Lempira, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_puerto_lempira_hospital_4p02m_2021",
    "DESIGN AND CONSTRUCTION OF REGIONAL HOSPITAL IN PUERTO LEMPIRA, HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0227_9700_W9127816D0102_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle953",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0227_9700_W9127816D0102_9700 (Eterna Puerto Lempira hospital). Signed 2021-07-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0227_9700_W9127816D0102_9700/.",
    "USASpending: Eterna Puerto Lempira hospital USD 4.018m. Supports eterna_puerto_lempira_hospital_4p02m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4017539.22; date_signed 2021-07-22.",
)

row_doc(
    "bonatti_soto_cano_barracks_3p99m_2024",
    "infrastructure", "building_materials", "other",
    "Bonatti — Soto Cano mobilization training barracks",
    "Honduras",
    "1 Apr 2024: U.S. Army Corps of Engineers awards task order W9127824F0069 to Bonatti for design and construction of mobilization training barracks on Soto Cano Air Force Base; obligated USD 3,986,765.72. CapEx face = award obligation. Distinct from cce_soto_cano_barracks_2011.",
    "3986765.72", "2024-04-01", "2024", "14.382", "-87.621",
    "Mobilization training barracks, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_bonatti_soto_cano_barracks_3p99m_2024",
    "DESIGN AND CONSTRUCTION OF MOBILIZATION TRAINING BARRACKS ON SOTO CANO AIRFORCE BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0069_9700_W9127823D0072_9700/",
    "Actor: Bonatti (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle953",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0069_9700_W9127823D0072_9700 (Bonatti Soto Cano barracks). Signed 2024-04-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0069_9700_W9127823D0072_9700/.",
    "USASpending: Bonatti Soto Cano barracks USD 3.987m. Supports bonatti_soto_cano_barracks_3p99m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3986765.72; date_signed 2024-04-01.",
)

row_doc(
    "rogers_gamboa_refurb_3p89m_2019",
    "infrastructure", "building_materials", "other",
    "Constructora Rogers (CONROSA) — Gamboa facilities refurbishment",
    "Panama",
    "12 Sep 2019: Smithsonian awards task order 33330219FF0010393 to Constructora Rogers for Gamboa refurbishment of facilities; obligated USD 3,892,988.08. CapEx face = award obligation. Distinct from kunkel_gamboa_b56.",
    "3892988.08", "2019-09-12", "2019", "9.117", "-79.700",
    "Gamboa facilities refurbishment, Panama (USASpending PoP Panama; Gamboa pin).",
    "usaspending_rogers_gamboa_refurb_3p89m_2019",
    "CONSTRUCTION SERVICES FOR THE GAMBOA REFURBISHMENT OF FACILITIES PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219FF0010393_3300_F15CC10192_3300/",
    "Actor: Constructora Rogers/CONROSA (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle953",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330219FF0010393_3300_F15CC10192_3300 (Rogers Gamboa refurb). Signed 2019-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219FF0010393_3300_F15CC10192_3300/.",
    "USASpending: Rogers Gamboa refurb USD 3.893m. Supports rogers_gamboa_refurb_3p89m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3892988.08; date_signed 2019-09-12.",
)

row_doc(
    "pono_aina_nassau_representational_3p63m_2022",
    "infrastructure", "building_materials", "us",
    "Pono Aina — Nassau embassy representational properties renovation",
    "Bahamas",
    "15 Aug 2022: Department of State awards contract 19AQMM22C0094 to Pono Aina for renovation/refurbishment of representational properties at U.S. Embassy Nassau; obligated USD 3,627,546.58. CapEx face = award obligation. Distinct from pono_aina_haiti_chiller.",
    "3627546.58", "2022-08-15", "2022", "25.048", "-77.355",
    "Representational properties renovation, U.S. Embassy Nassau, Bahamas (USASpending PoP Bahamas).",
    "usaspending_pono_aina_nassau_representational_3p63m_2022",
    "RENOVATION AND REFURBISHMENT OF THE REPRESENTATIONAL PROPERTIES AT  US EMBASSY NASSAU BAHAMAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0094_1900_-NONE-_-NONE-/",
    "Actor: Pono Aina (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle953",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22C0094_1900_-NONE-_-NONE- (Pono Aina Nassau representational). Signed 2022-08-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0094_1900_-NONE-_-NONE-/.",
    "USASpending: Pono Aina Nassau representational USD 3.628m. Supports pono_aina_nassau_representational_3p63m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3627546.58; date_signed 2022-08-15.",
)

row_doc(
    "ebital_etchepare_kitchen_3p57m_2016",
    "infrastructure", "building_materials", "other",
    "Ebital — Etchepare psychiatric hospital kitchen/laundry facility",
    "Uruguay",
    "30 Sep 2016: U.S. Army Corps of Engineers awards contract W912CL16C0005 to Ebital for construction of kitchen & laundry facility at Etchepare Psychiatric Hospital in Pueblo Nuevo; obligated USD 3,569,135.22. CapEx face = award obligation.",
    "3569135.22", "2016-09-30", "2016", "-34.730", "-56.220",
    "Kitchen/laundry facility, Etchepare Psychiatric Hospital, Pueblo Nuevo, Uruguay (USASpending PoP Uruguay; Las Piedras/Pueblo Nuevo pin).",
    "usaspending_ebital_etchepare_kitchen_3p57m_2016",
    "IGF::OT::IGF CONSTRUCTION OF KITCHEN&LAUNDRY FACILITY AT THE ETCHEPARE PSYCHIATRIC HOSPITAL IN PUEBLO NUEVO, URUGUAY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL16C0005_9700_-NONE-_-NONE-/",
    "Actor: Ebital (Uruguay) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle953",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL16C0005_9700_-NONE-_-NONE- (Ebital Etchepare kitchen). Signed 2016-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL16C0005_9700_-NONE-_-NONE-/.",
    "USASpending: Ebital Etchepare kitchen USD 3.569m. Supports ebital_etchepare_kitchen_3p57m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3569135.22; date_signed 2016-09-30.",
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
    print(f"cycles951-953 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
