#!/usr/bin/env python3
"""Cycle 30 hunt: shuffle_seed=20261030; equal budget across 18 subcategories."""
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


# seed 20261030 order:
# port_cranes, power_plants_grid, solar, bridges_roads, engineering_epc, rail,
# water, wind, building_materials, nickel, copper, balsa, port_ownership,
# niobium, fission_smr, graphite, lithium, other_renewables

# 1 infrastructure/port_cranes — miss (Sany Aracruz / Konecranes Manaus / ZPMC set already)
# 2 energy/power_plants_grid — miss (Hitachi Dosquebradas USD 80m tranche already)
# 3 energy/solar — miss (YPF Luz El Quemado logged C29)

# 4 infrastructure/bridges_roads — CRCC Ruta 5 Talca–Chillán
A(
    {
        "id": "crcc_talca_chillan_ruta5_2021",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "Consorcio CRCC — Segunda Concesión Ruta 5 Tramo Talca–Chillán",
        "country": "Chile",
        "asset": "MOP award (DS MOP Nº5 / Diario Oficial 13 Mar 2021) to Consorcio CRCC (CRCC International Investment Co. Ltd. + China Railway Construction Corporation (International) Limited) for Segunda Concesión Ruta 5 Talca–Chillán: ~195 km including Baipás Talca (~56 km), third lanes San Carlos–Chillán Viejo, 19 new bridges + structure upgrades; investment UF 19,180,000 (~USD 804 million); variable-term concession max 32 years (Sociedad Concesionaria Survías Maule-Ñuble S.A.); works start delayed into mid-2020s with ongoing MOP/CRCC disputes",
        "investment_type": "ppp_concession",
        "value": "804000000",
        "currency": "USD",
        "value_usd": "804000000",
        "fx_usd": "1",
        "fx_date": "2021-03-13",
        "year": "2021",
        "status": "active",
        "lat": "-35.7",
        "lon": "-71.5",
        "geo_note": "Ruta 5 Talca–Chillán corridor, Maule/Ñuble regions (MOP DGC award notice; approximate mid-corridor pin).",
        "evidence": "documented",
        "source_id": "mop_talca_chillan_award_2021",
        "note": "Actor: CRCC International Investment + CRCC (International) — prc. Official MOP Dirección General de Concesiones award page: UF 19.180.000 ≈ USD 804m. Distinct from CRCC Santiago–Batuco rail civil, CHEC Colombia/Jamaica highway, and OHLA Panamericana Este rows.",
    },
    {
        "id": "crcc_talca_chillan_ruta5_2021",
        "retrieved": "2026-10-01",
        "source_id": "mop_talca_chillan_award_2021",
        "url": "https://concesiones.mop.gob.cl/este-sabado-se-publico-en-el-diario-oficial-el-decreto-de-adjudicacion-de-la-segunda-concesion-ruta-5-tramo-talca-chillan/",
        "price_year": "2021",
        "evidence": "documented",
        "quote": "iniciativa que contempla una inversión de UF 19.180.000 (MM USD 804 aproximadamente) y que será desarrollada por el Consorcio CRCC, conformado por CRCC International Investment Co. Ltd. y China Railway Construction Corporation (International) Limited",
        "note": "Opened MOP DGC Spanish award notice. July 2026 executive informe corroborates CRCC ownership and UF budget.",
    },
    {
        "id": "mop_talca_chillan_award_2021",
        "type": "government",
        "chicago": "Dirección General de Concesiones, Ministerio de Obras Públicas (Chile). “Este sábado se publicó en el Diario Oficial el Decreto de Adjudicación de la Segunda Concesión Ruta 5 Tramo Talca-Chillán.” 13 March 2021.",
        "url": "https://concesiones.mop.gob.cl/este-sabado-se-publico-en-el-diario-oficial-el-decreto-de-adjudicacion-de-la-segunda-concesion-ruta-5-tramo-talca-chillan/",
        "annotation": "Official MOP award of Talca–Chillán Ruta 5 concession to CRCC at ~USD 804m. Supports crcc_talca_chillan_ruta5_2021.",
        "supports": ["crcc_talca_chillan_ruta5_2021", "hunt_infra_bridges_roads"],
    },
)

