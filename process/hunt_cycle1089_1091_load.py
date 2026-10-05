#!/usr/bin/env python3
"""Cycles 1089–1091: USASpending LatAm CapEx residual (~USD0.041–0.056m).

Seeds: 20262089–20262091. Thin top-up dry.
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


# === Cycle 1089 (seed 20262089) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "wje_mexico_seismic_model_ibc_49k_2016",
    "infrastructure", "engineering_epc", "us",
    'Wiss Janney Elstner — Mexico seismic model and IBC MCE spectral response',
    "Mexico",
    '26 Sep 2016: Department of State awards order SAQMMA16F5140 under IDV SAQMMA14D0021 to Wiss Janney Elstner Associates Inc to collect geologic source data, prepare seismic model, derive IBC MCE spectral response acceleration values, and prepare and submit report (PoP Mexico); obligated USD 48,930.90. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "48930.90", "2016-09-26", "2016", "", "",
    'Seismic model and IBC MCE spectral response report, Mexico (USASpending description; site not named — lat/lon blank).',
    "usaspending_wje_mexico_seismic_model_ibc_49k_2016",
    'IGF::OT::IGF THIS TASK ORDER PROVIDES FUNDING TO COLLECT GEOLOGIC SOURCE DATA, PREPARE SEISMIC MODEL, DERIVE IBC MCE SPECTRAL RESPONSE ACCELERATION VALUES, AND PREPARE&SUBMIT REPORT.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5140_1900_SAQMMA14D0021_1900/",
    'Actor: Wiss Janney Elstner Associates Inc (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1089",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F5140_1900_SAQMMA14D0021_1900 (WJE Mexico seismic model). Signed 2016-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F5140_1900_SAQMMA14D0021_1900/.',
    'USASpending: WJE Mexico seismic model USD 0.049m. Supports wje_mexico_seismic_model_ibc_49k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 48930.90; date_signed 2016-09-26.',
)
row_doc(
    "fabrication_designs_ecuador_metal_door_screen_45k_2022",
    "infrastructure", "building_materials", "us",
    'Fabrication Designs — Ecuador metal door screen for international embassies',
    "Ecuador",
    '14 Dec 2022: Department of State awards contract 19AQMM23P0100 to Fabrication Designs, Inc. for metal door screen etc. for international embassies (PoP Ecuador); obligated USD 44,594. CapEx face = award obligation. Exact embassy site unnamed — lat/lon blank.',
    "44594", "2022-12-14", "2022", "", "",
    'Metal door screen for international embassies, Ecuador (USASpending description; embassy not named — lat/lon blank).',
    "usaspending_fabrication_designs_ecuador_metal_door_screen_45k_2022",
    'METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0100_1900_-NONE-_-NONE-/",
    'Actor: Fabrication Designs, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1089",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23P0100_1900_-NONE-_-NONE- (Fabrication Designs Ecuador metal door). Signed 2022-12-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0100_1900_-NONE-_-NONE-/.',
    'USASpending: Fabrication Designs Ecuador metal door USD 0.045m. Supports fabrication_designs_ecuador_metal_door_screen_45k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 44594; date_signed 2022-12-14.',
)
row_doc(
    "misc_peru_soccer_field_illumination_56k_2015",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Peru soccer field illumination system replacement',
    "Peru",
    '28 Aug 2015: Department of State awards contract SPE50015M2191 to replace soccer field illumination system (PoP Peru); obligated USD 55,500. CapEx face = award obligation. Exact field unnamed — lat/lon blank.',
    "55500", "2015-08-28", "2015", "", "",
    'Replace soccer field illumination system, Peru (USASpending description; field not named — lat/lon blank).',
    "usaspending_misc_peru_soccer_field_illumination_56k_2015",
    '8/20 FAC - REPLACE SOCCER FIELD ILLUMINATION SYSTEM',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M2191_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.',
    "hunt_cycle1089",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50015M2191_1900_-NONE-_-NONE- (Peru soccer field illumination). Signed 2015-08-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M2191_1900_-NONE-_-NONE-/.',
    'USASpending: Peru soccer field illumination USD 0.056m. Supports misc_peru_soccer_field_illumination_56k_2015.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55500; date_signed 2015-08-28.',
)
row_doc(
    "misc_peru_south_terrace_roof_55k_2018",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Peru Lima south terrace roof next to MPR',
    "Peru",
    '25 Sep 2018: Department of State awards contract 19PE5018C0032 for south terrace roof next to MPR (PoP Peru); obligated USD 55,231.93. CapEx face = award obligation. Exact terrace unnamed — lat/lon blank.',
    "55231.93", "2018-09-25", "2018", "", "",
    'South terrace roof next to MPR, Peru (USASpending description; MPR named, site coords not stated — lat/lon blank).',
    "usaspending_misc_peru_south_terrace_roof_55k_2018",
    'EOY18 - SOUTH TERRACE ROOF - (NEXT TO MPR)',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5018C0032_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1089",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5018C0032_1900_-NONE-_-NONE- (Peru south terrace roof). Signed 2018-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5018C0032_1900_-NONE-_-NONE-/.',
    'USASpending: Peru south terrace roof USD 0.055m. Supports misc_peru_south_terrace_roof_55k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55231.93; date_signed 2018-09-25.',
)
row_doc(
    "misc_mexico_chancery_roof_waterproofing_55k_2011",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Mexico chancery roof waterproofing',
    "Mexico",
    '16 Feb 2011: Department of State awards contract SMX53011M0473 for OBO waterproofing of chancery roof (PoP Mexico); obligated USD 55,069.07. CapEx face = award obligation. Exact chancery unnamed — lat/lon blank.',
    "55069.07", "2011-02-16", "2011", "", "",
    'Waterproofing of chancery roof, Mexico (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_misc_mexico_chancery_roof_waterproofing_55k_2011",
    "MEX OBO WATER PROOFING OF CHANCERY'S ROOF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M0473_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1089",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53011M0473_1900_-NONE-_-NONE- (Mexico chancery roof waterproofing). Signed 2011-02-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M0473_1900_-NONE-_-NONE-/.',
    'USASpending: Mexico chancery roof waterproofing USD 0.055m. Supports misc_mexico_chancery_roof_waterproofing_55k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55069.07; date_signed 2011-02-16.',
)

# === Cycle 1090 (seed 20262090) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_argentina_metal_door_screen_44k_2025",
    "infrastructure", "building_materials", "us",
    'Norshield Security Products — Argentina metal door screen for international embassies',
    "Argentina",
    '10 Mar 2025: Department of State awards contract 19AQMM25P0526 to Norshield Security Products, LLC for metal door screen etc. for international embassies (PoP Argentina); obligated USD 44,435. CapEx face = award obligation. Exact embassy site unnamed — lat/lon blank.',
    "44435", "2025-03-10", "2025", "", "",
    'Metal door screen for international embassies, Argentina (USASpending description; embassy not named — lat/lon blank).',
    "usaspending_norshield_argentina_metal_door_screen_44k_2025",
    'METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0526_1900_-NONE-_-NONE-/",
    'Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1090",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0526_1900_-NONE-_-NONE- (Norshield Argentina metal door). Signed 2025-03-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0526_1900_-NONE-_-NONE-/.',
    'USASpending: Norshield Argentina metal door USD 0.044m. Supports norshield_argentina_metal_door_screen_44k_2025.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 44435; date_signed 2025-03-10.',
)
row_doc(
    "ace_roof_coatings_honduras_embassy_roof_44k_2026",
    "infrastructure", "building_materials", "us",
    'ACE Roof Coatings — Honduras materials to repair old embassy building roof FY26',
    "Honduras",
    '21 Jan 2026: Department of State awards contract 19H08026P0101 to ACE Roof Coatings, Inc for materials to repair old embassy building roof FY26 (PoP Honduras); obligated USD 43,648.33. CapEx face = award obligation. Exact embassy roof unnamed — lat/lon blank.',
    "43648.33", "2026-01-21", "2026", "", "",
    'Materials to repair old embassy building roof, Honduras (USASpending description; embassy named, site coords not stated — lat/lon blank).',
    "usaspending_ace_roof_coatings_honduras_embassy_roof_44k_2026",
    'FAC - MATERIALS TO REPAIR OLD EMBASSY BUILDING ROOF_FY26',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08026P0101_1900_-NONE-_-NONE-/",
    'Actor: ACE Roof Coatings, Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1090",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19H08026P0101_1900_-NONE-_-NONE- (ACE Roof Coatings Honduras embassy roof). Signed 2026-01-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08026P0101_1900_-NONE-_-NONE-/.',
    'USASpending: ACE Roof Coatings Honduras embassy roof USD 0.044m. Supports ace_roof_coatings_honduras_embassy_roof_44k_2026.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 43648.33; date_signed 2026-01-21.',
)
row_doc(
    "misc_honduras_five_generators_dli_55k_2011",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Honduras purchase of five generators with DLI funds',
    "Honduras",
    '30 Aug 2011: USAID awards contract AID522O1100040 for purchase of 5 generators with DLI funds (PoP Honduras); obligated USD 55,058.75. CapEx face = award obligation. Exact generator sites unnamed — lat/lon blank.',
    "55058.75", "2011-08-30", "2011", "", "",
    'Purchase of 5 generators with DLI funds, Honduras (USASpending description; sites not named — lat/lon blank).',
    "usaspending_misc_honduras_five_generators_dli_55k_2011",
    'PURCHASE OF 5 GENERATORS WITH DLI FUNDS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1100040_7200_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.',
    "hunt_cycle1090",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID522O1100040_7200_-NONE-_-NONE- (Honduras five generators DLI). Signed 2011-08-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID522O1100040_7200_-NONE-_-NONE-/.',
    'USASpending: Honduras five generators DLI USD 0.055m. Supports misc_honduras_five_generators_dli_55k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55058.75; date_signed 2011-08-30.',
)
row_doc(
    "misc_argentina_cervino_remodel_55k_2018",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Argentina Cervino 4616/24 6 A CABA remodel',
    "Argentina",
    '29 Sep 2018: Department of State awards contract 19AR2018C0009 to remodel Cervino 4616/24 6 A, C.A.B.A. (PoP Argentina); obligated USD 55,000.01. CapEx face = award obligation. Exact unit unnamed beyond address string — lat/lon blank.',
    "55000.01", "2018-09-29", "2018", "", "",
    'Remodel Cervino 4616/24 6 A, CABA, Argentina (USASpending description; street named, coords not stated — lat/lon blank).',
    "usaspending_misc_argentina_cervino_remodel_55k_2018",
    'REMODEL CERVINO 4616/24 6 A, C.A.B.A.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018C0009_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1090",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2018C0009_1900_-NONE-_-NONE- (Argentina Cervino remodel). Signed 2018-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018C0009_1900_-NONE-_-NONE-/.',
    'USASpending: Argentina Cervino remodel USD 0.055m. Supports misc_argentina_cervino_remodel_55k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55000.01; date_signed 2018-09-29.',
)
row_doc(
    "consorcio_pijaos_chain_link_fence_55k_2018",
    "infrastructure", "building_materials", "other",
    'Consorcio 2A Pijaos — Colombia chain link fence shoot house Pijaos',
    "Colombia",
    '1 Feb 2018: Department of State awards contract 19C01518C0003 to Consorcio 2A Pijaos for chain link fence shoot house Pijaos (PoP Colombia); obligated USD 55,365.61. CapEx face = award obligation. Exact shoot-house site unnamed — lat/lon blank.',
    "55365.61", "2018-02-01", "2018", "", "",
    'Chain link fence shoot house Pijaos, Colombia (USASpending description; Pijaos named, site coords not stated — lat/lon blank).',
    "usaspending_consorcio_pijaos_chain_link_fence_55k_2018",
    'CHAIN LINK FENCE SHOOT HOUSE PIJAOS',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01518C0003_1900_-NONE-_-NONE-/",
    'Actor: Consorcio 2A Pijaos (Colombia) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1090",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01518C0003_1900_-NONE-_-NONE- (Consorcio Pijaos chain link fence). Signed 2018-02-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01518C0003_1900_-NONE-_-NONE-/.',
    'USASpending: Consorcio Pijaos chain link fence USD 0.055m. Supports consorcio_pijaos_chain_link_fence_55k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55365.61; date_signed 2018-02-01.',
)

# === Cycle 1091 (seed 20262091) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "pono_aina_bahamas_cmr_window_repair_42k_2022",
    "infrastructure", "building_materials", "us",
    'Pono Aina Management — Bahamas CMR window repair',
    "Bahamas",
    '20 Jul 2022: Department of State awards contract 19BF5022P0552 to Pono Aina Management LLC for CMR window repair (PoP Bahamas); obligated USD 41,872.25. CapEx face = award obligation. Exact CMR site unnamed — lat/lon blank.',
    "41872.25", "2022-07-20", "2022", "", "",
    'CMR window repair, Bahamas (USASpending description; CMR named, site coords not stated — lat/lon blank).',
    "usaspending_pono_aina_bahamas_cmr_window_repair_42k_2022",
    'CMR WINDOW REPAIR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5022P0552_1900_-NONE-_-NONE-/",
    'Actor: Pono Aina Management LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1091",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BF5022P0552_1900_-NONE-_-NONE- (Pono Aina Bahamas CMR window). Signed 2022-07-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5022P0552_1900_-NONE-_-NONE-/.',
    'USASpending: Pono Aina Bahamas CMR window USD 0.042m. Supports pono_aina_bahamas_cmr_window_repair_42k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 41872.25; date_signed 2022-07-20.',
)
row_doc(
    "american_roofing_argentina_roof_h_41k_2011",
    "infrastructure", "building_materials", "us",
    'American Roofing & Metal — Argentina Buenos Aires Roof H project',
    "Argentina",
    '7 Sep 2011: Department of State awards order SAQMMA11F3252 under IDV SALMEC07D0029 to American Roofing & Metal Co Inc for Roof H project in Buenos Aires, Argentina; obligated USD 40,955.25. CapEx face = award obligation. Exact Roof H site unnamed — lat/lon blank.',
    "40955.25", "2011-09-07", "2011", "", "",
    'Roof H project in Buenos Aires, Argentina (USASpending description; Buenos Aires named, site coords not stated — lat/lon blank).',
    "usaspending_american_roofing_argentina_roof_h_41k_2011",
    'ROOF H PROJECT IN BUENOS AIRES, ARGENTINA.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3252_1900_SALMEC07D0029_1900/",
    'Actor: American Roofing & Metal Co Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1091",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F3252_1900_SALMEC07D0029_1900 (American Roofing Buenos Aires Roof H). Signed 2011-09-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3252_1900_SALMEC07D0029_1900/.',
    'USASpending: American Roofing Buenos Aires Roof H USD 0.041m. Supports american_roofing_argentina_roof_h_41k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 40955.25; date_signed 2011-09-07.',
)
row_doc(
    "gps_colombia_generators_ac_vita_55k_2020",
    "energy", "power_plants_grid", "other",
    'Government Project Services — Colombia generators and air conditioners VITA 2020',
    "Colombia",
    '5 Mar 2020: Department of Defense awards contract W913FT20P0018 to Government Project Services SAS for generators and air conditioners VITA 2020 (PoP Colombia); obligated USD 55,204.83. CapEx face = award obligation. Exact VITA site unnamed — lat/lon blank.',
    "55204.83", "2020-03-05", "2020", "", "",
    'Generators and air conditioners VITA 2020, Colombia (USASpending description; VITA named, site coords not stated — lat/lon blank).',
    "usaspending_gps_colombia_generators_ac_vita_55k_2020",
    'GENERATORS&AIR CONDITIONERS VITA 2020',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT20P0018_9700_-NONE-_-NONE-/",
    'Actor: Government Project Services SAS (Colombia) — other. Official USASpending Award API. Shuffle power_plants_grid.',
    "hunt_cycle1091",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT20P0018_9700_-NONE-_-NONE- (GPS Colombia generators/AC VITA). Signed 2020-03-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT20P0018_9700_-NONE-_-NONE-/.',
    'USASpending: GPS Colombia generators/AC VITA USD 0.055m. Supports gps_colombia_generators_ac_vita_55k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55204.83; date_signed 2020-03-05.',
)
row_doc(
    "akj_mexico_seneca_fire_alarm_55k_2024",
    "infrastructure", "building_materials", "other",
    'Servicios AKJ — Mexico MCI Seneca fire alarm installation FY24',
    "Mexico",
    '9 Feb 2024: Department of State awards contract 19MX5324P0451 to Servicios AKJ, S.A de C.V for MCI Seneca fire alarm installation FY24 (PoP Mexico); obligated USD 55,195.03. CapEx face = award obligation. Exact Seneca site unnamed — lat/lon blank.',
    "55195.03", "2024-02-09", "2024", "", "",
    'MCI Seneca fire alarm installation FY24, Mexico (USASpending description; Seneca named, site coords not stated — lat/lon blank).',
    "usaspending_akj_mexico_seneca_fire_alarm_55k_2024",
    'MEX-FAC-7902-MCI-SENECA FIRE ALARM INSTALLATION-FY24',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5324P0451_1900_-NONE-_-NONE-/",
    'Actor: Servicios AKJ, S.A de C.V (Mexico) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1091",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5324P0451_1900_-NONE-_-NONE- (AKJ Mexico Seneca fire alarm). Signed 2024-02-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5324P0451_1900_-NONE-_-NONE-/.',
    'USASpending: AKJ Mexico Seneca fire alarm USD 0.055m. Supports akj_mexico_seneca_fire_alarm_55k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 55195.03; date_signed 2024-02-09.',
)
row_doc(
    "misc_brazil_man_trap_construction_55k_2018",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil man trap construction project XJ0H0002',
    "Brazil",
    '10 Sep 2018: Department of State awards contract 19BR8118P0368 for man trap construction project XJ0H0002 (PoP Brazil); obligated USD 54,763.57. CapEx face = award obligation. Exact man-trap site unnamed — lat/lon blank.',
    "54763.57", "2018-09-10", "2018", "", "",
    'Man trap construction project XJ0H0002, Brazil (USASpending description; project code named, site coords not stated — lat/lon blank).',
    "usaspending_misc_brazil_man_trap_construction_55k_2018",
    'MAN TRAP CONSTRUCTION - PROJECT XJ0H0002',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8118P0368_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1091",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR8118P0368_1900_-NONE-_-NONE- (Brazil man trap construction). Signed 2018-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8118P0368_1900_-NONE-_-NONE-/.',
    'USASpending: Brazil man trap construction USD 0.055m. Supports misc_brazil_man_trap_construction_55k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 54763.57; date_signed 2018-09-10.',
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
