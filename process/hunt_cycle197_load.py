#!/usr/bin/env python3
"""Cycle 197 hunt: shuffle_seed=20261197; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261197).shuffle):
wind, fission_smr, other_renewables, solar, copper, building_materials, graphite,
port_cranes, bridges_roads, lithium, nickel, port_ownership, niobium,
engineering_epc, balsa, rail, water, power_plants_grid.

Thin top-up (recomputed after shuffle pass): balsa / nickel / fission_smr — all dry.
≥1/3 U.S. hunt budget spent on Microsoft Brazil cloud/AI, Google Uruguay Canelones,
SEC/EXIM/AES/Freeport/Wabtec Contagem sweeps — 2 new U.S. rows.
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


# 1. engineering_epc / us — Microsoft Brazil cloud/AI R$14.7bn (3 years)
row_doc(
    "microsoft_brazil_cloud_ai_14p7bn_brl_2024",
    "infrastructure",
    "engineering_epc",
    "us",
    "Microsoft — Brazil cloud and AI infrastructure package (3 years)",
    "Brazil",
    "26 Sep 2024 Microsoft News Center Brasil: largest single Microsoft investment in Brazil — plans to spend 14.7 billion Reais in cloud and artificial intelligence (AI) infrastructure over three years; expand cloud/AI infrastructure across several datacenter campuses in São Paulo state; ConectAI skills program (5 million people) is separate from the infrastructure CapEx figure. CapEx package = R$14.7bn. Distinct from microsoft_mexico_ai_1p3bn_2024 and AWS Chile / Google DR / ODATA rows.",
    "14700000000",
    "2024-09-26",
    "2024",
    "",
    "",
    "Microsoft Brazil São Paulo-state datacenter campus package (company multi-site — lat/lon blank).",
    "microsoft_brazil_14p7bn_20240926",
    "Today, Microsoft announced its largest single investment in Brazil, with plans to spend 14.7 billion Reais in cloud and artificial intelligence (AI) infrastructure over three years. … Microsoft will expand its cloud and AI infrastructure across several datacenter campuses in the state of São Paulo.",
    "https://news.microsoft.com/pt-br/microsoft-announces-14-7-billion-reais-investment-over-three-years-in-cloud-and-ai-infrastructure-and-provide-ai-training-at-scale-to-upskill-5-million-people-in-brazil/",
    "Actor: Microsoft Corporation (U.S.) — us. Company English News Center Brasil primary. CapEx package = R$14.7bn (BRL stored without FX). Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle197",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Microsoft. “Microsoft announces 14.7 billion Reais investment over three years in Cloud and AI infrastructure and provide AI training at scale to upskill 5 million people in Brazil.” Microsoft News Center Brasil, September 26, 2024. https://news.microsoft.com/pt-br/microsoft-announces-14-7-billion-reais-investment-over-three-years-in-cloud-and-ai-infrastructure-and-provide-ai-training-at-scale-to-upskill-5-million-people-in-brazil/.',
    annotation="Microsoft: Brazil cloud/AI CapEx R$14.7bn over 3 years. Supports microsoft_brazil_cloud_ai_14p7bn_brl_2024.",
    evid_note="Opened Microsoft News Center Brasil English primary 2026-10-04; R$14.7bn infrastructure confirmed.",
)

# 2. engineering_epc / us — Google Uruguay Canelones >USD 850m
row_doc(
    "google_uruguay_canelones_850m_2024",
    "infrastructure",
    "engineering_epc",
    "us",
    "Google — Canelones / Parque de las Ciencias data center (Uruguay)",
    "Uruguay",
    "29 Aug 2024 Google Blog: groundbreaking on second LatAm data center in Canelones, Uruguay; investing more than USD 850 million in the new data center; complements Chile Quilicura (2015). CapEx floor = USD 850m. Distinct from google_dr_digital_port_500m_2026 and AES Andes Google Quilicura PPA rows.",
    "850000000",
    "2024-08-29",
    "2024",
    "-34.78",
    "-56.05",
    "Canelones / Parque de las Ciencias, Municipality of Nicolich (Google datacenters location page; approximate pin).",
    "google_canelones_dc_20240829",
    "Today, after dedicated planning and analysis, we are taking another step forward with the construction of a second data center in Latin America, this time in Canelones, Uruguay. We’re investing more than $850 million USD in the new data center, which will bring greater connectivity across the region…",
    "https://blog.google/company-news/inside-google/around-the-globe/google-latin-america/a-new-data-center-in-latin-america/",
    "Actor: Google (Alphabet Inc., U.S.) — us. Company English blog primary. CapEx floor >USD 850m (stored as 8.5e8 floor). Shuffle engineering_epc; ≥1/3 U.S. hunt.",
    "hunt_cycle197",
    investment_type="greenfield_plant",
    evidence="documented",
    currency="USD",
    value_usd="850000000",
    fx_usd="1",
    bib_type="company",
    chicago='López, Eduardo. “A new data center in Latin America.” Google Blog, August 29, 2024. https://blog.google/company-news/inside-google/around-the-globe/google-latin-america/a-new-data-center-in-latin-america/.',
    annotation="Google: Canelones Uruguay DC >USD 850m. Supports google_uruguay_canelones_850m_2024.",
    evid_note="Opened Google Blog English primary 2026-10-04; >USD 850m confirmed.",
)

# 3. copper / allied — Antofagasta FY2025 Group CapEx USD 3.7bn
row_doc(
    "antofagasta_fy2025_capex_3p7bn",
    "resources",
    "copper",
    "allied",
    "Antofagasta plc — FY2025 consolidated Group capital expenditure",
    "Chile",
    "17 Feb 2026 Antofagasta plc FY2025 results: capital expenditure peaked in 2025 at USD 3.7 billion (2024: USD 2.4 billion), with major capital projects continuing in line with expectations; CEO notes invested USD 3.7 billion in the business during the year. Group Chile copper portfolio CapEx (Centinela Second Concentrator and other). CapEx = USD 3.7bn. Distinct from antofagasta_centinela_2nd_conc_2023 (USD 4.4bn project approval) and Almar Centinela water transfer.",
    "3700000000",
    "2026-02-17",
    "2025",
    "",
    "",
    "Antofagasta Group Chile copper operations CapEx (multi-mine portfolio — lat/lon blank).",
    "antofagasta_fy2025_results_20260217",
    "Capital expenditure peaked in 2025 at $3.7 billion (2024: $2.4 billion), with major capital projects continuing in line with expectations. … despite having invested $3.7 billion in our business during the year.",
    "https://www.antofagasta.co.uk/investors/news/2026/2025-full-year-results/",
    "Actor: Antofagasta plc (UK / Chile Luksic) — allied. Company English FY2025 results primary. CapEx = USD 3.7bn. Shuffle copper.",
    "hunt_cycle197",
    investment_type="capex_expansion",
    evidence="documented",
    currency="USD",
    value_usd="3700000000",
    fx_usd="1",
    bib_type="company",
    chicago='Antofagasta plc. “2025 Full Year Results.” February 17, 2026. https://www.antofagasta.co.uk/investors/news/2026/2025-full-year-results/.',
    annotation="Antofagasta: FY2025 Group CapEx USD 3.7bn. Supports antofagasta_fy2025_capex_3p7bn.",
    evid_note="Opened Antofagasta English FY2025 results page 2026-10-04.",
)

# 4. building_materials / other — Votorantim Cimentos FY2025 CapEx R$3.7bn
row_doc(
    "votorantim_fy2025_capex_3p7bn_brl",
    "infrastructure",
    "building_materials",
    "other",
    "Votorantim Cimentos — FY2025 consolidated CapEx",
    "Brazil",
    "18 Mar 2026 Votorantim Cimentos: investments (Capex) totaled R$3.7 billion in 2025 (+14% YoY), focused on structural competitiveness, capacity expansion, decarbonization and new businesses; separately notes R$2.7bn of the R$5bn Brazil 2024–2028 plan already invested (already logged as votorantim_brazil_plan_2p7bn_invested_2025). CapEx = R$3.7bn executed. Distinct from site-level Edealina/Nobres/Xambioá rows and the cumulative Brazil-plan progress row.",
    "3700000000",
    "2026-03-18",
    "2025",
    "",
    "",
    "Votorantim Cimentos consolidated CapEx (global; Brazil is largest region — lat/lon blank).",
    "votorantim_fy2025_results_20260318",
    "Our investments (Capex) totaled R$3.7 billion, up 14% compared to the previous year, and focused on structural competitiveness, capacity expansion, decarbonization and new businesses. … Last year, our investments (Capex) totaled R$3.7 billion, up 14% compared to 2024.",
    "https://www.votorantimcimentos.com/news/our-2025-financial-results/",
    "Actor: Votorantim Cimentos (Brazil) — other. Company English FY2025 results. CapEx = R$3.7bn (BRL stored without FX). Shuffle building_materials.",
    "hunt_cycle197",
    investment_type="capex_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Votorantim Cimentos. “Our 2025 financial results.” March 18, 2026. https://www.votorantimcimentos.com/news/our-2025-financial-results/.',
    annotation="Votorantim: FY2025 CapEx R$3.7bn. Supports votorantim_fy2025_capex_3p7bn_brl.",
    evid_note="Opened Votorantim English FY2025 results 2026-10-04; R$3.7bn CapEx confirmed.",
)

# 5. power_plants_grid / allied — ENGIE Brasil FY2025 CapEx R$6bn
row_doc(
    "engie_brasil_fy2025_capex_6bn_brl",
    "energy",
    "power_plants_grid",
    "allied",
    "ENGIE Brasil Energia — FY2025 CapEx (hydro acquisitions + modernization + projects)",
    "Brazil",
    "25 Feb 2026 ENGIE Brasil Energia: invested R$ 6 billion in 2025 in acquisition of new hydropower assets, modernization work, implementation of projects and generator-park revitalization; includes Santo Antônio do Jari / Cachoeira Caldeirão acquisition (~R$2.9bn of the envelope) plus Assuruá wind / Assú Sol solar COD milestones. CapEx = R$6bn. Distinct from engie_brasil_aneel_01_2026_15bn auction CapEx and engie_jaguara_modernization_500m_brl_2026.",
    "6000000000",
    "2026-02-25",
    "2025",
    "",
    "",
    "ENGIE Brasil Energia national generation/transmission CapEx (multi-asset — lat/lon blank).",
    "engie_brasil_fy2025_results_20260225",
    "During the year, the Company invested R$ 6 billion in the acquisition of new hydropower assets, in modernization work, the implementation of projects and generator park revitalization.",
    "https://www.engie.com.br/en/imprensa/press-releases/engie-brasil-energia-grows-14-6-in-revenue-and-invests-r-6-billion-in-2025/",
    "Actor: ENGIE Brasil Energia (France ENGIE) — allied. Company English primary. CapEx = R$6bn (BRL stored without FX). Shuffle power_plants_grid.",
    "hunt_cycle197",
    investment_type="capex_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='ENGIE Brasil Energia. “ENGIE Brasil Energia grows 14.6% in revenue and invests R$ 6 billion in 2025.” February 25, 2026. https://www.engie.com.br/en/imprensa/press-releases/engie-brasil-energia-grows-14-6-in-revenue-and-invests-r-6-billion-in-2025/.',
    annotation="ENGIE Brasil: FY2025 CapEx R$6bn. Supports engie_brasil_fy2025_capex_6bn_brl.",
    evid_note="Opened ENGIE Brasil English FY2025 release 2026-10-04.",
)

# 6. power_plants_grid / allied — Neoenergia FY2025 CapEx R$10.1bn
row_doc(
    "neoenergia_fy2025_capex_10p1bn_brl",
    "energy",
    "power_plants_grid",
    "allied",
    "Neoenergia (Iberdrola) — FY2025 CapEx",
    "Brazil",
    "11 Feb 2026 Neoenergia: Capex in 2025 of the order of R$ 10.1 billion — R$ 6.5 billion to distribution (expansion/maintenance/digitalization/modernization) and about R$ 3.3 billion to transmission (final four lots delivered 2025). CapEx = R$10.1bn. Distinct from Engie Brasil / CPFL CapEx rows.",
    "10100000000",
    "2026-02-11",
    "2025",
    "",
    "",
    "Neoenergia Brazil distribution/transmission CapEx (five distributors + TX portfolio — lat/lon blank).",
    "neoenergia_fy2025_results_20260211",
    "Com foco no cliente e na melhoria contínua nos serviços, companhia registrou no CAPEX em 2025, de R$ 10,1 bilhões - sendo R$ 6,5 bilhões em distribuição … a companhia registrou de Capex em 2025 da ordem de R$ 10,1 bilhões. Desse total, R$ 6,5 bilhões foram direcionados ao negócio de distribuição. … Em transmissão, o Capex foi de cerca de R$ 3,3 bilhões…",
    "https://www.neoenergia.com/w/2025-tem-lucro-de-5-bilhoes-1",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. Company Portuguese primary. CapEx = R$10.1bn (BRL stored without FX). Shuffle power_plants_grid.",
    "hunt_cycle197",
    investment_type="capex_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Neoenergia. “Neoenergia encerra 2025 com lucro de R$ 5 bilhões.” February 11, 2026. https://www.neoenergia.com/w/2025-tem-lucro-de-5-bilhoes-1.',
    annotation="Neoenergia: FY2025 CapEx R$10.1bn. Supports neoenergia_fy2025_capex_10p1bn_brl.",
    evid_note="Opened Neoenergia Portuguese FY2025 results 2026-10-04.",
)

# 7. power_plants_grid / prc — upgrade SPIC São Simão UG7 to company primary (>R$1bn floor)
row_doc(
    "spic_sao_simao_ug7_lrcap_2026",
    "energy",
    "power_plants_grid",
    "prc",
    "SPIC Brasil — São Simão UHE UG7 capacity expansion (310 MW / LRCAP 2026)",
    "Brazil",
    "18–19 Mar 2026 SPIC Brasil company release: winner at LRCAP 2026 for UG7 at UHE São Simão (MG–GO border) adding 310 MW; investment of more than R$ 1 billion; 15-year capacity-reserve contract; supply start targeted 2030; project start targeted still in 2026. CapEx floor = R$1bn (company ‘mais de R$ 1 bilhão’). Upgrades prior proxy R$1.4bn press figure to documented company primary. Distinct from ge_vernova_sao_simao_ug3_2026 / powerchina_sao_simao_bop_2026 six-unit modernization (>R$1.2bn) and Dongfang/CGGC UG7 equipment supply row.",
    "1000000000",
    "2026-03-19",
    "2026",
    "-18.99",
    "-50.24",
    "UHE São Simão, Goiás–Minas Gerais border (plant pin).",
    "spic_brasil_sao_simao_ug7_20260319",
    "O projeto representa um investimento de mais de R$ 1 bilhão e reforça o papel estratégico da fonte hidrelétrica para a segurança elétrica, modicidade tarifária, sustentabilidade ambiental e resiliência do Sistema Interligado Nacional (SIN). … O contrato de reserva de capacidade é de 15 anos, com início de suprimento previsto para 2030.",
    "https://www.spicbrasil.com.br/destaque/spic-brasil-expandira-a-uhe-sao-simao-em-310-mw-via-leilao-de-reserva-de-capacidade-com-mais-de-r-1-bilhao-em-investimentos/",
    "Actor: SPIC Brasil (State Power Investment Corp. PRC affiliate) — prc. Company Portuguese primary. CapEx floor >R$1bn (stored as 1e9 floor; prior R$1.4bn press proxy superseded). Shuffle power_plants_grid.",
    "hunt_cycle197",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='SPIC Brasil. “SPIC Brasil expandirá a UHE São Simão em 310 MW via Leilão de Reserva de Capacidade, com mais de R$ 1 bilhão em investimentos.” March 19, 2026. https://www.spicbrasil.com.br/destaque/spic-brasil-expandira-a-uhe-sao-simao-em-310-mw-via-leilao-de-reserva-de-capacidade-com-mais-de-r-1-bilhao-em-investimentos/.',
    annotation="SPIC Brasil: São Simão UG7 >R$1bn LRCAP. Supports spic_sao_simao_ug7_lrcap_2026.",
    evid_note="Opened SPIC Brasil Portuguese primary 2026-10-04; >R$1bn CapEx floor confirmed (upgrade from press proxy).",
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
    updated = []

    for row, evid, bib_e in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
            updated.append(rid)
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
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle197 added {len(added)}: {added}")
    print(f"cycle197 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
