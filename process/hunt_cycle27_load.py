#!/usr/bin/env python3
"""Cycle 27 hunt: shuffle_seed=20261027; equal budget across 18 subcategories."""
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


# seed 20261027 order:
# rail, graphite, wind, lithium, engineering_epc, balsa, fission_smr, copper,
# port_ownership, water, power_plants_grid, niobium, solar, nickel,
# bridges_roads, other_renewables, port_cranes, building_materials

# 1 infrastructure/rail — CRCC Gran Andes Santiago–Batuco surface works
A(
    {
        "id": "crcc_efe_santiago_batuco_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "prc",
        "counterpart": "CRCC / CR22 / CRCEB (Constructora Gran Andes) — EFE Santiago–Batuco surface civil/rail works",
        "country": "Chile",
        "asset": "Largest EFE contract in history: USD 470 million surface civil and railway works Mapocho–Batuco (six stations Renca/Quilicura/Lampa; seven rail bridges incl. Puente Mapocho; grade-separated crossings); part of 26 km / USD 950m Santiago–Batuco project; partial service 2028, full 2030",
        "investment_type": "epc_civil",
        "value": "470000000",
        "currency": "USD",
        "value_usd": "470000000",
        "fx_usd": "1",
        "fx_date": "2025-08-25",
        "year": "2025",
        "status": "active",
        "lat": "-33.4",
        "lon": "-70.73",
        "geo_note": "Future Estación Renca / Mapocho–Batuco corridor, Santiago Metropolitan Region (EFE release).",
        "evidence": "documented",
        "source_id": "efe_santiago_batuco_20250825",
        "note": "Actor: China Railway Construction Corporation + subsidiaries CR22/CRCEB via Constructora Gran Andes SpA — prc; counterpart EFE Trenes de Chile (state). Official EFE 25 Aug 2025. Distinct from efe_crrc_emu_2023 rolling stock and siemens_efe_etcs_chile_2025 signalling.",
    },
    {
        "id": "crcc_efe_santiago_batuco_2025",
        "retrieved": "2026-10-01",
        "source_id": "efe_santiago_batuco_20250825",
        "url": "https://www.efe.cl/efe-firma-contrato-de-obras-superficiales-del-tren-santiago-batuco-el-mas-grande-en-su-historia/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "contrato más grande en la historia de la empresa, con una inversión de US$ 470 millones, adjudicado al consorcio Constructora Gran Andes SpA, integrado por China Railway Construction Corporation (CRCC) y sus filiales CR22 y CRCEB",
        "note": "Opened EFE Trenes de Chile official Spanish release 25 Aug 2025.",
    },
    {
        "id": "efe_santiago_batuco_20250825",
        "type": "government",
        "chicago": "EFE Trenes de Chile. “EFE firma contrato de obras superficiales del Tren Santiago–Batuco, el más grande en su historia.” 25 August 2025.",
        "url": "https://www.efe.cl/efe-firma-contrato-de-obras-superficiales-del-tren-santiago-batuco-el-mas-grande-en-su-historia/",
        "annotation": "Official EFE award notice for CRCC Gran Andes USD 470m Santiago–Batuco surface works. Supports crcc_efe_santiago_batuco_2025.",
        "supports": ["crcc_efe_santiago_batuco_2025", "hunt_latam_rail_telecom"],
    },
)

