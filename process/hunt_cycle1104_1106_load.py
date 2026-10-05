#!/usr/bin/env python3
"""Cycles 1104–1106: USASpending LatAm CapEx residual (~USD0.030–0.056m).

Seeds: 20262104–20262106. Thin top-up dry.
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


# === Cycle 1104 (seed 20262104) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "haroldson_mexico_hardwood_floor_go_42k_2013",
    "infrastructure", "building_materials", "us",
    'Haroldson Group International — Mexico hardwood floor for government-owned property',
    "Mexico",
    '25 Jun 2013: Department of State awards contract SMX53013M0879 to Haroldson Group International, LLC for hardwood floor for GO (PoP Mexico); obligated USD 41,519.75. CapEx face = award obligation. Exact property unnamed — lat/lon blank.',
    "41519.75", "2013-06-25", "2013", "", "",
    'Hardwood floor for government-owned property, Mexico (USASpending description; property not named — lat/lon blank).',
    "usaspending_haroldson_mexico_hardwood_floor_go_42k_2013",
    'MEX- FAC 1901.0 / HARDWOOD FLOOR FOR GO IGF::OT::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0879_1900_-NONE-_-NONE-/",
    'Actor: Haroldson Group International, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1104",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53013M0879_1900_-NONE-_-NONE- (haroldson_mexico_hardwood_floor_go_42k_2013). Signed 2013-06-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0879_1900_-NONE-_-NONE-/.',
    'USASpending: haroldson_mexico_hardwood_floor_go_42k_2013 USD 0.042m. Supports haroldson_mexico_hardwood_floor_go_42k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 41519.75; date_signed 2013-06-25.',
)
row_doc(
    "caterpillar_honduras_three_generators_d30_41k_2012",
    "energy", "power_plants_grid", "us",
    'Caterpillar — Honduras three CAT D30-8S generators for leased residences',
    "Honduras",
    '13 Sep 2012: USAID awards contract AID522O1200057 to Caterpillar Inc for purchase of 3 generators CAT D30-8S for leased residences (PoP Honduras); obligated USD 41,464.08. CapEx face = award obligation. Exact residence sites unnamed — lat/lon blank.',
    "41464.08", "2012-09-13", "2012", "", "",
    'Purchase of 3 generators CAT D30-8S for leased residences, Honduras (USASpending description; sites not named — lat/lon blank).',
    "usaspending_caterpillar_honduras_three_generators_d30_41k_2012",
    'PURCHASE OF 3 GENERATORS CAT D30-8S FOR LEASED RESIDENCES.- FOR:(OTI C.R.)+(OTI D.C.R.)+(DLI)',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1200057_7200_-NONE-_-NONE-/",
    'Actor: Caterpillar Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1104",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID522O1200057_7200_-NONE-_-NONE- (caterpillar_honduras_three_generators_d30_41k_2012). Signed 2012-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1200057_7200_-NONE-_-NONE-/.',
    'USASpending: caterpillar_honduras_three_generators_d30_41k_2012 USD 0.041m. Supports caterpillar_honduras_three_generators_d30_41k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 41464.08; date_signed 2012-09-13.',
)
row_doc(
    "gordon_panama_gamboa_exterior_paint_56k_2020",
    "infrastructure", "building_materials", "other",
    'Gordon & Gordons Services — Panama Gamboa buildings 183/150/152 exterior paint and repair',
    "Panama",
    '17 Mar 2020: Smithsonian awards contract 33312920P00442123 to Gordon & Gordons Services, Inc. for Gamboa Bldg 183, 150, 152 exterior paint and repair (PoP Panama); obligated USD 55,961.60. CapEx face = award obligation. Exact building footprints unnamed — lat/lon blank.',
    "55961.60", "2020-03-17", "2020", "", "",
    'Gamboa Bldg 183, 150, 152 exterior paint and repair, Panama (USASpending description; Gamboa named, building coords not stated — lat/lon blank).',
    "usaspending_gordon_panama_gamboa_exterior_paint_56k_2020",
    'GAMBOA BLDG 183, 150, 152 EXTERIOR PAINT&REPAIR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312920P00442123_3300_-NONE-_-NONE-/",
    'Actor: Gordon & Gordons Services, Inc. (Panama-coded recipient) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1104",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33312920P00442123_3300_-NONE-_-NONE- (gordon_panama_gamboa_exterior_paint_56k_2020). Signed 2020-03-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312920P00442123_3300_-NONE-_-NONE-/.',
    'USASpending: gordon_panama_gamboa_exterior_paint_56k_2020 USD 0.056m. Supports gordon_panama_gamboa_exterior_paint_56k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55961.60; date_signed 2020-03-17.',
)
row_doc(
    "egarco_ecuador_chancery_open_areas_paint_56k_2022",
    "infrastructure", "building_materials", "other",
    'Egarco Egas Arguello — Ecuador chancery open areas painting',
    "Ecuador",
    '28 Sep 2022: Department of State awards contract 19EC7522C0019 to Egarco Egas Arguello Cia Ltda for chancery open areas painting (PoP Ecuador); obligated USD 55,905.79. CapEx face = award obligation. Exact areas unnamed — lat/lon blank.',
    "55905.79", "2022-09-28", "2022", "", "",
    'Chancery open areas painting, Ecuador (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_egarco_ecuador_chancery_open_areas_paint_56k_2022",
    'FAC-7904-ICASS-CHANCERY-FWP#196-CHANCERY OPEN AREAS PAINTING',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0019_1900_-NONE-_-NONE-/",
    'Actor: Egarco Egas Arguello Cia Ltda (Ecuador) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1104",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7522C0019_1900_-NONE-_-NONE- (egarco_ecuador_chancery_open_areas_paint_56k_2022). Signed 2022-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0019_1900_-NONE-_-NONE-/.',
    'USASpending: egarco_ecuador_chancery_open_areas_paint_56k_2022 USD 0.056m. Supports egarco_ecuador_chancery_open_areas_paint_56k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55905.79; date_signed 2022-09-28.',
)
row_doc(
    "misc_mexico_plumbing_supplies_renovation_53k_2011",
    "resources", "water", "other",
    'Miscellaneous foreign awardees — Mexico EOY plumbing supplies for renovation of GO properties',
    "Mexico",
    '26 Sep 2011: Department of State awards contract SMX53011M1739 for EOY plumbing supplies for renovation GO properties (PoP Mexico); obligated USD 52,874.37. CapEx face = award obligation. Exact properties unnamed — lat/lon blank.',
    "52874.37", "2011-09-26", "2011", "", "",
    'Plumbing supplies for renovation of government-owned properties, Mexico (USASpending description; properties not named — lat/lon blank).',
    "usaspending_misc_mexico_plumbing_supplies_renovation_53k_2011",
    '7901/MEX EOY PLUMBING SUPPLIES FOR RENOVATION GO PROPERTIES',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M1739_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water. Holdover closed.',
    "hunt_cycle1104",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53011M1739_1900_-NONE-_-NONE- (misc_mexico_plumbing_supplies_renovation_53k_2011). Signed 2011-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M1739_1900_-NONE-_-NONE-/.',
    'USASpending: misc_mexico_plumbing_supplies_renovation_53k_2011 USD 0.053m. Supports misc_mexico_plumbing_supplies_renovation_53k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 52874.37; date_signed 2011-09-26.',
)

# === Cycle 1105 (seed 20262105) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "pruitt_mexico_cancun_rcag_ladder_40k_2016",
    "infrastructure", "building_materials", "us",
    'H.L. Pruitt — Mexico Cancun RCAG facility ladder installation',
    "Mexico",
    '23 Feb 2016: FAA awards contract DTFACN16C00100 to H.L. Pruitt Corp. for ladder installation at remote communications air/ground (RCAG) facility in Cancun, Mexico; obligated USD 39,500. CapEx face = award obligation. Exact RCAG site unnamed — lat/lon blank.',
    "39500", "2016-02-23", "2016", "", "",
    'Ladder installation at RCAG facility in Cancun, Mexico (USASpending description; Cancun named, site coords not stated — lat/lon blank).',
    "usaspending_pruitt_mexico_cancun_rcag_ladder_40k_2016",
    'LADDER INSTALLATION AT REMOTE COMMUNICATIONS AIR/AROUND (RCAG)FACILITY IN CANCUN, MEXICO IGF::CT::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_DTFACN16C00100_6920_-NONE-_-NONE-/",
    'Actor: H.L. Pruitt Corp. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1105",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_DTFACN16C00100_6920_-NONE-_-NONE- (pruitt_mexico_cancun_rcag_ladder_40k_2016). Signed 2016-02-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_DTFACN16C00100_6920_-NONE-_-NONE-/.',
    'USASpending: pruitt_mexico_cancun_rcag_ladder_40k_2016 USD 0.040m. Supports pruitt_mexico_cancun_rcag_ladder_40k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 39500; date_signed 2016-02-23.',
)
row_doc(
    "tidewater_haiti_les_cayes_fuel_dispenser_39k_2019",
    "infrastructure", "building_materials", "us",
    'Tidewater — Haiti Les Cayes CG marine-grade fuel dispenser purchase and installation',
    "Haiti",
    '12 Sep 2019: Department of State awards contract 19HA7019P0574 to Tidewater, Inc. for purchase and installation of marine grade fuel dispenser at Les Cayes CG (PoP Haiti); obligated USD 38,798.22. CapEx face = award obligation. Exact CG site unnamed — lat/lon blank.',
    "38798.22", "2019-09-12", "2019", "", "",
    'Purchase and installation marine grade fuel dispenser at Les Cayes CG, Haiti (USASpending description; Les Cayes named, site coords not stated — lat/lon blank).',
    "usaspending_tidewater_haiti_les_cayes_fuel_dispenser_39k_2019",
    'PURCHASE AND INSTALLATION MARINE GRADE FUEL DISPENSER AT LES CAYES CG',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7019P0574_1900_-NONE-_-NONE-/",
    'Actor: Tidewater, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Weight under-covered Haiti.',
    "hunt_cycle1105",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7019P0574_1900_-NONE-_-NONE- (tidewater_haiti_les_cayes_fuel_dispenser_39k_2019). Signed 2019-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7019P0574_1900_-NONE-_-NONE-/.',
    'USASpending: tidewater_haiti_les_cayes_fuel_dispenser_39k_2019 USD 0.039m. Supports tidewater_haiti_les_cayes_fuel_dispenser_39k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 38798.22; date_signed 2019-09-12.',
)
row_doc(
    "zarza_paraguay_building_electrical_wiring_56k_2015",
    "infrastructure", "building_materials", "other",
    'Zarza Morel Miguel Antonio — Paraguay building maintenance/repair including electric wiring and light fixture installation',
    "Paraguay",
    '22 Sep 2015: USAID awards contract AID526O1500031 to Zarza Morel, Miguel Antonio for general maintenance and repair of the building, including electric wiring, installation of light fixtures (PoP Paraguay); obligated USD 55,856. CapEx face = award obligation. Exact building unnamed — lat/lon blank.',
    "55856", "2015-09-22", "2015", "", "",
    'Building repair including electric wiring and light fixture installation, Paraguay (USASpending description; building not named — lat/lon blank).',
    "usaspending_zarza_paraguay_building_electrical_wiring_56k_2015",
    'IGF::CL,CT::IGF. GENERAL MAINTENANCE AND REPAIR OF THE BUILDING, INCLUDING ELECTRIC WIRING, INSTALLATION OF LIGHT FIXTUR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID526O1500031_7200_-NONE-_-NONE-/",
    'Actor: Zarza Morel, Miguel Antonio (Paraguay) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1105",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID526O1500031_7200_-NONE-_-NONE- (zarza_paraguay_building_electrical_wiring_56k_2015). Signed 2015-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID526O1500031_7200_-NONE-_-NONE-/.',
    'USASpending: zarza_paraguay_building_electrical_wiring_56k_2015 USD 0.056m. Supports zarza_paraguay_building_electrical_wiring_56k_2015.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55856; date_signed 2015-09-22.',
)
row_doc(
    "misc_brazil_fence_paint_53k_2013",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil fence paint',
    "Brazil",
    '24 Sep 2013: Department of State awards contract SBR93013C0014 for fence paint (PoP Brazil); obligated USD 52,592.73. CapEx face = award obligation. Exact fence unnamed — lat/lon blank.',
    "52592.73", "2013-09-24", "2013", "", "",
    'Fence paint, Brazil (USASpending description; fence not named — lat/lon blank).',
    "usaspending_misc_brazil_fence_paint_53k_2013",
    '7901C - FENCE PAINT',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93013C0014_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1105",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR93013C0014_1900_-NONE-_-NONE- (misc_brazil_fence_paint_53k_2013). Signed 2013-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93013C0014_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_fence_paint_53k_2013 USD 0.053m. Supports misc_brazil_fence_paint_53k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 52592.73; date_signed 2013-09-24.',
)
row_doc(
    "misc_brazil_cgr_renovation_50k_2013",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil CGR renovation',
    "Brazil",
    '9 Sep 2013: Department of State awards contract SBR82013M1507 for FAC CGR renovation (PoP Brazil); obligated USD 50,150.67. CapEx face = award obligation. Exact CGR unnamed — lat/lon blank.',
    "50150.67", "2013-09-09", "2013", "", "",
    'FAC CGR renovation, Brazil (USASpending description; CGR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_brazil_cgr_renovation_50k_2013",
    'IGF::OT::IGF  FAC- CGR RENOVATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82013M1507_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1105",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82013M1507_1900_-NONE-_-NONE- (misc_brazil_cgr_renovation_50k_2013). Signed 2013-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82013M1507_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_cgr_renovation_50k_2013 USD 0.050m. Supports misc_brazil_cgr_renovation_50k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 50150.67; date_signed 2013-09-09.',
)

# === Cycle 1106 (seed 20262106) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "obera_panama_ops_center_flooring_door_31k_2025",
    "infrastructure", "building_materials", "us",
    'Obera — Panama Operations Center flooring and door installation',
    "Panama",
    '9 Jul 2025: Department of Defense awards contract FA489025P0011 to Obera LLC for Panama Operations Center flooring and door installation (PoP Panama); obligated USD 31,328.95. CapEx face = award obligation. Exact ops center unnamed — lat/lon blank.',
    "31328.95", "2025-07-09", "2025", "", "",
    'Panama Operations Center flooring and door installation (USASpending description; ops center not named — lat/lon blank).',
    "usaspending_obera_panama_ops_center_flooring_door_31k_2025",
    'PANAMA OPERATIONS CENTER FLOORING AND DOOR INSTALLATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489025P0011_9700_-NONE-_-NONE-/",
    'Actor: Obera LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1106",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_FA489025P0011_9700_-NONE-_-NONE- (obera_panama_ops_center_flooring_door_31k_2025). Signed 2025-07-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_FA489025P0011_9700_-NONE-_-NONE-/.',
    'USASpending: obera_panama_ops_center_flooring_door_31k_2025 USD 0.031m. Supports obera_panama_ops_center_flooring_door_31k_2025.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 31328.95; date_signed 2025-07-09.',
)
row_doc(
    "bentley_mills_mexico_fcs_carpet_30k_2012",
    "infrastructure", "building_materials", "us",
    'Bentley Mills — Mexico FCS office carpet',
    "Mexico",
    '10 Sep 2012: Department of State awards contract SMX53012M1671 to Bentley Mills Inc for carpet for FCS office (PoP Mexico); obligated USD 30,095.42. CapEx face = award obligation. Exact FCS office unnamed — lat/lon blank.',
    "30095.42", "2012-09-10", "2012", "", "",
    'Carpet for FCS office, Mexico (USASpending description; office not named — lat/lon blank).',
    "usaspending_bentley_mills_mexico_fcs_carpet_30k_2012",
    'MEX/FCS/1300/CARPET FOR FCS OFFICE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M1671_1900_-NONE-_-NONE-/",
    'Actor: Bentley Mills Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1106",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53012M1671_1900_-NONE-_-NONE- (bentley_mills_mexico_fcs_carpet_30k_2012). Signed 2012-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M1671_1900_-NONE-_-NONE-/.',
    'USASpending: bentley_mills_mexico_fcs_carpet_30k_2012 USD 0.030m. Supports bentley_mills_mexico_fcs_carpet_30k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 30095.42; date_signed 2012-09-10.',
)
row_doc(
    "misc_colombia_hangar_renovation_39k_2012",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Colombia hangar renovation',
    "Colombia",
    '10 Sep 2012: Department of State awards contract SCO15012CN016 for hangar renovation (PoP Colombia); obligated USD 38,891.71. CapEx face = award obligation. Exact hangar unnamed — lat/lon blank.',
    "38891.71", "2012-09-10", "2012", "", "",
    'Hangar renovation, Colombia (USASpending description; hangar not named — lat/lon blank).',
    "usaspending_misc_colombia_hangar_renovation_39k_2012",
    'HANGAR RENOVATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012CN016_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1106",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15012CN016_1900_-NONE-_-NONE- (misc_colombia_hangar_renovation_39k_2012). Signed 2012-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012CN016_1900_-NONE-_-NONE-/.',
    'USASpending: misc_colombia_hangar_renovation_39k_2012 USD 0.039m. Supports misc_colombia_hangar_renovation_39k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 38891.71; date_signed 2012-09-10.',
)
row_doc(
    "misc_colombia_cmr_lift_interior_renovation_48k_2026",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Colombia CMR lift interior renovation',
    "Colombia",
    '22 Sep 2026: Department of State awards contract 19C02026C0009 for CMR lift interior renovation (PoP Colombia); obligated USD 48,369.61. CapEx face = award obligation. Exact lift unnamed — lat/lon blank.',
    "48369.61", "2026-09-22", "2026", "", "",
    'CMR lift interior renovation, Colombia (USASpending description; CMR named, lift coords not stated — lat/lon blank).',
    "usaspending_misc_colombia_cmr_lift_interior_renovation_48k_2026",
    'PR16298958: CMR LIFT INTERIOR RENOVATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026C0009_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1106",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02026C0009_1900_-NONE-_-NONE- (misc_colombia_cmr_lift_interior_renovation_48k_2026). Signed 2026-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026C0009_1900_-NONE-_-NONE-/.',
    'USASpending: misc_colombia_cmr_lift_interior_renovation_48k_2026 USD 0.048m. Supports misc_colombia_cmr_lift_interior_renovation_48k_2026.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 48369.61; date_signed 2026-09-22.',
)
row_doc(
    "corporate_computing_barbados_camera_install_53k_2017",
    "infrastructure", "building_materials", "other",
    'Corporate Computing — Barbados acquisition and installation of camera equipment',
    "Barbados",
    '31 Jul 2017: Department of State awards contract SBB21017M0703 to Corporate Computing Incorporated for acquisition and installation of camera equipment (PoP Barbados); obligated USD 53,280.69. CapEx face = award obligation. Exact camera sites unnamed — lat/lon blank.',
    "53280.69", "2017-07-31", "2017", "", "",
    'Acquisition and installation of camera equipment, Barbados (USASpending description; sites not named — lat/lon blank).',
    "usaspending_corporate_computing_barbados_camera_install_53k_2017",
    'IGF::OT::IGF ACQUISITION AND INSTALLATION OF CAMERA EQUIPMENT',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21017M0703_1900_-NONE-_-NONE-/",
    'Actor: Corporate Computing Incorporated (Barbados) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1106",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21017M0703_1900_-NONE-_-NONE- (corporate_computing_barbados_camera_install_53k_2017). Signed 2017-07-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21017M0703_1900_-NONE-_-NONE-/.',
    'USASpending: corporate_computing_barbados_camera_install_53k_2017 USD 0.053m. Supports corporate_computing_barbados_camera_install_53k_2017.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53280.69; date_signed 2017-07-31.',
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
