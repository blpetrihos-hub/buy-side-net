#!/usr/bin/env python3
"""Cycle 3 hunt: shuffle_seed=20261003; equal budget across 18 subcategories."""
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


# seed 20261003 order:
# nickel, fission_smr, engineering_epc, water, bridges_roads, wind, power_plants_grid,
# balsa, niobium, port_cranes, copper, building_materials, lithium, rail, solar,
# dimension_stone, other_renewables, port_ownership

# 1 resources/nickel — budget: no new distinct public source beyond cycle1–2 MMG/Anglo pair (miss in HUNT_STATE)

# 2 energy/fission_smr — budget: no new SMR award beyond CAREM/CNNC rows (miss)

# 3 infrastructure/engineering_epc — budget: no new distinct EPC filing opened beyond cycle-2 Fluor/Bechtel (miss)

# 4 resources/water — Acciona Collahuasi desal
A(
    {
        "id": "acciona_collahuasi_desal_chile",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Compañía Minera Doña Inés de Collahuasi — Patache Port desalination plant",
        "country": "Chile",
        "asset": "ACCIONA design/build + 2-year O&M for 1,050 l/s seawater desalination plant at Patache Port",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2022",
        "status": "active",
        "lat": "-20.8",
        "lon": "-70.18",
        "geo_note": "Patache Port, ~70 km south of Iquique, Tarapacá (ACCIONA release).",
        "evidence": "documented",
        "source_id": "acciona_collahuasi_desal_20220802",
        "note": "Actor: ACCIONA (Spanish) — allied. Company release 2 Aug 2022: award for design/construction + O&M; 1,050 l/s initial capacity. No contract USD on page.",
    },
    {
        "id": "acciona_collahuasi_desal_chile",
        "retrieved": "2026-10-01",
        "source_id": "acciona_collahuasi_desal_20220802",
        "url": "https://www.acciona.com/updates/news/acciona-build-operate-chilean-desalination-plant-mining-firm-dona-ines-collahuasi",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "Compañía Minera Doña Inés de Collahuasi (CMDIC) has awarded ACCIONA the design and construction of a seawater desalination plant at Collahuasi's Patache Port... The desalination plant at the Patache Port will have an initial capacity of 1,050 liters per second.",
        "note": "Opened ACCIONA news page.",
    },
    {
        "id": "acciona_collahuasi_desal_20220802",
        "type": "official",
        "chicago": "ACCIONA. “ACCIONA to build and operate Chilean desalination plant for mining firm Doña Ines de Collahuasi.” 2 August 2022.",
        "url": "https://www.acciona.com/updates/news/acciona-build-operate-chilean-desalination-plant-mining-firm-dona-ines-collahuasi",
        "annotation": "Company primary award notice for Collahuasi Patache desal. Supports acciona_collahuasi_desal_chile.",
        "supports": ["acciona_collahuasi_desal_chile", "hunt_res_water"],
    },
)

# 5 infrastructure/bridges_roads — miss (SPARK/SCHIP/Demerara already logged)

