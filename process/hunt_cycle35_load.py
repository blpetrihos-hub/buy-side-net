#!/usr/bin/env python3
"""Cycle 35 hunt: shuffle_seed=20261035; equal budget across 18 subcategories."""
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


# seed 20261035 order:
# building_materials, port_cranes, graphite, power_plants_grid, copper, wind,
# engineering_epc, bridges_roads, solar, rail, lithium, other_renewables,
# fission_smr, nickel, water, port_ownership, niobium, balsa

# 1 infrastructure/building_materials — CBB Mejillones + Cruz Azul Hidalgo
A(
    {
        "id": "cbb_mejillones_grind_42m_2026",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "allied",
        "counterpart": "Cementos Bío Bío (Carmeuse Belgium) — Mejillones grind + batch plant",
        "country": "Chile",
        "asset": "Jul 2026: CBB (Carmeuse-controlled since Sep 2025) activates USD 42 million investment for modular cement grinding plant + ready-mix batch plant inside Puerto Abierto / PASA complex, Mejillones (Antofagasta); up to 350,000 tpy cement and 20,000 m³/y concrete; clinker via ~590 m enclosed belt from existing PASA; SEA pertinencia consulta filed (new works not yet started)",
        "investment_type": "greenfield_plant",
        "value": "42000000",
        "currency": "USD",
        "value_usd": "42000000",
        "fx_usd": "1",
        "fx_date": "2026-07-14",
        "year": "2026",
        "status": "active",
        "lat": "-23.1",
        "lon": "-70.45",
        "geo_note": "Puerto Abierto / Mejillones, Antofagasta Region (SEA pertinencia geography via press).",
        "evidence": "proxy",
        "source_id": "roadshow_cbb_mejillones_20260714",
        "note": "Actor: Carmeuse (Belgian) via CBB — allied. UNVERIFIED proxy: RoadShow 14 Jul 2026 summarizing company SEA pertinencia and USD 42m. Distinct from carmeuse_bio_bio_chile_2025 (ownership acquisition).",
    },
    {
        "id": "cbb_mejillones_grind_42m_2026",
        "retrieved": "2026-10-01",
        "source_id": "roadshow_cbb_mejillones_20260714",
        "url": "https://roadshow.cl/cementos-biobio-planta-mejillones-us-42-millones/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Cementos Bío Bío (CBB) activó en Mejillones, Región de Antofagasta, una inversión de US$42 millones para construir una planta de molienda de cemento y una instalación dosificadora de hormigón",
        "note": "Opened RoadShow Spanish 14 Jul 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "roadshow_cbb_mejillones_20260714",
        "type": "trade_press",
        "chicago": "RoadShow. “Belga Carmeuse activa su primera inversión en Cementos Bío Bío: US$42 millones en Mejillones.” 14 July 2026.",
        "url": "https://roadshow.cl/cementos-biobio-planta-mejillones-us-42-millones/",
        "annotation": "Trade press on CBB/Carmeuse Mejillones grind plant USD 42m. Supports cbb_mejillones_grind_42m_2026.",
        "supports": ["cbb_mejillones_grind_42m_2026", "hunt_infra_building_materials"],
    },
)

