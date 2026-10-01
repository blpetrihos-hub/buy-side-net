#!/usr/bin/env python3
"""Cycle 2 hunt: shuffle_seed=20261002; equal budget across 18 subcategories."""
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


# --- shuffled_order seed 20261002 ---
# 1 energy/solar
A(
    {
        "id": "jinko_brazil_module_imports_2023",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Brazil PV module import market (Greener ranking via Canal Solar)",
        "country": "Brazil",
        "asset": "JinkoSolar leading Brazil PV module imports in 2023 (3.402 MWp reported)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "National import aggregate; no plant pin.",
        "evidence": "proxy",
        "source_id": "canalsolar_greener_imports_2023",
        "note": "UNVERIFIED proxy. Canal Solar (22 Mar 2024) citing Greener: Jinko 3.402 MWp imports to Brazil in 2023. Consultancy ranking reprinted in press — not a customs microdata extract opened here. Upgrades hunt_energy_solar.",
    },
    {
        "id": "jinko_brazil_module_imports_2023",
        "retrieved": "2026-10-01",
        "source_id": "canalsolar_greener_imports_2023",
        "url": "https://canalsolar.com.br/en/ranking-of-most-imported-manufacturers-2023/",
        "price_year": "2023",
        "evidence": "proxy",
        "quote": "Jinko Solar appears in first place as the manufacturer that imported the most panels last year, with 3.402 MWp.",
        "note": "Opened Canal Solar English page.",
    },
    {
        "id": "canalsolar_greener_imports_2023",
        "type": "journalism",
        "chicago": "Badra, Mateus. “Ranking shows the manufacturers that imported the most modules in 2023.” Canal Solar, 22 March 2024.",
        "url": "https://canalsolar.com.br/en/ranking-of-most-imported-manufacturers-2023/",
        "annotation": "Press reprint of Greener Brazil module-import ranking (Jinko first). UNVERIFIED proxy. Supports jinko_brazil_module_imports_2023.",
        "supports": ["jinko_brazil_module_imports_2023", "hunt_energy_solar"],
    },
)

# 2 energy/fission_smr
A(
    {
        "id": "carem25_argentina_iaea_2025",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "other",
        "counterpart": "CNEA / CAREM-25 prototype (Atucha site), Argentina",
        "country": "Argentina",
        "asset": "CAREM-25 domestically designed SMR prototype — licensing/construction status in Argentina national nuclear safety report",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-33.967",
        "lon": "-59.217",
        "geo_note": "Atucha complex, Buenos Aires Province (national report context).",
        "evidence": "documented",
        "source_id": "iaea_argentina_nnr_2025",
        "note": "Actor: Argentine state program (other/host). IAEA-hosted National Nuclear Safety Report Argentina 2025 documents CAREM-25 licensing/construction. Not a U.S./PRC technology sale; host SMR program presence. No USD on opened pages. Complements cnnc_atucha_hualong_epc_2022.",
    },
    {
        "id": "carem25_argentina_iaea_2025",
        "retrieved": "2026-10-01",
        "source_id": "iaea_argentina_nnr_2025",
        "url": "https://www.iaea.org/sites/default/files/2026-01/national-report_argentina_2025.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "currently engaged in the licensing process of the CAREM 25 Prototype Reactor.",
        "note": "Opened IAEA-hosted national report PDF (173 pages).",
    },
    {
        "id": "iaea_argentina_nnr_2025",
        "type": "official",
        "chicago": "Argentina. “National Nuclear Safety Report Argentina 2025.” Submitted via IAEA, 2025.",
        "url": "https://www.iaea.org/sites/default/files/2026-01/national-report_argentina_2025.pdf",
        "annotation": "Official national report documenting CAREM-25 licensing/construction. Supports carem25_argentina_iaea_2025.",
        "supports": ["carem25_argentina_iaea_2025", "hunt_energy_fission_smr"],
    },
)

# 3 infrastructure/port_ownership
A(
    {
        "id": "hutchison_eit_ensenada_2022",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "other",
        "counterpart": "Hutchison Ports EIT — Ensenada container terminal expansion",
        "country": "Mexico",
        "asset": "Hutchison Ports EIT Ensenada terminal expansion (MXN 2,300 million stated investment)",
        "investment_type": "concession",
        "value": "2300000000",
        "currency": "MXN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2022",
        "status": "active",
        "lat": "31.8667",
        "lon": "-116.6167",
        "geo_note": "Port of Ensenada, Baja California (company newsroom).",
        "evidence": "documented",
        "source_id": "hutchison_eit_ensenada_news",
        "note": "Actor: Hutchison Ports (Hong Kong–based CK Hutchison group) — coded other (non-U.S., not PRC state). Company Mexico newsroom: MXN 2,300m expansion; works began 26 Dec 2022. USD left blank (no FX cited on page).",
    },
    {
        "id": "hutchison_eit_ensenada_2022",
        "retrieved": "2026-10-01",
        "source_id": "hutchison_eit_ensenada_news",
        "url": "https://www.hutchisonports.com.mx/newsroom/Hutchison-Ports-eit-invierte-2300-millones-de-pesos-en-ampliacion-de-su-Terminal",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "Con una inversión total de 2,300 millones de pesos destinados a la ampliación de su terminal en el Puerto de Ensenada... Las obras de ampliación del muelle y patios de Hutchison Ports EIT iniciaron el 26 de diciembre de 2022",
        "note": "Opened Hutchison Ports Mexico newsroom page.",
    },
    {
        "id": "hutchison_eit_ensenada_news",
        "type": "official",
        "chicago": "Hutchison Ports Mexico. “Hutchison Ports EIT invierte 2,300 millones de pesos en ampliación de su Terminal.” Company newsroom, 22 May 2023.",
        "url": "https://www.hutchisonports.com.mx/newsroom/Hutchison-Ports-eit-invierte-2300-millones-de-pesos-en-ampliacion-de-su-Terminal",
        "annotation": "Company primary notice of Ensenada terminal expansion investment. Supports hutchison_eit_ensenada_2022.",
        "supports": ["hutchison_eit_ensenada_2022", "hunt_infra_port_ownership"],
    },
)

