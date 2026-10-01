#!/usr/bin/env python3
"""Cycle 7 hunt: shuffle_seed=20261007; equal budget across 18 subcategories."""
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


# seed 20261007 order:
# other_renewables, bridges_roads, graphite, engineering_epc, port_ownership,
# niobium, copper, wind, solar, port_cranes, water, power_plants_grid, fission_smr,
# nickel, building_materials, rail, balsa, lithium

# 1 energy/other_renewables — PowerChina Ivirizu hydropower (Bolivia)
A(
    {
        "id": "powerchina_ivirizu_bolivia_2025",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "POWERCHINA — Ivirizu Hydropower Station Sections I–II handover, Cochabamba",
        "country": "Bolivia",
        "asset": "Construction/handover of Bolivia’s largest hydropower station (RCC gravity dam Section I; diversion tunnels, intakes, camps Section II) — formal acceptance Oct 2025",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-17.73",
        "lon": "-65.19",
        "geo_note": "Totora, Cochabamba (POWERCHINA release).",
        "evidence": "documented",
        "source_id": "powerchina_ivirizu_20251028",
        "note": "Actor: POWERCHINA (PRC) — prc. Company English release 28 Oct 2025 on Section II handover. Distinct from PowerChina Chucas CR / San Gabán Peru other_renewables rows.",
    },
    {
        "id": "powerchina_ivirizu_bolivia_2025",
        "retrieved": "2026-10-01",
        "source_id": "powerchina_ivirizu_20251028",
        "url": "https://en.powerchina.cn/2025-10/28/c_829011.htm",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "POWERCHINA officially signed the handover minutes for Section II of Bolivia's Ivirizu Hydropower Station Project … The project is located in Totora, Cochabamba, and is the largest hydropower station with the largest installed capacity in Bolivia to date.",
        "note": "Opened POWERCHINA English news page.",
    },
    {
        "id": "powerchina_ivirizu_20251028",
        "type": "official",
        "chicago": "POWERCHINA. “POWERCHINA delivers Bolivia’s largest hydropower project.” 28 October 2025.",
        "url": "https://en.powerchina.cn/2025-10/28/c_829011.htm",
        "annotation": "Company primary Ivirizu handover notice. Supports powerchina_ivirizu_bolivia_2025.",
        "supports": ["powerchina_ivirizu_bolivia_2025", "hunt_energy_other_renewables"],
    },
)

# 2 infrastructure/bridges_roads — CHEC Mar 2 Expressway Colombia
A(
    {
        "id": "chec_mar2_colombia",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "CHEC Americas — Mar 2 Expressway PPP (Autopista al Mar 2), Antioquia",
        "country": "Colombia",
        "asset": "136 km 4G PPP (118.3 km rehab/improvement + 17.7 km new construction); flagged by CHEC as first Chinese enterprise-funded PPP in Latin America",
        "investment_type": "ppp_concession",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "7.0",
        "lon": "-76.0",
        "geo_note": "Antioquia Atlantic corridor / Cañasgordas–Necoclí alignment (CHEC Americas).",
        "evidence": "documented",
        "source_id": "chec_mar2_project",
        "note": "Actor: CHEC (PRC) — prc. Company project page (IN PROGRESS). Distinct from Jamaica SPARK/SCHIP/Montego Bay CHEC rows.",
    },
    {
        "id": "chec_mar2_colombia",
        "retrieved": "2026-10-01",
        "source_id": "chec_mar2_project",
        "url": "https://www.checamerica.com/projects-mar-2-expressway/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The Mar 2 project is the second largest Public-Private Partnership (PPP) initiative within Colombia’s national 4G highway program. Spanning a total of 136 kilometers, the project includes the rehabilitation and improvement of 118.3 kilometers of existing road, along with 17.7 kilometers of new construction. … recognized by China’s National Development and Reform Commission as the first Chinese enterprise-funded PPP project in Latin America",
        "note": "Opened CHEC Americas Mar 2 project page.",
    },
    {
        "id": "chec_mar2_project",
        "type": "official",
        "chicago": "CHEC Americas. “Projects Mar 2 Expressway.” Company project page (accessed 1 October 2026).",
        "url": "https://www.checamerica.com/projects-mar-2-expressway/",
        "annotation": "Company primary Mar 2 PPP project page. Supports chec_mar2_colombia.",
        "supports": ["chec_mar2_colombia", "hunt_infra_bridges_roads"],
    },
)