# 6 energy/wind — Vestas Cimarron Mexico (Sempra)
A(
    {
        "id": "vestas_cimarron_mexico_2024",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Sempra Infrastructure — Cimarron wind farm (Energía Sierra Juárez Phase 3), Tecate, Baja California",
        "country": "Mexico",
        "asset": "Vestas supply/install 319 MW (46 × V163-4.5 + 18 × V162-6.2) + 10-year AOM 5000 service",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "32.45",
        "lon": "-116.6",
        "geo_note": "Tecate, Baja California (Vestas release).",
        "evidence": "documented",
        "source_id": "vestas_cimarron_20240314",
        "note": "Actor: Vestas (Danish) — allied; customer Sempra Infrastructure (U.S.). Company release 14 Mar 2024: 319 MW order; delivery Q4 2024; COD Q4 2025. No USD on page.",
    },
    {
        "id": "vestas_cimarron_mexico_2024",
        "retrieved": "2026-10-01",
        "source_id": "vestas_cimarron_20240314",
        "url": "https://www.vestas.com/en/media/company-news/2024/vestas-wins-order-from-sempra-infrastructure-to-build-a-c3946123",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Sempra Infrastructure, a subsidiary of Sempra, has placed a 319 MW order for the Cimarron wind farm in Tecate, in the state of Baja California, Mexico. ... supply and installation of 46 V163-4.5 MW turbines and 18 V162-6.2 MW turbines.",
        "note": "Opened Vestas company news release.",
    },
    {
        "id": "vestas_cimarron_20240314",
        "type": "official",
        "chicago": "Vestas. “Vestas wins order from Sempra infrastructure to build a 319 MW wind farm in Mexico.” 14 March 2024.",
        "url": "https://www.vestas.com/en/media/company-news/2024/vestas-wins-order-from-sempra-infrastructure-to-build-a-c3946123",
        "annotation": "Company primary wind order for Cimarron/Sempra Mexico. Supports vestas_cimarron_mexico_2024.",
        "supports": ["vestas_cimarron_mexico_2024", "hunt_energy_wind"],
    },
)

# 7 energy/power_plants_grid — Hitachi Garabi + Hitachi Brazil transformer capex
A(
    {
        "id": "hitachi_garabi_hvdc_upgrade_2023",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "Taesa — Garabi HVDC converter station (Brazil–Argentina interconnection)",
        "country": "Brazil",
        "asset": "Hitachi Energy MACH control/protection upgrade of Garabi 2,200 MW back-to-back HVDC station",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "-28.03",
        "lon": "-55.2",
        "geo_note": "Garabi converter station, Brazil near Argentina border (Hitachi release).",
        "evidence": "documented",
        "source_id": "hitachi_garabi_20231109",
        "note": "Actor: Hitachi Energy (Japan/Switzerland) — allied. Company release 9 Nov 2023: Taesa order for Garabi HVDC upgrade; first HVDC upgrade in Brazil. No USD on page.",
    },
    {
        "id": "hitachi_garabi_hvdc_upgrade_2023",
        "retrieved": "2026-10-01",
        "source_id": "hitachi_garabi_20231109",
        "url": "https://www.hitachienergy.com/news-and-events/press-releases/2023/11/hitachi-energy-wins-order-to-upgrade-world-record-high-voltage-direct-current-transmission-system",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Hitachi Energy ... won an order to provide Taesa ... with an extensive upgrade of the Garabi high-voltage direct current (HVDC) converter station in Brazil. The link can transmit up to 2,200 megawatts of electricity",
        "note": "Opened Hitachi Energy press release.",
    },
    {
        "id": "hitachi_garabi_20231109",
        "type": "official",
        "chicago": "Hitachi Energy. “Hitachi Energy wins order to upgrade world-record high-voltage direct current transmission system.” 9 November 2023.",
        "url": "https://www.hitachienergy.com/news-and-events/press-releases/2023/11/hitachi-energy-wins-order-to-upgrade-world-record-high-voltage-direct-current-transmission-system",
        "annotation": "Company primary Garabi HVDC upgrade award. Supports hitachi_garabi_hvdc_upgrade_2023.",
        "supports": ["hitachi_garabi_hvdc_upgrade_2023", "hunt_br_power_equip"],
    },
)

