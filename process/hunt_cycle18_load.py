#!/usr/bin/env python3
"""Cycle 18 hunt: shuffle_seed=20261018; equal budget across 18 subcategories."""
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


# seed 20261018 order:
# engineering_epc, other_renewables, nickel, balsa, power_plants_grid, solar, wind,
# building_materials, port_ownership, bridges_roads, port_cranes, water, copper, lithium,
# fission_smr, rail, graphite, niobium

# 1 infrastructure/engineering_epc — Worley feasibility technical adviser for St George Araxá
A(
    {
        "id": "worley_st_george_araxa_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "Worley Engenharia — feasibility technical adviser for St George Araxá Nb-REE (Minas Gerais)",
        "country": "Brazil",
        "asset": "Technical services agreement: engineering/project-management advice for niobium-rare earths mine development studies at Araxá (feasibility/cost studies, metallurgy/process, plant design, mine planning, tailings, procurement, construction support); delivered via Worley Engenharia Ltda / Worley Consulting Brasil",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "Araxá Project, Minas Gerais (adjacent CBMM carbonatite complex; Worley release).",
        "evidence": "documented",
        "source_id": "worley_st_george_araxa_20260507",
        "note": "Actor: Worley (Australian) — allied; client St George Mining (Australian ASX). Company 7 May 2026 insight. Non-grid mining engineering advisory (pre-FID). Distinct from worley_rincon / worley_diablillos. Complements st_george_araxa_nb_2025 ownership row.",
    },
    {
        "id": "worley_st_george_araxa_2026",
        "retrieved": "2026-10-01",
        "source_id": "worley_st_george_araxa_20260507",
        "url": "https://www.worley.com/en/insights/our-news/resources/2026/st-george-niobium-rare-earths-brazil-araxa-project",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Worley has been selected by Australian company St George Mining as feasibility technical advisor for its Araxá niobium and rare earths project in Brazil, led by Worley Consulting Brasil and delivered through Worley’s Brazilian subsidiary, Worley Engenharia Ltda. … Worley will provide strategic consulting, engineering and project management support across feasibility and cost studies, metallurgical and process engineering, mine planning, process plant design, tailings management, procurement and plant construction.",
        "note": "Opened Worley company insight 7 May 2026.",
    },
    {
        "id": "worley_st_george_araxa_20260507",
        "type": "company",
        "chicago": "Worley. “Worley to help advance St George’s niobium and rare earths project in Brazil.” 7 May 2026.",
        "url": "https://www.worley.com/en/insights/our-news/resources/2026/st-george-niobium-rare-earths-brazil-araxa-project",
        "annotation": "Company primary feasibility-adviser award for Araxá Nb-REE. Supports worley_st_george_araxa_2026.",
        "supports": ["worley_st_george_araxa_2026", "hunt_infra_engineering_epc"],
    },
)

# 2 energy/other_renewables — AES Andes Pampas + Cristales hybrid renewables + BESS
A(
    {
        "id": "aes_andes_pampas_cristales_2025",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "AES Andes — Pampas + Cristales hybrid renewables/BESS (Antofagasta)",
        "country": "Chile",
        "asset": "Construction start on Pampas (128 MW wind + 229 MW solar PV + 340 MW BESS) and Cristales (288 MW solar PV + 340 MW BESS); combined ~1,325 MW generation/storage package; company states total investment more than USD 1.1 billion; COD targeted toward 2027",
        "investment_type": "ownership_equity",
        "value": "1100000000",
        "currency": "USD",
        "value_usd": "1100000000",
        "fx_usd": "1",
        "fx_date": "2025-07-30",
        "year": "2025",
        "status": "active",
        "lat": "-25.4",
        "lon": "-70.48",
        "geo_note": "Antofagasta Region hybrid sites (AES Andes release; Taltal/Pampa approximate pin).",
        "evidence": "documented",
        "source_id": "aes_andes_pampas_cristales_20250730",
        "note": "Actor: AES Andes / AES Corporation (U.S.) — us. Company 30 Jul 2025 press: >USD 1.1bn for Pampas+Cristales with large co-located BESS. Coded other_renewables for hybrid storage-backed package (not pure solar/wind OEM). Distinct from Engie Assú Sol solar ownership row.",
    },
    {
        "id": "aes_andes_pampas_cristales_2025",
        "retrieved": "2026-10-01",
        "source_id": "aes_andes_pampas_cristales_20250730",
        "url": "https://www.aesandes.com/en/press-release/aes-andes-starts-construction-1325-mw-renewables-accelerating-energy-transition",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The Pampas project will include a wind farm with an installed capacity of 128 MW and a solar photovoltaic (PV) farm with 229 MW. The site will also feature a battery energy storage system (BESS) with a capacity of 340 MW. The Cristales project includes a 288 MW solar PV farm and a 340 MW BESS. Together, these initiatives represent a total investment of more than $1.1 billion.",
        "note": "Opened AES Andes English press release 30 Jul 2025. Stored headline >USD 1.1bn floor as 1100000000.",
    },
    {
        "id": "aes_andes_pampas_cristales_20250730",
        "type": "company",
        "chicago": "AES Andes. “AES Andes starts construction on 1,325 MW of renewables, accelerating the energy transition.” 30 July 2025.",
        "url": "https://www.aesandes.com/en/press-release/aes-andes-starts-construction-1325-mw-renewables-accelerating-energy-transition",
        "annotation": "Company primary construction-start notice for Pampas/Cristales hybrid+BESS package. Supports aes_andes_pampas_cristales_2025.",
        "supports": ["aes_andes_pampas_cristales_2025", "hunt_energy_other_renewables"],
    },
)

