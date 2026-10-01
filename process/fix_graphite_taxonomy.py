#!/usr/bin/env python3
"""Ben correction: dimension_stone/granite → graphite. Archive granite rows; add graphite rows."""
from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "codebook" / "observations.csv"
EVID = ROOT / "data" / "attribution" / "evidence"
BIB = ROOT / "sources" / "bibliography.yml"
FIELDS = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")).fieldnames)


def blank():
    return {k: "" for k in FIELDS}


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}

    # --- Rename hunt seed ---
    old_hunt = "hunt_res_dimension_stone"
    new_hunt = "hunt_res_graphite"
    if old_hunt in by_id:
        r = rows[by_id[old_hunt]]
        r["id"] = new_hunt
        r["subcategory"] = "graphite"
        r["country"] = ""
        r["asset"] = (
            "LatAm graphite mining, processing, or anode/CSPG supply-chain stake "
            "(Brazil, Mexico, others)"
        )
        r["note"] = (
            "Hunt: graphite mine, concentrator, spherical/coated anode material, or offtake "
            "linking Latin America (esp. Brazil, Mexico) to a U.S. or PRC buyer/processor. "
            "No pin until a named site exists. Taxonomy correction 2026-10-01: subcategory is "
            "graphite (not dimension stone/granite). Prior granite ABIROCHAS rows archived."
        )
        by_id[new_hunt] = by_id.pop(old_hunt)
        old_ev = EVID / f"{old_hunt}.json"
        new_ev = EVID / f"{new_hunt}.json"
        if old_ev.exists():
            payload = json.loads(old_ev.read_text(encoding="utf-8"))
            payload["id"] = new_hunt
            payload["note"] = (
                "Hunt seed retargeted to graphite mining/processing/anode chains "
                "(Ben correction 2026-10-01)."
            )
            new_ev.write_text(
                json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
            old_ev.unlink()

    # --- Archive granite / dimension-stone rows (wrong commodity) ---
    for rid in ("abirochas_br_stone_china_2023", "abirochas_br_stone_us_2023"):
        if rid not in by_id:
            continue
        r = rows[by_id[rid]]
        r["status"] = "archived"
        r["evidence"] = "exclude"
        r["subcategory"] = "graphite"  # keep key valid for schema; archived exclude
        r["note"] = (
            (r.get("note") or "")
            + " ARCHIVED 2026-10-01: filed under former dimension_stone/granite subcategory; "
            "Scarce Natural Resources taxonomy is graphite (Ben correction). Ornamental stone "
            "trade is out of scope — not a graphite observation."
        ).strip()

    # --- New graphite observations ---
    items = []

    items.append(
        (
            {
                "id": "south_star_santa_cruz_graphite_2024",
                "layer": "resources",
                "subcategory": "graphite",
                "side": "allied",
                "counterpart": "South Star Battery Metals — Santa Cruz Graphite Mine (Bahia)",
                "country": "Brazil",
                "asset": "Santa Cruz Phase 1 natural flake graphite mine/plant — ~12,000 tpy nameplate; substantial completion / commissioning announced Jul 2024",
                "investment_type": "ownership_equity",
                "value": "",
                "currency": "USD",
                "value_usd": "",
                "fx_usd": "",
                "fx_date": "",
                "year": "2024",
                "status": "active",
                "lat": "-15.65",
                "lon": "-39.65",
                "geo_note": "Southern Bahia, Brazil (company release; approximate regional pin).",
                "evidence": "documented",
                "source_id": "south_star_santa_cruz_20240729",
                "note": "Actor: South Star Battery Metals (Canadian TSXV/OTCQB) — allied. Company release 29 Jul 2024: Phase 1 ~12,000 tpy flake concentrates; first new Americas graphite production since 1996 claimed. Also advancing CSPG/anode product suite. Upgrades hunt_res_graphite.",
            },
            {
                "id": "south_star_santa_cruz_graphite_2024",
                "retrieved": "2026-10-01",
                "source_id": "south_star_santa_cruz_20240729",
                "url": "https://southstarbatterymetals.com/wp-content/uploads/2024/07/2024-07-29_STS_SubstantialCompletion_Final.pdf",
                "price_year": "2024",
                "evidence": "documented",
                "quote": "Phase 1 construction for the Company’s flagship Santa Cruz Graphite Mine (“Santa Cruz”) is substantially complete and commissioning is underway. Santa Cruz is located in Bahia, Brazil, and the Phase 1 plant has a nameplate capacity of approximately 12,000 tonnes/year (“tpy”) of natural flake graphite concentrates.",
                "note": "Opened South Star company PDF release.",
            },
            {
                "id": "south_star_santa_cruz_20240729",
                "type": "official",
                "chicago": "South Star Battery Metals Corp. “South Star Announces Substantial Completion and Commissioning of the Santa Cruz Phase 1 Graphite Mine in Brazil.” 29 July 2024.",
                "url": "https://southstarbatterymetals.com/wp-content/uploads/2024/07/2024-07-29_STS_SubstantialCompletion_Final.pdf",
                "annotation": "Company primary notice of Santa Cruz Phase 1 graphite plant substantial completion. Supports south_star_santa_cruz_graphite_2024.",
                "supports": ["south_star_santa_cruz_graphite_2024", "hunt_res_graphite"],
            },
        )
    )

    items.append(
        (
            {
                "id": "nacional_de_grafite_mg_presence",
                "layer": "resources",
                "subcategory": "graphite",
                "side": "other",
                "counterpart": "Nacional de Grafite Ltda. — Minas Gerais crystalline graphite operations",
                "country": "Brazil",
                "asset": "Nacional de Grafite natural crystalline graphite mining/processing (three MG production units + São Paulo business unit)",
                "investment_type": "ownership_equity",
                "value": "",
                "currency": "USD",
                "value_usd": "",
                "fx_usd": "",
                "fx_date": "",
                "year": "2024",
                "status": "active",
                "lat": "-20.47",
                "lon": "-45.0",
                "geo_note": "Itapecerica / Minas Gerais production region (company site).",
                "evidence": "documented",
                "source_id": "nacional_de_grafite_en_home",
                "note": "Actor: Nacional de Grafite (Brazilian host producer) — other. Company English site documents three modern production units near major MG reserves and SP business unit. Host-country graphite mining/processing presence for comparative net. No transaction USD on page.",
            },
            {
                "id": "nacional_de_grafite_mg_presence",
                "retrieved": "2026-10-01",
                "source_id": "nacional_de_grafite_en_home",
                "url": "https://www.grafite.com/en/",
                "price_year": "2024",
                "evidence": "documented",
                "quote": "We have three modern production units strategically located near the major reserves in Minas Gerais, and a business unit in São Paulo, the main financial centre of Latin America.",
                "note": "Opened Nacional de Grafite English home page.",
            },
            {
                "id": "nacional_de_grafite_en_home",
                "type": "official",
                "chicago": "Nacional de Grafite Ltda. “Nacional de Grafite - high-quality crystalline graphite.” Company site. Accessed 1 October 2026.",
                "url": "https://www.grafite.com/en/",
                "annotation": "Company primary description of MG graphite production footprint. Supports nacional_de_grafite_mg_presence.",
                "supports": ["nacional_de_grafite_mg_presence", "hunt_res_graphite"],
            },
        )
    )

    items.append(
        (
            {
                "id": "graphex_south_star_brazil_offtake_2023",
                "layer": "resources",
                "subcategory": "graphite",
                "side": "us",
                "counterpart": "Graphex Technologies LLC — offtake collaboration covering South Star Santa Cruz (Brazil) graphite for anode midstream",
                "country": "Brazil",
                "asset": "Graphex Technologies offtake/collaboration for raw graphite from South Star Santa Cruz (Brazil) toward North American anode processing",
                "investment_type": "offtake",
                "value": "",
                "currency": "USD",
                "value_usd": "",
                "fx_usd": "",
                "fx_date": "",
                "year": "2023",
                "status": "active",
                "lat": "-15.65",
                "lon": "-39.65",
                "geo_note": "Santa Cruz, Bahia supply source (Graphex release naming Brazil Santa Cruz).",
                "evidence": "documented",
                "source_id": "graphex_exchina_strategy_20231025",
                "note": "Actor: Graphex Technologies LLC (U.S. subsidiary of Graphex Group) — coded us for U.S. anode midstream offtake of Brazilian flake. Company release 25 Oct 2023 lists South Star Battery Metals for supply from Brazil (Santa Cruz) and the U.S. No USD on page. Complements south_star_santa_cruz_graphite_2024.",
            },
            {
                "id": "graphex_south_star_brazil_offtake_2023",
                "retrieved": "2026-10-01",
                "source_id": "graphex_exchina_strategy_20231025",
                "url": "https://graphexgroup.com/2023/10/25/graphex-technologies-reinforces-its-diverse-mine-to-battery-global-strategy-following-the-announcement-of-graphite-export-limits-from-china/",
                "price_year": "2023",
                "evidence": "documented",
                "quote": "South Star Battery Metals, for supply from both Brazil and the United States, through the Santa Cruz Graphite Project and the Ceylon Graphite Project.",
                "note": "Opened Graphex Group press page.",
            },
            {
                "id": "graphex_exchina_strategy_20231025",
                "type": "official",
                "chicago": "Graphex Group Limited / Graphex Technologies, LLC. “Graphex Technologies Reinforces its Diverse Mine-to-Battery Global Strategy Following the Announcement of Graphite Export Limits from China.” 25 October 2023.",
                "url": "https://graphexgroup.com/2023/10/25/graphex-technologies-reinforces-its-diverse-mine-to-battery-global-strategy-following-the-announcement-of-graphite-export-limits-from-china/",
                "annotation": "Company release listing South Star Brazil Santa Cruz among graphite offtake sources for U.S. anode strategy. Supports graphex_south_star_brazil_offtake_2023.",
                "supports": [
                    "graphex_south_star_brazil_offtake_2023",
                    "hunt_res_graphite",
                ],
            },
        )
    )

    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}

    # Rename hunt id in all bib supports
    for e in bib:
        supports = e.get("supports") or []
        if "hunt_res_dimension_stone" in supports:
            e["supports"] = sorted(
                {("hunt_res_graphite" if s == "hunt_res_dimension_stone" else s) for s in supports}
            )

    for row, evidence, bib_entry in items:
        rid = row["id"]
        full = blank()
        full.update(row)
        if rid in by_id:
            rows[by_id[rid]] = full
        else:
            by_id[rid] = len(rows)
            rows.append(full)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        sid = bib_entry["id"]
        if sid in bib_by:
            existing = bib[bib_by[sid]]
            supports = set(existing.get("supports") or [])
            supports.update(bib_entry.get("supports") or [])
            existing["supports"] = sorted(supports)
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

    # Any remaining dimension_stone subcategory → graphite
    for r in rows:
        if r.get("subcategory") == "dimension_stone":
            r["subcategory"] = "graphite"

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print("graphite rename complete; new rows:", [t[0]["id"] for t in items])


if __name__ == "__main__":
    main()
