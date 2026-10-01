#!/usr/bin/env python3
"""Cycle 1 hunt: add sourced LatAm/Caribbean observations across all subcategories."""
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

# Each item: row dict + evidence dict + bib dict
ITEMS = []


def add(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


# --- Infrastructure ---
add(
    {
        "id": "cosco_chancay_port_2024",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "prc",
        "counterpart": "COSCO SHIPPING Ports Chancay Peru / Volcan (40%)",
        "country": "Peru",
        "asset": "Chancay Port Phase I (4 berths; COSCO first green/smart port investment in South America)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "1",
        "fx_date": "2024-11-14",
        "year": "2024",
        "status": "active",
        "lat": "-11.574",
        "lon": "-77.270",
        "geo_note": "Port of Chancay, ~78 km north of Lima (company release).",
        "evidence": "documented",
        "source_id": "cosco_chancay_inauguration_20241115",
        "note": "Actor: COSCO SHIPPING Ports (60% per company materials and prior HKEX subscription). Company press release documents Phase I inauguration 14 Nov 2024, design capacity 1m TEU / 6m t bulk / 160k vehicles. No Phase I USD capex figure on the opened Cosco page — value left blank (never fabricate). Upgrades hunt_infra_port_ownership.",
    },
    {
        "id": "cosco_chancay_port_2024",
        "retrieved": "2026-10-01",
        "source_id": "cosco_chancay_inauguration_20241115",
        "url": "https://ports.coscoshipping.com/en/Media/PressReleases/content.php?id=20241115",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Chancay Port is COSCO SHIPPING’s first green and smart port investment in South America... Spanning 1,500 meters in length with 4 berths... Designed for a throughput capacity of 1 million TEUs, 6 million tons of bulk cargo, and 160,000 vehicles annually.",
        "note": "Opened Cosco Ports press release; ownership stake confirmed in related Cosco materials.",
    },
    {
        "id": "cosco_chancay_inauguration_20241115",
        "type": "official",
        "chicago": "COSCO SHIPPING Ports Limited. “The Inauguration Ceremony of Chancay Port Was Successfully Held.” Press release, 15 November 2024.",
        "url": "https://ports.coscoshipping.com/en/Media/PressReleases/content.php?id=20241115",
        "annotation": "Company primary release on Chancay Phase I inauguration and design capacity. Does not print a Phase I USD capex on this page. Supports cosco_chancay_port_2024.",
        "supports": ["cosco_chancay_port_2024", "hunt_infra_port_ownership"],
    },
)

add(
    {
        "id": "zpmc_itapoa_rtg_2023",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "Port of Itapoá",
        "country": "Brazil",
        "asset": "5 rubber-tired gantry (RTG) cranes (181 t each) shipped assembled to Itapoá",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "-26.184",
        "lon": "-48.606",
        "geo_note": "Port of Itapoá, Santa Catarina (named terminal).",
        "evidence": "documented",
        "source_id": "zpmc_itapoa_rtg_pr_20230428",
        "note": "Actor: Shanghai Zhenhua Heavy Industries (ZPMC). Company PR Newswire release 28 Apr 2023: five RTGs shipped to Itapoá. No unit or package USD price on the opened page — value blank. Upgrades hunt_infra_port_cranes.",
    },
    {
        "id": "zpmc_itapoa_rtg_2023",
        "retrieved": "2026-10-01",
        "source_id": "zpmc_itapoa_rtg_pr_20230428",
        "url": "https://www.prnewswire.com/apac/news-releases/zpmc-ships-5-rtg-cranes-to-itapoa-brazil-301810531.html",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "ZPMC recently completed the uploading of 5 rubber-tired gantry (RTG) cranes. The units are now in transit to Itapoa Port in Brazil. The cranes, specially designed for the Brazilian port and each weighing 181 tons, were shipped already assembled.",
        "note": "Opened PR Newswire company release.",
    },
    {
        "id": "zpmc_itapoa_rtg_pr_20230428",
        "type": "official",
        "chicago": "Shanghai Zhenhua Heavy Industries Co., Ltd. “ZPMC Ships 5 RTG Cranes to Itapoa, Brazil.” PR Newswire, 28 April 2023.",
        "url": "https://www.prnewswire.com/apac/news-releases/zpmc-ships-5-rtg-cranes-to-itapoa-brazil-301810531.html",
        "annotation": "ZPMC company release on five RTG deliveries to Itapoá. No USD price on the page. Supports zpmc_itapoa_rtg_2023.",
        "supports": ["zpmc_itapoa_rtg_2023", "hunt_infra_port_cranes"],
    },
)

add(
    {
        "id": "chec_jamaica_spark_roads_2024",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "Government of Jamaica (MEGJC / SPARK Programme)",
        "country": "Jamaica",
        "asset": "SPARK road-network packages 1–4 awarded to China Harbour Engineering Company (CHEC)",
        "investment_type": "epc",
        "value": "36040000000",
        "currency": "JMD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "18.0179",
        "lon": "-76.8099",
        "geo_note": "Signing at Jamaica House, Kingston (ministry page). Packages cover island-wide corridors.",
        "evidence": "documented",
        "source_id": "jamaica_megid_chec_spark_20241205",
        "note": "Actor: China Harbour Engineering Company. Jamaica Ministry page 5 Dec 2024: four SPARK packages; PM states ~J$36.04bn for road work (+J$2bn pipes/mains; ~J$38bn total). Stored J$36.04bn road figure. USD conversion left blank pending a cited FX on the award date. Upgrades hunt_infra_bridges_roads.",
    },
    {
        "id": "chec_jamaica_spark_roads_2024",
        "retrieved": "2026-10-01",
        "source_id": "jamaica_megid_chec_spark_20241205",
        "url": "https://megid.gov.jm/contracts-signed-with-chec-for-spark-programme/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "the contracts cover four packages and are valued at over $36.04 billion dollars for the road work, while an additional $2 billion will be spent on pipes and water mains... that would total approximately J$38 billion with J$36 billion applicable to road infrastructure",
        "note": "Opened Jamaica MEGID ministry page.",
    },
    {
        "id": "jamaica_megid_chec_spark_20241205",
        "type": "official",
        "chicago": "Jamaica. Ministry of Economic Growth and Job Creation / MEGID. “Contracts signed with CHEC for SPARK Programme.” 5 December 2024.",
        "url": "https://megid.gov.jm/contracts-signed-with-chec-for-spark-programme/",
        "annotation": "Ministry primary notice of CHEC SPARK road packages and JMD package totals. Supports chec_jamaica_spark_roads_2024.",
        "supports": ["chec_jamaica_spark_roads_2024", "hunt_infra_bridges_roads"],
    },
)

add(
    {
        "id": "crcc_demerara_bridge_2022",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "Government of Guyana (Ministry of Public Works)",
        "country": "Guyana",
        "asset": "New Demerara River Bridge (four-lane) — CRCC-led joint venture contract",
        "investment_type": "epc",
        "value": "260000000",
        "currency": "USD",
        "value_usd": "260000000",
        "fx_usd": "1",
        "fx_date": "2022-05-25",
        "year": "2022",
        "status": "active",
        "lat": "6.8045",
        "lon": "-58.1551",
        "geo_note": "Demerara River crossing at Greater Georgetown / west bank corridor; pin is capital process city pending surveyed abutment coordinates.",
        "evidence": "proxy",
        "source_id": "kaieteur_demerara_bridge_20220526",
        "note": "UNVERIFIED proxy (press). Kaieteur News 26 May 2022 reports US$260m contract signed with China Railway Construction Corporation-led JV. Press-only until a ministry PDF is opened. Actor: CRCC.",
    },
    {
        "id": "crcc_demerara_bridge_2022",
        "retrieved": "2026-10-01",
        "source_id": "kaieteur_demerara_bridge_20220526",
        "url": "https://kaieteurnewsonline.com/2022/05/26/us260m-contract-signed-for-new-demerara-river-bridge/",
        "price_year": "2022",
        "evidence": "proxy",
        "quote": "the Government of Guyana through the Ministry of Public Works on Wednesday signed the contract for the construction of a new US$260 million Demerara River Bridge (DRB).",
        "note": "Opened Kaieteur News article; press-only figure.",
    },
    {
        "id": "kaieteur_demerara_bridge_20220526",
        "type": "journalism",
        "chicago": "Kaieteur News. “US$260M contract signed for new Demerara River Bridge.” 26 May 2022.",
        "url": "https://kaieteurnewsonline.com/2022/05/26/us260m-contract-signed-for-new-demerara-river-bridge/",
        "annotation": "Press report of CRCC-led Demerara River Bridge contract at US$260m. UNVERIFIED until ministry document confirms. Supports crcc_demerara_bridge_2022.",
        "supports": ["crcc_demerara_bridge_2022"],
    },
)

add(
    {
        "id": "huaxin_embu_aggregates_br_2025",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "prc",
        "counterpart": "EMBU S.A. Engenharia e Comércio / ITATUBA Participações (São Paulo aggregates)",
        "country": "Brazil",
        "asset": "Acquisition of São Paulo-area aggregates producer EMBU (via ITATUBA) — Huaxin Cement",
        "investment_type": "ownership_equity",
        "value": "176900000",
        "currency": "USD",
        "value_usd": "176900000",
        "fx_usd": "1",
        "fx_date": "2025-03-17",
        "year": "2025",
        "status": "active",
        "lat": "-23.5505",
        "lon": "-46.6333",
        "geo_note": "São Paulo metropolitan aggregates plants (company filing); pin is metro area, not a surveyed quarry gate.",
        "evidence": "documented",
        "source_id": "huaxin_hkex_brazil_completion_20250326",
        "note": "Actor: Huaxin Cement (via Huaxin Hainan Investment). HKEX announcement: acquisition completed 17 Mar 2025; initial consideration USD 176.9 million paid; targets become indirect wholly-owned subsidiaries. Upgrades hunt_infra_building_materials.",
    },
    {
        "id": "huaxin_embu_aggregates_br_2025",
        "retrieved": "2026-10-01",
        "source_id": "huaxin_hkex_brazil_completion_20250326",
        "url": "https://www.hkexnews.hk/listedco/listconews/sehk/2025/0326/2025032601508.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The acquisition was completed on 17 March 2025 and an initial consideration of USD176.9 million was paid.",
        "note": "Opened Huaxin HKEX PDF.",
    },
    {
        "id": "huaxin_hkex_brazil_completion_20250326",
        "type": "official",
        "chicago": "Huaxin Cement Co., Ltd. Announcement regarding completion of acquisition of equity interests in the Brazilian aggregate project. Hong Kong Stock Exchange filing, 26 March 2025.",
        "url": "https://www.hkexnews.hk/listedco/listconews/sehk/2025/0326/2025032601508.pdf",
        "annotation": "HKEX primary filing: Huaxin completes Brazil EMBU/ITATUBA aggregates acquisition at initial USD 176.9m. Supports huaxin_embu_aggregates_br_2025.",
        "supports": ["huaxin_embu_aggregates_br_2025", "hunt_infra_building_materials"],
    },
)

add(
    {
        "id": "sinoma_loma_negra_amali_epc",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "prc",
        "counterpart": "Loma Negra (InterCement) — L’Amali Line II, Olavarría",
        "country": "Argentina",
        "asset": "Sinoma Overseas EPC for 5,800 tpd L’Amali Line II cement plant",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "-36.8927",
        "lon": "-60.3225",
        "geo_note": "Olavarría, Buenos Aires Province (CemNet article).",
        "evidence": "documented",
        "source_id": "cemnet_sinoma_amali_20230109",
        "note": "Actor: Sinoma Overseas Development (CNBM). CemNet 9 Jan 2023 (Sinoma-authored): first SODC EPC in South America; 5800 tpd L’Amali II; scope engineering through commissioning. No contract USD on the opened page — value blank. Observation year is the 2023 performance write-up of the operating line. Upgrades hunt_infra_engineering_epc.",
    },
    {
        "id": "sinoma_loma_negra_amali_epc",
        "retrieved": "2026-10-01",
        "source_id": "cemnet_sinoma_amali_20230109",
        "url": "https://www.cemnet.com/Articles/story/174108/sinoma-s-latin-american-debut.html",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Loma Negra’s L’Amali Line II project in Argentina is the first EPC project contracted by Sinoma Overseas Development Co Ltd (a subsidiary of CNBM) in South America... The 5800tpd L’Amali II production line... is located in Olavarría, Argentina.",
        "note": "Opened CemNet article.",
    },
    {
        "id": "cemnet_sinoma_amali_20230109",
        "type": "official",
        "chicago": "Sinoma Overseas Development Co Ltd. “Sinoma’s Latin American debut.” CemNet, 9 January 2023.",
        "url": "https://www.cemnet.com/Articles/story/174108/sinoma-s-latin-american-debut.html",
        "annotation": "Company-authored CemNet article on Sinoma EPC for Loma Negra L’Amali II (5800 tpd). No USD contract figure on the page. Supports sinoma_loma_negra_amali_epc.",
        "supports": ["sinoma_loma_negra_amali_epc", "hunt_infra_engineering_epc"],
    },
)

# Rail already has SP metro / EFE — add Vestas is wind; note rail hunt stays but we add nothing duplicate.
# Upgrade hunt note via a thin documented US/allied rail presence if needed — skip if already covered.

# --- Resources ---
add(
    {
        "id": "ganfeng_pastos_grandes_stake_2024",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "Lithium Argentina (Proyecto Pastos Grandes S.A.), Salta",
        "country": "Argentina",
        "asset": "Ganfeng acquisition of 14.9% of Pastos Grandes project company for $70 million",
        "investment_type": "ownership_equity",
        "value": "70000000",
        "currency": "USD",
        "value_usd": "70000000",
        "fx_usd": "1",
        "fx_date": "2024-08-16",
        "year": "2024",
        "status": "active",
        "lat": "-24.5",
        "lon": "-66.75",
        "geo_note": "Pastos Grandes basin, Salta Province (company release). Approximate basin pin; not a surveyed well pad.",
        "evidence": "documented",
        "source_id": "globenewswire_laac_ganfeng_pg_20240816",
        "note": "Actor: Ganfeng Lithium. Lithium Argentina GlobeNewswire 16 Aug 2024: Ganfeng acquired $70m newly issued shares of PGCo = 14.9% of Pastos Grandes. Upgrades hunt_res_lithium.",
    },
    {
        "id": "ganfeng_pastos_grandes_stake_2024",
        "retrieved": "2026-10-01",
        "source_id": "globenewswire_laac_ganfeng_pg_20240816",
        "url": "https://www.globenewswire.com/news-release/2024/08/16/2931501/0/en/lithium-argentina-closes-pastos-grandes-transaction-with-ganfeng-lithium.html",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Ganfeng Lithium acquired $70 million in newly issued shares of Proyecto Pastos Grandes S.A. (“PGCo”)... representing a 14.9% interest in PGCo and Pastos Grandes.",
        "note": "Opened GlobeNewswire company release.",
    },
    {
        "id": "globenewswire_laac_ganfeng_pg_20240816",
        "type": "official",
        "chicago": "Lithium Americas (Argentina) Corp. “Lithium Argentina Closes Pastos Grandes Transaction with Ganfeng Lithium.” GlobeNewswire, 16 August 2024.",
        "url": "https://www.globenewswire.com/news-release/2024/08/16/2931501/0/en/lithium-argentina-closes-pastos-grandes-transaction-with-ganfeng-lithium.html",
        "annotation": "Issuer release on Ganfeng’s US$70m / 14.9% Pastos Grandes stake. Supports ganfeng_pastos_grandes_stake_2024.",
        "supports": ["ganfeng_pastos_grandes_stake_2024", "hunt_res_lithium"],
    },
)

add(
    {
        "id": "ganfeng_lithea_ppg_2022",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "Lithea (Pozuelos–Pastos Grandes), Salta, Argentina",
        "country": "Argentina",
        "asset": "Ganfeng agreement to acquire Lithea / PPG lithium brine assets for up to US$962 million",
        "investment_type": "ownership_equity",
        "value": "962000000",
        "currency": "USD",
        "value_usd": "962000000",
        "fx_usd": "1",
        "fx_date": "2022-07-11",
        "year": "2022",
        "status": "active",
        "lat": "-24.7",
        "lon": "-66.7",
        "geo_note": "Pozuelos–Pastos Grandes, Salta (exchange announcement via CnEVPost). Approximate basin pin.",
        "evidence": "proxy",
        "source_id": "cnevpost_ganfeng_lithea_20220712",
        "note": "UNVERIFIED proxy pending HKEX/SSE primary PDF open in this cycle. CnEVPost 12 Jul 2022 summarizes Shenzhen-listed Ganfeng announcement: up to US$962m for Lithea PPG assets. Press/aggregator reprint of exchange filing.",
    },
    {
        "id": "ganfeng_lithea_ppg_2022",
        "retrieved": "2026-10-01",
        "source_id": "cnevpost_ganfeng_lithea_20220712",
        "url": "https://cnevpost.com/2022/07/12/ganfeng-lithium-to-buy-lithea-which-has-lithium-resources-in-argentina-for-up-to-962-million/",
        "price_year": "2022",
        "evidence": "proxy",
        "quote": "Ganfeng Lithium (SHE: 002460) plans to buy up to 100 percent of Argentina-focused Lithea for up to $962 million, the Shenzhen-listed Chinese lithium giant said in an exchange announcement Monday.",
        "note": "Opened CnEVPost; primary SSE PDF not opened this cycle.",
    },
    {
        "id": "cnevpost_ganfeng_lithea_20220712",
        "type": "journalism",
        "chicago": "CnEVPost. “Ganfeng Lithium to buy Lithea, which has lithium resources in Argentina, for up to $962 million.” 12 July 2022.",
        "url": "https://cnevpost.com/2022/07/12/ganfeng-lithium-to-buy-lithea-which-has-lithium-resources-in-argentina-for-up-to-962-million/",
        "annotation": "Trade press summarizing Ganfeng exchange announcement on Lithea/PPG. Treated as UNVERIFIED proxy until primary filing opened. Supports ganfeng_lithea_ppg_2022.",
        "supports": ["ganfeng_lithea_ppg_2022"],
    },
)

add(
    {
        "id": "mmg_las_bambas_peru",
        "layer": "resources",
        "subcategory": "copper",
        "side": "prc",
        "counterpart": "Minera Las Bambas (Apurímac, Peru)",
        "country": "Peru",
        "asset": "Las Bambas copper mine — MMG-led consortium (MMG 62.5%, Guoxin 22.5%, CITIC Metal 15%)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-14.083",
        "lon": "-72.317",
        "geo_note": "Las Bambas, Cotabambas/Grau, Apurímac (MMG operations page).",
        "evidence": "documented",
        "source_id": "mmg_las_bambas_ops",
        "note": "Actor: MMG Limited (China Minmetals–controlled) as operator with Guoxin and CITIC Metal. MMG operations page documents ownership split and commercial production since 2016. No new acquisition USD on this page — value blank. Observation year 2024 = page retrieval window for ongoing presence. Upgrades hunt_res_copper.",
    },
    {
        "id": "mmg_las_bambas_peru",
        "retrieved": "2026-10-01",
        "source_id": "mmg_las_bambas_ops",
        "url": "https://www.mmg.com/operations/las-bambas/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Minera Las Bambas belongs to a consortium led by MMG Limited (MMG) (62.5%) together with Guoxin International Investment Co. Ltd (22.5%) and CITIC Metal Co. Ltd (15%), with MMG as the operator.",
        "note": "Opened MMG operations page.",
    },
    {
        "id": "mmg_las_bambas_ops",
        "type": "official",
        "chicago": "MMG Limited. “Las Bambas.” Operations page. Accessed 1 October 2026.",
        "url": "https://www.mmg.com/operations/las-bambas/",
        "annotation": "Company primary page for Las Bambas ownership and location. Supports mmg_las_bambas_peru.",
        "supports": ["mmg_las_bambas_peru", "hunt_res_copper"],
    },
)

add(
    {
        "id": "fcx_cerro_verde_peru",
        "layer": "resources",
        "subcategory": "copper",
        "side": "us",
        "counterpart": "Cerro Verde / El Abra (Freeport-McMoRan South America)",
        "country": "Peru",
        "asset": "Freeport-McMoRan South America copper operations (Cerro Verde, Peru; El Abra, Chile listed on same ops page)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-16.533",
        "lon": "-71.567",
        "geo_note": "Cerro Verde, Arequipa region (FCX South America operations listing).",
        "evidence": "documented",
        "source_id": "fcx_south_america_ops",
        "note": "Actor: Freeport-McMoRan (U.S.). Company operations page lists Cerro Verde (Peru) and El Abra (Chile) under South America. Presence observation; no transaction USD on the page. Country coded Peru for the Cerro Verde pin.",
    },
    {
        "id": "fcx_cerro_verde_peru",
        "retrieved": "2026-10-01",
        "source_id": "fcx_south_america_ops",
        "url": "https://www.fcx.com/operations/south-america",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "SOUTH AMERICA Cerro Verde El Abra",
        "note": "Opened Freeport operations page listing Cerro Verde and El Abra.",
    },
    {
        "id": "fcx_south_america_ops",
        "type": "official",
        "chicago": "Freeport-McMoRan. “South America.” Operations page. Accessed 1 October 2026.",
        "url": "https://www.fcx.com/operations/south-america",
        "annotation": "Company primary listing of Cerro Verde (Peru) and El Abra (Chile). Supports fcx_cerro_verde_peru.",
        "supports": ["fcx_cerro_verde_peru"],
    },
)

add(
    {
        "id": "mmg_anglo_nickel_brazil_2025",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "prc",
        "counterpart": "Anglo American Nickel Brazil (Barro Alto, Codemin / Niquelândia)",
        "country": "Brazil",
        "asset": "MMG SPA to acquire Anglo American’s Brazil nickel business for up to US$500 million",
        "investment_type": "ownership_equity",
        "value": "500000000",
        "currency": "USD",
        "value_usd": "500000000",
        "fx_usd": "1",
        "fx_date": "2025-02-18",
        "year": "2025",
        "status": "active",
        "lat": "-14.95",
        "lon": "-48.92",
        "geo_note": "Barro Alto / Niquelândia nickel belt, Goiás (company announcement). Approximate ops pin; deal still subject to regulatory clearances per later HKEX update.",
        "evidence": "documented",
        "source_id": "mmg_anglo_nickel_20250218",
        "note": "Actor: MMG Limited. Company release 18 Feb 2025: up to US$500m (US$350m upfront + contingent). Stored headline aggregate cap. Status remains conditional (EU review extended long-stop to 2026 per later filing) — still a disclosed PRC-side investment agreement. Upgrades hunt_res_nickel.",
    },
    {
        "id": "mmg_anglo_nickel_brazil_2025",
        "retrieved": "2026-10-01",
        "source_id": "mmg_anglo_nickel_20250218",
        "url": "https://www.mmg.com/investors/news-centre/mmg-to-acquire-anglo-americans-nickel-business/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "MMG Limited... has entered into a Share Purchase Agreement with Anglo American plc... for their nickel business in Brazil... for an aggregate cash consideration of up to US$500 million, comprised of upfront cash consideration of US$350 million and up to US$150 million in contingent consideration.",
        "note": "Opened MMG news centre release.",
    },
    {
        "id": "mmg_anglo_nickel_20250218",
        "type": "official",
        "chicago": "MMG Limited. “MMG to acquire Anglo American’s nickel business.” 18 February 2025.",
        "url": "https://www.mmg.com/investors/news-centre/mmg-to-acquire-anglo-americans-nickel-business/",
        "annotation": "Company primary announcement of up-to-US$500m Brazil nickel acquisition. Supports mmg_anglo_nickel_brazil_2025.",
        "supports": ["mmg_anglo_nickel_brazil_2025", "hunt_res_nickel"],
    },
)

add(
    {
        "id": "abirochas_br_stone_china_2023",
        "layer": "resources",
        "subcategory": "dimension_stone",
        "side": "prc",
        "counterpart": "China (importer of Brazilian ornamental stone / blocks)",
        "country": "Brazil",
        "asset": "Brazilian ornamental & dimension stone exports to China — 2023 trade (ABIROCHAS balanço)",
        "investment_type": "offtake",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "National export aggregate; no named quarry pin.",
        "evidence": "documented",
        "source_id": "abirochas_balanco_2023",
        "note": "PRC as dominant block buyer class in ABIROCHAS 2023 sector balance. Report lists China among top destinations with low average price (blocks). Exact China USD total not extracted as a clean single cell without risk of mis-read — value left blank; presence/offtake observation only. Upgrades hunt_res_dimension_stone.",
    },
    {
        "id": "abirochas_br_stone_china_2023",
        "retrieved": "2026-10-01",
        "source_id": "abirochas_balanco_2023",
        "url": "https://abirochas.com.br/wp-content/uploads/2024/03/Informe-01_2024-Balanco-2023.pdf",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Os dez principais destinos das exportações brasileiras de rochas em 2023 incluíram, nesta ordem e em faturamento, EUA, China, Itália... O preço médio dos produtos exportados variou de US$ 260/t para a China, com blocos...",
        "note": "Opened ABIROCHAS Informe 01/2024 PDF.",
    },
    {
        "id": "abirochas_balanco_2023",
        "type": "official",
        "chicago": "ABIROCHAS (Associação Brasileira da Indústria de Rochas Ornamentais). “Balanço do setor brasileiro de rochas ornamentais e de revestimento em 2023.” Informe 01/2024, March 2024.",
        "url": "https://abirochas.com.br/wp-content/uploads/2024/03/Informe-01_2024-Balanco-2023.pdf",
        "annotation": "Industry association primary export balance; China among top destinations for Brazilian stone (esp. blocks). Supports abirochas_br_stone_china_2023.",
        "supports": ["abirochas_br_stone_china_2023", "hunt_res_dimension_stone"],
    },
)

add(
    {
        "id": "wits_ecuador_balsa_china_2022",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "prc",
        "counterpart": "China (importer of Ecuador HS 440723 balsa/related sawn wood)",
        "country": "Ecuador",
        "asset": "Ecuador exports of HS 440723 (balsa and related sawn woods) to China — 2022 WITS/Comtrade",
        "investment_type": "offtake",
        "value": "85859460",
        "currency": "USD",
        "value_usd": "85859460",
        "fx_usd": "1",
        "fx_date": "2022-12-31",
        "year": "2022",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "National customs aggregate; no named mill pin.",
        "evidence": "documented",
        "source_id": "wits_ecuador_balsa_2022",
        "note": "World Bank WITS table: Ecuador→China HS 440723 export trade value US$85,859.46 thousand in 2022 (quantity 31,389 m³). Buy-side destination is PRC. Upgrades hunt_res_balsa.",
    },
    {
        "id": "wits_ecuador_balsa_china_2022",
        "retrieved": "2026-10-01",
        "source_id": "wits_ecuador_balsa_2022",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2022/tradeflow/Exports/partner/ALL/product/440723",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "Ecuador exported Baboen, Mahogany, Imbuia and Balsa wood, sawn l to China ($85,859.46K , 31,389 m³)",
        "note": "Opened WITS/Comtrade table.",
    },
    {
        "id": "wits_ecuador_balsa_2022",
        "type": "official",
        "chicago": "World Bank. World Integrated Trade Solution (WITS) / UN Comtrade. “Ecuador exports by country — HS 440723 (2022).”",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2022/tradeflow/Exports/partner/ALL/product/440723",
        "annotation": "Public customs aggregate for Ecuador balsa-related sawn wood exports to China. Supports wits_ecuador_balsa_china_2022.",
        "supports": ["wits_ecuador_balsa_china_2022", "hunt_res_balsa"],
    },
)

add(
    {
        "id": "wits_ecuador_balsa_us_2022",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "us",
        "counterpart": "United States (importer of Ecuador HS 440723)",
        "country": "Ecuador",
        "asset": "Ecuador exports of HS 440723 to the United States — 2022 WITS/Comtrade",
        "investment_type": "offtake",
        "value": "3783980",
        "currency": "USD",
        "value_usd": "3783980",
        "fx_usd": "1",
        "fx_date": "2022-12-31",
        "year": "2022",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "National customs aggregate; no named mill pin.",
        "evidence": "documented",
        "source_id": "wits_ecuador_balsa_2022",
        "note": "Same WITS table: Ecuador→United States HS 440723 = US$3,783.98 thousand (1,501 m³) in 2022. Comparative U.S. offtake alongside PRC row.",
    },
    {
        "id": "wits_ecuador_balsa_us_2022",
        "retrieved": "2026-10-01",
        "source_id": "wits_ecuador_balsa_2022",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2022/tradeflow/Exports/partner/ALL/product/440723",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "Ecuador exported Baboen, Mahogany, Imbuia and Balsa wood, sawn l to... United States ($3,783.98K , 1,501 m³)",
        "note": "Same opened WITS table as China row.",
    },
    {
        "id": "wits_ecuador_balsa_2022",
        "type": "official",
        "chicago": "World Bank. World Integrated Trade Solution (WITS) / UN Comtrade. “Ecuador exports by country — HS 440723 (2022).”",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2022/tradeflow/Exports/partner/ALL/product/440723",
        "annotation": "Public customs aggregate for Ecuador balsa-related sawn wood exports. Supports wits_ecuador_balsa_china_2022 and wits_ecuador_balsa_us_2022.",
        "supports": ["wits_ecuador_balsa_china_2022", "wits_ecuador_balsa_us_2022", "hunt_res_balsa"],
    },
)

add(
    {
        "id": "bechtel_qb2_desal_chile",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Teck Quebrada Blanca Phase 2 (Tarapacá, Chile)",
        "country": "Chile",
        "asset": "QB2 desalination plant + water pipeline (Bechtel EPC scope within QB2 megaproject)",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-20.2167",
        "lon": "-70.1500",
        "geo_note": "QB2 desal/port area, Tarapacá Region / Iquique corridor (Bechtel project page). Approximate coastal works pin.",
        "evidence": "documented",
        "source_id": "bechtel_qb2_project",
        "note": "Actor: Bechtel (U.S.). Company project page: QB2 includes high-capacity desalination plant and 165 km water pipeline; project completed 2024 / inaugurated Oct 2023. No standalone desal USD on the page — value blank. Upgrades hunt_res_water.",
    },
    {
        "id": "bechtel_qb2_desal_chile",
        "retrieved": "2026-10-01",
        "source_id": "bechtel_qb2_project",
        "url": "https://www.bechtel.com/projects/quebrada-blanca-phase-2/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "QB2 included a concentrator... as well as various complementary facilities, a new port and a desalination plant, infrastructure that is connected by concentrate and desalinated water pipelines.",
        "note": "Opened Bechtel project page.",
    },
    {
        "id": "bechtel_qb2_project",
        "type": "official",
        "chicago": "Bechtel. “Quebrada Blanca Phase 2.” Project page. Accessed 1 October 2026.",
        "url": "https://www.bechtel.com/projects/quebrada-blanca-phase-2/",
        "annotation": "U.S. EPC company page documenting QB2 desalination plant and water pipeline in Chile. Supports bechtel_qb2_desal_chile.",
        "supports": ["bechtel_qb2_desal_chile", "hunt_res_water"],
    },
)

add(
    {
        "id": "ide_saddn_desal_chile_2023",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Codelco Northern District / Techint E&C (SADDN), Tocopilla area",
        "country": "Chile",
        "asset": "SADDN desalination plant EPC (design ~73,000 m³/day phase 1) — IDE Technologies",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "-22.092",
        "lon": "-70.196",
        "geo_note": "Tocopilla area, northern Chile (IDE release).",
        "evidence": "documented",
        "source_id": "ide_saddn_ntp_20230605",
        "note": "Actor: IDE Technologies (Israeli) — allied/other non-PRC. Company release 5 Jun 2023: NTP for desal EPC within SADDN for Codelco. Capacity stated; no USD on page.",
    },
    {
        "id": "ide_saddn_desal_chile_2023",
        "retrieved": "2026-10-01",
        "source_id": "ide_saddn_ntp_20230605",
        "url": "https://ide-tech.com/en/ide-to-execute-epc-of-the-saddn-desalination-plant-in-northern-chile/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "IDE Technologies... received the NTP (Notice To Proceed) of the EPC contract of the SADDN Desalination Plant by Techint E&C... design capacity of 840 lps (roughly 73,000 m3/day).",
        "note": "Opened IDE company release.",
    },
    {
        "id": "ide_saddn_ntp_20230605",
        "type": "official",
        "chicago": "IDE Technologies. “IDE to execute EPC of the SADDN Desalination Plant in Northern Chile.” 5 June 2023.",
        "url": "https://ide-tech.com/en/ide-to-execute-epc-of-the-saddn-desalination-plant-in-northern-chile/",
        "annotation": "Company primary NTP release for Codelco SADDN desal EPC. Supports ide_saddn_desal_chile_2023.",
        "supports": ["ide_saddn_desal_chile_2023"],
    },
)

# Niobium: upgrade hunt with USGS Brazil context already archived mostly — keep hunt_fenb; add CBMM presence note from USGS MCS already archived for US. Use CBMM site for Brazil mine presence without inventing price.
add(
    {
        "id": "cbmm_araxa_presence_2024",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "CBMM (Companhia Brasileira de Metalurgia e Mineração), Araxá",
        "country": "Brazil",
        "asset": "CBMM Araxá niobium operations (ongoing Brazilian producer presence)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-19.5902",
        "lon": "-46.9406",
        "geo_note": "CBMM headquarters / Araxá operations area.",
        "evidence": "documented",
        "source_id": "cbmm_site_2026",
        "note": "Actor: CBMM (Brazilian; allied/other non-PRC vs PRC FeNb). Company site documents Brazil niobium operations. No sale price on the opened page — presence only. Complements hunt_fenb_araxa.",
    },
    {
        "id": "cbmm_araxa_presence_2024",
        "retrieved": "2026-10-01",
        "source_id": "cbmm_site_2026",
        "url": "https://cbmm.com/en",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "CBMM",
        "note": "Opened CBMM corporate site confirming Brazilian niobium producer presence at Araxá.",
    },
    {
        "id": "cbmm_site_2026",
        "type": "official",
        "chicago": "CBMM (Companhia Brasileira de Metalurgia e Mineração). Corporate website. Accessed 1 October 2026.",
        "url": "https://cbmm.com/en",
        "annotation": "Company site establishing CBMM as the Brazilian niobium producer at Araxá. Presence only; no unit price. Supports cbmm_araxa_presence_2024.",
        "supports": ["cbmm_araxa_presence_2024", "hunt_fenb_araxa"],
    },
)

# --- Energy ---
add(
    {
        "id": "cnnc_atucha_hualong_epc_2022",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "prc",
        "counterpart": "Nucleoeléctrica Argentina (Atucha complex)",
        "country": "Argentina",
        "asset": "Reported turnkey EPC for Hualong-1 / HPR1000 at Atucha (CNNC) — Feb 2022 contract narrative",
        "investment_type": "epc",
        "value": "6800000000",
        "currency": "USD",
        "value_usd": "6800000000",
        "fx_usd": "1",
        "fx_date": "2022-02-01",
        "year": "2022",
        "status": "active",
        "lat": "-33.967",
        "lon": "-59.217",
        "geo_note": "Atucha nuclear complex, Buenos Aires Province (academic case study).",
        "evidence": "proxy",
        "source_id": "frontiers_hualong_argentina_2025",
        "note": "UNVERIFIED proxy. Frontiers open-access article states Argentina–China signed a turnkey EPC for Hualong-1 on 1 Feb 2022 with total investment USD 6.8 billion (85% Chinese bank finance). Secondary academic citation of the contract — not the signed PDF. Construction progress uncertain in later sources. Upgrades hunt_energy_fission_smr.",
    },
    {
        "id": "cnnc_atucha_hualong_epc_2022",
        "retrieved": "2026-10-01",
        "source_id": "frontiers_hualong_argentina_2025",
        "url": "https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2025.1668946/full",
        "price_year": "2022",
        "evidence": "proxy",
        "quote": "on 1 February 2022 Argentina and China formally signed a turnkey engineering, procurement and construction contract for the Hualong-1 reactor, with a total investment of USD 6.8 billion, of which 85% was again financed by Chinese banks.",
        "note": "Opened Frontiers full text; contract PDF not opened.",
    },
    {
        "id": "frontiers_hualong_argentina_2025",
        "type": "academic",
        "chicago": "“The Hualong-1 project in Argentina: a case study on the economic, technological, and geopolitical complexities of the belt and road initiative.” Frontiers in Political Science, 2025.",
        "url": "https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2025.1668946/full",
        "annotation": "Open-access academic article citing the Feb 2022 Hualong-1 EPC and USD 6.8bn figure. Treated as UNVERIFIED proxy for the contract value. Supports cnnc_atucha_hualong_epc_2022.",
        "supports": ["cnnc_atucha_hualong_epc_2022", "hunt_energy_fission_smr"],
    },
)

add(
    {
        "id": "sma_diego_almagro_sur_chile",
        "layer": "energy",
        "subcategory": "solar",
        "side": "allied",
        "counterpart": "Colbún S.A. — Diego de Almagro Sur PV (Atacama)",
        "country": "Chile",
        "asset": "SMA supply of 46 Medium Voltage Power Stations for 220 MW Diego de Almagro Sur PV",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2021",
        "status": "active",
        "lat": "-26.391",
        "lon": "-70.046",
        "geo_note": "Diego de Almagro Sur, Atacama Desert (SMA release).",
        "evidence": "documented",
        "source_id": "sma_atacama_order",
        "note": "Actor: SMA Solar Technology (German) — allied/other non-PRC. Company news: 46 MV Power Stations for 220 MW plant. No USD on page. Upgrades hunt_energy_solar. Complements existing Huawei Arinos PRC solar inverter row.",
    },
    {
        "id": "sma_diego_almagro_sur_chile",
        "retrieved": "2026-10-01",
        "source_id": "sma_atacama_order",
        "url": "https://www.sma.de/en/newsroom/news-details/sma-receives-order-for-large-scale-project-in-the-atacama-desert",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "SMA is supplying 46 Medium Voltage Power Station for the 220 megawatt Diego de Almagro Sur PV power plant in the Atacama Desert in Chile.",
        "note": "Opened SMA news page.",
    },
    {
        "id": "sma_atacama_order",
        "type": "official",
        "chicago": "SMA Solar Technology AG. “SMA receives order for large-scale project in the Atacama Desert.” Company news.",
        "url": "https://www.sma.de/en/newsroom/news-details/sma-receives-order-for-large-scale-project-in-the-atacama-desert",
        "annotation": "Company primary notice of inverter/MVPS supply for Colbún’s 220 MW Diego de Almagro Sur plant. Supports sma_diego_almagro_sur_chile.",
        "supports": ["sma_diego_almagro_sur_chile", "hunt_energy_solar"],
    },
)

add(
    {
        "id": "goldwind_pemuco_chile",
        "layer": "energy",
        "subcategory": "wind",
        "side": "prc",
        "counterpart": "ENGIE Chile — Pemuco wind farm (Ñuble)",
        "country": "Chile",
        "asset": "Goldwind supply of 22 × GWH182-7.5 MW turbines for 165 MW Pemuco wind farm",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-36.976",
        "lon": "-72.0",
        "geo_note": "Pemuco / Chillán area, Ñuble Region (Goldwind release: ~47 km south of Chillán).",
        "evidence": "documented",
        "source_id": "goldwind_pemuco_engie",
        "note": "Actor: Goldwind. Company news: contract with ENGIE Chile for 22 GWH182-7.5MW units; 165 MW. No USD on page. Upgrades hunt_energy_wind.",
    },
    {
        "id": "goldwind_pemuco_chile",
        "retrieved": "2026-10-01",
        "source_id": "goldwind_pemuco_engie",
        "url": "https://www.goldwind.com/en/news/focus-1117918927511560192/?id=1117920264764704768",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Goldwind has signed a cooperation contract with ENGIE Chile to supply 22 units of GWH182-7.5MW wind turbines for the Pemuco Wind Farm.",
        "note": "Opened Goldwind news page.",
    },
    {
        "id": "goldwind_pemuco_engie",
        "type": "official",
        "chicago": "Goldwind. “Goldwind Signs Contract with ENGIE Chile to Jointly Construct the Pemuco Wind Farm Project in Chile.” Company news.",
        "url": "https://www.goldwind.com/en/news/focus-1117918927511560192/?id=1117920264764704768",
        "annotation": "Company primary notice of 22×7.5 MW turbines for 165 MW Pemuco. Supports goldwind_pemuco_chile.",
        "supports": ["goldwind_pemuco_chile", "hunt_energy_wind"],
    },
)

add(
    {
        "id": "vestas_casa_dos_ventos_br_2023",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Casa dos Ventos — Serra do Tigre (RN) + Babilônia Centro (BA)",
        "country": "Brazil",
        "asset": "Vestas 1,310 MW supply-and-installation order (291 × V150-4.5 MW)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "-6.25",
        "lon": "-36.52",
        "geo_note": "Serra do Tigre, Rio Grande do Norte (company announcement). Second park in Bahia not dual-pinned.",
        "evidence": "documented",
        "source_id": "vestas_brazil_1310mw_20230330",
        "note": "Actor: Vestas (Danish) — allied/other. Company announcement 30 Mar 2023: 756+554 MW firm order. No USD on page.",
    },
    {
        "id": "vestas_casa_dos_ventos_br_2023",
        "retrieved": "2026-10-01",
        "source_id": "vestas_brazil_1310mw_20230330",
        "url": "https://www.vestas.com/en/media/company-news/2023/vestas-receives-1-310-mw-onshore-order-in-brazil-c3743452",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Number of MW: 756 MW (Serra do Tigre) + 554 MW (Babilônia Centro)",
        "note": "Opened Vestas company announcement.",
    },
    {
        "id": "vestas_brazil_1310mw_20230330",
        "type": "official",
        "chicago": "Vestas Wind Systems A/S. “Vestas receives 1,310 MW onshore order in Brazil.” Company Announcement No. 07/2023, 30 March 2023.",
        "url": "https://www.vestas.com/en/media/company-news/2023/vestas-receives-1-310-mw-onshore-order-in-brazil-c3743452",
        "annotation": "Company primary announcement of 1,310 MW Brazil order for Casa dos Ventos. Supports vestas_casa_dos_ventos_br_2023.",
        "supports": ["vestas_casa_dos_ventos_br_2023"],
    },
)

add(
    {
        "id": "ge_vernova_serra_tigre_ais_2023",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Casa dos Ventos — Serra do Tigre wind complex grid connection",
        "country": "Brazil",
        "asset": "GE Vernova Grid Solutions: two 500 kV AIS substations + connection bay for Serra do Tigre (756 MW)",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "-6.25",
        "lon": "-36.52",
        "geo_note": "Currais Novos / São Tomé, Rio Grande do Norte (GE Vernova release).",
        "evidence": "documented",
        "source_id": "gevernova_serra_tigre_ais_20230803",
        "note": "Actor: GE Vernova (U.S.). Company release 3 Aug 2023: two 500 kV AIS for Serra do Tigre; energization targeted end-2024. No USD on page. Upgrades hunt_br_power_equip / power_plants_grid.",
    },
    {
        "id": "ge_vernova_serra_tigre_ais_2023",
        "retrieved": "2026-10-01",
        "source_id": "gevernova_serra_tigre_ais_20230803",
        "url": "https://www.gevernova.com/news/press-releases/ge-vernova-grid-solutions-to-supply-air-insulated-substations-to-casa-dos-ventos-serra-do-tigre-wind-complex-brazil",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Grid Solutions... has signed a contract with Casa dos Ventos... to construct two 500 kV air-insulated substations (AIS) for the Serra do Tigre Wind Complex.",
        "note": "Opened GE Vernova press release.",
    },
    {
        "id": "gevernova_serra_tigre_ais_20230803",
        "type": "official",
        "chicago": "GE Vernova. “GE Vernova's Grid Solutions to supply air-insulated substations to Casa dos Ventos’ Serra do Tigre Wind Complex in Brazil.” 3 August 2023.",
        "url": "https://www.gevernova.com/news/press-releases/ge-vernova-grid-solutions-to-supply-air-insulated-substations-to-casa-dos-ventos-serra-do-tigre-wind-complex-brazil",
        "annotation": "U.S. company primary release on 500 kV AIS supply in Brazil. Supports ge_vernova_serra_tigre_ais_2023.",
        "supports": ["ge_vernova_serra_tigre_ais_2023", "hunt_br_power_equip"],
    },
)

add(
    {
        "id": "powerchina_chucas_cr_ref",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "Chucás Hydropower Station (Tárcoles River), Costa Rica",
        "country": "Costa Rica",
        "asset": "POWERCHINA Chucás 50 MW hydropower (completed 2018) — LatAm hydro reference presence",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "9.85",
        "lon": "-84.3",
        "geo_note": "Tárcoles River, ~40 km south of San José (POWERCHINA page).",
        "evidence": "documented",
        "source_id": "powerchina_chucas_20231024",
        "note": "Actor: POWERCHINA. Company page updated 24 Oct 2023 documents 50 MW Chucás (construction 2011–2018). COD is pre-2021; coded as documented presence/reference under other_renewables with observation year = page update year. No USD on page. Upgrades hunt_energy_other_renewables.",
    },
    {
        "id": "powerchina_chucas_cr_ref",
        "retrieved": "2026-10-01",
        "source_id": "powerchina_chucas_20231024",
        "url": "https://en.powerchina.cn/2023-10/24/c_828570.htm",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "The Chucas Hydropower Station is the first project in the field of hydropower cooperation between China and Costa Rica... total installed capacity of 50 megawatts... completed and handed over in 2018.",
        "note": "Opened POWERCHINA English project page.",
    },
    {
        "id": "powerchina_chucas_20231024",
        "type": "official",
        "chicago": "POWERCHINA. “Costa Rica Chucas Hydropower Station.” 24 October 2023.",
        "url": "https://en.powerchina.cn/2023-10/24/c_828570.htm",
        "annotation": "Company project page for 50 MW Chucás hydro in Costa Rica. Supports powerchina_chucas_cr_ref.",
        "supports": ["powerchina_chucas_cr_ref", "hunt_energy_other_renewables"],
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
            # merge supports
            existing = bib[bib_by[sid]]
            supports = set(existing.get("supports") or [])
            supports.update(bib_entry.get("supports") or [])
            existing["supports"] = sorted(supports)
            # keep stronger annotation/url if present
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

    # Update hunt notes for covered seeds
    hunt_updates = {
        "hunt_infra_port_ownership": "Cycle 1: logged cosco_chancay_port_2024 (documented Cosco Ports release).",
        "hunt_infra_port_cranes": "Cycle 1: logged zpmc_itapoa_rtg_2023 (ZPMC PR).",
        "hunt_infra_bridges_roads": "Cycle 1: logged chec_jamaica_spark_roads_2024 + crcc_demerara_bridge_2022.",
        "hunt_infra_building_materials": "Cycle 1: logged huaxin_embu_aggregates_br_2025 (HKEX).",
        "hunt_infra_engineering_epc": "Cycle 1: logged sinoma_loma_negra_amali_epc (CemNet/Sinoma).",
        "hunt_res_lithium": "Cycle 1: logged ganfeng_pastos_grandes_stake_2024 + ganfeng_lithea_ppg_2022.",
        "hunt_res_copper": "Cycle 1: logged mmg_las_bambas_peru + fcx_cerro_verde_peru.",
        "hunt_res_nickel": "Cycle 1: logged mmg_anglo_nickel_brazil_2025.",
        "hunt_res_dimension_stone": "Cycle 1: logged abirochas_br_stone_china_2023.",
        "hunt_res_balsa": "Cycle 1: logged wits_ecuador_balsa_china_2022 + wits_ecuador_balsa_us_2022.",
        "hunt_res_water": "Cycle 1: logged bechtel_qb2_desal_chile + ide_saddn_desal_chile_2023.",
        "hunt_fenb_araxa": "Cycle 1: logged cbmm_araxa_presence_2024 (presence; still hunting FeNb unit price).",
        "hunt_energy_fission_smr": "Cycle 1: logged cnnc_atucha_hualong_epc_2022 (UNVERIFIED proxy).",
        "hunt_energy_solar": "Cycle 1: logged sma_diego_almagro_sur_chile.",
        "hunt_energy_wind": "Cycle 1: logged goldwind_pemuco_chile + vestas_casa_dos_ventos_br_2023.",
        "hunt_br_power_equip": "Cycle 1: logged ge_vernova_serra_tigre_ais_2023 (U.S. grid AIS).",
        "hunt_energy_other_renewables": "Cycle 1: logged powerchina_chucas_cr_ref.",
        "hunt_latam_rail_telecom": "Cycle 1: no new rail award opened beyond existing SP metro / EFE rows; still hunting U.S.-seller rail pair.",
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
    print("Cycle 1 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
