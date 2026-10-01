#!/usr/bin/env python3
"""Cycle 36 hunt: shuffle_seed=20261036; equal budget across 18 subcategories."""
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


# seed 20261036 order:
# fission_smr, nickel, building_materials, solar, power_plants_grid, niobium,
# balsa, rail, wind, lithium, copper, graphite, bridges_roads, other_renewables,
# port_cranes, port_ownership, water, engineering_epc

# 1 energy/fission_smr — miss (Meitner ACR-300 / Brazil microreactor / Nuclearis already)

# 2 resources/nickel — Brazilian Nickel Piauí total CAPEX USD 1.4bn (distinct from DFC LOI)
A(
    {
        "id": "brazilian_nickel_pnp_capex_1p4bn_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "Brazilian Nickel (TechMet) — Projeto Piauí Níquel total CAPEX",
        "country": "Brazil",
        "asset": "17 Jun 2026 Bloomberg Línea interview with CFO André Simão: planned Piauí Nickel/Cobalt mine CAPEX USD 1.4 billion; seeking anchor equity (BNDES/DFC/EC) plus Canada ECA up to USD 275 million debt and Ecora ~USD 62 million; target ~28 ktpa Ni + 1 ktpa Co first 10 years; production 1H 2030. Distinct from brazilian_nickel_dfc_loi_2024 (DFC LOI up to USD 550m senior debt only)",
        "investment_type": "greenfield_mine",
        "value": "1400000000",
        "currency": "USD",
        "value_usd": "1400000000",
        "fx_usd": "1",
        "fx_date": "2026-06-17",
        "year": "2026",
        "status": "active",
        "lat": "-5.09",
        "lon": "-42.8",
        "geo_note": "Piauí Nickel Project, Northeast Brazil (company geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "bloomberg_linea_brn_pnp_20260617",
        "note": "Actor: Brazilian Nickel (UK) with TechMet (Ireland) as largest investor — allied. UNVERIFIED proxy: Bloomberg Línea 17 Jun 2026 CFO interview. Press-only CAPEX; financing not closed.",
    },
    {
        "id": "brazilian_nickel_pnp_capex_1p4bn_2026",
        "retrieved": "2026-10-01",
        "source_id": "bloomberg_linea_brn_pnp_20260617",
        "url": "https://www.bloomberglinea.com.br/negocios/brazilian-nickel-busca-investidor-ancora-para-mina-de-us-14-bilhao-no-piaui/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "A Brazilian Nickel procura um investidor-âncora para ajudar a atrair mais investimentos em participação acionária para sua planejada mina de níquel e cobalto de US$ 1,4 bilhão no Nordeste.",
        "note": "Opened Bloomberg Línea Portuguese 17 Jun 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "bloomberg_linea_brn_pnp_20260617",
        "type": "trade_press",
        "chicago": "Durão, Mariana, and Annie Lee. “Brazilian Nickel busca investidor-âncora para mina de US$ 1,4 bilhão no Piauí.” Bloomberg Línea, 17 June 2026.",
        "url": "https://www.bloomberglinea.com.br/negocios/brazilian-nickel-busca-investidor-ancora-para-mina-de-us-14-bilhao-no-piaui/",
        "annotation": "CFO interview stating Piauí Nickel CAPEX USD 1.4bn. Supports brazilian_nickel_pnp_capex_1p4bn_2026.",
        "supports": ["brazilian_nickel_pnp_capex_1p4bn_2026", "hunt_res_nickel"],
    },
)

