#!/usr/bin/env python3
"""Cycle 5 hunt: shuffle_seed=20261005; equal budget across 18 subcategories."""
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


# seed 20261005 order:
# graphite, balsa, engineering_epc, niobium, bridges_roads, solar, lithium,
# building_materials, power_plants_grid, fission_smr, port_ownership, wind,
# other_renewables, port_cranes, rail, water, nickel, copper

# 1 resources/graphite — miss (no distinct new LatAm mine/anode actor beyond South Star/Graphcoa/Nacional/Graphex)

# 2 resources/balsa — miss (WITS 2022–2024 pairs already thick)

# 3 infrastructure/engineering_epc — Worley Lead Integration Delivery Partner, Rincon Li plant
A(
    {
        "id": "worley_rincon_lithium_epc_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "Worley — Lead Integration Delivery Partner for Rio Tinto Rincon lithium carbonate plant (Argentina)",
        "country": "Argentina",
        "asset": "Worley named Lead Integration Delivery Partner for Rincon Li2CO3 plant delivery/subcontractor coordination (Rio Tinto >USD 2bn project context)",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-24.1",
        "lon": "-66.95",
        "geo_note": "Salar de Rincón / Puna, Salta (Worley release).",
        "evidence": "documented",
        "source_id": "worley_rincon_20250227",
        "note": "Actor: Worley (Australian) — allied; customer Rio Tinto. Company insight 27 Feb 2025: Lead Integration Delivery Partner for Rincon lithium carbonate plant. Complements rio_tinto_rincon_expansion_2024 ownership row; non-grid EPC.",
    },
    {
        "id": "worley_rincon_lithium_epc_2025",
        "retrieved": "2026-10-01",
        "source_id": "worley_rincon_20250227",
        "url": "https://www.worley.com/en/insights/our-news/resources/2025/helping-rio-tinto-scaleup-production-critical-battery-materials",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Rincon Mining recently named Worley as the Lead Integration Delivery Partner for its new lithium project in Argentina. With a total investment of more than $2 billion USD by Rio Tinto ... We are responsible for the delivery of the lithium carbonate plant and coordination with all subcontractors",
        "note": "Opened Worley company news/insight page.",
    },
    {
        "id": "worley_rincon_20250227",
        "type": "official",
        "chicago": "Worley. “Helping Rio Tinto scale up production of critical battery materials.” 27 February 2025.",
        "url": "https://www.worley.com/en/insights/our-news/resources/2025/helping-rio-tinto-scaleup-production-critical-battery-materials",
        "annotation": "Company primary Rincon Lead Integration Delivery Partner notice. Supports worley_rincon_lithium_epc_2025.",
        "supports": ["worley_rincon_lithium_epc_2025", "hunt_infra_engineering_epc"],
    },
)

