#!/usr/bin/env python3
"""Cycle 25 hunt: shuffle_seed=20261025; equal budget across 18 subcategories."""
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


# seed 20261025 order:
# solar, rail, building_materials, port_ownership, copper, other_renewables,
# power_plants_grid, engineering_epc, niobium, port_cranes, wind, nickel,
# balsa, graphite, bridges_roads, lithium, water, fission_smr

# 1 energy/solar — Hanersun / Solfácil 400 MW N-type module supply (Brazil)
A(
    {
        "id": "hanersun_solfacil_400mw_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Hanersun — 400 MW N-type module supply agreement with Solfácil (Brazil)",
        "country": "Brazil",
        "asset": "New 400 MW supply agreement for HITOUCH 5N N-type modules signed at SNEC 2025 with Brazilian distributor/financier Solfácil; targets residential and C&I distributed solar; continues partnership begun 2022",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-23.55",
        "lon": "-46.63",
        "geo_note": "Brazil distributed-solar portfolio pin (Solfácil HQ São Paulo metro; project sites unnamed on Hanersun release).",
        "evidence": "documented",
        "source_id": "hanersun_solfacil_400mw_20250612",
        "note": "Actor: Hanersun (PRC) — prc; buyer Solfácil (Brazilian). Company English news 12 Jun 2025. No contract USD on opened page. Distinct from jinko_casa_ventos_413mwp_2026 utility supply.",
    },
    {
        "id": "hanersun_solfacil_400mw_2025",
        "retrieved": "2026-10-01",
        "source_id": "hanersun_solfacil_400mw_20250612",
        "url": "https://www.hanersun.com/hanersun-and-solfacil-renew-400mw-n-type-module-supply-agreement-at-snec-2025/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Hanersun and Solfácil signed a new 400MW supply agreement for high-efficiency solar modules at SNEC 2025. … Under the agreement, Hanersun will continue to supply its flagship HITOUCH 5N series modules.",
        "note": "Opened Hanersun company English news 12–13 Jun 2025.",
    },
    {
        "id": "hanersun_solfacil_400mw_20250612",
        "type": "company",
        "chicago": "Hanersun. “Hanersun and Solfácil Renew 400MW N-Type Module Supply Agreement at SNEC 2025.” 12 June 2025.",
        "url": "https://www.hanersun.com/hanersun-and-solfacil-renew-400mw-n-type-module-supply-agreement-at-snec-2025/",
        "annotation": "Company primary on Hanersun–Solfácil 400 MW Brazil module supply. Supports hanersun_solfacil_400mw_2025.",
        "supports": ["hanersun_solfacil_400mw_2025", "hunt_energy_solar"],
    },
)

# 2 infrastructure/rail — CAF Trivia Trens €500m 24-year maintenance (São Paulo)
A(
    {
        "id": "caf_trivia_sp_maint_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "CAF — comprehensive maintenance of 107 EMUs for Trivia Trens (São Paulo Lines 11/12/13)",
        "country": "Brazil",
        "asset": "24-year comprehensive maintenance contract with Trivia Trens S.A. (Comporte) for 107 electric trains on Lines 11-Coral, 12-Safira, 13-Jade; LeadMind digital platform; services start with assisted commercial ops July 2026; ~EUR 500 million",
        "investment_type": "services_contract",
        "value": "500000000",
        "currency": "EUR",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-23.55",
        "lon": "-46.63",
        "geo_note": "São Paulo metropolitan train Lines 11/12/13 / Alto Tietê Lot (CAF release).",
        "evidence": "documented",
        "source_id": "caf_trivia_maint_20251120",
        "note": "Actor: CAF / Construcciones y Auxiliar de Ferrocarriles (Spanish) — allied; customer Trivia Trens (Brazilian Comporte). Company press 20 Nov 2025. Value stored as EUR 500m (no FX). Distinct from hitachi_trivia_sp_metro_power_2026 (power supply) and caf_medellin_santiago_metro_2024.",
    },
    {
        "id": "caf_trivia_sp_maint_2025",
        "retrieved": "2026-10-01",
        "source_id": "caf_trivia_maint_20251120",
        "url": "https://www.cafmobility.com/en/press-room/caf-awarded-maintenance-of-rains-operating-on-s%C3%A3o-paulo-commuter-lines/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "CAF has signed a contract with Trivia Trens S.A. … for the comprehensive maintenance of 107 electric trains. … The 24-year contract is valued at approximately EUR500 million",
        "note": "Opened CAF company English press 20 Nov 2025.",
    },
    {
        "id": "caf_trivia_maint_20251120",
        "type": "company",
        "chicago": "CAF. “CAF awarded comprehensive maintenance of trains operating on São Paulo commuter lines 11, 12, and 13.” 20 November 2025.",
        "url": "https://www.cafmobility.com/en/press-room/caf-awarded-maintenance-of-rains-operating-on-s%C3%A3o-paulo-commuter-lines/",
        "annotation": "Company primary on CAF €500m Trivia Trens SP maintenance. Supports caf_trivia_sp_maint_2025.",
        "supports": ["caf_trivia_sp_maint_2025", "hunt_latam_rail_telecom"],
    },
)

