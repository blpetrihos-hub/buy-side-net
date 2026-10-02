#!/usr/bin/env python3
"""Cycle 138 hunt: shuffle_seed=20261138; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: water, bridges_roads, power_plants_grid, port_cranes, copper,
wind, port_ownership, fission_smr, lithium, building_materials, rail, niobium, nickel,
graphite, solar, engineering_epc, balsa, other_renewables.

PRC push with equal US/PRC budget (PRC ahead by 6 after 137 — no padding).
Thin top-up: balsa/graphite/nickel (dry → fission_smr).
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
    bib_type="company",
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
        },
        {
            "id": rid,
            "retrieved": "2026-10-02",
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
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. wind / us — Invenergy 10% + O&M on ~600 MW Brazil wind portfolio
row_doc(
    "invenergy_patria_600mw_br_2024",
    "energy",
    "wind",
    "us",
    "Invenergy — 10% equity + O&M on ~600 MW Brazil wind portfolio (Patria 90%)",
    "Brazil",
    "1 Jul 2024 Invenergy: with Patria Investments acquires ContourGlobal and Eletrobras’ nearly 600 MW wind portfolio in Brazil — Asa Branca, Chapada I, Chapada II, Chapada III (Piauí and Rio Grande do Norte); Invenergy holds 10% ownership and provides wind-turbine O&M; Patria holds 90%; long-term auction PPAs. Purchase CapEx USD not disclosed on opened page.",
    "",
    "",
    "2024",
    "-5.20",
    "-42.80",
    "Northeast Brazil wind cluster (Piauí / Rio Grande do Norte; portfolio pin approximate).",
    "invenergy_patria_600mw_20240701",
    "SÃO PAULO, BR (July 1, 2024) - Invenergy … today announced with Patria Investments the acquisition of ContourGlobal and Eletrobras’ nearly 600-megawatt (MW) wind energy portfolio in Brazil. Invenergy will hold a 10% ownership stake in the portfolio, while the remaining 90% will be owned by Patria Investments. Invenergy will also provide wind turbine operations & maintenance services for the portfolio. … The wind energy portfolio includes four projects located across Piauí and Rio Grande do Norte, Brazil: Asa Branca, Chapada I, Chapada II and Chapada III.",
    "https://invenergy.com/news/invenergy-and-patria-investments-acquire-600-mw-brazil-wind-portfolio-from-contourglobal-and-eletrobras",
    "Actor: Invenergy (Chicago HQ) — us. Company English primary. CapEx blank (equity share undisclosed). Distinct from ContourGlobal Chile/Colombia solar rows and Engie Asa Branca transmission.",
    "hunt_energy_wind",
    investment_type="ownership_equity",
    bib_type="company",
    chicago='Invenergy LLC. “Invenergy and Patria Investments Acquire 600 MW Brazil Wind Portfolio from ContourGlobal and Eletrobras.” July 1, 2024. https://invenergy.com/news/invenergy-and-patria-investments-acquire-600-mw-brazil-wind-portfolio-from-contourglobal-and-eletrobras.',
    annotation="Invenergy primary: 10% of ~600 MW Asa Branca/Chapada wind portfolio + O&M. Supports invenergy_patria_600mw_br_2024.",
    evid_note="Opened Invenergy English release 1 Jul 2024 (~600 MW Brazil wind / 10% equity + O&M).",
)

# 2. solar / prc — POWERCHINA Piarco Airport 518.84 kW Trinidad
row_doc(
    "powerchina_piarco_trinidad_2024",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Piarco International Airport Solar Park (Trinidad and Tobago)",
    "Trinidad and Tobago",
    "1 Aug 2024 POWERCHINA: Piarco International Airport Solar Park commissioning ceremony 30 Jul 2024 — first centralized PV project by POWERCHINA in Trinidad and Tobago; 518.84 kW solar PV station (design/procurement/construction/commissioning) for Trinidad and Tobago Airport Authority; EU / Global Climate Change Alliance funded; ≥767,034 kWh/y. CapEx USD not disclosed on opened page.",
    "",
    "",
    "2024",
    "10.60",
    "-61.34",
    "Piarco International Airport, Trinidad (solar park site).",
    "powerchina_piarco_solar_20240801",
    "The commissioning ceremony for the Piarco International Airport Solar Park Project, the first centralized photovoltaic project undertaken by POWERCHINA in Trinidad and Tobago, was held on July 30, marking the official commencement of the project's operations. … Located at Piarco International Airport, it involves the construction of a 518.84-kilowatt solar photovoltaic power station, including design, procurement, construction and commissioning. … The Piarco International Airport Solar Park Project will generate at least 767,034 kilowatt-hours of electricity annually",
    "https://en.powerchina.cn/2024-08/01/c_828745.htm",
    "Actor: POWERCHINA (PRC SOE) — prc. Company English primary. CapEx blank (EPC/presence; EU-funded). Distinct from Suriname microgrid / Colombia Francisco Juana / Palmira III rows. Undersampled Trinidad.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="company",
    chicago='POWERCHINA. “Piarco International Airport Solar Park begins operating.” August 1, 2024. https://en.powerchina.cn/2024-08/01/c_828745.htm.',
    annotation="POWERCHINA primary: 518.84 kW Piarco Airport solar COD Jul 2024. Supports powerchina_piarco_trinidad_2024.",
    evid_note="Opened POWERCHINA English release 1 Aug 2024 (Piarco 518.84 kW COD).",
)

# 3. power_plants_grid / allied — Wärtsilä 36×34SG engines for Origem 371 MW Brazil
row_doc(
    "wartsila_origem_371mw_br_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "Wärtsilä — 36 × 34SG engines for Origem Energia 371 MW LRCAP plants (Brazil)",
    "Brazil",
    "13 May 2026 Wärtsilä: two equipment-supply contracts with Origem Energia for 36 Wärtsilä 34SG balancing engines (two batches of 18; Q1 and Q2 2026 bookings) totaling 371 MW — Pilar and Pilar Nova COD Oct 2028; Manguaba I–V COD Aug 2029; LRCAP 2026 winners; Alagoas gas-to-wire. Equipment CapEx USD not disclosed on opened page.",
    "",
    "",
    "2026",
    "-9.60",
    "-35.95",
    "Alagoas, Brazil (Pilar / Manguaba LRCAP cluster; approximate).",
    "wartsila_origem_371mw_20260513",
    "Technology group Wärtsilä has signed two equipment supply contracts with Origem Energia for the development of new balancing power projects in Brazil. The contracts cover the supply of two batches of 18 Wärtsilä 34SG balancing engines, totaling 36 engines … The selected projects include the Pilar and Pilar Nova power plants, set to begin operations in October 2028, as well as the Manguaba I–V projects, scheduled to begin operations in August 2029. … Together, these projects will contribute to the supply of reliable and flexible capacity to the Brazilian power grid.",
    "https://www.wartsila.com/media/news/13-05-2026-wartsila-and-origem-energia-partner-on-371-mw-power-plant-projects-to-deliver-reliable-and-flexible-capacity-to-brazil-s-power-grid-3750306",
    "Actor: Wärtsilä (Nasdaq Helsinki / Finland HQ) — allied. Company English primary. CapEx blank (equipment supply). Distinct from GE Vernova Azulão / NFE Barcarena thermal rows.",
    "hunt_energy_power_plants_grid",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='Wärtsilä Corporation. “Wärtsilä and Origem Energia partner on 371 MW power plant projects to deliver reliable and flexible capacity to Brazil’s power grid.” May 13, 2026. https://www.wartsila.com/media/news/13-05-2026-wartsila-and-origem-energia-partner-on-371-mw-power-plant-projects-to-deliver-reliable-and-flexible-capacity-to-brazil-s-power-grid-3750306.',
    annotation="Wärtsilä primary: 36×34SG / 371 MW for Origem LRCAP plants. Supports wartsila_origem_371mw_br_2026.",
    evid_note="Opened Wärtsilä English release 13 May 2026 (Origem 371 MW / 36 engines).",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        supports = list(existing.get("supports") or [])
        for s in entry.get("supports") or []:
            if s not in supports:
                supports.append(s)
        existing.update(entry)
        existing["supports"] = supports
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
        yaml.safe_dump(bib, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print(f"Cycle 138 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
