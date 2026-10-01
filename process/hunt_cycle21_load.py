#!/usr/bin/env python3
"""Cycle 21 hunt: shuffle_seed=20261021; equal budget across 18 subcategories."""
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


# seed 20261021 order (canonical BRIEF list):
# building_materials, rail, copper, power_plants_grid, port_cranes, wind, nickel,
# fission_smr, lithium, bridges_roads, balsa, graphite, engineering_epc, solar,
# niobium, port_ownership, water, other_renewables

# 1 infrastructure/building_materials — miss (CSN Cimentos sale not closed)
# 2 infrastructure/rail — miss (Alstom Mexico / SP Line 4 / Salvador CRRC already logged)
# 3 resources/copper — miss (Vicuña RIGI / El Abra EIS already logged)
# 4 energy/power_plants_grid — miss (thick)
# 5 infrastructure/port_cranes — miss (OPC Cortés names RTG/quay buys but OEM unnamed)
# 6 energy/wind — miss (Sento Sé / Esquina do Vento already logged)
# 7 resources/nickel — miss
# 8 energy/fission_smr — miss
# 9 resources/lithium — miss (Ganfeng convertible / Rincon financing already logged)

# 10 infrastructure/bridges_roads — Salvador–Itaparica PPP (CCECC / CCCC)
A(
    {
        "id": "ccecc_cccc_salvador_itaparica_2025",
        "layer": "infrastructure",
        "subcategory": "bridges_roads",
        "side": "prc",
        "counterpart": "Concessionária Ponte Salvador–Itaparica (CCECC / CCCC) — Sistema Rodoviário Ponte Salvador–Ilha de Itaparica PPP",
        "country": "Brazil",
        "asset": "Sponsored PPP for 12.4 km cross-bay bridge + Salvador/Itaparica road accesses and BA-001 duplication; 1º Termo Aditivo 4 Jun 2025 resets works clock (foundations targeted from Jun 2026; completion Jun 2031); 35-year concession (works ~6 years + O&M ~29 years)",
        "investment_type": "ppp_concession",
        "value": "",
        "currency": "BRL",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-12.95",
        "lon": "-38.55",
        "geo_note": "Baía de Todos os Santos crossing Salvador–Vera Cruz / Itaparica (Bahia state project page).",
        "evidence": "documented",
        "source_id": "ba_gov_ponte_salvador_itaparica_2026",
        "note": "Actors: China Civil Engineering Construction Corporation (CCECC) and China Communications Construction Company (CCCC) — prc. Primary: Bahia state project page naming Chinese concessionaire; SEFAZ PPP page corroborates Contrato nº 001/2020 and 1º Termo Aditivo 04/06/2025. Contractual NPV figures on SEFAZ page are payment-stream estimates (jan/2019 base) — CAPEX left blank. Distinct from CCECC Quinto Puente Ecuador / CRBC Arequipa rows.",
    },
    {
        "id": "ccecc_cccc_salvador_itaparica_2025",
        "retrieved": "2026-10-01",
        "source_id": "ba_gov_ponte_salvador_itaparica_2026",
        "url": "https://www.ba.gov.br/pontesalvadoritaparica/projeto",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "O projeto é executado por meio de uma Parceria Público-Privada (PPP) entre o Governo do Estado da Bahia e a Concessionária Ponte Salvador–Itaparica (CPSI), formada por dois dos maiores grupos chineses de engenharia do mundo: China Civil Engineering Construction Corporation (CCECC) e China Communications Construction Company (CCCC).",
        "note": "Opened Bahia state official project page. Termo Aditivo / schedule corroborated via SEFAZ PPP page.",
    },
    {
        "id": "ba_gov_ponte_salvador_itaparica_2026",
        "type": "government",
        "chicago": "Bahia. Governo do Estado. “Projeto | Ponte Salvador Itaparica.” Portal Oficial, updated 29 April 2026.",
        "url": "https://www.ba.gov.br/pontesalvadoritaparica/projeto",
        "annotation": "Official Bahia project page naming CCECC/CCCC concessionaire for Salvador–Itaparica PPP. Supports ccecc_cccc_salvador_itaparica_2025.",
        "supports": ["ccecc_cccc_salvador_itaparica_2025", "hunt_infra_bridges_roads"],
    },
)

# 11 resources/balsa — miss
# 12 resources/graphite — miss

