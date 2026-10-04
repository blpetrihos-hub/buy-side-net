#!/usr/bin/env python3
"""Cycle 220 hunt: shuffle_seed=20261220; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261220).shuffle):
solar, balsa, graphite, port_cranes, lithium, fission_smr, water, other_renewables,
port_ownership, engineering_epc, wind, power_plants_grid, building_materials, copper,
niobium, nickel, bridges_roads, rail.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    nickel CapEx-fill (Centaurus Jaguar BNDES company US$190m dual-quote);
    balsa/fission_smr dry.
≥1/3 U.S. hunt budget spent on Atlas Luiz Carlos Side B + Ascenty SPO06 CapEx-fills
+ Freeport/EnergyX/EXIM/Bechtel/Fluor/SSA/USTDA/Nextracker/Jervois/Wabtec sweeps
(2 US CapEx-fills; catalog dense otherwise).
PRC equal-budget: BYD Brazil BESS factory CapEx-fill; Sungrow/Goldwind/ZPMC/
PowerChina already logged; holdovers unsigned.
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
BRL_FX_DATE = "2026-09-25"


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
            "id": rid, "retrieved": "2026-10-04", "source_id": source_id, "url": url,
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


# 1. solar / us — CapEx-fill Atlas Luiz Carlos Side B R$895m
row_doc(
    "atlas_luiz_carlos_side_b_bot_2025",
    "energy", "solar", "us",
    "Atlas Renewable Energy (GIP) / ArcelorMittal — Luiz Carlos Solar Park Side B",
    "Brazil",
    "9 Dec 2025 Atlas: completes Side B of Luiz Carlos Solar Park in Paracatu, Minas Gerais — 315 MWp (ArcelorMittal’s first Brazil solar plant); company cites investments of R$895 million. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~172.38m for stored R$895m face. Distinct from atlas_luiz_carlos_fc_1p5bn_brazil_2024 financing row.",
    "895000000", BRL_FX_DATE, "2025", "-17.222", "-46.875",
    "Paracatu, Minas Gerais (Atlas release; municipal pin).",
    "atlas_luiz_carlos_side_b_20251209",
    "ArcelorMittal and Atlas Renewable Energy have completed part B of the Luiz Carlos Solar Park, 90 days ahead of schedule. The photovoltaic facility, located in Paracatu in northwestern Minas Gerais... has an installed capacity of 315 MWp... The Luiz Carlos Solar Plant, located in Paracatu, Minas Gerais, received investments of R$895 million.",
    "https://atlasrenewableenergy.com/news-and-insights/arcelormittal-and-atlas-renewable-energy-complete-construction-of-a-solar-plant-in-minas-gerais-brazil/",
    "Actor: Atlas Renewable Energy (Miami HQ / GIP USA) — us. CapEx-fill: retain R$895m; add Fed H.10 Sep 25 2026 FX to USD ~172.38m. ≥1/3 U.S. hunt / shuffle solar.",
    "hunt_cycle220", investment_type="bot_completion", evidence="documented", currency="BRL",
    value_usd=str(round(895000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Atlas Renewable Energy. “ArcelorMittal and Atlas Renewable Energy complete construction of a solar plant in Minas Gerais, Brazil.” December 9, 2025. https://atlasrenewableenergy.com/news-and-insights/arcelormittal-and-atlas-renewable-energy-complete-construction-of-a-solar-plant-in-minas-gerais-brazil/.',
    annotation="Atlas Luiz Carlos Side B CapEx-fill ~USD 172.38m via Fed H.10. Supports atlas_luiz_carlos_side_b_bot_2025.",
    evid_note="Opened Atlas company English BOT completion; R$895m / 315 MWp Side B confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 2. engineering_epc / us — CapEx-fill Ascenty SPO06 R$600m
row_doc(
    "ascenty_spo06_600m_brl_2026",
    "infrastructure", "engineering_epc", "us",
    "Ascenty (Digital Realty / Brookfield) — SPO06 data center (Greater São Paulo)",
    "Brazil",
    "Ascenty company English: SPO06 construction advancing on same Greater São Paulo campus as SPO05; estimated investment R$ 600 million; inauguration targeted May 2027. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~115.56m for stored R$600m face. Distinct from ascenty_spo05_300m_brl_2025.",
    "600000000", BRL_FX_DATE, "2026", "-23.50", "-46.60",
    "Ascenty SPO06, Greater São Paulo campus, Brazil (company geography; approximate metro pin).",
    "ascenty_spo05_spo06_campus",
    "SPO05 was announced in July 2025 and represents an investment of R$300 million. SPO06 is scheduled to be inaugurated in May 2027, with an estimated investment of R$600 million. Together, the two data centers will deliver a total capacity of 26 MW.",
    "https://ascenty.com/en/blog/news-ascenty-en/ascenty-sao-paulo-campus/",
    "Actor: Ascenty JV Digital Realty (U.S.) + Brookfield — us. CapEx-fill: retain R$600m; add Fed H.10 Sep 25 2026 FX to USD ~115.56m. ≥1/3 U.S. hunt / shuffle engineering_epc.",
    "hunt_cycle220", investment_type="greenfield_plant", evidence="documented", currency="BRL",
    value_usd=str(round(600000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Ascenty. “Ascenty expands 60 MW São Paulo campus as SPO05 begins operations and SPO06 construction advances.” 2026. https://ascenty.com/en/blog/news-ascenty-en/ascenty-sao-paulo-campus/.',
    annotation="Ascenty SPO06 CapEx-fill ~USD 115.56m via Fed H.10. Supports ascenty_spo06_600m_brl_2026.",
    evid_note="Opened Ascenty English campus page; R$600m SPO06 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 3. solar / allied — CapEx-fill ENGIE Assú Sol R$3.3bn
row_doc(
    "engie_assu_sol_2026",
    "energy", "solar", "allied",
    "ENGIE Brasil — Assú Sol Photovoltaic Complex (Rio Grande do Norte)",
    "Brazil",
    "Assú Sol PV complex reached 100% commercial operation 13 Feb 2026; 895 MWp / 753 MWac installed; ~229.6 average MW free-market commercial capacity; investment worth R$ 3.3 billion. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~635.58m for stored R$3.3bn face.",
    "3300000000", BRL_FX_DATE, "2026", "-5.58", "-36.91",
    "Assú, Rio Grande do Norte (ENGIE geography).",
    "engie_assu_sol_20260223",
    "Built by ENGIE Brasil, the Assú Sol Photovoltaic Complex in Assú (RN) began full commercial operations on February 13 … At an investment worth R$ 3.3 billion and an installed capacity of 895 MWp (753 MWac) and having 229,6 average MW of commercial capacity totally earmarked to the Free Market Environment …",
    "https://www.engie.com.br/en/imprensa/press-releases/assu-sol-photovoltaic-complex-engies-largest-solar-energy-asset-worldwide-now-operating-at-full-commercial-capacity/",
    "Actor: ENGIE Brasil (France) — allied. CapEx-fill: retain R$3.3bn; add Fed H.10 Sep 25 2026 FX to USD ~635.58m. Shuffle solar.",
    "hunt_cycle220", investment_type="ownership_equity", evidence="documented", currency="BRL",
    value_usd=str(round(3300000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ENGIE Brasil. “Assú Sol Photovoltaic Complex — ENGIE’s largest solar energy asset worldwide — now operating at full commercial capacity.” February 23, 2026. https://www.engie.com.br/en/imprensa/press-releases/assu-sol-photovoltaic-complex-engies-largest-solar-energy-asset-worldwide-now-operating-at-full-commercial-capacity/.',
    annotation="ENGIE Assú Sol CapEx-fill ~USD 635.58m via Fed H.10. Supports engie_assu_sol_2026.",
    evid_note="Opened ENGIE Brasil English release; R$3.3bn / 895 MWp / COD 13 Feb 2026 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. other_renewables / prc — CapEx-fill BYD Brazil BESS factory ≤R$500m
row_doc(
    "byd_brazil_bess_factory_500m_2026",
    "energy", "other_renewables", "prc",
    "BYD — industrial BESS production capacity in Brazil (Manaus candidate)",
    "Brazil",
    "Jun/Sep 2026: BYD announces intent to invest up to R$ 500 million in phased industrial capacity to produce stationary BESS systems in Brazil (possible Manaus expansion or new plant; location not finalized on opened page). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~96.30m for stored R$500m ceiling face (UNVERIFIED proxy CapEx retained).",
    "500000000", BRL_FX_DATE, "2026", "-3.1", "-60.02",
    "Manaus candidate / Brazil BESS industrial capacity (press geography; approximate Manaus pin).",
    "poder360_byd_bess_20260612",
    "A montadora chinesa BYD vai investir até R$ 500 milhões na produção de sistemas de armazenamento de energia em baterias no Brasil. O projeto pode ampliar a fábrica de Manaus (AM) ou levar à construção de uma nova unidade industrial no país, ainda sem localização definida.",
    "https://www.poder360.com.br/poder-economia/byd-anuncia-investimento-de-ate-r-500-mi-em-baterias-no-brasil/",
    "Actor: BYD (PRC) — prc. CapEx-fill: retain UNVERIFIED proxy ≤R$500m ceiling; add Fed H.10 Sep 25 2026 FX to USD ~96.30m. Shuffle other_renewables / PRC equal-budget.",
    "hunt_cycle220", investment_type="greenfield_plant", evidence="proxy", currency="BRL",
    value_usd=str(round(500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Poder360. “BYD anuncia investimento de até R$ 500 mi em baterias no Brasil.” June 12, 2026. https://www.poder360.com.br/poder-economia/byd-anuncia-investimento-de-ate-r-500-mi-em-baterias-no-brasil/.',
    annotation="BYD Brazil BESS CapEx-fill ~USD 96.30m via Fed H.10. Supports byd_brazil_bess_factory_500m_2026.",
    evid_note="Opened Poder360; ≤R$500m BESS industrial intent confirmed (UNVERIFIED proxy). CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. graphite / allied — CapEx-fill Graphcoa Jordânia ~R$700m
row_doc(
    "graphcoa_jordania_dfs_capex_2026",
    "resources", "graphite", "allied",
    "Graphcoa / Appian Capital Brazil — Projeto Grafite Jordânia",
    "Brazil",
    "Graphcoa (Appian Capital Brazil) Projeto Grafite Jordânia integrated natural-graphite mine + concentrator at Jordânia (Jequitinhonha Valley, Minas Gerais); press cites ~R$700 million CapEx. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~134.82m for stored R$700m face (UNVERIFIED proxy CapEx retained). Distinct from graphcoa_boa_sorte_bahia_2024.",
    "700000000", BRL_FX_DATE, "2026", "-15.90", "-40.18",
    "Jordânia, Vale do Jequitinhonha, Minas Gerais (press geography).",
    "diario_comercio_graphcoa_jordania_700m",
    "A Graphcoa planeja investir em torno de R$ 700 milhões em uma planta voltada à produção de grafite concentrado, com teores de aproximadamente 95% de carbono grafítico, no município de Jordânia, na região do Vale do Jequitinhonha, em Minas Gerais.",
    "https://diariodocomercio.com.br/economia/graphcoa-grafite-minas/",
    "Actor: Graphcoa / Appian Capital Brazil (UK PE) — allied. CapEx-fill: retain UNVERIFIED proxy ~R$700m; add Fed H.10 Sep 25 2026 FX to USD ~134.82m. Shuffle graphite.",
    "hunt_cycle220", investment_type="feasibility_capex", evidence="proxy", currency="BRL",
    value_usd=str(round(700000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Diário do Comércio. “Graphcoa planeja R$ 700 milhões em grafite em Jordânia (MG).” 2026. https://diariodocomercio.com.br/economia/graphcoa-grafite-minas/.',
    annotation="Graphcoa Jordânia CapEx-fill ~USD 134.82m via Fed H.10. Supports graphcoa_jordania_dfs_capex_2026.",
    evid_note="Opened Diário do Comércio; ~R$700m / Jordânia confirmed (UNVERIFIED proxy). CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 6. nickel / allied — CapEx-fill Centaurus Jaguar BNDES LOI company US$190m (thin)
row_doc(
    "centaurus_jaguar_bndes_loi_2026",
    "resources", "nickel", "allied",
    "BNDES FINEM LOI — R$1 billion debt funding for Centaurus Jaguar Nickel Project",
    "Brazil",
    "Non-binding Letter of Intent from BNDES for R$1 billion (~US$190 million per company) FINEM long-term project finance for 100%-owned Jaguar Nickel Project (Pará). CapEx-fill: enter company dual-quoted US$190 million as value_usd (retain R$1bn face). Distinct from Centaurus Jaguar JVEP CapEx / Glencore offtake rows.",
    "1000000000", "2026-03-23", "2026", "-6.65", "-49.0",
    "Jaguar Nickel Project, Pará (Centaurus geography; approximate).",
    "centaurus_jaguar_bndes_loi_20260323",
    "Centaurus Metals has received a non-binding Letter of Intent from the Brazilian Development Bank (BNDES) for R$1 billion (approximately US$190 million) of long-term project finance debt funding under the FINEM credit line for the Company’s 100%-owned Jaguar Nickel Sulphide Project in Brazil.",
    "https://www.centaurus.com.au/news/bndes-provides-non-binding-letter-of-intent-for-r1-billion-us190-million-of-debt-funding-for-the-jaguar-nickel-project",
    "Actor: Centaurus Metals (Australia) — allied; BNDES LOI financing. CapEx-fill: company dual-quotes ~US$190m alongside R$1bn — store both. Thin nickel top-up / shuffle nickel.",
    "hunt_cycle220", investment_type="financing", evidence="documented", currency="BRL",
    value_usd="190000000", fx_usd=str(round(1000000000 / 190000000, 4)),
    chicago='Centaurus Metals. “BNDES Provides Non-Binding Letter of Intent for R$1 Billion (US$190 Million) of Debt Funding for the Jaguar Nickel Project.” March 23, 2026. https://www.centaurus.com.au/news/bndes-provides-non-binding-letter-of-intent-for-r1-billion-us190-million-of-debt-funding-for-the-jaguar-nickel-project.',
    annotation="Centaurus Jaguar BNDES CapEx-fill company US$190m dual-quote. Supports centaurus_jaguar_bndes_loi_2026.",
    evid_note="Opened Centaurus company primary; R$1bn / ~US$190m BNDES FINEM LOI confirmed. CapEx-fill uses company USD.",
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
    print(f"cycle220 added {len(added)}: {added}")
    print(f"cycle220 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
