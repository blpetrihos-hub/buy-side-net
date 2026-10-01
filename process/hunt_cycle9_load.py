#!/usr/bin/env python3
"""Cycle 9 hunt: shuffle_seed=20261009; equal budget across 18 subcategories."""
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


# seed 20261009 order:
# other_renewables, power_plants_grid, fission_smr, wind, rail, nickel,
# port_ownership, water, lithium, copper, balsa, graphite, bridges_roads,
# port_cranes, engineering_epc, building_materials, solar, niobium

# 1 energy/other_renewables — JICA Chachimbiro geothermal Phase I Ecuador
A(
    {
        "id": "jica_chachimbiro_ecuador_2024",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "allied",
        "counterpart": "JICA / CELEC EP — Chachimbiro Geothermal Development Project (Phase I), Imbabura",
        "country": "Ecuador",
        "asset": "Japanese ODA yen loan for exploratory well drilling + engineering services toward Ecuador’s first geothermal plant (Phase I); max loan JPY 6,582 million; Phase II plant construction to follow",
        "investment_type": "financing",
        "value": "6582000000",
        "currency": "JPY",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "0.47",
        "lon": "-78.25",
        "geo_note": "Chachimbiro geothermal area, Imbabura Province (JICA / CELEC EP).",
        "evidence": "documented",
        "source_id": "jica_chachimbiro_20241025",
        "note": "Actor: JICA (Japan) financing CELEC EP — allied. JICA 25 Oct 2024 ODA loan signing notice. Distinct from PowerChina hydro/geothermal rows and LaGeo Chinameca.",
    },
    {
        "id": "jica_chachimbiro_ecuador_2024",
        "retrieved": "2026-10-01",
        "source_id": "jica_chachimbiro_20241025",
        "url": "https://www.jica.go.jp/english/information/press/2024/20241025_41.html",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "On October 24, the Japan International Cooperation Agency (JICA) signed a loan agreement with the Empresa Pública Estratégica Corporación Eléctrica del Ecuador … Maximum Loan Amount 6,582 million Japanese Yen … Chachimbiro Geothermal Development Project (Phase I)",
        "note": "Opened JICA English press release on Chachimbiro Phase I ODA loan.",
    },
    {
        "id": "jica_chachimbiro_20241025",
        "type": "official",
        "chicago": "Japan International Cooperation Agency. “Signing of Japanese ODA Loan Agreement for Ecuador: … Construction of a Geothermal Power Plant.” 25 October 2024.",
        "url": "https://www.jica.go.jp/english/information/press/2024/20241025_41.html",
        "annotation": "JICA primary ODA loan notice for Chachimbiro Phase I. Supports jica_chachimbiro_ecuador_2024.",
        "supports": ["jica_chachimbiro_ecuador_2024", "hunt_energy_other_renewables"],
    },
)

# 2 energy/power_plants_grid — Hitachi Energy Dosquebradas Colombia + Brazil add-on
A(
    {
        "id": "hitachi_dosquebradas_colombia_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "Hitachi Energy — Dosquebradas (Risaralda) power transformer factory expansion, Colombia",
        "country": "Colombia",
        "asset": "USD 80 million of a USD 150 million LatAm transformer-capacity package allocated to expand Dosquebradas plant (2026–2028); remainder USD 70 million accelerates Brazil Pindamonhangaba/Guarulhos",
        "investment_type": "ownership_equity",
        "value": "80000000",
        "currency": "USD",
        "value_usd": "80000000",
        "fx_usd": "1",
        "fx_date": "2026-03-09",
        "year": "2026",
        "status": "active",
        "lat": "4.84",
        "lon": "-75.68",
        "geo_note": "Dosquebradas, Risaralda (Hitachi Energy factory expansion notice).",
        "evidence": "documented",
        "source_id": "hitachi_latam_xfmr_20260309",
        "note": "Actor: Hitachi Energy (Japan/Switzerland group) — allied. Company 9 Mar 2026 feature. Colombia USD 80m tranche coded; Brazil add-on already partly covered by prior Hitachi Brazil transformer capex row — this pins the new Colombia plant expansion.",
    },
    {
        "id": "hitachi_dosquebradas_colombia_2026",
        "retrieved": "2026-10-01",
        "source_id": "hitachi_latam_xfmr_20260309",
        "url": "https://www.hitachienergy.com/us/en/news-and-events/features/2026/03/hitachi-energy-reaffirms-commitment-to-latin-america-through-an-additional-150-million-usd-investment-to-expand-power-transformer-manufacturing-capacity",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "In Colombia, $80 million USD will go into expanding and increasing the efficiency of the Dosquebradas (Risaralda) transformer factory, while in Brazil, $70 million USD will build on previously announced investments",
        "note": "Opened Hitachi Energy LatAm transformer investment feature.",
    },
    {
        "id": "hitachi_latam_xfmr_20260309",
        "type": "official",
        "chicago": "Hitachi Energy. “Hitachi Energy reaffirms commitment to Latin America through an additional $150 million USD investment to expand power transformer manufacturing capacity.” 9 March 2026.",
        "url": "https://www.hitachienergy.com/us/en/news-and-events/features/2026/03/hitachi-energy-reaffirms-commitment-to-latin-america-through-an-additional-150-million-usd-investment-to-expand-power-transformer-manufacturing-capacity",
        "annotation": "Company primary LatAm transformer capex notice. Supports hitachi_dosquebradas_colombia_2026.",
        "supports": ["hitachi_dosquebradas_colombia_2026", "hunt_br_power_equip"],
    },
)

