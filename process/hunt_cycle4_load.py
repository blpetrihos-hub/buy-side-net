#!/usr/bin/env python3
"""Cycle 4 hunt: shuffle_seed=20261004; equal budget across 18 subcategories."""
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


# seed 20261004 order:
# solar, other_renewables, port_ownership, power_plants_grid, water, fission_smr,
# balsa, wind, lithium, rail, graphite, bridges_roads, copper, building_materials,
# niobium, nickel, port_cranes, engineering_epc

# 1 energy/solar — SPIC/Recurrent Marangatu (PRC majority equity)
A(
    {
        "id": "spic_recurrent_marangatu_br_2024",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "SPIC Brasil (70%) / Recurrent Energy (30%) — Marangatu Solar Complex, Piauí",
        "country": "Brazil",
        "asset": "446 MWp / 360 MWac Marangatu Solar Complex inaugurated Jun 2024 (SPIC majority ownership)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-4.13",
        "lon": "-41.78",
        "geo_note": "Brasileira, Piauí (company release).",
        "evidence": "documented",
        "source_id": "prnewswire_marangatu_20240610",
        "note": "Actor: SPIC Brasil (PRC state-linked) majority 70%; Recurrent Energy / Canadian Solar 30% — coded prc for majority equity. Company PRNewswire release 10 Jun 2024: fully energized Apr 2024 after 14 months construction. Complements recurrent_ciranda_solar_br_2023.",
    },
    {
        "id": "spic_recurrent_marangatu_br_2024",
        "retrieved": "2026-10-01",
        "source_id": "prnewswire_marangatu_20240610",
        "url": "https://www.prnewswire.com/news-releases/recurrent-energy-and-spic-inaugurate-446-mwp-solar-complex-in-brazil-302167837.html",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Recurrent Energy, a subsidiary of Canadian Solar Inc. ... announced today the inauguration of the 446 MWp / 360 MWac Marangatu Solar Complex in Brasileira, Brazil. SPIC owns 70% of the project, while Recurrent Energy owns the remaining 30%.",
        "note": "Opened PRNewswire Canadian Solar / Recurrent Energy release.",
    },
    {
        "id": "prnewswire_marangatu_20240610",
        "type": "official",
        "chicago": "Canadian Solar Inc. / Recurrent Energy. “Recurrent Energy and SPIC Inaugurate 446 MWp Solar Complex in Brazil.” PR Newswire, 10 June 2024.",
        "url": "https://www.prnewswire.com/news-releases/recurrent-energy-and-spic-inaugurate-446-mwp-solar-complex-in-brazil-302167837.html",
        "annotation": "Company primary inauguration notice for Marangatu SPIC/Recurrent Brazil. Supports spic_recurrent_marangatu_br_2024.",
        "supports": ["spic_recurrent_marangatu_br_2024", "hunt_energy_solar"],
    },
)

# 2 energy/other_renewables — POWERCHINA San Gabán III Peru hydro commercial operation
A(
    {
        "id": "powerchina_san_gaban_iii_peru_2025",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "POWERCHINA (Hydroelectric Bureau 6) — San Gabán III hydropower plant, Puno",
        "country": "Peru",
        "asset": "San Gabán III hydropower station — 209.3 MW nominal; full commercial generation reported May 2025",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-13.45",
        "lon": "-70.4",
        "geo_note": "San Gabán district, Carabaya, Puno (Osinergmin / POWERCHINA).",
        "evidence": "documented",
        "source_id": "powerchina_6j_sangaban_20250527",
        "note": "Actor: POWERCHINA Hydroelectric Bureau 6 (PRC) construction contractor. Company page 27 May 2025: owner thank-you for San Gabán III full commercial generation. Osinergmin 30 May 2025 confirms 209.3 MW commercial operation. Complements powerchina_chucas_cr_ref.",
    },
    {
        "id": "powerchina_san_gaban_iii_peru_2025",
        "retrieved": "2026-10-01",
        "source_id": "powerchina_6j_sangaban_20250527",
        "url": "http://6j.powerchina.cn/col/col4463/art/2025/art_28b686f9144945ee879752c8e5a67f57.html",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "近日，公司收到秘鲁圣加旺项目业主感谢信，信中就秘鲁圣加旺III水电站顺利实现全面投产发电目标对水电六局及施工团队致以衷心的感谢和崇高的敬意。",
        "note": "Opened POWERCHINA Bureau 6 Chinese news page; Osinergmin confirms 209.3 MW COD.",
    },
    {
        "id": "powerchina_6j_sangaban_20250527",
        "type": "official",
        "chicago": "中国电建水电六局 (POWERCHINA Hydroelectric Bureau 6). “【制造安装公司】公司收到秘鲁圣加旺项目业主感谢信.” 27 May 2025.",
        "url": "http://6j.powerchina.cn/col/col4463/art/2025/art_28b686f9144945ee879752c8e5a67f57.html",
        "annotation": "Company primary notice of San Gabán III Peru full commercial generation. Supports powerchina_san_gaban_iii_peru_2025.",
        "supports": ["powerchina_san_gaban_iii_peru_2025", "hunt_energy_other_renewables"],
    },
)

