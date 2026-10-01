#!/usr/bin/env python3
"""Cycle 28 hunt: shuffle_seed=20261028; equal budget across 18 subcategories."""
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


# seed 20261028 order:
# engineering_epc, water, balsa, nickel, wind, power_plants_grid, graphite,
# bridges_roads, fission_smr, solar, building_materials, rail, copper, lithium,
# port_ownership, niobium, port_cranes, other_renewables

# 1 infrastructure/engineering_epc — miss (Bechtel–EIMISA already logged)
# 2 resources/water — miss (Rosarito / Collahuasi / Sacyr / Ilopango already)

# 3 resources/balsa — Ecuador 2025 manufactures exports (China / US destination shares)
A(
    {
        "id": "aima_ecuador_balsa_mfr_china_2025",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "prc",
        "counterpart": "Ecuador — 2025 manufactures-of-balsa exports attributed to China (AIMA share)",
        "country": "Ecuador",
        "asset": "AIMA via MAGAP: Ecuador 2025 manufactures-of-balsa exports USD 301.3 million (+38% vs 2024); Forbes Ecuador citing AIMA attributes 72.51% of manufactures-of-balsa destination share to China → implied ~USD 218.47 million China-bound manufactures (UNVERIFIED destination split)",
        "investment_type": "trade_flow",
        "value": "218472630",
        "currency": "USD",
        "value_usd": "218472630",
        "fx_usd": "1",
        "fx_date": "2025-12-31",
        "year": "2025",
        "status": "active",
        "lat": "-2.17",
        "lon": "-79.9",
        "geo_note": "Ecuador coastal balsa manufacturing/export hub proxy (Guayas/Los Ríos corridor).",
        "evidence": "proxy",
        "source_id": "magap_aima_balsa_2025",
        "note": "Trade flow (manufactures, not WITS HS 440723 logs). MAGAP official page documents AIMA USD 301.3m 2025 manufactures total; China 72.51% share from Forbes Ecuador citing AIMA (UNVERIFIED destination split applied to MAGAP total). Distinct from wits_ecuador_balsa_china_2022–2024 HS 440723 rows and plantabal_3a presence.",
    },
    {
        "id": "aima_ecuador_balsa_mfr_china_2025",
        "retrieved": "2026-10-01",
        "source_id": "magap_aima_balsa_2025",
        "url": "https://www.agricultura.gob.ec/ecuador-fortalece-la-cadena-de-balsa-para-proteger-su-acceso-a-mercados-internacionales/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "en 2025, las exportaciones mundiales de manufacturas de balsa alcanzaron USD 301,3 millones, un 38% más que en 2024, de acuerdo a información proporcionada por AIMA",
        "note": "Opened MAGAP official Spanish page. Destination China share from Forbes Ecuador (secondary) applied as proxy.",
    },
    {
        "id": "magap_aima_balsa_2025",
        "type": "government",
        "chicago": "Ministerio de Agricultura, Ganadería y Pesca (Ecuador) / AIMA. “Ecuador fortalece la cadena de balsa para proteger su acceso a mercados internacionales.” 2026.",
        "url": "https://www.agricultura.gob.ec/ecuador-fortalece-la-cadena-de-balsa-para-proteger-su-acceso-a-mercados-internacionales/",
        "annotation": "Official MAGAP notice citing AIMA USD 301.3m 2025 balsa manufactures exports. Supports aima_ecuador_balsa_mfr_china_2025 / _us_2025 (destination shares proxy).",
        "supports": [
            "aima_ecuador_balsa_mfr_china_2025",
            "aima_ecuador_balsa_mfr_us_2025",
            "hunt_res_balsa",
        ],
    },
)
A(
    {
        "id": "aima_ecuador_balsa_mfr_us_2025",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "us",
        "counterpart": "Ecuador — 2025 manufactures-of-balsa exports attributed to United States (AIMA share)",
        "country": "Ecuador",
        "asset": "Same AIMA/MAGAP 2025 manufactures-of-balsa total USD 301.3 million; Forbes Ecuador citing AIMA attributes 9.95% destination share to United States → implied ~USD 29.98 million US-bound manufactures (UNVERIFIED destination split)",
        "investment_type": "trade_flow",
        "value": "29979350",
        "currency": "USD",
        "value_usd": "29979350",
        "fx_usd": "1",
        "fx_date": "2025-12-31",
        "year": "2025",
        "status": "active",
        "lat": "-2.17",
        "lon": "-79.9",
        "geo_note": "Ecuador coastal balsa manufacturing/export hub proxy (Guayas/Los Ríos corridor).",
        "evidence": "proxy",
        "source_id": "magap_aima_balsa_2025",
        "note": "Paired with aima_ecuador_balsa_mfr_china_2025. US 9.95% share from Forbes Ecuador citing AIMA (UNVERIFIED) applied to MAGAP/AIMA total. Distinct from wits_ecuador_balsa_us_2022–2024.",
    },
    {
        "id": "aima_ecuador_balsa_mfr_us_2025",
        "retrieved": "2026-10-01",
        "source_id": "magap_aima_balsa_2025",
        "url": "https://www.agricultura.gob.ec/ecuador-fortalece-la-cadena-de-balsa-para-proteger-su-acceso-a-mercados-internacionales/",
        "price_year": "2025",
        "evidence": "proxy",
        "quote": "en 2025, las exportaciones mundiales de manufacturas de balsa alcanzaron USD 301,3 millones, un 38% más que en 2024, de acuerdo a información proporcionada por AIMA",
        "note": "Opened MAGAP official Spanish page. Destination US share from Forbes Ecuador (secondary) applied as proxy.",
    },
    {
        "id": "forbes_ecuador_balsa_dest_2025",
        "type": "press",
        "chicago": "Forbes Ecuador. “La balsa ecuatoriana conquista la industria eólica mundial.” 2026.",
        "url": "https://www.forbes.com.ec/negocios/la-balsa-ecuatoriana-conquista-industria-eolica-mundial-n90920",
        "annotation": "Secondary press citing AIMA destination shares (China 72.51%, US 9.95%) for 2025 balsa manufactures. Supports proxy destination splits on aima_ecuador_balsa_mfr_*_2025.",
        "supports": [
            "aima_ecuador_balsa_mfr_china_2025",
            "aima_ecuador_balsa_mfr_us_2025",
            "hunt_res_balsa",
        ],
    },
)

