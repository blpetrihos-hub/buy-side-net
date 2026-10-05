#!/usr/bin/env python3
"""Cycle 304 hunt: shuffle_seed=20261304; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261304).shuffle):
nickel, balsa, graphite, rail, fission_smr, port_cranes, engineering_epc, water,
building_materials, niobium, copper, other_renewables, wind, bridges_roads,
power_plants_grid, solar, lithium, port_ownership.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (nickel first / balsa second / fission_smr fifth in shuffle — CapEx-fill dry;
  Syrah Balama Mozambique out of LatAm; Horizonte Araguaia CapEx blank on IR).
≥1/3 U.S. hunt budget: AES AR CapEx-fill dry after Atacama Solar; Arenales blank;
  Wabtec Vale CapEx blank; Progress Rail R$430m absent; Bechtel 403; ENGIE RI 403.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
OTHER: NEW Cemig GT transmission CapEx — REA Reforços e Melhorias R$924.6m +
  Lote 1 leilão 02/2022 R$242.2m + COD-year CapEx schedule 2026–2029 + Total
  R$1,166.787m (from 1S26/2T26 results presentation).
Skipped: thin dry; Neoenergia Dist×distributor nested complete; gás R$227m
  taxonomy-out; holdovers unsigned.
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
CEMIG_URL = "https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf"
CEMIG_CHICAGO = (
    'Cemig. “Resultados 1S26 / 2T26” (company RI presentation PDF). June 30, 2026. '
    + CEMIG_URL + "."
)
CEMIG_SID = "cemig_1s26_results_presentation_20260630"


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


GEO = "Cemig GT Minas Gerais transmission footprint (Belo Horizonte HQ pin)."
LAT, LON = "-19.92", "-43.94"

# REA Reforços e Melhorias grande porte CapEx R$924.6m
row_doc(
    "cemig_rea_rm_capex_924p6m_brl", "energy", "power_plants_grid", "other",
    "Cemig — REA Reforços e Melhorias grande porte CapEx R$924.6m",
    "Brazil",
    "30 Jun 2026 Cemig Resultados 1S26/2T26 presentation: Cemig already has REA approval for large-porte Reforços e Melhorias with CapEx totaling R$924.6 million. CapEx: enter REA RM envelope. Distinct from period TX CapEx 1S26 R$275.2m / 2T26 R$165.9m realized faces; pairs with Lote 1 leilão 02/2022 R$242.2m toward COD-year schedule Total R$1,166.787m.",
    "924600000", "2026-06-30", "2026", LAT, LON, GEO,
    CEMIG_SID,
    "A Cemig já tem aprovação (REA) para Reforços e Melhorias de grande porte com CAPEX totalizando R$ 924,6 milhões",
    CEMIG_URL,
    "Actor: Cemig — other. NEW REA RM CapEx. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle304", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(924600000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=CEMIG_CHICAGO,
    annotation="Cemig REA RM CapEx via Fed H.10. Supports cemig_rea_rm_capex_924p6m_brl.",
    evid_note="Opened Cemig 1S26/2T26 RI PDF; REA Reforços e Melhorias CapEx R$924.6m confirmed.",
)

# Lote 1 leilão 02/2022 CapEx R$242.2m
row_doc(
    "cemig_lote1_leilao022022_capex_242p2m_brl", "energy", "power_plants_grid", "other",
    "Cemig — Lote 1 leilão ANEEL 02/2022 CapEx R$242.2m",
    "Brazil",
    "30 Jun 2026 Cemig Resultados 1S26/2T26 presentation: investments of R$242.2 million referring to Lote 1 of auction 02/2022 (works conclusion planned for 2028). CapEx: enter Lote 1 envelope. Distinct from REA RM R$924.6m; together form COD-year CapEx schedule Total R$1,166.787m.",
    "242200000", "2026-06-30", "2026", LAT, LON, GEO,
    CEMIG_SID,
    "além de investimentos de R$242,2 milhões referentes ao Lote 1 do leilão 02/2022 (com conclusão das obras prevista para 2028)",
    CEMIG_URL,
    "Actor: Cemig — other. NEW Lote 1 CapEx. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle304", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(242200000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=CEMIG_CHICAGO,
    annotation="Cemig Lote 1 CapEx via Fed H.10. Supports cemig_lote1_leilao022022_capex_242p2m_brl.",
    evid_note="Opened Cemig 1S26/2T26 RI PDF; Lote 1 leilão 02/2022 CapEx R$242.2m confirmed.",
)

# COD-year CapEx schedule (table labeled Capex - R$ mil)
for rid, year_label, val_thousands, quote in [
    ("cemig_tx_capex_cod2026_263p61m_brl", "2026", 263610, "2026 263.610 42.880"),
    ("cemig_tx_capex_cod2027_491p35m_brl", "2027", 491349, "2027 491.349 81.093"),
    ("cemig_tx_capex_cod2028_403p43m_brl", "2028", 403429, "2028 403.429 46.876"),
    ("cemig_tx_capex_cod2029_8p4m_brl", "2029", 8399, "2029 8.399 1.416"),
    ("cemig_tx_rm_lote1_total_1166p79m_brl", "Total", 1166787, "Total 1.166.787 172.265"),
]:
    val = int(val_thousands * 1000)  # R$ mil → R$
    val_m = val / 1e6
    row_doc(
        rid, "energy", "power_plants_grid", "other",
        f"Cemig — TX CapEx COD {year_label} R${val_m:.2f}m".replace(".00", ""),
        "Brazil",
        f"30 Jun 2026 Cemig Resultados 1S26/2T26 presentation: Previsão de entrada em operação Capex schedule (R$ mil) — {year_label} CapEx R${val_thousands:,} thousand (= R${val_m:.3f} million). CapEx: enter COD-year schedule face for REA RM + Lote 1 package. Nested under REA R$924.6m + Lote 1 R$242.2m envelopes; distinct from period realized TX CapEx.",
        str(val), "2026-06-30", "2026", LAT, LON, GEO,
        CEMIG_SID, quote, CEMIG_URL,
        f"Actor: Cemig — other. NEW TX CapEx COD {year_label}. Shuffle power_plants_grid; other equal-budget.",
        "hunt_cycle304", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago=CEMIG_CHICAGO,
        annotation=f"Cemig TX CapEx COD {year_label} via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Cemig 1S26/2T26 RI PDF; CapEx COD {year_label} R${val_thousands:,} mil confirmed.",
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
    print(f"cycle304 added {len(added)}: {added}")
    print(f"cycle304 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
