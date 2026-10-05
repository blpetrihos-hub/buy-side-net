#!/usr/bin/env python3
"""Cycles 1056–1058: USASpending LatAm CapEx residual (~USD0.056–0.069m).

Seeds: 20262056–20262058. Thin top-up dry. Coibita solar; Haiti Arcahaie PV.
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


# === Cycle 1056 (seed 20262056) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "wholesale_solar_coibita_60k_2019",
    "energy", "solar", "us",
    "Wholesale Solar — Panama Coibita off-grid solar system",
    "Panama",
    "20 Sep 2019: Smithsonian awards contract 33330519P00432018 to Wholesale Solar, Inc. for off-grid solar system — Coibita (PoP Panama); obligated USD 60,029. CapEx face = award obligation.",
    "60029", "2019-09-20", "2019", "7.628", "-81.728",
    "Off-grid solar system at Coibita, Panama (USASpending description; Coibita named).",
    "usaspending_wholesale_solar_coibita_60k_2019",
    "OFF-GRID SOLAR SYSTEM - COIBITA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330519P00432018_3300_-NONE-_-NONE-/",
    "Actor: Wholesale Solar, Inc. (U.S.) — us. Official USASpending Award API. Shuffle solar; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1056",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330519P00432018_3300_-NONE-_-NONE- (Wholesale Solar Coibita). Signed 2019-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330519P00432018_3300_-NONE-_-NONE-/.",
    "USASpending: Wholesale Solar Coibita USD 0.060m. Supports wholesale_solar_coibita_60k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60029; date_signed 2019-09-20.",
)

row_doc(
    "muka_brazil_circuit_breakers_60k_2025",
    "energy", "power_plants_grid", "us",
    "Muka Trade — Brazil Brasília electric circuit breakers",
    "Brazil",
    "9 Sep 2025: Department of State awards contract 19BR2525P1292 to Muka Trade LLC for electric circuit breakers (PoP Brazil); obligated USD 60,200. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "60200", "2025-09-09", "2025", "", "",
    "Electric circuit breakers, Brasília post, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_muka_brazil_circuit_breakers_60k_2025",
    "BSB|FAC|7901-R|FWP 601.01 ELECTRIC CIRCUIT BREAKERS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2525P1292_1900_-NONE-_-NONE-/",
    "Actor: Muka Trade LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1056",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2525P1292_1900_-NONE-_-NONE- (Muka Brazil circuit breakers). Signed 2025-09-09. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2525P1292_1900_-NONE-_-NONE-/.",
    "USASpending: Muka Brazil circuit breakers USD 0.060m. Supports muka_brazil_circuit_breakers_60k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60200; date_signed 2025-09-09.",
)

row_doc(
    "alerco_chile_barracks_san_fernando_61k_2010",
    "infrastructure", "building_materials", "other",
    "Constructora Alerco — Chile San Fernando barracks renovation",
    "Chile",
    "30 Apr 2010: Department of Defense awards contract W9127810P0225 to Constructora Alerco Limitada for design and construction of barracks renovation in San Fernando, Chile (PoP Chile); obligated USD 60,898. CapEx face = award obligation.",
    "60898", "2010-04-30", "2010", "-34.588", "-70.989",
    "Barracks renovation in San Fernando, Chile (USASpending description; San Fernando named).",
    "usaspending_alerco_chile_barracks_san_fernando_61k_2010",
    "DESIGN AND CONSTRUCTION OF BARRACKS RENOVATION IN SAN FERNANDO, CHILE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0225_9700_-NONE-_-NONE-/",
    "Actor: Constructora Alerco Limitada (Chile) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1056",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127810P0225_9700_-NONE-_-NONE- (Alerco San Fernando barracks). Signed 2010-04-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127810P0225_9700_-NONE-_-NONE-/.",
    "USASpending: Alerco San Fernando barracks USD 0.061m. Supports alerco_chile_barracks_san_fernando_61k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60898; date_signed 2010-04-30.",
)

row_doc(
    "misc_argentina_las_heras_67k_2018",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina Las Heras 2651 Martínez renovation",
    "Argentina",
    "11 Sep 2018: Department of State awards contract 19AR2018P0858 for renovation of GOP Las Heras 2651, Martinez (PoP Argentina); obligated USD 66,730.25. CapEx face = award obligation.",
    "66730.25", "2018-09-11", "2018", "-34.494", "-58.497",
    "Renovation of GOP Las Heras 2651, Martínez, Argentina (USASpending description; address named).",
    "usaspending_misc_argentina_las_heras_67k_2018",
    "RENOVATION OF GOP LAS HERAS 2651, MARTINEZ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P0858_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1056",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AR2018P0858_1900_-NONE-_-NONE- (Argentina Las Heras). Signed 2018-09-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AR2018P0858_1900_-NONE-_-NONE-/.",
    "USASpending: Argentina Las Heras USD 0.067m. Supports misc_argentina_las_heras_67k_2018.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 66730.25; date_signed 2018-09-11.",
)

row_doc(
    "gordon_stri_gamboa_repairs_68k_2021",
    "infrastructure", "building_materials", "other",
    "Gordon & Gordons — Panama STRI Gamboa greenhouse repairs",
    "Panama",
    "14 Sep 2021: Smithsonian awards contract 33330221CF0010440 to Gordon & Gordons Services, Inc. for labor, material and transport for repairs at STRI Gamboa greenhouses (PoP Panama); obligated USD 68,130.65. CapEx face = award obligation.",
    "68130.65", "2021-09-14", "2021", "9.119", "-79.694",
    "Greenhouse repairs at STRI Gamboa, Panama (USASpending description; Gamboa named).",
    "usaspending_gordon_stri_gamboa_repairs_68k_2021",
    "TO SERVICE LABOR, MATERIAL AND TRANSPORT FOR REPAIRS AT STRI GAMBOA GREENHOUSES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010440_3300_-NONE-_-NONE-/",
    "Actor: Gordon & Gordons Services, Inc. (Panama) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1056",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_33330221CF0010440_3300_-NONE-_-NONE- (Gordon STRI Gamboa). Signed 2021-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_33330221CF0010440_3300_-NONE-_-NONE-/.",
    "USASpending: Gordon STRI Gamboa USD 0.068m. Supports gordon_stri_gamboa_repairs_68k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68130.65; date_signed 2021-09-14.",
)

# === Cycle 1057 (seed 20262057) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "cummins_honduras_cmr_generators_59k_2014",
    "energy", "power_plants_grid", "us",
    "Cummins Power Generation — Honduras CMR and DCR generators",
    "Honduras",
    "15 May 2014: Department of State awards order SHO80014F0204 to Cummins Power Generation Inc. for purchase of generators for CMR and DCR (PoP Honduras); obligated USD 58,858.31. CapEx face = award obligation. Exact sites unnamed — lat/lon blank.",
    "58858.31", "2014-05-15", "2014", "", "",
    "Generators for CMR and DCR, Honduras (USASpending description; CMR/DCR named, site coords not stated — lat/lon blank).",
    "usaspending_cummins_honduras_cmr_generators_59k_2014",
    "PURCHASE OF GENERATORS FOR CMR AND DCR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80014F0204_1900_GS07F9004D_4730/",
    "Actor: Cummins Power Generation Inc. (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1057",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80014F0204_1900_GS07F9004D_4730 (Cummins Honduras CMR generators). Signed 2014-05-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80014F0204_1900_GS07F9004D_4730/.",
    "USASpending: Cummins Honduras CMR generators USD 0.059m. Supports cummins_honduras_cmr_generators_59k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 58858.31; date_signed 2014-05-15.",
)

row_doc(
    "nesi_peru_chancery_roof_56k_2014",
    "infrastructure", "building_materials", "us",
    "Nesi Solutions — Peru chancery roof SPF replacement",
    "Peru",
    "29 Apr 2014: Department of State awards contract SPE50014M0855 to Nesi Solutions LLC for replace SPF-R-1 and 2 on chancery roof (PoP Peru); obligated USD 56,077.96. CapEx face = award obligation. Exact chancery site unnamed — lat/lon blank.",
    "56077.96", "2014-04-29", "2014", "", "",
    "SPF roof replacement on chancery, Peru (USASpending description; chancery named, site coords not stated — lat/lon blank).",
    "usaspending_nesi_peru_chancery_roof_56k_2014",
    "FAC-REPLACE SPF-R-1AND2 ON CHANCERY ROOF IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M0855_1900_-NONE-_-NONE-/",
    "Actor: Nesi Solutions LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1057",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPE50014M0855_1900_-NONE-_-NONE- (Nesi Peru chancery roof). Signed 2014-04-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPE50014M0855_1900_-NONE-_-NONE-/.",
    "USASpending: Nesi Peru chancery roof USD 0.056m. Supports nesi_peru_chancery_roof_56k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 56077.96; date_signed 2014-04-29.",
)

row_doc(
    "isobox_panama_corozal_repairs_58k_2022",
    "infrastructure", "building_materials", "other",
    "Isobox — Panama Corozal East facility repairs",
    "Panama",
    "4 Apr 2022: Department of Defense awards contract H9228122C0001 to Isobox Inc for Corozal East facility repairs (PoP Panama); obligated USD 57,800. CapEx face = award obligation.",
    "57800", "2022-04-04", "2022", "8.985", "-79.575",
    "Facility repairs at Corozal East, Panama (USASpending description; Corozal East named).",
    "usaspending_isobox_panama_corozal_repairs_58k_2022",
    "COROZAL EAST FACILITY REPAIRS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228122C0001_9700_-NONE-_-NONE-/",
    "Actor: Isobox Inc (Panama) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1057",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_H9228122C0001_9700_-NONE-_-NONE- (Isobox Corozal East). Signed 2022-04-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228122C0001_9700_-NONE-_-NONE-/.",
    "USASpending: Isobox Corozal East USD 0.058m. Supports isobox_panama_corozal_repairs_58k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 57800; date_signed 2022-04-04.",
)

row_doc(
    "energy_central_haiti_arcahaie_solar_66k_2015",
    "energy", "solar", "other",
    "Energy Central — Haiti Arcahaie prison solar panel installation",
    "Haiti",
    "3 Jun 2015: Department of State awards contract SHA70015M1088 to Energy Central SA for INL installation of solar panel at Arcahaie prison (PoP Haiti); obligated USD 65,567.20. CapEx face = award obligation.",
    "65567.20", "2015-06-03", "2015", "18.769", "-72.511",
    "Solar panel installation at Arcahaie prison, Haiti (USASpending description; Arcahaie named).",
    "usaspending_energy_central_haiti_arcahaie_solar_66k_2015",
    "INL-COR-INSTALLATION OF SOLAR PANEL AT ARCAHAIE PRISON",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHA70015M1088_1900_-NONE-_-NONE-/",
    "Actor: Energy Central SA (Haiti) — other. Official USASpending Award API. Shuffle solar. Haiti under-covered weight.",
    "hunt_cycle1057",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHA70015M1088_1900_-NONE-_-NONE- (Energy Central Arcahaie solar). Signed 2015-06-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHA70015M1088_1900_-NONE-_-NONE-/.",
    "USASpending: Energy Central Arcahaie solar USD 0.066m. Supports energy_central_haiti_arcahaie_solar_66k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65567.20; date_signed 2015-06-03.",
)

row_doc(
    "pavimentaciones_peru_asphalt_66k_2019",
    "infrastructure", "bridges_roads", "other",
    "Pavimentaciones — Peru asphalt repair parking lots",
    "Peru",
    "23 Sep 2019: Department of State awards contract 19PE5019C0025 to Pavimentaciones Sociedad Anonima Cerrada for asphalt repair parking lots 2019 (PoP Peru); obligated USD 65,917.63. CapEx face = award obligation. Exact lots unnamed — lat/lon blank.",
    "65917.63", "2019-09-23", "2019", "", "",
    "Asphalt repair of parking lots, Peru (USASpending description; lots not named — lat/lon blank).",
    "usaspending_pavimentaciones_peru_asphalt_66k_2019",
    "ASPHALT REPAIR PARKING LOTS 2019",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5019C0025_1900_-NONE-_-NONE-/",
    "Actor: Pavimentaciones Sociedad Anonima Cerrada (Peru) — other. Official USASpending Award API. Shuffle bridges_roads.",
    "hunt_cycle1057",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5019C0025_1900_-NONE-_-NONE- (Pavimentaciones Peru asphalt). Signed 2019-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5019C0025_1900_-NONE-_-NONE-/.",
    "USASpending: Pavimentaciones Peru asphalt USD 0.066m. Supports pavimentaciones_peru_asphalt_66k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65917.63; date_signed 2019-09-23.",
)

# === Cycle 1058 (seed 20262058) — 2 US / 0 PRC / 0 allied / 3 other ===
row_doc(
    "mckinney_stri_fire_ae_61k_2010",
    "infrastructure", "engineering_epc", "us",
    "McKinney and Company — Panama STRI BCI fire protection A/E",
    "Panama",
    "28 Apr 2010: Smithsonian awards order F10CW10175 to McKinney and Company, Inc for A/E services for BCI fire protection system at the STRI (PoP Panama); obligated USD 60,746.74. CapEx face = award obligation. Exact STRI site unnamed beyond post — lat/lon blank.",
    "60746.74", "2010-04-28", "2010", "", "",
    "A/E services for BCI fire protection system at STRI, Panama (USASpending description; STRI named, site coords not stated — lat/lon blank).",
    "usaspending_mckinney_stri_fire_ae_61k_2010",
    "A/E SERVICES FOR BCI FIRE PROTECTION SYSTEM AT THE STRI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_F10CW10175_3300_F06CC10332_3300/",
    "Actor: McKinney and Company, Inc (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1058",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_F10CW10175_3300_F06CC10332_3300 (McKinney STRI fire A/E). Signed 2010-04-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_F10CW10175_3300_F06CC10332_3300/.",
    "USASpending: McKinney STRI fire A/E USD 0.061m. Supports mckinney_stri_fire_ae_61k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 60746.74; date_signed 2010-04-28.",
)

row_doc(
    "simplified_safety_peru_guardrail_59k_2019",
    "infrastructure", "building_materials", "us",
    "Simplified Safety — Peru annex roof non-penetrating safety guardrail",
    "Peru",
    "17 Sep 2019: Department of State awards contract 19PE5019P2010 to Simplified Safety, Inc. for non penetrating safety guardrail for annex roof (PoP Peru); obligated USD 58,922.42. CapEx face = award obligation. Exact annex unnamed — lat/lon blank.",
    "58922.42", "2019-09-17", "2019", "", "",
    "Non-penetrating safety guardrail for annex roof, Peru (USASpending description; annex not named — lat/lon blank).",
    "usaspending_simplified_safety_peru_guardrail_59k_2019",
    "NON PENETRATING SAFETY GUARDRAIL FOR ANNEX ROOF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5019P2010_1900_-NONE-_-NONE-/",
    "Actor: Simplified Safety, Inc. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1058",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19PE5019P2010_1900_-NONE-_-NONE- (Simplified Safety Peru guardrail). Signed 2019-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19PE5019P2010_1900_-NONE-_-NONE-/.",
    "USASpending: Simplified Safety Peru guardrail USD 0.059m. Supports simplified_safety_peru_guardrail_59k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 58922.42; date_signed 2019-09-17.",
)

row_doc(
    "ayre_honduras_hvac_rtu_69k_2019",
    "infrastructure", "building_materials", "other",
    "Ayre Tegucigalpa — Honduras OBX HVAC rooftop units",
    "Honduras",
    "5 Aug 2019: Department of State awards contract 19H08019P0657 to Ayre Tegucigalpa SA de CV for BME for OBX HVAC roof top units (PoP Honduras); obligated USD 68,743.44. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "68743.44", "2019-08-05", "2019", "", "",
    "HVAC rooftop units for OBX, Honduras (USASpending description; site not named — lat/lon blank).",
    "usaspending_ayre_honduras_hvac_rtu_69k_2019",
    "BME FOR OBX HVAC ROOF TOP UNITS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08019P0657_1900_-NONE-_-NONE-/",
    "Actor: Ayre Tegucigalpa SA de CV (Honduras) — other. Official USASpending Award API. Shuffle building_materials. Holdover closed.",
    "hunt_cycle1058",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19H08019P0657_1900_-NONE-_-NONE- (Ayre Honduras HVAC RTU). Signed 2019-08-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19H08019P0657_1900_-NONE-_-NONE-/.",
    "USASpending: Ayre Honduras HVAC RTU USD 0.069m. Supports ayre_honduras_hvac_rtu_69k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 68743.44; date_signed 2019-08-05.",
)

row_doc(
    "gerardo_leon_mexico_generator_65k_2024",
    "energy", "power_plants_grid", "other",
    "Gerardo Leon Rosales — Mexico POR diesel generator remove-install",
    "Mexico",
    "18 Jul 2024: Department of State awards contract 19MX6024P0097 to Gerardo Leon Rosales for remove-install diesel generator at POR (PoP Mexico); obligated USD 65,434.07. CapEx face = award obligation. Exact POR site unnamed — lat/lon blank.",
    "65434.07", "2024-07-18", "2024", "", "",
    "Diesel generator remove-install at POR, Mexico (USASpending description; POR named, site coords not stated — lat/lon blank).",
    "usaspending_gerardo_leon_mexico_generator_65k_2024",
    "REMOVE-INSTALL DIESEL GENERATOR AT POR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6024P0097_1900_-NONE-_-NONE-/",
    "Actor: Gerardo Leon Rosales (Mexico) — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1058",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX6024P0097_1900_-NONE-_-NONE- (Gerardo Leon Mexico generator). Signed 2024-07-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX6024P0097_1900_-NONE-_-NONE-/.",
    "USASpending: Gerardo Leon Mexico generator USD 0.065m. Supports gerardo_leon_mexico_generator_65k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 65434.07; date_signed 2024-07-18.",
)

row_doc(
    "misc_brazil_shis_fence_66k_2025",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil SHIS QL backyard fence upgrade",
    "Brazil",
    "3 Sep 2025: Department of State awards contract 19BR2525P1234 for RSO backyard fence upgrade at SHIS QL 12-06-19/20 (PoP Brazil); obligated USD 66,138.54. CapEx face = award obligation.",
    "66138.54", "2025-09-03", "2025", "-15.833", "-47.857",
    "Backyard fence upgrade at SHIS QL 12-06-19/20, Brasília, Brazil (USASpending description; SHIS QL address named).",
    "usaspending_misc_brazil_shis_fence_66k_2025",
    "BSB|RSO|BACK YARD FENCE UPGRADE AT SHIS QL 12-06-19/20",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2525P1234_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1058",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2525P1234_1900_-NONE-_-NONE- (Brazil SHIS fence). Signed 2025-09-03. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2525P1234_1900_-NONE-_-NONE-/.",
    "USASpending: Brazil SHIS fence USD 0.066m. Supports misc_brazil_shis_fence_66k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 66138.54; date_signed 2025-09-03.",
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
