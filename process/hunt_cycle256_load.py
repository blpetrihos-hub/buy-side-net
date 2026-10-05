#!/usr/bin/env python3
"""Cycle 256 hunt: shuffle_seed=20261256; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261256).shuffle):
power_plants_grid, balsa, building_materials, solar, copper, water, other_renewables,
engineering_epc, graphite, port_ownership, niobium, rail, bridges_roads, wind, lithium,
nickel, port_cranes, fission_smr.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: spent (Atlas 3bn refi / Ascenty 1bn / ODATA DeltaFlow already
  logged; ODATA SP04 >R$2.6bn without openable company CapEx primary distinct from
  DeltaFlow) — honest residual.
PRC equal-budget: honest residual (CPFL nested C254; Sinoma/Votorantim Z02 already).
Other: NEW Cemig 1S26 CapEx R$3.28bn; NEW Votorantim Cimentos 2T26 CapEx R$803m.
Skipped: thin dry; ISA 2T26 CapEx only on investidor10 mirror; holdovers unsigned.
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


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid, layer, subcategory, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, source_id, quote, url, note, hunt_support,
    investment_type="epc", evidence="documented", currency="USD", value_usd=None,
    fx_usd=None, chicago=None, bib_type="company", annotation=None, evid_note=None,
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
            "fx_date": fx_date if value_usd else "", "year": year, "status": "active",
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


# 1. power_plants_grid / other — NEW Cemig 1S26 CapEx R$3.28bn
row_doc(
    "cemig_1s26_capex_3p28bn_brl",
    "energy", "power_plants_grid", "other",
    "Cemig — 1S26 CapEx R$3.28bn",
    "Brazil",
    "Cemig 1S26 / 2T26 results presentation (company RI PDF dated 2026-06-30 path): Capex realizado de R$3,28 bilhões no 1S26 (+19.2% vs 1S25), with regulated-business focus — distribution R$2.64bn (11 new + 3 expanded substations; +1,886 km LV/MV networks); transmission R$275.2m. Of the total, R$1.80bn in 2T26. CapEx: enter R$3.28bn 1S26 face. Nested vs cemig_capex_plan_44bn_brl_2026_2030 envelope (not additive).",
    "3280000000", "2026-06-30", "2026", "-19.92", "-43.94",
    "Cemig Minas Gerais footprint (Belo Horizonte HQ pin).",
    "cemig_1s26_results_presentation_20260630",
    "Capex realizado de R$3,28 bilhões no 1S26 (aumento de 19,2% x 1S25), com destaque para os negócios regulados o Distribuição: R$2,64 bilhões; 11 subestações novas e 3 ampliadas, adição de 1.886 km de redes de baixa e média tensão o Transmissão: R$275,2 milhões",
    "https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf",
    "Actor: Cemig (Minas Gerais state-controlled utility) — other. NEW nested 1S26 CapEx R$3.28bn. Shuffle power_plants_grid.",
    "hunt_cycle256", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(3280000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Cemig. “Teleconferência / Apresentação de Resultados” (1S26 / 2T26). June 30, 2026. https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf.',
    annotation="Cemig 1S26 NEW R$3.28bn ~USD 631.73m via Fed H.10. Supports cemig_1s26_capex_3p28bn_brl.",
    evid_note="Opened Cemig company RI PDF; Capex 1S26 R$3.28bn / distribuição R$2.64bn / transmissão R$275.2m / 2T26 R$1.80bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. building_materials / other — NEW Votorantim Cimentos 2T26 CapEx R$803m
row_doc(
    "votorantim_cimentos_2t26_capex_803m_brl",
    "infrastructure", "building_materials", "other",
    "Votorantim Cimentos — 2T26 CapEx R$803m",
    "Brazil",
    "Votorantim Cimentos company Portuguese 2T26 results page (and companion IR presentation): Capex totaled R$ 803 million in 2T26 (in line with 2T25); 74% sustaining/modernization/efficiency and 26% capacity expansion; Brazil 2024–2028 R$5bn plan with R$3.1bn projects already announced (Xambioá grind line R$260m nested separately). CapEx: enter R$803m 2T26 face. Distinct from votorantim_brazil_plan_3p1bn_invested_2026 / Xambioá / Nobres project rows.",
    "803000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Votorantim Cimentos Brazil footprint (São Paulo HQ pin).",
    "votorantim_cimentos_2t26_results_2026",
    "Nossos investimentos (Capex) totalizaram R$ 803 milhões no 2T26, em linha com o montante do 2T25. Desconsiderando os efeitos da variação cambial na conversão dos investimentos realizados no exterior, o CAPEX apresentaria crescimento na comparação anual. Do total investido no trimestre, 74% foram destinados a projetos de sustentação (sustaining), modernização e eficiência operacional, enquanto 26% foram direcionados a projetos de expansão de capacidade.",
    "https://www.votorantimcimentos.com.br/noticia/nossos-resultados-financeiros-no-segundo-trimestre-de-2026/",
    "Actor: Votorantim Cimentos (Brazilian cement) — other. NEW nested 2T26 CapEx R$803m. Shuffle building_materials.",
    "hunt_cycle256", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(803000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Votorantim Cimentos. “Nossos resultados financeiros no segundo trimestre de 2026.” 2026. https://www.votorantimcimentos.com.br/noticia/nossos-resultados-financeiros-no-segundo-trimestre-de-2026/.',
    annotation="Votorantim Cimentos 2T26 NEW R$803m ~USD 154.66m via Fed H.10. Supports votorantim_cimentos_2t26_capex_803m_brl.",
    evid_note="Opened Votorantim Cimentos Portuguese 2T26 results page (IR presentation corroborates Capex 803); 74%/26% sustaining/expansion split confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle256 added {len(added)}: {added}")
    print(f"cycle256 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
