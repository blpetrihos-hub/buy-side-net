#!/usr/bin/env python3
"""Cycle 19 hunt: shuffle_seed=20261019; equal budget across 18 subcategories."""
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


# seed 20261019 order:
# solar, port_cranes, wind, power_plants_grid, fission_smr, balsa, nickel, other_renewables,
# rail, engineering_epc, port_ownership, water, building_materials, copper, lithium, niobium,
# bridges_roads, graphite

# 1 energy/solar — miss (Assú Sol logged C18)
# 2 infrastructure/port_cranes — miss (MultiRio logged C18)
# 3 energy/wind — miss (CTG Serra da Palmeira logged C18)

# 4 energy/power_plants_grid — Nari Technology Chilquinta Agua Santa award (PRC)
A(
    {
        "id": "nari_chilquinta_agua_santa_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "prc",
        "counterpart": "Nari Technology — Chilquinta Agua Santa–Laguna Verde line sectioning (Valparaíso)",
        "country": "Chile",
        "asset": "Chilquinta Transmisión award to Nari Technology to section circuit Nº1 of 2×110 kV Agua Santa–Laguna Verde at S/E Los Placeres and increase capacity of 2×110 kV Tap Placeres–Los Placeres; UNVERIFIED press associated investment US$6.3 million",
        "investment_type": "epc",
        "value": "6300000",
        "currency": "USD",
        "value_usd": "6300000",
        "fx_usd": "1",
        "fx_date": "2026-05-25",
        "year": "2026",
        "status": "active",
        "lat": "-33.05",
        "lon": "-71.6",
        "geo_note": "Los Placeres / Agua Santa corridor, Valparaíso Region (BNamericas citing CEN auction notice).",
        "evidence": "proxy",
        "source_id": "bnamericas_nari_chilquinta_20260525",
        "note": "Actor: Nari Technology (PRC) — prc; asset owner Chilquinta. UNVERIFIED proxy: BNamericas 25 May 2026 summarizing CEN auction result notice. Distinct from Siemens/GE/Hitachi/PowerChina Parinas grid rows.",
    },
    {
        "id": "nari_chilquinta_agua_santa_2026",
        "retrieved": "2026-10-01",
        "source_id": "bnamericas_nari_chilquinta_20260525",
        "url": "https://www.bnamericas.com/en/news/transelec-chilquinta-transmision-award-chile-grid-expansion-work",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Meanwhile, Chilquinta awarded to Nari Technology a US$6.3mn project to section a circuit of the 2x110kV Agua Santa-Laguna Verde line and increase the capacity of the 2x110kV Tap Placeres-Los Placeres line.",
        "note": "Opened BNamericas English report citing CEN auction result notice (primary CEN PDF not opened this cycle).",
    },
    {
        "id": "bnamericas_nari_chilquinta_20260525",
        "type": "press",
        "chicago": "BNamericas. “Transelec, Chilquinta Transmisión award Chile grid expansion work.” 25 May 2026.",
        "url": "https://www.bnamericas.com/en/news/transelec-chilquinta-transmision-award-chile-grid-expansion-work",
        "annotation": "Trade press on Chilquinta award to Nari Technology (US$6.3m). Supports nari_chilquinta_agua_santa_2026 (UNVERIFIED).",
        "supports": ["nari_chilquinta_agua_santa_2026", "hunt_cl_power_equip"],
    },
)

# 5 energy/fission_smr — miss
# 6 resources/balsa — miss

