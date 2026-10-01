#!/usr/bin/env python3
"""Cycle 6 hunt: shuffle_seed=20261006; equal budget across 18 subcategories."""
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


# seed 20261006 order:
# power_plants_grid, fission_smr, other_renewables, engineering_epc, port_cranes,
# niobium, lithium, port_ownership, graphite, balsa, water, bridges_roads, copper,
# building_materials, solar, nickel, rail, wind

# 1 energy/power_plants_grid — Siemens Energy AXIA (ex-Chesf) 40-substation retrofit
A(
    {
        "id": "siemens_axia_chesf_retrofit_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "Siemens Energy — AXIA Energia (ex-Eletrobras Chesf) northeast Brazil substation retrofit",
        "country": "Brazil",
        "asset": "Replacement of 240 circuit breakers and 731 disconnectors across 40 AXIA Energia substations (largest LatAm equipment upgrade cited by Siemens Energy)",
        "investment_type": "epc_equipment",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-8.05",
        "lon": "-34.88",
        "geo_note": "Northeast Brazil Chesf/AXIA transmission footprint (Recife reference; multi-state).",
        "evidence": "documented",
        "source_id": "siemens_axia_20251027",
        "note": "Actor: Siemens Energy (German) — allied. Company reference case 27 Oct 2025: >1,000 components across 40 substations; goal of replacing >1,000 pieces by 2025. Distinct from prior Siemens Furnas/Eletrobras GIS packages.",
    },
    {
        "id": "siemens_axia_chesf_retrofit_2025",
        "retrieved": "2026-10-01",
        "source_id": "siemens_axia_20251027",
        "url": "https://www.siemens-energy.com/global/en/home/references/axia-energia-brazil-power-grid-modernization.html",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "This project covered 40 substations operated by AXIA Energia. Siemens Energy replaced 240 circuit breakers and 731 disconnectors. The goal of this grid modernization was to maintain quality and reliability during the largest equipment upgrade in Latin America.",
        "note": "Opened Siemens Energy AXIA Energia Brazil reference page.",
    },
    {
        "id": "siemens_axia_20251027",
        "type": "official",
        "chicago": "Siemens Energy. “AXIA Energia, Brazil: Modernizing Brazil’s Power Grid – A milestone in efficiency and reliability.” 27 October 2025.",
        "url": "https://www.siemens-energy.com/global/en/home/references/axia-energia-brazil-power-grid-modernization.html",
        "annotation": "Company primary AXIA/Chesf substation retrofit case. Supports siemens_axia_chesf_retrofit_2025.",
        "supports": ["siemens_axia_chesf_retrofit_2025", "hunt_br_power_equip"],
    },
)

# 2 energy/fission_smr — INVAP–CNEA MoU on CAREM SMR export commercialization (press)
A(
    {
        "id": "invap_cnea_carem_mou_2024",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "other",
        "counterpart": "INVAP / CNEA — MoU to commercialize/export CAREM SMR and associated nuclear services",
        "country": "Argentina",
        "asset": "March 2024 memorandum of understanding for joint exploration of CAREM export opportunities, components, engineering and related nuclear-electric services; prototype ~65% complete / 32 MWe at Atucha",
        "investment_type": "technology_mou",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-33.97",
        "lon": "-59.21",
        "geo_note": "CAREM prototype site adjacent to Complejo Atucha, Lima, Buenos Aires (EconoJournal).",
        "evidence": "proxy",
        "source_id": "econojournal_invap_cnea_20240313",
        "note": "Actors: INVAP (Argentine state tech) and CNEA — other. UNVERIFIED proxy: EconoJournal 13 Mar 2024 reporting MoU signing (Serquis/Giussi) and Pedre quotes on export scope beyond whole-reactor sales. Complements carem25_argentina_iaea_2025 and meitner_acr300_atucha_2026.",
    },
    {
        "id": "invap_cnea_carem_mou_2024",
        "retrieved": "2026-10-01",
        "source_id": "econojournal_invap_cnea_20240313",
        "url": "https://econojournal.com.ar/energia/invap-cnea-carem-exportar/",
        "price_year": "2024",
        "evidence": "proxy",
        "quote": "INVAP y la Comisión Nacional de Energía Atómica (CNEA) trabajarán de forma conjunta para exportar el reactor CAREM y componentes y servicios vinculados con el segmento de los reactores modulares pequeños (SMR). … El acto de firma se llevó a cabo el martes con la presencia de la presidenta de la CNEA, Adriana Serquis y el nuevo Gerente General y CEO de INVAP, Darío Giussi.",
        "note": "Opened EconoJournal Spanish press report of INVAP–CNEA MoU.",
    },
    {
        "id": "econojournal_invap_cnea_20240313",
        "type": "press",
        "chicago": "Deza, Nicolás. “INVAP trabajará con la CNEA para impulsar exportaciones nucleares vinculadas al reactor CAREM.” EconoJournal, 13 March 2024.",
        "url": "https://econojournal.com.ar/energia/invap-cnea-carem-exportar/",
        "annotation": "Spanish trade press on INVAP–CNEA CAREM export MoU. UNVERIFIED proxy for invap_cnea_carem_mou_2024.",
        "supports": ["invap_cnea_carem_mou_2024", "hunt_energy_fission_smr"],
    },
)

