#!/usr/bin/env python3
"""Cycle 8 hunt: shuffle_seed=20261008; equal budget across 18 subcategories."""
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


# seed 20261008 order:
# engineering_epc, fission_smr, balsa, lithium, copper, other_renewables,
# port_ownership, niobium, graphite, water, wind, power_plants_grid,
# building_materials, rail, bridges_roads, solar, port_cranes, nickel

# 1 infrastructure/engineering_epc — Acciona SP Metro Line 6 civil works
A(
    {
        "id": "acciona_sp_line6_epc_2025",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "ACCIONA — civil works contractor for São Paulo Metro Line 6-Orange PPP",
        "country": "Brazil",
        "asset": "Construction of 15.3 km metro tunnel + 15 stations; >BRL 19 billion committed PPP investment; works >77% complete through 2025",
        "investment_type": "epc_ppp",
        "value": "19000000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-23.5",
        "lon": "-46.65",
        "geo_note": "São Paulo Metro Line 6 corridor Brasilândia–São Joaquim (ACCIONA).",
        "evidence": "documented",
        "source_id": "acciona_line6_milestones_20260112",
        "note": "Actor: ACCIONA (Spanish) — allied; PPP with Linha Uni / State of São Paulo. Company 12 Jan 2026 milestones article. Value stored as BRL (no FX). Distinct from Alstom Line 6 rolling-stock row and prior Acciona desal rows.",
    },
    {
        "id": "acciona_sp_line6_epc_2025",
        "retrieved": "2026-10-01",
        "source_id": "acciona_line6_milestones_20260112",
        "url": "https://www.acciona.com/updates/articles/sao-paulo-metro-line-6-project-reaches-key-milestones",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Construction of the São Paulo Metro Line 6 Orange — the largest infrastructure project underway in Latin America, carried out by ACCIONA — has reached important milestones throughout 2025 and now stands at over 77% completion. … With a committed investment of more than BRL 19 billion … The works are being carried out by ACCIONA",
        "note": "Opened ACCIONA Line 6 milestones article.",
    },
    {
        "id": "acciona_line6_milestones_20260112",
        "type": "official",
        "chicago": "ACCIONA. “São Paulo Metro Line 6 project reaches key milestones.” 12 January 2026.",
        "url": "https://www.acciona.com/updates/articles/sao-paulo-metro-line-6-project-reaches-key-milestones",
        "annotation": "Company primary Line 6 civil-works progress notice. Supports acciona_sp_line6_epc_2025.",
        "supports": ["acciona_sp_line6_epc_2025", "hunt_infra_engineering_epc"],
    },
)

# 2 energy/fission_smr — Argentina joins U.S. FIRST SMR program
A(
    {
        "id": "argentina_first_smr_2025",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "us",
        "counterpart": "Argentina — contributing partner in U.S. FIRST small modular reactor program",
        "country": "Argentina",
        "asset": "First Latin American contributing partner in U.S.-led FIRST (Foundational Infrastructure for Responsible Use of SMR Technology); to co-host 2026 LAC SMR conference in Buenos Aires",
        "investment_type": "program_partnership",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-34.6",
        "lon": "-58.38",
        "geo_note": "Buenos Aires (Cancillería / U.S. Embassy notices).",
        "evidence": "documented",
        "source_id": "cancilleria_first_20250919",
        "note": "Actors: Argentine state + U.S. State Department FIRST program — us coding for U.S.-led SMR partnership. Cancillería 19 Sep 2025 official notice. Complements CAREM/INVAP MoU/Meitner ACR-300 rows (program-level, not reactor EPC).",
    },
    {
        "id": "argentina_first_smr_2025",
        "retrieved": "2026-10-01",
        "source_id": "cancilleria_first_20250919",
        "url": "https://www.cancilleria.gob.ar/es/actualidad/noticias/argentina-ingresa-al-programa-de-infraestructura-fundamental-para-el-uso",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "La Argentina se convierte en el primer país de América Latina en unirse como socio contribuyente al Programa de Infraestructura Fundamental para el Uso Responsable de la Tecnología de Reactores Modulares Pequeños (FIRST), liderado por Estados Unidos. … La Argentina y Estados Unidos copresidirán la próxima conferencia regional de FIRST para países de América Latina y el Caribe sobre despliegue de SMR en Buenos Aires en 2026.",
        "note": "Opened Argentine Cancillería Spanish official notice.",
    },
    {
        "id": "cancilleria_first_20250919",
        "type": "official",
        "chicago": "Ministerio de Relaciones Exteriores, Comercio Internacional y Culto (Argentina). “Argentina ingresa al Programa … (FIRST) de Estados Unidos.” 19 September 2025.",
        "url": "https://www.cancilleria.gob.ar/es/actualidad/noticias/argentina-ingresa-al-programa-de-infraestructura-fundamental-para-el-uso",
        "annotation": "Argentine MFA primary FIRST contributing-partner notice. Supports argentina_first_smr_2025.",
        "supports": ["argentina_first_smr_2025", "hunt_energy_fission_smr"],
    },
)

