#!/usr/bin/env python3
"""Cycle 40 hunt: shuffle_seed=20261040; equal budget across 18 subcategories."""
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


# seed 20261040 order:
# bridges_roads, nickel, lithium, solar, other_renewables, water, balsa,
# port_cranes, fission_smr, niobium, building_materials, port_ownership,
# graphite, engineering_epc, copper, wind, power_plants_grid, rail

# 1 infrastructure/bridges_roads — CAF up to USD 150m loan for Salvador–Itaparica
A(
    {
        "id": "caf_salvador_itaparica_150m_2024",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "allied",
        "counterpart": "CAF — loan to Bahia for Sistema Viário Ponte Salvador–Itaparica",
        "country": "Brazil",
        "asset": "11–12 Dec 2024: Bahia state signs financing contract with CAF (Banco de Desarrollo de América Latina y el Caribe) for up to USD 150 million (~R$800m cited) toward Sistema Viário Integrado Ponte Salvador–Ilha de Itaparica — partial financing of FGAP guarantee-fund contributions and BA-001 complementary works (Nazaré das Farinhas–Ponte do Funil). Distinct from Chinese CCECC/CCCC PPP concession row.",
        "investment_type": "financing",
        "value": "150000000",
        "currency": "USD",
        "value_usd": "150000000",
        "fx_usd": "1",
        "fx_date": "2024-12-12",
        "year": "2024",
        "status": "active",
        "lat": "-12.95",
        "lon": "-38.55",
        "geo_note": "Salvador–Itaparica bay crossing (same corridor as Chinese PPP; press geography).",
        "evidence": "proxy",
        "source_id": "g1_caf_salvador_itaparica_20241212",
        "note": "Actor: CAF (Latin American multilateral development bank — allied). UNVERIFIED proxy: g1 BA 12 Dec 2024. Complements PRC concessionaire PPP (ccecc_cccc_salvador_itaparica_2025) with multilateral FGAP financing — not a matched auction pair.",
    },
    {
        "id": "caf_salvador_itaparica_150m_2024",
        "retrieved": "2026-10-01",
        "source_id": "g1_caf_salvador_itaparica_20241212",
        "url": "https://g1.globo.com/ba/bahia/noticia/2024/12/12/governo-da-bahia-assina-contrato-de-emprestimo-para-construcao-da-ponte-salvador-itaparica.ghtml",
        "price_year": "2024",
        "evidence": "proxy",
        "quote": "O acordo liberado pelo Senado Federal prevê empréstimo de até US$ 150 milhões, que pode chegar a R$ 800 milhões quando convertidos para a moeda brasileira. ... Banco de Desenvolvimento da América Latina e do Caribe (CAF), que irá financiar o dinheiro.",
        "note": "Opened g1 Portuguese 12 Dec 2024. Mark UNVERIFIED proxy.",
    },
    {
        "id": "g1_caf_salvador_itaparica_20241212",
        "type": "trade_press",
        "chicago": "g1 BA. “Governo da Bahia assina contrato de empréstimo para construção da Ponte Salvador-Itaparica; acordo prevê até US$ 150 milhões.” g1 / TV Globo, 12 December 2024.",
        "url": "https://g1.globo.com/ba/bahia/noticia/2024/12/12/governo-da-bahia-assina-contrato-de-emprestimo-para-construcao-da-ponte-salvador-itaparica.ghtml",
        "annotation": "Press on CAF up to USD 150m loan for Salvador–Itaparica FGAP/BA-001. Supports caf_salvador_itaparica_150m_2024.",
        "supports": ["caf_salvador_itaparica_150m_2024", "hunt_infra_bridges_roads"],
    },
)

# 2 resources/nickel — miss (MMG/Anglo already; Araguaia Chinese interest unconfirmed)

# 3 resources/lithium — miss (Ganfeng Mariana plant already; solar carved to energy/solar)

