#!/usr/bin/env python3
"""Cycle 252 hunt: shuffle_seed=20261252; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261252).shuffle):
graphite, water, fission_smr, engineering_epc, wind, other_renewables, bridges_roads,
lithium, power_plants_grid, balsa, port_cranes, rail, solar, port_ownership,
building_materials, nickel, copper, niobium.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW John Deere Catalão R$700m factory expansion; NEW Scala AI City
  USD 500m initial (DigitalBridge-backed); NEW Scala cumulative >R$12bn investments.
PRC equal-budget: honest residual (BYD Camaçari / Goldwind Camaçari / SPIC São Simão /
  CTG H2V / CPFL 1H26 already logged this session).
Allied: NEW Grenergy Central Oasis USD 900m platform CapEx; NEW Grenergy Monte Águila
  USD 268m senior financing (nested).
Other: NEW Tecto LatAm USD 2bn 2026–2028 CapEx plan (BTG/CPPIB/GIC).
Skipped: Ada R$2.7bn Valor-only without company CapEx figure; Scala FY2025 CapEx
  R$4.7bn sustainability vs R$1.82bn DFS conflict — use cumulative + AI City instead;
  thin dry; holdovers unsigned.
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


# 1. engineering_epc / us — NEW John Deere Catalão R$700m
row_doc(
    "john_deere_catalao_700m_brl_2024",
    "infrastructure", "engineering_epc", "us",
    "John Deere — Catalão (GO) factory expansion CapEx (~R$700m)",
    "Brazil",
    "22 Apr 2024 John Deere Brasil: announces R$700 million investment in Catalão (GO) factory producing sprayers and sugarcane harvesters; >20,000 m² expansion on 62,000 m² plant; ~400 jobs over 60 months; nationalizes See & Spray™ intelligent spraying. CapEx: enter R$700m face. Distinct from john_deere_canoas_pulverizer_42m_2026 and john_deere_canoas_electronics_75m_2026.",
    "700000000", "2024-04-22", "2024", "-18.17", "-47.94",
    "John Deere Catalão factory, Goiás.",
    "john_deere_catalao_700m_20240422",
    "A John Deere anunciou nesta segunda-feira (22) um investimento de R$ 700 milhões em sua fábrica de Catalão (GO), onde são produzidos pulverizadores e colhedoras de cana.",
    "https://www.deere.com.br/pt/a-nossa-empresa/not%C3%ADcias/sala-de-imprensa/2024/abr/john-deere-anuncia-investimento-na-f%C3%A1brica-de-catal%C3%A3o/",
    "Actor: John Deere / Deere & Company (U.S.) — us. NEW row: company Portuguese R$700m Catalão expansion. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle252", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(700000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='John Deere Brasil. “John Deere anuncia investimento na fábrica de Catalão.” April 22, 2024. https://www.deere.com.br/pt/a-nossa-empresa/not%C3%ADcias/sala-de-imprensa/2024/abr/john-deere-anuncia-investimento-na-f%C3%A1brica-de-catal%C3%A3o/.',
    annotation="John Deere Catalão NEW R$700m ~USD 134.82m via Fed H.10. Supports john_deere_catalao_700m_brl_2024.",
    evid_note="Opened John Deere Brasil Portuguese press; R$700m Catalão / See & Spray / ~400 jobs confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. engineering_epc / us — NEW Scala AI City USD 500m
row_doc(
    "scala_ai_city_500m_2024",
    "infrastructure", "engineering_epc", "us",
    "Scala Data Centers (DigitalBridge) — Scala AI City Eldorado do Sul Phase 1 CapEx",
    "Brazil",
    "11 Sep 2024 Scala Data Centers: with Rio Grande do Sul government signs letter of intent for Scala AI City in Eldorado do Sul (Porto Alegre metro); initial investment USD 500 million (~BRL 3 billion) first phase; initial IT capacity 54 MW expandable toward 4,750 MW; 100% renewable; FutureProof AI racks >150 kW. CapEx: enter USD 500m Phase 1 face. Distinct from scala_chile_pf_328m_2025.",
    "500000000", "2024-09-11", "2024", "-30.08", "-51.31",
    "Scala AI City, Eldorado do Sul, Rio Grande do Sul.",
    "scala_ai_city_500m_20240911",
    "The “data center city” represents an initial investment of USD 500 million (around BRL 3 billion) in the first phase alone, marking a decisive step toward positioning Brazil as a central hub in the global Artificial Intelligence (AI) revolution and transforming Rio Grande do Sul through the economic potential of digital infrastructure.",
    "https://scaladatacenters.com/en/with-an-initial-investment-of-usd-500-million-scala-data-centers-and-rio-grande-do-sul-government-sign-agreement-for-largest-digital-infrastructure-project-in-the-state-of-southern-brazil/",
    "Actor: Scala Data Centers (DigitalBridge-backed) — us. NEW row: company English USD 500m AI City Phase 1. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle252", investment_type="corporate_capex", evidence="documented", currency="USD",
    chicago='Scala Data Centers. “With an initial investment of USD 500 million, Scala Data Centers and Rio Grande do Sul Government Sign Agreement for Largest Digital Infrastructure Project in the State of Southern Brazil.” September 11, 2024. https://scaladatacenters.com/en/with-an-initial-investment-of-usd-500-million-scala-data-centers-and-rio-grande-do-sul-government-sign-agreement-for-largest-digital-infrastructure-project-in-the-state-of-southern-brazil/.',
    annotation="Scala AI City NEW USD 500m. Supports scala_ai_city_500m_2024.",
    evid_note="Opened Scala English LOI press; USD 500m Phase 1 / 54 MW / Eldorado do Sul / DigitalBridge support confirmed.",
)

# 3. engineering_epc / us — NEW Scala cumulative >R$12bn
row_doc(
    "scala_cumulative_12bn_brl_2025",
    "infrastructure", "engineering_epc", "us",
    "Scala Data Centers (DigitalBridge) — cumulative LatAm CapEx >R$12bn",
    "Brazil",
    "Scala Data Centers S.A. 2025 Demonstrações Financeiras (company PDF): Scala is Latin America’s leading sustainable hyperscale data-center platform, headquartered in Brazil and backed by DigitalBridge; has already executed more than R$12 billion in investments; >200 MW installed/in development; landbank >11 million m² across four countries. CapEx: enter >R$12bn cumulative floor. Envelope vs AI City / Chile PF project rows (not additive).",
    "12000000000", "2025-12-31", "2025", "-23.51", "-46.85",
    "Scala Brazil/Chile/Colombia/Mexico multi-campus footprint (Tamboré/Barueri pin).",
    "scala_dfs_2025_cumulative_12bn",
    "A Scala Data Centers é a principal plataforma de data centers sustentáveis da América Latina voltada ao mercado Hyperscale. Com sede no Brasil e apoiada pela DigitalBridge, a companhia já realizou mais de R$ 12 bilhões em investimentos.",
    "https://scaladatacenters.com/wp-content/uploads/2026/04/2025-Demonstracoes-Financeiras.pdf",
    "Actor: Scala Data Centers (DigitalBridge-backed) — us. NEW row: company DFS >R$12bn cumulative CapEx. Shuffle engineering_epc / U.S. ≥1/3 budget.",
    "hunt_cycle252", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(12000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Scala Data Centers S.A. “Demonstrações Financeiras” (exercício 2025). March 26, 2026. https://scaladatacenters.com/wp-content/uploads/2026/04/2025-Demonstracoes-Financeiras.pdf.',
    annotation="Scala cumulative NEW >R$12bn ~USD 2311.20m via Fed H.10. Supports scala_cumulative_12bn_brl_2025.",
    evid_note="Opened Scala 2025 DFS PDF; >R$12bn investments / DigitalBridge / >200 MW confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. engineering_epc / other — NEW Tecto USD 2bn
row_doc(
    "tecto_2bn_latam_2026_2028",
    "infrastructure", "engineering_epc", "other",
    "Tecto Data Centers — LatAm CapEx plan USD 2bn (2026–2028)",
    "Brazil",
    "7 Apr 2026 Tecto Data Centers company: announces USD 2 billion investment plan 2026–2028 for LatAm digital infrastructure expansion (AI Grid / AI Factory); five new data centers to be announced in 2026 plus TPOA1 Porto Alegre and TGRU1 Santana de Parnaíba (up to 200 MW); operates 7 sites (Fortaleza×3, Rio TGIG1, Barranquilla×3). CapEx: enter USD 2bn plan face. Shareholders CPPIB and GIC via BTG Pactual — Brazilian platform coded other.",
    "2000000000", "2026-04-07", "2026", "-23.44", "-46.92",
    "Tecto Brazil/Colombia multi-campus (Santana de Parnaíba / Fortaleza / Barranquilla; São Paulo pin).",
    "tecto_2bn_plan_20260407",
    "A Tecto Data Centers anuncia um novo ciclo de expansão na América Latina, com um plano de investimentos de US$ 2 bilhões entre 2026 e 2028, que combina a construção de novos data centers numa estratégia integrada de AI Grid e AI Factory.",
    "https://tecto.com/radar-tecto/tecto-data-centers-anuncia-plano-de-investimento-de-us-2-bilhoes-e-amplia-atuacao-comercial-ao-oferecer-solucoes-para-o-mercado-enterprise/",
    "Actor: Tecto Data Centers (V.tal group; CPPIB/GIC via BTG) — other. NEW row: company Portuguese USD 2bn 2026–2028 CapEx plan. Shuffle engineering_epc.",
    "hunt_cycle252", investment_type="capex_plan", evidence="documented", currency="USD",
    chicago='Tecto Data Centers. “Tecto Data Centers anuncia plano de investimento de US$ 2 bilhões e amplia atuação comercial ao oferecer soluções para o mercado enterprise.” April 7/14, 2026. https://tecto.com/radar-tecto/tecto-data-centers-anuncia-plano-de-investimento-de-us-2-bilhoes-e-amplia-atuacao-comercial-ao-oferecer-solucoes-para-o-mercado-enterprise/.',
    annotation="Tecto NEW USD 2bn CapEx plan. Supports tecto_2bn_latam_2026_2028.",
    evid_note="Opened Tecto Portuguese press; USD 2bn 2026–2028 / five new DCs / TGRU1 200 MW / CPPIB+GIC via BTG confirmed.",
)

# 5. other_renewables / allied — NEW Grenergy Central Oasis USD 900m
row_doc(
    "grenergy_central_oasis_900m_chile",
    "energy", "other_renewables", "allied",
    "Grenergy — Central Oasis Chile hybrid solar+BESS platform CapEx (~USD 900m)",
    "Chile",
    "11 May 2026 Grenergy English: Central Oasis is a key Chile strategic platform with planned total capacity 1.1 GW solar and 4 GWh storage and estimated investment of USD 900 million; COD expected 2026–2027; replicates Oasis de Atacama hybrid model. CapEx: enter USD 900m platform face. Distinct from ContourGlobal Oasis de Atacama acquisition and BYD BESS supply rows; Monte Águila financing nested separately.",
    "900000000", "2026-05-11", "2026", "-35.43", "-71.67",
    "Grenergy Central Oasis (Gran Teno / Maule / Biobío region platforms; Talca-area pin).",
    "grenergy_central_oasis_900m_20260511",
    "Central Oasis represents one of Grenergy’s key strategic bets in Chile, with a planned total capacity of 1.1 GW of solar and 4 GWh of storage, and an estimated investment of $900 million.",
    "https://grenergy.eu/grenergy-secures-a-new-268-million-financing-for-central-oasis/",
    "Actor: Grenergy (Spanish IPP) — allied. NEW row: company English USD 900m Central Oasis CapEx. Shuffle other_renewables.",
    "hunt_cycle252", investment_type="capex_plan", evidence="documented", currency="USD",
    chicago='Grenergy. “Grenergy secures a new $268 million financing for Central Oasis.” May 11, 2026. https://grenergy.eu/grenergy-secures-a-new-268-million-financing-for-central-oasis/.',
    annotation="Grenergy Central Oasis NEW USD 900m. Supports grenergy_central_oasis_900m_chile.",
    evid_note="Opened Grenergy English press; USD 900m Central Oasis / 1.1 GW solar + 4 GWh BESS / COD 2026–2027 confirmed.",
)

# 6. other_renewables / allied — NEW Grenergy Monte Águila USD 268m financing
row_doc(
    "grenergy_monte_aguila_268m_fin_2026",
    "energy", "other_renewables", "allied",
    "Grenergy — Monte Águila (Central Oasis Phase IV) senior financing USD 268m",
    "Chile",
    "11 May 2026 Grenergy: closed USD 268 million senior non-recourse financing (incl. credit facilities) for Monte Águila hybrid plant — 342 MW solar + 1,034 MWh storage — part of Central Oasis; syndicate BNP Paribas lead with KfW IPEX, Rabobank, Natixis, Scotiabank; company has secured close to USD 2 billion non-recourse financing across Oasis platforms. CapEx/financing: enter USD 268m face. Nested vs Central Oasis USD 900m platform envelope.",
    "268000000", "2026-05-11", "2026", "-37.08", "-72.43",
    "Monte Águila plant, Central Oasis Phase IV, Chile (Biobío/Ñuble area pin).",
    "grenergy_monte_aguila_268m_20260511",
    "Grenergy has closed a $268 million senior non-recourse financing agreement, including credit facilities, for the Monte Águila plant. The project has a solar capacity of 342 MW and 1,034 MWh of storage and is part of the Central Oasis platform, located in Chile.",
    "https://grenergy.eu/grenergy-secures-a-new-268-million-financing-for-central-oasis/",
    "Actor: Grenergy (Spanish IPP) — allied. NEW nested Monte Águila financing USD 268m. Shuffle other_renewables.",
    "hunt_cycle252", investment_type="financing", evidence="documented", currency="USD",
    chicago='Grenergy. “Grenergy secures a new $268 million financing for Central Oasis.” May 11, 2026. https://grenergy.eu/grenergy-secures-a-new-268-million-financing-for-central-oasis/.',
    annotation="Grenergy Monte Águila NEW USD 268m financing. Supports grenergy_monte_aguila_268m_fin_2026.",
    evid_note="Opened Grenergy English press; USD 268m senior NR financing / 342 MW + 1,034 MWh / ~USD 2bn Oasis financings cumulative confirmed.",
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
    print(f"cycle252 added {len(added)}: {added}")
    print(f"cycle252 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
