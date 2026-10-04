#!/usr/bin/env python3
"""Cycle 213 hunt: shuffle_seed=20261213; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261213).shuffle):
engineering_epc, building_materials, bridges_roads, graphite, niobium, fission_smr,
rail, port_ownership, port_cranes, power_plants_grid, water, wind, lithium, copper,
solar, other_renewables, balsa, nickel.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES Andes Hub/EXIM Black Giant/DFC Serra/
EnergyX/Nextracker/Array/Wabtec MRS/GE Vernova São Simão/Bechtel/Fluor/
Fluence/USTDA/Equinix/Freeport El Abra/SSA Marine sweeps (0 new U.S. rows —
catalog dense). PRC equal-budget: PowerChina Chile Decree 4 / Dune Plus /
Palmira / State Grid UHV / ZPMC / CAMCE already logged; holdovers unsigned.
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
    rid,
    layer,
    subcategory,
    side,
    counterpart,
    country,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    source_id,
    quote,
    url,
    note,
    hunt_support,
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd=None,
    fx_usd=None,
    chicago=None,
    bib_type="company",
    annotation=None,
    evid_note=None,
    pair_id="",
    counterpart_side="",
    counterpart_actor="",
    counterpart_value="",
    counterpart_currency="",
    counterpart_value_usd="",
    gap="",
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": investment_type,
            "value": value,
            "currency": currency,
            "value_usd": value_usd,
            "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "",
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": evidence,
            "source_id": source_id,
            "note": note,
            "pair_id": pair_id,
            "counterpart_side": counterpart_side,
            "counterpart_actor": counterpart_actor,
            "counterpart_value": counterpart_value,
            "counterpart_currency": counterpart_currency,
            "counterpart_value_usd": counterpart_value_usd,
            "gap": gap,
        },
        {
            "id": rid,
            "retrieved": "2026-10-04",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": evidence,
            "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id,
            "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url,
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. engineering_epc / other — Schwager–Incimmet Chuquicamata vertical developments CLP 104.258bn
row_doc(
    "schwager_incimmet_chuqui_104bn_clp_2026",
    "infrastructure",
    "engineering_epc",
    "other",
    "Consorcio Schwager–Incimmet — Codelco Chuquicamata vertical developments / linings (Líneas 5–6)",
    "Chile",
    "18–19 May 2026: Consorcio Schwager–Incimmet SpA (Schwager Service S.A. 60% / Incimmet Chile SpA 40%) accepts Codelco Chuquicamata award LIC 046/25 “Desarrollos Verticales y Blindajes de Continuidad Líneas 5 y 6 Norte y Sur” — mechanized Blind Hole / Raise Borer raises, ventilation raises, civil/structural works. Maximum contract price CLP 104.258 billion (unit-price modality; base scope CLP 62.569 billion; initial 36 months extendable to 67 months). Distinct from Codelco QB stake / MIGA climate financing rows.",
    "104258000000",
    "2026-05-19",
    "2026",
    "-22.29",
    "-68.90",
    "Chuquicamata underground mine, Calama, Antofagasta Region (company geography).",
    "schwager_chuqui_adjudicacion_202605",
    "El contrato contempla un monto máximo de hasta $104.258 millones, bajo modalidad de precios unitarios, incluyendo un alcance base de $62.569 millones y una eventual extensión sujeta a evaluación de desempeño.",
    "https://www.schwager.cl/consorcio-schwager-incimmet-se-adjudica-contrato-por-mas-de-104-mil-millones-con-codelco-para-desarrollos-verticales-en-chuquicamata/",
    "Actor: Schwager (Chile) + Incimmet (Peru) consortium — other (LatAm host contractors). Company Spanish primary. CapEx face = CLP 104.258bn max. USD blank (Fed H.10 unreachable). Shuffle engineering_epc.",
    "hunt_cycle213",
    investment_type="epc",
    evidence="documented",
    currency="CLP",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Schwager S.A. “Consorcio Schwager-Incimmet se adjudica contrato por más de $104 mil millones con Codelco para desarrollos verticales en Chuquicamata.” May 2026. https://www.schwager.cl/consorcio-schwager-incimmet-se-adjudica-contrato-por-mas-de-104-mil-millones-con-codelco-para-desarrollos-verticales-en-chuquicamata/.',
    annotation="Schwager–Incimmet Chuquicamata EPC CLP 104.258bn. Supports schwager_incimmet_chuqui_104bn_clp_2026.",
    evid_note="Opened Schwager Spanish primary 2026-10-04; CLP 104.258bn max / CLP 62.569bn base / Líneas 5–6 / Blind Hole–Raise Borer / 36–67 months confirmed.",
)

# 2. graphite / allied — CapEx-fill Graphcoa Jordânia to R$700m (press refresh vs RIMA R$621.76m)
row_doc(
    "graphcoa_jordania_dfs_capex_2026",
    "resources",
    "graphite",
    "allied",
    "Graphcoa / Appian Capital Brazil — Projeto Grafite Jordânia",
    "Brazil",
    "Graphcoa (Appian Capital Brazil) Projeto Grafite Jordânia integrated natural-graphite mine + concentrator at Jordânia (Jequitinhonha Valley, MG); ~53,000 t/year capacity; construction targeted from mid-2027 with commercial ops 2H 2029. CapEx-fill refresh: Diário do Comércio reports planned investment around R$ 700 million (prior RIMA implantation estimate R$ 621.76 million / ~USD 120m retained as context). Distinct from graphcoa_boa_sorte / graphcoa_projects_invested_75m rows.",
    "700000000",
    "2026-06-20",
    "2026",
    "-15.90",
    "-40.18",
    "Jordânia, Vale do Jequitinhonha, Minas Gerais (company/project geography; municipal pin).",
    "diario_comercio_graphcoa_jordania_700m",
    "A Graphcoa planeja investir em torno de R$ 700 milhões em uma planta voltada à produção de grafite concentrado, com teores de aproximadamente 95% de carbono grafítico, no município de Jordânia, na região do Vale do Jequitinhonha, em Minas Gerais.",
    "https://diariodocomercio.com.br/economia/graphcoa-grafite-minas/",
    "Actor: Graphcoa / Appian Capital Brazil (UK PE) — allied. CapEx-fill upgrade from R$621.76m RIMA DFS to ~R$700m press figure. USD blank (Fed H.10 unreachable). Shuffle graphite.",
    "hunt_cycle213",
    investment_type="feasibility_capex",
    evidence="proxy",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="press",
    chicago='Diário do Comércio. “Graphcoa deve investir R$ 700 mi em planta de grafite em Minas.” https://diariodocomercio.com.br/economia/graphcoa-grafite-minas/.',
    annotation="Graphcoa Jordânia CapEx-fill ~R$700m (press). Supports graphcoa_jordania_dfs_capex_2026.",
    evid_note="Opened Diário do Comércio 2026-10-04; ~R$700m / Jordânia / ~50 ktpa / 2H 2029 ops confirmed. UNVERIFIED proxy refresh vs prior RIMA R$621.76m; CapEx-fill upgrade.",
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
    if not isinstance(bib, list):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added = []
    updated = []

    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
            updated.append(rid)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_e)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle213 added {len(added)}: {added}")
    print(f"cycle213 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
