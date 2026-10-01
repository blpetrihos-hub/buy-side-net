#!/usr/bin/env python3
"""Cycle 34 hunt: shuffle_seed=20261034; equal budget across 18 subcategories."""
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


# seed 20261034 order:
# building_materials, lithium, graphite, other_renewables, port_cranes, wind,
# niobium, port_ownership, power_plants_grid, copper, engineering_epc, water,
# fission_smr, bridges_roads, solar, balsa, nickel, rail

# 1 infrastructure/building_materials — InterCement / LATCEM–Redwood–Moneda new money
A(
    {
        "id": "intercement_latcem_newmoney_2026",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "other",
        "counterpart": "LATCEM / Redwood Capital / Moneda Patria — InterCement control + Loma Negra",
        "country": "Brazil",
        "asset": "7 Apr 2026 Global Cement (citing Bloomberg Línea): completion of second phase of InterCement judicial reorganisation; consortium LATCEM (~39%), Redwood Capital Management (~27%), Moneda Patria Investments (~24%) takes control of Brazil-based InterCement and indirect control of Argentina Loma Negra; trio injects ~USD 110 million into InterCement; Marcelo Mindlin (LATCEM) appointed Loma Negra president",
        "investment_type": "ownership_equity",
        "value": "110000000",
        "currency": "USD",
        "value_usd": "110000000",
        "fx_usd": "1",
        "fx_date": "2026-04-07",
        "year": "2026",
        "status": "active",
        "lat": "-23.55",
        "lon": "-46.63",
        "geo_note": "InterCement HQ São Paulo (company geography; approximate pin). Assets span Brazil cement plants + Argentina Loma Negra.",
        "evidence": "proxy",
        "source_id": "globalcement_intercement_20260407",
        "note": "Actor mix: LATCEM (Argentine Mindlin) lead + U.S. Redwood + Moneda Patria — coded other (LatAm-led control). UNVERIFIED proxy: Global Cement trade press summarizing Bloomberg Línea on USD 110m inject and ownership split. Distinct from huaxin_embu / holcim_cemex_colombia / sinoma_loma_negra_amali_epc.",
    },
    {
        "id": "intercement_latcem_newmoney_2026",
        "retrieved": "2026-10-01",
        "source_id": "globalcement_intercement_20260407",
        "url": "https://globalcement.com/news/20621-consortium-takes-control-of-intercement-and-loma-negra",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "The trio of investors has injected US$110m into InterCement. They now hold around 39%, 27% and 24% respectively of the company.",
        "note": "Opened Global Cement 7 Apr 2026 trade summary (Bloomberg Línea). Mark UNVERIFIED proxy.",
    },
    {
        "id": "globalcement_intercement_20260407",
        "type": "trade_press",
        "chicago": "Global Cement. “Consortium takes control of InterCement and Loma Negra.” 7 April 2026.",
        "url": "https://globalcement.com/news/20621-consortium-takes-control-of-intercement-and-loma-negra",
        "annotation": "Trade press on InterCement reorganisation control transfer and USD 110m inject. Supports intercement_latcem_newmoney_2026.",
        "supports": ["intercement_latcem_newmoney_2026", "hunt_infra_building_materials"],
    },
)

