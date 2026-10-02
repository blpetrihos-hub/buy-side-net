#!/usr/bin/env python3
"""Cycle 62 hunt: shuffle_seed=20261062; equal budget; U.S. ≥1/3; thin after.

Order: nickel, wind, other_renewables, copper, port_cranes, rail, engineering_epc,
water, niobium, graphite, fission_smr, port_ownership, building_materials, solar,
lithium, bridges_roads, power_plants_grid, balsa.
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
# 7 infrastructure/engineering_epc — Honeywell Ecofining for Acelen Bahia (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "honeywell_acelen_bahia_ecofining_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Honeywell UOP — Ecofining modular process tech for Acelen Renewables Bahia SAF/HVO",
        "country": "Brazil",
        "asset": "17 Jun 2026 Honeywell release: modular UOP Ecofining process technology, pumps, compressors, and Experion PKS integrated control/safety systems selected for Acelen Renewables greenfield SAF and renewable diesel biorefinery in Bahia (São Francisco do Conde). Plant targets ~1 billion liters/y SAF/HVO; macaúba feedstock path; operations targeted ~2029. Distinct from honeywell_petrobras_etj_replan_2026.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-12.627",
        "lon": "-38.680",
        "geo_note": "São Francisco do Conde, Bahia (company/AFRY geography; approximate pin).",
        "evidence": "documented",
        "source_id": "honeywell_acelen_ecofining_20260617",
        "note": "Actor: Honeywell (NASDAQ: HON) — us. Company English release. CapEx USD not disclosed in release.",
    },
    {
        "id": "honeywell_acelen_bahia_ecofining_2026",
        "retrieved": "2026-10-01",
        "source_id": "honeywell_acelen_ecofining_20260617",
        "url": "https://www.honeywell.com/us/en/news/press-releases/2026/06/honeywell-modular-technology-to-power-and-automate-acelen-renewables-biofuel-production",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Honeywell (NASDAQ: HON) today announced that its modular Ecofining™ process technology, specialized pumps, compressors, and integrated control and safety systems will help drive sustainable aviation fuel (SAF) and renewable diesel production for Acelen Renewables' greenfield site in Bahia, Brazil.",
        "note": "Opened Honeywell company release on Acelen Bahia Ecofining award.",
    },
    {
        "id": "honeywell_acelen_ecofining_20260617",
        "type": "company",
        "chicago": "Honeywell. “Honeywell Modular Technology to Power and Automate Acelen Renewables Biofuel Production.” Press release, 17 June 2026.",
        "url": "https://www.honeywell.com/us/en/news/press-releases/2026/06/honeywell-modular-technology-to-power-and-automate-acelen-renewables-biofuel-production",
        "annotation": "Honeywell UOP Ecofining modular tech for Acelen Bahia SAF/HVO. Supports honeywell_acelen_bahia_ecofining_2026.",
        "supports": ["honeywell_acelen_bahia_ecofining_2026", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 8 resources/water — NADBank Water Resiliency Fund USD 400m (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "nadbank_water_resiliency_fund_400m_2025",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "NADBank — Water Resiliency Fund (U.S.–Mexico border)",
        "country": "Mexico",
        "asset": "29 Aug 2025 NADBank Summit’25: Board approves Water Resiliency Fund providing up to US$400m for priority water conservation/diversification infrastructure in the U.S.–Mexico border region — up to US$100m concessional from retained earnings over five years plus US$300m low-interest loan-program capacity (may add market-rate). Distinct from nadbank_baja_rosarito_distrib_82m_2026 (project loan).",
        "investment_type": "financing",
        "value": "400000000",
        "currency": "USD",
        "value_usd": "400000000",
        "fx_usd": "1",
        "fx_date": "2025-08-29",
        "year": "2025",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "Binational U.S.–Mexico border water program (no single named build site in announcement).",
        "evidence": "documented",
        "source_id": "nadbank_wrf_20250829",
        "note": "Actor: North American Development Bank (U.S.–Mexico) — us. Fund ceiling from NADBank press release.",
    },
    {
        "id": "nadbank_water_resiliency_fund_400m_2025",
        "retrieved": "2026-10-01",
        "source_id": "nadbank_wrf_20250829",
        "url": "https://nadbank.org/news/press-release/nadbank-launches-us400-million-water-resiliency-fund-to-support-water-conservation-and-diversification-in-the-u.s.-mexico-border-region",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "the Water Resiliency Fund (WRF), which will provide up to US$400 million in financing for priority infrastructure projects aimed at conserving and diversifying water supply sources in the U.S.-Mexico border region.",
        "note": "Opened NADBank press release on Water Resiliency Fund approval.",
    },
    {
        "id": "nadbank_wrf_20250829",
        "type": "agency",
        "chicago": "North American Development Bank. “NADBank Launches US$400-Million Water Resiliency Fund to Support Water Conservation and Diversification in the U.S.-Mexico Border Region.” Press release, 29 August 2025.",
        "url": "https://nadbank.org/news/press-release/nadbank-launches-us400-million-water-resiliency-fund-to-support-water-conservation-and-diversification-in-the-u.s.-mexico-border-region",
        "annotation": "NADBank USD 400m Water Resiliency Fund. Supports nadbank_water_resiliency_fund_400m_2025.",
        "supports": ["nadbank_water_resiliency_fund_400m_2025", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 14 energy/solar — IDB Invest 360 Energy Argentina USD 50m (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "idb_360_energy_argentina_50m_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "allied",
        "counterpart": "IDB Invest — 360 Energy Solar SA loan (Argentina PV + BESS)",
        "country": "Argentina",
        "asset": "17 Jul 2026 IDB Invest approval: USD 50m loan to 360 Energy Solar SA for CapEx on PSF Arrecifes, PSF Realicó, PSF La Rioja IV, PSF Palomar, and PSF Córdoba, including BESS at Arrecifes and Realicó plus interconnection. Category B; disclosed 7 Apr 2026. Distinct from idb_invest_genneia_95m_2025.",
        "investment_type": "financing",
        "value": "50000000",
        "currency": "USD",
        "value_usd": "50000000",
        "fx_usd": "1",
        "fx_date": "2026-07-17",
        "year": "2026",
        "status": "active",
        "lat": "-34.07",
        "lon": "-60.10",
        "geo_note": "PSF Arrecifes (Buenos Aires Province) — one of five named parks in IDB Invest scope; approximate pin.",
        "evidence": "documented",
        "source_id": "idb_invest_360_energy_20260717",
        "note": "Actor: IDB Invest (IADB Group) — allied. Financing amount from IDB Invest project page.",
    },
    {
        "id": "idb_360_energy_argentina_50m_2026",
        "retrieved": "2026-10-01",
        "source_id": "idb_invest_360_energy_20260717",
        "url": "https://idbinvest.org/en/projects/360-energy-financing-improving-energy-security-argentina",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Financing amount USD $ 50,000,000 … support capital expenditures for the design, construction, operation, and maintenance of new solar renewable energy facilities in Argentina, specifically PSF Arrecifes, PSF Realicó, PSF La Rioja IV, PSF Palomar, and PSF Cordoba.",
        "note": "Opened IDB Invest project page for 360 Energy Argentina.",
    },
    {
        "id": "idb_invest_360_energy_20260717",
        "type": "agency",
        "chicago": "IDB Invest. “360 Energy Financing - Improving Energy Security in Argentina.” Project 15704-01. Approval date 17 July 2026.",
        "url": "https://idbinvest.org/en/projects/360-energy-financing-improving-energy-security-argentina",
        "annotation": "IDB Invest USD 50m loan for 360 Energy Argentina solar/BESS portfolio. Supports idb_360_energy_argentina_50m_2026.",
        "supports": ["idb_360_energy_argentina_50m_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 15 resources/lithium — Ganfeng/Exar Cauchari-Olaroz Stage 2 RIGI (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ganfeng_exar_cauchari_rigi_stage2_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "Ganfeng / Minera Exar — Cauchari-Olaroz Stage 2 RIGI (+45 kt/y LCE)",
        "country": "Argentina",
        "asset": "Resolución ME 825/2026 (Boletín Oficial 5 Jun 2026): approves RIGI adhesion for Minera Exar Sucursal Dedicada “Ampliación Cauchari Olaroz” in Susques, Jujuy — +45,000 t/y LCE capacity on existing ~40,000 t/y Stage 1. Declared computable-asset investment USD 1,166,677,726. Ganfeng 46.7% / Lithium Argentina 44.8% / JEMSE 8.5%. Distinct from ganfeng_mariana / pastos_grandes rows.",
        "investment_type": "ownership_equity",
        "value": "1166677726",
        "currency": "USD",
        "value_usd": "1166677726",
        "fx_usd": "1",
        "fx_date": "2026-06-05",
        "year": "2026",
        "status": "active",
        "lat": "-23.68",
        "lon": "-66.70",
        "geo_note": "Cauchari-Olaroz / Susques Department, Jujuy (RIGI geography; approximate pin).",
        "evidence": "documented",
        "source_id": "boletin_oficial_res_825_2026",
        "note": "Actor: Ganfeng Lithium (largest Exar shareholder, PRC) via Minera Exar — prc. Value = declared RIGI computable assets from Boletín Oficial Resolución 825/2026.",
    },
    {
        "id": "ganfeng_exar_cauchari_rigi_stage2_2026",
        "retrieved": "2026-10-01",
        "source_id": "boletin_oficial_res_825_2026",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/342818/20260605",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "EXARSD declaró que el Proyecto implicará una inversión total en activos computables de mil ciento sesenta y seis millones seiscientos setenta y siete mil setecientos veintiséis dólares estadounidenses (USD 1.166.677.726)",
        "note": "Opened Argentina Boletín Oficial Resolución 825/2026 on Exar Cauchari-Olaroz RIGI.",
    },
    {
        "id": "boletin_oficial_res_825_2026",
        "type": "government",
        "chicago": "Argentina. Ministerio de Economía. “Resolución 825/2026.” Boletín Oficial de la República Argentina, 5 June 2026.",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/342818/20260605",
        "annotation": "RIGI approval for Minera Exar Cauchari-Olaroz Stage 2 (USD 1.166bn computable assets). Supports ganfeng_exar_cauchari_rigi_stage2_2026.",
        "supports": ["ganfeng_exar_cauchari_rigi_stage2_2026", "hunt_res_lithium"],
    },
)

# ---------------------------------------------------------------------------
# 17 energy/power_plants_grid — Shell Manzanillo Block 1 ~420 MW (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "shell_manzanillo_gas_power_block1_dr_2024",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "Shell Gas & Power / HIC / ENERLA — Manzanillo Gas & Power Block 1 CCGT + LNG",
        "country": "Dominican Republic",
        "asset": "MEM Resolución R-MEM-LCG-003-2024 (19 Feb 2024): construction permit for Manzanillo Gas & Power, S.A. (consortium Haina Investment Co., ENERLA, Shell Gas & Power Development B.V.) — ~420 MW net 1×1 CCGT plus LNG import/storage/regasification terminal at Bahía de Manzanillo, Pepillo Salcedo, Monte Cristi; 42-month build; Shell fuel supply. Distinct from lindsayca_manzanillo_block2_dr_2026 / siemens_manzanillo_power_land_414mw_2026.",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "19.70",
        "lon": "-71.74",
        "geo_note": "Bahía de Manzanillo / Pepillo Salcedo, Monte Cristi (MEM geography).",
        "evidence": "documented",
        "source_id": "mem_manzanillo_block1_20240219",
        "note": "Actor: Shell Gas & Power Development B.V. (Netherlands) in MG&P consortium — allied. CapEx USD not stated in MEM resolution.",
    },
    {
        "id": "shell_manzanillo_gas_power_block1_dr_2024",
        "retrieved": "2026-10-01",
        "source_id": "mem_manzanillo_block1_20240219",
        "url": "https://mem.gob.do/transparencia/wp-content/uploads/2018/10/Resolucion-Num.-R-MEM-LCG-003-2024-MANZANILLO-GAS-POWER-SA.pdf",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Central de generación eléctrica de un conjunto compuesto por una turbina de gas en ciclo combinado (\"CCGT\" por sus siglas en ingles), de última generación. Alimentada con gas natural, en arreglo 1 x 1 y con una capacidad neta de 420 MW.",
        "note": "Opened MEM Dominican Republic construction permit PDF for Manzanillo Block 1.",
    },
    {
        "id": "mem_manzanillo_block1_20240219",
        "type": "government",
        "chicago": "Dominican Republic. Ministerio de Energía y Minas. “Resolución Núm. R-MEM-LCG-003-2024 — Manzanillo Gas & Power, S.A.” 19 February 2024.",
        "url": "https://mem.gob.do/transparencia/wp-content/uploads/2018/10/Resolucion-Num.-R-MEM-LCG-003-2024-MANZANILLO-GAS-POWER-SA.pdf",
        "annotation": "MEM permit for Shell/HIC/ENERLA Manzanillo Block 1 ~420 MW CCGT + LNG. Supports shell_manzanillo_gas_power_block1_dr_2024.",
        "supports": ["shell_manzanillo_gas_power_block1_dr_2024", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 17 energy/power_plants_grid — Golar SESA MK II FLNG FID (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "golar_sesa_mkii_flng_argentina_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "Golar LNG — Southern Energy MK II FLNG 3.5 MTPA charter (San Matías Gulf)",
        "country": "Argentina",
        "asset": "6 Aug 2025 Golar release: SESA FID for 20-year charter of Golar 3.5 MTPA MK II FLNG (net charter hire US$400m/y + commodity tariff). Moored in San Matías Gulf near Hilli; startup targeted 2028. Combined Hilli+MKII nameplate 5.95 MTPA. SESA owners: PAE 30%, YPF 25%, Pampa 20%, Harbour Energy 15%, Golar 10%. Distinct from pumpco_bonatti_argentina_lng_epc_2026.",
        "investment_type": "equipment_supply",
        "value": "400000000",
        "currency": "USD",
        "value_usd": "400000000",
        "fx_usd": "1",
        "fx_date": "2025-08-06",
        "year": "2025",
        "status": "active",
        "lat": "-40.80",
        "lon": "-64.90",
        "geo_note": "San Matías Gulf / Río Negro FLNG mooring area (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "golar_sesa_mkii_fid_20250806",
        "note": "Actor: Golar LNG Limited (Bermuda/Norway-listed FLNG) — allied. Value = stated annual net charter hire (not total CapEx).",
    },
    {
        "id": "golar_sesa_mkii_flng_argentina_2025",
        "retrieved": "2026-10-01",
        "source_id": "golar_sesa_mkii_fid_20250806",
        "url": "https://www.globenewswire.com/news-release/2025/08/06/3128725/0/en/Final-Investment-Decision-for-20-year-charter-of-MK-II-FLNG-to-Southern-Energy-in-Argentina.html",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Southern Energy S.A. (“SESA”) has reached Final Investment Decision for the charter of Golar’s 3.5MTPA MK II FLNG … net charter hire to Golar of US$ 400 million per year",
        "note": "Opened Golar GlobeNewswire FID release for SESA MK II FLNG.",
    },
    {
        "id": "golar_sesa_mkii_fid_20250806",
        "type": "company",
        "chicago": "Golar LNG Limited. “Final Investment Decision for 20-Year Charter of MK II FLNG to Southern Energy in Argentina.” GlobeNewswire, 6 August 2025.",
        "url": "https://www.globenewswire.com/news-release/2025/08/06/3128725/0/en/Final-Investment-Decision-for-20-year-charter-of-MK-II-FLNG-to-Southern-Energy-in-Argentina.html",
        "annotation": "Golar SESA MK II FLNG FID (US$400m/y net hire). Supports golar_sesa_mkii_flng_argentina_2025.",
        "supports": ["golar_sesa_mkii_flng_argentina_2025", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 17 energy/power_plants_grid — Cheniere–Petrobras LNG SPA 0.8 mtpa (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cheniere_petrobras_lng_spa_0p8mtpa_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Cheniere Marketing — Petrobras long-term LNG SPA (~0.8 mtpa FOB, 22 years)",
        "country": "Brazil",
        "asset": "29 Sep 2026 Cheniere release: Cheniere Marketing SPA with Petrobras for ~0.8 mtpa LNG on FOB basis for 22 years from Cheniere’s U.S. Gulf liquefaction platform. Distinct from sempra_petrobras_lng_spa_0p8mtpa_2026 / exim_bahamas_lng.",
        "investment_type": "offtake",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "FOB SPA (U.S. Gulf supply to Petrobras); no single named Brazilian receipt terminal in release.",
        "evidence": "documented",
        "source_id": "cheniere_petrobras_spa_20260929",
        "note": "Actor: Cheniere Energy (NYSE: LNG) — us. Volume disclosed; USD contract value not disclosed.",
    },
    {
        "id": "cheniere_petrobras_lng_spa_0p8mtpa_2026",
        "retrieved": "2026-10-01",
        "source_id": "cheniere_petrobras_spa_20260929",
        "url": "https://lngir.cheniere.com/news-events/press-releases/detail/346/cheniere-and-petrobras-sign-long-term-lng-sale-and-purchase",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Petrobras has agreed to purchase approximately 0.8 million tonnes per annum (“mtpa”) of LNG from Cheniere Marketing on a free-on-board (FOB) basis for 22 years.",
        "note": "Opened Cheniere IR release on Petrobras LNG SPA.",
    },
    {
        "id": "cheniere_petrobras_spa_20260929",
        "type": "company",
        "chicago": "Cheniere Energy, Inc. “Cheniere and Petrobras Sign Long-Term LNG Sale and Purchase Agreement.” Press release, 29 September 2026.",
        "url": "https://lngir.cheniere.com/news-events/press-releases/detail/346/cheniere-and-petrobras-sign-long-term-lng-sale-and-purchase",
        "annotation": "Cheniere–Petrobras ~0.8 mtpa / 22-year FOB LNG SPA. Supports cheniere_petrobras_lng_spa_0p8mtpa_2026.",
        "supports": ["cheniere_petrobras_lng_spa_0p8mtpa_2026", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 17 energy/power_plants_grid — Sempra–Petrobras LNG SPA 0.8 Mtpa (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sempra_petrobras_lng_spa_0p8mtpa_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Sempra Infrastructure — Petrobras 20-year LNG SPA (~0.8 Mtpa from Port Arthur LNG Phase 2)",
        "country": "Brazil",
        "asset": "14 Sep 2026 Sempra Infrastructure release: 20-year SPA with Petrobras for ~0.8 Mtpa LNG sourced from contracted Port Arthur LNG Phase 2 capacity (Jefferson County, Texas). Distinct from cheniere_petrobras_lng_spa_0p8mtpa_2026.",
        "investment_type": "offtake",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "FOB SPA (Port Arthur LNG Phase 2 supply to Petrobras); no single named Brazilian receipt terminal in release.",
        "evidence": "documented",
        "source_id": "sempra_petrobras_spa_20260914",
        "note": "Actor: Sempra Infrastructure (Sempra, NYSE: SRE) — us. Volume disclosed; USD contract value not disclosed.",
    },
    {
        "id": "sempra_petrobras_lng_spa_0p8mtpa_2026",
        "retrieved": "2026-10-01",
        "source_id": "sempra_petrobras_spa_20260914",
        "url": "https://www.prnewswire.com/news-releases/sempra-infrastructure-announces-long-term-lng-supply-agreement-with-petrobras-302878157.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Sempra Infrastructure … announced a 20-year sales and purchase agreement (SPA) with Petrobras, under which Sempra Infrastructure will supply approximately 0.8 million tonnes per annum (Mtpa) of liquefied natural gas (LNG).",
        "note": "Opened Sempra Infrastructure / PR Newswire release on Petrobras LNG SPA.",
    },
    {
        "id": "sempra_petrobras_spa_20260914",
        "type": "company",
        "chicago": "Sempra Infrastructure. “Sempra Infrastructure Announces Long-Term LNG Supply Agreement with Petrobras.” PR Newswire, 14 September 2026.",
        "url": "https://www.prnewswire.com/news-releases/sempra-infrastructure-announces-long-term-lng-supply-agreement-with-petrobras-302878157.html",
        "annotation": "Sempra–Petrobras ~0.8 Mtpa / 20-year LNG SPA from Port Arthur LNG Phase 2. Supports sempra_petrobras_lng_spa_0p8mtpa_2026.",
        "supports": ["sempra_petrobras_lng_spa_0p8mtpa_2026", "hunt_br_power_equip"],
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
        "hunt_res_nickel": "Cycle 62: equal budget; Jervois SMP / Westwin / DFC Piauí / MMG Anglo already (miss).",
        "hunt_energy_wind": "Cycle 62: equal budget; Vestas / Goldwind Sento Sé / Envision Casa already (miss).",
        "hunt_energy_other_renewables": "Cycle 62: equal budget; ClearPower Tinajones / ContourGlobal already (miss).",
        "hunt_res_copper": "Cycle 62: equal budget; Chinalco Los Calatos / CMOC Cangrejos already (miss).",
        "hunt_infra_port_cranes": "Cycle 62: equal budget; Liebherr Compas / SSA Manzanillo STS already (miss).",
        "hunt_latam_rail_telecom": "Cycle 62: equal budget; EXIM Wabtec GMXT / PowerChina Chancay already (miss).",
        "hunt_infra_engineering_epc": "Cycle 62: logged honeywell_acelen_bahia_ecofining_2026 (U.S.).",
        "hunt_res_water": "Cycle 62: logged nadbank_water_resiliency_fund_400m_2025 (U.S.).",
        "hunt_fenb_araxa": "Cycle 62: equal budget; St George / CBMM / CMOC / Boston Metal already (miss).",
        "hunt_res_graphite": "Cycle 62: equal budget; Atlas Malacacheta / Graphcoa already (miss).",
        "hunt_energy_fission_smr": "Cycle 62: equal budget; Peru FIRST / USTDA LAC nuclear / Meitner already (miss).",
        "hunt_infra_port_ownership": "Cycle 62: equal budget; SSA / EXIM Berbice / COSCO Chancay already (miss).",
        "hunt_infra_building_materials": "Cycle 62: equal budget; Holcim / Sinoma already (miss).",
        "hunt_energy_solar": "Cycle 62: logged idb_360_energy_argentina_50m_2026 (allied).",
        "hunt_res_lithium": "Cycle 62: logged ganfeng_exar_cauchari_rigi_stage2_2026 (PRC).",
        "hunt_infra_bridges_roads": "Cycle 62: equal budget; USACE Guatemala / ICA CA-9 already (miss).",
        "hunt_br_power_equip": "Cycle 62: logged shell_manzanillo_gas_power_block1_dr_2024 (allied) + golar_sesa_mkii_flng_argentina_2025 (allied) + cheniere_petrobras_lng_spa_0p8mtpa_2026 (U.S.) + sempra_petrobras_lng_spa_0p8mtpa_2026 (U.S.).",
        "hunt_res_balsa": "Cycle 62: equal budget; AIMA / Plantabal / CoreLite already (miss).",
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
    print("Cycle 62 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
