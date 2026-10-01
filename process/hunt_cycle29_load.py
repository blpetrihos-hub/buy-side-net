#!/usr/bin/env python3
"""Cycle 29 hunt: shuffle_seed=20261029; equal budget across 18 subcategories."""
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


# seed 20261029 order:
# balsa, port_ownership, bridges_roads, nickel, fission_smr, power_plants_grid,
# copper, port_cranes, niobium, water, rail, building_materials, wind,
# engineering_epc, graphite, lithium, solar, other_renewables

# 1 resources/balsa — miss (AIMA 2025 manufactures pair logged C28)

# 2 infrastructure/port_ownership — Marcona / Jinzhao
A(
    {
        "id": "jinzhao_marcona_port_concession_2024",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "prc",
        "counterpart": "Terminal Portuario Jinzhao Perú / San Juan Port — Nuevo Terminal Portuario San Juan de Marcona",
        "country": "Peru",
        "asset": "APP concession: design, finance, build, operate and maintain Nuevo Terminal Portuario de San Juan de Marcona (Nazca, Ica); ProInversión direct award 22 Mar 2024 to Terminal Portuario Jinzhao Perú S.A. after no third-party interest; contract signed 31 Mar 2026 (PROINVERSIÓN as concedente; Sociedad Concesionaria San Juan Port S.A.); investment US$ 405 million; two berths / three berths multipurpose + mineral; third-largest Peruvian port after Callao and Chancay (agency framing)",
        "investment_type": "ppp_concession",
        "value": "405000000",
        "currency": "USD",
        "value_usd": "405000000",
        "fx_usd": "1",
        "fx_date": "2024-03-22",
        "year": "2024",
        "status": "active",
        "lat": "-15.36",
        "lon": "-75.17",
        "geo_note": "San Juan de Marcona, Nazca province, Ica region (ProInversión).",
        "evidence": "documented",
        "source_id": "proinversion_marcona_jinzhao_20240322",
        "note": "Actor: Terminal Portuario Jinzhao Perú S.A. (Chinese Jinzhao Mining SPV; contract vehicle later styled Sociedad Concesionaria San Juan Port S.A.) — prc. Official ProInversión comunicado 22 Mar 2024 names Jinzhao and US$405m; Invest in Peru 31 Mar 2026 confirms contract signature and US$405m. Distinct from Cosco Chancay / DP World Callao / APM / Hutchison / ICTSI / Tisur Matarani port rows.",
    },
    {
        "id": "jinzhao_marcona_port_concession_2024",
        "retrieved": "2026-10-01",
        "source_id": "proinversion_marcona_jinzhao_20240322",
        "url": "https://www.gob.pe/institucion/proinversion/noticias/925401-comunicado-proinversion",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "PROINVERSIÓN adjudicó a la empresa Terminal Portuario Jinzhao Perú S.A el diseño, financiamiento, construcción, operación y mantenimiento del Nuevo Terminal Portuario de San Juan de Marcona … compromete una inversión para el país de US$ 405 millones",
        "note": "Opened official ProInversión Spanish comunicado. Contract-signing corroboration: Invest in Peru 31 Mar 2026.",
    },
    {
        "id": "proinversion_marcona_jinzhao_20240322",
        "type": "government",
        "chicago": "Agencia de Promoción de la Inversión Privada (PROINVERSIÓN). “Comunicado ProInversión” (adjudicación Terminal Portuario Jinzhao Perú — Nuevo Terminal Portuario de San Juan de Marcona). 22 March 2024.",
        "url": "https://www.gob.pe/institucion/proinversion/noticias/925401-comunicado-proinversion",
        "annotation": "Official award of Marcona multipurpose port concession to Jinzhao Perú at US$405m. Supports jinzhao_marcona_port_concession_2024.",
        "supports": ["jinzhao_marcona_port_concession_2024", "hunt_infra_port_ownership"],
    },
)