# 2 resources/lithium — Galan HMW RIGI
A(
    {
        "id": "galan_hmw_rigi_2025",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "Galán Litio SA / Galán SDE (Galan Lithium ASX:GLN) — Hombre Muerto Oeste HMW",
        "country": "Argentina",
        "asset": "Ministerio de Economía Resolución 1271/2025 (Boletín Oficial 28 Aug 2025): RIGI adhesion approved for Proyecto Hombre Muerto Oeste (HMW) — 12,000 tpa LCE; declared computable investment USD 217,090,266 from 1 Jan 2025; ~48-month construction; adhesion date 17 Jul 2025; minimum-investment deadline 31 Dec 2029; Catamarca / Salar del Hombre Muerto (~90 km N of Antofagasta de la Sierra)",
        "investment_type": "greenfield_mine",
        "value": "217090266",
        "currency": "USD",
        "value_usd": "217090266",
        "fx_usd": "1",
        "fx_date": "2025-08-27",
        "year": "2025",
        "status": "active",
        "lat": "-25.4",
        "lon": "-67.0",
        "geo_note": "Salar del Hombre Muerto, Catamarca (Boletín geography; approximate pin).",
        "evidence": "documented",
        "source_id": "bo_galan_hmw_rigi_20250828",
        "note": "Actor: Galan Lithium (ASX Australian) via Galán Litio SA — allied. Official Boletín Oficial RESOL-2025-1271-APN-MEC. Distinct from rio_tinto_fenix_1b_rigi_2026 / posco_sal_de_oro_ii_rigi_2026 / zijin_liex_tres_quebradas_rigi_2026.",
    },
    {
        "id": "galan_hmw_rigi_2025",
        "retrieved": "2026-10-01",
        "source_id": "bo_galan_hmw_rigi_20250828",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/330470/20250828",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "el Proyecto implicará una inversión total en activos computables, a partir del 1° de enero de 2025 de doscientos diecisiete millones noventa mil doscientos sesenta y seis dólares estadounidenses (USD 217.090.266)",
        "note": "Opened Boletín Oficial Resolución 1271/2025 Spanish text.",
    },
    {
        "id": "bo_galan_hmw_rigi_20250828",
        "type": "government",
        "chicago": "Ministerio de Economía (Argentina). “Resolución 1271/2025 — Régimen de Incentivo para Grandes Inversiones: Proyecto Hombre Muerto Oeste (HMW).” Boletín Oficial, 28 August 2025.",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/330470/20250828",
        "annotation": "Official RIGI approval of Galan HMW with USD 217.09m declared investment. Supports galan_hmw_rigi_2025.",
        "supports": ["galan_hmw_rigi_2025", "hunt_res_lithium"],
    },
)

# 3 resources/graphite — miss (Graphcoa Jordânia / Atlas / South Star already)

# 4 energy/other_renewables — Grupo Enal Celaya geothermal
A(
    {
        "id": "enal_celaya_geothermal_80m_2025",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "other",
        "counterpart": "Grupo Enal (Grupo Carso / Carlos Slim) — Celaya geothermal concession",
        "country": "Mexico",
        "asset": "1 Sep 2025 SENER 30-year geothermal concession title for Celaya Geothermal Area (Guanajuato) published in DOF; Grupo Enal (Energías Alternas, Estudios y Proyectos — Carso) developing ~26 MW geothermal plant; UNVERIFIED press cites estimated investment ~USD 80 million",
        "investment_type": "greenfield_generation",
        "value": "80000000",
        "currency": "USD",
        "value_usd": "80000000",
        "fx_usd": "1",
        "fx_date": "2025-09-01",
        "year": "2025",
        "status": "active",
        "lat": "20.53",
        "lon": "-100.81",
        "geo_note": "Celaya, Guanajuato (concession geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "mnd_enal_celaya_20250908",
        "note": "Actor: Grupo Carso / Slim (Mexican private) — other. UNVERIFIED proxy: Mexico News Daily 8 Sep 2025 summarizing DOF concession and USD 80m plant estimate (also El Financiero). Distinct from ormat_dominica / lageo_chinameca.",
    },
    {
        "id": "enal_celaya_geothermal_80m_2025",
        "retrieved": "2026-10-01",
        "source_id": "mnd_enal_celaya_20250908",
        "url": "https://www.mexiconewsdaily.com/business/slim-subsidiary-granted-permit-80-million-geothermal-plot/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "Energías Alternas, Estudios y Proyectos (Grupo Enal), a subsidiary of Slim’s Grupo Carso, has been granted a 30-year concession to develop geothermal resources for electricity generation in Celaya … The Celaya plant is expected to have an installed capacity of 26 megawatts.",
        "note": "Opened Mexico News Daily 8 Sep 2025. Capex USD 80m is press estimate — UNVERIFIED proxy.",
    },
    {
        "id": "mnd_enal_celaya_20250908",
        "type": "trade_press",
        "chicago": "Mexico News Daily. “Slim subsidiary granted 30-year concession to develop geothermal plot in Guanajuato.” 8 September 2025.",
        "url": "https://www.mexiconewsdaily.com/business/slim-subsidiary-granted-permit-80-million-geothermal-plot/",
        "annotation": "Press on Enal/Carso Celaya geothermal concession and ~USD 80m plant. Supports enal_celaya_geothermal_80m_2025.",
        "supports": ["enal_celaya_geothermal_80m_2025", "hunt_energy_other_renewables"],
    },
)

