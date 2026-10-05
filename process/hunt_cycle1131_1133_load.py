#!/usr/bin/env python3
"""Cycles 1131–1133: USASpending LatAm CapEx residual (~USD0.020–0.036m).

Seeds: 20262131–20262133. Thin top-up dry.
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


# === Cycle 1131 (seed 20262131) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_panama_metal_door_screen_21k_2025",
    "infrastructure", "building_materials", "us",
    'Norshield Security Products — Panama metal door screen frame for international embassies',
    "Panama",
    '3 Sep 2025: Department of State awards contract 19AQMM25P0031 to Norshield Security Products, LLC for metal door screen frame etc. for international embassies (PoP Panama); obligated USD 20,550. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.',
    "20550", "2025-09-03", "2025", "", "",
    'Metal door screen frame for international embassies, Panama (USASpending description; embassy not named — lat/lon blank).',
    "usaspending_norshield_panama_metal_door_screen_21k_2025",
    'METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0031_1900_-NONE-_-NONE-/",
    'Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1131",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0031_1900_-NONE-_-NONE- (norshield_panama_metal_door_screen_21k_2025). Signed 2025-09-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0031_1900_-NONE-_-NONE-/.',
    'USASpending: norshield_panama_metal_door_screen_21k_2025 USD 0.021m. Supports norshield_panama_metal_door_screen_21k_2025.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 20550; date_signed 2025-09-03.',
)
row_doc(
    "morton_buildings_mexico_restroom_building_20k_2012",
    "infrastructure", "building_materials", "us",
    'Morton Buildings — Mexico restroom building 18 x 8 x 9',
    "Mexico",
    '24 Sep 2012: Department of Agriculture awards contract AGVCHA26312 to Morton Buildings, Inc for restroom building 18 x 8 x 9 (PoP Mexico); obligated USD 20,310. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "20310", "2012-09-24", "2012", "", "",
    'Restroom building 18 x 8 x 9, Mexico (USASpending description; site not named — lat/lon blank).',
    "usaspending_morton_buildings_mexico_restroom_building_20k_2012",
    'RESTROOM BUILDING 18 X 8 X 9',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AGVCHA26312_12K3_GS07F0151Y_4732/",
    'Actor: Morton Buildings, Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1131",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AGVCHA26312_12K3_GS07F0151Y_4732 (morton_buildings_mexico_restroom_building_20k_2012). Signed 2012-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AGVCHA26312_12K3_GS07F0151Y_4732/.',
    'USASpending: morton_buildings_mexico_restroom_building_20k_2012 USD 0.020m. Supports morton_buildings_mexico_restroom_building_20k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 20310; date_signed 2012-09-24.',
)
row_doc(
    "arcadia_colombia_inl_generator_36k_2020",
    "energy", "power_plants_grid", "other",
    'Comercializadora Arcadia — Colombia INL generator',
    "Colombia",
    '15 Sep 2020: Department of State awards contract 19C01520P0339 to Comercializadora Arcadia SAS for INL generator (PoP Colombia); obligated USD 35,556.22. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "35556.22", "2020-09-15", "2020", "", "",
    'INL generator, Colombia (USASpending description; site not named — lat/lon blank).',
    "usaspending_arcadia_colombia_inl_generator_36k_2020",
    'INL-GENERATOR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520P0339_1900_-NONE-_-NONE-/",
    'Actor: Comercializadora Arcadia SAS (Colombia) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1131",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01520P0339_1900_-NONE-_-NONE- (arcadia_colombia_inl_generator_36k_2020). Signed 2020-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01520P0339_1900_-NONE-_-NONE-/.',
    'USASpending: arcadia_colombia_inl_generator_36k_2020 USD 0.036m. Supports arcadia_colombia_inl_generator_36k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35556.22; date_signed 2020-09-15.',
)
row_doc(
    "peak_scientific_mexico_hydrogen_generators_36k_2026",
    "energy", "power_plants_grid", "other",
    'Peak Scientific — Mexico INL hydrogen generators',
    "Mexico",
    '29 Jul 2026: Department of State awards contract 19MX9026P0058 to Peak Scientific S.A. de C.V. for INL hydrogen generators WHP.MX.0236.A01 (PoP Mexico); obligated USD 35,531.23. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "35531.23", "2026-07-29", "2026", "", "",
    'INL hydrogen generators WHP.MX.0236.A01, Mexico (USASpending description; project code named, site coords not stated — lat/lon blank).',
    "usaspending_peak_scientific_mexico_hydrogen_generators_36k_2026",
    'INL-MX_CD-FOR_IN41MX70-HYDROGEN GENERATORS WHP.MX.0236.A01',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX9026P0058_1900_-NONE-_-NONE-/",
    'Actor: Peak Scientific S.A. de C.V. (Mexico) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1131",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX9026P0058_1900_-NONE-_-NONE- (peak_scientific_mexico_hydrogen_generators_36k_2026). Signed 2026-07-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX9026P0058_1900_-NONE-_-NONE-/.',
    'USASpending: peak_scientific_mexico_hydrogen_generators_36k_2026 USD 0.036m. Supports peak_scientific_mexico_hydrogen_generators_36k_2026.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35531.23; date_signed 2026-07-29.',
)
row_doc(
    "misc_dominican_republic_cmr_sallyport_renovation_35k_2022",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Dominican Republic CMR sallyport renovation and replacement',
    "Dominican Republic",
    '21 Sep 2022: Department of State awards contract 19DR8622P1765 for sallyport renovation and replacement at CMR (PoP Dominican Republic); obligated USD 35,365.75. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.',
    "35365.75", "2022-09-21", "2022", "", "",
    'Sallyport renovation and replacement at CMR, Dominican Republic (USASpending description; CMR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_dominican_republic_cmr_sallyport_renovation_35k_2022",
    'OBO7355 - SALLYPORT RENOVATION AND REPLACEMENT AT CMR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622P1765_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1131",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8622P1765_1900_-NONE-_-NONE- (misc_dominican_republic_cmr_sallyport_renovation_35k_2022). Signed 2022-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622P1765_1900_-NONE-_-NONE-/.',
    'USASpending: misc_dominican_republic_cmr_sallyport_renovation_35k_2022 USD 0.035m. Supports misc_dominican_republic_cmr_sallyport_renovation_35k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35365.75; date_signed 2022-09-21.',
)

# === Cycle 1132 (seed 20262132) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "johnson_controls_barbados_nec_chiller_vsd_power_assembly_20k_2014",
    "energy", "power_plants_grid", "us",
    'Johnson Controls — Barbados NEC chillers replacement power assembly VSD',
    "Barbados",
    '8 Dec 2014: Department of State awards contract SBB21015M0162 to Johnson Controls Inc for replacement power assembly VSD-NEC chillers (PoP Barbados); obligated USD 20,250. CapEx face = award obligation. Exact NEC unnamed — lat/lon blank.',
    "20250", "2014-12-08", "2014", "", "",
    'Replacement power assembly VSD-NEC chillers, Barbados (USASpending description; NEC named, site coords not stated — lat/lon blank).',
    "usaspending_johnson_controls_barbados_nec_chiller_vsd_power_assembly_20k_2014",
    'REPLACEMENT POWER ASSEMBLY VSD-NEC CHILLERS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21015M0162_1900_-NONE-_-NONE-/",
    'Actor: Johnson Controls Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1132",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21015M0162_1900_-NONE-_-NONE- (johnson_controls_barbados_nec_chiller_vsd_power_assembly_20k_2014). Signed 2014-12-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21015M0162_1900_-NONE-_-NONE-/.',
    'USASpending: johnson_controls_barbados_nec_chiller_vsd_power_assembly_20k_2014 USD 0.020m. Supports johnson_controls_barbados_nec_chiller_vsd_power_assembly_20k_2014.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 20250; date_signed 2014-12-08.',
)
row_doc(
    "norshield_nicaragua_metal_door_screen_20k_2022",
    "infrastructure", "building_materials", "us",
    'Norshield Security Products — Nicaragua metal door screen for international embassies',
    "Nicaragua",
    '6 Jul 2022: Department of State awards contract 19AQMM22P0762 to Norshield Security Products, LLC for metal door screen etc. (PoP Nicaragua); obligated USD 20,120. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.',
    "20120", "2022-07-06", "2022", "", "",
    'Metal door screen etc., Nicaragua (USASpending description; embassy not named — lat/lon blank).',
    "usaspending_norshield_nicaragua_metal_door_screen_20k_2022",
    'METAL DOOR SCREEN ETC.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0762_1900_-NONE-_-NONE-/",
    'Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1132",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22P0762_1900_-NONE-_-NONE- (norshield_nicaragua_metal_door_screen_20k_2022). Signed 2022-07-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0762_1900_-NONE-_-NONE-/.',
    'USASpending: norshield_nicaragua_metal_door_screen_20k_2022 USD 0.020m. Supports norshield_nicaragua_metal_door_screen_20k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 20120; date_signed 2022-07-06.',
)
row_doc(
    "misc_bahamas_cabinet_installation_35k_2026",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Bahamas cabinet installation',
    "Bahamas",
    '21 Sep 2026: Department of State awards contract 19BF5026P0505 for cabinet installation (PoP Bahamas); obligated USD 35,365. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "35365", "2026-09-21", "2026", "", "",
    'Cabinet installation, Bahamas (USASpending description; site not named — lat/lon blank).',
    "usaspending_misc_bahamas_cabinet_installation_35k_2026",
    'CABINET INSTALLATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5026P0505_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1132",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BF5026P0505_1900_-NONE-_-NONE- (misc_bahamas_cabinet_installation_35k_2026). Signed 2026-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5026P0505_1900_-NONE-_-NONE-/.',
    'USASpending: misc_bahamas_cabinet_installation_35k_2026 USD 0.035m. Supports misc_bahamas_cabinet_installation_35k_2026.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35365; date_signed 2026-09-21.',
)
row_doc(
    "misc_costa_rica_compu_room_ac_install_35k_2012",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Costa Rica OFDA purchase and installation of A/C for computer room',
    "Costa Rica",
    '24 Sep 2012: Department of State awards contract SCS80012M0983 for purchase and installation of A/C for compu room (PoP Costa Rica); obligated USD 35,344. CapEx face = award obligation. Exact computer room unnamed — lat/lon blank.',
    "35344", "2012-09-24", "2012", "", "",
    'Purchase and installation of A/C for computer room, Costa Rica (USASpending description; room not named — lat/lon blank).',
    "usaspending_misc_costa_rica_compu_room_ac_install_35k_2012",
    'OFDA/OFDA - PURCHASE AND INSTALLATION OF A/C FOR COMPU ROOM',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80012M0983_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1132",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80012M0983_1900_-NONE-_-NONE- (misc_costa_rica_compu_room_ac_install_35k_2012). Signed 2012-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80012M0983_1900_-NONE-_-NONE-/.',
    'USASpending: misc_costa_rica_compu_room_ac_install_35k_2012 USD 0.035m. Supports misc_costa_rica_compu_room_ac_install_35k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35344; date_signed 2012-09-24.',
)
row_doc(
    "misc_colombia_tumaco_mesh_fence_35k_2011",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Colombia COLAR AV NCT mesh fence Tumaco',
    "Colombia",
    '2 Nov 2011: Department of State awards contract SCO15012M0153 for COLAR AV NCT mesh fence Tumaco (PoP Colombia); obligated USD 35,337.43. CapEx face = award obligation. Tumaco named; site coords not stated — lat/lon blank.',
    "35337.43", "2011-11-02", "2011", "", "",
    'COLAR AV NCT mesh fence Tumaco, Colombia (USASpending description; Tumaco named, site coords not stated — lat/lon blank).',
    "usaspending_misc_colombia_tumaco_mesh_fence_35k_2011",
    'COLAR AV NCT MESH FENCE TUMACO',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M0153_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1132",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15012M0153_1900_-NONE-_-NONE- (misc_colombia_tumaco_mesh_fence_35k_2011). Signed 2011-11-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M0153_1900_-NONE-_-NONE-/.',
    'USASpending: misc_colombia_tumaco_mesh_fence_35k_2011 USD 0.035m. Supports misc_colombia_tumaco_mesh_fence_35k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35337.43; date_signed 2011-11-02.',
)

# === Cycle 1133 (seed 20262133) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "americas_generators_colombia_electric_generator_20k_2012",
    "energy", "power_plants_grid", "us",
    'Americas Generators — Colombia electric generator',
    "Colombia",
    '1 Jun 2012: Department of Defense awards contract W913FT12P0179 to Americas Generators, Inc. for electric generator (PoP Colombia); obligated USD 20,109.99. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "20109.99", "2012-06-01", "2012", "", "",
    'Electric generator, Colombia (USASpending description; site not named — lat/lon blank).',
    "usaspending_americas_generators_colombia_electric_generator_20k_2012",
    'ELECTRIC GENERATOR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0179_9700_-NONE-_-NONE-/",
    'Actor: Americas Generators, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1133",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12P0179_9700_-NONE-_-NONE- (americas_generators_colombia_electric_generator_20k_2012). Signed 2012-06-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0179_9700_-NONE-_-NONE-/.',
    'USASpending: americas_generators_colombia_electric_generator_20k_2012 USD 0.020m. Supports americas_generators_colombia_electric_generator_20k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 20109.99; date_signed 2012-06-01.',
)
row_doc(
    "multistack_ecuador_chiller_tandem_compressors_20k_2024",
    "energy", "power_plants_grid", "us",
    'Multistack — Ecuador tandem compressors for chiller',
    "Ecuador",
    '31 Jan 2024: Department of State awards contract 19EC3024P0124 to Multistack LLC for tandem compressors for chiller (PoP Ecuador); obligated USD 20,108.82. CapEx face = award obligation. Exact chiller site unnamed — lat/lon blank.',
    "20108.82", "2024-01-31", "2024", "", "",
    'Tandem compressors for chiller, Ecuador (USASpending description; site not named — lat/lon blank).',
    "usaspending_multistack_ecuador_chiller_tandem_compressors_20k_2024",
    'TANDEM COMPRESSORS FOR CHILLER',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3024P0124_1900_-NONE-_-NONE-/",
    'Actor: Multistack LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1133",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC3024P0124_1900_-NONE-_-NONE- (multistack_ecuador_chiller_tandem_compressors_20k_2024). Signed 2024-01-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC3024P0124_1900_-NONE-_-NONE-/.',
    'USASpending: multistack_ecuador_chiller_tandem_compressors_20k_2024 USD 0.020m. Supports multistack_ecuador_chiller_tandem_compressors_20k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 20108.82; date_signed 2024-01-31.',
)
row_doc(
    "misc_mexico_emr_kitchen_renovation_preliminary_35k_2011",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Mexico EMR kitchen renovation preliminary works',
    "Mexico",
    '1 Jul 2011: Department of State awards contract SMX53011M1077 for OBO MEX EMR kitchen renovation preliminary works (PoP Mexico); obligated USD 35,205.99. CapEx face = award obligation. Exact EMR unnamed — lat/lon blank.',
    "35205.99", "2011-07-01", "2011", "", "",
    'EMR kitchen renovation preliminary works, Mexico (USASpending description; EMR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_mexico_emr_kitchen_renovation_preliminary_35k_2011",
    'OBO MEX EMR KITCHEN RENOVATION PRELIMINARY WORKS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M1077_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1133",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53011M1077_1900_-NONE-_-NONE- (misc_mexico_emr_kitchen_renovation_preliminary_35k_2011). Signed 2011-07-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M1077_1900_-NONE-_-NONE-/.',
    'USASpending: misc_mexico_emr_kitchen_renovation_preliminary_35k_2011 USD 0.035m. Supports misc_mexico_emr_kitchen_renovation_preliminary_35k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35205.99; date_signed 2011-07-01.',
)
row_doc(
    "tecniservicios_costa_rica_agua_dulce_medium_voltage_35k_2023",
    "energy", "power_plants_grid", "other",
    'Tecniservicios FBV — Costa Rica CBP Post Agua Dulce medium voltage system',
    "Costa Rica",
    '4 Apr 2023: Department of State awards contract 19CS8023P0482 to Tecniservicios FBV SRL for INL medium voltage system CBP Post Agua Dulce (PoP Costa Rica); obligated USD 35,208.01. CapEx face = award obligation. Agua Dulce named; site coords not stated — lat/lon blank.',
    "35208.01", "2023-04-04", "2023", "", "",
    'Medium voltage system CBP Post Agua Dulce, Costa Rica (USASpending description; Agua Dulce named, site coords not stated — lat/lon blank).',
    "usaspending_tecniservicios_costa_rica_agua_dulce_medium_voltage_35k_2023",
    'INL 1930.0 MEDIUM VOLTAGE SYSTEM - CBP POST AGUA DULCE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8023P0482_1900_-NONE-_-NONE-/",
    'Actor: Tecniservicios FBV SRL (Costa Rica) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1133",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8023P0482_1900_-NONE-_-NONE- (tecniservicios_costa_rica_agua_dulce_medium_voltage_35k_2023). Signed 2023-04-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8023P0482_1900_-NONE-_-NONE-/.',
    'USASpending: tecniservicios_costa_rica_agua_dulce_medium_voltage_35k_2023 USD 0.035m. Supports tecniservicios_costa_rica_agua_dulce_medium_voltage_35k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35208.01; date_signed 2023-04-04.',
)
row_doc(
    "misc_colombia_school_refurbishment_project_33076_35k_2017",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Colombia project 33076 refurbishment of school',
    "Colombia",
    '7 Mar 2017: Department of Defense awards contract W913FT17P0124 for project 33076 refurbishment of school (PoP Colombia); obligated USD 35,155.83. CapEx face = award obligation. Exact school unnamed — lat/lon blank.',
    "35155.83", "2017-03-07", "2017", "", "",
    'Project 33076 refurbishment of school, Colombia (USASpending description; school not named — lat/lon blank).',
    "usaspending_misc_colombia_school_refurbishment_project_33076_35k_2017",
    'PROJECT#33076 REFURBISHMENT OF SCHOOL',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT17P0124_9700_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1133",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT17P0124_9700_-NONE-_-NONE- (misc_colombia_school_refurbishment_project_33076_35k_2017). Signed 2017-03-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT17P0124_9700_-NONE-_-NONE-/.',
    'USASpending: misc_colombia_school_refurbishment_project_33076_35k_2017 USD 0.035m. Supports misc_colombia_school_refurbishment_project_33076_35k_2017.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35155.83; date_signed 2017-03-07.',
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
