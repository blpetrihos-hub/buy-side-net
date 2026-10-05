#!/usr/bin/env python3
"""Cycle 280 hunt: shuffle_seed=20261280; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered + Random(20261280).shuffle):
port_cranes, port_ownership, copper, solar, fission_smr, lithium, rail,
bridges_roads, graphite, niobium, power_plants_grid, water, balsa, nickel,
other_renewables, building_materials, engineering_epc, wind.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget: CapEx-fill Freeport Cerro Verde OxI package >USD14m
  (AES green nested exhausted; EXIM/USTDA/Progress/Wabtec/Equinix/Seven Seas/ICM
  probes; SSA Guaymas CapEx blank).
PRC equal-budget: CapEx-fill CREC Cañas–Bebedero PRC grant ₡9,815m (host 406 on
  re-open; retain prior evidence quote; currency CRC stored without FX).
Allied: (Neoenergia Networks faces exhausted this pass).
Other: NEW Copel Geração 2T26 R$371.5m + TX 2T26 R$90.8m + Hydro 2T26 R$34.4m +
  Eólica 2T26 R$19.2m; Rumo Norte 6M26 R$2,988m + Expansão Norte 6M26 R$2,207m;
  Equatorial Outros 2T26 R$13m; Aegea Guariroba 6M26 R$87m.
Skipped: thin dry; ENGIE Colibri 403; Ascenty 403; Alupar TECP CapEx figure absent;
  Progress Rail VLI R$430m unsigned; Motiva Minas_SP R$750m is bargain-purchase
  gain not CapEx; Wabtec Vale 50 loco CapEx blank; holdovers unsigned.
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


# 1. bridges_roads / us — CapEx-fill Freeport Cerro Verde OxI >USD14m package
row_doc(
    "fcx_cerro_verde_oxi_uchumayo_2026",
    "infrastructure", "bridges_roads", "us",
    "Freeport-McMoRan / Cerro Verde — Peru Works for Taxes OxI package >USD14m",
    "Peru",
    "24 Jul 2026 Freeport-McMoRan: Cerro Verde completed first two Peru Works for Taxes (Obras por Impuestos) projects investing more than USD 14 million — including a major road infrastructure project in Uchumayo district (resurfacing, drainage, signage, sidewalks, green spaces) plus a National University of San Agustín campus in El Pedregal, Majes. CapEx-fill: enter USD14m floor for OxI package (road+campus; split not disclosed). Nested vs road-only blank prior (not additive).",
    "14000000", "2026-07-24", "2026", "-16.43", "-71.52",
    "Uchumayo district road works / Arequipa region (company geography; Uchumayo pin).",
    "fcx_cerro_verde_oxi_20260724",
    "Cerro Verde has completed its first two projects through Peru's Works for Taxes (Obras por Impuestos, OxI) program, investing more than $14 million",
    "https://fcx.com/freeport-features/07242026",
    "Actor: Freeport-McMoRan / Sociedad Minera Cerro Verde (U.S. majority) — us. CapEx-fill: USD14m OxI package floor. Shuffle bridges_roads; ≥1/3 U.S. hunt.",
    "hunt_cycle280", investment_type="epc", evidence="documented", currency="USD",
    value_usd="14000000", fx_usd="1", bib_type="company",
    chicago='Freeport-McMoRan. “Cerro Verde Completes First Works for Taxes Projects in Arequipa.” July 24, 2026. https://fcx.com/freeport-features/07242026.',
    annotation="Freeport Cerro Verde OxI package CapEx-fill >USD14m. Supports fcx_cerro_verde_oxi_uchumayo_2026.",
    evid_note="Re-opened Freeport Features 24 Jul 2026; OxI package investing more than USD 14 million confirmed for CapEx-fill.",
)

# 2. water / prc — CapEx-fill CREC Cañas–Bebedero PRC grant ₡9,815m
row_doc(
    "crec_canas_bebedero_water_costa_rica_2022",
    "resources", "water", "prc",
    "CREC / PRC grant — Cañas–Bebedero aqueduct ₡9,815m",
    "Costa Rica",
    "24 Mar 2022 Costa Rica Presidency: Cañas–Bebedero aqueduct/potabilization plant delivered — PRC grant ₡9,815 million; AyA equips and operates; serves ~37,000 people. CapEx-fill: enter CRC 9,815,000,000 grant face (USD FX not applied — Fed H.10 CRC not retrieved this cycle). Nested vs prior blank CapEx row.",
    "9815000000", "2022-03-24", "2022", "10.43", "-85.09",
    "Cañas–Bebedero aqueduct / Guanacaste (Cañas pin).",
    "cr_presidencia_canas_bebedero_20220324",
    "El proyecto Cañas-Bebedero tuvo un costo de ₡9.815 millones donados por la República Popular China",
    "https://presidencia.gobiernocarlosalvarado.cr/comunicados/2022/03/canas-recibe-planta-potabilizadora-mas-moderna-del-pais-por-parte-de-aya-y-la-republica-popular-china/",
    "Actor: CREC / PRC grant — prc. CapEx-fill: CRC 9,815m grant face. Shuffle water; PRC equal-budget.",
    "hunt_cycle280", investment_type="grant", evidence="documented", currency="CRC",
    value_usd="", fx_usd="", bib_type="government",
    chicago='Presidencia de la República de Costa Rica. “Cañas recibe planta potabilizadora más moderna del país.” March 24, 2022. https://presidencia.gobiernocarlosalvarado.cr/comunicados/2022/03/canas-recibe-planta-potabilizadora-mas-moderna-del-pais-por-parte-de-aya-y-la-republica-popular-china/.',
    annotation="CREC Cañas–Bebedero PRC grant CapEx-fill ₡9,815m. Supports crec_canas_bebedero_water_costa_rica_2022.",
    evid_note="CapEx-fill from prior-opened CR Presidency quote (host 406 on 2026-10-05 re-open); CRC 9,815m grant face retained.",
)

# 3. power_plants_grid / other — NEW Copel Geração 2T26 R$371.5m
row_doc(
    "copel_geracao_2t26_371p5m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — Geração CapEx 2T26 R$371.5m",
    "Brazil",
    "Copel 2T26 earnings presentation CapEx table: Geração R$371.5 million in 2T26 (within GeT; includes LRCAP R$317.9m + Hydro R$34.4m + Eólica R$19.2m). CapEx: enter R$371.5m Geração 2T26 face. Nested vs copel_get_2t26_476p4m_brl / copel_lrcap_2t26_317p9m_brl (not additive).",
    "371500000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Copel generation assets, Paraná (Curitiba pin).",
    "copel_2t26_investidor10_1s26",
    "Geração 371,5 25,7 1.345,5 430,2 46,2 831,2",
    "https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/",
    "Actor: Copel — other. NEW nested Geração 2T26 CapEx R$371.5m. Shuffle power_plants_grid.",
    "hunt_cycle280", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(371500000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel (Companhia Paranaense de Energia). “Destaques 2T26” CapEx table (RI republication). 2026. https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/.',
    annotation="Copel Geração 2T26 CapEx R$371.5m via Fed H.10. Supports copel_geracao_2t26_371p5m_brl.",
    evid_note="Opened Copel 2T26 CapEx presentation PDF; Geração 2T26 Capex R$371.5m confirmed.",
)

# 4. power_plants_grid / other — NEW Copel Transmissão 2T26 R$90.8m
row_doc(
    "copel_tx_2t26_90p8m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — Transmissão CapEx 2T26 R$90.8m",
    "Brazil",
    "Copel 2T26 earnings presentation CapEx table: Transmissão R$90.8 million in 2T26 (1S26 R$164.2m). CapEx: enter R$90.8m TX 2T26 face. Nested vs copel_get_2t26_476p4m_brl (not additive).",
    "90800000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Copel transmission assets, Paraná (Curitiba pin).",
    "copel_2t26_investidor10_1s26",
    "Transmissão 90,8 64,7 40,3 164,2 113,6 44,5",
    "https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/",
    "Actor: Copel — other. NEW nested Transmissão 2T26 CapEx R$90.8m. Shuffle power_plants_grid.",
    "hunt_cycle280", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(90800000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel (Companhia Paranaense de Energia). “Destaques 2T26” CapEx table (RI republication). 2026. https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/.',
    annotation="Copel TX 2T26 CapEx R$90.8m via Fed H.10. Supports copel_tx_2t26_90p8m_brl.",
    evid_note="Opened Copel 2T26 CapEx presentation PDF; Transmissão 2T26 Capex R$90.8m confirmed.",
)

# 5. power_plants_grid / other — NEW Copel Hidrelétricas 2T26 R$34.4m
row_doc(
    "copel_hydro_2t26_34p4m_brl",
    "energy", "power_plants_grid", "other",
    "Copel — Hidrelétricas CapEx 2T26 R$34.4m",
    "Brazil",
    "Copel 2T26 earnings presentation CapEx table: Hidrelétricas R$34.4 million in 2T26 (1S26 R$77.9m). CapEx: enter R$34.4m hydro 2T26 face. Nested vs copel_geracao_2t26_371p5m_brl / LRCAP (not additive).",
    "34400000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Copel hydro plants, Paraná (Curitiba pin).",
    "copel_2t26_investidor10_1s26",
    "Hidrelétricas 34,4 12,0 186,7 77,9 20,7 276,3",
    "https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/",
    "Actor: Copel — other. NEW nested Hidrelétricas 2T26 CapEx R$34.4m. Shuffle power_plants_grid.",
    "hunt_cycle280", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(34400000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel (Companhia Paranaense de Energia). “Destaques 2T26” CapEx table (RI republication). 2026. https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/.',
    annotation="Copel Hydro 2T26 CapEx R$34.4m via Fed H.10. Supports copel_hydro_2t26_34p4m_brl.",
    evid_note="Opened Copel 2T26 CapEx presentation PDF; Hidrelétricas 2T26 Capex R$34.4m confirmed.",
)

# 6. wind / other — NEW Copel Eólica 2T26 R$19.2m
row_doc(
    "copel_eolica_2t26_19p2m_brl",
    "energy", "wind", "other",
    "Copel — Eólica CapEx 2T26 R$19.2m",
    "Brazil",
    "Copel 2T26 earnings presentation CapEx table: Eólica R$19.2 million in 2T26 (1S26 R$34.4m). CapEx: enter R$19.2m wind 2T26 face. Nested vs copel_geracao_2t26_371p5m_brl (not additive).",
    "19200000", "2026-06-30", "2026", "-25.43", "-49.27",
    "Copel wind assets, Paraná/NE Brazil (Curitiba HQ pin).",
    "copel_2t26_investidor10_1s26",
    "Eólica 19,2 13,6 41,2 34,4 25,5 34,9",
    "https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/",
    "Actor: Copel — other. NEW nested Eólica 2T26 CapEx R$19.2m. Shuffle wind.",
    "hunt_cycle280", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(19200000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Copel (Companhia Paranaense de Energia). “Destaques 2T26” CapEx table (RI republication). 2026. https://investidor10.com.br/acoes/link_comunicado/CPLE3/46836/.',
    annotation="Copel Eólica 2T26 CapEx R$19.2m via Fed H.10. Supports copel_eolica_2t26_19p2m_brl.",
    evid_note="Opened Copel 2T26 CapEx presentation PDF; Eólica 2T26 Capex R$19.2m confirmed.",
)

# 7. rail / other — NEW Rumo Operação Norte 6M26 R$2,988m
row_doc(
    "rumo_norte_6m26_2988m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Operação Norte CapEx 6M26 R$2,988m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Norte R$2,988 million in 6M26 (2T26 R$1,393m already nested). CapEx: enter R$2,988m Norte 6M26 face. Nested vs rumo_norte_2t26_1393m_brl / rumo_6m26_capex_3371m_brl (not additive).",
    "2988000000", "2026-06-30", "2026", "-15.60", "-56.10",
    "Rumo Operação Norte corridor (Rondonópolis / Mato Grosso pin).",
    "rumo_2t26_release_20260812",
    "1.393 1.186 17,5 % Operação Norte 2.988 2.782 7,4 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Operação Norte 6M26 CapEx R$2,988m. Shuffle rail.",
    "hunt_cycle280", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2988000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Norte 6M26 CapEx R$2,988m via Fed H.10. Supports rumo_norte_6m26_2988m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Operação Norte Capex 6M26 R$2,988m confirmed.",
)

# 8. rail / other — NEW Rumo Expansão Norte 6M26 R$2,207m
row_doc(
    "rumo_expansao_norte_6m26_2207m_brl",
    "infrastructure", "rail", "other",
    "Rumo — Expansão Norte CapEx 6M26 R$2,207m",
    "Brazil",
    "12 Aug 2026 Rumo S.A. Relatório de Resultados 2T26: Capex table Operação Norte Expansão R$2,207 million in 6M26 (2T26 R$979m already nested). CapEx: enter R$2,207m Expansão Norte 6M26 face. Nested vs rumo_expansao_norte_2t26_979m_brl / rumo_norte_6m26_2988m_brl (not additive).",
    "2207000000", "2026-06-30", "2026", "-15.60", "-56.10",
    "Rumo Operação Norte expansion works (Rondonópolis / Mato Grosso pin).",
    "rumo_2t26_release_20260812",
    "979 881 11,1 % Expansão 2.207 2.190 0,8 %",
    "https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2",
    "Actor: Rumo S.A. — other. NEW nested Expansão Norte 6M26 CapEx R$2,207m. Shuffle rail.",
    "hunt_cycle280", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(2207000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Rumo S.A. “Relatório de Resultados 2T26.” August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/003f6029-d45a-44ac-9c9e-869fe5df83fc/019d7c48-331a-e6fa-90fc-1a0f01dcccd5?origin=2.',
    annotation="Rumo Expansão Norte 6M26 CapEx R$2,207m via Fed H.10. Supports rumo_expansao_norte_6m26_2207m_brl.",
    evid_note="Opened Rumo 2T26 MZ IQ PDF; Expansão Norte Capex 6M26 R$2,207m confirmed.",
)

# 9. power_plants_grid / other — NEW Equatorial Outros 2T26 R$13m
row_doc(
    "equatorial_outros_2t26_13m_brl",
    "energy", "power_plants_grid", "other",
    "Equatorial — Outros CapEx 2T26 R$13m",
    "Brazil",
    "12 Aug 2026 Equatorial S.A. 2T26 earnings release: CapEx table Outros R$13 million in 2T26 (+110% vs 2T25 R$6m). CapEx: enter R$13m Outros face. Nested vs equatorial_2t26_capex_2p6bn_brl total (not additive).",
    "13000000", "2026-06-30", "2026", "-15.78", "-47.93",
    "Equatorial multi-utility other CapEx (Brasília HQ pin).",
    "equatorial_2t26_release_20260812",
    "Outros 6                      13                    110% 7",
    "https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2",
    "Actor: Equatorial S.A. — other. NEW nested Outros 2T26 CapEx R$13m. Shuffle power_plants_grid.",
    "hunt_cycle280", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(13000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Equatorial S.A. “Resultados 2T26” (company MZ IQ PDF). August 12, 2026. https://api.mziq.com/mzfilemanager/v2/d/62b21cba-838c-49a4-aaef-e0fb2350c169/b1f651f0-9cd8-d2e0-87f0-498cd4b24f8b?origin=2.',
    annotation="Equatorial Outros 2T26 CapEx R$13m via Fed H.10. Supports equatorial_outros_2t26_13m_brl.",
    evid_note="Opened Equatorial 2T26 MZ IQ PDF; Outros Capex 2T26 R$13m confirmed.",
)

# 10. water / other — NEW Aegea Guariroba 6M26 R$87m
row_doc(
    "aegea_guariroba_6m26_87m_brl",
    "resources", "water", "other",
    "Aegea — Guariroba Capex 6M26 R$87m",
    "Brazil",
    "Aegea 2T26/6M26 earnings release: Capex table Guariroba R$87 million in 6M26 (2T26 R$49m already nested). CapEx: enter R$87m Guariroba 6M26 face. Nested vs aegea_guariroba_2t26_49m_brl / ecosystem Capex (not additive).",
    "87000000", "2026-06-30", "2026", "-20.47", "-54.62",
    "Guariroba / Campo Grande MS sanitation concession (Campo Grande pin).",
    "aegea_2t26_6m26_release_mziq",
    "Guariroba 49 41 19,4% 87 77 13,3%",
    "https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2",
    "Actor: Aegea Saneamento — other. NEW nested Guariroba 6M26 Capex R$87m. Shuffle water.",
    "hunt_cycle280", investment_type="corporate_capex", evidence="documented", currency="BRL",
    value_usd=str(round(87000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="company",
    chicago='Aegea Saneamento. “Resultados 2T26 / 6M26” (company MZ IQ PDF). https://api.mziq.com/mzfilemanager/v2/d/9aa4d8c5-604a-4097-acc9-2d8be8f71593/059c8a63-d6dc-b073-bb33-76e316044799?origin=2.',
    annotation="Aegea Guariroba 6M26 Capex R$87m via Fed H.10. Supports aegea_guariroba_6m26_87m_brl.",
    evid_note="Opened Aegea 2T26/6M26 MZ IQ PDF; Guariroba Capex 6M26 R$87m confirmed.",
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
    print(f"cycle280 added {len(added)}: {added}")
    print(f"cycle280 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
