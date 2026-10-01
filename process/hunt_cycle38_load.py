#!/usr/bin/env python3
"""Cycle 38 hunt: shuffle_seed=20261038; equal budget across 18 subcategories."""
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


# seed 20261038 order:
# rail, port_cranes, other_renewables, nickel, balsa, graphite, water,
# building_materials, lithium, solar, port_ownership, wind, bridges_roads,
# fission_smr, niobium, power_plants_grid, engineering_epc, copper

# 1 infrastructure/rail — miss (PowerChina Chancay already C36)
# 2 infrastructure/port_cranes — Kalmar 20 hybrid straddles TCP Montevideo
A(
    {
        "id": "kalmar_tcp_montevideo_straddle_2024",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Kalmar (Cargotec) — 20 hybrid straddle carriers for TCP Montevideo",
        "country": "Uruguay",
        "asset": "9 Jan 2024 Kalmar/Cargotec press: agreement with Terminal Cuenca del Plata (Katoen Natie 80% / ANP 20%) to supply 20 Kalmar hybrid straddle carriers (60 t) + Kalmar Insight; booked Q4 2023 order intake; delivery targeted Q3 2024. Part of TCP fleet renewal within terminal expansion (>USD 500m cited on Kalmar page; ownership CAPEX also logged as katoen_tcp_montevideo_455m_2021)",
        "investment_type": "equipment_order",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-34.9",
        "lon": "-56.21",
        "geo_note": "Port of Montevideo TCP.",
        "evidence": "documented",
        "source_id": "kalmar_tcp_straddle_20240109",
        "note": "Actor: Kalmar/Cargotec (Finland/Sweden — allied OEM) supplying Katoen Natie TCP. Company press. Distinct from zpmc_tcp_montevideo_sts_2026 (STS) and Portonave Kalmar ERS row.",
    },
    {
        "id": "kalmar_tcp_montevideo_straddle_2024",
        "retrieved": "2026-10-01",
        "source_id": "kalmar_tcp_straddle_20240109",
        "url": "https://www.kalmarglobal.com/news--insights/press_releases/2024/kalmar-hybrid-straddle-carriers-to/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Kalmar, part of Cargotec, has concluded an agreement with Terminal Cuenca del Plata S.A. (TCP), a mixed company between Katoen Natie (80%) and National Port Authority ANP (20%), to supply 20 Kalmar hybrid straddle carriers for deployment at Terminal Cuenca del Plata (TCP) in the Port of Montevideo, Uruguay.",
        "note": "Opened Kalmar company press 9 Jan 2024.",
    },
    {
        "id": "kalmar_tcp_straddle_20240109",
        "type": "company",
        "chicago": "Kalmar / Cargotec. “Kalmar hybrid straddle carriers to help Katoen Natie cut equipment fuel consumption and emissions at Montevideo terminal.” Press release, 9 January 2024.",
        "url": "https://www.kalmarglobal.com/news--insights/press_releases/2024/kalmar-hybrid-straddle-carriers-to/",
        "annotation": "Company order for 20 hybrid straddles at TCP Montevideo. Supports kalmar_tcp_montevideo_straddle_2024.",
        "supports": ["kalmar_tcp_montevideo_straddle_2024", "hunt_infra_port_cranes"],
    },
)