# 4 resources/niobium — CBMM R$10bn five-year investment plan (thin; press)
A(
    {
        "id": "cbmm_araxa_capex_plan_2025",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "CBMM — Araxá niobium complex five-year investment plan",
        "country": "Brazil",
        "asset": "Reported R$10 billion investment plan over five years (half industrial expansion/maintenance); ~100 kt FeNb-equivalent production target 2025",
        "investment_type": "ownership_equity",
        "value": "10000000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "Araxá, Minas Gerais (Folha/Reuters citing CBMM).",
        "evidence": "proxy",
        "source_id": "folha_cbmm_capex_20251030",
        "note": "Actor: CBMM (Brazilian Moreira Salles–controlled; Chinese steel consortium minority) — allied coding retained with prior CBMM presence row. UNVERIFIED proxy: Folha/Reuters interview quotes R$10bn five-year plan and 100 kt 2025 FeNb-eq target. Value stored as BRL (no FX). Complements cbmm_araxa_presence_2024.",
    },
    {
        "id": "cbmm_araxa_capex_plan_2025",
        "retrieved": "2026-10-01",
        "source_id": "folha_cbmm_capex_20251030",
        "url": "https://www1.folha.uol.com.br/mercado/2025/10/cbmm-preve-elevar-producao-de-ferrobiobio-em-5-neste-ano-e-investir-r-10-bi-em-5-anos.shtml",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "a empresa conta com uma previsão de investimentos de R$ 10 bilhões nos próximos cinco anos, sendo que metade desse valor está relacionada com a expansão das atividades industriais ... CBMM prevê produzir neste ano 100 mil toneladas de ferronióbio equivalente",
        "note": "Opened Folha de S.Paulo page (Reuters byline).",
    },
    {
        "id": "folha_cbmm_capex_20251030",
        "type": "journalism",
        "chicago": "Folha de S.Paulo / Reuters (Marta Nogueira). “CBMM prevê elevar produção de ferrobióbio em 5% neste ano e investir R$ 10 bi em 5 anos.” 30 October 2025.",
        "url": "https://www1.folha.uol.com.br/mercado/2025/10/cbmm-preve-elevar-producao-de-ferrobiobio-em-5-neste-ano-e-investir-r-10-bi-em-5-anos.shtml",
        "annotation": "Press interview on CBMM capex/production plan. Supports cbmm_araxa_capex_plan_2025 (UNVERIFIED proxy).",
        "supports": ["cbmm_araxa_capex_plan_2025", "hunt_fenb_araxa"],
    },
)

# 5 infrastructure/bridges_roads — miss (no distinct new highway/bridge award beyond prior CHEC/CRCC/CRBC rows)

# 6 energy/solar — Atlas/Hydro Rein Vista Alegre 902 MWp
A(
    {
        "id": "atlas_vista_alegre_solar_br_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "allied",
        "counterpart": "Atlas Renewable Energy (majority) / Hydro Rein (20%) — Vista Alegre Solar Complex, Minas Gerais",
        "country": "Brazil",
        "asset": "902 MWp Vista Alegre solar complex (Brazil’s largest single-phase); full COD early Dec 2024; Hydro Rein acquired 20% Jan 2025; Albras 21-year PPA",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-15.8",
        "lon": "-43.27",
        "geo_note": "Janaúba, Minas Gerais (Hydro Rein / Atlas releases).",
        "evidence": "documented",
        "source_id": "hydrorein_vista_alegre_20250130",
        "note": "Actor: Atlas (GIP-backed) majority + Hydro Rein (Norwegian/Macquarie) 20% — allied. Hydro Rein release 30 Jan 2025: 902 MWp; ~2 TWh/year; BNDES largest USD renewable loan. Complements SPIC Marangatu / Ciranda solar rows.",
    },
    {
        "id": "atlas_vista_alegre_solar_br_2025",
        "retrieved": "2026-10-01",
        "source_id": "hydrorein_vista_alegre_20250130",
        "url": "https://www.hydrorein.com/en/news/hydro-rein-acquires-stake-in-brazils-largest-single-phase-solar-complex-vista-alegre/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Hydro Rein ... has acquired a 20% stake in the Vista Alegre solar power complex from Atlas Renewable Energy ... The 902 MWp solar complex, which began full commercial operations in early December, is expected to produce 2 TWh annually.",
        "note": "Opened Hydro Rein company news page.",
    },
    {
        "id": "hydrorein_vista_alegre_20250130",
        "type": "official",
        "chicago": "Hydro Rein. “Hydro Rein acquires stake in Brazil’s largest single-phase solar complex, Vista Alegre.” 30 January 2025.",
        "url": "https://www.hydrorein.com/en/news/hydro-rein-acquires-stake-in-brazils-largest-single-phase-solar-complex-vista-alegre/",
        "annotation": "Company primary Vista Alegre equity acquisition/COD notice. Supports atlas_vista_alegre_solar_br_2025.",
        "supports": ["atlas_vista_alegre_solar_br_2025", "hunt_energy_solar"],
    },
)

