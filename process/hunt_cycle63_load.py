#!/usr/bin/env python3
"""Cycle 63 hunt: shuffle_seed=20261063; equal budget; U.S. ≥1/3; thin after.

Order: graphite, niobium, building_materials, water, other_renewables, bridges_roads,
engineering_epc, wind, lithium, fission_smr, nickel, port_cranes, copper,
port_ownership, rail, power_plants_grid, solar, balsa.
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
# 4 resources/water — ACCIONA/BRK Pernambuco sanitation (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "acciona_brk_pernambuco_sanitation_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "ACCIONA / BRK — Pernambuco water & sanitation concession (153 municipalities)",
        "country": "Brazil",
        "asset": "29 Apr 2026 ACCIONA release: ACCIONA and BRK sign 35-year concession for basic sanitation (water distribution and wastewater) in 153 municipalities + one district in Pernambuco; investment BRL 15.4 billion (€2.68bn stated). Serves Recife metro, Agreste, Sertão, Zona da Mata, Fernando de Noronha. Distinct from Acciona Paraná/Espírito Santo water awards.",
        "investment_type": "concession",
        "value": "15400000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-8.05",
        "lon": "-34.90",
        "geo_note": "Recife signing / Pernambuco concession geography (approximate pin).",
        "evidence": "documented",
        "source_id": "acciona_pernambuco_20260429",
        "note": "Actor: ACCIONA (Spain) with BRK — allied. CapEx BRL 15.4bn from company release; USD not converted here.",
    },
    {
        "id": "acciona_brk_pernambuco_sanitation_2026",
        "retrieved": "2026-10-01",
        "source_id": "acciona_pernambuco_20260429",
        "url": "https://www.acciona.com/updates/news/acciona-signs-sanitation-contract-153-municipalities-pernambuco-brazil",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The 35-year agreement includes an investment of BRL 15.4 billion (€2.68 billion) to expand and modernize the region’s water supply and urban sanitation infrastructure.",
        "note": "Opened ACCIONA company release on Pernambuco sanitation concession signing.",
    },
    {
        "id": "acciona_pernambuco_20260429",
        "type": "company",
        "chicago": "ACCIONA. “ACCIONA Signs Sanitation Contract for 153 Municipalities in Pernambuco (Brazil).” 29 April 2026.",
        "url": "https://www.acciona.com/updates/news/acciona-signs-sanitation-contract-153-municipalities-pernambuco-brazil",
        "annotation": "ACCIONA/BRK Pernambuco 35-year sanitation concession (BRL 15.4bn). Supports acciona_brk_pernambuco_sanitation_2026.",
        "supports": ["acciona_brk_pernambuco_sanitation_2026", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 7 infrastructure/engineering_epc — Baker Hughes Petrobras turbomachinery (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "baker_hughes_petrobras_turbomachinery_60mo_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Baker Hughes — Petrobras 60-month aeroderivative turbomachinery service (≤64 turbines)",
        "country": "Brazil",
        "asset": "18 Mar 2026 Baker Hughes release: substantial 60-month service award (signed Feb 2026 after open tender) for maintenance, repairs, and engineering advisory on up to 64 aeroderivative gas turbines (LM2500/LM6000) across ~19 FPSOs and Replan refinery (Paulínia). Delivered from Petrópolis Service Center; expansion with advanced grinding planned. Distinct from baker_hughes_petrobras_wells_santos_2026.",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-22.505",
        "lon": "-43.182",
        "geo_note": "Baker Hughes Service Center, Petrópolis, Rio de Janeiro (company geography).",
        "evidence": "documented",
        "source_id": "baker_hughes_petrobras_tm_20260318",
        "note": "Actor: Baker Hughes (NASDAQ: BKR) — us. Contract value USD not disclosed.",
    },
    {
        "id": "baker_hughes_petrobras_turbomachinery_60mo_2026",
        "retrieved": "2026-10-01",
        "source_id": "baker_hughes_petrobras_tm_20260318",
        "url": "https://investors.bakerhughes.com/news/press-releases/news-details/2026/Baker-Hughes-Petrobras-Sign-Strategic-Service-Agreement-for-Critical-Turbomachinery-Equipment/default.aspx",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "a substantial 60-month service award from Petrobras to support critical turbomachinery equipment … up to 64 aeroderivative gas turbines … across approximately 19 floating production, storage and offloading (FPSO) vessels … and at the Replan refinery in Paulínia",
        "note": "Opened Baker Hughes IR release on Petrobras turbomachinery service award.",
    },
    {
        "id": "baker_hughes_petrobras_tm_20260318",
        "type": "company",
        "chicago": "Baker Hughes. “Baker Hughes, Petrobras Sign Strategic Service Agreement for Critical Turbomachinery Equipment.” Press release, 18 March 2026.",
        "url": "https://investors.bakerhughes.com/news/press-releases/news-details/2026/Baker-Hughes-Petrobras-Sign-Strategic-Service-Agreement-for-Critical-Turbomachinery-Equipment/default.aspx",
        "annotation": "Baker Hughes 60-month Petrobras turbomachinery services (≤64 turbines). Supports baker_hughes_petrobras_turbomachinery_60mo_2026.",
        "supports": ["baker_hughes_petrobras_turbomachinery_60mo_2026", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 7 infrastructure/engineering_epc — Baker Hughes Petrobras completions (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "baker_hughes_petrobras_completions_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Baker Hughes — Petrobras multi-year integrated completions systems (deepwater)",
        "country": "Brazil",
        "asset": "20 Mar 2025 Baker Hughes release: major multi-year fully integrated completions systems contract with Petrobras after open tender — SureCONTROL Premium ICVs, SureSENS gauges, SureTREAT, Sur-Set, Orbit barrier valves, gas lift, REACH/DeepShield SSSVs, Premier packers, screens/gravel pack. Delivery from late 2025 across multiple deepwater fields. Distinct from wells Santos / turbomachinery / subsea trees rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "Multiple unnamed Petrobras deepwater fields (no single site in release).",
        "evidence": "documented",
        "source_id": "baker_hughes_petrobras_completions_20250320",
        "note": "Actor: Baker Hughes (NASDAQ: BKR) — us. Contract value USD not disclosed.",
    },
    {
        "id": "baker_hughes_petrobras_completions_2025",
        "retrieved": "2026-10-01",
        "source_id": "baker_hughes_petrobras_completions_20250320",
        "url": "https://investors.bakerhughes.com/news/press-releases/news-details/2025/Baker-Hughes-to-Provide-Fully-Integrated-Completions-for-Petrobras-Offshore-Fields-03-20-2025/default.aspx",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "a major, multi-year fully integrated completions systems contract with Petrobras. The award followed an open tender … Delivery will begin in late 2025.",
        "note": "Opened Baker Hughes IR release on Petrobras integrated completions award.",
    },
    {
        "id": "baker_hughes_petrobras_completions_20250320",
        "type": "company",
        "chicago": "Baker Hughes. “Baker Hughes to Provide Fully Integrated Completions for Petrobras’ Offshore Fields.” Press release, 20 March 2025.",
        "url": "https://investors.bakerhughes.com/news/press-releases/news-details/2025/Baker-Hughes-to-Provide-Fully-Integrated-Completions-for-Petrobras-Offshore-Fields-03-20-2025/default.aspx",
        "annotation": "Baker Hughes multi-year Petrobras integrated completions. Supports baker_hughes_petrobras_completions_2025.",
        "supports": ["baker_hughes_petrobras_completions_2025", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 7 infrastructure/engineering_epc — Baker Hughes Petrobras subsea trees (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "baker_hughes_petrobras_subsea_trees_50_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Baker Hughes — Petrobras up to 50 pre-salt standard subsea trees + services",
        "country": "Brazil",
        "asset": "29 Sep 2025 Baker Hughes release: open-tender award to supply up to 50 Petrobras pre-salt standard subsea trees plus SDUs, in-line tees, vertical connection systems, and topside control cabinets. Fields include Albacora, Jubarte, Barracuda-Caratinga, Mero, and Búzios. Procurement/manufacturing from Q3 2025. Distinct from completions / turbomachinery / wells Santos.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-22.50",
        "lon": "-40.50",
        "geo_note": "Campos/Santos Basin field cluster named in release (approximate offshore pin).",
        "evidence": "documented",
        "source_id": "baker_hughes_petrobras_trees_20250929",
        "note": "Actor: Baker Hughes (NASDAQ: BKR) — us. Contract value USD not disclosed.",
    },
    {
        "id": "baker_hughes_petrobras_subsea_trees_50_2025",
        "retrieved": "2026-10-01",
        "source_id": "baker_hughes_petrobras_trees_20250929",
        "url": "https://investors.bakerhughes.com/news/press-releases/news-details/2025/Baker-Hughes-to-Supply-Subsea-Tree-Systems-and-Associated-Services-for-Petrobras-09-29-2025/default.aspx",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "a significant award from Petrobras to supply up to 50 subsea tree systems and associated services … Albacora, Jubarte and Barracuda-Caratinga … Mero and Buzios fields",
        "note": "Opened Baker Hughes IR release on Petrobras subsea trees award.",
    },
    {
        "id": "baker_hughes_petrobras_trees_20250929",
        "type": "company",
        "chicago": "Baker Hughes. “Baker Hughes to Supply Subsea Tree Systems and Associated Services for Petrobras.” Press release, 29 September 2025.",
        "url": "https://investors.bakerhughes.com/news/press-releases/news-details/2025/Baker-Hughes-to-Supply-Subsea-Tree-Systems-and-Associated-Services-for-Petrobras-09-29-2025/default.aspx",
        "annotation": "Baker Hughes up to 50 Petrobras subsea trees. Supports baker_hughes_petrobras_subsea_trees_50_2025.",
        "supports": ["baker_hughes_petrobras_subsea_trees_50_2025", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 7 infrastructure/engineering_epc — AFRY Acelen Bahia OE/CM (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "afry_acelen_bahia_owners_eng_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "AFRY — Owner’s Engineering / Construction Management for Acelen Bahia SAF/HVO",
        "country": "Brazil",
        "asset": "6 Aug 2026 AFRY release: Owner’s Engineering and Construction Management plus supply-package delivery for Acelen Renewables greenfield biofuel plant in São Francisco do Conde, Bahia (~1 billion liters/y HVO/SAF; COD ~2029). Builds on prior AFRY conceptual/basic engineering and licensing. Distinct from honeywell_acelen_bahia_ecofining_2026.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-12.627",
        "lon": "-38.680",
        "geo_note": "São Francisco do Conde, Bahia (company geography).",
        "evidence": "documented",
        "source_id": "afry_acelen_bahia_20260806",
        "note": "Actor: AFRY (Sweden/Finland) — allied. Fee/CapEx USD not disclosed.",
    },
    {
        "id": "afry_acelen_bahia_owners_eng_2026",
        "retrieved": "2026-10-01",
        "source_id": "afry_acelen_bahia_20260806",
        "url": "https://afry.com/en/newsroom/press-releases/afry-provide-comprehensive-project-delivery-services-acelen-renewables-new-biofuel-plant-in-brazil",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "AFRY’s scope of work includes Owner’s Engineering and Construction Management services as well as ensuring timely delivery of essential supply packages. … located in the city of São Francisco do Conde, in the state of Bahia",
        "note": "Opened AFRY press release on Acelen Bahia OE/CM award.",
    },
    {
        "id": "afry_acelen_bahia_20260806",
        "type": "company",
        "chicago": "AFRY. “AFRY to Provide Comprehensive Project Delivery Services for Acelen Renewables’ New Biofuel Plant in Brazil.” Press release, 6 August 2026.",
        "url": "https://afry.com/en/newsroom/press-releases/afry-provide-comprehensive-project-delivery-services-acelen-renewables-new-biofuel-plant-in-brazil",
        "annotation": "AFRY OE/CM for Acelen Bahia SAF/HVO plant. Supports afry_acelen_bahia_owners_eng_2026.",
        "supports": ["afry_acelen_bahia_owners_eng_2026", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 16 energy/power_plants_grid — GE Vernova PREPA LM2500XPRESS (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ge_vernova_prepa_lm2500xpress_pr_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "GE Vernova — six LM2500XPRESS packages for PREPA Daguao/Jobos/Yabucoa (Genera PR)",
        "country": "Puerto Rico",
        "asset": "30 Jun 2025 GE Vernova release: order from RG Engineering for six LM2500XPRESS aeroderivative packages to modernize PREPA plants at Daguao, Jobos, and Yabucoa (operated by Genera PR). Stated ~224 MW (also notes ~244 MW total estimate); Q2 2025 booking; Hungary assembly. Distinct from ge_vernova_azulao / EXIM FOCOL TM2500.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "18.227",
        "lon": "-65.666",
        "geo_note": "Daguao plant area, eastern Puerto Rico (one of three named PREPA sites; approximate pin).",
        "evidence": "documented",
        "source_id": "ge_vernova_prepa_lm2500_20250630",
        "note": "Actor: GE Vernova (NYSE: GEV) — us. CapEx USD not disclosed; MW figures from company release.",
    },
    {
        "id": "ge_vernova_prepa_lm2500xpress_pr_2025",
        "retrieved": "2026-10-01",
        "source_id": "ge_vernova_prepa_lm2500_20250630",
        "url": "https://www.gevernova.com/news/press-releases/ge-vernova-aeroderivative-solutions-expected-improve-reliability-puerto-ricos",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "secured an order for six of its LM2500XPRESS* aeroderivative gas turbine packages from … RG Engineering (RGE) … modernize the Puerto Rico Electric Power Authority (PREPA) power plants at Daguao, Jobos, and Yabucoa",
        "note": "Opened GE Vernova company release on PREPA LM2500XPRESS order.",
    },
    {
        "id": "ge_vernova_prepa_lm2500_20250630",
        "type": "company",
        "chicago": "GE Vernova. “GE Vernova’s Aeroderivative Solutions Expected to Improve Reliability of Puerto Rico’s Electricity Supply.” Press release, 30 June 2025.",
        "url": "https://www.gevernova.com/news/press-releases/ge-vernova-aeroderivative-solutions-expected-improve-reliability-puerto-ricos",
        "annotation": "GE Vernova six LM2500XPRESS for PREPA Daguao/Jobos/Yabucoa. Supports ge_vernova_prepa_lm2500xpress_pr_2025.",
        "supports": ["ge_vernova_prepa_lm2500xpress_pr_2025", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 16 energy/power_plants_grid — State Grid Mantiqueira acquisition (prc, proxy)
# ---------------------------------------------------------------------------
A(
    {
        "id": "state_grid_mantiqueira_tx_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "prc",
        "counterpart": "State Grid Brazil Holding — acquisition of Mantiqueira Transmissão (Minas Gerais)",
        "country": "Brazil",
        "asset": "Nov 2025 State Grid Brazil Holding notes SPA for 100% of Concessionária Mantiqueira Transmissão (~1,222 km lines in Minas Gerais); CADE clearance reported Jan 2026; integration targeted 2026. Press estimates enterprise value ~R$7bn (UNVERIFIED). Distinct from State Grid NE UHV / CPFL rows.",
        "investment_type": "ownership_equity",
        "value": "7000000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-19.92",
        "lon": "-43.94",
        "geo_note": "Minas Gerais transmission corridor (approximate pin near Belo Horizonte).",
        "evidence": "proxy",
        "source_id": "cnnbrasil_state_grid_mantiqueira_20251128",
        "note": "Actor: State Grid Corporation of China via SGBH — prc. SPA confirmed in SGBH 2025 DFs; R$7bn EV is UNVERIFIED press proxy (CNN Brasil/Estadão).",
    },
    {
        "id": "state_grid_mantiqueira_tx_2025",
        "retrieved": "2026-10-01",
        "source_id": "cnnbrasil_state_grid_mantiqueira_20251128",
        "url": "https://www.cnnbrasil.com.br/economia/investimentos/state-grid-assina-contrato-para-compra-da-linha-de-transmissao-mantiqueira-2/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "O MME … cerimônia de assinatura do contrato que formaliza a compra da linha de transmissão Mantiqueira, atualmente pertencente à Quantum Participações, pela chinesa State Grid. … O negócio é estimado em R$ 7 bilhões.",
        "note": "Opened CNN Brasil Portuguese press on State Grid–Mantiqueira SPA; EV UNVERIFIED.",
    },
    {
        "id": "cnnbrasil_state_grid_mantiqueira_20251128",
        "type": "press",
        "chicago": "Monteiro, Renan. “State Grid Assina Contrato para Compra da Linha de Transmissão Mantiqueira.” CNN Brasil, 28 November 2025.",
        "url": "https://www.cnnbrasil.com.cn/economia/investimentos/state-grid-assina-contrato-para-compra-da-linha-de-transmissao-mantiqueira-2/",
        "annotation": "Press on State Grid Mantiqueira acquisition (~R$7bn UNVERIFIED EV). Supports state_grid_mantiqueira_tx_2025.",
        "supports": ["state_grid_mantiqueira_tx_2025", "hunt_br_power_equip"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    # Fix typo in CNN URL if present
    if bib_entry.get("id") == "cnnbrasil_state_grid_mantiqueira_20251128":
        bib_entry["url"] = (
            "https://www.cnnbrasil.com.br/economia/investimentos/"
            "state-grid-assina-contrato-para-compra-da-linha-de-transmissao-mantiqueira-2/"
        )
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
    # Fix URL typo in ITEMS evidence too
    for row, evidence, bib_entry in ITEMS:
        if evidence.get("source_id") == "cnnbrasil_state_grid_mantiqueira_20251128":
            evidence["url"] = (
                "https://www.cnnbrasil.com.br/economia/investimentos/"
                "state-grid-assina-contrato-para-compra-da-linha-de-transmissao-mantiqueira-2/"
            )
        if bib_entry.get("id") == "cnnbrasil_state_grid_mantiqueira_20251128":
            bib_entry["url"] = evidence["url"]

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
        "hunt_res_graphite": "Cycle 63: equal budget; Atlas Malacacheta / Graphcoa already (miss).",
        "hunt_fenb_araxa": "Cycle 63: equal budget; St George / CBMM / Boston Metal already (miss).",
        "hunt_infra_building_materials": "Cycle 63: equal budget; Holcim / Sinoma already (miss).",
        "hunt_res_water": "Cycle 63: logged acciona_brk_pernambuco_sanitation_2026 (allied).",
        "hunt_energy_other_renewables": "Cycle 63: equal budget; ClearPower / ContourGlobal / Ormat already (miss).",
        "hunt_infra_bridges_roads": "Cycle 63: equal budget; USACE Guatemala / ICA CA-9 already (miss).",
        "hunt_infra_engineering_epc": "Cycle 63: logged baker_hughes_petrobras_turbomachinery_60mo_2026 + baker_hughes_petrobras_completions_2025 + baker_hughes_petrobras_subsea_trees_50_2025 (U.S.) + afry_acelen_bahia_owners_eng_2026 (allied).",
        "hunt_energy_wind": "Cycle 63: equal budget; Vestas / Goldwind / Envision already (miss).",
        "hunt_res_lithium": "Cycle 63: equal budget; Ganfeng Exar Cauchari RIGI just prior (miss).",
        "hunt_energy_fission_smr": "Cycle 63: equal budget; Peru FIRST / USTDA LAC nuclear already (miss).",
        "hunt_res_nickel": "Cycle 63: equal budget; Jervois / Westwin / DFC Piauí already (miss).",
        "hunt_infra_port_cranes": "Cycle 63: equal budget; Liebherr / SSA Manzanillo already (miss).",
        "hunt_res_copper": "Cycle 63: equal budget; Chinalco Calatos / CMOC Cangrejos already (miss).",
        "hunt_infra_port_ownership": "Cycle 63: equal budget; SSA / COSCO Chancay already (miss).",
        "hunt_latam_rail_telecom": "Cycle 63: equal budget; EXIM Wabtec / PowerChina Chancay already (miss).",
        "hunt_br_power_equip": "Cycle 63: logged ge_vernova_prepa_lm2500xpress_pr_2025 (U.S.) + state_grid_mantiqueira_tx_2025 (PRC proxy).",
        "hunt_energy_solar": "Cycle 63: equal budget; IDB 360 Energy / POWERCHINA Conchagua already (miss).",
        "hunt_res_balsa": "Cycle 63: equal budget; AIMA / Plantabal / CoreLite already (miss).",
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
    print("Cycle 63 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
