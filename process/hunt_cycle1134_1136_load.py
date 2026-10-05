#!/usr/bin/env python3
"""Cycles 1134–1136: USASpending LatAm CapEx residual (~USD0.018–0.035m).

Seeds: 20262134–20262136. Thin top-up dry.
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


# === Cycle 1134 (seed 20262134) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "light_edge_el_salvador_replace_light_fixtures_35k_2013",
    "infrastructure", "building_materials", "us",
    "Light Edge — El Salvador replace light fixtures",
    "El Salvador",
    "12 Sep 2013: Department of State awards contract SES60013F0113 to Light Edge Inc., The for replace light fixtures (PoP El Salvador); obligated USD 35,310.24. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "35310.24", "2013-09-12", "2013", "", "",
    "Replace light fixtures, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_light_edge_el_salvador_replace_light_fixtures_35k_2013",
    "7901C FUNDS--REPLACE LIGHT FIXTURES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60013F0113_1900_GS07F0517W_4730/",
    "Actor: Light Edge Inc., The (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1134",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60013F0113_1900_GS07F0517W_4730 (light_edge_el_salvador_replace_light_fixtures_35k_2013). Signed 2013-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60013F0113_1900_GS07F0517W_4730/.",
    "USASpending: light_edge_el_salvador_replace_light_fixtures_35k_2013 USD 0.035m. Supports light_edge_el_salvador_replace_light_fixtures_35k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 35310.24; date_signed 2013-09-12.",
)
row_doc(
    "power_pros_mexico_powerware_ferrups_hale_20k_2011",
    "energy", "power_plants_grid", "us",
    "Power Pros — Mexico Powerware Ferrups to support Hale project",
    "Mexico",
    "17 May 2011: Department of State awards contract SMX53011M0945 to Power Pros, Inc. for NAS-MI IN23MX91 Powerware Ferrups to supp Hale project (PoP Mexico); obligated USD 20,094. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "20094", "2011-05-17", "2011", "", "",
    "Powerware Ferrups to support Hale project, Mexico (USASpending description; project named, site coords not stated — lat/lon blank).",
    "usaspending_power_pros_mexico_powerware_ferrups_hale_20k_2011",
    "NAS-MI IN23MX91 POWERWARE FERRUPS TO SUPP HALE PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M0945_1900_-NONE-_-NONE-/",
    "Actor: Power Pros, Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1134",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53011M0945_1900_-NONE-_-NONE- (power_pros_mexico_powerware_ferrups_hale_20k_2011). Signed 2011-05-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53011M0945_1900_-NONE-_-NONE-/.",
    "USASpending: power_pros_mexico_powerware_ferrups_hale_20k_2011 USD 0.020m. Supports power_pros_mexico_powerware_ferrups_hale_20k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 20094; date_signed 2011-05-17.",
)
row_doc(
    "misc_panama_nec_perimeter_wall_extend_20k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Panama NEC extend top of perimeter wall for security",
    "Panama",
    "16 Aug 2011: Department of State awards contract SPM07011M0514 for PO extend top of perimeter wall for security - NEC (PoP Panama); obligated USD 19,900. CapEx face = award obligation. Exact NEC unnamed — lat/lon blank.",
    "19900", "2011-08-16", "2011", "", "",
    "Extend top of perimeter wall for security - NEC, Panama (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_panama_nec_perimeter_wall_extend_20k_2011",
    "PO EXTEND TOP OF PERIMETER WALL FOR SECURITY - NEC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07011M0514_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1134",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07011M0514_1900_-NONE-_-NONE- (misc_panama_nec_perimeter_wall_extend_20k_2011). Signed 2011-08-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07011M0514_1900_-NONE-_-NONE-/.",
    "USASpending: misc_panama_nec_perimeter_wall_extend_20k_2011 USD 0.020m. Supports misc_panama_nec_perimeter_wall_extend_20k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19900; date_signed 2011-08-16.",
)
row_doc(
    "misc_costa_rica_obc_replace_chill_water_pumps_20k_2012",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Costa Rica OBC replace chill water pumps and accessories",
    "Costa Rica",
    "24 Aug 2012: Department of State awards contract SCS80012M0753 for FAC/7901 OBC replace chill water pumps and accesories (PoP Costa Rica); obligated USD 19,890. CapEx face = award obligation. Exact OBC unnamed — lat/lon blank.",
    "19890", "2012-08-24", "2012", "", "",
    "OBC replace chill water pumps and accessories, Costa Rica (USASpending description; OBC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_obc_replace_chill_water_pumps_20k_2012",
    "FAC/7901 OBC REPLACE CHILL WATER PUMPS AND ACCESORIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80012M0753_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1134",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80012M0753_1900_-NONE-_-NONE- (misc_costa_rica_obc_replace_chill_water_pumps_20k_2012). Signed 2012-08-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80012M0753_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_obc_replace_chill_water_pumps_20k_2012 USD 0.020m. Supports misc_costa_rica_obc_replace_chill_water_pumps_20k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19890; date_signed 2012-08-24.",
)
row_doc(
    "misc_ecuador_computer_room_ups_install_35k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Ecuador UPS installation for computer room",
    "Ecuador",
    "17 Jun 2011: Department of State awards contract SEC75011M0543 for 7901.0 - UPS installation for computer room (PoP Ecuador); obligated USD 34,865. CapEx face = award obligation. Exact computer room unnamed — lat/lon blank.",
    "34865", "2011-06-17", "2011", "", "",
    "UPS installation for computer room, Ecuador (USASpending description; room not named — lat/lon blank).",
    "usaspending_misc_ecuador_computer_room_ups_install_35k_2011",
    "7901.0 - UPS INSTALLATION FOR COMPUTER ROOM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75011M0543_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1134",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SEC75011M0543_1900_-NONE-_-NONE- (misc_ecuador_computer_room_ups_install_35k_2011). Signed 2011-06-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC75011M0543_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_computer_room_ups_install_35k_2011 USD 0.035m. Supports misc_ecuador_computer_room_ups_install_35k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 34865; date_signed 2011-06-17.",
)

# === Cycle 1135 (seed 20262135) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_brazil_brasilia_security_glazing_35k_2023",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Brazil Brasilia embassy security glazing",
    "Brazil",
    "29 Nov 2023: Department of State awards contract 19AQMM24P0062 to Norshield Security Products, LLC for Brasilia security glazing with Sungate LowE (PoP Brazil); obligated USD 35,235. CapEx face = award obligation. Brasilia embassy named; site coords not stated — lat/lon blank.",
    "35235", "2023-11-29", "2023", "", "",
    "Brasilia embassy security glazing, Brazil (USASpending description; Brasilia (E) SES named, site coords not stated — lat/lon blank).",
    "usaspending_norshield_brazil_brasilia_security_glazing_35k_2023",
    "---------- COMMENTS: BRASILIA_NS_S-CAC-GPR-01EA. NS PROPOSAL NO. 110123-01.  PROVIDE/AIR SHIP SECURITY GP DOS CODE: 1123, TYPE:255 SECURITY GLAZING W/SUNGATE LOWE. SIZE IS 39-7/8  X 66-3/8 . GLASS WEIGHT IS APPROX. 370 LBS.  ADDRESS: BRASILIA (E) SES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0062_1900_-NONE-_-NONE-/",
    "Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1135",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0062_1900_-NONE-_-NONE- (norshield_brazil_brasilia_security_glazing_35k_2023). Signed 2023-11-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0062_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_brazil_brasilia_security_glazing_35k_2023 USD 0.035m. Supports norshield_brazil_brasilia_security_glazing_35k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 35235; date_signed 2023-11-29.",
)
row_doc(
    "city_electric_colombia_parking_lot_led_kit_20k_2020",
    "energy", "power_plants_grid", "us",
    "City Electric Supply — Colombia LED kit for exterior parking lot lights",
    "Colombia",
    "23 Sep 2020: Department of State awards contract 19C02020P0574 to City Electric Supply Company for LED kit for exterior parking lot lights (PoP Colombia); obligated USD 19,900. CapEx face = award obligation. Exact parking lot unnamed — lat/lon blank.",
    "19900", "2020-09-23", "2020", "", "",
    "LED kit for exterior parking lot lights, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_city_electric_colombia_parking_lot_led_kit_20k_2020",
    "PR9153324 LED KIT FOR EXTERIOR PARKING LOT LIGHTS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02020P0574_1900_-NONE-_-NONE-/",
    "Actor: City Electric Supply Company (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1135",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02020P0574_1900_-NONE-_-NONE- (city_electric_colombia_parking_lot_led_kit_20k_2020). Signed 2020-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02020P0574_1900_-NONE-_-NONE-/.",
    "USASpending: city_electric_colombia_parking_lot_led_kit_20k_2020 USD 0.020m. Supports city_electric_colombia_parking_lot_led_kit_20k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19900; date_signed 2020-09-23.",
)
row_doc(
    "misc_bolivia_llojeta_warehouse_bathroom_renovation_20k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bolivia Llojeta warehouse bathroom renovation",
    "Bolivia",
    "10 Jun 2025: Department of State awards contract 19BL4025P0179 for bathroom renovation Llojeta warehouse (PoP Bolivia); obligated USD 19,881.75. CapEx face = award obligation. Llojeta warehouse named; site coords not stated — lat/lon blank.",
    "19881.75", "2025-06-10", "2025", "", "",
    "Bathroom renovation Llojeta warehouse, Bolivia (USASpending description; Llojeta named, site coords not stated — lat/lon blank).",
    "usaspending_misc_bolivia_llojeta_warehouse_bathroom_renovation_20k_2025",
    "BATHROOM RENOVATION LLOJETA WAREHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BL4025P0179_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1135",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BL4025P0179_1900_-NONE-_-NONE- (misc_bolivia_llojeta_warehouse_bathroom_renovation_20k_2025). Signed 2025-06-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BL4025P0179_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bolivia_llojeta_warehouse_bathroom_renovation_20k_2025 USD 0.020m. Supports misc_bolivia_llojeta_warehouse_bathroom_renovation_20k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19881.75; date_signed 2025-06-10.",
)
row_doc(
    "misc_bahamas_chancery_annex_restroom_renovation_18k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas chancery annex restroom renovation",
    "Bahamas",
    "30 Sep 2015: Department of State awards contract SBF50015C0006 for chancery - annex restroom renovation (PoP Bahamas); obligated USD 18,000. CapEx face = award obligation. Chancery annex named; site coords not stated — lat/lon blank.",
    "18000", "2015-09-30", "2015", "", "",
    "Chancery annex restroom renovation, Bahamas (USASpending description; chancery annex named, site coords not stated — lat/lon blank).",
    "usaspending_misc_bahamas_chancery_annex_restroom_renovation_18k_2015",
    "IGF::OT::IGF CHANCERY - ANNEX RESTROOM RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50015C0006_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1135",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50015C0006_1900_-NONE-_-NONE- (misc_bahamas_chancery_annex_restroom_renovation_18k_2015). Signed 2015-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50015C0006_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_chancery_annex_restroom_renovation_18k_2015 USD 0.018m. Supports misc_bahamas_chancery_annex_restroom_renovation_18k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18000; date_signed 2015-09-30.",
)
row_doc(
    "misc_venezuela_niv_cons_fence_install_18k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Venezuela NIV-CONS area fence install",
    "Venezuela",
    "14 Sep 2015: Department of State awards contract SVE30015M0885 for install fence in the NIV-CONS area (PoP Venezuela); obligated USD 18,000. CapEx face = award obligation. NIV-CONS area named; site coords not stated — lat/lon blank.",
    "18000", "2015-09-14", "2015", "", "",
    "Install fence in the NIV-CONS area, Venezuela (USASpending description; NIV-CONS named, site coords not stated — lat/lon blank).",
    "usaspending_misc_venezuela_niv_cons_fence_install_18k_2015",
    "INSTALL FENCE IN THE NIV-CONS AREA- SEE FAC FOR CHARGING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30015M0885_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1135",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30015M0885_1900_-NONE-_-NONE- (misc_venezuela_niv_cons_fence_install_18k_2015). Signed 2015-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30015M0885_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_niv_cons_fence_install_18k_2015 USD 0.018m. Supports misc_venezuela_niv_cons_fence_install_18k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18000; date_signed 2015-09-14.",
)

# === Cycle 1136 (seed 20262136) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "rrds_el_salvador_comalapa_gun_range_ac_install_35k_2025",
    "energy", "power_plants_grid", "us",
    "RRDS — El Salvador CSL Comalapa gun range air conditioner installation",
    "El Salvador",
    "29 Aug 2025: Department of State awards contract 19ES6025P0806 to RRDS Inc for air conditioner installation at CSL Comalapa gun range (PoP El Salvador); obligated USD 34,952. CapEx face = award obligation. CSL Comalapa gun range named; site coords not stated — lat/lon blank.",
    "34952", "2025-08-29", "2025", "", "",
    "Air conditioner installation at CSL Comalapa gun range, El Salvador (USASpending description; Comalapa named, site coords not stated — lat/lon blank).",
    "usaspending_rrds_el_salvador_comalapa_gun_range_ac_install_35k_2025",
    "AIR CONDITIONER INSTALLATION AT CSL COMALAPA GUN RANGE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6025P0806_1900_-NONE-_-NONE-/",
    "Actor: RRDS Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1136",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6025P0806_1900_-NONE-_-NONE- (rrds_el_salvador_comalapa_gun_range_ac_install_35k_2025). Signed 2025-08-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6025P0806_1900_-NONE-_-NONE-/.",
    "USASpending: rrds_el_salvador_comalapa_gun_range_ac_install_35k_2025 USD 0.035m. Supports rrds_el_salvador_comalapa_gun_range_ac_install_35k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 34952; date_signed 2025-08-29.",
)
row_doc(
    "habersham_guatemala_metal_door_screen_20k_2023",
    "infrastructure", "building_materials", "us",
    "Habersham Metal Products — Guatemala metal door screen for international embassies",
    "Guatemala",
    "27 Mar 2023: Department of State awards contract 19AQMM23P0378 to Habersham Metal Products Company for metal door screen etc. for international embassies (PoP Guatemala); obligated USD 19,876. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "19876", "2023-03-27", "2023", "", "",
    "Metal door screen etc. for international embassies, Guatemala (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_habersham_guatemala_metal_door_screen_20k_2023",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0378_1900_-NONE-_-NONE-/",
    "Actor: Habersham Metal Products Company (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1136",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23P0378_1900_-NONE-_-NONE- (habersham_guatemala_metal_door_screen_20k_2023). Signed 2023-03-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0378_1900_-NONE-_-NONE-/.",
    "USASpending: habersham_guatemala_metal_door_screen_20k_2023 USD 0.020m. Supports habersham_guatemala_metal_door_screen_20k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19876; date_signed 2023-03-27.",
)
row_doc(
    "misc_brazil_rso_security_solid_doors_20k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil RSO security solid doors for residential security program",
    "Brazil",
    "27 Jan 2017: Department of State awards contract SBR25017M0330 for RSO purchase of security solid doors for res sec program (PoP Brazil); obligated USD 19,858.71. CapEx face = award obligation. Exact residences unnamed — lat/lon blank.",
    "19858.71", "2017-01-27", "2017", "", "",
    "RSO security solid doors for residential security program, Brazil (USASpending description; residences not named — lat/lon blank).",
    "usaspending_misc_brazil_rso_security_solid_doors_20k_2017",
    "IGF::OT::IGF RSO - PURCHASE OF SECURITY SOLID DOORS FOR RES SEC PROGRAM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M0330_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1136",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25017M0330_1900_-NONE-_-NONE- (misc_brazil_rso_security_solid_doors_20k_2017). Signed 2017-01-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M0330_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_rso_security_solid_doors_20k_2017 USD 0.020m. Supports misc_brazil_rso_security_solid_doors_20k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19858.71; date_signed 2017-01-27.",
)
row_doc(
    "misc_peru_lima_fcs_offices_construction_20k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru Lima construction of new FCS offices",
    "Peru",
    "26 Sep 2016: Department of State awards contract SPE50016C0042 for Lima - contract for construction of new FCS offices (PoP Peru); obligated USD 19,874.15. CapEx face = award obligation. Lima FCS offices named; site coords not stated — lat/lon blank.",
    "19874.15", "2016-09-26", "2016", "", "",
    "Construction of new FCS offices, Lima, Peru (USASpending description; Lima FCS named, site coords not stated — lat/lon blank).",
    "usaspending_misc_peru_lima_fcs_offices_construction_20k_2016",
    'LIMA - CONTRACT FOR CONSTRUCTION OF NEW FCS OFFICES "IGF::OT::IGF"',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0042_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1136",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50016C0042_1900_-NONE-_-NONE- (misc_peru_lima_fcs_offices_construction_20k_2016). Signed 2016-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50016C0042_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_lima_fcs_offices_construction_20k_2016 USD 0.020m. Supports misc_peru_lima_fcs_offices_construction_20k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19874.15; date_signed 2016-09-26.",
)
row_doc(
    "misc_guatemala_milgp_generators_35k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Guatemala MILGP generators",
    "Guatemala",
    "30 Sep 2010: Department of State awards contract SGT50010M0433 for MILGP-generators (PoP Guatemala); obligated USD 34,884.59. CapEx face = award obligation. Exact MILGP site unnamed — lat/lon blank.",
    "34884.59", "2010-09-30", "2010", "", "",
    "MILGP generators, Guatemala (USASpending description; MILGP named, site coords not stated — lat/lon blank).",
    "usaspending_misc_guatemala_milgp_generators_35k_2010",
    "MILGP-GENERATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50010M0433_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1136",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50010M0433_1900_-NONE-_-NONE- (misc_guatemala_milgp_generators_35k_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50010M0433_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_milgp_generators_35k_2010 USD 0.035m. Supports misc_guatemala_milgp_generators_35k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 34884.59; date_signed 2010-09-30.",
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