# 7 resources/lithium — Eramet Centenario Phase 1 inauguration
A(
    {
        "id": "eramet_centenario_phase1_2024",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "Eramet / Eramine — Centenario-Ratones Phase 1 DLE plant (Salta)",
        "country": "Argentina",
        "asset": "Centenario Phase 1 DLE plant inaugurated Jul 2024; design 24,000 tpy battery-grade Li2CO3; ~USD 870m investment (100% basis); JV then Eramet 50.1% / Tsingshan 49.9%",
        "investment_type": "ownership_equity",
        "value": "870000000",
        "currency": "USD",
        "value_usd": "870000000",
        "fx_usd": "1",
        "fx_date": "2024-07-03",
        "year": "2024",
        "status": "active",
        "lat": "-24.1",
        "lon": "-66.6",
        "geo_note": "Centenario-Ratones salar, Salta Province (Eramet release; approximate).",
        "evidence": "documented",
        "source_id": "eramet_centenario_20240703",
        "note": "Actor: Eramet (French) majority JV with Tsingshan (PRC) at inauguration — coded allied for Eramet operator/majority. Company release 3 Jul 2024: USD 870m Phase 1; 24 ktpy LCE. Complements Rio Tinto Rincon / Ganfeng rows. Later Eramet bought out Tsingshan (not required for this row).",
    },
    {
        "id": "eramet_centenario_phase1_2024",
        "retrieved": "2026-10-01",
        "source_id": "eramet_centenario_20240703",
        "url": "https://www.eramet.com/en/news/eramet-inaugurates-its-direct-lithium-extraction-plant-in-argentina-becoming-the-first-european-company-to-produce-battery-grade-lithium-carbonate-at-industrial-scale/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "This industrial flagship is operated by Eramine, a joint venture owned by Eramet (50.1%) and its partner Tsingshan (49.9%). ... At full capacity, the Centenario Phase 1 plant will produce 24,000 t/year ... The total amount of investment for Centenario Phase 1 is forecast to be around $870m",
        "note": "Opened Eramet company news release.",
    },
    {
        "id": "eramet_centenario_20240703",
        "type": "official",
        "chicago": "Eramet. “Eramet inaugurates its direct lithium extraction plant in Argentina, becoming the first European company to produce battery-grade lithium carbonate at industrial scale.” 3 July 2024.",
        "url": "https://www.eramet.com/en/news/eramet-inaugurates-its-direct-lithium-extraction-plant-in-argentina-becoming-the-first-european-company-to-produce-battery-grade-lithium-carbonate-at-industrial-scale/",
        "annotation": "Company primary Centenario Phase 1 inauguration. Supports eramet_centenario_phase1_2024.",
        "supports": ["eramet_centenario_phase1_2024", "hunt_res_lithium"],
    },
)

# 8 infrastructure/building_materials — Carmeuse Cementos Bío Bío (thin)
A(
    {
        "id": "carmeuse_bio_bio_chile_2025",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Carmeuse Group — controlling stake in Cementos Bío Bío (Chile)",
        "country": "Chile",
        "asset": "Acquisition of 97.1% of Cementos Bío Bío (4 cement plants Chile + 1 Peru; lime/concrete footprint Chile/Argentina/Peru); tender closed 11 Sep 2025",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-36.82",
        "lon": "-73.05",
        "geo_note": "Concepción / Bío Bío region cement footprint (Carmeuse release; approximate).",
        "evidence": "documented",
        "source_id": "carmeuse_cbb_20250915",
        "note": "Actor: Carmeuse (Belgian) — allied. Company release 15 Sep 2025: 97.1% stake via public tender. Complements Holcim Pacasmayo / Huaxin Embu building-materials rows.",
    },
    {
        "id": "carmeuse_bio_bio_chile_2025",
        "retrieved": "2026-10-01",
        "source_id": "carmeuse_cbb_20250915",
        "url": "https://www.carmeuse.com/na-en/newsroom/global/carmeuse-announces-acquisition-controlling-stake-cementos-bio-bio",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The Carmeuse Group has acquired a 97.1% stake in the Chilean publicly traded company. The public tender offer was finalized on the 11th of September 2025 ... CBB’s Group has 4 cement facilities in Chile and 1 in Peru",
        "note": "Opened Carmeuse company newsroom page.",
    },
    {
        "id": "carmeuse_cbb_20250915",
        "type": "official",
        "chicago": "Carmeuse Group. “Carmeuse Announces the Acquisition of Controlling Stake in Cementos Bío Bío.” 15 September 2025.",
        "url": "https://www.carmeuse.com/na-en/newsroom/global/carmeuse-announces-acquisition-controlling-stake-cementos-bio-bio",
        "annotation": "Company primary CBB controlling-stake acquisition notice. Supports carmeuse_bio_bio_chile_2025.",
        "supports": ["carmeuse_bio_bio_chile_2025", "hunt_infra_building_materials"],
    },
)

