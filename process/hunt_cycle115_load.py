#!/usr/bin/env python3
"""Cycle 115 hunt: shuffle_seed=20261115; equal budget; U.S./PRC split; thin after.

Order: building_materials, power_plants_grid, lithium, port_cranes, bridges_roads,
niobium, copper, fission_smr, engineering_epc, rail, other_renewables, graphite,
solar, water, balsa, wind, port_ownership, nickel.
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


A(
    {
        "id": "bl_harbert_hermosillo_ncc_2018",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "BL Harbert International LLC — State Dept Hermosillo New Consulate Compound",
        "country": "Mexico",
        "asset": "29 Sep 2018: Department of State awards contract 19AQMM18C0235 to BL Harbert International LLC for design/build New Consulate Compound (NCC) in Hermosillo, Mexico; obligated USD 155,799,837.65 including VAT. Distinct from Guadalajara / Mérida / Nogales NCC awards.",
        "investment_type": "epc",
        "value": "155799837.65",
        "currency": "USD",
        "value_usd": "155799837.65",
        "fx_usd": "1",
        "fx_date": "2018-09-29",
        "year": "2018",
        "status": "active",
        "lat": "29.090",
        "lon": "-110.960",
        "geo_note": "New U.S. Consulate Compound, Hermosillo, Sonora, Mexico (USASpending PoP Mexico).",
        "evidence": "documented",
        "source_id": "usaspending_harbert_hermosillo_20180929",
        "note": "Actor: BL Harbert International (Birmingham AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "bl_harbert_hermosillo_ncc_2018",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_harbert_hermosillo_20180929",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0235_1900_-NONE-_-NONE-/",
        "price_year": "2018",
        "evidence": "documented",
        "quote": "DESIGN/BUILD CONSTRUCTION SERVICES FOR HERMOSILLO, MEXICO NEW CONSULATE COMPOUND (NCC).",
        "note": "Opened USASpending: BL Harbert; USD 155,799,837.65; signed 2018-09-29; PoP Mexico.",
    },
    {
        "id": "usaspending_harbert_hermosillo_20180929",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0235_1900_-NONE-_-NONE- (BL Harbert International LLC; Hermosillo NCC). Signed 29 September 2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0235_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0235_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 155.8m Hermosillo NCC. Supports bl_harbert_hermosillo_ncc_2018.",
        "supports": ["bl_harbert_hermosillo_ncc_2018", "hunt_infra_engineering_epc"],
    },
)

A(
    {
        "id": "bl_harbert_merida_ncc_2019",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "BL Harbert International LLC — State Dept Mérida New Consulate Compound",
        "country": "Mexico",
        "asset": "28 Sep 2019: Department of State awards contract 19AQMM19C0161 to BL Harbert International LLC for design-build New Consulate Compound (NCC) in Mérida, Mexico; obligated USD 140,586,214.12. Distinct from Hermosillo / Guadalajara / Nogales NCC awards.",
        "investment_type": "epc",
        "value": "140586214.12",
        "currency": "USD",
        "value_usd": "140586214.12",
        "fx_usd": "1",
        "fx_date": "2019-09-28",
        "year": "2019",
        "status": "active",
        "lat": "20.970",
        "lon": "-89.620",
        "geo_note": "New U.S. Consulate Compound, Mérida, Yucatán, Mexico (USASpending PoP Mexico).",
        "evidence": "documented",
        "source_id": "usaspending_harbert_merida_20190928",
        "note": "Actor: BL Harbert International (Birmingham AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "bl_harbert_merida_ncc_2019",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_harbert_merida_20190928",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0161_1900_-NONE-_-NONE-/",
        "price_year": "2019",
        "evidence": "documented",
        "quote": "DESIGN-BUILD CONSTRUCTION SERVICES FOR THE NEW CONSULATE COMPOUND (NCC) IN MERIDA, MEXICO",
        "note": "Opened USASpending: BL Harbert; USD 140,586,214.12; signed 2019-09-28; PoP Mexico.",
    },
    {
        "id": "usaspending_harbert_merida_20190928",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0161_1900_-NONE-_-NONE- (BL Harbert International LLC; Mérida NCC). Signed 28 September 2019. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0161_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0161_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 140.6m Mérida NCC. Supports bl_harbert_merida_ncc_2019.",
        "supports": ["bl_harbert_merida_ncc_2019", "hunt_infra_engineering_epc"],
    },
)

A(
    {
        "id": "bl_harbert_nogales_ncc_2018",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "BL Harbert International LLC — State Dept Nogales New Consulate Compound",
        "country": "Mexico",
        "asset": "21 Aug 2018: Department of State awards contract 19AQMM18C0092 to BL Harbert International LLC for New Consulate Compound (NCC) in Nogales, Mexico; obligated USD 135,201,167.34. Distinct from Hermosillo / Mérida / Guadalajara NCC awards.",
        "investment_type": "epc",
        "value": "135201167.34",
        "currency": "USD",
        "value_usd": "135201167.34",
        "fx_usd": "1",
        "fx_date": "2018-08-21",
        "year": "2018",
        "status": "active",
        "lat": "31.305",
        "lon": "-110.945",
        "geo_note": "New U.S. Consulate Compound, Nogales, Sonora, Mexico (USASpending PoP Mexico).",
        "evidence": "documented",
        "source_id": "usaspending_harbert_nogales_20180821",
        "note": "Actor: BL Harbert International (Birmingham AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "bl_harbert_nogales_ncc_2018",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_harbert_nogales_20180821",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0092_1900_-NONE-_-NONE-/",
        "price_year": "2018",
        "evidence": "documented",
        "quote": "NCC FOR NOGALES",
        "note": "Opened USASpending: BL Harbert; USD 135,201,167.34; signed 2018-08-21; PoP Mexico.",
    },
    {
        "id": "usaspending_harbert_nogales_20180821",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0092_1900_-NONE-_-NONE- (BL Harbert International LLC; Nogales NCC). Signed 21 August 2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0092_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0092_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 135.2m Nogales NCC. Supports bl_harbert_nogales_ncc_2018.",
        "supports": ["bl_harbert_nogales_ncc_2018", "hunt_infra_engineering_epc"],
    },
)

A(
    {
        "id": "caddell_santo_domingo_nec_2010",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Caddell Construction Co. Inc — State Dept Santo Domingo New Embassy Compound",
        "country": "Dominican Republic",
        "asset": "29 Sep 2010: Department of State awards contract SAQMMA10C0294 to Caddell Construction Co., Inc. for design/build New Embassy Compound in Santo Domingo, Dominican Republic; obligated USD 150,934,461.57. Distinct from later Caddell LatAm NEC awards.",
        "investment_type": "epc",
        "value": "150934461.57",
        "currency": "USD",
        "value_usd": "150934461.57",
        "fx_usd": "1",
        "fx_date": "2010-09-29",
        "year": "2010",
        "status": "active",
        "lat": "18.470",
        "lon": "-69.920",
        "geo_note": "New U.S. Embassy Compound, Santo Domingo, Dominican Republic (USASpending PoP).",
        "evidence": "documented",
        "source_id": "usaspending_caddell_sd_nec_20100929",
        "note": "Actor: Caddell Construction (Montgomery AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "caddell_santo_domingo_nec_2010",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caddell_sd_nec_20100929",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10C0294_1900_-NONE-_-NONE-/",
        "price_year": "2010",
        "evidence": "documented",
        "quote": "DESIGN/BUILD OF NEW EMBASSY COMPOUND FOR SANTO DOMINGO, DOMINICAN REPUBLIC",
        "note": "Opened USASpending: Caddell; USD 150,934,461.57; signed 2010-09-29; PoP Dominican Republic.",
    },
    {
        "id": "usaspending_caddell_sd_nec_20100929",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA10C0294_1900_-NONE-_-NONE- (Caddell Construction Co., Inc.; Santo Domingo NEC). Signed 29 September 2010. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10C0294_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA10C0294_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 150.9m Santo Domingo NEC. Supports caddell_santo_domingo_nec_2010.",
        "supports": ["caddell_santo_domingo_nec_2010", "hunt_infra_engineering_epc"],
    },
)

A(
    {
        "id": "caddell_buenos_aires_sip_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Caddell Construction Co. (DE) LLC — State Dept Buenos Aires selective improvements",
        "country": "Argentina",
        "asset": "6 Feb 2025: Department of State awards contract 19AQMM25C0283 to Caddell Construction Co. (DE), LLC for Buenos Aires, Argentina Selective Improvements Project to provide safe and secure facilities; obligated USD 170,869,147.00. Distinct from full NEC awards elsewhere in LatAm.",
        "investment_type": "epc",
        "value": "170869147.00",
        "currency": "USD",
        "value_usd": "170869147.00",
        "fx_usd": "1",
        "fx_date": "2025-02-06",
        "year": "2025",
        "status": "active",
        "lat": "-34.600",
        "lon": "-58.380",
        "geo_note": "U.S. Embassy Buenos Aires selective improvements, Argentina (USASpending PoP Argentina).",
        "evidence": "documented",
        "source_id": "usaspending_caddell_ba_sip_20250206",
        "note": "Actor: Caddell Construction (Montgomery AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "caddell_buenos_aires_sip_2025",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caddell_ba_sip_20250206",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25C0283_1900_-NONE-_-NONE-/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "BUENOS AIRES, ARGENTINA SELECTIVE IMPROVEMENTS PROJECT TO PROVIDE SAFE AND SECURE FACILITIES.",
        "note": "Opened USASpending: Caddell; USD 170,869,147.00; signed 2025-02-06; PoP Argentina.",
    },
    {
        "id": "usaspending_caddell_ba_sip_20250206",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM25C0283_1900_-NONE-_-NONE- (Caddell Construction Co. (DE), LLC; Buenos Aires SIP). Signed 6 February 2025. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25C0283_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM25C0283_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 170.9m Buenos Aires selective improvements. Supports caddell_buenos_aires_sip_2025.",
        "supports": ["caddell_buenos_aires_sip_2025", "hunt_infra_engineering_epc"],
    },
)

A(
    {
        "id": "fluor_haiti_nec_2005",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Fluor Intercontinental Inc — State Dept Haiti New Embassy Compound",
        "country": "Haiti",
        "asset": "14 Jan 2005: Department of State awards contract SALMEC05C0002 to Fluor Intercontinental, Inc for construction of New Embassy Compound (NEC) project in Haiti; obligated USD 72,262,286.45. Distinct from Fluor Maria grid-repair awards in Puerto Rico.",
        "investment_type": "epc",
        "value": "72262286.45",
        "currency": "USD",
        "value_usd": "72262286.45",
        "fx_usd": "1",
        "fx_date": "2005-01-14",
        "year": "2005",
        "status": "active",
        "lat": "18.540",
        "lon": "-72.335",
        "geo_note": "U.S. Embassy Port-au-Prince / Haiti NEC (USASpending PoP Haiti).",
        "evidence": "documented",
        "source_id": "usaspending_fluor_haiti_nec_20050114",
        "note": "Actor: Fluor Intercontinental (Fluor Corp Irving TX HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "fluor_haiti_nec_2005",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_fluor_haiti_nec_20050114",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC05C0002_1900_-NONE-_-NONE-/",
        "price_year": "2005",
        "evidence": "documented",
        "quote": "CONSTRUCTION OF NEC PROJECT",
        "note": "Opened USASpending: Fluor Intercontinental; USD 72,262,286.45; signed 2005-01-14; PoP Haiti.",
    },
    {
        "id": "usaspending_fluor_haiti_nec_20050114",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SALMEC05C0002_1900_-NONE-_-NONE- (Fluor Intercontinental, Inc; Haiti NEC). Signed 14 January 2005. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC05C0002_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SALMEC05C0002_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 72.3m Haiti NEC. Supports fluor_haiti_nec_2005.",
        "supports": ["fluor_haiti_nec_2005", "hunt_infra_engineering_epc"],
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
        "hunt_infra_building_materials": "Cycle 115: equal budget; Caribbean Lumber dense (miss).",
        "hunt_br_power_equip": "Cycle 115: equal budget; Siemens GTMO dense (miss).",
        "hunt_res_lithium": "Cycle 115: equal budget; Ganfeng dense (miss).",
        "hunt_infra_port_cranes": "Cycle 115: equal budget; ZPMC dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 115: equal budget; De Diego / CHEC dense (miss).",
        "hunt_fenb_araxa": "Cycle 115: equal budget; CBMM dense (miss).",
        "hunt_res_copper": "Cycle 115: equal budget; CMOC dense (miss).",
        "hunt_energy_fission_smr": "Cycle 115: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_infra_engineering_epc": "Cycle 115: logged bl_harbert_hermosillo_ncc_2018 + bl_harbert_merida_ncc_2019 + bl_harbert_nogales_ncc_2018 + caddell_santo_domingo_nec_2010 + caddell_buenos_aires_sip_2025 + fluor_haiti_nec_2005.",
        "hunt_latam_rail_telecom": "Cycle 115: equal budget; CRRC/CRCC dense (miss).",
        "hunt_energy_other_renewables": "Cycle 115: equal budget; Trina Luz del Norte/Alma Sur dense (miss).",
        "hunt_res_graphite": "Cycle 115: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_energy_solar": "Cycle 115: equal budget; Sungrow Vista Alegre dense (miss).",
        "hunt_res_water": "Cycle 115: equal budget; Portugués/Ferrovial dense (miss).",
        "hunt_res_balsa": "Cycle 115: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_energy_wind": "Cycle 115: equal budget; Goldwind dense (miss).",
        "hunt_infra_port_ownership": "Cycle 115: equal budget; Hutchison/APM dense (miss).",
        "hunt_res_nickel": "Cycle 115: equal budget; BRN/MMG dense (miss). Thin dry — shift.",
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
    print("Cycle 115 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
