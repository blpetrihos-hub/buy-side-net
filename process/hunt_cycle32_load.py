#!/usr/bin/env python3
"""Cycle 32 hunt: shuffle_seed=20261032; equal budget across 18 subcategories."""
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


# seed 20261032 order:
# copper, building_materials, wind, water, port_cranes, fission_smr, solar,
# engineering_epc, other_renewables, port_ownership, graphite, lithium,
# power_plants_grid, balsa, nickel, bridges_roads, rail, niobium

# 1 resources/copper — Antofagasta Centinela Second Concentrator
A(
    {
        "id": "antofagasta_centinela_2nd_conc_2023",
        "layer": "resources",
        "subcategory": "copper",
        "side": "allied",
        "counterpart": "Antofagasta (70%) / Marubeni (30%) — Centinela Second Concentrator",
        "country": "Chile",
        "asset": "20 Dec 2023 Antofagasta board approval of Centinela Second Concentrator: project cost USD 4.4 billion (95 ktpd concentrator with HPGR, seawater system expansion, new TSF, power/logistics/port upgrades, Esperanza Sur mine fleet/autonomy). +~170 ktpa CuEq (~144 ktpa Cu + Au/Mo by-products) over first 10 years; first copper 2027; 36-year mine life on ~2 Bt reserve. Mar 2024: USD 2.5bn project finance closed (JBIC, EDC, KEXIM + commercial banks). Water system later outsourced to Almar/Transelec (separate water row), reducing concentrator project CAPEX by ~USD 380m",
        "investment_type": "brownfield_expansion",
        "value": "4400000000",
        "currency": "USD",
        "value_usd": "4400000000",
        "fx_usd": "1",
        "fx_date": "2023-12-20",
        "year": "2023",
        "status": "active",
        "lat": "-22.1",
        "lon": "-69.1",
        "geo_note": "Centinela district, Antofagasta Region (company geography; approximate pin).",
        "evidence": "documented",
        "source_id": "anto_centinela_approval_20231220",
        "note": "Actors: Antofagasta plc (UK) 70% + Marubeni (Japan) 30% — allied. Company English approval release 20 Dec 2023 stating USD 4.4bn. Distinct from bhp_escondida_new_concentrator_2026 and fcx_el_abra_mill_chile_2026.",
    },
    {
        "id": "antofagasta_centinela_2nd_conc_2023",
        "retrieved": "2026-10-01",
        "source_id": "anto_centinela_approval_20231220",
        "url": "https://www.antofagasta.co.uk/investors/news/2023/centinela-second-concentrator-project-approved-for-development/",
        "price_year": "2023",
        "evidence": "documented",
        "quote": "Capital investment: Project cost of $4.4 billion, including a new 95ktpd concentrator plant incorporating high pressure grinding rolls (“HPGRs”) …",
        "note": "Opened Antofagasta plc English approval release 20 Dec 2023. Financing corroboration: 2024 USD 2.5bn facility release.",
    },
    {
        "id": "anto_centinela_approval_20231220",
        "type": "company",
        "chicago": "Antofagasta plc. “Centinela Second Concentrator Project Approved For Development.” 20 December 2023.",
        "url": "https://www.antofagasta.co.uk/investors/news/2023/centinela-second-concentrator-project-approved-for-development/",
        "annotation": "Company primary approving Centinela Second Concentrator at USD 4.4bn. Supports antofagasta_centinela_2nd_conc_2023.",
        "supports": ["antofagasta_centinela_2nd_conc_2023", "hunt_res_copper"],
    },
)

