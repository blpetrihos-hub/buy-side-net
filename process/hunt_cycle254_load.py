#!/usr/bin/env python3
"""Cycle 254 hunt: shuffle_seed=20261254; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261254).shuffle):
fission_smr, engineering_epc, water, balsa, lithium, nickel, rail, power_plants_grid,
wind, bridges_roads, niobium, building_materials, other_renewables, copper, port_cranes,
port_ownership, solar, graphite.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Brasil 2024–2028 CapEx plan R$1,348.4m (AES Corp).
PRC equal-budget: NEW CPFL Energia 2T26 CapEx R$1.5bn (State Grid; nested vs 1H26 R$2.8bn).
Other: NEW Sabesp 1H26 CapEx R$7,458m + FY2026 plan ~R$20bn; NEW Equatorial 2T26 CapEx R$2.6bn.
Skipped: thin balsa/nickel/fission dry; DFC V.tal already archived cycle-86 telecom scope;
  Ascenty/Microsoft/El Abra CapEx already logged; holdovers unsigned.
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


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def row_doc(
    rid, layer, subcategory, side, counterpart, country, asset, value, fx_date, year,
    lat, lon, geo, source_id, quote, url, note, hunt_support,
    investment_type="epc", evidence="documented", currency="USD", value_usd=None,
    fx_usd=None, chicago=None, bib_type="company", annotation=None, evid_note=None,
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
            "fx_date": fx_date if value_usd else "", "year": year, "status": "active",
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


# 1. power_plants_grid / us — NEW AES Brasil 2024–2028 CapEx plan R$1,348.4m
row_doc(
    "aes_brasil_capex_plan_1348m_brl_2024_2028",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2024–2028 CapEx plan (~R$1.348bn)",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact (English): updated investment projections 2024–2028 totaling R$1,348.4 million — modernization/maintenance R$829.4m; Cajuína pipeline + AGV VII solar R$130.8m; expansion R$388.2m (Tucano R$14.4m + Cajuína R$373.8m). CapEx: enter R$1,348.4m plan face. Distinct from AES Andes Chile CapEx envelopes.",
    "1348400000", "2024-02-26", "2024", "-23.55", "-46.63",
    "AES Brasil multi-asset footprint (São Paulo HQ pin; Cajuína/Tucano/AGV sites multi).",
    "aes_brasil_mf_capex_20240226",
    "Between 2024 and 2028, AES Brasil plans to invest approximately BRL 1.3 billion, earmarked for: (i) the modernization and maintenance of operational assets, including the turnaround of wind assets acquired through M&A; (ii) the completion of the construction works of already contracted projects; and (iii) the development of the Cajuína pipeline and construction of the AGV VII solar park",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil Energia (AES Corporation U.S.) — us. NEW row: company English Material Fact R$1,348.4m 2024–2028 CapEx plan. Shuffle power_plants_grid / U.S. ≥1/3 budget.",
    "hunt_cycle254", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(1348400000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil NEW R$1,348.4m CapEx plan ~USD 259.70m via Fed H.10. Supports aes_brasil_capex_plan_1348m_brl_2024_2028.",
    evid_note="Opened AES Brasil English Material Fact PDF; Total Investments 1,348.4 (R$ million) 2024–2028 table confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. water / other — NEW Sabesp 1H26 CapEx R$7,458m
row_doc(
    "sabesp_1h26_capex_7458m_brl",
    "resources", "water", "other",
    "Sabesp — 1H26 CapEx R$7,458m",
    "Brazil",
    "Sabesp 2Q26 Earnings Release (SEC Form 6-K): Capex in 2Q26 totaled R$3,731 mn (+3.6% y/y); investments in 1H26 reached R$7,458 mn (+15.6% y/y); water R$2,293m / sewage R$5,165m in 1H26. CapEx: enter R$7,458m 1H26 face. Nested vs ~R$20bn FY2026 CapEx guidance row (not additive).",
    "7458000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Sabesp São Paulo state water/sewage concession (São Paulo pin).",
    "sabesp_2q26_sec_6k_2026",
    "In 2Q26, Capex totaled R$ 3,731 mn, an increase of 3.6% compared to the same period of the previous year. Investments in 1H26 reached R$ 7,458 mn, a 15.6% increase y/y.",
    "https://www.sec.gov/Archives/edgar/data/1170858/000129281426004252/sbsitr2q26_6k.htm",
    "Actor: Sabesp (Companhia de Saneamento Básico do Estado de São Paulo) — other. NEW row: company SEC 6-K 1H26 CapEx R$7,458m. Shuffle water.",
    "hunt_cycle254", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(7458000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia de Saneamento Básico do Estado de São Paulo — SABESP. “Earnings Release 2Q26” (Form 6-K). 2026. https://www.sec.gov/Archives/edgar/data/1170858/000129281426004252/sbsitr2q26_6k.htm.',
    annotation="Sabesp 1H26 NEW R$7,458m ~USD 1436.41m via Fed H.10. Supports sabesp_1h26_capex_7458m_brl.",
    evid_note="Opened Sabesp SEC 6-K 2Q26 earnings release HTML; Capex 1H26 R$7,458m / 2Q26 R$3,731m / water-sewage split confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. water / other — NEW Sabesp FY2026 CapEx guidance ~R$20bn
row_doc(
    "sabesp_2026_capex_plan_20bn_brl",
    "resources", "water", "other",
    "Sabesp — FY2026 CapEx guidance ~R$20bn",
    "Brazil",
    "Sabesp 2Q26 Earnings Release (SEC Form 6-K) CEO message: Company remains focused on investing close to R$20 billion in CapEx in the year, supporting acceleration of universalization, quality of service and greater operational resilience. CapEx: enter R$20bn soft floor FY2026 plan. Envelope vs 1H26 R$7,458m realized (not additive).",
    "20000000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Sabesp São Paulo state water/sewage concession (São Paulo pin).",
    "sabesp_2q26_sec_6k_2026",
    "to be on investing close to R$20 billion in CapEx in the year, supporting the acceleration of universalization, quality of service and greater operational",
    "https://www.sec.gov/Archives/edgar/data/1170858/000129281426004252/sbsitr2q26_6k.htm",
    "Actor: Sabesp — other. NEW nested FY2026 CapEx guidance ~R$20bn soft floor. Shuffle water.",
    "hunt_cycle254", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(20000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia de Saneamento Básico do Estado de São Paulo — SABESP. “Earnings Release 2Q26” (Form 6-K). 2026. https://www.sec.gov/Archives/edgar/data/1170858/000129281426004252/sbsitr2q26_6k.htm.',
    annotation="Sabesp FY2026 plan NEW ~R$20bn ~USD 3852.01m via Fed H.10. Supports sabesp_2026_capex_plan_20bn_brl.",
    evid_note="Opened Sabesp SEC 6-K 2Q26; ~R$20bn CapEx year guidance in CEO message confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / other — NEW Equatorial 2T26 CapEx R$2.6bn
row_doc(
    "equatorial_2t26_capex_2p6bn_brl",
    "energy", "power_plants_grid", "other",
    "Equatorial — 2T26 consolidated CapEx ~R$2.6bn",
    "Brazil",
    "12 Aug 2026 Equatorial S.A. 2T26 earnings release (company RI PDF): consolidated investments totaled about R$ 2.6 billion in 2T26 (−3.8% vs 2T25; table shows Investimentos 2.600 vs 2.704 R$ million). CapEx: enter R$2.6bn soft face. Distinct from equatorial_quantum_170m_brl_2026 project row; multi-utility distribution/sanitation/telecom envelope.",
    "2600000000", "2026-06-30", "2026", "-15.78", "-47.93",
    "Equatorial multi-state Brazil footprint (Brasília release pin).",
    "equatorial_2t26_release_20260812",
    "No 2T26 os investimentos consolidados somaram cerca de R$ 2,6 bilhões, volume 3,8% inferior ao registrado no 2T25.",
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2",
    "Actor: Equatorial S.A. (Brazilian multi-utility) — other. NEW row: company Portuguese 2T26 CapEx ~R$2.6bn. Shuffle power_plants_grid.",
    "hunt_cycle254", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2600000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Resultados do segundo trimestre de 2026 (2T26).” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2.',
    annotation="Equatorial 2T26 NEW ~R$2.6bn ~USD 500.76m via Fed H.10. Supports equatorial_2t26_capex_2p6bn_brl.",
    evid_note="Opened Equatorial 2T26 RI PDF; investimentos consolidados ~R$2.6bn / table 2.600 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. power_plants_grid / prc — NEW CPFL 2T26 CapEx R$1.5bn
row_doc(
    "cpfl_2t26_capex_1p5bn_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia — 2T26 CapEx R$1.5bn",
    "Brazil",
    "CPFL Energia company Portuguese results note: investments (CAPEX) totaled R$ 1.5 billion in the quarter, totaling R$ 2.8 billion year-to-date; ~80% directed to distribution (expansion, modernization, customer service, network resilience). CapEx: enter R$1.5bn 2T26 face. Nested vs cpfl_1h26_capex_2p8bn_brl envelope and R$31.1bn 2026–2030 plan (not additive).",
    "1500000000", "2026-06-30", "2026", "-22.91", "-47.06",
    "CPFL Energia Brazil distribution/transmission footprint (Campinas / São Paulo pin).",
    "cpfl_2t26_results_20260813",
    "Os investimentos (CAPEX) somaram R$ 1,5 bilhão no trimestre, totalizando R$ 2,8 bilhões no acumulado do ano. Cerca de 80% dos recursos foram direcionados à distribuição, com foco na expansão, modernização, atendimento ao cliente e em melhoria e resiliência de rede.",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213",
    "Actor: CPFL Energia (State Grid Corporation of China–controlled) — prc. NEW nested 2T26 CapEx R$1.5bn. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle254", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia. “CPFL Energia registra lucro de R$ 1,4 bilhão no 2T26, alta de 21,3%.” August 2026. https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213.',
    annotation="CPFL 2T26 NEW R$1.5bn ~USD 288.90m via Fed H.10. Supports cpfl_2t26_capex_1p5bn_brl.",
    evid_note="Opened CPFL Portuguese company results page; CAPEX R$1.5bn quarter / R$2.8bn YTD / ~80% distribution confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    supports = entry.get("supports") or []
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        prev = existing.get("supports") or []
        for s in supports:
            if s not in prev:
                prev.append(s)
        existing.update(entry)
        existing["supports"] = prev
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if not isinstance(bib, list):
        bib = bib.get("sources") or bib.get("entries") or []
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
    print(f"cycle254 added {len(added)}: {added}")
    print(f"cycle254 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