# 9 energy/power_plants_grid — miss (thick; prior Siemens/GE/Hitachi coverage)

# 10 energy/fission_smr — miss (Angra 3 still feasibility/decision pending; no new award)

# 11 infrastructure/port_ownership — APM Lazaro Cardenas Phase II expansion
A(
    {
        "id": "apmt_lazaro_phase2_2025",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "APM Terminals — Lázaro Cárdenas Phase II expansion (Mexico)",
        "country": "Mexico",
        "asset": "Phase II expansion: +65 ha yard; capacity to 2.2m TEU; USD 165 million invested to date (as of Jun 2025); ops targeted 2026",
        "investment_type": "concession",
        "value": "165000000",
        "currency": "USD",
        "value_usd": "165000000",
        "fx_usd": "1",
        "fx_date": "2025-06-03",
        "year": "2025",
        "status": "active",
        "lat": "17.95",
        "lon": "-102.17",
        "geo_note": "Lázaro Cárdenas, Michoacán (APM Terminals release).",
        "evidence": "documented",
        "source_id": "apmt_lazaro_armg_20250603",
        "note": "Actor: APM Terminals (Maersk/Denmark) — allied. Company release 3 Jun 2025: USD 165m invested to date in Phase II; capacity doubling to 2.2m TEU. Complements BTP Santos / DP World Callao ownership rows.",
    },
    {
        "id": "apmt_lazaro_phase2_2025",
        "retrieved": "2026-10-01",
        "source_id": "apmt_lazaro_armg_20250603",
        "url": "https://www.apmterminals.com/en/news/news-releases/2025/250603-six-new-cranes-in-lazaro-cardenas",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "APM Terminals has invested USD 165 million to date in this expansion phase ... Phase II includes expanding the terminal area by 65 hectares, doubling the terminal's capacity to 2.2 million TEUs.",
        "note": "Opened APM Terminals news release.",
    },
    {
        "id": "apmt_lazaro_armg_20250603",
        "type": "official",
        "chicago": "APM Terminals. “Six new electric cranes for APM Terminals Lázaro Cárdenas in Mexico.” 3 June 2025.",
        "url": "https://www.apmterminals.com/en/news/news-releases/2025/250603-six-new-cranes-in-lazaro-cardenas",
        "annotation": "Company primary Lazaro Phase II investment/capacity notice. Supports apmt_lazaro_phase2_2025.",
        "supports": ["apmt_lazaro_phase2_2025", "hunt_infra_port_ownership"],
    },
)

