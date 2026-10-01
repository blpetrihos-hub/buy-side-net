#!/usr/bin/env python3
"""Cycle 54 thin_topup: post-equal thinnest = niobium/nickel/graphite/balsa (21).
Top-up: niobium (CBMM–Toshiba planned oxide plant), nickel (Millstreet SMP equity),
graphite (Sprott Santa Cruz Phase 2 stream CapEx tranche).
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
# niobium — CBMM Toshiba mixed Nb-oxide battery plant (planned) thin_topup
# ---------------------------------------------------------------------------
A(
    {
        "id": "cbmm_toshiba_nb_oxide_plant_planned_2025",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "CBMM / Toshiba — planned mixed niobium-oxide battery plant (Araxá)",
        "country": "Brazil",
        "asset": "13 Nov 2024: Diário do Comércio reports CBMM will inaugurate in early 2025 at Araxá a new industrial plant for large-scale mixed niobium oxides for batteries using technology developed with Toshiba Corporation; design capacity 1,000 tpy; plant described as in final implementation alongside the already-inaugurated Echion XNO unit. Distinct from cbmm_echion_xno_araxa_2024. Inauguration confirmation not opened this cycle — planned-plant / proxy.",
        "investment_type": "plant_planned",
        "value": "",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2024-11-13",
        "year": "2025",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "CBMM Araxá industrial complex, Minas Gerais.",
        "evidence": "proxy",
        "source_id": "diario_cbmm_toshiba_20241113",
        "note": "Actor: CBMM (Brazilian; Allied tech partner Toshiba/Japan) — allied. UNVERIFIED proxy: Diário do Comércio 13 Nov 2024 on planned early-2025 Toshiba-tech plant; distinct from logged Echion XNO inauguration.",
    },
    {
        "id": "cbmm_toshiba_nb_oxide_plant_planned_2025",
        "retrieved": "2026-10-01",
        "source_id": "diario_cbmm_toshiba_20241113",
        "url": "https://diariodocomercio.com.br/economia/cbmm-vai-inaugurar-nova-planta-industrial-de-niobio-em-2025/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "A Companhia Brasileira de Metalurgia e Mineração (CBMM) irá inaugurar no início de 2025, em Araxá, no Alto Paranaíba, uma nova planta industrial para produção em larga escala de óxidos mistos de nióbio para baterias, com uma tecnologia desenvolvida em parceria com a Toshiba Corporation. A capacidade de produção será de mil toneladas por ano (t/a).",
        "note": "Opened Diário do Comércio CBMM–Toshiba planned plant article.",
    },
    {
        "id": "diario_cbmm_toshiba_20241113",
        "type": "press",
        "chicago": "Neves, Marco Aurélio. “CBMM Vai Inaugurar Nova Planta Industrial de Nióbio em Parceria com a Toshiba em 2025.” Diário do Comércio, 13 November 2024.",
        "url": "https://diariodocomercio.com.br/economia/cbmm-vai-inaugurar-nova-planta-industrial-de-niobio-em-2025/",
        "annotation": "UNVERIFIED PT press on planned CBMM–Toshiba 1,000 tpy Nb-oxide battery plant at Araxá. Supports cbmm_toshiba_nb_oxide_plant_planned_2025.",
        "supports": ["cbmm_toshiba_nb_oxide_plant_planned_2025", "hunt_fenb_araxa"],
    },
)

# ---------------------------------------------------------------------------
# nickel — Millstreet USD 70m equity for Jervois SMP restart thin_topup
# ---------------------------------------------------------------------------
A(
    {
        "id": "jervois_millstreet_smp_equity_70m_2025",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "us",
        "counterpart": "Millstreet Capital — USD 70m equity commitment for Jervois SMP restart",
        "country": "Brazil",
        "asset": "2 Jan 2025: Jervois Global ASX release — Restructuring Support Agreement with Millstreet Capital Management LLC (U.S.) provides US$145 million new equity capital pre-/post-recapitalisation, including a US$70 million equity commitment specifically to underpin restart of the São Miguel Paulista Class 1 Ni–Co electrolytic refinery; implemented via prepackaged U.S. Chapter 11. Distinct from jervois_smp_restart_2025 (FID/ops framing), jervois_smp_restart_construction_2026, and EU CRMA status row.",
        "investment_type": "financing",
        "value": "70000000",
        "currency": "USD",
        "value_usd": "70000000",
        "fx_usd": "1",
        "fx_date": "2025-01-02",
        "year": "2025",
        "status": "active",
        "lat": "-23.50",
        "lon": "-46.44",
        "geo_note": "São Miguel Paulista refinery neighbourhood, São Paulo.",
        "evidence": "documented",
        "source_id": "jervois_millstreet_asx_20250102",
        "note": "Actor: Millstreet Capital (U.S.) equity to Jervois SMP Brazil — us. Official ASX announcement; value uses the USD 70m SMP-dedicated equity commitment (not the full USD 145m group package).",
    },
    {
        "id": "jervois_millstreet_smp_equity_70m_2025",
        "retrieved": "2026-10-01",
        "source_id": "jervois_millstreet_asx_20250102",
        "url": "https://announcements.asx.com.au/asxpdf/20250102/pdf/06d61l41d3kpc5.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Millstreet will provide US$145 million of pre- and post-recapitalisation new equity capital to recapitalise the Jervois group business, including a US$70 million equity commitment to underpin the SMP nickel cobalt refinery restart",
        "note": "Opened Jervois ASX Millstreet recapitalisation announcement PDF.",
    },
    {
        "id": "jervois_millstreet_asx_20250102",
        "type": "company",
        "chicago": "Jervois Global Limited. “Jervois Global Signs Recapitalisation Agreement.” ASX announcement, 2 January 2025.",
        "url": "https://announcements.asx.com.au/asxpdf/20250102/pdf/06d61l41d3kpc5.pdf",
        "annotation": "ASX primary on Millstreet USD 70m equity commitment for São Miguel Paulista restart. Supports jervois_millstreet_smp_equity_70m_2025.",
        "supports": ["jervois_millstreet_smp_equity_70m_2025", "hunt_res_nickel"],
    },
)

# ---------------------------------------------------------------------------
# graphite — Sprott Santa Cruz Phase 2 stream CapEx tranche thin_topup
# ---------------------------------------------------------------------------
A(
    {
        "id": "south_star_sprott_phase2_stream_27m",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "Sprott Resource Streaming — Santa Cruz Phase 2 CapEx stream (partial)",
        "country": "Brazil",
        "asset": "South Star Battery Metals company release on US$28 million Sprott Resource Streaming & Royalty Corp streaming package: Phase 2 Stream provides minimum US$9m / up to US$18m cash consideration for partial funding of Phase 2 CapEx stated as US$27 million (25,000 tpy expansion path at Santa Cruz, Bahia). Distinct from south_star_sprott_4m_term_2025 (2025 indicative US$4m term sheet) and south_star_santa_cruz_restart_202604. Later 2026 updates note board pursuing alternative financing after Sprott discussions — row captures the disclosed Phase 2 CapEx/stream structure.",
        "investment_type": "financing",
        "value": "27000000",
        "currency": "USD",
        "value_usd": "27000000",
        "fx_usd": "1",
        "fx_date": "2022-01-01",
        "year": "2022",
        "status": "active",
        "lat": "-16.28",
        "lon": "-39.30",
        "geo_note": "Santa Cruz Graphite Project, southern Bahia (South Star geography).",
        "evidence": "documented",
        "source_id": "south_star_sprott_stream_28m",
        "note": "Actor: Sprott Streaming (Canada/allied) + South Star (Canada) — allied. Company primary; value uses disclosed Phase 2 CapEx USD 27m (stream is partial funding up to USD 18m). Year set to streaming announcement frame on company page.",
    },
    {
        "id": "south_star_sprott_phase2_stream_27m",
        "retrieved": "2026-10-01",
        "source_id": "south_star_sprott_stream_28m",
        "url": "https://southstarbatterymetals.com/us28-million-streaming-agreement-with-sprott-resource-streaming-and-royalty-corp-for-the-santa-cruz-graphite-project-in-brazil/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "The Phase 2 Stream payment (“Phase 2 Stream”) has a minimum of US$9M and up to US$18M cash consideration for partial funding of Phase 2 CAPEX (US$27M), subject to SRSR Phase 2 due diligence as well as investment committee update and approval.",
        "note": "Opened South Star Sprott streaming agreement page (Phase 2 CapEx USD 27m).",
    },
    {
        "id": "south_star_sprott_stream_28m",
        "type": "company",
        "chicago": "South Star Battery Metals Corp. “US$28 Million Streaming Agreement with Sprott Resource Streaming and Royalty Corp for the Santa Cruz Graphite Project in Brazil.”",
        "url": "https://southstarbatterymetals.com/us28-million-streaming-agreement-with-sprott-resource-streaming-and-royalty-corp-for-the-santa-cruz-graphite-project-in-brazil/",
        "annotation": "South Star primary on Sprott stream including Phase 2 CapEx USD 27m / up to USD 18m stream. Supports south_star_sprott_phase2_stream_27m.",
        "supports": ["south_star_sprott_phase2_stream_27m", "hunt_res_graphite"],
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
        "hunt_fenb_araxa": "Cycle 54 thin_topup: logged cbmm_toshiba_nb_oxide_plant_planned_2025 (allied; 1,000 tpy planned Toshiba-tech oxide plant).",
        "hunt_res_nickel": "Cycle 54 thin_topup: logged jervois_millstreet_smp_equity_70m_2025 (U.S.; USD 70m Millstreet equity for SMP).",
        "hunt_res_graphite": "Cycle 54 thin_topup: logged south_star_sprott_phase2_stream_27m (allied; Phase 2 CapEx USD 27m / stream up to USD 18m).",
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
    print("Cycle 54 thin_topup rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
