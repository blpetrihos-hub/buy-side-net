#!/usr/bin/env python3
"""Cycle 61 hunt: shuffle_seed=20261061; equal budget; U.S. ≥1/3; thin after.

Order: port_ownership, copper, water, solar, lithium, building_materials, rail,
nickel, fission_smr, other_renewables, wind, niobium, engineering_epc,
port_cranes, balsa, power_plants_grid, graphite, bridges_roads.
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
# 2 resources/copper — Chinalco Los Calatos acquisition (prc, proxy)
# ---------------------------------------------------------------------------
A(
    {
        "id": "chinalco_los_calatos_peru_2026",
        "layer": "resources",
        "subcategory": "copper",
        "side": "prc",
        "counterpart": "Chinalco — acquisition of Minera Hampton Perú / Los Calatos Cu-Mo (Moquegua)",
        "country": "Peru",
        "asset": "Jul 2026 press: Chinalco acquires 100% of Minera Hampton Perú (ex-CD Capital), owner of Los Calatos copper-molybdenum greenfield in Mariscal Nieto, Moquegua. Press values deal >US$200m; Indecopi phase-1 clearance cited. Underground plan ~60,000 t/y refined Cu; ~24-year life; construction targeted 2027 / production ~2029 pending EIA-d. Distinct from chinalco_toromocho_peru / chinalco_toromocho_its3_700m_2026.",
        "investment_type": "ownership_equity",
        "value": "200000000",
        "currency": "USD",
        "value_usd": "200000000",
        "fx_usd": "1",
        "fx_date": "2026-07-07",
        "year": "2026",
        "status": "active",
        "lat": "-17.19",
        "lon": "-70.93",
        "geo_note": "Los Calatos / Mariscal Nieto Province, Moquegua (press geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "proactivo_chinalco_calatos_20260707",
        "note": "Actor: Chinalco / Aluminum Corporation of China (PRC) — prc. ProActivo Spanish press; deal value >US$200m is UNVERIFIED press proxy (no company filing opened).",
    },
    {
        "id": "chinalco_los_calatos_peru_2026",
        "retrieved": "2026-10-01",
        "source_id": "proactivo_chinalco_calatos_20260707",
        "url": "https://proactivo.com.pe/chinalco-expande-sus-operaciones-en-peru-con-la-compra-de-los-calatos/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "La empresa china Chinalco —titular de la mina Toromocho en la región Junín— concretó la adquisición de Minera Hampton Perú, propietaria del proyecto Los Calatos en Moquegua. La operación, valorizada en más de US$ 200 millones, ya cuenta con la aprobación en primera fase del … Indecopi.",
        "note": "Opened ProActivo Spanish press on Chinalco–Hampton/Los Calatos.",
    },
    {
        "id": "proactivo_chinalco_calatos_20260707",
        "type": "press",
        "chicago": "ProActivo. “Chinalco Expande Sus Operaciones en Perú con la Adquisición del Proyecto Cuprífero Los Calatos.” 7 July 2026.",
        "url": "https://proactivo.com.pe/chinalco-expande-sus-operaciones-en-peru-con-la-compra-de-los-calatos/",
        "annotation": "Press on Chinalco acquisition of Los Calatos via Minera Hampton (>US$200m UNVERIFIED). Supports chinalco_los_calatos_peru_2026.",
        "supports": ["chinalco_los_calatos_peru_2026", "hunt_res_copper"],
    },
)

# ---------------------------------------------------------------------------
# 4 energy/solar — POWERCHINA Conchagua 30 MW El Salvador EPC (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "powerchina_conchagua_salvador_30mw_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "POWERCHINA — Conchagua 30 MW PV EPC (La Unión Bay)",
        "country": "El Salvador",
        "asset": "9 Mar 2026 (company 23 Mar release): POWERCHINA signs EPC contract for Conchagua 30 MW centralized PV — described as El Salvador’s first large-scale centralized PV; scope plant through 34.5/115 kV booster station (engineering, procurement, construction, installation, commissioning, COD). Expected ~71.2 GWh/y. Company’s Central America new-energy market entry. Distinct from powerchina_huayra_peru_96p9mw_2026 / francisco_juana.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "13.28",
        "lon": "-87.86",
        "geo_note": "Conchagua / La Unión Bay region, southeast of San Salvador (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "powerchina_conchagua_20260323",
        "note": "Actor: POWERCHINA (PRC) — prc. Company English release. CapEx USD not disclosed.",
    },
    {
        "id": "powerchina_conchagua_salvador_30mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "powerchina_conchagua_20260323",
        "url": "https://en.powerchina.cn/2026-03/23/c_829061.htm",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "POWERCHINA signed the contract for the Conchagua 30 MW Photovoltaic (PV) Project in El Salvador on March 9. … Located in the region of La Unión Bay … this project holds pioneering significance as the country’s first large-scale centralized PV power plant. … expected to generate an average of 71.2 million kWh of electricity annually.",
        "note": "Opened POWERCHINA English company news on Conchagua contract.",
    },
    {
        "id": "powerchina_conchagua_20260323",
        "type": "company",
        "chicago": "Power Construction Corporation of China. “POWERCHINA Signs Contract for Conchagua 30 MW PV Project in El Salvador.” 23 March 2026.",
        "url": "https://en.powerchina.cn/2026-03/23/c_829061.htm",
        "annotation": "POWERCHINA Conchagua 30 MW El Salvador PV EPC contract. Supports powerchina_conchagua_salvador_30mw_2026.",
        "supports": ["powerchina_conchagua_salvador_30mw_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 4b energy/solar — IDB Invest Genneia Argentina renewables+BESS (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "idb_invest_genneia_95m_2025",
        "layer": "energy",
        "subcategory": "solar",
        "side": "allied",
        "counterpart": "IDB Invest — Genneia renewable expansion + Alma-GBA BESS (Argentina)",
        "country": "Argentina",
        "asset": "4 Nov 2025 approval / 30 Dec 2025 signing: IDB Invest USD 95 million loan to Genneia to expand renewable generation (~340 MW) and install 40 MW batteries awarded under Alma-GBA storage initiative. Distinct from ifc_pcr_olavarria_wind_2026 / vestas_argentina_217mw_2025.",
        "investment_type": "financing",
        "value": "95000000",
        "currency": "USD",
        "value_usd": "95000000",
        "fx_usd": "1",
        "fx_date": "2025-12-30",
        "year": "2025",
        "status": "active",
        "lat": "",
        "lon": "",
        "geo_note": "Argentina multi-site Genneia portfolio — no single plant pin on IDB Invest summary.",
        "evidence": "documented",
        "source_id": "idb_invest_genneia_15408_2025",
        "note": "Actor: IDB Invest (multilateral; coded allied) financing Genneia (Argentina) — allied. Official IDB Invest project page amount USD 95m (not press USD 185m package).",
    },
    {
        "id": "idb_invest_genneia_95m_2025",
        "retrieved": "2026-10-01",
        "source_id": "idb_invest_genneia_15408_2025",
        "url": "https://idbinvest.org/en/projects/supporting-expansion-renewable-energy-capacity-argentina-genneia",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Financing amount USD $ 95,000,000 … The transaction aims to finance the expansion of renewable energy generation capacity throughout the country (approximately 340 MW), as well as the installation of 40 MW of batteries, awarded under Argentina's first large-scale storage initiative, Alma-GBA.",
        "note": "Opened IDB Invest project page 15408-01.",
    },
    {
        "id": "idb_invest_genneia_15408_2025",
        "type": "ifp",
        "chicago": "IDB Invest. “Supporting the Expansion of Renewable Energy Capacity in Argentina with Genneia.” Project 15408-01, approved 4 November 2025, signed 30 December 2025.",
        "url": "https://idbinvest.org/en/projects/supporting-expansion-renewable-energy-capacity-argentina-genneia",
        "annotation": "IDB Invest USD 95m Genneia Argentina renewables + Alma-GBA BESS. Supports idb_invest_genneia_95m_2025.",
        "supports": ["idb_invest_genneia_95m_2025", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 13 infrastructure/engineering_epc — Honeywell UOP ETJ for Petrobras REPLAN (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "honeywell_petrobras_etj_replan_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "us",
        "counterpart": "Honeywell UOP — Ethanol-to-Jet process technology for Petrobras REPLAN (São Paulo)",
        "country": "Brazil",
        "asset": "14 Apr 2026: Honeywell announces Petrobras selected Honeywell UOP Ethanol-to-Jet (ETJ) process technology for project development at REPLAN refinery (São Paulo). Once approved, up to 10,000 bpd SAF — first large-scale ETJ in Latin America. Complements prior Honeywell UOP HEFA license at RPBC Cubatão (2024). Distinct from powerchina_ufn3_petrobras_epc_2026.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.19",
        "lon": "-47.29",
        "geo_note": "Petrobras REPLAN refinery, Paulínia / São Paulo area (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "honeywell_petrobras_etj_20260414",
        "note": "Actor: Honeywell (U.S.) process-technology licensor — us. Company press. CapEx/FID pending approval; technology-selection row.",
    },
    {
        "id": "honeywell_petrobras_etj_replan_2026",
        "retrieved": "2026-10-01",
        "source_id": "honeywell_petrobras_etj_20260414",
        "url": "https://www.honeywell.com/us/en/press/2026/04/honeywell-to-fuel-petrobras-first-large-scale-ethanol-to-jet-project-in-latin-america",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Honeywell … announced that Petrobras has selected Honeywell UOP’s Ethanol-to-Jet (ETJ) process technology for project development at its REPLAN refinery in São Paulo, Brazil. Once approved, the project will deliver up to 10,000 barrels per day of sustainable aviation fuel (SAF), representing the first large-scale ETJ initiative in Latin America.",
        "note": "Opened Honeywell English press 14 Apr 2026.",
    },
    {
        "id": "honeywell_petrobras_etj_20260414",
        "type": "company",
        "chicago": "Honeywell. “Honeywell to Fuel Petrobras’ First, Large-Scale Ethanol-To-Jet Project in Latin America.” Press release, 14 April 2026.",
        "url": "https://www.honeywell.com/us/en/press/2026/04/honeywell-to-fuel-petrobras-first-large-scale-ethanol-to-jet-project-in-latin-america",
        "annotation": "Honeywell UOP ETJ selected for Petrobras REPLAN SAF project. Supports honeywell_petrobras_etj_replan_2026.",
        "supports": ["honeywell_petrobras_etj_replan_2026", "hunt_infra_engineering_epc"],
    },
)

# ---------------------------------------------------------------------------
# 16 energy/power_plants_grid — Lindsayca Consorcio Manzanillo Energy Block 2 (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "lindsayca_manzanillo_block2_dr_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "Lindsayca / Consorcio Manzanillo Energy — Manzanillo Block 2 ~420 MW CCGT (Montecristi)",
        "country": "Dominican Republic",
        "asset": "MEM R-MEM-LCG-017-2024 and 2026 financing close: Consorcio Manzanillo Energy (Coastal Petroleum Dominicana, Manzanillo Energy, Lindsayca Inc.) develops Block 2 ~420 MW net CCGT at Pepillo Salcedo / Manzanillo Bay, fueled via Block 1 LNG terminal. Part of Manzanillo Gas & Power complex totaling ~840 MW; Presidency notes USD 1.067bn financing close (Citi/JPMorgan/IDB Invest/CAF). Distinct from exim_guyana_gte_527m_2025 / lindsayca_borinquen_i_em_2026.",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "19.70",
        "lon": "-71.74",
        "geo_note": "Pepillo Salcedo / Bahía de Manzanillo, Montecristi Province (MEM/Presidency geography; approximate pin).",
        "evidence": "documented",
        "source_id": "mem_manzanillo_block2_2024",
        "note": "Actor: Lindsayca Inc. (Houston, U.S.) consortium partner — us. MEM resolution names Lindsayca as Block 2 adjudicatario member; Presidency financing close is complex-level (do not attribute full USD 1.067bn solely to Block 2).",
    },
    {
        "id": "lindsayca_manzanillo_block2_dr_2026",
        "retrieved": "2026-10-01",
        "source_id": "mem_manzanillo_block2_2024",
        "url": "https://mem.gob.do/transparencia/wp-content/uploads/2018/10/Resolucion-Num.-R-MEM-LCG-017-2024-CONSORCIO-MANZANILLO-ENERGY-SA.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "declarado al consorcio ganador \"MANZANILLO ENERGY, S.A.S., COASTAL PETROLEUM DOMINICANA S.A., Y LINDSAYCA, INC, como ADJUDICATARIO, del Bloque 2 compuesta de una central térmica de ciclo combinado con capacidad de aproximadamente 420MW netos",
        "note": "Opened Dominican MEM resolution PDF naming Lindsayca on Block 2 award.",
    },
    {
        "id": "mem_manzanillo_block2_2024",
        "type": "government",
        "chicago": "Dominican Republic Ministerio de Energía y Minas. “Resolución Núm. R-MEM-LCG-017-2024 — Consorcio Manzanillo Energy, S.A.” 2024.",
        "url": "https://mem.gob.do/transparencia/wp-content/uploads/2018/10/Resolucion-Num.-R-MEM-LCG-017-2024-CONSORCIO-MANZANILLO-ENERGY-SA.pdf",
        "annotation": "MEM award of Manzanillo Block 2 CCGT to consortium including Lindsayca. Supports lindsayca_manzanillo_block2_dr_2026.",
        "supports": ["lindsayca_manzanillo_block2_dr_2026", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 16b energy/power_plants_grid — Siemens Energy / Energía 2000 Manzanillo Power Land (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "siemens_manzanillo_power_land_414mw_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "Siemens Energy design — Energía 2000 Manzanillo Power Land 414 MW CCGT",
        "country": "Dominican Republic",
        "asset": "27–30 Mar 2026: President Abinader inaugurates Manzanillo Power Land 414 MW net natural-gas CCGT at Pepillo Salcedo (Energía 2000). Banreservas: plant designed by Siemens Energy; Banreservas/Afi Reservas US$345m within US$440m syndicate; Presidency cites ~USD 950m total investment with complementary infrastructure. Distinct from lindsayca_manzanillo_block2_dr_2026 (Block 2).",
        "investment_type": "equipment_supply",
        "value": "950000000",
        "currency": "USD",
        "value_usd": "950000000",
        "fx_usd": "1",
        "fx_date": "2026-03-27",
        "year": "2026",
        "status": "active",
        "lat": "19.70",
        "lon": "-71.74",
        "geo_note": "Pepillo Salcedo / Manzanillo, Monte Cristi (Presidency/Banreservas geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "banreservas_manzanillo_power_land_20260330",
        "note": "Actor: Siemens Energy (Germany) designer/technology — allied; developer Energía 2000 (DR). ~USD 950m total investment from Presidency is UNVERIFIED press/government figure for plant+complements.",
    },
    {
        "id": "siemens_manzanillo_power_land_414mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "banreservas_manzanillo_power_land_20260330",
        "url": "https://banreservas.com/noticiasyprensa/banreservas-lidera-financiamiento-por-us-345-millones-para-la-termoelectrica-manzanillo-power-land/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "El proyecto Manzanillo Power Land, desarrollado por la empresa Energía 2000, es una planta termoeléctrica de ciclo combinado de 414 megavatios, ubicada en Pepillo Salcedo, Monte Cristi. Fue diseñada por la empresa Siemens Energy y operará con gas natural",
        "note": "Opened Banreservas inauguration financing notice naming Siemens Energy design.",
    },
    {
        "id": "banreservas_manzanillo_power_land_20260330",
        "type": "press",
        "chicago": "Banco de Reservas de la República Dominicana. “Banreservas Lidera Financiamiento por US$345 Millones para la Termoeléctrica Manzanillo Power Land.” 30 March 2026.",
        "url": "https://banreservas.com/noticiasyprensa/banreservas-lidera-financiamiento-por-us-345-millones-para-la-termoelectrica-manzanillo-power-land/",
        "annotation": "Banreservas on Manzanillo Power Land 414 MW COD; Siemens Energy design. Supports siemens_manzanillo_power_land_414mw_2026.",
        "supports": ["siemens_manzanillo_power_land_414mw_2026", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 16c energy/power_plants_grid — EXIM Bahamas LNG Partner USD 99m (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "exim_bahamas_lng_99m_2025",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "U.S. EXIM — Bahamas LNG Partner Ltd. U.S. LNG purchase financing",
        "country": "Bahamas",
        "asset": "18 Sep 2025: EXIM Board approves USD 99 million to support Bahamas LNG Partner Ltd. purchasing U.S. LNG — complements 26 Jun 2025 FOCOL GE Vernova TM2500 + Pike pipeline transaction. Distinct from exim_focol_bahamas_99p6m_2025 (equipment/pipelines).",
        "investment_type": "financing",
        "value": "99000000",
        "currency": "USD",
        "value_usd": "99000000",
        "fx_usd": "1",
        "fx_date": "2025-09-18",
        "year": "2025",
        "status": "active",
        "lat": "25.01",
        "lon": "-77.45",
        "geo_note": "New Providence power fuel supply (complements FOCOL Blue Hills corridor; approximate pin).",
        "evidence": "documented",
        "source_id": "exim_bahamas_lng_20250918",
        "note": "Actor: U.S. EXIM — us. Official EXIM Board release same day as GMXT locomotives. Fuel-purchase financing for Bahamas generation.",
    },
    {
        "id": "exim_bahamas_lng_99m_2025",
        "retrieved": "2026-10-01",
        "source_id": "exim_bahamas_lng_20250918",
        "url": "https://www.exim.gov/news/export-import-bank-united-states-board-directors-approves-infrastructure-investments-totaling",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "In the second transaction, the Board approved $99 million dollars to support Bahamas LNG Partner Ltd. in purchasing U.S. liquefied natural gas (LNG). This LNG financing complements a transaction previously approved by the EXIM Board of Directors on June 26th, 2025, which includes the procurement of General Electric (GE) Vernova TM2500 Gen 8 Aeroderivative gas turbines, along with the construction of a natural gas pipeline and a diesel pipeline.",
        "note": "Opened EXIM Board approval release 18 Sep 2025 (same page as GMXT).",
    },
    {
        "id": "exim_bahamas_lng_20250918",
        "type": "government",
        "chicago": "Export-Import Bank of the United States. “Export-Import Bank of the United States Board of Directors Approves Infrastructure Investments Totaling Nearly $285 Million.” Press release, 18 September 2025.",
        "url": "https://www.exim.gov/news/export-import-bank-united-states-board-directors-approves-infrastructure-investments-totaling",
        "annotation": "EXIM USD 99m Bahamas LNG Partner U.S. LNG purchase financing. Supports exim_bahamas_lng_99m_2025.",
        "supports": ["exim_bahamas_lng_99m_2025", "exim_wabtec_gmxt_185m_2025", "hunt_br_power_equip"],
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
        "hunt_infra_port_ownership": "Cycle 61: equal budget; APM Lázaro III / SSA Guaymas / Hutchison ICAVE already (miss).",
        "hunt_res_copper": "Cycle 61: logged chinalco_los_calatos_peru_2026 (PRC proxy).",
        "hunt_res_water": "Cycle 61: equal budget; Cagece Dessal / NADBank Baja already (miss).",
        "hunt_energy_solar": "Cycle 61: logged powerchina_conchagua_salvador_30mw_2026 (PRC) + idb_invest_genneia_95m_2025 (allied).",
        "hunt_res_lithium": "Cycle 61: equal budget; Lilac Kachi / Albemarle TED / EnergyX already (miss).",
        "hunt_infra_building_materials": "Cycle 61: equal budget; Holcim Cemex Colombia / Sinoma Panam already (miss).",
        "hunt_latam_rail_telecom": "Cycle 61: equal budget; EXIM Wabtec GMXT just prior (miss).",
        "hunt_res_nickel": "Cycle 61: equal budget; Jervois / Westwin / DFC Piauí already (miss).",
        "hunt_energy_fission_smr": "Cycle 61: equal budget; Peru FIRST / USTDA LAC nuclear / Meitner already (miss).",
        "hunt_energy_other_renewables": "Cycle 61: equal budget; ClearPower Tinajones just prior (miss).",
        "hunt_energy_wind": "Cycle 61: equal budget; Vestas Argentina 217 MW just prior (miss).",
        "hunt_fenb_araxa": "Cycle 61: equal budget; St George Boston Metal / CBMM / CMOC already (miss).",
        "hunt_infra_engineering_epc": "Cycle 61: logged honeywell_petrobras_etj_replan_2026 (U.S.).",
        "hunt_infra_port_cranes": "Cycle 61: equal budget; Liebherr Compas Cartagena just prior (miss).",
        "hunt_res_balsa": "Cycle 61: equal budget; AIMA / Plantabal already (miss).",
        "hunt_br_power_equip": "Cycle 61: logged lindsayca_manzanillo_block2_dr_2026 (U.S.) + siemens_manzanillo_power_land_414mw_2026 (allied) + exim_bahamas_lng_99m_2025 (U.S.).",
        "hunt_res_graphite": "Cycle 61: equal budget; Atlas Malacacheta / Graphcoa already (miss).",
        "hunt_infra_bridges_roads": "Cycle 61: equal budget; USACE Guatemala / Aldesa Chiapas already (miss).",
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
    print("Cycle 61 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
