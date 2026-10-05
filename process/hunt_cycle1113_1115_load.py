#!/usr/bin/env python3
"""Cycles 1113–1115: USASpending LatAm CapEx residual (~USD0.027–0.047m).

Seeds: 20262113–20262115. Thin top-up dry. Holdovers USMAX/Alban/Southwestern/Caterpillar/Bentley library closed.
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


# === Cycle 1113 (seed 20262113) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "cummins_st_kitts_engine_installation_30k_2024",
    "energy", "power_plants_grid", "us",
    'Cummins — Saint Kitts engine installation',
    "Saint Kitts and Nevis",
    '2 Aug 2024: Department of Defense awards contract W91QEX24P0053 to Cummins Inc. for engine installation (St Kitts) (PoP Saint Kitts and Nevis); obligated USD 29,929.79. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "29929.79", "2024-08-02", "2024", "", "",
    'Engine installation (St Kitts), Saint Kitts and Nevis (USASpending description; site not named — lat/lon blank).',
    "usaspending_cummins_st_kitts_engine_installation_30k_2024",
    'ENGINE INSTALLATION (ST KITTS)',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W91QEX24P0053_9700_-NONE-_-NONE-/",
    'Actor: Cummins Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1113",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W91QEX24P0053_9700_-NONE-_-NONE- (cummins_st_kitts_engine_installation_30k_2024). Signed 2024-08-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W91QEX24P0053_9700_-NONE-_-NONE-/.',
    'USASpending: cummins_st_kitts_engine_installation_30k_2024 USD 0.030m. Supports cummins_st_kitts_engine_installation_30k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 29929.79; date_signed 2024-08-02.',
)
row_doc(
    "usmax_mexico_technical_security_systems_install_29k_2018",
    "infrastructure", "building_materials", "us",
    'USMAX — Mexico technical security systems installation',
    "Mexico",
    '10 Sep 2018: Department of State awards contract 19AQMM18F3428 to USMAX Corporation for technical security systems installation (PoP Mexico); obligated USD 28,811.46. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "28811.46", "2018-09-10", "2018", "", "",
    'Technical security systems installation, Mexico (USASpending description; site not named — lat/lon blank).',
    "usaspending_usmax_mexico_technical_security_systems_install_29k_2018",
    'TECHNICAL SECURITY SYSTEMS INSTALLATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F3428_1900_SAQMMA13D0055_1900/",
    'Actor: USMAX Corporation (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1113",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F3428_1900_SAQMMA13D0055_1900 (usmax_mexico_technical_security_systems_install_29k_2018). Signed 2018-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F3428_1900_SAQMMA13D0055_1900/.',
    'USASpending: usmax_mexico_technical_security_systems_install_29k_2018 USD 0.029m. Supports usmax_mexico_technical_security_systems_install_29k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 28811.46; date_signed 2018-09-10.',
)
row_doc(
    "misc_brazil_gso_6th_floor_renovation_46k_2011",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil GSO 6th floor renovation extra work',
    "Brazil",
    '3 Jun 2011: Department of State awards contract SBR82011M1740 for GSO 6th floor renovation extra work (PoP Brazil); obligated USD 46,429.93. CapEx face = award obligation. Exact building unnamed — lat/lon blank.',
    "46429.93", "2011-06-03", "2011", "", "",
    'GSO 6th floor renovation extra work, Brazil (USASpending description; floor named, site coords not stated — lat/lon blank).',
    "usaspending_misc_brazil_gso_6th_floor_renovation_46k_2011",
    'GSO - 6TH FLOOR RENOVATION EXTRA WORK',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82011M1740_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1113",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82011M1740_1900_-NONE-_-NONE- (misc_brazil_gso_6th_floor_renovation_46k_2011). Signed 2011-06-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82011M1740_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_gso_6th_floor_renovation_46k_2011 USD 0.046m. Supports misc_brazil_gso_6th_floor_renovation_46k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 46429.93; date_signed 2011-06-03.',
)
row_doc(
    "misc_haiti_reyes_compound_utility_power_connection_38k_2024",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Haiti Reyes compound utility power connection 2nd phase',
    "Haiti",
    '16 Jul 2024: Department of State awards contract 19HA7024P0834 for utility power connection at Reyes compound 2nd phase (PoP Haiti); obligated USD 37,981.46. CapEx face = award obligation. Reyes compound named; site coords not stated — lat/lon blank.',
    "37981.46", "2024-07-16", "2024", "", "",
    'Utility power connection at Reyes compound 2nd phase, Haiti (USASpending description; Reyes compound named, site coords not stated — lat/lon blank).',
    "usaspending_misc_haiti_reyes_compound_utility_power_connection_38k_2024",
    'FAC-UTILITY POWER CONNECTION AT REYES COMPOUND 2ND PHASE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7024P0834_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Weight under-covered Haiti.',
    "hunt_cycle1113",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7024P0834_1900_-NONE-_-NONE- (misc_haiti_reyes_compound_utility_power_connection_38k_2024). Signed 2024-07-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7024P0834_1900_-NONE-_-NONE-/.',
    'USASpending: misc_haiti_reyes_compound_utility_power_connection_38k_2024 USD 0.038m. Supports misc_haiti_reyes_compound_utility_power_connection_38k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37981.46; date_signed 2024-07-16.',
)
row_doc(
    "misc_panama_nec_consulate_parking_lot_38k_2011",
    "infrastructure", "bridges_roads", "other",
    'Miscellaneous foreign awardees — Panama NEC consulate customer parking lot',
    "Panama",
    '25 Mar 2011: Department of State awards contract SPM07011M0253 to build new parking lot for consulate customers at NEC (PoP Panama); obligated USD 37,875. CapEx face = award obligation. NEC named; site coords not stated — lat/lon blank.',
    "37875", "2011-03-25", "2011", "", "",
    'Build new parking lot for consulate customers at NEC, Panama (USASpending description; NEC named, site coords not stated — lat/lon blank).',
    "usaspending_misc_panama_nec_consulate_parking_lot_38k_2011",
    'BUILD NEW PARKING LOT FOR CONSULATE CUSTOMERS AT NEC',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07011M0253_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.',
    "hunt_cycle1113",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07011M0253_1900_-NONE-_-NONE- (misc_panama_nec_consulate_parking_lot_38k_2011). Signed 2011-03-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07011M0253_1900_-NONE-_-NONE-/.',
    'USASpending: misc_panama_nec_consulate_parking_lot_38k_2011 USD 0.038m. Supports misc_panama_nec_consulate_parking_lot_38k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37875; date_signed 2011-03-25.',
)

# === Cycle 1114 (seed 20262114) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "alban_tractor_guyana_usaid_generator_28k_2015",
    "energy", "power_plants_grid", "us",
    'Alban Tractor — Guyana USAID generator',
    "Guyana",
    '29 Sep 2015: Department of State awards contract SGY20015M0365 to Alban Tractor, LLC for USAID generator (PoP Guyana); obligated USD 27,710. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "27710", "2015-09-29", "2015", "", "",
    'USAID generator, Guyana (USASpending description; site not named — lat/lon blank).',
    "usaspending_alban_tractor_guyana_usaid_generator_28k_2015",
    'USAID GENERATOR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20015M0365_1900_-NONE-_-NONE-/",
    'Actor: Alban Tractor, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1114",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGY20015M0365_1900_-NONE-_-NONE- (alban_tractor_guyana_usaid_generator_28k_2015). Signed 2015-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20015M0365_1900_-NONE-_-NONE-/.',
    'USASpending: alban_tractor_guyana_usaid_generator_28k_2015 USD 0.028m. Supports alban_tractor_guyana_usaid_generator_28k_2015.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27710; date_signed 2015-09-29.',
)
row_doc(
    "southwestern_petroleum_honduras_obx_roof_coating_28k_2013",
    "infrastructure", "building_materials", "us",
    'Southwestern Petroleum — Honduras OBX roof coating products',
    "Honduras",
    '17 Sep 2013: Department of State awards contract SHO80013M0790 to Southwestern Petroleum Corporation for purchase of roof coating products for OBX (PoP Honduras); obligated USD 27,644.26. CapEx face = award obligation. Exact OBX unnamed — lat/lon blank.',
    "27644.26", "2013-09-17", "2013", "", "",
    'Purchase of roof coating products for OBX, Honduras (USASpending description; OBX named, site coords not stated — lat/lon blank).',
    "usaspending_southwestern_petroleum_honduras_obx_roof_coating_28k_2013",
    'FM- PURCHASE OF ROOF COATING PRODUCTS FOR OBX',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80013M0790_1900_-NONE-_-NONE-/",
    'Actor: Southwestern Petroleum Corporation (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1114",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80013M0790_1900_-NONE-_-NONE- (southwestern_petroleum_honduras_obx_roof_coating_28k_2013). Signed 2013-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80013M0790_1900_-NONE-_-NONE-/.',
    'USASpending: southwestern_petroleum_honduras_obx_roof_coating_28k_2013 USD 0.028m. Supports southwestern_petroleum_honduras_obx_roof_coating_28k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27644.26; date_signed 2013-09-17.',
)
row_doc(
    "misc_peru_iquitos_lab_admin_roof_insulation_38k_2011",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Peru Iquitos lab and admin roof building insulation',
    "Peru",
    '29 Sep 2011: Department of State awards contract SPE50011M1440 for Iquitos lab and admin roof building insulation (PoP Peru); obligated USD 37,996. CapEx face = award obligation. Iquitos named; site coords not stated — lat/lon blank.',
    "37996", "2011-09-29", "2011", "", "",
    'Iquitos lab and admin roof building insulation, Peru (USASpending description; Iquitos named, site coords not stated — lat/lon blank).',
    "usaspending_misc_peru_iquitos_lab_admin_roof_insulation_38k_2011",
    'FAC - IQUITOS LAB AND ADMIN ROOF BUILDING INSULATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50011M1440_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1114",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50011M1440_1900_-NONE-_-NONE- (misc_peru_iquitos_lab_admin_roof_insulation_38k_2011). Signed 2011-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50011M1440_1900_-NONE-_-NONE-/.',
    'USASpending: misc_peru_iquitos_lab_admin_roof_insulation_38k_2011 USD 0.038m. Supports misc_peru_iquitos_lab_admin_roof_insulation_38k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37996; date_signed 2011-09-29.',
)
row_doc(
    "misc_jamaica_wall_floor_tiles_38k_2023",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Jamaica FAC wall and floor tiles',
    "Jamaica",
    '25 Aug 2023: Department of State awards contract 19JM3723P1395 for wall and floor tiles (PoP Jamaica); obligated USD 37,799.11. CapEx face = award obligation. Exact building unnamed — lat/lon blank.',
    "37799.11", "2023-08-25", "2023", "", "",
    'Wall and floor tiles, Jamaica (USASpending description; building not named — lat/lon blank).',
    "usaspending_misc_jamaica_wall_floor_tiles_38k_2023",
    'FAC - WALL & FLOOR TILES',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3723P1395_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1114",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3723P1395_1900_-NONE-_-NONE- (misc_jamaica_wall_floor_tiles_38k_2023). Signed 2023-08-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3723P1395_1900_-NONE-_-NONE-/.',
    'USASpending: misc_jamaica_wall_floor_tiles_38k_2023 USD 0.038m. Supports misc_jamaica_wall_floor_tiles_38k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37799.11; date_signed 2023-08-25.',
)
row_doc(
    "misc_chile_ups_installation_38k_2023",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Chile UPS installation',
    "Chile",
    '3 Apr 2023: Department of State awards contract 19C18023P0646 for UPS installation (PoP Chile); obligated USD 37,722.68. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "37722.68", "2023-04-03", "2023", "", "",
    'UPS installation, Chile (USASpending description; site not named — lat/lon blank).',
    "usaspending_misc_chile_ups_installation_38k_2023",
    'UPS INSTALLATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18023P0646_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1114",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C18023P0646_1900_-NONE-_-NONE- (misc_chile_ups_installation_38k_2023). Signed 2023-04-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18023P0646_1900_-NONE-_-NONE-/.',
    'USASpending: misc_chile_ups_installation_38k_2023 USD 0.038m. Supports misc_chile_ups_installation_38k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37722.68; date_signed 2023-04-03.',
)

# === Cycle 1115 (seed 20262115) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "caterpillar_honduras_nas_residences_generator_28k_2012",
    "energy", "power_plants_grid", "us",
    'Caterpillar — Honduras NAS director/deputy residences generator',
    "Honduras",
    '27 Sep 2012: Department of State awards contract SHO80012F0259 to Caterpillar Inc for INL/PDANDS generator for NAS director/deputy residences (PoP Honduras); obligated USD 27,642.72. CapEx face = award obligation. Exact residences unnamed — lat/lon blank.',
    "27642.72", "2012-09-27", "2012", "", "",
    'INL/PDANDS generator for NAS director/deputy residences, Honduras (USASpending description; residences not named — lat/lon blank).',
    "usaspending_caterpillar_honduras_nas_residences_generator_28k_2012",
    'INL/PDANDS GENERATOR FOR NAS DIRECTOR/DEPUTY RESIDENCES 1930.0',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80012F0259_1900_GS07F5666R_4730/",
    'Actor: Caterpillar Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1115",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80012F0259_1900_GS07F5666R_4730 (caterpillar_honduras_nas_residences_generator_28k_2012). Signed 2012-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80012F0259_1900_GS07F5666R_4730/.',
    'USASpending: caterpillar_honduras_nas_residences_generator_28k_2012 USD 0.028m. Supports caterpillar_honduras_nas_residences_generator_28k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27642.72; date_signed 2012-09-27.',
)
row_doc(
    "bentley_mills_mexico_franklin_library_carpet_27k_2017",
    "infrastructure", "building_materials", "us",
    'Bentley Mills — Mexico Benjamin Franklin Library carpet tile supply',
    "Mexico",
    '1 Aug 2017: Department of State awards contract SMX53017M1191 to Bentley Mills Inc for carpet tile supply for the Benjamin Franklin Library (PoP Mexico); obligated USD 27,465.8. CapEx face = award obligation. Library named; site coords not stated — lat/lon blank.',
    "27465.8", "2017-08-01", "2017", "", "",
    'Carpet tile supply for the Benjamin Franklin Library, Mexico (USASpending description; library named, site coords not stated — lat/lon blank).',
    "usaspending_bentley_mills_mexico_franklin_library_carpet_27k_2017",
    'CARPET TILE SUPPLY FOR THE BENJAMIN FRANKLIN LIBRARY',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53017M1191_1900_-NONE-_-NONE-/",
    'Actor: Bentley Mills Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1115",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53017M1191_1900_-NONE-_-NONE- (bentley_mills_mexico_franklin_library_carpet_27k_2017). Signed 2017-08-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53017M1191_1900_-NONE-_-NONE-/.',
    'USASpending: bentley_mills_mexico_franklin_library_carpet_27k_2017 USD 0.027m. Supports bentley_mills_mexico_franklin_library_carpet_27k_2017.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27465.8; date_signed 2017-08-01.',
)
row_doc(
    "misc_haiti_stecher_roumain_safety_fence_38k_2018",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Haiti Stecher-Roumain safety fence',
    "Haiti",
    '16 Jul 2018: Department of State awards contract 19HA7018P0958 for new Stecher-Roumain safety fence (PoP Haiti); obligated USD 37,647.01. CapEx face = award obligation. Stecher-Roumain named; site coords not stated — lat/lon blank.',
    "37647.01", "2018-07-16", "2018", "", "",
    'New Stecher-Roumain safety fence, Haiti (USASpending description; Stecher-Roumain named, site coords not stated — lat/lon blank).',
    "usaspending_misc_haiti_stecher_roumain_safety_fence_38k_2018",
    'NEW STECHER-ROUMAIN SAFETY FENCE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7018P0958_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Weight under-covered Haiti.',
    "hunt_cycle1115",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7018P0958_1900_-NONE-_-NONE- (misc_haiti_stecher_roumain_safety_fence_38k_2018). Signed 2018-07-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7018P0958_1900_-NONE-_-NONE-/.',
    'USASpending: misc_haiti_stecher_roumain_safety_fence_38k_2018 USD 0.038m. Supports misc_haiti_stecher_roumain_safety_fence_38k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37647.01; date_signed 2018-07-16.',
)
row_doc(
    "misc_bolivia_north_patio_granite_pavers_38k_2010",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Bolivia north patio terrazzo tile replacement with granite pavers',
    "Bolivia",
    '20 Jul 2010: Department of State awards contract SBL40010M0545 to replace north patio terrazzo tile with granite pavers (PoP Bolivia); obligated USD 37,604.59. CapEx face = award obligation. Exact patio unnamed — lat/lon blank.',
    "37604.59", "2010-07-20", "2010", "", "",
    'Replace north patio terrazzo tile with granite pavers, Bolivia (USASpending description; patio named, site coords not stated — lat/lon blank).',
    "usaspending_misc_bolivia_north_patio_granite_pavers_38k_2010",
    'REPLACE NORTH PATIO TERRAZO TILE WITHGRANITE PAVERS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40010M0545_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1115",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBL40010M0545_1900_-NONE-_-NONE- (misc_bolivia_north_patio_granite_pavers_38k_2010). Signed 2010-07-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40010M0545_1900_-NONE-_-NONE-/.',
    'USASpending: misc_bolivia_north_patio_granite_pavers_38k_2010 USD 0.038m. Supports misc_bolivia_north_patio_granite_pavers_38k_2010.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37604.59; date_signed 2010-07-20.',
)
row_doc(
    "misc_mexico_cooling_tower_basins_replacement_37k_2021",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Mexico FAC OBO cooling tower basins replacement',
    "Mexico",
    '12 May 2021: Department of State awards contract 19MX5321P0522 for cooling tower basins replacement FY21 (PoP Mexico); obligated USD 36,710.64. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "36710.64", "2021-05-12", "2021", "", "",
    'Cooling tower basins replacement FY21, Mexico (USASpending description; site not named — lat/lon blank).',
    "usaspending_misc_mexico_cooling_tower_basins_replacement_37k_2021",
    'MX-FAC-OBO-COOLING TOWER BASINS REPLACEMENT-FY21',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5321P0522_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1115",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5321P0522_1900_-NONE-_-NONE- (misc_mexico_cooling_tower_basins_replacement_37k_2021). Signed 2021-05-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5321P0522_1900_-NONE-_-NONE-/.',
    'USASpending: misc_mexico_cooling_tower_basins_replacement_37k_2021 USD 0.037m. Supports misc_mexico_cooling_tower_basins_replacement_37k_2021.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36710.64; date_signed 2021-05-12.',
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