# 12 energy/wind — Vestas Dom Inocêncio 828 MW
A(
    {
        "id": "vestas_dom_inocencio_br_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Vestas / Casa dos Ventos — Dom Inocêncio Wind Complex (Piauí)",
        "country": "Brazil",
        "asset": "828 MW order: 184 × V150-4.5 MW turbines + construction management + 25-year AOM 5000; project investment >BRL 5 billion; COD targeted 2028",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-8.9",
        "lon": "-42.5",
        "geo_note": "South-central Piauí (Vestas release; approximate).",
        "evidence": "documented",
        "source_id": "vestas_dom_inocencio_20251217",
        "note": "Actor: Vestas (Danish) — allied; customer Casa dos Ventos (Brazilian). Company release 17 Dec 2025: 828 MW Dom Inocêncio. Distinct from vestas_casa_dos_ventos_br_2023 (1,310 MW).",
    },
    {
        "id": "vestas_dom_inocencio_br_2025",
        "retrieved": "2026-10-01",
        "source_id": "vestas_dom_inocencio_20251217",
        "url": "https://www.vestas.com/en/media/company-news/2025/casa-dos-ventos-and-vestas-announce-new-partnership-for-c4283083",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Casa dos Ventos ... and Vestas ... announce ... the 828 MW order for the Dom Inocêncio wind complex. ... The project will feature 184 V150-4.5 MW turbines ... The project represents a total investment of over BRL 5 billion",
        "note": "Opened Vestas company news release.",
    },
    {
        "id": "vestas_dom_inocencio_20251217",
        "type": "official",
        "chicago": "Vestas. “Casa dos Ventos and Vestas announce new partnership for the 828 MW Dom Inocêncio Wind Complex in Brazil.” 17 December 2025.",
        "url": "https://www.vestas.com/en/media/company-news/2025/casa-dos-ventos-and-vestas-announce-new-partnership-for-c4283083",
        "annotation": "Company primary Dom Inocêncio wind order. Supports vestas_dom_inocencio_br_2025.",
        "supports": ["vestas_dom_inocencio_br_2025", "hunt_energy_wind"],
    },
)

# 13 energy/other_renewables — miss (San Gabán / Ormat already covered recently)

# 14 infrastructure/port_cranes — ZPMC ARMG for APM Lazaro (thin) + ICTSI CMSA ZPMC RTGs
A(
    {
        "id": "zpmc_apmt_lazaro_armg_2024",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — APM Terminals Lázaro Cárdenas Phase II ARMG / straddle carriers",
        "country": "Mexico",
        "asset": "Agreement for ZPMC to deliver 6 automated RMG (ARMG) cranes + 14 hybrid straddle carriers for APM Lazaro Cardenas Phase II",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "17.95",
        "lon": "-102.17",
        "geo_note": "Lázaro Cárdenas, Michoacán (APM Terminals equipment agreement).",
        "evidence": "documented",
        "source_id": "apmt_equipment_agreements_20240605",
        "note": "Actor: ZPMC (PRC OEM); buyer APM Terminals. Company release 5 Jun 2024 explicitly names ZPMC for Lazaro 6 ARMG + 14 straddles. Complements zpmc_santos_brasil / Itapoa / Lirquén crane rows.",
    },
    {
        "id": "zpmc_apmt_lazaro_armg_2024",
        "retrieved": "2026-10-01",
        "source_id": "apmt_equipment_agreements_20240605",
        "url": "https://www.apmterminals.com/en/news/news-releases/2024/240605-apm-terminals-ramps-up-capacity",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Crane manufacturer ZPMC will deliver ... 6 automated rail mounted gantry cranes and 14, 1-over-1 hybrid straddle carriers for APM Terminals Lazaro in Mexico.",
        "note": "Opened APM Terminals equipment agreements release.",
    },
    {
        "id": "apmt_equipment_agreements_20240605",
        "type": "official",
        "chicago": "APM Terminals. “APM Terminals ramps up capacity with agreements for 240 pieces of container handling equipment.” 5 June 2024.",
        "url": "https://www.apmterminals.com/en/news/news-releases/2024/240605-apm-terminals-ramps-up-capacity",
        "annotation": "Company primary ZPMC Lazaro ARMG/straddle agreement. Supports zpmc_apmt_lazaro_armg_2024.",
        "supports": ["zpmc_apmt_lazaro_armg_2024", "hunt_infra_port_cranes"],
    },
)

