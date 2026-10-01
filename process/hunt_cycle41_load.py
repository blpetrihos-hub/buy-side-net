#!/usr/bin/env python3
"""Cycle 41 hunt: shuffle_seed=20261041; equal budget across 18 subcategories."""
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


# seed 20261041 order:
# solar, port_ownership, rail, power_plants_grid, port_cranes, bridges_roads, balsa,
# engineering_epc, wind, graphite, nickel, copper, niobium, other_renewables, water,
# lithium, fission_smr, building_materials

# 1 energy/solar — Polaris–CFE Mexico mixed investment ~USD 217m
A(
    {
        "id": "polaris_cfe_mexico_solar_217m_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "allied",
        "counterpart": "Polaris Renewable Energy — CFE Mixed Investment (3 solar+BESS projects)",
        "country": "Mexico",
        "asset": "3 Jul 2026: Polaris (Canada) executes Contrato de Inversión Mixta with CFE fiduciary Banca Mifel for three solar+BESS projects — Los Girasoles (Quintana Roo, 132.57 MWdc / 33 MW·101.5 MWh, CAPEX ~USD 120m), Tres Hermanos (Tlaxcala, 91.06 MWdc / 22.5 MW·71.6 MWh, ~USD 78m), Don Humberto (Sinaloa, 25.3 MWdc / 6.1 MW·18.9 MWh, ~USD 19m); combined ~250 MWdc + 61.6 MW/192 MWh; estimated CAPEX USD 217m excl. interconnection; COD targets Apr–Dec 2028; CFE 54% stake framework.",
        "investment_type": "ownership_equity",
        "value": "217000000",
        "currency": "USD",
        "value_usd": "217000000",
        "fx_usd": "1",
        "fx_date": "2026-07-07",
        "year": "2026",
        "status": "active",
        "lat": "20.5",
        "lon": "-87.2",
        "geo_note": "Pinned to Los Girasoles / Quintana Roo (largest CAPEX site; company geography; approximate).",
        "evidence": "documented",
        "source_id": "polaris_cfe_cim_20260707",
        "note": "Actor: Polaris Renewable Energy (Canada) — allied, with CFE majority framework. Company primary 7 Jul 2026. CAPEX excl. interconnection upgrades.",
    },
    {
        "id": "polaris_cfe_mexico_solar_217m_2026",
        "retrieved": "2026-10-01",
        "source_id": "polaris_cfe_cim_20260707",
        "url": "https://polarisrei.com/wp-content/uploads/2026/07/PR-Mexico-Mixed-Investment-Agreement-Executed-July-7th.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The projects comprise approximately 250 MWdc of solar generation capacity and 61.6 MW / 192.0 MWh of battery energy storage … Los Girasoles … estimated CAPEX of US$120 million … Tres Hermanos … US$78 million … Don Humberto … US$19 million.",
        "note": "Opened Polaris company PDF 7 Jul 2026.",
    },
    {
        "id": "polaris_cfe_cim_20260707",
        "type": "company",
        "chicago": "Polaris Renewable Energy Inc. “Polaris Announces Execution of Mixed Investment Agreement for the Three Mexico Projects.” Press release, 7 July 2026.",
        "url": "https://polarisrei.com/wp-content/uploads/2026/07/PR-Mexico-Mixed-Investment-Agreement-Executed-July-7th.pdf",
        "annotation": "Company PDF on Polaris–CFE Mexico solar+BESS CIM ~USD 217m. Supports polaris_cfe_mexico_solar_217m_2026.",
        "supports": ["polaris_cfe_mexico_solar_217m_2026", "hunt_energy_solar"],
    },
)

# 2–6 port_ownership, rail, power_plants_grid, port_cranes, bridges_roads — miss

