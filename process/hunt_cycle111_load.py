#!/usr/bin/env python3
"""Cycle 111 hunt: shuffle_seed=20261111; equal budget; U.S./PRC split; thin after.

Order: building_materials, fission_smr, niobium, power_plants_grid, water,
bridges_roads, port_ownership, wind, other_renewables, port_cranes, nickel,
graphite, engineering_epc, lithium, rail, balsa, copper, solar.
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
# energy/power_plants_grid — Weston Maria temporary power 2017 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "weston_maria_temp_power_2017",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Weston Solutions Inc — USACE temporary power Hurricane Maria (2 months)",
        "country": "Puerto Rico",
        "asset": "8 Oct 2017: USACE awards delivery order W9128F18F0002 under IDIQ to Weston Solutions Inc for temporary power for 2 months in support of Hurricane Maria recovery; obligated USD 218,389,743.35; place of performance Toa Baja. Distinct from Weston Palo Seco/San Juan FY23 temporary-power orders and APTIM Yabucoa temporary power.",
        "investment_type": "epc",
        "value": "218389743.35",
        "currency": "USD",
        "value_usd": "218389743.35",
        "fx_usd": "1",
        "fx_date": "2017-10-08",
        "year": "2017",
        "status": "active",
        "lat": "18.432",
        "lon": "-66.213",
        "geo_note": "Toa Baja Municipality, Puerto Rico (USASpending PoP; Maria temporary-power staging).",
        "evidence": "documented",
        "source_id": "usaspending_weston_maria_20171008",
        "note": "Actor: Weston Solutions Inc (U.S. HQ) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "weston_maria_temp_power_2017",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_weston_maria_20171008",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F18F0002_9700_W9128F14D0024_9700/",
        "price_year": "2017",
        "evidence": "documented",
        "quote": "TEMPORARY POWER FOR 2 MONTHS FOR PUERTO RICO IN SUPPORT OF HURRICANE MARIA RECOVERY EFFORTS",
        "note": "Opened USASpending Award API: Weston; USD 218,389,743.35; date_signed 2017-10-08; PoP Toa Baja, PR.",
    },
    {
        "id": "usaspending_weston_maria_20171008",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9128F18F0002_9700_W9128F14D0024_9700 (Weston Solutions Inc; USACE Maria temporary power). Signed 8 October 2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F18F0002_9700_W9128F14D0024_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F18F0002_9700_W9128F14D0024_9700/",
        "annotation": "USASpending primary: USD 218.4m Maria temporary power. Supports weston_maria_temp_power_2017.",
        "supports": ["weston_maria_temp_power_2017", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# energy/power_plants_grid — WSP Hurricane Maria power transmission install (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "wsp_maria_power_install_2017",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "WSP USA Solutions Inc — USACE Hurricane Maria Puerto Rico power equipment installation",
        "country": "Puerto Rico",
        "asset": "20 Sep 2017: USACE awards delivery order W911WN17F3031 under IDIQ to WSP USA Solutions Inc for Hurricane Maria Puerto Rico response; obligated USD 596,980,875.96; PSC N030 installation of mechanical power transmission equipment; place of performance San Juan. WSP Global HQ Canada — allied. Distinct from WSP Maria non-federal generators and ACI-TEP orders.",
        "investment_type": "epc",
        "value": "596980875.96",
        "currency": "USD",
        "value_usd": "596980875.96",
        "fx_usd": "1",
        "fx_date": "2017-09-20",
        "year": "2017",
        "status": "active",
        "lat": "18.466",
        "lon": "-66.106",
        "geo_note": "Puerto Rico island-wide Maria power response (USASpending PoP San Juan; PSC N030).",
        "evidence": "documented",
        "source_id": "usaspending_wsp_maria_install_20170920",
        "note": "Actor: WSP USA Solutions Inc (WSP Global, Canada HQ) — allied. Official USASpending Award API; PSC N030 power-transmission equipment installation.",
    },
    {
        "id": "wsp_maria_power_install_2017",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_wsp_maria_install_20170920",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W911WN17F3031_9700_W911WN15D0001_9700/",
        "price_year": "2017",
        "evidence": "documented",
        "quote": "HURRICANE MARIA - PUERTO RICO",
        "note": "Opened USASpending Award API: WSP; USD 596,980,875.96; date_signed 2017-09-20; PSC N030.",
    },
    {
        "id": "usaspending_wsp_maria_install_20170920",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W911WN17F3031_9700_W911WN15D0001_9700 (WSP USA Solutions Inc; USACE Hurricane Maria Puerto Rico). Signed 20 September 2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W911WN17F3031_9700_W911WN15D0001_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W911WN17F3031_9700_W911WN15D0001_9700/",
        "annotation": "USASpending primary: USD 597.0m Maria power equipment installation (PSC N030). Supports wsp_maria_power_install_2017.",
        "supports": ["wsp_maria_power_install_2017", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# resources/water — Foresight Guajataca gate repairs 2018 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "foresight_guajataca_gates_2018",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Foresight Construction Group Inc — USACE Guajataca Dam hydraulic high-pressure gate repairs",
        "country": "Puerto Rico",
        "asset": "31 Oct 2018: USACE awards contract W912EP19C0003 to Foresight Construction Group, Inc. for Guajataca Dam hydraulic high-pressure gate repairs; obligated USD 1,106,467.55. Distinct from Del Valle Guajataca Stage 2 / risk reduction and Thompson pumping awards.",
        "investment_type": "epc",
        "value": "1106467.55",
        "currency": "USD",
        "value_usd": "1106467.55",
        "fx_usd": "1",
        "fx_date": "2018-10-31",
        "year": "2018",
        "status": "active",
        "lat": "18.404",
        "lon": "-66.923",
        "geo_note": "Guajataca Dam, northwest Puerto Rico (USASpending award description).",
        "evidence": "documented",
        "source_id": "usaspending_foresight_guajataca_20181031",
        "note": "Actor: Foresight Construction Group Inc (U.S.) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "foresight_guajataca_gates_2018",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_foresight_guajataca_20181031",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP19C0003_9700_-NONE-_-NONE-/",
        "price_year": "2018",
        "evidence": "documented",
        "quote": "GUAJATACA DAM HYDRAULIC HIGH PRESSURE GATE REPAIRS",
        "note": "Opened USASpending Award API: Foresight; USD 1,106,467.55; date_signed 2018-10-31.",
    },
    {
        "id": "usaspending_foresight_guajataca_20181031",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP19C0003_9700_-NONE-_-NONE- (Foresight Construction Group Inc; USACE Guajataca Dam gate repairs). Signed 31 October 2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP19C0003_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP19C0003_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 1.1m Guajataca Dam gate repairs. Supports foresight_guajataca_gates_2018.",
        "supports": ["foresight_guajataca_gates_2018", "hunt_res_water"],
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
        "hunt_infra_building_materials": "Cycle 111: equal budget; Caribbean Lumber dense (miss).",
        "hunt_energy_fission_smr": "Cycle 111: equal budget; CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_fenb_araxa": "Cycle 111: equal budget; CBMM CapEx dense (miss).",
        "hunt_br_power_equip": "Cycle 111: logged weston_maria_temp_power_2017 + wsp_maria_power_install_2017.",
        "hunt_res_water": "Cycle 111: logged foresight_guajataca_gates_2018 (USD 1.1m USACE).",
        "hunt_infra_bridges_roads": "Cycle 111: equal budget; FHWA construction ≥USD 2.5m exhausted (miss).",
        "hunt_infra_port_ownership": "Cycle 111: equal budget; Hutchison / APM dense (miss).",
        "hunt_energy_wind": "Cycle 111: equal budget; Goldwind / Vestas dense (miss).",
        "hunt_energy_other_renewables": "Cycle 111: equal budget; BESS Coya dense (miss).",
        "hunt_infra_port_cranes": "Cycle 111: equal budget; ZPMC Kingston / ICAVE dense (miss).",
        "hunt_res_nickel": "Cycle 111: equal budget; BRN / MMG dense (miss). Thin dry — shift.",
        "hunt_res_graphite": "Cycle 111: equal budget; South Star / Graphcoa dense (miss). Thin dry — shift.",
        "hunt_infra_engineering_epc": "Cycle 111: equal budget; RQ-AECOM Ponce just prior (miss).",
        "hunt_res_lithium": "Cycle 111: equal budget; Ganfeng PPG dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 111: equal budget; CRRC / CRCC dense (miss).",
        "hunt_res_balsa": "Cycle 111: equal budget; Plantabal / WITS dense (miss). Thin dry — shift.",
        "hunt_res_copper": "Cycle 111: equal budget; CMOC Cangrejos dense (miss).",
        "hunt_energy_solar": "Cycle 111: equal budget; Sungrow Atacama/Futura/Helio Valgas dense (miss).",
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
    print("Cycle 111 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
