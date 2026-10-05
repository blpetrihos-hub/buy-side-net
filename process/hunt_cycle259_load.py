#!/usr/bin/env python3
"""Cycle 259 hunt: shuffle_seed=20261259; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261259).shuffle):
other_renewables, power_plants_grid, wind, water, copper, lithium, nickel,
building_materials, rail, balsa, bridges_roads, engineering_epc, port_ownership,
solar, fission_smr, port_cranes, graphite, niobium.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: spent residual (Scala BNDES C257; Equinix/Ascenty/AES Andes dense;
  Equinix SP USD109m / Progress Rail VLI R$430m without openable dual primary).
PRC equal-budget: honest residual (BYD BESS ≤R$500m without company CapEx primary).
Other: NEW AXIA 2Q26 CapEx R$3,117m; NEW AXIA 6M26 CapEx R$4,472m;
  NEW AXIA contracted TX CapEx ~R$15.54bn; NEW WEG Itajaí BESS factory CapEx R$330m;
  NEW WEG Mexico Atotonilco generators CapEx USD 24m.
Skipped: thin dry; holdovers unsigned; Alupar TECP/Lot 7 company PDF; Ultrapar fuel-scope;
  WEG Americas transformers R$2.1bn includes U.S. without separable LatAm-only primary.
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


# 1. power_plants_grid / other — NEW AXIA 2Q26 CapEx R$3,117m
row_doc(
    "axia_2q26_capex_3117m_brl",
    "energy", "power_plants_grid", "other",
    "AXIA Energia — 2Q26 CapEx R$3,117m",
    "Brazil",
    "6 Aug 2026 AXIA Energia SEC Form 6-K (2Q26 Earnings Presentation): Investments R$3,117 million in 2Q26 (+52.6% YoY); transmission expansion R$636m; reinforcements and improvements R$1,073m. CapEx: enter R$3,117m 2Q26 face. Nested vs 6M26 / TX contracted envelopes (not additive).",
    "3117000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "AXIA Energia Brazil generation/transmission footprint (Rio de Janeiro HQ pin).",
    "axia_2q26_6k_20260806",
    "Investments: R$ 3,117 million, up 52.6% YoY … Total investments reached R$ 3,117 million in 2Q26, up 52.6% year over year … Investments in transmission expansion increased significantly, reaching R$ 636 million this quarter … Investments in reinforcements and improvements totaled R$ 1,073 million in 2Q26.",
    "https://www.sec.gov/Archives/edgar/data/1439124/000129281426004105/axia20260806_6k2.htm",
    "Actor: AXIA Energia S.A. (ex-Eletrobras; Brazilian utility) — other. NEW nested 2Q26 CapEx R$3,117m. Shuffle power_plants_grid.",
    "hunt_cycle259", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(3117000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AXIA Energia S.A. “Form 6-K — 2Q26 Earnings Presentation.” August 6, 2026. https://www.sec.gov/Archives/edgar/data/1439124/000129281426004105/axia20260806_6k2.htm.',
    annotation="AXIA 2Q26/6M26 CapEx and TX contracted ~R$15.54bn via Fed H.10. Supports axia_2q26_capex_3117m_brl; axia_6m26_capex_4472m_brl; axia_tx_contracted_15p54bn_brl_2026.",
    evid_note="Opened AXIA SEC 6-K 2Q26 presentation; CapEx R$3,117m (+52.6%) / TX expansion R$636m / R&I R$1,073m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. power_plants_grid / other — NEW AXIA 6M26 CapEx R$4,472m
row_doc(
    "axia_6m26_capex_4472m_brl",
    "energy", "power_plants_grid", "other",
    "AXIA Energia — 6M26 CapEx R$4,472m",
    "Brazil",
    "6 Aug 2026 AXIA Energia SEC Form 6-K (2Q26 Earnings Presentation): Total investments R$4,472 million in 6M26 (+47.2% vs 6M25). CapEx: enter R$4,472m 6M26 face. Nested vs axia_2q26_capex_3117m_brl (not additive).",
    "4472000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "AXIA Energia Brazil generation/transmission footprint (Rio de Janeiro HQ pin).",
    "axia_2q26_6k_20260806",
    "Total investments reached R$ 3,117 million in 2Q26, up 52.6% year over year, and R$ 4,472 million in 6M26 … Investments totaled R$ 3,117 million in 2Q26 and R$ 4,472 million in 6M26, representing increases of 52.6% and 47.2% compared to 2Q25 and 6M25, respectively.",
    "https://www.sec.gov/Archives/edgar/data/1439124/000129281426004105/axia20260806_6k2.htm",
    "Actor: AXIA Energia S.A. (ex-Eletrobras) — other. NEW nested 6M26 CapEx R$4,472m. Shuffle power_plants_grid.",
    "hunt_cycle259", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(4472000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AXIA Energia S.A. “Form 6-K — 2Q26 Earnings Presentation.” August 6, 2026. https://www.sec.gov/Archives/edgar/data/1439124/000129281426004105/axia20260806_6k2.htm.',
    annotation="AXIA 2Q26/6M26 CapEx and TX contracted ~R$15.54bn via Fed H.10. Supports axia_2q26_capex_3117m_brl; axia_6m26_capex_4472m_brl; axia_tx_contracted_15p54bn_brl_2026.",
    evid_note="Opened AXIA SEC 6-K 2Q26 presentation; CapEx 6M26 R$4,472m (+47.2%) confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / other — NEW AXIA contracted TX CapEx ~R$15.54bn
row_doc(
    "axia_tx_contracted_15p54bn_brl_2026",
    "energy", "power_plants_grid", "other",
    "AXIA Energia — contracted transmission CapEx ~R$15.54bn",
    "Brazil",
    "6 Aug 2026 AXIA Energia SEC Form 6-K (2Q26 Earnings Presentation): Contracted Transmission Investments table totals ANEEL CapEx R$15,540 million / RAP R$2,000 million (auctions 01/2023–01/2026 + large-scale reinforcements + small-scale improvements); slide also states transmission investments already contracted totaling >R$15 billion / 288 large-scale projects RAP +R$2.0bn through 2030 with estimated CapEx R$15.5bn. CapEx: enter R$15.54bn table total. Distinct from quarterly executed CapEx rows.",
    "15540000000", "2026-08-06", "2026", "-22.91", "-43.17",
    "AXIA Energia Brazil transmission portfolio (national; Rio de Janeiro HQ pin).",
    "axia_2q26_6k_20260806",
    "Contracted Transmission Investments … Total 15,540 2,000 … Transmission investments already contracted totaling > R$ 15 billion … 288 large-scale projects are under implementation, representing an additional RAP of R$ 2.0 billion between 2026 and 2030 with a total estimated CAPEX of R$ 15.5 billion.",
    "https://www.sec.gov/Archives/edgar/data/1439124/000129281426004105/axia20260806_6k2.htm",
    "Actor: AXIA Energia S.A. (ex-Eletrobras) — other. NEW contracted TX CapEx envelope R$15.54bn. Shuffle power_plants_grid.",
    "hunt_cycle259", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(15540000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AXIA Energia S.A. “Form 6-K — 2Q26 Earnings Presentation.” August 6, 2026. https://www.sec.gov/Archives/edgar/data/1439124/000129281426004105/axia20260806_6k2.htm.',
    annotation="AXIA 2Q26/6M26 CapEx and TX contracted ~R$15.54bn via Fed H.10. Supports axia_2q26_capex_3117m_brl; axia_6m26_capex_4472m_brl; axia_tx_contracted_15p54bn_brl_2026.",
    evid_note="Opened AXIA SEC 6-K 2Q26 presentation; contracted TX CapEx table Total R$15,540m / RAP R$2,000m / >R$15bn narrative confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. other_renewables / other — NEW WEG Itajaí BESS factory CapEx R$330m
row_doc(
    "weg_itajai_bess_330m_brl_2026",
    "energy", "other_renewables", "other",
    "WEG — Itajaí BESS factory CapEx R$330m (updated)",
    "Brazil",
    "25 Sep 2026 WEG company news: amplifies Itajaí/SC BESS factory project to total estimated investment R$330 million and annual capacity 4 GWh; operations expected 2H2027. CapEx: enter R$330m total face. Distinct from weg_itajai_bess_280m_brl_2026 (BNDES Mais Inovação financing R$280m for earlier plant announcement).",
    "330000000", "2026-09-25", "2026", "-26.91", "-48.67",
    "WEG BESS factory Itajaí, Santa Catarina (Itajaí pin).",
    "weg_itajai_bess_330m_20260925",
    "A WEG anuncia a ampliação do projeto de sua nova fábrica de sistemas de armazenamento de energia em baterias (BESS), em construção em Itajaí / SC. Anunciada em fevereiro deste ano, a nova fábrica terá um investimento total estimado de R$ 330 milhões e capacidade anual de 4 GWh … com início das operações previsto para o segundo semestre de 2027.",
    "https://developers.weg.net/institutional/BR/pt/news/geral/weg-amplia-projeto-da-fabrica-de-sistemas-de-armazenamento-de-energia-em-baterias-bess-em-itajai-sc",
    "Actor: WEG S.A. (Brazilian electro-equipment) — other. NEW CapEx total R$330m for Itajaí BESS factory (updated vs R$280m financing row). Shuffle other_renewables.",
    "hunt_cycle259", investment_type="greenfield_capex", evidence="documented", currency="BRL",
    value_usd=str(round(330000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='WEG S.A. “WEG amplia projeto da fábrica de sistemas de armazenamento de energia em baterias (BESS) em Itajaí / SC.” September 25, 2026. https://developers.weg.net/institutional/BR/pt/news/geral/weg-amplia-projeto-da-fabrica-de-sistemas-de-armazenamento-de-energia-em-baterias-bess-em-itajai-sc.',
    annotation="WEG Itajaí BESS NEW R$330m ~USD 63.56m via Fed H.10. Supports weg_itajai_bess_330m_brl_2026.",
    evid_note="Opened WEG company Portuguese news; CapEx total R$330m / 4 GWh / COD 2H2027 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. engineering_epc / other — NEW WEG Mexico Atotonilco generators CapEx USD 24m
row_doc(
    "weg_mexico_atotonilco_generators_24m_2026",
    "infrastructure", "engineering_epc", "other",
    "WEG — Atotonilco de Tula (Mexico) generator assembly CapEx USD 24m",
    "Mexico",
    "28 Sep 2026 WEG company news: Phase 1 of North America generator expansion invests USD 24 million to acquire/adapt industrial building next to Parque Industrial de Quma I in Atotonilco de Tula, Mexico, for generator assembly; operations targeted 2Q2027. (Phase 2 USD 141m location TBD in North America — not entered; may include U.S.) CapEx: enter Mexico Phase 1 USD 24m only.",
    "24000000", "2026-09-28", "2026", "20.00", "-99.22",
    "Atotonilco de Tula, Hidalgo, Mexico (Quma I industrial park pin).",
    "weg_na_generators_165m_20260928",
    "A primeira fase do projeto contempla investimentos de US$ 24 milhões para aquisição e adequação de um prédio industrial localizado ao lado do atual Parque Industrial de Quma I, em Atotonilco de Tula, no México. A unidade será destinada à montagem de geradores … com início das operações previsto para o segundo trimestre de 2027.",
    "https://developers.weg.net/institutional/BR/pt/news/geral/weg-anuncia-investimento-de-us-165-milhoes-para-ampliar-producao-de-geradores-na-america-do-norte",
    "Actor: WEG S.A. (Brazilian) — other. NEW Mexico Phase 1 CapEx USD 24m only (Phase 2 TBD North America excluded). Shuffle engineering_epc.",
    "hunt_cycle259", investment_type="greenfield_capex", evidence="documented", currency="USD",
    value_usd="24000000", fx_usd="1", bib_type="company",
    chicago='WEG S.A. “WEG anuncia investimento de US$ 165 milhões para ampliar produção de geradores na América do Norte.” September 28, 2026. https://developers.weg.net/institutional/BR/pt/news/geral/weg-anuncia-investimento-de-us-165-milhoes-para-ampliar-producao-de-geradores-na-america-do-norte.',
    annotation="WEG Mexico Atotonilco NEW USD 24m Phase 1. Supports weg_mexico_atotonilco_generators_24m_2026.",
    evid_note="Opened WEG company Portuguese news; Mexico Phase 1 USD 24m Atotonilco / COD 2Q2027 confirmed; Phase 2 USD 141m TBD excluded.",
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
    print(f"cycle259 added {len(added)}: {added}")
    print(f"cycle259 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