# 3 infrastructure/port_ownership — DP World Callao Bicentennial Pier
A(
    {
        "id": "dpworld_callao_bicentennial_2024",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "DP World — Port of Callao South Terminal Bicentennial Pier expansion",
        "country": "Peru",
        "asset": "Completed USD 400 million Callao South Terminal expansion; pier 650→1,050 m; capacity 1.5→2.7m TEU/year",
        "investment_type": "concession",
        "value": "400000000",
        "currency": "USD",
        "value_usd": "400000000",
        "fx_usd": "1",
        "fx_date": "2024-06-21",
        "year": "2024",
        "status": "active",
        "lat": "-12.05",
        "lon": "-77.15",
        "geo_note": "Port of Callao South Terminal, Peru (DP World release).",
        "evidence": "documented",
        "source_id": "dpworld_callao_20240621",
        "note": "Actor: DP World (UAE) — allied. Company release 21 Jun 2024: USD 400m Bicentennial Pier expansion completed; also 15 electric cranes + 20 electric ITVs (OEM not named on page).",
    },
    {
        "id": "dpworld_callao_bicentennial_2024",
        "retrieved": "2026-10-01",
        "source_id": "dpworld_callao_20240621",
        "url": "https://www.dpworld.com/en/news/peruvian-trade-set-for-boost-as-dp-world-completes-400m-callao-port-expansion",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "DP World has completed a major $400 million expansion project at the Port of Callao in Peru, boosting container handling capacity at the South Terminal by 80% ... The project increases handling capacity from 1.5 million TEUs ... to 2.7 million TEUs",
        "note": "Opened DP World company news release.",
    },
    {
        "id": "dpworld_callao_20240621",
        "type": "official",
        "chicago": "DP World. “Peruvian Trade Set for Boost as DP World Completes $400m Callao Port Expansion.” 21 June 2024.",
        "url": "https://www.dpworld.com/en/news/peruvian-trade-set-for-boost-as-dp-world-completes-400m-callao-port-expansion",
        "annotation": "Company primary Callao South Terminal expansion completion notice. Supports dpworld_callao_bicentennial_2024.",
        "supports": ["dpworld_callao_bicentennial_2024", "hunt_infra_port_ownership"],
    },
)

# 4 energy/power_plants_grid — budget miss (already thick; Siemens Eletrobras / GE Vernova / Hitachi already logged)

# 5 resources/water — ACCIONA Los Cabos desalination PPP Mexico
A(
    {
        "id": "acciona_los_cabos_desal_mexico",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "ACCIONA Agua / La Peninsular — Los Cabos SWRO desalination plant (Baja California Sur)",
        "country": "Mexico",
        "asset": "Los Cabos seawater RO desalination plant — 250 l/s (~21,600 m³/day); design/finance/build + 25-year O&M PPP; budget €134.5m",
        "investment_type": "concession",
        "value": "134500000",
        "currency": "EUR",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2021",
        "status": "active",
        "lat": "22.89",
        "lon": "-109.91",
        "geo_note": "Los Cabos municipality, Baja California Sur (ACCIONA project page).",
        "evidence": "documented",
        "source_id": "acciona_los_cabos_desal_page",
        "note": "Actor: ACCIONA (Spanish) — allied. Company project/news pages: €134.5m PPP; 250 l/s; 25-year O&M. FY2024 results list concession window 2023–2048 / €79m equity method investment. Value stored as EUR budget on page (no FX conversion applied). Complements Chile desal rows.",
    },
    {
        "id": "acciona_los_cabos_desal_mexico",
        "retrieved": "2026-10-01",
        "source_id": "acciona_los_cabos_desal_page",
        "url": "https://www.acciona.com/updates/news/acciona-build-operate-cabos-desalination-plant-mexico",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "ACCIONA will build and operate a desalination plant in the municipality of Los Cabos, in Baja California (Mexico). The project has an overall budget of €134.5 million. ... capacity of 250 liters per second ... operation, conservation and maintenance for a period of 25 years, through a public-private partnership scheme.",
        "note": "Opened ACCIONA news page for Los Cabos desal.",
    },
    {
        "id": "acciona_los_cabos_desal_page",
        "type": "official",
        "chicago": "ACCIONA. “ACCIONA to build and operate Los Cabos desalination plant in Mexico.” Company news release.",
        "url": "https://www.acciona.com/updates/news/acciona-build-operate-cabos-desalination-plant-mexico",
        "annotation": "Company primary Los Cabos desalination PPP notice. Supports acciona_los_cabos_desal_mexico.",
        "supports": ["acciona_los_cabos_desal_mexico", "hunt_res_water"],
    },
)