A(
    {
        "id": "hitachi_brazil_transformer_capex_2024",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "Hitachi Energy Brazil — Guarulhos transformer factory expansion + greenfield plant",
        "country": "Brazil",
        "asset": "Hitachi Energy investment over USD 200 million to expand Brazil transformer manufacturing (Guarulhos + new facility by 2028)",
        "investment_type": "ownership_equity",
        "value": "200000000",
        "currency": "USD",
        "value_usd": "200000000",
        "fx_usd": "1",
        "fx_date": "2024-09-04",
        "year": "2024",
        "status": "active",
        "lat": "-23.45",
        "lon": "-46.53",
        "geo_note": "Guarulhos, São Paulo (company feature); greenfield site TBD by 2028.",
        "evidence": "documented",
        "source_id": "hitachi_brazil_xfmr_20240904",
        "note": "Actor: Hitachi Energy — allied. Company feature 4 Sep 2024: >USD 200m Brazil transformer capacity investment. Manufacturing presence supporting LatAm grid equipment supply.",
    },
    {
        "id": "hitachi_brazil_transformer_capex_2024",
        "retrieved": "2026-10-01",
        "source_id": "hitachi_brazil_xfmr_20240904",
        "url": "https://www.hitachienergy.com/news-and-events/features/2024/09/hitachi-energy-invests-over-200-million-usd-to-expand-transformer-operations-in-brazil-and-address-increased-global-demand",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Hitachi Energy today announced an investment of over $200 million USD to significantly enhance its operations in Brazil... expansion and modernization of the Guarulhos’ transformer factory in São Paulo and the construction of a state-of-the-art greenfield transformer manufacturing facility, expected to be set up by 2028.",
        "note": "Opened Hitachi Energy feature page.",
    },
    {
        "id": "hitachi_brazil_xfmr_20240904",
        "type": "official",
        "chicago": "Hitachi Energy. “Hitachi Energy invests over $200 million USD to expand transformer operations in Brazil and address increased global demand.” 4 September 2024.",
        "url": "https://www.hitachienergy.com/news-and-events/features/2024/09/hitachi-energy-invests-over-200-million-usd-to-expand-transformer-operations-in-brazil-and-address-increased-global-demand",
        "annotation": "Company primary Brazil transformer manufacturing investment notice. Supports hitachi_brazil_transformer_capex_2024.",
        "supports": ["hitachi_brazil_transformer_capex_2024", "hunt_br_power_equip"],
    },
)

# 8 resources/balsa — WITS 2024
A(
    {
        "id": "wits_ecuador_balsa_china_2024",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "prc",
        "counterpart": "China — Ecuador HS 440723 sawn balsa/related wood imports (WITS/Comtrade)",
        "country": "Ecuador",
        "asset": "Ecuador 2024 exports of HS 440723 to China — USD 94.222 million (WITS)",
        "investment_type": "other",
        "value": "94221650",
        "currency": "USD",
        "value_usd": "94221650",
        "fx_usd": "1",
        "fx_date": "2024-12-31",
        "year": "2024",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "National trade aggregate; no site pin.",
        "evidence": "documented",
        "source_id": "wits_ecu_440723_2024",
        "note": "Trade flow. WITS/Comtrade Ecuador HS 440723 to China 2024. Complements 2022–2023 WITS balsa rows.",
    },
    {
        "id": "wits_ecuador_balsa_china_2024",
        "retrieved": "2026-10-01",
        "source_id": "wits_ecu_440723_2024",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2024/tradeflow/Exports/partner/ALL/product/440723",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Ecuador exported Baboen, Mahogany, Imbuia and Balsa wood, sawn l to China ($94,221.65K , 327,801 m³)",
        "note": "Opened WITS 2024 HS 440723 page.",
    },
    {
        "id": "wits_ecu_440723_2024",
        "type": "official",
        "chicago": "World Bank WITS / UN Comtrade. “Ecuador Baboen, Mahogany, Imbuia and Balsa wood, sawn l exports by country | 2024.” HS 440723.",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2024/tradeflow/Exports/partner/ALL/product/440723",
        "annotation": "Official trade mirror for Ecuador HS 440723 2024 exports. Supports China and US 2024 balsa rows.",
        "supports": [
            "wits_ecuador_balsa_china_2024",
            "wits_ecuador_balsa_us_2024",
            "hunt_res_balsa",
        ],
    },
)

