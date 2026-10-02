#!/usr/bin/env python3
"""Cycle 146 hunt: shuffle_seed=20261146; equal budget; U.S./PRC split; thin after.

Canonical shuffle order: water, wind, port_ownership, bridges_roads, other_renewables,
rail, fission_smr, niobium, copper, graphite, solar, building_materials, port_cranes,
engineering_epc, nickel, lithium, balsa, power_plants_grid.

PRC ahead by 8 after 145 — keep equal US/PRC budget without padding.
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


# 1. wind / us — AES Andes Mesamávida 68 MW (Memoria capacity; first-stage COD 2022)
row_doc(
    "aes_andes_mesamavida_68mw_cod_2022",
    "energy",
    "wind",
    "us",
    "AES Andes — Mesamávida Wind Farm (Biobío, Chile)",
    "Chile",
    "AES Gener/Andes Memoria Anual 2020 lists Mesamávida at 68 MW (COD planned 2021); AES Andes English history: commencement of operation of the first stage of Mesamávida Wind Farm in 2022 (same Biobío hub as Los Olmos/Campo Lindo). CapEx blank. Distinct from aes_andes_los_olmos_110mw_cod_2022 and aes_andes_campo_lindo_cod_2023.",
    "",
    "",
    "2022",
    "-37.470",
    "-72.350",
    "Los Ángeles / Biobío Region, Chile (company Mesamávida geography; hub pin family).",
    "aes_andes_history_mesamavida_2022",
    "Commencement of operation of the first stage of the Mesamávida Wind Farm in Chile.",
    "https://www.aesandes.com/en/our-history",
    "Actor: AES Andes / AES Corporation (U.S.) — us. Company history primary for first-stage COD 2022; 68 MW nameplate from AES Gener Memoria Anual 2020 (MESAMÁVIDA 68MW). CapEx blank.",
    "hunt_energy_wind",
    investment_type="greenfield_generation",
    chicago='AES Andes. “Our history.” Accessed 2026. https://www.aesandes.com/en/our-history.',
    annotation="AES Andes history: Mesamávida first-stage COD 2022 (68 MW per Memoria 2020). Supports aes_andes_mesamavida_68mw_cod_2022.",
    evid_note="Opened AES Andes history (Mesamávida first-stage COD 2022); Memoria 2020 states 68 MW.",
)

# 2. rail / us — AECOM Panama–David railway master-plan advisory B/.2.2m
row_doc(
    "aecom_panama_david_master_plan_2p2m_2024",
    "infrastructure",
    "rail",
    "us",
    "AECOM USA — Panama–David–Frontera railway master-plan technical advisory",
    "Panama",
    "26 Dec 2024 Presidencia de la República: Secretaría Nacional del Ferrocarril signs technical-advisory contract with AECOM USA (Los Angeles HQ) for review/update of Tren Panamá–David–Frontera Master Plan — B/.2.2 million; 210 calendar days; phases 1–2 B/.1,117,080 each + optional phase 3 B/.685,709.50. CapEx = stated contract amount (B/. = USD 1:1).",
    "2200000",
    "2024-12-26",
    "2024",
    "8.983",
    "-79.520",
    "Panama City (Palacio de las Garzas signing; corridor Panama–David–Paso Canoas).",
    "presidencia_panama_aecom_ferrocarril_20241226",
    "La Secretaría Nacional del Ferrocarril de Panamá ha firmado un contrato de asesoría técnica por B/.2.2 millones con la empresa estadounidense AECOM USA, para la revisión y actualización del Plan Maestro del Tren Panamá-David-Frontera.",
    "https://www.presidencia.gob.pa/publicacion/contratan-empresa-para-actualizar-el-plan-maestro-del-tren-panama-david-frontera",
    "Actor: AECOM USA (U.S. HQ Los Angeles) — us. Official Presidencia primary. Distinct from later Gabinete USD 4.17m feasibility follow-on (2026).",
    "hunt_infra_rail",
    investment_type="services_contract",
    bib_type="government",
    chicago='Presidencia de la República de Panamá. “Contratan empresa para actualizar el Plan Maestro del Tren Panamá-David-Frontera.” December 26, 2024. https://www.presidencia.gob.pa/publicacion/contratan-empresa-para-actualizar-el-plan-maestro-del-tren-panama-david-frontera.',
    annotation="Presidencia Panama: AECOM USA B/.2.2m Panama–David master-plan advisory. Supports aecom_panama_david_master_plan_2p2m_2024.",
    evid_note="Opened Presidencia Panama release 26 Dec 2024 (AECOM B/.2.2m master-plan contract).",
)

# 3. wind / prc — Goldwind Lomas de Taltal 342 MW full turbine installation (Dec 2024)
row_doc(
    "goldwind_lomas_taltal_342mw_install_2024",
    "energy",
    "wind",
    "prc",
    "Goldwind — Lomas de Taltal Wind Farm turbine installation (ENGIE Chile)",
    "Chile",
    "11 Mar 2025 Goldwind English: in Dec 2024 Goldwind and ENGIE Chile completed full turbine installation at Lomas de Taltal Wind Project in Atacama Desert / Antofagasta — 57 × GW165-6.0 MW turbines totaling 342 MW. CapEx blank on Goldwind install wrap (ENGIE Hecho Esencial earlier disclosed ~USD 450m full-project budget including non-turbine works — not entered as Goldwind contract USD). Distinct from goldwind_pemuco_chile (165 MW supply).",
    "",
    "",
    "2024",
    "-25.400",
    "-70.480",
    "Taltal commune, Antofagasta Region, Chile (ENGIE/Goldwind project geography).",
    "goldwind_lomas_taltal_install_20250311",
    "In December 2024, Goldwind and ENGIE Chile successfully completed the full turbine installation at the Lomas de Taltal Wind Project… Goldwind successfully installed 57 units of GW165-6.0MW turbines at this site, totaling 342MW in capacity.",
    "https://www.goldwind.com/en/news/focus-1117920264764704768/?id=1117922476714815488",
    "Actor: Goldwind (PRC) turbine OEM — prc; owner ENGIE Chile (allied) not dual-sided. Company English primary. CapEx blank (full-park USD 450m is ENGIE project budget, not OEM contract).",
    "hunt_energy_wind",
    investment_type="equipment_supply",
    chicago='Goldwind. “Goldwind Signs Contract with ENGIE Chile to Jointly Construct the Pemuco Wind Farm Project in Chile.” March 11, 2025 (includes Lomas de Taltal installation wrap). https://www.goldwind.com/en/news/focus-1117920264764704768/?id=1117922476714815488.',
    annotation="Goldwind primary: Lomas de Taltal 57×6.0 MW / 342 MW full installation Dec 2024. Supports goldwind_lomas_taltal_342mw_install_2024.",
    evid_note="Opened Goldwind EN release 11 Mar 2025 (Lomas de Taltal 342 MW install Dec 2024).",
)

# 4. solar / prc — POWERCHINA Cafayate Argentina 97.6 MW EPC (Canadian Solar owner)
row_doc(
    "powerchina_cafayate_argentina_97p6mw_epc",
    "energy",
    "solar",
    "prc",
    "POWERCHINA — Parque Solar Cafayate EPC (Salta, Argentina)",
    "Argentina",
    "POWERCHINA Argentina branch: Canadian Solar (owner of Parque Solar Cafayate, 97.6 MW) contracted POWERCHINA under EPC modality for full project execution — first solar park in Salta Province; site north of Cafayate on RN 40; commercial operation scheduled mid-2019. CapEx blank on branch page. Distinct from powerchina_cauchari_solar_epc_2020.",
    "",
    "",
    "2019",
    "-26.070",
    "-65.980",
    "North of Cafayate, Salta Province, Argentina (company geography; RN 40).",
    "powerchina_ar_cafayate_epc",
    "Recientemente la Empresa Canadian Solar, propietaria del Parque Solar Cafayate de 97,6 Mw, ha contratado a POWERCHINA para ejecutar el proyecto bajo la modalidad EPC… Es el primer parque de energía solar que se construya en la provincia de Salta.",
    "https://www.powerchina.com.ar/cafayate.html",
    "Actor: POWERCHINA (PRC SOE) — prc; owner Canadian Solar (Canada/China-listed module maker — not dual-sided). Company Argentina branch primary. CapEx blank.",
    "hunt_energy_solar",
    investment_type="epc",
    chicago='POWERCHINA Ltd. Sucursal Argentina. “Parque Solar Cafayate.” Accessed 2026. https://www.powerchina.com.ar/cafayate.html.',
    annotation="POWERCHINA Argentina: Cafayate 97.6 MW EPC for Canadian Solar. Supports powerchina_cafayate_argentina_97p6mw_epc.",
    evid_note="Opened POWERCHINA Argentina Cafayate project page (97.6 MW EPC).",
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
    print(f"Cycle 146 added {len(added)} rows: {added}")


if __name__ == "__main__":
    main()