# 4 energy/solar — Ganfeng Mariana supporting solar park USD 190m
A(
    {
        "id": "ganfeng_mariana_solar_190m_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Ganfeng Lithium — supporting solar park for Mariana LiCl plant (Salta)",
        "country": "Argentina",
        "asset": "Feb 2025 company/press: alongside Mariana lithium chloride plant start-up (USD 790m / 20 ktpa LiCl from Salar de Llullaillaco), Ganfeng reports USD 190 million invested in a supporting solar park to power the plant. Distinct from ganfeng_mariana_production_2025 (plant CAPEX row).",
        "investment_type": "greenfield_generation",
        "value": "190000000",
        "currency": "USD",
        "value_usd": "190000000",
        "fx_usd": "1",
        "fx_date": "2025-02-13",
        "year": "2025",
        "status": "active",
        "lat": "-24.72",
        "lon": "-68.55",
        "geo_note": "Salar de Llullaillaco / Mariana industrial area, Salta (press geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "redimin_ganfeng_mariana_20250213",
        "note": "Actor: Ganfeng Lithium (PRC). UNVERIFIED proxy: REDIMIN 13 Feb 2025 summarizing company inauguration figures. Solar CAPEX separated from plant row for layer taxonomy.",
    },
    {
        "id": "ganfeng_mariana_solar_190m_2025",
        "retrieved": "2026-10-01",
        "source_id": "redimin_ganfeng_mariana_20250213",
        "url": "https://www.redimin.cl/ganfeng-lithium-inicia-produccion-de-litio-en-argentina-con-inversion-de-790-millones-de-dolares-en-salta",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "Además, la compañía ha invertido 190 millones de dólares en la construcción de un parque solar destinado a abastecer las necesidades energéticas de la planta.",
        "note": "Opened REDIMIN Spanish 13 Feb 2025. Mark UNVERIFIED proxy.",
    },
    {
        "id": "redimin_ganfeng_mariana_20250213",
        "type": "trade_press",
        "chicago": "Recabarren Ortiz, Cristian. “Ganfeng Lithium inicia producción de litio en Argentina con inversión de 790 millones de dólares en Salta.” REDIMIN, 13 February 2025.",
        "url": "https://www.redimin.cl/ganfeng-lithium-inicia-produccion-de-litio-en-argentina-con-inversion-de-790-millones-de-dolares-en-salta",
        "annotation": "Press on Ganfeng Mariana USD 190m supporting solar. Supports ganfeng_mariana_solar_190m_2025.",
        "supports": ["ganfeng_mariana_solar_190m_2025", "hunt_energy_solar"],
    },
)

# 5 energy/other_renewables — BYD up to R$500m BESS manufacturing Brazil
A(
    {
        "id": "byd_brazil_bess_factory_500m_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "BYD — industrial BESS production capacity in Brazil (Manaus candidate)",
        "country": "Brazil",
        "asset": "Jun/Sep 2026: BYD announces intent to invest up to R$ 500 million in phased industrial capacity to produce stationary BESS systems in Brazil — expand Manaus battery plant or new unit (location TBD pending studies and MME Portaria 136); 300–400 direct jobs initially; aimed at LRCAP storage demand and C&I. Distinct from byd_grenergy_central_oasis_2026 (Chile supply).",
        "investment_type": "greenfield_plant",
        "value": "500000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-3.1",
        "lon": "-60.02",
        "geo_note": "Manaus (AM) cited as leading expansion option; final site TBD (press geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "poder360_byd_bess_20260612",
        "note": "Actor: BYD (PRC). UNVERIFIED proxy: Poder360 12 Jun 2026 / pv magazine Brasil 8 Sep 2026. Up-to amount; location not final.",
    },
    {
        "id": "byd_brazil_bess_factory_500m_2026",
        "retrieved": "2026-10-01",
        "source_id": "poder360_byd_bess_20260612",
        "url": "https://www.poder360.com.br/poder-economia/byd-anuncia-investimento-de-ate-r-500-mi-em-baterias-no-brasil/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "A montadora chinesa BYD vai investir até R$ 500 milhões na produção de sistemas de armazenamento de energia em baterias no Brasil. O projeto pode ampliar a fábrica de Manaus (AM) ou levar à construção de uma nova unidade industrial no país, ainda sem localização definida.",
        "note": "Opened Poder360 Portuguese 12 Jun 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "poder360_byd_bess_20260612",
        "type": "trade_press",
        "chicago": "Poder360. “BYD anuncia investimento de até R$ 500 mi em baterias no Brasil.” Poder360, 12 June 2026.",
        "url": "https://www.poder360.com.br/poder-economia/byd-anuncia-investimento-de-ate-r-500-mi-em-baterias-no-brasil/",
        "annotation": "Press on BYD up to R$500m Brazil BESS factory. Supports byd_brazil_bess_factory_500m_2026.",
        "supports": ["byd_brazil_bess_factory_500m_2026", "hunt_energy_other_renewables"],
    },
)

