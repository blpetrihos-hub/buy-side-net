#!/usr/bin/env python3
"""Cycle 54 hunt: shuffle_seed=20261054; equal budget; U.S. side ≥1/3; thin_topup after.

Order: wind, lithium, nickel, graphite, niobium, water, rail, other_renewables, solar,
copper, fission_smr, port_cranes, power_plants_grid, engineering_epc, port_ownership,
bridges_roads, building_materials, balsa.
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
# 6 resources/water — Fluence / ArcelorMittal Tubarão SWRO (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fluence_arcelormittal_tubarao_desal_2021",
        "layer": "resources",
        "subcategory": "water",
        "side": "us",
        "counterpart": "Fluence — ArcelorMittal Tubarão seawater desalination plant",
        "country": "Brazil",
        "asset": "Fluence South America installed a seawater desalination plant at ArcelorMittal Tubarão (Vitória, Espírito Santo) producing 12,000 m³/day (3.1 MGD / 500 m³/h) industrial demineralized water via disk filters + 7 UF trains + 5 two-pass RO trains with energy recovery; commissioned 2021 and cited by Fluence as Brazil’s largest industrial SWRO, modularly expandable toward 1,500 m³/h. Brazilian trade press (Tratamento de Água) attributes R$ 50 million CapEx — UNVERIFIED proxy vs Fluence case page (no CapEx).",
        "investment_type": "plant",
        "value": "50000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2021-09-01",
        "year": "2021",
        "status": "active",
        "lat": "-20.25",
        "lon": "-40.22",
        "geo_note": "ArcelorMittal Tubarão steel complex, Vitória / Serra coast, Espírito Santo.",
        "evidence": "proxy",
        "source_id": "fluence_tubarao_case",
        "note": "Actor: Fluence Corp (U.S./Nasdaq; Plymouth, MN HQ) EPC for ArcelorMittal Brazil — us. Fluence case documents capacity/technology/COD 2021; R$50m CapEx is UNVERIFIED Brazilian press figure. Distinct from Acciona/IDE/SADDN Chile desal rows.",
    },
    {
        "id": "fluence_arcelormittal_tubarao_desal_2021",
        "retrieved": "2026-10-01",
        "source_id": "fluence_tubarao_case",
        "url": "https://www.fluencecorp.com/case/seawater-desalination-for-industrial-water-company/",
        "price_year": "2021",
        "evidence": "proxy",
        "quote": "The desalination water treatment project installed by Fluence South America at the Arcelor Mittal Tubarão facility has the ability to produce 3.1 MGD (12,000 m³/day) of treated water. … The Arcelor Mittal Tubarão desalination water treatment plant has demonstrated, since its commissioning in 2021, that the desalination of seawater is a sustainable and acceptable alternative to meeting industrial facility water demands.",
        "note": "Opened Fluence Tubarão SWRO case study; CapEx from secondary PT press only.",
    },
    {
        "id": "fluence_tubarao_case",
        "type": "company",
        "chicago": "Fluence Corporation. “Seawater Desalination for Industrial Water Company.” Case study (ArcelorMittal Tubarão, Vitória, Brazil).",
        "url": "https://www.fluencecorp.com/case/seawater-desalination-for-industrial-water-company/",
        "annotation": "Fluence primary on Tubarão 12,000 m³/day industrial SWRO (COD 2021). CapEx R$50m is secondary PT press only. Supports fluence_arcelormittal_tubarao_desal_2021.",
        "supports": ["fluence_arcelormittal_tubarao_desal_2021", "hunt_res_water"],
    },
)

# ---------------------------------------------------------------------------
# 7 infrastructure/rail — CCECC/Aldesa Querétaro–Irapuato workshops (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ccecc_aldesa_queretaro_irapuato_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "prc",
        "counterpart": "CCECC / Aldesa — Querétaro–Irapuato passenger-rail supporting works",
        "country": "Mexico",
        "asset": "5 Mar 2026 (Aldesa) / 24 Mar 2026 (MexCham): ATTRAPI awards consortium including China Civil Engineering Construction Corporation (CCECC; CRCC subsidiary) and Aldesa Group (CRCC-controlled) the design/build of four auxiliary buildings (refueling, workshops, coach yards, maintenance base) on the Querétaro–Irapuato passenger rail corridor; Aldesa states contract value MXN 3,279 million (~EUR 160 million); works start March 2026 through July 2028; MexCham cites ~226,000 m² construction area and ~4.3 km of related track/systems. Distinct from Motá-Engil QI mainline tramos.",
        "investment_type": "epc_contract",
        "value": "3279000000",
        "currency": "MXN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2026-03-05",
        "year": "2026",
        "status": "active",
        "lat": "20.59",
        "lon": "-100.39",
        "geo_note": "Querétaro–Irapuato passenger corridor (Bajío); pin at Querétaro metro approximate.",
        "evidence": "documented",
        "source_id": "aldesa_queretaro_irapuato_20260305",
        "note": "Actor: CCECC/CRCC + Aldesa (PRC-controlled) — prc. Aldesa company primary states MXN 3,279m / EUR 160m; USD left blank (no official FX). Complements mota_engil_qi_tramo1/2 mainline rows.",
    },
    {
        "id": "ccecc_aldesa_queretaro_irapuato_2026",
        "retrieved": "2026-10-01",
        "source_id": "aldesa_queretaro_irapuato_20260305",
        "url": "https://aldesa.com/aldesa-participara-en-el-desarrollo-de-infraestructuras-clave-del-tren-de-pasajeros-queretaro-irapuato-en-mexico/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "El contrato ha sido adjudicado por la Agencia de Trenes y Transporte Público Integrado (ATTRAPI) … a un consorcio internacional en el que participa Aldesa junto a varias compañías del sector. El importe total del contrato asciende a 3.279 millones de pesos mexicanos (160 millones de euros) y los trabajos tienen previsto iniciarse en este mes de marzo. El proyecto contempla el diseño y construcción de cuatro instalaciones auxiliares destinadas a zonas de repostaje, talleres, cocheras y una base de mantenimiento.",
        "note": "Opened Aldesa Querétaro–Irapuato supporting-works award release.",
    },
    {
        "id": "aldesa_queretaro_irapuato_20260305",
        "type": "company",
        "chicago": "Aldesa Construcción. “Aldesa Participará en el Desarrollo de Infraestructuras Clave del Tren de Pasajeros Querétaro–Irapuato en México.” 5 March 2026.",
        "url": "https://aldesa.com/aldesa-participara-en-el-desarrollo-de-infraestructuras-clave-del-tren-de-pasajeros-queretaro-irapuato-en-mexico/",
        "annotation": "Aldesa primary on ATTRAPI award of MXN 3,279m Querétaro–Irapuato auxiliary rail facilities (CCECC/Aldesa consortium). Supports ccecc_aldesa_queretaro_irapuato_2026.",
        "supports": ["ccecc_aldesa_queretaro_irapuato_2026", "hunt_latam_rail_telecom"],
    },
)

# ---------------------------------------------------------------------------
# 8 energy/other_renewables — ContourGlobal Quillagua inauguration (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "contourglobal_quillagua_inaug_2025",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "ContourGlobal (KKR) — Quillagua solar + BESS inauguration",
        "country": "Chile",
        "asset": "8 Apr 2025: ContourGlobal inaugurates Quillagua I+II hybrid plant in María Elena (Antofagasta) — 221 MWp PV + 1.2 GWh / 200 MW×6.2h BESS — cited as Latin America’s largest solar-plus-storage plant at commissioning; long-term overnight PPA; COD expected within weeks of inauguration. Acquired from Grenergy end-2024 with Víctor Jara. Distinct from contourglobal_oasis_atacama_ev_2024 (portfolio EV), contourglobal_victor_jara_cod_2026, and contourglobal_los_maitenes_chile_2026.",
        "investment_type": "plant_cod",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2025-04-08",
        "year": "2025",
        "status": "active",
        "lat": "-21.67",
        "lon": "-69.65",
        "geo_note": "Quillagua, comuna María Elena, Antofagasta Region (ContourGlobal plant geography).",
        "evidence": "documented",
        "source_id": "contourglobal_quillagua_20250408",
        "note": "Actor: ContourGlobal (KKR-backed U.S. ownership) — us. Company English inauguration release; CapEx USD not restated on page (prior EV acquisition logged separately).",
    },
    {
        "id": "contourglobal_quillagua_inaug_2025",
        "retrieved": "2026-10-01",
        "source_id": "contourglobal_quillagua_20250408",
        "url": "https://www.contourglobal.com/news/contourglobal-inaugurates-latin-americas-largest-solar-plant-battery-storage-chile/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Quillagua is a 221 MWp photovoltaic solar plant with a 1.2 GWh battery storage system, capable of delivering 200 MW for 6.2 hours after sunset, making it the largest solar plant with a storage system in Latin America. This milestone marks the final stage before commencing commercial operation in the coming weeks and starting to fulfill its long-term clean energy purchase agreement (PPA).",
        "note": "Opened ContourGlobal Quillagua inauguration release.",
    },
    {
        "id": "contourglobal_quillagua_20250408",
        "type": "company",
        "chicago": "ContourGlobal. “ContourGlobal Inaugurates Latin America’s Largest Solar Plant with Battery Storage in Chile.” 8 April 2025.",
        "url": "https://www.contourglobal.com/news/contourglobal-inaugurates-latin-americas-largest-solar-plant-battery-storage-chile/",
        "annotation": "ContourGlobal primary on Quillagua 221 MWp + 1.2 GWh BESS inauguration. Supports contourglobal_quillagua_inaug_2025.",
        "supports": ["contourglobal_quillagua_inaug_2025", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# 9 energy/solar — POWERCHINA Palmira III handover (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "powerchina_palmira_iii_colombia_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "POWERCHINA — Solar Palmira III EPC/O&M handover (Celsia)",
        "country": "Colombia",
        "asset": "30 Jun 2026: POWERCHINA receives final acceptance certificate from Celsia Colombia S.A. E.S.P. for Solar Palmira III (Valle del Cauca) — 9.9 MWac / 12.56 MWdc standardized EPC plus two years O&M — company’s first fully delivered solar plant in Colombia (English release 17 Jul 2026). Distinct from powerchina_francisco_juana_colombia_2026 and Guayepo III.",
        "investment_type": "epc_om_handover",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2026-06-30",
        "year": "2026",
        "status": "active",
        "lat": "3.54",
        "lon": "-76.30",
        "geo_note": "Palmira, Valle del Cauca (POWERCHINA Colombia project geography).",
        "evidence": "documented",
        "source_id": "powerchina_palmira_iii_20260717",
        "note": "Actor: POWERCHINA (PRC) EPC/O&M for Celsia — prc. Company English primary; CapEx USD not disclosed on opened page.",
    },
    {
        "id": "powerchina_palmira_iii_colombia_2026",
        "retrieved": "2026-10-01",
        "source_id": "powerchina_palmira_iii_20260717",
        "url": "https://en.powerchina.cn/2026-07/17/c_829100.htm",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The Solar Palmira III Project in Colombia, constructed by POWERCHINA, received its final acceptance certificate on June 30 from the owner, Celsia Colombia S.A. E.S.P., marking the completion of EPC construction and two years of operations and maintenance (O&M), making it POWERCHINA’s first delivered solar power plant in Colombia. Developed under a standardized EPC model, the project features a capacity of 9.9 MWac and 12.56 MWdc.",
        "note": "Opened POWERCHINA English Palmira III handover release.",
    },
    {
        "id": "powerchina_palmira_iii_20260717",
        "type": "company",
        "chicago": "POWERCHINA. “POWERCHINA Hands Over First Solar Power Plant in Colombia.” 17 July 2026.",
        "url": "https://en.powerchina.cn/2026-07/17/c_829100.htm",
        "annotation": "POWERCHINA primary on Palmira III 9.9 MWac / 12.56 MWdc final acceptance. Supports powerchina_palmira_iii_colombia_2026.",
        "supports": ["powerchina_palmira_iii_colombia_2026", "hunt_energy_solar"],
    },
)

# ---------------------------------------------------------------------------
# 12 infrastructure/port_cranes — SSA MIT Panama +6 ZPMC ASC (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ssa_mit_asc_zpmc_2024",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "us",
        "counterpart": "SSA Marine MIT — six additional ZPMC automated stacking cranes",
        "country": "Panama",
        "asset": "18 Oct 2024: SSA Marine Manzanillo International Terminal (MIT, Colón) takes delivery of six new ZPMC automated stacking cranes (ASC), doubling the prior six-ASC fleet operating since 2014; each ASC rated 40 t lift / 21 m height / 12-wide stacking with dual-end load/unload — part of MIT yard-automation expansion. CapEx USD not disclosed on opened Spanish trade coverage (Seatrade Maritime via MundoMarítimo). Distinct from ssa_guaymas_sts_ertg_2026 and ssa_manzanillo_sts_21m_2025 (Mexico).",
        "investment_type": "equipment_delivery",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2024-10-18",
        "year": "2024",
        "status": "active",
        "lat": "9.37",
        "lon": "-79.88",
        "geo_note": "Manzanillo International Terminal (MIT), Colón, Atlantic Panama.",
        "evidence": "documented",
        "source_id": "mundomaritimo_ssa_mit_asc_20241018",
        "note": "Actor: SSA Marine / Carrix (U.S.) terminal receiving ZPMC (PRC OEM) ASCs — coded us (operator/investor side, consistent with ssa_guaymas_sts_ertg_2026). MundoMarítimo Spanish trade coverage of Seatrade Maritime report.",
    },
    {
        "id": "ssa_mit_asc_zpmc_2024",
        "retrieved": "2026-10-01",
        "source_id": "mundomaritimo_ssa_mit_asc_20241018",
        "url": "https://www.mundomaritimo.cl/noticias/ssa-marine-mit-de-panama-recibe-seis-nuevas-gruas-apiladoras-automatizadas",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "SSA Marine MIT, en Panamá, incorporó seis nuevas grúas apiladoras automatizadas (stacking cranes, ASC) a sus instalaciones. Los equipos fueron fabricados por Shanghai Zhenhua Heavy Industry Co (ZPMC) y forman parte de un plan de expansión para incrementar la productividad de la terminal, indicó Seatrade Maritime. Las nuevas grúas se suman a otras seis similares que han estado en operación desde 2014. Cada una de las ASC tiene una capacidad de elevación de 40 toneladas y una altura máxima de 21 metros.",
        "note": "Opened MundoMarítimo Spanish coverage of SSA MIT ASC delivery.",
    },
    {
        "id": "mundomaritimo_ssa_mit_asc_20241018",
        "type": "press",
        "chicago": "MundoMarítimo. “SSA Marine MIT de Panamá Recibe Seis Nuevas Grúas Apiladoras Automatizadas.” 18 October 2024.",
        "url": "https://www.mundomaritimo.cl/noticias/ssa-marine-mit-de-panama-recibe-seis-nuevas-gruas-apiladoras-automatizadas",
        "annotation": "Spanish trade press on six ZPMC ASCs delivered to SSA Marine MIT Panama. Supports ssa_mit_asc_zpmc_2024.",
        "supports": ["ssa_mit_asc_zpmc_2024", "hunt_infra_port_cranes"],
    },
)

# ---------------------------------------------------------------------------
# 15 infrastructure/port_ownership — SSA/Blackstone Panama interest (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ssa_blackstone_panama_interest_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "us",
        "counterpart": "SSA Marine / Blackstone — Panama new-port / Canal project interest",
        "country": "Panama",
        "asset": "24 Sep 2026: Autoridad Marítima de Panamá reports President José Raúl Mulino met in New York with SSA Marine (Carrix; already operates Manzanillo International Terminal in Colón) and Blackstone Infrastructure Group; both groups, working in alliance, expressed interest in new maritime opportunities including new ports and Panama Canal-related projects. Interest/meeting stage — no named concession award or CapEx. Distinct from existing SSA Mexico concession/crane rows and CHEC Fourth Bridge.",
        "investment_type": "investment_interest",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2026-09-24",
        "year": "2026",
        "status": "active",
        "lat": "9.37",
        "lon": "-79.88",
        "geo_note": "MIT Colón / national Panama port system (interest is multi-site; pin at existing SSA MIT footprint).",
        "evidence": "documented",
        "source_id": "amp_ssa_blackstone_20260924",
        "note": "Actor: SSA Marine (U.S.) + Blackstone Infrastructure (U.S.) — us. AMP official press note; exploratory interest only — no closed concession.",
    },
    {
        "id": "ssa_blackstone_panama_interest_2026",
        "retrieved": "2026-10-01",
        "source_id": "amp_ssa_blackstone_20260924",
        "url": "https://www.amp.gob.pa/noticias/notas-de-prensa/blackstone-y-ssa-marine-muestran-interes-en-nuevas-inversiones-en-panama-tras-reunion-con-el-presidente-mulino/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "El mandatario panameño se reunió con representantes de BlackStone, la firma gestora de activos más grande del mundo; y SSA Marine, filial del grupo Carrix, el mayor operador de terminales marítimas de Estados Unidos y América, que tiene en Panamá participación en el puerto de Mazanillo, Colón. Ambos grupos, que trabajan en alianza, mostraron interés en participar de las nuevas oportunidades marítimas que se abrirán en Panamá, principalmente con los nuevos puertos y proyectos en el Canal de Panamá.",
        "note": "Opened AMP official SSA/Blackstone Panama interest release.",
    },
    {
        "id": "amp_ssa_blackstone_20260924",
        "type": "agency",
        "chicago": "Autoridad Marítima de Panamá. “Blackstone y SSA Marine Muestran Interés en Nuevas Inversiones en Panamá, Tras Reunión con el Presidente Mulino.” 24 September 2026.",
        "url": "https://www.amp.gob.pa/noticias/notas-de-prensa/blackstone-y-ssa-marine-muestran-interes-en-nuevas-inversiones-en-panama-tras-reunion-con-el-presidente-mulino/",
        "annotation": "AMP primary on SSA Marine/Blackstone Panama port/Canal investment interest meeting. Supports ssa_blackstone_panama_interest_2026.",
        "supports": ["ssa_blackstone_panama_interest_2026", "hunt_infra_port_ownership"],
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
        "hunt_energy_wind": "Cycle 54: equal budget; Vestas Esquina / Goldwind Sento Sé / IFC Olavarría already (miss).",
        "hunt_res_lithium": "Cycle 54: equal budget; Atlas Neves DFS / EnergyX EXIM / Albemarle TED already (miss).",
        "hunt_res_nickel": "Cycle 54: equal budget; DFC Piauí / Westwin offtake / Jervois SMP already (miss).",
        "hunt_res_graphite": "Cycle 54: equal budget; Atlas Malacacheta MRE / Graphcoa / South Star already (miss).",
        "hunt_fenb_araxa": "Cycle 54: equal budget; Boston Metal Coronel Xavier / CBMM XNO / CMOC Catalão already (miss).",
        "hunt_res_water": "Cycle 54: logged fluence_arcelormittal_tubarao_desal_2021 (U.S.; 12,000 m³/day Tubarão SWRO; R$50m proxy).",
        "hunt_latam_rail_telecom": "Cycle 54: logged ccecc_aldesa_queretaro_irapuato_2026 (PRC; MXN 3,279m QI workshops).",
        "hunt_energy_other_renewables": "Cycle 54: logged contourglobal_quillagua_inaug_2025 (U.S.; 221 MWp + 1.2 GWh BESS).",
        "hunt_energy_solar": "Cycle 54: logged powerchina_palmira_iii_colombia_2026 (PRC; 9.9 MWac / 12.56 MWdc handover).",
        "hunt_res_copper": "Cycle 54: equal budget; FCX El Abra / Cerro Verde MEIA2 / MMG Las Bambas already (miss).",
        "hunt_energy_fission_smr": "Cycle 54: equal budget; Meitner ACR-300 / El Salvador 123 / CNNC dialogue already (miss).",
        "hunt_infra_port_cranes": "Cycle 54: logged ssa_mit_asc_zpmc_2024 (U.S.; six ZPMC ASCs at MIT Colón).",
        "hunt_br_power_equip": "Cycle 54: equal budget; GE Vernova Azulão / USTDA Ecuador / Hitachi already (miss).",
        "hunt_infra_engineering_epc": "Cycle 54: equal budget; Bechtel EIMISA / KBR Pampa / Fluor already (miss).",
        "hunt_infra_port_ownership": "Cycle 54: logged ssa_blackstone_panama_interest_2026 (U.S.; AMP Mulino meeting).",
        "hunt_infra_bridges_roads": "Cycle 54: equal budget; CHEC Jamaica N-S / Itaparica / Panamericana already (miss).",
        "hunt_infra_building_materials": "Cycle 54: equal budget; Huaxin CSN bid / Holcim Pacasmayo already (miss).",
        "hunt_res_balsa": "Cycle 54: equal budget; Plantabal 2,951 ha / CoreLite / WITS already (miss).",
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
    print("Cycle 54 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