A(
    {
        "id": "cruz_azul_hidalgo_383m_2026",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "other",
        "counterpart": "Cooperativa La Cruz Azul — Hidalgo cement plant reactivation",
        "country": "Mexico",
        "asset": "19 Aug 2026 presidential press conference: La Cruz Azul announces USD 383 million to reactivate Hidalgo cement plant toward ~3 Mtpy capacity; includes USD 106 million renovation/reconditioning underway and USD 217 million new production line (~85% complete per board chair Víctor Manuel Velázquez). Remainder of package not itemized on opened page",
        "investment_type": "brownfield_expansion",
        "value": "383000000",
        "currency": "USD",
        "value_usd": "383000000",
        "fx_usd": "1",
        "fx_date": "2026-08-19",
        "year": "2026",
        "status": "active",
        "lat": "19.93",
        "lon": "-99.23",
        "geo_note": "Cruz Azul plant, Hidalgo (company geography; approximate pin).",
        "evidence": "proxy",
        "source_id": "globalcement_cruz_azul_20260820",
        "note": "Actor: Cooperativa La Cruz Azul (Mexican cooperative) — other. UNVERIFIED proxy: Global Cement 20 Aug 2026 summarizing Sheinbaum press conference. Distinct from cemex_dr_divest / holcim Colombia.",
    },
    {
        "id": "cruz_azul_hidalgo_383m_2026",
        "retrieved": "2026-10-01",
        "source_id": "globalcement_cruz_azul_20260820",
        "url": "https://www.globalcement.com/news/21145-cooperativa-la-cruz-azul-invests-us-383m-in-hidalgo-plant",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "La Cruz Azul announced an investment of US$383m to ‘reactivate’ its cement plant in Hildalgo. The project is expected to restore production capacity to 3Mt/yr.",
        "note": "Opened Global Cement 20 Aug 2026. Mark UNVERIFIED proxy.",
    },
    {
        "id": "globalcement_cruz_azul_20260820",
        "type": "trade_press",
        "chicago": "Global Cement. “Cooperativa La Cruz Azul invests US$383m in Hidalgo plant.” 20 August 2026.",
        "url": "https://www.globalcement.com/news/21145-cooperativa-la-cruz-azul-invests-us-383m-in-hidalgo-plant",
        "annotation": "Trade press on Cruz Azul Hidalgo reactivation USD 383m. Supports cruz_azul_hidalgo_383m_2026.",
        "supports": ["cruz_azul_hidalgo_383m_2026", "hunt_infra_building_materials"],
    },
)

# 2 infrastructure/port_cranes — miss (SSA Guaymas / Suape Sany / MultiRio / Aracruz already)

# 3 resources/graphite — upgrade Graphcoa Jordânia to EIA-cited R$621.76m / USD 120m
A(
    {
        "id": "graphcoa_jordania_dfs_capex_2026",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "allied",
        "counterpart": "Graphcoa / Appian Capital Brazil — Projeto Grafite Jordânia",
        "country": "Brazil",
        "asset": "Cycle 35 refreshes CAPEX from prior ~R$700m interview proxy to BNamericas 24 Jun 2026 citing company EIA-Rima: planned investment R$ 621.76 million (US$120 million) for Jordânia (MG) graphite concentrate project; works Jun 2027–Jun 2029; commissioning Mar–Jun 2029; ops from Jul 2029; ramp-up through Dec 2030; ~53 ktpy high-purity concentrate (≥14-year life)",
        "investment_type": "greenfield_mine",
        "value": "621760000",
        "currency": "BRL",
        "value_usd": "120000000",
        "fx_usd": "",
        "fx_date": "2026-06-24",
        "year": "2026",
        "status": "active",
        "lat": "-15.9",
        "lon": "-40.2",
        "geo_note": "Jordânia, Vale do Jequitinhonha, Minas Gerais (EIA geography via press).",
        "evidence": "proxy",
        "source_id": "bnamericas_graphcoa_jordania_20260624",
        "note": "Actor: Graphcoa / Appian — allied. Cycle 35 value refresh to EIA-cited R$621.76m / USD 120m (still UNVERIFIED press summarizing EIA). Distinct from graphcoa_boa_sorte / graphcoa_jordania_mg presence.",
    },
    {
        "id": "graphcoa_jordania_dfs_capex_2026",
        "retrieved": "2026-10-01",
        "source_id": "bnamericas_graphcoa_jordania_20260624",
        "url": "https://www.bnamericas.com/en/news/appian-unit-in-brazil-will-invest-us120-million-in-graphite-project",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Graphcoa … plans to invest 621.76 million (mn) reais (US$120mn) in a project in the Brazilian state of Minas Gerais. … production capacity of 53 thousand tons per year",
        "note": "Opened BNamericas 24 Jun 2026 citing EIA-Rima. Mark UNVERIFIED proxy.",
    },
    {
        "id": "bnamericas_graphcoa_jordania_20260624",
        "type": "trade_press",
        "chicago": "BNamericas. “Appian unit in Brazil will invest US$120 million in graphite project.” 24 June 2026.",
        "url": "https://www.bnamericas.com/en/news/appian-unit-in-brazil-will-invest-us120-million-in-graphite-project",
        "annotation": "Trade press citing Graphcoa EIA investment R$621.76m / USD 120m. Supports graphcoa_jordania_dfs_capex_2026.",
        "supports": ["graphcoa_jordania_dfs_capex_2026", "hunt_res_graphite"],
    },
)

