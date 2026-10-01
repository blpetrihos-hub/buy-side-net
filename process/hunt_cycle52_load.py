#!/usr/bin/env python3
"""Cycle 52 hunt: shuffle_seed=20261052; equal budget; U.S. side ≥1/3; thin_topup after.

Order: wind, engineering_epc, solar, fission_smr, niobium, building_materials, rail,
power_plants_grid, nickel, lithium, copper, port_ownership, balsa, water, port_cranes,
bridges_roads, graphite, other_renewables.
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
# 1 energy/wind — ENGIE Serra do Assuruá 846 MW (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "engie_serra_assurua_846mw_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "ENGIE Brasil Energia — Serra do Assuruá Wind Complex (846 MW)",
        "country": "Brazil",
        "asset": "18 Dec 2025: ENGIE Brasil Energia announces full commercial operations at Serra do Assuruá Wind Complex (Gentio do Ouro, Bahia) — 188 turbines across 24 wind farms, 846 MW installed; 28 km transmission to SIN; built in a single phase with investment of R$ 6 billion (company approx. USD 1.2 billion); gradual COD from Aug 2024 after ANEEL authorization; Free Energy Market offtake. Distinct from Goldwind Sento Sé / ENGIE Assú Sol solar.",
        "investment_type": "greenfield_generation",
        "value": "6000000000",
        "currency": "BRL",
        "value_usd": "1200000000",
        "fx_usd": "",
        "fx_date": "2025-12-18",
        "year": "2025",
        "status": "active",
        "lat": "-11.43",
        "lon": "-42.51",
        "geo_note": "Gentio do Ouro, Bahia (Serra do Assuruá wind complex pin).",
        "evidence": "proxy",
        "source_id": "engie_serra_assurua_20251218",
        "note": "Actor: ENGIE (French) — allied. Company press 18 Dec 2025; R$6bn CAPEX with company USD 1.2bn approx — UNVERIFIED proxy for USD conversion.",
    },
    {
        "id": "engie_serra_assurua_846mw_2025",
        "retrieved": "2026-10-01",
        "source_id": "engie_serra_assurua_20251218",
        "url": "https://www.engie.com.br/en/imprensa/press-releases/engie-begins-full-commercial-operation-of-the-serra-do-assurua-wind-complex-in-brazil/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "ENGIE Brasil Energia announces the start of full commercial operations at the Serra do Assuruá Wind Complex, located in Gentio do Ouro, in the state of Bahia. With 188 wind turbines across 24 wind farms and a total installed capacity of 846 MW … The complex, built in a single phase with an investment of R$ 6 billion (approximately USD 1.2 billion), began operating gradually in August 2024, following authorization from the National Electric Energy Agency (Aneel).",
        "note": "Opened ENGIE Brasil Serra do Assuruá full COD release.",
    },
    {
        "id": "engie_serra_assurua_20251218",
        "type": "company",
        "chicago": "ENGIE Brasil Energia. “ENGIE Begins Full Commercial Operation of the Serra do Assuruá Wind Complex in Brazil.” 18 December 2025.",
        "url": "https://www.engie.com.br/en/imprensa/press-releases/engie-begins-full-commercial-operation-of-the-serra-do-assurua-wind-complex-in-brazil/",
        "annotation": "Company primary on Serra do Assuruá 846 MW full COD and R$6bn CAPEX. Supports engie_serra_assurua_846mw_2025.",
        "supports": ["engie_serra_assurua_846mw_2025", "engie_asa_branca_tx_2p7bn_2025", "hunt_energy_wind"],
    },
)

# ---------------------------------------------------------------------------
# 2 infrastructure/engineering_epc — Xinhai / St George Araxá EPC MoU (PRC)
# ---------------------------------------------------------------------------
A(
    {
        "id": "xinhai_st_george_araxa_epc_mou_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "prc",
        "counterpart": "Shandong Xinhai / HongKong Xinhai Mining Services — St George Araxá Nb-REE EPC MoU",
        "country": "Brazil",
        "asset": "11–12 Feb 2025: Binding MoU between St George Mining and Shandong Xinhai Mining Technology & Equipment for Araxá niobium-REE project (Minas Gerais): negotiate Strategic Partnership with first/last refusal for EPCM+O; fixed-price EPC proposal; Xinhai (and nominees) commit A$8 million equity into St George A$20m raise supporting Araxá acquisition; proposed SPA includes exclusive distribution/marketing rights for 80% of niobium offtake sold into China. Distinct from Worley feasibility adviser / Boston Metal MOE MoU.",
        "investment_type": "mou_epc_negotiation",
        "value": "8000000",
        "currency": "AUD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2025-02-12",
        "year": "2025",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "Araxá, Minas Gerais (St George Nb-REE project adjacent to CBMM).",
        "evidence": "documented",
        "source_id": "stgm_xinhai_epc_20250212",
        "note": "Actor: Shandong Xinhai (PRC) — prc. ASX release 12 Feb 2025; A$8m equity commitment documented; EPC contract not yet executed — MoU framework.",
    },
    {
        "id": "xinhai_st_george_araxa_epc_mou_2025",
        "retrieved": "2026-10-01",
        "source_id": "stgm_xinhai_epc_20250212",
        "url": "https://www.stgm.com.au/pdf/e55b3358-7e64-435a-bf84-0d65dd829820/A8M-Investment-and-EPC-Deal-for-Araxa-Niobium-Project.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "St George and Shandong Xinhai Mining Technology & Equipment Inc (“Xinhai”) … have entered into a binding Memorandum of Understanding (“MoU”) to work together on the development of the high-grade Araxá niobium-REE Project in Brazil. … Xinhai will have a first and last right of refusal for an EPCM+O contract for the Araxá Project … Xinhai (and its nominees) has committed to invest A$8 million in the A$20 million equity fund raising being completed by St George in support of the Araxá acquisition.",
        "note": "Opened St George ASX PDF on Xinhai A$8m / EPC MoU.",
    },
    {
        "id": "stgm_xinhai_epc_20250212",
        "type": "company",
        "chicago": "St George Mining Limited. “A$8M Investment and EPC Deal for Araxá Niobium Project.” ASX release, 12 February 2025.",
        "url": "https://www.stgm.com.au/pdf/e55b3358-7e64-435a-bf84-0d65dd829820/A8M-Investment-and-EPC-Deal-for-Araxa-Niobium-Project.pdf",
        "annotation": "ASX primary on Xinhai Araxá EPC MoU and A$8m equity. Supports xinhai_st_george_araxa_epc_mou_2025.",
        "supports": ["xinhai_st_george_araxa_epc_mou_2025", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 3 energy/solar — ContourGlobal Los Maitenes hybrid PV+BESS (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "contourglobal_los_maitenes_chile_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "us",
        "counterpart": "ContourGlobal (KKR) — Los Maitenes hybrid PV + BESS (O’Higgins)",
        "country": "Chile",
        "asset": "4 Aug 2026: ContourGlobal starts construction of Los Maitenes hybrid solar-plus-storage in Chile’s O’Higgins Region — 131 MWp PV + 90 MW / 360 MWh BESS; long-term PPA covering daytime and nighttime blocks; COD targeted end-2027; expands ContourGlobal Chile portfolio toward ~583 MWp solar with 490 MW / 2.9 GWh BESS. Distinct from contourglobal_victor_jara_cod_2026 and Oasis de Atacama Quillagua.",
        "investment_type": "greenfield_generation",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-34.17",
        "lon": "-70.74",
        "geo_note": "O’Higgins Region, Chile (Los Maitenes hybrid plant pin — approximate).",
        "evidence": "documented",
        "source_id": "contourglobal_los_maitenes_20260804",
        "note": "Actor: ContourGlobal (KKR-backed, U.S. ownership chain) — us. Company release 4 Aug 2026; project CAPEX USD not disclosed on opened page.",
    },
    {
        "id": "contourglobal_los_maitenes_chile_2026",
        "retrieved": "2026-10-01",
        "source_id": "contourglobal_los_maitenes_20260804",
        "url": "https://www.contourglobal.com/news/contourglobal-to-expand-chile-hybrid-renewables-platform-with-new-solar-plus-storage-project/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "ContourGlobal today announced the start of construction of Los Maitenes, a new hybrid solar-plus-storage investment in Chile for a facility combining 131 MWp of solar PV capacity with 90 MW/360 MWh of battery storage. When completed, the facility will push ContourGlobal’s Chilean renewables and storage portfolio to approximately 583 MWp of solar PV with 490 MW / 2.9 GWh of BESS capacity … The new facility is expected to generate around 220 GWh of clean electricity per year, and to be fully built by end of 2027.",
        "note": "Opened ContourGlobal Los Maitenes construction start release.",
    },
    {
        "id": "contourglobal_los_maitenes_20260804",
        "type": "company",
        "chicago": "ContourGlobal. “ContourGlobal to expand Chile hybrid renewables platform with new solar-plus-storage project.” 4 August 2026.",
        "url": "https://www.contourglobal.com/news/contourglobal-to-expand-chile-hybrid-renewables-platform-with-new-solar-plus-storage-project/",
        "annotation": "Company primary on Los Maitenes 131 MWp / 90 MW BESS construction start. Supports contourglobal_los_maitenes_chile_2026.",
        "supports": ["contourglobal_los_maitenes_chile_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 5 resources/niobium — Boston Metal / St George Araxá MOE MoU (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "st_george_boston_metal_moe_mou_2026",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "us",
        "counterpart": "Boston Electrometallurgical Corporation (Boston Metal) — St George Araxá FeNb MOE trial MoU",
        "country": "Brazil",
        "asset": "1 Apr 2026: St George Mining MoU with Boston Metal (Woburn, Massachusetts) to trial molten oxide electrolysis (MOE) for ferroniobium production from Araxá Nb-REE ore (Minas Gerais); each party bears own testwork costs; long-term licensing subject to future formal agreement; Boston Metal commissioning first commercial critical-metals plant in Brazil. Distinct from Fangda offtake MoU / REAlloys MoU / Xinhai EPC MoU.",
        "investment_type": "technology_mou",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "Araxá, Minas Gerais (St George Nb-REE project; Boston Metal MOE trial feedstock).",
        "evidence": "documented",
        "source_id": "stgm_boston_metal_20260401",
        "note": "Actor: Boston Metal (U.S., Woburn MA) — us. ASX release 1 Apr 2026; non-binding MoU / trial — no CAPEX USD on page.",
    },
    {
        "id": "st_george_boston_metal_moe_mou_2026",
        "retrieved": "2026-10-01",
        "source_id": "stgm_boston_metal_20260401",
        "url": "https://announcements.asx.com.au/asxpdf/20260401/pdf/06y1jdgz8756rk.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "St George Mining Limited (ASX: SGQ) … has signed a Memorandum of Understanding (“MoU”) with Boston Metal to trial a new-generation processing technology at St George’s 100%-owned advanced, high-grade Araxá niobium-REE Project in Minas Gerais, Brazil … Boston Metal will evaluate niobium from the Araxá Project with the aim of assessing the application of MOE for ferroniobium production. … Boston Metal is headquartered in Woburn, Massachusetts and has a wholly owned subsidiary in Brazil.",
        "note": "Opened St George ASX PDF on Boston Metal MOE MoU.",
    },
    {
        "id": "stgm_boston_metal_20260401",
        "type": "company",
        "chicago": "St George Mining Limited. “Strategic Alliance with Boston Metal for Innovative Niobium Processing at the Araxá Project, Brazil.” ASX release, 1 April 2026.",
        "url": "https://announcements.asx.com.au/asxpdf/20260401/pdf/06y1jdgz8756rk.pdf",
        "annotation": "ASX primary on Boston Metal MOE ferroniobium trial MoU at Araxá. Supports st_george_boston_metal_moe_mou_2026.",
        "supports": ["st_george_boston_metal_moe_mou_2026", "hunt_fenb_araxa"],
    },
)

# ---------------------------------------------------------------------------
# 7 infrastructure/rail — CRRC São Paulo Metro Frota R 44 trains (PRC)
# ---------------------------------------------------------------------------
A(
    {
        "id": "crrc_sp_metro_frota_r_44_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "prc",
        "counterpart": "Consórcio CRRC Sifang Brasil — São Paulo Metro Frota R (44 six-car trains)",
        "country": "Brazil",
        "asset": "22 Jul 2025: Contract signed with Consórcio CRRC Sifang Brasil for 44 six-car metro trains (Frota R) for São Paulo Metro Lines 1-Azul, 2-Verde and 3-Vermelha; contract value R$ 3,104,298,999.76 (base date 1 Apr 2024); 70-month term; supports Line 2-Verde extension toward Penha/Guarulhos. Homologation published 18 Mar 2025 (CRRC beat Alstom). Distinct from crrc_salvador_metro_2026 and crrc_araraquara_factory_2026.",
        "investment_type": "rolling_stock",
        "value": "3104298999.76",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2025-07-22",
        "year": "2025",
        "status": "active",
        "lat": "-23.55",
        "lon": "-46.63",
        "geo_note": "São Paulo Metro network (Lines 1/2/3 Frota R deployment pin).",
        "evidence": "proxy",
        "source_id": "diario_transporte_crrc_sp_20250723",
        "note": "Actor: CRRC Sifang Brasil (PRC) — prc. Diário do Transporte 23 Jul 2025 citing Diário Oficial contract extract; BRL point value documented — USD conversion left blank (UNVERIFIED without opened FX sheet).",
    },
    {
        "id": "crrc_sp_metro_frota_r_44_2025",
        "retrieved": "2026-10-01",
        "source_id": "diario_transporte_crrc_sp_20250723",
        "url": "https://diariodotransporte.com.br/2025/07/23/contrato-para-44-novos-trens-do-metro-de-sp-e-assinado-com-estatal-chinesa-quase-quatro-meses-apos-homologacao-da-licitacao/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "O contrato para o fornecimento de 44 novos trens metropolitanos para a Companhia do Metropolitano de São Paulo – Metrô foi finalmente assinado nesta terça-feira, 22 de julho de 2025 … O documento foi formalizado com o Consórcio CRRC Sifang Brasil, vencedor da licitação. … O valor total do contrato é de R$ 3,1 bilhões (R$ 3.104.298.999,76), com data-base em 1º de abril de 2024. O prazo de vigência do acordo é de 70 meses.",
        "note": "Opened Diário do Transporte coverage of CRRC Sifang Frota R contract signing / DOE extract.",
    },
    {
        "id": "diario_transporte_crrc_sp_20250723",
        "type": "press",
        "chicago": "Pelegi, Alexandre. “Contrato para 44 novos trens do Metrô de SP é assinado com estatal chinesa quase quatro meses após homologação da licitação.” Diário do Transporte, 23 July 2025.",
        "url": "https://diariodotransporte.com.br/2025/07/23/contrato-para-44-novos-trens-do-metro-de-sp-e-assinado-com-estatal-chinesa-quase-quatro-meses-apos-homologacao-da-licitacao/",
        "annotation": "Trade press citing DOE extract on CRRC Sifang R$3.104bn Frota R contract. Supports crrc_sp_metro_frota_r_44_2025.",
        "supports": ["crrc_sp_metro_frota_r_44_2025", "hunt_latam_rail_telecom"],
    },
)

# ---------------------------------------------------------------------------
# 8 energy/power_plants_grid — ENGIE Asa Branca transmission (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "engie_asa_branca_tx_2p7bn_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "ENGIE Brasil Energia — Asa Branca Transmission System (~1,000 km)",
        "country": "Brazil",
        "asset": "ENGIE commissions first 334 km stretch of Asa Branca 500 kV transmission (Morro do Chapéu II–Poções III, Bahia) interconnecting Northeast–Southeast for renewable offtake; full system ~1,000 km across Bahia, Minas Gerais and Espírito Santo with associated substation expansions; company cites further BRL 2.7 billion (approx. USD 540 million) investment. Distinct from Serra do Assuruá generation and Graúna TX.",
        "investment_type": "epc",
        "value": "2700000000",
        "currency": "BRL",
        "value_usd": "540000000",
        "fx_usd": "",
        "fx_date": "2025-12-18",
        "year": "2025",
        "status": "active",
        "lat": "-11.55",
        "lon": "-41.16",
        "geo_note": "Morro do Chapéu / Poções corridor, Bahia (Asa Branca first stretch pin).",
        "evidence": "proxy",
        "source_id": "engie_serra_assurua_20251218",
        "note": "Actor: ENGIE (French) — allied. Same ENGIE Brasil 18 Dec 2025 release naming Asa Branca first stretch + BRL 2.7bn / USD 540m company approx — UNVERIFIED proxy for USD.",
    },
    {
        "id": "engie_asa_branca_tx_2p7bn_2025",
        "retrieved": "2026-10-01",
        "source_id": "engie_serra_assurua_20251218",
        "url": "https://www.engie.com.br/en/imprensa/press-releases/engie-begins-full-commercial-operation-of-the-serra-do-assurua-wind-complex-in-brazil/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "Recently, it put into operation in the state the first 334-kilometer stretch of the Asa Branca Transmission Project, a strategic infrastructure spanning approximately 1,000 kilometers in the states of Bahia, Minas Gerais and Espírito Santo. The initiative includes the expansion of five substations and represents a further BRL 2.7 billion (USD 540 million) investment in Brazil’s energy infrastructure.",
        "note": "Opened ENGIE Brasil release section on Asa Branca first stretch / CAPEX.",
    },
    {
        "id": "engie_serra_assurua_20251218",
        "type": "company",
        "chicago": "ENGIE Brasil Energia. “ENGIE Begins Full Commercial Operation of the Serra do Assuruá Wind Complex in Brazil.” 18 December 2025.",
        "url": "https://www.engie.com.br/en/imprensa/press-releases/engie-begins-full-commercial-operation-of-the-serra-do-assurua-wind-complex-in-brazil/",
        "annotation": "Company primary also documenting Asa Branca first stretch and BRL 2.7bn CAPEX. Supports engie_asa_branca_tx_2p7bn_2025.",
        "supports": ["engie_serra_assurua_846mw_2025", "engie_asa_branca_tx_2p7bn_2025", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 10 resources/lithium — EXIM LOI Lithium Ionic Bandeira USD 266m (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "lithium_ionic_exim_loi_266m_2024",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "us",
        "counterpart": "U.S. EXIM / Lithium Ionic — Bandeira Lithium Project LOI",
        "country": "Brazil",
        "asset": "27 Nov 2024: Non-binding Letter of Interest from Export-Import Bank of the United States for up to USD 266 million debt financing for Lithium Ionic’s 100%-owned Bandeira Lithium Project (Minas Gerais / Lithium Valley); covers 100% of May 2024 Feasibility Study CAPEX; max 15-year repayment; aligned with EXIM CTEP critical minerals. Conditional on application, due diligence and final approval. Distinct from EnergyX Chile EXIM LOI and Hatch Bandeira EPC row.",
        "investment_type": "financing",
        "value": "266000000",
        "currency": "USD",
        "value_usd": "266000000",
        "fx_usd": "1",
        "fx_date": "2024-11-27",
        "year": "2024",
        "status": "active",
        "lat": "-16.85",
        "lon": "-42.07",
        "geo_note": "Bandeira / Araçuaí area, Minas Gerais Lithium Valley (project pin — approximate).",
        "evidence": "documented",
        "source_id": "lithium_ionic_exim_20241127",
        "note": "Actor: U.S. EXIM LOI for Bandeira — us. Company release 27 Nov 2024; LOI non-binding / conditional (not closed loan).",
    },
    {
        "id": "lithium_ionic_exim_loi_266m_2024",
        "retrieved": "2026-10-01",
        "source_id": "lithium_ionic_exim_20241127",
        "url": "https://www.lithiumionic.com/_resources/news/nr-20241127.pdf",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Lithium Ionic Corp. … is pleased to announce the receipt of a non-binding Letter of Interest (“LOI”) from the Export-Import Bank of the United States (“EXIM”) to provide up to US$266 million in debt financing for its 100%-owned flagship Bandeira Lithium Project (“Bandeira” or the “Project”), located in Minas Gerais, Brazil. This funding represents 100% of the capital expenditure (“CAPEX”) outlined in the May 2024 Feasibility Study … Maximum repayment term of 15 years.",
        "note": "Opened Lithium Ionic EXIM LOI PDF release.",
    },
    {
        "id": "lithium_ionic_exim_20241127",
        "type": "company",
        "chicago": "Lithium Ionic Corp. “Lithium Ionic Secures LOI from EXIM for US$266M, Representing 100% of Bandeira Project CAPEX.” 27 November 2024.",
        "url": "https://www.lithiumionic.com/_resources/news/nr-20241127.pdf",
        "annotation": "Company primary on EXIM non-binding LOI up to USD 266m for Bandeira. Supports lithium_ionic_exim_loi_266m_2024.",
        "supports": ["lithium_ionic_exim_loi_266m_2024", "hunt_res_lithium"],
    },
)

# ---------------------------------------------------------------------------
# 11 resources/copper — Capstone Mantoverde Optimized USD 176m (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "capstone_mantoverde_optimized_176m_2025",
        "layer": "resources",
        "subcategory": "copper",
        "side": "allied",
        "counterpart": "Capstone Copper — Mantoverde Optimized sulphide concentrator expansion",
        "country": "Chile",
        "asset": "Q3 2025 sanction / under construction through Q2 2026 reporting: Mantoverde Optimized brownfield expansion raises sulphide concentrator design throughput from 32,000 to 45,000 tpd; incremental ~20 ktpa Cu and ~6 koz Au; mine life 19→25 years; capital cost estimate USD 176 million unchanged; tie-in expected Q3 2026 with ramp-up Q4 2026. Capstone 70% ownership (100% basis figures). Distinct from BHP Escondida / FCX El Abra / Centinela.",
        "investment_type": "brownfield_expansion",
        "value": "176000000",
        "currency": "USD",
        "value_usd": "176000000",
        "fx_usd": "1",
        "fx_date": "2025-09-30",
        "year": "2025",
        "status": "active",
        "lat": "-26.55",
        "lon": "-70.35",
        "geo_note": "Mantoverde mine, Atacama Region, Chile (Capstone sulphide plant pin).",
        "evidence": "documented",
        "source_id": "capstone_q2_2026_mv_optimized",
        "note": "Actor: Capstone Copper (Canadian) — allied. Company Q2 2026 results; USD 176m CAPEX estimate documented.",
    },
    {
        "id": "capstone_mantoverde_optimized_176m_2025",
        "retrieved": "2026-10-01",
        "source_id": "capstone_q2_2026_mv_optimized",
        "url": "https://capstonecopper.com/news/capstone-copper-reports-second-quarter-2026-results/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "MV Optimized, a capital-efficient brownfield expansion of Mantoverde’s sulphide concentrator, was sanctioned for development during Q3 2025. MV Optimized is expected to increase concentrator design throughput from 32,000 to 45,000 ore tonnes per day, providing incremental copper and gold production of approximately 20,000 tonnes and 6,000 ounces of gold per annum, respectively, and extending the mine life from 19 to 25 years, at an estimated capital cost of $176 million, which is unchanged. … The capital cost estimate of $176 million is unchanged.",
        "note": "Opened Capstone Copper Q2 2026 results on MV Optimized.",
    },
    {
        "id": "capstone_q2_2026_mv_optimized",
        "type": "company",
        "chicago": "Capstone Copper Corp. “Capstone Copper Reports Second Quarter 2026 Results.” 2026.",
        "url": "https://capstonecopper.com/news/capstone-copper-reports-second-quarter-2026-results/",
        "annotation": "Company primary on Mantoverde Optimized USD 176m brownfield expansion. Supports capstone_mantoverde_optimized_176m_2025.",
        "supports": ["capstone_mantoverde_optimized_176m_2025", "hunt_res_copper"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None:
                existing[k] = v
        # merge supports
        supports = list(dict.fromkeys((existing.get("supports") or []) + (bib_entry.get("supports") or [])))
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
        "hunt_energy_wind": "Cycle 52: logged engie_serra_assurua_846mw_2025 (allied; 846 MW / R$6bn full COD).",
        "hunt_infra_engineering_epc": "Cycle 52: logged xinhai_st_george_araxa_epc_mou_2025 (PRC; A$8m / EPCM MoU).",
        "hunt_energy_solar": "Cycle 52: logged contourglobal_los_maitenes_chile_2026 (U.S.; 131 MWp + 90 MW BESS).",
        "hunt_energy_fission_smr": "Cycle 52: equal budget; Peru/Argentina FIRST / El Salvador 123 already (miss).",
        "hunt_fenb_araxa": "Cycle 52: logged st_george_boston_metal_moe_mou_2026 (U.S.; MOE FeNb trial MoU).",
        "hunt_infra_building_materials": "Cycle 52: equal budget; Holcim Pacasmayo / Cemex Colombia already (miss).",
        "hunt_latam_rail_telecom": "Cycle 52: logged crrc_sp_metro_frota_r_44_2025 (PRC; R$3.104bn Frota R).",
        "hunt_br_power_equip": "Cycle 52: logged engie_asa_branca_tx_2p7bn_2025 (allied; ~1,000 km / BRL 2.7bn).",
        "hunt_res_nickel": "Cycle 52: equal budget; DFC Piauí / Jervois / Westwin already (miss).",
        "hunt_res_lithium": "Cycle 52: logged lithium_ionic_exim_loi_266m_2024 (U.S.; EXIM LOI up to USD 266m).",
        "hunt_res_copper": "Cycle 52: logged capstone_mantoverde_optimized_176m_2025 (allied; USD 176m).",
        "hunt_infra_port_ownership": "Cycle 52: equal budget; SSA / DFC Yilport / APM already (miss).",
        "hunt_res_balsa": "Cycle 52: equal budget; CoreLite / Plantabal / Gurit already (miss).",
        "hunt_res_water": "Cycle 52: equal budget; AIIB Aguas Pacífico / Newmont / Barrick already (miss).",
        "hunt_infra_port_cranes": "Cycle 52: equal budget; Konecranes / SSA / ZPMC already (miss).",
        "hunt_infra_bridges_roads": "Cycle 52: equal budget; CHEC / Mota-Engil / CRBC already (miss).",
        "hunt_res_graphite": "Cycle 52: equal budget; Graphcoa / South Star / Atlas already (miss).",
        "hunt_energy_other_renewables": "Cycle 52: equal budget; ContourGlobal Oasis / CIP / AES already (miss).",
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
    print("Cycle 52 rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