# 4 infrastructure/rail
A(
    {
        "id": "crrc_ba_line_b_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "prc",
        "counterpart": "SBASE — Buenos Aires Metro Line B rolling stock (LPI 234/2023)",
        "country": "Argentina",
        "asset": "CRRC Changchun award for Line B rolling stock — USD 263,185,329.76 CIF",
        "investment_type": "equipment_supply",
        "value": "263185329.76",
        "currency": "USD",
        "value_usd": "263185329.76",
        "fx_usd": "1",
        "fx_date": "2025-05-16",
        "year": "2025",
        "status": "active",
        "lat": "-34.6037",
        "lon": "-58.3816",
        "geo_note": "Buenos Aires Metro Line B (city process pin).",
        "evidence": "documented",
        "source_id": "sbase_lpi234_adjudicacion_2025",
        "note": "Actor: CRRC Changchun Railway Vehicles. SBASE adjudication resolution awards LPI 234/2023 at USD 263,185,329.76 CIF. Upgrades hunt_latam_rail_telecom.",
    },
    {
        "id": "crrc_ba_line_b_2025",
        "retrieved": "2026-10-01",
        "source_id": "sbase_lpi234_adjudicacion_2025",
        "url": "https://static.buenosaires.gob.ar/sites/default/files/2025-07/LPI%20234.23%20-%20Resoluci%C3%B3n%20de%20Adjudicaci%C3%B3n%20-%20RESDI-2025-87-GCABA-SBASE.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Adjudicar la Licitación Pública Internacional N° 234/2023 ... a favor de la firma CRRC CHANGCHUN RAILWAY VEHICLES CO. LTD. ... (USD 263.185.329,76) Condición CIF",
        "note": "Opened SBASE adjudication PDF (4 pages).",
    },
    {
        "id": "sbase_lpi234_adjudicacion_2025",
        "type": "official",
        "chicago": "SBASE (Subterráneos de Buenos Aires). Resolución de adjudicación, Licitación Pública Internacional N° 234/2023 (Material rodante Línea B). 2025.",
        "url": "https://static.buenosaires.gob.ar/sites/default/files/2025-07/LPI%20234.23%20-%20Resoluci%C3%B3n%20de%20Adjudicaci%C3%B3n%20-%20RESDI-2025-87-GCABA-SBASE.pdf",
        "annotation": "Official award of Buenos Aires Line B rolling stock to CRRC Changchun at USD 263.2m CIF. Supports crrc_ba_line_b_2025.",
        "supports": ["crrc_ba_line_b_2025", "hunt_latam_rail_telecom"],
    },
)

A(
    {
        "id": "alstom_mexico_dmu_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "ARTF / Mexico passenger rail corridors (CDMX–Querétaro–Irapuato; Saltillo–Monterrey–Nuevo Laredo)",
        "country": "Mexico",
        "asset": "Alstom supply of 47 DMU passenger trains + 5-year maintenance (~MXN 20.2 billion)",
        "investment_type": "equipment_supply",
        "value": "20200000000",
        "currency": "MXN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "19.4326",
        "lon": "-99.1332",
        "geo_note": "Mexico City process pin for ARTF award (corridors are multi-city).",
        "evidence": "documented",
        "source_id": "alstom_mexico_47trains_20251226",
        "note": "Actor: Alstom (French) — allied. Company release 26 Dec 2025: ~MXN 20.2bn (~€920m stated). Stored MXN figure; USD blank without cited FX on page.",
    },
    {
        "id": "alstom_mexico_dmu_2025",
        "retrieved": "2026-10-01",
        "source_id": "alstom_mexico_47trains_20251226",
        "url": "https://www.alstom.com/press-releases-news/2025/12/alstom-supply-47-trains-and-associated-maintenance-new-rail-corridors-mexico",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The contract is valued at approximately 20,2 billion Mexican pesos (approximately 920 million euros)",
        "note": "Opened Alstom press release.",
    },
    {
        "id": "alstom_mexico_47trains_20251226",
        "type": "official",
        "chicago": "Alstom. “Alstom to supply 47 trains and associated maintenance for new rail corridors in Mexico.” 26 December 2025.",
        "url": "https://www.alstom.com/press-releases-news/2025/12/alstom-supply-47-trains-and-associated-maintenance-new-rail-corridors-mexico",
        "annotation": "Company primary release on MXN 20.2bn / 47 DMU Mexico award. Supports alstom_mexico_dmu_2025.",
        "supports": ["alstom_mexico_dmu_2025", "hunt_latam_rail_telecom"],
    },
)

