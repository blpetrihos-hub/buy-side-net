#!/usr/bin/env python3
"""Cycles 1198–1203: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262198–20262203. Thin top-up dry.
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

# === Cycle 1198 ===
row_doc(
    "hdr_honduras_barracks_811k_2011",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — Honduras barracks",
    "Honduras",
    "19 Apr 2010: Department of Defense awards contract 0008 to HDR ENGINEERING INC for Barracks CapEx delivery order (PoP Honduras); obligated USD 810501. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "810501", "2010-04-19", "2010", "", "",
    "Barracks CapEx delivery order, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_hdr_honduras_barracks_811k_2011",
    "BARRACKS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127810D0022_9700/",
    "Actor: HDR ENGINEERING INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1198",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0008_9700_W9127810D0022_9700 (hdr_honduras_barracks_811k_2011). Signed 2010-04-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0008_9700_W9127810D0022_9700/.",
    "USASpending: hdr_honduras_barracks_811k_2011 USD 0.811m. Supports hdr_honduras_barracks_811k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 810501.0; date_signed 2010-04-19.",
)

# === Cycle 1198 ===
row_doc(
    "hdr_panama_design_build_641k_2011",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — Panama design/build",
    "Panama",
    "22 Apr 2010: Department of Defense awards contract 0006 to HDR ENGINEERING INC for Design/build CapEx delivery order (PoP Panama); obligated USD 640962. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "640962", "2010-04-22", "2010", "", "",
    "Design/build CapEx delivery order, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_hdr_panama_design_build_641k_2011",
    "DESIGN/BUILD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127810D0022_9700/",
    "Actor: HDR ENGINEERING INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1198",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0006_9700_W9127810D0022_9700 (hdr_panama_design_build_641k_2011). Signed 2010-04-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W9127810D0022_9700/.",
    "USASpending: hdr_panama_design_build_641k_2011 USD 0.641m. Supports hdr_panama_design_build_641k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 640962.0; date_signed 2010-04-22.",
)

# === Cycle 1198 ===
row_doc(
    "misc_dominican_chancery_roof_waterproofing_13k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic OBO waterproofing chancery roof",
    "Dominican Republic",
    "11 Sep 2011: Department of State awards contract SDR86011M1556 for OBO waterproofing chancery roof (PoP Dominican Republic); obligated USD 13424.23. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13424.23", "2011-09-11", "2011", "", "",
    "OBO waterproofing chancery roof, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_dominican_chancery_roof_waterproofing_13k_2011",
    "OBO - WATERPROOFING CHANCERY ROOF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011M1556_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1198",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86011M1556_1900_-NONE-_-NONE- (misc_dominican_chancery_roof_waterproofing_13k_2011). Signed 2011-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011M1556_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_chancery_roof_waterproofing_13k_2011 USD 0.013m. Supports misc_dominican_chancery_roof_waterproofing_13k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13424.23; date_signed 2011-09-11.",
)

# === Cycle 1198 ===
row_doc(
    "misc_jamaica_powell_plaza_security_cameras_upgrade_13k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Jamaica RSO Powell Plaza security cameras upgrade",
    "Jamaica",
    "19 Aug 2010: Department of State awards contract SJM37010M0980 for RSO Powell Plaza security cameras upgrade (PoP Jamaica); obligated USD 13423.22. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13423.22", "2010-08-19", "2010", "", "",
    "RSO Powell Plaza security cameras upgrade, Jamaica (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_jamaica_powell_plaza_security_cameras_upgrade_13k_2010",
    "RSO - POWELL PLAZA SECURITY CAMERAS UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37010M0980_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1198",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37010M0980_1900_-NONE-_-NONE- (misc_jamaica_powell_plaza_security_cameras_upgrade_13k_2010). Signed 2010-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37010M0980_1900_-NONE-_-NONE-/.",
    "USASpending: misc_jamaica_powell_plaza_security_cameras_upgrade_13k_2010 USD 0.013m. Supports misc_jamaica_powell_plaza_security_cameras_upgrade_13k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13423.22; date_signed 2010-08-19.",
)

# === Cycle 1198 ===
row_doc(
    "misc_panama_corozal_cctv_cameras_install_13k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Panama ODC installment of CCTV cameras in Corozal",
    "Panama",
    "19 Aug 2015: Department of State awards contract SPM07015M0802 for ODC installment of CCTV cameras in Corozal (PoP Panama); obligated USD 13414.95. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13414.95", "2015-08-19", "2015", "", "",
    "ODC installment of CCTV cameras in Corozal, Panama (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_panama_corozal_cctv_cameras_install_13k_2015",
    "ODC-INSTALLMENT OF CCTV CAMERAS IN COROZAL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07015M0802_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1198",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07015M0802_1900_-NONE-_-NONE- (misc_panama_corozal_cctv_cameras_install_13k_2015). Signed 2015-08-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07015M0802_1900_-NONE-_-NONE-/.",
    "USASpending: misc_panama_corozal_cctv_cameras_install_13k_2015 USD 0.013m. Supports misc_panama_corozal_cctv_cameras_install_13k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13414.95; date_signed 2015-08-19.",
)

# === Cycle 1199 ===
row_doc(
    "hdr_belize_san_pedro_cn_ops_center_design_371k_2012",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — Belize A/E design CN ops center San Pedro",
    "Belize",
    "29 Nov 2010: Department of Defense awards contract 0016 to HDR ENGINEERING INC for A/E design CN ops center, San Pedro, Belize (PoP Belize); obligated USD 371277. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "371277", "2010-11-29", "2010", "", "",
    "A/E design CN ops center, San Pedro, Belize, Belize (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_hdr_belize_san_pedro_cn_ops_center_design_371k_2012",
    "TAS::21 2020::TAS A/E DESIGN CN OPS CENTER, SAN PEDRO, BELIZE, DESIGN CT FACILITIES, BELIZE, AND DESIGN CN JOINT OP CENTER, PRICE BARRACKS, BELIZE, DESIGN CN OPS CENTER, HUNTING CAY, BELIZE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0016_9700_W9127810D0022_9700/",
    "Actor: HDR ENGINEERING INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1199",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0016_9700_W9127810D0022_9700 (hdr_belize_san_pedro_cn_ops_center_design_371k_2012). Signed 2010-11-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0016_9700_W9127810D0022_9700/.",
    "USASpending: hdr_belize_san_pedro_cn_ops_center_design_371k_2012 USD 0.371m. Supports hdr_belize_san_pedro_cn_ops_center_design_371k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 371277.0; date_signed 2010-11-29.",
)

# === Cycle 1199 ===
row_doc(
    "hdr_guatemala_southcom_cn_projects_256k_2012",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — Guatemala SOUTHCOM CN projects",
    "Guatemala",
    "30 Jan 2012: Department of Defense awards contract 0031 to HDR ENGINEERING INC for SOUTHCOM CN projects (PoP Guatemala); obligated USD 255989. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "255989", "2012-01-30", "2012", "", "",
    "SOUTHCOM CN projects, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_hdr_guatemala_southcom_cn_projects_256k_2012",
    "SOUTHCOM CN PROJECTS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0031_9700_W9127810D0022_9700/",
    "Actor: HDR ENGINEERING INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1199",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0031_9700_W9127810D0022_9700 (hdr_guatemala_southcom_cn_projects_256k_2012). Signed 2012-01-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0031_9700_W9127810D0022_9700/.",
    "USASpending: hdr_guatemala_southcom_cn_projects_256k_2012 USD 0.256m. Supports hdr_guatemala_southcom_cn_projects_256k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 255989.0; date_signed 2012-01-30.",
)

# === Cycle 1199 ===
row_doc(
    "misc_mexico_cdj_2nd_floor_renovation_13k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico OBO CDJ-MGT consolidation 2nd floor renovation",
    "Mexico",
    "29 Sep 2016: Department of State awards contract SMX11516M0444 for OBO CDJ-MGT consolidation project/2nd floor renovation (PoP Mexico); obligated USD 13370.61. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13370.61", "2016-09-29", "2016", "", "",
    "OBO CDJ-MGT consolidation project/2nd floor renovation, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_cdj_2nd_floor_renovation_13k_2016",
    "OBO CDJ-MGT CONSOLIDATION PROJECT/2ND FLOOR RENOVATION P1001 ''IGF::OT::IGF''",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516M0444_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1199",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11516M0444_1900_-NONE-_-NONE- (misc_mexico_cdj_2nd_floor_renovation_13k_2016). Signed 2016-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516M0444_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_cdj_2nd_floor_renovation_13k_2016 USD 0.013m. Supports misc_mexico_cdj_2nd_floor_renovation_13k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13370.61; date_signed 2016-09-29.",
)

# === Cycle 1199 ===
row_doc(
    "misc_mexico_nvl_enclose_generator_annex_13k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico NVL/OBO enclose generator at annex cons building",
    "Mexico",
    "8 Sep 2010: Department of State awards contract SMX61010M0084 for NVL/OBO enclose generator at annex cons building (PoP Mexico); obligated USD 13363.79. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13363.79", "2010-09-08", "2010", "", "",
    "NVL/OBO enclose generator at annex cons building, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_nvl_enclose_generator_annex_13k_2010",
    "NVL/OBO/ENCLOSE GENERATOR AT ANNEX CONS BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX61010M0084_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1199",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX61010M0084_1900_-NONE-_-NONE- (misc_mexico_nvl_enclose_generator_annex_13k_2010). Signed 2010-09-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX61010M0084_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_nvl_enclose_generator_annex_13k_2010 USD 0.013m. Supports misc_mexico_nvl_enclose_generator_annex_13k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13363.79; date_signed 2010-09-08.",
)

# === Cycle 1199 ===
row_doc(
    "misc_mexico_nogales_security_grills_new_residences_13k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico DS security grills for new residences Nogales",
    "Mexico",
    "27 Jun 2011: Department of State awards contract SMX60011M0075 for DS security grills for new residences — Nogales (PoP Mexico); obligated USD 13360.94. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13360.94", "2011-06-27", "2011", "", "",
    "DS security grills for new residences — Nogales, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_nogales_security_grills_new_residences_13k_2011",
    "DS - SECURITY GRILLS FOR NEW RESIDENCES - NOGALES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX60011M0075_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1199",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX60011M0075_1900_-NONE-_-NONE- (misc_mexico_nogales_security_grills_new_residences_13k_2011). Signed 2011-06-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX60011M0075_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_nogales_security_grills_new_residences_13k_2011 USD 0.013m. Supports misc_mexico_nogales_security_grills_new_residences_13k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13360.94; date_signed 2011-06-27.",
)

# === Cycle 1200 ===
row_doc(
    "hdr_nicaragua_southcom_cn_fy12_231k_2012",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — Nicaragua FY12 SOUTHCOM CN",
    "Nicaragua",
    "12 Jul 2012: Department of Defense awards contract 0039 to HDR ENGINEERING INC for FY12 SOUTHCOM CN (PoP Nicaragua); obligated USD 230568. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "230568", "2012-07-12", "2012", "", "",
    "FY12 SOUTHCOM CN, Nicaragua (USASpending description; site not named — lat/lon blank).",
    "usaspending_hdr_nicaragua_southcom_cn_fy12_231k_2012",
    "TAS::21 2050::TAS FY12 SOUTHCOM CN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0039_9700_W9127810D0022_9700/",
    "Actor: HDR ENGINEERING INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1200",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0039_9700_W9127810D0022_9700 (hdr_nicaragua_southcom_cn_fy12_231k_2012). Signed 2012-07-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0039_9700_W9127810D0022_9700/.",
    "USASpending: hdr_nicaragua_southcom_cn_fy12_231k_2012 USD 0.231m. Supports hdr_nicaragua_southcom_cn_fy12_231k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 230568.0; date_signed 2012-07-12.",
)

# === Cycle 1200 ===
row_doc(
    "hdr_costa_rica_southcom_cn_infrastructure_225k_2012",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — Costa Rica HQ SOUTHCOM counter-narcotics infrastructure",
    "Costa Rica",
    "21 Sep 2011: Department of Defense awards contract 0029 to HDR ENGINEERING INC for HQ SOUTHCOM counter-narcotics infrastructure (PoP Costa Rica); obligated USD 225008. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "225008", "2011-09-21", "2011", "", "",
    "HQ SOUTHCOM counter-narcotics infrastructure, Costa Rica (USASpending description; site not named — lat/lon blank).",
    "usaspending_hdr_costa_rica_southcom_cn_infrastructure_225k_2012",
    "TAS::21 2020::TAS HQ SOUTHCOM COUNTER-NARCOTICS INFRASTRUCTURE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0029_9700_W9127810D0022_9700/",
    "Actor: HDR ENGINEERING INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1200",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0029_9700_W9127810D0022_9700 (hdr_costa_rica_southcom_cn_infrastructure_225k_2012). Signed 2011-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0029_9700_W9127810D0022_9700/.",
    "USASpending: hdr_costa_rica_southcom_cn_infrastructure_225k_2012 USD 0.225m. Supports hdr_costa_rica_southcom_cn_infrastructure_225k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 225008.0; date_signed 2011-09-21.",
)

# === Cycle 1200 ===
row_doc(
    "misc_bahamas_msgr_generator_exhaust_stack_replace_13k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Bahamas MSGR generator exhaust stack replacement",
    "Bahamas",
    "5 Sep 2016: Department of State awards contract SBF50016M0829 for MSGR generator exhaust stack replacement (PoP Bahamas); obligated USD 13357.05. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13357.05", "2016-09-05", "2016", "", "",
    "MSGR generator exhaust stack replacement, Bahamas (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_bahamas_msgr_generator_exhaust_stack_replace_13k_2016",
    "IGF::OT::IGF MSGR - GENERATOR EXHAUST STACK REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50016M0829_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1200",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50016M0829_1900_-NONE-_-NONE- (misc_bahamas_msgr_generator_exhaust_stack_replace_13k_2016). Signed 2016-09-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50016M0829_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_msgr_generator_exhaust_stack_replace_13k_2016 USD 0.013m. Supports misc_bahamas_msgr_generator_exhaust_stack_replace_13k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13357.05; date_signed 2016-09-05.",
)

# === Cycle 1200 ===
row_doc(
    "misc_brazil_fence_upgrade_13k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil fence upgrade",
    "Brazil",
    "14 Sep 2022: Department of State awards contract 19BR2522P1715 for Fence upgrade (PoP Brazil); obligated USD 13348.05. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13348.05", "2022-09-14", "2022", "", "",
    "Fence upgrade, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_fence_upgrade_13k_2022",
    "FENCE UPGRADE -",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2522P1715_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1200",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2522P1715_1900_-NONE-_-NONE- (misc_brazil_fence_upgrade_13k_2022). Signed 2022-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2522P1715_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_fence_upgrade_13k_2022 USD 0.013m. Supports misc_brazil_fence_upgrade_13k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13348.05; date_signed 2022-09-14.",
)

# === Cycle 1200 ===
row_doc(
    "misc_paraguay_cmr_handicap_bathroom_renovation_13k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Paraguay FAC renovation new handicap accessible bathroom CMR",
    "Paraguay",
    "21 Sep 2023: Department of State awards contract 19PA1023P0488 for FAC renovation — new handicap accessible bathroom CMR (PoP Paraguay); obligated USD 13319.58. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13319.58", "2023-09-21", "2023", "", "",
    "FAC renovation — new handicap accessible bathroom CMR, Paraguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_paraguay_cmr_handicap_bathroom_renovation_13k_2023",
    "SOLUMAX FAC-7902 - RENOVATION - NEW HANDICAP ACCESSIBLE BATHROOM CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1023P0488_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1200",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PA1023P0488_1900_-NONE-_-NONE- (misc_paraguay_cmr_handicap_bathroom_renovation_13k_2023). Signed 2023-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1023P0488_1900_-NONE-_-NONE-/.",
    "USASpending: misc_paraguay_cmr_handicap_bathroom_renovation_13k_2023 USD 0.013m. Supports misc_paraguay_cmr_handicap_bathroom_renovation_13k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13319.58; date_signed 2023-09-21.",
)

# === Cycle 1201 ===
row_doc(
    "johnson_controls_mexico_tij_msgr_fabrication_194k_2018",
    "infrastructure", "building_materials", "us",
    "Johnson Controls — Mexico continued fabrication for TIJ MSGR",
    "Mexico",
    "25 May 2018: Department of State awards contract 19AQMM18P1094 to JOHNSON CONTROLS INC for Continued fabrication by Johnson Controls for the TIJ MSGR (PoP Mexico); obligated USD 194055. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "194055", "2018-05-25", "2018", "", "",
    "Continued fabrication by Johnson Controls for the TIJ MSGR, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_johnson_controls_mexico_tij_msgr_fabrication_194k_2018",
    "CONTINUED FABRICATION BY JOHNSON CONTROLS FOR THE TIJ MSGR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P1094_1900_-NONE-_-NONE-/",
    "Actor: JOHNSON CONTROLS INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1201",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18P1094_1900_-NONE-_-NONE- (johnson_controls_mexico_tij_msgr_fabrication_194k_2018). Signed 2018-05-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P1094_1900_-NONE-_-NONE-/.",
    "USASpending: johnson_controls_mexico_tij_msgr_fabrication_194k_2018 USD 0.194m. Supports johnson_controls_mexico_tij_msgr_fabrication_194k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 194055.0; date_signed 2018-05-25.",
)

# === Cycle 1201 ===
row_doc(
    "hdr_honduras_soto_cano_barracks_design_188k_2011",
    "infrastructure", "engineering_epc", "us",
    "HDR Engineering — Honduras design FY-11 barracks for Soto Cano",
    "Honduras",
    "25 Feb 2011: Department of Defense awards contract 0022 to HDR ENGINEERING INC for Design FY-11 barracks for Soto Cano (PoP Honduras); obligated USD 188079. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "188079", "2011-02-25", "2011", "", "",
    "Design FY-11 barracks for Soto Cano, Honduras (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_hdr_honduras_soto_cano_barracks_design_188k_2011",
    "TAS::21 2050::TAS DESIGN FY-11 BARRACKS FOR SOTO CANO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0022_9700_W9127810D0022_9700/",
    "Actor: HDR ENGINEERING INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1201",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0022_9700_W9127810D0022_9700 (hdr_honduras_soto_cano_barracks_design_188k_2011). Signed 2011-02-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0022_9700_W9127810D0022_9700/.",
    "USASpending: hdr_honduras_soto_cano_barracks_design_188k_2011 USD 0.188m. Supports hdr_honduras_soto_cano_barracks_design_188k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 188079.0; date_signed 2011-02-25.",
)

# === Cycle 1201 ===
row_doc(
    "misc_dominican_make_ready_los_bambues_48_13k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic APHIS make-ready Los Bambues 48",
    "Dominican Republic",
    "27 Jun 2024: Department of State awards contract 19DR8624C0040 for APHIS make-ready work Los Bambues 48 PID 821 (PoP Dominican Republic); obligated USD 13319.50. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13319.50", "2024-06-27", "2024", "", "",
    "APHIS make-ready work Los Bambues 48 PID 821, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_make_ready_los_bambues_48_13k_2024",
    "APHIS- MAKE READY WORK LOS BAMBUES 48 PID 821 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0040_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1201",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0040_1900_-NONE-_-NONE- (misc_dominican_make_ready_los_bambues_48_13k_2024). Signed 2024-06-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0040_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_make_ready_los_bambues_48_13k_2024 USD 0.013m. Supports misc_dominican_make_ready_los_bambues_48_13k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13319.5; date_signed 2024-06-27.",
)

# === Cycle 1201 ===
row_doc(
    "misc_brazil_fmc_electrical_data_cabling_phase2_13k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil FMC office electrical/data cabling restoration phase 2",
    "Brazil",
    "23 Mar 2017: Department of State awards contract SBR25017M0438 for FMC office electrical/data cabling restoration (phase 2) (PoP Brazil); obligated USD 13315.74. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13315.74", "2017-03-23", "2017", "", "",
    "FMC office electrical/data cabling restoration (phase 2), Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_fmc_electrical_data_cabling_phase2_13k_2017",
    "FMC OFFICE ELETRICAL/DATA CABLING RESTORATION(PHASE 2)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M0438_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1201",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25017M0438_1900_-NONE-_-NONE- (misc_brazil_fmc_electrical_data_cabling_phase2_13k_2017). Signed 2017-03-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M0438_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_fmc_electrical_data_cabling_phase2_13k_2017 USD 0.013m. Supports misc_brazil_fmc_electrical_data_cabling_phase2_13k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13315.74; date_signed 2017-03-23.",
)

# === Cycle 1201 ===
row_doc(
    "misc_peru_lima_elec_water_heaters_replace_13k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Peru Lima replace electric water heaters (chancery, motor pool)",
    "Peru",
    "22 Mar 2016: Department of State awards contract SPE50016C0010 for Lima contract to replace elec water heaters (chancery, motor pool) (PoP Peru); obligated USD 13308.98. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13308.98", "2016-03-22", "2016", "", "",
    "Lima contract to replace elec water heaters (chancery, motor pool), Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_peru_lima_elec_water_heaters_replace_13k_2016",
    "LIMA-CONTRACT TO REPLACE ELEC WATER HEATERS (CHCY, MPOOL) IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0010_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1201",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50016C0010_1900_-NONE-_-NONE- (misc_peru_lima_elec_water_heaters_replace_13k_2016). Signed 2016-03-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0010_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_lima_elec_water_heaters_replace_13k_2016 USD 0.013m. Supports misc_peru_lima_elec_water_heaters_replace_13k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13308.98; date_signed 2016-03-22.",
)

# === Cycle 1202 ===
row_doc(
    "norshield_brazil_metal_door_screen_9k_2016",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Brazil metal door screen",
    "Brazil",
    "19 Jan 2016: Department of State awards contract SAQMMA16M0256 to NORSHIELD SECURITY PRODUCTS, LLC for Metal door, screen etc. (PoP Brazil); obligated USD 9545. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "9545", "2016-01-19", "2016", "", "",
    "Metal door, screen etc., Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_brazil_metal_door_screen_9k_2016",
    "METAL DOOR, SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M0256_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1202",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16M0256_1900_-NONE-_-NONE- (norshield_brazil_metal_door_screen_9k_2016). Signed 2016-01-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16M0256_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_brazil_metal_door_screen_9k_2016 USD 0.010m. Supports norshield_brazil_metal_door_screen_9k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9545.0; date_signed 2016-01-19.",
)

# === Cycle 1202 ===
row_doc(
    "norshield_jamaica_metal_door_screen_9k_2017",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Jamaica metal door screen",
    "Jamaica",
    "25 Jan 2017: Department of State awards contract SAQMMA17M0199 to NORSHIELD SECURITY PRODUCTS, LLC for Metal door, screen etc. (PoP Jamaica); obligated USD 9496. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "9496", "2017-01-25", "2017", "", "",
    "Metal door, screen etc., Jamaica (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_jamaica_metal_door_screen_9k_2017",
    "METAL DOOR, SCREEN ETC. IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0199_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1202",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17M0199_1900_-NONE-_-NONE- (norshield_jamaica_metal_door_screen_9k_2017). Signed 2017-01-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0199_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_jamaica_metal_door_screen_9k_2017 USD 0.009m. Supports norshield_jamaica_metal_door_screen_9k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9496.0; date_signed 2017-01-25.",
)

# === Cycle 1202 ===
row_doc(
    "misc_dominican_gso_generator_autodialers_13k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic GSO generator autodialers",
    "Dominican Republic",
    "25 Aug 2011: Department of State awards contract SDR86011M1392 for PROG-525-GSO generator autodialers (PoP Dominican Republic); obligated USD 13300. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13300", "2011-08-25", "2011", "", "",
    "PROG-525-GSO generator autodialers, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_dominican_gso_generator_autodialers_13k_2011",
    "PROG-525-GSO  GENERATOR AUTODIALERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011M1392_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1202",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86011M1392_1900_-NONE-_-NONE- (misc_dominican_gso_generator_autodialers_13k_2011). Signed 2011-08-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011M1392_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_gso_generator_autodialers_13k_2011 USD 0.013m. Supports misc_dominican_gso_generator_autodialers_13k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13300.0; date_signed 2011-08-25.",
)

# === Cycle 1202 ===
row_doc(
    "misc_dominican_maag_paz_res_generator_13k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic MAAG/PAZ residence generator",
    "Dominican Republic",
    "7 Sep 2010: Department of State awards contract SDR86010M0201 for MAAG/PAZ residence generator (PoP Dominican Republic); obligated USD 13279. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13279", "2010-09-07", "2010", "", "",
    "MAAG/PAZ residence generator, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_dominican_maag_paz_res_generator_13k_2010",
    "MAAG/PAZ RES GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86010M0201_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1202",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86010M0201_1900_-NONE-_-NONE- (misc_dominican_maag_paz_res_generator_13k_2010). Signed 2010-09-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86010M0201_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_maag_paz_res_generator_13k_2010 USD 0.013m. Supports misc_dominican_maag_paz_res_generator_13k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13279.0; date_signed 2010-09-07.",
)

# === Cycle 1202 ===
row_doc(
    "misc_uruguay_security_grills_residence_13k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Uruguay security grills for residence",
    "Uruguay",
    "7 Dec 2017: Department of State awards contract 19UY6018P0080 for Security grills for residence (PoP Uruguay); obligated USD 13265.45. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13265.45", "2017-12-07", "2017", "", "",
    "Security grills for residence, Uruguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_uruguay_security_grills_residence_13k_2018",
    "SECURITY GRILLS FOR RESIDENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6018P0080_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1202",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19UY6018P0080_1900_-NONE-_-NONE- (misc_uruguay_security_grills_residence_13k_2018). Signed 2017-12-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19UY6018P0080_1900_-NONE-_-NONE-/.",
    "USASpending: misc_uruguay_security_grills_residence_13k_2018 USD 0.013m. Supports misc_uruguay_security_grills_residence_13k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13265.45; date_signed 2017-12-07.",
)

# === Cycle 1203 ===
row_doc(
    "norshield_brazil_metal_door_screen_9k_2019",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Brazil metal door screen",
    "Brazil",
    "10 Jun 2019: Department of State awards contract 19AQMM19P0967 to NORSHIELD SECURITY PRODUCTS, LLC for Metal door screen etc. (PoP Brazil); obligated USD 9260. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "9260", "2019-06-10", "2019", "", "",
    "Metal door screen etc., Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_brazil_metal_door_screen_9k_2019",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0967_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1203",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19P0967_1900_-NONE-_-NONE- (norshield_brazil_metal_door_screen_9k_2019). Signed 2019-06-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0967_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_brazil_metal_door_screen_9k_2019 USD 0.009m. Supports norshield_brazil_metal_door_screen_9k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9260.0; date_signed 2019-06-10.",
)

# === Cycle 1203 ===
row_doc(
    "harden_argentina_metal_door_screen_frame_9k_2024",
    "infrastructure", "building_materials", "us",
    "Harden Architectural Security Products — Argentina metal door screen frame for international embassies",
    "Argentina",
    "27 Nov 2023: Department of State awards contract 19AQMM24P0055 to HARDEN ARCHITECTURAL SECURITY PRODUCTS, LLC for Metal door screen frame etc. for international embassies (PoP Argentina); obligated USD 8537. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "8537", "2023-11-27", "2023", "", "",
    "Metal door screen frame etc. for international embassies, Argentina (USASpending description; site not named — lat/lon blank).",
    "usaspending_harden_argentina_metal_door_screen_frame_9k_2024",
    "METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0055_1900_-NONE-_-NONE-/",
    "Actor: HARDEN ARCHITECTURAL SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1203",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0055_1900_-NONE-_-NONE- (harden_argentina_metal_door_screen_frame_9k_2024). Signed 2023-11-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0055_1900_-NONE-_-NONE-/.",
    "USASpending: harden_argentina_metal_door_screen_frame_9k_2024 USD 0.009m. Supports harden_argentina_metal_door_screen_frame_9k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 8537.0; date_signed 2023-11-27.",
)

# === Cycle 1203 ===
row_doc(
    "misc_mexico_nogales_portofino_security_grills_13k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico DS security grills at Portofino residences Nogales",
    "Mexico",
    "14 Jul 2016: Department of State awards contract SMX60016M0087 for DS security grills at Portofino residences — Nogales (PoP Mexico); obligated USD 13261.12. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13261.12", "2016-07-14", "2016", "", "",
    "DS security grills at Portofino residences — Nogales, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_nogales_portofino_security_grills_13k_2016",
    "DS - SECURITY GRILLS AT PORTOFINO RESIDENCES - NOGALES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX60016M0087_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1203",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX60016M0087_1900_-NONE-_-NONE- (misc_mexico_nogales_portofino_security_grills_13k_2016). Signed 2016-07-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX60016M0087_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_nogales_portofino_security_grills_13k_2016 USD 0.013m. Supports misc_mexico_nogales_portofino_security_grills_13k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13261.12; date_signed 2016-07-14.",
)

# === Cycle 1203 ===
row_doc(
    "misc_venezuela_chancery_fan_coils_consular_13k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Venezuela chancery new fan coils installation at consular section",
    "Venezuela",
    "28 Jun 2013: Department of State awards contract SVE30013M0449 for Chancery new fan coils installation at consular section (PoP Venezuela); obligated USD 13248.48. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13248.48", "2013-06-28", "2013", "", "",
    "Chancery new fan coils installation at consular section, Venezuela (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_venezuela_chancery_fan_coils_consular_13k_2013",
    "CHANCERY:  NEW FAN COILS INSTALLATION AT CONSULAR SECTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30013M0449_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1203",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30013M0449_1900_-NONE-_-NONE- (misc_venezuela_chancery_fan_coils_consular_13k_2013). Signed 2013-06-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30013M0449_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_chancery_fan_coils_consular_13k_2013 USD 0.013m. Supports misc_venezuela_chancery_fan_coils_consular_13k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13248.48; date_signed 2013-06-28.",
)

# === Cycle 1203 ===
row_doc(
    "misc_dominican_make_ready_los_bambues_27_14k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic OSC make-ready Los Bambues 27",
    "Dominican Republic",
    "10 Jul 2024: Department of State awards contract 19DR8624C0054 for OSC make-ready work Los Bambues 27 PID 849 (PoP Dominican Republic); obligated USD 14001.95. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "14001.95", "2024-07-10", "2024", "", "",
    "OSC make-ready work Los Bambues 27 PID 849, Dominican Republic (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_make_ready_los_bambues_27_14k_2024",
    "OSC- MAKE READY WORK LOS BAMBUES 27 PID 849 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0054_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1203",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0054_1900_-NONE-_-NONE- (misc_dominican_make_ready_los_bambues_27_14k_2024). Signed 2024-07-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0054_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_make_ready_los_bambues_27_14k_2024 USD 0.014m. Supports misc_dominican_make_ready_los_bambues_27_14k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14001.95; date_signed 2024-07-10.",
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
