#!/usr/bin/env python3
"""Cycle 282 hunt: shuffle_seed=20261282; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261282).shuffle):
lithium, niobium, balsa, other_renewables, port_cranes, building_materials,
power_plants_grid, engineering_epc, rail, solar, copper, wind, fission_smr,
water, nickel, graphite, bridges_roads, port_ownership.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Freeport Cerro Verde Concentrator CapEx USD1.1bn
  (TRS nested); Ormat/Wabtec/Progress/Equinix/SSA Guaymas/Seven Seas CapEx blanks;
  EXIM/USTDA probes; SCCO SEC opened (Grupo Mexico majority → other, not us).
PRC equal-budget: NEW CPFL Transmissão Rio Grande do Sul ~R$3.9bn 2025–2029
  (Jornal do Comércio proxy quoting company); NEW COFCO STS11 complementary
  rolling-stock CapEx R$1.2bn (Folha proxy).
Other: NEW Rumo Norte Recorrente / Contêiner / Porto e Terminais 6M26;
  Aegea Manaus / Teresina / Prolagos / Demais Concessões 6M26;
  Southern Copper 6M26 CapEx USD864.7m (SEC company; LatAm Peru+Mexico ops).
Skipped: thin dry; ENGIE Colibri 403; Ascenty 403; Alupar TECP CapEx absent;
  holdovers unsigned.
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


# 1. copper / us — NEW Freeport Cerro Verde Concentrator CapEx USD1.1bn (TRS nested)
row_doc(
    "fcx_cerro_verde_concentrator_1p1bn_2024",
    "resources", "copper", "us",
    "Freeport-McMoRan / Cerro Verde — Concentrator CapEx USD1.1bn (LOM)",
    "Peru",
    "31 Jan 2025 Freeport Cerro Verde TRS (effective 31 Dec 2024): capital cost table Concentrator USD 1.1 billion within LOM total USD 5.2bn. CapEx: enter USD1.1bn Concentrator face. Nested vs fcx_cerro_verde_lom_sustaining_5p2bn_2024 / Mine USD1.7bn / Supporting Infra USD2.4bn (not additive).",
    "1100000000", "2024-12-31", "2024", "-16.533", "-71.567",
    "Cerro Verde concentrator / Arequipa (TRS geography; Cerro Verde pin).",
    "fcx_cerro_verde_trs_20250131",
    "Concentrator  1.1",
    "https://www.fcx.com/sites/fcx/files/documents/operations/TRS-CerroVerde.pdf",
    "Actor: Freeport-McMoRan / Cerro Verde — us. NEW nested Concentrator CapEx USD1.1bn. Shuffle copper; ≥1/3 U.S. hunt.",
    "hunt_cycle282", investment_type="sustaining_capex", evidence="documented", currency="USD",
    value_usd="1100000000", fx_usd="1", bib_type="company",
    chicago='Freeport-McMoRan Inc. “Technical Report Summary of Mineral Reserves and Mineral Resources for Cerro Verde Mine, Arequipa, Peru.” Effective date December 31, 2024; report date January 31, 2025. https://www.fcx.com/sites/fcx/files/documents/operations/TRS-CerroVerde.pdf.',
    annotation="Freeport Cerro Verde Concentrator CapEx USD1.1bn TRS nested. Supports fcx_cerro_verde_concentrator_1p1bn_2024.",
    evid_note="Opened FCX Cerro Verde TRS PDF; Concentrator CapEx $1.1bn confirmed.",
)

# 2. power_plants_grid / prc — NEW CPFL Transmissão RS ~R$3.9bn 2025–2029
row_doc(
    "cpfl_tx_rs_3p9bn_2025_2029",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — Rio Grande do Sul transmission CapEx ~R$3.9bn 2025–2029",
    "Brazil",
    "24 Apr 2025 Jornal do Comércio: CPFL Transmissão projects approximately R$ 3.9 billion investment in Rio Grande do Sul transmission system for 2025–2029 (substation modernization, fleet, capacity expansion, equipment replacement); 2025 planned disbursement R$638m; Nova Prata 2 modernization ~R$78m. CapEx: enter R$3.9bn cycle floor. Nested vs cpfl_tx_2026_2030_4540m_brl national TX plan (RS subset; not additive). UNVERIFIED press proxy quoting company.",
    "3900000000", "2025-04-24", "2025", "-30.03", "-51.23",
    "CPFL Transmissão Rio Grande do Sul system (Porto Alegre / Canoas pin).",
    "jornal_comercio_cpfl_tx_rs_20250424",
    "a companhia projeta um aporte de aproximadamente R$ 3,9 bilhões no período",
    "https://www.jornaldocomercio.com/economia/2025/04/1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html",
    "Actor: CPFL Transmissão (State Grid–controlled CPFL) — prc. NEW ~R$3.9bn RS TX cycle (UNVERIFIED press proxy). Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle282", investment_type="corporate_capex", evidence="proxy", currency="BRL",
    value_usd=str(round(3900000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Klein, Jefferson. “CPFL investirá R$ 3,9 bilhões no sistema gaúcho de transmissão até 2029.” Jornal do Comércio, April 24, 2025. https://www.jornaldocomercio.com/economia/2025/04/1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html.',
    annotation="CPFL TX RS ~R$3.9bn 2025–2029 via Fed H.10 (UNVERIFIED press). Supports cpfl_tx_rs_3p9bn_2025_2029.",
    evid_note="Opened Jornal do Comércio 24 Apr 2025; ~R$3.9bn RS TX CapEx quote confirmed.",
)

# 3. rail / prc — NEW COFCO STS11 complementary rolling stock R$1.2bn
row_doc(
    "cofco_sts11_rolling_stock_1p2bn_2025",
    "infrastructure", "rail", "prc",
    "COFCO International — STS11 complementary logistics CapEx R$1.2bn (979 wagons + 23 locomotives)",
    "Brazil",
    "5 Mar 2025 Folha de S.Paulo: COFCO STS11 complementary logistics investment R$ 1.2 billion for purchase of 979 railcars and 23 locomotives (alongside R$1.64bn direct terminal CapEx already CapEx-filled). CapEx: enter R$1.2bn rolling-stock face. Nested vs cofco_sts11_santos_port_2023 direct terminal (not additive). UNVERIFIED Folha proxy quoting company.",
    "1200000000", "2025-03-05", "2025", "-23.95", "-46.30",
    "COFCO STS11 rail logistics / Port of Santos corridor (Santos pin).",
    "folha_cofco_sts11_20250305",
    "O terminal consumiu R$ 1,64 bilhão em investimento direto e outro R$ 1,2 bilhão em investimento complementar, em logística, para a compra de 979 vagões e 23 locomotivas.",
    "https://www1.folha.uol.com.br/mercado/2025/03/chinesa-investe-r-284-bi-e-abre-em-marco-novo-terminal-em-santos.shtml",
    "Actor: COFCO International — prc. NEW complementary rolling-stock CapEx R$1.2bn (UNVERIFIED Folha proxy). Shuffle rail; PRC equal-budget.",
    "hunt_cycle282", investment_type="equipment_supply", evidence="proxy", currency="BRL",
    value_usd=str(round(1200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Sá, Nelson de. “Chinesa investe R$ 2,84 bi em novo terminal em Santos.” Folha de S.Paulo, March 5, 2025. https://www1.folha.uol.com.br/mercado/2025/03/chinesa-investe-r-284-bi-e-abre-em-marco-novo-terminal-em-santos.shtml.',
    annotation="COFCO STS11 rolling stock R$1.2bn via Fed H.10 (UNVERIFIED Folha). Supports cofco_sts11_rolling_stock_1p2bn_2025.",
    evid_note="Opened Folha 5 Mar 2025; R$1.2bn complementary wagons/locomotives CapEx quote confirmed.",
)

# 4. copper / other — NEW Southern Copper 6M26 CapEx USD864.7m
row_doc(
    "southern_copper_6m26_capex_864p7m_usd",
    "resources", "copper", "other",
    "Southern Copper — 6M26 capital investments USD864.7m",
    "Peru",
    "21 Jul 2026 Southern Copper Corp. 2Q26 earnings release (SEC exhibit): capital investments USD 864.7 million in first half 2026 (2Q26 USD 422.8m); company operates mining units in Peru and Mexico (both LatAm). CapEx: enter USD864.7m 6M26 face. Distinct from Tía María USD1.8bn / notes USD1.25bn / El Pilar / Ilo rows (not additive envelopes).",
    "864700000", "2026-06-30", "2026", "-16.62", "-71.87",
    "Southern Copper LatAm ops (Peru Toquepala/Cuajone pin; Mexico also in scope).",
    "scco_2q26_ex99_20260721",
    "In the first half of the year, we spent $864.7 million on capital investments",
    "https://www.sec.gov/Archives/edgar/data/1001838/000110465926085515/scco-20260721xex99d1.htm",
    "Actor: Southern Copper (Grupo Mexico majority) — other. NEW 6M26 CapEx USD864.7m. Shuffle copper.",
    "hunt_cycle282", investment_type="corporate_capex", evidence="documented", currency="USD",
    value_usd="864700000", fx_usd="1", bib_type="company",
    chicago='Southern Copper Corporation. “Southern Copper Corporation Reports 2Q26 Results” (SEC Exhibit 99.1). July 21, 2026. https://www.sec.gov/Archives/edgar/data/1001838/000110465926085515/scco-20260721xex99d1.htm.',
    annotation="Southern Copper 6M26 CapEx USD864.7m SEC. Supports southern_copper_6m26_capex_864p7m_usd.",
    evid_note="Opened SCCO 2Q26 SEC Exhibit 99.1; 6M26 capital investments $864.7m confirmed.",
)

# 5. rail / other — NEW Rumo Norte Recorrente 6M26 R$780m
row_doc(
    "rumo_norte_recorrente_6m26_780m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Norte Recorrente CapEx 6M26 R$780m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Norte Recorrente R$780 million in 6M26 (2T26 R$415m already nested). CapEx: enter R$780m Norte Recorrente 6M26 face. Nested vs rumo_norte_recorrente_2t26_415m_brl / rumo_norte_6m26_2988m_brl (not additive).",
    "780000000", "2026-06-30", "2026", "-15.60", "-56.10",
    "Rumo Operação Norte recurring CapEx (Rondonópolis / Mato Grosso pin).",
    "rumo_2t26_release_20260812",
    "415 305 35,9 % Recorrente 780 592 31,9 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Norte Recorrente 6M26 CapEx R$780m. Shuffle rail.",
    "hunt_cycle282", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(780000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Norte Recorrente 6M26 CapEx R$780m via Fed H.10. Supports rumo_norte_recorrente_6m26_780m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Norte Recorrente Capex 6M26 R$780m confirmed.",
)

# 6. rail / other — NEW Rumo Operação Contêiner 6M26 R$40m
row_doc(
    "rumo_conteiner_6m26_40m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Contêiner CapEx 6M26 R$40m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Contêiner R$40 million in 6M26 (2T26 R$21m already nested). CapEx: enter R$40m Contêiner 6M26 face. Nested vs rumo_conteiner_2t26_21m_brl / rumo_6m26_capex_3371m_brl (not additive).",
    "40000000", "2026-06-30", "2026", "-23.95", "-46.30",
    "Rumo/Brado container ops (Santos corridor pin).",
    "rumo_2t26_release_20260812",
    "21 17 25,4 % Operação Contêiner 40 22 83,6 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Contêiner 6M26 CapEx R$40m. Shuffle rail.",
    "hunt_cycle282", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(40000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Contêiner 6M26 CapEx R$40m via Fed H.10. Supports rumo_conteiner_6m26_40m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Operação Contêiner Capex 6M26 R$40m confirmed.",
)

# 7. port_ownership / other — NEW Rumo Capacitação Porto e Terminais 6M26 R$41m
row_doc(
    "rumo_porto_terminais_6m26_41m_brl",
    "infrastructure", "port_ownership", "other",
    "Rumo — Capacitação Porto e Terminais CapEx 6M26 R$41m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Capacitação Porto e Terminais R$41 million in 6M26 (2T26 R$39m already nested; Pera de Outeiros / Porto de Santos cited). CapEx: enter R$41m Porto e Terminais 6M26 face. Nested vs rumo_porto_terminais_2t26_39m_brl (not additive).",
    "41000000", "2026-06-30", "2026", "-23.95", "-46.30",
    "Rumo Porto de Santos terminals / Pera de Outeiros (Santos pin).",
    "rumo_2t26_release_20260812",
    "39 28 40,6 % Capacitação Porto e Terminais 41 99 -59,0 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Porto e Terminais 6M26 CapEx R$41m. Shuffle port_ownership.",
    "hunt_cycle282", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(41000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Porto e Terminais 6M26 CapEx R$41m via Fed H.10. Supports rumo_porto_terminais_6m26_41m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Capacitação Porto e Terminais Capex 6M26 R$41m confirmed.",
)

# 8. water / other — NEW Aegea Manaus 6M26 R$164m
row_doc(
    "aegea_manaus_6m26_164m_brl",
    "resources", "water", "other",
    "Aegea — Manaus Capex 6M26 R$164m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Manaus R$164 million in 6M26 (2T26 R$91m already nested). CapEx: enter R$164m Manaus 6M26 face. Nested vs aegea_manaus_2t26_91m_brl / ecosystem Capex (not additive).",
    "164000000", "2026-06-30", "2026", "-3.12", "-60.02",
    "Águas de Manaus sanitation concession (Manaus pin).",
    "aegea_2t26_6m26_release_mziq",
    "Manaus 91 111 -18,1% 164 221 -25,6%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Manaus 6M26 Capex R$164m. Shuffle water.",
    "hunt_cycle282", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(164000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Manaus 6M26 Capex R$164m via Fed H.10. Supports aegea_manaus_6m26_164m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Manaus Capex 6M26 R$164m confirmed.",
)

# 9. water / other — NEW Aegea Teresina 6M26 R$82m
row_doc(
    "aegea_teresina_6m26_82m_brl",
    "resources", "water", "other",
    "Aegea — Teresina Capex 6M26 R$82m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Teresina R$82 million in 6M26 (2T26 R$38m already nested). CapEx: enter R$82m Teresina 6M26 face. Nested vs aegea_teresina_2t26_38m_brl / ecosystem Capex (not additive).",
    "82000000", "2026-06-30", "2026", "-5.09", "-42.80",
    "Águas de Teresina sanitation concession (Teresina pin).",
    "aegea_2t26_6m26_release_mziq",
    "Teresina 38 41 -7,5% 82 91 -9,7%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Teresina 6M26 Capex R$82m. Shuffle water.",
    "hunt_cycle282", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(82000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Teresina 6M26 Capex R$82m via Fed H.10. Supports aegea_teresina_6m26_82m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Teresina Capex 6M26 R$82m confirmed.",
)

# 10. water / other — NEW Aegea Prolagos 6M26 R$69m
row_doc(
    "aegea_prolagos_6m26_69m_brl",
    "resources", "water", "other",
    "Aegea — Prolagos Capex 6M26 R$69m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Prolagos R$69 million in 6M26 (2T26 R$39m already nested). CapEx: enter R$69m Prolagos 6M26 face. Nested vs aegea_prolagos_2t26_39m_brl / ecosystem Capex (not additive).",
    "69000000", "2026-06-30", "2026", "-22.88", "-42.02",
    "Prolagos Região dos Lagos RJ concession (Cabo Frio pin).",
    "aegea_2t26_6m26_release_mziq",
    "Prolagos 39 26 49,7% 69 46 49,9%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Prolagos 6M26 Capex R$69m. Shuffle water.",
    "hunt_cycle282", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(69000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Prolagos 6M26 Capex R$69m via Fed H.10. Supports aegea_prolagos_6m26_69m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Prolagos Capex 6M26 R$69m confirmed.",
)

# 11. water / other — NEW Aegea Demais Concessões 6M26 R$682m
row_doc(
    "aegea_demais_6m26_682m_brl",
    "resources", "water", "other",
    "Aegea — Demais Concessões Capex 6M26 R$682m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Demais Concessões R$682 million in 6M26 (2T26 R$356m already nested). CapEx: enter R$682m Demais 6M26 face. Nested vs aegea_demais_2t26_356m_brl / ecosystem Capex (not additive).",
    "682000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Aegea remaining concessions CapEx (São Paulo HQ pin).",
    "aegea_2t26_6m26_release_mziq",
    "Demais Concessões 356 204 74,5% 682 348 96,0%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Demais Concessões 6M26 Capex R$682m. Shuffle water.",
    "hunt_cycle282", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(682000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Demais 6M26 Capex R$682m via Fed H.10. Supports aegea_demais_6m26_682m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Demais Concessões Capex 6M26 R$682m confirmed.",
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
    print(f"cycle282 added {len(added)}: {added}")
    print(f"cycle282 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