# 3 energy/other_renewables — World Bank / LaGeo Chinameca geothermal (El Salvador)
A(
    {
        "id": "lageo_chinameca_wb_2025",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "other",
        "counterpart": "LaGeo / CEL — Chinameca geothermal plant (World Bank IBRD financing)",
        "country": "El Salvador",
        "asset": "US$150 million IBRD six-year project financing construction of ~25 MW geothermal plant at Chinameca field; exploratory work to support up to ~40 MW",
        "investment_type": "project_finance",
        "value": "150000000",
        "currency": "USD",
        "value_usd": "150000000",
        "fx_usd": "1",
        "fx_date": "2025-03-28",
        "year": "2025",
        "status": "active",
        "lat": "13.48",
        "lon": "-88.32",
        "geo_note": "Chinameca Geothermal Field ~115 km east of San Salvador (World Bank).",
        "evidence": "documented",
        "source_id": "worldbank_elsalvador_geo_20250328",
        "note": "Actors: LaGeo (Salvadoran state geothermal) with CEL borrower; IBRD lender — other (not PRC/US corporate OEM). World Bank Board approval 28 Mar 2025. Distinct from Ormat Guatemala rows.",
    },
    {
        "id": "lageo_chinameca_wb_2025",
        "retrieved": "2026-10-01",
        "source_id": "worldbank_elsalvador_geo_20250328",
        "url": "https://www.worldbank.org/en/news/press-release/2025/03/26/banco-mundial-el-salvador-impulsan-energia-geotermica-desarrollo-sostenible-inclusivo",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "LaGeo, a State-owned company responsible for generating electricity using El Salvador’s geothermal resources, is the implementing agency, and will move forward with the construction of a 25 MW geothermal power plant in the Chinameca Geothermal Field … The US$150 million, six-year “El Salvador Geothermal Energy for Sustainable and Inclusive Development Project”",
        "note": "Opened World Bank press release (English).",
    },
    {
        "id": "worldbank_elsalvador_geo_20250328",
        "type": "official",
        "chicago": "World Bank. “World Bank and El Salvador Promote Geothermal Energy for Sustainable and Inclusive Development.” 28 March 2025.",
        "url": "https://www.worldbank.org/en/news/press-release/2025/03/26/banco-mundial-el-salvador-impulsan-energia-geotermica-desarrollo-sostenible-inclusivo",
        "annotation": "IBRD Board approval notice for Chinameca geothermal. Supports lageo_chinameca_wb_2025.",
        "supports": ["lageo_chinameca_wb_2025", "hunt_energy_other_renewables"],
    },
)

