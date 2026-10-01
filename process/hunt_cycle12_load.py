#!/usr/bin/env python3
"""Cycle 12 hunt: shuffle_seed=20261012; equal budget across 18 subcategories."""
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


# seed 20261012 order:
# rail, balsa, lithium, building_materials, engineering_epc, nickel, other_renewables,
# niobium, bridges_roads, wind, graphite, water, copper, solar, power_plants_grid,
# port_cranes, port_ownership, fission_smr

# 1 infrastructure/rail — miss (Alstom Mexico DMU / Salvador CRRC already logged)
# 2 resources/balsa — miss

# 3 resources/lithium — POSCO Sal de Oro II RIGI (Li2CO3 plant)
A(
    {
        "id": "posco_sal_de_oro_ii_rigi_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "Posco Argentina SAU SDE — Sal de Oro II RIGI adhesión (Li2CO3 plant)",
        "country": "Argentina",
        "asset": "RIGI Project Único “Sal de Oro II” (Res. 1157/2026): ~23,000 tpa lithium carbonate plant at Salar del Hombre Muerto (Salta/Catamarca border); conventional solar-pond + CaO chemical treatment; export-dedicated; declared computable assets USD 207,936,427.20; adhesión 12 Jun 2026; ops target 1 Jul 2026",
        "investment_type": "ownership_equity",
        "value": "207936427.20",
        "currency": "USD",
        "value_usd": "207936427.20",
        "fx_usd": "1",
        "fx_date": "2026-07-31",
        "year": "2026",
        "status": "active",
        "lat": "-25.4",
        "lon": "-67.1",
        "geo_note": "Salar del Hombre Muerto border Salta/Catamarca (Boletín Oficial Res. 1157/2026).",
        "evidence": "documented",
        "source_id": "boletin_oficial_res_1157_2026",
        "note": "Actor: POSCO Argentina (South Korean) — allied. Distinct from posco_sal_de_oro_lioh_2024 (LiOH Güemes plant) and Zijin Tres Quebradas RIGI. Value = declared computable assets from Res. 1157/2026.",
    },
    {
        "id": "posco_sal_de_oro_ii_rigi_2026",
        "retrieved": "2026-10-01",
        "source_id": "boletin_oficial_res_1157_2026",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/345279/20260731",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "POSCO SDE declaró que el Proyecto implicará una inversión total en activos computables de doscientos siete millones novecientos treinta y seis mil cuatrocientos veintisiete dólares estadounidenses con veinte céntimos (USD 207.936.427,20) … capacidad operativa de veintitrés mil (23.000) toneladas anuales … carbonato de litio (Li2CO3)",
        "note": "Opened Boletín Oficial Resolución 1157/2026.",
    },
    {
        "id": "boletin_oficial_res_1157_2026",
        "type": "official",
        "chicago": "Argentina. Ministerio de Economía. “Resolución 1157/2026” (RIGI adhesión — Posco Argentina SAU SDE / Sal de Oro II). Boletín Oficial de la República Argentina, 31 July 2026.",
        "url": "https://www.boletinoficial.gob.ar/detalleAviso/primera/345279/20260731",
        "annotation": "Official RIGI approval for POSCO Sal de Oro II Li2CO3 plant. Supports posco_sal_de_oro_ii_rigi_2026.",
        "supports": ["posco_sal_de_oro_ii_rigi_2026", "hunt_res_lithium"],
    },
)

# 4 infrastructure/building_materials — miss (CSN/Huaxin bids not closed)
# 5 infrastructure/engineering_epc — miss (Worley Diablillos logged C11)
# 6 resources/nickel — miss

