#!/usr/bin/env python3
"""Cycle 298 hunt: shuffle_seed=20261298; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261298).shuffle):
lithium, building_materials, other_renewables, nickel, niobium, port_cranes,
fission_smr, balsa, engineering_epc, power_plants_grid, bridges_roads, graphite,
copper, solar, rail, port_ownership, water, wind.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (nickel fourth / balsa eighth in shuffle — CapEx-fill dry).
≥1/3 U.S. hunt budget: NEW Progress Rail VLI cumulative 27-loco CapEx ~R$600m
  (distinct from R$200m eight-loco face); R$430m holdover still not dual-confirmed;
  Arenales/SSA STS/Bechtel blanks; lithium CapEx-fill blanks.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
ALLIED: NEW Alupar TAP/TPC/TCN CapEx Realizado from 2T26 implantation table.
Skipped: thin dry; Motiva Capex Proforma largely mined; holdovers unsigned.
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

BRL_USD = "5.1921"
VLI_URL = (
    "https://www.vli-logistica.com.br/vli-e-progress-rail-celebram-recebimento-de-"
    "locomotivas-para-operacao-na-ferrovia-centro-atlantica/"
)
ALUPAR_URL = "https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip"


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid, layer, subcategory, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, source_id, quote, url, note, hunt_support,
    investment_type="epc", evidence="documented", currency="USD", value_usd=None,
    fx_usd=None, chicago=None, bib_type="company", annotation=None, evid_note=None,
    status="active",
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid, "layer": layer, "subcategory": subcategory, "side": side,
            "counterpart": counterpart, "country": country, "asset": asset,
            "investment_type": investment_type, "value": value, "currency": currency,
            "value_usd": value_usd, "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "", "year": year, "status": status,
            "lat": lat, "lon": lon, "geo_note": geo, "evidence": evidence,
            "source_id": source_id, "note": note, "pair_id": "", "counterpart_side": "",
            "counterpart_actor": "", "counterpart_value": "", "counterpart_currency": "",
            "counterpart_value_usd": "", "gap": "",
        },
        {
            "id": rid, "retrieved": "2026-10-05", "source_id": source_id, "url": url,
            "price_year": year, "evidence": evidence, "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id, "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url, "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# Progress Rail / VLI cumulative locomotive CapEx (US) — breaks US CapEx dry streak
row_doc(
    "progress_rail_vli_27loco_600m_brl_2026", "infrastructure", "rail", "us",
    "Progress Rail — VLI cumulative 27 locomotives CapEx ~R$600m since 2024",
    "Brazil",
    "10 Feb 2026 VLI Portuguese (Progress Rail Caterpillar celebration): with completion of eight EMD SD70ACe-BB delivery, VLI accumulates acquisition of 27 locomotives since 2024 totaling investments of about R$600 million. CapEx: enter cumulative locomotive CapEx face. Distinct from eight-loco ~R$200m face and from MSA up to R$500m (Corredor Norte); R$430m holdover figure still not dual-confirmed as separable.",
    "600000000", "2026-02-10", "2026", "-19.92", "-43.94",
    "Ferrovia Centro-Atlântica / VLI Progress Rail delivery celebration (Belo Horizonte pin).",
    "vli_progress_rail_sd70_20260210",
    "Com a concretização do negócio, a VLI acumula a aquisição de 27 locomotivas desde 2024, totalizando investimentos de cerca de R$ 600 milhões.",
    VLI_URL,
    "Actor: Progress Rail (Caterpillar) — us. NEW cumulative 27-loco CapEx. Shuffle rail; ≥1/3 US hunt budget.",
    "hunt_cycle298", investment_type="equipment_supply", evidence="documented", currency="BRL",
    value_usd=str(round(600000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='VLI Logística. “VLI e Progress Rail celebram recebimento de locomotivas para operação na Ferrovia Centro-Atlântica.” February 10, 2026. ' + VLI_URL + ".",
    annotation="Progress Rail VLI 27-loco cumulative CapEx via Fed H.10. Supports progress_rail_vli_27loco_600m_brl_2026.",
    evid_note="Opened VLI Portuguese Progress Rail celebration; ~R$600m for 27 locomotives since 2024 confirmed.",
)

# Alupar CapEx Realizado — Brazil TAP/TPC/TCN (allied)
ALUPAR_CHICAGO = (
    'Alupar Investimento S.A. “Release de Resultados 2T26” (RI ZIP). August 6, 2026. '
    + ALUPAR_URL + "."
)
for rid, name, val, quote, lat, lon, geo in [
    ("alupar_tap_capex_realizado_226p1m_brl", "TAP", 226100000, "CAPEX Realizado (MM) R$ 226,1",
     "-15.78", "-47.93", "Alupar TAP transmission project Brazil (Brasília HQ pin)."),
    ("alupar_tpc_capex_realizado_305p8m_brl", "TPC", 305800000, "CAPEX Realizado (MM) … R$ 305,8",
     "-15.78", "-47.93", "Alupar TPC transmission project Brazil (Brasília HQ pin)."),
    ("alupar_tcn_capex_realizado_35p1m_brl", "TCN", 35100000, "CAPEX Realizado (MM) … R$ 35,1",
     "-15.78", "-47.93", "Alupar TCN transmission project Brazil (Brasília HQ pin)."),
]:
    row_doc(
        rid, "energy", "power_plants_grid", "allied",
        f"Alupar — {name} CapEx Realizado R${val/1e6:.1f}m (2T26 table)",
        "Brazil",
        f"6 Aug 2026 Alupar Investimento 2T26 earnings release: Projetos de Transmissão em Implantação — {name} CAPEX Realizado R${val/1e6:,.1f} million (vs CAPEX Previsto already logged). CapEx: enter cumulative realized face. Nested under implantation portfolio; distinct from Custo de Infraestrutura 2T26 R$379.2m period spend.",
        str(val), "2026-08-06", "2026", lat, lon, geo,
        "alupar_2t26_release_20260806", quote, ALUPAR_URL,
        f"Actor: Alupar Investimento — allied. NEW {name} CapEx Realizado. Shuffle power_plants_grid; allied equal-budget.",
        "hunt_cycle298", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago=ALUPAR_CHICAGO,
        annotation=f"Alupar {name} CapEx Realizado via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Alupar 2T26 RI ZIP PDF; {name} CapEx Realizado R${val/1e6:,.1f}m confirmed.",
    )


def upsert_bib(bib, bib_by, entry):
    sid = entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        old = existing.get("supports") or []
        new = entry["supports"] or []
        merged = list(dict.fromkeys(list(old) + list(new)))
        existing.update({k: v for k, v in entry.items() if k != "supports"})
        existing["supports"] = merged
    else:
        bib.append(entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("entries") or bib.get("sources") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added, updated = [], []
    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            existing = rows[by_id[rid]]
            for k, v in full.items():
                if k != "id" and v != "" and v is not None:
                    existing[k] = v
            updated.append(rid)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
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
    print(f"cycle298 added {len(added)}: {added}")
    print(f"cycle298 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