# 5 resources/copper
A(
    {
        "id": "chinalco_toromocho_peru",
        "layer": "resources",
        "subcategory": "copper",
        "side": "prc",
        "counterpart": "Minera Chinalco Perú — Toromocho copper mine (Junín)",
        "country": "Peru",
        "asset": "Toromocho copper mine owned/operated by Chinalco Peru",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-11.6",
        "lon": "-76.14",
        "geo_note": "Toromocho / Morococha district, Junín (company history page).",
        "evidence": "documented",
        "source_id": "chinalco_peru_history",
        "note": "Actor: Chinalco (PRC SOE). Company history page documents Toromocho ownership and operations. No new acquisition USD on this page. Complements mmg_las_bambas_peru / fcx_cerro_verde_peru.",
    },
    {
        "id": "chinalco_toromocho_peru",
        "retrieved": "2026-10-01",
        "source_id": "chinalco_peru_history",
        "url": "https://www.chinalco.com.pe/en/our-history",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "In 2007 Aluminum Corporation of China (CHINALCO) created Mineria Chinalco Peru S.A. (Chinalco Peru) in order to construct, develop and operate the copper mega-project Toromocho.",
        "note": "Opened Chinalco Peru history page.",
    },
    {
        "id": "chinalco_peru_history",
        "type": "official",
        "chicago": "Chinalco Peru. “Our History.” Company page. Accessed 1 October 2026.",
        "url": "https://www.chinalco.com.pe/en/our-history",
        "annotation": "Company primary history of Toromocho ownership. Supports chinalco_toromocho_peru.",
        "supports": ["chinalco_toromocho_peru", "hunt_res_copper"],
    },
)

# 6 resources/nickel — Anglo American seller-side (allied) documenting Brazil Ni assets
A(
    {
        "id": "anglo_brazil_nickel_sale_2025",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "Anglo American Nickel Brazil (Barro Alto, Codemin / Niquelândia) — SPA to MMG",
        "country": "Brazil",
        "asset": "Anglo American Brazil nickel business (Barro Alto + Codemin) agreed sale up to USD 500m to MMG",
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
        "geo_note": "Barro Alto / Niquelândia nickel belt, Goiás (Anglo release).",
        "evidence": "documented",
        "source_id": "anglo_nickel_sale_20250218",
        "note": "Actor: Anglo American (UK) — allied seller documenting Brazil Ni ops subject to SPA. Complements mmg_anglo_nickel_brazil_2025 (PRC buyer). Same headline USD 500m; completion still conditional. Pair_id left blank (not a matched buy-side gap).",
    },
    {
        "id": "anglo_brazil_nickel_sale_2025",
        "retrieved": "2026-10-01",
        "source_id": "anglo_nickel_sale_20250218",
        "url": "https://www.angloamerican.com/media/press-releases/2025/18-02-2025a",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Anglo American plc (“Anglo American”) announces that it has entered into a definitive agreement to sell its nickel business to MMG Singapore Resources Pte. Ltd... for a cash consideration of up to $500 million... The nickel business comprises two ferronickel operations in Brazil – Barro Alto and Codemin",
        "note": "Opened Anglo American press release.",
    },
    {
        "id": "anglo_nickel_sale_20250218",
        "type": "official",
        "chicago": "Anglo American plc. “Anglo American agrees sale of nickel business for up to $500 million.” 18 February 2025.",
        "url": "https://www.angloamerican.com/media/press-releases/2025/18-02-2025a",
        "annotation": "Seller-side primary release on Brazil nickel SPA to MMG. Supports anglo_brazil_nickel_sale_2025.",
        "supports": ["anglo_brazil_nickel_sale_2025", "hunt_res_nickel"],
    },
)

# 7 infrastructure/bridges_roads — CHEC SCHIP Jamaica
A(
    {
        "id": "chec_jamaica_schip_bri",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "CHEC Americas — Jamaica Southern Coastal Highway Improvement Project (SCHIP)",
        "country": "Jamaica",
        "asset": "SCHIP Sections A and B-ii design/construct by CHEC Americas (BRI framework)",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "17.9714",
        "lon": "-76.7931",
        "geo_note": "Southern coastal Jamaica corridor (company project page; Kingston process pin).",
        "evidence": "documented",
        "source_id": "chec_americas_schip",
        "note": "Actor: CHEC Americas (PRC). Company project page: design/construction of Sections A and B-ii; first project under China–Jamaica BRI framework. No USD on page. Complements chec_jamaica_spark_roads_2024.",
    },
    {
        "id": "chec_jamaica_schip_bri",
        "retrieved": "2026-10-01",
        "source_id": "chec_americas_schip",
        "url": "https://www.checamerica.com/projects-jamaica-schip/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "CHEC Americas responsible for the design and construction of Sections A and B-ii. As the first project launched under the Belt and Road Framework Agreement between the governments of China and Jamaica",
        "note": "Opened CHEC Americas SCHIP project page.",
    },
    {
        "id": "chec_americas_schip",
        "type": "official",
        "chicago": "CHEC Americas. “Southern Coastal Highway Improvement Project.” Company project page. Accessed 1 October 2026.",
        "url": "https://www.checamerica.com/projects-jamaica-schip/",
        "annotation": "Company primary description of SCHIP Sections A/B-ii. Supports chec_jamaica_schip_bri.",
        "supports": ["chec_jamaica_schip_bri", "hunt_infra_bridges_roads"],
    },
)