# 3 infrastructure/building_materials — Votorantim Xambioá grinding line R$260m
A(
    {
        "id": "votorantim_xambioa_grind_2026",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "other",
        "counterpart": "Votorantim Cimentos — new grinding line at Xambioá cement plant (Tocantins)",
        "country": "Brazil",
        "asset": "R$260 million investment announced July 2026 for new cement grinding line at Xambioá (TO); +500,000 tpy capacity → site total 1.5 Mtpy from July 2028; part of R$5bn Brazil 2024–28 plan alongside kiln modernization / lower-CO2 cement",
        "investment_type": "capex_expansion",
        "value": "260000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-6.41",
        "lon": "-48.36",
        "geo_note": "Xambioá cement plant, Tocantins (Votorantim Cimentos 2Q26 results).",
        "evidence": "documented",
        "source_id": "votorantim_2q26_xambioa_20260813",
        "note": "Actor: Votorantim Cimentos (Brazilian) — other (host-country industrial). Company English 2Q26 results 13 Aug 2026. Value stored as BRL (no FX). Distinct from sinoma_votorantim_z02_br_2024 (Sinoma EPC at Edealina) and Holcim Pacasmayo / Heidelberg Inka acquisitions.",
    },
    {
        "id": "votorantim_xambioa_grind_2026",
        "retrieved": "2026-10-01",
        "source_id": "votorantim_2q26_xambioa_20260813",
        "url": "https://www.votorantimcimentos.com/news/our-financial-results-in-the-second-quarter-of-2026/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "In July, we announced an investment of R$260 million for the construction of a new grinding line at the Xambioá plant, which will add 500,000 tonnes to the site’s current production capacity, bringing the total to 1.5 million tonnes/year starting in July 2028.",
        "note": "Opened Votorantim Cimentos English 2Q26 results page 13 Aug 2026.",
    },
    {
        "id": "votorantim_2q26_xambioa_20260813",
        "type": "company",
        "chicago": "Votorantim Cimentos. “Our Financial Results in the Second Quarter of 2026.” 13 August 2026.",
        "url": "https://www.votorantimcimentos.com/news/our-financial-results-in-the-second-quarter-of-2026/",
        "annotation": "Company primary on R$260m Xambioá grinding expansion. Supports votorantim_xambioa_grind_2026.",
        "supports": ["votorantim_xambioa_grind_2026", "hunt_infra_building_materials"],
    },
)

# 4 infrastructure/port_ownership — miss (ICTSI Aratu / Rio Brasil / OPC already logged)
# 5 resources/copper — miss (Chinalco Toromocho ITS-3 logged C23; Los Calatos / NFC Raura press-only)