# 3 energy/fission_smr — Brazil CNEN microreactor program
A(
    {
        "id": "brazil_microreactor_cnen_2025",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "other",
        "counterpart": "CNEN / INB / Diamante Energia — Brazilian 3–5 MW microreactor development program",
        "country": "Brazil",
        "asset": "Three-year BRL 50 million (~USD 9.1 million) concept program for a containerized 3–5 MW heat-pipe microreactor; first units targeted 8–10 years; INB fuel/engineering support",
        "investment_type": "other",
        "value": "50000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-15.78",
        "lon": "-47.93",
        "geo_note": "National nuclear program (CNEN/INB); pin Brasília as program HQ proxy — no single plant site named yet.",
        "evidence": "documented",
        "source_id": "wnn_brazil_microreactor_20251113",
        "note": "Actors: Brazilian state nuclear complex + private Diamante/Núcleo/Terminus — other (domestic). World Nuclear News 13 Nov 2025 summarizing CNEN program; BRL value as stated (no FX). Distinct from Argentina CAREM/Meitner/FIRST rows.",
    },
    {
        "id": "brazil_microreactor_cnen_2025",
        "retrieved": "2026-10-01",
        "source_id": "wnn_brazil_microreactor_20251113",
        "url": "https://www.world-nuclear-news.org/articles/brazils-microreactor-project-under-way",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "A three-year BRL50 million (USD9.1 million) project brings together private and public sector bodies to develop a concept for a 5 MWt microreactor … The National Nuclear Energy Commission (CNEN) project aims to demonstrate the feasibility of the development of a Brazilian 3-5 MW microreactor.",
        "note": "Opened World Nuclear News Brazil microreactor article citing CNEN.",
    },
    {
        "id": "wnn_brazil_microreactor_20251113",
        "type": "secondary",
        "chicago": "World Nuclear News. “Brazil’s microreactor project under way.” 13 November 2025.",
        "url": "https://www.world-nuclear-news.org/articles/brazils-microreactor-project-under-way",
        "annotation": "Industry press summarizing CNEN/INB microreactor program. Supports brazil_microreactor_cnen_2025.",
        "supports": ["brazil_microreactor_cnen_2025", "hunt_energy_fission_smr"],
    },
)