# 8 energy/power_plants_grid
A(
    {
        "id": "ge_vernova_transelec_sync_chile_2024",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Transelec — Ana María and Monte Mina substations (Northern Chile)",
        "country": "Chile",
        "asset": "GE Vernova: four synchronous condensers + 220 kV HV substations for Ana María and Monte Mina",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-22.45",
        "lon": "-68.93",
        "geo_note": "Northern Chile grid (company release; approximate Antofagasta-region pin).",
        "evidence": "documented",
        "source_id": "gevernova_transelec_sync_20240712",
        "note": "Actor: GE Vernova (U.S.). Company release 12 Jul 2024: four sync condensers + 220 kV GIS/transformers for Transelec Ana María / Monte Mina; COD targeted 2027. No USD on page. Complements ge_vernova_serra_tigre_ais_2023.",
    },
    {
        "id": "ge_vernova_transelec_sync_chile_2024",
        "retrieved": "2026-10-01",
        "source_id": "gevernova_transelec_sync_20240712",
        "url": "https://www.gevernova.com/news/press-releases/ge-vernova-synchronous-condenser-equipment-grid-stability",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "GE Vernova Inc. ... has secured an order with Transelec Holdings Rentas Ltd ... to deliver synchronous condensers and high-voltage substation for the Ana Maria and Monte Mina substation projects in Northern Chile.",
        "note": "Opened GE Vernova press release.",
    },
    {
        "id": "gevernova_transelec_sync_20240712",
        "type": "official",
        "chicago": "GE Vernova. “GE Vernova to supply synchronous condensers equipment to help improve grid stability in Northern Chile.” 12 July 2024.",
        "url": "https://www.gevernova.com/news/press-releases/ge-vernova-synchronous-condenser-equipment-grid-stability",
        "annotation": "Company primary release on Transelec sync-condenser / HV order. Supports ge_vernova_transelec_sync_chile_2024.",
        "supports": ["ge_vernova_transelec_sync_chile_2024", "hunt_br_power_equip", "hunt_cl_power_equip"],
    },
)

# 9 resources/water
A(
    {
        "id": "ide_aconcagua_desal_chile_2023",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Aguas Pacífico SpA — Aconcagua desalination plant (Quintero Bay / Valparaíso)",
        "country": "Chile",
        "asset": "IDE Technologies EPC/construction start — Aconcagua SWRO 86,400 m³/day",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "-32.783",
        "lon": "-71.533",
        "geo_note": "Quintero bay area, Valparaíso Region (IDE release).",
        "evidence": "documented",
        "source_id": "ide_aconcagua_20230320",
        "note": "Actor: IDE Technologies (Israeli) — allied/other non-PRC. Company release 20 Mar 2023: construction commenced; 86,400 m³/day; developer Aguas Pacífico (Patria). No USD on page. Complements ide_saddn_desal_chile_2023 / bechtel_qb2_desal_chile.",
    },
    {
        "id": "ide_aconcagua_desal_chile_2023",
        "retrieved": "2026-10-01",
        "source_id": "ide_aconcagua_20230320",
        "url": "https://ide-tech.com/en/ide-technologies-commences-construction-of-the-aconcagua-desalination-plant-in-the-valparaiso-region-of-chile/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "IDE Technologies ... commenced construction of the Aconcagua Desalination Plant with a capacity of 86,400 m3/day located in the Quintero bay area of Chile.",
        "note": "Opened IDE Technologies press page.",
    },
    {
        "id": "ide_aconcagua_20230320",
        "type": "official",
        "chicago": "IDE Technologies. “IDE Technologies Commences Construction of the Aconcagua Desalination Plant in the Valparaiso Region of Chile.” 20 March 2023.",
        "url": "https://ide-tech.com/en/ide-technologies-commences-construction-of-the-aconcagua-desalination-plant-in-the-valparaiso-region-of-chile/",
        "annotation": "Company primary notice of Aconcagua desal construction start. Supports ide_aconcagua_desal_chile_2023.",
        "supports": ["ide_aconcagua_desal_chile_2023", "hunt_res_water"],
    },
)

# 10 resources/lithium
A(
    {
        "id": "codelco_sqm_novaandino_2025",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "other",
        "counterpart": "Codelco / SQM — Nova Andino Litio SpA (Salar de Atacama)",
        "country": "Chile",
        "asset": "Nova Andino Litio JV formed by merger of Minera Tarar (Codelco) into SQM Salar — Atacama lithium through 2060",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-23.5",
        "lon": "-68.25",
        "geo_note": "Salar de Atacama (Codelco release).",
        "evidence": "documented",
        "source_id": "codelco_sqm_novaandino_20251227",
        "note": "Actor: Chilean state Codelco + SQM (Chilean-listed; Tianqi minority history) — coded other (host public–private JV). Codelco release 27 Dec 2025: Nova Andino Litio formed; majority state participation stated. No transaction USD on page. Complements ganfeng Argentina rows.",
    },
    {
        "id": "codelco_sqm_novaandino_2025",
        "retrieved": "2026-10-01",
        "source_id": "codelco_sqm_novaandino_20251227",
        "url": "https://www.codelco.com/en/prensa/2025/codelco-y-sqm-forman-novaandino-litio-la-sociedad-conjunta-para-el",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Codelco and SQM announced the creation of Nova Andino Litio SpA, resulting from the merger between their subsidiaries Minera Tarar SpA and SQM Salar SpA, respectively, formally establishing the joint venture that will develop ... lithium in the Salar de Atacama until 2060.",
        "note": "Opened Codelco English press page.",
    },
    {
        "id": "codelco_sqm_novaandino_20251227",
        "type": "official",
        "chicago": "Codelco. “Codelco and SQM form NovaAndino Litio, the joint venture for the development of lithium in the Salar de Atacama.” 27 December 2025.",
        "url": "https://www.codelco.com/en/prensa/2025/codelco-y-sqm-forman-novaandino-litio-la-sociedad-conjunta-para-el",
        "annotation": "Official Codelco notice of Nova Andino Litio JV formation. Supports codelco_sqm_novaandino_2025.",
        "supports": ["codelco_sqm_novaandino_2025", "hunt_res_lithium"],
    },
)