# 7 resources/nickel — Atlantic Nickel Santa Rita underground expansion CAPEX
A(
    {
        "id": "atlantic_nickel_ug_capex_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "Atlantic Nickel (Appian) — Santa Rita underground expansion (Bahia)",
        "country": "Brazil",
        "asset": "Projeto Underground at Santa Rita open-pit NiS mine toward underground mining; inaugural South Portal blast 27 Mar 2026; >300 m of tunnels; first UG ore targeted end-2028; UNVERIFIED press cites ~R$ 3.3 billion investment and >30-year life extension",
        "investment_type": "ownership_equity",
        "value": "3300000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-11.0",
        "lon": "-39.5",
        "geo_note": "Santa Rita / Itagibá area, Bahia (Exame citing Appian/Atlantic Nickel).",
        "evidence": "proxy",
        "source_id": "exame_appian_atlantic_ug_20260825",
        "note": "Actor: Atlantic Nickel / Appian Capital Brazil (UK PE) — allied. UNVERIFIED proxy: Exame 25 Aug 2026 interview citing R$3.3bn UG capex and Mar 2026 portal blast. Distinct from atlantic_nickel_santa_rita_br presence and IFC/Appian fund rows. Value stored as BRL.",
    },
    {
        "id": "atlantic_nickel_ug_capex_2026",
        "retrieved": "2026-10-01",
        "source_id": "exame_appian_atlantic_ug_20260825",
        "url": "https://exame.com/invest/mercados/appian-vai-investir-ate-r-700-milhoes-em-grafite-em-mg-com-demanda-de-carros-eletricos/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "O Projeto Underground, na Mina Santa Rita, prevê investimentos de cerca de R$ 3,3 bilhões e deve estender a vida útil da operação para mais de 30 anos. … O projeto teve o desmonte inaugural para a abertura do Portal Sul em 27 de março de 2026 e já ultrapassou 300 metros de túneis construídos. A previsão é que ao final de 2028 o minério já esteja sendo produzido.",
        "note": "Opened Exame PT interview with Appian Brazil executives (company primary UG CAPEX notice not opened this cycle).",
    },
    {
        "id": "exame_appian_atlantic_ug_20260825",
        "type": "press",
        "chicago": "Exame. “Appian vai investir até R$ 700 milhões em grafite em MG com demanda de carros elétricos.” 25 August 2026.",
        "url": "https://exame.com/invest/mercados/appian-vai-investir-ate-r-700-milhoes-em-grafite-em-mg-com-demanda-de-carros-eletricos/",
        "annotation": "PT trade press interview citing Atlantic Nickel Santa Rita UG ~R$3.3bn and Graphcoa Jordânia ~R$700m. Supports atlantic_nickel_ug_capex_2026 and graphcoa_jordania_dfs_capex_2026 (UNVERIFIED).",
        "supports": [
            "atlantic_nickel_ug_capex_2026",
            "graphcoa_jordania_dfs_capex_2026",
            "hunt_res_nickel",
            "hunt_res_graphite",
        ],
    },
)

# 8 energy/other_renewables — miss
# 9 infrastructure/rail — miss

# 10 infrastructure/engineering_epc — Ausenco EPCM for Jervois SMP
A(
    {
        "id": "ausenco_jervois_smp_epcm_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "Ausenco — EPCM for Jervois São Miguel Paulista Ni-Co refinery restart",
        "country": "Brazil",
        "asset": "EPCM contract signed 30 Dec 2025; Ausenco responsible for engineering through pre-commissioning; detailed engineering/procurement underway Jan 2026 with ~50-person mobilisation (BH office + site); supports restart targeting 12 ktpy Ni + 2 ktpy Co",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.5",
        "lon": "-46.45",
        "geo_note": "São Miguel Paulista, São Paulo (International Mining citing Ausenco).",
        "evidence": "proxy",
        "source_id": "im_mining_ausenco_jervois_20260110",
        "note": "Actor: Ausenco (Australian/Canadian) — allied; client Jervois Brasil. UNVERIFIED proxy: International Mining 10 Jan 2026 (quotes Ausenco project director). Complements jervois_smp_restart_2025 ownership row. Non-grid refinery EPCM. No contract USD on opened page.",
    },
    {
        "id": "ausenco_jervois_smp_epcm_2026",
        "retrieved": "2026-10-01",
        "source_id": "im_mining_ausenco_jervois_20260110",
        "url": "https://im-mining.com/2026/01/10/ausenco-mobilises-team-to-revitalise-jervois-nickel-and-cobalt-refinery/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "The mobilisation comes after Ausenco and Jervois Brasil signed an EPCM contract on 30 December. Ausenco will be responsible for the engineering, up to pre-commissioning, of the nickel and cobalt refinery, located in the São Miguel Paulista (SMP) neighbourhood, in the eastern zone of São Paulo.",
        "note": "Opened International Mining trade press 10 Jan 2026.",
    },
    {
        "id": "im_mining_ausenco_jervois_20260110",
        "type": "press",
        "chicago": "International Mining. “Ausenco mobilises team to revitalise Jervois nickel and cobalt refinery.” 10 January 2026.",
        "url": "https://im-mining.com/2026/01/10/ausenco-mobilises-team-to-revitalise-jervois-nickel-and-cobalt-refinery/",
        "annotation": "Trade press on Ausenco–Jervois SMP EPCM signing/mobilisation. Supports ausenco_jervois_smp_epcm_2026 (UNVERIFIED).",
        "supports": ["ausenco_jervois_smp_epcm_2026", "hunt_infra_engineering_epc"],
    },
)

