#!/usr/bin/env python3
"""Cycles 1168–1170: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262168–20262170. Thin top-up dry.
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


# === Cycle 1168 (seed 20262168) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "spectrum_electrical_paraguay_fire_alarm_upgrade_399k_2012",
    "infrastructure", "building_materials", "us",
    "Spectrum Electrical Services — Paraguay fire alarm upgrade",
    "Paraguay",
    "21 Mar 2012: Department of State awards contract SAQMMA12F1065 to Spectrum Electrical Services, Inc for fire alarm upgrade (PoP Paraguay); obligated USD 398,779.28. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "398779.28", "2012-03-21", "2012", "", "",
    "Fire alarm upgrade, Paraguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_spectrum_electrical_paraguay_fire_alarm_upgrade_399k_2012",
    "FIRE ALARM UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1065_1900_SAQMMA08D0007_1900/",
    "Actor: SPECTRUM ELECTRICAL SERVICES, INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1168",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F1065_1900_SAQMMA08D0007_1900 (spectrum_electrical_paraguay_fire_alarm_upgrade_399k_2012). Signed 2012-03-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1065_1900_SAQMMA08D0007_1900/.",
    "USASpending: spectrum_electrical_paraguay_fire_alarm_upgrade_399k_2012 USD 0.399m. Supports spectrum_electrical_paraguay_fire_alarm_upgrade_399k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 398779.28; date_signed 2012-03-21.",
)
row_doc(
    "applied_security_mexico_consulate_outbuildings_ids_install_84k_2024",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Mexico procure ship install 5 IDS systems for new consulate outbuildings",
    "Mexico",
    "8 Jan 2024: Department of State awards contract 19AQMM24F0202 to Applied Security Technologies Inc to procure, ship, and install 5 IDS systems for outbuildings for new consulate compound (PoP Mexico); obligated USD 84,250.0. CapEx face = award obligation. Consulate compound named; site coords not stated — lat/lon blank.",
    "84250", "2024-01-08", "2024", "", "",
    "IDS systems install for new consulate outbuildings, Mexico (USASpending description; consulate compound named, site coords not stated — lat/lon blank).",
    "usaspending_applied_security_mexico_consulate_outbuildings_ids_install_84k_2024",
    "TO PROCURE, SHIP, AND INSTALL (5) IDS SYSTEMS FOR THE OUTBUILDINGS FOR NEW CONSULATE COMPOUND (NCC).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0202_1900_19AQMM19D0002_1900/",
    "Actor: APPLIED SECURITY TECHNOLOGIES INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1168",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24F0202_1900_19AQMM19D0002_1900 (applied_security_mexico_consulate_outbuildings_ids_install_84k_2024). Signed 2024-01-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F0202_1900_19AQMM19D0002_1900/.",
    "USASpending: applied_security_mexico_consulate_outbuildings_ids_install_84k_2024 USD 0.084m. Supports applied_security_mexico_consulate_outbuildings_ids_install_84k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 84250.0; date_signed 2024-01-08.",
)
row_doc(
    "misc_trinidad_embassy_compound_fence_install_14k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Trinidad and Tobago fence installation at embassy compound",
    "Trinidad and Tobago",
    "3 Mar 2016: Department of State awards contract STD55016M0124 for fence installation at the embassy compound (PoP Trinidad and Tobago); obligated USD 13,939.49. CapEx face = award obligation. Embassy compound named; site coords not stated — lat/lon blank.",
    "13939.49", "2016-03-03", "2016", "", "",
    "Fence installation at embassy compound, Trinidad and Tobago (USASpending description; compound named, site coords not stated — lat/lon blank).",
    "usaspending_misc_trinidad_embassy_compound_fence_install_14k_2016",
    "FC 7945: FENCE INSTALLATION AT THE EMBASSY COMPOUND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_STD55016M0124_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1168",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_STD55016M0124_1900_-NONE-_-NONE- (misc_trinidad_embassy_compound_fence_install_14k_2016). Signed 2016-03-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_STD55016M0124_1900_-NONE-_-NONE-/.",
    "USASpending: misc_trinidad_embassy_compound_fence_install_14k_2016 USD 0.014m. Supports misc_trinidad_embassy_compound_fence_install_14k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13939.49; date_signed 2016-03-03.",
)
row_doc(
    "misc_trinidad_residences_generator_install_13k_2018",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Trinidad and Tobago generator installation at residences",
    "Trinidad and Tobago",
    "26 Sep 2018: Department of State awards contract 19TD5518P0450 for generator installation at residences (PoP Trinidad and Tobago); obligated USD 13,233.08. CapEx face = award obligation. Residences unnamed — lat/lon blank.",
    "13233.08", "2018-09-26", "2018", "", "",
    "Generator installation at residences, Trinidad and Tobago (USASpending description; residences unnamed — lat/lon blank).",
    "usaspending_misc_trinidad_residences_generator_install_13k_2018",
    "GENERATOR INSTALLATION AT RESIDENCES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5518P0450_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1168",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19TD5518P0450_1900_-NONE-_-NONE- (misc_trinidad_residences_generator_install_13k_2018). Signed 2018-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5518P0450_1900_-NONE-_-NONE-/.",
    "USASpending: misc_trinidad_residences_generator_install_13k_2018 USD 0.013m. Supports misc_trinidad_residences_generator_install_13k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13233.08; date_signed 2018-09-26.",
)
row_doc(
    "misc_jamaica_inl_aluminium_doors_building_renovation_14k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Jamaica INL aluminium doors for building renovation",
    "Jamaica",
    "21 Apr 2022: Department of State awards contract 19JM3722P0468 for INL aluminium doors for building renovation (PoP Jamaica); obligated USD 14,217.81. CapEx face = award obligation. Exact building unnamed — lat/lon blank.",
    "14217.81", "2022-04-21", "2022", "", "",
    "Aluminium doors for building renovation, Jamaica (USASpending description; building unnamed — lat/lon blank).",
    "usaspending_misc_jamaica_inl_aluminium_doors_building_renovation_14k_2022",
    "INL - ALUMINIUM DOORS FOR BUILDING RENOVATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3722P0468_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1168",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3722P0468_1900_-NONE-_-NONE- (misc_jamaica_inl_aluminium_doors_building_renovation_14k_2022). Signed 2022-04-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3722P0468_1900_-NONE-_-NONE-/.",
    "USASpending: misc_jamaica_inl_aluminium_doors_building_renovation_14k_2022 USD 0.014m. Supports misc_jamaica_inl_aluminium_doors_building_renovation_14k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14217.81; date_signed 2022-04-21.",
)

# === Cycle 1169 (seed 20262169) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_honduras_san_pedro_sula_fe_br_doors_windows_80k_2022",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Honduras San Pedro Sula FE-BR doors and windows for consulate office",
    "Honduras",
    "26 Sep 2022: Department of State awards contract 19H08022P0771 to Norshield Security Products, LLC for FE-BR doors and windows for San Pedro Sula consulate office (PoP Honduras); obligated USD 79,690.0. CapEx face = award obligation. San Pedro Sula named; site coords not stated — lat/lon blank.",
    "79690", "2022-09-26", "2022", "", "",
    "FE-BR doors and windows for San Pedro Sula consulate office, Honduras (USASpending description; San Pedro Sula named, site coords not stated — lat/lon blank).",
    "usaspending_norshield_honduras_san_pedro_sula_fe_br_doors_windows_80k_2022",
    "FE-BR DOORS AND WINDOWS FOR SAN PEDRO SULA CONSULATE OFFICE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08022P0771_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1169",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19H08022P0771_1900_-NONE-_-NONE- (norshield_honduras_san_pedro_sula_fe_br_doors_windows_80k_2022). Signed 2022-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08022P0771_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_honduras_san_pedro_sula_fe_br_doors_windows_80k_2022 USD 0.08m. Supports norshield_honduras_san_pedro_sula_fe_br_doors_windows_80k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79690.0; date_signed 2022-09-26.",
)
row_doc(
    "norshield_brazil_metal_door_screen_69k_2020",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Brazil metal door screen",
    "Brazil",
    "25 Feb 2020: Department of State awards contract 19AQMM20P0437 to Norshield Security Products, LLC for metal door screen etc. (PoP Brazil); obligated USD 68,800.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "68800", "2020-02-25", "2020", "", "",
    "Metal door screen etc., Brazil (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_brazil_metal_door_screen_69k_2020",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0437_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1169",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20P0437_1900_-NONE-_-NONE- (norshield_brazil_metal_door_screen_69k_2020). Signed 2020-02-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0437_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_brazil_metal_door_screen_69k_2020 USD 0.069m. Supports norshield_brazil_metal_door_screen_69k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68800.0; date_signed 2020-02-25.",
)
row_doc(
    "misc_trinidad_ttps_scene_house_cctv_15k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Trinidad and Tobago TTPS scene house CCTV",
    "Trinidad and Tobago",
    "1 Feb 2022: Department of State awards contract 19TD5522P0079 for INLTT TTPS scene house CCTV (PoP Trinidad and Tobago); obligated USD 14,742.5. CapEx face = award obligation. TTPS scene house named; site coords not stated — lat/lon blank.",
    "14742.50", "2022-02-01", "2022", "", "",
    "TTPS scene house CCTV, Trinidad and Tobago (USASpending description; TTPS named, site coords not stated — lat/lon blank).",
    "usaspending_misc_trinidad_ttps_scene_house_cctv_15k_2022",
    "INLTT: TTPS SCENE HOUSE CCTV",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5522P0079_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1169",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19TD5522P0079_1900_-NONE-_-NONE- (misc_trinidad_ttps_scene_house_cctv_15k_2022). Signed 2022-02-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5522P0079_1900_-NONE-_-NONE-/.",
    "USASpending: misc_trinidad_ttps_scene_house_cctv_15k_2022 USD 0.015m. Supports misc_trinidad_ttps_scene_house_cctv_15k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14742.5; date_signed 2022-02-01.",
)
row_doc(
    "misc_honduras_obo663_security_upgrades_new_commissioning_15k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Honduras HSG security upgrades OBO 663 new commissioning INL",
    "Honduras",
    "26 Sep 2023: Department of State awards contract 19H08023P0770 for HSG security upgrades OBO 663 new commissioning INL (PoP Honduras); obligated USD 14,867.89. CapEx face = award obligation. OBO 663 named; site coords not stated — lat/lon blank.",
    "14867.89", "2023-09-26", "2023", "", "",
    "Security upgrades OBO 663 new commissioning, Honduras (USASpending description; OBO property named, site coords not stated — lat/lon blank).",
    "usaspending_misc_honduras_obo663_security_upgrades_new_commissioning_15k_2023",
    "HSG - SECURITY UPGRADES - OBO 663 - NEW COMMISSIONING - INL",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08023P0770_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1169",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19H08023P0770_1900_-NONE-_-NONE- (misc_honduras_obo663_security_upgrades_new_commissioning_15k_2023). Signed 2023-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08023P0770_1900_-NONE-_-NONE-/.",
    "USASpending: misc_honduras_obo663_security_upgrades_new_commissioning_15k_2023 USD 0.015m. Supports misc_honduras_obo663_security_upgrades_new_commissioning_15k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14867.89; date_signed 2023-09-26.",
)
row_doc(
    "misc_paraguay_new_dcr_residential_security_upgrades_13k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Paraguay security upgrades to the new DCR",
    "Paraguay",
    "9 Aug 2021: Department of State awards contract 19PA1021P0281 for RSO residential security upgrades to the new DCR (PoP Paraguay); obligated USD 13,366.95. CapEx face = award obligation. New DCR named; site coords not stated — lat/lon blank.",
    "13366.95", "2021-08-09", "2021", "", "",
    "Security upgrades to the new DCR, Paraguay (USASpending description; DCR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_paraguay_new_dcr_residential_security_upgrades_13k_2021",
    "RSO/RESIDENTIAL SECURITY/SECURITY UPGRADES TO THE NEW DCR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1021P0281_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1169",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PA1021P0281_1900_-NONE-_-NONE- (misc_paraguay_new_dcr_residential_security_upgrades_13k_2021). Signed 2021-08-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PA1021P0281_1900_-NONE-_-NONE-/.",
    "USASpending: misc_paraguay_new_dcr_residential_security_upgrades_13k_2021 USD 0.013m. Supports misc_paraguay_new_dcr_residential_security_upgrades_13k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13366.95; date_signed 2021-08-09.",
)

# === Cycle 1170 (seed 20262170) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "norshield_nicaragua_metal_door_screen_68k_2017",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Nicaragua metal door screen",
    "Nicaragua",
    "9 Feb 2017: Department of State awards contract SAQMMA17M0268 to Norshield Security Products, LLC for metal door, screen etc. (PoP Nicaragua); obligated USD 68,390.0. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "68390", "2017-02-09", "2017", "", "",
    "Metal door screen etc., Nicaragua (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_nicaragua_metal_door_screen_68k_2017",
    "METAL DOOR, SCREEN ETC. IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0268_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1170",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17M0268_1900_-NONE-_-NONE- (norshield_nicaragua_metal_door_screen_68k_2017). Signed 2017-02-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0268_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_nicaragua_metal_door_screen_68k_2017 USD 0.068m. Supports norshield_nicaragua_metal_door_screen_68k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68390.0; date_signed 2017-02-09.",
)
row_doc(
    "norshield_mexico_force_entry_doors_windows_41k_2017",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Mexico fabrication and transportation of three force entry doors and windows",
    "Mexico",
    "2 Mar 2017: Department of State awards contract SMX61017M0047 to Norshield Security Products, LLC for fabrication and transportation of three force entry doors and three forced entry windows (PoP Mexico); obligated USD 40,650.0. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "40650", "2017-03-02", "2017", "", "",
    "Force entry doors and windows fabrication, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_mexico_force_entry_doors_windows_41k_2017",
    "FABRICATION AND TRANSPORTATION OF THREE FORCE ENTRY DOORS AND THREE FORCED ENTRY WINDOWS TO LAREDO, TEXAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX61017M0047_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1170",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX61017M0047_1900_-NONE-_-NONE- (norshield_mexico_force_entry_doors_windows_41k_2017). Signed 2017-03-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX61017M0047_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_mexico_force_entry_doors_windows_41k_2017 USD 0.041m. Supports norshield_mexico_force_entry_doors_windows_41k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 40650.0; date_signed 2017-03-02.",
)
row_doc(
    "misc_bolivia_residences_air_conditioners_14k_2023",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Bolivia GSO/PMU air conditioner units for residences FAP",
    "Bolivia",
    "23 Mar 2023: Department of State awards contract 19BL4023P0140 for GSO/PMU air conditioner units for residences FAP (PoP Bolivia); obligated USD 13,660.91. CapEx face = award obligation. Residences unnamed — lat/lon blank.",
    "13660.91", "2023-03-23", "2023", "", "",
    "Air conditioner units for residences FAP, Bolivia (USASpending description; residences unnamed — lat/lon blank).",
    "usaspending_misc_bolivia_residences_air_conditioners_14k_2023",
    "GSO/PMU AIR CONDITIONERS UNITS FOR RESIDENCES (FAP...",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BL4023P0140_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1170",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BL4023P0140_1900_-NONE-_-NONE- (misc_bolivia_residences_air_conditioners_14k_2023). Signed 2023-03-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BL4023P0140_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bolivia_residences_air_conditioners_14k_2023 USD 0.014m. Supports misc_bolivia_residences_air_conditioners_14k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13660.91; date_signed 2023-03-23.",
)
row_doc(
    "misc_bolivia_nas_bdtf_generator_14k_2012",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Bolivia NAS/BDTF generator",
    "Bolivia",
    "15 Oct 2012: Department of State awards contract SBL40013M0006 for NAS/BDTF generator (PoP Bolivia); obligated USD 13,847.78. CapEx face = award obligation. BDTF named; site coords not stated — lat/lon blank.",
    "13847.78", "2012-10-15", "2012", "", "",
    "NAS/BDTF generator, Bolivia (USASpending description; BDTF named, site coords not stated — lat/lon blank).",
    "usaspending_misc_bolivia_nas_bdtf_generator_14k_2012",
    "NAS/BDTF GENERATOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40013M0006_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1170",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBL40013M0006_1900_-NONE-_-NONE- (misc_bolivia_nas_bdtf_generator_14k_2012). Signed 2012-10-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40013M0006_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bolivia_nas_bdtf_generator_14k_2012 USD 0.014m. Supports misc_bolivia_nas_bdtf_generator_14k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13847.78; date_signed 2012-10-15.",
)
row_doc(
    "misc_argentina_las_heras_kitchen_bathroom_cabinets_closet_14k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina Las Heras kitchen and bathroom cabinets/closet",
    "Argentina",
    "21 Sep 2018: Department of State awards contract 19AR2018P0939 for Las Heras kitchen and bathroom cabinets/closet (PoP Argentina); obligated USD 14,157.0. CapEx face = award obligation. Las Heras named; site coords not stated — lat/lon blank.",
    "14157", "2018-09-21", "2018", "", "",
    "Kitchen and bathroom cabinets/closet, Las Heras, Argentina (USASpending description; Las Heras named, site coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_las_heras_kitchen_bathroom_cabinets_closet_14k_2018",
    "FM- LAS HERAS KITCHEN&BATHROOM CABINETS/CLOSET **LATE PR**",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P0939_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1170",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2018P0939_1900_-NONE-_-NONE- (misc_argentina_las_heras_kitchen_bathroom_cabinets_closet_14k_2018). Signed 2018-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P0939_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_las_heras_kitchen_bathroom_cabinets_closet_14k_2018 USD 0.014m. Supports misc_argentina_las_heras_kitchen_bathroom_cabinets_closet_14k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14157.0; date_signed 2018-09-21.",
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