# 5 infrastructure/port_cranes — SSA Guaymas STS + eRTG
A(
    {
        "id": "ssa_guaymas_sts_ertg_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "us",
        "counterpart": "SSA Marine México (Carrix / SSA Marine) — Guaymas multi-use terminal cranes",
        "country": "Mexico",
        "asset": "Sep 2026 delivery of two Super Post-Panamax STS cranes (~62 m outreach; 65 t under spreader) + two electric RTGs to SSA Marine México’s new Guaymas terminal; operations targeted in coming weeks; terminal to handle containers, general cargo, and automobiles. Capex USD not disclosed on opened page — value blank",
        "investment_type": "equipment_procurement",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "27.92",
        "lon": "-110.89",
        "geo_note": "Port of Guaymas, Sonora (SSA Marine delivery geography).",
        "evidence": "documented",
        "source_id": "maritimepro_ssa_guaymas_20260921",
        "note": "Actor: SSA Marine / Carrix (U.S.-headquartered terminal operator) — us. Maritime Professional 21 Sep 2026 company-sourced delivery notice. OEM not named on page. Distinct from zpmc_santos_brasil / konecranes_arica / portonave_electric_fleet.",
    },
    {
        "id": "ssa_guaymas_sts_ertg_2026",
        "retrieved": "2026-10-01",
        "source_id": "maritimepro_ssa_guaymas_20260921",
        "url": "https://www.maritimeprofessional.com/news/marine-xico-guaymas-terminal-received-423079",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "This week, two Ship-to-Shore (STS) Super Post-Panamax cranes and two Electric Rubber-Tired Gantry (ERTG) cranes arrived at SSA Marine México’s new Guaymas terminal … approximate outreach of 62 meters and a lifting capacity of 65 tons under spreader",
        "note": "Opened Maritime Professional 21 Sep 2026.",
    },
    {
        "id": "maritimepro_ssa_guaymas_20260921",
        "type": "trade_press",
        "chicago": "Maritime Professional. “SSA Marine México Guaymas Terminal Received STS, ERTG Cranes.” 21 September 2026.",
        "url": "https://www.maritimeprofessional.com/news/marine-xico-guaymas-terminal-received-423079",
        "annotation": "Trade notice of SSA Guaymas STS/eRTG delivery. Supports ssa_guaymas_sts_ertg_2026.",
        "supports": ["ssa_guaymas_sts_ertg_2026", "hunt_infra_port_cranes"],
    },
)

# 6 energy/wind — miss (Vestas Dom Inocêncio / Goldwind Sento Sé / Envision already)
# 7 resources/niobium — miss (CBMM R$13bn / CMOC already)
# 8 infrastructure/port_ownership — miss (Tecon 10 / DP World Callao still pre-award)
# 9 energy/power_plants_grid — miss (thick; equal-budget pass)

# 10 resources/copper — MMG Las Bambas 2026 capex guidance
A(
    {
        "id": "mmg_las_bambas_2026_capex",
        "layer": "resources",
        "subcategory": "copper",
        "side": "prc",
        "counterpart": "MMG Limited — Las Bambas 2026 sustaining/growth capex",
        "country": "Peru",
        "asset": "3 Mar 2026 MMG 2025 Annual Results HKEX announcement: 2026 group capex guidance USD 1.6–1.7 billion including USD 800–850 million for Las Bambas (capitalised mining, Ferrobamba pit infrastructure, and tailings dam facility expansion). Row value uses USD 800 million floor of disclosed range",
        "investment_type": "brownfield_expansion",
        "value": "800000000",
        "currency": "USD",
        "value_usd": "800000000",
        "fx_usd": "1",
        "fx_date": "2026-03-03",
        "year": "2026",
        "status": "active",
        "lat": "-14.083",
        "lon": "-72.317",
        "geo_note": "Las Bambas, Cotabambas/Grau, Apurímac (MMG operations geography).",
        "evidence": "documented",
        "source_id": "mmg_annual_results_20260303",
        "note": "Actor: MMG (China Minmetals–controlled) — prc. Company HKEX annual-results announcement. Distinct from blank-value mmg_las_bambas_peru ownership presence row; this captures 2026 capex guidance.",
    },
    {
        "id": "mmg_las_bambas_2026_capex",
        "retrieved": "2026-10-01",
        "source_id": "mmg_annual_results_20260303",
        "url": "https://www.mmg.com/content/uploads/2026/03/e_2026-03-03_2025-Annual-Results.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "2026 Capital Expenditure: Total capital expenditure is expected to be between US$1,600 million and US$1,700 million, including US$800-850 million for Las Bambas (capitalised mining, Ferrobamba pit infrastructure, and tailings dam facility expansion)",
        "note": "Opened MMG HKEX annual results PDF 3 Mar 2026.",
    },
    {
        "id": "mmg_annual_results_20260303",
        "type": "company",
        "chicago": "MMG Limited. “Announcement on 2025 Annual Results.” 3 March 2026.",
        "url": "https://www.mmg.com/content/uploads/2026/03/e_2026-03-03_2025-Annual-Results.pdf",
        "annotation": "Company annual results with Las Bambas 2026 capex guidance USD 800–850m. Supports mmg_las_bambas_2026_capex.",
        "supports": ["mmg_las_bambas_2026_capex", "hunt_res_copper"],
    },
)