# 4 resources/nickel — miss (Atlantic Santa Rita UG already logged)
# 5 energy/wind — miss
# 6 energy/power_plants_grid — miss
# 7 resources/graphite — miss
# 8 infrastructure/bridges_roads — miss
# 9 energy/fission_smr — miss
# 10 energy/solar — miss
# 11 infrastructure/building_materials — miss
# 12 infrastructure/rail — miss
# 13 resources/copper — miss

# 14 resources/lithium — Lanshen / Argentina Lithium Rincon West framework
A(
    {
        "id": "lanshen_argentina_lithium_rincon_west_2026",
        "layer": "resources",
        "subcategory": "lithium",
        "side": "prc",
        "counterpart": "Xi’an Lanshen — non-binding framework for up to USD 100m earn-in at Rincon West (Salta)",
        "country": "Argentina",
        "asset": "Non-binding Heads of Terms / Framework Agreement (21 Apr 2026): Lanshen proposed earn-in up to 30% of ALESA via staged contributions totaling ~USD 100 million (Stage 3 ~USD 95.9m turnkey DLE/Li2CO3 plant EPC-supply for 5,000 tpy battery-grade carbonate); replaces Dec 2025 MOU; subject to definitive agreements, TSXV, Chinese export approvals, Stellantis consents",
        "investment_type": "technology_mou",
        "value": "100000000",
        "currency": "USD",
        "value_usd": "100000000",
        "fx_usd": "1",
        "fx_date": "2026-04-21",
        "year": "2026",
        "status": "active",
        "lat": "-24.2",
        "lon": "-66.9",
        "geo_note": "Rincon West lithium brine project, Salta Province (company release; adjacent Rio Tinto Rincon).",
        "evidence": "documented",
        "source_id": "argentina_lithium_lanshen_20260421",
        "note": "Actor: Xi’an Lanshen New Material Technology (PRC) — prc; counterpart Argentina Lithium (Canadian) / ALESA with Stellantis 19.9%. Company PDF 21 Apr 2026. Non-binding except confidentiality — proposed transaction USD entered as stated ceiling. Distinct from Rio Tinto Rincon / Ganfeng PPG / CUH Arizaro lithium rows.",
    },
    {
        "id": "lanshen_argentina_lithium_rincon_west_2026",
        "retrieved": "2026-10-01",
        "source_id": "argentina_lithium_lanshen_20260421",
        "url": "https://argentinalithium.com/site/assets/files/6705/2026-04-21-lit-lanshen-framework-agrmt-v7-final.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Lanshen be granted the right to earn up to a 30% equity interest in … ALESA, through staged contributions totaling up to approximately US$100 million … Lanshen is expected to contribute approximately US$95.9 million … 5,000 tonnes per year of battery-grade lithium carbonate",
        "note": "Opened Argentina Lithium company PDF Newsfile 21 Apr 2026.",
    },
    {
        "id": "argentina_lithium_lanshen_20260421",
        "type": "company",
        "chicago": "Argentina Lithium & Energy Corp. “Argentina Lithium Signs US$100 Million Heads of Terms and Framework Agreement with Lanshen for Rincon West.” 21 April 2026.",
        "url": "https://argentinalithium.com/site/assets/files/6705/2026-04-21-lit-lanshen-framework-agrmt-v7-final.pdf",
        "annotation": "Company primary on non-binding Lanshen up-to-USD 100m Rincon West DLE framework. Supports lanshen_argentina_lithium_rincon_west_2026.",
        "supports": ["lanshen_argentina_lithium_rincon_west_2026", "hunt_res_lithium"],
    },
)