# 3 resources/balsa — miss

# 4 resources/lithium — miss (equal budget; already covered Ganfeng/Eramet/Rio Tinto/POSCO)

# 5 resources/copper — Teck Quebrada Blanca ownership presence
A(
    {
        "id": "teck_quebrada_blanca_chile",
        "layer": "resources",
        "subcategory": "copper",
        "side": "allied",
        "counterpart": "Teck Resources (60%) — Quebrada Blanca copper operation, Tarapacá",
        "country": "Chile",
        "asset": "Expanded QB copper mine (Teck 60%; Sumitomo 30%; Codelco 10%); 2025 copper production 190 kt; 100% desalinated seawater for processes",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-21.0",
        "lon": "-68.8",
        "geo_note": "Quebrada Blanca, Tarapacá ~4,400 m elevation (Teck operations page).",
        "evidence": "documented",
        "source_id": "teck_qb_operations",
        "note": "Actor: Teck (Canadian) majority — allied. Company operations page + 2025 production figures. Complements bechtel_qb2_desal_chile water/EPC context without duplicating desal row; distinct from Codelco-Anglo Andina/Los Bronces JV.",
    },
    {
        "id": "teck_quebrada_blanca_chile",
        "retrieved": "2026-10-01",
        "source_id": "teck_qb_operations",
        "url": "https://www.teck.com/operations/chile/operations/quebrada-blanca/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Teck holds an indirect 60% interest in the mine. Sumitomo Metal Mining Co., Ltd. and Sumitomo Corporation together have a collective 30% indirect interest … Codelco … has a 10% non-funding interest. … Production (thousand tonnes) … 2025 … 190",
        "note": "Opened Teck Quebrada Blanca operations page.",
    },
    {
        "id": "teck_qb_operations",
        "type": "official",
        "chicago": "Teck Resources. “Quebrada Blanca.” Operations page (accessed 1 October 2026).",
        "url": "https://www.teck.com/operations/chile/operations/quebrada-blanca/",
        "annotation": "Company primary QB ownership/production page. Supports teck_quebrada_blanca_chile.",
        "supports": ["teck_quebrada_blanca_chile", "hunt_res_copper"],
    },
)

# 6 energy/other_renewables — miss

# 7 infrastructure/port_ownership — DP World Santos USD 50m equipment phase
A(
    {
        "id": "dpworld_santos_equip_2024",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "allied",
        "counterpart": "DP World — Port of Santos left-bank terminal equipment expansion",
        "country": "Brazil",
        "asset": "USD 50 million acquisition of 21 equipment units (2 quay cranes, 5 RTGs, 12 ITVs, 2 ECHs) within USD 85 million expansion to ~1.7 million TEU capacity",
        "investment_type": "concession_capex",
        "value": "50000000",
        "currency": "USD",
        "value_usd": "50000000",
        "fx_usd": "1",
        "fx_date": "2024-03-21",
        "year": "2024",
        "status": "active",
        "lat": "-23.93",
        "lon": "-46.32",
        "geo_note": "DP World Santos left bank (company release).",
        "evidence": "documented",
        "source_id": "dpworld_santos_20240321",
        "note": "Actor: DP World — allied. Company 21 Mar 2024 Brazil release. Crane OEMs not named — coded as ownership/capex. Distinct from DP World Callao / Posorja rows.",
    },
    {
        "id": "dpworld_santos_equip_2024",
        "retrieved": "2026-10-01",
        "source_id": "dpworld_santos_20240321",
        "url": "https://www.dpworld.com/en/news/brazil/dp-world-anuncia-novo-investimento-de-250-milhoes",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "DP World … announces a new investment of USD$50 million … in the acquisition of new port equipment for its terminal located on the left bank of the Port of Santos, Brazil. … 21 new pieces of equipment will be acquired, comprising two quay cranes, five RTGs … The new equipment also allows the terminal to expand capacity to 1.7 million TEUs",
        "note": "Opened DP World Santos English news page.",
    },
    {
        "id": "dpworld_santos_20240321",
        "type": "official",
        "chicago": "DP World. “DP World Announces New Investment of $50 Million for Expansion of Container Operations at Brazil’s Port of Santos.” 21 March 2024.",
        "url": "https://www.dpworld.com/en/news/brazil/dp-world-anuncia-novo-investimento-de-250-milhoes",
        "annotation": "Operator primary Santos equipment-capex notice. Supports dpworld_santos_equip_2024.",
        "supports": ["dpworld_santos_equip_2024", "hunt_infra_port_ownership"],
    },
)

