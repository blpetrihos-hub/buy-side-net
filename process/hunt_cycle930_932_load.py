#!/usr/bin/env python3
"""Cycles 930–932: USASpending residual Caribbean / Southern Cone / Central America.

Seeds: 20261930–20261932. Thin top-up dry.
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


# === 930 ===
row_doc(
    "emr_paramaribo_esw_4p91m_2011",
    "infrastructure", "building_materials", "us",
    "Enviro-Management & Research, Inc. — Paramaribo early site work construction",
    "Suriname",
    "8 Jul 2011: Department of State awards task order SAQMMA11F2136 to Enviro-Management & Research, "
    "Inc. for construction of Paramaribo early site work; obligated USD 4,911,560. CapEx face = "
    "award obligation. Distinct from bl_harbert_paramaribo_nec residual.",
    "4911560", "2011-07-08", "2011", "5.852", "-55.204",
    "Early site work construction, Paramaribo, Suriname (USASpending PoP Suriname).",
    "usaspending_emr_paramaribo_esw_20110708",
    "CONSTRUCTION OF PARAMARIBO EARLY SITE WORK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F2136_1900_SAQMMA08D0010_1900/",
    "Actor: Enviro-Management & Research, Inc. (U.S./Springfield) under State — us. Official "
    "USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle930",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA11F2136_1900_SAQMMA08D0010_1900 (EMR; Paramaribo ESW). Signed 8 July 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F2136_1900_SAQMMA08D0010_1900/.",
    "USASpending: EMR Paramaribo ESW USD 4.912m. Supports emr_paramaribo_esw_4p91m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,911,560; date_signed 2011-07-08.",
)
row_doc(
    "greenway_asuncion_db_8p44m_2012",
    "infrastructure", "engineering_epc", "us",
    "Greenway Enterprises Inc. — Paraguay design/build task order",
    "Paraguay",
    "29 Sep 2012: Department of State awards task order SAQMMA12F4542 to Greenway Enterprises Inc. "
    "for IDIQ design/build; obligated USD 8,436,659.99; PoP Paraguay. CapEx face = award "
    "obligation. Distinct from falcon_asuncion_electrical_1p60m_2010.",
    "8436659.99", "2012-09-29", "2012", "-25.264", "-57.576",
    "Design/build diplomatic construction, Asunción / Paraguay (USASpending PoP Paraguay).",
    "usaspending_greenway_asuncion_db_20120929",
    "IDIQ TASK ORDER AWARD FOR DESIGN/BUILD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F4542_1900_SAQMMA08D0011_1900/",
    "Actor: Greenway Enterprises Inc. (U.S./Helena) under State — us. Official USASpending Award "
    "API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle930",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA12F4542_1900_SAQMMA08D0011_1900 (Greenway; Paraguay DB). Signed 29 September "
    "2012. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F4542_1900_SAQMMA08D0011_1900/.",
    "USASpending: Greenway Asunción DB USD 8.437m. Supports greenway_asuncion_db_8p44m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8,436,659.99; date_signed 2012-09-29.",
)
row_doc(
    "trison_georgetown_p2_5p49m_2018",
    "infrastructure", "building_materials", "us",
    "Trison Construction Inc. — Georgetown Phase II renovations",
    "Guyana",
    "26 Sep 2018: Department of State awards task order 19AQMM18F4218 to Trison Construction Inc. "
    "for Georgetown Phase II renovations; obligated USD 5,489,596.04. CapEx face = award "
    "obligation. Distinct from nika_georgetown_voltage_705k_2011 / fluid/spectrum Georgetown rows.",
    "5489596.04", "2018-09-26", "2018", "6.801", "-58.155",
    "Phase II renovations, Georgetown, Guyana (USASpending PoP Guyana).",
    "usaspending_trison_georgetown_p2_20180926",
    "BASE AWARD FOR GEORGETOWN PHASE II RENOVATIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4218_1900_SAQMMA14D0052_1900/",
    "Actor: Trison Construction Inc. (U.S./College Park) under State — us. Official USASpending "
    "Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle930",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM18F4218_1900_SAQMMA14D0052_1900 (Trison; Georgetown P2). Signed 26 September "
    "2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4218_1900_SAQMMA14D0052_1900/.",
    "USASpending: Trison Georgetown P2 USD 5.490m. Supports trison_georgetown_p2_5p49m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5,489,596.04; date_signed 2018-09-26.",
)
row_doc(
    "castries_pier_db_1p33m_2009",
    "infrastructure", "port_ownership", "other",
    "Construction and Industrial Equipment Limited — Castries DB pier / Vieux Fort pier repairs",
    "Saint Lucia",
    "29 Sep 2009: DoD awards contract N6945009C0095 to Construction and Industrial Equipment Limited "
    "for Castries design-build pier and Vieux Fort pier repairs, St. Lucia; obligated USD "
    "1,331,573. CapEx face = award obligation.",
    "1331573", "2009-09-29", "2009", "14.010", "-60.990",
    "Castries design-build pier + Vieux Fort pier repairs, Saint Lucia (USASpending PoP Saint Lucia; "
    "Castries pin).",
    "usaspending_castries_pier_db_20090929",
    "CASTRIES DESIGN BUILD PIER; VIEUX FORT PIER REPAIRS; ST. LUCIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945009C0095_9700_-NONE-_-NONE-/",
    "Actor: Construction and Industrial Equipment Limited (Castries, Saint Lucia) under DoD — other. "
    "Official USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle930",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_N6945009C0095_9700_-NONE-_-NONE- (CIE Ltd; Castries pier). Signed 29 September 2009. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945009C0095_9700_-NONE-_-NONE-/.",
    "USASpending: Castries pier DB USD 1.332m. Supports castries_pier_db_1p33m_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,331,573; date_signed 2009-09-29.",
)
row_doc(
    "sca_dominica_odm_1p69m_2020",
    "infrastructure", "building_materials", "us",
    "Strategic Consulting Alliances, LLC — Dominica Office of Disaster Management facility",
    "Dominica",
    "29 Sep 2020: DoD awards contract N6945020C0070 to Strategic Consulting Alliances, LLC for new "
    "Office of Disaster Management (ODM) facility, Dominica; obligated USD 1,692,048.19. CapEx face "
    "= award obligation.",
    "1692048.19", "2020-09-29", "2020", "15.301", "-61.388",
    "New Office of Disaster Management facility, Dominica (USASpending PoP Dominica; Roseau pin).",
    "usaspending_sca_dominica_odm_20200929",
    "NEW OFFICE OF DISASTER MANAGEMENT (ODM)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945020C0070_9700_-NONE-_-NONE-/",
    "Actor: Strategic Consulting Alliances, LLC (U.S./Crisfield) under DoD — us. Official "
    "USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle930",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_N6945020C0070_9700_-NONE-_-NONE- (SCA; Dominica ODM). Signed 29 September 2020. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945020C0070_9700_-NONE-_-NONE-/.",
    "USASpending: SCA Dominica ODM USD 1.692m. Supports sca_dominica_odm_1p69m_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,692,048.19; date_signed 2020-09-29.",
)

# === 931 ===
row_doc(
    "baker_tandil_f16_ae_8p25m_2025",
    "infrastructure", "engineering_epc", "us",
    "Baker-Stanley-Cardno JV — F-16 FAA beddown Title I AE (Tandil AB)",
    "Argentina",
    "7 Dec 2025: USAF awards task order FA890326F0016 to Baker-Stanley-Cardno JV for Title I / "
    "design services for the F-16 FAA beddown program at Argentina Air Force Tandil AB; obligated "
    "USD 8,253,528.48. CapEx face = award obligation.",
    "8253528.48", "2025-12-07", "2025", "-37.237", "-59.228",
    "F-16 FAA beddown Title I AE, Tandil Air Base, Argentina (USASpending PoP Argentina; Tandil pin).",
    "usaspending_baker_tandil_f16_ae_20251207",
    "TITLE I / DESIGN SERVICES FOR THE F-16 FAA BEDDOWN PROGRAM ARGENTINA AIR FORCE TANDIL AB - AE "
    "NEXT POOL 4 TASK ORDER TITLE I ARCHITECT-ENGINEERING (A- E)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA890326F0016_9700_FA890321D0004_9700/",
    "Actor: Baker-Stanley-Cardno JV (U.S./Moon Township) under DoD/USAF — us. Official USASpending "
    "Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle931",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_FA890326F0016_9700_FA890321D0004_9700 (Baker-Stanley-Cardno; Tandil AE). Signed 7 "
    "December 2025. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA890326F0016_9700_FA890321D0004_9700/.",
    "USASpending: Baker Tandil F-16 AE USD 8.254m. Supports baker_tandil_f16_ae_8p25m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8,253,528.48; date_signed 2025-12-07.",
)
row_doc(
    "vistas_brasilia_db_6p96m_2012",
    "infrastructure", "building_materials", "us",
    "The Vistas Group Global Inc. — Brasília design-build construction",
    "Brazil",
    "7 Jun 2012: Department of State awards task order SAQMMA12F1973 to The Vistas Group Global Inc. "
    "for design-build construction services — Brasília; obligated USD 6,964,944. CapEx face = "
    "award obligation. Distinct from beltsville_brasilia_psu / studio_gang_brasilia_nec_design / "
    "markon_brasilia_nec_eng.",
    "6964944", "2012-06-07", "2012", "-15.797", "-47.892",
    "Design-build construction services, Brasília, Brazil (USASpending PoP Brazil).",
    "usaspending_vistas_brasilia_db_20120607",
    "DESIGN-BUILD CONSTRUCTION SERVICES - BRASILIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1973_1900_SAQMMA08D0006_1900/",
    "Actor: The Vistas Group Global Inc. (U.S./Chicago) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle931",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA12F1973_1900_SAQMMA08D0006_1900 (Vistas; Brasília DB). Signed 7 June 2012. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1973_1900_SAQMMA08D0006_1900/.",
    "USASpending: Vistas Brasília DB USD 6.965m. Supports vistas_brasilia_db_6p96m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6,964,944; date_signed 2012-06-07.",
)
row_doc(
    "tidewater_sao_paulo_canopy_4p44m_2023",
    "infrastructure", "building_materials", "us",
    "Tidewater, Inc. — São Paulo consular canopy and waiting area improvements",
    "Brazil",
    "15 Sep 2023: Department of State awards task order 19AQMM23F2799 to Tidewater, Inc. for "
    "design-build consular affairs canopy and waiting area improvements — São Paulo, Brazil; "
    "obligated USD 4,437,260. CapEx face = award obligation. Distinct from "
    "tidewater_managua_consular_6p27m_2025.",
    "4437260", "2023-09-15", "2023", "-23.551", "-46.633",
    "Consular canopy / waiting area, São Paulo, Brazil (USASpending PoP Brazil; São Paulo pin).",
    "usaspending_tidewater_sao_paulo_canopy_20230915",
    "DESIGN-BUILD CONSTRUCTION SERVICES FOR CONSULAR AFFAIRS CANOPY AND WAITING AREA IMPROVEMENTS - "
    "SAO PAULO, BRAZIL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2799_1900_19AQMM22D0058_1900/",
    "Actor: Tidewater, Inc. (U.S./Elkridge) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle931",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM23F2799_1900_19AQMM22D0058_1900 (Tidewater; São Paulo canopy). Signed 15 "
    "September 2023. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2799_1900_19AQMM22D0058_1900/.",
    "USASpending: Tidewater São Paulo canopy USD 4.438m. Supports tidewater_sao_paulo_canopy_4p44m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,437,260; date_signed 2023-09-15.",
)
row_doc(
    "desbuild_powell_plaza_5p22m_2018",
    "infrastructure", "building_materials", "us",
    "Desbuild Incorporated — Kingston Powell Plaza 9th floor renovation",
    "Jamaica",
    "27 Sep 2018: Department of State awards task order 19AQMM18F4853 to Desbuild Incorporated for "
    "Kingston, Jamaica Powell Plaza 9th floor renovation; obligated USD 5,223,405.11. CapEx face = "
    "award obligation. Distinct from tabcon_kingston_nec_roof_6p02m_2024 / desbuild_belize_msgr.",
    "5223405.11", "2018-09-27", "2018", "18.018", "-76.810",
    "Powell Plaza 9th floor renovation, Kingston, Jamaica (USASpending PoP Jamaica).",
    "usaspending_desbuild_powell_plaza_20180927",
    "KINGSTON, JAMAICA POWELL PLAZA 9TH FLOOR RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4853_1900_SAQMMA14D0063_1900/",
    "Actor: Desbuild Incorporated (U.S./Hyattsville) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle931",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM18F4853_1900_SAQMMA14D0063_1900 (Desbuild; Powell Plaza). Signed 27 September "
    "2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4853_1900_SAQMMA14D0063_1900/.",
    "USASpending: Desbuild Powell Plaza USD 5.223m. Supports desbuild_powell_plaza_5p22m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5,223,405.11; date_signed 2018-09-27.",
)
row_doc(
    "ped_jamaica_boat_facility_2p53m_2023",
    "infrastructure", "building_materials", "us",
    "PED Concepts Inc. — Jamaica boat maintenance facility",
    "Jamaica",
    "30 Jun 2023: DoD awards contract N6945023C0016 to PED Concepts Inc. for Jamaica boat "
    "maintenance facility; obligated USD 2,526,950. CapEx face = award obligation. Distinct from "
    "ped_concepts_antigua_trinidad_2p69m_2026.",
    "2526950", "2023-06-30", "2023", "17.971", "-76.793",
    "Boat maintenance facility, Jamaica (USASpending PoP Jamaica; Kingston-area pin).",
    "usaspending_ped_jamaica_boat_20230630",
    "JAMAICA BOAT MAINTENANCE FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945023C0016_9700_-NONE-_-NONE-/",
    "Actor: PED Concepts Inc. (U.S./Jacksonville) under DoD — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle931",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_N6945023C0016_9700_-NONE-_-NONE- (PED; Jamaica boat facility). Signed 30 June 2023. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945023C0016_9700_-NONE-_-NONE-/.",
    "USASpending: PED Jamaica boat facility USD 2.527m. Supports ped_jamaica_boat_facility_2p53m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,526,950; date_signed 2023-06-30.",
)

# === 932 ===
row_doc(
    "edifice_montevideo_msgr_3p63m_2018",
    "infrastructure", "building_materials", "us",
    "Edifice Worldwide LLC — Montevideo MSGR improvements",
    "Uruguay",
    "28 Sep 2018: Department of State awards task order 19AQMM18F4455 to Edifice Worldwide LLC for "
    "Montevideo, Uruguay Marine Security Guard Residence improvements; obligated USD 3,626,199.34. "
    "CapEx face = award obligation. Distinct from cts_montevideo_psu_2p10m_2011.",
    "3626199.34", "2018-09-28", "2018", "-34.901", "-56.164",
    "MSGR improvements, Montevideo, Uruguay (USASpending PoP Uruguay).",
    "usaspending_edifice_montevideo_msgr_20180928",
    "MONTEVIDEO, URUGUAY MARINE SECURITY GUARD RESIDENCE IMPROVEMENTS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4455_1900_SAQMMA14D0048_1900/",
    "Actor: Edifice Worldwide LLC (U.S./Beltsville) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle932",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM18F4455_1900_SAQMMA14D0048_1900 (Edifice; Montevideo MSGR). Signed 28 September "
    "2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4455_1900_SAQMMA14D0048_1900/.",
    "USASpending: Edifice Montevideo MSGR USD 3.626m. Supports edifice_montevideo_msgr_3p63m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,626,199.34; date_signed 2018-09-28.",
)
row_doc(
    "hardline_lapaz_febr_1p77m_2016",
    "infrastructure", "building_materials", "us",
    "Hardline Nati Construction LLC — La Paz FEBR door/window/elevation repair",
    "Bolivia",
    "28 Sep 2016: Department of State awards task order SAQMMA16F4874 to Hardline Nati Construction "
    "LLC for FEBR door, window, and elevation repair and replacement at U.S. Embassy La Paz; "
    "obligated USD 1,769,879.10. CapEx face = award obligation. Distinct from "
    "amentum_lapaz_power_plant_10m_2023.",
    "1769879.10", "2016-09-28", "2016", "-16.500", "-68.150",
    "FEBR repair/replacement, U.S. Embassy La Paz, Bolivia (USASpending PoP Bolivia).",
    "usaspending_hardline_lapaz_febr_20160928",
    "IGF::OT::IGF  FEBR DOOR, WINDOW, AND ELEVATION REPAIR AND REPLACEMENT AT US EMBASSY LA PAZ.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F4874_1900_SAQMMA14D0085_1900/",
    "Actor: Hardline Nati Construction LLC (U.S./College Park) under State — us. Official "
    "USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle932",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA16F4874_1900_SAQMMA14D0085_1900 (Hardline; La Paz FEBR). Signed 28 September "
    "2016. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F4874_1900_SAQMMA14D0085_1900/.",
    "USASpending: Hardline La Paz FEBR USD 1.770m. Supports hardline_lapaz_febr_1p77m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,769,879.10; date_signed 2016-09-28.",
)
row_doc(
    "comp_roof_lapaz_1p01m_2015",
    "infrastructure", "building_materials", "us",
    "Competition Roofing Inc. — La Paz chancery roof replacement",
    "Bolivia",
    "15 Jul 2015: Department of State awards task order SAQMMA15F1983 to Competition Roofing Inc. "
    "for La Paz, Bolivia chancery roof replacement project; obligated USD 1,011,500.05. CapEx face "
    "= award obligation. Distinct from hardline_lapaz_febr_1p77m_2016 / amentum_lapaz_power.",
    "1011500.05", "2015-07-15", "2015", "-16.500", "-68.150",
    "Chancery roof replacement, La Paz, Bolivia (USASpending PoP Bolivia).",
    "usaspending_comp_roof_lapaz_20150715",
    "LA PAZ, BOLIVIA CHANCERY ROOF REPLACEMENT PROJECT. IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1983_1900_SAQMMA13D0127_1900/",
    "Actor: Competition Roofing Inc. (U.S./Houston) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle932",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA15F1983_1900_SAQMMA13D0127_1900 (Competition Roofing; La Paz). Signed 15 July "
    "2015. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1983_1900_SAQMMA13D0127_1900/.",
    "USASpending: Competition Roofing La Paz USD 1.012m. Supports comp_roof_lapaz_1p01m_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,011,500.05; date_signed 2015-07-15.",
)
row_doc(
    "bonatti_panama_pier_4p64m_2022",
    "infrastructure", "port_ownership", "other",
    "Bonatti Ingenieros y Arquitectos — Panama City pier renovation (FMS design/build)",
    "Panama",
    "18 Aug 2022: USACE awards task order W9127822F0257 to Bonatti Ingenieros y Arquitectos Sociedad "
    "Anónima for D/B pier renovation (FMS), Panama City, Panama; obligated USD 4,636,168.95. CapEx "
    "face = award obligation. Distinct from bonatti_hunting_caye / bonatti_san_pedro Belize rows.",
    "4636168.95", "2022-08-18", "2022", "8.982", "-79.520",
    "Pier renovation (FMS), Panama City, Panama (USASpending PoP Panama).",
    "usaspending_bonatti_panama_pier_20220818",
    "D/B PIER RENOVATION (FMS), PANAMA CITY, PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0257_9700_W9127821D0076_9700/",
    "Actor: Bonatti Ingenieros y Arquitectos S.A. (Guatemala) under DoD/USACE — other. Official "
    "USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle932",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127822F0257_9700_W9127821D0076_9700 (Bonatti; Panama pier). Signed 18 August 2022. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0257_9700_W9127821D0076_9700/.",
    "USASpending: Bonatti Panama pier USD 4.636m. Supports bonatti_panama_pier_4p64m_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,636,168.95; date_signed 2022-08-18.",
)
row_doc(
    "neals_belmopan_fire_849k_2018",
    "infrastructure", "building_materials", "us",
    "Neal's Construction, LLC — Belmopan fire station construction",
    "Belize",
    "26 Sep 2018: DoD awards contract W912CL18C0003 to Neal's Construction, LLC for construction of "
    "fire station in Belmopan, Belize; obligated USD 849,418.23. CapEx face = award obligation. "
    "Distinct from desbuild_belize_msgr_14m_2015 / chugach_belmopan_hvac.",
    "849418.23", "2018-09-26", "2018", "17.251", "-88.759",
    "Fire station construction, Belmopan, Belize (USASpending PoP Belize).",
    "usaspending_neals_belmopan_fire_20180926",
    "CONSTRUCTION FIRE STATION IN BELMOPAN, BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL18C0003_9700_-NONE-_-NONE-/",
    "Actor: Neal's Construction, LLC (U.S./Beaufort) under DoD — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle932",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W912CL18C0003_9700_-NONE-_-NONE- (Neal's; Belmopan fire). Signed 26 September 2018. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL18C0003_9700_-NONE-_-NONE-/.",
    "USASpending: Neal's Belmopan fire station USD 0.849m. Supports neals_belmopan_fire_849k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 849,418.23; date_signed 2018-09-26.",
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
    print(f"cycles930-932 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
