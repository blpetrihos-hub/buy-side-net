#!/usr/bin/env python3
"""Cycle 909 hunt: shuffle_seed=20261909; USASpending Haiti US CapEx + PIP residual.

Shuffle: engineering_epc, copper, port_ownership, graphite, building_materials, rail,
niobium, water, nickel, bridges_roads, solar, lithium, power_plants_grid,
other_renewables, fission_smr, balsa, port_cranes, wind.

Thin top-up balsa/nickel/fission_smr dry.
US: NEW AECOM Haiti A&E + PHS CHDC settlement CM + UEP Cap-Haïtien Port electrical.
OTHER: Haiti PIP rehab urbaine national + PAP metro streets.
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


# 1. engineering_epc / us — AECOM Haiti multi-sector A&E
row_doc(
    "aecom_haiti_ae_portfolio_6p55m_2018",
    "infrastructure",
    "engineering_epc",
    "us",
    "AECOM Technical Services, Inc. — USAID Haiti multi-sector infrastructure A&E",
    "Haiti",
    "22 Feb 2018: USAID awards task order 72052118F00004 to AECOM Technical Services, Inc. "
    "to provide professional architecture and engineering technical services for USAID Haiti "
    "multi-sectorial infrastructure portfolio design and management; obligated USD 6,550,233.70. "
    "CapEx face = award obligation. Distinct from aecom_panama_david_master_plan_2p2m_2024 / "
    "fluor_haiti_nec_2005.",
    "6550233.70",
    "2018-02-22",
    "2018",
    "18.540",
    "-72.340",
    "USAID Haiti multi-sector infrastructure portfolio (PoP Haiti; Port-au-Prince approximate).",
    "usaspending_aecom_haiti_ae_20180222",
    "PROVIDE PROFESSIONAL ARCHITECTURE AND ENGINEERING TECHNICAL SERVICES TO ASSIST USAID HAITI "
    "TO DESIGN AND MANAGE THE MULTI-SECTORIAL INFRASTRUCTURE PORTFOLIO.",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_72052118F00004_7200_AIDOAAI1500045_7200/",
    "Actor: AECOM Technical Services, Inc. (U.S. HQ) under USAID — us. Official USASpending Award "
    "API. Shuffle engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle909",
    investment_type="epc",
    chicago=(
        "U.S. Department of the Treasury, USAspending.gov. Award "
        "CONT_AWD_72052118F00004_7200_AIDOAAI1500045_7200 (AECOM Technical Services, Inc.; "
        "USAID Haiti multi-sector A&E). Signed 22 February 2018. "
        "https://api.usaspending.gov/api/v2/awards/CONT_AWD_72052118F00004_7200_AIDOAAI1500045_7200/."
    ),
    annotation="USASpending: AECOM Haiti A&E USD 6.550m. Supports aecom_haiti_ae_portfolio_6p55m_2018.",
    evid_note="Opened USASpending Award API 2026-10-05; total_obligation USD 6,550,233.70; date_signed 2018-02-22.",
)

# 2. engineering_epc / us — PHS CHDC permanent settlement CM
row_doc(
    "phs_chdc_settlement_cm_6p28m_2011",
    "infrastructure",
    "engineering_epc",
    "us",
    "PHS Group Inc. — CHDC Cap-Haïtien corridor permanent settlement design/CM",
    "Haiti",
    "8 Dec 2011: USAID awards contract AID521C1200002 to PHS Group Inc. for design engineering "
    "and construction management of proposed permanent settlement sites in the Cap-Haïtien "
    "Development Corridor (CHDC), including Fort-Liberté, Terrier Rouge, Quartier Morin, and "
    "Ouanaminthe; obligated USD 6,284,620.87. CapEx face = award obligation. Distinct from "
    "dfs_caracol_drainage_13p6m_2015 / trigon_cap_haitien_cm_to_3p0m_2023.",
    "6284620.87",
    "2011-12-08",
    "2011",
    "19.700",
    "-72.000",
    "CHDC Cap-Haïtien Development Corridor settlements (Fort-Liberté / Terrier Rouge / Quartier "
    "Morin / Ouanaminthe; Nord-Est corridor approximate).",
    "usaspending_phs_chdc_settlement_20111208",
    "THE PURPOSE OF THIS ACTION IS TO REQUEST THE SOLICITATION OF AN AWARD FOR THE DESIGN "
    "ENGINEERING AND THE CONSTRUCTION MANAGEMENT ASSOCIATED WITH THE PROPOSED PERMANENT "
    "SETTLEMENT SITES IN THE CHDC CAPCAP HAITIEN DEVELOPMENT CORRIDOR. THEY INCLUDE FORT "
    "LIBERTE, TERRIER ROUGE, QUARTIER MORIN AND OUANAMINTHE .",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1200002_7200_-NONE-_-NONE-/",
    "Actor: PHS Group Inc. (U.S.) under USAID — us. Official USASpending Award API. Shuffle "
    "engineering_epc; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle909",
    investment_type="epc",
    chicago=(
        "U.S. Department of the Treasury, USAspending.gov. Award "
        "CONT_AWD_AID521C1200002_7200_-NONE-_-NONE- (PHS Group Inc.; CHDC permanent settlement "
        "design/CM). Signed 8 December 2011. "
        "https://api.usaspending.gov/api/v2/awards/CONT_AWD_AID521C1200002_7200_-NONE-_-NONE-/."
    ),
    annotation="USASpending: PHS CHDC settlement CM USD 6.285m. Supports phs_chdc_settlement_cm_6p28m_2011.",
    evid_note="Opened USASpending Award API 2026-10-05; total_obligation USD 6,284,620.87; date_signed 2011-12-08.",
)

# 3. power_plants_grid / us — UEP Cap-Haïtien Port electrical renewal
row_doc(
    "uep_chp_electrical_renewal_4p67m_2023",
    "energy",
    "power_plants_grid",
    "us",
    "UnitedEngineParts Inc. — Cap-Haïtien Port (CHP) electrical services renewal",
    "Haiti",
    "30 Aug 2023: USAID awards contract 72052123C00003 to UnitedEngineParts Inc. for renewed "
    "electrical services to Cap-Haïtien Port (CHP) facilities including generator plant "
    "(demolition of existing works noted in award description); obligated USD 4,673,892.64. "
    "CapEx face = award obligation. Distinct from ute_ppseld_td_materials_2p33m_2014 / "
    "peco_ppseld_td_materials_402k_2014.",
    "4673892.64",
    "2023-08-30",
    "2023",
    "19.759",
    "-72.201",
    "Cap-Haïtien Port (CHP) electrical / generator plant, Nord, Haiti (USASpending PoP Haiti; "
    "Cap-Haïtien port pin).",
    "usaspending_uep_chp_electrical_20230830",
    "TO MEET THE ANTICIPATED CAPACITY REQUIREMENTS AT THE CHP AND SUPPORT ECONOMIC DEVELOPMENT "
    "IN NORTHERN HAITI USAID HAS COMMITTED TO THE FOLLOWING RENEWED ELECTRICAL SERVICES TO ALL "
    "FACILITIES INCLUDING GENERATOR PLANT. DEMOLITION OF EXISTING W",
    "https://api.usaspending.gov/api/v2/awards/CONT_AWD_72052123C00003_7200_-NONE-_-NONE-/",
    "Actor: UnitedEngineParts Inc. (U.S.-owned per USASpending) under USAID — us. Official "
    "USASpending Award API. Shuffle power_plants_grid; ≥1/3 U.S. hunt CapEx.",
    "hunt_cycle909",
    investment_type="epc",
    chicago=(
        "U.S. Department of the Treasury, USAspending.gov. Award "
        "CONT_AWD_72052123C00003_7200_-NONE-_-NONE- (UnitedEngineParts Inc.; Cap-Haïtien Port "
        "electrical renewal). Signed 30 August 2023. "
        "https://api.usaspending.gov/api/v2/awards/CONT_AWD_72052123C00003_7200_-NONE-_-NONE-/."
    ),
    annotation="USASpending: UEP CHP electrical USD 4.674m. Supports uep_chp_electrical_renewal_4p67m_2023.",
    evid_note="Opened USASpending Award API 2026-10-05; total_obligation USD 4,673,892.64; date_signed 2023-08-30.",
)

# 4. bridges_roads / other — PIP rehab urbaine national
row_doc(
    "haiti_pip_rehab_urbaine_national_262m_htg_fy2526",
    "infrastructure",
    "bridges_roads",
    "other",
    "MTPTC — Programme de réhabilitation urbaine national (PIP FY2025–26)",
    "Haiti",
    "PIP FY2025–26 line 11141-1-25-21-38 PROGRAMME DE REHABILITATION URBAINE NATIONAL: "
    "Trésor 262,269,015 HTG = TOTAL PIP 262,269,015 HTG. CapEx: FY PIP face (HTG; USD blank — "
    "no Fed H.10 HTG). Distinct from city-level rehab urbaine faces (Gonaïves / Miragoâne / "
    "Hinche / Jacmel).",
    "262269015",
    "",
    "2025",
    "",
    "",
    "Haiti national urban rehabilitation program — lat/lon blank (national programme).",
    PIP_SID,
    "11141-1-25-21-38- PROGRAMME DE REHABILITATION URBAINE NATIONAL               262,269,015                                -              262,269,015                              -                                      -                               -               262,269,015",
    PIP_URL,
    "Actor: MTPTC / République d'Haïti PIP — other. Official MPCE PIP PDF. FY face HTG; USD blank. "
    "Shuffle bridges_roads; Haiti under-covered.",
    "hunt_cycle909",
    investment_type="rehabilitation",
    currency="HTG",
    value_usd="",
    fx_usd="",
    chicago=PIP_CHICAGO,
    annotation="Haiti PIP FY2025–26: rehab urbaine national 262,269,015 HTG. Supports haiti_pip_rehab_urbaine_national_262m_htg_fy2526.",
    evid_note="Opened haitidocs MPCE PIP FY2025–26 PDF 2026-10-05; rehab urbaine national TOTAL PIP.",
)

# 5. bridges_roads / other — PIP PAP metro streets
row_doc(
    "haiti_pip_rues_pap_metro_100m_htg_fy2526",
    "infrastructure",
    "bridges_roads",
    "other",
    "MTPTC — Réhabilitation et entretien des rues zone métropolitaine de Port-au-Prince (PIP FY2025–26)",
    "Haiti",
    "PIP FY2025–26 line 1114-1-12-52-19 REHABILITATION ET ENTRETIEN DES RUES DANS LA ZONE "
    "METROPOLITAINE DE PORT-AU-PRINCE (Ouest): Trésor 100,000,000 HTG = TOTAL PIP 100,000,000 HTG. "
    "CapEx: FY PIP face (HTG; USD blank). Distinct from haiti_pip_rehab_urbaine_national_262m_htg_fy2526.",
    "100000000",
    "",
    "2025",
    "18.540",
    "-72.340",
    "Zone métropolitaine de Port-au-Prince, Ouest, Haiti (PIP localisation; metro approximate).",
    PIP_SID,
    "1114-1-12-52-19- REHABILITATION ET ENTRETIEN DES RUES DANS LA ZONE METROPOLITAINE DE "
    "PORT-AU-PRINCE OUEST               100,000,000                                -              100,000,000                              -                                      -                               -               100,000,000",
    PIP_URL,
    "Actor: MTPTC / République d'Haïti PIP — other. Official MPCE PIP PDF. FY face HTG; USD blank. "
    "Shuffle bridges_roads; Haiti under-covered.",
    "hunt_cycle909",
    investment_type="rehabilitation",
    currency="HTG",
    value_usd="",
    fx_usd="",
    chicago=PIP_CHICAGO,
    annotation="Haiti PIP FY2025–26: PAP metro streets 100,000,000 HTG. Supports haiti_pip_rues_pap_metro_100m_htg_fy2526.",
    evid_note="Opened haitidocs MPCE PIP FY2025–26 PDF 2026-10-05; PAP metro streets TOTAL PIP.",
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
    print(f"cycle909 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
