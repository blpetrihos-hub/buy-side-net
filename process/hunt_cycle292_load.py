#!/usr/bin/env python3
"""Cycle 292 hunt: shuffle_seed=20261292; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261292).shuffle):
port_cranes, balsa, port_ownership, power_plants_grid, rail, graphite, copper,
fission_smr, solar, building_materials, other_renewables, bridges_roads, niobium,
engineering_epc, wind, lithium, nickel, water.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (balsa second in shuffle — dry).
≥1/3 U.S. hunt budget: SSA Guaymas STS CapEx-fill — MXN424.8m already on TUM
  concession face (no distinct STS dollar); Bechtel QB2 desal blank; Arenales
  blank; Progress Rail VLI R$430m unsigned.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
OTHER: NEW Equatorial 2T26 nested Ativos elétricos + Obrigações especiais for
  PA/GO/MA/PI distributors.
Skipped: thin dry; port_cranes/port_ownership/rail/graphite/copper/fission_smr/
  solar/building_materials/other_renewables/bridges_roads/niobium/engineering_epc/
  wind/lithium/nickel/water dense or CapEx-blank; Motiva 1S26 roads/rails split
  not separately disclosed beyond 2T26 nested; holdovers unsigned.
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
EQ_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/"
    "b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2"
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


# Equatorial 2T26 nested Ativos elétricos / OE by distributor (other)
# Columns MA PA PI AL RS AP GO — 2T26: eletricos 279/362/179/169/262/71/611; OE 30/329/49/10/-/23/20
for rid, name, line, val, lat, lon, geo, quote in [
    ("equatorial_pa_eletricos_2t26_362m_brl", "Equatorial Pará", "Ativos elétricos", 362000000, "-1.46", "-48.50", "Equatorial Pará (Belém pin).", "Ativos elétricos … 362"),
    ("equatorial_pa_oe_2t26_329m_brl", "Equatorial Pará", "Obrigações especiais", 329000000, "-1.46", "-48.50", "Equatorial Pará PLPT / special obligations (Belém pin).", "Obrigações especiais … 329"),
    ("equatorial_go_eletricos_2t26_611m_brl", "Equatorial Goiás", "Ativos elétricos", 611000000, "-16.69", "-49.25", "Equatorial Goiás (Goiânia pin).", "Ativos elétricos … 611"),
    ("equatorial_ma_eletricos_2t26_279m_brl", "Equatorial Maranhão", "Ativos elétricos", 279000000, "-2.53", "-44.30", "Equatorial Maranhão (São Luís pin).", "Ativos elétricos … 279"),
    ("equatorial_pi_eletricos_2t26_179m_brl", "Equatorial Piauí", "Ativos elétricos", 179000000, "-5.09", "-42.80", "Equatorial Piauí (Teresina pin).", "Ativos elétricos … 179"),
    ("equatorial_pi_oe_2t26_49m_brl", "Equatorial Piauí", "Obrigações especiais", 49000000, "-5.09", "-42.80", "Equatorial Piauí PLPT (Teresina pin).", "Obrigações especiais … 49"),
    ("equatorial_rs_eletricos_2t26_262m_brl", "Equatorial CEEE-D (RS)", "Ativos elétricos", 262000000, "-30.03", "-51.23", "Equatorial CEEE-D (Porto Alegre pin).", "Ativos elétricos … 262"),
    ("equatorial_ma_oe_2t26_30m_brl", "Equatorial Maranhão", "Obrigações especiais", 30000000, "-2.53", "-44.30", "Equatorial Maranhão OE (São Luís pin).", "Obrigações especiais … 30"),
]:
    row_doc(
        rid, "energy", "power_plants_grid", "other",
        f"{name} — {line} CapEx 2T26 R${val/1e6:.0f}m",
        "Brazil",
        f"12 Aug 2026 Equatorial 2T26 release: Investimentos Distribuidoras — {name} {line} 2T26 R${val/1e6:,.0f} million. CapEx: enter face. Nested under distributor Total / Dist Ativos elétricos R$1.933bn / OE R$460m (not additive).",
        str(val), "2026-08-12", "2026", lat, lon, geo,
        "equatorial_2t26_release_20260812", quote, EQ_URL,
        f"Actor: {name} — other. NEW 2T26 {line}. Shuffle power_plants_grid; other equal-budget.",
        "hunt_cycle292", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. ' + EQ_URL + ".",
        annotation=f"{name} 2T26 {line} via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Equatorial 2T26 PDF; {name} {line} 2T26 R${val/1e6:,.0f}m confirmed.",
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
    print(f"cycle292 added {len(added)}: {added}")
    print(f"cycle292 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