# 3 resources/nickel — Jervois SMP restart FID (U.S.-controlled private group)
A(
    {
        "id": "jervois_smp_restart_2025",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "us",
        "counterpart": "Jervois — São Miguel Paulista nickel-cobalt refinery restart (São Paulo)",
        "country": "Brazil",
        "asset": "FID/investment approval to restart Latin America’s only electrolytic Class 1 Ni-Co refinery; process MHP + Co hydroxide; forecast 12,000 mt/yr Ni + 2,000 mt/yr Co cathode; construction ~12 months from Jan 2026 mobilisation; ramp-up across 2027; company primary does not state CAPEX (trade press cites ~USD 130m — not entered)",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-23.5",
        "lon": "-46.45",
        "geo_note": "São Miguel Paulista district, São Paulo municipality (Jervois release).",
        "evidence": "documented",
        "source_id": "jervois_smp_fid_20251125",
        "note": "Actor: Jervois group — us (13 May 2025 company notice: recapitalised private U.S.-controlled group under Millstreet Capital). Company 25 Nov 2025 SMP restart investment approval PDF. Distinct from MMG/Anglo Barro Alto, Centaurus Jaguar, Vale Onça Puma, Atlantic Nickel. CAPEX blank (no USD on opened company PDF).",
    },
    {
        "id": "jervois_smp_restart_2025",
        "retrieved": "2026-10-01",
        "source_id": "jervois_smp_fid_20251125",
        "url": "https://jervoisglobal.com/wp-content/uploads/2025/12/SMP-investment-decision-External-vf_.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The Jervois group (“Jervois”) is pleased to announce its investment for the capital project to restart its 100% owned São Miguel Paulista (“SMP”) nickel-cobalt refinery in São Paulo, Brazil. The project will commence in December 2025, with contractor mobilization beginning in January 2026. … SMP will process mixed hydroxide precipitate (“MHP”) and cobalt hydroxide, and Jervois forecasts to produce 12,000 metric tons per year (“mt/yr”) and 2,000 mt/yr of refined nickel and cobalt metal cathode respectively.",
        "note": "Opened Jervois company PDF 25 Nov 2025. Side coding cross-checked with Jervois 13 May 2025 U.S.-controlled emergence notice.",
    },
    {
        "id": "jervois_smp_fid_20251125",
        "type": "company",
        "chicago": "Jervois. “São Miguel Paulista Restart Project Investment Approval.” 25 November 2025.",
        "url": "https://jervoisglobal.com/wp-content/uploads/2025/12/SMP-investment-decision-External-vf_.pdf",
        "annotation": "Company primary SMP restart investment approval. Supports jervois_smp_restart_2025.",
        "supports": ["jervois_smp_restart_2025", "hunt_res_nickel"],
    },
)

# 4 resources/balsa — miss (WITS years exhausted)
# 5 energy/power_plants_grid — miss (thick subcategory)

