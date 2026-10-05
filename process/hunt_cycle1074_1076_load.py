#!/usr/bin/env python3
"""Cycles 1074–1076: USASpending LatAm CapEx residual (~USD0.052–0.063m).

Seeds: 20262074–20262076. Thin top-up dry.
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


# === Cycle 1074 (seed 20262074) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "hcs_honduras_ae_support_58k_2013",
    "infrastructure", "engineering_epc", "us",
    "HCS Group — Honduras A&E support",
    "Honduras",
    "29 Sep 2013: Department of Defense awards task order 0044 under IDV W9127810D0050 to HCS Group, P.C. for A&E support (PoP Honduras); obligated USD 58,299.35. CapEx face = award obligation. Exact project site unnamed — lat/lon blank.",
    "58299.35", "2013-09-29", "2013", "", "",
    "A&E support, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_hcs_honduras_ae_support_58k_2013",
    "A&E SUPPORT  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0044_9700_W9127810D0050_9700/",
    "Actor: HCS Group, P.C. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1074",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0044_9700_W9127810D0050_9700 (HCS Honduras A&E). Signed 2013-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0044_9700_W9127810D0050_9700/.",
    "USASpending: HCS Honduras A&E USD 0.058m. Supports hcs_honduras_ae_support_58k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 58299.35; date_signed 2013-09-29.",
)

row_doc(
    "ganahl_jamaica_plaza_deck_repair_58k_2016",
    "infrastructure", "building_materials", "us",
    "Ganahl Lumber — Jamaica Plaza stores lumber and deck repair",
    "Jamaica",
    "22 Sep 2016: Department of State awards contract SJM37016M1332 to Ganahl Lumber Company for lumber for stores and deck repair at P. Plaza (PoP Jamaica); obligated USD 57,630.18. CapEx face = award obligation. Exact Plaza site unnamed — lat/lon blank.",
    "57630.18", "2016-09-22", "2016", "", "",
    "Lumber for stores and deck repair at P. Plaza, Jamaica (USASpending description; Plaza named, site coords not stated — lat/lon blank).",
    "usaspending_ganahl_jamaica_plaza_deck_repair_58k_2016",
    "IGF::OT::IGF FAC: LUMBER FOR STORES AND DECK REPAIR P. PLAZA [7901.3]",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016M1332_1900_-NONE-_-NONE-/",
    "Actor: Ganahl Lumber Company (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1074",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37016M1332_1900_-NONE-_-NONE- (Ganahl Jamaica deck repair). Signed 2016-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016M1332_1900_-NONE-_-NONE-/.",
    "USASpending: Ganahl Jamaica deck repair USD 0.058m. Supports ganahl_jamaica_plaza_deck_repair_58k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 57630.18; date_signed 2016-09-22.",
)

row_doc(
    "carranza_belize_kd_range_62k_2010",
    "infrastructure", "building_materials", "other",
    "Carlos Carranza — Belize K-D range repair restore",
    "Belize",
    "4 Mar 2010: Department of Defense awards contract W9127810P0122 to Carlos Carranza for repair restore K-D range (PoP Belize); obligated USD 61,500. CapEx face = award obligation. Exact range site unnamed — lat/lon blank.",
    "61500", "2010-03-04", "2010", "", "",
    "Repair restore K-D range, Belize (USASpending description; range named, site coords not stated — lat/lon blank).",
    "usaspending_carranza_belize_kd_range_62k_2010",
    "REPAIR RESTORE K-D RANGE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0122_9700_-NONE-_-NONE-/",
    "Actor: Carlos Carranza (Belize) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1074",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127810P0122_9700_-NONE-_-NONE- (Carranza Belize K-D range). Signed 2010-03-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0122_9700_-NONE-_-NONE-/.",
    "USASpending: Carranza Belize K-D range USD 0.062m. Supports carranza_belize_kd_range_62k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61500; date_signed 2010-03-04.",
)

row_doc(
    "misc_honduras_transformer_100kva_61k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras 100 kVA transformer",
    "Honduras",
    "17 Aug 2011: Department of Defense awards contract W912QM11P0052 for transformer 100 kVA 34500 120/240V (PoP Honduras); obligated USD 61,438.15. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "61438.15", "2011-08-17", "2011", "", "",
    "Transformer 100 kVA 34500 120/240V, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_honduras_transformer_100kva_61k_2011",
    "TRANSFORMER 100 KVA 34500 120/240V",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM11P0052_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1074",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM11P0052_9700_-NONE-_-NONE- (Honduras 100 kVA transformer). Signed 2011-08-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM11P0052_9700_-NONE-_-NONE-/.",
    "USASpending: Honduras 100 kVA transformer USD 0.061m. Supports misc_honduras_transformer_100kva_61k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61438.15; date_signed 2011-08-17.",
)

row_doc(
    "misc_colombia_facilities_remodeling_63k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia facilities remodeling",
    "Colombia",
    "4 May 2011: Department of State awards contract SCO15011CN010 for facilities remodeling (PoP Colombia); obligated USD 62,635.45. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "62635.45", "2011-05-04", "2011", "", "",
    "Facilities remodeling, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_colombia_facilities_remodeling_63k_2011",
    "FACILITIES REMODELING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011CN010_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1074",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15011CN010_1900_-NONE-_-NONE- (Colombia facilities remodeling). Signed 2011-05-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011CN010_1900_-NONE-_-NONE-/.",
    "USASpending: Colombia facilities remodeling USD 0.063m. Supports misc_colombia_facilities_remodeling_63k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62635.45; date_signed 2011-05-04.",
)

# === Cycle 1075 (seed 20262075) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "baskerville_peru_callao_mic_expansion_56k_2018",
    "infrastructure", "engineering_epc", "us",
    "Baskerville Donovan — Peru Callao naval base MIC expansion D/B",
    "Peru",
    "1 Jun 2018: Department of Defense awards task order W9127818F0325 under IDV W9127814D0075 to Baskerville Donovan Inc for D/B RFP for expansion of MIC at Callao naval base, Lima (PoP Peru); obligated USD 56,432. CapEx face = award obligation. Exact MIC site unnamed — lat/lon blank.",
    "56432", "2018-06-01", "2018", "", "",
    "D/B expansion of MIC at Callao naval base, Lima, Peru (USASpending description; Callao named, site coords not stated — lat/lon blank).",
    "usaspending_baskerville_peru_callao_mic_expansion_56k_2018",
    "D/B RFP FOR THE EXPANSION OF MIC IN CALLAO NAVAL BASE, LIMA, PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0325_9700_W9127814D0075_9700/",
    "Actor: Baskerville Donovan Inc (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1075",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0325_9700_W9127814D0075_9700 (Baskerville Callao MIC). Signed 2018-06-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0325_9700_W9127814D0075_9700/.",
    "USASpending: Baskerville Callao MIC USD 0.056m. Supports baskerville_peru_callao_mic_expansion_56k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 56432; date_signed 2018-06-01.",
)

row_doc(
    "mount_airey_argentina_cabling_54k_2018",
    "infrastructure", "engineering_epc", "us",
    "Mount Airey Group — Argentina cabling services",
    "Argentina",
    "24 Jan 2018: Department of State awards contract 19AR2018P0217 to Mount Airey Group LLC for cabling services (PoP Argentina); obligated USD 53,844.13. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "53844.13", "2018-01-24", "2018", "", "",
    "Cabling services, Argentina (USASpending description; site not named — lat/lon blank).",
    "usaspending_mount_airey_argentina_cabling_54k_2018",
    "CABLING SERVICES IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P0217_1900_-NONE-_-NONE-/",
    "Actor: Mount Airey Group LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1075",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2018P0217_1900_-NONE-_-NONE- (Mount Airey Argentina cabling). Signed 2018-01-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P0217_1900_-NONE-_-NONE-/.",
    "USASpending: Mount Airey Argentina cabling USD 0.054m. Supports mount_airey_argentina_cabling_54k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 53844.13; date_signed 2018-01-24.",
)

row_doc(
    "sistemas_honduras_nec_tower_movement_62k_2016",
    "energy", "power_plants_grid", "other",
    "Sistemas y Soluciones de Telecomunicaciones — Honduras NEC tower movement",
    "Honduras",
    "28 Nov 2016: Department of State awards contract SHO80017M0085 to Sistemas y Soluciones de Telecomunicaciones for tower movement for NEC (PoP Honduras); obligated USD 61,962.24. CapEx face = award obligation. Exact NEC site unnamed — lat/lon blank.",
    "61962.24", "2016-11-28", "2016", "", "",
    "Tower movement for NEC, Honduras (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_sistemas_honduras_nec_tower_movement_62k_2016",
    "IGF::CT::IGF TOWER MOVEMENT FOR NEC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80017M0085_1900_-NONE-_-NONE-/",
    "Actor: Sistemas y Soluciones de Telecomunicaciones (Honduras) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1075",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80017M0085_1900_-NONE-_-NONE- (Honduras NEC tower movement). Signed 2016-11-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80017M0085_1900_-NONE-_-NONE-/.",
    "USASpending: Honduras NEC tower movement USD 0.062m. Supports sistemas_honduras_nec_tower_movement_62k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61962.24; date_signed 2016-11-28.",
)

row_doc(
    "misc_colombia_cartagena_diran_access_control_62k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Cartagena DIRAN base port security access control",
    "Colombia",
    "8 Jul 2013: Department of State awards contract SCO15013M0981 for port security access control system for DIRAN base at Cartagena (PoP Colombia); obligated USD 61,862.39. CapEx face = award obligation. Exact base site unnamed — lat/lon blank.",
    "61862.39", "2013-07-08", "2013", "", "",
    "Port security access control system for DIRAN base at Cartagena, Colombia (USASpending description; Cartagena named, site coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_cartagena_diran_access_control_62k_2013",
    "PORT SEC. ACCES CONTROL SYSTEM FOR DIRAN BASE AT CARTAGENA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0981_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1075",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15013M0981_1900_-NONE-_-NONE- (Colombia Cartagena DIRAN access control). Signed 2013-07-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0981_1900_-NONE-_-NONE-/.",
    "USASpending: Colombia Cartagena DIRAN access control USD 0.062m. Supports misc_colombia_cartagena_diran_access_control_62k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61862.39; date_signed 2013-07-08.",
)

row_doc(
    "misc_colombia_condoto_container_remodel_62k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Condoto COLAR material container remodeling",
    "Colombia",
    "18 Jun 2013: Department of State awards contract SCO15013M0919 for NAU COLAR material container remodeling Condoto (PoP Colombia); obligated USD 61,820.86. CapEx face = award obligation. Exact Condoto site unnamed — lat/lon blank.",
    "61820.86", "2013-06-18", "2013", "", "",
    "Material container remodeling at Condoto, Colombia (USASpending description; Condoto named, site coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_condoto_container_remodel_62k_2013",
    "NAU COLAR MATERIAL CONTAINER REMODELING CONDOTO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0919_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1075",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15013M0919_1900_-NONE-_-NONE- (Colombia Condoto container remodel). Signed 2013-06-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0919_1900_-NONE-_-NONE-/.",
    "USASpending: Colombia Condoto container remodel USD 0.062m. Supports misc_colombia_condoto_container_remodel_62k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61820.86; date_signed 2013-06-18.",
)

# === Cycle 1076 (seed 20262076) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "grotheer_colombia_chiller_design_53k_2012",
    "infrastructure", "engineering_epc", "us",
    "Grotheer & Co. — Colombia primary chiller replacement design",
    "Colombia",
    "12 Apr 2012: Department of State awards contract SCO20012M1278 to Grotheer & Co. for design services for primary chiller replacement (PoP Colombia); obligated USD 53,099.05. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "53099.05", "2012-04-12", "2012", "", "",
    "Design services for primary chiller replacement, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_grotheer_colombia_chiller_design_53k_2012",
    "DESIGN SERVICES FOR PRIMARY CHILLER REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012M1278_1900_-NONE-_-NONE-/",
    "Actor: Grotheer & Co. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1076",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20012M1278_1900_-NONE-_-NONE- (Grotheer Colombia chiller design). Signed 2012-04-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012M1278_1900_-NONE-_-NONE-/.",
    "USASpending: Grotheer Colombia chiller design USD 0.053m. Supports grotheer_colombia_chiller_design_53k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 53099.05; date_signed 2012-04-12.",
)

row_doc(
    "valkyrie_paraguay_telecom_cabling_53k_2022",
    "infrastructure", "engineering_epc", "us",
    "Valkyrie Enterprises — Paraguay Asuncion telecommunications cabling system",
    "Paraguay",
    "23 Jun 2022: Department of State awards order 19AQMM22F2246 to Valkyrie Enterprises, LLC for telecommunications cabling system in Asuncion (PoP Paraguay); obligated USD 52,950.58. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "52950.58", "2022-06-23", "2022", "", "",
    "Telecommunications cabling system in Asuncion, Paraguay (USASpending description; Asuncion named, site coords not stated — lat/lon blank).",
    "usaspending_valkyrie_paraguay_telecom_cabling_53k_2022",
    "TELECOMMUNICATIONS CABLING SYSTEM IN ASUNCION, PARAGUAY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2246_1900_19AQMM21D0155_1900/",
    "Actor: Valkyrie Enterprises, LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1076",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F2246_1900_19AQMM21D0155_1900 (Valkyrie Paraguay telecom cabling). Signed 2022-06-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2246_1900_19AQMM21D0155_1900/.",
    "USASpending: Valkyrie Paraguay telecom cabling USD 0.053m. Supports valkyrie_paraguay_telecom_cabling_53k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 52950.58; date_signed 2022-06-23.",
)

row_doc(
    "wkl_panama_mpr_motor_pool_repair_61k_2015",
    "infrastructure", "building_materials", "other",
    "W.K.L. Arquitectos — Panama MPR and motor pool offices repair",
    "Panama",
    "22 Sep 2015: Department of State awards contract SPM07015M0938 to W.K.L. Arquitectos S.A. for repair MPR and motor pool offices (PoP Panama); obligated USD 60,925. CapEx face = award obligation. Exact offices unnamed — lat/lon blank.",
    "60925", "2015-09-22", "2015", "", "",
    "Repair MPR and motor pool offices, Panama (USASpending description; offices not named — lat/lon blank).",
    "usaspending_wkl_panama_mpr_motor_pool_repair_61k_2015",
    "REPAIR MPR AND MOTOR POOL OFFICES IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07015M0938_1900_-NONE-_-NONE-/",
    "Actor: W.K.L. Arquitectos S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1076",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07015M0938_1900_-NONE-_-NONE- (WKL Panama MPR/motor pool). Signed 2015-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07015M0938_1900_-NONE-_-NONE-/.",
    "USASpending: WKL Panama MPR/motor pool USD 0.061m. Supports wkl_panama_mpr_motor_pool_repair_61k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60925; date_signed 2015-09-22.",
)

row_doc(
    "misc_nicaragua_buildings_1_2_renovation_61k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Nicaragua renovation of buildings 1 and 2",
    "Nicaragua",
    "26 Jan 2010: Department of Defense awards contract W912CL10C0003 for renovation of building 1 and 2 (PoP Nicaragua); obligated USD 60,908.49. CapEx face = award obligation. Exact buildings unnamed — lat/lon blank.",
    "60908.49", "2010-01-26", "2010", "", "",
    "Renovation of buildings 1 and 2, Nicaragua (USASpending description; buildings numbered, site coords not stated — lat/lon blank).",
    "usaspending_misc_nicaragua_buildings_1_2_renovation_61k_2010",
    "RENOVATION OF BUILDING 1 & 2",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0003_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1076",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0003_9700_-NONE-_-NONE- (Nicaragua buildings 1&2 renovation). Signed 2010-01-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0003_9700_-NONE-_-NONE-/.",
    "USASpending: Nicaragua buildings 1&2 renovation USD 0.061m. Supports misc_nicaragua_buildings_1_2_renovation_61k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60908.49; date_signed 2010-01-26.",
)

row_doc(
    "misc_peru_chancery_computer_room_ac_61k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Peru chancery computer room AC unit replacement",
    "Peru",
    "19 May 2010: Department of State awards contract SPE50010C0049 for replace AC unit for chancery computer room (PoP Peru); obligated USD 60,825.82. CapEx face = award obligation. Exact chancery site unnamed — lat/lon blank.",
    "60825.82", "2010-05-19", "2010", "", "",
    "Replace AC unit for chancery computer room, Peru (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_misc_peru_chancery_computer_room_ac_61k_2010",
    "FAC - REPLACE AC UNIT FOR CHANCERY COMPUTER ROOM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50010C0049_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1076",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50010C0049_1900_-NONE-_-NONE- (Peru chancery computer room AC). Signed 2010-05-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50010C0049_1900_-NONE-_-NONE-/.",
    "USASpending: Peru chancery computer room AC USD 0.061m. Supports misc_peru_chancery_computer_room_ac_61k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60825.82; date_signed 2010-05-19.",
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
