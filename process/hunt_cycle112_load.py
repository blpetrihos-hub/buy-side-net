#!/usr/bin/env python3
"""Cycle 112 hunt: shuffle_seed=20261112; equal budget; U.S./PRC split; thin after.

Order: lithium, building_materials, port_ownership, engineering_epc, copper,
graphite, rail, solar, water, port_cranes, nickel, bridges_roads, balsa,
fission_smr, wind, other_renewables, power_plants_grid, niobium.
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
# resources/water — Flatiron Portugués Dam construction 2008 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "flatiron_portugues_dam_2008",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Flatiron Dragados USA Inc. — USACE Portugués Dam construction",
        "country": "Puerto Rico",
        "asset": "27 Mar 2008: USACE awards contract W912EP08C0011 to Flatiron Dragados USA, Inc. for Portugués Dam construction; obligated USD 217,698,067.99; place of performance Adjuntas. Distinct from Flatiron Bechara / Margarita Channel Río Puerto Nuevo flood-control awards.",
        "investment_type": "epc",
        "value": "217698067.99",
        "currency": "USD",
        "value_usd": "217698067.99",
        "fx_usd": "1",
        "fx_date": "2008-03-27",
        "year": "2008",
        "status": "active",
        "lat": "18.180",
        "lon": "-66.722",
        "geo_note": "Portugués Dam / Portugués River, Adjuntas–Ponce corridor, Puerto Rico (USASpending PoP Adjuntas).",
        "evidence": "documented",
        "source_id": "usaspending_flatiron_portugues_20080327",
        "note": "Actor: Flatiron Dragados USA under USACE Civil Works — coded us (consistent with Bechara/Margarita USACE rows). Official USASpending Award API.",
    },
    {
        "id": "flatiron_portugues_dam_2008",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_flatiron_portugues_20080327",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP08C0011_9700_-NONE-_-NONE-/",
        "price_year": "2008",
        "evidence": "documented",
        "quote": "PORTUGUES DAM CONSTRUCTION",
        "note": "Opened USASpending Award API: Flatiron Dragados USA; USD 217,698,067.99; date_signed 2008-03-27; PoP Adjuntas, PR.",
    },
    {
        "id": "usaspending_flatiron_portugues_20080327",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP08C0011_9700_-NONE-_-NONE- (Flatiron Dragados USA Inc.; USACE Portugués Dam). Signed 27 March 2008. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP08C0011_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP08C0011_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 217.7m Portugués Dam construction. Supports flatiron_portugues_dam_2008.",
        "supports": ["flatiron_portugues_dam_2008", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/bridges_roads — Carro De Diego Bridge 2007 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "carro_de_diego_bridge_2007",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "Carro & Carro Enterprises Inc — USACE De Diego Bridge Contract 2D1 reprocurement",
        "country": "Puerto Rico",
        "asset": "28 Sep 2007: USACE awards contract W912EP07C0024 to Carro & Carro Enterprises Inc for Contract 2D1 De Diego Bridge reprocurement (replacement of terminated default contract W912EP-03-C-0012); obligated USD 34,965,825.68; place of performance San Juan. Distinct from FHWA Emergency Relief landslide/sign packages.",
        "investment_type": "epc",
        "value": "34965825.68",
        "currency": "USD",
        "value_usd": "34965825.68",
        "fx_usd": "1",
        "fx_date": "2007-09-28",
        "year": "2007",
        "status": "active",
        "lat": "18.450",
        "lon": "-66.075",
        "geo_note": "De Diego Bridge / José de Diego Expressway corridor, San Juan, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_carro_dediego_20070928",
        "note": "Actor: Carro & Carro Enterprises Inc (Puerto Rico / U.S.) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "carro_de_diego_bridge_2007",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_carro_dediego_20070928",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP07C0024_9700_-NONE-_-NONE-/",
        "price_year": "2007",
        "evidence": "documented",
        "quote": "CONTRACT 2D1, DE DIEGO BRIDGE REPROCUREMENT CONTRACT OF TERMINATION FOR DEFAULT CONTRACT W912EP-03-C-0012",
        "note": "Opened USASpending Award API: Carro & Carro; USD 34,965,825.68; date_signed 2007-09-28; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_carro_dediego_20070928",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP07C0024_9700_-NONE-_-NONE- (Carro & Carro Enterprises Inc; USACE De Diego Bridge). Signed 28 September 2007. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP07C0024_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP07C0024_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 35.0m De Diego Bridge Contract 2D1. Supports carro_de_diego_bridge_2007.",
        "supports": ["carro_de_diego_bridge_2007", "hunt_infra_bridges_roads"],
    },
)


def upsert_bib(bib: list, bib_by: dict, entry: dict) -> None:
    eid = entry["id"]
    if eid in bib_by:
        bib[bib_by[eid]].update(entry)
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added: list[str] = []

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
        "hunt_res_lithium": "Cycle 112: equal budget; Ganfeng PPG dense (miss).",
        "hunt_infra_building_materials": "Cycle 112: equal budget; Caribbean Lumber dense (miss).",
        "hunt_infra_port_ownership": "Cycle 112: equal budget; Hutchison / APM dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 112: equal budget; RQ-AECOM/Tutor dense (miss).",
        "hunt_res_copper": "Cycle 112: equal budget; CMOC Cangrejos dense (miss).",
        "hunt_res_graphite": "Cycle 112: equal budget; South Star / Graphcoa dense (miss). Thin dry — shift.",
        "hunt_latam_rail_telecom": "Cycle 112: equal budget; CRRC / CRCC dense (miss).",
        "hunt_energy_solar": "Cycle 112: equal budget; Sungrow Atacama/Futura/Helio Valgas dense (miss).",
        "hunt_res_water": "Cycle 112: logged flatiron_portugues_dam_2008 (USD 217.7m USACE).",
        "hunt_infra_port_cranes": "Cycle 112: equal budget; ZPMC Kingston / ICAVE dense (miss).",
        "hunt_res_nickel": "Cycle 112: equal budget; BRN / MMG dense (miss). Thin dry — shift.",
        "hunt_infra_bridges_roads": "Cycle 112: logged carro_de_diego_bridge_2007 (USD 35.0m USACE).",
        "hunt_res_balsa": "Cycle 112: equal budget; Plantabal / WITS dense (miss). Thin dry — shift.",
        "hunt_energy_fission_smr": "Cycle 112: equal budget; CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_energy_wind": "Cycle 112: equal budget; Goldwind / Vestas dense (miss).",
        "hunt_energy_other_renewables": "Cycle 112: equal budget; BESS Coya dense (miss).",
        "hunt_br_power_equip": "Cycle 112: equal budget; Weston/WSP/Fluor Maria dense (miss).",
        "hunt_fenb_araxa": "Cycle 112: equal budget; CBMM CapEx dense (miss).",
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
    print("Cycle 112 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