# 3 infrastructure/building_materials — Holcim México Macuspana grind USD 55m
A(
    {
        "id": "holcim_macuspana_grind_55m_2024",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Holcim México — Macuspana (Tabasco) cement grinding unit",
        "country": "Mexico",
        "asset": "13 Feb 2024 Holcim México company release: USD 55 million for new grinding unit at Macuspana cement plant (Tabasco), lifting cement capacity to 1.5 Mtpy to supply Tabasco, Chiapas, Campeche, Yucatán, Quintana Roo; ~800 construction jobs; ops targeted end-2024; plant noted as first in Mexico producing calcined-clay cement",
        "investment_type": "brownfield_expansion",
        "value": "55000000",
        "currency": "USD",
        "value_usd": "55000000",
        "fx_usd": "1",
        "fx_date": "2024-02-13",
        "year": "2024",
        "status": "active",
        "lat": "17.76",
        "lon": "-92.59",
        "geo_note": "Holcim Macuspana cement plant, Tabasco (company geography).",
        "evidence": "documented",
        "source_id": "holcim_mx_macuspana_20240213",
        "note": "Actor: Holcim México (Swiss Holcim) — allied. Company Spanish release. Distinct from Holcim Pacasmayo/Comacsa Peru, Guayaquil calcined clay, and Cemex Colombia.",
    },
    {
        "id": "holcim_macuspana_grind_55m_2024",
        "retrieved": "2026-10-01",
        "source_id": "holcim_mx_macuspana_20240213",
        "url": "https://www.holcim.com.mx/con-una-inversion-de-55-mdd-holcim-mexico-fortalece-su-presencia-en-tabasco-con-nueva-unidad-de",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Holcim México, líder en soluciones innovadoras y sostenibles para la construcción, ha anunciado una inversión estratégica de 55 millones de dólares para la construcción de un nuevo molino en su planta de cemento en Macuspana, Tabasco.",
        "note": "Opened Holcim México company Spanish page 13 Feb 2024.",
    },
    {
        "id": "holcim_mx_macuspana_20240213",
        "type": "company",
        "chicago": "Holcim México. “Con una inversión de 55 mdd, Holcim México fortalece su presencia en Tabasco con nueva unidad de molienda.” 13 February 2024.",
        "url": "https://www.holcim.com.mx/con-una-inversion-de-55-mdd-holcim-mexico-fortalece-su-presencia-en-tabasco-con-nueva-unidad-de",
        "annotation": "Company release on Macuspana grind unit USD 55m. Supports holcim_macuspana_grind_55m_2024.",
        "supports": ["holcim_macuspana_grind_55m_2024", "hunt_infra_building_materials"],
    },
)

# 4 energy/solar — PowerChina Intrepid/Mauriti Ceará R$1.8bn EPC
A(
    {
        "id": "powerchina_intrepid_mauriti_1p8bn_2023",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "PowerChina — Intrepid/Mauriti solar complex (Ceará)",
        "country": "Brazil",
        "asset": "May 2023 Reuters via Época Negócios: PowerChina–Pontoon partnership for Intrepid solar complex in Ceará, 425 MWp, EPC/construction investment R$ 1.8 billion; PowerChina takes ready-to-build asset and funds construction/operation. SolarQuarter 27 Sep 2025: Mauriti Solar Complex (425 MW) begins commercial operations after operating certificate; nine SPVs + 230 kV booster; BNDES/BNB green loans cited",
        "investment_type": "greenfield_plant",
        "value": "1800000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "-7.39",
        "lon": "-38.77",
        "geo_note": "Mauriti / Ceará solar complex (press geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "epoca_powerchina_intrepid_20230526",
        "note": "Actor: PowerChina (PRC SOE) — prc. UNVERIFIED proxy: Reuters/Época 26 May 2023 R$1.8bn EPC figure; ops confirmed SolarQuarter Sep 2025. Distinct from Guayepo III / Trina Sidón.",
    },
    {
        "id": "powerchina_intrepid_mauriti_1p8bn_2023",
        "retrieved": "2026-10-01",
        "source_id": "epoca_powerchina_intrepid_20230526",
        "url": "https://epocanegocios.globo.com/futuro-da-industria/noticia/2023/05/pontoon-e-powerchina-fecham-acordo-em-energia-solar-no-brasil.ghtml",
        "price_year": "2023",
        "evidence": "proxy",
        "quote": "A parceria estratégia se inicia com o complexo solar Intrepid, localizado no Ceará, com capacidade instalada de 425 megawatts-pico (MWp) e investimentos de 1,8 bilhão de reais na fase de engenharia, aquisições e construção (EPC, na sigla em inglês).",
        "note": "Opened Época Negócios / Reuters Portuguese 26 May 2023. Mark UNVERIFIED proxy for CAPEX; ops later confirmed.",
    },
    {
        "id": "epoca_powerchina_intrepid_20230526",
        "type": "trade_press",
        "chicago": "Reuters. “Pontoon e PowerChina fecham acordo em energia solar no Brasil.” Época Negócios, 26 May 2023.",
        "url": "https://epocanegocios.globo.com/futuro-da-industria/noticia/2023/05/pontoon-e-powerchina-fecham-acordo-em-energia-solar-no-brasil.ghtml",
        "annotation": "Reuters/Época on PowerChina Intrepid/Mauriti R$1.8bn EPC. Supports powerchina_intrepid_mauriti_1p8bn_2023.",
        "supports": ["powerchina_intrepid_mauriti_1p8bn_2023", "hunt_energy_solar"],
    },
)