# 4 energy/wind — Envision 630 MW Casa dos Ventos Brazil
A(
    {
        "id": "envision_casa_ventos_630mw_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "prc",
        "counterpart": "Envision Energy — 630 MW wind turbine supply + 30-year service to Casa dos Ventos (Brazil)",
        "country": "Brazil",
        "asset": "630 MW supply of customized 8.x MW Galileo AI turbines with 30-year LTSA; Envision’s first large net-zero wind deployment partnership in Brazil",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-8.0",
        "lon": "-45.0",
        "geo_note": "Casa dos Ventos Brazil wind partnership (Envision PR); no single farm pin on the opened release — approximate NE Brazil wind belt.",
        "evidence": "documented",
        "source_id": "envision_casa_ventos_20260108",
        "note": "Actor: Envision Energy (PRC) — prc. Company PRNewswire 8 Jan 2026. Distinct from Vestas Dom Inocêncio / Goldwind Touros / Nordex Cajuína OEM rows.",
    },
    {
        "id": "envision_casa_ventos_630mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "envision_casa_ventos_20260108",
        "url": "https://www.prnewswire.com/news-releases/envision-breaks-into-brazil-with-630mw-casa-dos-ventos-project-deploying-ai-driven-wind-power-at-scale-302656544.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Envision Energy … has signed a 630MW wind turbine supply and a 30-year long-term service agreement with Casa dos Ventos … Envision will supply its customized 8.xMW Galileo AI wind turbines",
        "note": "Opened Envision PRNewswire release.",
    },
    {
        "id": "envision_casa_ventos_20260108",
        "type": "official",
        "chicago": "Envision Energy. “Envision Breaks into Brazil with 630MW Casa dos Ventos Project, Deploying AI-Driven Wind Power at Scale.” PR Newswire, 8 January 2026.",
        "url": "https://www.prnewswire.com/news-releases/envision-breaks-into-brazil-with-630mw-casa-dos-ventos-project-deploying-ai-driven-wind-power-at-scale-302656544.html",
        "annotation": "Company primary turbine-supply announcement. Supports envision_casa_ventos_630mw_2026.",
        "supports": ["envision_casa_ventos_630mw_2026", "hunt_energy_wind"],
    },
)

# 5 infrastructure/rail — Siemens Mobility ETCS L2 Chile EFE
A(
    {
        "id": "siemens_efe_etcs_chile_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "Siemens Mobility — ETCS Level 2 / Signaling X for EFE Trenes de Chile (Alameda–Melipilla + Santiago–Batuco)",
        "country": "Chile",
        "asset": "First ETCS L2 deployment in Chile and first Signaling X in LatAm across 87 km (61 km Melipilla + 26 km Batuco); 5-year install + 10-year maintenance; onboard systems for 32 trains",
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
        "geo_note": "Santiago metropolitan EFE corridors (Siemens Mobility press).",
        "evidence": "documented",
        "source_id": "siemens_efe_etcs_20251127",
        "note": "Actor: Siemens Mobility (Germany) — allied. Siemens AG 27 Nov 2025 press release. Distinct from Siemens SP Line 4 CBTC and CAF/Alstom rolling-stock rows.",
    },
    {
        "id": "siemens_efe_etcs_chile_2025",
        "retrieved": "2026-10-01",
        "source_id": "siemens_efe_etcs_20251127",
        "url": "https://press.siemens.com/global/en/pressrelease/siemens-mobility-secures-landmark-contract-digitalizing-rail-chile-latin-america",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Siemens Mobility has been awarded by EFE Trenes de Chile … its first European Train Control System Level 2 (ETCS L2) project in the country … covers 87 kilometers across the Alameda-Melipilla (61 km) and Santiago-Batuco (26 km) lines",
        "note": "Opened Siemens Mobility Chile ETCS press release.",
    },
    {
        "id": "siemens_efe_etcs_20251127",
        "type": "official",
        "chicago": "Siemens AG. “Siemens Mobility secures landmark contract for digitalizing rail in Chile, Latin America.” 27 November 2025.",
        "url": "https://press.siemens.com/global/en/pressrelease/siemens-mobility-secures-landmark-contract-digitalizing-rail-chile-latin-america",
        "annotation": "Company primary EFE ETCS L2 award notice. Supports siemens_efe_etcs_chile_2025.",
        "supports": ["siemens_efe_etcs_chile_2025", "hunt_latam_rail_telecom"],
    },
)

