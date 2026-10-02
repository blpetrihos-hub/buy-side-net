#!/usr/bin/env python3
"""Cycle 104 hunt: shuffle_seed=20261104; equal budget; U.S./PRC split; thin after.

Order: solar, building_materials, rail, engineering_epc, fission_smr,
power_plants_grid, wind, port_cranes, copper, water, other_renewables,
bridges_roads, port_ownership, nickel, lithium, balsa, graphite, niobium.
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
# energy/solar — TrinaTracker CGN Lagoa do Barro 56.11 MWp (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "trinatracker_cgn_lagoa_barro_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "TrinaTracker Brasil — 1,083 Vanguard 1P trackers for CGN Brasil Lagoa do Barro (Piauí)",
        "country": "Brazil",
        "asset": "26 Aug 2025 Trinasolar EN: TrinaTracker Brasil agreement with CGN Brasil to supply 1,083 Vanguard 1P smart trackers (SuperTrack) for the Lagoa do Barro solar complex in Piauí — installed capacity 56.11 MWp once operational; DDP delivery incl. commissioning/training/O&M support; hybrid solar+wind context serving São Paulo Metro. CapEx USD not disclosed. Distinct from prior Trina Storage BESS and Trina Pillancó/Sidón solar rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2025-08-26",
        "year": "2025",
        "status": "active",
        "lat": "-8.50",
        "lon": "-42.90",
        "geo_note": "Lagoa do Barro solar complex, Piauí, Brazil (company geography; approximate regional pin).",
        "evidence": "documented",
        "source_id": "trina_cgn_lagoa_barro_20250826",
        "note": "Actor: TrinaTracker / Trinasolar (PRC HQ) — prc; buyer CGN Brasil (China General Nuclear subsidiary) — prc counterpart. Company English newsroom primary. CapEx blank.",
    },
    {
        "id": "trinatracker_cgn_lagoa_barro_2025",
        "retrieved": "2026-10-02",
        "source_id": "trina_cgn_lagoa_barro_20250826",
        "url": "https://www.trinasolar.com/en-glb/newsroom202508260552/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "TrinaTracker will deliver 1,083 Vanguard 1P trackers. Once operational, the complex will have an installed capacity of 56.11 MWp",
        "note": "Opened Trinasolar EN newsroom: TrinaTracker–CGN Brasil Lagoa do Barro; datePublished 2025-08-26; CapEx blank.",
    },
    {
        "id": "trina_cgn_lagoa_barro_20250826",
        "type": "company",
        "chicago": "Trinasolar. “TrinaTracker Brasil to Supply Smart Tracking Systems for CGN Brasil’s Lagoa do Barro Solar Project in Piauí.” Newsroom, 26 August 2025. https://www.trinasolar.com/en-glb/newsroom202508260552/.",
        "url": "https://www.trinasolar.com/en-glb/newsroom202508260552/",
        "annotation": "Company English primary: 1,083 Vanguard 1P trackers; 56.11 MWp Lagoa do Barro (Piauí) for CGN Brasil. Supports trinatracker_cgn_lagoa_barro_2025.",
        "supports": ["trinatracker_cgn_lagoa_barro_2025", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — RQ-LORD JV Ramey ARC microgrid (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "rq_lord_ramey_arc_microgrid_2024",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "RQ-LORD JV — USACE Ramey ARC Microgrid ERCIP (Aguadilla)",
        "country": "Puerto Rico",
        "asset": "30 Aug 2024: U.S. Army Corps of Engineers awards definitive contract W912QR24C0029 to RQ-LORD JV for Ramey Army Reserve Center (ARC) Microgrid under ERCIP; obligated USD 19,490,971.86; place of performance Aguadilla. Distinct from Parsons Pesquera ARC microgrid and school/FFE awards at Ramey.",
        "investment_type": "epc",
        "value": "19490971.86",
        "currency": "USD",
        "value_usd": "19490971.86",
        "fx_usd": "1",
        "fx_date": "2024-08-30",
        "year": "2024",
        "status": "active",
        "lat": "18.495",
        "lon": "-67.136",
        "geo_note": "Ramey U.S. Army Reserve Center / former Ramey AFB area, Aguadilla, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_rq_lord_ramey_20240830",
        "note": "Actor: RQ-LORD JV (U.S. construction JV; RQ Construction / LORD lineage) under USACE ERCIP — us. Official USASpending Award API.",
    },
    {
        "id": "rq_lord_ramey_arc_microgrid_2024",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_rq_lord_ramey_20240830",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QR24C0029_9700_-NONE-_-NONE-/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "RAMEY ARC MICROGRID ERCIP",
        "note": "Opened USASpending Award API: RQ-LORD JV; USD 19,490,971.86; date_signed 2024-08-30; PoP Aguadilla, PR.",
    },
    {
        "id": "usaspending_rq_lord_ramey_20240830",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QR24C0029_9700_-NONE-_-NONE- (RQ-LORD JV; USACE Ramey ARC Microgrid ERCIP). Signed 30 August 2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QR24C0029_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QR24C0029_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 19.5m Ramey ARC microgrid. Supports rq_lord_ramey_arc_microgrid_2024.",
        "supports": ["rq_lord_ramey_arc_microgrid_2024", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — Parsons Pesquera ARC microgrid (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "parsons_pesquera_arc_microgrid_2024",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "Parsons Government Services Inc. — LTC Hernan G. Pesquera ARC Microgrid (Juana Díaz)",
        "country": "Puerto Rico",
        "asset": "23 Aug 2024: USACE awards definitive contract W912QR24C0027 to Parsons Government Services Inc. for construction of LTC Hernan G. Pesquera Army Reserve Center microgrid in Juana Díaz; obligated USD 17,158,600.75; place of performance Juana Díaz. Distinct from RQ-LORD Ramey ARC microgrid.",
        "investment_type": "epc",
        "value": "17158600.75",
        "currency": "USD",
        "value_usd": "17158600.75",
        "fx_usd": "1",
        "fx_date": "2024-08-23",
        "year": "2024",
        "status": "active",
        "lat": "18.053",
        "lon": "-66.507",
        "geo_note": "LTC Hernan G. Pesquera USARC, Juana Díaz, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_parsons_pesquera_20240823",
        "note": "Actor: Parsons Government Services Inc. (Parsons Corp, U.S. HQ) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "parsons_pesquera_arc_microgrid_2024",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_parsons_pesquera_20240823",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QR24C0027_9700_-NONE-_-NONE-/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "CONSTRUCTION OF LTC HERNAN G. PESQUERA ARC MICROGRID IN JUANA DIAZ, PUERTO RICO",
        "note": "Opened USASpending Award API: Parsons; USD 17,158,600.75; date_signed 2024-08-23; PoP Juana Díaz, PR.",
    },
    {
        "id": "usaspending_parsons_pesquera_20240823",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912QR24C0027_9700_-NONE-_-NONE- (Parsons Government Services Inc.; USACE Pesquera ARC Microgrid). Signed 23 August 2024. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QR24C0027_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912QR24C0027_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 17.2m Pesquera ARC microgrid. Supports parsons_pesquera_arc_microgrid_2024.",
        "supports": ["parsons_pesquera_arc_microgrid_2024", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — Johnson Controls Fort Buchanan RES task 0003 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "johnson_controls_buchanan_res_0003_2011",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "Johnson Controls Government Systems LLC — Fort Buchanan renewable energy systems (task 0003)",
        "country": "Puerto Rico",
        "asset": "20 Dec 2011: USACE awards delivery order 0003 under IDIQ W912DY09D0017 to Johnson Controls Government Systems, LLC for renewable energy systems at Fort Buchanan (Guaynabo); obligated USD 54,400,926.43; period of performance through Jan 2034 (ESPC-style). Distinct from task 0006 renewable energy systems order and National Guard ESPC row.",
        "investment_type": "epc",
        "value": "54400926.43",
        "currency": "USD",
        "value_usd": "54400926.43",
        "fx_usd": "1",
        "fx_date": "2011-12-20",
        "year": "2011",
        "status": "active",
        "lat": "18.410",
        "lon": "-66.124",
        "geo_note": "Fort Buchanan, Guaynabo, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_jc_buchanan_0003_20111220",
        "note": "Actor: Johnson Controls Government Systems LLC (U.S. HQ) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "johnson_controls_buchanan_res_0003_2011",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_jc_buchanan_0003_20111220",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W912DY09D0017_9700/",
        "price_year": "2011",
        "evidence": "documented",
        "quote": "RENEWABLE ENERGY SYSTEMS",
        "note": "Opened USASpending Award API: Johnson Controls; USD 54,400,926.43; date_signed 2011-12-20; PoP Fort Buchanan / Guaynabo, PR.",
    },
    {
        "id": "usaspending_jc_buchanan_0003_20111220",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0003_9700_W912DY09D0017_9700 (Johnson Controls Government Systems LLC; Fort Buchanan renewable energy systems). Signed 20 December 2011. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W912DY09D0017_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0003_9700_W912DY09D0017_9700/",
        "annotation": "USASpending primary: USD 54.4m Fort Buchanan renewable energy systems. Supports johnson_controls_buchanan_res_0003_2011.",
        "supports": ["johnson_controls_buchanan_res_0003_2011", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — Johnson Controls Fort Buchanan RES task 0006 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "johnson_controls_buchanan_res_0006_2012",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "Johnson Controls Government Systems LLC — Fort Buchanan renewable energy systems (task 0006)",
        "country": "Puerto Rico",
        "asset": "29 Sep 2012: USACE awards delivery order 0006 under IDIQ W912DY09D0017 to Johnson Controls Government Systems, LLC for renewable energy systems at Fort Buchanan (Guaynabo); obligated USD 34,711,619.31; period of performance through Jun 2034. Distinct from task 0003 renewable energy systems order.",
        "investment_type": "epc",
        "value": "34711619.31",
        "currency": "USD",
        "value_usd": "34711619.31",
        "fx_usd": "1",
        "fx_date": "2012-09-29",
        "year": "2012",
        "status": "active",
        "lat": "18.410",
        "lon": "-66.124",
        "geo_note": "Fort Buchanan, Guaynabo, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_jc_buchanan_0006_20120929",
        "note": "Actor: Johnson Controls Government Systems LLC (U.S. HQ) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "johnson_controls_buchanan_res_0006_2012",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_jc_buchanan_0006_20120929",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W912DY09D0017_9700/",
        "price_year": "2012",
        "evidence": "documented",
        "quote": "RENEWABLE ENERGY SYSTEMS",
        "note": "Opened USASpending Award API: Johnson Controls; USD 34,711,619.31; date_signed 2012-09-29; PoP Fort Buchanan / Guaynabo, PR.",
    },
    {
        "id": "usaspending_jc_buchanan_0006_20120929",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0006_9700_W912DY09D0017_9700 (Johnson Controls Government Systems LLC; Fort Buchanan renewable energy systems task 0006). Signed 29 September 2012. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W912DY09D0017_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0006_9700_W912DY09D0017_9700/",
        "annotation": "USASpending primary: USD 34.7m Fort Buchanan renewable energy systems task 0006. Supports johnson_controls_buchanan_res_0006_2012.",
        "supports": ["johnson_controls_buchanan_res_0006_2012", "hunt_energy_other_renewables"],
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
        "hunt_energy_solar": "Cycle 104: logged trinatracker_cgn_lagoa_barro_2025 (CGN Brasil Lagoa do Barro trackers).",
        "hunt_infra_building_materials": "Cycle 104: equal budget; Sinoma / CNBM dense (miss). Thin spare dry.",
        "hunt_latam_rail_telecom": "Cycle 104: equal budget; CRRC / CRCC dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 104: equal budget; Curtin / Jacobs dense (miss).",
        "hunt_energy_fission_smr": "Cycle 104: equal budget; CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_br_power_equip": "Cycle 104: equal budget; Weston Palo Seco/San Juan dense (miss).",
        "hunt_energy_wind": "Cycle 104: equal budget; Goldwind / Vestas dense (miss).",
        "hunt_infra_port_cranes": "Cycle 104: equal budget; ZPMC Kingston / ICAVE dense (miss).",
        "hunt_res_copper": "Cycle 104: equal budget; CMOC Cangrejos dense (miss).",
        "hunt_res_water": "Cycle 104: equal budget; Ferrovial shaft / Novel CMP dense (miss).",
        "hunt_energy_other_renewables": "Cycle 104: logged rq_lord_ramey_arc_microgrid_2024 + parsons_pesquera_arc_microgrid_2024 + johnson_controls_buchanan_res_0003_2011 + johnson_controls_buchanan_res_0006_2012.",
        "hunt_infra_bridges_roads": "Cycle 104: equal budget; FHWA construction ≥USD 2.5m exhausted; USVI out of geography list (miss).",
        "hunt_infra_port_ownership": "Cycle 104: equal budget; Hutchison / APM dense (miss).",
        "hunt_res_nickel": "Cycle 104: equal budget; BRN / MMG dense (miss). Thin dry — shift.",
        "hunt_res_lithium": "Cycle 104: equal budget; Ganfeng PPG dense (miss).",
        "hunt_res_balsa": "Cycle 104: equal budget; Plantabal / WITS dense (miss). Thin dry — shift.",
        "hunt_res_graphite": "Cycle 104: equal budget; South Star / Graphcoa dense (miss). Thin dry — shift.",
        "hunt_fenb_araxa": "Cycle 104: equal budget; CBMM CapEx dense (miss).",
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
    print("Cycle 104 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