# 5 infrastructure/engineering_epc — miss (PowerChina UFN-III / Bechtel–EIMISA already)

# 6 infrastructure/rail — Siemens–Sonda México ETCS
A(
    {
        "id": "siemens_sonda_mexico_etcs_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "Siemens Mobility + SONDA — ETCS L1 signaling CDMX–Querétaro–Irapuato",
        "country": "Mexico",
        "asset": "ATTPI international public tender award (26 Mar 2026) to Siemens Mobility–SONDA México consortium for design/supply/install/commission of technological systems on México–Querétaro and Querétaro–Irapuato passenger corridors (>300 km, 11 stations): ETCS Level 1 wayside, OCC + backup, SCADA, first LatAm TPS.plan; SONDA telecom/CCTV/civil; Siemens first ETCS contract in Mexico. Consortium partner SONDA states contract value MXN 3,844 million (~USD 192 million stated); ~4-year execution",
        "investment_type": "equipment_supply",
        "value": "3844000000",
        "currency": "MXN",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "20.6",
        "lon": "-100.4",
        "geo_note": "CDMX–Querétaro–Irapuato passenger corridor (Siemens/SONDA releases; approximate Querétaro pin).",
        "evidence": "documented",
        "source_id": "siemens_mexico_etcs_20260326",
        "note": "Actors: Siemens Mobility (German) + SONDA México (Chilean tech) — allied. Siemens AG English press confirms award/scope; MXN 3,844m value from SONDA company Spanish release (approx USD 192m stated — FX not entered). Distinct from siemens_efe_etcs_chile_2025, alstom_mexico_dmu_2025, and crrc_mexico_pachuca_trains_2025.",
    },
    {
        "id": "siemens_sonda_mexico_etcs_2026",
        "retrieved": "2026-10-01",
        "source_id": "siemens_mexico_etcs_20260326",
        "url": "https://press.siemens.com/global/en/pressrelease/siemens-mobility-and-sonda-win-etcs-signaling-project-mexico",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Siemens Mobility, in consortium with Sonda México SA de CV, has been awarded a landmark contract to deliver … ETCS Level 1 for the Mexico City–Querétaro–Irapuato railway corridor.",
        "note": "Opened Siemens Mobility English press 26 Mar 2026. Value from paired SONDA company page.",
    },
    {
        "id": "siemens_mexico_etcs_20260326",
        "type": "company",
        "chicago": "Siemens Mobility. “Siemens Mobility and Sonda win ETCS signaling project in Mexico.” 26 March 2026.",
        "url": "https://press.siemens.com/global/en/pressrelease/siemens-mobility-and-sonda-win-etcs-signaling-project-mexico",
        "annotation": "Company primary on first Mexico ETCS L1 award for CDMX–Querétaro–Irapuato. Supports siemens_sonda_mexico_etcs_2026.",
        "supports": ["siemens_sonda_mexico_etcs_2026", "hunt_latam_rail_telecom"],
    },
)

# 7 resources/water — miss (Cox Rosarito / Sacyr Coquimbo already)
# 8 energy/wind — miss
# 9 infrastructure/building_materials — miss (Holcim Guayaquil / Pacasmayo / Cemex Colombia already)
# 10 resources/nickel — miss
# 11 resources/copper — miss
# 12 resources/balsa — miss
# 13 infrastructure/port_ownership — miss (Marcona / HGT Aracruz already)

