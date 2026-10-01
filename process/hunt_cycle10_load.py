#!/usr/bin/env python3
"""Cycle 10 hunt: shuffle_seed=20261010; equal budget across 18 subcategories."""
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


# seed 20261010 order:
# rail, port_ownership, power_plants_grid, bridges_roads, graphite, wind, copper,
# water, nickel, solar, niobium, engineering_epc, building_materials, fission_smr,
# other_renewables, port_cranes, lithium, balsa

# 1 infrastructure/rail — miss (Trenes del Norte / BA Line B already logged)

# 2 infrastructure/port_ownership — APM Terminals Suape
A(
    {
        "id": "apm_suape_brazil_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "APM Terminals — new fully electrified container terminal at Port of Suape (Pernambuco)",
        "country": "Brazil",
        "asset": "New APM Terminals Suape facility; ~USD 350 million total investment; initial capacity up to 400,000 TEU/year (+55% for Suape complex); operations 2H 2026; Latin America’s first fully electrified port facility (company claim)",
        "investment_type": "ownership_equity",
        "value": "350000000",
        "currency": "USD",
        "value_usd": "350000000",
        "fx_usd": "1",
        "fx_date": "2026-03-09",
        "year": "2026",
        "status": "active",
        "lat": "-8.39",
        "lon": "-34.97",
        "geo_note": "Port of Suape, Pernambuco (APM Terminals Suape notices).",
        "evidence": "documented",
        "source_id": "apmt_suape_20260309",
        "note": "Actor: APM Terminals (Maersk/Denmark) — allied. Company 9 Mar 2026 Suape construction-phase release. Distinct from APM Santos BTP and Lázaro Cárdenas rows. Equipment OEM logged separately under port_cranes.",
    },
    {
        "id": "apm_suape_brazil_2026",
        "retrieved": "2026-10-01",
        "source_id": "apmt_suape_20260309",
        "url": "https://www.apmterminals.com/en/news/news-releases/2026/260309-APMTerminals-Suape-enters-final-construction-phase",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "With a total estimated investment of USD 350 million, the construction of the Suape terminal is nearing completion … initial capacity to handle up to 400,000 TEUs per year",
        "note": "Opened APM Terminals Suape final-construction-phase release.",
    },
    {
        "id": "apmt_suape_20260309",
        "type": "official",
        "chicago": "APM Terminals. “APM Terminals Suape enters final construction phase as USD 47 million in equipment arrives on site.” 9 March 2026.",
        "url": "https://www.apmterminals.com/en/news/news-releases/2026/260309-APMTerminals-Suape-enters-final-construction-phase",
        "annotation": "Company primary Suape terminal investment/progress notice. Supports apm_suape_brazil_2026.",
        "supports": ["apm_suape_brazil_2026", "hunt_infra_port_ownership"],
    },
)

# 3 energy/power_plants_grid — miss (thick)

# 4 infrastructure/bridges_roads — CHEC Fourth Bridge Panama Canal
A(
    {
        "id": "chec_fourth_bridge_panama",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "China Harbour Engineering Company (CHEC) — Fourth Bridge over the Panama Canal",
        "country": "Panama",
        "asset": "Three-span steel-concrete composite cable-stayed main bridge 965 m (240+485+240 m); H-shaped main tower ~186 m; 75 m navigation clearance; deck width 36.87 m; project in progress (viaducts/interchanges included)",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "8.95",
        "lon": "-79.57",
        "geo_note": "Fourth Bridge over Panama Canal, Panama City area (CHEC Americas projects).",
        "evidence": "documented",
        "source_id": "chec_americas_fourth_bridge",
        "note": "Actor: CHEC (CCCC/PRC) — prc. CHEC Americas projects page (scope; no contract USD on opened page). Distinct from CHEC Ruta 32 / Jamaica / Mar 2 rows.",
    },
    {
        "id": "chec_fourth_bridge_panama",
        "retrieved": "2026-10-01",
        "source_id": "chec_americas_fourth_bridge",
        "url": "https://www.checamerica.com/projects/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The Fourth Bridge over the Panama Canal … three-span steel-concrete composite cable-stayed bridge, measuring 965 meters in total length (240m + 485m + 240m). The bridge features a distinctive H-shaped main tower standing approximately 186 meters tall, with a 75-meter navigation clearance",
        "note": "Opened CHEC Americas projects page Fourth Bridge entry.",
    },
    {
        "id": "chec_americas_fourth_bridge",
        "type": "official",
        "chicago": "CHEC Americas. “Projects” (Fourth Bridge over the Panama Canal entry). Accessed 1 October 2026.",
        "url": "https://www.checamerica.com/projects/",
        "annotation": "Company project listing for Fourth Bridge. Supports chec_fourth_bridge_panama.",
        "supports": ["chec_fourth_bridge_panama", "hunt_infra_bridges_roads"],
    },
)