# 6 resources/nickel — Brazilian Nickel Piauí DFC LOI
A(
    {
        "id": "brazilian_nickel_dfc_loi_2024",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "us",
        "counterpart": "U.S. International Development Finance Corporation — LOI for up to USD 550 million senior loan to Brazilian Nickel Piauí Nickel Project",
        "country": "Brazil",
        "asset": "DFC letter of interest for up to USD 550 million senior debt toward commercial-scale Piauí Nickel Project (PNP) heap-leach Ni/Co; LOI is not a closed loan",
        "investment_type": "financing",
        "value": "550000000",
        "currency": "USD",
        "value_usd": "550000000",
        "fx_usd": "1",
        "fx_date": "2024-12-31",
        "year": "2024",
        "status": "active",
        "lat": "-8.1",
        "lon": "-42.5",
        "geo_note": "Piauí Nickel Project, Capitão Gervásio Oliveira area (Brazilian Nickel sustainability report).",
        "evidence": "documented",
        "source_id": "brn_sustentabilidade_2024",
        "note": "Actor: U.S. DFC LOI to UK-domiciled Brazilian Nickel — us financing coding. Company 2024 sustainability PDF. Distinct from MMG/Anglo Barro Alto, Atlantic Nickel Santa Rita, Centaurus Jaguar, Vale Onça Puma.",
    },
    {
        "id": "brazilian_nickel_dfc_loi_2024",
        "retrieved": "2026-10-01",
        "source_id": "brn_sustentabilidade_2024",
        "url": "https://braziliannickel.com/upload/arquivos/RS-Brazilian-Nickel-2024-PTBR.pdf",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Um marco relevante foi a emissão de uma Carta de Intenção pela U.S. Development Finance Corporation (DFC), indicando a possibilidade de concessão de um empréstimo sênior de até US$ 550 milhões para apoiar a implementação do Projeto Piauí Níquel de grande escala.",
        "note": "Opened Brazilian Nickel 2024 Portuguese sustainability report PDF.",
    },
    {
        "id": "brn_sustentabilidade_2024",
        "type": "official",
        "chicago": "Brazilian Nickel Limited. Relatório de Sustentabilidade 2024 (Portuguese). 2025.",
        "url": "https://braziliannickel.com/upload/arquivos/RS-Brazilian-Nickel-2024-PTBR.pdf",
        "annotation": "Company sustainability report disclosing DFC LOI for Piauí. Supports brazilian_nickel_dfc_loi_2024.",
        "supports": ["brazilian_nickel_dfc_loi_2024", "hunt_res_nickel"],
    },
)

# 7 infrastructure/port_ownership — APM/HGT Sunset Puerto Caldera Costa Rica
A(
    {
        "id": "apm_hgt_caldera_costa_rica_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "Consorcio Sunset (APM Terminals + Hanseatic Global Terminals) — Puerto Caldera modernization concession recommendation",
        "country": "Costa Rica",
        "asset": "INCOP Junta Directiva recommended award of public-works-with-public-service concession for Puerto Caldera modernization/equipment to Consorcio Sunset (only admissible bidder); estimated investment ~USD 600 million on tender intake notice",
        "investment_type": "concession",
        "value": "600000000",
        "currency": "USD",
        "value_usd": "600000000",
        "fx_usd": "1",
        "fx_date": "2025-11-07",
        "year": "2026",
        "status": "active",
        "lat": "9.91",
        "lon": "-84.72",
        "geo_note": "Puerto Caldera, Puntarenas (INCOP notices).",
        "evidence": "documented",
        "source_id": "incop_caldera_adjudicacion_20260310",
        "note": "Actors: APM Terminals (Maersk/Denmark) + HGT (Hapag-Lloyd/Germany) — allied. INCOP 9–10 Mar 2026 recommendation of award; USD 600m from INCOP 7 Nov 2025 two-offer intake notice (estimated). Distinct from prior APM Santos/Lázaro rows.",
    },
    {
        "id": "apm_hgt_caldera_costa_rica_2026",
        "retrieved": "2026-10-01",
        "source_id": "incop_caldera_adjudicacion_20260310",
        "url": "https://incop.go.cr/noticias/aprueba-recomendacion-adjudicacion-modernizacion-puerto-caldera/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "La Junta Directiva del Instituto Costarricense de Puertos del Pacífico (INCOP), aprobó … la recomendación de adjudicación al Consorcio Sunset … modernización de la infraestructura y equipamiento de Puerto Caldera.",
        "note": "Opened INCOP award-recommendation notice; value corroborated on INCOP two-offers notice.",
    },
    {
        "id": "incop_caldera_adjudicacion_20260310",
        "type": "official",
        "chicago": "Instituto Costarricense de Puertos del Pacífico (INCOP). “Comunicado: INCOP aprueba recomendación de adjudicación para la modernización de Puerto Caldera.” 10 March 2026.",
        "url": "https://incop.go.cr/noticias/aprueba-recomendacion-adjudicacion-modernizacion-puerto-caldera/",
        "annotation": "Port authority primary award-recommendation notice. Supports apm_hgt_caldera_costa_rica_2026. Companion intake notice: https://incop.go.cr/noticias/se-reciben-2-ofertas-modernizacion-caldera/ (USD 600m estimate; names Sunset = APM Terminals + HGT).",
        "supports": ["apm_hgt_caldera_costa_rica_2026", "hunt_infra_port_ownership"],
    },
)