# 2 resources/graphite — Graph+ / New Mining Santa Maria do Salto
A(
    {
        "id": "graph_plus_santa_maria_salto_2024",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "other",
        "counterpart": "Graph+ (New Mining) — Santa Maria do Salto graphite extraction plant (Vale do Jequitinhonha)",
        "country": "Brazil",
        "asset": "Announced >R$200 million private investment through 2028 for graphite extraction plant at Santa Maria do Salto (MG); construction ~2027–mid-2028; operations targeted July 2028; ~300 permanent jobs by 2030; prior R$4m studies 2020–24 and R$16m licensing 2025–26",
        "investment_type": "capex_mine",
        "value": "200000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-16.32",
        "lon": "-40.15",
        "geo_note": "Santa Maria do Salto, Vale do Jequitinhonha, Minas Gerais (Invest Minas / Agência Minas).",
        "evidence": "documented",
        "source_id": "invest_minas_graph_plus_20241003",
        "note": "Actor: Graph+ subsidiary of New Mining (Brazilian) — other (host-country). Official Invest Minas 3 Oct 2024 announcing Exposibram 2024 commitment. Value stored as BRL (no FX). Distinct from Graphcoa Jordânia / South Star Santa Cruz graphite rows.",
    },
    {
        "id": "graph_plus_santa_maria_salto_2024",
        "retrieved": "2026-10-01",
        "source_id": "invest_minas_graph_plus_20241003",
        "url": "https://investminas.mg.gov.br/2024/10/03/governo-anuncia-investimento-privado-superior-a-r-200-milhoes-na-exposibram-2024/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "aporte de mais de R$ 200 milhões, a ser feito até 2028, pela Graph+. A planta da empresa, subsidiária da New Mining, será voltada para a extração de grafite no município de Santa Maria do Salto",
        "note": "Opened Invest Minas official Portuguese release 3 Oct 2024.",
    },
    {
        "id": "invest_minas_graph_plus_20241003",
        "type": "government",
        "chicago": "Invest Minas. “Investimento privado de R$ 200 milhões para extração de grafite é anunciado na Exposibram 2024.” 3 October 2024.",
        "url": "https://investminas.mg.gov.br/2024/10/03/governo-anuncia-investimento-privado-superior-a-r-200-milhoes-na-exposibram-2024/",
        "annotation": "State investment agency primary on Graph+/New Mining >R$200m Santa Maria do Salto graphite plant. Supports graph_plus_santa_maria_salto_2024.",
        "supports": ["graph_plus_santa_maria_salto_2024", "hunt_res_graphite"],
    },
)

# 3 energy/wind — miss (CTG Serra da Palmeira / Goldwind / Vestas set already)
# 4 resources/lithium — miss (Zijin 3Q RIGI / CUH Arizaro / Eramet already)
# 5 infrastructure/engineering_epc — miss (PowerChina Chile G15 Parinas overlaps cen_parinas; Chancay–Sierra PowerChina press without openable MTC primary)

# 6 resources/balsa — Plantabal / 3A Composites Ecuador plantations
A(
    {
        "id": "plantabal_3a_ecuador_presence",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "allied",
        "counterpart": "Plantabal S.A. (3A Composites Core Materials) — Ecuador plantation-grown BALTEK balsa operations",
        "country": "Ecuador",
        "asset": "Largest Ecuadorian balsa forestry/processing operation (Plantabal): FSC-certified plantation-grown BALTEK core materials; nursery-to-kit vertical integration across Santo Domingo, Guayas, Cotopaxi, Esmeraldas, Manabí and Los Ríos; supplies wind/marine/aerospace core markets worldwide",
        "investment_type": "ownership_presence",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-1.03",
        "lon": "-79.47",
        "geo_note": "Plantabal main plant Quevedo, Los Ríos (3A Composites site page).",
        "evidence": "documented",
        "source_id": "a3_composites_ecuador_balsa",
        "note": "Actor: 3A Composites Core Materials / Plantabal (Schweiter Technologies group, Swiss) — allied. Company Ecuador production-site page (opened 2026-10-01). Presence — no new CAPEX USD on page. Distinct from WITS Ecuador–China/US trade-flow rows; fills thin balsa actor gap.",
    },
    {
        "id": "plantabal_3a_ecuador_presence",
        "retrieved": "2026-10-01",
        "source_id": "a3_composites_ecuador_balsa",
        "url": "https://www.3accorematerials.com/en/we-care/Ecuador",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "The 3A Composites Core Materials Ecuador operation, Plantabal S.A., has spearheaded the balsa wood business for over 85 years. 3A Composites is the largest forester in Ecuador, with thousands of hectares planted every year",
        "note": "Opened 3A Composites Core Materials Ecuador page.",
    },
    {
        "id": "a3_composites_ecuador_balsa",
        "type": "company",
        "chicago": "3A Composites Core Materials. “Production site in Ecuador.” Accessed 1 October 2026.",
        "url": "https://www.3accorematerials.com/en/we-care/Ecuador",
        "annotation": "Company primary on Plantabal FSC plantation balsa operations in Ecuador. Supports plantabal_3a_ecuador_presence.",
        "supports": ["plantabal_3a_ecuador_presence", "hunt_res_balsa"],
    },
)

