#!/usr/bin/env python3
"""Cycle 116 hunt: shuffle_seed=20261116; equal budget; U.S./PRC split; thin after.

Order: port_cranes, power_plants_grid, lithium, rail, building_materials, wind,
balsa, bridges_roads, port_ownership, nickel, solar, graphite, copper,
engineering_epc, fission_smr, water, other_renewables, niobium.
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


def row_epc(rid, counterpart, country, asset, value, fx_date, year, lat, lon, geo, source_id, quote, url, note):
    A(
        {
            "id": rid,
            "layer": "infrastructure",
            "subcategory": "engineering_epc",
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
            "chicago": f"U.S. Department of the Treasury, USAspending.gov. Award {url.rsplit('/', 2)[-2]} ({counterpart.split('—')[0].strip()}; {country}). Signed {fx_date}. {url}.",
            "url": url,
            "annotation": f"USASpending primary. Supports {rid}.",
            "supports": [rid, "hunt_infra_engineering_epc"],
        },
    )


row_epc(
    "caddell_panama_city_nec_2004",
    "Caddell Construction Co. Inc — State Dept Panama City New Embassy Compound",
    "Panama",
    "15 Sep 2004: Department of State awards contract SALMEC04C0026 to Caddell Construction Co., Inc. for New Embassy Compound (NEC) Panama City, Panama; obligated USD 70,980,242.32. Distinct from later Caddell LatAm NEC awards.",
    "70980242.32",
    "2004-09-15",
    "2004",
    "8.980",
    "-79.520",
    "New U.S. Embassy Compound, Panama City, Panama (USASpending PoP Panama).",
    "usaspending_caddell_panama_20040915",
    "NEW EMBASSY COMPOUND (NEC) PANAMA CITY, PANAMA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC04C0026_1900_-NONE-_-NONE-/",
    "Actor: Caddell Construction (Montgomery AL HQ) under State OBO — us. Official USASpending Award API.",
)

row_epc(
    "zachry_managua_nec_2004",
    "Zachry International Inc — State Dept Managua New Embassy Compound",
    "Nicaragua",
    "21 Sep 2004: Department of State awards contract SALMEC04C0031 to Zachry International, Inc. for New Embassy Compound (NEC) Managua, Nicaragua; obligated USD 68,335,371.34. Distinct from Caddell/Fluor LatAm NEC awards.",
    "68335371.34",
    "2004-09-21",
    "2004",
    "12.135",
    "-86.250",
    "New U.S. Embassy Compound, Managua, Nicaragua (USASpending PoP Nicaragua).",
    "usaspending_zachry_managua_20040921",
    "NEW EMBASSY COMPOUND (NEC) MANAGUA, NICARAGUA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC04C0031_1900_-NONE-_-NONE-/",
    "Actor: Zachry International (San Antonio TX HQ) under State OBO — us. Official USASpending Award API.",
)

row_epc(
    "bl_harbert_matamoros_nec_2015",
    "BL Harbert International LLC — State Dept Matamoros New Embassy Compound",
    "Mexico",
    "30 Sep 2015: Department of State awards contract SAQMMA15C0250 to BL Harbert International LLC for design and construction of New Embassy Compound in Matamoros, Mexico; obligated USD 124,609,273.54. Distinct from Nuevo Laredo / Nogales NCC awards.",
    "124609273.54",
    "2015-09-30",
    "2015",
    "25.870",
    "-97.505",
    "New U.S. Embassy Compound, Matamoros, Tamaulipas, Mexico (USASpending PoP Mexico).",
    "usaspending_harbert_matamoros_20150930",
    "DESIGN AND CONSTRUCTION OF NEW EMBASSY COMPOUND IN MATAMOROS, MEXICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA15C0250_1900_-NONE-_-NONE-/",
    "Actor: BL Harbert International (Birmingham AL HQ) under State OBO — us. Official USASpending Award API.",
)

row_epc(
    "perini_montevideo_chancery_2017",
    "Perini Management Services Inc — State Dept Montevideo chancery renovation",
    "Uruguay",
    "10 Aug 2017: Department of State awards contract SAQMMA17C0244 to Perini Management Services, Inc. for major chancery renovation at U.S. Embassy Montevideo, Uruguay; obligated USD 125,880,217.37. Distinct from Tutor Perini San Juan Customs / USCG awards.",
    "125880217.37",
    "2017-08-10",
    "2017",
    "-34.910",
    "-56.170",
    "U.S. Embassy Montevideo chancery, Uruguay (USASpending PoP Uruguay).",
    "usaspending_perini_montevideo_20170810",
    "CONSTRUCTION FOR MAJOR CHANCERY RENOVATION AT U.S. EMBASSY MONTEVIDEO, URUGUAY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0244_1900_-NONE-_-NONE-/",
    "Actor: Perini Management Services (Tutor Perini / U.S.) under State OBO — us. Official USASpending Award API.",
)

row_epc(
    "yates_desbuild_monterrey_nec_2009",
    "Yates Desbuild Joint Venture — State Dept Monterrey New Embassy Compound",
    "Mexico",
    "30 Sep 2009: Department of State awards contract SAQMMA09C0282 to Yates Desbuild Joint Venture for New Embassy Compound in Monterrey, Mexico; obligated USD 124,818,874.00. Distinct from BL Harbert Matamoros / Nuevo Laredo awards.",
    "124818874.00",
    "2009-09-30",
    "2009",
    "25.670",
    "-100.310",
    "New U.S. Embassy Compound, Monterrey, Nuevo León, Mexico (USASpending PoP Mexico).",
    "usaspending_yates_monterrey_20090930",
    "NEW EMBASSY COMPOUND - MONTERREY, MEXICO",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA09C0282_1900_-NONE-_-NONE-/",
    "Actor: Yates Desbuild JV (U.S. construction JV) under State OBO — us. Official USASpending Award API.",
)

row_epc(
    "rq_gtmo_jtf_barracks_2019",
    "RQ Construction LLC — NAVFAC JTF barracks NS Guantanamo Bay",
    "Cuba",
    "30 Sep 2019: Department of the Navy awards contract N6945019C1324 to RQ Construction, LLC for JTF barracks at Naval Station Guantanamo Bay, Cuba; obligated USD 82,758,090.73. Distinct from Siemens GTMO LNG ESPC and USCG Borinquen RQ-AECOM awards.",
    "82758090.73",
    "2019-09-30",
    "2019",
    "19.915",
    "-75.125",
    "JTF barracks, Naval Station Guantanamo Bay, Cuba (USASpending PoP Cuba).",
    "usaspending_rq_gtmo_barracks_20190930",
    "JTF BARRACKS, NS GUANTANAMO BAY, CUBA",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945019C1324_9700_-NONE-_-NONE-/",
    "Actor: RQ Construction (Carlsbad CA HQ) under NAVFAC — us. Official USASpending Award API.",
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
        "hunt_infra_port_cranes": "Cycle 116: equal budget; ZPMC Chancay/Manzanillo dense (miss).",
        "hunt_br_power_equip": "Cycle 116: equal budget; Siemens GTMO dense (miss).",
        "hunt_res_lithium": "Cycle 116: equal budget; Ganfeng dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 116: equal budget; CRRC dense (miss).",
        "hunt_infra_building_materials": "Cycle 116: equal budget; Caribbean Lumber dense (miss).",
        "hunt_energy_wind": "Cycle 116: equal budget; Goldwind/SANY dense (miss).",
        "hunt_res_balsa": "Cycle 116: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_infra_bridges_roads": "Cycle 116: equal budget; De Diego/CHEC dense (miss).",
        "hunt_infra_port_ownership": "Cycle 116: equal budget; COSCO Chancay dense (miss).",
        "hunt_res_nickel": "Cycle 116: equal budget; BRN/MMG dense (miss). Thin dry — shift.",
        "hunt_energy_solar": "Cycle 116: equal budget; Sungrow Vista Alegre dense (miss).",
        "hunt_res_graphite": "Cycle 116: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_res_copper": "Cycle 116: equal budget; CMOC dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 116: logged caddell_panama_city_nec_2004 + zachry_managua_nec_2004 + bl_harbert_matamoros_nec_2015 + perini_montevideo_chancery_2017 + yates_desbuild_monterrey_nec_2009 + rq_gtmo_jtf_barracks_2019.",
        "hunt_energy_fission_smr": "Cycle 116: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_res_water": "Cycle 116: equal budget; Portugués dense (miss).",
        "hunt_energy_other_renewables": "Cycle 116: equal budget; Trina BESS dense (miss).",
        "hunt_fenb_araxa": "Cycle 116: equal budget; CBMM dense (miss).",
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
    print("Cycle 116 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
