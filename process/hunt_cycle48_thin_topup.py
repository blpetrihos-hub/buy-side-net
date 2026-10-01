#!/usr/bin/env python3
"""Cycle 48 thin_topup: post-pass thinnest balsa, niobium, fission_smr (recompute).

Adds processor/plant angles for balsa + CBMM 2025 annual spend for niobium;
fission_smr documented miss.
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
# thin: resources/balsa — Plantabal 2025 Responsible Sourcing Policy (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "plantabal_sourcing_policy_2025",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "allied",
        "counterpart": "Plantabal S.A. — Responsible Sourcing Policy CE-CW-D2 (Aug 2025)",
        "country": "Ecuador",
        "asset": "August 2025 Plantabal Responsible Sourcing Policy (CE-CW-D2 v05): mandatory supply-chain due diligence for legal, properly managed plantation/forest raw materials across Plantabal silviculture and contractors — processor governance angle for Ecuador plantation-to-BALTEK wind-blade core chain. Distinct from planting/revenue/FSC MIX product rows; not a trade-flow duplicate.",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Plantabal Quevedo operations, Los Ríos (processor pin).",
        "evidence": "documented",
        "source_id": "plantabal_sourcing_policy_202508",
        "note": "Actor: Plantabal / 3A Composites (Switzerland) — allied. Company policy PDF Aug 2025; no CAPEX.",
    },
    {
        "id": "plantabal_sourcing_policy_2025",
        "retrieved": "2026-10-01",
        "source_id": "plantabal_sourcing_policy_202508",
        "url": "https://www.3accorematerials.com/uploads/pdf/CE-CW-D2-Sourcing-Policy-Plantabal-2025.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "At Plantaciones de Balsa, Plantabal S.A., we are firmly committed to sourcing products and services that ensure the raw materials we used come from legal, properly managed forests and plantations. … This Responsible Sourcing Policy is mandatory for all forestry operations and processes of Plantaciones de Balsa, Plantabal S.A., as well as for all products and services we procure.",
        "note": "Opened Plantabal CE-CW-D2 Responsible Sourcing Policy PDF (v05, 08/2025).",
    },
    {
        "id": "plantabal_sourcing_policy_202508",
        "type": "company",
        "chicago": "Plantaciones de Balsa Plantabal S.A. “Política de Abastecimiento Responsable / Responsible Sourcing Policy.” CE-CW-D2, versión 05, August 2025.",
        "url": "https://www.3accorematerials.com/uploads/pdf/CE-CW-D2-Sourcing-Policy-Plantabal-2025.pdf",
        "annotation": "Company primary responsible-sourcing policy for Ecuador Plantabal operations. Supports plantabal_sourcing_policy_2025.",
        "supports": ["plantabal_sourcing_policy_2025", "hunt_res_balsa"],
    },
)

# ---------------------------------------------------------------------------
# thin: resources/niobium — CBMM R$1.1bn 2025 growth/innovation spend (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cbmm_araxa_2025_spend_1p1bn",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "CBMM — 2025 Araxá growth and innovation investment",
        "country": "Brazil",
        "asset": "Brasil Mineral 24 Mar 2026 citing CBMM: company invested R$1.1 billion in growth and innovation in 2025, leveraged by expansion into electric mobility, energy storage and data centers, alongside Codemig partnership renewal. Annual executed spend — distinct from cbmm_araxa_capex_plan_2025 (R$10bn five-year plan), cbmm_araxa_13bn_plan_2026, and cbmm_araxa_2026_spend_2bn.",
        "investment_type": "other",
        "value": "1100000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "CBMM Araxá industrial complex, Minas Gerais.",
        "evidence": "proxy",
        "source_id": "brasilmineral_cbmm_2025_1p1bn",
        "note": "Actor: CBMM — allied. UNVERIFIED proxy: Brasil Mineral 24 Mar 2026 citing company R$1.1bn 2025 spend. Value stored as BRL (no FX).",
    },
    {
        "id": "cbmm_araxa_2025_spend_1p1bn",
        "retrieved": "2026-10-01",
        "source_id": "brasilmineral_cbmm_2025_1p1bn",
        "url": "https://brasilmineral.com.br/noticias/cbmm-investe-r-11-bilhao-em-crescimento-e-inovacao-em-2025",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "CBMM investe R$ 1,1 bilhão em crescimento e inovação em 2025 … Investimento é alavancado por expansão em mobilidade elétrica, armazenamento de energia e data centers, além da renovação da parceria com a Codemig que garante acesso ao minério até 2070.",
        "note": "Opened Brasil Mineral article summarizing CBMM 2025 R$1.1bn spend.",
    },
    {
        "id": "brasilmineral_cbmm_2025_1p1bn",
        "type": "press",
        "chicago": "Brasil Mineral. “CBMM investe R$ 1,1 bilhão em crescimento e inovação em 2025.” 24 March 2026.",
        "url": "https://brasilmineral.com.br/noticias/cbmm-investe-r-11-bilhao-em-crescimento-e-inovacao-em-2025",
        "annotation": "UNVERIFIED proxy press on CBMM R$1.1bn 2025 growth/innovation spend at Araxá. Supports cbmm_araxa_2025_spend_1p1bn.",
        "supports": ["cbmm_araxa_2025_spend_1p1bn", "hunt_fenb_araxa"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None:
                existing[k] = v
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

    notes = {
        "hunt_res_balsa": "Cycle 48 thin_topup: logged plantabal_sourcing_policy_2025 (allied; processor governance — not trade duplicate).",
        "hunt_fenb_araxa": "Cycle 48 thin_topup: logged cbmm_araxa_2025_spend_1p1bn (allied; R$1.1bn 2025 spend proxy).",
        "hunt_energy_fission_smr": "Cycle 48 thin_topup: miss (Meitner ACR-300 / FIRST / Rosatom / El Salvador 123 already).",
    }
    for hid, note in notes.items():
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
    print("Cycle 48 thin_topup rows added:", len(added))
    print("\n".join(added) if added else "(none)")


if __name__ == "__main__":
    main()