# 14 resources/niobium — CBMM R$13bn 2026–2031 plan
A(
    {
        "id": "cbmm_araxa_13bn_plan_2026",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "CBMM — Araxá niobium complex 2026–2031 investment plan",
        "country": "Brazil",
        "asset": "Company note to Diário do Comércio (18 Sep 2026): planned investments ~R$ 13 billion between 2026 and 2031 for productive-capacity expansion, new materials/applications, and technology/innovation/infrastructure at Araxá complex; company states R$ 2 billion already invested in 2026 YTD on new lines/plants and equipment modernization; FeNb-eq capacity 150 ktpy; 2025 production >100 kt FeNb-eq",
        "investment_type": "capex_plan",
        "value": "13000000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "CBMM Industrial Complex, Araxá, Minas Gerais (Diário do Comércio citing CBMM).",
        "evidence": "proxy",
        "source_id": "diario_comercio_cbmm_13bn_20260918",
        "note": "Actor: CBMM (Brazilian Moreira Salles–controlled) — allied. UNVERIFIED proxy: Diário do Comércio 18 Sep 2026 citing CBMM note to the paper (R$13bn 2026–2031; R$2bn 2026 YTD). Distinct from cbmm_araxa_capex_plan_2025 (R$10bn five-year Folha/Reuters proxy) and XNO anode plant row. Value stored as BRL.",
    },
    {
        "id": "cbmm_araxa_13bn_plan_2026",
        "retrieved": "2026-10-01",
        "source_id": "diario_comercio_cbmm_13bn_20260918",
        "url": "https://diariodocomercio.com.br/economia/cbmm-niobio-investimentos/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "A Companhia Brasileira de Metalurgia e Mineração (CBMM) planeja investimentos da ordem de R$ 13 bilhões entre 2026 e 2031 … Somente neste ano, a companhia já investiu R$ 2 bilhões em seu complexo industrial localizado em Araxá",
        "note": "Opened Diário do Comércio Portuguese article citing CBMM note to the paper.",
    },
    {
        "id": "diario_comercio_cbmm_13bn_20260918",
        "type": "press",
        "chicago": "Diário do Comércio. “Mineira CBMM planeja investimentos de R$ 13 bilhões até 2031.” 18 September 2026.",
        "url": "https://diariodocomercio.com.br/economia/cbmm-niobio-investimentos/",
        "annotation": "UNVERIFIED press citing CBMM R$13bn 2026–2031 Araxá plan. Supports cbmm_araxa_13bn_plan_2026.",
        "supports": ["cbmm_araxa_13bn_plan_2026", "hunt_fenb_araxa"],
    },
)

# 15 energy/fission_smr — miss (Meitner / CAREM / Angra standstill already)
# 16 resources/graphite — miss

# 17 resources/lithium — Albemarle TED DLE EIA
A(
    {
        "id": "albemarle_ted_dle_atacama_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "us",
        "counterpart": "Albemarle — Transition to Direct Lithium Extraction (TED) EIA at Salar de Atacama",
        "country": "Chile",
        "asset": "25 Mar 2026: Albemarle submits Environmental Impact Assessment for TED Project using DLE in Salar de Atacama (San Pedro de Atacama / ~31 km from Peine); modular plant up to six production lines (~50 l/s brine each); designed to roughly double lithium recovery while reducing net brine pumping vs evaporation; +~29 km 220 kV renewable transmission line parallel to Route B-39; FID pending permitting; pilot at La Negra >1 year with >94% Li recovery stated; CAPEX USD not disclosed",
        "investment_type": "permitting",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-23.45",
        "lon": "-68.25",
        "geo_note": "Eastern Salar de Atacama core / San Pedro de Atacama municipality (Albemarle Chile release).",
        "evidence": "documented",
        "source_id": "albemarle_ted_dle_20260325",
        "note": "Actor: Albemarle Corporation (U.S.) — us. Company Chile English release 25 Mar 2026. Pre-FID EIA milestone — no CAPEX USD on page. Distinct from Codelco–SQM NovaAndino / Rio Tinto Rincón / Ganfeng / Zijin lithium rows.",
    },
    {
        "id": "albemarle_ted_dle_atacama_2026",
        "retrieved": "2026-10-01",
        "source_id": "albemarle_ted_dle_20260325",
        "url": "https://www.albemarle.com/cl/en/news/albemarle-initiates-environmental-review-chiles-first-direct-lithium-extraction-project-salar",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Albemarle Corporation … today announced it has submitted the Environmental Impact Assessment (EIA) for the Transition to Direct Lithium Extraction (TED) Project … in the Salar de Atacama in Chile.",
        "note": "Opened Albemarle Chile English company release 25 Mar 2026.",
    },
    {
        "id": "albemarle_ted_dle_20260325",
        "type": "company",
        "chicago": "Albemarle Corporation. “Albemarle Initiates Environmental Review for Chile’s First Direct Lithium Extraction Project in Salar de Atacama.” 25 March 2026.",
        "url": "https://www.albemarle.com/cl/en/news/albemarle-initiates-environmental-review-chiles-first-direct-lithium-extraction-project-salar",
        "annotation": "Company primary on TED/DLE EIA submission at Salar de Atacama. Supports albemarle_ted_dle_atacama_2026.",
        "supports": ["albemarle_ted_dle_atacama_2026", "hunt_res_lithium"],
    },
)

