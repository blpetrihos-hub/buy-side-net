#!/usr/bin/env python3
"""Cycle 31 hunt: shuffle_seed=20261031; equal budget across 18 subcategories."""
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


# seed 20261031 order:
# other_renewables, fission_smr, solar, niobium, engineering_epc, building_materials,
# wind, rail, graphite, power_plants_grid, balsa, bridges_roads, port_ownership,
# copper, port_cranes, water, lithium, nickel

# 1 energy/other_renewables — Lindsayca Borinquen I electromechanical award
A(
    {
        "id": "lindsayca_borinquen_i_em_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "Lindsayca Integrated Energy (Houston) — ICE Borinquen I geothermal EM package",
        "country": "Costa Rica",
        "asset": "4 Jun 2026 ICE award of LPI 2024LI-000001-PROV for design/supply/supervision/testing/commissioning of electromechanical generation equipment for Proyecto Geotérmico Borinquen I (55 MW, Liberia / Rincón de la Vieja, Guanacaste) to Lindsayca Integrated Energy S.A. (Houston HQ; Venezuelan-origin EPC). ICE-communicated operation amount ~USD 100 million (UNVERIFIED press paraphrase of ICE release); contract signing targeted H2 2026; machine-house works start ~Jul 2027; plant COD early 2030. Award under CGR appeal by Cox Energy EPC / Cox ABG (CGR-REAP-2026004334) as of late Jun 2026 — not final until appeal resolved. Project financed in part via JICA geothermal loan (Ley 9254)",
        "investment_type": "equipment_supply",
        "value": "100000000",
        "currency": "USD",
        "value_usd": "100000000",
        "fx_usd": "1",
        "fx_date": "2026-06-04",
        "year": "2026",
        "status": "active",
        "lat": "10.83",
        "lon": "-85.37",
        "geo_note": "Borinquen I geothermal site, Liberia / Rincón de la Vieja, Guanacaste (ICE project geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "semanario_borinquen_lindsayca_20260626",
        "note": "Actor: Lindsayca Integrated Energy S.A. (Houston, Texas) — us. Award winner + ~USD 100m from Semanario Universidad (UCR) citing ICE 10 Jun comunicado and CGR appeal expediente; ICE primary URL returned 404 at retrieve. UNVERIFIED proxy for exact USD figure and pending CGR appeal. Distinct from ormat_dominica_geothermal_cod_2026.",
    },
    {
        "id": "lindsayca_borinquen_i_em_2026",
        "retrieved": "2026-10-01",
        "source_id": "semanario_borinquen_lindsayca_20260626",
        "url": "https://semanariouniversidad.com/pais/empresa-espanola-apela-ante-contraloria-millonario-contrato-del-ice-para-planta-geotermica-borinquen-i/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "El equipamiento electromecánico para el Proyecto Geotérmico Borinquen l fue adjudicado el 4 de junio a la empresa Lindsayca Integrated Energy S.A., con sede en Houston, Texas. … se informó que el monto de la operación era cercano a los $100 millones.",
        "note": "Opened Semanario Universidad (UCR) Spanish investigation 26 Jun 2026 citing ICE award and CGR appeal file. Value and winner corroborated; ICE HTML press URL 404 at retrieve.",
    },
    {
        "id": "semanario_borinquen_lindsayca_20260626",
        "type": "press",
        "chicago": "Pomareda García, Fabiola. “Empresa española apela ante Contraloría millonario contrato del ICE para planta geotérmica Borinquen I.” Semanario Universidad (Universidad de Costa Rica), 26 June 2026.",
        "url": "https://semanariouniversidad.com/pais/empresa-espanola-apela-ante-contraloria-millonario-contrato-del-ice-para-planta-geotermica-borinquen-i/",
        "annotation": "UCR Spanish press naming Lindsayca Houston as Borinquen I EM awardee and ~USD 100m ICE figure, with CGR appeal context. Supports lindsayca_borinquen_i_em_2026 (proxy).",
        "supports": ["lindsayca_borinquen_i_em_2026", "hunt_energy_other_renewables"],
    },
)

# 2 energy/fission_smr — miss (Meitner ACR-300 / CAREM / Nuclearis N1 / RMB already)

