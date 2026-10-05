#!/usr/bin/env python3
"""Cycle 288 hunt: shuffle_seed=20261288; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261288).shuffle):
other_renewables, power_plants_grid, water, lithium, graphite, port_cranes, wind,
balsa, nickel, solar, fission_smr, niobium, port_ownership, bridges_roads, copper,
engineering_epc, building_materials, rail.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: NEW AES Brasil 2025E Modernization R$213.9m + Pipeline
  R$0.3m (Material Fact residual faces); NEW AES Andes Chile CapEx envelope
  USD2.5bn 2024–2027 (San Matías COD release); Equinix/Ascenty/SSA/Wabtec/
  Progress Rail CapEx blanks; EXIM probes.
PRC equal-budget: NEW CPFL Cidade Industrial revitalization R$162m (Canoas) +
  two live-line trucks ~R$2.6m each (~R$5.2m) via Wayback JC (live paywall);
  SGBH RS 2025 reopened (supplier opex / social not CapEx).
OTHER equal-budget: NEW Equatorial 2T26 nested Ativos elétricos R$1.933bn +
  Obrigações especiais R$460m (company 2T26 release).
Skipped: thin dry; water/lithium/graphite/port_cranes/wind/solar/niobium/
  port_ownership/bridges_roads/copper/engineering_epc/building_materials/rail
  dense or CapEx-blank; Motiva airports taxonomy-out; holdovers unsigned;
  San Matías project-level CapEx still blank (envelope only).
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
JC_WAYBACK = (
    "https://web.archive.org/web/20250424183808/"
    "https://www.jornaldocomercio.com/economia/2025/04/"
    "1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html"
)
JC_LIVE = (
    "https://www.jornaldocomercio.com/economia/2025/04/"
    "1199907-cpfl-investira-rs-39-bilhoes-no-sistema-gaucho-de-transmissao-ate-2029.html"
)
AES_MF = (
    "https://api.mziq.com/mzfilemanager/v2/d/e498993c-3cba-4d72-b30c-36dab672b462/"
    "d1fcd476-a595-8eb6-5212-a19e494bc3e0?origin=1"
)
EQ_2T26 = (
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/"
    "b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2"
)
SAN_MATIAS = (
    "https://www.aesandes.com/en/press-release/"
    "aes-andes-initiates-commercial-operation-san-matias-and-consolidates-its-wind"
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


# 1. other_renewables / us — NEW AES Andes Chile CapEx envelope USD2.5bn 2024–2027
row_doc(
    "aes_andes_chile_capex_2p5bn_2024_2027",
    "energy", "other_renewables", "us",
    "AES Andes — Chile renewable CapEx envelope >USD2.5bn 2024–2027",
    "Chile",
    "27 Jun 2024 AES Andes English (San Matías COD): Chile projects under construction for 767 MW renewable capacity plus 1,700 MW under development already contracted, with expected investments exceeding US$2.5 billion between 2024 and 2027. CapEx: enter USD2.5bn envelope face. Distinct from later Solar IV USD1.9bn / Jan 2025 USD2.0bn faces and Greentegra spent USD2.3bn (not additive; successive envelope disclosures).",
    "2500000000", "2024-06-27", "2024", "-23.65", "-70.40",
    "AES Andes Chile renewable portfolio under construction / development (Antofagasta region pin).",
    "aes_andes_san_matias_cod_20240627",
    "all with expected investments exceeding US$2.5 billion between 2024 and 2027",
    SAN_MATIAS,
    "Actor: AES Andes — us. NEW Chile CapEx envelope >USD2.5bn 2024–2027. Shuffle other_renewables; ≥1/3 U.S. hunt.",
    "hunt_cycle288", investment_type="corporate_capex", evidence="documented", currency="USD",
    bib_type="company",
    chicago='AES Andes. “AES Andes initiates commercial operation of San Matías and consolidates its wind generation.” June 27, 2024. '
    + SAN_MATIAS + ".",
    annotation="AES Andes Chile CapEx envelope >USD2.5bn 2024–2027 (San Matías COD). Supports aes_andes_chile_capex_2p5bn_2024_2027.",
    evid_note="Opened AES Andes San Matías COD English release; Chile investments exceeding US$2.5bn 2024–2027 confirmed.",
)

# 2. power_plants_grid / us — NEW AES Brasil 2025E Modernization R$213.9m
row_doc(
    "aes_brasil_2025e_modernization_213p9m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2025E Modernization and Maintenance R$213.9m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: Modernization and Maintenance 2025E R$213.9 million (nested under Total Investments 2025E R$214.2m with Pipeline R$0.3m). CapEx: enter R$213.9m face. Distinct from Total Investments / Capitalized Interest faces (not additive).",
    "213900000", "2024-02-26", "2025", "-23.55", "-46.63",
    "AES Brasil operating generation assets modernization (São Paulo HQ pin).",
    "aes_brasil_mf_capex_20240226",
    "Modernization and Maintenance 193.9 213.9 136.7 125.5 159.5 829.4",
    AES_MF,
    "Actor: AES Brasil — us. NEW 2025E Modernization and Maintenance R$213.9m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle288", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(213900000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. ' + AES_MF + ".",
    annotation="AES Brasil 2025E Modernization R$213.9m via Fed H.10. Supports aes_brasil_2025e_modernization_213p9m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2025E Modernization and Maintenance R$213.9m confirmed.",
)

# 3. power_plants_grid / us — NEW AES Brasil 2025E Pipeline R$0.3m
row_doc(
    "aes_brasil_2025e_pipeline_0p3m_brl",
    "energy", "power_plants_grid", "us",
    "AES Brasil — 2025E Pipeline Development (Cajuína / AGV VII) R$0.3m",
    "Brazil",
    "26 Feb 2024 AES Brasil Material Fact: Pipeline Development — Cajuína (Phases 3 and 4) and AGV VII 2025E R$0.3 million (nested under Total Investments 2025E R$214.2m). CapEx: enter R$0.3m face. Distinct from Total / Modernization / prior Pipeline 2024E R$130.6m (not additive).",
    "300000", "2024-02-26", "2025", "-5.19", "-37.34",
    "Cajuína wind pipeline / AGV VII solar development (Rio Grande do Norte pin).",
    "aes_brasil_mf_capex_20240226",
    "Pipeline Development - Cajuína (Phases 3 and 4) and AGV VII 130.6 0.3 0.0 0.0 0.0 130.8",
    AES_MF,
    "Actor: AES Brasil — us. NEW 2025E Pipeline Development R$0.3m. Shuffle power_plants_grid; ≥1/3 U.S. hunt.",
    "hunt_cycle288", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(300000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='AES Brasil Energia S.A. “Material Fact” (investment projections 2024–2028). February 26, 2024. ' + AES_MF + ".",
    annotation="AES Brasil 2025E Pipeline R$0.3m via Fed H.10. Supports aes_brasil_2025e_pipeline_0p3m_brl.",
    evid_note="Opened AES Brasil Material Fact PDF; 2025E Pipeline Development R$0.3m confirmed.",
)

# 4. power_plants_grid / prc — NEW CPFL Cidade Industrial revitalization R$162m
row_doc(
    "cpfl_cidade_industrial_162m_brl_2025",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — Cidade Industrial substation revitalization R$162m (Canoas)",
    "Brazil",
    "24 Apr 2025 Jornal do Comércio (Wayback full text; live paywall): CPFL concluded revitalization of Cidade Industrial substation in Canoas, RS — investment R$162 million raising capacity from 400 MVA to 600 MVA. CapEx: enter R$162m face. Nested vs Nova Prata 2 R$78m / Lote 3 ~R$1.1bn / RS cycle R$3.9bn (not additive). UNVERIFIED press proxy quoting company.",
    "162000000", "2025-04-24", "2025", "-29.9177", "-51.1836",
    "Subestação Cidade Industrial, Canoas, Rio Grande do Sul.",
    "jornal_comercio_cpfl_tx_rs_20250424_wayback",
    "O investimento na iniciativa foi de R$ 162 milhões, o que possibilitou a elevação da capacidade de fornecimento de energia de 400 MVA para 600 MVA",
    JC_WAYBACK,
    "Actor: CPFL Transmissão (State Grid–controlled) — prc. NEW Cidade Industrial revitalization R$162m (Wayback JC). Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle288", investment_type="brownfield_expansion", evidence="proxy", currency="BRL",
    value_usd=str(round(162000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Klein, Jefferson. “CPFL investirá R$ 3,9 bilhões no sistema gaúcho de transmissão até 2029.” Jornal do Comércio, April 24, 2025. Wayback Machine snapshot. '
    + JC_WAYBACK + f" (live: {JC_LIVE}).",
    annotation="CPFL Cidade Industrial R$162m via Fed H.10 (Wayback JC; UNVERIFIED press). Supports cpfl_cidade_industrial_162m_brl_2025.",
    evid_note="Opened Wayback JC 24 Apr 2025 snapshot; Cidade Industrial revitalization R$162m (400→600 MVA) confirmed.",
)

# 5. power_plants_grid / prc — NEW CPFL live-line trucks 2×~R$2.6m (~R$5.2m)
row_doc(
    "cpfl_live_line_trucks_52m_brl_2025",
    "energy", "power_plants_grid", "prc",
    "CPFL Transmissão — two North-American-tech live-line trucks ~R$5.2m",
    "Brazil",
    "24 Apr 2025 Jornal do Comércio (Wayback full text; live paywall): at Cidade Industrial ceremony CPFL presented one of two trucks with North American technology for live-line work up to 230 kV; each vehicle cost about R$2.6 million (aerial basket to 28 m). CapEx: enter 2×R$2.6m = R$5.2m face. Nested vs Cidade Industrial R$162m (not additive). UNVERIFIED press proxy quoting company; US tech origin noted but CapEx is CPFL spend (prc).",
    "5200000", "2025-04-24", "2025", "-29.9177", "-51.1836",
    "CPFL Transmissão live-line fleet (presented at Canoas Cidade Industrial ceremony).",
    "jornal_comercio_cpfl_tx_rs_20250424_wayback",
    "Cada um desses veículos teve um custo de cerca de R$ 2,6 milhões",
    JC_WAYBACK,
    "Actor: CPFL Transmissão (State Grid–controlled) — prc. NEW two live-line trucks ~R$5.2m (Wayback JC). Shuffle power_plants_grid; PRC equal-budget.",
    "hunt_cycle288", investment_type="equipment", evidence="proxy", currency="BRL",
    value_usd=str(round(5200000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Klein, Jefferson. “CPFL investirá R$ 3,9 bilhões no sistema gaúcho de transmissão até 2029.” Jornal do Comércio, April 24, 2025. Wayback Machine snapshot. '
    + JC_WAYBACK + f" (live: {JC_LIVE}).",
    annotation="CPFL live-line trucks 2×~R$2.6m via Fed H.10 (Wayback JC; UNVERIFIED press). Supports cpfl_live_line_trucks_52m_brl_2025.",
    evid_note="Opened Wayback JC 24 Apr 2025 snapshot; two live-line trucks ~R$2.6m each confirmed.",
)

# 6. power_plants_grid / other — NEW Equatorial 2T26 Ativos elétricos R$1.933bn
row_doc(
    "equatorial_ativos_eletricos_2t26_1933m_brl",
    "energy", "power_plants_grid", "other",
    "Equatorial — Distribuição Ativos elétricos CapEx 2T26 R$1.933bn",
    "Brazil",
    "12 Aug 2026 Equatorial 2T26 release: Distribuição Ativos elétricos 2T26 R$1.933 billion (vs 2T25 R$2.101bn; −8%). CapEx: enter R$1.933bn face. Nested under Distribuição Total R$2.527bn / consolidated R$2.600bn (not additive).",
    "1933000000", "2026-08-12", "2026", "-15.78", "-47.93",
    "Equatorial distribution companies (Brasília HQ pin).",
    "equatorial_2t26_release_20260812",
    "Ativos elétricos … 1.933",
    EQ_2T26,
    "Actor: Equatorial S.A. — other. NEW 2T26 Ativos elétricos R$1.933bn. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle288", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(1933000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. ' + EQ_2T26 + ".",
    annotation="Equatorial 2T26 Ativos elétricos R$1.933bn via Fed H.10. Supports equatorial_ativos_eletricos_2t26_1933m_brl.",
    evid_note="Opened Equatorial 2T26 PDF; Distribuição Ativos elétricos 2T26 R$1.933bn confirmed.",
)

# 7. power_plants_grid / other — NEW Equatorial 2T26 Obrigações especiais R$460m
row_doc(
    "equatorial_obrigacoes_especiais_2t26_460m_brl",
    "energy", "power_plants_grid", "other",
    "Equatorial — Distribuição Obrigações especiais CapEx 2T26 R$460m",
    "Brazil",
    "12 Aug 2026 Equatorial 2T26 release: Distribuição Obrigações especiais 2T26 R$460 million (vs 2T25 R$430m; +7%), driven by PLPT (Programa Luz para Todos), with Equatorial Piauí +R$24.41m absolute impact. CapEx: enter R$460m face. Nested under Distribuição Total R$2.527bn / consolidated R$2.600bn (not additive).",
    "460000000", "2026-08-12", "2026", "-15.78", "-47.93",
    "Equatorial distribution PLPT / special obligations (Brasília HQ pin).",
    "equatorial_2t26_release_20260812",
    "Obrigações especiais 430 460 7% 31",
    EQ_2T26,
    "Actor: Equatorial S.A. — other. NEW 2T26 Obrigações especiais R$460m. Shuffle power_plants_grid; other equal-budget.",
    "hunt_cycle288", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(460000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Release de Resultados 2T26.” August 12, 2026. ' + EQ_2T26 + ".",
    annotation="Equatorial 2T26 Obrigações especiais R$460m via Fed H.10. Supports equatorial_obrigacoes_especiais_2t26_460m_brl.",
    evid_note="Opened Equatorial 2T26 PDF; Distribuição Obrigações especiais 2T26 R$460m confirmed.",
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
    print(f"cycle288 added {len(added)}: {added}")
    print(f"cycle288 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
