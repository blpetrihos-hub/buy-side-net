#!/usr/bin/env python3
"""Cycles 1153–1155: USASpending LatAm CapEx (larger residual + holdovers).

Seeds: 20262153–20262155. Thin top-up dry.
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


# === Cycle 1153 (seed 20262153) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "spectrum_electrical_brazil_sao_paulo_electrical_upgrade_1_37m_2018",
    "energy", "power_plants_grid", "us",
    "Spectrum Electrical Services — Brazil Sao Paulo electrical work upgrade",
    "Brazil",
    "20 Sep 2018: Department of State awards contract 19AQMM18F4036 to Spectrum Electrical Services, Inc for electrical work Sao Paulo upgrade (PoP Brazil); obligated USD 1,374,050.68. CapEx face = award obligation. Sao Paulo named; site coords not stated — lat/lon blank.",
    "1374050.68", "2018-09-20", "2018", "", "",
    "Electrical work Sao Paulo upgrade, Brazil (USASpending description; Sao Paulo named, site coords not stated — lat/lon blank).",
    "usaspending_spectrum_electrical_brazil_sao_paulo_electrical_upgrade_1_37m_2018",
    "ELECTRICAL WORK  SAO PAULO UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4036_1900_19AQMM18D0072_1900/",
    "Actor: Spectrum Electrical Services, Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1153",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18F4036_1900_19AQMM18D0072_1900 (spectrum_electrical_brazil_sao_paulo_electrical_upgrade_1_37m_2018). Signed 2018-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18F4036_1900_19AQMM18D0072_1900/.",
    "USASpending: spectrum_electrical_brazil_sao_paulo_electrical_upgrade_1_37m_2018 USD 1.374m. Supports spectrum_electrical_brazil_sao_paulo_electrical_upgrade_1_37m_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1374050.68; date_signed 2018-09-20.",
)
row_doc(
    "spectrum_electrical_mexico_switchgear_upgrade_1_15m_2021",
    "energy", "power_plants_grid", "us",
    "Spectrum Electrical Services — Mexico switchgear upgrade project",
    "Mexico",
    "14 Sep 2021: Department of State awards contract 19AQMM21F3652 to Spectrum Electrical Services, Inc for switchgear upgrade project (PoP Mexico); obligated USD 1,146,836.14. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "1146836.14", "2021-09-14", "2021", "", "",
    "Switchgear upgrade project, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_spectrum_electrical_mexico_switchgear_upgrade_1_15m_2021",
    "SWITCHGEAR UPGRADE PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3652_1900_19AQMM18D0072_1900/",
    "Actor: Spectrum Electrical Services, Inc (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1153",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21F3652_1900_19AQMM18D0072_1900 (spectrum_electrical_mexico_switchgear_upgrade_1_15m_2021). Signed 2021-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21F3652_1900_19AQMM18D0072_1900/.",
    "USASpending: spectrum_electrical_mexico_switchgear_upgrade_1_15m_2021 USD 1.147m. Supports spectrum_electrical_mexico_switchgear_upgrade_1_15m_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1146836.14; date_signed 2021-09-14.",
)
row_doc(
    "misc_peru_warehouse_rooftop_ac_units_install_8k_2018",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Peru install new rooftop AC units for warehouse building",
    "Peru",
    "23 Jan 2018: Department of State awards contract 19PE5018C0006 for install new rooftop AC units for warehouse building (PoP Peru); obligated USD 7,983.41. CapEx face = award obligation. Warehouse named; site coords not stated — lat/lon blank.",
    "7983.41", "2018-01-23", "2018", "", "",
    "Install new rooftop AC units for warehouse building, Peru (USASpending description; warehouse named, site coords not stated — lat/lon blank).",
    "usaspending_misc_peru_warehouse_rooftop_ac_units_install_8k_2018",
    "INSTALL NEW ROOFTOP AC UNITS FOR WAREHOUSE BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5018C0006_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1153",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5018C0006_1900_-NONE-_-NONE- (misc_peru_warehouse_rooftop_ac_units_install_8k_2018). Signed 2018-01-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5018C0006_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_warehouse_rooftop_ac_units_install_8k_2018 USD 0.008m. Supports misc_peru_warehouse_rooftop_ac_units_install_8k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7983.41; date_signed 2018-01-23.",
)
row_doc(
    "misc_jamaica_isc_ups_8k_2014",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Jamaica ISC UPS",
    "Jamaica",
    "20 Mar 2014: Department of State awards contract SJM37014M0426 for ISC UPS (PoP Jamaica); obligated USD 7,958.26. CapEx face = award obligation. ISC named; site coords not stated — lat/lon blank.",
    "7958.26", "2014-03-20", "2014", "", "",
    "ISC UPS, Jamaica (USASpending description; ISC named, site coords not stated — lat/lon blank).",
    "usaspending_misc_jamaica_isc_ups_8k_2014",
    "IGF::OT::IGF ISC: UPS FOR ISC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37014M0426_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1153",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SJM37014M0426_1900_-NONE-_-NONE- (misc_jamaica_isc_ups_8k_2014). Signed 2014-03-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SJM37014M0426_1900_-NONE-_-NONE-/.",
    "USASpending: misc_jamaica_isc_ups_8k_2014 USD 0.008m. Supports misc_jamaica_isc_ups_8k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7958.26; date_signed 2014-03-20.",
)
row_doc(
    "misc_argentina_goyena_central_ac_replace_8k_2017",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Argentina replace central air conditioning at GOP Pedro Goyena 972 Acassuso",
    "Argentina",
    "29 Sep 2017: Department of State awards contract SAR20017M0504 for replace central air conditioning at GOP Pedro Goyena 972-Acassuso (PoP Argentina); obligated USD 7,942.21. CapEx face = award obligation. Pedro Goyena 972 Acassuso named; site coords not stated — lat/lon blank.",
    "7942.21", "2017-09-29", "2017", "", "",
    "Replace central air conditioning at GOP Pedro Goyena 972 Acassuso, Argentina (USASpending description; address named, site coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_goyena_central_ac_replace_8k_2017",
    "IGF::OT::IGF REPLACE CENTRAL AIR CONDITIONING AT GOP PEDRO GOYENA 972-ACASSUSO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20017M0504_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1153",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20017M0504_1900_-NONE-_-NONE- (misc_argentina_goyena_central_ac_replace_8k_2017). Signed 2017-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20017M0504_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_goyena_central_ac_replace_8k_2017 USD 0.008m. Supports misc_argentina_goyena_central_ac_replace_8k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7942.21; date_signed 2017-09-29.",
)

# === Cycle 1154 (seed 20262154) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "habersham_haiti_ul_level_8_bullet_resistant_window_732k_2026",
    "infrastructure", "building_materials", "us",
    "Habersham Metal Products — Haiti UL Level 8 bullet resistant window",
    "Haiti",
    "30 Sep 2026: Department of State awards contract 19HA7026P1183 to Habersham Metal Products Company for purchase of UL Level 8 bullet resistant window (PoP Haiti); obligated USD 732,240. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "732240", "2026-09-30", "2026", "", "",
    "UL Level 8 bullet resistant window, Haiti (USASpending description; site not named — lat/lon blank).",
    "usaspending_habersham_haiti_ul_level_8_bullet_resistant_window_732k_2026",
    "PURCHASE OF UL LEVEL 8 BULLET RESISTANT WINDOW",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7026P1183_1900_-NONE-_-NONE-/",
    "Actor: Habersham Metal Products Company (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1154",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7026P1183_1900_-NONE-_-NONE- (habersham_haiti_ul_level_8_bullet_resistant_window_732k_2026). Signed 2026-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7026P1183_1900_-NONE-_-NONE-/.",
    "USASpending: habersham_haiti_ul_level_8_bullet_resistant_window_732k_2026 USD 0.732m. Supports habersham_haiti_ul_level_8_bullet_resistant_window_732k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 732240; date_signed 2026-09-30.",
)
row_doc(
    "multistack_colombia_bogota_airstack_chiller_purchase_install_330k_2012",
    "energy", "power_plants_grid", "us",
    "Multistack — Colombia Bogota AmEmb purchase and installation of Airstack chiller unit",
    "Colombia",
    "27 Sep 2012: Department of State awards contract SGE50012C0083 to Multistack LLC for AmEmb Bogota purchase and installation of an Airstack chiller unit (PoP Colombia); obligated USD 330,270.53. CapEx face = award obligation. Bogota embassy named; site coords not stated — lat/lon blank.",
    "330270.53", "2012-09-27", "2012", "", "",
    "Purchase and installation of Airstack chiller unit, AmEmb Bogota, Colombia (USASpending description; Bogota named, site coords not stated — lat/lon blank).",
    "usaspending_multistack_colombia_bogota_airstack_chiller_purchase_install_330k_2012",
    "AMEMB BOGOTA, COLOMBIA; PURCHASE AND INSTALLATION OF AN AIRSTACK CHILLER UNIT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50012C0083_1900_-NONE-_-NONE-/",
    "Actor: Multistack LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1154",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGE50012C0083_1900_-NONE-_-NONE- (multistack_colombia_bogota_airstack_chiller_purchase_install_330k_2012). Signed 2012-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50012C0083_1900_-NONE-_-NONE-/.",
    "USASpending: multistack_colombia_bogota_airstack_chiller_purchase_install_330k_2012 USD 0.330m. Supports multistack_colombia_bogota_airstack_chiller_purchase_install_330k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 330270.53; date_signed 2012-09-27.",
)
row_doc(
    "misc_guatemala_cmr_minisplits_install_8k_2012",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Guatemala minisplits and materials for installation at CMR",
    "Guatemala",
    "12 Sep 2012: Department of State awards contract SGT50012M0587 for FM-program minisplits and materials for installation at CMR (PoP Guatemala); obligated USD 7,952.02. CapEx face = award obligation. Exact CMR unnamed — lat/lon blank.",
    "7952.02", "2012-09-12", "2012", "", "",
    "Minisplits and materials for installation at CMR, Guatemala (USASpending description; CMR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_guatemala_cmr_minisplits_install_8k_2012",
    "FM-PROGRAM- MINISPLITS AND MATERIALS FOR INSTALLATION AT CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50012M0587_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1154",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGT50012M0587_1900_-NONE-_-NONE- (misc_guatemala_cmr_minisplits_install_8k_2012). Signed 2012-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGT50012M0587_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guatemala_cmr_minisplits_install_8k_2012 USD 0.008m. Supports misc_guatemala_cmr_minisplits_install_8k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7952.02; date_signed 2012-09-12.",
)
row_doc(
    "misc_guyana_socu_cctv_system_8k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Guyana INL CCTV system for SOCU office",
    "Guyana",
    "17 Aug 2016: Department of State awards contract SGY20016M0301 for INL CCTV system for SOCU's office (PoP Guyana); obligated USD 7,920.79. CapEx face = award obligation. SOCU office named; site coords not stated — lat/lon blank.",
    "7920.79", "2016-08-17", "2016", "", "",
    "CCTV system for SOCU office, Guyana (USASpending description; SOCU named, site coords not stated — lat/lon blank).",
    "usaspending_misc_guyana_socu_cctv_system_8k_2016",
    "IGF::OT::IGF  INL - CCTV SYSTEM FOR SOCU'S OFFICE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20016M0301_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1154",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGY20016M0301_1900_-NONE-_-NONE- (misc_guyana_socu_cctv_system_8k_2016). Signed 2016-08-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGY20016M0301_1900_-NONE-_-NONE-/.",
    "USASpending: misc_guyana_socu_cctv_system_8k_2016 USD 0.008m. Supports misc_guyana_socu_cctv_system_8k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7920.79; date_signed 2016-08-17.",
)
row_doc(
    "misc_brazil_cgr_guards_area_toilets_renovation_8k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil CGR toilets renovation guards area",
    "Brazil",
    "23 Sep 2013: Department of State awards contract SBR82013M1537 for FAC toilets renovation (guards area) - CGR (PoP Brazil); obligated USD 7,954.55. CapEx face = award obligation. CGR named; site coords not stated — lat/lon blank.",
    "7954.55", "2013-09-23", "2013", "", "",
    "Toilets renovation guards area CGR, Brazil (USASpending description; CGR named, site coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_cgr_guards_area_toilets_renovation_8k_2013",
    "IGF::OT::IGF FAC - TOILETS RENOVATION (GUARDS AREA) - CGR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82013M1537_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1154",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82013M1537_1900_-NONE-_-NONE- (misc_brazil_cgr_guards_area_toilets_renovation_8k_2013). Signed 2013-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82013M1537_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_cgr_guards_area_toilets_renovation_8k_2013 USD 0.008m. Supports misc_brazil_cgr_guards_area_toilets_renovation_8k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7954.55; date_signed 2013-09-23.",
)

# === Cycle 1155 (seed 20262155) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "applied_security_trinidad_port_of_spain_tss_installation_362k_2025",
    "infrastructure", "building_materials", "us",
    "Applied Security Technologies — Trinidad Port of Spain TSS installation",
    "Trinidad and Tobago",
    "28 May 2025: Department of State awards contract 19AQMM25F0716 to Applied Security Technologies Inc for TSS installation at the Port of Spain, Trinidad (PoP Trinidad and Tobago); obligated USD 361,979.02. CapEx face = award obligation. Port of Spain named; site coords not stated — lat/lon blank.",
    "361979.02", "2025-05-28", "2025", "", "",
    "TSS installation at Port of Spain, Trinidad and Tobago (USASpending description; Port of Spain named, site coords not stated — lat/lon blank).",
    "usaspending_applied_security_trinidad_port_of_spain_tss_installation_362k_2025",
    "TSS INSTALLATION AT THE PORT OF SPAIN, TRINIDAD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F0716_1900_19AQMM19D0002_1900/",
    "Actor: Applied Security Technologies Inc (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1155",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25F0716_1900_19AQMM19D0002_1900 (applied_security_trinidad_port_of_spain_tss_installation_362k_2025). Signed 2025-05-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25F0716_1900_19AQMM19D0002_1900/.",
    "USASpending: applied_security_trinidad_port_of_spain_tss_installation_362k_2025 USD 0.362m. Supports applied_security_trinidad_port_of_spain_tss_installation_362k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 361979.02; date_signed 2025-05-28.",
)
row_doc(
    "cummins_honduras_tegucigalpa_10_residential_generators_239k_2013",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Honduras Tegucigalpa 10 residential generators for US Embassy",
    "Honduras",
    "21 Feb 2013: Department of State awards contract SAQMMA13F0652 to Cummins Power Generation Inc. to purchase 10 residential generators for the US Embassy in Tegucigalpa, Honduras (PoP Honduras); obligated USD 239,398.53. CapEx face = award obligation. Tegucigalpa embassy named; site coords not stated — lat/lon blank.",
    "239398.53", "2013-02-21", "2013", "", "",
    "10 residential generators for US Embassy Tegucigalpa, Honduras (USASpending description; Tegucigalpa named, site coords not stated — lat/lon blank).",
    "usaspending_cummins_honduras_tegucigalpa_10_residential_generators_239k_2013",
    "CONTRACT WITH CUMMINS POWER GENERATION, INC. TO PURCHASE 10 RESIDENTIAL GENERATORS FOR THE US EMBASSY IN TEGUCIGALPAS, HONDURAS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F0652_1900_GS07F9004D_4730/",
    "Actor: Cummins Power Generation Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1155",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F0652_1900_GS07F9004D_4730 (cummins_honduras_tegucigalpa_10_residential_generators_239k_2013). Signed 2013-02-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F0652_1900_GS07F9004D_4730/.",
    "USASpending: cummins_honduras_tegucigalpa_10_residential_generators_239k_2013 USD 0.239m. Supports cummins_honduras_tegucigalpa_10_residential_generators_239k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 239398.53; date_signed 2013-02-21.",
)
row_doc(
    "misc_mexico_jersey_barriers_post_8k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico jersey barriers for post",
    "Mexico",
    "29 May 2018: Department of State awards contract 19MX6018P0054 for jersey barriers for post (PoP Mexico); obligated USD 7,956.56. CapEx face = award obligation. Exact post unnamed — lat/lon blank.",
    "7956.56", "2018-05-29", "2018", "", "",
    "Jersey barriers for post, Mexico (USASpending description; post not named — lat/lon blank).",
    "usaspending_misc_mexico_jersey_barriers_post_8k_2018",
    "JERSEY BARRIERS FOR POST",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6018P0054_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1155",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX6018P0054_1900_-NONE-_-NONE- (misc_mexico_jersey_barriers_post_8k_2018). Signed 2018-05-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6018P0054_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_jersey_barriers_post_8k_2018 USD 0.008m. Supports misc_mexico_jersey_barriers_post_8k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7956.56; date_signed 2018-05-29.",
)
row_doc(
    "misc_el_salvador_xochiquetzal_grills_bars_install_8k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador grills/bars installation Xochiquetzal 24-C",
    "El Salvador",
    "6 Apr 2017: Department of State awards contract SES60017M0417 for grills/bars installation Xochiquetzal 24-C (PoP El Salvador); obligated USD 7,965.25. CapEx face = award obligation. Xochiquetzal 24-C named; site coords not stated — lat/lon blank.",
    "7965.25", "2017-04-06", "2017", "", "",
    "Grills/bars installation Xochiquetzal 24-C, El Salvador (USASpending description; address named, site coords not stated — lat/lon blank).",
    "usaspending_misc_el_salvador_xochiquetzal_grills_bars_install_8k_2017",
    "GRILLS/BARS INSTALLATION XOCHIQUETZAL 24-C IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60017M0417_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1155",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60017M0417_1900_-NONE-_-NONE- (misc_el_salvador_xochiquetzal_grills_bars_install_8k_2017). Signed 2017-04-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60017M0417_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_xochiquetzal_grills_bars_install_8k_2017 USD 0.008m. Supports misc_el_salvador_xochiquetzal_grills_bars_install_8k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7965.25; date_signed 2017-04-06.",
)
row_doc(
    "misc_colombia_fms_services_building_door_replacement_8k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia replacement of deteriorated door in services building FMS",
    "Colombia",
    "8 Nov 2011: Department of State awards contract SCO20012M0163 for replacement of deteriorated door in services building - FMS (PoP Colombia); obligated USD 7,929.50. CapEx face = award obligation. Exact services building unnamed — lat/lon blank.",
    "7929.5", "2011-11-08", "2011", "", "",
    "Replacement of deteriorated door in services building FMS, Colombia (USASpending description; FMS named, site coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_fms_services_building_door_replacement_8k_2011",
    "REPLACEMENT OF DETERIORATED DOOR IN SERVICES BUILDING - FMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012M0163_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1155",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20012M0163_1900_-NONE-_-NONE- (misc_colombia_fms_services_building_door_replacement_8k_2011). Signed 2011-11-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20012M0163_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_fms_services_building_door_replacement_8k_2011 USD 0.008m. Supports misc_colombia_fms_services_building_door_replacement_8k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 7929.5; date_signed 2011-11-08.",
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
