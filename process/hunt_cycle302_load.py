#!/usr/bin/env python3
"""Cycle 302 hunt: shuffle_seed=20261302; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261302).shuffle):
lithium, building_materials, balsa, power_plants_grid, copper, rail, solar, water,
port_ownership, other_renewables, niobium, fission_smr, graphite, engineering_epc,
port_cranes, nickel, wind, bridges_roads.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (balsa third / fission_smr twelfth / nickel sixteenth in shuffle).
≥1/3 U.S. hunt budget: CapEx-FILL aes_atacama_solar_acquisition_2025 USD105m from
  AES Corp 2025 Annual Report (10-K investing discussion); Arenales still CapEx-
  blank in AR construction table; Wabtec Vale / Progress Rail R$430m / Caterpillar
  CapEx-fill blanks; Bechtel 403.
PRC equal-budget: Goldwind/Sungrow/BYD CapEx-blank COD faces.
ALLIED: NEW Neoenergia Dist CapEx Melhoria da Rede / Perdas e Inadimplência /
  Outros × Coelba/PE/Cosern/Elektro/Brasília 6M26 (15 faces) — completes deferred
  category×distributor nested after cycle 301 Expansão/Novas Ligações/Novas SEs/
  Renovação.
Skipped: thin dry; Equatorial Dist nested already mined; Neoenergia Material/
  Investimento Bruto/Líquido×distributor deferred; holdovers unsigned.
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

AES_AR_URL = (
    "https://www.aes.com/sites/vault/files/2026-03/AES-Corp-2025-Annual-Report-03-20-2026.pdf"
)
AES_AR_CHICAGO = (
    'The AES Corporation. “2025 Annual Report / Form 10-K.” March 20, 2026. '
    + AES_AR_URL + "."
)
AES_AR_SID = "aes_corp_2025_annual_report_20260320"

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


# CapEx-FILL: AES Atacama Solar acquisition USD105m (US solar)
row_doc(
    "aes_atacama_solar_acquisition_2025", "energy", "solar", "us",
    "AES Pacífico Chile / AES Corporation — Atacama Solar PV acquisition (Tarapacá)",
    "Chile",
    "9 Jan 2025 AES Andes: AES Pacífico Chile SpA acquires Atacama Solar 171 MWp PV (Pica/Pozo Almonte, Tarapacá) from Sonnedix — operational since Apr 2021; 494,640 panels; connected via 46 km line to 220 kV. CapEx-FILL: AES Corp 2025 Annual Report (Form 10-K) investing discussion states prior-year acquisition of Atacama Solar in Chile for $105 million. CapEx: enter acquisition cash consideration. Distinct from aes_atacama_bess_250mw_chile_2026 storage add-on (CapEx still blank).",
    "105000000", "2025-12-31", "2025", "-20.49", "-69.57",
    "Pica / Pozo Almonte, Tarapacá Region (company geography; approximate municipal pin).",
    AES_AR_SID,
    "Cash paid for acquisitions of business interests decreased $138 million, primarily due to the prior year acquisition of Atacama Solar in Chile for $105 million",
    AES_AR_URL,
    "Actor: AES Pacífico Chile / AES Corporation (U.S.) — us. CapEx-FILL USD105m from AES Corp 2025 AR. Shuffle solar; ≥1/3 US hunt budget.",
    "hunt_cycle302", investment_type="acquisition", evidence="documented", currency="USD",
    value_usd="105000000", fx_usd="1", bib_type="company",
    chicago=AES_AR_CHICAGO,
    annotation="AES Atacama Solar acquisition CapEx USD105m from AES Corp 2025 AR. Supports aes_atacama_solar_acquisition_2025.",
    evid_note="Opened AES Corp 2025 Annual Report PDF; Atacama Solar Chile acquisition $105 million confirmed in investing cash-flow discussion.",
)

# Neoenergia Dist Melhoria / Perdas / Outros × distributor 6M26
CATEGORIES = [
    (
        "melhoria_rede",
        "Melhoria da Rede",
        [96, 47, 43, 48, 42],
        "Melhoria da Rede 96 … 47 … 43 … 48 … 42 … 276",
        "neoenergia_melhoria_rede_6m26_276m_brl",
    ),
    (
        "perdas_inadimplencia",
        "Perdas e Inadimplência",
        [49, 52, 6, 5, 24],
        "Perdas e Inadimplência 49 … 52 … 6 … 5 … 24 … 137",
        "neoenergia_perdas_6m26_137m_brl",
    ),
    (
        "outros_dist",
        "Outros (Dist)",
        [134, 120, 22, 87, 43],
        "Outros 134 … 120 … 22 … 87 … 43 … 405",
        "neoenergia_outros_dist_6m26_405m_brl",
    ),
]

for slug, label, vals, quote, parent in CATEGORIES:
    for (dslug, dname, state, lat, lon, geo), val_m in zip(DISTS, vals):
        val = int(val_m * 1_000_000)
        rid = f"neoenergia_{dslug}_{slug}_6m26_{val_m}m_brl"
        row_doc(
            rid, "energy", "power_plants_grid", "allied",
            f"Neoenergia {dname} — {label} CapEx 6M26 R${val_m}m",
            "Brazil",
            f"21 Jul 2026 Neoenergia S.A. Earnings Release 2Q26/6M26: Dist CapEx abertura por distribuidora — {dname} ({state}) {label} 6M26 R${val_m} million. CapEx: enter category×distributor nested face. Nested under {parent} aggregate and under {dname} Dist CapEx total already logged.",
            str(val), "2026-07-21", "2026", lat, lon, geo,
            NEO_SID, quote, NEO_URL,
            f"Actor: Neoenergia (Iberdrola) — allied. NEW {dname} {label} 6M26. Shuffle power_plants_grid; allied equal-budget.",
            "hunt_cycle302", investment_type="corporate_capex", evidence="documented", currency="BRL",
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
    print(f"cycle302 added {len(added)}: {added}")
    print(f"cycle302 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