# 11 infrastructure/port_ownership — DP World Santos R$1.6bn expansion cycle
A(
    {
        "id": "dpworld_santos_r16bn_2025",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "DP World — Port of Santos terminal expansion cycle (R$1.6bn)",
        "country": "Brazil",
        "asset": "Approved R$1.6 billion (company cites US$296 million) investment cycle to raise Santos terminal capacity 25% to 2.1 million TEU by 2028 (from 1.7m TEU after prior R$450m phase); includes new berth/yard, gates, reefers, and equipment (4 quay cranes, 15 RTGs, 40 ITVs)",
        "investment_type": "concession_capex",
        "value": "1600000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-23.93",
        "lon": "-46.32",
        "geo_note": "DP World Santos left-bank terminal (company release).",
        "evidence": "documented",
        "source_id": "dpworld_santos_r16bn_20251202",
        "note": "Actor: DP World (UAE) — allied. Company 2 Dec 2025 Americas release. Distinct from dpworld_santos_equip_2024 (USD 50m equipment tranche). Value stored as BRL 1.6bn (company also states US$296m — not dual-entered).",
    },
    {
        "id": "dpworld_santos_r16bn_2025",
        "retrieved": "2026-10-01",
        "source_id": "dpworld_santos_r16bn_20251202",
        "url": "https://www.dpworld.com/en/news/usa/dpw-invests-over-1-billion-reais-to-expand-santos-terminal-by-25-percent",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "DP World has approved a new R$1.6 billion (US$296 million) investment cycle to further strengthen Brazil’s trade capacity and enhance terminal operations at the Port of Santos, increasing total handling capacity by 25% to 2.1 million TEUs … by 2028.",
        "note": "Opened DP World company release 2 Dec 2025.",
    },
    {
        "id": "dpworld_santos_r16bn_20251202",
        "type": "company",
        "chicago": "DP World. “DP World to invest R$1.6 billion to expand Santos Terminal by 25%.” 2 December 2025.",
        "url": "https://www.dpworld.com/en/news/usa/dpw-invests-over-1-billion-reais-to-expand-santos-terminal-by-25-percent",
        "annotation": "Company primary Santos R$1.6bn expansion-cycle approval. Supports dpworld_santos_r16bn_2025.",
        "supports": ["dpworld_santos_r16bn_2025", "hunt_infra_port_ownership"],
    },
)

# 12 resources/water — miss
# 13 infrastructure/building_materials — miss (CSN sale not closed)
# 14 resources/copper — miss

