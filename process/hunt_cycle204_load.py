#!/usr/bin/env python3
"""Cycle 204 hunt: shuffle_seed=20261204; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261204).shuffle):
lithium, engineering_epc, power_plants_grid, niobium, building_materials,
graphite, other_renewables, fission_smr, nickel, copper, solar, rail, water,
bridges_roads, port_cranes, balsa, port_ownership, wind.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on AES/Freeport/EXIM/DFC/Fluence/Bechtel/Progress
Rail/Wabtec/Albemarle/EnergyX/Meitner/GE Vernova Venezuela sweeps (GE Vernova
Venezuela grid MoU logged CapEx blank). PRC equal-budget: CAMC/Zijin/PowerChina/
ZPMC/CRIG TAM-TSB already logged — miss.
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
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


def row_doc(
    rid,
    layer,
    subcategory,
    side,
    counterpart,
    country,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    source_id,
    quote,
    url,
    note,
    hunt_support,
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd=None,
    fx_usd=None,
    chicago=None,
    bib_type="company",
    annotation=None,
    evid_note=None,
    pair_id="",
    counterpart_side="",
    counterpart_actor="",
    counterpart_value="",
    counterpart_currency="",
    counterpart_value_usd="",
    gap="",
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": investment_type,
            "value": value,
            "currency": currency,
            "value_usd": value_usd,
            "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "",
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": evidence,
            "source_id": source_id,
            "note": note,
            "pair_id": pair_id,
            "counterpart_side": counterpart_side,
            "counterpart_actor": counterpart_actor,
            "counterpart_value": counterpart_value,
            "counterpart_currency": counterpart_currency,
            "counterpart_value_usd": counterpart_value_usd,
            "gap": gap,
        },
        {
            "id": rid,
            "retrieved": "2026-10-04",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": evidence,
            "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id,
            "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url,
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. power_plants_grid / us — GE Vernova–CORPOELEC Venezuela grid modernization (CapEx blank)
row_doc(
    "ge_vernova_corpoelec_venezuela_grid_2026",
    "energy",
    "power_plants_grid",
    "us",
    "GE Vernova — CORPOELEC Venezuela electric grid modernization / capacity add",
    "Venezuela",
    "2 Sep 2026 U.S. Department of Energy fact sheet: Secretary Wright witnesses execution of GE Vernova agreement to modernize and expand Venezuela’s electric grid — plans to bring 1 GW of new reliable power online within first 24 months plus 5 GW over the following four years; covers thermal and hydroelectric generation, transmission/distribution infrastructure, and key substations; builds on 15 Jun 2026 GE Vernova–CORPOELEC cooperation framework. CapEx / contract USD not disclosed on DOE page. Distinct from impsa_tocoma_macagua_672mw_2026 (IMPSA hydro rehab).",
    "",
    "",
    "2026",
    "7.77",
    "-62.89",
    "Guri / national grid rehab geography (DOE cites thermal+hydro+T&D nationwide; approximate Guri pin for hydro focus).",
    "doe_ge_vernova_venezuela_20260902",
    "Through this agreement, GE Vernova plans to bring 1 gigawatt of new reliable power online within the first 24 months, in addition to 5 gigawatts over the following four years, significantly expanding Venezuela’s power capacity. The agreement will address thermal and hydroelectric power generation, transmission and distribution infrastructure, and key substations.",
    "https://www.energy.gov/articles/fact-sheet-delivering-president-trumps-promise-unleash-prosperity-and-security-united",
    "Actor: GE Vernova (U.S.) — us; counterpart CORPOELEC (Venezuela state utility). U.S. DOE English primary fact sheet. CapEx blank (framework capacity targets only). Shuffle power_plants_grid; ≥1/3 U.S. hunt; fills Venezuela×grid beyond Tocoma.",
    "hunt_cycle204",
    investment_type="framework_agreement",
    evidence="documented",
    currency="USD",
    value_usd="",
    fx_usd="",
    bib_type="government",
    chicago='U.S. Department of Energy. “FACT SHEET: Delivering on President Trump’s Promise to Unleash Prosperity and Security for the United States and Venezuela.” September 2, 2026. https://www.energy.gov/articles/fact-sheet-delivering-president-trumps-promise-unleash-prosperity-and-security-united.',
    annotation="DOE: GE Vernova Venezuela grid 1 GW/24mo + 5 GW/4yr; CapEx blank. Supports ge_vernova_corpoelec_venezuela_grid_2026.",
    evid_note="Opened DOE English fact sheet 2026-10-04; 1 GW/24mo + 5 GW/4yr and CORPOELEC framework confirmed; CapEx undisclosed.",
)

# 2. water / allied — Sacyr Antofagasta Reúso Salar del Carmen project finance USD 460m
row_doc(
    "sacyr_antofagasta_reuse_financing_460m_2026",
    "resources",
    "water",
    "allied",
    "Sacyr Agua — Reúso Salar del Carmen project financing (Antofagasta)",
    "Chile",
    "27 Apr 2026 Sacyr: closes financing of Planta de Reúso Salar del Carmen (Antofagasta) for USD 460 million — subscribed by BancoEstado, BTG Pactual and Banco Internacional; 35-year Econssa concession; plant capacity to 900 l/s for mining reuse; COD targeted 2028; includes ~16 km conveyance (5.4 km microtunnel) plus laterals to La Negra and Mantos Blancos. Distinct from sacyr_antofagasta_reuse_292m_2025 (award CapEx ~USD 292m) — this row stores the project-finance close face.",
    "460000000",
    "2026-04-27",
    "2026",
    "-23.65",
    "-70.27",
    "Salar del Carmen sector, Antofagasta (company geography; same pin family as CapEx award row).",
    "sacyr_antofagasta_financing_20260427",
    "Sacyr Agua ha cerrado con éxito la financiación de la planta de agua Reúso Salar del Carmen, ubicada en Antofagasta (Chile), por un importe de 460 millones de dólares. El plazo de la concesión es de 35 años. La financiación ha sido suscrita por BancoEstado, BTG Pactual y Banco Internacional.",
    "https://sacyr.com/-/sacyr-cierra-la-financiaci%C3%B3n-de-la-planta-de-re%C3%BAso-de-agua-de-antofagasta-chile-por-460-millones-de-d%C3%B3lares",
    "Actor: Sacyr Agua (Spain) — allied. Company Spanish primary. Financing face = USD 460m (distinct from prior USD 292m award CapEx row). Shuffle water.",
    "hunt_cycle204",
    investment_type="project_finance",
    evidence="documented",
    currency="USD",
    value_usd="460000000",
    fx_usd="1",
    bib_type="company",
    chicago='Sacyr. “Sacyr cierra la financiación de la planta de reúso de agua de Antofagasta (Chile) por 460 millones de dólares.” April 27, 2026. https://sacyr.com/-/sacyr-cierra-la-financiaci%C3%B3n-de-la-planta-de-re%C3%BAso-de-agua-de-antofagasta-chile-por-460-millones-de-d%C3%B3lares.',
    annotation="Sacyr Antofagasta reuse financing: USD 460m. Supports sacyr_antofagasta_reuse_financing_460m_2026.",
    evid_note="Opened Sacyr Spanish company primary 2026-10-04; USD 460m / BancoEstado–BTG–Banco Internacional / 35-year concession confirmed.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    supports = entry.get("supports") or []
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        prev = existing.get("supports") or []
        for s in supports:
            if s not in prev:
                prev.append(s)
        existing.update(entry)
        existing["supports"] = prev
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if not isinstance(bib, list):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added = []
    updated = []

    for row, evid, bib_e in ITEMS:
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
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_e)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle204 added {len(added)}: {added}")
    print(f"cycle204 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
