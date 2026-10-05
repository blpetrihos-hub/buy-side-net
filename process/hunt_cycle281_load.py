#!/usr/bin/env python3
"""Cycle 281 hunt: shuffle_seed=20261281; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261281).shuffle):
other_renewables, water, building_materials, rail, port_cranes, wind,
engineering_epc, balsa, bridges_roads, power_plants_grid, graphite, nickel,
fission_smr, lithium, solar, port_ownership, niobium, copper.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Freeport Cerro Verde LOM sustaining CapEx USD5.2bn
  (TRS Dec 31 2024 / Jan 31 2025 company PDF) + nested Mine USD1.7bn + Supporting
  Infrastructure/Environmental USD2.4bn; Ormat Dominica/Amatitlán CapEx blanks;
  SSA Guaymas CapEx blank; Wabtec Vale 50 loco CapEx blank; Progress Rail VLI
  R$430m unsigned; Equinix/Ascenty/Seven Seas CapEx blanks; EXIM/USTDA probes.
PRC equal-budget: CapEx-fill COFCO STS11 Santos direct CapEx R$1.64bn (Folha
  5 Mar 2025 quoting company; company newsroom 403 — UNVERIFIED proxy).
Other: NEW Rumo Material Rodante / Capacitação Malha / FMT / Operação Sul 6M26;
  Aegea Corsan / Águas do Rio / Novas Operações / PPPs 6M26.
Skipped: thin dry; ENGIE Colibri 403; Ascenty 403; Alupar TECP CapEx figure
  absent; holdovers unsigned; Atlantic Nickel UG already logged.
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


# 1. copper / us — NEW Freeport Cerro Verde LOM sustaining CapEx USD5.2bn (TRS)
row_doc(
    "fcx_cerro_verde_lom_sustaining_5p2bn_2024",
    "resources", "copper", "us",
    "Freeport-McMoRan / Cerro Verde — LOM sustaining CapEx USD5.2bn",
    "Peru",
    "31 Jan 2025 Freeport-McMoRan Technical Report Summary (effective 31 Dec 2024): Cerro Verde life-of-mine capital expenditures total USD 5.2 billion — primarily sustaining projects (mine equipment replacements + site infrastructure; notably TSF and leach-pad capacity). CapEx: enter USD5.2bn LOM sustaining total. Nested vs MEIA-2 ~USD2.1bn / OxI >USD14m / La Enlozada >USD300m (not additive envelopes).",
    "5200000000", "2024-12-31", "2024", "-16.533", "-71.567",
    "Cerro Verde mine / Arequipa (TRS geography; Cerro Verde pin).",
    "fcx_cerro_verde_trs_20250131",
    "Total Capital Expenditures  $5.2",
    "https://www.fcx.com/sites/fcx/files/documents/operations/TRS-CerroVerde.pdf",
    "Actor: Freeport-McMoRan / Sociedad Minera Cerro Verde — us. NEW LOM sustaining CapEx USD5.2bn from company TRS. Shuffle copper; ≥1/3 U.S. hunt.",
    "hunt_cycle281", investment_type="sustaining_capex", evidence="documented", currency="USD",
    value_usd="5200000000", fx_usd="1", bib_type="company",
    chicago='Freeport-McMoRan Inc. “Technical Report Summary of Mineral Reserves and Mineral Resources for Cerro Verde Mine, Arequipa, Peru.” Effective date December 31, 2024; report date January 31, 2025. https://www.fcx.com/sites/fcx/files/documents/operations/TRS-CerroVerde.pdf.',
    annotation="Freeport Cerro Verde LOM sustaining CapEx USD5.2bn TRS. Supports fcx_cerro_verde_lom_sustaining_5p2bn_2024.",
    evid_note="Opened FCX Cerro Verde TRS PDF (effective 31 Dec 2024); Total Capital Expenditures $5.2bn confirmed.",
)

# 2. copper / us — NEW Freeport Cerro Verde Mine CapEx USD1.7bn (TRS nested)
row_doc(
    "fcx_cerro_verde_mine_capex_1p7bn_2024",
    "resources", "copper", "us",
    "Freeport-McMoRan / Cerro Verde — Mine CapEx USD1.7bn (LOM)",
    "Peru",
    "31 Jan 2025 Freeport Cerro Verde TRS (effective 31 Dec 2024): capital cost table Mine USD 1.7 billion within LOM total USD 5.2bn. CapEx: enter USD1.7bn Mine face. Nested vs fcx_cerro_verde_lom_sustaining_5p2bn_2024 total (not additive).",
    "1700000000", "2024-12-31", "2024", "-16.533", "-71.567",
    "Cerro Verde mine / Arequipa (TRS geography; Cerro Verde pin).",
    "fcx_cerro_verde_trs_20250131",
    "Mine  $1.7",
    "https://www.fcx.com/sites/fcx/files/documents/operations/TRS-CerroVerde.pdf",
    "Actor: Freeport-McMoRan / Cerro Verde — us. NEW nested Mine CapEx USD1.7bn. Shuffle copper; ≥1/3 U.S. hunt.",
    "hunt_cycle281", investment_type="sustaining_capex", evidence="documented", currency="USD",
    value_usd="1700000000", fx_usd="1", bib_type="company",
    chicago='Freeport-McMoRan Inc. “Technical Report Summary of Mineral Reserves and Mineral Resources for Cerro Verde Mine, Arequipa, Peru.” Effective date December 31, 2024; report date January 31, 2025. https://www.fcx.com/sites/fcx/files/documents/operations/TRS-CerroVerde.pdf.',
    annotation="Freeport Cerro Verde Mine CapEx USD1.7bn TRS nested. Supports fcx_cerro_verde_mine_capex_1p7bn_2024.",
    evid_note="Opened FCX Cerro Verde TRS PDF; Mine CapEx $1.7bn confirmed.",
)

# 3. copper / us — NEW Freeport Cerro Verde Supporting Infra/Env CapEx USD2.4bn (TRS nested)
row_doc(
    "fcx_cerro_verde_infra_env_capex_2p4bn_2024",
    "resources", "copper", "us",
    "Freeport-McMoRan / Cerro Verde — Supporting Infrastructure & Environmental CapEx USD2.4bn (LOM)",
    "Peru",
    "31 Jan 2025 Freeport Cerro Verde TRS (effective 31 Dec 2024): capital cost table Supporting Infrastructure and Environmental USD 2.4 billion within LOM total USD 5.2bn (notably TSF and leach-pad capacity). CapEx: enter USD2.4bn supporting face. Nested vs fcx_cerro_verde_lom_sustaining_5p2bn_2024 total (not additive).",
    "2400000000", "2024-12-31", "2024", "-16.533", "-71.567",
    "Cerro Verde supporting infrastructure / Arequipa (TRS geography; Cerro Verde pin).",
    "fcx_cerro_verde_trs_20250131",
    "Supporting Infrastructure and Environmental   2.4",
    "https://www.fcx.com/sites/fcx/files/documents/operations/TRS-CerroVerde.pdf",
    "Actor: Freeport-McMoRan / Cerro Verde — us. NEW nested Supporting Infra/Env CapEx USD2.4bn. Shuffle copper; ≥1/3 U.S. hunt.",
    "hunt_cycle281", investment_type="sustaining_capex", evidence="documented", currency="USD",
    value_usd="2400000000", fx_usd="1", bib_type="company",
    chicago='Freeport-McMoRan Inc. “Technical Report Summary of Mineral Reserves and Mineral Resources for Cerro Verde Mine, Arequipa, Peru.” Effective date December 31, 2024; report date January 31, 2025. https://www.fcx.com/sites/fcx/files/documents/operations/TRS-CerroVerde.pdf.',
    annotation="Freeport Cerro Verde Supporting Infra/Env CapEx USD2.4bn TRS nested. Supports fcx_cerro_verde_infra_env_capex_2p4bn_2024.",
    evid_note="Opened FCX Cerro Verde TRS PDF; Supporting Infrastructure and Environmental CapEx $2.4bn confirmed.",
)

# 4. port_ownership / prc — CapEx-fill COFCO STS11 Santos direct CapEx R$1.64bn
row_doc(
    "cofco_sts11_santos_port_2023",
    "infrastructure", "port_ownership", "prc",
    "COFCO International — STS11 Port of Santos terminal CapEx R$1.64bn direct",
    "Brazil",
    "5 Mar 2025 Folha de S.Paulo: COFCO STS11 terminal at Port of Santos consumed R$ 1.64 billion in direct investment plus R$ 1.2 billion complementary logistics (979 railcars + 23 locomotives). CapEx-fill: enter R$1.64bn direct terminal CapEx face (complementary rolling stock not stored here). Company newsroom CapEx blank / 403 on re-open — UNVERIFIED press proxy quoting company. Nested vs prior CapEx-blank presence row.",
    "1640000000", "2025-03-05", "2025", "-23.95", "-46.30",
    "STS11 / Port of Santos right bank (company / Folha geography; Santos pin).",
    "folha_cofco_sts11_20250305",
    "O terminal consumiu R$ 1,64 bilhão em investimento direto e outro R$ 1,2 bilhão em investimento complementar, em logística, para a compra de 979 vagões e 23 locomotivas.",
    "https://www1.folha.uol.com.br/mercado/2025/03/chinesa-investe-r-284-bi-e-abre-em-marco-novo-terminal-em-santos.shtml",
    "Actor: COFCO International (PRC SOE) — prc. CapEx-fill: R$1.64bn direct terminal CapEx (UNVERIFIED Folha proxy). Shuffle port_ownership; PRC equal-budget.",
    "hunt_cycle281", investment_type="brownfield_expansion", evidence="proxy", currency="BRL",
    value_usd=str(round(1640000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Sá, Nelson de. “Chinesa investe R$ 2,84 bi em novo terminal em Santos.” Folha de S.Paulo, March 5, 2025. https://www1.folha.uol.com.br/mercado/2025/03/chinesa-investe-r-284-bi-e-abre-em-marco-novo-terminal-em-santos.shtml.',
    annotation="COFCO STS11 CapEx-fill R$1.64bn direct via Fed H.10 (UNVERIFIED Folha). Supports cofco_sts11_santos_port_2023.",
    evid_note="Opened Folha 5 Mar 2025; R$1.64bn direct STS11 CapEx quote confirmed for CapEx-fill (company host 403).",
)

# 5. rail / other — NEW Rumo Material Rodante 6M26 R$547m
row_doc(
    "rumo_material_rodante_6m26_547m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Material Rodante CapEx 6M26 R$547m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Material Rodante R$547 million in 6M26 (2T26 R$115m already nested). CapEx: enter R$547m Material Rodante 6M26 face. Nested vs rumo_material_rodante_2t26_115m_brl / rumo_norte_6m26_2988m_brl (not additive).",
    "547000000", "2026-06-30", "2026", "-15.60", "-56.10",
    "Rumo Operação Norte rolling stock (Rondonópolis / Mato Grosso pin).",
    "rumo_2t26_release_20260812",
    "115 64 79,8 % Material Rodante 547 312 75,3 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Material Rodante 6M26 CapEx R$547m. Shuffle rail.",
    "hunt_cycle281", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(547000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Material Rodante 6M26 CapEx R$547m via Fed H.10. Supports rumo_material_rodante_6m26_547m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Material Rodante Capex 6M26 R$547m confirmed.",
)

# 6. rail / other — NEW Rumo Capacitação Malha 6M26 R$949m
row_doc(
    "rumo_capacitacao_6m26_949m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Capacitação Malha Ferroviária CapEx 6M26 R$949m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Capacitação Malha Ferroviária R$949 million in 6M26 (2T26 R$483m already nested). CapEx: enter R$949m Capacitação 6M26 face. Nested vs rumo_capacitacao_2t26_483m_brl / rumo_expansao_norte_6m26_2207m_brl (not additive).",
    "949000000", "2026-06-30", "2026", "-15.60", "-56.10",
    "Rumo Operação Norte track capacity works (Rondonópolis / Mato Grosso pin).",
    "rumo_2t26_release_20260812",
    "483 321 50,4 % Capacitação Malha Ferroviária 949 958 -0,9 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Capacitação Malha 6M26 CapEx R$949m. Shuffle rail.",
    "hunt_cycle281", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(949000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Capacitação Malha 6M26 CapEx R$949m via Fed H.10. Supports rumo_capacitacao_6m26_949m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Capacitação Malha Capex 6M26 R$949m confirmed.",
)

# 7. rail / other — NEW Rumo Ferrovia do Mato Grosso 6M26 R$671m
row_doc(
    "rumo_fmt_6m26_671m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Ferrovia do Mato Grosso CapEx 6M26 R$671m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Ferrovia do Mato Grosso R$671 million in 6M26 (2T26 R$342m already nested). CapEx: enter R$671m FMT 6M26 face. Nested vs rumo_fmt_2t26_342m_brl / rumo_norte_6m26_2988m_brl (not additive).",
    "671000000", "2026-06-30", "2026", "-15.60", "-56.10",
    "Ferrovia do Mato Grosso (Rondonópolis / Mato Grosso pin).",
    "rumo_2t26_release_20260812",
    "342 468 -26,9 % Ferrovia do Mato Grosso 671 821 -18,2 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested FMT 6M26 CapEx R$671m. Shuffle rail.",
    "hunt_cycle281", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(671000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo FMT 6M26 CapEx R$671m via Fed H.10. Supports rumo_fmt_6m26_671m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Ferrovia do Mato Grosso Capex 6M26 R$671m confirmed.",
)

# 8. rail / other — NEW Rumo Operação Sul 6M26 R$343m
row_doc(
    "rumo_sul_6m26_343m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Sul CapEx 6M26 R$343m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Sul R$343 million in 6M26 (2T26 R$183m already nested; all recurring). CapEx: enter R$343m Sul 6M26 face. Nested vs rumo_sul_2t26_183m_brl / rumo_6m26_capex_3371m_brl (not additive).",
    "343000000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Rumo Malha Sul / Paranaguá–São Francisco corridor (Curitiba pin).",
    "rumo_2t26_release_20260812",
    "183 192 -4,8 % Operação Sul 343 371 -7,6 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Operação Sul 6M26 CapEx R$343m. Shuffle rail.",
    "hunt_cycle281", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(343000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Sul 6M26 CapEx R$343m via Fed H.10. Supports rumo_sul_6m26_343m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Operação Sul Capex 6M26 R$343m confirmed.",
)

# 9. water / other — NEW Aegea Corsan 6M26 R$845m
row_doc(
    "aegea_corsan_6m26_845m_brl",
    "resources", "water", "other",
    "Aegea — Corsan Capex 6M26 R$845m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Corsan R$845 million in 6M26 (2T26 R$484m already nested). CapEx: enter R$845m Corsan 6M26 face. Nested vs aegea_corsan_2t26_484m_brl / ecosystem Capex (not additive).",
    "845000000", "2026-06-30", "2026", "-30.03", "-51.23",
    "Corsan / Rio Grande do Sul sanitation (Porto Alegre pin).",
    "aegea_2t26_6m26_release_mziq",
    "Corsan 484 428 13,1% 845 836 1,1%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Corsan 6M26 Capex R$845m. Shuffle water.",
    "hunt_cycle281", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(845000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Corsan 6M26 Capex R$845m via Fed H.10. Supports aegea_corsan_6m26_845m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Corsan Capex 6M26 R$845m confirmed.",
)

# 10. water / other — NEW Aegea Águas do Rio 6M26 R$663m
row_doc(
    "aegea_aguas_do_rio_6m26_663m_brl",
    "resources", "water", "other",
    "Aegea — Águas do Rio Capex 6M26 R$663m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Águas do Rio R$663 million in 6M26 (2T26 R$347m already nested). CapEx: enter R$663m Águas do Rio 6M26 face. Nested vs aegea_aguas_do_rio_2t26_347m_brl / ecosystem Capex (not additive).",
    "663000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Águas do Rio concessions / Rio de Janeiro metro (Rio pin).",
    "aegea_2t26_6m26_release_mziq",
    "Águas do Rio 347 291 19,4% 663 588 12,8%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Águas do Rio 6M26 Capex R$663m. Shuffle water.",
    "hunt_cycle281", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(663000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Águas do Rio 6M26 Capex R$663m via Fed H.10. Supports aegea_aguas_do_rio_6m26_663m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Águas do Rio Capex 6M26 R$663m confirmed.",
)

# 11. water / other — NEW Aegea Novas Operações 6M26 R$339m
row_doc(
    "aegea_novas_operacoes_6m26_339m_brl",
    "resources", "water", "other",
    "Aegea — Novas Operações Capex 6M26 R$339m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Novas Operações R$339 million in 6M26 (2T26 R$186m already nested). CapEx: enter R$339m Novas Operações 6M26 face. Nested vs aegea_novas_operacoes_2t26_186m_brl / ecosystem Capex (not additive).",
    "339000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Aegea new operations CapEx (São Paulo HQ pin).",
    "aegea_2t26_6m26_release_mziq",
    "Novas Operações 186 19 872,8% 339 19 1673,6%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Novas Operações 6M26 Capex R$339m. Shuffle water.",
    "hunt_cycle281", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(339000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Novas Operações 6M26 Capex R$339m via Fed H.10. Supports aegea_novas_operacoes_6m26_339m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Novas Operações Capex 6M26 R$339m confirmed.",
)

# 12. water / other — NEW Aegea PPPs 6M26 R$475m
row_doc(
    "aegea_ppps_6m26_475m_brl",
    "resources", "water", "other",
    "Aegea — PPPs Capex 6M26 R$475m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table PPPs R$475 million in 6M26 (2T26 R$237m already nested). CapEx: enter R$475m PPPs 6M26 face. Nested vs aegea_ppps_2t26_237m_brl / ecosystem Capex (not additive).",
    "475000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Aegea PPP sanitation contracts (São Paulo HQ pin).",
    "aegea_2t26_6m26_release_mziq",
    "PPPs 237 348 -31,8% 475 592 -19,8%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested PPPs 6M26 Capex R$475m. Shuffle water.",
    "hunt_cycle281", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(475000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea PPPs 6M26 Capex R$475m via Fed H.10. Supports aegea_ppps_6m26_475m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; PPPs Capex 6M26 R$475m confirmed.",
)


def upsert_bib(bib, bib_by, entry):
    sid = entry["id"]
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
    print(f"cycle281 added {len(added)}: {added}")
    print(f"cycle281 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