# 6 resources/water — Sacyr Antofagasta reuse concession ~USD 292m
A(
    {
        "id": "sacyr_antofagasta_reuse_292m_2025",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Sacyr Agua — Planta de Reúso Salar del Carmen (Antofagasta)",
        "country": "Chile",
        "asset": "8 May 2025 Sacyr: awarded Econssa concession for wastewater treatment/reuse and commercialization in Antofagasta — new Salar del Carmen plant to ~900 l/s final capacity for mining customers; ~USD 292 million investment; 35-year concession; COD targeted 2028; includes ~16 km conveyance plus laterals to La Negra and Mantos Blancos. Distinct from sacyr_coquimbo_desal_2026.",
        "investment_type": "concession",
        "value": "292000000",
        "currency": "USD",
        "value_usd": "292000000",
        "fx_usd": "1",
        "fx_date": "2025-05-08",
        "year": "2025",
        "status": "active",
        "lat": "-23.65",
        "lon": "-70.27",
        "geo_note": "Salar del Carmen sector, Antofagasta (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "sacyr_antofagasta_reuse_20250508",
        "note": "Actor: Sacyr Agua (Spain) — allied. Company primary 8 May 2025. Distinct from Coquimbo desal and Zaldívar water rows.",
    },
    {
        "id": "sacyr_antofagasta_reuse_292m_2025",
        "retrieved": "2026-10-01",
        "source_id": "sacyr_antofagasta_reuse_20250508",
        "url": "https://www.sacyr.com/-/planta-reuso-agua-antofagasta",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Sacyr Agua invertirá cerca de 292 millones de dólares en desarrollar el mayor proyecto de reúso de agua de Latinoamérica. ... El plazo de la concesión es de 35 años.",
        "note": "Opened Sacyr company Spanish release 8 May 2025.",
    },
    {
        "id": "sacyr_antofagasta_reuse_20250508",
        "type": "company",
        "chicago": "Sacyr. “Sacyr se adjudica la concesión del tratamiento de agua para el reúso y de su comercialización en Antofagasta (Chile).” Press release, 8 May 2025.",
        "url": "https://www.sacyr.com/-/planta-reuso-agua-antofagasta",
        "annotation": "Company release on Antofagasta reuse concession ~USD 292m. Supports sacyr_antofagasta_reuse_292m_2025.",
        "supports": ["sacyr_antofagasta_reuse_292m_2025", "hunt_res_water"],
    },
)

# 7 resources/balsa — miss (AIMA 2025 shares / Plantabal already)

# 8 infrastructure/port_cranes — miss (ZPMC Tecon Santos / Konecranes Acajutla already)

