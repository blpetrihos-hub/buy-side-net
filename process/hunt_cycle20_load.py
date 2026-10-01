#!/usr/bin/env python3
"""Cycle 20 hunt: shuffle_seed=20261020; equal budget across 18 subcategories."""
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


# seed 20261020 order:
# nickel, wind, bridges_roads, balsa, copper, water, building_materials, engineering_epc,
# fission_smr, rail, port_cranes, other_renewables, power_plants_grid, port_ownership,
# lithium, niobium, graphite, solar

# 1 resources/nickel — miss (Atlantic UG / Jervois logged prior)
# 2 energy/wind — miss
# 3 infrastructure/bridges_roads — miss
# 4 resources/balsa — miss

# 5 resources/copper — Vicuña RIGI PEELP (BHP/Lundin)
A(
    {
        "id": "vicuna_rigi_peelp_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "allied",
        "counterpart": "Vicuña Argentina (BHP 50% / Lundin Mining 50%) — Josemaría–Filo del Sol RIGI PEELP",
        "country": "Argentina",
        "asset": "Argentine Economy Ministry Resolución 1154/2026 approves Vicuña RIGI PEELP adhesion and investment plan for Josemaría + Filo del Sol Cu-Au-Ag district (San Juan); declared total investment USD 9,737,014,000 (computable assets USD 9,024,732,281); Stage 1 CAPEX estimate USD 7.1bn per Lundin technical study; FID Stage 1 targeted end-2026",
        "investment_type": "ownership_equity",
        "value": "9737014000",
        "currency": "USD",
        "value_usd": "9737014000",
        "fx_usd": "1",
        "fx_date": "2026-07-30",
        "year": "2026",
        "status": "active",
        "lat": "-28.9",
        "lon": "-69.5",
        "geo_note": "Josemaría / Filo del Sol district, San Juan Province (Boletín Oficial / Lundin).",
        "evidence": "documented",
        "source_id": "boletin_vicuna_rigi_1154_2026",
        "note": "Actors: Vicuña Corp JV — BHP (Australian) + Lundin Mining (Canadian) — allied. Primary: Boletín Oficial Resolución 1154/2026 (published 30 Jul 2026). Complements Lundin 16 Jun 2026 RIGI PEELP notice. Distinct from FCX El Abra / Codelco–Anglo Andina–Los Bronces / FQM Taca Taca copper rows. Pre-FID.",
    },
    {
        "id": "vicuna_rigi_peelp_2026",
        "retrieved": "2026-10-01",
        "source_id": "boletin_vicuna_rigi_1154_2026",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/345167/20260730",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Que la Solicitante declaró que el Proyecto implicará una inversión total de nueve mil setecientos treinta y siete millones catorce mil dólares estadounidenses (USD 9.737.014.000) … ARTÍCULO 1°.- Apruébase la solicitud de adhesión al Régimen de Incentivo para Grandes Inversiones (RIGI), como Proyecto de Exportación Estratégica de Largo Plazo … presentado por Vicuña Argentina SA … yacimientos Josemaría y Filo del Sol.",
        "note": "Opened Argentine Official Gazette Resolución 1154/2026. Ownership split corroborated via Lundin Mining 16 Jun 2026 company release.",
    },
    {
        "id": "boletin_vicuna_rigi_1154_2026",
        "type": "government",
        "chicago": "Argentina. Ministerio de Economía. “Resolución 1154/2026” (RIGI PEELP — Vicuña). Boletín Oficial, 30 July 2026.",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/345167/20260730",
        "annotation": "Official Gazette approval of Vicuña RIGI PEELP and USD 9.737bn investment plan. Supports vicuna_rigi_peelp_2026.",
        "supports": ["vicuna_rigi_peelp_2026", "hunt_res_copper"],
    },
)

# 6 resources/water — miss
# 7 infrastructure/building_materials — miss (CSN sale not closed)
# 8 infrastructure/engineering_epc — miss
# 9 energy/fission_smr — miss