# 3 energy/solar — Trina Pillancó Biobío
A(
    {
        "id": "trina_pillanco_biobio_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Trina Solar — Parque Fotovoltaico Pillancó (Biobío)",
        "country": "Chile",
        "asset": "27 Mar 2026: Comisión de Evaluación Región del Biobío unanimously approves DIA for Parque Fotovoltaico Pillancó (Trina Solar) in comunas Los Ángeles and Cabrero; up to 208 MW PV + lithium-ion BESS + HV evacuation to existing S/E El Rosal; approx USD 236 million investment; construction start targeted Jun 2026; ~32.5-year operating life; ~422 GWh/year at 28% plant factor (SEA/DIA materials)",
        "investment_type": "greenfield",
        "value": "236000000",
        "currency": "USD",
        "value_usd": "236000000",
        "fx_usd": "1",
        "fx_date": "2026-03-27",
        "year": "2026",
        "status": "active",
        "lat": "-37.15",
        "lon": "-72.35",
        "geo_note": "Pillancó sector, Cabrero / Los Ángeles, Región del Biobío (SEA notice; approximate generation-area pin).",
        "evidence": "documented",
        "source_id": "sea_pillanco_aprobacion_20260401",
        "note": "Actor: Trina Solar (PRC) — prc. Official SEA Chile Spanish notice 1 Apr 2026 stating USD 236m / ≤208 MW. Distinct from trina_cemig_sim_brazil_2023 and trina_atlas_copiapo_bess_2025.",
    },
    {
        "id": "trina_pillanco_biobio_2026",
        "retrieved": "2026-10-01",
        "source_id": "sea_pillanco_aprobacion_20260401",
        "url": "https://www.sea.gob.cl/noticias/comision-de-evaluacion-del-biobio-aprueba-proyecto-dia-parque-fotovoltaico-pillanco",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "La iniciativa, que se emplazará en las comunas de Los Ángeles y Cabrero, contempla la construcción y operación de un parque fotovoltaico con una potencia máxima de hasta 208 MW. El proyecto considera una inversión aproximada de USD 236 millones.",
        "note": "Opened SEA Chile official Spanish approval notice 1 Apr 2026.",
    },
    {
        "id": "sea_pillanco_aprobacion_20260401",
        "type": "government",
        "chicago": "Servicio de Evaluación Ambiental (Chile). “Comisión de Evaluación del Biobío aprueba proyecto DIA ‘Parque Fotovoltaico Pillancó’.” 1 April 2026.",
        "url": "https://www.sea.gob.cl/noticias/comision-de-evaluacion-del-biobio-aprueba-proyecto-dia-parque-fotovoltaico-pillanco",
        "annotation": "Official SEA Biobío DIA approval stating ≤208 MW and ~USD 236m for Trina Pillancó. Supports trina_pillanco_biobio_2026.",
        "supports": ["trina_pillanco_biobio_2026", "hunt_energy_solar"],
    },
)

# 4 resources/niobium — miss (CBMM Araxá R$13bn plan logged C30)
# 5 infrastructure/engineering_epc — miss (PowerChina UFN-III / Bechtel–EIMISA / Worley Diablillos already)
# 6 infrastructure/building_materials — miss (Holcim Pacasmayo / Cemex Colombia / Guayaquil clay already)