# 6 energy/fission_smr — Meitner ACR-300 Atucha proposal (thin; UNVERIFIED proposal)
A(
    {
        "id": "meitner_acr300_atucha_2026",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "us",
        "counterpart": "Meitner Energy — proposed ACR-300 SMR at Atucha (INVAP design; US private capital)",
        "country": "Argentina",
        "asset": "Proposed privately financed 300 MWe ACR-300 Generation III+ PWR SMR at Atucha; announced investment ~USD 1.2 billion (proposal / pre-license)",
        "investment_type": "other",
        "value": "1200000000",
        "currency": "USD",
        "value_usd": "1200000000",
        "fx_usd": "1",
        "fx_date": "2026-07-10",
        "year": "2026",
        "status": "active",
        "lat": "-33.97",
        "lon": "-59.21",
        "geo_note": "Atucha nuclear complex, Lima / Zárate, Buenos Aires Province (WNN / NEI).",
        "evidence": "proxy",
        "source_id": "wnn_meitner_acr300_20260710",
        "note": "Actor: Meitner Energy (US-incorporated; Ansari Group / INVAP Black River Technology JV) — coded us for US private capital presentation. UNVERIFIED proxy: press reports of Economy Ministry announcement of a USD 1.2bn proposal; ARN licensing and construction not started. Complements carem25 / cnnc_atucha rows.",
    },
    {
        "id": "meitner_acr300_atucha_2026",
        "retrieved": "2026-10-01",
        "source_id": "wnn_meitner_acr300_20260710",
        "url": "https://www.world-nuclear-news.org/articles/argentina-announces-privately-financed-smr-plan",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Argentina's government has said US-based Meitner Energy is planning to invest USD1.2 billion in the construction of a 300 MW small modular reactor at the Atucha site. ... The project will have an estimated investment of USD1.2 billion and will be funded through US private capital based on an Argentine patent.",
        "note": "Opened World Nuclear News page summarizing Caputo / Meitner announcement.",
    },
    {
        "id": "wnn_meitner_acr300_20260710",
        "type": "journalism",
        "chicago": "World Nuclear News. “Argentina announces privately-financed SMR plan.” 10 July 2026.",
        "url": "https://www.world-nuclear-news.org/articles/argentina-announces-privately-financed-smr-plan",
        "annotation": "Industry journalism on Meitner ACR-300 Atucha proposal. Supports meitner_acr300_atucha_2026 (UNVERIFIED proxy).",
        "supports": ["meitner_acr300_atucha_2026", "hunt_energy_fission_smr"],
    },
)

# 7 resources/balsa — budget miss (already thick WITS 2022–2024 pairs)

# 8 energy/wind — Goldwind SPIC Touros Brazil (local supply)
A(
    {
        "id": "goldwind_spic_touros_br_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "prc",
        "counterpart": "Goldwind — SPIC Brasil Touros-area wind farms (Rio Grande do Norte)",
        "country": "Brazil",
        "asset": "Supply of 17 × GWH182-6.2 MW turbines (~105.4 MW) + up to 30-year O&M for SPIC Brasil RN wind farms; first locally supplied Brazil project",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-5.2",
        "lon": "-35.55",
        "geo_note": "Touros / Rio Grande do Norte (Goldwind release).",
        "evidence": "documented",
        "source_id": "goldwind_brazil_spic_20250123",
        "note": "Actor: Goldwind (PRC). Company English news 23 Jan 2025: contract with SPIC Brasil for 17 GWH182-6.2MW units in RN; Camaçari Bahia local manufacturing; FINAME/BNDES certified. Complements goldwind_pemuco_chile.",
    },
    {
        "id": "goldwind_spic_touros_br_2025",
        "retrieved": "2026-10-01",
        "source_id": "goldwind_brazil_spic_20250123",
        "url": "https://www.goldwind.com/en/news/focus-1116679091689538560",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Recently, Goldwind successfully signed a contract with SPIC Brasil to supply 17 units of GWH182-6.2MW wind turbines for two new wind farms in Rio Grande do Norte state in northeastern Brazil, along with providing operation and maintenance services for up to 30 years. This marks Goldwind’s first locally supplied project in Brazil",
        "note": "Opened Goldwind English company news page.",
    },
    {
        "id": "goldwind_brazil_spic_20250123",
        "type": "official",
        "chicago": "Goldwind. “Goldwind Writes New Chapter in Brazil.” 23 January 2025.",
        "url": "https://www.goldwind.com/en/news/focus-1116679091689538560",
        "annotation": "Company primary SPIC Brasil GWH182 turbine supply notice. Supports goldwind_spic_touros_br_2025.",
        "supports": ["goldwind_spic_touros_br_2025", "hunt_energy_wind"],
    },
)

