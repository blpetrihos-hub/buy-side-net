#!/usr/bin/env python3
"""Cycles 1280–1285: USASpending LatAm CapEx (security/electrical/construction + residual other).

Seeds: 20262280–20262285. Thin top-up dry.
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

# === Cycle 1280 ===
row_doc(
    "quality_logistics_bahamas_marsh_harbour_security_3797k_2024",
    "infrastructure", "building_materials", "us",
    "Quality Logistics and Procurement — Bahamas Marsh Harbour security upgrades",
    "Bahamas",
    "30 Sep 2024: Department of State awards contract to QUALITY LOGISTICS AND PROCUREMENT SERVICES LIMITED for Marsh Harbour security upgrades (PoP Bahamas); obligated USD 3797564.43. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "3797564.43", "2024-09-30", "2024", "", "",
    "MARSH HARBOUR SECURITY UPGRADES, Bahamas (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_quality_logistics_bahamas_marsh_harbour_security_3797k_2024",
    "MARSH HARBOUR SECURITY UPGRADES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24C0147_1900_-NONE-_-NONE-/",
    "Actor: QUALITY LOGISTICS AND PROCUREMENT SERVICES LIMITED (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1280",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM24C0147_1900_-NONE-_-NONE- (quality_logistics_bahamas_marsh_harbour_security_3797k_2024). Signed 2024-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24C0147_1900_-NONE-_-NONE-/.",
    "USASpending: quality_logistics_bahamas_marsh_harbour_security_3797k_2024 USD 3.798m. Supports quality_logistics_bahamas_marsh_harbour_security_3797k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 3797564.43; date_signed 2024-09-30.",
    investment_type="epc",
)

# === Cycle 1280 ===
row_doc(
    "nika_emr_peru_lima_physical_security_2830k_2012",
    "infrastructure", "building_materials", "us",
    "NIKA & EMR Joint Venture — Lima physical security upgrade",
    "Peru",
    "8 Mar 2012: Department of State awards contract to NIKA & EMR JOINT VENTURE for Lima Peru physical security upgrade project (PoP Peru); obligated USD 2830196. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2830196", "2012-03-08", "2012", "", "",
    "LIMA, PERU PHYSICAL SECURITY UPGRADE PROJECT, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_nika_emr_peru_lima_physical_security_2830k_2012",
    "LIMA, PERU PHYSICAL SECURITY UPGRADE PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F0910_1900_SAQMMA08D0020_1900/",
    "Actor: NIKA & EMR JOINT VENTURE (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1280",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F0910_1900_SAQMMA08D0020_1900 (nika_emr_peru_lima_physical_security_2830k_2012). Signed 2012-03-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F0910_1900_SAQMMA08D0020_1900/.",
    "USASpending: nika_emr_peru_lima_physical_security_2830k_2012 USD 2.830m. Supports nika_emr_peru_lima_physical_security_2830k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2830196.0; date_signed 2012-03-08.",
    investment_type="epc",
)

# === Cycle 1280 ===
row_doc(
    "industrias_bendig_costarica_sierpe_base_camp_1410k_2022",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — Costa Rica Sierpe base camp construction",
    "Costa Rica",
    "20 Oct 2022: Department of State awards contract to INDUSTRIAS BENDIG SA for Sierpe base camp construction (PoP Costa Rica); obligated USD 1410982.80. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "1410982.80", "2022-10-20", "2022", "", "",
    "SIERPE BASE CAMP CONSTRUCTION, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_industrias_bendig_costarica_sierpe_base_camp_1410k_2022",
    "SIERPE BASE CAMP CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0166_1900_-NONE-_-NONE-/",
    "Actor: INDUSTRIAS BENDIG SA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1280",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22C0166_1900_-NONE-_-NONE- (industrias_bendig_costarica_sierpe_base_camp_1410k_2022). Signed 2022-10-20. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0166_1900_-NONE-_-NONE-/.",
    "USASpending: industrias_bendig_costarica_sierpe_base_camp_1410k_2022 USD 1.411m. Supports industrias_bendig_costarica_sierpe_base_camp_1410k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1410982.8; date_signed 2022-10-20.",
    investment_type="epc",
)

# === Cycle 1280 ===
row_doc(
    "industrias_bendig_costarica_incinerator_building_983k_2021",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — Costa Rica OIJ Poder Judicial incinerator building",
    "Costa Rica",
    "24 Sep 2021: Department of State awards contract to INDUSTRIAS BENDIG SA for OIJ Poder Judicial incinerator building (PoP Costa Rica); obligated USD 983275.80. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "983275.80", "2021-09-24", "2021", "", "",
    "OIJ PODER JUDICIAL - INCINERATOR BUILDING, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_industrias_bendig_costarica_incinerator_building_983k_2021",
    "OIJ PODER JUDICIAL - INCINERATOR BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21C0172_1900_-NONE-_-NONE-/",
    "Actor: INDUSTRIAS BENDIG SA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1280",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM21C0172_1900_-NONE-_-NONE- (industrias_bendig_costarica_incinerator_building_983k_2021). Signed 2021-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM21C0172_1900_-NONE-_-NONE-/.",
    "USASpending: industrias_bendig_costarica_incinerator_building_983k_2021 USD 0.983m. Supports industrias_bendig_costarica_incinerator_building_983k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 983275.8; date_signed 2021-09-24.",
    investment_type="epc",
)

# === Cycle 1280 ===
row_doc(
    "misc_colombia_larandia_heliport_fence_601k_2010",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Colombia Larandia heliport perimeter fence",
    "Colombia",
    "18 Sep 2010: Department of Defense awards contract to MISCELLANEOUS FOREIGN AWARDEES for Larandia heliport perimeter fence (PoP Colombia); obligated USD 601615.31. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "601615.31", "2010-09-18", "2010", "", "",
    "LARANDIA HELIPORT PERIMETER FENCE, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_larandia_heliport_fence_601k_2010",
    "LARANDIA HELIPORT PERIMETER FENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0047_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1280",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL10C0047_9700_-NONE-_-NONE- (misc_colombia_larandia_heliport_fence_601k_2010). Signed 2010-09-18. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL10C0047_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_larandia_heliport_fence_601k_2010 USD 0.602m. Supports misc_colombia_larandia_heliport_fence_601k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 601615.31; date_signed 2010-09-18.",
    investment_type="epc",
)

# === Cycle 1281 ===
row_doc(
    "mesan_martinez_jamaica_avr_replacement_887k_2011",
    "energy", "power_plants_grid", "us",
    "Mesan-Martinez Joint Venture — Kingston automated voltage regulator replacement",
    "Jamaica",
    "15 Sep 2011: Department of State awards contract to MESAN-MARTINEZ JOINT VENTURE LLP for design-build automated voltage regulator replacement in Kingston (PoP Jamaica); obligated USD 887400. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "887400", "2011-09-15", "2011", "", "",
    "DESIGN BUILD AUTOMATED VOLTAGE REGULATOR REPLACEMENT IN KINGSTON, JAMAICA, Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mesan_martinez_jamaica_avr_replacement_887k_2011",
    "DESIGN BUILD AUTOMATED VOLTAGE REGULATOR REPLACEMENT IN KINGSTON, JAMAICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3644_1900_SAQMMA11D0062_1900/",
    "Actor: MESAN-MARTINEZ JOINT VENTURE LLP (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1281",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F3644_1900_SAQMMA11D0062_1900 (mesan_martinez_jamaica_avr_replacement_887k_2011). Signed 2011-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F3644_1900_SAQMMA11D0062_1900/.",
    "USASpending: mesan_martinez_jamaica_avr_replacement_887k_2011 USD 0.887m. Supports mesan_martinez_jamaica_avr_replacement_887k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 887400.0; date_signed 2011-09-15.",
    investment_type="epc",
)

# === Cycle 1281 ===
row_doc(
    "mesan_martinez_jamaica_kingston_cac_security_869k_2010",
    "infrastructure", "building_materials", "us",
    "Mesan-Martinez Joint Venture — Kingston CAC security upgrade",
    "Jamaica",
    "30 Sep 2010: Department of State awards contract to MESAN-MARTINEZ JOINT VENTURE LLP for Kingston CAC security upgrade (PoP Jamaica); obligated USD 869095.16. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "869095.16", "2010-09-30", "2010", "", "",
    "TAS::19 0535 000::TAS KINGSTON CAC SECURITY UPGRADE., Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mesan_martinez_jamaica_kingston_cac_security_869k_2010",
    "TAS::19 0535 000::TAS KINGSTON CAC SECURITY UPGRADE.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F5091_1900_SAQMMA08D0015_1900/",
    "Actor: MESAN-MARTINEZ JOINT VENTURE LLP (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1281",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F5091_1900_SAQMMA08D0015_1900 (mesan_martinez_jamaica_kingston_cac_security_869k_2010). Signed 2010-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F5091_1900_SAQMMA08D0015_1900/.",
    "USASpending: mesan_martinez_jamaica_kingston_cac_security_869k_2010 USD 0.869m. Supports mesan_martinez_jamaica_kingston_cac_security_869k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 869095.16; date_signed 2010-09-30.",
    investment_type="epc",
)

# === Cycle 1281 ===
row_doc(
    "bq_arquitectura_colombia_tumaco_fence_516k_2015",
    "infrastructure", "building_materials", "other",
    "B Q Arquitectura — Colombia Tumaco perimeter fence",
    "Colombia",
    "6 Jul 2015: Department of Defense awards contract to B Q ARQUITECTURA LTDA for Tumaco perimeter fence (PoP Colombia); obligated USD 516102.30. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "516102.30", "2015-07-06", "2015", "", "",
    "IGF::OT::IGF TUMACO PERIMETER FENCE, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bq_arquitectura_colombia_tumaco_fence_516k_2015",
    "IGF::OT::IGF TUMACO PERIMETER FENCE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT15C0006_9700_-NONE-_-NONE-/",
    "Actor: B Q ARQUITECTURA LTDA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1281",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT15C0006_9700_-NONE-_-NONE- (bq_arquitectura_colombia_tumaco_fence_516k_2015). Signed 2015-07-06. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT15C0006_9700_-NONE-_-NONE-/.",
    "USASpending: bq_arquitectura_colombia_tumaco_fence_516k_2015 USD 0.516m. Supports bq_arquitectura_colombia_tumaco_fence_516k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 516102.3; date_signed 2015-07-06.",
    investment_type="epc",
)

# === Cycle 1281 ===
row_doc(
    "norma_gutierrez_mexico_tca_window_replacement_239k_2023",
    "infrastructure", "building_materials", "other",
    "Norma Isabel Gutiérrez López — Mexico TCA window replacement",
    "Mexico",
    "22 May 2023: Department of State awards contract to NORMA ISABEL GUTIERREZ LOPEZ for FAC TCA window replacement (PoP Mexico); obligated USD 239523.46. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "239523.46", "2023-05-22", "2023", "", "",
    "MEX-FAC-7903R-FWP579-TCA WINDOW REPLACEMENT, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_norma_gutierrez_mexico_tca_window_replacement_239k_2023",
    "MEX-FAC-7903R-FWP579-TCA WINDOW REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5323C0006_1900_-NONE-_-NONE-/",
    "Actor: NORMA ISABEL GUTIERREZ LOPEZ — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1281",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5323C0006_1900_-NONE-_-NONE- (norma_gutierrez_mexico_tca_window_replacement_239k_2023). Signed 2023-05-22. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5323C0006_1900_-NONE-_-NONE-/.",
    "USASpending: norma_gutierrez_mexico_tca_window_replacement_239k_2023 USD 0.240m. Supports norma_gutierrez_mexico_tca_window_replacement_239k_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 239523.46; date_signed 2023-05-22.",
    investment_type="epc",
)

# === Cycle 1281 ===
row_doc(
    "castro_elsalvador_ac_electrical_upgrades_271k_2025",
    "energy", "power_plants_grid", "other",
    "Francisco Rigoberto Castro — El Salvador AC installation and electrical upgrades",
    "El Salvador",
    "14 Jul 2025: Department of Defense awards contract to FRANCISCO RIGOBERTO CASTRO BARRERA for air conditioning installation and electrical upgrades (PoP El Salvador); obligated USD 271880. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "271880", "2025-07-14", "2025", "", "",
    "AIR CONDITIONING INSTALLATION AND ELECTRICAL UPGRADES., El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_castro_elsalvador_ac_electrical_upgrades_271k_2025",
    "AIR CONDITIONING INSTALLATION AND ELECTRICAL UPGRADES.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125C0005_9700_-NONE-_-NONE-/",
    "Actor: FRANCISCO RIGOBERTO CASTRO BARRERA — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1281",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_H9228125C0005_9700_-NONE-_-NONE- (castro_elsalvador_ac_electrical_upgrades_271k_2025). Signed 2025-07-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125C0005_9700_-NONE-_-NONE-/.",
    "USASpending: castro_elsalvador_ac_electrical_upgrades_271k_2025 USD 0.272m. Supports castro_elsalvador_ac_electrical_upgrades_271k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 271880.0; date_signed 2025-07-14.",
    investment_type="epc",
)

# === Cycle 1282 ===
row_doc(
    "jimenez_mexico_reynosa_electrical_663k_2016",
    "energy", "power_plants_grid", "us",
    "Jimenez Engineering Solutions — Reynosa electrical upgrades",
    "Mexico",
    "14 Jan 2016: Department of Agriculture awards contract to JIMENEZ ENGINEERING SOLUTIONS, LLC for Reynosa electrical upgrades (PoP Mexico); obligated USD 663736.52. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "663736.52", "2016-01-14", "2016", "", "",
    "IGF::OT::IGF REYNOSA ELECTRICAL UPGRADES, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_jimenez_mexico_reynosa_electrical_663k_2016",
    "IGF::OT::IGF REYNOSA ELECTRICAL UPGRADES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG32KWC160009_12K3_-NONE-_-NONE-/",
    "Actor: JIMENEZ ENGINEERING SOLUTIONS, LLC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1282",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AG32KWC160009_12K3_-NONE-_-NONE- (jimenez_mexico_reynosa_electrical_663k_2016). Signed 2016-01-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG32KWC160009_12K3_-NONE-_-NONE-/.",
    "USASpending: jimenez_mexico_reynosa_electrical_663k_2016 USD 0.664m. Supports jimenez_mexico_reynosa_electrical_663k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 663736.52; date_signed 2016-01-14.",
    investment_type="epc",
)

# === Cycle 1282 ===
row_doc(
    "jimenez_mexico_reynosa_fire_protection_550k_2016",
    "infrastructure", "building_materials", "us",
    "Jimenez Engineering Solutions — Reynosa fire protection upgrades",
    "Mexico",
    "4 Feb 2016: Department of Agriculture awards contract to JIMENEZ ENGINEERING SOLUTIONS, LLC for fire protection upgrades Reynosa MX (PoP Mexico); obligated USD 550907.94. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "550907.94", "2016-02-04", "2016", "", "",
    "IGF::OT::IGF  FIRE PROTECTION UPGRADES IS FFEF REYNOSA MX, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_jimenez_mexico_reynosa_fire_protection_550k_2016",
    "IGF::OT::IGF  FIRE PROTECTION UPGRADES IS FFEF REYNOSA MX",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG32KWC160016_12K3_-NONE-_-NONE-/",
    "Actor: JIMENEZ ENGINEERING SOLUTIONS, LLC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1282",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_AG32KWC160016_12K3_-NONE-_-NONE- (jimenez_mexico_reynosa_fire_protection_550k_2016). Signed 2016-02-04. https://api.usaspending.gov/api/v2/awards/CONT_AWD_AG32KWC160016_12K3_-NONE-_-NONE-/.",
    "USASpending: jimenez_mexico_reynosa_fire_protection_550k_2016 USD 0.551m. Supports jimenez_mexico_reynosa_fire_protection_550k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 550907.94; date_signed 2016-02-04.",
    investment_type="epc",
)

# === Cycle 1282 ===
row_doc(
    "castro_elsalvador_shoothouse_164k_2025",
    "infrastructure", "building_materials", "other",
    "Francisco Rigoberto Castro — El Salvador shoothouse construction",
    "El Salvador",
    "21 Apr 2025: Department of Defense awards contract to FRANCISCO RIGOBERTO CASTRO BARRERA for construction of shoothouse (PoP El Salvador); obligated USD 164038.32. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "164038.32", "2025-04-21", "2025", "", "",
    "CONSTRUCTION OF SHOOTHOUSE, El Salvador (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_castro_elsalvador_shoothouse_164k_2025",
    "CONSTRUCTION OF SHOOTHOUSE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125C0004_9700_-NONE-_-NONE-/",
    "Actor: FRANCISCO RIGOBERTO CASTRO BARRERA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1282",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_H9228125C0004_9700_-NONE-_-NONE- (castro_elsalvador_shoothouse_164k_2025). Signed 2025-04-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_H9228125C0004_9700_-NONE-_-NONE-/.",
    "USASpending: castro_elsalvador_shoothouse_164k_2025 USD 0.164m. Supports castro_elsalvador_shoothouse_164k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 164038.32; date_signed 2025-04-21.",
    investment_type="epc",
)

# === Cycle 1282 ===
row_doc(
    "industrias_bendig_costarica_construction_745k_2014",
    "infrastructure", "building_materials", "other",
    "Industrias Bendig — Costa Rica construction services",
    "Costa Rica",
    "1 Sep 2014: Department of State awards contract to INDUSTRIAS BENDIG SA for construction services firm fixed-price (PoP Costa Rica); obligated USD 745379. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "745379", "2014-09-01", "2014", "", "",
    "TOTAL FIRM FIXED-PRICE: CONSTRUCTION SERVICES, INCLUDING ALL LABOR, MATERIALS, EQUIPMENT, OVERHEAD, OTHER INDI, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_industrias_bendig_costarica_construction_745k_2014",
    "TOTAL FIRM FIXED-PRICE: CONSTRUCTION SERVICES, INCLUDING ALL LABOR, MATERIALS, EQUIPMENT, OVERHEAD, OTHER INDIRECT COSTS, COSTS FOR INSURANCE (OTHER THAN DBA), LETTER OF CREDITS, AND PROFIT: (SEE SECTION C.1.3.1) IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0160_1900_-NONE-_-NONE-/",
    "Actor: INDUSTRIAS BENDIG SA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1282",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14C0160_1900_-NONE-_-NONE- (industrias_bendig_costarica_construction_745k_2014). Signed 2014-09-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0160_1900_-NONE-_-NONE-/.",
    "USASpending: industrias_bendig_costarica_construction_745k_2014 USD 0.745m. Supports industrias_bendig_costarica_construction_745k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 745379.0; date_signed 2014-09-01.",
    investment_type="epc",
)

# === Cycle 1282 ===
row_doc(
    "industrias_bendig_costarica_sierpe_water_pump_92k_2024",
    "resources", "water", "other",
    "Industrias Bendig — Costa Rica Sierpe water pump and filtering system",
    "Costa Rica",
    "23 Sep 2024: Department of State awards contract to INDUSTRIAS BENDIG SA for INL water pump and filtering system Sierpe (PoP Costa Rica); obligated USD 92700. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "92700", "2024-09-23", "2024", "", "",
    "INL 1930.0 WATER PUMP & FILTERING SYSTEM, SIERPE BASE CAMP, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_industrias_bendig_costarica_sierpe_water_pump_92k_2024",
    "INL 1930.0 WATER PUMP & FILTERING SYSTEM, SIERPE BASE CAMP",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8024P1039_1900_-NONE-_-NONE-/",
    "Actor: INDUSTRIAS BENDIG SA — other. Official USASpending Award API. Shuffle water.",
    "hunt_cycle1282",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8024P1039_1900_-NONE-_-NONE- (industrias_bendig_costarica_sierpe_water_pump_92k_2024). Signed 2024-09-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8024P1039_1900_-NONE-_-NONE-/.",
    "USASpending: industrias_bendig_costarica_sierpe_water_pump_92k_2024 USD 0.093m. Supports industrias_bendig_costarica_sierpe_water_pump_92k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 92700.0; date_signed 2024-09-23.",
    investment_type="equipment_supply",
)

# === Cycle 1283 ===
row_doc(
    "bmk_jamaica_kingston_physical_security_401k_2016",
    "infrastructure", "building_materials", "us",
    "BMK Construction Services — Kingston embassy physical security upgrades",
    "Jamaica",
    "29 Aug 2016: Department of State awards contract to BMK CONSTRUCTION SERVICES, INC. for physical security upgrades U.S. Embassy Kingston (PoP Jamaica); obligated USD 401452.19. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "401452.19", "2016-08-29", "2016", "", "",
    "PHYSICAL SECURITY UPGRADES US EMBASSY KINGSTON JAMAICA.  IGF::OT::IGF, Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_bmk_jamaica_kingston_physical_security_401k_2016",
    "PHYSICAL SECURITY UPGRADES US EMBASSY KINGSTON JAMAICA.  IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0224_1900_-NONE-_-NONE-/",
    "Actor: BMK CONSTRUCTION SERVICES, INC. (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1283",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA16C0224_1900_-NONE-_-NONE- (bmk_jamaica_kingston_physical_security_401k_2016). Signed 2016-08-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA16C0224_1900_-NONE-_-NONE-/.",
    "USASpending: bmk_jamaica_kingston_physical_security_401k_2016 USD 0.401m. Supports bmk_jamaica_kingston_physical_security_401k_2016.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 401452.19; date_signed 2016-08-29.",
    investment_type="epc",
)

# === Cycle 1283 ===
row_doc(
    "kva_mexico_hermosillo_electrical_567k_2010",
    "energy", "power_plants_grid", "us",
    "KVA Electric — Hermosillo power systems electrical work",
    "Mexico",
    "8 Sep 2010: Department of State awards contract to KVA ELECTRIC INC for power systems Hermosillo electrical work (PoP Mexico); obligated USD 567119.67. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "567119.67", "2010-09-08", "2010", "", "",
    "POWER SYSTEMS HERMOSILLO ELECTRICAL WORK, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_kva_mexico_hermosillo_electrical_567k_2010",
    "POWER SYSTEMS HERMOSILLO ELECTRICAL WORK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F3725_1900_SALMEC05D0011_1900/",
    "Actor: KVA ELECTRIC INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1283",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F3725_1900_SALMEC05D0011_1900 (kva_mexico_hermosillo_electrical_567k_2010). Signed 2010-09-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F3725_1900_SALMEC05D0011_1900/.",
    "USASpending: kva_mexico_hermosillo_electrical_567k_2010 USD 0.567m. Supports kva_mexico_hermosillo_electrical_567k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 567119.67; date_signed 2010-09-08.",
    investment_type="epc",
)

# === Cycle 1283 ===
row_doc(
    "akj_mexico_cmr_double_pane_windows_79k_2021",
    "infrastructure", "building_materials", "other",
    "Servicios AKJ — Mexico CMR double pane windows replacement",
    "Mexico",
    "23 Apr 2021: Department of State awards contract to SERVICIOS AKJ, S.A DE C.V for FAC double pane windows replacement in the CMR (PoP Mexico); obligated USD 79503.68. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "79503.68", "2021-04-23", "2021", "", "",
    "MEX FAC DOUBLE PANE WINDOWS REPLACEMENT IN THE CMR, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_akj_mexico_cmr_double_pane_windows_79k_2021",
    "MEX FAC DOUBLE PANE WINDOWS REPLACEMENT IN THE CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5321C0002_1900_-NONE-_-NONE-/",
    "Actor: SERVICIOS AKJ, S.A DE C.V — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1283",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19MX5321C0002_1900_-NONE-_-NONE- (akj_mexico_cmr_double_pane_windows_79k_2021). Signed 2021-04-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19MX5321C0002_1900_-NONE-_-NONE-/.",
    "USASpending: akj_mexico_cmr_double_pane_windows_79k_2021 USD 0.080m. Supports akj_mexico_cmr_double_pane_windows_79k_2021.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 79503.68; date_signed 2021-04-23.",
    investment_type="epc",
)

# === Cycle 1283 ===
row_doc(
    "misc_brazil_doors_replacement_72k_2020",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil doors replacement",
    "Brazil",
    "11 Aug 2020: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for doors replacement (PoP Brazil); obligated USD 72328.52. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "72328.52", "2020-08-11", "2020", "", "",
    "DOORS REPLACEMENT, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_doors_replacement_72k_2020",
    "DOORS REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9320P0437_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1283",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR9320P0437_1900_-NONE-_-NONE- (misc_brazil_doors_replacement_72k_2020). Signed 2020-08-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR9320P0437_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_doors_replacement_72k_2020 USD 0.072m. Supports misc_brazil_doors_replacement_72k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 72328.52; date_signed 2020-08-11.",
    investment_type="epc",
)

# === Cycle 1283 ===
row_doc(
    "misc_haiti_cmr_safe_haven_door_46k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Haiti CMR safe haven door replacement",
    "Haiti",
    "10 Jun 2022: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for safe haven door replacement at CMR (PoP Haiti); obligated USD 46753.20. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "46753.20", "2022-06-10", "2022", "", "",
    "SAFE HAVEN DOOR REPLACEMENT AT CMR, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_cmr_safe_haven_door_46k_2022",
    "SAFE HAVEN DOOR REPLACEMENT AT CMR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7022P0534_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1283",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19HA7022P0534_1900_-NONE-_-NONE- (misc_haiti_cmr_safe_haven_door_46k_2022). Signed 2022-06-10. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19HA7022P0534_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_cmr_safe_haven_door_46k_2022 USD 0.047m. Supports misc_haiti_cmr_safe_haven_door_46k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 46753.2; date_signed 2022-06-10.",
    investment_type="epc",
)

# === Cycle 1284 ===
row_doc(
    "kva_costa_rica_electrical_391k_2011",
    "energy", "power_plants_grid", "us",
    "KVA Electric — Costa Rica electrical work",
    "Costa Rica",
    "16 Sep 2011: Department of State awards contract to KVA ELECTRIC INC for electrical work Costa Rica (PoP Costa Rica); obligated USD 391789.90. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "391789.90", "2011-09-16", "2011", "", "",
    "ELECTRICAL WORK COSTA RICA, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_kva_costa_rica_electrical_391k_2011",
    "ELECTRICAL WORK COSTA RICA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11C0265_1900_-NONE-_-NONE-/",
    "Actor: KVA ELECTRIC INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1284",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11C0265_1900_-NONE-_-NONE- (kva_costa_rica_electrical_391k_2011). Signed 2011-09-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11C0265_1900_-NONE-_-NONE-/.",
    "USASpending: kva_costa_rica_electrical_391k_2011 USD 0.392m. Supports kva_costa_rica_electrical_391k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 391789.9; date_signed 2011-09-16.",
    investment_type="epc",
)

# === Cycle 1284 ===
row_doc(
    "greenway_costa_rica_pcc_design_build_280k_2011",
    "infrastructure", "building_materials", "us",
    "Greenway Enterprises — San José PCC design/build upgrade",
    "Costa Rica",
    "23 Mar 2011: Department of State awards contract to GREENWAY ENTERPRISES INC for design/build PCC upgrade in San Jose (PoP Costa Rica); obligated USD 280841. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "280841", "2011-03-23", "2011", "", "",
    "DESIGN/BUILD PCC UPGRADE IN SAN JOSE, COSTA RICA., Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_greenway_costa_rica_pcc_design_build_280k_2011",
    "DESIGN/BUILD PCC UPGRADE IN SAN JOSE, COSTA RICA.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F1030_1900_SAQMMA08D0011_1900/",
    "Actor: GREENWAY ENTERPRISES INC (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1284",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA11F1030_1900_SAQMMA08D0011_1900 (greenway_costa_rica_pcc_design_build_280k_2011). Signed 2011-03-23. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA11F1030_1900_SAQMMA08D0011_1900/.",
    "USASpending: greenway_costa_rica_pcc_design_build_280k_2011 USD 0.281m. Supports greenway_costa_rica_pcc_design_build_280k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 280841.0; date_signed 2011-03-23.",
    investment_type="epc",
)

# === Cycle 1284 ===
row_doc(
    "misc_mexico_calizas_windows_replacement_42k_2015",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Calizas 476 windows replacement",
    "Mexico",
    "27 Feb 2015: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC windows replacement Calizas 476 DAO (PoP Mexico); obligated USD 42478.67. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "42478.67", "2015-02-27", "2015", "", "",
    "MEX/FAC-7901-WINDOWS REPLACEMENT CALIZAS 476 DAO X4004URGENT IGF::OT::IGF, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_calizas_windows_replacement_42k_2015",
    "MEX/FAC-7901-WINDOWS REPLACEMENT CALIZAS 476 DAO X4004URGENT IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015M0607_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1284",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53015M0607_1900_-NONE-_-NONE- (misc_mexico_calizas_windows_replacement_42k_2015). Signed 2015-02-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53015M0607_1900_-NONE-_-NONE-/.",
    "USASpending: misc_mexico_calizas_windows_replacement_42k_2015 USD 0.042m. Supports misc_mexico_calizas_windows_replacement_42k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 42478.67; date_signed 2015-02-27.",
    investment_type="epc",
)

# === Cycle 1284 ===
row_doc(
    "misc_jamaica_door_replacement_34k_2026",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Jamaica FAC door replacement",
    "Jamaica",
    "15 Sep 2026: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC door replacement (PoP Jamaica); obligated USD 34276.73. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "34276.73", "2026-09-15", "2026", "", "",
    "FAC - DOOR REPLACEMENT, Jamaica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_jamaica_door_replacement_34k_2026",
    "FAC - DOOR REPLACEMENT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3726P1129_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1284",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3726P1129_1900_-NONE-_-NONE- (misc_jamaica_door_replacement_34k_2026). Signed 2026-09-15. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3726P1129_1900_-NONE-_-NONE-/.",
    "USASpending: misc_jamaica_door_replacement_34k_2026 USD 0.034m. Supports misc_jamaica_door_replacement_34k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 34276.73; date_signed 2026-09-15.",
    investment_type="epc",
)

# === Cycle 1284 ===
row_doc(
    "mathews_honduras_residential_generator_25k_2014",
    "energy", "power_plants_grid", "other",
    "Casa Comercial Mathews — Honduras residential generator purchase",
    "Honduras",
    "16 Apr 2014: Department of State awards contract to CASA COMERCIAL MATHEWS SA DE CV for TAT residential generator purchase (PoP Honduras); obligated USD 25800. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "25800", "2014-04-16", "2014", "", "",
    "TAT- RESIDENTIAL GENERATOR PURCHASE, Honduras (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_mathews_honduras_residential_generator_25k_2014",
    "TAT- RESIDENTIAL GENERATOR PURCHASE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80014M0513_1900_-NONE-_-NONE-/",
    "Actor: CASA COMERCIAL MATHEWS SA DE CV — other. Official USASpending Award API. Shuffle power_plants_grid.",
    "hunt_cycle1284",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SHO80014M0513_1900_-NONE-_-NONE- (mathews_honduras_residential_generator_25k_2014). Signed 2014-04-16. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SHO80014M0513_1900_-NONE-_-NONE-/.",
    "USASpending: mathews_honduras_residential_generator_25k_2014 USD 0.026m. Supports mathews_honduras_residential_generator_25k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 25800.0; date_signed 2014-04-16.",
    investment_type="equipment_supply",
)

# === Cycle 1285 ===
row_doc(
    "fdc_peru_sprinkler_upgrade_299k_2012",
    "infrastructure", "building_materials", "us",
    "Facilities Development Corporation — Peru sprinkler upgrade",
    "Peru",
    "31 Jul 2012: Department of State awards contract to FACILITIES DEVELOPMENT CORPORATION for sprinkler upgrade (PoP Peru); obligated USD 299937.30. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "299937.30", "2012-07-31", "2012", "", "",
    "SPRINKLER UPGRADE, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fdc_peru_sprinkler_upgrade_299k_2012",
    "SPRINKLER UPGRADE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2630_1900_SAQMMA08D0014_1900/",
    "Actor: FACILITIES DEVELOPMENT CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1285",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA12F2630_1900_SAQMMA08D0014_1900 (fdc_peru_sprinkler_upgrade_299k_2012). Signed 2012-07-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F2630_1900_SAQMMA08D0014_1900/.",
    "USASpending: fdc_peru_sprinkler_upgrade_299k_2012 USD 0.300m. Supports fdc_peru_sprinkler_upgrade_299k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 299937.3; date_signed 2012-07-31.",
    investment_type="epc",
)

# === Cycle 1285 ===
row_doc(
    "kva_mexico_city_electrical_329k_2010",
    "energy", "power_plants_grid", "us",
    "KVA Electric — Mexico City power systems electrical work",
    "Mexico",
    "8 Sep 2010: Department of State awards contract to KVA ELECTRIC INC for power systems Mexico City electrical work (PoP Mexico); obligated USD 329378.57. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "329378.57", "2010-09-08", "2010", "", "",
    "POWER SYSTEMS MEXICO CITY ELECTRICAL WORK, Mexico (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_kva_mexico_city_electrical_329k_2010",
    "POWER SYSTEMS MEXICO CITY ELECTRICAL WORK",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F3720_1900_SALMEC05D0011_1900/",
    "Actor: KVA ELECTRIC INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1285",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10F3720_1900_SALMEC05D0011_1900 (kva_mexico_city_electrical_329k_2010). Signed 2010-09-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F3720_1900_SALMEC05D0011_1900/.",
    "USASpending: kva_mexico_city_electrical_329k_2010 USD 0.329m. Supports kva_mexico_city_electrical_329k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 329378.57; date_signed 2010-09-08.",
    investment_type="epc",
)

# === Cycle 1285 ===
row_doc(
    "desarrollo_integral_colombia_cmr_guardhouse_44k_2025",
    "infrastructure", "building_materials", "other",
    "Desarrollo Integral Proyectos — Colombia CMR guardhouse windows and doors replacement",
    "Colombia",
    "17 Sep 2025: Department of State awards contract to DESARROLLO INTEGRAL PROYECTOS INGENIERIA LIMITADA for CMR guardhouse windows and doors replacement (PoP Colombia); obligated USD 44168.37. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "44168.37", "2025-09-17", "2025", "", "",
    "PR15621236: CMR GUARDHOUSE WINDOWS & DOORS REPLACEMENT 7942 XJ, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_desarrollo_integral_colombia_cmr_guardhouse_44k_2025",
    "PR15621236: CMR GUARDHOUSE WINDOWS & DOORS REPLACEMENT 7942 XJ",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02025C0013_1900_-NONE-_-NONE-/",
    "Actor: DESARROLLO INTEGRAL PROYECTOS INGENIERIA LIMITADA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1285",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19C02025C0013_1900_-NONE-_-NONE- (desarrollo_integral_colombia_cmr_guardhouse_44k_2025). Signed 2025-09-17. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19C02025C0013_1900_-NONE-_-NONE-/.",
    "USASpending: desarrollo_integral_colombia_cmr_guardhouse_44k_2025 USD 0.044m. Supports desarrollo_integral_colombia_cmr_guardhouse_44k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 44168.37; date_signed 2025-09-17.",
    investment_type="epc",
)

# === Cycle 1285 ===
row_doc(
    "misc_dominican_cmr_wooden_doors_20k_2026",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican CMR wooden doors replacement",
    "Dominican Republic",
    "27 Aug 2026: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC CMR wooden doors replacement (PoP Dominican Republic); obligated USD 20148.10. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "20148.10", "2026-08-27", "2026", "", "",
    "FAC CMR- WOODEN DOORS REPLACEMENT PID 3004 OBO 7903R - C, Dominican Republic (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_dominican_cmr_wooden_doors_20k_2026",
    "FAC CMR- WOODEN DOORS REPLACEMENT PID 3004 OBO 7903R - C",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8626C0065_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1285",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19DR8626C0065_1900_-NONE-_-NONE- (misc_dominican_cmr_wooden_doors_20k_2026). Signed 2026-08-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19DR8626C0065_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_cmr_wooden_doors_20k_2026 USD 0.020m. Supports misc_dominican_cmr_wooden_doors_20k_2026.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 20148.1; date_signed 2026-08-27.",
    investment_type="epc",
)

# === Cycle 1285 ===
row_doc(
    "fabio_garzon_colombia_scan_eagle_building_590k_2011",
    "infrastructure", "building_materials", "other",
    "Fabio Garzón Daza — Colombia Scan Eagle building",
    "Colombia",
    "28 Sep 2011: Department of Defense awards contract to FABIO GARZON DAZA for Scan Eagle building (PoP Colombia); obligated USD 590228.61. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "590228.61", "2011-09-28", "2011", "", "",
    "SCAN EAGLE BUILDING, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_fabio_garzon_colombia_scan_eagle_building_590k_2011",
    "SCAN EAGLE BUILDING",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0043_9700_-NONE-_-NONE-/",
    "Actor: FABIO GARZON DAZA — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1285",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11C0043_9700_-NONE-_-NONE- (fabio_garzon_colombia_scan_eagle_building_590k_2011). Signed 2011-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11C0043_9700_-NONE-_-NONE-/.",
    "USASpending: fabio_garzon_colombia_scan_eagle_building_590k_2011 USD 0.590m. Supports fabio_garzon_colombia_scan_eagle_building_590k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 590228.61; date_signed 2011-09-28.",
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
