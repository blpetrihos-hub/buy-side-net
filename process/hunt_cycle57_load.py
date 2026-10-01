#!/usr/bin/env python3
"""Cycle 57 hunt: shuffle_seed=20261057; equal budget; U.S. ≥1/3; thin after.

Order: engineering_epc, wind, port_cranes, nickel, bridges_roads, graphite, rail,
solar, balsa, port_ownership, lithium, other_renewables, fission_smr,
power_plants_grid, niobium, building_materials, water, copper.
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
# 1 engineering_epc — McDermott Repsol Polok/Chinwol FEED (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "mcdermott_repsol_polok_chinwol_feed_2024",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "McDermott — Repsol Polok & Chinwol SURF FEED (Block 29, GoM Mexico)",
        "country": "Mexico",
        "asset": "3 Dec 2024: McDermott awarded FEED by Repsol Exploración México S.A. for Polok and Chinwol field development (Block 29, southeastern Gulf of Mexico off Veracruz/Tabasco); scope covers FEED for EPCI of subsea umbilicals, risers and flowlines (SURF); engineering delivery led from McDermott Houston. Distinct from mcdermott_brava_papa_terra_atlanta_2025 (Brazil T&I).",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "18.40",
        "lon": "-94.20",
        "geo_note": "Block 29 / Salina basin offshore Tabasco–Veracruz (approximate field pin ~88 km from Tabasco coast).",
        "evidence": "documented",
        "source_id": "mcdermott_repsol_polok_20241203",
        "note": "Actor: McDermott (U.S.) — us. Company primary; FEED contract value USD not disclosed.",
    },
    {
        "id": "mcdermott_repsol_polok_chinwol_feed_2024",
        "retrieved": "2026-10-01",
        "source_id": "mcdermott_repsol_polok_20241203",
        "url": "https://www.mcdermott.com/press-release-detail/123038/mcdermott-awarded-feed-contract-repsol-gulf-mexico",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "McDermott has been awarded a front-end engineering design (FEED) contract by Repsol Exploración México S.A. for the Polok and Chinwol field development project in the Gulf of Mexico. Under the contract scope, McDermott will provide comprehensive FEED services for the project's engineering, procurement, construction, and installation (EPCI) of subsea, umbilicals, risers, and flowlines (SURF).",
        "note": "Opened McDermott company press release 3 Dec 2024.",
    },
    {
        "id": "mcdermott_repsol_polok_20241203",
        "type": "company",
        "chicago": "McDermott International, Ltd. “McDermott Awarded FEED Contract by Repsol in the Gulf of Mexico.” 3 December 2024.",
        "url": "https://www.mcdermott.com/press-release-detail/123038/mcdermott-awarded-feed-contract-repsol-gulf-mexico",
        "annotation": "McDermott primary on Polok/Chinwol SURF FEED for Repsol Mexico Block 29. Supports mcdermott_repsol_polok_chinwol_feed_2024.",
        "supports": ["mcdermott_repsol_polok_chinwol_feed_2024", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 2 wind — AES Villagrán 456 MW MIA (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "aes_villagran_wind_726m_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "us",
        "counterpart": "AES / Transformaes — Parque Eólico Villagrán (Tamaulipas)",
        "country": "Mexico",
        "asset": "14 Aug 2026 SEMARNAT gaceta + BNamericas: Transformaes Creación Sostenible (AES) files MIA-R for Parque Eólico Villagrán, Villagrán municipality, Tamaulipas — 456 MW via 76 Vestas V162 turbines (6.2 MW limited to 6.0 MW), two 400/34.5 kV elevating substations, ~506.9 ha. BNamericas reports filing CapEx ~USD 726 million. Distinct from Oak Creek / Thermion CFE mixed awards.",
        "investment_type": "greenfield_generation",
        "value": "726000000",
        "currency": "USD",
        "value_usd": "726000000",
        "fx_usd": "1",
        "fx_date": "2026-08-14",
        "year": "2026",
        "status": "active",
        "lat": "24.56",
        "lon": "-99.51",
        "geo_note": "Villagrán municipality, Tamaulipas (municipal pin for AES MIA site).",
        "evidence": "proxy",
        "source_id": "bnamericas_aes_mexico_wind_20260824",
        "note": "Actor: AES (U.S.) via Transformaes — us. CapEx USD 726m from BNamericas citing filing — UNVERIFIED press proxy; SEMARNAT gaceta 0040-26 confirms 456 MW / 76 Vestas V162 scope without CapEx.",
    },
    {
        "id": "aes_villagran_wind_726m_2026",
        "retrieved": "2026-10-01",
        "source_id": "bnamericas_aes_mexico_wind_20260824",
        "url": "https://www.bnamericas.com/en/news/aes-doubles-down-with-nearly-us800mn-in-mexico-renewable-projects",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "The largest of the three AES projects, a 456MW wind farm in Tamaulipas state, will cost US$726 million (mn) to develop, according to the filing. The Parque Eólico Villagrán will generate electricity from 76 turbines supplied by Denmark-based manufacturer Vestas.",
        "note": "Opened BNamericas; SEMARNAT gaceta corroborates 456 MW / Vestas V162 MIA filing.",
    },
    {
        "id": "bnamericas_aes_mexico_wind_20260824",
        "type": "press",
        "chicago": "BNamericas. “AES Doubles Down with Nearly US$800mn in Mexico Renewable Projects.” 24 August 2026.",
        "url": "https://www.bnamericas.com/en/news/aes-doubles-down-with-nearly-us800mn-in-mexico-renewable-projects",
        "annotation": "Opened press on AES Transformaes Villagrán / El Quemado / San Agustín MIA filings and CapEx. Supports aes_villagran_wind_726m_2026 and aes_san_agustin_zacatecas_73m_2026.",
        "supports": [
            "aes_villagran_wind_726m_2026",
            "aes_san_agustin_zacatecas_73m_2026",
            "hunt_energy_wind",
        ],
    },
)

# ---------------------------------------------------------------------------
# 3 port_cranes — ZPMC Itapoá Phase IV 8th STS (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "zpmc_itapoa_sts8_phase4_2025",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — Porto Itapoá Phase IV 8th STS + RTG delivery",
        "country": "Brazil",
        "asset": "31 Dec 2025 PortalPortuario (citing Alphaliner): Shanghai Zhenhua (ZPMC) delivers one ship-to-shore STS crane and RTGs to Terminal de Contenedores de Itapoá (Tecon Santa Catarina / APMT 30%–Portoinvest 70%) aboard Zhen Hua 28; 8th STS brings fleet to eight on the 800 m quay as part of maxi-neo-panamax modernization with channel dredging to 16 m. Distinct from zpmc_itapoa_rtg_2023 (earlier ARTG batch).",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-26.18",
        "lon": "-48.61",
        "geo_note": "Porto Itapoá / Tecon Santa Catarina, Santa Catarina (terminal pin).",
        "evidence": "documented",
        "source_id": "portalportuario_zpmc_itapoa_20251231",
        "note": "Actor: ZPMC (PRC) — prc. Equipment CapEx USD not disclosed on opened page; Datamar 6 Jan 2026 corroborates Dec 2025 eighth STS arrival within Phase IV.",
    },
    {
        "id": "zpmc_itapoa_sts8_phase4_2025",
        "retrieved": "2026-10-01",
        "source_id": "portalportuario_zpmc_itapoa_20251231",
        "url": "https://portalportuario.cl/zpmc-entregara-nuevas-gruas-sts-y-rtg-al-terminal-de-contenedores-de-itapoa/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Shanghai Zhenhua Heavy Industries Company Limited (ZPMC) entregar una grúa ship-to-shore (STS) y dos grúas pórtico sobre neumáticos (RTG) al Terminal de Contenedores de Itapoá, Brasil. Las unidades llegarán totalmente ensambladas a bordo del buque Zhen Hua 28.",
        "note": "Opened PortalPortuario naming ZPMC STS/RTG delivery to Itapoá.",
    },
    {
        "id": "portalportuario_zpmc_itapoa_20251231",
        "type": "press",
        "chicago": "PortalPortuario. “ZPMC Entregará Nuevas Grúas STS y RTG al Terminal de Contenedores de Itapoá.” 31 December 2025.",
        "url": "https://portalportuario.cl/zpmc-entregara-nuevas-gruas-sts-y-rtg-al-terminal-de-contenedores-de-itapoa/",
        "annotation": "Opened Chilean port press naming ZPMC STS/RTG delivery to Itapoá Phase IV. Supports zpmc_itapoa_sts8_phase4_2025.",
        "supports": ["zpmc_itapoa_sts8_phase4_2025", "hunt_infra_port_cranes"],
    },
)

# ---------------------------------------------------------------------------
# 8 solar — ARRAY OmniTrack Lupi Peru (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "array_lupi_omnitrack_peru_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "us",
        "counterpart": "ARRAY Technologies — OmniTrack supply for Statkraft Lupi Solar (Peru)",
        "country": "Peru",
        "asset": "4 May 2026: ARRAY Technologies (NASDAQ: ARRY) contracted to supply OmniTrack terrain-following trackers for Statkraft Peru’s Lupi Solar Project (~180 MWp) in Mariscal Nieto province at average ~4,500 m elevation — first OmniTrack deployment in Latin America; main construction targeted Q2 2026, COD late 2027. Tracker CapEx USD not disclosed.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-17.20",
        "lon": "-70.85",
        "geo_note": "Mariscal Nieto province, Moquegua Region (high-altitude Lupi site; approximate provincial pin).",
        "evidence": "documented",
        "source_id": "array_lupi_peru_20260504",
        "note": "Actor: ARRAY Technologies (U.S.) tracker OEM — us. Company primary; Statkraft is project owner (allied) but observation is U.S. equipment supply.",
    },
    {
        "id": "array_lupi_omnitrack_peru_2026",
        "retrieved": "2026-10-01",
        "source_id": "array_lupi_peru_20260504",
        "url": "https://arraytechinc.com/press-release/array-technologies-selected-as-the-tracker-supplier-for-statkrafts-high-altitude-lupi-solar-project-in-peru/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "ARRAY Technologies, Inc. (NASDAQ: ARRY) … today announced that the ARRAY OmniTrack® terrain-following product has been contracted as the tracker technology for the Lupi Solar Project in Peru, developed by Statkraft Peru … The project will have an installed capacity of approximately 180 MWp.",
        "note": "Opened ARRAY company release 4 May 2026.",
    },
    {
        "id": "array_lupi_peru_20260504",
        "type": "company",
        "chicago": "ARRAY Technologies, Inc. “ARRAY Technologies Selected as the Tracker Supplier for Statkraft’s High Altitude Lupi Solar Project in Peru.” 4 May 2026.",
        "url": "https://arraytechinc.com/press-release/array-technologies-selected-as-the-tracker-supplier-for-statkrafts-high-altitude-lupi-solar-project-in-peru/",
        "annotation": "ARRAY primary on first LatAm OmniTrack supply for Lupi ~180 MWp. Supports array_lupi_omnitrack_peru_2026.",
        "supports": ["array_lupi_omnitrack_peru_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 8b solar — Nextracker Libélula low-carbon trackers (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "nextracker_libelula_engie_chile_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "us",
        "counterpart": "Nextracker — low-carbon NX Horizon trackers for ENGIE Libélula (Chile)",
        "country": "Chile",
        "asset": "May 2025 PV Tech (citing ENGIE): ENGIE Chile begins construction of PV & BESS Libélula (151 MWp solar + 199 MW / 5-hour BESS) in Colina/Tiltil Metropolitan Region; U.S. Nextracker to supply 2,311 low-carbon NX Horizon trackers with U.S. EAF steel — stated as first large-scale LatAm deployment of the low-carbon tracker line. Tracker contract USD not disclosed; plant CapEx variously reported USD 130–310m (not booked as Nextracker value).",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-33.20",
        "lon": "-70.80",
        "geo_note": "Colina / Tiltil, Santiago Metropolitan Region (Libélula site pin; approximate).",
        "evidence": "documented",
        "source_id": "pvtech_nextracker_libelula_20250521",
        "note": "Actor: Nextracker (U.S.) — us. Equipment-supply observation; ENGIE plant CapEx not attributed to Nextracker.",
    },
    {
        "id": "nextracker_libelula_engie_chile_2025",
        "retrieved": "2026-10-01",
        "source_id": "pvtech_nextracker_libelula_20250521",
        "url": "https://www.pv-tech.org/engie-begins-construction-at-151mw-199mw-solar-plus-storage-plant-in-chile/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Engie said the project will include low-carbon solar trackers from Nextracker. According to the company, this will be a first in Latin America with the US tracker manufacturer providing 2,311 of its low-carbon NX Horizon trackers. The trackers will incorporate steel produced in the US using electric arc furnace technology.",
        "note": "Opened PV Tech citing ENGIE on Nextracker low-carbon tracker supply.",
    },
    {
        "id": "pvtech_nextracker_libelula_20250521",
        "type": "press",
        "chicago": "Touriño Jacobo, Jonathan. “Engie Begins Construction at Chile Solar-Plus-Storage Plant.” PV Tech, 21 May 2025.",
        "url": "https://www.pv-tech.org/engie-begins-construction-at-151mw-199mw-solar-plus-storage-plant-in-chile/",
        "annotation": "Opened PV Tech on ENGIE Libélula and Nextracker 2,311 low-carbon NX Horizon trackers. Supports nextracker_libelula_engie_chile_2025.",
        "supports": ["nextracker_libelula_engie_chile_2025", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 10 port_ownership — FMS Peru Callao Naval Base design/construction (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fms_peru_callao_naval_1p5bn_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "us",
        "counterpart": "U.S. DSCA / FMS — Callao Naval Base maritime & onshore facilities package",
        "country": "Peru",
        "asset": "15 Jan 2026 Congressional notification / 17 Mar 2026 Federal Register: proposed Foreign Military Sale to Government of Peru for lifecycle design, construction, project management and related engineering services for maritime and onshore facilities at Callao Naval Base; estimated total cost USD 1.5 billion (national funds); up to 20 U.S. Gov/contractor personnel in Peru up to 10 years. Improves port infrastructure for naval/logistics operations. Distinct from APM/DP World Callao commercial terminal rows.",
        "investment_type": "epc_design_build",
        "value": "1500000000",
        "currency": "USD",
        "value_usd": "1500000000",
        "fx_usd": "1",
        "fx_date": "2026-01-15",
        "year": "2026",
        "status": "active",
        "lat": "-12.05",
        "lon": "-77.15",
        "geo_note": "Callao Naval Base, Callao Province (naval maritime facility pin).",
        "evidence": "documented",
        "source_id": "fr_peru_callao_fms_20260317",
        "note": "Actor: U.S. FMS / DSCA proposed sale — us. Official Federal Register arms-sales notification; contractor TBD; proposed LOA not yet a closed construction award.",
    },
    {
        "id": "fms_peru_callao_naval_1p5bn_2026",
        "retrieved": "2026-10-01",
        "source_id": "fr_peru_callao_fms_20260317",
        "url": "https://www.govinfo.gov/content/pkg/FR-2026-03-17/html/2026-05146.htm",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The Government of Peru has requested to buy equipment and services to support the procurement of maritime and onshore facilities at the Callao Naval Base. … The estimated total cost is $1.5 billion.",
        "note": "Opened Federal Register Transmittal 25-37 / FR Doc 2026-05146.",
    },
    {
        "id": "fr_peru_callao_fms_20260317",
        "type": "official",
        "chicago": "U.S. Department of Defense. “Arms Sales Notification — Peru—Design and Construction at Callao Naval Base” (Transmittal No. 25-37). Federal Register 91, no. 51 (17 March 2026): 12764–12766.",
        "url": "https://www.govinfo.gov/content/pkg/FR-2026-03-17/html/2026-05146.htm",
        "annotation": "Official FMS notification for USD 1.5bn Callao Naval Base maritime/onshore facilities package. Supports fms_peru_callao_naval_1p5bn_2026.",
        "supports": ["fms_peru_callao_naval_1p5bn_2026", "hunt_infra_port_ownership"],
    },
)

# ---------------------------------------------------------------------------
# 12 other_renewables — AES San Agustín hybrid solar+BESS (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "aes_san_agustin_zacatecas_73m_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "AES / Transformaes — Parque Solar San Agustín hybrid PV+BESS (Zacatecas)",
        "country": "Mexico",
        "asset": "Aug 2026 BNamericas: AES Transformaes files environmental permit for Parque Solar San Agustín in Zacatecas — 45 MW generation capacity hybrid solar-plus-battery project with stated CapEx USD 73 million. Companion filing to Villagrán wind and El Quemado wind. Hybrid PV+storage angle (other_renewables).",
        "investment_type": "greenfield_storage",
        "value": "73000000",
        "currency": "USD",
        "value_usd": "73000000",
        "fx_usd": "1",
        "fx_date": "2026-08-24",
        "year": "2026",
        "status": "active",
        "lat": "22.77",
        "lon": "-102.58",
        "geo_note": "Zacatecas state (San Agustín hybrid project; approximate state-capital pin).",
        "evidence": "proxy",
        "source_id": "bnamericas_aes_mexico_wind_20260824",
        "note": "Actor: AES (U.S.) — us. CapEx USD 73m from BNamericas citing filing — UNVERIFIED press proxy; BESS size not stated on opened page.",
    },
    {
        "id": "aes_san_agustin_zacatecas_73m_2026",
        "retrieved": "2026-10-01",
        "source_id": "bnamericas_aes_mexico_wind_20260824",
        "url": "https://www.bnamericas.com/en/news/aes-doubles-down-with-nearly-us800mn-in-mexico-renewable-projects",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "The third project registered by AES is a smaller hybrid solar and battery project in north-central Mexico, with 45MW of generation capacity. Located in Zacatecas state, Parque Solar San Agustín will cost US$73 million (mn) to develop.",
        "note": "Opened BNamericas AES Mexico renewables filing package.",
    },
    {
        "id": "bnamericas_aes_mexico_wind_20260824",
        "type": "press",
        "chicago": "BNamericas. “AES Doubles Down with Nearly US$800mn in Mexico Renewable Projects.” 24 August 2026.",
        "url": "https://www.bnamericas.com/en/news/aes-doubles-down-with-nearly-us800mn-in-mexico-renewable-projects",
        "annotation": "Opened press on AES Transformaes Villagrán / El Quemado / San Agustín MIA filings and CapEx. Supports aes_villagran_wind_726m_2026 and aes_san_agustin_zacatecas_73m_2026.",
        "supports": [
            "aes_villagran_wind_726m_2026",
            "aes_san_agustin_zacatecas_73m_2026",
            "hunt_energy_other_renewables",
        ],
    },
)

# ---------------------------------------------------------------------------
# 13 fission_smr — U.S.–Colombia civil nuclear MOU (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "colombia_us_civil_nuclear_mou_2026",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "us",
        "counterpart": "United States — Colombia Strategic Civil Nuclear Cooperation MOU",
        "country": "Colombia",
        "asset": "8 Sep 2026: U.S. Secretary of State Marco Rubio and Colombian Foreign Minister Omar Bula sign Memorandum of Understanding concerning Strategic Civil Nuclear Cooperation in Barranquilla — bilateral framework for regulatory capacity-building, industry partnerships, scientific exchanges, and exploration of U.S. nuclear technologies including advanced and small modular reactors, fuel, equipment and services (power and non-power). No reactor EPC CapEx on page. Distinct from FIRST/Argentina/Peru partner rows.",
        "investment_type": "bilateral_mou",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "10.99",
        "lon": "-74.79",
        "geo_note": "Barranquilla signing location (MOU ceremony pin).",
        "evidence": "documented",
        "source_id": "state_colombia_nuclear_mou_20260908",
        "note": "Actor: U.S. State Department MOU with Colombia — us. Agency primary; non-binding; no CapEx.",
    },
    {
        "id": "colombia_us_civil_nuclear_mou_2026",
        "retrieved": "2026-10-01",
        "source_id": "state_colombia_nuclear_mou_20260908",
        "url": "https://www.state.gov/releases/office-of-the-spokesperson/2026/09/secretary-rubio-and-colombian-foreign-minister-bula-sign-arrangements-on-critical-minerals-and-civil-nuclear-cooperation",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The Civil Nuclear Cooperation Memorandum of Understanding: … Expresses joint intent to collaborate across regulatory capacity-building, industry partnerships, and scientific and academic exchanges … explore U.S. nuclear technologies (including advanced and small modular reactors), fuel, equipment, and services …",
        "note": "Opened U.S. State Department spokesperson release 8 Sep 2026.",
    },
    {
        "id": "state_colombia_nuclear_mou_20260908",
        "type": "official",
        "chicago": "U.S. Department of State, Office of the Spokesperson. “Secretary Rubio and Colombian Foreign Minister Bula Sign Arrangements on Critical Minerals and Civil Nuclear Cooperation.” 8 September 2026.",
        "url": "https://www.state.gov/releases/office-of-the-spokesperson/2026/09/secretary-rubio-and-colombian-foreign-minister-bula-sign-arrangements-on-critical-minerals-and-civil-nuclear-cooperation",
        "annotation": "Official U.S. release on Colombia civil nuclear MOU including SMR exploration. Supports colombia_us_civil_nuclear_mou_2026.",
        "supports": ["colombia_us_civil_nuclear_mou_2026", "hunt_energy_fission_smr"],
    },
)

# ---------------------------------------------------------------------------
# 14 power_plants_grid — GE Vernova São Simão UG3 modernization (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ge_vernova_sao_simao_ug3_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "GE Vernova — São Simão UHE UG3 modernization (consortium lead)",
        "country": "Brazil",
        "asset": "14 Sep 2026: GE Vernova and SPIC Brasil announce completion of Generating Unit UG3 modernization at 1,710 MW São Simão hydro plant (Goiás–Minas Gerais border) in 10.3 months; GE Vernova leads engineering/integration/installation/commissioning of turbines, generators and auxiliaries within a >R$ 1.2 billion ten-year six-unit program (completion targeted 2029) including full digital control conversion. Distinct from ge_vernova_azulao_i_cod_2026 / Arauco GIS.",
        "investment_type": "epc",
        "value": "1200000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-18.99",
        "lon": "-50.24",
        "geo_note": "UHE São Simão, Goiás–Minas Gerais border (plant pin).",
        "evidence": "documented",
        "source_id": "ge_vernova_sao_simao_20260914",
        "note": "Actor: GE Vernova (U.S.-listed) consortium lead — us. Program CapEx >R$ 1.2bn stored in BRL without FX; UG3 is one of six units — figure is full-program investment stated by GE Vernova/SPIC.",
    },
    {
        "id": "ge_vernova_sao_simao_ug3_2026",
        "retrieved": "2026-10-01",
        "source_id": "ge_vernova_sao_simao_20260914",
        "url": "https://www.gevernova.com/news/press-releases/spic-brasil-ge-vernova-accelerate-modernization-sao-simao-hydroelectric-plant-brazil",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "SPIC Brasil … and GE Vernova Inc. (NYSE:GEV) today announced the successful completion of the modernization of Generating Unit (UG) 3. … The robust modernization program is driven by an investment exceeding R$ 1.2 billion distributed over ten years.",
        "note": "Opened GE Vernova company release 14 Sep 2026.",
    },
    {
        "id": "ge_vernova_sao_simao_20260914",
        "type": "company",
        "chicago": "GE Vernova Inc. “SPIC Brasil and GE Vernova Accelerate the Modernization of the São Simão Hydroelectric Plant, Achieving Important Performance Milestones.” 14 September 2026.",
        "url": "https://www.gevernova.com/news/press-releases/spic-brasil-ge-vernova-accelerate-modernization-sao-simao-hydroelectric-plant-brazil",
        "annotation": "GE Vernova primary on São Simão UG3 modernization and >R$1.2bn program; also names PowerChina consortium role. Supports ge_vernova_sao_simao_ug3_2026 and powerchina_sao_simao_bop_2026.",
        "supports": [
            "ge_vernova_sao_simao_ug3_2026",
            "powerchina_sao_simao_bop_2026",
            "hunt_br_power_equip",
        ],
    },
)

# ---------------------------------------------------------------------------
# 14b power_plants_grid — PowerChina São Simão BOP (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "powerchina_sao_simao_bop_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "prc",
        "counterpart": "PowerChina — São Simão UHE hydromechanical / SDSC / BOP supply",
        "country": "Brazil",
        "asset": "14 Sep 2026 GE Vernova release: PowerChina is consortium partner supplying hydromechanical systems, SDSC, and electrical/mechanical BOP for the São Simão six-unit modernization led by GE Vernova for SPIC Brasil. Equipment/EPC supply angle within the >R$ 1.2bn program — CapEx split not disclosed. Distinct from PowerChina Palmira / Mauriti solar rows.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-18.99",
        "lon": "-50.24",
        "geo_note": "UHE São Simão, Goiás–Minas Gerais border (same plant pin as GE Vernova row).",
        "evidence": "documented",
        "source_id": "ge_vernova_sao_simao_20260914",
        "note": "Actor: PowerChina (PRC) — prc. Named consortium equipment/BOP supplier on GE Vernova primary; contract USD not disclosed.",
    },
    {
        "id": "powerchina_sao_simao_bop_2026",
        "retrieved": "2026-10-01",
        "source_id": "ge_vernova_sao_simao_20260914",
        "url": "https://www.gevernova.com/news/press-releases/spic-brasil-ge-vernova-accelerate-modernization-sao-simao-hydroelectric-plant-brazil",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The modernization of the 1,710 MW power plant … is being carried out by a consortium led by GE Vernova and including Powerchina, responsible for supplying the hydromechanical, SDSC, and electrical and mechanical BOP systems.",
        "note": "Opened GE Vernova release naming PowerChina BOP/hydromechanical scope.",
    },
    {
        "id": "ge_vernova_sao_simao_20260914",
        "type": "company",
        "chicago": "GE Vernova Inc. “SPIC Brasil and GE Vernova Accelerate the Modernization of the São Simão Hydroelectric Plant, Achieving Important Performance Milestones.” 14 September 2026.",
        "url": "https://www.gevernova.com/news/press-releases/spic-brasil-ge-vernova-accelerate-modernization-sao-simao-hydroelectric-plant-brazil",
        "annotation": "GE Vernova primary on São Simão UG3 modernization and >R$1.2bn program; also names PowerChina consortium role. Supports ge_vernova_sao_simao_ug3_2026 and powerchina_sao_simao_bop_2026.",
        "supports": [
            "ge_vernova_sao_simao_ug3_2026",
            "powerchina_sao_simao_bop_2026",
            "hunt_br_power_equip",
        ],
    },
)

# ---------------------------------------------------------------------------
# 16 building_materials — Sinoma Cementos Cibao clinker line (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sinoma_cibao_clinker_line_2026",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "prc",
        "counterpart": "Sinoma — Cementos Cibao new clinker line (Santiago, DR)",
        "country": "Dominican Republic",
        "asset": "31 Mar 2026 Global Cement: Cementos Cibao inaugurates new clinker production line at Santiago plant (attended by President Abinader); capacity 3,500 t/day clinker with automation and emissions controls; construction ~1 year; line built by Sinoma; supports Caribbean exports. CapEx USD not disclosed. Distinct from Sinoma Votorantim Z02 / Cruz Azul captive EPC.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "19.45",
        "lon": "-70.70",
        "geo_note": "Santiago de los Caballeros, Dominican Republic (Cementos Cibao plant pin; approximate).",
        "evidence": "documented",
        "source_id": "globalcement_cibao_sinoma_20260331",
        "note": "Actor: Sinoma (PRC) EPC builder — prc. CapEx not on opened page; Cementos Cibao is Dominican owner (other).",
    },
    {
        "id": "sinoma_cibao_clinker_line_2026",
        "retrieved": "2026-10-01",
        "source_id": "globalcement_cibao_sinoma_20260331",
        "url": "https://globalcement.com/news/20601-cementos-cibao-inaugurates-new-clinker-production-line",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The new line has a production capacity of 3500t/day of clinker … The line was built by Sinoma and the company said that it will support exports to the Caribbean and other markets.",
        "note": "Opened Global Cement on Cementos Cibao / Sinoma Santiago clinker line inauguration.",
    },
    {
        "id": "globalcement_cibao_sinoma_20260331",
        "type": "press",
        "chicago": "Global Cement. “Cementos Cibao Inaugurates New Clinker Production Line.” 31 March 2026.",
        "url": "https://globalcement.com/news/20601-cementos-cibao-inaugurates-new-clinker-production-line",
        "annotation": "Opened trade press on Sinoma-built 3,500 t/d clinker line at Cementos Cibao Santiago. Supports sinoma_cibao_clinker_line_2026.",
        "supports": ["sinoma_cibao_clinker_line_2026", "hunt_infra_building_materials"],
    },
)

# ---------------------------------------------------------------------------
# 17 water — ENAPAC Solaer multicarrier desal (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "enapac_solaers_desal_1p5bn_2025",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Solaer / Aguasol — ENAPAC multicarrier desalination system (Atacama)",
        "country": "Chile",
        "asset": "30 Dec 2025 REDIMIN (citing El Mercurio / Claudio Bitran): ENAPAC seawater RO desalination + reservoir (~592,000 m³) + northern (~166 km) and eastern (~157 km) distribution arms near Caldera, Atacama, backed by ~100 MW solar + storage; Aguasol holding linked to Israeli Solaer Renewable Energies (with Spanish Himin Solar); estimated investment USD 1.5 billion; third RCA obtained ~Nov 2025; construction targeted ~4 years out with first water ~2030–2031 contingent on offtake contracts. Distinct from IDE SADDN / Aguas Pacífico / GS Inima Atacama.",
        "investment_type": "water_infrastructure",
        "value": "1500000000",
        "currency": "USD",
        "value_usd": "1500000000",
        "fx_usd": "1",
        "fx_date": "2025-12-30",
        "year": "2025",
        "status": "active",
        "lat": "-27.07",
        "lon": "-70.82",
        "geo_note": "Caldera area, Atacama Region (~30 km from Caldera; ENAPAC coastal plant pin approximate).",
        "evidence": "proxy",
        "source_id": "redimin_enapac_solaers_20251230",
        "note": "Actor: Solaer (Israel) via Aguasol — allied. CapEx USD 1.5bn from REDIMIN/El Mercurio interview — UNVERIFIED press proxy; not yet FID.",
    },
    {
        "id": "enapac_solaers_desal_1p5bn_2025",
        "retrieved": "2026-10-01",
        "source_id": "redimin_enapac_solaers_20251230",
        "url": "https://www.redimin.cl/avanza-desaladora-multicarrier-israelita-en-atacama-reciben-ultimo-permiso-ambiental-y-buscan-cerrar-contratos-en-2026",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "El proyecto «multicliente» del holding Aguasol, ligado al grupo israelita Solaer Renewable Energies (Solaer), y donde también participa la española Himin Solar estima una inversión por US$ 1.500 millones.",
        "note": "Opened REDIMIN citing El Mercurio interview with ENAPAC GM Bitran.",
    },
    {
        "id": "redimin_enapac_solaers_20251230",
        "type": "press",
        "chicago": "Recabarren Ortiz, Cristian. “Avanza Desaladora Multicarrier Israelita en Atacama: Reciben Último Permiso Ambiental y Buscan Cerrar Contratos en 2026.” REDIMIN, 30 December 2025.",
        "url": "https://www.redimin.cl/avanza-desaladora-multicarrier-israelita-en-atacama-reciben-ultimo-permiso-ambiental-y-buscan-cerrar-contratos-en-2026",
        "annotation": "Opened Chilean mining press on ENAPAC/Solaer USD 1.5bn multicarrier desal. Supports enapac_solaers_desal_1p5bn_2025.",
        "supports": ["enapac_solaers_desal_1p5bn_2025", "hunt_res_water"],
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
        "hunt_infra_engineering_epc": "Cycle 57: logged mcdermott_repsol_polok_chinwol_feed_2024 (U.S.).",
        "hunt_energy_wind": "Cycle 57: logged aes_villagran_wind_726m_2026 (U.S.; CapEx proxy).",
        "hunt_infra_port_cranes": "Cycle 57: logged zpmc_itapoa_sts8_phase4_2025 (PRC).",
        "hunt_res_nickel": "Cycle 57: equal budget; Jervois/DFC/Westwin/Centaurus already (miss).",
        "hunt_infra_bridges_roads": "Cycle 57: equal budget; USACE GT / CHEC San Carlos already (miss).",
        "hunt_res_graphite": "Cycle 57: equal budget; Graphcoa/South Star/Atlas already (miss).",
        "hunt_latam_rail_telecom": "Cycle 57: equal budget; PowerChina Chancay / Siemens Trivia already (miss).",
        "hunt_energy_solar": "Cycle 57: logged array_lupi_omnitrack_peru_2026 + nextracker_libelula_engie_chile_2025 (U.S.).",
        "hunt_res_balsa": "Cycle 57: equal budget; Plantabal/CoreLite/Gurit already (miss).",
        "hunt_infra_port_ownership": "Cycle 57: logged fms_peru_callao_naval_1p5bn_2026 (U.S. FMS).",
        "hunt_res_lithium": "Cycle 57: equal budget; EnergyX/Atlas/Albemarle already (miss).",
        "hunt_energy_other_renewables": "Cycle 57: logged aes_san_agustin_zacatecas_73m_2026 (U.S.; CapEx proxy).",
        "hunt_energy_fission_smr": "Cycle 57: logged colombia_us_civil_nuclear_mou_2026 (U.S.).",
        "hunt_br_power_equip": "Cycle 57: logged ge_vernova_sao_simao_ug3_2026 (U.S.) + powerchina_sao_simao_bop_2026 (PRC).",
        "hunt_fenb_araxa": "Cycle 57: equal budget; CBMM/Boston Metal/St George already (miss).",
        "hunt_infra_building_materials": "Cycle 57: logged sinoma_cibao_clinker_line_2026 (PRC).",
        "hunt_res_water": "Cycle 57: logged enapac_solaers_desal_1p5bn_2025 (allied; CapEx proxy).",
        "hunt_res_copper": "Cycle 57: equal budget; FCX El Abra / MMG Las Bambas already (miss).",
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
    print("Cycle 57 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
