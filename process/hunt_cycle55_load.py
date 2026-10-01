#!/usr/bin/env python3
"""Cycle 55 hunt: shuffle_seed=20261055; equal budget; U.S. side ≥1/3; thin_topup after.

Order: balsa, copper, nickel, solar, graphite, port_ownership, rail, engineering_epc,
lithium, port_cranes, bridges_roads, building_materials, niobium, water, fission_smr,
wind, other_renewables, power_plants_grid.
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
# 2 resources/copper — Teck QB TMF CapEx USD 420m (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "teck_qb_tmf_420m_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "allied",
        "counterpart": "Teck — Quebrada Blanca TMF CapEx 2026",
        "country": "Chile",
        "asset": "28 Oct 2025 Teck Resources news release: Quebrada Blanca (QB) copper operation (Teck 60% / Sumitomo 30% / Codelco 10%) continues to be constrained by Tailings Management Facility (TMF) development; Teck expects capital expenditures related to the TMF of USD 420 million in 2026 (in addition to USD 340 million TMF CapEx disclosed for 2025), including further mechanical raises of the tailings dam wall.",
        "investment_type": "capex",
        "value": "420000000",
        "currency": "USD",
        "value_usd": "420000000",
        "fx_usd": "1",
        "fx_date": "2025-10-28",
        "year": "2026",
        "status": "active",
        "lat": "-20.98",
        "lon": "-68.82",
        "geo_note": "Quebrada Blanca mine, Tarapacá Region, Chile (~4,400 m elevation).",
        "evidence": "documented",
        "source_id": "teck_tr_20251028",
        "note": "Actor: Teck Resources (Canada) operator — allied. Company primary states USD 420m 2026 TMF CapEx. Complements teck_quebrada_blanca_chile / bechtel_qb2_desal_chile (desal/EPC), not a duplicate of those rows.",
    },
    {
        "id": "teck_qb_tmf_420m_2026",
        "retrieved": "2026-10-01",
        "source_id": "teck_tr_20251028",
        "url": "https://www.teck.com/media/25-24-TR.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "As a result of ongoing TMF development work into 2026, including further mechanical raises of the tailings dam wall, we expect capital expenditures related to the TMF of $420 million in 2026. This is in addition to the $340 million of capital expenditures related to TMF in 2025, previously disclosed.",
        "note": "Opened Teck 28 Oct 2025 news release PDF (QB TMF CapEx).",
    },
    {
        "id": "teck_tr_20251028",
        "type": "company",
        "chicago": "Teck Resources Limited. “Teck Reports Unaudited Third Quarter Results for 2025.” News release PDF, 28 October 2025.",
        "url": "https://www.teck.com/media/25-24-TR.pdf",
        "annotation": "Teck primary on QB TMF CapEx USD 420m for 2026. Supports teck_qb_tmf_420m_2026.",
        "supports": ["teck_qb_tmf_420m_2026", "hunt_res_copper"],
    },
)

# ---------------------------------------------------------------------------
# 4 energy/solar — Global Solar América 3 Campeche CFE/MIA (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "global_solar_america3_campeche_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "us",
        "counterpart": "Global Solar América 3 — Campeche PV (CFE mixed / Semarnat MIA)",
        "country": "Mexico",
        "asset": "Feb 2026: Global Solar América 3 files Semarnat regional MIA for Parque Fotovoltaico Campeche — 130.026 MWac, 183,135 bifacial 710 W modules on single-axis trackers, ~269.78 ha in Carmen, Campeche, plus 26.92 km 230 kV evacuation line; 80-week build / 35-year life. June 2026: CFE First Call mixed-development awards list Global Solar America 3 — Global Solar 3 Campeche 100 MW among 37 awarded projects (Von Wobeser / Energy21 / pv magazine Global).",
        "investment_type": "plant",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "18.65",
        "lon": "-91.83",
        "geo_note": "Carmen municipality, Campeche (MIA site; approximate coastal pin).",
        "evidence": "documented",
        "source_id": "pv_mag_campeche_mia_20260210",
        "note": "Actor: Global Solar América 3 (U.S.-named developer in CFE mixed scheme) — us. CapEx not stated on opened pages (leave blank). Distinct from cubico_cfe_mexico_1bn_2026.",
    },
    {
        "id": "global_solar_america3_campeche_2026",
        "retrieved": "2026-10-01",
        "source_id": "pv_mag_campeche_mia_20260210",
        "url": "https://www.pv-magazine-mexico.com/2026/02/10/entra-al-sermanat-el-proyecto-fotovoltaico-campeche-de-130-mw/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "La Secretaría de Medio Ambiente y Recursos Naturales (Semarnat) recibió la Manifestación de Impacto Ambiental (MIA) regional del proyecto fotovoltaico Campeche, impulsado por la empresa Global Solar América 3, que prevé la construcción y operación de una central solar de 130.026 MW en corriente alterna en el municipio de Carmen, estado de Campeche.",
        "note": "Opened pv magazine México MIA coverage; CFE award confirmed in secondary legal/trade coverage.",
    },
    {
        "id": "pv_mag_campeche_mia_20260210",
        "type": "press",
        "chicago": "Ini, Luis. “Entra al Sermanat el proyecto fotovoltaico Campeche, de 130 MW.” pv magazine México, 10 February 2026.",
        "url": "https://www.pv-magazine-mexico.com/2026/02/10/entra-al-sermanat-el-proyecto-fotovoltaico-campeche-de-130-mw/",
        "annotation": "Opened Semarnat MIA summary for Global Solar América 3 Campeche 130 MWac. Supports global_solar_america3_campeche_2026.",
        "supports": ["global_solar_america3_campeche_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 6 infrastructure/port_ownership — EXIM Berbice deepwater LOI (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "exim_guyana_berbice_deepwater_loi_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "us",
        "counterpart": "U.S. EXIM — Berbice deepwater port Letter of Interest",
        "country": "Guyana",
        "asset": "11 Apr 2026 Kaieteur News / subsequent DPI 22 Sep 2026: U.S. EXIM Bank Chairman John Jovanovic issues a Letter of Interest for Guyana’s proposed Berbice deepwater port; DPI later states EXIM “will be part of a structure” for the port alongside GTE Phase Two discussions. LOI is preliminary interest, not a board-approved loan or financial close. Bechtel cited as studying the deepwater design. Distinct from the separate US$285m Berbice Port sod-turning project referenced by President Ali.",
        "investment_type": "financing",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "6.00",
        "lon": "-57.30",
        "geo_note": "Proposed deepwater port at Berbice River mouth, Region Six, Guyana (approximate).",
        "evidence": "documented",
        "source_id": "kaieteur_exim_berbice_20260411",
        "note": "Actor: U.S. EXIM — us. No LOI dollar amount on opened Kaieteur/DPI pages (leave blank). Distinct from exim_guyana_gte_527m_2025 (Wales GTE Phase One).",
    },
    {
        "id": "exim_guyana_berbice_deepwater_loi_2026",
        "retrieved": "2026-10-01",
        "source_id": "kaieteur_exim_berbice_20260411",
        "url": "https://kaieteurnewsonline.com/2026/04/11/u-s-exim-bank-signals-interest-in-major-berbice-deep-water-port-project/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "One of the highlights from the lunch was our chairman issuing a letter of interest for the deep-water ports and so this is yet another project in which we can support the infrastructure requirements of the Guyanese people.",
        "note": "Opened Kaieteur News on EXIM Berbice deepwater LOI; DPI Sep 2026 corroborates continued EXIM port interest.",
    },
    {
        "id": "kaieteur_exim_berbice_20260411",
        "type": "press",
        "chicago": "Kaieteur News. “U.S. EXIM Bank Signals Interest in Major Berbice Deep-Water Port Project.” 11 April 2026.",
        "url": "https://kaieteurnewsonline.com/2026/04/11/u-s-exim-bank-signals-interest-in-major-berbice-deep-water-port-project/",
        "annotation": "Opened Guyanese press on EXIM LOI for Berbice deepwater port. Supports exim_guyana_berbice_deepwater_loi_2026.",
        "supports": ["exim_guyana_berbice_deepwater_loi_2026", "hunt_infra_port_ownership"],
    },
)

# ---------------------------------------------------------------------------
# 9 resources/lithium — Atlas Neves 71% CapEx contracted (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "atlas_lithium_neves_71pct_capex_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "us",
        "counterpart": "Atlas Lithium — Neves Project 71% direct CapEx contracted",
        "country": "Brazil",
        "asset": "9 Sep 2026: Atlas Lithium (NASDAQ:ATLX; Boca Raton) announces ~71% of Neves Project direct CapEx (per DFS) is covered by executed contracts/firm agreements; contracted costs ~16% below corresponding DFS budget. Scope includes earthworks/civil, DMS plant electromechanical assembly, crushing, electrical, detailed engineering, construction management, buildings, and Brazil logistics. Plant already in Brazil for assembly; project fully permitted. Distinct from atlas_lithium_neves_dfs_57p6m_2025 (DFS CapEx USD 57.6m announcement).",
        "investment_type": "epc_contract",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-16.85",
        "lon": "-42.07",
        "geo_note": "Neves / Araçuaí Lithium Valley, Minas Gerais (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "inn_atlas_neves_71pct_20260909",
        "note": "Actor: Atlas Lithium (U.S.-listed) — us. Percentage contracting milestone; contracted dollar total not stated on opened INN/Folha mirrors (leave blank). Complements DFS CapEx row.",
    },
    {
        "id": "atlas_lithium_neves_71pct_capex_2026",
        "retrieved": "2026-10-01",
        "source_id": "inn_atlas_neves_71pct_20260909",
        "url": "https://investingnews.com/atlas-lithium-materially-de-risks-neves-project-with-71-of-direct-capital-budget-already-contracted/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Atlas Lithium Corporation (NASDAQ: ATLX) (\"Atlas Lithium\" or the \"Company\") today announced that approximately 71% of the direct capital expenditures (\"CAPEX\") for its 100%-owned Neves Project (\"Project\"), as outlined in the Company's Definitive Feasibility Study (\"DFS\"), are now supported by executed contracts and firm agreements with selected execution partners. In aggregate, these contracted costs are approximately 16% below the corresponding DFS budget.",
        "note": "Opened INN republication of Atlas Lithium 9 Sep 2026 release.",
    },
    {
        "id": "inn_atlas_neves_71pct_20260909",
        "type": "company",
        "chicago": "Atlas Lithium Corporation. “Atlas Lithium Materially De-Risks Neves Project with 71% of Direct Capital Budget Already Contracted.” Investing News Network, 9 September 2026.",
        "url": "https://investingnews.com/atlas-lithium-materially-de-risks-neves-project-with-71-of-direct-capital-budget-already-contracted/",
        "annotation": "Opened Atlas Neves 71% CapEx contracting release via INN. Supports atlas_lithium_neves_71pct_capex_2026.",
        "supports": ["atlas_lithium_neves_71pct_capex_2026", "hunt_res_lithium"],
    },
)

# ---------------------------------------------------------------------------
# 10 infrastructure/port_cranes — CICE/Liebherr Veracruz GPR (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "liebherr_cice_veracruz_gpr_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Liebherr / Grupo CICE — Veracruz Bahía Norte rail-mounted multipurpose cranes",
        "country": "Mexico",
        "asset": "3 Sep 2026 Grupo CICE company release: two Liebherr P180 L-S rail-mounted multipurpose cranes (GPR) enter commercial operation at CICE’s Terminal Semiespecializada de Contenedores y Carga Proyecto, Bahía Norte, Port of Veracruz — first lifts on CMA CGM Altamira Express (Elbbridge) and ZIM Gulf Toucan (Spyros V). Safe working load to 65 t; Twin Lift to 80 t; Tandem 80–100 t; up to 20 container rows; remote ROS and Active Front End energy recovery. CapEx not disclosed.",
        "investment_type": "equipment_delivery",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "19.22",
        "lon": "-96.13",
        "geo_note": "Bahía Norte, Port of Veracruz, Mexico.",
        "evidence": "documented",
        "source_id": "cice_liebherr_veracruz_20260903",
        "note": "Actor: Liebherr (Germany/Austria) equipment to Mexican operator Grupo CICE — allied. Distinct from hutchison_icave_fase2 and SSA ZPMC rows.",
    },
    {
        "id": "liebherr_cice_veracruz_gpr_2026",
        "retrieved": "2026-10-01",
        "source_id": "cice_liebherr_veracruz_20260903",
        "url": "https://home.grupocice.com/grupo-cice-fortalece-la-atencion-de-servicios-maritimos-con-la-puesta-en-operacion-de-sus-gruas-polivalentes-sobre-rieles/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Grupo CICE fortalece sus capacidades para la atención de servicios navieros con la puesta en operación de dos Grúas Polivalentes sobre Rieles (GPR) Liebherr P180 L-S en su Terminal Semiespecializada de Contenedores y Carga Proyecto en la Bahía Norte del Puerto de Veracruz.",
        "note": "Opened Grupo CICE company release on Liebherr GPR COD.",
    },
    {
        "id": "cice_liebherr_veracruz_20260903",
        "type": "company",
        "chicago": "Grupo CICE. “Grupo CICE Fortalece la Atención de Servicios Marítimos con la Puesta en Operación de Sus Grúas Polivalentes sobre Rieles.” 3 September 2026.",
        "url": "https://home.grupocice.com/grupo-cice-fortalece-la-atencion-de-servicios-maritimos-con-la-puesta-en-operacion-de-sus-gruas-polivalentes-sobre-rieles/",
        "annotation": "CICE primary on two Liebherr P180 L-S GPR COD at Veracruz Bahía Norte. Supports liebherr_cice_veracruz_gpr_2026.",
        "supports": ["liebherr_cice_veracruz_gpr_2026", "hunt_infra_port_cranes"],
    },
)

# ---------------------------------------------------------------------------
# 11 infrastructure/bridges_roads — CHEC San Carlos central tranche (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "chec_san_carlos_central_cr_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "CHEC — Vía a San Carlos central tranche (Sifón–La Abundancia)",
        "country": "Costa Rica",
        "asset": "29 Jul 2026 CR Hoy: MOPT will sign in Q4 2026 the construction contract for the 29 km central tranche of the San Carlos highway (Sifón de San Ramón to La Abundancia, Ciudad Quesada) with China Harbour Engineering Company (CHEC), sole valid bidder; financing shifted from IDB procurement to national budget/legislation after IDB non-objection delays. Press estimates cost at ~USD 300 million — UNVERIFIED proxy. Completes corridor with north tip operating since 2018 and south tip under construction. Distinct from chec_ruta32_costa_rica.",
        "investment_type": "epc_contract",
        "value": "300000000",
        "currency": "USD",
        "value_usd": "300000000",
        "fx_usd": "1",
        "fx_date": "2026-07-29",
        "year": "2026",
        "status": "active",
        "lat": "10.35",
        "lon": "-84.45",
        "geo_note": "Sifón–La Abundancia corridor, Alajuela Province, Costa Rica (approximate midpoint).",
        "evidence": "proxy",
        "source_id": "crhoy_chec_san_carlos_20260729",
        "note": "Actor: CHEC (PRC SOE / CCCC) — prc. Contract signing pending Q4 2026 per CR Hoy; USD 300m is UNVERIFIED press estimate.",
    },
    {
        "id": "chec_san_carlos_central_cr_2026",
        "retrieved": "2026-10-01",
        "source_id": "crhoy_chec_san_carlos_20260729",
        "url": "https://crhoy.com/nacionales/gobierno-firmara-con-chec-proyecto-para-tramo-central-de-via-a-san-carlos/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "El Ministerio de Obras Públicas y Transportes (MOPT) firmará en el último trimestre del año el contrato para la construcción del tramo central de la carretera a San Carlos con la empresa china CHEC. … Los recursos para ejecutar estas obras vendrán del presupuesto nacional. El costo se estima en $300 millones.",
        "note": "Opened CR Hoy on CHEC San Carlos central tranche; CapEx UNVERIFIED press.",
    },
    {
        "id": "crhoy_chec_san_carlos_20260729",
        "type": "press",
        "chicago": "Ruiz, Francisco. “Gobierno Firmará con CHEC Proyecto para Tramo Central de Vía a San Carlos.” CR Hoy, 29 July 2026.",
        "url": "https://crhoy.com/nacionales/gobierno-firmara-con-chec-proyecto-para-tramo-central-de-via-a-san-carlos/",
        "annotation": "Opened Costa Rican press on CHEC San Carlos central contract. Supports chec_san_carlos_central_cr_2026.",
        "supports": ["chec_san_carlos_central_cr_2026", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# 13 resources/niobium — Boston Metal USD 51m convertible (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "boston_metal_51m_convertible_brazil_2025",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "us",
        "counterpart": "Boston Metal — USD 51m convertible note for Brazil critical-metals Phase II",
        "country": "Brazil",
        "asset": "10 Jul 2025 GlobeNewswire: Boston Metal (Woburn, MA) raises USD 51 million convertible note from existing investors (BHP Ventures, Breakthrough Energy Ventures, Piva Capital, SiteGround) to accelerate Phase II of its Minas Gerais critical-metals MOE plant (niobium/tantalum/tin from mining waste), slated mid-2026, and continue green-steel development. Distinct from boston_metal_coronel_xavier_plant_2025 (R$1bn plant CapEx proxy).",
        "investment_type": "financing",
        "value": "51000000",
        "currency": "USD",
        "value_usd": "51000000",
        "fx_usd": "1",
        "fx_date": "2025-07-10",
        "year": "2025",
        "status": "active",
        "lat": "-21.02",
        "lon": "-44.22",
        "geo_note": "Boston Metal do Brasil plant, Coronel Xavier Chaves, Minas Gerais.",
        "evidence": "documented",
        "source_id": "boston_metal_51m_gnw_20250710",
        "note": "Actor: Boston Metal (U.S.) — us. Company primary convertible-note financing for Brazil Phase II scale-up.",
    },
    {
        "id": "boston_metal_51m_convertible_brazil_2025",
        "retrieved": "2026-10-01",
        "source_id": "boston_metal_51m_gnw_20250710",
        "url": "https://www.globenewswire.com/news-release/2025/07/10/3113511/0/en/Boston-Metal-Announces-51-Million-Convertible-Note-to-Accelerate-Scale-Up-of-Critical-Metals-Plant-and-Capitalize-on-Recent-Steel-Technology-Milestone.html",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Boston Metal … today announced it has raised $51 million in a convertible note investment from existing investors including BHP Ventures, Breakthrough Energy Ventures, Piva Capital and SiteGround. … funds from the note will support the deployment of the second phase of its critical metals plant in Brazil, slated to come online in mid-2026.",
        "note": "Opened Boston Metal GlobeNewswire primary.",
    },
    {
        "id": "boston_metal_51m_gnw_20250710",
        "type": "company",
        "chicago": "Boston Metal. “Boston Metal Announces $51 Million Convertible Note to Accelerate Scale-Up of Critical Metals Plant and Capitalize on Recent Steel Technology Milestone.” GlobeNewswire, 10 July 2025.",
        "url": "https://www.globenewswire.com/news-release/2025/07/10/3113511/0/en/Boston-Metal-Announces-51-Million-Convertible-Note-to-Accelerate-Scale-Up-of-Critical-Metals-Plant-and-Capitalize-on-Recent-Steel-Technology-Milestone.html",
        "annotation": "Boston Metal primary on USD 51m note for Brazil Phase II. Supports boston_metal_51m_convertible_brazil_2025.",
        "supports": ["boston_metal_51m_convertible_brazil_2025", "hunt_fenb_araxa"],
    },
)

# ---------------------------------------------------------------------------
# 14 resources/water — Fluence Eneva Azulão demin USD 4.8m (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fluence_eneva_azulao_demin_4p8m_2024",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Fluence — Eneva Azulão demineralized water system",
        "country": "Brazil",
        "asset": "30 May 2024 Fluence (Plymouth, MN / ASX:FLC): USD 4.8 million contract to supply skid-mounted demineralized water treatment (UF + two-pass RO + CEDI) for Eneva’s Azulão I/II thermal complex in Silves, Amazonas; completion targeted Q1 2026. Part of Eneva’s ~USD 1.1 billion / ~950 MW thermal complex. Brazilian trade press cites 720 m³/day demin + 216 m³/day UF make-up. Distinct from fluence_arcelormittal_tubarao_desal_2021 and ge_vernova_azulao_i_cod_2026 (turbine COD).",
        "investment_type": "epc_equipment",
        "value": "4800000",
        "currency": "USD",
        "value_usd": "4800000",
        "fx_usd": "1",
        "fx_date": "2024-05-30",
        "year": "2024",
        "status": "active",
        "lat": "-2.84",
        "lon": "-58.21",
        "geo_note": "Azulão thermal complex, Silves, Amazonas, Brazil.",
        "evidence": "documented",
        "source_id": "fluence_eneva_azulao_20240530",
        "note": "Actor: Fluence Corp (U.S. HQ Plymouth, MN) — us. Company primary contract value USD 4.8m.",
    },
    {
        "id": "fluence_eneva_azulao_demin_4p8m_2024",
        "retrieved": "2026-10-01",
        "source_id": "fluence_eneva_azulao_20240530",
        "url": "https://www.fluencecorp.com/fluence-awarded-us-4-8-million-contract-in-brazil/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Fluence Corporation Limited (ASX: FLC; the “Company”) is pleased to announce that it has secured a US $4.8 million contract to provide a demineralized water treatment system (the “System”) for Eneva in Silves, Amazonas, Brazil. … Work is expected to commence immediately and be completed by the first quarter of 2026.",
        "note": "Opened Fluence primary award release.",
    },
    {
        "id": "fluence_eneva_azulao_20240530",
        "type": "company",
        "chicago": "Fluence Corporation. “Fluence Awarded US $4.8 Million Contract in Brazil.” 30 May 2024.",
        "url": "https://www.fluencecorp.com/fluence-awarded-us-4-8-million-contract-in-brazil/",
        "annotation": "Fluence primary on Azulão demin system USD 4.8m. Supports fluence_eneva_azulao_demin_4p8m_2024.",
        "supports": ["fluence_eneva_azulao_demin_4p8m_2024", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 16 energy/wind — Oak Creek CFE mixed awards Mexico (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "oak_creek_cfe_mexico_1160mw_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "us",
        "counterpart": "Oak Creek — CFE mixed-development awards (Tamaulipas / Nuevo León)",
        "country": "Mexico",
        "asset": "Jun 2026 Energy21 / El CEO: U.S. Oak Creek (Oak Creek Energía de México) ranks among top CFE First Call mixed-development awardees with ~1,160 MW combining solar and wind in Tamaulipas and Nuevo León; press cites ~USD 1,160–1,473 million investment range and ~348 MW storage — UNVERIFIED CapEx proxies. Oak Creek company site documents Mexico construction/O&M presence including 306 MW Tamaulipas construction management. Distinct from aes_andes / cubico_cfe rows.",
        "investment_type": "plant",
        "value": "1160000000",
        "currency": "USD",
        "value_usd": "1160000000",
        "fx_usd": "1",
        "fx_date": "2026-06-08",
        "year": "2026",
        "status": "active",
        "lat": "25.67",
        "lon": "-100.31",
        "geo_note": "Nuevo León / Tamaulipas award cluster (approximate Monterrey-region pin).",
        "evidence": "proxy",
        "source_id": "energy21_oak_creek_cfe_2026",
        "note": "Actor: Oak Creek Energy (U.S.) — us. MW award documented in Mexican energy press; USD investment figures are UNVERIFIED proxies. Hybrid solar+wind portfolio booked under wind subcategory (largest US CFE wind-capable award).",
    },
    {
        "id": "oak_creek_cfe_mexico_1160mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "energy21_oak_creek_cfe_2026",
        "url": "https://energy21.com.mx/cuatro-empresas-acaparan-el-55-de-los-contratos-mixtos-de-cfe/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "En segundo lugar se ubica la estadounidense Oak Creek, con mil 160 MW que combinan generación solar y eólica en Tamaulipas y Nuevo León. Su inversión ronda los mil 160 millones de dólares, con costos que varían entre 50 y 85 dólares por megawatt-hora dependiendo de la tecnología.",
        "note": "Opened Energy21 on Oak Creek CFE mixed awards; CapEx UNVERIFIED press.",
    },
    {
        "id": "energy21_oak_creek_cfe_2026",
        "type": "press",
        "chicago": "Arias, Adrián. “Cuatro Empresas Acaparan el 55% de los Contratos Mixtos de CFE.” Energy21, June 2026.",
        "url": "https://energy21.com.mx/cuatro-empresas-acaparan-el-55-de-los-contratos-mixtos-de-cfe/",
        "annotation": "Opened Mexican energy press on Oak Creek ~1,160 MW CFE awards. Supports oak_creek_cfe_mexico_1160mw_2026.",
        "supports": ["oak_creek_cfe_mexico_1160mw_2026", "hunt_energy_wind"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None and k != "supports":
                existing[k] = v
        supports = list(
            dict.fromkeys((existing.get("supports") or []) + (bib_entry.get("supports") or []))
        )
        existing["supports"] = supports
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
        "hunt_res_balsa": "Cycle 55: equal budget; Plantabal / AIMA–Siemens MoU / estrategia nacional already (miss).",
        "hunt_res_copper": "Cycle 55: logged teck_qb_tmf_420m_2026 (allied; USD 420m QB TMF CapEx 2026).",
        "hunt_res_nickel": "Cycle 55: equal budget; Jervois SMP / Brazilian Nickel / Centaurus Jaguar already (miss).",
        "hunt_energy_solar": "Cycle 55: logged global_solar_america3_campeche_2026 (U.S.; Campeche PV MIA / CFE award).",
        "hunt_res_graphite": "Cycle 55: equal budget; Graphcoa Jordânia / Atlas Malacacheta / South Star already (miss).",
        "hunt_infra_port_ownership": "Cycle 55: logged exim_guyana_berbice_deepwater_loi_2026 (U.S.; EXIM Berbice LOI).",
        "hunt_latam_rail_telecom": "Cycle 55: equal budget; USTDA Honduras CONFI / CCECC QI already (miss).",
        "hunt_infra_engineering_epc": "Cycle 55: equal budget; Bechtel EIMISA / Acciona Yanacocha commissioning already (miss).",
        "hunt_res_lithium": "Cycle 55: logged atlas_lithium_neves_71pct_capex_2026 (U.S.; 71% direct CapEx contracted).",
        "hunt_infra_port_cranes": "Cycle 55: logged liebherr_cice_veracruz_gpr_2026 (allied; two Liebherr P180 L-S at Veracruz).",
        "hunt_infra_bridges_roads": "Cycle 55: logged chec_san_carlos_central_cr_2026 (PRC; CHEC San Carlos central tranche; USD 300m proxy).",
        "hunt_infra_building_materials": "Cycle 55: equal budget pending thin_topup (Cruz Azul Hidalgo / Holcim–Cemex already).",
        "hunt_fenb_araxa": "Cycle 55: logged boston_metal_51m_convertible_brazil_2025 (U.S.; USD 51m note for Brazil Phase II).",
        "hunt_res_water": "Cycle 55: logged fluence_eneva_azulao_demin_4p8m_2024 (U.S.; USD 4.8m Azulão demin).",
        "hunt_energy_fission_smr": "Cycle 55: equal budget; Meitner ACR-300 / FIRST workshop already (miss).",
        "hunt_energy_wind": "Cycle 55: logged oak_creek_cfe_mexico_1160mw_2026 (U.S.; ~1,160 MW CFE mixed awards; CapEx proxy).",
        "hunt_energy_other_renewables": "Cycle 55: equal budget; ContourGlobal Quillagua / Ormat Dominica already (miss).",
        "hunt_br_power_equip": "Cycle 55: equal budget pending thin_topup (GTE Phase One / GE Vernova Azulão already).",
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
    print("Cycle 55 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