# 9 resources/lithium — Rio Tinto Rincon USD 2.5bn expansion
A(
    {
        "id": "rio_tinto_rincon_expansion_2024",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "Rio Tinto — Rincon lithium project expansion (Salta)",
        "country": "Argentina",
        "asset": "Board-approved USD 2.5 billion expansion to 60,000 tpy battery-grade Li2CO3 (3kt starter + 57kt expansion); first production targeted 2028",
        "investment_type": "ownership_equity",
        "value": "2500000000",
        "currency": "USD",
        "value_usd": "2500000000",
        "fx_usd": "1",
        "fx_date": "2024-12-12",
        "year": "2024",
        "status": "active",
        "lat": "-24.1",
        "lon": "-66.95",
        "geo_note": "Salar de Rincón, Salta Province (Rio Tinto release).",
        "evidence": "documented",
        "source_id": "riotinto_rincon_20241212",
        "note": "Actor: Rio Tinto (UK/Australia) — allied. Company release 12 Dec 2024: USD 2.5bn approved for Rincon expansion to 60ktpa; DLE technology; ~40-year mine life. Complements Ganfeng / NovaAndino lithium rows.",
    },
    {
        "id": "rio_tinto_rincon_expansion_2024",
        "retrieved": "2026-10-01",
        "source_id": "riotinto_rincon_20241212",
        "url": "https://www.riotinto.com/en/news/releases/2024/rio-tinto-to-invest-2_5-billion-to-expand-rincon-lithium-project-capacity-to-60000-tonnes-per-year",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Rio Tinto has approved $2.5 billion to expand the Rincon project in Argentina, the company’s first commercial scale lithium operation ... Rincon's capacity of 60,000 tonnes of battery grade lithium carbonate per year is comprised of the 3,000-tonne starter plant and 57,000-tonne expansion plant.",
        "note": "Opened Rio Tinto company news release.",
    },
    {
        "id": "riotinto_rincon_20241212",
        "type": "official",
        "chicago": "Rio Tinto. “Rio Tinto to invest $2.5 billion to expand Rincon lithium project capacity to 60,000 tonnes per year.” 12 December 2024.",
        "url": "https://www.riotinto.com/en/news/releases/2024/rio-tinto-to-invest-2_5-billion-to-expand-rincon-lithium-project-capacity-to-60000-tonnes-per-year",
        "annotation": "Company primary Rincon expansion investment approval. Supports rio_tinto_rincon_expansion_2024.",
        "supports": ["rio_tinto_rincon_expansion_2024", "hunt_res_lithium"],
    },
)

# 10 infrastructure/rail — Siemens Mobility SP Line 4-Yellow CBTC extension
A(
    {
        "id": "siemens_sp_line4_cbtc_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "Siemens Mobility — São Paulo Metro Line 4-Yellow extension signaling (Motiva)",
        "country": "Brazil",
        "asset": "CBTC Trainguard MT + interlocking/telecom/GoA4 for 3.3 km Line 4 extension Vila Sônia–Taboão da Serra; equip 6 trains",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.6",
        "lon": "-46.75",
        "geo_note": "São Paulo Line 4-Yellow western extension (Siemens release).",
        "evidence": "documented",
        "source_id": "siemens_line4_20260715",
        "note": "Actor: Siemens Mobility (German) — allied; customer Motiva. Company release 15 Jul 2026: CBTC/GoA4 package for Line 4 extension. Complements CRRC/Alstom rolling-stock rows.",
    },
    {
        "id": "siemens_sp_line4_cbtc_2026",
        "retrieved": "2026-10-01",
        "source_id": "siemens_line4_20260715",
        "url": "https://press.siemens.com/global/en/pressrelease/siemens-digitalize-sao-paulos-metro-line-4-yellow-extension",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Siemens Mobility has been selected by Motiva to equip São Paulo’s transformative Line 4-Yellow ... with latest signaling technology. ... Siemens Mobility will deliver a comprehensive signaling portfolio, including its CBTC system Trainguard MT, electronic interlocking, telecommunications, operational supervision, and GoA4.",
        "note": "Opened Siemens Mobility press release.",
    },
    {
        "id": "siemens_line4_20260715",
        "type": "official",
        "chicago": "Siemens Mobility. “Siemens to Digitalize São Paulo’s Metro Line 4-Yellow Extension.” 15 July 2026.",
        "url": "https://press.siemens.com/global/en/pressrelease/siemens-digitalize-sao-paulos-metro-line-4-yellow-extension",
        "annotation": "Company primary Line 4-Yellow CBTC award notice. Supports siemens_sp_line4_cbtc_2026.",
        "supports": ["siemens_sp_line4_cbtc_2026", "hunt_latam_rail_telecom"],
    },
)

