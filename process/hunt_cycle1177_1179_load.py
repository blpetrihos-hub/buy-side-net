#!/usr/bin/env python3
"""Cycles 1177–1179: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262177–20262179. Thin top-up dry.
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


# === Cycle 1177 (seed 20262177) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "bcs_usa_haiti_pap_irm_ups_18k_2023",
    "energy", "power_plants_grid", "us",
    "BCS USA — Haiti PAP-IRM uninterruptible power supply UPS",
    "Haiti",
    "19 Dec 2023: Department of State awards contract 19HA7024P0058 to BCS USA Inc for PAP-IRM uninterruptible power supply (UPS) (PoP Haiti); obligated USD 17,860.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "17860", "2023-12-19", "2023", "", "",
    "PAP-IRM UPS, Haiti (USASpending description; site not named — lat/lon blank).",
    "usaspending_bcs_usa_haiti_pap_irm_ups_18k_2023",
    "PAP-IRM UNINTERRUPTIBLE POWER SUPPLY (UPS)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7024P0058_1900_-NONE-_-NONE-/",
    "Actor: BCS USA INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1177",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7024P0058_1900_-NONE-_-NONE- (bcs_usa_haiti_pap_irm_ups_18k_2023). Signed 2023-12-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7024P0058_1900_-NONE-_-NONE-/.",
    "USASpending: bcs_usa_haiti_pap_irm_ups_18k_2023 USD 0.018m. Supports bcs_usa_haiti_pap_irm_ups_18k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 17860.0; date_signed 2023-12-19.",
)
row_doc(
    "hy_security_brazil_cac_sliding_gate_driver_replace_18k_2015",
    "infrastructure", "building_materials", "us",
    "Hy-Security Gate — Brazil replacement driver for CAC sliding gates",
    "Brazil",
    "31 Aug 2015: Department of State awards contract SBR25015M1585 to Hy-Security Gate, Inc. for replacement driver for CAC sliding gates (PoP Brazil); obligated USD 17,573.0. CapEx face = award obligation. CAC named; site coords not stated — lat/lon blank.",
    "17573", "2015-08-31", "2015", "", "",
    "Replacement driver for CAC sliding gates, Brazil (USASpending description; CAC named, site coords not stated — lat/lon blank).",
    "usaspending_hy_security_brazil_cac_sliding_gate_driver_replace_18k_2015",
    "REPLACEMENT DRIVER FOR CAC SLIDING GATES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25015M1585_1900_-NONE-_-NONE-/",
    "Actor: HY-SECURITY GATE, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1177",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25015M1585_1900_-NONE-_-NONE- (hy_security_brazil_cac_sliding_gate_driver_replace_18k_2015). Signed 2015-08-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25015M1585_1900_-NONE-_-NONE-/.",
    "USASpending: hy_security_brazil_cac_sliding_gate_driver_replace_18k_2015 USD 0.018m. Supports hy_security_brazil_cac_sliding_gate_driver_replace_18k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 17573.0; date_signed 2015-08-31.",
)
row_doc(
    "misc_guatemala_chancery_stairs_handrails_14k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guatemala new handrails for chancery stairs",
    "Guatemala",
    "31 Jul 2012: Department of State awards contract SGT50012C0007 for new handrails for chancery stairs (PoP Guatemala); obligated USD 14,310.28. CapEx face = award obligation. Chancery named; site coords not stated — lat/lon blank.",
    "14310.28", "2012-07-31", "2012", "", "",
    "New handrails for chancery stairs, Guatemala (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_misc_guatemala_chancery_stairs_handrails_14k_2012",
    "FM - NEW HANDRAILS FOR CHANCERY STAIRS - OS AS PER SOW INCLUDED IN THE CONTACT - SGT50012C0007",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50012C0007_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1177",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50012C0007_1900_-NONE-_-NONE- (misc_guatemala_chancery_stairs_handrails_14k_2012). Signed 2012-07-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50012C0007_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_chancery_stairs_handrails_14k_2012 USD 0.014m. Supports misc_guatemala_chancery_stairs_handrails_14k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14310.28; date_signed 2012-07-31.",
)
row_doc(
    "misc_belize_inl_police_stations_air_conditioners_14k_2015",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Belize INL air conditioners for police stations",
    "Belize",
    "30 Jul 2015: Department of State awards contract SBH20015M0242 for INLBMP air conditioners for police stations (PoP Belize); obligated USD 14,301.75. CapEx face = award obligation. Police stations unnamed — lat/lon blank.",
    "14301.75", "2015-07-30", "2015", "", "",
    "Air conditioners for police stations, Belize (USASpending description; stations unnamed — lat/lon blank).",
    "usaspending_misc_belize_inl_police_stations_air_conditioners_14k_2015",
    "IGF::OT::IGF - INLBMP- AIR CONDITIONERS FOR POLICE STATIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20015M0242_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1177",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20015M0242_1900_-NONE-_-NONE- (misc_belize_inl_police_stations_air_conditioners_14k_2015). Signed 2015-07-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20015M0242_1900_-NONE-_-NONE-/.",
    "USASpending: misc_belize_inl_police_stations_air_conditioners_14k_2015 USD 0.014m. Supports misc_belize_inl_police_stations_air_conditioners_14k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14301.75; date_signed 2015-07-30.",
)
row_doc(
    "misc_el_salvador_emergency_cut_off_switch_supply_install_14k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — El Salvador supply and installation of emergency cut off switch",
    "El Salvador",
    "23 Sep 2011: Department of State awards contract SES60011M1124 for supply and installation of emergency cut off switch (PoP El Salvador); obligated USD 14,300.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14300", "2011-09-23", "2011", "", "",
    "Supply and installation of emergency cut off switch, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_el_salvador_emergency_cut_off_switch_supply_install_14k_2011",
    "SUPPLY AND INSTALLATION OF EMERGENCY CUT OFF SWITCH",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60011M1124_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1177",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60011M1124_1900_-NONE-_-NONE- (misc_el_salvador_emergency_cut_off_switch_supply_install_14k_2011). Signed 2011-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60011M1124_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_emergency_cut_off_switch_supply_install_14k_2011 USD 0.014m. Supports misc_el_salvador_emergency_cut_off_switch_supply_install_14k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14300.0; date_signed 2011-09-23.",
)

# === Cycle 1178 (seed 20262178) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_nicaragua_metal_door_steel_17k_2020",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Nicaragua metal door steel",
    "Nicaragua",
    "11 May 2020: Department of State awards contract 19AQMM20P0837 to Norshield Security Products, LLC for metal door steel etc. (PoP Nicaragua); obligated USD 17,410.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "17410", "2020-05-11", "2020", "", "",
    "Metal door steel etc., Nicaragua (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_nicaragua_metal_door_steel_17k_2020",
    "METAL DOOR STEEL ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0837_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1178",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20P0837_1900_-NONE-_-NONE- (norshield_nicaragua_metal_door_steel_17k_2020). Signed 2020-05-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0837_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_nicaragua_metal_door_steel_17k_2020 USD 0.017m. Supports norshield_nicaragua_metal_door_steel_17k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 17410.0; date_signed 2020-05-11.",
)
row_doc(
    "norshield_nicaragua_metal_fire_door_17k_2015",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Nicaragua metal door fire door",
    "Nicaragua",
    "8 Apr 2015: Department of State awards contract SAQMMA15M0850 to Norshield Security Products, LLC for metal door, fire door etc. (PoP Nicaragua); obligated USD 17,290.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "17290", "2015-04-08", "2015", "", "",
    "Metal door, fire door etc., Nicaragua (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_nicaragua_metal_fire_door_17k_2015",
    "METAL DOOR, FIRE DOOR ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15M0850_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1178",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15M0850_1900_-NONE-_-NONE- (norshield_nicaragua_metal_fire_door_17k_2015). Signed 2015-04-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15M0850_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_nicaragua_metal_fire_door_17k_2015 USD 0.017m. Supports norshield_nicaragua_metal_fire_door_17k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 17290.0; date_signed 2015-04-08.",
)
row_doc(
    "misc_panama_fac_circuit_breaker_replace_14k_2010",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Panama replacement of circuit breaker for FAC",
    "Panama",
    "13 Aug 2010: Department of State awards contract SPM07010M0520 for replacement of circuit breaker for FAC (PoP Panama); obligated USD 14,291.16. CapEx face = award obligation. FAC named; site coords not stated — lat/lon blank.",
    "14291.16", "2010-08-13", "2010", "", "",
    "Replacement of circuit breaker for FAC, Panama (USASpending description; FAC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_panama_fac_circuit_breaker_replace_14k_2010",
    "REPLACEMENT OF CIRCUIT BREAKER FOR FAC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07010M0520_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1178",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07010M0520_1900_-NONE-_-NONE- (misc_panama_fac_circuit_breaker_replace_14k_2010). Signed 2010-08-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07010M0520_1900_-NONE-_-NONE-/.",
    "USASpending: misc_panama_fac_circuit_breaker_replace_14k_2010 USD 0.014m. Supports misc_panama_fac_circuit_breaker_replace_14k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14291.16; date_signed 2010-08-13.",
)
row_doc(
    "misc_trinidad_pinehurst_mlo_housing_commissioning_upgrades_14k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Trinidad and Tobago MLO housing commissioning upgrades 45 Pinehurst Dr",
    "Trinidad and Tobago",
    "29 Aug 2024: Department of State awards contract 19TD5524P0464 for MLO housing commissioning upgrades at 45 Pinehurst Dr. (PoP Trinidad and Tobago); obligated USD 14,279.37. CapEx face = award obligation. 45 Pinehurst Dr named; site coords not stated — lat/lon blank.",
    "14279.37", "2024-08-29", "2024", "", "",
    "MLO housing commissioning upgrades at 45 Pinehurst Dr, Trinidad and Tobago (USASpending description; address named, site coords not stated — lat/lon blank).",
    "usaspending_misc_trinidad_pinehurst_mlo_housing_commissioning_upgrades_14k_2024",
    "MLO HOUSING - COMMISSIONING UPGRADES - 45 PINEHURST DR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5524P0464_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1178",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19TD5524P0464_1900_-NONE-_-NONE- (misc_trinidad_pinehurst_mlo_housing_commissioning_upgrades_14k_2024). Signed 2024-08-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5524P0464_1900_-NONE-_-NONE-/.",
    "USASpending: misc_trinidad_pinehurst_mlo_housing_commissioning_upgrades_14k_2024 USD 0.014m. Supports misc_trinidad_pinehurst_mlo_housing_commissioning_upgrades_14k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14279.37; date_signed 2024-08-29.",
)
row_doc(
    "misc_barbados_residential_security_14k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Barbados residential security",
    "Barbados",
    "28 Jul 2023: Department of State awards contract 19BB2123P0807 for residential security (PoP Barbados); obligated USD 14,220.3. CapEx face = award obligation. Exact residences unnamed — lat/lon blank.",
    "14220.30", "2023-07-28", "2023", "", "",
    "Residential security, Barbados (USASpending description; residences unnamed — lat/lon blank).",
    "usaspending_misc_barbados_residential_security_14k_2023",
    "RESIDENTIAL SECURITY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2123P0807_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1178",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BB2123P0807_1900_-NONE-_-NONE- (misc_barbados_residential_security_14k_2023). Signed 2023-07-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BB2123P0807_1900_-NONE-_-NONE-/.",
    "USASpending: misc_barbados_residential_security_14k_2023 USD 0.014m. Supports misc_barbados_residential_security_14k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14220.3; date_signed 2023-07-28.",
)

# === Cycle 1179 (seed 20262179) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_brazil_metal_door_steel_frame_17k_2024",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Brazil metal door steel frame for international embassies",
    "Brazil",
    "23 Apr 2024: Department of State awards contract 19AQMM24P0410 to Norshield Security Products, LLC for metal door steel frame etc. for international embassies (PoP Brazil); obligated USD 16,600.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "16600", "2024-04-23", "2024", "", "",
    "Metal door steel frame etc. for international embassies, Brazil (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_brazil_metal_door_steel_frame_17k_2024",
    "METAL DOOR STEEL FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0410_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1179",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0410_1900_-NONE-_-NONE- (norshield_brazil_metal_door_steel_frame_17k_2024). Signed 2024-04-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0410_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_brazil_metal_door_steel_frame_17k_2024 USD 0.017m. Supports norshield_brazil_metal_door_steel_frame_17k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 16600.0; date_signed 2024-04-23.",
)
row_doc(
    "fabrication_designs_jamaica_metal_door_screen_frame_16k_2025",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Jamaica metal door screen frame for international embassies",
    "Jamaica",
    "22 Sep 2025: Department of State awards contract 19AQMM25P0422 to Fabrication Designs, Inc. for metal door screen frame etc. for international embassies (PoP Jamaica); obligated USD 16,303.11. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "16303.11", "2025-09-22", "2025", "", "",
    "Metal door screen frame etc. for international embassies, Jamaica (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_fabrication_designs_jamaica_metal_door_screen_frame_16k_2025",
    "METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0422_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1179",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0422_1900_-NONE-_-NONE- (fabrication_designs_jamaica_metal_door_screen_frame_16k_2025). Signed 2025-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0422_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_jamaica_metal_door_screen_frame_16k_2025 USD 0.016m. Supports fabrication_designs_jamaica_metal_door_screen_frame_16k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 16303.11; date_signed 2025-09-22.",
)
row_doc(
    "misc_mexico_cdj_dock_leveler_replace_14k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Ciudad Juarez replacement of dock leveler",
    "Mexico",
    "26 Sep 2014: Department of State awards contract SMX11514M0556 for CDJ replacement of dock leveler prop R1006 (PoP Mexico); obligated USD 14,353.16. CapEx face = award obligation. Ciudad Juarez named; site coords not stated — lat/lon blank.",
    "14353.16", "2014-09-26", "2014", "", "",
    "Replacement of dock leveler, Ciudad Juarez, Mexico (USASpending description; Ciudad Juarez named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_cdj_dock_leveler_replace_14k_2014",
    "CDJ EOY ICASS APROVED-REPLACEMENT OF DOCK LEVELER PROP R1006",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11514M0556_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1179",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX11514M0556_1900_-NONE-_-NONE- (misc_mexico_cdj_dock_leveler_replace_14k_2014). Signed 2014-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX11514M0556_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_cdj_dock_leveler_replace_14k_2014 USD 0.014m. Supports misc_mexico_cdj_dock_leveler_replace_14k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14353.16; date_signed 2014-09-26.",
)
row_doc(
    "misc_brazil_residence_security_door_locks_hinges_14k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil purchase of door locks and hinges for residential security program",
    "Brazil",
    "21 Dec 2016: Department of State awards contract SBR25017M0219 for purchase of door locks and hinges for residential security program (PoP Brazil); obligated USD 14,308.77. CapEx face = award obligation. Residences unnamed — lat/lon blank.",
    "14308.77", "2016-12-21", "2016", "", "",
    "Door locks and hinges for residential security program, Brazil (USASpending description; residences unnamed — lat/lon blank).",
    "usaspending_misc_brazil_residence_security_door_locks_hinges_14k_2016",
    "NOT APPLICABLE PURCHASE OF DOOR LOCKS&HINGES FOR RES SEC PROGRAM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M0219_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1179",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25017M0219_1900_-NONE-_-NONE- (misc_brazil_residence_security_door_locks_hinges_14k_2016). Signed 2016-12-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M0219_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_residence_security_door_locks_hinges_14k_2016 USD 0.014m. Supports misc_brazil_residence_security_door_locks_hinges_14k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14308.77; date_signed 2016-12-21.",
)
row_doc(
    "misc_argentina_workstation_ups_devices_15k_2021",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Argentina workstation UPS devices",
    "Argentina",
    "15 Sep 2021: Department of State awards contract 19AR2021P0886 for workstation UPS devices (PoP Argentina); obligated USD 14,500.04. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14500.04", "2021-09-15", "2021", "", "",
    "Workstation UPS devices, Argentina (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_argentina_workstation_ups_devices_15k_2021",
    "WORKSTATION UPS DEVICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2021P0886_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1179",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2021P0886_1900_-NONE-_-NONE- (misc_argentina_workstation_ups_devices_15k_2021). Signed 2021-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2021P0886_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_workstation_ups_devices_15k_2021 USD 0.015m. Supports misc_argentina_workstation_ups_devices_15k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14500.04; date_signed 2021-09-15.",
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
