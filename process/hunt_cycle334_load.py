#!/usr/bin/env python3
"""Cycle 334 hunt: shuffle_seed=20261334; Motiva 3T23 excl.-maintenance CapEx.

Shuffle: copper, bridges_roads, power_plants_grid, nickel, rail, wind, water, fission_smr, balsa, niobium, engineering_epc, building_materials, graphite, lithium, port_cranes, solar, other_renewables, port_ownership.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Motiva Capex Proforma 3T23 excl.-maintenance roads/rails + Outros/Motiva S.A.
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
    ("motiva_roads_exmaint_3t23_647m_brl", "Rodovias / Toll Roads", 646.802,
     "-23.55", "-46.63", "Motiva roads portfolio Brazil (São Paulo HQ pin).", True),
    ("motiva_vialagos_exmaint_3t23_1m_brl", "ViaLagos", 1.097,
     "-22.97", "-42.03", "ViaLagos concession (RJ Região dos Lagos pin).", False),
    ("motiva_autoban_exmaint_3t23_31m_brl", "AutoBAn", 30.821,
     "-23.55", "-46.63", "AutoBAn concession (São Paulo metro pin).", False),
    ("motiva_rodoanel_oeste_exmaint_3t23_12m_brl", "RodoAnel Oeste", 12.091,
     "-23.55", "-46.85", "RodoAnel Oeste (SP beltway west pin).", False),
    ("motiva_spvias_exmaint_3t23_46m_brl", "SPVias", 45.573,
     "-23.55", "-48.00", "SPVias concession (SP interior pin).", False),
    ("motiva_viario_exmaint_3t23_1m_brl", "ViaRio", 1.238,
     "-22.92", "-43.37", "ViaRio concession (Rio de Janeiro west zone pin).", False),
    ("motiva_pantanal_exmaint_3t23_1m_brl", "Pantanal", 1.105,
     "-20.44", "-54.65", "Motiva Pantanal concession (Campo Grande pin).", False),
    ("motiva_renovias_exmaint_3t23_10m_brl", "Renovias", 9.601,
     "-22.74", "-47.33", "Renovias concession (SP interior pin).", False),
    ("motiva_viasul_exmaint_3t23_133m_brl", "Motiva ViaSul", 132.598,
     "-29.68", "-51.12", "Motiva ViaSul (RS corridor pin).", False),
    ("motiva_viacosteira_exmaint_3t23_111m_brl", "Motiva ViaCosteira", 111.368,
     "-27.60", "-48.55", "Motiva ViaCosteira (SC coast pin).", False),
    ("motiva_rio_sp_exmaint_3t23_275m_brl", "Motiva Rio-SP", 274.545,
     "-22.90", "-43.20", "Motiva Rio-SP (Rio–São Paulo corridor pin).", False)
]

for rid, name, val_m, lat, lon, geo, is_agg in ROADS:
    brl, usd = brl_m(val_m)
    mid = int(round(val_m))
    nest = (
        "Distinct from gross Rodovias 3T23 R$1,402.744m (not additive)."
        if is_agg
        else "Nested under Rodovias excl. maint. 3T23 R$1,185.923m; distinct from "
        "gross concession 3T23 faces where values differ (not additive)."
    )
    row_doc(
        rid, "infrastructure", "bridges_roads", "other",
        f"Motiva — {name} CapEx excl. maint. 3T23 R${mid}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): CAPEX excluding "
        f"Maintenance and Financial Asset — {name} 3T23 R${val_m:,.3f} million. "
        f"CapEx: enter ex-maintenance face. {nest}",
        brl, "2023-09-30", "2023", lat, lon, geo,
        MOTIVA_SID, f"excl. maint {name} … 3T23={val_m}", MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 3T23 CapEx excl. maintenance. "
        f"Shuffle bridges_roads; other equal-budget.",
        "hunt_cycle334", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} 3T23 CapEx excl. maint. via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} excl. maint. 3T23 R${val_m:,.3f}m confirmed.",
    )

RAILS = [
    ("motiva_rails_exmaint_3t23_368m_brl", "Trilhos / Rails", 368.026,
     "-23.55", "-46.63", "Motiva rails portfolio Brazil (São Paulo HQ pin).", True),
    ("motiva_viaquatro_exmaint_3t23_18m_brl", "ViaQuatro", 17.803,
     "-23.55", "-46.63", "ViaQuatro Line 4 (São Paulo metro pin).", False),
    ("motiva_vlt_carioca_exmaint_3t23_64m_brl", "VLT Carioca", 63.912,
     "-22.90", "-43.18", "VLT Carioca (Rio de Janeiro pin).", False),
    ("motiva_metro_bahia_exmaint_3t23_28m_brl", "Metrô Bahia", 27.736,
     "-12.97", "-38.50", "Metrô Bahia (Salvador pin).", False),
    ("motiva_viamobilidade_exmaint_3t23_32m_brl", "ViaMobilidade", 32.478,
     "-23.55", "-46.63", "ViaMobilidade (São Paulo metro pin).", False),
    ("motiva_viamobilidade_l89_exmaint_3t23_226m_brl", "ViaMobilidade L 8/9", 226.097,
     "-23.55", "-46.70", "ViaMobilidade Lines 8/9 (São Paulo west pin).", False)
]

for rid, name, val_m, lat, lon, geo, is_agg in RAILS:
    brl, usd = brl_m(val_m)
    mid = int(round(val_m))
    nest = (
        "Distinct from gross Trilhos 3T23 R$198.308m (not additive)."
        if is_agg
        else "Nested under Trilhos excl. maint. 3T23 R$203.454m; distinct from "
        "gross concession 3T23 faces where values differ (not additive)."
    )
    row_doc(
        rid, "infrastructure", "rail", "other",
        f"Motiva — {name} CapEx excl. maint. 3T23 R${mid}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): CAPEX excluding "
        f"Maintenance and Financial Asset — {name} 3T23 R${val_m:,.3f} million. "
        f"CapEx: enter ex-maintenance face. {nest}",
        brl, "2023-09-30", "2023", lat, lon, geo,
        MOTIVA_SID, f"excl. maint {name} … 3T23={val_m}", MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 3T23 CapEx excl. maintenance. "
        f"Shuffle rail; other equal-budget.",
        "hunt_cycle334", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} 3T23 CapEx excl. maint. via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} excl. maint. 3T23 R${val_m:,.3f}m confirmed.",
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
    print(f"cycle334 added {len(added)}: {added}")
    print(f"cycle334 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