# 7 energy/fission_smr — Brazil CDPNB technical group for SMR/MMR infrastructure
A(
    {
        "id": "brazil_cdpnb_smr_gt_2026",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "other",
        "counterpart": "CDPNB / ANSN — technical group to assess national infrastructure for land-based SMRs and MMRs",
        "country": "Brazil",
        "asset": "DOU publication of CDPNB Resolution CDPNB nº 43 (6 Jan 2026) creating a Technical Group to study regulatory, institutional, technical and infrastructure requirements for receiving land-based Small Modular Reactors (SMRs) and Modular Microreactors (MMRs); proposal originated with ANSN via MME",
        "investment_type": "regulatory_program",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-15.78",
        "lon": "-47.93",
        "geo_note": "National program pin Brasília (CDPNB / ANSN); no reactor site named.",
        "evidence": "documented",
        "source_id": "ird_cdpnb_smr_gt_202601",
        "note": "Actor: Brazilian nuclear governance (CDPNB/ANSN/MME) — other (domestic). Official IRD/gov.br notice on DOU publication. Pre-deployment regulatory prep — no CAPEX USD. Distinct from brazil_microreactor_cnen_2025 concept program and Argentina Meitner/CAREM/FIRST rows.",
    },
    {
        "id": "brazil_cdpnb_smr_gt_2026",
        "retrieved": "2026-10-01",
        "source_id": "ird_cdpnb_smr_gt_202601",
        "url": "https://www.gov.br/ird/pt-br/assuntos/noticias/noticias-2026/publicada-no-dou-a-criacao-de-grupo-tecnico-para-avaliar-infraestrutura-nacional-para-pequenos-reatores",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Resolução CDPNB nº 43, de 6 de janeiro de 2026, formalizou a criação de um Grupo Técnico destinado a estudar a infraestrutura nacional necessária à recepção de reatores nucleares de potência, com foco em Pequenos Reatores Modulares (SMRs) e Microrreatores Modulares (MMRs) instalados em terra",
        "note": "Opened IRD/gov.br official Portuguese notice on CDPNB Resolution 43.",
    },
    {
        "id": "ird_cdpnb_smr_gt_202601",
        "type": "government",
        "chicago": "Instituto de Radioproteção e Dosimetria (IRD/CNEN). “Publicada no DOU a criação de Grupo Técnico para avaliar infraestrutura nacional para pequenos reatores.” January 2026.",
        "url": "https://www.gov.br/ird/pt-br/assuntos/noticias/noticias-2026/publicada-no-dou-a-criacao-de-grupo-tecnico-para-avaliar-infraestrutura-nacional-para-pequenos-reatores",
        "annotation": "Official Brazilian nuclear authority notice on CDPNB SMR/MMR infrastructure technical group. Supports brazil_cdpnb_smr_gt_2026.",
        "supports": ["brazil_cdpnb_smr_gt_2026", "hunt_energy_fission_smr"],
    },
)

