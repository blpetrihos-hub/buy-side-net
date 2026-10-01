#!/usr/bin/env python3
"""Cycle 42 hunt: shuffle_seed=20261042; equal budget; U.S. side ≥1/3; thin_topup after."""
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


# seed 20261042 order:
# copper, lithium, nickel, building_materials, port_ownership, other_renewables, wind,
# water, graphite, port_cranes, rail, power_plants_grid, engineering_epc, niobium,
# balsa, solar, fission_smr, bridges_roads

# 1 resources/copper — Chilean Cobalt EXIM LOI up to USD 375m (U.S. side)
A(
    {
        "id": "chilean_cobalt_exim_loi_375m_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "us",
        "counterpart": "U.S. EXIM — LOI for Chilean Cobalt La Cobaltera / El Cofre Co-Cu",
        "country": "Chile",
        "asset": "17 Aug 2026: Chilean Cobalt Corp. (U.S., OTCQB:COBA) receives new non-binding EXIM Letter of Interest for potential debt funding up to USD 375 million (tenor up to 15 years) under China and Transformational Exports Program (CTEP) for La Cobaltera / El Cofre cobalt-copper project (San Juan district, northern Chile). Replaces prior USD 317.4m LOI. Formal application targeted 2027 — not a closed commitment.",
        "investment_type": "financing",
        "value": "375000000",
        "currency": "USD",
        "value_usd": "375000000",
        "fx_usd": "1",
        "fx_date": "2026-08-17",
        "year": "2026",
        "status": "active",
        "lat": "-27.3",
        "lon": "-70.9",
        "geo_note": "San Juan mining district / northern Chile (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "chilean_cobalt_exim_loi_20260817",
        "note": "Actor: U.S. EXIM LOI to U.S.-based Chilean Cobalt — us. Company AccessNewswire 17 Aug 2026. Non-binding LOI; Co-Cu project coded under copper (cobalt not a taxonomy subcategory).",
    },
    {
        "id": "chilean_cobalt_exim_loi_375m_2026",
        "retrieved": "2026-10-01",
        "source_id": "chilean_cobalt_exim_loi_20260817",
        "url": "https://www.accessnewswire.com/newsroom/en/metals-and-mining/chilean-cobalt-corp.-announces-receipt-of-new-usd-375-million-letter-of-interest-1207683",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Chilean Cobalt Corp. … is pleased to announce that it has received a new non-binding Letter of Interest (“LOI”) from the Export-Import Bank of the United States (“EXIM”) for a potential debt funding package of up to $375 million, with a tenor of up to 15 years, to support the Company’s proposed capital funding plan for the La Cobaltera / El Cofre project in northern Chile.",
        "note": "Opened company AccessNewswire release 17 Aug 2026.",
    },
    {
        "id": "chilean_cobalt_exim_loi_20260817",
        "type": "company",
        "chicago": "Chilean Cobalt Corp. “Chilean Cobalt Corp. Announces Receipt of New USD $375 Million Letter of Interest from US EXIM Bank.” Access Newswire, 17 August 2026.",
        "url": "https://www.accessnewswire.com/newsroom/en/metals-and-mining/chilean-cobalt-corp.-announces-receipt-of-new-usd-375-million-letter-of-interest-1207683",
        "annotation": "U.S. company release on EXIM non-binding LOI up to USD 375m for Chile Co-Cu project. Supports chilean_cobalt_exim_loi_375m_2026.",
        "supports": ["chilean_cobalt_exim_loi_375m_2026", "hunt_res_copper"],
    },
)

