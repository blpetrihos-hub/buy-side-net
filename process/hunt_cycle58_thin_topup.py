#!/usr/bin/env python3
"""Cycle 58 thin_topup: 3 thinnest after equal pass.

Post-equal thinnest (active+hunt, evidence documented|proxy|hunt):
niobium 22, balsa 22, nickel/graphite/fission_smr 23 → top-up niobium, balsa, nickel.
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


# ---------------------------------------------------------------------------
# thin 1 resources/niobium — St George CEFET-MG Araxá pilot plant under construction
# ---------------------------------------------------------------------------
A(
    {
        "id": "st_george_cefet_pilot_plant_2026",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "St George Mining / CEFET-MG — Araxá Technological Centre pilot plant",
        "country": "Brazil",
        "asset": "2 Sep 2026 ASX: St George + CEFET-MG collaborate on large-scale pilot plant at CEFET Araxá campus (St George Technological Centre); throughput up to 300 kg/h for niobium flotation + rare-earth products (concentrate/MREC/oxides); environmental and building permits received; construction commenced; completion targeted Dec 2026, first ops Jan 2027; managed with Worley. Parallel CIT-SENAI Belo Horizonte ~9 t saprolite pilot flotation underway. Distinct from st_george_araxa_mre_upgrade_nb_2026, st_george_araxa_raise_aud60m_2026, worley_st_george_araxa_2026.",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "CEFET-MG Araxá campus / St George Technological Centre (city of Araxá, Minas Gerais).",
        "evidence": "documented",
        "source_id": "stgeorge_pilot_plant_asx_20260902",
        "note": "Actor: St George Mining (Australia) — allied. Company ASX primary; pilot CapEx USD not disclosed.",
    },
    {
        "id": "st_george_cefet_pilot_plant_2026",
        "retrieved": "2026-10-01",
        "source_id": "stgeorge_pilot_plant_asx_20260902",
        "url": "https://www.stgm.com.au/pdf/c83fbdbe-842d-47e2-9b84-835b63973c17/Platform/ListPage/Pilot-Plant-Test-Work-at-Araxa-Project.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "St George’s pilot plant is advancing with required environmental and building permits received and construction commenced… St George and CEFET… are collaborating on the construction of a new large-scale pilot plant… throughput capacity of up to 300 kg/hour… including niobium flotation… Construction of the St George Technological Centre has commenced, with expected completion in December 2026 and first operation of the pilot plant in January 2027.",
        "note": "Opened St George ASX release PDF 2 Sep 2026 (company mirror).",
    },
    {
        "id": "stgeorge_pilot_plant_asx_20260902",
        "type": "company",
        "chicago": "St George Mining Limited. “Pilot Plant Beneficiation Test Work at Araxá Project, Brazil.” ASX announcement, 2 September 2026.",
        "url": "https://www.stgm.com.au/pdf/c83fbdbe-842d-47e2-9b84-835b63973c17/Platform/ListPage/Pilot-Plant-Test-Work-at-Araxa-Project.pdf",
        "annotation": "ASX primary on CEFET-MG Araxá pilot plant construction commenced and CIT-SENAI study. Supports st_george_cefet_pilot_plant_2026.",
        "supports": ["st_george_cefet_pilot_plant_2026", "hunt_fenb_araxa"],
    },
)

# ---------------------------------------------------------------------------
# thin 2 resources/balsa — Plantabal → Baltek Inc. U.S. core-sheet shipment Sep 2026
# ---------------------------------------------------------------------------
A(
    {
        "id": "plantabal_baltek_us_coresheets_202609",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "us",
        "counterpart": "Plantabal (3A) — Baltek Inc. U.S. import of kiln-dried balsa core sheets",
        "country": "Ecuador",
        "asset": "ImportInfo U.S. customs mirror: Plantaciones de Balsa Plantabal S.A. (Samborondón/Quevedo, Ecuador) shipper to Baltek Inc. (Colfax, NC) — multiple Sep 2026 arrivals; e.g. house BOL WBLCGYE202676 / master HLCUGY3260830256, vessel Haiphong Express, arrival Newark NJ 29 Sep 2026, 36 PKG / 8,966 kg commodity “BALSA CORE SHEETS KILN DRIED AND GLUED UP”. Named Plantabal→U.S. Baltek offtake shipment (affiliate of 3A/BALTEK chain). Distinct from aggregate AIMA 2025 manufactures-share and WITS HS 440723 annual rows.",
        "investment_type": "offtake",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Plantabal Quevedo / Guayas–Los Ríos processing belt (export origin); U.S. consignee Colfax NC not mapped.",
        "evidence": "documented",
        "source_id": "importinfo_plantabal_baltek_202609",
        "note": "Actor: U.S. consignee Baltek Inc. (3A/BALTEK U.S.) — us. Customs mirror documents named shipper/consignee/commodity/weight; commercial invoice USD not on page.",
    },
    {
        "id": "plantabal_baltek_us_coresheets_202609",
        "retrieved": "2026-10-01",
        "source_id": "importinfo_plantabal_baltek_202609",
        "url": "https://www.importinfo.com/plantaciones-de-balsa-plantabal-s-a",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "PLANTACIONES DE BALSA PLANTABAL S.A … BALTEK INC … BALSA CORE SHEETS KILN DRIED AND GLUED UP AND ENCOLADA … Arrival Date 2026-09-29 … NEWARK, NEW JERSEY … 36 PKG … 8,966 KG … House BOL WBLCGYE202676",
        "note": "Opened ImportInfo U.S. import activity page listing Sep 2026 Plantabal→Baltek bills of lading.",
    },
    {
        "id": "importinfo_plantabal_baltek_202609",
        "type": "government",
        "chicago": "ImportInfo. “Plantaciones De Balsa Plantabal S.A | U.S. Import Activity.” Accessed 1 October 2026.",
        "url": "https://www.importinfo.com/plantaciones-de-balsa-plantabal-s-a",
        "annotation": "U.S. customs mirror of Plantabal→Baltek Inc. Sep 2026 balsa core-sheet shipments. Supports plantabal_baltek_us_coresheets_202609.",
        "supports": ["plantabal_baltek_us_coresheets_202609", "hunt_res_balsa"],
    },
)

# ---------------------------------------------------------------------------
# thin 3 resources/nickel — miss (documented in hunt note only; no new row)
# No ITEMS for nickel: Jervois SMP / MMG Anglo Ni Brazil / Centaurus Glencore /
# DFC Piauí / Brazilian Nickel stack already logged; no distinct new named deal opened.
# ---------------------------------------------------------------------------


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None and k != "supports":
                existing[k] = v
        supports = list(
            dict.fromkeys((existing.get("supports") or []) + (bib_entry.get("supports") or []))
        )
        existing["supports"] = supports
    else:
        bib.append(bib_entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
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
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_entry)

    # nickel thin miss note on hunt seed
    if "hunt_res_nickel" in by_id:
        rows[by_id["hunt_res_nickel"]]["note"] = (
            (rows[by_id["hunt_res_nickel"]].get("note") or "")
            + " Cycle 58 thin_topup: nickel half-budget — Jervois SMP / MMG Anglo Ni / Centaurus Glencore / DFC Piauí already (miss)."
        ).strip()
    if "hunt_fenb_araxa" in by_id:
        rows[by_id["hunt_fenb_araxa"]]["note"] = (
            (rows[by_id["hunt_fenb_araxa"]].get("note") or "")
            + " Cycle 58 thin_topup: logged st_george_cefet_pilot_plant_2026."
        ).strip()
    if "hunt_res_balsa" in by_id:
        rows[by_id["hunt_res_balsa"]]["note"] = (
            (rows[by_id["hunt_res_balsa"]].get("note") or "")
            + " Cycle 58 thin_topup: logged plantabal_baltek_us_coresheets_202609 (U.S.)."
        ).strip()

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print("Cycle 58 thin_topup rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
