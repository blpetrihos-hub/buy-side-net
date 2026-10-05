#!/usr/bin/env python3
"""Cycle 224 hunt: shuffle_seed=20261224; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261224).shuffle):
solar, niobium, other_renewables, graphite, port_cranes, lithium, power_plants_grid,
balsa, rail, fission_smr, engineering_epc, port_ownership, building_materials, copper,
nickel, wind, water, bridges_roads.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr —
    dry; next-thinnest graphite CapEx-fill (Graph+ Santa Maria do Salto >R$200m).
≥1/3 U.S. hunt budget spent on Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/Fluence/SSA/Atlas/Ascenty sweeps (US blank-USD residual exhausted;
0 US CapEx-fills this pass — honest residual).
PRC equal-budget: SPIC Luiz Gonzaga company US$70m dual + CEEC Coremas + Goldwind
Camaçari CapEx-fills; holdovers unsigned.
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
MXN_USD = "17.6932"
MXN_FX_DATE = "2026-09-25"
EUR_USD = "1.1400"  # Fed H.10 Sep 25 2026 USD per EUR


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


# 1. solar / prc — CapEx-fill SPIC Luiz Gonzaga company dual US$70m
row_doc(
    "spic_luiz_gonzaga_400m_brl_2024",
    "energy", "solar", "prc",
    "SPIC Brasil (70%) / Recurrent Energy — Luiz Gonzaga solar (Pernambuco)",
    "Brazil",
    "4–6 Nov 2024 SPIC Brasil: partnership with Recurrent Energy (Canadian Solar) investing approximately R$ 400 million (~USD 70 million company dual) in Luiz Gonzaga solar at Terra Nova, Pernambuco. CapEx-fill: enter company dual-quoted ~US$70m as value_usd (retain R$400m face).",
    "400000000", "2024-11-04", "2024", "-7.83", "-39.37",
    "Terra Nova, Pernambuco (company geography).",
    "spic_luiz_gonzaga_20241106",
    "A SPIC Brasil e Recurrent Energy (“Canadian Solar”) (NASDAQ: CSIQ) anunciaram nesta segunda-feira, 4 de novembro, uma nova parceria envolvendo o investimento de aproximadamente R$ 400 milhões (aprox. $70 milhões) no projeto solar Luiz Gonzaga, instalado em Terra Nova, Pernambuco.",
    "https://www.spicbrasil.com.br/destaque/investimento-complexo-solar-luiz-gonzaga/",
    "Actor: SPIC Brasil (PRC State Power Investment) — prc. CapEx-fill: company dual ~US$70m alongside R$400m. Shuffle solar / PRC equal-budget.",
    "hunt_cycle224", investment_type="ownership_equity", evidence="documented", currency="BRL",
    value_usd="70000000", fx_usd=str(round(400000000 / 70000000, 4)),
    chicago='SPIC Brasil. “Investimento Complexo Solar Luiz Gonzaga.” November 2024. https://www.spicbrasil.com.br/destaque/investimento-complexo-solar-luiz-gonzaga/.',
    annotation="SPIC Luiz Gonzaga CapEx-fill company dual ~US$70m. Supports spic_luiz_gonzaga_400m_brl_2024.",
    evid_note="Opened SPIC Brasil Portuguese; ~R$400m / ~US$70m dual / Terra Nova confirmed. CapEx-fill uses company USD.",
)

# 2. solar / prc — CapEx-fill CEEC Coremas ~R$520m EV
row_doc(
    "ceec_coremas_solar_520m_2025",
    "energy", "solar", "prc",
    "CEEC Brasil / China Energy — Coremas I–III PV acquisition",
    "Brazil",
    "4 Nov 2025: CEEC Brasil (China Energy Engineering Group) acquires Coremas I–III PV plants in Coremas, Paraíba for approximately R$ 520 million enterprise value. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~100.15m for stored R$520m face.",
    "520000000", BRL_FX_DATE, "2025", "-7.01", "-37.95",
    "Coremas, Paraíba (company geography).",
    "ceec_brasil_coremas_2025",
    "A CEEC Brasil, empresa do grupo China Energy, acaba de adquirir três usinas fotovoltaicas por um valor aproximado de R$ 520 milhões (enterprise value). O contrato de compra firmado em 4 de novembro com a FIP Coremas, controlada pela Nordic Power Partners.",
    "https://ceecbrasil.com.br/china-energy-adquire-usinas-fotovoltaicas-na-paraiba-e-marca-entrada-no-mercado-de-energias-renovaveis-no-brasil/",
    "Actor: CEEC Brasil / China Energy — prc. CapEx-fill: retain ~R$520m EV; add Fed H.10 Sep 25 2026 FX to USD ~100.15m. Shuffle solar / PRC equal-budget.",
    "hunt_cycle224", investment_type="mna_acquisition", evidence="documented", currency="BRL",
    value_usd=str(round(520000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='CEEC Brasil. “China Energy adquire usinas fotovoltaicas na Paraíba e marca entrada no mercado de energias renováveis no Brasil.” November 2025. https://ceecbrasil.com.br/china-energy-adquire-usinas-fotovoltaicas-na-paraiba-e-marca-entrada-no-mercado-de-energias-renovaveis-no-brasil/.',
    annotation="CEEC Coremas CapEx-fill ~USD 100.15m via Fed H.10. Supports ceec_coremas_solar_520m_2025.",
    evid_note="Opened CEEC Brasil Portuguese; ~R$520m EV / Coremas I–III confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 3. niobium / allied — CapEx-fill CBMM 2025 CapEx R$1.1bn
row_doc(
    "cbmm_araxa_2025_spend_1p1bn",
    "resources", "niobium", "allied",
    "CBMM — 2025 Araxá CapEx",
    "Brazil",
    "CBMM company news: invested R$ 1.1 billion in Capex in 2025. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~211.86m for stored R$1.1bn face. Distinct from cbmm_araxa_capex_630m_2024 / 2026 spend rows.",
    "1100000000", BRL_FX_DATE, "2025", "-19.59", "-46.94",
    "CBMM Araxá, Minas Gerais (company geography).",
    "cbmm_crescimento_diversificacao_2025",
    "Em 2025, a CBMM investiu R$ 1,1 bilhão em Capex, reforçando seu compromisso com o crescimento sustentável e competitividade de longo prazo.",
    "https://cbmm.com/pt/midias/noticias/cbmm-crescimento-diversificacao-niobio",
    "Actor: CBMM (Brazilian Moreira Salles–controlled) — allied. CapEx-fill: retain R$1.1bn 2025 CapEx; add Fed H.10 Sep 25 2026 FX to USD ~211.86m. Shuffle niobium.",
    "hunt_cycle224", investment_type="capex_spend", evidence="documented", currency="BRL",
    value_usd=str(round(1100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='CBMM. “CBMM: crescimento e diversificação do nióbio.” 2026. https://cbmm.com/pt/midias/noticias/cbmm-crescimento-diversificacao-niobio.',
    annotation="CBMM 2025 CapEx-fill ~USD 211.86m via Fed H.10. Supports cbmm_araxa_2025_spend_1p1bn.",
    evid_note="Opened CBMM Portuguese; R$1.1bn 2025 CapEx confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. rail / allied — CapEx-fill OHLA Santiago Metro L9 EUR 144.3m
row_doc(
    "ohla_metro_santiago_l9_2026",
    "infrastructure", "rail", "allied",
    "OHLA — Santiago Metro Line 9 Sections 1C/1D shafts, galleries, tunnels",
    "Chile",
    "27 Jul 2026: OHLA selected for civil works on shafts, galleries and tunnels for Sections 1C and 1D of future Santiago Metro Line 9 (Tramo 1); valued at €144.3 million; ~7.6 km underground. CapEx-fill: Fed H.10 Sep 25 2026 USD/EUR 1.1400 → USD ~164.50m for stored EUR 144.3m face.",
    "144300000", "2026-09-25", "2026", "-33.45", "-70.67",
    "Santiago Metro Line 9 Tramo 1 Sections 1C/1D, Chile (company geography; metro corridor pin).",
    "ohla_metro_l9_20260727",
    "OHLA … has been selected to carry out the civil works for shafts, galleries and tunnels in Sections 1C and 1D of the future Santiago Metro Line 9 in Chile. Valued at €144.3 million …",
    "https://www.ohla-group.com/en/ohla-secures-its-largest-ever-contract-for-the-santiago-metro-and-surpasses-e700-million-in-projects-across-the-network/",
    "Actor: OHLA (Spain) — allied. CapEx-fill: retain EUR 144.3m; add Fed H.10 Sep 25 2026 FX to USD ~164.50m. Shuffle rail.",
    "hunt_cycle224", investment_type="epc", evidence="documented", currency="EUR",
    value_usd=str(round(144300000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='OHLA. “OHLA secures its largest-ever contract for the Santiago Metro and surpasses €700 million in projects across the network.” July 27, 2026. https://www.ohla-group.com/en/ohla-secures-its-largest-ever-contract-for-the-santiago-metro-and-surpasses-e700-million-in-projects-across-the-network/.',
    annotation="OHLA Metro L9 CapEx-fill ~USD 164.50m via Fed H.10. Supports ohla_metro_santiago_l9_2026.",
    evid_note="Opened OHLA English; EUR 144.3m / Sections 1C–1D / 7.6 km confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 1.1400 USD/EUR.",
)

# 5. port_cranes / allied — CapEx-fill TIMSA e-RTG >MXN 70m
row_doc(
    "timsa_ertg_manzanillo_70m_mxn_2026",
    "infrastructure", "port_cranes", "allied",
    "Hutchison Ports TIMSA — two e-RTG electric yard cranes (Manzanillo)",
    "Mexico",
    "1 Jul 2026 T21 / Hutchison Ports TIMSA: investment exceeding MXN 70 million for two new electric Rubber Tyred Gantry (e-RTG) cranes; arrived 29 Jun on Xiang He Kou from China. CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~3.96m for stored MXN 70m floor face.",
    "70000000", MXN_FX_DATE, "2026", "19.06", "-104.32",
    "Hutchison Ports TIMSA, Manzanillo, Colima (press geography).",
    "t21_timsa_ertg_manzanillo_20260701",
    "Hutchison Ports TIMSA anunció una inversión superior a 70 millones de pesos para incorporar dos nuevas grúas eléctricas tipo Rubber Tyred Gantry Crane (e-RTG) … arribaron al puerto el pasado 29 de junio a bordo del buque Xiang He Kou, procedente de China",
    "https://t21.com.mx/hutchison-ports-timsa-suma-dos-nuevas-gruas-electricas-en-manzanillo/",
    "Actor: Hutchison Ports TIMSA (catalog side allied for this e-RTG row). CapEx-fill: retain >MXN 70m floor; add Fed H.10 Sep 25 2026 FX to USD ~3.96m. Shuffle port_cranes.",
    "hunt_cycle224", investment_type="equipment", evidence="documented", currency="MXN",
    value_usd=str(round(70000000 / float(MXN_USD), 2)), fx_usd=MXN_USD, bib_type="press",
    chicago='T21. “Hutchison Ports TIMSA suma dos nuevas grúas eléctricas en Manzanillo.” July 1, 2026. https://t21.com.mx/hutchison-ports-timsa-suma-dos-nuevas-gruas-electricas-en-manzanillo/.',
    annotation="TIMSA e-RTG CapEx-fill ~USD 3.96m via Fed H.10. Supports timsa_ertg_manzanillo_70m_mxn_2026.",
    evid_note="Opened T21 Spanish; >MXN 70m / two e-RTG / Xiang He Kou confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 6. power_plants_grid / allied — CapEx-fill ENGIE Brasil FY2025 R$6bn
row_doc(
    "engie_brasil_fy2025_capex_6bn_brl",
    "energy", "power_plants_grid", "allied",
    "ENGIE Brasil Energia — FY2025 CapEx (hydro acquisitions + modernization + projects)",
    "Brazil",
    "25 Feb 2026 ENGIE Brasil Energia: invested R$ 6 billion in 2025 in acquisition of new hydropower assets, modernization, project implementation and generator park revitalization. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~1155.60m for stored R$6bn face.",
    "6000000000", BRL_FX_DATE, "2025", "", "",
    "ENGIE Brasil Energia multi-asset CapEx (national footprint; no single-site pin).",
    "engie_brasil_fy2025_results_20260225",
    "During the year, the Company invested R$ 6 billion in the acquisition of new hydropower assets, in modernization work, the implementation of projects and generator park revitalization.",
    "https://www.engie.com.br/en/imprensa/press-releases/engie-brasil-energia-grows-14-6-in-revenue-and-invests-r-6-billion-in-2025/",
    "Actor: ENGIE Brasil Energia (France ENGIE) — allied. CapEx-fill: retain R$6bn FY2025; add Fed H.10 Sep 25 2026 FX to USD ~1155.60m. Shuffle power_plants_grid.",
    "hunt_cycle224", investment_type="capex_spend", evidence="documented", currency="BRL",
    value_usd=str(round(6000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='ENGIE Brasil Energia. “ENGIE Brasil Energia grows 14.6% in revenue and invests R$ 6 billion in 2025.” February 25, 2026. https://www.engie.com.br/en/imprensa/press-releases/engie-brasil-energia-grows-14-6-in-revenue-and-invests-r-6-billion-in-2025/.',
    annotation="ENGIE Brasil FY2025 CapEx-fill ~USD 1155.60m via Fed H.10. Supports engie_brasil_fy2025_capex_6bn_brl.",
    evid_note="Opened ENGIE Brasil English; R$6bn 2025 CapEx confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 7. graphite / other — CapEx-fill Graph+ >R$200m (thin next-thinnest)
row_doc(
    "graph_plus_santa_maria_salto_2024",
    "resources", "graphite", "other",
    "Graph+ (New Mining) — Santa Maria do Salto graphite extraction plant (Vale do Jequitinhonha)",
    "Brazil",
    "InvestMinas Exposibram 2024: Graph+ (New Mining subsidiary) announces >R$200 million private investment through 2028 for graphite extraction plant at Santa Maria do Salto (MG). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~38.52m for stored R$200m floor face (UNVERIFIED proxy CapEx retained).",
    "200000000", BRL_FX_DATE, "2024", "-16.32", "-40.15",
    "Santa Maria do Salto, Minas Gerais (InvestMinas geography).",
    "invest_minas_graph_plus_20241003",
    "aporte de mais de R$ 200 milhões, a ser feito até 2028, pela Graph+. A planta da empresa, subsidiária da New Mining, será voltada para a extração de grafite no município de Santa Maria do Salto",
    "https://investminas.mg.gov.br/2024/10/03/governo-anuncia-investimento-privado-superior-a-r-200-milhoes-na-exposibram-2024/",
    "Actor: Graph+ / New Mining (Brazil) — other. CapEx-fill: retain >R$200m floor UNVERIFIED proxy; add Fed H.10 Sep 25 2026 FX to USD ~38.52m. Thin next-thinnest graphite (balsa/nickel/fission_smr dry).",
    "hunt_cycle224", investment_type="greenfield_plant", evidence="proxy", currency="BRL",
    value_usd=str(round(200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="government",
    chicago='InvestMinas. “Governo anuncia investimento privado superior a R$ 200 milhões na Exposibram 2024.” October 3, 2024. https://investminas.mg.gov.br/2024/10/03/governo-anuncia-investimento-privado-superior-a-r-200-milhoes-na-exposibram-2024/.',
    annotation="Graph+ CapEx-fill ~USD 38.52m via Fed H.10. Supports graph_plus_santa_maria_salto_2024.",
    evid_note="Opened InvestMinas Portuguese; >R$200m / Santa Maria do Salto confirmed (UNVERIFIED proxy). CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
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
    print(f"cycle224 added {len(added)}: {added}")
    print(f"cycle224 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
