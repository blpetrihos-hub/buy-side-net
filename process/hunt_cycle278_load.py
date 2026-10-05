#!/usr/bin/env python3
"""Cycle 278 hunt: shuffle_seed=20261278; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261278).shuffle):
balsa, other_renewables, graphite, fission_smr, niobium, solar, water,
building_materials, nickel, power_plants_grid, engineering_epc, copper, lithium,
bridges_roads, rail, port_cranes, port_ownership, wind.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes Wind Chile allocated-through-June-2025
  US$4.93m + NEW Wind Chile June 2026 report add US$5.47m.
PRC equal-budget: NEW CPFL 2T26 Dist soft ~R$1.2bn (~80% of R$1.5bn 2T26 CapEx).
Allied: NEW Neoenergia Networks 2Q26 R$2,063m + Gen+Customers 2Q26 R$29m.
Other: NEW Equatorial Projetos Estratégicos R$46m; Copel DisCo 1S26 R$917.7m +
  GeT 1S26 R$617.7m; Aegea Brusque outorga R$50m + Piauí outorga 6M26 R$22m.
Skipped: thin dry; ENGIE Colibri host 403; Ascenty 403; Alupar TECP unsigned;
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


# 1. other_renewables / us — NEW AES Andes Wind Chile through June 2025 US$4.93m
row_doc(
    "aes_andes_green_wind_chile_jun2025_4p9m",
    "energy", "other_renewables", "us",
    "AES Andes — Wind Chile allocated through June 2025 report US$4.93m",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report allocation table: Wind Chile Amount allocated in June 2025 report = US$4,929,433 (before June 2026 report add US$5,466,362 to reach total US$10,395,795). CapEx/financing: enter USD4.93m June 2025 Wind Chile face. Nested vs aes_andes_green_wind_chile_10p4m total (not additive).",
    "4929433", "2025-06-30", "2025", "-37.47", "-72.35",
    "AES Andes Chile wind green-eligible projects (Biobío regional pin).",
    "aes_andes_green_impact_530m_202606",
    "Wind Chile 4,929,433     5,466,362     10,395,795",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW Wind Chile June 2025 allocated US$4.93m. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle278", investment_type="financing", evidence="documented", currency="USD",
    value_usd="4929433", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes Wind Chile June 2025 allocated US$4.93m. Supports aes_andes_green_wind_chile_jun2025_4p9m.",
    evid_note="Opened AES Andes June 2026 Green Bond Impact Report PDF; Wind Chile June 2025 allocated US$4,929,433 confirmed.",
)

# 2. other_renewables / us — NEW AES Andes Wind Chile June 2026 report add US$5.47m
row_doc(
    "aes_andes_green_wind_chile_added_5p5m",
    "energy", "other_renewables", "us",
    "AES Andes — Wind Chile June 2026 report-window add US$5.47m",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report allocation table: Wind Chile Amount allocated June 2026 report = US$5,466,362 (incremental in report window). CapEx/financing: enter USD5.47m Wind Chile add face. Nested vs aes_andes_green_wind_chile_10p4m total and jun2025 snapshot (not additive).",
    "5466362", "2026-03-31", "2026", "-37.47", "-72.35",
    "AES Andes Chile wind green-eligible projects (Biobío regional pin).",
    "aes_andes_green_impact_530m_202606",
    "Wind Chile 4,929,433     5,466,362     10,395,795",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW Wind Chile June 2026 report add US$5.47m. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle278", investment_type="financing", evidence="documented", currency="USD",
    value_usd="5466362", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes Wind Chile June 2026 report add US$5.47m. Supports aes_andes_green_wind_chile_added_5p5m.",
    evid_note="Opened AES Andes June 2026 Green Bond Impact Report PDF; Wind Chile June 2026 report add US$5,466,362 confirmed.",
)

# 3. power_plants_grid / prc — NEW CPFL 2T26 Dist soft ~R$1.2bn
row_doc(
    "cpfl_2t26_dist_soft_1200m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia — 2T26 Dist CapEx soft ~R$1.2bn",
    "Brazil",
    "13 Aug 2026 CPFL Energia company news: CapEx R$1.5 billion in 2T26; cerca de 80% of resources directed to distribution (same soft share applied to quarterly CapEx). Soft Dist ≈80% of R$1.5bn ≈ R$1.2bn. CapEx: enter soft ~R$1.2bn 2T26 Dist face. Nested vs cpfl_2t26_capex_1p5bn_brl / cpfl_1h26_dist_2240m_brl (not additive).",
    "1200000000", "2026-06-30", "2026", "-22.91", "-47.06",
    "CPFL Energia Brazil distribution footprint (Campinas HQ pin).",
    "cpfl_2t26_1h26_2p8bn",
    "Os investimentos (CAPEX) somaram R$ 1,5 bilhão no trimestre, totalizando R$ 2,8 bilhões no acumulado do ano. Cerca de 80% dos recursos foram direcionados à",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213",
    "Actor: CPFL Energia (State Grid–controlled) — prc. NEW soft ~R$1.2bn 2T26 Dist (~80% of R$1.5bn). Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle278", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1200000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia. “CPFL Energia registra lucro de R$ 1,4 bilhão no 2T26.” August 13, 2026. https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213.',
    annotation="CPFL 2T26 Dist soft ~R$1.2bn via Fed H.10. Supports cpfl_2t26_dist_soft_1200m_brl.",
    evid_note="Opened CPFL 2T26 company news; ~80% Dist of R$1.5bn 2T26 implies soft ~R$1.2bn Dist.",
)

# 4. power_plants_grid / allied — NEW Neoenergia Networks 2Q26 CapEx R$2,063m
row_doc(
    "neoenergia_networks_2q26_2063m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — Networks 2Q26 CapEx R$2,063m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release: CAPEX table Networks R$2,063 million in 2Q26 (Distributors R$1,984m + Transmission Lines R$80m already nested). CapEx: enter R$2,063m Networks face. Nested vs neoenergia_dist_2q26_1984m_brl / neoenergia_tx_2q26_80m_brl / neoenergia_6m26_capex_4bn_brl (not additive).",
    "2063000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil Networks footprint (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Networks 2,063        2,736          (25%) 3,913                4,932           (21%)",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Networks 2Q26 CapEx R$2,063m. Shuffle power_plants_grid.",
    "hunt_cycle278", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2063000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Networks 2Q26 CapEx R$2,063m via Fed H.10. Supports neoenergia_networks_2q26_2063m_brl.",
    evid_note="Opened Neoenergia 2Q26/6M26 MZ IQ PDF; Networks Capex 2Q26 R$2,063m confirmed.",
)

# 5. power_plants_grid / allied — NEW Neoenergia Gen+Customers 2Q26 CapEx R$29m
row_doc(
    "neoenergia_gen_customers_2q26_29m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — Generation and Customers 2Q26 CapEx R$29m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release: CAPEX table Generation and Customers R$29 million in 2Q26 (Hydro R$5m + Wind R$17m + Customers R$7m already nested). CapEx: enter R$29m Gen+Customers face. Nested vs neoenergia_gen_customers_6m26_57m_brl (not additive).",
    "29000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil generation and customers segment (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Generation and Customers 29                   55                    (47%) 57                         92                    (38%)",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Gen+Customers 2Q26 CapEx R$29m. Shuffle power_plants_grid.",
    "hunt_cycle278", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(29000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Gen+Customers 2Q26 CapEx R$29m via Fed H.10. Supports neoenergia_gen_customers_2q26_29m_brl.",
    evid_note="Opened Neoenergia 2Q26/6M26 MZ IQ PDF; Generation and Customers Capex 2Q26 R$29m confirmed.",
)

# 6. power_plants_grid / other — NEW Equatorial Projetos Estratégicos 2T26 R$46m
row_doc(
    "equatorial_projetos_estrategicos_2t26_46m_brl",
    "energy", "power_plants_grid", "other",
    "Equatorial — Projetos Estratégicos Dist CapEx R$46m (2T26)",
    "Brazil",
    "12 Aug 2026 Equatorial S.A. 2T26 earnings release: within Dist non-electric CapEx R$134.24m, investimentos em Projetos Estratégicos somaram R$46 milhões. CapEx: enter R$46m Projetos Estratégicos face. Nested vs equatorial_dist_nonelectric_2t26_134m_brl / equatorial_dist_2t26_2527m_brl (not additive).",
    "46000000", "2026-06-30", "2026", "-15.78", "-47.93",
    "Equatorial Brazil distribution footprint (Brasília HQ pin).",
    "equatorial_2t26_release_20260812",
    "Nesta linha, destacam-se os investimentos em Projetos Estratégicos, que somaram R$46 milhões.",
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2",
    "Actor: Equatorial S.A. — other. NEW nested Projetos Estratégicos 2T26 CapEx R$46m. Shuffle power_plants_grid.",
    "hunt_cycle278", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(46000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2.',
    annotation="Equatorial Projetos Estratégicos 2T26 CapEx R$46m via Fed H.10. Supports equatorial_projetos_estrategicos_2t26_46m_brl.",
    evid_note="Opened Equatorial 2T26 MZ IQ PDF; Projetos Estratégicos Capex R$46m confirmed.",
)

# 7. power_plants_grid / other — NEW Copel DisCo 1S26 CapEx R$917.7m
row_doc(
    "copel_disco_1s26_917p7m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — DisCo 1S26 CapEx R$917.7m",
    "Brazil",
    "Copel 2T26 earnings presentation CapEx table (company materials via RI republication): DisCo / Distribuição 1S26 R$917.7 million (2T26 R$479.1m). CapEx: enter R$917.7m DisCo 1S26 face. Nested vs copel_1s26_capex_1538p8m_brl / copel_disco_2026_plan_1940m_brl (not additive).",
    "917700000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Copel Distribuição Paraná concession (Curitiba HQ pin).",
    "copel_2t26_investidor10_1s26",
    "Distribuição 479,1 881,1 (45,6) 917,7 1.477,7 (37,9)",
    "https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/",
    "Actor: Copel — other. NEW nested DisCo 1S26 CapEx R$917.7m. Shuffle power_plants_grid.",
    "hunt_cycle278", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(917700000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel (Companhia Paranaense de Energia). “Destaques 2T26” CapEx table (RI republication). 2026. https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/.',
    annotation="Copel DisCo 1S26 CapEx R$917.7m via Fed H.10. Supports copel_disco_1s26_917p7m_brl.",
    evid_note="Opened Copel 2T26 CapEx presentation PDF; DisCo 1S26 Capex R$917.7m confirmed.",
)

# 8. power_plants_grid / other — NEW Copel GeT 1S26 CapEx R$617.7m
row_doc(
    "copel_get_1s26_617p7m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — GeT 1S26 CapEx R$617.7m",
    "Brazil",
    "Copel 2T26 earnings presentation CapEx table: Transmissão / GenCo (GeT) 1S26 R$617.7 million (2T26 R$476.4m; includes LRCAP investments). CapEx: enter R$617.7m GeT 1S26 face. Nested vs copel_1s26_capex_1538p8m_brl / copel_gen_tx_2026_971p6m_brl (not additive).",
    "617700000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Copel generation and transmission footprint, Paraná (Curitiba HQ pin).",
    "copel_2t26_investidor10_1s26",
    "Transmissão 476,4 92,5 415,0 617,7 173,2 256,6",
    "https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/",
    "Actor: Copel — other. NEW nested GeT 1S26 CapEx R$617.7m. Shuffle power_plants_grid.",
    "hunt_cycle278", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(617700000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel (Companhia Paranaense de Energia). “Destaques 2T26” CapEx table (RI republication). 2026. https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/.',
    annotation="Copel GeT 1S26 CapEx R$617.7m via Fed H.10. Supports copel_get_1s26_617p7m_brl.",
    evid_note="Opened Copel 2T26 CapEx presentation PDF; GeT/Transmissão 1S26 Capex R$617.7m confirmed.",
)

# 9. water / other — NEW Aegea Brusque outorga 2T26 R$50m
row_doc(
    "aegea_brusque_outorga_2t26_50m_brl",
    "resources", "water", "other",
    "Aegea — Brusque outorga 2T26 R$50m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Outorgas breakdown Brusque R$50 million in 2T26 (6M26 R$50m). CapEx/financing: enter R$50m Brusque outorga face. Nested vs aegea_outorgas_2t26_73m_brl / ecosystem Capex (not additive).",
    "50000000", "2026-06-30", "2026", "-27.10", "-48.92",
    "Brusque SC sanitation concession (Brusque pin).",
    "aegea_2t26_6m26_release_mziq",
    "Brusque 50 - N/A 50 - N/A",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Brusque outorga 2T26 R$50m. Shuffle water.",
    "hunt_cycle278", investment_type="financing", evidence="documented", currency="BRL",
    value_usd=str(round(50000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Brusque outorga 2T26 R$50m via Fed H.10. Supports aegea_brusque_outorga_2t26_50m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Brusque outorga 2T26 R$50m confirmed.",
)

# 10. water / other — NEW Aegea Piauí outorga 6M26 R$22m
row_doc(
    "aegea_piaui_outorga_6m26_22m_brl",
    "resources", "water", "other",
    "Aegea — Piauí outorga 6M26 R$22m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Outorgas breakdown Piauí R$22 million in 6M26 (2T26 — / N/A vs 2T25 R$88m). CapEx/financing: enter R$22m Piauí outorga face. Nested vs aegea_outorgas_2t26_73m_brl / aegea_para_outorga_6m26_285m_brl (not additive).",
    "22000000", "2026-06-30", "2026", "-5.09", "-42.80",
    "Águas do Piauí concession (Teresina regional pin).",
    "aegea_2t26_6m26_release_mziq",
    "Piauí - 88 N/A 22 88 -75,1%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Piauí outorga 6M26 R$22m. Shuffle water.",
    "hunt_cycle278", investment_type="financing", evidence="documented", currency="BRL",
    value_usd=str(round(22000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Piauí outorga 6M26 R$22m via Fed H.10. Supports aegea_piaui_outorga_6m26_22m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Piauí outorga 6M26 R$22m confirmed.",
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
    print(f"cycle278 added {len(added)}: {added}")
    print(f"cycle278 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