# 9 energy/fission_smr — INB–Westinghouse fuel-cycle cooperation
A(
    {
        "id": "inb_westinghouse_fuel_coop_2026",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "us",
        "counterpart": "Westinghouse Electric — cooperation with INB on Brazil nuclear fuel cycle",
        "country": "Brazil",
        "asset": "15 May 2026: Indústrias Nucleares do Brasil (INB) and U.S. Westinghouse Electric meet in the United States on expanding technical/industrial cooperation to raise domestic uranium production and fuel-cycle localization toward PNE 2050 nuclear expansion (~14 GW / ~3,000 t U cited). Also notes future SMR evaluation alongside Angra 3 discussions. Presence/MoU-stage — no CAPEX disclosed.",
        "investment_type": "technology_mou",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-22.98",
        "lon": "-44.37",
        "geo_note": "Pinned to Angra nuclear complex / INB fuel-cycle geography (Rio de Janeiro coast; approximate).",
        "evidence": "proxy",
        "source_id": "cenario_inb_westinghouse_20260515",
        "note": "Actor: Westinghouse (U.S.) with INB — us. UNVERIFIED proxy: Cenário Energia 15 May 2026. Cooperation/presence; no priced EPC.",
    },
    {
        "id": "inb_westinghouse_fuel_coop_2026",
        "retrieved": "2026-10-01",
        "source_id": "cenario_inb_westinghouse_20260515",
        "url": "https://cenarioenergia.com.br/2026/05/15/inb-e-westinghouse-avancam-em-parceria-estrategica-para-sustentar-expansao-nuclear-prevista-no-pne-2050/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Em reunião realizada nos Estados Unidos, a Indústrias Nucleares do Brasil (INB) e a Westinghouse Electric Company discutiram a ampliação da cooperação técnica e industrial voltada ao fortalecimento da cadeia nacional de combustível nuclear",
        "note": "Opened Cenário Energia Portuguese 15 May 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "cenario_inb_westinghouse_20260515",
        "type": "trade_press",
        "chicago": "Agência Cenário Energia. “INB e Westinghouse avançam em parceria estratégica para sustentar expansão nuclear prevista no PNE 2050.” Cenário Energia, 15 May 2026.",
        "url": "https://cenarioenergia.com.br/2026/05/15/inb-e-westinghouse-avancam-em-parceria-estrategica-para-sustentar-expansao-nuclear-prevista-no-pne-2050/",
        "annotation": "Press on INB–Westinghouse fuel-cycle cooperation. Supports inb_westinghouse_fuel_coop_2026.",
        "supports": ["inb_westinghouse_fuel_coop_2026", "hunt_energy_fission_smr"],
    },
)

# 10 resources/niobium — Codemig–CBMM Araxá renewal through 2070
A(
    {
        "id": "codemig_cbmm_renewal_2070_2025",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "other",
        "counterpart": "Codemig–CBMM — Araxá niobium partnership renewal",
        "country": "Brazil",
        "asset": "30 Oct 2025: Minas Gerais Codemig and CBMM sign new Araxá niobium exploration/profit-sharing agreement replacing instrument that would expire 2032 — 30 years with optional +15 years (to 2070); Codemig keeps 25% of CBMM net profits on niobium and gains 25% on other materials (incl. rare earths) without additional Codemig capex. Comipa JV remains Codemig 51% / CBMM 49%. Distinct from cbmm_araxa_13bn_plan_2026 CAPEX cycle.",
        "investment_type": "concession",
        "value": "",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-19.593",
        "lon": "-46.943",
        "geo_note": "Araxá / Complexo do Barreiro, Minas Gerais (company geography).",
        "evidence": "proxy",
        "source_id": "ofator_codemig_cbmm_20251030",
        "note": "Actors: Codemig (Minas Gerais SOE) + CBMM (Moreira Salles; Chinese consortium holds ~15% non-controlling) — other. UNVERIFIED proxy: O Fator 30 Oct 2025. Presence/renewal; no new disclosed CAPEX figure.",
    },
    {
        "id": "codemig_cbmm_renewal_2070_2025",
        "retrieved": "2026-10-01",
        "source_id": "ofator_codemig_cbmm_20251030",
        "url": "https://ofator.com.br/informacao/codemig-e-cbmm-renovam-acordo-para-exploracao-do-niobio-de-araxa/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "O governo de Minas e a Companhia de Desenvolvimento Econômico de Minas Gerais (Codemig) renovaram nesta quinta-feira (30), por mais 30 anos, o contrato com a Companhia Brasileira de Metalurgia e Mineração (CBMM) para exploração de nióbio em Araxá ... pode ser prorrogado por mais 15 anos, até 2070.",
        "note": "Opened O Fator Portuguese 30 Oct 2025. Mark UNVERIFIED proxy.",
    },
    {
        "id": "ofator_codemig_cbmm_20251030",
        "type": "trade_press",
        "chicago": "Ragazzi, Lucas. “Codemig e CBMM renovam acordo para exploração do nióbio de Araxá.” O Fator, 30 October 2025.",
        "url": "https://ofator.com.br/informacao/codemig-e-cbmm-renovam-acordo-para-exploracao-do-niobio-de-araxa/",
        "annotation": "Press on Codemig–CBMM Araxá renewal to 2070. Supports codemig_cbmm_renewal_2070_2025.",
        "supports": ["codemig_cbmm_renewal_2070_2025", "hunt_fenb_araxa"],
    },
)