# 7 resources/balsa — AIMA–Siemens Energy MoU
A(
    {
        "id": "aima_siemens_energy_balsa_mou_2026",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "allied",
        "counterpart": "Siemens Energy — MoU with AIMA on Ecuador balsa for wind-blade cores",
        "country": "Ecuador",
        "asset": "Feb 2026 El Comercio (Líderes): Asociación Ecuatoriana de la Industria Forestal y de la Madera (AIMA) signs MoU with Siemens Energy (ministries of Production/Environment/Energy and ProEcuador accompanying) to position Ecuadorian balsa as sustainable core material for wind-turbine blades — long-term cooperation on forest sustainability, traceability (incl. EU rules), training/certification, and R&D. Presence/MoU — no CAPEX disclosed. Context: AIMA says balsa product exports >USD 270m through Nov 2025 (~+27% YoY).",
        "investment_type": "technology_mou",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-0.18",
        "lon": "-78.47",
        "geo_note": "Quito institutional MoU geography (AIMA/ministries); processing belt Guayas–Los Ríos separately mapped.",
        "evidence": "proxy",
        "source_id": "elcomercio_aima_siemens_20260210",
        "note": "Actor: Siemens Energy (Germany) — allied, with Ecuador AIMA. UNVERIFIED proxy: El Comercio 10 Feb 2026. MoU/presence; not a priced plant investment.",
    },
    {
        "id": "aima_siemens_energy_balsa_mou_2026",
        "retrieved": "2026-10-01",
        "source_id": "elcomercio_aima_siemens_20260210",
        "url": "https://www.elcomercio.com/lideres/acuerdo-balsa-ecuatoriana-actor-clave-transicion-energetica/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "La Asociación Ecuatoriana de la Industria Forestal y de la Madera (AIMA) suscribió un Memorando de Entendimiento (MoU) con Siemens Energy. … La intención es posicionar a la balsa como material de núcleo sostenible para las palas de aerogeneradores",
        "note": "Opened El Comercio Spanish (schema datePublished 2026-02-10). Mark UNVERIFIED proxy.",
    },
    {
        "id": "elcomercio_aima_siemens_20260210",
        "type": "trade_press",
        "chicago": "Astudillo, Giovanni. “Un acuerdo para que la balsa ecuatoriana sea un actor clave de la transición energética.” El Comercio (Ecuador), 10 February 2026.",
        "url": "https://www.elcomercio.com/lideres/acuerdo-balsa-ecuatoriana-actor-clave-transicion-energetica/",
        "annotation": "Press on AIMA–Siemens Energy balsa MoU. Supports aima_siemens_energy_balsa_mou_2026.",
        "supports": ["aima_siemens_energy_balsa_mou_2026", "hunt_res_balsa"],
    },
)

# 8 infrastructure/engineering_epc — CHEC/CCCC Chancay port works USD 600m
A(
    {
        "id": "chec_chancay_port_epc_600m_2021",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "prc",
        "counterpart": "CHEC SAC–CCCC4TH — Chancay port/admin zone construction contract",
        "country": "Peru",
        "asset": "May 2021 MTC: Cosco Shipping Ports Chancay Perú awards Chinese consortium CHEC SAC–CCCC4TH the principal construction contract (~USD 600 million) for Chancay multipurpose terminal portuary and administrative zone — quays, breakwaters, O&M/operations areas, maneuvering/storage and admin facilities. Distinct from cosco_chancay_port_2024 ownership/Phase I equity row and powerchina_chancay_sierra_rail_2026.",
        "investment_type": "epc",
        "value": "600000000",
        "currency": "USD",
        "value_usd": "600000000",
        "fx_usd": "1",
        "fx_date": "2021-05-25",
        "year": "2021",
        "status": "active",
        "lat": "-11.574",
        "lon": "-77.270",
        "geo_note": "Puerto de Chancay, Huaral (MTC geography).",
        "evidence": "documented",
        "source_id": "mtc_chec_chancay_600m_20210525",
        "note": "Actor: CHEC / CCCC (PRC). Official MTC release 25 May 2021. EPC construction award year within 2021–2026 window.",
    },
    {
        "id": "chec_chancay_port_epc_600m_2021",
        "retrieved": "2026-10-01",
        "source_id": "mtc_chec_chancay_600m_20210525",
        "url": "https://www.gob.pe/institucion/mtc/noticias/494826-terminal-de-chancay-firman-contrato-por-us-600-millones-para-la-zona-portuaria-del-futuro-hub-de-la-region",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "Cosco Shipping Ports Chancay Perú firmó contrato con el consorcio chino CHEC SAC-CCCC4TH para la construcción de la zona portuaria y administrativa … acuerdo de ejecución de obras por US$ 600 millones.",
        "note": "Opened Peru MTC Spanish 25 May 2021.",
    },
    {
        "id": "mtc_chec_chancay_600m_20210525",
        "type": "official",
        "chicago": "Perú. Ministerio de Transportes y Comunicaciones. “Terminal de Chancay: Firman contrato por US$ 600 millones para la zona portuaria del futuro hub de la región.” 25 May 2021.",
        "url": "https://www.gob.pe/institucion/mtc/noticias/494826-terminal-de-chancay-firman-contrato-por-us-600-millones-para-la-zona-portuaria-del-futuro-hub-de-la-region",
        "annotation": "MTC notice on CHEC/CCCC Chancay EPC USD 600m. Supports chec_chancay_port_epc_600m_2021.",
        "supports": ["chec_chancay_port_epc_600m_2021", "hunt_infra_engineering_epc"],
    },
)

