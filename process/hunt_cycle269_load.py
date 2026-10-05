#!/usr/bin/env python3
"""Cycle 269 hunt: shuffle_seed=20261269; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261269).shuffle):
water, solar, niobium, copper, wind, lithium, port_ownership, rail,
building_materials, other_renewables, graphite, engineering_epc, nickel, balsa,
fission_smr, port_cranes, bridges_roads, power_plants_grid.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Scala FY2025 CapEx R$1.822783bn + NEW AES Andes
  Cristales RCA CapEx up to USD 710m (nested vs combined Pampas+Cristales).
PRC equal-budget: NEW CPFL Distribuição R$25.3bn within 2026–2030 plan.
Other: NEW MRS 1T26 CapEx R$753.6m + 2T26 R$643m; Aegea FY2025 CapEx R$7.304bn;
  Rumo Hortolândia viaduct R$57m + Malha Paulista spent >R$8bn.
Skipped: thin dry; holdovers unsigned; Equinix/Ascenty/Sabesp/Motiva dense.
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


# 1. engineering_epc / us — NEW Scala FY2025 CapEx R$1.822783bn
row_doc(
    "scala_fy2025_capex_1823m_brl",
    "infrastructure", "engineering_epc", "us",
    "Scala Data Centers (DigitalBridge) — FY2025 CapEx R$1.822783bn",
    "Brazil",
    "Scala Data Centers S.A. 2025 Demonstrações Financeiras (company PDF): investments executed in 2025 totaled R$1.822.783 thousand (R$1.822783 billion) vs R$4.301.539 thousand in 2024 — applied to data-center construction at Tamboré/SP, Fortaleza/CE, operating-site expansions, and Eldorado do Sul–RS land for Scala AI City; year-end 11 operating / 4 under construction. CapEx: enter R$1.822783bn FY2025 face. Nested vs scala_cumulative_12bn_brl_2025 envelope (not additive).",
    "1822783000", "2025-12-31", "2025", "-23.51", "-46.85",
    "Scala Brazil multi-campus (Tamboré/Barueri pin; Fortaleza/Eldorado do Sul also cited).",
    "scala_dfs_2025_fy_capex_1823m",
    "Os investimentos realizados em 2025 totalizaram R$1.822.783 versus um investimento de R$4.301.539 em 2024.",
    "https://scaladatacenters.com/wp-content/uploads/2026/04/2025-Demonstracoes-Financeiras.pdf",
    "Actor: Scala Data Centers (DigitalBridge-backed) — us. NEW FY2025 CapEx R$1.822783bn. Shuffle engineering_epc; ≥1/3 U.S. hunt. Holdover Scala FY2025 CapEx if sustainability R$4.7bn reconciles — this is company DFS CapEx face.",
    "hunt_cycle269", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1822783000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Scala Data Centers S.A. “Demonstrações Financeiras 2025.” March 26, 2026. https://scaladatacenters.com/wp-content/uploads/2026/04/2025-Demonstracoes-Financeiras.pdf.',
    annotation="Scala FY2025 CapEx R$1.822783bn via Fed H.10. Supports scala_fy2025_capex_1823m_brl.",
    evid_note="Opened Scala company DFS PDF; FY2025 investments R$1.822.783 thousand confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. other_renewables / us — NEW AES Andes Cristales RCA CapEx up to USD 710m
row_doc(
    "aes_andes_cristales_710m_rca_2024",
    "energy", "other_renewables", "us",
    "AES Andes — Cristales solar + BESS RCA CapEx up to USD 710m",
    "Chile",
    "27 Mar 2024 AES Chile/Andes: environmental approval for Cristales photovoltaic project (up to 340 MW PV) plus BESS (up to 542 MW for 5 hours); investment of up to US$ 710 million; includes Cristales S/E and 220 kV evacuation line; Antofagasta Region. CapEx: enter USD 710m RCA ceiling. Nested vs aes_andes_pampas_cristales_2025 combined >USD 1.1bn construction package (not additive).",
    "710000000", "2024-03-27", "2024", "-25.40", "-70.48",
    "Cristales / Antofagasta Region (AES Andes geography; approximate regional pin shared with Pampas corridor).",
    "aes_andes_cristales_rca_20240327",
    "The project involves an investment of up to US$ 710 million.",
    "https://www.aeschile.com/en/press-release/aes-andes-obtains-environmental-approval-its-cristales-project",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW nested Cristales RCA CapEx up to USD 710m. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle269", investment_type="greenfield_storage", evidence="documented", currency="USD",
    value_usd="710000000", fx_usd="1", bib_type="company",
    chicago='AES Andes. “AES Andes obtains environmental approval for its Cristales project.” March 27, 2024. https://www.aeschile.com/en/press-release/aes-andes-obtains-environmental-approval-its-cristales-project.',
    annotation="AES Andes Cristales RCA CapEx up to USD 710m. Supports aes_andes_cristales_710m_rca_2024.",
    evid_note="Opened AES Chile English RCA press; Cristales investment up to USD 710m confirmed.",
)

# 3. power_plants_grid / prc — NEW CPFL Distribuição R$25.3bn (2026–2030)
row_doc(
    "cpfl_dist_25p3bn_2026_2030",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia (State Grid–controlled) — 2026–2030 distribution CapEx R$25.3bn",
    "Brazil",
    "6 Mar 2026 CPFL Energia: Board approves 2026–2030 investment plan totaling R$ 31.1 billion, of which R$ 25.3 billion for Distribuição and R$ 4.5 billion for Transmissão. CapEx: enter R$25.3bn distribution breakout face. Nested vs cpfl_capex_plan_31p1bn_2026_2030 group envelope and cpfl_tx_2026_2030_4540m_brl TX face (not additive).",
    "25300000000", "2026-03-06", "2026", "-22.91", "-47.06",
    "CPFL Energia Brazil distribution footprint (Campinas / São Paulo pin; Paulista/Piratininga/Santa Cruz/RGE).",
    "cpfl_fy2025_results_20260306",
    "novo plano de investimentos para o período de 2026 a 2030, que totaliza R$ 31,1 bilhões, sendo R$ 25,3 bilhões para o segmento de Distribuição e R$ 4,5 bilhões para a Transmissão",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-ebitda-de-r-135-bilhoes-em-2025-e-investimento-recorde-de-r-61",
    "Actor: CPFL Energia (State Grid–controlled) — prc. NEW nested distribution CapEx R$25.3bn. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle269", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(25300000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia. “CPFL Energia registra EBITDA de R$ 13,5 bilhões em 2025 e investimento recorde de R$ 6,1 bilhões.” March 6, 2026. https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-ebitda-de-r-135-bilhoes-em-2025-e-investimento-recorde-de-r-61.',
    annotation="CPFL Distribuição R$25.3bn 2026–2030 via Fed H.10. Supports cpfl_dist_25p3bn_2026_2030; cpfl_capex_plan_31p1bn_2026_2030.",
    evid_note="Opened CPFL company Portuguese; R$25.3bn distribution breakout within R$31.1bn plan confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. rail / other — NEW MRS 1T26 CapEx R$753.6m
row_doc(
    "mrs_1t26_capex_753p6m_brl",
    "infrastructure", "rail", "other",
    "MRS Logística — 1T26 CapEx R$753.6m",
    "Brazil",
    "14 May 2026 MRS company Portuguese: 1T26 invested R$ 753.6 million in modernization and expansion of the rail network (+19.6% YoY); transported 46.3 Mt (+2.5%). CapEx: enter R$753.6m 1T26 face. Distinct from mrs_baixada_santista_2bn_brl_2026 cycle envelope and Wabtec MRS loco rows (not additive to 2T26).",
    "753600000", "2026-05-14", "2026", "-21.76", "-43.35",
    "MRS Logística MG–RJ–SP freight network (Juiz de Fora HQ / network pin).",
    "mrs_1t26_capex_20260514",
    "além de investir R$ 753,6 milhões em modernização e expansão da malha ferroviária",
    "https://www.mrs.com.br/noticia/mrs-investe-r7536-milhoes-e-transporta-463-milhoes-de-toneladas-no-1-trimestre-de-2026/",
    "Actor: MRS Logística (Brazilian freight railroad) — other. NEW 1T26 CapEx R$753.6m. Shuffle rail.",
    "hunt_cycle269", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(753600000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='MRS Logística. “MRS investe R$753,6 milhões e transporta 46,3 milhões de toneladas no 1° trimestre de 2026.” May 14, 2026. https://www.mrs.com.br/noticia/mrs-investe-r7536-milhoes-e-transporta-463-milhoes-de-toneladas-no-1-trimestre-de-2026/.',
    annotation="MRS 1T26 CapEx R$753.6m via Fed H.10. Supports mrs_1t26_capex_753p6m_brl.",
    evid_note="Opened MRS company Portuguese; 1T26 CapEx R$753.6m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. rail / other — NEW MRS 2T26 CapEx R$643m
row_doc(
    "mrs_2t26_capex_643m_brl",
    "infrastructure", "rail", "other",
    "MRS Logística — 2T26 CapEx R$643m",
    "Brazil",
    "13 Aug 2026 MRS company press PDF: 2T26 strategic investments totaled R$ 643 million directed to operational safety, rail-network modernization, capacity expansion, and concession-renewal commitments (−40.8% vs 2T25 elevated loco/wagon base). CapEx: enter R$643m 2T26 face. Distinct from mrs_1t26_capex_753p6m_brl (not additive).",
    "643000000", "2026-08-13", "2026", "-21.76", "-43.35",
    "MRS Logística MG–RJ–SP freight network (Juiz de Fora HQ / network pin).",
    "mrs_2t26_capex_20260813",
    "No 2T26, em linha com o plano estratégico ,os aportes somaram R$ 643 milhões, direcionados à manutenção da segurança operacional, modernização da malha ferroviária, expansão de capacidade e cumprimento dos compromissos da renovação da concessão.",
    "https://www.mrs.com.br/wp-content/uploads/2026/03/2026_08_MRS-Logistica-registra-EBITDA-de-R-11-bilhao-e-Receita-Liquida-de-R-19-bilhao-no-2T26.pdf",
    "Actor: MRS Logística — other. NEW 2T26 CapEx R$643m. Shuffle rail.",
    "hunt_cycle269", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(643000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='MRS Logística. “MRS Logística registra EBITDA de R$ 1,1 bilhão e Receita Líquida de R$ 1,9 bilhão no 2T26.” August 13, 2026. https://www.mrs.com.br/wp-content/uploads/2026/03/2026_08_MRS-Logistica-registra-EBITDA-de-R-11-bilhao-e-Receita-Liquida-de-R-19-bilhao-no-2T26.pdf.',
    annotation="MRS 2T26 CapEx R$643m via Fed H.10. Supports mrs_2t26_capex_643m_brl.",
    evid_note="Opened MRS company Portuguese PDF; 2T26 CapEx R$643m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 6. water / other — NEW Aegea FY2025 CapEx R$7.304bn
row_doc(
    "aegea_fy2025_capex_7304m_brl",
    "resources", "water", "other",
    "Aegea Saneamento — FY2025 CapEx R$7.304bn",
    "Brazil",
    "20 Apr 2026 Equipav Saneamento DFs (Aegea parent consolidation): Capex Proforma Ecossistema R$ 7.304 billion in 2025 (+35.0% vs R$5.409bn 2024); narrative states R$7.3bn Capex within R$8.6bn total investments (R$1.3bn outorgas). CapEx: enter R$7.304bn FY2025 face. Distinct from aegea_6m26_* / 2T26 ecosystem spent rows (not additive).",
    "7304000000", "2025-12-31", "2025", "-22.91", "-43.17",
    "Aegea sanitation ecosystem Brazil footprint (Rio de Janeiro metro pin).",
    "equipav_aegea_dfs_2025_capex_7304m",
    "CAPEX (R$ MM) 7.304 5.409 35,0%",
    "https://www.equipav.com.br/wp-content/uploads/2026/04/DFs-Equipav-Saneamento-Dez.25_vf.pdf",
    "Actor: Aegea Saneamento (Equipav-controlled) — other. NEW FY2025 CapEx R$7.304bn. Shuffle water.",
    "hunt_cycle269", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(7304000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equipav Saneamento S.A. “Demonstrações Financeiras — Resultados 2025.” April 20, 2026. https://www.equipav.com.br/wp-content/uploads/2026/04/DFs-Equipav-Saneamento-Dez.25_vf.pdf.',
    annotation="Aegea FY2025 CapEx R$7.304bn via Fed H.10. Supports aegea_fy2025_capex_7304m_brl.",
    evid_note="Opened Equipav/Aegea company DFS PDF; FY2025 Capex R$7.304bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 7. bridges_roads / other — NEW Rumo Hortolândia viaduct R$57m
row_doc(
    "rumo_hortolandia_viaduct_57m_brl_2026",
    "infrastructure", "bridges_roads", "other",
    "Rumo — Hortolândia rail-crossing viaduct CapEx R$57m",
    "Brazil",
    "13 Apr 2026 Rumo company Portuguese: delivered viaduct over the rail line in Hortolândia (SP) with investment of R$ 57 million, eliminating at-grade crossing; part of Malha Paulista early-renewal investment package. CapEx: enter R$57m project face. Nested vs rumo_malha_paulista_8bn_spent_brl envelope (not additive).",
    "57000000", "2026-04-13", "2026", "-22.86", "-47.22",
    "Hortolândia, São Paulo — Malha Paulista rail crossing (company geography).",
    "rumo_hortolandia_viaduct_20260413",
    "Com investimento de R$ 57 milhões, o novo viaduto elimina a passagem em nível sobre a linha férrea na região central do município",
    "https://www.rumolog.com/sala-de-imprensa/rumo-entrega-viaduto-em-hortolandia-sp-e-avanca-em-obras-da-renovacao-da-malha-paulista/",
    "Actor: Rumo Logística (Cosan) — other. NEW Hortolândia viaduct CapEx R$57m. Shuffle bridges_roads.",
    "hunt_cycle269", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(57000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo Logística. “Rumo entrega viaduto em Hortolândia (SP) e avança em obras da renovação da Malha Paulista.” April 13, 2026. https://www.rumolog.com/sala-de-imprensa/rumo-entrega-viaduto-em-hortolandia-sp-e-avanca-em-obras-da-renovacao-da-malha-paulista/.',
    annotation="Rumo Hortolândia viaduct R$57m via Fed H.10. Supports rumo_hortolandia_viaduct_57m_brl_2026.",
    evid_note="Opened Rumo company Portuguese; Hortolândia viaduct R$57m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 8. rail / other — NEW Rumo Malha Paulista spent >R$8bn
row_doc(
    "rumo_malha_paulista_8bn_spent_brl",
    "infrastructure", "rail", "other",
    "Rumo — Malha Paulista renewal CapEx spent >R$8bn",
    "Brazil",
    "13 Apr 2026 Rumo company Portuguese (Hortolândia viaduct delivery): structure integrates a package that has already invested more than R$ 8 billion in expanding rail capacity and reducing urban conflicts under the May 2020 Malha Paulista early-renewal contract; 110 interventions in 45 cities to date. CapEx: enter R$8bn soft floor of stated “mais de R$ 8 bilhões” spent. Envelope vs Hortolândia R$57m and 2026 CapEx plan rows (not additive).",
    "8000000000", "2026-04-13", "2026", "-23.55", "-46.63",
    "Rumo Malha Paulista concession (São Paulo state network pin).",
    "rumo_hortolandia_viaduct_20260413",
    "Estrutura integra pacote que já investiu mais de R$ 8 bilhões na ampliação da capacidade ferroviária e na redução de conflitos urbanos",
    "https://www.rumolog.com/sala-de-imprensa/rumo-entrega-viaduto-em-hortolandia-sp-e-avanca-em-obras-da-renovacao-da-malha-paulista/",
    "Actor: Rumo Logística — other. NEW Malha Paulista spent CapEx >R$8bn soft floor. Shuffle rail.",
    "hunt_cycle269", investment_type="concession_renewal", evidence="documented", currency="BRL",
    value_usd=str(round(8000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo Logística. “Rumo entrega viaduto em Hortolândia (SP) e avança em obras da renovação da Malha Paulista.” April 13, 2026. https://www.rumolog.com/sala-de-imprensa/rumo-entrega-viaduto-em-hortolandia-sp-e-avanca-em-obras-da-renovacao-da-malha-paulista/.',
    annotation="Rumo Malha Paulista >R$8bn spent via Fed H.10. Supports rumo_malha_paulista_8bn_spent_brl; rumo_hortolandia_viaduct_57m_brl_2026.",
    evid_note="Opened Rumo company Portuguese; Malha Paulista spent >R$8bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)


def upsert_bib(bib, bib_by, bib_e):
    sid = bib_e["id"]
    entry = {
        "id": sid,
        "type": bib_e.get("type", "company"),
        "chicago": bib_e["chicago"],
        "url": bib_e["url"],
        "annotation": bib_e.get("annotation", ""),
        "supports": bib_e.get("supports", []),
    }
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
    print(f"cycle269 added {len(added)}: {added}")
    print(f"cycle269 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