# 2 infrastructure/building_materials — UNACEM / Calidra CALCEM lime plant
A(
    {
        "id": "unacem_calcem_lime_peru_2025",
        "layer": "infrastructure",
        "subcategory": "building_materials",
        "side": "other",
        "counterpart": "UNACEM / Grupo Calidra — CALCEM quicklime plant (Condorcocha)",
        "country": "Peru",
        "asset": "20 Aug 2025: Grupo UNACEM and Mexico’s Grupo Calidra form CALCEM S.A. and begin construction of a quicklime / calcium-carbonate plant adjacent to UNACEM Condorcocha cement works (Tarma, Junín); initial capacity 200,000 tpa; investment USD 70 million; ops targeted Jun 2027. IDB Invest signed 15 Dec 2025 long-term loan up to USD 50 million for plant construction/commissioning (project 15037-01)",
        "investment_type": "greenfield",
        "value": "70000000",
        "currency": "USD",
        "value_usd": "70000000",
        "fx_usd": "1",
        "fx_date": "2025-08-20",
        "year": "2025",
        "status": "active",
        "lat": "-11.4",
        "lon": "-75.7",
        "geo_note": "Condorcocha industrial complex, Tarma Province, Junín (UNACEM/IDB Invest geography; approximate pin).",
        "evidence": "documented",
        "source_id": "unacem_calcem_20250820",
        "note": "Actors: UNACEM (Peru) + Calidra (Mexico) JV — other (LatAm corporates); IDB Invest loan noted as allied IFI financing corroboration. Company English release 20 Aug 2025. Distinct from holcim_pacasmayo / holcim_cemex_colombia / holcim_guayaquil rows.",
    },
    {
        "id": "unacem_calcem_lime_peru_2025",
        "retrieved": "2026-10-01",
        "source_id": "unacem_calcem_20250820",
        "url": "https://grupounacem.com/en/noticias/grupo-unacem-and-grupo-calidra-begin-construction-of-a-lime-plant-with-an-initial-capacity-of-200000-tons-per-year-and-an-investment-of-us70-million/",
        "price_year": "2025",
        "evidence": "documented",
        "quote": "For Grupo UNACEM, the initial project, with a capacity of 200,000 tons per year and an investment of US$70 million, represents a strategic diversification decision …",
        "note": "Opened Grupo UNACEM English company release 20 Aug 2025. IDB Invest project page corroborates up to USD 50m loan signed 15 Dec 2025.",
    },
    {
        "id": "unacem_calcem_20250820",
        "type": "company",
        "chicago": "Grupo UNACEM. “Grupo UNACEM and Grupo Calidra begin construction of a lime plant with an initial capacity of 200,000 tons per year and an investment of US$70 million.” 20 August 2025.",
        "url": "https://grupounacem.com/en/noticias/grupo-unacem-and-grupo-calidra-begin-construction-of-a-lime-plant-with-an-initial-capacity-of-200000-tons-per-year-and-an-investment-of-us70-million/",
        "annotation": "Company primary on CALCEM Condorcocha lime plant USD 70m. Supports unacem_calcem_lime_peru_2025.",
        "supports": ["unacem_calcem_lime_peru_2025", "hunt_infra_building_materials"],
    },
)

# 3 energy/wind — miss (Goldwind Sento Sé / Envision Casa dos Ventos / IFC Olavarría already)

