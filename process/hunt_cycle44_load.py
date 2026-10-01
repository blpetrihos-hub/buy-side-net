#!/usr/bin/env python3
"""Cycle 44 hunt: shuffle_seed=20261044; equal budget; U.S. side ≥1/3; thin_topup after.

Order: graphite, engineering_epc, balsa, fission_smr, power_plants_grid,
other_renewables, niobium, port_cranes, lithium, rail, wind, solar, copper,
nickel, bridges_roads, water, port_ownership, building_materials.
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
UPDATES: list[tuple[str, dict, dict | None, dict | None]] = []


def A(row, evidence, bib):
    ITEMS.append((row, evidence, bib))


def U(rid, row_patch, evidence=None, bib=None):
    UPDATES.append((rid, row_patch, evidence, bib))


# ---------------------------------------------------------------------------
# 1 resources/graphite — Atlas Malacacheta AETC nuclear-grade purification (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "atlas_malacacheta_aetc_nuclear_2025",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "us",
        "counterpart": "Atlas Critical Minerals / AETC — Malacacheta nuclear-grade graphite purification",
        "country": "Brazil",
        "asset": "12 Nov 2025: Atlas Critical Minerals (OTCQB: JUPGF) reports AETC (U.S.) thermal purification of Malacacheta (Minas Gerais) flake-graphite concentrate to 99.9995 wt.% C (ash 0.0005 wt.%) at 2,800°C in nitrogen without halogen gas — nuclear-grade purity target. Lab-scale characterization/purification milestone; no disclosed mine CAPEX in the release. Distinct from atlas_malacacheta_graphite_mre_2026 (MRE).",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-17.8",
        "lon": "-42.1",
        "geo_note": "Malacacheta municipality, Minas Gerais (Atlas/SGS geography; approximate pin).",
        "evidence": "documented",
        "source_id": "atlas_aetc_nuclear_graphite_20251112",
        "note": "Actor: Atlas Critical Minerals (U.S. OTCQB issuer) with AETC U.S. lab — us. Company Newsfile release 12 Nov 2025. Processing/anode–nuclear chain evidence; not a commercial reactor-qualified supply contract.",
    },
    {
        "id": "atlas_malacacheta_aetc_nuclear_2025",
        "retrieved": "2026-10-01",
        "source_id": "atlas_aetc_nuclear_graphite_20251112",
        "url": "https://www.atlascriticalminerals.com/news/atlas-critical-minerals-confirms-nuclear-grade-quality-at-its-graphite-project/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "comprehensive characterization and thermal purification testwork performed on graphite concentrate from its Malacacheta Graphite Project in Minas Gerais, Brazil has achieved nuclear-grade purity specifications of 99.9995 wt.% carbon (99.9995% C). … The testwork was conducted by American Energy Technologies Company (“AETC”) … Thermal purification at 2,800°C in an inert nitrogen atmosphere yielded loss on ignition (LOI) purity of 99.9995 wt.% carbon with ash content of only 0.0005 wt.%.",
        "note": "Opened Atlas Critical Minerals company news 12 Nov 2025.",
    },
    {
        "id": "atlas_aetc_nuclear_graphite_20251112",
        "type": "company",
        "chicago": "Atlas Critical Minerals Corporation. “Atlas Critical Minerals Confirms Nuclear-Grade Quality at Its Graphite Project.” 12 November 2025.",
        "url": "https://www.atlascriticalminerals.com/news/atlas-critical-minerals-confirms-nuclear-grade-quality-at-its-graphite-project/",
        "annotation": "Company primary on AETC nuclear-grade purification of Malacacheta concentrate. Supports atlas_malacacheta_aetc_nuclear_2025.",
        "supports": ["atlas_malacacheta_aetc_nuclear_2025", "hunt_res_graphite"],
    },
)

# ---------------------------------------------------------------------------
# 2 infrastructure/engineering_epc — equal-budget miss (U.S. search: Bechtel
#   Yanacocha WTP LinkedIn-only; Bechtel–EIMISA / Fluor Toromocho already logged).
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 3 resources/balsa — equal-budget miss (U.S. search: Plantabal→Baltek/TPI supply
#   chain in EIA report; Plantabal 2025 planting / WITS 2025 CN–US pair already).
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 4 energy/fission_smr — El Salvador NCMOU (U.S. State Dept; VOA Spanish coverage)
# ---------------------------------------------------------------------------
A(
    {
        "id": "el_salvador_ncmou_20250203",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "us",
        "counterpart": "U.S. Department of State — El Salvador Strategic Civil Nuclear NCMOU",
        "country": "El Salvador",
        "asset": "3 Feb 2025: U.S. Secretary of State Marco Rubio and Salvadoran Foreign Minister Alexandra Hill Tinoco sign a non-binding Nuclear Cooperation Memorandum of Understanding (NCMOU) on strategic civil nuclear cooperation. Framed as an initial step toward a civil nuclear partnership (energy security, safety/security/nonproliferation); does not itself authorize reactor exports or create legal obligations. Later followed by FIRST bilateral partnership (see NPT PrepCom U.S. statement). Framework diplomacy — no project CAPEX.",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "13.69",
        "lon": "-89.19",
        "geo_note": "San Salvador signing venue (country capital pin; no reactor site named).",
        "evidence": "documented",
        "source_id": "voa_elsalvador_ncmou_20250204",
        "note": "Actor: U.S. Department of State with El Salvador MFA — us. VOA (4 Feb 2025) relays State Department NCMOU framing; official State.gov release URL also exists (bot egress 403 in this environment). Distinct from peru_first / argentina_first workshop rows.",
    },
    {
        "id": "el_salvador_ncmou_20250203",
        "retrieved": "2026-10-01",
        "source_id": "voa_elsalvador_ncmou_20250204",
        "url": "https://www.vozdeamerica.com/a/que-propone-acuerdo-cooperacion-nuclear-eeuu-el-salvador/7962814.html",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Los jefes de la diplomacia de Estados Unidos y El Salvador, Marco Rubio y Alexandra Hill, respectivamente, firmaron el lunes un Memorando de Entendimiento sobre Cooperación Nuclear Civil Estratégica (NCMOU). … este NCMOU “representa un paso inicial hacia el establecimiento de una sólida asociación nuclear civil” entre los dos países con miras a “mejorar la seguridad energética” del país centroamericano.",
        "note": "Opened VOA Spanish coverage 4 Feb 2025 quoting U.S. State Department NCMOU language.",
    },
    {
        "id": "voa_elsalvador_ncmou_20250204",
        "type": "press",
        "chicago": "Voz de América. “¿Qué propone el acuerdo de cooperación en energía nuclear entre EEUU y El Salvador?” 4 February 2025.",
        "url": "https://www.vozdeamerica.com/a/que-propone-acuerdo-cooperacion-nuclear-eeuu-el-salvador/7962814.html",
        "annotation": "Spanish-language VOA report of U.S.–El Salvador NCMOU signing with State Department framing. Supports el_salvador_ncmou_20250203.",
        "supports": ["el_salvador_ncmou_20250203", "hunt_energy_fission_smr"],
    },
)

# ---------------------------------------------------------------------------
# 5 energy/power_plants_grid — GE Vernova Azulão I COD 295 MW (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ge_vernova_azulao_i_cod_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "GE Vernova / Eneva — Azulão I gas plant COD (Silves, Amazonas)",
        "country": "Brazil",
        "asset": "19 Aug 2026: GE Vernova and Eneva announce commercial operation of Azulão I thermal plant in Silves, Amazonas (~330 km from Manaus). Contracted 295 MW firm/dispatchable capacity to Brazil’s SIN for 15 years; powered by GE Vernova 7HA.02 gas turbine + H65 generator; includes 15-year GE Vernova service agreement. First phase of Azulão Complex (I+II targeting up to ~950 MW; Azulão II COD targeted Jul 2027). OEM/equipment+services milestone — plant CAPEX not stated in GE Vernova release.",
        "investment_type": "brownfield_expansion",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-2.84",
        "lon": "-58.21",
        "geo_note": "Silves, Amazonas (company geography ~330 km from Manaus; approximate plant pin).",
        "evidence": "documented",
        "source_id": "ge_vernova_azulao_cod_20260819",
        "note": "Actor: GE Vernova Inc. (NYSE: GEV, U.S.) equipment/services with Eneva (Brazil operator) — us. Company press 19 Aug 2026. Distinct from ge_vernova_serra_tigre_ais_2023 / ge_vernova_transelec_sync_chile_2024.",
    },
    {
        "id": "ge_vernova_azulao_i_cod_2026",
        "retrieved": "2026-10-01",
        "source_id": "ge_vernova_azulao_cod_20260819",
        "url": "https://www.gevernova.com/news/press-releases/eneva-ge-vernova-launch-operations-azulao-power-plant-deploy-firm-power-complex",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "GE Vernova Inc. (NYSE: GEV) and Eneva … celebrated the start of commercial operation of the Azulão I thermal power plant, located in Silves, approximately 330 kilometers (205 miles) from Manaus. Contracted to provide 295 megawatts (MW) of capacity to Brazil’s National Interconnected System (SIN) for 15 years … At the heart of the Azulão I facility is GE Vernova’s high-performance 7HA.02 gas turbine, paired with a H65 generator. … GE Vernova secured a 15-year service agreement.",
        "note": "Opened GE Vernova press release 19 Aug 2026.",
    },
    {
        "id": "ge_vernova_azulao_cod_20260819",
        "type": "company",
        "chicago": "GE Vernova. “Eneva and GE Vernova launch operations at Azulão Power Plant to deploy firm power in complex transmission environments.” 19 August 2026.",
        "url": "https://www.gevernova.com/news/press-releases/eneva-ge-vernova-launch-operations-azulao-power-plant-deploy-firm-power-complex",
        "annotation": "Company primary on Azulão I COD, 295 MW SIN contract, 7HA.02 + 15-year service. Supports ge_vernova_azulao_i_cod_2026.",
        "supports": ["ge_vernova_azulao_i_cod_2026", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 6 energy/other_renewables — CIP Patache BESS FNTP 300 MW / 1,500 MWh (allied)
# ---------------------------------------------------------------------------
A(
    {
        "id": "cip_patache_bess_fntp_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "allied",
        "counterpart": "Copenhagen Infrastructure Partners (GMF II) — Patache BESS FNTP",
        "country": "Chile",
        "asset": "20 Apr 2026: CIP Growth Markets Fund II issues Final Notice to Proceed for Patache standalone BESS (300 MW / 1,500 MWh) near Iquique, Tarapacá Region — second large CIP BESS in Chile after Arena (220 MW / 1,100 MWh). FNTP authorises construction under main supply/construction contracts. CAPEX not disclosed in CIP release.",
        "investment_type": "greenfield_storage",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-20.80",
        "lon": "-70.15",
        "geo_note": "Patache / Tarapacá near Iquique (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "cip_patache_fntp_20260420",
        "note": "Actor: Copenhagen Infrastructure Partners (Denmark) — allied. CIP/Cision release 20 Apr 2026. Distinct from catl_cip_alegria_bess_2026 / trina Atlas Copiapó / Acciona BESS rows.",
    },
    {
        "id": "cip_patache_bess_fntp_2026",
        "retrieved": "2026-10-01",
        "source_id": "cip_patache_fntp_20260420",
        "url": "https://news.cision.com/copenhagen-infrastructure-partners-p-s/r/copenhagen-infrastructure-partners-commences-construction-on-1-500-mwh-bess-project-in-chile,c4357424",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Copenhagen Infrastructure Partners (CIP), through its Growth Markets Fund II (GMF II) has issued Final Notice to Proceed (FNTP) for the 300 MW / 1,500 MWh Patache project. The issuance of FNTP authorises the start of construction activities under the main supply and construction contracts … Project Patache will be Copenhagen Infrastructure Partners’ second large-scale battery energy storage system (BESS) in Chile … builds on the learnings from CIP’s Arena BESS project, a 220 MW / 1,100 MWh BESS project located in the Antofagasta region.",
        "note": "Opened CIP Cision release 20 Apr 2026.",
    },
    {
        "id": "cip_patache_fntp_20260420",
        "type": "company",
        "chicago": "Copenhagen Infrastructure Partners. “Copenhagen Infrastructure Partners commences construction on 1,500 MWh BESS project in Chile.” Cision, 20 April 2026.",
        "url": "https://news.cision.com/copenhagen-infrastructure-partners-p-s/r/copenhagen-infrastructure-partners-commences-construction-on-1-500-mwh-bess-project-in-chile,c4357424",
        "annotation": "CIP primary on Patache 300 MW / 1,500 MWh FNTP. Supports cip_patache_bess_fntp_2026.",
        "supports": ["cip_patache_bess_fntp_2026", "hunt_energy_other_renewables"],
    },
)

# ---------------------------------------------------------------------------
# 7 resources/niobium — Fangda offtake/development MoU with St George Araxá (PRC)
# ---------------------------------------------------------------------------
A(
    {
        "id": "fangda_st_george_araxa_mou_20250115",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "prc",
        "counterpart": "Liaoning Fangda / Beijing Fangda — St George Araxá Nb offtake MoU",
        "country": "Brazil",
        "asset": "15 Jan 2025: St George Mining (ASX: SGQ) signs non-binding MoU with Liaoning Fangda Group (via Beijing Fangda Carbon-Tech) for Araxá niobium-REE project (Minas Gerais). Framework contemplates potential exclusive offtake of 20% of niobium products for 5 years (+5-year option), market-linked pricing, possible prepayment/development funding, and technical mine-development support. Aim to negotiate binding partnership within nine months. No financial obligation on St George under the MoU.",
        "investment_type": "offtake",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "Araxá, Minas Gerais (St George project geography; same pin family as st_george_araxa_nb_2025).",
        "evidence": "documented",
        "source_id": "stgm_fangda_mou_20250115",
        "note": "Actor: Liaoning Fangda Group / Beijing Fangda (PRC) — prc. Complements st_george_realloys_mou_2025 (U.S. REAlloys offtake MoU) as paired PRC-vs-U.S. offtake interest on same Araxá asset. ASX release 15 Jan 2025.",
    },
    {
        "id": "fangda_st_george_araxa_mou_20250115",
        "retrieved": "2026-10-01",
        "source_id": "stgm_fangda_mou_20250115",
        "url": "https://stgm.com.au/pdf/d7f79c5f-b803-441c-b362-df5383058514/Steelmaking-Giant-signs-Offtake-and-Development-MoU.pdf",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "St George Mining Limited (ASX: SGQ) … has signed a Memorandum of Understanding (“MoU”) with the Liaoning Fangda Group, through its wholly owned subsidiary Beijing Fangda Carbon-Tech Co., Ltd (“Beijing Fangda”) … Key terms of a potential offtake agreement may include: 1. Fangda to be granted exclusive rights to acquire 20% of niobium products from the Project; 2. Offtake to last for a term of five (5) years, with an option for Fangda to extend for a further five (5) years; 3. Pricing for offtake based on a market-linked reference price; and 4. A prepayment loan facility. … There is no financial obligation on St George under the MoU.",
        "note": "Opened St George Mining ASX PDF 15 Jan 2025.",
    },
    {
        "id": "stgm_fangda_mou_20250115",
        "type": "company",
        "chicago": "St George Mining Limited. “Steelmaking Giant signs Offtake and Development MoU with St George.” ASX release, 15 January 2025.",
        "url": "https://stgm.com.au/pdf/d7f79c5f-b803-441c-b362-df5383058514/Steelmaking-Giant-signs-Offtake-and-Development-MoU.pdf",
        "annotation": "ASX primary on Fangda–St George Araxá Nb offtake/development MoU. Supports fangda_st_george_araxa_mou_20250115.",
        "supports": ["fangda_st_george_araxa_mou_20250115", "hunt_fenb_araxa"],
    },
)

# ---------------------------------------------------------------------------
# 8 infrastructure/port_cranes — equal-budget miss (U.S. search: SSA Guaymas /
#   STI San Antonio equipment already logged under port_ownership this cycle).
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 9 resources/lithium — EnergyX EXIM LOI USD 690m for Project Black Giant (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "energyx_exim_loi_690m_black_giant_2025",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "us",
        "counterpart": "U.S. EXIM — LOI for EnergyX Project Black Giant (Chile)",
        "country": "Chile",
        "asset": "16 Sep 2025: EnergyX (Austin, TX) announces signed EXIM letter of interest representing USD 690 million in potential project-finance support for Project Black Giant™ DLE lithium mine/refinery (Antofagasta Region; target 52,500 tpa LCE). Same release notes PFS completion and Goldman Sachs FA mandate. LOI — not a closed loan; distinct from eni_energyx_black_giant_2026 (Eni 25% / USD 225m allied equity).",
        "investment_type": "financing",
        "value": "690000000",
        "currency": "USD",
        "value_usd": "690000000",
        "fx_usd": "1",
        "fx_date": "2025-09-16",
        "year": "2025",
        "status": "active",
        "lat": "-24.6",
        "lon": "-69.0",
        "geo_note": "Salar de Punta Negra / western alluvials, Antofagasta (EnergyX project geography; same pin family as eni_energyx_black_giant_2026).",
        "evidence": "documented",
        "source_id": "energyx_exim_loi_20250916",
        "note": "Actor: U.S. EXIM LOI to EnergyX (U.S. developer) — us. Company press 16 Sep 2025. Complements chilean_cobalt_exim_loi_375m_2026 / exim_argentina_build_future_7bn_2026 as LatAm critical-minerals EXIM pipeline.",
    },
    {
        "id": "energyx_exim_loi_690m_black_giant_2025",
        "retrieved": "2026-10-01",
        "source_id": "energyx_exim_loi_20250916",
        "url": "https://energyx.com/press-release/energyx-pfs-goldman-exim-project-black-giant",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "EnergyX has received a signed letter of interest from the United States Export Import Bank (EXIM) representing $690 million in project finance support … Project Black Giant will be designed for a total production capacity of 52,500 tonnes per annum (tpa) of battery-grade lithium carbonate (LCE). … In parallel, EnergyX has secured a signed letter of interest from EXIM bank representing $690 million in potential investment.",
        "note": "Opened EnergyX company press release 16 Sep 2025.",
    },
    {
        "id": "energyx_exim_loi_20250916",
        "type": "company",
        "chicago": "Energy Exploration Technologies, Inc. “EnergyX Engages with Goldman Sachs, Secures $690M Investor Interest from U.S. EXIM Bank, and Announces Completion of 52,500-ton Project Black Giant™ Lithium Validation Study.” 16 September 2025.",
        "url": "https://energyx.com/press-release/energyx-pfs-goldman-exim-project-black-giant",
        "annotation": "Company primary on EXIM LOI USD 690m for Black Giant Chile. Supports energyx_exim_loi_690m_black_giant_2025.",
        "supports": ["energyx_exim_loi_690m_black_giant_2025", "hunt_res_lithium"],
    },
)

# ---------------------------------------------------------------------------
# 10–16 equal-budget misses (U.S. search logged in hunt stub notes):
#   rail, wind, solar, copper, nickel, bridges_roads, water
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# 17 infrastructure/port_ownership — STI San Antonio concession CAPEX USD 66m (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "sti_san_antonio_capex_66m_2024",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "us",
        "counterpart": "SSA Marine / STI — San Antonio Terminal Internacional concession CAPEX",
        "country": "Chile",
        "asset": "Dec 2024: Empresa Portuaria San Antonio (EPSA) notifies CMF that STI fulfilled 2020 investment conditions; concession extended to 1 Jan 2030. STI GM Andrés Albertini: intensive CAPEX plan investing USD 66 million (of which USD 47 million to extend the concession). Upgrades include 2 STS + 2 RTG cranes, 27 reefer towers, reach stackers, terminal tractors, civil/tech. STI is 50/50 JV SSA Marine (Seattle) / SAAM. Capacity ~+30% to ~1.6m TEU/year.",
        "investment_type": "concession",
        "value": "66000000",
        "currency": "USD",
        "value_usd": "66000000",
        "fx_usd": "1",
        "fx_date": "2024-12-04",
        "year": "2024",
        "status": "active",
        "lat": "-33.58",
        "lon": "-71.61",
        "geo_note": "San Antonio Terminal Internacional, Port of San Antonio, Chile (terminal pin).",
        "evidence": "documented",
        "source_id": "container_news_sti_20241204",
        "note": "Actor: SSA Marine / Carrix (U.S.-headquartered) JV with SAAM — us (same convention as ssa_guaymas_sts_ertg_2026). Container News 4 Dec 2024 quoting STI/EPSA. Distinct from DP World San Antonio PCE.",
    },
    {
        "id": "sti_san_antonio_capex_66m_2024",
        "retrieved": "2026-10-01",
        "source_id": "container_news_sti_20241204",
        "url": "https://container-news.com/san-antonio-terminal-internacional-concession-extended-to-2030/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "“In recent years we have implemented an intensive capex plan, investing US$66 million, of which US$47 million was to extend the concession. …” commented STI general manager Andrés Albertini. … In total, contractual investments along with additional contributions amounted to US$66 million. STI’s upgrades included the acquisition of two STS cranes, two RTG cranes, 27 new reefer towers, six reach stackers, 26 terminal tractors, and significant civil infrastructure and technological enhancements.",
        "note": "Opened Container News 4 Dec 2024 (non-paywalled).",
    },
    {
        "id": "container_news_sti_20241204",
        "type": "press",
        "chicago": "Container News. “San Antonio Terminal Internacional concession extended to 2030.” 4 December 2024.",
        "url": "https://container-news.com/san-antonio-terminal-internacional-concession-extended-to-2030/",
        "annotation": "Trade press on STI USD 66m CAPEX and concession extension to 2030. Supports sti_san_antonio_capex_66m_2024.",
        "supports": ["sti_san_antonio_capex_66m_2024", "hunt_infra_port_ownership"],
    },
)

# ---------------------------------------------------------------------------
# 18 infrastructure/building_materials — equal-budget miss (U.S. search: Holcim /
#   Cemex LatAm already dense; no distinct new U.S. primary opened this box).
# ---------------------------------------------------------------------------


def upsert_bib(bib, bib_by, bib_entry):
    if not bib_entry:
        return
    sid = bib_entry["id"]
    if sid in bib_by:
        existing = bib[bib_by[sid]]
        for k, v in bib_entry.items():
            if v is not None:
                existing[k] = v
    else:
        bib.append(bib_entry)
        bib_by[sid] = len(bib) - 1


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {e["id"]: i for i, e in enumerate(bib)}
    added, updated = [], []

    for rid, patch, evidence, bib_entry in UPDATES:
        if rid not in by_id:
            raise SystemExit(f"missing update target {rid}")
        rows[by_id[rid]].update({k: v for k, v in patch.items() if v is not None})
        updated.append(rid)
        if evidence:
            (EVID / f"{rid}.json").write_text(
                json.dumps(evidence, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
        upsert_bib(bib, bib_by, bib_entry)

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: row.get(k, "") for k in FIELDS}
        if rid in by_id:
            rows[by_id[rid]].update(full)
            updated.append(rid)
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
        "hunt_res_graphite": "Cycle 44: logged atlas_malacacheta_aetc_nuclear_2025 (U.S. AETC nuclear-grade purification).",
        "hunt_infra_engineering_epc": "Cycle 44: equal budget; Bechtel Yanacocha LinkedIn-only / Bechtel–EIMISA already (miss).",
        "hunt_res_balsa": "Cycle 44: equal budget; Plantabal 2025 planting / WITS 2025 pair / Baltek supply chain already (miss).",
        "hunt_energy_fission_smr": "Cycle 44: logged el_salvador_ncmou_20250203 (U.S. NCMOU).",
        "hunt_br_power_equip": "Cycle 44: logged ge_vernova_azulao_i_cod_2026 (U.S.; 295 MW COD).",
        "hunt_energy_other_renewables": "Cycle 44: logged cip_patache_bess_fntp_2026 (allied; 300 MW / 1,500 MWh).",
        "hunt_fenb_araxa": "Cycle 44: logged fangda_st_george_araxa_mou_20250115 (PRC; pairs with REAlloys MoU).",
        "hunt_infra_port_cranes": "Cycle 44: equal budget; STI crane CAPEX coded under port_ownership; SSA Guaymas already (miss).",
        "hunt_res_lithium": "Cycle 44: logged energyx_exim_loi_690m_black_giant_2025 (U.S. EXIM LOI USD 690m).",
        "hunt_latam_rail_telecom": "Cycle 44: equal budget; Mota-Engil QI / CRCC / Alstom already (miss).",
        "hunt_energy_wind": "Cycle 44: equal budget; Vestas Emma / Statkraft / Nordex already (miss).",
        "hunt_energy_solar": "Cycle 44: equal budget; AES Andes III / Polaris / Trina already (miss).",
        "hunt_res_copper": "Cycle 44: equal budget; FCX El Abra / Chilean Cobalt EXIM / Tía María already (miss).",
        "hunt_res_nickel": "Cycle 44: equal budget; DFC PNP / Centaurus Jaguar / Atlantic Nickel already (miss).",
        "hunt_infra_bridges_roads": "Cycle 44: equal budget; CHEC / OHLA / Mota-Engil Santos–Guarujá already (miss).",
        "hunt_res_water": "Cycle 44: equal budget; Newmont Yanacocha IR bot-blocked; Acciona/Sacyr desal already (miss).",
        "hunt_infra_port_ownership": "Cycle 44: logged sti_san_antonio_capex_66m_2024 (U.S. SSA Marine JV; USD 66m).",
        "hunt_infra_building_materials": "Cycle 44: equal budget; Holcim/Cemex LatAm already dense (miss).",
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
    print("Cycle 44 rows added:", len(added))
    print("\n".join(added))
    print("Cycle 44 rows updated:", len(updated))
    print("\n".join(updated))


if __name__ == "__main__":
    main()