# 4 infrastructure/engineering_epc — Techint E&C SADDN desal + pipeline EPC (Chile)
A(
    {
        "id": "techint_saddn_epc_chile",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "Techint Engineering & Construction — SADDN desalination + pumping EPC for Aguas Horizonte / Codelco Northern District",
        "country": "Chile",
        "asset": "EPC of reverse-osmosis desalination plant (~840 l/s) plus ~160 km 48-inch pumping/transmission system to Codelco Northern District mines; expected completion 2026",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-22.0887",
        "lon": "-70.1961",
        "geo_note": "Tocopilla province coordinates published on Techint SADDN project page.",
        "evidence": "documented",
        "source_id": "techint_saddn_project",
        "note": "Actor: Techint E&C (Techint Group, Italian-Argentine) — allied. Company project page: EPC scope for BOOT Aguas Horizonte; complements ide_saddn_desal_chile_2023 technology subcontract row (non-duplicate overall EPC).",
    },
    {
        "id": "techint_saddn_epc_chile",
        "retrieved": "2026-10-01",
        "source_id": "techint_saddn_project",
        "url": "https://www.techint.com/en/our-projects/saddn",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "We are constructing a desalination plant and a water collection and pumping system for Aguas Horizonte, which will supply desalinated water to three large mining operations in northern Chile. … Scope of work: EPC … 840 liters/second current maximum desalination capacity … +160 kilometers of 48\" pipe … Expected completion: 2026",
        "note": "Opened Techint E&C SADDN project page.",
    },
    {
        "id": "techint_saddn_project",
        "type": "official",
        "chicago": "Techint Engineering & Construction. “SADDN.” Company project page (accessed 1 October 2026).",
        "url": "https://www.techint.com/en/our-projects/saddn",
        "annotation": "Company primary SADDN EPC scope page. Supports techint_saddn_epc_chile.",
        "supports": ["techint_saddn_epc_chile", "hunt_infra_engineering_epc"],
    },
)

# 5 infrastructure/port_cranes — ZPMC STS for Portonave (Navegantes)
A(
    {
        "id": "zpmc_portonave_sts_2025",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — two STS quay cranes for Portonave (TiL), Navegantes",
        "country": "Brazil",
        "asset": "Two electric Ship-to-Shore cranes from ZPMC (up to 100 t / 55 m lift / 25-row boom); part of ~USD 87.8m electric equipment package with operations targeted 2026",
        "investment_type": "equipment_supply",
        "value": "87800000",
        "currency": "USD",
        "value_usd": "87800000",
        "fx_usd": "1",
        "fx_date": "2025-01-10",
        "year": "2025",
        "status": "active",
        "lat": "-26.89",
        "lon": "-48.65",
        "geo_note": "Portonave terminal, Navegantes, Santa Catarina (company release).",
        "evidence": "documented",
        "source_id": "portonave_electric_equip_20250110",
        "note": "Actor: ZPMC (PRC) STS OEM; buyer Portonave (TiL/MSC Swiss) — crane side coded prc. Company 10 Jan 2025 English release names ZPMC for STS; Konecranes for RTGs (RTG OEM not coded as this row). Distinct from Santos Brasil / Itapoá / Lázaro ZPMC rows.",
    },
    {
        "id": "zpmc_portonave_sts_2025",
        "retrieved": "2026-10-01",
        "source_id": "portonave_electric_equip_20250110",
        "url": "https://www.portonave.com.br/en/todas-as-noticias/portonave-invests-usd87-8-million-in-100-electric-equipment",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Acquired from the Chinese manufacturer Shanghai Zhenhua Heavy Industries (ZPMC), the cranes can handle loads of up to 100 tons at a height of 55 meters … boom reach of up to 25 rows of containers. These new STSs will be the first of their kind in Brazil.",
        "note": "Opened Portonave English company news page.",
    },
    {
        "id": "portonave_electric_equip_20250110",
        "type": "official",
        "chicago": "Portonave. “Portonave invests $87.8 million in 100% electric equipment.” 10 January 2025.",
        "url": "https://www.portonave.com.br/en/todas-as-noticias/portonave-invests-usd87-8-million-in-100-electric-equipment",
        "annotation": "Terminal primary announcement naming ZPMC STS OEM. Supports zpmc_portonave_sts_2025.",
        "supports": ["zpmc_portonave_sts_2025", "hunt_infra_port_cranes"],
    },
)