# 11 resources/graphite — Acciona not stone. Use miss documented in HUNT_STATE.
# Prefer a sourced row: Brazilian stone trade press is thin; open ABIROCHAS PDF again for US destination if present is duplicate family.
# Record no new distinct stone row this cycle (budget spent opening ABIROCHAS + trade searches → miss).

# 12 infrastructure/port_cranes — ZPMC at DP World Lirquén (trade press → proxy)
A(
    {
        "id": "zpmc_dpworld_lirquen_2022",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "DP World Lirquén — Super Post-Panamax quay cranes",
        "country": "Chile",
        "asset": "Two ZPMC Super Post-Panamax quay cranes received at DP World Lirquén (part of ~USD 45m terminal investment stated)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2022",
        "status": "active",
        "lat": "-36.711",
        "lon": "-72.983",
        "geo_note": "Puerto Lirquén, Biobío Region (Seatrade report).",
        "evidence": "proxy",
        "source_id": "seatrade_dpworld_lirquen_20220720",
        "note": "UNVERIFIED proxy. Seatrade Maritime journalism (20 Jul 2022) reporting ZPMC Super Post-Panamax cranes at DP World Lirquén; ~USD 45m investment attributed to terminal GM quote. Not a ZPMC primary filing. Complements zpmc_itapoa_rtg_2023.",
    },
    {
        "id": "zpmc_dpworld_lirquen_2022",
        "retrieved": "2026-10-01",
        "source_id": "seatrade_dpworld_lirquen_20220720",
        "url": "https://www.seatrade-maritime.com/ports-logistics/dp-world-lirquen-receives-first-quay-cranes",
        "price_year": "2022",
        "evidence": "proxy",
        "quote": "DP World Lirquen, in Chile, has received the first two Super Post Panamax cranes from Chinese manufacturer ZPMC. ... A third similar crane will be added and the port equipment form part of a $45m investment.",
        "note": "Opened Seatrade Maritime page.",
    },
    {
        "id": "seatrade_dpworld_lirquen_20220720",
        "type": "journalism",
        "chicago": "Labrut, Michèle. “DP World Lirquen receives first quay cranes.” Seatrade Maritime, 20 July 2022.",
        "url": "https://www.seatrade-maritime.com/ports-logistics/dp-world-lirquen-receives-first-quay-cranes",
        "annotation": "Trade press on ZPMC quay cranes at Lirquén. UNVERIFIED proxy. Supports zpmc_dpworld_lirquen_2022.",
        "supports": ["zpmc_dpworld_lirquen_2022", "hunt_infra_port_cranes"],
    },
)

# 13 energy/other_renewables — Ormat Guatemala geothermal (U.S.)
A(
    {
        "id": "ormat_amatitlan_guatemala",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "Ormat Technologies — Amatitlán geothermal plant",
        "country": "Guatemala",
        "asset": "Ormat-owned Amatitlán geothermal power plant (listed on company global projects page)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "14.48",
        "lon": "-90.62",
        "geo_note": "Amatitlán, Guatemala (company projects listing).",
        "evidence": "documented",
        "source_id": "ormat_global_projects_guatemala",
        "note": "Actor: Ormat Technologies (U.S.). Company global projects page lists Amatitlan Guatemala among operating geothermal assets. Presence/ownership documentation; no new transaction USD on page. Complements powerchina_chucas_cr_ref.",
    },
    {
        "id": "ormat_amatitlan_guatemala",
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
        "annotation": "Company project listing of Ormat Guatemala geothermal plants. Supports ormat_amatitlan_guatemala.",
        "supports": ["ormat_amatitlan_guatemala", "hunt_energy_other_renewables"],
    },
)

