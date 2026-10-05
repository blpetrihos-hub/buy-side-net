#!/usr/bin/env python3
"""Cycles 1254–1255: USASpending LatAm CapEx (US scraps + residual other).

Seeds: 20262254–20262255. Thin top-up dry. US CapEx stock near exhaustion.
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

# === Cycle 1254 ===
row_doc(
    "daikin_jamaica_fac_evaporators_30k_2025",
    "energy", "power_plants_grid", "us",
    "Daikin Applied Americas — Jamaica FAC evaporators",
    "Jamaica",
    "2 Jun 2025: Department of State awards contract to DAIKIN APPLIED AMERICAS INC for FAC evaporators (PoP Jamaica); obligated USD 29596. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "29596", "2025-06-02", "2025", "", "",
    "FAC - EVAPORATORS, Jamaica (USASpending description; site not named — lat/lon blank).",
    "usaspending_daikin_jamaica_fac_evaporators_30k_2025",
    "FAC - EVAPORATORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3725P0677_1900_-NONE-_-NONE-/",
    "Actor: DAIKIN APPLIED AMERICAS INC (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1254",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19JM3725P0677_1900_-NONE-_-NONE- (daikin_jamaica_fac_evaporators_30k_2025). Signed 2025-06-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19JM3725P0677_1900_-NONE-_-NONE-/.",
    "USASpending: daikin_jamaica_fac_evaporators_30k_2025 USD 0.030m. Supports daikin_jamaica_fac_evaporators_30k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 29596.0; date_signed 2025-06-02.",
)

# === Cycle 1254 ===
row_doc(
    "inside_air_bahamas_chancery_chiller_replacement_10k_2011",
    "energy", "power_plants_grid", "us",
    "Inside Air Investment Group — Bahamas chancery rooftop chiller replacement",
    "Bahamas",
    "30 Sep 2011: Department of State awards contract to INSIDE AIR INVESTMENT GROUP, INC. for chancery rooftop chiller replacement 25 ton compressor (PoP Bahamas); obligated USD 9513. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "9513", "2011-09-30", "2011", "", "",
    "C-CHANCERY ROOFTOP CHILLER REPLACEMENT 25 TON COMPRESSORS, Bahamas (USASpending description; site not named — lat/lon blank).",
    "usaspending_inside_air_bahamas_chancery_chiller_replacement_10k_2011",
    "C-CHANCERY ROOFTOP CHILLER REPLACEMENT 25 TON COMPRESSORS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50011M0886_1900_-NONE-_-NONE-/",
    "Actor: INSIDE AIR INVESTMENT GROUP (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1254",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBF50011M0886_1900_-NONE-_-NONE- (inside_air_bahamas_chancery_chiller_replacement_10k_2011). Signed 2011-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBF50011M0886_1900_-NONE-_-NONE-/.",
    "USASpending: inside_air_bahamas_chancery_chiller_replacement_10k_2011 USD 0.010m. Supports inside_air_bahamas_chancery_chiller_replacement_10k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 9513.0; date_signed 2011-09-30.",
)

# === Cycle 1254 ===
row_doc(
    "misc_mexico_tres_canadas_make_ready_38k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Mexico Tres Canadas I-03 make-ready",
    "Mexico",
    "1 Feb 2012: Department of State awards contract for MX-FAC 7901 Tres Canadas I-03 make ready (PoP Mexico); obligated USD 38025.58. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "38025.58", "2012-02-01", "2012", "", "",
    "MX-FAC 7901 TRES CANADAS I-03 MAKE READY, Mexico (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_mexico_tres_canadas_make_ready_38k_2012",
    "MX-FAC 7901 TRES CANADAS I-03 MAKE READY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012L0007_1900_SMX53012A0011_1900/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1254",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SMX53012L0007_1900_SMX53012A0011_1900 (misc_mexico_tres_canadas_make_ready_38k_2012). Signed 2012-02-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SMX53012L0007_1900_SMX53012A0011_1900/.",
    "USASpending: misc_mexico_tres_canadas_make_ready_38k_2012 USD 0.038m. Supports misc_mexico_tres_canadas_make_ready_38k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 38025.58; date_signed 2012-02-01.",
)

# === Cycle 1254 ===
row_doc(
    "misc_dominican_usaid_director_glq_make_ready_37k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic USAID director GLQ make-ready works",
    "Dominican Republic",
    "29 Jun 2012: Department of State awards contract for USAID director GLQ make-ready works (PoP Dominican Republic); obligated USD 36829.48. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "36829.48", "2012-06-29", "2012", "", "",
    "USAID - DIRCTR.'S GLQ MAKE READY WORKS, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_dominican_usaid_director_glq_make_ready_37k_2012",
    "USAID - DIRCTR.'S GLQ MAKE READY WORKS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86012M1333_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1254",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86012M1333_1900_-NONE-_-NONE- (misc_dominican_usaid_director_glq_make_ready_37k_2012). Signed 2012-06-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86012M1333_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_usaid_director_glq_make_ready_37k_2012 USD 0.037m. Supports misc_dominican_usaid_director_glq_make_ready_37k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 36829.48; date_signed 2012-06-29.",
)

# === Cycle 1254 ===
row_doc(
    "misc_brazil_msgq_rui_barbosa_make_ready_36k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil FM make-ready MSGQ Rui Barbosa 870/701",
    "Brazil",
    "1 Dec 2011: Department of State awards contract for FM make-ready MSGQ Rui Barbosa 870/701 (PoP Brazil); obligated USD 36304.59. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "36304.59", "2011-12-01", "2011", "", "",
    "FM- MAKE READY MSGQ RUI BARBOSSA 870/701, Brazil (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_msgq_rui_barbosa_make_ready_36k_2012",
    "FM- MAKE READY MSGQ RUI BARBOSSA 870/701",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82012M0146_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1254",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBR82012M0146_1900_-NONE-_-NONE- (misc_brazil_msgq_rui_barbosa_make_ready_36k_2012). Signed 2011-12-01. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBR82012M0146_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_msgq_rui_barbosa_make_ready_36k_2012 USD 0.036m. Supports misc_brazil_msgq_rui_barbosa_make_ready_36k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 36304.59; date_signed 2011-12-01.",
)

# === Cycle 1255 ===
row_doc(
    "york_panama_cooling_towers_vsd_7k_2014",
    "energy", "power_plants_grid", "us",
    "York International — Panama NEC variable speed drive for 2 cooling towers",
    "Panama",
    "31 Jan 2014: Department of State awards contract to YORK INTERNATIONAL CORPORATION for variable speed drive for 2 cooling towers — NEC (PoP Panama); obligated USD 6575. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "6575", "2014-01-31", "2014", "", "",
    "VARIABLE SPEED DRIVE FOR 2 COOLING TOWERS-NEC, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_york_panama_cooling_towers_vsd_7k_2014",
    "VARIABLE SPEED DRIVE FOR 2 COOLING TOWERS-NEC",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014M0151_1900_-NONE-_-NONE-/",
    "Actor: YORK INTERNATIONAL CORPORATION (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1255",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07014M0151_1900_-NONE-_-NONE- (york_panama_cooling_towers_vsd_7k_2014). Signed 2014-01-31. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07014M0151_1900_-NONE-_-NONE-/.",
    "USASpending: york_panama_cooling_towers_vsd_7k_2014 USD 0.007m. Supports york_panama_cooling_towers_vsd_7k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6575.0; date_signed 2014-01-31.",
)

# === Cycle 1255 ===
row_doc(
    "johnson_controls_panama_cooling_tower_vsd_7k_2011",
    "energy", "power_plants_grid", "us",
    "Johnson Controls — Panama NEC variable speed drive for cooling tower",
    "Panama",
    "11 Aug 2011: Department of State awards contract to JOHNSON CONTROLS, INC. for variable speed drive for cooling tower — NEC (PoP Panama); obligated USD 6843. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "6843", "2011-08-11", "2011", "", "",
    "VARIABLE SPEED DRIVE FOR COOLING TOWER - NEC -7901, Panama (USASpending description; site not named — lat/lon blank).",
    "usaspending_johnson_controls_panama_cooling_tower_vsd_7k_2011",
    "VARIABLE SPEED DRIVE FOR COOLING TOWER - NEC -7901",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07011M0480_1900_-NONE-_-NONE-/",
    "Actor: JOHNSON CONTROLS (U.S.) — us. Official USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1255",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SPM07011M0480_1900_-NONE-_-NONE- (johnson_controls_panama_cooling_tower_vsd_7k_2011). Signed 2011-08-11. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SPM07011M0480_1900_-NONE-_-NONE-/.",
    "USASpending: johnson_controls_panama_cooling_tower_vsd_7k_2011 USD 0.007m. Supports johnson_controls_panama_cooling_tower_vsd_7k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6843.0; date_signed 2011-08-11.",
)

# === Cycle 1255 ===
row_doc(
    "misc_dominican_dcm_make_ready_35k_2012",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Dominican Republic PROG DCM make-ready work paid by LLD",
    "Dominican Republic",
    "29 Jun 2012: Department of State awards contract for PROG-DCM make-ready work paid by LLD (PoP Dominican Republic); obligated USD 34842.67. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "34842.67", "2012-06-29", "2012", "", "",
    "PROG- DCM MAKE READY WORK PAID BY LLD, Dominican Republic (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_dominican_dcm_make_ready_35k_2012",
    "PROG- DCM MAKE READY WORK PAID BY LLD",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86012M1337_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1255",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SDR86012M1337_1900_-NONE-_-NONE- (misc_dominican_dcm_make_ready_35k_2012). Signed 2012-06-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SDR86012M1337_1900_-NONE-_-NONE-/.",
    "USASpending: misc_dominican_dcm_make_ready_35k_2012 USD 0.035m. Supports misc_dominican_dcm_make_ready_35k_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 34842.67; date_signed 2012-06-29.",
)

# === Cycle 1255 ===
row_doc(
    "misc_argentina_estrada_make_ready_31k_2014",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Argentina FM make-ready 2014 works at GOP Estrada 2475",
    "Argentina",
    "14 Jul 2014: Department of State awards contract for FM make-ready 2014 works at GOP Estrada 2475 (PoP Argentina); obligated USD 31418.92. CapEx face = award obligation. Site/city named; site coords not stated — lat/lon blank.",
    "31418.92", "2014-07-14", "2014", "", "",
    "FM - MAKE READY 2014 WORKS AT GOP ESTRADA 2475 IGF::OT::IGF, Argentina (USASpending description; site/city named, coords not stated — lat/lon blank).",
    "usaspending_misc_argentina_estrada_make_ready_31k_2014",
    "FM - MAKE READY 2014 WORKS AT GOP ESTRADA 2475 IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20014M0410_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1255",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAR20014M0410_1900_-NONE-_-NONE- (misc_argentina_estrada_make_ready_31k_2014). Signed 2014-07-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAR20014M0410_1900_-NONE-_-NONE-/.",
    "USASpending: misc_argentina_estrada_make_ready_31k_2014 USD 0.031m. Supports misc_argentina_estrada_make_ready_31k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 31418.92; date_signed 2014-07-14.",
)

# === Cycle 1255 ===
row_doc(
    "misc_brazil_make_ready_bar_grills_29k_2022",
    "infrastructure", "building_materials", "other",
    "Miscellaneous foreign awardees — Brazil make-ready bar grills",
    "Brazil",
    "2 Jun 2022: Department of State awards contract for make-ready bar grills (PoP Brazil); obligated USD 28860.83. CapEx face = award obligation. Exact site unnamed — lat/lon blank.",
    "28860.83", "2022-06-02", "2022", "", "",
    "MAKE READY BAR GRILLS, Brazil (USASpending description; site not named — lat/lon blank).",
    "usaspending_misc_brazil_make_ready_bar_grills_29k_2022",
    "MAKE READY BAR GRILLS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8222P0225_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle building_materials.",
    "hunt_cycle1255",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR8222P0225_1900_-NONE-_-NONE- (misc_brazil_make_ready_bar_grills_29k_2022). Signed 2022-06-02. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR8222P0225_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_make_ready_bar_grills_29k_2022 USD 0.029m. Supports misc_brazil_make_ready_bar_grills_29k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 28860.83; date_signed 2022-06-02.",
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