# 3 resources/graphite — Appian–Urbix JDA with Graphcoa Brazilian concentrate feed (anode chain)
A(
    {
        "id": "appian_urbix_graphcoa_jda_2023",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "us",
        "counterpart": "Appian / Urbix — JDA for CSPG anode facility fed by Graphcoa Brazilian concentrate",
        "country": "Brazil",
        "asset": "Joint Development Agreement: commercial-scale coated spherical purified graphite (CSPG) facility with Graphcoa (Bahia) as designated natural-flake concentrate feed supplier",
        "investment_type": "offtake_jda",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "-16.0",
        "lon": "-40.0",
        "geo_note": "Graphcoa Boa Sorte / Itagimirim Bahia feed source (Appian JDA); CSPG plant planned with Urbix (U.S.).",
        "evidence": "documented",
        "source_id": "appian_urbix_jda_20231030",
        "note": "Actors: Urbix (U.S. anode tech) + Appian funds; Graphcoa Brazil feed — us coding for anode-chain developer. Company 30 Oct 2023 release. Complements graphcoa_boa_sorte_bahia_2024 mine row and graphex_south_star offtake (different US processor).",
    },
    {
        "id": "appian_urbix_graphcoa_jda_2023",
        "retrieved": "2026-10-01",
        "source_id": "appian_urbix_jda_20231030",
        "url": "https://appiancapitaladvisory.com/appian-announces-investment-in-urbix-inc-and-strategic-collaboration-to-develop-an-integrated-supplier-of-graphite-anode-material-for-the-rapidly-growing-north-and-south-american-lithium-ion-battery/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Agreement provides Urbix and the facility with a consistent source of high quality natural graphite concentrate feed from Brazilian graphite producer Graphcoa, another Appian investee company … Proposed facility would produce coated spherical purified graphite (“CSPG”), a high quality anode material used in lithium ion batteries",
        "note": "Opened Appian Capital Advisory JDA announcement.",
    },
    {
        "id": "appian_urbix_jda_20231030",
        "type": "official",
        "chicago": "Appian Capital Advisory. “Appian announces investment in Urbix, Inc. and strategic collaboration to develop an integrated supplier of graphite anode material …” 30 October 2023.",
        "url": "https://appiancapitaladvisory.com/appian-announces-investment-in-urbix-inc-and-strategic-collaboration-to-develop-an-integrated-supplier-of-graphite-anode-material-for-the-rapidly-growing-north-and-south-american-lithium-ion-battery/",
        "annotation": "Investor primary Graphcoa-fed CSPG JDA notice. Supports appian_urbix_graphcoa_jda_2023.",
        "supports": ["appian_urbix_graphcoa_jda_2023", "hunt_res_graphite"],
    },
)