# 11 infrastructure/building_materials — miss

# 12 infrastructure/port_ownership — Cosco Chancay Phase I USD 1.3bn value fill (upgrade)
A(
    {
        "id": "cosco_chancay_port_2024",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "prc",
        "counterpart": "COSCO Shipping Ports Chancay Perú — Phase I megaport",
        "country": "Peru",
        "asset": "Chancay Port Phase I (4 berths; COSCO first green/smart port investment in South America). Gestión 6 Nov 2024: Cosco/Volcan cite Phase I construction cost USD 1,300 million; master plan toward 15 berths could reach ~USD 3,500 million if demand and rail connectivity advance.",
        "investment_type": "ownership_equity",
        "value": "1300000000",
        "currency": "USD",
        "value_usd": "1300000000",
        "fx_usd": "1",
        "fx_date": "2024-11-06",
        "year": "2024",
        "status": "active",
        "lat": "-11.574",
        "lon": "-77.270",
        "geo_note": "Puerto de Chancay, Lima region.",
        "evidence": "proxy",
        "source_id": "gestion_chancay_3500m_20241106",
        "note": "Actor: COSCO Shipping Ports (PRC) 60% with Volcan 40%. UNVERIFIED proxy value fill: Gestión 6 Nov 2024 citing Cosco institutional affairs (Phase I USD 1.3bn; master ~USD 3.5bn contingent). Cycle 40 upgrade of prior presence row.",
    },
    {
        "id": "cosco_chancay_port_2024",
        "retrieved": "2026-10-01",
        "source_id": "gestion_chancay_3500m_20241106",
        "url": "https://gestion.pe/economia/inversion-total-del-puerto-de-chancay-sumaria-us-3500-millones-de-que-depende-megapuerto-de-chancay-cosco-shipping-noticia/",
        "price_year": "2024",
        "evidence": "proxy",
        "quote": "El puerto de Chancay inaugurará su primera etapa, que implicó destinar US$ 1,300 millones a su construcción ... contemplan una inversión total que bordearía los US$ 3,500 millones",
        "note": "Opened Gestión Spanish 6 Nov 2024. Mark UNVERIFIED proxy for Phase I USD figure.",
    },
    {
        "id": "gestion_chancay_3500m_20241106",
        "type": "trade_press",
        "chicago": "Gestión. “Inversión total del puerto de Chancay sumaría US$ 3,500 millones, ¿de qué depende?” Gestión (Peru), 6 November 2024.",
        "url": "https://gestion.pe/economia/inversion-total-del-puerto-de-chancay-sumaria-us-3500-millones-de-que-depende-megapuerto-de-chancay-cosco-shipping-noticia/",
        "annotation": "Press on Chancay Phase I USD 1.3bn and master ~USD 3.5bn. Supports cosco_chancay_port_2024 value fill.",
        "supports": ["cosco_chancay_port_2024", "hunt_infra_port_ownership"],
    },
)