# 10 infrastructure/rail — Alstom Santo Domingo Metro Line 2 extension trains
A(
    {
        "id": "alstom_santo_domingo_l2_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "Alstom — eight Metropolis trains for Santo Domingo Metro Line 2 extension",
        "country": "Dominican Republic",
        "asset": "Design/manufacture/delivery of eight three-car Metropolis trains for OPRET Line 2C extension (María Montez–Los Alcarrizos); first two delivered Apr 2026 from Santa Perpétua (Barcelona); Caribbean LatAm geography",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "18.49",
        "lon": "-69.99",
        "geo_note": "Santo Domingo Metro Line 2 / Los Alcarrizos corridor (Alstom release).",
        "evidence": "documented",
        "source_id": "alstom_santo_domingo_l2_20260402",
        "note": "Actor: Alstom (French) — allied; customer OPRET. Company 2 Apr 2026 press. No contract USD on opened page. Distinct from Alstom Santiago Line 7 / SP Line 6 / Mexico DMU rail rows.",
    },
    {
        "id": "alstom_santo_domingo_l2_2026",
        "retrieved": "2026-10-01",
        "source_id": "alstom_santo_domingo_l2_20260402",
        "url": "https://www.alstom.com/press-releases-news/2026/4/alstom-delivers-first-trains-extension-line-2-santo-domingo-metro",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Alstom … announced today that it has delivered the first two of eight new trains to the Oficina para el Reordenamiento del Transporte (OPRET) for the Santo Domingo Metro Line 2 expansion project. Alstom is designing, manufacturing and delivering eight three-car Metropolis trains …",
        "note": "Opened Alstom company press release 2 Apr 2026.",
    },
    {
        "id": "alstom_santo_domingo_l2_20260402",
        "type": "company",
        "chicago": "Alstom. “Alstom delivers the first trains for the extension of Line 2 of the Santo Domingo Metro.” 2 April 2026.",
        "url": "https://www.alstom.com/press-releases-news/2026/4/alstom-delivers-first-trains-extension-line-2-santo-domingo-metro",
        "annotation": "Company primary delivery notice for eight Metropolis trains (Santo Domingo L2). Supports alstom_santo_domingo_l2_2026.",
        "supports": ["alstom_santo_domingo_l2_2026", "hunt_latam_rail_telecom"],
    },
)

# 11 infrastructure/port_cranes — SANY STS/RTG for HGT Aracruz
A(
    {
        "id": "sany_hgt_aracruz_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "SANY Marine — 6 STS + 20 RTG for HGT Aracruz (Espírito Santo)",
        "country": "Brazil",
        "asset": "Agreement for 26 large port machines (6 ship-to-shore + 20 rubber-tired gantry cranes) for greenfield HGT Aracruz container terminal; SANY states largest single South American port-equipment order to date; contract USD not disclosed",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-19.82",
        "lon": "-40.27",
        "geo_note": "Aracruz, Espírito Santo (HGT / SANY releases).",
        "evidence": "documented",
        "source_id": "sany_hgt_aracruz_20260710",
        "note": "Actor: SANY Marine (PRC) — prc; buyer HGT Aracruz (Hapag-Lloyd HGT 50% / Grupo Imetame 50%). Company SANY 10 Jul 2026 release (counts) + HGT Aracruz site naming Brazil. Distinct from sany_apmt_suape_sts_rtg_2026.",
    },
    {
        "id": "sany_hgt_aracruz_2026",
        "retrieved": "2026-10-01",
        "source_id": "sany_hgt_aracruz_20260710",
        "url": "https://www.sanyglobal.com/press_releases/4881/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "SANY Marine and Hanseatic Global Terminals (HGT) officially signed an agreement for the purchase of 26 large port machines, including six ship-to-shore (STS) cranes and 20 rubber-tired gantry (RTG) cranes, marking SANY Marine’s largest single port equipment order in South America to date.",
        "note": "Opened SANY company release. Brazil/Aracruz pin from HGT company page: https://www.hanseaticglobalterminals.com/en/hgt/press/HGTGrupoImetameAgreement.html",
    },
    {
        "id": "sany_hgt_aracruz_20260710",
        "type": "company",
        "chicago": "SANY Marine. “SANY Marine Signs Record South American Port Equipment Order with HGT.” 10 July 2026.",
        "url": "https://www.sanyglobal.com/press_releases/4881/",
        "annotation": "Company primary 6 STS + 20 RTG order with HGT. Supports sany_hgt_aracruz_2026.",
        "supports": ["sany_hgt_aracruz_2026", "hunt_infra_port_cranes"],
    },
)

# 12 energy/other_renewables — miss
# 13 energy/power_plants_grid — miss

