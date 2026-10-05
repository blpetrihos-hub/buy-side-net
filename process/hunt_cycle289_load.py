#!/usr/bin/env python3
"""Cycle 289 hunt: shuffle_seed=20261289; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261289).shuffle):
fission_smr, engineering_epc, graphite, wind, nickel, balsa, niobium, solar,
power_plants_grid, other_renewables, lithium, rail, water, bridges_roads,
port_cranes, copper, building_materials, port_ownership.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry
  (fission_smr also first in shuffle — dry).
≥1/3 U.S. hunt budget: AES Andes Arenales CapEx-fill probe (still blank; Pampas+
  Cristales USD1.1bn already logged); SSA Guaymas STS CapEx blank (Maritime Pro /
  Radar Sonora MXN424.8m already on TUM concession face); FCX Cerro Verde /
  GE Vernova Azulão / DFC Piauí IPS / Equinix / Progress Rail VLI R$430m — CapEx
  blanks or already logged; no new US CapEx face this cycle.
PRC equal-budget: Goldwind/Sungrow/BYD/CTG CapEx-blank COD faces; CPFL residual
  dense after 288.
ALLIED equal-budget: NEW Neoenergia 6M26 nested Distribuição CapEx categories
  (Novas Ligações / Novas SE's e RD's / Renovação de Ativos / Melhoria da Rede);
  NEW ISA Energia Brasil 1S26 total CapEx + licitados + Serra Dourada / Piraquê /
  Itatiaia 2T26 spend faces (earnings release PDF).
OTHER equal-budget: NEW Equatorial 2T26 per-distributor Totals (PA / GO / MA).
Skipped: thin dry; fission_smr/engineering_epc/graphite/wind/nickel/balsa/
  niobium/solar/other_renewables/lithium/rail/water/bridges_roads/port_cranes/
  copper/building_materials/port_ownership dense or CapEx-blank; Motiva airports
  taxonomy-out; holdovers unsigned.
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
NEO_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/2aec7c3f-0df1-4df1-967a-66ab1030fc14/"
    "145001e6-59ad-7b1b-90fd-dc40064b1382?origin=2"
)
ISA_URL = (
    "https://ri.isaenergiabrasil.com.br/pt/documentos/"
    "6758-Earnings-Release-2T26-vfinal.pdf"
)
EQ_URL = (
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/"
    "b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2"
)


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


# --- Neoenergia 6M26 nested Distribuição CapEx (allied) ---
row_doc(
    "neoenergia_novas_ligacoes_6m26_1278m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — Distribuição Novas Ligações CapEx 6M26 R$1.278bn",
    "Brazil",
    "21 Jul 2026 Neoenergia 2T26/6M26 release: Distribuição CapEx table — Novas Ligações consolidado 6M26 R$1,278 million. CapEx: enter R$1.278bn face. Nested under Dist CapEx R$3.696bn / network expansion R$2.265bn siblings (not additive).",
    "1278000000", "2026-07-21", "2026", "-22.91", "-43.17",
    "Neoenergia distribution companies (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Novas Ligações … 1.278",
    NEO_URL,
    "Actor: Neoenergia (Iberdrola) — allied. NEW 6M26 Novas Ligações R$1.278bn. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle289", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1278000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Earnings Release 2Q26 / 6M26” (company MZ IQ PDF). ' + NEO_URL + ".",
    annotation="Neoenergia 6M26 Novas Ligações R$1.278bn via Fed H.10. Supports neoenergia_novas_ligacoes_6m26_1278m_brl.",
    evid_note="Opened Neoenergia 2T26/6M26 PDF; Distribuição Novas Ligações consolidado 6M26 R$1,278m confirmed.",
)

row_doc(
    "neoenergia_novas_ses_rds_6m26_831m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — Distribuição Novas SE's e RD's CapEx 6M26 R$831m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2T26/6M26 release: Distribuição CapEx table — Novas SE's e RD's consolidado 6M26 R$831 million. CapEx: enter R$831m face. Nested under Dist CapEx R$3.696bn (not additive).",
    "831000000", "2026-07-21", "2026", "-22.91", "-43.17",
    "Neoenergia distribution substations / distribution networks (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Novas SE's e RD's … 831",
    NEO_URL,
    "Actor: Neoenergia (Iberdrola) — allied. NEW 6M26 Novas SE's e RD's R$831m. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle289", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(831000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Earnings Release 2Q26 / 6M26” (company MZ IQ PDF). ' + NEO_URL + ".",
    annotation="Neoenergia 6M26 Novas SE's e RD's R$831m via Fed H.10. Supports neoenergia_novas_ses_rds_6m26_831m_brl.",
    evid_note="Opened Neoenergia 2T26/6M26 PDF; Novas SE's e RD's consolidado 6M26 R$831m confirmed.",
)

row_doc(
    "neoenergia_renovacao_ativos_6m26_674m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — Distribuição Renovação de Ativos CapEx 6M26 R$674m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2T26/6M26 release: Distribuição CapEx table — Renovação de Ativos consolidado 6M26 R$674 million. CapEx: enter R$674m face. Nested under Dist CapEx R$3.696bn (not additive).",
    "674000000", "2026-07-21", "2026", "-22.91", "-43.17",
    "Neoenergia distribution asset renewal (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Renovação de Ativos … 674",
    NEO_URL,
    "Actor: Neoenergia (Iberdrola) — allied. NEW 6M26 Renovação de Ativos R$674m. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle289", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(674000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Earnings Release 2Q26 / 6M26” (company MZ IQ PDF). ' + NEO_URL + ".",
    annotation="Neoenergia 6M26 Renovação de Ativos R$674m via Fed H.10. Supports neoenergia_renovacao_ativos_6m26_674m_brl.",
    evid_note="Opened Neoenergia 2T26/6M26 PDF; Renovação de Ativos consolidado 6M26 R$674m confirmed.",
)

row_doc(
    "neoenergia_melhoria_rede_6m26_276m_brl",
    "energy", "power_plants_grid", "allied",
    "Neoenergia — Distribuição Melhoria da Rede CapEx 6M26 R$276m",
    "Brazil",
    "21 Jul 2026 Neoenergia 2T26/6M26 release: Distribuição CapEx table — Melhoria da Rede consolidado 6M26 R$276 million. CapEx: enter R$276m face. Nested under Dist CapEx R$3.696bn (not additive).",
    "276000000", "2026-07-21", "2026", "-22.91", "-43.17",
    "Neoenergia distribution network improvement (Rio de Janeiro HQ pin).",
    "neoenergia_2q26_release_mziq",
    "Melhoria da Rede … 276",
    NEO_URL,
    "Actor: Neoenergia (Iberdrola) — allied. NEW 6M26 Melhoria da Rede R$276m. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle289", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(276000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Neoenergia S.A. “Earnings Release 2Q26 / 6M26” (company MZ IQ PDF). ' + NEO_URL + ".",
    annotation="Neoenergia 6M26 Melhoria da Rede R$276m via Fed H.10. Supports neoenergia_melhoria_rede_6m26_276m_brl.",
    evid_note="Opened Neoenergia 2T26/6M26 PDF; Melhoria da Rede consolidado 6M26 R$276m confirmed.",
)

# --- ISA Energia Brasil CapEx nested (allied) ---
row_doc(
    "isa_energia_1s26_capex_2275p9m_brl",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — CapEx 1S26 R$2,275.9m",
    "Brazil",
    "ISA Energia Brasil Earnings Release 2T26: total investments 1S26 R$2,275.9 million (+3.0% vs 1S25), of which R&M 35.8%. CapEx: enter R$2,275.9m face. Distinct from 2T26 R$1,053.5m nested quarter (not additive to 2T26 alone).",
    "2275900000", "2026-06-30", "2026", "-23.55", "-46.63",
    "ISA Energia Brasil transmission portfolio (São Paulo HQ pin).",
    "isa_energia_2t26_earnings_release",
    "o total de investimentos realizado no primeiro semestre de 2026 foi de R$ 2.275,9 milhões",
    ISA_URL,
    "Actor: ISA Energia Brasil — allied. NEW 1S26 CapEx R$2,275.9m. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle289", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2275900000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “Earnings Release 2T26.” 2026. ' + ISA_URL + ".",
    annotation="ISA Energia Brasil 1S26 CapEx R$2,275.9m via Fed H.10. Supports isa_energia_1s26_capex_2275p9m_brl.",
    evid_note="Opened ISA Energia Brasil 2T26 Earnings Release PDF; 1S26 investments R$2,275.9m confirmed.",
)

row_doc(
    "isa_energia_1s26_licitados_1460p4m_brl",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — greenfield/licitados CapEx 1S26 R$1,460.4m",
    "Brazil",
    "ISA Energia Brasil Earnings Release 2T26: investimentos em projetos licitados totalizaram R$1,460.4 million in 1S26 (−4.2% vs 1S25). CapEx: enter R$1,460.4m face. Nested under 1S26 total R$2,275.9m with R&M R$815.4m (not additive).",
    "1460400000", "2026-06-30", "2026", "-23.55", "-46.63",
    "ISA Energia Brasil greenfield transmission lots (São Paulo HQ pin).",
    "isa_energia_2t26_earnings_release",
    "os investimentos em projetos licitados totalizaram R$ 1.460,4 milhões no 1S26",
    ISA_URL,
    "Actor: ISA Energia Brasil — allied. NEW 1S26 licitados CapEx R$1,460.4m. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle289", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1460400000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “Earnings Release 2T26.” 2026. ' + ISA_URL + ".",
    annotation="ISA Energia Brasil 1S26 licitados R$1,460.4m via Fed H.10. Supports isa_energia_1s26_licitados_1460p4m_brl.",
    evid_note="Opened ISA Energia Brasil 2T26 Earnings Release PDF; 1S26 licitados R$1,460.4m confirmed.",
)

row_doc(
    "isa_energia_serra_dourada_2t26_455p7m_brl",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — Serra Dourada CapEx spend 2T26 R$455.7m",
    "Brazil",
    "ISA Energia Brasil Earnings Release 2T26: 2T26 licitados spend directed mainly to Serra Dourada (R$455.7 million), which reached 49% physical progress in 2T26. CapEx: enter R$455.7m quarterly spend face. Nested vs project CapEx total ~R$3.2bn / remanescente faces (not additive).",
    "455700000", "2026-06-30", "2026", "-11.09", "-43.14",
    "Serra Dourada transmission lot (BA/MG; prior Serra Dourada pin).",
    "isa_energia_2t26_earnings_release",
    "Serra Dourada (R$ 455,7 milhões), que atingiu 49% de avanço físico no 2T26",
    ISA_URL,
    "Actor: ISA Energia Brasil — allied. NEW Serra Dourada 2T26 spend R$455.7m. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle289", investment_type="greenfield", evidence="documented", currency="BRL",
    value_usd=str(round(455700000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “Earnings Release 2T26.” 2026. ' + ISA_URL + ".",
    annotation="ISA Serra Dourada 2T26 spend R$455.7m via Fed H.10. Supports isa_energia_serra_dourada_2t26_455p7m_brl.",
    evid_note="Opened ISA Energia Brasil 2T26 Earnings Release PDF; Serra Dourada 2T26 R$455.7m confirmed.",
)

row_doc(
    "isa_energia_piraque_2t26_84p4m_brl",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — Piraquê CapEx spend 2T26 R$84.4m",
    "Brazil",
    "ISA Energia Brasil Earnings Release 2T26: 2T26 licitados spend includes Piraquê R$84.4 million (bloco 3 energized June 2026). CapEx: enter R$84.4m quarterly spend face. Nested under 2T26 licitados R$608.1m (not additive).",
    "84400000", "2026-06-30", "2026", "-23.55", "-46.63",
    "Piraquê transmission project (company portfolio; São Paulo HQ pin — site coords not separately mapped).",
    "isa_energia_2t26_earnings_release",
    "Piraquê (R$ 84,4 milhões)",
    ISA_URL,
    "Actor: ISA Energia Brasil — allied. NEW Piraquê 2T26 spend R$84.4m. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle289", investment_type="greenfield", evidence="documented", currency="BRL",
    value_usd=str(round(84400000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “Earnings Release 2T26.” 2026. ' + ISA_URL + ".",
    annotation="ISA Piraquê 2T26 spend R$84.4m via Fed H.10. Supports isa_energia_piraque_2t26_84p4m_brl.",
    evid_note="Opened ISA Energia Brasil 2T26 Earnings Release PDF; Piraquê 2T26 R$84.4m confirmed.",
)

row_doc(
    "isa_energia_itatiaia_2t26_52p2m_brl",
    "energy", "power_plants_grid", "allied",
    "ISA Energia Brasil — Itatiaia CapEx spend 2T26 R$52.2m",
    "Brazil",
    "ISA Energia Brasil Earnings Release 2T26: 2T26 licitados spend includes Itatiaia R$52.2 million (33% physical progress at quarter-end; RJ/MG Lote 7). CapEx: enter R$52.2m quarterly spend face. Nested under 2T26 licitados R$608.1m / project CapEx table (not additive).",
    "52200000", "2026-06-30", "2026", "-22.50", "-44.56",
    "Itatiaia transmission lot RJ/MG (Itatiaia region pin).",
    "isa_energia_2t26_earnings_release",
    "Itatiaia (R$ 52,2 milhões), que terminou o trimestre com 33% de avanço físico",
    ISA_URL,
    "Actor: ISA Energia Brasil — allied. NEW Itatiaia 2T26 spend R$52.2m. Shuffle power_plants_grid; allied equal-budget.",
    "hunt_cycle289", investment_type="greenfield", evidence="documented", currency="BRL",
    value_usd=str(round(52200000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='ISA Energia Brasil. “Earnings Release 2T26.” 2026. ' + ISA_URL + ".",
    annotation="ISA Itatiaia 2T26 spend R$52.2m via Fed H.10. Supports isa_energia_itatiaia_2t26_52p2m_brl.",
    evid_note="Opened ISA Energia Brasil 2T26 Earnings Release PDF; Itatiaia 2T26 R$52.2m confirmed.",
)

# --- Equatorial 2T26 per-distributor Totals (other) ---
row_doc(
    "equatorial_pa_2t26_716m_brl",
    "energy", "power_plants_grid", "other",
    "Equatorial Pará — Distribuição CapEx Total 2T26 R$716m",
    "Brazil",
    "12 Aug 2026 Equatorial 2T26 release: Investimentos Distribuidoras table — PA Total 2T26 R$716 million (Ativos elétricos R$362m + Obrigações especiais R$329m + Ativos não elétricos R$25m). CapEx: enter R$716m face. Nested under Dist Total R$2.527bn (not additive).",
    "716000000", "2026-08-12", "2026", "-1.46", "-48.50",
    "Equatorial Pará distribution (Belém pin).",
    "equatorial_2t26_release_20260812",
    "Total … 716",
    EQ_URL,
    "Actor: Equatorial Pará — other. NEW 2T26 PA Total CapEx R$716m. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle289", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(716000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. ' + EQ_URL + ".",
    annotation="Equatorial PA 2T26 Total R$716m via Fed H.10. Supports equatorial_pa_2t26_716m_brl.",
    evid_note="Opened Equatorial 2T26 PDF; PA Distribuição Total 2T26 R$716m confirmed.",
)

row_doc(
    "equatorial_go_2t26_675m_brl",
    "energy", "power_plants_grid", "other",
    "Equatorial Goiás — Distribuição CapEx Total 2T26 R$675m",
    "Brazil",
    "12 Aug 2026 Equatorial 2T26 release: Investimentos Distribuidoras table — GO Total 2T26 R$675 million (Ativos elétricos R$611m + Obrigações especiais R$20m + Ativos não elétricos R$44m). CapEx: enter R$675m face. Nested under Dist Total R$2.527bn (not additive).",
    "675000000", "2026-08-12", "2026", "-16.69", "-49.25",
    "Equatorial Goiás distribution (Goiânia pin).",
    "equatorial_2t26_release_20260812",
    "Total … 675",
    EQ_URL,
    "Actor: Equatorial Goiás — other. NEW 2T26 GO Total CapEx R$675m. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle289", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(675000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. ' + EQ_URL + ".",
    annotation="Equatorial GO 2T26 Total R$675m via Fed H.10. Supports equatorial_go_2t26_675m_brl.",
    evid_note="Opened Equatorial 2T26 PDF; GO Distribuição Total 2T26 R$675m confirmed.",
)

row_doc(
    "equatorial_ma_2t26_330m_brl",
    "energy", "power_plants_grid", "other",
    "Equatorial Maranhão — Distribuição CapEx Total 2T26 R$330m",
    "Brazil",
    "12 Aug 2026 Equatorial 2T26 release: Investimentos Distribuidoras table — MA Total 2T26 R$330 million (Ativos elétricos R$279m + Obrigações especiais R$30m + Ativos não elétricos R$21m). CapEx: enter R$330m face. Nested under Dist Total R$2.527bn (not additive).",
    "330000000", "2026-08-12", "2026", "-2.53", "-44.30",
    "Equatorial Maranhão distribution (São Luís pin).",
    "equatorial_2t26_release_20260812",
    "Total … 330",
    EQ_URL,
    "Actor: Equatorial Maranhão — other. NEW 2T26 MA Total CapEx R$330m. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle289", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(330000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. ' + EQ_URL + ".",
    annotation="Equatorial MA 2T26 Total R$330m via Fed H.10. Supports equatorial_ma_2t26_330m_brl.",
    evid_note="Opened Equatorial 2T26 PDF; MA Distribuição Total 2T26 R$330m confirmed.",
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
    print(f"cycle289 added {len(added)}: {added}")
    print(f"cycle289 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
