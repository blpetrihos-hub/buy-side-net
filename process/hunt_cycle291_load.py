#!/usr/bin/env python3
"""Cycle 291 hunt: shuffle_seed=20261291; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261291).shuffle):
water, balsa, port_cranes, bridges_roads, wind, port_ownership, nickel, rail,
copper, lithium, niobium, solar, other_renewables, engineering_epc, graphite,
building_materials, power_plants_grid, fission_smr.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (balsa second in shuffle — dry).
≥1/3 U.S. hunt budget: Bechtel QB2 desal CapEx-fill blank; AES Andes Green Impact
  Report Jun 2026 fully mined (no new allocation faces); SSA Guaymas STS CapEx
  blank; Progress Rail VLI R$430m still unsigned; Arenales project CapEx blank.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
OTHER: NEW Aegea Ecossistema Investimentos Proforma 2T26 R$1.901bn / 6M26
  R$3.809bn (Capex+outorgas totals).
ALLIED: NEW Neoenergia Dist Investimento Bruto/Líquido / Perdas e Inadimplência /
  Outros / Movimentação Material 6M26 nested; NEW ISA Energia 1S26 R&M energized
  ~R$475m (company “cerca de”).
Skipped: thin dry; port_cranes/bridges_roads/wind/port_ownership/nickel/rail/
  copper/lithium/niobium/solar/other_renewables/engineering_epc/graphite/
  building_materials/power_plants_grid/fission_smr dense or CapEx-blank;
  holdovers unsigned.
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
AEGEA_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/"
    "059c8a63-d6dc-b073-bb33-76e316044799?origin=2"
)
NEO_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/"
    "145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2"
)
ISA_URL = (
    "https://ri.isaenergiabrasil.com.br/pt/documentos/"
    "6758-Earnings-Release-2T26-vfinal.pdf"
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


# water / other — Aegea Investimentos totals (Capex + outorgas)
row_doc(
    "aegea_2t26_investimentos_1901m_brl",
    "resources", "water", "other",
    "Aegea Ecossistema — Investimentos Proforma 2T26 R$1.901bn",
    "Brazil",
    "Aegea 2T26/6M26 release: Investimentos Proforma Ecossistema Aegea 2T26 R$1,901 million (Capex R$1,828m + Outorgas R$73m). CapEx envelope: enter R$1.901bn face. Distinct from Capex-only R$1.828bn nested (not additive).",
    "1901000000", "2026-08-12", "2026", "-23.55", "-46.63",
    "Aegea sanitation ecosystem (São Paulo HQ pin).",
    "aegea_2t26_6m26_release_mziq",
    "Investimentos Proforma Ecossistema Aegea 1.901",
    AEGEA_URL,
    "Actor: Aegea — other. NEW 2T26 Investimentos Proforma R$1.901bn. Shuffle water; other equal-budget.",
    "hunt_cycle291", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1901000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento e Participações S.A. “Release de Resultados 2T26 / 6M26.” ' + AEGEA_URL + ".",
    annotation="Aegea 2T26 Investimentos Proforma R$1.901bn via Fed H.10. Supports aegea_2t26_investimentos_1901m_brl.",
    evid_note="Opened Aegea 2T26/6M26 PDF; Investimentos Proforma Ecossistema 2T26 R$1,901m confirmed.",
)

row_doc(
    "aegea_6m26_investimentos_3809m_brl",
    "resources", "water", "other",
    "Aegea Ecossistema — Investimentos Proforma 6M26 R$3.809bn",
    "Brazil",
    "Aegea 2T26/6M26 release: Investimentos Proforma Ecossistema Aegea 6M26 R$3,809 million (Capex R$3,407m + Outorgas R$402m). CapEx envelope: enter R$3.809bn face. Distinct from Capex-only / outorga nested faces (not additive).",
    "3809000000", "2026-08-12", "2026", "-23.55", "-46.63",
    "Aegea sanitation ecosystem (São Paulo HQ pin).",
    "aegea_2t26_6m26_release_mziq",
    "Investimentos Proforma Ecossistema Aegea … 3.809",
    AEGEA_URL,
    "Actor: Aegea — other. NEW 6M26 Investimentos Proforma R$3.809bn. Shuffle water; other equal-budget.",
    "hunt_cycle291", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(3809000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento e Participações S.A. “Release de Resultados 2T26 / 6M26.” ' + AEGEA_URL + ".",
    annotation="Aegea 6M26 Investimentos Proforma R$3.809bn via Fed H.10. Supports aegea_6m26_investimentos_3809m_brl.",
    evid_note="Opened Aegea 2T26/6M26 PDF; Investimentos Proforma Ecossistema 6M26 R$3,809m confirmed.",
)

# Neoenergia Dist nested residual (allied)
for rid, label, val, quote in [
    ("neoenergia_investimento_bruto_6m26_4066m_brl", "Investimento Bruto", 4066000000, "Investimento Bruto … 4.066"),
    ("neoenergia_investimento_liquido_6m26_4005m_brl", "Investimento Líquido", 4005000000, "Investimento Líquido … 4.005"),
    ("neoenergia_perdas_6m26_137m_brl", "Perdas e Inadimplência", 137000000, "Perdas e Inadimplência … 137"),
    ("neoenergia_outros_dist_6m26_405m_brl", "Outros (Dist CapEx)", 405000000, "Outros … 405"),
    ("neoenergia_material_6m26_310m_brl", "Movimentação Material (Estoque x Obra)", 310000000, "Movimentação Material (Estoque x Obra) … 310"),
]:
    row_doc(
        rid, "energy", "power_plants_grid", "allied",
        f"Neoenergia — Distribuição {label} 6M26 R${val/1e6:.0f}m",
        "Brazil",
        f"21 Jul 2026 Neoenergia 2T26/6M26 release: Distribuição CapEx table consolidado — {label} 6M26 R${val/1e6:,.0f} million. CapEx: enter face. Nested under Dist CapEx R$3.696bn / Investimento Bruto R$4.066bn family (not additive).",
        str(val), "2026-07-21", "2026", "-22.91", "-43.17",
        "Neoenergia distribution companies (Rio de Janeiro HQ pin).",
        "neoenergia_2q26_release_mziq", quote, NEO_URL,
        f"Actor: Neoenergia (Iberdrola) — allied. NEW 6M26 {label}. Shuffle power_plants_grid; allied equal-budget.",
        "hunt_cycle291", investment_type="corporate_capex", evidence="documented", currency="BRL",
        value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
        chicago='Neoenergia S.A. “Earnings Release 2Q26 / 6M26” (company MZ IQ PDF). ' + NEO_URL + ".",
        annotation=f"Neoenergia 6M26 {label} via Fed H.10. Supports {rid}.",
        evid_note=f"Opened Neoenergia 2T26/6M26 PDF; {label} consolidado 6M26 R${val/1e6:,.0f}m confirmed.",
    )

# ISA 1S26 R&M energized ~R$475m (allied, company "cerca de")
row_doc(
    "isa_energia_1s26_rm_energized_475m_brl",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — R&M energized 1S26 ~R$475m",
    "Brazil",
    "ISA Energia Brasil Earnings Release 2T26: no semestre, os investimentos energizados totalizaram cerca de R$475 million (72% small / 28% large R&M projects). CapEx: enter ~R$475m face (company approximate). Nested under 1S26 R&M R$815.4m / 2T26 energized R$290.8m (not additive).",
    "475000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "ISA Energia Brasil R&M energized projects 1S26 (São Paulo HQ pin).",
    "isa_energia_2t26_earnings_release",
    "No semestre, os investimentos energizados totalizaram cerca de R$ 475 milhões",
    ISA_URL,
    "Actor: ISA Energia Brasil — allied. NEW 1S26 R&M energized ~R$475m. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle291", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(475000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “Earnings Release 2T26.” 2026. ' + ISA_URL + ".",
    annotation="ISA 1S26 R&M energized ~R$475m via Fed H.10. Supports isa_energia_1s26_rm_energized_475m_brl.",
    evid_note="Opened ISA Energia Brasil 2T26 Earnings Release PDF; 1S26 R&M energized cerca de R$475m confirmed.",
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
    print(f"cycle291 added {len(added)}: {added}")
    print(f"cycle291 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
