#!/usr/bin/env python3
"""Cycle 11 hunt: shuffle_seed=20261011; equal budget across 18 subcategories."""
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


# seed 20261011 order:
# bridges_roads, nickel, fission_smr, port_cranes, rail, niobium, graphite, copper,
# power_plants_grid, lithium, solar, water, port_ownership, building_materials,
# engineering_epc, other_renewables, balsa, wind

# 1 infrastructure/bridges_roads — MOP Panama Panamericana Oeste APP (Mexican consortium)
A(
    {
        "id": "mop_panama_panamericana_oeste_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "allied",
        "counterpart": "Consorcio APP Vías del Istmo (Mexican firms) — Panamericana Oeste rehabilitation PPP",
        "country": "Panama",
        "asset": "Rehabilitación, Mejora y Mantenimiento de la Carretera Panamericana Oeste (CPO); 192 km Loma Campana–Santiago (91 km + 101 km); 20-year APP; UNVERIFIED press investment figure USD 312.3 million",
        "investment_type": "ppp_concession",
        "value": "312300000",
        "currency": "USD",
        "value_usd": "312300000",
        "fx_usd": "1",
        "fx_date": "2026-01-14",
        "year": "2026",
        "status": "active",
        "lat": "8.4",
        "lon": "-80.4",
        "geo_note": "Panamericana Oeste corridor Loma Campana–Santiago, Veraguas/Coclé (La Prensa reporting MOP award).",
        "evidence": "proxy",
        "source_id": "prensa_panama_cpo_app_20260114",
        "note": "Actor: Consorcio APP Vías del Istmo — Promotora y Desarrolladora Mexicana de Infraestructura; Calzada Construcciones; Ingeniería Estrella (Mexican) — allied. UNVERIFIED proxy: La Prensa (14 Jan 2026) reports MOP award at USD 312.3 million vs USD 359.4 million reference; mop.gob.pa primary unreachable from hunt environment. Distinct from CHEC Fourth Bridge Panama.",
    },
    {
        "id": "mop_panama_panamericana_oeste_2026",
        "retrieved": "2026-10-01",
        "source_id": "prensa_panama_cpo_app_20260114",
        "url": "https://www.prensa.com/sociedad/mop-adjudica-segunda-app-del-pais-para-la-rehabilitacion-de-la-carretera-panamericana-oeste-por-312-millones/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "fue adjudicada por el Ministerio de Obras Públicas (MOP) al Consorcio APP Vías del Istmo, por un monto de $ 312.3 millones. El Consorcio APP Vías del Istmo está conformado por la Promotora y Desarrolladora Mexicana de Infraestructura, S.A.; Calzada Construcciones, S.A. de C.V.; e Ingeniería Estrella, S.A. … abarca 192 kilómetros, desde La Loma de Campana hasta la ciudad de Santiago",
        "note": "Opened La Prensa Panama award report (MOP primary unreachable this cycle).",
    },
    {
        "id": "prensa_panama_cpo_app_20260114",
        "type": "press",
        "chicago": "Mojica, Yaritza. “MOP adjudica segunda APP del país para la rehabilitación de la Carretera Panamericana Oeste por $312 millones.” La Prensa (Panamá), 14 January 2026.",
        "url": "https://www.prensa.com/sociedad/mop-adjudica-segunda-app-del-pais-para-la-rehabilitacion-de-la-carretera-panamericana-oeste-por-312-millones/",
        "annotation": "Press report of MOP Panamericana Oeste APP award to Mexican consortium. Supports mop_panama_panamericana_oeste_2026 (UNVERIFIED value).",
        "supports": ["mop_panama_panamericana_oeste_2026", "hunt_infra_bridges_roads"],
    },
)