# 5 energy/power_plants_grid — miss (Hitachi Brazil addl / Coca Codo O&M already)

# 6 resources/niobium — St George Araxá A$60m placement (Hancock)
A(
    {
        "id": "st_george_araxa_raise_aud60m_2026",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "St George Mining (Hancock Prospecting) — Araxá Nb-REE placement",
        "country": "Brazil",
        "asset": "17 Jun 2026 ASX: firm commitments to raise A$60 million (before costs) via two-tranche placement of 600 million shares at A$0.10; Hancock Prospecting commits A$20 million (200m shares) to ~10.5% holding; funds to advance Araxá rare-earths/niobium project feasibility and investment decision. Jul 2026 quarterly confirms placement completed",
        "investment_type": "equity_raise",
        "value": "60000000",
        "currency": "AUD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "Araxá Nb-REE project, Minas Gerais (company ASX geography).",
        "evidence": "documented",
        "source_id": "stgm_asx_aud60m_20260617",
        "note": "Actor: St George Mining (ASX:SGQ, Australia) with Hancock Prospecting (Australia) — allied. Company ASX release. Distinct from st_george_araxa_nb_2025 (Itafos acquisition USD 21m) and Worley advisory row.",
    },
    {
        "id": "st_george_araxa_raise_aud60m_2026",
        "retrieved": "2026-10-01",
        "source_id": "stgm_asx_aud60m_20260617",
        "url": "https://www.stgm.com.au/pdf/daec3170-d1c5-4743-b8f8-3c6c12f7dd90/Platform/ListPage/A60M-secured-for-Araxa-Rare-EarthsNiobium-Project.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "St George Mining Limited (ASX: SGQ) (“St George” or “the Company”) is pleased to announce it has received firm commitments to raise A$60 million (before costs) via a two-tranche institutional placement of 600 million new fully paid ordinary shares (“New Shares”) at an offer price of A$0.10 per New Share (“Placement”).",
        "note": "Opened St George Mining ASX PDF 17 Jun 2026.",
    },
    {
        "id": "stgm_asx_aud60m_20260617",
        "type": "company",
        "chicago": "St George Mining Limited. “St George Secures A$60 Million to Accelerate Development of the World-Class Rare Earths-Niobium Araxá Project.” ASX release, 17 June 2026.",
        "url": "https://www.stgm.com.au/pdf/daec3170-d1c5-4743-b8f8-3c6c12f7dd90/Platform/ListPage/A60M-secured-for-Araxa-Rare-EarthsNiobium-Project.pdf",
        "annotation": "ASX placement A$60m for Araxá Nb-REE. Supports st_george_araxa_raise_aud60m_2026.",
        "supports": ["st_george_araxa_raise_aud60m_2026", "hunt_fenb_araxa"],
    },
)

