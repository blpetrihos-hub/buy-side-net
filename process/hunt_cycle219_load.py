#!/usr/bin/env python3
"""Cycle 219 hunt: shuffle_seed=20261219; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261219).shuffle):
water, building_materials, niobium, port_ownership, solar, other_renewables,
port_cranes, lithium, engineering_epc, bridges_roads, fission_smr, nickel, wind,
rail, copper, graphite, power_plants_grid, balsa.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    dry; next-thinnest graphite CapEx-fill (Graphcoa Boa Sorte R$350m).
≥1/3 U.S. hunt budget spent on Fluence Tubarão + Atlas Luiz Carlos + Ascenty SPO05
+ Wabtec Contagem CapEx-fills + Freeport/EnergyX/EXIM/Bechtel/Fluor/SSA/USTDA/
Nextracker/Jervois sweeps (4 US CapEx-fills; catalog dense otherwise).
PRC equal-budget: ZPMC Tecon Santos CapEx-fill; Sungrow BHP / Goldwind / Envision /
PowerChina / CAMCE already logged; holdovers unsigned.
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
    rid,
    layer,
    subcategory,
    side,
    counterpart,
    country,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    source_id,
    quote,
    url,
    note,
    hunt_support,
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd=None,
    fx_usd=None,
    chicago=None,
    bib_type="company",
    annotation=None,
    evid_note=None,
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd and currency == "USD" else ""
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": investment_type,
            "value": value,
            "currency": currency,
            "value_usd": value_usd,
            "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "",
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": evidence,
            "source_id": source_id,
            "note": note,
            "pair_id": "",
            "counterpart_side": "",
            "counterpart_actor": "",
            "counterpart_value": "",
            "counterpart_currency": "",
            "counterpart_value_usd": "",
            "gap": "",
        },
        {
            "id": rid,
            "retrieved": "2026-10-04",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": evidence,
            "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id,
            "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url,
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. water / us — CapEx-fill Fluence Tubarão R$50m proxy
row_doc(
    "fluence_arcelormittal_tubarao_desal_2021",
    "resources",
    "water",
    "us",
    "Fluence — ArcelorMittal Tubarão seawater desalination plant",
    "Brazil",
    "Fluence South America installed a seawater desalination plant at ArcelorMittal Tubarão (Vitória, Espírito Santo) producing 12,000 m³/day (3.1 MGD); COD 2021. CapEx-fill: retain UNVERIFIED proxy R$50m secondary-press CapEx; Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~9.63m. Distinct from Fluence Eneva Azulão demin row.",
    "50000000",
    BRL_FX_DATE,
    "2021",
    "-20.25",
    "-40.22",
    "ArcelorMittal Tubarão steel complex, Vitória / Serra coast, Espírito Santo.",
    "fluence_tubarao_case",
    "The desalination water treatment project installed by Fluence South America at the Arcelor Mittal Tubarão facility has the ability to produce 3.1 MGD (12,000 m³/day) of treated water. … The Arcelor Mittal Tubarão desalination water treatment plant has demonstrated, since its commissioning in 2021, that the desalination of seawater is a sustainable and acceptable alternative to meeting industrial facility water demands.",
    "https://www.fluencecorp.com/case/seawater-desalination-for-industrial-water-company/",
    "Actor: Fluence Corp (U.S./Nasdaq) — us. CapEx-fill: retain UNVERIFIED proxy R$50m; add Fed H.10 Sep 25 2026 FX to USD ~9.63m. ≥1/3 U.S. hunt / shuffle water.",
    "hunt_cycle219",
    investment_type="plant",
    evidence="proxy",
    currency="BRL",
    value_usd=str(round(50000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    chicago='Fluence Corporation. “Seawater Desalination for Industrial Water Company.” Case study (ArcelorMittal Tubarão, Vitória, Brazil). https://www.fluencecorp.com/case/seawater-desalination-for-industrial-water-company/.',
    annotation="Fluence Tubarão CapEx-fill ~USD 9.63m via Fed H.10. Supports fluence_arcelormittal_tubarao_desal_2021.",
    evid_note="Opened Fluence Tubarão case; 12,000 m³/day / COD 2021 confirmed. CapEx R$50m remains UNVERIFIED proxy; CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 2. solar / us — CapEx-fill Atlas Luiz Carlos R$1.5bn financing
row_doc(
    "atlas_luiz_carlos_fc_1p5bn_brazil_2024",
    "energy",
    "solar",
    "us",
    "Atlas Renewable Energy (GIP) — Luiz Carlos solar complex project finance (Paracatu)",
    "Brazil",
    "15 Aug 2024 Atlas: secures R$1.5 billion financing coordinated by Itaú BBA for Luiz Carlos PV complex in Paracatu, Minas Gerais (R$750m incentivized debentures + R$720m commercial notes). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~288.90m for stored R$1.5bn face. Distinct from atlas_luiz_carlos_side_b_bot_2025 COD row.",
    "1500000000",
    BRL_FX_DATE,
    "2024",
    "-17.222",
    "-46.875",
    "Paracatu, Minas Gerais (Atlas release; municipal pin).",
    "atlas_luiz_carlos_fc_20240815",
    "Atlas Renewable Energy... secured a R$1.5 billion financing coordinated by Itaú BBA for the construction of the Luiz Carlos photovoltaic complex, of which, R$750 million came from incentivized debentures... The remaining R$720 million was obtained through commercial notes.",
    "https://atlasrenewableenergy.com/news-and-insights/atlas-renewable-energy-secures-r1-5-billion-for-the-construction-of-the-luiz-carlos-solar-complex-in-brazil-coordinated-by-itau-bba/",
    "Actor: Atlas Renewable Energy (Miami HQ / GIP USA) — us. CapEx-fill: retain R$1.5bn; add Fed H.10 Sep 25 2026 FX to USD ~288.90m. ≥1/3 U.S. hunt / shuffle solar.",
    "hunt_cycle219",
    investment_type="financing",
    evidence="documented",
    currency="BRL",
    value_usd=str(round(1500000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    chicago='Atlas Renewable Energy. “Atlas Renewable Energy secures R$1.5 billion for the construction of the Luiz Carlos solar complex in Brazil, coordinated by Itaú BBA.” August 15, 2024. https://atlasrenewableenergy.com/news-and-insights/atlas-renewable-energy-secures-r1-5-billion-for-the-construction-of-the-luiz-carlos-solar-complex-in-brazil-coordinated-by-itau-bba/.',
    annotation="Atlas Luiz Carlos CapEx-fill ~USD 288.90m via Fed H.10. Supports atlas_luiz_carlos_fc_1p5bn_brazil_2024.",
    evid_note="Opened Atlas company English financing release; R$1.5bn / Paracatu confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 3. engineering_epc / us — CapEx-fill Ascenty SPO05 R$300m
row_doc(
    "ascenty_spo05_300m_brl_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Ascenty (Digital Realty / Brookfield) — SPO05 data center (Greater São Paulo)",
    "Brazil",
    "Ascenty company English: SPO05 announced Jul 2025; investment R$ 300 million; COD begun on Greater São Paulo campus. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~57.78m for stored R$300m face. Distinct from ascenty_spo06_600m_brl_2026.",
    "300000000",
    BRL_FX_DATE,
    "2025",
    "-23.50",
    "-46.60",
    "Ascenty SPO05, Greater São Paulo campus, Brazil (company geography; approximate metro pin).",
    "ascenty_spo05_spo06_campus",
    "SPO05 was announced in July 2025 and represents an investment of R$300 million. SPO06 is scheduled to be inaugurated in May 2027, with an estimated investment of R$600 million. Together, the two data centers will deliver a total capacity of 26 MW.",
    "https://ascenty.com/en/blog/news-ascenty-en/ascenty-sao-paulo-campus/",
    "Actor: Ascenty JV Digital Realty (U.S.) + Brookfield Infrastructure — us. CapEx-fill: retain R$300m; add Fed H.10 Sep 25 2026 FX to USD ~57.78m. ≥1/3 U.S. hunt / shuffle engineering_epc.",
    "hunt_cycle219",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="BRL",
    value_usd=str(round(300000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    chicago='Ascenty. “Ascenty expands 60 MW São Paulo campus as SPO05 begins operations and SPO06 construction advances.” 2026. https://ascenty.com/en/blog/news-ascenty-en/ascenty-sao-paulo-campus/.',
    annotation="Ascenty SPO05 CapEx-fill ~USD 57.78m via Fed H.10. Supports ascenty_spo05_300m_brl_2025.",
    evid_note="Opened Ascenty English campus page; R$300m SPO05 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. engineering_epc / us — CapEx-fill Wabtec Contagem R$20m
row_doc(
    "wabtec_contagem_r20m_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Wabtec — Contagem Global Engineering Center / plant expansion",
    "Brazil",
    "5 Nov 2025: Wabtec investing R$20 million to expand Brazil operations — first LatAm Global Engineering Center (~9,000 m²) and new locomotive production line at Contagem, Minas Gerais. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~3.85m for stored R$20m face. Distinct from MRS USD 254m equipment package.",
    "20000000",
    BRL_FX_DATE,
    "2025",
    "-19.93",
    "-44.05",
    "Contagem, Minas Gerais — Cidade Industrial Wabtec plant (company geography).",
    "wabtec_contagem_20251105",
    "Wabtec Corporation (NYSE: WAB) is investing R$20 million to expand its operations, capabilities, and workforce in Brazil. … Wabtec plans to establish a Global Engineering Center – the company’s first in Latin America – and the launch of a new locomotive production line.",
    "https://www.wabteccorp.com/newsroom/press-releases/wabtec-to-expand-operations-and-workforce-in-brazil-with-r20-million-investment",
    "Actor: Wabtec (U.S.) — us. CapEx-fill: retain R$20m; add Fed H.10 Sep 25 2026 FX to USD ~3.85m. ≥1/3 U.S. hunt / shuffle engineering_epc.",
    "hunt_cycle219",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="BRL",
    value_usd=str(round(20000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    chicago='Wabtec Corporation. “Wabtec to Expand Operations and Workforce in Brazil with R$20 Million Investment.” November 5, 2025. https://www.wabteccorp.com/newsroom/press-releases/wabtec-to-expand-operations-and-workforce-in-brazil-with-r20-million-investment.',
    annotation="Wabtec Contagem CapEx-fill ~USD 3.85m via Fed H.10. Supports wabtec_contagem_r20m_2025.",
    evid_note="Opened Wabtec company release; R$20m / Contagem GEC confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. port_ownership / allied — CapEx-fill DP World Santos company US$296m dual-quote
row_doc(
    "dpworld_santos_r16bn_2025",
    "infrastructure",
    "port_ownership",
    "allied",
    "DP World — Port of Santos terminal expansion cycle (R$1.6bn)",
    "Brazil",
    "Approved R$1.6 billion (company cites US$296 million) investment cycle to raise Santos terminal capacity 25% to 2.1 million TEU by 2028 (from 1.7m TEU after prior R$450m phase); includes new berth/yard, gates, reefers, and equipment (4 quay cranes, 15 RTGs, 40 ITVs). CapEx-fill: enter company dual-quoted US$296 million as value_usd (retain R$1.6bn face). Distinct from dpworld_santos_equip_2024 (USD 50m equipment tranche).",
    "1600000000",
    "2025-12-02",
    "2025",
    "-23.93",
    "-46.32",
    "DP World Santos left-bank terminal (company release).",
    "dpworld_santos_r16bn_20251202",
    "DP World has approved a new R$1.6 billion (US$296 million) investment cycle to further strengthen Brazil’s trade capacity and enhance terminal operations at the Port of Santos, increasing total handling capacity by 25% to 2.1 million TEUs … by 2028.",
    "https://www.dpworld.com/en/news/usa/dpw-invests-over-1-billion-reais-to-expand-santos-terminal-by-25-percent",
    "Actor: DP World (UAE) — allied. CapEx-fill: company dual-quotes US$296m alongside R$1.6bn — store both (value_usd=296m; company FX ≈5.4054 BRL/USD on release date). Shuffle port_ownership.",
    "hunt_cycle219",
    investment_type="concession_capex",
    evidence="documented",
    currency="BRL",
    value_usd="296000000",
    fx_usd=str(round(1600000000 / 296000000, 4)),
    chicago='DP World. “DP World to invest R$1.6 billion to expand Santos Terminal by 25%.” December 2, 2025. https://www.dpworld.com/en/news/usa/dpw-invests-over-1-billion-reais-to-expand-santos-terminal-by-25-percent.',
    annotation="DP World Santos CapEx-fill company US$296m dual-quote. Supports dpworld_santos_r16bn_2025.",
    evid_note="Opened DP World company release; R$1.6bn / US$296m dual-quote / 2.1m TEU by 2028 confirmed. CapEx-fill uses company USD.",
)

# 6. port_cranes / prc — CapEx-fill ZPMC Tecon Santos R$300m
row_doc(
    "zpmc_santos_brasil_sts_rtg_2026",
    "infrastructure",
    "port_cranes",
    "prc",
    "ZPMC — Santos Brasil Tecon Santos STS + electric RTG delivery",
    "Brazil",
    "Delivery of 2 STS quay cranes + 8 electric RTGs (ZPMC) to Tecon Santos; package ~R$300 million; arrived 10 Jan 2026 on Zhen Hua 28. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~57.78m for stored R$300m face. Distinct from ZPMC Itapoá / MultiRio rows.",
    "300000000",
    BRL_FX_DATE,
    "2026",
    "-23.92",
    "-46.38",
    "Tecon Santos, left bank Port of Santos (Santos Brasil release).",
    "santosbrasil_zpmc_20260112",
    "Os equipamentos, fabricados pela chinesa ZPMC, chegaram ao Tecon Santos ... a bordo do navio Zhen Hua 28. ... Os dez guindastes têm investimentos da ordem de R$ 300 milhões.",
    "https://www.santosbrasil.com.br/v2021/noticia/novos-guindastes-de-operacao-remota-chegam-ao-tecon-santos",
    "Actor: ZPMC (PRC OEM); buyer Santos Brasil. CapEx-fill: retain R$300m; add Fed H.10 Sep 25 2026 FX to USD ~57.78m. Shuffle port_cranes / PRC equal-budget.",
    "hunt_cycle219",
    investment_type="equipment_supply",
    evidence="documented",
    currency="BRL",
    value_usd=str(round(300000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    chicago='Santos Brasil. “Novos guindastes de operação remota chegam ao Tecon Santos.” January 12, 2026. https://www.santosbrasil.com.br/v2021/noticia/novos-guindastes-de-operacao-remota-chegam-ao-tecon-santos.',
    annotation="ZPMC Tecon Santos CapEx-fill ~USD 57.78m via Fed H.10. Supports zpmc_santos_brasil_sts_rtg_2026.",
    evid_note="Opened Santos Brasil Portuguese news; ~R$300m / 2 STS + 8 e-RTG / Zhen Hua 28 confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 7. graphite / allied — CapEx-fill Graphcoa Boa Sorte R$350m (thin next-thinnest)
row_doc(
    "graphcoa_boa_sorte_bahia_2024",
    "resources",
    "graphite",
    "allied",
    "Graphcoa (Appian Capital Advisory) — Boa Sorte integrated graphite mine/plant, Itagimirim",
    "Brazil",
    "Boa Sorte mine + concentration plant began operations Dec 2024; ramp to 5,500 tpy by Aug 2025; Phase 1 investment R$350 million. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~67.41m for stored R$350m face. Distinct from Graphcoa Jordânia DFS CapEx row.",
    "350000000",
    BRL_FX_DATE,
    "2024",
    "-16.0",
    "-40.0",
    "Itagimirim, southern Bahia (Appian / Graphcoa interview).",
    "appian_graphcoa_20250409",
    "in December 2024, Graphcoa began operations at its first integrated graphite production facility in Itagimirim, southern Bahia. ... In this first phase, R$ 350 million was invested to implement the Boa Sorte mine in Itagimirim, southern Bahia.",
    "https://appiancapitaladvisory.com/graphcoas-new-graphite-plant-boosts-energy-transition-in-brazil/",
    "Actor: Graphcoa / Appian Capital Advisory (UK PE) — allied. CapEx-fill: retain R$350m; add Fed H.10 Sep 25 2026 FX to USD ~67.41m. Thin graphite top-up (balsa/nickel/fission_smr dry).",
    "hunt_cycle219",
    investment_type="ownership_equity",
    evidence="documented",
    currency="BRL",
    value_usd=str(round(350000000 / float(BRL_USD), 2)),
    fx_usd=BRL_USD,
    chicago='Appian Capital Advisory / Minera Brasil. “Graphcoa’s new graphite plant boosts energy transition in Brazil.” April 9, 2025. https://appiancapitaladvisory.com/graphcoas-new-graphite-plant-boosts-energy-transition-in-brazil/.',
    annotation="Graphcoa Boa Sorte CapEx-fill ~USD 67.41m via Fed H.10. Supports graphcoa_boa_sorte_bahia_2024.",
    evid_note="Opened Appian Graphcoa page; R$350m Phase 1 / Dec 2024 COD confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
    print(f"cycle219 added {len(added)}: {added}")
    print(f"cycle219 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