# 4 resources/water — Almar / Transelec Centinela seawater BOOT expansion
A(
    {
        "id": "almar_transelec_centinela_water_2024",
        "layer": "resources",
        "subcategory": "water",
        "side": "allied",
        "counterpart": "Almar Water Solutions / Transelec — Aguas Esperanza Centinela seawater BOOT",
        "country": "Chile",
        "asset": "Jun 2024 close: Minera Centinela transfers existing seawater transport assets/rights to Transelec–Almar consortium (Aguas Esperanza SpA) for ~USD 600 million cash proceeds; consortium undertakes planned parallel pipeline expansion (~144 km / +650 l/s) that removes ~USD 380 million of CAPEX from Centinela Second Concentrator budget. Almar (Jameel Environmental Services) describes ~USD 1.5 billion overall water-system investment including acquisition + new pipeline; ops of expanded system targeted ~2026 after ~20-month build",
        "investment_type": "ppp_concession",
        "value": "380000000",
        "currency": "USD",
        "value_usd": "380000000",
        "fx_usd": "1",
        "fx_date": "2024-06-04",
        "year": "2024",
        "status": "active",
        "lat": "-22.7",
        "lon": "-70.3",
        "geo_note": "Michilla–Centinela seawater corridor, Antofagasta Region (Almar/Antofagasta geography; approximate coastal pin).",
        "evidence": "documented",
        "source_id": "anto_centinela_water_transfer_2024",
        "note": "Actors: Almar Water Solutions (Spain / Jameel) + Transelec (Chile) — allied coding on Almar international water sponsor. Value stored as USD 380m expansion CAPEX shifted to consortium (Antofagasta completion release); USD 600m is asset-sale proceeds to Centinela (not entered as consortium CAPEX). Distinct from sacyr_coquimbo_desal_2026 and acciona_collahuasi_desal_chile.",
    },
    {
        "id": "almar_transelec_centinela_water_2024",
        "retrieved": "2026-10-01",
        "source_id": "anto_centinela_water_transfer_2024",
        "url": "https://www.antofagasta.co.uk/investors/news/2024/completion-of-process-to-transfer-centinelas-water-supply-infrastructure/",
        "price_year": "2024",
        "evidence": "documented",
        "quote": "Centinela’s existing water transportation assets and rights have been transferred to an international consortium formed of experienced partners, Transelec and Almar Water Solutions (“Almar”), with Centinela set to receive cash proceeds of $600 million during 2024. In addition, the planned expansion of the water transportation system will now be undertaken by the acquiring consortium, resulting in a reduction in the overall capital cost of the Centinela Second Concentrator Project by approximately $380 million",
        "note": "Opened Antofagasta plc English completion release. Almar company page corroborates ~USD 1.5bn overall system investment narrative.",
    },
    {
        "id": "anto_centinela_water_transfer_2024",
        "type": "company",
        "chicago": "Antofagasta plc. “Completion of Process to Transfer Centinela’s Water Supply Infrastructure.” June 2024.",
        "url": "https://www.antofagasta.co.uk/investors/news/2024/completion-of-process-to-transfer-centinelas-water-supply-infrastructure/",
        "annotation": "Company primary on Transelec–Almar Centinela seawater asset transfer and ~USD 380m expansion CAPEX shift. Supports almar_transelec_centinela_water_2024.",
        "supports": ["almar_transelec_centinela_water_2024", "hunt_res_water"],
    },
)

# 5 infrastructure/port_cranes — Paracas / TIL RTG+STS ITS
A(
    {
        "id": "paracas_rtg_sts_its_2026",
        "layer": "infrastructure",
        "subcategory": "port_cranes",
        "side": "allied",
        "counterpart": "Terminal Portuario Paracas (TIL/MSC) — 4th/5th RTG + STS tech mods ITS",
        "country": "Peru",
        "asset": "21 Sep 2026 Senace RD Nº 00106-2026-SENACE-PE/DEIN approves ITS for Terminal Portuario Paracas S.A. at Terminal Portuario General San Martín (Paracas, Pisco, Ica): add 4th and 5th RTG yard cranes, modify technical specs of two STS quay cranes, and reassign three free areas from EIA-d. Press citing the RD reports associated annual investment >USD 28 million. Terminal under TIL (MSC) control accelerating crane modernization",
        "investment_type": "equipment_supply",
        "value": "28000000",
        "currency": "USD",
        "value_usd": "28000000",
        "fx_usd": "1",
        "fx_date": "2026-09-21",
        "year": "2026",
        "status": "active",
        "lat": "-13.83",
        "lon": "-76.25",
        "geo_note": "Terminal Portuario General San Martín, Paracas / Pisco, Ica (Senace ITS geography).",
        "evidence": "proxy",
        "source_id": "energiminas_paracas_its_20260925",
        "note": "Actor: Terminal Portuario Paracas under TIL (Swiss MSC affiliate) — allied. UNVERIFIED proxy: USD figure from Energiminas Spanish report citing Senace RD (Senace HTML paywalled/password). Distinct from konecranes_yilport_acajutla_2026 and zpmc_santos_brasil_sts_rtg_2026.",
    },
    {
        "id": "paracas_rtg_sts_its_2026",
        "retrieved": "2026-10-01",
        "source_id": "energiminas_paracas_its_20260925",
        "url": "https://energiminas.com/2026/09/25/regulador-ambiental-aprueba-plan-de-us-28-millones-de-terminal-portuario-paracas-sa/",
        "price_year": "2026",
        "evidence": "proxy",
        "quote": "Mediante la Resolución Directoral Nº 00106-2026- SENACE-PE/DEIN del 21 de setiembre de 2026 … aprobó el Informe Técnico Sustentatorio (ITS) del proyecto “Implementación de dos Nuevas Grúas RTG (4ta y 5ta) y Modificación de Características Técnicas de dos (02) Grúas STS …”. … Implica un monto de inversión anual superior a los US$ 28 millones",
        "note": "Opened Energiminas Spanish report 25 Sep 2026 citing Senace RD number and ITS title/scope.",
    },
    {
        "id": "energiminas_paracas_its_20260925",
        "type": "press",
        "chicago": "Energiminas. “Regulador ambiental aprueba plan de US$ 28 millones de Terminal Portuario Paracas SA.” 25 September 2026.",
        "url": "https://energiminas.com/2026/09/25/regulador-ambiental-aprueba-plan-de-us-28-millones-de-terminal-portuario-paracas-sa/",
        "annotation": "Trade press citing Senace RD approving Paracas RTG/STS ITS at >USD 28m. Supports paracas_rtg_sts_its_2026 (proxy).",
        "supports": ["paracas_rtg_sts_its_2026", "hunt_infra_port_cranes"],
    },
)