# Also CRRC Salvador metro (cycle-3 miss preference)
A(
    {
        "id": "crrc_salvador_metro_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "prc",
        "counterpart": "CRRC Changchun / CRRC Brasil — Salvador metro Lines 1–2 trainsets",
        "country": "Brazil",
        "asset": "Selected consortium to supply 10 four-car metro trainsets for Salvador; contract value R$490.4 million (beat Alstom R$614.4m)",
        "investment_type": "equipment_supply",
        "value": "490400000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-12.97",
        "lon": "-38.51",
        "geo_note": "Salvador, Bahia metro (Railway Gazette).",
        "evidence": "proxy",
        "source_id": "railwaygazette_salvador_crrc_20260717",
        "note": "Actor: CRRC Changchun + CRRC Brasil (PRC). UNVERIFIED proxy: Railway Gazette 17 Jul 2026 reports Bahia selection at R$490.4m pending standstill/signing. Value stored as BRL (no FX). Complements sp_metro_crrc_alstom_2024.",
    },
    {
        "id": "crrc_salvador_metro_2026",
        "retrieved": "2026-10-01",
        "source_id": "railwaygazette_salvador_crrc_20260717",
        "url": "https://www.railwaygazette.com/metro-metro-categories/2026/07/17/crrc-wins-salvador-metro-train-order/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "The Bahia state government has selected a consortium of CRRC Changchun Railway Vehicles and CRRC Brasil Equipamentos Ferroviários to supply 10 four-car metro trainsets for use in the city of Salvador. The contract has a value of R$490.4m ... CRRC’s bid beat rival Alstom’s R$614.4m offer.",
        "note": "Opened Railway Gazette article (non-paywalled).",
    },
    {
        "id": "railwaygazette_salvador_crrc_20260717",
        "type": "journalism",
        "chicago": "Railway Gazette International. “CRRC wins Salvador metro train order.” 17 July 2026.",
        "url": "https://www.railwaygazette.com/metro-metro-categories/2026/07/17/crrc-wins-salvador-metro-train-order/",
        "annotation": "Industry journalism on CRRC Salvador metro award. Supports crrc_salvador_metro_2026 (UNVERIFIED proxy pending contract signature).",
        "supports": ["crrc_salvador_metro_2026", "hunt_latam_rail_telecom"],
    },
)

# 11 resources/graphite — Graphcoa Boa Sorte / Appian Bahia
A(
    {
        "id": "graphcoa_boa_sorte_bahia_2024",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "Graphcoa (Appian Capital Advisory) — Boa Sorte integrated graphite mine/plant, Itagimirim (Bahia)",
        "country": "Brazil",
        "asset": "Boa Sorte mine + concentration plant began operations Dec 2024; ramp to 5,500 tpy by Aug 2025; Phase 1 investment R$350 million",
        "investment_type": "ownership_equity",
        "value": "350000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-16.0",
        "lon": "-40.0",
        "geo_note": "Itagimirim, southern Bahia (Appian / Graphcoa interview).",
        "evidence": "documented",
        "source_id": "appian_graphcoa_20250409",
        "note": "Actor: Graphcoa backed by Appian Capital Advisory (UK PE) — allied. Appian site 9 Apr 2025 republishing Minera Brasil interview: ops started Dec 2024; R$350m Phase 1; target 5,500 tpy. Complements South Star / Nacional de Grafite / Graphex rows.",
    },
    {
        "id": "graphcoa_boa_sorte_bahia_2024",
        "retrieved": "2026-10-01",
        "source_id": "appian_graphcoa_20250409",
        "url": "https://appiancapitaladvisory.com/graphcoas-new-graphite-plant-boosts-energy-transition-in-brazil/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "in December 2024, Graphcoa began operations at its first integrated graphite production facility in Itagimirim, southern Bahia. ... In this first phase, R$ 350 million was invested to implement the Boa Sorte mine in Itagimirim, southern Bahia.",
        "note": "Opened Appian Capital Advisory page (Minera Brasil interview reprint).",
    },
    {
        "id": "appian_graphcoa_20250409",
        "type": "official",
        "chicago": "Appian Capital Advisory / Minera Brasil. “Graphcoa’s new graphite plant boosts energy transition in Brazil.” 9 April 2025.",
        "url": "https://appiancapitaladvisory.com/graphcoas-new-graphite-plant-boosts-energy-transition-in-brazil/",
        "annotation": "Investor/company interview on Graphcoa Boa Sorte graphite start-up. Supports graphcoa_boa_sorte_bahia_2024.",
        "supports": ["graphcoa_boa_sorte_bahia_2024", "hunt_res_graphite"],
    },
)

# 12 infrastructure/bridges_roads — CRBC Ecuador Quinindé-area highway (opened Nov 2023)
A(
    {
        "id": "crbc_ecuador_quininde_highway_2023",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "China Road and Bridge Corporation (CRBC) — ~40 km post-earthquake reconstruction highway (Esmeraldas / Imbabura / Pichincha)",
        "country": "Ecuador",
        "asset": "Approx. 40 km, 16 m-wide highway built by CRBC; started late 2018; opened November 2023 (post-2016 earthquake reconstruction)",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "0.34",
        "lon": "-79.47",
        "geo_note": "Quinindé / Esmeraldas corridor (People’s Daily / Guangdong commerce reprint).",
        "evidence": "proxy",
        "source_id": "people_daily_crbc_ecuador_20250218",
        "note": "Actor: China Road and Bridge (PRC). UNVERIFIED proxy: People’s Daily feature (via Guangdong commerce portal) 18 Feb 2025 describing CRBC-built ~40 km highway opened Nov 2023. No contract USD on page. Complements Jamaica CHEC / Guyana CRCC rows.",
    },
    {
        "id": "crbc_ecuador_quininde_highway_2023",
        "retrieved": "2026-10-01",
        "source_id": "people_daily_crbc_ecuador_20250218",
        "url": "https://com.gd.gov.cn/zcqggfwpt/tzjy/content/post_4669445.html",
        "price_year": "2023",
        "evidence": "proxy",
        "quote": "公路由中国路桥工程有限责任公司承建，2018年底正式开工，2023年11月竣工通车。",
        "note": "Opened Guangdong commerce reprint of People’s Daily Ecuador highway feature.",
    },
    {
        "id": "people_daily_crbc_ecuador_20250218",
        "type": "journalism",
        "chicago": "人民日报 (People’s Daily), via Guangdong Department of Commerce. “中企承建厄瓜多尔公路项目惠及超10万民众.” 18 February 2025.",
        "url": "https://com.gd.gov.cn/zcqggfwpt/tzjy/content/post_4669445.html",
        "annotation": "State journalism on CRBC Ecuador highway completion. Supports crbc_ecuador_quininde_highway_2023 (UNVERIFIED proxy).",
        "supports": ["crbc_ecuador_quininde_highway_2023", "hunt_infra_bridges_roads"],
    },
)