# 6 energy/other_renewables — Trina Storage / Atlas Copiapó 233 MW / 932 MWh GFM BESS
A(
    {
        "id": "trina_atlas_copiapo_bess_2025",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "Trina Storage — Elementa 2 grid-forming BESS for Atlas Copiapó PV+BESS (Chile)",
        "country": "Chile",
        "asset": "233 MW / 932 MWh grid-forming (GFM) BESS at Copiapó PV+BESS complex (Atacama) with Atlas Renewable Energy; Elementa 2 LFP platform; Trina scope from cell manufacturing through commissioning and long-term service; Atlas cites USD 475m financing for the solar-plus-storage complex (Trina OEM/supply — contract USD not restated on Trina page)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-27.37",
        "lon": "-70.33",
        "geo_note": "Copiapó / Atacama Region, Chile (Trina Storage release).",
        "evidence": "documented",
        "source_id": "trina_atlas_copiapo_20251028",
        "note": "Actor: Trina Storage / Trinasolar (PRC) — prc; developer Atlas Renewable Energy. Company English newsroom 28 Oct 2025. No Trina contract USD on opened page (Atlas USD 475m financing is for the complex, not dual-entered as Trina value). Distinct from catl_cip_alegria_bess_2026 and tesla_colbun_celda_solar_2024.",
    },
    {
        "id": "trina_atlas_copiapo_bess_2025",
        "retrieved": "2026-10-01",
        "source_id": "trina_atlas_copiapo_20251028",
        "url": "https://www.trinasolar.com/en-glb/newsroom202510281044/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Trina Storage and Atlas Renewable Energy have joined forces to deliver … the Copiapó PV + BESS Project, a 233 MW / 932 MWh grid-forming (GFM) facility located in Chile's Atacama Region.",
        "note": "Opened Trina Storage / Trinasolar English newsroom 28 Oct 2025.",
    },
    {
        "id": "trina_atlas_copiapo_20251028",
        "type": "company",
        "chicago": "Trina Storage / Trinasolar. “Trina Storage and Atlas Secures Gigawatt-Hour Scale Project in Latin America, Pioneering Grid-Forming Solutions.” 28 October 2025.",
        "url": "https://www.trinasolar.com/en-glb/newsroom202510281044/",
        "annotation": "Company primary on Trina Storage Elementa 2 Copiapó GFM BESS. Supports trina_atlas_copiapo_bess_2025.",
        "supports": ["trina_atlas_copiapo_bess_2025", "hunt_energy_other_renewables"],
    },
)

# 7 energy/power_plants_grid — miss (thick)
# 8 infrastructure/engineering_epc — miss (STRACON / Worley / Bechtel EIMISA already logged)

# 9 resources/niobium — Taboca / CNMC Pitinga USD 100m expansion (press UNVERIFIED)
A(
    {
        "id": "taboca_cnmc_pitinga_100m_2026",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "prc",
        "counterpart": "Mineração Taboca (CNMC) — USD 100m Pitinga mine/metallurgy expansion through 2028",
        "country": "Brazil",
        "asset": "Announced USD 100 million investment cycle through 2028 to double Pitinga mine/processing/metallurgy capacity: USD 25m mineral research; >USD 20m beneficiation modernization; USD 43m smelter upgrades (Nb/Ta smelting +10 ktpy at Pitinga; tin to 8 ktpy at Pirapora); first large CAPEX under China Nonferrous Trade Co. Ltd. control",
        "investment_type": "capex_expansion",
        "value": "100000000",
        "currency": "USD",
        "value_usd": "100000000",
        "fx_usd": "1",
        "fx_date": "2026-01-28",
        "year": "2026",
        "status": "active",
        "lat": "-0.79",
        "lon": "-60.07",
        "geo_note": "Mina Pitinga, Presidente Figueiredo, Amazonas (G1 / company location context; approximate).",
        "evidence": "proxy",
        "source_id": "g1_taboca_100m_20260128",
        "note": "Actor: Mineração Taboca under China Nonferrous Trade Co. Ltd. / CNMC (PRC) — prc. UNVERIFIED proxy: G1 Amazônia 28 Jan 2026 reporting company announcement (Taboca site did not restate USD 100m figure on opened pages). Complements CBMM Araxá / CMOC Catalão niobium rows; distinct tin/Nb-Ta polymetallic asset.",
    },
    {
        "id": "taboca_cnmc_pitinga_100m_2026",
        "retrieved": "2026-10-01",
        "source_id": "g1_taboca_100m_20260128",
        "url": "https://g1.globo.com/am/amazonas/noticia/2026/01/28/mineracao-taboca-anuncia-investimento-de-us-100-mi-para-dobrar-producao-no-am.ghtml",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "A Mineração Taboca anunciou … que vai investir US$ 100 milhões até 2028 para dobrar a capacidade de produção em mineração e metalurgia da Mina de Pitinga, no Amazonas. É o primeiro grande aporte desde que a companhia passou a ser administrada pela China Nonferrous Trade Co. Ltd. … Em Pitinga, a fundição de tântalo e nióbio terá capacidade ampliada em 10 mil toneladas por ano.",
        "note": "Opened G1 Amazônia 28 Jan 2026. UNVERIFIED press proxy of Taboca announcement.",
    },
    {
        "id": "g1_taboca_100m_20260128",
        "type": "press",
        "chicago": "g1 Amazônia. “Mineração Taboca investe US$ 100 mi para dobrar produção no AM.” 28 January 2026.",
        "url": "https://g1.globo.com/am/amazonas/noticia/2026/01/28/mineracao-taboca-anuncia-investimento-de-us-100-mi-para-dobrar-producao-no-am.ghtml",
        "annotation": "Press UNVERIFIED proxy on Taboca/CNMC USD 100m Pitinga expansion. Supports taboca_cnmc_pitinga_100m_2026.",
        "supports": ["taboca_cnmc_pitinga_100m_2026", "hunt_fenb_araxa"],
    },
)

