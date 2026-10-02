#!/usr/bin/env python3
"""Cycle 153 hunt: shuffle_seed=20261153; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: graphite, building_materials, port_cranes, lithium,
port_ownership, rail, solar, power_plants_grid, balsa, other_renewables,
engineering_epc, wind, copper, water, niobium, nickel, fission_smr, bridges_roads.

PRC ahead by 13 after 152 — keep equal US/PRC budget without padding.
Thin top-up: balsa/graphite then fission_smr/nickel (dry → niobium).
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
        fx_usd = "1" if value_usd and currency == "USD" else ""
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


# 1. other_renewables / us — AES Andes Solar IIb 180 MW PV + 112 MW/5h BESS COD
row_doc(
    "aes_andes_solar_iib_180mw_cod_2023",
    "energy",
    "other_renewables",
    "us",
    "AES Andes — Andes Solar IIb COD (180 MW PV + 112 MW / 5-hour BESS)",
    "Chile",
    "25 Jul 2023 AES Andes: commercial operation of Andes Solar IIb — 180 MW solar panels plus 112 MW lithium BESS for 5 hours (largest LatAm storage at announcement); ~230 km east of Antofagasta in Atacama Desert; includes 170 MW bifacial PV plus 10 MW 5B Maverick pilot; hub then 429 MW solar in Antofagasta Region. CapEx blank. Distinct from aes_andes_solar_iv_cod_2024 and aes_andes_solar_iii_hub_2026.",
    "",
    "",
    "2023",
    "-23.650",
    "-70.250",
    "Andes Solar Hub / Antofagasta Region, Chile (company geography; same approximate hub pin family).",
    "aes_andes_solar_iib_cod_20230725",
    "AES Andes today announced the commercial operation of Andes Solar IIb… The new plant will have a capacity of 180 MW of solar panels and a 112 MW battery storage system, the largest in Latin America… Located 230 kilometers east of Antofagasta, in the middle of the Atacama Desert… It has a capacity of 112 MW for 5 hours of energy, based on lithium batteries",
    "https://www.aesandes.com/en/press-release/historic-milestone-aes-andes-latin-americas-largest-solar-battery-storage-system-goes",
    "Actor: AES Andes / AES Corporation (U.S.) — us. Company English primary for COD capacities. CapEx blank. Hybrid PV+BESS coded other_renewables.",
    "hunt_energy_other_renewables",
    investment_type="greenfield",
    chicago='AES Andes. “Historic Milestone for AES Andes: Latin America’s Largest Solar Battery Storage System Goes into Operation.” July 25, 2023. https://www.aesandes.com/en/press-release/historic-milestone-aes-andes-latin-americas-largest-solar-battery-storage-system-goes.',
    annotation="AES Andes: Andes Solar IIb 180 MW + 112 MW/5h BESS COD. Supports aes_andes_solar_iib_180mw_cod_2023.",
    evid_note="Opened AES Andes Solar IIb COD primary (180 MW PV + 112 MW BESS; CapEx blank).",
)

# 2. other_renewables / us — AES Andes Virtual Reservoir II COD
row_doc(
    "aes_andes_virtual_reservoir_ii_cod_2023",
    "energy",
    "other_renewables",
    "us",
    "AES Andes — Virtual Reservoir II BESS COD (Alfalfal I; up to 197 MWh)",
    "Chile",
    "5 Dec 2023 AES Andes: commercial operation of Virtual Reservoir II — BESS for run-of-river hydro at Alfalfal I (Cordillera Complex, Metropolitan Region); stores up to 197 MWh of renewable energy for peak injection; Fluence Gridstack technology; company then cites 223 MW storage capacity in operation. CapEx blank. Distinct from aes_andes_alto_maipo_531mw_cod_2022 and Andes Solar IIb row.",
    "",
    "",
    "2023",
    "-33.550",
    "-70.300",
    "Alfalfal I / San José de Maipo, Metropolitan Region, Chile (AES Cordillera Complex naming).",
    "aes_andes_virtual_reservoir_ii_20231205",
    "AES Andes announced the entry into commercial operation of the second phase of the Virtual Reservoir… The new BESS system will allow the storage of up to 197 MWh of renewable energy produced by the Alfalfal I Hydroelectric Power Plant… Virtual Reservoir II is fitted with Fluence's Gridstack technology. Thanks to this milestone, the company now has 223 MW of storage capacity in operation",
    "https://www.aesandes.com/en/press-release/aes-andes-suma-nuevo-parque-de-almacenamiento-su-portafolio-y-afianza-liderazgo",
    "Actor: AES Andes / AES Corporation (U.S.) — us. Company English primary for VR II COD. CapEx blank. Fluence is equipment OEM (not dual-sided ownership).",
    "hunt_energy_other_renewables",
    investment_type="brownfield_storage",
    chicago='AES Andes. “AES Andes adds a new storage facility to its portfolio and strengthens its technological leadership in the region.” December 5, 2023. https://www.aesandes.com/en/press-release/aes-andes-suma-nuevo-parque-de-almacenamiento-su-portafolio-y-afianza-liderazgo.',
    annotation="AES Andes: Virtual Reservoir II COD (up to 197 MWh). Supports aes_andes_virtual_reservoir_ii_cod_2023.",
    evid_note="Opened AES Andes Virtual Reservoir II COD primary (CapEx blank).",
)

# 3. solar / prc — POWERCHINA Tamberías + Diaguitas (~USD 5m)
row_doc(
    "powerchina_tamberias_diaguitas_5m_2019",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Tamberías (3.6 MWp) + Diaguitas (2.4 MWp) solar (San Juan)",
    "Argentina",
    "POWERCHINA Argentina Sucursal: Tamberías and Diaguitas solar parks contracts signed 5 Feb 2019; both in San Juan Province; owner Latin American Energy; project amount approximately USD 5 million; completed end-2019 for generation and grid connection; Tamberías 3.6 MWp (~7,000 panels) in Calingasta; Diaguitas 2.4 MWp in Albardón. CapEx USD 5m is company “aproximadamente” figure — logged as UNVERIFIED proxy.",
    "5000000",
    "2019-02-05",
    "2019",
    "-31.350",
    "-68.550",
    "Tamberías (Calingasta) / Diaguitas (Albardón), San Juan Province, Argentina (POWERCHINA Sucursal naming; approximate mid-pin).",
    "powerchina_ar_tamberias_diaguitas",
    "Los dos proyectos de Parques Solares de Tamberías y Diaguitas fueron firmados el 5 de febrero de 2019… El monto del proyecto es de aproximadamente 5 millones de dólares. El proyecto se completó a finales de 2019… La planta fotovoltaica Tamberías cuenta con una potencia de 3,6 MWp… El Parque Solar Diaguitas, de 2,4 MWp",
    "https://www.powerchina.com.ar/tamberias.html",
    "Actor: POWERCHINA (PRC SOE) — prc. Company Argentina primary; CapEx approximately USD 5m — UNVERIFIED proxy.",
    "hunt_energy_solar",
    investment_type="epc",
    evidence="proxy",
    chicago='POWERCHINA Ltd. Sucursal Argentina. “Parque Solar Tamberías y Diaguitas.” https://www.powerchina.com.ar/tamberias.html.',
    annotation="POWERCHINA Argentina: Tamberías+Diaguitas ~6 MWp; ~USD 5m (proxy). Supports powerchina_tamberias_diaguitas_5m_2019.",
    evid_note="Opened POWERCHINA Argentina Tamberías/Diaguitas primary (~USD 5m approximate — UNVERIFIED proxy).",
)

# 4. bridges_roads / prc — CREC (TIESIJU) EGD Highway Bid 9 opening (Guyana)
row_doc(
    "crec_egd_highway_bid9_guyana_2023",
    "infrastructure",
    "bridges_roads",
    "prc",
    "CREC First Engineering Bureau (TIESIJU) — EGD Highway Bid 9 opening (Georgetown)",
    "Guyana",
    "2 Sep (CREC English, dated Oct 2023): EGD Highway Project in Guyana built by China TIESIJU Civil Engineering Group officially opened; President Irfaan Ali attended; project in Region 4 Georgetown from Eccles (East Bank Demerara) to Great Diamond; two-way four-lane divided into 12 sections; Bid 9 by CREC First Engineering Bureau totals 680 m (217 m asphalt concrete pavement 22.2 m wide; 463 m reinforced concrete pavement 21.2 m wide). CapEx blank on opened page. Distinct from crfg_guyana_east_coast_184m_2022 and crbc_corentyne_lot2_guyana_2026.",
    "",
    "",
    "2023",
    "6.800",
    "-58.130",
    "Eccles–Great Diamond / East Bank Demerara, Region 4, Guyana (CREC project naming; approximate corridor pin).",
    "crec_egd_highway_guyana_2023",
    "On September 2, local time, the EGD Highway Project in Guyana, which China TIESIJU Civil Engineering Group built, was officially opened to traffic… EGD Highway Project is located in the fourth district of Georgetown… starts from Eccles on the east bank of Demailala and ends at Great Diamond… The total length of the 9th bid constructed by The First Engineering Bureau of CREC is 680 meters",
    "https://www.crecg.com/zgztywz/cs11/10210606/2025021110100515448/index.html",
    "Actor: CREC / China TIESIJU Civil Engineering Group (PRC SOE) — prc. Company English primary for Bid 9 opening. CapEx blank.",
    "hunt_infra_bridges_roads",
    investment_type="epc",
    chicago='China Railway Group Limited. “The President of Guyana attended the opening ceremony of the EGD Highway project.” October 2023. https://www.crecg.com/zgztywz/cs11/10210606/2025021110100515448/index.html.',
    annotation="CREC/TIESIJU: EGD Highway Bid 9 Georgetown opening. Supports crec_egd_highway_bid9_guyana_2023.",
    evid_note="Opened CREC EGD Highway Bid 9 opening primary (CapEx blank).",
)


def upsert_bib(bib, bib_by, entry):
    eid = entry["id"]
    if eid in bib_by:
        existing = bib[bib_by[eid]]
        supports = list(existing.get("supports") or [])
        for s in entry.get("supports") or []:
            if s not in supports:
                supports.append(s)
        existing.update(entry)
        existing["supports"] = supports
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

    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in FIELDS})

    BIB.write_text(
        yaml.safe_dump(bib, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    print(f"Cycle 153 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