# 14 energy/wind
A(
    {
        "id": "nordex_auren_cajuina3_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Auren Energia — Cajuína 3 wind farm (Rio Grande do Norte)",
        "country": "Brazil",
        "asset": "Nordex supply/install 19 × N163/5.X turbines (112 MW) + 15-year service for Cajuína 3",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-5.7",
        "lon": "-36.25",
        "geo_note": "Lajes municipality, Rio Grande do Norte (Nordex release).",
        "evidence": "documented",
        "source_id": "nordex_auren_112mw_20250303",
        "note": "Actor: Nordex (German) — allied. Company release 3 Mar 2025: 112 MW / 19 N163/5.X; install from early 2026; COD autumn 2026. No USD on page. Complements vestas / goldwind wind rows.",
    },
    {
        "id": "nordex_auren_cajuina3_2025",
        "retrieved": "2026-10-01",
        "source_id": "nordex_auren_112mw_20250303",
        "url": "https://www.nordex-online.com/en/2025/03/nordex-group-receives-order-in-brazil-from-auren-energia-for-112-mw/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Auren Energia has commissioned the Nordex Group to supply and install 19 N163/5.X turbines. The 112 MW order includes the service for the turbines for an initial period of fifteen years",
        "note": "Opened Nordex press release.",
    },
    {
        "id": "nordex_auren_112mw_20250303",
        "type": "official",
        "chicago": "Nordex SE. “Nordex Group receives order in Brazil from Auren Energia for 112 MW.” 3 March 2025.",
        "url": "https://www.nordex-online.com/en/2025/03/nordex-group-receives-order-in-brazil-from-auren-energia-for-112-mw/",
        "annotation": "Company primary wind order notice for Cajuína 3. Supports nordex_auren_cajuina3_2025.",
        "supports": ["nordex_auren_cajuina3_2025", "hunt_energy_wind"],
    },
)

# 15 resources/niobium
A(
    {
        "id": "cmoc_catalao_niobium_br",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "prc",
        "counterpart": "CMOC Brasil — NML niobium mine (Catalão, Goiás)",
        "country": "Brazil",
        "asset": "CMOC 100% owned NML niobium mine / ferro-niobium production at Catalão",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-18.17",
        "lon": "-47.95",
        "geo_note": "Catalão, Goiás (CMOC company page).",
        "evidence": "documented",
        "source_id": "cmoc_brazil_nb_p_page",
        "note": "Actor: CMOC (PRC). Company Brazil Nb/P page: 100% NML niobium mine; 2025 production 10,348 t Nb stated. Presence/ops documentation; no acquisition USD on page. Complements cbmm_araxa_presence_2024.",
    },
    {
        "id": "cmoc_catalao_niobium_br",
        "retrieved": "2026-10-01",
        "source_id": "cmoc_brazil_nb_p_page",
        "url": "https://en.cmoc.com/html/Business/BRA-Nb-P/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "CMOC indirectly holds a 100% stake in NML niobium mine in Brazil... Geographic location Catalão, Goiás, Brazil... Production in 2025 Nb 10,348 tonnes",
        "note": "Opened CMOC English Brazil Nb/P business page.",
    },
    {
        "id": "cmoc_brazil_nb_p_page",
        "type": "official",
        "chicago": "CMOC Group Limited. “Brazil - niobium and phosphate.” Company page. Accessed 1 October 2026.",
        "url": "https://en.cmoc.com/html/Business/BRA-Nb-P/",
        "annotation": "Company primary description of Catalão NML niobium ownership/production. Supports cmoc_catalao_niobium_br.",
        "supports": ["cmoc_catalao_niobium_br", "hunt_fenb_araxa", "hunt_res_nickel"],
    },
)

# 16 resources/balsa — WITS 2023 China + US
A(
    {
        "id": "wits_ecuador_balsa_china_2023",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "prc",
        "counterpart": "China — Ecuador HS 440723 sawn balsa/related wood imports (WITS/Comtrade)",
        "country": "Ecuador",
        "asset": "Ecuador 2023 exports of HS 440723 to China — USD 66.225 million (WITS)",
        "investment_type": "other",
        "value": "66225180",
        "currency": "USD",
        "value_usd": "66225180",
        "fx_usd": "1",
        "fx_date": "2023-12-31",
        "year": "2023",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "National trade aggregate; no site pin.",
        "evidence": "documented",
        "source_id": "wits_ecu_440723_2023",
        "note": "Trade flow (not equity). WITS/Comtrade mirror for Ecuador HS 440723 exports to China in 2023. Complements 2022 WITS balsa rows. Product basket includes related tropical sawn woods under HS 440723.",
    },
    {
        "id": "wits_ecuador_balsa_china_2023",
        "retrieved": "2026-10-01",
        "source_id": "wits_ecu_440723_2023",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2023/tradeflow/Exports/partner/ALL/product/440723",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Ecuador exported Baboen, Mahogany, Imbuia and Balsa wood, sawn l to China ($66,225.18K , 27 m³)",
        "note": "Opened WITS Comtrade mirror page for ECU 2023 HS 440723.",
    },
    {
        "id": "wits_ecu_440723_2023",
        "type": "official",
        "chicago": "World Bank WITS / UN Comtrade. “Ecuador Baboen, Mahogany, Imbuia and Balsa wood, sawn l exports by country | 2023.” HS 440723.",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2023/tradeflow/Exports/partner/ALL/product/440723",
        "annotation": "Official trade mirror for Ecuador HS 440723 2023 exports. Supports wits_ecuador_balsa_china_2023 and wits_ecuador_balsa_us_2023.",
        "supports": [
            "wits_ecuador_balsa_china_2023",
            "wits_ecuador_balsa_us_2023",
            "hunt_res_balsa",
        ],
    },
)

