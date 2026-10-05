#!/usr/bin/env python3
"""Cycle 228 hunt: shuffle_seed=20261228; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261228).shuffle):
building_materials, power_plants_grid, port_ownership, balsa, port_cranes, solar,
engineering_epc, bridges_roads, nickel, wind, niobium, other_renewables, copper,
lithium, graphite, rail, water, fission_smr.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    dry; next-thinnest niobium CapEx-fill (CBMM R$13bn 2026–2031 plan).
≥1/3 U.S. hunt budget spent on Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/Fluence/SSA/Atlas/Ascenty/Progress Rail/GE Vernova/Oceaneering/AES/
NFE sweeps (US blank-USD CapEx residual exhausted; OxI >USD 14m is university+road
package — road-only share undisclosed; 0 new US CapEx this pass — honest residual).
PRC equal-budget: State Grid GATE UHV CapEx-fill; CTG Serra already dense; holdovers
unsigned.
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
BRL_FX_DATE = "2026-09-25"
MXN_USD = "17.6932"
MXN_FX_DATE = "2026-09-25"


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


# 1. building_materials / other — CapEx-fill Votorantim Xambioá R$260m
row_doc(
    "votorantim_xambioa_grind_2026",
    "infrastructure", "building_materials", "other",
    "Votorantim Cimentos — Xambioá new grinding line",
    "Brazil",
    "13 Aug 2026 Votorantim Cimentos 2Q26: announced investment of R$260 million for a new grinding line at Xambioá (Tocantins) adding 500,000 t/y (to 1.5 Mt/y) from July 2028. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~50.08m for stored R$260m face.",
    "260000000", BRL_FX_DATE, "2026", "-6.41", "-48.36",
    "Xambioá plant, Tocantins (company geography).",
    "votorantim_2q26_xambioa_20260813",
    "In July, we announced an investment of R$260 million for the construction of a new grinding line at the Xambioá plant, which will add 500,000 tonnes to the site’s current production capacity, bringing the total to 1.5 million tonnes/year starting in July 2028.",
    "https://www.votorantimcimentos.com/news/our-financial-results-in-the-second-quarter-of-2026/",
    "Actor: Votorantim Cimentos (Brazilian) — other (host-country industrial). CapEx-fill: retain R$260m; add Fed H.10 Sep 25 2026 FX to USD ~50.08m. Shuffle building_materials.",
    "hunt_cycle228", investment_type="capex_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(260000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Votorantim Cimentos. “Our Financial Results in the Second Quarter of 2026.” August 13, 2026. https://www.votorantimcimentos.com/news/our-financial-results-in-the-second-quarter-of-2026/.',
    annotation="Votorantim Xambioá CapEx-fill ~USD 50.08m via Fed H.10. Supports votorantim_xambioa_grind_2026.",
    evid_note="Opened Votorantim English 2Q26; R$260m / Xambioá grinding line / +500 kt confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 2. building_materials / other — CapEx-fill Votorantim FY2025 CapEx R$3.7bn
row_doc(
    "votorantim_fy2025_capex_3p7bn_brl",
    "infrastructure", "building_materials", "other",
    "Votorantim Cimentos — FY2025 CapEx",
    "Brazil",
    "18 Mar 2026 Votorantim Cimentos: investments (Capex) totaled R$3.7 billion in 2025 (+14% YoY), focused on structural competitiveness, capacity expansion, decarbonization and new businesses. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~712.62m for stored R$3.7bn face.",
    "3700000000", BRL_FX_DATE, "2025", "", "",
    "Votorantim Cimentos Brazil CapEx (national footprint; no single-site pin).",
    "votorantim_fy2025_results_20260318",
    "Our investments (Capex) totaled R$3.7 billion, up 14% compared to the previous year, and focused on structural competitiveness, capacity expansion, decarbonization and new businesses.",
    "https://www.votorantimcimentos.com/news/our-2025-financial-results/",
    "Actor: Votorantim Cimentos (Brazilian) — other. CapEx-fill: retain R$3.7bn FY2025 CapEx; add Fed H.10 Sep 25 2026 FX to USD ~712.62m. Shuffle building_materials.",
    "hunt_cycle228", investment_type="capex_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(3700000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Votorantim Cimentos. “Our 2025 financial results.” March 18, 2026. https://www.votorantimcimentos.com/news/our-2025-financial-results/.',
    annotation="Votorantim FY2025 CapEx-fill ~USD 712.62m via Fed H.10. Supports votorantim_fy2025_capex_3p7bn_brl.",
    evid_note="Opened Votorantim English FY2025; R$3.7bn CapEx confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 3. power_plants_grid / allied — CapEx-fill ISA Energia FY2025 R$5.1bn
row_doc(
    "isa_energia_fy2025_capex_5p1bn_brl",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — FY2025 CapEx record",
    "Brazil",
    "24 Feb 2026 ISA Energia Brasil: CapEx recorde de R$ 5,1 bilhões in 2025 (+40.4% / +R$1.46bn YoY); R$3.4bn greenfield concessions + R$1.69bn Reforços & Melhorias. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~982.26m for stored R$5.1bn face. Distinct from isa_energia_rm_370m_brl_1t26 (Q1 2026 R&M only).",
    "5100000000", BRL_FX_DATE, "2025", "", "",
    "ISA Energia Brasil national transmission CapEx (no single-site pin).",
    "isa_energia_4t25_results_20260224",
    "No acumulado de 2025, a Companhia atingiu um novo patamar de execução com o CapEx recorde de R$ 5,1 bilhões, um crescimento expressivo de R$ 1,46 bilhão (+40,4%).",
    "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-divulga-os-resultados-do-4t25-com-recorde-em-investimentos-de-r-51-bi-no-ano/",
    "Actor: ISA Energia Brasil (Colombia ISA / allied) — allied. CapEx-fill: retain R$5.1bn FY2025; add Fed H.10 Sep 25 2026 FX to USD ~982.26m. Shuffle power_plants_grid.",
    "hunt_cycle228", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(5100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ISA Energia Brasil. “ISA ENERGIA BRASIL divulga os resultados do 4T25 com recorde em investimentos de R$ 5,1 bi no ano.” February 24, 2026. https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/isa-energia-brasil-divulga-os-resultados-do-4t25-com-recorde-em-investimentos-de-r-51-bi-no-ano/.',
    annotation="ISA Energia FY2025 CapEx-fill ~USD 982.26m via Fed H.10. Supports isa_energia_fy2025_capex_5p1bn_brl.",
    evid_note="Opened ISA Energia Portuguese 4T25; R$5.1bn CapEx record confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. power_plants_grid / allied — CapEx-fill Neoenergia FY2025 R$10.1bn
row_doc(
    "neoenergia_fy2025_capex_10p1bn_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — FY2025 CapEx",
    "Brazil",
    "11 Feb 2026 Neoenergia: CapEx em 2025 da ordem de R$ 10,1 bilhões (R$6.5bn distribuição; ~R$3.3bn transmissão). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~1945.27m for stored R$10.1bn face.",
    "10100000000", BRL_FX_DATE, "2025", "", "",
    "Neoenergia Brazil distribution/transmission CapEx (national footprint; no single-site pin).",
    "neoenergia_fy2025_results_20260211",
    "Com foco no cliente e na melhoria contínua nos serviços, companhia registrou no CAPEX em 2025, de R$ 10,1 bilhões - sendo R$ 6,5 bilhões em distribuição",
    "https://www.neoenergia.com/w/2025-tem-lucro-de-5-bilhoes-1",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. CapEx-fill: retain R$10.1bn FY2025; add Fed H.10 Sep 25 2026 FX to USD ~1945.27m. Shuffle power_plants_grid.",
    "hunt_cycle228", investment_type="capex_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(10100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Neoenergia. “Neoenergia encerra 2025 com lucro de R$ 5 bilhões.” February 11, 2026. https://www.neoenergia.com/w/2025-tem-lucro-de-5-bilhoes-1.',
    annotation="Neoenergia FY2025 CapEx-fill ~USD 1945.27m via Fed H.10. Supports neoenergia_fy2025_capex_10p1bn_brl.",
    evid_note="Opened Neoenergia Portuguese FY2025; R$10.1bn CapEx / R$6.5bn distribution confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. power_plants_grid / prc — CapEx-fill State Grid GATE UHV R$18bn
row_doc(
    "state_grid_ne_uhv_construction_2026",
    "energy", "power_plants_grid", "prc",
    "State Grid Brazil Holding — Northeast Brazil UHVDC (GATE)",
    "Brazil",
    "State Grid Brazil Holding company Portuguese: GATE (Graça Aranha Transmissora de Energia) ±800 kV / 1,468 km UHVDC Graça Aranha (MA)–Silvânia (GO) with two converter stations — R$ 18 billion destined CapEx; construction launch ~30 Jun 2025 / operating target 2029. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~3466.81m for stored R$18bn face. Distinct from Belo Monte UHV phases.",
    "18000000000", BRL_FX_DATE, "2026", "-16.66", "-48.61",
    "Silvânia converter station launch site, Goiás (company geography); line Graça Aranha MA–Silvânia GO.",
    "stategrid_gate_silvania_18bn",
    "A State Grid Brazil Holding (SGBH) —subsidiária de um dos maiores grupos de energia do mundo, a State Grid Corporation of China (SGCC) — lançará em 30/6, em Silvânia (GO), a pedra fundamental do “Projeto de Ultra Alta Tensão no Nordeste do Brasil”, para o qual serão destinados R$ 18 bilhões.",
    "https://stategrid.com.br/municipio-goiano-de-silvania-sedia-lancamento-do-mais-caro-projeto-de-ultra-alta-tensao-800kv-da-historia-do-setor-eletrico-do-brasil/",
    "Actor: State Grid Brazil Holding (PRC SOE subsidiary) — prc. CapEx-fill: retain R$18bn GATE UHV CapEx; add Fed H.10 Sep 25 2026 FX to USD ~3466.81m. Shuffle power_plants_grid.",
    "hunt_cycle228", investment_type="concession_construction", evidence="documented", currency="BRL",
    value_usd=str(round(18000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='State Grid Brazil Holding. “Município goiano de Silvânia sedia lançamento do mais caro projeto de ultra alta tensão (±800 kV) da história do setor elétrico do Brasil.” https://stategrid.com.br/municipio-goiano-de-silvania-sedia-lancamento-do-mais-caro-projeto-de-ultra-alta-tensao-800kv-da-historia-do-setor-eletrico-do-brasil/.',
    annotation="State Grid GATE UHV CapEx-fill ~USD 3466.81m via Fed H.10. Supports state_grid_ne_uhv_construction_2026.",
    evid_note="Opened SGBH Portuguese; R$18bn / ±800 kV / 1,468 km GATE confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. port_ownership / other — CapEx-fill Hutchison EIT Ensenada MXN 2.3bn
row_doc(
    "hutchison_eit_ensenada_2022",
    "infrastructure", "port_ownership", "other",
    "Hutchison Ports EIT — Ensenada terminal expansion",
    "Mexico",
    "Hutchison Ports Mexico news: inversión total de 2,300 millones de pesos for Ensenada terminal expansion (additional 300 m quay, 4.0 ha yard, wave wall; capacity to 565k TEU). CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~129.99m for stored MXN 2.3bn face.",
    "2300000000", MXN_FX_DATE, "2022", "31.8667", "-116.6167",
    "Hutchison Ports EIT, Ensenada, Baja California (company geography).",
    "hutchison_eit_ensenada_news",
    "Con una inversión total de 2,300 millones de pesos destinados a la ampliación de su terminal en el Puerto de Ensenada, Hutchison Ports EIT busca aumentar significativamente su capacidad de operación",
    "https://www.hutchisonports.com.mx/newsroom/Hutchison-Ports-eit-invierte-2300-millones-de-pesos-en-ampliacion-de-su-Terminal",
    "Actor: Hutchison Ports (HK) — other. CapEx-fill: retain MXN 2.3bn; add Fed H.10 Sep 25 2026 FX to USD ~129.99m. Shuffle port_ownership.",
    "hunt_cycle228", investment_type="concession", evidence="documented", currency="MXN",
    value_usd=str(round(2300000000 / float(MXN_USD), 2)), fx_usd=MXN_USD, bib_type="company",
    chicago='Hutchison Ports México. “Hutchison Ports EIT invierte 2,300 millones de pesos en ampliación de su Terminal.” https://www.hutchisonports.com.mx/newsroom/Hutchison-Ports-eit-invierte-2300-millones-de-pesos-en-ampliacion-de-su-Terminal.',
    annotation="Hutchison EIT Ensenada CapEx-fill ~USD 129.99m via Fed H.10. Supports hutchison_eit_ensenada_2022.",
    evid_note="Opened Hutchison Ports México Spanish; MXN 2,300m Ensenada expansion confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 7. port_ownership / other — CapEx-fill ICTSI Rio Brasil R$948m
row_doc(
    "ictsi_rio_brasil_expansion_2025",
    "infrastructure", "port_ownership", "other",
    "ICTSI Rio Brasil Terminal — 2025–2029 expansion/modernization",
    "Brazil",
    "15 Dec 2025 ICTSI: total investment of R$948 million (≈R$414.4m infrastructure + R$533.5m equipment) to expand/modernize Rio Brasil Terminal 2025–2029; capacity 440k→750k TEU/year. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~182.58m for stored R$948m face.",
    "948000000", BRL_FX_DATE, "2025", "-22.89", "-43.18",
    "ICTSI Rio Brasil Terminal, Port of Rio de Janeiro (company geography).",
    "ictsi_rio_brasil_20251215",
    "The total investment of R$948 million comprises approximately R$414.4 million in infrastructure works and R$533.5 million in the acquisition of state-of-the-art equipment.",
    "https://ictsi.com/press-releases/ictsi-invest-r948-million-expand-modernize-rio-brasil-terminal",
    "Actor: ICTSI (Philippines) — other. CapEx-fill: retain R$948m; add Fed H.10 Sep 25 2026 FX to USD ~182.58m. Shuffle port_ownership.",
    "hunt_cycle228", investment_type="concession_capex", evidence="documented", currency="BRL",
    value_usd=str(round(948000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ICTSI. “ICTSI to invest R$948 million to expand, modernize Rio Brasil Terminal.” December 15, 2025. https://ictsi.com/press-releases/ictsi-invest-r948-million-expand-modernize-rio-brasil-terminal.',
    annotation="ICTSI Rio Brasil CapEx-fill ~USD 182.58m via Fed H.10. Supports ictsi_rio_brasil_expansion_2025.",
    evid_note="Opened ICTSI English; R$948m / 440k→750k TEU confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 8. port_ownership / other — CapEx-fill Portonave quay R$1.5bn
row_doc(
    "portonave_cais_1p5bn_brl_2026",
    "infrastructure", "port_ownership", "other",
    "Portonave — quay modernization phase 2 (~R$1.5bn)",
    "Brazil",
    "28 Nov 2025 Portonave: second-phase quay adequacy works totaling approximately R$1.5 billion (plus R$439m equipment; combined ~R$2bn program); depth 17 m / up to 400 m LOA vessels; capacity 1.5→2.0m TEU by end-2026. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~288.90m for stored R$1.5bn quay face (equipment tranche not double-counted here).",
    "1500000000", BRL_FX_DATE, "2026", "-26.89", "-48.65",
    "Portonave terminal, Navegantes, Santa Catarina (company geography).",
    "portonave_cais_2bn_program_2026",
    "a Portonave realiza a segunda etapa da obra de adequação do cais, com investimentos que totalizam aproximadamente R$ 1,5 bilhão e R$ 439 milhões em novos equipamentos",
    "https://www.portonave.com.br/pt/todas-as-noticias/investimentos-da-portonave-na-modernizacao-do-cais-e-em-novos-equipamentos-chegam-a-rusd-2-bilhoes",
    "Actor: Portonave S.A. (Brazilian private terminal) — other. CapEx-fill: retain R$1.5bn quay face; add Fed H.10 Sep 25 2026 FX to USD ~288.90m. Shuffle port_ownership.",
    "hunt_cycle228", investment_type="expansion", evidence="documented", currency="BRL",
    value_usd=str(round(1500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Portonave. “Investimentos da Portonave na modernização do cais e em novos equipamentos chegam a R$ 2 bilhões.” November 28, 2025. https://www.portonave.com.br/pt/todas-as-noticias/investimentos-da-portonave-na-modernizacao-do-cais-e-em-novos-equipamentos-chegam-a-rusd-2-bilhoes.',
    annotation="Portonave quay CapEx-fill ~USD 288.90m via Fed H.10. Supports portonave_cais_1p5bn_brl_2026.",
    evid_note="Opened Portonave Portuguese; ~R$1.5bn quay / R$439m equipment / ~R$2bn program confirmed. CapEx-fill uses quay R$1.5bn face via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 9. niobium / allied — CapEx-fill CBMM R$13bn 2026–2031 (thin next)
row_doc(
    "cbmm_araxa_13bn_plan_2026",
    "resources", "niobium", "allied",
    "CBMM — planned investments ~R$13bn (2026–2031)",
    "Brazil",
    "18 Sep 2026 Diário do Comércio (company note to press): CBMM planeja investimentos da ordem de R$ 13 bilhões entre 2026 e 2031 (capacity expansion, new materials/applications, tech/innovation/infrastructure); R$2bn already invested in 2026 at Araxá. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~2503.80m for stored R$13bn face. UNVERIFIED proxy press citing company note. Distinct from cbmm_araxa_capex_plan_2025 (R$10bn five-year).",
    "13000000000", BRL_FX_DATE, "2026", "-19.59", "-46.94",
    "CBMM Araxá, Minas Gerais (company geography).",
    "diario_comercio_cbmm_13bn_20260918",
    "A Companhia Brasileira de Metalurgia e Mineração (CBMM) planeja investimentos da ordem de R$ 13 bilhões entre 2026 e 2031 para dar continuidade à estratégia de crescimento de longo prazo",
    "https://diariodocomercio.com.br/economia/cbmm-niobio-investimentos/",
    "Actor: CBMM (Brazilian Moreira Salles–controlled) — allied. CapEx-fill: retain R$13bn 2026–2031 plan; add Fed H.10 Sep 25 2026 FX to USD ~2503.80m. Thin next-thinnest niobium (balsa/nickel/fission_smr dry).",
    "hunt_cycle228", investment_type="capex_plan", evidence="proxy", currency="BRL",
    value_usd=str(round(13000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Diário do Comércio. “Mineira CBMM planeja investimentos de R$ 13 bilhões até 2031.” September 18, 2026. https://diariodocomercio.com.br/economia/cbmm-niobio-investimentos/.',
    annotation="CBMM R$13bn CapEx-fill ~USD 2503.80m via Fed H.10 (proxy press). Supports cbmm_araxa_13bn_plan_2026.",
    evid_note="Opened Diário do Comércio Portuguese; R$13bn / 2026–2031 plan / R$2bn 2026 Araxá spend confirmed as company note to press (proxy). CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
    print(f"cycle228 added {len(added)}: {added}")
    print(f"cycle228 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
