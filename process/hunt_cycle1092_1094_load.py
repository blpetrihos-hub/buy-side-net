#!/usr/bin/env python3
"""Cycles 1092–1094: USASpending LatAm CapEx residual (~USD0.038–0.055m).

Seeds: 20262092–20262094. Thin top-up dry. Includes Nicaragua playground CapEx.
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


# === Cycle 1092 (seed 20262092) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "wje_trinidad_port_of_spain_seismic_45k_2012",
    "infrastructure", "engineering_epc", "us",
    'Wiss Janney Elstner — Trinidad Port of Spain limited seismicity update',
    "Trinidad and Tobago",
    '26 Sep 2012: Department of State awards order SAQMMA12F4504 under IDV SAQMMA08D0071 to Wiss, Janney, Elstner Associates, Inc. for limited seismicity update of the seismic hazard of the site in Port of Spain, Trinidad; obligated USD 45,031. CapEx face = award obligation. Exact site unnamed — lat/lon blank.',
    "45031", "2012-09-26", "2012", "", "",
    'Limited seismicity update for site in Port of Spain, Trinidad (USASpending description; Port of Spain named, site coords not stated — lat/lon blank).',
    "usaspending_wje_trinidad_port_of_spain_seismic_45k_2012",
    'LIMITED SEISMICITY UPDATE OF THE SEISMIC HAZARD OF THE SITE IN PORT OF SPAIN, TRINIDAD IN ACCORDANCE WITH THE SCOPE OF WORK',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F4504_1900_SAQMMA08D0071_1900/",
    'Actor: Wiss, Janney, Elstner Associates, Inc. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx. Holdover closed.',
    "hunt_cycle1092",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F4504_1900_SAQMMA08D0071_1900 (WJE Trinidad Port of Spain seismic). Signed 2012-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F4504_1900_SAQMMA08D0071_1900/.',
    'USASpending: WJE Trinidad Port of Spain seismic USD 0.045m. Supports wje_trinidad_port_of_spain_seismic_45k_2012.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 45031; date_signed 2012-09-26.',
)
row_doc(
    "play_mart_nicaragua_embassy_playground_44k_2020",
    "infrastructure", "building_materials", "us",
    'Play Mart — Nicaragua Embassy Managua playground equipment supply and installation',
    "Nicaragua",
    '30 Sep 2020: Department of State awards contract 19NU7020P0650 to Play Mart Inc for playground equipment supply and installation at Embassy Managua (PoP Nicaragua); obligated USD 43,960.34. CapEx face = award obligation. Exact playground footprint unnamed — lat/lon blank.',
    "43960.34", "2020-09-30", "2020", "", "",
    'Playground equipment supply and installation, Embassy Managua, Nicaragua (USASpending description; embassy named, site coords not stated — lat/lon blank).',
    "usaspending_play_mart_nicaragua_embassy_playground_44k_2020",
    'PLAYGROUND EQUIPMENT SUPPLY AND INSTALLATION-EMBASSY MANAGUA',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NU7020P0650_1900_-NONE-_-NONE-/",
    'Actor: Play Mart Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Weight under-covered Nicaragua.',
    "hunt_cycle1092",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19NU7020P0650_1900_-NONE-_-NONE- (Play Mart Nicaragua Embassy playground). Signed 2020-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19NU7020P0650_1900_-NONE-_-NONE-/.',
    'USASpending: Play Mart Nicaragua Embassy playground USD 0.044m. Supports play_mart_nicaragua_embassy_playground_44k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 43960.34; date_signed 2020-09-30.',
)
row_doc(
    "misc_haiti_guard_booth_construction_54k_2023",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Haiti guard booth construction and repair',
    "Haiti",
    '7 Jun 2023: Department of State awards contract 19HA7023P0828 for guard booth construction and repair (PoP Haiti); obligated USD 53,890.10. CapEx face = award obligation. Exact booth site unnamed — lat/lon blank.',
    "53890.10", "2023-06-07", "2023", "", "",
    'Guard booth construction and repair, Haiti (USASpending description; site not named — lat/lon blank).',
    "usaspending_misc_haiti_guard_booth_construction_54k_2023",
    'GUARD BOOTH CONSTRUCTION AND REPAIR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P0828_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Weight under-covered Haiti. Holdover closed.',
    "hunt_cycle1092",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7023P0828_1900_-NONE-_-NONE- (Haiti guard booth). Signed 2023-06-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7023P0828_1900_-NONE-_-NONE-/.',
    'USASpending: Haiti guard booth USD 0.054m. Supports misc_haiti_guard_booth_construction_54k_2023.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53890.10; date_signed 2023-06-07.',
)
row_doc(
    "misc_argentina_exterior_flooring_replacement_55k_2026",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Argentina exterior flooring replacement',
    "Argentina",
    '13 Aug 2026: Department of State awards contract 19AR2026C0011 for FAC exterior flooring replacement (PoP Argentina); obligated USD 54,604.30. CapEx face = award obligation. Exact flooring area unnamed — lat/lon blank.',
    "54604.30", "2026-08-13", "2026", "", "",
    'FAC exterior flooring replacement, Argentina (USASpending description; site not named — lat/lon blank).',
    "usaspending_misc_argentina_exterior_flooring_replacement_55k_2026",
    'FAC - EXTERIOR FLOORING REPLACEMENT',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2026C0011_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1092",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2026C0011_1900_-NONE-_-NONE- (Argentina exterior flooring). Signed 2026-08-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2026C0011_1900_-NONE-_-NONE-/.',
    'USASpending: Argentina exterior flooring USD 0.055m. Supports misc_argentina_exterior_flooring_replacement_55k_2026.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 54604.30; date_signed 2026-08-13.',
)
row_doc(
    "misc_brazil_cob_hallway_floor_tiles_54k_2010",
    "infrastructure", "building_materials", "other",
    'Miscellaneous foreign awardees — Brazil COB hallway floor tile replacement all floors',
    "Brazil",
    '16 Jun 2010: Department of State awards contract SBR82010M1503M001 to replace floor tiles of hallways at all floors at COB (PoP Brazil); obligated USD 54,002. CapEx face = award obligation. Exact COB unnamed — lat/lon blank.',
    "54002", "2010-06-16", "2010", "", "",
    'Replace floor tiles of hallways at all floors at COB, Brazil (USASpending description; COB named, site coords not stated — lat/lon blank).',
    "usaspending_misc_brazil_cob_hallway_floor_tiles_54k_2010",
    'REPLACE FLOOR TILES OF HALLWAYS AT ALL FLOORS AT COB.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82010M1503M001_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1092",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82010M1503M001_1900_-NONE-_-NONE- (Brazil COB hallway floor tiles). Signed 2010-06-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82010M1503M001_1900_-NONE-_-NONE-/.',
    'USASpending: Brazil COB hallway floor tiles USD 0.054m. Supports misc_brazil_cob_hallway_floor_tiles_54k_2010.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 54002; date_signed 2010-06-16.',
)

# === Cycle 1093 (seed 20262093) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "apollo_jamaica_motorpool_govs_canopy_41k_2014",
    "infrastructure", "building_materials", "us",
    'Apollo Sunguard Systems — Jamaica motorpool canopy for GOVs',
    "Jamaica",
    '25 Sep 2014: Department of State awards contract SJM37014M1199 to Apollo Sunguard Systems Inc for motorpool canopy for GOVs (PoP Jamaica); obligated USD 40,631.78. CapEx face = award obligation. Exact motorpool unnamed — lat/lon blank.',
    "40631.78", "2014-09-25", "2014", "", "",
    'Motorpool canopy for GOVs, Jamaica (USASpending description; motorpool not named — lat/lon blank).',
    "usaspending_apollo_jamaica_motorpool_govs_canopy_41k_2014",
    'IGF::OT::IGF EOFY-MPOOL-CANOPY FOR GOVS-ICASS AND PROGRAM',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37014M1199_1900_-NONE-_-NONE-/",
    'Actor: Apollo Sunguard Systems Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1093",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37014M1199_1900_-NONE-_-NONE- (Apollo Jamaica motorpool canopy). Signed 2014-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37014M1199_1900_-NONE-_-NONE-/.',
    'USASpending: Apollo Jamaica motorpool canopy USD 0.041m. Supports apollo_jamaica_motorpool_govs_canopy_41k_2014.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 40631.78; date_signed 2014-09-25.',
)
row_doc(
    "fabrication_designs_brazil_metal_door_screen_38k_2024",
    "infrastructure", "building_materials", "us",
    'Fabrication Designs — Brazil metal door screen frame for international embassies',
    "Brazil",
    '22 Sep 2024: Department of State awards contract 19AQMM24P1138 to Fabrication Designs, Inc. for metal door screen frame etc. for international embassies (PoP Brazil); obligated USD 38,400.04. CapEx face = award obligation. Exact embassy site unnamed — lat/lon blank.',
    "38400.04", "2024-09-22", "2024", "", "",
    'Metal door screen frame for international embassies, Brazil (USASpending description; embassy not named — lat/lon blank).',
    "usaspending_fabrication_designs_brazil_metal_door_screen_38k_2024",
    'METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P1138_1900_-NONE-_-NONE-/",
    'Actor: Fabrication Designs, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1093",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P1138_1900_-NONE-_-NONE- (Fabrication Designs Brazil metal door). Signed 2024-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P1138_1900_-NONE-_-NONE-/.',
    'USASpending: Fabrication Designs Brazil metal door USD 0.038m. Supports fabrication_designs_brazil_metal_door_screen_38k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 38400.04; date_signed 2024-09-22.',
)
row_doc(
    "misc_uruguay_chancery_mv_switchgear_53k_2020",
    "energy", "power_plants_grid", "other",
    'Miscellaneous foreign awardees — Uruguay chancery medium-voltage switchgear install',
    "Uruguay",
    '18 Mar 2020: Department of State awards contract 19UY6020P0230 to install new medium voltage switchgear equipment power service as part of the chancery power increase project (PoP Uruguay); obligated USD 52,983.18. CapEx face = award obligation. Exact switchgear room unnamed — lat/lon blank.',
    "52983.18", "2020-03-18", "2020", "", "",
    'Install new medium voltage switchgear for chancery power increase, Uruguay (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_misc_uruguay_chancery_mv_switchgear_53k_2020",
    'INSTALL NEW MEDIUM VOLTAGE SWITCHGEAR EQUIPMENT POWER SERVICE AS PART OF THE CHANCERY POWER INCREASE PROJECT',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6020P0230_1900_-NONE-_-NONE-/",
    'Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.',
    "hunt_cycle1093",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19UY6020P0230_1900_-NONE-_-NONE- (Uruguay chancery MV switchgear). Signed 2020-03-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6020P0230_1900_-NONE-_-NONE-/.',
    'USASpending: Uruguay chancery MV switchgear USD 0.053m. Supports misc_uruguay_chancery_mv_switchgear_53k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 52983.18; date_signed 2020-03-18.',
)
row_doc(
    "trinidad_el_salvador_ilopongo_barracks_renovate_54k_2011",
    "infrastructure", "building_materials", "other",
    'Sociedad Comercializadora Trinidad — El Salvador Ilopongo CEAT barracks/armory renovation',
    "El Salvador",
    '4 Apr 2011: Department of Defense awards contract W9127811P0189 to Sociedad Comercializadora Trinidad S.A. de C.V. to renovate barracks D/C armory CEAT, Ilopongo, El Salvador; obligated USD 53,994.38. CapEx face = award obligation. Exact barracks footprint unnamed — lat/lon blank.',
    "53994.38", "2011-04-04", "2011", "", "",
    'Renovate barracks D/C armory CEAT, Ilopongo, El Salvador (USASpending description; Ilopongo named, site coords not stated — lat/lon blank).',
    "usaspending_trinidad_el_salvador_ilopongo_barracks_renovate_54k_2011",
    'TAS::97 0500::TAS RENOVATE BARRACKS D/C ARMORY CEAT, ILAPONGO, EL SALVADOR',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0189_9700_-NONE-_-NONE-/",
    'Actor: Sociedad Comercializadora Trinidad S.A. de C.V. (El Salvador) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1093",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127811P0189_9700_-NONE-_-NONE- (Trinidad El Salvador Ilopongo barracks). Signed 2011-04-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127811P0189_9700_-NONE-_-NONE-/.',
    'USASpending: Trinidad El Salvador Ilopongo barracks USD 0.054m. Supports trinidad_el_salvador_ilopongo_barracks_renovate_54k_2011.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53994.38; date_signed 2011-04-04.',
)
row_doc(
    "mhg_brazil_facility_infra_upgrades_54k_2025",
    "energy", "power_plants_grid", "other",
    'MHG Projetos e Construcoes — Brazil facility infrastructure upgrades (electrical/HVAC)',
    "Brazil",
    '3 Sep 2025: Department of State awards contract 19BR9325P0717 to MHG Projetos e Construcoes Ltda. for facility infrastructure upgrades (30sqm) including electrical, HVAC and thermal-acoustic improvements (PoP Brazil); obligated USD 53,627.68. CapEx face = award obligation. Exact facility unnamed — lat/lon blank.',
    "53627.68", "2025-09-03", "2025", "", "",
    'Facility infrastructure upgrades (30sqm) including electrical, HVAC and thermal-acoustic improvements, Brazil (USASpending description; facility not named — lat/lon blank).',
    "usaspending_mhg_brazil_facility_infra_upgrades_54k_2025",
    'FACILITY INFRASTRUCTURE UPGRADES (30SQM) INCLUDING ELECTRICAL, HVAC AND THERMAL-ACOUSTIC IMPROVEMENTS. RFQ 19BR9325Q0021',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9325P0717_1900_-NONE-_-NONE-/",
    'Actor: MHG Projetos e Construcoes Ltda. (Brazil) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.',
    "hunt_cycle1093",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9325P0717_1900_-NONE-_-NONE- (MHG Brazil facility infrastructure upgrades). Signed 2025-09-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9325P0717_1900_-NONE-_-NONE-/.',
    'USASpending: MHG Brazil facility infrastructure upgrades USD 0.054m. Supports mhg_brazil_facility_infra_upgrades_54k_2025.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53627.68; date_signed 2025-09-03.',
)

# === Cycle 1094 (seed 20262094) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "hardline_dr_puerto_plata_forced_entry_doors_38k_2020",
    "infrastructure", "building_materials", "us",
    'Hardline Nati Construction — Dominican Republic Puerto Plata consulate forced-entry doors/windows',
    "Dominican Republic",
    '30 Sep 2020: Department of State awards contract 19DR8620P1225 to Hardline Nati Construction LLC for OBO installation of forced entry doors/windows at consulate Puerto Plata (PoP Dominican Republic); obligated USD 37,691.18. CapEx face = award obligation. Exact consulate site unnamed — lat/lon blank.',
    "37691.18", "2020-09-30", "2020", "", "",
    'OBO installation forced entry doors/windows, consulate Puerto Plata, Dominican Republic (USASpending description; Puerto Plata named, site coords not stated — lat/lon blank).',
    "usaspending_hardline_dr_puerto_plata_forced_entry_doors_38k_2020",
    'OBO INSTALLATION FORCED ENTRY DOORS/WINDS CONS PUERTO PLATA',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8620P1225_1900_-NONE-_-NONE-/",
    'Actor: Hardline Nati Construction LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1094",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8620P1225_1900_-NONE-_-NONE- (Hardline DR Puerto Plata forced-entry doors). Signed 2020-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8620P1225_1900_-NONE-_-NONE-/.',
    'USASpending: Hardline DR Puerto Plata forced-entry doors USD 0.038m. Supports hardline_dr_puerto_plata_forced_entry_doors_38k_2020.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37691.18; date_signed 2020-09-30.',
)
row_doc(
    "bentley_mills_chile_chancery_carpet_tiles_38k_2016",
    "infrastructure", "building_materials", "us",
    'Bentley Mills — Chile chancery carpet tile replacement',
    "Chile",
    '12 Feb 2016: Department of State awards contract SCI80016M0273 to Bentley Mills Inc for replacement of carpet tiles at chancery (PoP Chile); obligated USD 37,640.30. CapEx face = award obligation. Exact chancery unnamed — lat/lon blank.',
    "37640.30", "2016-02-12", "2016", "", "",
    'Replacement of carpet tiles / chancery, Chile (USASpending description; chancery named, site coords not stated — lat/lon blank).',
    "usaspending_bentley_mills_chile_chancery_carpet_tiles_38k_2016",
    'FAC - REPLACEMENT OF CARPET TILES / CHANCERY IGF::CL::IGF',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80016M0273_1900_-NONE-_-NONE-/",
    'Actor: Bentley Mills Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.',
    "hunt_cycle1094",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCI80016M0273_1900_-NONE-_-NONE- (Bentley Mills Chile chancery carpet). Signed 2016-02-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80016M0273_1900_-NONE-_-NONE-/.',
    'USASpending: Bentley Mills Chile chancery carpet USD 0.038m. Supports bentley_mills_chile_chancery_carpet_tiles_38k_2016.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 37640.30; date_signed 2016-02-12.',
)
row_doc(
    "qa_colombia_macarena_concrete_wall_53k_2022",
    "infrastructure", "building_materials", "other",
    'QA Construction Services — Colombia La Macarena Army Base reinforced concrete wall',
    "Colombia",
    '30 Sep 2022: Department of Defense awards task order W9127822F0478 under IDV W9127821D0081 to QA Construction Services S.A.S. to construct reinforced concrete wall at La Macarena Army Base, Meta, Colombia; obligated USD 53,401.15. CapEx face = award obligation. Exact wall alignment unnamed — lat/lon blank.',
    "53401.15", "2022-09-30", "2022", "", "",
    'Construct reinforced concrete wall, La Macarena Army Base, Meta, Colombia (USASpending description; La Macarena named, wall coords not stated — lat/lon blank).',
    "usaspending_qa_colombia_macarena_concrete_wall_53k_2022",
    'CONSTRUCT REINFORCED CONCRETE WALL, LA MACARENA ARMY BASE, META, COLOMBIA.',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0478_9700_W9127821D0081_9700/",
    'Actor: QA Construction Services S.A.S. (Colombia) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.',
    "hunt_cycle1094",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0478_9700_W9127821D0081_9700 (QA Colombia La Macarena concrete wall). Signed 2022-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0478_9700_W9127821D0081_9700/.',
    'USASpending: QA Colombia La Macarena concrete wall USD 0.053m. Supports qa_colombia_macarena_concrete_wall_53k_2022.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53401.15; date_signed 2022-09-30.',
)
row_doc(
    "supera_brazil_office_relocation_renovation_54k_2024",
    "infrastructure", "building_materials", "other",
    'Supera Engenharia — Brazil office relocation and renovation',
    "Brazil",
    '11 Sep 2024: Department of State awards contract 19BR2524P1592 to Supera Engenharia Ltda for office relocation and renovation (PoP Brazil); obligated USD 53,674.65. CapEx face = award obligation. Exact office unnamed — lat/lon blank.',
    "53674.65", "2024-09-11", "2024", "", "",
    'Office relocation and renovation, Brazil (USASpending description; office not named — lat/lon blank).',
    "usaspending_supera_brazil_office_relocation_renovation_54k_2024",
    'OFFICE RELOCATION & RENOVATION',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2524P1592_1900_-NONE-_-NONE-/",
    'Actor: Supera Engenharia Ltda (Brazil) — other. Official USASpending Award API. Shuffle building_materials.',
    "hunt_cycle1094",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2524P1592_1900_-NONE-_-NONE- (Supera Brazil office renovation). Signed 2024-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2524P1592_1900_-NONE-_-NONE-/.',
    'USASpending: Supera Brazil office renovation USD 0.054m. Supports supera_brazil_office_relocation_renovation_54k_2024.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 53674.65; date_signed 2024-09-11.',
)
row_doc(
    "technique_haiti_copper_fiber_chancery_stecher_55k_2018",
    "infrastructure", "building_materials", "other",
    'Technique Industrie Agriculture — Haiti copper and fiber install between chancery and Stecher Romain',
    "Haiti",
    '13 Aug 2018: Department of State awards contract 19HA7018P0971 to Technique Industrie Agriculture S A for copper and fiber install between chancery and Stecher Romain (PoP Haiti); obligated USD 54,916. CapEx face = award obligation. Exact pathway unnamed — lat/lon blank.',
    "54916", "2018-08-13", "2018", "", "",
    'Copper and fiber install between chancery and Stecher Romain, Haiti (USASpending description; Stecher Romain named, pathway coords not stated — lat/lon blank).',
    "usaspending_technique_haiti_copper_fiber_chancery_stecher_55k_2018",
    'COPPER AND FIBER INSTALL BETWEEN CHANCERY AND STECHER ROMAIN',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7018P0971_1900_-NONE-_-NONE-/",
    'Actor: Technique Industrie Agriculture S A (Haiti) — other. Official USASpending Award API. Shuffle building_materials. Weight under-covered Haiti.',
    "hunt_cycle1094",
    'U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7018P0971_1900_-NONE-_-NONE- (Technique Haiti copper/fiber). Signed 2018-08-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7018P0971_1900_-NONE-_-NONE-/.',
    'USASpending: Technique Haiti copper/fiber USD 0.055m. Supports technique_haiti_copper_fiber_chancery_stecher_55k_2018.',
    'Opened USASpending Award API 2026-10-05; total_obligation USD 54916; date_signed 2018-08-13.',
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