# 3 energy/other_renewables — Acciona El Romero BESS 196MW/980MWh
A(
    {
        "id": "acciona_el_romero_bess_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "allied",
        "counterpart": "ACCIONA Energía — El Romero BESS (Atacama)",
        "country": "Chile",
        "asset": "8 Jun 2026 Acciona company news: new ~1 GWh BESS integrated into El Romero PV plant (246 MWp) — 196 MW / 980 MWh, five-hour discharge; COD targeted end-2027. Follows Malgarida 1 GWh BESS (already logged). Contract USD not disclosed on opened page",
        "investment_type": "greenfield_storage",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-27.0",
        "lon": "-70.2",
        "geo_note": "El Romero PV / Atacama Desert (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "acciona_el_romero_bess_20260608",
        "note": "Actor: ACCIONA Energía (Spain) — allied. Company English release. Distinct from acciona_malgarida_bess_1gwh_2026.",
    },
    {
        "id": "acciona_el_romero_bess_2026",
        "retrieved": "2026-10-01",
        "source_id": "acciona_el_romero_bess_20260608",
        "url": "https://www.acciona.com/updates/news/acciona-energia-doubles-energy-storage-plans-chile",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The new facility, which will be integrated into El Romero photovoltaic plant (246MWp), will have a capacity of 196MW/980MWh and will be able to supply 196MW of clean energy for five consecutive hours. Commercial operations are expected to begin by the end of 2027.",
        "note": "Opened Acciona company English page 8 Jun 2026.",
    },
    {
        "id": "acciona_el_romero_bess_20260608",
        "type": "company",
        "chicago": "ACCIONA Energía. “ACCIONA Energía doubles energy storage plans in Chile.” 8 June 2026.",
        "url": "https://www.acciona.com/updates/news/acciona-energia-doubles-energy-storage-plans-chile",
        "annotation": "Company announcement of El Romero BESS 196MW/980MWh. Supports acciona_el_romero_bess_2026.",
        "supports": ["acciona_el_romero_bess_2026", "hunt_energy_other_renewables"],
    },
)

# 4–6 nickel, balsa, graphite — miss

# 7 resources/water — Antofagasta Zaldívar water pipeline ~USD 0.9bn
A(
    {
        "id": "antofagasta_zaldivar_water_900m_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Antofagasta plc — Zaldívar water pipeline and pumping system",
        "country": "Chile",
        "asset": "Q2 2026 Antofagasta production report: board-approved investment of approximately USD 0.9 billion (100% basis) over next two years for water pipeline and pumping system enabling Zaldívar to transition away from continental water from mid-2028 using reprocessed wastewater from City of Antofagasta; supports potential mine-life extension to 2051",
        "investment_type": "water_infrastructure",
        "value": "900000000",
        "currency": "USD",
        "value_usd": "900000000",
        "fx_usd": "1",
        "fx_date": "2026-06-30",
        "year": "2026",
        "status": "active",
        "lat": "-24.22",
        "lon": "-69.07",
        "geo_note": "Zaldívar mine, Antofagasta Region (company geography).",
        "evidence": "documented",
        "source_id": "antofagasta_q2_2026_zaldivar_water",
        "note": "Actor: Antofagasta plc (UK/Chile listed miner) — allied. Company Q2 2026 production report. Distinct from Acciona Collahuasi desal and Bechtel QB2 desal rows.",
    },
    {
        "id": "antofagasta_zaldivar_water_900m_2026",
        "retrieved": "2026-10-01",
        "source_id": "antofagasta_q2_2026_zaldivar_water",
        "url": "https://www.antofagasta.co.uk/investors/news/2026/q2-2026-production-report/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Zaldívar Water Supply: The Group announced an investment decision in Q2 2026 for the construction of a water pipeline and pumping system, which will enable Zaldívar to transition away from continental water from mid-2028. The planned investment of approximately $0.9 billion over the next two years (100% basis)",
        "note": "Opened Antofagasta plc Q2 2026 production report.",
    },
    {
        "id": "antofagasta_q2_2026_zaldivar_water",
        "type": "company",
        "chicago": "Antofagasta plc. “Q2 2026 Production Report.” Investor news, 2026.",
        "url": "https://www.antofagasta.co.uk/investors/news/2026/q2-2026-production-report/",
        "annotation": "Company report approving Zaldívar water supply ~USD 0.9bn. Supports antofagasta_zaldivar_water_900m_2026.",
        "supports": ["antofagasta_zaldivar_water_900m_2026", "hunt_res_water"],
    },
)