# 6 energy/solar — ENGIE Assú Sol full commercial ops
A(
    {
        "id": "engie_assu_sol_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "allied",
        "counterpart": "ENGIE Brasil — Assú Sol Photovoltaic Complex (Rio Grande do Norte)",
        "country": "Brazil",
        "asset": "Assú Sol PV complex reached 100% commercial operation 13 Feb 2026; 895 MWp / 753 MWac installed; ~229.6 average MW free-market commercial capacity; company states investment R$ 3.3 billion",
        "investment_type": "ownership_equity",
        "value": "3300000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-5.58",
        "lon": "-36.91",
        "geo_note": "Assú (Açu), Rio Grande do Norte (ENGIE release).",
        "evidence": "documented",
        "source_id": "engie_assu_sol_20260223",
        "note": "Actor: ENGIE Brasil / ENGIE (French) — allied. Company English press 23 Feb 2026. Value stored as BRL 3.3bn (no FX). Distinct from CTG Arinos Huawei inverter and AES Andes hybrid rows.",
    },
    {
        "id": "engie_assu_sol_2026",
        "retrieved": "2026-10-01",
        "source_id": "engie_assu_sol_20260223",
        "url": "https://www.engie.com.br/en/imprensa/press-releases/assu-sol-photovoltaic-complex-engies-largest-solar-energy-asset-worldwide-now-operating-at-full-commercial-capacity/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Built by ENGIE Brasil, the Assú Sol Photovoltaic Complex in Assú (RN) began full commercial operations on February 13 … At an investment worth R$ 3.3 billion and an installed capacity of 895 MWp (753 MWac) and having 229,6 average MW of commercial capacity totally earmarked to the Free Market Environment …",
        "note": "Opened ENGIE Brasil English press release 23 Feb 2026.",
    },
    {
        "id": "engie_assu_sol_20260223",
        "type": "company",
        "chicago": "ENGIE Brasil. “Assú Sol Photovoltaic Complex, ENGIE’s largest solar energy asset worldwide, now operating at full commercial capacity.” 23 February 2026.",
        "url": "https://www.engie.com.br/en/imprensa/press-releases/assu-sol-photovoltaic-complex-engies-largest-solar-energy-asset-worldwide-now-operating-at-full-commercial-capacity/",
        "annotation": "Company primary full commercial operation notice for Assú Sol. Supports engie_assu_sol_2026.",
        "supports": ["engie_assu_sol_2026", "hunt_energy_solar"],
    },
)

# 7 energy/wind — CTG Serra da Palmeira 648 MW (Goldwind turbines; NDB financing)
A(
    {
        "id": "ctg_serra_da_palmeira_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "prc",
        "counterpart": "China Three Gorges Brasil — Serra da Palmeira 648 MW wind (Paraíba)",
        "country": "Brazil",
        "asset": "648 MW onshore wind project (WTGs imported from China; NDB page names Goldwind Science & Technology as turbine supplier) + 34.5/500 kV substation and ~75 km 500 kV line to Campina Grande III; NDB financing approval 17 Sep 2025; total project cost BRL 4,327 million (NDB public summary)",
        "investment_type": "ownership_equity",
        "value": "4327000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-7.12",
        "lon": "-35.88",
        "geo_note": "Serra da Palmeira wind project, Paraíba State (NDB project page; approximate).",
        "evidence": "documented",
        "source_id": "ndb_serra_da_palmeira_2025",
        "note": "Actor: CTG Brasil / China Three Gorges — prc. NDB project page + public disclosure PDF (financing approval 17 Sep 2025). Value = total project cost BRL 4,327m from NDB summary (not only NDB loan tranche). Distinct from Goldwind Sento Sé / Touros OEM-supply rows (this is CTG ownership with Goldwind turbines).",
    },
    {
        "id": "ctg_serra_da_palmeira_2025",
        "retrieved": "2026-10-01",
        "source_id": "ndb_serra_da_palmeira_2025",
        "url": "https://www.ndb.int/project/serra-da-palmeira-wind-power-project/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "NDB will finance the construction of the Serra da Palmeira power project, a 648-MW wind power project in the State of Paraíba, Brazil. … The Project procured wind turbine generators produced by Goldwind Science & Technology Limited. … NDB RMB 1,400 million (BRL 1,072 million); Other Sources BRL 3,255 million.",
        "note": "Opened NDB project page; total project cost BRL 4,327 million corroborated from NDB Projects Summary for Public Disclosure PDF.",
    },
    {
        "id": "ndb_serra_da_palmeira_2025",
        "type": "mdb",
        "chicago": "New Development Bank. “Serra da Palmeira Wind Power Project.” Project page / public disclosure summary. Financing approval 17 September 2025.",
        "url": "https://www.ndb.int/project/serra-da-palmeira-wind-power-project/",
        "annotation": "MDB primary project page for CTG Serra da Palmeira 648 MW wind. Supports ctg_serra_da_palmeira_2025.",
        "supports": ["ctg_serra_da_palmeira_2025", "hunt_energy_wind"],
    },
)

