#!/usr/bin/env python3
"""Cycles 978–980: USASpending LatAm CapEx residual (~USD0.44–0.48m).

Seeds: 20261978–20261980. Thin top-up dry.
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


# === Cycle 978 ===
row_doc(
    "misc_peru_clinic_478k_2009",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru clinic construction",
    "Peru",
    "23 Sep 2009: U.S. Army Corps of Engineers awards contract W912CL09C0029 for clinic construction (PoP Peru); obligated USD 477,813.43. CapEx face = award obligation. Recipient redacted; site not named — lat/lon blank.",
    "477813.43", "2009-09-23", "2009", "", "",
    "Clinic construction, Peru (USASpending PoP Peru; site not named — lat/lon blank).",
    "usaspending_misc_peru_clinic_478k_2009",
    "CLINIC CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL09C0029_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle978",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL09C0029_9700_-NONE-_-NONE- (Peru clinic). Signed 2009-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL09C0029_9700_-NONE-_-NONE-/.",
    "USASpending: Peru clinic construction USD 0.478m. Supports misc_peru_clinic_478k_2009.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 477813.43; date_signed 2009-09-23.",
)

row_doc(
    "bonatti_nejapa_drw_476k_2010",
    "infrastructure", "building_materials", "other",
    "Bonatti — Nejapa disaster relief warehouse design/build",
    "El Salvador",
    "28 Sep 2010: U.S. Army Corps of Engineers awards task order 0004 under W9127809D0064 to Bonatti for design/build disaster relief warehouse in Nejapa, El Salvador; obligated USD 476,053.08. CapEx face = award obligation.",
    "476053.08", "2010-09-28", "2010", "13.813", "-89.230",
    "Disaster relief warehouse, Nejapa, El Salvador (USASpending description).",
    "usaspending_bonatti_nejapa_drw_476k_2010",
    "D/B DISASTER RELIEF WAREHOUSE, NEJAPA, EL SALVADOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127809D0064_9700/",
    "Actor: Bonatti Ingenieros y Arquitectos (Guatemala) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle978",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0004_9700_W9127809D0064_9700 (Bonatti Nejapa DRW). Signed 2010-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0004_9700_W9127809D0064_9700/.",
    "USASpending: Bonatti Nejapa DRW USD 0.476m. Supports bonatti_nejapa_drw_476k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 476053.08; date_signed 2010-09-28.",
)

row_doc(
    "mercadal_mout_chile_467k_2012",
    "infrastructure", "building_materials", "other",
    "Gonzalo Mercadal — MOUT training structures Chile PKO",
    "Chile",
    "2 Jan 2012: U.S. Army Corps of Engineers awards contract W912CL12C0001 to Gonzalo Mercadal for construction of Military Operations on Urban Terrain (MOUT) training structures for peacekeeping operations field exercise; obligated USD 467,456.92. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "467456.92", "2012-01-02", "2012", "", "",
    "MOUT training structures, Chile (USASpending PoP Chile; site not named — lat/lon blank).",
    "usaspending_mercadal_mout_chile_467k_2012",
    "CONSTRUCT MILITARY OPERATIONS ON URBAN TERRAIN (MOUT) TRAINING STRUCTURES FOR PEACE KEEPING OPERATIONS (PKO-A 2012 FEILD EXERCISE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL12C0001_9700_-NONE-_-NONE-/",
    "Actor: Gonzalo Mercadal y Compañía Limitada (Viña del Mar, Chile) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle978",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL12C0001_9700_-NONE-_-NONE- (Mercadal MOUT Chile). Signed 2012-01-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL12C0001_9700_-NONE-_-NONE-/.",
    "USASpending: Mercadal MOUT Chile USD 0.467m. Supports mercadal_mout_chile_467k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 467456.92; date_signed 2012-01-02.",
)

row_doc(
    "tabcon_guyana_cmr_roof_464k_2019",
    "infrastructure", "building_materials", "us",
    "Tabcon — U.S. Embassy Georgetown CMR roof replacement",
    "Guyana",
    "1 Aug 2019: Department of State awards contract 19GE5019C0017 to Tabcon for replacement of the roof on the Chief of Mission Residence of the U.S. Embassy Georgetown, Guyana; obligated USD 463,787.38. CapEx face = award obligation.",
    "463787.38", "2019-08-01", "2019", "6.801", "-58.155",
    "CMR roof replacement, U.S. Embassy Georgetown, Guyana (USASpending description).",
    "usaspending_tabcon_guyana_cmr_roof_464k_2019",
    "REPLACE THE ROOF ON THE CHIEF OF MISSION RESIDENCE OF THE US EMBASSY GEORGETOWN, GUYA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5019C0017_1900_-NONE-_-NONE-/",
    "Actor: Tabcon Inc. (Queen Creek AZ, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle978",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5019C0017_1900_-NONE-_-NONE- (Tabcon Guyana CMR roof). Signed 2019-08-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5019C0017_1900_-NONE-_-NONE-/.",
    "USASpending: Tabcon Guyana CMR roof USD 0.464m. Supports tabcon_guyana_cmr_roof_464k_2019.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 463787.38; date_signed 2019-08-01.",
)

row_doc(
    "trane_lima_chiller_461k_2017",
    "infrastructure", "building_materials", "other",
    "Trane Technologies Peru — Lima chiller replacement",
    "Peru",
    "28 Feb 2017: Department of State awards contract SGE50017C0012 to Trane Technologies Peru for Lima chiller replacement project; obligated USD 460,535. CapEx face = award obligation.",
    "460535", "2017-02-28", "2017", "-12.046", "-77.043",
    "Chiller replacement, Lima, Peru (USASpending description).",
    "usaspending_trane_lima_chiller_461k_2017",
    "IGF::OT::IGF LIMA, PERU - CHILLER REPLACEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50017C0012_1900_-NONE-_-NONE-/",
    "Actor: Trane Technologies Peru S.A.C. (Lima) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle978",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SGE50017C0012_1900_-NONE-_-NONE- (Trane Lima chiller). Signed 2017-02-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SGE50017C0012_1900_-NONE-_-NONE-/.",
    "USASpending: Trane Lima chiller USD 0.461m. Supports trane_lima_chiller_461k_2017.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 460535; date_signed 2017-02-28.",
)

# === Cycle 979 ===
row_doc(
    "ect_hap8800_warehouse_cr_458k_2010",
    "infrastructure", "building_materials", "other",
    "ECT — HAP 8800 warehouse design/build Costa Rica",
    "Costa Rica",
    "20 Sep 2010: U.S. Army Corps of Engineers awards task order 0011 under W9127809D0071 to Empresa de Construcción y Transporte for design/build HAP 8800 warehouse in Costa Rica; obligated USD 458,017.35. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "458017.35", "2010-09-20", "2010", "", "",
    "HAP 8800 warehouse, Costa Rica (USASpending PoP Costa Rica; site not named — lat/lon blank).",
    "usaspending_ect_hap8800_warehouse_cr_458k_2010",
    "D/B HAP 8800 WAREHOUSE, COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127809D0071_9700/",
    "Actor: Empresa de Construcción y Transporte (San Pedro Sula, Honduras) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle979",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0011_9700_W9127809D0071_9700 (ECT HAP 8800 warehouse). Signed 2010-09-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0011_9700_W9127809D0071_9700/.",
    "USASpending: ECT HAP 8800 warehouse USD 0.458m. Supports ect_hap8800_warehouse_cr_458k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 458017.35; date_signed 2010-09-20.",
)

row_doc(
    "misc_peru_six_classroom_454k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Peru six-classroom school",
    "Peru",
    "8 May 2010: U.S. Army Corps of Engineers awards contract W912CL10C0014 for six-classroom school with restrooms (PoP Peru); obligated USD 453,598.45. CapEx face = award obligation. Recipient redacted; site not named — lat/lon blank.",
    "453598.45", "2010-05-08", "2010", "", "",
    "Six-classroom school with restrooms, Peru (USASpending PoP Peru; site not named — lat/lon blank).",
    "usaspending_misc_peru_six_classroom_454k_2010",
    "SIX CLASSROOM SCHOOL WITH RESTROOMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0014_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle979",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0014_9700_-NONE-_-NONE- (Peru six-classroom). Signed 2010-05-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0014_9700_-NONE-_-NONE-/.",
    "USASpending: Peru six-classroom school USD 0.454m. Supports misc_peru_six_classroom_454k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 453598.45; date_signed 2010-05-08.",
)

row_doc(
    "arboleda_quito_wtp_454k_2022",
    "resources", "water", "other",
    "Arboleda Faini Hidrotecnología — U.S. Embassy Quito WTP upgrade",
    "Ecuador",
    "23 Sep 2022: Department of State awards contract 19GE5022C0041 to Arboleda Faini Hidrotecnología for design/construction of water treatment system upgrade at American Embassy Quito; obligated USD 453,588.27. CapEx face = award obligation.",
    "453588.27", "2022-09-23", "2022", "-0.180", "-78.467",
    "Water treatment system upgrade, U.S. Embassy Quito (USASpending description).",
    "usaspending_arboleda_quito_wtp_454k_2022",
    "DESIGN/CONSTRUCTION SERVICES FOR THE WATER TREATMENT SYSTEM UPGRADE PROJECT, AMERICAN EMBASSY QUITO, ECUADOR.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5022C0041_1900_-NONE-_-NONE-/",
    "Actor: Arboleda Faini Hidrotecnología C. Ltda. (Quito) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle979",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5022C0041_1900_-NONE-_-NONE- (Arboleda Quito WTP). Signed 2022-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5022C0041_1900_-NONE-_-NONE-/.",
    "USASpending: Arboleda Quito WTP USD 0.454m. Supports arboleda_quito_wtp_454k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 453588.27; date_signed 2022-09-23.",
)

row_doc(
    "proyectos_2nd_floor_451k_2012",
    "infrastructure", "building_materials", "other",
    "Proyectos Civiles — construct 2nd floor (Colombia)",
    "Colombia",
    "24 Sep 2012: U.S. Army Corps of Engineers awards contract W913FT12C0024 to Proyectos Civiles for construct 2nd floor (PoP Colombia); obligated USD 451,139.77. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "451139.77", "2012-09-24", "2012", "", "",
    "Construct 2nd floor, Colombia (USASpending PoP Colombia; site not named — lat/lon blank).",
    "usaspending_proyectos_2nd_floor_451k_2012",
    "CONSTRUCT 2ND FLOOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0024_9700_-NONE-_-NONE-/",
    "Actor: Proyectos Civiles S y M Limitada (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle979",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT12C0024_9700_-NONE-_-NONE- (Proyectos 2nd floor). Signed 2012-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT12C0024_9700_-NONE-_-NONE-/.",
    "USASpending: Proyectos 2nd floor USD 0.451m. Supports proyectos_2nd_floor_451k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 451139.77; date_signed 2012-09-24.",
)

row_doc(
    "misc_sao_paulo_stormwater_451k_2020",
    "resources", "water", "other",
    "Miscellaneous foreign awardees — São Paulo storm water mitigation",
    "Brazil",
    "7 Aug 2020: Department of State awards contract 19AQMM20C0044 for São Paulo storm water mitigation; obligated USD 450,919.71. CapEx face = award obligation. Recipient redacted.",
    "450919.71", "2020-08-07", "2020", "-23.551", "-46.633",
    "Storm water mitigation, São Paulo, Brazil (USASpending description; São Paulo pin).",
    "usaspending_misc_sao_paulo_stormwater_451k_2020",
    "SAO PAULO STORM WATER MITIGATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0044_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle979",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM20C0044_1900_-NONE-_-NONE- (São Paulo storm water). Signed 2020-08-07. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM20C0044_1900_-NONE-_-NONE-/.",
    "USASpending: São Paulo storm water USD 0.451m. Supports misc_sao_paulo_stormwater_451k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 450919.71; date_signed 2020-08-07.",
)

# === Cycle 980 ===
row_doc(
    "andrade_quito_classroom_451k_2023",
    "infrastructure", "building_materials", "other",
    "Constructora Andrade — classroom construction for U.S. Embassy Quito",
    "Ecuador",
    "11 Jul 2023: Department of State awards contract 19GE5023C0021 to Constructora Andrade Asociados for classroom construction on behalf of U.S. Embassy Quito; obligated USD 450,589.46. CapEx face = award obligation.",
    "450589.46", "2023-07-11", "2023", "-0.180", "-78.467",
    "Classroom construction, U.S. Embassy Quito (USASpending description).",
    "usaspending_andrade_quito_classroom_451k_2023",
    "ACQUISITION OF CLASSROOM CONSTRUCTION ON BEHALF OF U.S. EMBASSY QUITO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0021_1900_-NONE-_-NONE-/",
    "Actor: Constructora Andrade Asociados S.C.C. (Quito) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle980",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19GE5023C0021_1900_-NONE-_-NONE- (Andrade Quito classroom). Signed 2023-07-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19GE5023C0021_1900_-NONE-_-NONE-/.",
    "USASpending: Andrade Quito classroom USD 0.451m. Supports andrade_quito_classroom_451k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 450589.46; date_signed 2023-07-11.",
)

row_doc(
    "maheias_san_antonio_school_448k_2021",
    "infrastructure", "building_materials", "other",
    "Maheias United Concrete — San Antonio Corozal 3-room school",
    "Belize",
    "12 Jul 2021: U.S. Army Corps of Engineers awards contract W912CL21C0005 to Maheias United Concrete for construction of a 3-room school building in San Antonio, Corozal, Belize; obligated USD 448,123.20. CapEx face = award obligation.",
    "448123.20", "2021-07-12", "2021", "18.236", "-88.376",
    "3-room school building, San Antonio, Corozal, Belize (USASpending description).",
    "usaspending_maheias_san_antonio_school_448k_2021",
    "CONSTRUCTION A 3-ROOM SCHOOL BUILDING IN SAN ANTONIO, COROZAL, BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL21C0005_9700_-NONE-_-NONE-/",
    "Actor: Maheias United Concrete & Supplies Ltd. (Belize City) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle980",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL21C0005_9700_-NONE-_-NONE- (Maheias San Antonio school). Signed 2021-07-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL21C0005_9700_-NONE-_-NONE-/.",
    "USASpending: Maheias San Antonio school USD 0.448m. Supports maheias_san_antonio_school_448k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 448123.20; date_signed 2021-07-12.",
)

row_doc(
    "css_santo_domingo_pko_436k_2012",
    "infrastructure", "building_materials", "us",
    "CSS International — Santo Domingo PKO training school refurbishment",
    "Dominican Republic",
    "24 Jan 2012: U.S. Army Corps of Engineers awards contract W912CL12C0002 to CSS International for refurbishment of peacekeeping operations training school buildings in Santo Domingo, Dominican Republic; obligated USD 436,337.80. CapEx face = award obligation.",
    "436337.80", "2012-01-24", "2012", "18.486", "-69.931",
    "PKO training school buildings, Santo Domingo, Dominican Republic (USASpending description).",
    "usaspending_css_santo_domingo_pko_436k_2012",
    "REFURBISH PEACE KEEPING OPERATIONS TRAINING SCHOOL BUILDINGS IN SANTO DOMINGO, DOMINICAN REPUBLIC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL12C0002_9700_-NONE-_-NONE-/",
    "Actor: CSS International Holdings Inc. (Ada MI, U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle980",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL12C0002_9700_-NONE-_-NONE- (CSS Santo Domingo PKO). Signed 2012-01-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL12C0002_9700_-NONE-_-NONE-/.",
    "USASpending: CSS Santo Domingo PKO USD 0.436m. Supports css_santo_domingo_pko_436k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 436337.80; date_signed 2012-01-24.",
)

row_doc(
    "seobra_montevideo_warehouse_442k_2010",
    "infrastructure", "building_materials", "other",
    "Seobra — Montevideo relief warehouse design/build",
    "Uruguay",
    "21 Dec 2010: U.S. Army Corps of Engineers awards task order 0003 under W9127809D0081 to Seobra for design/build relief warehouse in Montevideo, Uruguay; obligated USD 442,143. CapEx face = award obligation.",
    "442143", "2010-12-21", "2010", "-34.901", "-56.164",
    "Relief warehouse, Montevideo, Uruguay (USASpending description).",
    "usaspending_seobra_montevideo_warehouse_442k_2010",
    "TAS::97 0819::TAS DESGIN BUILD RELIEF WAREHOUSE, MONTEVIDEO, URUGUAY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127809D0081_9700/",
    "Actor: Seobra S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle980",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W9127809D0081_9700 (Seobra Montevideo warehouse). Signed 2010-12-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W9127809D0081_9700/.",
    "USASpending: Seobra Montevideo warehouse USD 0.442m. Supports seobra_montevideo_warehouse_442k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 442143; date_signed 2010-12-21.",
)

row_doc(
    "seobra_san_pedro_school_440k_2021",
    "infrastructure", "building_materials", "other",
    "Seobra — San Pedro Corozal 3-classroom school",
    "Belize",
    "17 Jun 2021: U.S. Army Corps of Engineers awards contract W912CL21C0006 to Seobra for construction of a 3-classroom school building in San Pedro, Corozal, Belize; obligated USD 440,286.50. CapEx face = award obligation.",
    "440286.50", "2021-06-17", "2021", "18.350", "-88.340",
    "3-classroom school building, San Pedro, Corozal, Belize (USASpending description).",
    "usaspending_seobra_san_pedro_school_440k_2021",
    "CONSTRUCTION OF A 3 CLASSROOM SCHOOL BUILDING IN SAN PEDRO, COROZAL, BELIZE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL21C0006_9700_-NONE-_-NONE-/",
    "Actor: Seobra S.A.S. (Bogotá) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle980",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL21C0006_9700_-NONE-_-NONE- (Seobra San Pedro school). Signed 2021-06-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL21C0006_9700_-NONE-_-NONE-/.",
    "USASpending: Seobra San Pedro school USD 0.440m. Supports seobra_san_pedro_school_440k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 440286.50; date_signed 2021-06-17.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    supports = entry.get("supports") or []
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        prev = existing.get("supports") or []
        for s in supports:
            if s not in prev:
                prev.append(s)
        existing.update(entry)
        existing["supports"] = prev
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added = []
    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        upsert_bib(bib, bib_by, bib_entry)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})
    BIB.write_text(yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8")
    print(f"cycles978-980 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