# 8–13 building, lithium, solar, port_ownership, wind, bridges — miss

# 14 energy/fission_smr — Peru SMR law + Ecuador–US civil nuclear MoU
A(
    {
        "id": "peru_smr_promotion_law_2026",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "other",
        "counterpart": "Peru Congress / IPEN — SMR promotion law",
        "country": "Peru",
        "asset": "12 Mar 2026: Congreso approves (80–0–1) Ley promoting nuclear electricity generation and installation of small modular reactors (SMR); IPEN 13 Mar notice. Creates normative framework for peaceful nuclear power / SMR deployment with MINEM–MINAM–IPEN coordination. No project CAPEX or selected vendor on opened page",
        "investment_type": "policy_framework",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-12.05",
        "lon": "-77.05",
        "geo_note": "Lima / national policy pin.",
        "evidence": "documented",
        "source_id": "ipen_peru_smr_law_20260313",
        "note": "Actor: Peruvian state (other). Official IPEN Spanish notice. Descriptive framework only — no fabricated reactor award.",
    },
    {
        "id": "peru_smr_promotion_law_2026",
        "retrieved": "2026-10-01",
        "source_id": "ipen_peru_smr_law_20260313",
        "url": "https://www.gob.pe/institucion/ipen/noticias/1365603-congreso-de-la-republica-aprueba-ley-que-promueve-la-generacion-electrica-de-origen-nuclear-y-la-instalacion-de-reactores-modulares-pequenos",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "El jueves 12 de marzo, se aprobó por mayoría la “Ley que promueve la generación eléctrica de origen nuclear y la instalación de Reactores Modulares Pequeños (SMR) en el país”",
        "note": "Opened gob.pe / IPEN Spanish notice 13 Mar 2026.",
    },
    {
        "id": "ipen_peru_smr_law_20260313",
        "type": "government",
        "chicago": "Instituto Peruano de Energía Nuclear. “Congreso de la República aprueba Ley que promueve la generación eléctrica de origen nuclear y la instalación de Reactores Modulares Pequeños.” 13 March 2026.",
        "url": "https://www.gob.pe/institucion/ipen/noticias/1365603-congreso-de-la-republica-aprueba-ley-que-promueve-la-generacion-electrica-de-origen-nuclear-y-la-instalacion-de-reactores-modulares-pequenos",
        "annotation": "Official IPEN notice of Peru SMR promotion law. Supports peru_smr_promotion_law_2026.",
        "supports": ["peru_smr_promotion_law_2026", "hunt_energy_fission_smr"],
    },
)

A(
    {
        "id": "ecuador_us_nuclear_mou_2026",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "us",
        "counterpart": "United States–Ecuador civil nuclear cooperation MoU",
        "country": "Ecuador",
        "asset": "1 Apr 2026 U.S. Department of State: Deputy Secretary Christopher Landau and Ecuador MFA Gabriela Sommerfeld sign Memorandum of Understanding Concerning Civil Nuclear Cooperation — foundation for peaceful nuclear partnership (power generation, research reactors, medical isotopes); nonproliferation standards. No CAPEX or reactor award disclosed",
        "investment_type": "bilateral_mou",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-0.18",
        "lon": "-78.47",
        "geo_note": "Quito / national cooperation pin.",
        "evidence": "documented",
        "source_id": "state_ecuador_nuclear_mou_20260401",
        "note": "Actor: United States (us) MoU with Ecuador. Official State Department release. Parallel to argentina_first_smr_2025 style cooperation row — no fabricated plant value.",
    },
    {
        "id": "ecuador_us_nuclear_mou_2026",
        "retrieved": "2026-10-01",
        "source_id": "state_ecuador_nuclear_mou_20260401",
        "url": "https://www.state.gov/releases/office-of-the-spokesperson/2026/04/united-states-and-ecuador-sign-memorandum-of-understanding-concerning-strategic-civil-nuclear-cooperation",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "On April 1, 2026, U.S. Deputy Secretary of State Christopher Landau and Minister of Foreign Affairs Gabriela Sommerfeld of the Republic of Ecuador signed a Memorandum of Understanding Concerning Civil Nuclear Cooperation to advance peaceful civil nuclear cooperation between the United States and Ecuador.",
        "note": "Opened U.S. Department of State release 1 Apr 2026.",
    },
    {
        "id": "state_ecuador_nuclear_mou_20260401",
        "type": "government",
        "chicago": "U.S. Department of State, Office of the Spokesperson. “United States and Ecuador Sign Memorandum of Understanding Concerning Strategic Civil Nuclear Cooperation.” 1 April 2026.",
        "url": "https://www.state.gov/releases/office-of-the-spokesperson/2026/04/united-states-and-ecuador-sign-memorandum-of-understanding-concerning-strategic-civil-nuclear-cooperation",
        "annotation": "Official MoU on U.S.–Ecuador civil nuclear cooperation. Supports ecuador_us_nuclear_mou_2026.",
        "supports": ["ecuador_us_nuclear_mou_2026", "hunt_energy_fission_smr"],
    },
)