# 8 infrastructure/building_materials — miss (CSN Cimentos sale not closed)
# 9 infrastructure/port_ownership — miss
# 10 infrastructure/bridges_roads — miss (CCECC Quinto Puente logged C16)

# 11 infrastructure/port_cranes — ZPMC MultiRio STS (OEM named in trade press; value on Multiterminais)
A(
    {
        "id": "zpmc_multirio_sts_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — two Super Post-Panamax STS for MultiRio (Port of Rio de Janeiro)",
        "country": "Brazil",
        "asset": "Delivery Jun 2026 of two ZPMC STS quay cranes (arrived erected on Zhen Hua 15) lifting MultiRio STS fleet to seven; UNVERIFIED trade-press OEM attribution with Multiterminais stating ~R$ 110 million investment for the MultiRio pair",
        "investment_type": "equipment_supply",
        "value": "110000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-22.89",
        "lon": "-43.2",
        "geo_note": "MultiRio / Container Terminal II, Port of Rio de Janeiro (Multiterminais release).",
        "evidence": "proxy",
        "source_id": "hmt_multirio_zpmc_20260623",
        "note": "Actor: ZPMC (PRC) OEM; buyer Multiterminais MultiRio — prc crane coding. UNVERIFIED proxy: HMT News 23 Jun 2026 names ZPMC; Multiterminais 10 Jun 2026 company page states ~R$110m for MultiRio’s new portainers but does not name OEM on opened page. Distinct from ZPMC Santos Brasil / Portonave / Tecon Rio Grande rows. Value stored as BRL.",
    },
    {
        "id": "zpmc_multirio_sts_2026",
        "retrieved": "2026-10-01",
        "source_id": "hmt_multirio_zpmc_20260623",
        "url": "https://hmt-news.com/multiterminais-adds-sts-cranes-at-rio-terminal/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Multiterminais has received two new ZPMC ship-to-shore cranes for MultiRio … The ZPMC-built cranes arrived fully assembled on 10 June aboard Zhen Hua 15 … The investment is valued at about R$110 million, or $21 million.",
        "note": "Opened HMT News (trade press). Cross-check Multiterminais company page for R$110m without OEM name: https://www.multiterminais.com.br/noticias/multirio-investe-em-expansao-e-fortalece-competitividade-com-novos-porteineres",
    },
    {
        "id": "hmt_multirio_zpmc_20260623",
        "type": "press",
        "chicago": "HMT News. “Multiterminais Adds STS Cranes at Rio Terminal.” 23 June 2026.",
        "url": "https://hmt-news.com/multiterminais-adds-sts-cranes-at-rio-terminal/",
        "annotation": "Trade press naming ZPMC OEM and ~R$110m MultiRio STS package. Supports zpmc_multirio_sts_2026 (UNVERIFIED OEM vs Multiterminais primary).",
        "supports": ["zpmc_multirio_sts_2026", "hunt_infra_port_cranes"],
    },
)

# 12 resources/water — miss
# 13 resources/copper — miss
# 14 resources/lithium — miss
# 15 energy/fission_smr — miss
# 16 infrastructure/rail — miss
# 17 resources/graphite — miss

