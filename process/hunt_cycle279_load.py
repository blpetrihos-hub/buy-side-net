#!/usr/bin/env python3
"""Cycle 279 hunt: shuffle_seed=20261279; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261279).shuffle):
niobium, building_materials, solar, water, bridges_roads, engineering_epc, rail,
copper, graphite, fission_smr, other_renewables, wind, port_ownership, balsa,
nickel, lithium, power_plants_grid, port_cranes.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes Solar+BESS Chile June 2026 report add
  US$4.54m (AES/EXIM/USTDA/Progress Rail/Wabtec/Equinix/GE Vernova/DFC/embassy
  probes consumed ≥1/3 subcategory budgets; green-bond nested faces otherwise mined).
PRC equal-budget: NEW CPFL 2T26 non-Dist soft ~R$300m (~20% of R$1.5bn CapEx).
Allied: NEW Neoenergia Networks 6M26 R$3,913m.
Other: NEW Copel DisCo 2T26 R$479.1m + GeT 2T26 R$476.4m + LRCAP 2T26 R$317.9m;
  Aegea Corsan outorga 2T26 R$20m + Demais Concessões outorga 2T26 R$3m;
  Rumo Operação Contêiner 2T26 R$21m; Alupar Custo de Infraestrutura 2T26 R$379.2m.
Skipped: thin dry; ENGIE Colibri host 403; Ascenty 403; Alupar TECP CapEx unsigned
  (LI only); Progress Rail VLI R$430m unsigned; Motiva frota R$50m URL 404;
  Gasmig/Energisa gás out of taxonomy; holdovers unsigned.
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


# 1. solar / us — NEW AES Andes Solar+BESS Chile June 2026 report add US$4.54m
row_doc(
    "aes_andes_green_solar_bess_added_4p5m",
    "energy", "solar", "us",
    "AES Andes — Solar+BESS Chile June 2026 report-window add US$4.54m",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report allocation table: Solar + BESS Chile Amount allocated June 2026 report = US$4,541,556 (incremental in report window after June 2025 allocated US$188,113,133 to reach total US$192,654,689). CapEx/financing: enter USD4.54m Solar+BESS Chile add face. Nested vs aes_andes_green_solar_bess_chile_192p7m total and jun2025 snapshot (not additive).",
    "4541556", "2026-03-31", "2026", "-23.65", "-70.40",
    "AES Andes Chile Solar+BESS green-eligible projects (Antofagasta regional pin).",
    "aes_andes_green_impact_530m_202606",
    "Solar + BESS Chile 188,113,133     4,541,556  192,654,689",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW Solar+BESS Chile June 2026 report add US$4.54m. Shuffle solar; ≥1/3 U.S. hunt.",
    "hunt_cycle279", investment_type="financing", evidence="documented", currency="USD",
    value_usd="4541556", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes Solar+BESS Chile June 2026 report add US$4.54m. Supports aes_andes_green_solar_bess_added_4p5m.",
    evid_note="Opened AES Andes June 2026 Green Bond Impact Report PDF; Solar+BESS Chile June 2026 report add US$4,541,556 confirmed.",
)

# 2. power_plants_grid / prc — NEW CPFL 2T26 non-Dist soft ~R$300m
row_doc(
    "cpfl_2t26_nondist_soft_300m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia — 2T26 soft non-Dist CapEx ~R$300m",
    "Brazil",
    "13 Aug 2026 CPFL Energia company news: CapEx R$1.5 billion in 2T26; cerca de 80% of resources directed to distribution (soft Dist ~R$1.2bn already nested). Soft non-Dist residual ≈20% of R$1.5bn ≈ R$300m (generation/transmission/other). CapEx: enter soft ~R$300m 2T26 non-Dist face. Nested vs cpfl_2t26_capex_1p5bn_brl / cpfl_2t26_dist_soft_1200m_brl / cpfl_1h26_nondist_soft_560m_brl (not additive).",
    "300000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "CPFL Energia Brazil distribution/generation footprint (São Paulo HQ pin).",
    "cpfl_2t26_1h26_2p8bn",
    "Os investimentos (CAPEX) somaram R$ 1,5 bilhão no trimestre… Cerca de 80% dos recursos foram direcionados à distribuição",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213",
    "Actor: CPFL Energia (State Grid–controlled) — prc. NEW soft 2T26 non-Dist ~R$300m. Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle279", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(300000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia. “CPFL Energia registra lucro de R$ 1,4 bilhão no 2T26.” August 13, 2026. https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213.',
    annotation="CPFL 2T26 non-Dist soft ~R$300m via Fed H.10. Supports cpfl_2t26_nondist_soft_300m_brl.",
    evid_note="Opened CPFL 2T26 company news; soft non-Dist residual ~20% of R$1.5bn CapEx confirmed from cerca de 80% Dist share.",
)

# 3. power_plants_grid / allied — NEW Neoenergia Networks 6M26 R$3,913m
row_doc(
    "neoenergia_networks_6m26_3913m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — Networks CapEx 6M26 R$3,913m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release: CAPEX table Networks R$3,913 million in 6M26 (Distributors R$3,696m + Transmission Lines R$218m already nested). CapEx: enter R$3,913m Networks 6M26 face. Nested vs neoenergia_networks_2q26_2063m_brl / neoenergia_dist_6m26_3696m_brl / neoenergia_tx_6m26_218m_brl / neoenergia_6m26_capex_4bn_brl (not additive).",
    "3913000000", "2026-06-30", "2026", "-12.97", "-38.50",
    "Neoenergia Networks Brazil (Recife / Coelba regional pin).",
    "neoenergia_2q26_release_mziq",
    "Networks 2,063        2,736          (25%) 3,913                4,932           (21%)",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Networks 6M26 CapEx R$3,913m. Shuffle power_plants_grid.",
    "hunt_cycle279", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(3913000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Earnings Release 2Q26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Networks 6M26 CapEx R$3,913m via Fed H.10. Supports neoenergia_networks_6m26_3913m_brl.",
    evid_note="Opened Neoenergia 2Q26/6M26 MZ IQ PDF; Networks CapEx 6M26 R$3,913m confirmed.",
)

# 4. power_plants_grid / other — NEW Copel DisCo 2T26 R$479.1m
row_doc(
    "copel_disco_2t26_479p1m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — DisCo CapEx 2T26 R$479.1m",
    "Brazil",
    "Copel 2T26 earnings presentation CapEx table (company materials via RI republication): Copel Distribuição 2T26 R$479.1 million (1S26 R$917.7m already nested). CapEx: enter R$479.1m DisCo 2T26 face. Nested vs copel_disco_1s26_917p7m_brl / copel_2t26_capex_957p2m_brl (not additive).",
    "479100000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Copel Distribuição concession area, Paraná (Curitiba pin).",
    "copel_2t26_investidor10_1s26",
    "Copel Distribuição 479,1 881,1 (45,6) 917,7 1.477,7 (37,9)",
    "https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/",
    "Actor: Copel — other. NEW nested DisCo 2T26 CapEx R$479.1m. Shuffle power_plants_grid.",
    "hunt_cycle279", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(479100000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel (Companhia Paranaense de Energia). “Destaques 2T26” CapEx table (RI republication). 2026. https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/.',
    annotation="Copel DisCo 2T26 CapEx R$479.1m via Fed H.10. Supports copel_disco_2t26_479p1m_brl.",
    evid_note="Opened Copel 2T26 CapEx presentation PDF; Distribuição 2T26 Capex R$479.1m confirmed.",
)

# 5. power_plants_grid / other — NEW Copel GeT 2T26 R$476.4m
row_doc(
    "copel_get_2t26_476p4m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — GeT CapEx 2T26 R$476.4m",
    "Brazil",
    "Copel 2T26 earnings presentation CapEx table: Copel Geração e Transmissão 2T26 R$476.4 million (1S26 R$617.7m already nested; includes LRCAP R$317.9m). CapEx: enter R$476.4m GeT 2T26 face. Nested vs copel_get_1s26_617p7m_brl / copel_2t26_capex_957p2m_brl (not additive).",
    "476400000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Copel Geração e Transmissão assets, Paraná (Curitiba pin).",
    "copel_2t26_investidor10_1s26",
    "Copel Geração e Transmissão 476,4 92,5 415,0 617,7 173,2 256,6",
    "https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/",
    "Actor: Copel — other. NEW nested GeT 2T26 CapEx R$476.4m. Shuffle power_plants_grid.",
    "hunt_cycle279", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(476400000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel (Companhia Paranaense de Energia). “Destaques 2T26” CapEx table (RI republication). 2026. https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/.',
    annotation="Copel GeT 2T26 CapEx R$476.4m via Fed H.10. Supports copel_get_2t26_476p4m_brl.",
    evid_note="Opened Copel 2T26 CapEx presentation PDF; GeT 2T26 Capex R$476.4m confirmed.",
)

# 6. power_plants_grid / other — NEW Copel LRCAP 2T26/1S26 R$317.9m
row_doc(
    "copel_lrcap_2t26_317p9m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — LRCAP spent CapEx 2T26 R$317.9m",
    "Brazil",
    "Copel 2T26 earnings presentation CapEx table: LRCAP R$317.9 million in 2T26 (same 1S26; initial investments to expand installed capacity at UHEs Governador Bento Munhoz / Foz do Areia and Governador Ney Braga / Segredo after 18 Mar 2026 capacity-reserve auction). CapEx: enter R$317.9m LRCAP spent face. Nested vs copel_lrcap_foz_areia_190m_brl_2026 / copel_lrcap_segredo_541m_brl_2026 plan envelopes and copel_get_2t26_476p4m_brl (not additive).",
    "317900000", "2026-06-30", "2026", "-26.00", "-51.60",
    "UHEs Foz do Areia / Segredo LRCAP works, Paraná (Foz do Areia regional pin).",
    "copel_2t26_investidor10_1s26",
    "LRCAP 317,9  — — 317,9  — —",
    "https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/",
    "Actor: Copel — other. NEW nested LRCAP spent 2T26 CapEx R$317.9m. Shuffle power_plants_grid.",
    "hunt_cycle279", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(317900000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel (Companhia Paranaense de Energia). “Destaques 2T26” CapEx table (RI republication). 2026. https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/.',
    annotation="Copel LRCAP 2T26 CapEx R$317.9m via Fed H.10. Supports copel_lrcap_2t26_317p9m_brl.",
    evid_note="Opened Copel 2T26 CapEx presentation PDF; LRCAP Capex 2T26/1S26 R$317.9m confirmed.",
)

# 7. water / other — NEW Aegea Corsan outorga 2T26 R$20m
row_doc(
    "aegea_corsan_outorga_2t26_20m_brl",
    "resources", "water", "other",
    "Aegea — Corsan outorga 2T26 R$20m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Outorgas breakdown Corsan R$20 million in 2T26 (6M26 R$41m). CapEx/financing: enter R$20m Corsan outorga face. Nested vs aegea_corsan_2t26_484m_brl Capex row and aegea_outorgas_2t26_73m_brl (not additive).",
    "20000000", "2026-06-30", "2026", "-30.03", "-51.23",
    "Corsan / Aegea Rio Grande do Sul sanitation concession (Porto Alegre pin).",
    "aegea_2t26_6m26_release_mziq",
    "Corsan 20 30 -31,9% 41 82 -49,8%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Corsan outorga 2T26 R$20m. Shuffle water.",
    "hunt_cycle279", investment_type="financing", evidence="documented", currency="BRL",
    value_usd=str(round(20000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Corsan outorga 2T26 R$20m via Fed H.10. Supports aegea_corsan_outorga_2t26_20m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Corsan outorga 2T26 R$20m confirmed.",
)

# 8. water / other — NEW Aegea Demais Concessões outorga 2T26 R$3m
row_doc(
    "aegea_demais_outorga_2t26_3m_brl",
    "resources", "water", "other",
    "Aegea — Demais Concessões outorga 2T26 R$3m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Outorgas breakdown Demais Concessões R$3 million in 2T26 (6M26 R$3m). CapEx/financing: enter R$3m Demais Concessões outorga face. Nested vs aegea_demais_2t26_356m_brl Capex row and aegea_outorgas_2t26_73m_brl (not additive).",
    "3000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Aegea remaining sanitation concessions (São Paulo HQ pin).",
    "aegea_2t26_6m26_release_mziq",
    "Demais Concessões 3 - N/A 3 - N/A",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Demais Concessões outorga 2T26 R$3m. Shuffle water.",
    "hunt_cycle279", investment_type="financing", evidence="documented", currency="BRL",
    value_usd=str(round(3000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Demais Concessões outorga 2T26 R$3m via Fed H.10. Supports aegea_demais_outorga_2t26_3m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Demais Concessões outorga 2T26 R$3m confirmed.",
)

# 9. rail / other — NEW Rumo Operação Contêiner 2T26 R$21m
row_doc(
    "rumo_conteiner_2t26_21m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Contêiner CapEx 2T26 R$21m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Contêiner R$21 million in 2T26 (+25.4% vs 2T25 R$17m); 6M26 R$40m — nested container-rail CapEx. CapEx: enter R$21m Contêiner 2T26 face. Nested vs rumo_2t26_capex_1597m_brl / rumo_6m26_capex_3371m_brl (not additive).",
    "21000000", "2026-06-30", "2026", "-23.96", "-46.33",
    "Rumo container rail/terminal operations (Santos corridor pin).",
    "rumo_2t26_release_20260812",
    "21 17 25,4 % Operação Contêiner 40 22 83,6 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Operação Contêiner 2T26 CapEx R$21m. Shuffle rail.",
    "hunt_cycle279", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(21000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Contêiner 2T26 CapEx R$21m via Fed H.10. Supports rumo_conteiner_2t26_21m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Operação Contêiner Capex 2T26 R$21m confirmed.",
)

# 10. power_plants_grid / other — NEW Alupar Custo de Infraestrutura 2T26 R$379.2m
row_doc(
    "alupar_2t26_custo_infra_379p2m_brl",
    "energy", "power_plants_grid", "other",
    "Alupar — Custo de Infraestrutura (CapEx) 2T26 R$379.2m",
    "Brazil",
    "6 Aug 2026 Alupar 2T26 earnings release (company ZIP): Custo de Infraestrutura R$379.2 million in 2T26 (+134.6% vs 2T25 R$161.6m); 6M26 R$649.2m already nested. CapEx: enter R$379.2m 2T26 Custo de Infraestrutura face (company IFRS CapEx realized). Nested vs alupar_6m26_custo_infra_649p2m_brl / alupar_2t26_capex_354m_brl Cenário Energia proxy (not additive; company primary supersedes soft press face).",
    "379200000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Alupar transmission portfolio Brazil (São Paulo HQ pin).",
    "alupar_2t26_release_20260806",
    "Custo de Infraestrutura (270,0) (379,2) (161,6) 134,6% (649,2) (325,9) 99,2%",
    "https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip",
    "Actor: Alupar Investimento — other. NEW nested Custo de Infraestrutura 2T26 CapEx R$379.2m. Shuffle power_plants_grid.",
    "hunt_cycle279", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(379200000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Alupar Investimento S.A. “Release de Resultados 2T26” (company ZIP). August 6, 2026. https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip.',
    annotation="Alupar Custo de Infraestrutura 2T26 CapEx R$379.2m via Fed H.10. Supports alupar_2t26_custo_infra_379p2m_brl.",
    evid_note="Opened Alupar 2T26 company ZIP release PDF; Custo de Infraestrutura 2T26 R$379.2m confirmed.",
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
    print(f"cycle279 added {len(added)}: {added}")
    print(f"cycle279 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