# 7 energy/wind — IFC / PCR / Vestas Olavarría
A(
    {
        "id": "ifc_pcr_olavarria_wind_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "IFC (lead) + PCR / ArcelorMittal Acindar — Olavarría Wind Farm (Vestas turbines)",
        "country": "Argentina",
        "asset": "6 Mar 2026: IFC provides financing to PCR for Olavarría Wind Farm (Buenos Aires Province) co-developed with Acindar (ArcelorMittal); total project cost USD 275 million including 29 Vestas turbines (185.6 MW), 25 km line to Olavarría substation, and capacitor upgrades at Olavarría/Ezeiza; first renewable under Argentina RIGI with privately financed transmission into SADI; IFC lead arranger of USD 110m senior corporate loan (expandable to USD 140m) to GEAR S.A. affiliate (USD 30m IFC A-loan + USD 80m B/parallel). Vestas company news (12 Sep 2025) separately confirms 186 MW V162-6.4 MW Argentina order with 25-year AOM5000 (customer undisclosed on Vestas page; Spanish trade press links to PCR/Acindar Olavarría)",
        "investment_type": "greenfield",
        "value": "275000000",
        "currency": "USD",
        "value_usd": "275000000",
        "fx_usd": "1",
        "fx_date": "2026-03-06",
        "year": "2026",
        "status": "active",
        "lat": "-36.9",
        "lon": "-60.3",
        "geo_note": "Olavarría wind farm ~24 km from city, Buenos Aires Province (IFC/PCR geography; approximate pin).",
        "evidence": "documented",
        "source_id": "ifc_olavarria_wind_20260306",
        "note": "Actors: IFC (WBG) lead finance + Vestas (Denmark) turbines + ArcelorMittal Acindar offtake — allied; PCR Argentine sponsor. IFC English press 6 Mar 2026 states USD 275m total cost. Distinct from prior Goldwind/Envision Argentina wind rows.",
    },
    {
        "id": "ifc_pcr_olavarria_wind_2026",
        "retrieved": "2026-10-01",
        "source_id": "ifc_olavarria_wind_20260306",
        "url": "https://www.ifc.org/en/pressroom/2026/ifc-supports-landmark-wind-power-and-transmission-project-to-boost-clean-energy-su",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The investment represents a total cost of US$275 million and includes the installation of 29 wind turbines supplied by Vestas, with a total installed capacity of 185.6 megawatts.",
        "note": "Opened IFC English press 6 Mar 2026. Vestas 12 Sep 2025 order notice corroborates 186 MW Argentina turbine package.",
    },
    {
        "id": "ifc_olavarria_wind_20260306",
        "type": "ifi",
        "chicago": "International Finance Corporation. “IFC supports landmark Wind Power and Transmission Project to boost clean energy supply, jobs, and private investment in Argentina.” 6 March 2026.",
        "url": "https://www.ifc.org/en/pressroom/2026/ifc-supports-landmark-wind-power-and-transmission-project-to-boost-clean-energy-su",
        "annotation": "IFC primary on USD 275m Olavarría wind + transmission package with Vestas turbines. Supports ifc_pcr_olavarria_wind_2026.",
        "supports": ["ifc_pcr_olavarria_wind_2026", "hunt_energy_wind"],
    },
)

# 8 infrastructure/rail — miss (Siemens–Sonda ETCS / CRRC Pachuca / Alstom México DMU already)
# 9 resources/graphite — miss (Graphcoa Boa Sorte/Jordânia / South Star Santa Cruz already)
# 10 energy/power_plants_grid — miss (Hitachi Dosquebradas already; avoid over-invest)
# 11 resources/balsa — miss (WITS/AIMA pairs already)

# 12 infrastructure/bridges_roads — Sacyr Ruta 57 best economic offer
A(
    {
        "id": "sacyr_ruta57_best_offer_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "allied",
        "counterpart": "Sacyr Concesiones Chile — Segunda Concesión Ruta 57 Santiago–Colina–Los Andes (best economic offer)",
        "country": "Chile",
        "asset": "4 Sep 2026 MOP economic-bid opening: Sacyr Concesiones Chile SPA presented the best economic offer for Segunda Concesión Ruta 57 Santiago–Colina–Los Andes among three technically acceptable bidders (also Vías Chile SA; Consorcio Nueva Autopista Los Libertadores). Referential investment UF 23,153,000; ~110.4 km scope (Ruta 57 79.8 km + G-71 16.7 km + new 9.3 km link to Ruta 5 + 4.6 km Los Andes dry-port link); third lanes first 24 km; new parallel Chacabuco tunnel; new bridges/cycleways/pedestrian bridges. New works start ~2031; full service ~2035; current concession ends 8 Jan 2027. Best-offer stage — formal award decree not yet cited here",
        "investment_type": "ppp_concession",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-33.1",
        "lon": "-70.7",
        "geo_note": "Ruta 57 Santiago–Colina–Los Andes corridor (MOP notice; approximate mid-corridor pin).",
        "evidence": "documented",
        "source_id": "mop_ruta57_sacyr_best_20260904",
        "note": "Actor: Sacyr Concesiones Chile (Spanish Sacyr) — allied. Official MOP Spanish notice 4 Sep 2026. UF 23.153.000 stated; USD not entered (no official FX on page). Preferred/best-offer milestone pending award decree. Distinct from crcc_talca_chillan_ruta5_2021 and ohla_panama_panamericana_este_2025.",
    },
    {
        "id": "sacyr_ruta57_best_offer_2026",
        "retrieved": "2026-10-01",
        "source_id": "mop_ruta57_sacyr_best_20260904",
        "url": "https://www.mop.gob.cl/sacyr-concesiones-chile-spa-presento-la-mejor-oferta-para-el-desarrollo-del-proyecto-segunda-concesion-ruta-57-santiago-colina-los-andes/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Sacyr Concesiones Chile SPA presentó la mejor oferta, superando a los otros licitantes que presentaron ofertas técnicas aceptables, Vías Chile SA y el Consorcio Nueva Autopista Los Libertadores. … iniciativa que contempla una inversión estimada de UF 23.153.000.",
        "note": "Opened MOP Chile Spanish economic-opening notice 4 Sep 2026.",
    },
    {
        "id": "mop_ruta57_sacyr_best_20260904",
        "type": "government",
        "chicago": "Ministerio de Obras Públicas (Chile). “Sacyr Concesiones Chile SPA presentó la mejor oferta para el desarrollo del proyecto ‘Segunda Concesión Ruta 57 Santiago–Colina–Los Andes’.” 4 September 2026.",
        "url": "https://www.mop.gob.cl/sacyr-concesiones-chile-spa-presento-la-mejor-oferta-para-el-desarrollo-del-proyecto-segunda-concesion-ruta-57-santiago-colina-los-andes/",
        "annotation": "Official MOP best-economic-offer notice for Ruta 57 second concession (UF 23.153.000). Supports sacyr_ruta57_best_offer_2026.",
        "supports": ["sacyr_ruta57_best_offer_2026", "hunt_infra_bridges_roads"],
    },
)

