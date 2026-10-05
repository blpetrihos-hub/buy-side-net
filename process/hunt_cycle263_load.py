#!/usr/bin/env python3
"""Cycle 263 hunt: shuffle_seed=20261263; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261263).shuffle):
fission_smr, lithium, wind, port_ownership, building_materials, nickel, other_renewables,
balsa, bridges_roads, copper, rail, port_cranes, water, niobium, solar, power_plants_grid,
engineering_epc, graphite.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: spent residual (Equinix/Ascenty/Cirion/Wabtec/EXIM/USTDA dense).
PRC equal-budget: honest residual.
Other: NEW Motiva 2T26 roads CapEx R$1.64bn; NEW Motiva 2T26 rails CapEx R$175m;
  NEW Motiva 1S26 consolidated CapEx R$3.304bn; NEW Motiva 2026 highways CapEx plan R$7.167bn.
Skipped: thin dry; holdovers unsigned; EPR Litoral without openable company dual URL.
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


# 1. bridges_roads / other — NEW Motiva 2T26 roads CapEx R$1.64bn
row_doc(
    "motiva_2t26_roads_capex_1640m_brl",
    "infrastructure", "bridges_roads", "other",
    "Motiva — 2T26 roads CapEx R$1.64bn",
    "Brazil",
    "29 Jul 2026 Motiva company news (2T26): Capex R$1.83bn on highway and rail concessions (+13.2%); of which R$1.64bn applied to highway works (capacity expansion SP/RJ rural; Serra das Araras >75% physical; Paraná pavement; ViaSul BR-101/290/386; Pantanal). CapEx: enter R$1.64bn roads face. Nested vs 1S26 consolidated / 2026 highways plan (not additive).",
    "1640000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Motiva Brazil highway concession portfolio (São Paulo HQ pin; RioSP/Serra das Araras cited).",
    "motiva_2t26_company_news_20260729",
    "No segundo trimestre de 2026, a Companhia executou um Capex de R$ 1,83 bilhão em suas concessões de rodovias e trilhos, crescimento de 13,2% … No acumulado do primeiro semestre de 2026 … alta foi de 16,7%, para R$ 3,304 bilhões. No segundo trimestre de 2026, foram aplicados R$ 1,64 bilhão em obras de rodovias, com destaque para a ampliação de capacidade das vias em regiões rurais de São Paulo e Rio de Janeiro, além dos avanços nos trabalhos na Serra das Araras.",
    "https://www.motiva.com.br/noticias/motiva-lucro-liquido-2-trimestre-2026/",
    "Actor: Motiva S.A. (ex-CCR; Brazilian mobility concessionaire) — other. NEW nested 2T26 roads CapEx R$1.64bn. Shuffle bridges_roads.",
    "hunt_cycle263", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1640000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva S.A. “Motiva amplia resultado em 57,5% e mantém trajetória de crescimento.” July 29, 2026. https://www.motiva.com.br/noticias/motiva-lucro-liquido-2-trimestre-2026/.',
    annotation="Motiva 2T26 roads/rails CapEx and 1S26 consolidated via Fed H.10. Supports motiva_2t26_roads_capex_1640m_brl; motiva_2t26_rails_capex_175m_brl; motiva_1s26_capex_3304m_brl.",
    evid_note="Opened Motiva company Portuguese 2T26 news; Capex R$1.83bn total with R$1.64bn roads / R$175m rails and 1S26 R$3.304bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. rail / other — NEW Motiva 2T26 rails CapEx R$175m
row_doc(
    "motiva_2t26_rails_capex_175m_brl",
    "infrastructure", "rail", "other",
    "Motiva — 2T26 rails CapEx R$175m",
    "Brazil",
    "29 Jul 2026 Motiva company news (2T26): Em Trilhos, a Companhia executou R$175 milhões (ViaMobilidade lines cited in companion results materials). CapEx: enter R$175m rails face within R$1.83bn roads+rails CapEx. Nested vs 1S26 consolidated (not additive).",
    "175000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Motiva urban rail concessions (São Paulo ViaMobilidade footprint pin).",
    "motiva_2t26_company_news_20260729",
    "No segundo trimestre de 2026, a Companhia executou um Capex de R$ 1,83 bilhão em suas concessões de rodovias e trilhos … foram aplicados R$ 1,64 bilhão em obras de rodovias … Em Trilhos, a Companhia executou R$ 175 milhões.",
    "https://www.motiva.com.br/noticias/motiva-lucro-liquido-2-trimestre-2026/",
    "Actor: Motiva S.A. — other. NEW nested 2T26 rails CapEx R$175m. Shuffle rail.",
    "hunt_cycle263", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(175000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva S.A. “Motiva amplia resultado em 57,5% e mantém trajetória de crescimento.” July 29, 2026. https://www.motiva.com.br/noticias/motiva-lucro-liquido-2-trimestre-2026/.',
    annotation="Motiva 2T26 roads/rails CapEx and 1S26 consolidated via Fed H.10. Supports motiva_2t26_roads_capex_1640m_brl; motiva_2t26_rails_capex_175m_brl; motiva_1s26_capex_3304m_brl.",
    evid_note="Opened Motiva company 2T26 news; Trilhos CapEx R$175m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. bridges_roads / other — NEW Motiva 1S26 consolidated CapEx R$3.304bn
row_doc(
    "motiva_1s26_capex_3304m_brl",
    "infrastructure", "bridges_roads", "other",
    "Motiva — 1S26 CapEx R$3.304bn (roads+rails)",
    "Brazil",
    "29 Jul 2026 Motiva company news (2T26): 1S26 Capex R$3.304 billion (+16.7% vs 1S25) across highway and rail concessions. CapEx: enter R$3.304bn 1S26 face. Nested vs 2T26 roads/rails split rows (not additive).",
    "3304000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Motiva Brazil roads+rails concession portfolio (São Paulo HQ pin).",
    "motiva_2t26_company_news_20260729",
    "No acumulado do primeiro semestre de 2026 frente ao mesmo período de 2025, a alta foi de 16,7%, para R$ 3,304 bilhões.",
    "https://www.motiva.com.br/noticias/motiva-lucro-liquido-2-trimestre-2026/",
    "Actor: Motiva S.A. — other. NEW nested 1S26 CapEx R$3.304bn. Shuffle bridges_roads.",
    "hunt_cycle263", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(3304000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva S.A. “Motiva amplia resultado em 57,5% e mantém trajetória de crescimento.” July 29, 2026. https://www.motiva.com.br/noticias/motiva-lucro-liquido-2-trimestre-2026/.',
    annotation="Motiva 2T26 roads/rails CapEx and 1S26 consolidated via Fed H.10. Supports motiva_2t26_roads_capex_1640m_brl; motiva_2t26_rails_capex_175m_brl; motiva_1s26_capex_3304m_brl.",
    evid_note="Opened Motiva company 2T26 news; 1S26 Capex R$3.304bn (+16.7%) confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. bridges_roads / other — NEW Motiva 2026 highways CapEx plan R$7.167bn
row_doc(
    "motiva_2026_highways_plan_7167m_brl",
    "infrastructure", "bridges_roads", "other",
    "Motiva — 2026 highways CapEx plan R$7.167bn",
    "Brazil",
    "Feb 2026 Motiva 2025 results / 2026 investment plan coverage citing company breakdown: highways CapEx plan R$7.167 billion for 2026 (RioSP R$1.67bn; Pantanal R$1.1bn; Sorocabana R$935m; ViaSul R$667m among largest); total mobility CapEx plan R$8.33bn including rails R$1.05bn. CapEx: enter R$7.167bn highways plan face. Distinct from 1S26/2T26 spent rows.",
    "7167000000", "2026-02-10", "2026", "-23.55", "-46.63",
    "Motiva Brazil highway portfolio (São Paulo HQ pin; RioSP/Pantanal/Sorocabana/ViaSul cited).",
    "motiva_2026_investment_plan_oe_20260210",
    "Os gastos totais somam R$ 8,33 bilhões. … os investimentos em rodovias em 2026 sobem quase R$ 1 bilhão, para R$ 7,16 bilhões … RioSP R$ 1,67 bi … Pantanal R$ 1,10 bi … Sorocabana R$ 935 mi … ViaSul R$ 667 mi … Total: R$ 7,16 bilhões.",
    "https://revistaoe.com.br/motiva-investimentos-2026/",
    "Actor: Motiva S.A. — other. NEW 2026 highways CapEx plan R$7.167bn (trade press citing company plan table). Shuffle bridges_roads.",
    "hunt_cycle263", investment_type="capex_plan", evidence="proxy", currency="BRL",
    value_usd=str(round(7167000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Revista O Empreiteiro. “Motiva prevê R$ 8,33 bilhões em investimentos em 2026.” February 10, 2026. https://revistaoe.com.br/motiva-investimentos-2026/.',
    annotation="Motiva 2026 highways CapEx plan ~R$7.16bn via Fed H.10 (UNVERIFIED proxy trade press of company table). Supports motiva_2026_highways_plan_7167m_brl.",
    evid_note="Opened Revista OE Motiva 2026 investment plan article with concession CapEx table totaling R$7.16bn highways; mark proxy (trade press). CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)


def upsert_bib(bib, bib_by, bib_e):
    sid = bib_e["id"]
    entry = {
        "id": sid,
        "type": bib_e.get("type", "company"),
        "chicago": bib_e["chicago"],
        "url": bib_e["url"],
        "annotation": bib_e.get("annotation", ""),
        "supports": bib_e.get("supports", []),
    }
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
    print(f"cycle263 added {len(added)}: {added}")
    print(f"cycle263 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