A(
    {
        "id": "wits_ecuador_balsa_us_2024",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "us",
        "counterpart": "United States — Ecuador HS 440723 sawn balsa/related wood imports (WITS/Comtrade)",
        "country": "Ecuador",
        "asset": "Ecuador 2024 exports of HS 440723 to United States — USD 9.493 million (WITS)",
        "investment_type": "other",
        "value": "9493130",
        "currency": "USD",
        "value_usd": "9493130",
        "fx_usd": "1",
        "fx_date": "2024-12-31",
        "year": "2024",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "National trade aggregate; no site pin.",
        "evidence": "documented",
        "source_id": "wits_ecu_440723_2024",
        "note": "Trade flow. WITS/Comtrade Ecuador HS 440723 to United States 2024.",
    },
    {
        "id": "wits_ecuador_balsa_us_2024",
        "retrieved": "2026-10-01",
        "source_id": "wits_ecu_440723_2024",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2024/tradeflow/Exports/partner/ALL/product/440723",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Ecuador exported Baboen, Mahogany, Imbuia and Balsa wood, sawn l to ... United States ($9,493.13K , 24,116 m³)",
        "note": "Opened same WITS 2024 page; US partner row.",
    },
    {
        "id": "wits_ecu_440723_2024",
        "type": "official",
        "chicago": "World Bank WITS / UN Comtrade. “Ecuador Baboen, Mahogany, Imbuia and Balsa wood, sawn l exports by country | 2024.” HS 440723.",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2024/tradeflow/Exports/partner/ALL/product/440723",
        "annotation": "Official trade mirror for Ecuador HS 440723 2024 exports. Supports China and US 2024 balsa rows.",
        "supports": [
            "wits_ecuador_balsa_china_2024",
            "wits_ecuador_balsa_us_2024",
            "hunt_res_balsa",
        ],
    },
)

# 9 resources/niobium — miss (CBMM + CMOC already)

# 10 infrastructure/port_cranes — BTP renewal includes 4 STS + 27 RTG acquisitions (company; manufacturer not named → document under port_ownership APM; crane-maker miss)
# Use APM BTP for port_ownership; port_cranes miss this cycle (equipment OEM not named on opened page)

# 11 resources/copper — miss beyond Chinalco/MMG/FCX
# 12 infrastructure/building_materials — miss beyond Huaxin/Sinoma
# 13 resources/lithium — miss beyond Ganfeng/Codelco-SQM
# 14 infrastructure/rail — miss beyond CRRC/Alstom cycle2

# 15 energy/solar — Trina + Recurrent Ciranda
A(
    {
        "id": "trina_cemig_sim_brazil_2023",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Fiber X / CEMIG SIM DG solar plants (Minas Gerais)",
        "country": "Brazil",
        "asset": "Trina Solar supply of Vertex DEG21-660W modules + Vanguard 1P trackers for 90 MW CEMIG SIM portfolio",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "-19.92",
        "lon": "-43.94",
        "geo_note": "Minas Gerais DG portfolio (company PR; Belo Horizonte process pin).",
        "evidence": "documented",
        "source_id": "trina_cemig_sim_20231129",
        "note": "Actor: Trina Solar (PRC). Company PR Newswire 29 Nov 2023: modules + trackers for 90 MW CEMIG SIM via Fiber X. No USD on page.",
    },
    {
        "id": "trina_cemig_sim_brazil_2023",
        "retrieved": "2026-10-01",
        "source_id": "trina_cemig_sim_20231129",
        "url": "https://www.prnewswire.com/news-releases/trina-solar-to-offer-modules-and-trackers-for-90mw-pv-power-plants-in-brazil-302000288.html",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Trina Solar (SHA: 688599) has secured a supply agreement with the Brazilian EPC contractor Fiber X to offer solar modules and trackers to the CEMIG SIM project... The project has total capacity of 90MW.",
        "note": "Opened Trina/PR Newswire release.",
    },
    {
        "id": "trina_cemig_sim_20231129",
        "type": "official",
        "chicago": "Trina Solar. “Trina Solar to offer modules and trackers for 90MW PV power plants in Brazil.” PR Newswire, 29 November 2023.",
        "url": "https://www.prnewswire.com/news-releases/trina-solar-to-offer-modules-and-trackers-for-90mw-pv-power-plants-in-brazil-302000288.html",
        "annotation": "Company release on CEMIG SIM module/tracker supply. Supports trina_cemig_sim_brazil_2023.",
        "supports": ["trina_cemig_sim_brazil_2023", "hunt_energy_solar"],
    },
)

