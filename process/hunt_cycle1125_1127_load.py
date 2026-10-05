#!/usr/bin/env python3
"""Cycles 1125–1127: USASpending LatAm CapEx residual (~USD0.021–0.036m).

Seeds: 20262125–20262127. Thin top-up dry.
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


# === Cycle 1125 (seed 20262125) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "mst_barbados_dive_tanks_27k_2024",
    "infrastructure", "building_materials", "us",
    'MST Maritime Management — Barbados dive tanks',
    "Barbados",
    '7 May 2024: Department of Defense awards contract W569QE24P0025 to MST Maritime Management LLC for dive tanks (PoP Barbados); obligated USD 27,230.8. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "27230.8", "2024-05-07", "2024", "", "",
    'Dive tanks, Barbados (USASpending description; site not named — lat/lon blank).',
    "usaspending_mst_barbados_dive_tanks_27k_2024",
    'DIVE TANKS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W569QE24P0025_9700_-NONE-_-NONE-/",
    'Actor: MST Maritime Management LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1125",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W569QE24P0025_9700_-NONE-_-NONE- (mst_barbados_dive_tanks_27k_2024). Signed 2024-05-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W569QE24P0025_9700_-NONE-_-NONE-/.',
    'USASpending: mst_barbados_dive_tanks_27k_2024 USD 0.027m. Supports mst_barbados_dive_tanks_27k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27230.8; date_signed 2024-05-07.',
)
row_doc(
    "polaris_brazil_warehouse_safety_upgrades_27k_2019",
    "infrastructure", "building_materials", "us",
    'Polaris Sales — Brazil warehouse safety upgrades EOFY19',
    "Brazil",
    '19 Sep 2019: Department of State awards contract 19BR9319P0843 to Polaris Sales Inc for warehouse safety upgrades EOFY19 (PoP Brazil); obligated USD 27,222.74. CapEx face = award obligation. Exact warehouse unnamed — lat/lon blank.',
    "27222.74", "2019-09-19", "2019", "", "",
    'Warehouse safety upgrades EOFY19, Brazil (USASpending description; warehouse not named — lat/lon blank).',
    "usaspending_polaris_brazil_warehouse_safety_upgrades_27k_2019",
    'SP/GSO/ICASS - EOFY19-WAREHOUSE SAFETY UPGRADES',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9319P0843_1900_-NONE-_-NONE-/",
    'Actor: Polaris Sales Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1125",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9319P0843_1900_-NONE-_-NONE- (polaris_brazil_warehouse_safety_upgrades_27k_2019). Signed 2019-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9319P0843_1900_-NONE-_-NONE-/.',
    'USASpending: polaris_brazil_warehouse_safety_upgrades_27k_2019 USD 0.027m. Supports polaris_brazil_warehouse_safety_upgrades_27k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 27222.74; date_signed 2019-09-19.',
)
row_doc(
    "vinpar_colombia_obs_towers_construct_renovate_36k_2013",
    "infrastructure", "building_materials", "other",
    'Construcciones Vinpar — Colombia construct and renovate OBS towers',
    "Colombia",
    '19 Jul 2013: Department of Defense awards contract W913FT13P0124 to Construcciones Vinpar S.A.S. to construct and renovate OBS towers (PoP Colombia); obligated USD 36,303.45. CapEx face = award obligation. Exact tower sites unnamed — lat/lon blank.',
    "36303.45", "2013-07-19", "2013", "", "",
    'Construct and renovate OBS towers, Colombia (USASpending description; sites not named — lat/lon blank).',
    "usaspending_vinpar_colombia_obs_towers_construct_renovate_36k_2013",
    'CONSTRUCT AND RENOVATE OBS TOWERS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13P0124_9700_-NONE-_-NONE-/",
    'Actor: Construcciones Vinpar S.A.S. (Colombia) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1125",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT13P0124_9700_-NONE-_-NONE- (vinpar_colombia_obs_towers_construct_renovate_36k_2013). Signed 2013-07-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13P0124_9700_-NONE-_-NONE-/.',
    'USASpending: vinpar_colombia_obs_towers_construct_renovate_36k_2013 USD 0.036m. Supports vinpar_colombia_obs_towers_construct_renovate_36k_2013.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36303.45; date_signed 2013-07-19.',
)
row_doc(
    "misc_peru_cmr_emr_chiller_replacement_36k_2010",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Peru CMR replace EMR chiller',
    "Peru",
    '23 Jun 2010: Department of State awards contract SPE50010C0039 for CMR replace EMR chiller (PoP Peru); obligated USD 36,239.86. CapEx face = award obligation. Exact CMR/EMR unnamed — lat/lon blank.',
    "36239.86", "2010-06-23", "2010", "", "",
    'CMR replace EMR chiller, Peru (USASpending description; CMR/EMR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_peru_cmr_emr_chiller_replacement_36k_2010",
    '06/21 CMR - REPLACE EMR CHILLER',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50010C0039_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1125",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50010C0039_1900_-NONE-_-NONE- (misc_peru_cmr_emr_chiller_replacement_36k_2010). Signed 2010-06-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50010C0039_1900_-NONE-_-NONE-/.',
    'USASpending: misc_peru_cmr_emr_chiller_replacement_36k_2010 USD 0.036m. Supports misc_peru_cmr_emr_chiller_replacement_36k_2010.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36239.86; date_signed 2010-06-23.',
)
row_doc(
    "bolanos_ecuador_roof_paint_rstr_fwp_36k_2022",
    "infrastructure", "building_materials", "other",
    'Bolanos Alban Fausto Tarquino — Ecuador roof paint RSTR FWP 269 and 270',
    "Ecuador",
    '5 May 2022: Department of State awards contract 19EC7522C0007 to Bolanos Alban Fausto Tarquino for roof paint RSTR FWP 269 and 270 (PoP Ecuador); obligated USD 36,206.5. CapEx face = award obligation. Exact residences unnamed — lat/lon blank.',
    "36206.5", "2022-05-05", "2022", "", "",
    'Roof paint RSTR FWP 269 and 270, Ecuador (USASpending description; FWP codes named, site coords not stated — lat/lon blank).',
    "usaspending_bolanos_ecuador_roof_paint_rstr_fwp_36k_2022",
    '1900.0-PR10529313-FAC-7901-7903-RSTR-FWP#269&270-ROOF PAINT',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0007_1900_-NONE-_-NONE-/",
    'Actor: Bolanos Alban Fausto Tarquino (Ecuador) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1125",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7522C0007_1900_-NONE-_-NONE- (bolanos_ecuador_roof_paint_rstr_fwp_36k_2022). Signed 2022-05-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522C0007_1900_-NONE-_-NONE-/.',
    'USASpending: bolanos_ecuador_roof_paint_rstr_fwp_36k_2022 USD 0.036m. Supports bolanos_ecuador_roof_paint_rstr_fwp_36k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36206.5; date_signed 2022-05-05.',
)

# === Cycle 1126 (seed 20262126) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "interface_peru_chancery_carpet_stock_24k_2015",
    "infrastructure", "building_materials", "us",
    'Interface Americas — Peru stock of carpet for chancery building',
    "Peru",
    '20 Mar 2015: Department of State awards contract SPE50015M0902 to Interface Americas Inc for stock of carpet for chancery building (PoP Peru); obligated USD 24,482.76. CapEx face = award obligation. Exact chancery unnamed — lat/lon blank.',
    "24482.76", "2015-03-20", "2015", "", "",
    'Stock of carpet for chancery building, Peru (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_interface_peru_chancery_carpet_stock_24k_2015",
    '3/17 FAC - STOCK OF CARPET FOR CHANCERY BUILDING',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M0902_1900_-NONE-_-NONE-/",
    'Actor: Interface Americas Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1126",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50015M0902_1900_-NONE-_-NONE- (interface_peru_chancery_carpet_stock_24k_2015). Signed 2015-03-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M0902_1900_-NONE-_-NONE-/.',
    'USASpending: interface_peru_chancery_carpet_stock_24k_2015 USD 0.024m. Supports interface_peru_chancery_carpet_stock_24k_2015.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 24482.76; date_signed 2015-03-20.',
)
row_doc(
    "interface_peru_annex_carpet_stock_22k_2014",
    "infrastructure", "building_materials", "us",
    'Interface Americas — Peru stock of carpet for annex building',
    "Peru",
    '14 Aug 2014: Department of State awards contract SPE50014M1829 to Interface Americas Inc for stock of carpet for annex building (PoP Peru); obligated USD 21,573.35. CapEx face = award obligation. Exact annex unnamed — lat/lon blank.',
    "21573.35", "2014-08-14", "2014", "", "",
    'Stock of carpet for annex building, Peru (USASpending description; annex named, site coords not stated — lat/lon blank).',
    "usaspending_interface_peru_annex_carpet_stock_22k_2014",
    '8/11 FAC - STOCK OF CARPET FOR ANNEX BUILDING',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M1829_1900_-NONE-_-NONE-/",
    'Actor: Interface Americas Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1126",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50014M1829_1900_-NONE-_-NONE- (interface_peru_annex_carpet_stock_22k_2014). Signed 2014-08-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M1829_1900_-NONE-_-NONE-/.',
    'USASpending: interface_peru_annex_carpet_stock_22k_2014 USD 0.022m. Supports interface_peru_annex_carpet_stock_22k_2014.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 21573.35; date_signed 2014-08-14.',
)
row_doc(
    "misc_chile_rso_grills_installation_36k_2016",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Chile RSO grills installation',
    "Chile",
    '2 Jun 2016: Department of State awards contract SCI80016M0596 for RSO grills installation (PoP Chile); obligated USD 36,167.06. CapEx face = award obligation. Exact RSO site unnamed — lat/lon blank.',
    "36167.06", "2016-06-02", "2016", "", "",
    'RSO grills installation, Chile (USASpending description; RSO named, site coords not stated — lat/lon blank).',
    "usaspending_misc_chile_rso_grills_installation_36k_2016",
    'RSO - GRILLS INSTALLATION IGF::CL::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80016M0596_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1126",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCI80016M0596_1900_-NONE-_-NONE- (misc_chile_rso_grills_installation_36k_2016). Signed 2016-06-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80016M0596_1900_-NONE-_-NONE-/.',
    'USASpending: misc_chile_rso_grills_installation_36k_2016 USD 0.036m. Supports misc_chile_rso_grills_installation_36k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36167.06; date_signed 2016-06-02.',
)
row_doc(
    "bonatti_honduras_soto_cano_condensing_unit_install_36k_2017",
    "energy", "power_plants_grid", "other",
    'Bonatti Ingenieros y Arquitectos — Honduras Soto Cano Air Base condensing unit installation',
    "Honduras",
    '13 Mar 2017: Department of Defense awards contract W912QM17P0018 to Bonatti Ingenieros y Arquitectos Sociedad Anonima for condensing unit 10.1 kW installation at Soto Cano Air Base (PoP Honduras); obligated USD 36,150.38. CapEx face = award obligation. Soto Cano named; site coords not stated — lat/lon blank.',
    "36150.38", "2017-03-13", "2017", "", "",
    'Condensing unit 10.1 kW installation at Soto Cano Air Base, Honduras (USASpending description; Soto Cano named, site coords not stated — lat/lon blank).',
    "usaspending_bonatti_honduras_soto_cano_condensing_unit_install_36k_2017",
    'IGF::OT::IGF CONDENSING UNIT 10.1 KW INSTALLATION AT SOTO CANO AIR BASE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM17P0018_9700_-NONE-_-NONE-/",
    'Actor: Bonatti Ingenieros y Arquitectos Sociedad Anonima (Guatemala-registered) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1126",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QM17P0018_9700_-NONE-_-NONE- (bonatti_honduras_soto_cano_condensing_unit_install_36k_2017). Signed 2017-03-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QM17P0018_9700_-NONE-_-NONE-/.',
    'USASpending: bonatti_honduras_soto_cano_condensing_unit_install_36k_2017 USD 0.036m. Supports bonatti_honduras_soto_cano_condensing_unit_install_36k_2017.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36150.38; date_signed 2017-03-13.',
)
row_doc(
    "misc_brazil_compound_perimeter_lights_replacement_36k_2019",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil compound perimeter lights replacement',
    "Brazil",
    '19 Apr 2019: Department of State awards contract 19BR9319P0362 for replacement of compound perimeter lights (PoP Brazil); obligated USD 36,070.7. CapEx face = award obligation. Exact compound unnamed — lat/lon blank.',
    "36070.7", "2019-04-19", "2019", "", "",
    'Replacement of compound perimeter lights, Brazil (USASpending description; compound not named — lat/lon blank).',
    "usaspending_misc_brazil_compound_perimeter_lights_replacement_36k_2019",
    'SP/FAC/7901 - REPLACEMENT OF COMPOUND PERIMETER LIGTHS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9319P0362_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1126",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9319P0362_1900_-NONE-_-NONE- (misc_brazil_compound_perimeter_lights_replacement_36k_2019). Signed 2019-04-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9319P0362_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_compound_perimeter_lights_replacement_36k_2019 USD 0.036m. Supports misc_brazil_compound_perimeter_lights_replacement_36k_2019.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36070.7; date_signed 2019-04-19.',
)

# === Cycle 1127 (seed 20262127) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "spectrum_dominican_republic_mechanical_interlock_install_22k_2016",
    "infrastructure", "building_materials", "us",
    'Spectrum Electrical Services — Dominican Republic program relay and mechanical interlock installation',
    "Dominican Republic",
    '25 Jul 2016: Department of State awards contract SDR86016M0623 to Spectrum Electrical Services, Inc for program relay and installing mechanical interlock (PoP Dominican Republic); obligated USD 21,555.54. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "21555.54", "2016-07-25", "2016", "", "",
    'Program relay and installing mechanical interlock, Dominican Republic (USASpending description; site not named — lat/lon blank).',
    "usaspending_spectrum_dominican_republic_mechanical_interlock_install_22k_2016",
    'IGF::CL::IGF FOR CLOSELY ASSOCIATED  PROGRAM RELAY AND INSTALLING MECHANICAL INTERLOCK---SPECTRUM',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86016M0623_1900_-NONE-_-NONE-/",
    'Actor: Spectrum Electrical Services, Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1127",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86016M0623_1900_-NONE-_-NONE- (spectrum_dominican_republic_mechanical_interlock_install_22k_2016). Signed 2016-07-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86016M0623_1900_-NONE-_-NONE-/.',
    'USASpending: spectrum_dominican_republic_mechanical_interlock_install_22k_2016 USD 0.022m. Supports spectrum_dominican_republic_mechanical_interlock_install_22k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 21555.54; date_signed 2016-07-25.',
)
row_doc(
    "harden_mexico_metal_door_screen_21k_2023",
    "infrastructure", "building_materials", "us",
    'Harden Architectural Security Products — Mexico metal door screen for international embassies',
    "Mexico",
    '23 Aug 2023: Department of State awards contract 19AQMM23P1077 to Harden Architectural Security Products, LLC for metal door screen etc. for international embassies (PoP Mexico); obligated USD 21,453. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.',
    "21453", "2023-08-23", "2023", "", "",
    'Metal door screen for international embassies, Mexico (USASpending description; embassy not named — lat/lon blank).',
    "usaspending_harden_mexico_metal_door_screen_21k_2023",
    'METAL, DOOR, SCREEN ETC. FOR INTERNATIONAL EMBASSIES.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P1077_1900_-NONE-_-NONE-/",
    'Actor: Harden Architectural Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1127",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23P1077_1900_-NONE-_-NONE- (harden_mexico_metal_door_screen_21k_2023). Signed 2023-08-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P1077_1900_-NONE-_-NONE-/.',
    'USASpending: harden_mexico_metal_door_screen_21k_2023 USD 0.021m. Supports harden_mexico_metal_door_screen_21k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 21453; date_signed 2023-08-23.',
)
row_doc(
    "misc_brazil_dx_hvac_units_lifecycle_replacement_36k_2012",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Brazil life cycle replacement of 4 DX HVAC units',
    "Brazil",
    '29 Sep 2012: Department of State awards contract SBR93012M0788 for life cycle replacement of 4 DX HVAC units (PoP Brazil); obligated USD 36,051.6. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "36051.6", "2012-09-29", "2012", "", "",
    'Life cycle replacement of 4 DX HVAC units, Brazil (USASpending description; site not named — lat/lon blank).',
    "usaspending_misc_brazil_dx_hvac_units_lifecycle_replacement_36k_2012",
    'LIFE CYCLE REPLACEMENT OF 4 DX HVAC UNITS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93012M0788_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1127",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR93012M0788_1900_-NONE-_-NONE- (misc_brazil_dx_hvac_units_lifecycle_replacement_36k_2012). Signed 2012-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR93012M0788_1900_-NONE-_-NONE-/.',
    'USASpending: misc_brazil_dx_hvac_units_lifecycle_replacement_36k_2012 USD 0.036m. Supports misc_brazil_dx_hvac_units_lifecycle_replacement_36k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 36051.6; date_signed 2012-09-29.',
)
row_doc(
    "bouwbedrijf_suriname_nassiefstraat_patio_floor_restoration_36k_2022",
    "infrastructure", "building_materials", "other",
    'Bouwbedrijf Insaso — Suriname Nassiefstraat back patio floor restoration',
    "Suriname",
    '26 Sep 2022: Department of State awards contract 19NS5022P0608 to Bouwbedrijf Insaso NV for Nassiefstraat back patio floor restoration project (PoP Suriname); obligated USD 35,811.62. CapEx face = award obligation. Nassiefstraat named; site coords not stated — lat/lon blank.',
    "35811.62", "2022-09-26", "2022", "", "",
    'Nassiefstraat back patio floor restoration project, Suriname (USASpending description; street named, site coords not stated — lat/lon blank).',
    "usaspending_bouwbedrijf_suriname_nassiefstraat_patio_floor_restoration_36k_2022",
    'FAC 7355 NASSIEFSTRAAT  BACK PATIO FLOOR RESTORATION PROJECT',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5022P0608_1900_-NONE-_-NONE-/",
    'Actor: Bouwbedrijf Insaso NV (Suriname) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1127",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19NS5022P0608_1900_-NONE-_-NONE- (bouwbedrijf_suriname_nassiefstraat_patio_floor_restoration_36k_2022). Signed 2022-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NS5022P0608_1900_-NONE-_-NONE-/.',
    'USASpending: bouwbedrijf_suriname_nassiefstraat_patio_floor_restoration_36k_2022 USD 0.036m. Supports bouwbedrijf_suriname_nassiefstraat_patio_floor_restoration_36k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35811.62; date_signed 2022-09-26.',
)
row_doc(
    "dese_panama_culebra_fence_repair_36k_2011",
    "infrastructure", "building_materials", "other",
    'Dese Construction — Panama Culebra fence repair',
    "Panama",
    '23 Jun 2011: Smithsonian awards contract F11PO3440000229257 to Dese Construction S.A. for repair Culebra\'s fence (PoP Panama); obligated USD 35,947. CapEx face = award obligation. Culebra named; site coords not stated — lat/lon blank.',
    "35947", "2011-06-23", "2011", "", "",
    'Repair Culebra\'s fence, Panama (USASpending description; Culebra named, site coords not stated — lat/lon blank).',
    "usaspending_dese_panama_culebra_fence_repair_36k_2011",
    'FOR REPAIR CULEBRA\'S FENCE',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F11PO3440000229257_3300_-NONE-_-NONE-/",
    'Actor: Dese Construction S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1127",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F11PO3440000229257_3300_-NONE-_-NONE- (dese_panama_culebra_fence_repair_36k_2011). Signed 2011-06-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F11PO3440000229257_3300_-NONE-_-NONE-/.',
    'USASpending: dese_panama_culebra_fence_repair_36k_2011 USD 0.036m. Supports dese_panama_culebra_fence_repair_36k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 35947; date_signed 2011-06-23.',
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
