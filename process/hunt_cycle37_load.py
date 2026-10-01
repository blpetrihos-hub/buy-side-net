#!/usr/bin/env python3
"""Cycle 37 hunt: shuffle_seed=20261037; equal budget across 18 subcategories."""
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


# seed 20261037 order:
# graphite, nickel, building_materials, copper, niobium, other_renewables, water,
# solar, fission_smr, port_cranes, power_plants_grid, engineering_epc, rail,
# lithium, port_ownership, balsa, bridges_roads, wind

# 1 resources/graphite — Graphcoa Jordânia development spend USD 8m (distinct from DFS CAPEX)
A(
    {
        "id": "graphcoa_jordania_dev_8m_2026",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "Graphcoa (Appian) — Jordânia graphite development spend to date",
        "country": "Brazil",
        "asset": "25 Jul 2026 Cidades & Minerais interview with Graphcoa executive Ricardo Alves: ~USD 8 million already invested in Jordânia (MG) natural-graphite project development toward environmental licensing completion in 2026 and commercial FID targeted 2Q 2027. Distinct from graphcoa_jordania_dfs_capex_2026 (planned full plant CAPEX R$621.76m / USD 120m)",
        "investment_type": "exploration_development",
        "value": "8000000",
        "currency": "USD",
        "value_usd": "8000000",
        "fx_usd": "1",
        "fx_date": "2026-07-25",
        "year": "2026",
        "status": "active",
        "lat": "-15.9",
        "lon": "-40.18",
        "geo_note": "Jordânia, Jequitinhonha Valley, Minas Gerais (company geography).",
        "evidence": "proxy",
        "source_id": "cidades_minerais_graphcoa_8m_20260725",
        "note": "Actor: Graphcoa / Appian Capital (allied). UNVERIFIED proxy: Cidades & Minerais 25 Jul 2026 summarizing executive interview. Development spend only — not full plant CAPEX.",
    },
    {
        "id": "graphcoa_jordania_dev_8m_2026",
        "retrieved": "2026-10-01",
        "source_id": "cidades_minerais_graphcoa_8m_20260725",
        "url": "https://cidadeseminerais.com.br/mineradoras/graphcoa-investimento-grafite-minas/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Até o momento, aproximadamente US$ 8 milhões já foram destinados ao desenvolvimento desse projeto.",
        "note": "Opened Cidades & Minerais Portuguese 25 Jul 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "cidades_minerais_graphcoa_8m_20260725",
        "type": "trade_press",
        "chicago": "Luciano, Raquel. “Graphcoa aposta em investimento de US$ 8 milhões para ampliar projeto de grafite em Minas Gerais.” Cidades & Minerais, 25 July 2026.",
        "url": "https://cidadeseminerais.com.br/mineradoras/graphcoa-investimento-grafite-minas/",
        "annotation": "Press interview citing Graphcoa Jordânia development spend USD 8m. Supports graphcoa_jordania_dev_8m_2026.",
        "supports": ["graphcoa_jordania_dev_8m_2026", "hunt_res_graphite"],
    },
)

