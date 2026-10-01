#!/usr/bin/env python3
"""Cycle 53 thin_topup: post-pass thinnest = niobium(20 already topped in equal pass),
building_materials(21), nickel(21)/graphite/balsa/water/fission_smr(21).
Top-up: building_materials, water, fission_smr.
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
# building_materials — Huaxin binding offer for CSN Cimentos (prc) thin_topup
# ---------------------------------------------------------------------------
A(
    {
        "id": "huaxin_csn_cimentos_bid_2026",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "prc",
        "counterpart": "Huaxin Cement — binding offer for CSN Cimentos (Brazil)",
        "country": "Brazil",
        "asset": "10 Aug 2026: Valor International reports CSN received three binding offers for its cement business — China’s Huaxin (reportedly most aggressive), a Votorantim–Cementir consortium, and Polimix; deal expected at least R$ 12 billion; Sinoma International had shown interest but did not advance to binding stage. Huaxin entered Brazil ~2025 via EMBU aggregates (logged separately). Offer stage — not a closed acquisition.",
        "investment_type": "mna_bid",
        "value": "12000000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2026-08-10",
        "year": "2026",
        "status": "active",
        "lat": "-23.55",
        "lon": "-46.63",
        "geo_note": "CSN Cimentos Brazil HQ / São Paulo metro (national cement portfolio; approximate pin).",
        "evidence": "proxy",
        "source_id": "valor_csn_cimentos_bids_20260810",
        "note": "Actor: Huaxin Cement (PRC; Holcim holds minority stake in Huaxin) — prc. UNVERIFIED proxy: Valor International 10 Aug 2026 citing sources on binding offers and ≥R$12bn expectation; not a closed SPA. Distinct from huaxin_embu_aggregates_br_2025.",
    },
    {
        "id": "huaxin_csn_cimentos_bid_2026",
        "retrieved": "2026-10-01",
        "source_id": "valor_csn_cimentos_bids_20260810",
        "url": "https://valorinternational.globo.com/business/news/2026/08/10/csn-has-three-binding-offers-for-its-cement-business-sources-say.ghtml",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "CSN, the group led by Benjamin Steinbruch, has received three binding offers for its cement business, according to information obtained by Valor. The offers came from China’s Huaxin, a consortium formed by Brazil’s Votorantim and Italy’s Cementir, and Brazilian company Polimix, sources familiar with the talks say. … The deal was expected to be closed for at least R$12 billion. Huaxin’s offer was reportedly the most aggressive, according to a source.",
        "note": "Opened Valor International CSN Cimentos binding-offers article.",
    },
    {
        "id": "valor_csn_cimentos_bids_20260810",
        "type": "press",
        "chicago": "Fontes, Stella, and Mônica Scaramuzzo. “CSN Has Three Binding Offers for Its Cement Business, Sources Say.” Valor International, 10 August 2026.",
        "url": "https://valorinternational.globo.com/business/news/2026/08/10/csn-has-three-binding-offers-for-its-cement-business-sources-say.ghtml",
        "annotation": "UNVERIFIED press on Huaxin/Votorantim–Cementir/Polimix binding offers for CSN Cimentos. Supports huaxin_csn_cimentos_bid_2026.",
        "supports": ["huaxin_csn_cimentos_bid_2026", "hunt_infra_building_materials"],
    },
)

# ---------------------------------------------------------------------------
# water — Techint SADDN first desalinated water at Radomiro Tomic (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "techint_saddn_rt_first_water_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Techint E&C — SADDN first desalinated water at Radomiro Tomic",
        "country": "Chile",
        "asset": "23 Jun 2026: Techint E&C reports arrival of desalinated water at the new Radomiro Tomic reservoir under the SADDN (Desalinated Water Supply for the Northern District) EPC for Aguas Horizonte — seawater intake, desalination plant (Antofagasta coast), >160 km pipelines and three pumping stations; design capacity up to 840 l/s with expansion potential to 1,956 l/s; milestone is construction/commissioning validation, not declared commercial COD. Distinct from techint_saddn_epc_chile award row and ide_saddn_desal_chile_2023 technology row.",
        "investment_type": "epc_commissioning",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2026-06-23",
        "year": "2026",
        "status": "active",
        "lat": "-22.10",
        "lon": "-68.92",
        "geo_note": "Radomiro Tomic mine reservoir / Codelco Northern District, Antofagasta Region (Techint release).",
        "evidence": "documented",
        "source_id": "techint_saddn_rt_20260623",
        "note": "Actor: Techint E&C (Italian/Argentine Techint Group) — allied. Company English news 23 Jun 2026; CAPEX blank (prior BOOT >USD 1bn not restated here).",
    },
    {
        "id": "techint_saddn_rt_first_water_2026",
        "retrieved": "2026-10-01",
        "source_id": "techint_saddn_rt_20260623",
        "url": "https://www.techint.com/en/news/2026/techint-ec-reaches-new-milestone-in-one-of-chile-s-largest-water-infrastructure-projects-for-mining",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The arrival of desalinated water at Radomiro Tomic marks a significant milestone for the SADDN Project, which integrates seawater intake, desalination, and more than 160 kilometers of pipelines to supply mining operations in northern Chile. … Developed under an EPC contract by Techint E&C for Aguas Horizonte, SADDN is one of the largest water infrastructure projects currently under development for the mining industry in Chile. … Once fully operational, the system will have the capacity to produce up to 840 liters per second of desalinated water, with expansion potential reaching 1,956 liters per second",
        "note": "Opened Techint SADDN Radomiro Tomic first-water release.",
    },
    {
        "id": "techint_saddn_rt_20260623",
        "type": "company",
        "chicago": "Techint Engineering & Construction. “Techint E&C Reaches New Milestone in One of Chile’s Largest Water Infrastructure Projects for Mining.” 23 June 2026.",
        "url": "https://www.techint.com/en/news/2026/techint-ec-reaches-new-milestone-in-one-of-chile-s-largest-water-infrastructure-projects-for-mining",
        "annotation": "Company primary on SADDN first desalinated water at Radomiro Tomic. Supports techint_saddn_rt_first_water_2026.",
        "supports": ["techint_saddn_rt_first_water_2026", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# fission_smr — Brazil MME–CNNC SMR dialogue Shanghai (prc) thin_topup
# ---------------------------------------------------------------------------
A(
    {
        "id": "brazil_mme_cnnc_smr_dialogue_2026",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "prc",
        "counterpart": "CNNC — Brazil MME SMR / nuclear-sector dialogue (Shanghai)",
        "country": "Brazil",
        "asset": "22 Jan 2026: Brazil Mines and Energy Minister Alexandre Silveira meets CNNC leadership in Shanghai (incl. chief economist Mingang Huang) to deepen bilateral nuclear-sector dialogue focused on advanced applications including Small Modular Reactors (SMRs), uranium fuel-cycle cooperation, and Brazil’s nuclear-sector restructuring toward completing Angra 3. No reactor EPC award or CAPEX disclosed — high-level technology/cooperation dialogue only. Distinct from CNNC Atucha Hualong proxy and Brazil microreactor CNEN rows.",
        "investment_type": "bilateral_dialogue",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2026-01-22",
        "year": "2026",
        "status": "active",
        "lat": "-22.99",
        "lon": "-44.37",
        "geo_note": "Angra dos Reis / Angra 3 nuclear complex pin (MME dialogue context cites Angra 3 completion; meeting held in Shanghai — LatAm asset pin).",
        "evidence": "proxy",
        "source_id": "brasil247_mme_cnnc_20260122",
        "note": "Actor: CNNC (PRC) with Brazil MME — prc. UNVERIFIED proxy: Brasil 247 22 Jan 2026 summarizing MME information on Shanghai CNNC SMR dialogue; no contract USD.",
    },
    {
        "id": "brazil_mme_cnnc_smr_dialogue_2026",
        "retrieved": "2026-10-01",
        "source_id": "brasil247_mme_cnnc_20260122",
        "url": "https://www.brasil247.com/sul-global/brasil-amplia-cooperacao-com-a-china-em-energia-nuclear-e-pequenos-reatores/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "O ministro de Minas e Energia, Alexandre Silveira (PSD), participou nesta quinta-feira (22), em Xangai, de uma reunião com dirigentes da China National Nuclear Corporation (CNNC) para aprofundar o diálogo bilateral sobre o desenvolvimento do setor nuclear e as aplicações de tecnologias avançadas, como os pequenos reatores modulares. O encontro reforça o interesse do Brasil em soluções capazes de diversificar a matriz energética … segundo informações do Ministério de Minas e Energia. Durante a conversa com o economista-chefe da CNNC, Mingang Huang, e outros representantes da estatal chinesa",
        "note": "Opened Brasil 247 article summarizing MME–CNNC Shanghai SMR dialogue.",
    },
    {
        "id": "brasil247_mme_cnnc_20260122",
        "type": "press",
        "chicago": "Brasil 247. “Brasil amplia cooperação com a China em energia nuclear e pequenos reatores.” 22 January 2026.",
        "url": "https://www.brasil247.com/sul-global/brasil-amplia-cooperacao-com-a-china-em-energia-nuclear-e-pequenos-reatores/",
        "annotation": "UNVERIFIED press summarizing MME on CNNC SMR dialogue in Shanghai. Supports brazil_mme_cnnc_smr_dialogue_2026.",
        "supports": ["brazil_mme_cnnc_smr_dialogue_2026", "hunt_energy_fission_smr"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
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
        "hunt_infra_building_materials": "Cycle 53 thin_topup: logged huaxin_csn_cimentos_bid_2026 (PRC; ≥R$12bn binding-offer proxy).",
        "hunt_res_water": "Cycle 53 thin_topup: logged techint_saddn_rt_first_water_2026 (allied; first water at Radomiro Tomic).",
        "hunt_energy_fission_smr": "Cycle 53 thin_topup: logged brazil_mme_cnnc_smr_dialogue_2026 (PRC; Shanghai SMR dialogue proxy).",
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
    print("Cycle 53 thin_topup rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
