#!/usr/bin/env python3
"""Cycle 305 hunt: shuffle_seed=20261305; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261305).shuffle):
engineering_epc, copper, building_materials, bridges_roads, niobium, graphite,
port_cranes, balsa, nickel, lithium, water, fission_smr, other_renewables, rail,
port_ownership, solar, wind, power_plants_grid.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (balsa eighth / nickel ninth / fission_smr twelfth in shuffle).
≥1/3 U.S. hunt budget: AES AR CapEx-fill dry after Atacama Solar; Arenales blank;
  Fluor Quellaveco CapEx blank; Wabtec Vale CapEx blank; Progress Rail R$430m
  absent; Bechtel/ENGIE 403.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
ALLIED: NEW ISA Energia Brasil Anexo I Greenfield CapEx ANEEL + CapEx ISA until
  30/06/2026 faces for Água Vermelha, Riacho Grande, Piraquê, Minuano, Ivaí,
  Serra Dourada CapEx ANEEL, Itatiaia CapEx ANEEL, Jacarandá CapEx ANEEL, and
  portfolio Totals (from 2T26 Earnings Release project table).
Skipped: thin dry; older 2017–2020 greenfield CapEx ANEEL/ISA pairs deferred;
  Itatiaia/Serra CapEx ISA-até vs Total Realizado near-duplicates deferred;
  holdovers unsigned.
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


# (rid, name, kind, val_m, quote, extra_note)
FACES = [
    ("isa_energia_agua_vermelha_capex_aneel_94p2m_brl", "Água Vermelha", "CapEx ANEEL",
     94.2, "Água Vermelha (Lote 9) … 94,2 87,1",
     "Lote 9 / IE Tibagi 100% SP; distinct from CapEx ISA até 30/06/2026 R$87.1m."),
    ("isa_energia_agua_vermelha_capex_30jun26_87p1m_brl", "Água Vermelha", "CapEx ISA até 30/06/2026",
     87.1, "Água Vermelha (Lote 9) … 94,2 87,1",
     "Lote 9 / IE Tibagi; distinct from CapEx ANEEL R$94.2m; COD 2T25."),
    ("isa_energia_riacho_grande_capex_aneel_1140p6m_brl", "Riacho Grande", "CapEx ANEEL",
     1140.6, "Riacho Grande (Lote 7) … 1.140,6 922,1",
     "Lote 7 / IE Riacho Grande 100% SP; distinct from CapEx ISA até 30/06/2026 R$922.1m."),
    ("isa_energia_riacho_grande_capex_30jun26_922p1m_brl", "Riacho Grande", "CapEx ISA até 30/06/2026",
     922.1, "Riacho Grande (Lote 7) … 1.140,6 922,1",
     "Distinct from CapEx ANEEL R$1,140.6m; COD 4T25."),
    ("isa_energia_piraque_capex_aneel_3653p6m_brl", "Piraquê", "CapEx ANEEL",
     3653.6, "Piraquê … 3.653,6 3.866,1",
     "Distinct from 2T26 spend R$84.4m and from CapEx ISA até 30/06/2026 R$3,866.1m."),
    ("isa_energia_piraque_capex_30jun26_3866p1m_brl", "Piraquê", "CapEx ISA até 30/06/2026",
     3866.1, "Piraquê … 3.653,6 3.866,1",
     "Distinct from CapEx ANEEL R$3,653.6m and from 2T26 spend R$84.4m."),
    ("isa_energia_minuano_capex_aneel_681p6m_brl", "Minuano", "CapEx ANEEL",
     681.6, "Minuano (Lote 1) … 681,6 737,6",
     "Evrecy 100% RS; distinct from 2T26 spend R$1.9m and CapEx ISA até 30/06/2026 R$737.6m."),
    ("isa_energia_minuano_capex_30jun26_737p6m_brl", "Minuano", "CapEx ISA até 30/06/2026",
     737.6, "Minuano (Lote 1) … 681,6 737,6",
     "Distinct from CapEx ANEEL R$681.6m and from 2T26 spend R$1.9m."),
    ("isa_energia_ivai_capex_aneel_968p2m_brl", "Ivaí", "CapEx ANEEL",
     968.2, "Ivaí (Lote 1) … 968,2 1.064,4",
     "IE Ivaí 50% PR; table shows ISA participation CapEx ANEEL; distinct from CapEx ISA até 30/06/2026 R$1,064.4m and 2T26 spend R$0.2m."),
    ("isa_energia_ivai_capex_30jun26_1064p4m_brl", "Ivaí", "CapEx ISA até 30/06/2026",
     1064.4, "Ivaí (Lote 1) … 968,2 1.064,4",
     "IE Ivaí 50%; distinct from CapEx ANEEL R$968.2m and 2T26 spend R$0.2m."),
    ("isa_energia_serra_dourada_capex_aneel_3156p8m_brl", "Serra Dourada", "CapEx ANEEL",
     3156.8, "Serra Dourada (Lote 1) … 3.156,8 1.790,5",
     "Distinct from Total Realizado R$1,844.5m and from prior Serra Dourada R$3.2bn envelope row; CapEx ISA até 30/06/2026 R$1,790.5m deferred (near Realizado)."),
    ("isa_energia_itatiaia_capex_aneel_2300p6m_brl", "Itatiaia", "CapEx ANEEL",
     2300.6, "Itatiaia (Lote 7) … 2.300,6 533,4",
     "Distinct from Total Realizado R$549.7m and 2T26 spend R$52.2m; CapEx ISA até 30/06/2026 R$533.4m deferred (near Realizado)."),
    ("isa_energia_jacaranda_capex_aneel_232p3m_brl", "Jacarandá", "CapEx ANEEL",
     232.3, "Jacarandá (Lote 6) … 232,3 189,3",
     "Distinct from project CapEx R$188.8m face and 2T26 spend R$13.5m."),
    ("isa_energia_greenfield_capex_aneel_total_15742p9m_brl", "Greenfield portfolio", "CapEx ANEEL Total",
     15742.9, "1.909,7 15.742,9 12.083,7",
     "Anexo I portfolio Total CapEx ANEEL (R$ milhões); distinct from CapEx ISA Total R$12,083.7m."),
    ("isa_energia_greenfield_capex_30jun26_total_12083p7m_brl", "Greenfield portfolio", "CapEx ISA Total até 30/06/2026",
     12083.7, "1.909,7 15.742,9 12.083,7",
     "Anexo I portfolio Total CapEx ISA até 30/06/2026; distinct from CapEx ANEEL Total R$15,742.9m."),
]

for rid, name, kind, val_m, quote, extra in FACES:
    val = int(round(val_m * 1_000_000))
    row_doc(
        rid, "energy", "power_plants_grid", "allied",
        f"ISA Energia Brasil — {name} {kind} R${val_m}m",
        "Brazil",
        f"3 Aug 2026 ISA Energia Brasil Earnings Release 2T26: Anexo I – Projetos Greenfield desde 2016 — {name} {kind} R${val_m} million. CapEx: enter labeled table face. {extra}",
        str(val), "2026-08-03", "2026", LAT, LON, GEO,
        ISA_SID, quote, ISA_URL,
        f"Actor: ISA Energia Brasil — allied. NEW {name} {kind}. Shuffle power_plants_grid; allied equal-budget.",
        "hunt_cycle305", investment_type="corporate_capex", evidence="documented", currency="BRL",
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
    print(f"cycle305 added {len(added)}: {added}")
    print(f"cycle305 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
