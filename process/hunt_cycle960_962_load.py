#!/usr/bin/env python3
"""Cycles 960–962: USASpending CapEx residual + Peru balsa SERFOR presence (thin).

Seeds: 20261960–20261962. Thin top-up: Peru balsa SERFOR chain presence.
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
    investment_type="epc", currency="USD", value_usd=None, fx_usd="1",
):
    if value_usd is None:
        value_usd = value
    A(
        {
            "id": rid, "layer": layer, "subcategory": sub, "side": side,
            "counterpart": counterpart, "country": country, "asset": asset,
            "investment_type": investment_type, "value": value, "currency": currency,
            "value_usd": value_usd, "fx_usd": fx_usd, "fx_date": fx_date, "year": year,
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


# === Cycle 960 ===
row_doc(
    "mexico_nec_perimeter_fence_basin_2p28m_2017",
    "infrastructure", "building_materials", "other",
    "Foreign awardee — Mexico NEC perimeter fence / retention basin preliminary works",
    "Mexico",
    "12 Jan 2017: Department of State awards contract SAQMMA17M0107 for preliminary works of perimeter fence, retention basin construction, subsequent site maintenance (PoP Mexico); obligated USD 2,282,082.73. CapEx face = award obligation.",
    "2282082.73", "2017-01-12", "2017", "19.433", "-99.133",
    "Perimeter fence / retention basin preliminary works, Mexico NEC (USASpending PoP Mexico; Mexico City pin).",
    "usaspending_mexico_nec_perimeter_fence_basin_2p28m_2017",
    "PRELIMINARY WORKS OF PERIMETER FENCE, RETENTION BASIN CONSTRUCTION, SUBSEQUENT SITE MAINTE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0107_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardee — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle960",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17M0107_1900_-NONE-_-NONE- (Mexico NEC perimeter fence/basin). Signed 2017-01-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0107_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico NEC perimeter fence/basin USD 2.282m. Supports mexico_nec_perimeter_fence_basin_2p28m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2282082.73; date_signed 2017-01-12.",
)

row_doc(
    "olgoonik_nassau_febr_2p27m_2013",
    "infrastructure", "building_materials", "us",
    "Olgoonik Specialty Contractors — Nassau FE/BR doors/windows replacement",
    "Bahamas",
    "28 Sep 2013: Department of State awards task order SAQMMA13F3944 to Olgoonik Specialty Contractors to replace 13 FE/BR doors, multi-unit door/window elevations, vault door, fixed windows, teller window, and glazing panels in Nassau; obligated USD 2,270,564. CapEx face = award obligation.",
    "2270564", "2013-09-28", "2013", "25.048", "-77.355",
    "FE/BR doors/windows replacement, Nassau, Bahamas (USASpending PoP Bahamas).",
    "usaspending_olgoonik_nassau_febr_2p27m_2013",
    "CONSTRUCTION: TO REPLACE (13) FE/BR DOORS, SIX MULTI-UNIT DOOR AND WINDOW ELEVATIONS, ONE VAULT DOOR, AND 12 FIXED WINDOWS, ONE TELLER WINDOW, AND EIGHT GLAZING PANELS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F3944_1900_SAQMMA13D0124_1900/",
    "Actor: Olgoonik Specialty Contractors (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle960",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F3944_1900_SAQMMA13D0124_1900 (Olgoonik Nassau FE/BR). Signed 2013-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F3944_1900_SAQMMA13D0124_1900/.",
    "USASpending: Olgoonik Nassau FE/BR USD 2.271m. Supports olgoonik_nassau_febr_2p27m_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2270564; date_signed 2013-09-28.",
)

row_doc(
    "meptek_mexico_hvac_1p86m_2024",
    "infrastructure", "building_materials", "other",
    "Meptek — Mexico engineer/build HVAC systems replacement",
    "Mexico",
    "30 Sep 2024: Department of State awards task order 19GE5024F0707 to Meptek for engineer/build HVAC systems replacement (PoP Mexico); obligated USD 1,860,794.95. CapEx face = award obligation.",
    "1860794.95", "2024-09-30", "2024", "", "",
    "HVAC systems replacement, Mexico (USASpending PoP Mexico; post not named — lat/lon blank).",
    "usaspending_meptek_mexico_hvac_1p86m_2024",
    "ENGINEER/BUILD HVAC SYSTEMS REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024F0707_1900_19GE5024D0049_1900/",
    "Actor: Meptek (Turkey) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle960",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5024F0707_1900_19GE5024D0049_1900 (Meptek Mexico HVAC). Signed 2024-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024F0707_1900_19GE5024D0049_1900/.",
    "USASpending: Meptek Mexico HVAC USD 1.861m. Supports meptek_mexico_hvac_1p86m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1860794.95; date_signed 2024-09-30.",
)

row_doc(
    "proyectos_civiles_mansilla_kennels_1p76m_2023",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles — Mansilla kennels construction",
    "Colombia",
    "18 Aug 2023: Department of State awards task order 19AQMM23F1720 to Proyectos Civiles for Mansilla kennels construction; obligated USD 1,758,421.54. CapEx face = award obligation.",
    "1758421.54", "2023-08-18", "2023", "4.624", "-74.065",
    "Mansilla kennels construction, Colombia (USASpending PoP Colombia; Bogotá-area pin).",
    "usaspending_proyectos_civiles_mansilla_kennels_1p76m_2023",
    "MANSILLA KENNELS CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1720_1900_19AQMM21D0039_1900/",
    "Actor: Proyectos Civiles (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle960",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F1720_1900_19AQMM21D0039_1900 (Proyectos Civiles Mansilla kennels). Signed 2023-08-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F1720_1900_19AQMM21D0039_1900/.",
    "USASpending: Proyectos Civiles Mansilla kennels USD 1.758m. Supports proyectos_civiles_mansilla_kennels_1p76m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1758421.54; date_signed 2023-08-18.",
)

row_doc(
    "serrano_galapagos_indigenous_school_1p75m_2025",
    "infrastructure", "building_materials", "other",
    "Serrano Proaño — Galápagos indigenous school",
    "Ecuador",
    "26 Sep 2025: U.S. Army Corps of Engineers awards task order W9127825FA273 to Serrano Proaño for indigenous school in Galápagos (South America MATOC); obligated USD 1,747,605.62. CapEx face = award obligation. Distinct from serrano_galapagos_eoc.",
    "1747605.62", "2025-09-26", "2025", "-0.740", "-90.315",
    "Indigenous school, Galápagos, Ecuador (USASpending PoP Ecuador; Santa Cruz/Puerto Ayora area pin).",
    "usaspending_serrano_galapagos_indigenous_school_1p75m_2025",
    "INDIGENOUS SCHOOL IN GALAPAGOS, ECUADOR. THE TASK WILL BE PERFORMED UNDER THE SOUTH AMERIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA273_9700_W9127823D0060_9700/",
    "Actor: Serrano Proaño (Ecuador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle960",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825FA273_9700_W9127823D0060_9700 (Serrano Galápagos indigenous school). Signed 2025-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825FA273_9700_W9127823D0060_9700/.",
    "USASpending: Serrano Galápagos indigenous school USD 1.748m. Supports serrano_galapagos_indigenous_school_1p75m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1747605.62; date_signed 2025-09-26.",
)

# === Cycle 961 ===
row_doc(
    "falcon_spectrum_brazil_fire_alarm_1p73m_2012",
    "infrastructure", "building_materials", "us",
    "Falcon Spectrum JV — Brazil fire alarm upgrade",
    "Brazil",
    "17 Jul 2012: Department of State awards task order SAQMMA12F2435 to Falcon Spectrum JV for fire alarm upgrade (PoP Brazil); obligated USD 1,728,547.86. CapEx face = award obligation. Distinct from falcon_spectrum_rio_elevators.",
    "1728547.86", "2012-07-17", "2012", "", "",
    "Fire alarm upgrade, Brazil (USASpending PoP Brazil; post not named — lat/lon blank).",
    "usaspending_falcon_spectrum_brazil_fire_alarm_1p73m_2012",
    "FIRE ALARM UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2435_1900_SAQMMA08D0016_1900/",
    "Actor: Falcon Spectrum JV (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle961",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F2435_1900_SAQMMA08D0016_1900 (Falcon Spectrum Brazil fire alarm). Signed 2012-07-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2435_1900_SAQMMA08D0016_1900/.",
    "USASpending: Falcon Spectrum Brazil fire alarm USD 1.729m. Supports falcon_spectrum_brazil_fire_alarm_1p73m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1728547.86; date_signed 2012-07-17.",
)

row_doc(
    "ecuainger_catamayo_police_1p70m_2010",
    "infrastructure", "building_materials", "other",
    "Ecuaingerconstructec — Catamayo police station",
    "Ecuador",
    "3 Feb 2010: Department of State awards contract SWHARC10C0003 to Ecuaingerconstructec for construction of police station at Catamayo; obligated USD 1,704,330.92. CapEx face = award obligation.",
    "1704330.92", "2010-02-03", "2010", "-3.983", "-79.350",
    "Police station, Catamayo, Loja, Ecuador (USASpending PoP Ecuador).",
    "usaspending_ecuainger_catamayo_police_1p70m_2010",
    "CONSTRUCTION OF POLICE STATION AT CATAMAYO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC10C0003_1900_-NONE-_-NONE-/",
    "Actor: Ecuaingerconstructec (Ecuador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle961",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC10C0003_1900_-NONE-_-NONE- (Ecuainger Catamayo police). Signed 2010-02-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC10C0003_1900_-NONE-_-NONE-/.",
    "USASpending: Ecuainger Catamayo police USD 1.704m. Supports ecuainger_catamayo_police_1p70m_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1704330.92; date_signed 2010-02-03.",
)

row_doc(
    "mfg_muzu_lodging_1p70m_2020",
    "infrastructure", "building_materials", "other",
    "MFG Ingeniería — Muzu anti-drug school lodging building",
    "Colombia",
    "24 Aug 2020: Department of State awards contract 19AQMM20C0169 to MFG Ingeniería for construction of lodging building at anti-drug school in Muzu; obligated USD 1,695,701.43. CapEx face = award obligation.",
    "1695701.43", "2020-08-24", "2020", "5.530", "-74.290",
    "Lodging building, anti-drug school, Muzu, Colombia (USASpending PoP Colombia; Muzo/Muzu Boyacá pin).",
    "usaspending_mfg_muzu_lodging_1p70m_2020",
    "CONSTRUCTION OF LODGING BUILDING AT ANT-DRUG SCHOOL IN MUZU, COLOMBIA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0169_1900_-NONE-_-NONE-/",
    "Actor: MFG Ingeniería (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle961",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20C0169_1900_-NONE-_-NONE- (MFG Muzu lodging). Signed 2020-08-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0169_1900_-NONE-_-NONE-/.",
    "USASpending: MFG Muzu lodging USD 1.696m. Supports mfg_muzu_lodging_1p70m_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1695701.43; date_signed 2020-08-24.",
)

row_doc(
    "colibri_chapicuy_clinic_1p68m_2016",
    "infrastructure", "building_materials", "other",
    "Colibrí Proyectos — Chapicuy clinic construction",
    "Uruguay",
    "29 Sep 2016: U.S. Army Corps of Engineers awards contract W912CL16C0001 to Colibrí for Chapicuy clinic construction; obligated USD 1,682,092.84. CapEx face = award obligation. Distinct from colibri_peru_school.",
    "1682092.84", "2016-09-29", "2016", "-31.650", "-56.850",
    "Clinic construction, Chapicuy, Uruguay (USASpending PoP Uruguay).",
    "usaspending_colibri_chapicuy_clinic_1p68m_2016",
    "IGF::OT::IGF CHAPICUY CLINIC CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL16C0001_9700_-NONE-_-NONE-/",
    "Actor: Colibrí Proyectos (Peru-registered) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle961",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL16C0001_9700_-NONE-_-NONE- (Colibrí Chapicuy clinic). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL16C0001_9700_-NONE-_-NONE-/.",
    "USASpending: Colibrí Chapicuy clinic USD 1.682m. Supports colibri_chapicuy_clinic_1p68m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1682092.84; date_signed 2016-09-29.",
)

row_doc(
    "marago_diran_dicar_base_1p64m_2018",
    "infrastructure", "building_materials", "other",
    "Constructora Marago — DIRAN & DICAR base construction",
    "Colombia",
    "24 Sep 2018: Department of State awards contract 19AQMM18C0121 to Constructora Marago for DIRAN & DICAR base construction; obligated USD 1,640,351.47. CapEx face = award obligation.",
    "1640351.47", "2018-09-24", "2018", "4.624", "-74.065",
    "DIRAN & DICAR base construction, Colombia (USASpending PoP Colombia; Bogotá pin).",
    "usaspending_marago_diran_dicar_base_1p64m_2018",
    "19AQMM18C0121 DIRAN&DICAR BASE CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0121_1900_-NONE-_-NONE-/",
    "Actor: Constructora Marago (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle961",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0121_1900_-NONE-_-NONE- (Marago DIRAN/DICAR base). Signed 2018-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0121_1900_-NONE-_-NONE-/.",
    "USASpending: Marago DIRAN/DICAR base USD 1.640m. Supports marago_diran_dicar_base_1p64m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1640351.47; date_signed 2018-09-24.",
)

# === Cycle 962 ===
row_doc(
    "eterna_florencia_police_1p63m_2019",
    "infrastructure", "building_materials", "other",
    "Eterna — Florencia INL rural police station",
    "Colombia",
    "24 Sep 2019: U.S. Army Corps of Engineers awards task order W9127819F0489 to Eterna to construct rural INL police station in Florencia; obligated USD 1,628,986.24. CapEx face = award obligation.",
    "1628986.24", "2019-09-24", "2019", "1.614", "-75.606",
    "INL rural police station, Florencia, Caquetá, Colombia (USASpending PoP Colombia).",
    "usaspending_eterna_florencia_police_1p63m_2019",
    "THE PURPOSE OF THIS TASK ORDER IS TO CONSTRUCT A RURAL INL POLICE STATION IN FLORENCIA, CO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0489_9700_W9127817D0095_9700/",
    "Actor: Eterna (Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle962",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127819F0489_9700_W9127817D0095_9700 (Eterna Florencia police). Signed 2019-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127819F0489_9700_W9127817D0095_9700/.",
    "USASpending: Eterna Florencia police USD 1.629m. Supports eterna_florencia_police_1p63m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1628986.24; date_signed 2019-09-24.",
)

row_doc(
    "palgag_us_terrier_rouge_1p59m_2016",
    "infrastructure", "building_materials", "us",
    "Palgag US — Terrier Rouge construction",
    "Haiti",
    "23 Jun 2016: Department of State awards contract SAQMMA16C0138 to Palgag US for Terrier Rouge construction; obligated USD 1,588,000. CapEx face = award obligation.",
    "1588000", "2016-06-23", "2016", "19.650", "-71.950",
    "Construction contract, Terrier Rouge, Haiti (USASpending PoP Haiti).",
    "usaspending_palgag_us_terrier_rouge_1p59m_2016",
    "TERRIER ROUGE CONSTRUCTION CONTRACT OTHER FUNCTIONS IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0138_1900_-NONE-_-NONE-/",
    "Actor: Palgag US LLC (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle962",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16C0138_1900_-NONE-_-NONE- (Palgag US Terrier Rouge). Signed 2016-06-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0138_1900_-NONE-_-NONE-/.",
    "USASpending: Palgag US Terrier Rouge USD 1.588m. Supports palgag_us_terrier_rouge_1p59m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1588000; date_signed 2016-06-23.",
)

row_doc(
    "montajes_savart_bogota_canopy_1p57m_2014",
    "infrastructure", "building_materials", "other",
    "Montajes Savart — Bogotá consular waiting area canopy",
    "Colombia",
    "21 Feb 2014: Department of State awards contract SAQMMA14C0060 to Montajes Savart for Bogotá consular waiting area canopy construction; obligated USD 1,568,802.96. CapEx face = award obligation.",
    "1568802.96", "2014-02-21", "2014", "4.624", "-74.065",
    "Consular waiting area canopy, Bogotá, Colombia (USASpending PoP Colombia).",
    "usaspending_montajes_savart_bogota_canopy_1p57m_2014",
    "BOGOTA CONSULAR WAITING AREA CANOPY CONSTRUCTION PROJECT.  IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0060_1900_-NONE-_-NONE-/",
    "Actor: Montajes Savart (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle962",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14C0060_1900_-NONE-_-NONE- (Montajes Savart Bogotá canopy). Signed 2014-02-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0060_1900_-NONE-_-NONE-/.",
    "USASpending: Montajes Savart Bogotá canopy USD 1.569m. Supports montajes_savart_bogota_canopy_1p57m_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1568802.96; date_signed 2014-02-21.",
)

row_doc(
    "mesan_trinidad_consular_waiting_1p56m_2011",
    "infrastructure", "building_materials", "us",
    "Mesan-Martinez JV — Trinidad consular waiting area enclosure design/build",
    "Trinidad and Tobago",
    "29 Sep 2011: Department of State awards task order SAQMMA11F4440 to Mesan-Martinez JV for design/build consular waiting area enclosure (PoP Trinidad and Tobago); obligated USD 1,564,699.60. CapEx face = award obligation.",
    "1564699.60", "2011-09-29", "2011", "10.654", "-61.502",
    "Consular waiting area enclosure, Port of Spain area, Trinidad and Tobago (USASpending PoP Trinidad and Tobago).",
    "usaspending_mesan_trinidad_consular_waiting_1p56m_2011",
    "DESIGN/BUILD FOR CONSULAR WAITING AREA ENCLOSURE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4440_1900_SAQMMA08D0015_1900/",
    "Actor: Mesan-Martinez JV (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle962",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F4440_1900_SAQMMA08D0015_1900 (Mesan Trinidad consular waiting). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4440_1900_SAQMMA08D0015_1900/.",
    "USASpending: Mesan Trinidad consular waiting USD 1.565m. Supports mesan_trinidad_consular_waiting_1p56m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1564699.60; date_signed 2011-09-29.",
)

row_doc(
    "serfor_peru_balsa_tornillo_chain_2025",
    "resources", "balsa", "other",
    "SERFOR / MIDAGRI — Peru commercial forest plantations chain (tornillo y balsa)",
    "Peru",
    "SERFOR (MIDAGRI) public notice: promotes the productive chain of commercial forest plantations of tornillo and balsa wood in Peru via Jueves del Conocimiento webinar. Presence/policy face — CapEx USD blank (event does not state a balsa-only CapEx envelope).",
    "", "2025-01-01", "2025", "-12.046", "-77.043",
    "SERFOR national program presence, Peru (Lima pin for ministry; plantations nationwide).",
    "serfor_peru_balsa_tornillo_chain_2025",
    "viene impulsando la cadena productiva de plantaciones forestales comerciales de madera tornillo y balsa en el Perú",
    "https://www.gob.pe/institucion/serfor/noticias/1219301-midagri-serfor-promueve-la-cadena-productiva-de-plantaciones-forestales-comerciales-de-madera-tornillo-y-balsa",
    "Actor: SERFOR / Gobierno del Perú — other. Official gob.pe primary. Thin top-up balsa (Peru under-covered). CapEx blank.",
    "hunt_cycle962",
    "Servicio Nacional Forestal y de Fauna Silvestre (SERFOR). “MIDAGRI: SERFOR promueve la cadena productiva de plantaciones forestales comerciales de madera tornillo y balsa.” Gob.pe. https://www.gob.pe/institucion/serfor/noticias/1219301-midagri-serfor-promueve-la-cadena-productiva-de-plantaciones-forestales-comerciales-de-madera-tornillo-y-balsa.",
    "SERFOR Peru tornillo y balsa productive chain (presence). Supports serfor_peru_balsa_tornillo_chain_2025.",
    "Opened gob.pe SERFOR notice 2026-10-05; no balsa-only CapEx figure on page.",
    investment_type="presence", currency="USD", value_usd="", fx_usd="",
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
    print(f"cycles960-962 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