# 4 energy/power_plants_grid — Hitachi Brazil additional USD 70m
A(
    {
        "id": "hitachi_brazil_addl_70m_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "allied",
        "counterpart": "Hitachi Energy — additional Brazil transformer manufacturing Capex",
        "country": "Brazil",
        "asset": "9 Mar 2026 Hitachi Energy announcement: additional USD 70 million through 2027 for Pindamonhangaba new factory and Guarulhos expansion (São Paulo), on top of previously announced USD 200 million; +50% production capacity; ~48,300 m² built area; serves Brazil plus exports to North America/Europe/Middle East. (Same package also restates Colombia Dosquebradas USD 80m already logged separately)",
        "investment_type": "manufacturing_capex",
        "value": "70000000",
        "currency": "USD",
        "value_usd": "70000000",
        "fx_usd": "1",
        "fx_date": "2026-03-09",
        "year": "2026",
        "status": "active",
        "lat": "-22.92",
        "lon": "-45.46",
        "geo_note": "Pindamonhangaba / Guarulhos, São Paulo State (company announcement).",
        "evidence": "documented",
        "source_id": "hitachi_latam_addl_20260309",
        "note": "Actor: Hitachi Energy (Japanese/Swiss allied OEM) — allied. Company primary. Distinct from hitachi_brazil_transformer_capex_2024 (USD 200m) and hitachi_dosquebradas_colombia_2026 (USD 80m).",
    },
    {
        "id": "hitachi_brazil_addl_70m_2026",
        "retrieved": "2026-10-01",
        "source_id": "hitachi_latam_addl_20260309",
        "url": "https://www.hitachienergy.com/ch/it/news-and-events/features/2026/03/hitachi-energy-reaffirms-commitment-to-latin-america-through-an-additional-150-million-usd-investment-to-expand-power-transformer-manufacturing-capacity",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "In Brazil, Hitachi Energy will invest an additional $70 million USD through 2027, adding to the previously announced $200 million investment for the construction of a new factory in Pindamonhangaba and the expansion of the Guarulhos factory",
        "note": "Opened Hitachi Energy company feature 9 Mar 2026.",
    },
    {
        "id": "hitachi_latam_addl_20260309",
        "type": "company",
        "chicago": "Hitachi Energy. “Hitachi Energy reaffirms commitment to Latin America through an additional $150 million USD investment to expand power transformer manufacturing capacity.” 9 March 2026.",
        "url": "https://www.hitachienergy.com/ch/it/news-and-events/features/2026/03/hitachi-energy-reaffirms-commitment-to-latin-america-through-an-additional-150-million-usd-investment-to-expand-power-transformer-manufacturing-capacity",
        "annotation": "Company announcement of additional LatAm transformer Capex incl. Brazil USD 70m. Supports hitachi_brazil_addl_70m_2026.",
        "supports": ["hitachi_brazil_addl_70m_2026", "hunt_br_power_equip"],
    },
)

# 5 resources/copper — miss (Las Bambas / Centinela / El Abra already)
# 6 energy/wind — Goldwind 470 MW FINAME
A(
    {
        "id": "goldwind_470mw_finame_br_2026",
        "layer": "energy",
        "subcategory": "wind",
        "side": "prc",
        "counterpart": "Goldwind — first FINAME-qualified Brazil turbine order (~470 MW)",
        "country": "Brazil",
        "asset": "2 Jan 2026: Goldwind finalises first Brazil FINAME-framework order for >470 MW onshore wind; 76 × GWH182-6.2 MW turbines manufactured at Bahia local plant; 30-year full-service O&M; BNDES/Northeast Bank financing eligibility via local content. Customer/project name not disclosed on opened page — Capex USD blank",
        "investment_type": "equipment_procurement",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-12.7",
        "lon": "-38.3",
        "geo_note": "Goldwind Bahia manufacturing / NE Brazil offtake (company geography; approximate Camaçari pin).",
        "evidence": "documented",
        "source_id": "windtech_goldwind_470_20260102",
        "note": "Actor: Goldwind (PRC) — prc. Windtech International 2 Jan 2026 summarizing company FINAME first order. Distinct from goldwind_sento_se_872mw_2026 / goldwind_spic_touros_br_2025.",
    },
    {
        "id": "goldwind_470mw_finame_br_2026",
        "retrieved": "2026-10-01",
        "source_id": "windtech_goldwind_470_20260102",
        "url": "https://www.windtech-international.com/projects-and-contracts/goldwind-secures-470mw-wind-turbine-order-in-brazil",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Goldwind has finalised its first order in Brazil under the FINAME financing framework, covering more than 470 MW of installed onshore wind capacity. … supply of 76 GWH182-6.2 MW wind turbine generators, which will be manufactured at Goldwind’s local production facility in Bahia.",
        "note": "Opened Windtech International 2 Jan 2026.",
    },
    {
        "id": "windtech_goldwind_470_20260102",
        "type": "trade_press",
        "chicago": "Windtech International. “Goldwind secures 470MW wind turbine order in Brazil.” 2 January 2026.",
        "url": "https://www.windtech-international.com/projects-and-contracts/goldwind-secures-470mw-wind-turbine-order-in-brazil",
        "annotation": "Trade notice of Goldwind first FINAME Brazil order >470 MW. Supports goldwind_470mw_finame_br_2026.",
        "supports": ["goldwind_470mw_finame_br_2026", "hunt_energy_wind"],
    },
)

