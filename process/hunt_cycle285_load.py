#!/usr/bin/env python3
"""Cycle 285 hunt: shuffle_seed=20261285; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261285).shuffle):
graphite, niobium, lithium, wind, port_ownership, water, copper, engineering_epc,
power_plants_grid, balsa, other_renewables, fission_smr, port_cranes, rail, nickel,
bridges_roads, building_materials, solar.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Brasil 2024E Total / Modernization / Expansion CapEx
  nested within Material Fact 2024–2028 plan; Equinix/Ascenty CapEx blanks; EXIM probes.
PRC equal-budget: NEW CPFL Transmissão 2030 plan R$605m (company FR nested within
  2026–2030 R$4.540bn); 2025 FR column 804 skipped as near-duplicate of
  cpfl_fy2025_tx_804m_brl group TX face.
Other: NEW Motiva FY2025 CapEx R$8.7bn + rodovias R$6.5bn + trilhos R$1.3bn;
  Rumo Contêiner Recorrente 2T26 R$2m; Aegea Demais outorga 6M26 R$3m.
Skipped: thin dry; graphite/niobium/lithium/wind dense; airports CapEx out of
  18-subcat taxonomy; Alupar TECP CapEx face still absent beyond TAP R$498.52m;
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


# 1. water / other — NEW Aegea Demais outorga 6M26 R$3m
row_doc(
    "aegea_demais_outorga_6m26_3m_brl",
    "resources", "water", "other",
    "Aegea — Demais Concessões outorga 6M26 R$3m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Outorgas table Demais Concessões R$3 million in 6M26 (2T26 R$3m already nested). CapEx/financing: enter R$3m Demais outorga 6M26 face. Nested vs aegea_demais_outorga_2t26_3m_brl / aegea_demais_6m26_682m_brl Capex (not additive).",
    "3000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Aegea remaining sanitation concessions (São Paulo HQ pin).",
    "aegea_2t26_6m26_release_mziq",
    "Demais Concessões 3 - N/A 3 - N/A",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Demais outorga 6M26 R$3m. Shuffle water.",
    "hunt_cycle285", investment_type="concession_payment", evidence="documented", currency="BRL",
    value_usd=str(round(3000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Demais outorga 6M26 R$3m via Fed H.10. Supports aegea_demais_outorga_6m26_3m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Demais Concessões outorga 6M26 R$3m confirmed.",
)

# 2. power_plants_grid / us — NEW AES Brasil 2024E Total CapEx R$712.7m
row_doc(
    "aes_brasil_2024e_capex_712p7m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2024E Total Investments CapEx R$712.7m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact (English): investment projections 2024–2028 table shows 2024E Total Investments R$712.7 million (Modernization R$193.9m; Pipeline Development R$130.6m; Expansion R$388.2m). CapEx: enter R$712.7m 2024E face. Nested vs aes_brasil_capex_plan_1348m_brl_2024_2028 multi-year envelope / later year faces (not additive).",
    "712700000", "2024-02-26", "2024", "-23.55", "-46.63",
    "AES Brasil generation portfolio (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Total Investments 712.7 214.2 136.7 125.5 159.5 1,348.4",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil (AES Corp U.S.–controlled) — us. NEW nested 2024E CapEx R$712.7m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle285", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(712700000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2024E CapEx R$712.7m via Fed H.10. Supports aes_brasil_2024e_capex_712p7m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2024E Total Investments R$712.7m confirmed.",
)

# 3. power_plants_grid / us — NEW AES Brasil 2024E Modernization R$193.9m
row_doc(
    "aes_brasil_2024e_modernization_193p9m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2024E Modernization and Maintenance CapEx R$193.9m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: 2024E Modernization and Maintenance R$193.9 million within Total Investments R$712.7m. CapEx: enter R$193.9m Modernization face. Nested vs aes_brasil_2024e_capex_712p7m_brl total (not additive).",
    "193900000", "2024-02-26", "2024", "-23.55", "-46.63",
    "AES Brasil generation portfolio (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Modernization and Maintenance 193.9 213.9 136.7 125.5 159.5 829.4",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil — us. NEW nested 2024E Modernization CapEx R$193.9m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle285", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(193900000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2024E Modernization CapEx R$193.9m via Fed H.10. Supports aes_brasil_2024e_modernization_193p9m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2024E Modernization R$193.9m confirmed.",
)

# 4. power_plants_grid / us — NEW AES Brasil 2024E Expansion R$388.2m
row_doc(
    "aes_brasil_2024e_expansion_388p2m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2024E Expansion CapEx R$388.2m (Tucano + Cajuína)",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: 2024E Expansion R$388.2 million (Tucano Wind Complex R$14.4m + Cajuína Wind Complex R$373.8m) within Total Investments R$712.7m. CapEx: enter R$388.2m Expansion face. Nested vs aes_brasil_2024e_capex_712p7m_brl total (not additive).",
    "388200000", "2024-02-26", "2024", "-23.55", "-46.63",
    "AES Brasil Tucano/Cajuína wind expansion (São Paulo HQ pin; NE Brazil farms).",
    "aes_brasil_mf_capex_20240226",
    "Expansion 388.2 0.0 0.0 0.0 0.0 388.2",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil — us. NEW nested 2024E Expansion CapEx R$388.2m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle285", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(388200000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2024E Expansion CapEx R$388.2m via Fed H.10. Supports aes_brasil_2024e_expansion_388p2m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2024E Expansion R$388.2m confirmed.",
)

# 5. power_plants_grid / us — NEW AES Brasil 2024E Pipeline Development R$130.6m
row_doc(
    "aes_brasil_2024e_pipeline_130p6m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2024E Pipeline Development CapEx R$130.6m (Cajuína Phases 3–4 + AGV VII)",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: 2024E Pipeline Development — Cajuína (Phases 3 and 4) and AGV VII R$130.6 million within Total Investments R$712.7m. CapEx: enter R$130.6m Pipeline face. Nested vs aes_brasil_2024e_capex_712p7m_brl / Expansion R$388.2m (not additive).",
    "130600000", "2024-02-26", "2024", "-23.55", "-46.63",
    "AES Brasil Cajuína/AGV VII pipeline (São Paulo HQ pin; NE Brazil development).",
    "aes_brasil_mf_capex_20240226",
    "Pipeline Development - Cajuína (Phases 3 and 4) and AGV VII 130.6 0.3 0.0 0.0 0.0 130.8",
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1",
    "Actor: AES Brasil — us. NEW nested 2024E Pipeline CapEx R$130.6m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle285", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(130600000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1.',
    annotation="AES Brasil 2024E Pipeline CapEx R$130.6m via Fed H.10. Supports aes_brasil_2024e_pipeline_130p6m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2024E Pipeline Development R$130.6m confirmed.",
)

# 6. power_plants_grid / prc — NEW CPFL TX 2030 CapEx R$605m
row_doc(
    "cpfl_tx_2030_capex_605m_brl",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — 2030 CapEx plan R$605m",
    "Brazil",
    "28 May 2026 CPFL Transmissão Formulário de Referência: CapEx projection table CPFL-T shows 2030*=605 (R$605 million) within 2026–2030 sequence. CapEx: enter R$605m 2030 face. Nested vs cpfl_tx_2026_2030_4540m_brl / prior year faces (not additive).",
    "605000000", "2026-05-28", "2030", "-22.91", "-47.06",
    "CPFL Transmissão Brazil footprint (Campinas / São Paulo pin).",
    "cpfl_tx_fr_2026_20260528",
    "CPFL-T 804 856 1.221 1.059 799 605",
    "https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D",
    "Actor: CPFL Transmissão (State Grid–controlled) — prc. NEW nested 2030 TX CapEx plan R$605m. Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle285", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(605000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='CPFL Transmissão. “Formulário de Referência 2026” (FR_CPFL Transmissão 2026). May 28, 2026. https://ri.cpfl.com.br/Download.aspx?Arquivo=CAx5uyIsFGKmXBS6mHTr9A%3D%3D.',
    annotation="CPFL TX 2030 CapEx R$605m via Fed H.10. Supports cpfl_tx_2030_capex_605m_brl.",
    evid_note="Opened CPFL Transmissão FR 2026 PDF; 2030*=605 CapEx projection confirmed.",
)

# 7. rail / other — NEW Rumo Contêiner Recorrente 2T26 R$2m
row_doc(
    "rumo_conteiner_recorrente_2t26_2m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Contêiner Recorrente CapEx 2T26 R$2m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Contêiner Recorrente R$2 million in 2T26 (6M26 R$8m already nested). CapEx: enter R$2m Contêiner Recorrente 2T26 face. Nested vs rumo_conteiner_recorrente_6m26_8m_brl / rumo_conteiner_2t26_21m_brl (not additive).",
    "2000000", "2026-06-30", "2026", "-23.95", "-46.30",
    "Rumo/Brado container ops (Santos corridor pin).",
    "rumo_2t26_release_20260812",
    "2 6 -69,7 % Recorrente 8 8 -1,8 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Contêiner Recorrente 2T26 CapEx R$2m. Shuffle rail.",
    "hunt_cycle285", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Contêiner Recorrente 2T26 CapEx R$2m via Fed H.10. Supports rumo_conteiner_recorrente_2t26_2m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Contêiner Recorrente Capex 2T26 R$2m confirmed.",
)

# 8. bridges_roads / other — NEW Motiva FY2025 CapEx R$8.7bn
row_doc(
    "motiva_fy2025_capex_87bn_brl",
    "infrastructure", "bridges_roads", "other",
    "Motiva — FY2025 CapEx R$8.7bn (rodovias+trilhos+aeroportos)",
    "Brazil",
    "Motiva company FY2025 results news: invested R$ 8.7 billion in highway, rail, and airport operations in 2025 (+17.5% vs R$7.4bn in 2024). CapEx: enter R$8.7bn FY2025 total face. Distinct from 2026 plan R$8.3bn (ex-airports) and 1S26/2T26 spent rows (not additive).",
    "8700000000", "2025-12-31", "2025", "-23.55", "-46.63",
    "Motiva Brazil roads+rails+airports portfolio (São Paulo HQ pin).",
    "motiva_fy2025_results_8p3bn_2026",
    "a Companhia aportou R$ 8, 7 bilhões em suas operações de rodovias, trilhos e aeroportos",
    "https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/",
    "Actor: Motiva S.A. — other. NEW FY2025 CapEx R$8.7bn. Shuffle bridges_roads.",
    "hunt_cycle285", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(8700000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva S.A. “Motiva encerra 2025 com lucro líquido de R$ 3,27 bilhões….” 2026. https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/.',
    annotation="Motiva FY2025 CapEx R$8.7bn via Fed H.10. Supports motiva_fy2025_capex_87bn_brl.",
    evid_note="Opened Motiva FY2025 company news; CapEx R$8.7bn confirmed.",
)

# 9. bridges_roads / other — NEW Motiva FY2025 rodovias R$6.5bn
row_doc(
    "motiva_fy2025_roads_65bn_brl",
    "infrastructure", "bridges_roads", "other",
    "Motiva — FY2025 rodovias CapEx R$6.5bn",
    "Brazil",
    "Motiva company FY2025 results news: of R$8.7bn total 2025 CapEx, R$ 6.5 billion applied to highway works (Via Dutra capacity, Serra das Araras, ViaSul BR-101/290/386). CapEx: enter R$6.5bn rodovias face. Nested vs motiva_fy2025_capex_87bn_brl total (not additive).",
    "6500000000", "2025-12-31", "2025", "-23.55", "-46.63",
    "Motiva Brazil highway concessions (São Paulo HQ pin; Via Dutra/Serra das Araras/ViaSul cited).",
    "motiva_fy2025_results_8p3bn_2026",
    "R$ 6, 5 bilhões foram aplicados em obras no segmento de rodovias",
    "https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/",
    "Actor: Motiva S.A. — other. NEW nested FY2025 rodovias CapEx R$6.5bn. Shuffle bridges_roads.",
    "hunt_cycle285", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(6500000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva S.A. “Motiva encerra 2025 com lucro líquido de R$ 3,27 bilhões….” 2026. https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/.',
    annotation="Motiva FY2025 rodovias CapEx R$6.5bn via Fed H.10. Supports motiva_fy2025_roads_65bn_brl.",
    evid_note="Opened Motiva FY2025 company news; rodovias CapEx R$6.5bn confirmed.",
)

# 10. rail / other — NEW Motiva FY2025 trilhos R$1.3bn
row_doc(
    "motiva_fy2025_rails_13bn_brl",
    "infrastructure", "rail", "other",
    "Motiva — FY2025 trilhos CapEx R$1.3bn",
    "Brazil",
    "Motiva company FY2025 results news: invested R$ 1.3 billion in rail (Trilhos), highlighting ViaMobilidade Lines 8-Diamante and 9-Esmeralda works (energy network/substations, track revitalization). CapEx: enter R$1.3bn trilhos face. Nested vs motiva_fy2025_capex_87bn_brl total / motiva_fy2025_roads_65bn_brl (not additive).",
    "1300000000", "2025-12-31", "2025", "-23.55", "-46.63",
    "Motiva ViaMobilidade Lines 8/9 (São Paulo metro pin).",
    "motiva_fy2025_results_8p3bn_2026",
    "Em T rilhos, a Companhia investiu R$ 1, 3 bilhão",
    "https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/",
    "Actor: Motiva S.A. — other. NEW nested FY2025 trilhos CapEx R$1.3bn. Shuffle rail.",
    "hunt_cycle285", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1300000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Motiva S.A. “Motiva encerra 2025 com lucro líquido de R$ 3,27 bilhões….” 2026. https://www.motiva.com.br/noticias/motiva-encerra-2025-com-lucro-liquido-de-3-bilhoes/.',
    annotation="Motiva FY2025 trilhos CapEx R$1.3bn via Fed H.10. Supports motiva_fy2025_rails_13bn_brl.",
    evid_note="Opened Motiva FY2025 company news; trilhos CapEx R$1.3bn confirmed.",
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
    print(f"cycle285 added {len(added)}: {added}")
    print(f"cycle285 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
