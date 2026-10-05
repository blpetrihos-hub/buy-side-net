#!/usr/bin/env python3
"""Cycle 260 hunt: shuffle_seed=20261260; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261260).shuffle):
building_materials, power_plants_grid, engineering_epc, niobium, water, bridges_roads,
graphite, rail, lithium, port_ownership, nickel, wind, other_renewables, copper,
port_cranes, balsa, fission_smr, solar.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: spent residual (Equinix/Ascenty/Cirion/Scala/AES Andes dense;
  Equinix SP USD109m / Progress Rail VLI R$430m without openable dual primary).
PRC equal-budget: honest residual (BYD BESS ≤R$500m / GATE R$20bn without company primary).
Allied: NEW Enel Distribuição SP 2T26 CapEx R$807.657m; NEW Enel SP 6M26 CapEx R$1,497.932m;
  NEW Enel Américas H1 Gross CapEx USD 983m; NEW Enel Américas Brazil H1 Gross CapEx USD 678m.
Other: NEW Sabesp 2Q26 CapEx R$3,731m; NEW Rumo 2T26 CapEx R$1,597m; NEW Rumo 6M26 CapEx R$3,371m;
  NEW Alupar TESP Lot 7 ANEEL CapEx R$1,089m (company 2T26 PDF via RI ZIP).
Skipped: thin dry; holdovers unsigned; Alupar TECP R$2.0518bn still not company face;
  TPC/TAP planned CapEx deferred to keep cycle focused on signed auction + spent CapEx.
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
            "fx_date": fx_date if value_usd else "", "year": year, "status": "active",
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


# 1. power_plants_grid / allied — NEW Enel Distribuição São Paulo 2T26 CapEx R$807.657m
row_doc(
    "enel_sp_2t26_capex_807p657m_brl",
    "energy", "power_plants_grid", "allied",
    "Enel Distribuição São Paulo — 2T26 CapEx R$807.657m",
    "Brazil",
    "Jul/Aug 2026 Enel Distribuição São Paulo Earnings Release 2T26/6M26 (company RI PDF): CAPEX total R$807.657 million in 2T26 (+28.3% vs 2T25); financed by company R$800.134m / by client R$7.523m. CapEx: enter R$807.657m 2T26 face. Nested vs enel_sp_6m26 / enel_brasil_25p3bn / enel_americas Brazil grids envelopes (not additive).",
    "807657000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Enel Distribuição São Paulo concession (São Paulo pin).",
    "enel_sp_2t26_6m26_release",
    "Investimentos totalizaram R$ 807,7 milhões no 2T26 e R$ 1.497,9 milhões nos 6M26 (+28,3% e +34,5% vs ano anterior) … CAPEX (R$ mil) 807.657 … 1.497.932 … Total 807.657 629.414 28,3% 1.497.932 1.113.877 34,5%.",
    "https://ri.enel.com/Documento/DownloadPublicFile?fileNameKey=c57a6f7a-0337-48b3-9ebd-2519fd6c332f.pdf&tipoPath=2",
    "Actor: Enel Distribuição São Paulo (Enel Italy) — allied. NEW nested 2T26 CapEx R$807.657m. Shuffle power_plants_grid.",
    "hunt_cycle260", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(807657000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Enel Distribuição São Paulo. “Earnings Release 2T26 / 6M26.” 2026. https://ri.enel.com/Documento/DownloadPublicFile?fileNameKey=c57a6f7a-0337-48b3-9ebd-2519fd6c332f.pdf&tipoPath=2.',
    annotation="Enel SP 2T26/6M26 CapEx via Fed H.10. Supports enel_sp_2t26_capex_807p657m_brl; enel_sp_6m26_capex_1497p932m_brl.",
    evid_note="Opened Enel Distribuição São Paulo 2T26/6M26 RI PDF; CAPEX table R$807.657m / R$1,497.932m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 2. power_plants_grid / allied — NEW Enel Distribuição São Paulo 6M26 CapEx R$1,497.932m
row_doc(
    "enel_sp_6m26_capex_1497p932m_brl",
    "energy", "power_plants_grid", "allied",
    "Enel Distribuição São Paulo — 6M26 CapEx R$1,497.932m",
    "Brazil",
    "Jul/Aug 2026 Enel Distribuição São Paulo Earnings Release 2T26/6M26: CAPEX total R$1,497.932 million in 6M26 (+34.5% vs 6M25); company notes >R$14bn invested in São Paulo since 2018 concession start through 6M26. CapEx: enter R$1,497.932m 6M26 face. Nested vs enel_sp_2t26_capex_807p657m_brl (not additive).",
    "1497932000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Enel Distribuição São Paulo concession (São Paulo pin).",
    "enel_sp_2t26_6m26_release",
    "Investimentos totalizaram R$ 807,7 milhões no 2T26 e R$ 1.497,9 milhões nos 6M26 (+28,3% e +34,5% vs ano anterior) … CAPEX (R$ mil) … 1.497.932 … Total 807.657 629.414 28,3% 1.497.932 1.113.877 34,5% … o montante investido na área de concessão totalizou R$ 1,5 bilhão.",
    "https://ri.enel.com/Documento/DownloadPublicFile?fileNameKey=c57a6f7a-0337-48b3-9ebd-2519fd6c332f.pdf&tipoPath=2",
    "Actor: Enel Distribuição São Paulo (Enel Italy) — allied. NEW nested 6M26 CapEx R$1,497.932m. Shuffle power_plants_grid.",
    "hunt_cycle260", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1497932000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Enel Distribuição São Paulo. “Earnings Release 2T26 / 6M26.” 2026. https://ri.enel.com/Documento/DownloadPublicFile?fileNameKey=c57a6f7a-0337-48b3-9ebd-2519fd6c332f.pdf&tipoPath=2.',
    annotation="Enel SP 2T26/6M26 CapEx via Fed H.10. Supports enel_sp_2t26_capex_807p657m_brl; enel_sp_6m26_capex_1497p932m_brl.",
    evid_note="Opened Enel SP 2T26/6M26 RI PDF; 6M26 CAPEX R$1,497.932m (+34.5%) confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 3. power_plants_grid / allied — NEW Enel Américas H1 2026 Gross CapEx USD 983m
row_doc(
    "enel_americas_h1_26_gross_capex_983m",
    "energy", "power_plants_grid", "allied",
    "Enel Américas — H1 2026 Gross CapEx USD 983m",
    "Chile",
    "2026 Enel Américas Q2 & H1 2026 Results Presentation: Gross CAPEX H1 2026 USD 983 mn (+4% YoY); Q2 USD 537 mn (flat YoY); Brazil leads CapEx growth; grids ~90% of mix. CapEx: enter USD 983m H1 group face (Argentina/Brazil/Colombia/Central America–Peru footprint). Nested vs Brazil H1 USD 678m row and 2026–28 Brazil grids plan (not additive).",
    "983000000", "2026-06-30", "2026", "-33.45", "-70.66",
    "Enel Américas LatAm grids/generation footprint (Santiago HQ pin; multi-country).",
    "enel_americas_q2_h1_2026_presentation",
    "Gross CAPEX … Focus on Grids aligned with Strategic Plan goals; Brazil leads CAPEX growth … H1 2026 … USD 983 mn (+4% YoY) … USD 537 mn (Flat YoY).",
    "https://www.enelamericas.com/content/dam/enel-americas/investor/presentaciones-de-resultados/resultados-trimestrales/presentaciones/2026/Enel-Americas-Q2-2026-Results-Presentation.pdf",
    "Actor: Enel Américas (Enel SpA Italy; Chile-listed) — allied. NEW nested H1 2026 Gross CapEx USD 983m. Shuffle power_plants_grid.",
    "hunt_cycle260", investment_type="corporate_capex", evidence="documented", currency="USD",
    value_usd="983000000", fx_usd="1", bib_type="company",
    chicago='Enel Américas S.A. “Q2 & H1 2026 Results Presentation.” 2026. https://www.enelamericas.com/content/dam/enel-americas/investor/presentaciones-de-resultados/resultados-trimestrales/presentaciones/2026/Enel-Americas-Q2-2026-Results-Presentation.pdf.',
    annotation="Enel Américas H1 Gross CapEx USD 983m / Brazil H1 USD 678m. Supports enel_americas_h1_26_gross_capex_983m; enel_americas_brazil_h1_26_gross_capex_678m.",
    evid_note="Opened Enel Américas Q2/H1 2026 results PDF; Gross CAPEX H1 USD 983m and Brazil H1 Gross Capex Gen 28 + Grids 650 = Total 678 confirmed.",
)

# 4. power_plants_grid / allied — NEW Enel Américas Brazil H1 Gross CapEx USD 678m
row_doc(
    "enel_americas_brazil_h1_26_gross_capex_678m",
    "energy", "power_plants_grid", "allied",
    "Enel Américas — Brazil H1 2026 Gross CapEx USD 678m",
    "Brazil",
    "2026 Enel Américas Q2 & H1 2026 Results Presentation Brazil cumulative table: Gross Capex H1 2026 Generation USD 28m (−54%) / Grids USD 650m (+42%) / Total USD 678m (+31% vs H1 2025 USD 518m). CapEx: enter USD 678m Brazil H1 face. Nested vs group H1 USD 983m and enel_sp spent R$ envelopes (not additive).",
    "678000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Enel Américas Brazil grids/generation concessions (São Paulo pin).",
    "enel_americas_q2_h1_2026_presentation",
    "Brazil (USD mn) … Cumulative results … Gross Capex … H1 2025 60 / H1 2026 28 (−54%) Generation; … 458 / 650 (+42%) Grids; … 518 / 678 (+31%) Total.",
    "https://www.enelamericas.com/content/dam/enel-americas/investor/presentaciones-de-resultados/resultados-trimestrales/presentaciones/2026/Enel-Americas-Q2-2026-Results-Presentation.pdf",
    "Actor: Enel Américas (Enel Italy) — allied. NEW nested Brazil H1 2026 Gross CapEx USD 678m. Shuffle power_plants_grid.",
    "hunt_cycle260", investment_type="corporate_capex", evidence="documented", currency="USD",
    value_usd="678000000", fx_usd="1", bib_type="company",
    chicago='Enel Américas S.A. “Q2 & H1 2026 Results Presentation.” 2026. https://www.enelamericas.com/content/dam/enel-americas/investor/presentaciones-de-resultados/resultados-trimestrales/presentaciones/2026/Enel-Americas-Q2-2026-Results-Presentation.pdf.',
    annotation="Enel Américas H1 Gross CapEx USD 983m / Brazil H1 USD 678m. Supports enel_americas_h1_26_gross_capex_983m; enel_americas_brazil_h1_26_gross_capex_678m.",
    evid_note="Opened Enel Américas Q2/H1 2026 PDF Brazil cumulative Gross Capex Total H1 2026 USD 678m (Grids 650 + Gen 28).",
)

# 5. water / other — NEW Sabesp 2Q26 CapEx R$3,731m (nested under 1H26)
row_doc(
    "sabesp_2q26_capex_3731m_brl",
    "resources", "water", "other",
    "Sabesp — 2Q26 CapEx R$3,731m",
    "Brazil",
    "Sabesp 2Q26 Earnings Release (SEC Form 6-K): Capex in 2Q26 totaled R$3,731 mn (+3.6% y/y); water R$1,050m / sewage R$2,680m. CapEx: enter R$3,731m 2Q26 face. Nested vs sabesp_1h26_capex_7458m_brl / ~R$20bn FY2026 plan (not additive).",
    "3731000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Sabesp São Paulo state water/sewage concession (São Paulo pin).",
    "sabesp_2q26_sec_6k_2026",
    "In 2Q26, Capex totaled R$ 3,731 mn, an increase of 3.6% compared to the same period of the previous year. Investments in 1H26 reached R$ 7,458 mn … Water 1,050 … Sewage 2,680 … Total 3,731.",
    "https://www.sec.gov/Archives/edgar/data/1170858/000129281426004252/sbsitr2q26_6k.htm",
    "Actor: Sabesp — other. NEW nested 2Q26 CapEx R$3,731m under already-logged 1H26 envelope. Shuffle water.",
    "hunt_cycle260", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(3731000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Companhia de Saneamento Básico do Estado de São Paulo — Sabesp. “Form 6-K — Earnings Release 2Q26.” 2026. https://www.sec.gov/Archives/edgar/data/1170858/000129281426004252/sbsitr2q26_6k.htm.',
    annotation="Sabesp 2Q26/1H26/FY2026 CapEx via Fed H.10. Supports sabesp_1h26_capex_7458m_brl; sabesp_2026_capex_plan_20bn_brl; sabesp_2q26_capex_3731m_brl.",
    evid_note="Opened Sabesp SEC 6-K 2Q26; Capex R$3,731m (water 1,050 / sewage 2,680) confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 6. rail / other — NEW Rumo 2T26 CapEx R$1,597m
row_doc(
    "rumo_2t26_capex_1597m_brl",
    "infrastructure", "rail", "other",
    "Rumo — 2T26 CapEx R$1,597m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26 (company RI PDF): Investimentos totalizaram R$1.597 milhões in 2T26 (+14.5% vs 2T25 R$1.395m). CapEx: enter R$1,597m 2T26 face. Nested vs rumo_6m26_capex_3371m_brl (not additive).",
    "1597000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).",
    "rumo_2t26_release_20260812",
    "Investimentos totalizaram R$1.597 milhões. … 1.597 1.395 14,5 % Capex 3.371 3.175 6,2 %.",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. (Cosan Brazilian freight rail) — other. NEW 2T26 CapEx R$1,597m. Shuffle rail.",
    "hunt_cycle260", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1597000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo 2T26/6M26 CapEx via Fed H.10. Supports rumo_2t26_capex_1597m_brl; rumo_6m26_capex_3371m_brl.",
    evid_note="Opened Rumo company 2T26 results PDF; Capex R$1,597m / 6M26 R$3,371m confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 7. rail / other — NEW Rumo 6M26 CapEx R$3,371m
row_doc(
    "rumo_6m26_capex_3371m_brl",
    "infrastructure", "rail", "other",
    "Rumo — 6M26 CapEx R$3,371m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex 6M26 R$3,371 million (+6.2% vs 6M25 R$3,175m). CapEx: enter R$3,371m 6M26 face. Nested vs rumo_2t26_capex_1597m_brl (not additive).",
    "3371000000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Rumo Brazil freight-rail network (São Paulo HQ pin; multi-corridor).",
    "rumo_2t26_release_20260812",
    "1.597 1.395 14,5 % Capex 3.371 3.175 6,2 % … Capex 3,371 3,175 6.2 %.",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested 6M26 CapEx R$3,371m. Shuffle rail.",
    "hunt_cycle260", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(3371000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo 2T26/6M26 CapEx via Fed H.10. Supports rumo_2t26_capex_1597m_brl; rumo_6m26_capex_3371m_brl.",
    evid_note="Opened Rumo 2T26 company PDF; 6M26 Capex R$3,371m (+6.2%) confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)

# 8. power_plants_grid / other — NEW Alupar TESP Lot 7 ANEEL CapEx R$1,089m
row_doc(
    "alupar_lote7_tesp_1089m_brl_2026",
    "energy", "power_plants_grid", "other",
    "Alupar — TESP Lot 7 (ANEEL 01/2026 E2) CapEx R$1,089m",
    "Brazil",
    "6 Aug 2026 Alupar Investimento 2T26 earnings release (company RI ZIP PDF): TESP (Lote 7 do Leilão 01/2026, Etapa 2) in São Paulo — 1 substation + 17.4 km underground transmission; investimento previsto pelo regulador R$1.089 mm; RAP vencedora R$96.7 mm. CapEx: enter R$1,089m ANEEL auction CapEx face. Distinct from alupar_growth_cycle_8p1bn_brl envelope.",
    "1089000000", "2026-07-31", "2026", "-23.55", "-46.63",
    "Alupar TESP Lot 7 São Paulo underground TX / substation (São Paulo pin).",
    "alupar_2t26_release_20260806",
    "O projeto TESP (Lote 7 do Leilão 01/2026, Etapa 2): localizado em São Paulo … implantação de 1 subestação e de 17,4 km em linhas de transmissão subterrâneas. O investimento previsto pelo regulador é R$ 1.089 mm e a RAP vencedora é de R$ 96,7 mm. … Investimento Aneel: R$ 1.089 mm*.",
    "https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip",
    "Actor: Alupar Investimento (Brazilian private holding) — other. NEW Lot 7/TESP ANEEL CapEx R$1,089m from openable company 2T26 PDF. Shuffle power_plants_grid.",
    "hunt_cycle260", investment_type="greenfield", evidence="documented", currency="BRL",
    value_usd=str(round(1089000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Alupar Investimento S.A. “Release de Resultados 2T26.” August 6, 2026. https://cdn-sites-assets.mziq.com/wp-content/uploads/sites/4/2026/08/2T26-1.zip.',
    annotation="Alupar 2T26 company release (ZIP) Lot 7 TESP R$1,089m ANEEL CapEx via Fed H.10. Supports alupar_lote7_tesp_1089m_brl_2026.",
    evid_note="Opened Alupar 2T26 RI ZIP (2026_07_30_Release_2T26_PT.pdf); TESP Lot 7 regulator CapEx R$1,089 mm / RAP R$96.7 mm confirmed. CapEx USD via Fed H.10 Sep 25 2026 5.1921.",
)


def upsert_bib(bib, bib_by, bib_e):
    sid = bib_e["id"]
    entry = {
        "id": sid,
        "type": bib_e.get("type", "company"),
        "chicago": bib_e["chicago"],
        "url": bib_e["url"],
        "annotation": bib_e.get("annotation", ""),
        "supports": bib_e.get("supports", []),
    }
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        # merge supports
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
    # ensure sabesp bib supports includes new nested id
    if "sabesp_2q26_sec_6k_2026" in bib_by:
        e = bib[bib_by["sabesp_2q26_sec_6k_2026"]]
        supp = list(dict.fromkeys((e.get("supports") or []) + [
            "sabesp_2q26_capex_3731m_brl", "hunt_cycle260"
        ]))
        e["supports"] = supp
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    BIB.write_text(
        yaml.safe_dump(bib, allow_unicode=True, sort_keys=False, width=1000),
        encoding="utf-8",
    )
    print(f"cycle260 added {len(added)}: {added}")
    print(f"cycle260 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
