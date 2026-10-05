#!/usr/bin/env python3
"""Cycle 306 hunt: shuffle_seed=20261306; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261306).shuffle):
balsa, solar, fission_smr, niobium, port_ownership, rail, building_materials,
nickel, port_cranes, engineering_epc, other_renewables, water, power_plants_grid,
bridges_roads, copper, graphite, wind, lithium.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (balsa first / fission_smr third / nickel eighth in shuffle).
≥1/3 U.S. hunt budget: AES AR CapEx-fill dry after Atacama Solar; Arenales blank;
  Wabtec Vale CapEx blank; Progress Rail R$430m absent; Bechtel/Fluor CapEx-fill
  blanks; Equinix SEC 403.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
ALLIED: NEW ISA Energia Brasil Anexo I CapEx ANEEL + CapEx ISA até 30/06/2026 for
  older 2017–2020 greenfield projects (Paraguaçú, Aimorés, Itaúnas, Tibagi,
  Itaquerê, Aguapeí, Bauru, Lorena, Biguaçu, Três Lagoas, Triângulo Mineiro).
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
ISA_URL = "https://ri.isaenergiabrasil.com.br/pt/documentos/6758-Earnings-Release-2T26-vfinal.pdf"
ISA_CHICAGO = (
    'ISA Energia Brasil. “Earnings Release 2T26.” August 3, 2026. ' + ISA_URL + "."
)
ISA_SID = "isa_energia_2t26_earnings_release"
GEO = "ISA Energia Brasil transmission footprint (São Paulo HQ pin)."
LAT, LON = "-23.55", "-46.63"


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


# name, slug, aneel_m, isa_m, quote_fragment, extra
PROJECTS = [
    ("Paraguaçú", "paraguacu", 254.8, 333.4, "Paraguaçú (Lote 3) … 254,8 333,4", "IE Paraguaçu 50% BA/MG."),
    ("Aimorés", "aimores", 170.6, 197.5, "Aimorés (Lote 4) … 170,6 197,5", "IE Aimorés 50% MG."),
    ("Itaúnas", "itaunas", 297.8, 373.8, "Itaúnas (Lote 21) … 297,8 373,8", "IE Itaúnas 100% ES."),
    ("Tibagi", "tibagi", 134.6, 117.5, "Tibagi (Lote 5) … 134,6 117,5", "IE Tibagi 100% SP/PR."),
    ("Itaquerê", "itaquere", 397.7, 255.9, "Itaquerê (Lote 6) … 397,7 255,9", "IE Itaquerê 100% SP/PR."),
    ("Aguapeí", "aguapei", 601.9, 363.4, "Aguapeí (Lote 29) … 601,9 363,4", "IE Aguapeí 100% SP/PR."),
    ("Bauru", "bauru", 125.8, 63.0, "Bauru (Lote 25) … 125,8 63,0", "IE Jaguar 6 100% SP."),
    ("Lorena", "lorena", 237.9, 126.1, "Lorena (Lote 10) … 237,9 126,1", "IE Itapura 100% SP."),
    ("Biguaçu", "biguacu", 641.4, 456.0, "Biguaçu (Lote 1) … 641,4 456,0", "IE Biguaçu 100% SC."),
    ("Três Lagoas", "tres_lagoas", 98.8, 87.1, "Três Lagoas (Lote 6) … 98,8 87,1", "IE Tibagi 100% MS/SP."),
    ("Triângulo Mineiro", "triangulo_mineiro", 553.6, 519.6, "Triângulo Mineiro … 553,6 519,6", "IEMG 100% MG."),
]

for name, slug, aneel_m, isa_m, quote, extra in PROJECTS:
    for kind, kind_slug, val_m in [
        ("CapEx ANEEL", "capex_aneel", aneel_m),
        ("CapEx ISA até 30/06/2026", "capex_30jun26", isa_m),
    ]:
        val = int(round(val_m * 1_000_000))
        # format id: use p for decimal
        val_id = f"{val_m}".replace(".", "p")
        if val_id.endswith("p0"):
            val_id = val_id[:-2]
        rid = f"isa_energia_{slug}_{kind_slug}_{val_id}m_brl"
        row_doc(
            rid, "energy", "power_plants_grid", "allied",
            f"ISA Energia Brasil — {name} {kind} R${val_m}m",
            "Brazil",
            f"3 Aug 2026 ISA Energia Brasil Earnings Release 2T26: Anexo I – Projetos Greenfield desde 2016 — {name} {kind} R${val_m} million. CapEx: enter labeled table face. {extra} Distinct from peer CapEx ANEEL/ISA face for same project and from 2021–2023 greenfield faces logged cycle 305.",
            str(val), "2026-08-03", "2026", LAT, LON, GEO,
            ISA_SID, quote, ISA_URL,
            f"Actor: ISA Energia Brasil — allied. NEW {name} {kind}. Shuffle power_plants_grid; allied equal-budget.",
            "hunt_cycle306", investment_type="corporate_capex", evidence="documented", currency="BRL",
            value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
            chicago=ISA_CHICAGO,
            annotation=f"ISA {name} {kind} via Fed H.10. Supports {rid}.",
            evid_note=f"Opened ISA 2T26 Earnings Release PDF; {name} {kind} R${val_m}m confirmed.",
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
    print(f"cycle306 added {len(added)}: {added}")
    print(f"cycle306 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
