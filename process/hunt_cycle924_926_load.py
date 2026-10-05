#!/usr/bin/env python3
"""Cycles 924–926: USASpending Southern Cone / Mexico residual CapEx.

Seeds: 20261924–20261926. Thin top-up dry.
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


# === 924 ===
row_doc(
    "cts_montevideo_psu_2p10m_2011",
    "infrastructure", "building_materials", "us",
    "CTS-Hardline, LLC — Embassy Montevideo Phase II/III physical security upgrade",
    "Uruguay",
    "30 Sep 2011: Department of State awards task order SAQMMA11F4745 to CTS-Hardline, LLC for "
    "Phase II/III physical security upgrade (PSU) at U.S. Embassy Montevideo, Uruguay; obligated "
    "USD 2,098,770.92. CapEx face = award obligation. Distinct from perini_montevideo_chancery_2017.",
    "2098770.92", "2011-09-30", "2011", "-34.901", "-56.164",
    "U.S. Embassy Montevideo PSU, Uruguay (USASpending PoP Uruguay).",
    "usaspending_cts_montevideo_psu_20110930",
    "PHASE II/III PHYSICAL SECURITY UPGRADE (PSU), U.S. EMBASSY MONTEVIDEO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4745_1900_SAQMMA07D0010_1900/",
    "Actor: CTS-Hardline, LLC (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle924",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA11F4745_1900_SAQMMA07D0010_1900 (CTS-Hardline; Montevideo PSU). Signed 30 "
    "September 2011. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4745_1900_SAQMMA07D0010_1900/.",
    "USASpending: CTS Montevideo PSU USD 2.099m. Supports cts_montevideo_psu_2p10m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,098,770.92; date_signed 2011-09-30.",
)
row_doc(
    "arkel_tijuana_msgr_14p5m_2021",
    "infrastructure", "building_materials", "us",
    "Arkel International, L.L.C. — Tijuana Marine Security Guard Residence construction",
    "Mexico",
    "1 Jun 2021: Department of State awards contract 19AQMM21C0093 to Arkel International, L.L.C. "
    "for construction services for Tijuana Marine Security Guard Residence; obligated USD "
    "14,522,564.05. CapEx face = award obligation. Distinct from caddell_tijuana_ncc_2007.",
    "14522564.05", "2021-06-01", "2021", "32.515", "-117.038",
    "Marine Security Guard Residence, Tijuana, Mexico (USASpending PoP Mexico; Tijuana pin).",
    "usaspending_arkel_tijuana_msgr_20210601",
    "CONSTRUCTION SERVICES FOR TIJUANA MARINE SECURITY GUARD RESIDENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21C0093_1900_-NONE-_-NONE-/",
    "Actor: Arkel International, L.L.C. (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle924",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21C0093_1900_-NONE-_-NONE- "
    "(Arkel; Tijuana MSGR). Signed 1 June 2021. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21C0093_1900_-NONE-_-NONE-/.",
    "USASpending: Arkel Tijuana MSGR USD 14.523m. Supports arkel_tijuana_msgr_14p5m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14,522,564.05; date_signed 2021-06-01.",
)
row_doc(
    "framaco_buenos_aires_dcmr_3p78m_2023",
    "infrastructure", "building_materials", "us",
    "Framaco-Bozdemir JV LLC — Embassy Buenos Aires DCMR renovation",
    "Argentina",
    "23 May 2023: Department of State awards contract 19GE5023C0013 to Framaco-Bozdemir Joint "
    "Venture LLC for Deputy Chief of Mission Residence (DCMR) renovation at U.S. Embassy Buenos "
    "Aires, Argentina; obligated USD 3,781,576.85. CapEx face = award obligation. Distinct from "
    "caddell_buenos_aires_sip_2025 / framaco_barbados_renewable_4p45m_2021.",
    "3781576.85", "2023-05-23", "2023", "-34.604", "-58.382",
    "DCMR renovation, U.S. Embassy Buenos Aires, Argentina (USASpending PoP Argentina).",
    "usaspending_framaco_buenos_aires_dcmr_20230523",
    "DEPUTY CHIEF OF MISSION RESIDENCE (DCMR) RENOVATION, U.S. EMBASSY BUENOS AIRES, ARGENTINA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0013_1900_-NONE-_-NONE-/",
    "Actor: Framaco-Bozdemir JV LLC (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle924",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5023C0013_1900_-NONE-_-NONE- "
    "(Framaco-Bozdemir; Buenos Aires DCMR). Signed 23 May 2023. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0013_1900_-NONE-_-NONE-/.",
    "USASpending: Framaco Buenos Aires DCMR USD 3.782m. Supports framaco_buenos_aires_dcmr_3p78m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,781,576.85; date_signed 2023-05-23.",
)
row_doc(
    "american_roofing_buenos_aires_1p11m_2010",
    "infrastructure", "building_materials", "us",
    "American Roofing & Metal Co Inc. — Buenos Aires chancery compound roof D/B",
    "Argentina",
    "7 Jan 2010: Department of State awards task order SAQMMA10F0441 to American Roofing & Metal "
    "Co Inc. for design/build roof replacement and repair at chancery compound Buenos Aires, "
    "Argentina; obligated USD 1,110,295.00. CapEx face = award obligation.",
    "1110295.00", "2010-01-07", "2010", "-34.604", "-58.382",
    "Chancery compound roof, Buenos Aires, Argentina (USASpending PoP Argentina).",
    "usaspending_american_roofing_buenos_aires_20100107",
    "DESIGN/BUILD ROOF REPLACEMENT AND REPAIR AT CHANCERY COMPOUND BUENOS AIRES, ARGENTINA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F0441_1900_SALMEC07D0029_1900/",
    "Actor: American Roofing & Metal Co Inc. (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle924",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA10F0441_1900_SALMEC07D0029_1900 (American Roofing; Buenos Aires roof). Signed 7 "
    "January 2010. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F0441_1900_SALMEC07D0029_1900/.",
    "USASpending: American Roofing Buenos Aires USD 1.110m. Supports american_roofing_buenos_aires_1p11m_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,110,295.00; date_signed 2010-01-07.",
)
row_doc(
    "copper_river_santiago_msgr_6p63m_2023",
    "infrastructure", "building_materials", "us",
    "Copper River Infrastructure Services LLC — Santiago MSGR renovations completion",
    "Chile",
    "29 Sep 2023: Department of State awards contract 19AQMM23C0155 to Copper River Infrastructure "
    "Services LLC for construction contract for completion of the MSGR renovations in Santiago, "
    "Chile; obligated USD 6,627,937.30. CapEx face = award obligation.",
    "6627937.30", "2023-09-29", "2023", "-33.449", "-70.669",
    "MSGR renovations, Santiago, Chile (USASpending PoP Chile).",
    "usaspending_copper_river_santiago_msgr_20230929",
    "CONSTRUCTION CONTRACT FOR COMPLETION OF THE MSGR RENOVATIONS IN SANTIAGO, CHILE,",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23C0155_1900_-NONE-_-NONE-/",
    "Actor: Copper River Infrastructure Services LLC (U.S.) under State — us. Official USASpending "
    "Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle924",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23C0155_1900_-NONE-_-NONE- "
    "(Copper River; Santiago MSGR). Signed 29 September 2023. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23C0155_1900_-NONE-_-NONE-/.",
    "USASpending: Copper River Santiago MSGR USD 6.628m. Supports copper_river_santiago_msgr_6p63m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6,627,937.30; date_signed 2023-09-29.",
)

# === 925 ===
row_doc(
    "roofing_resources_santiago_obc_3p85m_2019",
    "infrastructure", "building_materials", "us",
    "Roofing Resources Inc. — Santiago OBC roof replacement",
    "Chile",
    "7 Aug 2019: Department of State awards task order 19AQMM19F2621 to Roofing Resources Inc. for "
    "Santiago, Chile OBC roof replacement project; obligated USD 3,853,896.21. CapEx face = award "
    "obligation. Distinct from roofing_resources_managua_roof_3p77m_2013 / "
    "copper_river_santiago_msgr_6p63m_2023.",
    "3853896.21", "2019-08-07", "2019", "-33.449", "-70.669",
    "OBC roof replacement, Santiago, Chile (USASpending PoP Chile).",
    "usaspending_roofing_santiago_obc_20190807",
    "SANTIAGO, CHILE OBC ROOF REPLACEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F2621_1900_19AQMM19D0080_1900/",
    "Actor: Roofing Resources Inc. (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle925",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM19F2621_1900_19AQMM19D0080_1900 (Roofing Resources; Santiago OBC). Signed 7 "
    "August 2019. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F2621_1900_19AQMM19D0080_1900/.",
    "USASpending: Roofing Resources Santiago OBC USD 3.854m. Supports roofing_resources_santiago_obc_3p85m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,853,896.21; date_signed 2019-08-07.",
)
row_doc(
    "oes_santiago_fe_br_3p60m_2011",
    "infrastructure", "building_materials", "us",
    "O.E.S., Inc. — Embassy Santiago Phase III/IV FE/BR replacement and repair",
    "Chile",
    "28 Sep 2011: Department of State awards task order SAQMMA11F4070 to O.E.S., Inc. for Phase "
    "III/IV forced entry/ballistic resistant (FE/BR) product replacement and repair at U.S. "
    "Embassy Santiago, Chile; obligated USD 3,595,742.41. CapEx face = award obligation. Distinct "
    "from oes_quito_fe_br_1p27m_2012.",
    "3595742.41", "2011-09-28", "2011", "-33.449", "-70.669",
    "U.S. Embassy Santiago FE/BR replacement, Chile (USASpending PoP Chile).",
    "usaspending_oes_santiago_fe_br_20110928",
    "PHASE III/IV FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND REPAIR AT U.S. "
    "EMBASSY SANTIAGO,",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4070_1900_SAQMMA07D0009_1900/",
    "Actor: O.E.S., Inc. (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle925",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA11F4070_1900_SAQMMA07D0009_1900 (O.E.S.; Santiago FE/BR). Signed 28 September "
    "2011. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F4070_1900_SAQMMA07D0009_1900/.",
    "USASpending: O.E.S. Santiago FE/BR USD 3.596m. Supports oes_santiago_fe_br_3p60m_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,595,742.41; date_signed 2011-09-28.",
)
row_doc(
    "studio_ma_santiago_design_3p57m_2025",
    "infrastructure", "engineering_epc", "us",
    "Studio MA, Inc. — existing embassy compound project development and design Santiago",
    "Chile",
    "1 Aug 2025: Department of State awards task order 19AQMM25F1073 to Studio MA, Inc. for project "
    "development and design services for an existing embassy compound in Santiago, Chile; "
    "obligated USD 3,566,510.38. CapEx face = award obligation.",
    "3566510.38", "2025-08-01", "2025", "-33.449", "-70.669",
    "Existing embassy compound design, Santiago, Chile (USASpending PoP Chile).",
    "usaspending_studio_ma_santiago_design_20250801",
    "PROJECT DEVELOPMENT AND DESIGN SERVICES FOR A EXISTING EMBASSY COMPOUND IN SANTIAGO EMBASSY - "
    "SANTIAGO, CHILE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F1073_1900_19AQMM19D0072_1900/",
    "Actor: Studio MA, Inc. (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle925",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM25F1073_1900_19AQMM19D0072_1900 (Studio MA; Santiago design). Signed 1 August "
    "2025. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F1073_1900_19AQMM19D0072_1900/.",
    "USASpending: Studio MA Santiago design USD 3.567m. Supports studio_ma_santiago_design_3p57m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3,566,510.38; date_signed 2025-08-01.",
)
row_doc(
    "beltsville_brasilia_psu_10p2m_2010",
    "infrastructure", "building_materials", "us",
    "Beltsville Industries Group, Inc. — Brasilia physical security upgrades D/B",
    "Brazil",
    "30 Sep 2010: Department of State awards contract SAQMMA10C0336 to Beltsville Industries Group, "
    "Inc. for design/build services for physical security upgrades in Brasilia; obligated USD "
    "10,226,242.65. CapEx face = award obligation. Distinct from caddell_brasilia_nec_2022.",
    "10226242.65", "2010-09-30", "2010", "-15.794", "-47.882",
    "Physical security upgrades, Brasilia, Brazil (USASpending PoP Brazil).",
    "usaspending_beltsville_brasilia_psu_20100930",
    "DESIGN/BUILD SERVICES FOR PHYSICAL SECURITY UPGRADES IN BRASILIA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10C0336_1900_-NONE-_-NONE-/",
    "Actor: Beltsville Industries Group, Inc. (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle925",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10C0336_1900_-NONE-_-NONE- "
    "(Beltsville; Brasilia PSU). Signed 30 September 2010. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10C0336_1900_-NONE-_-NONE-/.",
    "USASpending: Beltsville Brasilia PSU USD 10.226m. Supports beltsville_brasilia_psu_10p2m_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10,226,242.65; date_signed 2010-09-30.",
)
row_doc(
    "studio_gang_brasilia_nec_design_43p6m_2017",
    "infrastructure", "engineering_epc", "us",
    "Studio Gang Architects Ltd. — Brasilia New Embassy Compound design",
    "Brazil",
    "25 Sep 2017: Department of State awards contract SAQMMA17C0017 to Studio Gang Architects Ltd. "
    "for Brasilia New Embassy Compound; obligated USD 43,569,280.14. CapEx face = award obligation "
    "(design/A&E package). Distinct from caddell_brasilia_nec_2022 (construction). USASpending PoP "
    "codes United States — country coded Brazil per description.",
    "43569280.14", "2017-09-25", "2017", "-15.794", "-47.882",
    "New Embassy Compound design, Brasilia, Brazil (award description; Brasilia pin).",
    "usaspending_studio_gang_brasilia_nec_20170925",
    "BRASILIA NEW EMBASSY COMPOUND.IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0017_1900_-NONE-_-NONE-/",
    "Actor: Studio Gang Architects Ltd. (U.S.) under State — us. Official USASpending Award API. "
    "Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle925",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0017_1900_-NONE-_-NONE- "
    "(Studio Gang; Brasilia NEC design). Signed 25 September 2017. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0017_1900_-NONE-_-NONE-/.",
    "USASpending: Studio Gang Brasilia NEC design USD 43.569m. Supports studio_gang_brasilia_nec_design_43p6m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 43,569,280.14; date_signed 2017-09-25.",
)

# === 926 ===
row_doc(
    "venesco_ciudad_juarez_msgr_16p5m_2017",
    "infrastructure", "building_materials", "us",
    "Venesco Construction Management LLC — Ciudad Juárez Marine Security Guard Residence",
    "Mexico",
    "30 Sep 2017: Department of State awards contract SAQMMA17C0295 to Venesco Construction "
    "Management LLC for design and construction of new Marine Security Guard Residence in Ciudad "
    "Juárez, Mexico; obligated USD 16,473,527.22. CapEx face = award obligation. Distinct from "
    "arkel_tijuana_msgr_14p5m_2021.",
    "16473527.22", "2017-09-30", "2017", "31.690", "-106.425",
    "Marine Security Guard Residence, Ciudad Juárez, Mexico (USASpending PoP Mexico).",
    "usaspending_venesco_ciudad_juarez_msgr_20170930",
    "DESIGN AND CONSTRUCTION OF NEW MARINE SECURITY GUARD RESIDENCE LOCATED IN CIUDAD JUAREZ, MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0295_1900_-NONE-_-NONE-/",
    "Actor: Venesco Construction Management LLC (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle926",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0295_1900_-NONE-_-NONE- "
    "(Venesco; Ciudad Juárez MSGR). Signed 30 September 2017. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0295_1900_-NONE-_-NONE-/.",
    "USASpending: Venesco Ciudad Juárez MSGR USD 16.474m. Supports venesco_ciudad_juarez_msgr_16p5m_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 16,473,527.22; date_signed 2017-09-30.",
)
row_doc(
    "markon_brasilia_nec_eng_8p41m_2021",
    "infrastructure", "engineering_epc", "us",
    "Markon LLC — professional engineering services for Brasilia NEC",
    "Brazil",
    "19 Sep 2021: Department of State awards task order 19AQMM21F4135 to Markon LLC for professional "
    "engineering services in support of the Brasilia, Brazil New Embassy Compound (NEC) project; "
    "obligated USD 8,414,218.14. CapEx face = award obligation. Distinct from "
    "caddell_brasilia_nec_2022 / studio_gang_brasilia_nec_design_43p6m_2017.",
    "8414218.14", "2021-09-19", "2021", "-15.794", "-47.882",
    "Brasilia NEC engineering support, Brazil (USASpending PoP Brazil).",
    "usaspending_markon_brasilia_nec_20210919",
    "THE CONTRACTOR SHALL PROVIDE PROFESSIONAL ENGINEERING SERVICES IN SUPPORT OF THE BRASILIA, "
    "BRAZIL  NEW EMBASSY COMPOUND (NEC) PROJ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F4135_1900_SAQMMA13D0077_1900/",
    "Actor: Markon LLC (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle926",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM21F4135_1900_SAQMMA13D0077_1900 (Markon; Brasilia NEC engineering). Signed 19 "
    "September 2021. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F4135_1900_SAQMMA13D0077_1900/.",
    "USASpending: Markon Brasilia NEC eng USD 8.414m. Supports markon_brasilia_nec_eng_8p41m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8,414,218.14; date_signed 2021-09-19.",
)
row_doc(
    "versar_guadalajara_eng_1p70m_2019",
    "infrastructure", "engineering_epc", "us",
    "Versar, Inc. — third-party professional engineering for Guadalajara NCC",
    "Mexico",
    "17 Apr 2019: Department of State awards task order 19AQMM19F1351 to Versar, Inc. for third-party "
    "professional engineering services in support of the Guadalajara, Mexico New Consulate Compound; "
    "obligated USD 1,701,947.63. CapEx face = award obligation. Distinct from "
    "bl_harbert_guadalajara_ncc_2018.",
    "1701947.63", "2019-04-17", "2019", "20.660", "-103.350",
    "Guadalajara NCC engineering support, Mexico (USASpending PoP Mexico).",
    "usaspending_versar_guadalajara_eng_20190417",
    "THE CONTRACTOR SHALL PROVIDE A THIRD PARTY CONTRACTOR TO PROVIDE PROFESSIONAL ENGINEERING "
    "SERVICES IN SUPPORT OF THE GUADALAJARA,",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1351_1900_SAQMMA14D0035_1900/",
    "Actor: Versar, Inc. (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle926",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM19F1351_1900_SAQMMA14D0035_1900 (Versar; Guadalajara engineering). Signed 17 "
    "April 2019. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F1351_1900_SAQMMA14D0035_1900/.",
    "USASpending: Versar Guadalajara eng USD 1.702m. Supports versar_guadalajara_eng_1p70m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,701,947.63; date_signed 2019-04-17.",
)
row_doc(
    "src_hermosillo_ncc_eng_2p60m_2019",
    "infrastructure", "engineering_epc", "us",
    "Scientific Research Corporation — professional engineering for Hermosillo NCC",
    "Mexico",
    "17 Sep 2019: Department of State awards task order 19AQMM19F3722 to Scientific Research "
    "Corporation for third-party professional engineering services in support of the Hermosillo, "
    "Mexico New Consulate Compound (NCC) project; obligated USD 2,601,526.73. CapEx face = award "
    "obligation. Distinct from bl_harbert_hermosillo_ncc_2018.",
    "2601526.73", "2019-09-17", "2019", "29.073", "-110.958",
    "Hermosillo NCC engineering support, Mexico (USASpending PoP Mexico).",
    "usaspending_src_hermosillo_ncc_eng_20190917",
    "THIRD PARTY CONTRACTOR TO PROVIDE PROFESSIONAL ENGINEERING SERVICES IN SUPPORT OF THE "
    "HERMOSILLO, MEXICO NEW CONSULATE COMPOUND (NCC) PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F3722_1900_SAQMMA13D0078_1900/",
    "Actor: Scientific Research Corporation (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle926",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM19F3722_1900_SAQMMA13D0078_1900 (SRC; Hermosillo NCC engineering). Signed 17 "
    "September 2019. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F3722_1900_SAQMMA13D0078_1900/.",
    "USASpending: SRC Hermosillo NCC eng USD 2.602m. Supports src_hermosillo_ncc_eng_2p60m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,601,526.73; date_signed 2019-09-17.",
)
row_doc(
    "wsp_ciudad_juarez_cm_929k_2018",
    "infrastructure", "engineering_epc", "us",
    "WSP USA Solutions Inc. — Ciudad Juárez construction management / architectural services",
    "Mexico",
    "23 Mar 2018: Department of State awards task order 19AQMM18F1093 to WSP USA Solutions Inc. for "
    "construction management (base) and architectural services (optional) in support of Ciudad "
    "Juárez facilities; obligated USD 929,119.43. CapEx face = award obligation. Distinct from "
    "venesco_ciudad_juarez_msgr_16p5m_2017 / wsp_cap_haitien_port_cm_2p3m_2016.",
    "929119.43", "2018-03-23", "2018", "31.690", "-106.425",
    "Construction management / architectural services, Ciudad Juárez, Mexico (USASpending PoP Mexico).",
    "usaspending_wsp_ciudad_juarez_cm_20180323",
    "THE CONTRACTOR SHALL PROVIDE CONSTRUCTION MANAGEMENT (BASE SERVICES) AND ARCHITECTURAL "
    "SERVICES (OPTIONAL SERVICE) IN SUPPORT OF T",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1093_1900_SAQMMA13D0079_1900/",
    "Actor: WSP USA Solutions Inc. (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle926",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM18F1093_1900_SAQMMA13D0079_1900 (WSP; Ciudad Juárez CM). Signed 23 March 2018. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F1093_1900_SAQMMA13D0079_1900/.",
    "USASpending: WSP Ciudad Juárez CM USD 0.929m. Supports wsp_ciudad_juarez_cm_929k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 929,119.43; date_signed 2018-03-23.",
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
    print(f"cycles924-926 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
