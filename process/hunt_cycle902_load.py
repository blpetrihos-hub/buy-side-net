#!/usr/bin/env python3
"""Cycle 902 hunt: shuffle_seed=20261902; USASpending Haiti US CapEx + PIP mini-réseau.

Shuffle: other_renewables, building_materials, graphite, solar, lithium, nickel, rail,
port_ownership, power_plants_grid, wind, niobium, copper, engineering_epc, balsa,
fission_smr, bridges_roads, port_cranes, water.

Thin top-up balsa/nickel/fission_smr dry.
US: NEW GDG Cap-Haïtien DRW + CCE La Pointe/Caracol DB + DFS Caracol drainage +
UTE PPSELD T&D materials. ALLIED: Haiti PIP mini-réseau CDB.
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

PIP_URL = "https://docs.haitidocs.org/mpce-pip-2025-2026-adopte-cdm.pdf"
PIP_SID = "haiti_mpce_pip_fy2025_2026"
PIP_CHICAGO = (
    "République d'Haïti, Ministère de la Planification et de la Coopération Externe. "
    "“Programmes d'Investissements Publics — Exercice 2025-2026.” Budget Général de la "
    f"République d'Haïti. Retrieved October 5, 2026. {PIP_URL}."
)


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid,
    layer,
    subcategory,
    side,
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
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd=None,
    fx_usd=None,
    chicago=None,
    bib_type="government",
    annotation=None,
    evid_note=None,
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": investment_type,
            "value": value,
            "currency": currency,
            "value_usd": value_usd,
            "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "",
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": evidence,
            "source_id": source_id,
            "note": note,
            "pair_id": "",
            "counterpart_side": "",
            "counterpart_actor": "",
            "counterpart_value": "",
            "counterpart_currency": "",
            "counterpart_value_usd": "",
            "gap": "",
        },
        {
            "id": rid,
            "retrieved": "2026-10-05",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": evidence,
            "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id,
            "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url,
            "accessed": "2026-10-05",
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. building_materials / us — GDG Cap-Haïtien DRW
row_doc(
    "gdg_cap_haitien_drw_1p27m_2010",
    "infrastructure",
    "building_materials",
    "us",
    "GDG Beton & Construction (GDC Constructors) — Cap-Haïtien Disaster Relief Warehouse",
    "Haiti",
    "31 Aug 2010: DoD awards contract N6945010C0036 to GDG Beton & Construction S.A. "
    "(subsidiary of GDC Constructors Inc.) to design and construct a Disaster Relief "
    "Warehouse (DRW) in Cap-Haïtien, Haiti; obligated USD 1,274,791.96. CapEx face = "
    "award obligation. Distinct from trigon_cap_haitien_port_cm_43m / fluor_haiti_nec_2005.",
    "1274791.96",
    "2010-08-31",
    "2010",
    "19.760",
    "-72.200",
    "Cap-Haïtien Disaster Relief Warehouse, Nord, Haiti (USASpending PoP Haiti; Cap-Haïtien pin).",
    "usaspending_gdg_cap_haitien_drw_20100831",
    "DESIGN AND CONSTRUCT DISASTER RELIEF WAREHOUSE (DRW) IN CAP-HAITIEN, HAITI",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0036_9700_-NONE-_-NONE-/",
    "Actor: GDG Beton & Construction S.A. (subsidiary of GDC Constructors Inc., U.S.) under DoD — us. "
    "Official USASpending Award API. Shuffle building_materials; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle902",
    investment_type="epc",
    chicago=(
        "U.S. Department of the Treasury, USAspending.gov. Award "
        "CONT_AWD_N6945010C0036_9700_-NONE-_-NONE- (GDG Beton & Construction S.A.; Cap-Haïtien DRW). "
        "Signed 31 August 2010. "
        "https://api.usaspending.gov/api/v2/awards/CONT_AWD_N6945010C0036_9700_-NONE-_-NONE-/."
    ),
    annotation="USASpending: GDG Cap-Haïtien DRW USD 1.275m. Supports gdg_cap_haitien_drw_1p27m_2010.",
    evid_note="Opened USASpending Award API 2026-10-05; total_obligation USD 1,274,791.96; date_signed 2010-08-31.",
)

# 2. engineering_epc / us — CCE La Pointe / Caracol design-build
row_doc(
    "cce_lapointe_caracol_infra_6p8m_2012",
    "infrastructure",
    "engineering_epc",
    "us",
    "Contracting Consulting Engineering LLC — La Pointe / Caracol infrastructure design-build",
    "Haiti",
    "17 May 2012: Department of State awards order SAQMMA12F1738 to Contracting, Consulting, "
    "Engineering LLC for design-build infrastructure services at La Pointe and Caracol, Haiti; "
    "obligated USD 6,802,661.17. CapEx face = award obligation. Distinct from "
    "nreca_caracol_power_2013 / dfs_caracol_drainage_13p6m_2015.",
    "6802661.17",
    "2012-05-17",
    "2012",
    "19.740",
    "-72.020",
    "La Pointe / Caracol corridor, Nord-Est, Haiti (USASpending PoP Haiti; Caracol approximate).",
    "usaspending_cce_lapointe_caracol_20120517",
    "DESIGN BUILD SERVICES FOR INFRASTRUCTURE PROJECT IN LA POINTE AND CARACOL HAITI.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1738_1900_SAQMMA08D0003_1900/",
    "Actor: Contracting, Consulting, Engineering LLC (U.S.) under State OAM — us. "
    "Official USASpending Award API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle902",
    investment_type="epc",
    chicago=(
        "U.S. Department of the Treasury, USAspending.gov. Award "
        "CONT_AWD_SAQMMA12F1738_1900_SAQMMA08D0003_1900 (Contracting, Consulting, Engineering LLC; "
        "La Pointe/Caracol design-build). Signed 17 May 2012. "
        "https://api.usaspending.gov/api/v2/awards/CONT_AWD_SAQMMA12F1738_1900_SAQMMA08D0003_1900/."
    ),
    annotation="USASpending: CCE La Pointe/Caracol USD 6.803m. Supports cce_lapointe_caracol_infra_6p8m_2012.",
    evid_note="Opened USASpending Award API 2026-10-05; total_obligation USD 6,802,661.17; date_signed 2012-05-17.",
)

# 3. bridges_roads / us — DFS Caracol–Terrier Rouge–Ouanaminthe drainage
row_doc(
    "dfs_caracol_drainage_13p6m_2015",
    "infrastructure",
    "bridges_roads",
    "us",
    "DFS Construction — Cap-Haïtien corridor emergency repairs and drainage (USAID)",
    "Haiti",
    "26 Sep 2015: USAID awards contract AID521C1500013 to DFS Construction, LLC for emergency "
    "repairs and drainage works at Caracol-Ekam, Terrier Rouge and Ouanaminthe new settlement "
    "sites in the Cap-Haïtien development corridor; obligated USD 13,618,267.35. CapEx face = "
    "award obligation. Distinct from wb_haiti_resilient_corridors_80m_2025.",
    "13618267.35",
    "2015-09-26",
    "2015",
    "19.64",
    "-71.96",
    "Caracol-Ekam / Terrier Rouge / Ouanaminthe corridor, Nord-Est, Haiti (award description; Terrier Rouge pin).",
    "usaspending_dfs_caracol_drainage_20150926",
    "EMERGENCY REPAIRS AND DRAINAGE WORKS AT CARACOL-EKAM, TERRIER ROUGE AND OUNAMINTHE NEW SETTLEMENTS SITES IN THE CAP HAITIEN DEVELOPMENT CORRIDOR",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1500013_7200_-NONE-_-NONE-/",
    "Actor: DFS Construction, LLC (U.S.) under USAID — us. Official USASpending Award API. "
    "Shuffle bridges_roads; Haiti under-covered; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle902",
    investment_type="epc",
    chicago=(
        "U.S. Department of the Treasury, USAspending.gov. Award "
        "CONT_AWD_AID521C1500013_7200_-NONE-_-NONE- (DFS Construction, LLC; Cap-Haïtien corridor "
        "drainage). Signed 26 September 2015. "
        "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1500013_7200_-NONE-_-NONE-/."
    ),
    annotation="USASpending: DFS Cap-Haïtien drainage USD 13.618m. Supports dfs_caracol_drainage_13p6m_2015.",
    evid_note="Opened USASpending Award API 2026-10-05; total_obligation USD 13,618,267.35; date_signed 2015-09-26.",
)

# 4. power_plants_grid / us — UTE PPSELD T&D materials
row_doc(
    "ute_ppseld_td_materials_2p33m_2014",
    "energy",
    "power_plants_grid",
    "us",
    "Universal Trading & Engineering — PPSELD T&D materials near Caracol (USAID)",
    "Haiti",
    "8 Dec 2014: USAID awards AID521O1500005 to Universal Trading & Engineering Corporation to "
    "procure transmission and distribution materials for PPSELD expansion to three communes "
    "near Caracol Industrial Park; obligated USD 2,333,731.69. CapEx face = award obligation. "
    "Distinct from nreca_caracol_power_2013 (O&M plant contract).",
    "2333731.69",
    "2014-12-08",
    "2014",
    "19.740",
    "-72.020",
    "PPSELD expansion communes near Caracol Industrial Park, Nord-Est, Haiti (award geography; Caracol pin).",
    "usaspending_ute_ppseld_td_20141208",
    "RFQ TO PROCURE TRANSMISSION&DISTRIBUTION MATERIALS FOR PPSELD EXPANSION TO THREE OTHER COMMUNES NEAR TO THE CARACOL INDISTRIAL PARK.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521O1500005_7200_-NONE-_-NONE-/",
    "Actor: Universal Trading & Engineering Corporation (U.S.) under USAID — us. Official "
    "USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle902",
    investment_type="procurement",
    chicago=(
        "U.S. Department of the Treasury, USAspending.gov. Award "
        "CONT_AWD_AID521O1500005_7200_-NONE-_-NONE- (Universal Trading & Engineering; PPSELD T&D). "
        "Signed 8 December 2014. "
        "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521O1500005_7200_-NONE-_-NONE-/."
    ),
    annotation="USASpending: UTE PPSELD T&D USD 2.334m. Supports ute_ppseld_td_materials_2p33m_2014.",
    evid_note="Opened USASpending Award API 2026-10-05; total_obligation USD 2,333,731.69; date_signed 2014-12-08.",
)

# 5. power_plants_grid / allied — PIP mini-réseau CDB
row_doc(
    "haiti_pip_minireseau_cdb_55p4m_htg_fy2526",
    "energy",
    "power_plants_grid",
    "allied",
    "CDB — Mise en place d'un mini-réseau d'électrification rurale (PIP FY2025–26)",
    "Haiti",
    "PIP FY2025–26 line 1113-1-12-50-42 MISE EN PLACE D'UN MINI-RESEAU D'ELECTRIFICATION RURALE: "
    "multilatéral CDB DON 55,400,000 HTG = TOTAL PIP 55,400,000 HTG. CapEx/financing FY face "
    "(HTG; USD blank — no Fed H.10 HTG). Distinct from haiti_pip_hag1048_storage_nord_197m_htg_fy2526.",
    "55400000",
    "",
    "2025",
    "",
    "",
    "Haiti national rural mini-grid electrification program — lat/lon blank.",
    PIP_SID,
    "1113-1-12-50-42- MISE EN PLACE D'UN MINI-RESEAU D'ELECTRIFICATION RURALE NATIONAL                                -                                  -                                -                                -                       55,400,000  CDB  DON             55,400,000               55,400,000",
    PIP_URL,
    "Actor: Caribbean Development Bank (CDB) grant — allied multilateral. Official MPCE PIP PDF. "
    "FY face HTG; USD blank. Shuffle power_plants_grid; Haiti under-covered.",
    "hunt_cycle902",
    investment_type="financing",
    currency="HTG",
    value_usd="",
    fx_usd="",
    chicago=PIP_CHICAGO,
    annotation="Haiti PIP FY2025–26: CDB mini-réseau 55,400,000 HTG. Supports haiti_pip_minireseau_cdb_55p4m_htg_fy2526.",
    evid_note="Opened haitidocs MPCE PIP FY2025–26 PDF 2026-10-05; CDB mini-réseau TOTAL PIP.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    supports = entry.get("supports") or []
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        prev = existing.get("supports") or []
        for s in supports:
            if s not in prev:
                prev.append(s)
        existing.update(entry)
        existing["supports"] = prev
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

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"cycle902 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
