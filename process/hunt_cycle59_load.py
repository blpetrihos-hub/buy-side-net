#!/usr/bin/env python3
"""Cycle 59 hunt: shuffle_seed=20261059; equal budget; U.S. ≥1/3; thin after.

Order: graphite, water, power_plants_grid, port_ownership, bridges_roads, lithium,
other_renewables, port_cranes, niobium, nickel, engineering_epc, rail, fission_smr,
solar, copper, wind, building_materials, balsa.
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
# 2 resources/water — NADBank Baja California Rosarito distribution loan
# ---------------------------------------------------------------------------
A(
    {
        "id": "nadbank_baja_rosarito_distrib_82m_2026",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "NADBank / COFIDAN — Baja California Rosarito desal distribution loan",
        "country": "Mexico",
        "asset": "8 May 2026 NADBank certification: Water Distribution Infrastructure Project for State of Baja California — convey/store/distribute drinking water from Playas de Rosarito desalination plant (2,200 lps) to Ensenada, Playas de Rosarito and Tijuana; project cost US$271.44m; NADBank via COFIDAN market-rate loan US$82.16m (MXN 1.479bn awarded; loan agreement signed 29 May 2026). Distinct from cox_rosarito_desal_mexico_2026 (plant EPC).",
        "investment_type": "financing",
        "value": "82160000",
        "currency": "USD",
        "value_usd": "82160000",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "32.365",
        "lon": "-117.061",
        "geo_note": "Playas de Rosarito desal / Rosarito Tank transmission corridor (Baja California).",
        "evidence": "documented",
        "source_id": "nadbank_baja_water_distrib_20260508",
        "note": "Actor: North American Development Bank (U.S.–Mexico) via COFIDAN — us. Loan amount from NADBank project page.",
    },
    {
        "id": "nadbank_baja_rosarito_distrib_82m_2026",
        "retrieved": "2026-10-01",
        "source_id": "nadbank_baja_water_distrib_20260508",
        "url": "https://nadbank.org/our-projects/financed-projects/proyect/water-distribution-infrastructure-project-in-the-state-of-baja-california",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Certification date May 8, 2026 … Project cost US$271.44 million … NADBank Funds US$82.16 million - loan … convey, store and supply water from the new Playas de Rosarito Desalination Plant to the communities of Ensenada, Playas de Rosarito and Tijuana",
        "note": "Opened NADBank financed-projects page for Baja California water distribution.",
    },
    {
        "id": "nadbank_baja_water_distrib_20260508",
        "type": "government",
        "chicago": "North American Development Bank. “Water Distribution Infrastructure Project in the State of Baja California.” Financed projects, certified 8 May 2026.",
        "url": "https://nadbank.org/our-projects/financed-projects/proyect/water-distribution-infrastructure-project-in-the-state-of-baja-california",
        "annotation": "NADBank/COFIDAN US$82.16m loan for Rosarito desal distribution works. Supports nadbank_baja_rosarito_distrib_82m_2026.",
        "supports": ["nadbank_baja_rosarito_distrib_82m_2026", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 3 energy/power_plants_grid — POWERCHINA EDP Piauí 500 kV COD
# ---------------------------------------------------------------------------
A(
    {
        "id": "powerchina_edp_piaui_500kv_cod_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "prc",
        "counterpart": "POWERCHINA — EDP Piauí 500 kV transmission line COD",
        "country": "Brazil",
        "asset": "20 Sep 2026 POWERCHINA EN: 500 kV transmission line project in Piauí for EDP connected to grid on first attempt and commenced commercial operations 9 Sep 2026; 304 km with 611 towers; finished ~1 month ahead of schedule. Part of EDP Lot 2 (ANEEL auction) renewables evacuation. CapEx USD not disclosed on POWERCHINA page. Distinct from state_grid_ne_uhv_construction_2026 and São Simão BOP rows.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-8.35",
        "lon": "-42.25",
        "geo_note": "São João do Piauí II / Curral Novo–Ribeiro Gonçalves 500 kV corridor (Piauí).",
        "evidence": "documented",
        "source_id": "powerchina_edp_piaui_500kv_20260920",
        "note": "Actor: POWERCHINA (PRC SOE EPC) — prc. Owner EDP (Portugal) allied but row attributes EPC constructor.",
    },
    {
        "id": "powerchina_edp_piaui_500kv_cod_2026",
        "retrieved": "2026-10-01",
        "source_id": "powerchina_edp_piaui_500kv_20260920",
        "url": "https://en.powerchina.cn/2026-09/20/c_829121.htm",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The 500kV Transmission Line Project in Piauí, Brazil, constructed by POWERCHINA, was connected to the grid on the first attempt and commenced commercial operations on Sept 9. … spans a total length of 304 kilometers with 611 transmission towers built.",
        "note": "Opened POWERCHINA English company news 20 Sep 2026.",
    },
    {
        "id": "powerchina_edp_piaui_500kv_20260920",
        "type": "company",
        "chicago": "POWERCHINA. “POWERCHINA-built Transmission Line Project in Brazil Connected to Grid.” Company news, 20 September 2026.",
        "url": "https://en.powerchina.cn/2026-09/20/c_829121.htm",
        "annotation": "POWERCHINA COD of EDP Piauí 500 kV line (304 km / 611 towers). Supports powerchina_edp_piaui_500kv_cod_2026.",
        "supports": ["powerchina_edp_piaui_500kv_cod_2026", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 6 resources/lithium — Lilac / Lake Resources Kachi DIA (U.S. DLE)
# ---------------------------------------------------------------------------
A(
    {
        "id": "lilac_kachi_dia_permit_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "us",
        "counterpart": "Lilac Solutions / Lake Resources — Kachi DLE environmental DIA",
        "country": "Argentina",
        "asset": "29 Sep 2026 Lilac Solutions: Catamarca Ministry of Mining issued Declaración de Impacto Ambiental (DIA) for Kachi Lithium Brine Project (Salar de Carachi Pampa); Lilac holds 20% equity and supplies Lilac IX™ DLE; first commercial-scale DLE with brine reinjection permitted in South America; Phase 1 target 25,000 tpa LCE; advancing to FEED. CapEx USD not on release. Distinct from EnergyX Black Giant / Eni Chile stack.",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-26.50",
        "lon": "-67.45",
        "geo_note": "Salar de Carachi Pampa / Kachi project area, Catamarca Province.",
        "evidence": "documented",
        "source_id": "lilac_kachi_dia_20260929",
        "note": "Actor: Lilac Solutions (Oakland, CA / U.S. DLE tech + 20% equity) — us.",
    },
    {
        "id": "lilac_kachi_dia_permit_2026",
        "retrieved": "2026-10-01",
        "source_id": "lilac_kachi_dia_20260929",
        "url": "https://lilacsolutions.com/news/lilac-ix-direct-lithium-extraction-technology-secures-first-commercial-environmental-permit-in-south-america",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Catamarca Ministry of Mining has issued the Environmental Impact Declaration (Declaración de Impacto Ambiental, or “DIA”) for the Kachi Lithium Brine Project … Lilac holds a 20% equity stake in the project. … Phase 1 targets production of 25,000 tonnes per annum (tpa) LCE",
        "note": "Opened Lilac Solutions company news 29 Sep 2026.",
    },
    {
        "id": "lilac_kachi_dia_20260929",
        "type": "company",
        "chicago": "Lilac Solutions. “Lilac IX Direct Lithium Extraction Technology Secures First Commercial Environmental Permit in South America.” News release, 29 September 2026.",
        "url": "https://lilacsolutions.com/news/lilac-ix-direct-lithium-extraction-technology-secures-first-commercial-environmental-permit-in-south-america",
        "annotation": "U.S. Lilac DIA permit for Kachi DLE (Catamarca). Supports lilac_kachi_dia_permit_2026.",
        "supports": ["lilac_kachi_dia_permit_2026", "hunt_res_lithium"],
    },
)

# ---------------------------------------------------------------------------
# 8 infrastructure/port_cranes — Konecranes ESP.10 MHC Iquique
# ---------------------------------------------------------------------------
A(
    {
        "id": "konecranes_iquique_esp10_2025",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Konecranes — Iquique Terminal Internacional ESP.10 MHC",
        "country": "Chile",
        "asset": "11 Apr 2025 Konecranes: Iquique Terminal Internacional (SAAM) ordered Generation 6 Gottwald ESP.10 mobile harbor crane (largest in Konecranes portfolio) in Q3 2024; en route from Europe for April 2025 delivery; 10 m tower extension for nine-high / 22-row super-post-Panamax; two telescopic twin-lift spreaders + grab capability. CapEx USD not disclosed. Distinct from konecranes_arica_mhc_2026 and Yucatán Progreso ESP.7.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-20.205",
        "lon": "-70.152",
        "geo_note": "Iquique Terminal Internacional, Port of Iquique, Tarapacá Region.",
        "evidence": "documented",
        "source_id": "konecranes_iquique_esp10_20250411",
        "note": "Actor: Konecranes (Finland) — allied. SAAM Terminals operator Chile.",
    },
    {
        "id": "konecranes_iquique_esp10_2025",
        "retrieved": "2026-10-01",
        "source_id": "konecranes_iquique_esp10_20250411",
        "url": "https://www.konecranes.com/press-releases/chiles-iquique-terminal-internacional-sa-to-receive-largest-mobile-harbor-crane-in-konecranes-portfolio",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Iquique Terminal Internacional S.A. (ITI) in Chile ordered a Konecranes Gottwald ESP.10 – the largest mobile harbor crane in the Konecranes portfolio … deal was signed in Q3 2024, and the crane is now en route from Europe to be delivered in April 2025.",
        "note": "Opened Konecranes trade press release 11 Apr 2025.",
    },
    {
        "id": "konecranes_iquique_esp10_20250411",
        "type": "company",
        "chicago": "Konecranes. “Chile’s Iquique Terminal Internacional S.A. to Receive Largest Mobile Harbor Crane in Konecranes’ Portfolio.” Trade press release, 11 April 2025.",
        "url": "https://www.konecranes.com/press-releases/chiles-iquique-terminal-internacional-sa-to-receive-largest-mobile-harbor-crane-in-konecranes-portfolio",
        "annotation": "Konecranes ESP.10 MHC order/delivery for ITI Iquique. Supports konecranes_iquique_esp10_2025.",
        "supports": ["konecranes_iquique_esp10_2025", "hunt_infra_port_cranes"],
    },
)

# ---------------------------------------------------------------------------
# 11 infrastructure/engineering_epc — Baker Hughes Petrobras well construction
# ---------------------------------------------------------------------------
A(
    {
        "id": "baker_hughes_petrobras_wells_santos_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Baker Hughes — Petrobras Santos Basin integrated well construction extension",
        "country": "Brazil",
        "asset": "26 May 2026 Baker Hughes: major contract extension with Petrobras for integrated well-construction solutions across Santos Basin pre-salt oilfields; expands AutoTrak RSS, LWD tools, Dynamus bits plus wireline/cementing/fluids/geosciences via Integration & Solutions; builds on early-2024 award. Contract value USD not disclosed. Distinct from McDermott Brava Papa-Terra/Atlanta T&I.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-25.50",
        "lon": "-43.50",
        "geo_note": "Santos Basin pre-salt offshore well construction (Brazil).",
        "evidence": "documented",
        "source_id": "baker_hughes_petrobras_wells_20260526",
        "note": "Actor: Baker Hughes (U.S. energy technology) — us.",
    },
    {
        "id": "baker_hughes_petrobras_wells_santos_2026",
        "retrieved": "2026-10-01",
        "source_id": "baker_hughes_petrobras_wells_20260526",
        "url": "https://investors.bakerhughes.com/news/press-releases/news-details/2026/Baker-Hughes-Extends-and-Expands-Integrated-Well-Construction-Contract-with-Petrobras/default.aspx",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Baker Hughes … announced … a major contract extension with Petrobras to provide integrated solutions for well construction across Brazil’s Santos Basin. … builds on a well construction services award announced in early 2024",
        "note": "Opened Baker Hughes investor press release 26 May 2026.",
    },
    {
        "id": "baker_hughes_petrobras_wells_20260526",
        "type": "company",
        "chicago": "Baker Hughes. “Baker Hughes Extends and Expands Integrated Well Construction Contract with Petrobras.” Press release, 26 May 2026.",
        "url": "https://investors.bakerhughes.com/news/press-releases/news-details/2026/Baker-Hughes-Extends-and-Expands-Integrated-Well-Construction-Contract-with-Petrobras/default.aspx",
        "annotation": "U.S. Baker Hughes Petrobras Santos Basin well-construction extension. Supports baker_hughes_petrobras_wells_santos_2026.",
        "supports": ["baker_hughes_petrobras_wells_santos_2026", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 12 infrastructure/rail — CICSA–FCC Saltillo–Santa Catarina 111 km
# ---------------------------------------------------------------------------
A(
    {
        "id": "fcc_cicsa_saltillo_santa_catarina_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "FCC Construcción / CICSA (Carso) — Saltillo–Santa Catarina passenger rail civil works",
        "country": "Mexico",
        "asset": "15 Sep 2025 Grupo Carso BMV notice: SICT/ARTF awarded consortium Operadora CICSA (50%) + FCC Construcción S.A. (50%) design-and-build of 111 km Saltillo–Nuevo Laredo passenger train Segments 13–14 (Saltillo–Santa Catarina) for MXN 31,844 million incl. 16% IVA; works start 30 Sep 2025; 960 calendar-day term. Distinct from alstom_mexico_dmu_2025 rolling stock and siemens_sonda_mexico_etcs_2026 signaling.",
        "investment_type": "epc",
        "value": "31844000000",
        "currency": "MXN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "25.43",
        "lon": "-101.00",
        "geo_note": "Saltillo (Coahuila)–Santa Catarina (Nuevo León) passenger-rail segments 13–14.",
        "evidence": "documented",
        "source_id": "carso_fcc_saltillo_santa_catarina_20250915",
        "note": "Actor: FCC Construcción (Spain) 50% — allied (with Mexican CICSA). Contract MXN from Carso issuer notice; USD not converted.",
    },
    {
        "id": "fcc_cicsa_saltillo_santa_catarina_2025",
        "retrieved": "2026-10-01",
        "source_id": "carso_fcc_saltillo_santa_catarina_20250915",
        "url": "https://www.carso.com.mx/contrato-de-construccion-y-diseno-tren-de-pasajeros-segmentos-13-14-saltillo-santa-catarina/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "adjudicó al consorcio conformado por su subsidiaria Operadora Cicsa … y la empresa FCC Construcción, S.A. (FCC), un contrato … por un monto de $31,844 millones de pesos incluyendo el 16% de IVA. CICSA participa con el 50% y FCC con el 50%. El inicio de la obra será a partir del 30 de septiembre con un plazo de ejecución de 960 días naturales.",
        "note": "Opened Grupo Carso investor notice 15 Sep 2025.",
    },
    {
        "id": "carso_fcc_saltillo_santa_catarina_20250915",
        "type": "company",
        "chicago": "Grupo Carso, S.A.B. de C.V. “Contrato de Construcción y Diseño Tren de Pasajeros Segmentos 13-14 Saltillo-Santa Catarina.” Investor notice, 15 September 2025.",
        "url": "https://www.carso.com.mx/contrato-de-construccion-y-diseno-tren-de-pasajeros-segmentos-13-14-saltillo-santa-catarina/",
        "annotation": "CICSA–FCC MXN 31.844bn Saltillo–Santa Catarina rail civil award. Supports fcc_cicsa_saltillo_santa_catarina_2025.",
        "supports": ["fcc_cicsa_saltillo_santa_catarina_2025", "hunt_latam_rail_telecom"],
    },
)

# ---------------------------------------------------------------------------
# 14 energy/solar — Gonvarri Solar Steel Colombia 25 MW trackers
# ---------------------------------------------------------------------------
A(
    {
        "id": "gonvarri_solarsteel_colombia_25mw_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "allied",
        "counterpart": "Gonvarri Solar Steel — Colombia 25 MW 1P tracker supply",
        "country": "Colombia",
        "asset": "12 Mar 2026 Gonvarri Solar Steel: agreement to supply 1P single-row solar trackers for a 25 MW utility-scale PV project in Colombia; local support via Gonvarri Colombia. CapEx/USD and named site not disclosed on release. Distinct from Nextracker Casa dos Ventos / Libélula and Array Lupi Peru.",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "Colombia utility-scale PV site unnamed on supplier release — coordinates left blank.",
        "evidence": "documented",
        "source_id": "gonvarri_solarsteel_colombia_20260312",
        "note": "Actor: Gonvarri Solar Steel (Spain) — allied.",
    },
    {
        "id": "gonvarri_solarsteel_colombia_25mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "gonvarri_solarsteel_colombia_20260312",
        "url": "https://www.gsolarsteel.com/1p-solar-trackers-in-colombia/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Gonvarri Solar Steel … has announced a new agreement to supply its 1P single‑row solar tracking technology for a 25 MW solar project in Colombia. … The 25 MW installation will contribute to strengthening Colombia’s photovoltaic infrastructure",
        "note": "Opened Gonvarri Solar Steel press release 12 Mar 2026.",
    },
    {
        "id": "gonvarri_solarsteel_colombia_20260312",
        "type": "company",
        "chicago": "Gonvarri Solar Steel. “Gonvarri Solar Steel to Supply 1P Solar Trackers in Colombia.” Press release, 12 March 2026.",
        "url": "https://www.gsolarsteel.com/1p-solar-trackers-in-colombia/",
        "annotation": "Spanish tracker OEM 25 MW Colombia supply. Supports gonvarri_solarsteel_colombia_25mw_2026.",
        "supports": ["gonvarri_solarsteel_colombia_25mw_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 16 energy/wind — Mainstream Ckhúri Chile COD
# ---------------------------------------------------------------------------
A(
    {
        "id": "mainstream_ckhuri_cod_chile_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "Mainstream Renewable Power — Ckhúri Wind Farm COD",
        "country": "Chile",
        "asset": "12 May 2026 Mainstream: Ckhúri Wind Farm (Calama, Antofagasta) received CEN commercial-operation certificate; 109.2 MW with 26 Vestas turbines; part of Huemul Energía / Andes Renovables platform (Mainstream cites nine operational Chile assets totaling 1,222 MW). CapEx USD not on COD release. Distinct from vestas_dom_inocencio_br_2025 and Esquina do Vento.",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-22.45",
        "lon": "-68.93",
        "geo_note": "Ckhúri Wind Farm, Calama, Antofagasta Region.",
        "evidence": "documented",
        "source_id": "mainstream_ckhuri_cod_20260512",
        "note": "Actor: Mainstream Renewable Power (Ireland/Norway Aker-backed) — allied.",
    },
    {
        "id": "mainstream_ckhuri_cod_chile_2026",
        "retrieved": "2026-10-01",
        "source_id": "mainstream_ckhuri_cod_20260512",
        "url": "https://www.mainstreamrp.com/news/ckhuri-wind-farm-reaches-commercial-operation-date/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Ckhúri Wind Farm received the certificate confirming the commencement of commercial operations (COD) from the Coordinador Eléctrico Nacional … Located in Calama, Antofagasta Region, the 109.2 MW wind farm comprises 26 Vestas turbines",
        "note": "Opened Mainstream Renewable Power news 12 May 2026.",
    },
    {
        "id": "mainstream_ckhuri_cod_20260512",
        "type": "company",
        "chicago": "Mainstream Renewable Power. “Ckhúri Wind Farm Reaches Commercial Operation Date.” News release, 12 May 2026.",
        "url": "https://www.mainstreamrp.com/news/ckhuri-wind-farm-reaches-commercial-operation-date/",
        "annotation": "Mainstream Ckhúri 109.2 MW Chile COD. Supports mainstream_ckhuri_cod_chile_2026.",
        "supports": ["mainstream_ckhuri_cod_chile_2026", "hunt_energy_wind"],
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
        "hunt_res_graphite": "Cycle 59: equal budget; South Star July ops/PO / Graphcoa Urbix already (miss).",
        "hunt_res_water": "Cycle 59: logged nadbank_baja_rosarito_distrib_82m_2026 (U.S. NADBank).",
        "hunt_br_power_equip": "Cycle 59: logged powerchina_edp_piaui_500kv_cod_2026 (PRC).",
        "hunt_infra_port_ownership": "Cycle 59: equal budget; APM Callao 3B / DP World Callao addendum / Guaymas already (miss).",
        "hunt_infra_bridges_roads": "Cycle 59: equal budget; Aldesa Chiapas / CRBC Arequipa / Quinto Puente already (miss).",
        "hunt_res_lithium": "Cycle 59: logged lilac_kachi_dia_permit_2026 (U.S. Lilac).",
        "hunt_energy_other_renewables": "Cycle 59: equal budget; Ormat Dominica COD / Cerro Pabellón already (miss).",
        "hunt_infra_port_cranes": "Cycle 59: logged konecranes_iquique_esp10_2025 (allied).",
        "hunt_fenb_araxa": "Cycle 59: equal budget; St George CEFET pilot / CBMM Toshiba planned already (miss).",
        "hunt_res_nickel": "Cycle 59: equal budget; Jervois / Centaurus / DFC Piauí / Araguaia C&M already (miss).",
        "hunt_infra_engineering_epc": "Cycle 59: logged baker_hughes_petrobras_wells_santos_2026 (U.S.).",
        "hunt_latam_rail_telecom": "Cycle 59: logged fcc_cicsa_saltillo_santa_catarina_2025 (allied FCC).",
        "hunt_energy_fission_smr": "Cycle 59: equal budget; Peru FIRST partner / Colombia–US MOU / Meitner already (miss).",
        "hunt_energy_solar": "Cycle 59: logged gonvarri_solarsteel_colombia_25mw_2026 (allied).",
        "hunt_res_copper": "Cycle 59: equal budget; Freeport El Abra SEIA / Zijin La Arena already (miss).",
        "hunt_energy_wind": "Cycle 59: logged mainstream_ckhuri_cod_chile_2026 (allied).",
        "hunt_infra_building_materials": "Cycle 59: equal budget; Sinoma Cruz Azul / Cibao / Panam already (miss).",
        "hunt_res_balsa": "Cycle 59: equal budget; AIMA 2025 mfr destinations / Plantabal→Baltek already (miss).",
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
    print("Cycle 59 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
