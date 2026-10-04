#!/usr/bin/env python3
"""Cycle 198 hunt: shuffle_seed=20261198; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261198).shuffle):
rail, lithium, solar, other_renewables, niobium, graphite, wind, port_cranes,
building_materials, port_ownership, balsa, water, nickel, copper,
engineering_epc, power_plants_grid, fission_smr, bridges_roads.

Thin top-up (recomputed): balsa / nickel / fission_smr — all dry.
≥1/3 U.S. hunt budget spent on Amazon Brazil 2025 CapEx, Wabtec/EXIM/Freeport/
AES sweeps — 1 new U.S. row (Amazon).
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


# 1. engineering_epc / us — Amazon Brazil 2025 investments >R$19bn
row_doc(
    "amazon_brazil_invest_19bn_brl_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Amazon — Brazil 2025 investments (infra / logistics / cloud / tech)",
    "Brazil",
    "4 Aug 2026 About Amazon Brasil: since 2012 Amazon invested more than R$ 75 billion in Brazil; in 2025 alone investments exceeded R$ 19 billion (~5× historical annual average) across infrastructure, logistics, technology, cloud services (AWS), skilling and entrepreneurship. CapEx/invest face for 2025 = R$19bn floor. Distinct from aws_chile_region_4bn_2025 and Microsoft Brazil R$14.7bn cloud/AI package.",
    "19000000000",
    "2026-08-04",
    "2025",
    "",
    "",
    "Amazon Brazil national footprint (logistics + AWS + tech; multi-site — lat/lon blank).",
    "amazon_brasil_invest_20260804",
    "Desde sua chegada ao país, em 2012, a Amazon investiu mais de R$ 75 bilhoes no Brasil em infraestrutura, logística, tecnologia, serviços de nuvem, qualificação profissional e fomento ao empreendedorismo. Somente em 2025, os investimentos ultrapassaram R$19 bilhões — quase cinco vezes a média anual desde o início das operações, o equivalente a mais de R$ 52 milhões por dia.",
    "https://www.aboutamazon.com.br/noticias/noticias-da-empresa/amazon-reforca-compromisso-com-o-brasil-com-operacao-crescente-alinhada-a-estrategia-global",
    "Actor: Amazon.com Inc. (U.S.) — us. Company Portuguese About Amazon Brasil primary. CapEx/invest floor >R$19bn for 2025 (BRL stored without FX); envelope spans logistics+cloud. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle198",
    investment_type="capex_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Amazon. “Amazon reforça compromisso com o Brasil com operação crescente alinhada à estratégia global.” About Amazon Brasil, August 4, 2026. https://www.aboutamazon.com.br/noticias/noticias-da-empresa/amazon-reforca-compromisso-com-o-brasil-com-operacao-crescente-alinhada-a-estrategia-global.',
    annotation="Amazon: Brazil 2025 investments >R$19bn. Supports amazon_brazil_invest_19bn_brl_2025.",
    evid_note="Opened About Amazon Brasil Portuguese primary 2026-10-04; >R$19bn 2025 confirmed.",
)

# 2. copper / allied — Antofagasta 2026 CapEx guidance USD 3.4bn
row_doc(
    "antofagasta_2026_capex_guidance_3p4bn",
    "resources",
    "copper",
    "allied",
    "Antofagasta plc — 2026 consolidated Group CapEx guidance",
    "Chile",
    "17 Feb 2026 Antofagasta plc FY2025 results: in 2026, consolidated Group capital expenditure, which excludes Zaldívar, is expected to be USD 3.4 billion. Distinct from antofagasta_fy2025_capex_3p7bn (executed 2025 peak) and antofagasta_centinela_2nd_conc_2023 project approval.",
    "3400000000",
    "2026-02-17",
    "2026",
    "",
    "",
    "Antofagasta Group Chile copper operations CapEx guidance (multi-mine — lat/lon blank).",
    "antofagasta_fy2025_results_20260217",
    "In 2026, consolidated Group capital expenditure, which excludes Zaldívar, is expected to be $3.4 billion.",
    "https://www.antofagasta.co.uk/investors/news/2026/2025-full-year-results/",
    "Actor: Antofagasta plc (UK / Chile Luksic) — allied. Company English FY2025 results. CapEx guidance = USD 3.4bn. Shuffle copper.",
    "hunt_cycle198",
    investment_type="capex_expansion",
    evidence="documented",
    currency="USD",
    value_usd="3400000000",
    fx_usd="1",
    bib_type="company",
    chicago='Antofagasta plc. “2025 Full Year Results.” February 17, 2026. https://www.antofagasta.co.uk/investors/news/2026/2025-full-year-results/.',
    annotation="Antofagasta: 2026 CapEx guidance USD 3.4bn. Supports antofagasta_2026_capex_guidance_3p4bn.",
    evid_note="Opened Antofagasta English FY2025 results 2026-10-04; 2026 guidance USD 3.4bn confirmed.",
)

# 3. lithium / other — SQM CapEx plan USD 3bn 2026–2028
row_doc(
    "sqm_capex_3bn_2026_2028",
    "resources",
    "lithium",
    "other",
    "SQM — Group CapEx plan 2026–2028",
    "Chile",
    "19 Aug 2026 SQM 6-K / earnings release: expects capital expenditures of approximately USD 3 billion over 2026–2028 — ~60% Novandino (Codelco JV), ~20% Iodine and Plant Nutrition, ~20% International Lithium; includes ~USD 300m/year sustaining CapEx across divisions. CapEx plan = USD 3bn. Distinct from novandino_salar_futuro_3bn_2026 (project envelope over ~7 years after approvals).",
    "3000000000",
    "2026-08-19",
    "2026",
    "",
    "",
    "SQM Group CapEx plan (Chile Novandino + international lithium + iodine/nutrition — lat/lon blank).",
    "sqm_2q2026_earnings_6k",
    "We expect capital expenditures to be approximately US$3 billion over the three-year period from 2026 to 2028. The breakdown is as follows: approximately 60% for Novandino, 20% for the Iodine and Plant Nutrition Division, and 20% for the International Lithium Division. This estimate includes approximately US$300 million per year of sustaining capital expenditures across all divisions.",
    "https://www.sec.gov/Archives/edgar/data/909037/000090903726000034/a6-k_2q2026earningsrelease.htm",
    "Actor: SQM (Chilean) — other. Company SEC 6-K English primary. CapEx plan = USD 3bn. Shuffle lithium.",
    "hunt_cycle198",
    investment_type="capex_plan",
    evidence="documented",
    currency="USD",
    value_usd="3000000000",
    fx_usd="1",
    bib_type="company",
    chicago='Sociedad Química y Minera de Chile S.A. “SQM Reports Earnings for the Six Months Ended June 30, 2026.” Form 6-K, August 19, 2026. https://www.sec.gov/Archives/edgar/data/909037/000090903726000034/a6-k_2q2026earningsrelease.htm.',
    annotation="SQM: CapEx ~USD 3bn 2026–2028. Supports sqm_capex_3bn_2026_2028.",
    evid_note="Opened SQM SEC 6-K English earnings release 2026-10-04.",
)

# 4. lithium / other — Novandino Salar Futuro ~USD 3bn project
row_doc(
    "novandino_salar_futuro_3bn_2026",
    "resources",
    "lithium",
    "other",
    "Novandino (SQM / Codelco) — Salar Futuro project CapEx estimate",
    "Chile",
    "19 Aug 2026 SQM 6-K: Novandino submitted environmental/technical documentation for Salar Futuro in Salar de Atacama (Jul 2026); estimated capital investment approximately USD 3 billion over ~seven years following required approvals; aims higher recovery and lower environmental footprint (eliminate continental water use; renewable energy). CapEx estimate = USD 3bn. Distinct from sqm_capex_3bn_2026_2028 three-year Group CapEx guidance (overlapping but different horizon).",
    "3000000000",
    "2026-08-19",
    "2026",
    "-23.50",
    "-68.35",
    "Salar de Atacama / Novandino operations, Antofagasta Region (company geography; approximate salar pin).",
    "sqm_2q2026_earnings_6k",
    "Subject to the required approvals, Salar Futuro represents the next stage in the transformation of our operations in Chile. The project contemplates an estimated capital investment of approximately US$3 billion, to be deployed over approximately seven years following receipt of the required approvals, with the most capital-intensive phase currently expected during the third and fourth years of development.",
    "https://www.sec.gov/Archives/edgar/data/909037/000090903726000034/a6-k_2q2026earningsrelease.htm",
    "Actor: Novandino Litio (SQM + Codelco JV) — other. Company SEC 6-K English primary. CapEx estimate ≈ USD 3bn. Shuffle lithium.",
    "hunt_cycle198",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="USD",
    value_usd="3000000000",
    fx_usd="1",
    bib_type="company",
    chicago='Sociedad Química y Minera de Chile S.A. “SQM Reports Earnings for the Six Months Ended June 30, 2026.” Form 6-K, August 19, 2026. https://www.sec.gov/Archives/edgar/data/909037/000090903726000034/a6-k_2q2026earningsrelease.htm.',
    annotation="Novandino/SQM: Salar Futuro ~USD 3bn. Supports novandino_salar_futuro_3bn_2026.",
    evid_note="Opened SQM SEC 6-K English earnings release 2026-10-04; Salar Futuro ~USD 3bn confirmed.",
)

# 5. niobium / allied — upgrade CBMM 2025 CapEx R$1.1bn to company primary
row_doc(
    "cbmm_araxa_2025_spend_1p1bn",
    "resources",
    "niobium",
    "allied",
    "CBMM — 2025 Araxá CapEx",
    "Brazil",
    "CBMM company news (2025 results narrative): invested R$ 1.1 billion in Capex in 2025, reinforcing sustainable growth and long-term competitiveness; net revenue R$14.5bn; EBITDA R$10.2bn; net income R$6.4bn. CapEx = R$1.1bn. Upgrades prior Brasil Mineral press proxy to company Portuguese primary. Distinct from cbmm_araxa_13bn_plan_2026 / cbmm_araxa_2026_spend_2bn proxies and Codemig renewal.",
    "1100000000",
    "2026-03-24",
    "2025",
    "-19.59",
    "-46.94",
    "CBMM Araxá industrial complex, Minas Gerais.",
    "cbmm_crescimento_diversificacao_2025",
    "Em 2025, a CBMM investiu R$ 1,1 bilhão em Capex, reforçando seu compromisso com o crescimento sustentável e competitividade de longo prazo.",
    "https://cbmm.com/pt/midias/noticias/cbmm-crescimento-diversificacao-niobio",
    "Actor: CBMM (Moreira Salles–controlled Brazil) — allied. Company Portuguese primary. CapEx = R$1.1bn (BRL stored without FX). Shuffle niobium thin top-up / equal budget.",
    "hunt_cycle198",
    investment_type="capex_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='CBMM. “CBMM avança em sua estratégia de crescimento e diversificação.” Company news. https://cbmm.com/pt/midias/noticias/cbmm-crescimento-diversificacao-niobio.',
    annotation="CBMM: FY2025 CapEx R$1.1bn. Supports cbmm_araxa_2025_spend_1p1bn.",
    evid_note="Opened CBMM Portuguese company primary 2026-10-04; upgrades prior Brasil Mineral proxy.",
)

# 6. niobium / allied — CBMM CapEx plan R$11bn to 2030 (RS primary)
row_doc(
    "cbmm_capex_plan_11bn_2030",
    "resources",
    "niobium",
    "allied",
    "CBMM — CapEx / growth plan to 2030 (R$11bn)",
    "Brazil",
    "CBMM Sustainability Report 2025: plans investments of R$ 11 billion in Capex and the CBMM growth plan through 2030 — expansion of new lines/plants and equipment modernization; EDR9 tailings structure cited among new-cycle milestones. CapEx plan = R$11bn. Distinct from cbmm_araxa_13bn_plan_2026 (R$13bn 2026–2031 press proxy) and cbmm_araxa_2025_spend_1p1bn (executed 2025).",
    "11000000000",
    "2026-03-01",
    "2026",
    "-19.59",
    "-46.94",
    "CBMM Araxá industrial complex, Minas Gerais.",
    "cbmm_rs_2025",
    "Para os próximos anos, a empresa tem planos de investimento de R$ 11 bilhões em Capex e no plano de crescimento da CBMM até 2030. Serão direcionados investimentos na expansão de novas linhas e plantas, além da modernização de equipamentos.",
    "https://cbmm.com/relatorio-sustentabilidade/pdf/CBMM_RS25_D16_02.pdf",
    "Actor: CBMM — allied. Company Portuguese Sustainability Report 2025 PDF. CapEx plan = R$11bn (BRL stored without FX). Shuffle niobium.",
    "hunt_cycle198",
    investment_type="capex_plan",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='CBMM. Relatório de Sustentabilidade 2025. https://cbmm.com/relatorio-sustentabilidade/pdf/CBMM_RS25_D16_02.pdf.',
    annotation="CBMM: CapEx/growth plan R$11bn to 2030. Supports cbmm_capex_plan_11bn_2030.",
    evid_note="Opened CBMM RS 2025 PDF 2026-10-04; R$11bn plan confirmed.",
)

# 7. other_renewables / prc — CTG Brasil H2V pilot ~R$60m
row_doc(
    "ctg_brasil_h2v_pilot_60m_brl_2025",
    "energy",
    "other_renewables",
    "prc",
    "CTG Brasil — green hydrogen (H2V) pilot plant (Aneel-regulated spend)",
    "Brazil",
    "CTG Brasil Relatório Anual 2025: Hidrogênio Verde (H2V) project will develop a pilot plant inside a client industrial site to validate production/sale business model; investment of about R$ 60 million via Aneel-regulated funds; also studies electricity-sector impacts. CapEx ≈ R$60m. Distinct from ctg_serra_da_palmeira_2025 / Arinos solar rows.",
    "60000000",
    "2025-12-31",
    "2025",
    "",
    "",
    "CTG Brasil H2V pilot at unnamed client industrial site (company; site not named — lat/lon blank).",
    "ctg_brasil_relatorio_anual_2025",
    "O projeto de Hidrogênio Verde (H2V) vai desenvolver uma planta-piloto dentro do site industrial de um cliente para validar o modelo de negócio de produção e venda do hidrogênio verde. O investimento de cerca de R$ 60 milhões via verba regulada pela Aneel também vai estudar os impactos do modelo no setor elétrico.",
    "https://www.ctgbr.com.br/relatorioanual2025/",
    "Actor: CTG Brasil / China Three Gorges — prc. Company Portuguese annual report primary. CapEx ≈ R$60m (BRL stored without FX). Shuffle other_renewables.",
    "hunt_cycle198",
    investment_type="pilot_plant",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='CTG Brasil. Relatório Anual 2025. https://www.ctgbr.com.br/relatorioanual2025/.',
    annotation="CTG Brasil: H2V pilot ~R$60m. Supports ctg_brasil_h2v_pilot_60m_brl_2025.",
    evid_note="Opened CTG Brasil Relatório Anual 2025 page 2026-10-04.",
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
    print(f"cycle198 added {len(added)}: {added}")
    print(f"cycle198 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
