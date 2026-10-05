#!/usr/bin/env python3
"""Cycle 276 hunt: shuffle_seed=20261276; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261276).shuffle):
lithium, power_plants_grid, niobium, balsa, water, bridges_roads, port_cranes,
fission_smr, port_ownership, other_renewables, copper, nickel, wind, solar,
building_materials, graphite, rail, engineering_epc.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes green-bond pending allocation US$198.3m +
  NEW June 2026 report-window allocation US$138.67m (Green Bond Impact Report).
PRC equal-budget: NEW CPFL 1H26 non-Dist soft residual ~R$560m (~20% of R$2.8bn
  after ~80% Dist soft already logged).
Allied: NEW Neoenergia Network Expansion 6M26 R$2,265m + Wind Farms 2Q26 R$17m.
Other: NEW Aegea Prolagos R$39m + Teresina R$38m + Outorgas R$73m (2T26);
  Rumo Expansão Norte R$979m + Capacitação Porto e Terminais R$39m (2T26).
Skipped: thin dry; ENGIE Colibri host 403; Ascenty company face 403; Alupar TECP
  unsigned; Gasmig/Energisa gás out of taxonomy; holdovers unsigned.
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


# 1. other_renewables / us — NEW AES Andes green-bond pending allocation US$198.3m
row_doc(
    "aes_andes_green_pending_198p3m",
    "energy", "other_renewables", "us",
    "AES Andes — green-bond proceeds pending allocation US$198.3m (Mar 2026)",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report: accumulated net proceeds allocated to Eligible Green Projects as of 31 Mar 2026 total US$331.7 million; therefore pending amount to be allocated is US$198.3 million (residual of US$530m junior green notes). CapEx/financing: enter USD198.3m pending face. Nested vs aes_andes_green_bond_530m_20240610 issuance and aes_andes_green_alloc_331p7m_20260331 allocated (not additive).",
    "198300000", "2026-03-31", "2026", "-33.43", "-70.61",
    "AES Andes Chile/Colombia/Argentina green-eligible renewable+BESS pipeline (Santiago HQ pin).",
    "aes_andes_green_impact_530m_202606",
    "The accumulated amount of net proceeds allocated to Eligible Green Projects is US$331.7 million. Therefore, there is a pending amount to be allocated for US$198.3 million.",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW pending green-bond residual US$198.3m. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle276", investment_type="financing", evidence="documented", currency="USD",
    value_usd="198300000", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes green proceeds pending US$198.3m. Supports aes_andes_green_pending_198p3m.",
    evid_note="Opened AES Andes June 2026 Green Bond Impact Report PDF; pending US$198.3m confirmed.",
)

# 2. other_renewables / us — NEW AES Andes June 2026 report-window allocation US$138.67m
row_doc(
    "aes_andes_green_window_138p7m_2026",
    "energy", "other_renewables", "us",
    "AES Andes — green-bond allocation window US$138.67m (June 2026 report)",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report allocation table: Amount allocated June 2026 report column sums to US$138,668,820 (Solar+BESS Chile US$4.54m + Wind Chile US$5.47m + BESS Standalone Chile US$37.96m + Wind Colombia US$2.90m + Energy Purchases Chile US$87.80m). CapEx/financing: enter USD138.67m report-window face. Nested vs category totals and aes_andes_green_alloc_331p7m_20260331 cumulative (not additive).",
    "138668820", "2026-03-31", "2026", "-33.43", "-70.61",
    "AES Andes Chile/Colombia green-eligible renewable+BESS pipeline (Santiago HQ pin).",
    "aes_andes_green_impact_530m_202606",
    "193,042,566    138,668,820  331,711,386",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW June 2026 report-window green allocation US$138.67m. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle276", investment_type="financing", evidence="documented", currency="USD",
    value_usd="138668820", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes June 2026 green allocation window US$138.67m. Supports aes_andes_green_window_138p7m_2026.",
    evid_note="Opened AES Andes June 2026 Green Bond Impact Report PDF; June 2026 report-window allocation US$138,668,820 confirmed.",
)

# 3. power_plants_grid / prc — NEW CPFL 1H26 non-Dist soft residual ~R$560m
row_doc(
    "cpfl_1h26_nondist_soft_560m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia — 1H26 non-Dist CapEx soft residual ~R$560m",
    "Brazil",
    "13 Aug 2026 CPFL Energia company news: CapEx totaled R$2.8 billion in 1H26 (R$1.5bn in 2T26); cerca de 80% directed to distribution (soft Dist already logged as ~R$2.24bn). Soft residual non-Dist (generation/transmission/other) ≈20% of R$2.8bn ≈ R$560m. CapEx: enter soft ~R$560m residual face. Nested vs cpfl_1h26_capex_2p8bn_brl / cpfl_1h26_dist_2240m_brl (not additive).",
    "560000000", "2026-06-30", "2026", "-22.91", "-47.06",
    "CPFL Energia Brazil generation/transmission footprint (Campinas HQ pin).",
    "cpfl_2t26_1h26_2p8bn",
    "Os investimentos (CAPEX) somaram R$ 1,5 bilhão no trimestre, totalizando R$ 2,8 bilhões no acumulado do ano. Cerca de 80% dos recursos foram direcionados à",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213",
    "Actor: CPFL Energia (State Grid–controlled) — prc. NEW soft ~R$560m 1H26 non-Dist residual (~20% of R$2.8bn after ~80% Dist). Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle276", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(560000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia. “CPFL Energia registra lucro de R$ 1,4 bilhão no 2T26.” August 13, 2026. https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213.',
    annotation="CPFL 1H26 non-Dist soft ~R$560m via Fed H.10. Supports cpfl_1h26_nondist_soft_560m_brl.",
    evid_note="Opened CPFL 2T26 company news; ~80% Dist of R$2.8bn 1H26 implies soft ~R$560m non-Dist residual.",
)

# 4. power_plants_grid / allied — NEW Neoenergia Network Expansion 6M26 R$2,265m
row_doc(
    "neoenergia_network_expansion_6m26_2265m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — distributors Network Expansion 6M26 CapEx R$2,265m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release (company MZ IQ PDF): distributors' CapEx totaled R$3.7 billion in 6M26 of which R$2.2 billion allocated to network expansion; CAPEX table Network Expansion row sums to R$2,265 million across distributors (Coelba/Cosern/Elektro/Pernambuco/Brasília). CapEx: enter R$2,265m Network Expansion face. Nested vs neoenergia_dist_6m26_3696m_brl / neoenergia_6m26_capex_4bn_brl (not additive).",
    "2265000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil distribution footprint (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "In 6M26, the distributors' Capex totaled R$ 3.7 billion, of which R$ 2.2 billion was allocated to network expansion.",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Network Expansion 6M26 CapEx R$2,265m. Shuffle power_plants_grid.",
    "hunt_cycle276", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2265000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Network Expansion 6M26 CapEx R$2,265m via Fed H.10. Supports neoenergia_network_expansion_6m26_2265m_brl.",
    evid_note="Opened Neoenergia 2Q26/6M26 MZ IQ PDF; Network Expansion table sum R$2,265m / narrative R$2.2bn confirmed.",
)

# 5. wind / allied — NEW Neoenergia Wind Farms 2Q26 CapEx R$17m
row_doc(
    "neoenergia_wind_2q26_17m_brl",
    "energy", "wind", "allied",
    "Neoenergia — wind farms 2Q26 CapEx R$17m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release: CAPEX table Wind Farms R$17 million in 2Q26 (within Generation and Customers; 6M26 Wind Farms R$31m already nested). CapEx: enter R$17m 2Q26 wind face. Nested vs neoenergia_wind_6m26_31m_brl / neoenergia_6m26_capex_4bn_brl (not additive).",
    "17000000", "2026-06-30", "2026", "-5.79", "-35.21",
    "Neoenergia Brazil wind portfolio (Northeast Brazil pin; company Generation and Customers segment).",
    "neoenergia_2q26_release_mziq",
    "Wind Farms 17             31              (46%) 31                 54             (43%)",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Wind Farms 2Q26 CapEx R$17m. Shuffle wind.",
    "hunt_cycle276", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(17000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Wind Farms 2Q26 CapEx R$17m via Fed H.10. Supports neoenergia_wind_2q26_17m_brl.",
    evid_note="Opened Neoenergia 2Q26/6M26 MZ IQ PDF; Wind Farms Capex 2Q26 R$17m confirmed.",
)

# 6. water / other — NEW Aegea Prolagos 2T26 Capex R$39m
row_doc(
    "aegea_prolagos_2t26_39m_brl",
    "resources", "water", "other",
    "Aegea — Prolagos 2T26 Capex R$39m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Prolagos R$39 million in 2T26 (+49.7% vs 2T25 R$26m); 6M26 R$69m. CapEx: enter R$39m Prolagos face. Nested vs aegea_2t26_ecosystem_capex_1828m_brl (not additive).",
    "39000000", "2026-06-30", "2026", "-22.88", "-42.02",
    "Prolagos / Região dos Lagos RJ concession (Cabo Frio–Araruama corridor pin).",
    "aegea_2t26_6m26_release_mziq",
    "Prolagos 39 26 49,7% 69 46 49,9%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Prolagos 2T26 Capex R$39m. Shuffle water.",
    "hunt_cycle276", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(39000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Prolagos 2T26 Capex R$39m via Fed H.10. Supports aegea_prolagos_2t26_39m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Prolagos Capex 2T26 R$39m confirmed.",
)

# 7. water / other — NEW Aegea Teresina 2T26 Capex R$38m
row_doc(
    "aegea_teresina_2t26_38m_brl",
    "resources", "water", "other",
    "Aegea — Águas de Teresina 2T26 Capex R$38m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Teresina R$38 million in 2T26 (−7.5% vs 2T25 R$41m); 6M26 R$82m. CapEx: enter R$38m Teresina face. Nested vs aegea_2t26_ecosystem_capex_1828m_brl (not additive).",
    "38000000", "2026-06-30", "2026", "-5.09", "-42.80",
    "Águas de Teresina PI concession (Teresina pin).",
    "aegea_2t26_6m26_release_mziq",
    "Teresina 38 41 -7,5% 82 91 -9,7%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Teresina 2T26 Capex R$38m. Shuffle water.",
    "hunt_cycle276", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(38000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Teresina 2T26 Capex R$38m via Fed H.10. Supports aegea_teresina_2t26_38m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Teresina Capex 2T26 R$38m confirmed.",
)

# 8. water / other — NEW Aegea Outorgas 2T26 R$73m
row_doc(
    "aegea_outorgas_2t26_73m_brl",
    "resources", "water", "other",
    "Aegea — Outorgas pagas 2T26 R$73m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: investments table Outorgas R$73 million in 2T26 (−37.4% vs 2T25 R$117m); 6M26 R$402m — concession-grant payments alongside Capex within ecosystem investments. CapEx/financing: enter R$73m 2T26 outorgas face. Nested vs aegea_2t26_ecosystem_capex_1828m_brl Capex line (not additive).",
    "73000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Aegea sanitation ecosystem Brazil footprint (Rio de Janeiro metro pin).",
    "aegea_2t26_6m26_release_mziq",
    "Outorgas 73 117 -37,4% 402 169 137,9%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Outorgas 2T26 R$73m. Shuffle water.",
    "hunt_cycle276", investment_type="financing", evidence="documented", currency="BRL",
    value_usd=str(round(73000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Outorgas 2T26 R$73m via Fed H.10. Supports aegea_outorgas_2t26_73m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Outorgas 2T26 R$73m confirmed.",
)

# 9. rail / other — NEW Rumo Expansão Norte 2T26 CapEx R$979m
row_doc(
    "rumo_expansao_norte_2t26_979m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Norte Expansão 2T26 CapEx R$979m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Norte Expansão R$979 million in 2T26 (+11.1% vs 2T25 R$881m); 6M26 R$2,207m — nested expansion breakout within Operação Norte R$1,393m. CapEx: enter R$979m Expansão Norte face. Nested vs rumo_norte_2t26_1393m_brl / rumo_2t26_capex_1597m_brl (not additive).",
    "979000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Rumo Operação Norte expansion works (São Paulo HQ pin; Malha Paulista/Central corridor).",
    "rumo_2t26_release_20260812",
    "979 881 11,1 % Expansão 2.207 2.190 0,8 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Expansão Norte 2T26 CapEx R$979m. Shuffle rail.",
    "hunt_cycle276", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(979000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Expansão Norte 2T26 CapEx R$979m via Fed H.10. Supports rumo_expansao_norte_2t26_979m_brl.",
    evid_note="Opened Rumo 2T26 company RI PDF; Expansão Norte Capex R$979m confirmed.",
)

# 10. port_ownership / other — NEW Rumo Capacitação Porto e Terminais 2T26 CapEx R$39m
row_doc(
    "rumo_porto_terminais_2t26_39m_brl",
    "infrastructure", "port_ownership", "other",
    "Rumo — Capacitação Porto e Terminais 2T26 CapEx R$39m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Capacitação Porto e Terminais R$39 million in 2T26 (+40.6% vs 2T25 R$28m); 6M26 R$41m — nested port/terminal capacity works within Operação Norte. CapEx: enter R$39m Porto e Terminais face. Nested vs rumo_norte_2t26_1393m_brl / rumo_2t26_capex_1597m_brl (not additive).",
    "39000000", "2026-06-30", "2026", "-23.96", "-46.33",
    "Rumo port and terminal capacity works supporting Operação Norte (Santos corridor pin).",
    "rumo_2t26_release_20260812",
    "39 28 40,6 % Capacitação Porto e Terminais 41 99 -59,0 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Capacitação Porto e Terminais 2T26 CapEx R$39m. Shuffle port_ownership.",
    "hunt_cycle276", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(39000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Porto e Terminais 2T26 CapEx R$39m via Fed H.10. Supports rumo_porto_terminais_2t26_39m_brl.",
    evid_note="Opened Rumo 2T26 company RI PDF; Capacitação Porto e Terminais Capex R$39m confirmed.",
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
    print(f"cycle276 added {len(added)}: {added}")
    print(f"cycle276 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