# 11 infrastructure/engineering_epc — miss
# 12 resources/water — miss
# 13 energy/fission_smr — miss (Brazil microreactor / Meitner already)

# 14 infrastructure/bridges_roads — Longitudinal Sierra Tramo 4
A(
    {
        "id": "sierra_tramo4_vial_centro_2025",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "other",
        "counterpart": "Concesionaria Vial del Centro (CASA / Hidalgo e Hidalgo) — Longitudinal de la Sierra Tramo 4",
        "country": "Peru",
        "asset": "25 Jul 2025 PROINVERSIÓN award (on MTC mandate) of Longitudinal de la Sierra Tramo 4 APP (~965 km; Junín, Huancavelica, Ica, Ayacucho, Apurímac) to Concesionaria Vial del Centro; estimated total investment USD 1,582 million; 25-year concession: Evitamiento San Clemente 5.2 km + rehab/improvement Huancayo–Izcuchaca–Mayocc 179.3 km + periodic maintenance ~780.7 km",
        "investment_type": "ppp_concession",
        "value": "1582000000",
        "currency": "USD",
        "value_usd": "1582000000",
        "fx_usd": "1",
        "fx_date": "2025-07-25",
        "year": "2025",
        "status": "active",
        "lat": "-12.8",
        "lon": "-74.2",
        "geo_note": "Longitudinal de la Sierra Tramo 4 corridor mid-point (PROINVERSIÓN geography; approximate).",
        "evidence": "documented",
        "source_id": "proinversion_sierra_t4_20250725",
        "note": "Actor: Ecuadorian Hidalgo e Hidalgo + CASA vehicle — other (Andean private, not US/PRC/allied OECD). Official PROINVERSIÓN Spanish award notice. Distinct from erg_estanquillo_popayan_2026 / crbc_arequipa_la_joya_2026 / sacyr_ruta57.",
    },
    {
        "id": "sierra_tramo4_vial_centro_2025",
        "retrieved": "2026-10-01",
        "source_id": "proinversion_sierra_t4_20250725",
        "url": "https://www.gob.pe/institucion/proinversion/noticias/1214928-gobierno-adjudica-concesion-de-la-longitudinal-de-la-sierra-tramo-4-que-beneficiara-a-cinco-regiones",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "La buena pro fue otorgada a Concesionaria Vial del Centro, tras presentar la mejor oferta técnica y económica para ejecutar esta Asociación Público-Privada (APP), cuya inversión total estimada asciende a US$ 1582 millones.",
        "note": "Opened PROINVERSIÓN / gob.pe Spanish award notice 25 Jul 2025.",
    },
    {
        "id": "proinversion_sierra_t4_20250725",
        "type": "government",
        "chicago": "PROINVERSIÓN (Peru). “Gobierno adjudica concesión de la Longitudinal de la Sierra Tramo 4 que beneficiará a cinco regiones.” 25 July 2025.",
        "url": "https://www.gob.pe/institucion/proinversion/noticias/1214928-gobierno-adjudica-concesion-de-la-longitudinal-de-la-sierra-tramo-4-que-beneficiara-a-cinco-regiones",
        "annotation": "Official award of Sierra Tramo 4 APP at USD 1.582bn. Supports sierra_tramo4_vial_centro_2025.",
        "supports": ["sierra_tramo4_vial_centro_2025", "hunt_infra_bridges_roads"],
    },
)