# 13 resources/graphite — Graphcoa → Allied Graphite (US) anode offtake pathway
A(
    {
        "id": "graphcoa_allied_anode_offtake_2026",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "Graphcoa / Appian — Jordânia concentrate offtake to Allied Graphite (U.S. anode)",
        "country": "Brazil",
        "asset": "20 Jun 2026 Diário do Comércio interview: Graphcoa (Appian Capital Brazil) states majority of planned Jordânia (MG) flake concentrate (~50+ ktpa; commercial COD 2H 2029) is expected to go to Allied Graphite — Appian U.S. affiliate — for advanced processing to battery anode CSPG; Bahia Boa Sorte demo already shipped samples to U.S./Canada (~USD 50m spent on demo; >400 t concentrate). Distinct from graphcoa_jordania_dfs_capex_2026 CAPEX row.",
        "investment_type": "offtake",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-15.9",
        "lon": "-40.18",
        "geo_note": "Jordânia, Vale do Jequitinhonha, Minas Gerais (press geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "diario_comercio_graphcoa_20260620",
        "note": "Actor: Appian/Graphcoa (allied UK PE) with U.S. Allied Graphite anode path — allied. UNVERIFIED proxy: Diário do Comércio 20 Jun 2026. Offtake pathway; no disclosed offtake USD value.",
    },
    {
        "id": "graphcoa_allied_anode_offtake_2026",
        "retrieved": "2026-10-01",
        "source_id": "diario_comercio_graphcoa_20260620",
        "url": "https://diariodocomercio.com.br/economia/graphcoa-grafite-minas/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Contudo, a maior parte tende a ir para a Allied Graphite, empresa da Appian nos Estados Unidos, que fará o processamento avançado para elevar o teor do produto até a especificação para o ânodo de baterias.",
        "note": "Opened Diário do Comércio Portuguese 20 Jun 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "diario_comercio_graphcoa_20260620",
        "type": "trade_press",
        "chicago": "Henrique, Thyago. “Graphcoa planeja investir R$ 700 milhões em planta de grafite no Vale do Jequitinhonha.” Diário do Comércio, 20 June 2026.",
        "url": "https://diariodocomercio.com.br/economia/graphcoa-grafite-minas/",
        "annotation": "Press on Graphcoa→Allied Graphite U.S. anode offtake path. Supports graphcoa_allied_anode_offtake_2026.",
        "supports": ["graphcoa_allied_anode_offtake_2026", "hunt_res_graphite"],
    },
)

# 14 infrastructure/engineering_epc — miss
# 15 resources/copper — miss

# 16 energy/wind — Nordex first Ecuador order 112 MW + WEG/Statkraft Seabra 7 MW
A(
    {
        "id": "nordex_ecuador_112mw_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Nordex Group — first Ecuador order (19 × N149/5.X)",
        "country": "Ecuador",
        "asset": "17 Sep 2025 Nordex SE: first Ecuador order — 19 Delta4000 N149/5.X turbines for a 112 MW wind farm in southern Ecuador (customer/project name undisclosed); hub height 105 m; first turbine install Oct 2026; commissioning Mar 2027. Would raise national wind from ~69 MW to ~181 MW. Distinct from nordex_auren_cajuina3_2025 (Brazil).",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-3.99",
        "lon": "-79.2",
        "geo_note": "Southern Ecuador (company disclosure; site name undisclosed — approximate regional pin).",
        "evidence": "documented",
        "source_id": "nordex_ecuador_112mw_20250917",
        "note": "Actor: Nordex SE (Germany/Spain) — allied. Company primary 17 Sep 2025. Equipment supply; contract value not disclosed.",
    },
    {
        "id": "nordex_ecuador_112mw_2025",
        "retrieved": "2026-10-01",
        "source_id": "nordex_ecuador_112mw_20250917",
        "url": "https://www.nordex-online.com/en/2025/09/nordex-group-enters-ecuadorian-market-with-first-order-for-112-mw-wind-project/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The Nordex Group has secured a first order from Ecuador. A project developer has placed an order for 19 N149/5.X turbines for a wind farm located in the southern part of the country.",
        "note": "Opened Nordex company English release 17 Sep 2025.",
    },
    {
        "id": "nordex_ecuador_112mw_20250917",
        "type": "company",
        "chicago": "Nordex SE. “Nordex Group enters Ecuadorian market with first order for 112 MW wind project.” Press release, 17 September 2025.",
        "url": "https://www.nordex-online.com/en/2025/09/nordex-group-enters-ecuadorian-market-with-first-order-for-112-mw-wind-project/",
        "annotation": "Company release on Nordex 112 MW first Ecuador order. Supports nordex_ecuador_112mw_2025.",
        "supports": ["nordex_ecuador_112mw_2025", "hunt_energy_wind"],
    },
)

