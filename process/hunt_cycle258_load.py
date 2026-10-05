#!/usr/bin/env python3
"""Cycle 258 hunt: shuffle_seed=20261258; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261258).shuffle):
lithium, copper, other_renewables, graphite, port_cranes, niobium, building_materials,
engineering_epc, wind, rail, port_ownership, bridges_roads, nickel, water, solar, balsa,
fission_smr, power_plants_grid.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: spent (Scala BNDES C257; Equinix/Ascenty/AES Andes CapEx dense;
  Equinix SP cabinets USD109m without openable company filing primary this pass) — residual.
PRC equal-budget: honest residual (CPFL/State Grid/BYD BESS without company CapEx primary).
Allied: NEW ISA group 2Q26 CapEx COP 1.7tn; NEW ISA 1H26 CapEx COP 3.1tn;
  NEW ISA Vías Río Bueno–Puerto Montt projected CapEx USD 821m.
Other: NEW Copel 2026–2030 CapEx plan R$17.8bn; NEW Copasa 1S26 CapEx R$1,537.8m.
Skipped: thin dry; holdovers unsigned; Alupar TECP/Lot 7 without openable company PDF;
  Ada Franco da Rocha without company CapEx primary; Copel 1S26 nested under 2T26.
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


# 1. power_plants_grid / allied — NEW ISA group 2Q26 CapEx COP 1.7 trillion
row_doc(
    "isa_2q26_capex_1p7tn_cop",
    "energy", "power_plants_grid", "allied",
    "ISA — 2Q26 group CapEx COP 1.7tn",
    "Colombia",
    "3 Aug 2026 ISA Q2 2026 Financial Results (English): ISA made investments totaling COP 1.7 trillion in 2Q26 (+23% vs 2Q25); 73% Energy / 25% Roads / 2% Telecom. CapEx face = COP 1.7tn group executed investments (USD blank — no Fed H.10 COP). Nested vs isa_fy2025_invest_6p3tn_cop / isa_capex_plan_25p5tn_2026_2030 (not additive).",
    "1700000000000", "2026-06-30", "2026", "6.25", "-75.57",
    "ISA group LatAm footprint (Medellín HQ pin; multi-country Energy/Roads/Telecom).",
    "isa_q2_2026_financial_results",
    "ISA made investments totaling COP 1.7 trillion in the second quarter of 2026, a 23% increase over the investments made during the same period in 2025. … During 2Q26, ISA made investments totaling COP 1.7 trillion, 23% more than in the same period of 2025. … 73% of the quarter's investments were made in the Energy segment, 25% in Roads, and 2% in Telecommunications.",
    "https://www.otcmarkets.com/file/company/financial-report/591730/content",
    "Actor: ISA / Interconexión Eléctrica (Colombia; Ecopetrol group) — allied. NEW nested 2Q26 CapEx COP 1.7tn. Company English Q2 report (OTC-hosted full text; landing also at isa.co/en/informacion/isa-q2-2026-financial-results/). USD blank (no Fed H.10 COP). Shuffle power_plants_grid.",
    "hunt_cycle258", investment_type="corporate_capex", evidence="documented", currency="COP",
    value_usd="", fx_usd="", bib_type="company",
    chicago='Interconexión Eléctrica S.A. E.S.P. (ISA). “ISA Reports Strong Q2 2026 Results” / Second Quarter of 2026 Financial Results. August 3, 2026. https://www.otcmarkets.com/file/company/financial-report/591730/content (company landing: https://isa.co/en/informacion/isa-q2-2026-financial-results/).',
    annotation="ISA 2Q26 NEW COP 1.7tn (USD blank). Supports isa_2q26_capex_1p7tn_cop; isa_1h26_capex_3p1tn_cop; isa_vias_rio_bueno_puerto_montt_821m_2026.",
    evid_note="Opened ISA Q2 2026 English financial results (OTC-hosted company report dated Medellín Aug 3 2026); COP 1.7tn 2Q26 / +23% / 73% Energy confirmed.",
)

# 2. power_plants_grid / allied — NEW ISA group 1H26 CapEx COP 3.1 trillion
row_doc(
    "isa_1h26_capex_3p1tn_cop",
    "energy", "power_plants_grid", "allied",
    "ISA — 1H26 group CapEx COP 3.1tn",
    "Colombia",
    "3 Aug 2026 ISA Q2 2026 Financial Results (English): as of June 2026 cumulative investments totaled COP 3.1 trillion (+16% vs 1H25); management also states group invested COP 3.1tn in first half. CapEx face = COP 3.1tn. Nested vs isa_2q26_capex_1p7tn_cop / FY2025 / 25.5tn plan (not additive). USD blank (no Fed H.10 COP).",
    "3100000000000", "2026-06-30", "2026", "6.25", "-75.57",
    "ISA group LatAm footprint (Medellín HQ pin).",
    "isa_q2_2026_financial_results",
    "As of June 2026, cumulative investments totaled COP 3.1 trillion, representing a 16% increase compared to the first six months of 2025. … We also invested COP 3.1 trillion during the period, up 16% from the same period in 2025 … With the investments made during the quarter, ISA's total capex for 2026 reached COP 3.1 trillion, representing a 16% increase compared to the first half of 2025.",
    "https://www.otcmarkets.com/file/company/financial-report/591730/content",
    "Actor: ISA / Interconexión Eléctrica (Colombia; Ecopetrol group) — allied. NEW nested 1H26 CapEx COP 3.1tn. USD blank (no Fed H.10 COP). Shuffle power_plants_grid.",
    "hunt_cycle258", investment_type="corporate_capex", evidence="documented", currency="COP",
    value_usd="", fx_usd="", bib_type="company",
    chicago='Interconexión Eléctrica S.A. E.S.P. (ISA). “ISA Reports Strong Q2 2026 Results” / Second Quarter of 2026 Financial Results. August 3, 2026. https://www.otcmarkets.com/file/company/financial-report/591730/content (company landing: https://isa.co/en/informacion/isa-q2-2026-financial-results/).',
    annotation="ISA 2Q26/1H26 CapEx and Río Bueno USD 821m via company English report. Supports isa_2q26_capex_1p7tn_cop; isa_1h26_capex_3p1tn_cop; isa_vias_rio_bueno_puerto_montt_821m_2026.",
    evid_note="Opened ISA Q2 2026 English financial results; COP 3.1tn 1H26 / +16% confirmed.",
)

# 3. bridges_roads / allied — NEW ISA Vías Río Bueno–Puerto Montt USD 821m
row_doc(
    "isa_vias_rio_bueno_puerto_montt_821m_2026",
    "infrastructure", "bridges_roads", "allied",
    "ISA Vías — Río Bueno–Puerto Montt (Ruta de los Lagos) projected CapEx USD 821m",
    "Chile",
    "3 Aug 2026 ISA Q2 2026 Financial Results (English): Chile MOP supreme decree awards ISA Vías the Río Bueno–Puerto Montt (Ruta de los Lagos) concession — modernization of 129 km highway in southern Chile; projected CapEx USD 821 million (~COP 3tn); ISA Vías took over July 2026; construction phase scheduled to begin 2031. CapEx: enter USD 821m projected face.",
    "821000000", "2026-08-03", "2026", "-40.33", "-72.96",
    "Río Bueno–Puerto Montt / Ruta de los Lagos corridor (Los Lagos Region pin).",
    "isa_q2_2026_financial_results",
    "Chile’s Ministry of Public Works (MOP) issued the supreme decree awarding ISA VÍAS the Río Bueno–Puerto Montt (Ruta de los Lagos) concession, a project that involves the modernization of 129 km of highway in southern Chile. This project has a projected capex of USD 821 million (~COP 3 trillion). As this is the concession of an existing highway, ISA VÍAS took over the project in July 2026, with the construction phase scheduled to begin in 2031.",
    "https://www.otcmarkets.com/file/company/financial-report/591730/content",
    "Actor: ISA Vías (ISA Colombia–controlled) — allied. NEW projected CapEx USD 821m Chile road concession. Shuffle bridges_roads.",
    "hunt_cycle258", investment_type="concession_capex", evidence="documented", currency="USD",
    value_usd="821000000", fx_usd="1", bib_type="company",
    chicago='Interconexión Eléctrica S.A. E.S.P. (ISA). “ISA Reports Strong Q2 2026 Results” / Second Quarter of 2026 Financial Results. August 3, 2026. https://www.otcmarkets.com/file/company/financial-report/591730/content (company landing: https://isa.co/en/informacion/isa-q2-2026-financial-results/).',
    annotation="ISA 2Q26/1H26 CapEx and Río Bueno USD 821m via company English report. Supports isa_2q26_capex_1p7tn_cop; isa_1h26_capex_3p1tn_cop; isa_vias_rio_bueno_puerto_montt_821m_2026.",
    evid_note="Opened ISA Q2 2026 English financial results; Río Bueno–Puerto Montt USD 821m / 129 km / construction from 2031 confirmed.",
)

# 4. power_plants_grid / other — NEW Copel 2026–2030 CapEx plan R$17.8bn
row_doc(
    "copel_2026_2030_capex_17p8bn_brl",
    "energy", "power_plants_grid", "other",
    "Copel — 2026–2030 CapEx plan R$17.8bn",
    "Brazil",
    "17 Sep 2026 Copel company news: between 2026 and 2030 the company projects investing R$17.8 billion in generation, transmission and distribution — one of its most robust investment programs; of which R$13.4 billion for distribution. Distinct from copel_capex_2026_plan_3021m_brl single-year and copel_2t26_capex_957p2m_brl nested quarterly. CapEx: enter R$17.8bn face.",
    "17800000000", "2026-09-17", "2026", "-25.43", "-49.27",
    "Copel Paraná generation/transmission/distribution footprint (Curitiba HQ pin).",
    "copel_news_17p8bn_20260917",
    "Os investimentos previstos para 2026 marcam o início de um novo ciclo de expansão da infraestrutura elétrica da Copel. Entre 2026 e 2030, a companhia projeta investir R$ 17,8 bilhões em geração, transmissão e distribuição de energia, em um dos mais robustos programas de investimentos de sua história. Desse total, R$ 13,4 bilhões serão destinados à distribuição de energia.",
    "https://www.copel.com/site/noticias/copel-investe-r-3-bilhoes-em-obras-de-geracao-transmissao-e-distribuicao-de-energia-em-todo-o-parana/",
    "Actor: Copel (Paraná utility) — other. NEW 2026–2030 CapEx plan R$17.8bn company Portuguese news. Shuffle power_plants_grid.",
    "hunt_cycle258", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(17800000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia Paranaense de Energia (Copel). “Copel investe R$ 3 bilhões em obras de geração, transmissão e distribuição de energia em todo o Paraná.” September 17, 2026. https://www.copel.com/site/noticias/copel-investe-r-3-bilhoes-em-obras-de-geracao-transmissao-e-distribuicao-de-energia-em-todo-o-parana/.',
    annotation="Copel 2026–2030 NEW R$17.8bn ~USD 3428.29m via Fed H.10. Supports copel_2026_2030_capex_17p8bn_brl.",
    evid_note="Opened Copel company Portuguese news; R$17.8bn 2026–2030 / R$13.4bn distribution confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. water / other — NEW Copasa 1S26 CapEx R$1,537.8m
row_doc(
    "copasa_1s26_capex_1537p8m_brl",
    "resources", "water", "other",
    "COPASA MG — 1S26 CapEx R$1,537.8m",
    "Brazil",
    "12 Aug 2026 COPASA MG 2T26 earnings release (company release via investidor10 republisher / company news): consolidated investments Jan–Jun 2026 totaled R$1,537.8 million (+27% vs 1S25); controller R$1,515.0m including capitalizations (water R$780.5m; sewage R$416.7m). CapEx: enter consolidated R$1,537.8m 1S26 face. Distinct from Sabesp/Aegea water CapEx rows.",
    "1537800000", "2026-06-30", "2026", "-19.92", "-43.94",
    "COPASA Minas Gerais water/sewage footprint (Belo Horizonte HQ pin).",
    "copasa_2t26_release_20260812",
    "Conforme tabela a seguir, os valores investidos no período de janeiro a junho de 2026 (1S26), incluindo as capitalizações, totalizaram R$1,54 bilhão, 27% superior ao valor investido no mesmo período de 2025: … Total – Consolidado 1.537,8 … Capex no 1S26: R$1,5 bilhão (+27%)",
    "https://investidor10.com.br/acoes/link_comunicado/CSMG3/47519/",
    "Actor: COPASA MG (Minas Gerais state sanitation utility) — other. NEW nested 1S26 CapEx R$1,537.8m. Company release opened via investidor10 republisher (company news.copasa.com.br CapEx R$1.5bn contemporaneous). Shuffle water.",
    "hunt_cycle258", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1537800000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia de Saneamento de Minas Gerais (COPASA MG). “Release de Resultados 2T26.” August 12, 2026. https://investidor10.com.br/acoes/link_comunicado/CSMG3/47519/.',
    annotation="COPASA 1S26 NEW R$1,537.8m ~USD 296.18m via Fed H.10. Supports copasa_1s26_capex_1537p8m_brl.",
    evid_note="Opened COPASA 2T26 release text (investidor10 republisher of company IPE); consolidated CapEx 1S26 R$1,537.8m / +27% / water-sewage breakouts confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle258 added {len(added)}: {added}")
    print(f"cycle258 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
