#!/usr/bin/env python3
"""Cycle 117 hunt: shuffle_seed=20261117; equal budget; U.S./PRC split; thin after.

Order: niobium, graphite, port_cranes, balsa, rail, nickel, copper,
power_plants_grid, wind, water, fission_smr, other_renewables,
engineering_epc, solar, bridges_roads, lithium, port_ownership,
building_materials.
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


def row_epc(rid, counterpart, country, asset, value, fx_date, year, lat, lon, geo, source_id, quote, url, note, subcat="engineering_epc"):
    layer = "infrastructure"
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcat,
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
            "supports": [rid, f"hunt_infra_{subcat}" if subcat != "engineering_epc" else "hunt_infra_engineering_epc"],
        },
    )


row_epc(
    "bl_harbert_nuevo_laredo_ncc_2014",
    "BL Harbert International LLC — State Dept Nuevo Laredo Consulate Compound",
    "Mexico",
    "27 Sep 2014: Department of State awards contract SAQMMA14C0181 to BL Harbert International LLC for Nuevo Laredo Consulate Compound; obligated USD 108,406,277.00. Distinct from Matamoros NEC and Nogales/Hermosillo NCC awards.",
    "108406277.00",
    "2014-09-27",
    "2014",
    "27.500",
    "-99.510",
    "U.S. Consulate Compound, Nuevo Laredo, Tamaulipas, Mexico (USASpending PoP Mexico).",
    "usaspending_harbert_nuevo_laredo_20140927",
    "NUEVO LAREDO CONSULATE COMPOUND",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA14C0181_1900_-NONE-_-NONE-/",
    "Actor: BL Harbert International (Birmingham AL HQ) under State OBO — us. Official USASpending Award API.",
)

row_epc(
    "jajones_belmopan_nec_2004",
    "J A Jones International LLC — State Dept Belmopan New Embassy Compound",
    "Belize",
    "30 Sep 2004: Department of State awards contract SALMEC04C0027 to J A Jones International Limited Liability Company for New Embassy Compound Belmopan, Belize; obligated USD 50,414,816.75. Distinct from other State OBO LatAm NEC awards.",
    "50414816.75",
    "2004-09-30",
    "2004",
    "17.250",
    "-88.770",
    "New U.S. Embassy Compound, Belmopan, Belize (USASpending PoP Belize).",
    "usaspending_jajones_belmopan_20040930",
    "NEW EMBASSY COMPOUND BELPMOPAN",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC04C0027_1900_-NONE-_-NONE-/",
    "Actor: J A Jones International (U.S.) under State OBO — us. Official USASpending Award API.",
)

row_epc(
    "caddell_tijuana_ncc_2007",
    "Caddell Construction Co. Inc — State Dept Tijuana New Consulate Compound",
    "Mexico",
    "27 Sep 2007: Department of State awards contract SAQMMA07C0056 to Caddell Construction Co., Inc. for design/build New Consulate Compound in Tijuana, Mexico; obligated USD 76,199,999.00. Distinct from later Caddell Mexico City / Guadalajara-area awards.",
    "76199999.00",
    "2007-09-27",
    "2007",
    "32.520",
    "-117.020",
    "New U.S. Consulate Compound, Tijuana, Baja California, Mexico (USASpending PoP Mexico).",
    "usaspending_caddell_tijuana_20070927",
    "DESIGN / BUILD SERVICES FOR TIJUANA, MEXICO NCC.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA07C0056_1900_-NONE-_-NONE-/",
    "Actor: Caddell Construction (Montgomery AL HQ) under State OBO — us. Official USASpending Award API.",
)

row_epc(
    "cce_guayaquil_nab_2008",
    "Contracting Consulting Engineering LLC — State Dept Guayaquil New Office Building",
    "Ecuador",
    "30 Sep 2008: Department of State awards contract SAQMMA08C0245 to Contracting, Consulting, Engineering LLC for Guayaquil, Ecuador New Office Building (NAB); obligated USD 50,275,045.81. Distinct from Caddell/Harbert full NEC awards.",
    "50275045.81",
    "2008-09-30",
    "2008",
    "-2.170",
    "-79.900",
    "U.S. New Office Building / Consulate, Guayaquil, Ecuador (USASpending PoP Ecuador).",
    "usaspending_cce_guayaquil_20080930",
    "GUAYAQUIL, ECUADOR NAB;  AWARD PENDING FUNDS AVAILABILITY.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA08C0245_1900_-NONE-_-NONE-/",
    "Actor: Contracting Consulting Engineering LLC (U.S.) under State OBO — us. Official USASpending Award API.",
)

row_epc(
    "walsh_sj_federal_building_2016",
    "Walsh Puerto Rico LLC — GSA new Federal Building San Juan",
    "Puerto Rico",
    "4 Apr 2016: Public Buildings Service (GSA) awards contract GS02P16AZC7000 to Walsh Puerto Rico, LLC for the new Federal Building project in San Juan, Puerto Rico; obligated USD 81,661,584.68. Distinct from Walsh VA construction awards and Tutor Perini Customs House restoration.",
    "81661584.68",
    "2016-04-04",
    "2016",
    "18.430",
    "-66.070",
    "New Federal Building, San Juan, Puerto Rico (USASpending PoP San Juan).",
    "usaspending_walsh_sj_federal_20160404",
    "AWARD OF THE NEW FEDERAL BUILDING PROJECT IN SAN JUAN, PUERTO RICO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_GS02P16AZC7000_4740_-NONE-_-NONE-/",
    "Actor: Walsh Puerto Rico LLC (Walsh Group / U.S.) under GSA — us. Official USASpending Award API.",
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
        "hunt_fenb_araxa": "Cycle 117: equal budget; CBMM XNO/Araxá dense (miss). Thin niobium dry.",
        "hunt_res_graphite": "Cycle 117: equal budget; Graphcoa Jordânia/Boa Sorte dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 117: equal budget; ZPMC dense (miss).",
        "hunt_res_balsa": "Cycle 117: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_latam_rail_telecom": "Cycle 117: equal budget; CRRC dense (miss).",
        "hunt_res_nickel": "Cycle 117: equal budget; BRN DFC/BNDES dense (miss). Thin dry — shift.",
        "hunt_res_copper": "Cycle 117: equal budget; CMOC dense (miss).",
        "hunt_br_power_equip": "Cycle 117: equal budget; EXIM Guyana GTE dense (miss).",
        "hunt_energy_wind": "Cycle 117: equal budget; Goldwind dense (miss).",
        "hunt_res_water": "Cycle 117: equal budget; Portugués dense (miss).",
        "hunt_energy_fission_smr": "Cycle 117: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_energy_other_renewables": "Cycle 117: equal budget; Trina BESS dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 117: logged bl_harbert_nuevo_laredo_ncc_2014 + jajones_belmopan_nec_2004 + caddell_tijuana_ncc_2007 + cce_guayaquil_nab_2008 + walsh_sj_federal_building_2016.",
        "hunt_energy_solar": "Cycle 117: equal budget; Sungrow Vista Alegre dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 117: equal budget; De Diego dense (miss).",
        "hunt_res_lithium": "Cycle 117: equal budget; Ganfeng dense (miss).",
        "hunt_infra_port_ownership": "Cycle 117: equal budget; COSCO Chancay dense (miss).",
        "hunt_infra_building_materials": "Cycle 117: equal budget; Caribbean Lumber dense (miss).",
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
    print("Cycle 117 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