# 7 energy/other_renewables — Acciona La Gina multipurpose hydro (DR)
A(
    {
        "id": "acciona_la_gina_dr_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "allied",
        "counterpart": "Consorcio A&H Presa La Gina (Acciona Construcción / Acciona Infraestructuras México / Hage) — La Gina multipurpose hydro",
        "country": "Dominican Republic",
        "asset": "Construction of Aprovechamiento Múltiple Cuenca Alta Río Baní / Presa La Gina (Peravia); 45-month contract; award DO1.AWD.1951818 value DOP 6,362,123,311.24 (19 May 2026); irrigation/drinking water + hydro generation",
        "investment_type": "epc",
        "value": "6362123311.24",
        "currency": "DOP",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "18.45",
        "lon": "-70.45",
        "geo_note": "Upper Baní River basin, Peravia province (EGEHID / Compras Dominicana tender).",
        "evidence": "documented",
        "source_id": "compras_dominicana_la_gina_20260519",
        "note": "Actor: Consorcio A&H — Acciona (Spain) + Hage Constructora — allied (consortium composition from opened EH+ report; award value/company name from Compras Dominicana portal). Runner-up included PowerChina. Distinct from Acciona desal/metro EPC rows. DOP stored without USD conversion (no Fed H.10 opened this cycle).",
    },
    {
        "id": "acciona_la_gina_dr_2026",
        "retrieved": "2026-10-01",
        "source_id": "compras_dominicana_la_gina_20260519",
        "url": "https://comunidad.comprasdominicana.gob.do/Public/Tendering/OpportunityDetail/Index?asPopupView=true&isModal=true&noticeUID=DO1.NTC.1617547",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Award DO1.AWD.1951818 | Award Date 19/05/2026 11:52 | Award Value 6,362,123,311.24 Dominican Pesos | Awarded Company CONSORCIO A&H - PRESA LA GINA | Request Name: Contratación de una Compañía para la Construcción del Proyecto Aprovechamiento Múltiple de las Aguas en la Cuenca Alta Río Bani, Presa La Gina",
        "note": "Opened Dominican Republic Compras Dominicana award record for EGEHID-CCC-LPN-2025-0032.",
    },
    {
        "id": "compras_dominicana_la_gina_20260519",
        "type": "official",
        "chicago": "República Dominicana. Dirección General de Contrataciones Públicas / EGEHID. “EGEHID-CCC-LPN-2025-0032 — Presa La Gina” (Award DO1.AWD.1951818). Compras Dominicana, 19 May 2026.",
        "url": "https://comunidad.comprasdominicana.gob.do/Public/Tendering/OpportunityDetail/Index?asPopupView=true&isModal=true&noticeUID=DO1.NTC.1617547",
        "annotation": "Official procurement award for La Gina multipurpose dam/hydro. Supports acciona_la_gina_dr_2026.",
        "supports": ["acciona_la_gina_dr_2026", "hunt_energy_other_renewables"],
    },
)

# also other_renewables — Ormat Dominica 10 MW geothermal PPA
A(
    {
        "id": "ormat_dominica_geothermal_ppa_2023",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "Ormat Technologies — 10 MW binary geothermal plant PPA with DOMLEC (Dominica)",
        "country": "Dominica",
        "asset": "25-year PPA for 10 MW binary geothermal plant in Roseau Valley; build-operate-transfer to Government of Dominica at term end; expected operational by end-2025 (company 2023 release)",
        "investment_type": "concession",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2023",
        "status": "active",
        "lat": "15.3",
        "lon": "-61.37",
        "geo_note": "Roseau Valley geothermal field, Dominica (Ormat release).",
        "evidence": "documented",
        "source_id": "ormat_dominica_ppa_20231206",
        "note": "Actor: Ormat Technologies (U.S.) — us. Company 6 Dec 2023 COP28 release. Caribbean LatAm geography. Distinct from Ormat Amatitlán/Zunil Guatemala presence rows. No CAPEX USD on opened page.",
    },
    {
        "id": "ormat_dominica_geothermal_ppa_2023",
        "retrieved": "2026-10-01",
        "source_id": "ormat_dominica_ppa_20231206",
        "url": "https://investor.ormat.com/news-events/news/news-details/2023/Ormat-Signed-Historic-25-Year-Power-Purchase-Agreement-With-Dominica-Electricity-Services-Ltd/default.aspx",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "signing of a groundbreaking 25-year Power Purchase Agreement (PPA) with Dominica Electricity Services Ltd. (DOMLEC) for the development of a state-of-the-art 10 MW binary geothermal power plant in the Caribbean country of Dominica. The project is expected to be operational by the end of 2025.",
        "note": "Opened Ormat investor release.",
    },
    {
        "id": "ormat_dominica_ppa_20231206",
        "type": "official",
        "chicago": "Ormat Technologies, Inc. “Ormat Signed Historic 25-Year Power Purchase Agreement With Dominica Electricity Services Ltd.” 6 December 2023.",
        "url": "https://investor.ormat.com/news-events/news/news-details/2023/Ormat-Signed-Historic-25-Year-Power-Purchase-Agreement-With-Dominica-Electricity-Services-Ltd/default.aspx",
        "annotation": "Company primary Dominica geothermal PPA. Supports ormat_dominica_geothermal_ppa_2023.",
        "supports": ["ormat_dominica_geothermal_ppa_2023", "hunt_energy_other_renewables"],
    },
)

