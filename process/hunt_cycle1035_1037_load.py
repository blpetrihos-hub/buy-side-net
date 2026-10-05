#!/usr/bin/env python3
"""Cycles 1035–1037: USASpending LatAm CapEx residual (~USD0.06–0.09m).

Seeds: 20262035–20262037. Thin top-up dry.
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

# === Cycle 1035 ===
row_doc(
    "pinnacle_guyana_tower_lights_94k_2021",
    "energy", "power_plants_grid", "other",
    "Pinnacle Business Services — Guyana tower lights with generator",
    "Guyana",
    "9 Jun 2021: DoD awards contract W912CL21P0015 to Pinnacle Business Services for tower lights with generator (SIF funding) (PoP Guyana); obligated USD 93,912. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "93912", "2021-06-09", "2021", "", "",
    "Tower lights with generator, Guyana (USASpending PoP Guyana; site not named — lat/lon blank).",
    "usaspending_pinnacle_guyana_tower_lights_94k_2021",
    "TOWER LIGHTS W/GENERATOR (SIF FUNDING)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL21P0015_9700_-NONE-_-NONE-/",
    "Actor: Pinnacle Business Services Inc. (Guyana) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1035",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL21P0015_9700_-NONE-_-NONE- (Pinnacle Guyana tower lights). Signed 2021-06-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL21P0015_9700_-NONE-_-NONE-/.",
    "USASpending: Pinnacle Guyana tower lights USD 0.094m. Supports pinnacle_guyana_tower_lights_94k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 93912; date_signed 2021-06-09.",
)

row_doc(
    "misc_colombia_warehouse_structure_87k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia CGENA warehouse metallic structure",
    "Colombia",
    "12 Aug 2017: Department of State awards contract SCO20017M0651 for metallic structure to warehouse — CGENA (PoP Colombia); obligated USD 87,453.57. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "87453.57", "2017-08-12", "2017", "", "",
    "Metallic structure to warehouse CGENA, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_misc_colombia_warehouse_structure_87k_2017",
    "IGF::OT::IGF PR6241591: METALLIC STRUCTURE TO WAREHOUSE- CGENA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20017M0651_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1035",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20017M0651_1900_-NONE-_-NONE- (Colombia warehouse structure). Signed 2017-08-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20017M0651_1900_-NONE-_-NONE-/.",
    "USASpending: Colombia warehouse structure USD 0.087m. Supports misc_colombia_warehouse_structure_87k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 87453.57; date_signed 2017-08-12.",
)

row_doc(
    "wkl_panama_cdc_office_87k_2024",
    "infrastructure", "building_materials", "other",
    "W.K.L. Arquitectos — Panama CDC new office renovation",
    "Panama",
    "16 Apr 2024: Department of State awards contract 19PM0724P0446 to W.K.L. Arquitectos for CDC new office renovation (PoP Panama); obligated USD 87,470. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "87470", "2024-04-16", "2024", "", "",
    "CDC new office renovation, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_wkl_panama_cdc_office_87k_2024",
    "CDC  - NEW OFFICE RENOVATION  2024FAC001 (24Q0025)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0724P0446_1900_-NONE-_-NONE-/",
    "Actor: W.K.L. Arquitectos S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1035",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0724P0446_1900_-NONE-_-NONE- (WKL CDC office). Signed 2024-04-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0724P0446_1900_-NONE-_-NONE-/.",
    "USASpending: WKL CDC office USD 0.087m. Supports wkl_panama_cdc_office_87k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 87470; date_signed 2024-04-16.",
)

row_doc(
    "misc_hermosillo_generator_88k_2020",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico Hermosillo CGR power generator",
    "Mexico",
    "12 Mar 2020: Department of State awards contract 19MX5720P0051 for supply of the CGR power generator Caterpillar (PoP Mexico); obligated USD 87,552. CapEx face = award obligation. Recipient redacted.",
    "87552", "2020-03-12", "2020", "29.073", "-110.955",
    "CGR power generator, Hermosillo, Mexico (USASpending description HMO; Hermosillo named).",
    "usaspending_misc_hermosillo_generator_88k_2020",
    "HMO/FAC/OBO/SUPPLY OF THE CGR POWER GENERATOR CATERPILL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5720P0051_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1035",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5720P0051_1900_-NONE-_-NONE- (Hermosillo generator). Signed 2020-03-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5720P0051_1900_-NONE-_-NONE-/.",
    "USASpending: Hermosillo generator USD 0.088m. Supports misc_hermosillo_generator_88k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 87552; date_signed 2020-03-12.",
)

row_doc(
    "belle_grove_naos_wet_lab_86k_2016",
    "infrastructure", "building_materials", "us",
    "Belle Grove Management — Panama STRI Naos wet lab construction",
    "Panama",
    "23 Aug 2016: Smithsonian awards contract F16CC10530 to Belle Grove Management to construct a wet lab at Bldg 356 Naos Marine Laboratory (STRI); obligated USD 86,276.68. CapEx face = award obligation.",
    "86276.68", "2016-08-23", "2016", "8.913", "-79.533",
    "Wet lab at Bldg 356, Naos Marine Laboratory, Panama (USASpending description; Naos named).",
    "usaspending_belle_grove_naos_wet_lab_86k_2016",
    "TO CONSTRUCT A WET LAB AT BLDG 356 NAOS MARINE LABORATORY (STRI)      IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F16CC10530_3300_-NONE-_-NONE-/",
    "Actor: Belle Grove Management (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1035",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F16CC10530_3300_-NONE-_-NONE- (Belle Grove Naos wet lab). Signed 2016-08-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F16CC10530_3300_-NONE-_-NONE-/.",
    "USASpending: Belle Grove Naos wet lab USD 0.086m. Supports belle_grove_naos_wet_lab_86k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 86276.68; date_signed 2016-08-23.",
)

# === Cycle 1036 ===
row_doc(
    "atria_brazil_cmr_ae_86k_2019",
    "infrastructure", "engineering_epc", "other",
    "Atria Arquitetos — Brazil CMR representation expansion A&E",
    "Brazil",
    "13 Mar 2019: Department of State awards contract 19BR2519P0394 to Atria Arquitetos for A&E design services for CMR representation expansion (PoP Brazil); obligated USD 86,426.11. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "86426.11", "2019-03-13", "2019", "", "",
    "CMR representation expansion A&E design, Brazil (USASpending PoP Brazil; site not named — lat/lon blank).",
    "usaspending_atria_brazil_cmr_ae_86k_2019",
    "BSB-FAC A&E DESIGN SERVICES FOR CMR REPRESENTATION EXPA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0394_1900_-NONE-_-NONE-/",
    "Actor: Atria Arquitetos Sociedade Simples (Brazil) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1036",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2519P0394_1900_-NONE-_-NONE- (Atria Brazil CMR A&E). Signed 2019-03-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0394_1900_-NONE-_-NONE-/.",
    "USASpending: Atria Brazil CMR A&E USD 0.086m. Supports atria_brazil_cmr_ae_86k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 86426.11; date_signed 2019-03-13.",
)

row_doc(
    "mfg_gaitanias_shelter_86k_2012",
    "infrastructure", "building_materials", "other",
    "MFG Ingeniería — Colombia Gaitanias shelter construction",
    "Colombia",
    "10 Sep 2012: DoD awards contract W913FT12P0339 to MFG Ingeniería for Gaitanias shelter construction (PoP Colombia); obligated USD 86,166.59. CapEx face = award obligation.",
    "86166.59", "2012-09-10", "2012", "", "",
    "Gaitanias shelter construction, Colombia (USASpending description; Gaitanias named but coordinates not sourced — lat/lon blank).",
    "usaspending_mfg_gaitanias_shelter_86k_2012",
    "GAITANIAS SHELTER CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0339_9700_-NONE-_-NONE-/",
    "Actor: MFG Ingeniería S.A.S. (Colombia) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1036",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12P0339_9700_-NONE-_-NONE- (MFG Gaitanias shelter). Signed 2012-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0339_9700_-NONE-_-NONE-/.",
    "USASpending: MFG Gaitanias shelter USD 0.086m. Supports mfg_gaitanias_shelter_86k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 86166.59; date_signed 2012-09-10.",
)

row_doc(
    "atlas_haiti_attalaye_86k_2013",
    "infrastructure", "building_materials", "other",
    "Atlas Construction — Haiti St Michel de l'Attalaye health center renovation",
    "Haiti",
    "2 Aug 2013: USAID awards BPA call AID521BC1300002 to Atlas Construction to reinforce external doors/windows of four dispensaries and renovate the health center of St Michel de l'Attalaye for ARV services; obligated USD 86,127. CapEx face = award obligation.",
    "86127", "2013-08-02", "2013", "19.373", "-72.333",
    "Health center renovation and dispensary reinforcement, St Michel de l'Attalaye, Haiti (USASpending description; St Michel de l'Attalaye named).",
    "usaspending_atlas_haiti_attalaye_86k_2013",
    "IGF::OT::IGF - THE PUPOSE OF THIS BPA CALL IS TO REINFORCE ALL EXTERNAL DOORS AND WINDOWS OF FOUR DISPENSARIES AND RENOVATE THE HEALTH CENTER OF ST MICHEL DE L'ATTALAYE TO ACCOMMODATE ARV SERVICES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521BC1300002_7200_AID521E1200002_7200/",
    "Actor: Atlas Construction (Haiti) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1036",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AID521BC1300002_7200_AID521E1200002_7200 (Atlas Attalaye). Signed 2013-08-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521BC1300002_7200_AID521E1200002_7200/.",
    "USASpending: Atlas Attalaye USD 0.086m. Supports atlas_haiti_attalaye_86k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 86127; date_signed 2013-08-02.",
)

row_doc(
    "dts_guyana_generators_88k_2023",
    "energy", "power_plants_grid", "other",
    "DTS Trading and Shipping — Guyana Tradewinds 23 generators",
    "Guyana",
    "12 Jun 2023: DoD awards contract W569QE23P0041 to DTS Trading and Shipping for generators in support of Tradewinds 23 (PoP Guyana); obligated USD 87,500. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "87500", "2023-06-12", "2023", "", "",
    "Generators for Tradewinds 23, Guyana (USASpending PoP Guyana; site not named — lat/lon blank).",
    "usaspending_dts_guyana_generators_88k_2023",
    "GENERATORS IN SUPPORT OF TRADEWINDS 23",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W569QE23P0041_9700_-NONE-_-NONE-/",
    "Actor: DTS Trading and Shipping (Guyana) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1036",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W569QE23P0041_9700_-NONE-_-NONE- (DTS Guyana generators). Signed 2023-06-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W569QE23P0041_9700_-NONE-_-NONE-/.",
    "USASpending: DTS Guyana generators USD 0.088m. Supports dts_guyana_generators_88k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 87500; date_signed 2023-06-12.",
)

row_doc(
    "air_charter_chile_generators_69k_2010",
    "energy", "power_plants_grid", "us",
    "Air Charter Service — Chile 20 portable generators on trailers",
    "Chile",
    "29 Mar 2010: USAID awards contract AIDTRNC001000063 to Air Charter Service for 20 portable generators on trailers (PoP Chile); obligated USD 69,150. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "69150", "2010-03-29", "2010", "", "",
    "Twenty portable generators on trailers, Chile (USASpending PoP Chile; site not named — lat/lon blank).",
    "usaspending_air_charter_chile_generators_69k_2010",
    "20 PORTABLE GENERATORS, ON TRAILERS     TAS::72 1000::TAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AIDTRNC001000063_7200_-NONE-_-NONE-/",
    "Actor: Air Charter Service Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1036",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AIDTRNC001000063_7200_-NONE-_-NONE- (Air Charter Chile generators). Signed 2010-03-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AIDTRNC001000063_7200_-NONE-_-NONE-/.",
    "USASpending: Air Charter Chile generators USD 0.069m. Supports air_charter_chile_generators_69k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 69150; date_signed 2010-03-29.",
)

# === Cycle 1037 ===
row_doc(
    "misc_bolivia_generator_86k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Bolivia RDTF gas generator",
    "Bolivia",
    "18 Jun 2013: Department of State awards contract SBL40013M0372 for INL-RDTF gas generator for RDTF (PoP Bolivia); obligated USD 85,666.55. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "85666.55", "2013-06-18", "2013", "", "",
    "Gas generator for RDTF, Bolivia (USASpending PoP Bolivia; site not named — lat/lon blank).",
    "usaspending_misc_bolivia_generator_86k_2013",
    "INL-RDTF/GAS GENERATOR FOR RDTF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40013M0372_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1037",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBL40013M0372_1900_-NONE-_-NONE- (Bolivia RDTF generator). Signed 2013-06-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40013M0372_1900_-NONE-_-NONE-/.",
    "USASpending: Bolivia RDTF generator USD 0.086m. Supports misc_bolivia_generator_86k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 85666.55; date_signed 2013-06-18.",
)

row_doc(
    "misc_peru_msgq_kitchen_78k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru MSGQ kitchen renovation",
    "Peru",
    "24 Sep 2013: DoD awards contract SPE50013C0032 to renovate the MSGQ kitchen (PoP Peru); obligated USD 78,378.43. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "78378.43", "2013-09-24", "2013", "", "",
    "MSGQ kitchen renovation, Peru (USASpending PoP Peru; site not named — lat/lon blank).",
    "usaspending_misc_peru_msgq_kitchen_78k_2013",
    "CONTRACT TO RENOVATE THE MSGQ KITCHEN IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50013C0032_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1037",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50013C0032_1900_-NONE-_-NONE- (Peru MSGQ kitchen). Signed 2013-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50013C0032_1900_-NONE-_-NONE-/.",
    "USASpending: Peru MSGQ kitchen USD 0.078m. Supports misc_peru_msgq_kitchen_78k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 78378.43; date_signed 2013-09-24.",
)

row_doc(
    "misc_mexico_embassy_renovation_77k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico U.S. Embassy renovation improvements",
    "Mexico",
    "26 Sep 2011: Department of State awards contract SMX53011C0047 for renovation services for improvements at the U.S. Embassy (PoP Mexico); obligated USD 77,335.59. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "77335.59", "2011-09-26", "2011", "", "",
    "U.S. Embassy renovation improvements, Mexico (USASpending PoP Mexico; site not named — lat/lon blank).",
    "usaspending_misc_mexico_embassy_renovation_77k_2011",
    "RENOVATION SERVICES FOR IMPROVEMENTS AT THE U.S. EMBASS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011C0047_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1037",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53011C0047_1900_-NONE-_-NONE- (Mexico Embassy renovation). Signed 2011-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011C0047_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico Embassy renovation USD 0.077m. Supports misc_mexico_embassy_renovation_77k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 77335.59; date_signed 2011-09-26.",
)

row_doc(
    "urbanus_panama_nec_fence_74k_2019",
    "infrastructure", "building_materials", "other",
    "Urbanus Group — Panama NEC perimeter fence repairs south and east",
    "Panama",
    "9 Sep 2019: Department of State awards contract 19PM0719P0969 to Urbanus Group for NEC perimeter fence repairs south and east (PoP Panama); obligated USD 73,620.20. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "73620.2", "2019-09-09", "2019", "", "",
    "NEC perimeter fence repairs south and east, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_urbanus_panama_nec_fence_74k_2019",
    "19PM0719P0969 NEC PERIMETER FENCE REPAIRS SOUTH&EA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0969_1900_-NONE-_-NONE-/",
    "Actor: Urbanus Group Inc. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1037",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0719P0969_1900_-NONE-_-NONE- (Urbanus NEC fence). Signed 2019-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0719P0969_1900_-NONE-_-NONE-/.",
    "USASpending: Urbanus NEC fence USD 0.074m. Supports urbanus_panama_nec_fence_74k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 73620.2; date_signed 2019-09-09.",
)

row_doc(
    "york_barbados_chiller_67k_2016",
    "energy", "power_plants_grid", "us",
    "York International — Barbados BME chiller contract",
    "Barbados",
    "26 Jul 2016: Department of State awards contract SBB21016M0618 to York International for BME chiller contract (PoP Barbados); obligated USD 66,772. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "66772", "2016-07-26", "2016", "", "",
    "BME chiller, Barbados (USASpending PoP Barbados; site not named — lat/lon blank).",
    "usaspending_york_barbados_chiller_67k_2016",
    "BME CHILLER CONTRACT IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21016M0618_1900_-NONE-_-NONE-/",
    "Actor: York International Corporation (York PA, U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1037",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21016M0618_1900_-NONE-_-NONE- (York Barbados chiller). Signed 2016-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21016M0618_1900_-NONE-_-NONE-/.",
    "USASpending: York Barbados chiller USD 0.067m. Supports york_barbados_chiller_67k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 66772; date_signed 2016-07-26.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    supports = entry.get("supports") or []
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        prev = existing.get("supports") or []
        for s in supports:
            if s not in prev:
                prev.append(s)
        existing.update(entry)
        existing["supports"] = prev
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added = []
    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        upsert_bib(bib, bib_by, bib_entry)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})
    BIB.write_text(yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8")
    print(f"cycles1035-1037 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
