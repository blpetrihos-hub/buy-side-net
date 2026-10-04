#!/usr/bin/env python3
"""Cycle 192 hunt: shuffle_seed=20261192; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261192).shuffle):
building_materials, fission_smr, lithium, engineering_epc, port_cranes,
other_renewables, port_ownership, copper, balsa, solar, graphite,
power_plants_grid, nickel, water, wind, rail, bridges_roads, niobium.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr —
all dry this pass (catalog dense; Banova/AIMA/Plantabal already logged; holdovers unsigned).
≥1/3 U.S. hunt budget spent on SEC Pacasmayo / Digital Realty–Ascenty /
Freeport/EXIM/DFC/USTDA/NADBank/AES/Wabtec/Progress — 2 new U.S. rows
(Ascenty SPO05 R$300m + SPO06 R$600m; Digital Realty JV coded us).
Holdovers unsigned: CRBC Corentyne; CSCEC Nicaragua 290 km package decree;
CCECC Nicaragua rail still prefeasibility/feasibility.
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


# 1. building_materials / other — Cementos Pacasmayo 2025 CapEx S/144.3m (SEC 6-K)
row_doc(
    "pacasmayo_capex_144p3m_pen_2025",
    "infrastructure",
    "building_materials",
    "other",
    "Cementos Pacasmayo — 2025 sustaining CapEx (Pacasmayo/Piura/Rioja + concrete/aggregates)",
    "Peru",
    "12 Feb 2026 Cementos Pacasmayo SEC Form 6-K / Ex. 99.1 (4Q25/FY2025): as of 31 Dec 2025 company invested S/ 144.3 million (US$ 43.0 million stated on page) — Pacasmayo Plant Projects S/45.1m; Concrete and aggregates equipment S/62.9m; Piura Plant Projects S/29.1m; Rioja Plant Projects S/4.7m; Other S/2.5m. PEN stored without FX. Distinct from Holcim majority-stake acquisition rows (agreement/completion/ASPI cash).",
    "144300000",
    "2025-12-31",
    "2025",
    "-7.40",
    "-79.55",
    "Pacasmayo cement plant, northern Peru (company CapEx table; approximate plant pin).",
    "cpac_sec_6k_4q25_capex",
    "As of December 31, 2025 the Company invested S/ 144.3 million (US$ 43.0 million), allocated to the following projects: Pacasmayo Plant Projects 45.1; Concrete and aggregates equipment 62.9; Rioja Plant Projects 4.7; Piura Plant Projects 29.1; Other 2.5; Total 144.3",
    "https://www.sec.gov/Archives/edgar/data/1221029/000121390026015786/ea027662101ex99-1_cementos.htm",
    "Actor: Cementos Pacasmayo (Peruvian NYSE:CPAC; Holcim majority agreement then pending close) — other (host-country issuer CapEx). SEC EDGAR English 6-K exhibit. CapEx = PEN 144.3m (no FX). Shuffle building_materials; ≥1/3 U.S. hunt (SEC EDGAR).",
    "hunt_cycle192",
    investment_type="sustaining_capex",
    evidence="documented",
    currency="PEN",
    value_usd="",
    fx_usd="",
    bib_type="sec",
    chicago='Cementos Pacasmayo S.A.A. “Consolidated Results for the Fourth Quarter and Year 2025” (Form 6-K Exhibit 99.1). February 12, 2026. https://www.sec.gov/Archives/edgar/data/1221029/000121390026015786/ea027662101ex99-1_cementos.htm.',
    annotation="SEC 6-K: Pacasmayo FY2025 CapEx S/144.3m. Supports pacasmayo_capex_144p3m_pen_2025.",
    evid_note="Opened SEC EDGAR Ex. 99.1 CapEx table 2026-10-04.",
)

# 2. engineering_epc / us — Ascenty SPO05 Greater São Paulo R$300m (Digital Realty JV)
row_doc(
    "ascenty_spo05_300m_brl_2025",
    "infrastructure",
    "engineering_epc",
    "us",
    "Ascenty (Digital Realty / Brookfield) — SPO05 data center (Greater São Paulo)",
    "Brazil",
    "Ascenty company English: SPO05 announced Jul 2025; investment R$ 300 million; COD begun on Greater São Paulo campus; campus with SPO06 adds 26 MW combined. Digital Realty (U.S.) + Brookfield Infrastructure JV — coded us (U.S. hyperscale/colocation side, parallel CloudHQ). BRL stored without FX. Distinct from cloudhq_queretaro_campus_4p8bn_2025.",
    "300000000",
    "2025-07-01",
    "2025",
    "-23.50",
    "-46.60",
    "Ascenty SPO05, Greater São Paulo campus, Brazil (company geography; approximate metro pin).",
    "ascenty_spo05_spo06_campus",
    "SPO05 was announced in July 2025 and represents an investment of R$300 million. SPO06 is scheduled to be inaugurated in May 2027, with an estimated investment of R$600 million. Together, the two data centers will deliver a total capacity of 26 MW.",
    "https://ascenty.com/en/blog/news-ascenty-en/ascenty-sao-paulo-campus/",
    "Actor: Ascenty JV Digital Realty (U.S.) + Brookfield Infrastructure (Canada) — us. Company English primary. CapEx = R$300m. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle192",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Ascenty. “Ascenty expands 60 MW São Paulo campus as SPO05 begins operations and SPO06 construction advances.” 2026. https://ascenty.com/en/blog/news-ascenty-en/ascenty-sao-paulo-campus/.',
    annotation="Ascenty: SPO05 R$300m. Supports ascenty_spo05_300m_brl_2025.",
    evid_note="Opened Ascenty English campus page 2026-10-04; growth-revenue page corroborates R$300m SPO05 within USD 1bn 2026 LatAm CapEx envelope.",
)

# 3. engineering_epc / us — Ascenty SPO06 Greater São Paulo R$600m
row_doc(
    "ascenty_spo06_600m_brl_2026",
    "infrastructure",
    "engineering_epc",
    "us",
    "Ascenty (Digital Realty / Brookfield) — SPO06 data center (Greater São Paulo campus)",
    "Brazil",
    "Ascenty company English: SPO06 construction advancing on same Greater São Paulo campus as SPO05; estimated investment R$ 600 million; inauguration targeted May 2027; combined SPO05+SPO06 capacity 26 MW. BRL stored without FX. Distinct from ascenty_spo05_300m_brl_2025.",
    "600000000",
    "2026-01-01",
    "2026",
    "-23.50",
    "-46.60",
    "Ascenty SPO06, Greater São Paulo campus, Brazil (company geography; approximate metro pin).",
    "ascenty_spo05_spo06_campus",
    "SPO05 was announced in July 2025 and represents an investment of R$300 million. SPO06 is scheduled to be inaugurated in May 2027, with an estimated investment of R$600 million. Together, the two data centers will deliver a total capacity of 26 MW.",
    "https://ascenty.com/en/blog/news-ascenty-en/ascenty-sao-paulo-campus/",
    "Actor: Ascenty JV Digital Realty (U.S.) + Brookfield — us. Company English primary. CapEx = R$600m. Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle192",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Ascenty. “Ascenty expands 60 MW São Paulo campus as SPO05 begins operations and SPO06 construction advances.” 2026. https://ascenty.com/en/blog/news-ascenty-en/ascenty-sao-paulo-campus/.',
    annotation="Ascenty: SPO06 R$600m. Supports ascenty_spo06_600m_brl_2026.",
    evid_note="Opened Ascenty English campus page 2026-10-04 (same source_id as SPO05; distinct CapEx line).",
)

# 4. other_renewables / other — Novopan Ecuador biomass plant ~USD 16m
row_doc(
    "novopan_biomasa_16m_2025",
    "energy",
    "other_renewables",
    "other",
    "Novopan del Ecuador — industrial biomass thermal plant (Itulcachi / Pifo)",
    "Ecuador",
    "Jul 2025: Novopan inaugurates biomass plant generating up to ~30 MWh thermal for wood-drying at Itulcachi (Pifo, Quito); uses 4,000–5,000 t/month eucalyptus bark + urban wood residues; targets ~70% renewable energy matrix. Forbes Ecuador (23 Jul 2025) cites company comunicado: investment ~USD 16 million. Company Spanish page confirms COD/30 MWh without stating USD. UNVERIFIED proxy value. Distinct from Plantabal/3A balsa rows.",
    "16000000",
    "2025-07-23",
    "2025",
    "-0.23",
    "-78.33",
    "Novopan plant, Via La Troncal E-35, Itulcachi / Pifo, Quito, Ecuador (company contact geography; approximate pin).",
    "forbes_ec_novopan_biomasa_20250723",
    "Novopan puso en marcha su planta de biomasa. Se trata de un sistema capaz de generar hasta 30 MWh (megavatios), de energía térmica, según un comunicado. … La inversión bordea los US$ 16 millones.",
    "https://www.forbes.com.ec/innovacion/novopan-inauguro-su-planta-biomasa-invirtio-us-16-millones-n75731",
    "Actor: Novopan del Ecuador (Ecuadorian wood-panel) — other. UNVERIFIED proxy: Forbes Ecuador citing company comunicado for USD 16m; Novopan company page corroborates July 2025 COD / ~30 MWh without USD. CapEx = USD 16m. Shuffle other_renewables.",
    "hunt_cycle192",
    investment_type="brownfield_expansion",
    evidence="proxy",
    currency="USD",
    value_usd="16000000",
    fx_usd="1",
    bib_type="press",
    chicago='Forbes Ecuador. “Novopan inauguró su planta de biomasa; invirtió US$ 16 millones.” July 23, 2025. https://www.forbes.com.ec/innovacion/novopan-inauguro-su-planta-biomasa-invirtio-us-16-millones-n75731.',
    annotation="Forbes EC proxy: Novopan biomass ~USD 16m. Supports novopan_biomasa_16m_2025.",
    evid_note="Opened Forbes Ecuador 2026-10-04; cross-checked Novopan company Spanish biomass COD page (no USD on company page).",
)

# 5. other_renewables / allied — Aggreko LatAm 2026 CapEx USD 216m
row_doc(
    "aggreko_latam_capex_216m_2026",
    "energy",
    "other_renewables",
    "allied",
    "Aggreko — 2026 Latin America CapEx (hybrid solar+BESS / flexible power fleet)",
    "Brazil",
    "Canal Solar 4 Feb 2026 summarizing Aggreko LatAm CEO Pablo Varela: company announced USD 216 million CapEx for Latin America in 2026 (+249% vs 2025); pipeline includes Amazonas hybridization (88 MWp PV + 105 MWh BESS across 24 communities) under Pró-Amazônia Legal / CGPAL. Multi-country LatAm program (Brazil ~half per BNamericas interview); Brazil pin as primary market. UNVERIFIED proxy (trade press quoting CEO). Distinct from huawei_aggreko_amazonas_bess_2026 (Huawei BESS OEM supply).",
    "216000000",
    "2026-01-28",
    "2026",
    "",
    "",
    "Aggreko LatAm multi-country CapEx; Brazil primary share (trade press; multi-site — lat/lon blank).",
    "canalsolar_aggreko_216m_20260204",
    "As part of this strategy, Aggreko announced a US$216 million capital investment for Latin America in 2026, a 249% increase compared to 2025. … In this project, 24 communities in the state of Amazonas will have their systems hybridized, with the planned installation of 88 MWp in photovoltaic solar generation and 105 MWh in battery energy storage systems (BESS).",
    "https://canalsolar.com.br/en/Aggreko-Millions-Latin-America-2026/",
    "Actor: Aggreko (UK) — allied. UNVERIFIED proxy: Canal Solar English quoting LatAm CEO. CapEx = USD 216m. Shuffle other_renewables.",
    "hunt_cycle192",
    investment_type="capex_plan",
    evidence="proxy",
    currency="USD",
    value_usd="216000000",
    fx_usd="1",
    bib_type="press",
    chicago='Guerra, Raphael. “Aggreko announces a US$216 million investment in Latin America in 2026.” Canal Solar, February 4, 2026. https://canalsolar.com.br/en/Aggreko-Millions-Latin-America-2026/.',
    annotation="Canal Solar proxy: Aggreko LatAm CapEx USD 216m. Supports aggreko_latam_capex_216m_2026.",
    evid_note="Opened Canal Solar English 2026-10-04 quoting Aggreko LatAm CEO; BNamericas 28 Jan 2026 corroborates figure (paywalled).",
)

# 6. rail / allied — COMSA / RECSA / VISE QI Tramo III stations MXN 3,411.8m
row_doc(
    "comsa_qi_tramo3_3411p8m_mxn_2026",
    "infrastructure",
    "rail",
    "allied",
    "COMSA / RECSA / VISE — Querétaro–Irapuato Tramo III stations + 1.2 km",
    "Mexico",
    "15–16 Feb 2026 El Economista: consortium COMSA + COMSA Infraestructuras + RECSA + VISE awarded ATTRAPI contract MXN 3,411.8 million for design/build of 1.2 km Tramo III (km 107+000–108+200) plus five stations (Apaseo el Grande, Celaya, Cortázar, Salamanca, Irapuato) and Irapuato yard reconfiguration; 879 calendar-day execution; works start ~20 Feb 2026. COMSA company 27 Mar 2026 corroborates award (no MXN on company page). MXN stored without FX. Distinct from Mota-Engil QI Tramo I/II and Siemens/Sonda ETCS / CCECC–Aldesa QI auxiliaries.",
    "3411800000",
    "2026-02-15",
    "2026",
    "20.52",
    "-100.81",
    "Celaya / Bajío stations corridor, Guanajuato, Mexico (El Economista station list; approximate Celaya pin).",
    "eleconomista_comsa_qi_t3_20260215",
    "El consorcio integrado por COMSA, COMSA Infraestructuras, Regiomontana de Construcción y Servicios (Recsa) y Vise ganó … el contrato que se firmará con la Agencia de Trenes y Transporte Público Integrado (ATTRAPI) es por un monto de 3,411.8 millones de pesos … Las estaciones … Apaseo El Grande, Celaya, Cortázar, Salamanca e Irapuato",
    "https://www.eleconomista.com.mx/empresas/consorcio-comsa-gana-tramo-3-tren-queretaro-irapuato-20260215-800027.html",
    "Actor: COMSA Corporación (Spain) lead with RECSA/VISE (Mexico) — allied. Spanish business press; company award page corroborates without MXN. CapEx = MXN 3,411.8m. Shuffle rail.",
    "hunt_cycle192",
    investment_type="rail_epc",
    evidence="documented",
    currency="MXN",
    value_usd="",
    fx_usd="",
    bib_type="press",
    chicago='El Economista. “Consorcio de COMSA gana tramo 3 del tren Querétaro-Irapuato.” February 15, 2026. https://www.eleconomista.com.mx/empresas/consorcio-comsa-gana-tramo-3-tren-queretaro-irapuato-20260215-800027.html.',
    annotation="El Economista: COMSA QI Tramo III MXN 3,411.8m. Supports comsa_qi_tramo3_3411p8m_mxn_2026.",
    evid_note="Opened El Economista Spanish 2026-10-04; COMSA company 27 Mar 2026 award page cross-checked (no MXN on company page).",
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
    added = []

    for row, evid, bib_e in ITEMS:
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
            json.dumps(evid, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_e)

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print(f"cycle192 added {len(added)}: {added}")


if __name__ == "__main__":
    main()