# 2 resources/nickel — Canada ECA up to USD 275m potential debt for Piauí Nickel
A(
    {
        "id": "brazilian_nickel_canada_eca_275m_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "Canada export credit agency — potential debt for Brazilian Nickel Piauí",
        "country": "Brazil",
        "asset": "17 Jun 2026 Bloomberg Línea CFO interview: Canadian export-credit agency may provide up to USD 275 million debt financing toward Projeto Piauí Níquel; Ecora Royalties ~USD 62 million loans also cited. Not a closed commitment — potential financing only. Distinct from brazilian_nickel_dfc_loi_2024 and brazilian_nickel_pnp_capex_1p4bn_2026",
        "investment_type": "project_finance",
        "value": "275000000",
        "currency": "USD",
        "value_usd": "275000000",
        "fx_usd": "1",
        "fx_date": "2026-06-17",
        "year": "2026",
        "status": "active",
        "lat": "-5.09",
        "lon": "-42.8",
        "geo_note": "Piauí Nickel Project (approximate pin).",
        "evidence": "proxy",
        "source_id": "bloomberg_linea_brn_canada_eca_20260617",
        "note": "Actor: Canada ECA (allied) potential lender to Brazilian Nickel/TechMet project. UNVERIFIED proxy: Bloomberg Línea CFO interview — may-provide language; not closed loan.",
    },
    {
        "id": "brazilian_nickel_canada_eca_275m_2026",
        "retrieved": "2026-10-01",
        "source_id": "bloomberg_linea_brn_canada_eca_20260617",
        "url": "https://www.bloomberglinea.com.br/negocios/brazilian-nickel-busca-investidor-ancora-para-mina-de-us-14-bilhao-no-piaui/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "A agência de crédito à exportação do Canadá poderá fornecer US$ 275 milhões em financiamento por meio de dívida",
        "note": "Opened Bloomberg Línea Portuguese 17 Jun 2026. Mark UNVERIFIED proxy (potential, not closed).",
    },
    {
        "id": "bloomberg_linea_brn_canada_eca_20260617",
        "type": "trade_press",
        "chicago": "Durão, Mariana, and Annie Lee. “Brazilian Nickel busca investidor-âncora para mina de US$ 1,4 bilhão no Piauí.” Bloomberg Línea, 17 June 2026.",
        "url": "https://www.bloomberglinea.com.br/negocios/brazilian-nickel-busca-investidor-ancora-para-mina-de-us-14-bilhao-no-piaui/",
        "annotation": "CFO cites Canada ECA up to USD 275m debt. Supports brazilian_nickel_canada_eca_275m_2026.",
        "supports": ["brazilian_nickel_canada_eca_275m_2026", "hunt_res_nickel"],
    },
)

# 3 infrastructure/building_materials — Holcim Perú Villa 1 ITS S/13.1m
A(
    {
        "id": "holcim_ves_villa1_its_13m_pen_2026",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Holcim Perú — Planta Villa 1 (Villa El Salvador) modernization ITS",
        "country": "Peru",
        "asset": "27 Mar 2026 Gestión summarizing Holcim Perú Produce ITS: three interventions at Planta Villa 1 totaling S/ 13.1 million — high-efficiency 3rd-gen separator ~S/ 10.8m; automatic bag palletizer ~S/ 2.15m; independent medium-voltage line ~S/ 140,000. Distinguishes from Holcim Pacasmayo/Comacsa acquisitions",
        "investment_type": "brownfield_expansion",
        "value": "13100000",
        "currency": "PEN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-12.21",
        "lon": "-76.94",
        "geo_note": "Villa El Salvador, Lima (Planta Villa 1; press geography).",
        "evidence": "proxy",
        "source_id": "gestion_holcim_ves_20260327",
        "note": "Actor: Holcim Perú (Swiss Holcim) — allied. UNVERIFIED proxy: Gestión 27 Mar 2026 summarizing Produce ITS filing. Small brownfield package vs Pacasmayo control deal.",
    },
    {
        "id": "holcim_ves_villa1_its_13m_pen_2026",
        "retrieved": "2026-10-01",
        "source_id": "gestion_holcim_ves_20260327",
        "url": "https://gestion.pe/economia/empresas/cementera-suiza-holcim-y-los-tres-proyectos-en-planta-de-ves-multinacional-busca-aumentar-su-capacidad-en-peru-noticia/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "El plan contempla tres intervenciones principales y una inversión total de S/ 13.1 millones, siendo el componente más relevante el incremento de la capacidad de molienda",
        "note": "Opened Gestión Spanish 27 Mar 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "gestion_holcim_ves_20260327",
        "type": "trade_press",
        "chicago": "Gestión. “Cementera suiza Holcim y los tres proyectos en planta de VES: multinacional busca aumentar su capacidad en Perú.” 27 March 2026.",
        "url": "https://gestion.pe/economia/empresas/cementera-suiza-holcim-y-los-tres-proyectos-en-planta-de-ves-multinacional-busca-aumentar-su-capacidad-en-peru-noticia/",
        "annotation": "Press on Holcim Villa 1 ITS S/13.1m. Supports holcim_ves_villa1_its_13m_pen_2026.",
        "supports": ["holcim_ves_villa1_its_13m_pen_2026", "hunt_infra_building_materials"],
    },
)

# 4 resources/copper — miss
# 5 resources/niobium — miss