A(
    {
        "id": "wits_ecuador_balsa_us_2023",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "us",
        "counterpart": "United States — Ecuador HS 440723 sawn balsa/related wood imports (WITS/Comtrade)",
        "country": "Ecuador",
        "asset": "Ecuador 2023 exports of HS 440723 to United States — USD 13.520 million (WITS)",
        "investment_type": "other",
        "value": "13520010",
        "currency": "USD",
        "value_usd": "13520010",
        "fx_usd": "1",
        "fx_date": "2023-12-31",
        "year": "2023",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "National trade aggregate; no site pin.",
        "evidence": "documented",
        "source_id": "wits_ecu_440723_2023",
        "note": "Trade flow (not equity). WITS/Comtrade mirror for Ecuador HS 440723 exports to United States in 2023. Complements 2022 WITS balsa rows.",
    },
    {
        "id": "wits_ecuador_balsa_us_2023",
        "retrieved": "2026-10-01",
        "source_id": "wits_ecu_440723_2023",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2023/tradeflow/Exports/partner/ALL/product/440723",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Ecuador exported Baboen, Mahogany, Imbuia and Balsa wood, sawn l to ... United States ($13,520.01K , 3 m³)",
        "note": "Opened same WITS page; US partner row.",
    },
    {
        "id": "wits_ecu_440723_2023",
        "type": "official",
        "chicago": "World Bank WITS / UN Comtrade. “Ecuador Baboen, Mahogany, Imbuia and Balsa wood, sawn l exports by country | 2023.” HS 440723.",
        "url": "https://wits.worldbank.org/trade/comtrade/en/country/ECU/year/2023/tradeflow/Exports/partner/ALL/product/440723",
        "annotation": "Official trade mirror for Ecuador HS 440723 2023 exports. Supports wits_ecuador_balsa_china_2023 and wits_ecuador_balsa_us_2023.",
        "supports": [
            "wits_ecuador_balsa_china_2023",
            "wits_ecuador_balsa_us_2023",
            "hunt_res_balsa",
        ],
    },
)

# 17 infrastructure/building_materials — Sinoma Votorantim Z02 (trade press → proxy)
A(
    {
        "id": "sinoma_votorantim_z02_br_2024",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "prc",
        "counterpart": "Votorantim Cimentos — Z02 cement grinding station (Edealina, Brazil)",
        "country": "Brazil",
        "asset": "Sinoma Overseas engineering/supply contract for 150 tph Z02 grinding expansion (project cost BRL 200m / ~USD 36.47m stated in trade press)",
        "investment_type": "epc",
        "value": "36470000",
        "currency": "USD",
        "value_usd": "36470000",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-17.42",
        "lon": "-49.66",
        "geo_note": "Edealina, Goiás (CemNet report).",
        "evidence": "proxy",
        "source_id": "cemnet_sinoma_votorantim_z02_20240917",
        "note": "UNVERIFIED proxy. CemNet trade press (17 Sep 2024) reporting Sinoma Overseas contract with Votorantim for Z02; BRL200m / US$36.47m figures from press — not a Sinoma or Votorantim primary filing opened here. Complements sinoma_loma_negra_amali_epc / huaxin_embu.",
    },
    {
        "id": "sinoma_votorantim_z02_br_2024",
        "retrieved": "2026-10-01",
        "source_id": "cemnet_sinoma_votorantim_z02_20240917",
        "url": "https://www.cemnet.com/News/story/177749/sinoma-overseas-to-build-votorantim-z02-grinding-plant.html",
        "price_year": "2024",
        "evidence": "proxy",
        "quote": "Sinoma Overseas has secured an engineering and supply contract for the Z02 cement grinding station project in Edealina Brazil... 150tph cement grinding expansion project costing BRL200m (US$36.47m).",
        "note": "Opened CemNet news page.",
    },
    {
        "id": "cemnet_sinoma_votorantim_z02_20240917",
        "type": "journalism",
        "chicago": "Bell, Peter. “Sinoma Overseas to build Votorantim Z02 grinding plant.” CemNet, 17 September 2024.",
        "url": "https://www.cemnet.com/News/story/177749/sinoma-overseas-to-build-votorantim-z02-grinding-plant.html",
        "annotation": "Trade press on Sinoma–Votorantim Z02 grinding contract. UNVERIFIED proxy. Supports sinoma_votorantim_z02_br_2024.",
        "supports": ["sinoma_votorantim_z02_br_2024", "hunt_infra_building_materials"],
    },
)