# 6 resources/niobium — miss (no distinct new FeNb ownership/price beyond CBMM/CMOC)

# 7 resources/lithium — Ganfeng Mariana production start (press)
A(
    {
        "id": "ganfeng_mariana_production_2025",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "Ganfeng Lithium — Mariana lithium chloride plant, Salta",
        "country": "Argentina",
        "asset": "Reported start of production at Mariana (~USD 790m; 20,000 t/y lithium chloride from Llullaillaco brine) plus ~USD 190m supporting solar park",
        "investment_type": "ownership_equity",
        "value": "790000000",
        "currency": "USD",
        "value_usd": "790000000",
        "fx_usd": "1",
        "fx_date": "2025-02-12",
        "year": "2025",
        "status": "active",
        "lat": "-24.72",
        "lon": "-68.55",
        "geo_note": "Salar de Llullaillaco / Mariana plant, Salta (Reuters citing company).",
        "evidence": "proxy",
        "source_id": "reuters_ganfeng_mariana_20250212",
        "note": "Actor: Ganfeng Lithium (PRC) — prc. UNVERIFIED proxy: Reuters 12 Feb 2025 citing company inauguration figures (USD 790m plant; 20 kt/y LiCl; USD 190m solar). Distinct from Ganfeng Pastos Grandes / Lithea rows.",
    },
    {
        "id": "ganfeng_mariana_production_2025",
        "retrieved": "2026-10-01",
        "source_id": "reuters_ganfeng_mariana_20250212",
        "url": "https://www.reuters.com/markets/commodities/chinas-ganfeng-starts-lithium-production-argentinas-mariana-project-2025-02-12/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "The Mariana plant, in the province of Salta, represents a $790 million investment and has the capacity to produce 20,000 metric tons of lithium chloride per year from extraction at the Llullaillaco salt flat. Ganfeng also spent $190 million to build a solar park to support the plant's energy needs.",
        "note": "Opened Reuters article (non-paywalled text retrieved).",
    },
    {
        "id": "reuters_ganfeng_mariana_20250212",
        "type": "press",
        "chicago": "Raszewski, Eliana, and Daina Beth Solomon. “China’s Ganfeng starts lithium production at Argentina’s Mariana project.” Reuters, 12 February 2025.",
        "url": "https://www.reuters.com/markets/commodities/chinas-ganfeng-starts-lithium-production-argentinas-mariana-project-2025-02-12/",
        "annotation": "Wire press citing Ganfeng Mariana start. UNVERIFIED proxy for ganfeng_mariana_production_2025.",
        "supports": ["ganfeng_mariana_production_2025", "hunt_res_lithium"],
    },
)

# 8 infrastructure/port_ownership — ICTSI Rio Brasil Terminal expansion
A(
    {
        "id": "ictsi_rio_brasil_expansion_2025",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "other",
        "counterpart": "ICTSI — Rio Brasil Terminal expansion/modernization, Port of Rio de Janeiro",
        "country": "Brazil",
        "asset": "R$948 million 2025–2029 expansion raising capacity from ~440k to ~750k TEU/year (~R$414m infrastructure + ~R$534m equipment)",
        "investment_type": "concession_capex",
        "value": "948000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-22.89",
        "lon": "-43.18",
        "geo_note": "ICTSI Rio Brasil Terminal, Port of Rio de Janeiro (company release).",
        "evidence": "documented",
        "source_id": "ictsi_rio_brasil_20251215",
        "note": "Actor: ICTSI (Philippine independent operator) — other. Company 15 Dec 2025 release; value stored as BRL (no FX). Distinct from APM BTP Santos / DP World Callao / Hutchison Ensenada ownership rows.",
    },
    {
        "id": "ictsi_rio_brasil_expansion_2025",
        "retrieved": "2026-10-01",
        "source_id": "ictsi_rio_brasil_20251215",
        "url": "https://ictsi.com/press-releases/ictsi-invest-r948-million-expand-modernize-rio-brasil-terminal",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The total investment of R$948 million comprises approximately R$414.4 million in infrastructure works and R$533.5 million in the acquisition of state-of-the-art equipment. … increase the public terminal's operational capacity by 70.5%, from the current 440 thousand TEUs per year to 750 thousand TEUs per year",
        "note": "Opened ICTSI press release.",
    },
    {
        "id": "ictsi_rio_brasil_20251215",
        "type": "official",
        "chicago": "International Container Terminal Services, Inc. “ICTSI to invest R$948 million to expand, modernize Rio Brasil Terminal.” 15 December 2025.",
        "url": "https://ictsi.com/press-releases/ictsi-invest-r948-million-expand-modernize-rio-brasil-terminal",
        "annotation": "Operator primary Rio Brasil expansion announcement. Supports ictsi_rio_brasil_expansion_2025.",
        "supports": ["ictsi_rio_brasil_expansion_2025", "hunt_infra_port_ownership"],
    },
)