# 3 infrastructure/bridges_roads — OHLA Panamericana Este
A(
    {
        "id": "ohla_panama_panamericana_este_2025",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "allied",
        "counterpart": "OHLA — Carretera Panamericana Este rehabilitation (Panamá–Yaviza)",
        "country": "Panama",
        "asset": "Rehabilitation and improvement of ~246 km Panamericana Este between Ciudad de Panamá and Yaviza (Darién): paving and rest-bay/paradero expansion; awarded by Concesionaria Ruta del Este; estimated investment USD 260 million; 20-month construction; works start planned June 2025",
        "investment_type": "epc",
        "value": "260000000",
        "currency": "USD",
        "value_usd": "260000000",
        "fx_usd": "1",
        "fx_date": "2025-05-22",
        "year": "2025",
        "status": "active",
        "lat": "8.4",
        "lon": "-78.15",
        "geo_note": "Panamericana Este corridor Panamá City–Yaviza / Darién (OHLA release; approximate mid-corridor pin).",
        "evidence": "documented",
        "source_id": "ohla_panama_este_20250522",
        "note": "Actor: OHLA (Spanish; Mexican Amodio controlling shareholders) — allied. Company Spanish release 22 May 2025. Distinct from mop_panama_panamericana_oeste_2026 (Mexican consortium APP) and chec_fourth_bridge_panama / OHLA BR-040 Brazil rows.",
    },
    {
        "id": "ohla_panama_panamericana_este_2025",
        "retrieved": "2026-10-01",
        "source_id": "ohla_panama_este_20250522",
        "url": "https://www.ohla-group.com/ohla-refuerza-su-presencia-en-panama-con-un-nuevo-contrato-para-rehabilitar-la-carretera-panamericana-este/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "El proyecto abarca una longitud aproximada de 246 kilómetros entre la Ciudad de Panamá y Yaviza, en la provincia del Darién … con una inversión estimada de 260 millones de dólares.",
        "note": "Opened OHLA company Spanish page 22 May 2025.",
    },
    {
        "id": "ohla_panama_este_20250522",
        "type": "company",
        "chicago": "OHLA. “OHLA refuerza su presencia en Panamá con un nuevo contrato para rehabilitar la Carretera Panamericana Este.” 22 May 2025.",
        "url": "https://www.ohla-group.com/ohla-refuerza-su-presencia-en-panama-con-un-nuevo-contrato-para-rehabilitar-la-carretera-panamericana-este/",
        "annotation": "Company primary on USD 260m Panamericana Este rehab award. Supports ohla_panama_panamericana_este_2025.",
        "supports": ["ohla_panama_panamericana_este_2025", "hunt_infra_bridges_roads"],
    },
)

# 4 resources/nickel — miss (Glencore Jaguar / MMG / Atlantic already logged)
# 5 energy/fission_smr — miss (Meitner / CAREM / CDPNB / FIRST already)
# 6 energy/power_plants_grid — miss (thick; no new distinct grid award)
# 7 resources/copper — miss (Cerro Verde MEIA-2 / Toromocho ITS-3 already)

# 8 infrastructure/port_cranes — Konecranes Super Terminais Manaus
A(
    {
        "id": "konecranes_super_terminais_manaus_2025",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Konecranes — 3 Gottwald ESP.10 MHC for Super Terminais (Manaus)",
        "country": "Brazil",
        "asset": "Repeat order booked Q2 2025 for three Konecranes Gottwald ESP.10 pedestal-mounted mobile harbor cranes for Super Terminais at Port of Manaus; handover scheduled Q3 2026; doubles MHC fleet vs 2021 first three ESP.10 units; shore-power capable; max reach 64 m for up to super-post-Panamax",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-3.14",
        "lon": "-60.02",
        "geo_note": "Super Terminais, Port of Manaus, Amazonas (Konecranes release).",
        "evidence": "documented",
        "source_id": "konecranes_super_terminais_20250710",
        "note": "Actor: Konecranes (Finnish) — allied; buyer Super Terminais (Brazilian). Company Cision release 10 Jul 2025. No contract USD on page. Distinct from Konecranes Portonave RTG / Cartagena RTG / Arica MHC / Yucatán Progreso and ZPMC Santos/Aguadulce crane rows.",
    },
    {
        "id": "konecranes_super_terminais_manaus_2025",
        "retrieved": "2026-10-01",
        "source_id": "konecranes_super_terminais_20250710",
        "url": "https://news.cision.com/konecranes-oyj/r/super-terminais-orders-three-more-konecranes-gottwald-esp-10-mobile-harbor-cranes-to-expand-its-amaz,c4205040",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Port of Manaus operator Super Terminais … has placed a repeat order for three Konecranes Gottwald ESP.10 pedestal-mounted cranes. The deal was booked in Q2 2025, with handover scheduled for Q3 2026.",
        "note": "Opened Konecranes Cision English release 10 Jul 2025.",
    },
    {
        "id": "konecranes_super_terminais_20250710",
        "type": "company",
        "chicago": "Konecranes. “Super Terminais orders three more Konecranes Gottwald ESP.10 Mobile Harbor Cranes to expand its Amazon River operations.” 10 July 2025.",
        "url": "https://news.cision.com/konecranes-oyj/r/super-terminais-orders-three-more-konecranes-gottwald-esp-10-mobile-harbor-cranes-to-expand-its-amaz,c4205040",
        "annotation": "Company primary on Manaus ESP.10 MHC repeat order. Supports konecranes_super_terminais_manaus_2025.",
        "supports": ["konecranes_super_terminais_manaus_2025", "hunt_infra_port_cranes"],
    },
)