# 6 energy/fission_smr — miss (Meitner / CAREM / Nuclearis / Angra standstill already)
# 7 energy/solar — miss (Trina Pillancó / YPF Luz already)
# 8 infrastructure/engineering_epc — miss (PowerChina UFN-III / Worley / STRACON already)
# 9 energy/other_renewables — miss (Lindsayca Borinquen / Ormat already)
# 10 infrastructure/port_ownership — miss (Marcona / HGT Aracruz already)
# 11 resources/graphite — miss (Graphcoa / South Star already)
# 12 resources/lithium — miss (Fénix 1B RIGI / Albemarle TED already)
# 13 energy/power_plants_grid — miss (avoid over-invest)
# 14 resources/balsa — miss
# 15 resources/nickel — miss (Jaguar JVEP logged C31)
# 16 infrastructure/bridges_roads — miss (Sacyr Ruta 57 / CRCC Talca already)

# 17 infrastructure/rail — OHLA Santiago Metro Line 9 civil
A(
    {
        "id": "ohla_metro_santiago_l9_2026",
        "layer": "infrastructure",
        "subcategory": "rail",
        "side": "allied",
        "counterpart": "OHLA — Santiago Metro Line 9 Sections 1C/1D shafts, galleries, tunnels",
        "country": "Chile",
        "asset": "27 Jul 2026: OHLA selected for civil works on shafts, galleries and tunnels for Sections 1C and 1D of future Santiago Metro Line 9 (Tramo 1); 7.6 km underground infrastructure; contract value EUR 144.3 million — company’s largest-ever Santiago Metro award. Follows Jun 2026 >EUR 70 million award for six new Line 7 stations; cumulative Santiago Metro portfolio >EUR 700 million across 12 interventions",
        "investment_type": "epc",
        "value": "144300000",
        "currency": "EUR",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-33.45",
        "lon": "-70.65",
        "geo_note": "Santiago Metro Line 9 Tramo 1 corridor (OHLA release; approximate Santiago pin).",
        "evidence": "documented",
        "source_id": "ohla_metro_l9_20260727",
        "note": "Actor: OHLA (Spain) — allied. Company English release 27 Jul 2026. EUR stored without FX conversion. Distinct from ohla_panama_panamericana_este_2025 (roads) and siemens_sonda_mexico_etcs_2026.",
    },
    {
        "id": "ohla_metro_santiago_l9_2026",
        "retrieved": "2026-10-01",
        "source_id": "ohla_metro_l9_20260727",
        "url": "https://www.ohla-group.com/en/ohla-secures-its-largest-ever-contract-for-the-santiago-metro-and-surpasses-e700-million-in-projects-across-the-network/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "OHLA … has been selected to carry out the civil works for shafts, galleries and tunnels in Sections 1C and 1D of the future Santiago Metro Line 9 in Chile. Valued at €144.3 million …",
        "note": "Opened OHLA Group English corporate press 27 Jul 2026.",
    },
    {
        "id": "ohla_metro_l9_20260727",
        "type": "company",
        "chicago": "OHLA Group. “OHLA secures its largest-ever contract for the Santiago Metro and surpasses €700 million in projects across the network.” 27 July 2026.",
        "url": "https://www.ohla-group.com/en/ohla-secures-its-largest-ever-contract-for-the-santiago-metro-and-surpasses-e700-million-in-projects-across-the-network/",
        "annotation": "Company primary on EUR 144.3m Santiago Metro Line 9 civil award. Supports ohla_metro_santiago_l9_2026.",
        "supports": ["ohla_metro_santiago_l9_2026", "hunt_latam_rail_telecom"],
    },
)