# 13 resources/copper — Southern Copper Tía María construction progress
A(
    {
        "id": "southern_copper_tia_maria_2025",
        "layer": "resources",
        "subcategory": "copper",
        "side": "other",
        "counterpart": "Southern Copper (Grupo México) — Tía María SX-EW copper project, Arequipa",
        "country": "Peru",
        "asset": "Tía María greenfield SX-EW project — 120,000 tpy cathode design; USD 1.80bn budget; 24% progress / USD 790m committed end-2025; ops targeted 2027",
        "investment_type": "ownership_equity",
        "value": "1800000000",
        "currency": "USD",
        "value_usd": "1800000000",
        "fx_usd": "1",
        "fx_date": "2025-12-31",
        "year": "2025",
        "status": "active",
        "lat": "-17.0",
        "lon": "-71.85",
        "geo_note": "Islay province, Arequipa (Grupo México 4Q25 report).",
        "evidence": "documented",
        "source_id": "gmexico_4q25_tia_maria",
        "note": "Actor: Southern Copper / Grupo México (Mexican) — other. Company 4Q25 English report: USD 1.80bn budget; USD 790m committed; 24% progress at end-2025; 120ktpa SX-EW. Complements Chinalco / MMG / FCX Peru copper rows.",
    },
    {
        "id": "southern_copper_tia_maria_2025",
        "retrieved": "2026-10-01",
        "source_id": "gmexico_4q25_tia_maria",
        "url": "https://www.gmexico.com/GMDocs/Home/Eng/4th_Quarter_2025_Report.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Tia Maria - Arequipa.- This greenfield project in Arequipa, Peru will use state-of-the- art SX-EW technology ... capacity to produce 120,000 tonnes of SX EW copper cathodes per year. ... The project budget has been set at $1.80 billion. ... As at December 31, 2025, the company had committed $790 million ... progress at Tia Maria stood at 24%",
        "note": "Opened Grupo México 4Q25 English directors report PDF.",
    },
    {
        "id": "gmexico_4q25_tia_maria",
        "type": "official",
        "chicago": "Grupo México. “Fourth Quarter 2025 Report” (English). Tía María project update. 2025.",
        "url": "https://www.gmexico.com/GMDocs/Home/Eng/4th_Quarter_2025_Report.pdf",
        "annotation": "Company primary Tía María construction/budget update. Supports southern_copper_tia_maria_2025.",
        "supports": ["southern_copper_tia_maria_2025", "hunt_res_copper"],
    },
)

# 14 infrastructure/building_materials — Holcim Pacasmayo majority stake (thin)
A(
    {
        "id": "holcim_pacasmayo_peru_2025",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Holcim — majority stake acquisition of Cementos Pacasmayo (Peru)",
        "country": "Peru",
        "asset": "Agreed acquisition of majority stake in Cementos Pacasmayo (~5 Mtpy cement + 28 ready-mix/precast plants); ~USD 1.5bn EV on 100% basis; expected close H1 2026",
        "investment_type": "ownership_equity",
        "value": "1500000000",
        "currency": "USD",
        "value_usd": "1500000000",
        "fx_usd": "1",
        "fx_date": "2025-12-16",
        "year": "2025",
        "status": "active",
        "lat": "-7.4",
        "lon": "-79.55",
        "geo_note": "Pacasmayo cement operations, northern Peru (Holcim release; approximate).",
        "evidence": "documented",
        "source_id": "holcim_pacasmayo_20251216",
        "note": "Actor: Holcim (Swiss) — allied. Company release: majority stake; ~USD 1.5bn transaction value on 100% basis; subject to customary conditions/regulatory approval; expected close H1 2026. Complements Huaxin Embu / Sinoma Z02 Brazil building-materials rows.",
    },
    {
        "id": "holcim_pacasmayo_peru_2025",
        "retrieved": "2026-10-01",
        "source_id": "holcim_pacasmayo_20251216",
        "url": "https://www.holcim.com/media/media-releases/holcim-to-acquire-majority-stake-cementos-pacasmayo",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Holcim is acquiring a majority stake in Cementos Pacasmayo, a leading Peruvian producer of building materials with projected 2025 net sales of USD 630 million ... The transaction value of approximately USD 1.5 billion on a 100% basis ... expected to close in H1 2026.",
        "note": "Opened Holcim media release.",
    },
    {
        "id": "holcim_pacasmayo_20251216",
        "type": "official",
        "chicago": "Holcim. “Holcim to acquire majority stake in Cementos Pacasmayo.” Media release, December 2025.",
        "url": "https://www.holcim.com/media/media-releases/holcim-to-acquire-majority-stake-cementos-pacasmayo",
        "annotation": "Company primary Pacasmayo majority-stake acquisition notice. Supports holcim_pacasmayo_peru_2025.",
        "supports": ["holcim_pacasmayo_peru_2025", "hunt_infra_building_materials"],
    },
)