# 9 resources/graphite — miss (no distinct mine/anode actor beyond South Star/Nacional/Graphex/Graphcoa)

# 10 resources/balsa — miss (no new WITS year beyond 2022–2024)

# 11 resources/water — GS Inima Atacama desal (Chile)
A(
    {
        "id": "gs_inima_atacama_desal_chile",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "GS Inima — Atacama desalination plant (ECONSSA), Caldera",
        "country": "Chile",
        "asset": "38,880 m³/day seawater RO desalination plant (design/build/operate/maintain) serving Atacama Region potable supply; ~2.8 kWh/m³ cited energy intensity",
        "investment_type": "epc_om",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-27.07",
        "lon": "-70.82",
        "geo_note": "Caldera / Atacama Region (GS Inima project page).",
        "evidence": "documented",
        "source_id": "gs_inima_atacama_project",
        "note": "Actor: GS Inima (Spanish ACS water) — allied. Company project page: EPC+O&M for ECONSSA client. Distinct from IDE SADDN/Aconcagua and Acciona Collahuasi/Los Cabos desal rows.",
    },
    {
        "id": "gs_inima_atacama_desal_chile",
        "retrieved": "2026-10-01",
        "source_id": "gs_inima_atacama_project",
        "url": "https://inima.com/en/project/atacama/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "The Atacama desalination plant benefits more than 210 people in 4 communes of Chile. … Capacity 38.880 m³/day … Contract Type: Engineering, Supply, Construction, Operation and Maintenance … Client: ECONSSA … Location: Atacama, Chile",
        "note": "Opened GS Inima Atacama project page.",
    },
    {
        "id": "gs_inima_atacama_project",
        "type": "official",
        "chicago": "GS Inima. “Atacama Desalination Plant.” Company project page (accessed 1 October 2026).",
        "url": "https://inima.com/en/project/atacama/",
        "annotation": "Company primary Atacama desal EPC+O&M page. Supports gs_inima_atacama_desal_chile.",
        "supports": ["gs_inima_atacama_desal_chile", "hunt_res_water"],
    },
)

