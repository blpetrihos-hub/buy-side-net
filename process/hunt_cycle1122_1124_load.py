#!/usr/bin/env python3
"""Cycles 1122–1124: USASpending LatAm CapEx residual (~USD0.022–0.038m).

Seeds: 20262122–20262124. Thin top-up dry. Includes Venezuela gate operators.
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


# === Cycle 1122 (seed 20262122) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "hy_security_colombia_barrier_gate_equipment_25k_2015",
    "infrastructure", "building_materials", "us",
    'Hy-Security Gate — Colombia Delta/HySecurity barrier and gate equipment',
    "Colombia",
    '29 Sep 2015: Department of State awards contract SCO20015M1575 to Hy-Security Gate, Inc. for post purchase of Delta/HySecurity barrier and gate equipment (PoP Colombia); obligated USD 24,893. CapEx face = award obligation. Exact post unnamed — lat/lon blank.',
    "24893", "2015-09-29", "2015", "", "",
    'Post purchase of Delta/HySecurity barrier and gate equipment, Colombia (USASpending description; post not named — lat/lon blank).',
    "usaspending_hy_security_colombia_barrier_gate_equipment_25k_2015",
    'POST PURCHASE OF DELTA/HYSECURITY BARRIER AND GATE EQUIPMENTIGF::CL::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20015M1575_1900_-NONE-_-NONE-/",
    'Actor: Hy-Security Gate, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1122",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20015M1575_1900_-NONE-_-NONE- (hy_security_colombia_barrier_gate_equipment_25k_2015). Signed 2015-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20015M1575_1900_-NONE-_-NONE-/.',
    'USASpending: hy_security_colombia_barrier_gate_equipment_25k_2015 USD 0.025m. Supports hy_security_colombia_barrier_gate_equipment_25k_2015.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 24893; date_signed 2015-09-29.',
)
row_doc(
    "bentley_mills_mexico_dea_office_carpet_tiles_24k_2015",
    "infrastructure", "building_materials", "us",
    'Bentley Mills — Mexico GO building DEA office carpet tiles replace',
    "Mexico",
    '11 Aug 2015: Department of State awards contract SMX53015F0700 to Bentley Mills Inc for GO building DEA office carpet tiles replace (PoP Mexico); obligated USD 24,451.7. CapEx face = award obligation. Exact GO building unnamed — lat/lon blank.',
    "24451.7", "2015-08-11", "2015", "", "",
    'GO building DEA office carpet tiles replace, Mexico (USASpending description; GO/DEA named, site coords not stated — lat/lon blank).',
    "usaspending_bentley_mills_mexico_dea_office_carpet_tiles_24k_2015",
    'MEX-FAC-7901.C- GO BUILDING DEA OFFICE CARPET TILES REPLACE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015F0700_1900_SMX53015D0016_1900/",
    'Actor: Bentley Mills Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1122",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53015F0700_1900_SMX53015D0016_1900 (bentley_mills_mexico_dea_office_carpet_tiles_24k_2015). Signed 2015-08-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015F0700_1900_SMX53015D0016_1900/.',
    'USASpending: bentley_mills_mexico_dea_office_carpet_tiles_24k_2015 USD 0.024m. Supports bentley_mills_mexico_dea_office_carpet_tiles_24k_2015.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 24451.7; date_signed 2015-08-11.',
)
row_doc(
    "perez_romo_mexico_ccs_carpet_tile_replace_38k_2023",
    "infrastructure", "building_materials", "other",
    'Jorge Eduardo Perez Romo — Mexico CCS carpet tile replace FWP 168',
    "Mexico",
    '16 Mar 2023: Department of State awards contract 19MX1123P0071 to Jorge Eduardo Perez Romo for CCS carpet tile replace FWP 168 (PoP Mexico); obligated USD 37,771.92. CapEx face = award obligation. Exact CCS unnamed — lat/lon blank.',
    "37771.92", "2023-03-16", "2023", "", "",
    'CCS carpet tile replace FWP 168, Mexico (USASpending description; CCS named, site coords not stated — lat/lon blank).',
    "usaspending_perez_romo_mexico_ccs_carpet_tile_replace_38k_2023",
    'FAC7901-FWP 168 CCS CARPET TILE REPLACE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1123P0071_1900_-NONE-_-NONE-/",
    'Actor: Jorge Eduardo Perez Romo (Mexico) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1122",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX1123P0071_1900_-NONE-_-NONE- (perez_romo_mexico_ccs_carpet_tile_replace_38k_2023). Signed 2023-03-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1123P0071_1900_-NONE-_-NONE-/.',
    'USASpending: perez_romo_mexico_ccs_carpet_tile_replace_38k_2023 USD 0.038m. Supports perez_romo_mexico_ccs_carpet_tile_replace_38k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37771.92; date_signed 2023-03-16.',
)
row_doc(
    "proyectos_civiles_panama_escobal_clinic_roof_37k_2013",
    "infrastructure", "building_materials", "other",
    'Proyectos Civiles S y M Limitada — Panama Escobal clinic roof and misc improvements',
    "Panama",
    '26 Sep 2013: Department of Defense awards contract W912CL13C0012 to Proyectos Civiles S y M Limitada for Escobal clinic roof and misc improvements (PoP Panama); obligated USD 37,487.4. CapEx face = award obligation. Escobal named; site coords not stated — lat/lon blank.',
    "37487.4", "2013-09-26", "2013", "", "",
    'Escobal clinic roof and misc improvements, Panama (USASpending description; Escobal named, site coords not stated — lat/lon blank).',
    "usaspending_proyectos_civiles_panama_escobal_clinic_roof_37k_2013",
    'ESCOBAL CLINIC ROOF&MISC IMPROVEMENTS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL13C0012_9700_-NONE-_-NONE-/",
    'Actor: Proyectos Civiles S y M Limitada (Colombia-registered) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1122",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL13C0012_9700_-NONE-_-NONE- (proyectos_civiles_panama_escobal_clinic_roof_37k_2013). Signed 2013-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL13C0012_9700_-NONE-_-NONE-/.',
    'USASpending: proyectos_civiles_panama_escobal_clinic_roof_37k_2013 USD 0.037m. Supports proyectos_civiles_panama_escobal_clinic_roof_37k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37487.4; date_signed 2013-09-26.',
)
row_doc(
    "gordon_gordons_panama_tupper_meeting_rooms_renovation_37k_2025",
    "infrastructure", "building_materials", "other",
    'Gordon & Gordons Services — Panama Tupper building meeting rooms renovation',
    "Panama",
    '18 Sep 2025: Smithsonian awards contract 33312925P00529454 to Gordon & Gordons Services, Inc. for BM07-2025 renovation Tupper building meeting rooms (PoP Panama); obligated USD 37,288.23. CapEx face = award obligation. Tupper building named; site coords not stated — lat/lon blank.',
    "37288.23", "2025-09-18", "2025", "", "",
    'Renovation Tupper building meeting rooms, Panama (USASpending description; Tupper building named, site coords not stated — lat/lon blank).',
    "usaspending_gordon_gordons_panama_tupper_meeting_rooms_renovation_37k_2025",
    'BM07-2025 RENOVATION TUPPER BULDING MEETING ROOMS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312925P00529454_3300_-NONE-_-NONE-/",
    'Actor: Gordon & Gordons Services, Inc. (Panama) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1122",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33312925P00529454_3300_-NONE-_-NONE- (gordon_gordons_panama_tupper_meeting_rooms_renovation_37k_2025). Signed 2025-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312925P00529454_3300_-NONE-_-NONE-/.',
    'USASpending: gordon_gordons_panama_tupper_meeting_rooms_renovation_37k_2025 USD 0.037m. Supports gordon_gordons_panama_tupper_meeting_rooms_renovation_37k_2025.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37288.23; date_signed 2025-09-18.',
)

# === Cycle 1123 (seed 20262123) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "international_power_bolivia_la_paz_ups_electrical_22k_2010",
    "energy", "power_plants_grid", "us",
    'International Power Services — Bolivia La Paz UPS electrical work',
    "Bolivia",
    '25 Feb 2010: Department of State awards contract SAQMMA10M0411 to International Power Services, LLC for power systems engineering UPS La Paz electrical work (PoP Bolivia); obligated USD 22,000. CapEx face = award obligation. La Paz named; site coords not stated — lat/lon blank.',
    "22000", "2010-02-25", "2010", "", "",
    'UPS La Paz electrical work, Bolivia (USASpending description; La Paz named, site coords not stated — lat/lon blank).',
    "usaspending_international_power_bolivia_la_paz_ups_electrical_22k_2010",
    'POWER SYSTEMS ENGINEERING- UPS LA PAZ ELECTRICAL WORK',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10M0411_1900_-NONE-_-NONE-/",
    'Actor: International Power Services, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1123",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10M0411_1900_-NONE-_-NONE- (international_power_bolivia_la_paz_ups_electrical_22k_2010). Signed 2010-02-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10M0411_1900_-NONE-_-NONE-/.',
    'USASpending: international_power_bolivia_la_paz_ups_electrical_22k_2010 USD 0.022m. Supports international_power_bolivia_la_paz_ups_electrical_22k_2010.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 22000; date_signed 2010-02-25.',
)
row_doc(
    "continental_flooring_peru_chancery_ceiling_tiles_22k_2022",
    "infrastructure", "building_materials", "us",
    'Continental Flooring — Peru chancery building ceiling tiles purchase',
    "Peru",
    '7 Sep 2022: Department of State awards contract 19PE5022F0408 to Continental Flooring Co for purchase ceiling tiles for chancery building (PoP Peru); obligated USD 21,839. CapEx face = award obligation. Exact chancery unnamed — lat/lon blank.',
    "21839", "2022-09-07", "2022", "", "",
    'Purchase ceiling tiles for chancery building, Peru (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_continental_flooring_peru_chancery_ceiling_tiles_22k_2022",
    'FAC:7901:PURCHASE CEILING TILES FOR CHRY BLDG',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5022F0408_1900_47QSWA19D009U_4732/",
    'Actor: Continental Flooring Co (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1123",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5022F0408_1900_47QSWA19D009U_4732 (continental_flooring_peru_chancery_ceiling_tiles_22k_2022). Signed 2022-09-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5022F0408_1900_47QSWA19D009U_4732/.',
    'USASpending: continental_flooring_peru_chancery_ceiling_tiles_22k_2022 USD 0.022m. Supports continental_flooring_peru_chancery_ceiling_tiles_22k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 21839; date_signed 2022-09-07.',
)
row_doc(
    "altamirano_mexico_tres_canadas_gas_tank_replacement_37k_2023",
    "resources", "water", "other",
    'Edgar Altamirano Arteaga — Mexico Tres Canadas fixed gas tank replacement',
    "Mexico",
    '24 Mar 2023: Department of State awards contract 19MX5323C0003 to Edgar Altamirano Arteaga for Tres Canadas fixed gas tank replacement (PoP Mexico); obligated USD 37,164.7. CapEx face = award obligation. Tres Canadas named; site coords not stated — lat/lon blank.',
    "37164.7", "2023-03-24", "2023", "", "",
    'Tres Canadas fixed gas tank replacement, Mexico (USASpending description; Tres Canadas named, site coords not stated — lat/lon blank).',
    "usaspending_altamirano_mexico_tres_canadas_gas_tank_replacement_37k_2023",
    'TRES CANADAS FIXED GAS TANK REPLACEMENT',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5323C0003_1900_-NONE-_-NONE-/",
    'Actor: Edgar Altamirano Arteaga (Mexico) — other. Official USASpending Award API. Shuffle water.',
    "hunt_cycle1123",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5323C0003_1900_-NONE-_-NONE- (altamirano_mexico_tres_canadas_gas_tank_replacement_37k_2023). Signed 2023-03-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5323C0003_1900_-NONE-_-NONE-/.',
    'USASpending: altamirano_mexico_tres_canadas_gas_tank_replacement_37k_2023 USD 0.037m. Supports altamirano_mexico_tres_canadas_gas_tank_replacement_37k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37164.7; date_signed 2023-03-24.',
)
row_doc(
    "wkl_arquitectos_panama_cmr_guests_bathrooms_repair_37k_2019",
    "infrastructure", "building_materials", "other",
    'W.K.L. Arquitectos — Panama CMR guests bathrooms repair',
    "Panama",
    '26 Aug 2019: Department of State awards contract 19PM0719P0971 to W.K.L. Arquitectos S.A. for guests bathrooms repair CMR 7355 (PoP Panama); obligated USD 36,820. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.',
    "36820", "2019-08-26", "2019", "", "",
    'Guests bathrooms repair CMR 7355, Panama (USASpending description; CMR named, site coords not stated — lat/lon blank).',
    "usaspending_wkl_arquitectos_panama_cmr_guests_bathrooms_repair_37k_2019",
    '19PM0719P0971 GUESTS BATHROOMS REPAIR  CMR 7355 (19Q0047) WKL',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0971_1900_-NONE-_-NONE-/",
    'Actor: W.K.L. Arquitectos S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1123",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0719P0971_1900_-NONE-_-NONE- (wkl_arquitectos_panama_cmr_guests_bathrooms_repair_37k_2019). Signed 2019-08-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0971_1900_-NONE-_-NONE-/.',
    'USASpending: wkl_arquitectos_panama_cmr_guests_bathrooms_repair_37k_2019 USD 0.037m. Supports wkl_arquitectos_panama_cmr_guests_bathrooms_repair_37k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36820; date_signed 2019-08-26.',
)
row_doc(
    "sarti_guatemala_restroom_renovation_37k_2014",
    "infrastructure", "building_materials", "other",
    'Luis Alberto Sarti Calvillo — Guatemala restroom renovation',
    "Guatemala",
    '24 Jan 2014: Department of Defense awards contract W912QM14C0002 to Luis Alberto Sarti Calvillo for restroom renovation (PoP Guatemala); obligated USD 36,699.99. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "36699.99", "2014-01-24", "2014", "", "",
    'Restroom renovation, Guatemala (USASpending description; site not named — lat/lon blank).',
    "usaspending_sarti_guatemala_restroom_renovation_37k_2014",
    'RESTROOM RENOVATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM14C0002_9700_-NONE-_-NONE-/",
    'Actor: Luis Alberto Sarti Calvillo (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1123",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM14C0002_9700_-NONE-_-NONE- (sarti_guatemala_restroom_renovation_37k_2014). Signed 2014-01-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM14C0002_9700_-NONE-_-NONE-/.',
    'USASpending: sarti_guatemala_restroom_renovation_37k_2014 USD 0.037m. Supports sarti_guatemala_restroom_renovation_37k_2014.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36699.99; date_signed 2014-01-24.',
)

# === Cycle 1124 (seed 20262124) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "absolute_storage_nicaragua_cantilever_parking_space_22k_2011",
    "infrastructure", "bridges_roads", "us",
    'Absolute Storage — Nicaragua full-cantilever design parking space',
    "Nicaragua",
    '29 Sep 2011: Department of State awards contract SNU70011F0020 to Absolute Storage, LLC for full-cantilever design/parking space (PoP Nicaragua); obligated USD 21,730. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "21730", "2011-09-29", "2011", "", "",
    'Full-cantilever design/parking space, Nicaragua (USASpending description; site not named — lat/lon blank).',
    "usaspending_absolute_storage_nicaragua_cantilever_parking_space_22k_2011",
    'FULL-CANTILEVER DESIGN/PARKING SPACE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70011F0020_1900_GS07F9481S_4730/",
    'Actor: Absolute Storage, LLC (U.S.) — us. Official USASpending Award API. Shuffle bridges_roads; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1124",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SNU70011F0020_1900_GS07F9481S_4730 (absolute_storage_nicaragua_cantilever_parking_space_22k_2011). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70011F0020_1900_GS07F9481S_4730/.',
    'USASpending: absolute_storage_nicaragua_cantilever_parking_space_22k_2011 USD 0.022m. Supports absolute_storage_nicaragua_cantilever_parking_space_22k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 21730; date_signed 2011-09-29.',
)
row_doc(
    "fast_access_venezuela_chancery_gate_operators_22k_2014",
    "infrastructure", "building_materials", "us",
    'Fast Access Security — Venezuela chancery compound gate operators',
    "Venezuela",
    '13 May 2014: Department of State awards contract SVE30014M0242 to Fast Access Security Corp. for gate operators for the chancery compound (PoP Venezuela); obligated USD 21,591. CapEx face = award obligation. Exact chancery unnamed — lat/lon blank.',
    "21591", "2014-05-13", "2014", "", "",
    'Gate operators for the chancery compound, Venezuela (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_fast_access_venezuela_chancery_gate_operators_22k_2014",
    'GATE OPERATORS FOR THE CHANCERY COMPOUND- CHARGE 7945',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30014M0242_1900_-NONE-_-NONE-/",
    'Actor: Fast Access Security Corp. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Weight under-covered Venezuela.',
    "hunt_cycle1124",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30014M0242_1900_-NONE-_-NONE- (fast_access_venezuela_chancery_gate_operators_22k_2014). Signed 2014-05-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30014M0242_1900_-NONE-_-NONE-/.',
    'USASpending: fast_access_venezuela_chancery_gate_operators_22k_2014 USD 0.022m. Supports fast_access_venezuela_chancery_gate_operators_22k_2014.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 21591; date_signed 2014-05-13.',
)
row_doc(
    "miscelaneos_security_costa_rica_obc_hallways_painting_37k_2019",
    "infrastructure", "building_materials", "other",
    'Miscelaneos Security Services — Costa Rica OBC hallways painting',
    "Costa Rica",
    '22 May 2019: Department of State awards contract 19CS8019C0004 to Miscelaneos Security Services Sociedad Anonima for OBC hallways painting (PoP Costa Rica); obligated USD 36,728.89. CapEx face = award obligation. Exact OBC unnamed — lat/lon blank.',
    "36728.89", "2019-05-22", "2019", "", "",
    'OBC hallways painting, Costa Rica (USASpending description; OBC named, site coords not stated — lat/lon blank).',
    "usaspending_miscelaneos_security_costa_rica_obc_hallways_painting_37k_2019",
    'OBC HALLWAYS PAINTING',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8019C0004_1900_-NONE-_-NONE-/",
    'Actor: Miscelaneos Security Services Sociedad Anonima (Costa Rica) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1124",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8019C0004_1900_-NONE-_-NONE- (miscelaneos_security_costa_rica_obc_hallways_painting_37k_2019). Signed 2019-05-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8019C0004_1900_-NONE-_-NONE-/.',
    'USASpending: miscelaneos_security_costa_rica_obc_hallways_painting_37k_2019 USD 0.037m. Supports miscelaneos_security_costa_rica_obc_hallways_painting_37k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36728.89; date_signed 2019-05-22.',
)
row_doc(
    "casa_planas_mexico_tents_flooring_installation_foj_37k_2025",
    "infrastructure", "building_materials", "other",
    'Casa Planas Renta — Mexico tents and flooring installation FOJ FY25',
    "Mexico",
    '23 May 2025: Department of State awards contract 19MX5325P0874 to Casa Planas Renta for tents and flooring installation FOJ FY25 (PoP Mexico); obligated USD 36,525.03. CapEx face = award obligation. Exact FOJ site unnamed — lat/lon blank.',
    "36525.03", "2025-05-23", "2025", "", "",
    'Tents and flooring installation FOJ FY25, Mexico (USASpending description; FOJ named, site coords not stated — lat/lon blank).',
    "usaspending_casa_planas_mexico_tents_flooring_installation_foj_37k_2025",
    'MEX-FAC-PRGM-TENTS & FLOORING INSTALLATION FOJ FY25',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5325P0874_1900_-NONE-_-NONE-/",
    'Actor: Casa Planas Renta (Mexico) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1124",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5325P0874_1900_-NONE-_-NONE- (casa_planas_mexico_tents_flooring_installation_foj_37k_2025). Signed 2025-05-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5325P0874_1900_-NONE-_-NONE-/.',
    'USASpending: casa_planas_mexico_tents_flooring_installation_foj_37k_2025 USD 0.037m. Supports casa_planas_mexico_tents_flooring_installation_foj_37k_2025.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36525.03; date_signed 2025-05-23.',
)
row_doc(
    "misc_colombia_containers_supply_installation_37k_2012",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Colombia supply and installation of containers',
    "Colombia",
    '4 Jun 2012: Department of State awards contract SCO15012M1172 for INTER supply and installation of containers (PoP Colombia); obligated USD 37,211.34. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "37211.34", "2012-06-04", "2012", "", "",
    'Supply and installation of containers, Colombia (USASpending description; site not named — lat/lon blank).',
    "usaspending_misc_colombia_containers_supply_installation_37k_2012",
    'INTER (J) - SUPPLY AND INSTALLATION OF CONTAINERS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M1172_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1124",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15012M1172_1900_-NONE-_-NONE- (misc_colombia_containers_supply_installation_37k_2012). Signed 2012-06-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M1172_1900_-NONE-_-NONE-/.',
    'USASpending: misc_colombia_containers_supply_installation_37k_2012 USD 0.037m. Supports misc_colombia_containers_supply_installation_37k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37211.34; date_signed 2012-06-04.',
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