# 15–18 niobium, power_plants_grid, engineering_epc, copper — miss


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {b["id"]: i for i, b in enumerate(bib) if isinstance(b, dict) and "id" in b}

    added = []
    updated = []
    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        if rid in by_id:
            rows[by_id[rid]].update({k: v for k, v in row.items() if v != ""})
            updated.append(rid)
        else:
            rows.append({k: row.get(k, "") for k in FIELDS})
            by_id[rid] = len(rows) - 1
            added.append(rid)

        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

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

    hunt_updates = {
        "hunt_latam_rail_telecom": "Cycle 38: equal budget; PowerChina Chancay rail already (miss).",
        "hunt_infra_port_cranes": "Cycle 38: logged kalmar_tcp_montevideo_straddle_2024.",
        "hunt_energy_other_renewables": "Cycle 38: logged acciona_el_romero_bess_2026.",
        "hunt_res_nickel": "Cycle 38: equal budget; PNP CAPEX / Canada ECA already (miss).",
        "hunt_res_balsa": "Cycle 38: equal budget; AIMA destination shares already (miss).",
        "hunt_res_graphite": "Cycle 38: equal budget; Graphcoa DFS / USD 8m already (miss).",
        "hunt_res_water": "Cycle 38: logged antofagasta_zaldivar_water_900m_2026.",
        "hunt_infra_building_materials": "Cycle 38: equal budget; Holcim Pacasmayo complete / VES already (miss).",
        "hunt_res_lithium": "Cycle 38: equal budget; Galan / Zijin / Posco already (miss).",
        "hunt_energy_solar": "Cycle 38: equal budget; PowerChina Mauriti / Trina already (miss).",
        "hunt_infra_port_ownership": "Cycle 38: equal budget; Katoen TCP / ICAVE already (miss).",
        "hunt_energy_wind": "Cycle 38: equal budget; Goldwind / Vestas already (miss).",
        "hunt_infra_bridges_roads": "Cycle 38: equal budget; Contreras Vicuña / Sacyr R57 already (miss).",
        "hunt_energy_fission_smr": "Cycle 38: logged peru_smr_promotion_law_2026 + ecuador_us_nuclear_mou_2026.",
        "hunt_fenb_araxa": "Cycle 38: equal budget; CBMM / St George already (miss).",
        "hunt_br_power_equip": "Cycle 38: equal budget; Hitachi / Coca Codo already (miss).",
        "hunt_infra_engineering_epc": "Cycle 38: equal budget; GES Pampas already (miss).",
        "hunt_res_copper": "Cycle 38: equal budget; Las Bambas / El Abra / Centinela already (miss).",
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
    print("Cycle 38 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 38 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