# 18 resources/niobium — St George completes Araxá Nb-REE acquisition
A(
    {
        "id": "st_george_araxa_nb_2025",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "St George Mining — 100% acquisition of Araxá niobium-REE project (Minas Gerais)",
        "country": "Brazil",
        "asset": "Completion 26 Feb 2025 of 100% acquisition of Itafos Araxá (Araxá Nb-REE project adjacent CBMM carbonatite); staged cash consideration US$21 million to Itafos plus equity securities; mine-development studies commenced",
        "investment_type": "ownership_equity",
        "value": "21000000",
        "currency": "USD",
        "value_usd": "21000000",
        "fx_usd": "1",
        "fx_date": "2025-02-26",
        "year": "2025",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "Araxá Project, Minas Gerais (St George ASX presentation / completion notice).",
        "evidence": "documented",
        "source_id": "sgq_araxa_completion_20250227",
        "note": "Actor: St George Mining (Australian ASX:SGQ) — allied. ASX investor presentation 27 Feb 2025 (completion 26 Feb): US$21m staged cash + securities. Distinct from CBMM/CMOC/Echion XNO rows and from worley_st_george_araxa_2026 engineering advisory.",
    },
    {
        "id": "st_george_araxa_nb_2025",
        "retrieved": "2026-10-01",
        "source_id": "sgq_araxa_completion_20250227",
        "url": "https://announcements.asx.com.au/asxpdf/20250227/pdf/06g19b7r1qbpf3.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The Acquisition: Niobium Dragon Pty Ltd, wholly owned subsidiary of St George, has acquired all the issued capital of Itafos Araxa Mineracao E Fertilizantes S.A (Itafos Araxa) which owns 100% of the Araxá Project. Consideration - Cash: US$21,000,000 payable by St George to Itafos in stages: US$10,000,000 … on completion (Stage 1): PAID; US$6,000,000 … 9 months after completion; US$5,000,000 … 18 months after completion.",
        "note": "Opened ASX investor presentation PDF filed with completion announcement 27 Feb 2025.",
    },
    {
        "id": "sgq_araxa_completion_20250227",
        "type": "company",
        "chicago": "St George Mining Limited. “Completion of Araxá niobium-REE Project Acquisition” (investor presentation / ASX). 27 February 2025.",
        "url": "https://announcements.asx.com.au/asxpdf/20250227/pdf/06g19b7r1qbpf3.pdf",
        "annotation": "ASX primary completion materials with staged US$21m cash consideration. Supports st_george_araxa_nb_2025.",
        "supports": ["st_george_araxa_nb_2025", "hunt_fenb_araxa"],
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
        "hunt_infra_engineering_epc": "Cycle 18: logged worley_st_george_araxa_2026.",
        "hunt_energy_other_renewables": "Cycle 18: logged aes_andes_pampas_cristales_2025.",
        "hunt_res_nickel": "Cycle 18: logged jervois_smp_restart_2025.",
        "hunt_res_balsa": "Cycle 18: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_br_power_equip": "Cycle 18: equal budget; thick subcategory — miss.",
        "hunt_energy_solar": "Cycle 18: logged engie_assu_sol_2026.",
        "hunt_energy_wind": "Cycle 18: logged ctg_serra_da_palmeira_2025.",
        "hunt_infra_building_materials": "Cycle 18: equal budget; CSN Cimentos sale not closed; Pacasmayo/Inka already logged (miss).",
        "hunt_infra_port_ownership": "Cycle 18: equal budget; APM Callao Stage 3B logged C14 (miss).",
        "hunt_infra_bridges_roads": "Cycle 18: equal budget; CCECC Quinto Puente logged C16 (miss).",
        "hunt_infra_port_cranes": "Cycle 18: logged zpmc_multirio_sts_2026.",
        "hunt_res_water": "Cycle 18: equal budget; Sacyr Coquimbo / Cox Rosarito already logged (miss).",
        "hunt_res_copper": "Cycle 18: equal budget; no new copper beyond FCX/FQM/Teck/Chinalco (miss).",
        "hunt_res_lithium": "Cycle 18: equal budget; Ganfeng LAAC convertible logged C14 (miss).",
        "hunt_energy_fission_smr": "Cycle 18: equal budget; Meitner/Nuclearis/CAREM/Brazil microreactor already logged (miss).",
        "hunt_latam_rail_telecom": "Cycle 18: equal budget; Hitachi Trívia logged C17; CCECC Colombia rail still exploratory (miss).",
        "hunt_res_graphite": "Cycle 18: equal budget; Graphcoa/South Star/Nacional already logged (miss).",
        "hunt_fenb_araxa": "Cycle 18: logged st_george_araxa_nb_2025.",
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
    print("Cycle 18 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