# 2 resources/nickel — IFC/Appian EM critical-minerals fund first investment Santa Rita
A(
    {
        "id": "ifc_appian_santa_rita_fund_2025",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "IFC / Appian EM critical-minerals fund — first investment in Atlantic Nickel Santa Rita underground",
        "country": "Brazil",
        "asset": "Fund co-investment alongside Appian to advance Santa Rita (Bahia) underground nickel-copper-cobalt development; target ramp ~30,000 tpy NiEq; 30+ year mine life (company); discrete financing event vs ownership row",
        "investment_type": "financing",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-11.0",
        "lon": "-39.5",
        "geo_note": "Santa Rita / Itagibá area, Bahia (Appian Atlantic Nickel portfolio).",
        "evidence": "documented",
        "source_id": "appian_ifc_em_fund_20251022",
        "note": "Actors: IFC (World Bank Group) + Appian Capital Advisory (UK) — allied. Company 22 Oct 2025: Fund’s first investment is Atlantic Nickel Santa Rita underground co-investment; IFC investing on same terms after Citi/Standard Chartered valuations. No USD commitment amount on opened Appian page (press cites up to USD 50m — not entered). Distinct from atlantic_nickel_santa_rita_br ownership row.",
    },
    {
        "id": "ifc_appian_santa_rita_fund_2025",
        "retrieved": "2026-10-01",
        "source_id": "appian_ifc_em_fund_20251022",
        "url": "https://appiancapitaladvisory.com/appian-and-ifc-partner-in-new-us1-billion-critical-minerals-and-metals-fund-for-emerging-markets/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "The Fund’s first investment is in Atlantic Nickel’s producing Santa Rita project in Brazil. This is a co-investment alongside Appian to advance the underground development of a large-scale nickel-copper-cobalt asset with a 30+ year mine life … The mine is expected to ramp up production to approximately 30,000 tonnes per year of nickel equivalent",
        "note": "Opened Appian Capital Advisory IFC partnership release.",
    },
    {
        "id": "appian_ifc_em_fund_20251022",
        "type": "official",
        "chicago": "Appian Capital Advisory. “Appian and IFC partner in new US$1 billion critical minerals and metals fund for emerging markets.” 22 October 2025.",
        "url": "https://appiancapitaladvisory.com/appian-and-ifc-partner-in-new-us1-billion-critical-minerals-and-metals-fund-for-emerging-markets/",
        "annotation": "Company primary on IFC-anchored EM fund; first investment Santa Rita. Supports ifc_appian_santa_rita_fund_2025.",
        "supports": ["ifc_appian_santa_rita_fund_2025", "hunt_res_nickel"],
    },
)

# 3 energy/fission_smr — miss (CAREM/Meitner/Brazil microreactor already logged; Finep/CNEN pages unreachable)

# 4 infrastructure/port_cranes — Konecranes Gottwald ESP.7 for APM Yucatán / Progreso
A(
    {
        "id": "konecranes_yucatan_progreso_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Konecranes — two Gottwald ESP.7 MHC for APM Terminals Yucatán (Puerto Progreso)",
        "country": "Mexico",
        "asset": "Two Konecranes Gottwald ESP.7 mobile harbor cranes with external power supply; order booked Q4 2025; delivery end September 2026 to Puerto Progreso",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "21.29",
        "lon": "-89.66",
        "geo_note": "Puerto Progreso, Yucatán (Konecranes release).",
        "evidence": "documented",
        "source_id": "konecranes_yucatan_esp7_20260113",
        "note": "Actor: Konecranes (Finland) — allied; buyer Terminal de Contenedores de Yucatán / APM Terminals Yucatán. Company 13 Jan 2026 press release. Distinct from Konecranes Portonave RTG and Arica MHC rows.",
    },
    {
        "id": "konecranes_yucatan_progreso_2026",
        "retrieved": "2026-10-01",
        "source_id": "konecranes_yucatan_esp7_20260113",
        "url": "https://www.konecranes.com/press-releases/yucatan-deep-water-port-places-order-for-two-konecranes-gottwald-esp7-mobile-harbor-cranes",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Terminal de Contenedores de Yucatán, S.A. de C.V. (APM Terminals Yucatán) has ordered two Konecranes Gottwald ESP.7 Mobile Harbor Cranes … The order was booked in Q4 2025 and the cranes will be delivered to Puerto Progreso at the end of September 2026.",
        "note": "Opened Konecranes corporate press release.",
    },
    {
        "id": "konecranes_yucatan_esp7_20260113",
        "type": "official",
        "chicago": "Konecranes. “Yucatán deep-water port places order for two Konecranes Gottwald ESP.7 Mobile Harbor Cranes.” 13 January 2026.",
        "url": "https://www.konecranes.com/press-releases/yucatan-deep-water-port-places-order-for-two-konecranes-gottwald-esp7-mobile-harbor-cranes",
        "annotation": "Company primary MHC order for APM Yucatán/Progreso. Supports konecranes_yucatan_progreso_2026.",
        "supports": ["konecranes_yucatan_progreso_2026", "hunt_infra_port_cranes"],
    },
)

