#!/usr/bin/env python3
"""Cycles 1101–1103: USASpending LatAm CapEx residual (~USD0.031–0.054m).

Seeds: 20262101–20262103. Thin top-up dry.
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


# === Cycle 1101 (seed 20262101) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "ptg_mexico_tss_system_installation_44k_2020",
    "infrastructure", "building_materials", "us",
    'Professional Technologies Group — Mexico technical security services system installation',
    "Mexico",
    '6 Jan 2020: Department of State awards order 19AQMM20F0420 under IDV 19AQMM19D0009 to Professional Technologies Group, Inc. for technical security services system installation (PoP Mexico); obligated USD 44,116.44. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "44116.44", "2020-01-06", "2020", "", "",
    'Technical security services system installation, Mexico (USASpending description; site not named — lat/lon blank).',
    "usaspending_ptg_mexico_tss_system_installation_44k_2020",
    'TECHNICAL SECURITY SERVICES SYSTEM INSTALLATION.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F0420_1900_19AQMM19D0009_1900/",
    'Actor: Professional Technologies Group, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1101",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20F0420_1900_19AQMM19D0009_1900 (ptg_mexico_tss_system_installation_44k_2020). Signed 2020-01-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20F0420_1900_19AQMM19D0009_1900/.',
    'USASpending: ptg_mexico_tss_system_installation_44k_2020 USD 0.044m. Supports ptg_mexico_tss_system_installation_44k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 44116.44; date_signed 2020-01-06.',
)
row_doc(
    "usmax_mexico_tss_installation_43k_2022",
    "infrastructure", "building_materials", "us",
    'USMAX Corporation — Mexico technical security system installation',
    "Mexico",
    '20 Aug 2022: Department of State awards order 19AQMM22F3067 under IDV 19AQMM19D0007 to USMAX Corporation for technical security system installation (PoP Mexico); obligated USD 43,296.44. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "43296.44", "2022-08-20", "2022", "", "",
    'Technical security system installation, Mexico (USASpending description; site not named — lat/lon blank).',
    "usaspending_usmax_mexico_tss_installation_43k_2022",
    'TECHNICAL SECURITY SYSTEM INSTALLATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F3067_1900_19AQMM19D0007_1900/",
    'Actor: USMAX Corporation (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1101",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F3067_1900_19AQMM19D0007_1900 (usmax_mexico_tss_installation_43k_2022). Signed 2022-08-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F3067_1900_19AQMM19D0007_1900/.',
    'USASpending: usmax_mexico_tss_installation_43k_2022 USD 0.043m. Supports usmax_mexico_tss_installation_43k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 43296.44; date_signed 2022-08-20.',
)
row_doc(
    "misc_dr_construction_materials_54k_2023",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Dominican Republic construction materials',
    "Dominican Republic",
    '26 Jun 2023: Department of State awards contract 19DR8623P1148 for construction materials (PoP Dominican Republic); obligated USD 53,570.67. CapEx face = award obligation. Exact project site unnamed — lat/lon blank.',
    "53570.67", "2023-06-26", "2023", "", "",
    'Construction materials, Dominican Republic (USASpending description; site not named — lat/lon blank).',
    "usaspending_misc_dr_construction_materials_54k_2023",
    'CONSTRUCTION MATERIALS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623P1148_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1101",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8623P1148_1900_-NONE-_-NONE- (misc_dr_construction_materials_54k_2023). Signed 2023-06-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623P1148_1900_-NONE-_-NONE-/.',
    'USASpending: misc_dr_construction_materials_54k_2023 USD 0.054m. Supports misc_dr_construction_materials_54k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53570.67; date_signed 2023-06-26.',
)
row_doc(
    "misc_brazil_rec_center_fence_repair_54k_2019",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil rec center area fence repair',
    "Brazil",
    '13 Sep 2019: Department of State awards contract 19BR9319P0904 for fence repair rec center area (PoP Brazil); obligated USD 53,507.56. CapEx face = award obligation. Exact fence unnamed — lat/lon blank.',
    "53507.56", "2019-09-13", "2019", "", "",
    'Fence repair — rec center area, Brazil (USASpending description; rec center named, site coords not stated — lat/lon blank).',
    "usaspending_misc_brazil_rec_center_fence_repair_54k_2019",
    'FENCE REPAIR - REC CENTER AREA',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9319P0904_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1101",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9319P0904_1900_-NONE-_-NONE- (misc_brazil_rec_center_fence_repair_54k_2019). Signed 2019-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9319P0904_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_rec_center_fence_repair_54k_2019 USD 0.054m. Supports misc_brazil_rec_center_fence_repair_54k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53507.56; date_signed 2019-09-13.',
)
row_doc(
    "misc_mexico_wood_flooring_gov_properties_53k_2013",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Mexico wood flooring for government-owned properties',
    "Mexico",
    '27 Feb 2013: Department of State awards contract SMX53013M0446 for wood flooring for government owned properties (PoP Mexico); obligated USD 53,227.65. CapEx face = award obligation. Exact properties unnamed — lat/lon blank.',
    "53227.65", "2013-02-27", "2013", "", "",
    'Wood flooring for government-owned properties, Mexico (USASpending description; properties not named — lat/lon blank).',
    "usaspending_misc_mexico_wood_flooring_gov_properties_53k_2013",
    'MEX-FAC-7901/ WOOD FLOORING FOR GOVERNMENT OWNED PROPERTIES IGF::OT::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0446_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1101",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53013M0446_1900_-NONE-_-NONE- (misc_mexico_wood_flooring_gov_properties_53k_2013). Signed 2013-02-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0446_1900_-NONE-_-NONE-/.',
    'USASpending: misc_mexico_wood_flooring_gov_properties_53k_2013 USD 0.053m. Supports misc_mexico_wood_flooring_gov_properties_53k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53227.65; date_signed 2013-02-27.',
)

# === Cycle 1102 (seed 20262102) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "wecsys_colombia_armstrong_ceiling_tiles_41k_2012",
    "infrastructure", "building_materials", "us",
    'Wecsys — Colombia Armstrong ceiling tiles',
    "Colombia",
    '27 Sep 2012: Department of State awards order SCO20012F0012 under IDV GS06F0049S to Wecsys LLC for Armstrong 589B ceiling tile (PoP Colombia); obligated USD 41,496. CapEx face = award obligation. Exact office unnamed — lat/lon blank.',
    "41496", "2012-09-27", "2012", "", "",
    'Armstrong 589B ceiling tile, Colombia (USASpending description; office not named — lat/lon blank).',
    "usaspending_wecsys_colombia_armstrong_ceiling_tiles_41k_2012",
    'ARMSTRONG 589B CEILING TILE 24X24 IN, 3/4 IN T, PK 12 WHITE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012F0012_1900_GS06F0049S_4730/",
    'Actor: Wecsys LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1102",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20012F0012_1900_GS06F0049S_4730 (wecsys_colombia_armstrong_ceiling_tiles_41k_2012). Signed 2012-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012F0012_1900_GS06F0049S_4730/.',
    'USASpending: wecsys_colombia_armstrong_ceiling_tiles_41k_2012 USD 0.041m. Supports wecsys_colombia_armstrong_ceiling_tiles_41k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 41496; date_signed 2012-09-27.',
)
row_doc(
    "fluid_solutions_jamaica_fire_pump_controllers_37k_2026",
    "energy", "power_plants_grid", "us",
    'Fluid Solutions — Jamaica fire pump controllers',
    "Jamaica",
    '26 Aug 2026: Department of State awards contract 19JM3726P0989 to Fluid Solutions LLC for fire pump controllers (PoP Jamaica); obligated USD 37,055.87. CapEx face = award obligation. Exact pump room unnamed — lat/lon blank.',
    "37055.87", "2026-08-26", "2026", "", "",
    'Fire pump controllers, Jamaica (USASpending description; site not named — lat/lon blank).',
    "usaspending_fluid_solutions_jamaica_fire_pump_controllers_37k_2026",
    'FAC - FIRE PUMP CONTROLLERS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3726P0989_1900_-NONE-_-NONE-/",
    'Actor: Fluid Solutions LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1102",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3726P0989_1900_-NONE-_-NONE- (fluid_solutions_jamaica_fire_pump_controllers_37k_2026). Signed 2026-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3726P0989_1900_-NONE-_-NONE-/.',
    'USASpending: fluid_solutions_jamaica_fire_pump_controllers_37k_2026 USD 0.037m. Supports fluid_solutions_jamaica_fire_pump_controllers_37k_2026.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37055.87; date_signed 2026-08-26.',
)
row_doc(
    "misc_colombia_carimagua_electrical_materials_53k_2012",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Colombia COLAR AV electrical materials mobile base Carimagua',
    "Colombia",
    '20 Nov 2012: Department of State awards contract SCO15013M0172 for COLAR AV electrical materials mobile base phase Carimagua (PoP Colombia); obligated USD 53,290.64. CapEx face = award obligation. Exact Carimagua site unnamed — lat/lon blank.',
    "53290.64", "2012-11-20", "2012", "", "",
    'COLAR AV electrical materials mobile base phase Carimagua, Colombia (USASpending description; Carimagua named, site coords not stated — lat/lon blank).',
    "usaspending_misc_colombia_carimagua_electrical_materials_53k_2012",
    'COLAR AV ELECTRICAL MATERIALS MOBILE BASE PHASE CARIMAGUA',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0172_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1102",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15013M0172_1900_-NONE-_-NONE- (misc_colombia_carimagua_electrical_materials_53k_2012). Signed 2012-11-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0172_1900_-NONE-_-NONE-/.',
    'USASpending: misc_colombia_carimagua_electrical_materials_53k_2012 USD 0.053m. Supports misc_colombia_carimagua_electrical_materials_53k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53290.64; date_signed 2012-11-20.',
)
row_doc(
    "misc_peru_palmapampa_roof_gutters_53k_2015",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Peru Palmapampa antidrug base roof gutters repairs',
    "Peru",
    '29 Dec 2015: Department of State awards contract SPE50016C0004 for roof gutters repairs at Palmapampa antidrug base (PoP Peru); obligated USD 53,100. CapEx face = award obligation. Exact base unnamed beyond Palmapampa — lat/lon blank.',
    "53100", "2015-12-29", "2015", "", "",
    'Roof gutters repairs — Palmapampa antidrug base, Peru (USASpending description; Palmapampa named, site coords not stated — lat/lon blank).',
    "usaspending_misc_peru_palmapampa_roof_gutters_53k_2015",
    'ROOF GUTTERS REPAIRS-PALMAPAMPA ANTIDRUG BASE IGF::OT::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0004_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1102",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50016C0004_1900_-NONE-_-NONE- (misc_peru_palmapampa_roof_gutters_53k_2015). Signed 2015-12-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0004_1900_-NONE-_-NONE-/.',
    'USASpending: misc_peru_palmapampa_roof_gutters_53k_2015 USD 0.053m. Supports misc_peru_palmapampa_roof_gutters_53k_2015.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53100; date_signed 2015-12-29.',
)
row_doc(
    "misc_peru_dcr_kitchen_renovation_53k_2010",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Peru DCR kitchen renovation',
    "Peru",
    '7 Jul 2010: Department of State awards contract SPE50010C0047 for DCR kitchen renovation (PoP Peru); obligated USD 52,961.48. CapEx face = award obligation. Exact kitchen unnamed — lat/lon blank.',
    "52961.48", "2010-07-07", "2010", "", "",
    'DCR kitchen renovation, Peru (USASpending description; kitchen not named — lat/lon blank).',
    "usaspending_misc_peru_dcr_kitchen_renovation_53k_2010",
    '06/24 DCR - KITCHEN RENOVATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50010C0047_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1102",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50010C0047_1900_-NONE-_-NONE- (misc_peru_dcr_kitchen_renovation_53k_2010). Signed 2010-07-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50010C0047_1900_-NONE-_-NONE-/.',
    'USASpending: misc_peru_dcr_kitchen_renovation_53k_2010 USD 0.053m. Supports misc_peru_dcr_kitchen_renovation_53k_2010.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 52961.48; date_signed 2010-07-07.',
)

# === Cycle 1103 (seed 20262103) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "interface_colombia_carpet_tiles_milgroup_31k_2012",
    "infrastructure", "building_materials", "us",
    'Interface Flooring Systems — Colombia carpet tiles and adhesive for program and Milgroup offices',
    "Colombia",
    '28 Sep 2012: Department of State awards order SCO20012F0014 under IDV GS27F002A to Interface Flooring Systems Inc for EOY carpet tiles and adhesive for program and Milgroup offices (PoP Colombia); obligated USD 31,397.16. CapEx face = award obligation. Exact offices unnamed — lat/lon blank.',
    "31397.16", "2012-09-28", "2012", "", "",
    'Carpet tiles and adhesive for program and Milgroup offices, Colombia (USASpending description; offices not named — lat/lon blank).',
    "usaspending_interface_colombia_carpet_tiles_milgroup_31k_2012",
    'EOY CARPET TILES AND ADHESIVE FOR PROGRAM AND MILGROUP OFFICES IGF::CL::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012F0014_1900_GS27F002A_4730/",
    'Actor: Interface Flooring Systems Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1103",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20012F0014_1900_GS27F002A_4730 (interface_colombia_carpet_tiles_milgroup_31k_2012). Signed 2012-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012F0014_1900_GS27F002A_4730/.',
    'USASpending: interface_colombia_carpet_tiles_milgroup_31k_2012 USD 0.031m. Supports interface_colombia_carpet_tiles_milgroup_31k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 31397.16; date_signed 2012-09-28.',
)
row_doc(
    "kimball_paraguay_roof_skylights_b125_31k_2010",
    "infrastructure", "building_materials", "us",
    'L. Robert Kimball & Associates — Paraguay roof/skylights B125 project JLSS 06-0008',
    "Paraguay",
    '10 Mar 2010: Department of Defense awards order 0007 under IDV FA671207D0002 to L. Robert Kimball & Associates, Inc. for project JLSS 06-0008 roof/skylights B125 (PoP Paraguay); obligated USD 31,011.31. CapEx face = award obligation. Exact B125 site unnamed — lat/lon blank.',
    "31011.31", "2010-03-10", "2010", "", "",
    'Project JLSS 06-0008 roof/skylights B125, Paraguay (USASpending description; B125 named, site coords not stated — lat/lon blank).',
    "usaspending_kimball_paraguay_roof_skylights_b125_31k_2010",
    'PROJECT JLSS 06-0008 ROOF/SKYLIGHTS B125',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_FA671207D0002_9700/",
    'Actor: L. Robert Kimball & Associates, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1103",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0007_9700_FA671207D0002_9700 (kimball_paraguay_roof_skylights_b125_31k_2010). Signed 2010-03-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0007_9700_FA671207D0002_9700/.',
    'USASpending: kimball_paraguay_roof_skylights_b125_31k_2010 USD 0.031m. Supports kimball_paraguay_roof_skylights_b125_31k_2010.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 31011.31; date_signed 2010-03-10.',
)
row_doc(
    "misc_brazil_cmr_tennis_court_renovation_53k_2019",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil CMR tennis court renovation',
    "Brazil",
    '12 Aug 2019: Department of State awards contract 19BR2519P0970 for CMR tennis court renovation (PoP Brazil); obligated USD 52,949.20. CapEx face = award obligation. Exact court unnamed — lat/lon blank.',
    "52949.20", "2019-08-12", "2019", "", "",
    'CMR tennis court renovation, Brazil (USASpending description; CMR named, court coords not stated — lat/lon blank).',
    "usaspending_misc_brazil_cmr_tennis_court_renovation_53k_2019",
    'CMR - TENNIS COURT RENOVATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0970_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1103",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2519P0970_1900_-NONE-_-NONE- (misc_brazil_cmr_tennis_court_renovation_53k_2019). Signed 2019-08-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0970_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_cmr_tennis_court_renovation_53k_2019 USD 0.053m. Supports misc_brazil_cmr_tennis_court_renovation_53k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 52949.20; date_signed 2019-08-12.',
)
row_doc(
    "carlos_grenada_south_st_george_electrical_53k_2016",
    "energy", "power_plants_grid", "other",
    'Carlos Electrical — Grenada South St. George police station electrical repairs',
    "Grenada",
    '15 Aug 2016: Department of State awards contract SBB21016M0769 to Carlos Electrical for INL electrical repairs at South St. George police station (PoP Grenada); obligated USD 52,895.32. CapEx face = award obligation. Exact station unnamed beyond South St. George — lat/lon blank.',
    "52895.32", "2016-08-15", "2016", "", "",
    'Electrical repairs at South St. George police station, Grenada (USASpending description; South St. George named, site coords not stated — lat/lon blank).',
    "usaspending_carlos_grenada_south_st_george_electrical_53k_2016",
    'INL: ELECTRICAL REPAIRS/SOUTH ST. GEORGE POLICE STATION/GND IGF::CL::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21016M0769_1900_-NONE-_-NONE-/",
    'Actor: Carlos Electrical (Grenada) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1103",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21016M0769_1900_-NONE-_-NONE- (carlos_grenada_south_st_george_electrical_53k_2016). Signed 2016-08-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21016M0769_1900_-NONE-_-NONE-/.',
    'USASpending: carlos_grenada_south_st_george_electrical_53k_2016 USD 0.053m. Supports carlos_grenada_south_st_george_electrical_53k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 52895.32; date_signed 2016-08-15.',
)
row_doc(
    "misc_ecuador_check_valves_install_53k_2023",
    "resources", "water", "other",
    'Miscellaneous foreign awardees — Ecuador supply and installation of check valves',
    "Ecuador",
    '29 Sep 2023: Department of State awards contract 19EC3023P0855 for supply and installation of check valves (PoP Ecuador); obligated USD 53,497.94. CapEx face = award obligation. Exact valve sites unnamed — lat/lon blank.',
    "53497.94", "2023-09-29", "2023", "", "",
    'Supply and installation of check valves, Ecuador (USASpending description; sites not named — lat/lon blank).',
    "usaspending_misc_ecuador_check_valves_install_53k_2023",
    'SUPPLY & INSTALLATION OF CHECK VALVES',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3023P0855_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.',
    "hunt_cycle1103",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3023P0855_1900_-NONE-_-NONE- (misc_ecuador_check_valves_install_53k_2023). Signed 2023-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3023P0855_1900_-NONE-_-NONE-/.',
    'USASpending: misc_ecuador_check_valves_install_53k_2023 USD 0.053m. Supports misc_ecuador_check_valves_install_53k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53497.94; date_signed 2023-09-29.',
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
