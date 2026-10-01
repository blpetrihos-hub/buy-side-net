#!/usr/bin/env python3
"""Cycle 53 hunt: shuffle_seed=20261053; equal budget; U.S. side ≥1/3; thin_topup after.

Order: rail, power_plants_grid, bridges_roads, other_renewables, lithium, port_cranes,
copper, building_materials, wind, niobium, engineering_epc, graphite, nickel, fission_smr,
balsa, port_ownership, water, solar.
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
# 1 infrastructure/rail — USTDA / CONFI / ShorelineHudson Honduras corridor (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ustda_honduras_confi_shoreline_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "us",
        "counterpart": "USTDA / CONFI — ShorelineHudson interoceanic corridor feasibility",
        "country": "Honduras",
        "asset": "5 Mar 2026: USTDA hosts Honduran President Nasry Asfura for signing of agreement funding a feasibility study on an overland transportation corridor linking the Caribbean and Pacific; CONFI (National Commission for the Construction of the Interoceanic Railway) selected New Jersey–based Hudson-Arvon, LLC d/b/a ShorelineHudson to assess Port of San Lorenzo capacity upgrades, an inland intermodal rail terminal to relieve Port of Cortés congestion, future rail standards, and a financing/implementation plan identifying U.S. exporters (locomotives, railcars, container-handling equipment, TOS, security). Grant amount not disclosed on opened page — catalytic U.S. TA only.",
        "investment_type": "feasibility_ta",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2026-03-05",
        "year": "2026",
        "status": "active",
        "lat": "15.84",
        "lon": "-87.94",
        "geo_note": "Puerto Cortés (Caribbean terminus / inland intermodal relief target; San Lorenzo Pacific upgrades also in scope).",
        "evidence": "documented",
        "source_id": "ustda_honduras_corridor_20260305",
        "note": "Actor: USTDA (U.S.) + U.S. contractor ShorelineHudson (NJ) — us. Agency primary 5 Mar 2026; rail corridor + port bottlenecks; CAPEX USD blank (feasibility only). Distinct from ICTSI OPC Cortés ownership row.",
    },
    {
        "id": "ustda_honduras_confi_shoreline_2026",
        "retrieved": "2026-10-01",
        "source_id": "ustda_honduras_corridor_20260305",
        "url": "https://ustda.gov/ustda-hosts-honduran-president-signs-agreement-to-diversify-u-s-supply-chain-routes-in-the-western-hemisphere/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "USTDA’s funding will support Honduras’ National Commission for the Construction of the Interoceanic Railway (CONFI) to mitigate these risks, strengthening regional supply chains in the short term and paving the way for a coast-to-coast rail corridor. CONFI selected New Jersey-based Hudson-Arvon, LLC d/b/a ShorelineHudson to carry out the study. The firm will assess infrastructure upgrades at existing port bottlenecks, including enhancements to improve capacity at the Port of San Lorenzo and an inland intermodal rail terminal to relieve congestion and increase cargo throughput capacity at the Port of Cortés.",
        "note": "Opened USTDA Honduras interoceanic corridor feasibility release.",
    },
    {
        "id": "ustda_honduras_corridor_20260305",
        "type": "agency",
        "chicago": "U.S. Trade and Development Agency. “USTDA Hosts Honduran President, Signs Agreement to Diversify U.S. Supply Chain Routes in the Western Hemisphere.” 5 March 2026.",
        "url": "https://ustda.gov/ustda-hosts-honduran-president-signs-agreement-to-diversify-u-s-supply-chain-routes-in-the-western-hemisphere/",
        "annotation": "USTDA primary on CONFI/ShorelineHudson Honduras interoceanic rail–port corridor feasibility. Supports ustda_honduras_confi_shoreline_2026.",
        "supports": ["ustda_honduras_confi_shoreline_2026", "hunt_latam_rail_telecom"],
    },
)

# ---------------------------------------------------------------------------
# 3 infrastructure/bridges_roads — CHEC Jamaica North-South Highway MoU (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "chec_jamaica_north_south_mou_2025",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "China Harbour Engineering (CHEC) — Jamaica North-South Highway Extension MoU",
        "country": "Jamaica",
        "asset": "4 Aug 2025: CHEC Americas signs MoU with Jamaica’s Ministry of Economic Growth and Job Creation to conduct the feasibility study for the North-South Highway Extension (~40 km) aimed at easing congestion along the A1 coastal road and improving island-wide connectivity; ceremony witnessed by Prime Minister Andrew Holness and Chinese Embassy representatives. CAPEX USD not disclosed — feasibility MoU only. Distinct from CHEC SPARK / SCHIP / Montego Bay perimeter rows.",
        "investment_type": "mou_feasibility",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2025-08-04",
        "year": "2025",
        "status": "active",
        "lat": "18.15",
        "lon": "-77.30",
        "geo_note": "Jamaica North-South Highway corridor (island mid-corridor approximate; MoU is national highway extension).",
        "evidence": "documented",
        "source_id": "chec_jamaica_ns_mou_20250804",
        "note": "Actor: CHEC / CCCC (PRC) — prc. Company English release; feasibility MoU — no construction CAPEX.",
    },
    {
        "id": "chec_jamaica_north_south_mou_2025",
        "retrieved": "2026-10-01",
        "source_id": "chec_jamaica_ns_mou_20250804",
        "url": "https://www.checamerica.com/blog/2025/08/04/jamaican-prime-minister-witnesses-mou-signing-for-highway-extension/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "On August 4, our company signed a Memorandum of Understanding with Jamaica’s Ministry of Economic Growth and Job Creation to carry out the feasibility study for the North-South Highway Extension project. The ceremony was witnessed by Prime Minister Andrew Holness, representatives of the Chinese Embassy, government officials, and local media. The project aims to extend the highway by 40 km to ease congestion along the A1 coastal road, improve transport efficiency, and enhance connectivity across the island.",
        "note": "Opened CHEC Americas Jamaica North-South Highway Extension MoU release.",
    },
    {
        "id": "chec_jamaica_ns_mou_20250804",
        "type": "company",
        "chicago": "CHEC Americas. “Jamaican Prime Minister Witnesses MOU Signing for Highway Extension.” 4 August 2025.",
        "url": "https://www.checamerica.com/blog/2025/08/04/jamaican-prime-minister-witnesses-mou-signing-for-highway-extension/",
        "annotation": "CHEC primary on Jamaica North-South Highway Extension feasibility MoU. Supports chec_jamaica_north_south_mou_2025.",
        "supports": ["chec_jamaica_north_south_mou_2025", "hunt_infra_bridges_roads"],
    },
)

# ---------------------------------------------------------------------------
# 4 energy/other_renewables — CIP La Esperanza Solar+BESS Mexico FC (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cip_la_esperanza_mexico_fc_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "allied",
        "counterpart": "Copenhagen Infrastructure Partners (GMF II) — La Esperanza Solar + BESS (Campeche)",
        "country": "Mexico",
        "asset": "6–7 Aug 2026: CIP Growth Markets Fund II reaches FID/financial close and starts construction on La Esperanza Solar in Campeche (Yucatán Peninsula) — 420 MWdc PV + 150 MW / 5-hour (750 MWh) BESS; ~USD 510 million project debt from BNP Paribas, JPMorgan Chase, Natixis CIB, Santander and Scotiabank; equity GMF II with expected Profuturo co-investment; long-term PPA with CFE Calificados; SENER strategic designation; COD targeted 2028. Coded other_renewables for hybrid solar-plus-storage (same pattern as AES Andes Pampas/Cristales). Distinct from CATL–CIP La Alegría BESS supply row.",
        "investment_type": "project_finance",
        "value": "510000000",
        "currency": "USD",
        "value_usd": "510000000",
        "fx_usd": "1",
        "fx_date": "2026-08-06",
        "year": "2026",
        "status": "active",
        "lat": "19.83",
        "lon": "-90.53",
        "geo_note": "Campeche state / Yucatán Peninsula (CIP/Natixis geography; approximate state pin).",
        "evidence": "documented",
        "source_id": "natixis_cip_esperanza_20260807",
        "note": "Actor: CIP (Danish) GMF II — allied. Value = stated ~USD 510m debt package (not full project equity+debt). Natixis PR Newswire 7 Aug 2026.",
    },
    {
        "id": "cip_la_esperanza_mexico_fc_2026",
        "retrieved": "2026-10-01",
        "source_id": "natixis_cip_esperanza_20260807",
        "url": "https://www.prnewswire.com/news-releases/natixis-corporate--investment-banking-supports-cip-in-510-million-project-financing-in-mexico-302846231.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Natixis Corporate & Investment Banking (Natixis CIB) is pleased to support Copenhagen Infrastructure Partners (CIP), through its Growth Markets Funds II (GMF II), as Joint Bookrunner, Joint Lead Arranger, and Green Loan Coordinator for the $510 million project financing for La Esperanza Solar, a utility-scale hybrid solar and battery energy storage project, strengthening energy supply and reliability in the Yucatan Peninsula. … through its 420 MWdc of installed solar photovoltaic capacity combined with 150 MW / 5-hour battery energy storage system",
        "note": "Opened Natixis PR Newswire on CIP La Esperanza USD 510m financing.",
    },
    {
        "id": "natixis_cip_esperanza_20260807",
        "type": "company",
        "chicago": "Natixis Corporate & Investment Banking. “Natixis Corporate & Investment Banking Supports CIP in $510 Million Project Financing in Mexico.” PR Newswire, 7 August 2026.",
        "url": "https://www.prnewswire.com/news-releases/natixis-corporate--investment-banking-supports-cip-in-510-million-project-financing-in-mexico-302846231.html",
        "annotation": "Lender primary on CIP La Esperanza 420 MWdc + 150 MW/5h BESS FC and USD 510m debt. Supports cip_la_esperanza_mexico_fc_2026.",
        "supports": ["cip_la_esperanza_mexico_fc_2026", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# 5 resources/lithium — Atlas Lithium Neves DFS CapEx (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "atlas_lithium_neves_dfs_57p6m_2025",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "us",
        "counterpart": "Atlas Lithium (NASDAQ: ATLX) — Neves Lithium Project DFS CapEx",
        "country": "Brazil",
        "asset": "4 Aug 2025: Atlas Lithium (Boca Raton, FL) announces SGS Canada Definitive Feasibility Study (Reg. S-K 1300) for 100%-owned Neves hard-rock lithium project (Minas Gerais Lithium Valley): after-tax IRR 145%, NPV USD 539m, 11-month payback; expected direct CapEx USD 57.6 million (lowest among announced Brazil peers per company); ~USD 30m already invested acquiring/transporting modular DMS plant to Brazil; two non-dilutive pre-payment offtakes totaling USD 40m. Pre-FID study CapEx — not closed spend. Distinct from Lithium Ionic Bandeira EXIM LOI / Hatch EPC.",
        "investment_type": "feasibility_capex",
        "value": "57600000",
        "currency": "USD",
        "value_usd": "57600000",
        "fx_usd": "1",
        "fx_date": "2025-08-04",
        "year": "2025",
        "status": "active",
        "lat": "-16.85",
        "lon": "-42.07",
        "geo_note": "Neves / Araçuaí Lithium Valley, Minas Gerais (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "atlas_lithium_neves_dfs_20250804",
        "note": "Actor: Atlas Lithium (U.S.-listed NASDAQ:ATLX, Boca Raton) — us. Company Newsfile release 4 Aug 2025; DFS CapEx USD 57.6m documented.",
    },
    {
        "id": "atlas_lithium_neves_dfs_57p6m_2025",
        "retrieved": "2026-10-01",
        "source_id": "atlas_lithium_neves_dfs_20250804",
        "url": "https://www.atlas-lithium.com/news/atlas-lithiums-neves-project-completes-definitive-feasibility-study-estimating-145-irr-and-11-month-payback/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "SGS Canada Inc. (“SGS”) has completed the Definitive Feasibility Study (“DFS”) for the Company’s 100%-owned Neves Lithium Project (“Project”), a technical report prepared under the U.S. guidelines of Item 1300 of Regulation S-K (“Regulation S-K 1300”). … expected direct capital expenditures of $57.6 million will be needed for the implementation of the Project, by far the lowest such capital costs among other announced projects in Brazil. Notably, Atlas Lithium has already invested approximately $30 million in acquiring and transporting the Project’s newly fabricated dense media separation (“DMS”) plant to Brazil",
        "note": "Opened Atlas Lithium Neves DFS company release.",
    },
    {
        "id": "atlas_lithium_neves_dfs_20250804",
        "type": "company",
        "chicago": "Atlas Lithium Corporation. “Atlas Lithium’s Neves Project Completes Definitive Feasibility Study Estimating 145% IRR and 11-Month Payback.” 4 August 2025.",
        "url": "https://www.atlas-lithium.com/news/atlas-lithiums-neves-project-completes-definitive-feasibility-study-estimating-145-irr-and-11-month-payback/",
        "annotation": "Company primary on Neves S-K 1300 DFS and USD 57.6m direct CapEx. Supports atlas_lithium_neves_dfs_57p6m_2025.",
        "supports": ["atlas_lithium_neves_dfs_57p6m_2025", "hunt_res_lithium"],
    },
)

# ---------------------------------------------------------------------------
# 10 resources/niobium — Boston Metal Coronel Xavier Chaves MOE plant (us)
# ---------------------------------------------------------------------------
A(
    {
        "id": "boston_metal_coronel_xavier_plant_2025",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "us",
        "counterpart": "Boston Metal do Brasil — Coronel Xavier Chaves MOE critical-metals plant",
        "country": "Brazil",
        "asset": "Apr 2025 (Diário do Comércio) / May 2026 (MIT Technology Review): Boston Metal (U.S.) subsidiary Boston Metal do Brasil advances first commercial molten-oxide electrolysis (MOE) plant at Coronel Xavier Chaves (near São João del-Rei, Minas Gerais) to produce niobium, tantalum and tin ferroalloys from mining/metallurgical residues; press cites R$ 1 billion investment through 2026 and ~12,000 tpy product capacity across five electrolytic cells; MIT TR confirms Brazil commercial facility and Sep 2026 restart target after Jan 2026 refractory leak. Distinct from St George–Boston Metal Araxá MOE trial MoU (feedstock MoU only).",
        "investment_type": "greenfield_plant",
        "value": "1000000000",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2025-04-06",
        "year": "2025",
        "status": "active",
        "lat": "-21.02",
        "lon": "-44.22",
        "geo_note": "Coronel Xavier Chaves, Minas Gerais (Diário do Comércio / Boston Metal geography).",
        "evidence": "proxy",
        "source_id": "diario_comercio_boston_metal_20250406",
        "note": "Actor: Boston Metal (U.S.) via Boston Metal do Brasil — us. UNVERIFIED proxy: Diário do Comércio 6 Apr 2025 citing R$1bn through 2026 and 12 ktpy; MIT Technology Review 20 May 2026 confirms Brazil commercial Nb/Ta/Sn facility (no CapEx on MIT page). Value stored as BRL.",
    },
    {
        "id": "boston_metal_coronel_xavier_plant_2025",
        "retrieved": "2026-10-01",
        "source_id": "diario_comercio_boston_metal_20250406",
        "url": "https://diariodocomercio.com.br/economia/boston-metal-inicia-producao-escala-industrial-minas-gerais/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "A Boston Metal do Brasil irá iniciar no próximo mês a produção em escala industrial na unidade em Coronel Xavier Chaves, município próximo de São João del-Rei, no Campo das Vertentes. Com investimentos de R$ 1 bilhão até 2026, o espaço vai abrigar o primeiro hub de metais estratégicos do mundo produzidos a partir da tecnologia de Eletrólise de Óxido Fundido (MOE). A unidade terá capacidade para produzir 12 mil toneladas anuais de produtos à base de tântalo, nióbio e estanho",
        "note": "Opened Diário do Comércio Boston Metal Coronel Xavier Chaves plant article; CapEx UNVERIFIED proxy.",
    },
    {
        "id": "diario_comercio_boston_metal_20250406",
        "type": "press",
        "chicago": "Diário do Comércio. “Boston Metal vai investir R$ 1 bilhão até 2026 na planta de Coronel Xavier Chaves.” 6 April 2025.",
        "url": "https://diariodocomercio.com.br/economia/boston-metal-inicia-producao-escala-industrial-minas-gerais/",
        "annotation": "UNVERIFIED press on Boston Metal do Brasil Coronel Xavier Chaves MOE plant CapEx/capacity. Supports boston_metal_coronel_xavier_plant_2025.",
        "supports": ["boston_metal_coronel_xavier_plant_2025", "hunt_fenb_araxa"],
    },
)

# ---------------------------------------------------------------------------
# 18 energy/solar — POWERCHINA Francisco Juana PV Colombia (prc)
# ---------------------------------------------------------------------------
A(
    {
        "id": "powerchina_francisco_juana_colombia_2026",
        "layer": "energy",
        "subcategory": "solar",
        "side": "prc",
        "counterpart": "POWERCHINA — Francisco Juana PV Project (Caldas)",
        "country": "Colombia",
        "asset": "18–24 Sep 2026: POWERCHINA Francisco Juana PV Project in Caldas Department obtains owner acceptance certificate and is fully completed/handed over ahead of schedule; comprises Francisco (Plant F) and Juana (Plant D) solar plants totaling 15.99 MW; full EPC (design, procurement, international logistics, construction, commissioning, grid connection, handover); expected ~22.48 GWh/year; >200 direct jobs (95% local). POWERCHINA’s second completed new-energy plant handover in Colombia. CAPEX USD not disclosed. Distinct from POWERCHINA Guayepo III.",
        "investment_type": "epc",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "2026-09-18",
        "year": "2026",
        "status": "active",
        "lat": "5.07",
        "lon": "-75.52",
        "geo_note": "Caldas Department, Colombia (POWERCHINA release; approximate departmental pin).",
        "evidence": "documented",
        "source_id": "powerchina_francisco_juana_20260924",
        "note": "Actor: POWERCHINA (PRC SOE) — prc. Company English news 24 Sep 2026; no contract USD on page.",
    },
    {
        "id": "powerchina_francisco_juana_colombia_2026",
        "retrieved": "2026-10-01",
        "source_id": "powerchina_francisco_juana_20260924",
        "url": "https://en.powerchina.cn/2026-09/24/c_829123.htm",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "POWERCHINA's Francisco Juana PV Project in Colombia obtained the certificate of acceptance of works issued by the project owner on Sept 18. Having fulfilled all contractual obligations, the project was fully completed and handed over ahead of schedule. Located in the Caldas Department of Colombia, the project comprises Francisco (Plant F) and Juana (Plant D) solar power plants, with a total installed capacity of 15.99 MW. The construction covered the entire EPC process, including design, procurement, international logistics, construction and installation, commissioning, grid connection, and handover.",
        "note": "Opened POWERCHINA Francisco Juana PV completion release.",
    },
    {
        "id": "powerchina_francisco_juana_20260924",
        "type": "company",
        "chicago": "POWERCHINA. “POWERCHINA completes Francisco Juana PV Project in Colombia.” 24 September 2026.",
        "url": "https://en.powerchina.cn/2026-09/24/c_829123.htm",
        "annotation": "Company primary on Francisco Juana 15.99 MW EPC handover in Caldas. Supports powerchina_francisco_juana_colombia_2026.",
        "supports": ["powerchina_francisco_juana_colombia_2026", "hunt_energy_solar"],
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
        "hunt_latam_rail_telecom": "Cycle 53: logged ustda_honduras_confi_shoreline_2026 (U.S.; CONFI/ShorelineHudson corridor FS).",
        "hunt_br_power_equip": "Cycle 53: equal budget; GE Vernova Azulão / Siemens AXIA / USTDA Ecuador already (miss).",
        "hunt_infra_bridges_roads": "Cycle 53: logged chec_jamaica_north_south_mou_2025 (PRC; 40 km North-South FS MoU).",
        "hunt_energy_other_renewables": "Cycle 53: logged cip_la_esperanza_mexico_fc_2026 (allied; 420 MWdc + 150 MW/5h BESS; USD 510m debt).",
        "hunt_res_lithium": "Cycle 53: logged atlas_lithium_neves_dfs_57p6m_2025 (U.S.; DFS direct CapEx USD 57.6m).",
        "hunt_infra_port_cranes": "Cycle 53: equal budget; Konecranes Cartagena/Acajutla / ZPMC Aguadulce already (miss).",
        "hunt_res_copper": "Cycle 53: equal budget; FCX El Abra / Vicuña RIGI / Centinela already (miss).",
        "hunt_infra_building_materials": "Cycle 53: equal budget; Holcim Pacasmayo/Guayaquil/Nobsa already (miss).",
        "hunt_energy_wind": "Cycle 53: equal budget; Vestas Esquina do Vento / Dom Inocêncio / Goldwind already (miss).",
        "hunt_fenb_araxa": "Cycle 53: logged boston_metal_coronel_xavier_plant_2025 (U.S.; MOE Nb/Ta/Sn plant; R$1bn proxy).",
        "hunt_infra_engineering_epc": "Cycle 53: equal budget; Worley / Bechtel / Fluor / Xinhai already (miss).",
        "hunt_res_graphite": "Cycle 53: equal budget; Graphcoa / South Star / Atlas Malacacheta already (miss).",
        "hunt_res_nickel": "Cycle 53: equal budget; DFC Piauí / Centaurus Glencore / Jaguar JVEP already (miss).",
        "hunt_energy_fission_smr": "Cycle 53: equal budget; Jamaica AECL / El Salvador 123 / Meitner already (miss).",
        "hunt_res_balsa": "Cycle 53: equal budget; WITS / CoreLite / Plantabal already (miss).",
        "hunt_infra_port_ownership": "Cycle 53: equal budget; APM Callao 3B / Lázaro Phase III / SSA already (miss).",
        "hunt_res_water": "Cycle 53: equal budget; Acciona Yanacocha / Bechtel QB2 / SADDN already (miss).",
        "hunt_energy_solar": "Cycle 53: logged powerchina_francisco_juana_colombia_2026 (PRC; 15.99 MW Caldas handover).",
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
    print("Cycle 53 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