# 8 resources/niobium — miss

# 9 resources/graphite — miss

# 10 resources/water — miss

# 11 energy/wind — miss

# 12 energy/power_plants_grid — miss (thick)

# 13 infrastructure/building_materials — Cemex DR sale to Cementos Progreso
A(
    {
        "id": "cemex_dr_divest_progreso_2024",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Cementos Progreso Holdings — acquisition of Cemex Dominican Republic cement operations",
        "country": "Dominican Republic",
        "asset": "Sale of Cemex DR operations (~USD 950 million) including two-line integrated cement plant plus concrete/aggregates/marine terminal assets (Haiti export book included)",
        "investment_type": "ownership_equity",
        "value": "950000000",
        "currency": "USD",
        "value_usd": "950000000",
        "fx_usd": "1",
        "fx_date": "2024-08-05",
        "year": "2024",
        "status": "active",
        "lat": "18.5",
        "lon": "-69.9",
        "geo_note": "Dominican Republic cement plant footprint (Cemex release).",
        "evidence": "documented",
        "source_id": "cemex_dr_divest_20240805",
        "note": "Buyer: Cementos Progreso Holdings (Guatemalan) — allied regional; seller Cemex (Mexican). Company 5 Aug 2024 release. Caribbean LatAm geography. Distinct from Holcim/Carmeuse/Huaxin/Sinoma building-materials rows.",
    },
    {
        "id": "cemex_dr_divest_progreso_2024",
        "retrieved": "2026-10-01",
        "source_id": "cemex_dr_divest_20240805",
        "url": "https://www.cemex.com/w/cemex-to-divest-its-operations-in-the-dominican-republic",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Cemex announced today that an agreement has been signed for the sale of its operations in the Dominican Republic, for a total consideration of approximately US$950 million. … The divested assets mainly consist of one cement plant in the Dominican Republic consisting of two integrated production lines and related cement, concrete, aggregates and marine terminal assets.",
        "note": "Opened Cemex corporate release.",
    },
    {
        "id": "cemex_dr_divest_20240805",
        "type": "official",
        "chicago": "Cemex. “Cemex to divest its operations in the Dominican Republic.” 5 August 2024.",
        "url": "https://www.cemex.com/w/cemex-to-divest-its-operations-in-the-dominican-republic",
        "annotation": "Seller primary DR divestiture announcement (buyer Cementos Progreso). Supports cemex_dr_divest_progreso_2024.",
        "supports": ["cemex_dr_divest_progreso_2024", "hunt_infra_building_materials"],
    },
)

# 14 infrastructure/rail — Alstom SP Line 6 Metropolis fleet
A(
    {
        "id": "alstom_sp_line6_trains_2025",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "Alstom — 22 six-car Metropolis trains for São Paulo Metro Line 6-Orange",
        "country": "Brazil",
        "asset": "Fleet of 22 stainless-steel six-car trains (~2,044 passengers each) manufactured at Taubaté; first train delivered Jul 2025",
        "investment_type": "rolling_stock",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-23.02",
        "lon": "-45.55",
        "geo_note": "Alstom Taubaté manufacturing plant / Line 6 fleet (company release).",
        "evidence": "documented",
        "source_id": "alstom_line6_20250710",
        "note": "Actor: Alstom (French) — allied. Company 10 Jul 2025 release. Complements acciona_sp_line6_epc_2025 civil works; distinct from Alstom Santiago Line 7 / Mexico DMU rows.",
    },
    {
        "id": "alstom_sp_line6_trains_2025",
        "retrieved": "2026-10-01",
        "source_id": "alstom_line6_20250710",
        "url": "https://www.alstom.com/press-releases-news/2025/7/alstom-delivers-first-train-line-6-orange-sao-paulo",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Alstom … has delivered the first train for Line 6-Orange. It belongs of the fleet of 22 six-car trains produced at Alstom's manufacturing site located in Taubaté … Each train will have the capacity to carry up to 2,044 passengers",
        "note": "Opened Alstom press release.",
    },
    {
        "id": "alstom_line6_20250710",
        "type": "official",
        "chicago": "Alstom. “Alstom delivers the first train for Line 6-Orange, in São Paulo.” 10 July 2025.",
        "url": "https://www.alstom.com/press-releases-news/2025/7/alstom-delivers-first-train-line-6-orange-sao-paulo",
        "annotation": "Company primary Line 6 rolling-stock delivery notice. Supports alstom_sp_line6_trains_2025.",
        "supports": ["alstom_sp_line6_trains_2025", "hunt_latam_rail_telecom"],
    },
)

