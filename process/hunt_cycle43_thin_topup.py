#!/usr/bin/env python3
"""Cycle 43 thin_topup: balsa / graphite / fission_smr (fewest post-pass).

Hits: Plantabal 2025 planting 2,951 ha; Graphcoa Boa Sorte→Urbix U.S. first export.
Miss: fission_smr (FIRST workshop already in shuffled pass; no distinct new CAPEX).
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


# resources/balsa — Plantabal 2025 plantation planting (FSC public monitoring)
A(
    {
        "id": "plantabal_2025_planting_2951ha",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "allied",
        "counterpart": "3A Composites / Plantabal — 2025 balsa plantation planting (Ecuador)",
        "country": "Ecuador",
        "asset": "Plantabal S.A. 2025 public forest-monitoring summary: planted 2,951 hectares of balsa (Ochroma pyramidale) during 2025 across its ~14,347.64 ha plantation estate (Los Ríos, Cotopaxi, Manabí, Santo Domingo, Esmeraldas, Guayas, Pichincha). Winter storm damage required transplanting on some non-harvest haciendas. Ops/planting presence — no disclosed CAPEX USD on opened PDF.",
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
        "geo_note": "Quevedo / Los Ríos Plantabal main plant and plantation belt (company geography; approximate).",
        "evidence": "documented",
        "source_id": "plantabal_monitoreo_2025",
        "note": "Actor: 3A Composites / Plantabal (Swiss Schweiter) — allied. Company FSC-style public monitoring resumen 2025. Distinct from plantabal_3a_ecuador_presence (site presence without 2025 planting figure).",
    },
    {
        "id": "plantabal_2025_planting_2951ha",
        "retrieved": "2026-10-01",
        "source_id": "plantabal_monitoreo_2025",
        "url": "https://3accorematerials.com/uploads/pdf/Resumen-P%C3%BAblico-Monitoreo-2025.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Durante el año 2025 se realizó la siembra de 2,951 hectáreas de balsa. … Plantaciones de Balsa Plantabal S.A. administra un patrimonio forestal de aproximadamente 14,347.64 ha, de plantaciones de balsa (Ochroma pyramidale).",
        "note": "Opened Plantabal / 3A Composites Resumen Público Monitoreo 2025 PDF.",
    },
    {
        "id": "plantabal_monitoreo_2025",
        "type": "company",
        "chicago": "Plantaciones de Balsa Plantabal S.A. / 3A Composites. “Resumen Público de Monitoreo 2025.” Accessed 1 October 2026.",
        "url": "https://3accorematerials.com/uploads/pdf/Resumen-P%C3%BAblico-Monitoreo-2025.pdf",
        "annotation": "Company public FSC monitoring summary with 2025 planting hectares. Supports plantabal_2025_planting_2951ha.",
        "supports": ["plantabal_2025_planting_2951ha", "hunt_res_balsa"],
    },
)

# resources/graphite — Graphcoa Boa Sorte first concentrate exports to Urbix (U.S.)
A(
    {
        "id": "graphcoa_boa_sorte_urbix_export_2025",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "us",
        "counterpart": "Urbix / U.S. — Graphcoa Boa Sorte concentrate first exports for anode validation",
        "country": "Brazil",
        "asset": "2025 ramp at Graphcoa Mina Boa Sorte (Itagimirim, Bahia): press citing Graphcoa executive states exports to the United States begun for testing/validation with strategic customers; production processed by U.S. anode firm Urbix. Complements appian_urbix_graphcoa_jda_2023 (JDA) and graphcoa_boa_sorte_bahia_2024 (R$350m Phase 1 ops). No disclosed export USD on opened page.",
        "investment_type": "offtake",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-16.0",
        "lon": "-40.0",
        "geo_note": "Itagimirim / Boa Sorte, Bahia (press geography; approximate).",
        "evidence": "proxy",
        "source_id": "cenario_graphcoa_boa_sorte_20250728",
        "note": "Actor: U.S. Urbix receiving Brazilian Graphcoa concentrate — us. UNVERIFIED proxy: Cenário Energia 28 Jul 2025 quoting Graphcoa director Ricardo Alves on U.S. exports for validation. Distinct from JDA/Allied offtake path rows.",
    },
    {
        "id": "graphcoa_boa_sorte_urbix_export_2025",
        "retrieved": "2026-10-01",
        "source_id": "cenario_graphcoa_boa_sorte_20250728",
        "url": "https://cenarioenergia.com.br/2025/07/28/graphcoa-avanca-na-producao-de-grafite-na-bahia-e-mira-mercado-nacional-e-internacional/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "Já iniciamos as exportações para os Estados Unidos, com foco em testes e validação do nosso produto junto a clientes estratégicos. … Parte da produção da Mina Boa Sorte já está sendo exportada para os Estados Unidos, onde será processada pela Urbix, empresa norte-americana especializada em tecnologias para a fabricação de ânodos de grafite.",
        "note": "Opened Cenário Energia 28 Jul 2025 Graphcoa Boa Sorte feature.",
    },
    {
        "id": "cenario_graphcoa_boa_sorte_20250728",
        "type": "trade_press",
        "chicago": "Cenário Energia. “Graphcoa Avança Na Produção De Grafite Na Bahia E Mira Mercado Nacional E Internacional.” 28 July 2025.",
        "url": "https://cenarioenergia.com.br/2025/07/28/graphcoa-avanca-na-producao-de-grafite-na-bahia-e-mira-mercado-nacional-e-internacional/",
        "annotation": "Trade press on Boa Sorte ramp and U.S./Urbix exports. Supports graphcoa_boa_sorte_urbix_export_2025.",
        "supports": [
            "graphcoa_boa_sorte_urbix_export_2025",
            "hunt_res_graphite",
        ],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if k == "supports":
                existing["supports"] = sorted(
                    set(existing.get("supports") or []) | set(v or [])
                )
            elif v is not None:
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

    for hid, note in {
        "hunt_res_balsa": "Cycle 43 thin_topup: logged plantabal_2025_planting_2951ha.",
        "hunt_res_graphite": "Cycle 43 thin_topup: logged graphcoa_boa_sorte_urbix_export_2025 (U.S.).",
        "hunt_energy_fission_smr": "Cycle 43 thin_topup: fission miss (workshop already in shuffled pass).",
    }.items():
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
    print("Cycle 43 thin_topup added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
