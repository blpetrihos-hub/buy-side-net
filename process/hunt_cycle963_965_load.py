#!/usr/bin/env python3
"""Cycles 963–965: USASpending LatAm CapEx residual (police, schools, elevators, warehouses).

Seeds: 20261963–20261965. Thin top-up dry.
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


# === Cycle 963 ===
row_doc(
    "eterna_jardin_tama_police_1p55m_2019",
    "infrastructure", "building_materials", "other",
    "Eterna — Jardín de Tamana INL rural police station",
    "Colombia",
    "25 Jun 2019: U.S. Army Corps of Engineers awards task order W9127819F0253 to Eterna to construct rural INL police station in Jardín de Tamana; obligated USD 1,549,074.23. CapEx face = award obligation.",
    "1549074.23", "2019-06-25", "2019", "8.420", "-74.550",
    "INL rural police station, Jardín de Tamana, Colombia (USASpending PoP Colombia; Bolívar/Magdalena region pin).",
    "usaspending_eterna_jardin_tama_police_1p55m_2019",
    "THE PURPOSE OF THIS TASK ORDER IS TO CONSTRUCT A RURAL INL POLICE STATION IN JARDIN DE TAMANA, COLOMBIA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0253_9700_W9127817D0095_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle963",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0253_9700_W9127817D0095_9700 (Eterna Jardín de Tamana police). Signed 2019-06-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0253_9700_W9127817D0095_9700/.",
    "USASpending: Eterna Jardín de Tamana police USD 1.549m. Supports eterna_jardin_tama_police_1p55m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1549074.23; date_signed 2019-06-25.",
)

row_doc(
    "palgag_gonaives_hatte_school_1p55m_2011",
    "infrastructure", "building_materials", "allied",
    "Palgag Building Technologies — Gonaïves-Hatte school",
    "Haiti",
    "1 Feb 2011: Department of the Navy awards contract N6945011C0016 to Palgag for Gonaïves-Hatte school; obligated USD 1,547,297.72. CapEx face = award obligation.",
    "1547297.72", "2011-02-01", "2011", "19.450", "-72.690",
    "Gonaïves-Hatte school, Gonaïves, Haiti (USASpending PoP Haiti).",
    "usaspending_palgag_gonaives_hatte_school_1p55m_2011",
    "GONAIVES-HATTE SCHOOL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0016_9700_-NONE-_-NONE-/",
    "Actor: Palgag (Israel) — allied. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle963",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945011C0016_9700_-NONE-_-NONE- (Palgag Gonaïves-Hatte school). Signed 2011-02-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945011C0016_9700_-NONE-_-NONE-/.",
    "USASpending: Palgag Gonaïves-Hatte school USD 1.547m. Supports palgag_gonaives_hatte_school_1p55m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1547297.72; date_signed 2011-02-01.",
)

row_doc(
    "eei_ccopi_office_1p52m_2026",
    "infrastructure", "building_materials", "other",
    "EEI — CCOPI office construction",
    "Colombia",
    "31 Jul 2026: Department of State awards task order 19AQMM26F0993 to EEI for CCOPI office construction; obligated USD 1,516,335.85. CapEx face = award obligation.",
    "1516335.85", "2026-07-31", "2026", "4.624", "-74.065",
    "CCOPI office construction, Colombia (USASpending PoP Colombia; Bogotá pin).",
    "usaspending_eei_ccopi_office_1p52m_2026",
    "CCOPI OFFICE CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F0993_1900_19AQMM21D0037_1900/",
    "Actor: EEI (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle963",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM26F0993_1900_19AQMM21D0037_1900 (EEI CCOPI office). Signed 2026-07-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F0993_1900_19AQMM21D0037_1900/.",
    "USASpending: EEI CCOPI office USD 1.516m. Supports eei_ccopi_office_1p52m_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1516335.85; date_signed 2026-07-31.",
)

row_doc(
    "ect_chile_elevator_1p44m_2022",
    "infrastructure", "building_materials", "us",
    "East Coast Technologies — Chile elevator replacement",
    "Chile",
    "23 Sep 2022: Department of State awards contract 19GE5022C0043 to East Coast Technologies for elevator replacement project (PoP Chile); obligated USD 1,436,320.93. CapEx face = award obligation.",
    "1436320.93", "2022-09-23", "2022", "-33.449", "-70.669",
    "Elevator replacement, Chile (USASpending PoP Chile; Santiago pin for diplomatic post).",
    "usaspending_ect_chile_elevator_1p44m_2022",
    "ELEVATOR REPLACEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5022C0043_1900_-NONE-_-NONE-/",
    "Actor: East Coast Technologies (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle963",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5022C0043_1900_-NONE-_-NONE- (ECT Chile elevator). Signed 2022-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5022C0043_1900_-NONE-_-NONE-/.",
    "USASpending: ECT Chile elevator USD 1.436m. Supports ect_chile_elevator_1p44m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1436320.93; date_signed 2022-09-23.",
)

row_doc(
    "sea_pac_kingston_powell_elevator_1p39m_2024",
    "infrastructure", "building_materials", "us",
    "Sea Pac — Kingston Powell Plaza elevator replacement",
    "Jamaica",
    "16 Sep 2024: Department of State awards contract 19GE5024C0038 to Sea Pac for elevator replacement at Powell Plaza building, U.S. Embassy Kingston; obligated USD 1,390,653.19. CapEx face = award obligation.",
    "1390653.19", "2024-09-16", "2024", "18.017", "-76.810",
    "Elevator replacement, Powell Plaza, Kingston, Jamaica (USASpending PoP Jamaica).",
    "usaspending_sea_pac_kingston_powell_elevator_1p39m_2024",
    "U.S. EMBASSY KINGSTON, JAMAICA. ELEVATOR REPLACEMENT SERVICES AT THE POWELL PLAZA BUILDING.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024C0038_1900_-NONE-_-NONE-/",
    "Actor: Sea Pac Engineering (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle963",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5024C0038_1900_-NONE-_-NONE- (Sea Pac Kingston Powell elevator). Signed 2024-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024C0038_1900_-NONE-_-NONE-/.",
    "USASpending: Sea Pac Kingston Powell elevator USD 1.391m. Supports sea_pac_kingston_powell_elevator_1p39m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1390653.19; date_signed 2024-09-16.",
)

# === Cycle 964 ===
row_doc(
    "eterna_hap_warehouse_wells_1p39m_2021",
    "infrastructure", "building_materials", "other",
    "Eterna — HAP disaster relief warehouses and water wells",
    "Honduras",
    "6 Jul 2021: U.S. Army Corps of Engineers awards task order W9127821F0210 to Eterna for design/construction of HAP #39285/#39286 disaster relief warehouses and HAP #28375 water wells; obligated USD 1,391,882.24. CapEx face = award obligation.",
    "1391882.24", "2021-07-06", "2021", "14.072", "-87.192",
    "Disaster relief warehouses and water wells, Honduras (USASpending PoP Honduras; Tegucigalpa pin).",
    "usaspending_eterna_hap_warehouse_wells_1p39m_2021",
    "DESIGN AND CONSTRUCTION OF HAP #39285 DISASTER RELIEF WAREHOUSE HAP #39286 DISASTER RELIEF WAREHOUSE& HAP #28375 WATER WELLS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0210_9700_W9127816D0102_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle964",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127821F0210_9700_W9127816D0102_9700 (Eterna HAP warehouses/wells). Signed 2021-07-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0210_9700_W9127816D0102_9700/.",
    "USASpending: Eterna HAP warehouses/wells USD 1.392m. Supports eterna_hap_warehouse_wells_1p39m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1391882.24; date_signed 2021-07-06.",
)

row_doc(
    "marago_tumaco_utilities_1p38m_2021",
    "infrastructure", "building_materials", "other",
    "Constructora Marago — Tumaco CNP utilities upgrades",
    "Colombia",
    "9 Sep 2021: Department of State awards task order 19AQMM21F3269 to Constructora Marago for Tumaco CNP utilities upgrades construction; obligated USD 1,383,953.66. CapEx face = award obligation.",
    "1383953.66", "2021-09-09", "2021", "1.807", "-78.765",
    "CNP utilities upgrades, Tumaco, Nariño, Colombia (USASpending PoP Colombia).",
    "usaspending_marago_tumaco_utilities_1p38m_2021",
    "TUMACO CNP UTILITIES UPGRADES CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3269_1900_19AQMM21D0036_1900/",
    "Actor: Constructora Marago (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle964",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21F3269_1900_19AQMM21D0036_1900 (Marago Tumaco utilities). Signed 2021-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3269_1900_19AQMM21D0036_1900/.",
    "USASpending: Marago Tumaco utilities USD 1.384m. Supports marago_tumaco_utilities_1p38m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1383953.66; date_signed 2021-09-09.",
)

row_doc(
    "greenway_colombia_fire_alarm_1p37m_2017",
    "infrastructure", "building_materials", "us",
    "Greenway Enterprises — Colombia fire alarm upgrade",
    "Colombia",
    "27 Aug 2017: Department of State awards task order SAQMMA17F4122 to Greenway for fire alarm upgrade (PoP Colombia); obligated USD 1,370,388.87. CapEx face = award obligation.",
    "1370388.87", "2017-08-27", "2017", "4.624", "-74.065",
    "Fire alarm upgrade, Colombia (USASpending PoP Colombia; Bogotá pin).",
    "usaspending_greenway_colombia_fire_alarm_1p37m_2017",
    "FIRE ALARM UPGRADE  IGF::CT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F4122_1900_SAQMMA14D0050_1900/",
    "Actor: Greenway Enterprises (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle964",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17F4122_1900_SAQMMA14D0050_1900 (Greenway Colombia fire alarm). Signed 2017-08-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F4122_1900_SAQMMA14D0050_1900/.",
    "USASpending: Greenway Colombia fire alarm USD 1.370m. Supports greenway_colombia_fire_alarm_1p37m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1370388.87; date_signed 2017-08-27.",
)

row_doc(
    "eterna_soto_cano_arfor_hq_1p35m_2018",
    "infrastructure", "building_materials", "other",
    "Eterna — Soto Cano ARFOR HQ / LNO / CIF facility",
    "Honduras",
    "28 Sep 2018: U.S. Army Corps of Engineers awards task order W9127818F0739 to Eterna for construction of ARFOR HQ, LNO & CIF facility at Soto Cano; obligated USD 1,351,495.82. CapEx face = award obligation.",
    "1351495.82", "2018-09-28", "2018", "14.382", "-87.621",
    "ARFOR HQ/LNO/CIF facility, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_eterna_soto_cano_arfor_hq_1p35m_2018",
    "CONSTRUCTION OF ARFOR HQ, LNO,&CIF FACILITY, SOTO CANO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0739_9700_W9127816D0102_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle964",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127818F0739_9700_W9127816D0102_9700 (Eterna Soto Cano ARFOR HQ). Signed 2018-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0739_9700_W9127816D0102_9700/.",
    "USASpending: Eterna Soto Cano ARFOR HQ USD 1.351m. Supports eterna_soto_cano_arfor_hq_1p35m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1351495.82; date_signed 2018-09-28.",
)

row_doc(
    "bonatti_soto_cano_warehouse_atcals_1p35m_2020",
    "infrastructure", "building_materials", "other",
    "Bonatti — Soto Cano supply warehouse & consolidated ATCALS facility",
    "Honduras",
    "27 Sep 2020: U.S. Army Corps of Engineers awards task order W9127820F0489 to Bonatti for supply warehouse & consolidated ATCALS facility at Soto Cano; obligated USD 1,346,003.52. CapEx face = award obligation.",
    "1346003.52", "2020-09-27", "2020", "14.382", "-87.621",
    "Supply warehouse & ATCALS facility, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_bonatti_soto_cano_warehouse_atcals_1p35m_2020",
    "SUPPLY WAREHOUSE&CONSOLIDATED ATCALS FACILITY, SOTO CANO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0489_9700_W9127816D0099_9700/",
    "Actor: Bonatti (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle964",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127820F0489_9700_W9127816D0099_9700 (Bonatti Soto Cano warehouse/ATCALS). Signed 2020-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0489_9700_W9127816D0099_9700/.",
    "USASpending: Bonatti Soto Cano warehouse/ATCALS USD 1.346m. Supports bonatti_soto_cano_warehouse_atcals_1p35m_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1346003.52; date_signed 2020-09-27.",
)

# === Cycle 965 ===
row_doc(
    "global_vision_mexico_clinics_1p34m_2024",
    "infrastructure", "building_materials", "us",
    "Global Vision Enterprises — Mexico medical equipment supply and clinic refurbishment",
    "Mexico",
    "20 Mar 2024: Department of the Air Force awards contract FA251824P0002 to Global Vision for supply of medical equipment and refurbishment of clinics (PoP Mexico); obligated USD 1,342,728.78. CapEx face = award obligation.",
    "1342728.78", "2024-03-20", "2024", "", "",
    "Medical equipment supply and clinic refurbishment, Mexico (USASpending PoP Mexico; clinic sites not named — lat/lon blank).",
    "usaspending_global_vision_mexico_clinics_1p34m_2024",
    "SUPPLY OF MEDICAL EQUIPMENT AND REFURBISHMENT OF CLINICS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA251824P0002_9700_-NONE-_-NONE-/",
    "Actor: Global Vision Enterprises (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle965",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA251824P0002_9700_-NONE-_-NONE- (Global Vision Mexico clinics). Signed 2024-03-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA251824P0002_9700_-NONE-_-NONE-/.",
    "USASpending: Global Vision Mexico clinics USD 1.343m. Supports global_vision_mexico_clinics_1p34m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1342728.78; date_signed 2024-03-20.",
)

row_doc(
    "eei_sur_bolivar_health_1p33m_2024",
    "infrastructure", "building_materials", "other",
    "EEI — Sur de Bolívar health center HAP #70355",
    "Colombia",
    "29 Sep 2024: U.S. Army Corps of Engineers awards task order W9127824F0393 to EEI for design and construction of HAP #70355 health center in Sur de Bolívar; obligated USD 1,328,046.89. CapEx face = award obligation.",
    "1328046.89", "2024-09-29", "2024", "8.300", "-74.200",
    "Health center HAP #70355, Sur de Bolívar, Colombia (USASpending PoP Colombia).",
    "usaspending_eei_sur_bolivar_health_1p33m_2024",
    "DESIGN AND CONSTRUCTION OF HAP #70355 HEALTH CENTER IN SUR DE BOLIVAR, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0393_9700_W9127823D0058_9700/",
    "Actor: EEI (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle965",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0393_9700_W9127823D0058_9700 (EEI Sur de Bolívar health). Signed 2024-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0393_9700_W9127823D0058_9700/.",
    "USASpending: EEI Sur de Bolívar health USD 1.328m. Supports eei_sur_bolivar_health_1p33m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1328046.89; date_signed 2024-09-29.",
)

row_doc(
    "olgoonik_semar_materials_3p75m_2024",
    "infrastructure", "building_materials", "us",
    "Olgoonik Logistics — SEMAR construction materials",
    "Mexico",
    "8 Jul 2024: Department of State awards task order 19AQMR24F5009 to Olgoonik Logistics for construction materials for SEMAR (PoP Mexico); obligated USD 3,745,292.17. CapEx face = award obligation.",
    "3745292.17", "2024-07-08", "2024", "19.433", "-99.133",
    "Construction materials for SEMAR, Mexico (USASpending PoP Mexico; Mexico City pin).",
    "usaspending_olgoonik_semar_materials_3p75m_2024",
    "CONSTRUCTION MATERIALS FOR SEMAR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR24F5009_1900_19AQMM20D0098_1900/",
    "Actor: Olgoonik Logistics (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle965",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMR24F5009_1900_19AQMM20D0098_1900 (Olgoonik SEMAR materials). Signed 2024-07-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR24F5009_1900_19AQMM20D0098_1900/.",
    "USASpending: Olgoonik SEMAR materials USD 3.745m. Supports olgoonik_semar_materials_3p75m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3745292.17; date_signed 2024-07-08.",
)

row_doc(
    "bonatti_soto_cano_arms_room_1p28m_2024",
    "infrastructure", "building_materials", "other",
    "Bonatti — Soto Cano consolidated arms room facility",
    "Honduras",
    "30 Sep 2024: U.S. Army Corps of Engineers awards task order W9127824F0381 to Bonatti for design and construction of consolidated arms room facility at Soto Cano Air Base; obligated USD 1,276,359.04. CapEx face = award obligation.",
    "1276359.04", "2024-09-30", "2024", "14.382", "-87.621",
    "Consolidated arms room facility, Soto Cano Air Base, Comayagua, Honduras (USASpending PoP Honduras).",
    "usaspending_bonatti_soto_cano_arms_room_1p28m_2024",
    "DESIGN AND CONSTRUCTION OF CONSOLIDATED ARMS ROOM FACILITY IN SOTO CANO AIRBASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0381_9700_W9127823D0072_9700/",
    "Actor: Bonatti (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle965",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127824F0381_9700_W9127823D0072_9700 (Bonatti Soto Cano arms room). Signed 2024-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0381_9700_W9127823D0072_9700/.",
    "USASpending: Bonatti Soto Cano arms room USD 1.276m. Supports bonatti_soto_cano_arms_room_1p28m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1276359.04; date_signed 2024-09-30.",
)

row_doc(
    "bonatti_siquirres_warehouse_1p21m_2025",
    "infrastructure", "building_materials", "other",
    "Bonatti — Siquirres disaster response warehouse",
    "Costa Rica",
    "22 Sep 2025: U.S. Army Corps of Engineers awards task order W9127825FA173 to Bonatti for disaster response warehouse in Siquirres; obligated USD 1,214,345.79. CapEx face = award obligation.",
    "1214345.79", "2025-09-22", "2025", "10.098", "-83.507",
    "Disaster response warehouse, Siquirres, Costa Rica (USASpending PoP Costa Rica).",
    "usaspending_bonatti_siquirres_warehouse_1p21m_2025",
    "DISASTER RESPONSE WAREHOUSE IN SIQUIRRES, COSTA RICA. THE TASK WILL BE PERFORMED UNDER THE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA173_9700_W9127823D0072_9700/",
    "Actor: Bonatti (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle965",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA173_9700_W9127823D0072_9700 (Bonatti Siquirres warehouse). Signed 2025-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA173_9700_W9127823D0072_9700/.",
    "USASpending: Bonatti Siquirres warehouse USD 1.214m. Supports bonatti_siquirres_warehouse_1p21m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1214345.79; date_signed 2025-09-22.",
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
    print(f"cycles963-965 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
