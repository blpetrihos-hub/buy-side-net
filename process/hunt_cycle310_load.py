#!/usr/bin/env python3
"""Cycle 310 hunt: shuffle_seed=20261310; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261310).shuffle):
rail, water, balsa, engineering_epc, niobium, solar, wind, lithium, copper,
other_renewables, port_ownership, bridges_roads, nickel, building_materials,
power_plants_grid, fission_smr, graphite, port_cranes.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (balsa third / nickel thirteenth / fission_smr sixteenth in shuffle).
≥1/3 U.S. hunt budget: Progress Rail news page open but VLI R$430m absent;
  AES Andes prensa JS (Arenales CapEx blank); DFC media scanned (no new LatAm
  CapEx faces); Bechtel/Fluor/Wabtec/Equinix CapEx-fill blanks.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
OTHER: NEW Motiva Capex Proforma FY2025 Outros / Motiva S.A. (+ excl.-maint
  Outros); NEW Aegea Societário CapEx/Investimentos 2T26/6M26 + Outorgas 6M26
  aggregate — nested vs ecosystem CapEx perimeter.
Skipped: thin dry; Motiva airports taxonomy-out; holdovers unsigned.
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
AEGEA_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/"
    "059c8a63-d6dc-b073-bb33-76e316044799?origin=2"
)
AEGEA_SID = "aegea_2t26_6m26_release_mziq"
AEGEA_CHICAGO = (
    'Aegea Saneamento e Participações S.A. “Release de Resultados 2T26 / 6M26.” '
    + AEGEA_URL + "."
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


# Motiva FY2025 Outros / Motiva S.A. (gross + excl-maint Outros)
for rid, name, val_m, excl, lat, lon, geo in [
    ("motiva_outros_fy2025_116m_brl", "Outros / Others", 116.105, False,
     "-23.55", "-46.63", "Motiva S.A. HQ pin (São Paulo)."),
    ("motiva_sa_fy2025_78m_brl", "Motiva S.A.", 78.17, False,
     "-23.55", "-46.63", "Motiva S.A. HQ pin (São Paulo)."),
    ("motiva_outros_exmaint_fy2025_69m_brl", "Outros / Others", 69.043, True,
     "-23.55", "-46.63", "Motiva S.A. HQ pin (São Paulo)."),
    ("motiva_sa_exmaint_fy2025_78m_brl", "Motiva S.A.", 78.17, True,
     "-23.55", "-46.63", "Motiva S.A. HQ pin (São Paulo)."),
]:
    brl, usd = brl_m(val_m)
    mid = int(round(val_m))
    label = "CapEx excl. maint." if excl else "CapEx"
    nest = (
        "Nested under Consolidated FY2025 / distinct from roads/rails FY2025 faces "
        "(not additive; airports taxonomy-out)."
        if not excl
        else "Nested under excl.-maint Consolidated FY2025; distinct from gross "
        "Outros/Motiva S.A. FY2025 faces where values differ (not additive)."
    )
    quote_prefix = "excl. maint " if excl else ""
    row_doc(
        rid, "infrastructure", "bridges_roads", "other",
        f"Motiva — {name} {label} FY2025 R${mid}m",
        "Brazil",
        f"Motiva RI Capex Proforma spreadsheet (retrieved 5 Oct 2026): "
        f"{'CAPEX excluding Maintenance and Financial Asset — ' if excl else ''}"
        f"{name} FY2025 R${val_m:,.3f} million. CapEx: enter face. {nest}",
        brl, "2025-12-31", "2025", lat, lon, geo,
        MOTIVA_SID,
        f"{quote_prefix}{name} … FY2025={val_m}",
        MOTIVA_XLSX_URL,
        f"Actor: Motiva ({name}) — other. NEW FY2025 {label}. "
        f"Shuffle bridges_roads; other equal-budget.",
        "hunt_cycle310", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=MOTIVA_CHICAGO,
        annotation=f"Motiva {name} FY2025 {label} via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Motiva Capex Proforma xlsx; {name} FY2025 R${val_m:,.3f}m confirmed.",
    )

# Aegea Societário CapEx / Investimentos 2T26/6M26 + Outorgas 6M26
AEGEA_FACES = [
    ("aegea_societario_capex_2t26_1480m_brl", "water",
     "Aegea — Capex Societário 2T26 R$1,480m",
     "Aegea 2T26/6M26 earnings release: Capex Societário R$1,480 million in 2T26 "
     "(+21.5% vs 2T25 R$1,218m); narrower perimeter than Capex Ecossistema R$1,828m. "
     "CapEx: enter Societário face. Nested vs / distinct from "
     "aegea_2t26_ecosystem_capex_1828m_brl (not additive).",
     1480, "2026-06-30", "2026",
     "Capex Societário 1.480 1.218 21,5% 2.744 2.230 23,1%",
     "Aegea Societário Brazil water concessions (São Paulo HQ pin)."),
    ("aegea_societario_capex_6m26_2744m_brl", "water",
     "Aegea — Capex Societário 6M26 R$2,744m",
     "Aegea 2T26/6M26 earnings release: Capex Societário R$2,744 million in 6M26 "
     "(+23.1% vs 6M25 R$2,230m). CapEx: enter Societário 6M26 face. Nested vs "
     "aegea_societario_capex_2t26_1480m_brl / aegea_6m26_ecosystem_capex_3407m_brl "
     "(not additive).",
     2744, "2026-06-30", "2026",
     "Capex Societário 1.480 1.218 21,5% 2.744 2.230 23,1%",
     "Aegea Societário Brazil water concessions (São Paulo HQ pin)."),
    ("aegea_societario_investimentos_2t26_1554m_brl", "water",
     "Aegea — Investimentos Societário 2T26 R$1,554m",
     "Aegea 2T26/6M26 earnings release: Investimentos Aegea Societário R$1,554 "
     "million in 2T26 (+16.4% vs 2T25 R$1,335m) including outorgas within Societário "
     "perimeter. CapEx/investments: enter face. Nested vs Capex Societário R$1,480m / "
     "ecosystem Investimentos R$1,901m (not additive).",
     1554, "2026-06-30", "2026",
     "Investimentos Aegea Societário 1.554 1.335 16,4% 3.145 2.399 31,1%",
     "Aegea Societário Brazil water concessions (São Paulo HQ pin)."),
    ("aegea_societario_investimentos_6m26_3145m_brl", "water",
     "Aegea — Investimentos Societário 6M26 R$3,145m",
     "Aegea 2T26/6M26 earnings release: Investimentos Aegea Societário R$3,145 "
     "million in 6M26 (+31.1% vs 6M25 R$2,399m). CapEx/investments: enter face. "
     "Nested vs aegea_societario_investimentos_2t26_1554m_brl / ecosystem "
     "Investimentos R$3,809m (not additive).",
     3145, "2026-06-30", "2026",
     "Investimentos Aegea Societário 1.554 1.335 16,4% 3.145 2.399 31,1%",
     "Aegea Societário Brazil water concessions (São Paulo HQ pin)."),
    ("aegea_outorgas_6m26_402m_brl", "water",
     "Aegea — Outorgas 6M26 R$402m",
     "Aegea 2T26/6M26 earnings release: narrative states R$402 million in outorga "
     "payments within R$3.8bn 6M26 ecosystem investments (alongside R$3.4bn Capex). "
     "CapEx/financing: enter R$402m 6M26 outorgas aggregate. Nested vs "
     "aegea_outorgas_2t26_73m_brl / Pará/Brusque/Piauí/Corsan/Demais outorga faces "
     "(not additive to Capex lines).",
     402, "2026-06-30", "2026",
     "R$ 402 milhões em pagamento de outorgas e R$ 3,4 bilhões em Capex",
     "Aegea Brazil water concession portfolio (São Paulo HQ pin)."),
]

for rid, sub, counterpart, asset, val_m, fx_date, year, quote, geo in AEGEA_FACES:
    brl, usd = brl_m(val_m)
    row_doc(
        rid, "resources", sub, "other", counterpart, "Brazil", asset,
        brl, fx_date, year, "-23.55", "-46.63", geo,
        AEGEA_SID, quote, AEGEA_URL,
        f"Actor: Aegea Saneamento — other. NEW {counterpart}. Shuffle water; "
        f"other equal-budget.",
        "hunt_cycle310", investment_type="corporate_capex", evidence="documented",
        currency="BRL", value_usd=usd, fx_usd=BRL_USD, bib_type="company",
        chicago=AEGEA_CHICAGO,
        annotation=f"Aegea face via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Aegea 2T26/6M26 release; confirmed {quote[:60]}.",
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
    print(f"cycle310 added {len(added)}: {added}")
    print(f"cycle310 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
