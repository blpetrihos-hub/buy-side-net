#!/usr/bin/env python3
"""Cycle 201 hunt: shuffle_seed=20261201; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261201).shuffle):
nickel, power_plants_grid, fission_smr, lithium, niobium, balsa, port_cranes,
engineering_epc, solar, wind, graphite, port_ownership, rail, other_renewables,
bridges_roads, water, copper, building_materials.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on Wabtec Vale EFC MSA, AES Bolero CapEx upgrade,
Freeport/EXIM/DFC/Progress Rail/Jervois/Meitner sweeps (catalog dense).
PRC: State Grid GATE CapEx upgrade R$18bn company primary.
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


# 1. power_plants_grid / allied — Neoenergia distribution R$50bn 2026–2030
row_doc(
    "neoenergia_dist_50bn_brl_2026_2030",
    "energy",
    "power_plants_grid",
    "allied",
    "Neoenergia (Iberdrola) — five distributors CapEx plan 2026–2030",
    "Brazil",
    "8 May 2026 Neoenergia: with early MME renewal of Coelba/Cosern/Elektro concessions, announces R$ 50 billion of distribution investments 2026–2030 (+82% vs R$27.5bn in 2021–2025); 46% expansion / 40% modernization-digitalization / 14% losses+ops support; covers five distributors (>17m customers) including Brasília (not in this renewal). CapEx plan = R$50bn. Distinct from neoenergia_fy2025_capex_10p1bn_brl (single-year 2025).",
    "50000000000",
    "2026-05-08",
    "2026",
    "",
    "",
    "Neoenergia five-distributor Brazil network CapEx plan (BA/PE/RN/SP-MS/DF — lat/lon blank).",
    "neoenergia_50bn_dist_20260508",
    "A antecipação por mais 30 anos marca o início de um novo ciclo de investimentos da companhia, com aportes de R$ 50 bilhões entre 2026 e 2030, um crescimento de 82% em relação ao ciclo anterior (2021-2025), quando foram investidos R$ 27,5 bilhões.",
    "https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. Company Portuguese primary. CapEx plan = R$50bn (BRL stored without FX). Shuffle power_plants_grid.",
    "hunt_cycle201",
    investment_type="capex_plan",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Neoenergia. “Neoenergia renova mais três concessões e anuncia investimentos de R$ 50 bilhões em distribuição no país.” May 8, 2026. https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia.',
    annotation="Neoenergia distribution: R$50bn 2026–2030. Supports neoenergia_dist_50bn_brl_2026_2030.",
    evid_note="Opened Neoenergia Portuguese company primary 2026-10-04; R$50bn 2026–2030 confirmed.",
)

# 2. power_plants_grid / allied — Neoenergia Brasília R$3.1bn 2026–2030
row_doc(
    "neoenergia_brasilia_3p1bn_brl_2026_2030",
    "energy",
    "power_plants_grid",
    "allied",
    "Neoenergia Brasília — DF distribution CapEx plan 2026–2030",
    "Brazil",
    "6 Aug 2026 Neoenergia Brasília: largest DF cycle — R$ 3.1 billion 2026–2030 for expansion, modernization and digitalization of the distribution network (+118% vs prior cycle); five new/expanded substations; 132 km new HV lines; >1.3m customers. CapEx = R$3.1bn. Distinct from neoenergia_dist_50bn_brl_2026_2030 group envelope (Brasília share within/alongside group plan; logged as named DF concession program).",
    "3100000000",
    "2026-08-06",
    "2026",
    "-15.78",
    "-47.93",
    "Neoenergia Brasília DF concession (Brasília institutional pin).",
    "neoenergia_brasilia_3p1bn_20260806",
    "De 2026 até 2030, serão aplicados R$ 3,1 bilhões em obras de expansão, modernização e digitalização da rede de distribuição de energia.",
    "https://www.neoenergia.com/w/plano-recorde-de-3bi-para-fortalecer-infraestrutura-df",
    "Actor: Neoenergia Brasília (Iberdrola) — allied. Company Portuguese primary. CapEx = R$3.1bn. Shuffle power_plants_grid.",
    "hunt_cycle201",
    investment_type="capex_plan",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Neoenergia. “Neoenergia anuncia plano recorde de R$ 3,1 bilhões para fortalecer a infraestrutura elétrica do DF.” August 6, 2026. https://www.neoenergia.com/w/plano-recorde-de-3bi-para-fortalecer-infraestrutura-df.',
    annotation="Neoenergia Brasília: R$3.1bn 2026–2030. Supports neoenergia_brasilia_3p1bn_brl_2026_2030.",
    evid_note="Opened Neoenergia Brasília Portuguese company primary 2026-10-04; R$3.1bn confirmed.",
)

# 3. power_plants_grid / allied — Neoenergia Ilhabela R$200m
row_doc(
    "neoenergia_ilhabela_200m_brl_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "Neoenergia Elektro — Ilhabela substation + submarine/underground line",
    "Brazil",
    "8 May 2026 Neoenergia (within Elektro concession renewal package): named Ilhabela project with R$ 200 million investment for a new substation and underground/submarine transmission line reducing visual/environmental impact on the island. CapEx = R$200m. Within-envelope of neoenergia_dist_50bn_brl_2026_2030 (Elektro share) — project-level row, not additive to group R$50bn.",
    "200000000",
    "2026-05-08",
    "2026",
    "-23.78",
    "-45.36",
    "Ilhabela, São Paulo northern coast (company geography; approximate municipal pin).",
    "neoenergia_50bn_dist_20260508",
    "Com um investimento de R$ 200 milhões, está prevista a construção de uma nova subestação e de uma linha de transmissão subterrânea e subaquática, solução que reduz impactos visuais e ambientais, respeitando o ecossistema local e a paisagem natural da ilha.",
    "https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia",
    "Actor: Neoenergia Elektro (Iberdrola) — allied. Company Portuguese primary. CapEx = R$200m named Ilhabela works. Shuffle power_plants_grid.",
    "hunt_cycle201",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Neoenergia. “Neoenergia renova mais três concessões e anuncia investimentos de R$ 50 bilhões em distribuição no país.” May 8, 2026. https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia.',
    annotation="Neoenergia Ilhabela: R$200m. Supports neoenergia_ilhabela_200m_brl_2026.",
    evid_note="Opened Neoenergia Portuguese company primary 2026-10-04; R$200m Ilhabela confirmed.",
)

# 4. power_plants_grid / allied — Neoenergia Guará 2 R$32m
row_doc(
    "neoenergia_guara2_32m_brl_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "Neoenergia Brasília — Subestação Guará 2 delivery",
    "Brazil",
    "6 Aug 2026 Neoenergia Brasília: Subestação Guará 2 delivered as first major work of the new DF cycle — total investment R$ 32 million; +66.6 MVA; benefits ~180,000 residents. CapEx = R$32m. Distinct from neoenergia_brasilia_3p1bn_brl_2026_2030 multi-year plan (this is the delivered first asset within that cycle).",
    "32000000",
    "2026-08-06",
    "2026",
    "-15.82",
    "-47.98",
    "Subestação Guará 2, Guará, Distrito Federal (company geography; approximate).",
    "neoenergia_brasilia_3p1bn_20260806",
    "A nova subestação, que recebeu investimento total de R$ 32 milhões, acrescenta 66,6 MVA de potência ao sistema elétrico e beneficia cerca de 180 mil moradores diretamente.",
    "https://www.neoenergia.com/w/plano-recorde-de-3bi-para-fortalecer-infraestrutura-df",
    "Actor: Neoenergia Brasília (Iberdrola) — allied. Company Portuguese primary. CapEx = R$32m. Shuffle power_plants_grid.",
    "hunt_cycle201",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Neoenergia. “Neoenergia anuncia plano recorde de R$ 3,1 bilhões para fortalecer a infraestrutura elétrica do DF.” August 6, 2026. https://www.neoenergia.com/w/plano-recorde-de-3bi-para-fortalecer-infraestrutura-df.',
    annotation="Neoenergia Guará 2: R$32m. Supports neoenergia_guara2_32m_brl_2026.",
    evid_note="Opened Neoenergia Brasília Portuguese company primary 2026-10-04; R$32m Guará 2 confirmed.",
)

# 5. power_plants_grid / allied — Neoenergia Coelba coastal >R$7bn
row_doc(
    "neoenergia_coelba_litoral_7bn_brl_2026",
    "energy",
    "power_plants_grid",
    "allied",
    "Neoenergia Coelba — Bahia coastal distribution transformation package",
    "Brazil",
    "8 May 2026 Neoenergia: within renewed Coelba concession, coastal Bahia package of more than R$ 7 billion — 18 new substations + modernization/expansion of 10 units with advanced automation; serves ~2.9m customers and ~10m annual visitors along Brazil’s longest coastal strip. CapEx floor >R$7bn (stored as 7e9). Within-envelope of neoenergia_dist_50bn_brl_2026_2030 (Coelba share) — named corridor package, not additive to group R$50bn.",
    "7000000000",
    "2026-05-08",
    "2026",
    "-12.97",
    "-38.51",
    "Pinned to Salvador / Bahia coastal corridor start (company multi-municipality — approximate).",
    "neoenergia_50bn_dist_20260508",
    "O projeto, de mais de R$ 7 bilhões, contempla a implantação de 18 novas subestações e a modernização e ampliação de outras 10 unidades, com incorporação de tecnologias avançadas e automação.",
    "https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia",
    "Actor: Neoenergia Coelba (Iberdrola) — allied. Company Portuguese primary. CapEx floor >R$7bn. Shuffle power_plants_grid.",
    "hunt_cycle201",
    investment_type="brownfield_expansion",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Neoenergia. “Neoenergia renova mais três concessões e anuncia investimentos de R$ 50 bilhões em distribuição no país.” May 8, 2026. https://www.neoenergia.com/w/renovacao-concessao-coelba-cosern-elektro-50-bilhoes-distribuicao-energia.',
    annotation="Neoenergia Coelba coastal: >R$7bn. Supports neoenergia_coelba_litoral_7bn_brl_2026.",
    evid_note="Opened Neoenergia Portuguese company primary 2026-10-04; >R$7bn coastal package confirmed.",
)

# 6. rail / us — Wabtec Vale EFC MSA R$1.8bn
row_doc(
    "wabtec_vale_efc_msa_1p8bn_brl_2024",
    "infrastructure",
    "rail",
    "us",
    "Wabtec — 10-year MSA for Vale EFC Evolution Series locomotive fleet",
    "Brazil",
    "5 Jun 2024 Wabtec: master service agreement with Vale valued at R$ 1.8 billion over 10 years to optimize maintenance of Evolution Series (EVO) locomotives on Estrada de Ferro Carajás (EFC); real-time monitoring of 5,000 parameters; Global Performance Optimization Centers; jobs/training in São Luís. CapEx/services = R$1.8bn. Distinct from wabtec_vale_ptc_brl1bn_2026 (I-ETMS PTC) and wabtec_vale_50_locos_2026 (new locomotives).",
    "1800000000",
    "2024-06-05",
    "2024",
    "-2.53",
    "-44.30",
    "Pinned to São Luís / EFC Maranhão terminus (company geography; approximate).",
    "wabtec_vale_efc_msa_20240605",
    "The strategic 10-year deal, valued at R$1.8 billion, will optimize the maintenance services for Vale’s fleet increasing performance, reliability, and the potential for expanded freight transport on the EFC connecting the southeast of Pará to the capital of Maranhão, São Luís.",
    "https://www.wabteccorp.com/newsroom/press-releases/vale-and-wabtec-sign-an-r18b-services-agreement-to-enhance-caraj-s-railway-locomotive-fleet",
    "Actor: Wabtec Corporation (U.S., NYSE:WAB) — us; customer Vale. Company English primary. CapEx/services = R$1.8bn. Shuffle rail; ≥1/3 U.S. hunt.",
    "hunt_cycle201",
    investment_type="services_contract",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='Wabtec Corporation. “Vale and Wabtec Sign an R$1.8B Services Agreement to Enhance Carajás Railway Locomotive Fleet.” June 5, 2024. https://www.wabteccorp.com/newsroom/press-releases/vale-and-wabtec-sign-an-r18b-services-agreement-to-enhance-caraj-s-railway-locomotive-fleet.',
    annotation="Wabtec Vale EFC MSA: R$1.8bn. Supports wabtec_vale_efc_msa_1p8bn_brl_2024.",
    evid_note="Opened Wabtec English company primary 2026-10-04; R$1.8bn 10-year MSA confirmed.",
)

# 7. power_plants_grid / prc — upgrade State Grid GATE CapEx to R$18bn company primary
row_doc(
    "state_grid_ne_uhv_construction_2026",
    "energy",
    "power_plants_grid",
    "prc",
    "State Grid Brazil Holding — ±800 kV Northeast Brazil UHVDC (Graça Aranha–Silvânia)",
    "Brazil",
    "State Grid Brazil Holding company Portuguese: GATE (Graça Aranha Transmissora de Energia) ±800 kV / 1,468 km UHVDC Graça Aranha (MA)–Silvânia (GO) with two converter stations — R$ 18 billion destined to the project; foundation launch Silvânia; COD targeted 2029; 30-year concession; 5 GW capacity. Upgrades prior CapEx-blank construction-start row (SASAC English) with company CapEx figure. Distinct from excluded RAP auction row aneel_state_grid_rap_2023.",
    "18000000000",
    "2026-06-30",
    "2026",
    "-16.66",
    "-48.61",
    "Silvânia (GO) receiving-end converter area pin (State Grid / project corridor).",
    "stategrid_gate_silvania_18bn",
    "A State Grid Brazil Holding (SGBH) —subsidiária de um dos maiores grupos de energia do mundo, a State Grid Corporation of China (SGCC) — lançará em 30/6, em Silvânia (GO), a pedra fundamental do “Projeto de Ultra Alta Tensão no Nordeste do Brasil”, para o qual serão destinados R$ 18 bilhões.",
    "https://stategrid.com.br/municipio-goiano-de-silvania-sedia-lancamento-do-mais-caro-projeto-de-ultra-alta-tensao-800kv-da-historia-do-setor-eletrico-do-brasil/",
    "Actor: State Grid Brazil Holding (PRC SOE subsidiary) — prc. Company Portuguese primary CapEx R$18bn. Upgrades CapEx-blank construction milestone. Shuffle power_plants_grid.",
    "hunt_cycle201",
    investment_type="concession_construction",
    evidence="documented",
    currency="BRL",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago='State Grid Brazil Holding. “Município goiano de Silvânia sedia lançamento do mais caro projeto de Ultra Alta Tensão (800Kv) da história do setor elétrico do Brasil.” https://stategrid.com.br/municipio-goiano-de-silvania-sedia-lancamento-do-mais-caro-projeto-de-ultra-alta-tensao-800kv-da-historia-do-setor-eletrico-do-brasil/.',
    annotation="State Grid GATE: R$18bn. Supports state_grid_ne_uhv_construction_2026.",
    evid_note="Opened State Grid Brazil Holding Portuguese company primary 2026-10-04; R$18bn CapEx confirmed; upgrades prior blank CapEx.",
)

# 8. port_ownership / allied — upgrade APM Callao Stage 3B to company primary
row_doc(
    "apm_callao_stage3b_2026",
    "infrastructure",
    "port_ownership",
    "allied",
    "APM Terminals Callao — North Terminal Stage 3B modernization",
    "Peru",
    "26 Jun 2026 APM Terminals company: construction start on Stage 3B of Callao North Terminal modernization — investment approximately USD 570 million over two phases through 2030; Phase 1 (2026–2028) Pier 5C for ULCVs + three MalaccaMax quay cranes + container equipment + 16-lane general-cargo gate; Phase 2 (2028–2030) three new general-cargo berths; capacity 1.3→1.75m containers and 13.5→18m t general cargo. Upgrades prior DataPortuaria UNVERIFIED proxy to company primary. Crane OEM unnamed — coded port_ownership not port_cranes.",
    "570000000",
    "2026-06-26",
    "2026",
    "-12.048",
    "-77.143",
    "Terminal Norte Multipropósito, Port of Callao (APM Terminals geography).",
    "apm_callao_stage3b_20260626",
    "This phase represents an investment of approximately USD 570 million by APM Terminals Callao and will significantly expand the operational capacity of Peru’s first multipurpose terminal.",
    "https://www.apmterminals.com/en/callao/customer-zone/news-and-alerts/2026/260626-APM-Terminals-launches-next-phase-of-expansion-in-Callao",
    "Actor: APM Terminals (Maersk/Denmark) — allied. Company English primary. CapEx ≈ USD 570m. Upgrades prior DataPortuaria proxy. Shuffle port_ownership.",
    "hunt_cycle201",
    investment_type="concession_capex",
    evidence="documented",
    currency="USD",
    value_usd="570000000",
    fx_usd="1",
    bib_type="company",
    chicago='APM Terminals. “APM Terminals launches next phase of expansion in Callao.” June 26, 2026. https://www.apmterminals.com/en/callao/customer-zone/news-and-alerts/2026/260626-APM-Terminals-launches-next-phase-of-expansion-in-Callao.',
    annotation="APM Callao Stage 3B: USD 570m company primary. Supports apm_callao_stage3b_2026.",
    evid_note="Opened APM Terminals English company primary 2026-10-04; USD 570m confirmed; upgrades prior DataPortuaria proxy.",
)

# 9. other_renewables / us — upgrade AES Bolero BESS CapEx ~USD 137m (press citing firm)
row_doc(
    "aes_bolero_bess_146mw_chile_2025",
    "energy",
    "other_renewables",
    "us",
    "AES Andes / AES Corporation — Bolero BESS 146 MW / 438 MWh COD (Antofagasta)",
    "Chile",
    "3–4 Aug 2026: AES Andes starts commercial operations of Bolero BESS (146 MW / ~438 MWh / 3-hour) co-located with Bolero solar (Sierra Gorda, Antofagasta); Diario Financiero citing company announcement reports investment around USD 137 million; company reaches 756 MW BESS operated in Chile. Upgrades prior CapEx-blank construction-presence row with COD + UNVERIFIED press CapEx citing firm. Distinct from aes_andes_pampas_cristales_2025 / Arenales / Andes Solar III hub.",
    "137000000",
    "2026-08-03",
    "2026",
    "-22.90",
    "-69.30",
    "Bolero solar / BESS, Sierra Gorda, Antofagasta Region (company geography; approximate).",
    "df_aes_bolero_bess_20260803",
    "AES Andes anunció este lunes el inicio de operaciones de Bolero BESS, un nuevo sistema de almacenamiento de energía en baterías ubicado en la Región de Antofagasta, el cual involucra alrededor de US$ 137 millones en inversión.",
    "https://www.df.cl/empresas/energia/aes-andes-inicia-operacion-de-nuevo-sistema-de-almacenamiento-de-energia",
    "Actor: AES Andes / AES Corporation (U.S.) — us. UNVERIFIED proxy: Diario Financiero 3 Aug 2026 citing AES Andes announcement (~USD 137m); company Spanish pages confirm COD/scope without CapEx figure opened. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle201",
    investment_type="brownfield_storage",
    evidence="proxy",
    currency="USD",
    value_usd="137000000",
    fx_usd="1",
    bib_type="press",
    chicago='Peña, Karen. “AES Andes inicia operación de nuevo sistema de almacenamiento de energía que involucra más de US$ 130 millones.” Diario Financiero, August 3, 2026. https://www.df.cl/empresas/energia/aes-andes-inicia-operacion-de-nuevo-sistema-de-almacenamiento-de-energia.',
    annotation="AES Bolero BESS CapEx ~USD 137m (press citing firm). Supports aes_bolero_bess_146mw_chile_2025.",
    evid_note="Opened Diario Financiero Spanish 2026-10-04 citing AES Andes ~USD 137m; CapEx blank on opened AES Andes pages — evidence=proxy upgrade.",
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
    print(f"cycle201 added {len(added)}: {added}")
    print(f"cycle201 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
