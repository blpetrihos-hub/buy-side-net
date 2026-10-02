#!/usr/bin/env python3
"""Cycle 60 hunt: shuffle_seed=20261060; equal budget; U.S. ≥1/3; thin after.

Order: port_cranes, port_ownership, solar, wind, lithium, balsa, water,
bridges_roads, rail, niobium, nickel, copper, other_renewables, fission_smr,
power_plants_grid, engineering_epc, building_materials, graphite.
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


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


# ---------------------------------------------------------------------------
# 1 infrastructure/port_cranes — Liebherr LHM 600 Compas Cartagena (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "liebherr_compas_cartagena_lhm600_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Liebherr — LHM 600 mobile harbour crane for Compas Cartagena",
        "country": "Colombia",
        "asset": "June 2026: Compas places Liebherr LHM 600 into service at Cartagena multipurpose terminal — Colombia’s largest MHC (104 t SWL; 61 m outreach); supports container ops at terminal handling up to 250,000 TEU/y across four berths. Manufactured Liebherr-Rostock; mobile undercarriage for berth reassignment. Distinct from konecranes_cartagena_rtg_2025.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "10.391",
        "lon": "-75.514",
        "geo_note": "Compas Cartagena multipurpose terminal, Port of Cartagena (Caribbean gateway; approximate pin).",
        "evidence": "documented",
        "source_id": "liebherr_compas_lhm600_20260612",
        "note": "Actor: Liebherr-Rostock GmbH (Germany) — allied. Company English press 12 Jun 2026. CapEx USD not disclosed.",
    },
    {
        "id": "liebherr_compas_cartagena_lhm600_2026",
        "retrieved": "2026-10-01",
        "source_id": "liebherr_compas_lhm600_20260612",
        "url": "https://www.liebherr.com/en-int/n/lhm-600-supports-evolving-vessel-demands-at-cartagena-terminal-266688-3935641",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "With a lifting capacity of 104 tonnes and a maximum outreach of 61 metres, the Liebherr LHM 600 is now the largest mobile harbour crane operating in Colombia … Compas has placed an LHM 600 into service at its Cartagena terminal … supporting container operations at a terminal handling up to 250,000 TEUs annually across four berthing positions",
        "note": "Opened Liebherr English press release for Compas Cartagena LHM 600.",
    },
    {
        "id": "liebherr_compas_lhm600_20260612",
        "type": "company",
        "chicago": "Liebherr. “LHM 600 Supports Evolving Vessel Demands at Cartagena Terminal.” Press release, 12 June 2026.",
        "url": "https://www.liebherr.com/en-int/n/lhm-600-supports-evolving-vessel-demands-at-cartagena-terminal-266688-3935641",
        "annotation": "Liebherr LHM 600 MHC commissioning at Compas Cartagena. Supports liebherr_compas_cartagena_lhm600_2026.",
        "supports": ["liebherr_compas_cartagena_lhm600_2026", "hunt_infra_port_cranes"],
    },
)

# ---------------------------------------------------------------------------
# 3 energy/solar — POWERCHINA Huayra 96.9 MW Peru COD (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "powerchina_huayra_peru_96p9mw_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "POWERCHINA / Sinohydro Bureau 11 — Huayra 96.9 MW PV (Marcona, Ica)",
        "country": "Peru",
        "asset": "19 Sep 2026: POWERCHINA Huayra 96.9 MW PV project reaches full-capacity commercial generation in Marcona District, Nazca Province, Ica — company’s first new-energy project in Peru. ~136,000 modules; 2,345 single-axis trackers; seven 33 kV collector lines; one 220 kV step-up station and outgoing line. Expected ~250 GWh/y. Distinct from powerchina_francisco_juana_colombia_2026.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-15.36",
        "lon": "-75.16",
        "geo_note": "Huayra PV / Marcona District, Nazca Province, Ica Region (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "powerchina_huayra_cod_20260928",
        "note": "Actor: POWERCHINA / Sinohydro Bureau 11 (PRC) — prc. Company Chinese release 28 Sep 2026. CapEx USD not disclosed on opened page.",
    },
    {
        "id": "powerchina_huayra_peru_96p9mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "powerchina_huayra_cod_20260928",
        "url": "https://www.powerchina.cn/zxzx/jcdt/art/2026/art_506856551c1e41c597e678e44b83285e.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "当地时间9月19日，秘鲁瓦伊拉96.9兆瓦光伏项目实现全容量投产发电，标志着中国电建在秘鲁首个新能源项目顺利建成投产。该项目位于秘鲁伊卡大区纳斯卡省马尔科纳区，总装机容量 96.9兆瓦，共安装13.6万块光伏组件、2345套平单轴跟踪支架",
        "note": "Opened POWERCHINA Chinese company news on Huayra full-capacity COD.",
    },
    {
        "id": "powerchina_huayra_cod_20260928",
        "type": "company",
        "chicago": "Power Construction Corporation of China. “秘鲁瓦伊拉96.9兆瓦光伏项目全容量投产发电.” Company news, 28 September 2026.",
        "url": "https://www.powerchina.cn/zxzx/jcdt/art/2026/art_506856551c1e41c597e678e44b83285e.html",
        "annotation": "POWERCHINA Huayra 96.9 MW Peru PV full-capacity COD. Supports powerchina_huayra_peru_96p9mw_2026.",
        "supports": ["powerchina_huayra_peru_96p9mw_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 4 energy/wind — Vestas Argentina 217 MW turbine orders (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "vestas_argentina_217mw_2025",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Vestas — two Argentina wind turbine orders totaling 217 MW",
        "country": "Argentina",
        "asset": "12 Sep 2025: Vestas Latin America announces two Q3 Argentina orders totaling 217 MW — (1) 186 MW V162-6.4 MW with 25-year AOM5000; delivery/commissioning planned 2026; (2) 31 MW V162-6.2 MW with 25-year AOM5000; delivery 2026 / commissioning 2027. Customers/project names undisclosed on Vestas page. Distinct from ifc_pcr_olavarria_wind_2026 (IFC financing row for named Olavarría project).",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "Argentina national; Vestas release leaves customer/project names undisclosed — no site pin.",
        "evidence": "documented",
        "source_id": "vestas_argentina_217mw_20250912",
        "note": "Actor: Vestas Wind Systems (Denmark) — allied. Company order intake release. CapEx USD not disclosed. Equipment-supply angle distinct from IFC financing for Olavarría.",
    },
    {
        "id": "vestas_argentina_217mw_2025",
        "retrieved": "2026-10-01",
        "source_id": "vestas_argentina_217mw_20250912",
        "url": "https://www.vestas.com/en/media/company-news/2025/vestas-announces-two-orders-in-argentina-for-a-total-of-c4233692",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Vestas is proud to announce the following orders as part of our Q3 order intake: Argentina … 186 … V162 6.4 MW … Delivery and commissioning are planned for 2026; Argentina … 31 … V162 6.2 MW … Delivery is planned for 2026 and commissioning for 2027",
        "note": "Opened Vestas company news 12 Sep 2025 for Argentina 217 MW orders.",
    },
    {
        "id": "vestas_argentina_217mw_20250912",
        "type": "company",
        "chicago": "Vestas. “Vestas Announces Two Orders in Argentina for a Total of 217 MW.” Company news, 12 September 2025.",
        "url": "https://www.vestas.com/en/media/company-news/2025/vestas-announces-two-orders-in-argentina-for-a-total-of-c4233692",
        "annotation": "Vestas Q3 Argentina turbine orders totaling 217 MW. Supports vestas_argentina_217mw_2025.",
        "supports": ["vestas_argentina_217mw_2025", "hunt_energy_wind"],
    },
)

# ---------------------------------------------------------------------------
# 7 resources/water — Cagece Fortaleza Dessal construction authorization (other)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cagece_dessal_fortaleza_auth_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "other",
        "counterpart": "Cagece / Consórcio Águas de Fortaleza — Dessal Fortaleza seawater desalination PPP",
        "country": "Brazil",
        "asset": "16–17 Jul 2026: Cagece authorizes start of works on Planta de Dessalinização de Fortaleza (Dessal) at Praia do Futuro — largest seawater desal for human supply in Brazil. PPP with Consórcio Águas de Fortaleza (Marquise / PB Construções / Abengoa Água); 30-year build-operate; >R$3.1bn investment; 1,000 lps (~720k people; ~12% RMF demand); reverse osmosis; COD targeted H2 2028 (~24-month build). Distinct from nadbank_baja_rosarito_distrib_82m_2026.",
        "investment_type": "epc",
        "value": "3100000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-3.745",
        "lon": "-38.447",
        "geo_note": "Praia do Futuro desalination plant area, Fortaleza, Ceará (AESBE/Cagece geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "aesbe_cagece_dessal_20260717",
        "note": "Actor: Cagece (Ceará state utility) + PPP consortium — other. AESBE association release. R$3.1bn figure from AESBE page (press/association — UNVERIFIED proxy for USD conversion; leave value_usd blank). Abengoa Água is Spanish consortium member but authorizing utility is Brazilian state.",
    },
    {
        "id": "cagece_dessal_fortaleza_auth_2026",
        "retrieved": "2026-10-01",
        "source_id": "aesbe_cagece_dessal_20260717",
        "url": "https://aesbe.org.br/cagece-autoriza-inicio-das-obras-da-planta-de-dessalinizacao-de-fortaleza-marco-para-a-seguranca-hidrica-do-brasil/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Com investimento superior a R$ 3,1 bilhões, o empreendimento será o maior projeto de dessalinização de água do mar para consumo humano já implantado no país … A obra será executada pelo Consórcio Águas de Fortaleza, por meio de uma Parceria Público-Privada (PPP) com a Cagece … capacidade para produzir 1 metro cúbico de água por segundo (1.000 litros por segundo)",
        "note": "Opened AESBE Portuguese notice on Cagece Dessal Fortaleza works authorization.",
    },
    {
        "id": "aesbe_cagece_dessal_20260717",
        "type": "trade_association",
        "chicago": "Associação Brasileira das Empresas Estaduais de Saneamento (AESBE). “Cagece Autoriza Início das Obras da Planta de Dessalinização de Fortaleza.” 17 July 2026.",
        "url": "https://aesbe.org.br/cagece-autoriza-inicio-das-obras-da-planta-de-dessalinizacao-de-fortaleza-marco-para-a-seguranca-hidrica-do-brasil/",
        "annotation": "AESBE/Cagece authorization for Fortaleza seawater desal PPP (>R$3.1bn). Supports cagece_dessal_fortaleza_auth_2026.",
        "supports": ["cagece_dessal_fortaleza_auth_2026", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 9 infrastructure/rail — EXIM Wabtec GMXT locomotives ~USD 185m (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "exim_wabtec_gmxt_185m_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "us",
        "counterpart": "U.S. EXIM / Wabtec — Grupo México Transportes locomotive modernization financing",
        "country": "Mexico",
        "asset": "18 Sep 2025: EXIM Board approves nearly USD 185 million financing supporting export of Wabtec Corporation modernized locomotives to Grupo México Transportes (GMXT) fleet renewal; EXIM cites ~600 U.S. manufacturing jobs in Pennsylvania and Texas. Part of ~USD 285m dual-approval day with Bahamas LNG. Distinct from wabtec_mrs_254m_2026 (Brazil MRS).",
        "investment_type": "financing",
        "value": "185000000",
        "currency": "USD",
        "value_usd": "185000000",
        "fx_usd": "1",
        "fx_date": "2025-09-18",
        "year": "2025",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "Mexico national GMXT fleet renewal — no single depot named on EXIM release; leave lat/lon empty.",
        "evidence": "documented",
        "source_id": "exim_gmxt_wabtec_20250918",
        "note": "Actor: U.S. EXIM financing Wabtec (U.S.) exports — us. Official EXIM Board release. Amount cited as nearly USD 185 million.",
    },
    {
        "id": "exim_wabtec_gmxt_185m_2025",
        "retrieved": "2026-10-01",
        "source_id": "exim_gmxt_wabtec_20250918",
        "url": "https://www.exim.gov/news/export-import-bank-united-states-board-directors-approves-infrastructure-investments-totaling",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The first of the two approvals today supports the export of Wabtec Corporation modernized locomotives to Grupo Mexico Transportes (GMXT). The nearly $185 million in financing will support GMXT’s fleet renewal program and support 600 good-paying, skilled manufacturing jobs in Pennsylvania and Texas.",
        "note": "Opened EXIM Board approval release 18 Sep 2025.",
    },
    {
        "id": "exim_gmxt_wabtec_20250918",
        "type": "government",
        "chicago": "Export-Import Bank of the United States. “Export-Import Bank of the United States Board of Directors Approves Infrastructure Investments Totaling Nearly $285 Million.” Press release, 18 September 2025.",
        "url": "https://www.exim.gov/news/export-import-bank-united-states-board-directors-approves-infrastructure-investments-totaling",
        "annotation": "EXIM ~USD 185m Wabtec locomotive financing for GMXT Mexico. Supports exim_wabtec_gmxt_185m_2025.",
        "supports": ["exim_wabtec_gmxt_185m_2025", "hunt_latam_rail_telecom"],
    },
)

# ---------------------------------------------------------------------------
# 12 resources/copper — CMOC/Odin Los Cangrejos exploitation contract (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cmoc_cangrejos_ecuador_1p7bn_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "prc",
        "counterpart": "CMOC / ODIN Mining del Ecuador — Los Cangrejos gold-copper exploitation contract",
        "country": "Ecuador",
        "asset": "27 Apr 2026: Ecuador Ministry of Environment and Energy announces exploitation-contract signing for Los Cangrejos (El Oro; Santa Rosa / Atahualpa) with ODIN Mining del Ecuador S.A. (CMOC Group subsidiary). Ministry cites investment >USD 1.7bn; state 50% project-value share; advance royalties USD 54m staged. Gold-copper deposit (Cu byproduct coded under copper scarce-minerals layer). Distinct from mmg_las_bambas / chinalco_toromocho.",
        "investment_type": "ownership_equity",
        "value": "1700000000",
        "currency": "USD",
        "value_usd": "1700000000",
        "fx_usd": "1",
        "fx_date": "2026-04-27",
        "year": "2026",
        "status": "active",
        "lat": "-3.45",
        "lon": "-79.85",
        "geo_note": "Los Cangrejos project area, El Oro Province (Santa Rosa / Atahualpa; ministry geography; approximate pin).",
        "evidence": "documented",
        "source_id": "mae_ecuador_cangrejos_20260427",
        "note": "Actor: ODIN Mining / CMOC Group (PRC) — prc. Official MAE boletin. Investment floor >USD 1.7bn from ministry; gold-primary with copper byproduct — coded copper per scarce-minerals taxonomy.",
    },
    {
        "id": "cmoc_cangrejos_ecuador_1p7bn_2026",
        "retrieved": "2026-10-01",
        "source_id": "mae_ecuador_cangrejos_20260427",
        "url": "https://www.ambienteyenergia.gob.ec/firma-del-proyecto-minero-los-cangrejos-impulsa-usd-1-700-millonesde-inversion-en-el-pais/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "firma del contrato de explotación minera del proyecto “Los Cangrejos”, que representa una inversión superior a USD 1.700 millones … ubicado en la provincia de El Oro, en los cantones Santa Rosa y Atahualpa, y desarrollado por la empresa ODIN Mining del Ecuador S.A., filial de MOC Group",
        "note": "Opened Ecuador MAE official boletin 27 Apr 2026 on Cangrejos contract.",
    },
    {
        "id": "mae_ecuador_cangrejos_20260427",
        "type": "government",
        "chicago": "Ecuador Ministerio de Ambiente y Energía. “Firma del Proyecto Minero Los Cangrejos Impulsa USD 1.700 Millones de Inversión en el País.” Boletín de Prensa No. 252, 27 April 2026.",
        "url": "https://www.ambienteyenergia.gob.ec/firma-del-proyecto-minero-los-cangrejos-impulsa-usd-1-700-millonesde-inversion-en-el-pais/",
        "annotation": "MAE Ecuador: ODIN/CMOC Los Cangrejos exploitation contract >USD 1.7bn. Supports cmoc_cangrejos_ecuador_1p7bn_2026.",
        "supports": ["cmoc_cangrejos_ecuador_1p7bn_2026", "hunt_res_copper"],
    },
)

# ---------------------------------------------------------------------------
# 13 energy/other_renewables — ClearPower Tinajones hydro ~USD 35m (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "clearpower_tinajones_peru_35m_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "ClearPower Global — Tinajones System modular hydropower (PEOT)",
        "country": "Peru",
        "asset": "23 Sep 2026: ClearPower Global (Miami) announces PEOT authorization to develop modular hydropower in Lambayeque Tinajones water system — up to ~20 MW initial; up to 184 GWh/y; project investment USD 35 million; 30-year concession then revert to PEOT; ≥PEN 1.5m/y to operator. In-conduit turbines on existing irrigation infrastructure. Distinct from ormat / Cerro Pabellón geothermal rows.",
        "investment_type": "concession",
        "value": "35000000",
        "currency": "USD",
        "value_usd": "35000000",
        "fx_usd": "1",
        "fx_date": "2026-09-23",
        "year": "2026",
        "status": "active",
        "lat": "-6.628",
        "lon": "-79.745",
        "geo_note": "Sistema Hidráulico Mayor Tinajones / Presa Tinajones area, Lambayeque (PEOT geography; approximate pin).",
        "evidence": "documented",
        "source_id": "clearpower_tinajones_20260923",
        "note": "Actor: ClearPower Global (U.S.) — us. Company PR Newswire 23 Sep 2026; PEOT gob.pe corroborates authorization.",
    },
    {
        "id": "clearpower_tinajones_peru_35m_2026",
        "retrieved": "2026-10-01",
        "source_id": "clearpower_tinajones_20260923",
        "url": "https://www.prnewswire.com/news-releases/clearpower-receives-peot-authorization-for-hydropower-development-in-perus-tinajones-system-302886878.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "ClearPower Global has been selected by the Olmos Tinajones Special Project (PEOT) to generate renewable hydropower from Peru's Tinajones water system. The company plans to produce approximately 20 MW of hydropower, resulting in up to 184 GWh of initial generating capacity annually. ClearPower's project investment of $35 million",
        "note": "Opened ClearPower / PR Newswire release 23 Sep 2026.",
    },
    {
        "id": "clearpower_tinajones_20260923",
        "type": "company",
        "chicago": "ClearPower Global. “ClearPower Receives PEOT Authorization for Hydropower Development in Peru’s Tinajones System.” PR Newswire, 23 September 2026.",
        "url": "https://www.prnewswire.com/news-releases/clearpower-receives-peot-authorization-for-hydropower-development-in-perus-tinajones-system-302886878.html",
        "annotation": "ClearPower USD 35m Tinajones modular hydro PEOT authorization. Supports clearpower_tinajones_peru_35m_2026.",
        "supports": ["clearpower_tinajones_peru_35m_2026", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# 15 energy/power_plants_grid — EXIM FOCOL Bahamas ~USD 99.6m (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "exim_focol_bahamas_99p6m_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "U.S. EXIM / FOCOL — GE Vernova TM2500 + Pike Electric pipelines (New Providence)",
        "country": "Bahamas",
        "asset": "27 Jun 2025: EXIM Board approves nearly USD 99.6 million for FOCOL Holdings Limited energy production in The Bahamas — two pipelines (diesel + natural gas) from Pike Electric LLC (North Carolina) and two GE Vernova TM 2500 Gen 8 aeroderivative gas turbines (Massachusetts) for New Providence power. Distinct from exim_guyana_gte_527m_2025.",
        "investment_type": "financing",
        "value": "99600000",
        "currency": "USD",
        "value_usd": "99600000",
        "fx_usd": "1",
        "fx_date": "2025-06-27",
        "year": "2025",
        "status": "active",
        "lat": "25.01",
        "lon": "-77.45",
        "geo_note": "New Providence / Blue Hills power corridor (EXIM/press geography for FOCOL turbines+pipelines; approximate pin).",
        "evidence": "documented",
        "source_id": "exim_focol_bahamas_20250627",
        "note": "Actor: U.S. EXIM financing U.S. exporters (GE Vernova / Pike Electric) — us. Official EXIM Board release.",
    },
    {
        "id": "exim_focol_bahamas_99p6m_2025",
        "retrieved": "2026-10-01",
        "source_id": "exim_focol_bahamas_20250627",
        "url": "https://www.exim.gov/news/export-import-bank-united-states-board-directors-approves-transaction-support-energy-supply",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The Export-Import Bank of the United States’ (EXIM) Board of Directors yesterday approved a nearly $99.6 million deal for FOCOL Holdings Limited, supporting energy production in The Bahamas. … Pike Electric LLC is supplying the pipelines, while Massachusetts-based General Electric (GEV) Vernova is supplying the two TM 2500 Gen 8 aeroderivative gas turbines.",
        "note": "Opened EXIM Board approval release 27 Jun 2025.",
    },
    {
        "id": "exim_focol_bahamas_20250627",
        "type": "government",
        "chicago": "Export-Import Bank of the United States. “Export-Import Bank of the United States Board of Directors Approves Transaction to Support Energy Supply Chain.” Press release, 27 June 2025.",
        "url": "https://www.exim.gov/news/export-import-bank-united-states-board-directors-approves-transaction-support-energy-supply",
        "annotation": "EXIM ~USD 99.6m FOCOL Bahamas GE Vernova turbines + Pike pipelines. Supports exim_focol_bahamas_99p6m_2025.",
        "supports": ["exim_focol_bahamas_99p6m_2025", "hunt_br_power_equip"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None and k != "supports":
                existing[k] = v
        supports = list(
            dict.fromkeys((existing.get("supports") or []) + (bib_entry.get("supports") or []))
        )
        existing["supports"] = supports
    else:
        bib.append(bib_entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
        else:
            rows.append(full)
            by_id[rid] = len(rows) - 1
            added.append(rid)
        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        upsert_bib(bib, bib_by, bib_entry)

    hunt_updates = {
        "hunt_infra_port_cranes": "Cycle 60: logged liebherr_compas_cartagena_lhm600_2026 (allied).",
        "hunt_infra_port_ownership": "Cycle 60: equal budget; APM Lázaro III / SSA Isla Palma / Hutchison ICAVE already (miss).",
        "hunt_energy_solar": "Cycle 60: logged powerchina_huayra_peru_96p9mw_2026 (PRC).",
        "hunt_energy_wind": "Cycle 60: logged vestas_argentina_217mw_2025 (allied).",
        "hunt_res_lithium": "Cycle 60: equal budget; Lilac Kachi / Albemarle TED / EnergyX EXIM already (miss).",
        "hunt_res_balsa": "Cycle 60: equal budget; AIMA 2025 mfr destinations / Plantabal→Baltek already (miss).",
        "hunt_res_water": "Cycle 60: logged cagece_dessal_fortaleza_auth_2026 (other).",
        "hunt_infra_bridges_roads": "Cycle 60: equal budget; Aldesa Chiapas / CRBC Arequipa / Quinto Puente already (miss).",
        "hunt_latam_rail_telecom": "Cycle 60: logged exim_wabtec_gmxt_185m_2025 (U.S. EXIM).",
        "hunt_fenb_araxa": "Cycle 60: equal budget; St George Boston Metal MoU / CBMM / CMOC Catalão already (miss).",
        "hunt_res_nickel": "Cycle 60: equal budget; Jervois / Westwin / DFC Piauí / Centaurus already (miss).",
        "hunt_res_copper": "Cycle 60: logged cmoc_cangrejos_ecuador_1p7bn_2026 (PRC).",
        "hunt_energy_other_renewables": "Cycle 60: logged clearpower_tinajones_peru_35m_2026 (U.S.).",
        "hunt_energy_fission_smr": "Cycle 60: equal budget; Peru SMR law / USTDA LAC nuclear / Meitner already (miss).",
        "hunt_br_power_equip": "Cycle 60: logged exim_focol_bahamas_99p6m_2025 (U.S. EXIM).",
        "hunt_infra_engineering_epc": "Cycle 60: equal budget; Baker Hughes Petrobras / Fluor / Bechtel already (miss).",
        "hunt_infra_building_materials": "Cycle 60: equal budget; Holcim Cemex Colombia / Sinoma Panam / Huaxin already (miss).",
        "hunt_res_graphite": "Cycle 60: equal budget; Graphcoa Jordânia / Atlas Malacacheta / South Star already (miss).",
    }
    for hid, note in hunt_updates.items():
        if hid in by_id:
            rows[by_id[hid]]["note"] = (
                (rows[by_id[hid]].get("note") or "") + " " + note
            ).strip()

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.dump(bib, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8",
    )
    print("Cycle 60 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