# 18 resources/niobium — miss (CBMM R$13bn / CMOC Catalão production already)


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

    # IDB Invest corroboration for CALCEM financing
    idb_bib = {
        "id": "idb_invest_calcem_15037",
        "type": "ifi",
        "chicago": "IDB Invest. “CALCEM - Increasing production capacity of lime in Peru.” Project 15037-01 (signed 15 December 2025).",
        "url": "https://idbinvest.org/en/projects/calcem-increasing-production-capacity-lime-peru",
        "annotation": "IDB Invest project page for up to USD 50m CALCEM Condorcocha lime loan. Corroborates unacem_calcem_lime_peru_2025.",
        "supports": ["unacem_calcem_lime_peru_2025", "hunt_infra_building_materials"],
    }
    if idb_bib["id"] not in bib_by:
        bib.append(idb_bib)

    hunt_updates = {
        "hunt_res_copper": "Cycle 32: logged antofagasta_centinela_2nd_conc_2023.",
        "hunt_infra_building_materials": "Cycle 32: logged unacem_calcem_lime_peru_2025.",
        "hunt_energy_wind": "Cycle 32: equal budget; Goldwind Sento Sé / Envision / IFC Olavarría already (miss).",
        "hunt_res_water": "Cycle 32: logged almar_transelec_centinela_water_2024.",
        "hunt_infra_port_cranes": "Cycle 32: logged paracas_rtg_sts_its_2026 (UNVERIFIED proxy >USD 28m).",
        "hunt_energy_fission_smr": "Cycle 32: equal budget; Meitner / CAREM / Nuclearis / Angra standstill already (miss).",
        "hunt_energy_solar": "Cycle 32: equal budget; Trina Pillancó / YPF Luz already (miss).",
        "hunt_infra_engineering_epc": "Cycle 32: equal budget; PowerChina / Worley / STRACON already (miss).",
        "hunt_energy_other_renewables": "Cycle 32: equal budget; Lindsayca Borinquen / Ormat already (miss).",
        "hunt_infra_port_ownership": "Cycle 32: equal budget; Marcona / HGT Aracruz already (miss).",
        "hunt_res_graphite": "Cycle 32: equal budget; Graphcoa / South Star already (miss).",
        "hunt_res_lithium": "Cycle 32: equal budget; Fénix 1B RIGI / Albemarle TED already (miss).",
        "hunt_br_power_equip": "Cycle 32: equal budget; avoid over-invest power_plants_grid (miss).",
        "hunt_res_balsa": "Cycle 32: equal budget; WITS/AIMA already (miss).",
        "hunt_res_nickel": "Cycle 32: equal budget; Jaguar JVEP logged C31 (miss).",
        "hunt_infra_bridges_roads": "Cycle 32: equal budget; Sacyr Ruta 57 / CRCC Talca already (miss).",
        "hunt_latam_rail_telecom": "Cycle 32: logged ohla_metro_santiago_l9_2026.",
        "hunt_fenb_araxa": "Cycle 32: equal budget; CBMM R$13bn logged C30 (miss).",
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
    print("Cycle 32 rows written/updated:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
