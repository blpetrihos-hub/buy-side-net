#!/usr/bin/env python3
"""Cycle 272 hunt: shuffle_seed=20261272; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261272).shuffle):
other_renewables, copper, building_materials, water, port_ownership, solar,
graphite, bridges_roads, nickel, wind, fission_smr, balsa, niobium, lithium,
engineering_epc, power_plants_grid, port_cranes, rail.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes US$530m green junior notes (Jun 2024) +
  NEW allocated proceeds US$331.7m through Mar 2026 + NEW Solar+BESS Chile
  allocation US$192.65m (company Green Bond Impact Report June 2026).
PRC equal-budget: NEW CPFL FY2025 generation CapEx R$270m (same admin/DFs face
  as Dist/TX nested in cycle 271).
Allied: NEW Neoenergia Dist 2Q26 R$1,984m; Wind Farms 6M26 R$31m.
Other: NEW Motiva 1T26 roads R$1.37bn + rails R$93m; Aegea Águas do Rio 2T26
  Capex R$347m; Cemig Sim 11-UFV acquisition R$155m.
Skipped: thin dry; ENGIE Colibri host 403; Ascenty USD breakouts company face
  blocked; Alupar TECP CapEx still unsigned on company 2T26 ZIP; holdovers
  unsigned.
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


# 1. other_renewables / us — NEW AES Andes US$530m green junior notes
row_doc(
    "aes_andes_green_bond_530m_20240610",
    "energy", "other_renewables", "us",
    "AES Andes — US$530m 8.150% Green Junior Notes due 2055",
    "Chile",
    "10 Jun 2024 AES Andes issued under Rule 144-A / Reg S junior green bond for US$530 million at 8.150% due 2055; company June 2026 Green Bond Impact Report states proceeds finance purchase/construction of wind, solar, and BESS projects in Chile/Colombia pipeline plus ≥5-year renewable PPAs. CapEx/financing: enter USD530m issuance face. Nested vs Greentegra cumulative spent/plan envelopes (not additive).",
    "530000000", "2024-06-10", "2024", "-33.43", "-70.61",
    "AES Andes S.A. HQ Providencia, Santiago, Chile (company report address; multi-country green-eligible pipeline).",
    "aes_andes_green_impact_530m_202606",
    "On June 10, 2024, AES Andes issued under rule 144-A and Regulation S, junior bond for US$530 million at an annual interest of 8.150% and maturing in 2055.",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW green-bond financing CapEx USD530m. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle272", investment_type="financing", evidence="documented", currency="USD",
    value_usd="530000000", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes US$530m green junior notes. Supports aes_andes_green_bond_530m_20240610.",
    evid_note="Opened AES Andes Green Bond Impact Report June 2026 PDF; US$530m junior notes 10 Jun 2024 confirmed.",
)

# 2. other_renewables / us — NEW AES Andes green proceeds allocated US$331.7m
row_doc(
    "aes_andes_green_alloc_331p7m_20260331",
    "energy", "other_renewables", "us",
    "AES Andes — green-bond proceeds allocated US$331.7m (through Mar 2026)",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report: accumulated net proceeds allocated to Eligible Green Projects as of 31 Mar 2026 total US$331.7 million (pending US$198.3m); allocation table covers Solar+BESS Chile, Wind Chile, BESS Standalone Chile, Wind Colombia, and Chile energy purchases. CapEx: enter USD331.7m allocated face. Nested vs aes_andes_green_bond_530m_20240610 issuance (not additive).",
    "331711386", "2026-03-31", "2026", "-33.43", "-70.61",
    "AES Andes Chile/Colombia/Argentina green-eligible renewable+BESS pipeline (Santiago HQ pin).",
    "aes_andes_green_impact_530m_202606",
    "The accumulated amount of net proceeds allocated to Eligible Green Projects is US$331.7 million. Therefore, there is a pending amount to be allocated for US$198.3 million.",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW nested allocated green proceeds US$331.7m. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle272", investment_type="financing", evidence="documented", currency="USD",
    value_usd="331711386", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes green proceeds allocated US$331.7m. Supports aes_andes_green_alloc_331p7m_20260331; aes_andes_green_bond_530m_20240610.",
    evid_note="Opened AES Andes Green Bond Impact Report; allocated US$331.7m through 31 Mar 2026 confirmed.",
)

# 3. solar / us — NEW AES Andes Solar+BESS Chile allocation US$192.65m
row_doc(
    "aes_andes_green_solar_bess_chile_192p7m",
    "energy", "solar", "us",
    "AES Andes — green-bond Solar+BESS Chile allocation US$192.65m",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report allocation table: Solar + BESS Chile total amount allocated as of 31 Mar 2026 = US$192,654,689 (of which US$4,541,556 added since June 2025 report). CapEx: enter USD192.65m Solar+BESS Chile face. Nested vs aes_andes_green_alloc_331p7m_20260331 total allocated and project-level Andes Solar IV / Bolero rows (not additive).",
    "192654689", "2026-03-31", "2026", "-23.65", "-70.40",
    "AES Andes Solar+BESS Chile portfolio (Antofagasta Region pin; Andes Solar / Bolero geography).",
    "aes_andes_green_impact_530m_202606",
    "Solar + BESS Chile … Total amount allocated as of March 31, 2026 (US$) 192,654,689",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW nested Solar+BESS Chile green allocation US$192.65m. Shuffle solar; ≥1/3 U.S. hunt.",
    "hunt_cycle272", investment_type="financing", evidence="documented", currency="USD",
    value_usd="192654689", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes Solar+BESS Chile green allocation US$192.65m. Supports aes_andes_green_solar_bess_chile_192p7m.",
    evid_note="Opened AES Andes Green Bond Impact Report; Solar+BESS Chile allocated US$192,654,689 confirmed.",
)

# 4. power_plants_grid / prc — NEW CPFL FY2025 generation CapEx R$270m
row_doc(
    "cpfl_fy2025_gen_270m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia (State Grid–controlled) — FY2025 generation CapEx R$270m",
    "Brazil",
    "CPFL Energia Relatório de Administração / DFs 2025 (company RI PDF): of R$6.112bn total 2025 investments, R$270 million directed to geração. CapEx: enter R$270m generation face. Nested vs cpfl_fy2025_capex_6p1bn_brl / Dist R$4.964bn / TX R$804m (not additive).",
    "270000000", "2025-12-31", "2025", "-22.91", "-47.06",
    "CPFL Energia Brazil generation footprint (Campinas / São Paulo pin).",
    "cpfl_admin_dfs_2025_investments",
    "Em 2025, foram realizados investimentos de R$ 6.112 milhões para manutenção e expansão do negócio, dos quais R$ 4.964 milhões foram direcionados à distribuição, R$ 804 milhões ao segmento de transmissão, R$ 270 milhões à geração e R$ 74 milhões à comercialização, serviços e outros.",
    "https://ri.cpfl.com.br/Download.aspx?Arquivo=xGWXwO4pmQpCskEpHHDQQg%3D%3D",
    "Actor: CPFL Energia (State Grid–controlled) — prc. NEW nested FY2025 generation CapEx R$270m. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle272", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(270000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia S.A. “Relatório de Administração e Demonstrações Financeiras” (2025). Company RI PDF. https://ri.cpfl.com.br/Download.aspx?Arquivo=xGWXwO4pmQpCskEpHHDQQg%3D%3D.',
    annotation="CPFL FY2025 generation CapEx R$270m via Fed H.10. Supports cpfl_fy2025_gen_270m_brl; cpfl_fy2025_capex_6p1bn_brl.",
    evid_note="Opened CPFL admin/DFs PDF; geração R$270 milhões confirmed.",
)

# 5. power_plants_grid / allied — NEW Neoenergia Dist 2Q26 CapEx R$1,984m
row_doc(
    "neoenergia_dist_2q26_1984m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — distributors 2Q26 CapEx R$1.984bn",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release (company MZ IQ PDF): CAPEX table Distributors R$1,984 million in 2Q26 (+18% vs 2Q25 R$1,682m); within Networks R$2,063m / total CapEx R$2,095m. CapEx: enter R$1.984bn 2Q26 Dist face. Nested vs neoenergia_dist_6m26_3696m_brl / neoenergia_6m26_capex_4bn_brl (not additive).",
    "1984000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil distribution footprint (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Distributors 1,984 1,682 18% 3,696 3,009 23%",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Dist 2Q26 CapEx R$1.984bn. Shuffle power_plants_grid.",
    "hunt_cycle272", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1984000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Dist 2Q26 CapEx R$1.984bn via Fed H.10. Supports neoenergia_dist_2q26_1984m_brl.",
    evid_note="Opened Neoenergia 2Q26 MZ IQ PDF; Distributors CapEx 2Q26 R$1,984m confirmed.",
)

# 6. wind / allied — NEW Neoenergia Wind Farms 6M26 CapEx R$31m
row_doc(
    "neoenergia_wind_6m26_31m_brl",
    "energy", "wind", "allied",
    "Neoenergia — wind farms 6M26 CapEx R$31m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release (company MZ IQ PDF): CAPEX table Wind Farms R$31 million in 6M26 (2Q26 R$17m) within Generation and Customers R$57m. CapEx: enter R$31m wind face. Nested vs neoenergia_6m26_capex_4bn_brl consolidated (not additive).",
    "31000000", "2026-06-30", "2026", "-5.79", "-35.21",
    "Neoenergia Brazil wind portfolio (Northeast Brazil pin; company Generation and Customers segment).",
    "neoenergia_2q26_release_mziq",
    "Wind Farms 17 31 (46%) 31 54 (43%)",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Wind Farms 6M26 CapEx R$31m. Shuffle wind.",
    "hunt_cycle272", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(31000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Wind Farms 6M26 CapEx R$31m via Fed H.10. Supports neoenergia_wind_6m26_31m_brl.",
    evid_note="Opened Neoenergia 2Q26 MZ IQ PDF; Wind Farms CapEx 6M26 R$31m confirmed.",
)

# 7. bridges_roads / other — NEW Motiva 1T26 roads CapEx R$1.37bn
row_doc(
    "motiva_1t26_roads_1370m_brl",
    "infrastructure", "bridges_roads", "other",
    "Motiva — 1T26 roads CapEx R$1.37bn",
    "Brazil",
    "30 Apr 2026 Motiva company news (1T26): of R$1.47bn Capex executed in 1T26, R$1.37 billion applied to highway works (SP/RJ rural capacity; Serra das Araras ahead of schedule COD 2027; Paraná pavement; ViaSul BR-101/290/386; Pantanal expropriations/duplications). CapEx: enter R$1.37bn roads face. Nested vs motiva_1t26_capex_1473m_brl consolidated / motiva_2t26_roads_capex_1640m_brl (not additive).",
    "1370000000", "2026-03-31", "2026", "-23.55", "-46.63",
    "Motiva Brazil highway concession portfolio (São Paulo HQ pin; RioSP/Serra das Araras cited).",
    "motiva_1t26_company_news_20260430",
    "Deste valor, R$ 1,37 bilhão foi aplicado em obras de rodovias, com destaque para a ampliação de capacidade das vias em regiões rurais de São Paulo e Rio de Janeiro, além dos avanços nos trabalhos na Serra das Araras",
    "https://www.motiva.com.br/noticias/motiva-avanca-eficiencia-operacional-lucro-ajustado-1t26/",
    "Actor: Motiva S.A. (ex-CCR) — other. NEW nested 1T26 roads CapEx R$1.37bn. Shuffle bridges_roads.",
    "hunt_cycle272", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1370000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva. “Motiva avança eficiência operacional e lucro ajustado no 1T26.” April 30, 2026. https://www.motiva.com.br/noticias/motiva-avanca-eficiencia-operacional-lucro-ajustado-1t26/.',
    annotation="Motiva 1T26 roads CapEx R$1.37bn via Fed H.10. Supports motiva_1t26_roads_1370m_brl.",
    evid_note="Opened Motiva 1T26 company news; roads Capex R$1,37 bilhão confirmed.",
)

# 8. rail / other — NEW Motiva 1T26 rails CapEx R$93m
row_doc(
    "motiva_1t26_rails_93m_brl",
    "infrastructure", "rail", "other",
    "Motiva — 1T26 rails CapEx R$93m",
    "Brazil",
    "30 Apr 2026 Motiva company news (1T26): Em Trilhos, a Companhia executou R$93 million, especially ViaMobilidade works on Lines 8-Diamante (and related rail program). CapEx: enter R$93m rails face. Nested vs motiva_1t26_capex_1473m_brl / motiva_2t26_rails_capex_175m_brl (not additive).",
    "93000000", "2026-03-31", "2026", "-23.55", "-46.63",
    "Motiva ViaMobilidade São Paulo metro/rail concessions (São Paulo pin; Lines 8-Diamante cited).",
    "motiva_1t26_company_news_20260430",
    "Em Trilhos, a Companhia executou R$ 93 milhões, em especial em obras realizadas pela ViaMobilidade nas linhas 8-Diamante",
    "https://www.motiva.com.br/noticias/motiva-avanca-eficiencia-operacional-lucro-ajustado-1t26/",
    "Actor: Motiva S.A. — other. NEW nested 1T26 rails CapEx R$93m. Shuffle rail.",
    "hunt_cycle272", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(93000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva. “Motiva avança eficiência operacional e lucro ajustado no 1T26.” April 30, 2026. https://www.motiva.com.br/noticias/motiva-avanca-eficiencia-operacional-lucro-ajustado-1t26/.',
    annotation="Motiva 1T26 rails CapEx R$93m via Fed H.10. Supports motiva_1t26_rails_93m_brl.",
    evid_note="Opened Motiva 1T26 company news; Trilhos Capex R$93 milhões confirmed.",
)

# 9. water / other — NEW Aegea Águas do Rio 2T26 Capex R$347m
row_doc(
    "aegea_aguas_do_rio_2t26_347m_brl",
    "resources", "water", "other",
    "Aegea — Águas do Rio 2T26 Capex R$347m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release (company MZ IQ PDF): Investimentos Proforma Ecossistema Capex table — Águas do Rio R$347 million in 2T26 (+19.4% vs 2T25 R$291m); 6M26 R$663m. CapEx: enter R$347m 2T26 Águas do Rio face. Nested vs aegea_2t26_ecosystem_capex_1828m_brl consolidated Capex (not additive).",
    "347000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Águas do Rio concessions (Rio de Janeiro metro area pin; Aegea ecosystem).",
    "aegea_2t26_6m26_release_mziq",
    "Águas do Rio 347 291 19,4% 663 588 12,8%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento (Equipav-controlled) — other. NEW nested Águas do Rio 2T26 Capex R$347m. Shuffle water.",
    "hunt_cycle272", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(347000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Águas do Rio 2T26 Capex R$347m via Fed H.10. Supports aegea_aguas_do_rio_2t26_347m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Águas do Rio Capex 2T26 R$347m confirmed.",
)

# 10. solar / other — NEW Cemig Sim 11-UFV acquisition R$155m
row_doc(
    "cemig_sim_ufv_155m_brl_2t26",
    "energy", "solar", "other",
    "Cemig Sim — acquisition of 11 UFVs (26.2 MWp) for R$155m (2T26)",
    "Brazil",
    "Cemig 1S26/2T26 results presentation (company RI PDF): Cemig Sim acquired 11 UFVs in 2T26 totaling 26.2 MWp installed capacity for R$155 million. CapEx: enter R$155m acquisition face. Distinct from trina_cemig_sim_brazil_2023 module/tracker supply row.",
    "155000000", "2026-06-30", "2026", "-19.92", "-43.94",
    "Cemig Sim distributed solar portfolio, Minas Gerais (Belo Horizonte process pin).",
    "cemig_1s26_results_presentation_20260630",
    "Cemig Sim: aquisição de 11 UFVs no 2T6, totalizando 26,2 MWp de potência instalada, no valor de R$155 milhões",
    "https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf",
    "Actor: Cemig (Minas Gerais state utility) via Cemig Sim — other. NEW UFV acquisition CapEx R$155m. Shuffle solar.",
    "hunt_cycle272", investment_type="ownership_equity", evidence="documented", currency="BRL",
    value_usd=str(round(155000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Cemig. “Resultados 1S26 / 2T26” (company RI presentation PDF). https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf.',
    annotation="Cemig Sim 11-UFV acquisition R$155m via Fed H.10. Supports cemig_sim_ufv_155m_brl_2t26.",
    evid_note="Opened Cemig 1S26/2T26 results PDF; Cemig Sim 11 UFVs R$155 milhões confirmed.",
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
    print(f"cycle272 added {len(added)}: {added}")
    print(f"cycle272 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