# 12 infrastructure/bridges_roads — CHEC Montego Bay Perimeter Road
A(
    {
        "id": "chec_montego_bay_perimeter_jamaica",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "China Harbour Engineering Company (CHEC) — Montego Bay Perimeter Road Project",
        "country": "Jamaica",
        "asset": "US$274 million Design-Build contract for Montego Bay Bypass (~15 km), Long Hill Bypass (~10.5 km), and Barnett Street/West Green Avenue dualization (NROCC executing agency)",
        "investment_type": "epc_design_build",
        "value": "274000000",
        "currency": "USD",
        "value_usd": "274000000",
        "fx_usd": "1",
        "fx_date": "2024-10-18",
        "year": "2024",
        "status": "active",
        "lat": "18.47",
        "lon": "-77.92",
        "geo_note": "Montego Bay, St. James (NROCC project page).",
        "evidence": "documented",
        "source_id": "nrocc_montego_bay_perimeter",
        "note": "Actor: CHEC (PRC) — prc. NROCC official project page states US$274M Design-Build with CHEC. Distinct from chec_jamaica_spark_roads_2024 and chec_jamaica_schip_bri.",
    },
    {
        "id": "chec_montego_bay_perimeter_jamaica",
        "retrieved": "2026-10-01",
        "source_id": "nrocc_montego_bay_perimeter",
        "url": "https://www.h2kjamaica.com.jm/montego-bay-project",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "The Government of Jamaica (GOJ), through the Ministry of Economic Growth and Job Creation (MEGJC), entered a US$274M Design-Build Construction Contract with China Harbour Engineering Company Limited (CHEC) … for the execution of the Montego Bay Perimeter Road Project (MBPRP).",
        "note": "Opened NROCC / H2K Jamaica official project page.",
    },
    {
        "id": "nrocc_montego_bay_perimeter",
        "type": "official",
        "chicago": "National Road Operating and Constructing Company Limited (NROCC). “Montego Bay Perimeter Road Project.” Project page (accessed 1 October 2026).",
        "url": "https://www.h2kjamaica.com.jm/montego-bay-project",
        "annotation": "Jamaican executing-agency primary notice of CHEC Design-Build contract. Supports chec_montego_bay_perimeter_jamaica.",
        "supports": ["chec_montego_bay_perimeter_jamaica", "hunt_infra_bridges_roads"],
    },
)

# 13 resources/copper — Baiyin Nonferrous acquires Serrote (MVV)
A(
    {
        "id": "baiyin_serrote_mvv_brazil_2025",
        "layer": "resources",
        "subcategory": "copper",
        "side": "prc",
        "counterpart": "Baiyin Nonferrous — acquisition of Mineração Vale Verde / Serrote copper-gold mine, Alagoas",
        "country": "Brazil",
        "asset": "100% equity sale completed Apr 2025 for US$420 million cash-free/debt-free; Serrote open-pit copper-gold operation (2024 production ~18.3 kt Cu)",
        "investment_type": "ownership_equity",
        "value": "420000000",
        "currency": "USD",
        "value_usd": "420000000",
        "fx_usd": "1",
        "fx_date": "2025-04-02",
        "year": "2025",
        "status": "active",
        "lat": "-9.61",
        "lon": "-36.77",
        "geo_note": "Serrote mine, Craíbas, Alagoas (Appian exit release).",
        "evidence": "documented",
        "source_id": "appian_baiyin_mvv_20250402",
        "note": "Actor: Baiyin Nonferrous Group (PRC SOE) — prc. Seller Appian Capital funds. Company exit release 2 Apr 2025. Distinct from Chinalco Toromocho / MMG Las Bambas / FCX Cerro Verde / Anglo Quellaveco.",
    },
    {
        "id": "baiyin_serrote_mvv_brazil_2025",
        "retrieved": "2026-10-01",
        "source_id": "appian_baiyin_mvv_20250402",
        "url": "https://appiancapitaladvisory.com/exit-appian-completes-sale-of-mvv-to-baiyin-nonferrous-for-us420-million/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Appian Capital Advisory LLP … is pleased to announce the completion of the sale of Mineração Vale Verde (“MVV”) to Baiyin Nonferrous Group Co., Ltd (“Baiyin Nonferrous”) for an all-cash offer of US$420 million. … owner of the Serrote greenfield open-pit copper-gold asset located in Alagoas, Brazil",
        "note": "Opened Appian Capital Advisory exit announcement.",
    },
    {
        "id": "appian_baiyin_mvv_20250402",
        "type": "official",
        "chicago": "Appian Capital Advisory. “EXIT: Appian completes sale of MVV to Baiyin Nonferrous for US$420 million.” 2 April 2025.",
        "url": "https://appiancapitaladvisory.com/exit-appian-completes-sale-of-mvv-to-baiyin-nonferrous-for-us420-million/",
        "annotation": "Seller primary completion notice for Baiyin Serrote/MVV acquisition. Supports baiyin_serrote_mvv_brazil_2025.",
        "supports": ["baiyin_serrote_mvv_brazil_2025", "hunt_res_copper"],
    },
)

