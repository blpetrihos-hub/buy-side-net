#!/usr/bin/env python3
"""Cycles 1174–1176: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262174–20262176. Thin top-up dry.
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


# === Cycle 1174 (seed 20262174) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "valkyrie_mexico_obo_telecommunications_cabling_services_133k_2022",
    "infrastructure", "building_materials", "us",
    "Valkyrie Enterprises — Mexico OBO telecommunications cabling services",
    "Mexico",
    "14 Dec 2022: Department of State awards contract 19AQMM23F0101 to Valkyrie Enterprises, LLC for OBO PDCS DE EE telecommunications cabling services (PoP Mexico); obligated USD 132,508.36. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "132508.36", "2022-12-14", "2022", "", "",
    "OBO telecommunications cabling services, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_valkyrie_mexico_obo_telecommunications_cabling_services_133k_2022",
    "THE US DEPARTMENT OF STATE, BUREAU OF OVERSEAS BUILDING OPERATIONS, PROGRAM DEVELOPMENT, COORDINATION, AND SUPPORT, OFFICE OF DESIGN AND ENGINEERING, ELECTRICAL ENGINEERING DIVISION (OBO/PDCS/DE/EE), TO USE THE SERVICES OF A TELECOMMUNICATIONS CABLIN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0101_1900_19AQMM21D0155_1900/",
    "Actor: VALKYRIE ENTERPRISES, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1174",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23F0101_1900_19AQMM21D0155_1900 (valkyrie_mexico_obo_telecommunications_cabling_services_133k_2022). Signed 2022-12-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F0101_1900_19AQMM21D0155_1900/.",
    "USASpending: valkyrie_mexico_obo_telecommunications_cabling_services_133k_2022 USD 0.133m. Supports valkyrie_mexico_obo_telecommunications_cabling_services_133k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 132508.36; date_signed 2022-12-14.",
)
row_doc(
    "valkyrie_guatemala_nec_stcs_cabling_109k_2022",
    "infrastructure", "building_materials", "us",
    "Valkyrie Enterprises — Guatemala City NEC structured telecommunications cabling system",
    "Guatemala",
    "18 May 2022: Department of State awards contract 19AQMM22F1821 to Valkyrie Enterprises, LLC for structured telecommunications cabling system (STCS) at the new embassy compound (NEC) in Guatemala City (PoP Guatemala); obligated USD 109,102.0. CapEx face = award obligation. Guatemala City NEC named; site coords not stated — lat/lon blank.",
    "109102", "2022-05-18", "2022", "", "",
    "STCS at new embassy compound, Guatemala City, Guatemala (USASpending description; NEC Guatemala City named, site coords not stated — lat/lon blank).",
    "usaspending_valkyrie_guatemala_nec_stcs_cabling_109k_2022",
    "STRUCTURED TELECOMMUNICATIONS CABLING SYSTEM (STCS) AT THE NEW EMBASSY COMPOUND (NEC) IN GUATEMALA CITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1821_1900_19AQMM21D0155_1900/",
    "Actor: VALKYRIE ENTERPRISES, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1174",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F1821_1900_19AQMM21D0155_1900 (valkyrie_guatemala_nec_stcs_cabling_109k_2022). Signed 2022-05-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1821_1900_19AQMM21D0155_1900/.",
    "USASpending: valkyrie_guatemala_nec_stcs_cabling_109k_2022 USD 0.109m. Supports valkyrie_guatemala_nec_stcs_cabling_109k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 109102.0; date_signed 2022-05-18.",
)
row_doc(
    "misc_mexico_odc_security_upgrades_14k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico ODC security upgrades",
    "Mexico",
    "25 Feb 2013: Department of State awards contract SMX53013M0463 for MEX-ODC security upgrades (PoP Mexico); obligated USD 14,465.39. CapEx face = award obligation. ODC named; site coords not stated — lat/lon blank.",
    "14465.39", "2013-02-25", "2013", "", "",
    "ODC security upgrades, Mexico (USASpending description; ODC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_odc_security_upgrades_14k_2013",
    "IGF::OT::IGF MEX-ODC-1150.0/ SECURITY UPGRADES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0463_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1174",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53013M0463_1900_-NONE-_-NONE- (misc_mexico_odc_security_upgrades_14k_2013). Signed 2013-02-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0463_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_odc_security_upgrades_14k_2013 USD 0.014m. Supports misc_mexico_odc_security_upgrades_14k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14465.39; date_signed 2013-02-25.",
)
row_doc(
    "misc_trinidad_warehouse_storage_racks_supply_install_14k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Trinidad and Tobago storage racks for warehouse supply and install",
    "Trinidad and Tobago",
    "8 Feb 2013: Department of State awards contract STD55013M0099 for storage racks for warehouse supply and install (PoP Trinidad and Tobago); obligated USD 14,415.39. CapEx face = award obligation. Warehouse unnamed — lat/lon blank.",
    "14415.39", "2013-02-08", "2013", "", "",
    "Storage racks for warehouse supply and install, Trinidad and Tobago (USASpending description; warehouse unnamed — lat/lon blank).",
    "usaspending_misc_trinidad_warehouse_storage_racks_supply_install_14k_2013",
    "STORAGE RACKS FOR WAREHOUSE (SUPPLY AND INSTALL)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_STD55013M0099_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1174",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_STD55013M0099_1900_-NONE-_-NONE- (misc_trinidad_warehouse_storage_racks_supply_install_14k_2013). Signed 2013-02-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_STD55013M0099_1900_-NONE-_-NONE-/.",
    "USASpending: misc_trinidad_warehouse_storage_racks_supply_install_14k_2013 USD 0.014m. Supports misc_trinidad_warehouse_storage_racks_supply_install_14k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14415.39; date_signed 2013-02-08.",
)
row_doc(
    "misc_barbados_cmr_security_cameras_equipment_14k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Barbados RSO CMR security cameras and equipment",
    "Barbados",
    "9 Aug 2013: Department of State awards contract SBB21013M0634 for RSO CMR security cameras and equipment (PoP Barbados); obligated USD 14,362.92. CapEx face = award obligation. CMR named; site coords not stated — lat/lon blank.",
    "14362.92", "2013-08-09", "2013", "", "",
    "CMR security cameras and equipment, Barbados (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_barbados_cmr_security_cameras_equipment_14k_2013",
    "RSO//CMR SECURITY CAMERAS AND EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21013M0634_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1174",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21013M0634_1900_-NONE-_-NONE- (misc_barbados_cmr_security_cameras_equipment_14k_2013). Signed 2013-08-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21013M0634_1900_-NONE-_-NONE-/.",
    "USASpending: misc_barbados_cmr_security_cameras_equipment_14k_2013 USD 0.014m. Supports misc_barbados_cmr_security_cameras_equipment_14k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14362.92; date_signed 2013-08-09.",
)

# === Cycle 1175 (seed 20262175) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "johnson_controls_jamaica_bas_stand_alone_replacement_90k_2020",
    "energy", "power_plants_grid", "us",
    "Johnson Controls Building Automation Systems — Jamaica replacement of BAS stand-alone",
    "Jamaica",
    "6 Feb 2020: Department of State awards contract 19JM3720P0317 to Johnson Controls Building Automation Systems, LLC for replacement of BAS stand-alone (PoP Jamaica); obligated USD 90,459.75. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "90459.75", "2020-02-06", "2020", "", "",
    "Replacement of BAS stand-alone, Jamaica (USASpending description; site not named — lat/lon blank).",
    "usaspending_johnson_controls_jamaica_bas_stand_alone_replacement_90k_2020",
    "REPLACEMENT OF BAS-STAND ALONE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3720P0317_1900_-NONE-_-NONE-/",
    "Actor: JOHNSON CONTROLS BUILDING AUTOMATION SYSTEMS, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1175",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3720P0317_1900_-NONE-_-NONE- (johnson_controls_jamaica_bas_stand_alone_replacement_90k_2020). Signed 2020-02-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3720P0317_1900_-NONE-_-NONE-/.",
    "USASpending: johnson_controls_jamaica_bas_stand_alone_replacement_90k_2020 USD 0.09m. Supports johnson_controls_jamaica_bas_stand_alone_replacement_90k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 90459.75; date_signed 2020-02-06.",
)
row_doc(
    "applied_security_uruguay_technical_security_service_install_73k_2022",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Uruguay technical security service installation",
    "Uruguay",
    "6 May 2022: Department of State awards contract 19AQMM22F1752 to Applied Security Technologies Inc for technical security service installation (PoP Uruguay); obligated USD 72,723.14. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "72723.14", "2022-05-06", "2022", "", "",
    "Technical security service installation, Uruguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_applied_security_uruguay_technical_security_service_install_73k_2022",
    "TECHNICAL SECURITY SERVICE INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1752_1900_19AQMM19D0002_1900/",
    "Actor: APPLIED SECURITY TECHNOLOGIES INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1175",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F1752_1900_19AQMM19D0002_1900 (applied_security_uruguay_technical_security_service_install_73k_2022). Signed 2022-05-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F1752_1900_19AQMM19D0002_1900/.",
    "USASpending: applied_security_uruguay_technical_security_service_install_73k_2022 USD 0.073m. Supports applied_security_uruguay_technical_security_service_install_73k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 72723.14; date_signed 2022-05-06.",
)
row_doc(
    "misc_el_salvador_aid_servers_room_door_division_replace_14k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador AID servers room door and division replacement",
    "El Salvador",
    "14 Sep 2020: Department of State awards contract 19ES6020P0817 for AID servers room door and division replacement (PoP El Salvador); obligated USD 14,356.88. CapEx face = award obligation. AID servers room named; site coords not stated — lat/lon blank.",
    "14356.88", "2020-09-14", "2020", "", "",
    "AID servers room door and division replacement, El Salvador (USASpending description; servers room named, site coords not stated — lat/lon blank).",
    "usaspending_misc_el_salvador_aid_servers_room_door_division_replace_14k_2020",
    "AID SERVERS ROOM DOOR AND DIVISION REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6020P0817_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1175",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6020P0817_1900_-NONE-_-NONE- (misc_el_salvador_aid_servers_room_door_division_replace_14k_2020). Signed 2020-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6020P0817_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_aid_servers_room_door_division_replace_14k_2020 USD 0.014m. Supports misc_el_salvador_aid_servers_room_door_division_replace_14k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14356.88; date_signed 2020-09-14.",
)
row_doc(
    "misc_brazil_intelbras_amt8000_alarm_system_14k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil Intelbras AMT 8000 alarm system GPRS module",
    "Brazil",
    "24 Sep 2020: Department of State awards contract 19BR2520P0983 for Intelbras AMT 8000 alarm system GPRS 3G module (PoP Brazil); obligated USD 14,376.51. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14376.51", "2020-09-24", "2020", "", "",
    "Intelbras AMT 8000 alarm system module, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_intelbras_amt8000_alarm_system_14k_2020",
    "MODULO GPRS 3G INTELBRAS AMT 8000 ALARM SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0983_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1175",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2520P0983_1900_-NONE-_-NONE- (misc_brazil_intelbras_amt8000_alarm_system_14k_2020). Signed 2020-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0983_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_intelbras_amt8000_alarm_system_14k_2020 USD 0.014m. Supports misc_brazil_intelbras_amt8000_alarm_system_14k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14376.51; date_signed 2020-09-24.",
)
row_doc(
    "misc_barbados_schaller_security_grills_14k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Barbados security grills Schaller/program",
    "Barbados",
    "30 Sep 2010: Department of State awards contract SBB21010M0669 for security grills Schaller/program (PoP Barbados); obligated USD 14,397.0. CapEx face = award obligation. Schaller named; site coords not stated — lat/lon blank.",
    "14397", "2010-09-30", "2010", "", "",
    "Security grills Schaller/program, Barbados (USASpending description; Schaller named, site coords not stated — lat/lon blank).",
    "usaspending_misc_barbados_schaller_security_grills_14k_2010",
    "SECURITY GRILLS SCHALLER/PROGRAM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21010M0669_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1175",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBB21010M0669_1900_-NONE-_-NONE- (misc_barbados_schaller_security_grills_14k_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBB21010M0669_1900_-NONE-_-NONE-/.",
    "USASpending: misc_barbados_schaller_security_grills_14k_2010 USD 0.014m. Supports misc_barbados_schaller_security_grills_14k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14397.0; date_signed 2010-09-30.",
)

# === Cycle 1176 (seed 20262176) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "applied_security_mexico_technical_security_systems_install_38k_2017",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Mexico technical security systems installation",
    "Mexico",
    "22 Jun 2017: Department of State awards contract SAQMMA17F2060 to Applied Security Technologies Inc for technical security systems installation (PoP Mexico); obligated USD 38,049.43. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "38049.43", "2017-06-22", "2017", "", "",
    "Technical security systems installation, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_applied_security_mexico_technical_security_systems_install_38k_2017",
    "TECHNICAL SECURITY SYSTEMS INSTALLATIONIGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F2060_1900_SAQMMA13D0054_1900/",
    "Actor: APPLIED SECURITY TECHNOLOGIES INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1176",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17F2060_1900_SAQMMA13D0054_1900 (applied_security_mexico_technical_security_systems_install_38k_2017). Signed 2017-06-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17F2060_1900_SAQMMA13D0054_1900/.",
    "USASpending: applied_security_mexico_technical_security_systems_install_38k_2017 USD 0.038m. Supports applied_security_mexico_technical_security_systems_install_38k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 38049.43; date_signed 2017-06-22.",
)
row_doc(
    "norshield_uruguay_metal_door_screen_19k_2020",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Uruguay metal door screen",
    "Uruguay",
    "17 Aug 2020: Department of State awards contract 19AQMM20P1350 to Norshield Security Products, LLC for metal door screen etc. (PoP Uruguay); obligated USD 18,620.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "18620", "2020-08-17", "2020", "", "",
    "Metal door screen etc., Uruguay (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_uruguay_metal_door_screen_19k_2020",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P1350_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1176",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20P1350_1900_-NONE-_-NONE- (norshield_uruguay_metal_door_screen_19k_2020). Signed 2020-08-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P1350_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_uruguay_metal_door_screen_19k_2020 USD 0.019m. Supports norshield_uruguay_metal_door_screen_19k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18620.0; date_signed 2020-08-17.",
)
row_doc(
    "misc_mexico_chancery_two_restrooms_renovation_14k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico renovation of two restrooms on chancery",
    "Mexico",
    "5 Aug 2016: Department of State awards contract SMX53016C0006 for renovation of two restrooms on chancery (PoP Mexico); obligated USD 14,346.15. CapEx face = award obligation. Chancery named; site coords not stated — lat/lon blank.",
    "14346.15", "2016-08-05", "2016", "", "",
    "Renovation of two restrooms on chancery, Mexico (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_chancery_two_restrooms_renovation_14k_2016",
    "MEX FAC 7901 C RENOVATION OF TWO RESTROOMS ON CHANCERY IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53016C0006_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1176",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53016C0006_1900_-NONE-_-NONE- (misc_mexico_chancery_two_restrooms_renovation_14k_2016). Signed 2016-08-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53016C0006_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_chancery_two_restrooms_renovation_14k_2016 USD 0.014m. Supports misc_mexico_chancery_two_restrooms_renovation_14k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14346.15; date_signed 2016-08-05.",
)
row_doc(
    "misc_haiti_tabarre_blts_genset_install_14k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Haiti installation of a genset at Tabarre new BLTS office",
    "Haiti",
    "18 Jan 2011: Department of State awards contract SHA70011M0316 for installation of a genset at Tabarre new BLTS office (PoP Haiti); obligated USD 14,334.02. CapEx face = award obligation. Tabarre named; site coords not stated — lat/lon blank.",
    "14334.02", "2011-01-18", "2011", "", "",
    "Genset installation at Tabarre new BLTS office, Haiti (USASpending description; Tabarre named, site coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_tabarre_blts_genset_install_14k_2011",
    "INSTALLATION OF A GENSET AT TABARRE (NEW BLTS OFFICE)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHA70011M0316_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1176",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHA70011M0316_1900_-NONE-_-NONE- (misc_haiti_tabarre_blts_genset_install_14k_2011). Signed 2011-01-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHA70011M0316_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_tabarre_blts_genset_install_14k_2011 USD 0.014m. Supports misc_haiti_tabarre_blts_genset_install_14k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14334.02; date_signed 2011-01-18.",
)
row_doc(
    "misc_dominican_republic_cbpo_lafuente_generator_transfer_14k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic DHS/CBP-CSI generator and transfer for CBPO Lafuente house",
    "Dominican Republic",
    "22 Aug 2011: Department of State awards contract SDR86011M1358 for DHS/CBP-CSI generator and transfer for CBPO Lafuente house (PoP Dominican Republic); obligated USD 14,329.45. CapEx face = award obligation. CBPO Lafuente house named; site coords not stated — lat/lon blank.",
    "14329.45", "2011-08-22", "2011", "", "",
    "Generator and transfer for CBPO Lafuente house, Dominican Republic (USASpending description; residence named, site coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_republic_cbpo_lafuente_generator_transfer_14k_2011",
    "DHS/CBP-CSI GENERATOR AND TRANSFER FOR CBPO LAFUENTE'S HOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011M1358_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1176",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86011M1358_1900_-NONE-_-NONE- (misc_dominican_republic_cbpo_lafuente_generator_transfer_14k_2011). Signed 2011-08-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86011M1358_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_republic_cbpo_lafuente_generator_transfer_14k_2011 USD 0.014m. Supports misc_dominican_republic_cbpo_lafuente_generator_transfer_14k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14329.45; date_signed 2011-08-22.",
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
