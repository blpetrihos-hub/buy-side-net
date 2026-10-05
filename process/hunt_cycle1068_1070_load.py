#!/usr/bin/env python3
"""Cycles 1068–1070: USASpending LatAm CapEx residual (~USD0.058–0.065m).

Seeds: 20262068–20262070. Thin top-up dry.
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


# === Cycle 1068 (seed 20262068) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "pono_aina_bahamas_repair_renovate_63k_2021",
    "infrastructure", "building_materials", "us",
    "Pono Aina Management — Bahamas property repair/renovate",
    "Bahamas",
    "24 Sep 2021: Department of State awards contract 19BF5021P0809 to Pono Aina Management LLC for repair/renovate (properties 103-01-2004 and 103-01-2010) (PoP Bahamas); obligated USD 63,194.66. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.",
    "63194.66", "2021-09-24", "2021", "", "",
    "Repair/renovate properties 103-01-2004 and 103-01-2010, Bahamas (USASpending description; sites not named — lat/lon blank).",
    "usaspending_pono_aina_bahamas_repair_renovate_63k_2021",
    "103-01-2004 & 103-01-2010 - REPAIR/RENOVATE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5021P0809_1900_-NONE-_-NONE-/",
    "Actor: Pono Aina Management LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1068",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BF5021P0809_1900_-NONE-_-NONE- (Pono Aina Bahamas repair/renovate). Signed 2021-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5021P0809_1900_-NONE-_-NONE-/.",
    "USASpending: Pono Aina Bahamas repair/renovate USD 0.063m. Supports pono_aina_bahamas_repair_renovate_63k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 63194.66; date_signed 2021-09-24.",
)

row_doc(
    "ati_dr_chancery_bas_63k_2019",
    "energy", "power_plants_grid", "us",
    "ATI — Dominican Republic chancery building automation system",
    "Dominican Republic",
    "23 Nov 2019: Department of State awards contract 19DR8620P0046 to ATI, Inc. for BME building automation system (BAS) chancery building (PoP Dominican Republic); obligated USD 62,919. CapEx face = award obligation. Exact chancery site unnamed — lat/lon blank.",
    "62919", "2019-11-23", "2019", "", "",
    "Building automation system (BAS) for chancery building, Dominican Republic (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_ati_dr_chancery_bas_63k_2019",
    "BME BUILDING AUTOMATION SYSTEM (BAS) CHANCERY BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8620P0046_1900_-NONE-_-NONE-/",
    "Actor: ATI, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1068",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8620P0046_1900_-NONE-_-NONE- (ATI DR chancery BAS). Signed 2019-11-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8620P0046_1900_-NONE-_-NONE-/.",
    "USASpending: ATI DR chancery BAS USD 0.063m. Supports ati_dr_chancery_bas_63k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62919; date_signed 2019-11-23.",
)

row_doc(
    "misc_argentina_villate_remodel_65k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina C. Villate 1395 Olivos remodel",
    "Argentina",
    "30 Sep 2018: Department of State awards contract 19AR2018C0010 for remodel at C. Villate 1395, Olivos (PoP Argentina); obligated USD 64,682. CapEx face = award obligation. Exact building coords not stated — lat/lon blank.",
    "64682", "2018-09-30", "2018", "", "",
    "Remodel at C. Villate 1395, Olivos, Argentina (USASpending description; address named, coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_villate_remodel_65k_2018",
    "REMODEL C. VILLATE 1395, OLIVOS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018C0010_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1068",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2018C0010_1900_-NONE-_-NONE- (Argentina Villate remodel). Signed 2018-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018C0010_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina Villate remodel USD 0.065m. Supports misc_argentina_villate_remodel_65k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 64682; date_signed 2018-09-30.",
)

row_doc(
    "misc_panama_whse_racks_65k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Panama warehouse racks replacement",
    "Panama",
    "4 Jun 2010: Department of State awards contract SPM07010M0348 for replace warehouse racks (PoP Panama); obligated USD 65,000. CapEx face = award obligation. Exact warehouse unnamed — lat/lon blank.",
    "65000", "2010-06-04", "2010", "", "",
    "Replace warehouse racks, Panama (USASpending description; warehouse not named — lat/lon blank).",
    "usaspending_misc_panama_whse_racks_65k_2010",
    "REPLACE WHSE RACKS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07010M0348_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1068",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07010M0348_1900_-NONE-_-NONE- (Panama WHSE racks). Signed 2010-06-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07010M0348_1900_-NONE-_-NONE-/.",
    "USASpending: Panama WHSE racks USD 0.065m. Supports misc_panama_whse_racks_65k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65000; date_signed 2010-06-04.",
)

row_doc(
    "diaz_villegas_colombia_inl_ae_63k_2020",
    "infrastructure", "engineering_epc", "other",
    "Diaz Villegas Arquitectos — Colombia INL Bogota A&E",
    "Colombia",
    "7 Apr 2020: Department of State awards contract 19C01520P0137 to Diaz Villegas Arquitectos S.A.S. for INL Bogota A&E (PoP Colombia); obligated USD 63,036.41. CapEx face = award obligation. Exact project site unnamed — lat/lon blank.",
    "63036.41", "2020-04-07", "2020", "", "",
    "INL Bogota A&E, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_diaz_villegas_colombia_inl_ae_63k_2020",
    "INL BOGOTA A&E",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520P0137_1900_-NONE-_-NONE-/",
    "Actor: Diaz Villegas Arquitectos S.A.S. (Colombia) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1068",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01520P0137_1900_-NONE-_-NONE- (Diaz Villegas Colombia INL A&E). Signed 2020-04-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520P0137_1900_-NONE-_-NONE-/.",
    "USASpending: Diaz Villegas Colombia INL A&E USD 0.063m. Supports diaz_villegas_colombia_inl_ae_63k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 63036.41; date_signed 2020-04-07.",
)

# === Cycle 1069 (seed 20262069) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "siegel_costa_rica_ae_assessment_61k_2024",
    "infrastructure", "engineering_epc", "us",
    "Robert Siegel — Costa Rica San Jose A&E assessment report",
    "Costa Rica",
    "16 Sep 2024: Department of State awards order 19AQMM24F2169 to Robert Siegel for San Jose, Costa Rica A&E assessment report (PoP Costa Rica); obligated USD 61,081.19. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "61081.19", "2024-09-16", "2024", "", "",
    "A&E assessment report, San Jose, Costa Rica (USASpending description; San Jose named, site coords not stated — lat/lon blank).",
    "usaspending_siegel_costa_rica_ae_assessment_61k_2024",
    "SAN JOSE, COSTA RICA A&E ASSESSMENT REPORT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2169_1900_19AQMM19D0046_1900/",
    "Actor: Robert Siegel (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1069",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24F2169_1900_19AQMM19D0046_1900 (Siegel Costa Rica A&E). Signed 2024-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2169_1900_19AQMM19D0046_1900/.",
    "USASpending: Siegel Costa Rica A&E USD 0.061m. Supports siegel_costa_rica_ae_assessment_61k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 61081.19; date_signed 2024-09-16.",
)

row_doc(
    "digital_plaza_belize_ups_60k_2014",
    "energy", "power_plants_grid", "us",
    "Digital Plaza — Belize INL communications UPS electrical power hardware",
    "Belize",
    "5 Aug 2014: Department of State awards contract SBH20014M0214 to Digital Plaza LLC for INL communications system UPS electrical power hardware all sites (PoP Belize); obligated USD 59,899.65. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.",
    "59899.65", "2014-08-05", "2014", "", "",
    "Communications system UPS electrical power hardware, Belize (USASpending description; sites not named — lat/lon blank).",
    "usaspending_digital_plaza_belize_ups_60k_2014",
    "INL IN13BZMS COMM SYSTEM UPS ELEC PWR HARDWARE ALL SITES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20014M0214_1900_-NONE-_-NONE-/",
    "Actor: Digital Plaza LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1069",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20014M0214_1900_-NONE-_-NONE- (Digital Plaza Belize UPS). Signed 2014-08-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20014M0214_1900_-NONE-_-NONE-/.",
    "USASpending: Digital Plaza Belize UPS USD 0.060m. Supports digital_plaza_belize_ups_60k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59899.65; date_signed 2014-08-05.",
)

row_doc(
    "misc_chile_transformer_63k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Chile replacement service and new transformer",
    "Chile",
    "21 Mar 2024: Department of State awards contract 19C18024P0543 for replacement service and new transformer (PoP Chile); obligated USD 62,897.22. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "62897.22", "2024-03-21", "2024", "", "",
    "Replacement service and new transformer, Chile (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_chile_transformer_63k_2024",
    "REPLACEMENT SERVICE AND NEW TRANSFORMER.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18024P0543_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1069",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C18024P0543_1900_-NONE-_-NONE- (Chile transformer). Signed 2024-03-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18024P0543_1900_-NONE-_-NONE-/.",
    "USASpending: Chile transformer USD 0.063m. Supports misc_chile_transformer_63k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62897.22; date_signed 2024-03-21.",
)

row_doc(
    "misc_argentina_obc_locker_remodel_63k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina OBC basement locker rooms remodel",
    "Argentina",
    "28 Sep 2018: Department of State awards contract 19AR2018C0006 for basement locker rooms remodel at OBC (PoP Argentina); obligated USD 62,884.99. CapEx face = award obligation. Exact OBC site unnamed — lat/lon blank.",
    "62884.99", "2018-09-28", "2018", "", "",
    "Basement locker rooms remodel at OBC, Argentina (USASpending description; OBC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_obc_locker_remodel_63k_2018",
    "FM - BASEMENT LOCKER ROOMS REMODEL AT OBC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018C0006_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1069",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2018C0006_1900_-NONE-_-NONE- (Argentina OBC locker remodel). Signed 2018-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018C0006_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina OBC locker remodel USD 0.063m. Supports misc_argentina_obc_locker_remodel_63k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62884.99; date_signed 2018-09-28.",
)

row_doc(
    "gamma_mexico_musset_bathrooms_63k_2019",
    "infrastructure", "building_materials", "other",
    "Despacho de Arquitectos Gamma — Mexico Musset 337 bathroom repairs",
    "Mexico",
    "11 Jun 2019: Department of State awards contract 19MX5319C0010 to Despacho de Arquitectos Gamma for bathroom repairs at Musset 337 (PoP Mexico); obligated USD 62,768.06. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "62768.06", "2019-06-11", "2019", "", "",
    "Bathroom repairs at Musset 337, Mexico (USASpending description; Musset 337 named, coords not stated — lat/lon blank).",
    "usaspending_gamma_mexico_musset_bathrooms_63k_2019",
    "MEX-FAC-OBO-BATHROOMS REPAIRS AT MUSSET 337",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319C0010_1900_-NONE-_-NONE-/",
    "Actor: Despacho de Arquitectos Gamma (Mexico) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1069",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5319C0010_1900_-NONE-_-NONE- (Gamma Mexico Musset bathrooms). Signed 2019-06-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319C0010_1900_-NONE-_-NONE-/.",
    "USASpending: Gamma Mexico Musset bathrooms USD 0.063m. Supports gamma_mexico_musset_bathrooms_63k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62768.06; date_signed 2019-06-11.",
)

# === Cycle 1070 (seed 20262070) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "green_bear_mexico_led_fixtures_59k_2016",
    "infrastructure", "building_materials", "us",
    "Green Bear — Mexico ICASS LED fixtures property 1001",
    "Mexico",
    "29 Sep 2016: Department of State awards contract SMX11516M0438 to Green Bear LLC for ICASS LED fixtures at property 1001 (PoP Mexico); obligated USD 59,412.90. CapEx face = award obligation. Exact property unnamed beyond id — lat/lon blank.",
    "59412.90", "2016-09-29", "2016", "", "",
    "ICASS LED fixtures at property 1001, Mexico (USASpending description; property id named, coords not stated — lat/lon blank).",
    "usaspending_green_bear_mexico_led_fixtures_59k_2016",
    "ICASS-LED FIXTURES PROP 1001 ''IGF::OT::IGF''",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516M0438_1900_-NONE-_-NONE-/",
    "Actor: Green Bear LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1070",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11516M0438_1900_-NONE-_-NONE- (Green Bear Mexico LED). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516M0438_1900_-NONE-_-NONE-/.",
    "USASpending: Green Bear Mexico LED USD 0.059m. Supports green_bear_mexico_led_fixtures_59k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59412.90; date_signed 2016-09-29.",
)

row_doc(
    "jcba_panama_nec_chillers_ahu_59k_2020",
    "energy", "power_plants_grid", "us",
    "Johnson Controls Building Automation — Panama NEC chillers, cooling towers and AHU",
    "Panama",
    "22 Aug 2020: Department of State awards contract 19PM0720P0664 to Johnson Controls Building Automation Systems, LLC for NEC BME chillers, cooling towers and AHU (PoP Panama); obligated USD 58,512.57. CapEx face = award obligation. Exact NEC site unnamed — lat/lon blank.",
    "58512.57", "2020-08-22", "2020", "", "",
    "NEC BME chillers, cooling towers and AHU, Panama (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_jcba_panama_nec_chillers_ahu_59k_2020",
    "19PM0720P0664 NEC - BME - CHILLERS, COOLING TOWERS&AHU CONTRACT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0720P0664_1900_-NONE-_-NONE-/",
    "Actor: Johnson Controls Building Automation Systems, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1070",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0720P0664_1900_-NONE-_-NONE- (JCBA Panama NEC chillers/AHU). Signed 2020-08-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0720P0664_1900_-NONE-_-NONE-/.",
    "USASpending: JCBA Panama NEC chillers/AHU USD 0.059m. Supports jcba_panama_nec_chillers_ahu_59k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 58512.57; date_signed 2020-08-22.",
)

row_doc(
    "misc_honduras_usaid_reflective_glass_63k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Honduras USAID building reflective glass windows",
    "Honduras",
    "26 Sep 2015: USAID awards award AID522O1500081 for reflective glass windows for USAID building (PoP Honduras); obligated USD 62,727.40. CapEx face = award obligation. Exact USAID building unnamed — lat/lon blank.",
    "62727.40", "2015-09-26", "2015", "", "",
    "Reflective glass windows for USAID building, Honduras (USASpending description; building not named — lat/lon blank).",
    "usaspending_misc_honduras_usaid_reflective_glass_63k_2015",
    "IGF::CL::IGF REFLECTIVE GLASS WINDOWS FOR USAID/ BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1500081_7200_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1070",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID522O1500081_7200_-NONE-_-NONE- (Honduras USAID reflective glass). Signed 2015-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1500081_7200_-NONE-_-NONE-/.",
    "USASpending: Honduras USAID reflective glass USD 0.063m. Supports misc_honduras_usaid_reflective_glass_63k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62727.40; date_signed 2015-09-26.",
)

row_doc(
    "sukimotor_panama_power_generator_62k_2023",
    "energy", "power_plants_grid", "other",
    "Sukimotor — Panama power generator",
    "Panama",
    "23 Jun 2023: Department of State awards contract 19PM0723P0755 to Sukimotor, S.A. for power generator (PoP Panama); obligated USD 62,485.92. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "62485.92", "2023-06-23", "2023", "", "",
    "Power generator, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_sukimotor_panama_power_generator_62k_2023",
    "POWER GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0723P0755_1900_-NONE-_-NONE-/",
    "Actor: Sukimotor, S.A. (Panama) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1070",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0723P0755_1900_-NONE-_-NONE- (Sukimotor Panama generator). Signed 2023-06-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0723P0755_1900_-NONE-_-NONE-/.",
    "USASpending: Sukimotor Panama generator USD 0.062m. Supports sukimotor_panama_power_generator_62k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62485.92; date_signed 2023-06-23.",
)

row_doc(
    "misc_uruguay_cmr_parking_62k_2023",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Uruguay CMR rear service entrance parking repair",
    "Uruguay",
    "3 Feb 2023: Department of State awards contract 19UY6023P0235 for repair parking area at rear service entrance at CMR (PoP Uruguay); obligated USD 62,485.64. CapEx face = award obligation. Exact CMR site unnamed — lat/lon blank.",
    "62485.64", "2023-02-03", "2023", "", "",
    "Repair parking area at rear service entrance at CMR, Uruguay (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_uruguay_cmr_parking_62k_2023",
    "REPAIR PARKING AREA AT REAR SERVICE ENTRANCE AT CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6023P0235_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads. Holdover closed.",
    "hunt_cycle1070",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19UY6023P0235_1900_-NONE-_-NONE- (Uruguay CMR parking). Signed 2023-02-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6023P0235_1900_-NONE-_-NONE-/.",
    "USASpending: Uruguay CMR parking USD 0.062m. Supports misc_uruguay_cmr_parking_62k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 62485.64; date_signed 2023-02-03.",
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