# 13 infrastructure/engineering_epc — STRACON Pérez Caldera BOOM / USD 376m financing
A(
    {
        "id": "stracon_perez_caldera_boom_2026",
        "layer": "infrastructure",
        "subcategory": "engineering_epc",
        "side": "allied",
        "counterpart": "STRACON Group Holding — Pérez Caldera tailings infrastructure BOOM (Los Bronces / Anglo American Sur)",
        "country": "Chile",
        "asset": "Integrated engineering, construction, financing and long-term O&M (BOOM) for dedicated Pérez Caldera Tailings Dam removal/conditioning/transport infrastructure at Anglo American Los Bronces (Lo Barnechea); closed up to USD 376 million non-recourse project financing (up to USD 345m term loans + USD 31m DSR LCs) arranged by Natixis/SMBC/BCI",
        "investment_type": "epc_boom_financing",
        "value": "376000000",
        "currency": "USD",
        "value_usd": "376000000",
        "fx_usd": "1",
        "fx_date": "2026-04-01",
        "year": "2026",
        "status": "active",
        "lat": "-33.15",
        "lon": "-70.27",
        "geo_note": "Pérez Caldera / Los Bronces, Lo Barnechea district, Santiago Metropolitan Region (STRACON release).",
        "evidence": "documented",
        "source_id": "stracon_perez_caldera_financing_20260401",
        "note": "Actor: STRACON Group Holding (Toronto TSX:STG / BVL:STG; Canadian HQ) — allied. Awarded Dec 2025 by Anglo American Sur; financing close 1 Apr 2026. Non-grid mining infrastructure EPC/BOOM (not power_plants_grid). Distinct from Bechtel Los Pelambres / Fluor Toromocho / Worley Araxá EPC rows.",
    },
    {
        "id": "stracon_perez_caldera_boom_2026",
        "retrieved": "2026-10-01",
        "source_id": "stracon_perez_caldera_financing_20260401",
        "url": "https://www.newsfilecorp.com/release/290819/STRACON-Group-Holding-Inc.-Announces-Closing-of-US376-Million-NonRecourse-Project-Financing-for-Prez-Caldera-Infrastructure-Project",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "STRACON Group Holding Inc. … today announced the closing of up to US$376 million in non-recourse project financing for the Pérez Caldera infrastructure project in Chile. The financing … will fund the development, construction, ownership, operation and maintenance of dedicated tailings infrastructure at Anglo American's Los Bronces copper operation in Chile.",
        "note": "Opened Newsfile company release 1 Apr 2026 (STRACON). Award context corroborated via STRACON 31 Dec 2025 award PDF.",
    },
    {
        "id": "stracon_perez_caldera_financing_20260401",
        "type": "company",
        "chicago": "STRACON Group Holding Inc. “STRACON Group Holding Inc. Announces Closing of US$376 Million Non-Recourse Project Financing for Pérez Caldera Infrastructure Project.” Newsfile, 1 April 2026.",
        "url": "https://www.newsfilecorp.com/release/290819/STRACON-Group-Holding-Inc.-Announces-Closing-of-US376-Million-NonRecourse-Project-Financing-for-Prez-Caldera-Infrastructure-Project",
        "annotation": "Company primary on Pérez Caldera BOOM financing close. Supports stracon_perez_caldera_boom_2026.",
        "supports": ["stracon_perez_caldera_boom_2026", "hunt_infra_engineering_epc"],
    },
)

# 14 energy/solar — miss (JA Solar Exel 400MW press-only; company page blocked)
# 15 resources/niobium — miss (St George Araxá logged C18)

# 16 infrastructure/port_ownership — ICTSI OPC Puerto Cortés USD 100m expansion
A(
    {
        "id": "ictsi_opc_cortes_100m_2026",
        "layer": "infrastructure",
        "subcategory": "port_ownership",
        "side": "other",
        "counterpart": "Operadora Portuaria Centroamericana (ICTSI) — Puerto Cortés specialized container/general cargo terminal expansion",
        "country": "Honduras",
        "asset": "USD 100 million 2026 expansion: Yard 6 +9 ha; acquisition of 12 hybrid RTGs + two new quay cranes; projected capacity 1.4 million TEU/year by March 2027 (concession since 2013)",
        "investment_type": "concession_capex",
        "value": "100000000",
        "currency": "USD",
        "value_usd": "100000000",
        "fx_usd": "1",
        "fx_date": "2026-02-27",
        "year": "2026",
        "status": "active",
        "lat": "15.84",
        "lon": "-87.94",
        "geo_note": "Puerto Cortés, Cortés Department, Honduras (ICTSI company release).",
        "evidence": "documented",
        "source_id": "ictsi_opc_cortes_20260227",
        "note": "Actor: ICTSI (Philippine independent) via OPC — other (same coding as ictsi_rio_brasil_expansion_2025). Company 27 Feb 2026 release. Crane OEM unnamed on opened page — port_cranes miss; ownership/capex row only. Distinct from ICTSI Rio Brasil / CMSA Manzanillo rows. Caribbean/Central America LatAm geography.",
    },
    {
        "id": "ictsi_opc_cortes_100m_2026",
        "retrieved": "2026-10-01",
        "source_id": "ictsi_opc_cortes_20260227",
        "url": "https://www.ictsi.com/news/opc-invest-usd100-million-puerto-cortes-expansion",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Operadora Portuaria Centroamericana, International Container Terminal Services, Inc.’s (ICTSI) Honduran subsidiary, is investing USD100 million in 2026 for the expansion of the specialized container and general cargo terminal in Puerto Cortés. … It includes the extension of Yard 6 through the development of an additional 9-hectare area and the acquisition of 12 hybrid rubber-tired gantry cranes along with two new quay cranes.",
        "note": "Opened ICTSI company news 27 Feb 2026.",
    },
    {
        "id": "ictsi_opc_cortes_20260227",
        "type": "company",
        "chicago": "International Container Terminal Services, Inc. “OPC to invest USD100 million in Puerto Cortés expansion.” 27 February 2026.",
        "url": "https://www.ictsi.com/news/opc-invest-usd100-million-puerto-cortes-expansion",
        "annotation": "Company primary on ICTSI/OPC Puerto Cortés 2026 expansion. Supports ictsi_opc_cortes_100m_2026.",
        "supports": ["ictsi_opc_cortes_100m_2026", "hunt_infra_port_ownership"],
    },
)