A(
    {
        "id": "recurrent_ciranda_solar_br_2023",
        "layer": "energy",
        "subcategory": "solar",
        "side": "allied",
        "counterpart": "Recurrent Energy (Canadian Solar) — Ciranda Solar Power Cluster",
        "country": "Brazil",
        "asset": "300 MW Ciranda Cluster owned/operated by Recurrent Energy; BRL 490m (~USD 100m) non-recourse financing received",
        "investment_type": "financing",
        "value": "100000000",
        "currency": "USD",
        "value_usd": "100000000",
        "fx_usd": "1",
        "fx_date": "2023-11-22",
        "year": "2023",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "Brazil Ciranda Cluster (company release; no precise plant pin on opened page).",
        "evidence": "documented",
        "source_id": "recurrent_ciranda_financing_20231122",
        "note": "Actor: Recurrent Energy / Canadian Solar (Canada-founded NASDAQ) — allied/other Western. Company release 22 Nov 2023: BRL 490m (~USD 100m) financing; cluster completed Aug 2023; BiHiKu modules. Stored USD approx as stated on page.",
    },
    {
        "id": "recurrent_ciranda_solar_br_2023",
        "retrieved": "2026-10-01",
        "source_id": "recurrent_ciranda_financing_20231122",
        "url": "https://www.prnewswire.com/news-releases/recurrent-energy-receives-490-million-brazilian-reais-financing-for-ciranda-cluster-in-brazil-301995679.html",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Recurrent Energy ... has fully received 490 million Brazilian reais (approximately US$100 million) of non-recourse project financing for its 300 MW Ciranda Solar Power Cluster ... Completed in August 2023",
        "note": "Opened PR Newswire / Canadian Solar release.",
    },
    {
        "id": "recurrent_ciranda_financing_20231122",
        "type": "official",
        "chicago": "Canadian Solar Inc. / Recurrent Energy. “Recurrent Energy Receives 490 Million Brazilian Reais Financing for Ciranda Cluster in Brazil.” PR Newswire, 22 November 2023.",
        "url": "https://www.prnewswire.com/news-releases/recurrent-energy-receives-490-million-brazilian-reais-financing-for-ciranda-cluster-in-brazil-301995679.html",
        "annotation": "Company financing notice for Ciranda Cluster ownership/ops. Supports recurrent_ciranda_solar_br_2023.",
        "supports": ["recurrent_ciranda_solar_br_2023", "hunt_energy_solar"],
    },
)