# 8 resources/copper — Freeport Cerro Verde second MEIA / USD 2.1bn plan
A(
    {
        "id": "fcx_cerro_verde_meia2_2100m_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "us",
        "counterpart": "Freeport-McMoRan / Sociedad Minera Cerro Verde — Second MEIA enabling operations to 2053",
        "country": "Peru",
        "asset": "Senace RD 00014-2026-SENACE-PE/DEAR (6 Feb 2026) approves Second MEIA of Cerro Verde UP; company states ~USD 2,100 million investment over coming years and operations extension to 2053 (from prior ~2045 horizon); processing capacity path 408ktpd → 420ktpd concentrates",
        "investment_type": "capex_expansion",
        "value": "2100000000",
        "currency": "USD",
        "value_usd": "2100000000",
        "fx_usd": "1",
        "fx_date": "2026-02-06",
        "year": "2026",
        "status": "active",
        "lat": "-16.533",
        "lon": "-71.567",
        "geo_note": "Cerro Verde UP, Arequipa (company / Senace geography).",
        "evidence": "documented",
        "source_id": "cerro_verde_meia2_202602",
        "note": "Actor: Sociedad Minera Cerro Verde (Freeport-McMoRan-controlled) — us. Company news citing Senace RD 00014-2026; value as company-stated approximate USD 2,100m (capex+opex per trade press; company page says inversión aproximada). Distinct from fcx_cerro_verde_peru presence-only row.",
    },
    {
        "id": "fcx_cerro_verde_meia2_2100m_2026",
        "retrieved": "2026-10-01",
        "source_id": "cerro_verde_meia2_202602",
        "url": "https://www.cerroverde.pe/senace-aprueba-segunda-modificacion-del-estudio-de-impacto-ambiental-y-social-de-cerro-verde-tras-rigurosa-evaluacion-tecnica-296",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Esta aprobación permitirá viabilizar una inversión aproximada de US$ 2100 millones a lo largo de los próximos años, lo que hará que Cerro Verde extienda sus operaciones en Arequipa … hasta el año 2053",
        "note": "Opened Cerro Verde company Spanish news page citing Senace RD 00014-2026.",
    },
    {
        "id": "cerro_verde_meia2_202602",
        "type": "company",
        "chicago": "Sociedad Minera Cerro Verde. “Senace aprueba Segunda Modificación del Estudio de Impacto Ambiental y Social de Cerro Verde tras rigurosa evaluación técnica.” February 2026.",
        "url": "https://www.cerroverde.pe/senace-aprueba-segunda-modificacion-del-estudio-de-impacto-ambiental-y-social-de-cerro-verde-tras-rigurosa-evaluacion-tecnica-296",
        "annotation": "Company primary on Senace second MEIA approval and ~USD 2.1bn Cerro Verde plan to 2053. Supports fcx_cerro_verde_meia2_2100m_2026.",
        "supports": ["fcx_cerro_verde_meia2_2100m_2026", "hunt_res_copper"],
    },
)

# 9 infrastructure/port_ownership — TISUR Matarani adenda USD 700m
A(
    {
        "id": "tisur_matarani_adenda_700m_2025",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "TISUR (Grupo Tramarsa) — Matarani port concession adenda / ~USD 700m capacity expansion",
        "country": "Peru",
        "asset": "MEF-announced signing of concession-contract adenda for Terminal Portuario de Matarani: ~USD 700 million private advanced investment (~50% capacity increase); new multipurpose berth to 60,000 DWT, 40,000 t mineral warehouse, 4.6 ha container yard; ABC quay modernization; concession extended +30 years",
        "investment_type": "concession_expansion",
        "value": "700000000",
        "currency": "USD",
        "value_usd": "700000000",
        "fx_usd": "1",
        "fx_date": "2025-11-06",
        "year": "2025",
        "status": "active",
        "lat": "-17.0",
        "lon": "-72.1",
        "geo_note": "Terminal Portuario de Matarani, Islay, Arequipa (MEF release).",
        "evidence": "documented",
        "source_id": "mef_matarani_adenda_20251106",
        "note": "Actor: TISUR / Grupo Tramarsa (Peruvian private; Global Infrastructure Partners/BlackRock hold prior stake in operator group per trade press — not restated as value source) — allied regional private. Official MEF 6 Nov 2025. Distinct from COSCO Chancay / DP World Callao / APM Callao port-ownership rows.",
    },
    {
        "id": "tisur_matarani_adenda_700m_2025",
        "retrieved": "2026-10-01",
        "source_id": "mef_matarani_adenda_20251106",
        "url": "https://www.gob.pe/institucion/mef/noticias/1283181-gobierno-garantiza-inversion-privada-de-us-700-millones-para-modernizar-el-puerto-de-matarani-y-potenciar-el-sur-del-pais",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "adelanto de inversión de aproximadamente US$ 700 millones por parte de la concesionaria … adenda suscrita entre la Autoridad Portuaria Nacional (MTC) … y TISUR (Grupo Tramarsa)",
        "note": "Opened MEF/gob.pe official Spanish release 6 Nov 2025.",
    },
    {
        "id": "mef_matarani_adenda_20251106",
        "type": "government",
        "chicago": "Ministerio de Economía y Finanzas del Perú. “Gobierno garantiza inversión privada de US$ 700 millones para modernizar el Puerto de Matarani y potenciar el sur del país.” 6 November 2025.",
        "url": "https://www.gob.pe/institucion/mef/noticias/1283181-gobierno-garantiza-inversion-privada-de-us-700-millones-para-modernizar-el-puerto-de-matarani-y-potenciar-el-sur-del-pais",
        "annotation": "Official MEF notice on TISUR Matarani concession adenda and ~USD 700m private expansion. Supports tisur_matarani_adenda_700m_2025.",
        "supports": ["tisur_matarani_adenda_700m_2025", "hunt_infra_port_ownership"],
    },
)