# 17 resources/water — Veolia O&M Aguas Pacífico Valparaíso desal
A(
    {
        "id": "veolia_aguas_pacifico_om_2025",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Veolia — O&M of Aguas Pacífico multipurpose desalination plant (Valparaíso / Puchuncaví)",
        "country": "Chile",
        "asset": "Operation & maintenance contract for Chile’s first municipal/industrial multipurpose desal plant (1,000 L/s) + 105 km aqueduct/pumping system; initial term up to 4 years with renewal clauses through 2040; commissioning support then O&M once at regime",
        "investment_type": "om_contract",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2025",
        "status": "active",
        "lat": "-32.73",
        "lon": "-71.41",
        "geo_note": "Desal plant commune of Puchuncaví, Valparaíso Region (Veolia / Aguas Pacífico releases).",
        "evidence": "documented",
        "source_id": "veolia_aguas_pacifico_20251021",
        "note": "Actor: Veolia (French) — allied; project owner Aguas Pacífico (Patria Investments). Company press 21 Oct 2025. O&M contract USD not disclosed on opened page — value blank. Plant investment ~USD 1.2bn cited as Aguas Pacífico project finance context, not Veolia contract value. Distinct from Acciona/Sacyr/IDE/GS Inima desal EPC/ownership rows.",
    },
    {
        "id": "veolia_aguas_pacifico_om_2025",
        "retrieved": "2026-10-01",
        "source_id": "veolia_aguas_pacifico_20251021",
        "url": "https://www.veolia.com/en/our-media/press-releases/veolia-will-manage-first-municipal-and-industrial-desalination-plant-chile",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "Veolia was awarded the Operation and Maintenance (O&M) contract for the Aguas Pacífico multipurpose desalination plant in Valparaíso, the first in Chile (1,000 L/s) … The contract has an initial duration of four years and includes renewal clauses through 2040, covering both the operation and maintenance of the desalination plant and the 105 km pumping system.",
        "note": "Opened Veolia Group English press release 21 Oct 2025.",
    },
    {
        "id": "veolia_aguas_pacifico_20251021",
        "type": "company",
        "chicago": "Veolia. “Veolia will manage the first municipal and industrial desalination plant of Chile in Valparaíso.” Press release, 21 October 2025.",
        "url": "https://www.veolia.com/en/our-media/press-releases/veolia-will-manage-first-municipal-and-industrial-desalination-plant-chile",
        "annotation": "Company primary on Veolia O&M award for Aguas Pacífico desal. Supports veolia_aguas_pacifico_om_2025.",
        "supports": ["veolia_aguas_pacifico_om_2025", "hunt_res_water"],
    },
)