# 16 resources/dimension_stone — ABIROCHAS Brazil→US 2023
A(
    {
        "id": "abirochas_br_stone_us_2023",
        "layer": "resources",
        "subcategory": "dimension_stone",
        "side": "us",
        "counterpart": "United States — Brazilian ornamental/dimension stone imports (ABIROCHAS 2023 balance)",
        "country": "Brazil",
        "asset": "Brazil natural-stone exports to the United States — USD 608.4 million in 2023 (ABIROCHAS)",
        "investment_type": "other",
        "value": "608400000",
        "currency": "USD",
        "value_usd": "608400000",
        "fx_usd": "1",
        "fx_date": "2023-12-31",
        "year": "2023",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "National export aggregate; no quarry pin.",
        "evidence": "documented",
        "source_id": "abirochas_informe_01_2024",
        "note": "Trade flow (not equity). ABIROCHAS Informe 01/2024: US$608.4m to EUA in 2023 (54.7% of Brazil stone export value). Complements abirochas_br_stone_china_2023. Same source family as cycle-1 China row; US destination newly logged.",
    },
    {
        "id": "abirochas_br_stone_us_2023",
        "retrieved": "2026-10-01",
        "source_id": "abirochas_informe_01_2024",
        "url": "https://abirochas.com.br/wp-content/uploads/2024/03/Informe-01_2024-Balanco-2023.pdf",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Principal fornecedor para o mercado dos EUA (US$ 608 milhões exportados: -19% frente a 2022).",
        "note": "Opened ABIROCHAS Informe 01/2024 PDF (same file as China row; US destination).",
    },
    {
        "id": "abirochas_informe_01_2024",
        "type": "official",
        "chicago": "ABIROCHAS. “Balanço do Setor Brasileiro de Rochas Ornamentais e de Revestimento em 2023.” Informe 01/2024, March 2024.",
        "url": "https://abirochas.com.br/wp-content/uploads/2024/03/Informe-01_2024-Balanco-2023.pdf",
        "annotation": "Industry association balance of Brazilian ornamental stone exports. Supports China and US destination rows.",
        "supports": [
            "abirochas_br_stone_china_2023",
            "abirochas_br_stone_us_2023",
            "hunt_res_dimension_stone",
        ],
    },
)

# 17 energy/other_renewables — Ormat Zunil Guatemala
A(
    {
        "id": "ormat_zunil_guatemala",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "Ormat Technologies — Zunil geothermal plant",
        "country": "Guatemala",
        "asset": "Ormat-owned Zunil geothermal power plant (company global projects listing)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "14.76",
        "lon": "-91.45",
        "geo_note": "Zunil, Guatemala (company projects listing).",
        "evidence": "documented",
        "source_id": "ormat_global_projects_guatemala",
        "note": "Actor: Ormat (U.S.). Company global projects page lists Zunil Guatemala. Complements ormat_amatitlan_guatemala.",
    },
    {
        "id": "ormat_zunil_guatemala",
        "retrieved": "2026-10-01",
        "source_id": "ormat_global_projects_guatemala",
        "url": "https://www.ormat.com/en/projects/all/main/?pageNum=2",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Zunil Guatemala ... Amatitlan Guatemala",
        "note": "Opened Ormat Global Projects listing page.",
    },
    {
        "id": "ormat_global_projects_guatemala",
        "type": "official",
        "chicago": "Ormat Technologies Inc. “Global Projects.” Company page. Accessed 1 October 2026.",
        "url": "https://www.ormat.com/en/projects/all/main/?pageNum=2",
        "annotation": "Company project listing of Ormat Guatemala geothermal plants. Supports Amatitlán and Zunil rows.",
        "supports": [
            "ormat_amatitlan_guatemala",
            "ormat_zunil_guatemala",
            "hunt_energy_other_renewables",
        ],
    },
)