# 5 infrastructure/rail — miss
# 6 resources/niobium — miss
# 7 resources/graphite — miss (Boa Sorte / Jordânia / Urbix already logged)
# 8 resources/copper — miss
# 9 energy/power_plants_grid — miss (thick)

# 10 resources/lithium — Liex/Zijin Tres Quebradas RIGI adhesión (Boletín Oficial)
A(
    {
        "id": "zijin_liex_tres_quebradas_rigi_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "Liex S.A. (Zijin Mining) — Tres Quebradas (3Q) RIGI adhesión / DLE plant expansion",
        "country": "Argentina",
        "asset": "RIGI Project Único (Res. 1153/2026): Lodomar I/II/IV at Salar Tres Quebradas, Fiambalá (Catamarca); process plant + infrastructure for 40,000 tpa lithium carbonate via direct extraction; declared computable assets USD 594,136,000; adhesión date 3 Jul 2026; construction start 1 Jun 2026; ops target 1 Apr 2029",
        "investment_type": "ownership_equity",
        "value": "594136000",
        "currency": "USD",
        "value_usd": "594136000",
        "fx_usd": "1",
        "fx_date": "2026-07-29",
        "year": "2026",
        "status": "active",
        "lat": "-27.05",
        "lon": "-68.25",
        "geo_note": "Salar Tres Quebradas / Fiambalá, Catamarca (Boletín Oficial Res. 1153/2026).",
        "evidence": "documented",
        "source_id": "boletin_oficial_res_1153_2026",
        "note": "Actor: Liex S.A. Sucursal Dedicada — Zijin Mining 100% via Neo Lithium acquisition (Zijin Key Projects page opened) — prc. Value = declared computable assets from Res. 1153/2026 (not press USD 709m figure). Distinct from Rio Tinto Rincón / Altoandinos / Ganfeng lithium rows.",
    },
    {
        "id": "zijin_liex_tres_quebradas_rigi_2026",
        "retrieved": "2026-10-01",
        "source_id": "boletin_oficial_res_1153_2026",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/345075/20260729",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Liex S.A. declaró que el Proyecto implica una inversión total en activos computables de quinientos noventa y cuatro millones ciento treinta y seis mil dólares estadounidenses (USD 594.136.000) … capacidad de producción de cuarenta mil (40.000) toneladas anuales de carbonato de litio mediante el método de extracción directa … Salar Tres Quebradas (3Q), en el departamento de Fiambalá",
        "note": "Opened Boletín Oficial Resolución 1153/2026. Zijin ownership confirmed on opened Zijin Tres Quebradas Key Projects page.",
    },
    {
        "id": "boletin_oficial_res_1153_2026",
        "type": "official",
        "chicago": "Argentina. Ministerio de Economía. “Resolución 1153/2026” (RIGI adhesión — Liex S.A. Sucursal Dedicada / Proyecto Tres Quebradas). Boletín Oficial de la República Argentina, 29 July 2026.",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/345075/20260729",
        "annotation": "Official RIGI approval for Liex 3Q DLE expansion; USD 594.136m computable assets. Supports zijin_liex_tres_quebradas_rigi_2026.",
        "supports": ["zijin_liex_tres_quebradas_rigi_2026", "hunt_res_lithium"],
    },
)

# 11 energy/solar — miss (thick)
# 12 resources/water — miss
# 13 infrastructure/port_ownership — miss
# 14 infrastructure/building_materials — miss (Holcim Colombia / Pacasmayo already logged; CSN/Huaxin bids not closed)