# 6 energy/other_renewables — Jinko Aloe BESS USD 340m + AES Pampas PF USD 550m
A(
    {
        "id": "jinko_aloe_bess_340m_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "Jinko Power — BESS Aloe (Atacama)",
        "country": "Chile",
        "asset": "23 Jun 2026 BNamericas: Jinko Power carta de pertinencia to SEA for independent storage project Aloe — 267 MW / 1,602 MWh in Atacama Region, cost USD 340 million. Distinct from jinko_bess_amanecer_500m_2025 (Amanecer DIA USD 500m)",
        "investment_type": "greenfield_storage",
        "value": "340000000",
        "currency": "USD",
        "value_usd": "340000000",
        "fx_usd": "1",
        "fx_date": "2026-06-23",
        "year": "2026",
        "status": "active",
        "lat": "-27.37",
        "lon": "-70.33",
        "geo_note": "Atacama Region, Chile (BNamericas geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "bnamericas_jinko_aloe_20260623",
        "note": "Actor: Jinko Power (PRC) — prc. UNVERIFIED proxy: BNamericas 23 Jun 2026 summarizing SEA pertinencia. Pre-construction permitting.",
    },
    {
        "id": "jinko_aloe_bess_340m_2026",
        "retrieved": "2026-10-01",
        "source_id": "bnamericas_jinko_aloe_20260623",
        "url": "https://www.bnamericas.com/es/noticias/jinko-y-aple-buscan-definiciones-regulatorias-para-proyectos-de-almacenamiento-por-us640mn-en-chile",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Bautizado Aloe y con un costo de US$340 millones, el proyecto de Jinko contempla la instalación de un sistema de 267MW/1,602MWh en la región de Atacama.",
        "note": "Opened BNamericas Spanish 23 Jun 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "bnamericas_jinko_aloe_20260623",
        "type": "trade_press",
        "chicago": "BNamericas. “Jinko y Aple buscan definiciones regulatorias para proyectos de almacenamiento por US$640 millones en Chile.” 23 June 2026.",
        "url": "https://www.bnamericas.com/es/noticias/jinko-y-aple-buscan-definiciones-regulatorias-para-proyectos-de-almacenamiento-por-us640mn-en-chile",
        "annotation": "Trade press on Jinko Aloe BESS USD 340m. Supports jinko_aloe_bess_340m_2026.",
        "supports": ["jinko_aloe_bess_340m_2026", "hunt_energy_other_renewables"],
    },
)

A(
    {
        "id": "aes_pampas_pf_550m_2025",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "AES Andes / Energía Eólica Pampas SpA — Pampas hybrid project finance",
        "country": "Chile",
        "asset": "Nov 2025: AES Chile/Andes closes non-recourse project finance USD 550 million for Parque Híbrido Pampas (Taltal, Antofagasta) — 229 MW solar + 128 MW wind + 340 MW BESS; total project investment ~USD 800 million; COD targeted 2027. Distinct from aes_andes_pampas_cristales_2025 (combined >USD 1.1bn Pampas+Cristales CAPEX package)",
        "investment_type": "project_finance",
        "value": "550000000",
        "currency": "USD",
        "value_usd": "550000000",
        "fx_usd": "1",
        "fx_date": "2025-11-05",
        "year": "2025",
        "status": "active",
        "lat": "-25.4",
        "lon": "-70.48",
        "geo_note": "Taltal, Antofagasta Region (company geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "pv_mag_aes_pampas_pf_20251106",
        "note": "Actor: AES Andes / AES Corporation (U.S.) — us. UNVERIFIED proxy: pv magazine LatAm 6 Nov 2025 summarizing company financing close. Debt tranche for Pampas only.",
    },
    {
        "id": "aes_pampas_pf_550m_2025",
        "retrieved": "2026-10-01",
        "source_id": "pv_mag_aes_pampas_pf_20251106",
        "url": "https://www.pv-magazine-latam.com/2025/11/06/aes-chile-concreta-financiamiento-por-550-millones-de-dolares-para-su-proyecto-parque-hibrido-pampas/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "AES Chile anunció el cierre de un financiamiento por 550 millones de dólares para el desarrollo del Parque Híbrido Pampas, ubicado en la comuna de Taltal, región de Antofagasta.",
        "note": "Opened pv magazine LatAm Spanish 6 Nov 2025. Mark UNVERIFIED proxy.",
    },
    {
        "id": "pv_mag_aes_pampas_pf_20251106",
        "type": "trade_press",
        "chicago": "Ini, Luis. “AES Chile concreta financiamiento por 550 millones de dólares para su proyecto Parque Híbrido Pampas.” pv magazine Latinoamérica, 6 November 2025.",
        "url": "https://www.pv-magazine-latam.com/2025/11/06/aes-chile-concreta-financiamiento-por-550-millones-de-dolares-para-su-proyecto-parque-hibrido-pampas/",
        "annotation": "Trade press on AES Pampas project finance USD 550m. Supports aes_pampas_pf_550m_2025.",
        "supports": ["aes_pampas_pf_550m_2025", "hunt_energy_other_renewables"],
    },
)