# 10 resources/water — China-financed Ilopango potabilization plant (El Salvador)
A(
    {
        "id": "anda_ilopango_china_water_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "prc",
        "counterpart": "PRC cooperation — ANDA Ilopango potabilization plant (Gran San Salvador)",
        "country": "El Salvador",
        "asset": "ANDA Ilopango potabilization plant under PRC cooperation: >90% global progress (May 2026); 13 treatment/support structures complete; eight production wells drilled; benefits >250,000 residents across Ilopango, Soyapango, San Martín, Santo Tomás, San Marcos, Santiago Texacuangos, San Francisco Chinameca; hydraulic tests imminent",
        "investment_type": "grant_epc",
        "value": "40000000",
        "currency": "USD",
        "value_usd": "40000000",
        "fx_usd": "1",
        "fx_date": "2026-05-21",
        "year": "2026",
        "status": "active",
        "lat": "13.7",
        "lon": "-89.11",
        "geo_note": "Ilopango potabilization plant, Gran San Salvador (ANDA release).",
        "evidence": "proxy",
        "source_id": "anda_ilopango_china_20260521",
        "note": "Actor: PRC cooperation via Chinese contractor/financing cited by ANDA — prc; counterpart ANDA (Salvadoran state). Official ANDA 21 May 2026 documents China cooperation and >90% progress; USD 40 million figure is UNVERIFIED proxy from Salvadoran press citing ANDA (not printed on opened ANDA page). Caribbean/Central America LatAm geography.",
    },
    {
        "id": "anda_ilopango_china_water_2026",
        "retrieved": "2026-10-01",
        "source_id": "anda_ilopango_china_20260521",
        "url": "https://www.anda.gob.sv/verifican-avance-en-la-construccion-de-la-nueva-planta-potabilizadora-de-ilopango/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "se concreta gracias a los lazos de solidaridad y la valiosa cooperación brindada por la República Popular China … ya alcanza más de un 90% de progreso global",
        "note": "Opened ANDA official Spanish page 21 May 2026. Value USD 40m from secondary press (UNVERIFIED).",
    },
    {
        "id": "anda_ilopango_china_20260521",
        "type": "government",
        "chicago": "Administración Nacional de Acueductos y Alcantarillados (ANDA). “Presidente de ANDA y Embajador de la República Popular China verifican el 90% de avance en la construcción de la nueva Planta Potabilizadora de Ilopango.” 21 May 2026.",
        "url": "https://www.anda.gob.sv/verifican-avance-en-la-construccion-de-la-nueva-planta-potabilizadora-de-ilopango/",
        "annotation": "Official ANDA notice on PRC-cooperated Ilopango potabilization plant progress. Supports anda_ilopango_china_water_2026 (value proxy).",
        "supports": ["anda_ilopango_china_water_2026", "hunt_res_water"],
    },
)

