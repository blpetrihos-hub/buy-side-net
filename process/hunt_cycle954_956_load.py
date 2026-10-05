#!/usr/bin/env python3
"""Cycles 954–956: USASpending LatAm CapEx residual (STRI, roofs, runway, clinics, solar).

Seeds: 20261954–20261956. Thin top-up dry.
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


# === Cycle 954 ===
row_doc(
    "diaz_guardia_tupper_roof_2p96m_2025",
    "infrastructure", "building_materials", "other",
    "Díaz y Guardia — Earl S. Tupper Center library roof/electromechanical",
    "Panama",
    "29 Apr 2025: Smithsonian awards task order 33330225FF0010200 to Díaz y Guardia to replace & reinforce roof for library at Earl S. Tupper Center and improve electromechanical systems; obligated USD 2,962,437.70. CapEx face = award obligation.",
    "2962437.70", "2025-04-29", "2025", "8.990", "-79.550",
    "Earl S. Tupper Center library roof, Panama City / STRI, Panama (USASpending PoP Panama; Tupper Center pin).",
    "usaspending_diaz_guardia_tupper_roof_2p96m_2025",
    "STRI - REPLACE & REINFORCE ROOF FOR LIBRARY AT EARL S.TUPPER CENTER AND IMPROVE ELECTROMECHANICAL SYSTEMS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330225FF0010200_3300_F15CC10150_3300/",
    "Actor: Díaz y Guardia (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle954",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330225FF0010200_3300_F15CC10150_3300 (Díaz y Guardia Tupper roof). Signed 2025-04-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330225FF0010200_3300_F15CC10150_3300/.",
    "USASpending: Díaz y Guardia Tupper roof USD 2.962m. Supports diaz_guardia_tupper_roof_2p96m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2962437.70; date_signed 2025-04-29.",
)

row_doc(
    "meltech_bogota_chancery_roof_2p94m_2016",
    "infrastructure", "building_materials", "us",
    "Meltech — Bogotá chancery compound roof replacement",
    "Colombia",
    "10 Aug 2016: Department of State awards task order SAQMMA16F3336 to Meltech for Bogotá chancery compound roof replacement; obligated USD 2,942,870.70. CapEx face = award obligation.",
    "2942870.70", "2016-08-10", "2016", "4.624", "-74.065",
    "Chancery compound roof replacement, Bogotá, Colombia (USASpending PoP Colombia).",
    "usaspending_meltech_bogota_chancery_roof_2p94m_2016",
    "IGF::OT::IGF BOGOTA, COLOMBIA CHANCERY COMPOUND ROOF REPLACEMENT PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F3336_1900_SAQMMA13D0128_1900/",
    "Actor: Meltech (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle954",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F3336_1900_SAQMMA13D0128_1900 (Meltech Bogotá roof). Signed 2016-08-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F3336_1900_SAQMMA13D0128_1900/.",
    "USASpending: Meltech Bogotá roof USD 2.943m. Supports meltech_bogota_chancery_roof_2p94m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2942870.70; date_signed 2016-08-10.",
)

row_doc(
    "insaat_sao_paulo_warehouse_roof_3p20m_2022",
    "infrastructure", "building_materials", "other",
    "740 Insaat — São Paulo consulate warehouse roof/walls renovation",
    "Brazil",
    "27 Jul 2022: Department of State awards contract 19GE5022C0016 to 740 Insaat for renovation of warehouse roof and walls, American Consulate General São Paulo; obligated USD 3,203,942.56. CapEx face = award obligation.",
    "3203942.56", "2022-07-27", "2022", "-23.551", "-46.633",
    "Warehouse roof/walls renovation, U.S. Consulate General São Paulo, Brazil (USASpending PoP Brazil).",
    "usaspending_insaat_sao_paulo_warehouse_roof_3p20m_2022",
    "CONSTRUCTION SERVICES FOR THE RENOVATION OF THE WAREHOUSE ROOF AND AND WALLS, AMERICAN CONSULATE GENERAL SAO PAOLO, BRAZIL.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5022C0016_1900_-NONE-_-NONE-/",
    "Actor: 740 Insaat (Turkey) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle954",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5022C0016_1900_-NONE-_-NONE- (740 Insaat São Paulo warehouse). Signed 2022-07-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5022C0016_1900_-NONE-_-NONE-/.",
    "USASpending: 740 Insaat São Paulo warehouse USD 3.204m. Supports insaat_sao_paulo_warehouse_roof_3p20m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3203942.56; date_signed 2022-07-27.",
)

row_doc(
    "psi_mexico_runway_2p78m_2018",
    "infrastructure", "bridges_roads", "us",
    "Project Services International — Mexico INL runway refurbishment",
    "Mexico",
    "27 Sep 2018: Department of State awards contract 19AQMM18C0204 to Project Services International for runway refurbishment (Mexico INL); obligated USD 2,782,677.31. CapEx face = award obligation.",
    "2782677.31", "2018-09-27", "2018", "", "",
    "Runway refurbishment, Mexico INL (USASpending PoP Mexico; site lat/lon left blank — runway not named).",
    "usaspending_psi_mexico_runway_2p78m_2018",
    "RUNWAY REFURBISHMENT - MEXICO INL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0204_1900_-NONE-_-NONE-/",
    "Actor: Project Services International (U.S.) under award agency — us. Official USASpending Award API. Shuffle bridges_roads/airside CapEx; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle954",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0204_1900_-NONE-_-NONE- (PSI Mexico runway). Signed 2018-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0204_1900_-NONE-_-NONE-/.",
    "USASpending: PSI Mexico runway USD 2.783m. Supports psi_mexico_runway_2p78m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2782677.31; date_signed 2018-09-27.",
)

row_doc(
    "serrano_namru6_generator_2p70m_2020",
    "infrastructure", "power_plants_grid", "other",
    "Serrano Proaño — NAMRU-6 generator replacement",
    "Peru",
    "27 Sep 2020: U.S. Army Corps of Engineers awards task order W9127820F0495 to Serrano Proaño for replace generator, NAMRU-6, Peru; obligated USD 2,698,684.18. CapEx face = award obligation. Distinct from serrano_namru6_admin.",
    "2698684.18", "2020-09-27", "2020", "-12.077", "-76.981",
    "Generator replacement, NAMRU-6, Lima area, Peru (USASpending PoP Peru; NAMRU-6 pin).",
    "usaspending_serrano_namru6_generator_2p70m_2020",
    "REPLACE GENERATOR, NAMRU-6, PERU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0495_9700_W9127818D0034_9700/",
    "Actor: Serrano Proaño (Ecuador) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle954",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127820F0495_9700_W9127818D0034_9700 (Serrano NAMRU-6 generator). Signed 2020-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127820F0495_9700_W9127818D0034_9700/.",
    "USASpending: Serrano NAMRU-6 generator USD 2.699m. Supports serrano_namru6_generator_2p70m_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2698684.18; date_signed 2020-09-27.",
)

# === Cycle 955 ===
row_doc(
    "futron_kingston_powell_fire_2p69m_2025",
    "infrastructure", "building_materials", "us",
    "Futron — Powell Plaza staff housing fire alarm upgrade",
    "Jamaica",
    "29 Sep 2025: Department of State awards task order 19AQMM25F1835 to Futron for fire alarm upgrade at Powell Plaza staff housing building in Kingston; obligated USD 2,688,581.40. CapEx face = award obligation. Distinct from futron_kingston_pv.",
    "2688581.40", "2025-09-29", "2025", "18.017", "-76.810",
    "Fire alarm upgrade, Powell Plaza staff housing, Kingston, Jamaica (USASpending PoP Jamaica).",
    "usaspending_futron_kingston_powell_fire_2p69m_2025",
    "FIRE ALARM UPGRADE AT THE POWELL PLAZA STAFF HOUSING BUILDING IN KINGSTON, JAMAICA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F1835_1900_19AQMM22D0075_1900/",
    "Actor: Futron (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle955",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25F1835_1900_19AQMM22D0075_1900 (Futron Kingston Powell fire). Signed 2025-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F1835_1900_19AQMM22D0075_1900/.",
    "USASpending: Futron Kingston Powell fire USD 2.689m. Supports futron_kingston_powell_fire_2p69m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2688581.40; date_signed 2025-09-29.",
)

row_doc(
    "hana_bridgetown_febr_2p55m_2023",
    "infrastructure", "building_materials", "us",
    "Hana Technologies — Bridgetown FE/BR doors/windows/anti-ram barriers",
    "Barbados",
    "10 Jul 2023: Department of State awards task order 19AQMM23F1749 to Hana Technologies for FE/BR II design-build installation of forced entry/ballistic resistant doors, windows and anti-ram barriers (PoP Barbados); obligated USD 2,551,619.92. CapEx face = award obligation.",
    "2551619.92", "2023-07-10", "2023", "13.097", "-59.615",
    "FE/BR doors/windows/anti-ram barriers, Bridgetown, Barbados (USASpending PoP Barbados).",
    "usaspending_hana_bridgetown_febr_2p55m_2023",
    "FE/BR II WORLDWIDE PROGRAM CONSISTING OF DESIGN-BUILD AND/OR CONSTRUCTION SERVICES FOR THE INSTALLATION, MAINTENANCE, AND REPAIR & REPLACEMENT (R&R) OF FORCED ENTRY/ BALLISTIC RESISTANT (FE/BR) DOORS, WINDOWS AND ANTI-RAM BARRIERS (ARB).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1749_1900_19AQMM21D0065_1900/",
    "Actor: Hana Technologies (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle955",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F1749_1900_19AQMM21D0065_1900 (Hana Bridgetown FE/BR). Signed 2023-07-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1749_1900_19AQMM21D0065_1900/.",
    "USASpending: Hana Bridgetown FE/BR USD 2.552m. Supports hana_bridgetown_febr_2p55m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2551619.92; date_signed 2023-07-10.",
)

row_doc(
    "relyant_ceopaz_el_salvador_2p49m_2022",
    "infrastructure", "building_materials", "us",
    "Relyant Global — CEOPAZ GPOI installation design/construction",
    "El Salvador",
    "27 Sep 2022: U.S. Army Corps of Engineers awards task order W9127822F0401 to Relyant for design & construction of GPOI projects — CEOPAZ installation, El Salvador; obligated USD 2,493,955.77. CapEx face = award obligation. Distinct from relyant_guatemala_ha.",
    "2493955.77", "2022-09-27", "2022", "13.692", "-89.218",
    "CEOPAZ GPOI installation, El Salvador (USASpending PoP El Salvador; San Salvador pin).",
    "usaspending_relyant_ceopaz_el_salvador_2p49m_2022",
    "DESIGN & CONSTRUCTION OF GPOI PROJECTS - CEOPAZ INSTALLATION, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0401_9700_W9127821D0080_9700/",
    "Actor: Relyant Global (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle955",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0401_9700_W9127821D0080_9700 (Relyant CEOPAZ). Signed 2022-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0401_9700_W9127821D0080_9700/.",
    "USASpending: Relyant CEOPAZ USD 2.494m. Supports relyant_ceopaz_el_salvador_2p49m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2493955.77; date_signed 2022-09-27.",
)

row_doc(
    "bonatti_copan_clinic_2p45m_2025",
    "infrastructure", "building_materials", "other",
    "Bonatti — Copán medical clinic",
    "Honduras",
    "22 Sep 2025: U.S. Army Corps of Engineers awards task order W9127825FA223 to Bonatti for medical clinic in Copán, Honduras (Central America MATOC); obligated USD 2,453,557.72. CapEx face = award obligation.",
    "2453557.72", "2025-09-22", "2025", "14.833", "-89.150",
    "Medical clinic, Copán, Honduras (USASpending PoP Honduras; Copán Ruinas area pin).",
    "usaspending_bonatti_copan_clinic_2p45m_2025",
    "MEDICAL CLINIC IN COPAN, HONDURAS. THE TASK WILL BE PERFORMED UNDER THE CENTRAL AMERICA MATOC IN ACCORDANCE WITH THE ATTACHED SPECIFICATIONS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA223_9700_W9127823D0072_9700/",
    "Actor: Bonatti (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle955",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA223_9700_W9127823D0072_9700 (Bonatti Copán clinic). Signed 2025-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA223_9700_W9127823D0072_9700/.",
    "USASpending: Bonatti Copán clinic USD 2.454m. Supports bonatti_copan_clinic_2p45m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2453557.72; date_signed 2025-09-22.",
)

row_doc(
    "guaymaral_airport_shops_2p40m_2014",
    "infrastructure", "building_materials", "other",
    "Foreign awardee — Guaymaral Airport new shops construction",
    "Colombia",
    "11 Feb 2014: Department of State awards contract SCO15014CN009 for construction of new shops at Guaymaral Airport; obligated USD 2,395,337.74. CapEx face = award obligation.",
    "2395337.74", "2014-02-11", "2014", "4.812", "-74.065",
    "New shops construction, Guaymaral Airport, Bogotá area, Colombia (USASpending PoP Colombia).",
    "usaspending_guaymaral_airport_shops_2p40m_2014",
    "CONSTRUCTION OF NEW SHOPS AT THE GUAYMARAL AIRPOR 3.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15014CN009_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardee — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle955",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15014CN009_1900_-NONE-_-NONE- (Guaymaral airport shops). Signed 2014-02-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15014CN009_1900_-NONE-_-NONE-/.",
    "USASpending: Guaymaral airport shops USD 2.395m. Supports guaymaral_airport_shops_2p40m_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2395337.74; date_signed 2014-02-11.",
)

# === Cycle 956 ===
row_doc(
    "montajes_savart_candelilla_pier_2p12m_2018",
    "infrastructure", "port_ownership", "other",
    "Montajes Savart — Candelilla pier",
    "Colombia",
    "8 Feb 2018: Department of State awards contract 19AQMM18C0058 to Montajes Savart for pier in Candelilla, Colombia; obligated USD 2,118,572. CapEx face = award obligation.",
    "2118572", "2018-02-08", "2018", "7.150", "-77.700",
    "Pier, Candelilla, Colombia (USASpending PoP Colombia; Chocó/Candelilla coastal pin).",
    "usaspending_montajes_savart_candelilla_pier_2p12m_2018",
    "PIER IN CANDELILLA, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0058_1900_-NONE-_-NONE-/",
    "Actor: Montajes Savart (Colombia) — other. Official USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle956",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0058_1900_-NONE-_-NONE- (Montajes Savart Candelilla pier). Signed 2018-02-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0058_1900_-NONE-_-NONE-/.",
    "USASpending: Montajes Savart Candelilla pier USD 2.119m. Supports montajes_savart_candelilla_pier_2p12m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2118572; date_signed 2018-02-08.",
)

row_doc(
    "eterna_tierradentro_police_2p10m_2023",
    "infrastructure", "building_materials", "other",
    "Eterna — Tierradentro INL rural police station",
    "Colombia",
    "22 Feb 2023: U.S. Army Corps of Engineers awards task order W9127823F0082 to Eterna for construction of INL rural police station (SEA22006) in Tierradentro; obligated USD 2,103,741.06. CapEx face = award obligation.",
    "2103741.06", "2023-02-22", "2023", "2.580", "-76.000",
    "INL rural police station, Tierradentro, Colombia (USASpending PoP Colombia; Tierradentro/Cauca pin).",
    "usaspending_eterna_tierradentro_police_2p10m_2023",
    "CONSTRUCTION OF INL RURAL POLICE STATION (SEA22006), LOCATED IN TIERRADENTRO, COLOMBIA,",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0082_9700_W9127817D0095_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle956",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127823F0082_9700_W9127817D0095_9700 (Eterna Tierradentro police). Signed 2023-02-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0082_9700_W9127817D0095_9700/.",
    "USASpending: Eterna Tierradentro police USD 2.104m. Supports eterna_tierradentro_police_2p10m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2103741.06; date_signed 2023-02-22.",
)

row_doc(
    "tb_plus_providencia_solar_2p16m_2023",
    "energy", "solar", "us",
    "TB Plus Energy — Providencia Island 2.5 MW solar + 2.5 MWh BESS",
    "Colombia",
    "4 Aug 2023: USAID awards contract 72051423C00003 to TB Plus Energy for Providencia Island solar power plant — 2.5 MW nominal with 2.5 MWh battery storage as primary energy source; obligated USD 2,157,956.17. CapEx face = award obligation.",
    "2157956.17", "2023-08-04", "2023", "13.350", "-81.370",
    "2.5 MW solar + 2.5 MWh BESS, Providencia Island, Colombia (USASpending PoP Colombia).",
    "usaspending_tb_plus_providencia_solar_2p16m_2023",
    "THE PROVIDENCIA ISLAND SOLAR POWER PLANT PROJECT WILL SERVE TO MANUFACTURE OR PROCURE THE 2.5 MW NOMINAL POWER WITH 2.5 MWH BATTERY-BASED ELECTRICAL ENERGY STORAGE SYSTEM THAT WILL PROVIDE THE PRIMARY SOURCE OF ENERGY FOR PROVIDENCIA ISLAND, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_72051423C00003_7200_-NONE-_-NONE-/",
    "Actor: TB Plus Energy (U.S.) under USAID — us. Official USASpending Award API. Shuffle solar; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle956",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_72051423C00003_7200_-NONE-_-NONE- (TB Plus Providencia solar). Signed 2023-08-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_72051423C00003_7200_-NONE-_-NONE-/.",
    "USASpending: TB Plus Providencia solar USD 2.158m. Supports tb_plus_providencia_solar_2p16m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2157956.17; date_signed 2023-08-04.",
)

row_doc(
    "ics_la_paz_chiller_2p15m_2013",
    "infrastructure", "building_materials", "us",
    "International Construction Services — La Paz chiller replacement",
    "Bolivia",
    "5 Feb 2013: Department of State awards task order SAQMMA13F0539 to ICS for La Paz chiller replacement project; obligated USD 2,151,382.28. CapEx face = award obligation.",
    "2151382.28", "2013-02-05", "2013", "-16.500", "-68.150",
    "Chiller replacement, La Paz, Bolivia (USASpending PoP Bolivia).",
    "usaspending_ics_la_paz_chiller_2p15m_2013",
    "LA PAZ CHILLER REPLACEMENT PROJECT.  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F0539_1900_SAQMMA08D0005_1900/",
    "Actor: ICS (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle956",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F0539_1900_SAQMMA08D0005_1900 (ICS La Paz chiller). Signed 2013-02-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F0539_1900_SAQMMA08D0005_1900/.",
    "USASpending: ICS La Paz chiller USD 2.151m. Supports ics_la_paz_chiller_2p15m_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2151382.28; date_signed 2013-02-05.",
)

row_doc(
    "eei_bahamas_rbpf_college_1p96m_2024",
    "infrastructure", "building_materials", "other",
    "EEI — RBPF Police Training College renovations",
    "Bahamas",
    "13 Dec 2024: Department of State awards contract 19AQMM25C0087 to Estudios Edificaciones e Interventorías (EEI) for RBPF Police Training College renovations; obligated USD 1,962,190.24. CapEx face = award obligation.",
    "1962190.24", "2024-12-13", "2024", "25.048", "-77.355",
    "RBPF Police Training College renovations, Bahamas (USASpending PoP Bahamas; Nassau pin).",
    "usaspending_eei_bahamas_rbpf_college_1p96m_2024",
    "RBPF POLICE TRAINING COLLEGE RENOVATIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25C0087_1900_-NONE-_-NONE-/",
    "Actor: EEI (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle956",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25C0087_1900_-NONE-_-NONE- (EEI Bahamas RBPF college). Signed 2024-12-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25C0087_1900_-NONE-_-NONE-/.",
    "USASpending: EEI Bahamas RBPF college USD 1.962m. Supports eei_bahamas_rbpf_college_1p96m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1962190.24; date_signed 2024-12-13.",
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
    print(f"cycles954-956 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
