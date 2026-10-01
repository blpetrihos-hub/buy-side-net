#!/usr/bin/env python3
"""Cycle 23 hunt: shuffle_seed=20261023; equal budget across 18 subcategories."""
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


# seed 20261023 order (canonical BRIEF list):
# balsa, graphite, building_materials, rail, lithium, water, solar, port_cranes,
# wind, port_ownership, fission_smr, nickel, bridges_roads, engineering_epc,
# power_plants_grid, niobium, other_renewables, copper

# 1 resources/balsa — miss (no new named exporter/importer beyond WITS)
# 2 resources/graphite — miss (Graphcoa/South Star/Nacional/Urbix already logged)
# 3 infrastructure/building_materials — miss (CSN Cimentos still not closed)
# 4 infrastructure/rail — miss (Alstom Line 7 first-train is delivery milestone of logged contract)
# 5 resources/lithium — miss (Rincon financing / Eramet RIGI already logged)
# 6 resources/water — miss (Veolia Aguas Pacífico logged C21)

# 7 energy/solar — JinkoSolar 413.9 MWp Tiger Neo 3.0 to Casa dos Ventos
A(
    {
        "id": "jinko_casa_ventos_413mwp_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "JinkoSolar — 413.9 MWp Tiger Neo 3.0 module supply to Casa dos Ventos (Brazil)",
        "country": "Brazil",
        "asset": "Supply agreement for 413.9 MWp of Tiger Neo 3.0 N-type TOPCon modules for Casa dos Ventos utility-scale renewable projects (project name not disclosed on company page)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.55",
        "lon": "-46.63",
        "geo_note": "Brazil utility-scale portfolio pin (project site unnamed on JinkoSolar release; São Paulo metro approximate for developer HQ / national award).",
        "evidence": "documented",
        "source_id": "jinkosolar_casa_ventos_20260414",
        "note": "Actor: JinkoSolar (PRC) — prc; buyer Casa dos Ventos (Brazilian). Company English news 14 Apr 2026. No contract USD on opened page. Distinct from jinko_brazil_module_imports_2023 (national import aggregate) and Vestas/Envision/Goldwind Casa dos Ventos wind OEM rows.",
    },
    {
        "id": "jinko_casa_ventos_413mwp_2026",
        "retrieved": "2026-10-01",
        "source_id": "jinkosolar_casa_ventos_20260414",
        "url": "https://www.jinkosolar.com/en/site/newsdetail/2879",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "JinkoSolar … recently has signed an agreement with Casa dos Ventos … for the supply of 413.9 MWp of Tiger Neo 3.0 modules.",
        "note": "Opened JinkoSolar English company newsdetail 2879 (dated 2026-04-14).",
    },
    {
        "id": "jinkosolar_casa_ventos_20260414",
        "type": "company",
        "chicago": "JinkoSolar. “Casa dos Ventos and JinkoSolar Sign Agreement for the Supply of 413.9 MWp of High-Efficiency Solar Modules.” 14 April 2026.",
        "url": "https://www.jinkosolar.com/en/site/newsdetail/2879",
        "annotation": "Company primary on 413.9 MWp Tiger Neo 3.0 supply to Casa dos Ventos. Supports jinko_casa_ventos_413mwp_2026.",
        "supports": ["jinko_casa_ventos_413mwp_2026", "hunt_energy_solar"],
    },
)

# 8 infrastructure/port_cranes — miss (Tecon Santos / Suape / Cartagena already logged)
# 9 energy/wind — miss (Statkraft Emma / Vestas Esquina / Goldwind Sento Sé already logged)

