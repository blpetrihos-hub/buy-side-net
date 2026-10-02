#!/usr/bin/env python3
"""Cycle 122 hunt: shuffle_seed=20261122; equal budget; U.S./PRC split; thin after.

Order: copper, building_materials, other_renewables, port_cranes, engineering_epc,
fission_smr, bridges_roads, rail, balsa, niobium, solar, wind, port_ownership,
nickel, graphite, water, lithium, power_plants_grid.
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


def us_row(
    rid,
    layer,
    subcategory,
    counterpart,
    country,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    source_id,
    quote,
    url,
    note,
    hunt_support,
):
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": "us",
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": "epc",
            "value": value,
            "currency": "USD",
            "value_usd": value,
            "fx_usd": "1",
            "fx_date": fx_date,
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": "documented",
            "source_id": source_id,
            "note": note,
        },
        {
            "id": rid,
            "retrieved": "2026-10-02",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": "documented",
            "quote": quote,
            "note": f"Opened USASpending Award API; USD {value}; date_signed {fx_date}.",
        },
        {
            "id": source_id,
            "type": "government",
            "chicago": f"U.S. Department of the Treasury, USAspending.gov. Award supporting {rid}. Signed {fx_date}. {url}.",
            "url": url,
            "annotation": f"USASpending primary. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


us_row(
    "dick_usace_dams_pr_2002",
    "resources",
    "water",
    "Dick Corporation of Puerto Rico, Inc. — USACE construction of dams (San Juan PoP)",
    "Puerto Rico",
    "8 Nov 2002: USACE Jacksonville District awards contract DACW1703C0001 to Dick Corporation of Puerto Rico, Inc. for construction of dams (PSC Y211); obligated USD 78,508,082.00; place of performance San Juan. Distinct from later Río Puerto Nuevo channel/wall packages (Ferrovial/Flatiron/Del Valle/LP C&D).",
    "78508082.00",
    "2002-11-08",
    "2002",
    "",
    "",
    "San Juan, Puerto Rico (USASpending PoP); specific dam name not stated in FPDS dump — lat/lon left blank.",
    "usaspending_dick_dams_pr_20021108",
    "CONSTRUCTION OF DAMS",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_DACW1703C0001_9700_-NONE-_-NONE-/",
    "Actor: Dick Corporation of Puerto Rico under USACE — us. Official USASpending Award API (PSC Y211 Construction of Dams; NAICS 237990).",
    "hunt_res_water",
)

us_row(
    "zachry_ecuador_construction_2005",
    "infrastructure",
    "engineering_epc",
    "Zachry International, Inc. — State Dept Ecuador design & building construction",
    "Ecuador",
    "28 Sep 2005: Department of State awards contract SALMEC05C0035 to Zachry International, Inc. for design & building construction service in Ecuador; obligated USD 73,504,938.33. Distinct from Zachry Managua NEC and later LatAm OBO rows.",
    "73504938.33",
    "2005-09-28",
    "2005",
    "-0.180",
    "-78.470",
    "U.S. diplomatic construction, Ecuador (USASpending PoP Ecuador; Quito approximate for map).",
    "usaspending_zachry_ecuador_20050928",
    "DESIGN & BUILDING CONSTRUCTION SERVICE",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC05C0035_1900_-NONE-_-NONE-/",
    "Actor: Zachry International (U.S.-HQ) under State OBO — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

us_row(
    "caddell_mexico_nec_2005",
    "infrastructure",
    "engineering_epc",
    "Caddell Construction Co., Inc. — State Dept Mexico New Embassy Compound (2005)",
    "Mexico",
    "26 Sep 2005: Department of State awards contract SALMEC05C0043 to Caddell Construction Co., Inc. to construct New Embassy Compound in Mexico; obligated USD 71,000,000.00. Distinct from later Caddell Mexico City NEC SAQMMA17C0287 (2017).",
    "71000000.00",
    "2005-09-26",
    "2005",
    "19.420",
    "-99.170",
    "New U.S. Embassy Compound, Mexico (USASpending PoP Mexico; Mexico City campus approximate).",
    "usaspending_caddell_mexico_nec_20050926",
    "CONSTRUCT NEW EMBASSY COMPOUND.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC05C0043_1900_-NONE-_-NONE-/",
    "Actor: Caddell Construction (Montgomery AL HQ) under State OBO — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

us_row(
    "fluor_jamaica_construction_2003",
    "infrastructure",
    "engineering_epc",
    "Fluor Intercontinental, Inc. — State Dept Jamaica construction services",
    "Jamaica",
    "29 Sep 2003: Department of State awards contract SALMEC03C0030 to Fluor Intercontinental, Inc for construction services in Jamaica; obligated USD 50,651,629.58. Distinct from Fluor Haiti NEC and Fluor Puerto Rico Maria grid-repair awards.",
    "50651629.58",
    "2003-09-29",
    "2003",
    "18.015",
    "-76.745",
    "U.S. diplomatic construction, Jamaica (USASpending PoP Jamaica; Kingston approximate).",
    "usaspending_fluor_jamaica_20030929",
    "CONSTRUCTION SERVICES",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC03C0030_1900_-NONE-_-NONE-/",
    "Actor: Fluor Intercontinental (Fluor Corp Irving TX HQ) under State OBO — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

us_row(
    "vistas_porto_alegre_consulate_2015",
    "infrastructure",
    "engineering_epc",
    "The Vistas Group Global Inc — State Dept Porto Alegre new consulate lease fit-out",
    "Brazil",
    "6 Feb 2015: Department of State awards contract SAQMMA15C0057 to The Vistas Group Global Inc for lease fit-out of new consulate office project in Porto Alegre, Brazil; obligated USD 44,771,420.45. Distinct from Caddell Brasília NEC and Caddell Rio Consulate Compound.",
    "44771420.45",
    "2015-02-06",
    "2015",
    "-30.035",
    "-51.218",
    "New U.S. Consulate office fit-out, Porto Alegre, Brazil (award description).",
    "usaspending_vistas_porto_alegre_20150206",
    "LEASE FIT-OUT NEW CONSULATE OFFICE PROJECT IN PORTO ALEGRE, BRAZIL.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15C0057_1900_-NONE-_-NONE-/",
    "Actor: The Vistas Group Global Inc (U.S.) under State OBO — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

us_row(
    "rb_buchanan_readiness_2012",
    "infrastructure",
    "engineering_epc",
    "R.B. Construction Group, Inc. — USACE Fort Buchanan Readiness Center",
    "Puerto Rico",
    "7 Sep 2012: USACE awards contract W912LR12C0005 to R.B. Construction Group, Inc. for Fort Buchanan Readiness Center; obligated USD 38,429,011.13; place of performance Fort Buchanan. Distinct from PRARNG Joint Training Center Salinas MILCON.",
    "38429011.13",
    "2012-09-07",
    "2012",
    "18.415",
    "-66.122",
    "Fort Buchanan Readiness Center, Guaynabo / San Juan metro, Puerto Rico (USASpending PoP Fort Buchanan).",
    "usaspending_rb_buchanan_20120907",
    "FT BUCHANAN READINESS CENTER",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_W912LR12C0005_9700_-NONE-_-NONE-/",
    "Actor: R.B. Construction Group, Inc. (U.S.) under USACE — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

us_row(
    "qb_munoz_ang_comms_2021",
    "infrastructure",
    "engineering_epc",
    "QB Group LLC — NAVFAC Muñoz ANG communications & contingency response facilities",
    "Puerto Rico",
    "19 Aug 2021: Department of the Navy awards contract N6945021C0031 to QB Group LLC for design and construction of communications facility and contingency response facility at Muñoz Air National Guard Base, Isla Verde, Puerto Rico; obligated USD 37,744,842.89; place of performance Carolina. Distinct from PRARNG Salinas JTC and Fort Buchanan Readiness Center.",
    "37744842.89",
    "2021-08-19",
    "2021",
    "18.457",
    "-66.098",
    "Muñoz Air National Guard Base / Isla Verde, Carolina Municipality, Puerto Rico (USASpending PoP Carolina).",
    "usaspending_qb_munoz_ang_20210819",
    "DESIGN AND CONSTRUCTION CONTRACT FOR COMMUNICATIONS FACILITY AND CONTINGENCY RESPONSE FACILITY AT MUNOZ AIR NATIONAL GUARD BASE ISLA VERDE PUERTO RICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945021C0031_9700_-NONE-_-NONE-/",
    "Actor: QB Group LLC under NAVFAC — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
)

us_row(
    "teksol_pier_echo_2025",
    "infrastructure",
    "engineering_epc",
    "Teksol Integration Group Inc — USCG Sector San Juan Pier Echo Center M&R",
    "Puerto Rico",
    "13 Feb 2025: U.S. Coast Guard awards contract 70Z08225CCEUM0001 to Teksol Integration Group Inc for major maintenance and repair of the wharf Pier Echo Center section at USCG Sector San Juan; obligated USD 3,683,326.00; place of performance San Juan. Distinct from CH2M / Tutor Perini FRC homeporting awards.",
    "3683326.00",
    "2025-02-13",
    "2025",
    "18.464",
    "-66.116",
    "USCG Sector San Juan Pier Echo Center wharf, San Juan, Puerto Rico (USASpending PoP San Juan).",
    "usaspending_teksol_pier_echo_20250213",
    "MAJOR M & R OF THE WHARF PIER ECHO CENTER SECTION AT US COAST GUARD SECTOR SAN JUAN PNUM 13631542",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70Z08225CCEUM0001_7008_-NONE-_-NONE-/",
    "Actor: Teksol Integration Group Inc (Puerto Rico / U.S.) under USCG — us. Official USASpending Award API.",
    "hunt_infra_engineering_epc",
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
        "hunt_res_copper": "Cycle 122: equal budget; CMOC dense (miss).",
        "hunt_infra_building_materials": "Cycle 122: equal budget; Caribbean Lumber dense (miss).",
        "hunt_energy_other_renewables": "Cycle 122: equal budget; OEM product-only pass dry (miss).",
        "hunt_infra_port_cranes": "Cycle 122: equal budget; ZPMC dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 122: logged zachry_ecuador_construction_2005 + caddell_mexico_nec_2005 + fluor_jamaica_construction_2003 + vistas_porto_alegre_consulate_2015 + rb_buchanan_readiness_2012 + qb_munoz_ang_comms_2021 + teksol_pier_echo_2025.",
        "hunt_energy_fission_smr": "Cycle 122: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_infra_bridges_roads": "Cycle 122: equal budget; FHWA Branch residual closed (miss).",
        "hunt_latam_rail_telecom": "Cycle 122: equal budget; CRRC dense (miss).",
        "hunt_res_balsa": "Cycle 122: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_fenb_araxa": "Cycle 122: equal budget; CBMM dense (miss).",
        "hunt_energy_solar": "Cycle 122: equal budget; Sungrow dense (miss).",
        "hunt_energy_wind": "Cycle 122: equal budget; Goldwind dense (miss).",
        "hunt_infra_port_ownership": "Cycle 122: equal budget; COSCO/APM dense (miss).",
        "hunt_res_nickel": "Cycle 122: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_res_graphite": "Cycle 122: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_res_water": "Cycle 122: logged dick_usace_dams_pr_2002.",
        "hunt_res_lithium": "Cycle 122: equal budget; Ganfeng dense (miss).",
        "hunt_br_power_equip": "Cycle 122: equal budget; State Grid/EXIM dense (miss).",
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
    print("Cycle 122 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
