#!/usr/bin/env python3
"""Cycle 41 thin-subcategory top-up (BRIEF Rotation §3).

After shuffled pass, fewest active+hunt rows: balsa (12), then tie at 14 among
graphite / fission_smr / niobium. Top-up the three: balsa, graphite, fission_smr
(half-budget each). Niobium R$3bn St George CAPEX also logged as bonus thin hit
when evidence opened in the same top-up window (counted under niobium).
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


# thin: energy/fission_smr — Peru elevated to U.S. FIRST bilateral partner (28–30 Sep 2026 Lima)
A(
    {
        "id": "peru_first_bilateral_partner_2026",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "us",
        "counterpart": "United States FIRST program — Peru bilateral partner elevation",
        "country": "Peru",
        "asset": "28–30 Sep 2026 Lima: U.S. elevates Peru to bilateral partner in FIRST (Foundational Infrastructure for Responsible Use of SMR Technology) on margins of FIRST CSC regional workshop; deeper U.S. technical exchanges, training, and specialized assistance for Peru civil nuclear / SMR evaluation. Complements peru_smr_promotion_law_2026 (domestic framework) and argentina_first_smr_2025 (LAC contributing partner).",
        "investment_type": "program_partnership",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-12.05",
        "lon": "-77.05",
        "geo_note": "Lima workshop / national partnership pin.",
        "evidence": "proxy",
        "source_id": "diario_uno_peru_first_20261001",
        "note": "Actor: United States FIRST (State Department) with Peru/IPEN — us. UNVERIFIED proxy: Diario UNO 1 Oct 2026 summarizing IPEN announcement (U.S. Embassy Peru primary returned forbidden at retrieve). Program partnership — no CAPEX.",
    },
    {
        "id": "peru_first_bilateral_partner_2026",
        "retrieved": "2026-10-01",
        "source_id": "diario_uno_peru_first_20261001",
        "url": "https://diariouno.pe/2026/10/01/ipen-destaca-incorporacion-del-peru-como-socio-bilateral-del-programa-first-de-estados-unidos-de-america/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "El Perú se incorporó como socio bilateral del Programa de Infraestructura Fundacional para el Uso Responsable de la Tecnología de Reactores Modulares Pequeños (FIRST, por sus siglas en inglés) de Estados Unidos de América … Esta nueva condición permitirá ampliar la cooperación con Estados Unidos de América mediante asistencia técnica especializada, visitas técnicas, programas de capacitación y acciones de fortalecimiento institucional y regulatorio, principalmente en torno a los reactores modulares pequeños (SMR) y microreactores.",
        "note": "Opened Diario UNO 1 Oct 2026; embassy HTML blocked at retrieve.",
    },
    {
        "id": "diario_uno_peru_first_20261001",
        "type": "press",
        "chicago": "Diario UNO. “IPEN destaca incorporación del Perú como socio bilateral del programa FIRST de Estados Unidos de América.” 1 October 2026.",
        "url": "https://diariouno.pe/2026/10/01/ipen-destaca-incorporacion-del-peru-como-socio-bilateral-del-programa-first-de-estados-unidos-de-america/",
        "annotation": "Peruvian press summarizing IPEN on Peru FIRST bilateral partner elevation. Supports peru_first_bilateral_partner_2026 (UNVERIFIED vs embassy primary).",
        "supports": ["peru_first_bilateral_partner_2026", "hunt_energy_fission_smr"],
    },
)

# thin: resources/graphite — Graphcoa cumulative ~USD 75m invested across Brazil projects (Jun 2026)
A(
    {
        "id": "graphcoa_projects_invested_75m_2026",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "Graphcoa / Appian Capital Brazil — cumulative project spend to date",
        "country": "Brazil",
        "asset": "20 Jun 2026 Diário do Comércio interview: Graphcoa executive states company has already invested approximately USD 75 million across its Brazilian graphite projects (Bahia Boa Sorte demo plant + technical studies toward Jordânia MG). Distinct from graphcoa_jordania_dfs_capex_2026 (planned full plant ~USD 120m), graphcoa_jordania_dev_8m_2026 (Jordânia development only), and graphcoa_allied_anode_offtake_2026 (offtake path).",
        "investment_type": "capex_spent",
        "value": "75000000",
        "currency": "USD",
        "value_usd": "75000000",
        "fx_usd": "1",
        "fx_date": "2026-06-20",
        "year": "2026",
        "status": "active",
        "lat": "-16.0",
        "lon": "-40.0",
        "geo_note": "Pinned between Bahia Boa Sorte / Jequitinhonha graphite province (company portfolio; approximate).",
        "evidence": "proxy",
        "source_id": "diario_comercio_graphcoa_20260620",
        "note": "Actor: Graphcoa / Appian (allied). UNVERIFIED proxy: same Diário do Comércio interview already opened for offtake row; cumulative spend figure. Not FID for Jordânia plant.",
    },
    {
        "id": "graphcoa_projects_invested_75m_2026",
        "retrieved": "2026-10-01",
        "source_id": "diario_comercio_graphcoa_20260620",
        "url": "https://diariodocomercio.com.br/economia/graphcoa-grafite-minas/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "A Graphcoa acredita que esse movimento vai acontecer e, por isso, já investiu aproximadamente US$ 75 milhões nos projetos que possui.",
        "note": "Opened Diário do Comércio 20 Jun 2026 (same family as offtake row; new spend figure).",
    },
    {
        "id": "diario_comercio_graphcoa_20260620",
        "type": "press",
        "chicago": "Diário do Comércio. “Graphcoa planeja investir R$ 700 milhões em planta de grafite no Vale do Jequitinhonha.” 20 June 2026.",
        "url": "https://diariodocomercio.com.br/economia/graphcoa-grafite-minas/",
        "annotation": "PT trade press interview with Graphcoa on Jordânia CAPEX plans, Allied Graphite offtake path, and ~USD 75m already invested. Supports graphcoa_allied_anode_offtake_2026 and graphcoa_projects_invested_75m_2026 (UNVERIFIED).",
        "supports": [
            "graphcoa_allied_anode_offtake_2026",
            "graphcoa_projects_invested_75m_2026",
            "hunt_res_graphite",
        ],
    },
)

# thin: resources/niobium — St George Araxá maintains ~R$3bn investment plan (Sep 2026)
A(
    {
        "id": "st_george_araxa_capex_brl3bn_2026",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "St George Mining Brasil — Araxá Nb-REE planned investment",
        "country": "Brazil",
        "asset": "16 Sep 2026: St George Mining Brasil DG Thiago Amaral (Rádio Imbiara / The Mining) states company maintains approximately R$ 3 billion planned investment at Araxá Nb-REE project (Minas Gerais) while advancing rare-earths processing partnership options; production targeted 2028–2030. Distinct from st_george_araxa_nb_2025 (USD 21m acquisition), st_george_araxa_raise_aud60m_2026 (A$60m placement), and st_george_araxa_permitting_2026 (licensing milestone without CAPEX).",
        "investment_type": "capex_plan",
        "value": "3000000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "Araxá Project, Minas Gerais (company geography).",
        "evidence": "proxy",
        "source_id": "the_mining_sgq_araxa_3bn_20260916",
        "note": "Actor: St George Mining (Australia) — allied. UNVERIFIED proxy: The Mining Brasil summarizing Rádio Imbiara interview. Pre-FID CAPEX plan; BRL stored without FX.",
    },
    {
        "id": "st_george_araxa_capex_brl3bn_2026",
        "retrieved": "2026-10-01",
        "source_id": "the_mining_sgq_araxa_3bn_20260916",
        "url": "https://themining.com.br/2026/09/16/projeto-araxa-mantem-quase-r-3-bilhoes-em-investimentos/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "A St George Mining Brasil mantém investimentos de aproximadamente R$ 3 bilhões no Projeto Araxá, em Minas Gerais, enquanto avança em uma parceria voltada ao processamento de terras raras no Brasil.",
        "note": "Opened The Mining Brasil 16 Sep 2026.",
    },
    {
        "id": "the_mining_sgq_araxa_3bn_20260916",
        "type": "press",
        "chicago": "The Mining Brasil. “Projeto Araxá mantém quase R$ 3 bilhões em investimentos.” 16 September 2026.",
        "url": "https://themining.com.br/2026/09/16/projeto-araxa-mantem-quase-r-3-bilhoes-em-investimentos/",
        "annotation": "PT mining press citing St George Brasil DG on ~R$3bn Araxá plan. Supports st_george_araxa_capex_brl3bn_2026 (UNVERIFIED).",
        "supports": ["st_george_araxa_capex_brl3bn_2026", "hunt_fenb_araxa"],
    },
)

# thin: resources/balsa — miss (AIMA Siemens MoU already logged in shuffled pass; no distinct new trade year/actor)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added, updated = [], []

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

    hunt_notes = {
        "hunt_energy_fission_smr": "Cycle 41 thin_topup: logged peru_first_bilateral_partner_2026.",
        "hunt_res_graphite": "Cycle 41 thin_topup: logged graphcoa_projects_invested_75m_2026.",
        "hunt_fenb_araxa": "Cycle 41 thin_topup: logged st_george_araxa_capex_brl3bn_2026.",
        "hunt_res_balsa": "Cycle 41 thin_topup: AIMA Siemens MoU already in shuffled pass; no distinct new trade year/actor (miss).",
    }
    for hid, note in hunt_notes.items():
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
    print("Cycle 41 thin_topup added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
