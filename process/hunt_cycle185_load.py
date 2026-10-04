#!/usr/bin/env python3
"""Cycle 185 hunt: shuffle_seed=20261185; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF order + Random(20261185)):
water, lithium, fission_smr, copper, other_renewables, niobium, graphite,
bridges_roads, solar, wind, port_cranes, port_ownership, balsa, rail, nickel,
engineering_epc, building_materials, power_plants_grid.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (Plantabal/AIMA/WITS Ecuador balsa; Centaurus/Atlantic Nickel
already dense; Meitner/Colombia/Peru FIRST fission already logged).
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km; CCECC Nicaragua rail.
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
    pair_id="",
    counterpart_side="",
    counterpart_actor="",
    counterpart_value="",
    counterpart_currency="",
    counterpart_value_usd="",
    gap="",
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
            "pair_id": pair_id,
            "counterpart_side": counterpart_side,
            "counterpart_actor": counterpart_actor,
            "counterpart_value": counterpart_value,
            "counterpart_currency": counterpart_currency,
            "counterpart_value_usd": counterpart_value_usd,
            "gap": gap,
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


# 1. copper / allied — FQM Taca Taca initial CapEx fill from NI 43-101 presentation
row_doc(
    "fqm_taca_taca_initial_capex_4232m_2026",
    "resources",
    "copper",
    "allied",
    "First Quantum — Taca Taca initial CapEx to 40 Mtpa (USD 4.232bn)",
    "Argentina",
    "19 Feb 2026 First Quantum Taca Taca presentation (NI 43-101 Technical Report Jan 2026): initial capital to 40 Mtpa USD 4,232 million; expansion capital to 60 Mtpa USD 1,019 million; total development capital USD 5,250 million; Salta Province Puna; sanction pending ESIA/water/RIGI. CapEx = USD 4,232m initial train face. Distinct from fqm_taca_taca_argentina_2026 ownership row (CapEx blank) — this is the documented study CapEx fill.",
    "4232000000",
    "2026-02-19",
    "2026",
    "-24.60",
    "-67.70",
    "Taca Taca project, Salta Province, Argentina (company geography; approximate).",
    "fqm_taca_taca_presentation_20260219",
    "Initial capital to 40 Mtpa ($M) 4,232",
    "https://www.first-quantum.com/wp-content/uploads/2026/02/Taca-Taca-Presentation-FINAL.pdf",
    "Actor: First Quantum Minerals (Canada) — allied. Company investor presentation citing NI 43-101 Jan 2026. Pre-sanction study CapEx. Shuffle copper.",
    "hunt_cycle185",
    investment_type="feasibility_capex",
    evidence="documented",
    bib_type="company",
    chicago='First Quantum Minerals Ltd. “Taca Taca — NI 43-101 Technical Report presentation.” February 19, 2026. https://www.first-quantum.com/wp-content/uploads/2026/02/Taca-Taca-Presentation-FINAL.pdf.',
    annotation="FQM: Taca Taca initial CapEx USD 4.232bn. Supports fqm_taca_taca_initial_capex_4232m_2026.",
    evid_note="Opened First Quantum Taca Taca presentation PDF 2026-10-04.",
)

# 2. solar / us — Atlas Shangri-La IDB Invest / Bancolombia financing
row_doc(
    "atlas_shangri_la_idb_113m_2024",
    "energy",
    "solar",
    "us",
    "Atlas Renewable Energy — Shangri-La solar senior loan (IDB Invest / Bancolombia)",
    "Colombia",
    "IDB Invest / Atlas: long-term senior secured loan totaling COP 473.77 billion (approximately USD 113 million) from IDB Invest and Bancolombia for development/construction/operation of Shangri-La 201 MWp / 160 MWac PV in Tolima (Ibagué/Piedras); Atlas debut in Colombia; ISAGEN 1,000 MW partnership pipeline. CapEx/financing face = USD 113m approximate package. Distinct from atlas_shangri_la_colombia_201mwp_2025 COD row (CapEx blank on inauguration page).",
    "113000000",
    "2024-09-10",
    "2024",
    "4.4389",
    "-75.2322",
    "Shangri-La / Ibagué, Tolima, Colombia (same pin family as COD row).",
    "idb_invest_atlas_shangri_la_2024",
    "The financial package includes a senior secured loan totaling COP 473.77 billion (approximately $113 million), provided by IDB Invest and Bancolombia.",
    "https://idbinvest.org/en/news-media/idb-invest-bancolombia-and-atlas-renewable-energy-announce-investment-boost-colombias",
    "Actor: Atlas Renewable Energy (Miami HQ / GIP USA) — us. Official IDB Invest English release. Financing complements COD row. ≥1/3 U.S. hunt budget. Shuffle solar.",
    "hunt_cycle185",
    investment_type="financing",
    evidence="documented",
    bib_type="government",
    chicago='IDB Invest. “IDB Invest, Bancolombia and Atlas Renewable Energy Announce Investment to Boost Colombia’s Energy Transition.” https://idbinvest.org/en/news-media/idb-invest-bancolombia-and-atlas-renewable-energy-announce-investment-boost-colombias.',
    annotation="IDB Invest: Shangri-La ~USD 113m senior loan. Supports atlas_shangri_la_idb_113m_2024.",
    evid_note="Opened IDB Invest English news page 2026-10-04 (Enerdata cites 13 Sep 2024 close).",
)

# 3. power_plants_grid / allied — ENGIE Brasil ANEEL Transmission Auction 01/2026
row_doc(
    "engie_brasil_aneel_01_2026_15bn",
    "energy",
    "power_plants_grid",
    "allied",
    "ENGIE Brasil — ANEEL Transmission Auction 01/2026 Lots 2 + 3A–3D",
    "Brazil",
    "27 Mar 2026 ENGIE Brasil: subsidiary ENGIE Transmissão de Energia Participações wins Lot 2 (PR/SC ~143 km 230 kV) and Lots 3A–3D synchronous compensators (RN/CE) at ANEEL Transmission Auction 01/2026 (B3); contracted RAP R$122.7 million; ANEEL-estimated total CapEx about R$1.5 billion (Lot 2 >R$193m; Lot 3 sublots R$285.1m / R$272.1m / R$538.8m / R$285.1m per CVM IPE table). 30-year concessions; 42-month build. CapEx = R$1.5bn ANEEL estimate face. Distinct from engie_peru_grupo1_transmision_230m_2026.",
    "1500000000",
    "2026-03-27",
    "2026",
    "",
    "",
    "Multi-state transmission package (PR/SC Lot 2; RN/CE Lot 3) — lat/lon blank (multi-site).",
    "engie_brasil_aneel_01_20260327",
    "O lote 2 e os sublotes 3A, 3B, 3C e 3D foram arrematados com uma Receita Anual Permitida (RAP) de R$ 122,7 milhões e investimentos totais estimados pela ANEEL em cerca de R$ 1,5 bilhão",
    "https://www.engie.com.br/imprensa/press-releases/engie-arremata-lote-2-e-sublotes-do-3-no-leilao-da-aneel/",
    "Actor: ENGIE Brasil / ENGIE (France) — allied. Company Portuguese primary; CapEx = ANEEL estimated ~R$1.5bn (BRL stored without FX). Shuffle power_plants_grid.",
    "hunt_cycle185",
    investment_type="concession",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='ENGIE Brasil. “ENGIE arremata lote 2 e sublotes do 3 no leilão da ANEEL e reforça sua atuação em transmissão.” March 27, 2026. https://www.engie.com.br/imprensa/press-releases/engie-arremata-lote-2-e-sublotes-do-3-no-leilao-da-aneel/.',
    annotation="ENGIE Brasil: ANEEL 01/2026 Lots 2+3 CapEx ~R$1.5bn. Supports engie_brasil_aneel_01_2026_15bn.",
    evid_note="Opened ENGIE Brasil Portuguese press release 2026-10-04; cross-checked CVM IPE English/Portuguese lot CapEx table.",
)

# 4. power_plants_grid / prc — CWE CGE Transmisión Pitrufquén OA
row_doc(
    "cwe_cge_pitrufquen_14p2m_2026",
    "energy",
    "power_plants_grid",
    "prc",
    "CWE — CGE Transmisión OA Ampliación S/E Pitrufquén (NTR ATMT)",
    "Chile",
    "16 Jun 2026 CGE Transmisión Acta de Adjudicación (CGET_OA_1_2025): China International Water & Electric Corporation, Agencia en Chile awarded Ampliación en S/E Pitrufquén (NTR ATMT) — VI adjudicado USD 14,229,952.64. CapEx/award face = VI. Distinct from cwe_zapallar_embalse_chile_2026 (water) and nari_cge_parronal_casas_viejas_19p2m_2026.",
    "14229952.64",
    "2026-06-16",
    "2026",
    "-38.99",
    "-72.64",
    "S/E Pitrufquén, Región de La Araucanía, Chile (CGE OA geography; approximate municipal pin).",
    "cge_oa_acta_adjudicacion_20260616",
    "24_266_OA_30 Ampliación en S/E Pitrufquén (NTR ATMT) China International Water & Electric Corporation, Agencia en Chile 14.229.952,64",
    "https://www.coordinador.cl/wp-content/uploads/2026/06/CGET_OA_1_2025_Acta-de-Adjudicacion-Rev.0.pdf",
    "Actor: CWE (PRC SOE / PowerChina group) Agencia en Chile — prc. Official CGE Transmisión award acta. Same source_id family as Nari OA row (supports both). Shuffle power_plants_grid.",
    "hunt_cycle185",
    investment_type="epc",
    evidence="documented",
    bib_type="government",
    chicago='CGE Transmisión. “Acta de Adjudicación — Licitación Pública Internacional Obras de Ampliación CGE Transmisión (CGET_OA_1_2025).” June 16, 2026. https://www.coordinador.cl/wp-content/uploads/2026/06/CGET_OA_1_2025_Acta-de-Adjudicacion-Rev.0.pdf.',
    annotation="CGE OA acta: CWE Pitrufquén VI USD 14.23m. Supports cwe_cge_pitrufquen_14p2m_2026.",
    evid_note="Opened Coordinador-hosted CGE Transmisión Acta PDF 2026-10-04.",
)

# 5. copper / prc — CR19G Mirador South Pit mining/stripping services (proxy)
row_doc(
    "cr19g_mirador_south_pit_1537m_2026",
    "resources",
    "copper",
    "prc",
    "CR19G — Mirador South Pit open-pit mining/stripping services (2026–2036)",
    "Ecuador",
    "Aug 2026 Chinese trade/press (Seetao / Tianyancha reprints): China Railway 19th Bureau Group (CR19G) wins bid for Mirador copper mine South Pit open-pit mining and production-stripping professional services 2026–2036 in Zamora Chinchipe; contract amount USD 1,537,529,323.54 excl. VAT; term 1 Sep 2026–31 Aug 2036; annual rolling contracts; owner-operated Chinese Mirador complex. CapEx/contract face = USD 1,537,529,323.54. UNVERIFIED proxy — no opened Ecuadoran award decree this cycle. Distinct from Mirador Phase II mining-contract delay notices.",
    "1537529323.54",
    "2026-08-01",
    "2026",
    "-3.56",
    "-78.50",
    "Mirador mine / Zamora Chinchipe, Ecuador (press geography; approximate).",
    "seetao_cr19g_mirador_20260801",
    "CR19G has won the bid for the 2026-2036 open-pit mining and production stripping project at the southern mining site of Mirado Copper Mine in Ecuador, with a total contract amount of approximately 1.537 billion US dollars",
    "https://www.seetaoe.com/details/273290.html",
    "Actor: China Railway 19th Bureau Group / CRCC (PRC) — prc. UNVERIFIED proxy: Seetao English reprint of Chinese award notice citing USD 1,537,529,323.54. Shuffle copper.",
    "hunt_cycle185",
    investment_type="services_contract",
    evidence="proxy",
    bib_type="press",
    chicago='Seetao. “CR19G Wins 10-Year Mining Deal at Ecuador’s Mirador Copper Mine.” August 1, 2026. https://www.seetaoe.com/details/273290.html.',
    annotation="Seetao proxy: CR19G Mirador South Pit ~USD 1.537bn. Supports cr19g_mirador_south_pit_1537m_2026.",
    evid_note="Opened Seetao English page 2026-10-04; Tianyancha Chinese reprints corroborate USD 1,537,529,323.54 figure.",
)

# Thin top-up + remaining shuffle slots dry: water, lithium, fission_smr, other_renewables,
# niobium, graphite, bridges_roads, wind, port_cranes, port_ownership, balsa, rail, nickel,
# engineering_epc, building_materials (catalog dense; AES Pacífico 1.745bn / ENGIE Peru
# Grupo1 award / Sacyr Coquimbo / Vicuña RIGI / Progress Rail VLI / Fluor ICA already
# logged; Halliburton oil/gas out of taxonomy; holdovers unsigned).


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
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added: list[str] = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_entry)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"cycle185 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
