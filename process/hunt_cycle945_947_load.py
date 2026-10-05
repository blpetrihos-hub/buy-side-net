#!/usr/bin/env python3
"""Cycles 945–947: USASpending page-3 residual CapEx.

Seeds: 20261945–20261947. Thin top-up dry.
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

row_doc(
    "bonatti_gt_medical_clinic_1p29m_2025",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 Guatemala HAP 70421 medical clinic design & construction",
    "Guatemala",
    "13 Jan 2025: USACE awards task order W9127825F0048 to Bonatti for HAP 70421 medical clinic design & construction; obligated USD 1,287,627.08. CapEx face = award obligation. Distinct from bonatti_champerico_school.",
    "1287627.08", "2025-01-13", "2025", "14.635", "-90.507",
    "Medical clinic design/construction, Guatemala (USASpending PoP Guatemala; national pin).",
    "usaspending_bonatti_gt_medical_clinic_1p29m_2025",
    "HAP 70421 MEDICAL CLINIC DESIGN & CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825F0048_9700_W9127823D0072_9700/",
    "Actor: Bonatti (Guatemala) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle945",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825F0048_9700_W9127823D0072_9700 (Bonatti GT medical clinic). Signed 2025-01-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825F0048_9700_W9127823D0072_9700/.",
    "USASpending: Bonatti GT medical clinic USD 1.288m. Supports bonatti_gt_medical_clinic_1p29m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1287627.08; date_signed 2025-01-13.",
)

row_doc(
    "bonatti_gt_drw_962k_2025",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 Guatemala HAP 41940 disaster relief warehouse",
    "Guatemala",
    "15 Jan 2025: USACE awards task order W9127825F0052 to Bonatti for design and construction of HAP 41940 disaster relief warehouse; obligated USD 961,543.11. CapEx face = award obligation.",
    "961543.11", "2025-01-15", "2025", "14.635", "-90.507",
    "Disaster relief warehouse, Guatemala (USASpending PoP Guatemala; national pin).",
    "usaspending_bonatti_gt_drw_962k_2025",
    "DESIGN AND CONSTRUCTION OF HAP 41940 DISASTER RELIEF WAREHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825F0052_9700_W9127823D0072_9700/",
    "Actor: Bonatti (Guatemala) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle945",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825F0052_9700_W9127823D0072_9700 (Bonatti GT DRW). Signed 2025-01-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825F0052_9700_W9127823D0072_9700/.",
    "USASpending: Bonatti GT DRW USD 0.962m. Supports bonatti_gt_drw_962k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 961543.11; date_signed 2025-01-15.",
)

row_doc(
    "eterna_soto_cano_chapel_2p46m_2017",
    "infrastructure", "building_materials", "other",
    "Eterna \u2014 Soto Cano Air Base chapel facility",
    "Honduras",
    "26 Sep 2017: USACE awards task order W9127817F0404 to Eterna for chapel facility, Soto Cano AB, Honduras; obligated USD 2,462,431.95. CapEx face = award obligation.",
    "2462431.95", "2017-09-26", "2017", "14.382", "-87.621",
    "Chapel facility, Soto Cano Air Base, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_soto_cano_chapel_2p46m_2017",
    "IGF::OT::IGF CHAPEL FACILITY, SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0404_9700_W9127816D0102_9700/",
    "Actor: Eterna (Honduras) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle945",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0404_9700_W9127816D0102_9700 (Eterna Soto Cano chapel). Signed 2017-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0404_9700_W9127816D0102_9700/.",
    "USASpending: Eterna Soto Cano chapel USD 2.462m. Supports eterna_soto_cano_chapel_2p46m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2462431.95; date_signed 2017-09-26.",
)

row_doc(
    "brasilia_nec_power_infra_754k_2026",
    "infrastructure", "power_plants_grid", "other",
    "Miscellaneous foreign awardee \u2014 Bras\u00edlia NEC permanent power infrastructure",
    "Brazil",
    "24 Jul 2026: Department of State awards contract 19GE5026C0067 for design and construction of NEC permanent power infrastructure at U.S. Embassy Bras\u00edlia; obligated USD 753,874.67. CapEx face = award obligation.",
    "753874.67", "2026-07-24", "2026", "-15.797", "-47.892",
    "NEC permanent power infrastructure, U.S. Embassy Bras\u00edlia, Brazil (USASpending PoP Brazil).",
    "usaspending_brasilia_nec_power_infra_754k_2026",
    "DESIGN AND CONSTRUCTION OF NEC PERMANENT POWER INFRASTRUCTURE AT U.S. EMBASSY BRASILIA, BRAZIL.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0067_1900_-NONE-_-NONE-/",
    "Actor: Miscellaneous foreign awardee \u2014 other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle945",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5026C0067_1900_-NONE-_-NONE- (Bras\u00edlia NEC power). Signed 2026-07-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5026C0067_1900_-NONE-_-NONE-/.",
    "USASpending: Bras\u00edlia NEC power USD 0.754m. Supports brasilia_nec_power_infra_754k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 753874.67; date_signed 2026-07-24.",
)

row_doc(
    "bonatti_honduras_clinic_fire_1p91m_2021",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 Honduras medical clinic, fire station, maternity ward",
    "Honduras",
    "17 Jun 2021: USACE awards task order W9127821F0207 to Bonatti for HAP medical clinic, fire station, and maternity ward; obligated USD 1,914,686.44. CapEx face = award obligation.",
    "1914686.44", "2021-06-17", "2021", "14.072", "-87.192",
    "Medical clinic / fire station / maternity ward, Honduras (USASpending PoP Honduras; national pin).",
    "usaspending_bonatti_honduras_clinic_fire_1p91m_2021",
    "HAP #39591 MEDICAL CLINIC, HAP #39288 FIRE STATION, HAP #39287 MATERNITY WARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0207_9700_W9127816D0099_9700/",
    "Actor: Bonatti (Guatemala) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle945",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0207_9700_W9127816D0099_9700 (Bonatti Honduras clinic/fire). Signed 2021-06-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0207_9700_W9127816D0099_9700/.",
    "USASpending: Bonatti Honduras clinic/fire USD 1.915m. Supports bonatti_honduras_clinic_fire_1p91m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1914686.44; date_signed 2021-06-17.",
)

row_doc(
    "edifice_haiti_construction_4p71m_2016",
    "infrastructure", "building_materials", "us",
    "Edifice Worldwide LLC \u2014 Haiti construction/repairs",
    "Haiti",
    "29 Sep 2016: Department of State awards task order SAQMMA16F5447 to Edifice Worldwide LLC for construction/repairs (PoP Haiti); obligated USD 4,714,556.99. CapEx face = award obligation. Distinct from edifice_hnp_academy_reno.",
    "4714556.99", "2016-09-29", "2016", "18.540", "-72.339",
    "Construction/repairs, Haiti (USASpending PoP Haiti; Port-au-Prince pin).",
    "usaspending_edifice_haiti_construction_4p71m_2016",
    "CONSTRUCTION/REPAIRS. IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5447_1900_SAQMMA14D0048_1900/",
    "Actor: Edifice Worldwide (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle946",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F5447_1900_SAQMMA14D0048_1900 (Edifice Haiti construction). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5447_1900_SAQMMA14D0048_1900/.",
    "USASpending: Edifice Haiti construction USD 4.715m. Supports edifice_haiti_construction_4p71m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4714556.99; date_signed 2016-09-29.",
)

row_doc(
    "tseng_haiti_clinics_4p82m_2018",
    "infrastructure", "building_materials", "us",
    "Tseng Consulting Group \u2014 eleven Hurricane Matthew-damaged health clinics rehab",
    "Haiti",
    "27 Sep 2018: USAID awards contract 72052118C00002 to Tseng Consulting Group for renovation/rehab/utility upgrade of eleven Hurricane Matthew-damaged health clinics; obligated USD 4,819,094.69. CapEx face = award obligation.",
    "4819094.69", "2018-09-27", "2018", "18.540", "-72.339",
    "Eleven Hurricane Matthew-damaged health clinics rehab, Haiti (USASpending PoP Haiti).",
    "usaspending_tseng_haiti_clinics_4p82m_2018",
    "RENOVATION, REHABILITATION, REPAIR AND UTILITY UPGRADE OF ELEVEN HURRICANE MATTHEW-DAMAGED HEALTH CLINICS AND ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_72052118C00002_7200_-NONE-_-NONE-/",
    "Actor: Tseng Consulting (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle946",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_72052118C00002_7200_-NONE-_-NONE- (Tseng Haiti clinics). Signed 2018-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_72052118C00002_7200_-NONE-_-NONE-/.",
    "USASpending: Tseng Haiti clinics USD 4.819m. Supports tseng_haiti_clinics_4p82m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4819094.69; date_signed 2018-09-27.",
)

row_doc(
    "kunkel_culebra_fire_1p44m_2019",
    "infrastructure", "building_materials", "other",
    "Kunkel Construction \u2014 Culebra fire protection system construction",
    "Panama",
    "23 Sep 2019: Smithsonian awards contract 33330219CF0010425 to Kunkel for fire protection system at Culebra project; obligated USD 1,438,645.74. CapEx face = award obligation.",
    "1438645.74", "2019-09-23", "2019", "8.982", "-79.520",
    "Fire protection system, Culebra / STRI, Panama (USASpending PoP Panama).",
    "usaspending_kunkel_culebra_fire_1p44m_2019",
    "CONSTRUCTION SERVICES FOR THE FIRE PROTECTION SYSTEM AT CULEBRA PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219CF0010425_3300_-NONE-_-NONE-/",
    "Actor: Kunkel (Panama) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle946",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330219CF0010425_3300_-NONE-_-NONE- (Kunkel Culebra fire). Signed 2019-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219CF0010425_3300_-NONE-_-NONE-/.",
    "USASpending: Kunkel Culebra fire USD 1.439m. Supports kunkel_culebra_fire_1p44m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1438645.74; date_signed 2019-09-23.",
)

row_doc(
    "colibri_peru_school_1p38m_2015",
    "infrastructure", "building_materials", "other",
    "Colibr\u00ed Proyectos & Servicios \u2014 Peru school construction HAP",
    "Peru",
    "13 Aug 2015: DoD awards contract W912CL15C0004 to Colibr\u00ed for school construction HAP; obligated USD 1,376,181.64. CapEx face = award obligation.",
    "1376181.64", "2015-08-13", "2015", "-12.046", "-77.043",
    "School construction HAP, Peru (USASpending PoP Peru; national pin).",
    "usaspending_colibri_peru_school_1p38m_2015",
    "IGF::OT::IGF SCHOOL CONSTRUCTION HAP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL15C0004_9700_-NONE-_-NONE-/",
    "Actor: Colibr\u00ed (Peru) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle946",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL15C0004_9700_-NONE-_-NONE- (Colibr\u00ed Peru school). Signed 2015-08-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL15C0004_9700_-NONE-_-NONE-/.",
    "USASpending: Colibr\u00ed Peru school USD 1.376m. Supports colibri_peru_school_1p38m_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1376181.64; date_signed 2015-08-13.",
)

row_doc(
    "pem_guatemala_pnc_barracks_781k_2022",
    "infrastructure", "building_materials", "us",
    "Property & Environmental Management Inc. \u2014 Guatemala PNC barracks renovation",
    "Guatemala",
    "23 May 2022: Department of State awards contract 19AQMM22C0109 to PEM for Guatemala PNC barracks renovation; obligated USD 780,688.04. CapEx face = award obligation.",
    "780688.04", "2022-05-23", "2022", "14.635", "-90.507",
    "PNC barracks renovation, Guatemala (USASpending PoP Guatemala).",
    "usaspending_pem_guatemala_pnc_barracks_781k_2022",
    "GUATEMALA PNC BARRACKS RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0109_1900_-NONE-_-NONE-/",
    "Actor: PEM Inc. (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle946",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22C0109_1900_-NONE-_-NONE- (PEM Guatemala PNC barracks). Signed 2022-05-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0109_1900_-NONE-_-NONE-/.",
    "USASpending: PEM Guatemala PNC barracks USD 0.781m. Supports pem_guatemala_pnc_barracks_781k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 780688.04; date_signed 2022-05-23.",
)

row_doc(
    "comp_roof_guatemala_1p17m_2008",
    "infrastructure", "building_materials", "us",
    "Competition Roofing Inc. \u2014 Guatemala roof replacement",
    "Guatemala",
    "24 Sep 2008: Department of State awards task order SAQMMA08F6846 to Competition Roofing for Guatemala roof replacement; obligated USD 1,171,424. CapEx face = award obligation. Distinct from comp_roof_lapaz.",
    "1171424", "2008-09-24", "2008", "14.635", "-90.507",
    "Roof replacement, Guatemala (USASpending PoP Guatemala).",
    "usaspending_comp_roof_guatemala_1p17m_2008",
    "GUATEMALA ROOF REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA08F6846_1900_SALMEC07D0032_1900/",
    "Actor: Competition Roofing (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle947",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA08F6846_1900_SALMEC07D0032_1900 (Competition Roofing Guatemala). Signed 2008-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA08F6846_1900_SALMEC07D0032_1900/.",
    "USASpending: Competition Roofing Guatemala USD 1.171m. Supports comp_roof_guatemala_1p17m_2008.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1171424; date_signed 2008-09-24.",
)

row_doc(
    "falcon_panama_hvac_1p03m_2010",
    "infrastructure", "building_materials", "us",
    "Falcon Spectrum JV \u2014 Panama PCC piping networks and HVAC chiller replacement",
    "Panama",
    "12 Jan 2010: Department of State awards task order SAQMMA10F0471 to Falcon Spectrum JV for replacement of PCC piping networks and HVAC chiller system in Panama; obligated USD 1,026,431. CapEx face = award obligation.",
    "1026431", "2010-01-12", "2010", "8.982", "-79.520",
    "PCC piping / HVAC chiller replacement, Panama (USASpending PoP Panama).",
    "usaspending_falcon_panama_hvac_1p03m_2010",
    "REPLACEMENT OF PCC PIPING NETWORKS&HVAC CHILLER SYSTEM IN PANAMA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F0471_1900_SAQMMA08D0016_1900/",
    "Actor: Falcon Spectrum JV (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle947",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F0471_1900_SAQMMA08D0016_1900 (Falcon Panama HVAC). Signed 2010-01-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F0471_1900_SAQMMA08D0016_1900/.",
    "USASpending: Falcon Panama HVAC USD 1.026m. Supports falcon_panama_hvac_1p03m_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1026431; date_signed 2010-01-12.",
)

row_doc(
    "tidewater_guayaquil_construction_586k_2018",
    "infrastructure", "building_materials", "us",
    "Tidewater, Inc. \u2014 Guayaquil construction",
    "Ecuador",
    "16 Nov 2018: Department of State awards task order 19AQMM19F0121 to Tidewater for construction Guayaquil; obligated USD 586,349. CapEx face = award obligation. Distinct from montage_guayaquil_msgr.",
    "586349", "2018-11-16", "2018", "-2.171", "-79.922",
    "Construction, Guayaquil, Ecuador (USASpending PoP Ecuador).",
    "usaspending_tidewater_guayaquil_construction_586k_2018",
    "CONSTRUCTION GUAYAQUIL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F0121_1900_SAQMMA14D0045_1900/",
    "Actor: Tidewater (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle947",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19F0121_1900_SAQMMA14D0045_1900 (Tidewater Guayaquil). Signed 2018-11-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F0121_1900_SAQMMA14D0045_1900/.",
    "USASpending: Tidewater Guayaquil USD 0.586m. Supports tidewater_guayaquil_construction_586k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 586349; date_signed 2018-11-16.",
)

row_doc(
    "serrano_galapagos_eoc_551k_2010",
    "infrastructure", "building_materials", "other",
    "Serrano Proa\u00f1o \u2014 Gal\u00e1pagos EOC facility",
    "Ecuador",
    "29 Sep 2010: DoD awards contract W9127810C0123 to Serrano Proa\u00f1o for EOC facility, Gal\u00e1pagos, Ecuador; obligated USD 550,619.05. CapEx face = award obligation.",
    "550619.05", "2010-09-29", "2010", "-0.744", "-90.313",
    "EOC facility, Gal\u00e1pagos, Ecuador (USASpending PoP Ecuador; Gal\u00e1pagos pin).",
    "usaspending_serrano_galapagos_eoc_551k_2010",
    "BASE BID AWARD FOR EOC FACILITY, GALAPAGOS, ECUADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810C0123_9700_-NONE-_-NONE-/",
    "Actor: Serrano Proa\u00f1o (Ecuador) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle947",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127810C0123_9700_-NONE-_-NONE- (Serrano Gal\u00e1pagos EOC). Signed 2010-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810C0123_9700_-NONE-_-NONE-/.",
    "USASpending: Serrano Gal\u00e1pagos EOC USD 0.551m. Supports serrano_galapagos_eoc_551k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 550619.05; date_signed 2010-09-29.",
)

row_doc(
    "oeg_san_salvador_electrical_1p90m_2010",
    "infrastructure", "engineering_epc", "us",
    "OEG Inc. \u2014 San Salvador electrical / power systems engineering",
    "El Salvador",
    "23 Apr 2010: Department of State awards task order SAQMMA10F1452 to OEG Inc. for power systems engineering \u2014 San Salvador electrical work; obligated USD 1,899,862.90. CapEx face = award obligation.",
    "1899862.90", "2010-04-23", "2010", "13.693", "-89.219",
    "Electrical / power systems work, San Salvador, El Salvador (USASpending PoP El Salvador).",
    "usaspending_oeg_san_salvador_electrical_1p90m_2010",
    "POWER SYSTEMS ENGINEERING- SAN SALVADOR, EL SALVADOR ELECTRICAL WORK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F1452_1900_SALMEC05D0005_1900/",
    "Actor: OEG Inc. (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle engineering_epc; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle947",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F1452_1900_SALMEC05D0005_1900 (OEG San Salvador electrical). Signed 2010-04-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F1452_1900_SALMEC05D0005_1900/.",
    "USASpending: OEG San Salvador electrical USD 1.900m. Supports oeg_san_salvador_electrical_1p90m_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1899862.90; date_signed 2010-04-23.",
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
    print(f"cycles945-947 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
