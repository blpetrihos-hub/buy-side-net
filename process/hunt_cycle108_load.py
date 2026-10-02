#!/usr/bin/env python3
"""Cycle 108 hunt: shuffle_seed=20261108; equal budget; U.S./PRC split; thin after.

Order: engineering_epc, rail, wind, fission_smr, other_renewables, bridges_roads,
nickel, port_cranes, water, balsa, port_ownership, copper, niobium,
building_materials, power_plants_grid, lithium, solar, graphite.
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
# energy/solar — Sungrow Helio Valgas 500 MWac / 650 MWp (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sungrow_mercury_helio_valgas_2022",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Sungrow — SG3125HV-30 / SG6250HV-MV turnkey inverters for Mercury Renew Helio Valgas (MG)",
        "country": "Brazil",
        "asset": "31 Mar 2022 Sungrow: 500 MWac PV inverter supply contract with Mercury Renew (Comerc Energia Group) for Helio Valgas solar park in Várzea da Palma, Minas Gerais — 650 MWp plant capacity; SG3125HV-30 central inverters with SG6250HV-MV turnkey MV containers; expected >1,300 GWh/year to SIN. CapEx USD not disclosed. Distinct from Sungrow Aurora Chile / Observatorio / Librillo BESS rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2022-03-31",
        "year": "2022",
        "status": "active",
        "lat": "-17.598",
        "lon": "-44.731",
        "geo_note": "Helio Valgas PV plant, Várzea da Palma, Minas Gerais, Brazil (company release).",
        "evidence": "documented",
        "source_id": "sungrow_helio_valgas_20220331",
        "note": "Actor: Sungrow (PRC HQ) — prc; buyer Mercury Renew / Comerc (Brazil). Company English primary. CapEx blank.",
    },
    {
        "id": "sungrow_mercury_helio_valgas_2022",
        "retrieved": "2026-10-02",
        "source_id": "sungrow_helio_valgas_20220331",
        "url": "https://en.sungrowpower.com/newsDetail/2589",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "Sungrow recently closed a 500 MWac PV inverter solution supply contract with Mercury Renew... Helio Valgas PV plant in Varzea da Palma, Minas Gerais, with capacity of 650 MWp",
        "note": "Opened Sungrow English newsDetail/2589; dated 31 Mar 2022; CapEx blank.",
    },
    {
        "id": "sungrow_helio_valgas_20220331",
        "type": "company",
        "chicago": "Sungrow Power Supply Co., Ltd. “Sungrow Signs 500 MWac Contract with Mercury Renew to Supply PV Inverter Solutions to the Helio Valgas Solar Park in Brazil.” News release, 31 March 2022. https://en.sungrowpower.com/newsDetail/2589.",
        "url": "https://en.sungrowpower.com/newsDetail/2589",
        "annotation": "Company English primary: 500 MWac / 650 MWp Helio Valgas (Várzea da Palma, MG) for Mercury Renew. Supports sungrow_mercury_helio_valgas_2022.",
        "supports": ["sungrow_mercury_helio_valgas_2022", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# resources/water — Flatiron Margarita Channel CNT 2AR 2010 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "flatiron_margarita_channel_2010",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Flatiron Dragados USA Inc. — USACE Río Puerto Nuevo Margarita Channel improvements (CNT 2AR)",
        "country": "Puerto Rico",
        "asset": "29 Jun 2010: USACE awards contract W912EP10C0035 to Flatiron Dragados USA, Inc. for Río Puerto Nuevo Flood Control Project Margarita Channel improvements and misc. features (CNT 2AR), San Juan; obligated USD 57,668,620.33. Distinct from Flatiron Bechara Phases 1–2 and LP C&D Upper Margarita stilling-basin award.",
        "investment_type": "epc",
        "value": "57668620.33",
        "currency": "USD",
        "value_usd": "57668620.33",
        "fx_usd": "1",
        "fx_date": "2010-06-29",
        "year": "2010",
        "status": "active",
        "lat": "18.408",
        "lon": "-66.072",
        "geo_note": "Margarita Channel / Río Puerto Nuevo, San Juan, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_flatiron_margarita_20100629",
        "note": "Actor: Flatiron Dragados USA under USACE Civil Works — coded us (consistent with Bechara / Ferrovial USACE rows). Official USASpending Award API.",
    },
    {
        "id": "flatiron_margarita_channel_2010",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_flatiron_margarita_20100629",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP10C0035_9700_-NONE-_-NONE-/",
        "price_year": "2010",
        "evidence": "documented",
        "quote": "RIO PUERTO NUEVO FLOOD CONTROL PROJECT, MARGARITA CHANNEL IMPROVEMENTS AND MISC. FEATURES (CNT 2AR)",
        "note": "Opened USASpending Award API: Flatiron Dragados USA; USD 57,668,620.33; date_signed 2010-06-29.",
    },
    {
        "id": "usaspending_flatiron_margarita_20100629",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP10C0035_9700_-NONE-_-NONE- (Flatiron Dragados USA Inc.; USACE Margarita Channel CNT 2AR). Signed 29 June 2010. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP10C0035_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP10C0035_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 57.7m Margarita Channel CNT 2AR. Supports flatiron_margarita_channel_2010.",
        "supports": ["flatiron_margarita_channel_2010", "hunt_res_water"],
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
        "hunt_infra_engineering_epc": "Cycle 108: equal budget; Tutor/RQ-AECOM/Caddell just prior (miss).",
        "hunt_latam_rail_telecom": "Cycle 108: equal budget; CRRC / CRCC dense (miss).",
        "hunt_energy_wind": "Cycle 108: equal budget; Goldwind / Vestas dense (miss).",
        "hunt_energy_fission_smr": "Cycle 108: equal budget; CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_energy_other_renewables": "Cycle 108: equal budget; JC/Schneider dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 108: equal budget; FHWA construction ≥USD 2.5m exhausted (miss).",
        "hunt_res_nickel": "Cycle 108: equal budget; BRN / MMG dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 108: equal budget; ZPMC Kingston / ICAVE dense (miss).",
        "hunt_res_water": "Cycle 108: logged flatiron_margarita_channel_2010 (USD 57.7m USACE).",
        "hunt_res_balsa": "Cycle 108: equal budget; Plantabal / WITS dense (miss). Thin dry — shift.",
        "hunt_infra_port_ownership": "Cycle 108: equal budget; Hutchison / APM dense (miss).",
        "hunt_res_copper": "Cycle 108: equal budget; CMOC Cangrejos dense (miss).",
        "hunt_fenb_araxa": "Cycle 108: equal budget; CBMM CapEx dense (miss).",
        "hunt_infra_building_materials": "Cycle 108: equal budget; Caribbean Lumber dense (miss).",
        "hunt_br_power_equip": "Cycle 108: equal budget; Fluor/PowerSecure dense (miss).",
        "hunt_res_lithium": "Cycle 108: equal budget; Ganfeng PPG dense (miss).",
        "hunt_energy_solar": "Cycle 108: logged sungrow_mercury_helio_valgas_2022 (500 MWac / 650 MWp MG).",
        "hunt_res_graphite": "Cycle 108: equal budget; South Star / Graphcoa dense (miss). Thin dry — shift.",
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
    print("Cycle 108 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
