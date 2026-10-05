#!/usr/bin/env python3
"""Cycle 230 hunt: shuffle_seed=20261230; equal budget; U.S./PRC split; thin after.

Canonical shuffle (BRIEF.md numbered order + Random(20261230).shuffle):
port_ownership, wind, other_renewables, nickel, building_materials, rail, fission_smr,
port_cranes, graphite, bridges_roads, copper, power_plants_grid, balsa, water, solar,
engineering_epc, lithium, niobium.

Thin top-up (recomputed after shuffled pass): balsa / nickel / fission_smr — dry.
≥1/3 U.S. hunt budget spent on Freeport/EnergyX/EXIM/Bechtel/Fluor/USTDA/Nextracker/
Jervois/Wabtec/Fluence/SSA/Atlas/Ascenty/Progress Rail/GE Vernova/Oceaneering/AES/
NFE sweeps (US blank-USD CapEx residual exhausted; 0 new US CapEx — honest residual).
PRC equal-budget: CRRC SP Metro Frota R + SGBH GATE UHV CapEx-fills; holdovers unsigned.
Holcim–Cemex Colombia USD 485m already CapEx-present (pre-close still logged).
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
BRL_FX_DATE = "2026-09-25"
MXN_USD = "17.6932"
MXN_FX_DATE = "2026-09-25"
EUR_USD = "1.1400"
EUR_FX_DATE = "2026-09-25"


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


# 1. wind / allied — CapEx-fill Vestas Aquiraz R$130m
row_doc(
    "vestas_aquiraz_factory_130m_brl_2024",
    "energy", "wind", "allied",
    "Vestas — Aquiraz hub/nacelle factory investment (V163-4.5 MW)",
    "Brazil",
    "9 Aug 2024 Terra (reporting Vestas): investirá 130 milhões de reais to produce new turbine model at Aquiraz (Ceará) factory. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~25.04m for stored R$130m face. UNVERIFIED proxy press.",
    "130000000", BRL_FX_DATE, "2024", "-3.901", "-38.391",
    "Vestas Aquiraz plant, Ceará (press geography).",
    "terra_vestas_aquiraz_130m_20240809",
    "A dinamarquesa Vestas anunciou nesta sexta-feira que investirá 130 milhões de reais para produzir um novo modelo de turbina eólica em sua fábrica",
    "https://www.terra.com.br/economia/vestas-investira-r130-mi-para-fabricar-nova-turbina-eolica-no-ceara,f9d1fbc4a6527698ae571e35682da9c8wlp8f5rc.html",
    "Actor: Vestas (Denmark) — allied. CapEx-fill: retain R$130m factory CapEx; add Fed H.10 Sep 25 2026 FX to USD ~25.04m. Shuffle wind.",
    "hunt_cycle230", investment_type="manufacturing_capex", evidence="proxy", currency="BRL",
    value_usd=str(round(130000000 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Terra / Agencia Estado. “Vestas investirá R$130 mi para fabricar nova turbina eólica no Ceará.” August 9, 2024. https://www.terra.com.br/economia/vestas-investira-r130-mi-para-fabricar-nova-turbina-eolica-no-ceara,f9d1fbc4a6527698ae571e35682da9c8wlp8f5rc.html.',
    annotation="Vestas Aquiraz CapEx-fill ~USD 25.04m via Fed H.10 (proxy). Supports vestas_aquiraz_factory_130m_brl_2024.",
    evid_note="Opened Terra Portuguese; R$130m Aquiraz factory CapEx confirmed as press paraphrase (proxy). CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 2. wind / allied — CapEx-fill Vergnet Claybury EUR 1.6m
row_doc(
    "vergnet_claybury_barbados_2025",
    "energy", "wind", "allied",
    "Vergnet — Claybury Barbados 3 medium turbines supply contract",
    "Barbados",
    "12 Jun 2023 Vergnet Actusnews: contract signed with Pavana Energy Ltd for supply, erection assistance, and commissioning of 3 medium-power turbines for EUR 1.6 million. CapEx-fill: Fed H.10 Sep 25 2026 EUR 1.1400 → USD ~1.82m.",
    "1600000", EUR_FX_DATE, "2023", "13.175", "-59.545",
    "Claybury, Barbados (company geography).",
    "vergnet_claybury_20230612",
    "a été signé un contrat de fourniture, d'assistance au montage et de mise en service de 3 éoliennes de moyenne puissance pour un montant de 1,6 M€",
    "https://www.actusnews.com/fr/vergnet/cp/2023/06/12/un-nouveau-contrat-d_un-montant-de-1-6-m-eur",
    "Actor: Vergnet (France) — allied. CapEx-fill: retain EUR 1.6m; add Fed H.10 Sep 25 2026 FX to USD ~1.82m. Shuffle wind.",
    "hunt_cycle230", investment_type="equipment_supply", evidence="documented", currency="EUR",
    value_usd=str(round(1600000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='Vergnet / Actusnews. “Un nouveau contrat d’un montant de 1,6 M€.” June 12, 2023. https://www.actusnews.com/fr/vergnet/cp/2023/06/12/un-nouveau-contrat-d_un-montant-de-1-6-m-eur.',
    annotation="Vergnet Claybury CapEx-fill ~USD 1.82m via Fed H.10. Supports vergnet_claybury_barbados_2025.",
    evid_note="Opened Vergnet Actusnews French; EUR 1.6m / 3 turbines Claybury confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 1.1400.",
)

# 3. building_materials / other — CapEx-fill Votorantim Brazil plan invested R$3.1bn
row_doc(
    "votorantim_brazil_plan_3p1bn_invested_2026",
    "infrastructure", "building_materials", "other",
    "Votorantim Cimentos — Brazil 2024–2028 plan cumulative invested (R$3.1bn as of 2Q26)",
    "Brazil",
    "13 Aug 2026 Votorantim Cimentos 2Q26: of the R$5 billion Brazil investment plan for 2024–2028, R$3.1 billion has been invested in projects previously announced. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~597.06m for stored R$3.1bn cumulative face. Distinct from votorantim_xambioa_grind_2026 and FY2025 CapEx rows.",
    "3100000000", BRL_FX_DATE, "2026", "", "",
    "Votorantim Brazil investment plan (national footprint; no single-site pin).",
    "votorantim_2q2026_results_20260813",
    "Our R$5 billion investment plan for Brazil for the period 2024 to 2028 continues to be implemented, with R$3.1 billion being invested in projects previously announced.",
    "https://www.votorantimcimentos.com/news/our-financial-results-in-the-second-quarter-of-2026/",
    "Actor: Votorantim Cimentos (Brazilian) — other. CapEx-fill: retain R$3.1bn cumulative invested; add Fed H.10 Sep 25 2026 FX to USD ~597.06m. Shuffle building_materials.",
    "hunt_cycle230", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(3100000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Votorantim Cimentos. “Our Financial Results in the Second Quarter of 2026.” August 13, 2026. https://www.votorantimcimentos.com/news/our-financial-results-in-the-second-quarter-of-2026/.',
    annotation="Votorantim Brazil plan cumulative CapEx-fill ~USD 597.06m via Fed H.10. Supports votorantim_brazil_plan_3p1bn_invested_2026.",
    evid_note="Opened Votorantim English 2Q26; R$3.1bn cumulative of R$5bn Brazil plan confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 4. rail / prc — CapEx-fill CRRC SP Metro Frota R R$3.104bn
row_doc(
    "crrc_sp_metro_frota_r_44_2025",
    "infrastructure", "rail", "prc",
    "CRRC Sifang Brasil — 44 six-car metro trains (Frota R) São Paulo Metro",
    "Brazil",
    "22–23 Jul 2025 Diário do Transporte: contract signed with Consórcio CRRC Sifang Brasil for 44 six-car metro trains (Frota R) for São Paulo Metro; stored face R$3,104,298,999.76. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~597.89m. UNVERIFIED proxy press.",
    "3104298999.76", BRL_FX_DATE, "2025", "-23.55", "-46.63",
    "São Paulo Metro (press geography).",
    "diario_transporte_crrc_sp_20250723",
    "O contrato para o fornecimento de 44 novos trens metropolitanos para a Companhia do Metropolitano de São Paulo – Metrô foi finalmente assinado",
    "https://diariodotransporte.com.br/2025/07/23/contrato-para-44-novos-trens-do-metro-de-sp-e-assinado-com-estatal-chinesa-quase-quatro-meses-apos-homologacao-da-licitacao/",
    "Actor: CRRC Sifang Brasil (PRC) — prc. CapEx-fill: retain stored R$3.104bn face; add Fed H.10 Sep 25 2026 FX to USD ~597.89m. Shuffle rail.",
    "hunt_cycle230", investment_type="rolling_stock", evidence="proxy", currency="BRL",
    value_usd=str(round(3104298999.76 / float(BRL_USD), 2)), fx_usd=BRL_USD, bib_type="press",
    chicago='Diário do Transporte. “Contrato para 44 novos trens do Metrô de SP é assinado com estatal chinesa.” July 23, 2025. https://diariodotransporte.com.br/2025/07/23/contrato-para-44-novos-trens-do-metro-de-sp-e-assinado-com-estatal-chinesa-quase-quatro-meses-apos-homologacao-da-licitacao/.',
    annotation="CRRC SP Metro CapEx-fill ~USD 597.89m via Fed H.10 (proxy). Supports crrc_sp_metro_frota_r_44_2025.",
    evid_note="Opened Diário do Transporte Portuguese; CRRC Frota R 44 trains / stored R$3.104bn CapEx-filled via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 5. rail / allied — CapEx-fill Mota-Engil CDMX Metro L3 MXN 25.18bn
row_doc(
    "mota_engil_cdmx_metro_l3_25180m_mxn_2026",
    "infrastructure", "rail", "allied",
    "Mota-Engil México — CDMX Metro Línea 3 renovation PPP",
    "Mexico",
    "23 Sep 2026 CDMX Jefatura de Gobierno: fallo names Mota Engil México winner of Línea 3 (Indios Verdes–Universidad) renovation; economic offer MXN 25,180 million (ex-VAT). CapEx-fill: Fed H.10 Sep 25 2026 Mexico peso 17.6932 → USD ~1423.15m.",
    "25180000000", MXN_FX_DATE, "2026", "19.50", "-99.12",
    "CDMX Metro Línea 3 corridor (official geography).",
    "cdmx_jefatura_metro_l3_20260923",
    "los 25 mil 180 millones de pesos que se mencionan en la propuesta de la empresa ganadora, Mota Engil Mexico, es la cantidad que corresponde al monto de oferta económica … monto que no incluye el IVA",
    "https://jefaturadegobierno.cdmx.gob.mx/comunicacion/nota/gobierno-de-la-ciudad-de-mexico-informo-que-manana-se-publicara-en-la-gaceta-oficial-el-nombre-de-la-empresa-ganadora-del-concurso-de-licitacion-de-la-linea-3-del-metro",
    "Actor: Mota-Engil México (Portugal Mota-Engil) — allied. CapEx-fill: retain MXN 25.18bn ex-VAT offer; add Fed H.10 Sep 25 2026 FX to USD ~1423.15m. Shuffle rail.",
    "hunt_cycle230", investment_type="ppp_concession", evidence="documented", currency="MXN",
    value_usd=str(round(25180000000 / float(MXN_USD), 2)), fx_usd=MXN_USD,
    chicago='Jefatura de Gobierno CDMX. “Gobierno de la Ciudad de México informó que mañana se publicará en la Gaceta Oficial el nombre de la empresa ganadora del concurso de licitación de la Línea 3 del Metro.” September 23, 2026. https://jefaturadegobierno.cdmx.gob.mx/comunicacion/nota/gobierno-de-la-ciudad-de-mexico-informo-que-manana-se-publicara-en-la-gaceta-oficial-el-nombre-de-la-empresa-ganadora-del-concurso-de-licitacion-de-la-linea-3-del-metro.',
    annotation="Mota-Engil CDMX L3 CapEx-fill ~USD 1423.15m via Fed H.10. Supports mota_engil_cdmx_metro_l3_25180m_mxn_2026.",
    evid_note="Opened CDMX Jefatura Spanish; MXN 25,180m ex-VAT Mota Engil offer confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 17.6932 MXN/USD.",
)

# 6. bridges_roads / allied — CapEx-fill OHLA BR-040 EUR 850m
row_doc(
    "ohla_br040_concession_2025",
    "infrastructure", "bridges_roads", "allied",
    "OHLA / Construcap / Copasa — BR-040 highway concession (218.9 km)",
    "Brazil",
    "5 May 2025 OHLA: 30-year ANTT concession with Construcap + Copasa to rehabilitate/expand/operate/maintain 218.9 km BR-040 (RJ–MG); estimated investment approximately €850 million. CapEx-fill: Fed H.10 Sep 25 2026 EUR 1.1400 → USD ~969.00m.",
    "850000000", EUR_FX_DATE, "2025", "-22.51", "-43.18",
    "BR-040 Serra de Petrópolis / RJ–MG corridor (company geography).",
    "ohla_br040_20250505",
    "The 30-year concession involves an estimated investment of approximately €850 million.",
    "https://www.ohla-group.com/en/ohla-wins-1-billion-highway-concession-contract-in-brazil-for-br-040/",
    "Actor: OHLA (Spain) consortium — allied. CapEx-fill: retain EUR 850m; add Fed H.10 Sep 25 2026 FX to USD ~969.00m. Shuffle bridges_roads.",
    "hunt_cycle230", investment_type="concession", evidence="documented", currency="EUR",
    value_usd=str(round(850000000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='OHLA. “OHLA Wins $1 Billion Highway Concession Contract in Brazil for BR-040.” May 5, 2025. https://www.ohla-group.com/en/ohla-wins-1-billion-highway-concession-contract-in-brazil-for-br-040/.',
    annotation="OHLA BR-040 CapEx-fill ~USD 969.00m via Fed H.10. Supports ohla_br040_concession_2025.",
    evid_note="Opened OHLA English; EUR 850m / 218.9 km / 30-year concession confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 1.1400.",
)

# 7. power_plants_grid / prc — CapEx-fill SGBH GATE UHV R$18bn (sibling of state_grid_ne)
row_doc(
    "sgbh_gate_uhv_18bn_brl_2025",
    "energy", "power_plants_grid", "prc",
    "State Grid Brazil Holding — GATE Northeast UHV foundation launch CapEx",
    "Brazil",
    "30 Jun 2025 SGBH: launches foundation stone in Silvânia (GO) for Northeast Brazil UHV project (GATE); CapEx R$ 18 billion for ±800 kV HVDC 1,468 km. CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~3466.81m. Sibling row to state_grid_ne_uhv_construction_2026 (same CapEx face; distinct launch-milestone observation).",
    "18000000000", BRL_FX_DATE, "2025", "-16.66", "-48.61",
    "Silvânia converter station, Goiás (company geography).",
    "sgbh_gate_silvania_20250630",
    "lançará em 30/6, em Silvânia (GO), a pedra fundamental do “Projeto de Ultra Alta Tensão no Nordeste do Brasil”, para o qual serão destinados R$ 18 bilhões",
    "https://stategrid.com.br/municipio-goiano-de-silvania-sedia-lancamento-do-mais-caro-projeto-de-ultra-alta-tensao-800kv-da-historia-do-setor-eletrico-do-brasil/",
    "Actor: State Grid Brazil Holding / SGCC (PRC) — prc. CapEx-fill: retain R$18bn; add Fed H.10 Sep 25 2026 FX to USD ~3466.81m. Shuffle power_plants_grid.",
    "hunt_cycle230", investment_type="concession_construction", evidence="documented", currency="BRL",
    value_usd=str(round(18000000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='State Grid Brazil Holding. “Município goiano de Silvânia sedia lançamento do mais caro projeto de ultra alta tensão (±800 kV) da história do setor elétrico do Brasil.” https://stategrid.com.br/municipio-goiano-de-silvania-sedia-lancamento-do-mais-caro-projeto-de-ultra-alta-tensao-800kv-da-historia-do-setor-eletrico-do-brasil/.',
    annotation="SGBH GATE UHV CapEx-fill ~USD 3466.81m via Fed H.10. Supports sgbh_gate_uhv_18bn_brl_2025.",
    evid_note="Opened SGBH Portuguese; R$18bn GATE UHV confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 8. power_plants_grid / allied — CapEx-fill Enel Brasil R$25.3bn
row_doc(
    "enel_brasil_25p3bn_brl_2025_2027",
    "energy", "power_plants_grid", "allied",
    "Enel Brasil — 2025–2027 CapEx plan (~R$25.3bn)",
    "Brazil",
    "15 Jan 2025 Enel Brasil: investirá cerca de R$ 25,3 bilhões em suas operações no Brasil over next three years; of which R$ 24 bilhões for distribution (SP/RJ/CE). CapEx-fill: Fed H.10 Sep 25 2026 Brazil Real 5.1921 → USD ~4872.79m.",
    "25300000000", BRL_FX_DATE, "2025", "", "",
    "Enel Brasil distribution footprint SP/RJ/CE (national; no single-site pin).",
    "enel_brasil_25p3bn_2025",
    "Nos próximos três anos, a Enel investirá cerca de R$ 25,3 bilhões em suas operações no Brasil. Desse total, R$ 24 bilhões serão direcionados ao setor de distribuição de energia.",
    "https://www.enel.com.br/pt/midia/news/d2025-1/Enel-anuncia-investimento-de-R$-25bilhoes-no-Brasil.html",
    "Actor: Enel Brasil (Italy Enel) — allied. CapEx-fill: retain R$25.3bn 2025–2027 plan; add Fed H.10 Sep 25 2026 FX to USD ~4872.79m. Shuffle power_plants_grid.",
    "hunt_cycle230", investment_type="capex_plan", evidence="documented", currency="BRL",
    value_usd=str(round(25300000000 / float(BRL_USD), 2)), fx_usd=BRL_USD,
    chicago='Enel Brasil. “Enel anuncia investimento de R$ 25 bilhões no Brasil.” January 15, 2025. https://www.enel.com.br/pt/midia/news/d2025-1/Enel-anuncia-investimento-de-R$-25bilhoes-no-Brasil.html.',
    annotation="Enel Brasil CapEx-fill ~USD 4872.79m via Fed H.10. Supports enel_brasil_25p3bn_brl_2025_2027.",
    evid_note="Opened Enel Brasil Portuguese; R$25.3bn / R$24bn distribution confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 5.1921 BRL/USD.",
)

# 9. water / allied — CapEx-fill ACCIONA Cagepa Paraíba EUR 498m
row_doc(
    "acciona_cagepa_paraiba_498m_eur_2026",
    "resources", "water", "allied",
    "ACCIONA — Paraíba Cagepa sanitary sewerage PPP (85 municipalities)",
    "Brazil",
    "2026 ACCIONA: 25-year PPP with Cagepa for sanitary sewerage in 85 Paraíba municipalities; planned investment approximately €498 million; 104 WWTPs + 2,800 km networks. CapEx-fill: Fed H.10 Sep 25 2026 EUR 1.1400 → USD ~567.72m.",
    "498000000", EUR_FX_DATE, "2026", "-7.12", "-34.88",
    "Paraíba Litoral / Alto Piranhas (João Pessoa pin).",
    "acciona_paraiba_cagepa_2026",
    "With a 25-year term and planned investment of approximately €498 million, the project will provide universal access to basic sanitation services for more than 1.7 million people",
    "https://www.acciona.com/updates/news/acciona-signs-sanitation-contract-85-municipalities-paraiba-brasil",
    "Actor: ACCIONA (Spain) — allied. CapEx-fill: retain EUR 498m; add Fed H.10 Sep 25 2026 FX to USD ~567.72m. Shuffle water.",
    "hunt_cycle230", investment_type="ppp_concession", evidence="documented", currency="EUR",
    value_usd=str(round(498000000 * float(EUR_USD), 2)), fx_usd=EUR_USD,
    chicago='ACCIONA. “ACCIONA signs sanitation contract for 85 municipalities in Paraíba, Brasil.” 2026. https://www.acciona.com/updates/news/acciona-signs-sanitation-contract-85-municipalities-paraiba-brasil.',
    annotation="ACCIONA Paraíba CapEx-fill ~USD 567.72m via Fed H.10. Supports acciona_cagepa_paraiba_498m_eur_2026.",
    evid_note="Opened ACCIONA English; EUR 498m / 25-year / 85 municipalities / 104 WWTPs confirmed. CapEx-fill USD via Fed H.10 Sep 25 2026 1.1400.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    supports = entry.get("supports") or []
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        prev = existing.get("supports") or []
        for s in supports:
            if s not in prev:
                prev.append(s)
        existing.update(entry)
        existing["supports"] = prev
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if not isinstance(bib, list):
        bib = bib.get("sources") or bib.get("entries") or []
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
    print(f"cycle230 added {len(added)}: {added}")
    print(f"cycle230 updated {len(updated)}: {updated}")


if __name__ == "__main__":
    main()