A(
    {
        "id": "zpmc_cmsa_manzanillo_rtg_2025",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — Contecon Manzanillo (ICTSI) hybrid RTG delivery",
        "country": "Mexico",
        "asset": "Delivery of three ZPMC hybrid RTG cranes (Oct 2025) for CMSA Phase 3B expansion at Port of Manzanillo",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "19.05",
        "lon": "-104.3",
        "geo_note": "Port of Manzanillo, Colima (ICTSI release).",
        "evidence": "documented",
        "source_id": "ictsi_cmsa_rtg_20251126",
        "note": "Actor: ZPMC (PRC); terminal Contecon Manzanillo / ICTSI (Philippines) — coded prc for OEM supply. ICTSI release 26 Nov 2025 names ZPMC hybrid RTGs. Complements Lazaro ARMG row.",
    },
    {
        "id": "zpmc_cmsa_manzanillo_rtg_2025",
        "retrieved": "2026-10-01",
        "source_id": "ictsi_cmsa_rtg_20251126",
        "url": "https://ictsi.com/news/contecon-manzanillo-adds-hybrid-rtgs-equipment-fleet",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Contecon Manzanillo (CMSA) took delivery of three hybrid rubber-tired gantry (RTG) cranes in October ... Manufactured by ZPMC, the RTG cranes enhance the terminal’s cargo-handling capability",
        "note": "Opened ICTSI company news page.",
    },
    {
        "id": "ictsi_cmsa_rtg_20251126",
        "type": "official",
        "chicago": "International Container Terminal Services, Inc. “Contecon Manzanillo adds hybrid RTGs to equipment fleet.” 26 November 2025.",
        "url": "https://ictsi.com/news/contecon-manzanillo-adds-hybrid-rtgs-equipment-fleet",
        "annotation": "Company primary CMSA ZPMC hybrid RTG delivery. Supports zpmc_cmsa_manzanillo_rtg_2025.",
        "supports": ["zpmc_cmsa_manzanillo_rtg_2025", "hunt_infra_port_cranes"],
    },
)

# 15 infrastructure/rail — Alstom Santiago Metro Line 7
A(
    {
        "id": "alstom_santiago_line7_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "Alstom — Santiago Metro Line 7 Metropolis trains + Urbalis CBTC",
        "country": "Chile",
        "asset": "Contract for 37 five-car Metropolis trains (built at Taubaté, Brazil) + Urbalis CBTC + 20-year maintenance for Metro de Santiago Line 7",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-33.45",
        "lon": "-70.65",
        "geo_note": "Santiago Metro Line 7 corridor (Alstom release).",
        "evidence": "documented",
        "source_id": "alstom_line7_20250716",
        "note": "Actor: Alstom (French) — allied. Company release 16 Jul 2025: first carbody shell completed; 37 trains + CBTC + 20-year maintenance. Complements Alstom Mexico DMU / CRRC Chile EFE rows.",
    },
    {
        "id": "alstom_santiago_line7_2025",
        "retrieved": "2026-10-01",
        "source_id": "alstom_line7_20250716",
        "url": "https://www.alstom.com/press-releases-news/2025/7/alstom-completes-production-first-train-carbody-shell-santiago-metro-line-7",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "A total of 37 trains, each with five cars, will be produced at Alstom’s facility in Taubaté. These trains are part of a contract between Alstom and Metro de Santiago, which includes the supply of the Urbalis CBTC signalling system, a maintenance contract that spans 20 years, 37 Metropolis trains",
        "note": "Opened Alstom press release.",
    },
    {
        "id": "alstom_line7_20250716",
        "type": "official",
        "chicago": "Alstom. “Alstom completes production of the first train carbody shell for Santiago Metro Line 7.” 16 July 2025.",
        "url": "https://www.alstom.com/press-releases-news/2025/7/alstom-completes-production-first-train-carbody-shell-santiago-metro-line-7",
        "annotation": "Company primary Line 7 train/CBTC contract milestone. Supports alstom_santiago_line7_2025.",
        "supports": ["alstom_santiago_line7_2025", "hunt_latam_rail_telecom"],
    },
)

