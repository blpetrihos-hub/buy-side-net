#!/usr/bin/env python3
"""Cycle 301 hunt: shuffle_seed=20261301; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261301).shuffle):
balsa, copper, lithium, wind, fission_smr, water, engineering_epc,
other_renewables, port_cranes, graphite, power_plants_grid, rail, nickel,
niobium, bridges_roads, solar, port_ownership, building_materials.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (balsa first / fission_smr fifth / nickel thirteenth in shuffle).
≥1/3 U.S. hunt budget: AES Brasil MF largely mined; Arenales CapEx blank;
  Wabtec Vale CapEx blank; Progress Rail R$430m absent; Balsasud/CoreLite CapEx
  blank; Brazilian Nickel news 404; Bechtel/FCX CapEx-fill blanks.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
ALLIED: NEW Neoenergia Dist CapEx nested category×distributor 6M26 (Expansão de
  Rede / Novas Ligações / Novas SE's e RD's / Renovação de Ativos × Coelba/PE/
  Cosern/Elektro/Brasília) + NEW Neoenergia TOTAL CapEx 2T26 R$2.095bn.
Skipped: thin dry; Neoenergia Melhoria/Perdas/Outros×distributor deferred;
  Motiva/Alupar/Energisa/Aegea/ISA largely mined; holdovers unsigned.
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
NEO_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/"
    "145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2"
)
NEO_CHICAGO = (
    'Neoenergia S.A. “Earnings Release 2Q26 / 6M26” (company MZ IQ PDF). ' + NEO_URL + "."
)
NEO_SID = "neoenergia_2q26_release_mziq"

DISTS = [
    ("coelba", "Coelba", "Bahia", "-12.97", "-38.51", "Neoenergia Coelba (Salvador pin)."),
    ("pe", "Pernambuco", "Pernambuco", "-8.05", "-34.88", "Neoenergia Pernambuco (Recife pin)."),
    ("cosern", "Cosern", "Rio Grande do Norte", "-5.79", "-35.21", "Neoenergia Cosern (Natal pin)."),
    ("elektro", "Elektro", "São Paulo", "-23.55", "-46.63", "Neoenergia Elektro (São Paulo pin)."),
    ("brasilia", "Brasília", "Distrito Federal", "-15.78", "-47.93", "Neoenergia Brasília (Brasília pin)."),
]


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


# TOTAL CapEx 2T26 R$2.095bn (labeled face; distinct from 1T26 R$1.8bn and 6M26 R$4.0bn)
row_doc(
    "neoenergia_2t26_capex_2095m_brl", "energy", "power_plants_grid", "allied",
    "Neoenergia — TOTAL CapEx 2T26 R$2.095bn",
    "Brazil",
    "21 Jul 2026 Neoenergia S.A. Earnings Release 2Q26/6M26: CAPEX Neoenergia TOTAL 2T26 R$2.095 billion (Redes R$2.063bn + Geração e Clientes R$29m + Outros R$3m). CapEx: enter period TOTAL face. Distinct from 6M26 R$3.979bn TOTAL and from Dist/TX nested faces.",
    "2095000000", "2026-07-21", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil footprint (Rio de Janeiro HQ pin).",
    NEO_SID, "TOTAL 2.095 2.792 (25%) 3.979 5.032 (21%)", NEO_URL,
    "Actor: Neoenergia (Iberdrola) — allied. NEW TOTAL CapEx 2T26. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle301", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2095000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago=NEO_CHICAGO,
    annotation="Neoenergia TOTAL CapEx 2T26 via Fed H.10. Supports neoenergia_2t26_capex_2095m_brl.",
    evid_note="Opened Neoenergia 2Q26 MZ IQ PDF; TOTAL CapEx 2T26 R$2.095bn confirmed.",
)

# Dist CapEx category × distributor 6M26 (nested under Dist aggregate + company totals)
# Table columns: Coelba, PE, Cosern, Elektro, Brasília (6M26 faces)
CATEGORIES = [
    (
        "expansao_rede",
        "Expansão de Rede",
        [1415, 299, 137, 349, 65],
        "Expansão de Rede 1.415 … 299 … 137 … 349 … 65 … 2.265",
        "neoenergia_network_expansion_6m26_2265m_brl",
    ),
    (
        "novas_ligacoes",
        "Novas Ligações",
        [707, 219, 101, 219, 32],
        "Novas Ligações 707 … 219 … 101 … 219 … 32 … 1.278",
        "neoenergia_novas_ligacoes_6m26_1278m_brl",
    ),
    (
        "novas_ses_rds",
        "Novas SE's e RD's",
        [552, 79, 37, 130, 33],
        "Novas SE's e RD's 552 … 79 … 37 … 130 … 33 … 831",
        "neoenergia_novas_ses_rds_6m26_831m_brl",
    ),
    (
        "renovacao_ativos",
        "Renovação de Ativos",
        [223, 232, 37, 115, 67],
        "Renovação de Ativos 223 … 232 … 37 … 115 … 67 … 674",
        "neoenergia_renovacao_ativos_6m26_674m_brl",
    ),
]

for slug, label, vals, quote, parent in CATEGORIES:
    for (dslug, dname, state, lat, lon, geo), val_m in zip(DISTS, vals):
        val = int(val_m * 1_000_000)
        rid = f"neoenergia_{dslug}_{slug}_6m26_{val_m}m_brl".replace(".", "p")
        # tidy ids without decimal: all ints here
        rid = f"neoenergia_{dslug}_{slug}_6m26_{val_m}m_brl"
        row_doc(
            rid, "energy", "power_plants_grid", "allied",
            f"Neoenergia {dname} — {label} CapEx 6M26 R${val_m}m",
            "Brazil",
            f"21 Jul 2026 Neoenergia S.A. Earnings Release 2Q26/6M26: Dist CapEx abertura por distribuidora — {dname} ({state}) {label} 6M26 R${val_m} million. CapEx: enter category×distributor nested face. Nested under {parent} aggregate and under {dname} Dist CapEx total already logged.",
            str(val), "2026-07-21", "2026", lat, lon, geo,
            NEO_SID, quote, NEO_URL,
            f"Actor: Neoenergia (Iberdrola) — allied. NEW {dname} {label} 6M26. Shuffle power_plants_grid; allied equal-budget.",
            "hunt_cycle301", investment_type="corporate_capex", evidence="documented", currency="BRL",
            value_usd=str(round(val / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
            chicago=NEO_CHICAGO,
            annotation=f"Neoenergia {dname} {label} 6M26 via Fed H.10. Supports {rid}.",
            evid_note=f"Opened Neoenergia 2Q26 MZ IQ PDF; {dname} {label} 6M26 R${val_m}m confirmed.",
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
    print(f"cycle301 added {len(added)}: {added}")
    print(f"cycle301 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
