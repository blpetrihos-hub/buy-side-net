#!/usr/bin/env python3
"""Cycle 56 hunt: shuffle_seed=20261056; equal budget; U.S. ≥1/3; thin after.

Order: lithium, bridges_roads, engineering_epc, fission_smr, port_cranes, rail, balsa,
water, nickel, port_ownership, other_renewables, niobium, building_materials, solar,
wind, power_plants_grid, graphite, copper.
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
# 1 lithium — Mitsui Atlas Neves equity+offtake (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "mitsui_atlas_neves_30m_offtake_2024",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "allied",
        "counterpart": "Mitsui — Atlas Lithium Neves equity + concentrate offtake",
        "country": "Brazil",
        "asset": "28 Mar 2024 Atlas Lithium / Newsfile: Mitsui & Co. purchases USD 30 million Atlas Lithium common shares (10% premium to 5-day VWAP) and signs offtake for 15,000 t Phase 1 spodumene concentrate (one shipment) plus minimum 60,000 t/year for five years from Neves Phase 2 (Minas Gerais Lithium Valley). Distinct from atlas_lithium_neves_dfs_57p6m_2025 and atlas_lithium_neves_71pct_capex_2026.",
        "investment_type": "offtake",
        "value": "30000000",
        "currency": "USD",
        "value_usd": "30000000",
        "fx_usd": "1",
        "fx_date": "2024-03-28",
        "year": "2024",
        "status": "active",
        "lat": "-16.85",
        "lon": "-42.07",
        "geo_note": "Neves / Araçuaí Lithium Valley, Minas Gerais.",
        "evidence": "documented",
        "source_id": "atlas_mitsui_30m_20240328",
        "note": "Actor: Mitsui (Japan) equity+offtake into U.S.-listed Atlas Lithium Neves — allied. Company primary.",
    },
    {
        "id": "mitsui_atlas_neves_30m_offtake_2024",
        "retrieved": "2026-10-01",
        "source_id": "atlas_mitsui_30m_20240328",
        "url": "https://www.atlas-lithium.com/news/atlas-lithium-secures-us-30000000-strategic-investment-and-offtake-agreement-from-mitsui/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Mitsui is purchasing US$ 30,000,000 in common shares of Atlas Lithium at a 10% premium to the 5-day VWAP (the “Strategic Investment”) and at the same time entering into an Offtake Agreement (the “Offtake”) for the future purchase of 15,000 tons of lithium concentrate from Phase 1 and 60,000 tons per year for five years from Phase 2 of Atlas Lithium’s soon to be producing Neves Project in Brazil’s Lithium Valley.",
        "note": "Opened Atlas Lithium Mitsui investment/offtake release.",
    },
    {
        "id": "atlas_mitsui_30m_20240328",
        "type": "company",
        "chicago": "Atlas Lithium Corporation. “Atlas Lithium Secures US$ 30,000,000 Strategic Investment and Offtake Agreement from Mitsui.” 28 March 2024.",
        "url": "https://www.atlas-lithium.com/news/atlas-lithium-secures-us-30000000-strategic-investment-and-offtake-agreement-from-mitsui/",
        "annotation": "Atlas primary on Mitsui USD 30m equity and Neves offtake. Supports mitsui_atlas_neves_30m_offtake_2024.",
        "supports": ["mitsui_atlas_neves_30m_offtake_2024", "hunt_res_lithium"],
    },
)

# ---------------------------------------------------------------------------
# 2 bridges_roads — USACE Guatemala priority roads LOA (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "usace_guatemala_roads_110m_2026",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "us",
        "counterpart": "USACE — Guatemala priority roads/highways/overpasses LOA",
        "country": "Guatemala",
        "asset": "15 Jan 2026: Guatemala signs Letters of Offer and Acceptance with U.S. Army Corps of Engineers (USACE) via Ministry of Defense / CIV; Government of Guatemala assigns USD 110 million for critical road infrastructure (design/execution of priority roads, highways, overpasses) with USACE technical assistance; six priority projects to be designed in ~6 months and finished before Jan 2028 (Emisoras Unidas / Prensa Libre summarizing U.S. Embassy). Fully financed by Guatemala; USACE provides technical assistance. Same ceremony package as Quetzal rail study and port LOA expansion (logged separately).",
        "investment_type": "epc_design_build",
        "value": "110000000",
        "currency": "USD",
        "value_usd": "110000000",
        "fx_usd": "1",
        "fx_date": "2026-01-15",
        "year": "2026",
        "status": "active",
        "lat": "14.63",
        "lon": "-90.51",
        "geo_note": "Guatemala City / national priority-road package (approximate capital pin).",
        "evidence": "proxy",
        "source_id": "prensa_libre_usace_gt_20260115",
        "note": "Actor: USACE (U.S.) technical assistance — us. USD 110m is Guatemalan funding covering roads+rail studies package; road component not separately priced — UNVERIFIED allocation proxy for full package figure on opened press.",
    },
    {
        "id": "usace_guatemala_roads_110m_2026",
        "retrieved": "2026-10-01",
        "source_id": "prensa_libre_usace_gt_20260115",
        "url": "https://www.prensalibre.com/ahora/guatemala/comunitario/ee-uu-y-guatemala-firman-acuerdos-clave-para-mejorar-caminos-y-reactivar-sistema-ferroviario/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Guatemala firmó dos Cartas de Oferta y Aceptación con el Cuerpo de Ingenieros del Ejército de EE. UU., a través del Ministerio de la Defensa y con apoyo del CIV, para mejorar caminos, modernizar Puerto Quetzal y realizar estudios ferroviarios entre ese puerto y Escuintla, con una inversión de US$110 millones.",
        "note": "Opened Prensa Libre; Emisoras Unidas corroborates six road projects + USACE LOAs.",
    },
    {
        "id": "prensa_libre_usace_gt_20260115",
        "type": "press",
        "chicago": "Gutiérrez, Erick. “Guatemala Invertirá US$110 Millones con Apoyo de EE. UU. para Modernizar Caminos y Reactivar Red Ferroviaria.” Prensa Libre, 15 January 2026.",
        "url": "https://www.prensalibre.com/ahora/guatemala/comunitario/ee-uu-y-guatemala-firman-acuerdos-clave-para-mejorar-caminos-y-reactivar-sistema-ferroviario/",
        "annotation": "Opened Guatemalan press on USACE LOAs / USD 110m package. Supports usace_guatemala_roads_110m_2026 and related Quetzal rows.",
        "supports": [
            "usace_guatemala_roads_110m_2026",
            "usace_guatemala_quetzal_rail_2026",
            "usace_guatemala_quetzal_port_2026",
            "hunt_infra_bridges_roads",
        ],
    },
)

# ---------------------------------------------------------------------------
# 6 rail — USACE Quetzal–Escuintla industrial rail study (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "usace_guatemala_quetzal_rail_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "us",
        "counterpart": "USACE — Puerto Quetzal–Escuintla industrial rail conceptual design",
        "country": "Guatemala",
        "asset": "15 Jan 2026 USACE/Guatemala LOA package: comprehensive study and conceptual designs for an industrial rail system connecting Puerto Quetzal to a multimodal logistics station in Escuintla municipality; USACE technical assistance; Guatemalan funding within the USD 110 million assignment (press). Distinct from road LOA and Quetzal port modernization LOA expansion.",
        "investment_type": "epc_design_build",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "14.30",
        "lon": "-90.79",
        "geo_note": "Escuintla multimodal hub / Quetzal corridor (approximate Escuintla pin).",
        "evidence": "documented",
        "source_id": "emisoras_usace_gt_20260115",
        "note": "Actor: USACE — us. Study/design stage; CapEx for construction not disclosed.",
    },
    {
        "id": "usace_guatemala_quetzal_rail_2026",
        "retrieved": "2026-10-01",
        "source_id": "emisoras_usace_gt_20260115",
        "url": "https://emisorasunidas.com/nacional/2026/01/15/gobierno-presenta-proyectos-prioritarios-de-infraestructura/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "el Gobierno guatemalteco asignó $110 millones para mejorar la infraestructura vial crítica y para realizar estudios integrales y preparar los diseños conceptuales para la integración de un sistema ferroviario que conecte Puerto Quetzal con una estación logística multimodal en Escuintla, por medio del Cuerpo de Ingenieros del Ejército de Estados Unidos (USACE).",
        "note": "Opened Emisoras Unidas citing U.S. Embassy on Quetzal–Escuintla rail study.",
    },
    {
        "id": "emisoras_usace_gt_20260115",
        "type": "press",
        "chicago": "García, Jose. “Gobierno Presenta Proyectos Prioritarios de Infraestructura.” Emisoras Unidas, 15 January 2026.",
        "url": "https://emisorasunidas.com/nacional/2026/01/15/gobierno-presenta-proyectos-prioritarios-de-infraestructura/",
        "annotation": "Opened Emisoras Unidas on USACE Quetzal–Escuintla rail designs. Supports usace_guatemala_quetzal_rail_2026.",
        "supports": ["usace_guatemala_quetzal_rail_2026", "hunt_latam_rail_telecom"],
    },
)

# ---------------------------------------------------------------------------
# 9 nickel — Bravo Luanga PFS CapEx (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "bravo_luanga_pfs_785m_2026",
        "layer": "resources",
        "subcategory": "nickel",
        "side": "allied",
        "counterpart": "Bravo Mining — Luanga PGM+Ni PFS pre-production CapEx",
        "country": "Brazil",
        "asset": "22 Sep 2026 Bravo Mining (TSX.V:BRVO) PFS for 100%-owned Luanga palladium-platinum-rhodium-gold-nickel deposit, Carajás (Pará): pre-production CapEx USD 784.9 million (mine/plant USD 603.6m + Barcarena ZPE smelter USD 181.3m); after-tax NPV8% USD 1.45bn; IRR 35.1%. Includes Ni price assumption USD 7.71/lb. Study-stage CapEx — not FID. Distinct from Centaurus Jaguar / Atlantic Nickel Santa Rita.",
        "investment_type": "capex",
        "value": "784900000",
        "currency": "USD",
        "value_usd": "784900000",
        "fx_usd": "1",
        "fx_date": "2026-09-22",
        "year": "2026",
        "status": "active",
        "lat": "-6.05",
        "lon": "-50.05",
        "geo_note": "Luanga deposit, Carajás Mineral Province, Pará (approximate).",
        "evidence": "documented",
        "source_id": "bravo_luanga_pfs_20260922",
        "note": "Actor: Bravo Mining (Canada-listed) — allied. Company PFS release; PGM-primary with nickel byproduct/credit — booked under nickel scarce-resource chain.",
    },
    {
        "id": "bravo_luanga_pfs_785m_2026",
        "retrieved": "2026-10-01",
        "source_id": "bravo_luanga_pfs_20260922",
        "url": "https://bravomining.cl1.adnetcms.com/site/assets/files/6350/2026-09-22-nr-bravo.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Pre-production capital expenditures (“CAPEX”) of US$784.9 million and life-of-mine (“LOM”) sustaining CAPEX of US$98.2 million. … TOTAL Pre-Production CAPEX 784.9",
        "note": "Opened Bravo 22 Sep 2026 PFS news-release PDF.",
    },
    {
        "id": "bravo_luanga_pfs_20260922",
        "type": "company",
        "chicago": "Bravo Mining Corp. “Bravo Reports Results of Pre-Feasibility Study for Its Luanga Project.” News release PDF, 22 September 2026.",
        "url": "https://bravomining.cl1.adnetcms.com/site/assets/files/6350/2026-09-22-nr-bravo.pdf",
        "annotation": "Bravo primary PFS with USD 784.9m pre-production CapEx. Supports bravo_luanga_pfs_785m_2026.",
        "supports": ["bravo_luanga_pfs_785m_2026", "hunt_res_nickel"],
    },
)

# ---------------------------------------------------------------------------
# 10 port_ownership — USACE Puerto Quetzal modernization LOA expansion (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "usace_guatemala_quetzal_port_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "us",
        "counterpart": "USACE — Puerto Quetzal modernization LOA expansion",
        "country": "Guatemala",
        "asset": "15 Jan 2026: USACE/Guatemala LOA package expands prior LOA for modernization of Puerto Quetzal (Empresa Portuaria Quetzal), fully financed by Government of Guatemala with USACE technical assistance (Prensa Libre / Emisoras Unidas). Distinct from Quetzal–Escuintla rail study and priority-roads LOA in same ceremony.",
        "investment_type": "epc_design_build",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "13.92",
        "lon": "-90.72",
        "geo_note": "Puerto Quetzal, Escuintla Department, Pacific coast, Guatemala.",
        "evidence": "documented",
        "source_id": "prensa_libre_usace_gt_20260115",
        "note": "Actor: USACE — us. Port modernization technical assistance; construction CapEx not disclosed on opened pages.",
    },
    {
        "id": "usace_guatemala_quetzal_port_2026",
        "retrieved": "2026-10-01",
        "source_id": "prensa_libre_usace_gt_20260115",
        "url": "https://www.prensalibre.com/ahora/guatemala/comunitario/ee-uu-y-guatemala-firman-acuerdos-clave-para-mejorar-caminos-y-reactivar-sistema-ferroviario/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Puerto Quetzal: Ampliación de una LOA previa para continuar su modernización con fondos nacionales.",
        "note": "Opened Prensa Libre bullet on Quetzal LOA expansion.",
    },
    {
        "id": "prensa_libre_usace_gt_20260115",
        "type": "press",
        "chicago": "Gutiérrez, Erick. “Guatemala Invertirá US$110 Millones con Apoyo de EE. UU. para Modernizar Caminos y Reactivar Red Ferroviaria.” Prensa Libre, 15 January 2026.",
        "url": "https://www.prensalibre.com/ahora/guatemala/comunitario/ee-uu-y-guatemala-firman-acuerdos-clave-para-mejorar-caminos-y-reactivar-sistema-ferroviario/",
        "annotation": "Opened Guatemalan press on USACE Quetzal port LOA expansion. Supports usace_guatemala_quetzal_port_2026.",
        "supports": [
            "usace_guatemala_roads_110m_2026",
            "usace_guatemala_quetzal_rail_2026",
            "usace_guatemala_quetzal_port_2026",
            "hunt_infra_port_ownership",
        ],
    },
)

# ---------------------------------------------------------------------------
# 14 solar — Thermion CFE mixed awards (other)
# ---------------------------------------------------------------------------
A(
    {
        "id": "thermion_cfe_mexico_1600mw_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "other",
        "counterpart": "Thermion Energy — CFE mixed-development solar portfolio",
        "country": "Mexico",
        "asset": "Jun 2026 Energy21: Mexican developer Thermion Energy leads CFE First Call mixed-development awards with >1,600 MW across six solar plants and one hybrid project in Sonora, northeast, and Yucatán Peninsula; press cites ~USD 1.6 billion generation CapEx plus ~480 MW BESS (~USD 432 million) — UNVERIFIED proxies. Distinct from Oak Creek / Cubico CFE rows.",
        "investment_type": "plant",
        "value": "1600000000",
        "currency": "USD",
        "value_usd": "1600000000",
        "fx_usd": "1",
        "fx_date": "2026-06-16",
        "year": "2026",
        "status": "active",
        "lat": "29.09",
        "lon": "-110.97",
        "geo_note": "Sonora cluster among Thermion awards (approximate Hermosillo pin).",
        "evidence": "proxy",
        "source_id": "energy21_thermion_cfe_2026",
        "note": "Actor: Thermion Energy (Mexican) — other. MW award documented; USD figures UNVERIFIED press proxies.",
    },
    {
        "id": "thermion_cfe_mexico_1600mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "energy21_thermion_cfe_2026",
        "url": "https://energy21.com.mx/cuatro-empresas-acaparan-el-55-de-los-contratos-mixtos-de-cfe/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "La empresa mexicana Thermion Energy emerge como el actor dominante. La firma obtuvo más de mil 600 MW distribuidos en seis plantas solares y un proyecto híbrido en Sonora, el noreste y la Península de Yucatán. Su portafolio implica una inversión cercana a los mil 600 millones de dólares.",
        "note": "Opened Energy21 on Thermion CFE awards; CapEx UNVERIFIED.",
    },
    {
        "id": "energy21_thermion_cfe_2026",
        "type": "press",
        "chicago": "Arias, Adrián. “Cuatro Empresas Acaparan el 55% de los Contratos Mixtos de CFE.” Energy21, 16 June 2026.",
        "url": "https://energy21.com.mx/cuatro-empresas-acaparan-el-55-de-los-contratos-mixtos-de-cfe/",
        "annotation": "Opened Mexican energy press on Thermion >1,600 MW CFE awards. Supports thermion_cfe_mexico_1600mw_2026.",
        "supports": ["thermion_cfe_mexico_1600mw_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# lithium/us — EnergyX Black Giant CapEx estimate (us) complementary to Eni/EXIM
# ---------------------------------------------------------------------------
A(
    {
        "id": "energyx_black_giant_capex_1bn_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "us",
        "counterpart": "EnergyX — Black Giant project CapEx estimate (Chile)",
        "country": "Chile",
        "asset": "6 Jul 2026 EnergyX company release: Project Black Giant (Antofagasta / Salar de Punta Negra) total capital expenditure estimated just below USD 1 billion including financing costs for first two phases (52.5 ktpa LCE); Eni USD 225m equity and EXIM USD 690m debt LOI cited as financing stack. Distinct from eni_energyx_black_giant_2026 (Eni equity) and energyx_exim_loi_690m_black_giant_2025 (EXIM LOI).",
        "investment_type": "capex",
        "value": "1000000000",
        "currency": "USD",
        "value_usd": "1000000000",
        "fx_usd": "1",
        "fx_date": "2026-07-06",
        "year": "2026",
        "status": "active",
        "lat": "-24.58",
        "lon": "-69.00",
        "geo_note": "Salar de Punta Negra / Domeyko Range, Antofagasta Region (approximate).",
        "evidence": "proxy",
        "source_id": "energyx_eni_black_giant_20260706",
        "note": "Actor: EnergyX (U.S./Austin) — us. Company states CapEx 'just below $1 billion' — UNVERIFIED rounded proxy stored as USD 1bn.",
    },
    {
        "id": "energyx_black_giant_capex_1bn_2026",
        "retrieved": "2026-10-01",
        "source_id": "energyx_eni_black_giant_20260706",
        "url": "https://energyx.com/press-release/energyx-eni-strategic-investment/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "While the total capital expenditure into the project is estimated just below $1 billion, including financing costs, once the first two phases are fully operational, Project Black Giant™ is expected to generate approximately $1.3 billion in annual gross revenue based on current lithium prices of $25,000 per metric tonne as of May 2026.",
        "note": "Opened EnergyX primary; CapEx phrased as just below USD 1bn.",
    },
    {
        "id": "energyx_eni_black_giant_20260706",
        "type": "company",
        "chicago": "Energy Exploration Technologies, Inc. “EnergyX Secures $225 Million Strategic Investment from Eni to Advance the Black Giant™ Lithium Project in Chile.” 6 July 2026.",
        "url": "https://energyx.com/press-release/energyx-eni-strategic-investment/",
        "annotation": "EnergyX primary stating Black Giant CapEx just below USD 1bn. Supports energyx_black_giant_capex_1bn_2026.",
        "supports": ["energyx_black_giant_capex_1bn_2026", "hunt_res_lithium"],
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
        "hunt_res_lithium": "Cycle 56: logged mitsui_atlas_neves_30m_offtake_2024 (allied) + energyx_black_giant_capex_1bn_2026 (U.S.).",
        "hunt_infra_bridges_roads": "Cycle 56: logged usace_guatemala_roads_110m_2026 (U.S.; USACE LOA / USD 110m package proxy).",
        "hunt_infra_engineering_epc": "Cycle 56: equal budget; Bechtel/Worley already dense (miss).",
        "hunt_energy_fission_smr": "Cycle 56: equal budget; Meitner/FIRST already (miss).",
        "hunt_infra_port_cranes": "Cycle 56: equal budget; Liebherr CICE / ZPMC already (miss).",
        "hunt_latam_rail_telecom": "Cycle 56: logged usace_guatemala_quetzal_rail_2026 (U.S.; Quetzal–Escuintla rail study).",
        "hunt_res_balsa": "Cycle 56: equal budget; Plantabal/AIMA/CoreLite already (miss).",
        "hunt_res_water": "Cycle 56: equal budget; Fluence/Acciona/Cox already (miss).",
        "hunt_res_nickel": "Cycle 56: logged bravo_luanga_pfs_785m_2026 (allied; USD 784.9m PFS CapEx).",
        "hunt_infra_port_ownership": "Cycle 56: logged usace_guatemala_quetzal_port_2026 (U.S.; Quetzal LOA expansion).",
        "hunt_energy_other_renewables": "Cycle 56: equal budget; ContourGlobal/Ormat already (miss).",
        "hunt_fenb_araxa": "Cycle 56: equal budget; Boston Metal/CBMM already (miss).",
        "hunt_infra_building_materials": "Cycle 56: equal budget; Sinoma Cruz Azul already (miss).",
        "hunt_energy_solar": "Cycle 56: logged thermion_cfe_mexico_1600mw_2026 (other; >1,600 MW CFE; CapEx proxy).",
        "hunt_energy_wind": "Cycle 56: equal budget; Oak Creek already (miss).",
        "hunt_br_power_equip": "Cycle 56: equal budget pending thin (EXIM GTE2 already).",
        "hunt_res_graphite": "Cycle 56: equal budget; Graphcoa/South Star/Atlas already (miss).",
        "hunt_res_copper": "Cycle 56: equal budget; Teck QB TMF / FCX El Abra already (miss).",
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
    print("Cycle 56 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
