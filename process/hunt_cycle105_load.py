#!/usr/bin/env python3
"""Cycle 105 hunt: shuffle_seed=20261105; equal budget; U.S./PRC split; thin after.

Order: engineering_epc, wind, port_ownership, water, port_cranes, copper,
fission_smr, lithium, balsa, power_plants_grid, solar, rail, graphite,
nickel, niobium, bridges_roads, other_renewables, building_materials.
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
# energy/power_plants_grid — APTIM Yabucoa temporary power 2017 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "aptim_yabucoa_temp_power_2017",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "APTIM Federal Services LLC — USACE temporary power Yabucoa",
        "country": "Puerto Rico",
        "asset": "7 Nov 2017: USACE awards delivery order W9128F18F0016 under IDIQ to APTIM Federal Services, LLC for temporary power at Yabucoa, Puerto Rico (Hurricane Maria response); obligated USD 54,158,551.65; place of performance Yabucoa. Distinct from Weston Palo Seco/San Juan temporary-power orders.",
        "investment_type": "epc",
        "value": "54158551.65",
        "currency": "USD",
        "value_usd": "54158551.65",
        "fx_usd": "1",
        "fx_date": "2017-11-07",
        "year": "2017",
        "status": "active",
        "lat": "18.050",
        "lon": "-65.879",
        "geo_note": "Yabucoa Municipality, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_aptim_yabucoa_20171107",
        "note": "Actor: APTIM Federal Services LLC (U.S. HQ) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "aptim_yabucoa_temp_power_2017",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_aptim_yabucoa_20171107",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F18F0016_9700_W9128F14D0034_9700/",
        "price_year": "2017",
        "evidence": "documented",
        "quote": "TEMPORARY POWER YABUCOA PUERTO RICO",
        "note": "Opened USASpending Award API: APTIM; USD 54,158,551.65; date_signed 2017-11-07; PoP Yabucoa, PR.",
    },
    {
        "id": "usaspending_aptim_yabucoa_20171107",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W9128F18F0016_9700_W9128F14D0034_9700 (APTIM Federal Services LLC; USACE temporary power Yabucoa). Signed 7 November 2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F18F0016_9700_W9128F14D0034_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W9128F18F0016_9700_W9128F14D0034_9700/",
        "annotation": "USASpending primary: USD 54.2m temporary power Yabucoa. Supports aptim_yabucoa_temp_power_2017.",
        "supports": ["aptim_yabucoa_temp_power_2017", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# resources/water — Flatiron Dragados Puerto Nuevo Bechara 2011 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "flatiron_bechara_puerto_nuevo_2011",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Flatiron Dragados USA Inc. — USACE Puerto Nuevo Bechara Phases 1–2",
        "country": "Puerto Rico",
        "asset": "12 Aug 2011: USACE awards contract W912EP11C0027 to Flatiron Dragados USA, Inc. for Puerto Nuevo Bechara Phases 1 and 2 flood-control works (Río Puerto Nuevo program); obligated USD 43,132,231.70; place of performance San Juan. Distinct from Ferrovial Supplemental Contract 3 / shaft 6C and Del Valle Contract 2D.",
        "investment_type": "epc",
        "value": "43132231.70",
        "currency": "USD",
        "value_usd": "43132231.70",
        "fx_usd": "1",
        "fx_date": "2011-08-12",
        "year": "2011",
        "status": "active",
        "lat": "18.430",
        "lon": "-66.080",
        "geo_note": "Bechara / Puerto Nuevo flood-control area, San Juan, Puerto Rico (USASpending PoP San Juan).",
        "evidence": "documented",
        "source_id": "usaspending_flatiron_bechara_20110812",
        "note": "Actor: Flatiron Dragados USA under USACE Civil Works — coded us (consistent with Ferrovial USACE Río Puerto Nuevo rows). Official USASpending Award API.",
    },
    {
        "id": "flatiron_bechara_puerto_nuevo_2011",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_flatiron_bechara_20110812",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP11C0027_9700_-NONE-_-NONE-/",
        "price_year": "2011",
        "evidence": "documented",
        "quote": "PUERTO NUEVO BECHARA- PHASES 1 AND 2",
        "note": "Opened USASpending Award API: Flatiron Dragados USA; USD 43,132,231.70; date_signed 2011-08-12; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_flatiron_bechara_20110812",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP11C0027_9700_-NONE-_-NONE- (Flatiron Dragados USA Inc.; USACE Puerto Nuevo Bechara). Signed 12 August 2011. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP11C0027_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP11C0027_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 43.1m Puerto Nuevo Bechara Phases 1–2. Supports flatiron_bechara_puerto_nuevo_2011.",
        "supports": ["flatiron_bechara_puerto_nuevo_2011", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# resources/water — Del Valle Río Puerto Nuevo Contract 2D walls 2017 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "del_valle_rpn_2d_walls_2017",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Del Valle Group LLC — USACE Río Puerto Nuevo Contract 2D walls",
        "country": "Puerto Rico",
        "asset": "21 Feb 2017: USACE awards contract W912EP17C0009 to Del Valle Group LLC for Río Puerto Nuevo Contract 2D walls (flood-control program); obligated USD 23,969,754.00; place of performance San Juan. Distinct from Flatiron Bechara / Ferrovial shaft 6C / Supplemental Contract 3.",
        "investment_type": "epc",
        "value": "23969754.00",
        "currency": "USD",
        "value_usd": "23969754.00",
        "fx_usd": "1",
        "fx_date": "2017-02-21",
        "year": "2017",
        "status": "active",
        "lat": "18.415",
        "lon": "-66.075",
        "geo_note": "Río Puerto Nuevo flood-control corridor, San Juan, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_del_valle_rpn_2d_20170221",
        "note": "Actor: Del Valle Group LLC (Puerto Rico / U.S.) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "del_valle_rpn_2d_walls_2017",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_del_valle_rpn_2d_20170221",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP17C0009_9700_-NONE-_-NONE-/",
        "price_year": "2017",
        "evidence": "documented",
        "quote": "RIO PUERTO NUEVO CONTRACT 2D WALLS; PART OF RIO PUERTO FLOOD CONTROL",
        "note": "Opened USASpending Award API: Del Valle Group; USD 23,969,754; date_signed 2017-02-21; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_del_valle_rpn_2d_20170221",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP17C0009_9700_-NONE-_-NONE- (Del Valle Group LLC; USACE Río Puerto Nuevo Contract 2D). Signed 21 February 2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP17C0009_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP17C0009_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 24.0m Río Puerto Nuevo Contract 2D walls. Supports del_valle_rpn_2d_walls_2017.",
        "supports": ["del_valle_rpn_2d_walls_2017", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# resources/water — LP C&D Upper Margarita channel 2014 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "lpcd_rpn_margarita_2014",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "LP C & D Inc — USACE Río Puerto Nuevo Upper Margarita channel / stilling basin",
        "country": "Puerto Rico",
        "asset": "13 Aug 2014: USACE awards contract W912EP14C0021 to LP C & D Inc for Río Puerto Nuevo Upper Margarita channel and stilling basin (U-framed concrete stilling basin, transition channel, chute); obligated USD 21,163,163.98; place of performance San Juan. Distinct from Del Valle 2D / Flatiron Bechara / Ferrovial rows.",
        "investment_type": "epc",
        "value": "21163163.98",
        "currency": "USD",
        "value_usd": "21163163.98",
        "fx_usd": "1",
        "fx_date": "2014-08-13",
        "year": "2014",
        "status": "active",
        "lat": "18.405",
        "lon": "-66.070",
        "geo_note": "Upper Margarita channel / Río Puerto Nuevo, San Juan, Puerto Rico (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_lpcd_margarita_20140813",
        "note": "Actor: LP C & D Inc (Puerto Rico / U.S.) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "lpcd_rpn_margarita_2014",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_lpcd_margarita_20140813",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP14C0021_9700_-NONE-_-NONE-/",
        "price_year": "2014",
        "evidence": "documented",
        "quote": "RIO PUERTO NUEVO UPPER MARGARITA CHANNEL AND STILING BASIN",
        "note": "Opened USASpending Award API: LP C & D; USD 21,163,163.98; date_signed 2014-08-13; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_lpcd_margarita_20140813",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP14C0021_9700_-NONE-_-NONE- (LP C & D Inc; USACE Upper Margarita channel). Signed 13 August 2014. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP14C0021_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP14C0021_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 21.2m Upper Margarita channel/stilling basin. Supports lpcd_rpn_margarita_2014.",
        "supports": ["lpcd_rpn_margarita_2014", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — Johnson Controls PR National Guard ESPC 2014 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "johnson_controls_prng_espc_2014",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "Johnson Controls Government Systems LLC — ESPC Puerto Rico National Guard",
        "country": "Puerto Rico",
        "asset": "30 Sep 2014: USACE awards delivery order 0016 under IDIQ W912DY09D0017 to Johnson Controls Government Systems, LLC for Energy Savings Performance Contract (ESPC) at Puerto Rico National Guard; obligated USD 29,334,021.11; place of performance San Juan. Distinct from Fort Buchanan renewable energy systems tasks 0003/0006.",
        "investment_type": "epc",
        "value": "29334021.11",
        "currency": "USD",
        "value_usd": "29334021.11",
        "fx_usd": "1",
        "fx_date": "2014-09-30",
        "year": "2014",
        "status": "active",
        "lat": "18.430",
        "lon": "-66.120",
        "geo_note": "Puerto Rico National Guard facilities, San Juan area (USASpending PoP San Juan).",
        "evidence": "documented",
        "source_id": "usaspending_jc_prng_espc_20140930",
        "note": "Actor: Johnson Controls Government Systems LLC (U.S. HQ) under USACE ESPC — us. Official USASpending Award API.",
    },
    {
        "id": "johnson_controls_prng_espc_2014",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_jc_prng_espc_20140930",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0016_9700_W912DY09D0017_9700/",
        "price_year": "2014",
        "evidence": "documented",
        "quote": "ESPC AT PUERTO RICO NATIONAL GUARD",
        "note": "Opened USASpending Award API: Johnson Controls; USD 29,334,021.11; date_signed 2014-09-30; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_jc_prng_espc_20140930",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_0016_9700_W912DY09D0017_9700 (Johnson Controls Government Systems LLC; ESPC Puerto Rico National Guard). Signed 30 September 2014. https://api.usaspending.gov/api/v2/awards/CONT_AWD_0016_9700_W912DY09D0017_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_0016_9700_W912DY09D0017_9700/",
        "annotation": "USASpending primary: USD 29.3m PR National Guard ESPC. Supports johnson_controls_prng_espc_2014.",
        "supports": ["johnson_controls_prng_espc_2014", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/building_materials — Caribbean Lumber VALOR materials 2018 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "caribbean_lumber_valor_materials_2018",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "us",
        "counterpart": "Caribbean Lumber & Hardware Inc — FEMA VALOR building materials (Hurricane Maria)",
        "country": "Puerto Rico",
        "asset": "12 Jan 2018: FEMA awards delivery order 70FBR218F00000028 under IDIQ to Caribbean Lumber & Hardware, Inc. for purchase of building materials from a local small business to augment VOAD inventory under the VALOR program (minor home repairs / make-safe); obligated USD 23,187,330.07; place of performance San Juan. Distinct from Sinoma/CNBM cement OEM rows.",
        "investment_type": "equipment_supply",
        "value": "23187330.07",
        "currency": "USD",
        "value_usd": "23187330.07",
        "fx_usd": "1",
        "fx_date": "2018-01-12",
        "year": "2018",
        "status": "active",
        "lat": "18.466",
        "lon": "-66.106",
        "geo_note": "San Juan, Puerto Rico (USASpending PoP; island-wide VALOR distribution).",
        "evidence": "documented",
        "source_id": "usaspending_caribbean_lumber_20180112",
        "note": "Actor: Caribbean Lumber & Hardware Inc (Puerto Rico / U.S.) under FEMA — us. Building materials supply. Official USASpending Award API.",
    },
    {
        "id": "caribbean_lumber_valor_materials_2018",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caribbean_lumber_20180112",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70FBR218F00000028_7022_70FBR218D00000003_7022/",
        "price_year": "2018",
        "evidence": "documented",
        "quote": "PURCHASE OF BUILDING MATERIAL FROM LOCAL SMALL BUSINESS TO AUGMENT THE VOAD'S INVENTORY",
        "note": "Opened USASpending Award API: Caribbean Lumber; USD 23,187,330.07; date_signed 2018-01-12; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_caribbean_lumber_20180112",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_70FBR218F00000028_7022_70FBR218D00000003_7022 (Caribbean Lumber & Hardware Inc; FEMA VALOR building materials). Signed 12 January 2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_70FBR218F00000028_7022_70FBR218D00000003_7022/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70FBR218F00000028_7022_70FBR218D00000003_7022/",
        "annotation": "USASpending primary: USD 23.2m VALOR building materials. Supports caribbean_lumber_valor_materials_2018.",
        "supports": ["caribbean_lumber_valor_materials_2018", "hunt_infra_building_materials"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — Schneider Electric ESPC cool roofs PR 2010 (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "schneider_espc_pr_cool_roofs_2010",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "allied",
        "counterpart": "Schneider Electric Buildings Americas Inc — ESPC cool roofs / utility rate (USCG PR)",
        "country": "Puerto Rico",
        "asset": "17 Dec 2010: U.S. Coast Guard awards order HSCG8311JPMV073 to Schneider Electric Buildings Americas, Inc. for Energy Savings Performance Contract ECM 6 (cool roofs) and ECM 15 (utility rate/RESA) at various units in Puerto Rico; obligated USD 54,242,727.51; place of performance San Juan. Schneider Electric Group HQ France — allied. Distinct from Johnson Controls Fort Buchanan / PRNG ESPC rows.",
        "investment_type": "epc",
        "value": "54242727.51",
        "currency": "USD",
        "value_usd": "54242727.51",
        "fx_usd": "1",
        "fx_date": "2010-12-17",
        "year": "2010",
        "status": "active",
        "lat": "18.466",
        "lon": "-66.106",
        "geo_note": "Various U.S. Coast Guard units in Puerto Rico (USASpending PoP San Juan).",
        "evidence": "documented",
        "source_id": "usaspending_schneider_espc_pr_20101217",
        "note": "Actor: Schneider Electric Buildings Americas (Schneider Electric SE, France HQ) — allied. Official USASpending Award API.",
    },
    {
        "id": "schneider_espc_pr_cool_roofs_2010",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_schneider_espc_pr_20101217",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_HSCG8311JPMV073_7008_DEAM3609GO29042_8900/",
        "price_year": "2010",
        "evidence": "documented",
        "quote": "ENERGY SAVINGS PERFORMANCE CONTRACT (ESPC) FOR ECM 6 - COOL ROOFS&ECM 15 - UTILITY RATE (RESA) AT VARIOUS UNITS IN PUERTO RICO",
        "note": "Opened USASpending Award API: Schneider Electric Buildings Americas; USD 54,242,727.51; date_signed 2010-12-17; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_schneider_espc_pr_20101217",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_HSCG8311JPMV073_7008_DEAM3609GO29042_8900 (Schneider Electric Buildings Americas Inc; ESPC cool roofs Puerto Rico). Signed 17 December 2010. https://api.usaspending.gov/api/v2/awards/CONT_AWD_HSCG8311JPMV073_7008_DEAM3609GO29042_8900/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_HSCG8311JPMV073_7008_DEAM3609GO29042_8900/",
        "annotation": "USASpending primary: USD 54.2m Schneider ESPC cool roofs/utility rate PR. Supports schneider_espc_pr_cool_roofs_2010.",
        "supports": ["schneider_espc_pr_cool_roofs_2010", "hunt_energy_other_renewables"],
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
        "hunt_infra_engineering_epc": "Cycle 105: equal budget; Curtin / Jacobs dense (miss).",
        "hunt_energy_wind": "Cycle 105: equal budget; Goldwind / Vestas dense (miss).",
        "hunt_infra_port_ownership": "Cycle 105: equal budget; Hutchison / APM dense (miss).",
        "hunt_res_water": "Cycle 105: logged flatiron_bechara_puerto_nuevo_2011 + del_valle_rpn_2d_walls_2017 + lpcd_rpn_margarita_2014.",
        "hunt_infra_port_cranes": "Cycle 105: equal budget; ZPMC Kingston / ICAVE dense (miss).",
        "hunt_res_copper": "Cycle 105: equal budget; CMOC Cangrejos dense (miss).",
        "hunt_energy_fission_smr": "Cycle 105: equal budget; CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_res_lithium": "Cycle 105: equal budget; Ganfeng PPG dense (miss).",
        "hunt_res_balsa": "Cycle 105: equal budget; Plantabal / WITS dense (miss). Thin dry — shift.",
        "hunt_br_power_equip": "Cycle 105: logged aptim_yabucoa_temp_power_2017 (USACE temporary power).",
        "hunt_energy_solar": "Cycle 105: equal budget; TrinaTracker Lagoa do Barro just prior (miss).",
        "hunt_latam_rail_telecom": "Cycle 105: equal budget; CRRC / CRCC dense (miss).",
        "hunt_res_graphite": "Cycle 105: equal budget; South Star / Graphcoa dense (miss). Thin dry — shift.",
        "hunt_res_nickel": "Cycle 105: equal budget; BRN / MMG dense (miss). Thin dry — shift.",
        "hunt_fenb_araxa": "Cycle 105: equal budget; CBMM CapEx dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 105: equal budget; FHWA construction ≥USD 2.5m exhausted (miss).",
        "hunt_energy_other_renewables": "Cycle 105: logged johnson_controls_prng_espc_2014 + schneider_espc_pr_cool_roofs_2010.",
        "hunt_infra_building_materials": "Cycle 105: logged caribbean_lumber_valor_materials_2018 (FEMA VALOR).",
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
    print("Cycle 105 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