# 15 infrastructure/engineering_epc — Worley Diablillos LNTP
A(
    {
        "id": "worley_diablillos_abrasilver_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "Worley — Limited Notice to Proceed for AbraSilver Diablillos silver-gold bridging/FID phase",
        "country": "Argentina",
        "asset": "Bridging-phase engineering after Worley-delivered DFS: design, technical studies, procurement support, cost/schedule, permitting, site-camp planning toward FID targeted 2Q 2027; Puna (Salta/Catamarca)",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-25.3",
        "lon": "-66.7",
        "geo_note": "Diablillos project, Puna region Salta/Catamarca (Worley release).",
        "evidence": "documented",
        "source_id": "worley_diablillos_lntp_20260827",
        "note": "Actor: Worley (Australian) — allied; client AbraSilver. Company 27 Aug 2026 insight: LNTP for next phase after DFS. Non-grid mining EPC. Distinct from worley_rincon_lithium_epc_2025.",
    },
    {
        "id": "worley_diablillos_abrasilver_2026",
        "retrieved": "2026-10-01",
        "source_id": "worley_diablillos_lntp_20260827",
        "url": "https://www.worley.com/en/insights/our-news/resources/2026/abrasilver-diablillos-silver-gold-project-argentina",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Worley has received a Limited Notice to Proceed to support the next phase of AbraSilver’s Diablillos Silver‑Gold Project in Argentina. Diablillos is located in the Puna region, across the provinces of Salta and Catamarca. The award follows completion of the Definitive Feasibility Study (DFS) for Diablillos, which was also delivered by Worley",
        "note": "Opened Worley Diablillos LNTP insight.",
    },
    {
        "id": "worley_diablillos_lntp_20260827",
        "type": "official",
        "chicago": "Worley. “Worley to advance next phase of AbraSilver’s Diablillos Silver‑Gold project in Argentina.” 27 August 2026.",
        "url": "https://www.worley.com/en/insights/our-news/resources/2026/abrasilver-diablillos-silver-gold-project-argentina",
        "annotation": "Company primary LNTP award for Diablillos bridging phase. Supports worley_diablillos_abrasilver_2026.",
        "supports": ["worley_diablillos_abrasilver_2026", "hunt_infra_engineering_epc"],
    },
)

# 16 energy/other_renewables — miss
# 17 resources/balsa — miss
# 18 energy/wind — miss


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added: list[str] = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
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
        "hunt_infra_bridges_roads": "Cycle 11: logged mop_panama_panamericana_oeste_2026.",
        "hunt_res_nickel": "Cycle 11: logged ifc_appian_santa_rita_fund_2025.",
        "hunt_energy_fission_smr": "Cycle 11: equal budget; no new SMR beyond CAREM/Meitner/FIRST/Brazil microreactor (Finep/CNEN pages unreachable — miss).",
        "hunt_infra_port_cranes": "Cycle 11: logged konecranes_yucatan_progreso_2026.",
        "hunt_latam_rail_telecom": "Cycle 11: equal budget; Trenes del Norte / BA Line B / EFE Siemens already logged — miss.",
        "hunt_fenb_araxa": "Cycle 11: equal budget; no new FeNb ownership/price beyond CBMM/CMOC Catalão production update (miss).",
        "hunt_res_graphite": "Cycle 11: equal budget; no distinct new graphite beyond Boa Sorte/Jordânia/Urbix/Nacional/South Star (miss).",
        "hunt_res_copper": "Cycle 11: equal budget; no new copper ownership beyond existing FCX/FQM/Teck/Chinalco set (miss).",
        "hunt_br_power_equip": "Cycle 11: equal budget; thick subcategory — miss.",
        "hunt_res_lithium": "Cycle 11: logged zijin_liex_tres_quebradas_rigi_2026.",
        "hunt_energy_solar": "Cycle 11: equal budget; no new solar beyond existing thick set (miss).",
        "hunt_res_water": "Cycle 11: equal budget; no new desal beyond IDE/Acciona/GS Inima set (miss).",
        "hunt_infra_port_ownership": "Cycle 11: equal budget; no new port ownership beyond APM Suape / Hutchison / DP World / ICTSI set (miss).",
        "hunt_infra_building_materials": "Cycle 11: equal budget; Holcim Colombia already logged; CSN/Huaxin bids not closed (miss).",
        "hunt_infra_engineering_epc": "Cycle 11: logged worley_diablillos_abrasilver_2026.",
        "hunt_energy_other_renewables": "Cycle 11: equal budget; no new geothermal/hydro beyond JICA/PowerChina/LaGeo set (miss).",
        "hunt_res_balsa": "Cycle 11: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_energy_wind": "Cycle 11: equal budget; no new OEM award beyond Vestas/Goldwind/Nordex/Envision (miss).",
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
    print("Cycle 11 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
