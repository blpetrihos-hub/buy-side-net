#!/usr/bin/env python3
"""Cycle 103 hunt: shuffle_seed=20261103; equal budget; U.S./PRC split; thin after.

Order: graphite, port_cranes, fission_smr, balsa, niobium, wind, lithium,
power_plants_grid, copper, port_ownership, solar, water, nickel, bridges_roads,
other_renewables, engineering_epc, building_materials, rail.
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
# energy/power_plants_grid — Weston Palo Seco temporary power 2023 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "weston_palo_seco_temp_power_2023",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Weston Solutions Inc — USACE temporary power generation Palo Seco Power Plant",
        "country": "Puerto Rico",
        "asset": "24 Feb 2023: U.S. Army Corps of Engineers awards delivery order W9128F23F0065 under IDIQ to Weston Solutions Inc for temporary power generation at the Palo Seco Power Plant (PR-POWERFY23); obligated USD 816,199,718.54; place of performance San Juan. Distinct from Weston San Juan Power Plant temporary-power order.",
        "investment_type": "epc",
        "value": "816199718.54",
        "currency": "USD",
        "value_usd": "816199718.54",
        "fx_usd": "1",
        "fx_date": "2023-02-24",
        "year": "2023",
        "status": "active",
        "lat": "18.427",
        "lon": "-66.228",
        "geo_note": "Palo Seco Power Plant / Toa Baja–San Juan corridor, Puerto Rico (USASpending PoP San Juan; plant geography approximate).",
        "evidence": "documented",
        "source_id": "usaspending_weston_palo_seco_20230224",
        "note": "Actor: Weston Solutions Inc (U.S. HQ) under USACE award — us. Official USASpending Award API.",
    },
    {
        "id": "weston_palo_seco_temp_power_2023",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_weston_palo_seco_20230224",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F23F0065_9700_W9128F20D0005_9700/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "!!PR-POWERFY23!! TEMPORARY POWER GENERATION AT THE PALO SECO POWER PLANT",
        "note": "Opened USASpending Award API: Weston Solutions; USD 816,199,718.54; date_signed 2023-02-24; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_weston_palo_seco_20230224",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9128F23F0065_9700_W9128F20D0005_9700 (Weston Solutions Inc; USACE temporary power Palo Seco). Signed 24 February 2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F23F0065_9700_W9128F20D0005_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F23F0065_9700_W9128F20D0005_9700/",
        "annotation": "USASpending primary: USD 816.2m USACE temporary power at Palo Seco. Supports weston_palo_seco_temp_power_2023.",
        "supports": ["weston_palo_seco_temp_power_2023", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# energy/power_plants_grid — Weston San Juan temporary power 2023 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "weston_san_juan_temp_power_2023",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Weston Solutions Inc — USACE temporary power generation San Juan Power Plant",
        "country": "Puerto Rico",
        "asset": "10 Apr 2023: USACE awards delivery order W9128F23F0089 under IDIQ to Weston Solutions Inc for temporary power generation at the San Juan Power Plant (PR-POWERFY23); obligated USD 668,946,805.12; place of performance San Juan. Distinct from Palo Seco temporary-power order.",
        "investment_type": "epc",
        "value": "668946805.12",
        "currency": "USD",
        "value_usd": "668946805.12",
        "fx_usd": "1",
        "fx_date": "2023-04-10",
        "year": "2023",
        "status": "active",
        "lat": "18.428",
        "lon": "-66.112",
        "geo_note": "San Juan Power Plant / San Juan Harbor power complex, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_weston_san_juan_20230410",
        "note": "Actor: Weston Solutions Inc (U.S. HQ) under USACE award — us. Official USASpending Award API.",
    },
    {
        "id": "weston_san_juan_temp_power_2023",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_weston_san_juan_20230410",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F23F0089_9700_W9128F20D0005_9700/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "!!PR-POWERFY23!! TEMPORARY POWER GENERATION AT THE SAN JUAN  POWER PLANT",
        "note": "Opened USASpending Award API: Weston Solutions; USD 668,946,805.12; date_signed 2023-04-10; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_weston_san_juan_20230410",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9128F23F0089_9700_W9128F20D0005_9700 (Weston Solutions Inc; USACE temporary power San Juan). Signed 10 April 2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F23F0089_9700_W9128F20D0005_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F23F0089_9700_W9128F20D0005_9700/",
        "annotation": "USASpending primary: USD 668.9m USACE temporary power at San Juan Power Plant. Supports weston_san_juan_temp_power_2023.",
        "supports": ["weston_san_juan_temp_power_2023", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# energy/solar — Sungrow Zelestra Aurora hybrid BESS+PV Chile 2025 (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sungrow_zelestra_aurora_bess_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Sungrow — PowerTitan 2.0 BESS (~1 GWh) + 1+X inverters for Zelestra Aurora hybrid (Tarapacá)",
        "country": "Chile",
        "asset": "19 May 2025 Sungrow: agreement with Zelestra to supply PowerTitan 2.0 liquid-cooled BESS (~1 GWh) and MV PCUs plus 1+X Modular Inverters for the 220 MWdc Aurora hybrid solar+storage project in Tarapacá serving Abastible PPA; BESS deliveries targeted Q4 2025; plant expected ~600 GWh/year. CapEx USD not disclosed. Distinct from prior Sungrow LatAm inverter rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2025-05-19",
        "year": "2025",
        "status": "active",
        "lat": "-20.25",
        "lon": "-69.60",
        "geo_note": "Aurora hybrid project, Tarapacá Region, Chile (company geography; approximate regional pin).",
        "evidence": "documented",
        "source_id": "sungrow_zelestra_aurora_20250519",
        "note": "Actor: Sungrow (PRC HQ) equipment OEM — prc; developer Zelestra (EQT-backed, Spain) — allied counterpart. Company English primary. CapEx blank.",
    },
    {
        "id": "sungrow_zelestra_aurora_bess_2025",
        "retrieved": "2026-10-02",
        "source_id": "sungrow_zelestra_aurora_20250519",
        "url": "https://www.sungrowpower.com/phi/en/newsdetail/6455",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Sungrow will supply its PowerTitan 2.0 liquid-cooled Battery Energy Storage System and their MV Power Conversion Units for the BESS project, which has a storage capacity of approximately 1 GWh. It forms part of the hybrid Aurora scheme in Tarapacá, Chile, which also includes a 220 MWdc solar plant",
        "note": "Opened Sungrow company news: Aurora hybrid 1 GWh BESS + 220 MWdc PV inverter supply; CapEx blank.",
    },
    {
        "id": "sungrow_zelestra_aurora_20250519",
        "type": "company",
        "chicago": "Sungrow. “Zelestra Signs Major BESS Agreement with Sungrow for 1 GWh of Energy Storage at the Aurora Hybrid Project in Chile.” 19 May 2025. https://www.sungrowpower.com/phi/en/newsdetail/6455.",
        "url": "https://www.sungrowpower.com/phi/en/newsdetail/6455",
        "annotation": "Sungrow primary: Aurora Tarapacá ~1 GWh PowerTitan 2.0 + 220 MWdc inverters. Supports sungrow_zelestra_aurora_bess_2025.",
        "supports": ["sungrow_zelestra_aurora_bess_2025", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# resources/water — Ferrovial USACE drilled shaft Type 6C 2024 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ferrovial_usace_drilled_shaft_6c_2024",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Ferrovial Construcción PR LLC — USACE drilled shaft Type 6C (Río Puerto Nuevo program)",
        "country": "Puerto Rico",
        "asset": "9 Apr 2024: USACE awards contract W51DQV24C0002 to Ferrovial Construcción PR, LLC for drilled shaft Type 6C works (Río Puerto Nuevo flood-control program related); obligated USD 150,364,778.62; place of performance San Juan. Distinct from usace_ferrovial_rio_puerto_nuevo_1079m_2026 Supplemental Contract 3.",
        "investment_type": "epc",
        "value": "150364778.62",
        "currency": "USD",
        "value_usd": "150364778.62",
        "fx_usd": "1",
        "fx_date": "2024-04-09",
        "year": "2024",
        "status": "active",
        "lat": "18.41",
        "lon": "-66.07",
        "geo_note": "San Juan / Río Puerto Nuevo flood-control corridor (USASpending PoP San Juan).",
        "evidence": "documented",
        "source_id": "usaspending_ferrovial_shaft6c_20240409",
        "note": "Actor: Ferrovial Construcción PR under USACE Civil Works award — coded us (consistent with usace_ferrovial_rio_puerto_nuevo_1079m_2026). Official USASpending Award API.",
    },
    {
        "id": "ferrovial_usace_drilled_shaft_6c_2024",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_ferrovial_shaft6c_20240409",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W51DQV24C0002_9700_-NONE-_-NONE-/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "DRILLED SHAFT - TYPE 6C",
        "note": "Opened USASpending Award API: Ferrovial Construcción PR; USD 150,364,778.62; date_signed 2024-04-09; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_ferrovial_shaft6c_20240409",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W51DQV24C0002_9700_-NONE-_-NONE- (Ferrovial Construcción PR LLC; USACE drilled shaft Type 6C). Signed 9 April 2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W51DQV24C0002_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W51DQV24C0002_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 150.4m USACE drilled-shaft package. Supports ferrovial_usace_drilled_shaft_6c_2024.",
        "supports": ["ferrovial_usace_drilled_shaft_6c_2024", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# resources/water — Novel Canó Martín Peña CMP-ERP 2025 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "novel_cano_martin_pena_2025",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Novel Construction LLC — USACE Canó Martín Peña Ecosystem Restoration Contract 3 Phase 1",
        "country": "Puerto Rico",
        "asset": "30 Sep 2025: USACE awards contract W51DQV25CA007 to Novel Construction LLC for Canó Martín Peña Ecosystem Restoration Project (CMP-ERP) Contract 3 Phase 1 excavation and stabilization; obligated USD 57,427,000.00; place of performance San Juan. Distinct from Novel FHWA landslide packages.",
        "investment_type": "epc",
        "value": "57427000",
        "currency": "USD",
        "value_usd": "57427000",
        "fx_usd": "1",
        "fx_date": "2025-09-30",
        "year": "2025",
        "status": "active",
        "lat": "18.433",
        "lon": "-66.068",
        "geo_note": "Canó Martín Peña channel, San Juan, Puerto Rico (USASpending PoP / project geography).",
        "evidence": "documented",
        "source_id": "usaspending_novel_cmp_20250930",
        "note": "Actor: Novel Construction LLC (Puerto Rico / U.S.) under USACE award — us. Official USASpending Award API.",
    },
    {
        "id": "novel_cano_martin_pena_2025",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_novel_cmp_20250930",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W51DQV25CA007_9700_-NONE-_-NONE-/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "CANO MARTIN PENA ECOSYSTEM RESTORATION PROJECT (CMP-ERP) CONTRACT 3 PHASE 1, EXCAVATION AND STABILIZATION",
        "note": "Opened USASpending Award API: Novel Construction; USD 57,427,000; date_signed 2025-09-30; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_novel_cmp_20250930",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W51DQV25CA007_9700_-NONE-_-NONE- (Novel Construction LLC; USACE Canó Martín Peña CMP-ERP Contract 3 Phase 1). Signed 30 September 2025. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W51DQV25CA007_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W51DQV25CA007_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 57.4m USACE Canó Martín Peña excavation/stabilization. Supports novel_cano_martin_pena_2025.",
        "supports": ["novel_cano_martin_pena_2025", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Curtin Maritime San Juan Harbor dredging 2023 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "curtin_san_juan_harbor_dredge_2023",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Curtin Maritime Corp — USACE San Juan Harbor construction and maintenance dredging",
        "country": "Puerto Rico",
        "asset": "9 Jun 2023: USACE awards contract W912EP23C0017 to Curtin Maritime Corp for San Juan Harbor construction and maintenance dredging (44-foot and 36-foot project); obligated USD 54,230,767.42; place of performance San Juan. Distinct from FHWA road packages and Río Puerto Nuevo flood-control awards.",
        "investment_type": "epc",
        "value": "54230767.42",
        "currency": "USD",
        "value_usd": "54230767.42",
        "fx_usd": "1",
        "fx_date": "2023-06-09",
        "year": "2023",
        "status": "active",
        "lat": "18.460",
        "lon": "-66.110",
        "geo_note": "San Juan Harbor, Puerto Rico (USASpending PoP / project description).",
        "evidence": "documented",
        "source_id": "usaspending_curtin_sanjuan_20230609",
        "note": "Actor: Curtin Maritime Corp (U.S. HQ) under USACE award — us. Official USASpending Award API.",
    },
    {
        "id": "curtin_san_juan_harbor_dredge_2023",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_curtin_sanjuan_20230609",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP23C0017_9700_-NONE-_-NONE-/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "SAN JUAN HARBOR CONSTRUCTION AND MAINTENANCE DREDGING 44-FOOT AND 36-FOOT PROJECT, SAN JUAN, PUERTO RICO",
        "note": "Opened USASpending Award API: Curtin Maritime; USD 54,230,767.42; date_signed 2023-06-09; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_curtin_sanjuan_20230609",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP23C0017_9700_-NONE-_-NONE- (Curtin Maritime Corp; USACE San Juan Harbor dredging). Signed 9 June 2023. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP23C0017_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP23C0017_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 54.2m San Juan Harbor dredging. Supports curtin_san_juan_harbor_dredge_2023.",
        "supports": ["curtin_san_juan_harbor_dredge_2023", "hunt_infra_engineering_epc"],
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
        "hunt_res_graphite": "Cycle 103: equal budget; South Star / Graphcoa dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 103: equal budget; ZPMC Kingston / ICAVE / Lázaro dense (miss).",
        "hunt_energy_fission_smr": "Cycle 103: equal budget; CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_res_balsa": "Cycle 103: equal budget; Plantabal / WITS dense (miss). Thin dry — shift.",
        "hunt_fenb_araxa": "Cycle 103: equal budget; CBMM CapEx dense (miss).",
        "hunt_energy_wind": "Cycle 103: equal budget; Goldwind / Vestas dense (miss).",
        "hunt_res_lithium": "Cycle 103: equal budget; Ganfeng PPG dense (miss).",
        "hunt_br_power_equip": "Cycle 103: logged weston_palo_seco_temp_power_2023 + weston_san_juan_temp_power_2023 (USACE temporary power).",
        "hunt_res_copper": "Cycle 103: equal budget; CMOC Cangrejos dense (miss).",
        "hunt_infra_port_ownership": "Cycle 103: equal budget; Hutchison / APM dense (miss).",
        "hunt_energy_solar": "Cycle 103: logged sungrow_zelestra_aurora_bess_2025 (Aurora hybrid BESS+PV).",
        "hunt_res_water": "Cycle 103: logged ferrovial_usace_drilled_shaft_6c_2024 + novel_cano_martin_pena_2025.",
        "hunt_res_nickel": "Cycle 103: equal budget; BRN / MMG / Jaguar dense (miss). Thin dry — shift.",
        "hunt_infra_bridges_roads": "Cycle 103: equal budget; FHWA construction ≥USD 2.5m exhausted (miss).",
        "hunt_energy_other_renewables": "Cycle 103: equal budget; dense prior (miss).",
        "hunt_infra_engineering_epc": "Cycle 103: logged curtin_san_juan_harbor_dredge_2023 (USACE dredging).",
        "hunt_infra_building_materials": "Cycle 103: equal budget; Sinoma dense (miss). Thin spare dry.",
        "hunt_latam_rail_telecom": "Cycle 103: equal budget; CRRC / CRCC dense (miss).",
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
    print("Cycle 103 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
