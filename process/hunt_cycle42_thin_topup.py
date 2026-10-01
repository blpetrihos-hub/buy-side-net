#!/usr/bin/env python3
"""Cycle 42 thin_topup: balsa / graphite / fission_smr (fewest post-pass).

Hit: WITS Ecuador HS 440723 2025 China vs United States trade pair (PRC–U.S.).
Miss: graphite, fission_smr (and niobium in same window).
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


# WITS values are Trade Value 1000USD → multiply by 1000
# China 144,828.45 → 144828450; United States 4,699.55 → 4699550
CHINA = 144828450
US = 4699550
GAP = abs(US - CHINA) / CHINA

A(
    {
        "id": "wits_ecuador_balsa_china_2025",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "prc",
        "counterpart": "China — Ecuador HS 440723 sawn balsa/related wood imports (WITS/Comtrade)",
        "country": "Ecuador",
        "asset": "Ecuador 2025 exports of HS 440723 to China — USD 144.828 million (WITS); quantity 483,750 m³",
        "investment_type": "other",
        "value": str(CHINA),
        "currency": "USD",
        "value_usd": str(CHINA),
        "fx_usd": "1",
        "fx_date": "2025-12-31",
        "year": "2025",
        "status": "active",
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Quevedo / Guayas–Los Ríos balsa processing belt (export-origin proxy; not a single mill pin).",
        "evidence": "paired",
        "source_id": "wits_ecu_440723_2025",
        "note": "Trade flow. WITS/Comtrade Ecuador HS 440723 to China 2025. Paired same-year U.S. destination (wits_ecuador_balsa_us_2025). Complements 2022–2024 WITS and AIMA manufactures-share rows (different product basket).",
        "pair_id": "wits_ecu_balsa_2025_cn_us",
        "counterpart_side": "us",
        "counterpart_actor": "United States",
        "counterpart_value": str(US),
        "counterpart_currency": "USD",
        "counterpart_value_usd": str(US),
        "gap": f"{GAP:.6f}",
    },
    {
        "id": "wits_ecuador_balsa_china_2025",
        "retrieved": "2026-10-01",
        "source_id": "wits_ecu_440723_2025",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2025/tradeflow/Exports/partner/ALL/product/440723",
        "price_year": "2025",
        "evidence": "paired",
        "quote": "Ecuador exported Baboen, Mahogany, Imbuia and Balsa wood, sawn l to China ($144,828.45K , 483,750 m³), … United States ($4,699.55K , 45,481 m³).",
        "note": "Opened WITS/Comtrade Ecuador HS 440723 2025 exports-by-partner table.",
    },
    {
        "id": "wits_ecu_440723_2025",
        "type": "official",
        "chicago": "World Bank WITS / UN Comtrade. “Ecuador Baboen, Mahogany, Imbuia and Balsa wood, sawn l exports by country | 2025.” Accessed 1 October 2026.",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2025/tradeflow/Exports/partner/ALL/product/440723",
        "annotation": "Official trade mirror for Ecuador HS 440723 2025 exports. Supports wits_ecuador_balsa_china_2025 and wits_ecuador_balsa_us_2025.",
        "supports": [
            "wits_ecuador_balsa_china_2025",
            "wits_ecuador_balsa_us_2025",
            "hunt_res_balsa",
        ],
    },
)

A(
    {
        "id": "wits_ecuador_balsa_us_2025",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "us",
        "counterpart": "United States — Ecuador HS 440723 sawn balsa/related wood imports (WITS/Comtrade)",
        "country": "Ecuador",
        "asset": "Ecuador 2025 exports of HS 440723 to United States — USD 4.700 million (WITS); quantity 45,481 m³",
        "investment_type": "other",
        "value": str(US),
        "currency": "USD",
        "value_usd": str(US),
        "fx_usd": "1",
        "fx_date": "2025-12-31",
        "year": "2025",
        "status": "active",
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Quevedo / Guayas–Los Ríos balsa processing belt (export-origin proxy; not a single mill pin).",
        "evidence": "documented",
        "source_id": "wits_ecu_440723_2025",
        "note": "Trade flow. WITS/Comtrade Ecuador HS 440723 to United States 2025. U.S. counterpart to wits_ecuador_balsa_china_2025 paired row (same table).",
        "pair_id": "wits_ecu_balsa_2025_cn_us",
        "counterpart_side": "prc",
        "counterpart_actor": "China",
        "counterpart_value": str(CHINA),
        "counterpart_currency": "USD",
        "counterpart_value_usd": str(CHINA),
        "gap": f"{GAP:.6f}",
    },
    {
        "id": "wits_ecuador_balsa_us_2025",
        "retrieved": "2026-10-01",
        "source_id": "wits_ecu_440723_2025",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2025/tradeflow/Exports/partner/ALL/product/440723",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Ecuador exported … to … United States ($4,699.55K , 45,481 m³).",
        "note": "Opened same WITS 2025 table as China destination row.",
    },
    {
        "id": "wits_ecu_440723_2025",
        "type": "official",
        "chicago": "World Bank WITS / UN Comtrade. “Ecuador Baboen, Mahogany, Imbuia and Balsa wood, sawn l exports by country | 2025.” Accessed 1 October 2026.",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2025/tradeflow/Exports/partner/ALL/product/440723",
        "annotation": "Official trade mirror for Ecuador HS 440723 2025 exports. Supports wits_ecuador_balsa_china_2025 and wits_ecuador_balsa_us_2025.",
        "supports": [
            "wits_ecuador_balsa_china_2025",
            "wits_ecuador_balsa_us_2025",
            "hunt_res_balsa",
        ],
    },
)


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
        sid = bib_entry["id"]
        if sid in bib_by:
            existing = bib[bib_by[sid]]
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
            if bib_entry.get("supports"):
                existing["supports"] = sorted(
                    set(existing.get("supports") or []) | set(bib_entry["supports"])
                )
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

    if "hunt_res_balsa" in by_id:
        rows[by_id["hunt_res_balsa"]]["note"] = (
            (rows[by_id["hunt_res_balsa"]].get("note") or "")
            + " Cycle 42 thin_topup: logged wits_ecuador_balsa_china_2025 + wits_ecuador_balsa_us_2025 (paired)."
        ).strip()
    for hid, note in [
        (
            "hunt_res_graphite",
            "Cycle 42 thin_topup: Graphcoa/South Star/Atlas already (miss).",
        ),
        (
            "hunt_energy_fission_smr",
            "Cycle 42 thin_topup: Peru FIRST / INB–Westinghouse already (miss).",
        ),
    ]:
        if hid in by_id:
            rows[by_id[hid]]["note"] = (
                (rows[by_id[hid]].get("note") or "") + " " + note
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
    print("Cycle 42 thin_topup added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
