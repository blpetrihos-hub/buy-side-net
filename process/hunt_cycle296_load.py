#!/usr/bin/env python3
"""Cycle 296 hunt: shuffle_seed=20261296; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261296).shuffle):
graphite, other_renewables, port_cranes, bridges_roads, copper, wind, port_ownership,
lithium, engineering_epc, fission_smr, rail, solar, niobium, power_plants_grid,
balsa, water, nickel, building_materials.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: graphite CapEx-fill dry; embassy/Commerce/State hosts 403;
  Arenales/SSA STS/Bechtel/Progress Rail still open; DFC Honduras microfinance
  taxonomy-out.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
OTHER: NEW Motiva Capex Proforma 2T26 CapEx excl. maintenance nested roads/rails
  by concession; Outros 1T26; ViaRio 1T26.
Skipped: thin dry; graphite CapEx-fill dry; US CapEx dry; holdovers unsigned.
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


# Motiva Capex excl. maintenance 2T26 nested roads
for rid, name, val_m, lat, lon, geo in [
    ("motiva_autoban_exmaint_2t26_44m_brl", "AutoBAn", 44, "-23.55", "-46.63", "AutoBAn concession (São Paulo metro pin)."),
    ("motiva_viaoeste_exmaint_2t26_133m_brl", "ViaOeste", 133, "-23.50", "-47.45", "ViaOeste concession (SP west corridor pin)."),
    ("motiva_rodoanel_oeste_exmaint_2t26_17m_brl", "RodoAnel Oeste", 17, "-23.55", "-46.85", "RodoAnel Oeste (SP beltway west pin)."),
    ("motiva_spvias_exmaint_2t26_50m_brl", "SPVias", 50, "-23.55", "-48.00", "SPVias concession (SP interior pin)."),
    ("motiva_pantanal_exmaint_2t26_204m_brl", "Pantanal", 204, "-20.44", "-54.65", "Motiva Pantanal concession (Campo Grande pin)."),
    ("motiva_viasul_exmaint_2t26_178m_brl", "Motiva ViaSul", 178, "-29.68", "-51.12", "Motiva ViaSul (RS corridor pin)."),
    ("motiva_viacosteira_exmaint_2t26_70m_brl", "Motiva ViaCosteira", 70, "-27.60", "-48.55", "Motiva ViaCosteira (SC coast pin)."),
    ("motiva_rio_sp_exmaint_2t26_334m_brl", "Motiva Rio-SP", 334, "-22.90", "-43.20", "Motiva Rio-SP (Rio–São Paulo corridor pin)."),
    ("motiva_sorocabana_exmaint_2t26_126m_brl", "Sorocabana", 126, "-23.50", "-47.46", "Sorocabana concession (Sorocaba pin)."),
    ("motiva_pr_vias_exmaint_2t26_185m_brl", "PR Vias", 185, "-25.43", "-49.27", "PR Vias concession (Curitiba pin)."),
    ("motiva_minas_sp_exmaint_2t26_116m_brl", "Minas_SP (Fernão Dias)", 116, "-22.32", "-45.00", "Minas_SP / Fernão Dias corridor pin."),
]:
    val = val_m * 1_000_000
    row_doc(
        rid, "infrastructure", "bridges_roads", "other",
        f"Motiva — {name} CapEx excl. maint. 2T26 R${val_m}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): CAPEX excluding Maintenance and Financial Asset — {name} 2T26 R${val_m} million. CapEx: enter ex-maintenance face. Nested under Rodovias excl. maint. 2T26 R$1,454m; distinct from gross concession 2T26 faces where values differ (not additive).",
        str(val), "2026-06-30", "2026", lat, lon, geo,
        "motiva_capex_proforma_xlsx_2026",
        f"{name} … 2T26={val_m}",
        MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 2T26 CapEx excl. maintenance. Shuffle bridges_roads; other equal-budget.",
        "hunt_cycle296", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} ex-maint 2T26 via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} excl. maint. 2T26 R${val_m}m confirmed.",
    )

# Motiva Capex excl. maintenance 2T26 nested rails + rails aggregate
row_doc(
    "motiva_rails_exmaint_2t26_208m_brl", "infrastructure", "rail", "other",
    "Motiva — Trilhos CapEx excl. maint. 2T26 R$208m",
    "Brazil",
    "Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): CAPEX excluding Maintenance and Financial Asset — Trilhos / Rails 2T26 R$208 million. CapEx: enter ex-maintenance rails aggregate. Distinct from gross Trilhos 2T26 R$175m news face (not additive).",
    "208000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Motiva rails portfolio Brazil (São Paulo HQ pin).",
    "motiva_capex_proforma_xlsx_2026",
    "Trilhos / Rails … 2T26=208",
    MOTIVA_XLSX_URL,
    "Actor: Motiva — other. NEW 2T26 rails CapEx excl. maintenance. Shuffle rail; other equal-budget.",
    "hunt_cycle296", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(208000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=MOTIVA_CHICAGO,
    annotation="Motiva rails ex-maint 2T26 via Fed H.10. Supports motiva_rails_exmaint_2t26_208m_brl.",
    evid_note="Opened Motiva Capex Proforma xlsx; Trilhos excl. maint. 2T26 R$208m confirmed.",
)

for rid, name, val_m, lat, lon, geo in [
    ("motiva_viaquatro_exmaint_2t26_72m_brl", "ViaQuatro", 72, "-23.55", "-46.63", "ViaQuatro Line 4 (São Paulo metro pin)."),
    ("motiva_vlt_carioca_exmaint_2t26_20m_brl", "VLT Carioca", 20, "-22.90", "-43.18", "VLT Carioca (Rio de Janeiro pin)."),
    ("motiva_metro_bahia_exmaint_2t26_18m_brl", "Metrô Bahia", 18, "-12.97", "-38.50", "Metrô Bahia (Salvador pin)."),
    ("motiva_viamobilidade_exmaint_2t26_13m_brl", "ViaMobilidade", 13, "-23.55", "-46.63", "ViaMobilidade (São Paulo metro pin)."),
    ("motiva_viamobilidade_l89_exmaint_2t26_85m_brl", "ViaMobilidade L 8/9", 85, "-23.55", "-46.70", "ViaMobilidade Lines 8/9 (São Paulo west pin)."),
]:
    val = val_m * 1_000_000
    row_doc(
        rid, "infrastructure", "rail", "other",
        f"Motiva — {name} CapEx excl. maint. 2T26 R${val_m}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): CAPEX excluding Maintenance and Financial Asset — {name} 2T26 R${val_m} million. CapEx: enter ex-maintenance face. Nested under Trilhos excl. maint. 2T26 R$208m; distinct from gross 2T26 faces where values differ (not additive).",
        str(val), "2026-06-30", "2026", lat, lon, geo,
        "motiva_capex_proforma_xlsx_2026",
        f"{name} … 2T26={val_m}",
        MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW 2T26 CapEx excl. maintenance. Shuffle rail; other equal-budget.",
        "hunt_cycle296", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} ex-maint 2T26 via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} excl. maint. 2T26 R${val_m}m confirmed.",
    )

# Motiva Outros 1T26 + ViaRio 1T26
row_doc(
    "motiva_outros_1t26_13m_brl", "infrastructure", "bridges_roads", "other",
    "Motiva — Outros / Motiva S.A. CapEx 1T26 R$13m",
    "Brazil",
    "Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): Outros / Others and Motiva S.A. CapEx 1T26 R$13 million. CapEx: enter holding/other CapEx face. Nested under Consolidated 1T26 R$1,479m (not additive).",
    "13000000", "2026-03-31", "2026", "-23.55", "-46.63",
    "Motiva S.A. HQ pin (São Paulo).",
    "motiva_capex_proforma_xlsx_2026",
    "Outros / Others … 1T26=13 … Motiva S.A. … 1T26=13",
    MOTIVA_XLSX_URL,
    "Actor: Motiva S.A. — other. NEW 1T26 Outros CapEx. Shuffle bridges_roads; other equal-budget.",
    "hunt_cycle296", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(13000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=MOTIVA_CHICAGO,
    annotation="Motiva Outros 1T26 CapEx via Fed H.10. Supports motiva_outros_1t26_13m_brl.",
    evid_note="Opened Motiva Capex Proforma xlsx; Outros/Motiva S.A. 1T26 R$13m confirmed.",
)

row_doc(
    "motiva_viario_1t26_2m_brl", "infrastructure", "bridges_roads", "other",
    "Motiva — ViaRio CapEx 1T26 R$2m",
    "Brazil",
    "Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): Conces. ViaRio S.A. CapEx 1T26 R$2 million. CapEx: enter face. Nested under Rodovias 1T26 R$1,373m (not additive).",
    "2000000", "2026-03-31", "2026", "-22.92", "-43.37",
    "ViaRio concession (Rio de Janeiro west zone pin).",
    "motiva_capex_proforma_xlsx_2026",
    "Conces. ViaRio S.A … 1T26=2",
    MOTIVA_XLSX_URL,
    "Actor: Motiva ViaRio — other. NEW 1T26 CapEx. Shuffle bridges_roads; other equal-budget.",
    "hunt_cycle296", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=MOTIVA_CHICAGO,
    annotation="Motiva ViaRio 1T26 CapEx via Fed H.10. Supports motiva_viario_1t26_2m_brl.",
    evid_note="Opened Motiva Capex Proforma xlsx; ViaRio 1T26 R$2m confirmed.",
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
    print(f"cycle296 added {len(added)}: {added}")
    print(f"cycle296 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