# 10 infrastructure/port_cranes — miss (Kalmar Portonave / ZPMC Multirio / Santos Brasil already logged)
# 11 energy/wind — miss (thick OEM set)
# 12 resources/nickel — miss (MMG Anglo / BNDES Piauí / Centaurus already logged)
# 13 resources/balsa — miss (WITS years; no new named processing stake with openable primary)
# 14 resources/graphite — miss (South Star / Graphcoa set already logged)

# 15 infrastructure/bridges_roads — OHLA BR-040 concession ~€850m
A(
    {
        "id": "ohla_br040_concession_2025",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "allied",
        "counterpart": "OHLA consortium — BR-040 highway concession (RJ–MG, 218.9 km)",
        "country": "Brazil",
        "asset": "30-year concession (ANTT) with Construcap + Copasa to rehabilitate/expand/operate/maintain 218.9 km BR-040 (Rio de Janeiro–Minas Gerais): duplication 13 km, +87 km additional lanes, 3 tunnels, 13 viaducts, Serra de Petrópolis ascent; estimated investment ~EUR 850 million; ops start 2H 2025",
        "investment_type": "concession",
        "value": "850000000",
        "currency": "EUR",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-22.51",
        "lon": "-43.18",
        "geo_note": "BR-040 Serra de Petrópolis ascent / RJ–MG corridor (OHLA release; approximate).",
        "evidence": "documented",
        "source_id": "ohla_br040_20250505",
        "note": "Actors: OHLA (Spanish) lead with Construcap (Brazilian) and Copasa (Spanish) — allied. Company English release 5 May 2025. Value stored as EUR 850m (no FX). Distinct from CHEC Mar 2 / CRBC Arequipa / CCECC Salvador–Itaparica / Panamericana Oeste rows.",
    },
    {
        "id": "ohla_br040_concession_2025",
        "retrieved": "2026-10-01",
        "source_id": "ohla_br040_20250505",
        "url": "https://www.ohla-group.com/en/ohla-wins-1-billion-highway-concession-contract-in-brazil-for-br-040/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "OHLA, in consortium with Brazilian firm Construcap and Spanish company Copasa, has been awarded the concession contract to rehabilitate, expand, operate, and maintain a 218.9 km section of the BR-040 highway … The 30-year concession involves an estimated investment of approximately €850 million.",
        "note": "Opened OHLA company English news 5 May 2025.",
    },
    {
        "id": "ohla_br040_20250505",
        "type": "company",
        "chicago": "OHLA. “OHLA Wins $1 Billion Highway Concession Contract in Brazil for BR-040.” 5 May 2025.",
        "url": "https://www.ohla-group.com/en/ohla-wins-1-billion-highway-concession-contract-in-brazil-for-br-040/",
        "annotation": "Company primary on OHLA BR-040 ~€850m concession. Supports ohla_br040_concession_2025.",
        "supports": ["ohla_br040_concession_2025", "hunt_infra_bridges_roads"],
    },
)

