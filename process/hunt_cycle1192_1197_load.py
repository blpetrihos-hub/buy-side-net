#!/usr/bin/env python3
"""Cycles 1192–1197: USASpending LatAm CapEx (US holdovers + residual other).

Seeds: 20262192–20262197. Thin top-up dry.
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

# === Cycle 1192 ===
row_doc(
    "norshield_mexico_febr_tijuana_msgr_552k_2018",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Mexico FEBR products manufacturing for Tijuana MSGR",
    "Mexico",
    "25 May 2018: Department of State awards contract 19AQMM18P1091 to NORSHIELD SECURITY PRODUCTS, LLC for FEBR products manufacturing for Tijuana MSGR project (PoP Mexico); obligated USD 552450. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "552450", "2018-05-25", "2018", "", "",
    "FEBR/MSGR manufacturing for Tijuana MSGR, Mexico (USASpending description; exact plant coords not stated — lat/lon blank).",
    "usaspending_norshield_mexico_febr_tijuana_msgr_552k_2018",
    "FUNDING FOR CONTINUED MANUFACTURING OF FEBR PRODUCTS FOR THE TIJUANA, MEXICO MSGR PROJECT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P1091_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1192",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18P1091_1900_-NONE-_-NONE- (norshield_mexico_febr_tijuana_msgr_552k_2018). Signed 2018-05-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18P1091_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_mexico_febr_tijuana_msgr_552k_2018 USD 0.552m. Supports norshield_mexico_febr_tijuana_msgr_552k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 552450.0; date_signed 2018-05-25.",
)

# === Cycle 1192 ===
row_doc(
    "cummins_honduras_gensets_5x20kw_1x15kw_105k_2014",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Honduras purchase of gensets (5×20kW and 1×15kW)",
    "Honduras",
    "25 Sep 2014: Department of State awards contract SHO80014F0349 to CUMMINS POWER GENERATION INC. for Purchase of gensets (5) 20kW and (1) 15kW (PoP Honduras); obligated USD 104687.30. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "104687.30", "2014-09-25", "2014", "", "",
    "Purchase of gensets (5) 20kW and (1) 15kW, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_cummins_honduras_gensets_5x20kw_1x15kw_105k_2014",
    "PURCHASE OF GENSETS (5) 20KW AND (1) 15KW",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80014F0349_1900_GS07F9004D_4730/",
    "Actor: CUMMINS POWER GENERATION INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1192",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80014F0349_1900_GS07F9004D_4730 (cummins_honduras_gensets_5x20kw_1x15kw_105k_2014). Signed 2014-09-25. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80014F0349_1900_GS07F9004D_4730/.",
    "USASpending: cummins_honduras_gensets_5x20kw_1x15kw_105k_2014 USD 0.105m. Supports cummins_honduras_gensets_5x20kw_1x15kw_105k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 104687.3; date_signed 2014-09-25.",
)

# === Cycle 1192 ===
row_doc(
    "misc_colombia_metal_detectors_garzon_velez_tunja_50k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia metal detectors for Garzon, Velez and Tunja",
    "Colombia",
    "15 Dec 2021: Department of State awards contract 19C01522P0070 for Metal detectors for Garzon, Velez and Tunja (PoP Colombia); obligated USD 49984.34. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "49984.34", "2021-12-15", "2021", "", "",
    "Metal detectors for Garzon, Velez and Tunja, Colombia (USASpending description; cities named, site coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_metal_detectors_garzon_velez_tunja_50k_2021",
    "42/METAL DETECTORS FOR GARZON, VELEZ AND TUNJA/0222",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01522P0070_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1192",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C01522P0070_1900_-NONE-_-NONE- (misc_colombia_metal_detectors_garzon_velez_tunja_50k_2021). Signed 2021-12-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C01522P0070_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_metal_detectors_garzon_velez_tunja_50k_2021 USD 0.050m. Supports misc_colombia_metal_detectors_garzon_velez_tunja_50k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49984.34; date_signed 2021-12-15.",
)

# === Cycle 1192 ===
row_doc(
    "misc_brazil_gso_electrical_data_cabling_restoration_50k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil GSO offices electrical/data cabling restoration",
    "Brazil",
    "3 May 2017: Department of State awards contract SBR25017M0631 for GSO offices electrical/data cabling restoration (PoP Brazil); obligated USD 49983.91. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "49983.91", "2017-05-03", "2017", "", "",
    "GSO offices electrical/data cabling restoration, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_gso_electrical_data_cabling_restoration_50k_2017",
    "GSO OFFICES ELETRICAL/DATA CABLING RESTORATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M0631_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1192",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR25017M0631_1900_-NONE-_-NONE- (misc_brazil_gso_electrical_data_cabling_restoration_50k_2017). Signed 2017-05-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR25017M0631_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_gso_electrical_data_cabling_restoration_50k_2017 USD 0.050m. Supports misc_brazil_gso_electrical_data_cabling_restoration_50k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49983.91; date_signed 2017-05-03.",
)

# === Cycle 1192 ===
row_doc(
    "misc_peru_anfac_cameras_supply_install_50k_2017",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru supply and install cameras in ANFAC building",
    "Peru",
    "17 Feb 2017: Department of State awards contract SPE50017M0777 for Supply and install cameras in ANFAC building (PoP Peru); obligated USD 49925.80. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "49925.80", "2017-02-17", "2017", "", "",
    "Cameras in ANFAC building, Peru (USASpending description; building named, coords not stated — lat/lon blank).",
    "usaspending_misc_peru_anfac_cameras_supply_install_50k_2017",
    "\"OTHER FUNCTION\" - IGF::OT::IGF SUPPLY AND INSTALL CAMERAS IN ANFAC BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50017M0777_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1192",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50017M0777_1900_-NONE-_-NONE- (misc_peru_anfac_cameras_supply_install_50k_2017). Signed 2017-02-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50017M0777_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_anfac_cameras_supply_install_50k_2017 USD 0.050m. Supports misc_peru_anfac_cameras_supply_install_50k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 49925.8; date_signed 2017-02-17.",
)

# === Cycle 1193 ===
row_doc(
    "applied_security_brazil_power_systems_sao_paulo_85k_2013",
    "energy", "power_plants_grid", "us",
    "Applied Security Technologies — Brazil power systems work São Paulo",
    "Brazil",
    "8 Apr 2013: Department of State awards contract SAQMMA13F1222 to APPLIED SECURITY TECHNOLOGIES INC for Power systems work São Paulo, Brasil (PoP Brazil); obligated USD 84904.81. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "84904.81", "2013-04-08", "2013", "", "",
    "Power systems work, São Paulo, Brazil (USASpending description; exact site coords not stated — lat/lon blank).",
    "usaspending_applied_security_brazil_power_systems_sao_paulo_85k_2013",
    "POWER SYSTEMS WORK SAO PAULO, BRASIL IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F1222_1900_SAQMMA07D0030_1900/",
    "Actor: APPLIED SECURITY TECHNOLOGIES INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1193",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA13F1222_1900_SAQMMA07D0030_1900 (applied_security_brazil_power_systems_sao_paulo_85k_2013). Signed 2013-04-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA13F1222_1900_SAQMMA07D0030_1900/.",
    "USASpending: applied_security_brazil_power_systems_sao_paulo_85k_2013 USD 0.085m. Supports applied_security_brazil_power_systems_sao_paulo_85k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 84904.81; date_signed 2013-04-08.",
)

# === Cycle 1193 ===
row_doc(
    "cummins_nicaragua_genset_ats_santo_domingo_apartments_33k_2013",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Nicaragua genset and ATS for Old Santo Domingo apartments OBO",
    "Nicaragua",
    "3 May 2013: Department of State awards contract SNU70013M0152 to CUMMINS POWER GENERATION INC. for Genset and ATS for Old Santo Domingo apartments — OBO (PoP Nicaragua); obligated USD 33208.95. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "33208.95", "2013-05-03", "2013", "", "",
    "Genset/ATS for Old Santo Domingo apartments, Nicaragua (USASpending description; site named, coords not stated — lat/lon blank).",
    "usaspending_cummins_nicaragua_genset_ats_santo_domingo_apartments_33k_2013",
    "GENSET AND ATS FOR OLD SANTO DOMINGO APARTMENTS - OBO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70013M0152_1900_-NONE-_-NONE-/",
    "Actor: CUMMINS POWER GENERATION INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1193",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SNU70013M0152_1900_-NONE-_-NONE- (cummins_nicaragua_genset_ats_santo_domingo_apartments_33k_2013). Signed 2013-05-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SNU70013M0152_1900_-NONE-_-NONE-/.",
    "USASpending: cummins_nicaragua_genset_ats_santo_domingo_apartments_33k_2013 USD 0.033m. Supports cummins_nicaragua_genset_ats_santo_domingo_apartments_33k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 33208.95; date_signed 2013-05-03.",
)

# === Cycle 1193 ===
row_doc(
    "trane_peru_gso_warehouse_air_conditioners_88k_2024",
    "energy", "power_plants_grid", "other",
    "Trane Technologies Peru — GSO warehouse air conditioners FAP",
    "Peru",
    "13 Jun 2024: Department of State awards contract 19PE5024P1098 for GSO warehouse air conditioners FAP (PoP Peru); obligated USD 87650.40. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "87650.40", "2024-06-13", "2024", "", "",
    "GSO warehouse air conditioners FAP, Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_trane_peru_gso_warehouse_air_conditioners_88k_2024",
    "GSO WAREHOUSE - AIR CONDITIONERS FAP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5024P1098_1900_-NONE-_-NONE-/",
    "Actor: TRANE TECHNOLOGIES PERU S.A.C. (Peru-incorporated) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1193",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5024P1098_1900_-NONE-_-NONE- (trane_peru_gso_warehouse_air_conditioners_88k_2024). Signed 2024-06-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5024P1098_1900_-NONE-_-NONE-/.",
    "USASpending: trane_peru_gso_warehouse_air_conditioners_88k_2024 USD 0.088m. Supports trane_peru_gso_warehouse_air_conditioners_88k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 87650.4; date_signed 2024-06-13.",
)

# === Cycle 1193 ===
row_doc(
    "misc_panama_courtroom_av_equipment_install_14k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Panama installation-integration of A/V equipment for courtrooms",
    "Panama",
    "3 Jun 2021: Department of State awards contract 19PM0721P0534 for Installation-integration services of A/V equipment for courtrooms (PoP Panama); obligated USD 14500. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14500", "2021-06-03", "2021", "", "",
    "Installation-integration services of A/V equipment for courtrooms, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_panama_courtroom_av_equipment_install_14k_2021",
    "INSTALLATION-INTEGRATION SERVICES OF A/V EQUIPMENT FOR COURTROOMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0721P0534_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1193",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PM0721P0534_1900_-NONE-_-NONE- (misc_panama_courtroom_av_equipment_install_14k_2021). Signed 2021-06-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PM0721P0534_1900_-NONE-_-NONE-/.",
    "USASpending: misc_panama_courtroom_av_equipment_install_14k_2021 USD 0.015m. Supports misc_panama_courtroom_av_equipment_install_14k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14500.0; date_signed 2021-06-03.",
)

# === Cycle 1193 ===
row_doc(
    "misc_dominican_duncan_tye_make_ready_14k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic landlord make-ready work for Duncan Tye residence",
    "Dominican Republic",
    "3 Sep 2014: Department of State awards contract SDR86014M2197 for Landlord make-ready work for Duncan Tye residence (PoP Dominican Republic); obligated USD 13998.61. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13998.61", "2014-09-03", "2014", "", "",
    "Duncan Tye residence make-ready, Dominican Republic (USASpending description; residence named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_duncan_tye_make_ready_14k_2014",
    "LANDLORD MAKE READY WORK FOR DUNCAN TYE RESIDENCE: IGF::CL::IGF FOR CLOSELY ASSOCIATED",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M2197_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1193",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86014M2197_1900_-NONE-_-NONE- (misc_dominican_duncan_tye_make_ready_14k_2014). Signed 2014-09-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86014M2197_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_duncan_tye_make_ready_14k_2014 USD 0.014m. Supports misc_dominican_duncan_tye_make_ready_14k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13998.61; date_signed 2014-09-03.",
)

# === Cycle 1194 ===
row_doc(
    "cummins_belize_marigold_st_genset_26k_2015",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Belize Marigold St genset",
    "Belize",
    "28 Sep 2015: Department of State awards contract SBH20015M0369 to CUMMINS POWER GENERATION INC. for FM mechanical Marigold St genset (PoP Belize); obligated USD 25999.99. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "25999.99", "2015-09-28", "2015", "", "",
    "Marigold St genset, Belize (USASpending description; street named, coords not stated — lat/lon blank).",
    "usaspending_cummins_belize_marigold_st_genset_26k_2015",
    "FM - MECHANICAL - MARIGOLD ST GENSET",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20015M0369_1900_-NONE-_-NONE-/",
    "Actor: CUMMINS POWER GENERATION INC. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1194",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20015M0369_1900_-NONE-_-NONE- (cummins_belize_marigold_st_genset_26k_2015). Signed 2015-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20015M0369_1900_-NONE-_-NONE-/.",
    "USASpending: cummins_belize_marigold_st_genset_26k_2015 USD 0.026m. Supports cummins_belize_marigold_st_genset_26k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 25999.99; date_signed 2015-09-28.",
)

# === Cycle 1194 ===
row_doc(
    "datum_filing_costa_rica_new_filing_system_20k_2012",
    "infrastructure", "building_materials", "us",
    "Datum Filing Systems — Costa Rica new filing system",
    "Costa Rica",
    "10 Sep 2012: Department of State awards contract SCS80012M0793 to DATUM FILING SYSTEMS, INC. for CONS new filing system (PoP Costa Rica); obligated USD 20000. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "20000", "2012-09-10", "2012", "", "",
    "CONS new filing system, Costa Rica (USASpending description; site not named — lat/lon blank).",
    "usaspending_datum_filing_costa_rica_new_filing_system_20k_2012",
    "CONS - NEW FILING SYSTEM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80012M0793_1900_-NONE-_-NONE-/",
    "Actor: DATUM FILING SYSTEMS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1194",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCS80012M0793_1900_-NONE-_-NONE- (datum_filing_costa_rica_new_filing_system_20k_2012). Signed 2012-09-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCS80012M0793_1900_-NONE-_-NONE-/.",
    "USASpending: datum_filing_costa_rica_new_filing_system_20k_2012 USD 0.020m. Supports datum_filing_costa_rica_new_filing_system_20k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 20000.0; date_signed 2012-09-10.",
)

# === Cycle 1194 ===
row_doc(
    "misc_dominican_make_ready_lbb19_14k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic FAC make-ready work LBB 19",
    "Dominican Republic",
    "15 Apr 2025: Department of State awards contract 19DR8625C0029 for FAC make-ready work LBB 19 PID 844 (PoP Dominican Republic); obligated USD 14479.13. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "14479.13", "2025-04-15", "2025", "", "",
    "FAC make-ready work LBB 19 PID 844, Dominican Republic (USASpending description; residence named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_make_ready_lbb19_14k_2025",
    "FAC-MAKE READY WORK LBB 19 PID 844 CONS - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8625C0029_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1194",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8625C0029_1900_-NONE-_-NONE- (misc_dominican_make_ready_lbb19_14k_2025). Signed 2025-04-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8625C0029_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_make_ready_lbb19_14k_2025 USD 0.014m. Supports misc_dominican_make_ready_lbb19_14k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14479.13; date_signed 2025-04-15.",
)

# === Cycle 1194 ===
row_doc(
    "misc_colombia_metal_bunk_beds_jungla_caucacia_14k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia metal bunk beds for Jungla camp Caucacia",
    "Colombia",
    "12 Mar 2013: Department of State awards contract SCO15013M0531 for Metal bunk beds for Jungla camp (Caucacia) (PoP Colombia); obligated USD 14415.58. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "14415.58", "2013-03-12", "2013", "", "",
    "Jungla camp Caucacia metal bunk beds, Colombia (USASpending description; camp named, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_metal_bunk_beds_jungla_caucacia_14k_2013",
    "INTER (J) / METAL BUNK BEDS FOR JUNGLA CAMP (CAUCACIA)",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0531_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1194",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO15013M0531_1900_-NONE-_-NONE- (misc_colombia_metal_bunk_beds_jungla_caucacia_14k_2013). Signed 2013-03-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO15013M0531_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_metal_bunk_beds_jungla_caucacia_14k_2013 USD 0.014m. Supports misc_colombia_metal_bunk_beds_jungla_caucacia_14k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14415.58; date_signed 2013-03-12.",
)

# === Cycle 1194 ===
row_doc(
    "misc_mexico_nvl_parking_lot_awning_14k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico NVL program awning for parking lot",
    "Mexico",
    "28 Sep 2010: Department of State awards contract SMX61010M0041 for NVL program awning for parking lot (PoP Mexico); obligated USD 14369.04. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14369.04", "2010-09-28", "2010", "", "",
    "NVL program awning for parking lot, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_nvl_parking_lot_awning_14k_2010",
    "NVL/ PROGRAM/ AWNING FOR PARKING LOT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX61010M0041_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1194",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX61010M0041_1900_-NONE-_-NONE- (misc_mexico_nvl_parking_lot_awning_14k_2010). Signed 2010-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX61010M0041_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_nvl_parking_lot_awning_14k_2010 USD 0.014m. Supports misc_mexico_nvl_parking_lot_awning_14k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14369.04; date_signed 2010-09-28.",
)

# === Cycle 1195 ===
row_doc(
    "assa_abloy_jamaica_metal_door_screen_panel_11k_2025",
    "infrastructure", "building_materials", "us",
    "ASSA ABLOY Specialty Doors — Jamaica metal door screen panel for international embassies",
    "Jamaica",
    "11 Sep 2025: Department of State awards contract 19AQMM25P0219 to ASSA ABLOY SPECIALTY DOORS, LLC for Metal door screen panel etc. for international embassies (PoP Jamaica); obligated USD 11135. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "11135", "2025-09-11", "2025", "", "",
    "Metal door screen panel etc. for international embassies, Jamaica (USASpending description; site not named — lat/lon blank).",
    "usaspending_assa_abloy_jamaica_metal_door_screen_panel_11k_2025",
    "METAL DOOR SCREEN PANEL ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0219_1900_-NONE-_-NONE-/",
    "Actor: ASSA ABLOY SPECIALTY DOORS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1195",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25P0219_1900_-NONE-_-NONE- (assa_abloy_jamaica_metal_door_screen_panel_11k_2025). Signed 2025-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25P0219_1900_-NONE-_-NONE-/.",
    "USASpending: assa_abloy_jamaica_metal_door_screen_panel_11k_2025 USD 0.011m. Supports assa_abloy_jamaica_metal_door_screen_panel_11k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11135.0; date_signed 2025-09-11.",
)

# === Cycle 1195 ===
row_doc(
    "fabrication_designs_venezuela_metal_door_screen_11k_2019",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Venezuela metal door screen",
    "Venezuela",
    "5 Jun 2019: Department of State awards contract 19AQMM19P0842 to FABRICATION DESIGNS, INC. for Metal door screen etc. (PoP Venezuela); obligated USD 10902. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "10902", "2019-06-05", "2019", "", "",
    "Metal door screen etc., Venezuela (USASpending description; site not named — lat/lon blank).",
    "usaspending_fabrication_designs_venezuela_metal_door_screen_11k_2019",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0842_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1195",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19P0842_1900_-NONE-_-NONE- (fabrication_designs_venezuela_metal_door_screen_11k_2019). Signed 2019-06-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19P0842_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_venezuela_metal_door_screen_11k_2019 USD 0.011m. Supports fabrication_designs_venezuela_metal_door_screen_11k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10902.0; date_signed 2019-06-05.",
)

# === Cycle 1195 ===
row_doc(
    "misc_bahamas_cmr_5ton_ac_replacement_14k_2026",
    "energy", "power_plants_grid", "other",
    "Miscellaneous foreign awardees — Bahamas CMR 5-ton air-condition replacement",
    "Bahamas",
    "10 Jun 2026: Department of State awards contract 19BF5026P0311 for CMR 5-ton air-condition replacement (PoP Bahamas); obligated USD 14322.94. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14322.94", "2026-06-10", "2026", "", "",
    "CMR 5-ton air-condition replacement, Bahamas (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_bahamas_cmr_5ton_ac_replacement_14k_2026",
    "CMR - 5TON AIR-CONDITION REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5026P0311_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1195",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BF5026P0311_1900_-NONE-_-NONE- (misc_bahamas_cmr_5ton_ac_replacement_14k_2026). Signed 2026-06-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BF5026P0311_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_cmr_5ton_ac_replacement_14k_2026 USD 0.014m. Supports misc_bahamas_cmr_5ton_ac_replacement_14k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14322.94; date_signed 2026-06-10.",
)

# === Cycle 1195 ===
row_doc(
    "misc_dominican_make_ready_lbb05_14k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic PROG make-ready LBB#05",
    "Dominican Republic",
    "2 Aug 2022: Department of State awards contract 19DR8622C0028 for PROG make-ready LBB#05 PID 864 (PoP Dominican Republic); obligated USD 14248.82. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "14248.82", "2022-08-02", "2022", "", "",
    "PROG make-ready LBB#05 PID 864, Dominican Republic (USASpending description; residence named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_make_ready_lbb05_14k_2022",
    "PROG-MAKE READY LBB#05 PID 864 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622C0028_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1195",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8622C0028_1900_-NONE-_-NONE- (misc_dominican_make_ready_lbb05_14k_2022). Signed 2022-08-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8622C0028_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_make_ready_lbb05_14k_2022 USD 0.014m. Supports misc_dominican_make_ready_lbb05_14k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14248.82; date_signed 2022-08-02.",
)

# === Cycle 1195 ===
row_doc(
    "misc_dominican_make_ready_los_bambues_12_14k_2024",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic OSC make-ready Los Bambues 12",
    "Dominican Republic",
    "16 Jul 2024: Department of State awards contract 19DR8624C0059 for OSC make-ready work Los Bambues 12 PID 796 (PoP Dominican Republic); obligated USD 14127.81. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "14127.81", "2024-07-16", "2024", "", "",
    "OSC make-ready work Los Bambues 12 PID 796, Dominican Republic (USASpending description; residence named, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_make_ready_los_bambues_12_14k_2024",
    "OSC MAKE READY WORK LOS BAMBUES 12 PID 796 - AWARD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0059_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1195",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8624C0059_1900_-NONE-_-NONE- (misc_dominican_make_ready_los_bambues_12_14k_2024). Signed 2024-07-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8624C0059_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_make_ready_los_bambues_12_14k_2024 USD 0.014m. Supports misc_dominican_make_ready_los_bambues_12_14k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14127.81; date_signed 2024-07-16.",
)

# === Cycle 1196 ===
row_doc(
    "norshield_jamaica_metal_door_screen_10k_2020",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Jamaica metal door screen",
    "Jamaica",
    "23 Apr 2020: Department of State awards contract 19AQMM20P0748 to NORSHIELD SECURITY PRODUCTS, LLC for Metal door screen etc. (PoP Jamaica); obligated USD 10260. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "10260", "2020-04-23", "2020", "", "",
    "Metal door screen etc., Jamaica (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_jamaica_metal_door_screen_10k_2020",
    "METAL DOOR SCREEN ETC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0748_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1196",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20P0748_1900_-NONE-_-NONE- (norshield_jamaica_metal_door_screen_10k_2020). Signed 2020-04-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20P0748_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_jamaica_metal_door_screen_10k_2020 USD 0.010m. Supports norshield_jamaica_metal_door_screen_10k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 10260.0; date_signed 2020-04-23.",
)

# === Cycle 1196 ===
row_doc(
    "fabrication_designs_ecuador_metal_door_screen_10k_2017",
    "infrastructure", "building_materials", "us",
    "Fabrication Designs — Ecuador metal door screen",
    "Ecuador",
    "3 Apr 2017: Department of State awards contract SAQMMA17M0297 to FABRICATION DESIGNS, INC. for Metal door, screen (PoP Ecuador); obligated USD 9942.55. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "9942.55", "2017-04-03", "2017", "", "",
    "Metal door, screen, Ecuador (USASpending description; site not named — lat/lon blank).",
    "usaspending_fabrication_designs_ecuador_metal_door_screen_10k_2017",
    "METAL DOOR, SCREEN IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0297_1900_-NONE-_-NONE-/",
    "Actor: FABRICATION DESIGNS, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1196",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17M0297_1900_-NONE-_-NONE- (fabrication_designs_ecuador_metal_door_screen_10k_2017). Signed 2017-04-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0297_1900_-NONE-_-NONE-/.",
    "USASpending: fabrication_designs_ecuador_metal_door_screen_10k_2017 USD 0.010m. Supports fabrication_designs_ecuador_metal_door_screen_10k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9942.55; date_signed 2017-04-03.",
)

# === Cycle 1196 ===
row_doc(
    "misc_mexico_fac_make_ready_works_14k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico FAC make-ready works",
    "Mexico",
    "12 Jul 2013: Department of State awards contract SMX53013M0997 for FAC make-ready works (PoP Mexico); obligated USD 14039.85. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "14039.85", "2013-07-12", "2013", "", "",
    "FAC make-ready works, Mexico (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_mexico_fac_make_ready_works_14k_2013",
    "MEX/FAC-MAKE READY WORKS IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0997_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1196",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53013M0997_1900_-NONE-_-NONE- (misc_mexico_fac_make_ready_works_14k_2013). Signed 2013-07-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53013M0997_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_fac_make_ready_works_14k_2013 USD 0.014m. Supports misc_mexico_fac_make_ready_works_14k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 14039.85; date_signed 2013-07-12.",
)

# === Cycle 1196 ===
row_doc(
    "misc_bahamas_security_grills_dcr_fabricate_install_14k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Bahamas fabrication and installation of security grills at DCR",
    "Bahamas",
    "5 Jun 2014: Department of State awards contract SBF50014M0563 for Fabrication and installation of security grills at DCR (PoP Bahamas); obligated USD 13921. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13921", "2014-06-05", "2014", "", "",
    "Fabrication and installation of security grills at DCR, Bahamas (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_bahamas_security_grills_dcr_fabricate_install_14k_2014",
    "PC-C-FABRICATION AND INSTALLATION OF SECURITY GRILLS AT DCR IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50014M0563_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1196",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50014M0563_1900_-NONE-_-NONE- (misc_bahamas_security_grills_dcr_fabricate_install_14k_2014). Signed 2014-06-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50014M0563_1900_-NONE-_-NONE-/.",
    "USASpending: misc_bahamas_security_grills_dcr_fabricate_install_14k_2014 USD 0.014m. Supports misc_bahamas_security_grills_dcr_fabricate_install_14k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13921.0; date_signed 2014-06-05.",
)

# === Cycle 1196 ===
row_doc(
    "misc_belize_slide_gates_rails_replace_14k_2016",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Belize replacement of slide gates and rails at CACS",
    "Belize",
    "20 Jul 2016: Department of State awards contract SBH20016M0332 for Replacement of slide gates, rails at CACS (PoP Belize); obligated USD 13905. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13905", "2016-07-20", "2016", "", "",
    "Replacement of slide gates, rails at CACS, Belize (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_belize_slide_gates_rails_replace_14k_2016",
    "IGF::OT::IGFFM - REPLACEMENT OF SLIDE GATES, RAILS AT CACS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20016M0332_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1196",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBH20016M0332_1900_-NONE-_-NONE- (misc_belize_slide_gates_rails_replace_14k_2016). Signed 2016-07-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBH20016M0332_1900_-NONE-_-NONE-/.",
    "USASpending: misc_belize_slide_gates_rails_replace_14k_2016 USD 0.014m. Supports misc_belize_slide_gates_rails_replace_14k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13905.0; date_signed 2016-07-20.",
)

# === Cycle 1197 ===
row_doc(
    "norshield_brazil_metal_door_screen_embassies_10k_2023",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Brazil metal door screen for international embassies",
    "Brazil",
    "7 Mar 2023: Department of State awards contract 19AQMM23P0310 to NORSHIELD SECURITY PRODUCTS, LLC for Metal door screen etc. for international embassies (PoP Brazil); obligated USD 9845. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "9845", "2023-03-07", "2023", "", "",
    "Metal door screen etc. for international embassies, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_brazil_metal_door_screen_embassies_10k_2023",
    "METAL DOOR SCREEN ETC. FOR INTERNATIONAL EMBASSIES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0310_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1197",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23P0310_1900_-NONE-_-NONE- (norshield_brazil_metal_door_screen_embassies_10k_2023). Signed 2023-03-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23P0310_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_brazil_metal_door_screen_embassies_10k_2023 USD 0.010m. Supports norshield_brazil_metal_door_screen_embassies_10k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9845.0; date_signed 2023-03-07.",
)

# === Cycle 1197 ===
row_doc(
    "norshield_uruguay_metal_door_screen_10k_2017",
    "infrastructure", "building_materials", "us",
    "Norshield Security Products — Uruguay metal door screen",
    "Uruguay",
    "13 Jun 2017: Department of State awards contract SAQMMA17M0982 to NORSHIELD SECURITY PRODUCTS, LLC for Metal door screen etc. (PoP Uruguay); obligated USD 9580. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "9580", "2017-06-13", "2017", "", "",
    "Metal door screen etc., Uruguay (USASpending description; site not named — lat/lon blank).",
    "usaspending_norshield_uruguay_metal_door_screen_10k_2017",
    "METAL DOOR SCREEN ETC. IGF::CL::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0982_1900_-NONE-_-NONE-/",
    "Actor: NORSHIELD SECURITY PRODUCTS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1197",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17M0982_1900_-NONE-_-NONE- (norshield_uruguay_metal_door_screen_10k_2017). Signed 2017-06-13. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17M0982_1900_-NONE-_-NONE-/.",
    "USASpending: norshield_uruguay_metal_door_screen_10k_2017 USD 0.010m. Supports norshield_uruguay_metal_door_screen_10k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9580.0; date_signed 2017-06-13.",
)

# === Cycle 1197 ===
row_doc(
    "misc_el_salvador_metallic_fence_security_boxes_14k_2011",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador installation metallic fence over walls and security boxes",
    "El Salvador",
    "12 Sep 2011: Department of State awards contract SES60011M1038 for Installation metallic fence over walls and security boxes (PoP El Salvador); obligated USD 13899. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13899", "2011-09-12", "2011", "", "",
    "Installation metallic fence over walls and security boxes, El Salvador (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_el_salvador_metallic_fence_security_boxes_14k_2011",
    "CSL- INSTALLATION METALLIC FENCE OVER WALLS AND SECURITY BOXES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60011M1038_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1197",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SES60011M1038_1900_-NONE-_-NONE- (misc_el_salvador_metallic_fence_security_boxes_14k_2011). Signed 2011-09-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SES60011M1038_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_metallic_fence_security_boxes_14k_2011 USD 0.014m. Supports misc_el_salvador_metallic_fence_security_boxes_14k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13899.0; date_signed 2011-09-12.",
)

# === Cycle 1197 ===
row_doc(
    "misc_el_salvador_grilles_install_calle_tlacatl_14k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — El Salvador RSO grilles installation Calle Tlacatl #30",
    "El Salvador",
    "6 Jun 2022: Department of State awards contract 19ES6022P0516 for Grilles installation Calle Tlacatl #30 (PoP El Salvador); obligated USD 13895. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "13895", "2022-06-06", "2022", "", "",
    "Grilles installation Calle Tlacatl #30, El Salvador (USASpending description; address named, coords not stated — lat/lon blank).",
    "usaspending_misc_el_salvador_grilles_install_calle_tlacatl_14k_2022",
    "19ES6022P0516 RSO 5841 GRILLES INSTALLATION CALLE ATLACATL #30",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0516_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1197",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19ES6022P0516_1900_-NONE-_-NONE- (misc_el_salvador_grilles_install_calle_tlacatl_14k_2022). Signed 2022-06-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19ES6022P0516_1900_-NONE-_-NONE-/.",
    "USASpending: misc_el_salvador_grilles_install_calle_tlacatl_14k_2022 USD 0.014m. Supports misc_el_salvador_grilles_install_calle_tlacatl_14k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13895.0; date_signed 2022-06-06.",
)

# === Cycle 1197 ===
row_doc(
    "misc_peru_structural_roof_replace_mechanic_shop_14k_2013",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru replace structural roof (mechanic shop)",
    "Peru",
    "15 Aug 2013: Department of State awards contract SPE50013C0023 for Replace structural roof (mechanic shop) (PoP Peru); obligated USD 13924. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "13924", "2013-08-15", "2013", "", "",
    "Replace structural roof (mechanic shop), Peru (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_peru_structural_roof_replace_mechanic_shop_14k_2013",
    "CONTRACT TO REPLACE STRUCTURAL ROOF (MECHANIC SHOP) IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50013C0023_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1197",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50013C0023_1900_-NONE-_-NONE- (misc_peru_structural_roof_replace_mechanic_shop_14k_2013). Signed 2013-08-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50013C0023_1900_-NONE-_-NONE-/.",
    "USASpending: misc_peru_structural_roof_replace_mechanic_shop_14k_2013 USD 0.014m. Supports misc_peru_structural_roof_replace_mechanic_shop_14k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 13924.0; date_signed 2013-08-15.",
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