# 15 resources/lithium — Rio Tinto Rincon USD 1.175bn financing package
A(
    {
        "id": "rio_tinto_rincon_financing_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "Rio Tinto — Rincon lithium project financing package (IFC/IDB Invest/EFA/JBIC)",
        "country": "Argentina",
        "asset": "USD 1.175 billion loan package from IFC, IDB Invest, Export Finance Australia and JBIC supporting development of the USD 2.5 billion Rincon Li2CO3 expansion (~60 ktpa battery-grade; first production 2028)",
        "investment_type": "financing",
        "value": "1175000000",
        "currency": "USD",
        "value_usd": "1175000000",
        "fx_usd": "1",
        "fx_date": "2026-03-11",
        "year": "2026",
        "status": "active",
        "lat": "-24.1",
        "lon": "-66.95",
        "geo_note": "Salar de Rincón, Salta Province (Rio Tinto release).",
        "evidence": "documented",
        "source_id": "riotinto_rincon_financing_20260311",
        "note": "Actor: Rio Tinto (UK/Australia) borrower with MDB/ECA lenders — allied financing coding. Company 11 Mar 2026 release. Distinct from rio_tinto_rincon_expansion_2024 (USD 2.5bn ownership CAPEX) and worley_rincon EPC row.",
    },
    {
        "id": "rio_tinto_rincon_financing_2026",
        "retrieved": "2026-10-01",
        "source_id": "riotinto_rincon_financing_20260311",
        "url": "https://www.riotinto.com/en/news/releases/2026/rio-tinto-secures-1-175-billion-financing-package-for-rincon-lithium-project-in-argentina",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Rio Tinto has secured a $1.175 billion financing package from four international lenders to support development of the Rincon lithium project in Argentina’s Salta Province. The package comprises loans from the International Finance Corporation (IFC), IDB Invest, Export Finance Australia (EFA) and the Japan Bank for International Cooperation (JBIC).",
        "note": "Opened Rio Tinto company release 11 Mar 2026.",
    },
    {
        "id": "riotinto_rincon_financing_20260311",
        "type": "company",
        "chicago": "Rio Tinto. “Rio Tinto secures $1.175 billion financing package for Rincon lithium project in Argentina.” 11 March 2026.",
        "url": "https://www.riotinto.com/en/news/releases/2026/rio-tinto-secures-1-175-billion-financing-package-for-rincon-lithium-project-in-argentina",
        "annotation": "Company primary Rincon IFC/IDB/EFA/JBIC financing package. Supports rio_tinto_rincon_financing_2026.",
        "supports": ["rio_tinto_rincon_financing_2026", "hunt_res_lithium"],
    },
)

# 16 resources/niobium — miss
# 17 infrastructure/bridges_roads — miss (CRBC Arequipa / CCECC Quinto already logged)