# 18 energy/other_renewables — Tesla Megapack Colbún Celda Solar BESS
A(
    {
        "id": "tesla_colbun_celda_solar_2024",
        "layer": "energy",
        "subcategory": "other_renewables",
        "side": "us",
        "counterpart": "Tesla — Megapack BESS supply for Colbún Celda Solar (Camarones, Arica y Parinacota)",
        "country": "Chile",
        "asset": "Supply agreement for Tesla Megapack battery system totaling 228 MW / 912 MWh (>200 units) for Colbún’s first large-scale standalone BESS; Colbún states total project investment USD 260 million; COD targeted mid-2026",
        "investment_type": "equipment_supply",
        "value": "260000000",
        "currency": "USD",
        "value_usd": "260000000",
        "fx_usd": "1",
        "fx_date": "2024-12-18",
        "year": "2024",
        "status": "active",
        "lat": "-18.95",
        "lon": "-69.85",
        "geo_note": "Camarones commune / Valle de Chaca area, Arica y Parinacota Region (Colbún release; approximate).",
        "evidence": "documented",
        "source_id": "colbun_tesla_celda_solar_20241218",
        "note": "Actor: Tesla (U.S.) — us equipment supplier; developer Colbún (Chilean). Colbún company 18 Dec 2024 press: Megapack 228 MW / 912 MWh; USD 260m is stated total project investment (includes substation/line), not a separately disclosed Tesla equipment invoice. Coded other_renewables for grid-scale BESS (not pure solar/wind OEM). Distinct from AES Andes Pampas/Cristales hybrid package.",
    },
    {
        "id": "tesla_colbun_celda_solar_2024",
        "retrieved": "2026-10-01",
        "source_id": "colbun_tesla_celda_solar_20241218",
        "url": "https://www.colbun.cl/corporativo/sala-de-prensa/noticias-y-comunicados/detalle/2024/12/18/colbun-y-tesla-firman-contrato-para-suministro-de-baterias-por-228-mw-para-proyecto-celda-solar-en-camarones",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Colbún y el fabricante de baterías y autos eléctricos Tesla anunciaron hoy un acuerdo mediante el cual la compañía estadounidense suministrará un sistema de baterías Megapacks por 228 MW de potencia y 912 MWh de energía diaria para el proyecto Celda Solar … Celda Solar es un proyecto de almacenamiento de energía que demandará una inversión total de US$260 millones",
        "note": "Opened Colbún Spanish company press 18 Dec 2024.",
    },
    {
        "id": "colbun_tesla_celda_solar_20241218",
        "type": "company",
        "chicago": "Colbún. “Colbún y Tesla firman contrato para suministro de baterías por 228 MW para proyecto Celda Solar en Camarones.” 18 December 2024.",
        "url": "https://www.colbun.cl/corporativo/sala-de-prensa/noticias-y-comunicados/detalle/2024/12/18/colbun-y-tesla-firman-contrato-para-suministro-de-baterias-por-228-mw-para-proyecto-celda-solar-en-camarones",
        "annotation": "Company primary on Tesla Megapack supply for Celda Solar BESS. Supports tesla_colbun_celda_solar_2024.",
        "supports": ["tesla_colbun_celda_solar_2024", "hunt_energy_other_renewables"],
    },
)


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
        "hunt_infra_building_materials": "Cycle 21: equal budget; CSN Cimentos sale still not closed — Huaxin/Votorantim/Polimix bids open (miss).",
        "hunt_latam_rail_telecom": "Cycle 21: equal budget; Alstom Mexico DMU / SP Line 4 Siemens / Salvador CRRC already logged (miss).",
        "hunt_res_copper": "Cycle 21: equal budget; Vicuña RIGI C20 / El Abra EIS already logged (miss).",
        "hunt_br_power_equip": "Cycle 21: equal budget; thick power_plants_grid — miss.",
        "hunt_infra_port_cranes": "Cycle 21: equal budget; OPC Cortés expansion names RTG/quay buys but OEM unnamed (miss).",
        "hunt_energy_wind": "Cycle 21: equal budget; Goldwind Sento Sé / Vestas Esquina already logged (miss).",
        "hunt_res_nickel": "Cycle 21: equal budget; MMG/Anglo / Jervois / Atlantic / Centaurus set already logged (miss).",
        "hunt_energy_fission_smr": "Cycle 21: equal budget; Meitner/CAREM/Nuclearis/Brazil microreactor already logged (miss).",
        "hunt_res_lithium": "Cycle 21: equal budget; Ganfeng convertible / Rincon financing already logged (miss).",
        "hunt_infra_bridges_roads": "Cycle 21: logged ccecc_cccc_salvador_itaparica_2025.",
        "hunt_res_balsa": "Cycle 21: equal budget; no new named exporter/importer stake beyond WITS trade years (miss).",
        "hunt_res_graphite": "Cycle 21: equal budget; South Star / Graphcoa / Urbix set already logged (miss).",
        "hunt_infra_engineering_epc": "Cycle 21: logged stracon_perez_caldera_boom_2026.",
        "hunt_energy_solar": "Cycle 21: equal budget; JA Solar Exel 400MW press-only / company page blocked (miss).",
        "hunt_fenb_araxa": "Cycle 21: equal budget; St George Araxá logged C18 (miss).",
        "hunt_infra_port_ownership": "Cycle 21: logged ictsi_opc_cortes_100m_2026.",
        "hunt_res_water": "Cycle 21: logged veolia_aguas_pacifico_om_2025.",
        "hunt_energy_other_renewables": "Cycle 21: logged tesla_colbun_celda_solar_2024.",
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
    print("Cycle 21 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