# 8 resources/niobium — miss (CBMM R$13bn press overlaps prior capex proxy)
# 9 infrastructure/bridges_roads — miss
# 10 energy/wind — miss

# 11 resources/graphite — South Star Santa Cruz first commercial PO
A(
    {
        "id": "south_star_santa_cruz_po_36t_2026",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "South Star Battery Metals — first commercial purchase order for Santa Cruz flake graphite",
        "country": "Brazil",
        "asset": "36-tonne graphite concentrate purchase order after customer qualification of Santa Cruz (Bahia) flake/fines; first bulk commercial shipment scheduled Aug 2026; ramp toward ~5,000 tpa concentrate",
        "investment_type": "offtake",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-16.3",
        "lon": "-39.6",
        "geo_note": "Santa Cruz graphite mine/plant, southern Bahia (South Star releases).",
        "evidence": "documented",
        "source_id": "south_star_po_20260807",
        "note": "Actor: South Star Battery Metals (Canadian) — allied. Company 7 Aug 2026 GlobeNewswire. Distinct from south_star_santa_cruz_graphite_2024 presence/capacity row and Graphex offtake (different buyer path). Buyer unnamed; no USD on page.",
    },
    {
        "id": "south_star_santa_cruz_po_36t_2026",
        "retrieved": "2026-10-01",
        "source_id": "south_star_po_20260807",
        "url": "https://www.globenewswire.com/news-release/2026/08/07/3341011/0/en/south-star-achieves-graphite-purchase-order-milestone.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "successfully completed the qualification process for the graphite concentrate produced at the Santa Cruz mine with a significant graphite customer and has received a purchase order from this customer for 36 tonnes of graphite concentrate … This first bulk shipment is scheduled to be dispatched this week",
        "note": "Opened South Star GlobeNewswire purchase-order release.",
    },
    {
        "id": "south_star_po_20260807",
        "type": "official",
        "chicago": "South Star Battery Metals Corp. “South Star Achieves Graphite Purchase Order Milestone.” GlobeNewswire, 7 August 2026.",
        "url": "https://www.globenewswire.com/news-release/2026/08/07/3341011/0/en/south-star-achieves-graphite-purchase-order-milestone.html",
        "annotation": "Company primary first commercial PO for Santa Cruz concentrate. Supports south_star_santa_cruz_po_36t_2026.",
        "supports": ["south_star_santa_cruz_po_36t_2026", "hunt_res_graphite"],
    },
)

# 12 resources/water — miss
# 13 resources/copper — miss
# 14 energy/solar — miss
# 15 energy/power_plants_grid — miss