# 8 resources/water — GS Inima Ensenada desal Mexico
A(
    {
        "id": "gs_inima_ensenada_mexico",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "GS Inima — Ensenada seawater desalination plant (Baja California State Water Commission)",
        "country": "Mexico",
        "asset": "Largest human-consumption desalination plant in Mexico; 21,600 m³/day; design/engineering/O&M for Baja California State Water Commission",
        "investment_type": "epc_om",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "31.87",
        "lon": "-116.60",
        "geo_note": "Ensenada, Baja California (GS Inima project page).",
        "evidence": "documented",
        "source_id": "gs_inima_ensenada_project",
        "note": "Actor: GS Inima (Spain) — allied. Company project page (presence/capacity; no contract USD on page). Year coded 2024 as active observation year. Distinct from GS Inima Atacama Chile and Acciona Los Cabos desal rows. Not Hutchison EIT Ensenada port.",
    },
    {
        "id": "gs_inima_ensenada_mexico",
        "retrieved": "2026-10-01",
        "source_id": "gs_inima_ensenada_project",
        "url": "https://inima.com/en/project/ensenada/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "GS Inima provides services for seawater intake and desalination … in the Municipality of Ensenada, Baja California. The desalination plant is the largest in Mexico for human consumption … Capacity 21.600 m³/day … Contract Type Design, Engineering, Operation and Maintenance",
        "note": "Opened GS Inima Ensenada project page.",
    },
    {
        "id": "gs_inima_ensenada_project",
        "type": "official",
        "chicago": "GS Inima. “Ensenada Desalination Plant.” Company project page. Accessed 1 October 2026.",
        "url": "https://inima.com/en/project/ensenada/",
        "annotation": "Company primary Ensenada desal project description. Supports gs_inima_ensenada_mexico.",
        "supports": ["gs_inima_ensenada_mexico", "hunt_res_water"],
    },
)

# 9 resources/lithium — miss
# 10 resources/copper — Freeport El Abra mill expansion Chile
A(
    {
        "id": "fcx_el_abra_mill_chile_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "us",
        "counterpart": "Freeport-McMoRan (51%) / Codelco (49%) — El Abra potential major mill expansion, Chile",
        "country": "Chile",
        "asset": "Potential mill project that could add >700 million lb Cu/year; ~17.5 billion lb recoverable Cu reserves associated at YE 2025; EIS submitted to Chilean authorities March 2026 — FID pending",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-21.92",
        "lon": "-68.83",
        "geo_note": "El Abra mine, Antofagasta Region (FCX South America disclosures).",
        "evidence": "documented",
        "source_id": "fcx_2q2026_ex991",
        "note": "Actor: Freeport-McMoRan (U.S.) majority — us. FCX 2Q 2026 earnings exhibit. Distinct from fcx_cerro_verde_peru presence pin (Peru) and Codelco–Anglo Andina–Los Bronces JV plan.",
    },
    {
        "id": "fcx_el_abra_mill_chile_2026",
        "retrieved": "2026-10-01",
        "source_id": "fcx_2q2026_ex991",
        "url": "https://www.sec.gov/Archives/edgar/data/831259/000083125926000033/a2q2026exhibit991.htm",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "At the El Abra operations in Chile, FCX has an attractive opportunity to expand the operation to include a major mill facility … The project could result in the addition of over 700 million pounds of copper production per year. In March 2026, El Abra submitted an environmental impact study to Chile regulatory authorities.",
        "note": "Opened FCX SEC 2Q 2026 Exhibit 99.1.",
    },
    {
        "id": "fcx_2q2026_ex991",
        "type": "official",
        "chicago": "Freeport-McMoRan Inc. “Earnings Release / Exhibit 99.1 — Second-Quarter 2026 Results.” U.S. Securities and Exchange Commission EDGAR filing.",
        "url": "https://www.sec.gov/Archives/edgar/data/831259/000083125926000033/a2q2026exhibit991.htm",
        "annotation": "Company SEC earnings exhibit on El Abra mill EIS. Supports fcx_el_abra_mill_chile_2026.",
        "supports": ["fcx_el_abra_mill_chile_2026", "hunt_res_copper"],
    },
)

# 11 resources/balsa — miss
# 12 resources/graphite — miss

