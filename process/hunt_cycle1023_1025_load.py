#!/usr/bin/env python3
"""Cycles 1023–1025: USASpending LatAm CapEx residual (~USD0.08–0.11m).

Seeds: 20262023–20262025. Thin top-up dry.
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

# === Cycle 1023 ===
row_doc(
    "eterna_river_gates_97k_2011",
    "infrastructure", "bridges_roads", "other",
    "Eterna — Soto Cano river security gates construction",
    "Honduras",
    "27 Sep 2011: DoD awards delivery order 0008 under W9127811D0046 to Empresa de Construcción y Transporte Eterna for construction of river security gates, Soto Cano Air Base, Honduras; obligated USD 96,500.25. CapEx face = award obligation.",
    "96500.25", "2011-09-27", "2011", "14.382", "-87.621",
    "River security gates, Soto Cano Air Base, Honduras (USASpending description; Soto Cano named).",
    "usaspending_eterna_river_gates_97k_2011",
    "TAS::21 2020::TAS CONSTRUCTION OF RIVER SECURITY GATES, SOTO CANO AIR BASE, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127811D0046_9700/",
    "Actor: Empresa de Construcción y Transporte Eterna S.A. de C.V. (San Pedro Sula) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1023",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0008_9700_W9127811D0046_9700 (Eterna river gates). Signed 2011-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127811D0046_9700/.",
    "USASpending: Eterna river gates USD 0.097m. Supports eterna_river_gates_97k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 96500.25; date_signed 2011-09-27.",
)

row_doc(
    "misc_brazil_rcip_95k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil RCIP phase 2 civil construction",
    "Brazil",
    "11 Apr 2019: Department of State awards contract 19BR8119P0164 for civil construction RCIP phase 2 project XJ0H0003 (PoP Brazil); obligated USD 94,635.53. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "94635.53", "2019-04-11", "2019", "", "",
    "RCIP phase 2 civil construction, Brazil (USASpending PoP Brazil; site not named — lat/lon blank).",
    "usaspending_misc_brazil_rcip_95k_2019",
    "CIVIL CONSTRUCTION RCIP PHASE 2 - PROJECT XJ0H0003",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8119P0164_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1023",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR8119P0164_1900_-NONE-_-NONE- (Brazil RCIP). Signed 2019-04-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8119P0164_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil RCIP USD 0.095m. Supports misc_brazil_rcip_95k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 94635.53; date_signed 2019-04-11.",
)

row_doc(
    "inecon_bathrooms_93k_2013",
    "infrastructure", "building_materials", "other",
    "Inecon — Colombia bathrooms construction",
    "Colombia",
    "25 Jul 2013: DoD awards contract W913FT13P0136 to Inecon for bathrooms construction (PoP Colombia); obligated USD 93,449.12. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "93449.12", "2013-07-25", "2013", "", "",
    "Bathrooms construction, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_inecon_bathrooms_93k_2013",
    "BATHROOMS CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13P0136_9700_-NONE-_-NONE-/",
    "Actor: Inecon S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1023",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT13P0136_9700_-NONE-_-NONE- (Inecon bathrooms). Signed 2013-07-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT13P0136_9700_-NONE-_-NONE-/.",
    "USASpending: Inecon bathrooms USD 0.093m. Supports inecon_bathrooms_93k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 93449.12; date_signed 2013-07-25.",
)

row_doc(
    "mfg_shelter_canopy_93k_2012",
    "infrastructure", "building_materials", "other",
    "MFG Ingeniería — Colombia shelter and canopy construction",
    "Colombia",
    "7 Sep 2012: DoD awards contract W913FT12C0025 to MFG Ingeniería for shelter and canopy construction (PoP Colombia); obligated USD 92,904.13. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "92904.13", "2012-09-07", "2012", "", "",
    "Shelter and canopy construction, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_mfg_shelter_canopy_93k_2012",
    "SHELTER AND CANOPY CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0025_9700_-NONE-_-NONE-/",
    "Actor: MFG Ingeniería S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1023",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12C0025_9700_-NONE-_-NONE- (MFG shelter canopy). Signed 2012-09-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0025_9700_-NONE-_-NONE-/.",
    "USASpending: MFG shelter canopy USD 0.093m. Supports mfg_shelter_canopy_93k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 92904.13; date_signed 2012-09-07.",
)

row_doc(
    "fluid_bahamas_ups_97k_2019",
    "energy", "power_plants_grid", "us",
    "Fluid Solutions — Bahamas chancery building UPS",
    "Bahamas",
    "13 Jun 2019: Department of State awards contract 19BF5019C0002 to Fluid Solutions for chancery building UPS (BME) (PoP Bahamas); obligated USD 97,326. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "97326", "2019-06-13", "2019", "", "",
    "Chancery building UPS, Bahamas (USASpending PoP Bahamas; site not named — lat/lon blank).",
    "usaspending_fluid_bahamas_ups_97k_2019",
    "CHANCERY - BUILDING UPS (BME)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5019C0002_1900_-NONE-_-NONE-/",
    "Actor: Fluid Solutions LLC (Birmingham AL, U.S.-incorporated) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1023",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BF5019C0002_1900_-NONE-_-NONE- (Fluid Bahamas UPS). Signed 2019-06-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5019C0002_1900_-NONE-_-NONE-/.",
    "USASpending: Fluid Bahamas UPS USD 0.097m. Supports fluid_bahamas_ups_97k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 97326; date_signed 2019-06-13.",
)

# === Cycle 1024 ===
row_doc(
    "misc_suriname_fence_81k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Suriname NEC fence construction",
    "Suriname",
    "2 May 2012: Department of State awards contract SNS50012M0312 for NEC fence construction (PoP Suriname); obligated USD 81,350. CapEx face = award obligation. Recipient redacted; exact site unnamed — lat/lon blank.",
    "81350", "2012-05-02", "2012", "", "",
    "NEC fence construction, Suriname (USASpending PoP Suriname; site not named — lat/lon blank).",
    "usaspending_misc_suriname_fence_81k_2012",
    "MAINT. NEC FENCE CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNS50012M0312_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1024",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SNS50012M0312_1900_-NONE-_-NONE- (Suriname NEC fence). Signed 2012-05-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNS50012M0312_1900_-NONE-_-NONE-/.",
    "USASpending: Suriname NEC fence USD 0.081m. Supports misc_suriname_fence_81k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 81350; date_signed 2012-05-02.",
)

row_doc(
    "technic_panama_pool_electrical_87k_2020",
    "energy", "power_plants_grid", "other",
    "Technic Contractors — Panama CMR pool electrical construction repair",
    "Panama",
    "30 Sep 2020: Department of State awards contract 19PM0720P0895 to Technic Contractors for CMR pool electrical construction deficiency repair (PoP Panama); obligated USD 87,177.63. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "87177.63", "2020-09-30", "2020", "", "",
    "CMR pool electrical construction deficiency repair, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_technic_panama_pool_electrical_87k_2020",
    "CMR - POOL ELECTRICAL CONSTRUCTION DEFICIENCY REPAIR FWP#293",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0720P0895_1900_-NONE-_-NONE-/",
    "Actor: Technic Contractors Corp. (Panama) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1024",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0720P0895_1900_-NONE-_-NONE- (Technic Panama pool electrical). Signed 2020-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0720P0895_1900_-NONE-_-NONE-/.",
    "USASpending: Technic Panama pool electrical USD 0.087m. Supports technic_panama_pool_electrical_87k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 87177.63; date_signed 2020-09-30.",
)

row_doc(
    "heriberto_coban_force_protection_98k_2011",
    "infrastructure", "building_materials", "other",
    "Heriberto Osegueda — Guatemala Cobán base force protection structures",
    "Guatemala",
    "23 Sep 2011: DoD awards contract W9127811P0332 to Heriberto Antonio Osegueda Martínez for construction with incidental design base force protection structures Cobán, Guatemala; obligated USD 98,258.36. CapEx face = award obligation.",
    "98258.36", "2011-09-23", "2011", "15.470", "-90.375",
    "Base force protection structures, Cobán, Guatemala (USASpending description; Cobán named).",
    "usaspending_heriberto_coban_force_protection_98k_2011",
    "TAS::21 2020::TAS CONSTRUCTION WITH INCIDENTAL DESIGN BASE FORCE PROTECTION STRUCTURES COBAN, GUATEMALA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0332_9700_-NONE-_-NONE-/",
    "Actor: Heriberto Antonio Osegueda Martínez (San Salvador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1024",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811P0332_9700_-NONE-_-NONE- (Heriberto Cobán force protection). Signed 2011-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0332_9700_-NONE-_-NONE-/.",
    "USASpending: Heriberto Cobán force protection USD 0.098m. Supports heriberto_coban_force_protection_98k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 98258.36; date_signed 2011-09-23.",
)

row_doc(
    "hollingsworth_haiti_power_plant_design_96k_2014",
    "infrastructure", "engineering_epc", "us",
    "Hollingsworth-Pack — Haiti NEC central power plant design",
    "Haiti",
    "1 Aug 2014: Department of State awards order SAQMMA14F2560 to Hollingsworth-Pack for design services for the central power plant at the Haiti NEC; obligated USD 95,617.40. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "95617.4", "2014-08-01", "2014", "", "",
    "Central power plant design services at Haiti NEC (USASpending PoP Haiti; site not named — lat/lon blank).",
    "usaspending_hollingsworth_haiti_power_plant_design_96k_2014",
    "''IGF::OT::IGF'' THE CONTRACTOR IS TO PROVIDE DESIGN SERVICES FOR THE CENTRAL POWER PLANT AT THE HAI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F2560_1900_SAQMMA13D0194_1900/",
    "Actor: Hollingsworth-Pack Corporation (Williamsburg VA, U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1024",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14F2560_1900_SAQMMA13D0194_1900 (Hollingsworth Haiti power plant design). Signed 2014-08-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14F2560_1900_SAQMMA13D0194_1900/.",
    "USASpending: Hollingsworth Haiti power plant design USD 0.096m. Supports hollingsworth_haiti_power_plant_design_96k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 95617.4; date_signed 2014-08-01.",
)

row_doc(
    "arias_granados_cmr_pool_107k_2017",
    "infrastructure", "building_materials", "other",
    "Arias Granados Engineers — Panama CMR pool area renovation",
    "Panama",
    "9 Aug 2017: DoD awards contract SPM07017M0775 to Arias Granados Engineers for Panama 2017 CMR pool area renovation; obligated USD 107,000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "107000", "2017-08-09", "2017", "", "",
    "CMR pool area renovation, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_arias_granados_cmr_pool_107k_2017",
    "PANAMA 2017 CMR POOL AREA RENOVATION IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07017M0775_1900_-NONE-_-NONE-/",
    "Actor: Arias Granados Engineers S.A. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1024",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07017M0775_1900_-NONE-_-NONE- (Arias Granados CMR pool). Signed 2017-08-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07017M0775_1900_-NONE-_-NONE-/.",
    "USASpending: Arias Granados CMR pool USD 0.107m. Supports arias_granados_cmr_pool_107k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 107000; date_signed 2017-08-09.",
)

# === Cycle 1025 ===
row_doc(
    "kunkel_amphibian_rescue_94k_2019",
    "infrastructure", "building_materials", "other",
    "Kunkel Construction — Panama Amphibian Rescue Center phase III",
    "Panama",
    "3 Jun 2019: Smithsonian awards contract 33330219CT0010226 to Kunkel Construction for construction services for the Amphibian Rescue Center phase III project (PoP Panama); obligated USD 93,917.51. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "93917.51", "2019-06-03", "2019", "", "",
    "Amphibian Rescue Center phase III construction, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_kunkel_amphibian_rescue_94k_2019",
    "CONSTRUCTION SERVICES FOR THE AMPHIBIAN RESCUE CENTER PHASE III PROJECT, GA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219CT0010226_3300_-NONE-_-NONE-/",
    "Actor: Kunkel Construction, Inc. (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1025",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330219CT0010226_3300_-NONE-_-NONE- (Kunkel Amphibian Rescue). Signed 2019-06-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330219CT0010226_3300_-NONE-_-NONE-/.",
    "USASpending: Kunkel Amphibian Rescue USD 0.094m. Supports kunkel_amphibian_rescue_94k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 93917.51; date_signed 2019-06-03.",
)

row_doc(
    "cym_stri_ancon_chiller_room_86k_2021",
    "energy", "power_plants_grid", "other",
    "Construcciones y Mantenimientos — Panama STRI Ancon chiller room",
    "Panama",
    "17 Aug 2021: Smithsonian awards contract 33330221CF0010353 to Construcciones y Mantenimientos for construction of new room for AC chillers at STRI Ancon; obligated USD 85,845. CapEx face = award obligation.",
    "85845", "2021-08-17", "2021", "8.983", "-79.546",
    "New room for AC chillers at STRI Ancon, Panama (USASpending description; STRI Ancon named).",
    "usaspending_cym_stri_ancon_chiller_room_86k_2021",
    "TO FURNISH SERVICE, LABOR, MATERIAL AND TRANSPORT FOR CONSTRUCTION OF NEW ROOM FOR AC CHILLERS AT STRI ANCON.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010353_3300_-NONE-_-NONE-/",
    "Actor: Construcciones y Mantenimientos (Panama) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1025",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330221CF0010353_3300_-NONE-_-NONE- (CYM STRI Ancon chiller room). Signed 2021-08-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010353_3300_-NONE-_-NONE-/.",
    "USASpending: CYM STRI Ancon chiller room USD 0.086m. Supports cym_stri_ancon_chiller_room_86k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 85845; date_signed 2021-08-17.",
)

row_doc(
    "proyectos_achiote_clinic_101k_2013",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles — Panama Achiote clinic and school improvements",
    "Panama",
    "26 Sep 2013: DoD awards contract W912CL13C0013 to Proyectos Civiles S y M for Achiote clinic and school improvements (PoP Panama); obligated USD 100,944.86. CapEx face = award obligation.",
    "100944.86", "2013-09-26", "2013", "", "",
    "Clinic and school improvements, Achiote, Panama (USASpending description; Achiote named but coordinates not sourced — lat/lon blank).",
    "usaspending_proyectos_achiote_clinic_101k_2013",
    "ACHIOTE CLINIC AND SCHOOL IMPROVEMENTS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL13C0013_9700_-NONE-_-NONE-/",
    "Actor: Proyectos Civiles S y M Limitada — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1025",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL13C0013_9700_-NONE-_-NONE- (Achiote clinic). Signed 2013-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL13C0013_9700_-NONE-_-NONE-/.",
    "USASpending: Achiote clinic USD 0.101m. Supports proyectos_achiote_clinic_101k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 100944.86; date_signed 2013-09-26.",
)

row_doc(
    "oeg_juarez_electrical_82k_2010",
    "energy", "power_plants_grid", "us",
    "OEG — Mexico Ciudad Juárez power systems electrical work",
    "Mexico",
    "14 Sep 2010: Department of State awards order SAQMMA10F4012 to OEG for power systems Ciudad Juárez electrical work (PoP Mexico); obligated USD 82,216. CapEx face = award obligation.",
    "82216", "2010-09-14", "2010", "31.690", "-106.425",
    "Power systems electrical work, Ciudad Juárez, Mexico (USASpending description; Ciudad Juárez named).",
    "usaspending_oeg_juarez_electrical_82k_2010",
    "POWER SYSTEMS CIUDAD JUAREZ ELECTRICAL WORK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F4012_1900_SALMEC05D0005_1900/",
    "Actor: OEG Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1025",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F4012_1900_SALMEC05D0005_1900 (OEG Juárez electrical). Signed 2010-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F4012_1900_SALMEC05D0005_1900/.",
    "USASpending: OEG Juárez electrical USD 0.082m. Supports oeg_juarez_electrical_82k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 82216; date_signed 2010-09-14.",
)

row_doc(
    "york_panama_chiller_supplies_95k_2014",
    "energy", "power_plants_grid", "us",
    "York International — Panama STRI chiller and supplies",
    "Panama",
    "24 Jun 2014: Smithsonian awards contract F14PO7390000303497 to York International for FY2014 chiller and supplies (PoP Panama); obligated USD 94,987.25. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "94987.25", "2014-06-24", "2014", "", "",
    "Chiller and supplies, Panama (USASpending PoP Panama; site not named — lat/lon blank).",
    "usaspending_york_panama_chiller_supplies_95k_2014",
    "IGF::OT::IGF  REQUIRED SERVICES ARE NOT PROVIDED BY AGENCY EMPLOYEES. FY2014- CHILLER&SUPPLIES FOR S",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F14PO7390000303497_3300_-NONE-_-NONE-/",
    "Actor: York International Corporation (York PA, U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1025",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F14PO7390000303497_3300_-NONE-_-NONE- (York Panama chiller supplies). Signed 2014-06-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F14PO7390000303497_3300_-NONE-_-NONE-/.",
    "USASpending: York Panama chiller supplies USD 0.095m. Supports york_panama_chiller_supplies_95k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 94987.25; date_signed 2014-06-24.",
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
    print(f"cycles1023-1025 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