# 5 resources/graphite — Graphcoa Jordânia MG
A(
    {
        "id": "graphcoa_jordania_mg",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "Graphcoa (Appian Capital Brazil) — Projeto Grafite Jordânia Área C, Minas Gerais",
        "country": "Brazil",
        "asset": "Integrated natural-graphite mine + concentrator at Jordânia (Jequitinhonha Valley); ~53,000 t/year concentrate capacity; DFS stage; designed for battery-chain feed (distinct from Bahia Boa Sorte)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-15.9",
        "lon": "-40.18",
        "geo_note": "Jordânia municipality, Minas Gerais (Graphcoa project page).",
        "evidence": "documented",
        "source_id": "graphcoa_jordania_area_c",
        "note": "Actor: Graphcoa / Appian Capital Brazil (UK PE) — allied. Company Área C project page. No FID USD on opened page (press cites ~USD 120m / R$621m — not entered). Distinct from graphcoa_boa_sorte_bahia_2024 and Urbix JDA.",
    },
    {
        "id": "graphcoa_jordania_mg",
        "retrieved": "2026-10-01",
        "source_id": "graphcoa_jordania_area_c",
        "url": "https://graphcoa.com/area-c-grafite-jordania",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "O projeto “Grafite Jordania – Área C”, localizado no município de Jordânia (MG) … operação integrada de mineração e beneficiamento de grafite natural, com capacidade estimada de produção de aproximadamente 53 mil toneladas de concentrado por ano",
        "note": "Opened Graphcoa Jordânia Área C project page.",
    },
    {
        "id": "graphcoa_jordania_area_c",
        "type": "official",
        "chicago": "Graphcoa. “Área C – Grafite Jordânia.” Company project page. Accessed 1 October 2026.",
        "url": "https://graphcoa.com/area-c-grafite-jordania",
        "annotation": "Company primary Jordânia graphite project description. Supports graphcoa_jordania_mg.",
        "supports": ["graphcoa_jordania_mg", "hunt_res_graphite"],
    },
)

# 6 energy/wind — miss
# 7 resources/copper — First Quantum Taca Taca Argentina
A(
    {
        "id": "fqm_taca_taca_argentina_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "allied",
        "counterpart": "First Quantum Minerals — Taca Taca copper-gold-molybdenum project (Argentina)",
        "country": "Argentina",
        "asset": "Open-pit project with initial 40 Mtpa processing expanding to 60 Mtpa from year 5; NI 43-101 technical report filed Feb 2026; ESIA and RIGI application advancing; sanction decision pending",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-24.6",
        "lon": "-67.7",
        "geo_note": "Taca Taca project, Salta Province area (First Quantum technical report).",
        "evidence": "documented",
        "source_id": "fqm_taca_taca_202602",
        "note": "Actor: First Quantum Minerals (Canada) — allied. Company 43-101 filing release Feb 2026. Distinct from FCX/MMG/Codelco/Teck copper rows. No sanction USD entered.",
    },
    {
        "id": "fqm_taca_taca_argentina_2026",
        "retrieved": "2026-10-01",
        "source_id": "fqm_taca_taca_202602",
        "url": "https://www.first-quantum.com/wp-content/uploads/2026/02/NR-26-06-First-Quantum-Files-Taca-Taca-43-101-Technical-Report-FINAL.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The findings of the Report support the development of Taca Taca as an open pit mine with an initial processing capacity of 40 million tonnes per annum (“Mtpa”) with an expansion to 60 Mtpa commencing in the fifth year of operation. … ESIA in the first half of 2026 and an application to the Argentina Incentive Regime for Large Investments (“RIGI”).",
        "note": "Opened First Quantum Taca Taca 43-101 technical-report news PDF.",
    },
    {
        "id": "fqm_taca_taca_202602",
        "type": "official",
        "chicago": "First Quantum Minerals Ltd. “First Quantum Files Taca Taca 43-101 Technical Report” (NR 26-06). February 2026.",
        "url": "https://www.first-quantum.com/wp-content/uploads/2026/02/NR-26-06-First-Quantum-Files-Taca-Taca-43-101-Technical-Report-FINAL.pdf",
        "annotation": "Company primary Taca Taca technical-report filing notice. Supports fqm_taca_taca_argentina_2026.",
        "supports": ["fqm_taca_taca_argentina_2026", "hunt_res_copper"],
    },
)

# 8 resources/water — miss
# 9 resources/nickel — miss
# 10 energy/solar — miss