# 7 resources/balsa — Spain 5.08% of 2025 manufactures-of-balsa
A(
    {
        "id": "aima_ecuador_balsa_mfr_spain_2025",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "allied",
        "counterpart": "Ecuador manufactures-of-balsa exports — Spain destination share 2025",
        "country": "Ecuador",
        "asset": "AIMA via MAGAP: Ecuador 2025 manufactures-of-balsa exports USD 301.3 million (+38% vs 2024); Forbes Ecuador citing AIMA attributes 5.08% destination share to Spain → implied ~USD 15.31 million Spain-bound manufactures (UNVERIFIED destination-share proxy). Completes China/US/Spain top-three set from same Forbes/AIMA release",
        "investment_type": "trade_flow",
        "value": "15306040",
        "currency": "USD",
        "value_usd": "15306040",
        "fx_usd": "1",
        "fx_date": "2025-12-31",
        "year": "2025",
        "status": "active",
        "lat": "-2.17",
        "lon": "-79.92",
        "geo_note": "Ecuador balsa manufacturing regions (Guayas/Los Ríos/Santo Domingo; national trade pin).",
        "evidence": "proxy",
        "source_id": "forbes_ec_aima_balsa_spain_20260508",
        "note": "Actor: Spain destination (EU/allied buyer) — allied. UNVERIFIED proxy: Forbes Ecuador 8 May 2026 citing AIMA 5.08% share applied to MAGAP/AIMA USD 301.3m total. Paired with aima_ecuador_balsa_mfr_china_2025 and aima_ecuador_balsa_mfr_us_2025.",
    },
    {
        "id": "aima_ecuador_balsa_mfr_spain_2025",
        "retrieved": "2026-10-01",
        "source_id": "forbes_ec_aima_balsa_spain_20260508",
        "url": "https://www.forbes.com.ec/negocios/la-balsa-ecuatoriana-conquista-industria-eolica-mundial-n90920",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "China es el principal comprador de estos derivados de balsa, con el 72,51 % de participación de mercado. A continuación asoman Estados Unidos (9,95 %) y España (5,08 %).",
        "note": "Opened Forbes Ecuador 8 May 2026. Spain share applied to MAGAP/AIMA total USD 301.3m. Mark UNVERIFIED proxy.",
    },
    {
        "id": "forbes_ec_aima_balsa_spain_20260508",
        "type": "trade_press",
        "chicago": "Villanueva, Julissa. “La balsa ecuatoriana conquista la industria eólica mundial.” Forbes Ecuador, 8 May 2026.",
        "url": "https://www.forbes.com.ec/negocios/la-balsa-ecuatoriana-conquista-industria-eolica-mundial-n90920",
        "annotation": "Forbes Ecuador citing AIMA destination shares incl. Spain 5.08%. Supports aima_ecuador_balsa_mfr_spain_2025.",
        "supports": ["aima_ecuador_balsa_mfr_spain_2025", "hunt_res_balsa"],
    },
)