# 15 infrastructure/port_ownership — miss

# 16 resources/niobium — St George Araxá permitting kickoff
A(
    {
        "id": "st_george_araxa_permitting_2026",
        "layer": "resources",
        "subcategory": "niobium",
        "side": "allied",
        "counterpart": "St George Mining — Araxá Nb-REE mine permitting commenced (Minas Gerais)",
        "country": "Brazil",
        "asset": "ASX 25 Aug 2026: licensing commenced toward LP/LI/LO pathway with FEAM/COPAM for Araxá niobium–REE mine development; company expects LP+LI within ~12 months; LO targeted 2H 2029 subject to conditions and FID; greenfields development timeline",
        "investment_type": "permitting",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-19.59",
        "lon": "-46.94",
        "geo_note": "Araxá Project, Minas Gerais (St George ASX).",
        "evidence": "documented",
        "source_id": "sgq_araxa_permitting_20260825",
        "note": "Actor: St George Mining (Australian ASX:SGQ) — allied. Official ASX PDF 25 Aug 2026. Pre-FID permitting milestone — no CAPEX USD on page (press R$2–3bn / US$350m estimates not entered). Distinct from st_george_araxa_nb_2025 acquisition and worley_st_george_araxa_2026 advisory.",
    },
    {
        "id": "st_george_araxa_permitting_2026",
        "retrieved": "2026-10-01",
        "source_id": "sgq_araxa_permitting_20260825",
        "url": "https://announcements.asx.com.au/asxpdf/20260825/pdf/0735mpdwg5tccv.pdf",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "PERMITTING KICKS OFF FOR RARE EARTHS AND NIOBIUM MINE DEVELOPMENT AT ARAXÁ PROJECT … Licensing commences for Araxá",
        "note": "Opened St George ASX announcement PDF 25 Aug 2026.",
    },
    {
        "id": "sgq_araxa_permitting_20260825",
        "type": "company",
        "chicago": "St George Mining Limited. “Permitting Kicks Off for Rare Earths and Niobium Mine Development at Araxá Project.” ASX announcement, 25 August 2026.",
        "url": "https://announcements.asx.com.au/asxpdf/20260825/pdf/0735mpdwg5tccv.pdf",
        "annotation": "ASX primary on Araxá Nb-REE permitting commencement. Supports st_george_araxa_permitting_2026.",
        "supports": ["st_george_araxa_permitting_2026", "hunt_fenb_araxa"],
    },
)

