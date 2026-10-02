#!/usr/bin/env python3
"""Cycle 109 hunt: shuffle_seed=20261109; equal budget; U.S./PRC split; thin after.

Order: fission_smr, balsa, solar, graphite, bridges_roads, power_plants_grid,
copper, lithium, port_ownership, water, other_renewables, niobium, rail,
nickel, building_materials, wind, port_cranes, engineering_epc.
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
# energy/solar — Sungrow Focus Futura I 852 MWp Juazeiro (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sungrow_focus_futura_juazeiro_2021",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Sungrow — inverters and MV stations for Focus Energia Futura I (Juazeiro, BA)",
        "country": "Brazil",
        "asset": "8 Mar 2021 Sungrow: NTP with Focus Energia to supply inverters and MV stations for Futura Project Phase I — 852 MWp solar park (22 parks × 38.73 MWp) ~40 km from Juazeiro, Bahia; installation from Apr 2021; COD targeted 1H 2022. CapEx USD not disclosed. Distinct from Helio Valgas / Aurora / Observatorio rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2021-03-08",
        "year": "2021",
        "status": "active",
        "lat": "-9.450",
        "lon": "-40.500",
        "geo_note": "Futura I solar complex near Juazeiro, Bahia, Brazil (company release; ~40 km from urban center).",
        "evidence": "documented",
        "source_id": "sungrow_futura_juazeiro_20210308",
        "note": "Actor: Sungrow (PRC HQ) — prc; developer Focus Energia (Brazil). Company English primary. CapEx blank.",
    },
    {
        "id": "sungrow_focus_futura_juazeiro_2021",
        "retrieved": "2026-10-02",
        "source_id": "sungrow_futura_juazeiro_20210308",
        "url": "https://en.sungrowpower.com/newsDetail/2169",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "Sungrow will supply inverters and MV stations for the implementation of the first phase of the Futura Project, an 852MWp solar park",
        "note": "Opened Sungrow English newsDetail/2169; dated 8 Mar 2021; CapEx blank.",
    },
    {
        "id": "sungrow_futura_juazeiro_20210308",
        "type": "company",
        "chicago": "Sungrow Power Supply Co., Ltd. “Sungrow Supplies Latin America’s Largest Under Construction PV Plant.” News release, 8 March 2021. https://en.sungrowpower.com/newsDetail/2169.",
        "url": "https://en.sungrowpower.com/newsDetail/2169",
        "annotation": "Company English primary: Futura I 852 MWp near Juazeiro, BA for Focus Energia. Supports sungrow_focus_futura_juazeiro_2021.",
        "supports": ["sungrow_focus_futura_juazeiro_2021", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# energy/other_renewables — Sungrow ENGIE BESS Coya 638 MWh (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sungrow_engie_bess_coya_638mwh_2022",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "Sungrow — 638 MWh liquid-cooled DC-coupled BESS for ENGIE BESS Coya (María Elena)",
        "country": "Chile",
        "asset": "13 Dec 2022 Sungrow: contract with ENGIE to supply 638 MWh DC-coupled liquid-cooled ESS (232 PowerTitan containers) for BESS Coya at the 181.25 MWac Coya Solar PV plant, María Elena district, Antofagasta Region; 5-hour daily dispatch (~200 GWh/year); construction from Dec 2022; commissioning targeted 1Q 2024. CapEx USD not disclosed. Distinct from Sungrow–ENGIE Tocopilla SC2000UD and Aurora BESS rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2022-12-13",
        "year": "2022",
        "status": "active",
        "lat": "-22.350",
        "lon": "-69.650",
        "geo_note": "BESS Coya / Coya Solar plant, María Elena, Antofagasta Region, Chile (company release).",
        "evidence": "documented",
        "source_id": "sungrow_engie_coya_20221213",
        "note": "Actor: Sungrow (PRC HQ) — prc; buyer ENGIE (France) — allied counterpart. Company English primary. CapEx blank.",
    },
    {
        "id": "sungrow_engie_bess_coya_638mwh_2022",
        "retrieved": "2026-10-02",
        "source_id": "sungrow_engie_coya_20221213",
        "url": "https://en.sungrowpower.com/newsDetail/3170",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "forged a contract with ENGIE to supply 638 MWh of its DC-coupled liquid cooled energy storage system (ESS) solution to Chile... BESS Coya, will be located within the 181.25MWac Coya Solar PV Plant in the María Elena district",
        "note": "Opened Sungrow English newsDetail/3170; dated 13 Dec 2022; CapEx blank.",
    },
    {
        "id": "sungrow_engie_coya_20221213",
        "type": "company",
        "chicago": "Sungrow Power Supply Co., Ltd. “Sungrow Forges a Contract with ENGIE to Supply 638 MWh Liquid Cooled Energy Storage System to Chile.” News release, 13 December 2022. https://en.sungrowpower.com/newsDetail/3170.",
        "url": "https://en.sungrowpower.com/newsDetail/3170",
        "annotation": "Company English primary: 638 MWh BESS Coya at ENGIE Coya Solar (María Elena). Supports sungrow_engie_bess_coya_638mwh_2022.",
        "supports": ["sungrow_engie_bess_coya_638mwh_2022", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# energy/power_plants_grid — WSP Maria non-federal generators 2017 (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "wsp_maria_nonfederal_generators_2017",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "WSP USA Solutions Inc — USACE DFA temporary non-federal generators (Hurricane Maria)",
        "country": "Puerto Rico",
        "asset": "6 Oct 2017: USACE awards delivery order W911WN18F3001 under IDIQ to WSP USA Solutions Inc for DFA activities — Hurricane Maria Puerto Rico non-federal generators; obligated USD 22,602,696.93; place of performance San Juan. WSP Global HQ Canada — allied. Distinct from WSP ACI-TEP 2022 temporary emergency power order.",
        "investment_type": "epc",
        "value": "22602696.93",
        "currency": "USD",
        "value_usd": "22602696.93",
        "fx_usd": "1",
        "fx_date": "2017-10-06",
        "year": "2017",
        "status": "active",
        "lat": "18.466",
        "lon": "-66.106",
        "geo_note": "Puerto Rico island-wide non-federal generator DFA (USASpending PoP San Juan).",
        "evidence": "documented",
        "source_id": "usaspending_wsp_maria_gen_20171006",
        "note": "Actor: WSP USA Solutions Inc (WSP Global, Canada HQ) — allied. Official USASpending Award API.",
    },
    {
        "id": "wsp_maria_nonfederal_generators_2017",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_wsp_maria_gen_20171006",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W911WN18F3001_9700_W911WN15D0001_9700/",
        "price_year": "2017",
        "evidence": "documented",
        "quote": "DFA ACTIVITIES FOR HURRICANE MARIA - PUERTO RICO NON FEDERAL GENERATORS",
        "note": "Opened USASpending Award API: WSP; USD 22,602,696.93; date_signed 2017-10-06.",
    },
    {
        "id": "usaspending_wsp_maria_gen_20171006",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W911WN18F3001_9700_W911WN15D0001_9700 (WSP USA Solutions Inc; USACE Maria non-federal generators). Signed 6 October 2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W911WN18F3001_9700_W911WN15D0001_9700/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W911WN18F3001_9700_W911WN15D0001_9700/",
        "annotation": "USASpending primary: USD 22.6m Maria non-federal generators DFA. Supports wsp_maria_nonfederal_generators_2017.",
        "supports": ["wsp_maria_nonfederal_generators_2017", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# resources/water — Thompson Pump Guajataca Dam pumping 2018 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "thompson_guajataca_pumping_2018",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Thompson Pump and Manufacturing Company Inc — USACE Guajataca Dam pumping services",
        "country": "Puerto Rico",
        "asset": "2 Oct 2018: USACE awards contract W912EP19C0001 to Thompson Pump and Manufacturing Company, Inc. for Guajataca Dam pumping services; obligated USD 3,981,815.29; place of performance Aguadilla. Distinct from Del Valle Guajataca Stage 2 spillway and risk-reduction awards.",
        "investment_type": "equipment_supply",
        "value": "3981815.29",
        "currency": "USD",
        "value_usd": "3981815.29",
        "fx_usd": "1",
        "fx_date": "2018-10-02",
        "year": "2018",
        "status": "active",
        "lat": "18.404",
        "lon": "-66.923",
        "geo_note": "Guajataca Dam, northwest Puerto Rico (USASpending PoP Aguadilla).",
        "evidence": "documented",
        "source_id": "usaspending_thompson_guajataca_20181002",
        "note": "Actor: Thompson Pump and Manufacturing Company Inc (U.S. HQ) under USACE — us. Official USASpending Award API.",
    },
    {
        "id": "thompson_guajataca_pumping_2018",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_thompson_guajataca_20181002",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP19C0001_9700_-NONE-_-NONE-/",
        "price_year": "2018",
        "evidence": "documented",
        "quote": "GUAJATACA DAM PUMPING SERVICES",
        "note": "Opened USASpending Award API: Thompson Pump; USD 3,981,815.29; date_signed 2018-10-02.",
    },
    {
        "id": "usaspending_thompson_guajataca_20181002",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_W912EP19C0001_9700_-NONE-_-NONE- (Thompson Pump and Manufacturing Company Inc; USACE Guajataca Dam pumping). Signed 2 October 2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP19C0001_9700_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912EP19C0001_9700_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 4.0m Guajataca Dam pumping. Supports thompson_guajataca_pumping_2018.",
        "supports": ["thompson_guajataca_pumping_2018", "hunt_res_water"],
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
        "hunt_energy_fission_smr": "Cycle 109: equal budget; CAREM / CNNC dense (miss). Thin spare dry.",
        "hunt_res_balsa": "Cycle 109: equal budget; Plantabal / WITS dense (miss). Thin dry — shift.",
        "hunt_energy_solar": "Cycle 109: logged sungrow_focus_futura_juazeiro_2021 (852 MWp Futura I).",
        "hunt_res_graphite": "Cycle 109: equal budget; South Star / Graphcoa dense (miss). Thin dry — shift.",
        "hunt_infra_bridges_roads": "Cycle 109: equal budget; FHWA construction ≥USD 2.5m exhausted (miss).",
        "hunt_br_power_equip": "Cycle 109: logged wsp_maria_nonfederal_generators_2017 (USD 22.6m).",
        "hunt_res_copper": "Cycle 109: equal budget; CMOC Cangrejos dense (miss).",
        "hunt_res_lithium": "Cycle 109: equal budget; Ganfeng PPG dense (miss).",
        "hunt_infra_port_ownership": "Cycle 109: equal budget; Hutchison / APM dense (miss).",
        "hunt_res_water": "Cycle 109: logged thompson_guajataca_pumping_2018 (USD 4.0m USACE).",
        "hunt_energy_other_renewables": "Cycle 109: logged sungrow_engie_bess_coya_638mwh_2022 (638 MWh BESS Coya).",
        "hunt_fenb_araxa": "Cycle 109: equal budget; CBMM CapEx dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 109: equal budget; CRRC / CRCC dense (miss).",
        "hunt_res_nickel": "Cycle 109: equal budget; BRN / MMG dense (miss). Thin dry — shift.",
        "hunt_infra_building_materials": "Cycle 109: equal budget; Caribbean Lumber dense (miss).",
        "hunt_energy_wind": "Cycle 109: equal budget; Goldwind / Vestas dense (miss).",
        "hunt_infra_port_cranes": "Cycle 109: equal budget; ZPMC Kingston / ICAVE dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 109: equal budget; Tutor/RQ-AECOM/Caddell dense (miss).",
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
    print("Cycle 109 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