# 15 resources/niobium — budget miss (CBMM / CMOC already covered)

# 16 resources/nickel — Centaurus Jaguar mining lease (thin)
A(
    {
        "id": "centaurus_jaguar_nickel_lease_2025",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "Centaurus Metals — Jaguar Nickel Sulphide Project mining lease (Pará)",
        "country": "Brazil",
        "asset": "MME grant of Mining Lease for Jaguar Ni sulphide project — final key approval enabling commercial mining; FID/financing still pending",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-6.65",
        "lon": "-49.0",
        "geo_note": "Jaguar project, northern Pará / Carajás region (company ASX release; approximate).",
        "evidence": "documented",
        "source_id": "centaurus_jaguar_lease_20251010",
        "note": "Actor: Centaurus Metals (Australian ASX) — allied. ASX release 10 Oct 2025: Mining Lease granted by MME; all key environmental/mining approvals for construction; FID still pending financing. Distinct from MMG/Anglo Brazil nickel SPA pair.",
    },
    {
        "id": "centaurus_jaguar_nickel_lease_2025",
        "retrieved": "2026-10-01",
        "source_id": "centaurus_jaguar_lease_20251010",
        "url": "https://www.centaurus.com.au/site/pdf/621b42c5-21e4-4c49-b7e2-dc2ae304ffc2/Jaguar-Nickel-Project-Mining-Lease-Granted.pdf?Platform=ListPage",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Centaurus Metals ... is pleased to announce that the Mining Lease for its flagship Jaguar Nickel Sulphide Project in northern Brazil has been granted by the Brazilian Ministry of Mines and Energy (MME). ... Centaurus now holds all the key environmental and mining licences and approvals necessary to start the construction of Jaguar Project",
        "note": "Opened Centaurus ASX PDF announcement.",
    },
    {
        "id": "centaurus_jaguar_lease_20251010",
        "type": "official",
        "chicago": "Centaurus Metals Limited. “Jaguar Nickel Project Mining Lease Granted.” ASX announcement, 10 October 2025.",
        "url": "https://www.centaurus.com.au/site/pdf/621b42c5-21e4-4c49-b7e2-dc2ae304ffc2/Jaguar-Nickel-Project-Mining-Lease-Granted.pdf?Platform=ListPage",
        "annotation": "Company primary Jaguar Mining Lease grant notice. Supports centaurus_jaguar_nickel_lease_2025.",
        "supports": ["centaurus_jaguar_nickel_lease_2025", "hunt_res_nickel"],
    },
)

# 17 infrastructure/port_cranes — ZPMC STS+RTG delivery to Santos Brasil (thin)
A(
    {
        "id": "zpmc_santos_brasil_sts_rtg_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — Santos Brasil Tecon Santos STS + electric RTG delivery",
        "country": "Brazil",
        "asset": "Delivery of 2 STS quay cranes + 8 electric RTGs (ZPMC) to Tecon Santos; package ~R$300 million; arrived 10 Jan 2026 on Zhen Hua 28",
        "investment_type": "equipment_supply",
        "value": "300000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.92",
        "lon": "-46.38",
        "geo_note": "Tecon Santos, left bank Port of Santos (Santos Brasil release).",
        "evidence": "documented",
        "source_id": "santosbrasil_zpmc_20260112",
        "note": "Actor: ZPMC (PRC OEM); buyer Santos Brasil (Brazilian terminal). Company news 12 Jan 2026: 2 portêineres + 8 electric RTGs from ZPMC; ~R$300m; remote-ops capable. Distinct from zpmc_itapoa_rtg_2023 and DP World Lirquén. Value stored as BRL (no FX).",
    },
    {
        "id": "zpmc_santos_brasil_sts_rtg_2026",
        "retrieved": "2026-10-01",
        "source_id": "santosbrasil_zpmc_20260112",
        "url": "https://www.santosbrasil.com.br/v2021/noticia/novos-guindastes-de-operacao-remota-chegam-ao-tecon-santos",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Os equipamentos, fabricados pela chinesa ZPMC, chegaram ao Tecon Santos ... a bordo do navio Zhen Hua 28. ... Os dez guindastes têm investimentos da ordem de R$ 300 milhões.",
        "note": "Opened Santos Brasil Portuguese company news page.",
    },
    {
        "id": "santosbrasil_zpmc_20260112",
        "type": "official",
        "chicago": "Santos Brasil. “Novos guindastes de operação remota chegam ao Tecon Santos.” 12 January 2026.",
        "url": "https://www.santosbrasil.com.br/v2021/noticia/novos-guindastes-de-operacao-remota-chegam-ao-tecon-santos",
        "annotation": "Terminal operator primary notice of ZPMC STS/RTG delivery. Supports zpmc_santos_brasil_sts_rtg_2026.",
        "supports": ["zpmc_santos_brasil_sts_rtg_2026", "hunt_infra_port_cranes"],
    },
)