# 11 energy/power_plants_grid — PowerChina Coca Codo Sinclair O&M transfer
A(
    {
        "id": "powerchina_coca_codo_om_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "prc",
        "counterpart": "PowerChina — planned O&M / risk transfer for Coca Codo Sinclair (1,500 MW)",
        "country": "Ecuador",
        "asset": "CELEC EP roadmap after ICC arbitration award: definitive reception from Sinohydro plus transfer of operation, maintenance and 100% construction-defect risk of 1,500 MW Coca Codo Sinclair hydro to Power Construction Corporation of China; settlement package USD 400 million (USD 200m cash + USD 200m renewable investment for Ecuador); ownership retained by Ecuadorian state",
        "investment_type": "om_concession",
        "value": "400000000",
        "currency": "USD",
        "value_usd": "400000000",
        "fx_usd": "1",
        "fx_date": "2026-04-08",
        "year": "2026",
        "status": "active",
        "lat": "-0.2",
        "lon": "-77.7",
        "geo_note": "Coca Codo Sinclair, Napo/Sucumbíos (CELEC bulletin).",
        "evidence": "documented",
        "source_id": "celec_coca_codo_20260408",
        "note": "Actor: PowerChina (PRC SOE) for O&M/risk; Sinohydro settlement counterpart — prc. Official CELEC EP bulletin 8 Apr 2026. USD 400m is arbitration settlement package (not O&M fee). Pre-AOM signature roadmap. Distinct from transmission/EPCm PowerChina Chile rows.",
    },
    {
        "id": "powerchina_coca_codo_om_2026",
        "retrieved": "2026-10-01",
        "source_id": "celec_coca_codo_20260408",
        "url": "https://www.celec.gob.ec/hidronacion/uncategorized/la-recepcion-de-coca-codo-sinclair-fue-aprobada-por-la-corte-internacional-de-arbitraje-de-la-camara-de-comercio-internacional/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "traspasará su operación y mantenimiento y el 100% del riesgo a Power Construction Corporation of China (PowerChina). … compensación total de USD 400 millones, compuesta por USD 200 millones … y USD 200 millones para inversión en proyectos renovables",
        "note": "Opened CELEC EP / Hidronación official Spanish bulletin 8 Apr 2026.",
    },
    {
        "id": "celec_coca_codo_20260408",
        "type": "government",
        "chicago": "CELEC EP / Hidronación. “La recepción de Coca Codo Sinclair fue aprobada por la Corte Internacional de Arbitraje de la Cámara de Comercio Internacional.” 8 April 2026.",
        "url": "https://www.celec.gob.ec/hidronacion/uncategorized/la-recepcion-de-coca-codo-sinclair-fue-aprobada-por-la-corte-internacional-de-arbitraje-de-la-camara-de-comercio-internacional/",
        "annotation": "Official CELEC bulletin on ICC award, Sinohydro settlement, and PowerChina O&M/risk transfer for Coca Codo Sinclair. Supports powerchina_coca_codo_om_2026.",
        "supports": ["powerchina_coca_codo_om_2026", "hunt_br_power_equip"],
    },
)

# 12 resources/niobium — miss
# 13 energy/solar — miss
# 14 resources/nickel — miss
# 15 infrastructure/bridges_roads — miss
# 16 energy/other_renewables — miss
# 17 infrastructure/port_cranes — miss

