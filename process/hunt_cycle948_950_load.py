#!/usr/bin/env python3
"""Cycles 948–950: USASpending page-4 LatAm CapEx residual.

Seeds: 20261948–20261950. Thin top-up dry.
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
    "hsu_sao_paulo_fire_alarm_642k_2018",
    "infrastructure", "building_materials", "us",
    "HSU Development, Inc. \u2014 S\u00e3o Paulo fire detection/alarm system replacement",
    "Brazil",
    "23 Apr 2018: Department of State awards task order 19AQMM18F1434 to HSU Development for S\u00e3o Paulo fire detection/alarm system replacement Phase I; obligated USD 641,835.76. CapEx face = award obligation.",
    "641835.76", "2018-04-23", "2018", "-23.551", "-46.633",
    "Fire detection/alarm replacement, S\u00e3o Paulo, Brazil (USASpending PoP Brazil).",
    "usaspending_hsu_sao_paulo_fire_alarm_642k_2018",
    "SAO PAULO FIRE DETECTION/ALARM SYSTEM REPLACEMENT PROJECT # XJ-0K-0004. THIS PR7263644 IS FOR PHASE I (SITE SU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1434_1900_SAQMMA14D0058_1900/",
    "Actor: HSU Development (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle948",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F1434_1900_SAQMMA14D0058_1900 (HSU S\u00e3o Paulo fire alarm). Signed 2018-04-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1434_1900_SAQMMA14D0058_1900/.",
    "USASpending: HSU S\u00e3o Paulo fire alarm USD 0.642m. Supports hsu_sao_paulo_fire_alarm_642k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 641835.76; date_signed 2018-04-23.",
)

row_doc(
    "pono_aina_haiti_chiller_3p94m_2020",
    "infrastructure", "building_materials", "us",
    "Pono Aina Management LLC \u2014 Haiti chiller design/construct/install",
    "Haiti",
    "30 Sep 2020: Department of State awards contract 19AQMM20C0234 to Pono Aina for design, construct and/or install chiller replacement (PoP Haiti); obligated USD 3,940,542.97. CapEx face = award obligation.",
    "3940542.97", "2020-09-30", "2020", "18.540", "-72.339",
    "Chiller replacement design/construct/install, Haiti (USASpending PoP Haiti).",
    "usaspending_pono_aina_haiti_chiller_3p94m_2020",
    "THE CONTRACTOR SHALL COMPLETE ALL SERVICES AND WORK REQUIRED TO DESIGN, CONSTRUCT AND/OR INSTALL CHILLER REPLA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0234_1900_-NONE-_-NONE-/",
    "Actor: Pono Aina (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle948",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20C0234_1900_-NONE-_-NONE- (Pono Aina Haiti chiller). Signed 2020-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0234_1900_-NONE-_-NONE-/.",
    "USASpending: Pono Aina Haiti chiller USD 3.941m. Supports pono_aina_haiti_chiller_3p94m_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3940542.97; date_signed 2020-09-30.",
)

row_doc(
    "solustart_haiti_clinics_3p22m_2016",
    "infrastructure", "building_materials", "other",
    "Solustart SRL \u2014 Haiti health clinic renovation upgrades",
    "Haiti",
    "24 May 2016: USAID awards task order AID521TO1600003 to Solustart SRL for renovation work health clinic upgrades; obligated USD 3,218,571.68. CapEx face = award obligation. Distinct from tseng_haiti_clinics.",
    "3218571.68", "2016-05-24", "2016", "18.540", "-72.339",
    "Health clinic renovation upgrades, Haiti (USASpending PoP Haiti).",
    "usaspending_solustart_haiti_clinics_3p22m_2016",
    "IGF::OT::IGF RENOVATION WORK HEALTH CLINIC UPGRADES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521TO1600003_7200_AID521I1500002_7200/",
    "Actor: Solustart SRL (Dominican Republic) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle948",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521TO1600003_7200_AID521I1500002_7200 (Solustart Haiti clinics). Signed 2016-05-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521TO1600003_7200_AID521I1500002_7200/.",
    "USASpending: Solustart Haiti clinics USD 3.219m. Supports solustart_haiti_clinics_3p22m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3218571.68; date_signed 2016-05-24.",
)

row_doc(
    "taft_gamboa_fire_983k_2026",
    "infrastructure", "building_materials", "other",
    "Grupo Taft S.A. \u2014 STRI Gamboa campus fire protection system construction",
    "Panama",
    "28 Aug 2026: Smithsonian awards task order 33330226FF0010391 to Grupo Taft for construction services at Gamboa campus fire protection system project; obligated USD 982,760.97. CapEx face = award obligation. Distinct from kunkel_culebra_fire.",
    "982760.97", "2026-08-28", "2026", "9.117", "-79.700",
    "Fire protection system construction, Gamboa campus, Panama (USASpending PoP Panama).",
    "usaspending_taft_gamboa_fire_983k_2026",
    "STRI - CONSTRUCTION SERVICES AT THE GAMBOA CAMPUS FIRE PROTECTION SYSTEM PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330226FF0010391_3300_33330226DF0010119_3300/",
    "Actor: Grupo Taft S.A. (Panama) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle948",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330226FF0010391_3300_33330226DF0010119_3300 (Taft Gamboa fire). Signed 2026-08-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330226FF0010391_3300_33330226DF0010119_3300/.",
    "USASpending: Taft Gamboa fire USD 0.983m. Supports taft_gamboa_fire_983k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 982760.97; date_signed 2026-08-28.",
)

row_doc(
    "bonatti_puerto_barrios_clinic_780k_2025",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 Puerto Barrios medical clinic/hospital",
    "Guatemala",
    "18 Sep 2025: USACE awards task order W9127825FA203 to Bonatti for medical clinic/hospital in Puerto Barrios, Guatemala; obligated USD 780,422.05. CapEx face = award obligation.",
    "780422.05", "2025-09-18", "2025", "15.728", "-88.594",
    "Medical clinic/hospital, Puerto Barrios, Guatemala (USASpending PoP Guatemala).",
    "usaspending_bonatti_puerto_barrios_clinic_780k_2025",
    "MEDICAL CLINIC/HOSPITAL IN PUERTO BARRIOS, GUATEMALA. THE TASK WILL BE PERFORMED UNDER THE CENTRAL AMERICA MAT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA203_9700_W9127823D0072_9700/",
    "Actor: Bonatti (Guatemala) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle948",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA203_9700_W9127823D0072_9700 (Bonatti Puerto Barrios clinic). Signed 2025-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA203_9700_W9127823D0072_9700/.",
    "USASpending: Bonatti Puerto Barrios clinic USD 0.780m. Supports bonatti_puerto_barrios_clinic_780k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 780422.05; date_signed 2025-09-18.",
)

row_doc(
    "tecpro_guatemala_school_824k_2017",
    "infrastructure", "building_materials", "other",
    "Tecnolog\u00eda de Proyectos \u2014 Guatemala elementary school",
    "Guatemala",
    "30 Sep 2017: USACE awards task order W9127817F0516 to Tecnolog\u00eda de Proyectos for elementary school; obligated USD 824,425.55. CapEx face = award obligation.",
    "824425.55", "2017-09-30", "2017", "14.635", "-90.507",
    "Elementary school, Guatemala (USASpending PoP Guatemala; national pin).",
    "usaspending_tecpro_guatemala_school_824k_2017",
    "IGF::OT::IGF ELEMENTARY SCHOOL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0516_9700_W9127816D0103_9700/",
    "Actor: Tecnolog\u00eda de Proyectos (Honduras) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle949",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0516_9700_W9127816D0103_9700 (TecPro Guatemala school). Signed 2017-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0516_9700_W9127816D0103_9700/.",
    "USASpending: TecPro Guatemala school USD 0.824m. Supports tecpro_guatemala_school_824k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 824425.55; date_signed 2017-09-30.",
)

row_doc(
    "iap_soto_cano_power_1p92m_2019",
    "energy", "power_plants_grid", "us",
    "IAP Worldwide Services, Inc. \u2014 Soto Cano prime/standby power",
    "Honduras",
    "3 May 2019: DoD awards contract W9127819C0015 to IAP Worldwide Services for prime/standby power, Soto Cano AB, Honduras; obligated USD 1,915,872.89. CapEx face = award obligation. Distinct from eterna_scab_grid / eterna_soto_cano_pv.",
    "1915872.89", "2019-05-03", "2019", "14.382", "-87.621",
    "Prime/standby power, Soto Cano Air Base, Honduras (USASpending PoP Honduras).",
    "usaspending_iap_soto_cano_power_1p92m_2019",
    "PROVIDE PRIME/STANDBY POWER, SOTO CANO AB,HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819C0015_9700_-NONE-_-NONE-/",
    "Actor: IAP Worldwide Services (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle power_plants_grid; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle949",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819C0015_9700_-NONE-_-NONE- (IAP Soto Cano power). Signed 2019-05-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819C0015_9700_-NONE-_-NONE-/.",
    "USASpending: IAP Soto Cano power USD 1.916m. Supports iap_soto_cano_power_1p92m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1915872.89; date_signed 2019-05-03.",
)

row_doc(
    "bonatti_la_paz_hn_clinic_1p48m_2022",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 La Paz, Honduras clinic renovation design/build",
    "Honduras",
    "21 Jun 2022: USACE awards task order W9127822F0157 to Bonatti for D/B HAP 42241 clinic renovation, La Paz, Honduras; obligated USD 1,484,580. CapEx face = award obligation.",
    "1484580", "2022-06-21", "2022", "14.320", "-87.680",
    "Clinic renovation, La Paz, Honduras (USASpending PoP Honduras).",
    "usaspending_bonatti_la_paz_hn_clinic_1p48m_2022",
    "D/B HAP 42241 CLINIC RENOVATION, LA PAZ, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0157_9700_W9127821D0076_9700/",
    "Actor: Bonatti (Guatemala) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle949",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0157_9700_W9127821D0076_9700 (Bonatti La Paz HN clinic). Signed 2022-06-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0157_9700_W9127821D0076_9700/.",
    "USASpending: Bonatti La Paz HN clinic USD 1.485m. Supports bonatti_la_paz_hn_clinic_1p48m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1484580; date_signed 2022-06-21.",
)

row_doc(
    "bonatti_es_firefighter_house_1p72m_2019",
    "infrastructure", "building_materials", "other",
    "Bonatti Ingenieros \u2014 El Salvador firefighter training house",
    "El Salvador",
    "26 Sep 2019: USACE awards task order W9127819F0519 to Bonatti for HAP fire fighter training house; obligated USD 1,717,993.56. CapEx face = award obligation.",
    "1717993.56", "2019-09-26", "2019", "13.693", "-89.219",
    "Firefighter training house, El Salvador (USASpending PoP El Salvador; San Salvador pin).",
    "usaspending_bonatti_es_firefighter_house_1p72m_2019",
    "HAP FIRE FIGHTER TRAINING HOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0519_9700_W9127816D0099_9700/",
    "Actor: Bonatti (Guatemala) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle949",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0519_9700_W9127816D0099_9700 (Bonatti ES firefighter house). Signed 2019-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0519_9700_W9127816D0099_9700/.",
    "USASpending: Bonatti ES firefighter house USD 1.718m. Supports bonatti_es_firefighter_house_1p72m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1717993.56; date_signed 2019-09-26.",
)

row_doc(
    "arco_san_ildefonso_clinic_1p13m_2014",
    "infrastructure", "building_materials", "other",
    "Arco Ingenieros \u2014 San Ildefonso clinic reconstruction",
    "El Salvador",
    "18 Dec 2014: USAID awards contract AID519C1500001 to Arco Ingenieros for final design and reconstruction of San Ildefonso clinic; obligated USD 1,134,401.20. CapEx face = award obligation.",
    "1134401.20", "2014-12-18", "2014", "13.700", "-89.200",
    "San Ildefonso clinic reconstruction, El Salvador (USASpending PoP El Salvador; approximate pin).",
    "usaspending_arco_san_ildefonso_clinic_1p13m_2014",
    "IGF::CL::IGF TO PROVIDE PROFESSIONAL FINAL DESIGN SERVICES AND RECONSTRUCTION OF THE SAN ILDEFONSO CLINIC, WHI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID519C1500001_7200_-NONE-_-NONE-/",
    "Actor: Arco Ingenieros (El Salvador) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle949",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID519C1500001_7200_-NONE-_-NONE- (Arco San Ildefonso clinic). Signed 2014-12-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID519C1500001_7200_-NONE-_-NONE-/.",
    "USASpending: Arco San Ildefonso clinic USD 1.134m. Supports arco_san_ildefonso_clinic_1p13m_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1134401.20; date_signed 2014-12-18.",
)

row_doc(
    "rio_blanco_cr_school_524k_2010",
    "infrastructure", "building_materials", "other",
    "Constructora R\u00edo Blanco S.A. \u2014 Costa Rica school renovation",
    "Costa Rica",
    "26 Sep 2010: DoD awards contract W912CL10C0031 to Constructora R\u00edo Blanco for school renovation; obligated USD 523,941.92. CapEx face = award obligation.",
    "523941.92", "2010-09-26", "2010", "9.928", "-84.091",
    "School renovation, Costa Rica (USASpending PoP Costa Rica; national pin).",
    "usaspending_rio_blanco_cr_school_524k_2010",
    "SCHOOL RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0031_9700_-NONE-_-NONE-/",
    "Actor: Constructora R\u00edo Blanco (Costa Rica) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle950",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0031_9700_-NONE-_-NONE- (R\u00edo Blanco CR school). Signed 2010-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0031_9700_-NONE-_-NONE-/.",
    "USASpending: R\u00edo Blanco CR school USD 0.524m. Supports rio_blanco_cr_school_524k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 523941.92; date_signed 2010-09-26.",
)

row_doc(
    "misc_cr_clinic_531k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardee \u2014 Costa Rica clinic construction",
    "Costa Rica",
    "5 Aug 2010: DoD awards contract W912CL10C0021 for clinic construction (PoP Costa Rica); obligated USD 530,870. CapEx face = award obligation.",
    "530870", "2010-08-05", "2010", "9.928", "-84.091",
    "Clinic construction, Costa Rica (USASpending PoP Costa Rica; national pin).",
    "usaspending_misc_cr_clinic_531k_2010",
    "CLINIC CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0021_9700_-NONE-_-NONE-/",
    "Actor: Miscellaneous foreign awardee \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle950",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0021_9700_-NONE-_-NONE- (CR clinic construction). Signed 2010-08-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0021_9700_-NONE-_-NONE-/.",
    "USASpending: CR clinic construction USD 0.531m. Supports misc_cr_clinic_531k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 530870; date_signed 2010-08-05.",
)

row_doc(
    "misc_guayaquil_canine_523k_2007",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardee \u2014 Guayaquil police canine unit construction/remodel",
    "Ecuador",
    "27 Jun 2007: Department of State awards contract SWHARC07C0007 for construction and remodeling at the police canine unit in Guayaquil; obligated USD 522,892.50. CapEx face = award obligation.",
    "522892.50", "2007-06-27", "2007", "-2.171", "-79.922",
    "Police canine unit construction/remodel, Guayaquil, Ecuador (USASpending PoP Ecuador).",
    "usaspending_misc_guayaquil_canine_523k_2007",
    "CONSTRUCTION AND REMODELING AT THE POLICE CANINE UNIT IN GUAYAQUIL, ECUADOR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC07C0007_1900_-NONE-_-NONE-/",
    "Actor: Miscellaneous foreign awardee \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle950",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC07C0007_1900_-NONE-_-NONE- (Guayaquil canine unit). Signed 2007-06-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC07C0007_1900_-NONE-_-NONE-/.",
    "USASpending: Guayaquil canine unit USD 0.523m. Supports misc_guayaquil_canine_523k_2007.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 522892.50; date_signed 2007-06-27.",
)

row_doc(
    "ics_brazil_construction_932k_2023",
    "infrastructure", "building_materials", "us",
    "International Construction Services \u2014 Brazil construction task order",
    "Brazil",
    "27 Sep 2023: Department of State awards task order 19AQMM23F3206 to International Construction Services for construction (PoP Brazil); obligated USD 931,702.50. CapEx face = award obligation. Distinct from ics_lima_msgr_reno.",
    "931702.50", "2023-09-27", "2023", "-15.797", "-47.892",
    "Construction task order, Brazil (USASpending PoP Brazil; Bras\u00edlia pin for diplomatic facilities).",
    "usaspending_ics_brazil_construction_932k_2023",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F3206_1900_19AQMM22D0053_1900/",
    "Actor: ICS (U.S.) under award agency \u2014 us. Official USASpending Award API. Shuffle building_materials; \u22651/3 U.S. hunt CapEx.",
    "hunt_cycle950",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F3206_1900_19AQMM22D0053_1900 (ICS Brazil construction). Signed 2023-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F3206_1900_19AQMM22D0053_1900/.",
    "USASpending: ICS Brazil construction USD 0.932m. Supports ics_brazil_construction_932k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 931702.50; date_signed 2023-09-27.",
)

row_doc(
    "cobos_ecuador_construction_546k_2023",
    "infrastructure", "building_materials", "other",
    "Mar\u00eda Graciela Cobos Carri\u00f3n \u2014 Ecuador construction services",
    "Ecuador",
    "28 Jun 2023: Department of State awards contract 19GE5023C0016 to Mar\u00eda Graciela Cobos Carri\u00f3n for construction services (PoP Ecuador); obligated USD 546,425.13. CapEx face = award obligation.",
    "546425.13", "2023-06-28", "2023", "-0.180", "-78.468",
    "Construction services, Ecuador (USASpending PoP Ecuador; Quito pin).",
    "usaspending_cobos_ecuador_construction_546k_2023",
    "CONSTRUCTION SERVICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0016_1900_-NONE-_-NONE-/",
    "Actor: Mar\u00eda Graciela Cobos Carri\u00f3n (Ecuador) \u2014 other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle950",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5023C0016_1900_-NONE-_-NONE- (Cobos Ecuador construction). Signed 2023-06-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0016_1900_-NONE-_-NONE-/.",
    "USASpending: Cobos Ecuador construction USD 0.546m. Supports cobos_ecuador_construction_546k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 546425.13; date_signed 2023-06-28.",
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
    print(f"cycles948-950 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