# 16 resources/water — miss (Chile/Mexico desal already thick; Fortaleza Abengoa PPP not opened as primary)

# 17 resources/nickel — Vale Onça Puma Furnace 2 (thin)
A(
    {
        "id": "vale_onca_puma_furnace2_2025",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "other",
        "counterpart": "Vale Base Metals — Onça Puma Furnace 2 ferronickel expansion (Pará)",
        "country": "Brazil",
        "asset": "Furnace 2 start-up Sep 2025 adding 15 ktpy Ni; site nameplate to 40 ktpa; project delivered ~13% under budget (final CAPEX ~USD 480m per Vale 3Q25)",
        "investment_type": "ownership_equity",
        "value": "480000000",
        "currency": "USD",
        "value_usd": "480000000",
        "fx_usd": "1",
        "fx_date": "2025-09-30",
        "year": "2025",
        "status": "active",
        "lat": "-6.5",
        "lon": "-51.2",
        "geo_note": "Onça Puma complex, southeastern Pará (Vale release; approximate).",
        "evidence": "documented",
        "source_id": "vale_onca_puma_furnace2_20250930",
        "note": "Actor: Vale Base Metals / Vale S.A. (Brazilian) — other. Company release 30 Sep 2025: Furnace 2 start-up; +15 ktpy to 40 ktpa. Vale 3Q25 financials cite ~USD 480m final CAPEX. Distinct from MMG/Anglo / Centaurus nickel rows.",
    },
    {
        "id": "vale_onca_puma_furnace2_2025",
        "retrieved": "2026-10-01",
        "source_id": "vale_onca_puma_furnace2_20250930",
        "url": "https://vale.com/w/vale-base-metals-announces-start-up-of-furnace-2-at-onca-puma-1",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Vale Base Metals today began operating the second nickel processing furnace (Furnace 2) at the Onça Puma Mining Complex in southeastern Pará, Brazil ... adding 15 kilotons of nickel production capacity, bringing the operation to a nameplate production capacity of 40 ktpa. The company completed the project on schedule and nearly 13 per cent below budget.",
        "note": "Opened Vale Base Metals company release; CAPEX cross-checked to Vale 3Q25 financials (USD 480m).",
    },
    {
        "id": "vale_onca_puma_furnace2_20250930",
        "type": "official",
        "chicago": "Vale Base Metals. “Vale Base Metals Announces Start-Up of Furnace 2 at Onça Puma.” 30 September 2025.",
        "url": "https://vale.com/w/vale-base-metals-announces-start-up-of-furnace-2-at-onca-puma-1",
        "annotation": "Company primary Onça Puma Furnace 2 start-up. Supports vale_onca_puma_furnace2_2025.",
        "supports": ["vale_onca_puma_furnace2_2025", "hunt_res_nickel"],
    },
)