# 14 infrastructure/port_ownership — HGT Aracruz JV greenfield terminal
A(
    {
        "id": "hgt_aracruz_jv_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "Hanseatic Global Terminals / Grupo Imetame — HGT Aracruz greenfield container terminal",
        "country": "Brazil",
        "asset": "50/50 JV established June 2026 for greenfield container terminal at Aracruz (Espírito Santo); gateway + transshipment hub on Brazil’s east coast; equipment package ordered from SANY (separate crane row); JV CAPEX USD not disclosed on opened pages",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-19.82",
        "lon": "-40.27",
        "geo_note": "Aracruz, Espírito Santo (HGT company release).",
        "evidence": "documented",
        "source_id": "hgt_aracruz_imetame_2026",
        "note": "Actors: HGT (Hapag-Lloyd / German–allied terminal arm) 50% + Grupo Imetame (Brazilian) 50% — allied coding for HGT/Hapag-Lloyd. Company HGT press. Complements sany_hgt_aracruz_2026 crane supply. Distinct from DP World Santos / APM Suape / ICTSI Rio Brasil ownership rows.",
    },
    {
        "id": "hgt_aracruz_jv_2026",
        "retrieved": "2026-10-01",
        "source_id": "hgt_aracruz_imetame_2026",
        "url": "https://www.hanseaticglobalterminals.com/en/hgt/press/HGTGrupoImetameAgreement.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "This agreement marks an important step in the development of the greenfield terminal, Hanseatic Global Terminals Aracruz, in Aracruz, Espírito Santo, Brazil. Hanseatic Global Terminals Aracruz was established in June 2026 as a 50/50 joint venture between Hanseatic Global Terminals and Grupo Imetame.",
        "note": "Opened HGT company press page.",
    },
    {
        "id": "hgt_aracruz_imetame_2026",
        "type": "company",
        "chicago": "Hanseatic Global Terminals. “Hanseatic Global Terminals, Grupo Imetame and SANY Sign Agreement of major equipment for the new terminal in Aracruz.” 2026.",
        "url": "https://www.hanseaticglobalterminals.com/en/hgt/press/HGTGrupoImetameAgreement.html",
        "annotation": "Company primary HGT–Imetame Aracruz JV + SANY equipment agreement. Supports hgt_aracruz_jv_2026 (and context for sany_hgt_aracruz_2026).",
        "supports": ["hgt_aracruz_jv_2026", "sany_hgt_aracruz_2026", "hunt_infra_port_ownership"],
    },
)

# 15 resources/lithium — miss
# 16 resources/niobium — miss
# 17 resources/graphite — miss
# 18 energy/solar — miss


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
        "hunt_res_nickel": "Cycle 20: equal budget; Atlantic UG / Jervois SMP logged prior (miss).",
        "hunt_energy_wind": "Cycle 20: equal budget; CTG Serra da Palmeira logged C18 (miss).",
        "hunt_infra_bridges_roads": "Cycle 20: equal budget; CCECC Quinto / CRBC Arequipa already logged (miss).",
        "hunt_res_balsa": "Cycle 20: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_res_copper": "Cycle 20: logged vicuna_rigi_peelp_2026.",
        "hunt_res_water": "Cycle 20: equal budget; Sacyr/Cox/Acciona/IDE/GS Inima desal set already logged (miss).",
        "hunt_infra_building_materials": "Cycle 20: equal budget; CSN Cimentos sale not closed (miss).",
        "hunt_infra_engineering_epc": "Cycle 20: equal budget; Ausenco Jervois / Worley Araxá logged prior (miss).",
        "hunt_energy_fission_smr": "Cycle 20: equal budget; Meitner/Nuclearis/CAREM/Brazil microreactor already logged (miss).",
        "hunt_latam_rail_telecom": "Cycle 20: logged alstom_santo_domingo_l2_2026.",
        "hunt_infra_port_cranes": "Cycle 20: logged sany_hgt_aracruz_2026.",
        "hunt_energy_other_renewables": "Cycle 20: equal budget; AES Andes Pampas/Cristales logged C18 (miss).",
        "hunt_br_power_equip": "Cycle 20: equal budget; thick Brazil grid subcategory — miss.",
        "hunt_infra_port_ownership": "Cycle 20: logged hgt_aracruz_jv_2026.",
        "hunt_res_lithium": "Cycle 20: equal budget; Rio Tinto Rincon financing logged C19 (miss).",
        "hunt_fenb_araxa": "Cycle 20: equal budget; St George Araxá logged C18 (miss).",
        "hunt_res_graphite": "Cycle 20: equal budget; Graphcoa Jordânia DFS CAPEX logged C19 (miss).",
        "hunt_energy_solar": "Cycle 20: equal budget; ENGIE Assú Sol logged C18 (miss).",
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
    print("Cycle 20 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
