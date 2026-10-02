#!/usr/bin/env python3
"""Cycle 129 hunt: shuffle_seed=20261129; equal budget; U.S./PRC split; thin after.

Order: wind, graphite, engineering_epc, balsa, port_cranes, copper, lithium,
water, bridges_roads, solar, building_materials, niobium, other_renewables,
power_plants_grid, rail, nickel, fission_smr, port_ownership.

Sources: Hunt C96/C97 unlogged verified leads (ENDE Windey Warnes II; Vergnet
Claybury; Konecranes Arawak Nassau; BWA CRSEG South Coast; DOE Pattern Amanecer;
DOE AES Marahu).
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


def row_doc(
    rid,
    layer,
    subcategory,
    side,
    counterpart,
    country,
    asset,
    value,
    fx_date,
    year,
    lat,
    lon,
    geo,
    source_id,
    quote,
    url,
    note,
    hunt_support,
    investment_type="epc",
    evidence="documented",
    currency="USD",
    value_usd=None,
    fx_usd=None,
    chicago=None,
    bib_type="company",
    annotation=None,
    evid_note=None,
):
    if value_usd is None:
        value_usd = value if currency == "USD" and value else ""
    if fx_usd is None:
        fx_usd = "1" if value_usd else ""
    A(
        {
            "id": rid,
            "layer": layer,
            "subcategory": subcategory,
            "side": side,
            "counterpart": counterpart,
            "country": country,
            "asset": asset,
            "investment_type": investment_type,
            "value": value,
            "currency": currency,
            "value_usd": value_usd,
            "fx_usd": fx_usd,
            "fx_date": fx_date if value_usd else "",
            "year": year,
            "status": "active",
            "lat": lat,
            "lon": lon,
            "geo_note": geo,
            "evidence": evidence,
            "source_id": source_id,
            "note": note,
        },
        {
            "id": rid,
            "retrieved": "2026-10-02",
            "source_id": source_id,
            "url": url,
            "price_year": year,
            "evidence": evidence,
            "quote": quote,
            "note": evid_note or f"Opened primary source for {rid}.",
        },
        {
            "id": source_id,
            "type": bib_type,
            "chicago": chicago or f"Primary source supporting {rid}. {url}.",
            "url": url,
            "annotation": annotation or f"Primary source. Supports {rid}.",
            "supports": [rid, hunt_support],
        },
    )


# 1. wind / prc — ENDE Warnes II Windey turbines
row_doc(
    "windey_warnes_ii_bolivia_45mw_2025",
    "energy",
    "wind",
    "prc",
    "Windey — Warnes II 45 MW wind turbines (ENDE Bolivia)",
    "Bolivia",
    "30 Jan 2025 ENDE: aerogenerator structures for Parque Eólico Warnes II (Santa Cruz) arrive from China via Puerto Jennefer; lot includes Windey WD156-4500 turbines at 4.5 MW each; once assembled, 45 MW total to SIN; ~120 m hub height / ~200 t per machine; ENDE executes project. CapEx USD not disclosed on ENDE page.",
    "",
    "",
    "2025",
    "-17.520",
    "-63.165",
    "Parque Eólico Warnes II, municipio de Warnes, Santa Cruz, Bolivia (ENDE geography; approximate pin).",
    "ende_warnes_ii_windey_20250130",
    "El lote recibido incluye componentes clave de los aerogeneradores Windey WD156-4500, cada uno con una potencia de 4,5 megavatios (MW). Una vez ensamblados y operativizados, permitirán una producción adicional de 45 MW",
    "https://www.ende.bo/noticia/noticia/817",
    "Actor: Windey (PRC OEM) equipment for ENDE Corporación — prc. Official ENDE Spanish primary. CapEx blank.",
    "hunt_energy_wind",
    investment_type="equipment_supply",
    bib_type="government",
    chicago="Empresa Nacional de Electricidad (ENDE Corporación). “Aerogeneradores para Parque Eólico Warnes II llegan para aportar al cambio de la matriz energética en Bolivia.” 30 January 2025. https://www.ende.bo/noticia/noticia/817.",
    annotation="ENDE Spanish primary naming Windey WD156-4500 for Warnes II 45 MW. Supports windey_warnes_ii_bolivia_45mw_2025.",
)

# 2. wind / allied — Vergnet Claybury Barbados
row_doc(
    "vergnet_claybury_barbados_2025",
    "energy",
    "wind",
    "allied",
    "Vergnet SA — Claybury 875 kW wind (3× GEV MP-C)",
    "Barbados",
    "12 Jun 2023 Vergnet Actusnews: contract signed with Pavana Energy Ltd for supply, erection assistance, and commissioning of 3 medium-power turbines at Claybury (near Redland) totaling 875 kW for EUR 1.6 million; second Pavana project after Ashford. Nacelles shipped Feb 2025 (separate Actusnews). EUR stored; USD FX blank.",
    "1600000",
    "2023-06-12",
    "2023",
    "13.175",
    "-59.545",
    "Claybury wind farm near Redland, Barbados (Vergnet geography; approximate pin).",
    "vergnet_claybury_20230612",
    "a été signé un contrat de fourniture, d'assistance au montage et de mise en service de 3 éoliennes de moyenne puissance pour un montant de 1,6 M€. Située à Claybury… la puissance totale de la ferme éolienne est de 875 kW",
    "https://www.actusnews.com/fr/vergnet/cp/2023/06/12/un-nouveau-contrat-d_un-montant-de-1-6-m-eur",
    "Actor: Vergnet SA (France) — allied; buyer Pavana Energy Ltd. Company Actusnews wire. EUR CapEx; value_usd blank.",
    "hunt_energy_wind",
    investment_type="equipment_supply",
    currency="EUR",
    value_usd="",
    fx_usd="",
    bib_type="company",
    chicago="Vergnet SA. “Un nouveau contrat d’un montant de 1,6 M EUR.” Actusnews Wire, 12 June 2023. https://www.actusnews.com/fr/vergnet/cp/2023/06/12/un-nouveau-contrat-d_un-montant-de-1-6-m-eur.",
    annotation="Vergnet company wire: Claybury 875 kW / EUR 1.6m. Supports vergnet_claybury_barbados_2025.",
)

# 3. port_cranes / allied — Konecranes Arawak Nassau
row_doc(
    "konecranes_arawak_nassau_esp6_2024",
    "infrastructure",
    "port_cranes",
    "allied",
    "Konecranes — Gottwald ESP.6 MHC (Arawak Port Development / Port of Nassau)",
    "Bahamas",
    "11 Apr 2024 Konecranes: Arawak Port Development Limited (APD) ordered a Konecranes Gottwald ESP.6 mobile harbor crane for Port of Nassau — first at the port to run on mains power (zero emissions in operation); ordered Q1 2024; delivered Q3 2024; second Gottwald Gen 6 MHC after an existing unit. CapEx USD not disclosed.",
    "",
    "",
    "2024",
    "25.078",
    "-77.339",
    "Arawak Port Development terminal, Port of Nassau, Bahamas (Konecranes geography; approximate pin).",
    "konecranes_arawak_nassau_20240411",
    "Arawak Port Development Limited (APD) has ordered a Konecranes Gottwald ESP.6 mobile harbor crane to add substantial extra capacity to their terminal at the Port of Nassau. This crane will be the first at the port to run on mains power… ordered in Q1 2024 and will be delivered in Q3 2024",
    "https://www.konecranes.com/en-us/press-releases/bahamas-port-goes-electric-with-konecranes-gottwald-generation-6-mobile-harbor-crane",
    "Actor: Konecranes (Finland) — allied; buyer APD. Company English press. CapEx blank. Distinct from Caddell Nassau NEC.",
    "hunt_infra_port_cranes",
    investment_type="equipment_supply",
    bib_type="company",
    chicago="Konecranes. “Bahamas port goes electric with Konecranes Gottwald Generation 6 Mobile Harbor Crane.” 11 April 2024. https://www.konecranes.com/en-us/press-releases/bahamas-port-goes-electric-with-konecranes-gottwald-generation-6-mobile-harbor-crane.",
    annotation="Konecranes primary naming APD Nassau ESP.6 MHC. Supports konecranes_arawak_nassau_esp6_2024.",
)

# 4. water / prc — CRSEG Barbados South Coast
row_doc(
    "crseg_barbados_south_coast_water_2026",
    "resources",
    "water",
    "prc",
    "China Railway Shanghai Engineering Group — South Coast Water Reclamation Facility (Component 1)",
    "Barbados",
    "24 Jul 2026 BWA: South Coast Water Reclamation Project enters implementation; Component One (construction of South Coast Water Reclamation and Reuse Facility) contractor is China Railway Shanghai Engineering Group Co., Ltd. (CRSEG); AECOM is Contract Administrator; financing via IDB / EIB / GCF debt-for-climate arrangement. Contractor CapEx share not split on BWA page — value blank. Distinct from PowerChina Barbados water infrastructure handover.",
    "",
    "",
    "2026",
    "13.070",
    "-59.535",
    "South Coast Water Reclamation and Reuse Facility, Barbados (BWA project geography; approximate south-coast pin).",
    "bwa_crseg_south_coast_20260724",
    "China Railway Shanghai Engineering Group Co., Ltd. (CRSEG) is the contractor engaged to carry out the construction works under Component One. AECOM serves as Contract Administrator for this component",
    "https://barbadoswaterauthority.com/press-release-south-coast-water-reclamation-project-moves-into-implementation-phase/",
    "Actor: China Railway Shanghai Engineering Group (PRC SOE) — prc. Official BWA English primary. CapEx blank (contractor share undisclosed).",
    "hunt_res_water",
    investment_type="epc",
    bib_type="government",
    chicago="Barbados Water Authority. “Press Release – South Coast Water Reclamation Project Moves into Implementation Phase.” 24 July 2026. https://barbadoswaterauthority.com/press-release-south-coast-water-reclamation-project-moves-into-implementation-phase/.",
    annotation="BWA primary naming CRSEG as Component One contractor. Supports crseg_barbados_south_coast_water_2026.",
)

# 5. other_renewables / us — Pattern Amanecer DOE EDF
row_doc(
    "pattern_amanecer_doe_edf_489m_pr_2026",
    "energy",
    "other_renewables",
    "us",
    "Pattern Energy / Amanecer Puerto Rico LLC — DOE EDF USD 489m BESS loan (Arecibo & Santa Isabel)",
    "Puerto Rico",
    "Aug 2026: U.S. DOE Energy Dominance Financing Program closes USD 489 million loan to Amanecer Puerto Rico LLC (Pattern Energy subsidiary) for two stand-alone battery energy storage system projects totaling 220 MW in Arecibo and Santa Isabel, Puerto Rico. Distinct from Convergent / AES Marahu DOE LPO solar+storage packages.",
    "489000000",
    "2026-08-01",
    "2026",
    "18.450",
    "-66.390",
    "Arecibo and Santa Isabel BESS sites, Puerto Rico (DOE EDF project geography; Arecibo approximate pin).",
    "doe_edf_pattern_amanecer_202608",
    "In August 2026, EDF closed a $489 million loan to Amanecer Puerto Rico LLC, a subsidiary of Pattern Energy… two stand-alone battery energy storage system projects totaling 220 MW of energy in the municipalities of Arecibo and Santa Isabel",
    "https://www.energy.gov/edf/pattern-puerto-rico",
    "Actor: Pattern Energy (U.S.) via Amanecer Puerto Rico LLC — us; DOE EDF lender. Official DOE EDF project page.",
    "hunt_energy_other_renewables",
    investment_type="greenfield_storage",
    bib_type="government",
    chicago="U.S. Department of Energy, Energy Dominance Financing. “Pattern Puerto Rico.” August 2026. https://www.energy.gov/edf/pattern-puerto-rico.",
    annotation="DOE EDF primary: USD 489m Pattern Amanecer BESS. Supports pattern_amanecer_doe_edf_489m_pr_2026.",
)

# 6. solar / us — AES Marahu DOE LPO
row_doc(
    "aes_marahu_doe_lpo_861m_2024",
    "energy",
    "solar",
    "us",
    "AES / Clean Flexible Energy — DOE LPO USD 861.3m Marahu solar+storage (Guayama & Salinas)",
    "Puerto Rico",
    "Oct 2024: DOE Loan Programs Office closes USD 861.3 million loan guarantee to Clean Flexible Energy, LLC (sponsors AES Corporation and TotalEnergies Holdings USA) for Project Marahu — two solar PV farms with battery storage plus two standalone BESS in Guayama (Jobos) and Salinas, Puerto Rico. Distinct from Pattern Amanecer stand-alone BESS and Convergent Coamo package.",
    "861300000",
    "2024-10-01",
    "2024",
    "17.984",
    "-66.114",
    "Jobos (Guayama) and Salinas solar+storage sites, Puerto Rico (DOE LPO geography; Salinas approximate pin).",
    "doe_lpo_aes_marahu_202410",
    "In October 2024, LPO announced the closing of an $861.3 million loan guarantee to finance the construction of two solar photovoltaic (PV) farms equipped with battery storage and two standalone battery energy storage systems (BESS) in Puerto Rico… municipalities of Guayama (Jobos) and Salinas",
    "https://www.energy.gov/edf/aes-marahu",
    "Actor: AES Corporation (U.S.) co-sponsor via Clean Flexible Energy — us; TotalEnergies co-sponsor. Official DOE project page.",
    "hunt_energy_solar",
    investment_type="greenfield_generation",
    bib_type="government",
    chicago="U.S. Department of Energy, Loan Programs Office / Energy Dominance Financing. “AES MARAHU.” October 2024. https://www.energy.gov/edf/aes-marahu.",
    annotation="DOE primary: USD 861.3m AES Marahu solar+storage. Supports aes_marahu_doe_lpo_861m_2024.",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    if eid in bib_by:
        bib[bib_by[eid]].update(entry)
    else:
        bib.append(entry)
        bib_by[eid] = len(bib) - 1


def main() -> None:
    rows = list(csv.DictReader(CSV_PATH.open(encoding="utf-8")))
    by_id = {r["id"]: i for i, r in enumerate(rows)}
    bib = yaml.safe_load(BIB.read_text(encoding="utf-8")) or []
    if isinstance(bib, dict):
        bib = bib.get("sources") or bib.get("entries") or []
    bib_by = {e["id"]: i for i, e in enumerate(bib) if isinstance(e, dict) and "id" in e}
    added: list[str] = []

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
        "hunt_energy_wind": "Cycle 129: logged windey_warnes_ii_bolivia_45mw_2025 + vergnet_claybury_barbados_2025.",
        "hunt_res_graphite": "Cycle 129: equal budget; Graphcoa dense (miss). Thin dry — shift.",
        "hunt_infra_engineering_epc": "Cycle 129: equal budget; GTMO/PR residual dense this pass (miss).",
        "hunt_res_balsa": "Cycle 129: equal budget; Plantabal dense (miss). Thin dry — shift.",
        "hunt_infra_port_cranes": "Cycle 129: logged konecranes_arawak_nassau_esp6_2024.",
        "hunt_res_copper": "Cycle 129: equal budget; CMOC dense (miss).",
        "hunt_res_lithium": "Cycle 129: equal budget; Ganfeng dense (miss).",
        "hunt_res_water": "Cycle 129: logged crseg_barbados_south_coast_water_2026.",
        "hunt_infra_bridges_roads": "Cycle 129: equal budget; CRBC dense (miss).",
        "hunt_energy_solar": "Cycle 129: logged aes_marahu_doe_lpo_861m_2024.",
        "hunt_infra_building_materials": "Cycle 129: equal budget; Caribbean Lumber dense (miss).",
        "hunt_fenb_araxa": "Cycle 129: equal budget; CBMM dense (miss).",
        "hunt_energy_other_renewables": "Cycle 129: logged pattern_amanecer_doe_edf_489m_pr_2026.",
        "hunt_br_power_equip": "Cycle 129: equal budget; grid EPC dense (miss).",
        "hunt_latam_rail_telecom": "Cycle 129: equal budget; CRRC/Alstom dense (miss).",
        "hunt_res_nickel": "Cycle 129: equal budget; BRN dense (miss). Thin dry — shift.",
        "hunt_energy_fission_smr": "Cycle 129: equal budget; CAREM/FIRST dense (miss). Thin spare dry.",
        "hunt_infra_port_ownership": "Cycle 129: equal budget; COSCO/APM dense (miss).",
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
    print("Cycle 129 equal-pass rows added:", len(added))
    print("\n".join(added))


if __name__ == "__main__":
    main()