# 9 energy/wind — EDF Diana Phase 1 142.5 MW (Jacobina) with Vale Base Metals PPA
A(
    {
        "id": "edf_diana_jacobina_142mw_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "allied",
        "counterpart": "EDF power solutions — Parque Eólico Diana Phase 1 (Jacobina, Bahia)",
        "country": "Brazil",
        "asset": "5 Aug 2026: EDF power solutions signs energy sales PPA for Diana Phase 1 — 142.5 MW / 23 turbines in Jacobina, northern Bahia; COD 2027. Offtakers Salobo Metais and Mineração Onça Puma (Vale Base Metals) under self-production model for nickel/copper decarbonization; surplus may go to market. Distinct from prior Vestas/Goldwind Casa dos Ventos rows.",
        "investment_type": "greenfield_generation",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-11.18",
        "lon": "-40.51",
        "geo_note": "Jacobina, Bahia (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "edf_diana_ppa_20260805",
        "note": "Actor: EDF power solutions (France) — allied. Company primary 5 Aug 2026. PPA/presence; CAPEX not disclosed in release.",
    },
    {
        "id": "edf_diana_jacobina_142mw_2026",
        "retrieved": "2026-10-01",
        "source_id": "edf_diana_ppa_20260805",
        "url": "https://brazil.edf-powersolutions.com/2026/08/05/edf-power-solutions-fecha-ppa-para-parque-eolico-na-bahia/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "A EDF power solutions estabeleceu um Contrato de Venda de Energia (PPA) referente à eletricidade produzida pela Fase 1 do Parque Eólico Diana. Localizado em Jacobina, no norte da Bahia, esta fase do parque tem capacidade instalada de 142,5 MW, é composto por 23 turbinas e iniciará suas operações comerciais em 2027.",
        "note": "Opened EDF power solutions Brasil Portuguese 5 Aug 2026.",
    },
    {
        "id": "edf_diana_ppa_20260805",
        "type": "company",
        "chicago": "EDF power solutions Brasil. “EDF power solutions fecha PPA para parque eólico na Bahia.” Press release, 5 August 2026.",
        "url": "https://brazil.edf-powersolutions.com/2026/08/05/edf-power-solutions-fecha-ppa-para-parque-eolico-na-bahia/",
        "annotation": "Company release on EDF Diana 142.5 MW PPA with Vale Base Metals. Supports edf_diana_jacobina_142mw_2026.",
        "supports": ["edf_diana_jacobina_142mw_2026", "hunt_energy_wind"],
    },
)

# 10–13 graphite, nickel, copper, niobium — miss

