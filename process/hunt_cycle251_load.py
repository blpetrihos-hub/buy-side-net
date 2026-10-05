#!/usr/bin/env python3
"""Cycle 251 hunt: shuffle_seed=20261251; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261251).shuffle):
solar, bridges_roads, graphite, building_materials, water, fission_smr,
port_ownership, lithium, copper, engineering_epc, nickel, niobium, rail,
port_cranes, wind, balsa, other_renewables, power_plants_grid.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Atlas Draco BRL ~1bn BNDES construction financing (GIP/US);
  NEW ODATA/Aligned DeltaFlow first-phase USD 630m (SP04 Brazil + QR03 Mexico).
PRC equal-budget: NEW CPFL Energia 1H26 CapEx R$2.8bn (State Grid–controlled; nested
  vs 31.1bn plan / FY2025 R$6.1bn).
Other: NEW TAESA four greenfield ANEEL R$4.3bn; NEW TAESA FY2025 CapEx R$1,782.8m;
  NEW Alupar growth-cycle R$8.1bn; NEW KIO LatAm cumulative >USD 900m (Mexican;
  I Squared shareholder).
Skipped: Meitner ACR-300 already logged; Wabtec MRS 254m already logged; Equinix
  419m already logged; thin balsa/nickel/fission dry; GATE R$20bn without State Grid
  company primary vs R$18bn; Progress Rail R$430m conflict with R$200m eight-loco;
  Alupar R$10bn press without openable 2T26 PDF (use sustainability R$8.1bn instead).
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


# 1. solar / us — NEW Atlas Draco BNDES ~R$1bn construction financing
row_doc(
    "atlas_draco_bndes_1bn_brl_2025",
    "energy", "solar", "us",
    "Atlas Renewable Energy (GIP) — Draco Solar Complex BNDES construction financing",
    "Brazil",
    "28 Jul 2025 Atlas Renewable Energy: with BNDES approved an approximately BRL 1 billion (about US$179 million) financing package for construction of the Draco Solar Complex in Minas Gerais — 11 PV plants totaling 505 MWac (579 MWdc), plus 500 kV substation and 15 km single-circuit transmission to SIN; COD early 2026. CapEx/financing: enter R$1bn face. Distinct from atlas_luiz_carlos / atlas_latam_3bn_refi envelopes.",
    "1000000000", "2025-07-28", "2025", "-18.51", "-44.56",
    "Draco Solar Complex, Minas Gerais (state-level pin; multi-plant campus).",
    "atlas_draco_bndes_1bn_20250728",
    "Atlas Renewable Energy and Brazil’s National Bank for Economic and Social Development (BNDES) approved an approximately BRL 1 billion (about US$179 million) financing package for the construction of the Draco Solar Complex in Minas Gerais, Brazil.",
    "https://atlasrenewableenergy.com/news-and-insights/bndes-approves-brl-1b-financing-for-atlas-renewable-energys-11-solar-plants-in-brazil-powering-data-centers/",
    "Actor: Atlas Renewable Energy (GIP / U.S. HQ Miami) — us. NEW row: company English BRL ~1bn Draco construction financing. Shuffle solar / U.S. ≥1/3 budget.",
    "hunt_cycle251", investment_type="financing", evidence="documented", currency="BRL",
    value_usd=str(round(1000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Atlas Renewable Energy. “BNDES Approves BRL 1B Financing for Atlas Renewable Energy’s 11 Solar Plants in Brazil Powering Data Centers.” July 28, 2025. https://atlasrenewableenergy.com/news-and-insights/bndes-approves-brl-1b-financing-for-atlas-renewable-energys-11-solar-plants-in-brazil-powering-data-centers/.',
    annotation="Atlas Draco NEW R$1bn ~USD 192.60m via Fed H.10. Supports atlas_draco_bndes_1bn_brl_2025.",
    evid_note="Opened Atlas English press; BRL ~1bn BNDES / 505 MWac Draco / MG / COD early 2026 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. engineering_epc / us — NEW ODATA DeltaFlow first-phase USD 630m
row_doc(
    "odata_deltaflow_630m_2026",
    "infrastructure", "engineering_epc", "us",
    "ODATA (Aligned Data Centers) — DeltaFlow liquid-cooling first-phase CapEx (SP04 + QR03)",
    "Brazil",
    "17 Sep 2026 ODATA / Aligned Data Centers: deploying DeltaFlow liquid cooling at SP04 (Brazil) and QR03 (Mexico) flagship campuses; supported by a combined USD 630 million first-phase investment; phase-one installation and testing underway. CapEx: enter USD 630m face. Distinct from odata_aligned_green_financing_1p02bn_2025 financing envelope and SP04 >USD 450m campus announcement.",
    "630000000", "2026-09-17", "2026", "-23.53", "-46.79",
    "ODATA SP04 Osasco (Brazil) + QR03 Querétaro (Mexico); multi-site — São Paulo metro pin.",
    "odata_deltaflow_630m_20260917",
    "Supported by a combined $630 million investment, phase one installation and testing are already underway at both facilities.",
    "https://aligneddc.com/press-release/odata-brings-next-generation-cooling-to-latin-america-with-deltaflow-liquid-cooling-technology/",
    "Actor: ODATA / Aligned Data Centers (U.S. parent) — us. NEW row: company English USD 630m first-phase CapEx SP04+QR03. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle251", investment_type="corporate_capex", evidence="documented", currency="USD",
    chicago='ODATA / Aligned Data Centers. “ODATA Brings Next-Generation Cooling to Latin America with DeltaFlow~™ Liquid Cooling Technology.” September 17, 2026. https://aligneddc.com/press-release/odata-brings-next-generation-cooling-to-latin-america-with-deltaflow-liquid-cooling-technology/.',
    annotation="ODATA DeltaFlow NEW USD 630m. Supports odata_deltaflow_630m_2026.",
    evid_note="Opened Aligned/ODATA English press; USD 630m first-phase / SP04 Brazil + QR03 Mexico / DeltaFlow confirmed.",
)

# 3. engineering_epc / other — NEW KIO LatAm cumulative >USD 900m
row_doc(
    "kio_cumulative_900m_latam_2026",
    "infrastructure", "engineering_epc", "other",
    "KIO Data Centers — cumulative LatAm digital-infrastructure CapEx >USD 900m (since 2022)",
    "Mexico",
    "13 Aug 2026 KIO Data Centers company English: since I Squared Capital became a shareholder in 2022, KIO has invested more than USD 900 million in Mexico and Latin America; also completed QRO2 phases 2–3 bringing that campus to USD 170 million and commits >USD 200 million in 2026 for new Mexico City / Monterrey / Querétaro projects; evaluating up to USD 1.3bn QRO3 through 2030. CapEx: enter >USD 900m cumulative floor. Mexican company (other) despite I Squared shareholder.",
    "900000000", "2026-08-13", "2026", "20.59", "-100.39",
    "KIO Mexico/LatAm multi-campus footprint (Querétaro Mega Campus pin).",
    "kio_cumulative_900m_20260813",
    "Since I Squared Capital became a shareholder in 2022, KIO Data Centers has invested more than $900 million USD in Mexico and Latin America to strengthen its digital infrastructure platform and consolidate a network equipped to meet the demands of the region’s growing digital economy.",
    "https://kiodatacenters.com/en/newsroom/expansion/kio-data-centers-invest-growth-2030",
    "Actor: KIO Data Centers (Mexican company; I Squared shareholder) — other. NEW row: company English >USD 900m cumulative LatAm CapEx. Shuffle engineering_epc.",
    "hunt_cycle251", investment_type="corporate_capex", evidence="documented", currency="USD",
    chicago='KIO Data Centers. “KIO Data Centers Surpasses $900 Million USD in Investment and Sets the Stage for a New Phase of Growth Through 2030.” August 14, 2026. https://kiodatacenters.com/en/newsroom/expansion/kio-data-centers-invest-growth-2030.',
    annotation="KIO cumulative NEW >USD 900m floor. Supports kio_cumulative_900m_latam_2026.",
    evid_note="Opened KIO English newsroom; >USD 900m since 2022 / QRO2 USD 170m / 2026 >USD 200m / QRO3 eval USD 1.3bn confirmed.",
)

# 4. power_plants_grid / prc — NEW CPFL 1H26 CapEx R$2.8bn
row_doc(
    "cpfl_1h26_capex_2p8bn_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia (State Grid–controlled) — 1H26 CapEx spend (~R$2.8bn)",
    "Brazil",
    "13 Aug 2026 CPFL Energia: CapEx R$1.5 billion in Q2 2026, totaling R$2.8 billion year-to-date; ~80% directed to distribution (expansion, modernization, customer service, network resilience). CapEx: enter R$2.8bn 1H26 spent face. Nested vs cpfl_capex_plan_31p1bn_2026_2030 and cpfl_fy2025_capex_6p1bn_brl.",
    "2800000000", "2026-06-30", "2026", "-22.91", "-47.06",
    "CPFL Energia Brazil multi-concession distribution footprint (Campinas/São Paulo pin).",
    "cpfl_2t26_1h26_2p8bn",
    "Os investimentos (CAPEX) somaram R$ 1,5 bilhão no trimestre, totalizando R$ 2,8 bilhões no acumulado do ano. Cerca de 80% dos recursos foram direcionados à distribuição, com foco na expansão, modernização, atendimento ao cliente e em melhoria e resiliência de rede.",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213",
    "Actor: CPFL Energia — controlled by State Grid Corporation of China — prc. NEW nested 1H26 spent CapEx R$2.8bn. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle251", investment_type="capex_spend", evidence="documented", currency="BRL",
    value_usd=str(round(2800000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia. “CPFL Energia registra lucro de R$ 1,4 bilhão no 2T26, alta de 21,3%.” August 13, 2026. https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213.',
    annotation="CPFL 1H26 NEW R$2.8bn ~USD 539.28m via Fed H.10. Supports cpfl_1h26_capex_2p8bn_brl.",
    evid_note="Opened CPFL Portuguese 2T26; R$1.5bn Q2 / R$2.8bn YTD / ~80% distribution confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 5. power_plants_grid / other — NEW TAESA greenfield ANEEL R$4.3bn
row_doc(
    "taesa_greenfield_4p3bn_brl_aneel",
    "energy", "power_plants_grid", "other",
    "TAESA — four greenfield transmission projects ANEEL investment ~R$4.3bn",
    "Brazil",
    "FY2025 / 4T25 TAESA English earnings: Company currently has four greenfield projects under implementation, with total ANEEL investment of R$4.3 billion and RAP of R$490.7 million (RAP cycle 2025–2026); portion already in operation (Saíra R$137.5m; Tangará R$35.1m). CapEx: enter R$4.3bn ANEEL investment face. Distinct from TAESA FY2025 executed CapEx row.",
    "4300000000", "2025-12-31", "2025", "-15.78", "-47.93",
    "TAESA four greenfield transmission projects (Brazil multi-state; Brasília pin).",
    "taesa_4t25_greenfield_4p3bn",
    "The Company currently has four greenfield projects under implementation, with total ANEEL investment of R$ 4.3 billion and an Annual Permitted Revenue (RAP) of R$ 490.7 million (RAP cycle 2025-2026).",
    "https://ri.taesa.com.br/wp-content/uploads/2026/03/Release-4T25_ing.pdf",
    "Actor: TAESA (Brazilian transmission company) — other. NEW row: company English ANEEL greenfield R$4.3bn. Shuffle power_plants_grid / holdover filled.",
    "hunt_cycle251", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(4300000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='TAESA. “Earnings Release 4Q25 and 2025.” March 2026. https://ri.taesa.com.br/wp-content/uploads/2026/03/Release-4T25_ing.pdf.',
    annotation="TAESA greenfield NEW R$4.3bn ~USD 828.18m via Fed H.10. Supports taesa_greenfield_4p3bn_brl_aneel.",
    evid_note="Opened TAESA English 4T25 PDF; R$4.3bn ANEEL four greenfield / RAP R$490.7m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 6. power_plants_grid / other — NEW TAESA FY2025 CapEx R$1,782.8m
row_doc(
    "taesa_fy2025_capex_1p783bn_brl",
    "energy", "power_plants_grid", "other",
    "TAESA — FY2025 transmission construction CapEx (~R$1.783bn)",
    "Brazil",
    "FY2025 / 4T25 TAESA English: Company, subsidiaries, jointly controlled entities, and associates invested a total of R$1,782.8 million in 2025 vs R$999.6 million in 2024 related to projects under construction (+78.4%); highest recent construction CapEx volume; five-year cumulative ~R$6.3 billion. CapEx: enter R$1,782.8m FY2025 spent face. Nested vs greenfield R$4.3bn ANEEL pipeline.",
    "1782800000", "2025-12-31", "2025", "-15.78", "-47.93",
    "TAESA Brazil transmission construction portfolio (multi-concession; Brasília pin).",
    "taesa_4t25_fy2025_capex_1p783bn",
    "In 2025, the Company, its subsidiaries, jointly controlled entities, and associates invested a total of R$ 1,782.8 million, compared to R$ 999.6 million invested in 2024, related to projects under construction.",
    "https://ri.taesa.com.br/wp-content/uploads/2026/03/Release-4T25_ing.pdf",
    "Actor: TAESA (Brazilian transmission company) — other. NEW nested FY2025 CapEx R$1,782.8m. Shuffle power_plants_grid.",
    "hunt_cycle251", investment_type="capex_spend", evidence="documented", currency="BRL",
    value_usd=str(round(1782800000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='TAESA. “Earnings Release 4Q25 and 2025.” March 2026. https://ri.taesa.com.br/wp-content/uploads/2026/03/Release-4T25_ing.pdf.',
    annotation="TAESA FY2025 NEW R$1.783bn ~USD 343.37m via Fed H.10. Supports taesa_fy2025_capex_1p783bn_brl.",
    evid_note="Opened TAESA English 4T25 PDF; R$1,782.8m FY2025 CapEx / +78.4% / five-year ~R$6.3bn confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 7. power_plants_grid / other — NEW Alupar growth-cycle R$8.1bn
row_doc(
    "alupar_growth_cycle_8p1bn_brl",
    "energy", "power_plants_grid", "other",
    "Alupar — new growth-cycle CapEx plan (~R$8.1bn)",
    "Brazil",
    "Alupar 2024 Sustainability Report company site: Novo Ciclo de Crescimento — R$8.1 bilhões em investimento / R$1.1 bilhão em novas receitas; 12 new projects in last two years; transmission + generation Brazil and LatAm (Chile, Colombia, Peru among international footprint). CapEx: enter R$8.1bn growth-cycle face. Distinct from TECP/Lot 7 project-level CapEx reported in press without openable 2T26 PDF.",
    "8100000000", "2025-01-01", "2025", "-23.55", "-46.63",
    "Alupar Brazil + LatAm transmission/generation portfolio (São Paulo pin).",
    "alupar_sustentabilidade_8p1bn",
    "Novo Ciclo de Crescimento - R$ 8,1 bilhões em investimento - R$ 1,1 bilhão em novas receitas.",
    "https://rs.alupar.com.br/",
    "Actor: Alupar Investimento (Brazilian private holding) — other. NEW row: company sustainability R$8.1bn growth-cycle CapEx. Shuffle power_plants_grid.",
    "hunt_cycle251", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(8100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Alupar Investimento S.A. “Relatório de Sustentabilidade” (Novo Ciclo de Crescimento). https://rs.alupar.com.br/.',
    annotation="Alupar growth-cycle NEW R$8.1bn ~USD 1559.99m via Fed H.10. Supports alupar_growth_cycle_8p1bn_brl.",
    evid_note="Opened Alupar sustainability site; R$8.1bn investment cycle / R$1.1bn new revenues / 12 new projects confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
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
    print(f"cycle251 added {len(added)}: {added}")
    print(f"cycle251 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