# 4 infrastructure/engineering_epc — Hatch engineering for Lithium Ionic Bandeira
A(
    {
        "id": "hatch_bandeira_lithium_epc_2024",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "Hatch Ltd. — engineering/design EPCM services for Lithium Ionic Bandeira lithium project, Minas Gerais",
        "country": "Brazil",
        "asset": "Award of engineering and design services (with Reta Engenharia construction management) initiating EPCM phase toward H2 2026 targeted initial production",
        "investment_type": "epcm",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-16.85",
        "lon": "-41.85",
        "geo_note": "Bandeira / Araçuaí–Itinga Lithium Valley, Minas Gerais (company NR).",
        "evidence": "documented",
        "source_id": "lithium_ionic_hatch_20241022",
        "note": "Actor: Hatch (Canadian) — allied; customer Lithium Ionic (Canadian junior). Company 22 Oct 2024 NR. Distinct from Worley Rincon / Techint SADDN / Fluor rows.",
    },
    {
        "id": "hatch_bandeira_lithium_epc_2024",
        "retrieved": "2026-10-01",
        "source_id": "lithium_ionic_hatch_20241022",
        "url": "https://www.lithiumionic.com/_resources/news/nr-20241022.pdf",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Hatch Ltd. has been awarded engineering and design services. … Reta Engenharia … has been selected to provide construction management services for the Bandeira Project.",
        "note": "Opened Lithium Ionic 22 Oct 2024 news-release PDF.",
    },
    {
        "id": "lithium_ionic_hatch_20241022",
        "type": "official",
        "chicago": "Lithium Ionic Corp. “Lithium Ionic Initiates Engineering and Construction Management Services Contracts, Awarded to Hatch and Reta for Bandeira Project Development.” 22 October 2024.",
        "url": "https://www.lithiumionic.com/_resources/news/nr-20241022.pdf",
        "annotation": "Issuer primary Hatch/Reta EPCM award notice. Supports hatch_bandeira_lithium_epc_2024.",
        "supports": ["hatch_bandeira_lithium_epc_2024", "hunt_infra_engineering_epc"],
    },
)

# 5 infrastructure/port_ownership — DP World Posorja USD 140m berth expansion
A(
    {
        "id": "dpworld_posorja_expansion_2025",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "DP World — Port of Posorja berth expansion, Ecuador",
        "country": "Ecuador",
        "asset": "USD 140 million berth expansion to ~700 m quay, capacity to ~1.4 million TEU/year; two electric Super Post-Panamax quay cranes received Oct 2025",
        "investment_type": "concession_capex",
        "value": "140000000",
        "currency": "USD",
        "value_usd": "140000000",
        "fx_usd": "1",
        "fx_date": "2025-10-28",
        "year": "2025",
        "status": "active",
        "lat": "-2.7",
        "lon": "-80.25",
        "geo_note": "Port of Posorja, Guayas (DP World release).",
        "evidence": "documented",
        "source_id": "dpworld_posorja_20251028",
        "note": "Actor: DP World (UAE/Dubai) — allied. Company 28 Oct 2025 Americas release. OEM of quay cranes not named on this page — coded as ownership/capex, not port_cranes. Distinct from DP World Callao Bicentennial.",
    },
    {
        "id": "dpworld_posorja_expansion_2025",
        "retrieved": "2026-10-01",
        "source_id": "dpworld_posorja_20251028",
        "url": "https://www.dpworld.com/en/news/usa/dpw-receives-ecuadors-longest-reaching-cranes-as-part-of-140m-usd-major-berth-expansion",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "It is part of DP World’s ongoing USD$140 million berth expansion project at Posorja, which will extend the quay to 700 meters, allow simultaneous servicing of two post-Panamax vessels, and increase annual terminal capacity to 1.4 million TEUs.",
        "note": "Opened DP World Americas news page.",
    },
    {
        "id": "dpworld_posorja_20251028",
        "type": "official",
        "chicago": "DP World. “DP World Receives Ecuador’s Longest-Reaching Cranes as Part of $140M Major Berth Expansion.” 28 October 2025.",
        "url": "https://www.dpworld.com/en/news/usa/dpw-receives-ecuadors-longest-reaching-cranes-as-part-of-140m-usd-major-berth-expansion",
        "annotation": "Operator primary Posorja expansion notice. Supports dpworld_posorja_expansion_2025.",
        "supports": ["dpworld_posorja_expansion_2025", "hunt_infra_port_ownership"],
    },
)

# 6 resources/niobium — miss