# 2 resources/lithium — value fill Albemarle TED CAPEX USD 3.1bn (company DLE page)
U(
    "albemarle_ted_dle_atacama_2026",
    {
        "value": "3100000000",
        "currency": "USD",
        "value_usd": "3100000000",
        "fx_usd": "1",
        "fx_date": "2026-03-25",
        "source_id": "albemarle_dle_ted_capex_page",
        "note": "Actor: Albemarle Corporation (U.S.) — us. Cycle 42 value fill: company Chile DLE page states total estimated TED investment USD 3.100 billion (alongside prior EIA release without CAPEX). Pre-FID; still permitting.",
        "asset": "25 Mar 2026 EIA for TED DLE at Salar de Atacama; company DLE page states total estimated TED investment USD 3.100 billion; modular plant up to six ~50 l/s lines; ~29 km 220 kV line; FID pending permitting. Pilot at La Negra logged separately.",
    },
    {
        "id": "albemarle_ted_dle_atacama_2026",
        "retrieved": "2026-10-01",
        "source_id": "albemarle_dle_ted_capex_page",
        "url": "https://www.albemarle.com/cl/en/dle",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "$3.100 Millions (US) is the total estimated investment of the TED Project.",
        "note": "Opened Albemarle Chile English DLE/TED project page for CAPEX fill.",
    },
    {
        "id": "albemarle_dle_ted_capex_page",
        "type": "company",
        "chicago": "Albemarle Corporation. “Direct Lithium Extraction: Innovation with Purpose.” Albemarle Chile DLE project page. Accessed 1 October 2026.",
        "url": "https://www.albemarle.com/cl/en/dle",
        "annotation": "Company TED/DLE page stating USD 3.1bn estimated TED investment and La Negra pilot ~USD 30m. Supports albemarle_ted_dle_atacama_2026 value fill and albemarle_la_negra_dle_pilot_30m_2026.",
        "supports": [
            "albemarle_ted_dle_atacama_2026",
            "albemarle_la_negra_dle_pilot_30m_2026",
            "hunt_res_lithium",
        ],
    },
)

A(
    {
        "id": "albemarle_la_negra_dle_pilot_30m_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "us",
        "counterpart": "Albemarle — La Negra DLE pilot plant (Antofagasta)",
        "country": "Chile",
        "asset": "Company DLE page: pilot plant at La Negra complex (Antofagasta) representing an investment of about USD 30 million; validates TED commercial DLE pathway (>94% Li recovery cited in related community notes). Distinct from albemarle_ted_dle_atacama_2026 commercial TED CAPEX.",
        "investment_type": "pilot_plant",
        "value": "30000000",
        "currency": "USD",
        "value_usd": "30000000",
        "fx_usd": "1",
        "fx_date": "2026-03-25",
        "year": "2026",
        "status": "active",
        "lat": "-23.65",
        "lon": "-70.40",
        "geo_note": "La Negra industrial complex, Antofagasta Region (company geography; approximate).",
        "evidence": "documented",
        "source_id": "albemarle_dle_ted_capex_page",
        "note": "Actor: Albemarle (U.S.) — us. Company Chile DLE page. Pilot spend distinct from TED USD 3.1bn commercial estimate.",
    },
    {
        "id": "albemarle_la_negra_dle_pilot_30m_2026",
        "retrieved": "2026-10-01",
        "source_id": "albemarle_dle_ted_capex_page",
        "url": "https://www.albemarle.com/cl/en/dle",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Pilot plant at the La Negra complex in Antofagasta, representing an investment of about $30 million dollars.",
        "note": "Opened Albemarle Chile DLE page.",
    },
    {
        "id": "albemarle_dle_ted_capex_page",
        "type": "company",
        "chicago": "Albemarle Corporation. “Direct Lithium Extraction: Innovation with Purpose.” Albemarle Chile DLE project page. Accessed 1 October 2026.",
        "url": "https://www.albemarle.com/cl/en/dle",
        "annotation": "Company TED/DLE page stating USD 3.1bn estimated TED investment and La Negra pilot ~USD 30m. Supports albemarle_ted_dle_atacama_2026 value fill and albemarle_la_negra_dle_pilot_30m_2026.",
        "supports": [
            "albemarle_ted_dle_atacama_2026",
            "albemarle_la_negra_dle_pilot_30m_2026",
            "hunt_res_lithium",
        ],
    },
)

