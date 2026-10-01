#!/usr/bin/env python3
"""Cycle 46 hunt: shuffle_seed=20261046; equal budget; U.S. side ≥1/3; thin_topup after.

Order: graphite, other_renewables, fission_smr, niobium, solar, rail, lithium,
building_materials, port_ownership, port_cranes, wind, water, balsa, copper,
nickel, engineering_epc, power_plants_grid, bridges_roads.
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


# ---------------------------------------------------------------------------
# 1 resources/graphite — Graphcoa Boa Sorte expansion CAPEX USD 20.6m (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "graphcoa_boa_sorte_expand_20p6m_2025",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "Graphcoa / Appian Capital — Boa Sorte full-scale expansion (Itagimirim)",
        "country": "Brazil",
        "asset": "Sep 2025 In The Mine citing Graphcoa/RIMA (DOM Itagimirim 10 Feb 2025): LP/LI filed to expand Boa Sorte from 5.5 ktpa to 20 ktpa concentrate. Total implementation CAPEX estimated at USD 20.6 million (plant equipment, PDER, contingency); initial assets/commissioning ~USD 1m. Distinct from graphcoa_boa_sorte_bahia_2024 (phase-1 presence) and graphcoa_boa_sorte_urbix_export_2025.",
        "investment_type": "brownfield_expansion",
        "value": "20600000",
        "currency": "USD",
        "value_usd": "20600000",
        "fx_usd": "1",
        "fx_date": "2025-09-01",
        "year": "2025",
        "status": "active",
        "lat": "-16.00",
        "lon": "-40.08",
        "geo_note": "Mina Boa Sorte, Itagimirim, Bahia (União Baiana district; approximate pin).",
        "evidence": "documented",
        "source_id": "inthemine_graphcoa_boa_sorte_202509",
        "note": "Actor: Graphcoa (Appian Capital Advisory, UK) — allied. CAPEX from In The Mine citing Graphcoa/RIMA. Distinct from Jordânia DFS CAPEX and cumulative spend rows.",
    },
    {
        "id": "graphcoa_boa_sorte_expand_20p6m_2025",
        "retrieved": "2026-10-01",
        "source_id": "inthemine_graphcoa_boa_sorte_202509",
        "url": "https://www.inthemine.com.br/site/em-ramp-up-mina-de-grafite-ja-prepara-expansao/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Para a implementação total, incluindo a construção da PDER e fechamento da lavra, além da aquisição de equipamentos para a planta e do fundo de contingência, o investimento estimado chega a US$ 20,6 milhões.",
        "note": "Opened In The Mine (Facto) Sep 2025 article on Boa Sorte expansion licensing and CAPEX.",
    },
    {
        "id": "inthemine_graphcoa_boa_sorte_202509",
        "type": "press",
        "chicago": "Revista In The Mine. “Em ramp up, mina de grafite já prepara expansão.” September 2025.",
        "url": "https://www.inthemine.com.br/site/em-ramp-up-mina-de-grafite-ja-prepara-expansao/",
        "annotation": "Portuguese mining press on Graphcoa Boa Sorte 5.5→20 ktpa expansion CAPEX USD 20.6m. Supports graphcoa_boa_sorte_expand_20p6m_2025.",
        "supports": ["graphcoa_boa_sorte_expand_20p6m_2025", "hunt_res_graphite"],
    },
)

# ---------------------------------------------------------------------------
# 2 energy/other_renewables — ContourGlobal (KKR) Oasis de Atacama EV >USD 900m (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "contourglobal_oasis_atacama_ev_2024",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "ContourGlobal (KKR) — Oasis de Atacama Quillagua I–II / Víctor Jara portfolio",
        "country": "Chile",
        "asset": "17 Dec 2024: ContourGlobal (KKR portfolio company) acquires from Grenergy the first three Oasis de Atacama phases (Quillagua I–II, Antofagasta; Víctor Jara, Tarapacá): 451 MWp solar PV + 2.5 GWh BESS. Company states enterprise value more than USD 900 million including secured project finance debt of USD 643 million; 15-year overnight PPA. Distinct from byd_grenergy_central_oasis_2026 (BYD battery supply) and cip_arena/cip_patache BESS rows.",
        "investment_type": "ownership_equity",
        "value": "900000000",
        "currency": "USD",
        "value_usd": "900000000",
        "fx_usd": "1",
        "fx_date": "2024-12-17",
        "year": "2024",
        "status": "active",
        "lat": "-21.70",
        "lon": "-69.50",
        "geo_note": "Quillagua / northern Atacama hybrid solar+BESS corridor (approximate portfolio pin).",
        "evidence": "documented",
        "source_id": "contourglobal_oasis_atacama_20241217",
        "note": "Actor: ContourGlobal owned by KKR (U.S. PE) — us. Value at ContourGlobal stated floor (>USD 900m EV). Seller Grenergy cited up to USD 962m including earn-outs (not used as primary figure).",
    },
    {
        "id": "contourglobal_oasis_atacama_ev_2024",
        "retrieved": "2026-10-01",
        "source_id": "contourglobal_oasis_atacama_20241217",
        "url": "https://www.contourglobal.com/news/contourglobal-enters-chile-large-scale-solar-pv-and-bess-portfolio-capable-powering/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "The transaction for more than US$900 million Enterprise Value (including secured project finance debt of US$643 million) comprises three independent projects in the Northern regions of Atacama (Quillagua I and II in Antofagasta and Victor Jara in Tarapacá), with a hybrid Solar PV generation capacity of 451 MWp and 2.5 GWh of BESS.",
        "note": "Opened ContourGlobal company release 17 Dec 2024. Corroboration: Grenergy PR (up to USD 962m EV).",
    },
    {
        "id": "contourglobal_oasis_atacama_20241217",
        "type": "company",
        "chicago": "ContourGlobal. “ContourGlobal enters Chile with large scale solar PV and BESS portfolio capable of powering the country at night.” 17 December 2024.",
        "url": "https://www.contourglobal.com/news/contourglobal-enters-chile-large-scale-solar-pv-and-bess-portfolio-capable-powering/",
        "annotation": "KKR ContourGlobal primary on >USD 900m EV Oasis de Atacama acquisition. Supports contourglobal_oasis_atacama_ev_2024.",
        "supports": ["contourglobal_oasis_atacama_ev_2024", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# 3–4, 6, 8, 11–12, 14, 16–18 misses noted in hunt stubs below
# fission_smr, niobium, rail, building_materials, wind, water, copper,
# engineering_epc, power_plants_grid, bridges_roads
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 5 energy/solar — Cox Energy Ecuador package USD 600m (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cox_ecuador_renewables_600m_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "allied",
        "counterpart": "Grupo COX (Spain) — Ecuador renewable package (Tocachi, Malchingui, La Ceiba 1, Matala, Illapo 1)",
        "country": "Ecuador",
        "asset": "30 Jun 2025: Ecuador Presidential Communication Secretariat announces USD 600 million investment package with Spanish Grupo COX for five electric projects — Tocachi, Malchingui, La Ceiba 1, Matala, Illapo 1 — plus an 80 km transmission line, as part of a USD 1 billion China+Spain energy announcement (PowerChina USD 400m tracked separately as powerchina_coca_codo_om_2026).",
        "investment_type": "greenfield_generation",
        "value": "600000000",
        "currency": "USD",
        "value_usd": "600000000",
        "fx_usd": "1",
        "fx_date": "2025-06-30",
        "year": "2025",
        "status": "active",
        "lat": "-0.05",
        "lon": "-78.45",
        "geo_note": "Tocachi / Malchingui corridor north of Quito (named project cluster; approximate pin).",
        "evidence": "documented",
        "source_id": "comunicacion_ec_cox_powerchina_20250630",
        "note": "Actor: Grupo COX (Spain) — allied. Official Ecuador government bulletin. CAPEX at announced package total; individual plant CAPEX not broken out on the page.",
    },
    {
        "id": "cox_ecuador_renewables_600m_2025",
        "retrieved": "2026-10-01",
        "source_id": "comunicacion_ec_cox_powerchina_20250630",
        "url": "https://www.comunicacion.gob.ec/como-resultado-de-la-gira-presidencial-ecuador-recibira-usd-1-000-millones-de-inversion-extranjera-de-china-y-espana-para-el-sector-energetico/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Mientras que los USD 600 millones, de la cifra de inversión global, se concretaron durante la visita del presidente Noboa a España, en donde se acordaron negociaciones con el Grupo COX … Esta firma invertirá en cinco proyectos eléctricos: Tocachi, Malchingui, La Ceiba 1, Matala, Illapo 1, y en una línea de transmisión de 80 kilómetros.",
        "note": "Opened Secretaría General de Comunicación de la Presidencia bulletin 30 Jun 2025.",
    },
    {
        "id": "comunicacion_ec_cox_powerchina_20250630",
        "type": "official",
        "chicago": "Ecuador. Secretaría General de Comunicación de la Presidencia. “Como resultado de la gira presidencial, Ecuador recibirá USD 1.000 millones de inversión extranjera de China y España para el sector energético.” Boletín N° 39, 30 June 2025.",
        "url": "https://www.comunicacion.gob.ec/como-resultado-de-la-gira-presidencial-ecuador-recibira-usd-1-000-millones-de-inversion-extranjera-de-china-y-espana-para-el-sector-energetico/",
        "annotation": "Official Ecuador release on COX USD 600m renewable package. Supports cox_ecuador_renewables_600m_2025.",
        "supports": ["cox_ecuador_renewables_600m_2025", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 7 resources/lithium — Lithium Argentina / Ganfeng PPG Stage 1 CAPEX USD 1.1bn
# ---------------------------------------------------------------------------
A(
    {
        "id": "lithium_argentina_ppg_stage1_1p1bn_2025",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "Lithium Argentina / Ganfeng — PPG Stage 1 (Pozuelos–Pastos Grandes) CAPEX",
        "country": "Argentina",
        "asset": "10 Nov 2025: Lithium Argentina and Ganfeng announce PPG Scoping Study — Stage 1 initial capital cost estimated at USD 1.1 billion (incl. 16% contingency) for 50,000 tpa LCE; Stage 1 DIA environmental approval received; total life-of-project capital USD 3.3 billion across three stages. Distinct from ganfeng_lithea_ppg_2022 (asset acquisition up to USD 962m) and ganfeng_laac_convertible_180m_2026.",
        "investment_type": "greenfield_mine",
        "value": "1100000000",
        "currency": "USD",
        "value_usd": "1100000000",
        "fx_usd": "1",
        "fx_date": "2025-11-10",
        "year": "2025",
        "status": "active",
        "lat": "-24.55",
        "lon": "-66.75",
        "geo_note": "Pastos Grandes / Pozuelos basin, Salta Province (project geography; approximate pin).",
        "evidence": "documented",
        "source_id": "lithium_argentina_ppg_scoping_20251110",
        "note": "Actor: Lithium Argentina AG (allied listed) with PRC partner Ganfeng in PPG JV — coded allied for Lithium Argentina Stage 1 CAPEX disclosure. Company IR / SEC exhibit.",
    },
    {
        "id": "lithium_argentina_ppg_stage1_1p1bn_2025",
        "retrieved": "2026-10-01",
        "source_id": "lithium_argentina_ppg_scoping_20251110",
        "url": "https://investors.lithium-argentina.com/news-releases/news-release-details/lithium-argentina-and-ganfeng-announce-ppg-scoping-study-results",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Competitive capital cost: Stage 1 initial capital cost estimated at $1.1 billion (including 16% contingency). Total capital cost of $3.3 billion over life of project.",
        "note": "Opened Lithium Argentina IR release 10 Nov 2025. SEC exhibit 99.1 corroborates same figures.",
    },
    {
        "id": "lithium_argentina_ppg_scoping_20251110",
        "type": "company",
        "chicago": "Lithium Argentina AG. “Lithium Argentina and Ganfeng Announce PPG Scoping Study Results and Stage 1 Environmental Approval.” 10 November 2025.",
        "url": "https://investors.lithium-argentina.com/news-releases/news-release-details/lithium-argentina-and-ganfeng-announce-ppg-scoping-study-results",
        "annotation": "Company primary on PPG Stage 1 USD 1.1bn CAPEX and DIA approval. Supports lithium_argentina_ppg_stage1_1p1bn_2025.",
        "supports": ["lithium_argentina_ppg_stage1_1p1bn_2025", "hunt_res_lithium"],
    },
)

# ---------------------------------------------------------------------------
# 9 infrastructure/port_ownership — SSA Marine Lázaro Cárdenas Isla de la Palma yard (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ssa_lazaro_isla_palma_mxn143m_2025",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "us",
        "counterpart": "SSA Marine México — Isla de la Palma vehicle distribution yard (Lázaro Cárdenas)",
        "country": "Mexico",
        "asset": "2025 (Alera SCI 18 Mar 2026 roundup): SSA Marine México enables an external vehicle patio on Isla de la Palma (10.5 ha, ~2.5 km from port) with capacity for 4,918 units and 15 madrina docks; investment MXN 142.6 million. Complements on-terminal TEA Polígono 5 expansion (MXN 54.2 million; not separate row). Distinct from ssa_progreso_cruise_54m_2026 and apmt_lazaro_phase3_350m_2026.",
        "investment_type": "brownfield_expansion",
        "value": "142600000",
        "currency": "MXN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "17.96",
        "lon": "-102.17",
        "geo_note": "Isla de la Palma / Lázaro Cárdenas, Michoacán (terminal-adjacent yard; approximate pin).",
        "evidence": "documented",
        "source_id": "alerasci_ssa_mexico_20260318",
        "note": "Actor: SSA Marine / Carrix (U.S.) via SSA Marine México — us. Spanish trade blog summarizing 2025 SSA investments. MXN stored without FX (no Fed H.10 pin on page).",
    },
    {
        "id": "ssa_lazaro_isla_palma_mxn143m_2025",
        "retrieved": "2026-10-01",
        "source_id": "alerasci_ssa_mexico_20260318",
        "url": "https://alerasci.com/crecimiento-estrategico-y-operacion-responsable/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Complementando esta acción, se habilitó un patio externo en la Isla de la Palma con un área de 10.5 hectáreas, a solo 2.5 km del puerto, con capacidad para 4,918 unidades. … La inversión en este proyecto fue de 142.6 millones de pesos.",
        "note": "Opened Alera SCI 18 Mar 2026 Spanish coverage of SSA Marine México 2025 investments.",
    },
    {
        "id": "alerasci_ssa_mexico_20260318",
        "type": "press",
        "chicago": "Alera SCI. “Crecimiento estratégico y operación responsable.” 18 March 2026.",
        "url": "https://alerasci.com/crecimiento-estrategico-y-operacion-responsable/",
        "annotation": "Spanish logistics press on SSA Marine México 2025 Manzanillo STS and Lázaro Cárdenas auto-yard investments. Supports ssa_lazaro_isla_palma_mxn143m_2025 and ssa_manzanillo_sts_21m_2025.",
        "supports": [
            "ssa_lazaro_isla_palma_mxn143m_2025",
            "ssa_manzanillo_sts_21m_2025",
            "hunt_infra_port_ownership",
            "hunt_infra_port_cranes",
        ],
    },
)

# ---------------------------------------------------------------------------
# 10 infrastructure/port_cranes — SSA Manzanillo TEC I Super Post-Panamax STS (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ssa_manzanillo_sts_21m_2025",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "us",
        "counterpart": "SSA Marine México — Manzanillo TEC I Super Post-Panamax STS cranes",
        "country": "Mexico",
        "asset": "2025 (Alera SCI 18 Mar 2026): Terminal Especializada de Contenedores I (TEC I) at Manzanillo incorporates two new Super Post-Panamax STS cranes with investment exceeding USD 21 million; each crane rated to 65 t under spreader / 80 t under hook. Distinct from ssa_guaymas_sts_ertg_2026 and zpmc_cmsa_manzanillo_rtg_2025.",
        "investment_type": "equipment_supply",
        "value": "21000000",
        "currency": "USD",
        "value_usd": "21000000",
        "fx_usd": "1",
        "fx_date": "2025-12-31",
        "year": "2025",
        "status": "active",
        "lat": "19.07",
        "lon": "-104.30",
        "geo_note": "TEC I, Puerto de Manzanillo, Colima (terminal pin).",
        "evidence": "documented",
        "source_id": "alerasci_ssa_mexico_20260318",
        "note": "Actor: SSA Marine / Carrix (U.S.) — us. Value at stated floor (>USD 21m). Same Alera SCI source family as Isla de la Palma yard row.",
    },
    {
        "id": "ssa_manzanillo_sts_21m_2025",
        "retrieved": "2026-10-01",
        "source_id": "alerasci_ssa_mexico_20260318",
        "url": "https://alerasci.com/crecimiento-estrategico-y-operacion-responsable/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Así mismo durante el año, la TEC I incorporó dos nuevas grúas Super Post-Panamax, realizando así una inversión superior a 21 millones de dólares. Cada grúa cuenta con capacidad de hasta 65 toneladas bajo spreader y hasta 80 toneladas bajo gancho.",
        "note": "Opened Alera SCI 18 Mar 2026.",
    },
    {
        "id": "alerasci_ssa_mexico_20260318",
        "type": "press",
        "chicago": "Alera SCI. “Crecimiento estratégico y operación responsable.” 18 March 2026.",
        "url": "https://alerasci.com/crecimiento-estrategico-y-operacion-responsable/",
        "annotation": "Spanish logistics press on SSA Marine México 2025 Manzanillo STS and Lázaro Cárdenas auto-yard investments. Supports ssa_lazaro_isla_palma_mxn143m_2025 and ssa_manzanillo_sts_21m_2025.",
        "supports": [
            "ssa_lazaro_isla_palma_mxn143m_2025",
            "ssa_manzanillo_sts_21m_2025",
            "hunt_infra_port_ownership",
            "hunt_infra_port_cranes",
        ],
    },
)

# ---------------------------------------------------------------------------
# 13 resources/balsa — Plantabal BALTEK SBC FSC MIX product declaration (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "plantabal_baltek_sbc_fsc_mix_2025",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "allied",
        "counterpart": "3A Composites / Plantabal — BALTEK SBC FSC MIX product declaration (Ecuador)",
        "country": "Ecuador",
        "asset": "15 May 2025: 3A Composites Core Materials announces that effective 1 May 2025 BALTEK SBC balsa core products are formally declared FSC MIX certified on select markets, extending FSC claims from Ecuador/PNG plantation patrimony through Chain of Custody to end products used in wind-blade cores and other sandwich applications. Distinct from plantabal_3a_ecuador_presence and plantabal_2025_planting_2951ha (no duplicate trade/financing row).",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Plantabal Quevedo processing site, Los Ríos (company site geography).",
        "evidence": "documented",
        "source_id": "3a_baltek_sbc_fsc_mix_20250515",
        "note": "Actor: 3A Composites / Plantabal (Switzerland/Schweiter) — allied. Processor/certification angle for wind-blade balsa supply chain; no CAPEX figure on page.",
    },
    {
        "id": "plantabal_baltek_sbc_fsc_mix_2025",
        "retrieved": "2026-10-01",
        "source_id": "3a_baltek_sbc_fsc_mix_20250515",
        "url": "https://www.3accorematerials.com/en/news-and-stories/3a-composites-core-materials-officially-declares-baltek-sbc-products-as-fsc-mix-certified-on-select-markets",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Effective May 1, 2025, 3A Composites Core Materials is proud to have switched to formally declare its BALTEK® SBC product line as FSC™ MIX certified … A FSC™ MIX product is comprised by at least 70% wood from FSC managed plantations (in this case, the 3A Composites Core Materials forest patrimony in Ecuador and Papua New Guinea).",
        "note": "Opened 3A Composites Core Materials news 15 May 2025.",
    },
    {
        "id": "3a_baltek_sbc_fsc_mix_20250515",
        "type": "company",
        "chicago": "3A Composites Core Materials. “3A Composites Core Materials officially declares BALTEK® SBC products as FSC™ MIX certified on select markets.” 15 May 2025.",
        "url": "https://www.3accorematerials.com/en/news-and-stories/3a-composites-core-materials-officially-declares-baltek-sbc-products-as-fsc-mix-certified-on-select-markets",
        "annotation": "Company primary on BALTEK SBC FSC MIX declaration tied to Ecuador plantations. Supports plantabal_baltek_sbc_fsc_mix_2025.",
        "supports": ["plantabal_baltek_sbc_fsc_mix_2025", "hunt_res_balsa"],
    },
)

# ---------------------------------------------------------------------------
# 15 resources/nickel — Brazilian Nickel–Westwin U.S. MHP offtake MoU (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "brazilian_nickel_westwin_offtake_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "us",
        "counterpart": "Westwin Elements — offtake MoU for Brazilian Nickel Piauí MHP (U.S. refining)",
        "country": "Brazil",
        "asset": "19–20 Jan 2026: Brazilian Nickel signs non-binding offtake MoU with U.S. refiner Westwin Elements (Oklahoma) for Piauí Nickel Project MHP destined to Class 1 nickel powder/briquettes in the United States. Press reports up to 10,000 tpa Ni-in-MHP and ~240–400 tpa Co-in-MHP (UNVERIFIED press figures). Distinct from brazilian_nickel_dfc_loi_2024 / bndes_piaui_nickel_maq_100m_2026 financing rows — offtake angle.",
        "investment_type": "offtake",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-8.23",
        "lon": "-42.30",
        "geo_note": "Piauí Nickel Project, Capitão Gervásio Oliveira, Piauí (project geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "mining_brn_westwin_20260120",
        "note": "Actor: Westwin Elements (U.S.) offtaker — us. Press-only tonnage figures marked UNVERIFIED. Non-binding MoU. Complements DFC LOI / BNDES financing without duplicating those rows.",
    },
    {
        "id": "brazilian_nickel_westwin_offtake_2026",
        "retrieved": "2026-10-01",
        "source_id": "mining_brn_westwin_20260120",
        "url": "https://www.mining.com/brazilian-nickel-westwin-ink-offtake-mou-on-piaui-project-for-us-market/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Under the deal, the UK-based miner would sell 10,000 tonnes per annum (tpa) of nickel in MHP and about 240 to 400 tpa of cobalt in MHP, extracted from its Piauí deposit in Brazil … Westwin, which operates the only major US nickel refinery in Oklahoma, would then process the MHP material into class 1 nickel powder and briquettes for the US market.",
        "note": "Opened Mining.com 20 Jan 2026 (quotes Brazilian Nickel news release). Company media landing returned 404 at retrieval; tonnage UNVERIFIED press proxy.",
    },
    {
        "id": "mining_brn_westwin_20260120",
        "type": "journalism",
        "chicago": "Mining.com. “Brazilian Nickel, Westwin ink offtake deal on Piauí project for US market.” 20 January 2026.",
        "url": "https://www.mining.com/brazilian-nickel-westwin-ink-offtake-mou-on-piaui-project-for-us-market/",
        "annotation": "Trade press on Brazilian Nickel–Westwin non-binding MHP offtake MoU for U.S. refining. Supports brazilian_nickel_westwin_offtake_2026 (press tonnage UNVERIFIED).",
        "supports": ["brazilian_nickel_westwin_offtake_2026", "hunt_res_nickel"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None:
                existing[k] = v
    else:
        bib.append(bib_entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_entry)

    hunt_updates = {
        "hunt_res_graphite": "Cycle 46: logged graphcoa_boa_sorte_expand_20p6m_2025 (allied; USD 20.6m expansion CAPEX).",
        "hunt_energy_other_renewables": "Cycle 46: logged contourglobal_oasis_atacama_ev_2024 (U.S./KKR; >USD 900m EV).",
        "hunt_energy_fission_smr": "Cycle 46: equal budget; El Salvador 123 / Argentina FIRST / Meitner already (miss).",
        "hunt_fenb_araxa": "Cycle 46: equal budget; Codemig renewal / CBMM spend already (miss).",
        "hunt_energy_solar": "Cycle 46: logged cox_ecuador_renewables_600m_2025 (allied; USD 600m).",
        "hunt_latam_rail_telecom": "Cycle 46: equal budget; Mota-Engil QI / CRCC / Siemens EFE already (miss).",
        "hunt_res_lithium": "Cycle 46: logged lithium_argentina_ppg_stage1_1p1bn_2025 (allied; USD 1.1bn Stage 1 CAPEX).",
        "hunt_infra_building_materials": "Cycle 46: equal budget; Holcim/Cemex already dense (miss).",
        "hunt_infra_port_ownership": "Cycle 46: logged ssa_lazaro_isla_palma_mxn143m_2025 (U.S.; MXN 142.6m).",
        "hunt_infra_port_cranes": "Cycle 46: logged ssa_manzanillo_sts_21m_2025 (U.S.; >USD 21m).",
        "hunt_energy_wind": "Cycle 46: equal budget; Vestas Dom Inocêncio/Esquina / Goldwind Sento Sé already (miss).",
        "hunt_res_water": "Cycle 46: equal budget; SADDN/Collahuasi/Aguas Pacífico already (miss).",
        "hunt_res_balsa": "Cycle 46: logged plantabal_baltek_sbc_fsc_mix_2025 (allied; processor FSC MIX declaration — not trade duplicate).",
        "hunt_res_copper": "Cycle 46: equal budget; FCX El Abra USD 7.5bn already (miss).",
        "hunt_res_nickel": "Cycle 46: logged brazilian_nickel_westwin_offtake_2026 (U.S.; offtake MoU — not financing duplicate).",
        "hunt_infra_engineering_epc": "Cycle 46: equal budget; Techint/Bechtel/Worley already dense (miss).",
        "hunt_br_power_equip": "Cycle 46: equal budget; GE Vernova Azulão / PowerChina Coca Codo already (miss).",
        "hunt_infra_bridges_roads": "Cycle 46: equal budget; CHEC/Mota-Engil/OHLA already (miss).",
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
    print("Cycle 46 rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
