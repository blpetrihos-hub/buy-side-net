#!/usr/bin/env python3
"""Cycles 1312–1314: USASpending LatAm CapEx (Leidos x-ray/VACIS + Cambridge C4I + IsoBOX).

Seeds: 20262312–20262314. Thin top-up dry.
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

# === Cycle 1312 ===
row_doc(
    "leidos_mexico_vip6500_xray_5252k_2011",
    "infrastructure", "building_materials", "us",
    "Leidos — Mexico VIP6500 vehicle/cargo x-ray inspection systems",
    "Mexico",
    "1 Apr 2011: Department of State awards contract to LEIDOS, INC. for supply and delivery of qty. 2 Model VIP6500 full-scan integrated vehicle and cargo x-ray inspection systems; obligated USD 5251674.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "5251674.00", "2011-04-01", "2011", "", "",
    "CONTRACTOR TO PROVIDE ALL PLANT, LABOR, MATERIALS, ETC, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_leidos_mexico_vip6500_xray_5252k_2011",
    "CONTRACTOR TO PROVIDE ALL PLANT, LABOR, MATERIALS, ETC. NECESSARY TO SUPPLY AND DELIVERY QTY. 2, MODEL VIP6500 FULL SCAN INTEGRATED VEHICLE AND CARGO X-RAY INSPECTION SYSTEMS IN SUPPORT OF US/MEXICAN COUNTER NARCOTICS&LAW ENFORCEMENT PROGRAM, MERIDA INITIATIVE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11F0039_1900_GS07F0210J_4730/",
    "Actor: LEIDOS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1312",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC11F0039_1900_GS07F0210J_4730 (leidos_mexico_vip6500_xray_5252k_2011). Signed 2011-04-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC11F0039_1900_GS07F0210J_4730/.",
    "USASpending: leidos_mexico_vip6500_xray_5252k_2011 USD 5.252m. Supports leidos_mexico_vip6500_xray_5252k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5251674.0; date_signed 2011-04-01.",
    investment_type="equipment_supply",
)

# === Cycle 1312 ===
row_doc(
    "leidos_mexico_xray_portal_install_2122k_2017",
    "infrastructure", "building_materials", "us",
    "Leidos — Mexico x-ray integrated portal system procurement and installation",
    "Mexico",
    "31 Oct 2017: Department of State awards contract to LEIDOS, INC. for procurement and installation of an x-ray integrated portal system to expand non-intrusive inspection capabilities; obligated USD 2122363.90. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2122363.90", "2017-10-31", "2017", "", "",
    "THE PROCUREMENT AND INSTALLATION OF AN X-RAY INTEGRATED PORTAL SYSTEM, TO EXPAND THE NON-INTRUSIVE INSPECTION CAPABILITI, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_leidos_mexico_xray_portal_install_2122k_2017",
    "THE PROCUREMENT AND INSTALLATION OF AN X-RAY INTEGRATED PORTAL SYSTEM, TO EXPAND THE NON-INTRUSIVE INSPECTION CAPABILITIES OF MEXICAN GOVERNMENT LAW ENFORCEMENT AND CUSTOMS INSTITUTIONS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19WHAR18P0001_1900_-NONE-_-NONE-/",
    "Actor: LEIDOS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1312",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19WHAR18P0001_1900_-NONE-_-NONE- (leidos_mexico_xray_portal_install_2122k_2017). Signed 2017-10-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19WHAR18P0001_1900_-NONE-_-NONE-/.",
    "USASpending: leidos_mexico_xray_portal_install_2122k_2017 USD 2.122m. Supports leidos_mexico_xray_portal_install_2122k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2122363.9; date_signed 2017-10-31.",
    investment_type="equipment_supply",
)

# === Cycle 1312 ===
row_doc(
    "misc_colombia_perimeter_lights_360k_2016",
    "infrastructure", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Colombia perimeter lights",
    "Colombia",
    "27 Sep 2016: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for perimeter lights; obligated USD 359541.33. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "359541.33", "2016-09-27", "2016", "", "",
    "IGF::OT::IGF PERIMETER LIGHTS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_perimeter_lights_360k_2016",
    "IGF::OT::IGF PERIMETER LIGHTS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT16C0003_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1312",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT16C0003_9700_-NONE-_-NONE- (misc_colombia_perimeter_lights_360k_2016). Signed 2016-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT16C0003_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_perimeter_lights_360k_2016 USD 0.360m. Supports misc_colombia_perimeter_lights_360k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 359541.33; date_signed 2016-09-27.",
    investment_type="equipment_supply",
)

# === Cycle 1312 ===
row_doc(
    "misc_ecuador_emergency_power_stations_352k_2024",
    "infrastructure", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Ecuador emergency power stations",
    "Ecuador",
    "15 Nov 2024: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for emergency power stations; obligated USD 352350.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "352350.00", "2024-11-15", "2024", "", "",
    "EMERGENCY POWER STATIONS, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_ecuador_emergency_power_stations_352k_2024",
    "EMERGENCY POWER STATIONS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7525P0152_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1312",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7525P0152_1900_-NONE-_-NONE- (misc_ecuador_emergency_power_stations_352k_2024). Signed 2024-11-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7525P0152_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_emergency_power_stations_352k_2024 USD 0.352m. Supports misc_ecuador_emergency_power_stations_352k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 352350.0; date_signed 2024-11-15.",
    investment_type="equipment_supply",
)

# === Cycle 1312 ===
row_doc(
    "misc_mexico_security_wall_perimeter_244k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico security wall perimeter upgrade",
    "Mexico",
    "23 Feb 2023: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for security wall perimeter upgrade; obligated USD 243739.20. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "243739.20", "2023-02-23", "2023", "", "",
    "SECURITY WALL PERIMETER UPGRADE, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_security_wall_perimeter_244k_2023",
    "SECURITY WALL PERIMETER UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX7223P0115_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1312",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX7223P0115_1900_-NONE-_-NONE- (misc_mexico_security_wall_perimeter_244k_2023). Signed 2023-02-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX7223P0115_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_security_wall_perimeter_244k_2023 USD 0.244m. Supports misc_mexico_security_wall_perimeter_244k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 243739.2; date_signed 2023-02-23.",
    investment_type="epc",
)

# === Cycle 1313 ===
row_doc(
    "leidos_mexico_vacis_ip6500_install_1886k_2017",
    "infrastructure", "engineering_epc", "us",
    "Leidos — Mexico VACIS IP6500 system installation",
    "Mexico",
    "20 Dec 2017: Department of State awards contract to LEIDOS, INC. for installation, maintenance and training for VACIS IP6500 system (CapEx face = award obligation); obligated USD 1885619.41. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1885619.41", "2017-12-20", "2017", "", "",
    "INSTALLATION, MAINTENANCE AND TRAINING FOR VACIS IP6500 SYSTEM, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_leidos_mexico_vacis_ip6500_install_1886k_2017",
    "INSTALLATION, MAINTENANCE AND TRAINING FOR VACIS IP6500 SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F0065_1900_GS07F0210J_4730/",
    "Actor: LEIDOS, INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1313",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F0065_1900_GS07F0210J_4730 (leidos_mexico_vacis_ip6500_install_1886k_2017). Signed 2017-12-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F0065_1900_GS07F0210J_4730/.",
    "USASpending: leidos_mexico_vacis_ip6500_install_1886k_2017 USD 1.886m. Supports leidos_mexico_vacis_ip6500_install_1886k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1885619.41; date_signed 2017-12-20.",
    investment_type="equipment_supply",
)

# === Cycle 1313 ===
row_doc(
    "cambridge_bahamas_c4i_minor_construction_913k_2019",
    "infrastructure", "engineering_epc", "us",
    "Cambridge International Systems — Bahamas C4I CIIS engineering and minor construction",
    "Bahamas",
    "24 Jul 2019: Department of State awards contract to CAMBRIDGE INTERNATIONAL SYSTEMS, INC. for engineering services and minor construction for C4I CIIS; obligated USD 913479.53. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "913479.53", "2019-07-24", "2019", "", "",
    "ENGINEERING SERVICES AND MINOR CONSTRUCTION FOR C4I CIIS, Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_cambridge_bahamas_c4i_minor_construction_913k_2019",
    "ENGINEERING SERVICES AND MINOR CONSTRUCTION FOR C4I CIIS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0003919F0349_9700_N0003915D0037_9700/",
    "Actor: CAMBRIDGE INTERNATIONAL SYSTEMS, INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1313",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_N0003919F0349_9700_N0003915D0037_9700 (cambridge_bahamas_c4i_minor_construction_913k_2019). Signed 2019-07-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_N0003919F0349_9700_N0003915D0037_9700/.",
    "USASpending: cambridge_bahamas_c4i_minor_construction_913k_2019 USD 0.913m. Supports cambridge_bahamas_c4i_minor_construction_913k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 913479.53; date_signed 2019-07-24.",
    investment_type="epc",
)

# === Cycle 1313 ===
row_doc(
    "misc_trinidad_nec_chain_link_fence_232k_2023",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Trinidad NEC chain-link fence and gates",
    "Trinidad and Tobago",
    "10 May 2023: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for NEC installation of chain link fence and gates; obligated USD 231931.28. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "231931.28", "2023-05-10", "2023", "", "",
    "(NEC) INSTALLATION OF CHAIN LINK FENCE AND GATES, Trinidad and Tobago (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_trinidad_nec_chain_link_fence_232k_2023",
    "(NEC) INSTALLATION OF CHAIN LINK FENCE AND GATES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5523C0005_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1313",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19TD5523C0005_1900_-NONE-_-NONE- (misc_trinidad_nec_chain_link_fence_232k_2023). Signed 2023-05-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19TD5523C0005_1900_-NONE-_-NONE-/.",
    "USASpending: misc_trinidad_nec_chain_link_fence_232k_2023 USD 0.232m. Supports misc_trinidad_nec_chain_link_fence_232k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 231931.28; date_signed 2023-05-10.",
    investment_type="epc",
)

# === Cycle 1313 ===
row_doc(
    "misc_suriname_paramaribo_permanent_power_222k_2014",
    "infrastructure", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Suriname Paramaribo new embassy permanent power",
    "Suriname",
    "28 Aug 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for permanent power for the new embassy project in Paramaribo; obligated USD 222194.03. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "222194.03", "2014-08-28", "2014", "", "",
    "CONTRACT FOR PERMANENT POWER FOR THE NEW EMBASSY PROJECT IN PARAMARIBO  IGF::OT::IGF, Suriname (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_suriname_paramaribo_permanent_power_222k_2014",
    "CONTRACT FOR PERMANENT POWER FOR THE NEW EMBASSY PROJECT IN PARAMARIBO  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0168_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1313",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14C0168_1900_-NONE-_-NONE- (misc_suriname_paramaribo_permanent_power_222k_2014). Signed 2014-08-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0168_1900_-NONE-_-NONE-/.",
    "USASpending: misc_suriname_paramaribo_permanent_power_222k_2014 USD 0.222m. Supports misc_suriname_paramaribo_permanent_power_222k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 222194.03; date_signed 2014-08-28.",
    investment_type="epc",
)

# === Cycle 1313 ===
row_doc(
    "misc_guatemala_perimeter_wall_220k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guatemala chemical precursors complex perimeter wall",
    "Guatemala",
    "22 Aug 2022: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for Guate INLG RM LI perimeter wall chemical precursors complex; obligated USD 219967.08. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "219967.08", "2022-08-22", "2022", "", "",
    "GUATE INLG RM LI PERIMETER WALL CHEMICAL PRECURSORS COMPLEX, Guatemala (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_guatemala_perimeter_wall_220k_2022",
    "GUATE INLG RM LI PERIMETER WALL CHEMICAL PRECURSORS COMPLEX",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5022C0021_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1313",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GT5022C0021_1900_-NONE-_-NONE- (misc_guatemala_perimeter_wall_220k_2022). Signed 2022-08-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GT5022C0021_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_perimeter_wall_220k_2022 USD 0.220m. Supports misc_guatemala_perimeter_wall_220k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 219967.08; date_signed 2022-08-22.",
    investment_type="epc",
)

# === Cycle 1314 ===
row_doc(
    "isobox_panama_modular_ops_center_102k_2021",
    "infrastructure", "engineering_epc", "us",
    "IsoBOX — Panama temporary modular operations center",
    "Panama",
    "3 Jun 2021: Department of State awards contract to ISOBOX INC for temporary modular operations center; obligated USD 102060.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "102060.00", "2021-06-03", "2021", "", "",
    "TEMPORARY MODULAR OPERATIONS CENTER, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_isobox_panama_modular_ops_center_102k_2021",
    "TEMPORARY MODULAR OPERATIONS CENTER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0721P0578_1900_-NONE-_-NONE-/",
    "Actor: ISOBOX INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1314",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0721P0578_1900_-NONE-_-NONE- (isobox_panama_modular_ops_center_102k_2021). Signed 2021-06-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0721P0578_1900_-NONE-_-NONE-/.",
    "USASpending: isobox_panama_modular_ops_center_102k_2021 USD 0.102m. Supports isobox_panama_modular_ops_center_102k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 102060.0; date_signed 2021-06-03.",
    investment_type="equipment_supply",
)

# === Cycle 1314 ===
row_doc(
    "isobox_panama_modular_classrooms_76k_2023",
    "infrastructure", "engineering_epc", "us",
    "IsoBOX — Panama portable modular classrooms",
    "Panama",
    "9 Nov 2023: Department of State awards contract to ISOBOX INC for portable modular classrooms; obligated USD 75640.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "75640.00", "2023-11-09", "2023", "", "",
    "PORTABLE MODULAR CLASSROOMS, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_isobox_panama_modular_classrooms_76k_2023",
    "PORTABLE MODULAR CLASSROOMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0724P0021_1900_-NONE-_-NONE-/",
    "Actor: ISOBOX INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1314",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0724P0021_1900_-NONE-_-NONE- (isobox_panama_modular_classrooms_76k_2023). Signed 2023-11-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0724P0021_1900_-NONE-_-NONE-/.",
    "USASpending: isobox_panama_modular_classrooms_76k_2023 USD 0.076m. Supports isobox_panama_modular_classrooms_76k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 75640.0; date_signed 2023-11-09.",
    investment_type="equipment_supply",
)

# === Cycle 1314 ===
row_doc(
    "idac_colombia_brcna_chain_link_fence_211k_2017",
    "infrastructure", "bridges_roads", "other",
    "IDAC S.A.S. — Colombia BRCNA bases chain-link fence",
    "Colombia",
    "12 Jul 2017: Department of State awards contract to IDAC S A S for COLAR AV chain link fence for BRCNA bases CAQ SJE Animas; obligated USD 211324.01. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "211324.01", "2017-07-12", "2017", "", "",
    "COLAR AV CHAIN LINK FENCE FOR BRCNA BASES CAQ SJE ANIMAS IGF::OT::IGF, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_idac_colombia_brcna_chain_link_fence_211k_2017",
    "COLAR AV CHAIN LINK FENCE FOR BRCNA BASES CAQ SJE ANIMAS IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15017C0011_1900_-NONE-_-NONE-/",
    "Actor: IDAC S A S — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1314",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15017C0011_1900_-NONE-_-NONE- (idac_colombia_brcna_chain_link_fence_211k_2017). Signed 2017-07-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15017C0011_1900_-NONE-_-NONE-/.",
    "USASpending: idac_colombia_brcna_chain_link_fence_211k_2017 USD 0.211m. Supports idac_colombia_brcna_chain_link_fence_211k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 211324.01; date_signed 2017-07-12.",
    investment_type="epc",
)

# === Cycle 1314 ===
row_doc(
    "misc_brazil_rec_center_perimeter_wall_210k_2021",
    "infrastructure", "bridges_roads", "other",
    "Miscellaneous foreign awardees — Brazil rec center perimeter wall",
    "Brazil",
    "6 Jan 2021: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for rec center perimeter wall construction and repairs; obligated USD 209839.57. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "209839.57", "2021-01-06", "2021", "", "",
    "REC CENTER PERIMETER WALL - CONSTR & REPAIRS (RFQ PR9166192), Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_rec_center_perimeter_wall_210k_2021",
    "REC CENTER PERIMETER WALL - CONSTR & REPAIRS (RFQ PR9166192)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9321P0104_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1314",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9321P0104_1900_-NONE-_-NONE- (misc_brazil_rec_center_perimeter_wall_210k_2021). Signed 2021-01-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9321P0104_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_rec_center_perimeter_wall_210k_2021 USD 0.210m. Supports misc_brazil_rec_center_perimeter_wall_210k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 209839.57; date_signed 2021-01-06.",
    investment_type="epc",
)

# === Cycle 1314 ===
row_doc(
    "anahi_mexico_cgr_perimeter_wall_188k_2023",
    "infrastructure", "bridges_roads", "other",
    "Anahi Rosario Acosta Vargas — Mexico CGR perimeter wall upgrade",
    "Mexico",
    "14 Jul 2023: Department of State awards contract to ANAHI ROSARIO ACOSTA VARGAS for FAC CGR perimeter wall upgrade; obligated USD 188186.75. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "188186.75", "2023-07-14", "2023", "", "",
    "FAC 7942-FWP 186-CGR-PERIMETER WALL UPGRADE, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_anahi_mexico_cgr_perimeter_wall_188k_2023",
    "FAC 7942-FWP 186-CGR-PERIMETER WALL UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1123P0153_1900_-NONE-_-NONE-/",
    "Actor: ANAHI ROSARIO ACOSTA VARGAS — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1314",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX1123P0153_1900_-NONE-_-NONE- (anahi_mexico_cgr_perimeter_wall_188k_2023). Signed 2023-07-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX1123P0153_1900_-NONE-_-NONE-/.",
    "USASpending: anahi_mexico_cgr_perimeter_wall_188k_2023 USD 0.188m. Supports anahi_mexico_cgr_perimeter_wall_188k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 188186.75; date_signed 2023-07-14.",
    investment_type="epc",
)

def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: r for r in rows}
    for row, _ev, _bib in ITEMS:
        rid = row["id"]
        if rid in by_id: raise SystemExit(f"duplicate id: {rid}")
        rows.append(row); by_id[rid] = row
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader(); w.writerows(rows)
    EVID.mkdir(parents=True, exist_ok=True)
    for row, ev, _bib in ITEMS:
        (EVID / f"{row['id']}.json").write_text(json.dumps(ev, indent=2) + "\n", encoding="utf-8")
    bib_docs = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by_id = {b["id"]: b for b in bib_docs}
    for _row, _ev, bib in ITEMS:
        sid = bib["id"]
        if sid in bib_by_id:
            existing = bib_by_id[sid]
            for s in bib.get("supports") or []:
                if s not in (existing.get("supports") or []): existing.setdefault("supports", []).append(s)
        else: bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")


if __name__ == "__main__":
    main()