# 7 resources/copper — Codelco–Anglo Andina/Los Bronces joint mine plan
A(
    {
        "id": "codelco_anglo_andina_bronces_2025",
        "layer": "resources",
        "subcategory": "copper",
        "side": "allied",
        "counterpart": "Codelco / Anglo American — Andina–Los Bronces joint mine plan agreement",
        "country": "Chile",
        "asset": "Definitive Sept 2025 agreement for joint mine plan at adjacent Andina and Los Bronces operations; ~2.7 Mt incremental copper over 21 years once permitted (~2030)",
        "investment_type": "jv_mine_plan",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-33.15",
        "lon": "-70.28",
        "geo_note": "Andina / Los Bronces district, Chile central Andes (Codelco report).",
        "evidence": "documented",
        "source_id": "codelco_ops_report_20250930",
        "note": "Actors: Codelco (Chilean state) and Anglo American (UK) — allied coding for Anglo participation with Codelco partner. Codelco operational/financial report to 30 Sep 2025. Distinct from Quellaveco / Cerro Verde / Baiyin Serrote copper rows.",
    },
    {
        "id": "codelco_anglo_andina_bronces_2025",
        "retrieved": "2026-10-01",
        "source_id": "codelco_ops_report_20250930",
        "url": "https://www.codelco.com/sites/site/docs/20250428/20250428185356/operational_and_financial_report_september_30__2025.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "On September 16, CODELCO and Anglo American announced a definitive agreement to implement a joint mine plan, for their adjacent copper operations, Andina and Los Bronces … The joint mine plan will unlock an additional 2.7 million tonnes of copper production over a 21-year period, once the necessary permits—currently expected by 2030— are obtained.",
        "note": "Opened Codelco operational and financial report PDF (30 Sep 2025).",
    },
    {
        "id": "codelco_ops_report_20250930",
        "type": "official",
        "chicago": "Codelco. “Operational and Financial Report — September 30, 2025.” PDF.",
        "url": "https://www.codelco.com/sites/site/docs/20250428/20250428185356/operational_and_financial_report_september_30__2025.pdf",
        "annotation": "Issuer primary disclosure of Andina–Los Bronces joint mine plan. Supports codelco_anglo_andina_bronces_2025.",
        "supports": ["codelco_anglo_andina_bronces_2025", "hunt_res_copper"],
    },
)

# 8 energy/wind — Vestas 128 MW Chile order
A(
    {
        "id": "vestas_chile_128mw_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Vestas — 128 MW V162-6.4 MW turbine order, Chile",
        "country": "Chile",
        "asset": "128 MW order (undisclosed customer/project) for V162-6.4 MW turbines with 10-year AOM5000 service; delivery/commissioning planned Q1 2027",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-33.45",
        "lon": "-70.67",
        "geo_note": "Chile national (customer/project undisclosed on Vestas release); Santiago reference.",
        "evidence": "documented",
        "source_id": "vestas_chile_128_20250801",
        "note": "Actor: Vestas (Danish) — allied. Company 1 Aug 2025 LATAM release. Distinct from Vestas Dom Inocêncio / Casa dos Ventos / Cimarrón Mexico / Casa dos Ventos 2023 Brazil rows.",
    },
    {
        "id": "vestas_chile_128mw_2025",
        "retrieved": "2026-10-01",
        "source_id": "vestas_chile_128_20250801",
        "url": "https://www.vestas.com/en/media/company-news/2025/vestas-announces-128-mw-order-in-chile-c4213693",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Chile | Americas | Undisclosed | Undisclosed | 128 | V162-6.4MW | 10-year AOM5000 Service Agreement | Delivery and commissioning are planned for Q1-2027",
        "note": "Opened Vestas company news page.",
    },
    {
        "id": "vestas_chile_128_20250801",
        "type": "official",
        "chicago": "Vestas. “Vestas announces 128 MW order in Chile.” 1 August 2025.",
        "url": "https://www.vestas.com/en/media/company-news/2025/vestas-announces-128-mw-order-in-chile-c4213693",
        "annotation": "Company primary Chile 128 MW order notice. Supports vestas_chile_128mw_2025.",
        "supports": ["vestas_chile_128mw_2025", "hunt_energy_wind"],
    },
)