# 7–16 misses recorded in hunt_updates
# 17 resources/niobium — CBMM 2026 spend R$2bn
A(
    {
        "id": "cbmm_araxa_2026_spend_2bn",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "CBMM — Araxá 2026 industrial Capex already executed",
        "country": "Brazil",
        "asset": "Diário do Comércio 18 Sep 2026 citing CBMM note: company already invested R$ 2 billion in 2026 at Araxá industrial complex (new lines/plants; equipment acquisition/modernization), within broader R$13 billion 2026–2031 plan already logged separately; includes niobium-oxide lines for batteries/electronics/data-center applications",
        "investment_type": "brownfield_expansion",
        "value": "2000000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2026-09-18",
        "year": "2026",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "CBMM Araxá complex, Minas Gerais.",
        "evidence": "proxy",
        "source_id": "diario_comercio_cbmm_13bn_20260918",
        "note": "Actor: CBMM — allied. UNVERIFIED proxy: same Diário do Comércio CBMM note used for cbmm_araxa_13bn_plan_2026; this row isolates disclosed 2026 executed spend R$2bn (not the multi-year envelope). Distinct from cbmm_araxa_13bn_plan_2026.",
    },
    {
        "id": "cbmm_araxa_2026_spend_2bn",
        "retrieved": "2026-10-01",
        "source_id": "diario_comercio_cbmm_13bn_20260918",
        "url": "https://diariodocomercio.com.br/economia/cbmm-niobio-investimentos/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Somente neste ano, a companhia já investiu R$ 2 bilhões em seu complexo industrial localizado em Araxá, no Alto Paranaíba, incluindo novas linhas e plantas, além da aquisição e modernização de equipamentos.",
        "note": "Opened Diário do Comércio 18 Sep 2026 citing CBMM note. Mark UNVERIFIED proxy.",
    },
    {
        "id": "diario_comercio_cbmm_13bn_20260918",
        "type": "trade_press",
        "chicago": "Diário do Comércio. “Nióbio: CBMM planeja investimentos de R$ 13 bilhões até 2031.” 18 September 2026.",
        "url": "https://diariodocomercio.com.br/economia/cbmm-niobio-investimentos/",
        "annotation": "Press citing CBMM note on R$13bn plan and R$2bn 2026 spend. Supports cbmm_araxa_13bn_plan_2026 and cbmm_araxa_2026_spend_2bn.",
        "supports": [
            "cbmm_araxa_13bn_plan_2026",
            "cbmm_araxa_2026_spend_2bn",
            "hunt_fenb_araxa",
        ],
    },
)