# 16 infrastructure/port_cranes — Konecranes Cartagena 25 RTGs
A(
    {
        "id": "konecranes_cartagena_rtg_2025",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Konecranes — 25 new RTGs + 10 remote-supervision RTG retrofits (Port of Cartagena)",
        "country": "Colombia",
        "asset": "25 Konecranes RTGs ordered by a major Cartagena container terminal; deal signed Q3 2025; deliveries in five batches Q4 2026–Q1 2028; plus 10 existing RTGs retrofitted for supervised remote ops (separate from 37 third-party RTG retrofit program)",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "10.4",
        "lon": "-75.52",
        "geo_note": "Port of Cartagena container terminal complex (Konecranes release; terminal name withheld on page).",
        "evidence": "documented",
        "source_id": "konecranes_cartagena_25rtg_press",
        "note": "Actor: Konecranes (Finland) — allied. Company IR press (deal Q3 2025). Distinct from Konecranes Portonave/Arica/Yucatán crane rows. No contract USD on opened page.",
    },
    {
        "id": "konecranes_cartagena_rtg_2025",
        "retrieved": "2026-10-01",
        "source_id": "konecranes_cartagena_25rtg_press",
        "url": "https://investors.konecranes.com/press/major-colombian-container-terminal-extends-its-konecranes-led-yard-modernization-new-order-25",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "A major global terminal in the Port of Cartagena, Colombia has ordered 25 Konecranes Rubber-Tired Gantry Cranes (RTGs), along with Konecranes retrofits for 10 existing RTGs to enable supervised operations. The deal was signed in Q3 2025 and the new cranes will be delivered in five batches: the first in Q4 2026 and the last in Q1 2028.",
        "note": "Opened Konecranes investor press release.",
    },
    {
        "id": "konecranes_cartagena_25rtg_press",
        "type": "official",
        "chicago": "Konecranes. “Major Colombian Container Terminal extends its Konecranes-led yard modernization with new order for 25 RTGs and 10 more retrofits for remote supervision.” Accessed 1 October 2026.",
        "url": "https://investors.konecranes.com/press/major-colombian-container-terminal-extends-its-konecranes-led-yard-modernization-new-order-25",
        "annotation": "Company primary Cartagena RTG modernization order. Supports konecranes_cartagena_rtg_2025.",
        "supports": ["konecranes_cartagena_rtg_2025", "hunt_infra_port_cranes"],
    },
)

# 17 infrastructure/port_ownership — miss
# 18 energy/fission_smr — miss (MCTI/Finep page JS-empty; Brazil microreactor already logged)


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
        "hunt_latam_rail_telecom": "Cycle 12: equal budget; Alstom Mexico DMU / Salvador CRRC already logged — miss.",
        "hunt_res_balsa": "Cycle 12: equal budget; no new balsa trade year beyond WITS 2022–2024 (miss).",
        "hunt_res_lithium": "Cycle 12: logged posco_sal_de_oro_ii_rigi_2026.",
        "hunt_infra_building_materials": "Cycle 12: equal budget; CSN/Huaxin bids not closed (miss).",
        "hunt_infra_engineering_epc": "Cycle 12: equal budget; Worley Diablillos logged C11 — miss.",
        "hunt_res_nickel": "Cycle 12: equal budget; no distinct new Ni beyond IFC/Appian Santa Rita fund (miss).",
        "hunt_energy_other_renewables": "Cycle 12: logged acciona_la_gina_dr_2026 + ormat_dominica_geothermal_ppa_2023.",
        "hunt_fenb_araxa": "Cycle 12: equal budget; CBMM R$13bn press overlaps prior capex proxy — miss.",
        "hunt_infra_bridges_roads": "Cycle 12: equal budget; Panamericana Oeste logged C11 — miss.",
        "hunt_energy_wind": "Cycle 12: equal budget; no new OEM beyond Vestas/Goldwind/Nordex/Envision (miss).",
        "hunt_res_graphite": "Cycle 12: logged south_star_santa_cruz_po_36t_2026.",
        "hunt_res_water": "Cycle 12: equal budget; no new desal beyond IDE/Acciona/GS Inima (miss).",
        "hunt_res_copper": "Cycle 12: equal budget; no new copper beyond FCX/FQM/Teck/Chinalco (miss).",
        "hunt_energy_solar": "Cycle 12: equal budget; thick set — miss.",
        "hunt_br_power_equip": "Cycle 12: equal budget; thick subcategory — miss.",
        "hunt_infra_port_cranes": "Cycle 12: logged konecranes_cartagena_rtg_2025.",
        "hunt_infra_port_ownership": "Cycle 12: equal budget; no new port ownership beyond APM/Hutchison/DP World/ICTSI (miss).",
        "hunt_energy_fission_smr": "Cycle 12: equal budget; MCTI/Finep page unreachable/JS-empty; Brazil microreactor already logged (miss).",
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
    print("Cycle 12 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