# 17 infrastructure/port_cranes — ZPMC STS at Puerto Aguadulce (Colombia)
A(
    {
        "id": "zpmc_aguadulce_sts_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "prc",
        "counterpart": "ZPMC — two super post-Panamax STS quay cranes delivered to SPIA Puerto Aguadulce",
        "country": "Colombia",
        "asset": "Delivery of two ZPMC super post-Panamax quay cranes (outreach up to 24 rows; 65 t twin-lift / 80 t heavy-lift) plus three hybrid RTGs to Sociedad Puerto Industrial de Aguadulce (SPIA; ICTSI–PSA JV) at Buenaventura; largest quay cranes in Colombia per operator",
        "investment_type": "equipment_supply",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "3.89",
        "lon": "-77.08",
        "geo_note": "Puerto Aguadulce / Buenaventura, Valle del Cauca (ICTSI release).",
        "evidence": "documented",
        "source_id": "ictsi_aguadulce_zpmc_20260204",
        "note": "Actor: ZPMC (PRC) equipment — prc; terminal SPIA (ICTSI Philippines / PSA Singapore JV) — allied operator counterpart. Company ICTSI 4 Feb 2026. No crane contract USD on page. Distinct from ZPMC Santos / MultiRio / CMSA Manzanillo crane rows.",
    },
    {
        "id": "zpmc_aguadulce_sts_2026",
        "retrieved": "2026-10-01",
        "source_id": "ictsi_aguadulce_zpmc_20260204",
        "url": "https://ictsi.com/press-releases/puerto-aguadulce-enhances-capacity-efficiency-new-equipment",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The quay cranes, manufactured by Shanghai Zhenhua Heavy Industries Co. Ltd. (ZPMC), are the largest in the country … outreach of up to 24 rows across … 65 tons in twin-lift mode and up to 80 tons in heavy-lift mode",
        "note": "Opened ICTSI company English press release 4 Feb 2026.",
    },
    {
        "id": "ictsi_aguadulce_zpmc_20260204",
        "type": "company",
        "chicago": "International Container Terminal Services, Inc. “Puerto Aguadulce enhances capacity, efficiency with new equipment.” 4 February 2026.",
        "url": "https://ictsi.com/press-releases/puerto-aguadulce-enhances-capacity-efficiency-new-equipment",
        "annotation": "Company primary on ZPMC super post-Panamax STS delivery to Aguadulce. Supports zpmc_aguadulce_sts_2026.",
        "supports": ["zpmc_aguadulce_sts_2026", "hunt_infra_port_cranes"],
    },
)

