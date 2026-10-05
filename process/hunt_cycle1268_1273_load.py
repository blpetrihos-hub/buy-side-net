#!/usr/bin/env python3
"""Cycles 1268–1273: USASpending LatAm CapEx (Hardline/Olgoonik/AECOM/Hollingsworth/Human Tech/Alutiiq + residual other).

Seeds: 20262268–20262273. Thin top-up dry. Security/shelters/A&E CapEx + Dominican/Mexico/Brazil/Venezuela make-ready.
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

# === Cycle 1268 ===
row_doc(
    "hardline_colombia_febr_replacement_2221k_2011",
    "infrastructure", "building_materials", "us",
    "CTS-Hardline — Colombia FE/BR product replacement",
    "Colombia",
    "11 Feb 2011: Department of State awards contract to CTS-HARDLINE, LLC for Phase III/IV forced entry/ballistic resistant (FE/BR) product replacement (PoP Colombia); obligated USD 2221565. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2221565", "2011-02-11", "2011", "", "",
    "PHASE III/IV FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND R&HR (REPAIR&HARDWARE REPLACEMEN, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hardline_colombia_febr_replacement_2221k_2011",
    "PHASE III/IV FORCED ENTRY/BALLISTIC RESISTANT (FE/BR) PRODUCT REPLACEMENT AND R&HR (REPAIR&HARDWARE REPLACEMENT) AT U.S. EMBASSY BOGOTA, COLOMBIA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0680_1900_SAQMMA07D0010_1900/",
    "Actor: CTS-HARDLINE, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1268",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F0680_1900_SAQMMA07D0010_1900 (hardline_colombia_febr_replacement_2221k_2011). Signed 2011-02-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F0680_1900_SAQMMA07D0010_1900/.",
    "USASpending: hardline_colombia_febr_replacement_2221k_2011 USD 2.222m. Supports hardline_colombia_febr_replacement_2221k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2221565.0; date_signed 2011-02-11.",
    investment_type="equipment_supply",
)

# === Cycle 1268 ===
row_doc(
    "olgoonik_panama_febr_avb_replacement_5644k_2025",
    "infrastructure", "building_materials", "us",
    "Olgoonik — Panama City embassy FEBR AVB product repair and replacement",
    "Panama",
    "23 Sep 2025: Department of State awards contract to OLGOONIK INNOVATIONS, LLC for FEBR AVB product repair and replacement at U.S. Embassy Panama City (PoP Panama); obligated USD 5644162. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "5644162", "2025-09-23", "2025", "", "",
    "FEBR AVB PRODUCT REPAIR AND REPLACEMENT AT U.S. EMBASSY PANAMA CITY, PANAMA., Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_olgoonik_panama_febr_avb_replacement_5644k_2025",
    "FEBR AVB PRODUCT REPAIR AND REPLACEMENT AT U.S. EMBASSY PANAMA CITY, PANAMA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F1208_1900_19AQMM25D0612_1900/",
    "Actor: OLGOONIK INNOVATIONS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1268",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25F1208_1900_19AQMM25D0612_1900 (olgoonik_panama_febr_avb_replacement_5644k_2025). Signed 2025-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F1208_1900_19AQMM25D0612_1900/.",
    "USASpending: olgoonik_panama_febr_avb_replacement_5644k_2025 USD 5.644m. Supports olgoonik_panama_febr_avb_replacement_5644k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5644162.0; date_signed 2025-09-23.",
    investment_type="equipment_supply",
)

# === Cycle 1268 ===
row_doc(
    "misc_dominican_mccarthy_make_ready_22k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican landlord make-ready McCarthy residence",
    "Dominican Republic",
    "2 Apr 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for landlord make-ready work McCarthy residence (PoP Dominican Republic); obligated USD 22371.99. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "22371.99", "2015-04-02", "2015", "", "",
    "LANDLORD MAKE READY WORK MCCARTHY RESIDENCE : IGF::CL::IGF FOR CLOSELY ASSOCIATED, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_mccarthy_make_ready_22k_2015",
    "LANDLORD MAKE READY WORK MCCARTHY RESIDENCE : IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1287_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1268",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86015M1287_1900_-NONE-_-NONE- (misc_dominican_mccarthy_make_ready_22k_2015). Signed 2015-04-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1287_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_mccarthy_make_ready_22k_2015 USD 0.022m. Supports misc_dominican_mccarthy_make_ready_22k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 22371.99; date_signed 2015-04-02.",
    investment_type="epc",
)

# === Cycle 1268 ===
row_doc(
    "misc_dominican_betts_make_ready_21k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican landlord make-ready Howard Betts",
    "Dominican Republic",
    "16 Jul 2013: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for landlord make-ready Howard Betts (PoP Dominican Republic); obligated USD 21884.40. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "21884.40", "2013-07-16", "2013", "", "",
    "LANDLORD MAKE READY HOWARD BETTS   IGF::CL::IGF FOR CLOSELY ASSOCIATED, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_betts_make_ready_21k_2013",
    "LANDLORD MAKE READY HOWARD BETTS   IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86013M1098_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1268",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86013M1098_1900_-NONE-_-NONE- (misc_dominican_betts_make_ready_21k_2013). Signed 2013-07-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86013M1098_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_betts_make_ready_21k_2013 USD 0.022m. Supports misc_dominican_betts_make_ready_21k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 21884.4; date_signed 2013-07-16.",
    investment_type="epc",
)

# === Cycle 1268 ===
row_doc(
    "misc_dominican_los_bambues18_make_ready_20k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Los Bambues 18 make-ready",
    "Dominican Republic",
    "4 Sep 2024: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for CBP make-ready work Los Bambues 18 PID 840 (PoP Dominican Republic); obligated USD 20804.34. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "20804.34", "2024-09-04", "2024", "", "",
    "CBP- MAKE READY WORK LOS BAMBUES 18 PID 840 - AWARD, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_los_bambues18_make_ready_20k_2024",
    "CBP- MAKE READY WORK LOS BAMBUES 18 PID 840 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0071_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1268",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0071_1900_-NONE-_-NONE- (misc_dominican_los_bambues18_make_ready_20k_2024). Signed 2024-09-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0071_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_los_bambues18_make_ready_20k_2024 USD 0.021m. Supports misc_dominican_los_bambues18_make_ready_20k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 20804.34; date_signed 2024-09-04.",
    investment_type="epc",
)

# === Cycle 1269 ===
row_doc(
    "aecom_honduras_soto_cano_fuel_farm_design_3554k_2022",
    "infrastructure", "engineering_epc", "us",
    "AECOM — Soto Cano AB fuel farm design",
    "Honduras",
    "14 Feb 2022: Department of Defense awards contract to AECOM SERVICES, LLC for base task 1/2/3 design of fuel farm Soto Cano AB (PoP Honduras); obligated USD 3554989.89. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3554989.89", "2022-02-14", "2022", "", "",
    "BASE TASK 1, 2 AND 3 DESIGN OF FUEL FARM, SOTO CANO AB, HONDURAS, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_aecom_honduras_soto_cano_fuel_farm_design_3554k_2022",
    "BASE TASK 1, 2 AND 3 DESIGN OF FUEL FARM, SOTO CANO AB, HONDURAS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0051_9700_W9127821D0013_9700/",
    "Actor: AECOM SERVICES, LLC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1269",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127822F0051_9700_W9127821D0013_9700 (aecom_honduras_soto_cano_fuel_farm_design_3554k_2022). Signed 2022-02-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127822F0051_9700_W9127821D0013_9700/.",
    "USASpending: aecom_honduras_soto_cano_fuel_farm_design_3554k_2022 USD 3.555m. Supports aecom_honduras_soto_cano_fuel_farm_design_3554k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3554989.89; date_signed 2022-02-14.",
    investment_type="epc",
)

# === Cycle 1269 ===
row_doc(
    "alutiiq_mexico_inl_checkpoint_equipment_3288k_2023",
    "infrastructure", "building_materials", "us",
    "Alutiiq — Mexico City INL checkpoint equipment for migration management",
    "Mexico",
    "9 May 2023: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for INL Mexico City equipment for checkpoints for migration management (PoP Mexico); obligated USD 3288963.73. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3288963.73", "2023-05-09", "2023", "", "",
    "BUREAU OF INL MEXICO CITY EQUIPMENT FOR CHECKPOINTS FOR MIGRATION MANAGEMENT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_inl_checkpoint_equipment_3288k_2023",
    "BUREAU OF INL MEXICO CITY EQUIPMENT FOR CHECKPOINTS FOR MIGRATION MANAGEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5006_1900_19AQMM20D0010_1900/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1269",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMR23F5006_1900_19AQMM20D0010_1900 (alutiiq_mexico_inl_checkpoint_equipment_3288k_2023). Signed 2023-05-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMR23F5006_1900_19AQMM20D0010_1900/.",
    "USASpending: alutiiq_mexico_inl_checkpoint_equipment_3288k_2023 USD 3.289m. Supports alutiiq_mexico_inl_checkpoint_equipment_3288k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3288963.73; date_signed 2023-05-09.",
    investment_type="equipment_supply",
)

# === Cycle 1269 ===
row_doc(
    "misc_brazil_ca_startup_make_ready_20k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil new CA positions startup make-ready",
    "Brazil",
    "27 Jun 2012: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for new CA positions start-up funds make-ready (PoP Brazil); obligated USD 20621.06. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "20621.06", "2012-06-27", "2012", "", "",
    "05 NEW CA POSITIONS START UP FUNDS - MAKE READY, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_ca_startup_make_ready_20k_2012",
    "05 NEW CA POSITIONS START UP FUNDS - MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25012M1309_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1269",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25012M1309_1900_-NONE-_-NONE- (misc_brazil_ca_startup_make_ready_20k_2012). Signed 2012-06-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25012M1309_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_ca_startup_make_ready_20k_2012 USD 0.021m. Supports misc_brazil_ca_startup_make_ready_20k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 20621.06; date_signed 2012-06-27.",
    investment_type="epc",
)

# === Cycle 1269 ===
row_doc(
    "misc_dominican_hatuey_make_ready_20k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Hatuey 94B make-ready",
    "Dominican Republic",
    "26 Jun 2024: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for ICASS make-ready work Hatuey 94B PID 701 (PoP Dominican Republic); obligated USD 20158.41. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "20158.41", "2024-06-26", "2024", "", "",
    "ICASS MAKE READY WORK HATUEY 94B PID 701 - AWARD, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_hatuey_make_ready_20k_2024",
    "ICASS MAKE READY WORK HATUEY 94B PID 701 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0045_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1269",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0045_1900_-NONE-_-NONE- (misc_dominican_hatuey_make_ready_20k_2024). Signed 2024-06-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0045_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_hatuey_make_ready_20k_2024 USD 0.020m. Supports misc_dominican_hatuey_make_ready_20k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 20158.41; date_signed 2024-06-26.",
    investment_type="epc",
)

# === Cycle 1269 ===
row_doc(
    "misc_dominican_lbb07_make_ready_20k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican LBB 07 make-ready",
    "Dominican Republic",
    "13 Jul 2022: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for consular make-ready LBB 07 PID 831 (PoP Dominican Republic); obligated USD 20083.32. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "20083.32", "2022-07-13", "2022", "", "",
    "CONS MAKE READY LBB 07 PID 831 - AWARD, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_lbb07_make_ready_20k_2022",
    "CONS MAKE READY LBB 07 PID 831 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622C0024_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1269",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8622C0024_1900_-NONE-_-NONE- (misc_dominican_lbb07_make_ready_20k_2022). Signed 2022-07-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622C0024_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_lbb07_make_ready_20k_2022 USD 0.020m. Supports misc_dominican_lbb07_make_ready_20k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 20083.32; date_signed 2022-07-13.",
    investment_type="epc",
)

# === Cycle 1270 ===
row_doc(
    "human_tech_colombia_rapid_shelters_2985k_2024",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Colombia rapid shelters",
    "Colombia",
    "13 Sep 2024: Department of State awards contract to HUMAN TECHNOLOGIES CORP for award of rapid shelters (PoP Colombia); obligated USD 2985177.37. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2985177.37", "2024-09-13", "2024", "", "",
    "AWARD OF RAPID SHELTERS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_colombia_rapid_shelters_2985k_2024",
    "AWARD OF RAPID SHELTERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0022_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1270",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24F0022_1900_19AQMM21D0007_1900 (human_tech_colombia_rapid_shelters_2985k_2024). Signed 2024-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0022_1900_19AQMM21D0007_1900/.",
    "USASpending: human_tech_colombia_rapid_shelters_2985k_2024 USD 2.985m. Supports human_tech_colombia_rapid_shelters_2985k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2985177.37; date_signed 2024-09-13.",
    investment_type="equipment_supply",
)

# === Cycle 1270 ===
row_doc(
    "human_tech_guatemala_eod_equipment_1964k_2024",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Guatemala EOD equipment",
    "Guatemala",
    "22 Apr 2024: Department of State awards contract to HUMAN TECHNOLOGIES CORP for EOD equipment (PoP Guatemala); obligated USD 1964813.68. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1964813.68", "2024-04-22", "2024", "", "",
    "EOD EQUIPMENT, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_guatemala_eod_equipment_1964k_2024",
    "EOD EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0020_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1270",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24F0020_1900_19AQMM21D0007_1900 (human_tech_guatemala_eod_equipment_1964k_2024). Signed 2024-04-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0020_1900_19AQMM21D0007_1900/.",
    "USASpending: human_tech_guatemala_eod_equipment_1964k_2024 USD 1.965m. Supports human_tech_guatemala_eod_equipment_1964k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1964813.68; date_signed 2024-04-22.",
    investment_type="equipment_supply",
)

# === Cycle 1270 ===
row_doc(
    "misc_dominican_los_bambues08_make_ready_19k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Los Bambues 08 make-ready",
    "Dominican Republic",
    "5 May 2022: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for consular make-ready work Los Bambues 08 PID 826 (PoP Dominican Republic); obligated USD 19679.21. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "19679.21", "2022-05-05", "2022", "", "",
    "CONS MAKE READY WORK LOS BAMBUES 08 PID 826 - AWARD, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_los_bambues08_make_ready_19k_2022",
    "CONS MAKE READY WORK LOS BAMBUES 08 PID 826 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622C0015_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1270",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8622C0015_1900_-NONE-_-NONE- (misc_dominican_los_bambues08_make_ready_19k_2022). Signed 2022-05-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622C0015_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_los_bambues08_make_ready_19k_2022 USD 0.020m. Supports misc_dominican_los_bambues08_make_ready_19k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19679.21; date_signed 2022-05-05.",
    investment_type="epc",
)

# === Cycle 1270 ===
row_doc(
    "misc_mexico_tres_canadas_make_ready_19k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Tres Cañadas III-15 make-ready",
    "Mexico",
    "6 Jul 2010: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for make-ready 2010 Tres Canadas III-15 (PoP Mexico); obligated USD 19298.65. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "19298.65", "2010-07-06", "2010", "", "",
    "MAKE READY 2010 TRES CANADAS III-15 MEX/OBO, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_tres_canadas_make_ready_19k_2010",
    "MAKE READY 2010 TRES CANADAS III-15 MEX/OBO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0555_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1270",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53010M0555_1900_-NONE-_-NONE- (misc_mexico_tres_canadas_make_ready_19k_2010). Signed 2010-07-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53010M0555_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_tres_canadas_make_ready_19k_2010 USD 0.019m. Supports misc_mexico_tres_canadas_make_ready_19k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19298.65; date_signed 2010-07-06.",
    investment_type="epc",
)

# === Cycle 1270 ===
row_doc(
    "misc_mexico_tarahumara_make_ready_18k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Sean Jones S. Tarahumara make-ready",
    "Mexico",
    "12 Mar 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC-USAID make-ready Sean Jones S. Tarahumara (PoP Mexico); obligated USD 18704.33. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "18704.33", "2015-03-12", "2015", "", "",
    "MEX/FAC-USAID/MAKE READY-SEAN JONES-S. TARAHUMARA 615/URGENT IGF::OT::IGF, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_tarahumara_make_ready_18k_2015",
    "MEX/FAC-USAID/MAKE READY-SEAN JONES-S. TARAHUMARA 615/URGENT IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015M0614_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1270",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53015M0614_1900_-NONE-_-NONE- (misc_mexico_tarahumara_make_ready_18k_2015). Signed 2015-03-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015M0614_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_tarahumara_make_ready_18k_2015 USD 0.019m. Supports misc_mexico_tarahumara_make_ready_18k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18704.33; date_signed 2015-03-12.",
    investment_type="epc",
)

# === Cycle 1271 ===
row_doc(
    "human_tech_colombia_mecad_rigid_shelters_1066k_2023",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Colombia MECAD camp rigid shelters",
    "Colombia",
    "27 Sep 2023: Department of State awards contract to HUMAN TECHNOLOGIES CORP for procurement of rigid shelters for Colombia MECAD camp (PoP Colombia); obligated USD 1066631. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1066631", "2023-09-27", "2023", "", "",
    "PROCUREMENT OF RIGID SHELTERS FOR COLOMBIA MECAD CAMP, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_colombia_mecad_rigid_shelters_1066k_2023",
    "PROCUREMENT OF RIGID SHELTERS FOR COLOMBIA MECAD CAMP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE23F0055_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1271",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE23F0055_1900_19AQMM21D0007_1900 (human_tech_colombia_mecad_rigid_shelters_1066k_2023). Signed 2023-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE23F0055_1900_19AQMM21D0007_1900/.",
    "USASpending: human_tech_colombia_mecad_rigid_shelters_1066k_2023 USD 1.067m. Supports human_tech_colombia_mecad_rigid_shelters_1066k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1066631.0; date_signed 2023-09-27.",
    investment_type="equipment_supply",
)

# === Cycle 1271 ===
row_doc(
    "hollingsworth_haiti_ae_design_425k_2013",
    "infrastructure", "engineering_epc", "us",
    "Hollingsworth-Pack — Haiti A&E design services",
    "Haiti",
    "12 Sep 2013: Department of State awards contract to HOLLINGSWORTH-PACK CORPORATION for A&E design services (PoP Haiti); obligated USD 425754.14. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "425754.14", "2013-09-12", "2013", "", "",
    "A&E DESIGN SERVICES IGF::OT::IGF, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hollingsworth_haiti_ae_design_425k_2013",
    "A&E DESIGN SERVICES IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50013F0304_1900_SGE50009D0006_1900/",
    "Actor: HOLLINGSWORTH-PACK CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1271",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGE50013F0304_1900_SGE50009D0006_1900 (hollingsworth_haiti_ae_design_425k_2013). Signed 2013-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50013F0304_1900_SGE50009D0006_1900/.",
    "USASpending: hollingsworth_haiti_ae_design_425k_2013 USD 0.426m. Supports hollingsworth_haiti_ae_design_425k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 425754.14; date_signed 2013-09-12.",
    investment_type="epc",
)

# === Cycle 1271 ===
row_doc(
    "misc_mexico_la_gavia8_make_ready_18k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico La Gavia 8 make-ready",
    "Mexico",
    "15 Feb 2012: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC 7901 La Gavia 8 make-ready (PoP Mexico); obligated USD 18421.33. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "18421.33", "2012-02-15", "2012", "", "",
    "MX-FAC 7901 LA GAVIA 8 MAKE READY, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_la_gavia8_make_ready_18k_2012",
    "MX-FAC 7901 LA GAVIA 8 MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012L0014_1900_SMX53012A0011_1900/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1271",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53012L0014_1900_SMX53012A0011_1900 (misc_mexico_la_gavia8_make_ready_18k_2012). Signed 2012-02-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012L0014_1900_SMX53012A0011_1900/.",
    "USASpending: misc_mexico_la_gavia8_make_ready_18k_2012 USD 0.018m. Supports misc_mexico_la_gavia8_make_ready_18k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18421.33; date_signed 2012-02-15.",
    investment_type="epc",
)

# === Cycle 1271 ===
row_doc(
    "misc_dominican_las_violetas_make_ready_18k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Las Violetas 1-7 make-ready",
    "Dominican Republic",
    "1 Aug 2024: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for consular make-ready work Las Violetas 1-7 PID 699 (PoP Dominican Republic); obligated USD 18232.11. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "18232.11", "2024-08-01", "2024", "", "",
    "CONS- MAKE READY WORK LAS VIOLETAS 1-7 PID 699 - AWARD, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_las_violetas_make_ready_18k_2024",
    "CONS- MAKE READY WORK LAS VIOLETAS 1-7 PID 699 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0065_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1271",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0065_1900_-NONE-_-NONE- (misc_dominican_las_violetas_make_ready_18k_2024). Signed 2024-08-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0065_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_las_violetas_make_ready_18k_2024 USD 0.018m. Supports misc_dominican_las_violetas_make_ready_18k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18232.11; date_signed 2024-08-01.",
    investment_type="epc",
)

# === Cycle 1271 ===
row_doc(
    "misc_venezuela_bosque_de_oro_make_ready_18k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Venezuela Bosque de Oro 4-A make-ready",
    "Venezuela",
    "29 Aug 2011: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for Bosque de Oro 4-A make-ready (PoP Venezuela); obligated USD 18204.11. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "18204.11", "2011-08-29", "2011", "", "",
    "BOSQUE DE ORO 4-A MAKE READY, Venezuela (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_venezuela_bosque_de_oro_make_ready_18k_2011",
    "BOSQUE DE ORO 4-A MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30011M0701_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1271",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30011M0701_1900_-NONE-_-NONE- (misc_venezuela_bosque_de_oro_make_ready_18k_2011). Signed 2011-08-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30011M0701_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_bosque_de_oro_make_ready_18k_2011 USD 0.018m. Supports misc_venezuela_bosque_de_oro_make_ready_18k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18204.11; date_signed 2011-08-29.",
    investment_type="epc",
)

# === Cycle 1272 ===
row_doc(
    "hollingsworth_brazil_brasilia_nec_ae_198k_2024",
    "infrastructure", "engineering_epc", "us",
    "Hollingsworth-Pack — Brasilia NEC A&E services",
    "Brazil",
    "29 Aug 2024: Department of State awards contract to HOLLINGSWORTH-PACK CORPORATION for A&E services for the NEC in Brasilia (PoP Brazil); obligated USD 198000. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "198000", "2024-08-29", "2024", "", "",
    "A&E SERVICES FOR THE NEC IN BRASILIA, BRAZIL, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hollingsworth_brazil_brasilia_nec_ae_198k_2024",
    "A&E SERVICES FOR THE NEC IN BRASILIA, BRAZIL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024P0066_1900_-NONE-_-NONE-/",
    "Actor: HOLLINGSWORTH-PACK CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1272",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5024P0066_1900_-NONE-_-NONE- (hollingsworth_brazil_brasilia_nec_ae_198k_2024). Signed 2024-08-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5024P0066_1900_-NONE-_-NONE-/.",
    "USASpending: hollingsworth_brazil_brasilia_nec_ae_198k_2024 USD 0.198m. Supports hollingsworth_brazil_brasilia_nec_ae_198k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 198000.0; date_signed 2024-08-29.",
    investment_type="epc",
)

# === Cycle 1272 ===
row_doc(
    "hollingsworth_haiti_police_stations_ae_178k_2013",
    "infrastructure", "engineering_epc", "us",
    "Hollingsworth-Pack — Haiti three police stations A&E design",
    "Haiti",
    "6 Feb 2013: Department of State awards contract to HOLLINGSWORTH-PACK CORPORATION for A&E and design services for 3 police stations in Haiti (PoP Haiti); obligated USD 178097.33. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "178097.33", "2013-02-06", "2013", "", "",
    "A&E AND DESIGN SERVICES FOR 3 POLICE STATIONS IN HAITI. IGF::OT::IGF, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hollingsworth_haiti_police_stations_ae_178k_2013",
    "A&E AND DESIGN SERVICES FOR 3 POLICE STATIONS IN HAITI. IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50013F0088_1900_SGE50009D0006_1900/",
    "Actor: HOLLINGSWORTH-PACK CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1272",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGE50013F0088_1900_SGE50009D0006_1900 (hollingsworth_haiti_police_stations_ae_178k_2013). Signed 2013-02-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50013F0088_1900_SGE50009D0006_1900/.",
    "USASpending: hollingsworth_haiti_police_stations_ae_178k_2013 USD 0.178m. Supports hollingsworth_haiti_police_stations_ae_178k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 178097.33; date_signed 2013-02-06.",
    investment_type="epc",
)

# === Cycle 1272 ===
row_doc(
    "misc_dominican_lbb04_ex_towers_make_ready_20k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican LBB-04 Ex-Towers make-ready",
    "Dominican Republic",
    "16 Jun 2023: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for USAID maintenance/repairs/make-ready LBB-04 Ex-Towers (PoP Dominican Republic); obligated USD 20853.77. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "20853.77", "2023-06-16", "2023", "", "",
    "USAID M., REP. & M. READY LBB-04 MAKE READY EX-TOWERS, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_lbb04_ex_towers_make_ready_20k_2023",
    "USAID M., REP. & M. READY LBB-04 MAKE READY EX-TOWERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0019_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1272",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8623C0019_1900_-NONE-_-NONE- (misc_dominican_lbb04_ex_towers_make_ready_20k_2023). Signed 2023-06-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0019_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_lbb04_ex_towers_make_ready_20k_2023 USD 0.021m. Supports misc_dominican_lbb04_ex_towers_make_ready_20k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 20853.77; date_signed 2023-06-16.",
    investment_type="epc",
)

# === Cycle 1272 ===
row_doc(
    "misc_dominican_landlord_make_ready_19k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican closely associated landlord make-ready",
    "Dominican Republic",
    "9 Jul 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for closely associated landlord make-ready (PoP Dominican Republic); obligated USD 19695.31. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "19695.31", "2015-07-09", "2015", "", "",
    "IGF::CL::IGF FOR CLOSELY ASSOCIATED LANDLORD MAKE READY WORK RONALD SAVAGE RESIDENCE, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_landlord_make_ready_19k_2015",
    "IGF::CL::IGF FOR CLOSELY ASSOCIATED LANDLORD MAKE READY WORK RONALD SAVAGE RESIDENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1608_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1272",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86015M1608_1900_-NONE-_-NONE- (misc_dominican_landlord_make_ready_19k_2015). Signed 2015-07-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M1608_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_landlord_make_ready_19k_2015 USD 0.020m. Supports misc_dominican_landlord_make_ready_19k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19695.31; date_signed 2015-07-09.",
    investment_type="epc",
)

# === Cycle 1272 ===
row_doc(
    "misc_dominican_lbb11_make_ready_19k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican LBB11 make-ready",
    "Dominican Republic",
    "18 Jul 2023: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for program maintenance repairs & make-ready LBB11 PID 839 (PoP Dominican Republic); obligated USD 19578.39. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "19578.39", "2023-07-18", "2023", "", "",
    "PROG MAINTENANCE REPAIRS & MAKE READY LBB11 PID 834 - AWARD, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_lbb11_make_ready_19k_2023",
    "PROG MAINTENANCE REPAIRS & MAKE READY LBB11 PID 834 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0026_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1272",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8623C0026_1900_-NONE-_-NONE- (misc_dominican_lbb11_make_ready_19k_2023). Signed 2023-07-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0026_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_lbb11_make_ready_19k_2023 USD 0.020m. Supports misc_dominican_lbb11_make_ready_19k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19578.39; date_signed 2023-07-18.",
    investment_type="epc",
)

# === Cycle 1273 ===
row_doc(
    "olgoonik_mexico_nuevo_laredo_febr_windows_226k_2023",
    "infrastructure", "building_materials", "us",
    "Olgoonik — Nuevo Laredo consulate FEBR windows",
    "Mexico",
    "30 Sep 2023: Department of State awards contract to OLGOONIK FEDERAL, LLC for FEBR windows for consulate in Nuevo Laredo (PoP Mexico); obligated USD 226308. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "226308", "2023-09-30", "2023", "", "",
    "FEBR WINDOWS FOR CONSULATE IN NUEVO LAREDO, MEXICO, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_olgoonik_mexico_nuevo_laredo_febr_windows_226k_2023",
    "FEBR WINDOWS FOR CONSULATE IN NUEVO LAREDO, MEXICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0956_1900_19AQMM20D0006_1900/",
    "Actor: OLGOONIK FEDERAL, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1273",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F0956_1900_19AQMM20D0006_1900 (olgoonik_mexico_nuevo_laredo_febr_windows_226k_2023). Signed 2023-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0956_1900_19AQMM20D0006_1900/.",
    "USASpending: olgoonik_mexico_nuevo_laredo_febr_windows_226k_2023 USD 0.226m. Supports olgoonik_mexico_nuevo_laredo_febr_windows_226k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 226308.0; date_signed 2023-09-30.",
    investment_type="equipment_supply",
)

# === Cycle 1273 ===
row_doc(
    "hollingsworth_bahamas_nassau_police_college_ae_124k_2019",
    "infrastructure", "engineering_epc", "us",
    "Hollingsworth-Pack — Nassau Police College A&E",
    "Bahamas",
    "14 Dec 2018: Department of State awards contract to HOLLINGSWORTH-PACK CORPORATION for Nassau Police College A&E (PoP Bahamas); obligated USD 124746.45. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "124746.45", "2018-12-14", "2018", "", "",
    "NASSAU POLICE COLLEGE A&E, Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hollingsworth_bahamas_nassau_police_college_ae_124k_2019",
    "NASSAU POLICE COLLEGE A&E",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0006_1900_-NONE-_-NONE-/",
    "Actor: HOLLINGSWORTH-PACK CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1273",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0006_1900_-NONE-_-NONE- (hollingsworth_bahamas_nassau_police_college_ae_124k_2019). Signed 2018-12-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0006_1900_-NONE-_-NONE-/.",
    "USASpending: hollingsworth_bahamas_nassau_police_college_ae_124k_2019 USD 0.125m. Supports hollingsworth_bahamas_nassau_police_college_ae_124k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 124746.45; date_signed 2018-12-14.",
    investment_type="epc",
)

# === Cycle 1273 ===
row_doc(
    "misc_dominican_lbb03_make_ready_22k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican CDC LBB 03 make-ready",
    "Dominican Republic",
    "20 Jun 2023: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for CDC maintenance repairs & make-ready LBB 03 PID 855 (PoP Dominican Republic); obligated USD 22300.44. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "22300.44", "2023-06-20", "2023", "", "",
    "CDC MAINTENANCE REPAIRS & MAKE READY LBB 03 PID 855 - AWARD, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_lbb03_make_ready_22k_2023",
    "CDC MAINTENANCE REPAIRS & MAKE READY LBB 03 PID 855 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0017_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1273",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8623C0017_1900_-NONE-_-NONE- (misc_dominican_lbb03_make_ready_22k_2023). Signed 2023-06-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0017_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_lbb03_make_ready_22k_2023 USD 0.022m. Supports misc_dominican_lbb03_make_ready_22k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 22300.44; date_signed 2023-06-20.",
    investment_type="epc",
)

# === Cycle 1273 ===
row_doc(
    "misc_dominican_fpd_pid42_make_ready_21k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican FPD PID 42 make-ready",
    "Dominican Republic",
    "18 Jul 2023: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FPD maintenance repairs and make-ready work 42 PID (PoP Dominican Republic); obligated USD 21210.52. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "21210.52", "2023-07-18", "2023", "", "",
    "FPD MAINTENANCE REPAIRS AND MAKE READY WORK 42 PID - AWARD, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_fpd_pid42_make_ready_21k_2023",
    "FPD MAINTENANCE REPAIRS AND MAKE READY WORK 42 PID - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0029_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1273",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8623C0029_1900_-NONE-_-NONE- (misc_dominican_fpd_pid42_make_ready_21k_2023). Signed 2023-07-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0029_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_fpd_pid42_make_ready_21k_2023 USD 0.021m. Supports misc_dominican_fpd_pid42_make_ready_21k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 21210.52; date_signed 2023-07-18.",
    investment_type="epc",
)

# === Cycle 1273 ===
row_doc(
    "misc_dominican_lbb24_make_ready_20k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican LBB-24 make-ready",
    "Dominican Republic",
    "29 Jun 2023: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for consular maintenance repairs & make-ready LBB-24 PID 848 (PoP Dominican Republic); obligated USD 20049.72. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "20049.72", "2023-06-29", "2023", "", "",
    "CONS MAINT, REPAIRS & MAKE READY LBB-24 PID 848 - AWARD, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_lbb24_make_ready_20k_2023",
    "CONS MAINT, REPAIRS & MAKE READY LBB-24 PID 848 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0021_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1273",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8623C0021_1900_-NONE-_-NONE- (misc_dominican_lbb24_make_ready_20k_2023). Signed 2023-06-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8623C0021_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_lbb24_make_ready_20k_2023 USD 0.020m. Supports misc_dominican_lbb24_make_ready_20k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 20049.72; date_signed 2023-06-29.",
    investment_type="epc",
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
        w.writeheader(); w.writerows(rows)
    EVID.mkdir(parents=True, exist_ok=True)
    for row, ev, _bib in ITEMS:
        (EVID / f"{row['id']}.json").write_text(json.dumps(ev, indent=2) + "\n", encoding="utf-8")
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
            bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")

if __name__ == "__main__":
    main()
