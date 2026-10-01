#!/usr/bin/env python3
"""Cycle 49 hunt: shuffle_seed=20261049; equal budget; U.S. side ≥1/3; thin_topup after.

Order: other_renewables, power_plants_grid, graphite, niobium, solar, nickel, rail,
engineering_epc, water, lithium, bridges_roads, wind, balsa, port_cranes,
port_ownership, copper, fission_smr, building_materials.
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
# 2 energy/power_plants_grid — USTDA–ARCONEL power-generation TA (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ustda_ecuador_arconel_power_gen_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "USTDA / ARCONEL — technical assistance for private power-generation regulation",
        "country": "Ecuador",
        "asset": "25 Sep 2026: USTDA signs agreement with Ecuador’s ARCONEL to fund technical assistance developing regulations/procedures for greater private participation in power generation; Massachusetts-based The Innovation Network, LLC selected to deliver the study (best-practice review + adoption roadmap). Catalytic U.S. government TA toward generation investment — CAPEX USD not disclosed on page.",
        "investment_type": "financing",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-0.18",
        "lon": "-78.47",
        "geo_note": "Quito (ARCONEL HQ / national regulator pin).",
        "evidence": "documented",
        "source_id": "ustda_arconel_20260925",
        "note": "Actor: USTDA (U.S.) + U.S. contractor The Innovation Network — us. Company/agency release; grant amount not stated on opened page.",
    },
    {
        "id": "ustda_ecuador_arconel_power_gen_2026",
        "retrieved": "2026-10-01",
        "source_id": "ustda_arconel_20260925",
        "url": "https://ustda.gov/ustda-partners-with-ecuador-to-expand-private-investment-in-power-generation/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Today, USTDA signed an agreement with Ecuador’s Agency for the Regulation and Control of Electricity (ARCONEL) to fund technical assistance that will develop recommendations for regulations and procedures building on recent legal reforms that have opened the door to greater private sector participation in the sector. … ARCONEL has selected Massachusetts-based The Innovation Network, LLC … to carry out the technical assistance.",
        "note": "Opened USTDA 25 Sep 2026 ARCONEL release.",
    },
    {
        "id": "ustda_arconel_20260925",
        "type": "government",
        "chicago": "U.S. Trade and Development Agency. “USTDA Partners with Ecuador to Expand Private Investment in Power Generation.” 25 September 2026.",
        "url": "https://ustda.gov/ustda-partners-with-ecuador-to-expand-private-investment-in-power-generation/",
        "annotation": "USTDA primary on ARCONEL power-generation regulatory TA. Supports ustda_ecuador_arconel_power_gen_2026.",
        "supports": ["ustda_ecuador_arconel_power_gen_2026", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 2b energy/power_plants_grid — USTDA–CNEL EP ADMS TA (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ustda_ecuador_cnel_adms_2026",
        "layer": "energy",
        "subcategory": "power_plants_grid",
        "side": "us",
        "counterpart": "USTDA / CNEL EP — Advanced Distribution Management System technical assistance",
        "country": "Ecuador",
        "asset": "28 Jul 2026: USTDA and CNEL EP (Ecuador’s largest distributor, >2.7m customers) sign agreement for TA to advance next-generation ADMS deployment including AI modules; California-based Electric Power Research Institute (EPRI) selected. Distinct from ARCONEL generation-regulation TA.",
        "investment_type": "financing",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-2.19",
        "lon": "-79.89",
        "geo_note": "Guayaquil (CNEL EP primary coastal operations / HQ pin).",
        "evidence": "documented",
        "source_id": "ustda_cnel_adms_20260728",
        "note": "Actor: USTDA (U.S.) + EPRI (U.S.) — us. Agency release; grant amount not stated on opened page.",
    },
    {
        "id": "ustda_ecuador_cnel_adms_2026",
        "retrieved": "2026-10-01",
        "source_id": "ustda_cnel_adms_20260728",
        "url": "https://ustda.gov/ustda-deepens-u-s-ecuador-partnership-by-advancing-electricity-infrastructure/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "USTDA and the National Electricity Corporation (CNEL EP), Ecuador’s largest distribution company, has signed an agreement that will advance deployment of an Advanced Distribution Management System (ADMS) … CNEL EP selected California-based The Electric Power Research Institute, Inc. to conduct the assistance … CNEL EP provides electricity distribution service to more than 2.7 million residential, commercial, and industrial customers in Ecuador.",
        "note": "Opened USTDA 28 Jul 2026 CNEL EP ADMS release.",
    },
    {
        "id": "ustda_cnel_adms_20260728",
        "type": "government",
        "chicago": "U.S. Trade and Development Agency. “USTDA Deepens U.S.-Ecuador Partnership by Advancing Electricity Infrastructure.” 28 July 2026.",
        "url": "https://ustda.gov/ustda-deepens-u-s-ecuador-partnership-by-advancing-electricity-infrastructure/",
        "annotation": "USTDA primary on CNEL EP ADMS technical assistance. Supports ustda_ecuador_cnel_adms_2026.",
        "supports": ["ustda_ecuador_cnel_adms_2026", "hunt_br_power_equip"],
    },
)

# ---------------------------------------------------------------------------
# 3 resources/graphite — Atlas Malacacheta 11 km corridor consolidation (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "atlas_malacacheta_corridor_11km_2026",
        "layer": "resources",
        "subcategory": "graphite",
        "side": "us",
        "counterpart": "Atlas Critical Minerals — Malacacheta Graphite Project corridor consolidation",
        "country": "Brazil",
        "asset": "10 Mar 2026: Atlas Critical Minerals (NASDAQ: ATCX) acquires additional mineral right linking two existing NE Minas Gerais graphite tenements; combined Graphite Project ~2,822 ha (+124%) forming continuous >11 km mineralized corridor; peak chip sample 19.4% Cg. Distinct from atlas_malacacheta_aetc_nuclear_2025 (purification) and atlas_malacacheta_graphite_mre_2026 (maiden resource).",
        "investment_type": "ownership_equity",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-17.84",
        "lon": "-42.15",
        "geo_note": "Malacacheta Graphite Project, northeastern Minas Gerais (project pin; approximate).",
        "evidence": "documented",
        "source_id": "atlas_malacacheta_corridor_20260310",
        "note": "Actor: Atlas Critical Minerals (U.S.-listed NASDAQ: ATCX) — us. Company release; acquisition consideration USD not disclosed.",
    },
    {
        "id": "atlas_malacacheta_corridor_11km_2026",
        "retrieved": "2026-10-01",
        "source_id": "atlas_malacacheta_corridor_20260310",
        "url": "https://www.atlascriticalminerals.com/news/atlas-critical-minerals-consolidates-11-kilometer-graphite-corridor-in-brazil-reports-record-19-4-graphitic-carbon-results/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "Atlas Critical Minerals Corporation (NASDAQ: ATCX) … announces the acquisition of an additional mineral right that links its two existing graphite areas tenements in northeastern Minas Gerais, Brazil. The combined three mineral rights now comprise the Company’s Graphite Project, totaling approximately 2,822 hectares – an increase of approximately 124% – and establish a continuous mineralized corridor exceeding 11 kilometers … Systematic chip sampling returned a peak result of 19.4% graphitic carbon.",
        "note": "Opened Atlas Critical Minerals 10 Mar 2026 corridor consolidation release.",
    },
    {
        "id": "atlas_malacacheta_corridor_20260310",
        "type": "company",
        "chicago": "Atlas Critical Minerals Corporation. “Atlas Critical Minerals Consolidates 11-Kilometer Graphite Corridor in Brazil; Reports Record 19.4% Graphitic Carbon Results.” 10 March 2026.",
        "url": "https://www.atlascriticalminerals.com/news/atlas-critical-minerals-consolidates-11-kilometer-graphite-corridor-in-brazil-reports-record-19-4-graphitic-carbon-results/",
        "annotation": "Company primary on Malacacheta 2,822 ha / 11 km corridor consolidation. Supports atlas_malacacheta_corridor_11km_2026.",
        "supports": ["atlas_malacacheta_corridor_11km_2026", "hunt_res_graphite"],
    },
)

# ---------------------------------------------------------------------------
# 13 resources/balsa — Ecuador Estrategia Nacional de la Balsa (other)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ecuador_estrategia_nacional_balsa_2026",
        "layer": "resources",
        "subcategory": "balsa",
        "side": "other",
        "counterpart": "Ecuador MDEP — Estrategia Nacional de la Balsa (traceability / EUDR)",
        "country": "Ecuador",
        "asset": "21 Aug 2026: Ministerio de Desarrollo Económico y Productivo announces work on a National Balsa Strategy to strengthen georeferencing, legality, traceability and sustainability across the plantation-to-export chain for wind-blade core markets (China/Europe), with GIZ Ecuador workshop support in Guayaquil. Host-government governance angle — not a trade-flow or Plantabal duplicate; no CAPEX USD.",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "-2.17",
        "lon": "-79.92",
        "geo_note": "Guayaquil (MDEP/GIZ strategy workshop pin).",
        "evidence": "documented",
        "source_id": "expreso_estrategia_balsa_20260821",
        "note": "Actor: Ecuador MDEP (host) with GIZ support — other. Expreso 21 Aug 2026 citing MDEP comunicado. Press also cites AIMA 40% wood-export share and global balsa manufactures exports USD 301.3m in 2025 (context only; not dual-entered as trade row).",
    },
    {
        "id": "ecuador_estrategia_nacional_balsa_2026",
        "retrieved": "2026-10-01",
        "source_id": "expreso_estrategia_balsa_20260821",
        "url": "https://www.expreso.ec/economia-y-negocios/ecuador-prepara-estrategia-nacional-balsa-nuevas-exigencias-ue-293215.html",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "El Ministerio de Desarrollo Económico y Productivo (MDEP) anunció que trabaja en la construcción de una Estrategia Nacional de la Balsa, que demuestre de dónde proviene esta madera producida en el país y bajo qué condiciones, lo que fortalecerá los mecanismos de trazabilidad, georreferenciación, legalidad y sostenibilidad. … el MDEP con el apoyo de la Cooperación Alemana Ecuador (GIZ), desarrolló recientemente un taller técnico … en la ciudad de Guayaquil.",
        "note": "Opened Expreso coverage of MDEP National Balsa Strategy.",
    },
    {
        "id": "expreso_estrategia_balsa_20260821",
        "type": "press",
        "chicago": "López, Vanessa. “Ecuador prepara Estrategia Nacional de la Balsa ante nuevas exigencias de la UE.” Expreso, 21 August 2026.",
        "url": "https://www.expreso.ec/economia-y-negocios/ecuador-prepara-estrategia-nacional-balsa-nuevas-exigencias-ue-293215.html",
        "annotation": "Ecuador press citing MDEP National Balsa Strategy and GIZ workshop. Supports ecuador_estrategia_nacional_balsa_2026.",
        "supports": ["ecuador_estrategia_nacional_balsa_2026", "hunt_res_balsa"],
    },
)

# ---------------------------------------------------------------------------
# 17 energy/fission_smr — USTDA LAC civil nuclear delegation (U.S.)
# ---------------------------------------------------------------------------
A(
    {
        "id": "ustda_lac_nuclear_delegation_2026",
        "layer": "energy",
        "subcategory": "fission_smr",
        "side": "us",
        "counterpart": "USTDA — LAC civil nuclear partnership delegation (U.S. industry/ORNL)",
        "country": "El Salvador",
        "asset": "8 Jun 2026: USTDA brings 11 public-sector energy leaders from Colombia, Ecuador, El Salvador, Jamaica, and Paraguay to Washington/Knoxville (6–13 Jun) to view U.S. advanced civil nuclear technologies, meet U.S. firms/officials, and tour Oak Ridge National Laboratory; public business briefing 10 Jun. Program-level U.S. civil nuclear outreach — complements El Salvador NCMOU/123 and FIRST rows; pin El Salvador as named partner (multi-country delegation).",
        "investment_type": "other",
        "value": "",
        "currency": "USD",
        "value_usd": "",
        "fx_usd": "",
        "fx_date": "",
        "year": "2026",
        "status": "active",
        "lat": "13.69",
        "lon": "-89.19",
        "geo_note": "San Salvador (El Salvador partner pin for multi-country USTDA nuclear delegation).",
        "evidence": "documented",
        "source_id": "ustda_lac_nuclear_20260608",
        "note": "Actor: USTDA (U.S.) — us. Agency release; no reactor EPC CAPEX. Multi-country LAC partners listed on page.",
    },
    {
        "id": "ustda_lac_nuclear_delegation_2026",
        "retrieved": "2026-10-01",
        "source_id": "ustda_lac_nuclear_20260608",
        "url": "https://ustda.gov/ustda-connects-latin-america-and-the-caribbean-to-u-s-nuclear-energy-solutions/",
        "price_year": "2026",
        "evidence": "documented",
        "quote": "The U.S. Trade and Development Agency will bring a delegation of energy decision makers from Colombia, Ecuador, El Salvador, Jamaica, and Paraguay to the United States to build partnerships in support of developing Latin American and Caribbean civil nuclear capabilities. … Delegates will also visit the Oak Ridge National Laboratory and tour facilities developing cutting-edge nuclear energy technologies.",
        "note": "Opened USTDA 8 Jun 2026 LAC nuclear solutions release.",
    },
    {
        "id": "ustda_lac_nuclear_20260608",
        "type": "government",
        "chicago": "U.S. Trade and Development Agency. “USTDA Connects Latin America and the Caribbean to U.S. Nuclear Energy Solutions.” 8 June 2026.",
        "url": "https://ustda.gov/ustda-connects-latin-america-and-the-caribbean-to-u-s-nuclear-energy-solutions/",
        "annotation": "USTDA primary on LAC civil nuclear partnership delegation. Supports ustda_lac_nuclear_delegation_2026.",
        "supports": ["ustda_lac_nuclear_delegation_2026", "hunt_energy_fission_smr"],
    },
)


def upsert_bib(bib, bib_by, bib_entry):
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
        "hunt_energy_other_renewables": "Cycle 49: equal budget; ContourGlobal / CATL / AES Pampas already (miss).",
        "hunt_br_power_equip": "Cycle 49: logged ustda_ecuador_arconel_power_gen_2026 + ustda_ecuador_cnel_adms_2026 (U.S. USTDA TA).",
        "hunt_res_graphite": "Cycle 49: logged atlas_malacacheta_corridor_11km_2026 (U.S.; 2,822 ha / 11 km corridor).",
        "hunt_fenb_araxa": "Cycle 49: equal budget; CBMM 2025 spend / Codemig / St George already (miss).",
        "hunt_energy_solar": "Cycle 49: equal budget; ContourGlobal Víctor Jara COD just prior cycle (miss).",
        "hunt_res_nickel": "Cycle 49: equal budget; Jervois SMP restart / Westwin offtake already (miss).",
        "hunt_latam_rail_telecom": "Cycle 49: equal budget; CRRC Araraquara / PowerChina Chancay already (miss).",
        "hunt_infra_engineering_epc": "Cycle 49: equal budget; Ausenco SMP / Bechtel / Wabtec Contagem already (miss).",
        "hunt_res_water": "Cycle 49: equal budget; Barrick Pueblo Viejo ETP / Newmont Yanacocha already (miss).",
        "hunt_res_lithium": "Cycle 49: equal budget; PPG / Albemarle / EnergyX already (miss).",
        "hunt_infra_bridges_roads": "Cycle 49: equal budget; CHEC/Mota-Engil already (miss).",
        "hunt_energy_wind": "Cycle 49: equal budget; Envision/Vestas/Goldwind already (miss).",
        "hunt_res_balsa": "Cycle 49: logged ecuador_estrategia_nacional_balsa_2026 (other; national traceability strategy — not trade duplicate).",
        "hunt_infra_port_cranes": "Cycle 49: equal budget; SSA Guaymas/Manzanillo already (miss).",
        "hunt_infra_port_ownership": "Cycle 49: equal budget; SSA Guaymas TUM / DP World Caucedo just prior (miss).",
        "hunt_res_copper": "Cycle 49: equal budget; Southern Ilo smelter just prior (miss).",
        "hunt_energy_fission_smr": "Cycle 49: logged ustda_lac_nuclear_delegation_2026 (U.S.; LAC civil nuclear partnership delegation).",
        "hunt_infra_building_materials": "Cycle 49: equal budget; Holcim–Cemex Colombia already (miss).",
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
    print("Cycle 49 rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
