#!/usr/bin/env python3
"""Cycle 366 hunt: shuffle_seed=20261366; Motiva 2T20 by-concession CapEx.

Shuffle: engineering_epc, solar, fission_smr, bridges_roads, niobium, port_ownership, water, power_plants_grid, balsa, nickel, graphite, rail, copper, wind, building_materials, lithium, port_cranes, other_renewables.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Motiva Capex Proforma 2T20 roads/rails + Outros/Motiva S.A.
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
MOTIVA_XLSX_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/8516d569-e11b-4864-a777-68eca8245423/"
    "3d12e316-e0e9-ec78-cfdc-d60e5189d2db?origin=2"
)
MOTIVA_SID = "motiva_capex_proforma_xlsx_2026"
MOTIVA_CHICAGO = (
    'Motiva Infraestrutura de Mobilidade S.A. “Fundamentos — Capex Proforma '
    '(planilha RI).” Retrieved October 5, 2026. ' + MOTIVA_XLSX_URL + "."
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


def brl_m(val_m: float) -> tuple[str, str]:
    brl = int(round(val_m * 1_000_000))
    usd = round(brl / float(BRL_USD), 2)
    return str(brl), str(usd)


ROADS = [
    ("motiva_roads_2t20_212m_brl", "Rodovias / Toll Roads", 211.90000000000003,
     "-23.55", "-46.63", "Motiva roads portfolio Brazil (São Paulo HQ pin).", True),
    ("motiva_vialagos_2t20_1m_brl", "ViaLagos", 0.6,
     "-22.97", "-42.03", "ViaLagos concession (RJ Região dos Lagos pin).", False),
    ("motiva_autoban_2t20_3m_brl", "AutoBAn", 3.4,
     "-23.55", "-46.63", "AutoBAn concession (São Paulo metro pin).", False),
    ("motiva_viaoeste_2t20_4m_brl", "ViaOeste", 3.5,
     "-23.50", "-47.45", "ViaOeste concession (SP west corridor pin).", False),
    ("motiva_rodoanel_oeste_2t20_2m_brl", "RodoAnel Oeste", 1.7,
     "-23.55", "-46.85", "RodoAnel Oeste (SP beltway west pin).", False),
    ("motiva_spvias_2t20_26m_brl", "SPVias", 25.8,
     "-23.55", "-48.00", "SPVias concession (SP interior pin).", False),
    ("motiva_viario_2t20_0p3m_brl", "ViaRio", 0.3,
     "-22.92", "-43.37", "ViaRio concession (Rio de Janeiro west zone pin).", False),
    ("motiva_pantanal_2t20_10m_brl", "Pantanal", 10.4,
     "-20.44", "-54.65", "Motiva Pantanal concession (Campo Grande pin).", False),
    ("motiva_renovias_2t20_0p4m_brl", "Renovias", 0.4,
     "-22.74", "-47.33", "Renovias concession (SP interior pin).", False),
    ("motiva_viasul_2t20_65m_brl", "Motiva ViaSul", 65.4,
     "-29.68", "-51.12", "Motiva ViaSul (RS corridor pin).", False),
    ("motiva_viacosteira_2t20_5m_brl", "Motiva ViaCosteira", 5.0,
     "-27.60", "-48.55", "Motiva ViaCosteira (SC coast pin).", False),
    ("motiva_outros_2t20_14m_brl", "Outros / Others", 13.8,
     "-23.55", "-46.63", "Motiva S.A. HQ pin (São Paulo).", False)
]

for rid, name, val_m, lat, lon, geo, is_agg in ROADS:
    brl, usd = brl_m(val_m)
    mid = int(round(val_m)) if val_m >= 0.5 else round(val_m, 1)
    label = f"R${mid}m" if isinstance(mid, int) else f"R${mid}m"
    nest = (
        "Nested under / distinct from FY2025 Rodovias (not additive)."
        if is_agg
        else "Nested under Rodovias 2T20 R$905.387m / FY2025 Rodovias (not additive)."
    )
    row_doc(
        rid, "infrastructure", "bridges_roads", "other",
        f"Motiva — {name} CapEx 2T20 {label}",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): {name} CapEx "
        f"2T20 R${val_m:,.3f} million. CapEx: enter face. {nest}",
        brl, "2020-06-30", "2020", lat, lon, geo,
        MOTIVA_SID, f"{name} … 2T20={val_m}", MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 2T20 concession CapEx. "
        f"Shuffle bridges_roads; other equal-budget.",
        "hunt_cycle366", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} 2T20 CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} 2T20 R${val_m:,.3f}m confirmed.",
    )

RAILS = [
    ("motiva_rails_2t20_24m_brl", "Trilhos / Rails", 23.900000000000002,
     "-23.55", "-46.63", "Motiva rails portfolio Brazil (São Paulo HQ pin).", True),
    ("motiva_viaquatro_2t20_17m_brl", "ViaQuatro", 16.6,
     "-23.55", "-46.63", "ViaQuatro Line 4 (São Paulo metro pin).", False),
    ("motiva_vlt_carioca_2t20_1m_brl", "VLT Carioca", 1.1,
     "-22.90", "-43.18", "VLT Carioca (Rio de Janeiro pin).", False),
    ("motiva_viamobilidade_2t20_12m_brl", "ViaMobilidade", 11.6,
     "-23.55", "-46.63", "ViaMobilidade (São Paulo metro pin).", False)
]

for rid, name, val_m, lat, lon, geo, is_agg in RAILS:
    brl, usd = brl_m(val_m)
    mid = int(round(val_m))
    nest = (
        "Nested under / distinct from FY2025 Trilhos (not additive)."
        if is_agg
        else "Nested under Trilhos 2T20 R$212.224m / FY2025 Trilhos (not additive)."
    )
    row_doc(
        rid, "infrastructure", "rail", "other",
        f"Motiva — {name} CapEx 2T20 R${mid}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): {name} CapEx "
        f"2T20 R${val_m:,.3f} million. CapEx: enter face. {nest}",
        brl, "2020-06-30", "2020", lat, lon, geo,
        MOTIVA_SID, f"{name} … 2T20={val_m}", MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 2T20 rail CapEx. "
        f"Shuffle rail; other equal-budget.",
        "hunt_cycle366", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} 2T20 CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} 2T20 R${val_m:,.3f}m confirmed.",
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
    print(f"cycle366 added {len(added)}: {added}")
    print(f"cycle366 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
