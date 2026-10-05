#!/usr/bin/env python3
"""Cycles 1262–1267: USASpending LatAm CapEx (Hardline/Alutiiq security + fire/roof/elevator + residual other).

Seeds: 20262262–20262267. Thin top-up dry. Security/ballistics CapEx tranche + residual make-ready.
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

# === Cycle 1262 ===
row_doc(
    "hardline_mexico_psu_febr_4585k_2011",
    "infrastructure", "building_materials", "us",
    "CTS-Hardline — Mexico physical security upgrade FE/BR",
    "Mexico",
    "1 Sep 2011: Department of State awards contract to CTS-HARDLINE, LLC for Phase II/III/IV physical security upgrade (PSU) and forced entry/ballistic resistant works (PoP Mexico); obligated USD 4585291.51. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "4585291.51", "2011-09-01", "2011", "", "",
    "PHASE II/III/IV - PHYSICAL SECURITY UPGRADE (PSU) AND FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACE, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hardline_mexico_psu_febr_4585k_2011",
    "PHASE II/III/IV - PHYSICAL SECURITY UPGRADE (PSU) AND FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND REPAIR - MATAMOROS, MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3162_1900_SAQMMA07D0010_1900/",
    "Actor: CTS-HARDLINE, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1262",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F3162_1900_SAQMMA07D0010_1900 (hardline_mexico_psu_febr_4585k_2011). Signed 2011-09-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3162_1900_SAQMMA07D0010_1900/.",
    "USASpending: hardline_mexico_psu_febr_4585k_2011 USD 4.585m. Supports hardline_mexico_psu_febr_4585k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4585291.51; date_signed 2011-09-01.",
    investment_type="epc",
)

# === Cycle 1262 ===
row_doc(
    "alutiiq_mexico_fgr_ballistics_lab_5519k_2023",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Mexico City FGR mobile ballistics laboratory",
    "Mexico",
    "10 Jul 2023: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for FGR mobile ballistics laboratory project Mexico City (PoP Mexico); obligated USD 5519018.48. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "5519018.48", "2023-07-10", "2023", "", "",
    "FGR MOBILE BALLISTICS LABORATORY PROJECT - MEXICO CITY, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_fgr_ballistics_lab_5519k_2023",
    "FGR MOBILE BALLISTICS LABORATORY PROJECT - MEXICO CITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5007_1900_19AQMM20D0067_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1262",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMR23F5007_1900_19AQMM20D0067_1900 (alutiiq_mexico_fgr_ballistics_lab_5519k_2023). Signed 2023-07-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5007_1900_19AQMM20D0067_1900/.",
    "USASpending: alutiiq_mexico_fgr_ballistics_lab_5519k_2023 USD 5.519m. Supports alutiiq_mexico_fgr_ballistics_lab_5519k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5519018.48; date_signed 2023-07-10.",
    investment_type="equipment_supply",
)

# === Cycle 1262 ===
row_doc(
    "empresa_construccion_elsalvador_fire_suppression_651k_2017",
    "infrastructure", "building_materials", "other",
    "Empresa de Construcción y Transporte — El Salvador fire suppression systems",
    "El Salvador",
    "27 Sep 2017: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for fire suppression systems (PoP El Salvador); obligated USD 651081.50. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "651081.50", "2017-09-27", "2017", "", "",
    "IGF::OT::IGF FIRE SUPPRESSION SYSTEMS, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_empresa_construccion_elsalvador_fire_suppression_651k_2017",
    "IGF::OT::IGF FIRE SUPPRESSION SYSTEMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0443_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1262",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0443_9700_W9127816D0102_9700 (empresa_construccion_elsalvador_fire_suppression_651k_2017). Signed 2017-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0443_9700_W9127816D0102_9700/.",
    "USASpending: empresa_construccion_elsalvador_fire_suppression_651k_2017 USD 0.651m. Supports empresa_construccion_elsalvador_fire_suppression_651k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 651081.5; date_signed 2017-09-27.",
    investment_type="epc",
)

# === Cycle 1262 ===
row_doc(
    "tss_elsalvador_ilea_fire_suppression_alarm_244k_2023",
    "infrastructure", "building_materials", "other",
    "Technology and Services Solutions — El Salvador ILEA fire suppression and alarm",
    "El Salvador",
    "3 Mar 2023: Department of State awards contract to TECHNOLOGY AND SERVICES SOLUTIONS S.A. DE C.V. for ILEA fire suppression and alarm system (PoP El Salvador); obligated USD 244719.11. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "244719.11", "2023-03-03", "2023", "", "",
    "ILEA FIRE SUPPRESSION AND ALARM SYSTEM, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tss_elsalvador_ilea_fire_suppression_alarm_244k_2023",
    "ILEA FIRE SUPPRESSION AND ALARM SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6023P0314_1900_-NONE-_-NONE-/",
    "Actor: TECHNOLOGY AND SERVICES SOLUTIONS S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1262",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6023P0314_1900_-NONE-_-NONE- (tss_elsalvador_ilea_fire_suppression_alarm_244k_2023). Signed 2023-03-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6023P0314_1900_-NONE-_-NONE-/.",
    "USASpending: tss_elsalvador_ilea_fire_suppression_alarm_244k_2023 USD 0.245m. Supports tss_elsalvador_ilea_fire_suppression_alarm_244k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 244719.11; date_signed 2023-03-03.",
    investment_type="epc",
)

# === Cycle 1262 ===
row_doc(
    "misc_dominican_espinosa_make_ready_27k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican landlord make-ready Mark Espinosa residence",
    "Dominican Republic",
    "23 Feb 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for LLD make-ready Mark Espinosa residence (PoP Dominican Republic); obligated USD 27782.17. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "27782.17", "2015-02-23", "2015", "", "",
    "LLD MAKE READY MARK ESPINOSA RESIDENCE : IGF::CL::IGF FOR CLOSELY ASSOCIATED, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_espinosa_make_ready_27k_2015",
    "LLD MAKE READY MARK ESPINOSA RESIDENCE : IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1097_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1262",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86015M1097_1900_-NONE-_-NONE- (misc_dominican_espinosa_make_ready_27k_2015). Signed 2015-02-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1097_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_espinosa_make_ready_27k_2015 USD 0.028m. Supports misc_dominican_espinosa_make_ready_27k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 27782.17; date_signed 2015-02-23.",
    investment_type="epc",
)

# === Cycle 1263 ===
row_doc(
    "hardline_uruguay_montevideo_psu_2098k_2011",
    "infrastructure", "building_materials", "us",
    "CTS-Hardline — Uruguay Montevideo embassy PSU",
    "Uruguay",
    "30 Sep 2011: Department of State awards contract to CTS-HARDLINE, LLC for Phase II/III physical security upgrade (PSU) U.S. Embassy Montevideo (PoP Uruguay); obligated USD 2098770.92. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2098770.92", "2011-09-30", "2011", "", "",
    "PHASE II/III PHYSICAL SECURITY UPGRADE (PSU), U.S. EMBASSY MONTEVIDEO., Uruguay (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hardline_uruguay_montevideo_psu_2098k_2011",
    "PHASE II/III PHYSICAL SECURITY UPGRADE (PSU), U.S. EMBASSY MONTEVIDEO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4745_1900_SAQMMA07D0010_1900/",
    "Actor: CTS-HARDLINE, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1263",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F4745_1900_SAQMMA07D0010_1900 (hardline_uruguay_montevideo_psu_2098k_2011). Signed 2011-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4745_1900_SAQMMA07D0010_1900/.",
    "USASpending: hardline_uruguay_montevideo_psu_2098k_2011 USD 2.099m. Supports hardline_uruguay_montevideo_psu_2098k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2098770.92; date_signed 2011-09-30.",
    investment_type="epc",
)

# === Cycle 1263 ===
row_doc(
    "alutiiq_mexico_fgr_ballistics_equip_3846k_2021",
    "infrastructure", "building_materials", "us",
    "Alutiiq Technical Services — Mexico City FGR ballistics project equipment",
    "Mexico",
    "16 Dec 2021: Department of State awards contract to ALUTIIQ TECHNICAL SERVICES LLC for purchase of FGR ballistics project equipment for Mexico City (PoP Mexico); obligated USD 3846686.22. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3846686.22", "2021-12-16", "2021", "", "",
    "PURCHASE OF FGR BALLISTICS PROJECT EQUIPMENT FOR MEXICO CITY, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_fgr_ballistics_equip_3846k_2021",
    "PURCHASE OF FGR BALLISTICS PROJECT EQUIPMENT FOR MEXICO CITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR22F5001_1900_19AQMM21D0040_1900/",
    "Actor: ALUTIIQ TECHNICAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1263",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMR22F5001_1900_19AQMM21D0040_1900 (alutiiq_mexico_fgr_ballistics_equip_3846k_2021). Signed 2021-12-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR22F5001_1900_19AQMM21D0040_1900/.",
    "USASpending: alutiiq_mexico_fgr_ballistics_equip_3846k_2021 USD 3.847m. Supports alutiiq_mexico_fgr_ballistics_equip_3846k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3846686.22; date_signed 2021-12-16.",
    investment_type="equipment_supply",
)

# === Cycle 1263 ===
row_doc(
    "tecpro_honduras_sofa_fire_hvac_1617k_2016",
    "infrastructure", "building_materials", "other",
    "Tecnología de Proyectos — Honduras SOFA fire protection/HVAC AAFES repair",
    "Honduras",
    "26 Sep 2016: Department of Defense awards contract to TECNOLOGIA DE PROYECTOS S.R.L. DE C.V. for SOFA agreement repair fire protection/HVAC AAFES (PoP Honduras); obligated USD 1617680.89. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1617680.89", "2016-09-26", "2016", "", "",
    "IGF::OT::IGF SOFA AGREEMENT REPAIR FIRE PROTECTION/HVAC AAFES, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tecpro_honduras_sofa_fire_hvac_1617k_2016",
    "IGF::OT::IGF SOFA AGREEMENT REPAIR FIRE PROTECTION/HVAC AAFES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127816D0103_9700/",
    "Actor: TECNOLOGIA DE PROYECTOS S.R.L. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1263",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0001_9700_W9127816D0103_9700 (tecpro_honduras_sofa_fire_hvac_1617k_2016). Signed 2016-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0001_9700_W9127816D0103_9700/.",
    "USASpending: tecpro_honduras_sofa_fire_hvac_1617k_2016 USD 1.618m. Supports tecpro_honduras_sofa_fire_hvac_1617k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1617680.89; date_signed 2016-09-26.",
    investment_type="epc",
)

# === Cycle 1263 ===
row_doc(
    "kone_mexico_elevator_replacement_149k_2025",
    "infrastructure", "building_materials", "other",
    "KONE México — elevator replacement",
    "Mexico",
    "15 Aug 2025: Department of State awards contract to KONE MEXICO SA DE CV for elevator replacement (PoP Mexico); obligated USD 149266.16. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "149266.16", "2025-08-15", "2025", "", "",
    "ELEVATOR REPLACEMENT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_kone_mexico_elevator_replacement_149k_2025",
    "ELEVATOR REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5325C0004_1900_-NONE-_-NONE-/",
    "Actor: KONE MEXICO SA DE CV — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1263",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5325C0004_1900_-NONE-_-NONE- (kone_mexico_elevator_replacement_149k_2025). Signed 2025-08-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5325C0004_1900_-NONE-_-NONE-/.",
    "USASpending: kone_mexico_elevator_replacement_149k_2025 USD 0.149m. Supports kone_mexico_elevator_replacement_149k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 149266.16; date_signed 2025-08-15.",
    investment_type="equipment_supply",
)

# === Cycle 1263 ===
row_doc(
    "misc_dominican_pulido_make_ready_27k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican landlord make-ready Roxanna Pulido",
    "Dominican Republic",
    "18 Aug 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for landlord make-ready work Roxanna Pulido (PoP Dominican Republic); obligated USD 27179.34. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "27179.34", "2014-08-18", "2014", "", "",
    "LANDLORD- MAKE READY WORK ROXANNA PULIDO : IGF::CL::IGF FOR CLOSELY ASSOCIATED, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_pulido_make_ready_27k_2014",
    "LANDLORD- MAKE READY WORK ROXANNA PULIDO : IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M1360_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1263",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86014M1360_1900_-NONE-_-NONE- (misc_dominican_pulido_make_ready_27k_2014). Signed 2014-08-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M1360_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_pulido_make_ready_27k_2014 USD 0.027m. Supports misc_dominican_pulido_make_ready_27k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 27179.34; date_signed 2014-08-18.",
    investment_type="epc",
)

# === Cycle 1264 ===
row_doc(
    "hardline_guyana_febr_replacement_2638k_2010",
    "infrastructure", "building_materials", "us",
    "CTS-Hardline — Guyana FE/BR product replacement",
    "Guyana",
    "24 Sep 2010: Department of State awards contract to CTS-HARDLINE, LLC for Phase III/IV forced entry/ballistic resistant (FE/BR) product replacement (PoP Guyana); obligated USD 2638169.27. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2638169.27", "2010-09-24", "2010", "", "",
    "PHASE III/IV FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND REPAIR & HARDWARE REPLACEMENT PR, Guyana (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hardline_guyana_febr_replacement_2638k_2010",
    "PHASE III/IV FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND REPAIR & HARDWARE REPLACEMENT PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F4608_1900_SAQMMA07D0010_1900/",
    "Actor: CTS-HARDLINE, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1264",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F4608_1900_SAQMMA07D0010_1900 (hardline_guyana_febr_replacement_2638k_2010). Signed 2010-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F4608_1900_SAQMMA07D0010_1900/.",
    "USASpending: hardline_guyana_febr_replacement_2638k_2010 USD 2.638m. Supports hardline_guyana_febr_replacement_2638k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2638169.27; date_signed 2010-09-24.",
    investment_type="equipment_supply",
)

# === Cycle 1264 ===
row_doc(
    "human_tech_haiti_ballistic_equipment_3386k_2026",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Haiti ballistic equipment delivery order",
    "Haiti",
    "16 Mar 2026: Department of State awards contract to HUMAN TECHNOLOGIES CORP for delivery order for ballistic equipment (PoP Haiti); obligated USD 3386557. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3386557", "2026-03-16", "2026", "", "",
    "NEW DELIVERY ORDER IN THE AMOUNT OF $3,386,557.00 FOR BALLISTIC EQUIPMENT WITH A DELIVERY DATE OF 07/24/26. TH, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_haiti_ballistic_equipment_3386k_2026",
    "NEW DELIVERY ORDER IN THE AMOUNT OF $3,386,557.00 FOR BALLISTIC EQUIPMENT WITH A DELIVERY DATE OF 07/24/26. THIS REQUIREMENT IS IN SUPPORT OF THE INL SECTION AT THE U.S. EMBASSY HAITI.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE26F0008_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1264",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE26F0008_1900_19AQMM21D0007_1900 (human_tech_haiti_ballistic_equipment_3386k_2026). Signed 2026-03-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE26F0008_1900_19AQMM21D0007_1900/.",
    "USASpending: human_tech_haiti_ballistic_equipment_3386k_2026 USD 3.387m. Supports human_tech_haiti_ballistic_equipment_3386k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3386557.0; date_signed 2026-03-16.",
    investment_type="equipment_supply",
)

# === Cycle 1264 ===
row_doc(
    "tecpro_honduras_fire_design_construct_368k_2019",
    "infrastructure", "building_materials", "other",
    "Tecnología de Proyectos — Honduras fire design/construct/repair",
    "Honduras",
    "20 Sep 2019: Department of Defense awards contract to TECNOLOGIA DE PROYECTOS S.R.L. DE C.V. for design/construct and repair of fire protection works (PoP Honduras); obligated USD 368587.89. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "368587.89", "2019-09-20", "2019", "", "",
    "THE PURPOSE OF THIS TASK ORDER IS TO DESIGN/ CONSTRUCT AND REPAIR OF FIRE SUPPRESSION SYSTEM (FSS), IN BLDG. 5, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tecpro_honduras_fire_design_construct_368k_2019",
    "THE PURPOSE OF THIS TASK ORDER IS TO DESIGN/ CONSTRUCT AND REPAIR OF FIRE SUPPRESSION SYSTEM (FSS), IN BLDG. 553, SOTO CANO AIR BASE, HONDURAS. TO BE PERFORMED UNDER THE CENTRAL AMERICAN MATOC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0440_9700_W9127816D0103_9700/",
    "Actor: TECNOLOGIA DE PROYECTOS S.R.L. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1264",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0440_9700_W9127816D0103_9700 (tecpro_honduras_fire_design_construct_368k_2019). Signed 2019-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0440_9700_W9127816D0103_9700/.",
    "USASpending: tecpro_honduras_fire_design_construct_368k_2019 USD 0.369m. Supports tecpro_honduras_fire_design_construct_368k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 368587.89; date_signed 2019-09-20.",
    investment_type="epc",
)

# === Cycle 1264 ===
row_doc(
    "tas_elsalvador_access_control_residence_hall_86k_2020",
    "infrastructure", "building_materials", "other",
    "TAS El Salvador — access control system residence hall",
    "El Salvador",
    "4 Mar 2020: Department of State awards contract to TAS EL SALVADOR S.A. DE C.V. for access control system residence hall (PoP El Salvador); obligated USD 86892.67. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "86892.67", "2020-03-04", "2020", "", "",
    "1930.1 ACCESS CONTROL SYSTEM RESIDENCE HALL, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_tas_elsalvador_access_control_residence_hall_86k_2020",
    "1930.1 ACCESS CONTROL SYSTEM RESIDENCE HALL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6020P0306_1900_-NONE-_-NONE-/",
    "Actor: TAS EL SALVADOR S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1264",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6020P0306_1900_-NONE-_-NONE- (tas_elsalvador_access_control_residence_hall_86k_2020). Signed 2020-03-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6020P0306_1900_-NONE-_-NONE-/.",
    "USASpending: tas_elsalvador_access_control_residence_hall_86k_2020 USD 0.087m. Supports tas_elsalvador_access_control_residence_hall_86k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 86892.67; date_signed 2020-03-04.",
    investment_type="equipment_supply",
)

# === Cycle 1264 ===
row_doc(
    "misc_dominican_maupin_make_ready_25k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican landlord make-ready Stacey Maupin residence",
    "Dominican Republic",
    "10 Jul 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for landlord make-ready work Stacey Maupin residence (PoP Dominican Republic); obligated USD 25556.85. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "25556.85", "2014-07-10", "2014", "", "",
    "LANDLORD- MAKE READY WORK STACEY MAUPIN RESIDENCE : IGF::CL::IGF FOR CLOSELY ASSOCIATED, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_maupin_make_ready_25k_2014",
    "LANDLORD- MAKE READY WORK STACEY MAUPIN RESIDENCE : IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M1599_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1264",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86014M1599_1900_-NONE-_-NONE- (misc_dominican_maupin_make_ready_25k_2014). Signed 2014-07-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M1599_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_maupin_make_ready_25k_2014 USD 0.026m. Supports misc_dominican_maupin_make_ready_25k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 25556.85; date_signed 2014-07-10.",
    investment_type="epc",
)

# === Cycle 1265 ===
row_doc(
    "alutiiq_mexico_ibis_ballistics_2577k_2025",
    "infrastructure", "building_materials", "us",
    "Alutiiq — Mexico IBIS ballistics hardware/software for state AGs",
    "Mexico",
    "25 Nov 2025: Department of State awards contract to ALUTIIQ TECHNICAL SERVICES LLC for IBIS ballistics hardware and software for Mexican state attorneys general (PoP Mexico); obligated USD 2577613. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2577613", "2025-11-25", "2025", "", "",
    "IBIS BALLISTICS HARDWARE AND SOFTWARE FOR MEXICAN STATE ATTORNEYS GENERAL OFFICES, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_ibis_ballistics_2577k_2025",
    "IBIS BALLISTICS HARDWARE AND SOFTWARE FOR MEXICAN STATE ATTORNEYS GENERAL OFFICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F0001_1900_19AQMM21D0040_1900/",
    "Actor: ALUTIIQ TECHNICAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1265",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM26F0001_1900_19AQMM21D0040_1900 (alutiiq_mexico_ibis_ballistics_2577k_2025). Signed 2025-11-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F0001_1900_19AQMM21D0040_1900/.",
    "USASpending: alutiiq_mexico_ibis_ballistics_2577k_2025 USD 2.578m. Supports alutiiq_mexico_ibis_ballistics_2577k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2577613.0; date_signed 2025-11-25.",
    investment_type="equipment_supply",
)

# === Cycle 1265 ===
row_doc(
    "meltech_bahamas_nassau_chancery_roof_301k_2014",
    "infrastructure", "building_materials", "us",
    "Meltech — Bahamas Nassau office building chancery roof replacement",
    "Bahamas",
    "20 Aug 2014: Department of State awards contract to MELTECH CORPORATION, INC. for Nassau Bahamas office building chancery roof replacement (PoP Bahamas); obligated USD 301482.92. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "301482.92", "2014-08-20", "2014", "", "",
    "IGF::OT::IGF NASSAU, THE BAHAMAS OFFICE BUILDING CHANCERY ROOF REPLACEMENT PROJECT AWARDED TO MELTECH CORP, IN, Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_meltech_bahamas_nassau_chancery_roof_301k_2014",
    "IGF::OT::IGF NASSAU, THE BAHAMAS OFFICE BUILDING CHANCERY ROOF REPLACEMENT PROJECT AWARDED TO MELTECH CORP, INC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F2829_1900_SAQMMA13D0128_1900/",
    "Actor: MELTECH CORPORATION, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1265",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14F2829_1900_SAQMMA13D0128_1900 (meltech_bahamas_nassau_chancery_roof_301k_2014). Signed 2014-08-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F2829_1900_SAQMMA13D0128_1900/.",
    "USASpending: meltech_bahamas_nassau_chancery_roof_301k_2014 USD 0.301m. Supports meltech_bahamas_nassau_chancery_roof_301k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 301482.92; date_signed 2014-08-20.",
    investment_type="epc",
)

# === Cycle 1265 ===
row_doc(
    "empresa_construccion_honduras_soto_cano_roof_1109k_2020",
    "infrastructure", "building_materials", "other",
    "Empresa de Construcción y Transporte — Soto Cano roof repairs",
    "Honduras",
    "29 Sep 2020: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for roof repairs at Soto Cano (PoP Honduras); obligated USD 1109306.20. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1109306.20", "2020-09-29", "2020", "", "",
    "ROOF REPAIRS AT SOTO CANO., Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_empresa_construccion_honduras_soto_cano_roof_1109k_2020",
    "ROOF REPAIRS AT SOTO CANO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0543_9700_W9127816D0102_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1265",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127820F0543_9700_W9127816D0102_9700 (empresa_construccion_honduras_soto_cano_roof_1109k_2020). Signed 2020-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0543_9700_W9127816D0102_9700/.",
    "USASpending: empresa_construccion_honduras_soto_cano_roof_1109k_2020 USD 1.109m. Supports empresa_construccion_honduras_soto_cano_roof_1109k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1109306.2; date_signed 2020-09-29.",
    investment_type="epc",
)

# === Cycle 1265 ===
row_doc(
    "gamma_mexico_musset_elevator_modernization_63k_2019",
    "infrastructure", "building_materials", "other",
    "Despacho de Arquitectos Gamma — Mexico Musset hydraulic elevator modernization",
    "Mexico",
    "17 Sep 2019: Department of State awards contract to DESPACHO DE ARQUITECTOS GAMMA for hydraulic elevator modernization at Musset 337 (PoP Mexico); obligated USD 63152.69. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "63152.69", "2019-09-17", "2019", "", "",
    "MEX-FAC-7902 HYDRAULILC ELEVATOR MODERNIZATION AT MUSSET 337, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_gamma_mexico_musset_elevator_modernization_63k_2019",
    "MEX-FAC-7902 HYDRAULILC ELEVATOR MODERNIZATION AT MUSSET 337",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319C0027_1900_-NONE-_-NONE-/",
    "Actor: DESPACHO DE ARQUITECTOS GAMMA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1265",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5319C0027_1900_-NONE-_-NONE- (gamma_mexico_musset_elevator_modernization_63k_2019). Signed 2019-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319C0027_1900_-NONE-_-NONE-/.",
    "USASpending: gamma_mexico_musset_elevator_modernization_63k_2019 USD 0.063m. Supports gamma_mexico_musset_elevator_modernization_63k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 63152.69; date_signed 2019-09-17.",
    investment_type="epc",
)

# === Cycle 1265 ===
row_doc(
    "misc_dominican_lbb13_make_ready_22k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican LBB 13 make-ready",
    "Dominican Republic",
    "30 Apr 2025: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC make-ready work LBB 13 PID 836 (PoP Dominican Republic); obligated USD 22440.42. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "22440.42", "2025-04-30", "2025", "", "",
    "FAC-MAKE READY WORK LBB 13 PID 836 ICASS-CONS-AWARD, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_lbb13_make_ready_22k_2025",
    "FAC-MAKE READY WORK LBB 13 PID 836 ICASS-CONS-AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8625C0033_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1265",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8625C0033_1900_-NONE-_-NONE- (misc_dominican_lbb13_make_ready_22k_2025). Signed 2025-04-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8625C0033_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_lbb13_make_ready_22k_2025 USD 0.022m. Supports misc_dominican_lbb13_make_ready_22k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 22440.42; date_signed 2025-04-30.",
    investment_type="epc",
)

# === Cycle 1266 ===
row_doc(
    "hollingsworth_elsalvador_roof_ae_632k_2024",
    "infrastructure", "engineering_epc", "us",
    "Hollingsworth-Pack — El Salvador A+E roof replacement design",
    "El Salvador",
    "25 Jan 2024: Department of State awards contract to HOLLINGSWORTH-PACK CORPORATION for A+E services to design roof replacements at San Salvador (PoP El Salvador); obligated USD 632518.27. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "632518.27", "2024-01-25", "2024", "", "",
    "SAN SALVADOR, EL SALVADOR - A+E SERVICES TO DESIGN ROOF REPLACEMENTS AND REPAIRS FOR MULTIPLE BUILDINGS, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hollingsworth_elsalvador_roof_ae_632k_2024",
    "SAN SALVADOR, EL SALVADOR - A+E SERVICES TO DESIGN ROOF REPLACEMENTS AND REPAIRS FOR MULTIPLE BUILDINGS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024F0111_1900_19GE5022D0009_1900/",
    "Actor: HOLLINGSWORTH-PACK CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1266",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5024F0111_1900_19GE5022D0009_1900 (hollingsworth_elsalvador_roof_ae_632k_2024). Signed 2024-01-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024F0111_1900_19GE5022D0009_1900/.",
    "USASpending: hollingsworth_elsalvador_roof_ae_632k_2024 USD 0.633m. Supports hollingsworth_elsalvador_roof_ae_632k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 632518.27; date_signed 2024-01-25.",
    investment_type="epc",
)

# === Cycle 1266 ===
row_doc(
    "ge_jamaica_switchgear_parts_135k_2016",
    "energy", "power_plants_grid", "us",
    "General Electric International — Jamaica NEC switchgear replacement parts",
    "Jamaica",
    "14 Sep 2016: Department of State awards contract to GENERAL ELECTRIC INTERNATIONAL, INC. for FAC replacement switch gear parts NEC 7901.C (PoP Jamaica); obligated USD 135947.50. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "135947.50", "2016-09-14", "2016", "", "",
    "IGF::OT::IGF FAC- REPLACEMENT SWITCH GEAR PARTS - NEC (7901.C), Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_ge_jamaica_switchgear_parts_135k_2016",
    "IGF::OT::IGF FAC- REPLACEMENT SWITCH GEAR PARTS - NEC (7901.C)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016M1265_1900_-NONE-_-NONE-/",
    "Actor: GENERAL ELECTRIC INTERNATIONAL, INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1266",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37016M1265_1900_-NONE-_-NONE- (ge_jamaica_switchgear_parts_135k_2016). Signed 2016-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37016M1265_1900_-NONE-_-NONE-/.",
    "USASpending: ge_jamaica_switchgear_parts_135k_2016 USD 0.136m. Supports ge_jamaica_switchgear_parts_135k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 135947.5; date_signed 2016-09-14.",
    investment_type="equipment_supply",
)

# === Cycle 1266 ===
row_doc(
    "empresa_construccion_honduras_soto_cano_roof_389k_2022",
    "infrastructure", "building_materials", "other",
    "Empresa de Construcción y Transporte — Soto Cano AB roof repair",
    "Honduras",
    "30 Sep 2022: Department of Defense awards contract to EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. for roof repair Soto Cano AB (PoP Honduras); obligated USD 389425.45. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "389425.45", "2022-09-30", "2022", "", "",
    "ROOF REPAIR SOTO CANO AB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_empresa_construccion_honduras_soto_cano_roof_389k_2022",
    "ROOF REPAIR SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0387_9700_W9127821D0075_9700/",
    "Actor: EMPRESA DE CONSTRUCCION Y TRANSPORTE ETERNA S.A. DE C.V. — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1266",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0387_9700_W9127821D0075_9700 (empresa_construccion_honduras_soto_cano_roof_389k_2022). Signed 2022-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0387_9700_W9127821D0075_9700/.",
    "USASpending: empresa_construccion_honduras_soto_cano_roof_389k_2022 USD 0.389m. Supports empresa_construccion_honduras_soto_cano_roof_389k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 389425.45; date_signed 2022-09-30.",
    investment_type="epc",
)

# === Cycle 1266 ===
row_doc(
    "misc_argentina_guemes_make_ready_21k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina Guemes 469 make-ready",
    "Argentina",
    "28 Jul 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FM works to complete make-ready at Guemes 469 (PoP Argentina); obligated USD 21952.02. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "21952.02", "2015-07-28", "2015", "", "",
    "FM-WORKS TO COMPLETE MAKE READY @ GUEMES 469 IGF::OT::IGF, Argentina (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_guemes_make_ready_21k_2015",
    "FM-WORKS TO COMPLETE MAKE READY @ GUEMES 469 IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20015M0422_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1266",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20015M0422_1900_-NONE-_-NONE- (misc_argentina_guemes_make_ready_21k_2015). Signed 2015-07-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20015M0422_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_guemes_make_ready_21k_2015 USD 0.022m. Supports misc_argentina_guemes_make_ready_21k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 21952.02; date_signed 2015-07-28.",
    investment_type="epc",
)

# === Cycle 1266 ===
row_doc(
    "misc_dominican_steckler_make_ready_23k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican landlord make-ready Adam Steckler residence",
    "Dominican Republic",
    "12 May 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for landlord make-ready Adam Steckler residence (PoP Dominican Republic); obligated USD 23047.03. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "23047.03", "2014-05-12", "2014", "", "",
    "LANDLORD- MAKE READY ADAM STECKLER RESIDENCE   IGF::CL::IGF FOR CLOSELY ASSOCIATED, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_steckler_make_ready_23k_2014",
    "LANDLORD- MAKE READY ADAM STECKLER RESIDENCE   IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M1127_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1266",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86014M1127_1900_-NONE-_-NONE- (misc_dominican_steckler_make_ready_23k_2014). Signed 2014-05-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M1127_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_steckler_make_ready_23k_2014 USD 0.023m. Supports misc_dominican_steckler_make_ready_23k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 23047.03; date_signed 2014-05-12.",
    investment_type="epc",
)

# === Cycle 1267 ===
row_doc(
    "perimeter_security_bahamas_exuma_gates_85k_2011",
    "infrastructure", "building_materials", "us",
    "Perimeter Security Solutions — Bahamas Exuma gates furnish/install",
    "Bahamas",
    "20 Jan 2011: Department of State awards contract to PERIMETER SECURITY SOLUTIONS, INC. for LF furnish and install gates in Exuma (PoP Bahamas); obligated USD 85000. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "85000", "2011-01-20", "2011", "", "",
    "LF-FURNISH AND INSTALL GATES IN EXUMA, Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_perimeter_security_bahamas_exuma_gates_85k_2011",
    "LF-FURNISH AND INSTALL GATES IN EXUMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50011F0002_1900_GS07F6069R_4730/",
    "Actor: PERIMETER SECURITY SOLUTIONS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1267",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50011F0002_1900_GS07F6069R_4730 (perimeter_security_bahamas_exuma_gates_85k_2011). Signed 2011-01-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50011F0002_1900_GS07F6069R_4730/.",
    "USASpending: perimeter_security_bahamas_exuma_gates_85k_2011 USD 0.085m. Supports perimeter_security_bahamas_exuma_gates_85k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 85000.0; date_signed 2011-01-20.",
    investment_type="equipment_supply",
)

# === Cycle 1267 ===
row_doc(
    "daikin_panama_chiller_driver_install_4k_2019",
    "energy", "power_plants_grid", "us",
    "Daikin Applied Latin America — Panama chiller driver supply/install",
    "Panama",
    "29 Jul 2019: Smithsonian Institution awards contract to DAIKIN APPLIED LATIN AMERICA, L.L.C. for supply and installation of driver at chillers (PoP Panama); obligated USD 4508.46. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "4508.46", "2019-07-29", "2019", "", "",
    "SUPPLY AND INSTALLATION OF DRIVER AT CHILLERS, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_daikin_panama_chiller_driver_install_4k_2019",
    "SUPPLY AND INSTALLATION OF DRIVER AT CHILLERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312919P00428346_3300_-NONE-_-NONE-/",
    "Actor: DAIKIN APPLIED LATIN AMERICA, L.L.C. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1267",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33312919P00428346_3300_-NONE-_-NONE- (daikin_panama_chiller_driver_install_4k_2019). Signed 2019-07-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312919P00428346_3300_-NONE-_-NONE-/.",
    "USASpending: daikin_panama_chiller_driver_install_4k_2019 USD 0.005m. Supports daikin_panama_chiller_driver_install_4k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4508.46; date_signed 2019-07-29.",
    investment_type="equipment_supply",
)

# === Cycle 1267 ===
row_doc(
    "misc_dominican_flores_make_ready_22k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican DAO housing make-ready Leonardo Flores residence",
    "Dominican Republic",
    "20 May 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for DAO housing make-ready Leonardo Flores residence (PoP Dominican Republic); obligated USD 22772.07. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "22772.07", "2015-05-20", "2015", "", "",
    "DAO-HOUSING MAKE READY. LEONARDO FLORES RESIDENCE: IGF::CL::IGF FOR CLOSELY ASSOCIATED, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_flores_make_ready_22k_2015",
    "DAO-HOUSING MAKE READY. LEONARDO FLORES RESIDENCE: IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1381_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1267",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86015M1381_1900_-NONE-_-NONE- (misc_dominican_flores_make_ready_22k_2015). Signed 2015-05-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1381_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_flores_make_ready_22k_2015 USD 0.023m. Supports misc_dominican_flores_make_ready_22k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 22772.07; date_signed 2015-05-20.",
    investment_type="epc",
)

# === Cycle 1267 ===
row_doc(
    "misc_dominican_daboville_make_ready_22k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican LLD make-ready Karen D'Aboville residence",
    "Dominican Republic",
    "5 Feb 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for LLD make-ready Karen D'Aboville residence (PoP Dominican Republic); obligated USD 22432.31. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "22432.31", "2015-02-05", "2015", "", "",
    "LLD MAKE READY KAREN D'ABOVILLE RESIDENCE: IGF::CL::IGF FOR CLOSELY ASSOCIATED, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_daboville_make_ready_22k_2015",
    "LLD MAKE READY KAREN D'ABOVILLE RESIDENCE: IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M0854_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1267",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86015M0854_1900_-NONE-_-NONE- (misc_dominican_daboville_make_ready_22k_2015). Signed 2015-02-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M0854_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_daboville_make_ready_22k_2015 USD 0.022m. Supports misc_dominican_daboville_make_ready_22k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 22432.31; date_signed 2015-02-05.",
    investment_type="epc",
)

# === Cycle 1267 ===
row_doc(
    "misc_argentina_guemes_martinez_make_ready_21k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina Guemes 469 Martinez make-ready",
    "Argentina",
    "14 Jul 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FM make-ready 2014 Guemes 469 Martinez (PoP Argentina); obligated USD 21839.42. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "21839.42", "2014-07-14", "2014", "", "",
    "FM - MAKE READY 2014 - GUEMES 469, MARTINEZ IGF::OT::IGF, Argentina (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_guemes_martinez_make_ready_21k_2014",
    "FM - MAKE READY 2014 - GUEMES 469, MARTINEZ IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20014M0348_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1267",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20014M0348_1900_-NONE-_-NONE- (misc_argentina_guemes_martinez_make_ready_21k_2014). Signed 2014-07-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20014M0348_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_guemes_martinez_make_ready_21k_2014 USD 0.022m. Supports misc_argentina_guemes_martinez_make_ready_21k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 21839.42; date_signed 2014-07-14.",
    investment_type="epc",
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
        w.writeheader(); w.writerows(rows)
    EVID.mkdir(parents=True, exist_ok=True)
    for row, ev, _bib in ITEMS:
        (EVID / f"{row['id']}.json").write_text(json.dumps(ev, indent=2) + "\n", encoding="utf-8")
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
            bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")

if __name__ == "__main__":
    main()