# 13 infrastructure/port_ownership — miss (Jinzhao Marcona / HGT Aracruz already)

# 14 resources/copper — Freeport El Abra USD 7.5bn EIA (value fill on existing id) + BHP Escondida new concentrator
A(
    {
        "id": "fcx_el_abra_mill_chile_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "us",
        "counterpart": "Freeport-McMoRan (51%) / Codelco (49%) — El Abra Continuidad Operacional + concentrator EIA",
        "country": "Chile",
        "asset": "18 Mar 2026: Minera El Abra (Freeport-McMoRan Chile subsidiary; Freeport 51% / Codelco 49%) submits Continuidad Operacional project to SEIA Antofagasta — preliminary investment ~USD 7.5 billion including new concentrator, desalination + water conveyance, thickened-tailings deposit, mine expansion, and leach continuity; aims to extend mine life ~40 years and add >300 ktpa Cu (~700 Mlb/y) with expanded ops targeted ~2033 if approved. SEA evaluation later suspended to 17 Dec 2026 pending Adenda (administrative pause, not rejection)",
        "investment_type": "permitting",
        "value": "7500000000",
        "currency": "USD",
        "value_usd": "7500000000",
        "fx_usd": "1",
        "fx_date": "2026-03-18",
        "year": "2026",
        "status": "active",
        "lat": "-21.9",
        "lon": "-68.8",
        "geo_note": "Minera El Abra, El Loa / Antofagasta Region (company El Abra release; approximate pin).",
        "evidence": "documented",
        "source_id": "elabra_continuidad_eia_20260318",
        "note": "Actor: Freeport-McMoRan (U.S.) majority — us. Company El Abra Spanish release 18 Mar 2026 stating ~USD 7.5bn. Cycle 31 value/source refresh of prior mill-presence stub. Distinct from fcx_cerro_verde_meia2_2100m_2026.",
    },
    {
        "id": "fcx_el_abra_mill_chile_2026",
        "retrieved": "2026-10-01",
        "source_id": "elabra_continuidad_eia_20260318",
        "url": "https://www.elabra.cl/minera-el-abra-filial-de-freeport-mcmoran-ingresa-proyecto-de-continuidad-operacional-para-evaluacion-ambiental/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "La inversión preliminar estimada del proyecto asciende aproximadamente a US$7.500 millones e incluye el desarrollo de una planta concentradora, una planta desalinizadora y un sistema de impulsión de agua, un depósito de relaves espesados, la expansión de la mina y la continuidad de las operaciones de lixiviación.",
        "note": "Opened Minera El Abra / Freeport Chile company Spanish release (dated 18 Mar 2026 on page).",
    },
    {
        "id": "elabra_continuidad_eia_20260318",
        "type": "company",
        "chicago": "Minera El Abra / Freeport-McMoRan Chile. “Minera El Abra, filial de Freeport-McMoRan ingresa Proyecto de Continuidad Operacional para evaluación ambiental.” 18 March 2026.",
        "url": "https://www.elabra.cl/minera-el-abra-filial-de-freeport-mcmoran-ingresa-proyecto-de-continuidad-operacional-para-evaluacion-ambiental/",
        "annotation": "Company primary stating ~USD 7.5bn El Abra Continuidad Operacional SEIA filing. Supports fcx_el_abra_mill_chile_2026.",
        "supports": ["fcx_el_abra_mill_chile_2026", "hunt_res_copper"],
    },
)

