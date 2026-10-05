#!/usr/bin/env python3
"""Cycle 308 hunt: shuffle_seed=20261308; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261308).shuffle):
port_ownership, niobium, graphite, building_materials, rail, nickel, fission_smr,
other_renewables, bridges_roads, lithium, copper, power_plants_grid, port_cranes,
balsa, wind, water, solar, engineering_epc.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (nickel sixth / fission_smr seventh / balsa fourteenth in shuffle).
≥1/3 U.S. hunt budget: AES Andes Arenales CapEx blank (AR MW/COD only); Progress
  Rail VLI R$430m absent; Bechtel QB2 desal / Fluor CapEx-fill blanks; Wabtec Vale
  CapEx blank; SSA Guaymas STS dollar blank; Equinix SP USD109m SEC 403.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
OTHER: NEW Motiva Capex Proforma FY2025 (col 81) nested roads/rails by concession
  under motiva_fy2025_roads_65bn_brl / motiva_fy2025_rails_13bn_brl envelopes
  (not additive to news aggregates; airports taxonomy-out).
Skipped: thin dry; airports FY2025 R$780.9m taxonomy-out; holdovers unsigned.
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
    """Return (value_brl_str, value_usd_str) from R$ millions face."""
    brl = int(round(val_m * 1_000_000))
    usd = round(brl / float(BRL_USD), 2)
    return str(brl), str(usd)


# Motiva Capex Proforma FY2025 (col 81) nested roads — values R$ millions
ROADS_FY2025 = [
    ("motiva_vialagos_fy2025_7m_brl", "ViaLagos", 7.217, "-22.97", "-42.03",
     "ViaLagos concession (RJ Região dos Lagos pin)."),
    ("motiva_autoban_fy2025_923m_brl", "AutoBAn", 922.962, "-23.55", "-46.63",
     "AutoBAn concession (São Paulo metro pin)."),
    ("motiva_viaoeste_fy2025_791m_brl", "ViaOeste", 790.775, "-23.50", "-47.45",
     "ViaOeste concession (SP west corridor pin)."),
    ("motiva_rodoanel_oeste_fy2025_76m_brl", "RodoAnel Oeste", 76.429, "-23.55", "-46.85",
     "RodoAnel Oeste (SP beltway west pin)."),
    ("motiva_spvias_fy2025_132m_brl", "SPVias", 132.167, "-23.55", "-48.00",
     "SPVias concession (SP interior pin)."),
    ("motiva_viario_fy2025_6m_brl", "ViaRio", 6.373, "-22.92", "-43.37",
     "ViaRio concession (Rio de Janeiro west zone pin)."),
    ("motiva_pantanal_fy2025_390m_brl", "Pantanal", 389.961, "-20.44", "-54.65",
     "Motiva Pantanal concession (Campo Grande pin)."),
    ("motiva_renovias_fy2025_61m_brl", "Renovias", 61.304, "-22.74", "-47.33",
     "Renovias concession (SP interior pin)."),
    ("motiva_viasul_fy2025_1026m_brl", "Motiva ViaSul", 1026.108, "-29.68", "-51.12",
     "Motiva ViaSul (RS corridor pin)."),
    ("motiva_viacosteira_fy2025_411m_brl", "Motiva ViaCosteira", 411.079, "-27.60", "-48.55",
     "Motiva ViaCosteira (SC coast pin)."),
    ("motiva_rio_sp_fy2025_1723m_brl", "Motiva Rio-SP", 1722.811, "-22.90", "-43.20",
     "Motiva Rio-SP (Rio–São Paulo corridor pin)."),
    ("motiva_sorocabana_fy2025_465m_brl", "Sorocabana", 465.448, "-23.50", "-47.46",
     "Sorocabana concession (Sorocaba pin)."),
    ("motiva_pr_vias_fy2025_406m_brl", "PR Vias", 405.839, "-25.43", "-49.27",
     "PR Vias concession (Curitiba pin)."),
]

for rid, name, val_m, lat, lon, geo in ROADS_FY2025:
    brl, usd = brl_m(val_m)
    mid = int(round(val_m))
    row_doc(
        rid, "infrastructure", "bridges_roads", "other",
        f"Motiva — {name} CapEx FY2025 R${mid}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): {name} CapEx "
        f"FY2025 R${val_m:,.3f} million. CapEx: enter face. Nested under Rodovias "
        f"FY2025 R$6,418.473m / motiva_fy2025_roads_65bn_brl news aggregate "
        f"(not additive).",
        brl, "2025-12-31", "2025", lat, lon, geo,
        MOTIVA_SID,
        f"{name} … FY2025={val_m}",
        MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW FY2025 concession CapEx. "
        f"Shuffle bridges_roads; other equal-budget.",
        "hunt_cycle308", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} FY2025 CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} FY2025 R${val_m:,.3f}m confirmed.",
    )

# Motiva Capex Proforma FY2025 nested rails
RAILS_FY2025 = [
    ("motiva_viaquatro_fy2025_257m_brl", "ViaQuatro", 256.909, "-23.55", "-46.63",
     "ViaQuatro Line 4 (São Paulo metro pin)."),
    ("motiva_vlt_carioca_fy2025_39m_brl", "VLT Carioca", 38.65, "-22.90", "-43.18",
     "VLT Carioca (Rio de Janeiro pin)."),
    ("motiva_metro_bahia_fy2025_89m_brl", "Metrô Bahia", 89.392, "-12.97", "-38.50",
     "Metrô Bahia (Salvador pin)."),
    ("motiva_viamobilidade_fy2025_84m_brl", "ViaMobilidade", 84.014, "-23.55", "-46.63",
     "ViaMobilidade (São Paulo metro pin)."),
    ("motiva_viamobilidade_l89_fy2025_830m_brl", "ViaMobilidade L 8/9", 830.371,
     "-23.55", "-46.70", "ViaMobilidade Lines 8/9 (São Paulo west pin)."),
]

for rid, name, val_m, lat, lon, geo in RAILS_FY2025:
    brl, usd = brl_m(val_m)
    mid = int(round(val_m))
    row_doc(
        rid, "infrastructure", "rail", "other",
        f"Motiva — {name} CapEx FY2025 R${mid}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): {name} CapEx "
        f"FY2025 R${val_m:,.3f} million. CapEx: enter face. Nested under Trilhos "
        f"FY2025 R$1,299.336m / motiva_fy2025_rails_13bn_brl news aggregate "
        f"(not additive).",
        brl, "2025-12-31", "2025", lat, lon, geo,
        MOTIVA_SID,
        f"{name} … FY2025={val_m}",
        MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW FY2025 rail CapEx. "
        f"Shuffle rail; other equal-budget.",
        "hunt_cycle308", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} FY2025 CapEx via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} FY2025 R${val_m:,.3f}m confirmed.",
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
    print(f"cycle308 added {len(added)}: {added}")
    print(f"cycle308 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
