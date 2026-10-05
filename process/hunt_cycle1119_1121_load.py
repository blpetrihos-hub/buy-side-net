#!/usr/bin/env python3
"""Cycles 1119–1121: USASpending LatAm CapEx residual (~USD0.025–0.038m).

Seeds: 20262119–20262121. Thin top-up dry.
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


# === Cycle 1119 (seed 20262119) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "frazier_dominican_republic_ac_ladders_offices_28k_2011",
    "energy", "power_plants_grid", "us",
    'J.R. Frazier Enterprises — Dominican Republic A/Cs 5 tons and ladders for offices',
    "Dominican Republic",
    '21 Sep 2011: USAID awards contract AID517O1100096 to J.R. Frazier Enterprises, Inc. for A/Cs, 5 tons and ladders for offices (PoP Dominican Republic); obligated USD 27,971.35. CapEx face = award obligation. Exact offices unnamed — lat/lon blank.',
    "27971.35", "2011-09-21", "2011", "", "",
    'A/Cs, 5 tons and ladders for offices, Dominican Republic (USASpending description; offices not named — lat/lon blank).',
    "usaspending_frazier_dominican_republic_ac_ladders_offices_28k_2011",
    'A/CS, 5 TONS AND LADDERS FOR OFFICES.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID517O1100096_7200_-NONE-_-NONE-/",
    'Actor: J.R. Frazier Enterprises, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1119",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID517O1100096_7200_-NONE-_-NONE- (frazier_dominican_republic_ac_ladders_offices_28k_2011). Signed 2011-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID517O1100096_7200_-NONE-_-NONE-/.',
    'USASpending: frazier_dominican_republic_ac_ladders_offices_28k_2011 USD 0.028m. Supports frazier_dominican_republic_ac_ladders_offices_28k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27971.35; date_signed 2011-09-21.',
)
row_doc(
    "aes_brazil_sao_paulo_security_installation_28k_2012",
    "infrastructure", "building_materials", "us",
    'AES Corporation — Brazil Sao Paulo security installation',
    "Brazil",
    '27 Nov 2012: Department of State awards contract SAQMMA13F0177 to AES Corporation for security installation Sao Paulo, Brazil (PoP Brazil); obligated USD 27,939.09. CapEx face = award obligation. Sao Paulo named; site coords not stated — lat/lon blank.',
    "27939.09", "2012-11-27", "2012", "", "",
    'Security installation Sao Paulo, Brazil (USASpending description; Sao Paulo named, site coords not stated — lat/lon blank).',
    "usaspending_aes_brazil_sao_paulo_security_installation_28k_2012",
    'SECURITY INSTALLATION SAO PAULO, BRAZIL IGF::CL::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F0177_1900_SAQMMA07D0031_1900/",
    'Actor: AES Corporation (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1119",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F0177_1900_SAQMMA07D0031_1900 (aes_brazil_sao_paulo_security_installation_28k_2012). Signed 2012-11-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F0177_1900_SAQMMA07D0031_1900/.',
    'USASpending: aes_brazil_sao_paulo_security_installation_28k_2012 USD 0.028m. Supports aes_brazil_sao_paulo_security_installation_28k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27939.09; date_signed 2012-11-27.',
)
row_doc(
    "misc_ecuador_asphalt_road_repair_38k_2021",
    "infrastructure", "bridges_roads", "other",
    'Miscellaneous foreign awardees — Ecuador asphalt road repair',
    "Ecuador",
    '2 Jul 2021: Department of State awards contract 19EC3021P0479 for asphalt road repair (PoP Ecuador); obligated USD 37,899.68. CapEx face = award obligation. Exact road unnamed — lat/lon blank.',
    "37899.68", "2021-07-02", "2021", "", "",
    'Asphalt road repair, Ecuador (USASpending description; road not named — lat/lon blank).',
    "usaspending_misc_ecuador_asphalt_road_repair_38k_2021",
    'ASPHALT ROAD REPAIR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3021P0479_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.',
    "hunt_cycle1119",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3021P0479_1900_-NONE-_-NONE- (misc_ecuador_asphalt_road_repair_38k_2021). Signed 2021-07-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3021P0479_1900_-NONE-_-NONE-/.',
    'USASpending: misc_ecuador_asphalt_road_repair_38k_2021 USD 0.038m. Supports misc_ecuador_asphalt_road_repair_38k_2021.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37899.68; date_signed 2021-07-02.',
)
row_doc(
    "perez_romo_mexico_carpet_floor_replace_38k_2019",
    "infrastructure", "building_materials", "other",
    'Jorge Eduardo Perez Romo — Mexico carpet floor replace gov prop 1001',
    "Mexico",
    '18 Jun 2019: Department of State awards contract 19MX1119P0223 to Jorge Eduardo Perez Romo for carpet floor replace gov prop 1001 (PoP Mexico); obligated USD 37,972.8. CapEx face = award obligation. Exact property unnamed — lat/lon blank.',
    "37972.8", "2019-06-18", "2019", "", "",
    'Carpet floor replace gov prop 1001, Mexico (USASpending description; property code named, site coords not stated — lat/lon blank).',
    "usaspending_perez_romo_mexico_carpet_floor_replace_38k_2019",
    'IGT::OT::IGT - CARPET FLOOR REPLACE GOV PROP 1001',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1119P0223_1900_-NONE-_-NONE-/",
    'Actor: Jorge Eduardo Perez Romo (Mexico) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1119",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX1119P0223_1900_-NONE-_-NONE- (perez_romo_mexico_carpet_floor_replace_38k_2019). Signed 2019-06-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1119P0223_1900_-NONE-_-NONE-/.',
    'USASpending: perez_romo_mexico_carpet_floor_replace_38k_2019 USD 0.038m. Supports perez_romo_mexico_carpet_floor_replace_38k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37972.8; date_signed 2019-06-18.',
)
row_doc(
    "misc_guatemala_public_ministry_renovation_materials_37k_2021",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Guatemala INL materials for renovation Public Ministry',
    "Guatemala",
    '26 Apr 2021: Department of State awards contract 19GT5021P0448 for INLG JSR OAP materials for renovation, Public Ministry (PoP Guatemala); obligated USD 37,219.67. CapEx face = award obligation. Public Ministry named; site coords not stated — lat/lon blank.',
    "37219.67", "2021-04-26", "2021", "", "",
    'Materials for renovation, Public Ministry, Guatemala (USASpending description; Public Ministry named, site coords not stated — lat/lon blank).',
    "usaspending_misc_guatemala_public_ministry_renovation_materials_37k_2021",
    'INLG JSR OAP MATERIALS FOR RENOVATION, PUBLIC MINISTRY',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5021P0448_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1119",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GT5021P0448_1900_-NONE-_-NONE- (misc_guatemala_public_ministry_renovation_materials_37k_2021). Signed 2021-04-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5021P0448_1900_-NONE-_-NONE-/.',
    'USASpending: misc_guatemala_public_ministry_renovation_materials_37k_2021 USD 0.037m. Supports misc_guatemala_public_ministry_renovation_materials_37k_2021.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37219.67; date_signed 2021-04-26.',
)

# === Cycle 1120 (seed 20262120) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "dynamic_insights_mexico_central_ups_batteries_28k_2023",
    "energy", "power_plants_grid", "us",
    'Dynamic Insights International — Mexico FAC replace central UPS batteries',
    "Mexico",
    '28 Sep 2023: Department of State awards contract 19MX5323P1771 to Dynamic Insights International LLC for replace central UPS batteries FY23 (PoP Mexico); obligated USD 27,760. CapEx face = award obligation. Exact chancery unnamed — lat/lon blank.',
    "27760", "2023-09-28", "2023", "", "",
    'Replace central UPS batteries FY23, Mexico (USASpending description; site not named — lat/lon blank).',
    "usaspending_dynamic_insights_mexico_central_ups_batteries_28k_2023",
    'MEX-FAC-7901S-CHA-REPLACE CENTRAL UPS BATTERIES-FY23',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5323P1771_1900_-NONE-_-NONE-/",
    'Actor: Dynamic Insights International LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1120",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5323P1771_1900_-NONE-_-NONE- (dynamic_insights_mexico_central_ups_batteries_28k_2023). Signed 2023-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5323P1771_1900_-NONE-_-NONE-/.',
    'USASpending: dynamic_insights_mexico_central_ups_batteries_28k_2023 USD 0.028m. Supports dynamic_insights_mexico_central_ups_batteries_28k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27760; date_signed 2023-09-28.',
)
row_doc(
    "tidewater_panama_annex_generator_fuel_tank_25k_2019",
    "resources", "water", "us",
    'Tidewater — Panama annex building generator fuel tank replacement',
    "Panama",
    '19 Aug 2019: Department of State awards contract 19PM0719P0884 to Tidewater, Inc. for annex building generator fuel tank replacement (PoP Panama); obligated USD 25,062.92. CapEx face = award obligation. Annex named; site coords not stated — lat/lon blank.',
    "25062.92", "2019-08-19", "2019", "", "",
    '19PM0719P0884 ANNEX BUILDING GENERATOR FUEL TANK REPLACEMENT / 7901',
    "usaspending_tidewater_panama_annex_generator_fuel_tank_25k_2019",
    '19PM0719P0884 ANNEX BUILDING GENERATOR FUEL TANK REPLACEMENT / 7901',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0884_1900_-NONE-_-NONE-/",
    'Actor: Tidewater, Inc. (U.S.) — us. Official USASpending Award API. Shuffle water; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1120",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0719P0884_1900_-NONE-_-NONE- (tidewater_panama_annex_generator_fuel_tank_25k_2019). Signed 2019-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0884_1900_-NONE-_-NONE-/.',
    'USASpending: tidewater_panama_annex_generator_fuel_tank_25k_2019 USD 0.025m. Supports tidewater_panama_annex_generator_fuel_tank_25k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 25062.92; date_signed 2019-08-19.',
)
row_doc(
    "misc_brazil_dcr_windows_doors_grills_replacement_37k_2020",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil DCR windows and doors grills replacement',
    "Brazil",
    '17 Sep 2020: Department of State awards contract 19BR2520P0810 for windows and doors grills replacement at DCR QI09-07-17 (PoP Brazil); obligated USD 36,762.19. CapEx face = award obligation. DCR named; site coords not stated — lat/lon blank.',
    "36762.19", "2020-09-17", "2020", "", "",
    'Windows and doors grills replacement at DCR QI09-07-17, Brazil (USASpending description; DCR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_brazil_dcr_windows_doors_grills_replacement_37k_2020",
    'FAC - WINDOWS&DOORS GRILLS REPLACEMENT AT DCR - QI09-07-17',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0810_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1120",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2520P0810_1900_-NONE-_-NONE- (misc_brazil_dcr_windows_doors_grills_replacement_37k_2020). Signed 2020-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0810_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_dcr_windows_doors_grills_replacement_37k_2020 USD 0.037m. Supports misc_brazil_dcr_windows_doors_grills_replacement_37k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36762.19; date_signed 2020-09-17.',
)
row_doc(
    "misc_brazil_embassy_sand_volleyball_court_37k_2012",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil embassy sand volleyball court build',
    "Brazil",
    '27 Sep 2012: Department of State awards contract SBR25012M2360 to build sand volleyball court ICASS (PoP Brazil); obligated USD 36,667.49. CapEx face = award obligation. Embassy named; site coords not stated — lat/lon blank.',
    "36667.49", "2012-09-27", "2012", "", "",
    'Build sand volleyball court, Brazil embassy (USASpending description; embassy named, site coords not stated — lat/lon blank).',
    "usaspending_misc_brazil_embassy_sand_volleyball_court_37k_2012",
    'EMBASSY- BUILD SAND VOLLEYBALL COURT- ICASS- PROC ACTION IGF::OT::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25012M2360_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1120",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25012M2360_1900_-NONE-_-NONE- (misc_brazil_embassy_sand_volleyball_court_37k_2012). Signed 2012-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25012M2360_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_embassy_sand_volleyball_court_37k_2012 USD 0.037m. Supports misc_brazil_embassy_sand_volleyball_court_37k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36667.49; date_signed 2012-09-27.',
)
row_doc(
    "misc_brazil_niv_refurbishment_addition_37k_2010",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil addition to NIV refurbishment work',
    "Brazil",
    '24 Nov 2010: Department of State awards contract SBR82011M1205 for addition to NIV refurbishment work (PoP Brazil); obligated USD 36,540. CapEx face = award obligation. Exact NIV unnamed — lat/lon blank.',
    "36540", "2010-11-24", "2010", "", "",
    'Addition to NIV refurbishment work, Brazil (USASpending description; NIV named, site coords not stated — lat/lon blank).',
    "usaspending_misc_brazil_niv_refurbishment_addition_37k_2010",
    'ADDITION TO NIV REFURBISHMENT WORK',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82011M1205_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1120",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82011M1205_1900_-NONE-_-NONE- (misc_brazil_niv_refurbishment_addition_37k_2010). Signed 2010-11-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82011M1205_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_niv_refurbishment_addition_37k_2010 USD 0.037m. Supports misc_brazil_niv_refurbishment_addition_37k_2010.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36540; date_signed 2010-11-24.',
)

# === Cycle 1121 (seed 20262121) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "hy_security_jamaica_cacs_gate_operators_25k_2013",
    "infrastructure", "building_materials", "us",
    'Hy-Security Gate — Jamaica CACS gate operators replacement',
    "Jamaica",
    '12 Aug 2013: Department of State awards contract SJM37013M0971 to Hy-Security Gate, Inc. for replacement for gate operators at CACS (PoP Jamaica); obligated USD 24,794. CapEx face = award obligation. CACS named; site coords not stated — lat/lon blank.',
    "24794", "2013-08-12", "2013", "", "",
    'Replacement for gate operators at CACS, Jamaica (USASpending description; CACS named, site coords not stated — lat/lon blank).',
    "usaspending_hy_security_jamaica_cacs_gate_operators_25k_2013",
    'IGF::OT::IGF FAC - REPLACEMENT FOR GATE OPERATORS AT CACS (7901.C)',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37013M0971_1900_-NONE-_-NONE-/",
    'Actor: Hy-Security Gate, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1121",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37013M0971_1900_-NONE-_-NONE- (hy_security_jamaica_cacs_gate_operators_25k_2013). Signed 2013-08-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37013M0971_1900_-NONE-_-NONE-/.',
    'USASpending: hy_security_jamaica_cacs_gate_operators_25k_2013 USD 0.025m. Supports hy_security_jamaica_cacs_gate_operators_25k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 24794; date_signed 2013-08-12.',
)
row_doc(
    "flex_court_colombia_outdoor_basketball_court_25k_2011",
    "infrastructure", "building_materials", "us",
    'Flex Court International — Colombia outdoor basketball court and logo',
    "Colombia",
    '31 Mar 2011: Department of Defense awards contract W913FT11P0084 to Flex Court International, Inc. for outdoor basketball court and logo (PoP Colombia); obligated USD 24,998.01. CapEx face = award obligation. Exact court site unnamed — lat/lon blank.',
    "24998.01", "2011-03-31", "2011", "", "",
    'Outdoor basketball court and logo, Colombia (USASpending description; site not named — lat/lon blank).',
    "usaspending_flex_court_colombia_outdoor_basketball_court_25k_2011",
    'OUTDOOR BASKETBALL COURT AND LOGO',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0084_9700_-NONE-_-NONE-/",
    'Actor: Flex Court International, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1121",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11P0084_9700_-NONE-_-NONE- (flex_court_colombia_outdoor_basketball_court_25k_2011). Signed 2011-03-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0084_9700_-NONE-_-NONE-/.',
    'USASpending: flex_court_colombia_outdoor_basketball_court_25k_2011 USD 0.025m. Supports flex_court_colombia_outdoor_basketball_court_25k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 24998.01; date_signed 2011-03-31.',
)
row_doc(
    "misc_costa_rica_dcmr_perimeter_wall_painting_36k_2018",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Costa Rica DCMR perimeter wall painting 2018',
    "Costa Rica",
    '1 Jun 2018: Department of State awards contract 19CS8018C0011 for DCMR perimeter wall painting 2018 (PoP Costa Rica); obligated USD 36,451.25. CapEx face = award obligation. Exact DCMR unnamed — lat/lon blank.',
    "36451.25", "2018-06-01", "2018", "", "",
    'DCMR perimeter wall painting 2018, Costa Rica (USASpending description; DCMR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_costa_rica_dcmr_perimeter_wall_painting_36k_2018",
    'FAC ST 1900.0 7355 DCMR PERIMETER WALL PAINTING 2018',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8018C0011_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1121",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8018C0011_1900_-NONE-_-NONE- (misc_costa_rica_dcmr_perimeter_wall_painting_36k_2018). Signed 2018-06-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8018C0011_1900_-NONE-_-NONE-/.',
    'USASpending: misc_costa_rica_dcmr_perimeter_wall_painting_36k_2018 USD 0.036m. Supports misc_costa_rica_dcmr_perimeter_wall_painting_36k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36451.25; date_signed 2018-06-01.',
)
row_doc(
    "misc_brazil_dcr_new_guard_booth_36k_2019",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil DCR build new guard booth',
    "Brazil",
    '19 Sep 2019: Department of State awards contract 19BR2519P1201 to build new guard booth at DCR (PoP Brazil); obligated USD 36,422.35. CapEx face = award obligation. DCR named; site coords not stated — lat/lon blank.',
    "36422.35", "2019-09-19", "2019", "", "",
    'Build new guard booth at DCR, Brazil (USASpending description; DCR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_brazil_dcr_new_guard_booth_36k_2019",
    'FAC - DCR - BUILD NEW GUARD BOOTH',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P1201_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1121",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2519P1201_1900_-NONE-_-NONE- (misc_brazil_dcr_new_guard_booth_36k_2019). Signed 2019-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P1201_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_dcr_new_guard_booth_36k_2019 USD 0.036m. Supports misc_brazil_dcr_new_guard_booth_36k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36422.35; date_signed 2019-09-19.',
)
row_doc(
    "marko_mexico_guadalajara_msgr_emergency_generator_37k_2020",
    "energy", "power_plants_grid", "other",
    'Grupo Constructor de Marko — Mexico Guadalajara MSGR emergency generator',
    "Mexico",
    '9 Nov 2020: Department of State awards contract 19MX3021P0022 to Grupo Constructor de Marko, S.A. de C.V. for emergency generator for the MSGR FY21 (PoP Mexico); obligated USD 36,808.57. CapEx face = award obligation. Exact MSGR unnamed — lat/lon blank.',
    "36808.57", "2020-11-09", "2020", "", "",
    'Emergency generator for the MSGR FY21, Guadalajara, Mexico (USASpending description; MSGR named, site coords not stated — lat/lon blank).',
    "usaspending_marko_mexico_guadalajara_msgr_emergency_generator_37k_2020",
    'GDL-OBO-FAC-EMERGENCY GENERATOR FOR THE MSGR-FY21',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX3021P0022_1900_-NONE-_-NONE-/",
    'Actor: Grupo Constructor de Marko, S.A. de C.V. (Mexico) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1121",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX3021P0022_1900_-NONE-_-NONE- (marko_mexico_guadalajara_msgr_emergency_generator_37k_2020). Signed 2020-11-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX3021P0022_1900_-NONE-_-NONE-/.',
    'USASpending: marko_mexico_guadalajara_msgr_emergency_generator_37k_2020 USD 0.037m. Supports marko_mexico_guadalajara_msgr_emergency_generator_37k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36808.57; date_signed 2020-11-09.',
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
