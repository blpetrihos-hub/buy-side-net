#!/usr/bin/env python3
"""Cycle 270 hunt: shuffle_seed=20261270; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261270).shuffle):
fission_smr, niobium, engineering_epc, balsa, other_renewables, lithium,
port_ownership, power_plants_grid, bridges_roads, building_materials, water,
solar, nickel, copper, wind, rail, port_cranes, graphite.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW Equinix MO2 total build-out ~USD189m + NEW Equinix
  Brazil avg ~R$1bn/yr decade CapEx (company Portuguese SP6 newsroom).
PRC equal-budget: NEW CPFL Energia 2026 CapEx budget R$6.308bn (Formulário).
Allied: NEW Neoenergia Dist 6M26 CapEx R$3.696bn nested.
Other: NEW Cemig Dist/TX 1S26 nested; Copel DisCo 2026 plan R$1.94bn + LRCAP
  Foz do Areia R$190m + Segredo R$541m; Motiva 1T26 CapEx R$1.473bn.
Skipped: thin dry; holdovers unsigned; catalog dense elsewhere.
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


# 1. engineering_epc / us — NEW Equinix MO2 total build-out ~USD189m
row_doc(
    "equinix_mo2_total_189m_buildout",
    "infrastructure", "engineering_epc", "us",
    "Equinix — MO2 Monterrey total build-out CapEx ~USD189m",
    "Mexico",
    "30 Oct 2025 Equinix México Spanish newsroom: MO2 Monterrey (Apodaca) phase-1 investment USD 81 million; company states total facility investment expected approximately US$189 million once fully built. CapEx: enter USD 189m total build-out ceiling. Nested vs equinix_mo2_monterrey_81m_2025 phase-1 face (not additive).",
    "189000000", "2025-10-30", "2025", "25.78", "-100.19",
    "Equinix MO2, Apodaca / Monterrey, Nuevo León, Mexico (company geography; approximate Apodaca pin).",
    "equinix_mo2_monterrey_20251030",
    "Se prevé que la nueva instalación tenga una inversión total de aproximadamente US$189 millones una vez construida.",
    "https://newsroom.equinix.com/2025-10-30-Equinix-Mexico-invierte-US-81-millones-en-nuevo-centro-de-datos-en-Monterrey",
    "Actor: Equinix (U.S. Nasdaq:EQIX) — us. NEW nested MO2 total build-out ~USD189m. Shuffle engineering_epc; ≥1/3 U.S. hunt. Reuses company Spanish newsroom already supporting phase-1 row.",
    "hunt_cycle270", investment_type="greenfield_plant", evidence="documented", currency="USD",
    value_usd="189000000", fx_usd="1", bib_type="company",
    chicago='Equinix. “Equinix México invierte US$ 81 millones en nuevo centro de datos en Monterrey.” October 30, 2025. https://newsroom.equinix.com/2025-10-30-Equinix-Mexico-invierte-US-81-millones-en-nuevo-centro-de-datos-en-Monterrey.',
    annotation="Equinix MO2 total build-out ~USD189m. Supports equinix_mo2_total_189m_buildout; equinix_mo2_monterrey_81m_2025.",
    evid_note="Opened Equinix México Spanish newsroom; total investment ~USD189m once built confirmed. Nested vs USD81m phase 1.",
)

# 2. engineering_epc / us — NEW Equinix Brazil avg ~R$1bn/yr decade CapEx
row_doc(
    "equinix_brazil_avg_1bn_brl_yr",
    "infrastructure", "engineering_epc", "us",
    "Equinix — Brazil average annual CapEx ~R$1bn (last decade)",
    "Brazil",
    "16 Apr 2026 Equinix Portuguese newsroom (SP6 inauguration): company states it invests on average about R$1 billion per year in Brazil over the last decade. CapEx: enter R$1bn soft average-annual face (historical average, not a single-year commitment). Nested vs equinix_sp6_114m_2026 / equinix_brazil_270m_2025_2026 site/breakout rows (not additive).",
    "1000000000", "2026-04-16", "2026", "-23.444", "-46.918",
    "Equinix Brazil IBX footprint (Santana de Parnaíba / Greater São Paulo pin; SP6 campus cited).",
    "equinix_sp6_ops_20260416",
    "Esse movimento reflete o compromisso contínuo da Equinix com o país, onde a companhia investe, em média, cerca de R$ 1 bilhão por ano ao longo da última década.",
    "https://newsroom.equinix.com/2026-04-16-Equinix-fortalece-lideranca-na-America-Latina-com-inauguracao-de-novo-data-center-SP6-em-Sao-Paulo",
    "Actor: Equinix (U.S.) — us. NEW soft average-annual Brazil CapEx ~R$1bn/yr. Shuffle engineering_epc; ≥1/3 U.S. hunt. Reuses SP6 company newsroom.",
    "hunt_cycle270", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equinix. “Equinix fortalece liderança na América Latina com inauguração de novo data center SP6 em São Paulo.” April 16, 2026. https://newsroom.equinix.com/2026-04-16-Equinix-fortalece-lideranca-na-America-Latina-com-inauguracao-de-novo-data-center-SP6-em-Sao-Paulo.',
    annotation="Equinix Brazil avg ~R$1bn/yr via Fed H.10. Supports equinix_brazil_avg_1bn_brl_yr; equinix_sp6_114m_2026.",
    evid_note="Opened Equinix Portuguese SP6 newsroom; média cerca de R$1 bilhão por ano confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / prc — NEW CPFL 2026 CapEx budget R$6.308bn
row_doc(
    "cpfl_2026_budget_6308m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia (State Grid–controlled) — 2026 CapEx budget R$6.308bn",
    "Brazil",
    "CPFL Energia Formulário de Referência (company RI PDF): plans capital investments aggregating approximately R$6.494 billion in 2025 and R$6.308 billion in 2026; of the combined 2025–2026 budget R$10.483bn (81.9%) to distribution. CapEx: enter R$6.308bn 2026 budget face. Nested vs cpfl_capex_plan_31p1bn_2026_2030 / cpfl_dist_25p3bn_2026_2030 (not additive; FR annual budget may predate Mar 2026 plan refresh cited elsewhere as R$6.48bn).",
    "6308000000", "2026-01-01", "2026", "-22.91", "-47.06",
    "CPFL Energia Brazil multi-concession footprint (Campinas / São Paulo pin).",
    "cpfl_fr_2026_budget_6308m",
    "Para essa finalidade, planejamos fazer investimentos de capital agregando aproximadamente R$ 6.494 milhões em 2025 e R$ 6.308 milhões em 2026.",
    "https://ri.cpfl.com.br/Download.aspx?Arquivo=+NxF6ZeI3ozQLDsdjlbLlQ%3D%3D&linguagem=pt",
    "Actor: CPFL Energia (State Grid–controlled) — prc. NEW nested 2026 CapEx budget R$6.308bn from company Formulário. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle270", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(6308000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia S.A. “Formulário de Referência.” Company RI PDF (Portuguese). https://ri.cpfl.com.br/Download.aspx?Arquivo=+NxF6ZeI3ozQLDsdjlbLlQ%3D%3D&linguagem=pt.',
    annotation="CPFL 2026 CapEx budget R$6.308bn via Fed H.10. Supports cpfl_2026_budget_6308m_brl.",
    evid_note="Opened CPFL Formulário de Referência PDF; R$6.308 milhões em 2026 confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 4. power_plants_grid / allied — NEW Neoenergia Dist 6M26 CapEx R$3.696bn
row_doc(
    "neoenergia_dist_6m26_3696m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — distributors 6M26 CapEx R$3.696bn",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release (company MZ IQ PDF): CAPEX table shows Distributors R$3,696 million in 6M26 (+23% vs 6M25 R$3,009m); headline states CAPEX of R$4 billion in 6M26 of which R$3.7 billion in distribution. CapEx: enter R$3.696bn distributors face. Nested vs neoenergia_6m26_capex_4bn_brl consolidated (not additive).",
    "3696000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil distribution footprint (Rio de Janeiro HQ pin; Coelba/Cosern/Elektro/Pernambuco/Brasília).",
    "neoenergia_2q26_release_mziq",
    "Distributors 1,984 1,682 18% 3,696 3,009 23%",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Dist 6M26 CapEx R$3.696bn. Shuffle power_plants_grid.",
    "hunt_cycle270", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(3696000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Dist 6M26 CapEx R$3.696bn via Fed H.10. Supports neoenergia_dist_6m26_3696m_brl; neoenergia_6m26_capex_4bn_brl.",
    evid_note="Opened Neoenergia 2Q26 MZ IQ PDF; Distributors CapEx 6M26 R$3,696m confirmed.",
)

# 5. power_plants_grid / other — NEW Cemig Dist 1S26 CapEx R$2.64bn
row_doc(
    "cemig_dist_1s26_2640m_brl",
    "energy", "power_plants_grid", "other",
    "Cemig — distribution 1S26 CapEx R$2.64bn",
    "Brazil",
    "Cemig 1S26/2T26 results presentation (company RI PDF): Capex realizado R$3.28bn in 1S26; Distribuição R$2.64 bilhões (11 new + 3 expanded substations; +1,886 km LV/MV networks). CapEx: enter R$2.64bn Dist face. Nested vs cemig_1s26_capex_3p28bn_brl consolidated (not additive).",
    "2640000000", "2026-06-30", "2026", "-19.92", "-43.94",
    "Cemig D Minas Gerais distribution footprint (Belo Horizonte HQ pin).",
    "cemig_1s26_results_presentation_20260630",
    "Distribuição: R$2,64 bilhões; 11 subestações novas e 3 ampliadas, adição de 1.886 km de redes de baixa e média tensão",
    "https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf",
    "Actor: Cemig (Minas Gerais state-controlled) — other. NEW nested Dist 1S26 CapEx R$2.64bn. Shuffle power_plants_grid.",
    "hunt_cycle270", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2640000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Cemig. “Resultados 1S26 / 2T26” (company RI presentation PDF). June 30, 2026. https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf.',
    annotation="Cemig Dist 1S26 CapEx R$2.64bn via Fed H.10. Supports cemig_dist_1s26_2640m_brl; cemig_1s26_capex_3p28bn_brl.",
    evid_note="Opened Cemig 1S26 results PDF; Distribuição R$2,64 bilhões confirmed.",
)

# 6. power_plants_grid / other — NEW Cemig TX 1S26 CapEx R$275.2m
row_doc(
    "cemig_tx_1s26_275p2m_brl",
    "energy", "power_plants_grid", "other",
    "Cemig — transmission 1S26 CapEx R$275.2m",
    "Brazil",
    "Cemig 1S26/2T26 results presentation (company RI PDF): Transmissão R$275.2 milhões in 1S26 with R$36.2 milhões de RAP adicionada. CapEx: enter R$275.2m TX face. Nested vs cemig_1s26_capex_3p28bn_brl / cemig_dist_1s26_2640m_brl (not additive).",
    "275200000", "2026-06-30", "2026", "-19.92", "-43.94",
    "Cemig GT Minas Gerais transmission footprint (Belo Horizonte HQ pin).",
    "cemig_1s26_results_presentation_20260630",
    "Transmissão: R$275,2 milhões; com R$36,2 milhões de RAP adicionada",
    "https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf",
    "Actor: Cemig — other. NEW nested TX 1S26 CapEx R$275.2m. Shuffle power_plants_grid.",
    "hunt_cycle270", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(275200000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Cemig. “Resultados 1S26 / 2T26” (company RI presentation PDF). June 30, 2026. https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf.',
    annotation="Cemig TX 1S26 CapEx R$275.2m via Fed H.10. Supports cemig_tx_1s26_275p2m_brl; cemig_1s26_capex_3p28bn_brl.",
    evid_note="Opened Cemig 1S26 results PDF; Transmissão R$275,2 milhões confirmed.",
)

# 7. power_plants_grid / other — NEW Copel DisCo 2026 CapEx plan R$1.94bn
row_doc(
    "copel_disco_2026_plan_1940m_brl",
    "energy", "power_plants_grid", "other",
    "Copel Distribuição — 2026 CapEx plan R$1.94bn",
    "Brazil",
    "Copel company Portuguese news (2026 investment program): of ~R$3 billion planned for 2026, R$1.94 billion applied to distribution (automated network expansion, feeders, >3,000 devices, >3,500 km new networks); R$971.6m to generation and transmission. CapEx: enter R$1.94bn DisCo 2026 plan face. Nested vs copel_1s26_capex_1538p8m_brl spent and 2026–2030 R$17.8bn plan (not additive).",
    "1940000000", "2026-01-01", "2026", "-25.43", "-49.27",
    "Copel Distribuição Paraná concession (Curitiba HQ pin).",
    "copel_2026_3bn_program_news",
    "Do total previsto para este ano, R$ 1,94 bilhão será aplicado na distribuição de energia, enquanto R$ 971,6 milhões serão destinados aos negócios de geração e transmissão.",
    "https://www.copel.com/site/noticias/copel-investe-r-3-bilhoes-em-obras-de-geracao-transmissao-e-distribuicao-de-energia-em-todo-o-parana/",
    "Actor: Copel (Paraná state utility) — other. NEW DisCo 2026 CapEx plan R$1.94bn. Shuffle power_plants_grid.",
    "hunt_cycle270", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(1940000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel. “Copel investe R$ 3 bilhões em obras de geração, transmissão e distribuição de energia em todo o Paraná.” Company news. https://www.copel.com/site/noticias/copel-investe-r-3-bilhoes-em-obras-de-geracao-transmissao-e-distribuicao-de-energia-em-todo-o-parana/.',
    annotation="Copel DisCo 2026 plan R$1.94bn via Fed H.10. Supports copel_disco_2026_plan_1940m_brl.",
    evid_note="Opened Copel company Portuguese news; R$1,94 bilhão distribuição 2026 confirmed.",
)

# 8. power_plants_grid / other — NEW Copel LRCAP Foz do Areia 2026 CapEx R$190m
row_doc(
    "copel_lrcap_foz_areia_190m_brl_2026",
    "energy", "power_plants_grid", "other",
    "Copel — LRCAP Foz do Areia expansion CapEx R$190m (2026)",
    "Brazil",
    "Copel company Portuguese news: within 2026 investment program, CapEx of R$190 million planned for expansion of UHE Governador Bento Munhoz da Rocha Netto (Foz do Areia) under Capacity Reserve Auction (LRCAP/LRCP). CapEx: enter R$190m 2026 face. Nested vs ANDRITZ EPC mid-three-digit EUR award and Segredo companion row (not additive).",
    "190000000", "2026-01-01", "2026", "-26.00", "-51.67",
    "UHE Foz do Areia / Governador Bento Munhoz, Iguaçu River, Paraná (company geography; approximate plant pin).",
    "copel_2026_3bn_program_news",
    "Neste ano, a Copel prevê investimentos de R$ 190 milhões na ampliação da Usina Hidrelétrica Governador Bento Munhoz da Rocha Netto (Foz do Areia) e de R$ 541 milhões na ampliação da Usina Hidrelétrica Governador Ney Braga (Segredo).",
    "https://www.copel.com/site/noticias/copel-investe-r-3-bilhoes-em-obras-de-geracao-transmissao-e-distribuicao-de-energia-em-todo-o-parana/",
    "Actor: Copel — other. NEW LRCAP Foz do Areia 2026 CapEx R$190m. Shuffle power_plants_grid.",
    "hunt_cycle270", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(190000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel. “Copel investe R$ 3 bilhões em obras de geração, transmissão e distribuição de energia em todo o Paraná.” Company news. https://www.copel.com/site/noticias/copel-investe-r-3-bilhoes-em-obras-de-geracao-transmissao-e-distribuicao-de-energia-em-todo-o-parana/.',
    annotation="Copel LRCAP Foz do Areia R$190m via Fed H.10. Supports copel_lrcap_foz_areia_190m_brl_2026.",
    evid_note="Opened Copel company news; Foz do Areia R$190 milhões 2026 LRCAP CapEx confirmed.",
)

# 9. power_plants_grid / other — NEW Copel LRCAP Segredo 2026 CapEx R$541m
row_doc(
    "copel_lrcap_segredo_541m_brl_2026",
    "energy", "power_plants_grid", "other",
    "Copel — LRCAP Segredo expansion CapEx R$541m (2026)",
    "Brazil",
    "Copel company Portuguese news: within 2026 investment program, CapEx of R$541 million planned for expansion of UHE Governador Ney Braga (Segredo) under Capacity Reserve Auction (LRCAP/LRCP). CapEx: enter R$541m 2026 face. Nested vs Foz do Areia companion and ANDRITZ EPC award (not additive).",
    "541000000", "2026-01-01", "2026", "-25.79", "-52.12",
    "UHE Segredo / Governador Ney Braga, Iguaçu River, Paraná (company geography; approximate plant pin).",
    "copel_2026_3bn_program_news",
    "Neste ano, a Copel prevê investimentos de R$ 190 milhões na ampliação da Usina Hidrelétrica Governador Bento Munhoz da Rocha Netto (Foz do Areia) e de R$ 541 milhões na ampliação da Usina Hidrelétrica Governador Ney Braga (Segredo).",
    "https://www.copel.com/site/noticias/copel-investe-r-3-bilhoes-em-obras-de-geracao-transmissao-e-distribuicao-de-energia-em-todo-o-parana/",
    "Actor: Copel — other. NEW LRCAP Segredo 2026 CapEx R$541m. Shuffle power_plants_grid.",
    "hunt_cycle270", investment_type="brownfield_expansion", evidence="documented", currency="BRL",
    value_usd=str(round(541000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel. “Copel investe R$ 3 bilhões em obras de geração, transmissão e distribuição de energia em todo o Paraná.” Company news. https://www.copel.com/site/noticias/copel-investe-r-3-bilhoes-em-obras-de-geracao-transmissao-e-distribuicao-de-energia-em-todo-o-parana/.',
    annotation="Copel LRCAP Segredo R$541m via Fed H.10. Supports copel_lrcap_segredo_541m_brl_2026.",
    evid_note="Opened Copel company news; Segredo R$541 milhões 2026 LRCAP CapEx confirmed.",
)

# 10. bridges_roads / other — NEW Motiva 1T26 CapEx R$1.473bn
row_doc(
    "motiva_1t26_capex_1473m_brl",
    "infrastructure", "bridges_roads", "other",
    "Motiva — 1T26 CapEx R$1.473bn",
    "Brazil",
    "30 Apr 2026 Motiva company news (1T26): executed Capex of R$1.47 billion (+21.7% vs R$1.21bn 1T25); table CAPEX 1T26 R$1.473 billion. CapEx: enter R$1.473bn 1T26 face. Nested vs motiva_1s26_capex_3304m_brl / 2T26 spent rows (not additive).",
    "1473000000", "2026-03-31", "2026", "-23.55", "-46.63",
    "Motiva Brazil roads+rails concession portfolio (São Paulo HQ pin).",
    "motiva_1t26_company_news_20260430",
    "No primeiro trimestre de 2026, a Companhia executou um Capex de R$ 1,47 bilhão, aumento de 21,7% na comparação com o R$ 1,21 bilhão apurado em igual intervalo de 2025.",
    "https://www.motiva.com.br/noticias/motiva-avanca-eficiencia-operacional-lucro-ajustado-1t26/",
    "Actor: Motiva S.A. (ex-CCR) — other. NEW nested 1T26 CapEx R$1.473bn. Shuffle bridges_roads.",
    "hunt_cycle270", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1473000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva. “Motiva tem alta de 16,3% no Lucro Líquido Ajustado no 1T26.” April 30, 2026. https://www.motiva.com.br/noticias/motiva-avanca-eficiencia-operacional-lucro-ajustado-1t26/.',
    annotation="Motiva 1T26 CapEx R$1.473bn via Fed H.10. Supports motiva_1t26_capex_1473m_brl.",
    evid_note="Opened Motiva 1T26 company news; Capex R$1,47 bilhão / table R$1.473bn confirmed.",
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
    print(f"cycle270 added {len(added)}: {added}")
    print(f"cycle270 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
