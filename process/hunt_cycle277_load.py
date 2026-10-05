#!/usr/bin/env python3
"""Cycle 277 hunt: shuffle_seed=20261277; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261277).shuffle):
fission_smr, power_plants_grid, building_materials, bridges_roads, water, niobium,
rail, other_renewables, lithium, graphite, balsa, engineering_epc, wind,
port_cranes, port_ownership, nickel, solar, copper.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes green-bond June 2025 report allocated
  snapshot US$193.04m + NEW Solar+BESS Chile allocated-through-June-2025
  US$188.11m (Green Bond Impact Report table).
PRC equal-budget: NEW SGBH P&D/inovação R$8.7m (RS 2025).
Allied: NEW Neoenergia Hydro 2Q26 R$5m + Customers 2Q26 R$7m.
Other: NEW Equatorial Dist non-electric 2T26 R$134.24m; Rumo Material Rodante
  R$115m + FMT R$342m + Norte Recorrente R$415m (2T26); Aegea Pará outorga
  6M26 R$285m.
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


# 1. other_renewables / us — NEW AES Andes June 2025 report allocated snapshot US$193.04m
row_doc(
    "aes_andes_green_alloc_jun2025_193p0m",
    "energy", "other_renewables", "us",
    "AES Andes — green-bond allocated through June 2025 report US$193.04m",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report allocation table: Amount allocated in June 2025 report column totals US$193,042,566 (prior cumulative allocated snapshot before June 2026 report-window adds). CapEx/financing: enter USD193.04m June 2025 report face. Nested vs aes_andes_green_alloc_331p7m_20260331 cumulative and aes_andes_green_window_138p7m_2026 (not additive).",
    "193042566", "2025-06-30", "2025", "-33.43", "-70.61",
    "AES Andes Chile/Colombia/Argentina green-eligible renewable+BESS pipeline (Santiago HQ pin).",
    "aes_andes_green_impact_530m_202606",
    "193,042,566    138,668,820  331,711,386",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW June 2025 report allocated snapshot US$193.04m. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle277", investment_type="financing", evidence="documented", currency="USD",
    value_usd="193042566", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes June 2025 green allocated snapshot US$193.04m. Supports aes_andes_green_alloc_jun2025_193p0m.",
    evid_note="Opened AES Andes June 2026 Green Bond Impact Report PDF; June 2025 report allocated US$193,042,566 confirmed.",
)

# 2. other_renewables / us — NEW AES Andes Solar+BESS Chile through June 2025 US$188.11m
row_doc(
    "aes_andes_green_solar_bess_jun2025_188p1m",
    "energy", "other_renewables", "us",
    "AES Andes — Solar+BESS Chile allocated through June 2025 report US$188.11m",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report allocation table: Solar + BESS Chile Amount allocated in June 2025 report = US$188,113,133 (before June 2026 report add US$4,541,556 to reach total US$192,654,689). CapEx/financing: enter USD188.11m June 2025 Solar+BESS Chile face. Nested vs aes_andes_green_solar_bess_chile_192p7m total and jun2025 snapshot (not additive).",
    "188113133", "2025-06-30", "2025", "-23.65", "-70.40",
    "AES Andes Chile Solar+BESS green-eligible projects (Antofagasta regional pin).",
    "aes_andes_green_impact_530m_202606",
    "Solar + BESS Chile 188,113,133     4,541,556  192,654,689",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW Solar+BESS Chile June 2025 allocated US$188.11m. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle277", investment_type="financing", evidence="documented", currency="USD",
    value_usd="188113133", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes Solar+BESS Chile June 2025 allocated US$188.11m. Supports aes_andes_green_solar_bess_jun2025_188p1m.",
    evid_note="Opened AES Andes June 2026 Green Bond Impact Report PDF; Solar+BESS Chile June 2025 allocated US$188,113,133 confirmed.",
)

# 3. power_plants_grid / prc — NEW SGBH P&D/inovação R$8.7m (2025)
row_doc(
    "sgbh_pd_8p7m_brl_2025",
    "energy", "power_plants_grid", "prc",
    "State Grid Brazil Holding — P&D/inovação CapEx R$8.7m (2025)",
    "Brazil",
    "SGBH Relatório de Sustentabilidade 2025: R$ 8,7 milhões investidos em 9 projetos de P&D e inovação; narrative also states Em 2025, destinamos R$ 8,7 milhões ao gerenciamento do portfólio de projetos de P&D. CapEx: enter R$8.7m P&D face. Distinct from sgbh_cumulative_30bn_brl_2010_2025 / GATE R$18bn project envelopes (not additive).",
    "8700000", "2025-12-31", "2025", "", "",
    "SGBH Brazil multi-state transmission footprint (nationwide; lat/lon blank).",
    "sgbh_rs2025_cumulative_30bn",
    "R$ 8,7 milhões investidos em 9 projetos de P&D e inovação",
    "https://stategrid.com.br/wp-content/uploads/2026/04/SGBH_RS25_VFb.pdf",
    "Actor: State Grid Brazil Holding / SGCC (PRC) — prc. NEW P&D/inovação CapEx R$8.7m. Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle277", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(8700000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='State Grid Brazil Holding. “Relatório de Sustentabilidade 2025.” 2026. https://stategrid.com.br/wp-content/uploads/2026/04/SGBH_RS25_VFb.pdf.',
    annotation="SGBH P&D/inovação 2025 CapEx R$8.7m via Fed H.10. Supports sgbh_pd_8p7m_brl_2025.",
    evid_note="Opened SGBH RS 2025 PDF; R$8.7m P&D/inovação confirmed.",
)

# 4. power_plants_grid / allied — NEW Neoenergia Hydro 2Q26 CapEx R$5m
row_doc(
    "neoenergia_hydro_2q26_5m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — hydroelectric plants 2Q26 CapEx R$5m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release: CAPEX table Hydroelectric plants R$5 million in 2Q26 (6M26 R$6m already nested). CapEx: enter R$5m 2Q26 hydro face. Nested vs neoenergia_hydro_6m26_6m_brl / neoenergia_6m26_capex_4bn_brl (not additive).",
    "5000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil hydro portfolio (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Hydroelectric plants 5              3               52% 6                  12               (48%)",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Hydro 2Q26 CapEx R$5m. Shuffle power_plants_grid.",
    "hunt_cycle277", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(5000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Hydro 2Q26 CapEx R$5m via Fed H.10. Supports neoenergia_hydro_2q26_5m_brl.",
    evid_note="Opened Neoenergia 2Q26/6M26 MZ IQ PDF; Hydroelectric plants Capex 2Q26 R$5m confirmed.",
)

# 5. power_plants_grid / allied — NEW Neoenergia Customers 2Q26 CapEx R$7m
row_doc(
    "neoenergia_customers_2q26_7m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — Customers 2Q26 CapEx R$7m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release: CAPEX table Customers R$7 million in 2Q26 (6M26 R$19m already nested within Generation and Customers). CapEx: enter R$7m 2Q26 Customers face. Nested vs neoenergia_customers_6m26_19m_brl / neoenergia_6m26_capex_4bn_brl (not additive).",
    "7000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil customers segment (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Customers 7               3               94% 19                 7                173%",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Customers 2Q26 CapEx R$7m. Shuffle power_plants_grid.",
    "hunt_cycle277", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(7000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Customers 2Q26 CapEx R$7m via Fed H.10. Supports neoenergia_customers_2q26_7m_brl.",
    evid_note="Opened Neoenergia 2Q26/6M26 MZ IQ PDF; Customers Capex 2Q26 R$7m confirmed.",
)

# 6. power_plants_grid / other — NEW Equatorial Dist non-electric 2T26 CapEx R$134.24m
row_doc(
    "equatorial_dist_nonelectric_2t26_134m_brl",
    "energy", "power_plants_grid", "other",
    "Equatorial — Dist non-electric CapEx R$134.24m (2T26)",
    "Brazil",
    "12 Aug 2026 Equatorial S.A. 2T26 earnings release (company MZ IQ PDF): Os investimentos em ativos não elétricos no segmento de distribuição totalizaram R$ 134,24 milhões (5.3% of Dist CapEx 2T26); within Dist CapEx R$2,527m already nested. CapEx: enter R$134.24m non-electric Dist face. Nested vs equatorial_dist_2t26_2527m_brl (not additive).",
    "134240000", "2026-06-30", "2026", "-15.78", "-47.93",
    "Equatorial Brazil distribution footprint (Brasília HQ pin).",
    "equatorial_2t26_release_20260812",
    "Os investimentos em ativos não elétricos no segmento de distribuição totalizaram R$ 134,24 milhões, representando 5,3% do CAPEX total de distribuição no 2T26.",
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2",
    "Actor: Equatorial S.A. — other. NEW nested Dist non-electric 2T26 CapEx R$134.24m. Shuffle power_plants_grid.",
    "hunt_cycle277", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(134240000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2.',
    annotation="Equatorial Dist non-electric 2T26 CapEx R$134.24m via Fed H.10. Supports equatorial_dist_nonelectric_2t26_134m_brl.",
    evid_note="Opened Equatorial 2T26 MZ IQ PDF; Dist non-electric Capex R$134.24m confirmed.",
)

# 7. rail / other — NEW Rumo Material Rodante 2T26 CapEx R$115m
row_doc(
    "rumo_material_rodante_2t26_115m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Material Rodante 2T26 CapEx R$115m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Material Rodante R$115 million in 2T26 (+79.8% vs 2T25 R$64m); 6M26 R$547m — nested rolling-stock CapEx within Operação Norte. CapEx: enter R$115m Material Rodante face. Nested vs rumo_norte_2t26_1393m_brl / rumo_2t26_capex_1597m_brl (not additive).",
    "115000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Rumo Operação Norte rolling stock (São Paulo HQ pin).",
    "rumo_2t26_release_20260812",
    "115 64 79,8 % Material Rodante 547 312 75,3 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Material Rodante 2T26 CapEx R$115m. Shuffle rail.",
    "hunt_cycle277", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(115000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Material Rodante 2T26 CapEx R$115m via Fed H.10. Supports rumo_material_rodante_2t26_115m_brl.",
    evid_note="Opened Rumo 2T26 company RI PDF; Material Rodante Capex R$115m confirmed.",
)

# 8. rail / other — NEW Rumo Ferrovia do Mato Grosso 2T26 CapEx R$342m
row_doc(
    "rumo_fmt_2t26_342m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Ferrovia do Mato Grosso 2T26 CapEx R$342m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Ferrovia do Mato Grosso R$342 million in 2T26 (−26.9% vs 2T25 R$468m); 6M26 R$671m — nested spent face within Operação Norte (distinct from rumo_ferrovia_mt_1bn_brl_2026 plan envelope). CapEx: enter R$342m FMT 2T26 face. Nested vs rumo_norte_2t26_1393m_brl (not additive).",
    "342000000", "2026-06-30", "2026", "-15.60", "-56.10",
    "Ferrovia do Mato Grosso corridor (Mato Grosso regional pin).",
    "rumo_2t26_release_20260812",
    "342 468 -26,9 % Ferrovia do Mato Grosso 671 821 -18,2 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Ferrovia do Mato Grosso 2T26 CapEx R$342m. Shuffle rail.",
    "hunt_cycle277", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(342000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo FMT 2T26 CapEx R$342m via Fed H.10. Supports rumo_fmt_2t26_342m_brl.",
    evid_note="Opened Rumo 2T26 company RI PDF; Ferrovia do Mato Grosso Capex R$342m confirmed.",
)

# 9. rail / other — NEW Rumo Operação Norte Recorrente 2T26 CapEx R$415m
row_doc(
    "rumo_norte_recorrente_2t26_415m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Norte Recorrente 2T26 CapEx R$415m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Norte Recorrente R$415 million in 2T26 (+35.9% vs 2T25 R$305m); 6M26 R$780m — nested recurrent CapEx within Operação Norte R$1,393m. CapEx: enter R$415m Norte Recorrente face. Nested vs rumo_norte_2t26_1393m_brl / rumo_expansao_norte_2t26_979m_brl (not additive).",
    "415000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Rumo Operação Norte recurrent CapEx (São Paulo HQ pin).",
    "rumo_2t26_release_20260812",
    "415 305 35,9 % Recorrente 780 592 31,9 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Norte Recorrente 2T26 CapEx R$415m. Shuffle rail.",
    "hunt_cycle277", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(415000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Norte Recorrente 2T26 CapEx R$415m via Fed H.10. Supports rumo_norte_recorrente_2t26_415m_brl.",
    evid_note="Opened Rumo 2T26 company RI PDF; Norte Recorrente Capex R$415m confirmed.",
)

# 10. water / other — NEW Aegea Pará outorga 6M26 R$285m
row_doc(
    "aegea_para_outorga_6m26_285m_brl",
    "resources", "water", "other",
    "Aegea — Pará outorga 6M26 R$285m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Outorgas breakdown Pará R$285 million in 6M26 (2T26 — / N/A); nested concession-grant payment within Outorgas 6M26 R$402m / ecosystem investments. CapEx/financing: enter R$285m Pará outorga face. Nested vs aegea_outorgas_2t26_73m_brl 2T26 and ecosystem Capex (not additive).",
    "285000000", "2026-06-30", "2026", "-1.46", "-48.50",
    "Águas do Pará concession (Belém regional pin).",
    "aegea_2t26_6m26_release_mziq",
    "Pará - - N/A 285 - N/A",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Pará outorga 6M26 R$285m. Shuffle water.",
    "hunt_cycle277", investment_type="financing", evidence="documented", currency="BRL",
    value_usd=str(round(285000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Pará outorga 6M26 R$285m via Fed H.10. Supports aegea_para_outorga_6m26_285m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Pará outorga 6M26 R$285m confirmed.",
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
    print(f"cycle277 added {len(added)}: {added}")
    print(f"cycle277 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