# 16 resources/lithium — China Union Holdings / Lithium Chile Arizaro USD 175m
A(
    {
        "id": "cuh_arizaro_argentum_175m_2025",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "China Union Holdings — definitive SPA to acquire Argentum Lithium / Arizaro project interest",
        "country": "Argentina",
        "asset": "Definitive share purchase agreement to acquire 100% of Lithium Chile’s Argentum Lithium S.A. (indirect Arizaro salar interest, Salta) for USD 175 million cash (92.5% at close / 7.5% escrow 18 months) + USD 5m guarantee deposit; closing subject to ARLI stake step-up to 80%, regulatory approvals (incl. PRC/Canada/Argentina), TSXV acceptance; subsequent ICA formal review noted in 2026 updates",
        "investment_type": "ownership_equity",
        "value": "175000000",
        "currency": "USD",
        "value_usd": "175000000",
        "fx_usd": "1",
        "fx_date": "2025-12-22",
        "year": "2025",
        "status": "active",
        "lat": "-24.75",
        "lon": "-67.4",
        "geo_note": "Salar de Arizaro, Salta Province, Argentina (Lithium Chile Definitive Agreement release).",
        "evidence": "documented",
        "source_id": "lithium_chile_arizaro_spa_20251222",
        "note": "Actor: China Union Holdings Ltd. (PRC-linked purchaser; PRC outbound approvals contemplated) — prc; seller Lithium Chile Inc. (Canadian). Company PDF Definitive Agreement announcement 22 Dec 2025. Distinct from ganfeng_laac_convertible_180m_2026 / Zijin Tres Quebradas / Eni Black Giant. Closing not assured (ICA review / conditions).",
    },
    {
        "id": "cuh_arizaro_argentum_175m_2025",
        "retrieved": "2026-10-01",
        "source_id": "lithium_chile_arizaro_spa_20251222",
        "url": "https://lithiumchile.ca/wp-content/uploads/2025/12/December-22-2025-LITHIUM-CHILE-EXECUTES-DEFINITIVE-AGREEMENT.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "the Company has entered into a definitive share purchase agreement … with China Union Holdings Ltd. … for the sale … of its Argentine subsidiary, Argentum Lithium S.A. … The purchase price is USD $175,000,000, subject to customary closing adjustments and payable in cash at closing",
        "note": "Opened Lithium Chile company PDF Definitive Agreement release 22 Dec 2025.",
    },
    {
        "id": "lithium_chile_arizaro_spa_20251222",
        "type": "company",
        "chicago": "Lithium Chile Inc. “Lithium Chile Executes the Formal Agreement for the Sale of Its Argentine, Arizaro Project.” 22 December 2025.",
        "url": "https://lithiumchile.ca/wp-content/uploads/2025/12/December-22-2025-LITHIUM-CHILE-EXECUTES-DEFINITIVE-AGREEMENT.pdf",
        "annotation": "Company primary on China Union Holdings USD 175m Arizaro/Argentum SPA. Supports cuh_arizaro_argentum_175m_2025.",
        "supports": ["cuh_arizaro_argentum_175m_2025", "hunt_res_lithium"],
    },
)

# 17 resources/water — miss (Techint Collahuasi impulse logged C24; Acciona/IDE/Sacyr set)
# 18 energy/fission_smr — miss (CNEN–INVAP RMB / Candu PIAP / Meitner ACR-300 already logged)


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
        "hunt_energy_solar": "Cycle 25: logged hanersun_solfacil_400mw_2025.",
        "hunt_latam_rail_telecom": "Cycle 25: logged caf_trivia_sp_maint_2025.",
        "hunt_infra_building_materials": "Cycle 25: logged votorantim_xambioa_grind_2026.",
        "hunt_infra_port_ownership": "Cycle 25: equal budget; ICTSI Aratu / Rio Brasil / OPC already logged (miss).",
        "hunt_res_copper": "Cycle 25: equal budget; Chinalco Toromocho ITS-3 logged C23; Los Calatos / NFC Raura press-only (miss).",
        "hunt_energy_other_renewables": "Cycle 25: logged trina_atlas_copiapo_bess_2025.",
        "hunt_br_power_equip": "Cycle 25: equal budget; State Grid NE UHV / thick grid set (miss).",
        "hunt_infra_engineering_epc": "Cycle 25: equal budget; STRACON / Worley / Bechtel EIMISA already logged (miss).",
        "hunt_fenb_araxa": "Cycle 25: logged taboca_cnmc_pitinga_100m_2026 (UNVERIFIED proxy).",
        "hunt_infra_port_cranes": "Cycle 25: equal budget; Kalmar Portonave / ZPMC Multirio / Santos Brasil already logged (miss).",
        "hunt_energy_wind": "Cycle 25: equal budget; Vestas/Goldwind/Nordex/Envision OEM set already logged (miss).",
        "hunt_res_nickel": "Cycle 25: equal budget; MMG Anglo / BNDES Piauí / Centaurus already logged (miss).",
        "hunt_res_balsa": "Cycle 25: equal budget; no new named exporter/processor stake beyond WITS years (miss).",
        "hunt_res_graphite": "Cycle 25: equal budget; South Star / Graphcoa set already logged (miss).",
        "hunt_infra_bridges_roads": "Cycle 25: logged ohla_br040_concession_2025.",
        "hunt_res_lithium": "Cycle 25: logged cuh_arizaro_argentum_175m_2025.",
        "hunt_res_water": "Cycle 25: equal budget; Techint Collahuasi impulse logged C24 (miss).",
        "hunt_energy_fission_smr": "Cycle 25: equal budget; CNEN–INVAP RMB / Candu PIAP / Meitner ACR-300 already logged (miss).",
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
    print("Cycle 25 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
