#!/usr/bin/env python3
"""Cycle 110 hunt: shuffle_seed=20261110; equal budget; U.S./PRC split; thin after.

Order: port_cranes, port_ownership, other_renewables, lithium, building_materials,
fission_smr, niobium, bridges_roads, solar, copper, rail, water, power_plants_grid,
graphite, balsa, wind, engineering_epc, nickel.
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
# energy/solar — Sungrow HDEC Atacama 480 MW turnkey inverters 2022 (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sungrow_hdec_atacama_480mw_2022",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Sungrow — turnkey PV inverter solutions for POWERCHINA HDEC 480 MW Atacama plant",
        "country": "Chile",
        "asset": "24 May 2022 Sungrow: supply of turnkey PV inverter solutions to a 480 MW PV plant in Chile’s Atacama Desert; EPC POWERCHINA Huadong Engineering Corporation Limited (HDEC); >400 ha site; expected commissioning 2023; ~1,145 GWh/year. CapEx USD not disclosed. Distinct from Helio Valgas / Futura / BESS Coya / Aurora rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2022-05-24",
        "year": "2022",
        "status": "active",
        "lat": "-24.50",
        "lon": "-69.25",
        "geo_note": "Atacama Desert PV plant, Chile (company geography; approximate desert pin).",
        "evidence": "documented",
        "source_id": "sungrow_atacama_480_20220524",
        "note": "Actor: Sungrow (PRC HQ) — prc; EPC POWERCHINA HDEC (PRC) — prc counterpart. Company English primary. CapEx blank.",
    },
    {
        "id": "sungrow_hdec_atacama_480mw_2022",
        "retrieved": "2026-10-02",
        "source_id": "sungrow_atacama_480_20220524",
        "url": "https://en.sungrowpower.com/newsDetail/2669",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "supply its turnkey PV inverter solutions solutions to a 480 MW PV plant in Chile’s Atacama Desert... The project’s EPC, POWERCHINA HUADONG Engineering Corporation Limited (HDEC)",
        "note": "Opened Sungrow English newsDetail/2669; dated 24 May 2022; CapEx blank.",
    },
    {
        "id": "sungrow_atacama_480_20220524",
        "type": "company",
        "chicago": "Sungrow Power Supply Co., Ltd. “Sungrow to Supply a 480 MW PV Project in Chile with Turnkey Inverter Solutions.” News release, 24 May 2022. https://en.sungrowpower.com/newsDetail/2669.",
        "url": "https://en.sungrowpower.com/newsDetail/2669",
        "annotation": "Company English primary: 480 MW Atacama Desert PV with POWERCHINA HDEC EPC. Supports sungrow_hdec_atacama_480mw_2022.",
        "supports": ["sungrow_hdec_atacama_480mw_2022", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — RQ-AECOM Ponce RIO rebuild 2021 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "rq_aecom_ponce_rio_2021",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "RQ-AECOM 2 JV — USCG rebuild Resident Inspection Office (RIO) Ponce",
        "country": "Puerto Rico",
        "asset": "22 Jun 2021: U.S. Coast Guard awards task order 70Z04721FPONCRO00 to RQ-AECOM 2 JV for rebuild of Resident Inspection Office (RIO) facilities in Ponce; obligated USD 21,421,607.89. Distinct from RQ-AECOM Borinquen Phase 2 and RQ-LORD Ramey microgrid.",
        "investment_type": "epc",
        "value": "21421607.89",
        "currency": "USD",
        "value_usd": "21421607.89",
        "fx_usd": "1",
        "fx_date": "2021-06-22",
        "year": "2021",
        "status": "active",
        "lat": "17.984",
        "lon": "-66.614",
        "geo_note": "USCG Resident Inspection Office, Ponce, Puerto Rico (award description).",
        "evidence": "documented",
        "source_id": "usaspending_rq_aecom_ponce_20210622",
        "note": "Actor: RQ-AECOM 2 JV (U.S. construction JV) under USCG — us. Official USASpending Award API.",
    },
    {
        "id": "rq_aecom_ponce_rio_2021",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_rq_aecom_ponce_20210622",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04721FPONCRO00_7008_70Z04718DRQAECM00_7008/",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "REBUILD FACILITIES RESIDENT INSPECTION OFFICE (RIO) PONCE, PONCE, PUERTO RICO",
        "note": "Opened USASpending Award API: RQ-AECOM 2 JV; USD 21,421,607.89; date_signed 2021-06-22.",
    },
    {
        "id": "usaspending_rq_aecom_ponce_20210622",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_70Z04721FPONCRO00_7008_70Z04718DRQAECM00_7008 (RQ-AECOM 2 JV; USCG RIO Ponce rebuild). Signed 22 June 2021. https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04721FPONCRO00_7008_70Z04718DRQAECM00_7008/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04721FPONCRO00_7008_70Z04718DRQAECM00_7008/",
        "annotation": "USASpending primary: USD 21.4m USCG RIO Ponce rebuild. Supports rq_aecom_ponce_rio_2021.",
        "supports": ["rq_aecom_ponce_rio_2021", "hunt_infra_engineering_epc"],
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
        "hunt_infra_port_cranes": "Cycle 110: equal budget; ZPMC Kingston / ICAVE dense (miss).",
        "hunt_infra_port_ownership": "Cycle 110: equal budget; Hutchison / APM dense (miss).",
        "hunt_energy_other_renewables": "Cycle 110: equal budget; BESS Coya just prior (miss).",
        "hunt_res_lithium": "Cycle 110: equal budget; Ganfeng PPG dense (miss).",
        "hunt_infra_building_materials": "Cycle 110: equal budget; Caribbean Lumber dense (miss).",
        "hunt_energy_fission_smr": "Cycle 110: equal budget; CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_fenb_araxa": "Cycle 110: equal budget; CBMM CapEx dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 110: equal budget; FHWA construction ≥USD 2.5m exhausted (miss).",
        "hunt_energy_solar": "Cycle 110: logged sungrow_hdec_atacama_480mw_2022 (480 MW Atacama / HDEC).",
        "hunt_res_copper": "Cycle 110: equal budget; CMOC Cangrejos dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 110: equal budget; CRRC / CRCC dense (miss).",
        "hunt_res_water": "Cycle 110: equal budget; Guajataca / Margarita dense (miss).",
        "hunt_br_power_equip": "Cycle 110: equal budget; Fluor/PowerSecure/WSP dense (miss).",
        "hunt_res_graphite": "Cycle 110: equal budget; South Star / Graphcoa dense (miss). Thin dry — shift.",
        "hunt_res_balsa": "Cycle 110: equal budget; Plantabal / WITS dense (miss). Thin dry — shift.",
        "hunt_energy_wind": "Cycle 110: equal budget; Goldwind / Vestas dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 110: logged rq_aecom_ponce_rio_2021 (USCG RIO Ponce).",
        "hunt_res_nickel": "Cycle 110: equal budget; BRN / MMG dense (miss). Thin dry — shift.",
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
    print("Cycle 110 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
