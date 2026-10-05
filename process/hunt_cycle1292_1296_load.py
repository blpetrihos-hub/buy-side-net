#!/usr/bin/env python3
"""Cycles 1292–1296: USASpending LatAm CapEx (Alutiiq radio/IT + Bendig/Desarrollo + residual).

Seeds: 20262292–20262296. Thin top-up dry.
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

# === Cycle 1292 ===
row_doc(
    "alutiiq_mexico_p25_radio_network_43402k_2018",
    "infrastructure", "building_materials", "us",
    "Alutiiq Information Management — Mexico P-25 trunked radio communications network",
    "Mexico",
    "7 Jun 2018: Department of State awards contract to ALUTIIQ INFORMATION MANAGEMENT, LLC for P-25 trunked radio communications network for police/military interoperability (PoP Mexico); obligated USD 43402531.91. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "43402531.91", "2018-06-07", "2018", "", "",
    "IGF::OT::IGF THE PURPOSE OF THIS PROJECT IS TO PROVIDE A P-25 TRUNKED RADIO COMMUNICATIONS NETWORK THAT WILL P, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_p25_radio_network_43402k_2018",
    "IGF::OT::IGF THE PURPOSE OF THIS PROJECT IS TO PROVIDE A P-25 TRUNKED RADIO COMMUNICATIONS NETWORK THAT WILL PROVIDE A FULL INTEROPERABILITY, SECURE VOICE/DATA COMMUNICATIONS SYSTEM WITH THE ABILITY TO SHARE CRITICAL, REAL-TIME INFORMATION SUPPORTING A WIDE RANGE OF OPERATIONS FOR POLICE, MILITARY, IMMIGRATION AND CUSTOMS OFFICES IN EIGHT SOUTHERN-BORDER STATES OF MEXICO (CAMPECHE, CHIAPAS, GUERRERO, OAXACA, QUINTANA ROO, TABASCO, VERACRUZ, AND YUCATAN).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0113_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ INFORMATION MANAGEMENT, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1292",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0113_1900_-NONE-_-NONE- (alutiiq_mexico_p25_radio_network_43402k_2018). Signed 2018-06-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0113_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_p25_radio_network_43402k_2018 USD 43.403m. Supports alutiiq_mexico_p25_radio_network_43402k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 43402531.91; date_signed 2018-06-07.",
    investment_type="equipment_supply",
)

# === Cycle 1292 ===
row_doc(
    "alutiiq_mexico_setec_it_comms_18259k_2016",
    "infrastructure", "building_materials", "us",
    "Alutiiq Essential Services — Mexico SETEC IT and communications infrastructure",
    "Mexico",
    "11 Jul 2016: Department of State awards contract to ALUTIIQ ESSENTIAL SERVICES LLC for INL Mexico SETEC IT and communications infrastructure provision/delivery/installation (PoP Mexico); obligated USD 18259969.20. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "18259969.20", "2016-07-11", "2016", "", "",
    "IGF::OT::IGF  INL MEXICO SETEC IT AND COMMUNICATIONS INFRASTRUCTURE PROJECT: PROVISION, DELIVERY, INSTALLATION, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_setec_it_comms_18259k_2016",
    "IGF::OT::IGF  INL MEXICO SETEC IT AND COMMUNICATIONS INFRASTRUCTURE PROJECT: PROVISION, DELIVERY, INSTALLATION, AND WARRANTY AND SUPPORT OF A VARIETY OF IT AND COMMUNICATIONS EQUIPMENT AND SOFTWARE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16C0006_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ ESSENTIAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1292",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC16C0006_1900_-NONE-_-NONE- (alutiiq_mexico_setec_it_comms_18259k_2016). Signed 2016-07-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC16C0006_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_setec_it_comms_18259k_2016 USD 18.260m. Supports alutiiq_mexico_setec_it_comms_18259k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 18259969.2; date_signed 2016-07-11.",
    investment_type="equipment_supply",
)

# === Cycle 1292 ===
row_doc(
    "industrias_bendig_costarica_oij_shooting_range_511k_2023",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — Costa Rica OIJ shooting range",
    "Costa Rica",
    "2 Jun 2023: Department of State awards contract to INDUSTRIAS BENDIG SA for OIJ shooting range (PoP Costa Rica); obligated USD 511038.86. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "511038.86", "2023-06-02", "2023", "", "",
    "OIJ SHOOTING RANGE, COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_industrias_bendig_costarica_oij_shooting_range_511k_2023",
    "OIJ SHOOTING RANGE, COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23C0074_1900_-NONE-_-NONE-/",
    "Actor: INDUSTRIAS BENDIG SA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1292",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23C0074_1900_-NONE-_-NONE- (industrias_bendig_costarica_oij_shooting_range_511k_2023). Signed 2023-06-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23C0074_1900_-NONE-_-NONE-/.",
    "USASpending: industrias_bendig_costarica_oij_shooting_range_511k_2023 USD 0.511m. Supports industrias_bendig_costarica_oij_shooting_range_511k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 511038.86; date_signed 2023-06-02.",
    investment_type="epc",
)

# === Cycle 1292 ===
row_doc(
    "industrias_bendig_costarica_puerto_viejo_police_422k_2023",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — Costa Rica Puerto Viejo police station",
    "Costa Rica",
    "21 Apr 2023: Department of State awards contract to INDUSTRIAS BENDIG SA for police station Puerto Viejo (PoP Costa Rica); obligated USD 422879. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "422879", "2023-04-21", "2023", "", "",
    "POLICE STATION, PUERTO VIEJO, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_industrias_bendig_costarica_puerto_viejo_police_422k_2023",
    "POLICE STATION, PUERTO VIEJO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23C0034_1900_-NONE-_-NONE-/",
    "Actor: INDUSTRIAS BENDIG SA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1292",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM23C0034_1900_-NONE-_-NONE- (industrias_bendig_costarica_puerto_viejo_police_422k_2023). Signed 2023-04-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23C0034_1900_-NONE-_-NONE-/.",
    "USASpending: industrias_bendig_costarica_puerto_viejo_police_422k_2023 USD 0.423m. Supports industrias_bendig_costarica_puerto_viejo_police_422k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 422879.0; date_signed 2023-04-21.",
    investment_type="epc",
)

# === Cycle 1292 ===
row_doc(
    "industrias_bendig_costarica_inl_rappel_403k_2019",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — Costa Rica INL rappel facility",
    "Costa Rica",
    "29 Sep 2019: Department of State awards contract to INDUSTRIAS BENDIG SA for INL rappel facility contract (PoP Costa Rica); obligated USD 403200. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "403200", "2019-09-29", "2019", "", "",
    "INDUSTRIAS BENDIG  CONTRACT: 19AQMM19-C-0159 INL RAPPEL TOWER MURCIELAGO PERIOD OF PERFORMANCE: 120 CALENDAR D, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_industrias_bendig_costarica_inl_rappel_403k_2019",
    "INDUSTRIAS BENDIG  CONTRACT: 19AQMM19-C-0159 INL RAPPEL TOWER MURCIELAGO PERIOD OF PERFORMANCE: 120 CALENDAR DAYS AFTER ISSUANCE OF NTP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0159_1900_-NONE-_-NONE-/",
    "Actor: INDUSTRIAS BENDIG SA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1292",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0159_1900_-NONE-_-NONE- (industrias_bendig_costarica_inl_rappel_403k_2019). Signed 2019-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0159_1900_-NONE-_-NONE-/.",
    "USASpending: industrias_bendig_costarica_inl_rappel_403k_2019 USD 0.403m. Supports industrias_bendig_costarica_inl_rappel_403k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 403200.0; date_signed 2019-09-29.",
    investment_type="epc",
)

# === Cycle 1293 ===
row_doc(
    "alutiiq_colombia_bogota_radio_comms_15350k_2018",
    "infrastructure", "building_materials", "us",
    "Alutiiq Technical Services — Bogotá INL radio communications project",
    "Colombia",
    "28 Feb 2018: Department of State awards contract to ALUTIIQ TECHNICAL SERVICES LLC for INL Bogota radio communications project provision/delivery of radio and satellite equipment (PoP Colombia); obligated USD 15350865.74. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "15350865.74", "2018-02-28", "2018", "", "",
    "INL BOGOTA RADIO COMMUNICATIONS PROJECT: PROVISION, DELIVERY, TRAINING, AND LOCAL SUPPORT FOR A VARIETY OF RAD, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_colombia_bogota_radio_comms_15350k_2018",
    "INL BOGOTA RADIO COMMUNICATIONS PROJECT: PROVISION, DELIVERY, TRAINING, AND LOCAL SUPPORT FOR A VARIETY OF RADIO AND SATELLITE COMMUNICATIONS EQUIPMENT.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19WHAR18C0001_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ TECHNICAL SERVICES LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1293",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19WHAR18C0001_1900_-NONE-_-NONE- (alutiiq_colombia_bogota_radio_comms_15350k_2018). Signed 2018-02-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19WHAR18C0001_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_colombia_bogota_radio_comms_15350k_2018 USD 15.351m. Supports alutiiq_colombia_bogota_radio_comms_15350k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 15350865.74; date_signed 2018-02-28.",
    investment_type="equipment_supply",
)

# === Cycle 1293 ===
row_doc(
    "human_tech_colombia_rapid_shelter_systems_270k_2024",
    "infrastructure", "building_materials", "us",
    "Human Technologies — Colombia rapid shelter systems",
    "Colombia",
    "9 Sep 2024: Department of State awards contract to HUMAN TECHNOLOGIES CORP for Colombia rapid shelter systems (PoP Colombia); obligated USD 270103.93. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "270103.93", "2024-09-09", "2024", "", "",
    "COLOMBIA RAPID SHELTER SYSTEMS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_human_tech_colombia_rapid_shelter_systems_270k_2024",
    "COLOMBIA RAPID SHELTER SYSTEMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0053_1900_19AQMM21D0007_1900/",
    "Actor: HUMAN TECHNOLOGIES CORP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1293",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24F0053_1900_19AQMM21D0007_1900 (human_tech_colombia_rapid_shelter_systems_270k_2024). Signed 2024-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0053_1900_19AQMM21D0007_1900/.",
    "USASpending: human_tech_colombia_rapid_shelter_systems_270k_2024 USD 0.270m. Supports human_tech_colombia_rapid_shelter_systems_270k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 270103.93; date_signed 2024-09-09.",
    investment_type="equipment_supply",
)

# === Cycle 1293 ===
row_doc(
    "industrias_bendig_costarica_mag_monitoring_center_342k_2019",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — Costa Rica MAG monitoring center building Santa Rosa",
    "Costa Rica",
    "28 Sep 2019: Department of State awards contract to INDUSTRIAS BENDIG SA for MAG monitoring center building in Santa Rosa district (PoP Costa Rica); obligated USD 342870.51. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "342870.51", "2019-09-28", "2019", "", "",
    "THE MAG MONITORING CENTER BUILDING IN SANTA ROSA DISTRICT, SANTO DOMINGO CANTON, HEREDIA PROVINCE, COSTA RICA , Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_industrias_bendig_costarica_mag_monitoring_center_342k_2019",
    "THE MAG MONITORING CENTER BUILDING IN SANTA ROSA DISTRICT, SANTO DOMINGO CANTON, HEREDIA PROVINCE, COSTA RICA IS AN INFRASTRUCTURE PROJECT TO RETROFIT A BUILDING TO BE USED AS A MONITORING CENTER.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0162_1900_-NONE-_-NONE-/",
    "Actor: INDUSTRIAS BENDIG SA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1293",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0162_1900_-NONE-_-NONE- (industrias_bendig_costarica_mag_monitoring_center_342k_2019). Signed 2019-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0162_1900_-NONE-_-NONE-/.",
    "USASpending: industrias_bendig_costarica_mag_monitoring_center_342k_2019 USD 0.343m. Supports industrias_bendig_costarica_mag_monitoring_center_342k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 342870.51; date_signed 2019-09-28.",
    investment_type="epc",
)

# === Cycle 1293 ===
row_doc(
    "desarrollo_integral_colombia_cmr_ramps_212k_2024",
    "infrastructure", "building_materials", "other",
    "Desarrollo Integral Proyectos — Colombia CMR accessibility ramps",
    "Colombia",
    "24 Sep 2024: Department of State awards contract to DESARROLLO INTEGRAL PROYECTOS INGENIERIA LIMITADA for CMR accessibility ramps X2002 (PoP Colombia); obligated USD 212986.30. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "212986.30", "2024-09-24", "2024", "", "",
    "PR12937039: CMR ACCESSIBILITY RAMPS X2002 - 7919, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_desarrollo_integral_colombia_cmr_ramps_212k_2024",
    "PR12937039: CMR ACCESSIBILITY RAMPS X2002 - 7919",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024C0013_1900_-NONE-_-NONE-/",
    "Actor: DESARROLLO INTEGRAL PROYECTOS INGENIERIA LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1293",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02024C0013_1900_-NONE-_-NONE- (desarrollo_integral_colombia_cmr_ramps_212k_2024). Signed 2024-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024C0013_1900_-NONE-_-NONE-/.",
    "USASpending: desarrollo_integral_colombia_cmr_ramps_212k_2024 USD 0.213m. Supports desarrollo_integral_colombia_cmr_ramps_212k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 212986.3; date_signed 2024-09-24.",
    investment_type="epc",
)

# === Cycle 1293 ===
row_doc(
    "desarrollo_integral_colombia_ctg_security_158k_2024",
    "infrastructure", "building_materials", "other",
    "Desarrollo Integral Proyectos — Colombia CTG security upgrades",
    "Colombia",
    "17 Sep 2024: Department of State awards contract to DESARROLLO INTEGRAL PROYECTOS INGENIERIA LIMITADA for CTG security upgrades (PoP Colombia); obligated USD 158693.54. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "158693.54", "2024-09-17", "2024", "", "",
    "PR12916460: CTG SECURITY UPGRADES - 7945 FUNDS, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_desarrollo_integral_colombia_ctg_security_158k_2024",
    "PR12916460: CTG SECURITY UPGRADES - 7945 FUNDS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024C0007_1900_-NONE-_-NONE-/",
    "Actor: DESARROLLO INTEGRAL PROYECTOS INGENIERIA LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1293",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02024C0007_1900_-NONE-_-NONE- (desarrollo_integral_colombia_ctg_security_158k_2024). Signed 2024-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02024C0007_1900_-NONE-_-NONE-/.",
    "USASpending: desarrollo_integral_colombia_ctg_security_158k_2024 USD 0.159m. Supports desarrollo_integral_colombia_ctg_security_158k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 158693.54; date_signed 2024-09-17.",
    investment_type="epc",
)

# === Cycle 1294 ===
row_doc(
    "ics_brazil_consular_expansion_hubzone_256k_2012",
    "infrastructure", "building_materials", "us",
    "International Construction Services — Brazil consular expansion hubzone",
    "Brazil",
    "17 Mar 2012: Department of State awards contract to INTERNATIONAL CONSTRUCTION SERVICES, LLC for Brazil consular expansion projects hubzone IDIQ (PoP Brazil); obligated USD 256468. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "256468", "2012-03-17", "2012", "", "",
    "BRAZIL CONSULAR EXPANSION PROJECTS. 2 HUBZONE IDIQ CONTRACTORS COMPETED TO PROCURE AND DELIVER GFE/GFP OF FORC, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_ics_brazil_consular_expansion_hubzone_256k_2012",
    "BRAZIL CONSULAR EXPANSION PROJECTS. 2 HUBZONE IDIQ CONTRACTORS COMPETED TO PROCURE AND DELIVER GFE/GFP OF FORCED ENTRY BALLISTIC RESISTENCE PRODUCTS TO SAO PAULO, FOR OTHER CONTRACTORS TO INSTALL AT CONSULAR VISA OFFICES AT BRAZILIA, RIO DE JANEIRO, AND SAO PAULO, UNDER OTHER SEPARATE CONTRACT ACTIONS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F0730_1900_SAQMMA08D0005_1900/",
    "Actor: INTERNATIONAL CONSTRUCTION SERVICES, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1294",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F0730_1900_SAQMMA08D0005_1900 (ics_brazil_consular_expansion_hubzone_256k_2012). Signed 2012-03-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F0730_1900_SAQMMA08D0005_1900/.",
    "USASpending: ics_brazil_consular_expansion_hubzone_256k_2012 USD 0.256m. Supports ics_brazil_consular_expansion_hubzone_256k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 256468.0; date_signed 2012-03-17.",
    investment_type="epc",
)

# === Cycle 1294 ===
row_doc(
    "kva_honduras_power_systems_electrical_212k_2011",
    "energy", "power_plants_grid", "us",
    "KVA Electric — Honduras power systems electrical work",
    "Honduras",
    "20 Sep 2011: Department of State awards contract to KVA ELECTRIC INC for power systems Honduras electrical work (PoP Honduras); obligated USD 212714.01. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "212714.01", "2011-09-20", "2011", "", "",
    "POWER SYSTEMS HONDURAS ELECTRICAL WORK, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_kva_honduras_power_systems_electrical_212k_2011",
    "POWER SYSTEMS HONDURAS ELECTRICAL WORK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11C0253_1900_-NONE-_-NONE-/",
    "Actor: KVA ELECTRIC INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1294",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11C0253_1900_-NONE-_-NONE- (kva_honduras_power_systems_electrical_212k_2011). Signed 2011-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11C0253_1900_-NONE-_-NONE-/.",
    "USASpending: kva_honduras_power_systems_electrical_212k_2011 USD 0.213m. Supports kva_honduras_power_systems_electrical_212k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 212714.01; date_signed 2011-09-20.",
    investment_type="epc",
)

# === Cycle 1294 ===
row_doc(
    "norma_gutierrez_mexico_double_pane_window_159k_2022",
    "infrastructure", "building_materials", "other",
    "Norma Isabel Gutiérrez López — Mexico TCA double pane window",
    "Mexico",
    "29 Apr 2022: Department of State awards contract to NORMA ISABEL GUTIERREZ LOPEZ for FAC TCA double pane window (PoP Mexico); obligated USD 159277.91. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "159277.91", "2022-04-29", "2022", "", "",
    "MEX-FAC-7903FWP550.02-TCA-DOUBLE PANE WINDOW, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_norma_gutierrez_mexico_double_pane_window_159k_2022",
    "MEX-FAC-7903FWP550.02-TCA-DOUBLE PANE WINDOW",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5322C0005_1900_-NONE-_-NONE-/",
    "Actor: NORMA ISABEL GUTIERREZ LOPEZ — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1294",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5322C0005_1900_-NONE-_-NONE- (norma_gutierrez_mexico_double_pane_window_159k_2022). Signed 2022-04-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5322C0005_1900_-NONE-_-NONE-/.",
    "USASpending: norma_gutierrez_mexico_double_pane_window_159k_2022 USD 0.159m. Supports norma_gutierrez_mexico_double_pane_window_159k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 159277.91; date_signed 2022-04-29.",
    investment_type="epc",
)

# === Cycle 1294 ===
row_doc(
    "norma_gutierrez_mexico_cmr_electrical_substation_148k_2018",
    "energy", "power_plants_grid", "other",
    "Norma Isabel Gutiérrez López — Mexico CMR electrical substation",
    "Mexico",
    "10 Aug 2018: Department of State awards contract to NORMA ISABEL GUTIERREZ LOPEZ for electrical substation for CMR FY2018 (PoP Mexico); obligated USD 148863.29. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "148863.29", "2018-08-10", "2018", "", "",
    "MX-FAC-ELECTRICAL SUBSTATION FOR CMR FY2018 IGT::OT::IGT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_norma_gutierrez_mexico_cmr_electrical_substation_148k_2018",
    "MX-FAC-ELECTRICAL SUBSTATION FOR CMR FY2018 IGT::OT::IGT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5318C0004_1900_-NONE-_-NONE-/",
    "Actor: NORMA ISABEL GUTIERREZ LOPEZ — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1294",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5318C0004_1900_-NONE-_-NONE- (norma_gutierrez_mexico_cmr_electrical_substation_148k_2018). Signed 2018-08-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5318C0004_1900_-NONE-_-NONE-/.",
    "USASpending: norma_gutierrez_mexico_cmr_electrical_substation_148k_2018 USD 0.149m. Supports norma_gutierrez_mexico_cmr_electrical_substation_148k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 148863.29; date_signed 2018-08-10.",
    investment_type="epc",
)

# === Cycle 1294 ===
row_doc(
    "desarrollo_integral_colombia_med_unit_99k_2023",
    "infrastructure", "building_materials", "other",
    "Desarrollo Integral Proyectos — Bogotá med unit improvement",
    "Colombia",
    "8 Sep 2023: Department of State awards contract to DESARROLLO INTEGRAL PROYECTOS INGENIERIA LIMITADA for Bogota med unit improvement project (PoP Colombia); obligated USD 99622.58. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "99622.58", "2023-09-08", "2023", "", "",
    "PR12007298: BOGOTA MED UNIT IMPROVEMENT PROJECT, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_desarrollo_integral_colombia_med_unit_99k_2023",
    "PR12007298: BOGOTA MED UNIT IMPROVEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02023C0005_1900_-NONE-_-NONE-/",
    "Actor: DESARROLLO INTEGRAL PROYECTOS INGENIERIA LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1294",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02023C0005_1900_-NONE-_-NONE- (desarrollo_integral_colombia_med_unit_99k_2023). Signed 2023-09-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02023C0005_1900_-NONE-_-NONE-/.",
    "USASpending: desarrollo_integral_colombia_med_unit_99k_2023 USD 0.100m. Supports desarrollo_integral_colombia_med_unit_99k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 99622.58; date_signed 2023-09-08.",
    investment_type="epc",
)

# === Cycle 1295 ===
row_doc(
    "mesan_mexico_tijuana_multimedia_gps_377k_2011",
    "infrastructure", "building_materials", "us",
    "Mesan-Martinez — Tijuana consulate multi-media GPS and Q-Flows installation",
    "Mexico",
    "11 Apr 2011: Department of State awards contract to MESAN-MARTINEZ JOINT VENTURE LLP for design, purchase and installation of multi-media GPS and Q-Flows systems in Tijuana Consulate General (PoP Mexico); obligated USD 377098.01. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "377098.01", "2011-04-11", "2011", "", "",
    "DESIGN, PURCHASE AND INSTALLATION OF MULTI-MEDIA GPS AND Q-FLOWS SYSTEMS IN TIJUANA CONSULATE GENERAL LOCATION, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mesan_mexico_tijuana_multimedia_gps_377k_2011",
    "DESIGN, PURCHASE AND INSTALLATION OF MULTI-MEDIA GPS AND Q-FLOWS SYSTEMS IN TIJUANA CONSULATE GENERAL LOCATION.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F1240_1900_SAQMMA08D0015_1900/",
    "Actor: MESAN-MARTINEZ JOINT VENTURE LLP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1295",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F1240_1900_SAQMMA08D0015_1900 (mesan_mexico_tijuana_multimedia_gps_377k_2011). Signed 2011-04-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F1240_1900_SAQMMA08D0015_1900/.",
    "USASpending: mesan_mexico_tijuana_multimedia_gps_377k_2011 USD 0.377m. Supports mesan_mexico_tijuana_multimedia_gps_377k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 377098.01; date_signed 2011-04-11.",
    investment_type="equipment_supply",
)

# === Cycle 1295 ===
row_doc(
    "hollingsworth_brazil_brasilia_nec_ae_147k_2021",
    "infrastructure", "engineering_epc", "us",
    "Hollingsworth-Pack — Brasilia NEC A&E services",
    "Brazil",
    "17 Aug 2021: Department of State awards contract to HOLLINGSWORTH-PACK CORPORATION for A&E services for the NEC Brasilia (PoP Brazil); obligated USD 147386.98. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "147386.98", "2021-08-17", "2021", "", "",
    "A&E SERVICES FOR THE NEC BRASILIA, BRAZIL., Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hollingsworth_brazil_brasilia_nec_ae_147k_2021",
    "A&E SERVICES FOR THE NEC BRASILIA, BRAZIL.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021F0433_1900_SGE50016D0009_1900/",
    "Actor: HOLLINGSWORTH-PACK CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1295",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5021F0433_1900_SGE50016D0009_1900 (hollingsworth_brazil_brasilia_nec_ae_147k_2021). Signed 2021-08-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5021F0433_1900_SGE50016D0009_1900/.",
    "USASpending: hollingsworth_brazil_brasilia_nec_ae_147k_2021 USD 0.147m. Supports hollingsworth_brazil_brasilia_nec_ae_147k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 147386.98; date_signed 2021-08-17.",
    investment_type="epc",
)

# === Cycle 1295 ===
row_doc(
    "desarrollo_integral_colombia_chancery_bathroom_95k_2026",
    "infrastructure", "building_materials", "other",
    "Desarrollo Integral Proyectos — Colombia chancery bathroom modernization",
    "Colombia",
    "24 Sep 2026: Department of State awards contract to DESARROLLO INTEGRAL PROYECTOS INGENIERIA LIMITADA for chancery bathroom modernization project (PoP Colombia); obligated USD 95427.35. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "95427.35", "2026-09-24", "2026", "", "",
    "PR16302130: CHANCERY BATHROOM MODERNIZATION PROJECT 7902 XJ1D0.., Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_desarrollo_integral_colombia_chancery_bathroom_95k_2026",
    "PR16302130: CHANCERY BATHROOM MODERNIZATION PROJECT 7902 XJ1D0..",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026C0011_1900_-NONE-_-NONE-/",
    "Actor: DESARROLLO INTEGRAL PROYECTOS INGENIERIA LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1295",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02026C0011_1900_-NONE-_-NONE- (desarrollo_integral_colombia_chancery_bathroom_95k_2026). Signed 2026-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02026C0011_1900_-NONE-_-NONE-/.",
    "USASpending: desarrollo_integral_colombia_chancery_bathroom_95k_2026 USD 0.095m. Supports desarrollo_integral_colombia_chancery_bathroom_95k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 95427.35; date_signed 2026-09-24.",
    investment_type="epc",
)

# === Cycle 1295 ===
row_doc(
    "fabio_garzon_colombia_construction_120k_2011",
    "infrastructure", "building_materials", "other",
    "Fabio Garzón Daza — Colombia construction",
    "Colombia",
    "5 Jul 2011: Department of Defense awards contract to FABIO GARZON DAZA for construction (PoP Colombia); obligated USD 120705.17. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "120705.17", "2011-07-05", "2011", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fabio_garzon_colombia_construction_120k_2011",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0153_9700_-NONE-_-NONE-/",
    "Actor: FABIO GARZON DAZA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1295",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11P0153_9700_-NONE-_-NONE- (fabio_garzon_colombia_construction_120k_2011). Signed 2011-07-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0153_9700_-NONE-_-NONE-/.",
    "USASpending: fabio_garzon_colombia_construction_120k_2011 USD 0.121m. Supports fabio_garzon_colombia_construction_120k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 120705.17; date_signed 2011-07-05.",
    investment_type="epc",
)

# === Cycle 1295 ===
row_doc(
    "fabio_garzon_colombia_construction_94k_2011",
    "infrastructure", "building_materials", "other",
    "Fabio Garzón Daza — Colombia construction (second package)",
    "Colombia",
    "6 Jul 2011: Department of Defense awards contract to FABIO GARZON DAZA for construction (PoP Colombia); obligated USD 94117.59. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "94117.59", "2011-07-06", "2011", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fabio_garzon_colombia_construction_94k_2011",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0155_9700_-NONE-_-NONE-/",
    "Actor: FABIO GARZON DAZA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1295",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11P0155_9700_-NONE-_-NONE- (fabio_garzon_colombia_construction_94k_2011). Signed 2011-07-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0155_9700_-NONE-_-NONE-/.",
    "USASpending: fabio_garzon_colombia_construction_94k_2011 USD 0.094m. Supports fabio_garzon_colombia_construction_94k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 94117.59; date_signed 2011-07-06.",
    investment_type="epc",
)

# === Cycle 1296 ===
row_doc(
    "hollingsworth_jamaica_design_services_138k_2020",
    "infrastructure", "engineering_epc", "us",
    "Hollingsworth-Pack — Jamaica design services",
    "Jamaica",
    "18 Sep 2020: Department of State awards contract to HOLLINGSWORTH-PACK CORPORATION for design services (PoP Jamaica); obligated USD 138681.46. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "138681.46", "2020-09-18", "2020", "", "",
    "DESIGN SERVICES, Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_hollingsworth_jamaica_design_services_138k_2020",
    "DESIGN SERVICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5020F0460_1900_SGE50016D0009_1900/",
    "Actor: HOLLINGSWORTH-PACK CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1296",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5020F0460_1900_SGE50016D0009_1900 (hollingsworth_jamaica_design_services_138k_2020). Signed 2020-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5020F0460_1900_SGE50016D0009_1900/.",
    "USASpending: hollingsworth_jamaica_design_services_138k_2020 USD 0.139m. Supports hollingsworth_jamaica_design_services_138k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 138681.46; date_signed 2020-09-18.",
    investment_type="epc",
)

# === Cycle 1296 ===
row_doc(
    "alutiiq_mexico_emc_install_116k_2014",
    "infrastructure", "building_materials", "us",
    "Alutiiq — Mexico EMC installation for GOM",
    "Mexico",
    "24 Sep 2014: Department of State awards contract to ALUTIIQ SECURITY & TECHNOLOGY, LLC for installation of EMC for the GOM (PoP Mexico); obligated USD 116867.64. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "116867.64", "2014-09-24", "2014", "", "",
    "IGF::OT::IGF INSTALLATION OF EMC FOR THE GOM, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_alutiiq_mexico_emc_install_116k_2014",
    "IGF::OT::IGF INSTALLATION OF EMC FOR THE GOM",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC14M0042_1900_-NONE-_-NONE-/",
    "Actor: ALUTIIQ SECURITY & TECHNOLOGY, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1296",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SWHARC14M0042_1900_-NONE-_-NONE- (alutiiq_mexico_emc_install_116k_2014). Signed 2014-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SWHARC14M0042_1900_-NONE-_-NONE-/.",
    "USASpending: alutiiq_mexico_emc_install_116k_2014 USD 0.117m. Supports alutiiq_mexico_emc_install_116k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 116867.64; date_signed 2014-09-24.",
    investment_type="equipment_supply",
)

# === Cycle 1296 ===
row_doc(
    "fabio_garzon_colombia_construction_88k_2011",
    "infrastructure", "building_materials", "other",
    "Fabio Garzón Daza — Colombia construction (third package)",
    "Colombia",
    "5 Jul 2011: Department of Defense awards contract to FABIO GARZON DAZA for construction (PoP Colombia); obligated USD 88088.38. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "88088.38", "2011-07-05", "2011", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fabio_garzon_colombia_construction_88k_2011",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0151_9700_-NONE-_-NONE-/",
    "Actor: FABIO GARZON DAZA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1296",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11P0151_9700_-NONE-_-NONE- (fabio_garzon_colombia_construction_88k_2011). Signed 2011-07-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0151_9700_-NONE-_-NONE-/.",
    "USASpending: fabio_garzon_colombia_construction_88k_2011 USD 0.088m. Supports fabio_garzon_colombia_construction_88k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 88088.38; date_signed 2011-07-05.",
    investment_type="epc",
)

# === Cycle 1296 ===
row_doc(
    "misc_brazil_usgo_renovation_phase2_244k_2021",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil USGO renovation phase II",
    "Brazil",
    "20 Sep 2021: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC renovation phase II USGO (PoP Brazil); obligated USD 244992.10. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "244992.10", "2021-09-20", "2021", "", "",
    "BSB|FAC| RENOVATION-PHASE II-USGO QL 12-10-13 15, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_usgo_renovation_phase2_244k_2021",
    "BSB|FAC| RENOVATION-PHASE II-USGO QL 12-10-13 15",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521C0008_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1296",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2521C0008_1900_-NONE-_-NONE- (misc_brazil_usgo_renovation_phase2_244k_2021). Signed 2021-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2521C0008_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_usgo_renovation_phase2_244k_2021 USD 0.245m. Supports misc_brazil_usgo_renovation_phase2_244k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 244992.1; date_signed 2021-09-20.",
    investment_type="epc",
)

# === Cycle 1296 ===
row_doc(
    "misc_ecuador_consular_renovation_239k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Ecuador consular renovation project",
    "Ecuador",
    "29 Sep 2020: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for consular renovation project (PoP Ecuador); obligated USD 239189.58. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "239189.58", "2020-09-29", "2020", "", "",
    "1900.0-PR9285011-CONSULAR RENOVATION PROJECT, Ecuador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_ecuador_consular_renovation_239k_2020",
    "1900.0-PR9285011-CONSULAR RENOVATION PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7520C0007_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1296",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19EC7520C0007_1900_-NONE-_-NONE- (misc_ecuador_consular_renovation_239k_2020). Signed 2020-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19EC7520C0007_1900_-NONE-_-NONE-/.",
    "USASpending: misc_ecuador_consular_renovation_239k_2020 USD 0.239m. Supports misc_ecuador_consular_renovation_239k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 239189.58; date_signed 2020-09-29.",
    investment_type="epc",
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
                if s not in (existing.get("supports") or []):
                    existing.setdefault("supports", []).append(s)
        else:
            bib_docs.append(bib); bib_by_id[sid] = bib
    BIB.write_text(yaml.safe_dump(bib_docs, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
    print(f"loaded {len(ITEMS)} rows")

if __name__ == "__main__":
    main()