# 13 infrastructure/bridges_roads — CHEC Highway 32 Costa Rica
A(
    {
        "id": "chec_ruta32_costa_rica",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "China Harbour Engineering Company (CHEC) — National Route 32 (Braulio Carrillo) expansion, Costa Rica",
        "country": "Costa Rica",
        "asset": "Reconstruction/expansion of 104.2 km Highway 32 (Ruta 4 junction to Limón) to four-lane expressway; CONAVI–CHEC design+construction contract USD 465.6 million",
        "investment_type": "epc",
        "value": "465593387",
        "currency": "USD",
        "value_usd": "465593387",
        "fx_usd": "1",
        "fx_date": "2024-11-01",
        "year": "2024",
        "status": "active",
        "lat": "10.15",
        "lon": "-83.70",
        "geo_note": "Ruta Nacional 32 corridor toward Limón (CHEC Americas / CONAVI).",
        "evidence": "documented",
        "source_id": "chec_americas_projects_ruta32",
        "note": "Actor: CHEC (CCCC/PRC) — prc. CHEC Americas projects page for scope; contract USD from CONAVI Informe Ejecutivo de Obras No. 75 (Nov 2024) opened during hunt. Distinct from CHEC Jamaica/Mar 2 Colombia rows.",
    },
    {
        "id": "chec_ruta32_costa_rica",
        "retrieved": "2026-10-01",
        "source_id": "chec_americas_projects_ruta32",
        "url": "https://www.checamerica.com/projects/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Highway 32 … reconstruction and expansion of a 104.2 km stretch of Highway 32—from the Ofrio junction (Highways 4 and 32) to Limón—into a modern four-lane expressway.",
        "note": "Opened CHEC Americas projects page; contract value from CONAVI executive works report.",
    },
    {
        "id": "chec_americas_projects_ruta32",
        "type": "official",
        "chicago": "CHEC Americas. “Projects” (Highway 32, Costa Rica entry). Accessed 1 October 2026.",
        "url": "https://www.checamerica.com/projects/",
        "annotation": "Company project listing for Ruta 32. Supports chec_ruta32_costa_rica. Value corroborated in CONAVI Informe Ejecutivo de Obras No. 75 (Nov 2024).",
        "supports": ["chec_ruta32_costa_rica", "hunt_infra_bridges_roads"],
    },
)

# 14 infrastructure/port_cranes — Konecranes Arica MHC
A(
    {
        "id": "konecranes_arica_mhc_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Konecranes — two Generation 6 Gottwald ESP.10 mobile harbor cranes for Terminal Puerto Arica (TPA / Neltume Ports)",
        "country": "Chile",
        "asset": "Two ESP.10 MHCs (64 m outreach, 125 t capacity) ordered Q1 2026; operations targeted January 2027; expands large-vessel container/bulk handling at Port of Arica",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-18.48",
        "lon": "-70.33",
        "geo_note": "Port of Arica, Chile (Konecranes investor press).",
        "evidence": "documented",
        "source_id": "konecranes_arica_20260323",
        "note": "Actor: Konecranes (Finland) — allied. Company 23 Mar 2026 press. Distinct from Konecranes Portonave RTG and ZPMC STS/RTG rows.",
    },
    {
        "id": "konecranes_arica_mhc_2026",
        "retrieved": "2026-10-01",
        "source_id": "konecranes_arica_20260323",
        "url": "https://investors.konecranes.com/press/chilean-gateway-port-boosts-its-large-vessel-capacity-two-generation-6-konecranes-gottwald",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Terminal Puerto Arica S.A. (TPA) has invested in two Konecranes Gottwald ESP.10 Mobile Harbor Cranes … The order was booked in Q1 2026 and the cranes are scheduled to be in operation by January 2027.",
        "note": "Opened Konecranes investor press release.",
    },
    {
        "id": "konecranes_arica_20260323",
        "type": "official",
        "chicago": "Konecranes. “Chilean gateway port boosts its large-vessel capacity with two Generation 6 Konecranes Gottwald ESP.10 Mobile Harbor Cranes.” 23 March 2026.",
        "url": "https://investors.konecranes.com/press/chilean-gateway-port-boosts-its-large-vessel-capacity-two-generation-6-konecranes-gottwald",
        "annotation": "Company primary MHC order notice for Arica. Supports konecranes_arica_mhc_2026.",
        "supports": ["konecranes_arica_mhc_2026", "hunt_infra_port_cranes"],
    },
)

