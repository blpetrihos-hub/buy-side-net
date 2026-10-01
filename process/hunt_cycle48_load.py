#!/usr/bin/env python3
"""Cycle 48 hunt: shuffle_seed=20261048; equal budget; U.S. side ≥1/3; thin_topup after.

Order: port_ownership, wind, nickel, lithium, other_renewables, power_plants_grid,
niobium, bridges_roads, graphite, balsa, engineering_epc, solar, water, port_cranes,
copper, rail, fission_smr, building_materials.
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
# 1 infrastructure/port_ownership — SSA Guaymas TUM concession (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ssa_guaymas_tum_concession_2025",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "us",
        "counterpart": "SSA Marine México — Guaymas Multi-Use Terminal (TUM) concession",
        "country": "Mexico",
        "asset": "15 Oct 2025: SSA Marine México signs partial rights-transfer / concession to operate a new Multi-Use Terminal at Port of Guaymas (Sonora) under PMDP 2022–2027: 106,439.689 m² for general cargo, containers, and autos; Phase 1 Dock T1 329×40 m at 16 m depth plus 44,236 m² container yard; 18-year term with extension option. Distinct from ssa_guaymas_sts_ertg_2026 (STS/eRTG equipment delivery only).",
        "investment_type": "concession",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "27.92",
        "lon": "-110.89",
        "geo_note": "Port of Guaymas, Sonora (northern multipurpose terminal pin).",
        "evidence": "documented",
        "source_id": "ssa_mexico_guaymas_tum_20251016",
        "note": "Actor: SSA Marine / Carrix (U.S.) via SSA Marine México — us. Company news 16 Oct 2025; CAPEX USD not disclosed on opened page.",
    },
    {
        "id": "ssa_guaymas_tum_concession_2025",
        "retrieved": "2026-10-01",
        "source_id": "ssa_mexico_guaymas_tum_20251016",
        "url": "https://www.ssamarine.mx/ssa-ing/newsdetails?id=245",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "On October 15, we had the honor of signing … the partial rights transfer agreement that will allow SSA Marine Mexico to operate a new Multi-Use Terminal (TUM) at the Port of Guaymas, Sonora. … It will cover a total land area of 106,439.689 square meters … The concession … is valid for 18 years with the possibility of extension.",
        "note": "Opened SSA Marine México English news page on Guaymas TUM concession.",
    },
    {
        "id": "ssa_mexico_guaymas_tum_20251016",
        "type": "company",
        "chicago": "SSA Marine México. “SSA Marine Mexico to Operate New Multi-Use Terminal at the Port of Guaymas.” 16 October 2025.",
        "url": "https://www.ssamarine.mx/ssa-ing/newsdetails?id=245",
        "annotation": "Company primary on Guaymas TUM partial rights transfer / 18-year concession. Supports ssa_guaymas_tum_concession_2025.",
        "supports": ["ssa_guaymas_tum_concession_2025", "hunt_infra_port_ownership"],
    },
)

# ---------------------------------------------------------------------------
# 1b infrastructure/port_ownership — DP World Caucedo USD 760m MoU (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "dpworld_caucedo_760m_2025",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "DP World — Port of Caucedo + Free Trade Zone expansion MoU",
        "country": "Dominican Republic",
        "asset": "9 May 2025: DP World signs USD 760 million MoU with Dominican MICM to expand Port of Caucedo and FTZ — split USD 380m port (quay/breakwater, STS cranes, yard, gates/automation) + USD 380m FTZ (roads, utilities, pre-built storage); capacity 2.5→~3.1m TEU; +225 ha FTZ land. Distinct from DP World Callao/Posorja/Santos ownership rows.",
        "investment_type": "concession",
        "value": "760000000",
        "currency": "USD",
        "value_usd": "760000000",
        "fx_usd": "1",
        "fx_date": "2025-05-09",
        "year": "2025",
        "status": "active",
        "lat": "18.43",
        "lon": "-69.63",
        "geo_note": "Port of Caucedo, Dominican Republic (terminal/FTZ pin).",
        "evidence": "documented",
        "source_id": "dpworld_caucedo_20250509",
        "note": "Actor: DP World (UAE) — allied. Company Americas release 9 May 2025. MoU initiates negotiations; CAPEX as stated package.",
    },
    {
        "id": "dpworld_caucedo_760m_2025",
        "retrieved": "2026-10-01",
        "source_id": "dpworld_caucedo_20250509",
        "url": "https://www.dpworld.com/en/news/usa/dp-world-signs-agreement-to-expand-port-caucedo-in-dominican-republic",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "DP World has signed a landmark US$760 million Memorandum of Understanding (MoU) with the government of the Dominican Republic to expand the Port of Caucedo and its Free Trade Zone … raise Caucedo’s container handling capacity from 2.5 million TEUs … to approximately 3.1 million TEUs … The new $760 million investment will be split evenly: $380 million for the port … $380 million for the Free Trade Zone.",
        "note": "Opened DP World Americas release on Caucedo MoU.",
    },
    {
        "id": "dpworld_caucedo_20250509",
        "type": "company",
        "chicago": "DP World. “DP World Signs Agreement to Launch $760M Port and Free Trade Zone in Dominican Republic.” 9 May 2025.",
        "url": "https://www.dpworld.com/en/news/usa/dp-world-signs-agreement-to-expand-port-caucedo-in-dominican-republic",
        "annotation": "Company primary on Caucedo USD 760m port+FTZ MoU. Supports dpworld_caucedo_760m_2025.",
        "supports": ["dpworld_caucedo_760m_2025", "hunt_infra_port_ownership"],
    },
)

# ---------------------------------------------------------------------------
# 3 resources/nickel — Jervois SMP Class 1 refinery restart underway (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "jervois_smp_restart_construction_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "us",
        "counterpart": "Jervois — São Miguel Paulista Ni–Co Class 1 refinery restart (construction underway)",
        "country": "Brazil",
        "asset": "Jervois company asset page (2026 project update): refurbishment/construction restart of São Miguel Paulista electrolytic Class 1 nickel–cobalt refinery underway through 2026–2027; targeted output 12,000 tpa Ni and 2,000 tpa Co metal cathode — only Class 1 refinery in Latin America once restarted. Processor/smelter-restart angle; distinct from jervois_smp_eu_crma_status_2026 (CRMA designation only) and from offtake/financing rows.",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.50",
        "lon": "-46.44",
        "geo_note": "São Miguel Paulista neighbourhood, eastern São Paulo (refinery pin).",
        "evidence": "documented",
        "source_id": "jervois_smp_asset_page_2026",
        "note": "Actor: Jervois (U.S.-listed / Australia-headquartered; coded us with prior SMP rows) — us. No CAPEX USD on opened page.",
    },
    {
        "id": "jervois_smp_restart_construction_2026",
        "retrieved": "2026-10-01",
        "source_id": "jervois_smp_asset_page_2026",
        "url": "https://jervoisglobal.com/assets/sao-miguel-paulista-refinery/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The refurbishment and construction project to restart the São Miguel Paulista nickel cobalt refinery is underway; once back in operation, it will be the only Class 1 refinery in Latin America. We are expecting to produce 12,000 metric tons of refined nickel metal and 2,000 metric tons of cobalt metal each year … Work has commenced on the refurbishment and restart project, which we anticipate will continue across 2026 and 2027.",
        "note": "Opened Jervois SMP asset page for construction-underway processor angle.",
    },
    {
        "id": "jervois_smp_asset_page_2026",
        "type": "company",
        "chicago": "Jervois. “São Miguel Paulista Refinery.” Company asset page (refurbishment/restart project update).",
        "url": "https://jervoisglobal.com/assets/sao-miguel-paulista-refinery/",
        "annotation": "Company primary on SMP Class 1 Ni–Co refinery restart construction through 2026–27. Supports jervois_smp_restart_construction_2026.",
        "supports": ["jervois_smp_restart_construction_2026", "jervois_smp_eu_crma_status_2026", "hunt_res_nickel"],
    },
)

# ---------------------------------------------------------------------------
# 11 infrastructure/engineering_epc — Ausenco EPCM for Jervois SMP (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ausenco_jervois_smp_epcm_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "Ausenco — EPCM for Jervois São Miguel Paulista Ni–Co refinery restart",
        "country": "Brazil",
        "asset": "30 Dec 2025 contract / Jan 2026 mobilisation: Ausenco EPCM through pre-commissioning for Jervois Brasil SMP nickel–cobalt refinery revitalisation (São Paulo); ~50 Ausenco professionals; plant targeted 12,000 tpy Ni / 2,000 tpy Co. Distinct from Bechtel/Fluor/Wabtec Contagem engineering rows.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.50",
        "lon": "-46.44",
        "geo_note": "SMP refinery, São Miguel Paulista, São Paulo (project site pin).",
        "evidence": "documented",
        "source_id": "gmr_ausenco_jervois_20260119",
        "note": "Actor: Ausenco (Canada) — allied. Global Mining Review 19 Jan 2026 citing Ausenco mobilisation after 30 Dec EPCM signing. CAPEX not disclosed.",
    },
    {
        "id": "ausenco_jervois_smp_epcm_2026",
        "retrieved": "2026-10-01",
        "source_id": "gmr_ausenco_jervois_20260119",
        "url": "https://www.globalminingreview.com/mining/19012026/ausenco-to-revitalise-jervois-nickel-and-cobalt-refinery/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The mobilisation comes after Ausenco and Jervois Brasil signed an engineering, procurement, and construction management (EPCM) contract on 30 December. Ausenco will be responsible for the engineering, up to pre-commissioning, of the nickel and cobalt refinery, located in the São Miguel Paulista (SMP) neighbourhood … The forecast is to produce 12 000 tpy of nickel and 2000 tpy of cobalt.",
        "note": "Opened Global Mining Review Ausenco–Jervois EPCM notice.",
    },
    {
        "id": "gmr_ausenco_jervois_20260119",
        "type": "press",
        "chicago": "Global Mining Review. “Ausenco to revitalise Jervois nickel and cobalt refinery.” 19 January 2026.",
        "url": "https://www.globalminingreview.com/mining/19012026/ausenco-to-revitalise-jervois-nickel-and-cobalt-refinery/",
        "annotation": "Trade press on Ausenco EPCM mobilisation for Jervois SMP restart. Supports ausenco_jervois_smp_epcm_2026.",
        "supports": ["ausenco_jervois_smp_epcm_2026", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 12 energy/solar — ContourGlobal Víctor Jara hybrid COD (U.S./KKR)
# ---------------------------------------------------------------------------
A(
    {
        "id": "contourglobal_victor_jara_cod_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "us",
        "counterpart": "ContourGlobal (KKR) — Víctor Jara solar PV + long-duration BESS COD",
        "country": "Chile",
        "asset": "27 May 2026: ContourGlobal announces start of operations of BESS at Víctor Jara hybrid plant (Tarapacá): 231 MWp solar PV paired with ~1.3 GWh / 6.5-hour / 200 MW BESS; night-only 15-year PPA with Copec EMOAC. COD milestone for solar-plus-storage asset within Oasis de Atacama portfolio acquired Dec 2024 — distinct from contourglobal_oasis_atacama_ev_2024 (portfolio EV acquisition).",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-20.27",
        "lon": "-69.63",
        "geo_note": "Víctor Jara hybrid plant, Tarapacá Region (project pin; approximate).",
        "evidence": "documented",
        "source_id": "contourglobal_victor_jara_20260527",
        "note": "Actor: ContourGlobal owned by KKR (U.S. PE) — us. Company release 27 May 2026 COD; no new CAPEX on page (prior EV already logged).",
    },
    {
        "id": "contourglobal_victor_jara_cod_2026",
        "retrieved": "2026-10-01",
        "source_id": "contourglobal_victor_jara_20260527",
        "url": "https://www.contourglobal.com/news/contourglobal-inaugurates-a-hybrid-solar-pv-plant-in-chile-with-a-6-5-hour-battery-storage-system-latin-americas-longest-duration-utility-scale-bess/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "ContourGlobal announced the start of operations of the battery energy storage system (BESS) at the Victor Jara hybrid plant, in Tarapacá, Chile, capable of delivering 6.5 hours of continuous power output. Paired with the on-site 231 MWp solar PV plant, the storage system enables the delivery of up to 200 MW of clean energy long after sunset … ContourGlobal’s solar-plus-storage portfolio in Chile is now fully operational and includes the Victor Jara project (231 MWp solar PV combined with a 1.3 GWh battery system).",
        "note": "Opened ContourGlobal Víctor Jara COD release.",
    },
    {
        "id": "contourglobal_victor_jara_20260527",
        "type": "company",
        "chicago": "ContourGlobal. “ContourGlobal inaugurates a hybrid solar PV plant in Chile with a 6.5-hour battery storage system: Latin America’s longest-duration utility-scale BESS.” 27 May 2026.",
        "url": "https://www.contourglobal.com/news/contourglobal-inaugurates-a-hybrid-solar-pv-plant-in-chile-with-a-6-5-hour-battery-storage-system-latin-americas-longest-duration-utility-scale-bess/",
        "annotation": "Company primary on Víctor Jara 231 MWp + 1.3 GWh BESS COD. Supports contourglobal_victor_jara_cod_2026.",
        "supports": ["contourglobal_victor_jara_cod_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 13 resources/water — Barrick Pueblo Viejo ETP + RO (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "barrick_pueblo_viejo_etp_ro_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Barrick — Pueblo Viejo new effluent treatment plant + RO engineering (Naranjo MLE)",
        "country": "Dominican Republic",
        "asset": "Q2 2026 Barrick results: Pueblo Viejo mine-life extension advances Naranjo TSF with temporary water-management structure permits secured; construction underway on new effluent treatment plant; reverse-osmosis plant engineering ongoing; H2 2026 water-management scope definition planned. Water-treatment angle of MLE — distinct from Newmont Yanacocha water rows; no isolated water CAPEX split on opened page.",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "18.91",
        "lon": "-70.17",
        "geo_note": "Pueblo Viejo mine, Sánchez Ramírez Province (site pin).",
        "evidence": "documented",
        "source_id": "barrick_q2_2026_results",
        "note": "Actor: Barrick Mining (Canada/US-listed; coded us for North American operator group convention on U.S.-market filings — Barrick is Canadian; RECODE to allied). Wait — Barrick is Canadian → allied.",
    },
    {
        "id": "barrick_pueblo_viejo_etp_ro_2026",
        "retrieved": "2026-10-01",
        "source_id": "barrick_q2_2026_results",
        "url": "https://www.barrick.com/English/news/news-details/2026/q2-2026-results/default.aspx",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Pueblo Viejo's expansion advanced as focus shifted toward the Naranjo tailings storage facility, with temporary water management structures permits secured and starter dam permit approval targeted for Q1 2027. Construction remains underway for Haul Roads 17 and 19, the diorite crusher, and the new effluent treatment plant, alongside ongoing engineering for the reverse osmosis plant … and planned H2 2026 water management scope definition.",
        "note": "Opened Barrick Q2 2026 results page.",
    },
    {
        "id": "barrick_q2_2026_results",
        "type": "company",
        "chicago": "Barrick Mining Corporation. “Barrick Reports Second Quarter 2026 Results.” 2026.",
        "url": "https://www.barrick.com/English/news/news-details/2026/q2-2026-results/default.aspx",
        "annotation": "Company Q2 2026 results noting Pueblo Viejo effluent treatment plant construction and RO engineering. Supports barrick_pueblo_viejo_etp_ro_2026.",
        "supports": ["barrick_pueblo_viejo_etp_ro_2026", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 15 resources/copper — Southern Copper Ilo smelter USD 1.3bn (other)
# ---------------------------------------------------------------------------
A(
    {
        "id": "southern_copper_ilo_fundicion_1p3bn_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "other",
        "counterpart": "Southern Copper / Southern Perú — Fundición Ilo expansion (smelter)",
        "country": "Peru",
        "asset": "May 2026 company presentation lists Fundición Ilo among Peru growth projects at US$1.3 billion (alongside Fundición Empalme US$1.1bn and Tía María US$1.8bn). Smelter/processor angle for Ilo metallurgical complex (Moquegua) — distinct from southern_copper_tia_maria_2025 mine project.",
        "investment_type": "other",
        "value": "1300000000",
        "currency": "USD",
        "value_usd": "1300000000",
        "fx_usd": "1",
        "fx_date": "2026-05-26",
        "year": "2026",
        "status": "active",
        "lat": "-17.64",
        "lon": "-71.34",
        "geo_note": "Ilo metallurgical complex, Moquegua (smelter pin).",
        "evidence": "documented",
        "source_id": "southern_copper_pp_20260526",
        "note": "Actor: Southern Copper / Grupo México (Mexico) — other. Company May 2026 presentaión lists Fundición Ilo US$1.3B in investment program.",
    },
    {
        "id": "southern_copper_ilo_fundicion_1p3bn_2026",
        "retrieved": "2026-10-01",
        "source_id": "southern_copper_pp_20260526",
        "url": "https://southerncoppercorp.com/wp-content/uploads/2026/05/pp260526.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "FUNDICIÓN ILO  US$1.3 B",
        "note": "Opened Southern Copper May 2026 company presentation PDF (pp260526).",
    },
    {
        "id": "southern_copper_pp_20260526",
        "type": "company",
        "chicago": "Southern Copper Corporation. “Presentación de la Compañía.” May 2026 investor presentation (pp260526.pdf).",
        "url": "https://southerncoppercorp.com/wp-content/uploads/2026/05/pp260526.pdf",
        "annotation": "Company presentation listing Fundición Ilo at US$1.3B. Supports southern_copper_ilo_fundicion_1p3bn_2026.",
        "supports": ["southern_copper_ilo_fundicion_1p3bn_2026", "hunt_res_copper"],
    },
)

# ---------------------------------------------------------------------------
# 16 infrastructure/rail — CRRC Araraquara train factory (PRC)
# ---------------------------------------------------------------------------
A(
    {
        "id": "crrc_araraquara_factory_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "prc",
        "counterpart": "CRRC Brasil / Consórcio C2 — Araraquara rolling-stock factory",
        "country": "Brazil",
        "asset": "25 Mar 2026: installation ceremony for CRRC Brasil Equipamentos Ferroviários factory at former Hyundai plant in Araraquara (SP); Consórcio C2 (CRRC + Comporte) to produce TIC Eixo Norte trains and São Paulo Metro compositions (44 metro trains in Novo PAC package); operations targeted 2H 2026 with deliveries from 2027. Manufacturing presence — distinct from CRRC Salvador/Buenos Aires/Mexico rolling-stock supply rows. BNDES R$5.6bn contracts signed same day are SP state financing, not CRRC CAPEX.",
        "investment_type": "other",
        "value": "",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-21.79",
        "lon": "-48.18",
        "geo_note": "CRRC Brasil plant, Araraquara, São Paulo (factory pin).",
        "evidence": "documented",
        "source_id": "g1_crrc_araraquara_20260325",
        "note": "Actor: CRRC (PRC) + Comporte — prc. G1 25 Mar 2026 ceremony coverage. Factory CAPEX not disclosed; BNDES figures are state financing and not attributed as CRRC investment.",
    },
    {
        "id": "crrc_araraquara_factory_2026",
        "retrieved": "2026-10-01",
        "source_id": "g1_crrc_araraquara_20260325",
        "url": "https://g1.globo.com/sp/sao-carlos-regiao/noticia/2026/03/25/fabrica-de-trens-e-inaugurada-em-araraquara-e-contratos-de-r-56-bilhoes-do-bndes-sao-assinados.ghtml",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Araraquara (SP) realizou … a cerimônia de instalação da fábrica da CRRC Brasil Equipamentos Ferroviários. A unidade integra o Consórcio C2, formado pela empresa chinesa e pela brasileira Comporte Participações. O grupo será responsável pela produção dos trens do Trem Intercidades (TIC) Eixo Norte … A empresa também produzirá composições do metrô de São Paulo.",
        "note": "Opened G1 coverage of CRRC Araraquara factory installation.",
    },
    {
        "id": "g1_crrc_araraquara_20260325",
        "type": "press",
        "chicago": "g1 São Carlos e Araraquara. “Fábrica de trens é inaugurada em Araraquara, e contratos de R$ 5,6 bilhões do BNDES são assinados.” 25 March 2026.",
        "url": "https://g1.globo.com/sp/sao-carlos-regiao/noticia/2026/03/25/fabrica-de-trens-e-inaugurada-em-araraquara-e-contratos-de-r-56-bilhoes-do-bndes-sao-assinados.ghtml",
        "annotation": "Brazilian press on CRRC Araraquara factory installation and related BNDES SP mobility contracts. Supports crrc_araraquara_factory_2026.",
        "supports": ["crrc_araraquara_factory_2026", "hunt_latam_rail_telecom"],
    },
)

# ---------------------------------------------------------------------------
# 16b infrastructure/rail — PowerChina Chancay–Sierra Central USD 420m (PRC)
# ---------------------------------------------------------------------------
A(
    {
        "id": "powerchina_chancay_sierra_420m_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "prc",
        "counterpart": "PowerChina — Ferrocarril Chancay–Sierra Central EPC",
        "country": "Peru",
        "asset": "Jan 2026: Peru awards Power Construction Corporation of China (PowerChina) ~120 km freight railway linking Megapuerto de Chancay with Sierra Central; investment US$420 million; ~36-month build; ops targeted 2028; Andes alignment with tunnels/viaducts for mineral freight (Cu/Li). Distinct from Cosco Chancay port-ownership and Lima–Ica proposals.",
        "investment_type": "epc",
        "value": "420000000",
        "currency": "USD",
        "value_usd": "420000000",
        "fx_usd": "1",
        "fx_date": "2026-01-23",
        "year": "2026",
        "status": "active",
        "lat": "-11.59",
        "lon": "-77.27",
        "geo_note": "Chancay port end of corridor, Huaral Province (coastal terminus pin).",
        "evidence": "proxy",
        "source_id": "larepublica_chancay_sierra_20260123",
        "note": "Actor: PowerChina (PRC SOE) — prc. UNVERIFIED proxy: La República 23/29 Jan 2026 reporting award and US$420m; official ProInversión/MTC award PDF not opened this cycle.",
    },
    {
        "id": "powerchina_chancay_sierra_420m_2026",
        "retrieved": "2026-10-01",
        "source_id": "larepublica_chancay_sierra_20260123",
        "url": "https://larepublica.pe/sociedad/2026/01/23/peru-adjudica-proyecto-del-tren-que-unira-el-megapuerto-de-chancay-con-la-sierra-central-atravesara-la-cordillera-de-los-andes-y-tendra-una-inversion-de-us420-millones-1375860",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "La concesión fue otorgada a Power Construction Corporation of China … El ferrocarril Chancay–sierra central, con una longitud aproximada de 120 kilómetros … La inversión estimada para la ejecución de la obra asciende a US$420 millones y el plazo de construcción fue fijado en alrededor de 36 meses. El inicio de operaciones está proyectado para el año 2028.",
        "note": "Opened La República coverage of PowerChina Chancay–Sierra award.",
    },
    {
        "id": "larepublica_chancay_sierra_20260123",
        "type": "press",
        "chicago": "Torres, Aarón. “Perú adjudica proyecto del tren que unirá el Megapuerto de Chancay con la sierra central … inversión de US$420 millones.” La República, 23 January 2026 (updated 29 January 2026).",
        "url": "https://larepublica.pe/sociedad/2026/01/23/peru-adjudica-proyecto-del-tren-que-unira-el-megapuerto-de-chancay-con-la-sierra-central-atravesara-la-cordillera-de-los-andes-y-tendra-una-inversion-de-us420-millones-1375860",
        "annotation": "UNVERIFIED proxy press on PowerChina Chancay–Sierra Central US$420m award. Supports powerchina_chancay_sierra_420m_2026.",
        "supports": ["powerchina_chancay_sierra_420m_2026", "hunt_latam_rail_telecom"],
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
    # Fix Barrick side to allied (Canadian) before write
    for row, _e, _b in ITEMS:
        if row["id"] == "barrick_pueblo_viejo_etp_ro_2026":
            row["side"] = "allied"
            row["note"] = (
                "Actor: Barrick Mining Corporation (Canada) — allied. "
                "Q2 2026 results: ETP construction + RO engineering under Naranjo MLE; "
                "no isolated water CAPEX split on page."
            )

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
        "hunt_infra_port_ownership": "Cycle 48: logged ssa_guaymas_tum_concession_2025 (U.S.) + dpworld_caucedo_760m_2025 (allied; USD 760m MoU).",
        "hunt_energy_wind": "Cycle 48: equal budget; Envision Casa dos Ventos 630 MW / Vestas / Goldwind already (miss).",
        "hunt_res_nickel": "Cycle 48: logged jervois_smp_restart_construction_2026 (U.S.; Class 1 refinery restart underway — processor angle, not financing duplicate).",
        "hunt_res_lithium": "Cycle 48: equal budget; PPG / Albemarle TED / EnergyX EXIM / Eni Black Giant already (miss).",
        "hunt_energy_other_renewables": "Cycle 48: equal budget; ContourGlobal Oasis EV / CATL La Alegría / AES Pampas already (miss).",
        "hunt_br_power_equip": "Cycle 48: equal budget; GE Vernova Azulão / PowerChina Coca Codo already (miss).",
        "hunt_fenb_araxa": "Cycle 48: equal budget; Codemig/CBMM R$13bn / 2026 spend already (miss).",
        "hunt_infra_bridges_roads": "Cycle 48: equal budget; CHEC/Mota-Engil already; PowerChina Chancay coded rail (miss).",
        "hunt_res_graphite": "Cycle 48: equal budget; Graphcoa Jordânia / Boa Sorte / South Star already (miss).",
        "hunt_res_balsa": "Cycle 48: equal budget; Plantabal revenue/FSC/planting already dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 48: logged ausenco_jervois_smp_epcm_2026 (allied; EPCM for SMP restart).",
        "hunt_energy_solar": "Cycle 48: logged contourglobal_victor_jara_cod_2026 (U.S./KKR; 231 MWp + 1.3 GWh COD).",
        "hunt_res_water": "Cycle 48: logged barrick_pueblo_viejo_etp_ro_2026 (allied; ETP construction + RO engineering).",
        "hunt_infra_port_cranes": "Cycle 48: equal budget; SSA Guaymas STS/eRTG already (miss).",
        "hunt_res_copper": "Cycle 48: logged southern_copper_ilo_fundicion_1p3bn_2026 (other; Fundición Ilo US$1.3bn smelter).",
        "hunt_latam_rail_telecom": "Cycle 48: logged crrc_araraquara_factory_2026 (PRC) + powerchina_chancay_sierra_420m_2026 (PRC; US$420m proxy).",
        "hunt_energy_fission_smr": "Cycle 48: equal budget; Meitner ACR-300 / FIRST / Rosatom already (miss).",
        "hunt_infra_building_materials": "Cycle 48: equal budget; Holcim–Cemex Colombia USD 485m already (miss).",
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
    print("Cycle 48 rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
