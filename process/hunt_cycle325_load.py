#!/usr/bin/env python3
"""Cycle 325 hunt: shuffle_seed=20261325; Motiva 3T24 by-concession CapEx.

Shuffle: other_renewables, port_cranes, bridges_roads, building_materials, graphite,
water, port_ownership, rail, niobium, engineering_epc, balsa, power_plants_grid,
copper, lithium, wind, solar, nickel, fission_smr.

Thin top-up balsa/nickel/fission_smr dry. ≥1/3 US CapEx dry.
OTHER: NEW Motiva Capex Proforma 3T24 (col 74) roads/rails + Outros/Motiva S.A.
  (ViaOeste/Sorocabana/PR Vias/Minas_SP 0 skipped; Samm/airports taxonomy-out).
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
    ("motiva_roads_3t24_975m_brl", "Rodovias / Toll Roads", 975.242,
     "-23.55", "-46.63", "Motiva roads portfolio Brazil (São Paulo HQ pin).", True),
    ("motiva_vialagos_3t24_2m_brl", "ViaLagos", 1.864,
     "-22.97", "-42.03", "ViaLagos concession (RJ Região dos Lagos pin).", False),
    ("motiva_autoban_3t24_166m_brl", "AutoBAn", 165.67899999999997,
     "-23.55", "-46.63", "AutoBAn concession (São Paulo metro pin).", False),
    ("motiva_rodoanel_oeste_3t24_20m_brl", "RodoAnel Oeste", 19.893,
     "-23.55", "-46.85", "RodoAnel Oeste (SP beltway west pin).", False),
    ("motiva_spvias_3t24_51m_brl", "SPVias", 50.678000000000004,
     "-23.55", "-48.00", "SPVias concession (SP interior pin).", False),
    ("motiva_viario_3t24_1m_brl", "ViaRio", 1.381,
     "-22.92", "-43.37", "ViaRio concession (Rio de Janeiro west zone pin).", False),
    ("motiva_pantanal_3t24_4m_brl", "Pantanal", 3.942,
     "-20.44", "-54.65", "Motiva Pantanal concession (Campo Grande pin).", False),
    ("motiva_renovias_3t24_3m_brl", "Renovias", 2.579,
     "-22.74", "-47.33", "Renovias concession (SP interior pin).", False),
    ("motiva_viasul_3t24_181m_brl", "Motiva ViaSul", 180.943,
     "-29.68", "-51.12", "Motiva ViaSul (RS corridor pin).", False),
    ("motiva_viacosteira_3t24_85m_brl", "Motiva ViaCosteira", 84.804,
     "-27.60", "-48.55", "Motiva ViaCosteira (SC coast pin).", False),
    ("motiva_rio_sp_3t24_465m_brl", "Motiva Rio-SP", 465.38,
     "-22.90", "-43.20", "Motiva Rio-SP (Rio–São Paulo corridor pin).", False),
    ("motiva_outros_3t24_12m_brl", "Outros / Others", 11.826,
     "-23.55", "-46.63", "Motiva S.A. HQ pin (São Paulo).", False),
    ("motiva_sa_3t24_47m_brl", "Motiva S.A.", 47.327,
     "-23.55", "-46.63", "Motiva S.A. HQ pin (São Paulo).", False)
]

for rid, name, val_m, lat, lon, geo, is_agg in ROADS:
    brl, usd = brl_m(val_m)
    mid = int(round(val_m)) if val_m >= 0.5 else round(val_m, 1)
    label = f"R${mid}m" if isinstance(mid, int) else f"R${mid}m"
    nest = (
        "Nested under / distinct from FY2024 Rodovias (not additive)."
        if is_agg
        else "Nested under Rodovias 3T24 R$975.242m / FY2024 Rodovias (not additive)."
    )
    row_doc(
        rid, "infrastructure", "bridges_roads", "other",
        f"Motiva — {name} CapEx 3T24 {label}",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): {name} CapEx "
        f"3T24 R${val_m:,.3f} million. CapEx: enter face. {nest}",
        brl, "2024-09-30", "2024", lat, lon, geo,
        MOTIVA_SID, f"{name} … 3T24={val_m}", MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 3T24 concession CapEx. "
        f"Shuffle bridges_roads; other equal-budget.",
        "hunt_cycle325", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} 3T24 CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} 3T24 R${val_m:,.3f}m confirmed.",
    )

RAILS = [
    ("motiva_rails_3t24_410m_brl", "Trilhos / Rails", 409.65299999999996,
     "-23.55", "-46.63", "Motiva rails portfolio Brazil (São Paulo HQ pin).", True),
    ("motiva_viaquatro_3t24_3m_brl", "ViaQuatro", 2.5690000000000026,
     "-23.55", "-46.63", "ViaQuatro Line 4 (São Paulo metro pin).", False),
    ("motiva_vlt_carioca_3t24_9m_brl", "VLT Carioca", 8.558000000000002,
     "-22.90", "-43.18", "VLT Carioca (Rio de Janeiro pin).", False),
    ("motiva_metro_bahia_3t24_14m_brl", "Metrô Bahia", 13.844,
     "-12.97", "-38.50", "Metrô Bahia (Salvador pin).", False),
    ("motiva_viamobilidade_3t24_45m_brl", "ViaMobilidade", 45.455,
     "-23.55", "-46.63", "ViaMobilidade (São Paulo metro pin).", False),
    ("motiva_viamobilidade_l89_3t24_339m_brl", "ViaMobilidade L 8/9", 339.227,
     "-23.55", "-46.70", "ViaMobilidade Lines 8/9 (São Paulo west pin).", False)
]

for rid, name, val_m, lat, lon, geo, is_agg in RAILS:
    brl, usd = brl_m(val_m)
    mid = int(round(val_m))
    nest = (
        "Nested under / distinct from FY2024 Trilhos (not additive)."
        if is_agg
        else "Nested under Trilhos 3T24 R$409.653m / FY2024 Trilhos (not additive)."
    )
    row_doc(
        rid, "infrastructure", "rail", "other",
        f"Motiva — {name} CapEx 3T24 R${mid}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): {name} CapEx "
        f"3T24 R${val_m:,.3f} million. CapEx: enter face. {nest}",
        brl, "2024-09-30", "2024", lat, lon, geo,
        MOTIVA_SID, f"{name} … 3T24={val_m}", MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 3T24 rail CapEx. "
        f"Shuffle rail; other equal-budget.",
        "hunt_cycle325", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} 3T24 CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} 3T24 R${val_m:,.3f}m confirmed.",
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
    print(f"cycle325 added {len(added)}: {added}")
    print(f"cycle325 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