# 18 infrastructure/engineering_epc
A(
    {
        "id": "fluor_salares_norte_chile_2024",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Gold Fields — Salares Norte mining project (Atacama)",
        "country": "Chile",
        "asset": "Fluor EPCM for Salares Norte — first gold announced April 2024",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-26.0",
        "lon": "-69.0",
        "geo_note": "Atacama Region, northern Chile (Fluor release; high-Andes site).",
        "evidence": "documented",
        "source_id": "fluor_salares_norte_20240403",
        "note": "Actor: Fluor (U.S.). Company release 3 Apr 2024: Fluor EPCM; first gold achieved; ~350koz Au/yr expected. No contract USD on page. Complements bechtel_qb2 / sinoma EPC rows under engineering_epc mandate (non-grid).",
    },
    {
        "id": "fluor_salares_norte_chile_2024",
        "retrieved": "2026-10-01",
        "source_id": "fluor_salares_norte_20240403",
        "url": "https://newsroom.fluor.com/news-releases/news-details/2024/Fluor-Announces-First-Gold-from-Gold-Fields-Salares-Norte-Mining-Project-in-Chile/default.aspx",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Fluor Corporation’s (NYSE: FLR) Mining & Metals business announced today that first gold has been achieved at Gold Fields’ Salares Norte mining project in Chile. ... Fluor is responsible for the engineering, procurement and construction management of the project.",
        "note": "Opened Fluor newsroom release.",
    },
    {
        "id": "fluor_salares_norte_20240403",
        "type": "official",
        "chicago": "Fluor Corporation. “Fluor Announces First Gold from Gold Fields’ Salares Norte Mining Project in Chile.” 3 April 2024.",
        "url": "https://newsroom.fluor.com/news-releases/news-details/2024/Fluor-Announces-First-Gold-from-Gold-Fields-Salares-Norte-Mining-Project-in-Chile/default.aspx",
        "annotation": "Company primary EPCM milestone release for Salares Norte. Supports fluor_salares_norte_chile_2024.",
        "supports": ["fluor_salares_norte_chile_2024", "hunt_infra_engineering_epc"],
    },
)

A(
    {
        "id": "bechtel_los_pelambres_inco_2024",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Antofagasta Minerals — Los Pelambres INCO MLP expansion",
        "country": "Chile",
        "asset": "Bechtel EPC for Los Pelambres INCO MLP (concentrator expansion + 400 l/s desal + pipeline); inaugurated March 2024",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-31.72",
        "lon": "-71.25",
        "geo_note": "Los Pelambres / Coquimbo Region (Bechtel project page).",
        "evidence": "documented",
        "source_id": "bechtel_los_pelambres_page",
        "note": "Actor: Bechtel (U.S.). Company project page: INCO MLP inaugurated March 2024; EPC for concentrator expansion, 400 l/s desal, 65 km pipeline. No contract USD on page. Dual-use with water layer narrative; coded engineering_epc (mine EPC).",
    },
    {
        "id": "bechtel_los_pelambres_inco_2024",
        "retrieved": "2026-10-01",
        "source_id": "bechtel_los_pelambres_page",
        "url": "https://www.bechtel.com/projects/los-pelambres-copper-mine/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "In early 2019, Bechtel began construction of the INCO MLP project at Los Pelambres, which was inaugurated in March 2024. The project considered EPC direct hire for a concentrator plant expansion, a desalinated water plant and a water pipeline.",
        "note": "Opened Bechtel Los Pelambres project page.",
    },
    {
        "id": "bechtel_los_pelambres_page",
        "type": "official",
        "chicago": "Bechtel. “Los Pelambres Copper Mine.” Company project page. Accessed 1 October 2026.",
        "url": "https://www.bechtel.com/projects/los-pelambres-copper-mine/",
        "annotation": "Company primary project description of INCO MLP EPC. Supports bechtel_los_pelambres_inco_2024.",
        "supports": ["bechtel_los_pelambres_inco_2024", "hunt_infra_engineering_epc"],
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
        "hunt_energy_solar": "Cycle 2: logged jinko_brazil_module_imports_2023 (Canal Solar/Greener proxy).",
        "hunt_energy_fission_smr": "Cycle 2: logged carem25_argentina_iaea_2025 (IAEA national report).",
        "hunt_infra_port_ownership": "Cycle 2: logged hutchison_eit_ensenada_2022.",
        "hunt_latam_rail_telecom": "Cycle 2: logged crrc_ba_line_b_2025 + alstom_mexico_dmu_2025.",
        "hunt_res_copper": "Cycle 2: logged chinalco_toromocho_peru.",
        "hunt_res_nickel": "Cycle 2: logged anglo_brazil_nickel_sale_2025 (allied seller-side).",
        "hunt_infra_bridges_roads": "Cycle 2: logged chec_jamaica_schip_bri.",
        "hunt_br_power_equip": "Cycle 2: logged ge_vernova_transelec_sync_chile_2024.",
        "hunt_cl_power_equip": "Cycle 2: logged ge_vernova_transelec_sync_chile_2024.",
        "hunt_res_water": "Cycle 2: logged ide_aconcagua_desal_chile_2023.",
        "hunt_res_lithium": "Cycle 2: logged codelco_sqm_novaandino_2025.",
        "hunt_res_graphite": "Cycle 2: budget spent; no new distinct stone source opened beyond cycle-1 ABIROCHAS (miss).",
        "hunt_infra_port_cranes": "Cycle 2: logged zpmc_dpworld_lirquen_2022 (Seatrade proxy).",
        "hunt_energy_other_renewables": "Cycle 2: logged ormat_amatitlan_guatemala.",
        "hunt_energy_wind": "Cycle 2: logged nordex_auren_cajuina3_2025.",
        "hunt_fenb_araxa": "Cycle 2: logged cmoc_catalao_niobium_br (CMOC Catalão presence).",
        "hunt_res_balsa": "Cycle 2: logged wits_ecuador_balsa_china_2023 + wits_ecuador_balsa_us_2023.",
        "hunt_infra_building_materials": "Cycle 2: logged sinoma_votorantim_z02_br_2024 (CemNet proxy).",
        "hunt_infra_engineering_epc": "Cycle 2: logged fluor_salares_norte_chile_2024 + bechtel_los_pelambres_inco_2024.",
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
    print("Cycle 2 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