# 18 resources/graphite — Graphcoa Jordânia DFS + ~R$700m CAPEX (proxy)
A(
    {
        "id": "graphcoa_jordania_dfs_capex_2026",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "Graphcoa / Appian — Jordânia graphite DFS and CAPEX estimate (Minas Gerais)",
        "country": "Brazil",
        "asset": "Definitive Feasibility Study completed for Projeto Grafite Jordânia; >50 ktpy concentrate (~95% Cg) targeting commercial ops 2H 2029; UNVERIFIED press cites ~R$ 700 million investment (executive interview)",
        "investment_type": "ownership_equity",
        "value": "700000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-15.9",
        "lon": "-40.18",
        "geo_note": "Jordânia, Jequitinhonha Valley, Minas Gerais (Exame citing Graphcoa/Appian).",
        "evidence": "proxy",
        "source_id": "exame_appian_atlantic_ug_20260825",
        "note": "Actor: Graphcoa / Appian Capital Brazil — allied. UNVERIFIED proxy: Exame 25 Aug 2026 interview (Ricardo Alves) on DFS completion and ~R$700m. Distinct from graphcoa_jordania_mg presence row (blank CAPEX) and Boa Sorte / Urbix rows. Value stored as BRL.",
    },
    {
        "id": "graphcoa_jordania_dfs_capex_2026",
        "retrieved": "2026-10-01",
        "source_id": "exame_appian_atlantic_ug_20260825",
        "url": "https://exame.com/invest/mercados/appian-vai-investir-ate-r-700-milhoes-em-grafite-em-mg-com-demanda-de-carros-eletricos/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Com investimento estimado em cerca de R$ 700 milhões, segundo o diretor executivo Ricardo Alves, a companhia desenvolve o Projeto Grafite Jordânia, da Graphcoa, no Vale do Jequitinhonha (MG). … O projeto acaba de concluir o seu Estudo de Viabilidade Definitivo (Definitive Feasibility Study – DFS) … previsão de entrar em operação comercial no segundo semestre de 2029.",
        "note": "Opened Exame PT interview; same source family as Atlantic Nickel UG row this cycle.",
    },
    {
        "id": "exame_appian_atlantic_ug_20260825",
        "type": "press",
        "chicago": "Exame. “Appian vai investir até R$ 700 milhões em grafite em MG com demanda de carros elétricos.” 25 August 2026.",
        "url": "https://exame.com/invest/mercados/appian-vai-investir-ate-r-700-milhoes-em-grafite-em-mg-com-demanda-de-carros-eletricos/",
        "annotation": "PT trade press interview citing Atlantic Nickel Santa Rita UG ~R$3.3bn and Graphcoa Jordânia ~R$700m. Supports atlantic_nickel_ug_capex_2026 and graphcoa_jordania_dfs_capex_2026 (UNVERIFIED).",
        "supports": [
            "atlantic_nickel_ug_capex_2026",
            "graphcoa_jordania_dfs_capex_2026",
            "hunt_res_nickel",
            "hunt_res_graphite",
        ],
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
        "hunt_energy_solar": "Cycle 19: equal budget; ENGIE Assú Sol logged C18 (miss).",
        "hunt_infra_port_cranes": "Cycle 19: equal budget; ZPMC MultiRio logged C18 (miss).",
        "hunt_energy_wind": "Cycle 19: equal budget; CTG Serra da Palmeira logged C18 (miss).",
        "hunt_cl_power_equip": "Cycle 19: logged nari_chilquinta_agua_santa_2026.",
        "hunt_br_power_equip": "Cycle 19: equal budget; thick Brazil grid subcategory — miss.",
        "hunt_energy_fission_smr": "Cycle 19: equal budget; Meitner/Nuclearis/CAREM/Brazil microreactor already logged (miss).",
        "hunt_res_balsa": "Cycle 19: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_res_nickel": "Cycle 19: logged atlantic_nickel_ug_capex_2026.",
        "hunt_energy_other_renewables": "Cycle 19: equal budget; AES Andes Pampas/Cristales logged C18 (miss).",
        "hunt_latam_rail_telecom": "Cycle 19: equal budget; Hitachi Trívia logged C17 (miss).",
        "hunt_infra_engineering_epc": "Cycle 19: logged ausenco_jervois_smp_epcm_2026.",
        "hunt_infra_port_ownership": "Cycle 19: logged dpworld_santos_r16bn_2025.",
        "hunt_res_water": "Cycle 19: equal budget; Sacyr/Cox/Acciona/IDE/GS Inima desal set already logged (miss).",
        "hunt_infra_building_materials": "Cycle 19: equal budget; CSN Cimentos sale not closed (miss).",
        "hunt_res_copper": "Cycle 19: equal budget; no new copper beyond FCX/FQM/Teck/Chinalco (miss).",
        "hunt_res_lithium": "Cycle 19: logged rio_tinto_rincon_financing_2026.",
        "hunt_fenb_araxa": "Cycle 19: equal budget; St George Araxá logged C18 (miss).",
        "hunt_infra_bridges_roads": "Cycle 19: equal budget; CCECC Quinto / CRBC Arequipa already logged (miss).",
        "hunt_res_graphite": "Cycle 19: logged graphcoa_jordania_dfs_capex_2026.",
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
    print("Cycle 19 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