# 18 infrastructure/port_ownership — APM Terminals BTP Santos
A(
    {
        "id": "apmt_btp_santos_concession_2023",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "APM Terminals / TiL — Brasil Terminal Portuário (Port of Santos)",
        "country": "Brazil",
        "asset": "BTP lease renewal to 2047 with planned R$1.9bn (~USD 380–390m) investment; capacity to 2.1m TEU",
        "investment_type": "concession",
        "value": "380000000",
        "currency": "USD",
        "value_usd": "380000000",
        "fx_usd": "1",
        "fx_date": "2023-12-20",
        "year": "2023",
        "status": "active",
        "lat": "-23.95",
        "lon": "-46.3",
        "geo_note": "Port of Santos, Brazil (APM Terminals release).",
        "evidence": "documented",
        "source_id": "apmt_btp_renewal_20231220",
        "note": "Actor: APM Terminals (Maersk / Denmark) JV with TiL — allied. Company release 20 Dec 2023: 20-year extension to 2047; R$1.9bn (~USD 380m) investment plan (headline also says USD 390m). Stored USD 380m as explicit R$1.9bn approx on page. Also plans 4 STS + 27 RTG (OEM not named).",
    },
    {
        "id": "apmt_btp_santos_concession_2023",
        "retrieved": "2026-10-01",
        "source_id": "apmt_btp_renewal_20231220",
        "url": "https://www.apmterminals.com/en/news/news-releases/2023/231220-usd-390-million-investment-and-new-concession-for-brasil-terminal",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Brasil Terminal Portuário (BTP) has been authorized ... to operate at Port of Santos for an additional 20 years. As part of the contract extending until 2047, BTP plans to invest R$ 1.9 billion (approximately USD 380 million) in the container terminal",
        "note": "Opened APM Terminals news release.",
    },
    {
        "id": "apmt_btp_renewal_20231220",
        "type": "official",
        "chicago": "APM Terminals. “USD 390 million investment and new concession for Brasil Terminal Portuário.” 20 December 2023.",
        "url": "https://www.apmterminals.com/en/news/news-releases/2023/231220-usd-390-million-investment-and-new-concession-for-brasil-terminal",
        "annotation": "Company primary BTP Santos concession renewal/investment notice. Supports apmt_btp_santos_concession_2023.",
        "supports": ["apmt_btp_santos_concession_2023", "hunt_infra_port_ownership"],
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
        "hunt_res_nickel": "Cycle 3: equal budget; no new distinct Ni source beyond MMG/Anglo pair (miss).",
        "hunt_energy_fission_smr": "Cycle 3: equal budget; no new SMR award beyond CAREM/CNNC (miss).",
        "hunt_infra_engineering_epc": "Cycle 3: equal budget; no new EPC beyond Fluor/Bechtel cycle-2 (miss).",
        "hunt_res_water": "Cycle 3: logged acciona_collahuasi_desal_chile.",
        "hunt_infra_bridges_roads": "Cycle 3: equal budget; no new bridges/roads award beyond SPARK/SCHIP/Demerara (miss).",
        "hunt_energy_wind": "Cycle 3: logged vestas_cimarron_mexico_2024.",
        "hunt_br_power_equip": "Cycle 3: logged hitachi_garabi_hvdc_upgrade_2023 + hitachi_brazil_transformer_capex_2024.",
        "hunt_res_balsa": "Cycle 3: logged wits_ecuador_balsa_china_2024 + wits_ecuador_balsa_us_2024.",
        "hunt_fenb_araxa": "Cycle 3: equal budget; no new niobium unit-price source (miss).",
        "hunt_infra_port_cranes": "Cycle 3: equal budget; BTP names STS/RTG buys but not OEM — crane-maker miss.",
        "hunt_res_copper": "Cycle 3: equal budget; no new copper ownership beyond Chinalco/MMG/FCX (miss).",
        "hunt_infra_building_materials": "Cycle 3: equal budget; no new cement/aggregates award (miss).",
        "hunt_res_lithium": "Cycle 3: equal budget; no new lithium deal beyond Ganfeng/NovaAndino (miss).",
        "hunt_latam_rail_telecom": "Cycle 3: equal budget; no new rail award beyond CRRC/Alstom cycle-2 (miss).",
        "hunt_energy_solar": "Cycle 3: logged trina_cemig_sim_brazil_2023 + recurrent_ciranda_solar_br_2023.",
        "hunt_res_dimension_stone": "Cycle 3: logged abirochas_br_stone_us_2023 (US destination from ABIROCHAS).",
        "hunt_energy_other_renewables": "Cycle 3: logged ormat_zunil_guatemala.",
        "hunt_infra_port_ownership": "Cycle 3: logged apmt_btp_santos_concession_2023.",
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
    print("Cycle 3 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