# 15 infrastructure/bridges_roads — miss

# 16 energy/solar — Canadian Solar Morada do Sol 381 MWp Brazil
A(
    {
        "id": "canadian_solar_morada_sol_br",
        "layer": "energy",
        "subcategory": "solar",
        "side": "allied",
        "counterpart": "Canadian Solar — Morada do Sol 381 MWp solar project (Usiminas corporate PPA), Goiás",
        "country": "Brazil",
        "asset": "381 MWp Morada do Sol development with corporate PPA committing 50% of output to Usiminas; construction targeted from 2024 toward Jan 2025 COD",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2024",
        "status": "active",
        "lat": "-15.9",
        "lon": "-49.3",
        "geo_note": "Goiás state Morada do Sol project (Canadian Solar release).",
        "evidence": "documented",
        "source_id": "canadian_solar_morada_20220225",
        "note": "Actor: Canadian Solar (Canadian/listed) — allied. Company 25 Feb 2022 PPA release with 2024–2025 build/COD schedule. Distinct from SPIC/Atlas/Trina/Recurrent solar rows.",
    },
    {
        "id": "canadian_solar_morada_sol_br",
        "retrieved": "2026-10-01",
        "source_id": "canadian_solar_morada_20220225",
        "url": "https://investors.canadiansolar.com/news-releases/news-release-details/canadian-solar-signs-381-mwp-solar-corporate-ppa-brazil",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Canadian Solar will develop and build the 381 MWp Morada do Sol project in the State of Goiás. Construction is expected to start in the first quarter of 2024 and the project is expected to reach commercial operation by January 2025.",
        "note": "Opened Canadian Solar investor news release.",
    },
    {
        "id": "canadian_solar_morada_20220225",
        "type": "official",
        "chicago": "Canadian Solar Inc. “Canadian Solar Signs 381 MWp Solar Corporate PPA in Brazil.” 25 February 2022.",
        "url": "https://investors.canadiansolar.com/news-releases/news-release-details/canadian-solar-signs-381-mwp-solar-corporate-ppa-brazil",
        "annotation": "Company primary Morada do Sol PPA/development notice. Supports canadian_solar_morada_sol_br.",
        "supports": ["canadian_solar_morada_sol_br", "hunt_energy_solar"],
    },
)

# 17 infrastructure/port_cranes — miss (Santos quay cranes OEM unnamed on DP World page)

# 18 resources/nickel — miss


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
        "hunt_infra_engineering_epc": "Cycle 8: logged acciona_sp_line6_epc_2025.",
        "hunt_energy_fission_smr": "Cycle 8: logged argentina_first_smr_2025.",
        "hunt_res_balsa": "Cycle 8: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_res_lithium": "Cycle 8: equal budget; no distinct new Li deal beyond Ganfeng/Eramet/Rio Tinto/POSCO (miss).",
        "hunt_res_copper": "Cycle 8: logged teck_quebrada_blanca_chile.",
        "hunt_energy_other_renewables": "Cycle 8: equal budget; no new geothermal/hydro beyond Ivirizu/Chinameca/Ormat/San Gabán (miss).",
        "hunt_infra_port_ownership": "Cycle 8: logged dpworld_santos_equip_2024.",
        "hunt_fenb_araxa": "Cycle 8: equal budget; no distinct new FeNb ownership/price beyond CBMM/CMOC (miss).",
        "hunt_res_graphite": "Cycle 8: equal budget; no distinct new graphite mine/anode beyond South Star/Graphcoa/Urbix/Nacional/Graphex (miss).",
        "hunt_res_water": "Cycle 8: equal budget; no new desal beyond IDE/Acciona/GS Inima/Techint (miss).",
        "hunt_energy_wind": "Cycle 8: equal budget; no new OEM award beyond Vestas/Goldwind/Nordex set (miss).",
        "hunt_br_power_equip": "Cycle 8: equal budget; thick subcategory — miss.",
        "hunt_infra_building_materials": "Cycle 8: logged cemex_dr_divest_progreso_2024.",
        "hunt_latam_rail_telecom": "Cycle 8: logged alstom_sp_line6_trains_2025.",
        "hunt_infra_bridges_roads": "Cycle 8: equal budget; no new highway/bridge beyond CHEC Jamaica/Colombia/Ecuador set (miss).",
        "hunt_energy_solar": "Cycle 8: logged canadian_solar_morada_sol_br.",
        "hunt_infra_port_cranes": "Cycle 8: equal budget; Santos quay crane OEM unnamed on DP World page (miss).",
        "hunt_res_nickel": "Cycle 8: equal budget; no distinct new Ni ownership beyond MMG/Anglo/Vale/Centaurus/Atlantic Nickel (miss).",
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
    print("Cycle 8 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
