#!/usr/bin/env python3
"""Cycles 1186–1188: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262186–20262188. Thin top-up dry.
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


# === Cycle 1186 (seed 20262186) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "fabrication_designs_brazil_metal_door_screen_frame_13k_2024",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Brazil metal door screen frame for international embassies",
    "Brazil",
    "5 Jun 2024: Department of State awards contract 19AQMM24P0509 to Fabrication Designs, Inc. for metal door screen frame etc. for international embassies (PoP Brazil); obligated USD 13,219.19. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "13219.19", "2024-06-05", "2024", "", "",
    "Metal door screen frame etc. for international embassies, Brazil (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_fabrication_designs_brazil_metal_door_screen_frame_13k_2024",
    "METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0509_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1186",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0509_1900_-NONE-_-NONE- (fabrication_designs_brazil_metal_door_screen_frame_13k_2024). Signed 2024-06-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0509_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_brazil_metal_door_screen_frame_13k_2024 USD 0.013m. Supports fabrication_designs_brazil_metal_door_screen_frame_13k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13219.19; date_signed 2024-06-05.",
)
row_doc(
    "norshield_brazil_metal_door_steel_embassies_13k_2024",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Brazil metal door steel for international embassies",
    "Brazil",
    "11 Jan 2024: Department of State awards contract 19AQMM24P0142 to Norshield Security Products, LLC for metal door steel etc. for international embassies (PoP Brazil); obligated USD 12,600.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "12600", "2024-01-11", "2024", "", "",
    "Metal door steel etc. for international embassies, Brazil (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_brazil_metal_door_steel_embassies_13k_2024",
    "METAL DOOR STEEL ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0142_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1186",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0142_1900_-NONE-_-NONE- (norshield_brazil_metal_door_steel_embassies_13k_2024). Signed 2024-01-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0142_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_brazil_metal_door_steel_embassies_13k_2024 USD 0.013m. Supports norshield_brazil_metal_door_steel_embassies_13k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12600.0; date_signed 2024-01-11.",
)
row_doc(
    "misc_chile_grills_installation_14k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Chile grills installation",
    "Chile",
    "30 Nov 2018: Department of State awards contract 19C18019P0102 for grills installation (PoP Chile); obligated USD 14,025.84. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14025.84", "2018-11-30", "2018", "", "",
    "Grills installation, Chile (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_chile_grills_installation_14k_2018",
    "GRILLS INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18019P0102_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1186",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C18019P0102_1900_-NONE-_-NONE- (misc_chile_grills_installation_14k_2018). Signed 2018-11-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C18019P0102_1900_-NONE-_-NONE-/.",
    "USASpending: misc_chile_grills_installation_14k_2018 USD 0.014m. Supports misc_chile_grills_installation_14k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14025.84; date_signed 2018-11-30.",
)
row_doc(
    "misc_costa_rica_compstat_network_cabling_14k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Costa Rica INL Merida network cabling for CompStat project",
    "Costa Rica",
    "10 Aug 2012: Department of State awards contract SCS80012M0667 for INL/Merida network cabling for the CompStat project (PoP Costa Rica); obligated USD 14,046.16. CapEx face = award obligation. CompStat project named; site coords not stated — lat/lon blank.",
    "14046.16", "2012-08-10", "2012", "", "",
    "Network cabling for CompStat project, Costa Rica (USASpending description; CompStat named, site coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_compstat_network_cabling_14k_2012",
    "INL/MERIDA-IN13CRM3 NETWORK CABLING FOR THE COPMSTAT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80012M0667_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1186",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80012M0667_1900_-NONE-_-NONE- (misc_costa_rica_compstat_network_cabling_14k_2012). Signed 2012-08-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80012M0667_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_compstat_network_cabling_14k_2012 USD 0.014m. Supports misc_costa_rica_compstat_network_cabling_14k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14046.16; date_signed 2012-08-10.",
)
row_doc(
    "misc_guatemala_30_network_drops_install_14k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guatemala installation of 30 network drops",
    "Guatemala",
    "28 Sep 2017: Department of State awards contract SGT50017M0944 for installation of 30 network drops (PoP Guatemala); obligated USD 14,093.78. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14093.78", "2017-09-28", "2017", "", "",
    "Installation of 30 network drops, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guatemala_30_network_drops_install_14k_2017",
    "IGF::CL::IGF INSTALLATION 30 NETWORK DROPS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50017M0944_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1186",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50017M0944_1900_-NONE-_-NONE- (misc_guatemala_30_network_drops_install_14k_2017). Signed 2017-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50017M0944_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_30_network_drops_install_14k_2017 USD 0.014m. Supports misc_guatemala_30_network_drops_install_14k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14093.78; date_signed 2017-09-28.",
)

# === Cycle 1187 (seed 20262187) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "harden_belize_metal_door_screen_13k_2022",
    "infrastructure", "building_materials", "us",
    "Harden Architectural Security Products — Belize metal door screen for international embassies",
    "Belize",
    "13 Jul 2022: Department of State awards contract 19AQMM22P0819 to Harden Architectural Security Products, LLC for metal door screen etc. for international embassies (PoP Belize); obligated USD 12,580.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "12580", "2022-07-13", "2022", "", "",
    "Metal door screen etc. for international embassies, Belize (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_harden_belize_metal_door_screen_13k_2022",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0819_1900_-NONE-_-NONE-/",
    "Actor: HARDEN ARCHITECTURAL SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1187",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22P0819_1900_-NONE-_-NONE- (harden_belize_metal_door_screen_13k_2022). Signed 2022-07-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0819_1900_-NONE-_-NONE-/.",
    "USASpending: harden_belize_metal_door_screen_13k_2022 USD 0.013m. Supports harden_belize_metal_door_screen_13k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12580.0; date_signed 2022-07-13.",
)
row_doc(
    "hy_security_el_salvador_replacement_gate_drivers_12k_2011",
    "infrastructure", "building_materials", "us",
    "Hy-Security Gate — El Salvador replacement gate drivers",
    "El Salvador",
    "13 Jun 2011: Department of State awards contract SES60011M0570 to Hy-Security Gate, Inc. for replacement gate drivers (PoP El Salvador); obligated USD 12,327.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "12327", "2011-06-13", "2011", "", "",
    "Replacement gate drivers, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_hy_security_el_salvador_replacement_gate_drivers_12k_2011",
    "7901- REPLACEMENT GATE DRIVERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60011M0570_1900_-NONE-_-NONE-/",
    "Actor: HY-SECURITY GATE, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1187",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60011M0570_1900_-NONE-_-NONE- (hy_security_el_salvador_replacement_gate_drivers_12k_2011). Signed 2011-06-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60011M0570_1900_-NONE-_-NONE-/.",
    "USASpending: hy_security_el_salvador_replacement_gate_drivers_12k_2011 USD 0.012m. Supports hy_security_el_salvador_replacement_gate_drivers_12k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 12327.0; date_signed 2011-06-13.",
)
row_doc(
    "misc_dominican_republic_kim_gutierrez_generator_tank_14k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic DHS/CBP generator and tank Kim Gutierrez",
    "Dominican Republic",
    "23 Jan 2013: Department of State awards contract SDR86013M0500 for DHS/CBP generator and tank Kim Gutierrez (PoP Dominican Republic); obligated USD 14,059.06. CapEx face = award obligation. Kim Gutierrez named; site coords not stated — lat/lon blank.",
    "14059.06", "2013-01-23", "2013", "", "",
    "Generator and tank Kim Gutierrez, Dominican Republic (USASpending description; named site, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_republic_kim_gutierrez_generator_tank_14k_2013",
    "DHS/CBP GENERATOR AND TANK KIM GUTIERREZ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86013M0500_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1187",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86013M0500_1900_-NONE-_-NONE- (misc_dominican_republic_kim_gutierrez_generator_tank_14k_2013). Signed 2013-01-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86013M0500_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_republic_kim_gutierrez_generator_tank_14k_2013 USD 0.014m. Supports misc_dominican_republic_kim_gutierrez_generator_tank_14k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14059.06; date_signed 2013-01-23.",
)
row_doc(
    "misc_guatemala_emergency_generators_preheaters_14k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Guatemala emergency generators pre-heaters",
    "Guatemala",
    "1 Mar 2024: Department of State awards contract 19GT5024P0366 for emergency generators pre-heaters (PoP Guatemala); obligated USD 14,091.59. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14091.59", "2024-03-01", "2024", "", "",
    "Emergency generators pre-heaters, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guatemala_emergency_generators_preheaters_14k_2024",
    "EMERGENCY GENERATORS PRE-HEATERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5024P0366_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1187",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GT5024P0366_1900_-NONE-_-NONE- (misc_guatemala_emergency_generators_preheaters_14k_2024). Signed 2024-03-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5024P0366_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_emergency_generators_preheaters_14k_2024 USD 0.014m. Supports misc_guatemala_emergency_generators_preheaters_14k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14091.59; date_signed 2024-03-01.",
)
row_doc(
    "misc_mexico_cdj_metallic_structure_fence_cabinets_14k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Ciudad Juarez paint metallic structure fence and cabinets",
    "Mexico",
    "16 May 2016: Department of State awards contract SMX11516M0164 for CDJ paint metallic structure, fence and cabinets (PoP Mexico); obligated USD 14,178.81. CapEx face = award obligation. Ciudad Juarez named; site coords not stated — lat/lon blank.",
    "14178.81", "2016-05-16", "2016", "", "",
    "Metallic structure fence and cabinets, Ciudad Juarez, Mexico (USASpending description; Ciudad Juarez named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_cdj_metallic_structure_fence_cabinets_14k_2016",
    "7901 CDJ-PAINT METALIC STRUCTURE, FENCE ANDCABINETS PROP 1000 IGF::OT::IGF - FOR OTHER FUNCTIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516M0164_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1187",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11516M0164_1900_-NONE-_-NONE- (misc_mexico_cdj_metallic_structure_fence_cabinets_14k_2016). Signed 2016-05-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11516M0164_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_cdj_metallic_structure_fence_cabinets_14k_2016 USD 0.014m. Supports misc_mexico_cdj_metallic_structure_fence_cabinets_14k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14178.81; date_signed 2016-05-16.",
)

# === Cycle 1188 (seed 20262188) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "ross_technology_mexico_metal_door_screen_12k_2020",
    "infrastructure", "building_materials", "us",
    "Ross Technology — Mexico metal door screen",
    "Mexico",
    "2 Jun 2020: Department of State awards contract 19AQMM20P0945 to Ross Technology Company for metal door screen etc. (PoP Mexico); obligated USD 11,806.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "11806", "2020-06-02", "2020", "", "",
    "Metal door screen etc., Mexico (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_ross_technology_mexico_metal_door_screen_12k_2020",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0945_1900_-NONE-_-NONE-/",
    "Actor: ROSS TECHNOLOGY COMPANY (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1188",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20P0945_1900_-NONE-_-NONE- (ross_technology_mexico_metal_door_screen_12k_2020). Signed 2020-06-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0945_1900_-NONE-_-NONE-/.",
    "USASpending: ross_technology_mexico_metal_door_screen_12k_2020 USD 0.012m. Supports ross_technology_mexico_metal_door_screen_12k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11806.0; date_signed 2020-06-02.",
)
row_doc(
    "norshield_brazil_metal_door_steel_frame_embassies_12k_2024",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Brazil metal door steel frame for international embassies",
    "Brazil",
    "1 Aug 2024: Department of State awards contract 19AQMM24P0731 to Norshield Security Products, LLC for metal door steel frame for international embassies (PoP Brazil); obligated USD 11,625.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "11625", "2024-08-01", "2024", "", "",
    "Metal door steel frame for international embassies, Brazil (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_brazil_metal_door_steel_frame_embassies_12k_2024",
    "METAL DOOR STEEL FRAME FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0731_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1188",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0731_1900_-NONE-_-NONE- (norshield_brazil_metal_door_steel_frame_embassies_12k_2024). Signed 2024-08-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0731_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_brazil_metal_door_steel_frame_embassies_12k_2024 USD 0.012m. Supports norshield_brazil_metal_door_steel_frame_embassies_12k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11625.0; date_signed 2024-08-01.",
)
row_doc(
    "misc_mexico_plumbing_flush_valves_replace_14k_2019",
    "infrastructure", "water", "other",
    "Miscellaneous foreign awardees — Mexico replacement of plumbing flush valves",
    "Mexico",
    "4 Apr 2019: Department of State awards contract 19MX5319P0614 for replacement of plumbing flush valves (PoP Mexico); obligated USD 14,171.16. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14171.16", "2019-04-04", "2019", "", "",
    "Replacement of plumbing flush valves, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_plumbing_flush_valves_replace_14k_2019",
    "MX-FAC-OBO-REPLACEMENT OF PLUMBING FLUSH VALVES-FY19",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319P0614_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1188",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5319P0614_1900_-NONE-_-NONE- (misc_mexico_plumbing_flush_valves_replace_14k_2019). Signed 2019-04-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5319P0614_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_plumbing_flush_valves_replace_14k_2019 USD 0.014m. Supports misc_mexico_plumbing_flush_valves_replace_14k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14171.16; date_signed 2019-04-04.",
)
row_doc(
    "misc_brazil_residential_security_alarm_receiver_14k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil alarm receiver for residential security program",
    "Brazil",
    "26 Jul 2016: Department of State awards contract SBR25016M1365 for alarm receiver for residential security program (PoP Brazil); obligated USD 14,022.67. CapEx face = award obligation. Residences unnamed — lat/lon blank.",
    "14022.67", "2016-07-26", "2016", "", "",
    "Alarm receiver for residential security program, Brazil (USASpending description; residences unnamed — lat/lon blank).",
    "usaspending_misc_brazil_residential_security_alarm_receiver_14k_2016",
    "ALARM RECEIVER FOR RESIDENTIAL SECURITY PROGRAM \"IGF::OT::IGF\"",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25016M1365_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1188",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25016M1365_1900_-NONE-_-NONE- (misc_brazil_residential_security_alarm_receiver_14k_2016). Signed 2016-07-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25016M1365_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_residential_security_alarm_receiver_14k_2016 USD 0.014m. Supports misc_brazil_residential_security_alarm_receiver_14k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14022.67; date_signed 2016-07-26.",
)
row_doc(
    "misc_brazil_obo651_apartment_make_ready_commissioning_14k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil commissioning services for OBO651 apartment make ready",
    "Brazil",
    "1 Dec 2023: Department of State awards contract 19BR9324P0044 for commissioning services for OBO651 apartment make ready (PoP Brazil); obligated USD 14,077.08. CapEx face = award obligation. OBO651 named; site coords not stated — lat/lon blank.",
    "14077.08", "2023-12-01", "2023", "", "",
    "Commissioning/make-ready for OBO651 apartment, Brazil (USASpending description; OBO651 named, site coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_obo651_apartment_make_ready_commissioning_14k_2023",
    "COMMISSIONING SERVICES FOR OBO651 - APARTMENT MAKE READY (PAINTING, HYDRAULIC, ELECTRICAL, WOODWORKING SERVICES AND ETC).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9324P0044_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1188",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9324P0044_1900_-NONE-_-NONE- (misc_brazil_obo651_apartment_make_ready_commissioning_14k_2023). Signed 2023-12-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9324P0044_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_obo651_apartment_make_ready_commissioning_14k_2023 USD 0.014m. Supports misc_brazil_obo651_apartment_make_ready_commissioning_14k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14077.08; date_signed 2023-12-01.",
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
