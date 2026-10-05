#!/usr/bin/env python3
"""Cycle 307 hunt: shuffle_seed=20261307; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261307).shuffle):
port_cranes, port_ownership, graphite, other_renewables, nickel, building_materials,
bridges_roads, engineering_epc, power_plants_grid, niobium, rail, fission_smr,
copper, balsa, solar, lithium, water, wind.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (nickel fifth / fission_smr twelfth / balsa fourteenth in shuffle).
≥1/3 U.S. hunt budget: AES Andes prensa JS-only (Arenales CapEx blank); AES AR
  CapEx-fill dry after Atacama Solar; Wabtec Vale CapEx blank; Progress Rail
  R$430m absent; Bechtel/Fluor CapEx-fill blanks; Axia RI 000.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
ALLIED: NEW Alupar USD period cash CapEx (visão caixa) 1T26/2T26 for TES/TEL/
  SED/TEP/TSA/TER/Geral — nested under CapEx Realizado USD cumulative; project
  order matches implantation CapEx Realizado table (skip unlabeled 2T26-only
  US$5.51 eighth USD line).
Skipped: thin dry; ISA Anexo I CapEx pairs complete; holdovers unsigned.
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

ALUPAR_URL = "https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip"
ALUPAR_CHICAGO = (
    'Alupar Investimento S.A. “Release de Resultados 2T26” (RI ZIP). August 6, 2026. '
    + ALUPAR_URL + "."
)
ALUPAR_SID = "alupar_2t26_release_20260806"


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid, layer, subcategory, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, source_id, quote, url, note, hunt_support,
    investment_type="epc", evidence="documented", currency="USD", value_usd=None,
    fx_usd=None, chicago=None, bib_type="company", annotation=None, evid_note=None,
    status="active",
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid, "layer": layer, "subcategory": subcategory, "side": side,
            "counterpart": counterpart, "country": country, "asset": asset,
            "investment_type": investment_type, "value": value, "currency": currency,
            "value_usd": value_usd, "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "", "year": year, "status": status,
            "lat": lat, "lon": lon, "geo_note": geo, "evidence": evidence,
            "source_id": source_id, "note": note, "pair_id": "", "counterpart_side": "",
            "counterpart_actor": "", "counterpart_value": "", "counterpart_currency": "",
            "counterpart_value_usd": "", "gap": "",
        },
        {
            "id": rid, "retrieved": "2026-10-05", "source_id": source_id, "url": url,
            "price_year": year, "evidence": evidence, "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id, "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url, "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# Project order matches CapEx Realizado USD block: TES TEL SED TEP TSA TER Geral
# Period cash table (visão caixa) 1T26 / 2T26; skip unlabeled 8th USD line US$5.51.
PROJECTS = [
    ("tes", "TES", "Peru", "1 SE + LT 9 km",
     {"1t26": 2.79, "2t26": 19.43},
     "US$ 2,79 … US$ 19,43"),
    ("tel", "TEL", "Chile", "2 SEs + LT 15.7 km",
     {"1t26": 0.05, "2t26": 1.50},
     "US$ 0,05 … US$ 1,50"),
    ("sed", "SED", "Colombia", "3 SEs + LT 100 km",
     {"1t26": 0.46, "2t26": 0.52},
     "US$ 0,46 … US$ 0,52"),
    ("tep", "TEP", "Chile", "2 SEs + synchronous compensators",
     {"1t26": 0.17, "2t26": 8.35},
     "US$ 0,17 … US$ 8,35"),
    ("tsa", "TSA", "Peru", "LT 9.5 km + 3 SEs",
     {"1t26": 0.06, "2t26": 0.24},
     "US$ 0,06 … US$ 0,24"),
    ("ter", "TER", "Peru", "LT 176.5 km + 6 SEs",
     {"1t26": 1.98, "2t26": 0.55},
     "US$ 1,98 … US$ 0,55"),
    ("geral", "Geral", "Peru", "LT 76.0 km + 2 SEs",
     {"1t26": 0.19, "2t26": 0.45},
     "US$ 0,19 … US$ 0,45"),
]

for slug, name, country, chars, periods, quote in PROJECTS:
    for period, val_m in periods.items():
        val = int(round(val_m * 1_000_000))
        # id formatting: 19.43 -> 19p43; 0.05 -> 0p05; 1.50 -> 1p5 or 1p50
        val_id = f"{val_m:.2f}".rstrip("0").rstrip(".").replace(".", "p")
        rid = f"alupar_{slug}_capex_{period}_{val_id}m_usd"
        geo = f"Alupar {name} transmission ({country}; site coords not named — left blank)."
        row_doc(
            rid, "energy", "power_plants_grid", "allied",
            f"Alupar — {name} CapEx {period.upper()} USD{val_m}m (visão caixa)",
            country,
            f"6 Aug 2026 Alupar Investimento 2T26 earnings release: Investimentos nos Projetos em Andamento (visão caixa, consonant with CAPEX Realizado) — {name} ({country}; {chars}) {period.upper()} US${val_m} million. CapEx: enter period cash face. Nested under {name} CapEx Realizado USD cumulative; distinct from CapEx Previsto USD envelope. Unlabeled 2T26-only US$5.51 eighth USD line not entered.",
            str(val), "2026-08-06", "2026", "", "", geo,
            ALUPAR_SID, quote, ALUPAR_URL,
            f"Actor: Alupar Investimento — allied. NEW {name} {period.upper()} cash CapEx USD. Shuffle power_plants_grid; allied equal-budget.",
            "hunt_cycle307", investment_type="corporate_capex", evidence="documented", currency="USD",
            value_usd=str(val), fx_usd="1", bib_type="company",
            chicago=ALUPAR_CHICAGO,
            annotation=f"Alupar {name} {period.upper()} CapEx USD. Supports {rid}.",
            evid_note=f"Opened Alupar 2T26 RI ZIP PDF; {name} {period.upper()} cash CapEx US${val_m}m confirmed.",
        )


def upsert_bib(bib, bib_by, entry):
    sid = entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        old = existing.get("supports") or []
        new = entry["supports"] or []
        merged = list(dict.fromkeys(list(old) + list(new)))
        existing.update({k: v for k, v in entry.items() if k != "supports"})
        existing["supports"] = merged
    else:
        bib.append(entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("entries") or bib.get("sources") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added, updated = [], []
    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            existing = rows[by_id[rid]]
            for k, v in full.items():
                if k != "id" and v != "" and v is not None:
                    existing[k] = v
            updated.append(rid)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        upsert_bib(bib, bib_by, bib_e)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle307 added {len(added)}: {added}")
    print(f"cycle307 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