# 7–9 water, solar, fission_smr — miss

# 10 infrastructure/port_cranes — ZPMC STS delivery TCP Montevideo (first of five)
A(
    {
        "id": "zpmc_tcp_montevideo_sts_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — STS delivery to Katoen Natie TCP Montevideo",
        "country": "Uruguay",
        "asset": "21 Sep 2026 WorldCargo News: Terminal Cuenca del Plata (Katoen Natie) takes delivery of new Super Post Panamax STS from ZPMC — ninth STS at terminal; first of five ordered; 85 m height, 62 m outreach, 65 t twin-lift / 75 t hook; Siemens drives; service targeted Oct 2026 after testing; remaining four cranes next year. Unit price not disclosed on opened page",
        "investment_type": "equipment_delivery",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-34.9",
        "lon": "-56.21",
        "geo_note": "Port of Montevideo TCP (terminal geography).",
        "evidence": "documented",
        "source_id": "worldcargo_tcp_zpmc_sts_20260921",
        "note": "Actor: ZPMC (PRC) supplier to Katoen Natie TCP — prc on equipment side. WorldCargo News 21 Sep 2026. Related ownership expansion logged separately as katoen_tcp_montevideo_455m_2021.",
    },
    {
        "id": "zpmc_tcp_montevideo_sts_2026",
        "retrieved": "2026-10-01",
        "source_id": "worldcargo_tcp_zpmc_sts_20260921",
        "url": "https://www.worldcargonews.com/cargo-handling-equipment/2026/09/katoen-naties-montevideo-terminal-bolsters-sts-crane-fleet/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Terminal Cuenca del Plata (TCP), the Katoen Natie-operated container terminal at Uruguay’s Port of Montevideo, has taken delivery of a new STS crane from ZPMC as part of a wider expansion of its cargo-handling infrastructure.",
        "note": "Opened WorldCargo News 21 Sep 2026.",
    },
    {
        "id": "worldcargo_tcp_zpmc_sts_20260921",
        "type": "trade_press",
        "chicago": "WorldCargo News. “Katoen Natie’s Montevideo terminal bolsters STS crane fleet.” 21 September 2026.",
        "url": "https://www.worldcargonews.com/cargo-handling-equipment/2026/09/katoen-naties-montevideo-terminal-bolsters-sts-crane-fleet/",
        "annotation": "Trade press on ZPMC STS delivery to TCP Montevideo. Supports zpmc_tcp_montevideo_sts_2026.",
        "supports": ["zpmc_tcp_montevideo_sts_2026", "hunt_infra_port_cranes"],
    },
)

# 11 energy/power_plants_grid — miss

# 12 infrastructure/engineering_epc — GES Pampas EPC (Spanish)
A(
    {
        "id": "ges_pampas_epc_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "GES (Global Energy Services) — EPC for AES Pampas hybrid",
        "country": "Chile",
        "asset": "Sep 2025: Spanish GES awarded engineering, construction and commissioning contract for AES Andes Parque Híbrido Pampas (>695 MW: 128 MW wind + 229 MW solar + 340 MW BESS) in Antofagasta; company calls it largest project in GES history and 400th project executed. Contract USD value not disclosed on opened company/press pages",
        "investment_type": "epc_contract",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-25.4",
        "lon": "-70.48",
        "geo_note": "Taltal / Antofagasta Pampas site (AES geography).",
        "evidence": "documented",
        "source_id": "ges_pampas_company_202509",
        "note": "Actor: GES Spain — allied. Company English release. EPC actor row distinct from aes_andes_pampas_cristales_2025 (owner CAPEX) and aes_pampas_pf_550m_2025 (debt).",
    },
    {
        "id": "ges_pampas_epc_2025",
        "retrieved": "2026-10-01",
        "source_id": "ges_pampas_company_202509",
        "url": "https://services-ges.com/en/ges-consolidates-its-international-presence-with-a-new-hybrid-project-in-chile/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "GES will be responsible for the engineering, construction and commissioning of the project, confirming its position as a strategic partner in the implementation of comprehensive, large-scale solutions.",
        "note": "Opened GES company English page on Pampas award.",
    },
    {
        "id": "ges_pampas_company_202509",
        "type": "company",
        "chicago": "GES Global Energy Services. “GES Consolidates Its International Presence with a Hybrid Project in Chile.” Company news, September 2025.",
        "url": "https://services-ges.com/en/ges-consolidates-its-international-presence-with-a-new-hybrid-project-in-chile/",
        "annotation": "Company release on GES EPC for Pampas hybrid. Supports ges_pampas_epc_2025.",
        "supports": ["ges_pampas_epc_2025", "hunt_infra_engineering_epc"],
    },
)

