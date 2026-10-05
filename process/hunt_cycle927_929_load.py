#!/usr/bin/env python3
"""Cycles 927–929: USASpending Venezuela CapEx-fill + CA/Andean/Caribbean residual.

Seeds: 20261927–20261929. Thin top-up dry (balsa/nickel/fission/niobium).
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


# === 927 ===
row_doc(
    "cce_caracas_msgq_11p6m_2009",
    "infrastructure", "building_materials", "us",
    "Contracting, Consulting, Engineering LLC — Caracas MSGQ design/build",
    "Venezuela",
    "30 Sep 2009: Department of State awards task order SAQMMA09F4609 to Contracting, Consulting, "
    "Engineering LLC for design/build MSGQ (Marine Security Guard Quarters) Caracas, Venezuela; "
    "obligated USD 11,597,388.72. CapEx face = award obligation. CapEx-fill for Venezuela blank cell.",
    "11597388.72", "2009-09-30", "2009", "10.481", "-66.904",
    "MSGQ / U.S. Embassy Caracas, Venezuela (USASpending PoP Venezuela; Caracas pin).",
    "usaspending_cce_caracas_msgq_20090930",
    "DESIGN/BUILD MSGQ CARACAS, VENEZUELA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA09F4609_1900_SAQMMA08D0003_1900/",
    "Actor: Contracting, Consulting, Engineering LLC (U.S./Easton) under State — us. Official "
    "USASpending Award API. Shuffle building_materials; Venezuela CapEx-fill; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle927",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA09F4609_1900_SAQMMA08D0003_1900 (CCE; Caracas MSGQ). Signed 30 September 2009. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA09F4609_1900_SAQMMA08D0003_1900/.",
    "USASpending: CCE Caracas MSGQ USD 11.597m. Supports cce_caracas_msgq_11p6m_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11,597,388.72; date_signed 2009-09-30.",
)
row_doc(
    "nve_caracas_electrical_4p44m_2026",
    "infrastructure", "engineering_epc", "us",
    "NVE, Inc. — Caracas electrical upgrades",
    "Venezuela",
    "18 Sep 2026: Department of State awards task order 19AQMM26F1456 to NVE, Inc. for Caracas "
    "electrical upgrades; obligated USD 4,437,428. CapEx face = award obligation. Distinct from "
    "cce_caracas_msgq_11p6m_2009 / aecom_caracas_electrical_1p91m_2014.",
    "4437428", "2026-09-18", "2026", "10.481", "-66.904",
    "Electrical upgrades, Caracas / U.S. diplomatic facilities, Venezuela (USASpending PoP Venezuela).",
    "usaspending_nve_caracas_electrical_20260918",
    "CARACAS ELECTRICAL UPGRADES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F1456_1900_19AQMM24D0035_1900/",
    "Actor: NVE, Inc. (U.S./Reston) under State — us. Official USASpending Award API. Shuffle "
    "engineering_epc; Venezuela CapEx-fill; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle927",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM26F1456_1900_19AQMM24D0035_1900 (NVE; Caracas electrical). Signed 18 September "
    "2026. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM26F1456_1900_19AQMM24D0035_1900/.",
    "USASpending: NVE Caracas electrical USD 4.437m. Supports nve_caracas_electrical_4p44m_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 4,437,428; date_signed 2026-09-18.",
)
row_doc(
    "aecom_caracas_electrical_1p91m_2014",
    "infrastructure", "engineering_epc", "us",
    "AECOM Energy & Construction, Inc. — Caracas electrical work",
    "Venezuela",
    "27 Sep 2014: Department of State awards task order SAQMMA14F4390 to AECOM Energy & Construction, "
    "Inc. for electrical work Caracas; obligated USD 1,907,635.20. CapEx face = award obligation. "
    "Distinct from nve_caracas_electrical_4p44m_2026.",
    "1907635.20", "2014-09-27", "2014", "10.481", "-66.904",
    "Electrical work, Caracas, Venezuela (USASpending PoP Venezuela).",
    "usaspending_aecom_caracas_electrical_20140927",
    "ELECTRICAL WORK CARACAS IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F4390_1900_SAQMMA12D0193_1900/",
    "Actor: AECOM Energy & Construction, Inc. (U.S.) under State — us. Official USASpending Award "
    "API. Shuffle engineering_epc; Venezuela CapEx-fill; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle927",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA14F4390_1900_SAQMMA12D0193_1900 (AECOM; Caracas electrical). Signed 27 September "
    "2014. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F4390_1900_SAQMMA12D0193_1900/.",
    "USASpending: AECOM Caracas electrical USD 1.908m. Supports aecom_caracas_electrical_1p91m_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,907,635.20; date_signed 2014-09-27.",
)
row_doc(
    "horizon_costa_rica_msgr_6p37m_2019",
    "infrastructure", "building_materials", "us",
    "Horizon Construction Group / ICS JV — Costa Rica MSGR renovation",
    "Costa Rica",
    "13 Mar 2019: Department of State awards task order 19AQMM19F0678 to Horizon Construction Group / "
    "International Construction Services JV, LLC to renovate a Marine Security Guard Residence in "
    "Costa Rica; obligated USD 6,373,794.19. CapEx face = award obligation.",
    "6373794.19", "2019-03-13", "2019", "9.928", "-84.091",
    "Marine Security Guard Residence renovation, Costa Rica (USASpending PoP Costa Rica; San José pin).",
    "usaspending_horizon_costa_rica_msgr_20190313",
    "THE PURPOSE OF THIS TASK ORDER IS TO RENOVATE A MARINE SECURITY GUARD RESIDENCE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F0678_1900_SAQMMA14D0056_1900/",
    "Actor: Horizon Construction Group / ICS JV (U.S./Memphis) under State — us. Official USASpending "
    "Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle927",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM19F0678_1900_SAQMMA14D0056_1900 (Horizon; Costa Rica MSGR). Signed 13 March 2019. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19F0678_1900_SAQMMA14D0056_1900/.",
    "USASpending: Horizon Costa Rica MSGR USD 6.374m. Supports horizon_costa_rica_msgr_6p37m_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6,373,794.19; date_signed 2019-03-13.",
)
row_doc(
    "roofing_panama_nec_5p19m_2015",
    "infrastructure", "building_materials", "us",
    "Roofing Resources Inc. — Panama City NEC roof replacement",
    "Panama",
    "28 Sep 2015: Department of State awards task order SAQMMA15F3907 to Roofing Resources Inc. for "
    "the Panama City NEC roof replacement project; obligated USD 5,191,123.30. CapEx face = award "
    "obligation. Distinct from roofing_resources_santiago_obc_3p85m_2019 / "
    "roofing_resources_managua_roof_3p77m_2013.",
    "5191123.30", "2015-09-28", "2015", "8.982", "-79.520",
    "NEC roof replacement, Panama City, Panama (USASpending PoP Panama).",
    "usaspending_roofing_panama_nec_20150928",
    "IGF::OT::IGF AWARD OF THE PANAMA CITY NEC ROOF REPLACEMENT PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F3907_1900_SAQMMA13D0137_1900/",
    "Actor: Roofing Resources Inc. (U.S./Chadds Ford) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle927",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA15F3907_1900_SAQMMA13D0137_1900 (Roofing Resources; Panama NEC roof). Signed 28 "
    "September 2015. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F3907_1900_SAQMMA13D0137_1900/.",
    "USASpending: Roofing Panama NEC USD 5.191m. Supports roofing_panama_nec_5p19m_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5,191,123.30; date_signed 2015-09-28.",
)

# === 928 ===
row_doc(
    "amentum_lapaz_power_plant_10m_2023",
    "energy", "power_plants_grid", "us",
    "Amentum Services, Inc. — La Paz OBO OPS FAC power plant",
    "Bolivia",
    "20 Dec 2023: Department of State awards task order 19AQMM24F0150 to Amentum Services, Inc. for "
    "OBO OPS FAC La Paz power plant; obligated USD 9,997,460. CapEx face = award obligation.",
    "9997460", "2023-12-20", "2023", "-16.500", "-68.150",
    "OBO OPS FAC power plant, La Paz, Bolivia (USASpending PoP Bolivia).",
    "usaspending_amentum_lapaz_power_20231220",
    "OBO OPS FAC LA PAZ POWER PLANT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0150_1900_19AQMM18D0073_1900/",
    "Actor: Amentum Services, Inc. (U.S./Germantown) under State — us. Official USASpending Award "
    "API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle928",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM24F0150_1900_19AQMM18D0073_1900 (Amentum; La Paz power plant). Signed 20 December "
    "2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0150_1900_19AQMM18D0073_1900/.",
    "USASpending: Amentum La Paz power plant USD 9.998m. Supports amentum_lapaz_power_plant_10m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9,997,460; date_signed 2023-12-20.",
)
row_doc(
    "tabcon_kingston_nec_roof_6p02m_2024",
    "infrastructure", "building_materials", "us",
    "Tabcon, Inc. — Kingston NEC design-build roof",
    "Jamaica",
    "25 Sep 2024: Department of State awards task order 19AQMM24F2351 to Tabcon, Inc. for U.S. "
    "Embassy Kingston, Jamaica NEC design-build roof requirement; obligated USD 6,019,644. CapEx "
    "face = award obligation. Distinct from yates_kingston_nox / desbuild residual Kingston rows.",
    "6019644", "2024-09-25", "2024", "18.018", "-76.810",
    "NEC design-build roof, U.S. Embassy Kingston, Jamaica (USASpending PoP Jamaica).",
    "usaspending_tabcon_kingston_nec_roof_20240925",
    "US EMBASSY KINGSTON, JAMAICA NEC DESIGN BUILD ROOF REQUIREMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2351_1900_19AQMM19D0084_1900/",
    "Actor: Tabcon, Inc. (U.S./Queen Creek) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle928",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM24F2351_1900_19AQMM19D0084_1900 (Tabcon; Kingston NEC roof). Signed 25 September "
    "2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F2351_1900_19AQMM19D0084_1900/.",
    "USASpending: Tabcon Kingston NEC roof USD 6.020m. Supports tabcon_kingston_nec_roof_6p02m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6,019,644; date_signed 2024-09-25.",
)
row_doc(
    "futron_kingston_pv_2p19m_2024",
    "energy", "solar", "us",
    "Futron, Inc. — Kingston chiller and photovoltaic energy upgrade",
    "Jamaica",
    "20 Mar 2024: Department of State awards task order 19AQMM24F0649 to Futron, Inc. for design and "
    "construction of the Kingston chiller and photovoltaic energy upgrade project at Embassy "
    "Kingston, Jamaica; obligated USD 2,189,342.23. CapEx face = award obligation.",
    "2189342.23", "2024-03-20", "2024", "18.018", "-76.810",
    "Chiller + photovoltaic upgrade, U.S. Embassy Kingston, Jamaica (USASpending PoP Jamaica).",
    "usaspending_futron_kingston_pv_20240320",
    "DESIGN AND CONSTRUCTION OF THE KINGSTON CHILLER AND PHOTOVOLTAIC ENERGY UPGRADE PROJECT AT THE "
    "EMBASSY KINGSTON, JAMAICA)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0649_1900_19AQMM22D0075_1900/",
    "Actor: Futron, Inc. (U.S./Woodbridge) under State — us. Official USASpending Award API. Shuffle "
    "solar; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle928",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM24F0649_1900_19AQMM22D0075_1900 (Futron; Kingston PV). Signed 20 March 2024. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0649_1900_19AQMM22D0075_1900/.",
    "USASpending: Futron Kingston PV USD 2.189m. Supports futron_kingston_pv_2p19m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2,189,342.23; date_signed 2024-03-20.",
)
row_doc(
    "aecom_callao_harbor_p2_14p5m_2024",
    "infrastructure", "port_ownership", "us",
    "AECOM Technical Services, Inc. — Peruvian Navy Port of Callao Phase 2 harbor design-build",
    "Peru",
    "6 Jun 2024: USACE awards task order W9127824F0117 to AECOM Technical Services, Inc. for FMS "
    "Peruvian Navy Port of Callao Phase 2 harbor design-build; obligated USD 14,450,194.46. CapEx "
    "face = award obligation. Distinct from kgn_callao_navy_infra_22p2m_2025 (W9127825C0021).",
    "14450194.46", "2024-06-06", "2024", "-12.051", "-77.126",
    "Port of Callao Phase 2 harbor design-build, Peru (USASpending PoP Peru; Callao pin).",
    "usaspending_aecom_callao_harbor_p2_20240606",
    "FMS PERUVIAN NAVY PORT OF CALLAO - PHASE 2 HARBOR DESIGNBUILD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0117_9700_W9127821D0040_9700/",
    "Actor: AECOM Technical Services, Inc. (U.S./Los Angeles) under DoD/USACE — us. Official "
    "USASpending Award API. Shuffle port_ownership; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle928",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127824F0117_9700_W9127821D0040_9700 (AECOM; Callao Phase 2). Signed 6 June 2024. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127824F0117_9700_W9127821D0040_9700/.",
    "USASpending: AECOM Callao harbor P2 USD 14.450m. Supports aecom_callao_harbor_p2_14p5m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14,450,194.46; date_signed 2024-06-06.",
)
row_doc(
    "desbuild_belize_msgr_14m_2015",
    "infrastructure", "building_materials", "us",
    "Desbuild Incorporated — Belize MSGR + consulate office renovations",
    "Belize",
    "26 Feb 2015: Department of State awards contract SAQMMA15C0021 to Desbuild Incorporated for "
    "design/build construction of new Marine Security Guard Residence (MSGR) and renovations to the "
    "consulate office building, Belize; obligated USD 13,982,593.56. CapEx face = award obligation. "
    "Distinct from desbuild_bogota_consular_11p9m_2023 / desbuild Kingston rows.",
    "13982593.56", "2015-02-26", "2015", "17.251", "-88.759",
    "MSGR + consulate office renovations, Belmopan, Belize (USASpending PoP Belize).",
    "usaspending_desbuild_belize_msgr_20150226",
    "DESIGN/BUILD CONSTRUCTION: NEW MARINE SECURITY GUARD RESIDENCE (MSGR) AND RENOVATIONS TO THE "
    "CONSULATE OFFICE BUILDING IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15C0021_1900_-NONE-_-NONE-/",
    "Actor: Desbuild Incorporated (U.S./Hyattsville) under State — us. Official USASpending Award "
    "API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle928",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA15C0021_1900_-NONE-_-NONE- (Desbuild; Belize MSGR). Signed 26 February 2015. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15C0021_1900_-NONE-_-NONE-/.",
    "USASpending: Desbuild Belize MSGR USD 13.983m. Supports desbuild_belize_msgr_14m_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13,982,593.56; date_signed 2015-02-26.",
)

# === 929 ===
row_doc(
    "montage_guayaquil_msgr_16p7m_2014",
    "infrastructure", "building_materials", "us",
    "Montage, Inc. — Guayaquil MSGR design and construction",
    "Ecuador",
    "30 Sep 2014: Department of State awards contract SAQMMA14C0200 to Montage, Inc. for design and "
    "construction of new Marine Security Guard Residence (MSGR) in Guayaquil, Ecuador; obligated "
    "USD 16,652,702.76. CapEx face = award obligation.",
    "16652702.76", "2014-09-30", "2014", "-2.171", "-79.922",
    "New MSGR, Guayaquil, Ecuador (USASpending PoP Ecuador; Guayaquil pin).",
    "usaspending_montage_guayaquil_msgr_20140930",
    "OTHER FUNCTIONS    IGF::OT::IGF   DESIGN AND CONSTRUCTION OF NEW MARINE SECURITY GUARD "
    "RESIDENCE (MSGR) IN GUAYAQUIL, ECUADOR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0200_1900_-NONE-_-NONE-/",
    "Actor: Montage, Inc. (U.S./Washington) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle929",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA14C0200_1900_-NONE-_-NONE- (Montage; Guayaquil MSGR). Signed 30 September 2014. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0200_1900_-NONE-_-NONE-/.",
    "USASpending: Montage Guayaquil MSGR USD 16.653m. Supports montage_guayaquil_msgr_16p7m_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 16,652,702.76; date_signed 2014-09-30.",
)
row_doc(
    "tidewater_managua_consular_6p27m_2025",
    "infrastructure", "building_materials", "us",
    "Tidewater, Inc. — Managua consular affairs renovation design/build",
    "Nicaragua",
    "5 Mar 2025: Department of State awards task order 19AQMM25F0451 to Tidewater, Inc. for "
    "design/build U.S. Embassy Managua consular affairs renovation; obligated USD 6,273,249. CapEx "
    "face = award obligation. Distinct from roofing_resources_managua_roof_3p77m_2013 / "
    "blackwell_managua_design_910k_2023.",
    "6273249", "2025-03-05", "2025", "12.136", "-86.251",
    "Consular affairs renovation, U.S. Embassy Managua, Nicaragua (USASpending PoP Nicaragua).",
    "usaspending_tidewater_managua_consular_20250305",
    "DESIGN/BUILD CONTRACT FOR THE U.S. EMBASSY MANAGUA CONSULAR AFFAIRS RENOVATION.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F0451_1900_19AQMM22D0058_1900/",
    "Actor: Tidewater, Inc. (U.S./Elkridge) under State — us. Official USASpending Award API. "
    "Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle929",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM25F0451_1900_19AQMM22D0058_1900 (Tidewater; Managua consular). Signed 5 March "
    "2025. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F0451_1900_19AQMM22D0058_1900/.",
    "USASpending: Tidewater Managua consular USD 6.273m. Supports tidewater_managua_consular_6p27m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6,273,249; date_signed 2025-03-05.",
)
row_doc(
    "interim_santiago_power_6p23m_2023",
    "energy", "power_plants_grid", "us",
    "Interim Homes, Inc. — Santiago power plant replacement",
    "Chile",
    "27 Sep 2023: Department of State awards task order 19AQMM23F3324 to Interim Homes, Inc. for "
    "Santiago power plant replacement; obligated USD 6,225,841.99. CapEx face = award obligation. "
    "Distinct from alutiiq_santiago_psap_12p1m_2016 / copper_river_santiago_msgr_6p63m_2023.",
    "6225841.99", "2023-09-27", "2023", "-33.449", "-70.669",
    "Power plant replacement, U.S. Embassy Santiago, Chile (USASpending PoP Chile).",
    "usaspending_interim_santiago_power_20230927",
    "SANTIAGO POWER PLANT REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F3324_1900_19AQMM18D0140_1900/",
    "Actor: Interim Homes, Inc. (U.S./Annapolis) under State — us. Official USASpending Award API. "
    "Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle929",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM23F3324_1900_19AQMM18D0140_1900 (Interim Homes; Santiago power). Signed 27 "
    "September 2023. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F3324_1900_19AQMM18D0140_1900/.",
    "USASpending: Interim Santiago power USD 6.226m. Supports interim_santiago_power_6p23m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6,225,841.99; date_signed 2023-09-27.",
)
row_doc(
    "palgag_namru6_lima_25p4m_2018",
    "infrastructure", "building_materials", "allied",
    "Palgag Building Technologies Ltd — NAMRU-6 Building 1 revitalization (Lima)",
    "Peru",
    "25 Sep 2018: USACE awards task order W9127818F0650 to Palgag Building Technologies Ltd for "
    "NAMRU-6 Building 1 revitalization; obligated USD 25,383,314.23. CapEx face = award obligation. "
    "Distinct from palgag Haiti/Barbados modular rows.",
    "25383314.23", "2018-09-25", "2018", "-12.046", "-77.043",
    "NAMRU-6 Building 1 revitalization, Lima, Peru (USASpending PoP Peru; Lima pin).",
    "usaspending_palgag_namru6_lima_20180925",
    "NAMRU-6 BUILDING 1 REVITALIZATION - TASK ORDER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0650_9700_W9127817D0096_9700/",
    "Actor: Palgag Building Technologies Ltd (Israel/Kibbutz Gaash) under DoD/USACE — allied. "
    "Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle929",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127818F0650_9700_W9127817D0096_9700 (Palgag; NAMRU-6 Lima). Signed 25 September 2018. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127818F0650_9700_W9127817D0096_9700/.",
    "USASpending: Palgag NAMRU-6 Lima USD 25.383m. Supports palgag_namru6_lima_25p4m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 25,383,314.23; date_signed 2018-09-25.",
)
row_doc(
    "eterna_carrillo_coco_schools_1p78m_2021",
    "infrastructure", "building_materials", "other",
    "Empresa de Construcción y Transporte Eterna — Carrillo & Playas del Coco elementary schools",
    "Costa Rica",
    "30 Sep 2021: USACE awards task order W9127821F0494 to Empresa de Construcción y Transporte "
    "Eterna S.A. de C.V. for design and construction of HAP 32323 & HAP 37941 elementary schools at "
    "Carrillo & Playas del Coco, Costa Rica; obligated USD 1,775,410.96. CapEx face = award "
    "obligation. Distinct from eterna_el_bluff_ops_1p43m_2011.",
    "1775410.96", "2021-09-30", "2021", "10.443", "-85.765",
    "Elementary schools at Carrillo & Playas del Coco, Guanacaste, Costa Rica (USASpending PoP Costa "
    "Rica; Carrillo pin).",
    "usaspending_eterna_cr_schools_20210930",
    "DESIGN AND CONSTRUCTION OF HAP 32323 & HAP 37941 ELEMENTARY SCHOOLS, LOCATED AT CARRILLO & "
    "PLAYAS DEL COCO, COSTA RICA, RESPECTIVELY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0494_9700_W9127821D0075_9700/",
    "Actor: Empresa de Construcción y Transporte Eterna S.A. de C.V. (Honduras/San Pedro Sula) under "
    "DoD/USACE — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle929",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_W9127821F0494_9700_W9127821D0075_9700 (Eterna; CR schools). Signed 30 September 2021. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127821F0494_9700_W9127821D0075_9700/.",
    "USASpending: Eterna CR schools USD 1.775m. Supports eterna_carrillo_coco_schools_1p78m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,775,410.96; date_signed 2021-09-30.",
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
    print(f"cycles927-929 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