A(
    {
        "id": "weg_statkraft_seabra_7mw_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Statkraft / WEG / Petrobras — 7 MW onshore turbine at Seabra (Bahia)",
        "country": "Brazil",
        "asset": "18 Sep 2025 Statkraft: Petrobras–WEG–Statkraft put into operation a 7 MW WEG onshore turbine (Americas’ largest cited) at Parque Eólico Seabra, Complexo Brotas de Macaúbas (Bahia) for repowering; Petrobras R$ 130 million innovation investment (ANP/BNDES/MMA resources) co-developed the machine with WEG; Statkraft acquired/installed the unit. Commissioning completed Jul 2025.",
        "investment_type": "equipment_supply",
        "value": "130000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-12.42",
        "lon": "-41.77",
        "geo_note": "Seabra / Brotas de Macaúbas complex, Bahia (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "statkraft_weg_seabra_20250918",
        "note": "Actors: Statkraft (Norway — allied) buyer; WEG (Brazil) OEM; Petrobras R$130m innovation spend (other/host). Side=allied for Statkraft acquisition into operating fleet. Company primary.",
    },
    {
        "id": "weg_statkraft_seabra_7mw_2025",
        "retrieved": "2026-10-01",
        "source_id": "statkraft_weg_seabra_20250918",
        "url": "https://www.statkraft.com.br/sala-de-comunicacao/ultimas-noticias/2025/parceria-inovadora-entre-petrobras-weg-e-statkraft-coloca-em-operacao-o-maior-aerogerador-onshore-das-americas/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "O projeto é resultado de um investimento de R$130 milhões da Petrobrás ... E como parte do investimento em inovação tecnológica, o aerogerador foi adquirido pela Statkraft para o projeto de repowering do Parque Eólico de Seabra",
        "note": "Opened Statkraft Brasil Portuguese 18 Sep 2025.",
    },
    {
        "id": "statkraft_weg_seabra_20250918",
        "type": "company",
        "chicago": "Statkraft Brasil. “Parceria inovadora entre Petrobras, WEG e Statkraft coloca em operação o maior aerogerador onshore das Américas.” Press release, 18 September 2025.",
        "url": "https://www.statkraft.com.br/sala-de-comunicacao/ultimas-noticias/2025/parceria-inovadora-entre-petrobras-weg-e-statkraft-coloca-em-operacao-o-maior-aerogerador-onshore-das-americas/",
        "annotation": "Company release on WEG 7 MW Seabra turbine / Petrobras R$130m. Supports weg_statkraft_seabra_7mw_2025.",
        "supports": ["weg_statkraft_seabra_7mw_2025", "hunt_energy_wind"],
    },
)

# 17 energy/power_plants_grid — miss new deals; quality: fill xdcb lat/lon to Silvânia receiving end
# 18 infrastructure/rail — miss

