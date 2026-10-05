#!/usr/bin/env python3
"""Cycles 1140–1142: USASpending LatAm CapEx residual (~USD0.011–0.035m).

Seeds: 20262140–20262142. Thin top-up dry.
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


# === Cycle 1140 (seed 20262140) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "tri_ed_brazil_new_cmr_cameras_20k_2015",
    "infrastructure", "building_materials", "us",
    "Tri-Ed Distribution — Brazil cameras for new CMR",
    "Brazil",
    "8 Jul 2015: Department of State awards contract SBR25015M1054 to Tri-Ed Distribution Inc. for cameras for new CMR (PoP Brazil); obligated USD 19,877. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.",
    "19877", "2015-07-08", "2015", "", "",
    "Cameras for new CMR, Brazil (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_tri_ed_brazil_new_cmr_cameras_20k_2015",
    'CAMERAS FOR NEW CMR "IGF::OT::IGF"',
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25015M1054_1900_-NONE-_-NONE-/",
    "Actor: Tri-Ed Distribution Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1140",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25015M1054_1900_-NONE-_-NONE- (tri_ed_brazil_new_cmr_cameras_20k_2015). Signed 2015-07-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25015M1054_1900_-NONE-_-NONE-/.",
    "USASpending: tri_ed_brazil_new_cmr_cameras_20k_2015 USD 0.020m. Supports tri_ed_brazil_new_cmr_cameras_20k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 19877; date_signed 2015-07-08.",
)
row_doc(
    "mcgrath_mexico_prefabricated_office_building_16k_2012",
    "infrastructure", "building_materials", "us",
    "McGrath RentCorp — Mexico 8 x 20 prefabricated office building",
    "Mexico",
    "21 Sep 2012: Department of Agriculture awards contract AGVCHA26212 to McGrath RentCorp for 1 EA standards 8 x 20' prefabricated office building (PoP Mexico); obligated USD 15,961.50. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "15961.5", "2012-09-21", "2012", "", "",
    "8 x 20' prefabricated office building, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_mcgrath_mexico_prefabricated_office_building_16k_2012",
    "1 EA STANDARDS 8 X 20' PREFABRICATED OFFICE BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AGVCHA26212_12K3_GS07F0401X_4732/",
    "Actor: McGrath RentCorp (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1140",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AGVCHA26212_12K3_GS07F0401X_4732 (mcgrath_mexico_prefabricated_office_building_16k_2012). Signed 2012-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AGVCHA26212_12K3_GS07F0401X_4732/.",
    "USASpending: mcgrath_mexico_prefabricated_office_building_16k_2012 USD 0.016m. Supports mcgrath_mexico_prefabricated_office_building_16k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15961.5; date_signed 2012-09-21.",
)
row_doc(
    "freund_el_salvador_acajutla_windows_ceiling_install_35k_2021",
    "infrastructure", "building_materials", "other",
    "Freund de El Salvador — Acajutla supply and installation windows and ceiling",
    "El Salvador",
    "15 Apr 2021: Department of State awards contract 19ES6021P0423 to Freund de El Salvador, Ltda de C.V. for supply and installation windows & ceiling for Acajutla (PoP El Salvador); obligated USD 34,549.87. CapEx face = award obligation. Acajutla named; site coords not stated — lat/lon blank.",
    "34549.87", "2021-04-15", "2021", "", "",
    "Supply and installation windows and ceiling for Acajutla, El Salvador (USASpending description; Acajutla named, site coords not stated — lat/lon blank).",
    "usaspending_freund_el_salvador_acajutla_windows_ceiling_install_35k_2021",
    "SUPPLY AND INSTALLATION WINDOWS & CEILING FOR ACAJUTLA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0423_1900_-NONE-_-NONE-/",
    "Actor: Freund de El Salvador, Ltda de C.V. (El Salvador) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1140",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6021P0423_1900_-NONE-_-NONE- (freund_el_salvador_acajutla_windows_ceiling_install_35k_2021). Signed 2021-04-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6021P0423_1900_-NONE-_-NONE-/.",
    "USASpending: freund_el_salvador_acajutla_windows_ceiling_install_35k_2021 USD 0.035m. Supports freund_el_salvador_acajutla_windows_ceiling_install_35k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 34549.87; date_signed 2021-04-15.",
)
row_doc(
    "sect_honduras_electric_backup_generator_install_33k_2024",
    "energy", "power_plants_grid", "other",
    "SECT — Honduras electric backup generator and installation for INL section",
    "Honduras",
    "26 Sep 2024: Department of State awards contract 191NLE24P0127 to Servicios Energia Construccion y Telecomunicaciones SA de CV for electric backup generator and installation (PoP Honduras); obligated USD 32,888.46. CapEx face = award obligation. Exact INL site unnamed — lat/lon blank.",
    "32888.46", "2024-09-26", "2024", "", "",
    "Electric backup generator and installation for INL section, Honduras (USASpending description; INL section named, site coords not stated — lat/lon blank).",
    "usaspending_sect_honduras_electric_backup_generator_install_33k_2024",
    "NEW PURCHASE ORDER IN THE AMOUNT OF $32,888.46 FOR AN ELECTRIC BACKUP GENERATOR AND INSTALLATION WITH A DELIVERY DATE OF 12/27/2024. THIS REQUIREMENT IS IN SUPPORT OF THE INL SECTI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24P0127_1900_-NONE-_-NONE-/",
    "Actor: Servicios Energia Construccion y Telecomunicaciones SA de CV (Honduras) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1140",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24P0127_1900_-NONE-_-NONE- (sect_honduras_electric_backup_generator_install_33k_2024). Signed 2024-09-26. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24P0127_1900_-NONE-_-NONE-/.",
    "USASpending: sect_honduras_electric_backup_generator_install_33k_2024 USD 0.033m. Supports sect_honduras_electric_backup_generator_install_33k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 32888.46; date_signed 2024-09-26.",
)
row_doc(
    "misc_dominican_republic_cmr_perimeter_wall_lighting_cacs_33k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic CMR perimeter wall lighting and CACS rewiring",
    "Dominican Republic",
    "12 Feb 2015: Department of State awards contract SDR86015M0914 for OBO CMR perimeter wall lighting and CACS rewiring (PoP Dominican Republic); obligated USD 32,924.07. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.",
    "32924.07", "2015-02-12", "2015", "", "",
    "CMR perimeter wall lighting and CACS rewiring, Dominican Republic (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_republic_cmr_perimeter_wall_lighting_cacs_33k_2015",
    "OBO - CMR PERIMETER WALL LIGHTING AND CACS REWIRING: IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M0914_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1140",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86015M0914_1900_-NONE-_-NONE- (misc_dominican_republic_cmr_perimeter_wall_lighting_cacs_33k_2015). Signed 2015-02-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86015M0914_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_republic_cmr_perimeter_wall_lighting_cacs_33k_2015 USD 0.033m. Supports misc_dominican_republic_cmr_perimeter_wall_lighting_cacs_33k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 32924.07; date_signed 2015-02-12.",
)

# === Cycle 1141 (seed 20262141) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "playmore_west_bolivia_usaid_playground_structure_16k_2012",
    "infrastructure", "building_materials", "us",
    "Playmore West — Bolivia USAID playground structure",
    "Bolivia",
    "28 Sep 2012: Department of State awards contract SBL40012M0498 to Playmore West, Inc. for EOY USAID playground structure (PoP Bolivia); obligated USD 15,920. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "15920", "2012-09-28", "2012", "", "",
    "USAID playground structure, Bolivia (USASpending description; site not named — lat/lon blank).",
    "usaspending_playmore_west_bolivia_usaid_playground_structure_16k_2012",
    "EOY - USAID PLAYGROUND STRUCTURE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40012M0498_1900_-NONE-_-NONE-/",
    "Actor: Playmore West, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1141",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBL40012M0498_1900_-NONE-_-NONE- (playmore_west_bolivia_usaid_playground_structure_16k_2012). Signed 2012-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40012M0498_1900_-NONE-_-NONE-/.",
    "USASpending: playmore_west_bolivia_usaid_playground_structure_16k_2012 USD 0.016m. Supports playmore_west_bolivia_usaid_playground_structure_16k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15920; date_signed 2012-09-28.",
)
row_doc(
    "norshield_nicaragua_metal_door_screen_18k_2025",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Nicaragua metal door screen for international embassies",
    "Nicaragua",
    "25 Mar 2025: Department of State awards contract 19AQMM25P0590 to Norshield Security Products, LLC for metal door screen frame etc. for international embassies (PoP Nicaragua); obligated USD 17,900. CapEx face = award obligation. Exact embassy unnamed — lat/lon blank.",
    "17900", "2025-03-25", "2025", "", "",
    "Metal door screen frame etc. for international embassies, Nicaragua (USASpending description; embassy not named — lat/lon blank).",
    "usaspending_norshield_nicaragua_metal_door_screen_18k_2025",
    "METAL DOOR SCREEN FRAME ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0590_1900_-NONE-_-NONE-/",
    "Actor: Norshield Security Products, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1141",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0590_1900_-NONE-_-NONE- (norshield_nicaragua_metal_door_screen_18k_2025). Signed 2025-03-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0590_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_nicaragua_metal_door_screen_18k_2025 USD 0.018m. Supports norshield_nicaragua_metal_door_screen_18k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 17900; date_signed 2025-03-25.",
)
row_doc(
    "misc_dominican_republic_dnp_ups_system_31k_2014",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Dominican Republic UPS system for INF TECH dept at DNP",
    "Dominican Republic",
    "25 Feb 2014: Department of State awards contract SDR86014M0657 for INL UPS system for INF TECH dept at DNP (PoP Dominican Republic); obligated USD 31,000. CapEx face = award obligation. DNP named; site coords not stated — lat/lon blank.",
    "31000", "2014-02-25", "2014", "", "",
    "UPS system for INF TECH dept at DNP, Dominican Republic (USASpending description; DNP named, site coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_republic_dnp_ups_system_31k_2014",
    "INL - UPS SYSTEM FOR INF TECH DEPT AT DNP: IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M0657_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1141",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86014M0657_1900_-NONE-_-NONE- (misc_dominican_republic_dnp_ups_system_31k_2014). Signed 2014-02-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M0657_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_republic_dnp_ups_system_31k_2014 USD 0.031m. Supports misc_dominican_republic_dnp_ups_system_31k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 31000; date_signed 2014-02-25.",
)
row_doc(
    "misc_colombia_embassy_main_transformer_breaker_16k_2024",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Colombia embassy main transformer breaker replacement",
    "Colombia",
    "2 Aug 2024: Department of State awards contract 19C02024P1483 for embassy main transformer breaker replacement 7901 urgent (PoP Colombia); obligated USD 15,986.16. CapEx face = award obligation. Embassy named; site coords not stated — lat/lon blank.",
    "15986.16", "2024-08-02", "2024", "", "",
    "Embassy main transformer breaker replacement, Colombia (USASpending description; embassy named, site coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_embassy_main_transformer_breaker_16k_2024",
    "PR12772089: X3003 EMBASSY MAIN TRANSFORMER BREAKER REPLACEM 7901 URGENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024P1483_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1141",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02024P1483_1900_-NONE-_-NONE- (misc_colombia_embassy_main_transformer_breaker_16k_2024). Signed 2024-08-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024P1483_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_embassy_main_transformer_breaker_16k_2024 USD 0.016m. Supports misc_colombia_embassy_main_transformer_breaker_16k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15986.16; date_signed 2024-08-02.",
)
row_doc(
    "misc_chile_dcr_roof_replacement_16k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Chile DCR roof replacement",
    "Chile",
    "1 Jun 2012: Department of State awards contract SCI80012C0003 for roof replacement at the DCR (PoP Chile); obligated USD 15,939.58. CapEx face = award obligation. DCR named; site coords not stated — lat/lon blank.",
    "15939.58", "2012-06-01", "2012", "", "",
    "Roof replacement at the DCR, Chile (USASpending description; DCR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_chile_dcr_roof_replacement_16k_2012",
    "ROOF REPLACEMENT AT THE DCR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80012C0003_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1141",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCI80012C0003_1900_-NONE-_-NONE- (misc_chile_dcr_roof_replacement_16k_2012). Signed 2012-06-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCI80012C0003_1900_-NONE-_-NONE-/.",
    "USASpending: misc_chile_dcr_roof_replacement_16k_2012 USD 0.016m. Supports misc_chile_dcr_roof_replacement_16k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15939.58; date_signed 2012-06-01.",
)

# === Cycle 1142 (seed 20262142) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "winter_park_el_salvador_chancery_electronic_flush_valves_17k_2012",
    "infrastructure", "building_materials", "us",
    "Winter Park Trading — El Salvador chancery electronic flush valves",
    "El Salvador",
    "19 Sep 2012: Department of State awards contract SES60012M1084 to Winter Park Trading, Inc. for electronic flush valves-chancery building (PoP El Salvador); obligated USD 16,929. CapEx face = award obligation. Chancery named; site coords not stated — lat/lon blank.",
    "16929", "2012-09-19", "2012", "", "",
    "Electronic flush valves, chancery building, El Salvador (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_winter_park_el_salvador_chancery_electronic_flush_valves_17k_2012",
    "7901 C ELECTRONIC FLUSH VALVES-CHANCERY BUILDING.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60012M1084_1900_-NONE-_-NONE-/",
    "Actor: Winter Park Trading, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1142",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60012M1084_1900_-NONE-_-NONE- (winter_park_el_salvador_chancery_electronic_flush_valves_17k_2012). Signed 2012-09-19. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60012M1084_1900_-NONE-_-NONE-/.",
    "USASpending: winter_park_el_salvador_chancery_electronic_flush_valves_17k_2012 USD 0.017m. Supports winter_park_el_salvador_chancery_electronic_flush_valves_17k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 16929; date_signed 2012-09-19.",
)
row_doc(
    "appalachian_land_designs_colombia_cctv_pdands_17k_2010",
    "infrastructure", "building_materials", "us",
    "Appalachian Land Designs — Colombia CCTV PDANDS",
    "Colombia",
    "2 Dec 2010: Department of State awards contract SCO15011M0289 to Appalachian Land Designs, LLC for CCTV-PDANDS (PoP Colombia); obligated USD 16,880.18. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "16880.18", "2010-12-02", "2010", "", "",
    "CCTV-PDANDS, Colombia (USASpending description; site not named — lat/lon blank).",
    "usaspending_appalachian_land_designs_colombia_cctv_pdands_17k_2010",
    "CCTV-PDANDS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011M0289_1900_-NONE-_-NONE-/",
    "Actor: Appalachian Land Designs, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1142",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15011M0289_1900_-NONE-_-NONE- (appalachian_land_designs_colombia_cctv_pdands_17k_2010). Signed 2010-12-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15011M0289_1900_-NONE-_-NONE-/.",
    "USASpending: appalachian_land_designs_colombia_cctv_pdands_17k_2010 USD 0.017m. Supports appalachian_land_designs_colombia_cctv_pdands_17k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 16880.18; date_signed 2010-12-02.",
)
row_doc(
    "misc_panama_conduit_installation_15k_2015",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Panama conduit installation 7901.C",
    "Panama",
    "21 Sep 2015: Department of State awards contract SPM07015M0943 for conduit installation - 7901.C (PoP Panama); obligated USD 15,000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "15000", "2015-09-21", "2015", "", "",
    "Conduit installation 7901.C, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_panama_conduit_installation_15k_2015",
    "CONDUIT INSTALLATION - 7901.C (SPM07015Q0067) IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07015M0943_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1142",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07015M0943_1900_-NONE-_-NONE- (misc_panama_conduit_installation_15k_2015). Signed 2015-09-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07015M0943_1900_-NONE-_-NONE-/.",
    "USASpending: misc_panama_conduit_installation_15k_2015 USD 0.015m. Supports misc_panama_conduit_installation_15k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15000; date_signed 2015-09-21.",
)
row_doc(
    "misc_bahamas_dcr_security_grille_installation_15k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas DCR security grille installation",
    "Bahamas",
    "15 Sep 2010: Department of State awards contract SBF50010M1058 for PC-C-security grille installation @ DCR (PoP Bahamas); obligated USD 15,000. CapEx face = award obligation. DCR named; site coords not stated — lat/lon blank.",
    "15000", "2010-09-15", "2010", "", "",
    "Security grille installation at DCR, Bahamas (USASpending description; DCR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_bahamas_dcr_security_grille_installation_15k_2010",
    "PC-C-SECURITY GRILLE INSTALLATION @ DCR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50010M1058_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1142",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50010M1058_1900_-NONE-_-NONE- (misc_bahamas_dcr_security_grille_installation_15k_2010). Signed 2010-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50010M1058_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_dcr_security_grille_installation_15k_2010 USD 0.015m. Supports misc_bahamas_dcr_security_grille_installation_15k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15000; date_signed 2010-09-15.",
)
row_doc(
    "misc_nicaragua_ltc_gonzalez_power_generator_11k_2011",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Nicaragua new power generator for LTC Gonzalez residence",
    "Nicaragua",
    "22 Feb 2011: Department of State awards contract SNU70011M0101 for new power generator for LTC Gonzalez res. (PoP Nicaragua); obligated USD 11,000. CapEx face = award obligation. LTC Gonzalez residence named; site coords not stated — lat/lon blank.",
    "11000", "2011-02-22", "2011", "", "",
    "New power generator for LTC Gonzalez residence, Nicaragua (USASpending description; residence named, site coords not stated — lat/lon blank).",
    "usaspending_misc_nicaragua_ltc_gonzalez_power_generator_11k_2011",
    "NEW POWER GENERATOR FOR LTC GONZALEZ RES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70011M0101_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1142",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SNU70011M0101_1900_-NONE-_-NONE- (misc_nicaragua_ltc_gonzalez_power_generator_11k_2011). Signed 2011-02-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70011M0101_1900_-NONE-_-NONE-/.",
    "USASpending: misc_nicaragua_ltc_gonzalez_power_generator_11k_2011 USD 0.011m. Supports misc_nicaragua_ltc_gonzalez_power_generator_11k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11000; date_signed 2011-02-22.",
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