# 9 energy/solar — miss (thick)

# 10 infrastructure/port_cranes — Konecranes 14 e-RTGs for Portonave
A(
    {
        "id": "konecranes_portonave_rtg_2025",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Konecranes — 14 fully electric RTGs for Portonave (TiL), Navegantes",
        "country": "Brazil",
        "asset": "Order booked Q4 2024 for 14 battery/busbar electric RTGs; delivery mid-2026 (pairs with Portonave ZPMC STS package)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-26.89",
        "lon": "-48.65",
        "geo_note": "Portonave, Navegantes, Santa Catarina (Konecranes release).",
        "evidence": "documented",
        "source_id": "konecranes_portonave_20250417",
        "note": "Actor: Konecranes (Finnish) — allied. Company 17 Apr 2025 trade press release. Complements zpmc_portonave_sts_2025 (PRC STS OEM on same terminal modernization).",
    },
    {
        "id": "konecranes_portonave_rtg_2025",
        "retrieved": "2026-10-01",
        "source_id": "konecranes_portonave_20250417",
        "url": "https://www.konecranes.com/press-releases/konecranes-expands-presence-in-brazil-with-order-for-14-electric-rtgs-from-portonave",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Portonave … has ordered 14 Konecranes fully electric RTGs … The order was booked in Q4 2024 and the cranes will be delivered in mid-2026.",
        "note": "Opened Konecranes press release.",
    },
    {
        "id": "konecranes_portonave_20250417",
        "type": "official",
        "chicago": "Konecranes. “Konecranes expands presence in Brazil with order for 14 electric RTGs from Portonave.” 17 April 2025.",
        "url": "https://www.konecranes.com/press-releases/konecranes-expands-presence-in-brazil-with-order-for-14-electric-rtgs-from-portonave",
        "annotation": "OEM primary Portonave e-RTG order notice. Supports konecranes_portonave_rtg_2025.",
        "supports": ["konecranes_portonave_rtg_2025", "hunt_infra_port_cranes"],
    },
)

# 11 resources/water — miss

# 12 energy/power_plants_grid — Hitachi Energy Rio Madeira HVDC service extension
A(
    {
        "id": "hitachi_rio_madeira_service_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "Hitachi Energy — EnCompass long-term service extension for Rio Madeira HVDC, Brazil",
        "country": "Brazil",
        "asset": "Extension of long-term HVDC service agreement with Eletrobras for 2,375 km / 3.15 GW Rio Madeira link, adding digital monitoring and cybersecurity suite",
        "investment_type": "service_contract",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-8.76",
        "lon": "-63.9",
        "geo_note": "Rio Madeira HVDC corridor (Porto Velho converter reference).",
        "evidence": "documented",
        "source_id": "hitachi_rio_madeira_20250603",
        "note": "Actor: Hitachi Energy (Japanese/Swiss) — allied. Company 3 Jun 2025 release. Distinct from Hitachi Garabi HVDC upgrade and Brazil transformer capex rows.",
    },
    {
        "id": "hitachi_rio_madeira_service_2025",
        "retrieved": "2026-10-01",
        "source_id": "hitachi_rio_madeira_20250603",
        "url": "https://www.hitachienergy.com/news-and-events/press-releases/2025/06/eletrobras-extends-long-term-service-partnership-with-hitachi-energy-for-rio-madeira-hvdc-system",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Hitachi Energy announces the extension of its service contract with Eletrobras … for the Rio Madeira high-voltage direct current (HVDC) system. The 2,375-kilometer (km) HVDC link is one of the longest in the world … to deliver 3.15 GW of power to some 45 million people.",
        "note": "Opened Hitachi Energy press release.",
    },
    {
        "id": "hitachi_rio_madeira_20250603",
        "type": "official",
        "chicago": "Hitachi Energy. “Eletrobras extends long-term service partnership with Hitachi Energy for Rio Madeira HVDC system.” 3 June 2025.",
        "url": "https://www.hitachienergy.com/news-and-events/press-releases/2025/06/eletrobras-extends-long-term-service-partnership-with-hitachi-energy-for-rio-madeira-hvdc-system",
        "annotation": "Company primary Rio Madeira service-extension notice. Supports hitachi_rio_madeira_service_2025.",
        "supports": ["hitachi_rio_madeira_service_2025", "hunt_br_power_equip"],
    },
)