# 10 infrastructure/port_ownership — ICTSI Americas SPA for CS Porto Aratu (ATU12/ATU18)
A(
    {
        "id": "ictsi_aratu_hsim_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "other",
        "counterpart": "ICTSI Americas B.V. — binding SPA for 100% of HSIM / CS Porto Aratu (ATU12 + ATU18)",
        "country": "Brazil",
        "asset": "Binding purchase of 100% HSIM (ATU12 + ATU18 agricultural bulk terminals at Port of Aratu, Bahia); Enterprise Value R$1.8 billion (Equity Value R$750m = R$650m at closing + R$100m earn-out within 18 months; net debt R$1.0bn at 1Q26); subject to CADE + grantor approvals; potential throughput ~9.5 Mtpy after Simpar modernization",
        "investment_type": "ownership_equity",
        "value": "1800000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-12.78",
        "lon": "-38.5",
        "geo_note": "Port of Aratu / Candeias, Bahia (Simpar Material Fact; ATU12/ATU18).",
        "evidence": "documented",
        "source_id": "simpar_fr_aratu_ictsi_20260723",
        "note": "Actor: ICTSI Americas B.V. (Philippine ICTSI) — other (same coding as ictsi_rio_brasil / ictsi_opc_cortes). Seller SIMPAR / CS Brasil Holding. Official CVM Material Fact 23 Jul 2026. Closing conditional. Value stored as BRL EV (no FX). Distinct from ICTSI Rio Brasil expansion and OPC Cortés rows.",
    },
    {
        "id": "ictsi_aratu_hsim_2026",
        "retrieved": "2026-10-01",
        "source_id": "simpar_fr_aratu_ictsi_20260723",
        "url": "https://www.rad.cvm.gov.br/ENETWeb/frmDownloadDocumento.aspx?CodigoInstituicao=1&Tela=ext&descTipo=IPE&numProtocolo=1547175",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "on July 23, 2026, the Company and CS Brasil Holding … entered into a binding purchase and sale agreement with ICTSI AMERICAS B.V. for the sale of 100% of the stake in HSIM … which wholly owns ATU12 … and ATU18 … (together, “CS Porto Aratu”), for an Enterprise Value of R$ 1.8 billion",
        "note": "Opened SIMPAR CVM Material Fact / Fato Relevante PDF via ENET (protocol 1547175).",
    },
    {
        "id": "simpar_fr_aratu_ictsi_20260723",
        "type": "company",
        "chicago": "SIMPAR S.A. “Fato Relevante — Alienação da CS Porto Aratu (HSIM / ATU12–ATU18) to ICTSI Americas B.V.” Comissão de Valores Mobiliários (CVM) Material Fact, 23 July 2026.",
        "url": "https://www.rad.cvm.gov.br/ENETWeb/frmDownloadDocumento.aspx?CodigoInstituicao=1&Tela=ext&descTipo=IPE&numProtocolo=1547175",
        "annotation": "Official SIMPAR CVM Material Fact on Aratu terminal sale to ICTSI. Supports ictsi_aratu_hsim_2026.",
        "supports": ["ictsi_aratu_hsim_2026", "hunt_infra_port_ownership"],
    },
)

# 11 energy/fission_smr — Candu Energy / CNEA MoU to restart PIAP heavy-water plant (Neuquén)
A(
    {
        "id": "candu_cnea_piap_mou_2025",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "allied",
        "counterpart": "Candu Energy (AtkinsRéalis) — MoU with CNEA to restart PIAP heavy-water plant (Neuquén)",
        "country": "Argentina",
        "asset": "Memorandum of understanding for restart of CNEA-owned Industrial Heavy Water Plant (PIAP) in Neuquén plus long-term acquisition of heavy-water output for CANDU fleet support; AtkinsRéalis to support basic refurbishment; PIAP expected to resume as early as 2027 (idle ~8 years per CNEA)",
        "investment_type": "mou_refurbishment",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-39.1",
        "lon": "-68.55",
        "geo_note": "PIAP / Arroyito area, Neuquén Province (AtkinsRéalis / CNEA statements; approximate).",
        "evidence": "documented",
        "source_id": "atkinsrealis_cnea_piap_20250521",
        "note": "Actor: Candu Energy Inc. / AtkinsRéalis (Canadian) — allied; counterpart CNEA (Argentine state). Company trade release 21 May 2025. MoU / pre-FID — no CAPEX USD on opened page. Distinct from CNNC Atucha Hualong proxy, CAREM/Meitner/Nuclearis SMR rows; CANDU heavy-water supply chain supporting Embalse-class technology in Argentina.",
    },
    {
        "id": "candu_cnea_piap_mou_2025",
        "retrieved": "2026-10-01",
        "source_id": "atkinsrealis_cnea_piap_20250521",
        "url": "https://www.atkinsrealis.com/en/media/trade-releases/2025/2025-05-21",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Candu Energy Inc., an AtkinsRéalis company, announces it has signed a memorandum of understanding (MOU) with the National Atomic Energy Commission (CNEA) of Argentina … to produce heavy water. The MOU provides for the restart of the Industrial Heavy Water Plant (PIAP) in Neuquén, Argentina, along with the long-term acquisition of its heavy water output.",
        "note": "Opened AtkinsRéalis company trade release 21 May 2025.",
    },
    {
        "id": "atkinsrealis_cnea_piap_20250521",
        "type": "company",
        "chicago": "AtkinsRéalis / Candu Energy Inc. “AtkinsRéalis secures supply of Heavy water and future of CANDU technology around the world.” Trade release, 21 May 2025.",
        "url": "https://www.atkinsrealis.com/en/media/trade-releases/2025/2025-05-21",
        "annotation": "Company primary on Candu–CNEA PIAP heavy-water MoU in Neuquén. Supports candu_cnea_piap_mou_2025.",
        "supports": ["candu_cnea_piap_mou_2025", "hunt_energy_fission_smr"],
    },
)

