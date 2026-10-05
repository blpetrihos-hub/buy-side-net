#!/usr/bin/env python3
"""Cycle 247 hunt: shuffle_seed=20261247; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261247).shuffle):
port_ownership, balsa, lithium, solar, other_renewables, graphite, bridges_roads,
niobium, power_plants_grid, wind, fission_smr, rail, engineering_epc, water,
port_cranes, nickel, building_materials, copper.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Equinix Brazil AI-infrastructure CapEx USD 234m
  (company blog; nested vs Brazil USD 270m / LatAm USD 419m envelopes).
PRC equal-budget: NEW CPFL smart-meter program R$1.2bn through 2029 (company).
Allied: NEW ENGIE Brasil Energia FY2025 CapEx R$6bn (company).
Other: NEW Equatorial Quantum smart-grid pilot >R$170m (O Tempo press).
Skipped: Equatorial ADMS company pages 403/Incapsula; Sungrow–BHP no CapEx face;
  holdovers unsigned; thin dry.
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


# 1. engineering_epc / us — NEW Equinix Brazil AI CapEx USD 234m
row_doc(
    "equinix_brazil_234m_ai_2026",
    "infrastructure", "engineering_epc", "us",
    "Equinix — Brazil AI-infrastructure CapEx package (SP6/SP7/SP4/RJ3)",
    "Brazil",
    "15 Apr 2026 Equinix Interconnections blog (Managing Director Brazil): made USD 234 million in total recent investments to strengthen AI infrastructure in Brazil — SP6 (opening), upcoming SP7, and expansions of SP4 and RJ3. CapEx: enter USD 234m face. Nested vs equinix_brazil_270m_2025_2026 / equinix_latam_419m_2025_2026 / site rows SP6/RJ3.",
    "234000000", "2026-04-15", "2026", "-23.48", "-46.85",
    "Equinix Brazil IBX portfolio (São Paulo metro pin).",
    "equinix_brazil_234m_ai_20260415",
    "We've made $234 million in total recent investments to strengthen the infrastructure needed to support AI in Brazil. This includes: Equinix SP6, our newest data center in São Paulo, which opens its doors today; The upcoming Equinix SP7 data center in São Paulo; Expansions to existing data centers (Equinix SP4 in São Paulo and Equinix RJ3 in Rio de Janeiro).",
    "https://blog.equinix.com/blog/2026/04/15/brazil-from-regional-leader-to-global-ai-infrastructure-hub/",
    "Actor: Equinix (U.S.) — us. NEW nested AI CapEx package USD 234m. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle247", investment_type="greenfield_plant", evidence="documented", currency="USD",
    chicago='Arnaud, Victor. “Brazil: From Regional Leader to Global AI Infrastructure Hub.” Equinix Interconnections, April 15, 2026. https://blog.equinix.com/blog/2026/04/15/brazil-from-regional-leader-to-global-ai-infrastructure-hub/.',
    annotation="Equinix Brazil AI NEW USD 234m nested. Supports equinix_brazil_234m_ai_2026.",
    evid_note="Opened Equinix English blog; USD 234m recent Brazil AI investments / SP6/SP7/SP4/RJ3 confirmed.",
)

# 2. power_plants_grid / prc — NEW CPFL smart meters R$1.2bn
row_doc(
    "cpfl_smart_meters_1p2bn_brl_2025_2029",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia — smart-meter / telemedição program (Paulista/Piratininga/Santa Cruz)",
    "Brazil",
    "26 Feb 2025 CPFL company: plans to replace about 1.6 million conventional meters with smart meters across CPFL Paulista, Piratininga and Santa Cruz through 2029; projected investment R$ 1.2 billion (of which R$ 800 million from BNDES Mais Inovação); ~400 thousand consumers per year. CapEx: enter R$1.2bn face. Distinct from cpfl_fy2025_capex_6p1bn / RGE 9.3bn / group 31.1bn plan.",
    "1200000000", "2025-02-26", "2025", "-23.55", "-46.63",
    "CPFL Paulista / Piratininga / Santa Cruz concessions (São Paulo pin).",
    "cpfl_smart_meters_1p2bn_20250226",
    "Com uma projeção de investimento de R$ 1,2 bilhão, dos quais R$ 800 milhões são provenientes do programa BNDES Mais Inovação, a iniciativa beneficiará aproximadamente 400 mil consumidores por ano.",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-preve-investir-r-12-bilhao-em-projeto-de-medidores-inteligentes",
    "Actor: CPFL Energia (State Grid–controlled) — prc. NEW row: company Portuguese smart-meter CapEx R$1.2bn. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle247", investment_type="modernization", evidence="documented", currency="BRL",
    value_usd=str(round(1200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia. “CPFL Energia prevê investir R$ 1,2 bilhão em projeto de medidores inteligentes.” February 26, 2025. https://www.grupocpfl.com.br/noticia/cpfl-energia-preve-investir-r-12-bilhao-em-projeto-de-medidores-inteligentes.',
    annotation="CPFL smart meters NEW R$1.2bn ~USD 231.12m via Fed H.10. Supports cpfl_smart_meters_1p2bn_brl_2025_2029.",
    evid_note="Opened CPFL Portuguese; R$1.2bn / 1.6m meters / BNDES R$800m / three SP distributors confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / allied — NEW ENGIE FY2025 CapEx R$6bn
row_doc(
    "engie_fy2025_capex_6bn_brl",
    "energy", "power_plants_grid", "allied",
    "ENGIE Brasil Energia — FY2025 CapEx R$6bn (generation + transmission)",
    "Brazil",
    "25 Feb 2026 ENGIE Brasil Energia company: in the period invested R$ 6 billion in acquisition of new hydroelectric assets, modernization works, project implantation and revitalization of the generating fleet (FY2025). CapEx: enter R$6bn face. Distinct from engie_asa_branca_tx_2p7bn_2025 / Jari–Cachoeira Caldeirão ~R$2.9bn acquisition nested in same release.",
    "6000000000", "2026-02-25", "2025", "-27.59", "-48.55",
    "ENGIE Brasil Energia portfolio (Florianópolis / multi-state pin).",
    "engie_fy2025_capex_6bn_20260225",
    "No período, a Companhia investiu R$ 6 bilhões na aquisição de novos ativos hidrelétricos, em obras de modernização, na implantação de projetos e na revitalização do parque gerador.",
    "https://www.engie.com.br/imprensa/press-releases/engie-brasil-energia-cresce-146-em-receita-e-investe-r-6-bilhoes-em-2025/",
    "Actor: ENGIE Brasil Energia (France) — allied. NEW row: company Portuguese FY2025 CapEx R$6bn. Shuffle power_plants_grid.",
    "hunt_cycle247", investment_type="modernization", evidence="documented", currency="BRL",
    value_usd=str(round(6000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ENGIE Brasil Energia. “ENGIE Brasil Energia cresce 14,6% em receita e investe R$ 6 bilhões em 2025.” February 25, 2026. https://www.engie.com.br/imprensa/press-releases/engie-brasil-energia-cresce-146-em-receita-e-investe-r-6-bilhoes-em-2025/.',
    annotation="ENGIE FY2025 NEW R$6bn ~USD 1155.60m via Fed H.10. Supports engie_fy2025_capex_6bn_brl.",
    evid_note="Opened ENGIE Portuguese; R$6bn FY2025 CapEx / hydro acquisition / modernization confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / other — NEW Equatorial Quantum >R$170m (press)
row_doc(
    "equatorial_quantum_170m_brl_2026",
    "energy", "power_plants_grid", "other",
    "Equatorial — Projeto Quantum smart-grid pilot (Barreirinhas MA / Canaã dos Carajás PA)",
    "Brazil",
    "19 Jun 2026 O Tempo (citing Equatorial): Projeto Quantum digital transformation / smart-grid pilot will receive investment of more than R$ 170 million; initial tests in Barreirinhas (MA) and Canaã dos Carajás (PA) with remote network monitoring. CapEx: enter R$170m soft floor.",
    "170000000", "2026-06-19", "2026", "-2.75", "-42.83",
    "Equatorial Quantum pilot — Barreirinhas (MA) pin (multi-state program).",
    "otempo_equatorial_quantum_170m_20260619",
    "O Grupo Equatorial anunciou o início do projeto Quantum, uma iniciativa de transformação digital voltada para a implementação de tecnologias de redes inteligentes (smart grids). O projeto-piloto receberá um investimento superior a R$ 170 milhões e será testado inicialmente nos municípios de Barreirinhas (MA) e Canaã dos Carajás (PA), com foco no monitoramento remoto da rede elétrica.",
    "https://www.otempo.com.br/economia/2026/6/19/grupo-equatorial-investe-r-170-milhoes-em-projeto-de-redes-inteligentes",
    "Actor: Equatorial Energia (Brazilian multi-utility) — other. NEW row: press CapEx >R$170m Quantum pilot (UNVERIFIED press). Shuffle power_plants_grid.",
    "hunt_cycle247", investment_type="modernization", evidence="press", currency="BRL",
    value_usd=str(round(170000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Neves, Marco Aurélio. “Grupo Equatorial investe R$ 170 milhões em projeto de redes inteligentes.” O Tempo, June 19, 2026. https://www.otempo.com.br/economia/2026/6/19/grupo-equatorial-investe-r-170-milhoes-em-projeto-de-redes-inteligentes.',
    annotation="Equatorial Quantum NEW >R$170m floor ~USD 32.74m via Fed H.10 (press). Supports equatorial_quantum_170m_brl_2026.",
    evid_note="Opened O Tempo Portuguese; >R$170m Quantum pilot / Barreirinhas + Canaã dos Carajás confirmed. CapEx enter R$170m soft floor; USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle247 added {len(added)}: {added}")
    print(f"cycle247 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