# 14 infrastructure/building_materials — Holcim Peru entry via Comacsa/Mixercon
A(
    {
        "id": "holcim_comacsa_mixercon_peru_2024",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Holcim — acquisition of Comacsa and Mixercon (Peru market entry)",
        "country": "Peru",
        "asset": "2024 entry into Peru via Comacsa (industrial minerals/white cement) and Mixercon (cement/ready-mix); Holcim states these prior acquisitions preceded Pacasmayo majority stake",
        "investment_type": "ownership_equity",
        "value": "100000000",
        "currency": "USD",
        "value_usd": "100000000",
        "fx_usd": "1",
        "fx_date": "2024-08-09",
        "year": "2024",
        "status": "active",
        "lat": "-12.05",
        "lon": "-77.04",
        "geo_note": "Lima / national Peru footprint (Holcim/World Cement).",
        "evidence": "proxy",
        "source_id": "worldcement_holcim_comacsa_20240809",
        "note": "Actor: Holcim (Swiss) — allied. UNVERIFIED proxy: World Cement 9 Aug 2024 reports US$100m for 100% of Comacsa and Mixercon; Holcim NextGen Peru story corroborates 2024 Comacsa/Mixercon entry without stating price. Distinct from holcim_pacasmayo_peru_2025.",
    },
    {
        "id": "holcim_comacsa_mixercon_peru_2024",
        "retrieved": "2026-10-01",
        "source_id": "worldcement_holcim_comacsa_20240809",
        "url": "https://www.worldcement.com/the-americas/09082024/holcim-enters-perus-construction-market-with-the-acquisition-of-comacsa-and-mixercon/",
        "price_year": "2024",
        "evidence": "proxy",
        "quote": "Holcim … has entered Peru's construction market with the acquisition of 100% of the shares and operations of the companies Comacsa … and Mixercon … The investment made by Holcim was a total of US$100 million for both companies.",
        "note": "Opened World Cement trade press article.",
    },
    {
        "id": "worldcement_holcim_comacsa_20240809",
        "type": "press",
        "chicago": "Gardner, Evie. “Holcim enters Peru’s construction market with the acquisition of Comacsa and Mixercon.” World Cement, 9 August 2024.",
        "url": "https://www.worldcement.com/the-americas/09082024/holcim-enters-perus-construction-market-with-the-acquisition-of-comacsa-and-mixercon/",
        "annotation": "Trade press on Holcim Comacsa/Mixercon entry; USD 100m UNVERIFIED proxy. Supports holcim_comacsa_mixercon_peru_2024.",
        "supports": ["holcim_comacsa_mixercon_peru_2024", "hunt_infra_building_materials"],
    },
)

# 15 energy/solar — miss (thick; equal budget; no distinct new module/plant actor beyond SPIC/Atlas/Trina/Recurrent/Jinko/SMA set)

# 16 resources/nickel — miss (no distinct new Ni ownership beyond MMG/Anglo/Vale Onça Puma/Centaurus)