# 18 resources/copper — Anglo American Quellaveco Peru
A(
    {
        "id": "anglo_quellaveco_peru",
        "layer": "resources",
        "subcategory": "copper",
        "side": "allied",
        "counterpart": "Anglo American (60%) / Mitsubishi (40%) — Quellaveco copper mine (Moquegua)",
        "country": "Peru",
        "asset": "Quellaveco open-pit copper mine — commercial ops from 2022; ~300 ktpa Cu average first 10 years; ~USD 5.5bn construction capex (incl. COVID costs)",
        "investment_type": "ownership_equity",
        "value": "5500000000",
        "currency": "USD",
        "value_usd": "5500000000",
        "fx_usd": "1",
        "fx_date": "2022-09-26",
        "year": "2022",
        "status": "active",
        "lat": "-17.1",
        "lon": "-70.85",
        "geo_note": "Moquegua Region, southern Peru (Anglo American).",
        "evidence": "documented",
        "source_id": "anglo_quellaveco_20220926",
        "note": "Actor: Anglo American (UK) 60% / Mitsubishi 40% — allied. Company release 26 Sep 2022: commercial copper ops start; USD 5.5bn total capex. Complements Chinalco / MMG / FCX / Southern Copper Peru copper rows. Observation year = commercial start.",
    },
    {
        "id": "anglo_quellaveco_peru",
        "retrieved": "2026-10-01",
        "source_id": "anglo_quellaveco_20220926",
        "url": "https://www.angloamerican.com/media/press-releases/2022/26-09-2022",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "Anglo American plc ... announces the start of commercial copper operations at its Quellaveco project in Peru ... Quellaveco is expected to produce 300,000 tonnes per year of copper equivalent volume on average over its first ten years. ... estimated total capex of $5.5 billion",
        "note": "Opened Anglo American press release.",
    },
    {
        "id": "anglo_quellaveco_20220926",
        "type": "official",
        "chicago": "Anglo American. “Anglo American to begin copper shipments from Quellaveco.” 26 September 2022.",
        "url": "https://www.angloamerican.com/media/press-releases/2022/26-09-2022",
        "annotation": "Company primary Quellaveco commercial start notice. Supports anglo_quellaveco_peru.",
        "supports": ["anglo_quellaveco_peru", "hunt_res_copper"],
    },
)


def blank_row():
    return {k: "" for k in FIELDS}


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}

    added = []
    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = blank_row()
        full.update(row)
        for k in FIELDS:
            full.setdefault(k, "")
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
        "hunt_res_graphite": "Cycle 5: equal budget; no distinct new graphite mine/anode actor beyond South Star/Graphcoa/Nacional/Graphex (miss).",
        "hunt_res_balsa": "Cycle 5: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_infra_engineering_epc": "Cycle 5: logged worley_rincon_lithium_epc_2025.",
        "hunt_fenb_araxa": "Cycle 5: logged cbmm_araxa_capex_plan_2025 (UNVERIFIED proxy).",
        "hunt_infra_bridges_roads": "Cycle 5: equal budget; no new highway/bridge award beyond prior CHEC/CRCC/CRBC (miss).",
        "hunt_energy_solar": "Cycle 5: logged atlas_vista_alegre_solar_br_2025.",
        "hunt_res_lithium": "Cycle 5: logged eramet_centenario_phase1_2024.",
        "hunt_infra_building_materials": "Cycle 5: logged carmeuse_bio_bio_chile_2025.",
        "hunt_br_power_equip": "Cycle 5: equal budget; no new grid award beyond prior Siemens/GE/Hitachi (miss).",
        "hunt_energy_fission_smr": "Cycle 5: equal budget; Angra 3 still decision/feasibility — no new SMR award (miss).",
        "hunt_infra_port_ownership": "Cycle 5: logged apmt_lazaro_phase2_2025.",
        "hunt_energy_wind": "Cycle 5: logged vestas_dom_inocencio_br_2025.",
        "hunt_energy_other_renewables": "Cycle 5: equal budget; no new geothermal/small-hydro beyond San Gabán/Ormat (miss).",
        "hunt_infra_port_cranes": "Cycle 5: logged zpmc_apmt_lazaro_armg_2024 + zpmc_cmsa_manzanillo_rtg_2025.",
        "hunt_latam_rail_telecom": "Cycle 5: logged alstom_santiago_line7_2025.",
        "hunt_res_water": "Cycle 5: equal budget; no new desal primary beyond Acciona/IDE/Bechtel set (miss).",
        "hunt_res_nickel": "Cycle 5: logged vale_onca_puma_furnace2_2025.",
        "hunt_res_copper": "Cycle 5: logged anglo_quellaveco_peru.",
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
    print("Cycle 5 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
