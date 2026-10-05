#!/usr/bin/env python3
"""Cycles 993–995: USASpending LatAm CapEx residual (~USD0.21–0.25m).

Seeds: 20261993–20261995. Thin top-up dry.
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


# === Cycle 993 ===
row_doc(
    "tss_building_remodel_248k_2024",
    "infrastructure", "building_materials", "other",
    "Technology and Services Solutions — El Salvador building remodel",
    "El Salvador",
    "10 Oct 2024: Department of State awards contract 19ES6025P0006 to Technology and Services Solutions for building remodel (PoP El Salvador); obligated USD 248,362.68. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "248362.68", "2024-10-10", "2024", "", "",
    "Building remodel, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_tss_building_remodel_248k_2024",
    "BUILDING REMODEL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6025P0006_1900_-NONE-_-NONE-/",
    "Actor: Technology and Services Solutions S.A. de C.V. (Santa Tecla) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle993",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6025P0006_1900_-NONE-_-NONE- (TSS building remodel). Signed 2024-10-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6025P0006_1900_-NONE-_-NONE-/.",
    "USASpending: TSS building remodel USD 0.248m. Supports tss_building_remodel_248k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 248362.68; date_signed 2024-10-10.",
)

row_doc(
    "misc_community_center_248k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia community center",
    "Colombia",
    "11 Sep 2013: U.S. Army Corps of Engineers awards contract W913FT13C0018 for construction of a community center (PoP Colombia); obligated USD 247,887.51. CapEx face = award obligation. Recipient redacted; site not named — lat/lon blank.",
    "247887.51", "2013-09-11", "2013", "", "",
    "Community center construction, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_misc_community_center_248k_2013",
    "CONSTRUCT A COMMUNITY CENTER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13C0018_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle993",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT13C0018_9700_-NONE-_-NONE- (Colombia community center). Signed 2013-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13C0018_9700_-NONE-_-NONE-/.",
    "USASpending: Colombia community center USD 0.248m. Supports misc_community_center_248k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 247887.51; date_signed 2013-09-11.",
)

row_doc(
    "misc_pijaos_barracks_247k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Pijaos barracks and offices",
    "Colombia",
    "1 Jul 2011: Department of State awards contract SCO15011CN014 for barracks and offices construction at Pijaos; obligated USD 247,060.58. CapEx face = award obligation. Recipient redacted.",
    "247060.58", "2011-07-01", "2011", "4.090", "-75.150",
    "Barracks and offices construction, Pijaos, Colombia (USASpending description; approximate Tolima pin).",
    "usaspending_misc_pijaos_barracks_247k_2011",
    "BARRACS AND OFFICES CONSTRUCTION AT PIJAOS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011CN014_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle993",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15011CN014_1900_-NONE-_-NONE- (Pijaos barracks). Signed 2011-07-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011CN014_1900_-NONE-_-NONE-/.",
    "USASpending: Pijaos barracks USD 0.247m. Supports misc_pijaos_barracks_247k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 247060.58; date_signed 2011-07-01.",
)

row_doc(
    "isobox_corozal_este_237k_2025",
    "infrastructure", "building_materials", "other",
    "Isobox — Corozal Este renovation",
    "Panama",
    "1 Sep 2025: Department of Defense awards contract H9228125CE002 to Isobox for renovation project at Corozal Este, Panama; obligated USD 237,445.40. CapEx face = award obligation.",
    "237445.40", "2025-09-01", "2025", "8.980", "-79.575",
    "Renovation project, Corozal Este, Panama (USASpending description).",
    "usaspending_isobox_corozal_este_237k_2025",
    "THE PURPOSE OF THIS CONTRACT IS TO COMPLETE A RENOVATION PROJECT AT COROZAL ESTE, PANAMA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125CE002_9700_-NONE-_-NONE-/",
    "Actor: Isobox Inc. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle993",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_H9228125CE002_9700_-NONE-_-NONE- (Isobox Corozal Este). Signed 2025-09-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125CE002_9700_-NONE-_-NONE-/.",
    "USASpending: Isobox Corozal Este USD 0.237m. Supports isobox_corozal_este_237k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 237445.40; date_signed 2025-09-01.",
)

row_doc(
    "misc_tobar_donoso_barracks_227k_2009",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Tobar Donoso military barracks",
    "Ecuador",
    "9 Sep 2009: Department of State awards contract SWHARC09C0003 for construction of military barracks in Tobar Donoso, Ecuador; obligated USD 226,708.63. CapEx face = award obligation. Recipient redacted.",
    "226708.63", "2009-09-09", "2009", "1.050", "-78.520",
    "Military barracks, Tobar Donoso, Ecuador (USASpending description).",
    "usaspending_misc_tobar_donoso_barracks_227k_2009",
    "CONSTRUCTION OF MILITARY BARARCKS IN TOBAR DONOSO ECUADOR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC09C0003_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle993",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC09C0003_1900_-NONE-_-NONE- (Tobar Donoso barracks). Signed 2009-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC09C0003_1900_-NONE-_-NONE-/.",
    "USASpending: Tobar Donoso barracks USD 0.227m. Supports misc_tobar_donoso_barracks_227k_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 226708.63; date_signed 2009-09-09.",
)

# === Cycle 994 ===
row_doc(
    "trison_nassau_chiller_226k_2013",
    "infrastructure", "building_materials", "us",
    "Trison Construction — Nassau embassy chiller piping modification",
    "Bahamas",
    "24 Dec 2013: Department of State awards task order SAQMMA14F0355 to Trison Construction for chiller piping modification at U.S. Embassy Nassau, Bahamas; obligated USD 226,204. CapEx face = award obligation.",
    "226204", "2013-12-24", "2013", "25.078", "-77.345",
    "Chiller piping modification, U.S. Embassy Nassau, Bahamas (USASpending description).",
    "usaspending_trison_nassau_chiller_226k_2013",
    "CHILLER PIPING MODIFICATION PROJECT AT THE U.S. EMBASSY IN NASSAU, BAHAMAS IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F0355_1900_SAQMMA08D0019_1900/",
    "Actor: Trison Construction Inc. (College Park MD, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle994",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14F0355_1900_SAQMMA08D0019_1900 (Trison Nassau chiller). Signed 2013-12-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F0355_1900_SAQMMA08D0019_1900/.",
    "USASpending: Trison Nassau chiller USD 0.226m. Supports trison_nassau_chiller_226k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 226204; date_signed 2013-12-24.",
)

row_doc(
    "misc_brasilia_cmr_road_pool_225k_2019",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Brasília CMR service road and pool",
    "Brazil",
    "17 Jun 2019: Department of State awards contract 19BR2519P0884 for CMR construction of service road and pool (PoP Brazil/Brasília); obligated USD 224,753.87. CapEx face = award obligation. Recipient redacted.",
    "224753.87", "2019-06-17", "2019", "-15.794", "-47.883",
    "CMR service road and pool construction, Brasília, Brazil (USASpending description).",
    "usaspending_misc_brasilia_cmr_road_pool_225k_2019",
    "BSB-FAC CMR CONSTRUCTION OF SERVICE ROAD AND POOL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0884_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle994",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2519P0884_1900_-NONE-_-NONE- (Brasília CMR road/pool). Signed 2019-06-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0884_1900_-NONE-_-NONE-/.",
    "USASpending: Brasília CMR road/pool USD 0.225m. Supports misc_brasilia_cmr_road_pool_225k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 224753.87; date_signed 2019-06-17.",
)

row_doc(
    "kunkel_gamboa_refurb_224k_2023",
    "infrastructure", "building_materials", "other",
    "Kunkel Construction — Gamboa facilities refurbishment supplementary works",
    "Panama",
    "15 May 2023: Smithsonian awards contract 33330223CF0010230 to Kunkel Construction for supplementary works for the Gamboa refurbishment of facilities project; obligated USD 224,133.46. CapEx face = award obligation.",
    "224133.46", "2023-05-15", "2023", "9.120", "-79.700",
    "Gamboa facilities refurbishment, Colón Province, Panama (USASpending / Smithsonian).",
    "usaspending_kunkel_gamboa_refurb_224k_2023",
    "CONSTRUCTION SERVICES FOR SUPPLEMENTARY WORKS FOR THE GAMBOA REFURBISHMENT OF FACILITIES PROJECT. REFURBISHMENT OF FACILITIES PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330223CF0010230_3300_-NONE-_-NONE-/",
    "Actor: Kunkel Construction Inc. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle994",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330223CF0010230_3300_-NONE-_-NONE- (Kunkel Gamboa refurb). Signed 2023-05-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330223CF0010230_3300_-NONE-_-NONE-/.",
    "USASpending: Kunkel Gamboa refurb USD 0.224m. Supports kunkel_gamboa_refurb_224k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 224133.46; date_signed 2023-05-15.",
)

row_doc(
    "palgag_dr_atfp_gates_220k_2010",
    "infrastructure", "building_materials", "allied",
    "Palgag Building Technologies — Dominican Republic ATFP gates",
    "Dominican Republic",
    "30 Sep 2010: Department of Defense awards contract N6945010C0070 to Palgag Building Technologies for construction of ATFP gates in Dominican Republic; obligated USD 220,000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "220000", "2010-09-30", "2010", "", "",
    "ATFP gates construction, Dominican Republic (USASpending PoP Dominican Republic; site not named — lat/lon blank).",
    "usaspending_palgag_dr_atfp_gates_220k_2010",
    "CONSTRUCT ATFP GATES; DOMINICAN REPUBLIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0070_9700_-NONE-_-NONE-/",
    "Actor: Palgag Building Technologies Ltd. (Kibbutz Gaash, Israel) — allied. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle994",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945010C0070_9700_-NONE-_-NONE- (Palgag DR ATFP gates). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0070_9700_-NONE-_-NONE-/.",
    "USASpending: Palgag DR ATFP gates USD 0.220m. Supports palgag_dr_atfp_gates_220k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 220000; date_signed 2010-09-30.",
)

row_doc(
    "bolanos_manta_port_dorms_219k_2011",
    "infrastructure", "building_materials", "other",
    "Bolaños Albán — Manta Port dormitories and kennels",
    "Ecuador",
    "18 Jan 2011: Department of State awards contract SWHARC11C0002 to Bolaños Albán Fausto Tarquino for construction project at Manta Port, Ecuador (dormitories and kennels); obligated USD 219,469.29. CapEx face = award obligation.",
    "219469.29", "2011-01-18", "2011", "-0.950", "-80.730",
    "Dormitories and kennels, Manta Port, Ecuador (USASpending description).",
    "usaspending_bolanos_manta_port_dorms_219k_2011",
    "CONSTRUCTION PROJECT AT MANTA PORT, ECUADOR (DORMITORIES AND KENNELS)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11C0002_1900_-NONE-_-NONE-/",
    "Actor: Bolaños Albán Fausto Tarquino (Quito) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle994",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC11C0002_1900_-NONE-_-NONE- (Bolaños Manta Port dorms). Signed 2011-01-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11C0002_1900_-NONE-_-NONE-/.",
    "USASpending: Bolaños Manta Port dorms USD 0.219m. Supports bolanos_manta_port_dorms_219k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 219469.29; date_signed 2011-01-18.",
)

# === Cycle 995 ===
row_doc(
    "kunkel_bci_dorm_d_216k_2023",
    "infrastructure", "building_materials", "other",
    "Kunkel Construction — STRI BCI Dorm D refurbishment",
    "Panama",
    "19 Sep 2023: Smithsonian awards contract 33330223CF0010526 to Kunkel Construction for refurbishment of dormitories at STRI BCI Dorm D; obligated USD 216,201.63. CapEx face = award obligation.",
    "216201.63", "2023-09-19", "2023", "9.165", "-79.838",
    "Dorm D refurbishment, Barro Colorado Island / STRI, Panama (USASpending / Smithsonian).",
    "usaspending_kunkel_bci_dorm_d_216k_2023",
    "REFURBISH DORMITORIES AT STRI, BCI, DORM D",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330223CF0010526_3300_-NONE-_-NONE-/",
    "Actor: Kunkel Construction Inc. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle995",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330223CF0010526_3300_-NONE-_-NONE- (Kunkel BCI Dorm D). Signed 2023-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330223CF0010526_3300_-NONE-_-NONE-/.",
    "USASpending: Kunkel BCI Dorm D USD 0.216m. Supports kunkel_bci_dorm_d_216k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 216201.63; date_signed 2023-09-19.",
)

row_doc(
    "misc_peru_cmu_living_214k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru CMU living quarters",
    "Peru",
    "6 Sep 2013: Department of Defense awards contract FA441713C6000 for construction of CMU living quarters (PoP Peru); obligated USD 214,439.56. CapEx face = award obligation. Recipient redacted; site not named — lat/lon blank.",
    "214439.56", "2013-09-06", "2013", "", "",
    "CMU living quarters construction, Peru (USASpending PoP Peru; site not named — lat/lon blank).",
    "usaspending_misc_peru_cmu_living_214k_2013",
    "IGF::OT::IGF CONSTRUCTION OF CMU LIVING QUARTERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA441713C6000_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle995",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA441713C6000_9700_-NONE-_-NONE- (Peru CMU living quarters). Signed 2013-09-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA441713C6000_9700_-NONE-_-NONE-/.",
    "USASpending: Peru CMU living quarters USD 0.214m. Supports misc_peru_cmu_living_214k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 214439.56; date_signed 2013-09-06.",
)

row_doc(
    "serrano_emergency_water_211k_2017",
    "resources", "water", "other",
    "Serrano Proaño — emergency water supply project",
    "Peru",
    "29 Sep 2017: U.S. Army Corps of Engineers awards task order W9127817F0475 to Serrano Proaño for emergency water supply project (PoP Peru); obligated USD 211,268.16. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "211268.16", "2017-09-29", "2017", "", "",
    "Emergency water supply project, Peru (USASpending PoP Peru; site not named — lat/lon blank).",
    "usaspending_serrano_emergency_water_211k_2017",
    "IGF::OT::IGF EMERGENCY WATER SUPPLY PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0475_9700_W9127816D0109_9700/",
    "Actor: Serrano Proaño Diseño y Construcción S.A. (Quito) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle995",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0475_9700_W9127816D0109_9700 (Serrano emergency water). Signed 2017-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0475_9700_W9127816D0109_9700/.",
    "USASpending: Serrano emergency water USD 0.211m. Supports serrano_emergency_water_211k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 211268.16; date_signed 2017-09-29.",
)

row_doc(
    "bendig_msp_joc_210k_2026",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — MSP/JOC relocation and renovation",
    "Costa Rica",
    "11 Sep 2026: Department of State awards contract 19CS8026P0956 to Industrias Bendig for INL relocation and renovation of the MSP/JOC; obligated USD 209,550. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "209550", "2026-09-11", "2026", "", "",
    "MSP/JOC relocation and renovation, Costa Rica (USASpending PoP Costa Rica; site not named — lat/lon blank).",
    "usaspending_bendig_msp_joc_210k_2026",
    "INL 1930.0 RELOCATION & RENOVATION OF THE MSP/JOC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8026P0956_1900_-NONE-_-NONE-/",
    "Actor: Industrias Bendig SA (Desamparados, Costa Rica) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle995",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8026P0956_1900_-NONE-_-NONE- (Bendig MSP/JOC). Signed 2026-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8026P0956_1900_-NONE-_-NONE-/.",
    "USASpending: Bendig MSP/JOC USD 0.210m. Supports bendig_msp_joc_210k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 209550; date_signed 2026-09-11.",
)

row_doc(
    "fuduric_ceopaz_warehouse_209k_2019",
    "infrastructure", "building_materials", "allied",
    "Josip Fudurić — CEOPAZ warehouse El Salvador",
    "El Salvador",
    "3 Apr 2019: U.S. Army Corps of Engineers awards contract W912CL19C0004 to Josip Fudurić for construction of a warehouse for CEOPAZ in El Salvador; obligated USD 209,267.98. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "209267.98", "2019-04-03", "2019", "", "",
    "CEOPAZ warehouse construction, El Salvador (USASpending PoP El Salvador; site not named — lat/lon blank).",
    "usaspending_fuduric_ceopaz_warehouse_209k_2019",
    "CONSTRUCTION WORK TO BUILD A WAREHOUSE FOR CEOPAZ IN EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL19C0004_9700_-NONE-_-NONE-/",
    "Actor: Josip Fudurić d.o.o. (Zagreb, Croatia) — allied. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle995",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL19C0004_9700_-NONE-_-NONE- (Fudurić CEOPAZ warehouse). Signed 2019-04-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL19C0004_9700_-NONE-_-NONE-/.",
    "USASpending: Fudurić CEOPAZ warehouse USD 0.209m. Supports fuduric_ceopaz_warehouse_209k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 209267.98; date_signed 2019-04-03.",
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
    print(f"cycles993-995 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
