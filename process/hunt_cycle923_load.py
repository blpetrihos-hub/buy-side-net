#!/usr/bin/env python3
"""Cycle 923: USASpending Andean/Southern Cone CapEx (Colombia/Peru/Ecuador/Paraguay/Uruguay).

Seed: 20261923. Thin top-up dry.
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


row_doc(
    "desbuild_bogota_consular_11p9m_2023",
    "infrastructure", "engineering_epc", "us",
    "Desbuild Incorporated — Embassy Bogotá consular affairs selective improvements renovation",
    "Colombia",
    "25 Aug 2023: Department of State awards task order 19AQMM23F2205 to Desbuild Incorporated for "
    "Consular Affairs selective improvements renovation at U.S. Embassy Bogotá, Colombia; "
    "obligated USD 11,886,136.00. CapEx face = award obligation. Distinct from cce_bogota_annex_2005.",
    "11886136.00", "2023-08-25", "2023", "4.711", "-74.072",
    "U.S. Embassy Bogotá consular renovation, Colombia (USASpending PoP Colombia).",
    "usaspending_desbuild_bogota_consular_20230825",
    "CONSULAR AFFAIRS SELECTIVE IMPROVEMENTS RENOVATION AT US EMBASSY BOGOTA, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2205_1900_19AQMM22D0073_1900/",
    "Actor: Desbuild Incorporated (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle923",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM23F2205_1900_19AQMM22D0073_1900 (Desbuild; Bogotá consular). Signed 25 August "
    "2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM23F2205_1900_19AQMM22D0073_1900/.",
    "USASpending: Desbuild Bogotá consular USD 11.886m. Supports desbuild_bogota_consular_11p9m_2023.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 11,886,136.00; date_signed 2023-08-25.",
)
row_doc(
    "kgn_callao_navy_infra_22p2m_2025",
    "infrastructure", "port_ownership", "us",
    "KGN Support Services LLC — Peruvian Navy Callao base infrastructure design-build",
    "Peru",
    "17 Jun 2025: USACE awards contract W9127825C0021 to KGN Support Services LLC for design-build "
    "construction of Peruvian Navy infrastructure construction requirements on Callao Navy Base, "
    "Lima, Peru; obligated USD 22,189,297.00. CapEx face = award obligation.",
    "22189297.00", "2025-06-17", "2025", "-12.050", "-77.140",
    "Callao Navy Base infrastructure, Lima, Peru (USASpending PoP Peru; Callao pin).",
    "usaspending_kgn_callao_navy_20250617",
    "DESIGN BUILD CONSTRUCTION \"C\" STANDALONE CONTRACT FOR PERUVIAN NAVY INFRASTRUCTURE "
    "CONSTRUCTION REQUIREMENTS ON CALLAO NAVY BASE, LIMA, PERU.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825C0021_9700_-NONE-_-NONE-/",
    "Actor: KGN Support Services LLC (U.S.) under USACE — us. Official USASpending Award API. "
    "Shuffle port_ownership (navy base/port complex); ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle923",
    "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9127825C0021_9700_-NONE-_-NONE- "
    "(KGN; Callao Navy infrastructure). Signed 17 June 2025. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9127825C0021_9700_-NONE-_-NONE-/.",
    "USASpending: KGN Callao Navy USD 22.189m. Supports kgn_callao_navy_infra_22p2m_2025.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 22,189,297.00; date_signed 2025-06-17.",
)
row_doc(
    "machado_silvetti_bogota_design_5p01m_2024",
    "infrastructure", "engineering_epc", "us",
    "Machado and Silvetti Associates, Inc. — project development and design Bogotá",
    "Colombia",
    "17 Jul 2024: Department of State awards task order 19AQMM24F1347 to Machado and Silvetti "
    "Associates, Inc. for project development and design services in Bogotá, Colombia; obligated "
    "USD 5,008,513.63. CapEx face = award obligation. Distinct from "
    "desbuild_bogota_consular_11p9m_2023.",
    "5008513.63", "2024-07-17", "2024", "4.711", "-74.072",
    "U.S. facilities design services, Bogotá, Colombia (USASpending PoP Colombia).",
    "usaspending_machado_bogota_design_20240717",
    "PROJECT DEVELOPMENT AND DESIGN SERVICES IN BOGOTA, COLOMBIA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F1347_1900_19AQMM20D0032_1900/",
    "Actor: Machado and Silvetti Associates, Inc. (U.S.) under State — us. Official USASpending "
    "Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle923",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_19AQMM24F1347_1900_19AQMM20D0032_1900 (Machado & Silvetti; Bogotá design). Signed 17 "
    "July 2024. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM24F1347_1900_19AQMM20D0032_1900/.",
    "USASpending: Machado Bogotá design USD 5.009m. Supports machado_silvetti_bogota_design_5p01m_2024.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 5,008,513.63; date_signed 2024-07-17.",
)
row_doc(
    "falcon_asuncion_electrical_1p60m_2010",
    "energy", "power_plants_grid", "us",
    "Falcon Spectrum JV LLC — chancery electrical upgrade Asunción",
    "Paraguay",
    "29 Sep 2010: Department of State awards task order SAQMMA10F5003 to Falcon Spectrum Joint "
    "Venture, LLC for electrical upgrade of chancery building in Asunción, Paraguay; obligated "
    "USD 1,600,000.00. CapEx face = award obligation. Distinct from caddell_asuncion_nec_2017.",
    "1600000.00", "2010-09-29", "2010", "-25.286", "-57.647",
    "Chancery electrical upgrade, Asunción, Paraguay (USASpending PoP Paraguay).",
    "usaspending_falcon_asuncion_electrical_20100929",
    "ELECTRICAL UPGRADE OF CHAUNCERY BLDG IN ASUNCION, PARAGUAY",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F5003_1900_SAQMMA08D0016_1900/",
    "Actor: Falcon Spectrum JV LLC (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle923",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA10F5003_1900_SAQMMA08D0016_1900 (Falcon Spectrum; Asunción electrical). Signed "
    "29 September 2010. "
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10F5003_1900_SAQMMA08D0016_1900/.",
    "USASpending: Falcon Asunción electrical USD 1.600m. Supports falcon_asuncion_electrical_1p60m_2010.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,600,000.00; date_signed 2010-09-29.",
)
row_doc(
    "oes_quito_fe_br_1p27m_2012",
    "infrastructure", "building_materials", "us",
    "O.E.S., Inc. — Embassy Quito Phase III/IV FE/BR repair and replacement",
    "Ecuador",
    "13 Sep 2012: Department of State awards task order SAQMMA12F3751 to O.E.S., Inc. for U.S. "
    "Embassy Quito, Ecuador Phase III/IV FE/BR repair and replacement project; obligated USD "
    "1,274,362.38. CapEx face = award obligation.",
    "1274362.38", "2012-09-13", "2012", "-0.180", "-78.468",
    "U.S. Embassy Quito FE/BR repair/replacement, Ecuador (USASpending PoP Ecuador).",
    "usaspending_oes_quito_fe_br_20120913",
    "U.S. EMBASSY QUITO, ECUADOR PHASE III/IV FE/BR REPAIR AND REPLACEMENT PROJECT",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F3751_1900_SAQMMA07D0009_1900/",
    "Actor: O.E.S., Inc. (U.S.) under State — us. Official USASpending Award API. Shuffle "
    "building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle923",
    "U.S. Department of the Treasury, USAspending.gov. Award "
    "CONT_AWD_SAQMMA12F3751_1900_SAQMMA07D0009_1900 (O.E.S.; Quito FE/BR). Signed 13 September "
    "2012. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F3751_1900_SAQMMA07D0009_1900/.",
    "USASpending: O.E.S. Quito FE/BR USD 1.274m. Supports oes_quito_fe_br_1p27m_2012.",
    "Opened USASpending Award API 2026-10-05; total_obligation USD 1,274,362.38; date_signed 2012-09-13.",
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
    print(f"cycle923 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
