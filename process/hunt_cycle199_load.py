#!/usr/bin/env python3
"""Cycle 199 hunt: shuffle_seed=20261199; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261199).shuffle):
rail, niobium, engineering_epc, other_renewables, port_cranes, solar, wind,
fission_smr, copper, balsa, lithium, bridges_roads, port_ownership, graphite,
water, power_plants_grid, building_materials, nickel.

Thin top-up (recomputed): balsa / nickel / fission_smr — all dry.
≥1/3 U.S. hunt budget spent on Ascenty LatAm CapEx, EXIM/DFC/AES/Wabtec/
Progress Rail / Freeport sweeps — 1 new U.S. row (Ascenty).
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
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


# 1. engineering_epc / us — Ascenty USD 1bn approved 2026 CapEx (BR/MX/CL)
row_doc(
    "ascenty_2026_capex_1bn_latam",
    "infrastructure",
    "engineering_epc",
    "us",
    "Ascenty (Digital Realty / Brookfield) — 2026 approved LatAm CapEx plan",
    "Brazil",
    "Ascenty English company release: approved investments of USD 1 billion for 2026 across Brazil, Mexico and Chile (25 operating data centers); cites SPO05 (~R$300m; already logged), SPO06 and SLC04 Chile among 13 projects under development. CapEx plan face = USD 1bn. Distinct from ascenty_ai_1p2bn_brazil_2026 (May 2026 AI hyperscale package) and SPO05/SPO06 project-level rows (within-envelope; not additive).",
    "1000000000",
    "2026-01-01",
    "2026",
    "",
    "",
    "Ascenty Brazil/Mexico/Chile multi-site 2026 CapEx plan (national multi-campus — lat/lon blank).",
    "ascenty_growth_revenue_1bn_2026",
    "To sustain this pace, the company has US$ 1 billion in approved investments for 2026 across Brazil, Mexico, and Chile—countries where it already operates 25 data centers.",
    "https://ascenty.com/en/blog/news-ascenty-en/ascenty-growth-revenue/",
    "Actor: Ascenty JV Digital Realty (U.S.) + Brookfield Infrastructure — us. Company English primary. CapEx plan = USD 1bn. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle199",
    investment_type="capex_plan",
    evidence="documented",
    currency="USD",
    value_usd="1000000000",
    fx_usd="1",
    bib_type="company",
    chicago='Ascenty. “Ascenty Achieves Over 30% Growth in Enterprise Revenue in 2025 and Accelerates Expansion with a US$ 1 Billion Investment.” https://ascenty.com/en/blog/news-ascenty-en/ascenty-growth-revenue/.',
    annotation="Ascenty: USD 1bn approved 2026 LatAm CapEx. Supports ascenty_2026_capex_1bn_latam.",
    evid_note="Opened Ascenty English company primary 2026-10-04; USD 1bn 2026 approved CapEx confirmed.",
)

# 2. copper / other — Vale Bacaba USD 290m
row_doc(
    "vale_bacaba_copper_290m_2025",
    "resources",
    "copper",
    "other",
    "Vale Base Metals — Bacaba copper project implementation CapEx (Pará)",
    "Brazil",
    "17 Jun 2025 Vale Base Metals: Preliminary Environmental License for Bacaba copper project in Canaã dos Carajás, Pará; designed to extend Sossego Mining Complex life with ~50 ktpa average copper over 8-year mine life; approximately USD 290 million invested during implementation phase; production start-up planned 1H 2028. CapEx = USD 290m. Distinct from vale_carajas_copper_capex_3p5bn_2026_2030 multi-project schedule (includes Bacaba).",
    "290000000",
    "2025-06-17",
    "2025",
    "-6.53",
    "-49.85",
    "Bacaba / Canaã dos Carajás, Pará (Vale Base Metals geography; approximate municipal pin).",
    "vale_bacaba_license_20250617",
    "Approximately US$ 290 million will be invested during the project’s implementation phase and the production startup is planned for the first half of 2028.",
    "https://valebasemetals.com/news/preliminary-license-issued-for-the-bacaba-copper-project/",
    "Actor: Vale Base Metals / Vale S.A. (Brazilian) — other. Company English primary. CapEx = USD 290m. Shuffle copper.",
    "hunt_cycle199",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="USD",
    value_usd="290000000",
    fx_usd="1",
    bib_type="company",
    chicago='Vale Base Metals. “Preliminary License Issued for the Bacaba Copper Project.” June 17, 2025. https://valebasemetals.com/news/preliminary-license-issued-for-the-bacaba-copper-project/.',
    annotation="Vale Bacaba: USD 290m implementation CapEx. Supports vale_bacaba_copper_290m_2025.",
    evid_note="Opened Vale Base Metals English primary 2026-10-04; USD 290m confirmed.",
)

# 3. copper / other — Vale Carajás copper CapEx schedule USD 3.5bn 2026–2030
row_doc(
    "vale_carajas_copper_capex_3p5bn_2026_2030",
    "resources",
    "copper",
    "other",
    "Vale — Carajás copper growth projects CapEx schedule 2026–2030",
    "Brazil",
    "23 Feb 2026 Vale SEC Form 6-K: updated capital investment schedule for copper projects — annual investments for copper projects in the Carajás region US$0.3bn (2026), US$0.4bn (2027), US$0.8bn (2028), US$0.9bn (2029), US$1.1bn (2030), totaling US$3.5 billion in 2026–2030; based on copper growth projects including Bacaba under implementation. CapEx schedule = USD 3.5bn. Distinct from vale_bacaba_copper_290m_2025 (single-project implementation CapEx).",
    "3500000000",
    "2026-02-23",
    "2026",
    "",
    "",
    "Carajás Mineral Province copper growth package, Pará (multi-project — lat/lon blank).",
    "vale_carajas_cu_capex_6k_20260223",
    "Annual investments for copper projects in the Carajás region: US$ 0.3 billion in 2026; US$ 0.4 billion in 2027; US$ 0.8 billion in 2028; US$ 0.9 billion in 2029 and US$ 1.1 billion in 2030, totaling US$ 3.5 billion in 2026-2030 period.",
    "https://www.sec.gov/Archives/edgar/data/917851/000129281426000464/vale20260223_6k.htm",
    "Actor: Vale S.A. (Brazilian) — other. Company SEC 6-K English primary. CapEx schedule = USD 3.5bn. Shuffle copper.",
    "hunt_cycle199",
    investment_type="capex_plan",
    evidence="documented",
    currency="USD",
    value_usd="3500000000",
    fx_usd="1",
    bib_type="company",
    chicago='Vale S.A. “Vale informs on estimates update.” Form 6-K, February 23, 2026. https://www.sec.gov/Archives/edgar/data/917851/000129281426000464/vale20260223_6k.htm.',
    annotation="Vale: Carajás copper CapEx USD 3.5bn 2026–2030. Supports vale_carajas_copper_capex_3p5bn_2026_2030.",
    evid_note="Opened Vale SEC 6-K English primary 2026-10-04; USD 3.5bn schedule confirmed.",
)

# 4. solar / prc — SPIC Luiz Gonzaga R$400m
row_doc(
    "spic_luiz_gonzaga_400m_brl_2024",
    "energy",
    "solar",
    "prc",
    "SPIC Brasil (70%) / Recurrent Energy — Luiz Gonzaga solar (Pernambuco)",
    "Brazil",
    "4–6 Nov 2024 SPIC Brasil: partnership with Recurrent Energy (Canadian Solar) investing approximately R$ 400 million (~USD 70m company paraphrase) in Luiz Gonzaga solar project at Terra Nova, Pernambuco — SPIC Brasil 70% stake; 114 MWp / ~166,000 panels; COD targeted Nov 2024; BNB financing R$170m / 24 years cited; >90% of generation contracted through 2033. CapEx = R$400m. Distinct from spic_recurrent_marangatu_br_2024 / Panati and SPIC Pedra/Paraíso wind CapEx.",
    "400000000",
    "2024-11-04",
    "2024",
    "-7.83",
    "-39.37",
    "Terra Nova, Pernambuco / Luiz Gonzaga complex (company geography; approximate municipal pin).",
    "spic_luiz_gonzaga_20241106",
    "A SPIC Brasil e Recurrent Energy (“Canadian Solar”) (NASDAQ: CSIQ) anunciaram nesta segunda-feira, 4 de novembro, uma nova parceria envolvendo o investimento de aproximadamente R$ 400 milhões (aprox. $70 milhões) no projeto solar Luiz Gonzaga, instalado em Terra Nova, Pernambuco, no qual a SPIC Brasil terá 70% de participação.",
    "https://www.spicbrasil.com.br/destaque/investimento-complexo-solar-luiz-gonzaga/",
    "Actor: SPIC Brasil (PRC State Power Investment Corp. affiliate) majority 70% — prc; Recurrent Energy (Canadian Solar) 30%. Company Portuguese primary. CapEx = R$400m (BRL stored without FX; company ~USD 70m paraphrase not entered as FX). Shuffle solar.",
    "hunt_cycle199",
    investment_type="ownership_equity",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='SPIC Brasil. “SPIC Brasil anuncia investimento de R$ 400 milhões em novo solar em parceria com a Recurrent Energy.” November 6, 2024. https://www.spicbrasil.com.br/destaque/investimento-complexo-solar-luiz-gonzaga/.',
    annotation="SPIC Luiz Gonzaga: ~R$400m. Supports spic_luiz_gonzaga_400m_brl_2024.",
    evid_note="Opened SPIC Brasil Portuguese company primary 2026-10-04; R$400m confirmed.",
)

# 5. graphite / allied — upgrade Graphcoa Jordânia CapEx to RIMA primary
row_doc(
    "graphcoa_jordania_dfs_capex_2026",
    "resources",
    "graphite",
    "allied",
    "Graphcoa / Appian Capital Brazil — Projeto Grafite Jordânia",
    "Brazil",
    "Graphcoa RIMA PDF (Projeto Grafite Jordânia): estimated implantation investment R$ 621.76 million for integrated natural-graphite mine + concentrator at Jordânia (Jequitinhonha Valley, MG); ~53,000 t/year high-purity concentrate; works Jun 2027–Jun 2029; commissioning Mar–Jun 2029; ops from Jul 2029; ramp-up through Dec 2030; ≥14-year life. Upgrades prior BNamericas press proxy summarizing EIA to company RIMA primary. Distinct from graphcoa_boa_sorte / graphcoa_jordania_mg presence.",
    "621760000",
    "2025-11-01",
    "2026",
    "-15.9",
    "-40.2",
    "Jordânia, Vale do Jequitinhonha, Minas Gerais (RIMA geography).",
    "graphcoa_jordania_rima_2025",
    "O investimento estimado para essa implantação é de R$ 621,76 milhões.",
    "https://graphcoa.com/wp-content/uploads/2025/11/RIMA.pdf",
    "Actor: Graphcoa / Appian Capital Brazil (UK PE) — allied. Company Portuguese RIMA primary CapEx R$621.76m. Upgrades prior BNamericas proxy. Shuffle graphite / thin top-up preference.",
    "hunt_cycle199",
    investment_type="greenfield_mine",
    evidence="documented",
    currency="BRL",
    value_usd="120000000",
    fx_usd="",
    bib_type="company",
    chicago='Graphcoa. “Projeto Grafite Jordânia — Relatório de Impacto Ambiental (RIMA).” https://graphcoa.com/wp-content/uploads/2025/11/RIMA.pdf.',
    annotation="Graphcoa Jordânia RIMA: R$621.76m. Supports graphcoa_jordania_dfs_capex_2026.",
    evid_note="Opened Graphcoa RIMA PDF 2026-10-04; R$621.76m implantation CapEx confirmed; upgrades prior BNamericas proxy.",
)

# 6. solar / other — CHEC Francisco + Doña Juana CapEx COP 60.05bn
row_doc(
    "chec_francisco_juana_60bn_cop_2025",
    "energy",
    "solar",
    "other",
    "CHEC (EPM) — San Francisco + Doña Juana solar parks CapEx (Caldas)",
    "Colombia",
    "15 Feb 2025 La Patria: Central Hidroeléctrica de Caldas (CHEC / Grupo EPM) invests COP 60,050,403,301 (incl. IVA) in Parque Solar San Francisco (Palestina, Caldas) and Parque Solar Doña Juana (La Dorada, Caldas); acta de inicio 22 Jan 2025 with contractor PowerChina International Group Colombia; same dual plant later handed over as POWERCHINA Francisco Juana 15.99 MW (Sep 2026; EPC row already logged without CapEx). CapEx = COP 60.05bn. Distinct from powerchina_francisco_juana_colombia_2026 (PRC EPC handover; CapEx blank).",
    "60050403301",
    "2025-02-15",
    "2025",
    "5.02",
    "-75.67",
    "Pinned to San Francisco / Palestina, Caldas (larger site; La Patria / CHEC geography).",
    "lapatria_chec_francisco_juana_20250215",
    "Con $60 mil 50 millones 403 mil 301 (incluyendo el IVA) la Chec le quita esa etiqueta. Dicha inversión se destina desde inicios del 2025 a los parques solares San Francisco (Palestina, Caldas) y Doña Juana (La Dorada, Caldas).",
    "https://www.lapatria.com/caldas/caldas-multinacional-china-y-la-chec-construyen-dos-parques-solares-por-60-mil-millones-asi",
    "Actor: CHEC / Grupo EPM (Colombian) — other; PowerChina EPC already on separate PRC row. UNVERIFIED proxy: La Patria 15 Feb 2025 citing CHEC investment figure. CapEx stored as COP without FX. Shuffle solar.",
    "hunt_cycle199",
    investment_type="greenfield_generation",
    evidence="proxy",
    currency="COP",
    value_usd="",
    fx_usd="",
    bib_type="press",
    chicago='Carmona Caraballo, Santiago. “Caldas: multinacional china y la Chec construyen dos parques solares por $60 mil millones.” La Patria, February 15, 2025. https://www.lapatria.com/caldas/caldas-multinacional-china-y-la-chec-construyen-dos-parques-solares-por-60-mil-millones-asi.',
    annotation="CHEC Francisco/Juana CapEx COP 60.05bn. Supports chec_francisco_juana_60bn_cop_2025.",
    evid_note="Opened La Patria Spanish press 2026-10-04; COP 60,050,403,301 incl. IVA cited; UNVERIFIED proxy for CHEC figure.",
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
    print(f"cycle199 added {len(added)}: {added}")
    print(f"cycle199 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
