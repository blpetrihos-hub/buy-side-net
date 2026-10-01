#!/usr/bin/env python3
"""Cycle 45 hunt: shuffle_seed=20261045; equal budget; U.S. side ≥1/3; thin_topup after.

Order: copper, engineering_epc, nickel, rail, bridges_roads, water, balsa,
building_materials, other_renewables, niobium, solar, port_ownership,
power_plants_grid, fission_smr, port_cranes, wind, lithium, graphite.
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
# 1–8 equal-budget misses with U.S. search noted in hunt stubs:
# copper, engineering_epc, nickel, rail, bridges_roads, water, balsa,
# building_materials
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 9 energy/other_renewables — CIP Arena BESS FID + CNE USD 236m CAPEX (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cip_arena_bess_236m_2025",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "allied",
        "counterpart": "Copenhagen Infrastructure Partners (GMF II) — Arena BESS Antofagasta",
        "country": "Chile",
        "asset": "7 Oct 2024 CIP FID / FNTP on Arena standalone BESS (220 MW / 1,100 MWh) in Antofagasta Region (Taltal / Arena substation). Chilean trade press (Electrominería, Apr 2025) reporting CNE declared the project under construction with investment USD 236 million. CIP’s first LatAm BESS; precedes cip_patache_bess_fntp_2026.",
        "investment_type": "greenfield_storage",
        "value": "236000000",
        "currency": "USD",
        "value_usd": "236000000",
        "fx_usd": "1",
        "fx_date": "2025-04-16",
        "year": "2025",
        "status": "active",
        "lat": "-25.40",
        "lon": "-70.48",
        "geo_note": "Taltal / Arena substation, Antofagasta Region (CNE/Electrominería geography; approximate pin).",
        "evidence": "documented",
        "source_id": "electromineria_arena_bess_20250416",
        "note": "Actor: CIP (Denmark) — allied. CAPEX from Electrominería citing CNE construction declaration; FID from CIP Cision 7 Oct 2024. Distinct from cip_patache_bess_fntp_2026.",
    },
    {
        "id": "cip_arena_bess_236m_2025",
        "retrieved": "2026-10-01",
        "source_id": "electromineria_arena_bess_20250416",
        "url": "https://electromineria.cl/almacenamiento-proyecto-bess-de-220-mw-1-100-mwh-es-declarado-en-construccion-por-la-cne/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "La Comisión Nacional de Energía (CNE) declaró en construcción el proyecto de almacenamiento de energía stand alone Arena BESS, perteneciente al fondo de inversión CI NMF, el cual contempla una potencia instalada de 220 MW y una capacidad de 1.100 MWh, para ubicarse en la comuna de Taltal, en la región de Antofagasta. La iniciativa considera una inversión de US$236 millones.",
        "note": "Opened Electrominería 16 Apr 2025 (CNE construction declaration + CAPEX). CIP FID corroboration: https://news.cision.com/copenhagen-infrastructure-partners-p-s/r/copenhagen-infrastructure-partners-takes-fid-and-commences-construction-on-1-100-mwh-battery-energy-storage-project-in-chile,c4357456",
    },
    {
        "id": "electromineria_arena_bess_20250416",
        "type": "press",
        "chicago": "Electrominería. “Almacenamiento: proyecto BESS, de 220 MW/1.100 MWh, es declarado en construcción por la CNE.” 16 April 2025.",
        "url": "https://electromineria.cl/almacenamiento-proyecto-bess-de-220-mw-1-100-mwh-es-declarado-en-construccion-por-la-cne/",
        "annotation": "Chilean energy press on CNE construction declaration and USD 236m Arena BESS CAPEX. Supports cip_arena_bess_236m_2025.",
        "supports": ["cip_arena_bess_236m_2025", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# 10–11, 13–15 misses: niobium, solar, power_plants_grid, fission_smr, port_cranes
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 12 infrastructure/port_ownership — SSA Marine Progreso cruise terminal (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ssa_progreso_cruise_54m_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "us",
        "counterpart": "SSA Marine México — Puerto Progreso cruise terminal Phase 2",
        "country": "Mexico",
        "asset": "Jun 2026: SSA Marine México announces private investment of US$54 million (MXN 948 million) for Phase 2 expansion of the Puerto de Altura de Progreso cruise terminal (Yucatán): berth/waterfront extension 332→450 m to use 13.3 m draft; capacity toward >1 million cruise passengers/year (from ~450k). Additional US$16 million (MXN 285 million) cited for passenger-facility modernization. Distinct from ssa_guaymas_sts_ertg_2026 / konecranes_yucatan_progreso_2026.",
        "investment_type": "brownfield_expansion",
        "value": "54000000",
        "currency": "USD",
        "value_usd": "54000000",
        "fx_usd": "1",
        "fx_date": "2026-06-24",
        "year": "2026",
        "status": "active",
        "lat": "21.33",
        "lon": "-89.68",
        "geo_note": "Puerto de Altura de Progreso, Yucatán (terminal pin).",
        "evidence": "documented",
        "source_id": "mexiconow_ssa_progreso_20260624",
        "note": "Actor: SSA Marine / Carrix (U.S.) via SSA Marine México — us. MexicoNOW 24 Jun 2026 (USD); Spanish info-transportes corroborates MXN 948m + MXN 285m.",
    },
    {
        "id": "ssa_progreso_cruise_54m_2026",
        "retrieved": "2026-10-01",
        "source_id": "mexiconow_ssa_progreso_20260624",
        "url": "https://mexico-now.com/yucatan-receives-us54-million-for-modernization/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The Puerto de Altura de Progreso in Yucatan has begun a new phase of modernization with a private investment of US$54 million from SSA Marine Mexico, aimed at expanding the cruise terminal … The second phase involves extending the terminal’s waterfront or berthing area from 332 to 450 meters. … SSA Marine Mexico announced an additional investment of US$16 million to modernize facilities and enhance the passenger experience.",
        "note": "Opened MexicoNOW 24 Jun 2026. Corroboration: https://info-transportes.com.mx/index.php/puertos-y-terminales/4892-ssa-marine-e-ip-invertiran-948-millones-en-ampliar-puerto-progreso",
    },
    {
        "id": "mexiconow_ssa_progreso_20260624",
        "type": "press",
        "chicago": "Jáquez, Noah. “Yucatan receives US$54 million for modernization.” MexicoNOW, 24 June 2026.",
        "url": "https://mexico-now.com/yucatan-receives-us54-million-for-modernization/",
        "annotation": "English trade press on SSA Marine México USD 54m Progreso cruise-terminal Phase 2. Supports ssa_progreso_cruise_54m_2026.",
        "supports": ["ssa_progreso_cruise_54m_2026", "hunt_infra_port_ownership"],
    },
)

# ---------------------------------------------------------------------------
# 16 energy/wind — AES Colombia JK1–JK2 IDB Invest proposed loan USD 150m (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "aes_jk1_jk2_idb_invest_150m_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "us",
        "counterpart": "AES Colombia / Ecopetrol — JK1–JK2 wind; IDB Invest proposed USD 150m",
        "country": "Colombia",
        "asset": "IDB Invest project 15653-01 (disclosed 11 Nov 2025; status Proposed): proposed loan of USD 150 million for AES Colombia–Ecopetrol Jemeiwaa Ka’I JK1 and JK2 wind farms totaling 259 MW, plus internal transmission, access roads, and a substation, connecting via Colectora 1. Not yet approved/signed — financing proposal disclosure.",
        "investment_type": "financing",
        "value": "150000000",
        "currency": "USD",
        "value_usd": "150000000",
        "fx_usd": "1",
        "fx_date": "2025-11-11",
        "year": "2025",
        "status": "active",
        "lat": "11.50",
        "lon": "-72.80",
        "geo_note": "La Guajira / Jemeiwaa Ka’I wind cluster geography (approximate; Colectora corridor).",
        "evidence": "documented",
        "source_id": "idb_invest_aes_jk_20251111",
        "note": "Actor: AES Colombia (AES Corp U.S. affiliate) with Ecopetrol — us. IDB Invest early disclosure. Complements aes_andes_pampas_cristales_2025 / aes_andes_solar_iii_hub_2026 Chile renewables.",
    },
    {
        "id": "aes_jk1_jk2_idb_invest_150m_2025",
        "retrieved": "2026-10-01",
        "source_id": "idb_invest_aes_jk_20251111",
        "url": "https://idbinvest.org/en/projects/aes-wind-farms-jk1-jk2-financing-colombia",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Sponsoring entity AES Colombia y Ecopetrol … Financing amount USD $ 150,000,000 … Status Proposed … The financing would cover the construction and operation of: (i) the JK1 and JK2 wind farms, with a combined installed capacity of 259 MW; (ii) their internal transmission lines and related civil works, including access roads; and (iii) a substation.",
        "note": "Opened IDB Invest project page (disclosed 11 Nov 2025).",
    },
    {
        "id": "idb_invest_aes_jk_20251111",
        "type": "official",
        "chicago": "IDB Invest. “AES Wind Farms JK1-JK2 Financing - Colombia.” Project 15653-01, disclosed 11 November 2025.",
        "url": "https://idbinvest.org/en/projects/aes-wind-farms-jk1-jk2-financing-colombia",
        "annotation": "MDB disclosure of proposed USD 150m loan for AES Colombia JK1–JK2 259 MW. Supports aes_jk1_jk2_idb_invest_150m_2025.",
        "supports": ["aes_jk1_jk2_idb_invest_150m_2025", "hunt_energy_wind"],
    },
)

# ---------------------------------------------------------------------------
# 17 resources/lithium — equal-budget miss (EXIM Black Giant / Argentina framework /
#   Albemarle TED already this session).
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 18 resources/graphite — South Star Sprott Streaming USD 4m term sheet (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "south_star_sprott_4m_term_2025",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "Sprott Streaming — indicative USD 4m loan for South Star Santa Cruz",
        "country": "Brazil",
        "asset": "26 Aug 2025: South Star Battery Metals (TSXV: STS) announces non-binding indicative term sheet with Sprott Streaming and Royalty for a USD 4,000,000 loan facility (3-year maturity) to support Santa Cruz Graphite Mine (Bahia) equipment upgrades, working capital, and ramp toward 450→1,000 tpm concentrate. Initial USD 200k tranche conditional on USD 2m equity/subordinated debt. Distinct from south_star_santa_cruz_restart_202604 / south_star_bndes_finep_select_2025.",
        "investment_type": "financing",
        "value": "4000000",
        "currency": "USD",
        "value_usd": "4000000",
        "fx_usd": "1",
        "fx_date": "2025-08-26",
        "year": "2025",
        "status": "active",
        "lat": "-15.65",
        "lon": "-39.50",
        "geo_note": "Santa Cruz Graphite Mine, southern Bahia (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "south_star_sprott_20250826",
        "note": "Actor: Sprott Streaming (Canada) to South Star (Canada) — allied. Company GlobeNewswire/OTC Markets 26 Aug 2025. Non-binding term sheet.",
    },
    {
        "id": "south_star_sprott_4m_term_2025",
        "retrieved": "2026-10-01",
        "source_id": "south_star_sprott_20250826",
        "url": "https://www.otcmarkets.com/stock/STSBF/news/South-Star-Announces-Indicative-Term-Sheet-for-US4M-Debt-Financing-for-the-Santa-Cruz-Graphite-Mine-in-Brazil-and-Appoin?id=490501",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "South Star Battery Metals Corp. … is pleased to announce that it has signed a non-binding indicative term sheet (“Term Sheet”) with Sprott Streaming and Royalty (“Sprott Streaming”) for a US$4,000,000 loan facility (“Loan”) to support the continued development of the Phase 1 Santa Cruz Graphite Mine in Brazil. The Loan has a 3-year maturity … The initial Loan tranche of US$200,000 at closing is conditional on US$2,000,000 equity or subordinated debt financing.",
        "note": "Opened OTC Markets / GlobeNewswire company release 26 Aug 2025.",
    },
    {
        "id": "south_star_sprott_20250826",
        "type": "company",
        "chicago": "South Star Battery Metals Corp. “South Star Announces Indicative Term Sheet for US$4M Debt Financing for the Santa Cruz Graphite Mine in Brazil and Appointment of New CFO.” 26 August 2025.",
        "url": "https://www.otcmarkets.com/stock/STSBF/news/South-Star-Announces-Indicative-Term-Sheet-for-US4M-Debt-Financing-for-the-Santa-Cruz-Graphite-Mine-in-Brazil-and-Appoin?id=490501",
        "annotation": "Company primary on Sprott Streaming USD 4m indicative loan for Santa Cruz. Supports south_star_sprott_4m_term_2025.",
        "supports": ["south_star_sprott_4m_term_2025", "hunt_res_graphite"],
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
        "hunt_res_copper": "Cycle 45: equal budget; Chilean Cobalt EXIM / FCX El Abra / Tía María already (miss).",
        "hunt_infra_engineering_epc": "Cycle 45: equal budget; Fluor/Bechtel/Worley already dense (miss).",
        "hunt_res_nickel": "Cycle 45: equal budget; DFC PNP / Centaurus / Atlantic UG already (miss).",
        "hunt_latam_rail_telecom": "Cycle 45: equal budget; Mota-Engil QI / CRCC already (miss).",
        "hunt_infra_bridges_roads": "Cycle 45: equal budget; CHEC/OHLA/Mota-Engil already (miss).",
        "hunt_res_water": "Cycle 45: equal budget; Aguas Pacífico USD 1.2bn just prior cycle (miss).",
        "hunt_res_balsa": "Cycle 45: equal budget; WITS/AIMA/Plantabal already dense (miss).",
        "hunt_infra_building_materials": "Cycle 45: equal budget; Holcim/Cemex already dense (miss).",
        "hunt_energy_other_renewables": "Cycle 45: logged cip_arena_bess_236m_2025 (allied; USD 236m).",
        "hunt_fenb_araxa": "Cycle 45: equal budget; Fangda/REAlloys MoUs already (miss).",
        "hunt_energy_solar": "Cycle 45: equal budget; AES Andes III / Polaris already (miss).",
        "hunt_infra_port_ownership": "Cycle 45: logged ssa_progreso_cruise_54m_2026 (U.S.; USD 54m).",
        "hunt_br_power_equip": "Cycle 45: equal budget; GE Vernova Azulão / EXIM Guyana already (miss).",
        "hunt_energy_fission_smr": "Cycle 45: equal budget; El Salvador NCMOU / Argentina FIRST already (miss).",
        "hunt_infra_port_cranes": "Cycle 45: equal budget; SSA Guaymas / Konecranes Progreso already (miss).",
        "hunt_energy_wind": "Cycle 45: logged aes_jk1_jk2_idb_invest_150m_2025 (U.S.; proposed USD 150m).",
        "hunt_res_lithium": "Cycle 45: equal budget; EnergyX EXIM / Argentina framework already (miss).",
        "hunt_res_graphite": "Cycle 45: logged south_star_sprott_4m_term_2025 (allied; USD 4m term sheet).",
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
    print("Cycle 45 rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