# 18 infrastructure/engineering_epc — Fluor Toromocho expansion EPCm (cycle-3 miss preference)
A(
    {
        "id": "fluor_toromocho_expansion_peru",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Fluor — Toromocho Expansion Project EPCm for Minera Chinalco Perú",
        "country": "Peru",
        "asset": "Fluor EPCm for Toromocho copper mine expansion designed to raise copper output ~45% (toward ~300,000 tpy)",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-11.6",
        "lon": "-76.15",
        "geo_note": "Junín Region, Peru (Fluor project page; high-altitude Toromocho).",
        "evidence": "documented",
        "source_id": "fluor_toromocho_expansion_page",
        "note": "Actor: Fluor (U.S.) EPCm for Chinalco Perú (PRC owner). Company project page documents selection for Toromocho Expansion. Complements fluor_salares_norte_chile_2024 / bechtel_los_pelambres; distinct asset from chinalco_toromocho_peru ownership row.",
    },
    {
        "id": "fluor_toromocho_expansion_peru",
        "retrieved": "2026-10-01",
        "source_id": "fluor_toromocho_expansion_page",
        "url": "https://www.fluor.com/projects/toromocho-expansion-project",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Fluor was selected by Minera Chinalco Perú S.A. to provide engineering, procurement and construction management (EPCm) services for its Toromocho Expansion Project in Junín Region, Peru. The expansion was designed to increase the mine’s copper output by 45%.",
        "note": "Opened Fluor project page.",
    },
    {
        "id": "fluor_toromocho_expansion_page",
        "type": "official",
        "chicago": "Fluor Corporation. “Toromocho Expansion Project — Fluor EPCM Project in Peru.” Company project page. Accessed 1 October 2026.",
        "url": "https://www.fluor.com/projects/toromocho-expansion-project",
        "annotation": "Company primary Toromocho Expansion EPCm project description. Supports fluor_toromocho_expansion_peru.",
        "supports": ["fluor_toromocho_expansion_peru", "hunt_infra_engineering_epc"],
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
        "hunt_energy_solar": "Cycle 4: logged spic_recurrent_marangatu_br_2024.",
        "hunt_energy_other_renewables": "Cycle 4: logged powerchina_san_gaban_iii_peru_2025.",
        "hunt_infra_port_ownership": "Cycle 4: logged dpworld_callao_bicentennial_2024.",
        "hunt_br_power_equip": "Cycle 4: equal budget; no new distinct grid award beyond prior Siemens/GE/Hitachi rows (miss).",
        "hunt_res_water": "Cycle 4: logged acciona_los_cabos_desal_mexico.",
        "hunt_energy_fission_smr": "Cycle 4: logged meitner_acr300_atucha_2026 (UNVERIFIED proposal proxy).",
        "hunt_res_balsa": "Cycle 4: equal budget; no new balsa trade year beyond WITS 2022–2024 pairs (miss).",
        "hunt_energy_wind": "Cycle 4: logged goldwind_spic_touros_br_2025.",
        "hunt_res_lithium": "Cycle 4: logged rio_tinto_rincon_expansion_2024.",
        "hunt_latam_rail_telecom": "Cycle 4: logged siemens_sp_line4_cbtc_2026 + crrc_salvador_metro_2026.",
        "hunt_res_graphite": "Cycle 4: logged graphcoa_boa_sorte_bahia_2024.",
        "hunt_infra_bridges_roads": "Cycle 4: logged crbc_ecuador_quininde_highway_2023.",
        "hunt_res_copper": "Cycle 4: logged southern_copper_tia_maria_2025.",
        "hunt_infra_building_materials": "Cycle 4: logged holcim_pacasmayo_peru_2025.",
        "hunt_fenb_araxa": "Cycle 4: equal budget; no new niobium unit-price/ownership beyond CBMM/CMOC (miss).",
        "hunt_res_nickel": "Cycle 4: logged centaurus_jaguar_nickel_lease_2025.",
        "hunt_infra_port_cranes": "Cycle 4: logged zpmc_santos_brasil_sts_rtg_2026.",
        "hunt_infra_engineering_epc": "Cycle 4: logged fluor_toromocho_expansion_peru.",
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
    print("Cycle 4 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