A(
    {
        "id": "bhp_escondida_new_concentrator_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "allied",
        "counterpart": "BHP — Escondida New Concentrator (SEIA filing)",
        "country": "Chile",
        "asset": "Mar 2026: BHP submits Escondida New Concentrator to Chile SEIA to replace ageing Los Colorados plant capacity; investment estimated US$4.4–5.9 billion; target throughput ~50 Mt/y (up to ~57.5 Mt/y avg) via SABC circuit + HydroFloat CPF; maintains ~460 ktpd sulphide processing; first production 2031–2032 if approved; includes 25.7 km 220 kV double-circuit line. BHP.com article returned HTTP 403 at retrieve — figures from International Mining report of BHP filing (UNVERIFIED proxy vs company HTML)",
        "investment_type": "permitting",
        "value": "4400000000",
        "currency": "USD",
        "value_usd": "4400000000",
        "fx_usd": "1",
        "fx_date": "2026-03-17",
        "year": "2026",
        "status": "active",
        "lat": "-24.27",
        "lon": "-69.07",
        "geo_note": "Escondida mine, Antofagasta Region (project geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "immining_escondida_concentrator_20260317",
        "note": "Actor: BHP (Australia/UK) — allied. Value stored at stated range floor USD 4.4bn (upper USD 5.9bn in source). UNVERIFIED proxy because bhp.com primary returned 403 at retrieve; International Mining paraphrases BHP SEIA filing. Distinct from teck_quebrada_blanca_chile and fcx_el_abra_mill_chile_2026.",
    },
    {
        "id": "bhp_escondida_new_concentrator_2026",
        "retrieved": "2026-10-01",
        "source_id": "immining_escondida_concentrator_20260317",
        "url": "https://im-mining.com/2026/03/17/bhp-submits-eia-application-for-new-escondida-concentrator/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "The new concentrator will replace the production capacity of the historic Los Colorados plant, which is nearing the end of its operational life and whose investment is estimated to range between US$4.4 billion and US$5.9 billion.",
        "note": "Opened International Mining 17 Mar 2026 report of BHP SEIA filing. Company HTML blocked (403) at retrieve.",
    },
    {
        "id": "immining_escondida_concentrator_20260317",
        "type": "press",
        "chicago": "International Mining. “BHP submits EIA application for New Escondida Concentrator.” 17 March 2026.",
        "url": "https://im-mining.com/2026/03/17/bhp-submits-eia-application-for-new-escondida-concentrator/",
        "annotation": "Trade press paraphrase of BHP Escondida New Concentrator SEIA filing (USD 4.4–5.9bn). Supports bhp_escondida_new_concentrator_2026 (proxy).",
        "supports": ["bhp_escondida_new_concentrator_2026", "hunt_res_copper"],
    },
)