# 9 resources/niobium — miss (St George permitting / CBMM capex already)
# 10 resources/water — miss (Sacyr Coquimbo / Cox Rosarito / Acciona / IDE already; Enlozada press-only)

# 11 infrastructure/rail — CRRC México–Pachuca (press fallo)
A(
    {
        "id": "crrc_mexico_pachuca_trains_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "prc",
        "counterpart": "CRRC Zhuzhou + México Railway Transportation Equipment — CDMX–Pachuca 15 EMUs",
        "country": "Mexico",
        "asset": "ARTF award (Sep 2025) to CRRC Zhuzhou Locomotive Co. Ltd. in joint participation with México Railway Transportation Equipment for 15 passenger trains with ERTMS, workshop fit-out and 60-month maintenance for Tren Ciudad de México–Pachuca / AIFA–Pachuca; contract total MXN 5,846,410,431.88 incl. VAT; term through 30 Oct 2032 (UNVERIFIED press citing ARTF fallo)",
        "investment_type": "equipment_supply",
        "value": "5846410431.88",
        "currency": "MXN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "19.85",
        "lon": "-98.95",
        "geo_note": "CDMX–Pachuca / AIFA passenger corridor (press citing ARTF; approximate mid-corridor pin).",
        "evidence": "proxy",
        "source_id": "elfinanciero_crrc_pachuca_20250912",
        "note": "Actor: CRRC Zhuzhou (PRC SOE) — prc. UNVERIFIED proxy: El Financiero / Info-Transportes / La Silla Rota citing ARTF fallo figures; ARTF primary PDF unreachable from hunt environment. Value stored as MXN (no FX). Distinct from alstom_mexico_dmu_2025 (47 DMUs other corridors) and CRRC São Paulo / Salvador metro rows.",
    },
    {
        "id": "crrc_mexico_pachuca_trains_2025",
        "retrieved": "2026-10-01",
        "source_id": "elfinanciero_crrc_pachuca_20250912",
        "url": "https://www.elfinanciero.com.mx/empresas/2025/09/12/china-mete-las-manos-en-la-obra-mexico-pachuca-crrc-zhuzhou-locomotive-vendera-15-trenes-electricos/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "CRRC Zhuzhou Locomotive … ganó el contrato para suministrar 15 trenes eléctricos para la ruta México-Pachuca … el contrato adjudicado asciende a 5 mil 846 millones de pesos, con IVA incluido",
        "note": "Opened El Financiero Spanish press citing ARTF award. Cross-checked Info-Transportes MXN 5,846,410,431.88 figure.",
    },
    {
        "id": "elfinanciero_crrc_pachuca_20250912",
        "type": "press",
        "chicago": "El Financiero. “China ‘mete las manos’ en la obra México-Pachuca: CRRC Zhuzhou Locomotive venderá 15 trenes eléctricos.” 12 September 2025.",
        "url": "https://www.elfinanciero.com.mx/empresas/2025/09/12/china-mete-las-manos-en-la-obra-mexico-pachuca-crrc-zhuzhou-locomotive-vendera-15-trenes-electricos/",
        "annotation": "UNVERIFIED press on ARTF CRRC Zhuzhou CDMX–Pachuca 15-train award (~MXN 5.85bn). Supports crrc_mexico_pachuca_trains_2025.",
        "supports": ["crrc_mexico_pachuca_trains_2025", "hunt_latam_rail_telecom"],
    },
)

