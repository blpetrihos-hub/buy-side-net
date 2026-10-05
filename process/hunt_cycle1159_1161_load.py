#!/usr/bin/env python3
"""Cycles 1159–1161: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262159–20262161. Thin top-up dry.
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


# === Cycle 1159 (seed 20262159) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "cummins_haiti_embassy_generator_purchase_install_129k_2019",
    "energy", "power_plants_grid", "us",
    "Cummins Caribbean — Haiti embassy generator purchase and installation",
    "Haiti",
    "3 Sep 2019: Department of State awards contract 19HA7019P0498 to Cummins Caribbean LLC for purchase and installation of new generator for embassy (PoP Haiti); obligated USD 129,311.0. CapEx face = award obligation. Embassy named; site coords not stated — lat/lon blank.",
    "129311", "2019-09-03", "2019", "", "",
    "Embassy generator purchase and installation, Haiti (USASpending description; embassy named in description; site coords not stated — lat/lon blank).",
    "usaspending_cummins_haiti_embassy_generator_purchase_install_129k_2019",
    "PURCHASE AND INSTALLATION OF NEW GENERATOR FOR EMBASSY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7019P0498_1900_-NONE-_-NONE-/",
    "Actor: CUMMINS CARIBBEAN LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1159",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7019P0498_1900_-NONE-_-NONE- (cummins_haiti_embassy_generator_purchase_install_129k_2019). Signed 2019-09-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7019P0498_1900_-NONE-_-NONE-/.",
    "USASpending: cummins_haiti_embassy_generator_purchase_install_129k_2019 USD 0.129m. Supports cummins_haiti_embassy_generator_purchase_install_129k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 129311.0; date_signed 2019-09-03.",
)
row_doc(
    "norshield_panama_metal_door_screen_84k_2022",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Panama metal door screen for international embassies",
    "Panama",
    "16 Nov 2022: Department of State awards contract 19AQMM23P0041 to Norshield Security Products, LLC for metal door screen etc. for international embassies (PoP Panama); obligated USD 84,390.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "84390", "2022-11-16", "2022", "", "",
    "Metal door screen etc. for international embassies, Panama (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_panama_metal_door_screen_84k_2022",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0041_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1159",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23P0041_1900_-NONE-_-NONE- (norshield_panama_metal_door_screen_84k_2022). Signed 2022-11-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0041_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_panama_metal_door_screen_84k_2022 USD 0.084m. Supports norshield_panama_metal_door_screen_84k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 84390.0; date_signed 2022-11-16.",
)
row_doc(
    "misc_costa_rica_fire_control_equipment_install_15k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Costa Rica installation of fire control equipment",
    "Costa Rica",
    "13 Sep 2018: Department of State awards contract 19CS8018P0662 for installation of fire control equipment (PoP Costa Rica); obligated USD 15,000.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "15000", "2018-09-13", "2018", "", "",
    "Installation of fire control equipment, Costa Rica (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_costa_rica_fire_control_equipment_install_15k_2018",
    "INSTALLATION OF FIRE CONTROL EQUIPMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8018P0662_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1159",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8018P0662_1900_-NONE-_-NONE- (misc_costa_rica_fire_control_equipment_install_15k_2018). Signed 2018-09-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8018P0662_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_fire_control_equipment_install_15k_2018 USD 0.015m. Supports misc_costa_rica_fire_control_equipment_install_15k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15000.0; date_signed 2018-09-13.",
)
row_doc(
    "misc_el_salvador_two_75kva_transformers_supply_install_15k_2021",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — El Salvador supply and installation of two 75kVA transformers",
    "El Salvador",
    "17 Nov 2021: Department of State awards contract 19ES6022P0062 for supply and installation of two 75kVA transformers (PoP El Salvador); obligated USD 14,999.61. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14999.61", "2021-11-17", "2021", "", "",
    "Supply and installation of two 75kVA transformers, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_el_salvador_two_75kva_transformers_supply_install_15k_2021",
    "SUPPLY AND INSTALLATION OF TWO 75KVA TRANSFORMERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0062_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1159",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6022P0062_1900_-NONE-_-NONE- (misc_el_salvador_two_75kva_transformers_supply_install_15k_2021). Signed 2021-11-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0062_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_two_75kva_transformers_supply_install_15k_2021 USD 0.015m. Supports misc_el_salvador_two_75kva_transformers_supply_install_15k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14999.61; date_signed 2021-11-17.",
)
row_doc(
    "misc_ecuador_armored_doors_15k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador armored doors",
    "Ecuador",
    "27 Jul 2022: Department of State awards contract 19EC7522P0809 for armored doors (PoP Ecuador); obligated USD 14,999.99. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14999.99", "2022-07-27", "2022", "", "",
    "Armored doors, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_ecuador_armored_doors_15k_2022",
    "ARMORED DOORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522P0809_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1159",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7522P0809_1900_-NONE-_-NONE- (misc_ecuador_armored_doors_15k_2022). Signed 2022-07-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7522P0809_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_armored_doors_15k_2022 USD 0.015m. Supports misc_ecuador_armored_doors_15k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14999.99; date_signed 2022-07-27.",
)

# === Cycle 1160 (seed 20262160) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "cummins_ecuador_residential_generators_136k_2010",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Ecuador generators for residences",
    "Ecuador",
    "12 Aug 2010: Department of State awards contract SEC30010M0721 to Cummins Power Generation Inc. for generators for residences (PoP Ecuador); obligated USD 135,736.0. CapEx face = award obligation. Residences unnamed; site coords not stated — lat/lon blank.",
    "135736", "2010-08-12", "2010", "", "",
    "Generators for residences, Ecuador (USASpending description; residences unnamed; site coords not stated — lat/lon blank).",
    "usaspending_cummins_ecuador_residential_generators_136k_2010",
    "GENERATORS FOR RESIDENCES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC30010M0721_1900_-NONE-_-NONE-/",
    "Actor: CUMMINS POWER GENERATION INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1160",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SEC30010M0721_1900_-NONE-_-NONE- (cummins_ecuador_residential_generators_136k_2010). Signed 2010-08-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SEC30010M0721_1900_-NONE-_-NONE-/.",
    "USASpending: cummins_ecuador_residential_generators_136k_2010 USD 0.136m. Supports cummins_ecuador_residential_generators_136k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 135736.0; date_signed 2010-08-12.",
)
row_doc(
    "hy_security_el_salvador_compound_sliding_gate_hydraulic_drivers_101k_2022",
    "infrastructure", "building_materials", "us",
    "Hy-Security Gate — El Salvador hydraulic drivers for compound sliding gates",
    "El Salvador",
    "13 Jan 2022: Department of State awards contract 19ES6022P0159 to Hy-Security Gate, Inc. for hydraulic drivers for compound sliding gates (PoP El Salvador); obligated USD 101,195.0. CapEx face = award obligation. Compound unnamed; site coords not stated — lat/lon blank.",
    "101195", "2022-01-13", "2022", "", "",
    "Hydraulic drivers for compound sliding gates, El Salvador (USASpending description; compound unnamed; site coords not stated — lat/lon blank).",
    "usaspending_hy_security_el_salvador_compound_sliding_gate_hydraulic_drivers_101k_2022",
    "7901- HYDRAULIC DRIVERS FOR COMPOUND SLIDING GATES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0159_1900_-NONE-_-NONE-/",
    "Actor: HY-SECURITY GATE, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1160",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6022P0159_1900_-NONE-_-NONE- (hy_security_el_salvador_compound_sliding_gate_hydraulic_drivers_101k_2022). Signed 2022-01-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0159_1900_-NONE-_-NONE-/.",
    "USASpending: hy_security_el_salvador_compound_sliding_gate_hydraulic_drivers_101k_2022 USD 0.101m. Supports hy_security_el_salvador_compound_sliding_gate_hydraulic_drivers_101k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 101195.0; date_signed 2022-01-13.",
)
row_doc(
    "misc_peru_cmr_soundproof_windows_15k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru CMR soundproof windows",
    "Peru",
    "30 Sep 2015: Department of State awards contract SPE50015M2538 for soundproof windows at CMR (PoP Peru); obligated USD 14,999.42. CapEx face = award obligation. CMR named; site coords not stated — lat/lon blank.",
    "14999.42", "2015-09-30", "2015", "", "",
    "Soundproof windows at CMR, Peru (USASpending description; CMR named; site coords not stated — lat/lon blank).",
    "usaspending_misc_peru_cmr_soundproof_windows_15k_2015",
    "9/25 WLB SOUNDPROOF WINDOWS AT CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M2538_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1160",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50015M2538_1900_-NONE-_-NONE- (misc_peru_cmr_soundproof_windows_15k_2015). Signed 2015-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50015M2538_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_cmr_soundproof_windows_15k_2015 USD 0.015m. Supports misc_peru_cmr_soundproof_windows_15k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14999.42; date_signed 2015-09-30.",
)
row_doc(
    "misc_peru_dcr_pool_bathrooms_upgrade_15k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru DCR pool bathrooms upgrade",
    "Peru",
    "25 Sep 2014: Department of State awards contract SPE50014C0019 to upgrade pool bathrooms at DCR Lima (PoP Peru); obligated USD 14,999.99. CapEx face = award obligation. DCR Lima named; site coords not stated — lat/lon blank.",
    "14999.99", "2014-09-25", "2014", "", "",
    "Upgrade pool bathrooms at DCR, Lima, Peru (USASpending description; DCR Lima named; site coords not stated — lat/lon blank).",
    "usaspending_misc_peru_dcr_pool_bathrooms_upgrade_15k_2014",
    "LIMA- CONTRACT TO UPGRADE POOL BATHROOMS AT DCR IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014C0019_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1160",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50014C0019_1900_-NONE-_-NONE- (misc_peru_dcr_pool_bathrooms_upgrade_15k_2014). Signed 2014-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014C0019_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_dcr_pool_bathrooms_upgrade_15k_2014 USD 0.015m. Supports misc_peru_dcr_pool_bathrooms_upgrade_15k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14999.99; date_signed 2014-09-25.",
)
row_doc(
    "misc_brazil_cmr_external_lighting_electric_cables_15k_2015",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil new CMR electric cables for external lighting",
    "Brazil",
    "11 Sep 2015: Department of State awards contract SBR25015M1784 for new CMR electric cables for external lighting (PoP Brazil); obligated USD 14,960.46. CapEx face = award obligation. CMR named; site coords not stated — lat/lon blank.",
    "14960.46", "2015-09-11", "2015", "", "",
    "Electric cables for external lighting, new CMR, Brazil (USASpending description; CMR named; site coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_cmr_external_lighting_electric_cables_15k_2015",
    "NEW CMR - ELETRIC CABLES FOR EXTERNAL LIGHTING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25015M1784_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1160",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25015M1784_1900_-NONE-_-NONE- (misc_brazil_cmr_external_lighting_electric_cables_15k_2015). Signed 2015-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25015M1784_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_cmr_external_lighting_electric_cables_15k_2015 USD 0.015m. Supports misc_brazil_cmr_external_lighting_electric_cables_15k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14960.46; date_signed 2015-09-11.",
)

# === Cycle 1161 (seed 20262161) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "ross_technology_dominican_republic_consular_frame_doors_138k_2020",
    "infrastructure", "building_materials", "us",
    "Ross Technology — Dominican Republic frame and doors for consular area",
    "Dominican Republic",
    "30 Sep 2020: Department of State awards contract 19DR8620P1226 to Ross Technology Company for frame and doors for consular area (PoP Dominican Republic); obligated USD 137,827.0. CapEx face = award obligation. Consular area named; site coords not stated — lat/lon blank.",
    "137827", "2020-09-30", "2020", "", "",
    "Frame and doors for consular area, Dominican Republic (USASpending description; consular area named; site coords not stated — lat/lon blank).",
    "usaspending_ross_technology_dominican_republic_consular_frame_doors_138k_2020",
    "FRAME AND DOORS FOR CONSULAR AREA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8620P1226_1900_-NONE-_-NONE-/",
    "Actor: ROSS TECHNOLOGY COMPANY (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1161",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8620P1226_1900_-NONE-_-NONE- (ross_technology_dominican_republic_consular_frame_doors_138k_2020). Signed 2020-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8620P1226_1900_-NONE-_-NONE-/.",
    "USASpending: ross_technology_dominican_republic_consular_frame_doors_138k_2020 USD 0.138m. Supports ross_technology_dominican_republic_consular_frame_doors_138k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 137827.0; date_signed 2020-09-30.",
)
row_doc(
    "spectrum_electrical_brazil_rio_de_janeiro_electrical_work_362k_2015",
    "energy", "power_plants_grid", "us",
    "Spectrum Electrical Services — Brazil Rio de Janeiro electrical work",
    "Brazil",
    "29 May 2015: Department of State awards contract SAQMMA15F1576 to Spectrum Electrical Services, Inc for electrical work Rio de Janeiro (PoP Brazil); obligated USD 361,791.07. CapEx face = award obligation. Rio de Janeiro named; site coords not stated — lat/lon blank.",
    "361791.07", "2015-05-29", "2015", "", "",
    "Electrical work Rio de Janeiro, Brazil (USASpending description; Rio de Janeiro named; site coords not stated — lat/lon blank).",
    "usaspending_spectrum_electrical_brazil_rio_de_janeiro_electrical_work_362k_2015",
    "ELECTRICAL WORK RIO DE JANEIRO, BRAZIL IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1576_1900_SAQMMA12D0194_1900/",
    "Actor: SPECTRUM ELECTRICAL SERVICES, INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1161",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA15F1576_1900_SAQMMA12D0194_1900 (spectrum_electrical_brazil_rio_de_janeiro_electrical_work_362k_2015). Signed 2015-05-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15F1576_1900_SAQMMA12D0194_1900/.",
    "USASpending: spectrum_electrical_brazil_rio_de_janeiro_electrical_work_362k_2015 USD 0.362m. Supports spectrum_electrical_brazil_rio_de_janeiro_electrical_work_362k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 361791.07; date_signed 2015-05-29.",
)
row_doc(
    "misc_peru_callao_forensic_lab_glass_doors_15k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru Callao forensic laboratory glass doors",
    "Peru",
    "13 Nov 2018: Department of State awards contract 19PE5019P0121 for glass doors forensic laboratory Callao MPS (PoP Peru); obligated USD 14,968.3. CapEx face = award obligation. Callao named; site coords not stated — lat/lon blank.",
    "14968.30", "2018-11-13", "2018", "", "",
    "Glass doors forensic laboratory Callao MPS, Peru (USASpending description; Callao named; site coords not stated — lat/lon blank).",
    "usaspending_misc_peru_callao_forensic_lab_glass_doors_15k_2018",
    "IN23PE02- GLASS DOORS FORENCIC LABORATORY- CALLAO MPS IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5019P0121_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1161",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5019P0121_1900_-NONE-_-NONE- (misc_peru_callao_forensic_lab_glass_doors_15k_2018). Signed 2018-11-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5019P0121_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_callao_forensic_lab_glass_doors_15k_2018 USD 0.015m. Supports misc_peru_callao_forensic_lab_glass_doors_15k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14968.3; date_signed 2018-11-13.",
)
row_doc(
    "misc_bolivia_heat_pump_15k_2012",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Bolivia heat pump",
    "Bolivia",
    "27 Sep 2012: Department of State awards contract SBL40012M0461 for heat pump (PoP Bolivia); obligated USD 14,946.48. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14946.48", "2012-09-27", "2012", "", "",
    "Heat pump, Bolivia (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_bolivia_heat_pump_15k_2012",
    "EOY - HEAT PUMP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40012M0461_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1161",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBL40012M0461_1900_-NONE-_-NONE- (misc_bolivia_heat_pump_15k_2012). Signed 2012-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40012M0461_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bolivia_heat_pump_15k_2012 USD 0.015m. Supports misc_bolivia_heat_pump_15k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14946.48; date_signed 2012-09-27.",
)
row_doc(
    "misc_mexico_ipc_ups_contingency_15k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Mexico IMO UPS for IPC contingency",
    "Mexico",
    "7 Nov 2017: Department of State awards contract 19MX5318P0102 for UPS for IPC contingency (PoP Mexico); obligated USD 14,937.88. CapEx face = award obligation. IPC named; site coords not stated — lat/lon blank.",
    "14937.88", "2017-11-07", "2017", "", "",
    "UPS for IPC contingency, Mexico (USASpending description; IPC named; site coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_ipc_ups_contingency_15k_2017",
    "MEX/IMO - UPS- FOR IPC CONTINGENCY PURPOSES/FY17 IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5318P0102_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1161",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5318P0102_1900_-NONE-_-NONE- (misc_mexico_ipc_ups_contingency_15k_2017). Signed 2017-11-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5318P0102_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_ipc_ups_contingency_15k_2017 USD 0.015m. Supports misc_mexico_ipc_ups_contingency_15k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14937.88; date_signed 2017-11-07.",
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
