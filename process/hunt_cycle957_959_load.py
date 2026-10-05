#!/usr/bin/env python3
"""Cycles 957–959: USASpending LatAm CapEx residual (Caucasia, clinics, Obera SSC, elevators).

Seeds: 20261957–20261959. Thin top-up dry.
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


# === Cycle 957 ===
row_doc(
    "vistas_brazil_chiller_2p84m_2012",
    "infrastructure", "building_materials", "us",
    "The Vistas Group — Brazil chiller replacement",
    "Brazil",
    "8 Aug 2012: Department of State awards task order SAQMMA12F2735 to The Vistas Group for chiller replacement project (PoP Brazil); obligated USD 2,837,735. CapEx face = award obligation. Distinct from vistas_porto_alegre/brasilia/recife rows.",
    "2837735", "2012-08-08", "2012", "", "",
    "Chiller replacement, Brazil (USASpending PoP Brazil; post not named — lat/lon blank).",
    "usaspending_vistas_brazil_chiller_2p84m_2012",
    "CHILLER REPLACEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2735_1900_SAQMMA08D0006_1900/",
    "Actor: The Vistas Group (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle957",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F2735_1900_SAQMMA08D0006_1900 (Vistas Brazil chiller). Signed 2012-08-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2735_1900_SAQMMA08D0006_1900/.",
    "USASpending: Vistas Brazil chiller USD 2.838m. Supports vistas_brazil_chiller_2p84m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2837735; date_signed 2012-08-08.",
)

row_doc(
    "proyectos_civiles_caucasia_2p33m_2022",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles S y M — BRCNA Caucasia renovations",
    "Colombia",
    "12 May 2022: Department of State awards task order 19AQMM22F0796 to Proyectos Civiles for BRCNA Caucasia renovations; obligated USD 2,334,421.49. CapEx face = award obligation.",
    "2334421.49", "2022-05-12", "2022", "7.987", "-75.198",
    "BRCNA renovations, Caucasia, Antioquia, Colombia (USASpending PoP Colombia).",
    "usaspending_proyectos_civiles_caucasia_2p33m_2022",
    "BRCNA CAUCASIA RENOVATIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0796_1900_19AQMM21D0039_1900/",
    "Actor: Proyectos Civiles S y M (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle957",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F0796_1900_19AQMM21D0039_1900 (Proyectos Civiles Caucasia). Signed 2022-05-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F0796_1900_19AQMM21D0039_1900/.",
    "USASpending: Proyectos Civiles Caucasia USD 2.334m. Supports proyectos_civiles_caucasia_2p33m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2334421.49; date_signed 2022-05-12.",
)

row_doc(
    "eei_caucasia_admin_lodging_2p29m_2026",
    "infrastructure", "building_materials", "other",
    "EEI — CNP Caucasia admin and lodging construction",
    "Colombia",
    "28 Jul 2026: Department of State awards task order 19AQMM26F0994 to EEI for CNP Caucasia admin and lodging construction; obligated USD 2,294,643.46. CapEx face = award obligation. Distinct from proyectos_civiles_caucasia.",
    "2294643.46", "2026-07-28", "2026", "7.987", "-75.198",
    "CNP admin and lodging construction, Caucasia, Antioquia, Colombia (USASpending PoP Colombia).",
    "usaspending_eei_caucasia_admin_lodging_2p29m_2026",
    "CNP CAUCASIA ADMIN AND LODGING CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F0994_1900_19AQMM21D0037_1900/",
    "Actor: EEI (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle957",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM26F0994_1900_19AQMM21D0037_1900 (EEI Caucasia admin). Signed 2026-07-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F0994_1900_19AQMM21D0037_1900/.",
    "USASpending: EEI Caucasia admin USD 2.295m. Supports eei_caucasia_admin_lodging_2p29m_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2294643.46; date_signed 2026-07-28.",
)

row_doc(
    "guayaquil_antinarcotics_facility_2p23m_2009",
    "infrastructure", "building_materials", "other",
    "Foreign awardee — Guayaquil port anti-narcotics police facility",
    "Ecuador",
    "9 Sep 2009: Department of State awards contract SWHARC09C0002 for construction of anti-narcotics police facility at Port of Guayaquil, Guayas; obligated USD 2,230,551.17. CapEx face = award obligation.",
    "2230551.17", "2009-09-09", "2009", "-2.170", "-79.922",
    "Anti-narcotics police facility, Port of Guayaquil, Ecuador (USASpending PoP Ecuador).",
    "usaspending_guayaquil_antinarcotics_facility_2p23m_2009",
    "CONSTRUCTION OF ANTI-NARCOTICS POLICE FACILITY AT THE PORT OF GUAYAQUIL -- GUAYAS PROVINCE OF ECUADOR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC09C0002_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardee — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle957",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC09C0002_1900_-NONE-_-NONE- (Guayaquil anti-narcotics facility). Signed 2009-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC09C0002_1900_-NONE-_-NONE-/.",
    "USASpending: Guayaquil anti-narcotics facility USD 2.231m. Supports guayaquil_antinarcotics_facility_2p23m_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2230551.17; date_signed 2009-09-09.",
)

row_doc(
    "anastasia_mexico_clinics_1p96m_2021",
    "infrastructure", "building_materials", "us",
    "The Anastasia Group — Mexico 17 medical clinics refurbishment",
    "Mexico",
    "20 May 2021: Department of the Air Force awards contract FA251821C0001 to The Anastasia Group to refurbish 17 medical clinics (PoP Mexico); obligated USD 1,963,640. CapEx face = award obligation.",
    "1963640", "2021-05-20", "2021", "", "",
    "Refurbish 17 medical clinics, Mexico (USASpending PoP Mexico; clinic sites not named — lat/lon blank).",
    "usaspending_anastasia_mexico_clinics_1p96m_2021",
    "SERVICES TO REFURBISH 17 MEDICAL CLINICS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA251821C0001_9700_-NONE-_-NONE-/",
    "Actor: The Anastasia Group (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle957",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA251821C0001_9700_-NONE-_-NONE- (Anastasia Mexico clinics). Signed 2021-05-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA251821C0001_9700_-NONE-_-NONE-/.",
    "USASpending: Anastasia Mexico clinics USD 1.964m. Supports anastasia_mexico_clinics_1p96m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1963640; date_signed 2021-05-20.",
)

# === Cycle 958 ===
row_doc(
    "sea_pac_colombia_elevator_1p96m_2023",
    "infrastructure", "building_materials", "us",
    "Sea Pac Engineering — Colombia elevator project",
    "Colombia",
    "20 Jul 2023: Department of State awards contract 19GE5023C0026 to Sea Pac Engineering for elevator project (PoP Colombia); obligated USD 1,955,000. CapEx face = award obligation. Distinct from sea_pac_lima/san_jose/san_salvador elevators.",
    "1955000", "2023-07-20", "2023", "4.624", "-74.065",
    "Elevator project, Colombia (USASpending PoP Colombia; Bogotá pin for diplomatic post).",
    "usaspending_sea_pac_colombia_elevator_1p96m_2023",
    "ELEVATOR PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0026_1900_-NONE-_-NONE-/",
    "Actor: Sea Pac Engineering (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle958",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5023C0026_1900_-NONE-_-NONE- (Sea Pac Colombia elevator). Signed 2023-07-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0026_1900_-NONE-_-NONE-/.",
    "USASpending: Sea Pac Colombia elevator USD 1.955m. Supports sea_pac_colombia_elevator_1p96m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1955000; date_signed 2023-07-20.",
)

row_doc(
    "trinity_bhate_monterrey_fence_1p90m_2016",
    "infrastructure", "building_materials", "us",
    "Trinity/Bhate JV — Monterrey NCC fence, consular canopy, drainage",
    "Mexico",
    "9 Sep 2016: Department of State awards task order SAQMMA16F4006 to Trinity/Bhate JV for fence, consular canopy and drainage at Monterrey New Consulate Compound; obligated USD 1,895,287. CapEx face = award obligation.",
    "1895287", "2016-09-09", "2016", "25.686", "-100.316",
    "Fence/canopy/drainage, Monterrey NCC, Mexico (USASpending PoP Mexico).",
    "usaspending_trinity_bhate_monterrey_fence_1p90m_2016",
    "TASK ORDER FOR CONSTRUCTION OF A FENCE, CONSULAR CANOPY AND DRAINAGE FOR THE MONTERREY, MEXICO NEW CONSULATE COMPOUND.  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F4006_1900_SAQMMA14D0044_1900/",
    "Actor: Trinity/Bhate JV (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle958",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F4006_1900_SAQMMA14D0044_1900 (Trinity/Bhate Monterrey). Signed 2016-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F4006_1900_SAQMMA14D0044_1900/.",
    "USASpending: Trinity/Bhate Monterrey USD 1.895m. Supports trinity_bhate_monterrey_fence_1p90m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1895287; date_signed 2016-09-09.",
)

row_doc(
    "cfe_ncc_acolhuas_feeders_1p90m_2021",
    "infrastructure", "power_plants_grid", "other",
    "CFE Distribución — NCC Calle Acolhuas medium-voltage feeders",
    "Mexico",
    "3 Feb 2021: Department of State awards contract 19GE5021C0005 to CFE Distribución to design and construct two new medium-voltage three-phase power feeders from two substations to U.S. Consulate Compound (NCC) demarcation room on Calle Acolhuas; obligated USD 1,899,590.79. CapEx face = award obligation. Distinct from cfe_nec_mexico_city_electrical.",
    "1899590.79", "2021-02-03", "2021", "-19.330", "-99.110",
    "Medium-voltage feeders to NCC on Calle Acolhuas, Mexico (USASpending PoP Mexico; Culhuacán/Mexico City area pin).",
    "usaspending_cfe_ncc_acolhuas_feeders_1p90m_2021",
    "THE CONTRACTOR SHALL COMPLETE ALL WORK REQUIRED TO DESIGN AND CONSTRUCT TWO NEW MEDIUM VOLTAGE, THREE PHASE POWER FEEDERS FROM TWO DISTINCT SUBSTATIONS TO THE U.S. CONSULATE COMPOUND (NCC) DEMARCATION ROOM LOCATED ON CALLE ACOLHUAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0005_1900_-NONE-_-NONE-/",
    "Actor: CFE Distribución (Mexico) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle958",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5021C0005_1900_-NONE-_-NONE- (CFE NCC Acolhuas feeders). Signed 2021-02-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0005_1900_-NONE-_-NONE-/.",
    "USASpending: CFE NCC Acolhuas feeders USD 1.900m. Supports cfe_ncc_acolhuas_feeders_1p90m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1899590.79; date_signed 2021-02-03.",
)

row_doc(
    "serrano_ecuador_residence_3p29m_2020",
    "infrastructure", "building_materials", "other",
    "Serrano Proaño — Ecuador residence design/build renovation",
    "Ecuador",
    "24 Sep 2020: Department of State awards contract 19GE5020C0027 to Serrano Proaño for design/build residence renovation (PoP Ecuador); obligated USD 3,286,371.67. CapEx face = award obligation.",
    "3286371.67", "2020-09-24", "2020", "-0.180", "-78.468",
    "Residence design/build renovation, Ecuador (USASpending PoP Ecuador; Quito pin).",
    "usaspending_serrano_ecuador_residence_3p29m_2020",
    "DESIGN/BUILD SERVICES FOR RESIDENCE RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5020C0027_1900_-NONE-_-NONE-/",
    "Actor: Serrano Proaño (Ecuador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle958",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5020C0027_1900_-NONE-_-NONE- (Serrano Ecuador residence). Signed 2020-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5020C0027_1900_-NONE-_-NONE-/.",
    "USASpending: Serrano Ecuador residence USD 3.286m. Supports serrano_ecuador_residence_3p29m_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3286371.67; date_signed 2020-09-24.",
)

row_doc(
    "falcon_spectrum_rio_elevators_2p69m_2009",
    "infrastructure", "building_materials", "us",
    "Falcon Spectrum JV — Rio de Janeiro elevator repair/improvement",
    "Brazil",
    "20 Aug 2009: Department of State awards task order SAQMMA09F2722 to Falcon Spectrum JV for Phase I site survey repair and improvement of 4 elevators in Rio de Janeiro; obligated USD 2,689,338.55. CapEx face = award obligation.",
    "2689338.55", "2009-08-20", "2009", "-22.907", "-43.173",
    "Elevator repair/improvement (4 elevators), Rio de Janeiro, Brazil (USASpending PoP Brazil).",
    "usaspending_falcon_spectrum_rio_elevators_2p69m_2009",
    "PHASE I - SITE SURVEY REPAIR AND IMPROVEMENT OF 4 ELEVATORS. GENERAL CONTRACTING SERVICES FOR ELEVATOR REPAIR AND IMPROVEMENT PROJECT IN RIO DE JANEIRO, BRAZIL.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA09F2722_1900_SAQMMA08D0016_1900/",
    "Actor: Falcon Spectrum JV (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle958",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA09F2722_1900_SAQMMA08D0016_1900 (Falcon Spectrum Rio elevators). Signed 2009-08-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA09F2722_1900_SAQMMA08D0016_1900/.",
    "USASpending: Falcon Spectrum Rio elevators USD 2.689m. Supports falcon_spectrum_rio_elevators_2p69m_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2689338.55; date_signed 2009-08-20.",
)

# === Cycle 959 ===
row_doc(
    "obera_mexico_ssc_7p80m_2023",
    "infrastructure", "building_materials", "us",
    "Obera — Northern/Southern Command small-scale construction (Mexico PoP)",
    "Mexico",
    "27 Sep 2023: Department of the Air Force awards contract FA489023C0035 to Obera for Northern and Southern Command small-scale construction (PoP Mexico); obligated USD 7,797,746.98. CapEx face = award obligation.",
    "7797746.98", "2023-09-27", "2023", "", "",
    "NORTHCOM/SOUTHCOM small-scale construction, Mexico (USASpending PoP Mexico; sites not named — lat/lon blank).",
    "usaspending_obera_mexico_ssc_7p80m_2023",
    "NORTHERN AND SOUTHERN COMMAND SMALL SCALE CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489023C0035_9700_-NONE-_-NONE-/",
    "Actor: Obera (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle959",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489023C0035_9700_-NONE-_-NONE- (Obera Mexico SSC). Signed 2023-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489023C0035_9700_-NONE-_-NONE-/.",
    "USASpending: Obera Mexico SSC USD 7.798m. Supports obera_mexico_ssc_7p80m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7797746.98; date_signed 2023-09-27.",
)

row_doc(
    "obera_mexico_fy24_ssc_7p74m_2024",
    "infrastructure", "building_materials", "us",
    "Obera — FY24 NORTHCOM small-scale construction (Mexico PoP)",
    "Mexico",
    "27 Sep 2024: Department of the Air Force awards task order FA489024F0168 to Obera for FY24 NORTHCOM small-scale construction / counter-narcotics and global threats ops support (PoP Mexico); obligated USD 7,742,416.05. CapEx face = award obligation. Distinct from obera_mexico_ssc_7p80m_2023.",
    "7742416.05", "2024-09-27", "2024", "", "",
    "FY24 NORTHCOM small-scale construction, Mexico (USASpending PoP Mexico; sites not named — lat/lon blank).",
    "usaspending_obera_mexico_fy24_ssc_7p74m_2024",
    "FY 24 NORTHCOM SMALL SCALE CONSTRUCTION  COUNTER-NARCOTICS AND GLOBAL THREATS OPERATIONS, LOGISTICS AND TRAINING SUPPORT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489024F0168_9700_FA489023D0008_9700/",
    "Actor: Obera (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle959",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489024F0168_9700_FA489023D0008_9700 (Obera Mexico FY24 SSC). Signed 2024-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489024F0168_9700_FA489023D0008_9700/.",
    "USASpending: Obera Mexico FY24 SSC USD 7.742m. Supports obera_mexico_fy24_ssc_7p74m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7742416.05; date_signed 2024-09-27.",
)

row_doc(
    "obera_costa_rica_ssc_4p82m_2024",
    "infrastructure", "building_materials", "us",
    "Obera — SOUTHCOM small-scale construction (Costa Rica PoP)",
    "Costa Rica",
    "23 Sep 2024: Department of the Air Force awards task order FA489024F0158 to Obera for SOUTHCOM small-scale construction / counter-narcotics and global threats ops support (PoP Costa Rica); obligated USD 4,817,459.52. CapEx face = award obligation.",
    "4817459.52", "2024-09-23", "2024", "", "",
    "SOUTHCOM small-scale construction, Costa Rica (USASpending PoP Costa Rica; sites not named — lat/lon blank).",
    "usaspending_obera_costa_rica_ssc_4p82m_2024",
    "SOUTHCOM SMALL SCALE CONSTRUCTION  COUNTER-NARCOTICS AND GLOBAL THREATS OPERATIONS, LOGISTICS AND TRAINING SUPPORT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489024F0158_9700_FA489023D0008_9700/",
    "Actor: Obera (U.S.) under award agency — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle959",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489024F0158_9700_FA489023D0008_9700 (Obera Costa Rica SSC). Signed 2024-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489024F0158_9700_FA489023D0008_9700/.",
    "USASpending: Obera Costa Rica SSC USD 4.817m. Supports obera_costa_rica_ssc_4p82m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4817459.52; date_signed 2024-09-23.",
)

row_doc(
    "solustart_haiti_small_reno_2p94m_2015",
    "infrastructure", "building_materials", "other",
    "Solustart — Haiti health clinic small renovations / ADA education upgrades",
    "Haiti",
    "24 Sep 2015: USAID awards task order AID521TO1500005 to Solustart for Haiti Health Infrastructure Program small renovation projects (health clinic renovations and ADA upgrades to educational facilities); obligated USD 2,944,066.36. CapEx face = award obligation. Distinct from solustart_haiti_clinics_3p22m_2016.",
    "2944066.36", "2015-09-24", "2015", "18.540", "-72.339",
    "Health clinic small renovations / ADA education upgrades, Haiti (USASpending PoP Haiti; Port-au-Prince pin).",
    "usaspending_solustart_haiti_small_reno_2p94m_2015",
    "IGF::OT::IGF HITI HEALTH INFRASTRUCTURE PROGRAM TASK ORDER: SMALL RENOVATION PROJECTS IDIQ FOR HEALTH CLINIC RENOVATIONS AND AMERICAN DISABILITY ACT UPGRADES TO EDUCATIONAL FACILITIES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521TO1500005_7200_AID521I1500002_7200/",
    "Actor: Solustart SRL (Dominican Republic) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle959",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521TO1500005_7200_AID521I1500002_7200 (Solustart Haiti small reno). Signed 2015-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521TO1500005_7200_AID521I1500002_7200/.",
    "USASpending: Solustart Haiti small reno USD 2.944m. Supports solustart_haiti_small_reno_2p94m_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2944066.36; date_signed 2015-09-24.",
)

row_doc(
    "seobra_panama_rural_clinic_1p97m_2017",
    "infrastructure", "building_materials", "other",
    "Seobra — Panama rural health clinic",
    "Panama",
    "12 Sep 2017: U.S. Army Corps of Engineers awards task order W9127817F0213 to Seobra for rural health clinic (PoP Panama); obligated USD 1,971,493.58. CapEx face = award obligation. Distinct from seobra_colombia_arws.",
    "1971493.58", "2017-09-12", "2017", "", "",
    "Rural health clinic, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_seobra_panama_rural_clinic_1p97m_2017",
    "IGF::OT::IGF RURAL HEALTH CLINIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0213_9700_W9127817D0097_9700/",
    "Actor: Seobra (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle959",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127817F0213_9700_W9127817D0097_9700 (Seobra Panama rural clinic). Signed 2017-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127817F0213_9700_W9127817D0097_9700/.",
    "USASpending: Seobra Panama rural clinic USD 1.971m. Supports seobra_panama_rural_clinic_1p97m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1971493.58; date_signed 2017-09-12.",
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
    print(f"cycles957-959 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
