#!/usr/bin/env python3
"""Cycle 297 hunt: shuffle_seed=20261297; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261297).shuffle):
engineering_epc, graphite, copper, fission_smr, rail, port_cranes, power_plants_grid,
wind, other_renewables, lithium, balsa, nickel, solar, building_materials,
port_ownership, water, bridges_roads, niobium.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (balsa/nickel mid-shuffle).
≥1/3 U.S. hunt budget: graphite CapEx-fill dry; AES Brasil RI / Equinix /
  Scala/ODATA hosts blocked; Arenales/SSA STS/Bechtel/Progress Rail /
  Wabtec Vale CapEx blanks; fission_smr MoU blanks.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
OTHER: NEW Motiva Capex Proforma 1T26 CapEx excl. maintenance nested
  roads/rails aggregates + by concession.
Skipped: thin dry; US CapEx dry; holdovers unsigned.
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


row_doc(
    "motiva_roads_exmaint_1t26_1263m_brl", "infrastructure", "bridges_roads", "other",
    "Motiva — Rodovias CapEx excl. maint. 1T26 R$1,263m",
    "Brazil",
    "Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): CAPEX excluding Maintenance and Financial Asset — Rodovias / Toll Roads 1T26 R$1,263 million. CapEx: enter ex-maintenance roads aggregate. Distinct from gross Rodovias 1T26 R$1,373m / motiva_1t26_roads_1370m (not additive).",
    "1263000000", "2026-03-31", "2026", "-23.55", "-46.63",
    "Motiva roads portfolio Brazil (São Paulo HQ pin).",
    "motiva_capex_proforma_xlsx_2026",
    "Rodovias / Toll Roads … 1T26=1263",
    MOTIVA_XLSX_URL,
    "Actor: Motiva — other. NEW 1T26 roads CapEx excl. maintenance. Shuffle bridges_roads; other equal-budget.",
    "hunt_cycle297", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1263000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=MOTIVA_CHICAGO,
    annotation="Motiva roads ex-maint 1T26 via Fed H.10. Supports motiva_roads_exmaint_1t26_1263m_brl.",
    evid_note="Opened Motiva Capex Proforma xlsx; Rodovias excl. maint. 1T26 R$1,263m confirmed.",
)

for rid, name, val_m, lat, lon, geo in [
    ("motiva_autoban_exmaint_1t26_30m_brl", "AutoBAn", 30, "-23.55", "-46.63", "AutoBAn concession (São Paulo metro pin)."),
    ("motiva_viaoeste_exmaint_1t26_127m_brl", "ViaOeste", 127, "-23.50", "-47.45", "ViaOeste concession (SP west corridor pin)."),
    ("motiva_rodoanel_oeste_exmaint_1t26_11m_brl", "RodoAnel Oeste", 11, "-23.55", "-46.85", "RodoAnel Oeste (SP beltway west pin)."),
    ("motiva_spvias_exmaint_1t26_54m_brl", "SPVias", 54, "-23.55", "-48.00", "SPVias concession (SP interior pin)."),
    ("motiva_pantanal_exmaint_1t26_160m_brl", "Pantanal", 160, "-20.44", "-54.65", "Motiva Pantanal concession (Campo Grande pin)."),
    ("motiva_viasul_exmaint_1t26_193m_brl", "Motiva ViaSul", 193, "-29.68", "-51.12", "Motiva ViaSul (RS corridor pin)."),
    ("motiva_viacosteira_exmaint_1t26_49m_brl", "Motiva ViaCosteira", 49, "-27.60", "-48.55", "Motiva ViaCosteira (SC coast pin)."),
    ("motiva_rio_sp_exmaint_1t26_312m_brl", "Motiva Rio-SP", 312, "-22.90", "-43.20", "Motiva Rio-SP (Rio–São Paulo corridor pin)."),
    ("motiva_sorocabana_exmaint_1t26_108m_brl", "Sorocabana", 108, "-23.50", "-47.46", "Sorocabana concession (Sorocaba pin)."),
    ("motiva_pr_vias_exmaint_1t26_214m_brl", "PR Vias", 214, "-25.43", "-49.27", "PR Vias concession (Curitiba pin)."),
    ("motiva_viario_exmaint_1t26_2m_brl", "ViaRio", 2, "-22.92", "-43.37", "ViaRio concession (Rio de Janeiro west zone pin)."),
    ("motiva_renovias_exmaint_1t26_2m_brl", "Renovias", 2, "-23.18", "-46.88", "Renovias concession (SP interior pin)."),
    ("motiva_vialagos_exmaint_1t26_1m_brl", "ViaLagos", 1, "-22.88", "-42.02", "ViaLagos concession (RJ lakes region pin)."),
]:
    val = val_m * 1_000_000
    row_doc(
        rid, "infrastructure", "bridges_roads", "other",
        f"Motiva — {name} CapEx excl. maint. 1T26 R${val_m}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): CAPEX excluding Maintenance and Financial Asset — {name} 1T26 R${val_m} million. CapEx: enter ex-maintenance face. Nested under Rodovias excl. maint. 1T26 R$1,263m; distinct from gross 1T26 faces where values differ (not additive).",
        str(val), "2026-03-31", "2026", lat, lon, geo,
        "motiva_capex_proforma_xlsx_2026",
        f"{name} … 1T26={val_m}",
        MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 1T26 CapEx excl. maintenance. Shuffle bridges_roads; other equal-budget.",
        "hunt_cycle297", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} ex-maint 1T26 via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} excl. maint. 1T26 R${val_m}m confirmed.",
    )

row_doc(
    "motiva_rails_exmaint_1t26_195m_brl", "infrastructure", "rail", "other",
    "Motiva — Trilhos CapEx excl. maint. 1T26 R$195m",
    "Brazil",
    "Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): CAPEX excluding Maintenance and Financial Asset — Trilhos / Rails 1T26 R$195 million. CapEx: enter ex-maintenance rails aggregate. Distinct from gross Trilhos 1T26 R$93m / motiva_1t26_rails_93m (not additive).",
    "195000000", "2026-03-31", "2026", "-23.55", "-46.63",
    "Motiva rails portfolio Brazil (São Paulo HQ pin).",
    "motiva_capex_proforma_xlsx_2026",
    "Trilhos / Rails … 1T26=195",
    MOTIVA_XLSX_URL,
    "Actor: Motiva — other. NEW 1T26 rails CapEx excl. maintenance. Shuffle rail; other equal-budget.",
    "hunt_cycle297", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(195000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=MOTIVA_CHICAGO,
    annotation="Motiva rails ex-maint 1T26 via Fed H.10. Supports motiva_rails_exmaint_1t26_195m_brl.",
    evid_note="Opened Motiva Capex Proforma xlsx; Trilhos excl. maint. 1T26 R$195m confirmed.",
)

for rid, name, val_m, lat, lon, geo in [
    ("motiva_viaquatro_exmaint_1t26_68m_brl", "ViaQuatro", 68, "-23.55", "-46.63", "ViaQuatro Line 4 (São Paulo metro pin)."),
    ("motiva_vlt_carioca_exmaint_1t26_3m_brl", "VLT Carioca", 3, "-22.90", "-43.18", "VLT Carioca (Rio de Janeiro pin)."),
    ("motiva_metro_bahia_exmaint_1t26_14m_brl", "Metrô Bahia", 14, "-12.97", "-38.50", "Metrô Bahia (Salvador pin)."),
    ("motiva_viamobilidade_exmaint_1t26_9m_brl", "ViaMobilidade", 9, "-23.55", "-46.63", "ViaMobilidade (São Paulo metro pin)."),
    ("motiva_viamobilidade_l89_exmaint_1t26_101m_brl", "ViaMobilidade L 8/9", 101, "-23.55", "-46.70", "ViaMobilidade Lines 8/9 (São Paulo west pin)."),
]:
    val = val_m * 1_000_000
    row_doc(
        rid, "infrastructure", "rail", "other",
        f"Motiva — {name} CapEx excl. maint. 1T26 R${val_m}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): CAPEX excluding Maintenance and Financial Asset — {name} 1T26 R${val_m} million. CapEx: enter ex-maintenance face. Nested under Trilhos excl. maint. 1T26 R$195m; distinct from gross 1T26 faces where values differ (not additive).",
        str(val), "2026-03-31", "2026", lat, lon, geo,
        "motiva_capex_proforma_xlsx_2026",
        f"{name} … 1T26={val_m}",
        MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 1T26 CapEx excl. maintenance. Shuffle rail; other equal-budget.",
        "hunt_cycle297", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} ex-maint 1T26 via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} excl. maint. 1T26 R${val_m}m confirmed.",
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
    print(f"cycle297 added {len(added)}: {added}")
    print(f"cycle297 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
