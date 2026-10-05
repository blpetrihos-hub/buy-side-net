#!/usr/bin/env python3
"""Cycle 273 hunt: shuffle_seed=20261273; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261273).shuffle):
rail, other_renewables, niobium, port_cranes, wind, fission_smr,
building_materials, power_plants_grid, solar, bridges_roads, balsa,
port_ownership, copper, nickel, graphite, engineering_epc, water, lithium.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Andes green-bond BESS-standalone Chile allocation
  US$37.96m + Wind Chile US$10.40m + Wind Colombia US$2.90m (same June 2026
  Green Bond Impact Report nested vs cycle-272 issuance/total allocated).
PRC equal-budget: NEW CPFL 1H26 Dist CapEx ~R$2.24bn (company soft ~80% of
  R$2.8bn 1H26 CapEx directed to distribution).
Allied: NEW Neoenergia TX 2Q26 R$80m; Generation and Customers 6M26 R$57m.
Other: NEW Aegea Corsan 2T26 Capex R$484m; Equatorial Renováveis 2T26 R$48m;
  Cemig Dist 2T26 R$1.36bn; Cemig TX 2T26 R$165.9m.
Skipped: thin dry; ENGIE Colibri host 403; Ascenty company face 403; Alupar TECP
  unsigned; holdovers unsigned.
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


# 1. other_renewables / us — NEW AES Andes green BESS-standalone Chile US$37.96m
row_doc(
    "aes_andes_green_bess_chile_38m",
    "energy", "other_renewables", "us",
    "AES Andes — green-bond BESS Standalone Chile allocation US$37.96m",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report allocation table: BESS Standalone Chile total amount allocated as of 31 Mar 2026 = US$37,961,342 (all added in June 2026 report window). CapEx: enter USD37.96m BESS-standalone Chile face. Nested vs aes_andes_green_alloc_331p7m_20260331 total allocated (not additive).",
    "37961342", "2026-03-31", "2026", "-23.65", "-70.40",
    "AES Andes Chile standalone BESS portfolio (Antofagasta / northern Chile pin).",
    "aes_andes_green_impact_530m_202606",
    "BESS Standalone Chile … Total amount allocated as of March 31, 2026 (US$) 37,961,342",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW nested BESS Standalone Chile green allocation US$37.96m. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle273", investment_type="financing", evidence="documented", currency="USD",
    value_usd="37961342", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes BESS Standalone Chile green allocation US$37.96m. Supports aes_andes_green_bess_chile_38m.",
    evid_note="Opened AES Andes Green Bond Impact Report; BESS Standalone Chile US$37,961,342 confirmed.",
)

# 2. wind / us — NEW AES Andes green Wind Chile US$10.40m
row_doc(
    "aes_andes_green_wind_chile_10p4m",
    "energy", "wind", "us",
    "AES Andes — green-bond Wind Chile allocation US$10.40m",
    "Chile",
    "AES Andes June 2026 Green Bond Impact Report: Wind Chile total allocated as of 31 Mar 2026 = US$10,395,795. CapEx: enter USD10.40m Wind Chile face. Nested vs total allocated US$331.7m and Campo Lindo/Mesamávida/San Matías project rows (not additive).",
    "10395795", "2026-03-31", "2026", "-37.47", "-72.35",
    "AES Andes Chile wind portfolio (Biobío Region pin; Campo Lindo/Mesamávida/San Matías geography).",
    "aes_andes_green_impact_530m_202606",
    "Wind Chile … Total amount allocated as of March 31, 2026 (US$) 10,395,795",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW nested Wind Chile green allocation US$10.40m. Shuffle wind; ≥1/3 U.S. hunt.",
    "hunt_cycle273", investment_type="financing", evidence="documented", currency="USD",
    value_usd="10395795", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes Wind Chile green allocation US$10.40m. Supports aes_andes_green_wind_chile_10p4m.",
    evid_note="Opened AES Andes Green Bond Impact Report; Wind Chile US$10,395,795 confirmed.",
)

# 3. wind / us — NEW AES Andes green Wind Colombia US$2.90m
row_doc(
    "aes_andes_green_wind_colombia_2p9m",
    "energy", "wind", "us",
    "AES Andes — green-bond Wind Colombia allocation US$2.90m",
    "Colombia",
    "AES Andes June 2026 Green Bond Impact Report: Wind Colombia total allocated as of 31 Mar 2026 = US$2,901,292 (JK Guajira first-stage pipeline cited in Projects Funded). CapEx: enter USD2.90m Wind Colombia face. Nested vs total allocated and JK1/JK2 project geography (not additive).",
    "2901292", "2026-03-31", "2026", "11.92", "-72.00",
    "AES Andes JK wind project area, Uribia / Guajira, Colombia (company report geography; approximate pin).",
    "aes_andes_green_impact_530m_202606",
    "Wind Colombia … Total amount allocated as of March 31, 2026 (US$) 2,901,292",
    "https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf",
    "Actor: AES Andes / AES Corporation (U.S.) — us. NEW nested Wind Colombia green allocation US$2.90m. Shuffle wind; ≥1/3 U.S. hunt. Weights under-covered Colombia cell.",
    "hunt_cycle273", investment_type="financing", evidence="documented", currency="USD",
    value_usd="2901292", fx_usd="1", bib_type="company",
    chicago='AES Andes S.A. “US$ 530 million 8.150% Junior Notes due 2055 Green Bond Impact Report.” June 2026. https://www.aesandes.com/sites/aesandes.com/files/2026-07/AES-Andes-Green-Impact-Report-US530M-June-2026.pdf.',
    annotation="AES Andes Wind Colombia green allocation US$2.90m. Supports aes_andes_green_wind_colombia_2p9m.",
    evid_note="Opened AES Andes Green Bond Impact Report; Wind Colombia US$2,901,292 confirmed.",
)

# 4. power_plants_grid / prc — NEW CPFL 1H26 Dist CapEx ~R$2.24bn (~80% of R$2.8bn)
row_doc(
    "cpfl_1h26_dist_2240m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Energia (State Grid–controlled) — 1H26 Dist CapEx ~R$2.24bn (~80% of R$2.8bn)",
    "Brazil",
    "13 Aug 2026 CPFL Energia Portuguese results note: CapEx R$2.8 billion year-to-date; company states cerca de 80% of resources directed to distribution (expansion, modernization, customer service, network resilience). CapEx: enter soft ~R$2.24bn Dist face (=0.80×R$2.8bn). Nested vs cpfl_1h26_capex_2p8bn_brl consolidated and cpfl_2t26_capex_1p5bn_brl (not additive).",
    "2240000000", "2026-06-30", "2026", "-22.91", "-47.06",
    "CPFL Energia Brazil distribution footprint (Campinas / São Paulo pin).",
    "cpfl_2t26_1h26_2p8bn",
    "Os investimentos (CAPEX) somaram R$ 1,5 bilhão no trimestre, totalizando R$ 2,8 bilhões no acumulado do ano. Cerca de 80% dos recursos foram direcionados à distribuição, com foco na expansão, modernização, atendimento ao cliente e em melhoria e resiliência de rede.",
    "https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213",
    "Actor: CPFL Energia (State Grid–controlled) — prc. NEW nested 1H26 Dist soft CapEx ~R$2.24bn from company ~80% of R$2.8bn. Shuffle power_plants_grid / PRC equal-budget.",
    "hunt_cycle273", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2240000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Energia. “CPFL Energia registra lucro de R$ 1,4 bilhão no 2T26.” August 13, 2026. https://www.grupocpfl.com.br/noticia/cpfl-energia-registra-lucro-de-r-14-bilhao-no-2t26-alta-de-213.',
    annotation="CPFL 1H26 Dist soft CapEx ~R$2.24bn via Fed H.10. Supports cpfl_1h26_dist_2240m_brl; cpfl_1h26_capex_2p8bn_brl.",
    evid_note="Opened CPFL Portuguese 2T26 note; ~80% of R$2.8bn Dist share confirmed; enter 0.80×R$2.8bn soft face.",
)

# 5. power_plants_grid / allied — NEW Neoenergia TX 2Q26 CapEx R$80m
row_doc(
    "neoenergia_tx_2q26_80m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — transmission 2Q26 CapEx R$80m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release (company MZ IQ PDF): CAPEX table Transmission Lines R$80 million in 2Q26; within Networks R$2,063m. CapEx: enter R$80m 2Q26 TX face. Nested vs neoenergia_tx_6m26_218m_brl / neoenergia_6m26_capex_4bn_brl (not additive).",
    "80000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil transmission portfolio (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Transmission Lines 80 1,054 (92%) 218 1,923 (89%)",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested TX 2Q26 CapEx R$80m. Shuffle power_plants_grid.",
    "hunt_cycle273", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(80000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia TX 2Q26 CapEx R$80m via Fed H.10. Supports neoenergia_tx_2q26_80m_brl.",
    evid_note="Opened Neoenergia 2Q26 MZ IQ PDF; Transmission Lines CapEx 2Q26 R$80m confirmed.",
)

# 6. power_plants_grid / allied — NEW Neoenergia Generation and Customers 6M26 R$57m
row_doc(
    "neoenergia_gen_customers_6m26_57m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — Generation and Customers 6M26 CapEx R$57m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2Q26/6M26 earnings release: CAPEX table Generation and Customers R$57 million in 6M26 (Hydro R$6m + Wind R$31m + Customers R$19m; Solar/Termo R$0). CapEx: enter R$57m Generation and Customers face. Nested vs neoenergia_wind_6m26_31m_brl wind breakout and neoenergia_6m26_capex_4bn_brl (not additive).",
    "57000000", "2026-06-30", "2026", "-22.91", "-43.17",
    "Neoenergia Brazil generation and customers segment (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Generation and Customers 29 55 (47%) 57 92 (38%)",
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2",
    "Actor: Neoenergia (Iberdrola Spain–controlled) — allied. NEW nested Gen+Customers 6M26 CapEx R$57m. Shuffle power_plants_grid.",
    "hunt_cycle273", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(57000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Results as of June 30, 2026” (2Q26/6M26 earnings release). July 21, 2026. https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2.',
    annotation="Neoenergia Gen+Customers 6M26 CapEx R$57m via Fed H.10. Supports neoenergia_gen_customers_6m26_57m_brl.",
    evid_note="Opened Neoenergia 2Q26 MZ IQ PDF; Generation and Customers CapEx 6M26 R$57m confirmed.",
)

# 7. water / other — NEW Aegea Corsan 2T26 Capex R$484m
row_doc(
    "aegea_corsan_2t26_484m_brl",
    "resources", "water", "other",
    "Aegea — Corsan 2T26 Capex R$484m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release (company MZ IQ PDF): Investimentos Proforma Ecossistema Capex table — Corsan R$484 million in 2T26 (+13.1% vs 2T25 R$428m); 6M26 R$845m. CapEx: enter R$484m 2T26 Corsan face. Nested vs aegea_2t26_ecosystem_capex_1828m_brl consolidated (not additive).",
    "484000000", "2026-06-30", "2026", "-30.03", "-51.23",
    "Corsan / Aegea Rio Grande do Sul water concession (Porto Alegre pin).",
    "aegea_2t26_6m26_release_mziq",
    "Corsan 484 428 13,1% 845 836 1,1%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento (Equipav-controlled) — other. NEW nested Corsan 2T26 Capex R$484m. Shuffle water.",
    "hunt_cycle273", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(484000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Corsan 2T26 Capex R$484m via Fed H.10. Supports aegea_corsan_2t26_484m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Corsan Capex 2T26 R$484m confirmed.",
)

# 8. other_renewables / other — NEW Equatorial Renováveis 2T26 CapEx R$48m
row_doc(
    "equatorial_renovaveis_2t26_48m_brl",
    "energy", "other_renewables", "other",
    "Equatorial — Renováveis 2T26 CapEx R$48m",
    "Brazil",
    "12 Aug 2026 Equatorial S.A. 2T26 earnings release (company MZ IQ PDF): Investimentos table Renováveis R$48 million in 2T26 (Ativos Operacionais R$48m); within consolidated ~R$2.6bn. CapEx: enter R$48m Renováveis face. Nested vs equatorial_2t26_capex_2p6bn_brl / equatorial_dist_2t26_2527m_brl (not additive).",
    "48000000", "2026-06-30", "2026", "-15.78", "-47.93",
    "Equatorial Renováveis / Echoenergia Brazil renewable portfolio (Brasília release pin).",
    "equatorial_2t26_release_20260812",
    "Renováveis 11 48 341% 37",
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2",
    "Actor: Equatorial S.A. — other. NEW nested Renováveis 2T26 CapEx R$48m. Shuffle other_renewables.",
    "hunt_cycle273", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(48000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Resultados do segundo trimestre de 2026 (2T26).” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2.',
    annotation="Equatorial Renováveis 2T26 CapEx R$48m via Fed H.10. Supports equatorial_renovaveis_2t26_48m_brl.",
    evid_note="Opened Equatorial 2T26 MZ IQ PDF; Renováveis CapEx 2T26 R$48m confirmed.",
)

# 9. power_plants_grid / other — NEW Cemig Dist 2T26 CapEx R$1.36bn
row_doc(
    "cemig_dist_2t26_1360m_brl",
    "energy", "power_plants_grid", "other",
    "Cemig Distribuição — 2T26 CapEx R$1.36bn",
    "Brazil",
    "Cemig 1S26/2T26 results presentation (company RI PDF): of R$1.80bn invested in 2T26, R$1.36 billion by Cemig Distribuição (91 MVA transformation capacity; 5 new + 2 expanded substations; 1,121 km BT/MT networks; 66k smart meters). CapEx: enter R$1.36bn Dist 2T26 face. Nested vs cemig_dist_1s26_2640m_brl / cemig_2t26_capex_1805p3m_brl (not additive).",
    "1360000000", "2026-06-30", "2026", "-19.92", "-43.94",
    "Cemig Distribuição Minas Gerais concession (Belo Horizonte pin).",
    "cemig_1s26_results_presentation_20260630",
    "Os principais destaques no 2T26 foram: investimento de R$1,36 bilhão realizado pela Cemig Distribuição, ampliação de 91 MVA na capacidade de transformação , 5 novas subestações e 2 ampliadas",
    "https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf",
    "Actor: Cemig (Minas Gerais state utility) — other. NEW nested Dist 2T26 CapEx R$1.36bn. Shuffle power_plants_grid.",
    "hunt_cycle273", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1360000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Cemig. “Resultados 1S26 / 2T26” (company RI presentation PDF). https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf.',
    annotation="Cemig Dist 2T26 CapEx R$1.36bn via Fed H.10. Supports cemig_dist_2t26_1360m_brl.",
    evid_note="Opened Cemig 1S26/2T26 results PDF; Cemig Distribuição R$1,36 bilhão confirmed.",
)

# 10. power_plants_grid / other — NEW Cemig TX 2T26 CapEx R$165.9m
row_doc(
    "cemig_tx_2t26_165p9m_brl",
    "energy", "power_plants_grid", "other",
    "Cemig — transmission reinforcements 2T26 CapEx R$165.9m",
    "Brazil",
    "Cemig 1S26/2T26 results presentation: investimento de R$165.9 million in transmission reinforcements and improvements in 2T26 (alongside Dist R$1.36bn and gasodutos). CapEx: enter R$165.9m TX 2T26 face. Nested vs cemig_tx_1s26_275p2m_brl / cemig_2t26_capex_1805p3m_brl (not additive).",
    "165900000", "2026-06-30", "2026", "-19.92", "-43.94",
    "Cemig transmission footprint, Minas Gerais (Belo Horizonte pin).",
    "cemig_1s26_results_presentation_20260630",
    "investimento de R$165,9 milhões em reforços e melhorias na transmissão",
    "https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf",
    "Actor: Cemig — other. NEW nested TX 2T26 CapEx R$165.9m. Shuffle power_plants_grid.",
    "hunt_cycle273", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(165900000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Cemig. “Resultados 1S26 / 2T26” (company RI presentation PDF). https://ri.cemig.com.br/docs/Cemig-2026-06-30-THtJzCB9.pdf.',
    annotation="Cemig TX 2T26 CapEx R$165.9m via Fed H.10. Supports cemig_tx_2t26_165p9m_brl.",
    evid_note="Opened Cemig 1S26/2T26 results PDF; TX reforços R$165,9 milhões confirmed.",
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
    print(f"cycle273 added {len(added)}: {added}")
    print(f"cycle273 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
