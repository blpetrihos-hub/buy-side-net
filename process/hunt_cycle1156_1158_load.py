#!/usr/bin/env python3
"""Cycles 1156–1158: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262156–20262158. Thin top-up dry.
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


# === Cycle 1156 (seed 20262156) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "spectrum_electrical_bahamas_nassau_electrical_work_900k_2016",
    "energy", "power_plants_grid", "us",
    "Spectrum Electrical Services — Bahamas Nassau electrical work",
    "Bahamas",
    "21 Jul 2016: Department of State awards contract SAQMMA16F2898 to Spectrum Electrical Services, Inc for electrical work Nassau (PoP Bahamas); obligated USD 899,984.99. CapEx face = award obligation. Nassau named; site coords not stated — lat/lon blank.",
    "899984.99", "2016-07-21", "2016", "", "",
    "Electrical work Nassau, Bahamas (USASpending description; Nassau named, site coords not stated — lat/lon blank).",
    "usaspending_spectrum_electrical_bahamas_nassau_electrical_work_900k_2016",
    "ELECTRICAL WORK NASSAU IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F2898_1900_SAQMMA12D0194_1900/",
    "Actor: Spectrum Electrical Services, Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1156",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16F2898_1900_SAQMMA12D0194_1900 (spectrum_electrical_bahamas_nassau_electrical_work_900k_2016). Signed 2016-07-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16F2898_1900_SAQMMA12D0194_1900/.",
    "USASpending: spectrum_electrical_bahamas_nassau_electrical_work_900k_2016 USD 0.900m. Supports spectrum_electrical_bahamas_nassau_electrical_work_900k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 899984.99; date_signed 2016-07-21.",
)
row_doc(
    "valkyrie_brazil_brasilia_tss_security_installation_516k_2012",
    "infrastructure", "building_materials", "us",
    "Valkyrie Enterprises — Brazil Brasilia technical security services security installation",
    "Brazil",
    "23 Aug 2012: Department of State awards contract SAQMMA12F2993 to Valkyrie Enterprises, LLC for technical security services Brasilia, Brazil security installation (PoP Brazil); obligated USD 515,667.65. CapEx face = award obligation. Brasilia named; site coords not stated — lat/lon blank.",
    "515667.65", "2012-08-23", "2012", "", "",
    "Technical security services security installation, Brasilia, Brazil (USASpending description; Brasilia named, site coords not stated — lat/lon blank).",
    "usaspending_valkyrie_brazil_brasilia_tss_security_installation_516k_2012",
    "TECHNICAL SECURITY SERVICES BRASILIA, BRAZIL SECURITY INSTALLATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2993_1900_SAQMMA07D0026_1900/",
    "Actor: Valkyrie Enterprises, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1156",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F2993_1900_SAQMMA07D0026_1900 (valkyrie_brazil_brasilia_tss_security_installation_516k_2012). Signed 2012-08-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2993_1900_SAQMMA07D0026_1900/.",
    "USASpending: valkyrie_brazil_brasilia_tss_security_installation_516k_2012 USD 0.516m. Supports valkyrie_brazil_brasilia_tss_security_installation_516k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 515667.65; date_signed 2012-08-23.",
)
row_doc(
    "misc_colombia_apc_power_saving_back_ups_rs1500_8k_2012",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Colombia APC power-saving Back-UPS RS 1500 VA",
    "Colombia",
    "27 Aug 2012: Department of Defense awards contract W913FT12P0313 for APC power-saving Back-UPS RS 1500 VA (PoP Colombia); obligated USD 7,996.69. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "7996.69", "2012-08-27", "2012", "", "",
    "APC power-saving Back-UPS RS 1500 VA, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_colombia_apc_power_saving_back_ups_rs1500_8k_2012",
    "APC POWER-SAVING BACK-UPS RS 1500 VA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0313_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1156",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12P0313_9700_-NONE-_-NONE- (misc_colombia_apc_power_saving_back_ups_rs1500_8k_2012). Signed 2012-08-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12P0313_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_apc_power_saving_back_ups_rs1500_8k_2012 USD 0.008m. Supports misc_colombia_apc_power_saving_back_ups_rs1500_8k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7996.69; date_signed 2012-08-27.",
)
row_doc(
    "misc_brazil_congen_water_pumps_motor_starter_8k_2013",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Brazil Congen water pumps motor starter command replacement",
    "Brazil",
    "12 Sep 2013: Department of State awards contract SBR82013M1522 for FAC water pumps motor starter command replacement (Congen) (PoP Brazil); obligated USD 7,990.33. CapEx face = award obligation. Congen named; site coords not stated — lat/lon blank.",
    "7990.33", "2013-09-12", "2013", "", "",
    "Water pumps motor starter command replacement, Congen, Brazil (USASpending description; Congen named, site coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_congen_water_pumps_motor_starter_8k_2013",
    "IGF::OT::IGF FAC- WATER PUMPS- MOTOR STARTER COMMAND REPLACEMENT (CONGEN)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82013M1522_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1156",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82013M1522_1900_-NONE-_-NONE- (misc_brazil_congen_water_pumps_motor_starter_8k_2013). Signed 2013-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82013M1522_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_congen_water_pumps_motor_starter_8k_2013 USD 0.008m. Supports misc_brazil_congen_water_pumps_motor_starter_8k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7990.33; date_signed 2013-09-12.",
)
row_doc(
    "misc_haiti_hnp_school_air_condition_unit_7k_2016",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Haiti INL HNP 27th promotion HNP school air condition unit 18BTU",
    "Haiti",
    "29 Jun 2016: Department of State awards contract SHA70016M1274 for INL-HNP 27th promotion HNP school air condition unit 18BTU (PoP Haiti); obligated USD 7,000. CapEx face = award obligation. HNP school named; site coords not stated — lat/lon blank.",
    "7000", "2016-06-29", "2016", "", "",
    "HNP school air condition unit 18BTU, Haiti (USASpending description; HNP school named, site coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_hnp_school_air_condition_unit_7k_2016",
    "INL-HNP 27TH PROMOTION HNP SCHOOL AIR CONDITION UNIT 18BTU",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHA70016M1274_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1156",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHA70016M1274_1900_-NONE-_-NONE- (misc_haiti_hnp_school_air_condition_unit_7k_2016). Signed 2016-06-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHA70016M1274_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_hnp_school_air_condition_unit_7k_2016 USD 0.007m. Supports misc_haiti_hnp_school_air_condition_unit_7k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7000; date_signed 2016-06-29.",
)

# === Cycle 1157 (seed 20262157) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "fabrication_designs_trinidad_metal_door_screen_278k_2025",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Trinidad and Tobago metal door screen for international embassies",
    "Trinidad and Tobago",
    "17 Jan 2025: Department of State awards contract 19AQMM25P0328 to Fabrication Designs, Inc. for metal door screen etc. for international embassies (PoP Trinidad and Tobago); obligated USD 277,799. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "277799", "2025-01-17", "2025", "", "",
    "Metal door screen etc. for international embassies, Trinidad and Tobago (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_fabrication_designs_trinidad_metal_door_screen_278k_2025",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0328_1900_-NONE-_-NONE-/",
    "Actor: Fabrication Designs, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1157",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0328_1900_-NONE-_-NONE- (fabrication_designs_trinidad_metal_door_screen_278k_2025). Signed 2025-01-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0328_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_trinidad_metal_door_screen_278k_2025 USD 0.278m. Supports fabrication_designs_trinidad_metal_door_screen_278k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 277799; date_signed 2025-01-17.",
)
row_doc(
    "fabrication_designs_uruguay_montevideo_embassy_doors_227k_2024",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Uruguay Montevideo embassy doors air ship",
    "Uruguay",
    "26 Jun 2024: Department of State awards contract 19AQMM24P0570 to Fabrication Designs, Inc. for procure and air ship doors to U.S. Embassy Montevideo (PoP Uruguay); obligated USD 227,086.47. CapEx face = award obligation. Montevideo embassy named; site coords not stated — lat/lon blank.",
    "227086.47", "2024-06-26", "2024", "", "",
    "Procure and air ship doors to U.S. Embassy Montevideo, Uruguay (USASpending description; Montevideo named, site coords not stated — lat/lon blank).",
    "usaspending_fabrication_designs_uruguay_montevideo_embassy_doors_227k_2024",
    "---------- COMMENTS: MONTEVIDEO, FDI QUOTE: 4124_GPR'S_13EA.   POLY ONLY_01EA.  PROCURE AND AIR SHIP DOOR TO DOOR TO U.S. EMBASSY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0570_1900_-NONE-_-NONE-/",
    "Actor: Fabrication Designs, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1157",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24P0570_1900_-NONE-_-NONE- (fabrication_designs_uruguay_montevideo_embassy_doors_227k_2024). Signed 2024-06-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24P0570_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_uruguay_montevideo_embassy_doors_227k_2024 USD 0.227m. Supports fabrication_designs_uruguay_montevideo_embassy_doors_227k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 227086.47; date_signed 2024-06-26.",
)
row_doc(
    "misc_costa_rica_obc_stainless_steel_hand_rails_7k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Costa Rica OBC install stainless steel hand rails",
    "Costa Rica",
    "18 Sep 2013: Department of State awards contract SCS80013M0812 for FAC/ICASS OBC install stainless steel hand rails (PoP Costa Rica); obligated USD 7,000. CapEx face = award obligation. OBC named; site coords not stated — lat/lon blank.",
    "7000", "2013-09-18", "2013", "", "",
    "OBC install stainless steel hand rails, Costa Rica (USASpending description; OBC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_obc_stainless_steel_hand_rails_7k_2013",
    "FAC/ICASS 1901.0  OBC INSTALL STAINLESS STEEL HAND RAILS. IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80013M0812_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1157",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80013M0812_1900_-NONE-_-NONE- (misc_costa_rica_obc_stainless_steel_hand_rails_7k_2013). Signed 2013-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80013M0812_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_obc_stainless_steel_hand_rails_7k_2013 USD 0.007m. Supports misc_costa_rica_obc_stainless_steel_hand_rails_7k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7000; date_signed 2013-09-18.",
)
row_doc(
    "misc_venezuela_gso_renovation_project_7k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Venezuela renovation project for GSO",
    "Venezuela",
    "30 Sep 2011: Department of State awards contract SVE30011M0914 for FM renovation project for GSO (PoP Venezuela); obligated USD 6,992.32. CapEx face = award obligation. Exact GSO site unnamed — lat/lon blank.",
    "6992.32", "2011-09-30", "2011", "", "",
    "Renovation project for GSO, Venezuela (USASpending description; GSO named, site coords not stated — lat/lon blank).",
    "usaspending_misc_venezuela_gso_renovation_project_7k_2011",
    "FM - RENOVATION PROJECT FOR GSO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30011M0914_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1157",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SVE30011M0914_1900_-NONE-_-NONE- (misc_venezuela_gso_renovation_project_7k_2011). Signed 2011-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SVE30011M0914_1900_-NONE-_-NONE-/.",
    "USASpending: misc_venezuela_gso_renovation_project_7k_2011 USD 0.007m. Supports misc_venezuela_gso_renovation_project_7k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6992.32; date_signed 2011-09-30.",
)
row_doc(
    "misc_costa_rica_cmr_kitchen_countertops_install_7k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Costa Rica provide and install CMR kitchen countertops",
    "Costa Rica",
    "5 Jun 2015: Department of State awards contract SCS80015M0310 for FAC/ICASS provide and install CMR kitchen countertops (PoP Costa Rica); obligated USD 6,990. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.",
    "6990", "2015-06-05", "2015", "", "",
    "Provide and install CMR kitchen countertops, Costa Rica (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_costa_rica_cmr_kitchen_countertops_install_7k_2015",
    "FAC/ICASS 7901.3. PROVIDE AND INSTALL CMR KITCHEN COUNTERTOPS IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80015M0310_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1157",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80015M0310_1900_-NONE-_-NONE- (misc_costa_rica_cmr_kitchen_countertops_install_7k_2015). Signed 2015-06-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80015M0310_1900_-NONE-_-NONE-/.",
    "USASpending: misc_costa_rica_cmr_kitchen_countertops_install_7k_2015 USD 0.007m. Supports misc_costa_rica_cmr_kitchen_countertops_install_7k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6990; date_signed 2015-06-05.",
)

# === Cycle 1158 (seed 20262158) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_mexico_metal_door_screen_152k_2022",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Mexico metal door screen for international embassies",
    "Mexico",
    "15 Jul 2022: Department of State awards contract 19AQMM22P0833 to Norshield Security Products, LLC for metal door screen etc. for international embassies (PoP Mexico); obligated USD 152,479. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "152479", "2022-07-15", "2022", "", "",
    "Metal door screen etc. for international embassies, Mexico (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_mexico_metal_door_screen_152k_2022",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0833_1900_-NONE-_-NONE-/",
    "Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1158",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22P0833_1900_-NONE-_-NONE- (norshield_mexico_metal_door_screen_152k_2022). Signed 2022-07-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22P0833_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_mexico_metal_door_screen_152k_2022 USD 0.152m. Supports norshield_mexico_metal_door_screen_152k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 152479; date_signed 2022-07-15.",
)
row_doc(
    "norshield_nicaragua_metal_door_screen_97k_2019",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Nicaragua metal door screen for international embassies",
    "Nicaragua",
    "3 Jun 2019: Department of State awards contract 19AQMM19P0845 to Norshield Security Products, LLC for metal door screen etc. (PoP Nicaragua); obligated USD 97,298. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "97298", "2019-06-03", "2019", "", "",
    "Metal door screen etc., Nicaragua (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_nicaragua_metal_door_screen_97k_2019",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0845_1900_-NONE-_-NONE-/",
    "Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1158",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19P0845_1900_-NONE-_-NONE- (norshield_nicaragua_metal_door_screen_97k_2019). Signed 2019-06-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0845_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_nicaragua_metal_door_screen_97k_2019 USD 0.097m. Supports norshield_nicaragua_metal_door_screen_97k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 97298; date_signed 2019-06-03.",
)
row_doc(
    "misc_brazil_cmr_side_walls_construction_7k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil side walls construction for CMR",
    "Brazil",
    "14 Jun 2010: Department of State awards contract SBR25010M1735 for side walls construction for CMR (PoP Brazil); obligated USD 6,984.13. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.",
    "6984.13", "2010-06-14", "2010", "", "",
    "Side walls construction for CMR, Brazil (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_cmr_side_walls_construction_7k_2010",
    "SIDE WALLS CONSTRUCTION FOR CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25010M1735_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1158",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25010M1735_1900_-NONE-_-NONE- (misc_brazil_cmr_side_walls_construction_7k_2010). Signed 2010-06-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25010M1735_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_cmr_side_walls_construction_7k_2010 USD 0.007m. Supports misc_brazil_cmr_side_walls_construction_7k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6984.13; date_signed 2010-06-14.",
)
row_doc(
    "misc_colombia_condoto_concertina_fence_7k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia NAU ERAD concertina fence base Condoto",
    "Colombia",
    "14 Jun 2012: Department of State awards contract SCO15012M1211 for NAU ERAD concertina fence base Condoto (PoP Colombia); obligated USD 6,981.10. CapEx face = award obligation. Condoto named; site coords not stated — lat/lon blank.",
    "6981.1", "2012-06-14", "2012", "", "",
    "Concertina fence base Condoto, Colombia (USASpending description; Condoto named, site coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_condoto_concertina_fence_7k_2012",
    "NAU ERAD CONCERTINA FENCE BASE CONDOTO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M1211_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1158",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15012M1211_1900_-NONE-_-NONE- (misc_colombia_condoto_concertina_fence_7k_2012). Signed 2012-06-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15012M1211_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_condoto_concertina_fence_7k_2012 USD 0.007m. Supports misc_colombia_condoto_concertina_fence_7k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6981.1; date_signed 2012-06-14.",
)
row_doc(
    "misc_honduras_new_property_acs_supply_install_7k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Honduras supply and installation of A/Cs for new property OBO 586 FAP",
    "Honduras",
    "22 Sep 2017: Department of State awards contract SHO80017M1049 for HSG supply+installation of A/Cs for new property OBO 586 FAP (PoP Honduras); obligated USD 6,978.72. CapEx face = award obligation. Exact property unnamed — lat/lon blank.",
    "6978.72", "2017-09-22", "2017", "", "",
    "Supply and installation of A/Cs for new property OBO 586 FAP, Honduras (USASpending description; property code named, site coords not stated — lat/lon blank).",
    "usaspending_misc_honduras_new_property_acs_supply_install_7k_2017",
    "HSG_SUPPLY+INSTALLATION OF A/CS FOR NEW PROPERTY OBO 586_FAP''IGF::OT::IGF''",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80017M1049_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1158",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80017M1049_1900_-NONE-_-NONE- (misc_honduras_new_property_acs_supply_install_7k_2017). Signed 2017-09-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80017M1049_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_new_property_acs_supply_install_7k_2017 USD 0.007m. Supports misc_honduras_new_property_acs_supply_install_7k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6978.72; date_signed 2017-09-22.",
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