# 17 infrastructure/rail — CAF Medellín + Santiago metro units
A(
    {
        "id": "caf_medellin_santiago_metro_2024",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "CAF — metro rolling stock for Medellín (13 units) and Santiago Line 6 (6 units)",
        "country": "Colombia",
        "asset": "Combined contracts exceeding €200 million: 13 three-car INNEO metro trains for Medellín Lines A/B plus 6 five-car GoA4 units for Santiago Line 6 extensions",
        "investment_type": "rolling_stock",
        "value": "200000000",
        "currency": "EUR",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "6.25",
        "lon": "-75.57",
        "geo_note": "Medellín Metro primary award geocode; Santiago Line 6 portion is Chile (CAF dual award).",
        "evidence": "documented",
        "source_id": "caf_medellin_santiago_20241209",
        "note": "Actor: CAF (Spanish) — allied. Company 9 Dec 2024 release; combined value >€200m stored as EUR (no FX). Dual-country award mapped at Medellín with Chile noted. Distinct from Alstom Line 7 / CRRC Line B / Alstom Mexico DMU rows.",
    },
    {
        "id": "caf_medellin_santiago_metro_2024",
        "retrieved": "2026-10-01",
        "source_id": "caf_medellin_santiago_20241209",
        "url": "https://www.cafmobility.com/en/press-room/caf-to-supply-metro-units-colombia-and-chile/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "CAF has secured two new contracts to supply metro units based on its INNEO platform. The company will manufacture 13 units for the Medellín Metro and 6 units for the Santiago de Chile metro. The combined value of the contracts exceeds €200 million.",
        "note": "Opened CAF press room page.",
    },
    {
        "id": "caf_medellin_santiago_20241209",
        "type": "official",
        "chicago": "CAF. “CAF to supply metro units in Colombia and Chile.” 9 December 2024.",
        "url": "https://www.cafmobility.com/en/press-room/caf-to-supply-metro-units-colombia-and-chile/",
        "annotation": "Company primary Medellín/Santiago metro award notice. Supports caf_medellin_santiago_metro_2024.",
        "supports": ["caf_medellin_santiago_metro_2024", "hunt_latam_rail_telecom"],
    },
)

# 18 energy/wind — miss (no distinct new OEM award with clean non-paywalled primary beyond Vestas/Goldwind SPIC/Nordex set; Goldwind 470 MW FINAME claim lacked named project on goldwind.com)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added: list[str] = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]] = full
        else:
            by_id[rid] = len(rows)
            rows.append(full)
        added.append(rid)

        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

        sid = bib_entry["id"]
        if sid in bib_by:
            existing = bib[bib_by[sid]]
            supports = set(existing.get("supports") or [])
            supports.update(bib_entry.get("supports") or [])
            existing["supports"] = sorted(supports)
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

    hunt_updates = {
        "hunt_br_power_equip": "Cycle 6: logged siemens_axia_chesf_retrofit_2025.",
        "hunt_energy_fission_smr": "Cycle 6: logged invap_cnea_carem_mou_2024 (UNVERIFIED proxy).",
        "hunt_energy_other_renewables": "Cycle 6: logged lageo_chinameca_wb_2025.",
        "hunt_infra_engineering_epc": "Cycle 6: logged techint_saddn_epc_chile.",
        "hunt_infra_port_cranes": "Cycle 6: logged zpmc_portonave_sts_2025.",
        "hunt_fenb_araxa": "Cycle 6: equal budget; no distinct new FeNb ownership/price beyond CBMM/CMOC (miss).",
        "hunt_res_lithium": "Cycle 6: logged ganfeng_mariana_production_2025 (UNVERIFIED proxy).",
        "hunt_infra_port_ownership": "Cycle 6: logged ictsi_rio_brasil_expansion_2025.",
        "hunt_res_graphite": "Cycle 6: equal budget; no distinct new graphite mine/anode actor beyond South Star/Graphcoa/Nacional/Graphex (miss).",
        "hunt_res_balsa": "Cycle 6: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_res_water": "Cycle 6: logged gs_inima_atacama_desal_chile.",
        "hunt_infra_bridges_roads": "Cycle 6: logged chec_montego_bay_perimeter_jamaica.",
        "hunt_res_copper": "Cycle 6: logged baiyin_serrote_mvv_brazil_2025.",
        "hunt_infra_building_materials": "Cycle 6: logged holcim_comacsa_mixercon_peru_2024 (UNVERIFIED proxy value).",
        "hunt_energy_solar": "Cycle 6: equal budget; thick subcategory — miss.",
        "hunt_res_nickel": "Cycle 6: equal budget; no distinct new Ni ownership beyond MMG/Anglo/Vale/Centaurus (miss).",
        "hunt_latam_rail_telecom": "Cycle 6: logged caf_medellin_santiago_metro_2024.",
        "hunt_energy_wind": "Cycle 6: equal budget; no clean named-project OEM award beyond prior Vestas/Goldwind/Nordex set (miss).",
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
    print("Cycle 6 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
