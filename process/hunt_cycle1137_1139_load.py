#!/usr/bin/env python3
"""Cycles 1137–1139: USASpending LatAm CapEx residual (~USD0.011–0.035m).

Seeds: 20262137–20262139. Thin top-up dry.
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


# === Cycle 1137 (seed 20262137) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "greener_concepts_colombia_icass_playground_equipment_35k_2015",
    "infrastructure", "building_materials", "us",
    "Greener Concepts — Colombia ICASS playground equipment",
    "Colombia",
    "23 Sep 2015: Department of State awards contract SCO20015M1547 to Greener Concepts, LLC for EOFY 15 ICASS playground equipment (PoP Colombia); obligated USD 34,999.45. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "34999.45", "2015-09-23", "2015", "", "",
    "ICASS playground equipment, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_greener_concepts_colombia_icass_playground_equipment_35k_2015",
    "IGF::OT::IGF EOFY 15_ICASS_PLAYGROUND EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20015M1547_1900_-NONE-_-NONE-/",
    "Actor: Greener Concepts, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1137",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20015M1547_1900_-NONE-_-NONE- (greener_concepts_colombia_icass_playground_equipment_35k_2015). Signed 2015-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20015M1547_1900_-NONE-_-NONE-/.",
    "USASpending: greener_concepts_colombia_icass_playground_equipment_35k_2015 USD 0.035m. Supports greener_concepts_colombia_icass_playground_equipment_35k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 34999.45; date_signed 2015-09-23.",
)
row_doc(
    "critical_power_colombia_electrical_generator_30kva_20k_2012",
    "energy", "power_plants_grid", "us",
    "Critical Power Solutions — Colombia electrical generator 30kVA",
    "Colombia",
    "27 Aug 2012: Department of Defense awards contract W913FT12P0310 to Critical Power Solutions, LLC for generator, electrical 30kVA shipping (PoP Colombia); obligated USD 19,882.75. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "19882.75", "2012-08-27", "2012", "", "",
    "Electrical generator 30kVA, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_critical_power_colombia_electrical_generator_30kva_20k_2012",
    "GENERATOR, ELECTRICAL 30KVA SHIPPING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0310_9700_-NONE-_-NONE-/",
    "Actor: Critical Power Solutions, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1137",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12P0310_9700_-NONE-_-NONE- (critical_power_colombia_electrical_generator_30kva_20k_2012). Signed 2012-08-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0310_9700_-NONE-_-NONE-/.",
    "USASpending: critical_power_colombia_electrical_generator_30kva_20k_2012 USD 0.020m. Supports critical_power_colombia_electrical_generator_30kva_20k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19882.75; date_signed 2012-08-27.",
)
row_doc(
    "misc_el_salvador_iml_air_conditioners_20k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — El Salvador INL air conditioners for medical examiners office (IML)",
    "El Salvador",
    "30 Aug 2024: Department of State awards contract 19ES6024P1096 for INL air conditioners for medical examiners office (IML) (PoP El Salvador); obligated USD 19,868.39. CapEx face = award obligation. IML named; site coords not stated — lat/lon blank.",
    "19868.39", "2024-08-30", "2024", "", "",
    "INL air conditioners for medical examiners office (IML), El Salvador (USASpending description; IML named, site coords not stated — lat/lon blank).",
    "usaspending_misc_el_salvador_iml_air_conditioners_20k_2024",
    "INL - AIR CONDITIONERS FOR MEDICAL EXAMINERS OFFICE (IML)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6024P1096_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1137",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6024P1096_1900_-NONE-_-NONE- (misc_el_salvador_iml_air_conditioners_20k_2024). Signed 2024-08-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6024P1096_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_iml_air_conditioners_20k_2024 USD 0.020m. Supports misc_el_salvador_iml_air_conditioners_20k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19868.39; date_signed 2024-08-30.",
)
row_doc(
    "misc_bahamas_nec_anti_climb_gate_system_35k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas NEC anti-climb gate system",
    "Bahamas",
    "22 Jul 2025: Department of State awards contract 19BF5025P0556 for NEC anti-climb gate system (PoP Bahamas); obligated USD 34,774. CapEx face = award obligation. Exact NEC unnamed — lat/lon blank.",
    "34774", "2025-07-22", "2025", "", "",
    "NEC anti-climb gate system, Bahamas (USASpending description; NEC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_bahamas_nec_anti_climb_gate_system_35k_2025",
    "7112 - NEC ANTI-CLIMB GATE SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5025P0556_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1137",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BF5025P0556_1900_-NONE-_-NONE- (misc_bahamas_nec_anti_climb_gate_system_35k_2025). Signed 2025-07-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5025P0556_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_nec_anti_climb_gate_system_35k_2025 USD 0.035m. Supports misc_bahamas_nec_anti_climb_gate_system_35k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 34774; date_signed 2025-07-22.",
)
row_doc(
    "misc_guatemala_canopy_roof_sheets_replacement_20k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guatemala canopy roof sheets replacements",
    "Guatemala",
    "8 May 2013: Department of State awards contract SGT50013M0267 for FM canopy roof sheets replacements - OS (PoP Guatemala); obligated USD 19,885.36. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "19885.36", "2013-05-08", "2013", "", "",
    "Canopy roof sheets replacements, Guatemala (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_guatemala_canopy_roof_sheets_replacement_20k_2013",
    "FM - CANOPY ROOF SHEETS REPLACEMENTS - OS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50013M0267_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1137",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50013M0267_1900_-NONE-_-NONE- (misc_guatemala_canopy_roof_sheets_replacement_20k_2013). Signed 2013-05-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50013M0267_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_canopy_roof_sheets_replacement_20k_2013 USD 0.020m. Supports misc_guatemala_canopy_roof_sheets_replacement_20k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19885.36; date_signed 2013-05-08.",
)

# === Cycle 1138 (seed 20262138) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "applied_security_brazil_recife_tss_installation_35k_2012",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Brazil Recife technical security services installation",
    "Brazil",
    "15 Sep 2012: Department of State awards contract SAQMMA12F3867 to Applied Security Technologies Inc for technical security services Recife, Brazil installation (PoP Brazil); obligated USD 34,952.39. CapEx face = award obligation. Recife named; site coords not stated — lat/lon blank.",
    "34952.39", "2012-09-15", "2012", "", "",
    "Technical security services installation, Recife, Brazil (USASpending description; Recife named, site coords not stated — lat/lon blank).",
    "usaspending_applied_security_brazil_recife_tss_installation_35k_2012",
    "TECHNICAL SECURITY SERVICES RECIFE, BRAZIL INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F3867_1900_SAQMMA07D0030_1900/",
    "Actor: Applied Security Technologies Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1138",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F3867_1900_SAQMMA07D0030_1900 (applied_security_brazil_recife_tss_installation_35k_2012). Signed 2012-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F3867_1900_SAQMMA07D0030_1900/.",
    "USASpending: applied_security_brazil_recife_tss_installation_35k_2012 USD 0.035m. Supports applied_security_brazil_recife_tss_installation_35k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 34952.39; date_signed 2012-09-15.",
)
row_doc(
    "harden_suriname_metal_door_screen_17k_2024",
    "infrastructure", "building_materials", "us",
    "Harden Architectural Security Products — Suriname metal door screen for international embassies",
    "Suriname",
    "20 Dec 2024: Department of State awards contract 19AQMM25P0213 to Harden Architectural Security Products, LLC for metal door screen frame etc. for international embassies (PoP Suriname); obligated USD 16,885. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "16885", "2024-12-20", "2024", "", "",
    "Metal door screen frame etc. for international embassies, Suriname (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_harden_suriname_metal_door_screen_17k_2024",
    "METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0213_1900_-NONE-_-NONE-/",
    "Actor: Harden Architectural Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1138",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0213_1900_-NONE-_-NONE- (harden_suriname_metal_door_screen_17k_2024). Signed 2024-12-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0213_1900_-NONE-_-NONE-/.",
    "USASpending: harden_suriname_metal_door_screen_17k_2024 USD 0.017m. Supports harden_suriname_metal_door_screen_17k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 16885; date_signed 2024-12-20.",
)
row_doc(
    "misc_guatemala_cmr_air_conditioning_system_35k_2020",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Guatemala air conditioning system for CMR",
    "Guatemala",
    "3 Sep 2020: Department of State awards contract 19GT5020P0435 for air conditioning system for CMR (PoP Guatemala); obligated USD 34,812.18. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.",
    "34812.18", "2020-09-03", "2020", "", "",
    "Air conditioning system for CMR, Guatemala (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_guatemala_cmr_air_conditioning_system_35k_2020",
    "AIR CONDITIONING SYSTEM FOR CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5020P0435_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1138",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GT5020P0435_1900_-NONE-_-NONE- (misc_guatemala_cmr_air_conditioning_system_35k_2020). Signed 2020-09-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5020P0435_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_cmr_air_conditioning_system_35k_2020 USD 0.035m. Supports misc_guatemala_cmr_air_conditioning_system_35k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 34812.18; date_signed 2020-09-03.",
)
row_doc(
    "misc_mexico_puebla_tv_aluminum_windows_doors_20k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico aluminum windows and doors for Puebla TV",
    "Mexico",
    "4 Jun 2013: Department of State awards contract SMX90013M0262 for INL-IN41MX72 aluminum windows and doors for Puebla TV (PoP Mexico); obligated USD 19,875.05. CapEx face = award obligation. Puebla TV named; site coords not stated — lat/lon blank.",
    "19875.05", "2013-06-04", "2013", "", "",
    "Aluminum windows and doors for Puebla TV, Mexico (USASpending description; Puebla TV named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_puebla_tv_aluminum_windows_doors_20k_2013",
    "INL-IN41MX72- ALUMINUM WINDOWS AND DOORS FOR PUEBLA TV",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX90013M0262_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1138",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX90013M0262_1900_-NONE-_-NONE- (misc_mexico_puebla_tv_aluminum_windows_doors_20k_2013). Signed 2013-06-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX90013M0262_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_puebla_tv_aluminum_windows_doors_20k_2013 USD 0.020m. Supports misc_mexico_puebla_tv_aluminum_windows_doors_20k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19875.05; date_signed 2013-06-04.",
)
row_doc(
    "misc_peru_power_stabilizer_transformer_17k_2019",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Peru power stabilizer with transformer",
    "Peru",
    "27 Sep 2019: Department of Defense awards contract N4485219P0285 for power stabilizer, transformer included (PoP Peru); obligated USD 16,984.92. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "16984.92", "2019-09-27", "2019", "", "",
    "Power stabilizer with transformer, Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_peru_power_stabilizer_transformer_17k_2019",
    "POWER STABILIZER, TRANSFORMER INCLUDED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N4485219P0285_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1138",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N4485219P0285_9700_-NONE-_-NONE- (misc_peru_power_stabilizer_transformer_17k_2019). Signed 2019-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N4485219P0285_9700_-NONE-_-NONE-/.",
    "USASpending: misc_peru_power_stabilizer_transformer_17k_2019 USD 0.017m. Supports misc_peru_power_stabilizer_transformer_17k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 16984.92; date_signed 2019-09-27.",
)

# === Cycle 1139 (seed 20262139) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_nicaragua_security_glazing_ng225_16k_2023",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Nicaragua NG225 security glazing for international embassies",
    "Nicaragua",
    "13 Dec 2023: Department of State awards contract 19AQMM24P0067 to Norshield Security Products, LLC for NG225 security glazing (PoP Nicaragua); obligated USD 15,950. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "15950", "2023-12-13", "2023", "", "",
    "NG225 security glazing for international embassies, Nicaragua (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_nicaragua_security_glazing_ng225_16k_2023",
    "---------- COMMENTS: PROVIDE NG225 SECURITY GLAZING SIZE:23-1/4 X 31-3/8 X 2.25 THK, 91LBS. DOS 1123,W/LOWE UNIT SIZE:23  X 47-1/2 X 2.25 THK, 136LBS, DOS 1123, CLEAR UNIT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0067_1900_-NONE-_-NONE-/",
    "Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1139",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0067_1900_-NONE-_-NONE- (norshield_nicaragua_security_glazing_ng225_16k_2023). Signed 2023-12-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0067_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_nicaragua_security_glazing_ng225_16k_2023 USD 0.016m. Supports norshield_nicaragua_security_glazing_ng225_16k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15950; date_signed 2023-12-13.",
)
row_doc(
    "valkyrie_venezuela_caracas_tss_installation_17k_2012",
    "infrastructure", "building_materials", "us",
    "Valkyrie Enterprises — Venezuela Caracas technical security services installation",
    "Venezuela",
    "8 Aug 2012: Department of State awards contract SAQMMA12F2719 to Valkyrie Enterprises, LLC for technical security services installation Caracas, Venezuela (PoP Venezuela); obligated USD 16,889.19. CapEx face = award obligation. Caracas named; site coords not stated — lat/lon blank.",
    "16889.19", "2012-08-08", "2012", "", "",
    "Technical security services installation, Caracas, Venezuela (USASpending description; Caracas named, site coords not stated — lat/lon blank).",
    "usaspending_valkyrie_venezuela_caracas_tss_installation_17k_2012",
    "TECHNICAL SECURITY SERVICES INSTALLATION CARACAS, VENEZUELA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2719_1900_SAQMMA07D0026_1900/",
    "Actor: Valkyrie Enterprises, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1139",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F2719_1900_SAQMMA07D0026_1900 (valkyrie_venezuela_caracas_tss_installation_17k_2012). Signed 2012-08-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2719_1900_SAQMMA07D0026_1900/.",
    "USASpending: valkyrie_venezuela_caracas_tss_installation_17k_2012 USD 0.017m. Supports valkyrie_venezuela_caracas_tss_installation_17k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 16889.19; date_signed 2012-08-08.",
)
row_doc(
    "misc_costa_rica_inl_annex_126kw_emergency_generator_32k_2019",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Costa Rica INL annex 126kW emergency electric generator",
    "Costa Rica",
    "10 Jan 2019: Department of State awards contract 19CS8019P0224 for INL 1930.0 126kW emergency electric generator, INL annex (PoP Costa Rica); obligated USD 31,972. CapEx face = award obligation. INL annex named; site coords not stated — lat/lon blank.",
    "31972", "2019-01-10", "2019", "", "",
    "126kW emergency electric generator, INL annex, Costa Rica (USASpending description; INL annex named, site coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_inl_annex_126kw_emergency_generator_32k_2019",
    "PR8005115-V2 - INL 1930.0 126KW EMERGENCY ELECTRIC GENERATOR, INL ANNEX",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8019P0224_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1139",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8019P0224_1900_-NONE-_-NONE- (misc_costa_rica_inl_annex_126kw_emergency_generator_32k_2019). Signed 2019-01-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8019P0224_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_inl_annex_126kw_emergency_generator_32k_2019 USD 0.032m. Supports misc_costa_rica_inl_annex_126kw_emergency_generator_32k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 31972; date_signed 2019-01-10.",
)
row_doc(
    "misc_haiti_cas_kitchen_renovation_32k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Haiti CAS kitchen renovation",
    "Haiti",
    "15 Jul 2025: Department of State awards contract 19HA7025P0624 for FAC-CAS kitchen renovation (PoP Haiti); obligated USD 31,970. CapEx face = award obligation. CAS named; site coords not stated — lat/lon blank.",
    "31970", "2025-07-15", "2025", "", "",
    "CAS kitchen renovation, Haiti (USASpending description; CAS named, site coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_cas_kitchen_renovation_32k_2025",
    "FAC-CAS KITCHEN RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7025P0624_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1139",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7025P0624_1900_-NONE-_-NONE- (misc_haiti_cas_kitchen_renovation_32k_2025). Signed 2025-07-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7025P0624_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_cas_kitchen_renovation_32k_2025 USD 0.032m. Supports misc_haiti_cas_kitchen_renovation_32k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 31970; date_signed 2025-07-15.",
)
row_doc(
    "misc_mexico_hmo_low_voltage_diesel_standby_generators_32k_2018",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico Hermosillo low voltage diesel standby generators",
    "Mexico",
    "14 Sep 2018: Department of State awards contract 19MX5718P0163 for HMO-BME 7901 contract low voltage diesel standby generators (PoP Mexico); obligated USD 31,962.23. CapEx face = award obligation. Hermosillo (HMO) named; site coords not stated — lat/lon blank.",
    "31962.23", "2018-09-14", "2018", "", "",
    "Low voltage diesel standby generators, Hermosillo, Mexico (USASpending description; HMO named, site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_hmo_low_voltage_diesel_standby_generators_32k_2018",
    "HMO-BME:7901/CONTRACT LOW VOLTAGE DIESEL STANDBY GENERATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5718P0163_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1139",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5718P0163_1900_-NONE-_-NONE- (misc_mexico_hmo_low_voltage_diesel_standby_generators_32k_2018). Signed 2018-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5718P0163_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_hmo_low_voltage_diesel_standby_generators_32k_2018 USD 0.032m. Supports misc_mexico_hmo_low_voltage_diesel_standby_generators_32k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 31962.23; date_signed 2018-09-14.",
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