# 15 infrastructure/engineering_epc — Bechtel–EIMISA Chile partnership
A(
    {
        "id": "bechtel_eimisa_chile_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Bechtel + EIMISA — mining and infrastructure project-delivery partnership (Chile / South America)",
        "country": "Chile",
        "asset": "May 2026 agreement pairing Bechtel EPC/project management with EIMISA direct-hire construction for select large-scale mining and infrastructure projects in Chile and across South America",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-33.45",
        "lon": "-70.66",
        "geo_note": "Santiago announcement (Bechtel press); Chile delivery focus.",
        "evidence": "documented",
        "source_id": "bechtel_eimisa_20260505",
        "note": "Actor: Bechtel (U.S.) — us. Company 5 May 2026 press. Partnership/framework (no single named mine package USD). Distinct from Bechtel QB2 desal and Los Pelambres INCO rows.",
    },
    {
        "id": "bechtel_eimisa_chile_2026",
        "retrieved": "2026-10-01",
        "source_id": "bechtel_eimisa_20260505",
        "url": "https://www.bechtel.com/press-releases/bechtel-and-eimisa-partner-to-deliver-mining-and-infrastructure-projects-in-chile/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Bechtel … today announced an agreement with Echeverría Izquierdo Montajes Industriales S.A. (EIMISA) … to support the delivery of select large-scale mining and infrastructure projects in Chile and across South America.",
        "note": "Opened Bechtel–EIMISA partnership press release.",
    },
    {
        "id": "bechtel_eimisa_20260505",
        "type": "official",
        "chicago": "Bechtel. “Bechtel and EIMISA Partner to Deliver Mining and Infrastructure Projects in Chile.” 5 May 2026.",
        "url": "https://www.bechtel.com/press-releases/bechtel-and-eimisa-partner-to-deliver-mining-and-infrastructure-projects-in-chile/",
        "annotation": "Company primary Chile delivery partnership notice. Supports bechtel_eimisa_chile_2026.",
        "supports": ["bechtel_eimisa_chile_2026", "hunt_infra_engineering_epc"],
    },
)

# 16 infrastructure/building_materials — Holcim acquires Cemex Colombia assets
A(
    {
        "id": "holcim_cemex_colombia_2026",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Holcim — agreement to acquire Cemex Colombia building-materials operations (Caracolito cement plant + Santa Rosa grinding + >20 ready-mix/aggregates sites)",
        "country": "Colombia",
        "asset": "USD 485 million transaction for Cemex Colombia assets with projected 2026 net sales ~USD 360 million; close expected around end-2026 subject to approvals",
        "investment_type": "ownership_equity",
        "value": "485000000",
        "currency": "USD",
        "value_usd": "485000000",
        "fx_usd": "1",
        "fx_date": "2026-03-12",
        "year": "2026",
        "status": "active",
        "lat": "5.07",
        "lon": "-74.6",
        "geo_note": "Caracolito cement plant area, Colombia (Holcim media release).",
        "evidence": "documented",
        "source_id": "holcim_colombia_cemex_2026",
        "note": "Actor: Holcim (Switzerland) — allied. Holcim media release. Distinct from Holcim Pacasmayo Peru and Comacsa/Mixercon Peru rows and Cemex DR divestiture.",
    },
    {
        "id": "holcim_cemex_colombia_2026",
        "retrieved": "2026-10-01",
        "source_id": "holcim_colombia_cemex_2026",
        "url": "https://www.holcim.com/media/media-releases/holcim-expands-in-colombia",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Holcim has signed an agreement … acquiring building materials and solutions operations in Colombia from Cemex that represent projected 2026 net sales of around USD 360 million. … The transaction value of USD 485 million … expected to close around the end of the year.",
        "note": "Opened Holcim Colombia expansion media release.",
    },
    {
        "id": "holcim_colombia_cemex_2026",
        "type": "official",
        "chicago": "Holcim. “Holcim expands in Colombia.” Media release.",
        "url": "https://www.holcim.com/media/media-releases/holcim-expands-in-colombia",
        "annotation": "Company primary Colombia Cemex-assets acquisition notice. Supports holcim_cemex_colombia_2026.",
        "supports": ["holcim_cemex_colombia_2026", "hunt_infra_building_materials"],
    },
)