# 3 resources/nickel — Centaurus Jaguar international financier interest up to USD 320m
A(
    {
        "id": "centaurus_jaguar_intl_finance_320m_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "Centaurus Metals — Jaguar Ni project finance proposals (up to USD 320m)",
        "country": "Brazil",
        "asset": "13 Apr 2026 ASX: Centaurus receives strong interest from ten leading international resource financiers for Jaguar Nickel Sulphide Project (Pará); non-binding offers for up to USD 320 million (multiple proposals over USD 250m). Preferred financier/syndicate targeted Q3 2026 with FID. Complements BNDES FINEM LOI (R$1bn) and Glencore offtake — not a closed facility.",
        "investment_type": "financing",
        "value": "320000000",
        "currency": "USD",
        "value_usd": "320000000",
        "fx_usd": "1",
        "fx_date": "2026-04-13",
        "year": "2026",
        "status": "active",
        "lat": "-6.65",
        "lon": "-49.0",
        "geo_note": "Jaguar Nickel Project, Carajás / Pará (company ASX).",
        "evidence": "documented",
        "source_id": "centaurus_jaguar_finance_20260413",
        "note": "Actor: Centaurus Metals (Australia) — allied. Company ASX PDF 13 Apr 2026. Non-binding offers ceiling USD 320m — not closed loan.",
    },
    {
        "id": "centaurus_jaguar_intl_finance_320m_2026",
        "retrieved": "2026-10-01",
        "source_id": "centaurus_jaguar_finance_20260413",
        "url": "https://www.centaurus.com.au/site/pdf/54d68631-943e-4bb3-b950-0c2dfa3f4146/Strong-International-Financier-Interest-for-Jaguar-Funding.pdf?Platform=ListPage",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Non-binding offers received are for up to US$320 million, with multiple proposals over US$250 million.",
        "note": "Opened Centaurus ASX PDF 13 Apr 2026.",
    },
    {
        "id": "centaurus_jaguar_finance_20260413",
        "type": "company",
        "chicago": "Centaurus Metals Limited. “Centaurus Receives Strong Interest from Leading International Financiers for Jaguar Nickel Development.” ASX announcement, 13 April 2026.",
        "url": "https://www.centaurus.com.au/site/pdf/54d68631-943e-4bb3-b950-0c2dfa3f4146/Strong-International-Financier-Interest-for-Jaguar-Funding.pdf?Platform=ListPage",
        "annotation": "ASX PDF on non-binding Jaguar project-finance offers up to USD 320m. Supports centaurus_jaguar_intl_finance_320m_2026.",
        "supports": ["centaurus_jaguar_intl_finance_320m_2026", "hunt_res_nickel"],
    },
)

# 4 infrastructure/building_materials — Holcim Mexico Geocycle Tecomán ~MXN 200m
A(
    {
        "id": "holcim_geocycle_tecoman_mxn200m_2026",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Holcim México / Geocycle — Tecomán biomass co-processing plant",
        "country": "Mexico",
        "asset": "4 Aug 2026: Holcim México announces investment of nearly MXN 200 million via Geocycle for biomass (sugarcane bagasse) drying/grinding infrastructure at Tecomán, Colima — ~45,000 t/y biomass; kiln waste-heat drying up to 220 t/day; low-carbon cement fuel feedstock. Distinct from Holcim Pacasmayo / Colombia Cemex acquisition / Macuspana grind rows.",
        "investment_type": "plant_capex",
        "value": "200000000",
        "currency": "MXN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "18.92",
        "lon": "-103.87",
        "geo_note": "Tecomán, Colima (company release).",
        "evidence": "documented",
        "source_id": "holcim_mx_geocycle_tecoman_20260804",
        "note": "Actor: Holcim (Switzerland) / Holcim México — allied. Company Spanish release. MXN stored without FX.",
    },
    {
        "id": "holcim_geocycle_tecoman_mxn200m_2026",
        "retrieved": "2026-10-01",
        "source_id": "holcim_mx_geocycle_tecoman_20260804",
        "url": "https://www.holcim.com.mx/holcim-mexico-invierte-cerca-de-200-millones-de-pesos-para-acelerar-la-economia-circular",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Holcim México anunció una reciente inversión cercana a 200 millones de pesos para poner en marcha infraestructura innovadora en Tecomán, Colima. Desarrollada a través de Geocycle … la nueva planta permitirá resolver la problemática de manejo de cerca de 45,000 toneladas anuales de biomasa de la industria azucarera.",
        "note": "Opened Holcim México Spanish release 4 Aug 2026.",
    },
    {
        "id": "holcim_mx_geocycle_tecoman_20260804",
        "type": "company",
        "chicago": "Holcim México. “Holcim México invierte cerca de 200 millones de pesos para acelerar la economía circular.” 4 August 2026.",
        "url": "https://www.holcim.com.mx/holcim-mexico-invierte-cerca-de-200-millones-de-pesos-para-acelerar-la-economia-circular",
        "annotation": "Company Spanish release on Geocycle Tecomán ~MXN 200m biomass plant. Supports holcim_geocycle_tecoman_mxn200m_2026.",
        "supports": ["holcim_geocycle_tecoman_mxn200m_2026", "hunt_infra_building_materials"],
    },
)