# 18 energy/other_renewables — Acciona Malgarida 1 GWh BESS (CATL supply UNVERIFIED)
A(
    {
        "id": "acciona_malgarida_bess_1gwh_2026",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "allied",
        "counterpart": "ACCIONA Energía — 200 MW / 1 GWh BESS at Malgarida PV complex (Atacama)",
        "country": "Chile",
        "asset": "Company-announced construction of 200 MW / 1 GWh battery energy storage at Malgarida photovoltaic complex (238 MWp); commissioning targeted early 2027; part of Chile storage pipeline totaling 1.5 GWh linked to Acciona PV plants; trade press attributes supply to CATL Tener Stack (UNVERIFIED — not named on opened Acciona page)",
        "investment_type": "bess",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-27.4",
        "lon": "-70.3",
        "geo_note": "Malgarida PV complex, Atacama Desert (Acciona release).",
        "evidence": "documented",
        "source_id": "acciona_malgarida_bess_2026",
        "note": "Actor: ACCIONA Energía (Spanish) — allied developer/owner of BESS. Company English release. CAPEX blank (not stated). CATL Tener Stack supply reported by ESS-News only — not entered as PRC-side row without Acciona confirmation. Distinct from BYD/Grenergy / Trina Atlas / Tesla Colbún BESS rows.",
    },
    {
        "id": "acciona_malgarida_bess_1gwh_2026",
        "retrieved": "2026-10-01",
        "source_id": "acciona_malgarida_bess_2026",
        "url": "https://www.acciona.com/updates/news/acciona-energia-install-battery-atacama-desert",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "construction of a 1 GWh battery energy storage system (BESS) at Malgarida photovoltaic complex (238MWp) … capacity of 200MW/1GWh … commissioning expected in early 2027",
        "note": "Opened Acciona Energía company English news page.",
    },
    {
        "id": "acciona_malgarida_bess_2026",
        "type": "company",
        "chicago": "ACCIONA Energía. “ACCIONA Energía to install a 1GWh battery in the Atacama desert.” 2026.",
        "url": "https://www.acciona.com/updates/news/acciona-energia-install-battery-atacama-desert",
        "annotation": "Company primary on Malgarida 200MW/1GWh BESS. Supports acciona_malgarida_bess_1gwh_2026.",
        "supports": ["acciona_malgarida_bess_1gwh_2026", "hunt_energy_other_renewables"],
    },
)


def main():
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    bib_by = {b["id"]: i for i, b in enumerate(bib)}
    added = []

    for row, evidence, bib_entry in ITEMS:
        rid = row["id"]
        full = {k: "" for k in FIELDS}
        full.update(row)
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

    # Also register Forbes bib (used by US balsa row evidence chain)
    # already added via second A() call

    hunt_updates = {
        "hunt_infra_engineering_epc": "Cycle 28: equal budget; Bechtel–EIMISA already logged (miss).",
        "hunt_res_water": "Cycle 28: equal budget; Rosarito / Collahuasi / Sacyr / Ilopango already logged (miss).",
        "hunt_res_balsa": "Cycle 28: logged aima_ecuador_balsa_mfr_china_2025 and aima_ecuador_balsa_mfr_us_2025.",
        "hunt_res_nickel": "Cycle 28: equal budget; Atlantic Santa Rita UG already logged (miss).",
        "hunt_energy_wind": "Cycle 28: equal budget; CTG Serra / Goldwind / Vestas set already logged (miss).",
        "hunt_br_power_equip": "Cycle 28: equal budget; Coca Codo / Parinas / thick grid set already logged (miss).",
        "hunt_res_graphite": "Cycle 28: equal budget; Graph+ / Graphcoa / South Star set already logged (miss).",
        "hunt_infra_bridges_roads": "Cycle 28: equal budget; Quinto Puente / Salvador–Itaparica / OHLA already logged (miss).",
        "hunt_energy_fission_smr": "Cycle 28: equal budget; CDPNB GT / Meitner / CAREM set already logged (miss).",
        "hunt_energy_solar": "Cycle 28: equal budget; PowerChina Francisco Juana without company primary; Hanersun already logged (miss).",
        "hunt_infra_building_materials": "Cycle 28: equal budget; Votorantim Nobres / Xambioá already logged (miss).",
        "hunt_latam_rail_telecom": "Cycle 28: equal budget; CRCC Batuco logged C27 (miss).",
        "hunt_res_copper": "Cycle 28: equal budget; Cerro Verde MEIA-2 logged C27 (miss).",
        "hunt_res_lithium": "Cycle 28: logged lanshen_argentina_lithium_rincon_west_2026.",
        "hunt_infra_port_ownership": "Cycle 28: equal budget; Matarani / Callao / Caldera set already logged (miss).",
        "hunt_fenb_araxa": "Cycle 28: logged st_george_araxa_permitting_2026.",
        "hunt_infra_port_cranes": "Cycle 28: logged zpmc_aguadulce_sts_2026.",
        "hunt_energy_other_renewables": "Cycle 28: logged acciona_malgarida_bess_1gwh_2026.",
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
    print("Cycle 28 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