# 14 energy/other_renewables — Cubico–CFE Mexico ~USD 1bn renewables+BESS
A(
    {
        "id": "cubico_cfe_mexico_1bn_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "allied",
        "counterpart": "Cubico Sustainable Investments — CFE mixed scheme (5 projects + BESS)",
        "country": "Mexico",
        "asset": "22 Jul 2026: Cubico (UK) and CFE sign partnership for five mixed-scheme renewable projects totaling 578 MWac plus BESS 175.7 MW / 500 MWh (~3-hour); 25-year framework; joint investment near USD 1,000 million. First site Altamira Solar (Tamaulipas, 78 MW + BESS) construction targeted Dec 2026; other four from Q2 2027. Mix of PV and wind across Tamaulipas, Nuevo León, Campeche and Yucatán peninsula. Distinct from polaris_cfe_mexico_solar_217m_2026.",
        "investment_type": "ownership_equity",
        "value": "1000000000",
        "currency": "USD",
        "value_usd": "1000000000",
        "fx_usd": "1",
        "fx_date": "2026-07-22",
        "year": "2026",
        "status": "active",
        "lat": "22.4",
        "lon": "-97.9",
        "geo_note": "Pinned to Altamira Solar / Tamaulipas (first construction site cited; approximate).",
        "evidence": "proxy",
        "source_id": "pv_mag_cubico_cfe_20260722",
        "note": "Actor: Cubico Sustainable Investments (UK) — allied, with CFE ≥54% mixed-scheme stake. UNVERIFIED proxy: pv magazine México 22 Jul 2026 summarizing Cubico communication. Near-USD 1bn joint investment figure.",
    },
    {
        "id": "cubico_cfe_mexico_1bn_2026",
        "retrieved": "2026-10-01",
        "source_id": "pv_mag_cubico_cfe_20260722",
        "url": "https://www.pv-magazine-mexico.com/2026/07/22/cubico-y-cfe-acuerdan-desarrollar-578-mw-renovables-con-500-mwh-en-baterias/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Cubico Sustainable Investments y la Comisión Federal de Electricidad (CFE) han firmado un acuerdo de asociación para desarrollar cinco proyectos de energía renovable con una capacidad conjunta de 578 MWac y sistemas de almacenamiento en baterías de 175.7 MW/500 MWh. … contempla una inversión conjunta cercana a 1,000 millones de dólares",
        "note": "Opened pv magazine México Spanish 22 Jul 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "pv_mag_cubico_cfe_20260722",
        "type": "trade_press",
        "chicago": "Ini, Luis. “Cubico y CFE acuerdan desarrollar 578 MW renovables con 500 MWh en baterías.” pv magazine México, 22 July 2026.",
        "url": "https://www.pv-magazine-mexico.com/2026/07/22/cubico-y-cfe-acuerdan-desarrollar-578-mw-renovables-con-500-mwh-en-baterias/",
        "annotation": "Press on Cubico–CFE ~USD 1bn mixed renewables+BESS. Supports cubico_cfe_mexico_1bn_2026.",
        "supports": ["cubico_cfe_mexico_1bn_2026", "hunt_energy_other_renewables"],
    },
)

# 15–18 water, lithium, fission_smr, building_materials — miss


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
        "hunt_energy_solar": "Cycle 41: logged polaris_cfe_mexico_solar_217m_2026.",
        "hunt_infra_port_ownership": "Cycle 41: equal budget; Cosco Chancay / ICAVE already (miss).",
        "hunt_latam_rail_telecom": "Cycle 41: equal budget; ACA/Tren Macho/PowerChina already (miss).",
        "hunt_br_power_equip": "Cycle 41: equal budget; State Grid NE / Hitachi already (miss).",
        "hunt_infra_port_cranes": "Cycle 41: equal budget; ZPMC/Kalmar/Konecranes already (miss).",
        "hunt_infra_bridges_roads": "Cycle 41: equal budget; CAF/Mota-Engil already (miss).",
        "hunt_res_balsa": "Cycle 41: logged aima_siemens_energy_balsa_mou_2026.",
        "hunt_infra_engineering_epc": "Cycle 41: logged chec_chancay_port_epc_600m_2021.",
        "hunt_energy_wind": "Cycle 41: logged edf_diana_jacobina_142mw_2026.",
        "hunt_res_graphite": "Cycle 41: equal budget; Graphcoa Allied offtake already (miss).",
        "hunt_res_nickel": "Cycle 41: equal budget; PNP/MMG already (miss; Diana PPA logged under wind).",
        "hunt_res_copper": "Cycle 41: equal budget; El Abra/Las Bambas already (miss).",
        "hunt_fenb_araxa": "Cycle 41: equal budget; Codemig renewal already (miss).",
        "hunt_energy_other_renewables": "Cycle 41: logged cubico_cfe_mexico_1bn_2026.",
        "hunt_res_water": "Cycle 41: equal budget; Sacyr Antofagasta already (miss).",
        "hunt_res_lithium": "Cycle 41: equal budget; Posco/Zijin/Ganfeng already (miss).",
        "hunt_energy_fission_smr": "Cycle 41: equal budget; INB–Westinghouse already (miss).",
        "hunt_infra_building_materials": "Cycle 41: equal budget; Holcim/Votorantim already (miss).",
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
    print("Cycle 41 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 41 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