# 12 infrastructure/building_materials — Holcim Guayaquil calcined clay
A(
    {
        "id": "holcim_guayaquil_calcined_clay_2025",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Holcim Ecuador — Guayaquil calcined-clay cement project",
        "country": "Ecuador",
        "asset": "Holcim Ecuador calcined-clay (arcillas calcinadas) project at Guayaquil cement plant: company states USD 17 million investment to produce lower-carbon cement with calcined clay; secondary industry press places commissioning 2H 2025 and up to ~0.9 Mtpa calcined-clay cement capacity (capacity figure not on Holcim EC page — not entered)",
        "investment_type": "capex_expansion",
        "value": "17000000",
        "currency": "USD",
        "value_usd": "17000000",
        "fx_usd": "1",
        "fx_date": "2025-01-01",
        "year": "2025",
        "status": "active",
        "lat": "-2.17",
        "lon": "-79.9",
        "geo_note": "Holcim Planta Guayaquil cement works, Guayas (Holcim Ecuador project page).",
        "evidence": "documented",
        "source_id": "holcim_ec_arcillas_calcinadas",
        "note": "Actor: Holcim Ecuador (Swiss Holcim) — allied. Company Spanish page states $17 million. Distinct from Holcim Pacasmayo / Comacsa Peru and Cemex Colombia building-materials rows.",
    },
    {
        "id": "holcim_guayaquil_calcined_clay_2025",
        "retrieved": "2026-10-01",
        "source_id": "holcim_ec_arcillas_calcinadas",
        "url": "https://www.holcim.com.ec/arcillas-calcinadas",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Con una inversión de $17 millones, Holcim Ecuador lidera un proyecto de arcillas calcinadas que transforma la industria del cemento hacia un modelo más sostenible",
        "note": "Opened Holcim Ecuador Spanish project page.",
    },
    {
        "id": "holcim_ec_arcillas_calcinadas",
        "type": "company",
        "chicago": "Holcim Ecuador. “Proyecto de Arcillas Calcinadas.” n.d. (opened 2026-10-01).",
        "url": "https://www.holcim.com.ec/arcillas-calcinadas",
        "annotation": "Company primary on USD 17m Guayaquil calcined-clay cement project. Supports holcim_guayaquil_calcined_clay_2025.",
        "supports": ["holcim_guayaquil_calcined_clay_2025", "hunt_infra_building_materials"],
    },
)

# 13 energy/wind — miss (Goldwind Sento Sé / Envision / Vestas already)

# 14 infrastructure/engineering_epc — PowerChina UFN-III Petrobras
A(
    {
        "id": "powerchina_ufn3_petrobras_epc_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "prc",
        "counterpart": "POWERCHINA — UFN-III nitrogen fertilizer plant EPC lots 6/8/10 (Petrobras)",
        "country": "Brazil",
        "asset": "EPC contracts signed 25 Jun 2026 with Petrobras for lots 6, 8 and 10 of UFN-III Nitrogen Fertilizer Plant at Três Lagoas (Mato Grosso do Sul); Novo PAC flagship; design capacity ~1.2 Mtpa urea + ~700 ktpa anhydrous ammonia; ops targeted 2029; PowerChina states first fertilizer plant project globally incorporating its core processing technologies. Contract USD not disclosed on opened page.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-20.79",
        "lon": "-51.71",
        "geo_note": "Três Lagoas, Mato Grosso do Sul (PowerChina release).",
        "evidence": "documented",
        "source_id": "powerchina_ufn3_20260706",
        "note": "Actor: POWERCHINA (PRC SOE) — prc; client Petrobras (Brazilian). Company English release 6 Jul 2026. Non-energy industrial EPC (fertilizer) under engineering_epc. No lot USD on page. Distinct from PowerChina Coca Codo / San Gabán / Chucas energy rows and Fluor/Bechtel/Worley mining EPC rows.",
    },
    {
        "id": "powerchina_ufn3_petrobras_epc_2026",
        "retrieved": "2026-10-01",
        "source_id": "powerchina_ufn3_20260706",
        "url": "https://en.powerchina.cn/2026-07/06/c_829084.htm",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "POWERCHINA and Petrobras signed the engineering, procurement, and construction (EPC) contracts for EPC lot 6, 8, and 10 of the UFN-III Nitrogen Fertilizer Plant Project on June 25.",
        "note": "Opened PowerChina English company page 6 Jul 2026.",
    },
    {
        "id": "powerchina_ufn3_20260706",
        "type": "company",
        "chicago": "POWERCHINA. “POWERCHINA to construct fertilizer plant in Brazil.” 6 July 2026.",
        "url": "https://en.powerchina.cn/2026-07/06/c_829084.htm",
        "annotation": "Company primary on Petrobras UFN-III EPC lots 6/8/10 at Três Lagoas. Supports powerchina_ufn3_petrobras_epc_2026.",
        "supports": ["powerchina_ufn3_petrobras_epc_2026", "hunt_infra_engineering_epc"],
    },
)