# 11 resources/niobium — CMOC Catalão 2025 record production
A(
    {
        "id": "cmoc_catalao_nb_prod_2025",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "prc",
        "counterpart": "CMOC Brasil — NML Catalão niobium mine 2025 production record",
        "country": "Brazil",
        "asset": "2025 niobium production 10,348 tonnes (record); phosphate 1.21 Mt; CMOC Brazil revenue RMB 7.693 billion (+17.61% YoY)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-18.17",
        "lon": "-47.95",
        "geo_note": "Catalão, Goiás (CMOC Brazil operations page).",
        "evidence": "documented",
        "source_id": "cmoc_brazil_nb_p_page",
        "note": "Actor: CMOC Group (PRC) 100% — prc. Company Brazil Nb/P business page updating 2025 output. Complements cmoc_catalao_niobium_br presence row with explicit 2025 production year.",
    },
    {
        "id": "cmoc_catalao_nb_prod_2025",
        "retrieved": "2026-10-01",
        "source_id": "cmoc_brazil_nb_p_page",
        "url": "https://en.cmoc.com/html/Business/BRA-Nb-P/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "In 2025, CMOC Brazil achieved record-high production of both niobium and phosphate fertilizers, reaching 10,348 tonnes and 1.21 million tonnes respectively, while generating RMB7.693 billion in revenue, up 17.61% YoY. … Production in 2025 Nb 10,348 tonnes",
        "note": "Opened CMOC English Brazil niobium/phosphate business page.",
    },
    {
        "id": "cmoc_brazil_nb_p_page",
        "type": "official",
        "chicago": "CMOC Group Limited. “Brazil - niobium and phosphate.” Company business page. Accessed 1 October 2026.",
        "url": "https://en.cmoc.com/html/Business/BRA-Nb-P/",
        "annotation": "Company primary 2025 Catalão niobium production disclosure. Supports cmoc_catalao_nb_prod_2025.",
        "supports": ["cmoc_catalao_nb_prod_2025", "hunt_fenb_araxa"],
    },
)

# 12 infrastructure/engineering_epc — miss
# 13 infrastructure/building_materials — miss
# 14 energy/fission_smr — miss
# 15 energy/other_renewables — miss

# 16 infrastructure/port_cranes — Sany equipment for APM Suape
A(
    {
        "id": "sany_apmt_suape_sts_rtg_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "Sany Marine — 2 remote STS + 7 remote electric RTGs (+ other electric yard gear) for APM Terminals Suape",
        "country": "Brazil",
        "asset": "USD 47 million fully electrified equipment package delivered Mar 2026 incl. 2 STS (70 m outreach) and 7 RTGs for remote operation; part of Suape terminal readiness for 2H 2026 start",
        "investment_type": "equipment_supply",
        "value": "47000000",
        "currency": "USD",
        "value_usd": "47000000",
        "fx_usd": "1",
        "fx_date": "2026-03-09",
        "year": "2026",
        "status": "active",
        "lat": "-8.39",
        "lon": "-34.97",
        "geo_note": "APM Terminals Suape, Pernambuco (APM equipment arrival release).",
        "evidence": "documented",
        "source_id": "apmt_suape_sany_20240605",
        "note": "Actor: Sany (PRC) equipment to APM Terminals — prc. APM 5 Jun 2024 names Sany package; APM 9 Mar 2026 arrival release states USD 47m for delivered electrified equipment. Distinct from ZPMC/Konecranes crane rows.",
    },
    {
        "id": "sany_apmt_suape_sts_rtg_2026",
        "retrieved": "2026-10-01",
        "source_id": "apmt_suape_sany_20240605",
        "url": "https://www.apmterminals.com/en/suape/news/news/2024/240605-apm-terminals-ramps-up-capacity",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Sany will deliver 2 remotely operated ship-to-shore cranes, 7 remote controlled rubber tyred gantry cranes, 2 electric reach stackers, 2 electric empty container handlers, 1 electric forklift and 14 electric terminal tractors for APM Terminals Suape.",
        "note": "Opened APM Terminals June 2024 Sany Suape equipment agreement; USD 47m corroborated on Mar 2026 arrival release.",
    },
    {
        "id": "apmt_suape_sany_20240605",
        "type": "official",
        "chicago": "APM Terminals. “APM Terminals ramps up capacity with agreements for 240 pieces of container handling equipment.” 5 June 2024.",
        "url": "https://www.apmterminals.com/en/suape/news/news/2024/240605-apm-terminals-ramps-up-capacity",
        "annotation": "Company primary Sany Suape crane/equipment agreement. Supports sany_apmt_suape_sts_rtg_2026 (USD 47m on companion Mar 2026 arrival release).",
        "supports": ["sany_apmt_suape_sts_rtg_2026", "hunt_infra_port_cranes"],
    },
)

