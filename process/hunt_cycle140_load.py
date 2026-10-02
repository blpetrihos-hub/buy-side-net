#!/usr/bin/env python3
"""Cycle 140 hunt: shuffle_seed=20261140; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: port_cranes, lithium, nickel, solar, bridges_roads, wind,
fission_smr, graphite, power_plants_grid, balsa, water, engineering_epc,
building_materials, niobium, copper, rail, port_ownership, other_renewables.

PRC ahead by 6 after 139 — keep equal US/PRC budget without padding.
Thin top-up: balsa/graphite/nickel (dry → fission_smr → niobium).
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


# 1. solar / us — GameChange Solar 148 MW Colombia (distinct from 715 MWp portfolio)
row_doc(
    "gamechange_148mw_colombia_2024",
    "energy",
    "solar",
    "us",
    "GameChange Solar — 148 MW Genius Tracker + MaxSpan Colombia project",
    "Colombia",
    "22 Aug 2024 GameChange Solar (Norwalk, CT): order for a 148 MW solar project in Colombia — 101 MW Genius Tracker 1P + 47 MW MaxSpan fixed-tilt; company states seventh Colombia project. Developer/site name not disclosed on opened page — CapEx blank. Distinct from gamechange_715mwp_latam_2025 (Jun 2025 eight-project portfolio).",
    "",
    "",
    "2024",
    "4.71",
    "-74.07",
    "Colombia utility-scale PV (site unnamed on company page; Bogotá metro approximate for national award).",
    "gamechange_148mw_colombia_20240822",
    "NORWALK, CT – August 22, 2024 –GameChange Solar… today announced a new order for a 148 MW solar project in Colombia… The project will feature 101 MW of the Genius Tracker™ 1P system and 47 MW of the MaxSpan™ fixed-tilt system… \"We are proud to have local support in Colombia and are excited to be selected for our seventh project in the country,\" said Vikas Bansal",
    "https://www.gamechangesolar.com/news/gamechange-solar-secures-148-mw-solar-project-in-colombia",
    "Actor: GameChange Solar (Norwalk, CT HQ) — us. Company English primary. CapEx blank; site unnamed. Distinct from gamechange_715mwp_latam_2025.",
    "hunt_energy_solar",
    investment_type="equipment_supply",
    bib_type="company",
    chicago='GameChange Solar. “GameChange Solar Secures 148 MW Solar Project in Colombia.” August 22, 2024. https://www.gamechangesolar.com/news/gamechange-solar-secures-148-mw-solar-project-in-colombia.',
    annotation="GameChange primary: 148 MW Colombia trackers/fixed-tilt (7th Colombia project). Supports gamechange_148mw_colombia_2024.",
    evid_note="Opened GameChange Solar English release 22 Aug 2024 (148 MW Colombia).",
)

# 2. solar / prc — POWERCHINA Djoemoe Station COD (Suriname Phase II named station)
row_doc(
    "powerchina_djoemoe_suriname_2026",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Djoemoe Station COD (Suriname Villages Micro-grid Phase II)",
    "Suriname",
    "2 Feb 2026 POWERCHINA: Djoemoe Station of Suriname Villages Micro-grid Solar Project Phase II commissioned 22 Jan 2026 — fourth completed Phase II station; serves nine forest villages; ~2,000 MWh/y estimated. Phase II portfolio: nine stations along Suriname and Marowijne Rivers (Saramacca); 5.349 MW PV + 18.6 MWh storage + 2.813 MVA diesel; ~100 km MV/LV lines. CapEx USD blank. Distinct from powerchina_suriname_microgrid_p2_2026 (Kajana/Guyaba Sites 3/9 May 2026 handover).",
    "",
    "",
    "2026",
    "4.35",
    "-55.44",
    "Djoemoe / upper Suriname River corridor (company geography; approximate pin).",
    "powerchina_djoemoe_20260202",
    "On Jan 22, the Djoemoe Station of the Suriname Villages Micro-grid Solar Project Phase II, constructed by POWERCHINA, was successfully completed and officially put into operation. … The newly commissioned Djoemoe Station is the fourth completed station under Phase II of the project. It will provide stable, round-the-clock electricity to nine forest villages, with an estimated annual power generation of about 2,000 MWh",
    "https://en.powerchina.cn/2026-02/02/c_829052.htm",
    "Actor: POWERCHINA (PRC SOE) — prc. Company English primary. CapEx blank (named-station COD under Phase II; no incremental CapEx on page). Distinct from Kajana/Guyaba Phase II row.",
    "hunt_energy_solar",
    investment_type="epc",
    bib_type="company",
    chicago='POWERCHINA. “POWERCHINA\'s Djoemoe Station of Suriname Villages Micro-grid Solar Project Phase II successfully commissioned.” February 2, 2026. https://en.powerchina.cn/2026-02/02/c_829052.htm.',
    annotation="POWERCHINA primary: Djoemoe Station COD Jan 2026 (Phase II fourth station). Supports powerchina_djoemoe_suriname_2026.",
    evid_note="Opened POWERCHINA English release 2 Feb 2026 (Djoemoe Station COD).",
)

# 3. solar / allied — Greenwood Energy TERRA Site I Colombia (Libra Group)
row_doc(
    "greenwood_terra_site1_52mwp_2026",
    "energy",
    "solar",
    "allied",
    "Greenwood Energy (Libra Group) — TERRA Site I 52 MWp solar FC (El Copey)",
    "Colombia",
    "28 Jan 2026 Greenwood Energy: financial close of TERRA Site I (Arhuaco partnership) — two solar plants totaling 52 MWp in El Copey, Cesar, plus first TERRA village; investment exceeding USD 50 million; FDN project finance COP 163bn (~USD 42.5m) signed 24 Dec 2025 + ImpactA Global corporate financing 30 Dec 2025; COD targeted Q2 2027; three-phase platform to 156 MWp. CapEx floor >USD 50m from company page.",
    "50000000",
    "2026-01-28",
    "2026",
    "10.15",
    "-73.96",
    "El Copey, Cesar Department, Colombia (TERRA Site I; approximate municipal pin).",
    "greenwood_terra_site1_20260128",
    "Greenwood Energy announces the financial close of TERRɅ Site I… These agreements will enable the start of construction of TERRɅ Site I in the municipality of El Copey, Department of Cesar, including two solar plants with a total installed capacity of 52 MWp, as well as the first TERRɅ village… with an investment exceeding USD 50 million. The financing provided by FDN amounts to COP 163 billion [~USD 42.5 million].",
    "https://greenwood.energy/2026/01/28/greenwood-energy-closes-financing-for-terr%ca%8c-site-i-the-first-phase-of-terr%ca%8c-initi%ca%8ctive-a-landmark-platform-for-a-just-energy-transition-in-colombia/",
    "Actor: Greenwood Energy / Libra Group (Greek multinational; Panama office on page) — allied. Company English primary. CapEx >USD 50m floor stored. Distinct from Nextracker/GameChange OEM supply rows.",
    "hunt_energy_solar",
    investment_type="ownership_equity",
    evidence="documented",
    bib_type="company",
    chicago='Greenwood Energy. “Greenwood Energy Closes Financing for TERRɅ Site I, the First Phase of TERRɅ INITIɅTIVE…” January 28, 2026. https://greenwood.energy/2026/01/28/greenwood-energy-closes-financing-for-terr%ca%8c-site-i-the-first-phase-of-terr%ca%8c-initi%ca%8ctive-a-landmark-platform-for-a-just-energy-transition-in-colombia/.',
    annotation="Greenwood/Libra primary: TERRA Site I 52 MWp FC; investment >USD 50m. Supports greenwood_terra_site1_52mwp_2026.",
    evid_note="Opened Greenwood Energy English release 28 Jan 2026 (TERRA Site I FC / >USD 50m).",
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
    print(f"Cycle 140 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
