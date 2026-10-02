#!/usr/bin/env python3
"""Cycle 106 hunt: shuffle_seed=20261106; equal budget; U.S./PRC split; thin after.

Order: water, solar, graphite, balsa, power_plants_grid, other_renewables,
lithium, copper, fission_smr, wind, niobium, engineering_epc, nickel,
port_ownership, bridges_roads, building_materials, rail, port_cranes.
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
# energy/power_plants_grid — Fluor PREPA T&D 2017 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fluor_pr_transmission_distribution_2017",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Fluor Enterprises Inc — USACE PREPA transmission and distribution restoration",
        "country": "Puerto Rico",
        "asset": "17 Oct 2017: USACE awards delivery order W912DY18F0003 under IDIQ to Fluor Enterprises, Inc. for transmission and distribution restoration (Hurricane Maria / PREPA grid); obligated USD 505,715,895.26; place of performance San Juan. Distinct from PowerSecure grid survey/repair planning award and Weston temporary-power orders.",
        "investment_type": "epc",
        "value": "505715895.26",
        "currency": "USD",
        "value_usd": "505715895.26",
        "fx_usd": "1",
        "fx_date": "2017-10-17",
        "year": "2017",
        "status": "active",
        "lat": "18.466",
        "lon": "-66.106",
        "geo_note": "Puerto Rico PREPA transmission/distribution system (USASpending PoP San Juan; island-wide scope).",
        "evidence": "documented",
        "source_id": "usaspending_fluor_pr_td_20171017",
        "note": "Actor: Fluor Enterprises Inc (Fluor Corp, U.S. HQ) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "fluor_pr_transmission_distribution_2017",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_fluor_pr_td_20171017",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912DY18F0003_9700_W912DY15G0007_9700/",
        "price_year": "2017",
        "evidence": "documented",
        "quote": "TRANSMISSION AND DISTRIBUTION",
        "note": "Opened USASpending Award API: Fluor; USD 505,715,895.26; date_signed 2017-10-17; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_fluor_pr_td_20171017",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912DY18F0003_9700_W912DY15G0007_9700 (Fluor Enterprises Inc; USACE PREPA transmission and distribution). Signed 17 October 2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912DY18F0003_9700_W912DY15G0007_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912DY18F0003_9700_W912DY15G0007_9700/",
        "annotation": "USASpending primary: USD 505.7m PREPA T&D restoration. Supports fluor_pr_transmission_distribution_2017.",
        "supports": ["fluor_pr_transmission_distribution_2017", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# energy/power_plants_grid — PowerSecure PREPA grid survey/repair 2017 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "powersecure_pr_grid_survey_2017",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "PowerSecure Inc — USACE PREPA power-grid survey and repair planning",
        "country": "Puerto Rico",
        "asset": "18 Oct 2017: USACE awards contract W912EP18C0003 to PowerSecure, Inc. for detailed survey and report to determine destruction and plan for repair of the power grid (Hurricane Maria); obligated USD 505,534,662.00; place of performance Dorado. Distinct from Fluor T&D restoration delivery order.",
        "investment_type": "epc",
        "value": "505534662.00",
        "currency": "USD",
        "value_usd": "505534662.00",
        "fx_usd": "1",
        "fx_date": "2017-10-18",
        "year": "2017",
        "status": "active",
        "lat": "18.459",
        "lon": "-66.268",
        "geo_note": "Dorado Municipality, Puerto Rico (USASpending PoP; island-wide PREPA grid survey scope).",
        "evidence": "documented",
        "source_id": "usaspending_powersecure_pr_20171018",
        "note": "Actor: PowerSecure Inc (U.S.; Southern Company affiliate lineage) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "powersecure_pr_grid_survey_2017",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_powersecure_pr_20171018",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP18C0003_9700_-NONE-_-NONE-/",
        "price_year": "2017",
        "evidence": "documented",
        "quote": "DETAILED SURVEY AND REPORT TO DETERMINE THE DESTRUCTION AND PLAN FOR REPAIR OF THE POWER GRID",
        "note": "Opened USASpending Award API: PowerSecure; USD 505,534,662; date_signed 2017-10-18; PoP Dorado, PR.",
    },
    {
        "id": "usaspending_powersecure_pr_20171018",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP18C0003_9700_-NONE-_-NONE- (PowerSecure Inc; USACE PREPA power-grid survey). Signed 18 October 2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP18C0003_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP18C0003_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 505.5m PREPA grid survey/repair planning. Supports powersecure_pr_grid_survey_2017.",
        "supports": ["powersecure_pr_grid_survey_2017", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# resources/water — Del Valle Guajataca Dam Stage 2 2018 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "del_valle_guajataca_stage2_2018",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Del Valle Group LLC — USACE Guajataca Dam Stage 2 spillway and channel reinforcement",
        "country": "Puerto Rico",
        "asset": "12 Sep 2018: USACE awards contract W912EP18C0025 to Del Valle Group LLC for Guajataca Dam Stage 2 spillway and channel reinforcement; obligated USD 17,804,766.14; place of performance Toa Baja (dam site Quebradillas/Isabela corridor). Distinct from Del Valle Río Puerto Nuevo 2D walls and Guajataca risk-reduction award.",
        "investment_type": "epc",
        "value": "17804766.14",
        "currency": "USD",
        "value_usd": "17804766.14",
        "fx_usd": "1",
        "fx_date": "2018-09-12",
        "year": "2018",
        "status": "active",
        "lat": "18.404",
        "lon": "-66.923",
        "geo_note": "Guajataca Dam spillway, northwest Puerto Rico (USASpending PoP Toa Baja administrative; dam geography Quebradillas/Isabela).",
        "evidence": "documented",
        "source_id": "usaspending_del_valle_guajataca_s2_20180912",
        "note": "Actor: Del Valle Group LLC (Puerto Rico / U.S.) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "del_valle_guajataca_stage2_2018",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_del_valle_guajataca_s2_20180912",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP18C0025_9700_-NONE-_-NONE-/",
        "price_year": "2018",
        "evidence": "documented",
        "quote": "GUAJATACA DAM STAGE 2 SPILLWAY AND CHANNEL REINFORCEMENT",
        "note": "Opened USASpending Award API: Del Valle Group; USD 17,804,766.14; date_signed 2018-09-12.",
    },
    {
        "id": "usaspending_del_valle_guajataca_s2_20180912",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP18C0025_9700_-NONE-_-NONE- (Del Valle Group LLC; USACE Guajataca Dam Stage 2). Signed 12 September 2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP18C0025_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP18C0025_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 17.8m Guajataca Dam Stage 2 spillway. Supports del_valle_guajataca_stage2_2018.",
        "supports": ["del_valle_guajataca_stage2_2018", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# resources/water — Del Valle Guajataca risk reduction 2018 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "del_valle_guajataca_risk_2018",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Del Valle Group LLC — USACE Guajataca Dam risk reduction measures",
        "country": "Puerto Rico",
        "asset": "20 Apr 2018: USACE awards contract W912EP18C0013 to Del Valle Group LLC for Guajataca Dam risk reduction measures; obligated USD 5,815,005.41; place of performance Toa Baja. Distinct from Stage 2 spillway reinforcement award.",
        "investment_type": "epc",
        "value": "5815005.41",
        "currency": "USD",
        "value_usd": "5815005.41",
        "fx_usd": "1",
        "fx_date": "2018-04-20",
        "year": "2018",
        "status": "active",
        "lat": "18.404",
        "lon": "-66.923",
        "geo_note": "Guajataca Dam, northwest Puerto Rico (USASpending PoP Toa Baja administrative).",
        "evidence": "documented",
        "source_id": "usaspending_del_valle_guajataca_risk_20180420",
        "note": "Actor: Del Valle Group LLC (Puerto Rico / U.S.) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "del_valle_guajataca_risk_2018",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_del_valle_guajataca_risk_20180420",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP18C0013_9700_-NONE-_-NONE-/",
        "price_year": "2018",
        "evidence": "documented",
        "quote": "GUAJATACA DAM RISK REDUCTION MEASURES",
        "note": "Opened USASpending Award API: Del Valle Group; USD 5,815,005.41; date_signed 2018-04-20.",
    },
    {
        "id": "usaspending_del_valle_guajataca_risk_20180420",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP18C0013_9700_-NONE-_-NONE- (Del Valle Group LLC; USACE Guajataca Dam risk reduction). Signed 20 April 2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP18C0013_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP18C0013_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 5.8m Guajataca Dam risk reduction. Supports del_valle_guajataca_risk_2018.",
        "supports": ["del_valle_guajataca_risk_2018", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# energy/power_plants_grid — WSP ACI-TEP 2022 (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "wsp_aci_tep_pr_2022",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "WSP USA Solutions Inc — USACE Advance Contract Initiative Temporary Emergency Power (ACI-TEP)",
        "country": "Puerto Rico",
        "asset": "14 Sep 2022: USACE awards delivery order W911WN22F3067 under IDIQ to WSP USA Solutions Inc for Advance Contract Initiative – Temporary Emergency Power (ACI-TEP); obligated USD 20,054,659.75; place of performance Coto Laurel. WSP Global HQ Canada — allied. Distinct from WSP Hurricane Maria DFA generator row.",
        "investment_type": "epc",
        "value": "20054659.75",
        "currency": "USD",
        "value_usd": "20054659.75",
        "fx_usd": "1",
        "fx_date": "2022-09-14",
        "year": "2022",
        "status": "active",
        "lat": "18.007",
        "lon": "-66.558",
        "geo_note": "Coto Laurel, Ponce area, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_wsp_aci_tep_20220914",
        "note": "Actor: WSP USA Solutions Inc (WSP Global, Canada HQ) — allied. Official USASpending Award API.",
    },
    {
        "id": "wsp_aci_tep_pr_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_wsp_aci_tep_20220914",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W911WN22F3067_9700_W911WN19D3009_9700/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "ADVANCE CONTRACT INITIATIVE - TEMPORARY EMERGENCY POWER (ACI-TEP)",
        "note": "Opened USASpending Award API: WSP; USD 20,054,659.75; date_signed 2022-09-14; PoP Coto Laurel, PR.",
    },
    {
        "id": "usaspending_wsp_aci_tep_20220914",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W911WN22F3067_9700_W911WN19D3009_9700 (WSP USA Solutions Inc; USACE ACI-TEP). Signed 14 September 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W911WN22F3067_9700_W911WN19D3009_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W911WN22F3067_9700_W911WN19D3009_9700/",
        "annotation": "USASpending primary: USD 20.1m ACI-TEP temporary emergency power. Supports wsp_aci_tep_pr_2022.",
        "supports": ["wsp_aci_tep_pr_2022", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Tutor Perini USCG Río Bayamón 2025 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "tutor_perini_uscg_bayamon_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Tutor Perini Corporation — USCG design/build San Juan hurricane rebuild Río Bayamón Phase 1",
        "country": "Puerto Rico",
        "asset": "15 Jan 2025: U.S. Coast Guard awards task order 70Z04725FPCNI0002 to Tutor Perini Corporation for design/build San Juan hurricane rebuild Río Bayamón at USCG Base San Juan (Phase-1 re-procurement); obligated USD 20,542,009.81; place of performance Bayamón. Distinct from Tutor Perini San Juan Phase II/III waterfront rebuild task orders.",
        "investment_type": "epc",
        "value": "20542009.81",
        "currency": "USD",
        "value_usd": "20542009.81",
        "fx_usd": "1",
        "fx_date": "2025-01-15",
        "year": "2025",
        "status": "active",
        "lat": "18.399",
        "lon": "-66.162",
        "geo_note": "USCG Base San Juan / Río Bayamón corridor, Bayamón–San Juan, Puerto Rico (USASpending PoP Bayamón).",
        "evidence": "documented",
        "source_id": "usaspending_tutor_bayamon_20250115",
        "note": "Actor: Tutor Perini Corporation (U.S. HQ) under USCG — us. Official USASpending Award API.",
    },
    {
        "id": "tutor_perini_uscg_bayamon_2025",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_tutor_bayamon_20250115",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04725FPCNI0002_7008_70Z04723DPCNI0004_7008/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "DESIGN/BUILD SAN JUAN HURRICANE REBUILD RIO BAYAMON AT USCG BASE SAN JUAN, PR (PHASE-1 RE-PROCUREMENT)",
        "note": "Opened USASpending Award API: Tutor Perini; USD 20,542,009.81; date_signed 2025-01-15; PoP Bayamón, PR.",
    },
    {
        "id": "usaspending_tutor_bayamon_20250115",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_70Z04725FPCNI0002_7008_70Z04723DPCNI0004_7008 (Tutor Perini Corporation; USCG Río Bayamón rebuild). Signed 15 January 2025. https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04725FPCNI0002_7008_70Z04723DPCNI0004_7008/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z04725FPCNI0002_7008_70Z04723DPCNI0004_7008/",
        "annotation": "USASpending primary: USD 20.5m USCG Río Bayamón Phase-1 rebuild. Supports tutor_perini_uscg_bayamon_2025.",
        "supports": ["tutor_perini_uscg_bayamon_2025", "hunt_infra_engineering_epc"],
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
        "hunt_res_water": "Cycle 106: logged del_valle_guajataca_stage2_2018 + del_valle_guajataca_risk_2018.",
        "hunt_energy_solar": "Cycle 106: equal budget; TrinaTracker Lagoa do Barro dense (miss).",
        "hunt_res_graphite": "Cycle 106: equal budget; South Star / Graphcoa dense (miss). Thin dry — shift.",
        "hunt_res_balsa": "Cycle 106: equal budget; Plantabal / WITS dense (miss). Thin dry — shift.",
        "hunt_br_power_equip": "Cycle 106: logged fluor_pr_transmission_distribution_2017 + powersecure_pr_grid_survey_2017 + wsp_aci_tep_pr_2022.",
        "hunt_energy_other_renewables": "Cycle 106: equal budget; JC/Schneider ESPC just prior (miss).",
        "hunt_res_lithium": "Cycle 106: equal budget; Ganfeng PPG dense (miss).",
        "hunt_res_copper": "Cycle 106: equal budget; CMOC Cangrejos dense (miss).",
        "hunt_energy_fission_smr": "Cycle 106: equal budget; CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_energy_wind": "Cycle 106: equal budget; Goldwind / Vestas dense (miss).",
        "hunt_fenb_araxa": "Cycle 106: equal budget; CBMM CapEx dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 106: logged tutor_perini_uscg_bayamon_2025 (USCG design/build).",
        "hunt_res_nickel": "Cycle 106: equal budget; BRN / MMG dense (miss). Thin dry — shift.",
        "hunt_infra_port_ownership": "Cycle 106: equal budget; Hutchison / APM dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 106: equal budget; FHWA construction ≥USD 2.5m exhausted (miss).",
        "hunt_infra_building_materials": "Cycle 106: equal budget; Caribbean Lumber VALOR just prior (miss).",
        "hunt_latam_rail_telecom": "Cycle 106: equal budget; CRRC / CRCC dense (miss).",
        "hunt_infra_port_cranes": "Cycle 106: equal budget; ZPMC Kingston / ICAVE dense (miss).",
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
    print("Cycle 106 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
