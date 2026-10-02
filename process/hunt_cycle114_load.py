#!/usr/bin/env python3
"""Cycle 114 hunt: shuffle_seed=20261114; equal budget; U.S./PRC split; thin after.

Order: building_materials, nickel, fission_smr, solar, graphite, port_cranes,
engineering_epc, niobium, bridges_roads, balsa, port_ownership,
power_plants_grid, other_renewables, water, copper, wind, lithium, rail.
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
# infrastructure/engineering_epc — BL Harbert Tegucigalpa NEC 2018 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "bl_harbert_tegucigalpa_nec_2018",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "BL Harbert International LLC — State Dept Tegucigalpa New Embassy Compound",
        "country": "Honduras",
        "asset": "23 Sep 2018: Department of State awards contract 19AQMM18C0223 to BL Harbert International LLC for construction of New Embassy Compound (NEC) in Tegucigalpa, Honduras; obligated USD 268,215,569.46. Distinct from Guatemala City NEC and Mexico consulate NCC awards.",
        "investment_type": "epc",
        "value": "268215569.46",
        "currency": "USD",
        "value_usd": "268215569.46",
        "fx_usd": "1",
        "fx_date": "2018-09-23",
        "year": "2018",
        "status": "active",
        "lat": "14.085",
        "lon": "-87.205",
        "geo_note": "New U.S. Embassy Compound, Tegucigalpa, Honduras (USASpending PoP Honduras).",
        "evidence": "documented",
        "source_id": "usaspending_harbert_tegucigalpa_20180923",
        "note": "Actor: BL Harbert International (Birmingham AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "bl_harbert_tegucigalpa_nec_2018",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_harbert_tegucigalpa_20180923",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0223_1900_-NONE-_-NONE-/",
        "price_year": "2018",
        "evidence": "documented",
        "quote": "CONSTRUCTION SERVICES FOR NEW EMBASSY COMPOUND (NEC) IN TEGUCIGALPA, HONDURAS.",
        "note": "Opened USASpending Award API: BL Harbert; USD 268,215,569.46; date_signed 2018-09-23; PoP Honduras.",
    },
    {
        "id": "usaspending_harbert_tegucigalpa_20180923",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0223_1900_-NONE-_-NONE- (BL Harbert International LLC; Tegucigalpa NEC). Signed 23 September 2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0223_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0223_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 268.2m Tegucigalpa NEC. Supports bl_harbert_tegucigalpa_nec_2018.",
        "supports": ["bl_harbert_tegucigalpa_nec_2018", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Caddell Nassau NEC 2018 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "caddell_nassau_nec_2018",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Caddell Construction Co. (DE) LLC — State Dept Nassau New Embassy Compound",
        "country": "Bahamas",
        "asset": "28 Dec 2018: Department of State awards contract 19AQMM19C0026 to Caddell Construction Co. (DE), LLC for design/build New Embassy Compound in Nassau, Bahamas; obligated USD 228,106,169.85 including VAT. Distinct from Mexico City / Brasília / Port of Spain Caddell NECs.",
        "investment_type": "epc",
        "value": "228106169.85",
        "currency": "USD",
        "value_usd": "228106169.85",
        "fx_usd": "1",
        "fx_date": "2018-12-28",
        "year": "2018",
        "status": "active",
        "lat": "25.060",
        "lon": "-77.345",
        "geo_note": "New U.S. Embassy Compound, Nassau, Bahamas (USASpending PoP Bahamas).",
        "evidence": "documented",
        "source_id": "usaspending_caddell_nassau_20181228",
        "note": "Actor: Caddell Construction (Montgomery AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "caddell_nassau_nec_2018",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caddell_nassau_20181228",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0026_1900_-NONE-_-NONE-/",
        "price_year": "2018",
        "evidence": "documented",
        "quote": "DESIGN/BUILD SERVICES FOR THE NEW EMBASSY COMPOUND NASSAU, BAHAMAS.",
        "note": "Opened USASpending Award API: Caddell; USD 228,106,169.85; date_signed 2018-12-28; PoP Bahamas.",
    },
    {
        "id": "usaspending_caddell_nassau_20181228",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM19C0026_1900_-NONE-_-NONE- (Caddell Construction Co. (DE), LLC; Nassau NEC). Signed 28 December 2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0026_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM19C0026_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 228.1m Nassau NEC. Supports caddell_nassau_nec_2018.",
        "supports": ["caddell_nassau_nec_2018", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Caddell Asunción NEC 2017 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "caddell_asuncion_nec_2017",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Caddell Construction Co. (DE) LLC — State Dept Asunción New Embassy Complex",
        "country": "Paraguay",
        "asset": "31 Jan 2017: Department of State awards contract SAQMMA17C0082 to Caddell Construction Co. (DE), LLC for construction of New Embassy Complex (NEC) in Asunción, Paraguay, including early site-work and facility relocation; obligated USD 187,669,691.03. Distinct from other Caddell LatAm NEC awards.",
        "investment_type": "epc",
        "value": "187669691.03",
        "currency": "USD",
        "value_usd": "187669691.03",
        "fx_usd": "1",
        "fx_date": "2017-01-31",
        "year": "2017",
        "status": "active",
        "lat": "-25.285",
        "lon": "-57.575",
        "geo_note": "New U.S. Embassy Complex, Asunción, Paraguay (USASpending PoP Paraguay).",
        "evidence": "documented",
        "source_id": "usaspending_caddell_asuncion_20170131",
        "note": "Actor: Caddell Construction (Montgomery AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "caddell_asuncion_nec_2017",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caddell_asuncion_20170131",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0082_1900_-NONE-_-NONE-/",
        "price_year": "2017",
        "evidence": "documented",
        "quote": "ALL WORK TO CONSTRUCT THE NEW EMBASSY COMPLEX (NEC) IN ASUNCION, PARAGUAY, INCLUDING EARLY SITE-WORK",
        "note": "Opened USASpending Award API: Caddell; USD 187,669,691.03; date_signed 2017-01-31; PoP Paraguay.",
    },
    {
        "id": "usaspending_caddell_asuncion_20170131",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_SAQMMA17C0082_1900_-NONE-_-NONE- (Caddell Construction Co. (DE), LLC; Asunción NEC). Signed 31 January 2017. https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0082_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA17C0082_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 187.7m Asunción NEC. Supports caddell_asuncion_nec_2017.",
        "supports": ["caddell_asuncion_nec_2017", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Caddell Rio Consulate Compound 2022 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "caddell_rio_consulate_2022",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Caddell Construction Co. (DE) LLC — State Dept Rio de Janeiro New Consulate Compound",
        "country": "Brazil",
        "asset": "2 Aug 2022: Department of State awards contract 19AQMM22C0106 to Caddell Construction Co. (DE), LLC for Rio New Consulate Compound; obligated USD 322,420,659.60. Distinct from Brasília NEC (19AQMM22C0102) and other Caddell LatAm awards.",
        "investment_type": "epc",
        "value": "322420659.60",
        "currency": "USD",
        "value_usd": "322420659.60",
        "fx_usd": "1",
        "fx_date": "2022-08-02",
        "year": "2022",
        "status": "active",
        "lat": "-22.910",
        "lon": "-43.175",
        "geo_note": "New U.S. Consulate Compound, Rio de Janeiro, Brazil (USASpending PoP Brazil).",
        "evidence": "documented",
        "source_id": "usaspending_caddell_rio_ncc_20220802",
        "note": "Actor: Caddell Construction (Montgomery AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "caddell_rio_consulate_2022",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_caddell_rio_ncc_20220802",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0106_1900_-NONE-_-NONE-/",
        "price_year": "2022",
        "evidence": "documented",
        "quote": "RIO NEW CONSULATE COMPOUND CONTRACT AWARD",
        "note": "Opened USASpending Award API: Caddell; USD 322,420,659.60; date_signed 2022-08-02; PoP Brazil.",
    },
    {
        "id": "usaspending_caddell_rio_ncc_20220802",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM22C0106_1900_-NONE-_-NONE- (Caddell Construction Co. (DE), LLC; Rio Consulate Compound). Signed 2 August 2022. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0106_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM22C0106_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 322.4m Rio Consulate Compound. Supports caddell_rio_consulate_2022.",
        "supports": ["caddell_rio_consulate_2022", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — BL Harbert Guadalajara NCC 2018 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "bl_harbert_guadalajara_ncc_2018",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "BL Harbert International LLC — State Dept Guadalajara New Consulate Compound",
        "country": "Mexico",
        "asset": "29 Sep 2018: Department of State awards contract 19AQMM18C0246 to BL Harbert International LLC for design-build New Consulate Compound (NCC) in Guadalajara, Mexico; obligated USD 191,636,225.00. Distinct from Hermosillo / Mérida / Nogales NCC awards.",
        "investment_type": "epc",
        "value": "191636225.00",
        "currency": "USD",
        "value_usd": "191636225.00",
        "fx_usd": "1",
        "fx_date": "2018-09-29",
        "year": "2018",
        "status": "active",
        "lat": "20.675",
        "lon": "-103.350",
        "geo_note": "New U.S. Consulate Compound, Guadalajara, Jalisco, Mexico (USASpending PoP Mexico).",
        "evidence": "documented",
        "source_id": "usaspending_harbert_guadalajara_20180929",
        "note": "Actor: BL Harbert International (Birmingham AL HQ) under State OBO — us. Official USASpending Award API.",
    },
    {
        "id": "bl_harbert_guadalajara_ncc_2018",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_harbert_guadalajara_20180929",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0246_1900_-NONE-_-NONE-/",
        "price_year": "2018",
        "evidence": "documented",
        "quote": "DESIGN-BUILD SERVICES FOR NEW CONSULATE COMPOUND, GUADALAJARA, MEXICO",
        "note": "Opened USASpending Award API: BL Harbert; USD 191,636,225.00; date_signed 2018-09-29; PoP Mexico.",
    },
    {
        "id": "usaspending_harbert_guadalajara_20180929",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_19AQMM18C0246_1900_-NONE-_-NONE- (BL Harbert International LLC; Guadalajara NCC). Signed 29 September 2018. https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0246_1900_-NONE-_-NONE-/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_19AQMM18C0246_1900_-NONE-_-NONE-/",
        "annotation": "USASpending primary: USD 191.6m Guadalajara NCC. Supports bl_harbert_guadalajara_ncc_2018.",
        "supports": ["bl_harbert_guadalajara_ncc_2018", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# infrastructure/engineering_epc — Tutor Perini San Juan Customs House 2021 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "tutor_perini_sj_customs_2021",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Tutor Perini Corporation — CBP San Juan Customs House restoration",
        "country": "Puerto Rico",
        "asset": "14 Jan 2021: U.S. Customs and Border Protection awards task order 70B01C21F00000053 under USCG IDIQ to Tutor Perini Corporation for restoration/construction to repair and update the San Juan, PR Customs House; obligated USD 63,587,936.00. Distinct from Tutor Perini USCG San Juan Phase II waterfront rebuild.",
        "investment_type": "epc",
        "value": "63587936.00",
        "currency": "USD",
        "value_usd": "63587936.00",
        "fx_usd": "1",
        "fx_date": "2021-01-14",
        "year": "2021",
        "status": "active",
        "lat": "18.465",
        "lon": "-66.115",
        "geo_note": "U.S. Customs House, Old San Juan, Puerto Rico (USASpending PoP San Juan).",
        "evidence": "documented",
        "source_id": "usaspending_tutor_customs_20210114",
        "note": "Actor: Tutor Perini Corporation (Sylmar CA / U.S. HQ) under CBP — us. Official USASpending Award API.",
    },
    {
        "id": "tutor_perini_sj_customs_2021",
        "retrieved": "2026-10-02",
        "source_id": "usaspending_tutor_customs_20210114",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70B01C21F00000053_7014_70Z04718DTUTPER00_7008/",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "RESTORATION / CONSTRUCTION CONTRACT TO REPAIR AND UPDATE THE SAN JUAN, PR CUSTOMS HOUSE",
        "note": "Opened USASpending Award API: Tutor Perini; USD 63,587,936.00; date_signed 2021-01-14; PoP San Juan, PR.",
    },
    {
        "id": "usaspending_tutor_customs_20210114",
        "type": "government",
        "chicago": "U.S. Department of the Treasury, USAspending.gov. Award CONT_AWD_70B01C21F00000053_7014_70Z04718DTUTPER00_7008 (Tutor Perini Corporation; San Juan Customs House). Signed 14 January 2021. https://api.usaspending.gov/api/v2/awards/CONT_AWD_70B01C21F00000053_7014_70Z04718DTUTPER00_7008/.",
        "url": "https://api.usaspending.gov/api/v2/awards/CONT_AWD_70B01C21F00000053_7014_70Z04718DTUTPER00_7008/",
        "annotation": "USASpending primary: USD 63.6m San Juan Customs House restoration. Supports tutor_perini_sj_customs_2021.",
        "supports": ["tutor_perini_sj_customs_2021", "hunt_infra_engineering_epc"],
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
        "hunt_infra_building_materials": "Cycle 114: equal budget; Caribbean Lumber dense (miss).",
        "hunt_res_nickel": "Cycle 114: equal budget; BRN/MMG dense (miss). Thin dry — shift.",
        "hunt_energy_fission_smr": "Cycle 114: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_energy_solar": "Cycle 114: equal budget; Sungrow Vista Alegre dense (miss).",
        "hunt_res_graphite": "Cycle 114: equal budget; Graphcoa/South Star dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 114: equal budget; ZPMC dense (miss).",
        "hunt_infra_engineering_epc": "Cycle 114: logged bl_harbert_tegucigalpa_nec_2018 + caddell_nassau_nec_2018 + caddell_asuncion_nec_2017 + caddell_rio_consulate_2022 + bl_harbert_guadalajara_ncc_2018 + tutor_perini_sj_customs_2021.",
        "hunt_fenb_araxa": "Cycle 114: equal budget; CBMM dense (miss).",
        "hunt_infra_bridges_roads": "Cycle 114: equal budget; De Diego / CHEC dense (miss).",
        "hunt_res_balsa": "Cycle 114: equal budget; Plantabal/WITS dense (miss). Thin dry — shift.",
        "hunt_infra_port_ownership": "Cycle 114: equal budget; Hutchison/APM dense (miss).",
        "hunt_br_power_equip": "Cycle 114: equal budget; Siemens GTMO dense (miss).",
        "hunt_energy_other_renewables": "Cycle 114: equal budget; Sungrow BESS dense (miss).",
        "hunt_res_water": "Cycle 114: equal budget; Portugués/Ferrovial dense (miss).",
        "hunt_res_copper": "Cycle 114: equal budget; CMOC dense (miss).",
        "hunt_energy_wind": "Cycle 114: equal budget; Goldwind SPIC/Pemuco/Sento Sé dense (miss).",
        "hunt_res_lithium": "Cycle 114: equal budget; Ganfeng dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 114: equal budget; CRRC/CRCC dense (miss).",
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
    print("Cycle 114 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