# 5 infrastructure/port_ownership — APM Lazaro Phase III >USD 350m
A(
    {
        "id": "apmt_lazaro_phase3_350m_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "APM Terminals — Lázaro Cárdenas Phase III expansion",
        "country": "Mexico",
        "asset": "20 Mar 2026: APM Terminals inaugurates Lázaro Cárdenas Phase II (>USD 140m / MXN 2.8bn) and announces immediate start of Phase III with investment of more than USD 350 million (MXN 6.2bn) — +450 m berth to 1,200 m quay, yard expansion, new STS cranes; accelerates capacity ~8 years. Distinct from apmt_lazaro_phase2_2025 (Phase II USD 165m invested-to-date figure).",
        "investment_type": "concession",
        "value": "350000000",
        "currency": "USD",
        "value_usd": "350000000",
        "fx_usd": "1",
        "fx_date": "2026-03-20",
        "year": "2026",
        "status": "active",
        "lat": "17.95",
        "lon": "-102.17",
        "geo_note": "Lázaro Cárdenas, Michoacán (APM Terminals release).",
        "evidence": "documented",
        "source_id": "apmt_lazaro_phase3_20260320",
        "note": "Actor: APM Terminals (Maersk/Denmark) — allied. Company release 20 Mar 2026. Value at stated floor (>USD 350m).",
    },
    {
        "id": "apmt_lazaro_phase3_350m_2026",
        "retrieved": "2026-10-01",
        "source_id": "apmt_lazaro_phase3_20260320",
        "url": "https://www.apmterminals.com/en/news/news-releases/2026/260320-APMTerminals-lazaro-cardenas-announces-investment-PhaseII",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "APM Terminals Lázaro Cárdenas inaugurated the Phase II expansion … and announced the immediate start of construction of Phase III, a new stage of growth supported by an investment of more than USD 350 million (MXN 6.2 billion).",
        "note": "Opened APM Terminals company release 20 Mar 2026.",
    },
    {
        "id": "apmt_lazaro_phase3_20260320",
        "type": "company",
        "chicago": "APM Terminals. “APM Terminals Lázaro Cárdenas inaugurates Phase II and announces investment for the next stage.” 20 March 2026.",
        "url": "https://www.apmterminals.com/en/news/news-releases/2026/260320-APMTerminals-lazaro-cardenas-announces-investment-PhaseII",
        "annotation": "Company release on Lazaro Phase II inauguration and Phase III >USD 350m. Supports apmt_lazaro_phase3_350m_2026.",
        "supports": ["apmt_lazaro_phase3_350m_2026", "hunt_infra_port_ownership"],
    },
)

# 6–15 other_renewables, wind, water, graphite, port_cranes, rail, power_plants_grid,
# engineering_epc, niobium, balsa — miss (equal budget)