# 12 energy/other_renewables — Jinko BESS Amanecer
A(
    {
        "id": "jinko_bess_amanecer_500m_2025",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "prc",
        "counterpart": "Jinko Power — BESS Amanecer (Diego de Almagro, Atacama)",
        "country": "Chile",
        "asset": "Dec 2025 SEIA DIA filing: Sistema de Almacenamiento de Energía BESS Amanecer — estimated investment USD 500 million; 400 MW / 2,734.2 MWh (~6-hour discharge); 611 battery containers; Diego de Almagro, Atacama; construction targeted Sep 2029 (~13 months). UNVERIFIED press summarizing DIA",
        "investment_type": "greenfield_generation",
        "value": "500000000",
        "currency": "USD",
        "value_usd": "500000000",
        "fx_usd": "1",
        "fx_date": "2025-12-22",
        "year": "2025",
        "status": "active",
        "lat": "-26.39",
        "lon": "-70.05",
        "geo_note": "Diego de Almagro, Atacama Region (DIA geography via press).",
        "evidence": "proxy",
        "source_id": "redimin_jinko_amanecer_20251222",
        "note": "Actor: Jinko Power (PRC) — prc. UNVERIFIED proxy: REDIMIN 22 Dec 2025 summarizing SEIA DIA. Distinct from jinko_casa_ventos_413mwp_2026 (solar modules) and trina BESS rows.",
    },
    {
        "id": "jinko_bess_amanecer_500m_2025",
        "retrieved": "2026-10-01",
        "source_id": "redimin_jinko_amanecer_20251222",
        "url": "https://www.redimin.cl/jinko-power-impulsa-el-almacenamiento-energetico-en-chile-con-nuevo-megaproyecto-en-atacama-por-us500-millones",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "el proyecto “Sistema de Almacenamiento de Energía Bess Amanecer”, iniciativa que contempla una inversión estimada de US$500 millones … potencia instalada de 400 MW y una capacidad de almacenamiento de 2.734,2 MWh",
        "note": "Opened REDIMIN Spanish 22 Dec 2025. Mark UNVERIFIED proxy.",
    },
    {
        "id": "redimin_jinko_amanecer_20251222",
        "type": "trade_press",
        "chicago": "REDIMIN. “Jinko Power impulsa el almacenamiento energético en Chile con nuevo megaproyecto en Atacama por US$500 millones.” 22 December 2025.",
        "url": "https://www.redimin.cl/jinko-power-impulsa-el-almacenamiento-energetico-en-chile-con-nuevo-megaproyecto-en-atacama-por-us500-millones",
        "annotation": "Trade press on Jinko BESS Amanecer SEIA filing USD 500m. Supports jinko_bess_amanecer_500m_2025.",
        "supports": ["jinko_bess_amanecer_500m_2025", "hunt_energy_other_renewables"],
    },
)


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
        "hunt_infra_building_materials": "Cycle 35: logged cbb_mejillones_grind_42m_2026 + cruz_azul_hidalgo_383m_2026.",
        "hunt_infra_port_cranes": "Cycle 35: equal budget; Guaymas/Suape/MultiRio/Aracruz already (miss).",
        "hunt_res_graphite": "Cycle 35: refreshed graphcoa_jordania_dfs_capex_2026 to EIA-cited R$621.76m / USD 120m.",
        "hunt_br_power_equip": "Cycle 35: logged hitachi_brazil_addl_70m_2026.",
        "hunt_res_copper": "Cycle 35: equal budget; Las Bambas 2026 capex logged C34 (miss).",
        "hunt_energy_wind": "Cycle 35: logged goldwind_470mw_finame_br_2026.",
        "hunt_infra_engineering_epc": "Cycle 35: equal budget; Worley Diablillos / Sedgman already (miss).",
        "hunt_infra_bridges_roads": "Cycle 35: equal budget; Sierra T4 / ERG Popayán already (miss).",
        "hunt_energy_solar": "Cycle 35: equal budget; Trina Sidón/Pillancó already (miss).",
        "hunt_latam_rail_telecom": "Cycle 35: equal budget; CRCC Batuco / OHLA L9 already (miss).",
        "hunt_res_lithium": "Cycle 35: equal budget; Galan HMW logged C34 (miss).",
        "hunt_energy_other_renewables": "Cycle 35: logged jinko_bess_amanecer_500m_2025.",
        "hunt_energy_fission_smr": "Cycle 35: equal budget; Meitner/Brazil microreactor already (miss).",
        "hunt_res_nickel": "Cycle 35: equal budget; BNDES Piauí / Jaguar already (miss).",
        "hunt_res_water": "Cycle 35: equal budget; Cox Rosarito / Sacyr Coquimbo already (miss).",
        "hunt_infra_port_ownership": "Cycle 35: equal budget; Tecon 10 / DP World Callao still pre-award (miss).",
        "hunt_fenb_araxa": "Cycle 35: logged cbmm_araxa_2026_spend_2bn (R$2bn 2026 spend).",
        "hunt_res_balsa": "Cycle 35: equal budget; WITS/AIMA already (miss).",
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
    print("Cycle 35 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 35 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
