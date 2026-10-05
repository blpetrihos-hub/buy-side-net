#!/usr/bin/env python3
"""Cycles 917–919: USASpending Caribbean US CapEx (Suriname/Jamaica/DR/Guyana/Barbados).

Seeds: 20261917–20261919. Thin top-up dry.
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
    rid,
    layer,
    sub,
    side,
    counterpart,
    country,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    sid,
    quote,
    url,
    note,
    hunt,
    chicago,
    annotation,
    evid_note,
    investment_type="epc",
):
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": sub,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": investment_type,
            "value": value,
            "currency": "USD",
            "value_usd": value,
            "fx_usd": "1",
            "fx_date": fx_date,
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": "documented",
            "source_id": sid,
            "note": note,
            "pair_id": "",
            "counterpart_side": "",
            "counterpart_actor": "",
            "counterpart_value": "",
            "counterpart_currency": "",
            "counterpart_value_usd": "",
            "gap": "",
        },
        {
            "id": rid,
            "retrieved": "2026-10-05",
            "source_id": sid,
            "url": url,
            "price_year": year,
            "evidence": "documented",
            "quote": quote,
            "note": evid_note,
        },
        {
            "id": sid,
            "type": "government",
            "chicago": chicago,
            "url": url,
            "accessed": "2026-10-05",
            "annotation": annotation,
            "supports": [rid, hunt],
        },
    )


# === Cycle 917 ===
row_doc(
    "bl_harbert_paramaribo_nec_121m_2013",
    "infrastructure", "engineering_epc", "us",
    "BL Harbert International LLC — New Embassy Compound Paramaribo (design-bid-build)",
    "Suriname",
    "28 Sep 2013: Department of State awards contract SAQMMA13C0248 to BL Harbert International "
    "LLC for design-bid-build construction services for the New Embassy Compound in Paramaribo, "
    "Suriname; obligated USD 121,193,179.90. CapEx face = award obligation. Distinct from "
    "caddell_port_of_spain_nec_2024 / caddell_santo_domingo_nec_2010.",
    "121193179.90", "2013-09-28", "2013", "5.826", "-55.167",
    "New Embassy Compound, Paramaribo, Suriname (award description; Paramaribo pin).",
    "usaspending_bl_harbert_paramaribo_nec_20130928",
    "DESIGN-BID-BUILD, CONSTRUCTION SERVICES FOR THE NEW EMBASSY COMPOUND IN PARAMARIBO, SURINAME",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13C0248_1900_-NONE-_-NONE-/",
    "Actor: BL Harbert International LLC (U.S.) under State OBO — us. Official USASpending Award "
    "API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx; Suriname under-covered.",
    "hunt_cycle917",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13C0248_1900_-NONE-_-NONE- "
    "(BL Harbert; Paramaribo NEC). Signed 28 September 2013. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13C0248_1900_-NONE-_-NONE-/.",
    "USASpending: BL Harbert Paramaribo NEC USD 121.193m. Supports bl_harbert_paramaribo_nec_121m_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 121,193,179.90; date_signed 2013-09-28.",
)
row_doc(
    "yates_desbuild_kingston_nox_83m_2005",
    "infrastructure", "engineering_epc", "us",
    "Yates Desbuild Joint Venture — USAID Annex Building (NOX) Kingston",
    "Jamaica",
    "28 Sep 2005: Department of State awards contract SALMEC05C0039 to Yates Desbuild Joint "
    "Venture for New USAID Annex Building (NOX) in Kingston, Jamaica; obligated USD 83,048,978.88. "
    "CapEx face = award obligation. Distinct from desbuild_kingston_nox_12p9m_2005 (related "
    "Desbuild package).",
    "83048978.88", "2005-09-28", "2005", "18.017", "-76.810",
    "USAID Annex Building (NOX), Kingston, Jamaica (award description; Kingston pin). "
    "USASpending PoP field miscodes India — country coded Jamaica per description.",
    "usaspending_yates_desbuild_kingston_nox_20050928",
    "NEW USAID ANNEX BUILDING (NOX) KINGSTON, JAMAICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC05C0039_1900_-NONE-_-NONE-/",
    "Actor: Yates Desbuild JV (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx; Jamaica under-covered.",
    "hunt_cycle917",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SALMEC05C0039_1900_-NONE-_-NONE- "
    "(Yates Desbuild JV; Kingston USAID NOX). Signed 28 September 2005. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC05C0039_1900_-NONE-_-NONE-/.",
    "USASpending: Yates Desbuild Kingston NOX USD 83.049m. Supports yates_desbuild_kingston_nox_83m_2005.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 83,048,978.88; date_signed 2005-09-28.",
)
row_doc(
    "desbuild_kingston_nox_12p9m_2005",
    "infrastructure", "engineering_epc", "us",
    "Desbuild Incorporated — USAID Annex Building (NOX) Kingston",
    "Jamaica",
    "7 Sep 2005: Department of State awards contract SALMEC05C0029 to Desbuild Incorporated for "
    "New USAID Annex Building (NOX) in Kingston, Jamaica; obligated USD 12,904,610.42. CapEx face "
    "= award obligation. Distinct from yates_desbuild_kingston_nox_83m_2005.",
    "12904610.42", "2005-09-07", "2005", "18.017", "-76.810",
    "USAID Annex Building (NOX), Kingston, Jamaica (USASpending PoP Jamaica; Kingston pin).",
    "usaspending_desbuild_kingston_nox_20050907",
    "NEW USAID ANNEX BUILDING (NOX) KINGSTON, JAMAICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC05C0029_1900_-NONE-_-NONE-/",
    "Actor: Desbuild Incorporated (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle917",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SALMEC05C0029_1900_-NONE-_-NONE- "
    "(Desbuild; Kingston USAID NOX). Signed 7 September 2005. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC05C0029_1900_-NONE-_-NONE-/.",
    "USASpending: Desbuild Kingston NOX USD 12.905m. Supports desbuild_kingston_nox_12p9m_2005.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12,904,610.42; date_signed 2005-09-07.",
)
row_doc(
    "eg_designbuild_santo_domingo_qflow_3p35m_2023",
    "infrastructure", "engineering_epc", "us",
    "EG Designbuild, L.L.C. — Embassy Santo Domingo Q-Flow system replacement",
    "Dominican Republic",
    "18 Sep 2023: Department of State awards task order 19AQMM23F2535 to EG Designbuild, L.L.C. "
    "for total design and construction to replace the Q-Flow system at the Embassy in Santo "
    "Domingo, Dominican Republic; obligated USD 3,346,360.00. CapEx face = award obligation. "
    "Distinct from caddell_santo_domingo_nec_2010.",
    "3346360.00", "2023-09-18", "2023", "18.467", "-69.932",
    "U.S. Embassy Santo Domingo Q-Flow replacement, Dominican Republic (USASpending PoP Dominican Republic).",
    "usaspending_eg_qflow_santo_domingo_20230918",
    "TOTAL DESIGN AND CONSTRUCTION TO REPLACE THE Q-FLOW SYSTEM AT THE EMBASSY IN SANTO DOMINGO, "
    "DOMINICAN REPUBLIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2535_1900_19AQMM22D0056_1900/",
    "Actor: EG Designbuild, L.L.C. (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle917",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM23F2535_1900_19AQMM22D0056_1900 (EG Designbuild; Santo Domingo Q-Flow). Signed "
    "18 September 2023. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2535_1900_19AQMM22D0056_1900/.",
    "USASpending: EG Designbuild Santo Domingo Q-Flow USD 3.346m. Supports eg_designbuild_santo_domingo_qflow_3p35m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,346,360.00; date_signed 2023-09-18.",
)
row_doc(
    "akea_dominican_dormitory_1p87m_2012",
    "infrastructure", "building_materials", "us",
    "Akea, Inc. — dormitory building construction (Dominican Republic)",
    "Dominican Republic",
    "28 Sep 2012: DoD awards contract N6945012C0064 to Akea, Inc. to construct a dormitory "
    "building in the Dominican Republic; obligated USD 1,871,905.53. CapEx face = award "
    "obligation. Distinct from eg_designbuild_santo_domingo_qflow_3p35m_2023.",
    "1871905.53", "2012-09-28", "2012", "18.467", "-69.932",
    "Dormitory building, Dominican Republic (USASpending PoP Dominican Republic; Santo Domingo approximate).",
    "usaspending_akea_dominican_dorm_20120928",
    "CONSTRUCT DORMITORY BUILDING IN DOMINICAN REPUBLIC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945012C0064_9700_-NONE-_-NONE-/",
    "Actor: Akea, Inc. (U.S.) under DoD — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle917",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N6945012C0064_9700_-NONE-_-NONE- "
    "(Akea; Dominican dormitory). Signed 28 September 2012. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945012C0064_9700_-NONE-_-NONE-/.",
    "USASpending: Akea Dominican dormitory USD 1.872m. Supports akea_dominican_dormitory_1p87m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,871,905.53; date_signed 2012-09-28.",
)

# === Cycle 918 ===
row_doc(
    "eeii_mahdia_eoc_drw_2p42m_2023",
    "infrastructure", "building_materials", "other",
    "EEII S.A.S. — Mahdia EOC / Disaster Relief Warehouse (Guyana)",
    "Guyana",
    "28 Sep 2023: DoD awards task order W9127823F0467 to Estudios Edificaciones e Interventorias "
    "en Ingenieria EEII S.A.S. (Colombia) for construction of the Emergency Operations Center / "
    "Disaster Relief Warehouse in Mahdia, Guyana; obligated USD 2,421,282.30. CapEx face = award "
    "obligation.",
    "2421282.30", "2023-09-28", "2023", "5.267", "-59.150",
    "EOC / DRW, Mahdia, Guyana (USASpending PoP Guyana; Mahdia pin).",
    "usaspending_eeii_mahdia_eoc_20230928",
    "CONSTRUCTION OF THE EMERGENCY OPERATIONS CENTER/DISASTER RELIEF WAREHOUSE IN MAHDIA, GUYANA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0467_9700_W9127823D0058_9700/",
    "Actor: EEII S.A.S. (Colombia HQ) under DoD — other. Official USASpending Award API. Shuffle "
    "building_materials; Guyana under-covered.",
    "hunt_cycle918",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127823F0467_9700_W9127823D0058_9700 (EEII; Mahdia EOC/DRW). Signed 28 September "
    "2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127823F0467_9700_W9127823D0058_9700/.",
    "USASpending: EEII Mahdia EOC/DRW USD 2.421m. Supports eeii_mahdia_eoc_drw_2p42m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,421,282.30; recipient Colombia.",
)
row_doc(
    "tidewater_georgetown_fire_2p30m_2016",
    "infrastructure", "building_materials", "us",
    "Tidewater, Inc. — fire protection system at U.S. government warehouse Georgetown",
    "Guyana",
    "29 Sep 2016: Department of State awards task order SAQMMA16F5504 to Tidewater, Inc. for fire "
    "protection system installation at U.S. government warehouse in Georgetown, Guyana; obligated "
    "USD 2,304,523.21. CapEx face = award obligation.",
    "2304523.21", "2016-09-29", "2016", "6.801", "-58.155",
    "U.S. government warehouse fire protection, Georgetown, Guyana (USASpending PoP Guyana).",
    "usaspending_tidewater_georgetown_fire_20160929",
    "TASK ORDER FOR FIRE PROTECTION SYSTEM INSTALLATION AT U.S. GOVERNMENT WAREHOUSE IN GEORGETOWN, "
    "GUYANA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5504_1900_SAQMMA14D0045_1900/",
    "Actor: Tidewater, Inc. (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle918",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA16F5504_1900_SAQMMA14D0045_1900 (Tidewater; Georgetown fire protection). Signed "
    "29 September 2016. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5504_1900_SAQMMA14D0045_1900/.",
    "USASpending: Tidewater Georgetown fire USD 2.305m. Supports tidewater_georgetown_fire_2p30m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,304,523.21; date_signed 2016-09-29.",
)
row_doc(
    "fluid_solutions_georgetown_water_1p33m_2023",
    "resources", "water", "us",
    "Fluid Solutions LLC — Embassy Georgetown potable water treatment upgrades (D/B)",
    "Guyana",
    "28 Sep 2023: Department of State awards task order 19GE5023F0658 to Fluid Solutions LLC for "
    "design-build potable water treatment system upgrades at U.S. Embassy Georgetown, Guyana; "
    "obligated USD 1,332,382.03. CapEx face = award obligation.",
    "1332382.03", "2023-09-28", "2023", "6.801", "-58.155",
    "U.S. Embassy Georgetown potable water treatment upgrades, Guyana (USASpending PoP Guyana).",
    "usaspending_fluid_georgetown_water_20230928",
    "D/B POTABLE WATER TREATMENT SYSTEM UPGRADES PROJECT,  U.S. EMBASSY GEORGETOWN, GUYANA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023F0658_1900_19GE5023D0048_1900/",
    "Actor: Fluid Solutions LLC (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle918",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19GE5023F0658_1900_19GE5023D0048_1900 (Fluid Solutions; Georgetown water). Signed 28 "
    "September 2023. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023F0658_1900_19GE5023D0048_1900/.",
    "USASpending: Fluid Solutions Georgetown water USD 1.332m. Supports fluid_solutions_georgetown_water_1p33m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,332,382.03; date_signed 2023-09-28.",
)
row_doc(
    "krueck_sexton_georgetown_design_1p13m_2024",
    "infrastructure", "engineering_epc", "us",
    "Krueck & Sexton Architects, Ltd. — project development and design (Georgetown)",
    "Guyana",
    "24 Sep 2024: Department of State awards task order 19AQMM24F2387 to Krueck & Sexton "
    "Architects, Ltd. for project development and design services in Georgetown, Guyana; "
    "obligated USD 1,130,558.87. CapEx face = award obligation.",
    "1130558.87", "2024-09-24", "2024", "6.801", "-58.155",
    "U.S. facilities design services, Georgetown, Guyana (USASpending PoP Guyana).",
    "usaspending_krueck_georgetown_design_20240924",
    "PROJECT DEVELOPMENT AND DESIGN SERVICES IN GEORGETOWN, GUYANA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2387_1900_19AQMM19D0063_1900/",
    "Actor: Krueck & Sexton Architects, Ltd. (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle918",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM24F2387_1900_19AQMM19D0063_1900 (Krueck & Sexton; Georgetown design). Signed 24 "
    "September 2024. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2387_1900_19AQMM19D0063_1900/.",
    "USASpending: Krueck & Sexton Georgetown design USD 1.131m. Supports krueck_sexton_georgetown_design_1p13m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,130,558.87; date_signed 2024-09-24.",
)
row_doc(
    "spectrum_georgetown_pcc_generator_738k_2022",
    "energy", "power_plants_grid", "us",
    "Spectrum Electrical Services, Inc. — PCC generator / ATS / AVR replacement (Georgetown)",
    "Guyana",
    "19 Apr 2022: Department of State awards task order 19AQMM22F1586 to Spectrum Electrical "
    "Services, Inc. to replace PCC generator set, automatic transfer switch, and install new PCC "
    "automatic voltage regulator at U.S. facilities in Georgetown, Guyana; obligated USD 738,156.20. "
    "CapEx face = award obligation. Distinct from spectrum_haiti_switchgear_7p02m_2021.",
    "738156.20", "2022-04-19", "2022", "6.801", "-58.155",
    "PCC generator / ATS / AVR, Georgetown, Guyana (USASpending PoP Guyana).",
    "usaspending_spectrum_georgetown_generator_20220419",
    "REPLACE PCC GENERATOR SET, AUTOMATIC TRANSFER SWITCH, INSTALL NEW PCC AUTOMATIC VOLTAGE "
    "REGULATOR AN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1586_1900_19AQMM18D0072_1900/",
    "Actor: Spectrum Electrical Services, Inc. (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle918",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM22F1586_1900_19AQMM18D0072_1900 (Spectrum; Georgetown PCC generator). Signed 19 "
    "April 2022. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1586_1900_19AQMM18D0072_1900/.",
    "USASpending: Spectrum Georgetown PCC generator USD 0.738m. Supports spectrum_georgetown_pcc_generator_738k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 738,156.20; date_signed 2022-04-19.",
)

# === Cycle 919 ===
row_doc(
    "palgag_barbados_nrl_7p69m_2015",
    "infrastructure", "building_materials", "allied",
    "Palgag Building Technologies Ltd — National Reference Laboratory Bridgetown",
    "Barbados",
    "6 Mar 2015: Department of State awards contract SWHARC15C0003 to Palgag Building Technologies "
    "Ltd (Israel) for construction of a National Reference Laboratory in Bridgetown, Barbados; "
    "obligated USD 7,686,676.11. CapEx face = award obligation. Distinct from "
    "palgag_gonaives_clusters_3p55m_2011.",
    "7686676.11", "2015-03-06", "2015", "13.097", "-59.615",
    "National Reference Laboratory, Bridgetown, Barbados (USASpending PoP Barbados).",
    "usaspending_palgag_barbados_nrl_20150306",
    "CONSTRUCTION OF A NATIONAL REFERENCE LABORATORY IN BRIDGETOWN, BARBADOS, CONSTRUCTION "
    "CONSIDERED OTH",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15C0003_1900_-NONE-_-NONE-/",
    "Actor: Palgag Building Technologies Ltd (Israel) under State — allied. Official USASpending "
    "Award API. Shuffle building_materials; Barbados under-covered.",
    "hunt_cycle919",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC15C0003_1900_-NONE-_-NONE- "
    "(Palgag; Bridgetown NRL). Signed 6 March 2015. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC15C0003_1900_-NONE-_-NONE-/.",
    "USASpending: Palgag Barbados NRL USD 7.687m. Supports palgag_barbados_nrl_7p69m_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7,686,676.11; recipient Israel.",
)
row_doc(
    "framaco_barbados_renewable_4p45m_2021",
    "energy", "other_renewables", "us",
    "Framaco-Bozdemir JV LLC — Embassy Bridgetown design-build renewable energy installation",
    "Barbados",
    "24 Sep 2021: Department of State awards contract 19GE5021C0053 to Framaco-Bozdemir Joint "
    "Venture LLC for design-build renewable energy installation at U.S. facilities in Barbados; "
    "obligated USD 4,452,016.47. CapEx face = award obligation.",
    "4452016.47", "2021-09-24", "2021", "13.097", "-59.615",
    "U.S. Embassy Bridgetown renewable energy installation, Barbados (USASpending PoP Barbados).",
    "usaspending_framaco_barbados_re_20210924",
    "DESIGN BUILD RENEWABLE ENERGY INSTALLATION SOLICITATION                                PROJECT. "
    "U.S.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0053_1900_-NONE-_-NONE-/",
    "Actor: Framaco-Bozdemir JV LLC (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle other_renewables; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle919",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5021C0053_1900_-NONE-_-NONE- "
    "(Framaco-Bozdemir; Bridgetown renewable). Signed 24 September 2021. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021C0053_1900_-NONE-_-NONE-/.",
    "USASpending: Framaco Barbados renewable USD 4.452m. Supports framaco_barbados_renewable_4p45m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,452,016.47; date_signed 2021-09-24.",
)
row_doc(
    "qmax_bridgetown_roof_2p81m_2023",
    "infrastructure", "building_materials", "us",
    "Q-Max Construction Company, Inc. — Bridgetown Embassy roof replacement",
    "Barbados",
    "26 Sep 2023: Department of State awards task order 19AQMM23F3253 to Q-Max Construction "
    "Company, Inc. for Bridgetown, Barbados roof replacement project; obligated USD 2,814,004.98. "
    "CapEx face = award obligation.",
    "2814004.98", "2023-09-26", "2023", "13.097", "-59.615",
    "U.S. Embassy Bridgetown roof replacement, Barbados (USASpending PoP Barbados).",
    "usaspending_qmax_bridgetown_roof_20230926",
    "BRIDGETOWN, BARBADOS ROOF REPLACEMENT PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F3253_1900_19AQMM19D0083_1900/",
    "Actor: Q-Max Construction Company, Inc. (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle919",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM23F3253_1900_19AQMM19D0083_1900 (Q-Max; Bridgetown roof). Signed 26 September "
    "2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F3253_1900_19AQMM19D0083_1900/.",
    "USASpending: Q-Max Bridgetown roof USD 2.814m. Supports qmax_bridgetown_roof_2p81m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,814,004.98; date_signed 2023-09-26.",
)
row_doc(
    "horizon_bridgetown_hvac_1p56m_2016",
    "infrastructure", "building_materials", "us",
    "Horizon Construction Group / ICS JV — Embassy Bridgetown PCC HVAC upgrade",
    "Barbados",
    "28 Sep 2016: Department of State awards task order SAQMMA16F5171 to Horizon Construction "
    "Group\\International Construction Services JV, LLC for PCC HVAC upgrade at U.S. Embassy "
    "Bridgetown, Barbados; obligated USD 1,556,802.00. CapEx face = award obligation.",
    "1556802.00", "2016-09-28", "2016", "13.097", "-59.615",
    "U.S. Embassy Bridgetown PCC HVAC upgrade, Barbados (USASpending PoP Barbados).",
    "usaspending_horizon_bridgetown_hvac_20160928",
    "PCC HVAC UPGRADE AT THE U.S EMBASSY IN BRIDGETOWN, BARBADOS. IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5171_1900_SAQMMA14D0056_1900/",
    "Actor: Horizon/ICS JV (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle919",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA16F5171_1900_SAQMMA14D0056_1900 (Horizon/ICS; Bridgetown HVAC). Signed 28 "
    "September 2016. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5171_1900_SAQMMA14D0056_1900/.",
    "USASpending: Horizon Bridgetown HVAC USD 1.557m. Supports horizon_bridgetown_hvac_1p56m_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,556,802.00; date_signed 2016-09-28.",
)
row_doc(
    "epik_bridgetown_water_1p42m_2024",
    "resources", "water", "us",
    "EPIK-Aquashine JV LLC — Embassy Bridgetown potable water treatment upgrades (D/B)",
    "Barbados",
    "19 Apr 2024: Department of State awards task order 19GE5024F0277 to EPIK-Aquashine JV LLC "
    "for design/build potable water treatment system upgrades at U.S. Embassy Bridgetown, Barbados; "
    "obligated USD 1,419,457.00. CapEx face = award obligation. Distinct from "
    "fluid_solutions_georgetown_water_1p33m_2023.",
    "1419457.00", "2024-04-19", "2024", "13.097", "-59.615",
    "U.S. Embassy Bridgetown potable water treatment upgrades, Barbados (USASpending PoP Barbados).",
    "usaspending_epik_bridgetown_water_20240419",
    "DESIGN/BUILD CONSTRUCTION SERVICES - POTABLE WATER TREATMENT SYSTEM UPGRADES, U.S. EMBASSY "
    "BRIDGETOW",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024F0277_1900_19GE5023D0049_1900/",
    "Actor: EPIK-Aquashine JV LLC (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "water; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle919",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19GE5024F0277_1900_19GE5023D0049_1900 (EPIK-Aquashine; Bridgetown water). Signed 19 "
    "April 2024. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024F0277_1900_19GE5023D0049_1900/.",
    "USASpending: EPIK Bridgetown water USD 1.419m. Supports epik_bridgetown_water_1p42m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,419,457.00; date_signed 2024-04-19.",
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
    added: list[str] = []

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
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_entry)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"cycles917-919 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