# 13–14 rail, lithium — miss

# 15 infrastructure/port_ownership — Katoen Natie TCP Montevideo USD 455m program
A(
    {
        "id": "katoen_tcp_montevideo_455m_2021",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "Katoen Natie — TCP Montevideo concession expansion",
        "country": "Uruguay",
        "asset": "WorldCargo News 21 Sep 2026 recounting: 2021 Katoen Natie announced USD 455 million investment under concession extension with Uruguay — 700 m second quay, 22 ha yard, additional STS cranes and horizontal equipment, upgraded truck access, IT/control; capacity from 800k to 2.3m TEU/y; Katoen Natie 80% / ANP 20%. Ongoing expansion evidenced by 2026 ZPMC STS deliveries",
        "investment_type": "concession_expansion",
        "value": "455000000",
        "currency": "USD",
        "value_usd": "455000000",
        "fx_usd": "1",
        "fx_date": "2021-01-01",
        "year": "2021",
        "status": "active",
        "lat": "-34.9",
        "lon": "-56.21",
        "geo_note": "Port of Montevideo TCP.",
        "evidence": "proxy",
        "source_id": "worldcargo_tcp_zpmc_sts_20260921",
        "note": "Actor: Katoen Natie (Belgium) — allied. UNVERIFIED proxy: WorldCargo 2026 article restating 2021 USD 455m program (secondary recount). Distinct from Hutchison ICAVE / APM Callao ownership rows.",
    },
    {
        "id": "katoen_tcp_montevideo_455m_2021",
        "retrieved": "2026-10-01",
        "source_id": "worldcargo_tcp_zpmc_sts_20260921",
        "url": "https://www.worldcargonews.com/cargo-handling-equipment/2026/09/katoen-naties-montevideo-terminal-bolsters-sts-crane-fleet/",
        "price_year": "2021",
        "evidence": "proxy",
        "quote": "In 2021, Katoen Natie announced a US$455 million investment under its concession agreement extension with the Uruguayan government.",
        "note": "Opened WorldCargo News 21 Sep 2026 recounting 2021 program. Mark UNVERIFIED proxy for historical CAPEX figure.",
    },
    {
        "id": "worldcargo_tcp_montevideo_455m",
        "type": "trade_press",
        "chicago": "WorldCargo News. “Katoen Natie’s Montevideo terminal bolsters STS crane fleet.” 21 September 2026.",
        "url": "https://www.worldcargonews.com/cargo-handling-equipment/2026/09/katoen-naties-montevideo-terminal-bolsters-sts-crane-fleet/",
        "annotation": "Trade press restating Katoen Natie TCP USD 455m expansion. Supports katoen_tcp_montevideo_455m_2021.",
        "supports": ["katoen_tcp_montevideo_455m_2021", "hunt_infra_port_ownership"],
    },
)

# 16 resources/balsa — miss