# 17 resources/lithium — Rio Tinto Salares Altoandinos preferred partner
A(
    {
        "id": "rio_altoandinos_enami_2025",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "Rio Tinto (51% proposed) / ENAMI (49%) — Salares Altoandinos lithium project preferred partnership, Chile",
        "country": "Chile",
        "asset": "ENAMI selected Rio Tinto as preferred partner for Salares Altoandinos (Atacama region); proposed 51/49 ownership; ~USD 425m cash and non-cash contributions incl. DLE technology; binding agreements pending",
        "investment_type": "ownership_equity",
        "value": "425000000",
        "currency": "USD",
        "value_usd": "425000000",
        "fx_usd": "1",
        "fx_date": "2025-05-23",
        "year": "2025",
        "status": "active",
        "lat": "-26.5",
        "lon": "-69.3",
        "geo_note": "Salares Altoandinos, Atacama region (Rio Tinto release).",
        "evidence": "documented",
        "source_id": "rio_altoandinos_20250523",
        "note": "Actor: Rio Tinto (UK/Australia) — allied. Company 23 May 2025 preferred-partner release. Distinct from Rio Rincon Argentina and Codelco–SQM NovaAndino. Value is stated contribution package, not closed purchase price.",
    },
    {
        "id": "rio_altoandinos_enami_2025",
        "retrieved": "2026-10-01",
        "source_id": "rio_altoandinos_20250523",
        "url": "https://www.riotinto.com/en/news/releases/2025/rio-tinto-confirmed-as-preferred-partner-on-world-class-salares-altoandinos-lithium-project",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Rio Tinto has today been confirmed as the preferred partner for the Salares Altoandinos lithium project … Under the terms of the proposal, Rio Tinto would acquire an initial 51% stake … ENAMI holding the remaining 49%. … Rio Tinto will provide estimated $425m in cash and non-cash contributions including its Direct Lithium Extraction (DLE) Technology.",
        "note": "Opened Rio Tinto Altoandinos preferred-partner release.",
    },
    {
        "id": "rio_altoandinos_20250523",
        "type": "official",
        "chicago": "Rio Tinto. “Rio Tinto confirmed as preferred partner on world-class Salares Altoandinos lithium project.” 23 May 2025.",
        "url": "https://www.riotinto.com/en/news/releases/2025/rio-tinto-confirmed-as-preferred-partner-on-world-class-salares-altoandinos-lithium-project",
        "annotation": "Company primary ENAMI preferred-partner announcement. Supports rio_altoandinos_enami_2025.",
        "supports": ["rio_altoandinos_enami_2025", "hunt_res_lithium"],
    },
)

# 18 resources/balsa — miss


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
        "hunt_latam_rail_telecom": "Cycle 10: equal budget; Trenes del Norte / BA Line B already logged — miss.",
        "hunt_infra_port_ownership": "Cycle 10: logged apm_suape_brazil_2026.",
        "hunt_br_power_equip": "Cycle 10: equal budget; thick subcategory — miss.",
        "hunt_infra_bridges_roads": "Cycle 10: logged chec_fourth_bridge_panama.",
        "hunt_res_graphite": "Cycle 10: logged graphcoa_jordania_mg.",
        "hunt_energy_wind": "Cycle 10: equal budget; no new OEM award beyond Vestas/Goldwind/Nordex/Envision (miss).",
        "hunt_res_copper": "Cycle 10: logged fqm_taca_taca_argentina_2026.",
        "hunt_res_water": "Cycle 10: equal budget; no new desal beyond IDE/Acciona/GS Inima set (miss).",
        "hunt_res_nickel": "Cycle 10: equal budget; no distinct new Ni beyond MMG/Anglo/Vale/Centaurus/Atlantic/BRN DFC (miss).",
        "hunt_energy_solar": "Cycle 10: equal budget; no new solar beyond existing thick set (miss).",
        "hunt_fenb_araxa": "Cycle 10: logged cmoc_catalao_nb_prod_2025.",
        "hunt_infra_engineering_epc": "Cycle 10: equal budget; no new non-grid EPC beyond Acciona/Bechtel/Hatch/Techint/Worley set (miss).",
        "hunt_infra_building_materials": "Cycle 10: equal budget; no new cement/aggregates beyond Holcim/Huaxin/Cemex/Carmeuse (miss).",
        "hunt_energy_fission_smr": "Cycle 10: equal budget; no new SMR beyond CAREM/Meitner/FIRST/Brazil microreactor (miss).",
        "hunt_energy_other_renewables": "Cycle 10: equal budget; no new geothermal/hydro beyond JICA/PowerChina/LaGeo set (miss).",
        "hunt_infra_port_cranes": "Cycle 10: logged sany_apmt_suape_sts_rtg_2026.",
        "hunt_res_lithium": "Cycle 10: logged rio_altoandinos_enami_2025.",
        "hunt_res_balsa": "Cycle 10: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
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
    print("Cycle 10 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
