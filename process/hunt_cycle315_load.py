#!/usr/bin/env python3
"""Cycle 315 hunt: shuffle_seed=20261315; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261315).shuffle):
(printed at runtime).

Thin top-up: balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: EXIM news scanned (Argentina $7bn framework already
  logged; no new LatAm CapEx faces); Progress Rail VLI R$430m absent; AES
  Arenales CapEx blank; Bechtel/Fluor/Wabtec/Equinix CapEx-fill blanks.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
OTHER: NEW Motiva Capex Proforma 4T25 (col 80) nested roads/rails by concession
  + Outros/Motiva S.A. (airports taxonomy-out; skip Eliminação).
Skipped: thin dry; holdovers unsigned.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from random import Random

import yaml

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "codebook" / "observations.csv"
EVID = ROOT / "data" / "attribution" / "evidence"
BIB = ROOT / "sources" / "bibliography.yml"
FIELDS = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")).fieldnames)
ITEMS: list[tuple[dict, dict, dict]] = []

BRL_USD = "5.1921"
MOTIVA_XLSX_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/8516d569-e11b-4864-a777-68eca8245423/"
    "3d12e316-e0e9-ec78-cfdc-d60e5189d2db?origin=2"
)
MOTIVA_SID = "motiva_capex_proforma_xlsx_2026"
MOTIVA_CHICAGO = (
    'Motiva Infraestrutura de Mobilidade S.A. “Fundamentos — Capex Proforma '
    '(planilha RI).” Retrieved October 5, 2026. ' + MOTIVA_XLSX_URL + "."
)

_sh = [
    "port_ownership", "port_cranes", "rail", "bridges_roads", "building_materials",
    "engineering_epc", "niobium", "lithium", "copper", "nickel", "graphite", "balsa",
    "water", "fission_smr", "solar", "wind", "power_plants_grid", "other_renewables",
]
Random(20261315).shuffle(_sh)


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


def brl_m(val_m: float) -> tuple[str, str]:
    brl = int(round(val_m * 1_000_000))
    usd = round(brl / float(BRL_USD), 2)
    return str(brl), str(usd)


ROADS = [
    ("motiva_roads_4t25_2173m_brl", "Rodovias / Toll Roads", 2172.643,
     "-23.55", "-46.63", "Motiva roads portfolio Brazil (São Paulo HQ pin).", True),
    ("motiva_vialagos_4t25_3m_brl", "ViaLagos", 3.306,
     "-22.97", "-42.03", "ViaLagos concession (RJ Região dos Lagos pin).", False),
    ("motiva_autoban_4t25_244m_brl", "AutoBAn", 244.236,
     "-23.55", "-46.63", "AutoBAn concession (São Paulo metro pin).", False),
    ("motiva_viaoeste_4t25_345m_brl", "ViaOeste", 344.981,
     "-23.50", "-47.45", "ViaOeste concession (SP west corridor pin).", False),
    ("motiva_rodoanel_oeste_4t25_18m_brl", "RodoAnel Oeste", 17.953,
     "-23.55", "-46.85", "RodoAnel Oeste (SP beltway west pin).", False),
    ("motiva_spvias_4t25_40m_brl", "SPVias", 39.977,
     "-23.55", "-48.00", "SPVias concession (SP interior pin).", False),
    ("motiva_viario_4t25_4m_brl", "ViaRio", 4.046,
     "-22.92", "-43.37", "ViaRio concession (Rio de Janeiro west zone pin).", False),
    ("motiva_pantanal_4t25_239m_brl", "Pantanal", 239.228,
     "-20.44", "-54.65", "Motiva Pantanal concession (Campo Grande pin).", False),
    ("motiva_renovias_4t25_33m_brl", "Renovias", 32.695,
     "-22.74", "-47.33", "Renovias concession (SP interior pin).", False),
    ("motiva_viasul_4t25_280m_brl", "Motiva ViaSul", 280.242,
     "-29.68", "-51.12", "Motiva ViaSul (RS corridor pin).", False),
    ("motiva_viacosteira_4t25_120m_brl", "Motiva ViaCosteira", 119.551,
     "-27.60", "-48.55", "Motiva ViaCosteira (SC coast pin).", False),
    ("motiva_rio_sp_4t25_510m_brl", "Motiva Rio-SP", 510.318,
     "-22.90", "-43.20", "Motiva Rio-SP (Rio–São Paulo corridor pin).", False),
    ("motiva_sorocabana_4t25_168m_brl", "Sorocabana", 168.227,
     "-23.50", "-47.46", "Sorocabana concession (Sorocaba pin).", False),
    ("motiva_pr_vias_4t25_168m_brl", "PR Vias", 167.883,
     "-25.43", "-49.27", "PR Vias concession (Curitiba pin).", False),
    ("motiva_outros_4t25_77m_brl", "Outros / Others", 77.316,
     "-23.55", "-46.63", "Motiva S.A. HQ pin (São Paulo).", False),
    ("motiva_sa_4t25_25m_brl", "Motiva S.A.", 25.491,
     "-23.55", "-46.63", "Motiva S.A. HQ pin (São Paulo).", False),
]

for rid, name, val_m, lat, lon, geo, is_agg in ROADS:
    brl, usd = brl_m(val_m)
    mid = int(round(val_m))
    nest = (
        "Nested under / distinct from FY2025 Rodovias R$6,418.473m (not additive)."
        if is_agg
        else "Nested under Rodovias 4T25 R$2,172.643m / FY2025 Rodovias (not additive)."
    )
    row_doc(
        rid, "infrastructure", "bridges_roads", "other",
        f"Motiva — {name} CapEx 4T25 R${mid}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): {name} CapEx "
        f"4T25 R${val_m:,.3f} million. CapEx: enter face. {nest}",
        brl, "2025-12-31", "2025", lat, lon, geo,
        MOTIVA_SID, f"{name} … 4T25={val_m}", MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 4T25 concession CapEx. "
        f"Shuffle bridges_roads; other equal-budget.",
        "hunt_cycle315", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} 4T25 CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} 4T25 R${val_m:,.3f}m confirmed.",
    )

RAILS = [
    ("motiva_rails_4t25_596m_brl", "Trilhos / Rails", 596.392,
     "-23.55", "-46.63", "Motiva rails portfolio Brazil (São Paulo HQ pin).", True),
    ("motiva_viaquatro_4t25_205m_brl", "ViaQuatro", 205.184,
     "-23.55", "-46.63", "ViaQuatro Line 4 (São Paulo metro pin).", False),
    ("motiva_vlt_carioca_4t25_11m_brl", "VLT Carioca", 10.991,
     "-22.90", "-43.18", "VLT Carioca (Rio de Janeiro pin).", False),
    ("motiva_metro_bahia_4t25_36m_brl", "Metrô Bahia", 35.555,
     "-12.97", "-38.50", "Metrô Bahia (Salvador pin).", False),
    ("motiva_viamobilidade_4t25_25m_brl", "ViaMobilidade", 24.543,
     "-23.55", "-46.63", "ViaMobilidade (São Paulo metro pin).", False),
    ("motiva_viamobilidade_l89_4t25_320m_brl", "ViaMobilidade L 8/9", 320.119,
     "-23.55", "-46.70", "ViaMobilidade Lines 8/9 (São Paulo west pin).", False),
]

for rid, name, val_m, lat, lon, geo, is_agg in RAILS:
    brl, usd = brl_m(val_m)
    mid = int(round(val_m))
    nest = (
        "Nested under / distinct from FY2025 Trilhos R$1,299.336m (not additive)."
        if is_agg
        else "Nested under Trilhos 4T25 R$596.392m / FY2025 Trilhos (not additive)."
    )
    row_doc(
        rid, "infrastructure", "rail", "other",
        f"Motiva — {name} CapEx 4T25 R${mid}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): {name} CapEx "
        f"4T25 R${val_m:,.3f} million. CapEx: enter face. {nest}",
        brl, "2025-12-31", "2025", lat, lon, geo,
        MOTIVA_SID, f"{name} … 4T25={val_m}", MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 4T25 rail CapEx. "
        f"Shuffle rail; other equal-budget.",
        "hunt_cycle315", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} 4T25 CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} 4T25 R${val_m:,.3f}m confirmed.",
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
    print("shuffle_order_20261315:", _sh)
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
    print(f"cycle315 added {len(added)}: {added}")
    print(f"cycle315 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