# 13 energy/fission_smr — miss

# 14 resources/nickel — Atlantic Nickel / Santa Rita (Appian)
A(
    {
        "id": "atlantic_nickel_santa_rita_br",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "Atlantic Nickel (Appian) — Santa Rita nickel sulphide mine, Bahia",
        "country": "Brazil",
        "asset": "Operating open-pit NiS mine (~19 ktpa NiEq; ~6.5 Mtpa ore capacity); 2024 underground expansion PFS (~45 Mlb payable Ni/year; FID targeted 2026)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-11.0",
        "lon": "-39.5",
        "geo_note": "Santa Rita / Itagibá area, Bahia (Appian portfolio page).",
        "evidence": "documented",
        "source_id": "appian_atlantic_nickel",
        "note": "Actor: Appian Capital Advisory funds (UK PE) via Atlantic Nickel — allied. Company portfolio page. Distinct from MMG/Anglo Brazil SPA, Vale Onça Puma, Centaurus Jaguar.",
    },
    {
        "id": "atlantic_nickel_santa_rita_br",
        "retrieved": "2026-10-01",
        "source_id": "appian_atlantic_nickel",
        "url": "https://appiancapitaladvisory.com/portfolio/atlantic-nickel/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "The Santa Rita nickel mine (“Atlantic Nickel” …) is an operating open-pit nickel sulphide (“NiS”) mine with an estimated processing capacity of 6.5Mt of ore annually, located in the north-eastern Brazilian state of Bahia. … In 2024, Atlantic Nickel delivered a Pre-Feasibility Study (PFS) for the mine’s underground expansion. … delivering an average of 45 million pounds of payable nickel per year.",
        "note": "Opened Appian Atlantic Nickel portfolio page.",
    },
    {
        "id": "appian_atlantic_nickel",
        "type": "official",
        "chicago": "Appian Capital Advisory. “Atlantic Nickel.” Portfolio page (accessed 1 October 2026).",
        "url": "https://appiancapitaladvisory.com/portfolio/atlantic-nickel/",
        "annotation": "Investor primary Santa Rita/Atlantic Nickel operating description. Supports atlantic_nickel_santa_rita_br.",
        "supports": ["atlantic_nickel_santa_rita_br", "hunt_res_nickel"],
    },
)

# 15 infrastructure/building_materials — miss

# 16 infrastructure/rail — miss

# 17 resources/balsa — miss

