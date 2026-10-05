#!/usr/bin/env python3
"""Cycles 1116–1118: USASpending LatAm CapEx residual (~USD0.025–0.039m).

Seeds: 20262116–20262118. Thin top-up dry. Holdovers Syncroflo/Alban residential/Interface/Bentley FAC/Balco/Anacordia closed.
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


# === Cycle 1116 (seed 20262116) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "anacordia_jamaica_generator_fuel_mgmt_upgrade_28k_2020",
    "energy", "power_plants_grid", "us",
    'Anacordia — Jamaica FAC generator fuel management system upgrade',
    "Jamaica",
    '29 Sep 2020: Department of State awards contract 19JM3720P1012 to Anacordia Corporation for generator fuel mgmt system upgrade (PoP Jamaica); obligated USD 27,927.5. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "27927.5", "2020-09-29", "2020", "", "",
    'Generator fuel management system upgrade, Jamaica (USASpending description; site not named — lat/lon blank).',
    "usaspending_anacordia_jamaica_generator_fuel_mgmt_upgrade_28k_2020",
    'FAC - GENERATOR FUEL MGMT SYSTEM UPGRADE - (7901/REST/8000)',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3720P1012_1900_-NONE-_-NONE-/",
    'Actor: Anacordia Corporation (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1116",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3720P1012_1900_-NONE-_-NONE- (anacordia_jamaica_generator_fuel_mgmt_upgrade_28k_2020). Signed 2020-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3720P1012_1900_-NONE-_-NONE-/.',
    'USASpending: anacordia_jamaica_generator_fuel_mgmt_upgrade_28k_2020 USD 0.028m. Supports anacordia_jamaica_generator_fuel_mgmt_upgrade_28k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27927.5; date_signed 2020-09-29.',
)
row_doc(
    "alban_tractor_guyana_residential_generator_28k_2015",
    "energy", "power_plants_grid", "us",
    'Alban Tractor — Guyana USAID residential generator 16 BAS',
    "Guyana",
    '20 Mar 2015: Department of State awards contract SGY20015M0146 to Alban Tractor, LLC for USAID purchase of residential generator-16 BAS (PoP Guyana); obligated USD 27,710. CapEx face = award obligation. Exact residence unnamed — lat/lon blank.',
    "27710", "2015-03-20", "2015", "", "",
    'USAID residential generator-16 BAS, Guyana (USASpending description; residence not named — lat/lon blank).',
    "usaspending_alban_tractor_guyana_residential_generator_28k_2015",
    'USAID-PURCHASE OF RESIDENTIAL GENERATOR-16 BAS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20015M0146_1900_-NONE-_-NONE-/",
    'Actor: Alban Tractor, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1116",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGY20015M0146_1900_-NONE-_-NONE- (alban_tractor_guyana_residential_generator_28k_2015). Signed 2015-03-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20015M0146_1900_-NONE-_-NONE-/.',
    'USASpending: alban_tractor_guyana_residential_generator_28k_2015 USD 0.028m. Supports alban_tractor_guyana_residential_generator_28k_2015.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27710; date_signed 2015-03-20.',
)
row_doc(
    "misc_brazil_electrical_warehouse_renovation_38k_2011",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil electrical warehouse renovation project',
    "Brazil",
    '28 Sep 2011: Department of State awards contract SBR25011M2450 for electrical warehouse renovation project (PoP Brazil); obligated USD 38,419.32. CapEx face = award obligation. Exact warehouse unnamed — lat/lon blank.',
    "38419.32", "2011-09-28", "2011", "", "",
    'Electrical warehouse renovation project, Brazil (USASpending description; warehouse not named — lat/lon blank).',
    "usaspending_misc_brazil_electrical_warehouse_renovation_38k_2011",
    'ELECTRICAL WAREHOUSE RENOVATION PROJECT',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25011M2450_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1116",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25011M2450_1900_-NONE-_-NONE- (misc_brazil_electrical_warehouse_renovation_38k_2011). Signed 2011-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25011M2450_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_electrical_warehouse_renovation_38k_2011 USD 0.038m. Supports misc_brazil_electrical_warehouse_renovation_38k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 38419.32; date_signed 2011-09-28.',
)
row_doc(
    "misc_brazil_official_residency_mr_renovation_38k_2022",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil Brasilia official residency M&R renovation QL12-10-13 & 15',
    "Brazil",
    '20 Apr 2022: Department of State awards contract 19BR2522P0611 for official residency M&R renovation QL12-10-13 & 15 (PoP Brazil); obligated USD 38,120.29. CapEx face = award obligation. Exact residency unnamed — lat/lon blank.',
    "38120.29", "2022-04-20", "2022", "", "",
    'Official residency M&R renovation QL12-10-13 & 15, Brazil (USASpending description; residency named by QL codes, site coords not stated — lat/lon blank).',
    "usaspending_misc_brazil_official_residency_mr_renovation_38k_2022",
    'BSB-FAC|OFFICIAL RESIDENCY| M&R RENOVATION QL12-10-13 & 15',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2522P0611_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1116",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2522P0611_1900_-NONE-_-NONE- (misc_brazil_official_residency_mr_renovation_38k_2022). Signed 2022-04-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2522P0611_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_official_residency_mr_renovation_38k_2022 USD 0.038m. Supports misc_brazil_official_residency_mr_renovation_38k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 38120.29; date_signed 2022-04-20.',
)
row_doc(
    "misc_argentina_obc_guards_dressing_bathroom_repair_38k_2013",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Argentina OBC guards dressing room and bathroom repair',
    "Argentina",
    '19 Sep 2013: Department of State awards contract SAR20013M0639 for OBC guards dressing room and bathroom repair (PoP Argentina); obligated USD 37,722.06. CapEx face = award obligation. Exact OBC unnamed — lat/lon blank.',
    "37722.06", "2013-09-19", "2013", "", "",
    'OBC guards dressing room and bathroom repair, Argentina (USASpending description; OBC named, site coords not stated — lat/lon blank).',
    "usaspending_misc_argentina_obc_guards_dressing_bathroom_repair_38k_2013",
    'FM- OBC GUARDS DRESSING ROOM AND BATHROOM REPAIR IGF::OT::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20013M0639_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1116",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20013M0639_1900_-NONE-_-NONE- (misc_argentina_obc_guards_dressing_bathroom_repair_38k_2013). Signed 2013-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20013M0639_1900_-NONE-_-NONE-/.',
    'USASpending: misc_argentina_obc_guards_dressing_bathroom_repair_38k_2013 USD 0.038m. Supports misc_argentina_obc_guards_dressing_bathroom_repair_38k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37722.06; date_signed 2013-09-19.',
)

# === Cycle 1117 (seed 20262117) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "bentley_mills_mexico_fac_carpet_tiles_26k_2016",
    "infrastructure", "building_materials", "us",
    'Bentley Mills — Mexico FAC carpet tile supply',
    "Mexico",
    '15 Jun 2016: Department of State awards contract SMX53016F0579 to Bentley Mills Inc for FAC carpet tile supply (PoP Mexico); obligated USD 26,180. CapEx face = award obligation. Exact building unnamed — lat/lon blank.',
    "26180", "2016-06-15", "2016", "", "",
    'FAC carpet tile supply, Mexico (USASpending description; building not named — lat/lon blank).',
    "usaspending_bentley_mills_mexico_fac_carpet_tiles_26k_2016",
    'MEX/FAC/7901.C/CARPET TILE SUPPLY',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53016F0579_1900_SMX53015D0016_1900/",
    'Actor: Bentley Mills Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1117",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53016F0579_1900_SMX53015D0016_1900 (bentley_mills_mexico_fac_carpet_tiles_26k_2016). Signed 2016-06-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53016F0579_1900_SMX53015D0016_1900/.',
    'USASpending: bentley_mills_mexico_fac_carpet_tiles_26k_2016 USD 0.026m. Supports bentley_mills_mexico_fac_carpet_tiles_26k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 26180; date_signed 2016-06-15.',
)
row_doc(
    "syncroflo_honduras_obx_chancery_pump_heads_26k_2013",
    "resources", "water", "us",
    'Syncroflo — Honduras OBX/chancery water system pump heads',
    "Honduras",
    '10 Sep 2013: Department of State awards contract SHO80013M0788 to Syncroflo, Inc. for purchase of two pump heads water systems for OBX/chancery (PoP Honduras); obligated USD 25,650. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.',
    "25650", "2013-09-10", "2013", "", "",
    'Purchase of two pump heads water systems for OBX/chancery, Honduras (USASpending description; OBX/chancery named, site coords not stated — lat/lon blank).',
    "usaspending_syncroflo_honduras_obx_chancery_pump_heads_26k_2013",
    'IGF::CL::IGF PURCHASE OF TWO(2) PUMP HEADS WATER SYSTEMS FOR OBX/CHANCERY',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80013M0788_1900_-NONE-_-NONE-/",
    'Actor: Syncroflo, Inc. (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1117",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80013M0788_1900_-NONE-_-NONE- (syncroflo_honduras_obx_chancery_pump_heads_26k_2013). Signed 2013-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80013M0788_1900_-NONE-_-NONE-/.',
    'USASpending: syncroflo_honduras_obx_chancery_pump_heads_26k_2013 USD 0.026m. Supports syncroflo_honduras_obx_chancery_pump_heads_26k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 25650; date_signed 2013-09-10.',
)
row_doc(
    "misc_costa_rica_embassy_res_water_filter_install_37k_2012",
    "resources", "water", "other",
    'Miscellaneous foreign awardees — Costa Rica embassy residence water filter system installation',
    "Costa Rica",
    '2 Oct 2012: Department of State awards contract SCS80013C0005 for ICASS installation of water filter system for embassy residence (PoP Costa Rica); obligated USD 37,344.63. CapEx face = award obligation. Exact residence unnamed — lat/lon blank.',
    "37344.63", "2012-10-02", "2012", "", "",
    'Installation of water filter system for embassy residence, Costa Rica (USASpending description; residence not named — lat/lon blank).',
    "usaspending_misc_costa_rica_embassy_res_water_filter_install_37k_2012",
    'ICASS/INSTALLATION OF WATER FILTER SYSTEM FOR EMBASSY RESD. IGF::CL::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80013C0005_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.',
    "hunt_cycle1117",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80013C0005_1900_-NONE-_-NONE- (misc_costa_rica_embassy_res_water_filter_install_37k_2012). Signed 2012-10-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80013C0005_1900_-NONE-_-NONE-/.',
    'USASpending: misc_costa_rica_embassy_res_water_filter_install_37k_2012 USD 0.037m. Supports misc_costa_rica_embassy_res_water_filter_install_37k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37344.63; date_signed 2012-10-02.',
)
row_doc(
    "misc_trinidad_car_park_awnings_install_37k_2022",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Trinidad and Tobago three car park awnings purchase and installation',
    "Trinidad and Tobago",
    '19 Apr 2022: Department of State awards contract 19TD5522P0145 for purchase and installation of three car park awnings (PoP Trinidad and Tobago); obligated USD 37,279.09. CapEx face = award obligation. Exact car park unnamed — lat/lon blank.',
    "37279.09", "2022-04-19", "2022", "", "",
    'Purchase and installation of three car park awnings, Trinidad and Tobago (USASpending description; car park not named — lat/lon blank).',
    "usaspending_misc_trinidad_car_park_awnings_install_37k_2022",
    'PURCHASE AND INSTALLATION OF THREE CAR PARK AWNINGS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5522P0145_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1117",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19TD5522P0145_1900_-NONE-_-NONE- (misc_trinidad_car_park_awnings_install_37k_2022). Signed 2022-04-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5522P0145_1900_-NONE-_-NONE-/.',
    'USASpending: misc_trinidad_car_park_awnings_install_37k_2022 USD 0.037m. Supports misc_trinidad_car_park_awnings_install_37k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37279.09; date_signed 2022-04-19.',
)
row_doc(
    "misc_belize_pool_resurfacing_37k_2021",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Belize pool resurfacing',
    "Belize",
    '30 Sep 2021: Department of State awards contract 19BH2021P0200 for pool resurfacing (PoP Belize); obligated USD 37,250. CapEx face = award obligation. Exact pool unnamed — lat/lon blank.',
    "37250", "2021-09-30", "2021", "", "",
    'Pool resurfacing, Belize (USASpending description; pool not named — lat/lon blank).',
    "usaspending_misc_belize_pool_resurfacing_37k_2021",
    'POOL RESURFACING',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BH2021P0200_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1117",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BH2021P0200_1900_-NONE-_-NONE- (misc_belize_pool_resurfacing_37k_2021). Signed 2021-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BH2021P0200_1900_-NONE-_-NONE-/.',
    'USASpending: misc_belize_pool_resurfacing_37k_2021 USD 0.037m. Supports misc_belize_pool_resurfacing_37k_2021.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37250; date_signed 2021-09-30.',
)

# === Cycle 1118 (seed 20262118) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "interface_mexico_niv_carpet_25k_2012",
    "infrastructure", "building_materials", "us",
    'Interface Americas — Mexico NIV carpet',
    "Mexico",
    '21 Sep 2012: Department of State awards contract SMX53012M2044 to Interface Americas Inc for NIV carpet (PoP Mexico); obligated USD 25,278. CapEx face = award obligation. Exact NIV unnamed — lat/lon blank.',
    "25278", "2012-09-21", "2012", "", "",
    'NIV carpet, Mexico (USASpending description; NIV named, site coords not stated — lat/lon blank).',
    "usaspending_interface_mexico_niv_carpet_25k_2012",
    'MEX-NIV CARPET IGF::OT::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M2044_1900_-NONE-_-NONE-/",
    'Actor: Interface Americas Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1118",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53012M2044_1900_-NONE-_-NONE- (interface_mexico_niv_carpet_25k_2012). Signed 2012-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M2044_1900_-NONE-_-NONE-/.',
    'USASpending: interface_mexico_niv_carpet_25k_2012 USD 0.025m. Supports interface_mexico_niv_carpet_25k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 25278; date_signed 2012-09-21.',
)
row_doc(
    "balco_panama_nec_submersible_ss_pump_25k_2013",
    "resources", "water", "us",
    'Balco — Panama NEC submersible SS pump replacement',
    "Panama",
    '20 Sep 2013: Department of State awards contract SPM07013M0811 to Balco LLC for submersible SS pump NEC OBO replacement (PoP Panama); obligated USD 25,235. CapEx face = award obligation. NEC named; site coords not stated — lat/lon blank.',
    "25235", "2013-09-20", "2013", "", "",
    'Submersible SS pump NEC OBO replacement, Panama (USASpending description; NEC named, site coords not stated — lat/lon blank).',
    "usaspending_balco_panama_nec_submersible_ss_pump_25k_2013",
    'SUBMERSIBLE SS PUMP - NEC - OBO 7901.C (REPLACEMENT)',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07013M0811_1900_-NONE-_-NONE-/",
    'Actor: Balco LLC (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1118",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07013M0811_1900_-NONE-_-NONE- (balco_panama_nec_submersible_ss_pump_25k_2013). Signed 2013-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07013M0811_1900_-NONE-_-NONE-/.',
    'USASpending: balco_panama_nec_submersible_ss_pump_25k_2013 USD 0.025m. Supports balco_panama_nec_submersible_ss_pump_25k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 25235; date_signed 2013-09-20.',
)
row_doc(
    "misc_costa_rica_inl_electrical_generator_k35_37k_2016",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Costa Rica INL electrical generator K-35',
    "Costa Rica",
    '26 Feb 2016: Department of State awards contract SCS80016M0195 for INL electrical generator K-35 IN13CRNB 14 (PoP Costa Rica); obligated USD 37,291.08. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "37291.08", "2016-02-26", "2016", "", "",
    'INL electrical generator K-35 IN13CRNB 14, Costa Rica (USASpending description; project code named, site coords not stated — lat/lon blank).',
    "usaspending_misc_costa_rica_inl_electrical_generator_k35_37k_2016",
    'INL/1930.0  ELECTRICAL GENERATOR K-35 IN13CRNB 14',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80016M0195_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1118",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80016M0195_1900_-NONE-_-NONE- (misc_costa_rica_inl_electrical_generator_k35_37k_2016). Signed 2016-02-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80016M0195_1900_-NONE-_-NONE-/.',
    'USASpending: misc_costa_rica_inl_electrical_generator_k35_37k_2016 USD 0.037m. Supports misc_costa_rica_inl_electrical_generator_k35_37k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37291.08; date_signed 2016-02-26.',
)
row_doc(
    "misc_mexico_cg_residence_generator_install_37k_2019",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Mexico Merida OBO generator installation at CG residence',
    "Mexico",
    '13 Dec 2019: Department of State awards contract 19MX5220C0001 for Merida OBO delivery and installation of generator at CG residence (PoP Mexico); obligated USD 37,068.08. CapEx face = award obligation. Exact CG residence unnamed — lat/lon blank.',
    "37068.08", "2019-12-13", "2019", "", "",
    'Delivery and installation of generator at CG residence, Mexico (USASpending description; CG residence named, site coords not stated — lat/lon blank).',
    "usaspending_misc_mexico_cg_residence_generator_install_37k_2019",
    'MERIDA OBO - DELIVERY, INSTALLATION OF GENERATOR AT CG\'S RESIDENCE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5220C0001_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1118",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5220C0001_1900_-NONE-_-NONE- (misc_mexico_cg_residence_generator_install_37k_2019). Signed 2019-12-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5220C0001_1900_-NONE-_-NONE-/.',
    'USASpending: misc_mexico_cg_residence_generator_install_37k_2019 USD 0.037m. Supports misc_mexico_cg_residence_generator_install_37k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37068.08; date_signed 2019-12-13.',
)
row_doc(
    "misc_panama_yaviza_barracks_renovation_32k_2010",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Panama Yaviza barracks renovation',
    "Panama",
    '25 Feb 2010: Department of Defense awards contract W912CL10C0006 for Yaviza barracks renovation (PoP Panama); obligated USD 32,416.81. CapEx face = award obligation. Yaviza named; site coords not stated — lat/lon blank.',
    "32416.81", "2010-02-25", "2010", "", "",
    'Yaviza barracks renovation, Panama (USASpending description; Yaviza named, site coords not stated — lat/lon blank).',
    "usaspending_misc_panama_yaviza_barracks_renovation_32k_2010",
    'YAVIZA BARRACKS RENOVATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0006_9700_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1118",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0006_9700_-NONE-_-NONE- (misc_panama_yaviza_barracks_renovation_32k_2010). Signed 2010-02-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0006_9700_-NONE-_-NONE-/.',
    'USASpending: misc_panama_yaviza_barracks_renovation_32k_2010 USD 0.032m. Supports misc_panama_yaviza_barracks_renovation_32k_2010.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 32416.81; date_signed 2010-02-25.',
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