# 17 infrastructure/bridges_roads — Contreras Vicuña Corredor Norte USD 135m
A(
    {
        "id": "contreras_vicuna_corredor_norte_135m_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "other",
        "counterpart": "Contreras Hermanos / BBC / Construmin — Vicuña Josemaría Corredor Norte access",
        "country": "Argentina",
        "asset": "Sep 2026: Vicuña Argentina awards Corredor Norte de Acceso (Secciones A1–A2) to consortium Contreras Hermanos + Boetto y Buttigliengo + Construmin — 63.6 km in Iglesia, San Juan; contract USD 135,012,246.91; 27-month execution; heavy-haul mine access with bridges/drainage/structures toward Josemaría Phase 1",
        "investment_type": "road_epc",
        "value": "135012246.91",
        "currency": "USD",
        "value_usd": "135012246.91",
        "fx_usd": "1",
        "fx_date": "2026-09-18",
        "year": "2026",
        "status": "active",
        "lat": "-30.25",
        "lon": "-69.15",
        "geo_note": "Departamento Iglesia, San Juan (press geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "lenergy_contreras_vicuna_20260918",
        "note": "Actor: Argentine contractor consortium (Contreras/BBC/Construmin) — other. UNVERIFIED proxy: Latin Energy Group / ecojournal 18 Sep 2026. Distinct from vicuna_rigi_peelp_2026 (mine CAPEX).",
    },
    {
        "id": "contreras_vicuna_corredor_norte_135m_2026",
        "retrieved": "2026-10-01",
        "source_id": "lenergy_contreras_vicuna_20260918",
        "url": "https://www.lenergygroup.com/contreras-hermanos-se-adjudico-el-contrato-de-us-135-millones-para-construir-accesos-viales-al-proyecto-de-cobre-de-vicuna/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "El contrato prevé una inversión global de US$ 135.012.246,91 y contempla un plazo de ejecución de 27 meses.",
        "note": "Opened Latin Energy Group Spanish 18 Sep 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "lenergy_contreras_vicuna_20260918",
        "type": "trade_press",
        "chicago": "Latin Energy Group. “Contreras hermanos se adjudicó el contrato de US$ 135 millones para construir accesos viales al proyecto de cobre de Vicuña.” 18 September 2026.",
        "url": "https://www.lenergygroup.com/contreras-hermanos-se-adjudico-el-contrato-de-us-135-millones-para-construir-accesos-viales-al-proyecto-de-cobre-de-vicuna/",
        "annotation": "Press on Vicuña Corredor Norte road contract USD 135m. Supports contreras_vicuna_corredor_norte_135m_2026.",
        "supports": ["contreras_vicuna_corredor_norte_135m_2026", "hunt_infra_bridges_roads"],
    },
)

# 18 energy/wind — miss


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

    hunt_updates = {
        "hunt_res_graphite": "Cycle 37: logged graphcoa_jordania_dev_8m_2026 (USD 8m development).",
        "hunt_res_nickel": "Cycle 37: logged brazilian_nickel_canada_eca_275m_2026 (Canada ECA up to USD 275m).",
        "hunt_infra_building_materials": "Cycle 37: logged holcim_ves_villa1_its_13m_pen_2026.",
        "hunt_res_copper": "Cycle 37: equal budget; Las Bambas / El Abra / Vicuña RIGI already (miss).",
        "hunt_fenb_araxa": "Cycle 37: equal budget; St George A$60m / CBMM spend already (miss).",
        "hunt_energy_other_renewables": "Cycle 37: logged jinko_aloe_bess_340m_2026 + aes_pampas_pf_550m_2025.",
        "hunt_res_water": "Cycle 37: equal budget; Cox Rosarito / Sacyr Coquimbo already (miss).",
        "hunt_energy_solar": "Cycle 37: equal budget; PowerChina Mauriti / Trina already (miss).",
        "hunt_energy_fission_smr": "Cycle 37: equal budget; Meitner / Nuclearis already (miss).",
        "hunt_infra_port_cranes": "Cycle 37: logged zpmc_tcp_montevideo_sts_2026.",
        "hunt_br_power_equip": "Cycle 37: equal budget; Hitachi / Coca Codo already (miss).",
        "hunt_infra_engineering_epc": "Cycle 37: logged ges_pampas_epc_2025.",
        "hunt_latam_rail_telecom": "Cycle 37: equal budget; PowerChina Chancay rail already (miss).",
        "hunt_res_lithium": "Cycle 37: equal budget; Galan / Zijin / Posco RIGI already (miss).",
        "hunt_infra_port_ownership": "Cycle 37: logged katoen_tcp_montevideo_455m_2021.",
        "hunt_res_balsa": "Cycle 37: equal budget; AIMA Spain/China/US already (miss).",
        "hunt_infra_bridges_roads": "Cycle 37: logged contreras_vicuna_corredor_norte_135m_2026.",
        "hunt_energy_wind": "Cycle 37: equal budget; Goldwind FINAME / Vestas already (miss).",
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
    print("Cycle 37 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 37 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