# 16 energy/solar — FinDev Canada Illa Peru USD 56m
A(
    {
        "id": "findev_illa_solar_56m_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "allied",
        "counterpart": "FinDev Canada — Project Illa solar PV (Arequipa) loan",
        "country": "Peru",
        "asset": "5 Feb 2026: FinDev Canada commits USD 56 million loan to Energía Renovable La Joya S.A. (Enhol Energía / Grupo Enhol) for Project Illa — 396 MW solar PV in Arequipa, described as Peru’s largest solar plant; part of USD 289 million Santander CIB-led facility. Transaction signing 31 Dec 2025 per FinDev disclosure summary.",
        "investment_type": "financing",
        "value": "56000000",
        "currency": "USD",
        "value_usd": "56000000",
        "fx_usd": "1",
        "fx_date": "2026-02-05",
        "year": "2026",
        "status": "active",
        "lat": "-16.40",
        "lon": "-71.54",
        "geo_note": "Arequipa Region solar site (FinDev / Enhol geography; approximate pin).",
        "evidence": "documented",
        "source_id": "findev_illa_20260205",
        "note": "Actor: FinDev Canada (Canadian DFI) — allied, with Spanish Enhol sponsor. Official FinDev release.",
    },
    {
        "id": "findev_illa_solar_56m_2026",
        "retrieved": "2026-10-01",
        "source_id": "findev_illa_20260205",
        "url": "https://www.findevcanada.ca/en/news/findev-canada-commits-usd-56-million-energia-renovable-joya-sa-enhol-energia-strengthen",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "FinDev Canada, announces a USD 56 million loan to Energía Renovable La Joya S.A. The commitment will support the development, construction, and operation of Project Illa, a 396 MW solar photovoltaic (PV) power plant in Arequipa, Peru.",
        "note": "Opened FinDev Canada English release 5 Feb 2026.",
    },
    {
        "id": "findev_illa_20260205",
        "type": "ifi",
        "chicago": "FinDev Canada. “FinDev Canada commits USD 56 million to Energía Renovable La Joya S.A. (Enhol Energía) to strengthen renewable energy and economic growth in Peru.” 5 February 2026.",
        "url": "https://www.findevcanada.ca/en/news/findev-canada-commits-usd-56-million-energia-renovable-joya-sa-enhol-energia-strengthen",
        "annotation": "Canadian DFI release on USD 56m Illa solar loan in Peru. Supports findev_illa_solar_56m_2026.",
        "supports": ["findev_illa_solar_56m_2026", "hunt_energy_solar"],
    },
)

# 17 fission_smr, 18 bridges_roads — miss


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added, updated = [], []

    def upsert_bib(bib_entry):
        if not bib_entry:
            return
        sid = bib_entry["id"]
        if sid in bib_by:
            existing = bib[bib_by[sid]]
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
            if bib_entry.get("supports"):
                existing["supports"] = sorted(
                    set(existing.get("supports") or []) | set(bib_entry["supports"])
                )
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

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
        upsert_bib(bib_entry)

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
        upsert_bib(bib_entry)

    hunt_updates = {
        "hunt_res_copper": "Cycle 42: logged chilean_cobalt_exim_loi_375m_2026 (U.S. EXIM LOI).",
        "hunt_res_lithium": "Cycle 42: value-filled albemarle_ted_dle_atacama_2026 to USD 3.1bn; logged albemarle_la_negra_dle_pilot_30m_2026.",
        "hunt_res_nickel": "Cycle 42: logged centaurus_jaguar_intl_finance_320m_2026.",
        "hunt_infra_building_materials": "Cycle 42: logged holcim_geocycle_tecoman_mxn200m_2026.",
        "hunt_infra_port_ownership": "Cycle 42: logged apmt_lazaro_phase3_350m_2026.",
        "hunt_energy_other_renewables": "Cycle 42: equal budget; Cubico/Jinko/AES already (miss).",
        "hunt_energy_wind": "Cycle 42: equal budget; Vestas/Nordex/Goldwind/EDF already (miss).",
        "hunt_res_water": "Cycle 42: equal budget; Sacyr Coquimbo/Antofagasta / Cox Rosarito already (miss).",
        "hunt_res_graphite": "Cycle 42: equal budget; Graphcoa/South Star already (miss).",
        "hunt_infra_port_cranes": "Cycle 42: equal budget; Lazaro Phase III STS OEM unnamed (miss).",
        "hunt_latam_rail_telecom": "Cycle 42: equal budget; Alstom Mexico / CRRC Salvador already (miss).",
        "hunt_br_power_equip": "Cycle 42: equal budget; Hitachi/Siemens/GE already (miss).",
        "hunt_infra_engineering_epc": "Cycle 42: equal budget; CHEC Chancay / Worley already (miss).",
        "hunt_fenb_araxa": "Cycle 42: equal budget; St George R$3bn / CBMM already (miss).",
        "hunt_res_balsa": "Cycle 42: equal budget; AIMA Siemens MoU / 2025 shares already (miss).",
        "hunt_energy_solar": "Cycle 42: logged findev_illa_solar_56m_2026.",
        "hunt_energy_fission_smr": "Cycle 42: equal budget; Peru FIRST / INB–Westinghouse already (miss).",
        "hunt_infra_bridges_roads": "Cycle 42: equal budget; CAF/Mota-Engil/CRBC already (miss).",
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
    print("Cycle 42 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 42 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