# 15 infrastructure/port_cranes — Konecranes YILPORT Acajutla 18 E-Hybrid RTGs
A(
    {
        "id": "konecranes_yilport_acajutla_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Konecranes — 18 E-Hybrid RTGs for YILPORT Acajutla UPDP (El Salvador)",
        "country": "El Salvador",
        "asset": "Q2 2026 order (Konecranes release 3 Jul 2026): YILPORT Holding orders 53 E-Hybrid RTGs from Konecranes globally, including 18 E-Hybrid RTGs for Acajutla Port / UPDP Terminal in El Salvador; deliveries in batches over ~2 years. LatAm tranche only mapped here (Portugal/Ghana legs out of region / not mapped)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "13.59",
        "lon": "-89.83",
        "geo_note": "Puerto de Acajutla UPDP terminal, El Salvador (Konecranes/YILPORT release).",
        "evidence": "documented",
        "source_id": "konecranes_yilport_rtg_20260703",
        "note": "Actor: Konecranes (Finland) supplier — allied; YILPORT (Turkish global operator) customer. Company English press 3 Jul 2026. No USD disclosed for Acajutla tranche. Distinct from konecranes_cartagena_rtg_2025 and konecranes_super_terminais_manaus_2025. Portugal/Ghana portions of same order not mapped (out of LatAm).",
    },
    {
        "id": "konecranes_yilport_acajutla_2026",
        "retrieved": "2026-10-01",
        "source_id": "konecranes_yilport_rtg_20260703",
        "url": "https://www.konecranes.com/press-releases/konecranes-supports-yilports-global-investment-momentum-with-major-order-for-53-automated-and-manual-e-hybrid",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The order includes: … 18 E‑Hybrid RTGs for Acajutla Port in El Salvador …",
        "note": "Opened Konecranes English corporate press 3 Jul 2026.",
    },
    {
        "id": "konecranes_yilport_rtg_20260703",
        "type": "company",
        "chicago": "Konecranes. “Konecranes supports YILPORT’s global investment momentum with major order for 53 automated and manual E-Hybrid RTG cranes across three continents.” 3 July 2026.",
        "url": "https://www.konecranes.com/press-releases/konecranes-supports-yilports-global-investment-momentum-with-major-order-for-53-automated-and-manual-e-hybrid",
        "annotation": "Company primary on 18 E-Hybrid RTGs for YILPORT Acajutla (El Salvador). Supports konecranes_yilport_acajutla_2026.",
        "supports": ["konecranes_yilport_acajutla_2026", "hunt_infra_port_cranes"],
    },
)

# 16 resources/water — Acciona Yanacocha WTP commissioning
A(
    {
        "id": "acciona_yanacocha_wtp_commission_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "ACCIONA — Yanacocha East/West acid-water treatment plant commissioning (Newmont)",
        "country": "Peru",
        "asset": "ACCIONA selected by Newmont for 19-month commissioning services on East Plant (~2,700 m³/h) and West Plant (~3,000 m³/h) acid-water treatment facilities at Yanacocha gold mine (Cajamarca) — commissioning management system, construction/start-up coordination, testing oversight, vendor coordination, and initial operations support. Bechtel delivering integrated EPC for the two plants (separate actor; CAPEX not disclosed on Acciona page)",
        "investment_type": "services_contract",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-6.98",
        "lon": "-78.52",
        "geo_note": "Yanacocha mine water treatment plants, Cajamarca Region, Peru (Acciona/Newmont geography; approximate pin).",
        "evidence": "documented",
        "source_id": "acciona_yanacocha_commission_2026",
        "note": "Actor: ACCIONA (Spain) — allied; client Newmont (U.S.). Company English updates page; no contract USD disclosed. Distinct from acciona_collahuasi_desal_chile and bechtel_qb2_desal_chile.",
    },
    {
        "id": "acciona_yanacocha_wtp_commission_2026",
        "retrieved": "2026-10-01",
        "source_id": "acciona_yanacocha_commission_2026",
        "url": "https://www.acciona.com/updates/articles/acciona-commission-two-water-treatment-plants-part-yanacocha-mining-project",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "ACCIONA has been selected by Newmont to provide commissioning services for the East Plant and West Plant treatment facilities at the Yanacocha mine in Peru. The 19-month contract covers the coordination and supervision of both facilities, as well as the associated auxiliary systems.",
        "note": "Opened ACCIONA English company updates page.",
    },
    {
        "id": "acciona_yanacocha_commission_2026",
        "type": "company",
        "chicago": "ACCIONA. “ACCIONA to commission two water treatment plants as part of the Yanacocha mining project.” n.d.",
        "url": "https://www.acciona.com/updates/articles/acciona-commission-two-water-treatment-plants-part-yanacocha-mining-project",
        "annotation": "Company primary on Newmont Yanacocha East/West WTP commissioning award. Supports acciona_yanacocha_wtp_commission_2026.",
        "supports": ["acciona_yanacocha_wtp_commission_2026", "hunt_res_water"],
    },
)