# 12 resources/nickel — miss (BNDES Piauí / Centaurus Jaguar already logged)
# 13 infrastructure/bridges_roads — miss (Salvador–Itaparica logged C21; MTC Arequipa–La Joya does not name CRBC on opened page)
# 14 infrastructure/engineering_epc — miss (STRACON Pérez Caldera logged C21)
# 15 energy/power_plants_grid — miss (State Grid NE UHV logged C22; thick)
# 16 resources/niobium — miss (CBMM/CMOC/St George already logged)

# 17 energy/other_renewables — CATL TENER BESS for CIP La Alegría Solar (Campeche) — press proxy
A(
    {
        "id": "catl_cip_alegria_bess_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "CATL — TENER BESS supply for CIP La Alegría Solar (Campeche)",
        "country": "Mexico",
        "asset": "Reported supply agreement for 313 MW / 1,639.45 MWh CATL TENER BESS co-located with CIP La Alegría Solar hybrid (Campeche); described as Mexico’s first >1 GWh BESS; configuration larger than March Semarnat MIA-R BESS figures",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "19.83",
        "lon": "-90.53",
        "geo_note": "Campeche municipality / state (pv magazine / ess-news citing CATL–CIP; approximate).",
        "evidence": "proxy",
        "source_id": "ess_news_catl_alegria_20260930",
        "note": "UNVERIFIED proxy. Actor: CATL (PRC) — prc; developer CIP (Danish) GMF II. Trade press (pv magazine Mexico / ess-news) attributing figures to CATL announcement; opened CATL.com and CIP.com pages do not carry a named La Alegría supply release. No contract USD. Coded other_renewables for grid-scale BESS (same pattern as Tesla Celda / AES Andes hybrid). Distinct from Tesla Colbún Celda and AES Andes Pampas/Cristales.",
    },
    {
        "id": "catl_cip_alegria_bess_2026",
        "retrieved": "2026-10-01",
        "source_id": "ess_news_catl_alegria_20260930",
        "url": "https://www.ess-news.com/2026/09/30/catl-to-supply-313-mw-1-64-gwh-bess-in-mexico/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "CATL has signed an agreement with Copenhagen Infrastructure Partners (CIP) to supply a 313 MW/1,639.45 MWh BESS to the La Alegría Solar project, which the Danish investment manager is developing in the Mexican state of Campeche.",
        "note": "Opened ess-news (pv magazine) 30 Sep 2026 reprint attributing CATL announcement; company primary URL not located this cycle.",
    },
    {
        "id": "ess_news_catl_alegria_20260930",
        "type": "press",
        "chicago": "Ini, Luis. “CATL to supply 313 MW/1.64 GWh BESS in Mexico.” ess news / pv magazine, 30 September 2026.",
        "url": "https://www.ess-news.com/2026/09/30/catl-to-supply-313-mw-1-64-gwh-bess-in-mexico/",
        "annotation": "UNVERIFIED press proxy on CATL–CIP La Alegría BESS. Supports catl_cip_alegria_bess_2026.",
        "supports": ["catl_cip_alegria_bess_2026", "hunt_energy_other_renewables"],
    },
)

