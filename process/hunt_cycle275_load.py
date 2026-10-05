#!/usr/bin/env python3
"""Cycle 275 hunt: shuffle_seed=20261275; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261275).shuffle):
port_ownership, graphite, nickel, engineering_epc, wind, power_plants_grid, solar,
building_materials, bridges_roads, port_cranes, other_renewables, copper, lithium,
balsa, water, rail, niobium, fission_smr.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes three-project SEA package US$3bn (Solar
  Oriente/Altos del Sol/Llanos del Sol) + NEW Chile construction+contracted
  portfolio CapEx >US$2bn 2024–2027 (Atacama Solar acquisition company English).
PRC equal-budget: NEW CTG Brasil PDI CapEx >R$19m (2025 company growth cycle).
Allied: NEW Neoenergia Hydro 6M26 R$6m + Customers 6M26 R$19m.
Other: NEW Copel gen+TX 2026 plan R$971.6m; Aegea Guariroba R$49m + Novas
  Operações R$186m + Demais Concessões R$356m (2T26); Rumo Capacitação Malha
  Ferroviária 2T26 R$483m.
Skipped: thin dry; ENGIE Colibri host 403; Ascenty company face 403; Alupar TECP
  company ZIP unsigned (Cenário Energia 406); holdovers unsigned.
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


# 1. other_renewables / us — NEW AES Andes SEA three-project package US$3bn
row_doc(
    "aes_andes_sea_package_3bn_2024",
    "energy", "other_renewables", "us",
    "AES Andes — Solar Oriente / Altos del Sol / Llanos del Sol SEA package US$3bn",
    "Chile",
    "9 Jan 2025 AES Andes English (Atacama Solar acquisition release): during Aug–Sep 2024, three photovoltaic+BESS projects — Solar Oriente, Altos del Sol, Llanos del Sol — entered environmental assessing with a total investment of US$3,000 million; >1,700 MW PV + 2,400 MW BESS in Tarapacá/Antofagasta. CapEx: enter USD3bn package face. Nested vs project-level Oriente USD990m / Altos USD1.375bn / Llanos USD635m (not additive).",
    "3000000000", "2024-09-01", "2024", "-22.00", "-69.90",
    "AES Andes Tarapacá/Antofagasta SEA PV+BESS package (northern Chile pin).",
    "aes_chile_atacama_solar_20250109",
    "During August and September 2024, three photovoltaic projects with battery storage systems - Solar Oriente, Altos del Sol, Llanos del Sol - entered environmental assessing process, with a total investment of US$3,000 million.",
    "https://www.aesandes.com/en/press-release/aes-chile-acquires-atacama-solar-photovoltaic-plant",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW SEA package CapEx US$3bn envelope. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle275", investment_type="capex_plan", evidence="documented", currency="USD",
    value_usd="3000000000", fx_usd="1", bib_type="company",
    chicago='AES Andes. “AES Chile acquires Atacama Solar photovoltaic plant.” January 9, 2025. https://www.aesandes.com/en/press-release/aes-chile-acquires-atacama-solar-photovoltaic-plant.',
    annotation="AES Andes SEA three-project package US$3bn. Supports aes_andes_sea_package_3bn_2024.",
    evid_note="Opened AES Andes Atacama Solar English release; US$3,000 million SEA package confirmed.",
)

# 2. other_renewables / us — NEW AES Andes Chile >US$2bn 2024–2027 construction+contracted
row_doc(
    "aes_andes_chile_capex_2bn_2024_2027",
    "energy", "other_renewables", "us",
    "AES Andes — Chile construction + contracted portfolio CapEx >US$2bn (2024–2027)",
    "Chile",
    "9 Jan 2025 AES Andes English: initiatives under construction for 572 MW renewable capacity plus contracted project portfolio >1,620 MW in development, all with investment of over US$2,000 million between 2024 and 2027. CapEx: enter USD2bn soft floor. Nested vs aes_andes_chile_capex_1p9bn_2024_2027 (earlier >USD1.9bn / >1,300 MW advanced wording) and SEA package US$3bn (not additive).",
    "2000000000", "2025-01-09", "2025", "-23.65", "-70.40",
    "AES Andes Chile renewable construction/contracted portfolio (Antofagasta regional pin).",
    "aes_chile_atacama_solar_20250109",
    "They have initiatives under construction for 572 MW of renewable capacity, in addition to a contracted project portfolio of more than 1,620 MW in development, all with an investment of over US$2,000 million between 2024 and 2027.",
    "https://www.aesandes.com/en/press-release/aes-chile-acquires-atacama-solar-photovoltaic-plant",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW soft Chile CapEx floor >US$2bn 2024–2027. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle275", investment_type="capex_plan", evidence="documented", currency="USD",
    value_usd="2000000000", fx_usd="1", bib_type="company",
    chicago='AES Andes. “AES Chile acquires Atacama Solar photovoltaic plant.” January 9, 2025. https://www.aesandes.com/en/press-release/aes-chile-acquires-atacama-solar-photovoltaic-plant.',
    annotation="AES Andes Chile >US$2bn CapEx 2024–2027. Supports aes_andes_chile_capex_2bn_2024_2027.",
    evid_note="Opened AES Andes Atacama Solar English release; over US$2,000 million 2024–2027 confirmed.",
)

# 3. other_renewables / prc — NEW CTG Brasil PDI CapEx >R$19m (2025)
row_doc(
    "ctg_brasil_pdi_19m_brl_2025",
    "energy", "other_renewables", "prc",
    "CTG Brasil — PDI CapEx >R$19m (2025)",
    "Brazil",
    "CTG Brasil company Portuguese growth-cycle release: investimento superior a R$19 milhões in Pesquisa, Desenvolvimento e Inovação (PDI) in 2025; 15 active projects focused on operational efficiency and energy transition (Valor Inovação recognition cited). CapEx: enter R$19m soft floor. Distinct from ctg_brasil_h2v_pilot_60m_brl_2025 / FlexBESS R$15m.",
    "19000000", "2025-12-31", "2025", "-20.43", "-51.34",
    "CTG Brasil PDI program (Ilha Solteira / Brazil generation footprint pin).",
    "ctg_brasil_crescimento_sustentavel_2025",
    "Com investimento superior a R$ 19 milhões em Pesquisa, Desenvolvimento e Inovação (PDI), a companhia manteve 15 projetos ativos focados em aumentar a eficiência operacional e acelerar a transição energética.",
    "https://www.ctgbr.com.br/ctg-brasil-se-prepara-para-novo-ciclo-de-crescimento-sustentavel/",
    "Actor: CTG Brasil (China Three Gorges) — prc. NEW PDI CapEx >R$19m. Shuffle other_renewables / PRC equal-budget.",
    "hunt_cycle275", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(19000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CTG Brasil. “CTG Brasil se prepara para novo ciclo de crescimento sustentável.” Company Portuguese. https://www.ctgbr.com.br/ctg-brasil-se-prepara-para-novo-ciclo-de-crescimento-sustentavel/.',
    annotation="CTG Brasil PDI CapEx >R$19m via Fed H.10. Supports ctg_brasil_pdi_19m_brl_2025.",
    evid_note="Opened CTG Brasil growth-cycle page; PDI >R$19 milhões confirmed.",
)

# 4. power_plants_grid / allied — NEW Neoenergia Hydro 6M26 CapEx R$6m
row_doc(
    "neoenergia_hydro_6m26_6m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — hydroelectric plants 6M26 CapEx R$6m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release: CAPEX table Hydroelectric plants R$6 million in 6M26 (2Q26 R$5m) within Generation and Customers. CapEx: enter R$6m hydro face. Nested vs neoenergia_gen_customers_6m26_57m_brl (not additive).",
    "6000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil hydro portfolio (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Hydroelectric plants 5 3 52% 6 12 (48%)",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Hydro 6M26 CapEx R$6m. Shuffle power_plants_grid.",
    "hunt_cycle275", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(6000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Hydro 6M26 CapEx R$6m via Fed H.10. Supports neoenergia_hydro_6m26_6m_brl.",
    evid_note="Opened Neoenergia 2Q26 MZ IQ PDF; Hydroelectric plants CapEx 6M26 R$6m confirmed.",
)

# 5. power_plants_grid / allied — NEW Neoenergia Customers 6M26 CapEx R$19m
row_doc(
    "neoenergia_customers_6m26_19m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — Customers segment 6M26 CapEx R$19m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release: CAPEX table Customers R$19 million in 6M26 (2Q26 R$7m) within Generation and Customers. CapEx: enter R$19m Customers face. Nested vs neoenergia_gen_customers_6m26_57m_brl (not additive).",
    "19000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil Customers / energy-trade segment (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Customers 7 3 94% 19 7 173%",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Customers 6M26 CapEx R$19m. Shuffle power_plants_grid.",
    "hunt_cycle275", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(19000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Customers 6M26 CapEx R$19m via Fed H.10. Supports neoenergia_customers_6m26_19m_brl.",
    evid_note="Opened Neoenergia 2Q26 MZ IQ PDF; Customers CapEx 6M26 R$19m confirmed.",
)

# 6. power_plants_grid / other — NEW Copel gen+TX 2026 plan R$971.6m
row_doc(
    "copel_gen_tx_2026_971p6m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — generation and transmission 2026 CapEx plan R$971.6m",
    "Brazil",
    "Copel company Portuguese news (2026 investment program): of ~R$3 billion planned for 2026, R$971.6 million destined to geração e transmissão businesses (alongside DisCo R$1.94bn). CapEx: enter R$971.6m gen+TX face. Nested vs copel_disco_2026_plan_1940m_brl / LRCAP Foz/Segredo rows (not additive).",
    "971600000", "2026-01-01", "2026", "-25.43", "-49.27",
    "Copel generation and transmission footprint, Paraná (Curitiba HQ pin).",
    "copel_2026_3bn_program_news",
    "Do total previsto para este ano, R$ 1,94 bilhão será aplicado na distribuição de energia, enquanto R$ 971,6 milhões serão destinados aos negócios de geração e transmissão.",
    "https://www.copel.com/site/noticias/copel-investe-r-3-bilhoes-em-obras-de-geracao-transmissao-e-distribuicao-de-energia-em-todo-o-parana/",
    "Actor: Copel (Paraná state utility) — other. NEW nested gen+TX 2026 CapEx plan R$971.6m. Shuffle power_plants_grid.",
    "hunt_cycle275", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(971600000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel. “Copel investe R$ 3 bilhões em obras de geração, transmissão e distribuição de energia em todo o Paraná.” Company Portuguese news. https://www.copel.com/site/noticias/copel-investe-r-3-bilhoes-em-obras-de-geracao-transmissao-e-distribuicao-de-energia-em-todo-o-parana/.',
    annotation="Copel gen+TX 2026 CapEx plan R$971.6m via Fed H.10. Supports copel_gen_tx_2026_971p6m_brl.",
    evid_note="Opened Copel company Portuguese news; gen+TX R$971,6 milhões confirmed.",
)

# 7. water / other — NEW Aegea Guariroba 2T26 Capex R$49m
row_doc(
    "aegea_guariroba_2t26_49m_brl",
    "resources", "water", "other",
    "Aegea — Águas Guariroba 2T26 Capex R$49m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Guariroba R$49 million in 2T26 (+19.4% vs 2T25 R$41m); 6M26 R$87m. CapEx: enter R$49m Guariroba face. Nested vs aegea_2t26_ecosystem_capex_1828m_brl (not additive).",
    "49000000", "2026-06-30", "2026", "-20.44", "-54.65",
    "Águas Guariroba / Campo Grande MS concession (Campo Grande pin).",
    "aegea_2t26_6m26_release_mziq",
    "Guariroba 49 41 19,4% 87 77 13,3%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Guariroba 2T26 Capex R$49m. Shuffle water.",
    "hunt_cycle275", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(49000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Guariroba 2T26 Capex R$49m via Fed H.10. Supports aegea_guariroba_2t26_49m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Guariroba Capex 2T26 R$49m confirmed.",
)

# 8. water / other — NEW Aegea Novas Operações 2T26 Capex R$186m
row_doc(
    "aegea_novas_operacoes_2t26_186m_brl",
    "resources", "water", "other",
    "Aegea — Novas Operações 2T26 Capex R$186m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Novas Operações R$186 million in 2T26 (+872.8% vs 2T25 R$19m); 6M26 R$339m. CapEx: enter R$186m Novas Operações face. Nested vs aegea_2t26_ecosystem_capex_1828m_brl (not additive).",
    "186000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Aegea new-operations water/sanitation concessions (São Paulo HQ pin).",
    "aegea_2t26_6m26_release_mziq",
    "Novas Operações 186 19 872,8% 339 19 1673,6%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Novas Operações 2T26 Capex R$186m. Shuffle water.",
    "hunt_cycle275", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(186000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Novas Operações 2T26 Capex R$186m via Fed H.10. Supports aegea_novas_operacoes_2t26_186m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Novas Operações Capex 2T26 R$186m confirmed.",
)

# 9. water / other — NEW Aegea Demais Concessões 2T26 Capex R$356m
row_doc(
    "aegea_demais_2t26_356m_brl",
    "resources", "water", "other",
    "Aegea — Demais Concessões 2T26 Capex R$356m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Demais Concessões R$356 million in 2T26 (+74.5% vs 2T25 R$204m); 6M26 R$682m. CapEx: enter R$356m Demais Concessões face. Nested vs aegea_2t26_ecosystem_capex_1828m_brl (not additive).",
    "356000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Aegea remaining water/sanitation concessions portfolio (São Paulo HQ pin).",
    "aegea_2t26_6m26_release_mziq",
    "Demais Concessões 356 204 74,5% 682 348 96,0%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Demais Concessões 2T26 Capex R$356m. Shuffle water.",
    "hunt_cycle275", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(356000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Demais Concessões 2T26 Capex R$356m via Fed H.10. Supports aegea_demais_2t26_356m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Demais Concessões Capex 2T26 R$356m confirmed.",
)

# 10. rail / other — NEW Rumo Capacitação Malha Ferroviária 2T26 CapEx R$483m
row_doc(
    "rumo_capacitacao_2t26_483m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Capacitação Malha Ferroviária 2T26 CapEx R$483m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Capacitação Malha Ferroviária R$483 million in 2T26 (+50.4% vs 2T25 R$321m); 6M26 R$949m — nested breakout within Operação Norte capacity-expansion works. CapEx: enter R$483m Capacitação face. Nested vs rumo_norte_2t26_1393m_brl / rumo_2t26_capex_1597m_brl (not additive).",
    "483000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Rumo Operação Norte rail-capacity expansion (São Paulo HQ pin; Malha Paulista/Central corridor).",
    "rumo_2t26_release_20260812",
    "483 321 50,4 % Capacitação Malha Ferroviária 949 958 -0,9 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Capacitação Malha Ferroviária 2T26 CapEx R$483m. Shuffle rail.",
    "hunt_cycle275", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(483000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Capacitação Malha 2T26 CapEx R$483m via Fed H.10. Supports rumo_capacitacao_2t26_483m_brl.",
    evid_note="Opened Rumo 2T26 company RI PDF; Capacitação Malha Ferroviária Capex R$483m confirmed.",
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
    print(f"cycle275 added {len(added)}: {added}")
    print(f"cycle275 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
