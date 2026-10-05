#!/usr/bin/env python3
"""Cycle 246 hunt: shuffle_seed=20261246; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261246).shuffle):
solar, graphite, wind, fission_smr, rail, bridges_roads, port_cranes,
engineering_epc, copper, niobium, nickel, other_renewables, balsa, lithium,
building_materials, water, power_plants_grid, port_ownership.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Equinix Brazil 2025–26 CapEx breakout USD 270m
  (nested vs equinix_latam_419m envelope; company Portuguese newsroom).
PRC equal-budget: NEW CPFL RGE distribution CapEx R$9.3bn 2025–2029 (company).
Allied: NEW Neoenergia Coelba Bahia R$25bn 2026–2030; NEW Neoenergia Pernambuco
  R$9.7bn 2026–2030.
Skipped: Progress Rail R$430m Teclemídia press conflicts with VLI R$200m eight-loco
  CapEx already logged; Sungrow–BHP Escondida/Spence no CapEx face; holdovers
  unsigned; thin dry.
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


# 1. engineering_epc / us — NEW Equinix Brazil USD 270m 2025–26 breakout
row_doc(
    "equinix_brazil_270m_2025_2026",
    "infrastructure", "engineering_epc", "us",
    "Equinix — Brazil data-center CapEx breakout (2025–2026)",
    "Brazil",
    "26 May 2026 Equinix Portuguese newsroom: between 2025 and 2026 announced and executed investments exceeding USD 419 million across LatAm, including Brazil USD 270 million (Mexico 81 / Chile 42 / Colombia 28). CapEx: enter USD 270m Brazil breakout face. Nested vs equinix_latam_419m_2025_2026 envelope and site rows SP6/RJ3.",
    "270000000", "2026-05-26", "2026", "-23.48", "-46.85",
    "Equinix Brazil IBX portfolio (São Paulo metro pin).",
    "equinix_latam_brazil_270m_20260526",
    "Entre 2025 e 2026, a Equinix anunciou e executou investimentos superiores a USD 419 milhões em mercados estratégicos da América Latina, incluindo México (USD 81 milhões), Brasil (USD 270 milhões), Chile (USD 42 milhões) e Colômbia (USD 28 milhões).",
    "https://newsroom.equinix.com/2026-05-26-America-Latina-e-a-regiao-de-maior-crescimento-e-mais-dinamica-para-a-Equinix",
    "Actor: Equinix (U.S.) — us. NEW nested Brazil CapEx breakout USD 270m. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle246", investment_type="greenfield_plant", evidence="documented", currency="USD",
    chicago='Equinix. “América Latina é a região de maior crescimento e mais dinâmica para a Equinix.” May 26, 2026. https://newsroom.equinix.com/2026-05-26-America-Latina-e-a-regiao-de-maior-crescimento-e-mais-dinamica-para-a-Equinix.',
    annotation="Equinix Brazil NEW USD 270m nested. Supports equinix_brazil_270m_2025_2026.",
    evid_note="Opened Equinix Portuguese newsroom; Brazil USD 270m within LatAm >USD 419m confirmed.",
)

# 2. power_plants_grid / prc — NEW CPFL RGE R$9.3bn 2025–2029
row_doc(
    "cpfl_rge_9p3bn_brl_2025_2029",
    "energy", "power_plants_grid", "prc",
    "CPFL RGE — Rio Grande do Sul distribution CapEx R$9.3bn (2025–2029)",
    "Brazil",
    "23 Feb 2026 CPFL company (Região Central investments page): investments in the Central region are part of the amount planned in the 2025–2029 cycle, which provides for R$ 9.3 billion in investments for CPFL RGE alone. CapEx: enter R$9.3bn face. Distinct from cpfl_fy2025_capex_6p1bn_brl group executed / cpfl_capex_plan_31p1bn_2026_2030 group plan.",
    "9300000000", "2026-02-23", "2026", "-30.03", "-51.23",
    "CPFL RGE Rio Grande do Sul concession (Porto Alegre pin).",
    "cpfl_rge_9p3bn_20260223",
    "Os investimentos na região Central fazem parte do montante previsto no ciclo 2025–2029, que prevê R$ 9,3 bilhões em investimentos apenas na CPFL RGE.",
    "https://www.grupocpfl.com.br/noticia/regiao-central-recebe-r-163-milhoes-em-investimentos-na-rede-eletrica",
    "Actor: CPFL RGE (State Grid–controlled CPFL Energia) — prc. NEW row: company Portuguese RGE R$9.3bn 2025–2029. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle246", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(9300000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia. “Região Central recebe R$ 163 milhões em investimentos na rede elétrica.” February 23, 2026. https://www.grupocpfl.com.br/noticia/regiao-central-recebe-r-163-milhoes-em-investimentos-na-rede-eletrica.',
    annotation="CPFL RGE NEW R$9.3bn ~USD 1791.18m via Fed H.10. Supports cpfl_rge_9p3bn_brl_2025_2029.",
    evid_note="Opened CPFL Portuguese; R$9.3bn RGE 2025–2029 cycle confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / allied — NEW Neoenergia Coelba Bahia R$25bn
row_doc(
    "neoenergia_coelba_25bn_brl_2026_2030",
    "energy", "power_plants_grid", "allied",
    "Neoenergia Coelba — Bahia distribution CapEx ~R$25bn (2026–2030)",
    "Brazil",
    "8 Jun 2026 Neoenergia company: through Neoenergia Coelba will invest about R$ 25 billion by 2030 in expansion, modernization and reinforcement of Bahia electricity distribution infrastructure (within group R$50bn 2026–2030 plan). CapEx: enter R$25bn face. Distinct from neoenergia_dist_50bn envelope / Oeste Baiano nested / Cosern / Pernambuco.",
    "25000000000", "2026-06-08", "2026", "-12.97", "-38.51",
    "Neoenergia Coelba Bahia concession (Salvador pin).",
    "neoenergia_coelba_25bn_20260608",
    "A Neoenergia, por meio da Neoenergia Coelba, vai investir cerca de R$ 25 bilhões até 2030 na expansão, modernização e no reforço da infraestrutura de distribuição de energia elétrica da Bahia.",
    "https://www.neoenergia.com/w/investimentos-bahia-farm-show-bilhoes-energia-2030-coelba",
    "Actor: Neoenergia (Iberdrola Spain) — allied. NEW row: company Portuguese Coelba ~R$25bn through 2030. Shuffle power_plants_grid.",
    "hunt_cycle246", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(25000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia. “Neoenergia vai investir R$ 25 bilhões na Bahia até 2030.” June 8, 2026. https://www.neoenergia.com/w/investimentos-bahia-farm-show-bilhoes-energia-2030-coelba.',
    annotation="Neoenergia Coelba NEW ~R$25bn ~USD 4815.01m via Fed H.10. Supports neoenergia_coelba_25bn_brl_2026_2030.",
    evid_note="Opened Neoenergia Portuguese; ~R$25bn Bahia / within R$50bn group plan confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / allied — NEW Neoenergia Pernambuco R$9.7bn
row_doc(
    "neoenergia_pernambuco_9p7bn_brl_2026_2030",
    "energy", "power_plants_grid", "allied",
    "Neoenergia Pernambuco — state distribution CapEx R$9.7bn (2026–2030)",
    "Brazil",
    "10 Jul 2026 Neoenergia Pernambuco company: broader plan provides for R$ 9.7 billion in contributions between 2026 and 2030 (+123% vs prior cycle); 25 new substations / 34 expansions / 766 MVA / >9 thousand km networks. CapEx: enter R$9.7bn face. Distinct from neoenergia_dist_50bn / Coelba 25bn / Cosern 4.1bn.",
    "9700000000", "2026-07-10", "2026", "-8.05", "-34.88",
    "Neoenergia Pernambuco concession (Recife pin).",
    "neoenergia_pernambuco_9p7bn_20260710",
    "Os investimentos no Agreste e na Zona da Mata fazem parte de um plano mais amplo anunciado pela Neoenergia Pernambuco, que prevê R$ 9,7 bilhões em aportes entre 2026 e 2030. Trata-se do maior programa de investimentos já realizado pela distribuidora no Estado e representa um crescimento de 123% em relação ao ciclo anterior.",
    "https://www.neoenergia.com/web/pernambuco/w/investimento-sertao-plano-recorde-pernambuco-1",
    "Actor: Neoenergia (Iberdrola Spain) — allied. NEW row: company Portuguese Pernambuco R$9.7bn through 2030. Shuffle power_plants_grid.",
    "hunt_cycle246", investment_type="concession", evidence="documented", currency="BRL",
    value_usd=str(round(9700000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia Pernambuco. “Neoenergia Pernambuco investirá R$ 2,8 bilhões no Sertão em plano recorde de R$ 9,7 bilhões até 2030, no Estado.” July 10, 2026. https://www.neoenergia.com/web/pernambuco/w/investimento-sertao-plano-recorde-pernambuco-1.',
    annotation="Neoenergia Pernambuco NEW R$9.7bn ~USD 1868.22m via Fed H.10. Supports neoenergia_pernambuco_9p7bn_brl_2026_2030.",
    evid_note="Opened Neoenergia Pernambuco Portuguese; R$9.7bn 2026–2030 / +123% / 25+34 substations confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle246 added {len(added)}: {added}")
    print(f"cycle246 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