# 18 resources/copper — Chinalco Toromocho ITS-3 expansion >USD 700m (Senace / MINEM)
A(
    {
        "id": "chinalco_toromocho_its3_700m_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "prc",
        "counterpart": "Minera Chinalco Perú — Toromocho ITS-3 expansion to 170,000 TPD (Junín)",
        "country": "Peru",
        "asset": "Senace-approved Third ITS to MEIA for Toromocho expansion to 170,000 TPD: 28 projects / 33 components with investment superior to USD 700 million over next three years; adds molybdenum recovery alongside copper concentrator optimization",
        "investment_type": "expansion_capex",
        "value": "700000000",
        "currency": "USD",
        "value_usd": "700000000",
        "fx_usd": "1",
        "fx_date": "2026-04-14",
        "year": "2026",
        "status": "active",
        "lat": "-11.6",
        "lon": "-76.14",
        "geo_note": "Toromocho / Morococha district, Junín (MINEM release).",
        "evidence": "documented",
        "source_id": "minem_toromocho_its3_20260414",
        "note": "Actor: Chinalco Perú (PRC SOE subsidiary) — prc. Official MINEM news 14 Apr 2026 quoting Chinalco executive on >USD 700m / 28 projects after Senace ITS approval. Floor figure (page says 'superior a los 700 millones'). Distinct from chinalco_toromocho_peru (ownership presence) and fluor_toromocho_expansion_peru (Fluor EPCm row).",
    },
    {
        "id": "chinalco_toromocho_its3_700m_2026",
        "retrieved": "2026-10-01",
        "source_id": "minem_toromocho_its3_20260414",
        "url": "https://www.gob.pe/institucion/minem/noticias/1378448-minem-impulsa-incremento-en-la-produccion-de-minerales-criticos-a-traves-de-la-expansion-del-proyecto-toromocho",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Esta aprobación otorga la viabilidad para la implementación de 28 proyectos, que conjunto comprende un total de 33 componentes con una inversión superior a los 700 millones de dólares, en los próximos tres años",
        "note": "Opened MINEM (gob.pe) official news 14 Apr 2026.",
    },
    {
        "id": "minem_toromocho_its3_20260414",
        "type": "government",
        "chicago": "Peru. Ministerio de Energía y Minas. “MINEM impulsa incremento en la producción de minerales críticos a través de la expansión del Proyecto Toromocho.” 14 April 2026.",
        "url": "https://www.gob.pe/institucion/minem/noticias/1378448-minem-impulsa-incremento-en-la-produccion-de-minerales-criticos-a-traves-de-la-expansion-del-proyecto-toromocho",
        "annotation": "Official MINEM notice of Toromocho ITS-3 expansion >USD 700m. Supports chinalco_toromocho_its3_700m_2026.",
        "supports": ["chinalco_toromocho_its3_700m_2026", "hunt_res_copper"],
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
        "hunt_res_balsa": "Cycle 23: equal budget; no new named exporter/importer stake beyond WITS years (miss).",
        "hunt_res_graphite": "Cycle 23: equal budget; Graphcoa/South Star/Nacional/Urbix set already logged (miss).",
        "hunt_infra_building_materials": "Cycle 23: equal budget; CSN Cimentos sale still not closed — Huaxin/Votorantim/Polimix bids open (miss).",
        "hunt_latam_rail_telecom": "Cycle 23: equal budget; Alstom Santiago Line 7 first-train delivery is milestone of logged alstom_santiago_line7_2025 (miss).",
        "hunt_res_lithium": "Cycle 23: equal budget; Eramet RIGI / Rio Tinto Rincon financing already logged (miss).",
        "hunt_res_water": "Cycle 23: equal budget; Veolia Aguas Pacífico logged C21 (miss).",
        "hunt_energy_solar": "Cycle 23: logged jinko_casa_ventos_413mwp_2026.",
        "hunt_infra_port_cranes": "Cycle 23: equal budget; Tecon Santos / Suape / Cartagena crane set already logged (miss).",
        "hunt_energy_wind": "Cycle 23: equal budget; Statkraft Emma / Vestas Esquina / Goldwind Sento Sé already logged (miss).",
        "hunt_infra_port_ownership": "Cycle 23: logged ictsi_aratu_hsim_2026.",
        "hunt_energy_fission_smr": "Cycle 23: logged candu_cnea_piap_mou_2025.",
        "hunt_res_nickel": "Cycle 23: equal budget; BNDES Piauí / Centaurus Jaguar set already logged (miss).",
        "hunt_infra_bridges_roads": "Cycle 23: equal budget; Salvador–Itaparica logged C21; MTC Arequipa–La Joya page does not name CRBC (miss).",
        "hunt_infra_engineering_epc": "Cycle 23: equal budget; STRACON Pérez Caldera logged C21 (miss).",
        "hunt_br_power_equip": "Cycle 23: equal budget; State Grid NE UHV construction logged C22 (miss).",
        "hunt_fenb_araxa": "Cycle 23: equal budget; CBMM/CMOC/St George set already logged (miss).",
        "hunt_energy_other_renewables": "Cycle 23: logged catl_cip_alegria_bess_2026 (UNVERIFIED proxy).",
        "hunt_res_copper": "Cycle 23: logged chinalco_toromocho_its3_700m_2026.",
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
    print("Cycle 23 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
