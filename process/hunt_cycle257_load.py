#!/usr/bin/env python3
"""Cycle 257 hunt: shuffle_seed=20261257; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261257).shuffle):
port_ownership, power_plants_grid, graphite, lithium, water, rail, engineering_epc,
other_renewables, wind, niobium, solar, bridges_roads, balsa, nickel, fission_smr,
copper, port_cranes, building_materials.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Scala BNDES R$380m equipment CapEx financing (DigitalBridge);
  Atlas/Ascenty/Equinix/AES Andes CapEx dense elsewhere — residual after spend.
PRC equal-budget: honest residual (CPFL nested C254–C256; State Grid/CRRC dense).
Allied: NEW ISA Energia 2T26 CapEx R$1,053.5m; NEW ISA remanescente ~R$4.6bn;
  NEW Neoenergia 6M26 CapEx R$4.0bn; NEW ENGIE Brasil 2T26 CapEx R$329m.
Other: NEW Light 1T26 CapEx R$349m; NEW Energisa 2026 CapEx plan R$7.0914bn.
Skipped: thin dry; holdovers unsigned; Alupar TECP/Lot 7 without openable company PDF;
  Copel 1S26 nested under 2T26 without distinct company PDF; ODATA SP04 vs DeltaFlow.
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


# 1. power_plants_grid / allied — NEW ISA Energia 2T26 CapEx R$1,053.5m
row_doc(
    "isa_energia_2t26_capex_1053p5m_brl",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — 2T26 CapEx R$1,053.5m",
    "Brazil",
    "3 Aug 2026 ISA Energia Brasil company news (2T26): investments in Q2 reached R$1.1bn (−4% vs 2T25); of which R$445.4m Reforços e Melhorias (+17%) and R$608.1m greenfield/licitados (−16%). CapEx: enter component sum R$1,053.5m (445.4+608.1) as face (company rounded headline R$1.1bn). Nested vs isa_energia_fy2025_capex_5p1bn_brl / R&M rows (not additive).",
    "1053500000", "2026-06-30", "2026", "-23.55", "-46.63",
    "ISA Energia Brasil transmission footprint (São Paulo HQ pin).",
    "isa_energia_2t26_news_20260803",
    "No segundo trimestre, os investimentos alcançaram o volume de R$ 1,1 bilhão, um recuo de R$ 48,7 milhões (−4% vs. 2T25). Desse montante, R$ 445,4 milhões foram dedicados a projetos de Reforços e Melhorias, incremento de R$ 66,1 milhões (+17% vs. 2T25), e R$ 608,1 milhões a projetos licitados – uma redução de R$ 114,7 milhões (−16% vs. 2T25)",
    "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/com-energizacao-de-grandes-projetos-isa-energia-brasil-amplia-receita-liquida-em-21-no-trimestre/",
    "Actor: ISA Energia Brasil (ISA Colombia–controlled) — allied. NEW nested 2T26 CapEx R$1,053.5m from company components. Shuffle power_plants_grid. Holdover company-primary resolved.",
    "hunt_cycle257", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1053500000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “Com energização de grandes projetos, ISA ENERGIA BRASIL amplia receita líquida em 21% no trimestre.” August 3, 2026. https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/com-energizacao-de-grandes-projetos-isa-energia-brasil-amplia-receita-liquida-em-21-no-trimestre/.',
    annotation="ISA Energia 2T26 CapEx R$1,053.5m and remanescente ~R$4.6bn via Fed H.10. Supports isa_energia_2t26_capex_1053p5m_brl; isa_energia_remanescente_4p6bn_brl_2026.",
    evid_note="Opened ISA Energia Brasil company 2T26 news; CapEx headline R$1.1bn with R$445.4m R&M + R$608.1m licitados confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. power_plants_grid / allied — NEW ISA remanescente ~R$4.6bn Serra Dourada/Itatiaia
row_doc(
    "isa_energia_remanescente_4p6bn_brl_2026",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — remaining CapEx ~R$4.6bn (Serra Dourada/Itatiaia)",
    "Brazil",
    "3 Aug 2026 ISA Energia Brasil company news (2T26): after Jacarandá and Piraquê Bloco 3 energizations, Serra Dourada (BA/MG) and Itatiaia (MG/RJ) still have cerca de R$4.6 bilhões in remaining CapEx through ~2028 (combined RAP R$596.9m cycle 2026/2027). CapEx: enter R$4.6bn soft floor. Distinct from isa_energia_serra_dourada_3p2bn_2025 project total and R&M carteira 7.2bn.",
    "4600000000", "2026-08-03", "2026", "-14.86", "-40.84",
    "Serra Dourada BA/MG and Itatiaia MG/RJ transmission corridor (Bahia/Minas pin).",
    "isa_energia_2t26_news_20260803",
    "Com a energização do projeto Jacarandá e do Bloco 3 do projeto Piraquê, a Companhia avança na execução de outros dois novos empreendimentos com entrada em operação prevista até 2028 – Serra Dourada (BA/MG) e Itatiaia (MG/RJ) – que somam RAP de R$ 596,9 milhões (Ciclo 2026/2027), e ainda possuem cerca de R$ 4,6 bilhões em CapEx remanescente.",
    "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/com-energizacao-de-grandes-projetos-isa-energia-brasil-amplia-receita-liquida-em-21-no-trimestre/",
    "Actor: ISA Energia Brasil (ISA Colombia–controlled) — allied. NEW remaining CapEx ~R$4.6bn company soft floor. Shuffle power_plants_grid. Holdover company-primary resolved.",
    "hunt_cycle257", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(4600000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “Com energização de grandes projetos, ISA ENERGIA BRASIL amplia receita líquida em 21% no trimestre.” August 3, 2026. https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/com-energizacao-de-grandes-projetos-isa-energia-brasil-amplia-receita-liquida-em-21-no-trimestre/.',
    annotation="ISA Energia 2T26 CapEx R$1,053.5m and remanescente ~R$4.6bn via Fed H.10. Supports isa_energia_2t26_capex_1053p5m_brl; isa_energia_remanescente_4p6bn_brl_2026.",
    evid_note="Opened ISA Energia Brasil company 2T26 news; remaining CapEx cerca de R$4.6bn for Serra Dourada/Itatiaia confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / other — NEW Light 1T26 CapEx R$349m
row_doc(
    "light_1t26_capex_349m_brl",
    "energy", "power_plants_grid", "other",
    "Light S.A. — 1T26 CapEx R$349m",
    "Brazil",
    "Light S.A. 1T26 earnings release (company MZ IQ PDF): Company invested R$349 million in 1T26 (+18.0% YoY); DisCo Light SESA R$341m of which R$289m electrical assets (maintenance R$137m; expansion R$88m; loss-reduction R$61m). CapEx: enter R$349m 1T26 face. Nested vs light_sesa_10bn_brl_2026_2030 plan (not additive).",
    "349000000", "2026-03-31", "2026", "-22.91", "-43.17",
    "Light SESA Rio de Janeiro concession (Rio de Janeiro pin).",
    "light_1t26_release_mziq",
    "A Companhia investiu R$349 milhões no 1T26, crescimento de 18,0% frente ao 1T25, em alinhamento ao seu novo ciclo de investimentos na Distribuição, com foco na renovação, modernização e digitalização da rede",
    "https://api.mziq.com/mzfilemanager/v2/d/50b51302-4c48-4351-b296-bfcbe65fd70a/586839ac-be1f-07e6-6fdb-c67da0fac283?origin=2",
    "Actor: Light S.A. / Light SESA (Brazilian distributor) — other. NEW nested 1T26 CapEx R$349m. Shuffle power_plants_grid.",
    "hunt_cycle257", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(349000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Light S.A. “Release de Resultados 1T26.” 2026. https://api.mziq.com/mzfilemanager/v2/d/50b51302-4c48-4351-b296-bfcbe65fd70a/586839ac-be1f-07e6-6fdb-c67da0fac283?origin=2.',
    annotation="Light 1T26 NEW R$349m ~USD 67.22m via Fed H.10. Supports light_1t26_capex_349m_brl.",
    evid_note="Opened Light 1T26 company MZ IQ PDF; CapEx R$349m (+18.0% YoY) / SESA R$341m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / other — NEW Energisa 2026 CapEx plan R$7.0914bn
row_doc(
    "energisa_2026_capex_plan_7p091bn_brl",
    "energy", "power_plants_grid", "other",
    "Energisa — 2026 CapEx projection R$7.0914bn",
    "Brazil",
    "Energisa RI Investimentos page: 2026 CapEx projections total R$7,091.4 million (distribution R$6,546.2m; transmission R$180.3m; (re)energisa R$109.2m; DG R$91.4m; gas distribution R$176.3m; holdings/other R$79.4m). CapEx: enter R$7.0914bn face. Distinct from energisa_4states_18bn_brl_2026_2030 four-state renewal package.",
    "7091400000", "2026-01-01", "2026", "-21.76", "-43.35",
    "Energisa Brazilian distribution footprint (Juiz de Fora HQ pin).",
    "energisa_ri_investimentos_2026",
    "(=) Total | 7.091,4 | 6.638,8 | 6.772,0 | … Distribuição de energia elétrica | 6.546,2 … Transmissão de energia elétrica | 180,3 … Distribuição de gás natural | 176,3",
    "https://ri.energisa.com.br/divulgacoes-e-resultados/investimentos/",
    "Actor: Energisa (Brazilian utility group) — other. NEW 2026 CapEx projection R$7.0914bn company RI. Shuffle power_plants_grid.",
    "hunt_cycle257", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(7091400000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Energisa S.A. “Investimentos” (RI). Accessed October 5, 2026. https://ri.energisa.com.br/divulgacoes-e-resultados/investimentos/.',
    annotation="Energisa 2026 plan NEW R$7.0914bn ~USD 1365.81m via Fed H.10. Supports energisa_2026_capex_plan_7p091bn_brl.",
    evid_note="Opened Energisa RI Investimentos page; 2026 projection Total R$7,091.4m with segment breakouts confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. power_plants_grid / allied — NEW Neoenergia 6M26 CapEx R$4.0bn
row_doc(
    "neoenergia_6m26_capex_4bn_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — 6M26 CapEx R$4.0bn",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release (company MZ IQ PDF): CAPEX of R$4 billion in 6M26, of which R$3.7 billion in distribution leading to RAB R$47.3 billion; distributors' CapEx table shows CAPEX line R$3,696m 6M26. CapEx: enter R$4.0bn 6M26 face. Nested vs neoenergia_1t26_capex_1p8bn_brl / FY2025 / 50bn plan (not additive).",
    "4000000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil distribution/transmission footprint (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "▪ CAPEX of R$ 4 billion in 6M26, of which R$ 3.7 billion in distribution leading to a RAB of R$ 47.3 billion; … Neoenergia’s capex ended the 6M26 at R$ 4.0 billion",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested 6M26 CapEx R$4.0bn. Shuffle power_plants_grid.",
    "hunt_cycle257", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(4000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Release 2Q26 / 6M26.” July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia 6M26 NEW R$4.0bn ~USD 770.40m via Fed H.10. Supports neoenergia_6m26_capex_4bn_brl.",
    evid_note="Opened Neoenergia 2Q26 company MZ IQ PDF; CAPEX R$4.0bn 6M26 / R$3.7bn distribution confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 6. power_plants_grid / allied — NEW ENGIE Brasil 2T26 CapEx R$329m
row_doc(
    "engie_brasil_2t26_capex_329m_brl",
    "energy", "power_plants_grid", "allied",
    "ENGIE Brasil Energia — 2T26 CapEx R$329m",
    "Brazil",
    "5 Aug 2026 ENGIE Brasil Energia company press release (2T26): Company investments totaled R$329 million in the quarter; R$261m to new-project construction (Asa Branca R$111m; Graúna R$104m); remainder to generation and O&M revitalization. CapEx: enter R$329m 2T26 face. Nested vs engie_brasil_fy2025_capex_6bn_brl / ANEEL 01/2026 1.5bn (not additive).",
    "329000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "ENGIE Brasil Energia footprint (São Paulo HQ pin; Asa Branca/Graúna TX).",
    "engie_brasil_2t26_pr_20260805",
    "Os aportes da Companhia totalizaram R$ 329 milhões no trimestre. Desse montante, R$ 261 milhões foram destinados à construção de novos projetos. Destaque para os empreendimentos de transmissão Asa Branca e Graúna, que receberam investimentos de R$ 111 milhões e R$ 104 milhões, respectivamente.",
    "https://www.engie.com.br/imprensa/press-releases/engie-brasil-energia-registra-lucro-liquido-de-r-19-bilhao-246-no-segundo-trimestre-de-2026/",
    "Actor: ENGIE Brasil Energia (ENGIE France–controlled) — allied. NEW nested 2T26 CapEx R$329m. Shuffle power_plants_grid.",
    "hunt_cycle257", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(329000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ENGIE Brasil Energia. “ENGIE Brasil Energia registra lucro líquido de R$ 1,9 bilhão (+246%) no segundo trimestre de 2026.” August 5, 2026. https://www.engie.com.br/imprensa/press-releases/engie-brasil-energia-registra-lucro-liquido-de-r-19-bilhao-246-no-segundo-trimestre-de-2026/.',
    annotation="ENGIE Brasil 2T26 NEW R$329m ~USD 63.37m via Fed H.10. Supports engie_brasil_2t26_capex_329m_brl.",
    evid_note="Opened ENGIE Brasil company 2T26 press release; CapEx R$329m / Asa Branca R$111m / Graúna R$104m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 7. engineering_epc / us — NEW Scala BNDES R$380m equipment CapEx financing
row_doc(
    "scala_bndes_380m_brl_2025",
    "infrastructure", "engineering_epc", "us",
    "Scala Data Centers (DigitalBridge) — BNDES equipment CapEx financing R$380m",
    "Brazil",
    "27 Nov 2025 Scala Data Centers company press: BNDES approved additional R$200 million release for Scala hyperscale data-center equipment CapEx, bringing cumulative BNDES financing to R$380 million to date (machines, industrial systems, IT/automation components, domestic goods, specialized imports). CapEx financing: enter R$380m cumulative face. Nested vs scala_cumulative_12bn_brl_2025 / AI City / Chile PF (not additive).",
    "380000000", "2025-11-27", "2025", "-23.51", "-46.88",
    "Scala Campus Tamboré Barueri / multi-site Brazil expansion (Barueri pin).",
    "scala_bndes_380m_20251127",
    "O Banco Nacional de Desenvolvimento Econômico e Social (BNDES) aprovou uma liberação adicional de R$ 200 milhões para a Scala Data Centers … totalizando R$ 380 milhões até o momento … O investimento prevê a compra de máquinas, sistemas industriais, componentes de informática e de automação",
    "https://scaladatacenters.com/scala_na_midia/scala-data-centers-e-bndes-concluem-segunda-etapa-do-maior-financiamento-do-banco-no-setor-totalizando-r-380-milhoes-ate-o-momento/",
    "Actor: Scala Data Centers (DigitalBridge US–backed) — us. NEW BNDES equipment CapEx financing cumulative R$380m. Shuffle engineering_epc / ≥1/3 US budget.",
    "hunt_cycle257", investment_type="financing_capex", evidence="documented", currency="BRL",
    value_usd=str(round(380000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Scala Data Centers. “Scala Data Centers e BNDES concluem segunda etapa do maior financiamento do banco no setor, totalizando R$ 380 milhões até o momento.” November 27, 2025. https://scaladatacenters.com/scala_na_midia/scala-data-centers-e-bndes-concluem-segunda-etapa-do-maior-financiamento-do-banco-no-setor-totalizando-r-380-milhoes-ate-o-momento/.',
    annotation="Scala BNDES NEW R$380m ~USD 73.19m via Fed H.10. Supports scala_bndes_380m_brl_2025.",
    evid_note="Opened Scala company BNDES second-tranche press; cumulative R$380m / +R$200m equipment CapEx financing confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle257 added {len(added)}: {added}")
    print(f"cycle257 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
