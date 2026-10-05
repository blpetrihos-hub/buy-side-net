#!/usr/bin/env python3
"""Cycles 1080–1082: USASpending LatAm CapEx residual (~USD0.050–0.060m).

Seeds: 20262080–20262082. Thin top-up dry.
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


# === Cycle 1080 (seed 20262080) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "victory_awning_panama_carport_canopy_52k_2014",
    "infrastructure", "building_materials", "us",
    "Victory Awning — Panama pre-engineered carport canopy for armored vehicles",
    "Panama",
    "26 Sep 2014: Department of State awards order SPM07014F0271 to Victory Awning Inc for pre-engineered carport canopy to protect armored vehicles (PoP Panama); obligated USD 52,142.20. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "52142.20", "2014-09-26", "2014", "", "",
    "Pre-engineered carport canopy to protect armored vehicles, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_victory_awning_panama_carport_canopy_52k_2014",
    "PRE-ENGINEERED CARPORT CANOPY (TO PROTECT ARMORED VEH)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014F0271_1900_GS07F0651W_4730/",
    "Actor: Victory Awning Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1080",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07014F0271_1900_GS07F0651W_4730 (Victory Awning Panama carport). Signed 2014-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014F0271_1900_GS07F0651W_4730/.",
    "USASpending: Victory Awning Panama carport USD 0.052m. Supports victory_awning_panama_carport_canopy_52k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 52142.20; date_signed 2014-09-26.",
)

row_doc(
    "psi_colombia_generators_60kw_51k_2019",
    "energy", "power_plants_grid", "us",
    "Project Services International — Colombia 60 kW/75 kVA diesel generators",
    "Colombia",
    "25 Sep 2019: Department of the Army awards contract W913FT19P0069 to Project Services International Corporation for generators 60KW/75KVA power plant diesel (PoP Colombia); obligated USD 50,567. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "50567", "2019-09-25", "2019", "", "",
    "Generators 60 kW/75 kVA power plant diesel, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_psi_colombia_generators_60kw_51k_2019",
    "GENERATORS 60KW/75KVA POWER PLANT DIESEL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT19P0069_9700_-NONE-_-NONE-/",
    "Actor: Project Services International Corporation (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx. Holdover closed.",
    "hunt_cycle1080",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT19P0069_9700_-NONE-_-NONE- (PSI Colombia generators). Signed 2019-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT19P0069_9700_-NONE-_-NONE-/.",
    "USASpending: PSI Colombia generators USD 0.051m. Supports psi_colombia_generators_60kw_51k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 50567; date_signed 2019-09-25.",
)

row_doc(
    "misc_dr_maritime_ops_center_remodel_60k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic Armada maritime operations center remodeling",
    "Dominican Republic",
    "14 Aug 2023: Department of State awards contract 19DR8623C0035 for maritime operations center remodeling for Armada RD (PoP Dominican Republic); obligated USD 60,195.06. CapEx face = award obligation. Exact center unnamed — lat/lon blank.",
    "60195.06", "2023-08-14", "2023", "", "",
    "Maritime operations center remodeling for Armada RD, Dominican Republic (USASpending description; center not named — lat/lon blank).",
    "usaspending_misc_dr_maritime_ops_center_remodel_60k_2023",
    "MARITIME OPERATIONS CENTER REMODELING - ARMADA RD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0035_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1080",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8623C0035_1900_-NONE-_-NONE- (DR maritime ops center remodel). Signed 2023-08-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0035_1900_-NONE-_-NONE-/.",
    "USASpending: DR maritime ops center remodel USD 0.060m. Supports misc_dr_maritime_ops_center_remodel_60k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60195.06; date_signed 2023-08-14.",
)

row_doc(
    "misc_bahamas_electrical_refurbish_60k_2014",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Bahamas SHPY electrical refurbish",
    "Bahamas",
    "30 Sep 2014: Department of State awards contract SBF50014M0946 for SHPY electrical refurbish (PoP Bahamas); obligated USD 60,159.96. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "60159.96", "2014-09-30", "2014", "", "",
    "SHPY electrical refurbish, Bahamas (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_bahamas_electrical_refurbish_60k_2014",
    "IGF::OT::IGF SHPY - ELECTRICAL REFURBISH",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50014M0946_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1080",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50014M0946_1900_-NONE-_-NONE- (Bahamas electrical refurbish). Signed 2014-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50014M0946_1900_-NONE-_-NONE-/.",
    "USASpending: Bahamas electrical refurbish USD 0.060m. Supports misc_bahamas_electrical_refurbish_60k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60159.96; date_signed 2014-09-30.",
)

row_doc(
    "misc_colombia_barranquilla_structured_cabling_60k_2016",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Colombia Barranquilla COLAF ABD structured cabling",
    "Colombia",
    "24 Jun 2016: Department of State awards contract SCO15016C0004 for ABD structured cabling for ABD at COLAF base Barranquilla (PoP Colombia); obligated USD 60,089.16. CapEx face = award obligation. Exact base site unnamed — lat/lon blank.",
    "60089.16", "2016-06-24", "2016", "", "",
    "Structured cabling for ABD at COLAF base Barranquilla, Colombia (USASpending description; Barranquilla named, site coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_barranquilla_structured_cabling_60k_2016",
    "ABD. STRUCTURED CABLING FOR ABD AT COLAF BASE BARRANQUILLA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15016C0004_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc. Holdover closed.",
    "hunt_cycle1080",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15016C0004_1900_-NONE-_-NONE- (Colombia Barranquilla cabling). Signed 2016-06-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15016C0004_1900_-NONE-_-NONE-/.",
    "USASpending: Colombia Barranquilla cabling USD 0.060m. Supports misc_colombia_barranquilla_structured_cabling_60k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60089.16; date_signed 2016-06-24.",
)

# === Cycle 1081 (seed 20262081) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "tsi_ecuador_outdoor_xups_51k_2010",
    "energy", "power_plants_grid", "us",
    "TSI Power — Ecuador outdoor XUPS",
    "Ecuador",
    "23 Sep 2010: Department of State awards contract SEC75010M1435 to TSI Power Corp. for outdoor XUPS (PoP Ecuador); obligated USD 50,882.32. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "50882.32", "2010-09-23", "2010", "", "",
    "Outdoor XUPS, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_tsi_ecuador_outdoor_xups_51k_2010",
    "OUT DOOR XUPS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75010M1435_1900_-NONE-_-NONE-/",
    "Actor: TSI Power Corp. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1081",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SEC75010M1435_1900_-NONE-_-NONE- (TSI Ecuador outdoor XUPS). Signed 2010-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75010M1435_1900_-NONE-_-NONE-/.",
    "USASpending: TSI Ecuador outdoor XUPS USD 0.051m. Supports tsi_ecuador_outdoor_xups_51k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 50882.32; date_signed 2010-09-23.",
)

row_doc(
    "merrick_mexico_eclosion_office_design_51k_2014",
    "infrastructure", "engineering_epc", "us",
    "Merrick & Company — Mexico eclosion facility office building design",
    "Mexico",
    "22 Apr 2014: USDA awards order AG32KWD140094 to Merrick & Company for design services for the office building at the eclosion facility (PoP Mexico); obligated USD 51,341. CapEx face = award obligation. Exact facility unnamed — lat/lon blank.",
    "51341", "2014-04-22", "2014", "", "",
    "Design services for office building at eclosion facility, Mexico (USASpending description; facility not named — lat/lon blank).",
    "usaspending_merrick_mexico_eclosion_office_design_51k_2014",
    "IGF::OT::IGF   DESIGN SERVICES FOR THE OFFICE BUILDING AT THE ECLOSION FACILITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG32KWD140094_12K3_AG6395C110097_12K3/",
    "Actor: Merrick & Company (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1081",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AG32KWD140094_12K3_AG6395C110097_12K3 (Merrick Mexico eclosion design). Signed 2014-04-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG32KWD140094_12K3_AG6395C110097_12K3/.",
    "USASpending: Merrick Mexico eclosion design USD 0.051m. Supports merrick_mexico_eclosion_office_design_51k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 51341; date_signed 2014-04-22.",
)

row_doc(
    "misc_panama_stri_bci_generator_60k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Panama STRI BCI new generator",
    "Panama",
    "5 Jul 2024: Smithsonian Tropical Research Institute awards purchase order 33312924P00510560 for new generator for STRI BCI (PoP Panama); obligated USD 60,000. CapEx face = award obligation. Exact BCI site unnamed — lat/lon blank.",
    "60000", "2024-07-05", "2024", "", "",
    "New generator for STRI BCI, Panama (USASpending description; BCI named, site coords not stated — lat/lon blank).",
    "usaspending_misc_panama_stri_bci_generator_60k_2024",
    "NEW GENERATOR FOR STRI BCI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312924P00510560_3300_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1081",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33312924P00510560_3300_-NONE-_-NONE- (Panama STRI BCI generator). Signed 2024-07-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33312924P00510560_3300_-NONE-_-NONE-/.",
    "USASpending: Panama STRI BCI generator USD 0.060m. Supports misc_panama_stri_bci_generator_60k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60000; date_signed 2024-07-05.",
)

row_doc(
    "maquinas_honduras_12kw_generators_60k_2014",
    "energy", "power_plants_grid", "other",
    "Maquinas y Servicios Tecnicos — Honduras four 12 kW generators with ATS",
    "Honduras",
    "2 Sep 2014: Department of State awards contract SHO80014M0949 to Maquinas y Servicios Tecnicos, S de R.L. for supply, delivery, installation of four 12 kW generators with ATS (PoP Honduras); obligated USD 59,801.28. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.",
    "59801.28", "2014-09-02", "2014", "", "",
    "Supply, delivery, installation of four 12 kW generators with ATS, Honduras (USASpending description; sites not named — lat/lon blank).",
    "usaspending_maquinas_honduras_12kw_generators_60k_2014",
    "SUPPLY, DELIVERY, INSTALLATION OF ( 4) 12KW GENERATORS W/ATS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80014M0949_1900_-NONE-_-NONE-/",
    "Actor: Maquinas y Servicios Tecnicos, S de R.L. (Honduras) — other. Official USASpending Award API. Shuffle power_plants_grid. Holdover closed.",
    "hunt_cycle1081",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80014M0949_1900_-NONE-_-NONE- (Maquinas Honduras 12 kW generators). Signed 2014-09-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80014M0949_1900_-NONE-_-NONE-/.",
    "USASpending: Maquinas Honduras 12 kW generators USD 0.060m. Supports maquinas_honduras_12kw_generators_60k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59801.28; date_signed 2014-09-02.",
)

row_doc(
    "misc_mexico_chancery_tile_replace_60k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico chancery 1st and 5th level tile replacement",
    "Mexico",
    "9 Aug 2012: Department of State awards contract SMX53012M1491 for replace tile on chancery 1st and 5th level (PoP Mexico); obligated USD 59,774.85. CapEx face = award obligation. Exact chancery site unnamed — lat/lon blank.",
    "59774.85", "2012-08-09", "2012", "", "",
    "Replace tile on chancery 1st and 5th level, Mexico (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_chancery_tile_replace_60k_2012",
    "MEX/FM/REPLACE TILE ON CHANCERY 1ST AND 5TH LEVEL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M1491_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1081",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53012M1491_1900_-NONE-_-NONE- (Mexico chancery tile). Signed 2012-08-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012M1491_1900_-NONE-_-NONE-/.",
    "USASpending: Mexico chancery tile USD 0.060m. Supports misc_mexico_chancery_tile_replace_60k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59774.85; date_signed 2012-08-09.",
)

# === Cycle 1082 (seed 20262082) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_brazil_metal_door_screen_51k_2023",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Brazil metal door screen for international embassies",
    "Brazil",
    "21 Feb 2023: Department of State awards contract 19AQMM23P0274 to Norshield Security Products, LLC for metal door screen etc. for international embassies (PoP Brazil); obligated USD 51,450. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "51450", "2023-02-21", "2023", "", "",
    "Metal door screen for international embassies, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_brazil_metal_door_screen_51k_2023",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0274_1900_-NONE-_-NONE-/",
    "Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1082",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23P0274_1900_-NONE-_-NONE- (Norshield Brazil metal door screen). Signed 2023-02-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0274_1900_-NONE-_-NONE-/.",
    "USASpending: Norshield Brazil metal door screen USD 0.051m. Supports norshield_brazil_metal_door_screen_51k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 51450; date_signed 2023-02-21.",
)

row_doc(
    "fabrication_designs_ecuador_metal_door_screen_59k_2025",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Ecuador metal door screen frame for international embassies",
    "Ecuador",
    "22 Sep 2025: Department of State awards contract 19AQMM25P0435 to Fabrication Designs, Inc. for metal door screen frame etc. for international embassies (PoP Ecuador); obligated USD 58,546.06. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "58546.06", "2025-09-22", "2025", "", "",
    "Metal door screen frame for international embassies, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_fabrication_designs_ecuador_metal_door_screen_59k_2025",
    "METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0435_1900_-NONE-_-NONE-/",
    "Actor: Fabrication Designs, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1082",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0435_1900_-NONE-_-NONE- (Fabrication Designs Ecuador metal door). Signed 2025-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0435_1900_-NONE-_-NONE-/.",
    "USASpending: Fabrication Designs Ecuador metal door USD 0.059m. Supports fabrication_designs_ecuador_metal_door_screen_59k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 58546.06; date_signed 2025-09-22.",
)

row_doc(
    "misc_brazil_dpo_renovation_60k_2019",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil diplomatic pouch office renovation",
    "Brazil",
    "30 Apr 2019: Department of State awards contract 19BR2519P0583 for renovation for the new DPO diplomatic pouch office (PoP Brazil); obligated USD 59,689.53. CapEx face = award obligation. Exact office unnamed — lat/lon blank.",
    "59689.53", "2019-04-30", "2019", "", "",
    "Renovation for the new diplomatic pouch office (DPO), Brazil (USASpending description; office not named — lat/lon blank).",
    "usaspending_misc_brazil_dpo_renovation_60k_2019",
    "RENOVATION FOR THE NEW DPO (DIPLOMATIC POUCH OFFICE)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0583_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1082",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2519P0583_1900_-NONE-_-NONE- (Brazil DPO renovation). Signed 2019-04-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2519P0583_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil DPO renovation USD 0.060m. Supports misc_brazil_dpo_renovation_60k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59689.53; date_signed 2019-04-30.",
)

row_doc(
    "misc_costa_rica_obc_vav_terminals_60k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Costa Rica OBC single duct VAV terminals installation",
    "Costa Rica",
    "28 Sep 2011: Department of State awards contract SCS80011C0027 for OBC single duct VAV terminals installation project (PoP Costa Rica); obligated USD 60,000. CapEx face = award obligation. Exact OBC site unnamed — lat/lon blank.",
    "60000", "2011-09-28", "2011", "", "",
    "OBC single duct VAV terminals installation project, Costa Rica (USASpending description; OBC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_obc_vav_terminals_60k_2011",
    "OBC SINGLE DUCT VAV TERMINALS INSTALLATION PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80011C0027_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1082",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80011C0027_1900_-NONE-_-NONE- (Costa Rica OBC VAV terminals). Signed 2011-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80011C0027_1900_-NONE-_-NONE-/.",
    "USASpending: Costa Rica OBC VAV terminals USD 0.060m. Supports misc_costa_rica_obc_vav_terminals_60k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60000; date_signed 2011-09-28.",
)

row_doc(
    "misc_bahamas_ship_ahoy_windows_doors_60k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas Ship Ahoy window and door replacement",
    "Bahamas",
    "30 Sep 2014: Department of State awards contract SBF50014M0884 for Ship Ahoy window and door replacement (PoP Bahamas); obligated USD 59,633.69. CapEx face = award obligation. Exact property unnamed — lat/lon blank.",
    "59633.69", "2014-09-30", "2014", "", "",
    "Ship Ahoy window and door replacement, Bahamas (USASpending description; property named, coords not stated — lat/lon blank).",
    "usaspending_misc_bahamas_ship_ahoy_windows_doors_60k_2014",
    "IGF::OT::IGF SHIP AHOY - WINDOW AND DOOR REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50014M0884_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1082",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50014M0884_1900_-NONE-_-NONE- (Bahamas Ship Ahoy windows/doors). Signed 2014-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50014M0884_1900_-NONE-_-NONE-/.",
    "USASpending: Bahamas Ship Ahoy windows/doors USD 0.060m. Supports misc_bahamas_ship_ahoy_windows_doors_60k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 59633.69; date_signed 2014-09-30.",
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