# 15 energy/solar — Trina Sidón Solar SEA filing
A(
    {
        "id": "trina_sidon_solar_100m_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "Trina Solar — Parque Fotovoltaico Sidón Solar (Biobío / Ñuble)",
        "country": "Chile",
        "asset": "Jun 2025 SEIA/SEA entry for Parque Fotovoltaico Sidón Solar in Cabrero (Biobío) and Pemuco (Ñuble): ~USD 100 million estimated investment; ~162.55 MWdc installed / ~150 MW net injection; 224,208 × 725 W panels; ~5.7 km 220 kV line to S/E Entre Ríos; execution targeted Oct 2027; ~33-year life. UNVERIFIED press summarizing SEA filing",
        "investment_type": "greenfield_generation",
        "value": "100000000",
        "currency": "USD",
        "value_usd": "100000000",
        "fx_usd": "1",
        "fx_date": "2025-06-25",
        "year": "2025",
        "status": "active",
        "lat": "-37.05",
        "lon": "-72.35",
        "geo_note": "Cabrero–Pemuco corridor, Biobío/Ñuble (SEA filing geography via press; approximate mid-pin).",
        "evidence": "proxy",
        "source_id": "revistaei_sidon_solar_20250625",
        "note": "Actor: Trina Solar (PRC) — prc. UNVERIFIED proxy: Revista Electricidad 25 Jun 2025 summarizing SEA entry and USD 100m. Distinct from trina_pillanco_biobio_2026.",
    },
    {
        "id": "trina_sidon_solar_100m_2025",
        "retrieved": "2026-10-01",
        "source_id": "revistaei_sidon_solar_20250625",
        "url": "https://www.revistaei.cl/proyecto-fotovoltaico-emplazado-en-regiones-del-biobio-y-nuble-ingresa-al-sea/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "El proyecto “Parque Fotovoltaico Sidon Solar” ingresó recientemente al Servicio de Evaluación Ambiental (SEA). La iniciativa contempla una inversión de US$100 millones … capacidad instalada de 162,55 MW (150 MW de potencia neta a inyectar)",
        "note": "Opened Revista Electricidad 25 Jun 2025. Mark UNVERIFIED proxy pending SEA PDF.",
    },
    {
        "id": "revistaei_sidon_solar_20250625",
        "type": "trade_press",
        "chicago": "Revista Electricidad. “Proyecto fotovoltaico emplazado en regiones del Biobío y Ñuble ingresa al SEA.” 25 June 2025.",
        "url": "https://www.revistaei.cl/proyecto-fotovoltaico-emplazado-en-regiones-del-biobio-y-nuble-ingresa-al-sea/",
        "annotation": "Trade press on Trina Sidón Solar SEA entry and USD 100m. Supports trina_sidon_solar_100m_2025.",
        "supports": ["trina_sidon_solar_100m_2025", "hunt_energy_solar"],
    },
)

# 16 resources/balsa — miss (WITS/AIMA already)
# 17 resources/nickel — miss (BNDES Piauí / Jaguar / Santa Rita already)
# 18 infrastructure/rail — miss (CRCC Batuco / OHLA L9 already)


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
        "hunt_infra_building_materials": "Cycle 34: logged intercement_latcem_newmoney_2026 (proxy USD 110m).",
        "hunt_res_lithium": "Cycle 34: logged galan_hmw_rigi_2025 (documented USD 217.09m).",
        "hunt_res_graphite": "Cycle 34: equal budget; Graphcoa/Atlas/South Star already (miss).",
        "hunt_energy_other_renewables": "Cycle 34: logged enal_celaya_geothermal_80m_2025 (proxy USD 80m).",
        "hunt_infra_port_cranes": "Cycle 34: logged ssa_guaymas_sts_ertg_2026.",
        "hunt_energy_wind": "Cycle 34: equal budget; Vestas/Goldwind/Envision already (miss).",
        "hunt_fenb_araxa": "Cycle 34: equal budget; CBMM R$13bn already (miss).",
        "hunt_infra_port_ownership": "Cycle 34: equal budget; Tecon 10 / DP World Callao still pre-award (miss).",
        "hunt_br_power_equip": "Cycle 34: equal budget; avoid over-invest (miss).",
        "hunt_res_copper": "Cycle 34: logged mmg_las_bambas_2026_capex (documented USD 800m floor).",
        "hunt_infra_engineering_epc": "Cycle 34: equal budget; Ausenco/Worley already (miss).",
        "hunt_res_water": "Cycle 34: equal budget; Acciona/Sacyr/Almar already (miss).",
        "hunt_energy_fission_smr": "Cycle 34: equal budget; Meitner/Brazil microreactor already (miss).",
        "hunt_infra_bridges_roads": "Cycle 34: logged sierra_tramo4_vial_centro_2025 (documented USD 1.582bn).",
        "hunt_energy_solar": "Cycle 34: logged trina_sidon_solar_100m_2025 (proxy USD 100m).",
        "hunt_res_balsa": "Cycle 34: equal budget; WITS/AIMA already (miss).",
        "hunt_res_nickel": "Cycle 34: equal budget; BNDES Piauí / Jaguar already (miss).",
        "hunt_latam_rail_telecom": "Cycle 34: equal budget; CRCC Batuco / OHLA L9 already (miss).",
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
    print("Cycle 34 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 34 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