# 18 resources/lithium — POSCO Sal de Oro LiOH plant (Salta official)
A(
    {
        "id": "posco_sal_de_oro_lioh_2024",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "POSCO Argentina — Sal de Oro commercial lithium hydroxide plant, General Güemes",
        "country": "Argentina",
        "asset": "First commercial LiOH plant in Argentina (~25,000 t/y); phase investment cited >USD 800 million; brine from Salar del Hombre Muerto",
        "investment_type": "ownership_equity",
        "value": "800000000",
        "currency": "USD",
        "value_usd": "800000000",
        "fx_usd": "1",
        "fx_date": "2024-10-24",
        "year": "2024",
        "status": "active",
        "lat": "-24.68",
        "lon": "-65.05",
        "geo_note": "Parque Industrial General Güemes, Salta (provincial ministry release).",
        "evidence": "documented",
        "source_id": "salta_posco_lioh_20241024",
        "note": "Actor: POSCO Argentina (South Korean) — allied. Salta Ministry of Production & Mining 24 Oct 2024 inauguration notice cites >USD 800m phase investment and 25 kt/y LiOH. Distinct from Ganfeng/Eramet/Rio Tinto lithium rows.",
    },
    {
        "id": "posco_sal_de_oro_lioh_2024",
        "retrieved": "2026-10-01",
        "source_id": "salta_posco_lioh_20241024",
        "url": "https://produccionsalta.gob.ar/saenz-inauguro-en-salta-la-primera-planta-comercial-de-produccion-de-hidroxido-de-litio-del-pais/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Fue inaugurada en el Parque Industrial de General Güemes de Salta la primera planta comercial de producción de hidróxido de litio del país. Pertenece al proyecto «Sal de Oro» de la minera Posco Argentina … Con una inversión que supera en esta fase los USD 800 millones … Se estima que se producirán 25 mil toneladas de hidróxido de litio al año",
        "note": "Opened Salta provincial ministry Spanish official page.",
    },
    {
        "id": "salta_posco_lioh_20241024",
        "type": "official",
        "chicago": "Ministerio de Producción y Minería de Salta. “Sáenz inauguró en Salta la primera planta comercial de producción de hidróxido de litio del país.” 24 October 2024.",
        "url": "https://produccionsalta.gob.ar/saenz-inauguro-en-salta-la-primera-planta-comercial-de-produccion-de-hidroxido-de-litio-del-pais/",
        "annotation": "Provincial official inauguration notice for POSCO Sal de Oro LiOH plant. Supports posco_sal_de_oro_lioh_2024.",
        "supports": ["posco_sal_de_oro_lioh_2024", "hunt_res_lithium"],
    },
)


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
        "hunt_energy_other_renewables": "Cycle 7: logged powerchina_ivirizu_bolivia_2025.",
        "hunt_infra_bridges_roads": "Cycle 7: logged chec_mar2_colombia.",
        "hunt_res_graphite": "Cycle 7: logged appian_urbix_graphcoa_jda_2023 (anode-chain JDA).",
        "hunt_infra_engineering_epc": "Cycle 7: logged hatch_bandeira_lithium_epc_2024.",
        "hunt_infra_port_ownership": "Cycle 7: logged dpworld_posorja_expansion_2025.",
        "hunt_fenb_araxa": "Cycle 7: equal budget; no distinct new FeNb ownership/price beyond CBMM/CMOC (miss).",
        "hunt_res_copper": "Cycle 7: logged codelco_anglo_andina_bronces_2025.",
        "hunt_energy_wind": "Cycle 7: logged vestas_chile_128mw_2025.",
        "hunt_energy_solar": "Cycle 7: equal budget; thick subcategory — miss.",
        "hunt_infra_port_cranes": "Cycle 7: logged konecranes_portonave_rtg_2025.",
        "hunt_res_water": "Cycle 7: equal budget; no new desal primary beyond IDE/Acciona/GS Inima/Techint set (miss).",
        "hunt_br_power_equip": "Cycle 7: logged hitachi_rio_madeira_service_2025.",
        "hunt_energy_fission_smr": "Cycle 7: equal budget; no new SMR award beyond CAREM/INVAP MoU/Meitner/CNNC set (miss).",
        "hunt_res_nickel": "Cycle 7: logged atlantic_nickel_santa_rita_br.",
        "hunt_infra_building_materials": "Cycle 7: equal budget; no new cement/aggregates award beyond Huaxin/Sinoma/Holcim/Carmeuse (miss).",
        "hunt_latam_rail_telecom": "Cycle 7: equal budget; no new rolling-stock award beyond CAF/Alstom/CRRC/Siemens set (miss).",
        "hunt_res_balsa": "Cycle 7: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_res_lithium": "Cycle 7: logged posco_sal_de_oro_lioh_2024.",
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
    print("Cycle 7 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