# 8 infrastructure/rail — PowerChina Chancay–Sierra Central USD 420m
A(
    {
        "id": "powerchina_chancay_sierra_rail_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "prc",
        "counterpart": "PowerChina — Ferrocarril Chancay–Sierra Central",
        "country": "Peru",
        "asset": "Jan 2026 Spanish press (El Comercio 14 Jan; Revista Economía 20 Jan): Power Construction Corporation of China (PowerChina) awarded construction of ~120 km Chancay–Sierra Central railway linking Megapuerto de Chancay to central highland mining corridor; estimated investment USD 420 million; ~36-month build; ops targeted 2028; freight focus copper/lithium. UNVERIFIED press adjudication — no opened MTC/PROINVERSIÓN award decree in this cycle",
        "investment_type": "greenfield_rail",
        "value": "420000000",
        "currency": "USD",
        "value_usd": "420000000",
        "fx_usd": "1",
        "fx_date": "2026-01-14",
        "year": "2026",
        "status": "active",
        "lat": "-11.57",
        "lon": "-77.27",
        "geo_note": "Chancay port corridor toward sierra central (press geography; approximate pin at Chancay).",
        "evidence": "proxy",
        "source_id": "elcomercio_powerchina_chancay_rail_20260114",
        "note": "Actor: PowerChina (PRC SOE) — prc. UNVERIFIED proxy: El Comercio / Revista Economía Spanish press Jan 2026. Distinct from cosco_chancay_port_2024 (port ownership) and Siemens EFE ETCS.",
    },
    {
        "id": "powerchina_chancay_sierra_rail_2026",
        "retrieved": "2026-10-01",
        "source_id": "elcomercio_powerchina_chancay_rail_20260114",
        "url": "https://elcomercio.pe/lima/sucesos/dan-luz-verde-a-tren-que-unira-el-puerto-de-chancay-con-zona-central-del-peru-de-que-trata-y-que-impacto-tendra-noticia/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "En las últimas semanas del 2025, la compañía Power Construction Corporation of China (PowerChina) se adjudicó la construcción del tren que conectará el puerto de Chancay con la sierra central. … el cual contempla 120 km de extensión y una inversión de 420 millones de dólares.",
        "note": "Opened El Comercio Spanish 14 Jan 2026. Mark UNVERIFIED proxy (press adjudication).",
    },
    {
        "id": "elcomercio_powerchina_chancay_rail_20260114",
        "type": "trade_press",
        "chicago": "Medrano Marin, Hernán. “Dan luz verde a tren que unirá el puerto de Chancay con zona central del Perú.” El Comercio (Peru), 14 January 2026.",
        "url": "https://elcomercio.pe/lima/sucesos/dan-luz-verde-a-tren-que-unira-el-puerto-de-chancay-con-zona-central-del-peru-de-que-trata-y-que-impacto-tendra-noticia/",
        "annotation": "Spanish press on PowerChina Chancay–Sierra Central rail USD 420m. Supports powerchina_chancay_sierra_rail_2026.",
        "supports": ["powerchina_chancay_sierra_rail_2026", "hunt_latam_rail_telecom"],
    },
)

# 9–14 wind, lithium, copper, graphite, bridges_roads, other_renewables — miss
# (thick or already logged this session)

# 15 infrastructure/port_cranes — miss (SSA Guaymas / Paracas / Suape / Tecon already)

# 16 infrastructure/port_ownership — Hutchison ICAVE Veracruz Fase II MXN 4.5bn
A(
    {
        "id": "hutchison_icave_fase2_4500m_mxn_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "other",
        "counterpart": "Hutchison Ports ICAVE — Veracruz TEC Phase II expansion",
        "country": "Mexico",
        "asset": "Jan 2026: Hutchison Ports ICAVE formalizes ASIPONA Veracruz agreement (signed 19 Dec 2025) for Phase II of Specialized Container Terminal — new 350 m berth + 31 ha yard to 1,050 m quay / 72.4 ha; announced investment > MXN 4,500 million for equipment/tech incl. 3 STS + 11 electric RTG, CFS, access control; design capacity to 2.4m TEU/y. UNVERIFIED press figures",
        "investment_type": "brownfield_expansion",
        "value": "4500000000",
        "currency": "MXN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "19.2",
        "lon": "-96.13",
        "geo_note": "ICAVE outer harbor Veracruz (terminal geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "razon_icave_fase2_20260126",
        "note": "Actor: Hutchison Ports ICAVE (CK Hutchison / Hong Kong) — other (matches hutchison_eit_ensenada_2022 side). UNVERIFIED proxy: La Razón / PTC Spanish Jan 2026. Crane package also noted but logged under port_ownership as terminal expansion.",
    },
    {
        "id": "hutchison_icave_fase2_4500m_mxn_2026",
        "retrieved": "2026-10-01",
        "source_id": "razon_icave_fase2_20260126",
        "url": "https://www.razon.com.mx/negocios/2026/01/26/hutchison-ports-icave-arranca-fase-ii-en-veracruz-con-inversion-superior-a-4500-millones-de-pesos/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Como parte de este proyecto, Hutchison Ports ICAVE anunció una inversión superior a los 4,500 millones de pesos, destinada a incrementar la eficiencia operativa y la sostenibilidad de sus operaciones en el Golfo de México",
        "note": "Opened La Razón Spanish 26 Jan 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "razon_icave_fase2_20260126",
        "type": "trade_press",
        "chicago": "La Razón. “Hutchison Ports ICAVE arranca Fase II en Veracruz con inversión superior a 4,500 millones de pesos.” 26 January 2026.",
        "url": "https://www.razon.com.mx/negocios/2026/01/26/hutchison-ports-icave-arranca-fase-ii-en-veracruz-con-inversion-superior-a-4500-millones-de-pesos/",
        "annotation": "Press on ICAVE Veracruz Phase II >MXN 4.5bn. Supports hutchison_icave_fase2_4500m_mxn_2026.",
        "supports": ["hutchison_icave_fase2_4500m_mxn_2026", "hunt_infra_port_ownership"],
    },
)