# 18 energy/other_renewables — miss (Ormat Dominica COD logged C29)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {b["id"]: i for i, b in enumerate(bib) if isinstance(b, dict) and "id" in b}

    added = []
    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        if rid in by_id:
            rows[by_id[rid]].update({k: v for k, v in row.items() if v != ""})
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

    # SONDA corroboration bib for MXN value
    sonda_bib = {
        "id": "sonda_mexico_etcs_20260326",
        "type": "company",
        "chicago": "SONDA. “SONDA y Siemens Mobility ganan el proyecto de señalización ETCS en México.” 26 March 2026.",
        "url": "https://www.sonda.com/detalle-noticia/2026/03/26/sonda-impulsa-la-transformacion-ferroviaria-en-mexico-con-tecnologia-para-el-corredor-mexico-queretaro-irapuato",
        "annotation": "Consortium partner primary stating MXN 3,844m contract value for CDMX–Querétaro–Irapuato ETCS package. Supports siemens_sonda_mexico_etcs_2026.",
        "supports": ["siemens_sonda_mexico_etcs_2026", "hunt_latam_rail_telecom"],
    }
    if sonda_bib["id"] not in bib_by:
        bib.append(sonda_bib)

    hunt_updates = {
        "hunt_infra_port_cranes": "Cycle 30: equal budget; Sany Aracruz / Konecranes Manaus / ZPMC set already logged (miss).",
        "hunt_br_power_equip": "Cycle 30: equal budget; Hitachi Dosquebradas tranche already logged (miss).",
        "hunt_energy_solar": "Cycle 30: equal budget; YPF Luz El Quemado logged C29 (miss).",
        "hunt_infra_bridges_roads": "Cycle 30: logged crcc_talca_chillan_ruta5_2021.",
        "hunt_infra_engineering_epc": "Cycle 30: equal budget; PowerChina UFN-III / Bechtel–EIMISA already logged (miss).",
        "hunt_latam_rail_telecom": "Cycle 30: logged siemens_sonda_mexico_etcs_2026.",
        "hunt_res_water": "Cycle 30: equal budget; Cox Rosarito / Sacyr Coquimbo already logged (miss).",
        "hunt_energy_wind": "Cycle 30: equal budget; Goldwind / Envision / Vestas set already logged (miss).",
        "hunt_infra_building_materials": "Cycle 30: equal budget; Holcim Guayaquil / Pacasmayo / Cemex Colombia already (miss).",
        "hunt_res_nickel": "Cycle 30: equal budget; Glencore Jaguar / MMG / Atlantic already logged (miss).",
        "hunt_res_copper": "Cycle 30: equal budget; Cerro Verde / Toromocho already logged (miss).",
        "hunt_res_balsa": "Cycle 30: equal budget; AIMA 2025 manufactures pair logged C28 (miss).",
        "hunt_infra_port_ownership": "Cycle 30: equal budget; Marcona Jinzhao / HGT Aracruz already logged (miss).",
        "hunt_fenb_araxa": "Cycle 30: logged cbmm_araxa_13bn_plan_2026 (UNVERIFIED proxy).",
        "hunt_energy_fission_smr": "Cycle 30: equal budget; Meitner / CAREM / Angra standstill already (miss).",
        "hunt_res_graphite": "Cycle 30: equal budget; Graphcoa / South Star / Graph+ already logged (miss).",
        "hunt_res_lithium": "Cycle 30: logged albemarle_ted_dle_atacama_2026.",
        "hunt_energy_other_renewables": "Cycle 30: equal budget; Ormat Dominica COD logged C29 (miss).",
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
    print("Cycle 30 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
