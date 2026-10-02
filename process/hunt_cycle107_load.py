#!/usr/bin/env python3
"""Cycle 107 hunt: shuffle_seed=20261107; equal budget; U.S./PRC split; thin after.

Order: power_plants_grid, lithium, niobium, other_renewables, engineering_epc,
copper, port_ownership, fission_smr, wind, graphite, bridges_roads,
building_materials, nickel, balsa, rail, port_cranes, solar, water.
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
# energy/power_plants_grid — Fluor PREPA full grid restore 2017 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fluor_pr_grid_restore_2017",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Fluor Enterprises Inc — USACE repair/restore Puerto Rico power grid",
        "country": "Puerto Rico",
        "asset": "1 Dec 2017: USACE awards delivery order W912DY18F0032 under IDIQ to Fluor Enterprises, Inc. to repair and restore all aspects of the Puerto Rico power grid (Hurricane Maria); obligated USD 276,296,707.16; place of performance San Juan. Distinct from Fluor T&D order W912DY18F0003 and PowerSecure survey award.",
        "investment_type": "epc",
        "value": "276296707.16",
        "currency": "USD",
        "value_usd": "276296707.16",
        "fx_usd": "1",
        "fx_date": "2017-12-01",
        "year": "2017",
        "status": "active",
        "lat": "18.466",
        "lon": "-66.106",
        "geo_note": "Puerto Rico PREPA power grid (USASpending PoP San Juan; island-wide scope).",
        "evidence": "documented",
        "source_id": "usaspending_fluor_pr_restore_20171201",
        "note": "Actor: Fluor Enterprises Inc (U.S. HQ) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "fluor_pr_grid_restore_2017",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_fluor_pr_restore_20171201",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912DY18F0032_9700_W912DY15G0007_9700/",
        "price_year": "2017",
        "evidence": "documented",
        "quote": "REPAIR AND RESTORE ALL ASPECTS OF THE PUERTO RICO POWER GRID",
        "note": "Opened USASpending Award API: Fluor; USD 276,296,707.16; date_signed 2017-12-01; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_fluor_pr_restore_20171201",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912DY18F0032_9700_W912DY15G0007_9700 (Fluor Enterprises Inc; USACE PREPA grid restore). Signed 1 December 2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912DY18F0032_9700_W912DY15G0007_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912DY18F0032_9700_W912DY15G0007_9700/",
        "annotation": "USASpending primary: USD 276.3m PREPA full grid restore. Supports fluor_pr_grid_restore_2017.",
        "supports": ["fluor_pr_grid_restore_2017", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Tutor Perini USCG San Juan Phase II (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "tutor_perini_uscg_sj_phase2_2022",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Tutor Perini Corporation — USCG San Juan hurricane rebuild Phase II East / SE X waterfront",
        "country": "Puerto Rico",
        "asset": "12 Sep 2022: U.S. Coast Guard awards task order 70Z04722F43000017 to Tutor Perini Corporation for design/build hurricane rebuild San Juan Phase II East base bid and Option 5 SE X waterfront boat ramp; obligated USD 117,046,491.59; place of performance San Juan. Distinct from Phase III West/Central and Río Bayamón Phase-1 awards.",
        "investment_type": "epc",
        "value": "117046491.59",
        "currency": "USD",
        "value_usd": "117046491.59",
        "fx_usd": "1",
        "fx_date": "2022-09-12",
        "year": "2022",
        "status": "active",
        "lat": "18.460",
        "lon": "-66.116",
        "geo_note": "USCG Base San Juan waterfront, San Juan, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_tutor_sj_p2_20220912",
        "note": "Actor: Tutor Perini Corporation (U.S. HQ) under USCG — us. Official USASpending Award API.",
    },
    {
        "id": "tutor_perini_uscg_sj_phase2_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_tutor_sj_p2_20220912",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000017_7008_70Z04718DTUTPER00_7008/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "DESIGN/BUILD HURRICANE REBUILD TASK ORDER FOR SAN JUAN PHASE II EAST BASE BID AND OPTION  5: SE X WATERFRONT BOAT RAMP",
        "note": "Opened USASpending Award API: Tutor Perini; USD 117,046,491.59; date_signed 2022-09-12.",
    },
    {
        "id": "usaspending_tutor_sj_p2_20220912",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_70Z04722F43000017_7008_70Z04718DTUTPER00_7008 (Tutor Perini Corporation; USCG San Juan Phase II). Signed 12 September 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000017_7008_70Z04718DTUTPER00_7008/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000017_7008_70Z04718DTUTPER00_7008/",
        "annotation": "USASpending primary: USD 117.0m USCG San Juan Phase II East. Supports tutor_perini_uscg_sj_phase2_2022.",
        "supports": ["tutor_perini_uscg_sj_phase2_2022", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Tutor Perini USCG San Juan Phase III (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "tutor_perini_uscg_sj_phase3_2022",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Tutor Perini Corporation — USCG San Juan hurricane rebuild Phase III West/Central",
        "country": "Puerto Rico",
        "asset": "12 Sep 2022: U.S. Coast Guard awards task order 70Z04722F43000018 to Tutor Perini Corporation for design/build hurricane rebuild USCG San Juan Phase III West/Central (base bid + Option 1 SE I demo shoreline rip-rap/new construction revetment); obligated USD 17,927,679.92; place of performance San Juan. Distinct from Phase II East and Río Bayamón awards.",
        "investment_type": "epc",
        "value": "17927679.92",
        "currency": "USD",
        "value_usd": "17927679.92",
        "fx_usd": "1",
        "fx_date": "2022-09-12",
        "year": "2022",
        "status": "active",
        "lat": "18.458",
        "lon": "-66.120",
        "geo_note": "USCG Base San Juan West/Central shoreline, San Juan, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_tutor_sj_p3_20220912",
        "note": "Actor: Tutor Perini Corporation (U.S. HQ) under USCG — us. Official USASpending Award API.",
    },
    {
        "id": "tutor_perini_uscg_sj_phase3_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_tutor_sj_p3_20220912",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000018_7008_70Z04718DTUTPER00_7008/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "DESIGN/BUILD HURRICANE REBUILD USCG SAN JUAN PHASE III WEST/CENTRAL",
        "note": "Opened USASpending Award API: Tutor Perini; USD 17,927,679.92; date_signed 2022-09-12.",
    },
    {
        "id": "usaspending_tutor_sj_p3_20220912",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_70Z04722F43000018_7008_70Z04718DTUTPER00_7008 (Tutor Perini Corporation; USCG San Juan Phase III). Signed 12 September 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000018_7008_70Z04718DTUTPER00_7008/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000018_7008_70Z04718DTUTPER00_7008/",
        "annotation": "USASpending primary: USD 17.9m USCG San Juan Phase III West/Central. Supports tutor_perini_uscg_sj_phase3_2022.",
        "supports": ["tutor_perini_uscg_sj_phase3_2022", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — RQ-AECOM Borinquen Phase 2 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "rq_aecom_borinquen_phase2_2022",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "RQ-AECOM 2 JV — USCG rebuild Base Detachment & Air Station Borinquen Phase 2",
        "country": "Puerto Rico",
        "asset": "1 Apr 2022: U.S. Coast Guard awards task order 70Z04722F43000006 to RQ-AECOM 2 JV for rebuild of Base Detachment & Air Station Borinquen, Aguadilla, Phase 2; obligated USD 126,584,802.85; place of performance Aguadilla. Distinct from Caddell Nova Borinquen rebuild award and RQ-LORD Ramey microgrid.",
        "investment_type": "epc",
        "value": "126584802.85",
        "currency": "USD",
        "value_usd": "126584802.85",
        "fx_usd": "1",
        "fx_date": "2022-04-01",
        "year": "2022",
        "status": "active",
        "lat": "18.495",
        "lon": "-67.129",
        "geo_note": "USCG Air Station Borinquen, Aguadilla, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_rq_aecom_borinquen_20220401",
        "note": "Actor: RQ-AECOM 2 JV (U.S. construction JV) under USCG — us. Official USASpending Award API.",
    },
    {
        "id": "rq_aecom_borinquen_phase2_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_rq_aecom_borinquen_20220401",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000006_7008_70Z04718DRQAECM00_7008/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "REBUILD BASE DETACHMENT & AIR STATION BORINQUEN, AGUADILLA, PUERTO RICO, PHASE 2",
        "note": "Opened USASpending Award API: RQ-AECOM 2 JV; USD 126,584,802.85; date_signed 2022-04-01.",
    },
    {
        "id": "usaspending_rq_aecom_borinquen_20220401",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_70Z04722F43000006_7008_70Z04718DRQAECM00_7008 (RQ-AECOM 2 JV; USCG Borinquen Phase 2). Signed 1 April 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000006_7008_70Z04718DRQAECM00_7008/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000006_7008_70Z04718DRQAECM00_7008/",
        "annotation": "USASpending primary: USD 126.6m Borinquen Phase 2 rebuild. Supports rq_aecom_borinquen_phase2_2022.",
        "supports": ["rq_aecom_borinquen_phase2_2022", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Caddell Nova Borinquen rebuild (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "caddell_nova_borinquen_2022",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Caddell Nova A JV — USCG rebuild Base Detachment and Air Station Borinquen",
        "country": "Puerto Rico",
        "asset": "2022: U.S. Coast Guard awards task order 70Z04722F43000002 to Caddell Nova A JV for rebuild of Base Detachment and Air Station Borinquen, Aguadilla; obligated USD 83,964,602.16; place of performance Aguadilla. Distinct from RQ-AECOM Borinquen Phase 2.",
        "investment_type": "epc",
        "value": "83964602.16",
        "currency": "USD",
        "value_usd": "83964602.16",
        "fx_usd": "1",
        "fx_date": "2022-01-01",
        "year": "2022",
        "status": "active",
        "lat": "18.495",
        "lon": "-67.129",
        "geo_note": "USCG Air Station Borinquen, Aguadilla, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_caddell_borinquen_2022",
        "note": "Actor: Caddell Nova A JV (Caddell Construction, U.S. HQ) under USCG — us. Official USASpending Award API.",
    },
    {
        "id": "caddell_nova_borinquen_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caddell_borinquen_2022",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000002_7008_70Z04718DCADNOV00_7008/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "REBUILD BASE DETACHMENT AND AIR STATION BORINQUEN, AGUADILLA, PUERTO RICO",
        "note": "Opened USASpending Award API: Caddell Nova A JV; USD 83,964,602.16.",
    },
    {
        "id": "usaspending_caddell_borinquen_2022",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_70Z04722F43000002_7008_70Z04718DCADNOV00_7008 (Caddell Nova A JV; USCG Borinquen rebuild). https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000002_7008_70Z04718DCADNOV00_7008/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000002_7008_70Z04718DCADNOV00_7008/",
        "annotation": "USASpending primary: USD 84.0m Borinquen rebuild. Supports caddell_nova_borinquen_2022.",
        "supports": ["caddell_nova_borinquen_2022", "hunt_infra_engineering_epc"],
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
    # Fix Caddell date from API
    import urllib.request
    import json as _json

    try:
        with urllib.request.urlopen(
            "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000002_7008_70Z04718DCADNOV00_7008/",
            timeout=30,
        ) as resp:
            cd = _json.load(resp)
        signed = (cd.get("date_signed") or "2022-01-01")[:10]
        for row, evidence, bib in ITEMS:
            if row["id"] == "caddell_nova_borinquen_2022":
                row["fx_date"] = signed
                row["year"] = signed[:4]
                row["asset"] = (
                    f"{signed[8:10]} {['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][int(signed[5:7])]} {signed[:4]}: "
                    "U.S. Coast Guard awards task order 70Z04722F43000002 to Caddell Nova A JV for rebuild of "
                    "Base Detachment and Air Station Borinquen, Aguadilla; obligated USD 83,964,602.16; "
                    "place of performance Aguadilla. Distinct from RQ-AECOM Borinquen Phase 2."
                )
                evidence["note"] = (
                    f"Opened USASpending Award API: Caddell Nova A JV; USD 83,964,602.16; date_signed {signed}."
                )
                bib["chicago"] = (
                    "U.S. Department of the Treasury, USAspending.gov. Award "
                    "CONT_AWD_70Z04722F43000002_7008_70Z04718DCADNOV00_7008 "
                    f"(Caddell Nova A JV; USCG Borinquen rebuild). Signed {signed}. "
                    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04722F43000002_7008_70Z04718DCADNOV00_7008/."
                )
    except Exception as e:
        print("WARN caddell date fetch:", e)

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
        "hunt_br_power_equip": "Cycle 107: logged fluor_pr_grid_restore_2017 (USD 276.3m PREPA restore).",
        "hunt_res_lithium": "Cycle 107: equal budget; Ganfeng PPG dense (miss).",
        "hunt_fenb_araxa": "Cycle 107: equal budget; CBMM CapEx dense (miss).",
        "hunt_energy_other_renewables": "Cycle 107: equal budget; JC/Schneider dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 107: logged tutor_perini_uscg_sj_phase2_2022 + tutor_perini_uscg_sj_phase3_2022 + rq_aecom_borinquen_phase2_2022 + caddell_nova_borinquen_2022.",
        "hunt_res_copper": "Cycle 107: equal budget; CMOC Cangrejos dense (miss).",
        "hunt_infra_port_ownership": "Cycle 107: equal budget; Hutchison / APM dense (miss).",
        "hunt_energy_fission_smr": "Cycle 107: equal budget; CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_energy_wind": "Cycle 107: equal budget; Goldwind / Vestas dense (miss).",
        "hunt_res_graphite": "Cycle 107: equal budget; South Star / Graphcoa dense (miss). Thin dry — shift.",
        "hunt_infra_bridges_roads": "Cycle 107: equal budget; FHWA construction ≥USD 2.5m exhausted (miss).",
        "hunt_infra_building_materials": "Cycle 107: equal budget; Caribbean Lumber dense (miss).",
        "hunt_res_nickel": "Cycle 107: equal budget; BRN / MMG dense (miss). Thin dry — shift.",
        "hunt_res_balsa": "Cycle 107: equal budget; Plantabal / WITS dense (miss). Thin dry — shift.",
        "hunt_latam_rail_telecom": "Cycle 107: equal budget; CRRC / CRCC dense (miss).",
        "hunt_infra_port_cranes": "Cycle 107: equal budget; ZPMC Kingston / ICAVE dense (miss).",
        "hunt_energy_solar": "Cycle 107: equal budget; TrinaTracker Lagoa do Barro dense (miss).",
        "hunt_res_water": "Cycle 107: equal budget; Guajataca / Río Puerto Nuevo dense (miss).",
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
    print("Cycle 107 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
