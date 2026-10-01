#!/usr/bin/env python3
"""Cycle 43 hunt: shuffle_seed=20261043; equal budget; U.S. side ≥1/3; thin_topup after.

Order: nickel, other_renewables, lithium, rail, port_ownership, water,
building_materials, port_cranes, wind, bridges_roads, fission_smr, solar,
niobium, graphite, balsa, engineering_epc, power_plants_grid, copper.
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
UPDATES: list[tuple[str, dict, dict | None, dict | None]] = []


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def U(rid, row_patch, evidence=None, bib=None):
    UPDATES.append((rid, row_patch, evidence, bib))


# ---------------------------------------------------------------------------
# 1 resources/nickel — equal-budget miss (U.S. search: DFC PNP LOI / Jervois SMP /
#   Centaurus Jaguar intl finance already logged; no distinct new U.S. financing
#   primary opened this box).
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 2 energy/other_renewables — AES Andes Solar III COD; Andes Solar Hub >USD 1.3bn
# ---------------------------------------------------------------------------
A(
    {
        "id": "aes_andes_solar_iii_hub_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "AES Andes / AES Corporation — Andes Solar III + hub (Antofagasta)",
        "country": "Chile",
        "asset": "14 Apr 2026: AES announces commercial operations at Andes Solar III (171 MW PV + 171 MW / 3-hour BESS) in Antofagasta Region; Andes Solar Hub now 692 MW PV + 510 MW BESS with cumulative investment exceeding USD 1.3 billion. Pipeline >2,000 MW COD 2026–2027 cited. Coded other_renewables for co-located storage-backed solar hub (same convention as aes_andes_pampas_cristales_2025).",
        "investment_type": "greenfield_storage",
        "value": "1300000000",
        "currency": "USD",
        "value_usd": "1300000000",
        "fx_usd": "1",
        "fx_date": "2026-04-14",
        "year": "2026",
        "status": "active",
        "lat": "-23.65",
        "lon": "-70.25",
        "geo_note": "Andes Solar Hub / Antofagasta Region (company geography; approximate hub pin).",
        "evidence": "documented",
        "source_id": "aes_chile_andes_solar_iii_20260414",
        "note": "Actor: AES Andes / AES Corporation (U.S.) — us. Company English press 14 Apr 2026. Hub cumulative CAPEX >USD 1.3bn; Andes III is the COD milestone. Distinct from aes_andes_pampas_cristales_2025 / aes_pampas_pf_550m_2025.",
    },
    {
        "id": "aes_andes_solar_iii_hub_2026",
        "retrieved": "2026-10-01",
        "source_id": "aes_chile_andes_solar_iii_20260414",
        "url": "https://www.aeschile.com/en/press-release/aes-chile-adds-new-project-largest-solar-and-storage-hub-latin-america",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "After nearly a decade of development and more than US$1.3 billion in total investment, the company has completed another milestone within its Andes Solar Hub, reaching 692 MW of photovoltaic capacity and 510 MW of battery‑based storage. … Andes Solar III is a photovoltaic plant with 171 MW of installed solar capacity and a 171 MW / three‑hour battery energy storage system (BESS).",
        "note": "Opened AES Chile English press release 14 Apr 2026.",
    },
    {
        "id": "aes_chile_andes_solar_iii_20260414",
        "type": "company",
        "chicago": "AES Chile. “AES Chile adds a new project to the largest solar and storage hub in Latin America.” 14 April 2026.",
        "url": "https://www.aeschile.com/en/press-release/aes-chile-adds-new-project-largest-solar-and-storage-hub-latin-america",
        "annotation": "Company primary on Andes Solar III COD and >USD 1.3bn hub cumulative. Supports aes_andes_solar_iii_hub_2026.",
        "supports": ["aes_andes_solar_iii_hub_2026", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# 3 resources/lithium — EXIM Argentina Build the Future up to USD 7bn (U.S.);
#   Ganfeng USD 130m debt facility to Lithium Argentina (PRC)
# ---------------------------------------------------------------------------
A(
    {
        "id": "exim_argentina_build_future_7bn_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "us",
        "counterpart": "U.S. EXIM — Argentina Build the Future Framework (critical minerals)",
        "country": "Argentina",
        "asset": "23 Sep 2026: EXIM signs U.S.–Argentina Build the Future Framework to mobilize financing of up to USD 7 billion through 2027 for priority sectors including critical minerals development and processing, energy security and grid modernization, digital connectivity, and commercial space/advanced technologies. Critical-minerals cooperation framed under EXIM Supply Chain Resiliency Initiative (SCRI). Framework — not a closed project loan.",
        "investment_type": "financing",
        "value": "7000000000",
        "currency": "USD",
        "value_usd": "7000000000",
        "fx_usd": "1",
        "fx_date": "2026-09-23",
        "year": "2026",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "Country-level financing framework; no single mine/plant named — intentionally off-map.",
        "evidence": "documented",
        "source_id": "exim_argentina_build_future_20260923",
        "note": "Actor: U.S. EXIM with Government of Argentina — us. Official EXIM release 23 Sep 2026. Coded under lithium as Argentina’s flagship critical-mineral sector named in SCRI framing; also covers grid/energy. Framework ceiling, not a disbursed project facility. Complements chilean_cobalt_exim_loi_375m_2026 (project LOI).",
    },
    {
        "id": "exim_argentina_build_future_7bn_2026",
        "retrieved": "2026-10-01",
        "source_id": "exim_argentina_build_future_20260923",
        "url": "https://www.exim.gov/news/exim-signs-7-billion-argentina-build-future-framework-prioritize-energy-security-and-critical",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Today, the Export-Import Bank of the United States (EXIM) signed a U.S.-Argentina Build the Future Framework with the Government of Argentina to mobilize financing of up to $7 billion through 2027 for priority sectors, including critical minerals development and processing, energy security and grid modernization, digital connectivity and secure systems, and commercial space and advanced technologies.",
        "note": "Opened EXIM.gov press release 23 Sep 2026.",
    },
    {
        "id": "exim_argentina_build_future_20260923",
        "type": "official",
        "chicago": "Export-Import Bank of the United States. “EXIM Signs $7 Billion U.S.-Argentina Build the Future Framework to Prioritize Energy Security and Critical Minerals Development.” 23 September 2026.",
        "url": "https://www.exim.gov/news/exim-signs-7-billion-argentina-build-future-framework-prioritize-energy-security-and-critical",
        "annotation": "Official EXIM framework up to USD 7bn for Argentina critical minerals/energy. Supports exim_argentina_build_future_7bn_2026.",
        "supports": ["exim_argentina_build_future_7bn_2026", "hunt_res_lithium"],
    },
)

A(
    {
        "id": "ganfeng_lar_debt_130m_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "Ganfeng Lithium — USD 130m debt facility to Lithium Argentina",
        "country": "Argentina",
        "asset": "Q1 2026: Lithium Argentina completes USD 130 million six-year debt facility from Ganfeng at SOFR+2.5% to support refinancing of corporate debt tied to Argentina lithium platform (Cauchari-Olaroz / PPG pipeline). Distinct from ganfeng_laac_convertible_180m_2026 convertible note.",
        "investment_type": "financing",
        "value": "130000000",
        "currency": "USD",
        "value_usd": "130000000",
        "fx_usd": "1",
        "fx_date": "2026-03-31",
        "year": "2026",
        "status": "active",
        "lat": "-23.7",
        "lon": "-66.7",
        "geo_note": "Argentina lithium platform pin (Cauchari-Olaroz / Jujuy–Salta corridor; approximate; facility is corporate).",
        "evidence": "documented",
        "source_id": "lar_edgar_ex992_q1_2026",
        "note": "Actor: Ganfeng Lithium (PRC) lender to Lithium Argentina — prc. SEC EX-99.2 MD&A. Complements convertible note and Pastos Grandes equity rows.",
    },
    {
        "id": "ganfeng_lar_debt_130m_2026",
        "retrieved": "2026-10-01",
        "source_id": "lar_edgar_ex992_q1_2026",
        "url": "https://www.sec.gov/Archives/edgar/data/1440972/000119312526218128/lar-ex99_2.htm",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "In March 2026, the Company completed the $130 million debt facility (“Debt Facility”) from Ganfeng. The Debt Facility has a 6-year term at an interest rate of SOFR plus 2.5% providing increased flexibility to support refinancing the Company’s existing corporate debt.",
        "note": "Opened Lithium Argentina SEC EX-99.2 (Q1 2026 MD&A).",
    },
    {
        "id": "lar_edgar_ex992_q1_2026",
        "type": "filing",
        "chicago": "Lithium Argentina AG. “Management’s Discussion and Analysis — Exhibit 99.2.” U.S. Securities and Exchange Commission EDGAR filing. Accessed 1 October 2026.",
        "url": "https://www.sec.gov/Archives/edgar/data/1440972/000119312526218128/lar-ex99_2.htm",
        "annotation": "Issuer MD&A documenting Ganfeng USD 130m debt facility. Supports ganfeng_lar_debt_130m_2026.",
        "supports": ["ganfeng_lar_debt_130m_2026", "hunt_res_lithium"],
    },
)

# ---------------------------------------------------------------------------
# 4 infrastructure/rail — Mota-Engil Querétaro–Irapuato Tramo I €290m + Tramo II €820m
# ---------------------------------------------------------------------------
# Frankfurter/ECB-style: 2025-08-26 EURUSD=1.1656; 2025-10-20 EURUSD=1.1655
EUR_T1 = 290000000
USD_T1 = int(round(EUR_T1 * 1.1656))
EUR_T2 = 820000000
USD_T2 = int(round(EUR_T2 * 1.1655))

A(
    {
        "id": "mota_engil_qi_tramo1_290m_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "Mota-Engil México — Querétaro–Irapuato Tramo I (30.3 km)",
        "country": "Mexico",
        "asset": "26 Aug 2025: Mota-Engil signs railway design-and-construction contract ~EUR 290 million for first awarded section of Querétaro–Irapuato passenger train (30.3 km; up to ~11,000 daily passengers) under Mexico National Railway Plan.",
        "investment_type": "rail_epc",
        "value": str(EUR_T1),
        "currency": "EUR",
        "value_usd": str(USD_T1),
        "fx_usd": "1.1656",
        "fx_date": "2025-08-26",
        "year": "2025",
        "status": "active",
        "lat": "20.59",
        "lon": "-100.39",
        "geo_note": "Querétaro end of Tramo I / Bajío corridor (company geography; approximate).",
        "evidence": "documented",
        "source_id": "mota_engil_mexico_qi_t1_20250826",
        "note": "Actor: Mota-Engil (Portugal) — allied. Company CMVM/market notice 26 Aug 2025. FX: Frankfurter/ECB EURUSD 1.1656 on 2025-08-26. Distinct from Siemens/Sonda ETCS signaling row and Santos–Guarujá tunnel.",
    },
    {
        "id": "mota_engil_qi_tramo1_290m_2025",
        "retrieved": "2026-10-01",
        "source_id": "mota_engil_mexico_qi_t1_20250826",
        "url": "https://www.mota-engil.com/app/uploads/2025/08/document-19.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Mota-Engil S.G.P.S., S.A. (“MOTA-ENGIL”) informs that it has signed a railway construction contract in Mexico, with a total value of approximately €290 million. The contract includes the design and construction of the first awarded section of the Querétaro–Irapuato train connection, covering a total length of 30.3 km.",
        "note": "Opened Mota-Engil PDF market notice 26 Aug 2025.",
    },
    {
        "id": "mota_engil_mexico_qi_t1_20250826",
        "type": "company",
        "chicago": "Mota-Engil S.G.P.S., S.A. “Mota-Engil Informs on the Signing of Contracts in Portugal, Mexico and Rwanda in a Total Amount of €560 Million.” 26 August 2025.",
        "url": "https://www.mota-engil.com/app/uploads/2025/08/document-19.pdf",
        "annotation": "Company market notice on Querétaro–Irapuato Tramo I ~EUR 290m. Supports mota_engil_qi_tramo1_290m_2025.",
        "supports": ["mota_engil_qi_tramo1_290m_2025", "hunt_latam_rail_telecom"],
    },
)

A(
    {
        "id": "mota_engil_qi_tramo2_820m_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "Mota-Engil México — Querétaro–Irapuato Tramo II Apaseo–Irapuato (70.7 km)",
        "country": "Mexico",
        "asset": "20 Oct 2025: Mota-Engil México signs SICT railway design-and-construction contract ~EUR 820 million for second stretch Apaseo el Grande–Irapuato (70.7 km; ~29 months). Completes Mota-Engil execution of full Querétaro–Irapuato connection after Tramo I.",
        "investment_type": "rail_epc",
        "value": str(EUR_T2),
        "currency": "EUR",
        "value_usd": str(USD_T2),
        "fx_usd": "1.1655",
        "fx_date": "2025-10-20",
        "year": "2025",
        "status": "active",
        "lat": "20.67",
        "lon": "-101.35",
        "geo_note": "Irapuato / Apaseo el Grande corridor, Guanajuato (company geography; approximate).",
        "evidence": "documented",
        "source_id": "mota_engil_mexico_qi_t2_20251020",
        "note": "Actor: Mota-Engil (Portugal) — allied. Company market notice 20 Oct 2025. FX: Frankfurter/ECB EURUSD 1.1655 on 2025-10-20. Distinct from Tramo I row.",
    },
    {
        "id": "mota_engil_qi_tramo2_820m_2025",
        "retrieved": "2026-10-01",
        "source_id": "mota_engil_mexico_qi_t2_20251020",
        "url": "https://www.mota-engil.com/app/uploads/2025/10/Comunicado_20_10_2025_-Mexico_v3JPVvi.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "MOTA-ENGIL MEXICO has signed a new railway construction contract with Secretaria de Infraestructura, Comunicaciones y Transportes … for a total amount of circa of 820 million euros. … design and construction of the second stretch (between Apaseo el Grande and Irapuato) of the Querétaro–Irapuato railway connection, with a total length of 70.7 km.",
        "note": "Opened Mota-Engil PDF market notice 20 Oct 2025.",
    },
    {
        "id": "mota_engil_mexico_qi_t2_20251020",
        "type": "company",
        "chicago": "Mota-Engil S.G.P.S., S.A. “Mota-Engil Informs About the Signing of New Contracts in Mexico Worth Circa of 1,020 Million Euros.” 20 October 2025.",
        "url": "https://www.mota-engil.com/app/uploads/2025/10/Comunicado_20_10_2025_-Mexico_v3JPVvi.pdf",
        "annotation": "Company market notice on Querétaro–Irapuato Tramo II ~EUR 820m. Supports mota_engil_qi_tramo2_820m_2025.",
        "supports": ["mota_engil_qi_tramo2_820m_2025", "hunt_latam_rail_telecom"],
    },
)

# ---------------------------------------------------------------------------
# 5–8, 10, 12, 15–16, 18 — equal-budget misses logged in hunt notes
# (port_ownership, water, building_materials, port_cranes, bridges_roads,
#  solar, balsa, engineering_epc, copper)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 9 energy/wind — Vestas OEM for Statkraft Emma 72 MW (Peru)
# ---------------------------------------------------------------------------
A(
    {
        "id": "vestas_emma_peru_72mw_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Vestas — turbine supply for Statkraft Emma 72 MW (Piura, Peru)",
        "country": "Peru",
        "asset": "13 Aug 2026: Vestas company-news order listing announces 72 MW onshore order with Statkraft Peru for new wind project (Emma). Complements ownership row statkraft_emma_peru_72mw_2026 (no CAPEX on Statkraft page). OEM supply — no turbine contract USD on opened Vestas listing.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-5.2",
        "lon": "-80.6",
        "geo_note": "Piura region / Emma wind (Statkraft geography; approximate — same pin family as ownership row).",
        "evidence": "documented",
        "source_id": "vestas_statkraft_peru_order_20260813",
        "note": "Actor: Vestas (Denmark) — allied OEM; buyer Statkraft Peru. Vestas wind-turbine orders table 13 Aug 2026 (72 MW onshore). Distinct from ownership row.",
    },
    {
        "id": "vestas_emma_peru_72mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "vestas_statkraft_peru_order_20260813",
        "url": "https://www.vestas.com/en/media/company-news?publicationId=f3448f60-1f89-499b-a107-8a71de31fce7",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "13-08-26 — Vestas secures order with Statkraft Peru for new wind project — Onshore 72 MW.",
        "note": "Opened Vestas company-news / wind-turbine orders listing for 13 Aug 2026 Statkraft Peru 72 MW.",
    },
    {
        "id": "vestas_statkraft_peru_order_20260813",
        "type": "company",
        "chicago": "Vestas Wind Systems A/S. “Vestas secures order with Statkraft Peru for new wind project.” Company news / wind turbine orders listing, 13 August 2026.",
        "url": "https://www.vestas.com/en/media/company-news?publicationId=f3448f60-1f89-499b-a107-8a71de31fce7",
        "annotation": "Vestas OEM order listing for Statkraft Peru Emma 72 MW. Supports vestas_emma_peru_72mw_2026.",
        "supports": ["vestas_emma_peru_72mw_2026", "hunt_energy_wind"],
    },
)

# ---------------------------------------------------------------------------
# 11 energy/fission_smr — Argentina hosts FIRST LAC SMR workshop (U.S. program)
# ---------------------------------------------------------------------------
A(
    {
        "id": "argentina_first_smr_workshop_2026",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "us",
        "counterpart": "United States FIRST program — Argentina-hosted LAC SMR regional workshop",
        "country": "Argentina",
        "asset": "June 2026: Argentina (CNEA) co-hosts with U.S. State Department the fourth annual FIRST regional workshop for Latin America and the Caribbean on SMR deployment (Buenos Aires / Atucha tour). Nine regional delegations plus contributing partners US/Argentina/Canada/Japan/UK. Complements argentina_first_smr_2025 (contributing-partner accession) — this row is the 2026 hosted workshop milestone. Program partnership — no CAPEX.",
        "investment_type": "program_partnership",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-33.97",
        "lon": "-59.21",
        "geo_note": "Atucha Nuclear Complex tour cited in workshop coverage (Zárate / Lima party area; approximate).",
        "evidence": "proxy",
        "source_id": "nei_argentina_first_workshop_20260612",
        "note": "Actor: U.S. FIRST (State Department) with Argentina CNEA — us. UNVERIFIED proxy: Nuclear Engineering International 12 Jun 2026 (U.S. Embassy Argentina primary returned forbidden at retrieve). Distinct from argentina_first_smr_2025 accession row and peru_first_bilateral_partner_2026.",
    },
    {
        "id": "argentina_first_smr_workshop_2026",
        "retrieved": "2026-10-01",
        "source_id": "nei_argentina_first_workshop_20260612",
        "url": "https://www.neimagazine.com/news/argentina-hosts-first-smr-workshop/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Argentina has hosted the fourth annual regional workshop for Latin America and the Caribbean for the US Foundational Infrastructure for the Responsible Use of Small Modular Reactor Technology (FIRST) programme. The meeting was co-organised by the National Atomic Energy Commission (CNEA) and the US State Department.",
        "note": "Opened NEI workshop report 12 Jun 2026.",
    },
    {
        "id": "nei_argentina_first_workshop_20260612",
        "type": "trade_press",
        "chicago": "Nuclear Engineering International. “Argentina hosts FIRST SMR workshop.” 12 June 2026.",
        "url": "https://www.neimagazine.com/news/argentina-hosts-first-smr-workshop/",
        "annotation": "Trade press on Argentina-hosted FIRST LAC SMR workshop. Supports argentina_first_smr_workshop_2026.",
        "supports": ["argentina_first_smr_workshop_2026", "hunt_energy_fission_smr"],
    },
)

# ---------------------------------------------------------------------------
# 13 resources/niobium — St George–REAlloys U.S. offtake MoU (Araxá Nb-REE)
# ---------------------------------------------------------------------------
A(
    {
        "id": "st_george_realloys_mou_2025",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "us",
        "counterpart": "REAlloys Inc (Ohio) — MoU for Araxá rare-earth offtake path (Nb-REE project)",
        "country": "Brazil",
        "asset": "10 Sep 2025 ASX: St George Mining signs MoU with U.S. magnet-materials maker REAlloys Inc (Euclid, Ohio; DLA/DOE supply chain) to commercialise rare earths at 100%-owned Araxá niobium-REE project (Minas Gerais, adjacent CBMM). Contemplates potential long-term offtake for up to 40% of Araxá rare-earth production — non-binding until definitive offtake. Later extended to one-year horizon (Jan 2026) for metallurgical work. Coded under niobium taxonomy (Araxá dual Nb-REE asset; Nb is the LatAm scarce-resource subcategory).",
        "investment_type": "offtake",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "Araxá Nb-REE project, Minas Gerais (company ASX geography; same pin family as other St George Araxá rows).",
        "evidence": "documented",
        "source_id": "stgm_realloys_mou_20250910",
        "note": "Actor: REAlloys (U.S.) offtake-path MoU with St George (Australia) on Brazilian Araxá — side=us for U.S. downstream partner. Company ASX release 10 Sep 2025. Non-binding MoU. Distinct from st_george_araxa_capex_brl3bn_2026 / raise rows.",
    },
    {
        "id": "st_george_realloys_mou_2025",
        "retrieved": "2026-10-01",
        "source_id": "stgm_realloys_mou_20250910",
        "url": "https://stgm.com.au/PDF/c711a612-e8ce-4e2d-84f1-bd4c55892c24/USSTRATEGICALLIANCEFORARAXAPROJECTRAREEARTHS",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "St George Mining Limited … has signed a Memorandum of Understanding (“MoU”) with REAlloys Inc (“REAlloys”) to create a strategic alliance for both parties to collaborate on the commercialisation of the rare earths resource at the Company’s 100%-owned advanced, high-grade Araxá niobium-REE Project in Minas Gerais, Brazil … with a view to REAlloys securing a long-term offtake contract for up to 40% of the rare earths production from the Araxá Project.",
        "note": "Opened St George ASX PDF 10 Sep 2025.",
    },
    {
        "id": "stgm_realloys_mou_20250910",
        "type": "company",
        "chicago": "St George Mining Limited. “Strategic Alliance with US Rare Earths Processor and Offtake of Rare Earths from the Araxá Project, Brazil.” ASX release, 10 September 2025.",
        "url": "https://stgm.com.au/PDF/c711a612-e8ce-4e2d-84f1-bd4c55892c24/USSTRATEGICALLIANCEFORARAXAPROJECTRAREEARTHS",
        "annotation": "Company ASX MoU with U.S. REAlloys on Araxá offtake path. Supports st_george_realloys_mou_2025.",
        "supports": ["st_george_realloys_mou_2025", "hunt_fenb_araxa"],
    },
)

# ---------------------------------------------------------------------------
# 14 resources/graphite — South Star Santa Cruz plant restart (Bahia)
# ---------------------------------------------------------------------------
A(
    {
        "id": "south_star_santa_cruz_restart_202604",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "South Star Battery Metals — Santa Cruz graphite plant restart (Bahia)",
        "country": "Brazil",
        "asset": "8 Apr 2026 GlobeNewswire: South Star announces Santa Cruz plant re-started 7 Apr 2026 (~3 months ahead of schedule) after idle period / feed-system upgrades; ramp toward commissioning and ~5,000 tpy concentrate target cited in later ops updates. Presence/ops milestone — no new CAPEX USD on restart release. Distinct from south_star_santa_cruz_graphite_2024 Phase 1 presence and south_star_santa_cruz_po_36t_2026 PO.",
        "investment_type": "brownfield_restart",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-15.65",
        "lon": "-39.65",
        "geo_note": "Santa Cruz graphite plant, southern Bahia (company geography; same pin family as prior South Star rows).",
        "evidence": "documented",
        "source_id": "south_star_restart_20260408",
        "note": "Actor: South Star Battery Metals (Canada) — allied. Company GlobeNewswire 8 Apr 2026. Ops restart presence.",
    },
    {
        "id": "south_star_santa_cruz_restart_202604",
        "retrieved": "2026-10-01",
        "source_id": "south_star_restart_20260408",
        "url": "https://www.globenewswire.com/news-release/2026/04/08/3270297/0/en/South-Star-Announces-Re-Start-of-Santa-Cruz-Plant-Ahead-of-Schedule.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "South Star Battery Metals Corp. … is pleased to announce that the Santa Cruz plant was re-started yesterday, April 7, 2026. … these efforts have placed the re-start nearly three months ahead of schedule.",
        "note": "Opened South Star GlobeNewswire restart release 8 Apr 2026.",
    },
    {
        "id": "south_star_restart_20260408",
        "type": "company",
        "chicago": "South Star Battery Metals Corp. “South Star Announces Re-Start of Santa Cruz Plant Ahead of Schedule.” GlobeNewswire, 8 April 2026.",
        "url": "https://www.globenewswire.com/news-release/2026/04/08/3270297/0/en/South-Star-Announces-Re-Start-of-Santa-Cruz-Plant-Ahead-of-Schedule.html",
        "annotation": "Company restart notice for Santa Cruz graphite plant. Supports south_star_santa_cruz_restart_202604.",
        "supports": ["south_star_santa_cruz_restart_202604", "hunt_res_graphite"],
    },
)

# ---------------------------------------------------------------------------
# 17 energy/power_plants_grid — EXIM Guyana Gas-to-Energy ~USD 527m (U.S.)
#     (Prior icbc_finance-taxonomy row archived; new LatAm energy-layer row.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "exim_guyana_gte_527m_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "U.S. EXIM — Guyana Gas-to-Energy (300 MW CCGT + gas separation)",
        "country": "Guyana",
        "asset": "26 Dec 2024: EXIM Board approves ~USD 527 million financing to Guyana Ministry of Finance for Gas-to-Energy — natural gas separation plant, 300 MW combined-cycle gas turbine, and gas-supply pipeline services near Georgetown. Supports U.S. JV Lindsayca (Texas) / CH4 Systems (Puerto Rico) and ExxonMobil-related services; CTEP competition with PRC cited. Distinct from archived exim_us_guyana_gte_2025 (old icbc_finance interest-rate proxy).",
        "investment_type": "financing",
        "value": "527000000",
        "currency": "USD",
        "value_usd": "527000000",
        "fx_usd": "1",
        "fx_date": "2024-12-26",
        "year": "2025",
        "status": "active",
        "lat": "6.80",
        "lon": "-58.18",
        "geo_note": "Wales / West Bank Demerara Gas-to-Energy plant area near Georgetown (EXIM/project geography; approximate).",
        "evidence": "documented",
        "source_id": "exim_guyana_gte_approval_20241226",
        "note": "Actor: U.S. EXIM — us. Official EXIM Board approval release. Observation year 2025 (authorization/implementation window); approval date Dec 2024. Complements Stabroek/DPI rate proxies on archived finance-lane row.",
    },
    {
        "id": "exim_guyana_gte_527m_2025",
        "retrieved": "2026-10-01",
        "source_id": "exim_guyana_gte_approval_20241226",
        "url": "https://www.exim.gov/news/export-import-bank-united-states-board-directors-approves-more-526-million-for-guyanese-energy",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Today, the Board of Directors at the Export-Import Bank of the United States (EXIM) approved $527 million to the Ministry of Finance of the Cooperative Republic of Guyana to support a gas-to-energy project … The financing from today’s transaction will aid the construction of a natural gas separation plant, a 300 MW combined cycle gas turbine power plant and services related to the gas supply pipeline near Guyana’s capital, Georgetown.",
        "note": "Opened EXIM.gov Board approval release 26 Dec 2024.",
    },
    {
        "id": "exim_guyana_gte_approval_20241226",
        "type": "official",
        "chicago": "Export-Import Bank of the United States. “Export-Import Bank of the United States Board of Directors Approves More Than $526 Million for Guyanese Energy Project.” 26 December 2024.",
        "url": "https://www.exim.gov/news/export-import-bank-united-states-board-directors-approves-more-526-million-for-guyanese-energy",
        "annotation": "Official EXIM ~USD 527m Guyana Gas-to-Energy approval. Supports exim_guyana_gte_527m_2025.",
        "supports": ["exim_guyana_gte_527m_2025", "hunt_br_power_equip"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    if not bib_entry:
        return
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if k == "supports":
                existing["supports"] = sorted(
                    set(existing.get("supports") or []) | set(v or [])
                )
            elif v is not None:
                existing[k] = v
    else:
        bib.append(bib_entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added, updated = [], []

    for rid, patch, evidence, bib_entry in UPDATES:
        if rid not in by_id:
            raise SystemExit(f"missing update target {rid}")
        rows[by_id[rid]].update({k: v for k, v in patch.items() if v is not None})
        updated.append(rid)
        if evidence:
            (EVID / f"{rid}.json").write_text(
                json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
        upsert_bib(bib, bib_by, bib_entry)

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
            updated.append(rid)
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
        "hunt_res_nickel": "Cycle 43: equal budget; U.S. search — DFC PNP / Jervois SMP / Centaurus Jaguar already (miss).",
        "hunt_energy_other_renewables": "Cycle 43: logged aes_andes_solar_iii_hub_2026 (U.S.; hub >USD 1.3bn).",
        "hunt_res_lithium": "Cycle 43: logged exim_argentina_build_future_7bn_2026 (U.S.) + ganfeng_lar_debt_130m_2026 (PRC).",
        "hunt_latam_rail_telecom": "Cycle 43: logged mota_engil_qi_tramo1_290m_2025 + mota_engil_qi_tramo2_820m_2025.",
        "hunt_infra_port_ownership": "Cycle 43: equal budget; APM Lazaro Phase III / Suape / Cosco already (miss).",
        "hunt_res_water": "Cycle 43: equal budget; Sacyr Coquimbo/Antofagasta / Bechtel QB2 already (miss).",
        "hunt_infra_building_materials": "Cycle 43: equal budget; Holcim Colombia/Geocycle already (miss).",
        "hunt_infra_port_cranes": "Cycle 43: equal budget; Konecranes Yucatán / ZPMC / Kalmar already (miss).",
        "hunt_energy_wind": "Cycle 43: logged vestas_emma_peru_72mw_2026 (OEM for Statkraft Emma).",
        "hunt_infra_bridges_roads": "Cycle 43: equal budget; CAF/Mota-Engil Santos–Guarujá / CRBC already (miss).",
        "hunt_energy_fission_smr": "Cycle 43: logged argentina_first_smr_workshop_2026 (U.S. FIRST).",
        "hunt_energy_solar": "Cycle 43: equal budget; Andes Solar III coded other_renewables; Polaris/FinDev already (miss).",
        "hunt_fenb_araxa": "Cycle 43: logged st_george_realloys_mou_2025 (U.S. REAlloys offtake MoU).",
        "hunt_res_graphite": "Cycle 43: logged south_star_santa_cruz_restart_202604.",
        "hunt_res_balsa": "Cycle 43: equal budget; WITS 2025 pair / AIMA Siemens MoU already (miss).",
        "hunt_infra_engineering_epc": "Cycle 43: equal budget; Fluor/Bechtel/CHEC/Ausenco already (miss).",
        "hunt_br_power_equip": "Cycle 43: logged exim_guyana_gte_527m_2025 (U.S. EXIM ~USD 527m).",
        "hunt_res_copper": "Cycle 43: equal budget; Chilean Cobalt EXIM / El Abra / Las Bambas already (miss).",
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
    print("Cycle 43 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 43 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