# 17 energy/solar — PowerChina Guayepo III EPC for Enel Colombia
A(
    {
        "id": "powerchina_guayepo_iii_colombia_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "PowerChina — EPC contractor for Enel Colombia Guayepo III solar park (Atlántico)",
        "country": "Colombia",
        "asset": "PowerChina completed ~200 MW Guayepo III solar farm EPC for Enel; full grid connection reported Oct 2025; >457,700 panels between Ponedera and Sabanalarga",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "10.64",
        "lon": "-74.77",
        "geo_note": "Guayepo III, Ponedera/Sabanalarga, Atlántico (pv magazine / Enel reporting).",
        "evidence": "proxy",
        "source_id": "pv_mag_powerchina_guayepo_20251022",
        "note": "Actor: PowerChina (PRC) EPC for Enel Colombia — prc. pv magazine Global 22 Oct 2025 summarizing Enel/PowerChina completion — UNVERIFIED press proxy for capacity label (~200 MW vs later 180 MWac commercial figures elsewhere). No contract USD on opened page.",
    },
    {
        "id": "powerchina_guayepo_iii_colombia_2025",
        "retrieved": "2026-10-01",
        "source_id": "pv_mag_powerchina_guayepo_20251022",
        "url": "https://www.pv-magazine.com/2025/10/22/powerchina-completes-200-mw-solar-project-for-enel-in-colombia/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "Powerchina has finished the 200 MW Guayepo III solar farm in northern Colombia, connecting it to the grid six days ahead of schedule for Italian utility Enel. … Powerchina acted as the engineering, procurement, and construction contractor.",
        "note": "Opened pv magazine Global Guayepo III PowerChina completion article.",
    },
    {
        "id": "pv_mag_powerchina_guayepo_20251022",
        "type": "secondary",
        "chicago": "Ini, Luis. “Powerchina completes 200 MW solar project for Enel in Colombia.” pv magazine Global, 22 October 2025.",
        "url": "https://www.pv-magazine.com/2025/10/22/powerchina-completes-200-mw-solar-project-for-enel-in-colombia/",
        "annotation": "Trade press on PowerChina Guayepo III EPC completion. Supports powerchina_guayepo_iii_colombia_2025 (UNVERIFIED capacity label).",
        "supports": ["powerchina_guayepo_iii_colombia_2025", "hunt_energy_solar"],
    },
)

# 18 resources/niobium — miss


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
        "hunt_energy_other_renewables": "Cycle 9: logged jica_chachimbiro_ecuador_2024.",
        "hunt_br_power_equip": "Cycle 9: logged hitachi_dosquebradas_colombia_2026.",
        "hunt_energy_fission_smr": "Cycle 9: logged brazil_microreactor_cnen_2025.",
        "hunt_energy_wind": "Cycle 9: logged envision_casa_ventos_630mw_2026.",
        "hunt_latam_rail_telecom": "Cycle 9: logged siemens_efe_etcs_chile_2025.",
        "hunt_res_nickel": "Cycle 9: logged brazilian_nickel_dfc_loi_2024.",
        "hunt_infra_port_ownership": "Cycle 9: logged apm_hgt_caldera_costa_rica_2026.",
        "hunt_res_water": "Cycle 9: logged gs_inima_ensenada_mexico.",
        "hunt_res_lithium": "Cycle 9: equal budget; no distinct new Li deal beyond NovaAndino/Ganfeng/Rio Tinto/POSCO/Eramet (miss).",
        "hunt_res_copper": "Cycle 9: logged fcx_el_abra_mill_chile_2026.",
        "hunt_res_balsa": "Cycle 9: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_res_graphite": "Cycle 9: equal budget; no distinct new graphite mine/anode beyond South Star/Graphcoa/Urbix/Nacional/Graphex (miss).",
        "hunt_infra_bridges_roads": "Cycle 9: logged chec_ruta32_costa_rica.",
        "hunt_infra_port_cranes": "Cycle 9: logged konecranes_arica_mhc_2026.",
        "hunt_infra_engineering_epc": "Cycle 9: logged bechtel_eimisa_chile_2026.",
        "hunt_infra_building_materials": "Cycle 9: logged holcim_cemex_colombia_2026.",
        "hunt_energy_solar": "Cycle 9: logged powerchina_guayepo_iii_colombia_2025 (UNVERIFIED proxy).",
        "hunt_fenb_araxa": "Cycle 9: equal budget; no distinct new FeNb ownership/price beyond CBMM/CMOC (miss).",
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
    print("Cycle 9 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