# 17 resources/lithium — Rio Tinto Fénix Fase 1B RIGI
A(
    {
        "id": "rio_tinto_fenix_1b_rigi_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "Rio Tinto / Minera del Altiplano Sucursal Dedicada — Fénix Expansión Fase 1B RIGI",
        "country": "Argentina",
        "asset": "Resolución ME 431/2026 (Boletín Oficial 6 Apr 2026): approves RIGI adhesion for Proyecto Único “Expansión Fase 1B” by Minera del Altiplano S.A. Sucursal Dedicada (Rio Tinto Fénix complex, Salar del Hombre Muerto, Catamarca) — +9,500 tpa lithium carbonate capacity (28,500 → 38,000 tpa); declared computable investment USD 251,321,494; construction Jul 2024–Nov 2026; ops start ~Jul 2026; new selective-adsorption + carbonate plants, wells, ponds, pipelines, and Olacapato gas compressor (Salta). RIGI benefits apply only to incremental Fase 1B production",
        "investment_type": "brownfield_expansion",
        "value": "251321494",
        "currency": "USD",
        "value_usd": "251321494",
        "fx_usd": "1",
        "fx_date": "2026-03-25",
        "year": "2026",
        "status": "active",
        "lat": "-25.42",
        "lon": "-67.07",
        "geo_note": "Fénix / Salar del Hombre Muerto, Catamarca (Resolución 431/2026 geography; approximate pin).",
        "evidence": "documented",
        "source_id": "me_res_431_2026_fenix_rigi",
        "note": "Actor: Rio Tinto (UK/Australia) via Minera del Altiplano — allied. Official Boletín Oficial Resolución 431/2026 states USD 251,321,494 (Caputo X/press ~USD 530m figures are broader plan — not used). Distinct from rio_tinto_rincon_financing_2026 and posco_sal_de_oro_ii_rigi_2026.",
    },
    {
        "id": "rio_tinto_fenix_1b_rigi_2026",
        "retrieved": "2026-10-01",
        "source_id": "me_res_431_2026_fenix_rigi",
        "url": "https://www.boletinoficial.gov.ar/detalleAviso/primera/340329/20260406",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Que el Solicitante declaró que el Proyecto implicará una inversión total en activos computables de doscientos cincuenta y un millones trescientos veintiún mil cuatrocientos noventa y cuatro dólares estadounidenses (USD 251.321.494)",
        "note": "Opened Argentina Boletín Oficial Resolución 431/2026 HTML.",
    },
    {
        "id": "me_res_431_2026_fenix_rigi",
        "type": "government",
        "chicago": "Ministerio de Economía (Argentina). “Resolución 431/2026.” Boletín Oficial de la República Argentina, 6 April 2026.",
        "url": "https://www.boletinoficial.gov.ar/detalleAviso/primera/340329/20260406",
        "annotation": "Official RIGI approval of Fénix Expansión Fase 1B at USD 251,321,494 computable investment. Supports rio_tinto_fenix_1b_rigi_2026.",
        "supports": ["rio_tinto_fenix_1b_rigi_2026", "hunt_res_lithium"],
    },
)