# 17 resources/water — miss (Cox Rosarito / Sacyr Coquimbo already)
# 18 infrastructure/engineering_epc — miss (Worley Diablillos / PowerChina UFN3 already)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {b["id"]: i for i, b in enumerate(bib) if isinstance(b, dict) and "id" in b}

    added = []
    updated = []
    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        if rid in by_id:
            rows[by_id[rid]].update({k: v for k, v in row.items() if v != ""})
            updated.append(rid)
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

    hunt_updates = {
        "hunt_energy_fission_smr": "Cycle 36: equal budget; Meitner/Brazil microreactor/Nuclearis already (miss).",
        "hunt_res_nickel": "Cycle 36: logged brazilian_nickel_pnp_capex_1p4bn_2026 (USD 1.4bn CAPEX).",
        "hunt_infra_building_materials": "Cycle 36: logged holcim_macuspana_grind_55m_2024.",
        "hunt_energy_solar": "Cycle 36: logged powerchina_intrepid_mauriti_1p8bn_2023.",
        "hunt_br_power_equip": "Cycle 36: equal budget; Hitachi addl / Coca Codo already (miss).",
        "hunt_fenb_araxa": "Cycle 36: logged st_george_araxa_raise_aud60m_2026 (A$60m).",
        "hunt_res_balsa": "Cycle 36: logged aima_ecuador_balsa_mfr_spain_2025.",
        "hunt_latam_rail_telecom": "Cycle 36: logged powerchina_chancay_sierra_rail_2026 (USD 420m proxy).",
        "hunt_energy_wind": "Cycle 36: equal budget; Goldwind FINAME / Vestas Esquina already (miss).",
        "hunt_res_lithium": "Cycle 36: equal budget; Galan HMW / Zijin RIGI already (miss).",
        "hunt_res_copper": "Cycle 36: equal budget; Las Bambas / El Abra already (miss).",
        "hunt_res_graphite": "Cycle 36: equal budget; Graphcoa Jordânia DFS already (miss).",
        "hunt_infra_bridges_roads": "Cycle 36: equal budget; Sacyr Ruta 57 / Sierra T4 already (miss).",
        "hunt_energy_other_renewables": "Cycle 36: equal budget; Jinko BESS Amanecer already (miss).",
        "hunt_infra_port_cranes": "Cycle 36: equal budget; Guaymas/Paracas/Suape already (miss).",
        "hunt_infra_port_ownership": "Cycle 36: logged hutchison_icave_fase2_4500m_mxn_2026.",
        "hunt_res_water": "Cycle 36: equal budget; Cox Rosarito / Sacyr Coquimbo already (miss).",
        "hunt_infra_engineering_epc": "Cycle 36: equal budget; Worley Diablillos / UFN3 already (miss).",
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
    print("Cycle 36 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 36 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
