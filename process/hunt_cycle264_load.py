#!/usr/bin/env python3
"""Cycle 264 hunt: shuffle_seed=20261264; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261264).shuffle):
balsa, fission_smr, nickel, solar, water, power_plants_grid, niobium, wind, copper,
port_ownership, engineering_epc, other_renewables, graphite, port_cranes, bridges_roads,
rail, lithium, building_materials.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: spent residual (Equinix/Ascenty/Cirion/Wabtec/EXIM/USTDA/Meitner dense).
PRC equal-budget: honest residual (CPFL/State Grid/CRRC dense).
Allied: NEW ENGIE Brasil 1T26 CapEx R$219m; NEW Asa Branca 2T26 CapEx R$111m;
  NEW Graúna 2T26 CapEx R$104m.
Other: NEW Copel 1S26 CapEx R$1,538.8m; NEW Alupar Palca Peru CapEx USD 220m;
  NEW Alupar 2T26 CapEx desembolsado R$354m (proxy); NEW MRS Baixada Santista R$2bn;
  NEW Rumo 2026 CapEx plan R$5.5bn floor; NEW Rumo Ferrovia MT R$1bn stretch.
Skipped: thin dry; holdovers unsigned; Equinix SP USD109m SEC; BYD BESS company;
  EPR Litoral dual URL; Progress Rail VLI R$430m; Alupar TECP company face R$2.0518bn
  vs TPC Aneel CapEx already nested.
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


# 1. power_plants_grid / other — NEW Copel 1S26 CapEx R$1,538.8m
row_doc(
    "copel_1s26_capex_1538p8m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — 1S26 CapEx R$1,538.8m",
    "Brazil",
    "Copel 2T26 earnings release CapEx table (company materials via RI republication): Total Investments 1S26 R$1,538.8 million (2T26 R$957.2m already nested; DisCo 1S26 R$917.7m; GeT 1S26 R$617.7m incl. LRCAP R$317.9m). CapEx: enter R$1,538.8m 1S26 face. Nested vs 2T26 / 2026 plan / 2026–2030 plan (not additive).",
    "1538800000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Copel Paraná footprint (Curitiba HQ pin; DisCo/GeT statewide).",
    "copel_2t26_investidor10_1s26",
    "No 2T26, o montante realizado do programa de investimentos totalizou R$ 957,2 milhões … Total 957,2 … 1.538,8 … 1S26",
    "https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/",
    "Actor: Copel (Paraná state utility) — other. NEW nested 1S26 CapEx R$1,538.8m. Shuffle power_plants_grid.",
    "hunt_cycle264", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1538800000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel (Companhia Paranaense de Energia). “Destaques 2T26” CapEx table (RI republication). 2026. https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/.',
    annotation="Copel 1S26 CapEx R$1,538.8m via Fed H.10. Supports copel_1s26_capex_1538p8m_brl.",
    evid_note="Opened Copel 2T26 CapEx table republication; Total 1S26 R$1,538.8m confirmed beside 2T26 R$957.2m. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. power_plants_grid / allied — NEW ENGIE Brasil 1T26 CapEx R$219m
row_doc(
    "engie_brasil_1t26_capex_219m_brl",
    "energy", "power_plants_grid", "allied",
    "ENGIE Brasil — 1T26 CapEx R$219m",
    "Brazil",
    "7 May 2026 ENGIE Brasil Energia company PR (1T26): total investments R$219 million in the quarter for transmission infrastructure and renewable generation (Asa Branca LI cited; Graúna brownfield progress). CapEx: enter R$219m 1T26 face. Nested vs 2T26 R$329m / FY envelopes (not additive).",
    "219000000", "2026-03-31", "2026", "-27.60", "-48.55",
    "ENGIE Brasil Energia (Florianópolis HQ / Brazil generation-transmission portfolio pin).",
    "engie_brasil_1t26_pr_20260507",
    "Os investimentos totais da Companhia alcançaram R$ 219 milhões no período, sendo destinados a projetos de infraestrutura de transmissão e de geração renovável",
    "https://www.engie.com.br/imprensa/press-releases/receita-operacional-liquida-de-r-34-bilhoes-no-1t26/",
    "Actor: ENGIE Brasil Energia (France) — allied. NEW 1T26 CapEx R$219m. Shuffle power_plants_grid.",
    "hunt_cycle264", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(219000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ENGIE Brasil Energia. “ENGIE Brasil Energia registra receita operacional líquida de R$ 3,4 bilhões no primeiro trimestre de 2026.” May 7, 2026. https://www.engie.com.br/imprensa/press-releases/receita-operacional-liquida-de-r-34-bilhoes-no-1t26/.',
    annotation="ENGIE Brasil 1T26 CapEx R$219m via Fed H.10. Supports engie_brasil_1t26_capex_219m_brl.",
    evid_note="Opened ENGIE Brasil company 1T26 PR; CapEx R$219m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / allied — NEW ENGIE Asa Branca 2T26 CapEx R$111m
row_doc(
    "engie_asa_branca_2t26_capex_111m_brl",
    "energy", "power_plants_grid", "allied",
    "ENGIE Brasil — Asa Branca 2T26 CapEx R$111m",
    "Brazil",
    "5 Aug 2026 ENGIE Brasil Energia company PR (2T26): of R$329m quarterly CapEx, Asa Branca transmission received R$111 million. CapEx: enter R$111m Asa Branca 2T26 face. Nested vs Asa Branca Aneel CapEx envelope / consolidated 2T26 (not additive).",
    "111000000", "2026-06-30", "2026", "-12.40", "-41.30",
    "Asa Branca TX corridor (Bahia–Minas Gerais–Espírito Santo; approximate BA pin).",
    "engie_brasil_2t26_pr_20260805",
    "Os aportes da Companhia totalizaram R$ 329 milhões no trimestre. Desse montante, R$ 261 milhões foram destinados à construção de novos projetos. Destaque para os empreendimentos de transmissão Asa Branca e Graúna, que receberam investimentos de R$ 111 milhões e R$ 104 milhões, respectivamente.",
    "https://www.engie.com.br/imprensa/press-releases/engie-brasil-energia-registra-lucro-liquido-de-r-19-bilhao-246-no-segundo-trimestre-de-2026/",
    "Actor: ENGIE Brasil Energia (France) — allied. NEW nested Asa Branca 2T26 CapEx R$111m. Shuffle power_plants_grid.",
    "hunt_cycle264", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(111000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ENGIE Brasil Energia. “ENGIE Brasil Energia registra lucro líquido de R$ 1,9 bilhão (+246%) no segundo trimestre de 2026.” August 5, 2026. https://www.engie.com.br/imprensa/press-releases/engie-brasil-energia-registra-lucro-liquido-de-r-19-bilhao-246-no-segundo-trimestre-de-2026/.',
    annotation="ENGIE Brasil 2T26 Asa Branca/Graúna nested CapEx via Fed H.10. Supports engie_asa_branca_2t26_capex_111m_brl; engie_grauna_2t26_capex_104m_brl.",
    evid_note="Opened ENGIE Brasil company 2T26 PR; Asa Branca CapEx R$111m confirmed within R$329m quarter. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / allied — NEW ENGIE Graúna 2T26 CapEx R$104m
row_doc(
    "engie_grauna_2t26_capex_104m_brl",
    "energy", "power_plants_grid", "allied",
    "ENGIE Brasil — Graúna 2T26 CapEx R$104m",
    "Brazil",
    "5 Aug 2026 ENGIE Brasil Energia company PR (2T26): Graúna transmission received R$104 million within R$329m quarterly CapEx. CapEx: enter R$104m Graúna 2T26 face. Nested vs Graúna Aneel CapEx R$2,933.6m envelope / consolidated 2T26 (not additive).",
    "104000000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Graúna TX footprint (SC/PR/MG/SP/ES cited in companion materials; approximate South Brazil pin).",
    "engie_brasil_2t26_pr_20260805",
    "Os aportes da Companhia totalizaram R$ 329 milhões no trimestre … Destaque para os empreendimentos de transmissão Asa Branca e Graúna, que receberam investimentos de R$ 111 milhões e R$ 104 milhões, respectivamente.",
    "https://www.engie.com.br/imprensa/press-releases/engie-brasil-energia-registra-lucro-liquido-de-r-19-bilhao-246-no-segundo-trimestre-de-2026/",
    "Actor: ENGIE Brasil Energia (France) — allied. NEW nested Graúna 2T26 CapEx R$104m. Shuffle power_plants_grid.",
    "hunt_cycle264", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(104000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ENGIE Brasil Energia. “ENGIE Brasil Energia registra lucro líquido de R$ 1,9 bilhão (+246%) no segundo trimestre de 2026.” August 5, 2026. https://www.engie.com.br/imprensa/press-releases/engie-brasil-energia-registra-lucro-liquido-de-r-19-bilhao-246-no-segundo-trimestre-de-2026/.',
    annotation="ENGIE Brasil 2T26 Asa Branca/Graúna nested CapEx via Fed H.10. Supports engie_asa_branca_2t26_capex_111m_brl; engie_grauna_2t26_capex_104m_brl.",
    evid_note="Opened ENGIE Brasil company 2T26 PR; Graúna CapEx R$104m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. power_plants_grid / other — NEW Alupar Palca (Peru) CapEx USD 220m
row_doc(
    "alupar_palca_peru_capex_220m_usd",
    "energy", "power_plants_grid", "other",
    "Alupar — TEP Palca (Peru) CapEx USD 220m",
    "Peru",
    "6 Aug 2026 Alupar Investimento 2T26 earnings release (company RI ZIP PDF): TEP (Palca) Peru — Sep/2025 auction award; 5 substations + 248 km transmission lines; planned investment USD 220 million; winning RAP USD 31.8 million. CapEx: enter USD 220m planned face. Distinct from TCN/Maravilla/TSA Peru rows and Brazil TAP/TPC/TCN CapEx.",
    "220000000", "2026-06-30", "2026", "-13.16", "-74.22",
    "Alupar TEP Palca Peru transmission package (national footprint pin; 5 SE + 248 km).",
    "alupar_2t26_release_20260806",
    "O projeto TEP (Palca): localizado no Peru, foi objeto de leilão realizado em setembro/2025 e contempla a implantação de 5 subestações e de 248 km em linhas de transmissão. O investimento previsto para o projeto é US$ 220 mm e a RAP vencedora é de US$ 31,8 mm",
    "https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip",
    "Actor: Alupar Investimento — other. NEW Palca Peru CapEx USD 220m from company 2T26 PDF. Shuffle power_plants_grid.",
    "hunt_cycle264", investment_type="greenfield", evidence="documented", currency="USD",
    value_usd="220000000", fx_usd="1", bib_type="company",
    chicago='Alupar Investimento S.A. “Release de Resultados 2T26.” August 6, 2026. https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip.',
    annotation="Alupar 2T26 company ZIP: Palca Peru CapEx USD 220m; also supports prior Lot 7/TAP/TPC/TCN rows.",
    evid_note="Opened Alupar 2T26 RI ZIP PDF; TEP Palca Peru CapEx US$220 mm and RAP US$31.8 mm confirmed.",
)

# 6. power_plants_grid / other — NEW Alupar 2T26 CapEx desembolsado R$354m (proxy)
row_doc(
    "alupar_2t26_capex_354m_brl",
    "energy", "power_plants_grid", "other",
    "Alupar — 2T26 CapEx desembolsado R$354m (projects under construction)",
    "Brazil",
    "7 Aug 2026 Cenário Energia summarizing Alupar 2T26 results: CapEx desembolsado on projects under construction totaled R$354.0 million in 2T26 (vs R$135.2 million in 1T26); 14 projects Brazil/Chile/Colombia/Peru. CapEx: enter R$354m 2T26 spent face. Nested vs project CapEx previsto rows (not additive). UNVERIFIED proxy (trade press of company results).",
    "354000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Alupar transmission projects under construction (São Paulo HQ pin; LatAm multi-country).",
    "cenarioenergia_alupar_2t26_20260807",
    "O fluxo de investimentos acompanhou o ritmo das obras no período: o capex desembolsado nos projetos em implantação somou R$ 354,0 milhões no 2T26, ante R$ 135,2 milhões no primeiro trimestre do ano.",
    "https://cenarioenergia.com.br/2026/08/07/alupar-receita-regulatoria-2t26-projetos-transmissao-tecp/",
    "Actor: Alupar Investimento — other. NEW nested 2T26 CapEx desembolsado R$354m (proxy). Shuffle power_plants_grid.",
    "hunt_cycle264", investment_type="corporate_capex", evidence="proxy", currency="BRL",
    value_usd=str(round(354000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Cenário Energia. “Alupar amplia receita regulatória em 10,3% no 2T26 e acelera expansão com R$ 10 bilhões em projetos de transmissão.” August 7, 2026. https://cenarioenergia.com.br/2026/08/07/alupar-receita-regulatoria-2t26-projetos-transmissao-tecp/.',
    annotation="Alupar 2T26 CapEx desembolsado R$354m via Fed H.10 (UNVERIFIED proxy). Supports alupar_2t26_capex_354m_brl.",
    evid_note="Opened Cenário Energia Alupar 2T26 summary; CapEx desembolsado R$354.0m / 1T26 R$135.2m stated. Mark proxy. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 7. rail / other — NEW MRS Baixada Santista CapEx cycle R$2bn
row_doc(
    "mrs_baixada_santista_2bn_brl_2026",
    "infrastructure", "rail", "other",
    "MRS Logística — Baixada Santista rail CapEx cycle R$2bn",
    "Brazil",
    "30 Jun 2026 MRS company press PDF: CCOI Baixada Santista inauguration concludes MRS investment cycle totaling R$2 billion on Port of Santos rail access (six yards; >90 km TR-68; 126 AMVs; 2.4 km trains; CBTC/CTC 34 km; Cubatão viaduct). CapEx: enter R$2bn cycle face. Distinct from Wabtec MRS loco rows.",
    "2000000000", "2026-06-30", "2026", "-23.96", "-46.33",
    "Baixada Santista / Port of Santos rail access (Santos pin; Prainha/Jurubatuba/Quilombo yards cited).",
    "mrs_baixada_santista_ccoi_20260630",
    "A entrega do CCOI representa a conclusão de um robusto ciclo de investimentos na região, totalizando R$ 2 bilhões. … Os R$ 2 bilhões investidos na Baixada Santista pela MRS impulsionaram uma extensa modernização de infraestrutura",
    "https://www.mrs.com.br/wp-content/uploads/2026/03/07-2026_Ferrovias-Inauguram-CCOI-e-MRS-oficializa-investimentos-na-ferrovia-de-acesso-a-Santos.pdf",
    "Actor: MRS Logística (Brazilian freight railroad) — other. NEW Baixada Santista CapEx cycle R$2bn. Shuffle rail.",
    "hunt_cycle264", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='MRS Logística. “Ferrovias inauguram Centro de Controle Operacional Integrado e MRS entrega obras da Baixada Santista com investimento de R$ 2 bilhões.” June 30, 2026. https://www.mrs.com.br/wp-content/uploads/2026/03/07-2026_Ferrovias-Inauguram-CCOI-e-MRS-oficializa-investimentos-na-ferrovia-de-acesso-a-Santos.pdf.',
    annotation="MRS Baixada Santista CapEx cycle R$2bn via Fed H.10. Supports mrs_baixada_santista_2bn_brl_2026.",
    evid_note="Opened MRS company Portuguese PDF; R$2bn Baixada Santista investment cycle confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 8. rail / other — NEW Rumo 2026 CapEx plan R$5.5bn floor
row_doc(
    "rumo_2026_capex_plan_55bn_brl",
    "infrastructure", "rail", "other",
    "Rumo — 2026 CapEx plan R$5.5–6.1bn (enter R$5.5bn floor)",
    "Brazil",
    "2 Apr 2026 Rumo Logística company press (CEO Pedro Palma / CNN interview republished on rumolog.com): 2026 CapEx planned between R$5.5 billion and R$6.1 billion. CapEx: enter R$5.5bn range floor. Distinct from 2T26/6M26 spent CapEx rows; nested vs Ferrovia MT R$1bn stretch (not additive).",
    "5500000000", "2026-04-02", "2026", "-23.55", "-46.63",
    "Rumo Brazil rail network (São Paulo HQ pin; Malha Norte/Paulista/Central footprint).",
    "rumo_2026_capex_plan_20260402",
    "Maior operadora de ferrovias de carga do país, a Rumo Logística prevê investir entre R$ 5,5 bilhões e R$ 6,1 bilhões em 2026, segundo o CEO da companhia, Pedro Palma.",
    "https://rumolog.com/sala-de-imprensa/rumo-deve-investir-r-6-bi-em-2026-e-preve-estreia-de-ferrovia-ate-setembro/",
    "Actor: Rumo Logística (Cosan) — other. NEW 2026 CapEx plan range floor R$5.5bn. Shuffle rail.",
    "hunt_cycle264", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(5500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo Logística. “Rumo deve investir R$ 6 bi em 2026 e prevê estreia de ferrovia até setembro.” April 2, 2026. https://rumolog.com/sala-de-imprensa/rumo-deve-investir-r-6-bi-em-2026-e-preve-estreia-de-ferrovia-ate-setembro/.',
    annotation="Rumo 2026 CapEx plan R$5.5bn floor + Ferrovia MT R$1bn via Fed H.10. Supports rumo_2026_capex_plan_55bn_brl; rumo_ferrovia_mt_1bn_brl_2026.",
    evid_note="Opened Rumo company press; 2026 CapEx range R$5.5–6.1bn confirmed — store floor. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 9. rail / other — NEW Rumo Ferrovia MT first stretch R$1bn
row_doc(
    "rumo_ferrovia_mt_1bn_brl_2026",
    "infrastructure", "rail", "other",
    "Rumo — Ferrovia Estadual de Mato Grosso first stretch CapEx ~R$1bn (2026)",
    "Brazil",
    "2 Apr 2026 Rumo company press: CEO cites additional ~R$1 billion in 2026 to complete first 162 km stretch of Ferrovia Estadual de Mato Grosso (Malha Norte extension toward Lucas do Rio Verde; commercial ops targeted Jul–Sep 2026). CapEx: enter R$1bn stretch face. Nested within 2026 CapEx plan (not additive).",
    "1000000000", "2026-04-02", "2026", "-16.47", "-54.64",
    "Ferrovia MT first stretch (Rondonópolis MT pin; 162 km Malha Norte extension).",
    "rumo_2026_capex_plan_20260402",
    "Em entrevista à CNN, o executivo destacou um aporte de mais R$ 1 bilhão neste ano para concluir as obras do primeiro trecho da Ferrovia Estadual de Mato Grosso — na prática, um prolongamento da Malha Norte, que hoje vai de Rondonópolis (MT) ao Porto de Santos (SP).",
    "https://rumolog.com/sala-de-imprensa/rumo-deve-investir-r-6-bi-em-2026-e-preve-estreia-de-ferrovia-ate-setembro/",
    "Actor: Rumo Logística — other. NEW Ferrovia MT 2026 stretch CapEx ~R$1bn. Shuffle rail.",
    "hunt_cycle264", investment_type="expansion", evidence="documented", currency="BRL",
    value_usd=str(round(1000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo Logística. “Rumo deve investir R$ 6 bi em 2026 e prevê estreia de ferrovia até setembro.” April 2, 2026. https://rumolog.com/sala-de-imprensa/rumo-deve-investir-r-6-bi-em-2026-e-preve-estreia-de-ferrovia-ate-setembro/.',
    annotation="Rumo 2026 CapEx plan R$5.5bn floor + Ferrovia MT R$1bn via Fed H.10. Supports rumo_2026_capex_plan_55bn_brl; rumo_ferrovia_mt_1bn_brl_2026.",
    evid_note="Opened Rumo company press; ~R$1bn 2026 Ferrovia MT first-stretch CapEx confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle264 added {len(added)}: {added}")
    print(f"cycle264 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