# 18 infrastructure/building_materials — Votorantim Nobres/Cuiabá R$330m
A(
    {
        "id": "votorantim_nobres_cuiaba_330m_2025",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "other",
        "counterpart": "Votorantim Cimentos — Nobres grinding expansion + Cuiabá tire-shredding modernization (Mato Grosso)",
        "country": "Brazil",
        "asset": "R$330 million investment announced 4 Aug 2025 for Mato Grosso: new cement mill at Nobres (+60% to 1.2 Mtpy cement; aglime to 900 ktpy) plus Verdera tire-shredding/co-processing modernization at Cuiabá; construction 2025–end 2026; part of R$5bn Brazil 2024–28 plan",
        "investment_type": "capex_expansion",
        "value": "330000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-14.72",
        "lon": "-56.33",
        "geo_note": "Nobres cement plant, Mato Grosso (Votorantim Cimentos release; Cuiabá component co-located in same announcement).",
        "evidence": "documented",
        "source_id": "votorantim_nobres_cuiaba_20250804",
        "note": "Actor: Votorantim Cimentos (Brazilian) — other. Company English release 4 Aug 2025. Value stored as BRL (no FX). Distinct from votorantim_xambioa_grind_2026 and sinoma_votorantim_z02_br_2024 (Sinoma EPC at Edealina).",
    },
    {
        "id": "votorantim_nobres_cuiaba_330m_2025",
        "retrieved": "2026-10-01",
        "source_id": "votorantim_nobres_cuiaba_20250804",
        "url": "https://www.votorantimcimentos.com/news/we-announced-r330-million-investment-to-expand-and-modernize-cuiaba-and-nobres-plants-in-brazil/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "We announced today a R$330 million investment in the state of Mato Grosso, including expansions and the modernization of its sites located in the towns of Cuiabá and Nobres",
        "note": "Opened Votorantim Cimentos company English release 4 Aug 2025.",
    },
    {
        "id": "votorantim_nobres_cuiaba_20250804",
        "type": "company",
        "chicago": "Votorantim Cimentos. “We announced R$330 million investment to expand and modernize Cuiabá and Nobres plants in Brazil.” 4 August 2025.",
        "url": "https://www.votorantimcimentos.com/news/we-announced-r330-million-investment-to-expand-and-modernize-cuiaba-and-nobres-plants-in-brazil/",
        "annotation": "Company primary on R$330m Nobres/Cuiabá cement expansions. Supports votorantim_nobres_cuiaba_330m_2025.",
        "supports": ["votorantim_nobres_cuiaba_330m_2025", "hunt_infra_building_materials"],
    },
)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {b["id"]: i for i, b in enumerate(bib)}
    added = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: "" for k in FIELDS}
        full.update(row)
        if rid in by_id:
            rows[by_id[rid]] = full
        else:
            by_id[rid] = len(rows)
            rows.append(full)
        added.append(rid)

        EVID.mkdir(parents=True, exist_ok=True)
        (EVID / f"{rid}.json").write_text(
            json.dumps(evidence, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

        sid = bib_entry["id"]
        if sid in bib_by:
            existing = bib[bib_by[sid]]
            supports = set(existing.get("supports") or [])
            supports.update(bib_entry.get("supports") or [])
            existing["supports"] = sorted(supports)
            for k in ("chicago", "url", "annotation", "type"):
                if bib_entry.get(k):
                    existing[k] = bib_entry[k]
        else:
            bib.append(bib_entry)
            bib_by[sid] = len(bib) - 1

    hunt_updates = {
        "hunt_latam_rail_telecom": "Cycle 27: logged crcc_efe_santiago_batuco_2025.",
        "hunt_res_graphite": "Cycle 27: logged graph_plus_santa_maria_salto_2024.",
        "hunt_energy_wind": "Cycle 27: equal budget; CTG Serra da Palmeira / Goldwind / Vestas set already logged (miss).",
        "hunt_res_lithium": "Cycle 27: equal budget; Zijin 3Q RIGI / CUH Arizaro / Eramet already logged (miss).",
        "hunt_infra_engineering_epc": "Cycle 27: equal budget; PowerChina Chile G15 Parinas overlaps cen_parinas; Chancay–Sierra PowerChina without openable MTC primary (miss).",
        "hunt_res_balsa": "Cycle 27: logged plantabal_3a_ecuador_presence.",
        "hunt_energy_fission_smr": "Cycle 27: logged brazil_cdpnb_smr_gt_2026.",
        "hunt_res_copper": "Cycle 27: logged fcx_cerro_verde_meia2_2100m_2026.",
        "hunt_infra_port_ownership": "Cycle 27: logged tisur_matarani_adenda_700m_2025.",
        "hunt_res_water": "Cycle 27: logged anda_ilopango_china_water_2026.",
        "hunt_br_power_equip": "Cycle 27: logged powerchina_coca_codo_om_2026.",
        "hunt_fenb_araxa": "Cycle 27: equal budget; CBMM/CMOC/Taboca/St George set already logged (miss).",
        "hunt_energy_solar": "Cycle 27: equal budget; PowerChina Francisco Juana Colombia trade-press only without company primary (miss).",
        "hunt_res_nickel": "Cycle 27: equal budget; MMG Anglo / Centaurus / Atlantic Nickel already logged (miss).",
        "hunt_infra_bridges_roads": "Cycle 27: equal budget; CCECC Quinto Puente / Salvador–Itaparica already logged (miss).",
        "hunt_energy_other_renewables": "Cycle 27: equal budget; BYD/Grenergy / Trina BESS set already logged (miss).",
        "hunt_infra_port_cranes": "Cycle 27: equal budget; ZPMC Santos / MultiRio / Kalmar set already logged (miss).",
        "hunt_infra_building_materials": "Cycle 27: logged votorantim_nobres_cuiaba_330m_2025.",
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
    print("Cycle 27 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