# Quality fixes: fill missing lat/lon for active site-like rows
COORD_FIXES = {
    "recurrent_ciranda_solar_br_2023": {
        "lat": "-7.96",
        "lon": "-38.63",
        "geo_note": "São José do Belmonte, Pernambuco (Ciranda Cluster / Ciranda I–II public project geography).",
    },
    "xdcb_brazil_ne_uhv_ct_2024": {
        "lat": "-16.66",
        "lon": "-48.61",
        "geo_note": "Pinned to Silvânia (GO) receiving-end converter station of State Grid NE ±800 kV UHVDC (public project geography; approximate).",
    },
    # Ecuador balsa trade-flow rows: pin to Guayas/Los Ríos processing belt cited in public forestry press
    "wits_ecuador_balsa_china_2022": {
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Quevedo / Guayas–Los Ríos balsa processing belt (export-origin proxy; not a single mill pin).",
    },
    "wits_ecuador_balsa_us_2022": {
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Quevedo / Guayas–Los Ríos balsa processing belt (export-origin proxy; not a single mill pin).",
    },
    "wits_ecuador_balsa_china_2023": {
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Quevedo / Guayas–Los Ríos balsa processing belt (export-origin proxy; not a single mill pin).",
    },
    "wits_ecuador_balsa_us_2023": {
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Quevedo / Guayas–Los Ríos balsa processing belt (export-origin proxy; not a single mill pin).",
    },
    "wits_ecuador_balsa_china_2024": {
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Quevedo / Guayas–Los Ríos balsa processing belt (export-origin proxy; not a single mill pin).",
    },
    "wits_ecuador_balsa_us_2024": {
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Quevedo / Guayas–Los Ríos balsa processing belt (export-origin proxy; not a single mill pin).",
    },
    "jinko_brazil_module_imports_2023": {
        "lat": "-23.96",
        "lon": "-46.33",
        "geo_note": "Santos port complex — principal PV module import gateway cited in Brazil solar logistics press (import-flow proxy pin).",
    },
    # Argus FeNb price is a market series — leave lat/lon empty (not a site)
}


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {b["id"]: i for i, b in enumerate(bib) if isinstance(b, dict) and "id" in b}

    added = []
    updated = []
    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        if rid in by_id:
            rows[by_id[rid]].update({k: v for k, v in row.items() if v != ""})
            updated.append(rid)
        else:
            rows.append({k: row.get(k, "") for k in FIELDS})
            by_id[rid] = len(rows) - 1
            added.append(rid)

        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

        sid = bib_entry["id"]
        if sid in bib_by:
            existing = bib[bib_by[sid]]
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
            if bib_entry.get("supports"):
                existing["supports"] = sorted(
                    set(existing.get("supports") or []) | set(bib_entry["supports"])
                )
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

    for rid, fixes in COORD_FIXES.items():
        if rid in by_id:
            for k, v in fixes.items():
                if v:
                    rows[by_id[rid]][k] = v
            updated.append(f"{rid}[coords]")

    hunt_updates = {
        "hunt_infra_bridges_roads": "Cycle 40: logged caf_salvador_itaparica_150m_2024.",
        "hunt_res_nickel": "Cycle 40: equal budget; MMG/Anglo and PNP already (miss; Araguaia Chinese interest unconfirmed).",
        "hunt_res_lithium": "Cycle 40: equal budget; Mariana plant already; solar CAPEX carved to energy/solar.",
        "hunt_energy_solar": "Cycle 40: logged ganfeng_mariana_solar_190m_2025.",
        "hunt_energy_other_renewables": "Cycle 40: logged byd_brazil_bess_factory_500m_2026.",
        "hunt_res_water": "Cycle 40: logged sacyr_antofagasta_reuse_292m_2025.",
        "hunt_res_balsa": "Cycle 40: equal budget; AIMA 2025 shares / Plantabal already (miss).",
        "hunt_infra_port_cranes": "Cycle 40: equal budget; ZPMC Tecon Santos / Konecranes Acajutla already (miss).",
        "hunt_energy_fission_smr": "Cycle 40: logged inb_westinghouse_fuel_coop_2026.",
        "hunt_fenb_araxa": "Cycle 40: logged codemig_cbmm_renewal_2070_2025.",
        "hunt_infra_building_materials": "Cycle 40: equal budget; Holcim/Votorantim already (miss).",
        "hunt_infra_port_ownership": "Cycle 40: upgraded cosco_chancay_port_2024 with Phase I USD 1.3bn proxy.",
        "hunt_res_graphite": "Cycle 40: logged graphcoa_allied_anode_offtake_2026.",
        "hunt_infra_engineering_epc": "Cycle 40: equal budget; GES/Worley already (miss).",
        "hunt_res_copper": "Cycle 40: equal budget; El Abra / Las Bambas already (miss).",
        "hunt_energy_wind": "Cycle 40: logged nordex_ecuador_112mw_2025 + weg_statkraft_seabra_7mw_2025.",
        "hunt_br_power_equip": "Cycle 40: equal budget; State Grid NE / Hitachi already (miss); filled xdcb coords.",
        "hunt_latam_rail_telecom": "Cycle 40: equal budget; ACA/Tren Macho already (miss).",
    }
    for hid, note in hunt_updates.items():
        if hid in by_id:
            rows[by_id[hid]]["note"] = (
                (rows[by_id[hid]].get("note") or "") + " " + note
            ).strip()

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print("Cycle 40 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 40 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