# 18 resources/nickel — Centaurus Jaguar JVEP pre-production CAPEX
A(
    {
        "id": "centaurus_jaguar_jvep_capex_2025",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "Centaurus Metals — Jaguar Nickel Sulphide Project JVEP pre-production CAPEX",
        "country": "Brazil",
        "asset": "8 May 2025 ASX: Jaguar Value Engineering Process confirms revised pre-production development capital US$380 million (incl. pre-strip and contingency; ~US$44m pre-strip for IWL) for 100%-owned Jaguar Ni sulphide project, Carajás Mineral Province (Pará); FID still pending financing (BNDES FINEM LOI and Glencore offtake logged separately). First-quartile C1 US$2.67/lb and AISC US$3.55/lb (contained Ni) stated in JVEP",
        "investment_type": "feasibility_capex",
        "value": "380000000",
        "currency": "USD",
        "value_usd": "380000000",
        "fx_usd": "1",
        "fx_date": "2025-05-08",
        "year": "2025",
        "status": "active",
        "lat": "-6.3",
        "lon": "-49.5",
        "geo_note": "Jaguar Ni project, Carajás / Pará (Centaurus ASX; approximate pin).",
        "evidence": "documented",
        "source_id": "centaurus_jaguar_jvep_20250508",
        "note": "Actor: Centaurus Metals (Australian ASX) — allied. Company ASX JVEP PDF 8 May 2025. Pre-FID study CAPEX — not closed spend. Distinct from centaurus_jaguar_nickel_lease_2025, centaurus_jaguar_bndes_loi_2026, and centaurus_glencore_offtake_jaguar_2026.",
    },
    {
        "id": "centaurus_jaguar_jvep_capex_2025",
        "retrieved": "2026-10-01",
        "source_id": "centaurus_jaguar_jvep_20250508",
        "url": "https://www.centaurus.com.au/site/pdf/0960efe5-e561-4a5c-ae3c-09ddf3fa2ad1/Jaguar-Value-Engineering-Enhances-Project-Economics.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Confirmed low capital intensity with pre-production capex of US$380 million (including pre-strip and contingency)",
        "note": "Opened Centaurus Metals ASX JVEP PDF 8 May 2025.",
    },
    {
        "id": "centaurus_jaguar_jvep_20250508",
        "type": "company",
        "chicago": "Centaurus Metals Limited. “Jaguar Value Engineering Enhances Feasibility Study Economics and Confirms Long-Life, Sustainable and Low-Cost Nickel Sulphide Project.” ASX release, 8 May 2025.",
        "url": "https://www.centaurus.com.au/site/pdf/0960efe5-e561-4a5c-ae3c-09ddf3fa2ad1/Jaguar-Value-Engineering-Enhances-Project-Economics.pdf",
        "annotation": "ASX primary stating US$380m Jaguar pre-production CAPEX from JVEP. Supports centaurus_jaguar_jvep_capex_2025.",
        "supports": ["centaurus_jaguar_jvep_capex_2025", "hunt_res_nickel"],
    },
)


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

    # Vestas corroboration bib for Olavarría turbine order
    vestas_bib = {
        "id": "vestas_argentina_orders_20250912",
        "type": "company",
        "chicago": "Vestas. “Vestas announces two orders in Argentina for a total of 217 MW.” 12 September 2025.",
        "url": "https://www.vestas.com/en/media/company-news/2025/vestas-announces-two-orders-in-argentina-for-a-total-of-c4233692",
        "annotation": "Company order intake confirming 186 MW V162-6.4 MW Argentina package with 25-year AOM5000 (customer undisclosed). Corroborates ifc_pcr_olavarria_wind_2026 turbine supply.",
        "supports": ["ifc_pcr_olavarria_wind_2026", "hunt_energy_wind"],
    }
    if vestas_bib["id"] not in bib_by:
        bib.append(vestas_bib)

    hunt_updates = {
        "hunt_energy_other_renewables": "Cycle 31: logged lindsayca_borinquen_i_em_2026 (UNVERIFIED proxy ~USD 100m; CGR appeal pending).",
        "hunt_energy_fission_smr": "Cycle 31: equal budget; Meitner / CAREM / Nuclearis / RMB already logged (miss).",
        "hunt_energy_solar": "Cycle 31: logged trina_pillanco_biobio_2026.",
        "hunt_fenb_araxa": "Cycle 31: equal budget; CBMM Araxá R$13bn plan logged C30 (miss).",
        "hunt_infra_engineering_epc": "Cycle 31: equal budget; PowerChina UFN-III / Worley Diablillos / Bechtel–EIMISA already (miss).",
        "hunt_infra_building_materials": "Cycle 31: equal budget; Holcim Pacasmayo / Cemex Colombia / Guayaquil clay already (miss).",
        "hunt_energy_wind": "Cycle 31: logged ifc_pcr_olavarria_wind_2026.",
        "hunt_latam_rail_telecom": "Cycle 31: equal budget; Siemens–Sonda / CRRC Pachuca / Alstom México already (miss).",
        "hunt_res_graphite": "Cycle 31: equal budget; Graphcoa / South Star / Graph+ already logged (miss).",
        "hunt_br_power_equip": "Cycle 31: equal budget; Hitachi Dosquebradas already (miss; avoid over-invest).",
        "hunt_res_balsa": "Cycle 31: equal budget; WITS/AIMA pairs already (miss).",
        "hunt_infra_bridges_roads": "Cycle 31: logged sacyr_ruta57_best_offer_2026.",
        "hunt_infra_port_ownership": "Cycle 31: equal budget; Marcona Jinzhao / HGT Aracruz already (miss).",
        "hunt_res_copper": "Cycle 31: refreshed fcx_el_abra_mill_chile_2026 (+USD 7.5bn) and logged bhp_escondida_new_concentrator_2026 (proxy).",
        "hunt_infra_port_cranes": "Cycle 31: logged konecranes_yilport_acajutla_2026.",
        "hunt_res_water": "Cycle 31: logged acciona_yanacocha_wtp_commission_2026.",
        "hunt_res_lithium": "Cycle 31: logged rio_tinto_fenix_1b_rigi_2026.",
        "hunt_res_nickel": "Cycle 31: logged centaurus_jaguar_jvep_capex_2025.",
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
    print("Cycle 31 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 31 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