# 15 resources/graphite — miss (Graphcoa Jordânia / South Star / Graph+ already)
# 16 resources/lithium — miss (Lanshen / Zijin RIGI / Rio Tinto already)

# 17 energy/solar — YPF Luz El Quemado
A(
    {
        "id": "ypf_luz_el_quemado_solar_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "other",
        "counterpart": "YPF Luz — Parque Solar El Quemado 305 MW (Mendoza)",
        "country": "Argentina",
        "asset": "Inauguration 15 May 2026 of El Quemado solar park in Las Heras, Mendoza: 305 MW installed capacity (first RIGI renewable project to enter operation); company investment USD 211 million; staged COD — 200 MW online Dec 2025–Feb 2026 with final 105 MW in technical tests; MATER offtake",
        "investment_type": "greenfield",
        "value": "211000000",
        "currency": "USD",
        "value_usd": "211000000",
        "fx_usd": "1",
        "fx_date": "2026-05-15",
        "year": "2026",
        "status": "active",
        "lat": "-32.48",
        "lon": "-68.85",
        "geo_note": "Las Heras department, ~53 km north of Mendoza city (YPF Luz release).",
        "evidence": "documented",
        "source_id": "ypf_luz_el_quemado_20260515",
        "note": "Actor: YPF Luz (Argentine YPF renewable subsidiary) — other. Company news 15 May 2026. Distinct from AES Andes Solar Hub / Enel Guayepo / PowerChina Francisco Juana solar rows; not a U.S./PRC OEM equity deal.",
    },
    {
        "id": "ypf_luz_el_quemado_solar_2026",
        "retrieved": "2026-10-01",
        "source_id": "ypf_luz_el_quemado_20260515",
        "url": "https://www.ypfluz.com/Noticias/NoticiaCompleta/219",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "El nuevo parque tiene 305 MW de capacidad instalada … Requirió una inversión de USD 211 millones y es el primer proyecto en comenzar a operar bajo el RIGI.",
        "note": "Opened YPF Luz Spanish company news page 15 May 2026.",
    },
    {
        "id": "ypf_luz_el_quemado_20260515",
        "type": "company",
        "chicago": "YPF Luz. “YPF Luz inauguró El Quemado, el parque solar más grande de la Argentina.” 15 May 2026.",
        "url": "https://www.ypfluz.com/Noticias/NoticiaCompleta/219",
        "annotation": "Company primary on USD 211m / 305 MW El Quemado solar inauguration. Supports ypf_luz_el_quemado_solar_2026.",
        "supports": ["ypf_luz_el_quemado_solar_2026", "hunt_energy_solar"],
    },
)

