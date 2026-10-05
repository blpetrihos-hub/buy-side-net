#!/usr/bin/env python3
"""Cycles 1317–1318: USASpending LatAm CapEx (Rapiscan/S2/Smiths NII + misc construction).

Seeds: 20262317–20262318. Thin top-up dry.
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

# === Cycle 1317 ===
row_doc(
    "rapiscan_peru_drive_through_inspection_6874k_2024",
    "infrastructure", "engineering_epc", "us",
    "Rapiscan Systems — Peru drive-through inspection system",
    "Peru",
    "8 Jul 2024: Department of State awards contract to RAPISCAN SYSTEMS INC for drive-through inspection system (delivery order); obligated USD 6874393.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "6874393.00", "2024-07-08", "2024", "", "",
    "NEW DELIVERY ORDER IN THE AMOUNT OF $6,499,413, Peru (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_rapiscan_peru_drive_through_inspection_6874k_2024",
    "NEW DELIVERY ORDER IN THE AMOUNT OF $6,499,413.00 FOR DRIVE-THROUGH INSPECTION SYSTEMS WITH A DELIVERY DATE OF 07/07/25 AND OPTION YEAR(S) THROUGH 7/07/28. THIS REQUIREMENT IS IN SUPPORT OF THE INL SECTION AT THE U.S. EMBASSY LIMA, PERU.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0042_1900_19AQMM21D0044_1900/",
    "Actor: RAPISCAN SYSTEMS INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1317",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_191NLE24F0042_1900_19AQMM21D0044_1900 (rapiscan_peru_drive_through_inspection_6874k_2024). Signed 2024-07-08. https://api.usaspending.gov/api/v2/awards/CONT_AWD_191NLE24F0042_1900_19AQMM21D0044_1900/.",
    "USASpending: rapiscan_peru_drive_through_inspection_6874k_2024 USD 6.874m. Supports rapiscan_peru_drive_through_inspection_6874k_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 6874393.0; date_signed 2024-07-08.",
    investment_type="equipment_supply",
)

# === Cycle 1317 ===
row_doc(
    "rapiscan_panama_centralized_monitoring_2840k_2022",
    "infrastructure", "engineering_epc", "us",
    "Rapiscan Systems — Panama centralized monitoring center",
    "Panama",
    "14 Sep 2022: Department of State awards contract to RAPISCAN SYSTEMS INC for Panama centralized monitoring center, training, installation, program management (CapEx face = award obligation); obligated USD 2840497.81. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "2840497.81", "2022-09-14", "2022", "", "",
    "PANAMA CENTRALIZED MONITORING CENTER, TRAINING, INSTALLATION, PROGRAM MANAGEMENT SUPPORT, AND EXTENDED WARRANTY PERIODS, Panama (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_rapiscan_panama_centralized_monitoring_2840k_2022",
    "PANAMA CENTRALIZED MONITORING CENTER, TRAINING, INSTALLATION, PROGRAM MANAGEMENT SUPPORT, AND EXTENDED WARRANTY PERIODS.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2788_1900_19AQMM21D0044_1900/",
    "Actor: RAPISCAN SYSTEMS INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1317",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22F2788_1900_19AQMM21D0044_1900 (rapiscan_panama_centralized_monitoring_2840k_2022). Signed 2022-09-14. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22F2788_1900_19AQMM21D0044_1900/.",
    "USASpending: rapiscan_panama_centralized_monitoring_2840k_2022 USD 2.840m. Supports rapiscan_panama_centralized_monitoring_2840k_2022.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 2840497.81; date_signed 2022-09-14.",
    investment_type="equipment_supply",
)

# === Cycle 1317 ===
row_doc(
    "misc_colombia_construction_224k_2010",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Colombia construction",
    "Colombia",
    "27 Sep 2010: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for construction (PoP Colombia); obligated USD 223876.42. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "223876.42", "2010-09-27", "2010", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_construction_224k_2010",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10C0043_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1317",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT10C0043_9700_-NONE-_-NONE- (misc_colombia_construction_224k_2010). Signed 2010-09-27. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT10C0043_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_construction_224k_2010 USD 0.224m. Supports misc_colombia_construction_224k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 223876.42; date_signed 2010-09-27.",
    investment_type="epc",
)

# === Cycle 1317 ===
row_doc(
    "misc_colombia_construction_223k_2011",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Colombia construction",
    "Colombia",
    "21 Jul 2011: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for construction (PoP Colombia); obligated USD 222953.17. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "222953.17", "2011-07-21", "2011", "", "",
    "CONSTRUCTION, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_construction_223k_2011",
    "CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0168_9700_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1317",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W913FT11P0168_9700_-NONE-_-NONE- (misc_colombia_construction_223k_2011). Signed 2011-07-21. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W913FT11P0168_9700_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_construction_223k_2011 USD 0.223m. Supports misc_colombia_construction_223k_2011.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 222953.17; date_signed 2011-07-21.",
    investment_type="epc",
)

# === Cycle 1317 ===
row_doc(
    "misc_colombia_recreational_area_227k_2010",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Colombia recreational area construction",
    "Colombia",
    "29 Sep 2010: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for construction of recreational area (multipurpose basketball and tennis courts); obligated USD 227215.36. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "227215.36", "2010-09-29", "2010", "", "",
    "CONSTRUCTION OF RECREATIONAL AREA (MULTIPURPOSE BASEKETBALL AND TENIS COURTS), Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_colombia_recreational_area_227k_2010",
    "CONSTRUCTION OF RECREATIONAL AREA (MULTIPURPOSE BASEKETBALL AND TENIS COURTS).",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20010C0018_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1317",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SCO20010C0018_1900_-NONE-_-NONE- (misc_colombia_recreational_area_227k_2010). Signed 2010-09-29. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SCO20010C0018_1900_-NONE-_-NONE-/.",
    "USASpending: misc_colombia_recreational_area_227k_2010 USD 0.227m. Supports misc_colombia_recreational_area_227k_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 227215.36; date_signed 2010-09-29.",
    investment_type="epc",
)

# === Cycle 1318 ===
row_doc(
    "s2_global_costarica_scanners_integration_225k_2025",
    "infrastructure", "engineering_epc", "us",
    "S2 Global — Costa Rica San Jose scanners integration",
    "Costa Rica",
    "30 Sep 2025: Department of State awards contract to S2 GLOBAL INC for INL San Jose B&P scanners integration; obligated USD 225000.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "225000.00", "2025-09-30", "2025", "", "",
    "1930, Costa Rica (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_s2_global_costarica_scanners_integration_225k_2025",
    "1930.0 INL SAN JOSE B&P SCANNERS INTEGRATION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8025P1102_1900_-NONE-_-NONE-/",
    "Actor: S2 GLOBAL INC (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1318",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19CS8025P1102_1900_-NONE-_-NONE- (s2_global_costarica_scanners_integration_225k_2025). Signed 2025-09-30. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19CS8025P1102_1900_-NONE-_-NONE-/.",
    "USASpending: s2_global_costarica_scanners_integration_225k_2025 USD 0.225m. Supports s2_global_costarica_scanners_integration_225k_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 225000.0; date_signed 2025-09-30.",
    investment_type="equipment_supply",
)

# === Cycle 1318 ===
row_doc(
    "smiths_bolivia_el_alto_xray_163k_2013",
    "infrastructure", "engineering_epc", "us",
    "Smiths Detection — Bolivia El Alto airport x-ray machine",
    "Bolivia",
    "5 Dec 2012: Department of State awards contract to SMITHS DETECTION INC. for NAS-FELCN x-ray machine to be installed at El Alto airport; obligated USD 162600.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "162600.00", "2012-12-05", "2012", "", "",
    "NAS-FELCN X-RAY MACHINE TO BE INTALLED AT EL ALTO AIRPORT, Bolivia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_smiths_bolivia_el_alto_xray_163k_2013",
    "NAS-FELCN X-RAY MACHINE TO BE INTALLED AT EL ALTO AIRPORT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40013M0119_1900_-NONE-_-NONE-/",
    "Actor: SMITHS DETECTION INC. (U.S.) — us. Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle1318",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SBL40013M0119_1900_-NONE-_-NONE- (smiths_bolivia_el_alto_xray_163k_2013). Signed 2012-12-05. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SBL40013M0119_1900_-NONE-_-NONE-/.",
    "USASpending: smiths_bolivia_el_alto_xray_163k_2013 USD 0.163m. Supports smiths_bolivia_el_alto_xray_163k_2013.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 162600.0; date_signed 2012-12-05.",
    investment_type="equipment_supply",
)

# === Cycle 1318 ===
row_doc(
    "misc_haiti_marine_engineering_construction_220k_2014",
    "infrastructure", "port_ownership", "other",
    "Miscellaneous foreign awardees — Haiti marine engineering and construction services",
    "Haiti",
    "28 Sep 2014: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for marine engineering and construction services (Haiti) for INL; obligated USD 219674.00. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "219674.00", "2014-09-28", "2014", "", "",
    "MARINE ENGINEERING AND CONSTRUCTION SERVICES (HAITI) FOR INL, Haiti (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_haiti_marine_engineering_construction_220k_2014",
    "MARINE ENGINEERING AND CONSTRUCTION SERVICES (HAITI) FOR INL. IGF::OT::IGF",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14M1595_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle port_ownership.",
    "hunt_cycle1318",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA14M1595_1900_-NONE-_-NONE- (misc_haiti_marine_engineering_construction_220k_2014). Signed 2014-09-28. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14M1595_1900_-NONE-_-NONE-/.",
    "USASpending: misc_haiti_marine_engineering_construction_220k_2014 USD 0.220m. Supports misc_haiti_marine_engineering_construction_220k_2014.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 219674.0; date_signed 2014-09-28.",
    investment_type="epc",
)

# === Cycle 1318 ===
row_doc(
    "misc_brazil_cmr_landscaping_construction_234k_2020",
    "infrastructure", "engineering_epc", "other",
    "Miscellaneous foreign awardees — Brazil CMR landscaping construction",
    "Brazil",
    "12 Aug 2020: Department of State awards contract to MISCELLANEOUS FOREIGN AWARDEES for FAC-BSB CMR landscaping construction; obligated USD 234455.34. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "234455.34", "2020-08-12", "2020", "", "",
    "FAC-BSB  CMR LANDSCAPING CONSTRUCTION, Brazil (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_misc_brazil_cmr_landscaping_construction_234k_2020",
    "FAC-BSB  CMR LANDSCAPING CONSTRUCTION",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0644_1900_-NONE-_-NONE-/",
    "Actor: miscellaneous foreign awardees (redacted) — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1318",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19BR2520P0644_1900_-NONE-_-NONE- (misc_brazil_cmr_landscaping_construction_234k_2020). Signed 2020-08-12. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19BR2520P0644_1900_-NONE-_-NONE-/.",
    "USASpending: misc_brazil_cmr_landscaping_construction_234k_2020 USD 0.234m. Supports misc_brazil_cmr_landscaping_construction_234k_2020.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 234455.34; date_signed 2020-08-12.",
    investment_type="epc",
)

# === Cycle 1318 ===
row_doc(
    "marago_colombia_tumaco_observation_towers_123k_2015",
    "infrastructure", "engineering_epc", "other",
    "Constructora Marago — Colombia Tumaco observation towers",
    "Colombia",
    "24 Sep 2015: Department of State awards contract to CONSTRUCTORA MARAGO S A S for construction of observation towers — Tumaco Colombia; obligated USD 122995.94. CapEx face = award obligation. Exact site coords not stated — lat/lon blank.",
    "122995.94", "2015-09-24", "2015", "", "",
    "IGF::OT::IGF CONSTRUCTION OF OBSERVATION TOWERS - TUMACO COLOMBIA, Colombia (USASpending description; site/city named where present, coords not stated — lat/lon blank).",
    "usaspending_marago_colombia_tumaco_observation_towers_123k_2015",
    "IGF::OT::IGF CONSTRUCTION OF OBSERVATION TOWERS - TUMACO COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL15C0005_9700_-NONE-_-NONE-/",
    "Actor: CONSTRUCTORA MARAGO S A S — other. Official USASpending Award API. Shuffle engineering_epc.",
    "hunt_cycle1318",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912CL15C0005_9700_-NONE-_-NONE- (marago_colombia_tumaco_observation_towers_123k_2015). Signed 2015-09-24. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912CL15C0005_9700_-NONE-_-NONE-/.",
    "USASpending: marago_colombia_tumaco_observation_towers_123k_2015 USD 0.123m. Supports marago_colombia_tumaco_observation_towers_123k_2015.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 122995.94; date_signed 2015-09-24.",
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
