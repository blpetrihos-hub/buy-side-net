#!/usr/bin/env python3
"""Cycles 1098–1100: USASpending LatAm CapEx residual (~USD0.031–0.055m).

Seeds: 20262098–20262100. Thin top-up dry.
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


# === Cycle 1098 (seed 20262098) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "interface_colombia_usaid_carpet_34k_2014",
    "infrastructure", "building_materials", "us",
    'Interface Americas — Colombia USAID carpet purchase',
    "Colombia",
    '13 Mar 2014: Department of State awards contract SCO20014M0769 to Interface Americas Inc for USAID carpet purchase (PoP Colombia); obligated USD 34,458.24. CapEx face = award obligation. Exact office unnamed — lat/lon blank.',
    "34458.24", "2014-03-13", "2014", "", "",
    'USAID carpet purchase, Colombia (USASpending description; office not named — lat/lon blank).',
    "usaspending_interface_colombia_usaid_carpet_34k_2014",
    'IGF::CL::IGF USAID CARPET PURCHASE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20014M0769_1900_-NONE-_-NONE-/",
    'Actor: Interface Americas Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1098",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20014M0769_1900_-NONE-_-NONE- (interface_colombia_usaid_carpet_34k_2014). Signed 2014-03-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20014M0769_1900_-NONE-_-NONE-/.',
    'USASpending: interface_colombia_usaid_carpet_34k_2014 USD 0.034m. Supports interface_colombia_usaid_carpet_34k_2014.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 34458.24; date_signed 2014-03-13.',
)
row_doc(
    "clarke_brazil_fire_pump_drive_34k_2011",
    "energy", "power_plants_grid", "us",
    'Clarke Power Services — Brazil replacement fire pump drive',
    "Brazil",
    '16 Feb 2011: Department of State awards contract SBR25011M0671 to Clarke Power Services, Inc for replacement fire pump drive (PoP Brazil); obligated USD 34,220.20. CapEx face = award obligation. Exact pump site unnamed — lat/lon blank.',
    "34220.20", "2011-02-16", "2011", "", "",
    'Replacement fire pump drive, Brazil (USASpending description; site not named — lat/lon blank).',
    "usaspending_clarke_brazil_fire_pump_drive_34k_2011",
    'REPLACEMENT FIRE PUMP DRIVE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25011M0671_1900_-NONE-_-NONE-/",
    'Actor: Clarke Power Services, Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1098",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25011M0671_1900_-NONE-_-NONE- (clarke_brazil_fire_pump_drive_34k_2011). Signed 2011-02-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25011M0671_1900_-NONE-_-NONE-/.',
    'USASpending: clarke_brazil_fire_pump_drive_34k_2011 USD 0.034m. Supports clarke_brazil_fire_pump_drive_34k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 34220.20; date_signed 2011-02-16.',
)
row_doc(
    "mario_guatemala_aldea_euc_plumbing_55k_2019",
    "resources", "water", "other",
    'Mario Reginaldo Aguilar Galindo — Guatemala Aldea Eucalyptus school plumbing materials',
    "Guatemala",
    '25 Apr 2019: Department of Defense awards contract W912QM19P0029 to Mario Reginaldo Aguilar Galindo for Aldea Euc. school plumbing materials (PoP Guatemala); obligated USD 55,000. CapEx face = award obligation. Exact school site unnamed — lat/lon blank.',
    "55000", "2019-04-25", "2019", "", "",
    'Aldea Eucalyptus school plumbing materials, Guatemala (USASpending description; Aldea Euc named, site coords not stated — lat/lon blank).',
    "usaspending_mario_guatemala_aldea_euc_plumbing_55k_2019",
    'ALDEA EUC. SCHOOL PLUMBING MATERIALS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM19P0029_9700_-NONE-_-NONE-/",
    'Actor: Mario Reginaldo Aguilar Galindo (Honduras contractor; PoP Guatemala) — other. Official USASpending Award API. Shuffle water.',
    "hunt_cycle1098",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM19P0029_9700_-NONE-_-NONE- (mario_guatemala_aldea_euc_plumbing_55k_2019). Signed 2019-04-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM19P0029_9700_-NONE-_-NONE-/.',
    'USASpending: mario_guatemala_aldea_euc_plumbing_55k_2019 USD 0.055m. Supports mario_guatemala_aldea_euc_plumbing_55k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55000; date_signed 2019-04-25.',
)
row_doc(
    "misc_brazil_generation_day_tank_55k_2020",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Brazil generation day tank',
    "Brazil",
    '12 May 2020: Department of State awards contract 19BR9320P0309 for generation day tank (PoP Brazil); obligated USD 54,883.14. CapEx face = award obligation. Exact tank site unnamed — lat/lon blank.',
    "54883.14", "2020-05-12", "2020", "", "",
    'Generation day tank, Brazil (USASpending description; site not named — lat/lon blank).',
    "usaspending_misc_brazil_generation_day_tank_55k_2020",
    'GENERATION DAY TANK',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9320P0309_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1098",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9320P0309_1900_-NONE-_-NONE- (misc_brazil_generation_day_tank_55k_2020). Signed 2020-05-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9320P0309_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_generation_day_tank_55k_2020 USD 0.055m. Supports misc_brazil_generation_day_tank_55k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 54883.14; date_signed 2020-05-12.',
)
row_doc(
    "wkl_panama_door_relocation_wall_repair_54k_2016",
    "infrastructure", "building_materials", "other",
    'W.K.L. Arquitectos — Panama DHS door relocation and wall repair',
    "Panama",
    '19 Sep 2016: Department of State awards contract SPM07016M0777 to W.K.L. Arquitectos S.A. for DHS door relocation and wall repair (PoP Panama); obligated USD 54,275. CapEx face = award obligation. Exact DHS space unnamed — lat/lon blank.',
    "54275", "2016-09-19", "2016", "", "",
    'DHS door relocation and wall repair, Panama (USASpending description; site not named — lat/lon blank).',
    "usaspending_wkl_panama_door_relocation_wall_repair_54k_2016",
    'DHS DOOR RELOCATION AND WALL REPAIR - 7901.C (SPM07016Q0084) IGF::OT::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07016M0777_1900_-NONE-_-NONE-/",
    'Actor: W.K.L. Arquitectos S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1098",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07016M0777_1900_-NONE-_-NONE- (wkl_panama_door_relocation_wall_repair_54k_2016). Signed 2016-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07016M0777_1900_-NONE-_-NONE-/.',
    'USASpending: wkl_panama_door_relocation_wall_repair_54k_2016 USD 0.054m. Supports wkl_panama_door_relocation_wall_repair_54k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 54275; date_signed 2016-09-19.',
)

# === Cycle 1099 (seed 20262099) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "apollo_jamaica_motorpool_car_park_canopy_33k_2013",
    "infrastructure", "building_materials", "us",
    'Apollo Sunguard Systems — Jamaica motorpool car park canopy shades',
    "Jamaica",
    '30 Sep 2013: Department of State awards contract SJM37013M1071 to Apollo Sunguard Systems Inc for motorpool car park canopy shades (PoP Jamaica); obligated USD 33,160.22. CapEx face = award obligation. Exact motorpool unnamed — lat/lon blank.',
    "33160.22", "2013-09-30", "2013", "", "",
    'Motorpool car park canopy shades, Jamaica (USASpending description; motorpool not named — lat/lon blank).',
    "usaspending_apollo_jamaica_motorpool_car_park_canopy_33k_2013",
    'FAC - MOTORPOOL CAR PARK CANOPY SHADES - ICASS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37013M1071_1900_-NONE-_-NONE-/",
    'Actor: Apollo Sunguard Systems Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1099",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37013M1071_1900_-NONE-_-NONE- (apollo_jamaica_motorpool_car_park_canopy_33k_2013). Signed 2013-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37013M1071_1900_-NONE-_-NONE-/.',
    'USASpending: apollo_jamaica_motorpool_car_park_canopy_33k_2013 USD 0.033m. Supports apollo_jamaica_motorpool_car_park_canopy_33k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 33160.22; date_signed 2013-09-30.',
)
row_doc(
    "psi_mexico_semar_unopes_roof_materials_33k_2026",
    "infrastructure", "building_materials", "us",
    'Project Services International — Mexico SEMAR-UNOPES roof materials',
    "Mexico",
    '16 Mar 2026: Department of State awards contract 19MX9026P0033 to Project Services International Corporation, Inc for SEMAR-UNOPES roof materials WHP.MX.0268 (PoP Mexico); obligated USD 32,737.10. CapEx face = award obligation. Exact SEMAR-UNOPES site unnamed — lat/lon blank.',
    "32737.10", "2026-03-16", "2026", "", "",
    'SEMAR-UNOPES roof materials, Mexico (USASpending description; SEMAR-UNOPES named, site coords not stated — lat/lon blank).',
    "usaspending_psi_mexico_semar_unopes_roof_materials_33k_2026",
    'IN23MX66- ROOF MATERIALS SEMAR-UNOPES WHP.MX.0268',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX9026P0033_1900_-NONE-_-NONE-/",
    'Actor: Project Services International Corporation, Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1099",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX9026P0033_1900_-NONE-_-NONE- (psi_mexico_semar_unopes_roof_materials_33k_2026). Signed 2026-03-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX9026P0033_1900_-NONE-_-NONE-/.',
    'USASpending: psi_mexico_semar_unopes_roof_materials_33k_2026 USD 0.033m. Supports psi_mexico_semar_unopes_roof_materials_33k_2026.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 32737.10; date_signed 2026-03-16.',
)
row_doc(
    "misc_mexico_tile_floor_construction_54k_2025",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Mexico tile floor construction and improvement',
    "Mexico",
    '28 Apr 2025: Department of State awards contract 19MX1125P0113 for tile floor construction and improvement (PoP Mexico); obligated USD 53,985.29. CapEx face = award obligation. Exact floor unnamed — lat/lon blank.',
    "53985.29", "2025-04-28", "2025", "", "",
    'Tile floor construction and improvement, Mexico (USASpending description; site not named — lat/lon blank).',
    "usaspending_misc_mexico_tile_floor_construction_54k_2025",
    'IGT::OT::IGT TILE FLOOR CONSTRUCTION AND IMPROVEMENT',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1125P0113_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1099",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX1125P0113_1900_-NONE-_-NONE- (misc_mexico_tile_floor_construction_54k_2025). Signed 2025-04-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1125P0113_1900_-NONE-_-NONE-/.',
    'USASpending: misc_mexico_tile_floor_construction_54k_2025 USD 0.054m. Supports misc_mexico_tile_floor_construction_54k_2025.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53985.29; date_signed 2025-04-28.',
)
row_doc(
    "misc_costa_rica_coast_guard_generators_54k_2017",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Costa Rica INL purchase of two generators for coast guard',
    "Costa Rica",
    '25 Sep 2017: Department of State awards contract SCS80017M0061 for INL purchase of 2 generators for coast guard (PoP Costa Rica); obligated USD 53,966. CapEx face = award obligation. Exact coast-guard site unnamed — lat/lon blank.',
    "53966", "2017-09-25", "2017", "", "",
    'Purchase of 2 generators for coast guard, Costa Rica (USASpending description; site not named — lat/lon blank).',
    "usaspending_misc_costa_rica_coast_guard_generators_54k_2017",
    'INL PURCHASE OF 2 GENERATORS FOR COAST GUARD SNGC0369-2016',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80017M0061_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1099",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80017M0061_1900_-NONE-_-NONE- (misc_costa_rica_coast_guard_generators_54k_2017). Signed 2017-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80017M0061_1900_-NONE-_-NONE-/.',
    'USASpending: misc_costa_rica_coast_guard_generators_54k_2017 USD 0.054m. Supports misc_costa_rica_coast_guard_generators_54k_2017.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53966; date_signed 2017-09-25.',
)
row_doc(
    "misc_colombia_cartagena_ac_replace_54k_2018",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Colombia Cartagena embassy branch AC unit repair/replace',
    "Colombia",
    '16 Sep 2018: Department of State awards contract 19C02018P1082 to repair/replace AC units in Cartagena embassy branch (PoP Colombia); obligated USD 53,865.84. CapEx face = award obligation. Exact branch site unnamed — lat/lon blank.',
    "53865.84", "2018-09-16", "2018", "", "",
    'Repair/replace AC units in Cartagena embassy branch, Colombia (USASpending description; Cartagena named, site coords not stated — lat/lon blank).',
    "usaspending_misc_colombia_cartagena_ac_replace_54k_2018",
    'IGF::OT::IGF    PR7623914: REPAIR/REPLACE AC UNITS IN CARTAGENA EMBASSY BRANC',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02018P1082_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1099",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02018P1082_1900_-NONE-_-NONE- (misc_colombia_cartagena_ac_replace_54k_2018). Signed 2018-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02018P1082_1900_-NONE-_-NONE-/.',
    'USASpending: misc_colombia_cartagena_ac_replace_54k_2018 USD 0.054m. Supports misc_colombia_cartagena_ac_replace_54k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53865.84; date_signed 2018-09-16.',
)

# === Cycle 1100 (seed 20262100) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "alpha_tec_panama_building_59_flooring_32k_2022",
    "infrastructure", "building_materials", "us",
    'Alpha Tec Services — Panama flooring for refurbishment of Building #59',
    "Panama",
    '31 Aug 2022: Department of State awards contract 19PM0722P0889 to Alpha Tec Services Inc for flooring for refurbishment of Building #59 (PoP Panama); obligated USD 31,897. CapEx face = award obligation. Exact Building #59 site unnamed — lat/lon blank.',
    "31897", "2022-08-31", "2022", "", "",
    'Flooring for refurbishment of Building #59, Panama (USASpending description; Building #59 named, site coords not stated — lat/lon blank).',
    "usaspending_alpha_tec_panama_building_59_flooring_32k_2022",
    'FLOORING FOR REFURBISHMENT OF BUILDING #59',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0722P0889_1900_-NONE-_-NONE-/",
    'Actor: Alpha Tec Services Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1100",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0722P0889_1900_-NONE-_-NONE- (alpha_tec_panama_building_59_flooring_32k_2022). Signed 2022-08-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0722P0889_1900_-NONE-_-NONE-/.',
    'USASpending: alpha_tec_panama_building_59_flooring_32k_2022 USD 0.032m. Supports alpha_tec_panama_building_59_flooring_32k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 31897; date_signed 2022-08-31.',
)
row_doc(
    "ssi_peru_chancery_hvac_pumps_31k_2012",
    "energy", "power_plants_grid", "us",
    'Supplies & Services International — Peru chancery HVAC pump replacement',
    "Peru",
    '9 May 2012: Department of State awards contract SPE50012M0643 to Supplies & Services International Inc to replace HVAC pumps at chancery (PoP Peru); obligated USD 31,316.80. CapEx face = award obligation. Exact chancery unnamed — lat/lon blank.',
    "31316.80", "2012-05-09", "2012", "", "",
    'Replace HVAC pumps at chancery, Peru (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_ssi_peru_chancery_hvac_pumps_31k_2012",
    '4/30 FAC - REPLACE HVAC PUMPS AT CHANCERY',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50012M0643_1900_-NONE-_-NONE-/",
    'Actor: Supplies & Services International Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1100",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50012M0643_1900_-NONE-_-NONE- (ssi_peru_chancery_hvac_pumps_31k_2012). Signed 2012-05-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50012M0643_1900_-NONE-_-NONE-/.',
    'USASpending: ssi_peru_chancery_hvac_pumps_31k_2012 USD 0.031m. Supports ssi_peru_chancery_hvac_pumps_31k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 31316.80; date_signed 2012-05-09.',
)
row_doc(
    "misc_argentina_chancery_ext_paint_parking_54k_2018",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Argentina chancery exterior paint project and parking completion',
    "Argentina",
    '12 Sep 2018: Department of State awards contract 19AR2018P0880 for chancery completion of exterior paint project and parking (PoP Argentina); obligated USD 53,845. CapEx face = award obligation. Exact chancery unnamed — lat/lon blank.',
    "53845", "2018-09-12", "2018", "", "",
    'Chancery completion of exterior paint project and parking, Argentina (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_misc_argentina_chancery_ext_paint_parking_54k_2018",
    'FAC - CHANCERY - COMPLETION OF EXT PAINT PROJECT&PARKING',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P0880_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1100",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2018P0880_1900_-NONE-_-NONE- (misc_argentina_chancery_ext_paint_parking_54k_2018). Signed 2018-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P0880_1900_-NONE-_-NONE-/.',
    'USASpending: misc_argentina_chancery_ext_paint_parking_54k_2018 USD 0.054m. Supports misc_argentina_chancery_ext_paint_parking_54k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53845; date_signed 2018-09-12.',
)
row_doc(
    "mejores_panama_gamboa_bat_flight_cage_53k_2012",
    "infrastructure", "building_materials", "other",
    'Mejores Acabados — Panama Gamboa STRI bat flight cage construction',
    "Panama",
    '30 May 2012: Smithsonian awards contract F12CC10332 to Mejores Acabados S.A. to construct bat flight cage at Gamboa (STRI) (PoP Panama); obligated USD 53,009.93. CapEx face = award obligation. Exact cage footprint unnamed — lat/lon blank.',
    "53009.93", "2012-05-30", "2012", "", "",
    'Construct bat flight cage at Gamboa (STRI), Panama (USASpending description; Gamboa named, site coords not stated — lat/lon blank).',
    "usaspending_mejores_panama_gamboa_bat_flight_cage_53k_2012",
    'CONSTRUCT BAT FLIGHT CAGE AT GAMBOA (STRI)',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F12CC10332_3300_-NONE-_-NONE-/",
    'Actor: Mejores Acabados S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1100",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F12CC10332_3300_-NONE-_-NONE- (mejores_panama_gamboa_bat_flight_cage_53k_2012). Signed 2012-05-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F12CC10332_3300_-NONE-_-NONE-/.',
    'USASpending: mejores_panama_gamboa_bat_flight_cage_53k_2012 USD 0.053m. Supports mejores_panama_gamboa_bat_flight_cage_53k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53009.93; date_signed 2012-05-30.',
)
row_doc(
    "bolanos_ecuador_cmr_perimeter_wall_53k_2024",
    "infrastructure", "building_materials", "other",
    'Bolanos Alban Fausto Tarquino — Ecuador CMR perimeter wall repair',
    "Ecuador",
    '13 Sep 2024: Department of State awards contract 19EC7524C0018 to Bolanos Alban Fausto Tarquino for CMR perimeter wall repair (PoP Ecuador); obligated USD 53,240.05. CapEx face = award obligation. Exact wall segment unnamed — lat/lon blank.',
    "53240.05", "2024-09-13", "2024", "", "",
    'CMR perimeter wall repair, Ecuador (USASpending description; CMR named, wall coords not stated — lat/lon blank).',
    "usaspending_bolanos_ecuador_cmr_perimeter_wall_53k_2024",
    'FAC-7355SUST-CMR-PERIMETER WALL REPAIR AT CMR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7524C0018_1900_-NONE-_-NONE-/",
    'Actor: Bolanos Alban Fausto Tarquino (Ecuador) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1100",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7524C0018_1900_-NONE-_-NONE- (bolanos_ecuador_cmr_perimeter_wall_53k_2024). Signed 2024-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7524C0018_1900_-NONE-_-NONE-/.',
    'USASpending: bolanos_ecuador_cmr_perimeter_wall_53k_2024 USD 0.053m. Supports bolanos_ecuador_cmr_perimeter_wall_53k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53240.05; date_signed 2024-09-13.',
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
