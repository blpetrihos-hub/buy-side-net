#!/usr/bin/env python3
"""Cycle 299 hunt: shuffle_seed=20261299; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261299).shuffle):
power_plants_grid, copper, graphite, fission_smr, wind, bridges_roads, balsa,
building_materials, water, other_renewables, engineering_epc, port_cranes,
lithium, niobium, rail, port_ownership, solar, nickel.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (balsa seventh / nickel last in shuffle).
≥1/3 U.S. hunt budget: AES Andes Hub US$1.3bn already logged; Arenales CapEx
  blank; SSA Guaymas STS dollar blank; Wabtec Vale CapEx blank; Bechtel 403;
  graphite CapEx-fill blanks.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
ALLIED: NEW Alupar TES/TEL/SED/TEP/TSA/TER/Geral CapEx Realizado USD faces
  from 2T26 implantation table.
Skipped: thin dry; Motiva Capex Proforma largely mined; US CapEx dry this pass
  after Progress Rail R$600m in cycle 298; holdovers unsigned.
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


# Alupar CapEx Realizado USD — TES TEL SED TEP TSA TER Geral
# País: PER CHL COL CHL PER PER PER; CapEx Previsto 38.9/40.0/45.2/145.9/19.6/400.2/42.8
for rid, name, country, val, previsto, chars, geo, quote in [
    ("alupar_tes_capex_realizado_25p03m_usd", "TES", "Peru", 25030000, "38.9",
     "1 SE + LT 9 km", "Alupar TES transmission (Peru; site coords not named — left blank).",
     "CAPEX Realizado (MM) … US$ 25,03"),
    ("alupar_tel_capex_realizado_4p3m_usd", "TEL", "Chile", 4300000, "40.0",
     "2 SEs + LT 15.7 km", "Alupar TEL transmission (Chile; site coords not named — left blank).",
     "CAPEX Realizado (MM) … US$ 4,3"),
    ("alupar_sed_capex_realizado_3p6m_usd", "SED", "Colombia", 3600000, "45.2",
     "3 SEs + LT 100 km", "Alupar SED transmission (Colombia; site coords not named — left blank).",
     "CAPEX Realizado (MM) … US$ 3,6"),
    ("alupar_tep_capex_realizado_13p5m_usd", "TEP", "Chile", 13500000, "145.9",
     "2 SEs + synchronous compensators", "Alupar TEP transmission (Chile; site coords not named — left blank).",
     "CAPEX Realizado (MM) … US$ 13,5"),
    ("alupar_tsa_capex_realizado_0p4m_usd", "TSA", "Peru", 400000, "19.6",
     "LT 9.5 km + 3 SEs", "Alupar TSA transmission (Peru; site coords not named — left blank).",
     "CAPEX Realizado (MM) … US$ 0,4"),
    ("alupar_ter_capex_realizado_6p4m_usd", "TER", "Peru", 6400000, "400.2",
     "LT 176.5 km + 6 SEs", "Alupar TER transmission (Peru; site coords not named — left blank).",
     "CAPEX Realizado (MM) … US$ 6,4"),
    ("alupar_geral_capex_realizado_1p2m_usd", "Geral", "Peru", 1200000, "42.8",
     "LT 76.0 km + 2 SEs", "Alupar Geral transmission (Peru; site coords not named — left blank).",
     "CAPEX Realizado (MM) … US$ 1,2"),
]:
    row_doc(
        rid, "energy", "power_plants_grid", "allied",
        f"Alupar — {name} CapEx Realizado USD{val/1e6:.2f}m (2T26 table)",
        country,
        f"6 Aug 2026 Alupar Investimento 2T26 earnings release: Projetos de Transmissão em Implantação — {name} ({country}; {chars}) CAPEX Realizado US${val/1e6:.2f} million (vs CAPEX Previsto US${previsto}m). CapEx: enter cumulative realized face. Nested under implantation portfolio; distinct from Brazil TAP/TPC/TCN Realizado BRL faces and from period Custo de Infraestrutura.",
        str(val), "2026-08-06", "2026", "", "", geo,
        "alupar_2t26_release_20260806", quote, ALUPAR_URL,
        f"Actor: Alupar Investimento — allied. NEW {name} CapEx Realizado USD. Shuffle power_plants_grid; allied equal-budget.",
        "hunt_cycle299", investment_type="corporate_capex", evidence="documented", currency="USD",
        value_usd=str(val), fx_usd="1", bib_type="company",
        chicago=ALUPAR_CHICAGO,
        annotation=f"Alupar {name} CapEx Realizado USD. Supports {rid}.",
        evid_note=f"Opened Alupar 2T26 RI ZIP PDF; {name} CapEx Realizado US${val/1e6:.2f}m confirmed.",
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
    print(f"cycle299 added {len(added)}: {added}")
    print(f"cycle299 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
