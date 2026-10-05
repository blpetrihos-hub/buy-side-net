#!/usr/bin/env python3
"""Cycle 238 hunt: shuffle_seed=20261238; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261238).shuffle):
niobium, engineering_epc, bridges_roads, nickel, lithium, copper, port_cranes,
graphite, power_plants_grid, rail, other_renewables, port_ownership, solar,
fission_smr, building_materials, water, wind, balsa.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Equinix LatAm USD 419m 2025–26; CapEx-fill McDermott
  Brava Papa-Terra/Atlanta USD 1m floor of sizeable range; honest residual sweeps.
PRC equal-budget: CapEx-fill CRRC Araraquara factory R$50m.
NEW/CapEx allied: Vicuña Stage 1 USD 7.1bn (Lundin PEA); Konecranes Super Terminais
  Manaus R$120m CapEx-fill.
Skipped: RAP-as-CapEx; Huaxin–CSN; Xinhai MoU; Aldesa EUR; UFN fertilizer archived
  out-of-scope; COP/CLP/PEN (no Fed H.10); Siemens/Hitachi Trivia CapEx undisclosed;
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

EUR_USD = "1.1400"
EUR_FX_DATE = "2026-09-25"
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


# 1. NEW engineering_epc / us — Equinix LatAm CapEx cycle USD 419m 2025–26
row_doc(
    "equinix_latam_419m_2025_2026",
    "infrastructure", "engineering_epc", "us",
    "Equinix — Latin America IBX CapEx cycle 2025–2026",
    "Brazil",
    "26 May 2026 Equinix: between 2025 and 2026 announced and executed investments exceeding USD 419 million across strategic LatAm markets — Brazil USD 270m, Mexico USD 81m, Chile USD 42m, Colombia USD 28m — expanding IBX data centers and interconnection for cloud/AI. CapEx: enter company USD 419m floor (\"superiores a USD 419 milhões\"). Distinct from site-level equinix_sp6 / mo2 / st2 / bogota_dc2 / rj3 rows (nested components).",
    "419000000", "2026-05-26", "2026", "-23.45", "-46.53",
    "Equinix LatAm IBX footprint (São Paulo pin; multi-country program).",
    "equinix_latam_419m_20260526",
    "Entre 2025 e 2026, a Equinix anunciou e executou investimentos superiores a USD 419 milhões em mercados estratégicos da América Latina, incluindo México (USD 81 milhões), Brasil (USD 270 milhões), Chile (USD 42 milhões) e Colômbia (USD 28 milhões).",
    "https://newsroom.equinix.com/2026-05-26-America-Latina-e-a-regiao-de-maior-crescimento-e-mais-dinamica-para-a-Equinix",
    "Actor: Equinix (U.S. Nasdaq:EQIX) — us. NEW row: company Portuguese >USD 419m LatAm 2025–26 CapEx. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle238", investment_type="capex_program", evidence="documented", currency="USD",
    value_usd="419000000", fx_usd="1",
    chicago='Equinix. “América Latina é a região de maior crescimento e mais dinâmica para a Equinix.” May 26, 2026. https://newsroom.equinix.com/2026-05-26-America-Latina-e-a-regiao-de-maior-crescimento-e-mais-dinamica-para-a-Equinix.',
    annotation="Equinix LatAm NEW USD 419m floor. Supports equinix_latam_419m_2025_2026.",
    evid_note="Opened Equinix Portuguese newsroom; >USD 419m / Brazil 270 / Mexico 81 / Chile 42 / Colombia 28 confirmed.",
)

# 2. engineering_epc / us — CapEx-fill McDermott Brava Papa-Terra/Atlanta USD 1m floor
row_doc(
    "mcdermott_brava_papa_terra_atlanta_2025",
    "infrastructure", "engineering_epc", "us",
    "McDermott — BRAVA Energia Papa-Terra + Atlanta Phase 2 T&I",
    "Brazil",
    "7 Jul 2025 McDermott: sizeable offshore transportation and installation contract by BRAVA Energia for flexible pipelines, umbilicals and associated subsea equipment for two new wells at Papa-Terra (Campos) and two new wells for Atlanta Phase 2 (Santos BS-4); includes pre-commissioning and onshore base support. CapEx-fill: enter USD 1m floor of McDermott-defined sizeable range (USD 1–50 million).",
    "1000000", "2025-07-07", "2025", "-22.00", "-40.00",
    "Papa-Terra Campos Basin / Atlanta Santos Basin offshore Brazil (Campos pin).",
    "mcdermott_brava_20250707",
    "McDermott has been awarded a sizeable* offshore transportation and installation contract by BRAVA Energia… *McDermott defines a sizeable contract as between USD $1 million and USD $50 million.",
    "https://www.mcdermott.com/press-release-detail/123052/mcdermott-awarded-offshore-contract-brazils-brava-energia",
    "Actor: McDermott (U.S.) — us. CapEx-fill: enter USD 1m floor of sizeable USD 1–50m range. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle238", investment_type="epc", evidence="documented", currency="USD",
    value_usd="1000000", fx_usd="1",
    chicago='McDermott. “McDermott Awarded Offshore Contract by Brazil’s BRAVA Energia.” July 7, 2025. https://www.mcdermott.com/press-release-detail/123052/mcdermott-awarded-offshore-contract-brazils-brava-energia.',
    annotation="McDermott Brava CapEx-fill USD 1m floor. Supports mcdermott_brava_papa_terra_atlanta_2025.",
    evid_note="Opened McDermott English; sizeable = USD 1–50m / Papa-Terra+Atlanta Phase 2 confirmed. CapEx-fill enter USD 1m floor.",
)

# 3. rail / prc — CapEx-fill CRRC Araraquara factory R$50m
row_doc(
    "crrc_araraquara_factory_2026",
    "infrastructure", "rail", "prc",
    "CRRC Brasil — Araraquara rolling-stock factory (initial CapEx)",
    "Brazil",
    "24–25 Mar 2026: CRRC Brasil Equipamentos Ferroviários inaugurates factory at former Hyundai Rotem plant in Araraquara (SP) to assemble São Paulo Metro Frota R (44 trains) and support TIC Eixo Norte; initial investment R$50 million; ~100 direct jobs; production from 2H2026. CapEx-fill: Fed H.10 Sep 25 2026 BRL 5.1921 → USD ~9.63m.",
    "50000000", BRL_FX_DATE, "2026", "-21.79", "-48.18",
    "CRRC Araraquara factory (former Hyundai Rotem plant, SP-255).",
    "atarde_crrc_araraquara_50m_20260324",
    "Com um investimento inicial de R$ 50 milhões, a previsão é que a planta gere cerca de 100 empregos diretos, com a produção efetiva começando já no segundo semestre deste ano.",
    "https://atarde.com.br/economia/fabrica-de-trens-chinesa-inaugura-fabrica-de-r-50-milhoes-no-brasil-1383605",
    "Actor: CRRC (PRC) — prc. CapEx-fill: enter R$50m initial factory CapEx; Fed H.10 USD. UNVERIFIED proxy press (A Tarde citing company/gov event). Shuffle rail / PRC equal-budget.",
    "hunt_cycle238", investment_type="capex_program", evidence="press", currency="BRL",
    value_usd=str(round(50000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Abreu, Yuri. “CRRC Brasil inaugura nova fábrica de trens de R$ 50 milhões.” A Tarde, March 24, 2026. https://atarde.com.br/economia/fabrica-de-trens-chinesa-inaugura-fabrica-de-r-50-milhoes-no-brasil-1383605.',
    annotation="CRRC Araraquara CapEx-fill ~USD 9.63m via Fed H.10 (proxy). Supports crrc_araraquara_factory_2026.",
    evid_note="Opened A Tarde Portuguese; R$50m initial / Araraquara / Frota R confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. copper / allied — NEW Vicuña Stage 1 initial CapEx USD 7.1bn (Lundin PEA)
row_doc(
    "vicuna_stage1_capex_7p1bn_2026",
    "resources", "copper", "allied",
    "Vicuña Corp (BHP/Lundin) — Stage 1 initial CapEx (Josemaría sulphide mill)",
    "Argentina",
    "16 Feb 2026 Lundin Mining: Vicuña integrated PEA — Stage 1 (sulphide mill + Josemaría deposit) total initial capital cost estimated at USD 7.1 billion; Stages 1–3 USD 18.1 billion; FID Stage 1 targeted end-2026; Vicuña is 50/50 BHP–Lundin JV. CapEx: enter USD 7.1bn Stage 1 initial face. Distinct from vicuna_rigi_peelp_2026 (RIGI declared total USD 9.737bn covering Stage 1 + aspects of Stage 2).",
    "7100000000", "2026-02-16", "2026", "-28.90", "-69.50",
    "Josemaría deposit / Vicuña Stage 1 mill, San Juan Province (company geography).",
    "lundin_vicuna_pea_20260216",
    "Total initial capital cost for Stage 1 is estimated at $7.1 billion and $18.1 billion for stages 1-3.",
    "https://www.lundinmining.com/news/lundin-mining-announces-vicua-integrated-technical-study-results-highlighting-a-world-class-mining-district",
    "Actor: Vicuña Corp — BHP (Australia) + Lundin Mining (Canada) — allied. NEW row: company English Stage 1 USD 7.1bn PEA CapEx. Shuffle copper.",
    "hunt_cycle238", investment_type="capex_program", evidence="documented", currency="USD",
    value_usd="7100000000", fx_usd="1",
    chicago='Lundin Mining. “Lundin Mining Announces Vicuña Integrated Technical Study Results Highlighting a World-Class Mining District.” February 16, 2026. https://www.lundinmining.com/news/lundin-mining-announces-vicua-integrated-technical-study-results-highlighting-a-world-class-mining-district.',
    annotation="Vicuña Stage 1 NEW USD 7.1bn. Supports vicuna_stage1_capex_7p1bn_2026.",
    evid_note="Opened Lundin English; Stage 1 initial capital $7.1 billion / Stages 1–3 $18.1 billion confirmed.",
)

# 5. port_cranes / allied — CapEx-fill Konecranes Super Terminais Manaus R$120m
row_doc(
    "konecranes_super_terminais_manaus_2025",
    "infrastructure", "port_cranes", "allied",
    "Konecranes — Super Terminais Manaus three Gottwald ESP.10 MHCs",
    "Brazil",
    "8 Jul 2026 Logweb (terminal): Super Terminais receives three new electric Konecranes Gottwald ESP 10 mobile harbor cranes at Port of Manaus; investment of R$120 million as part of energy-transition / pier expansion (pier +120 m to 720 m; berths 4→6). CapEx-fill: Fed H.10 Sep 25 2026 BRL 5.1921 → USD ~23.11m. Matches prior hunt note of Q2 2025 repeat order / Q3 2026 handover.",
    "120000000", BRL_FX_DATE, "2026", "-3.14", "-60.02",
    "Super Terminais, Port of Manaus (Amazonas).",
    "logweb_super_terminais_konecranes_20260708",
    "A Super Terminais… recebeu três novos guindastes elétricos da fabricante alemã Konecranes. O investimento de R$ 120 milhões integra o plano de transição energética da companhia e amplia para seis o número de equipamentos elétricos em operação no terminal.",
    "https://logweb.com.br/super-terminais-guindastes-eletricos-infraestrutura-portuaria-manaus/",
    "Actor: Konecranes (Finland) — allied; buyer Super Terminais. CapEx-fill: enter R$120m package; Fed H.10 USD. UNVERIFIED proxy press. Shuffle port_cranes.",
    "hunt_cycle238", investment_type="equipment", evidence="press", currency="BRL",
    value_usd=str(round(120000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Logweb. “Super Terminais amplia infraestrutura portuária com três novos guindastes elétricos e investimento de R$ 120 milhões.” July 8, 2026. https://logweb.com.br/super-terminais-guindastes-eletricos-infraestrutura-portuaria-manaus/.',
    annotation="Konecranes Manaus CapEx-fill ~USD 23.11m via Fed H.10 (proxy). Supports konecranes_super_terminais_manaus_2025.",
    evid_note="Opened Logweb Portuguese; R$120m / three Gottwald ESP 10 / Manaus confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle238 added {len(added)}: {added}")
    print(f"cycle238 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
