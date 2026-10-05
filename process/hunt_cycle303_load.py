#!/usr/bin/env python3
"""Cycle 303 hunt: shuffle_seed=20261303; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261303).shuffle):
port_ownership, lithium, engineering_epc, graphite, bridges_roads, water, solar,
power_plants_grid, rail, other_renewables, copper, niobium, building_materials,
fission_smr, nickel, balsa, wind, port_cranes.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (fission_smr fourteenth / nickel fifteenth / balsa sixteenth in shuffle).
≥1/3 U.S. hunt budget: AES Corp AR re-scanned — Atacama Solar already CapEx-filled
  in 302; Arenales/Atacama BESS/blank AES COD faces still CapEx-blank; Cochrane
  $25m NCI attribution not clean CapEx; Wabtec Vale / Progress Rail R$430m /
  Bechtel CapEx-fill blanks.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
ALLIED: NEW Neoenergia Dist CapEx Movimentação Material / Investimento Bruto /
  Investimento Líquido × Coelba/PE/Cosern/Elektro/Brasília 6M26 (15 faces) —
  completes deferred Dist×distributor nested after cycles 301–302.
Skipped: thin dry; holdovers unsigned.
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

BRL_USD = "5.1921"
NEO_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/"
    "145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2"
)
NEO_CHICAGO = (
    'Neoenergia S.A. “Earnings Release 2Q26 / 6M26” (company MZ IQ PDF). ' + NEO_URL + "."
)
NEO_SID = "neoenergia_2q26_release_mziq"

DISTS = [
    ("coelba", "Coelba", "Bahia", "-12.97", "-38.51", "Neoenergia Coelba (Salvador pin)."),
    ("pe", "Pernambuco", "Pernambuco", "-8.05", "-34.88", "Neoenergia Pernambuco (Recife pin)."),
    ("cosern", "Cosern", "Rio Grande do Norte", "-5.79", "-35.21", "Neoenergia Cosern (Natal pin)."),
    ("elektro", "Elektro", "São Paulo", "-23.55", "-46.63", "Neoenergia Elektro (São Paulo pin)."),
    ("brasilia", "Brasília", "Distrito Federal", "-15.78", "-47.93", "Neoenergia Brasília (Brasília pin)."),
]


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


CATEGORIES = [
    (
        "material",
        "Movimentação Material (Estoque x Obra)",
        [175, 66, 26, 23, 21],
        "Movimentação Material (Estoque x Obra) 175 … 66 … 26 … 23 … 21 … 310",
        "neoenergia_material_6m26_310m_brl",
    ),
    (
        "investimento_bruto",
        "Investimento Bruto",
        [2092, 815, 271, 626, 262],
        "(=) Investimento Bruto 2.092 … 815 … 271 … 626 … 262 … 4.066",
        "neoenergia_investimento_bruto_6m26_4066m_brl",
    ),
    (
        "investimento_liquido",
        "Investimento Líquido",
        [2093, 811, 266, 586, 248],
        "(=) Investimento Líquido 2.093 … 811 … 266 … 586 … 248 … 4.005",
        "neoenergia_investimento_liquido_6m26_4005m_brl",
    ),
]

for slug, label, vals, quote, parent in CATEGORIES:
    for (dslug, dname, state, lat, lon, geo), val_m in zip(DISTS, vals):
        val = int(val_m * 1_000_000)
        rid = f"neoenergia_{dslug}_{slug}_6m26_{val_m}m_brl"
        row_doc(
            rid, "energy", "power_plants_grid", "allied",
            f"Neoenergia {dname} — {label} 6M26 R${val_m}m",
            "Brazil",
            f"21 Jul 2026 Neoenergia S.A. Earnings Release 2Q26/6M26: Dist CapEx abertura por distribuidora — {dname} ({state}) {label} 6M26 R${val_m} million. CapEx: enter category×distributor nested face. Nested under {parent} aggregate and under {dname} Dist CapEx total already logged. Distinct from (=) CAPEX line after material adjustment.",
            str(val), "2026-07-21", "2026", lat, lon, geo,
            NEO_SID, quote, NEO_URL,
            f"Actor: Neoenergia (Iberdrola) — allied. NEW {dname} {label} 6M26. Shuffle power_plants_grid; allied equal-budget.",
            "hunt_cycle303", investment_type="corporate_capex", evidence="documented", currency="BRL",
            value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
            chicago=NEO_CHICAGO,
            annotation=f"Neoenergia {dname} {label} 6M26 via Fed H.10. Supports {rid}.",
            evid_note=f"Opened Neoenergia 2Q26 MZ IQ PDF; {dname} {label} 6M26 R${val_m}m confirmed.",
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
    print(f"cycle303 added {len(added)}: {added}")
    print(f"cycle303 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
