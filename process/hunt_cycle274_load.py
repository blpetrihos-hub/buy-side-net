#!/usr/bin/env python3
"""Cycle 274 hunt: shuffle_seed=20261274; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261274).shuffle):
copper, rail, wind, power_plants_grid, water, solar, port_cranes, fission_smr,
engineering_epc, bridges_roads, balsa, niobium, building_materials, port_ownership,
other_renewables, nickel, graphite, lithium.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes green-bond Energy Purchases Chile allocation
  US$87.80m (same June 2026 Green Bond Impact Report).
PRC equal-budget: NEW CPFL FY2025 comercialização/serviços/outros CapEx R$74m
  (same admin/DFs face as Dist/TX/Gen nested prior cycles).
Allied: NEW ISA Energia 2T26 R&M R$445.4m + licitados/greenfield R$608.1m.
Other: NEW Rumo Operação Norte 2T26 R$1.393bn + Sul R$183m; Aegea Manaus Capex
  R$91m + PPPs R$237m; Equatorial Saneamento 2T26 R$12m; Cemig Gen 1S26 R$30m.
Skipped: thin dry; ENGIE Colibri host 403; Ascenty company face 403; Alupar TECP
  unsigned; PowerChina/CCCC English news hosts 404; holdovers unsigned.
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


# 1. other_renewables / us — NEW AES Andes green Energy Purchases Chile US$87.80m
row_doc(
    "aes_andes_green_purchases_chile_87p8m",
    "energy", "other_renewables", "us",
    "AES Andes — green-bond Energy Purchases Chile allocation US$87.80m",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report allocation table: Energy Purchases (contracts supplied by wind and solar or solar+BESS projects) Chile total allocated as of 31 Mar 2026 = US$87,798,268. CapEx/financing: enter USD87.80m Energy Purchases Chile face. Nested vs aes_andes_green_alloc_331p7m_20260331 total allocated (not additive).",
    "87798268", "2026-03-31", "2026", "-33.43", "-70.61",
    "AES Andes Chile renewable PPA / energy-purchase portfolio (Santiago HQ pin).",
    "aes_andes_green_impact_530m_202606",
    "Energy Purchases* Chile … Total amount allocated as of March 31, 2026 (US$) 87,798,268",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW nested Energy Purchases Chile green allocation US$87.80m. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle274", investment_type="financing", evidence="documented", currency="USD",
    value_usd="87798268", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes Energy Purchases Chile green allocation US$87.80m. Supports aes_andes_green_purchases_chile_87p8m.",
    evid_note="Opened AES Andes Green Bond Impact Report; Energy Purchases Chile US$87,798,268 confirmed.",
)

# 2. power_plants_grid / prc — NEW CPFL FY2025 comercialização/serviços/outros R$74m
row_doc(
    "cpfl_fy2025_other_74m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia (State Grid–controlled) — FY2025 comercialização/serviços/outros CapEx R$74m",
    "Brazil",
    "CPFL Energia Relatório de Administração / DFs 2025: of R$6.112bn total 2025 investments, R$74 million to comercialização, serviços e outros. CapEx: enter R$74m other-segment face. Nested vs cpfl_fy2025_capex_6p1bn_brl / Dist / TX / Gen faces (not additive).",
    "74000000", "2025-12-31", "2025", "-22.91", "-47.06",
    "CPFL Energia Brazil commercialization/services footprint (Campinas / São Paulo pin).",
    "cpfl_admin_dfs_2025_investments",
    "Em 2025, foram realizados investimentos de R$ 6.112 milhões para manutenção e expansão do negócio, dos quais R$ 4.964 milhões foram direcionados à distribuição, R$ 804 milhões ao segmento de transmissão, R$ 270 milhões à geração e R$ 74 milhões à comercialização, serviços e outros.",
    "https://ri.cpfl.com.br/Download.aspx?Arquivo=xGWXwO4pmQpCskEpHHDQQg%3D%3D",
    "Actor: CPFL Energia (State Grid–controlled) — prc. NEW nested FY2025 other-segment CapEx R$74m. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle274", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(74000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia S.A. “Relatório de Administração e Demonstrações Financeiras” (2025). Company RI PDF. https://ri.cpfl.com.br/Download.aspx?Arquivo=xGWXwO4pmQpCskEpHHDQQg%3D%3D.',
    annotation="CPFL FY2025 other-segment CapEx R$74m via Fed H.10. Supports cpfl_fy2025_other_74m_brl.",
    evid_note="Opened CPFL admin/DFs PDF; comercialização/serviços/outros R$74 milhões confirmed.",
)

# 3. power_plants_grid / allied — NEW ISA Energia 2T26 R&M CapEx R$445.4m
row_doc(
    "isa_energia_2t26_rm_445p4m_brl",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — 2T26 Reinforcements & Improvements CapEx R$445.4m",
    "Brazil",
    "3 Aug 2026 ISA Energia Brasil company news (2T26): of Q2 investments ~R$1.1bn, R$445.4 million dedicated to Reforços e Melhorias (+17% vs 2T25). CapEx: enter R$445.4m 2T26 R&M face. Nested vs isa_energia_2t26_capex_1053p5m_brl sum and isa_energia_rm_815m_brl_1s26 (not additive).",
    "445400000", "2026-06-30", "2026", "-23.55", "-46.63",
    "ISA Energia Brasil transmission R&M footprint (São Paulo HQ pin).",
    "isa_energia_2t26_news_20260803",
    "Desse montante, R$ 445,4 milhões foram dedicados a projetos de Reforços e Melhorias, incremento de R$ 66,1 milhões (+17% vs. 2T25), e R$ 608,1 milhões a projetos licitados",
    "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/com-energizacao-de-grandes-projetos-isa-energia-brasil-amplia-receita-liquida-em-21-no-trimestre/",
    "Actor: ISA Energia Brasil (ISA Colombia–controlled) — allied. NEW nested 2T26 R&M CapEx R$445.4m. Shuffle power_plants_grid.",
    "hunt_cycle274", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(445400000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “Com energização de grandes projetos, ISA Energia Brasil amplia receita líquida em 21% no trimestre.” August 3, 2026. https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/com-energizacao-de-grandes-projetos-isa-energia-brasil-amplia-receita-liquida-em-21-no-trimestre/.',
    annotation="ISA Energia 2T26 R&M CapEx R$445.4m via Fed H.10. Supports isa_energia_2t26_rm_445p4m_brl.",
    evid_note="Opened ISA Energia Brasil 2T26 company news; R&M R$445,4 milhões confirmed.",
)

# 4. power_plants_grid / allied — NEW ISA Energia 2T26 licitados CapEx R$608.1m
row_doc(
    "isa_energia_2t26_licitados_608p1m_brl",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — 2T26 licitados/greenfield CapEx R$608.1m",
    "Brazil",
    "3 Aug 2026 ISA Energia Brasil company news (2T26): R$608.1 million to projetos licitados (−16% vs 2T25) within Q2 ~R$1.1bn investments. CapEx: enter R$608.1m 2T26 licitados face. Nested vs isa_energia_2t26_capex_1053p5m_brl sum and Serra Dourada/Itatiaia remaining CapEx (not additive).",
    "608100000", "2026-06-30", "2026", "-23.55", "-46.63",
    "ISA Energia Brasil greenfield/licitados transmission portfolio (São Paulo HQ pin).",
    "isa_energia_2t26_news_20260803",
    "e R$ 608,1 milhões a projetos licitados – uma redução de R$ 114,7 milhões (−16% vs. 2T25)",
    "https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/com-energizacao-de-grandes-projetos-isa-energia-brasil-amplia-receita-liquida-em-21-no-trimestre/",
    "Actor: ISA Energia Brasil (ISA Colombia–controlled) — allied. NEW nested 2T26 licitados CapEx R$608.1m. Shuffle power_plants_grid.",
    "hunt_cycle274", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(608100000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “Com energização de grandes projetos, ISA Energia Brasil amplia receita líquida em 21% no trimestre.” August 3, 2026. https://www.isaenergiabrasil.com.br/centro-de-midia/noticias/com-energizacao-de-grandes-projetos-isa-energia-brasil-amplia-receita-liquida-em-21-no-trimestre/.',
    annotation="ISA Energia 2T26 licitados CapEx R$608.1m via Fed H.10. Supports isa_energia_2t26_licitados_608p1m_brl.",
    evid_note="Opened ISA Energia Brasil 2T26 company news; licitados R$608,1 milhões confirmed.",
)

# 5. rail / other — NEW Rumo Operação Norte 2T26 CapEx R$1.393bn
row_doc(
    "rumo_norte_2t26_1393m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Norte 2T26 CapEx R$1.393bn",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26 (company RI PDF): Capex table Operação Norte R$1,393 million in 2T26 (+17.5% vs 2T25 R$1,186m); 6M26 R$2,988m; within total Capex R$1,597m. CapEx: enter R$1.393bn Norte face. Nested vs rumo_2t26_capex_1597m_brl consolidated (not additive).",
    "1393000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Rumo Operação Norte (Malha Norte/Paulista/Central/Oeste; São Paulo HQ pin).",
    "rumo_2t26_release_20260812",
    "1.393 1.186 17,5 % Operação Norte 2.988 2.782 7,4 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. (Cosan) — other. NEW nested Operação Norte 2T26 CapEx R$1.393bn. Shuffle rail.",
    "hunt_cycle274", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1393000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Operação Norte 2T26 CapEx R$1.393bn via Fed H.10. Supports rumo_norte_2t26_1393m_brl.",
    evid_note="Opened Rumo 2T26 company RI PDF; Operação Norte Capex R$1,393m confirmed.",
)

# 6. rail / other — NEW Rumo Operação Sul 2T26 CapEx R$183m
row_doc(
    "rumo_sul_2t26_183m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Sul 2T26 CapEx R$183m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Sul R$183 million in 2T26 (−4.8% vs 2T25 R$192m); 6M26 R$343m. CapEx: enter R$183m Sul face. Nested vs rumo_2t26_capex_1597m_brl / rumo_norte_2t26_1393m_brl (not additive).",
    "183000000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Rumo Malha Sul / Operação Sul (Curitiba / southern Brazil pin).",
    "rumo_2t26_release_20260812",
    "183 192 -4,8 % Operação Sul 343 371 -7,6 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Operação Sul 2T26 CapEx R$183m. Shuffle rail.",
    "hunt_cycle274", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(183000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Operação Sul 2T26 CapEx R$183m via Fed H.10. Supports rumo_sul_2t26_183m_brl.",
    evid_note="Opened Rumo 2T26 company RI PDF; Operação Sul Capex R$183m confirmed.",
)

# 7. water / other — NEW Aegea Manaus 2T26 Capex R$91m
row_doc(
    "aegea_manaus_2t26_91m_brl",
    "resources", "water", "other",
    "Aegea — Águas de Manaus 2T26 Capex R$91m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release (company MZ IQ PDF): Capex table Manaus R$91 million in 2T26 (−18.1% vs 2T25 R$111m); 6M26 R$164m. CapEx: enter R$91m Manaus face. Nested vs aegea_2t26_ecosystem_capex_1828m_brl (not additive).",
    "91000000", "2026-06-30", "2026", "-3.12", "-60.02",
    "Águas de Manaus concession, Amazonas (Manaus pin).",
    "aegea_2t26_6m26_release_mziq",
    "Manaus 91 111 -18,1% 164 221 -25,6%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Manaus 2T26 Capex R$91m. Shuffle water.",
    "hunt_cycle274", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(91000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Manaus 2T26 Capex R$91m via Fed H.10. Supports aegea_manaus_2t26_91m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Manaus Capex 2T26 R$91m confirmed.",
)

# 8. water / other — NEW Aegea PPPs 2T26 Capex R$237m
row_doc(
    "aegea_ppps_2t26_237m_brl",
    "resources", "water", "other",
    "Aegea — PPPs 2T26 Capex R$237m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table PPPs R$237 million in 2T26 (−31.8% vs 2T25 R$348m); 6M26 R$475m. CapEx: enter R$237m PPPs face. Nested vs aegea_2t26_ecosystem_capex_1828m_brl (not additive).",
    "237000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Aegea Brazil water/sanitation PPP portfolio (São Paulo HQ pin).",
    "aegea_2t26_6m26_release_mziq",
    "PPPs 237 348 -31,8% 475 592 -19,8%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested PPPs 2T26 Capex R$237m. Shuffle water.",
    "hunt_cycle274", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(237000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea PPPs 2T26 Capex R$237m via Fed H.10. Supports aegea_ppps_2t26_237m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; PPPs Capex 2T26 R$237m confirmed.",
)

# 9. water / other — NEW Equatorial Saneamento 2T26 CapEx R$12m
row_doc(
    "equatorial_saneamento_2t26_12m_brl",
    "resources", "water", "other",
    "Equatorial — Saneamento 2T26 CapEx R$12m",
    "Brazil",
    "12 Aug 2026 Equatorial S.A. 2T26 earnings release (company MZ IQ PDF): Investimentos table Saneamento R$12 million in 2T26 (−7% vs 2T25 R$13m); within consolidated ~R$2.6bn. CapEx: enter R$12m Saneamento face. Nested vs equatorial_2t26_capex_2p6bn_brl (not additive).",
    "12000000", "2026-06-30", "2026", "-15.78", "-47.93",
    "Equatorial Saneamento Brazil portfolio (Brasília release pin).",
    "equatorial_2t26_release_20260812",
    "Saneamento 13 12 -7% (1)",
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2",
    "Actor: Equatorial S.A. — other. NEW nested Saneamento 2T26 CapEx R$12m. Shuffle water.",
    "hunt_cycle274", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(12000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Resultados do segundo trimestre de 2026 (2T26).” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2.',
    annotation="Equatorial Saneamento 2T26 CapEx R$12m via Fed H.10. Supports equatorial_saneamento_2t26_12m_brl.",
    evid_note="Opened Equatorial 2T26 MZ IQ PDF; Saneamento CapEx 2T26 R$12m confirmed.",
)

# 10. power_plants_grid / other — NEW Cemig Gen 1S26 CapEx R$30m
row_doc(
    "cemig_gen_1s26_30m_brl",
    "energy", "power_plants_grid", "other",
    "Cemig — generation expansion/maintenance 1S26 CapEx R$30m",
    "Brazil",
    "Cemig 1S26/2T26 results presentation (company RI PDF): Geração bullet states R$30 million in expansão e manutenção within 1S26 investment program highlights. CapEx: enter R$30m generation face. Nested vs cemig_1s26_capex_3p28bn_brl consolidated / Dist R$2.64bn / TX R$275.2m (not additive).",
    "30000000", "2026-06-30", "2026", "-19.92", "-43.94",
    "Cemig generation footprint, Minas Gerais (Belo Horizonte pin).",
    "cemig_1s26_results_presentation_20260630",
    "GERAÇÃO • R$ 30 milhões em expansão e manutenção",
    "https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf",
    "Actor: Cemig — other. NEW nested Gen 1S26 CapEx R$30m. Shuffle power_plants_grid.",
    "hunt_cycle274", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(30000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Cemig. “Resultados 1S26 / 2T26” (company RI presentation PDF). https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf.',
    annotation="Cemig Gen 1S26 CapEx R$30m via Fed H.10. Supports cemig_gen_1s26_30m_brl.",
    evid_note="Opened Cemig 1S26/2T26 results PDF; Geração R$30 milhões confirmed.",
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
    print(f"cycle274 added {len(added)}: {added}")
    print(f"cycle274 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