# 18 energy/other_renewables — Ormat Dominica COD
A(
    {
        "id": "ormat_dominica_geothermal_cod_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "Ormat Technologies — Dominica 10 MW Laudat geothermal COD",
        "country": "Dominica",
        "asset": "Commercial operation of 10 MW Dominica (Laudat / Roseau Valley) binary geothermal plant achieved July 2026 (company: July 2026 COD; earnings call: full operation since 31 July); expands Ormat Caribbean generation beside Bouillante (Guadeloupe); distinct milestone from Dec 2023 25-year DOMLEC PPA",
        "investment_type": "commissioning",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "15.3",
        "lon": "-61.37",
        "geo_note": "Laudat / Roseau Valley geothermal plant, Dominica (Ormat Q2 2026 release).",
        "evidence": "documented",
        "source_id": "ormat_q2_2026_results",
        "note": "Actor: Ormat Technologies (U.S.) — us. Company Q2 2026 results 5 Aug 2026. No incremental CAPEX USD on page. Distinct from ormat_dominica_geothermal_ppa_2023 (PPA award) and Ormat Amatitlán/Zunil Guatemala rows.",
    },
    {
        "id": "ormat_dominica_geothermal_cod_2026",
        "retrieved": "2026-10-01",
        "source_id": "ormat_q2_2026_results",
        "url": "https://investor.ormat.com/news-events/news/news-details/2026/Ormat-Technologies-Reports-Second-Quarter-2026-Financial-Results/default.aspx",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "In July 2026, we achieved commercial operation of our 10 MW Dominica geothermal power plant",
        "note": "Opened Ormat investor Q2 2026 results page. SEC exhibit mirrors same COD language.",
    },
    {
        "id": "ormat_q2_2026_results",
        "type": "company",
        "chicago": "Ormat Technologies, Inc. “Ormat Technologies Reports Second Quarter 2026 Financial Results.” 5 August 2026.",
        "url": "https://investor.ormat.com/news-events/news/news-details/2026/Ormat-Technologies-Reports-Second-Quarter-2026-Financial-Results/default.aspx",
        "annotation": "Company primary confirming July 2026 COD of 10 MW Dominica geothermal plant. Supports ormat_dominica_geothermal_cod_2026.",
        "supports": ["ormat_dominica_geothermal_cod_2026", "hunt_energy_other_renewables"],
    },
)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {b["id"]: i for i, b in enumerate(bib) if isinstance(b, dict) and "id" in b}

    added = []
    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        if rid in by_id:
            rows[by_id[rid]].update({k: v for k, v in row.items() if v != ""})
        else:
            rows.append({k: row.get(k, "") for k in FIELDS})
            by_id[rid] = len(rows) - 1
            added.append(rid)

        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

        sid = bib_entry["id"]
        if sid in bib_by:
            existing = bib[bib_by[sid]]
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
            if bib_entry.get("supports"):
                existing["supports"] = sorted(
                    set(existing.get("supports") or []) | set(bib_entry["supports"])
                )
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

    # Secondary Invest in Peru corroboration bib for Marcona contract signing
    marcona_sign = {
        "id": "investinperu_marcona_contract_20260331",
        "type": "government",
        "chicago": "PROINVERSIÓN / Invest in Peru. “PROINVERSIÓN suscribe contrato de más de US$ 400 millones para nuevo Terminal Portuario de San Juan de Marcona.” 31 March 2026.",
        "url": "https://www.investinperu.pe/proinversion-suscribe-contrato-de-mas-de-us-400-millones-para-nuevo-terminal-portuario-de-san-juan-de-marcona/",
        "annotation": "Official contract-signing notice (US$405m; San Juan Port S.A.). Corroborates jinzhao_marcona_port_concession_2024.",
        "supports": ["jinzhao_marcona_port_concession_2024", "hunt_infra_port_ownership"],
    }
    if marcona_sign["id"] not in bib_by:
        bib.append(marcona_sign)

    hunt_updates = {
        "hunt_res_balsa": "Cycle 29: equal budget; AIMA 2025 manufactures China/US pair logged C28 (miss).",
        "hunt_infra_port_ownership": "Cycle 29: logged jinzhao_marcona_port_concession_2024.",
        "hunt_infra_bridges_roads": "Cycle 29: logged ohla_panama_panamericana_este_2025.",
        "hunt_res_nickel": "Cycle 29: equal budget; Glencore Jaguar / MMG / Atlantic already logged (miss).",
        "hunt_energy_fission_smr": "Cycle 29: equal budget; Meitner / CAREM / CDPNB / FIRST already logged (miss).",
        "hunt_br_power_equip": "Cycle 29: equal budget; thick grid set; no new distinct award (miss).",
        "hunt_res_copper": "Cycle 29: equal budget; Cerro Verde MEIA-2 / Toromocho ITS-3 already logged (miss).",
        "hunt_infra_port_cranes": "Cycle 29: logged konecranes_super_terminais_manaus_2025.",
        "hunt_fenb_araxa": "Cycle 29: equal budget; St George permitting / CBMM capex already logged (miss).",
        "hunt_res_water": "Cycle 29: equal budget; Sacyr Coquimbo / Cox Rosarito / Acciona / IDE already; Cerro Verde Enlozada press-only (miss).",
        "hunt_latam_rail_telecom": "Cycle 29: logged crrc_mexico_pachuca_trains_2025 (UNVERIFIED proxy).",
        "hunt_infra_building_materials": "Cycle 29: logged holcim_guayaquil_calcined_clay_2025.",
        "hunt_energy_wind": "Cycle 29: equal budget; Goldwind Sento Sé / Envision / Vestas already logged (miss).",
        "hunt_infra_engineering_epc": "Cycle 29: logged powerchina_ufn3_petrobras_epc_2026.",
        "hunt_res_graphite": "Cycle 29: equal budget; Graphcoa Jordânia / South Star / Graph+ already logged (miss).",
        "hunt_res_lithium": "Cycle 29: equal budget; Lanshen / Zijin RIGI / Rio Tinto already logged (miss).",
        "hunt_energy_solar": "Cycle 29: logged ypf_luz_el_quemado_solar_2026.",
        "hunt_energy_other_renewables": "Cycle 29: logged ormat_dominica_geothermal_cod_2026.",
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
    print("Cycle 29 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
